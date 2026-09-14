#!/usr/bin/env python3
"""Fetch and register the primary sources required by AUDIT-SEED-3C."""

from __future__ import annotations

import csv
import gzip
import hashlib
import os
import shutil
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REGISTER = ROOT / "fetch-register.csv"
MAX_BYTES = 50_000_000
USER_AGENT = "Mozilla/5.0 (compatible; audit3c/1.0; research capture)"

REMOTE = [
    (
        "canary/rand-press-2024-10-09.html",
        "https://www.rand.org/news/press/2024/10/09.html",
    ),
    (
        "canary/metr-new-support-2024-10-09.html",
        "https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/",
    ),
    (
        "canary/barnes-shortform-2025-09-28.html",
        "https://www.greaterwrong.com/posts/yrephKDBFL6h9zAFv/beth-barnes-s-shortform/comment/w3e6cbHeozQJaJH5c",
    ),
    (
        "filings/high-tide-ty2024-202503179349100135.xml",
        "https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202503179349100135_public.xml",
    ),
    (
        "filings/high-tide-propublica.html",
        "https://projects.propublica.org/nonprofits/organizations/201164239",
    ),
    (
        "filings/ted-foundation-propublica.html",
        "https://projects.propublica.org/nonprofits/organizations/821934592",
    ),
    (
        "filings/ted-foundation-ty2021-202242949349100909.xml",
        "https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202242949349100909_public.xml",
    ),
    (
        "filings/ted-foundation-ty2022-202322779349100017.xml",
        "https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202322779349100017_public.xml",
    ),
    (
        "filings/ted-foundation-ty2023-202442359349100919.xml",
        "https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202442359349100919_public.xml",
    ),
    (
        "filings/ted-foundation-ty2024-202502549349100435.xml",
        "https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202502549349100435_public.xml",
    ),
    (
        "partners/audacious-about-live.html",
        "https://www.audaciousproject.org/about",
    ),
    (
        "partners/audacious-faq-live.html",
        "https://www.audaciousproject.org/faq",
    ),
    (
        "partners/audacious-about-wayback-20241009220522.html",
        "https://web.archive.org/web/20241009220522id_/https://www.audaciousproject.org/about",
    ),
    (
        "rand/rand-cast-funding.html",
        "https://www.rand.org/global-and-emerging-risks/centers/ai-security-and-technology/funding.html",
    ),
    (
        "rand/rand-canary-project.html",
        "https://www.rand.org/global-and-emerging-risks/centers/ai-security-and-technology/projects/canary.html",
    ),
    (
        "rand/rand-annual-report-2024.pdf",
        "https://www.rand.org/content/dam/rand/pubs/corporate_pubs/CPA1000/CPA1065-5/RAND_CPA1065-5.pdf",
    ),
    (
        "tarbell/coefficient-training-for-good.html",
        "https://coefficientgiving.org/grants/training-for-good-operating-costs-and-tarbell-fellowship/",
    ),
    (
        "tarbell/coefficient-general-support-3.html",
        "https://coefficientgiving.org/grants/general-support-3/",
    ),
    (
        "tarbell/coefficient-operating-costs.html",
        "https://coefficientgiving.org/grants/operating-costs/",
    ),
    (
        "tarbell/coefficient-general-support-49.html",
        "https://coefficientgiving.org/grants/general-support-49/",
    ),
    (
        "tarbell/sff-2024-recommendations.html",
        "https://survivalandflourishing.fund/2024/recommendations",
    ),
    (
        "tarbell/sff-2025-recommendations.html",
        "https://survivalandflourishing.fund/2025/recommendations",
    ),
]

LOCAL = [
    (
        "filings/valhalla-ty2024-202502559349100000.xml",
        Path("research/990pf-valhalla-ty2024-202502559349100000.xml"),
    ),
    (
        "tarbell/coefficient-index-2026-09-11.json",
        Path("/mnt/f/projects/memes/anthropic-investors/research/04-openphil-grants-raw-2026-09-11.json"),
    ),
    (
        "filings/goodventures-fye2024-202501349349105365.xml",
        Path("research/990pf-goodventures-202501349349105365.xml"),
    ),
    (
        "filings/goodventures-fye2025-202641359349102829.xml",
        Path("research/990pf-goodventures-202641359349102829.xml"),
    ),
    (
        "outlets/outlet_windows.csv",
        Path("/mnt/f/projects/memes/ai-machine/01-tarbell-bylines/research/outlet_windows.csv"),
    ),
    (
        "outlets/article-inventory.csv",
        Path("/mnt/f/projects/memes/ai-machine/01-tarbell-bylines/research/article-inventory.csv"),
    ),
    (
        "outlets/roster.csv",
        Path("/mnt/f/projects/memes/ai-machine/01-tarbell-bylines/research/roster.csv"),
    ),
    (
        "outlets/denominators/time.csv",
        Path("/mnt/f/projects/memes/ai-machine/01-tarbell-bylines/research/denominators/time.csv"),
    ),
    (
        "outlets/denominators/mit-technology-review.csv",
        Path("/mnt/f/projects/memes/ai-machine/01-tarbell-bylines/research/denominators/mit-technology-review.csv"),
    ),
    (
        "outlets/denominators/lawfare.csv",
        Path("/mnt/f/projects/memes/ai-machine/01-tarbell-bylines/research/denominators/lawfare.csv"),
    ),
    (
        "outlets/denominators/bloomberg.csv",
        Path("/mnt/f/projects/memes/ai-machine/01-tarbell-bylines/research/denominators/bloomberg.csv"),
    ),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def fetch(url: str) -> tuple[str, bytes]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise RuntimeError(f"response exceeds {MAX_BYTES} bytes")
            if data.startswith(b"\x1f\x8b"):
                data = gzip.decompress(data)
            return str(response.status), data
    except urllib.error.HTTPError as exc:
        data = exc.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise RuntimeError(f"error response exceeds {MAX_BYTES} bytes")
        if data.startswith(b"\x1f\x8b"):
            data = gzip.decompress(data)
        return str(exc.code), data


def main() -> None:
    rows: list[dict[str, str]] = []
    for relative, url in REMOTE:
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        stamp = utc_now()
        try:
            status, data = fetch(url)
            path.write_bytes(data)
            rows.append(
                {
                    "url": url,
                    "utc": stamp,
                    "status": status,
                    "sha256": digest(data),
                    "bytes": str(len(data)),
                    "path": str(path.relative_to(ROOT)),
                }
            )
        except Exception as exc:
            rows.append(
                {
                    "url": url,
                    "utc": stamp,
                    "status": f"ERROR: {type(exc).__name__}: {exc}",
                    "sha256": "",
                    "bytes": "0",
                    "path": str(path.relative_to(ROOT)),
                }
            )

    for relative, source in LOCAL:
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        stamp = utc_now()
        try:
            shutil.copyfile(source, path)
            data = path.read_bytes()
            rows.append(
                {
                    "url": str(source),
                    "utc": stamp,
                    "status": "LOCAL COPY",
                    "sha256": digest(data),
                    "bytes": str(len(data)),
                    "path": str(path.relative_to(ROOT)),
                }
            )
        except Exception as exc:
            rows.append(
                {
                    "url": str(source),
                    "utc": stamp,
                    "status": f"ERROR: {type(exc).__name__}: {exc}",
                    "sha256": "",
                    "bytes": "0",
                    "path": str(path.relative_to(ROOT)),
                }
            )

    temporary = REGISTER.with_suffix(".tmp")
    with temporary.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=["url", "utc", "status", "sha256", "bytes", "path"]
        )
        writer.writeheader()
        writer.writerows(rows)
    os.replace(temporary, REGISTER)
    for row in rows:
        print(row["status"], row["path"], row["bytes"], row["sha256"][:12])


if __name__ == "__main__":
    main()
