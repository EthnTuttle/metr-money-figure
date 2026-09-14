# Figure 10a money-pipes audit

The arithmetic is sound, but the figure should not ship unchanged. All 17 printed money totals recompute from the rows used by `fig_money(anth=True)`, and every `flow()` path has the width produced by the code's formula from the underlying unrounded amount. The consequential problems are categorical: the blue legend calls every Coefficient and SFF pipe “Good Ventures money”; the Coefficient node calls SVCF and NPT “its” donor-advised accounts; the Redwood node says Redwood worked on both investigations although the cited Anthropic record does not mention Redwood; and the unqualified “Direct: $0” is stronger than the record search can establish.

This audit assigns one verdict to each of the 85 rows required by `AUDIT-SEED-3A`: **82 CONFIRMED, 2 DIFFERS, 1 UNVERIFIABLE**. The two differences are TB05's 2024 Tarbell grantee identity and ST109's inclusion of a temporally impossible SVCF/RAND match. M59's $220,000 Longview amount is UNVERIFIABLE at the primary-source level: its cited Giving What We Can page reports the amount, while the refetched Longview and METR pages confirm the relationship but do not publish that transaction.

## Method and evidence integrity

I read the rendered HTML and `fig_money(anth=True)` first.[^1] I then refetched every fetchable `source_url` in scope and saved each response below `research/audit3-evidence/<lane>/`. The machine-readable register has 93 attempts: 52 HTTP 200, 2 HTTP 403, and 39 HTTP 404; 92 saved artifacts have SHA-256 hashes, and every saved hash rechecked successfully.[^2] The 403 RAND pages were recovered through the permitted `r.jina.ai` route. The 39 live 404s are Coefficient grant pages withdrawn after the site transition; those rows were checked against the required local index instead. M120's `source_url` cell contains a citation and local-save path but no URL; I fetched the canonical Coefficient article separately and recorded the source-field defect.

The retained Coefficient index is `04-openphil-grants-raw-2026-09-11.json`: its filename date is **2026-09-11**, it contains 2,911 records, and its SHA-256 is `91a9543d4a55153e900af29eb1f5dbd618b9a13ac361f209128f5e98c4c36022`.[^3] All 38 scoped index rows—M01–M32, M126–M128, and TB02–TB04—were found by URL, with exact amount and UTC award-date matches. Organization identity and titles match as well; M27 and M128 only have a trailing non-breaking space in the snapshot title.

The bounded calculation record contains the scope list, sums, SVG stroke inventory, snapshot comparisons, recipient-name searches, Tallinn rows, and register-integrity result.[^4] No prohibited account post was used. Awards, recommendations, commitments, filed grants, transfers, and investments were never added across types.

## Ranked findings

1. **The blue legend and Coefficient node over-attribute money to Good Ventures.** Coefficient says it submits recommendations either to Coefficient Giving Advisors or to external funding partners including SVCF, NPT, and Good Ventures, each of which separately approves grants.[^5] ST109 gives strong exact-amount evidence that many published awards were paid through SVCF/NPT, but neither the sponsors nor Coefficient identify the underlying donor for those accounts. SFF recommendations are from Jaan Tallinn and plainly are not Good Ventures money. Replace both the legend and “its DAF accounts” wording.

2. **“Redwood … METR's subcontractor on the OpenAI and Anthropic investigations” is unsupported for Anthropic.** RW31–RW34 confirm the OpenAI work, including the primary wording “a Redwood Research staff member contracting with METR.” RW35 says the Anthropic agreement is with METR and explicitly records that neither announcement names Redwood or another subcontractor.[^6] The dashed link correctly represents no recorded Redwood→METR grant, but “both investigations” does not follow from the cited rows.

3. **“Direct: $0” should be bounded to the checked records.** Exact recipient-name searches of the 2,911-row Coefficient snapshot for `METR`, `Model Evaluation`, and `Model Evaluation and Threat Research` returned zero. A raw substring search for `METR` is unsafe because it finds “Center for Welfare Metrics” and “Institute for Health Metrics and Evaluation.” Exact grant-recipient searches of Good Ventures' FY2024 and FY2025 990-PFs also returned zero through June 30, 2025. This establishes **no recorded direct grant in those sources**, not an all-source or all-time zero.

4. **The Audacious pipe must remain a commitment, not a payment.** The October 9, 2024 RAND release says Audacious “committed approximately $38 million” to RAND and METR; METR's same-day post says approximately $17 million would support METR.[^7] A later METR figure says the commitment “ended up being a bit under $16m” over three years. M119 and M143 document filed payments to RAND of $10,000,000 and $333,334, but no filing in scope documents a payment to METR. The current gray legend is correct; the METR-share label should show the dated revision.

5. **The figure's TED-filing caveat is now supportable only in its narrow form.** TED Foundation is a 990-PF filer, not a Form 990 Schedule-I filer. Its TY2021–TY2024 Part XV XMLs contain 3, 6, 1, and 2 readable paid-grant groups; none names METR, RAND, or Canary. TY2024's two grants total $100,253. Audacious's FAQ says TED itself does not fund grantees, so the absence of a TED Foundation line does not negate partner-funded Canary commitments or payments.[^8] M118 has already been corrected in place with the required `audit-3 2026-09-14: was ...` note.

6. **The $220,000 Longview amount is reported, not primary-confirmed.** Giving What We Can says “Longview Philanthropy recommended a grant of $220,000 from its public fund in 2023.” Longview's live AI page profiles METR without an amount, while METR names “pooled funds such as those of Longview Philanthropy.”[^9] The relationship is primary-confirmed, but the exact transaction, payment status, and general-support purpose require a Longview grant record or recipient ledger.

7. **TB05 assigns the 2024 SFF recommendation to the wrong entity.** The SFF primary lists applicant “Tarbell Fellowship,” receiving charity “Players Philanthropy Fund,” amount `$520,000 ($10,000)†`, and purpose “General support of Tarbell Fellowship.”[^10] TB05 instead names Tarbell Center for AI Journalism. The 2025 TB06 row correctly names the Tarbell Center.

8. **ST109 contains one false same-grant match.** SVCF's calendar-2024 Schedule I lists RAND Corporation, $2,000,000, purpose “Community Development.” The only $2,000,000 Coefficient award to RAND in the retained index is “Technology and Security Policy Center,” dated May 2, 2025. The recipient and amount match, but the award postdates SVCF's filing year, so it cannot be that 2024 payment. The other 18 listed exact-name/amount matches are temporally compatible; the strong routing pattern remains, but the RAND example must be removed or replaced.

9. **All code-level widths pass, but four rounded labels cannot reproduce the visible width.** FAR AI, SFF→ARC, SFF→Redwood, and DAF→ARC differ by 0.1 px when the formula is applied to the printed rounded label rather than the exact total. The `$70M+` Redwood path uses exactly the $70 million floor. The separate red “Direct: $0” line is 3 px, not the formula's 6 px floor, because the generator does not create it with `flow()`.

10. **The displayed `$22.9M` Constellation total is a rounding edge.** The exact $22,950,000 total formats as `$22.9M` under the generator's one-decimal floating-point formatting; ordinary decimal half-up presentation would be `$23.0M`. No row is missing. M91–M92 are also correctly excluded from the yellow DAF total because they are the filed-payment counterparts of M01–M02, not additional grants.

11. **The Tallinn matching test passes.** Every Founders Pledge row in M77–M80 matches the public ledger to the dollar. M82 is $50,450 in SVCF's filing versus $50,000 in the ledger, exactly the allowed $450 difference; M83's $20,000 equals two $10,000 ledger lines.[^11] These matches support donor attribution for those specific filed grants, not for other DAF rows.

## Amount recomputation

The code's `num()` treats composite strings as the sum of their numeric components, so M39 becomes $120,000 + $428,000 = $548,000. The latter $428,000 is a conditional SFF matching pledge; the $120,000 is the already-awarded speculation-grant portion within the $548,000 recommendation. The table keeps those attributes visible rather than treating the result as an unconditional cash payment.

| Figure pipe | Exact rows and recomputed amount | Printed | Result |
|---|---:|---:|---|
| Coefficient→ARC, M01–M02 | $1,515,000 | $1.5M | Matches after one-decimal rounding |
| Coefficient→RAND, M03 | $10,000,000 | $10.0M | Exact |
| Coefficient→Longview, M04–M14 | $26,251,590 | $26.3M | Matches after rounding |
| Coefficient→FAR AI, M15–M32 | $59,347,676 | $59.3M | Matches after rounding |
| SFF→ARC, M35–M37 | $5,623,000 | $5.6M | Matches after rounding |
| SFF→METR, M38–M39 | $752,000 | $752K | Exact |
| Audacious→Canary, M57 | approximately $38,000,000 | $38.0M | Matches the dated commitment |
| Audacious→METR share, M58 | approximately $17,000,000 | ~$17.0M | Matches 2024 announcement; later revised below $16M |
| ARC→METR, M63 | $4,553,935 | $4.6M | Matches after rounding; $4,477,169 cash + $76,766 noncash |
| Longview→METR, M59 | reported $220,000 | $220K | Numerically exact; primary status unresolved |
| DAF/regrantors→ARC, selected M77–M96 | $10,835,635 | $10.8M | Matches after rounding |
| Tallinn-attributed subset of that ARC pipe | $4,222,450 | $4.2M | Matches after rounding |
| DAF/regrantors→METR, M79/M83/M87 | $4,204,000 | $4.2M | $4.0M Vanguard + $184K Founders Pledge + $20K SVCF |
| Coefficient recommendation→Redwood, M120 | more than $70,000,000 | $70M+ | Correct floor; recommendation, not award/payment |
| SFF→Redwood, M47–M48 | $2,372,000 | $2.4M | Matches after rounding |
| Coefficient→Constellation, M126–M128 | $22,950,000 | $22.9M | Generator rounding edge; decimal half-up is $23.0M |
| SVCF→Constellation, ST107 | $10,000,000 | $10.0M | Exact filed grant |
| Coefficient→Tarbell, TB02–TB04 | $5,291,930 | $5.3M | Matches after rounding; SFF rows excluded |

Good Ventures' filed M91–M92 total is $1,515,000 and mirrors M01–M02. The SFF Tarbell recommendations total $1,303,000 and are not included in the blue $5.3M award pipe. The rows therefore avoid double-counting and cross-type addition.

## SVG pipe-width audit

For every generated money or relationship path, the test is `max(6, 6 + amount / 1,000,000 × 1.4)`, rounded to one decimal for the SVG attribute.

| Path in drawing order | Amount used by code | Expected / SVG px | Label consistency |
|---|---:|---:|---|
| Coefficient→ARC | $1,515,000 | 8.1 / 8.1 | Matches label at shown precision |
| Coefficient→RAND | $10,000,000 | 20.0 / 20.0 | Matches |
| Coefficient→Longview | $26,251,590 | 42.8 / 42.8 | Matches |
| Coefficient→FAR AI | $59,347,676 | 89.1 / 89.1 | Exact total passes; `$59.3M` alone implies 89.0 |
| SFF→ARC | $5,623,000 | 13.9 / 13.9 | Exact total passes; `$5.6M` alone implies 13.8 |
| SFF→METR | $752,000 | 7.1 / 7.1 | Matches |
| Audacious→Canary | $38,000,000 | 59.2 / 59.2 | Matches approximate commitment |
| Coefficient recommendation→Redwood | $70,000,000 floor | 104.0 / 104.0 | `$70M+` does not specify the excess |
| SFF→Redwood | $2,372,000 | 9.3 / 9.3 | Exact total passes; `$2.4M` alone implies 9.4 |
| Coefficient→Constellation | $22,950,000 | 38.1 / 38.1 | Matches |
| SVCF→Constellation | $10,000,000 | 20.0 / 20.0 | Matches |
| Redwood dashed relation | $0 recorded | 6.0 / 6.0 | Formula floor; see evidentiary caveat |
| Constellation dashed relation | $0 recorded | 6.0 / 6.0 | Formula floor |
| DAF/regrantors→ARC | $10,835,635 | 21.2 / 21.2 | Exact total passes; `$10.8M` alone implies 21.1 |
| DAF/regrantors→METR | $4,204,000 | 11.9 / 11.9 | Matches |
| Audacious→METR share | approximately $17,000,000 | 29.8 / 29.8 | Matches dated estimate |
| ARC→METR | $4,553,935 | 12.4 / 12.4 | Matches |
| Longview→METR | reported $220,000 | 6.3 / 6.3 | Matches |
| FAR-board dashed relation | $0 recorded | 6.0 / 6.0 | Formula floor |
| Coefficient→Tarbell | $5,291,930 | 13.4 / 13.4 | Matches |

The other SVG path widths are not scaled money pipes: one 12 px node connector, six 3 px decorative outlet-chip connectors, two 8 px equity paths on a separately disclosed scale, and the 3 px red direct-zero line. Thus all `flow()` calls pass. The direct-zero line is the sole labelled monetary-looking line outside the formula and should either be described as an annotation or raised to the 6 px floor.

## Money types and legend

| Rows / pipe | Type established by the primary | Figure treatment |
|---|---|---|
| M01–M32, M126–M128, TB02–TB04 | Coefficient index awards; Coefficient describes the workflow as a recommendation followed by separate approval by its grantmaking entity or an external funding partner | Amount and award labels are sound; “Good Ventures money” is not established for every pipe |
| M35–M39, M47–M48, TB05–TB06 | SFF recommendations; M39 includes a $428K conditional match and TB06 includes a $200K conditional match | Must remain recommendations; not Good Ventures money and not all paid |
| M120 | Internal Coefficient recommendation of more than $70M over two years | Correctly called a recommendation in the footnote; should not visually merge with indexed awards without a qualifier |
| M57–M58 | Approximate, multi-year Audacious commitment | Gray legend is correct; payment is not shown |
| M63 | ARC program-spin-off transfer: cash plus noncash assets | Filed transfer, not new outside funding and not attributable to one ARC donor |
| M77–M96, M119, M143, ST107 | Grants reported in Form 990 Schedule I or 990-PF Part XV | Yellow filed-grant description is correct; filing year is not necessarily transaction date |
| M118 | Negative search of TED Foundation 990-PF Part XV grant groups | Correct only as “no TED Foundation filing line,” not “no Audacious money” |
| M59–M60 | Reported recommended grant plus primary-confirmed unquantified pooled-funder relationship | Orange relationship is appropriate; exact $220K needs attribution to the reporting source |
| M139–M140 | Macroscopic's self-reported grants/support | Do not sum with investments or indexed awards |
| M141–M142 | Macroscopic's self-reported impact investments | Correctly separate from grants; not a figure pipe amount |

## Dashed links and recorded-zero test

- **Redwood:** no scoped `money_flows.csv` row records Redwood→METR money. RW32 does record a Redwood employee contracting with METR for the OpenAI review, so a contract relationship exists but its direction and amount are not published. RW35 does not establish Redwood involvement in the Anthropic review. Verdict on the zero: **no recorded Redwood→METR amount**, not proof of no payment.

- **Constellation:** M126 and METR's May 2026 post support the shared-office relationship. No scoped row records Constellation→METR money. The office link is supported; the zero is a bounded dataset result.

- **FAR AI:** board row B05 confirms that FAR AI CEO Adam Gleave is a METR adviser and board member. M15–M32 record money into FAR AI, not from FAR AI to METR. No scoped row records FAR AI→METR money. J08 is not the relevant board evidence; B05 is.

- **Direct Coefficient / Good Ventures:** the exact Coefficient recipient searches were `METR`, `Model Evaluation`, and `Model Evaluation and Threat Research`; each returned zero. Good Ventures searches used exact grant-recipient elements plus `MODEL EVALUATION` and `THREAT RESEARCH`, not a blind `METR` substring. No direct recipient line appears through its June 30, 2025 filing. The present footnote's qualification is directionally correct, but the prominent “Direct: $0” label needs the same boundary.

## Tallinn ledger reconciliation

| Filing row | Filed grant | Public-ledger line(s) | Difference |
|---|---:|---|---:|
| M77, Founders Pledge→ARC | $2,179,000 | 2022-12-20, FP-US→ARC, $2,179,000 | $0 |
| M78, Founders Pledge→ARC Evals | $1,846,000 | 2023-06-15, FP-US→ARC, $1,846,000 | $0 |
| M79, Founders Pledge→METR | $184,000 | 2024-12-06, FP-US→Model Evaluation and Threat Research, $184,000 | $0 |
| M80, Founders Pledge→ARC | $147,000 | 2024-11-21, FP-US→ARC, $147,000 | $0 |
| M82, SVCF→ARC | $50,450 | 2024-07-19, SFF-spec→ARC, $50,000 | $450 |
| M83, SVCF→METR | $20,000 | 2024-07-23 and 2024-07-24, SFF-spec→METR, $10,000 each | $0 |

The ledger test therefore passes exactly as specified. Its public payment dates also give transaction-level dates not supplied by the filing-year labels.

## Row-by-row verdicts

“Index exact” means amount, UTC award date, grantee, and title/purpose match the September 11 snapshot; the linked live grant page was nevertheless refetched and returned 404. “Filing exact” means the named IRS group matches the row's amount, grantee, filing year, and purpose text.

### Coefficient awards to ARC, RAND, Longview, and FAR AI

| Row | Verdict | Primary check |
|---|---|---|
| M01 | CONFIRMED | Index exact: ARC, $265,000, 2022-03-01, “General Support.” |
| M02 | CONFIRMED | Index exact: ARC, $1,250,000, 2022-11-18, “General Support.” |
| M03 | CONFIRMED | Index exact: RAND, $10,000,000, 2025-09-20, “AI Evaluation and Testing”; retained archived page identifies Canary, the RAND–METR collaboration. |
| M04 | CONFIRMED | Index exact: Longview, $500,000, 2022-04-06, “Nuclear Security Grantmaking.” |
| M05 | CONFIRMED | Index exact: Longview, $60,000, 2022-11-30, “Far-UVC Event.” |
| M06 | CONFIRMED | Index exact: Longview, $74,557, 2023-01-18, “Research Support for Kacper Kowalczyk.” |
| M07 | CONFIRMED | Index exact: Longview, $57,500, 2023-01-19, “Film Project Scoping Work.” |
| M08 | CONFIRMED | Index exact: Longview, $47,500, 2023-01-20, “Support for Richard Chappell.” |
| M09 | CONFIRMED | Index exact: Longview, $165,000, 2023-02-17, “Far-UVC Event.” |
| M10 | CONFIRMED | Index exact: Longview, $770,076, 2023-02-28, “AI Policy Development at the OECD.” |
| M11 | CONFIRMED | Index exact: Longview, $4,020,258, 2023-12-15, “General Support.” |
| M12 | CONFIRMED | Index exact: Longview, $595,426, 2024-01-23, “Effective Giving Information Sharing.” |
| M13 | CONFIRMED | Index exact: Longview, $15,961,273, 2024-10-29, “General Support.” |
| M14 | CONFIRMED | Index exact: Longview, $4,000,000, 2025-06-06, hardware-enabled AI-compliance RFP. |
| M15 | CONFIRMED | Index exact: FAR AI, $425,800, 2021-10-20, language-model misalignment. |
| M16 | CONFIRMED | Index exact: FAR AI, $463,693, 2022-08-15, language-model misalignment. |
| M17 | CONFIRMED | Index exact: FAR AI, $50,000, 2022-12-05, interpretability research. |
| M18 | CONFIRMED | Index exact: FAR AI, $49,500, 2022-12-06, Inverse Scaling Prize. |
| M19 | CONFIRMED | Index exact: FAR AI, $625,000, 2022-12-12, general support. |
| M20 | CONFIRMED | Index exact: FAR AI, $280,000, 2023-03-14, FAR Labs office space. |
| M21 | CONFIRMED | Index exact: FAR AI, $100,000, 2023-03-30, AI interpretability research. |
| M22 | CONFIRMED | Index exact: FAR AI, $460,000, 2023-07-09, general support. |
| M23 | CONFIRMED | Index exact: FAR AI, $166,500, 2023-09-25, Alignment Workshop. |
| M24 | CONFIRMED | Index exact: FAR AI, $645,750, 2024-01-16, AI alignment research projects. |
| M25 | CONFIRMED | Index exact: FAR AI, $2,160,000, 2024-04-19, general support. |
| M26 | CONFIRMED | Index exact: FAR AI, $1,700,000, 2024-04-19, FAR Labs office space. |
| M27 | CONFIRMED | Index exact: FAR AI, $1,800,000, 2024-04-19, AI field building; snapshot has only a trailing NBSP. |
| M28 | CONFIRMED | Index exact: FAR AI, $12,000,000, 2024-06-16, AI safety regranting. |
| M29 | CONFIRMED | Index exact: FAR AI, $676,180, 2024-07-25, AI alignment research projects. |
| M30 | CONFIRMED | Index exact: FAR AI, $2,420,253, 2025-04-13, communications and outreach. |
| M31 | CONFIRMED | Index exact: FAR AI, $6,650,000, 2025-04-13, AI field building. |
| M32 | CONFIRMED | Index exact: FAR AI, $28,675,000, 2025-09-14, AI safety research and field-building. |

### SFF, Audacious, Longview, ARC, and Jane Street rows

| Row | Verdict | Primary check |
|---|---|---|
| M35 | CONFIRMED | SFF 2022-H2 exact: Jaan Tallinn, ARC, $2,179,000, general support. |
| M36 | CONFIRMED | SFF 2023-H1 exact: ARC Evals Team, $3,247,000, general support. |
| M37 | CONFIRMED | SFF 2024 exact: ARC, total recommendation $197,000, general support; page separately annotates a $50,000 speculation grant. |
| M38 | CONFIRMED | SFF 2024 exact: METR, total recommendation $204,000, general support; page separately annotates a $20,000 speculation grant. |
| M39 | CONFIRMED | SFF 2025 exact: METR, $548,000 recommendation, general support; $120,000 speculation-grant portion and $428,000 conditional match. |
| M47 | CONFIRMED | SFF 2022-H1 exact: Redwood Research Group, $1,274,000, general support. |
| M48 | CONFIRMED | SFF 2023-H1 exact: Redwood Research Group, $1,098,000, general support. |
| M57 | CONFIRMED | RAND, 2024-10-09: Audacious committed approximately $38M to RAND and METR for Canary. |
| M58 | CONFIRMED | METR, 2024-10-09: approximately $17M would support METR; later update below $16M is a subsequent revision, not a mismatch to the dated row. |
| M59 | UNVERIFIABLE | Refetched GWWC report says Longview “recommended a grant of $220,000 ... in 2023,” but no primary Longview/METR record gives amount, payment status, or purpose. Manual route: Longview grant agreement/disbursement report or METR donor ledger. |
| M60 | CONFIRMED | Longview's primary page includes METR among work it funds, and METR names Longview among its pooled funds; both properly leave amount and date undisclosed. |
| M63 | CONFIRMED | ARC 990 exact: $4,477,169 cash plus $76,766 noncash, fair-market value $4,553,935, distribution date 2024-04-30, “Program Spin-Off.” |
| M75 | CONFIRMED | METR's current About page names “individuals from Jane Street” among donation supporters and gives no names, date, or amount; the row does not attribute the firm. |

### Filed DAF and regrantor grants

| Row | Verdict | Primary check |
|---|---|---|
| M77 | CONFIRMED | Founders Pledge TY2022 990-PF exact: ARC, $2,179,000, general support; Tallinn ledger exact. |
| M78 | CONFIRMED | Founders Pledge TY2023 990-PF exact: ARC, $1,846,000, general support of ARC Evals Team; ledger exact. |
| M79 | CONFIRMED | Founders Pledge TY2024 Schedule I exact: METR, $184,000, fund charitable activities; ledger exact. |
| M80 | CONFIRMED | Founders Pledge TY2024 Schedule I exact: ARC, $147,000, fund charitable activities; ledger exact. |
| M81 | CONFIRMED | SVCF TY2023 Schedule I exact: ARC, $1,401,000, Sciences. |
| M82 | CONFIRMED | SVCF TY2024 Schedule I exact: ARC, $50,450, Sciences; ledger is $50,000, a disclosed $450 difference. |
| M83 | CONFIRMED | SVCF TY2024 Schedule I exact: METR, $20,000, Sciences; two ledger lines total $20,000. |
| M84 | CONFIRMED | Vanguard FY2023 Schedule I exact: ARC, $201,000, recipient's exempt purpose. |
| M85 | CONFIRMED | Vanguard FY2024 Schedule I exact: ARC, $1,000,000, recipient's exempt purpose. |
| M86 | CONFIRMED | Vanguard FY2025 Schedule I exact: ARC, $1,500,000, recipient's exempt purpose. |
| M87 | CONFIRMED | Vanguard FY2025 Schedule I exact: METR, $4,000,000, recipient's exempt purpose. |
| M88 | CONFIRMED | Effective Ventures USA FY2023 Schedule I exact: ARC, $1,500,000, general nonprofit support. |
| M89 | CONFIRMED | Same filing, separate exact line: ARC, $54,543, AI-alignment research/collaboration. |
| M90 | CONFIRMED | Effective Ventures USA FY2024 Schedule I exact: ARC, $100,000, research on AI safety. |
| M91 | CONFIRMED | Good Ventures FY2022 990-PF exact: ARC, $265,000, general support; payment counterpart of M01, excluded from yellow sum. |
| M92 | CONFIRMED | Good Ventures FY2023 990-PF exact: ARC, $1,250,000, AI-alignment research; payment counterpart of M02, excluded from yellow sum. |
| M93 | CONFIRMED | Every.org TY2023 Schedule I exact: ARC, $223,805, online support for charitable purposes. |
| M94 | CONFIRMED | Every.org TY2024 Schedule I exact: ARC, $132,837, general support. |
| M95 | CONFIRMED | American Endowment Foundation TY2023 Schedule I exact: ARC, $400,000, general operating support. |
| M96 | CONFIRMED | Fidelity Charitable FY2024 Schedule I exact: ARC, $100,000, recipient's exempt purposes. |

### Good Ventures/Audacious, Redwood, Constellation, CERR, High Tide, and RAND

| Row | Verdict | Primary check |
|---|---|---|
| M117 | CONFIRMED | Good Ventures is on Audacious's live partner page but absent from the 2024-10-09 archived partner list; filings through June 2025 show no Audacious/TED/Canary/METR line. The row correctly says per-project donors are undisclosed. |
| M118 | CONFIRMED | Corrected row matches all four TED Foundation 990-PFs: 3/6/1/2 paid-grant groups, none to METR/RAND/Canary; TY2024 total $100,253. This is a TED-filing negative only. |
| M119 | CONFIRMED | Valhalla TY2024 990-PF exact: RAND, $10,000,000, “PROJECT CANARY, AN ARTIFICIAL INTELLIGENCE SAFETY INITIATIVE.” |
| M120 | CONFIRMED | Canonical Coefficient article dated 2026-09-09 says its grantmakers “recently recommended more than $70 million over the next two years” for Redwood. The CSV source field itself should be replaced with the canonical URL. |
| M126 | CONFIRMED | Index exact: Constellation, $3,000,000, 2023-06-06, “Coworking Space”; METR's primary post supports the shared-center relation. |
| M127 | CONFIRMED | Index exact: Constellation, $3,200,000, 2024-04-18, general support. |
| M128 | CONFIRMED | Index exact: Constellation, $16,750,000, 2024-06-19, programmatic activities and operating expenses; 990 facts in purpose also match. |
| M139 | CONFIRMED | Macroscopic's primary grants page lists Redwood among supported organizations, without amount or date. |
| M140 | CONFIRMED | Same page says it supported Longview's digital-sentience consortium and hardware-enabled-verification RFP, without amount or date. |
| M141 | CONFIRMED | Same page lists Apollo Research under “Impact Investments,” not grants; no amount/date shown. |
| M142 | CONFIRMED | Same page lists Halcyon Venture Partners under “Impact Investments,” not grants; no amount/date shown. |
| M143 | CONFIRMED | High Tide TY2024 990-PF exact: RAND, $333,334, “To support tTHE PROJECT CANARY” as filed; no METR grant line. |
| M146 | CONFIRMED | RAND's live CAST page contains all three separately described funder lists and every name recorded in the corrected row; earliest checked archive for list (iii), 2025-12-15, is identical.[^12] |

### Tarbell and SVCF/NPT rows

| Row | Verdict | Primary check |
|---|---|---|
| TB02 | CONFIRMED | Index exact: Tarbell Center, $816,000, 2024-11-17, general support. |
| TB03 | CONFIRMED | Index exact: Tarbell Center, $1,587,930, 2025-07-15, general support. |
| TB04 | CONFIRMED | Index exact: Tarbell Center, $2,888,000, 2025-03-06, operating costs. |
| TB05 | DIFFERS | SFF 2024 says applicant “Tarbell Fellowship,” receiving charity “Players Philanthropy Fund,” $520,000, “General support of Tarbell Fellowship.” Correct the CSV organization and do not assign this 2024 recommendation to Tarbell Center. |
| TB06 | CONFIRMED | SFF 2025 exact: Tarbell Center, $783,000 recommendation including $200,000 conditional matching pledge, general support. |
| ST107 | CONFIRMED | SVCF TY2024 Schedule I exact: NPT $1,591,322,838 and Constellation $10,000,000; the other named network lines, including ARC $50,450 and METR $20,000, also match. The filing does not identify underlying DAF donors. |
| ST109 | DIFFERS | Eighteen listed same-recipient exact-amount comparisons are temporally compatible. Remove SVCF-2024 RAND $2M: the sole Coefficient award with that recipient/amount/title is dated 2025-05-02 and cannot be the calendar-2024 filing payment. Exact matches establish a routing pattern, not ownership of the accounts. |

## Repository audit gate

The final gate was run from the `10-metr` directory after the report and evidence checks. Its last line was: **`figures=29 pngs=29 row_ids_in_research=2213 cited=1111 missing=0`**.

## Sources and evidence

1. Rendered figure and generator: [`figures/metr-01b-money-that-doesnt-show-up-with-anthropic.html`](../figures/metr-01b-money-that-doesnt-show-up-with-anthropic.html) and [`scripts/generate.py`](../scripts/generate.py).[^1]
2. Fetch artifacts and integrity register: [`research/audit3-evidence/`](audit3-evidence/) and [`fetch-register.json`](audit3-evidence/fetch-register.json).[^2]
3. Coefficient retained index: [`04-openphil-grants-raw-2026-09-11.json`](/mnt/f/projects/memes/anthropic-investors/research/04-openphil-grants-raw-2026-09-11.json).[^3]
4. Deterministic results: [`audit3a-calculations.json`](audit3-evidence/audit3a-calculations.json) and [`audit3a_verify.py`](audit3a_verify.py).[^4]
5. Primary organization pages: [Coefficient grantmaking process](https://coefficientgiving.org/grantmaking-process/), [SFF recommendations](https://survivalandflourishing.fund/2025/recommendations), [RAND Canary announcement](https://www.rand.org/news/press/2024/10/09.html), [METR Audacious announcement](https://metr.org/blog/2024-10-09-new-support-through-the-audacious-project/), [METR About](https://metr.org/about), [Longview AI](https://www.longview.org/artificial-intelligence/), [Macroscopic grants and investments](https://macroscopic.org/grants), and [RAND CAST funders](https://www.rand.org/global-and-emerging-risks/centers/ai-security-and-technology/funding.html).
6. Filing primaries are the IRS XML and rendered Schedule-I copies saved under [`audit3-evidence/filings/`](audit3-evidence/filings/) and [`audit3-evidence/stakes/`](audit3-evidence/stakes/); the exact URL, retrieval UTC, status, and hash are in the register.
7. Tallinn reconciliation source: [`tallinn-donations-ledger-2026-09-13.csv`](tallinn-donations-ledger-2026-09-13.csv).[^11]

[^1]: The source read covered the full `fig_money(anth=True)` function, including `tot()`, `pw()`, every `flow()` call, legend, and footnote—not just the visible PNG.
[^2]: A failed live status is retained as evidence rather than rewritten as success. Large IRS source URLs that timed out or exceeded the collector's 30 MB response bound were checked through saved official XML or row-specific ProPublica rendering routes.
[^3]: The snapshot date is confirmed by the required dated filename; the calculation record also fixes its count and hash. Live Coefficient grant URLs returned 404 and therefore do not supersede it.
[^4]: The checker is bounded to a 2 MB JSON output and validates all 85 row IDs, 38 snapshot rows, and every registered evidence hash.
[^5]: Coefficient's own wording is “our grantmaking entity ... or ... external funding partners”; it does not identify SVCF/NPT accounts as belonging to Good Ventures or the couple.
[^6]: [`redwood.csv`](redwood.csv) RW31–RW35; the OpenAI contract wording is in RW32 and the Anthropic evidentiary limit is recorded in RW35.
[^7]: “Approximately” and “commitment” are material. They are not filed-payment amounts and are not summed with M119/M143.
[^8]: [Audacious FAQ](https://www.audaciousproject.org/faq) and TED Foundation TY2021–TY2024 XML saved in the filings lane.
[^9]: [Giving What We Can's ARC Evals page](https://www.givingwhatwecan.org/charities/arc-evals) is the source of the exact $220,000 sentence; it is not a Longview disbursement record.
[^10]: [SFF 2024 recommendations](https://survivalandflourishing.fund/2024/recommendations), saved as `audit3-evidence/tarbell/sff-2024-recommendations.html`.
[^11]: Exact-equality matching does not convert an anonymous sponsor filing into donor disclosure; the public ledger is the independent attribution evidence for only the listed rows.
[^12]: RAND's first two categories are not simply “unrestricted” and “restricted”; the row now preserves RAND's full descriptions and keeps the three lists separate.

## Figure text recommendations

1. Replace the blue legend with: **“Coefficient/Open Philanthropy awards and SFF/Tallinn recommendations; colors show source/type, not a single donor (width: 1.4 px per $1M).”** Better still, give SFF recommendations a distinct color.

2. Replace the Coefficient node's payment sentence with: **“Recommends grants; Coefficient Giving Advisors or external partners including Good Ventures, SVCF, and NPT separately approve/pay. Public records do not identify the underlying donor for SVCF/NPT grants.”** Delete “its DAF accounts.”

3. Replace the headline **“Direct: $0”** with: **“No direct METR grant found in Coefficient's 2,911-row 2026-09-11 index or Good Ventures 990-PFs through 2025-06-30.”** Keep the existing unlisted-gifts limitation adjacent to the label.

4. Replace the Redwood node with: **“Redwood staff contracted with METR on the OpenAI investigation; public Anthropic/METR announcements do not name a Redwood subcontractor for the Anthropic investigation.”** Keep the dashed relationship, but describe its zero as “no recorded Redwood→METR grant/amount.”

5. Change the METR share label to: **“2024 announcement: ~$17M commitment; METR later: under $16M over 3 years.”** Do not imply either value is already paid.

6. Change the Longview label to: **“GWWC reports Longview recommended $220K in 2023; METR and Longview confirm additional pooled-funder relationship, amount undisclosed.”** Do not call the $220K paid without a primary record.

7. Change the TED footnote to: **“TED Foundation's TY2021–TY2024 990-PF Part XV lists no Canary, RAND, or METR grant; Audacious says partners fund grantees directly, so this is not evidence of zero partner funding.”**

8. Present Constellation as **`$22.95M`** or **`$23.0M`** if decimal half-up conventions are intended; retain `$22.9M` only if the generator's current binary floating-point formatting is deliberately authoritative.

9. In the Tarbell footnote, separate **Coefficient awards to Tarbell Center ($5.29193M)** from **SFF 2024 to Tarbell Fellowship via Players Philanthropy Fund ($520K)** and **SFF 2025 to Tarbell Center ($783K, including a $200K conditional match)**.

10. Either render the red direct-zero annotation at the 6 px floor or explicitly exempt annotations, decorative connectors, and separately scaled equity paths from the pipe-width rule.
