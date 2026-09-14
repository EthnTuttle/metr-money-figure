#!/usr/bin/env python3
"""Build the AUDIT-3D row scope and fetch its cited source URLs.

All outputs are bounded: source CSVs are limited to 5 MiB each, the figure HTML
to 2 MiB, and each fetched response to 50 MiB.  The register is CSV so no
general object graph is serialized.
"""

from __future__ import annotations

import csv
import hashlib
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlsplit


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
FIGURE = ROOT / "figures" / "metr-01b-money-that-doesnt-show-up-with-anthropic.html"
MAX_CSV = 5 * 1024 * 1024
MAX_HTML = 2 * 1024 * 1024
MAX_FETCH = 50 * 1024 * 1024

SOURCE_FILES = {
    "M": ROOT / "research" / "money_flows.csv",
    "ST": ROOT / "research" / "stakes.csv",
    "IV": ROOT / "research" / "investments.csv",
    "LD": ROOT / "research" / "share_ladder.csv",
    "TB": ROOT / "research" / "tarbell_funding.csv",
    "TO": ROOT / "research" / "tarbell_outlets.csv",
    "K": ROOT / "research" / "compute_inkind.csv",
    "S": ROOT / "research" / "staff_origins.csv",
    "G": ROOT / "research" / "budget.csv",
    "J": ROOT / "research" / "shared_donors.csv",
    "RW": ROOT / "research" / "redwood.csv",
    "AP": ROOT / "research" / "audacious-partners.csv",
}

URL_FIELDS = ("source_url", "url", "lab_source_url", "metr_source_url")
URL_RE = re.compile(r"https?://[^\s;,)]+")
ID_RE = re.compile(r"\b[A-Z]{1,2}\d{2,3}\b")
RANGE_RE = re.compile(r"\b([A-Z]{1,2})(\d{2,3})[–-](?:([A-Z]{1,2}))?(\d{2,3})\b")


def bounded_text(path: Path, limit: int) -> str:
    size = path.stat().st_size
    if size > limit:
        raise RuntimeError(f"input exceeds limit: {path} ({size} > {limit})")
    return path.read_text(encoding="utf-8-sig")


def prefix(row_id: str) -> str:
    match = re.match(r"[A-Z]+", row_id)
    if not match:
        raise RuntimeError(f"bad row id: {row_id}")
    return match.group(0)


def scope_ids() -> list[str]:
    text = re.sub(r"<[^>]+>", " ", bounded_text(FIGURE, MAX_HTML))
    ids = set(ID_RE.findall(text))
    for match in RANGE_RE.finditer(text):
        p1, start, p2, end = match.groups()
        p2 = p2 or p1
        if p1 == p2:
            ids.update(f"{p1}{number:02d}" for number in range(int(start), int(end) + 1))
    return sorted(ids, key=lambda item: (prefix(item), int(re.search(r"\d+", item).group())))


def load_rows(ids: list[str]) -> list[dict[str, str]]:
    by_prefix: dict[str, list[str]] = {}
    for row_id in ids:
        by_prefix.setdefault(prefix(row_id), []).append(row_id)
    found: dict[str, dict[str, str]] = {}
    for pfx, wanted in by_prefix.items():
        path = SOURCE_FILES[pfx]
        text = bounded_text(path, MAX_CSV)
        reader = csv.DictReader(text.splitlines())
        for row in reader:
            row_id = (row.get("row_id") or "").strip()
            if row_id in wanted:
                row["_source_csv"] = str(path.relative_to(ROOT))
                found[row_id] = row
    missing = [row_id for row_id in ids if row_id not in found]
    if missing:
        raise RuntimeError(f"missing scoped rows: {missing}")
    return [found[row_id] for row_id in ids]


def extract_urls(row: dict[str, str]) -> list[str]:
    urls: list[str] = []
    for field in URL_FIELDS:
        urls.extend(URL_RE.findall(row.get(field, "")))
    return list(dict.fromkeys(urls))


def transformed_fetches(source_url: str) -> list[tuple[str, str]]:
    attempts = [("direct", source_url)]
    parts = urlsplit(source_url)
    host = parts.netloc.lower()
    if host in {"x.com", "twitter.com", "www.x.com", "www.twitter.com"}:
        status_id = re.search(r"/status/(\d+)", parts.path)
        if status_id:
            attempts.append(("fxtwitter-api", f"https://api.fxtwitter.com/status/{status_id.group(1)}"))
    if host == "bsky.app":
        match = re.search(r"/profile/([^/]+)/post/([^/?#]+)", parts.path)
        if match:
            handle, rkey = match.groups()
            uri = f"at://{handle}/app.bsky.feed.post/{rkey}"
            attempts.append(("bluesky-api", "https://public.api.bsky.app/xrpc/app.bsky.feed.getPostThread?uri=" + quote(uri, safe="")))
    if host in {
        "www.forbes.com",
        "www.forbes.com.au",
        "www.wsj.com",
        "coefficientgiving.org",
        "www.coefficientgiving.org",
        "www.aripaev.ee",
        "majandus.postimees.ee",
    }:
        attempts.append(("jina", "https://r.jina.ai/http://" + source_url.split("://", 1)[1]))
    return attempts


def fetch_one(item: tuple[str, str, str, str]) -> dict[str, str]:
    row_ids, source_url, method, fetch_url = item
    digest = hashlib.sha256(fetch_url.encode("utf-8")).hexdigest()[:20]
    suffix = Path(urlsplit(fetch_url).path).suffix.lower()
    if suffix not in {".pdf", ".xml", ".json", ".csv", ".txt", ".html", ".htm"}:
        suffix = ".bin"
    artifact = OUT / f"fetch-{digest}{suffix}"
    result = subprocess.run(
        [
            "curl",
            "--location",
            "--compressed",
            "--silent",
            "--show-error",
            "--connect-timeout",
            "8",
            "--max-time",
            "25",
            "--retry",
            "1",
            "--max-filesize",
            str(MAX_FETCH),
            "--user-agent",
            "Mozilla/5.0 AUDIT-3D fetch-only source review",
            "--output",
            str(artifact),
            "--write-out",
            "%{http_code}\t%{content_type}\t%{size_download}",
            fetch_url,
        ],
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    timestamp = datetime.now(timezone.utc).isoformat()
    http_code = "000"
    content_type = ""
    size = "0"
    if result.stdout:
        values = result.stdout.rsplit("\t", 2)
        if len(values) == 3:
            http_code, content_type, size = values
    if artifact.exists():
        body = artifact.read_bytes()
        if len(body) > MAX_FETCH:
            raise RuntimeError(f"response exceeds limit after fetch: {fetch_url}")
        sha256 = hashlib.sha256(body).hexdigest()
        relative = str(artifact.relative_to(ROOT))
    else:
        sha256 = ""
        relative = ""
    status = f"curl={result.returncode};http={http_code};bytes={size}"
    if result.stderr.strip():
        status += ";error=" + " ".join(result.stderr.split())[:240]
    return {
        "row_ids": row_ids,
        "source_url": source_url,
        "fetch_method": method,
        "fetch_url": fetch_url,
        "utc": timestamp,
        "status": status,
        "content_type": content_type,
        "sha256": sha256,
        "artifact": relative,
    }


def write_scope(rows: list[dict[str, str]]) -> None:
    fields = ["row_id", "source_csv", "source_urls", "claim", "amount_or_value", "measure_or_type", "quote"]
    with (OUT / "scope-rows.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "row_id": row["row_id"],
                    "source_csv": row["_source_csv"],
                    "source_urls": " | ".join(extract_urls(row)),
                    "claim": row.get("statement") or row.get("purpose") or row.get("value") or row.get("what") or row.get("title") or row.get("investor") or row.get("outlet") or "",
                    "amount_or_value": row.get("amount_usd") or row.get("value") or row.get("n_tarbell_ai") or "",
                    "measure_or_type": row.get("measure") or row.get("claim_type") or row.get("source_type") or "",
                    "quote": row.get("quote_verbatim") or row.get("quote") or row.get("notes") or row.get("note") or "",
                }
            )


def local_register(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    targets: dict[Path, set[str]] = {FIGURE: set()}
    for row in rows:
        targets.setdefault(ROOT / row["_source_csv"], set()).add(row["row_id"])
        for field in URL_FIELDS:
            value = row.get(field, "").strip()
            if not value or value.startswith("http"):
                continue
            for token in re.split(r"[;|]", value):
                token = token.strip().split(" (", 1)[0]
                if not token:
                    continue
                candidate = Path(token)
                if not candidate.is_absolute():
                    candidate = ROOT / candidate
                if candidate.is_file():
                    targets.setdefault(candidate, set()).add(row["row_id"])
    stamp = datetime.now(timezone.utc).isoformat()
    records = []
    for path, row_ids in sorted(targets.items(), key=lambda item: str(item[0])):
        data = path.read_bytes()
        records.append(
            {
                "row_ids": " ".join(sorted(row_ids)),
                "source_url": path.as_uri(),
                "fetch_method": "local-authority",
                "fetch_url": path.as_uri(),
                "utc": stamp,
                "status": f"local;bytes={len(data)}",
                "content_type": "application/octet-stream",
                "sha256": hashlib.sha256(data).hexdigest(),
                "artifact": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
            }
        )
    return records


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ids = scope_ids()
    rows = load_rows(ids)
    write_scope(rows)

    urls: dict[str, set[str]] = {}
    for row in rows:
        for url in extract_urls(row):
            urls.setdefault(url, set()).add(row["row_id"])
    queue: list[tuple[str, str, str, str]] = []
    for source_url, row_ids in sorted(urls.items()):
        joined = " ".join(sorted(row_ids))
        for method, fetch_url in transformed_fetches(source_url):
            queue.append((joined, source_url, method, fetch_url))

    records = local_register(rows)
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(fetch_one, item) for item in queue]
        for future in as_completed(futures):
            records.append(future.result())
    records.sort(key=lambda row: (row["source_url"], row["fetch_method"], row["fetch_url"]))
    fields = ["row_ids", "source_url", "fetch_method", "fetch_url", "utc", "status", "content_type", "sha256", "artifact"]
    with (OUT / "fetch-register.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)
    print(f"scope_rows={len(rows)} unique_source_urls={len(urls)} fetch_attempts={len(queue)} register_rows={len(records)}")


if __name__ == "__main__":
    main()
