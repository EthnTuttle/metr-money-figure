#!/usr/bin/env python3
"""Refresh hashes for local authority and retained-primary files."""

from __future__ import annotations

import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
REGISTER = OUT / "fetch-register.csv"
MAX_FILE = 100 * 1024 * 1024
MAX_TOTAL = 1024 * 1024 * 1024
FIELDS = ["row_ids", "source_url", "fetch_method", "fetch_url", "utc", "status", "content_type", "sha256", "artifact"]

PATTERNS = [
    "figures/metr-01*.html",
    "figures/metr-01*.png",
    "figures/metr-26*.html",
    "figures/metr-27*.html",
    "README.md",
    "research/*.csv",
    "research/AUDIT-3D.md",
    "research/990*.xml",
    "research/agents-2026-09-14/S11-stakes/docs/*",
    "research/audit3-evidence/3d/*.csv",
    "research/audit3-evidence/3d/*.png",
    "research/audit3-evidence/3d/*.py",
    "research/audit3-evidence/3d/*.txt",
    "research/coefficient-pages/*",
    "research/daf-sponsors/*",
    "research/independence/coefficient-2026-09-09-urgently-scaling.*",
    "research/moskovitz-words/*",
    "research/press-pdfs/aripaev-2026-01-05-*",
    "research/press-pdfs/postimees-2026-02-22-*",
    "research/press-pdfs/wsj-2026-06-20-*",
    "research/press-pdfs/wsj-2026-09-12-*",
    "research/press-pdfs/nyt-2026-09-03-*",
    "research/sec-filings/*",
]

EXTERNALS = [
    Path("/mnt/f/projects/memes/anthropic-investors/research/04-openphil-grants-raw-2026-09-11.json"),
    Path("/mnt/f/projects/memes/ai-machine/01-tarbell-bylines/research/funding.csv"),
    Path("/mnt/f/projects/memes/ai-machine/01-tarbell-bylines/research/outlet_windows.csv"),
    Path("/mnt/f/projects/memes/ai-machine/01-tarbell-bylines/research/roster.csv"),
    Path("/mnt/f/projects/memes/ai-machine/01-tarbell-bylines/research/sources/S003.html"),
]


def main() -> None:
    with REGISTER.open(newline="", encoding="utf-8") as stream:
        rows = [row for row in csv.DictReader(stream) if row["fetch_method"] != "local-authority"]
    paths: set[Path] = set()
    for pattern in PATTERNS:
        paths.update(path for path in ROOT.glob(pattern) if path.is_file())
    paths.update(path for path in EXTERNALS if path.is_file())
    paths.discard(REGISTER)  # a register cannot carry a stable hash of itself
    total = sum(path.stat().st_size for path in paths)
    if total > MAX_TOTAL:
        raise RuntimeError(f"local evidence exceeds total limit: {total}")
    stamp = datetime.now(timezone.utc).isoformat()
    for path in sorted(paths, key=str):
        size = path.stat().st_size
        if size > MAX_FILE:
            raise RuntimeError(f"local evidence exceeds per-file limit: {path} ({size})")
        data = path.read_bytes()
        try:
            artifact = str(path.relative_to(ROOT))
        except ValueError:
            artifact = str(path)
        rows.append(
            {
                "row_ids": "support",
                "source_url": path.as_uri(),
                "fetch_method": "local-authority",
                "fetch_url": path.as_uri(),
                "utc": stamp,
                "status": f"local;bytes={size}",
                "content_type": "application/octet-stream",
                "sha256": hashlib.sha256(data).hexdigest(),
                "artifact": artifact,
            }
        )
    rows.sort(key=lambda row: (row["source_url"], row["fetch_method"], row["fetch_url"]))
    with REGISTER.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"register_rows={len(rows)} local_files={len(paths)} local_bytes={total}")


if __name__ == "__main__":
    main()
