#!/usr/bin/env python3
"""Write the one-verdict-per-scoped-row ledger for AUDIT-3D."""

from __future__ import annotations

import csv
from pathlib import Path


HERE = Path(__file__).resolve().parent

DIFFERS = {
    "AP49": ("The TED-FY2024 attachment claim was false. The final row now says the TY2021–TY2024 990-PF XML contains 3, 6, 1 and 2 readable paid-grant groups and no METR/RAND/Canary grant.", "The retained four TED XML returns; ReturnHeader binaryAttachmentCnt=0 and Part XV groups."),
    "M64": ("Amount changed from undisclosed to $184,000.", "M79 / the Founders Pledge Schedule I grant line."),
    "M65": ("Amount changed from undisclosed to $20,000.", "M83 / the SVCF Schedule I grant line."),
    "M66": ("Amount changed from undisclosed and date 2025 to $4,000,000, FY2025 (2024-07-01–2025-06-30).", "M87 / the Vanguard Charitable Schedule I grant line."),
    "M118": ("Measure changed from 990 Schedule I to 990-PF Part XV, and the false unread-attachment qualification was removed. The final row reports the four readable grant-group counts and no named Canary grant.", "The retained four TED XML returns; TY2024 has two paid grants totaling $100,253."),
    "M146": ("The first two RAND funding-category descriptions were not verbatim. The final row now preserves RAND's three separate categories and all names.", "RAND CAST funding page, freshly fetched."),
    "ST105": ("The prior row inferred that named SVCF/NPT accounts belonged to Moskovitz and Tuna. The page only calls SVCF/NPT/GVF external funding partners; it does not identify account principals.", "Coefficient grantmaking-process page: recommendations go to its entity or an external partner, which separately approves."),
    "ST118": ("The prior note said Moskovitz chairs Coefficient. The final row says he is a Board of Managers member and Cari Tuna is chair.", "Coefficient governance page, ST124."),
    "TO01": ("The old note treated the count as uniformly publisher-tagged. The final row says 42 keyword-fallback and 3 tag-page classifications in a partial source window.", "Tarbell bylines outlet_windows and article inventory recount."),
    "TO02": ("The old generic note omitted method/scope. The final row says 37 unique fellow-byline URLs in a partial publisher-tag window.", "Tarbell bylines outlet_windows and article inventory recount."),
    "TO03": ("The old generic note omitted method/scope. The final row says 22 tag-page and 4 keyword-fallback classifications in a complete trailing-year article window.", "Tarbell bylines outlet_windows and article inventory recount."),
    "TO04": ("The old generic note omitted that all 22 are keyword-fallback classifications in a partial Common Crawl/Wayback sample.", "Tarbell bylines outlet_windows and article inventory recount."),
    "TO05": ("The old generic note omitted method/scope. The final row says 20 unique fellow-byline URLs in a partial publisher-tag window.", "Tarbell bylines outlet_windows and article inventory recount."),
    "TO06": ("The old generic note omitted method/scope. The final row says 14 unique fellow-byline URLs in a partial publisher-tag window.", "Tarbell bylines outlet_windows and article inventory recount."),
}

UNVERIFIABLE = {
    "IV04": ("The cited CNBC page now returns 404 and no dated copy of that article was retained in the audit evidence.", "Retrieve the 2023-12-21 article from a licensed archive or replace it with an issuer/filing source for the closed Series D."),
    "LD01": ("Forge returned 403 and no dated Forge snapshot was retained, so the exact $2.57/$623.11M vendor figures could not be reproduced.", "Obtain the historical Forge page or the underlying Delaware certificate/cap-table source."),
    "LD03": ("Forge returned 403 and no dated Forge snapshot was retained, so its $11.23/$4.55B Series C split could not be reproduced.", "Obtain the historical Forge page or underlying Delaware certificate."),
    "LD04": ("Forge returned 403 and no dated Forge snapshot was retained, so the $30/$14.55B Series D-1 row could not be reproduced.", "Obtain the historical Forge page or underlying Delaware certificate."),
    "LD08": ("Forge returned 403 and no dated Forge snapshot was retained; Amazon's filing corroborates conversion, not every stated tranche price/share count.", "Obtain the historical Forge page or the relevant certificate and conversion schedule."),
    "LD11": ("Forge returned 403 and no dated Forge snapshot was retained; Anthropic confirms $13B/$183B but not the row's exact per-share/tranche data.", "Obtain the historical Forge page or Series F certificate."),
    "LD12": ("Forge returned 403 and no dated Forge snapshot was retained; Anthropic confirms $30B/$380B but not the row's exact per-share/tranche data.", "Obtain the historical Forge page or Series G certificate."),
    "LD14": ("Forge returned 403 and no dated Forge snapshot was retained; Anthropic confirms $65B/$965B but not every exact per-share/tranche figure in this row.", "Obtain the historical Forge page or Series H certificate; retain $965B separately as issuer-confirmed."),
    "LD21": ("The live NPM page says $777.40 as of 2026-08-31; the row's historical $773.98 as of 2026-08-28 survives only as a search-result observation.", "Use an archived NPM capture or omit the superseded historical indication."),
    "M105": ("The cited URL is one return and the retained coefficient-990 directory contains five returns, not the seven-return search claimed by the row.", "Retrieve and hash all seven named TY2022–TY2024 XMLs, then repeat the bounded recipient search."),
    "ST115": ("The IRS landing page was fetched, but the 98,802-row SOI split-interest-trust file and the claimed negative search were not retained in this audit evidence.", "Download the dated SOI file, hash it, and rerun the four-term bounded search."),
}


def main() -> None:
    rows = list(csv.DictReader((HERE / "scope-rows.csv").open(encoding="utf-8")))
    output = []
    for row in rows:
        row_id = row["row_id"]
        if row_id in DIFFERS:
            detail, route = DIFFERS[row_id]
            verdict = "DIFFERS"
        elif row_id in UNVERIFIABLE:
            detail, route = UNVERIFIABLE[row_id]
            verdict = "UNVERIFIABLE"
        else:
            verdict = "CONFIRMED"
            detail = "The freshly fetched or retained cited source matches the row at its stated measure and scope; any negative remains bounded to the records named in the row."
            route = "See scope-rows.csv and fetch-register.csv for the cited URL/local authority and artifact hash."
        output.append({
            "row_id": row_id,
            "source_csv": row["source_csv"],
            "verdict": verdict,
            "detail": detail,
            "evidence_or_manual_route": route,
        })
    if len(output) != 249 or len({r["row_id"] for r in output}) != 249:
        raise RuntimeError("scope is not exactly 249 unique rows")
    fields = ["row_id", "source_csv", "verdict", "detail", "evidence_or_manual_route"]
    with (HERE / "row-verdicts.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output)
    counts = {name: sum(r["verdict"] == name for r in output) for name in ("CONFIRMED", "DIFFERS", "UNVERIFIABLE")}
    print(f"row_verdicts={len(output)} confirmed={counts['CONFIRMED']} differs={counts['DIFFERS']} unverifiable={counts['UNVERIFIABLE']}")


if __name__ == "__main__":
    main()
