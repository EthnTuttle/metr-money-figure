#!/usr/bin/env python3
"""Bounded primary-source fetcher for AUDIT-3B.

Usage: python3 research/audit3-evidence/fetch.py LANE FILENAME URL
Appends one JSON object per attempt to fetch-register.jsonl.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import urllib.error
import urllib.request


BASE = Path(__file__).resolve().parent
REGISTER = BASE / "fetch-register.jsonl"
# The IRS split-interest microdata named by ST115 is about 78 MB.
MAX_BYTES = 100 * 1024 * 1024


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: fetch.py LANE FILENAME URL", file=sys.stderr)
        return 2
    lane, filename, url = sys.argv[1:]
    if not lane or Path(lane).name != lane or Path(filename).name != filename:
        print("lane and filename must be single path components", file=sys.stderr)
        return 2

    dest_dir = BASE / lane
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / filename
    utc = dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")
    record: dict[str, object] = {
        "url": url,
        "utc": utc,
        "lane": lane,
        "path": str(dest.relative_to(BASE.parent.parent)),
    }
    tmp_name = None
    try:
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 AUDIT-3B primary-source verifier",
                "Accept": "*/*",
            },
        )
        with urllib.request.urlopen(request, timeout=45) as response:
            status = getattr(response, "status", 200)
            digest = hashlib.sha256()
            size = 0
            with tempfile.NamedTemporaryFile(dir=dest_dir, delete=False) as tmp:
                tmp_name = tmp.name
                while True:
                    chunk = response.read(64 * 1024)
                    if not chunk:
                        break
                    size += len(chunk)
                    if size > MAX_BYTES:
                        raise ValueError(f"response exceeds {MAX_BYTES} bytes")
                    digest.update(chunk)
                    tmp.write(chunk)
        os.replace(tmp_name, dest)
        tmp_name = None
        record.update(
            status=status,
            bytes=size,
            sha256=digest.hexdigest(),
            content_type=response.headers.get("Content-Type", ""),
        )
        exit_code = 0 if 200 <= int(status) < 400 else 1
    except (OSError, ValueError, urllib.error.URLError) as exc:
        record.update(status="ERROR", error=f"{type(exc).__name__}: {exc}")
        exit_code = 1
    finally:
        if tmp_name:
            try:
                os.unlink(tmp_name)
            except FileNotFoundError:
                pass

    with REGISTER.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    print(json.dumps(record, ensure_ascii=False, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
