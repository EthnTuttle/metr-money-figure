# Third source audit D — figure 10a with Anthropic

Audit date: 2026-09-14. Scope: `AUDIT-SEED-3D.md`, figure `metr-01b-money-that-doesnt-show-up-with-anthropic`, its shared-code companion `metr-01-money-that-doesnt-show-up`, figures 10z/10aa, and the corresponding README verdict rows. This is an audit report, not a replacement goal contract.

## Overall verdict

**FIX.** The displayed grant, recommendation, commitment, transfer, filing and investment numbers generally recompute, the `≤ $7.7B` figure is a valid no-floor ceiling, Moskovitz and Tallinn each publicly call themselves Anthropic board observers, and the corrected card accurately says Moskovitz sits on Coefficient's Board of Managers while Cari Tuna chairs it. The figure nevertheless turns several bounded or unidentified relationships into categorical claims:

- Coefficient names SVCF, NPT and Good Ventures Foundation as external funding partners; it does **not** say that the particular SVCF/NPT accounts paying matched awards belong to Good Ventures, Moskovitz or Tuna.
- The title's “the same funders … are Anthropic's Series A investors” is false as a universal statement. Several drawn funders/intermediaries are not named Series A investors.
- Public records do not locate Moskovitz's donated stake. NPT's `$1.18B` closely-held-stock intake is an unattributed signal, not an identification or a demonstrated “leading candidate.”
- Forbes published the `$500M` estimate in November 2025 for a stake it said moved in early 2025. It did not establish a `$500M` value **at the transfer**.
- “Direct: $0” is only a no-named-line result in a 2,911-row index and specified filings, not proof of lifetime zero direct giving.
- Seven node boxes fail the figure's own height formula and seven labels produce eight intersections with unrelated boxes.
- The stated pipe rule is not the implemented rule: code uses `6 px + 1.4 px per $1M`, not `1.4 px per $1M with a 6 px floor`.
- The non-Anthropic companion contains four literal `Anthropic` references, so the requested no-leak check fails.

No reviewed sentence establishes motive, secret coordination or wrongdoing. The structural overstatements above are attribution errors, not evidence of intent.

## Evidence and boundaries

The full HTML citation expansion contains **249 unique scoped rows**: AP 2, G 1, IV 11, J 2, K 1, LD 22, M 150, RW 5, S 1, ST 43, TB 5 and TO 6. [The scope inventory](audit3-evidence/3d/scope-rows.csv) preserves each row and its source fields; [the substantive ledger](audit3-evidence/3d/row-verdicts.csv) assigns exactly one `CONFIRMED`, `DIFFERS` or `UNVERIFIABLE` verdict to every one. The [fresh/local fetch register](audit3-evidence/3d/fetch-register.csv) records source URL, UTC, transport status, SHA-256 and artifact. Targeted primary evidence and deterministic Canary/Tarbell calculations also remain under [audit3-evidence](audit3-evidence/).

The URL collector attempted all 195 distinct HTTP source URLs in scope, with Jina, Bluesky or fxtwitter fallbacks where applicable. HTTP success means only that bytes were retrieved. A substantive verdict also required the source text, filing, retained primary or transparent source-pack record to match. Current 404/401/403 responses were not treated as failures where a retained primary was hashed. No post by `@kevinnbass` was used. Awards, SFF recommendations, Audacious commitments, filed grants, program-asset transfers, free credits and equity are kept as separate measures throughout this audit.

## Sentence-by-sentence framing review

### Kicker, title, subtitle and group header

| Text | Rows | Verdict | Audit result |
|---|---|---|---|
| Kicker: “Funders → intermediaries → the evaluator, and the lab → the funders” | M01–M150; IV01–IV11; ST26, ST41, ST49, ST54, ST89–ST118 | **OVERSTATED** | It is an editorial map, but “the lab → the funders” collapses investments held by particular people/entities into all drawn funders. |
| Title, clause 1: “The same funders that reach METR through ARC, RAND, Longview and pooled funds are Anthropic's Series A investors, two of them its board observers” | IV01–IV02; ST41, ST118; M01–M60, M77–M96 | **OVERSTATED** | Moskovitz and Tallinn are early investors and self-described observers. Coefficient/Good Ventures, Audacious and anonymous DAF accounts are not all named Series A investors; the routes also mix grants, recommendations and commitments. |
| Title, clause 2: “Moskovitz donated a stake now worth up to $7.7B into a giving complex whose accounts sit where no filing names them” | ST32–ST33, ST78–ST79, ST89–ST92, ST104–ST113, ST121, ST133; IV10 | **OVERSTATED** | Donation and the no-floor ceiling are supported. The receiving vehicle/account is not. “Into a giving complex” and “whose accounts sit” convert an unresolved location into fact. Filing negatives must be bounded by filer and period. |
| Title, clause 3: “Good Ventures gave METR nothing directly” | M33, M97–M105, M117; ST78–ST79 | **OVERSTATED** | No named METR line was found in the Coefficient index or checked Good Ventures filings through June 2025. That cannot prove all-time zero or exclude an unlisted grant. |
| Subtitle sentence 1: “Dustin Moskovitz and Cari Tuna's giving complex is the money: Good Ventures Foundation, their $10.1B endowment, and donor-advised accounts at SVCF and NPT pay what Coefficient Giving recommends.” | ST91, ST100, ST105, ST107–ST109, ST114, ST116 | **OVERSTATED** | `$10.1B` is the Good Ventures Foundation FY2025 total-assets figure; exact matches establish that some SVCF/NPT accounts pay Coefficient awards. No source identifies those particular accounts as the couple's or Good Ventures'. |
| Subtitle sentence 2: “It has no grant to METR on its books; it funded METR's parent, joint-project partner, pooled-fund donor, a board member's organization, and the Tarbell Center that places AI reporters at TIME, The Verge and others.” | M01–M34, M59–M63, M120, M126–M128; TB02–TB04; TO01–TO06 | **OVERSTATED** | The no-grant result is bounded. The named organizations received distinct awards for their own programs; that is not proof the money was routed into METR. Tarbell fellows published at those outlets, but the outlet counts mix publisher tags and keyword fallback and do not show editorial control. |
| Subtitle sentence 3: “Moskovitz and Jaan Tallinn, both Anthropic board observers by their own account, bought into the 2021 Series A; Moskovitz donated his stake, under 0.8% of Anthropic, in 2025 to what he calls 'our foundation'.” | IV01; ST41, ST89, ST92, ST110, ST112–ST113, ST118 | **SUPPORTED** | The observer status is explicitly self-reported, not issuer-confirmed. The stake has a ceiling and no published floor, share count or receiving vehicle. |
| Subtitle sentence 4: “Forbes put it at $500M then; at the $965B Series H valuation the same bound is $7.7B, and no filing yet shows where it sits.” | ST32–ST33, ST78–ST79, ST92–ST106, ST121, ST133; IV10 | **OVERSTATED** | `0.8% × $965B = $7.72B`, correctly rounded to `$7.7B`. Forbes's `$500M` was a November 2025 estimate, not a transfer-date mark. “No filing” must name the filings and cutoff. |
| Header: “Dustin Moskovitz and Cari Tuna: the giving complex that funds the field” | ST81, ST91, ST100–ST116; M01–M34 | **OVERSTATED** | “Giving complex” and “the field” are undefined. The records show a foundation, grantmaking entities and external funding partners, not common ownership of every displayed account or funding of an entire field. |

### Node subtitles and Anthropic-panel statements

| Node or statement | Rows | Verdict | Audit result |
|---|---|---|---|
| Coefficient: “Formerly Open Philanthropy. Recommends the grants; Good Ventures or its DAF accounts at SVCF and NPT pay” | ST91, ST105, ST107–ST109, ST114, ST116 | **OVERSTATED** | Recommends/partner approval is supported; “its DAF accounts” is not. ST105 was corrected to remove that ownership inference. |
| Good Ventures: “Moskovitz and Tuna's $10.1B endowment (Jun 2025), Coefficient's principal funder; $10M to Coefficient Giving Advisors, 2024 (990-PF)” | ST100; Good Ventures FY2024 990-PF | **UNSOURCED** | The filing directly confirms `$10M` to then-Open Philanthropy Advisors and the endowment value, but the node supplies no row ID for the `$10M` line or “principal funder.” Create/cite a row rather than rely on an unnumbered local filing. |
| Jaan Tallinn/SFF: “Anthropic Series A lead, board observer” | IV01, ST41 | **SUPPORTED** | Tallinn is named as lead and publicly describes himself as an observer. |
| Audacious: donors pool commitments, select projects and pay grantees directly | M57–M58, M117–M119, M143, M146; AP47, AP49 | **SUPPORTED** | Audacious's FAQ says TED itself does not fund grantees; partners do. Commitment and filed payment measures remain separate. |
| Audacious: 2024 cohort funded Canary, filed Valhalla `$10M` and High Tide `$333K` to RAND; none to METR | M57–M58, M118–M119, M143; AP49 | **OVERSTATED** | The two RAND payments and no TED Foundation line are confirmed. “None to METR” is only the result of checked/readable filings; AP49 records unavailable or unread filings/attachments elsewhere in the partner set. |
| Audacious: Good Ventures joined after announcement; none traced | AP47; M117 | **SUPPORTED** | The 2024-10-09 capture has 46 partners and no Good Ventures; the live 60-name list includes it. “None traced” is correctly a bounded search result. |
| DAFs/regrantors: Founders Pledge grants match Tallinn's ledger exactly, SVCF within `$450`; other named sponsors do not disclose the donor | M77–M96; ST107 | **SUPPORTED** | The matching evidence is strong but remains matching evidence, not a DAF donor disclosure. |
| ARC: parent through Dec 2023; transferred `$4.55M` of evaluation-program assets at spin-out | M61–M63 | **SUPPORTED** | The total is `$4,553,935` (`$4,477,169` cash + `$76,766` noncash), rounded appropriately. It is a program-asset transfer, not a grant attributable to any one ARC funder. |
| RAND: Canary partner; `~$38M` commitment split `~$21M` RAND / `~$17M` METR; later METR figure “a bit under $16m” | M57–M58; G14 | **SUPPORTED** | `$21M` is the arithmetic remainder, not a separately quoted payment. The later `<$16M` is METR's own later account of its three-year commitment and should not be silently equated with the original `~$17M` allocation. |
| Longview: pooled-fund donor, `$220K` grant plus undisclosed pool | M59–M60 | **SUPPORTED** | Do not infer the pool's METR amount. |
| FAR AI: founder Adam Gleave sits on METR's board | B17/M136 contextual rows, not cited in the node | **UNSOURCED** | The public role is corroborated elsewhere in research, but this node gives no applicable row ID. |
| Redwood: METR subcontractor on OpenAI and Anthropic investigations; Greenblatt; “Barnes's partner” | RW31–RW36, RW58 | **OVERSTATED** | RW31–RW34 confirm the OpenAI work; RW36/RW58, not the displayed RW31–RW35 range, support the Anthropic subcontract. RW35 explicitly says the announcement names no Redwood subcontractor. The personal-relationship parenthetical is unnecessary and has no in-node citation. |
| Constellation: Berkeley office METR works from | M126 | **SUPPORTED** | The source calls it the shared research center hosting METR/AI-lab staff. |
| METR: says it takes no money from frontier labs or staff | N57 | **SUPPORTED** | This is METR's stated policy, not an independent all-transaction audit. |
| Tarbell: “Trains and places AI reporters at outlets”; Coefficient-funded; outlet chips | TB02–TB06; TO01–TO06 | **OVERSTATED** | Funding is confirmed. Fellow/outlet membership and the printed counts reproduce. “Places reporters” can imply organizational control, while the evidence establishes fellowship/roster affiliation and captured fellow bylines. “AI-tagged” is wrong for keyword-fallback records. |
| Anthropic: lab METR evaluates and now investigates | evaluation records; RW35/S13 context | **SUPPORTED** | Current engagement is supported; this does not establish the result of the ongoing investigation. |
| Series H `$965B`; WSJ IPO target `~$2T` | IV10–IV11 | **SUPPORTED** | `$965B` is a completed post-money round; `~$2T` is only a reported IPO target, as labeled. |
| Board observers “by their own account”: Moskovitz and Tallinn | ST41, ST118 | **SUPPORTED** | Both are observers, not directors, and neither status is asserted from an Anthropic roster. |
| Moskovitz panel paragraph: Series A; `<0.8%`; 2025 donation; “our foundation”; no FY2025 GV gift; Berger “not to us”; grants through SVCF/NPT accounts | IV01; ST78–ST79, ST89–ST118 | **OVERSTATED** | Every quoted statement is real, but the last clause again implies that the matched SVCF/NPT accounts are his. The records leave the receiving vehicle unidentified. |
| Tallinn: Series A lead/Series B; percentage undisclosed | IV01–IV02, ST98 | **SUPPORTED** | The quoted non-disclosure is source-supported. |
| Schmidt: Series A; Hillspire/D.E. Shaw relation; “Schmidt Sciences funds a METR board member” | IV01, ST26, ST49, J08 | **OVERSTATED** | J08 says Schmidt Sciences supports METR; it does not establish the board-member claim. M136 separately says Schmidt Sciences is among FAR AI's supporters and Gleave is a METR board member, but the panel does not cite it. |
| Jane Street firm: `$100M`, 3,332,833 shares near `$30`; Series E–H; METR names individuals from the firm | IV05–IV10, LD06, M75 | **SUPPORTED** | The firm/individual distinction is correctly explicit. The later-round amounts are undisclosed. |
| McClave: Series A/B; BEMC not a METR donor | IV01–IV02, J02 | **SUPPORTED** | The negative is bounded to the checked public donor records. |
| CERR/Macroscopic: Series A/B; supports Redwood/Longview; investments include Apollo/Halcyon venture arm | ST54, M139–M142 | **SUPPORTED** | Grants/support and investments remain separately described. |
| Good Ventures public book/AI manager/LP/ARC director chain | ST100–ST102, ST125, ST127 | **OVERSTATED** | The holdings and manager launch are source-backed. “AI-infrastructure portfolio” is an editorial classification; the ADV supports at least one charitable client as an LP but does not publicly identify which charity; this chain must be described as inference. |

### Legend, pipe labels, dashed links, equity band and bar chart

| Text | Rows | Verdict | Audit result |
|---|---|---|---|
| Equity legend: solid donated stake at 1/30 scale; dashed undisclosed/unattributed | ST41, ST92, ST104, ST121; IV10 | **SUPPORTED** | The solid band is a ceiling band, not an identified account balance. Dashed links appropriately denote missing percentage/location, subject to the NPT wording below. |
| Blue legend: “Good Ventures money: awards recommended by Coefficient / Open Philanthropy, or SFF recommendations” | M01–M48 | **OVERSTATED** | SFF recommendations are not Good Ventures money. Coefficient awards may be paid by distinct external partners whose principals are not disclosed. Split the legend by recommender/measure. |
| Grey legend: Audacious Project commitment | M57–M58 | **SUPPORTED** | It is correctly a commitment, not filed cash. |
| Yellow legend: filed DAF/regrantor grants; donor only where ledger matches | M77–M96 | **SUPPORTED** | “Donor named” should be “donor inferred by amount/date matching”; the filings themselves do not name DAF donors. |
| Orange legend: relationship to METR, dashed no money | M59–M63, M120, M126; RW31–RW36 | **OVERSTATED** | A dashed relationship means no money amount was established, not that zero money exists. This distinction matters for a subcontractor relationship. |
| `$1.5M` 2022 to ARC | M01–M02 | **SUPPORTED** | Exact sum `$1,515,000`; correctly rounded. |
| `$10.0M` 2025 AI Evaluation and Testing to RAND | M03 | **SUPPORTED** | Coefficient award, not a METR pass-through. |
| `$26.3M` 2022–25 to Longview | M04–M14 | **SUPPORTED** | Exact award sum `$26,251,590`; correctly rounded. |
| `$59.3M` 2021–25 to FAR AI | M15–M32 | **SUPPORTED** | Exact award sum `$59,347,676`; correctly rounded. |
| `$5.6M` 2022–24 to ARC/ARC Evals | M35–M37 | **SUPPORTED** | Exact SFF recommendation sum `$5,623,000`; not a Coefficient/Good Ventures award. |
| `$752K` 2024–25 to METR including match | M38–M39 | **SUPPORTED** | SFF recommendations including conditional match, not demonstrated cash paid. |
| `$38.0M` Audacious commitment to Canary | M57–M58 | **SUPPORTED** | A joint multi-year commitment; not summed with the separate `~$17M` branch. |
| `$70M+` 2026 recommendation to Redwood | M120 | **SUPPORTED** | A Coefficient recommendation over two years, not cash paid. |
| `$2.4M` 2022–23 to Redwood | M47–M48 | **OVERSTATED** | The amount is an SFF recommendation; the pipe omits the measure. |
| `$22.9M` 2023–24 to Constellation | M126–M128 | **SUPPORTED** | Exact Coefficient award sum `$22.95M`; display rounding is acceptable. |
| `$10.0M` SVCF to Constellation | ST107 | **SUPPORTED** | Filed Schedule I grant; donor/account principal not disclosed. |
| “subcontractor on both investigations (no money to METR)” | RW31–RW36, RW58 | **OVERSTATED** | Both relationships are supported only after adding RW36/RW58. Payment terms are undisclosed; “no money” is not established. |
| “office (no money)” | M126 | **OVERSTATED** | The office relationship is supported; a categorical zero is not established by that row. |
| `$10.8M` DAF/regrantor grants to ARC, `$4.2M` Tallinn | M77–M96 | **SUPPORTED** | The total is a sum of like-type filed grants. The Tallinn component is matching evidence, rounded from approximately `$4.222M` to ARC. |
| `$4.2M` DAF/regrantor grants to METR: Vanguard `$4.0M`, Founders Pledge `$184K`, SVCF `$20K` | M79, M83, M87 | **SUPPORTED** | Exact sum `$4,204,000`. M64–M66 were corrected from undisclosed amounts to these filing values. Vanguard's donor is unknown; Tallinn is inferred for the other two from his ledger. |
| `~$17.0M` to METR (grey) | M58; G14 | **SUPPORTED** | RAND/METR originally reported approximately `$17M`; METR later said a bit under `$16M`. Label it original allocation/commitment, not cash received. |
| `$4.6M` spin-out transfer | M63 | **SUPPORTED** | `$4,553,935` rounded; program assets, not traceable donor dollars. |
| `$220K` plus undisclosed Longview pooled fund | M59–M60 | **SUPPORTED** | The undisclosed amount is correctly not added. |
| Gleave board seat, “no money” | board context; M15–M32 | **OVERSTATED** | Relationship is public, but zero direct FAR-to-METR money is a bounded absence and lacks a row on this label. |
| `$5.3M` Coefficient awards to Tarbell plus SFF `$1.3M` | TB02–TB06 | **SUPPORTED** | `$5,291,930` awards and `$1,303,000` recommendations are not arithmetically combined in the pipe width, but the label should identify both measures explicitly. |
| Outlet chips: TIME 45; Verge 37; MIT Tech Review 26; Lawfare 22; Guardian 20; LA Times 14 | TO01–TO06 | **SUPPORTED** | Counts and windows reproduce the retained Tarbell pack. The six rows were corrected to state partial/complete window and publisher-tag/keyword-fallback methods. |
| Band labels `≤ $7.7B`, “stake, donated”, “drawn at 1/30 scale” | ST92; IV10 | **SUPPORTED** | `0.008 × $965B = $7.72B`; the band height is `int((6 + 7,700×1.4)/30) = 359 px`. It is a ceiling with no floor. |
| Tallinn dashed link: Series A lead, percentage undisclosed | IV01, ST98 | **SUPPORTED** | Correctly marks an undisclosed stake. |
| DAF dashed link: “or the same stake in a DAF account at SVCF/NPT: NPT is the leading candidate, unattributed” | ST104, ST121; contextual ST105–ST109 | **OVERSTATED** | “Unattributed” is correct. “The same stake” and “leading candidate” are hypotheses: NPT reports `$1.183B` across 19 closely held-stock gifts but names no donor or issuer. |
| Anthropic to METR: free tokens unbooked/unquantified; Joe Benton joins METR | K01, S13 | **SUPPORTED** | Neither item is cash funding; the figure keeps them separate. |
| Bar title: “What the donated stake was worth, and what it may be worth now” | ST32–ST33, ST92; IV10 | **OVERSTATED** | `$500M` is not established as the early-2025 transfer-date value, so the first half of the title is not demonstrated. |
| Bar subtitle: “Forbes' estimate at the transfer vs the ceiling … No filing states the number of shares.” | ST32–ST33, ST92; IV10 | **OVERSTATED** | Forbes published the estimate in November 2025 and said transfer occurred earlier. The no-share-count result is bounded to checked public records. |
| `$500M`, “early 2025”, “Forbes estimate at the transfer” | ST32–ST33 | **OVERSTATED** | Correct wording: “Forbes estimate published Nov. 2025; stake reported transferred in early 2025.” |
| `≤ $7.7B`, Sep 2026 ceiling, `0.8% × $965B`; “already skyrocketed” | ST92; IV10 | **SUPPORTED** | A mark derived from a percentage ceiling, not a sale price or current holding confirmation. |
| `×15 at the ceiling` | ST32, ST92; IV10 | **SUPPORTED** | `$7.7B / $0.5B = 15.4`; `×15` is acceptable rounding, subject to the incompatible-date/estimate caveat. |

### Quote cards

| Card sentence | Rows | Verdict | Audit result |
|---|---|---|---|
| Forbes quote: donated early Anthropic investment, `<0.8%`, already risen | ST92 | **SUPPORTED** | Quote matches the retained Forbes/Wayback text. |
| “The only named-outlet percentage bound” | ST92 and search record | **OVERSTATED** | It is the only such bound located in this research, not proof no other public report exists. |
| Three Moskovitz foundation statements on Bluesky | ST110, ST112, ST113 | **SUPPORTED** | All three API payloads match. “Foundation” is his word and does not resolve the legal entity/account. |
| “Good Ventures Foundation's return to June 2025 lists every gift and none is Anthropic stock; Berger: not to us” | ST78–ST79, ST89 | **OVERSTATED** | The return's contributor/asset schedules show no private-stock gift or named Anthropic holding, and Berger's quote matches. “Every gift” should say “the public Schedule B contributors and investment schedules.” |
| “Which account holds them is unattributed” | ST78–ST113 | **SUPPORTED** | This is the correct conclusion and should govern the title, node and DAF caption too. |
| Stratechery observer/boardroom quotes | ST118 | **SUPPORTED** | The retained transcript matches, including the awkward “I'm a chair of at Open Philanthropy” wording. |
| “Board observer, not a director … Tallinn says the same” | ST41, ST118 | **SUPPORTED** | Correctly qualified as self-account. |
| “Coefficient, on whose Board of Managers he sits (Tuna chairs it, ST124)” | ST124 | **SUPPORTED** | This is the corrected and accurate governance line. Moskovitz is a manager; Cari Tuna is Chair of the Board. |
| “[Coefficient] funds METR's parent, partner, pooled donor and subcontractor” | M01–M34, M120 | **OVERSTATED** | It funds those organizations for stated programs; the sentence should not imply those grants funded their METR relationships or flowed to METR. |
| “No motive is asserted” | all scoped evidence | **SUPPORTED** | The figure states relationships and explicitly disclaims motive. Several attribution errors still need correction. |
| “Direct: $0. No METR grant in Coefficient's 2,911-row index or in Good Ventures' 990-PF” | M33, M97–M105; ST78–ST79 | **OVERSTATED** | The second sentence is a valid bounded negative with cutoff; the `$0` headline is categorical and lacks the same boundary. |

## Footnote, sentence by sentence

| # | Footnote sentence, abbreviated | Rows | Verdict | Audit result |
|---:|---|---|---|---|
| 1 | Anthropic facts are from own round announcements and court-supervised FTX sales, IV01–IV11 | IV01–IV11 | **OVERSTATED** | Most round facts match; IV04's cited page is unavailable, IV06 is a press account, and IV11 is reported IPO ambition, not issuer/court evidence. |
| 2 | Moskovitz, Tallinn, Schmidt named Series A; amounts undisclosed | IV01 | **SUPPORTED** | Matches Anthropic's announcement. |
| 3 | Jane Street firm `$100M` and four later rounds; METR names individuals, no firm | IV05–IV10, LD06, M75 | **SUPPORTED** | Firm/individual distinction is correct. |
| 4 | No individual's current stake is public | IV/LD/ST search set | **OVERSTATED** | No current amount was found for the people at issue; the absolute public-record negative should be bounded. |
| 5 | Moskovitz stake bounded only by Forbes `<0.8%` | ST92 | **SUPPORTED** | A no-floor percentage ceiling. |
| 6 | `0.8%` of `$965B` = `$7.7B`; band ceiling; 1/30 because about 10,800 px | ST92, IV10 | **SUPPORTED** | Raw grant-scale width is `10,786 px`; description is acceptable rounding. |
| 7 | Forbes `$500M` is estimate “at the early-2025 transfer” | ST32–ST33 | **OVERSTATED** | Publication/estimate is November 2025; only the transfer is early 2025. |
| 8 | Bar chart uses same two rows | ST32–ST33, ST92 | **OVERSTATED** | The row mapping is correct but the bar inherits the timing error. |
| 9 | Coefficient holds no Anthropic stake on any filing; Moskovitz personally until 2025 | ST78–ST90 | **OVERSTATED** | Berger says Open Phil never invested and Moskovitz did. “Any filing” and the precise custody history exceed the inspected records. |
| 10 | Donated/“our foundation” while GV FY2025 has no gift | ST78–ST79, ST89, ST110, ST112–ST113 | **SUPPORTED** | The unresolved timing/entity tension is correctly shown, provided no location is inferred. |
| 11 | Coefficient page names SVCF/NPT DAF accounts as funders approving its grants | ST105 | **OVERSTATED** | It names external funding partners, not account ownership or principals. |
| 12 | Exact sponsor/award matches; SVCF→NPT `$1.59B`; NPT `$1.18B`/`+$1B`, unattributed | ST104, ST106–ST109 | **SUPPORTED** | Raw figures reproduce; `unattributed` is essential. |
| 13 | Vanguard Schedule B excludes it for transfer window | ST133 | **SUPPORTED** | Excludes Vanguard for that fiscal window and approximate block size, not later FY2026. |
| 14 | Moskovitz/Tallinn each self-describe as observer | ST41, ST118 | **SUPPORTED** | Correct. |
| 15 | CERR/Macroscopic supports Redwood/Longview and holds Apollo/Halcyon investments | ST54, M139–M142 | **SUPPORTED** | Correct, with grant/investment measures separate. |
| 16 | Good Ventures public book is an AI-infrastructure portfolio; VARA AI fund | ST100–ST102 | **OVERSTATED** | Holdings and fund are factual; portfolio classification is editorial. |
| 17 | Hillspire 10–25% of D.E. Shaw, whose venture arm joined H | ST49, ST26 | **SUPPORTED** | Two linked but distinct records; no claim that Schmidt owns the venture-arm investment directly. |
| 18 | Tarbell Coefficient awards: `$816K`, `$2.888M`, `$1.58793M` | TB02–TB04 | **SUPPORTED** | Sum `$5,291,930`; index records match. |
| 19 | SFF Tarbell recommendations `$520K`, `$783K` incl. match | TB05–TB06 | **SUPPORTED** | Sum `$1,303,000`; recommendation measure retained. |
| 20 | Chips count “AI-tagged” fellow articles; windows differ | TO01–TO06 | **OVERSTATED** | Counts/windows reproduce, but many rows use keyword fallback rather than an outlet AI tag; TO rows were corrected accordingly. |
| 21 | Per-share strip now only in LD01–LD22 | LD01–LD22 | **SUPPORTED** | True of the current figure. Eight Forge-dependent rows and the historic NPM observation remain unverifiable in the row ledger. |
| 22 | Money types kept apart; listed measure definitions | M01–M60 | **SUPPORTED** | Arithmetic does not sum awards, recommendations and commitments into one total. Some legend/labels still visually group them. |
| 23 | Pipe widths: 1.4 px per `$1M`, 6 px floor, no cap | generator implementation | **OVERSTATED** | Actual `pw(amt)` is `max(6, 6 + 1.4×amt_in_millions)`, hence always `6 + 1.4×amount` for nonnegative values. `$38M` draws at `59.2 px`, not `53.2 px`. |
| 24 | Direct `$0` defined as no index row; unlisted gifts not excluded | M33 | **SUPPORTED** | This bounded definition is sound and should replace categorical headlines. |
| 25 | Index backend; per-grant URLs withdrawn/404; later descriptions unpublished | coefficient index/pages | **SUPPORTED** | Current 404s and retained 2,911-row backend confirm the stated limitation. |
| 26 | ARC transfer and inability to attribute it to one donor | M01–M02, M35–M37, M63, M88–M92 | **SUPPORTED** | Correct separation of source grants from transferred program assets. |
| 27 | Tallinn ledger payments below recommendations and not summed | M35–M48 | **SUPPORTED** | Correct measure discipline. |
| 28 | Longview beyond `$220K` undisclosed | M59–M60 | **SUPPORTED** | Correct. |
| 29 | Redwood Coefficient `$70M+`, SFF `$2.4M`; both investigation roles cited RW31–RW35 | M47–M48, M120; RW31–RW35 | **OVERSTATED** | Funding measures are correct. Anthropic subcontract needs RW36/RW58; RW35 says Anthropic/METR announcements name neither Redwood nor subcontractors. |
| 30 | Constellation `$22.95M` + SVCF `$10M`; METR office | M126–M128, ST107 | **SUPPORTED** | Separate grant streams; no routing claim needed. |
| 31 | Canary joint project drawn through RAND | M57–M58 | **SUPPORTED** | Correct diagram convention. |
| 32 | Yellow flows are filed Schedule I/Part XV grants | M77–M96 | **SUPPORTED** | Correct measure. |
| 33 | Founders Pledge exact matches, SVCF within `$450`; `$4.4M` Tallinn money | M77–M83 | **OVERSTATED** | Amount/date matching strongly supports Tallinn attribution, but filings do not identify the DAF donor. Say “matches Tallinn's ledger” rather than “is his money.” |
| 34 | Vanguard `$4M` one/more anonymous DAF accounts | M87, ST133 | **SUPPORTED** | Correctly unattributed. |
| 35 | EV/Every.org/AEF/Fidelity donors unnamed | M88–M96 | **SUPPORTED** | Correct for the cited filing lines. |
| 36 | Audacious partners pay directly; TED filings no Canary line | M118 | **SUPPORTED** | Four TED Foundation 990-PF XMLs have 3/6/1/2 paid-grant groups, no Canary/METR/RAND grant, and `binaryAttachmentCnt=0`. M118/AP49 were corrected. |
| 37 | Two filed Canary payments to RAND | M119, M143, AP49 | **SUPPORTED** | Valhalla `$10M`; High Tide `$333,334`. It remains “two found,” not a complete partner-payment census. |
| 38 | RAND directed-funder list | M146 | **SUPPORTED** | Names match the fresh page after M146's category-text correction. |
| 39 | Good Ventures absent on announcement date, later added | AP47 | **SUPPORTED** | Captures show 46 then 60 names, no normalized drops. |
| 40 | METR later `<$16M`; no filing shows METR payment; `~$17M` rests on RAND release | G14, M58, AP49 | **OVERSTATED** | The two commitment statements are supported. The partner-filing search has unavailable/unread records, so “no filing” is too broad. |
| 41 | Good Ventures listed partner, no traced payment through Jun 2025 | M117, AP47 | **SUPPORTED** | Properly bounded to traced records/cutoff. |
| 42 | Good Ventures 990-PF through Jun 2025 has no METR line | Good Ventures filings | **SUPPORTED** | Valid filing-specific negative. |
| 43 | FAR/Longview/RAND totals are own-program grants, not METR routing | M03–M32 | **SUPPORTED** | This limitation is correct and conflicts with some stronger title/node language. |
| 44 | METR's no-lab-funding statement consistent with everything found | N57; scoped flows | **SUPPORTED** | An absence of located contradiction, not proof of completeness. |
| 45 | Blanket rows M01–M150 plus subset descriptions | M01–M150 | **OVERSTATED** | This imports 150 rows, many unused, while omitting necessary semantic support such as RW36/RW58 and N57 from the visible citation. Use claim-level citations. |
| 46 | Source/build/audit note | local files | **SUPPORTED** | Provenance statement, not a substantive claim. |

## Motive and attribution

The scoped 10a-Anthropic text does not directly assert that any named person intended to influence METR, coordinated a finding, or committed wrongdoing. Its final card expressly says no motive is asserted. That disclaimer should remain.

The issue is narrower and still material: phrases such as “the same funders,” “its DAF accounts,” “into a giving complex,” “NPT is the leading candidate,” “Good Ventures money” and “no money” turn unresolved ownership, routing or absence questions into facts. Those should be corrected without adding an intent narrative.

Every occurrence of `unattributed` is directionally correct:

1. The equity legend's dashed `unattributed` category is appropriate.
2. The NPT caption correctly ends `unattributed`, but the preceding “leading candidate” still overclaims.
3. The Bluesky card's “Which account holds them is unattributed” is correct.
4. The footnote's NPT `$1.18B`/`+$1B` statement is correctly marked unattributed.

## Named-person review

All named people are identified through public professional, governance, philanthropic, investor, author or employee roles. No nonpublic individual was added by this figure.

| Person | Public role used here | Supporting record | Result |
|---|---|---|---|
| Dustin Moskovitz | Public founder/philanthropist; Coefficient manager; self-described Anthropic observer/investor | IV01; ST89–ST118, ST124 | Public-role use confirmed. |
| Cari Tuna | Good Ventures president/board chair; Coefficient board chair; Forbes interviewee | ST33, ST91, ST124 | Public-role use confirmed. |
| Jaan Tallinn | Public founder/philanthropist, SFF recommender, named Anthropic investor/observer | IV01–IV02; ST41, ST98 | Public-role use confirmed. |
| Eric Schmidt | Named Anthropic investor; Hillspire/Schmidt Sciences public roles | IV01; ST26, ST49; J08 | Public-role use confirmed; board-member funding wording is miscited. |
| James McClave | Publicly named Anthropic investor; BEMC Foundation context | IV01–IV02; J02 | Use is limited to a public issuer/investor role. |
| Beth Barnes | METR founder/CEO and public report author | METR/RW records | Public-role use confirmed; omit the partner parenthetical because the relationship is unnecessary. |
| Ryan Greenblatt | Redwood chief scientist and named investigation contractor | RW31–RW34, RW58 | Public-role use confirmed. |
| Adam Gleave | FAR AI founder/CEO and METR board member | M136/B17 context | Public-role use confirmed; add a row citation on the node. |
| Paul Christiano | ARC founder and public AI-safety researcher | M61–M63 context | Public-role use confirmed. |
| Chris Anderson | Audacious/TED founder named by RAND as a directed funder | M146 | Public-role use confirmed. |
| Jacqueline Novogratz | Audacious partner/funder named by RAND | M146 | Public-role use confirmed. |
| Benjamin Hoskin | SEC-disclosed VARA owner/officer and ARC director link | ST101, ST125, ST127 | Public-role use confirmed. |
| Joe Benton | Public Anthropic alignment employee and publicly announced METR move | S13 | Public-role use confirmed. |
| Alexander Berger | Coefficient CEO speaking publicly | ST89, ST124 | Public-role use confirmed. |
| Matt Durot; Chase Peterson-Withorn | Forbes article bylines | ST92 | Public author roles confirmed. |

## Layout audit

The current HTML was re-rendered at device scale factor 2 and compared pixel-for-pixel with the committed PNG. Both are `4400×5200`, both hash to `9d3b0ae3a6637d6345e7ae08246307a25c47397b350dc880f255fad07cc60801`, and changed pixels = 0. The geometry results therefore describe the shipped PNG, not an approximate reconstruction. See [layout summary](audit3-evidence/3d/layout-summary.txt), [node heights](audit3-evidence/3d/node-heights.csv), [collisions](audit3-evidence/3d/label-collisions.csv), and [replay PNG](audit3-evidence/3d/rendered-check.png).

The required formula is `subtitle lines × 21 px + 62 ≤ box height`. Seven nodes fail:

| Node | Box `(x,y,w,h)` | Subtitle lines | Required | Margin |
|---|---:|---:|---:|---:|
| Jaan Tallinn / SFF | `(400,560,300,100)` | 2 | 104 | `-4 px` |
| DAFs and regrantors | `(400,1020,300,195)` | 7 | 209 | `-14 px` |
| Alignment Research Center | `(1130,60,340,110)` | 3 | 125 | `-15 px` |
| Longview Philanthropy | `(1130,460,340,100)` | 2 | 104 | `-4 px` |
| FAR AI | `(1130,660,340,100)` | 2 | 104 | `-4 px` |
| Constellation | `(1130,1060,340,100)` | 2 | 104 | `-4 px` |
| Tarbell Center for AI Journalism | `(1430,1190,300,140)` | 4 | 146 | `-6 px` |

Seven distinct labels produce eight unrelated-box intersections:

| Label | Text bounding box | Box intersected | Overlap rectangle |
|---|---|---|---|
| `$10.0M 2025 "AI Evaluation and Testing" → RAND` | `[753.51,228.85]–[1155.29,247.75]` | RAND | `[1130.00,240.00]–[1155.29,247.75]` |
| `$38.0M Audacious commitment …` | `[747.70,757.25]–[1355.27,776.15]` | FAR AI | `[1130.00,757.25]–[1355.27,760.00]` |
| `$70M+ 2026 recommendation → Redwood` | `[663.31,805.75]–[1061.10,824.65]` | Audacious | `[663.31,805.75]–[700.00,824.65]` |
| `$4.2M 2024–25 → METR …` | `[636.07,612.85]–[1615.80,631.75]` | Tallinn/SFF | `[636.07,612.85]–[700.00,631.75]` |
| `~$17.0M to METR (grey)` | `[1581.40,370.05]–[1773.46,388.95]` | METR | `[1760.00,380.00]–[1773.46,388.95]` |
| `$220K 2023 + undisclosed pooled fund` | `[1458.57,492.95]–[1771.43,511.85]` | Longview | `[1458.57,492.95]–[1470.00,511.85]` |
| Same `$220K` label | same | METR | `[1760.00,492.95]–[1771.43,511.85]` |
| `board seat (Gleave), no money` | `[1517.96,546.85]–[1765.24,565.75]` | METR | `[1760.00,546.85]–[1765.24,560.00]` |

The Tallinn → METR pipe **does not** cross the Longview box. Its closest center point is `(1480.74,587.70)`, centerline distance to the box is `29.71 px`, stroke width is `7.10 px`, and painted clearance is `26.16 px`.

## Cross-figure consistency

| Fact | 10a-Anthropic | 10z | 10aa | README | Result |
|---|---|---|---|---|---|
| `<0.8%` | Present, no floor | Present, no floor | Present | Present in 10aa verdict context | **AGREES** where present. |
| `≤ $7.7B` | Present as Series H ceiling | Present as Series H ceiling | Absent | Absent | **AGREES**, but 10a must not call it a current identified holding. |
| `$500M` | Mislabelled as transfer-date estimate | Correctly called a Nov. 2025 estimate | Absent | README's 10z row uses Nov. 2025 framing | **DIFFERS** in 10a wording. |
| “board observer” | Both, by own account | Tallinn and Moskovitz, self/public account | Both self-described | README reflects observer status | **AGREES**; observer is not director. |
| NPT `$1.18B` | Present, unattributed but called leading candidate | Absent | Present, unattributed | Present in 10aa verdict context | Raw figure **AGREES**; “leading candidate” appears only in 10a and is too strong. |
| `unattributed` | Four uses | Not applicable | Present | Present | **AGREES** on non-attribution. |

## Non-Anthropic companion (`metr-01`)

The current shared grant amounts, recipients and most common labels match because both variants are emitted from the same code path. No historical baseline was supplied, so this audit can confirm current equality but cannot prove that no earlier shared label changed.

The no-leak requirement fails. `metr-01` contains four literal `Anthropic` references:

1. Tallinn node: “Anthropic Series A lead, board observer.”
2. Redwood node: “OpenAI and Anthropic investigations.”
3. Footnote Redwood sentence: “subcontracted on the Anthropic one.”
4. Footnote DAF sentence: `$4.4M` is called “an Anthropic Series B investor's money.”

Its title/subtitle also overstate routing: “Its money reached METR's parent, which handed METR `$4.6M`” implies the ARC transfer contained Good Ventures dollars. M63 is a transfer of ARC evaluation-program assets; ARC had several funders, and the footnote correctly says the transfer cannot be attributed to one. Thus the title does not match the figure's own limitation.

## Scoped-row verdicts

The machine-readable ledger has one and only one verdict for all 249 rows: **224 CONFIRMED, 14 DIFFERS, 11 UNVERIFIABLE**. `CONFIRMED` means the primary/retained source matches the row at the row's stated scope and measure; a bounded negative is not upgraded to a universal absence.

**CONFIRMED:** AP47; G14; IV01, IV02, IV03, IV05, IV06, IV07, IV08, IV09, IV10, IV11; J02, J08; K01; LD02, LD05, LD06, LD07, LD09, LD10, LD13, LD15, LD16, LD17, LD18, LD19, LD20, LD22; M01–M63 except none; M67–M104; M106–M117; M119–M145; M147–M150; RW31–RW35; S13; ST26, ST32, ST33, ST41, ST49, ST54, ST78, ST79, ST89–ST104, ST106–ST114, ST116, ST117, ST121, ST124, ST125, ST127, ST133; TB02–TB06.

The M ranges above exclude every row separately listed below as `DIFFERS` or `UNVERIFIABLE`; the CSV ledger is authoritative for expansion. In particular M64–M66, M105, M118 and M146 are not in the confirmed set.

### DIFFERS — corrected in place

| Row | Exact difference and correct result |
|---|---|
| AP49 | Removed false “TED TY2024 grants are in an attachment” statement. Four 990-PF XMLs have 3/6/1/2 readable paid-grant groups; TY2024 totals `$100,253`; no METR/RAND/Canary grant. |
| M64 | Was amount undisclosed; correct Founders Pledge → METR amount is `$184,000` (M79 filing). |
| M65 | Was amount undisclosed; correct SVCF → METR amount is `$20,000` (M83 filing). |
| M66 | Was date 2025 and amount undisclosed; correct Vanguard → METR amount is `$4,000,000`, FY2025 (`2024-07-01`–`2025-06-30`; M87 filing). |
| M118 | Was labelled Schedule I and falsely said TY2024 was an unread attachment. Correct measure is 990-PF Part XV; all four grant lists are readable in XML and `binaryAttachmentCnt=0`. |
| M146 | RAND's first two funding-category descriptions were paraphrased incorrectly. The final row preserves the three current headings/lists and names. |
| ST105 | Removed the inference that the named SVCF/NPT accounts are the couple's. Source quote: recommendations go to Coefficient Giving Advisors or “one of our external funding partners” such as SVCF, NPT or GVF. |
| ST118 | Replaced “while he chairs Coefficient” with “while he sits on Coefficient's Board of Managers; Cari Tuna chairs it.” ST124 is explicit. |
| TO01 | Corrected method: 45 = 42 keyword fallback + 3 tag page; partial window. |
| TO02 | Corrected method: 37 unique fellow-byline URLs in partial publisher-tag window. |
| TO03 | Corrected method: 26 = 22 tag page + 4 keyword fallback; complete trailing-year article window. |
| TO04 | Corrected method: 22 keyword-fallback fellow-byline rows in a partial Common Crawl/Wayback sample. |
| TO05 | Corrected method: 20 unique fellow-byline URLs in partial publisher-tag window. |
| TO06 | Corrected method: 14 unique fellow-byline URLs in partial publisher-tag window. |

Every corrected CSV cell retains `audit-3 2026-09-14: was <old>` in its notes. No row was deleted.

### UNVERIFIABLE

| Row | Attempt and manual route |
|---|---|
| IV04 | CNBC cited page returned 404 and no dated copy was retained. Obtain a licensed/archive copy or replace with issuer/filing evidence for the closed Series D. |
| LD01 | Forge returned 403; exact `$2.57/$623.11M` vendor row lacks a retained capture. Obtain historical Forge/Delaware certificate. |
| LD03 | Forge returned 403; exact Series C `$11.23/$4.55B` vendor split lacks a retained capture. Obtain Forge/certificate. |
| LD04 | Forge returned 403; exact Series D-1 `$30/$14.55B` lacks a retained capture. Obtain Forge/certificate. |
| LD08 | Forge returned 403; Amazon corroborates conversion but not every tranche price/share count. Obtain Forge/certificate/conversion schedule. |
| LD11 | Forge returned 403; Anthropic confirms `$13B/$183B`, not exact per-share/tranche data. Obtain Forge/Series F certificate. |
| LD12 | Forge returned 403; Anthropic confirms `$30B/$380B`, not exact per-share/tranche data. Obtain Forge/Series G certificate. |
| LD14 | Forge returned 403; Anthropic confirms `$65B/$965B`, not every exact per-share/tranche value. Obtain Forge/Series H certificate; retain `$965B` separately. |
| LD21 | Live NPM says `$777.40` at Aug. 31, not the historical `$773.98` at Aug. 28 preserved from search results. Obtain an archived Aug. 28 page or omit. |
| M105 | One cited XML and five retained entity returns do not reproduce the claimed seven-return TY2022–TY2024 search. Retrieve/hash all seven and repeat the recipient search. |
| ST115 | IRS landing page fetched, but the 98,802-row SOI split-interest-trust dataset/search receipt was not retained. Download/hash the dated file and rerun the four-term search. |

## Numbered findings ranked by consequence

1. **The central ownership/routing thesis is stronger than the evidence.** Coefficient's source says external funding partners, not “Good Ventures or its DAF accounts.” Exact award matches identify sponsor accounts, not their donors. This affects the title, subtitle, header, Coefficient node, legend and footnote.

2. **The title falsely universalizes Anthropic Series A status.** Moskovitz/Tallinn/Schmidt/McClave/CERR are named early investors, but the diagram's other funders and anonymous DAF/regrantor accounts are not. Narrow the subject.

3. **The donated stake remains unlocated.** `<0.8%` and donation are supported, and `$7.7B` is valid only as a no-floor ceiling. NPT's `$1.18B`/19-gift anomaly is unattributed and cannot identify the stake, the issuer or donor.

4. **The `$500M` bar has the wrong time semantics.** Forbes published the estimate in November 2025 while reporting an early-2025 transfer. 10z and README preserve the correct distinction; 10a does not.

5. **Categorical zeros exceed bounded searches.** “Good Ventures gave METR nothing directly,” `Direct: $0`, and orange-link “no money” claims should be no-named-line/payment-terms-undisclosed statements. A subcontract is especially incompatible with an unsupported zero-money caption.

6. **The shared companion fails its content boundary.** The non-Anthropic figure contains four Anthropic references and its title attributes ARC's spin-out transfer to Good Ventures despite the footnote's explicit non-attribution.

7. **The shipped layout has material collisions.** Seven boxes fail the prescribed height formula, and seven labels intersect eight unrelated boxes. Coordinates are above. The Tallinn → METR pipe itself clears Longview.

8. **The pipe-scale disclosure is mathematically false.** The implementation adds a 6 px baseline to every pipe. Either describe `6 + 1.4 px/$1M` or later revise the generator to an actual `max(6, 1.4×amount)` rule; this audit does not edit the generator.

9. **Redwood's Anthropic subcontract is semantically miscited.** RW31–RW34 support OpenAI, RW35 names only the Anthropic/METR agreement and says it does not name Redwood, and RW36/RW58 provide the subcontract evidence.

10. **Tarbell counts reproduce, but the classification wording does not.** Some counts rely partly or entirely on keyword fallback and most source windows are partial. “AI-tagged” and “places reporters” overstate what the byline pack establishes.

11. **Audacious money needs consistent measure/coverage labels.** `$38M`/`~$17M` are commitments; `<$16M` is METR's later account. The two located partner payments went to RAND. TED's own four Part XV lists have no Canary line, but an incomplete wider partner-filing search cannot support “no filing shows a payment to METR.”

12. **One Anthropic-panel relationship has the wrong citation.** J08 supports Schmidt Sciences → METR, not “Schmidt Sciences funds a METR board member.” Use M136 for Schmidt Sciences → FAR AI/Gleave, or state the J08 fact.

13. **The corrected governance card is sound.** Moskovitz is a Coefficient Board of Managers member; Cari Tuna is Chair. The card does not claim he chairs it and does not assert motive.

14. **The arithmetic and money-type separation mostly hold.** All displayed grant/recommendation/commitment sums recompute, and the equity ceiling is not added to funding flows. Remaining problems are labels and attribution, not addition errors.

## Figure text recommendations

1. Replace the title with: **“Some funders connected to METR through ARC, RAND, Longview and pooled funds are also Anthropic investors; Moskovitz and Tallinn say they are board observers. Moskovitz says he donated his under-0.8% stake to a foundation, but the public records checked do not identify the recipient account. No METR grant appears in Coefficient's 2,911-row index or Good Ventures filings through June 2025.”**

2. Replace “the giving complex that funds the field” with **“Moskovitz/Tuna philanthropy and Coefficient funding partners.”**

3. Replace the Coefficient node with: **“Recommends grants; recommendations may go to Coefficient Giving Advisors or external funding partners including Good Ventures Foundation, SVCF and NPT. Public sources do not identify the principals of the matched SVCF/NPT accounts.”**

4. Replace the blue legend with separate measure labels: **“Coefficient/Open Philanthropy awards”** and **“SFF recommendations, including conditional matches.”** Do not label both “Good Ventures money.”

5. Replace every categorical direct-zero label with: **“No METR-named grant found in Coefficient's 2,911-row index or Good Ventures filings through June 2025; unlisted/later gifts are not excluded.”** Replace orange “no money” with **“payment amount/terms not established”** where appropriate.

6. Replace the NPT dashed caption with: **“Possible DAF custody route; no source attributes the stake to SVCF or NPT. NPT FY2025 received `$1.18B` of closely held stock across 19 gifts, donor and issuer unattributed.”**

7. Replace the `$500M` bar label with: **“Forbes estimate published Nov. 2025; stake reported transferred in early 2025.”** Rename the chart **“Two published bounds at different dates”** and retain the `$7.7B` label as **“no-floor ceiling at Series H.”**

8. Change the Redwood footnote citation to **RW31–RW36, RW58** and the relationship caption to **“OpenAI joint work; Anthropic subcontract reported by Redwood; terms undisclosed.”** Remove “Barnes's partner.”

9. Change the Schmidt line to either **“Schmidt Sciences is a named METR supporter (J08)”** or **“Schmidt Sciences supports FAR AI, whose CEO Adam Gleave is a METR board member (M136/B17).”**

10. Change Tarbell wording to: **“Tarbell fellows published the counted AI-classified articles at these outlets during outlet-specific captured windows; classifications combine publisher tags and keyword fallback, and most windows are partial (TO01–TO06).”**

11. Correct the pipe disclosure to **“width = 6 px + 1.4 px per `$1M`, no cap”** if the code is retained. Continue to state awards, recommendations and commitments separately.

12. Increase or shorten the seven undersized nodes to meet the formula, then reposition the seven listed labels outside unrelated boxes. Preserve at least the measured `26.16 px` painted clearance between the Tallinn → METR pipe and Longview.

13. In `metr-01`, remove all four Anthropic references. Replace its title's routing sentence with: **“Coefficient awarded ARC `$1.515M`; ARC later transferred `$4.554M` of evaluation-program assets to METR, but the transfer cannot be attributed to any one ARC funder.”**

14. Keep the corrected governance sentence and the explicit **“No motive is asserted”** disclaimer.

## Completion check

`python3 scripts/audit.py` exited 0. Last line:

`figures=29 pngs=29 row_ids_in_research=2213 cited=1111 missing=0`
