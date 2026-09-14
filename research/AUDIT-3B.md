# Third source audit — Figure 10a-anthropic: Anthropic, its investors, and the donated stake

Audit date: 2026-09-14 UTC. Scope is the 62 rows named by `AUDIT-SEED-3B.md`, plus M139–M142 because check 6 expressly requires them. All 66 rows have one verdict below. This is an audit report, not a replacement goal contract.

Overall figure verdict: **FIX TEXT; retain the quotation cards, investor links, arithmetic, and rounded equity-band dimensions.** The principal defect is attribution: no filing or issuer document reviewed attributes the SVCF or NPT account, NPT's closely held stock, or the SVCF-to-NPT transfer to Moskovitz or Tuna. The figure nevertheless calls SVCF/NPT accounts “their” or “its” accounts and makes NPT the leading candidate. It also assigns unspecified free tokens to Anthropic, calls Redwood a subcontractor on an Anthropic investigation whose announcement never names Redwood, treats Vanguard's issuer-free Schedule B descriptions as excluding Vanguard, and overstates what the VARA filing identifies.

Evidence: [AUDIT-SEED-3B](AUDIT-SEED-3B.md), [fetch register](audit3-evidence/fetch-register.jsonl), [deterministic calculations](audit3-evidence/audit3b-calculations.json), [check script](audit3-evidence/audit3b_checks.py), and [primary captures](audit3-evidence/). The register has 81 attempts: 63 HTTP-success responses and 18 disclosed transport/HTTP errors. Five of the 63 responses are BEMC anti-bot pages rather than filings; these are classified as content failures, not evidence. The register records URL, UTC time, transport status, saved path, byte count, and SHA-256. The deterministic pass found no missing scoped IDs, reproduced all 19 claimed DAF exact-amount matches, and found no hash mismatch among successfully saved artifacts. No source by `@kevinnbass` was used. Awards, recommendations, commitments, filed grants, investment values, and estimated equity values remain separate. No motive is asserted.

No CSV cells were changed. The seed permitted corrections but did not require them; the exact corrections and figure-only changes are stated below. `scripts/generate.py` was not edited.

## Numbered findings, ranked by consequence for the figure

1. **The SVCF/NPT ownership and donated-stock route are unattributed — DIFFERS.** Coefficient's page says that it submits recommendations to Coefficient Giving Advisors or external funding partners “such as” SVCF, NPT, or Good Ventures Foundation. The 19 to-the-dollar filing/index matches confirm that SVCF and NPT paid Coefficient-recommended grants. SVCF also paid NPT exactly $1,591,322,838 in calendar 2024. NPT's FY2025 Schedule M reports 19 closely held stock contributions with FMV $1,183,079,981; its year-end closely held equity rose from $737,806,285 to $1,734,031,057, an exact $996,224,772 increase. None of those documents names Moskovitz, Tuna, an account principal, or Anthropic. Moskovitz's “our foundation” statements and the aggregate filing pattern do not identify which legal vehicle or account held the shares. Therefore the subtitle's “their ... accounts,” the Coefficient node's “its DAF accounts,” the footnote's conversion of external funding partners into owned accounts, and “NPT is the leading candidate” are unsupported in their current declarative form.

2. **Two lab-to-evaluator links are unsupported — DIFFERS.** K01's primary text says only “frontier AI companies” provide significant free tokens; it does not identify Anthropic. The figure's “Anthropic → METR: free tokens” is therefore not supported by K01. RW31–RW34 establish Redwood's participation in the OpenAI/Hugging Face investigation. The Anthropic/METR announcement in RW35 describes an eight-week agreement with METR and contains no Redwood or subcontractor reference. Thus “Redwood ... subcontractor on the OpenAI and Anthropic investigations,” “subcontractor on both investigations,” and the corresponding footnote must not state the Anthropic leg as fact.

3. **Vanguard's posted Schedule B does not exclude Vanguard — DIFFERS.** The posted FY2025 disclosure reproduces the four contributor totals and noncash descriptions in ST133, including $184,277,747 of “MUTUAL FUNDS/PRIVATE EQUITY,” $91,680,000 of “PRIVATE EQUITY,” and $130,000,000 of “PRIVATE EQUITY” dated 2024-12-24. It does not name the issuers. Forbes's approximately $500M is an estimate made later, not a transfer-date appraisal. The descriptions and values therefore cannot rule out Anthropic stock, a partial block, or a differently valued block. The figure's “Vanguard ... excludes it for that window” is false; Vanguard remains unattributed and unresolved.

4. **The VARA filings support a narrower statement — DIFFERS.** The ADV reports two pooled-vehicle clients and two charitable-organization clients, four in total; Q20 says 50% of clients invested in VAR AI Fund. With the feeder as one investor and the master unable to invest in itself, at least one charitable client is an investor. The ADV does not identify which charity. Good Ventures is independently shown to be one of VARA's charitable clients by its $5,264,377 FY2025 manager fee, but that does not prove it is the charitable investor. The figure's “a Good Ventures-linked charity is one of its LPs” exceeds the filing. Timing also differs: the March 21, 2025 Form D says the first sale had yet to occur and $0 had been sold; $2,834,590,561 was sold by March 20, 2026 and $4,346,290,561 by June 15, 2026. “Launched a $4.35B AI hedge fund in Mar 2025” wrongly attaches the later amount to launch.

5. **Three source rows contain exact numerical or evidence-set defects — DIFFERS.** ST116's seven listed FY2025 grants sum to **$146,860,783**, approximately $146.9M, not approximately $170M. ST121's exact Schedule A threshold is $15,153,667,777 × 2% = **$303,073,355.54**; if Schedule B reports whole dollars, the minimum integer strictly above it is $303,073,356. ST103's stated Schedule M values reproduce, but `research/daf-sponsors/` contains **18**, not 22, returns. The latter should say 18 on-disk returns or identify and register the four additional returns.

6. **Two investment-round records need source qualification — one DIFFERS and one UNVERIFIABLE.** Anthropic's Series C announcement confirms $450M and the named investors in IV03 but does not state a $4.1B post-money valuation; that cell needs a separate contemporary source or “not disclosed by Anthropic.” IV04's live CNBC URL now returns a 404 through the text proxy, and the Wayback CDX request timed out. More importantly, the cited URL and headline describe Anthropic as “in talks” to raise $750M, while the row presents a completed Series D on January 11, 2024 at $18.4B. This audit could not verify that completed-transaction formulation from the cited source. The manual route is the archived CNBC article plus a closing announcement, corporate filing, or reliable transaction database snapshot that distinguishes proposed from completed terms.

7. **Good Ventures's filings confirm the narrow negative; the historical grantee name needs precision — CONFIRMED with a text correction.** Its FY2025 Schedule B has exactly two contributors: the Dustin A Moskovitz Remainder Interest Trust, $1,395,695,354 of publicly traded securities received 2025-06-30, and Beneficial AI Foundation, $150,027. No Schedule B item names Anthropic or private stock. Total assets are exactly $10,107,955,038. The six displayed holdings reproduce: TSMC $508,854,795; SK Hynix $399,749,206; Broadcom $290,449,924; Vistra $202,021,342; Micron $184,134,391; Vertiv $178,712,948. VARA's fee is exactly $5,264,377. The $10M FY2024 grant is also real, but the filing's legal recipient is **Open Philanthropy Advisors Inc**, now Coefficient Giving Advisors. The node should retain both names rather than silently modernizing a historical filing.

8. **The quoted statements and board-observer wording reproduce — CONFIRMED.** Fresh Bluesky thread responses exactly match the saved ST110, ST112, and ST113 payload texts. The ST90/ST111 thread includes both the reply saying Good Ventures is a beneficiary of the wave via Anthropic and other investments and the root clause: “CG, via funding from Good Ventures, is surging budgets in 2026.” The archived Forbes pages contain “worth an estimated $500 million,” “early 2025,” and “an estimated stake of less than 0.8%.” Berger's fresh payload contains “He's since donated his stake (and not to us).” Tallinn's Postimees statement and refusal to publish percentages reproduce. The specified Stratechery capture contains “I'm a board observer at Anthropic” and the boardroom passage used on the card. The figure uses “observer,” and its only `director` occurrence is the clarifying phrase “not a director.”

9. **The equity arithmetic and display dimensions reproduce — CONFIRMED, with rounded-bound notation worth tightening.** Anthropic's Series H announcement states $65B raised and a $965B post-money valuation. Exactly 0.8% × $965B = $7.72B. The displayed $7.7B divided by $500M is 15.4, consistent with “×15.” The generator's `pw(7.7e9)` result is 10,786 px; one thirtieth is 359.5 px and truncates to the displayed 359 px, approximately 360 px. Full scale is 5.19 canvases of 2,080 px, so “about 10,800 px, five canvases” is a fair rounded description. The figure repeatedly calls $7.7B a ceiling, not a valuation. For exact logic, `<0.8%` implies `<$7.72B`; the current `≤$7.7B` is a one-decimal display approximation and should be labeled as such.

10. **The remaining investor, filing, and personnel links reproduce within their stated limits — CONFIRMED.** D.I. 10241-1 records Jane Street Global Trading's 3,332,833 shares for exactly $99,999,988 and the first FTX sale's 29,465,891 shares for $884,109,327. D.I. 16380 records 15,073,349 shares for $452,268,300. Anthropic's Series E–H releases reproduce the later amounts, valuations, and Jane Street participation; Series H names D.E. Shaw Ventures. Forbes says Hillspire bought exactly 20% of D.E. Shaw & Co., so the figure's “10–25%” is true but unnecessarily imprecise. Macroscopic's live page lists Redwood and the two Longview programs as grants and Anthropic A/B, Apollo, and Halcyon Venture Partners as impact investments. ARC's FY2024 filing names Benjamin Hoskin as a board member. Benton's own September 2 post says he left Anthropic to join METR for embedded assessment/incident-investigation work. These records establish the stated roles and transactions, not motive or influence.

## Row-by-row verdicts

### `investments.csv`

| Row | Verdict | Primary-source result |
|---|---|---|
| IV01 | **CONFIRMED** | Anthropic's release states $124M and names Tallinn as lead plus Moskovitz, Schmidt, McClave, and CERR. Anthropic does not disclose a valuation; the row labels its secondary estimate unverified. |
| IV02 | **CONFIRMED** | Anthropic states $580M and the listed investors. The FTX docket supports Alameda's approximately $500M position; the valuation in the note is expressly an inference, not a disclosed post-money value. |
| IV03 | **DIFFERS** | The issuer release confirms $450M and the named investors but contains no $4.1B post-money valuation. Correct issuer-supported value: not disclosed by Anthropic; cite a separate source for $4.1B. |
| IV04 | **UNVERIFIABLE** | Live CNBC via the text proxy returned 404; Wayback CDX timed out. The cited headline says “in talks,” not completed. Manually recover the archived article and an independent closing record before retaining the January 11 completion/$18.4B formulation. |
| IV05 | **CONFIRMED** | D.I. 10241-1 gives 29,465,891 shares for $884,109,327; the row's 29.5M/$884M are accurate rounded values. Jane Street is exactly 3,332,833 shares for $99,999,988. |
| IV06 | **CONFIRMED** | D.I. 16380 gives 15,073,349 shares for $452,268,300; the row's 15M/$452M are accurate rounded values and G Squared's line is present. |
| IV07 | **CONFIRMED** | Anthropic states $3.5B at $61.5B post-money and names Jane Street. |
| IV08 | **CONFIRMED** | Anthropic states $13B at $183B post-money and names Jane Street. |
| IV09 | **CONFIRMED** | Anthropic states $30B at $380B post-money and names Jane Street and D.E. Shaw Ventures. |
| IV10 | **CONFIRMED** | Anthropic states $65B at $965B post-money; it names Jane Street and D.E. Shaw Ventures and says $5B of previously committed capital came from Amazon. |
| IV11 | **CONFIRMED** | The retained WSJ article says a possible IPO could raise up to $100B at around $2T. The row correctly labels this reporting, not a transaction. |

### `stakes.csv`

| Row | Verdict | Primary-source result |
|---|---|---|
| ST26 | **CONFIRMED** | Series H names Jane Street and D.E. Shaw Ventures; individual investment amounts are not disclosed. |
| ST32 | **CONFIRMED** | The archived US Forbes page and AU reprint say the Anthropic stake was worth an estimated $500M. |
| ST33 | **CONFIRMED** | Both Forbes versions say it moved into a nonprofit vehicle in early 2025 so gains could be invested for philanthropy. The vehicle is not named. |
| ST41 | **CONFIRMED** | Postimees identifies Tallinn as an observer and quotes his explanation for declining a board seat; the first “large enough” clause is the outlet's characterization, as the row notes. |
| ST49 | **CONFIRMED** | Forbes says Hillspire bought exactly 20% of D.E. Shaw & Co. and does not mention Anthropic. The figure's 10–25% range contains the sourced value but should use 20%. |
| ST54 | **CONFIRMED** | Anthropic's Series A release names CERR; its Series B release names CERR again. Amounts are undisclosed. |
| ST78 | **CONFIRMED** | FY2025 Schedule B has exactly the two listed contributors and one noncash gift, described as publicly traded securities; no Anthropic/private-stock gift appears. |
| ST79 | **CONFIRMED** | The filing has 406 named corporate-stock issuers and the listed aggregate alternative-investment categories; no direct Anthropic holding is named. The row correctly says categories cannot exclude indirect exposure. |
| ST89 | **CONFIRMED** | Fresh fxtwitter payload reproduces Berger: “He's since donated his stake (and not to us).” |
| ST90 | **CONFIRMED** | Fresh Bluesky payload reproduces “GV is itself a beneficiary of that wave (via Anthropic and a number of other investments).” |
| ST91 | **CONFIRMED** | Archived Forbes says the couple have approximately $10B in Good Ventures Foundation “plus more in donor-advised funds” and its named largest holdings do not include Anthropic. It does not name DAF sponsors or account principals. |
| ST92 | **CONFIRMED** | The specified April 20 archive contains the less-than-0.8% and donated-last-year language; the figure uses it as a rounded ceiling, not a valuation. |
| ST93 | **CONFIRMED** | Fresh Bluesky payload reproduces Moskovitz's statement that “We fund people like METR and Redwood.” |
| ST94 | **CONFIRMED** | The completed 2025/2026 TEOS scan register has 11 hits; the retained snippets classify them as vendors/training, ARC program text, named foundation holdings, or a contributor. None identifies a Moskovitz/Tuna Anthropic vehicle. This is a bounded scan result, not proof about unfiled or later returns. |
| ST95 | **CONFIRMED** | Meta's 2020 proxy footnote identifies Tom Van Loben Sels as trustee of the Dustin Moskovitz Remainder Interest Trust and gives 6,830,855 Class B shares; the earlier proxy carries the 2008-annuity-trust predecessor. |
| ST96 | **CONFIRMED** | The retained NYT article gives the quoted 1%–2% ranges, approximately 300 investors, and Spark board-seat statement; it provides no METR-named funder percentage. This remains attributed press reporting. |
| ST97 | **CONFIRMED** | The retained WSJ article says private-investment gains included an Anthropic stake bought from the FTX estate; it does not disclose current shares or value. |
| ST98 | **CONFIRMED** | The fresh Äripäev capture contains “protsente ei kuuluta” and the other stated portfolio/management context; Tallinn does not disclose a percentage. |
| ST99 | **CONFIRMED** | The retained Meta, Asana, Kodiak, and Apercen SEC filings reproduce the listed ownership vehicles and roles. None identifies the Anthropic purchase vehicle. |
| ST100 | **CONFIRMED** | The two 990-PFs reproduce the 406/462 issuer counts, displayed FY2025 holdings, and stated year-over-year changes. “AI-infrastructure portfolio” is an editorial characterization, not a filing category. |
| ST101 | **DIFFERS** | Fee, entities, dates, officers, later amounts, investor counts, and 13F sequence reproduce. The figure differs: $0 and no first sale were reported at March 2025 launch; $4.346B is the June 2026 amount sold. |
| ST102 | **CONFIRMED** | The three 13F tables parse to 72/$4,734,560,970; 86/$9,944,995,059; and 123/$40,111,386,090. No table names Anthropic, which a 13F would not ordinarily cover as private stock. |
| ST103 | **DIFFERS** | Every stated count/amount pair found in the folder reproduces, including NPT 19/$1,183,079,981. The source field says 22 returns, but the on-disk evidence folder contains 18 XML returns. |
| ST104 | **CONFIRMED** | NPT FY2025 reports 19/$1,183,079,981, the $162,706,505 preferred-stock/crypto category, and 52 appraisals. It does not name donors or issuers. |
| ST105 | **DIFFERS** | The row's quoted webpage text is exact. The figure differs by changing named external funding partners “such as” SVCF/NPT into Moskovitz/Tuna's or Good Ventures's owned DAF accounts. |
| ST106 | **CONFIRMED** | NPT's year-end closely held equity values are $752,489,888, $737,806,285, and $1,734,031,057; FY2025's increase is exactly $996,224,772. No issuer or donor is disclosed. |
| ST107 | **CONFIRMED** | SVCF's 2024 Schedule I records exactly $1,591,322,838 to NPT and reproduces the listed grantee pattern. It identifies neither the originating account nor its principal. |
| ST108 | **CONFIRMED** | NPT FY2023–FY2025 Schedule I reproduces the listed network grants and has no METR or ARC recipient. These are sponsor-filed grants, not donor identifications. |
| ST109 | **DIFFERS** | All 19 grantee-and-amount matches reproduce against the 2,911-row Coefficient index. The row itself says the accounts remain unattributed; the figure's “their/its accounts” language discards that limitation. |
| ST110 | **CONFIRMED** | Fresh getPostThread text exactly equals the saved payload and contains “Our Anthropic shares are entirely in our foundation - no personal benefit.” |
| ST111 | **CONFIRMED** | The fresh ancestor chain contains the full root clause naming Good Ventures and the anticipated-wave language. |
| ST112 | **CONFIRMED** | Fresh getPostThread text exactly equals the saved payload and contains “all Anthropic holdings are in the foundation, dedicated to charity.” |
| ST113 | **CONFIRMED** | Fresh getPostThread text exactly equals the saved payload and contains the approximately $20B/foundation and Anthropic sentences. It does not define a legal entity. |
| ST114 | **CONFIRMED** | The specified Wayback capture says grants typically were recommended to the Open Philanthropy Project fund, an advised fund at SVCF. It does not identify the Anthropic recipient account. |
| ST115 | **CONFIRMED** | The IRS file has exactly 98,802 data rows. No Dustin/Cari/CTF-family match appears; three Apercen and four 314 Lytton records are unrelated trusts, as the row states. |
| ST116 | **DIFFERS** | Each of the seven named NPT grants reproduces, but their exact same-measure sum is $146,860,783, not approximately $170M. The $50M Coefficient Giving Advisors line is exact and does not identify a donor. |
| ST117 | **CONFIRMED** | The freshly fetched Blue Owl S-1 selling-stockholder table contains both “Moskovitz Investments LLC” and “THE CTF TRUST UAD 122712.” It does not show which vehicle bought Anthropic. |
| ST118 | **CONFIRMED** | The specified Wayback capture contains both observer and boardroom passages. The figure accurately says observer and explicitly says not a director. |
| ST121 | **DIFFERS** | Correct arithmetic is $303,073,355.54, not $303,073,355. The instructions and NPT Schedule O support the public-inspection route; names/addresses can remain redacted. |
| ST125 | **DIFFERS** | Four clients, Q20 50%, the asset mix, and the inference that at least one charitable client invested all reproduce. The ADV does not show that the investing charity is Good Ventures-linked, contrary to the figure. |
| ST127 | **CONFIRMED** | VARA identifies Benjamin Hoskin; ARC's FY2024 officer list names him as BOARD MEMBER and marks the director indicator. |
| ST133 | **DIFFERS** | All posted Schedule B totals/descriptions reproduce and “Anthropic” does not appear. Because the private-equity issuers are unnamed and transfer-date value is unknown, Vanguard is not excluded. |

### Other scoped CSVs

| Row | Verdict | Primary-source result |
|---|---|---|
| J02 | **UNVERIFIABLE** | Anthropic confirms McClave in Series A/B, and the two retained recent BEMC filing renders show only the described grantees. This audit could not substantively recover all five FY2020–FY2024 XMLs: direct IRS and ProPublica endpoints returned 404/403, and the proxy returned anti-bot pages. Manual route: retrieve object IDs 202210469349100116, 202323199349109357, 202333199349106948, 202403209349103005, and 202523219349100137 from the corresponding IRS TEOS bulk archives, then recount Part XV. |
| J08 | **CONFIRMED** | METR's own about page names Schmidt Sciences; Anthropic's Series A release names Eric Schmidt. No source states the METR grant amount, as the row says. |
| K01 | **DIFFERS** | METR's primary wording exactly says “frontier AI companies” and “significant free tokens.” The row correctly leaves companies unspecified; the figure incorrectly assigns the tokens specifically to Anthropic. |
| S13 | **DIFFERS** | Benton's own September 2, 2026 post confirms that he left Anthropic to join METR for embedded assessment/incident investigations. The figure fact is supported, but the CSV's `source_url` is an NBC article rather than that primary post and should be replaced or supplemented with the self-post. |
| RW31 | **CONFIRMED** | METR's post says its OpenAI review was “with Redwood Research.” |
| RW32 | **CONFIRMED** | METR's report names a Redwood staff member contracting with METR for the OpenAI investigation. |
| RW33 | **CONFIRMED** | OpenAI's technical report names METR and Redwood in the third-party assessment. |
| RW34 | **CONFIRMED** | Redwood's own cross-post describes its chief scientist's participation in the OpenAI work. |
| RW35 | **DIFFERS** | The Anthropic announcement confirms an eight-week investigation agreement with METR but never names Redwood or a subcontractor. The row records that absence; the figure contradicts it by saying Redwood is subcontractor on both investigations. |

### Check-6 context rows from `money_flows.csv`

| Row | Verdict | Primary-source result |
|---|---|---|
| M139 | **CONFIRMED** | Macroscopic's live grants page lists Redwood Research. No amount is disclosed. |
| M140 | **CONFIRMED** | The same page lists the Consortium for Digital Sentience Research and Applied Work and the hardware-enabled-mechanisms RFP under Longview support. |
| M141 | **CONFIRMED** | Macroscopic's impact-investment list names Apollo Research alongside Anthropic Series A/B and the other stated investments. |
| M142 | **CONFIRMED** | The impact-investment list names Halcyon Venture Partners. This is the venture arm, not a grant to Halcyon Futures or METR. |

## Validation and limits

The check script's content comparisons used bounded standard-library JSON/XML/CSV parsing. Fresh Bluesky responses equal the saved payloads; the gzip-encoded Wayback responses were decompressed in memory; all 19 DAF matches were independently joined by grantee and exact amount; the three 13F totals were recomputed from their information tables; and all successful fetch artifacts match their registered hashes. Transport success was not treated as substantive success where a server returned a challenge or 404 body.

The completion gate is `python3 scripts/audit.py`. It checks figure/PNG parity and whether referenced IDs exist; it does not validate attribution, quotations, arithmetic, source authority, or semantic use of a row. It exited 0. Last line: `figures=29 pngs=29 row_ids_in_research=2213 cited=1111 missing=0`.

## Figure text recommendations

1. Replace every ownership assertion about SVCF/NPT with: **“Coefficient-recommended grants were paid from unattributed accounts at SVCF and NPT; no reviewed document identifies the account principals or the recipient of the Anthropic shares.”** Remove “their accounts,” “its DAF accounts,” and “NPT is the leading candidate,” or label the latter explicitly as an inference rather than a documented attribution.
2. Replace “Anthropic → METR: free tokens” with **“Frontier AI companies (unspecified) → METR: free tokens, unquantified (K01).”**
3. Change Redwood to **“contractor on the OpenAI investigation; no reviewed Anthropic/METR announcement names Redwood for the Anthropic investigation.”** Remove “subcontractor on both investigations” and the corresponding footnote claim.
4. Remove “Vanguard's posted Schedule B excludes it.” Use **“Vanguard Schedule B is posted but its private-equity issuers and donor names are undisclosed; unresolved.”**
5. Replace “a Good Ventures-linked charity is one of its LPs” with **“at least one of VARA's two unidentified charitable clients invested in VAR AI Fund.”** Replace “launched a $4.35B AI hedge fund in Mar 2025” with **“launched VAR AI Fund in Mar 2025 ($0 sold at filing); $4.35B sold by Jun 2026.”**
6. Label the historical payment **“$10M to Open Philanthropy Advisors Inc (now Coefficient Giving Advisors), FY2024.”**
7. Replace “the investor was Moskovitz personally until 2025” with **“Anthropic named Moskovitz as the investor; the purchasing vehicle and current recipient account are undisclosed.”**
8. Use Forbes's exact **20%** Hillspire/D.E. Shaw figure instead of 10–25%.
9. If displaying mathematical precision, label the band **“< $7.72B (≈$7.7B ceiling)”**; otherwise explicitly say `≤$7.7B` is rounded to one decimal place. Keep “ceiling, not a valuation,” “×15,” the approximately 360 px scaled width, and the approximately 10,800 px/five-canvas comparison.
