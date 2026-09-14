# Third source audit — Figure 10a-anthropic: Audacious/Canary, RAND, and Tarbell

Audit date: 2026-09-14 UTC. Scope is `AUDIT-SEED-3C.md`: 29 named rows across `money_flows.csv`, `audacious-partners.csv`, `budget.csv`, `tarbell_funding.csv`, and `tarbell_outlets.csv`, plus the current Figure 10a-anthropic HTML. This is an audit report, not a replacement goal contract.

Overall figure verdict: **FIX TEXT; retain the audited amounts and chip counts.** The Canary commitments, two filed Canary payments, partner-list chronology, three Tarbell-named Coefficient awards, two SFF recommendations, and all six displayed outlet counts reproduce. The material defects are semantic: most displayed outlet counts are not exclusively publisher-tagged articles; the branch label does not itself identify SFF's $1.303M as recommendations; the grey-pipe rule is described as a floor although the generator adds a 6 px intercept; and the ~$21M RAND share is a remainder derived from RAND's ~$38M total and METR's ~$17M statement, not a split stated wholly in RAND's release.

Evidence: [fetch register](audit3-evidence/fetch-register.csv), [deterministic calculations](audit3-evidence/calculations.json), [primary captures](audit3-evidence/), and [check script](audit3-evidence/audit3_checks.py). The register has 33 rows: 18 HTTP 200 captures, 11 local primary/source-pack copies, and four expected HTTP 404 captures for the retired Coefficient grant URLs. Every registered artifact exists and matches its SHA-256. A transport status means bytes were obtained; the substantive verdicts are below. No source by `@kevinnbass` was used. Awards, recommendations, commitments, and filed grants remain separate. No motive is asserted.

CSV corrections applied in place, without deleting rows: M118 (990-PF form and readable Part XV groups), M146 (RAND's actual category descriptions), AP06 (stale “only” and the Part XV group count), and TO01–TO07 (the actual source method/classification). Each changed row preserves the required `audit-3 2026-09-14: was …` note. `scripts/generate.py` was not edited.

## Numbered findings, ranked by consequence for the figure

1. **Outlet chips — DIFFERS in the figure's description and disclosure, although every count reproduces.** The seven source-pack recounts are TIME 45, The Verge 37, MIT Technology Review 26, Lawfare 22, The Guardian 20, Los Angeles Times 14, and Bloomberg 16. The displayed six therefore match TO01–TO06. But only The Verge, Guardian, and Los Angeles Times are independently recountable from `article-inventory.csv` using a non-empty `roster_id`, `ai_tag_verified=yes`, the outlet's captured date range, and unique article URLs. TIME, MIT Technology Review, Lawfare, and Bloomberg are derived from `research/denominators/*.csv` in the bylines pack. Among fellow rows, 42/45 TIME, 4/26 MIT Technology Review, 22/22 Lawfare, and 13/16 Bloomberg are `keyword_fallback`, not publisher-tag rows. Thus “fellows' AI-tagged articles” is false for three displayed chips and TO07. The figure says windows differ and points to the CSV, but prints neither exact ranges nor completeness: TIME 2025-09-12–2026-09-11 partial; Verge 2026-06-25–2026-09-11 partial; MIT Technology Review 2025-09-12–2026-09-11 complete; Lawfare 2025-09-15–2026-08-20 partial; Guardian 2025-09-18–2026-09-11 partial; Los Angeles Times 2026-06-05–2026-08-31 partial. Bloomberg, not displayed, is 2025-09-12–2026-09-11 complete. These are not comparable full-year publisher-tag censuses.

2. **Tarbell branch — DIFFERS in the on-graphic SFF label; amounts are CONFIRMED.** The retained 2,911-record Coefficient index has Tarbell Center awards of $816,000 on 2024-11-17, $2,888,000 on 2025-03-06, and $1,587,930 on 2025-07-15. Their exact same-type sum is $5,291,930, which correctly rounds to the printed $5.3M. The separate 2023 Training for Good award of $999,000 names “Operating Costs and Tarbell Fellowship” but is not a Tarbell Center award and is correctly excluded from $5.3M. All four index URLs currently return 404, so the retained index is the amount/date source. SFF's 2024 table recommends $520,000 for Tarbell Fellowship; its 2025 table recommends $783,000 for Tarbell Center for AI Journalism and marks a $200,000 matching pledge within that total. The figure's branch reads “+ SFF $1.3M”; only the legend/footnote says these are recommendations. That fails the seed's requirement that the figure itself say “recommended,” not imply paid money, and the plus sign visually joins unlike measures even though no combined total is printed.

3. **TED Foundation filing check — M118 DIFFERS and was corrected; the figure's “no Canary line” claim is CONFIRMED.** TED Foundation Inc is a Form 990-PF filer, not a Form 990 Schedule I filer. Its TY2021–TY2024 XMLs each report `binaryAttachmentCnt="0"` and contain 3, 6, 1, and 2 readable paid-grant groups, respectively. TY2024's two Part XV grants total $100,253. None of the four returns contains a paid-grant group naming Canary, RAND, METR, or Model Evaluation and Threat Research. The prior “attachment unread / not checkable in XML” caveat was wrong; no softening is needed. Audacious's live FAQ separately says, “TED itself does not provide funding for grantees.”

4. **Canary split and grey pipes — amounts CONFIRMED, attribution and scale wording DIFFER.** RAND states a commitment of approximately $38M to RAND and METR; METR states that approximately $17M “will support work at METR.” The displayed ~$21M RAND share is the arithmetic remainder, $38M − $17M, not a number stated in RAND's release. Barnes's 2025-09-28 comment is verbatim: “Audacious funding: This ended up being a bit under $16m, and is a commitment across 3 years.” The two grey paths use the intended M57/M58 values, but their actual stroke widths are 59.2 px and 29.8 px because `pw()` computes `6 + 1.4 × amount_in_millions`. The figure says “1.4 px per $1M, with a 6 px floor”; a true `max(6, 1.4 × amount)` rule would yield 53.2 px and 23.8 px. Since the generator cannot be edited in this lane, the footnote should describe the implemented 6 px intercept.

5. **Filed Canary payments — CONFIRMED; AP06's stale exclusivity/count text differed and was corrected.** Valhalla Foundation's TY2024 XML has 80 paid-grant groups and nine approved-future groups. Its paid group to RAND Corporation is exactly $10,000,000 for “PROJECT CANARY, AN ARTIFICIAL INTELLIGENCE SAFETY INITIATIVE”; it has no METR grant group. High Tide Foundation's TY2024 XML names the filer **HIGH TIDE FOUNDATION** and reports exactly $333,334 to **THE RAND CORPORATION** for “To support tTHE PROJECT CANARY”; it also has no METR group. ProPublica labels EIN 20-1164239 “Overlook International Foundation Inc,” so AP46/M143 correctly distinguish the e-file name from ProPublica's alias. These are two located filed payments, both to RAND; they are not evidence of a METR payment.

6. **Partner-list churn — CONFIRMED.** The raw 2024-10-09 22:05:22 Wayback capture has 46 partner/individual names and no Good Ventures. The live page has 60. After normalizing the two renames—Bill & Melinda Gates Foundation → Gates Foundation and Climate Leadership Initiative → Climate Lead—there are 14 additions and no drops: 10X Better Foundation; AKO Foundation; Arrow Impact; Cheryl and Jahm Najafi Family; Dovetail Impact Foundation; Good Ventures; Growald Climate Fund; Jay and Michaela (Mikey) Hoag; Jeff and Marieke Rothschild; Molly and Bill Ford; Skip Foundation; The Just Trust; The Patchwork Collective; The Tepper Foundation. Therefore “Good Ventures joined the partner list after Canary was announced” is supported. Good Ventures's FYE 2024 and 2025 990-PF grant groups contain no Canary, METR, Audacious, or TED Foundation grant; this does not identify who funded Canary.

7. **RAND CAST disclosures — names CONFIRMED; M146's first two category labels differed and were corrected.** RAND's live page has three lists. List 1 is gifts for independently initiated research allocated by RAND leadership to CAST: Coefficient Giving, Ergo Impact, Founders Pledge, Charlottes och Fredriks Stiftelse, Good Ventures, Jaan Tallinn, Longview, Sentinel Bio. List 2 is gifts/grants made specifically to support independently initiated research within RAND CAST: Effektiv Spenden, Fidelity Charitable, Tom Prickett, Waking Up Foundation. List 3 is directed grants/contracts for specific RAND CAST projects: The Audacious Project; Chris Anderson and Jacqueline Novogratz; Coefficient Giving; DALHAP Investments Ltd.; Ergo Impact; Fathom; Good Ventures; High Tide Foundation; The Li Lu Humanitarian Foundation; The Pew Charitable Trusts; Sea Grape Foundation; Valhalla Foundation; The William and Flora Hewlett Foundation. The figure footnote's intended directed-list subset—Audacious, Anderson and Novogratz, Valhalla, High Tide, Sea Grape, Coefficient, Good Ventures, Fathom—is correct. The source says “made or recommended by,” so the list is not itself proof that every entry paid money.

8. **AP49's all-partner census — UNVERIFIABLE at its full stated scope; the narrower figure wording is acceptable.** This lane recounted both partner pages, read the two located Canary payment filings, checked TED Foundation TY2021–TY2024, and checked Good Ventures's two relevant fiscal returns. It did not reconstruct primary filing evidence for every legal vehicle behind all 46 announcement-day and 60 live display names, and AP49 points to an agent-produced `G69-canary.csv` rather than a primary-source census register. The exact manual route is to map every display name to all grantmaking EINs/vehicles, obtain each TY2024 and available TY2025 990/990-PF plus any Part XV/Schedule I attachments, search recipient and purpose fields for RAND, METR, Canary, and Audacious, and record inaccessible/missing returns as unknown rather than zero. The figure says “two show a filed Canary payment” / “filed payments found,” not “only two exist,” so its narrower existential wording does not depend on completion of that census.

9. **Remaining scoped context — CONFIRMED.** RAND's Canary project page states that Audacious provided funding for RAND and METR to pursue the work jointly; RAND's 2024 annual report contains no Canary string while listing Valhalla among Campaign Grantmakers and Leading Lifetime Donors. Barnes's budget, runway, and fundraising lines reproduce G15–G17 verbatim: ~$13M current annual run rate (~$15M next year and plausibly $17M++), 12–16 months of runway, and a $10M end-2025 fundraising goal with Audacious described as one-off funding. These distinct measures are not added to the Canary commitment.

## Row-by-row verdicts

### `money_flows.csv`

| Row | Verdict | Primary-source result |
|---|---|---|
| M57 | **CONFIRMED** | RAND says Audacious “has committed approximately $38 million to RAND and METR for Canary.” This is a commitment, not a filed payment. |
| M58 | **CONFIRMED** | METR says Audacious catalyzed approximately $38M and “Approximately $17 million of this will support work at METR.” This is a subset of M57. |
| M117 | **CONFIRMED** | Good Ventures is absent from the 46-name announcement-day capture and present on the 60-name live list. Its FYE 2024/2025 990-PF paid-grant groups have no Canary, METR, Audacious, or TED Foundation match. The row appropriately leaves project funding undisclosed and calls the link weak. |
| M118 | **DIFFERS — corrected** | Correct value: `grant (990-PF Part XV)`. All four XMLs are readable; TY2024 has two paid-grant groups totaling $100,253 and `binaryAttachmentCnt="0"`. No Canary/RAND/METR grant group occurs. The prior Schedule I/unreadable-attachment wording was false. |
| M119 | **CONFIRMED** | Valhalla Foundation → RAND Corporation, $10,000,000, exact purpose “PROJECT CANARY, AN ARTIFICIAL INTELLIGENCE SAFETY INITIATIVE”; no METR grant group. |
| M143 | **CONFIRMED** | High Tide Foundation → The RAND Corporation, $333,334, exact filed purpose “To support tTHE PROJECT CANARY”; no METR grant group. ProPublica's organization alias is Overlook International Foundation Inc. |
| M146 | **DIFFERS — corrected** | All names match, but “unrestricted gifts” and the old list-2 shorthand were not RAND's category wording. The three correct descriptions and exact lists are in finding 7 and `calculations.json`. |

### `audacious-partners.csv`

| Row | Verdict | Primary-source result |
|---|---|---|
| AP06 | **DIFFERS — corrected** | Amount, recipient, purpose, and no-METR result match. Part XV has 80 paid plus nine approved-future groups, not “338 rows,” and Valhalla is one of two located filing-level Canary payments, not the only one. |
| AP43 | **CONFIRMED** | RAND's Canary page says Audacious provided funding for RAND and METR to jointly pursue AI-safety advances. The 2024 annual report does not name Canary; it does list the described donors without project attribution. |
| AP46 | **CONFIRMED** | The e-file name, ProPublica alias, $333,334 amount, RAND recipient, exact typo-preserving purpose, and absence of a METR group all reproduce. |
| AP47 | **CONFIRMED** | 46 names in the raw announcement-day capture, 60 live, two renames, 14 additions, no normalized drops; Good Ventures is one of the additions. |
| AP49 | **UNVERIFIABLE** | Tried: both partner-page recounts, the two positive filings, TED Foundation TY2021–TY2024, and Good Ventures FYE 2024/2025. Missing: a primary, vehicle-by-vehicle register proving all 46/60 names checked, including attachments and unavailable returns. Manual route is stated in finding 8. |

### `budget.csv`

| Row | Verdict | Primary-source result |
|---|---|---|
| G14 | **CONFIRMED** | Barnes, 2025-09-28: “Audacious funding: This ended up being a bit under $16m, and is a commitment across 3 years.” |
| G15 | **CONFIRMED** | Barnes: “Budget: We run at ~$13m p.a. rn (~$15m for the next year under modest growth assumptions, quite plausibly $17m++ …).” |
| G16 | **CONFIRMED** | Barnes: “Runway: Depending on spend/growth assumptions, we have between 12 and 16 months of runway.” |
| G17 | **CONFIRMED** | The same comment calls Audacious one-off funding and says, “Our fundraising goal for the end of 2025 is to raise $10M.” |

### `tarbell_funding.csv`

| Row | Verdict | Primary-source result |
|---|---|---|
| TB01 | **CONFIRMED** | Coefficient index post 16424: Training for Good, “Operating Costs and Tarbell Fellowship,” $999,000, 2023-09-26. It is not included in the Tarbell Center's $5.3M. URL now 404. |
| TB02 | **CONFIRMED** | Index post 28264: Tarbell Center for AI Journalism, General Support, $816,000, 2024-11-17. URL now 404. |
| TB03 | **CONFIRMED** | Index post 37845: Tarbell Center for AI Journalism, General Support, $1,587,930, 2025-07-15. URL now 404. |
| TB04 | **CONFIRMED** | Index post 28351: Tarbell Center for AI Journalism, Operating Costs, $2,888,000, 2025-03-06. URL now 404. TB02–TB04 sum exactly $5,291,930. |
| TB05 | **CONFIRMED** | SFF 2024 final recommendations list Tarbell Fellowship at $520,000, with a parenthetical $10,000 speculation amount; the $520,000 is a recommendation. |
| TB06 | **CONFIRMED** | SFF 2025 lists Tarbell Center at $783,000 and identifies a $200,000 matching pledge within that recommendation; fulfillment is conditional/unverified, not an extra paid amount. |

### `tarbell_outlets.csv`

| Row | Verdict | Primary-source result |
|---|---|---|
| TO01 | **DIFFERS — corrected** | Count/window match: TIME 45, 2025-09-12–2026-09-11. Correct classification: 42 `keyword_fallback`, three `tag_page`; source window partial. “AI-tagged” was wrong. |
| TO02 | **CONFIRMED — method note clarified** | The Verge 37, 2026-06-25–2026-09-11; 37 unique inventory URLs with non-empty `roster_id` and `ai_tag_verified=yes`; partial publisher-tag window. |
| TO03 | **DIFFERS — corrected** | Count/window match: MIT Technology Review 26, 2025-09-12–2026-09-11. Correct classification: 22 `tag_page`, four `keyword_fallback`; article window complete. |
| TO04 | **DIFFERS — corrected** | Count/window match: Lawfare 22, 2025-09-15–2026-08-20. All 22 are `keyword_fallback` in a partial Common Crawl/Wayback sample, not publisher-tagged articles. |
| TO05 | **CONFIRMED — method note clarified** | The Guardian 20, 2025-09-18–2026-09-11; 20 unique inventory URLs with non-empty `roster_id` and `ai_tag_verified=yes`; partial publisher-tag window. |
| TO06 | **CONFIRMED — method note clarified** | Los Angeles Times 14, 2026-06-05–2026-08-31; 14 unique inventory URLs with non-empty `roster_id` and `ai_tag_verified=yes`; partial publisher-tag window. |
| TO07 | **DIFFERS — corrected** | Count/window match: Bloomberg 16, 2025-09-12–2026-09-11. Correct classification: 13 `keyword_fallback`, three `publisher_tag`; complete trailing-year article window. TO07 is not a displayed chip and the figure correctly cites TO01–TO06. |

Verdict totals: **21 CONFIRMED, 7 DIFFERS, 1 UNVERIFIABLE = 29 scoped rows.** “Corrected” records what differed at audit time; it does not convert the audit finding into an original confirmation.

## Source coverage, integrity, and completion gate

The Wayback partner source was fetched through the timestamped `id_` raw route. The Coefficient evidence uses the retained 2026-09-11 index because all four per-grant URLs returned 404. The RAND, METR, GreaterWrong, Audacious, SFF, ProPublica, and IRS/gt990 sources were fetched without changing network or system configuration. The bylines pack files were read from the exact paths named by the seed and copied into the evidence directory with hashes. The calculation script deduplicates outlet rows by article URL and uses the source pack's outlet-specific date windows. It does not add unlike money measures.

The completion gate was run after this report draft from the `10-metr` directory and exited 0. Last line: **`figures=29 pngs=29 row_ids_in_research=2213 cited=1111 missing=0`**.

## figure text recommendations

1. Replace the Tarbell node's “fellows' AI-tagged articles” with: **“fellows' articles classified as AI by publisher tags where available or by the source pack's title/slug keyword fallback, in outlet-specific captured windows.”** Add the six exact date ranges and `complete`/`partial` status from finding 1, either in each chip or in the footnote. Do not imply that the partial windows are comparable full-year outlet shares.

2. Replace the branch label **“$5.3M 2024–25 → Tarbell (TB02–TB04) + SFF $1.3M (TB05–TB06)”** with two measure-explicit labels: **“Coefficient awards: $5.292M to Tarbell Center, 2024–25 (TB02–TB04)”** and **“SFF recommendations: $1.303M, 2024–25, including a $200K conditional match (TB05–TB06).”** Do not join them with a plus sign or a combined total.

3. Replace the RAND split wording with: **“~$38M Audacious commitment total (RAND); METR said ~$17M for METR; implied RAND remainder ~$21M; METR later said ‘a bit under $16m’ across 3 years (G14).”** In the footnote, cite both RAND and METR for the split and label ~$21M as subtraction, not a RAND quote.

4. Replace the scale sentence **“1.4 px per $1M, with a 6 px floor”** with **“stroke width = 6 px + 1.4 px per $1M, with no cap”** to describe the uneditable generator's implemented rule.

5. Retain **“Good Ventures joined the partner list after Canary was announced,”** the two named filed payments, and **“TED's own filings carry no Canary line.”** Strengthen the latter's citation text to **“TED Foundation TY2021–TY2024 990-PF Part XV XMLs list no Canary/RAND/METR grant; the XML grant groups are readable and no attachment caveat applies.”** Retain “filed payments found” rather than claiming the all-partner search is exhaustive.

6. In the CAST footnote, use RAND's exact names **“Chris Anderson and Jacqueline Novogratz”** and preserve “made or recommended by”; do not turn the directed-list disclosure into a claim that every named entity made a paid grant.
