#!/usr/bin/env python3
"""Deterministic checks for AUDIT-SEED-3C; writes calculations.json."""

from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]


class TextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.items: list[str] = []

    def handle_data(self, data: str) -> None:
        value = " ".join(html.unescape(data).split())
        if value:
            self.items.append(value)


def html_items(path: Path) -> list[str]:
    parser = TextParser()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    return parser.items


def local_name(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def first_text(parent: ET.Element, wanted: str) -> str:
    for element in parent.iter():
        if local_name(element) == wanted and element.text:
            return element.text.strip()
    return ""


def xml_summary(path: Path) -> dict[str, object]:
    root = ET.parse(path).getroot()
    header = next(e for e in root.iter() if local_name(e) == "ReturnHeader")
    filer = next(e for e in header.iter() if local_name(e) == "Filer")
    groups = [
        e
        for e in root.iter()
        if local_name(e) in {"GrantOrContributionPdDurYrGrp", "RecipientTable"}
    ]
    grants = []
    for group in groups:
        grants.append(
            {
                "recipient": first_text(group, "BusinessNameLine1Txt"),
                "purpose": first_text(group, "GrantOrContributionPurposeTxt")
                or first_text(group, "PurposeOfGrantTxt"),
                "amount": first_text(group, "Amt") or first_text(group, "CashGrantAmt"),
            }
        )
    return {
        "path": str(path.relative_to(HERE)),
        "tax_period_end": first_text(header, "TaxPeriodEndDt"),
        "filer": first_text(filer, "BusinessNameLine1Txt"),
        "ein": first_text(filer, "EIN"),
        "binary_attachment_count": header.attrib.get("binaryAttachmentCnt", ""),
        "grant_group_count": len(groups),
        "total_grants_paid": first_text(root, "TotalGrantOrContriPdDurYrAmt"),
        "grants": grants,
        "canary_grants": [
            g for g in grants if "CANARY" in (g["recipient"] + " " + g["purpose"]).upper()
        ],
        "metr_grants": [
            g
            for g in grants
            if re.search(r"\bMETR\b|MODEL EVALUATION", g["recipient"] + " " + g["purpose"], re.I)
        ],
        "rand_grants": [
            g for g in grants if re.search(r"\bRAND(?: CORPORATION)?\b", g["recipient"], re.I)
        ],
        "audacious_or_ted_grants": [
            g
            for g in grants
            if re.search(r"AUDACIOUS|\bTED FOUNDATION\b", g["recipient"] + " " + g["purpose"], re.I)
        ],
    }


def partner_names(path: Path) -> list[str]:
    source = path.read_text(encoding="utf-8", errors="replace")
    values = re.findall(
        r'<div class="p-small py-10 stagger-animate-2">(.*?)</div>', source, re.S
    )
    return [html.unescape(re.sub(r"<.*?>", "", value)).strip() for value in values]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    output: dict[str, object] = {
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    }

    register = list(csv.DictReader((HERE / "fetch-register.csv").open(encoding="utf-8")))
    register_checks = []
    for row in register:
        path = HERE / row["path"]
        actual = sha256(path) if path.exists() else ""
        register_checks.append(
            {
                "path": row["path"],
                "status": row["status"],
                "exists": path.exists(),
                "registered_sha256": row["sha256"],
                "actual_sha256": actual,
                "hash_matches": bool(actual) and actual == row["sha256"],
            }
        )
    output["fetch_register"] = {
        "rows": len(register),
        "all_files_exist": all(r["exists"] for r in register_checks),
        "all_hashes_match": all(r["hash_matches"] for r in register_checks),
        "checks": register_checks,
    }

    rand_press = " ".join(html_items(HERE / "canary/rand-press-2024-10-09.html"))
    metr_post = " ".join(html_items(HERE / "canary/metr-new-support-2024-10-09.html"))
    barnes_items = html_items(HERE / "canary/barnes-shortform-2025-09-28.html")
    output["canary"] = {
        "rand_38m_quote_present": "committed approximately $38 million to RAND and METR for Canary" in rand_press,
        "metr_38m_quote_present": "catalyzed approximately $38 million of funding for Canary" in metr_post,
        "metr_17m_quote_present": "Approximately $17 million of this will support work at METR" in metr_post,
        "derived_rand_remainder": 38_000_000 - 17_000_000,
        "barnes_visible_lines": [
            line
            for line in barnes_items
            if line.startswith(("Budget:", "Audacious funding:", "Runway:", "More context on our thinking:"))
        ],
        "barnes_date_line": next((line for line in barnes_items if line == "28 Sep 2025 20:34 UTC"), ""),
    }

    filings = {}
    filing_paths = [
        HERE / "filings/valhalla-ty2024-202502559349100000.xml",
        HERE / "filings/high-tide-ty2024-202503179349100135.xml",
        HERE / "filings/goodventures-fye2024-202501349349105365.xml",
        HERE / "filings/goodventures-fye2025-202641359349102829.xml",
        *sorted((HERE / "filings").glob("ted-foundation-ty*.xml")),
    ]
    for path in filing_paths:
        filings[path.name] = xml_summary(path)
    output["filings"] = filings
    high_tide_propublica = " ".join(html_items(HERE / "filings/high-tide-propublica.html"))
    output["high_tide_alias"] = {
        "propublica_name_present": "Overlook International Foundation Inc" in high_tide_propublica,
        "ein_present": "20-1164239" in high_tide_propublica,
        "xml_filer": filings["high-tide-ty2024-202503179349100135.xml"]["filer"],
    }

    old_partners = partner_names(HERE / "partners/audacious-about-wayback-20241009220522.html")
    live_partners = partner_names(HERE / "partners/audacious-about-live.html")
    rename_map = {
        "Bill & Melinda Gates Foundation": "Gates Foundation",
        "Climate Leadership Initiative": "Climate Lead",
    }
    normalized_old = {rename_map.get(name, name) for name in old_partners}
    output["partners"] = {
        "wayback_count": len(old_partners),
        "live_count": len(live_partners),
        "wayback_names": old_partners,
        "live_names": live_partners,
        "renames": rename_map,
        "added_after_normalizing_renames": sorted(set(live_partners) - normalized_old),
        "dropped_after_normalizing_renames": sorted(normalized_old - set(live_partners)),
        "good_ventures_wayback": "Good Ventures" in old_partners,
        "good_ventures_live": "Good Ventures" in live_partners,
    }

    faq_text = " ".join(html_items(HERE / "partners/audacious-faq-live.html"))
    output["audacious_faq"] = {
        "ted_no_funding_quote_present": "TED itself does not provide funding for grantees" in faq_text
    }

    rand_funding = html_items(HERE / "rand/rand-cast-funding.html")
    heading_1 = next(i for i, x in enumerate(rand_funding) if x.startswith("Gifts for independently initiated research from RAND supporters"))
    heading_2 = next(i for i, x in enumerate(rand_funding) if x.startswith("Gifts and grants from RAND supporters made specifically"))
    heading_3 = next(i for i, x in enumerate(rand_funding) if x.startswith("Directed grants or contracts for specific research projects"))
    output["rand_cast_funding"] = {
        "heading_1": rand_funding[heading_1],
        "list_1": rand_funding[heading_1 + 1 : heading_2],
        "heading_2": rand_funding[heading_2],
        "list_2": rand_funding[heading_2 + 1 : heading_3],
        "heading_3": rand_funding[heading_3],
        "list_3": rand_funding[heading_3 + 1 : heading_3 + 14],
    }

    index = json.loads((HERE / "tarbell/coefficient-index-2026-09-11.json").read_text(encoding="utf-8"))
    wanted_posts = {16424, 28264, 28351, 37845}
    coefficient_records = []
    for row in index:
        if row.get("post_id") in wanted_posts:
            coefficient_records.append(
                {
                    "post_id": row["post_id"],
                    "organization_name": row["organization_name"],
                    "title": row["title"],
                    "grant_amount": row["grant_amount"],
                    "award_date_utc": datetime.fromtimestamp(row["award_date"], timezone.utc).date().isoformat(),
                    "url": row["url"],
                }
            )
    output["tarbell_funding"] = {
        "index_record_count": len(index),
        "coefficient_records": sorted(coefficient_records, key=lambda row: row["post_id"]),
        "tarbell_named_sum": sum(
            row["grant_amount"]
            for row in coefficient_records
            if row["organization_name"] == ["Tarbell Center for AI Journalism"]
        ),
        "coefficient_page_statuses": {
            row["path"]: row["status"]
            for row in register
            if row["path"].startswith("tarbell/coefficient-") and row["path"].endswith(".html")
        },
        "sff_2024_tarbell_context": [
            x
            for x in html_items(HERE / "tarbell/sff-2024-recommendations.html")
            if x in {"Tarbell Fellowship", "$507,000", "$3,000", "$4,000", "$6,000", "$520,000 ($10,000)†", "Players Philanthropy Fund", "General support of Tarbell Fellowship"}
        ],
        "sff_2025_tarbell_context": [
            x
            for x in html_items(HERE / "tarbell/sff-2025-recommendations.html")
            if x in {"Tarbell Center for AI Journalism", "Main: $286,000", "Freedom: $47,000", "Fairness: $48,000", "Mean: $402,000", "$783,000", "Speculation: ($20,000)†", "Matching: {$200,000}‡", "Tarbell Center for AI Journalism, Inc."}
        ],
        "sff_sum": 520_000 + 783_000,
    }

    windows = {
        row["row_id"]: row
        for row in csv.DictReader((HERE / "outlets/outlet_windows.csv").open(encoding="utf-8-sig"))
    }
    copied = {
        row["row_id"]: row
        for row in csv.DictReader((REPO / "research/tarbell_outlets.csv").open(encoding="utf-8-sig"))
    }
    inventory = list(csv.DictReader((HERE / "outlets/article-inventory.csv").open(encoding="utf-8-sig")))
    source_rows = {
        "TO01": ("W005", "denominator", "time.csv"),
        "TO02": ("W004", "inventory", ""),
        "TO03": ("W006", "denominator", "mit-technology-review.csv"),
        "TO04": ("W016", "denominator", "lawfare.csv"),
        "TO05": ("W003", "inventory", ""),
        "TO06": ("W001", "inventory", ""),
        "TO07": ("W007", "denominator", "bloomberg.csv"),
    }
    outlet_checks = {}
    for target_id, (source_id, source_kind, filename) in source_rows.items():
        target = copied[target_id]
        source = windows[source_id]
        low, high = target["window_min"], target["window_max"]
        if source_kind == "inventory":
            selected = [
                row
                for row in inventory
                if row["outlet"] == target["outlet"]
                and row["roster_id"]
                and row["ai_tag_verified"].lower() == "yes"
                and low <= row["published"] <= high
            ]
            rules = Counter({"publisher_ai_tag": len({row["article_url"] for row in selected})})
        else:
            denominator = list(
                csv.DictReader((HERE / "outlets/denominators" / filename).open(encoding="utf-8-sig"))
            )
            selected = [
                row
                for row in denominator
                if row["roster_id"]
                and row["ai_flag"].lower() == "yes"
                and row["tarbell_byline"].lower() == "yes"
                and low <= row["published"] <= high
            ]
            rules = Counter(row["ai_rule"] for row in selected)
        urls = {row["article_url"] for row in selected}
        outlet_checks[target_id] = {
            "outlet": target["outlet"],
            "source_row": source_id,
            "source_kind": source_kind,
            "copied_n_tarbell_ai": int(target["n_tarbell_ai"]),
            "recount_n_tarbell_ai": len(urls),
            "count_matches": int(target["n_tarbell_ai"]) == len(urls),
            "copied_window": [target["window_min"], target["window_max"]],
            "source_window": [source["window_min"], source["window_max"]],
            "window_matches": [target["window_min"], target["window_max"]]
            == [source["window_min"], source["window_max"]],
            "classification_rules_for_fellow_rows": dict(rules),
            "source_completeness": source["completeness"],
            "source_method": source["method"],
        }
    output["outlets"] = outlet_checks

    figure_path = REPO / "figures/metr-01b-money-that-doesnt-show-up-with-anthropic.html"
    figure = figure_path.read_text(encoding="utf-8")
    figure_visible = " ".join(html_items(figure_path))
    output["figure_text"] = {
        "good_ventures_joined_after": "Good Ventures joined the partner list after Canary was announced" in figure_visible,
        "rand_split": '~$38M: ~$21M RAND, ~$17M METR' in figure_visible,
        "barnes_under_16m": 'METR later: "a bit under $16m" over 3 years' in figure_visible,
        "tarbell_pipe_label": "$5.3M 2024–25 → Tarbell (TB02–TB04) + SFF $1.3M (TB05–TB06)" in figure_visible,
        "tarbell_pipe_says_recommended": "→ Tarbell (TB02–TB04) + SFF recommended $1.3M" in figure_visible,
        "footnote_says_sff_recommendations": "SFF figures are recommendations" in figure_visible,
        "outlet_description_ai_tagged": "fellows' AI-tagged articles in the captured window" in figure_visible,
        "footnote_says_windows_differ": "windows differ by outlet and are stated there" in figure_visible,
        "exact_window_dates_visible": all(
            f'{row["window_min"]}–{row["window_max"]}' in figure_visible for row in copied.values()
        ),
        "chips": {
            target_id: f'{("MIT Tech Review" if target_id == "TO03" else "LA Times" if target_id == "TO06" else copied[target_id]["outlet"])} · {copied[target_id]["n_tarbell_ai"]}' in figure_visible
            for target_id in ["TO01", "TO02", "TO03", "TO04", "TO05", "TO06"]
        },
        "bloomberg_chip_present": f'Bloomberg · {copied["TO07"]["n_tarbell_ai"]}' in figure_visible,
        "ted_no_canary_line": "TED's own filings carry no Canary line" in figure_visible,
        "ted_unreadable_softening_present": "not checkable in the XML; attachment unread" in figure_visible,
    }
    # The generated HTML has self-closing paths followed by the corresponding label.
    total_match = re.search(
        r'stroke="#b2b4aa" stroke-width="([0-9.]+)"[^>]*/><text[^>]*>\$38\.0M Audacious commitment',
        figure,
    )
    share_match = re.search(
        r'stroke="#b2b4aa" stroke-width="([0-9.]+)"[^>]*/><text[^>]*>~\$17\.0M to METR',
        figure,
    )
    output["grey_pipes"] = {
        "actual_total_38m_width_px": float(total_match.group(1)) if total_match else None,
        "actual_share_17m_width_px": float(share_match.group(1)) if share_match else None,
        "width_if_1_4px_per_m_with_6px_floor_total": max(6.0, 38 * 1.4),
        "width_if_1_4px_per_m_with_6px_floor_share": max(6.0, 17 * 1.4),
        "width_under_generator_6px_plus_1_4px_per_m_total": 6.0 + 38 * 1.4,
        "width_under_generator_6px_plus_1_4px_per_m_share": 6.0 + 17 * 1.4,
        "figure_claims_floor_rule": "1.4 px per $1M, with a 6 px floor and no cap" in figure_visible,
    }

    scoped = {
        "money_flows.csv": {"M57", "M58", "M117", "M118", "M119", "M143", "M146"},
        "audacious-partners.csv": {"AP06", "AP43", "AP46", "AP47", "AP49"},
        "budget.csv": {"G14", "G15", "G16", "G17"},
        "tarbell_funding.csv": {"TB01", "TB02", "TB03", "TB04", "TB05", "TB06"},
        "tarbell_outlets.csv": {"TO01", "TO02", "TO03", "TO04", "TO05", "TO06", "TO07"},
    }
    coverage = {}
    for filename, wanted in scoped.items():
        with (REPO / "research" / filename).open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        found = {row["row_id"] for row in rows if row.get("row_id") in wanted}
        coverage[filename] = {
            "expected": sorted(wanted),
            "found": sorted(found),
            "missing": sorted(wanted - found),
        }
    output["scope_coverage"] = coverage

    path = HERE / "calculations.json"
    path.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {path.relative_to(REPO)}")
    print(f"fetches={len(register)} hashes_ok={output['fetch_register']['all_hashes_match']}")
    print(f"partners={len(old_partners)}->{len(live_partners)} added={len(output['partners']['added_after_normalizing_renames'])}")
    print(f"tarbell_named_sum={output['tarbell_funding']['tarbell_named_sum']} sff_sum={output['tarbell_funding']['sff_sum']}")
    print("outlet_counts=" + ",".join(f"{key}:{value['recount_n_tarbell_ai']}" for key, value in outlet_checks.items()))


if __name__ == "__main__":
    main()
