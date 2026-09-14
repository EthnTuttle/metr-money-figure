# S12 — Anthropic per-share price and share-count ladder (Series A 2021 → Series H 2026)

Built 2026-09-14. Fetch-only lane; no existing file edited. Files: `ladder.csv` (LD01–LD22), `holder_values.csv`, saved pages under `docs/`.

## 1. Headline findings

1. **The per-share ladder is documented at every priced round from Series D onward, and at Series A–C via one vendor.** Prices: A $2.57 → B $11.23 → C $11.23 (flat) → D $30.00 → E $56.09 → F $140.97 → G $259.14 → H $589.01. The FTX docket (primary) fixes $30.0045 in Mar 2024; a Delaware COI (via Prime Unicorn Index) fixes Series D $30 / Series E $56.09; Hustle Fund and Forge independently give Series H-1 $589.01. Series F ($140.97) and Series G ($259.14) rest on Forge's reproduction of the COI alone.
2. **Fully-diluted share count roughly tripled from ~567M (Jan 2024, from the FTX motion's 7.84%) to ~1,638M (May 2026, = $965B ÷ $589.01).** So the headline valuation rose 52× ($18.4B → $965B) while the price per share rose 19.6× ($30 → $589.01). Dilution, not price, explains the other ~2.7×.
3. **Jane Street's 3,332,833 shares (cost $99,999,988, D.I. 10241-1) were worth $1.963B at the Series H price and ~$3.08B at the $925 secondary print (Aug 2026)** — 19.6× and 30.8× on that one lot, before any of its undisclosed Series E/F/G/H participations.
4. **FTX-estate calibration:** the 44,465,891 shares sold for ~$1.34B in 2024 would have been worth $26.19B at the Series H price and ~$41.1B at $925.
5. **Anthropic's S-1 is not public as of 2026-09-14.** EDGAR full-text search for S-1 / S-1/A / DRS / DRS/A filings since 2026-06-01 containing "Anthropic" returns only SpaceX, Gloo Holdings, QumulusAI, Oura and Miluna filings (mentions of Anthropic as a customer/competitor), and no filing by Anthropic, PBC as filer. The June 1 2026 submission was a confidential draft (research/investments.csv IV10). No beneficial-ownership table exists to extract.
6. **No stock split found.** Every price in the ladder is monotonic and consistent with the same share unit (Series B $11.23 × 44,465,891 FTX shares = $499.4M ≈ the $500M cost; $30.0045 × 29,465,891 = $884.1M; Series H $589.01 × 70,096,048 = $41.29B). Stockanalysis.com: "Anthropic has split 0 times." Forge lists conversion ratio 1.0x on every series.

## 2. The ladder

| row | date | event | $/share | post-money | implied FD shares | source type |
|---|---|---|---|---|---|---|

| LD01 | 2021-05-28 | Series A (Forge) | $2.57 | $0.62B | — | Forge cap-table reproduction |
| LD02 | 2022-04-29 | Series B (Forge dates the COI 02/03/2023; Anthropic announced 2022-04-29) | $11.23 | $4.02B | — | Forge cap-table reproduction |
| LD03 | 2023-05-23 | Series C-1 and C-2 (Forge) | $11.23 | $4.10B | — | Forge cap-table reproduction + Anthropic release |
| LD04 | 2023-10-27 | Series D-1 (Google tranche, Forge) | $30.00 | $14.55B | — | Forge cap-table reproduction |
| LD05 | 2024-01-11 | Series D (Menlo-led $750M at $18.4B post; Forge D-2 $27.00 / D-3 $30.00 dated 03/27/2024, Amazo | $30.00 | $18.40B | 613.3M | Prime Unicorn Index (Delaware COI) + Forge + CNBC |
| LD06 | 2024-03-22 | FTX estate secondary sale #1: 29,465,891 Series B Preferred shares to 24 purchasers for $884,10 | $30.00 | — | — | Bankruptcy docket (primary) |
| LD07 | 2024-06-01 | FTX estate secondary sale #2: remaining 15,000,000 shares at ~$30 | $30.00 | — | — | The Block (press; docket notice not retrieved) |
| LD08 | 2024-11-22 | Series E-3 / E-4 / E-5 (Amazon note conversions, Forge; matches Amazon's Q1-2025 conversion) | $56.09 | $41.07B | — | Forge cap-table reproduction + Amazon 10-Q |
| LD09 | 2025-03-03 | Series E-1 ($56.09) and E-2 ($20.93) — $3.5B at $61.5B post | $56.09 | $61.50B | 1,096.5M | Delaware COI via Prime Unicorn Index; Forge; Anthropic relea |
| LD10 | 2025-05-05 | Employee tender offer #1 at $61.5B | $56.09 | $61.50B | 1,096.5M | SecondaryLink (press) |
| LD11 | 2025-09-02 | Series F-1 ($140.97) and F-2 ($20.93) — $13B at $183B post | $140.97 | $183.00B | 1,298.1M | Forge cap-table reproduction + Anthropic release |
| LD12 | 2026-02-12 | Series G-1/G-2 ($259.14), G-4 ($233.22), G-3 ($20.93) — $30B at $380B post | $259.14 | $380.00B | 1,466.4M | Forge cap-table reproduction + Anthropic release |
| LD13 | 2026-02-24 | Employee tender offer #2 at $350B (= Series G pre-money); closed ~2026-04-08 | — | $350.00B | — | SecondaryLink + Bloomberg (press) |
| LD14 | 2026-05-28 | Series H-1/H-2 ($589.01), H-4 ($50.48), H-3 ($20.93) — $65B at $965B post | $589.01 | $965.00B | 1,638.3M | Forge cap-table reproduction + Hustle Fund + Anthropic relea |
| LD15 | 2025-12-31 | US Marshals sale of forfeited Ellison ($10M) and Singh ($40M) Series B shares — during 2025, pr | — | — | — | Press citing Business Insider (2026-08-31); BI original not  |
| LD16 | 2025-02-11 | Secondary indication: Caplight | $70.00 | — | — | Secondary-market indication (not a transaction) |
| LD17 | 2026-05-12 | Secondary indication: Nasdaq Private Market estimate | $550.97 | — | — | Secondary-market indication (not a transaction) |
| LD18 | 2026-05-28 | Secondary indication: Notice.co algorithmic price | $572.41 | — | — | Secondary-market indication (not a transaction) |
| LD19 | 2026-06-05 | Secondary indication: Notice.co consensus | $625.26 | — | — | Secondary-market indication (not a transaction) |
| LD20 | 2026-08-11 | Secondary transaction observed by Prime Unicorn Index | $925.00 | — | — | Secondary transaction (price observed by index; size/counter |
| LD21 | 2026-08-28 | Secondary indication: Nasdaq Private Market estimate | $773.98 | — | — | Secondary-market indication (not a transaction) |
| LD22 | 2026-09-14 | Secondary indication: Notice.co algorithmic price | $870.36 | — | — | Secondary-market indication (not a transaction) |

Implied FD shares = post-money ÷ price, computed only where both come from sources (LD05, LD09, LD10, LD11, LD12, LD14). Series A–D-1 posts are Forge's own figures, so those implied counts are given in the notes column only.

### Arithmetic shown

- **FTX sale #1 (LD06):** $884,109,327 ÷ 29,465,891 sh = **$30.0045/sh**. Jane Street: $99,999,988 ÷ 3,332,833 = $30.0044. ATIC: $499,999,999 ÷ 16,664,167 = $30.0045.
- **FD shares Jan 2024 (from the motion):** 44,465,891 sh ÷ 0.0784 = **567.2M**; × $30.0045 = $17.0B (vs the $18.4B Series D post: an 8% gap — LD05 note).
- **Series B price check:** $500M ÷ 44,465,891 = $11.24 ≈ Forge's $11.23. (FTX said it paid ~$500M; the 44,465,891 = 29,465,891 + 15,000,000 from the two 2024 sales.)
- **Series D:** $18.4B ÷ $30.00 = **613.3M** FD.
- **Series E:** $61.5B ÷ $56.09 = **1,096.5M** FD (×1.79 vs Series D).
- **Series F:** $183B ÷ $140.97 = **1,298.1M** FD (×1.18). Check: $12.58B ÷ 89,240,219 = $140.97.
- **Series G:** $380B ÷ $259.14 = **1,466.4M** FD (×1.13). Check: $15.16B ÷ 58,508,869 = $259.11.
- **Series H:** $965B ÷ $589.01 = **1,638.4M** FD (×1.12). Check: $41.29B ÷ 70,096,048 = $589.04; $18.2B ÷ 30,907,511 = $588.85.
- **Price multiples:** H/D = 589.01/30 = 19.6×; H/E = 10.5×; H/F = 4.18×; H/G = 2.27×. Valuation multiples over the same spans: 52.4×, 15.7×, 5.27×, 2.54×.
- **$925 secondary (LD20):** 925/589.01 = 1.570 → PUI's "57% increase from its prior observed price" is measured from the Series H-1 price; 925 × 1,638.4M = $1.52T ≈ PUI's "~$1.50 trillion".

### Conversion tranches at legacy prices (why the round totals exceed the new money)

Forge's table shows, inside each round, tranches priced far below the round price: $20.93 at E-2 (77.1M sh), F-2 (20.1M), G-3 (13.3M), H-3 (92.8M) — 203.2M shares, $4.25B in total — and $50.48 / $53.28 at E-4/E-5 (Nov 2024, Amazon) and again $50.48 at H-4 (70.7M sh, $3.57B). These are convertible-note conversions at fixed prices, not priced sales. Amazon's 10-Qs confirm conversions to "nonvoting preferred stock" in Q1 2025 (gain $3.3B), Q3 2025 ($2.3B) and Q1 2026 ($4.5B). Forge attributes the Nov-2024 E-3/E-4/E-5 tranches to Amazon; it does not name the $20.93 holder. Anthropic's press "$65B Series H" therefore = ~$59.5B H-1/H-2 new money at $589.01 + ~$5.5B of conversions (H-3/H-4), matching its own line that $15B was "previously committed investments from hyperscalers".

## 3. Holder values


| holder | shares | at date | price | value | rows |
|---|---|---|---|---|---|
| Jane Street Global Trading LLC (Mar-2024 purchase on | 3,332,833 | 2024-03-22 | $30.00 | $0.100B | LD06 |
| Jane Street Global Trading LLC (Mar-2024 purchase on | 3,332,833 | 2025-03-03 | $56.09 | $0.187B | LD09,LD10 |
| Jane Street Global Trading LLC (Mar-2024 purchase on | 3,332,833 | 2025-09-02 | $140.97 | $0.470B | LD11 |
| Jane Street Global Trading LLC (Mar-2024 purchase on | 3,332,833 | 2026-02-12 | $259.14 | $0.864B | LD12 |
| Jane Street Global Trading LLC (Mar-2024 purchase on | 3,332,833 | 2026-05-28 | $589.01 | $1.963B | LD14 |
| Jane Street Global Trading LLC (Mar-2024 purchase on | 3,332,833 | 2026-08-11 | $925.00 | $3.083B | LD20 |
| Jane Street Global Trading LLC (Mar-2024 purchase on | 3,332,833 | 2026-09-14 | $870.36 | $2.901B | LD22 |
| FTX estate calibration (44,465,891 sh had it held) | 44,465,891 | 2024-03-22 | $30.00 | $1.334B | LD06 |
| FTX estate calibration (44,465,891 sh had it held) | 44,465,891 | 2025-03-03 | $56.09 | $2.494B | LD09,LD10 |
| FTX estate calibration (44,465,891 sh had it held) | 44,465,891 | 2025-09-02 | $140.97 | $6.268B | LD11 |
| FTX estate calibration (44,465,891 sh had it held) | 44,465,891 | 2026-02-12 | $259.14 | $11.523B | LD12 |
| FTX estate calibration (44,465,891 sh had it held) | 44,465,891 | 2026-05-28 | $589.01 | $26.191B | LD14 |
| FTX estate calibration (44,465,891 sh had it held) | 44,465,891 | 2026-08-11 | $925.00 | $41.131B | LD20 |
| FTX estate calibration (44,465,891 sh had it held) | 44,465,891 | 2026-09-14 | $870.36 | $38.701B | LD22 |

Jane Street multiples on the Mar-2024 lot alone: 1.87× (E), 4.70× (F), 8.64× (G), 19.63× (H), 30.8× ($925). Its share of FD equity fell from 0.59% (3.33M/567M, Jan 2024 basis) to 0.20% (3.33M/1,638M) at Series H — without buying more it would have been diluted by two-thirds. Jane Street is named as a participant in Series E, F, G and H (research/investments.csv IV07–IV10) with amounts undisclosed; nothing is added for those.

FTX estate: actual 2024 proceeds ≈ $884.1M + ~$450M ≈ $1.34B on ~$500M cost (2.7×). Had it held: $26.19B at Series H (52×), $41.1B at $925. The "US Gov lost $4.7B" press math for the Ellison/Singh shares uses the same ladder on ~4.45M shares ($50M ÷ $11.23): × $56.09 = $250M, × $140.97 = $628M, × $259.14 = $1.15B, × $589.01 = $2.62B — which reproduces every analyst range quoted (PitchBook $250M–$630M; UCLA $300M–$1.1B; "now $2.6B–$5.0B").

## 4. Public-company holders' carrying values (context for the ladder; not per-share)

| filer | as of | figure | quote (verbatim) |
|---|---|---|---|
| Amazon 10-K FY2023 | Q3 2023 | $1.25B note | "In 2023, we invested $1.25 billion in a note from Anthropic, PBC, which is convertible into equity." |
| Amazon 10-Q Q1 2024 | Q1 2024 | +$2.75B note | "In Q1 2024, we invested $ 2.75 billion in a second convertible note" |
| Amazon 10-K FY2024 | 2024-12-31 | notes FV $13.8B on $5.3B cost | "From Q3 2023 to Q4 2024, we invested $ 5.3 billion in convertible notes from Anthropic ... as of December 31, 2024 had an estimated fair value of approximately $ 13.8 billion" |
| Amazon 10-Q Q2 2025 | 2025-06-30 | $15.1B notes+pref | "As of June 30, 2025, the estimated fair value of our convertible notes and amounts recorded for nonvoting preferred stock investments was approximately $ 15.1 billion" |
| Amazon 10-Q Q3 2025 | 2025-09-30 | notes $23.7B + pref $14.8B | "As of September 30, 2025, the amount recorded on our consolidated balance sheet for nonvoting preferred stock was approximately $ 14.8 billion" / "estimated fair value of our convertible notes ... approximately $ 23.7 billion" |
| Amazon 10-K FY2025 | 2025-12-31 | notes $45.8B + pref $14.8B on $8.0B cost | "As of December 31, 2025, the estimated fair value of our convertible notes recorded on our consolidated balance sheet was approximately $ 45.8 billion, and the associated pre-tax unrealized gain ... was $ 39.5 billion" |
| Amazon 10-Q Q1 2026 | 2026-03-31 | notes $42.2B + pref $32.0B | "As of December 31, 2025 and March 31, 2026, the amounts recorded on our consolidated balance sheets for nonvoting preferred stock were approximately $ 14.8 billion and $ 32.0 billion" |
| Amazon 10-Q Q2 2026 | 2026-06-30 | notes $97.9B + pref $92.5B (cost $8.0B notes + $10.0B pref) | "As of December 31, 2025 and June 30, 2026, the amounts recorded ... for nonvoting preferred stock were approximately $ 14.8 billion and $ 92.5 billion" / "estimated fair value of our convertible notes ... approximately $ 45.8 billion and $ 97.9 billion" / "In Q2 2026, we invested $ 5.0 billion in Anthropic Series G nonvoting preferred stock" / "investing $ 5.0 billion in Anthropic Series H nonvoting preferred stock" / "upward adjustments of approximately $ 50.5 billion in Q2 2026" |
| Alphabet 10-K FY2024 / FY2025, 10-Q Q1/Q2 2026 | 2024-12-31 → 2026-06-30 | non-marketable equity securities (measurement alternative): $35.5B → $64.1B → $101.3B → $124.3B | "As of June 30, 2026, the carrying value of our non-marketable equity securities accounted for under the measurement alternative was $ 124.3 billion, of which $ 87.9 billion was remeasured at fair value during the three months ended June 30, 2026" — Alphabet never names Anthropic; Bloomberg 2026-07-23: "this value is 'primarily' driven by one investment, which is a reference to Alphabet's stake in Anthropic, according to a person familiar" |
| Google 14% (court) | Mar 2025 | ~14%, capped 15% | Yahoo/Barchart 2026: "Court documents put it at roughly 14% of Anthropic in straight equity, contractually capped at 15%"; Motley Fool 2026-06-16: "The New York Times also reported in 2025, citing court documents, that Alphabet owned about 14% of Anthropic." NYT original not retrieved. |
| SK Telecom | 2023-08 → 2025-12 | $100M (Aug 2023) → ~0.3% stake, carried ~₩1.3T | TechTimes 2026-06-10 (citing UPI): "taking a stake of roughly 0.7% that has since been diluted to about 0.3%"; "SKT carried the holding at about 1.3 trillion won — roughly $970 million — at the end of last year". DART filing not fetched. |

Sanity check on Amazon: $97.9B + $92.5B = $190.4B at 2026-06-30 on a $965B post = 19.7% (notes as-converted + preferred), consistent with Yahoo's "mid-to-high teens". Alphabet's $124.3B ÷ $965B = 12.9% (measurement-alternative carrying value lags the round price). SK Telecom's 0.3% × $965B = $2.9B vs its ₩1.3T (~$0.97B) end-2025 carrying value at the $183B Series F mark: 0.3% × $183B = $0.55B, so SKT's stake is closer to ~0.5% or its carrying mark is above cost — flagged, not resolved.

## 5. Gaps

1. **Series A/B/C per-share prices and post-moneys** rest on Forge alone ($2.57 / $11.23 / $11.23; posts $623M / $4.02B / $4.55B). Only Series B is cross-checked (FTX cost ÷ FTX shares). Anthropic disclosed $4.1B for Series C, not Forge's $4.55B.
2. **Series F ($140.97) and Series G ($259.14)** have one source (Forge). Prime Unicorn Index says the Series G share price was "previously reported" but its post is paywalled/not retrieved.
3. **Employee tender #2 (Feb–Apr 2026)**: no per-share price published anywhere found; $350B "same value as the February round" implies the Series G price by inference only. Amount actually sold undisclosed.
4. **US Marshals sale of Ellison/Singh shares (2025)**: no price, date, buyer, or share count disclosed; Business Insider original (Aug 31 2026) not retrieved (URL not found; BI 404 on guessed slug). ~4.45M-share count is arithmetic from the Series B price.
5. **FTX motion (D.I. 6952, 2024-02-03) and the June 2024 second-sale notice**: Kroll's site returns CloudFront 403 to direct download; only D.I. 7782-1 (revised proposed order, via r.jina.ai), D.I. 10241 + Exhibit 1 (RECAP), and D.I. 12844 (RECAP) were obtained. The "7.84% ... fully diluted" language is quoted from Unchained Crypto and CoinDesk reporting on the motion, not from the PDF.
6. **Dilution between rounds** is inferred from post ÷ price; Anthropic has never published a share count. The Series D→E jump (613M → 1,097M) is only partly explained by the $20.93 and Amazon conversion tranches (~129M sh) and must include large option-pool/RSU issuance and note-as-converted accounting — unquantified.
7. **Series D 613M vs 567M (FTX 7.84%)** discrepancy unresolved.
8. **Google's 14%** — court filing itself (NYT, Mar 2025) not retrieved; Alphabet's filings never name Anthropic.
9. **SK Telecom** — DART disclosure not fetched; stake % (0.3%) from UPI via TechTimes only.
10. **Nasdaq Private Market / Forge Price** company-level marks are behind login ("Price not yet available" on Forge; NPM masks round prices with XXXXX). Hiive's ~$1,303–$1,447 are SPV-unit asks. Secondary figures are indications except PUI's $925 observed transaction (size undisclosed).
11. **Bloomberg articles**: quotes taken from the WebFetch render; saved `docs/bloomberg-*.jina.txt` are paywall shells (title/date only).
12. **Caplight** redirects to a demo-scheduling page; no data retrieved beyond PUI's Feb-2025 citation of a $70 indication.

## 6. Sources saved in docs/

- `ftx-deb-188450-10241.1.pdf/.txt` — D.I. 10241-1 Exhibit 1, List of Purchasers (primary; Jane Street 3,332,833 sh / $99,999,988; total 29,465,891 sh / $884,109,327)
- `ftx-deb-188450-10241.0.pdf/.txt` — D.I. 10241 Notice of Proposed Sale (2024-03-22; cites motion D.I. 6952 and order D.I. 8215; "Series B Preferred Stock")
- `ftx-deb-188450-12844.0.pdf/.txt` — D.I. 12844 affidavit of service
- `kroll-revised-order-jina.txt` — D.I. 7782-1 revised proposed sale-procedures order (2024-02-21), incl. the Sale Disclosures rule "(A) a list of each purchaser, the number of Anthropic Shares to be purchased, and the aggregate purchase price to be paid"
- `forge-anthropic-ipo-jina.txt` — Forge round/price/share table (Series A → H-4)
- `notice-anthropic-jina.txt` — Notice.co ($870.36, round list; its per-round PPS/share fields are masked placeholders "lO.O / lOO,OOO")
- `amzn-2023*.htm/.txt … amzn-20260630-10q.htm/.txt` — eleven Amazon 10-K/10-Q filings (raw HTML + flattened text)
- `goog-20241231, goog-20251231, goog-20260331, goog-20260630 .htm/.txt` — Alphabet 10-K/10-Q
- `efts-*.json` — EDGAR full-text search results (Amazon, Alphabet, S-1/DRS since 2026-06-01, entity search); `goog-submissions.json`
- `cl-ftx-anthropic-entries.json`, `cl-ftx-anthropic-jina.txt` — CourtListener RECAP index for 22-11068 "Anthropic"
- press: `secondarylink-*`, `hustlefund-*`, `primeunicorn-*`, `coindesk-*`, `theblock-*`, `unchained-*`, `cryptonews-*`, `cryptotimes-*`, `fortune-*`, `anthropic-series-h`, `yahoo-*`, `fool-*`, `eciks-*`, `augment-*`, `nasdaqprivatemarket-*`, `public-com-*`, `techtimes-*`, `bloomberg-*` (shells)
- `wb-kroll-cdx.txt` — Wayback CDX listing of Kroll FTX PDFs (no capture of the Anthropic sale docs); `ddg-*.txt`, `bing-*.txt` — failed search-engine captures

EDGAR filers with "Anthropic" in the name (full-text entity search, 2026-06-01 → 2026-09-14): WU Anthropic LP (Form D, 2026-06-01), Anthropic Capital Fund, LP (D/A, 2026-07-30), Coastline Venture Partners Anthropic LLC (Form D, 2026-07-23) — all SPVs/feeder funds, none is Anthropic, PBC.
