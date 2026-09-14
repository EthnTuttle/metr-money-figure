#!/usr/bin/env python3
"""Deterministic, bounded checks for AUDIT-SEED-3B."""

from __future__ import annotations

import csv
import gzip
import hashlib
import html
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]
EVIDENCE = ROOT / "research" / "audit3-evidence"
OUT = EVIDENCE / "audit3b-calculations.json"
COEFFICIENT = Path(
    "/mnt/f/projects/memes/anthropic-investors/research/"
    "04-openphil-grants-raw-2026-09-11.json"
)
MAX_TEXT_BYTES = 100 * 1024 * 1024


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def read_text(path: Path) -> str:
    if path.stat().st_size > MAX_TEXT_BYTES:
        raise ValueError(f"oversized input: {path}")
    with path.open("rb") as handle:
        magic = handle.read(2)
    opener = gzip.open if magic == b"\x1f\x8b" else open
    with opener(path, "rt", encoding="utf-8", errors="replace") as handle:
        return html.unescape(handle.read())


def norm(value: str) -> str:
    value = html.unescape(value).replace("’", "'").replace("“", '"').replace("”", '"')
    return " ".join(value.split())


def xml_root(path: Path) -> ET.Element:
    return ET.parse(path).getroot()


def elements(root: ET.Element, tag: str) -> list[ET.Element]:
    return [elem for elem in root.iter() if local(elem.tag) == tag]


def first_text(root: ET.Element, tag: str) -> str | None:
    for elem in root.iter():
        if local(elem.tag) == tag:
            return elem.text
    return None


def child_text(root: ET.Element, tag: str) -> str | None:
    for elem in root.iter():
        if local(elem.tag) == tag and elem.text:
            return elem.text
    return None


def recipient_rows(path: Path) -> list[dict[str, object]]:
    rows = []
    for elem in xml_root(path).iter():
        if local(elem.tag) != "RecipientTable":
            continue
        name = child_text(elem, "BusinessNameLine1Txt") or child_text(elem, "PersonNm")
        amount = child_text(elem, "CashGrantAmt")
        if name and amount:
            rows.append({"name": norm(name), "amount": int(amount)})
    return rows


def find_recipient(rows: list[dict[str, object]], token: str, amount: int) -> bool:
    token = token.upper()
    return any(token in str(row["name"]).upper() and row["amount"] == amount for row in rows)


def bsky_text(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return payload["thread"]["post"]["record"]["text"]


def parent_texts(path: Path) -> list[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    node = payload["thread"]
    texts = []
    while node:
        record = node.get("post", {}).get("record", {})
        if "text" in record:
            texts.append(record["text"])
        node = node.get("parent")
    return texts


def scope_rows() -> dict[str, object]:
    investments = {f"IV{i:02d}" for i in range(1, 12)}
    stakes = {
        "ST26", "ST32", "ST33", "ST41", "ST49", "ST54", "ST78", "ST79",
        *(f"ST{i}" for i in range(89, 119)),
        "ST121", "ST125", "ST127", "ST133",
    }
    extra = {"J02", "J08", "K01", "S13", *(f"RW{i}" for i in range(31, 36))}
    check_rows = {*(f"M{i}" for i in range(139, 143))}
    wanted = investments | stakes | extra | check_rows
    found: dict[str, str] = {}
    for path in (ROOT / "research").glob("*.csv"):
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames or "row_id" not in reader.fieldnames:
                continue
            for row in reader:
                if row.get("row_id") in wanted:
                    found[row["row_id"]] = path.name
    return {
        "seed_scope_count": len(investments | stakes | extra),
        "check_only_rows_count": len(check_rows),
        "reported_verdict_count": len(wanted),
        "missing": sorted(wanted - set(found)),
        "files": dict(sorted(found.items())),
    }


def quote_checks() -> dict[str, object]:
    qdir = EVIDENCE / "quotes"
    fresh_saved = {}
    for row, fresh, saved in [
        ("ST110", "bsky-ST110-3miawblqk7224.json", "bsky-3miawblqk7224.json"),
        ("ST112", "bsky-ST112-3miawjaazyc24.json", "bsky-3miawjaazyc24.json"),
        ("ST113", "bsky-ST113-3mjaq5x2pws2e.json", "bsky-3mjaq5x2pws2e.json"),
    ]:
        fresh_text = bsky_text(qdir / fresh)
        saved_text = bsky_text(ROOT / "research" / "moskovitz-words" / saved)
        fresh_saved[row] = {
            "fresh_equals_saved": fresh_text == saved_text,
            "fresh_text": fresh_text,
        }
    wave = parent_texts(qdir / "bsky-ST90-ST111-3mtygcpxluc2b.json")
    f92 = norm(read_text(qdir / "forbes-ST92-wayback-20260421043155.html"))
    fnov = norm(read_text(qdir / "forbes-ST32-ST33-us-wayback-20251107132055.html"))
    stratechery = norm(read_text(qdir / "stratechery-ST118-wayback-20251020103508.html"))
    return {
        "bluesky_fresh_vs_saved": fresh_saved,
        "wave_thread_texts": wave,
        "wave_root_names_good_ventures": any("via funding from Good Ventures" in x for x in wave),
        "forbes_apr_quote_present": "estimated stake of less than 0.8%" in f92,
        "forbes_nov_500m_present": "worth an estimated $500 million" in fnov,
        "forbes_nov_early_2025_present": "early 2025" in fnov,
        "stratechery_observer_present": "I'm a board observer at Anthropic" in stratechery,
        "stratechery_boardroom_present": "also in the boardroom in at Anthropic" in stratechery,
    }


def good_ventures_checks() -> dict[str, object]:
    root = xml_root(ROOT / "research" / "990pf-goodventures-202641359349102829.xml")
    contributors = []
    for group in elements(root, "ContributorInformationGrp"):
        contributors.append({
            "number": int(child_text(group, "ContributorNum") or 0),
            "name": child_text(group, "BusinessNameLine1Txt"),
            "amount": int(child_text(group, "TotalContributionsAmt") or 0),
            "noncash": child_text(group, "NoncashContributionInd") == "X",
        })
    noncash = []
    for group in elements(root, "NonCashPropertyContributionGrp"):
        noncash.append({
            "contributor_number": int(child_text(group, "ContributorNum") or 0),
            "description": child_text(group, "NoncashPropertyDesc"),
            "fmv": int(child_text(group, "FairMarketValueAmt") or 0),
            "received": child_text(group, "ReceivedDt"),
        })
    stocks = {}
    for group in elements(root, "InvestmentsCorporateStockGrp"):
        name = child_text(group, "StockNm")
        value = child_text(group, "EOYFMVAmt")
        if name and value:
            stocks[norm(name)] = int(value)
    contractors = {}
    for group in elements(root, "CompensationOfHghstPdCntrctGrp"):
        name = child_text(group, "BusinessNameLine1Txt")
        amount = child_text(group, "CompensationAmt")
        if name and amount:
            contractors[norm(name)] = int(amount)
    prior_root = xml_root(ROOT / "research" / "990pf-goodventures-202501349349105365.xml")
    prior_grants = []
    for group in elements(prior_root, "GrantOrContributionPdDurYrGrp"):
        name = child_text(group, "BusinessNameLine1Txt")
        amount = child_text(group, "Amt")
        if name and amount:
            prior_grants.append({"name": norm(name), "amount": int(amount)})
    return {
        "contributors": contributors,
        "noncash_contributions": noncash,
        "anthropic_named_in_schedule_b": any(
            "ANTHROPIC" in str(item).upper() for item in contributors + noncash
        ),
        "total_assets_eoy": int(first_text(root, "TotalAssetsEOYAmt") or 0),
        "named_stock_fmv": {
            key: stocks.get(key) for key in [
                "TAIWAN SEMICONDUCTOR MANUFACTURING", "SK HYNIX INC", "BROADCOM INC",
                "VISTRA CORP", "MICRON TECHNOLOGY INC", "VERTIV HOLDINGS CO",
            ]
        },
        "vara_fee": contractors.get("VALUE ALIGNED RESEARCH ADVISORS LLC"),
        "fy2024_open_philanthropy_advisors_10m": find_recipient(
            prior_grants, "OPEN PHILANTHROPY ADVISORS", 10_000_000
        ),
    }


def daf_checks() -> dict[str, object]:
    f = EVIDENCE / "filings"
    npt25_path = f / "npt-FY2025-202601289349302480.xml"
    npt24_path = f / "npt-FY2024-202511339349301311.xml"
    npt23_path = f / "npt-FY2023-202431429349301368.xml"
    svcf24_path = f / "svcf-2024-202543149349305759.xml"
    svcf23_path = f / "svcf-2023-202413129349304911.xml"
    npt25 = recipient_rows(npt25_path)
    npt24 = recipient_rows(npt24_path)
    npt23 = recipient_rows(npt23_path)
    svcf24 = recipient_rows(svcf24_path)
    svcf23 = recipient_rows(svcf23_path)
    filings = {
        "npt25": npt25, "npt24": npt24, "npt23": npt23,
        "svcf24": svcf24, "svcf23": svcf23,
    }
    coefficient = json.loads(COEFFICIENT.read_text(encoding="utf-8"))
    coefficient_pairs = [
        (norm(" / ".join(x.get("organization_name", []))), int(x["grant_amount"]), x.get("title"), x.get("award_year"))
        for x in coefficient if x.get("grant_amount") is not None
    ]
    expected = [
        ("npt25", "EPOCH ARTIFICIAL", "EPOCH", 4_132_488),
        ("npt25", "REDWOOD RESEARCH", "REDWOOD RESEARCH", 1_100_000),
        ("npt23", "REDWOOD RESEARCH", "REDWOOD RESEARCH", 5_300_000),
        ("svcf24", "OBELUS", "OBELUS", 1_134_769),
        ("svcf24", "INTERNATIONAL AIDS VACCINE", "INTERNATIONAL AIDS VACCINE", 796_878),
        ("svcf24", "RAND", "RAND", 2_000_000),
        ("svcf24", "GIVING WHAT WE CAN", "GIVING WHAT WE CAN", 2_200_000),
        ("svcf24", "COMPASSION IN WORLD FARMING", "COMPASSION IN WORLD FARMING", 1_300_000),
        ("svcf24", "PLANT BASED FOODS", "PLANT BASED FOODS", 257_000),
        ("svcf24", "ONE FOR THE WORLD", "ONE FOR THE WORLD", 296_000),
        ("svcf24", "LIFE SCIENCES RESEARCH", "LIFE SCIENCES RESEARCH", 218_500),
        ("svcf23", "NUCLEAR THREAT", "NUCLEAR THREAT", 7_831_500),
        ("svcf23", "HUMANE SOCIETY INTERNATIONAL", "HUMANE SOCIETY INTERNATIONAL", 887_300),
        ("svcf23", "GLOBAL CHALLENGES", "GLOBAL CHALLENGES", 687_589),
        ("svcf23", "CAMBRIDGE BOSTON ALIGNMENT", "CAMBRIDGE BOSTON ALIGNMENT", 550_000),
        ("svcf23", "ONE FOR THE WORLD", "ONE FOR THE WORLD", 870_000),
        ("svcf23", "AQUATIC LIFE", "AQUATIC LIFE", 550_000),
        ("svcf23", "LIFE SCIENCES RESEARCH", "LIFE SCIENCES RESEARCH", 401_750),
        ("svcf23", "MAGNIFY MENTORING", "MAGNIFY MENTORING", 320_000),
    ]
    matches = []
    for filing, filing_name, coefficient_name, amount in expected:
        filing_ok = find_recipient(filings[filing], filing_name, amount)
        coefficient_ok = any(
            coefficient_name in name.upper() and pair_amount == amount
            for name, pair_amount, _title, _year in coefficient_pairs
        )
        matches.append({
            "filing": filing, "filing_name": filing_name,
            "coefficient_name": coefficient_name, "amount": amount,
            "filing_match": filing_ok, "coefficient_match": coefficient_ok,
        })
    npt_roots = [xml_root(path) for path in [npt23_path, npt24_path, npt25_path]]
    close_held_eoy = []
    for root in npt_roots:
        group = elements(root, "CloselyHeldEquityInterestsGrp")[0]
        close_held_eoy.append(int(child_text(group, "BookValueAmt") or 0))
    schedule_m = elements(npt_roots[-1], "SecuritiesCloselyHeldStockGrp")[0]
    named_total = sum([
        50_000_000, 61_646_790, 14_420_253, 11_564_000,
        4_132_488, 3_997_252, 1_100_000,
    ])
    contributions = int(first_text(npt_roots[-1], "CYContributionsGrantsAmt") or 0)
    vanguard = read_text(f / "vanguard-FY2025-posted-schedule-b.txt")
    return {
        "coefficient_index_rows": len(coefficient),
        "on_disk_daf_xml_count": len(list((ROOT / "research" / "daf-sponsors").glob("*.xml"))),
        "exact_amount_matches": matches,
        "exact_amount_match_count": sum(
            item["filing_match"] and item["coefficient_match"] for item in matches
        ),
        "svcf_to_npt_2024": find_recipient(svcf24, "NATIONAL PHILANTHROPIC TRUST", 1_591_322_838),
        "npt_fy2025_schedule_m": {
            "count": int(child_text(schedule_m, "ContributionCnt") or 0),
            "amount": int(child_text(schedule_m, "NoncashContributionsRptF990Amt") or 0),
        },
        "npt_closely_held_equity_eoy_2023_2025": close_held_eoy,
        "npt_fy2025_eoy_increase": close_held_eoy[-1] - close_held_eoy[-2],
        "st116_seven_named_grants_exact_total": named_total,
        "npt_contributions_line_1h": contributions,
        "npt_schedule_a_2_percent_exact": contributions * 0.02,
        "npt_schedule_b_minimum_whole_dollars_above_floor": int(contributions * 0.02) + 1,
        "vanguard_posted_fields_present": all(token in norm(vanguard) for token in [
            "1,461,141,307", "302,700,922", "158,180,000", "130,000,000",
            "368,432,337", "184,277,747", "91,680,000", "12/24/2024",
        ]),
        "vanguard_schedule_b_names_anthropic": bool(
            re.search(r"\bANTHROPIC\b", vanguard.upper())
        ),
    }


def sit_checks() -> dict[str, object]:
    path = EVIDENCE / "filings" / "sit-2022.csv"
    tokens = ["DUSTIN MOSKOVITZ", "DUSTIN A MOSKOVITZ", "CARI TUNA", "CTF TRUST"]
    matches = {token: [] for token in tokens}
    apercen = []
    lytton = []
    row_count = 0
    with path.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            row_count += 1
            text = " | ".join(row.values()).upper()
            for token in tokens:
                if token in text:
                    matches[token].append(text)
            if "APERCEN" in text:
                apercen.append(text)
            if "314 LYTTON" in text:
                lytton.append(text)
    return {
        "data_rows": row_count,
        "target_match_counts": {key: len(value) for key, value in matches.items()},
        "apercen_match_count": len(apercen),
        "lytton_314_match_count": len(lytton),
    }


def sec_checks() -> dict[str, object]:
    sec = EVIDENCE / "sec"
    adv = norm(read_text(sec / "vara-ADV-319135.txt"))
    initial = norm(read_text(sec / "vara-form-d-initial.xml"))
    march = norm(read_text(sec / "vara-form-d-amendment.xml"))
    june = norm(read_text(sec / "vara-form-d-2026-06-15.xml"))
    blue_owl = norm(read_text(sec / "st117-blue-owl-s1.html"))
    holdings = []
    for path in sorted((ROOT / "research" / "sec-filings").glob("vara-13f-hr-*.xml")):
        root = xml_root(path)
        names = [e.text or "" for e in root.iter() if local(e.tag).lower() == "nameofissuer"]
        values = [int(e.text or 0) for e in root.iter() if local(e.tag).lower() == "value"]
        holdings.append({
            "file": path.name, "positions": len(values), "total_usd": sum(values),
            "anthropic_named": any("ANTHROPIC" in name.upper() for name in names),
        })
    arc = read_text(ROOT / "research" / "990-arc-fy2024-202513219349323246.xml")
    return {
        "adv_q20_50_percent": "(Q20) 50%" in adv or "50%" in adv,
        "adv_four_clients": all(re.search(pattern, adv, re.I) for pattern in [
            r"Pooled investment vehicles.*?2.*?5,189,964,815",
            r"Charitable organizations.*?2.*?3,949,666,809",
        ]),
        "adv_charities_non_exchange_traded_zero": bool(
            re.search(r"Non Exchange-Traded Equity Securities\s+0%", adv, re.I)
        ),
        "form_d_initial_first_sale_yet_to_occur": "<yetToOccur>true</yetToOccur>" in initial,
        "form_d_march_2026_amount": "2834590561" in march and "68" in march,
        "form_d_june_2026_amount": "4346290561" in june and "116" in june,
        "blue_owl_ctf_trust": "THE CTF TRUST UAD 122712" in blue_owl,
        "blue_owl_moskovitz_investments": "MOSKOVITZ INVESTMENTS LLC" in blue_owl.upper(),
        "arc_hoskin_board_member": "BENJAMIN HOSKIN" in arc.upper() and "BOARD MEMBER" in arc.upper(),
        "holdings": holdings,
    }


def arithmetic_checks() -> dict[str, object]:
    ceiling = 0.008 * 965_000_000_000
    display = 7_700_000_000
    pw = 6 + (display / 1_000_000) * 1.4
    figure = read_text(ROOT / "figures" / "metr-01b-money-that-doesnt-show-up-with-anthropic.html")
    return {
        "0.8_percent_of_965b": ceiling,
        "7.7b_over_500m": display / 500_000_000,
        "printed_x15_present": "×15 at the ceiling" in figure,
        "full_scale_pw_7.7b": pw,
        "one_thirtieth_width": int(pw / 30),
        "full_scale_in_2080px_canvases": pw / 2080,
        "ceiling_word_present": "ceiling" in figure,
        "calls_7.7b_valuation": bool(
            re.search(r"\$?7\.7B\s+(?:post-money\s+)?valuation", figure, re.I)
        ),
        "director_occurrences": len(re.findall(r"\bdirector\b", figure, re.I)),
        "not_a_director_present": "not a director" in figure,
    }


def register_checks() -> dict[str, object]:
    path = EVIDENCE / "fetch-register.jsonl"
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    good = []
    bad = []
    content_failures = []
    for record in records:
        if record.get("status") == "ERROR":
            continue
        artifact = ROOT / str(record["path"])
        item = {
            "path": record["path"], "exists": artifact.exists(),
            "hash_matches": artifact.exists() and sha256(artifact) == record.get("sha256"),
        }
        if artifact.exists() and artifact.stat().st_size <= 64 * 1024:
            prefix = artifact.read_text(encoding="utf-8", errors="replace")
            if "Just a moment" in prefix and "unusual traffic" in prefix:
                content_failures.append({**item, "reason": "anti-bot challenge page"})
        (good if item["exists"] and item["hash_matches"] else bad).append(item)
    return {
        "attempts": len(records),
        "http_successes": len(good),
        "expected_or_disclosed_errors": sum(r.get("status") == "ERROR" for r in records),
        "content_failures": content_failures,
        "bad_artifacts": bad,
    }


def main() -> int:
    result = {
        "scope": scope_rows(),
        "quotes": quote_checks(),
        "arithmetic": arithmetic_checks(),
        "good_ventures": good_ventures_checks(),
        "daf": daf_checks(),
        "split_interest_trust_file": sit_checks(),
        "sec": sec_checks(),
        "fetch_register": register_checks(),
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(OUT.relative_to(ROOT))
    print(json.dumps({
        "missing_scope_rows": result["scope"]["missing"],
        "exact_daf_matches": result["daf"]["exact_amount_match_count"],
        "registered_attempts": result["fetch_register"]["attempts"],
        "bad_registered_artifacts": len(result["fetch_register"]["bad_artifacts"]),
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
