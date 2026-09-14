# S10-pay: what METR pays vs what it posts vs what critics said

Built 2026-09-14 (fetches 08:33-08:38 UTC). Fetch-only; no existing file edited. Data: `pay.csv` (79 rows, PY01-PY79). Saved pages under `docs/` (live Lever postings, metr.org/careers, BI direct + Jingletree copy, HN thread, Redwood/Epoch/Apollo careers, levels.fyi, and `docs/wayback/` raw captures; Wayback `id_` bodies were gzip and are decoded to `*.dec.html` / `*.txt`). 990 extraction script output: `docs/990-extract-raw.txt`. Fetch log with HTTP codes: `docs/fetch-times.txt`.

## 1. What the Form 990 shows (paid figures)

**METR FY2024** (EIN 99-1219864; first return; short year **2024-05-01 to 2024-12-31 = 8 months**; e-filed 2025-11-16). Part VII, reportable compensation from METR / from related org (ARC, Jan-Apr 2024) / other:

| Person (as filed) | Title | METR | ARC (related) | Other |
|---|---|---:|---:|---:|
| Maksym Taran | Technical staff | 243,560 | 0 | 0 |
| Rajiv Dattani | COO and Treasurer | 230,384 | 0 | 630 |
| Katharyn Garcia | Technical staff | 226,183 | 0 | 4,948 |
| Ben West | Member of technical staff (key employee) | 215,587 | 0 | 5,048 |
| Emma Abele | CEO/COO | 190,395 | 52,375 | 6,849 |
| Tao Lin | Technical staff | 184,335 | 84,127 | 5,993 |
| Elizabeth Barnes | CTO/CEO | 172,737 | 75,637 | 6,416 |
| Chris Painter | Member of policy staff (key employee) | 167,556 | 84,123 | 7,358 |
| Hannes Hjalmar Wijk | Technical staff | 160,170 | 67,212 | 6,486 |
| Harold Broadley | Technical staff | 144,693 | 0 | 7,674 |
| Kyle Scott | Secretary and Treasurer | 141,577 | 94,127 | 630 |
| Adam Gleave | Director (0.5 h/wk) | 0 | 0 | 0 |

Totals: reportable from org $2,077,177; other comp $52,032; **18 individuals over $100K** (in 8 months). Schedule J Part II: bonus $0, deferred $0 for every listed person; base = reportable. Schedule J Part I: compensation committee, independent consultant, other orgs' 990s, written contracts, compensation survey, board approval all checked; equity-based comp 0. Schedule O: "THE OPERATIONS TEAM CONTRACTED OUR LAW FIRM TO DO AN INDEPENDENT THIRD-PARTY COMPENSATION SURVEY, LOOKING AT INDUSTRY DATA AND FORM 990 OF SUPPORTING ORGANIZATIONS. THE BOARD THEN APPROVES THE COMPENSATION."

Part IX: line 5 officers/key employees **$1,118,235**; line 7 other salaries and wages **$2,962,402**; line 9 benefits $119,825; line 10 payroll taxes $304,718; Part I line 15 total **$4,505,180** (= 54.7% of $8,234,524 expenses). Part V line 2a employees (W-2s): **38**. Line 24 also lists "DATA & RESEARCH CONTRAC" $1,103,985 and "RECRUITMENT" $184,544; one contractor over $100K (Qally's, research contractor, $147,200).

**Arithmetic (short year caveat applies to every line):**
- Wages (lines 5+7) $4,080,637 / 38 W-2s = **$107,385 per W-2 for 8 months -> $161,078 annualized** (x 12/8).
- Salaries+benefits+taxes (line 15) $4,505,180 / 38 = $118,557 -> **$177,836 annualized**.
- The 38 W-2 count includes anyone paid during the period, so the average is pulled down by partial-period hires; the true annualized average per full-time-equivalent is higher than $161K but cannot be computed from the 990.
- Highest single 8-month figure, Taran $243,560, would be ~$365K if pro-rated to 12 months; the 990 does not say whether he was employed the full 8 months, so that is an upper-bound illustration, not a paid annual figure.
- Barnes' calendar-2024 total from both entities: 172,737 + 75,637 = $248,374 reportable (+$6,416 other). ARC's FY2024 return mirrors the Scott row (94,127 ARC / 141,577 METR) and lists METR as a related org on Schedule R.

**ARC FY2023** (pre-spin-out, full calendar year; 28 employees): Hilton $298,652; Xu $224,851; **Barnes (Evals Project Lead) $224,576**; Miles $203,601; Wijk $194,290; Scott $151,507; Christiano $0. 14 individuals over $100K. Lines 5+7 = $3,144,696 / 28 = **$112,311 per W-2 (full year)**; line 15 $3,479,531 / 28 = $124,269.

**ARC FY2024** (calendar year; 38 W-2s, most partial-year because evals staff moved to METR on 2024-05-01): Hilton (President) $328,284; Neyman $239,060; Matolsci $200,337; Xu $197,284; Scott $94,127 (+$141,577 from METR). 6 over $100K. Lines 5+7 = $2,774,968 / 38 = $73,025 (not meaningful as an annual average for the reason above). Schedule O: "ALL STAFF ARE SUBJECT TO SALARY BANDS AS RECOMMENDED IN AN INDEPENDENT COMPENSATION SURVEY OF COMPARABLE ORGANIZATIONS ... THE CURRENT EXECUTIVE DIRECTOR'S COMPENSATION WAS DETERMINED WITHIN THIS POLICY AND DID NOT INCREASE UPON PROMOTION FROM INDIVIDUAL RESEARCHER TO THE ED ROLE."

**Redwood Research** (comparison): TY2024, 6 employees: Greenblatt (Chief Scientist) **$314,922**; Shlegeris (CEO) $272,164. TY2023, 34 employees: Greenblatt $314,931; lines 5+7 $3,320,863 / 34 = $97,672 per W-2. Schedule O says Redwood benchmarked against "REPORTED SALARIES FOR MACHINE LEARNING ENGINEERS IN THE BAY AREA", "OFFER LETTERS RECEIVED BY INDIVIDUALS ON THE STAFF FROM OTHER ORGANIZATIONS", and "NONPROFIT REPORTED SALARIES FROM SIMILAR ORGANIZATIONS SUCH AS OPENAI."

Bottom line from filings: the highest reportable compensation on any METR or ARC return is Hilton's $328,284 (ARC 2024); at METR itself the top is $243,560 for an 8-month period. No 990 shows anyone paid $500K.

## 2. What the job listings say (posted base-salary ranges)

Live 2026-09-14, https://jobs.lever.co/metr (8 postings; metr.org/careers mirrors them):

| Posting | Range (verbatim) |
|---|---|
| Member of Technical Staff, Embedded Assessments | $402,048 - $687,759 a year |
| Member of Technical Staff, Evaluation Execution | $328,380 - $578,583 a year (junior/mid $328k-402k; senior $402k-578k) |
| Member of Technical Staff, Security Engineering | $328,380 - $578,583 a year |
| Member of Technical Staff, Cyberforensics | $402,048 - $578,583 a year |
| System Administrator | $260,937 - $471,969 a year |
| General Counsel | $328,380 - $402,048 a year ("Base salary commensurate with experience.") |
| Task Development Engineer (contractor, remote) | $150-300/hour |
| General Expression of Interest | "Compensation is competitive with Bay Area tech roles (excluding equity)." |

Every salaried posting states "The listed range applies to the base salary for this role" (Eval Execution wording) and the Eval Execution posting adds "For very experienced and exceptional candidates, we are open to exploring paying much higher than this stated range." metr.org/careers: "Salaries competitive with top AI labs." No equity.

**Range history (Wayback raw captures, decoded):**
- 2026-06-16 / 07-15: generic "Member of Technical Staff" (posting 1c044574, since removed) **$285,548 - $503,116 a year**; Cloud Evals Infrastructure Engineer $285,548 - $428,581.
- 2026-07-24, 08-09, 08-25: MTS, Evaluation Execution **$285,548 - $503,116** (08-25 adds junior $285k-350k / senior $350k-503k). 2026-08-01, 08-09: "Security Engineer" **$285,548 - $503,116**. 2026-08-08: Platform Engineer, Intern $150/hr.
- 2026-08-27: ranges raised. Security Engineering (same URL, retitled) $328,380 - $578,583; Embedded Assessments **$402,048 - $687,759** (new); System Administrator $260,937 - $471,969. metr.org/careers capture the same day shows $328K-$578K / $402K-$687K etc.
- 2026-09-09: Chief Information Security Officer $402,048 - $578,583 (gone from the board by 09-13); General Counsel $328,380 - $402,048.
- 2026-09-11 (BI publication date): Evaluation Execution $328,380 - $578,583.
- 2026-09-13 (HN comment date): board = the same 8 postings as today.

## 3. What critics and press claimed, and what "$500K" is

- **Business Insider**, Stephen Council, JSON-LD datePublished 2026-09-11 (slug "...-2026-8"): "Barnes left OpenAI to start the nonprofit in 2022 and sees such fierce competition for AI researchers that even METR's lofty salaries, which reach $503,000 on current job postings, don't address the nonprofit's talent shortage." Also, paraphrasing Chris Painter: "more people might leave the AI companies themselves — for similar salaries at METR, though without equity compensation — if a regulatory system gave safety research organizations greater authority."
- **Hacker News**, nullbio, 2026-09-13 (item 49682532): "METR's salaries are listing around 500k/yr. Gee, I wonder where this non-profit with ~35 people is getting all of its money?"
- **X**, Joshua Saxe, 2026-09-13 21:12 UTC: "Without knowing the details, many at METR gave up generational wealth to work there."

**Verdict on "$500K":** it is a **posted ceiling, not a paid figure.** BI's "$503,000" is the $503,116 top of the base-salary band on the generic MTS / Evaluation Execution / Security Engineer postings that were live from at least 2026-06-16 through 2026-08-25. It was already stale on BI's own publication date: by 2026-08-27 those bands had been raised to $578,583, and the Embedded Assessments posting carried a $687,759 ceiling. The HN "around 500k/yr" is consistent with the midpoints of the MTS bands ($453K-$545K) but is phrased as if it were what staff are paid; the 990 shows the top actual 8-month figure was $243,560 (Taran) and the annualized average across 38 W-2s was roughly $161K in wages. Note the two documents describe different periods: the 990 covers May-Dec 2024, the postings are 2026, and METR's bands rose ~15% between June and late August 2026 alone, so the gap between "paid in 2024" and "posted in 2026" is partly time, partly seniority targeting (the Embedded Assessments and Cyberforensics postings start at $402,048), and partly the difference between a band ceiling and a median. The FY2025 990 (calendar 2025) is not yet filed and would be the first full-year test.

**"Gave up generational wealth":** Saxe himself prefixes it "Without knowing the details." The only documentary support in this set is BI's Painter paraphrase ("similar salaries at METR, though without equity compensation") and the levels.fyi self-reported totals below; the 990 records no equity-based compensation (Schedule J Part I line 4b = 0).

## 4. Benchmarks (all fetched 2026-09-14)

- Redwood Research careers: "For the Member of Technical Staff role, compensation ranges from $350,000 to $850,000 per year, depending on experience." (higher ceiling than any METR posting; Redwood's own 990 top is $314,922).
- Epoch AI (Lever, remote): Senior Researcher $168,000-$300,000; Researcher $115,000-$185,000; Software Engineer, Benchmarking $150,000-$325,000; "willing to pay above these ranges for exceptional candidates in key locations."
- Apollo Research: "Competitive salary and equity packages, benchmarked by role and experience" (no numbers; Ashby API 404).
- levels.fyi (self-reported **total** comp incl. stock, "Last updated: September 14, 2026"): Anthropic Software Engineer US median $883K, range $367K-$1.42M (entry median $366,667; senior $591,346); company-wide median $402,350. OpenAI Software Engineer US median $880K, range $250K-$1.89M (L2 median $249,519); company-wide median $633,150. These are not base-salary figures, so they are not directly comparable to METR's base-only bands; they are the closest public proxy for the "equity" a lab researcher forgoes.

## 5. Caveats
- 990 Part VII lists only officers, directors, key employees and the five highest-paid; the other ~26 METR W-2s are known only through the line 7 aggregate.
- BI could not be fetched through r.jina.ai (Cloudflare challenge, 403); the direct fetch succeeded and the syndicated Jingletree copy matches word for word on the salary sentence.
- Wayback returned "connection refused" mid-batch for ~18 captures; all key ones were re-fetched successfully (`docs/wayback/retry-*`). The 2026-08-30 Cyberforensics capture was not retrieved; its live range is recorded instead.
- Employee count 38 is Part V line 2a (W-2s issued), not year-end headcount.
