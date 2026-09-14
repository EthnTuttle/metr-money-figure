# GROKREVIEW-B — review of Grok lanes G15, G20, G21, G23, G25 (fetched 2026-09-14 ~11:50–11:57 UTC)

Reviewer: Claude (fork), 2026-09-14. Read in full: research/grok-out/G15-openai-equity.csv (58 lines), G20-schmidt.csv (43), G21-jane-street.csv (89), G23-tallinn.csv (59), G25-donors.csv (73), and the five briefs in research/grok-briefs/. Compared against research/stakes.csv (ST01–ST85), money_flows.csv (M01–M138), shared_donors.csv (J01–J17), finances.csv (N01–N58), plus board.csv, evaluators.csv, investments.csv, independence_fight.csv, audacious-partners.csv, the G3/G5 grok-out files and the 10z/10aa figure code in scripts/generate.py. No files other than this one were written. Nothing was fetched.

Row citation convention: the Grok CSVs have no row-id column, so rows are cited as `<lane> L<line>` (1-based line in the file, header comments included) plus task letter and entity. Quotes are verbatim from the lane row's quote_300 field.

Bottom line for the two figures:
- Figure 10aa's OpenAI-equity claim ("none on any record") survives all five lanes and is now checked against three more rounds and two tenders (G15). Two scoping changes are needed: (i) the OpenAI Foundation's >$130M "AI Resilience" grant list — the one program that says it supports "independent testing and evaluations" — is unpublished, so "that foundation funds none of METR's network" is verifiable only against published lists; (ii) the only indirect OpenAI path found for any METR funder is Hillspire's 20% of D.E. Shaw & Co. while D.E. Shaw Ventures co-led OpenAI's Mar 2026 round (and is in Anthropic's Series H).
- Figure 10aa's "what rises" Anthropic cell is incomplete: G20 shows CERR/Macroscopic Ventures (Anthropic Series A and B investor) makes grants to Redwood Research and Longview and impact investments in Apollo Research and Halcyon Venture Partners. That is a third Anthropic investor funding METR's subcontractor, pooled funder, an evaluator, and the incubator's VC arm; the cell currently names only Good Ventures/Coefficient and SFF.
- Figure 10z: no lane produced a stake size or value for Schmidt, Jane Street (beyond ST20–ST30), McClave or Tallinn. The Tallinn line gains a second 2026 "declined to say" instance (Manifold #112, with a $10B figure that is the interviewer's, not his). One unrecorded fact bears on the funders-and-labs framing: Metaplanet's own portfolio lists xAI (2024) alongside Anthropic.

---

## 1. NEW FACTS

Each item: lane+row, date, who, URL, verbatim quote (≤300 chars), and the figure/row it changes. "Not in CSVs" means grep of stakes/money_flows/shared_donors/finances (and the other research CSVs named above) found no row.

### (a) Any METR funder holding OpenAI equity

**NF-1. OpenAI's Mar 2026 $122B round: investor list checked, none of the six present.**
- G15 L23 (Task A), 2026-03-31, OpenAI (issuer), https://openai.com/index/accelerating-the-next-phase-ai/
- Quote: "The round was anchored by our strategic partners Amazon, NVIDIA, and SoftBank, with continued participation from our long-term partner, Microsoft. SoftBank co-led the round alongside a16z, D. E. Shaw Ventures, MGX, TPG, and accounts advised by T. Rowe Price Associates, Inc."
- Not in CSVs: ST73–ST74 cover only Oct 2024 and Mar 2025. Also newly checked and negative: Oct 2025 ~$6B employee secondary (G15 L24, Fortune 2025-08-16; buyers Thrive, SoftBank, Dragoneer, MGX, T. Rowe), Nov 2024 SoftBank tender, Aug 2026 company buyback (G15 L24 note), EDGAR SPV/feeder names (G15 L25).
- Changes: 10aa equity cell and KPI "0 of 6 … rounds of Oct 2024 and Mar 2025 (ST73–ST74)" → extend to "three rounds (Oct 2024, Mar 2025, Mar 2026) and the Oct 2025 tender"; add a stakes row ST86-class for the Mar 2026 issuer list. Note many of these names (Altimeter, Blackstone, Coatue, D1, Fidelity, D.E. Shaw Ventures) are also Anthropic Series F–H investors, but none is a METR funder.

**NF-2. OpenAI opened a >$3B unnamed individual channel and ETF inclusion in Mar 2026 — an unclosable gap in "none on any record".**
- G15 L35 (Task A), 2026-03-31, OpenAI (issuer), same URL as NF-1
- Quote: "For the first time, we extended participation to investors through bank channels, raising over $3 billion from individual investors. Today, we're also announcing that OpenAI will be included in several exchange-traded funds managed by ARK Invest"
- Not in CSVs ("bank channel" 0 hits).
- Changes: 10aa footnote scope. It currently says "Indirect fund exposure and private secondary purchases are not checked"; it should add that OpenAI itself reports >$3B from unnamed individuals via bank channels and ETF availability, so an individual (including a Jane Street person or any named individual donor) could hold OpenAI without appearing on any list. Grok correctly graded this "unknown", not "holds".

**NF-3. Hillspire's 20% of D.E. Shaw & Co. is the only indirect OpenAI path found for a METR funder.**
- G15 L31 (Task A), 2015-04-23, Forbes (press), https://www.forbes.com/sites/nathanvardi/2015/04/23/eric-schmidt-buys-20-stake-in-quant-hedge-fund-de-shaw/
- Quote: "Eric Schmidt, Google's billionaire chairman, has purchased a 20% stake in DE Shaw, the big quantitative hedge fund firm founded by billionaire David Shaw. Schmidt's family office, Hillspire LLC, scooped up the stake from the estate of Lehman Brothers"
- Partly in CSVs: ST49 (Forbes profile, 2026) records the 20% D.E. Shaw stake; nothing records that D. E. Shaw Ventures co-led OpenAI's Mar 2026 round (NF-1) and is named in Anthropic's Series H (ST26). Grok did not treat it as a "holds" row (correct: no press names Schmidt/Hillspire as an OpenAI holder, and a stake in the management company is not the same as LP exposure to the venture fund's positions).
- Changes: 10aa equity cell footnote and 10z Schmidt line note: "Hillspire's 20% of D.E. Shaw & Co. (2015) gives an unquantified indirect interest in a firm whose venture arm co-led OpenAI's Mar 2026 round and joined Anthropic's Series H; whether the stake carries economic exposure to those fund positions is not public." See LEADS L2.

**NF-4. Cari Tuna's own statement: no OpenAI stake, personal or foundation (Nov 2025).**
- G15 L28 (Task A), 2025-11-07, Forbes / Phoebe Liu (press quoting Tuna), https://www.forbes.com/sites/phoebeliu/2025/11/07/cari-tuna-billionaire-open-philanthropy-facebook/
- Quote: "Then they poured $30 million into OpenAI's nonprofit in 2017 through their foundation, and Moskovitz invested in Anthropic's $124 million funding round in 2021, "before it was obvious that these labs would make money," Tuna says. [...] Neither the couple nor their foundation own a stake in OpenAI."
- Not in CSVs as a sentence: ST33 cites the same article (forbes.com.au republication dated 2025-11-10) for the $500M nonprofit-vehicle sentence only; ST72 is Open Philanthropy's 2017 statement. This is a 2025 personal-and-foundation denial, the strongest negative statement available for Moskovitz.
- Changes: 10aa equity cell (OpenAI side) can cite Tuna 2025 alongside Open Phil 2017; add stakes row. Caveat: Grok took the sentence from a search snippet because the live page was captcha-walled (G15 header); confirm in a browser before quoting (see NOT PULLED NP-3).

**NF-5. Metaplanet's portfolio lists xAI (2024) and DeepMind (2011) beside Anthropic — Tallinn's vehicle holds equity in a third frontier lab.**
- G15 L29 (Task A), 2026-09-14, Metaplanet (issuer/vehicle page), https://metaplanet.com/portfolio
- Quote: "Anthropic — AI research and products that put safety at the frontier — United States — 2021. DeepMind — Build AI responsibly to benefit humanity — United Kingdom — 2011. xAI — Building artificial intelligence to accelerate human scientific discovery — United States — 2024."
- Not in CSVs: "xai" has 0 hits in stakes/shared_donors/money_flows/investments. ST43 records only the Anthropic page.
- Changes: outside 10aa's OpenAI-vs-Anthropic frame (OpenAI still absent), but it changes the premise "the lab METR's funders do not own" if generalised: METR's Series A lead holds xAI too. Belongs in stakes.csv (Tallinn/xAI, amount undisclosed) and shared_donors J12; relevant to Figure 11 (same donors both sides). Grok noted site:metaplanet.com OpenAI hits are news about xAI moving into OpenAI's old HQ, not a holding.

**NF-6. OpenAI's ownership split while the S-1 is confidential: Foundation 26%, Microsoft ~27%, employees+investors 47%; SoftBank ~13%; confidential S-1 announced 2026-06-08.**
- G15 L40 (Task B), 2025-10-28, OpenAI (issuer), https://openai.com/our-structure/ — Quote: "As of the closing of the recapitalization, the OpenAI Foundation holds a 26% equity stake in OpenAI Group, worth approximately $130B based on OpenAI Group's current valuation. [...] Also as of closing of the recapitalization, Microsoft holds roughly 27% of OpenAI Group, and the remaining 47% is held"
- G15 L41 (Task B), 2026-02-27, SoftBank Group (issuer release), https://group.softbank/en/news/press/20260227 — Quote: "Upon completion of the Follow-on Investment, SBG's cumulative investment in OpenAI is expected to total USD 64.6 billion, representing an ownership interest of approximately 13%."
- G15 L39 (Task B), 2026-06-08, OpenAI, https://openai.com/index/openai-submits-confidential-s-1/ — Quote: "We recently submitted a confidential S-1. We expect it to leak so we're just announcing it. We have not decided on timing yet"
- G15 L42 (Task B), 2026-05-04, WIRED (Brockman testimony), https://www.wired.com/story/greg-brockman-testifies-musk-v-altman-trial/ — Quote: "Altogether, OpenAI employees hold about 25 percent of shares. The foundation has 27 percent."
- Partly in CSVs: ST75 has the ~$130B Foundation figure; ST77 has "no public S-1" via WSJ. The percentages, the SoftBank 13%, and the issuer's own confidential-S-1 post are not recorded.
- Changes: 10aa "what rises" OpenAI cell can state the Foundation's 26% next to "$130B"; ST77 should cite the issuer post rather than WSJ alone; WATCHLIST S-1 row. Note the 26% (issuer) vs 27% (Brockman) discrepancy — see CONTRADICTIONS C-4.

### (b) OpenAI Foundation grants to METR's network

**NF-7. The Foundation's >$130M AI Resilience grants are unnamed as of 2026-09-10, and that program is the one that "supports independent testing and evaluations".**
- G15 L51 (Task C), 2026-06-01, OpenAI Foundation, https://openaifoundation.org/news/resilience-in-the-age-of-ai — Quote: "In the few short months since initiating our work, the Foundation is working to finalize more than $130 million in grants to organizations through our AI Resilience program, to be shared publicly soon and with more to come."
- G15 L48 (Task C), 2026-03-24, OpenAI, https://openai.com/index/update-on-the-openai-foundation/ — Quote: "Over the next year, as we quickly ramp up, the Foundation expects to invest at least $1 billion across life sciences and curing diseases, jobs and economic impact, AI resilience, and community programs." (Grok's note: the AI Resilience bullet says "supporting independent testing and evaluations"; no org named.)
- Not in CSVs (openaifoundation.org 0 hits).
- Changes: 10aa "what rises" OpenAI cell: "That foundation funds none of METR's network" must be scoped to "on any published grant list (People-First waves 1–2, Alzheimer's, Common Health, farmers, Intercept); its >$130M AI Resilience grants, the program that names 'independent testing and evaluations', were unnamed as of Sep 10 2026." Add to WATCHLIST.

**NF-8. Every published Foundation grant list checked: no METR-network or METR-about org.**
- G15 L45 (2025-12-03, People-First wave 1, https://openai.com/index/people-first-ai-fund-grantees/): "Through an open call, the Foundation will provide $40.5 million in unrestricted grants to 208 nonprofits across the United States." — 208 names scanned; "Arc of Madison County Inc (AL)" is a disability nonprofit, not ARC.
- G15 L46 (2026-06-04, wave 2 $9.5M: CareMessage, Dollar For, Every Cure, Manton Center, OCHIN, Lenfest); L47 (2026 People-First $50M, awards by Oct 2026); L50 (2026-04-08 Alzheimer's >$100M across six institutions incl. Arc Institute — biomedical, not Alignment Research Center); L52 (2026-08-13 Common Health Coalition $100M); L53 (2026-09-10 farmers $60M: UChicago, UC Berkeley, Precision Development, AIM for Scale/Notre Dame, Digital Green, CIMMYT); L55 summary row.
- Not in CSVs. Changes: gives 10aa's OpenAI-Foundation sentence a citable enumeration (new stakes/money_flows rows or a NOTES entry with these URLs). Caveat from G15 L50/L61: two "Arc" false-friends must not be confused with ARC.

**NF-9. Arc Institute — an OpenAI Foundation Alzheimer's grantee — was co-founded as a donor project by Moskovitz and Tuna.**
- G25 L61 (Task B), 2026-09-14, Arc Institute (issuer), https://arcinstitute.org/about — Quote: "Arc was started by Silvana Konermann, Patrick Hsu, and Patrick Collison. Arc's founding donors include Vitalik Buterin, Patrick Collison, John Collison, the Ron Conway family, Crankstart, Elad Gil and Jennifer Huang Gil, Daniel Gross, Dustin Moskovitz and Cari Tuna"
- Cross-lane with G15 L50 (Arc Institute among the six Alzheimer's institutions). Not in CSVs.
- Changes: none to 10aa's claim (Arc Institute is not METR's network), but worth a footnote-level note: the nearest overlap between OpenAI Foundation money and METR's funders is a biomedical institute Moskovitz/Tuna co-founded.

**NF-10. "Individuals from Jane Street Capital" co-fund Intercept with the OpenAI Foundation and Anthropic.**
- G15 L34 (Task C), 2026-06-26, OpenAI Foundation (X) + Dealroom, https://x.com/FoundationOAI/status/2070533340416164196 — Quote: "The OpenAI Foundation is joining Intercept as a founding partner through our AI resilience program. As AI accelerates advances in biology and medicine, we also need to prepare for the risks of misuse, including the potential for engineered outbreaks."
- Grok's note: Dealroom lists the $500M Intercept consortium as Stripe, Anthropic, The Flu Lab, "individuals from Jane Street Capital", and a Gates vehicle. Not in CSVs ("intercept" only matches unrelated Vanguard Schedule I rows).
- Changes: not a grant to METR's network; but the same anonymised phrase METR uses ("individuals from Jane Street") recurs in a fund co-financed by Anthropic and the OpenAI Foundation. Lead for identifying the individuals (L6). Grok correctly flagged: "Jane Street individuals are co-funders of Intercept, not OpenAI-Foundation grantees."

**NF-11 (cross-lane, already partly recorded). OpenAI corporate money reaches METR's parent ARC through the UK AISI Alignment Project, whose coalition includes Halcyon Futures and Schmidt Sciences.**
- G15 L55 note: "OpenAI Group PBC $7.5M Alignment Project (UK AISI, 2026-02-19) … out of Foundation-grant scope". G20 L33 note: Halcyon Futures "named as a co-participant in Schmidt Sciences' 2025-07-30 Alignment Project coalition".
- Already in evaluators.csv (AISI row: "Alignment Project GBP 27m total incl. GBP 5.6m from OpenAI plus Microsoft, Anthropic, AWS, Schmidt Sciences, Halcyon Futures … awardees include Jacob Hilton / Alignment Research Center"). Not in money_flows.
- Changes: 10aa's OpenAI column says "lab money to METR: no cash"; that is METR-specific and stays true. But the network claim ("funds none of METR's network") is about the Foundation; OpenAI Group PBC's money did reach ARC via a pooled UK fund. Add a money_flows row (OpenAI Group PBC → AISI Alignment Project → ARC/Hilton, amount per project up to £1M, not itemised) and a one-line footnote in 10aa. Note the $7.5M (G15) vs GBP 5.6m (evaluators.csv) are the same commitment in two currencies; state one.

### (c) Stake sizes or values — Schmidt, Jane Street, McClave, Tallinn

**NF-12. Tallinn, asked on record about a "$10 billion" stake and a "permanent observer seat", neither confirmed nor denied (Apr/May 2026).**
- G23 L46 (Task C), 2026-05-21 (recorded end Apr 2026), Jaan Tallinn on Manifold #112 (interview transcript), https://www.manifold1.com/episodes/ai-billionaire-on-existential-risk-jaan-tallinn/transcript
- Quote: "Yeah, not directly. Like one thing that has happened is that Anthropic as it has scaled the board has, has increased to the point where there is like every kind of individual stakeholder, so to speak has like less and less voice."
- Grok's note: Hsu's immediately prior prompt was "it estimated at about $10 billion stake in Anthropic" and "a permanent observer seat on the board"; Tallinn does not confirm the $10B. Not in CSVs ("manifold1|hsu" only matches an unrelated Vanguard row; "$10B" 0 hits).
- Changes: 10z Tallinn line and ST38–ST46: add a self-statement row "did not confirm or deny a $10B estimate; described board voice as diluted as the board grew". Do NOT surface $10B as a figure; it is the interviewer's. Also G23 L47 (same transcript): "All these, like, evaluations and capability, like cards, sheets, they are basically done using a process that just evaluates this new alien that has stepped out of the, out of the machine." — Tallinn on evaluations; does not name METR.

**NF-13. Tallinn owns 99.78% of Metaplanet Holdings OÜ (Estonian register via Äripäev Radar).**
- G23 L54 (Task D), 2026-09-14, Äripäev Radar (press/register aggregator), https://radar.aripaev.ee/isik/13272/jaan-tallinn — Quote: "METAPLANET HOLDINGS OÜ 99.78% 1,01 mln € 0 € (2024)"
- Not in CSVs. Changes: ST43 note (vehicle ownership established; "1,01 mln €" is the register's figure for the OÜ, not an Anthropic value — do not read it as the stake). Minor.

**NF-14. Tom Brown's amicus declaration in US v. Google (public RECAP copy) names Amazon and Google as biggest investors with the Google % redacted.**
- G20 L25 (Task A), 2025-02-14, Anthropic/Tom Brown (court filing), https://www.courtlistener.com/docket/18552824/1165/2/united-states-of-america-v-google-llc/ — Quote: "Anthropic has received investments from many sources. Amazon and Google are two of Anthropic's biggest investors, and both have invested billions of dollars in the company."
- Not in CSVs ("tom brown|18552824" 0 hits; IV13 carries Google 14% "per court filings … via press").
- Changes: 10z Google line wording: the public filing redacts the percentage; the 14% comes from press reporting (NYT 2025-03-11) of the filing, not from a readable public court document. Precision fix; see C-5. No Schmidt/Hillspire figure anywhere in the filing (G20 L26 none-found).

**NF-15. Hedgeweek/Reuters independently restate Jane Street's Anthropic-driven private gains (Apr 2026).**
- G21 L63 (Task C), 2026-04-27, Hedgeweek restating Reuters (press), https://www.hedgeweek.com/jane-street-outpaces-rivals-with-record-40bn-trading-haul/ — Quote: "Alongside its core trading business, Jane Street also benefited from gains tied to stakes in private companies, including artificial intelligence group Anthropic, reflecting its broader investment activity in private markets."
- Not in CSVs (ST27–ST30 are Bloomberg, AI Weekly, KuCoin). Minor: adds a second outlet (Reuters via Hedgeweek) to the ST27 sentence. No stake size. G21 also confirmed the Bloomberg Apr 24 / May 8 sentences from Wayback (L54, L55; already ST27/ST28) and that the WSJ Jun 20 recovered text has no Anthropic sentence (L52), so ST29 remains second-hand (AI Weekly).

**NF-16. BEMC Foundation's TY2024 grants are $4.0M to GiveWell and $2.418M to Vox Future Perfect (plus $1.808M approved for future).**
- G21 L26/L40 (Task B), 2024-12-31 and 2024-12-11, BEMC Foundation 990-PF (IRS XML), https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202523219349100137_public.xml — Quote (XML): "<RecipientBusinessName><BusinessNameLine1Txt>VOX MEDIA FUTURE PERFECT PROJECT</BusinessNameLine1Txt>"; note: "Amt 2418054; GrantDt 2024-12-11 … Purpose text in XML discusses 2024 Future Perfect coverage including AI safety … Approved-for-future Vox Amt 1807987". TY2023: Vox $611,527, GiveWell $1,000,000 (G21 L41).
- Partly in CSVs: J02 and M103 record "only Vox Media Future Perfect and GiveWell" with no amounts. Amounts and the AI-safety-coverage purpose text are new.
- Changes: J02 note (amounts); not a 10z stake fact. Worth noting for the media figures: an Anthropic Series A/B investor's foundation funds the Vox vertical that covers AI safety (see LEADS L14). No Anthropic shares on the 990-PF (ST53 stands).

### (d) New METR donors, amounts, or channels

**NF-17. Coefficient Giving's own page states METR "is not a Coefficient Giving grantee" while its staff recommend donors give to METR (Dec 2025).**
- G25 L59 (Task B), 2025-12-19, Coefficient Giving (issuer), https://coefficientgiving.org/research/suggestions-for-individual-donors-from-coefficient-giving-staff-2025/ — Quote: "Model Evaluation and Threat Research. Recommended by Peter Favaloro and the rest of our Technical AI Safety team. Note: This organization is not a Coefficient Giving grantee."
- Not in CSVs: J13 rests on the 2,911-row index snapshot; IF61 has only Kelsey Piper's "My understanding is that METR is not a Coefficient Giving grantee". This is the funder's first-person statement.
- Changes: shared_donors J13 and money_flows (a 0-amount statement row); 10aa "what rises" Anthropic cell and Figure 19 (the rule and the donor) can cite Coefficient itself for "no direct grant", and note the endorsement channel (Coefficient's Technical AI Safety team steering individual donors to METR). Also G25 L59 note: Open Phil 990 object 202513209349301211 grepped, no METR/ARC (consistent with M105).

**NF-18. CERR / Macroscopic Ventures (Anthropic Series A and B investor) funds Redwood Research and Longview, and holds impact investments in Apollo Research and Halcyon Venture Partners.**
- G20 L39 (Task D), 2026-09-14, Macroscopic Ventures (issuer grants page), https://macroscopic.org/grants — Quote: "Redwood Research is a nonprofit AI safety and security research organization working to better understand the risks that could arise if powerful AI systems purposefully act against the interests of their developers and human institutions broadly"
- G20 L40, same page — Quote: "We have supported Longview Philanthropy's Consortium for Digital Sentience Research and Applied Work."
- G20 L41, same page — Quote: "Apollo Research is dedicated to improving our understanding of AI to mitigate risks from dangerous capabilities in advanced AI systems." (listed under Impact Investments)
- G15 L32, same page — Quote: "Impact Investments. In addition to grants, we also make selective impact investments in socially beneficial companies. Anthropic — As part of their Series A and Series B, we invested in Anthropic, an AI safety and research company. Apollo Research. Differential Labs. Gray Swan. Halcyon Venture Partn"
- Not in CSVs: "macroscopic" appears only in stakes.csv (ST54–ST55, the Anthropic investment) and evaluators.csv EV02 (Apollo's Jan 2026 seed round, where Macroscopic is a named investor). No money_flows row for any Macroscopic grant. Amounts and dates are not on the page.
- Changes (the most material finding in these five lanes for 10aa): the "what rises" Anthropic cell lists Good Ventures/Coefficient and SFF as the Anthropic-linked funders of ARC, Redwood, RAND, Longview, Constellation, Halcyon, Tarbell and METR. CERR is a third Anthropic investor whose money reaches Redwood (METR's subcontractor), Longview (METR's pooled funder), Apollo (a candidate evaluator) and Halcyon Venture Partners (the incubator's VC arm, which "Invested in Every Round" of AIUC per M133). Add four money_flows rows (amount undisclosed), a shared_donors row for CERR (J02 covers McClave only), and name CERR in the 10aa cell. ST55 already carries "~$30 million in grants in 2025" for scale. Note the Longview grant is to a digital-sentience consortium, not the Frontier AI Fund; state that.

**NF-19. Schmidt Sciences gave METR board member Adam Gleave an AI2050 Early Career Fellowship (Nov 2025; cohort $18M / 28 fellows).**
- G20 L28–L29 (Task B), 2025-11-05, Schmidt Sciences (issuer), https://www.schmidtsciences.org/2025-ai2050-fellows-announcement/ — Quote: "Schmidt Sciences announced today that 28 scholars studying how to fulfill AI's potential to dramatically benefit humankind are eligible to receive more than $18 million in AI2050 fellowships." and "Adam Gleave, Co-founder and CEO, FAR.AI"
- G20 L30, 2025-11-04, FAR.AI (grantee), https://www.far.ai/blog/adam-gleave-named-schmidt-sciences-ai2050-early-career-fellow
- Partly in CSVs: board.csv B05/B17 and M136 record Schmidt Sciences among FAR.AI's institutional supporters; J08 mentions the AI2050 program size. The personal fellowship to Gleave is not recorded. Individual award not stated (do not divide $18M by 28 as a fact).
- Changes: board.csv B05 (Figure 04, the evaluator's board) and shared_donors J08: a METR funder (Schmidt Sciences, named on metr.org/about) made a personal award to a METR board member.

**NF-20. SFF-2026: $20–40M across four rounds; Main Round recommendations promised for September 2026; none published as of 2026-09-14.**
- G23 L28–L29 (Task A), 2026-04-22, SFF (issuer), https://survivalandflourishing.fund/2026/application — Quote: "Survival and Flourishing Fund (SFF) is organizing another S-Process Grant Round in collaboration with Jaan Tallinn and Survival and Flourishing Corp (SFC), planning to announce recommendations for all rounds and tracks throughout the Fall of 2026. We estimate that $20MM - $40MM in funding will colle" and "We expect to have recommendations for the Main Round announced in September 2026."
- G23 L30/L33: /2026/recommendations and six URL variants 404; homepage table has no SFF-2026 rows.
- Not in CSVs ("sff-2026" 0 hits in the four core CSVs; G5 header mentions it). Changes: WATCHLIST row; when published, M35–M48-class rows and 10aa's "Tallinn's SFF" cell change. Genuinely unpublished — valid none-found.

**NF-21. Tallinn's public ledger is stale: last-modified 2025-12-20, last disbursement 2025-03-31, byte-identical to the local copy; no 2025 SFF recommendation to METR/FAR/etc. appears as a payment.**
- G23 L34 (Task B), ledger dated 2025-12-20, jaan.info (self-published CSV), https://jaan.info/philanthropy/donations.csv — Quote: "2025-03-31,Slimrock,USD,"800,000","$800,000",Undisclosed donations,Undisclosed"
- G23 header: HTTP Last-Modified Sat 20 Dec 2025; sha256 identical to research/tallinn-donations-ledger-2026-09-13.csv (1134 rows; local copy's last row confirmed 2025-03-31 in this review). Running totals from the live file: ARC $4,222,000; METR $204,000; Redwood $3,202,000.
- Partly in CSVs: M49–M56 carry the individual lines; nothing records the ledger's cutoff. Changes: M39/M46 notes ("recommendation, not a payment" — and Tallinn's own ledger shows no payment through Mar 2025); 10aa's "$120K + $428K match" must stay labelled as recommendation. Also confirms M38 (SFF-2024 $204K) was paid in full in 2024 via SVCF ($20K) + Founders Pledge ($184K): J12's "$204,000 in 2024" is the same money as M38/M52/M53/M55, not additional.

**NF-22. SFF-2025 METR matching pledge ($428K) is 1x with a deadline of 2026-09-30.**
- G25 L46 (Task B), 2025, SFF (issuer), https://survivalandflourishing.fund/2025/recommendations — Quote: "Jaan Tallinn Model Evaluation & Threat Research (METR) Main: $192,000 Freedom: $265,000 Fairness: $15,000 Mean: $76,000 $548,000 Speculation: ($120,000)† Matching: {$428,000}‡ Model Evaluation and Threat Research, Inc. General support"
- Partly in CSVs: M39 has "$120,000 + $428,000 matching pledge" but not the $548,000 headline recommendation, the per-track split, or the 2026-09-30 deadline (Grok note: "Matching pledge 1x, deadline 2026-09-30").
- Changes: M39 note; WATCHLIST (after Sep 30 the match either converts or lapses). Note the $548K headline vs $120K+$428K presentation on the homepage — see C-7.

**NF-23. LaCentra-Sumerlin's METR support is labelled "Frontier Fund" in METR's own Aug 14 image alt text; LCSF is otherwise a Santa Barbara community foundation.**
- G25 L38 (Task B), 2024 (990) / 2026-08-14 (alt text), LaCentra-Sumerlin Foundation, 990-PF FYE Nov 2024 https://gt990datalake-rawdata.s3.amazonaws.com/EfileData/XmlFiles/202502889349100435_public.xml — Grok note: "Live lcsf.org describes Santa Barbara County community grants (education, homelessness, arts); Aug 14 image alt text says 'LaCentra-Sumerlin Foundation Frontier Fund'."
- Not in CSVs ("frontier fund" only matches an unrelated Vanguard row). Changes: M71/M101 note; LEADS L10 (the METR gift likely came from a named sub-fund, which would explain why the community foundation's grants list does not show it).

**NF-24. Effektiv Spenden forwarded further allocations in Feb/Mar/May 2024 (amounts to METR unstated).**
- G25 L44 (Task B), 2023-08 page (Wayback 2025-05-22), Effektiv Spenden, https://web.archive.org/web/20250522234351/https://effektiv-spenden.org/en/safeguarding-the-future/ — Quote: "METR, (formerly ARC Evals) - Evaluation of state-of-the-art AI systems to identify and minimize risks (128.000 €) Grants were made in August 2023." Note: "Page also says later allocations were forwarded Feb/Mar/May 2024 and names Longview as partner."
- Partly in CSVs: M61 has the €128,000 Aug 2023 line only. Changes: M61 note; LEADS L11.

**NF-25. philanthropy.org who-funds aggregate for METR through FY2024: $8.7M / 3 grants / 3 funders (ARC, Vanguard Charitable, Founders Pledge); no Schmidt entity.**
- G20 L31 (Task B), 2024-12-31, philanthropy.org (990 aggregator), https://philanthropy.org/990/who-funds/991219864/model-evaluation-and-threat-research — Quote: "Model Evaluation and Threat Research has received $8.7 million across 3 grants from 3 funders. Its largest funder is Alignment Research Center."
- Consistent with existing rows (N54 $4,553,935 [cash $4,477,169] + M87 $4,000,000 + M79 $184,000 ≈ $8.66M). Not new money; new as an independent aggregator confirming that through FY2024 990s Schmidt Sciences, Packard, Pew, Sijbrandij, LaCentra-Sumerlin, Astralis and Expa do not appear as METR grantors (each also confirmed negative from their own 990s in G25 L34–L40, matching M97–M102). Changes: none; supports the "not yet visible in 990s" wording for the about-page foundations (their grants post-date FY2024 filings — DM15–DM28 first-naming dates are Dec 2025–Aug 2026).

Items reviewed and found already recorded (no action): G15 L26–L27 Open Phil 2017 no-equity (ST72); G15 L56 @sama "employee-like access" post (IF17); G21 L56 FTX-estate 3,332,833 shares (ST20–ST21); G21 L57–L60 Series E–H (ST23–ST26); G21 L62 Apr 8 2026 tender lede (ST62); G25 L24–L25 Audacious $17M/$38M (M57–M58); G25 L27 Audacious FAQ (M119 note); G25 L30 Valhalla $10M to RAND and $3M to TED Foundation (M119, audacious-partners.csv AP06); G25 L42 Longview $220K (M59); G25 L45 SFF-2024 $204K (M38); G25 L52–L54 Founders Pledge 990 lines (M77–M79); G25 L55 EV USA $100K ARC (M90); G25 L60 ARC spin-off $4.55M (N54); G25 L63 Vanguard $4M (M87); G25 L64–L66 SVCF/AEF/Fidelity (M83, M95, M96); G25 L67–L68 $71M announcement (G3 DM01–DM03, G5 RZ01–RZ03); G23 L48–L49 Postimees dilution/observer quotes (ST40–ST41); G23 L52 Metaplanet Anthropic page (ST43).

---

## 2. LEADS (ranked)

**L1. Size and date CERR/Macroscopic's grants to Redwood and Longview and its Apollo/Halcyon Venture Partners investments (NF-18).** Why: adds a third Anthropic Series A/B investor to 10aa's "what rises" cell with named recipients in METR's network. Routes: (i) Macroscopic Ventures is a Swiss nonprofit (macroscopic.org/about, "founded 2019") — Zefix (zefix.ch) for the registered name/canton, then the cantonal foundation-supervision authority's published annual report if any; (ii) Redwood Research Group 990s TY2023–TY2024 (research/990-redwood-*.xml already on disk) Schedule B is redacted, but Redwood's own funders page or Coefficient grant pages may name CERR; (iii) Longview's "Consortium for Digital Sentience Research" page lists consortium funders; (iv) EA Forum topic page (ST55) says ~$30M of 2025 grants — its source link may be a Macroscopic annual letter with a grantee table; (v) Apollo Research's Jan 2026 seed announcement (evaluators.csv EV02) for Macroscopic's cheque.

**L2. Hillspire's D.E. Shaw stake: does 20% of D.E. Shaw & Co. carry exposure to D.E. Shaw Ventures' OpenAI (Mar 2026) and Anthropic (Series H) positions? (NF-3)** Why: the only indirect OpenAI path found for any METR funder; 10aa's "none on any record" needs a footnote either way. Routes: Forbes 2015 piece and Forbes profile (still lists the 20% in 2026, ST49); D.E. Shaw group structure (D. E. Shaw & Co., L.P. is the management company; D. E. Shaw Ventures is described on deshaw.com as the firm's venture arm investing from the firm's own capital and affiliated funds); any Form ADV Part 2 for D. E. Shaw & Co. (adviserinfo.sec.gov) listing Hillspire as an owner ≥25% (20% would fall below the Schedule A threshold — check whether it appears at all); press on whether Hillspire sold the stake.

**L3. OpenAI Foundation's >$130M AI Resilience grantee list (NF-7).** Why: the one Foundation program that names "independent testing and evaluations"; until published, 10aa's "funds none of METR's network" is unverifiable for the program most likely to fund an evaluator. Routes: openaifoundation.org/news (weekly); the Foundation is the old OpenAI, Inc. nonprofit — its Form 990 for 2025 (due Nov 2026, ProPublica EIN 81-0861541) Schedule I will list every grantee; the People-First 2026 awards (Oct 2026).

**L4. OpenAI Group PBC → UK AISI Alignment Project → ARC (Jacob Hilton): amount and date of the ARC award (NF-11).** Why: OpenAI corporate money reaching METR's parent via a pool; 10aa footnote. Routes: the AISI Alignment Project awardee PDF already cited in evaluators.csv (per-project up to £1M; check whether ARC's amount is listed); ARC's 2026 990 (Nov 2027) too late; Halcyon Futures' coalition role via schmidtsciences.org 2025-07-30 announcement.

**L5. Individual AI2050 award to Adam Gleave (NF-19).** Why: METR funder → METR board member personal award; board.csv B05. Routes: schmidtsciences.org/awardees profile page for Gleave (Early Career fellows' award sizes are usually stated on ai2050.schmidtsciences.org fellow pages); FAR.AI 990 TY2025 (Nov 2026) will not itemise a personal fellowship — so the fellow page is the only route.

**L6. Who the "individuals from Jane Street" are (NF-10; G21 Task A none-found).** Routes: Intercept Health Fund's founding-partner page (Dealroom paraphrased "individuals from Jane Street Capital"); Founders Pledge member directory (founderspledge.com/members, JS-rendered — open in browser and search "Jane Street"); GWWC pledge list; METR's next annual report; LinkedIn ("Jane Street" + "METR" advisor/board); the SFC board (G5 JS01 already found Andrew Critch, ex-Jane Street, SFC director). Do not infer McClave/Berger without a source (Grok correctly refused).

**L7. Metaplanet's xAI holding (NF-5).** Why: a METR funder with equity in a third frontier lab; belongs in stakes.csv and Figure 11. Routes: metaplanet.com/portfolio/xai page (year 2024; look for round name); xAI's 2024 Series B/C investor lists (issuer post May 2024 / Dec 2024) for "Metaplanet" or "Jaan Tallinn"; Estonian press (Äripäev) "Tallinn xAI".

**L8. SFF-2026 Main Round recommendations (NF-20) and the SFF-2025 match deadline 2026-09-30 (NF-22).** Routes: survivalandflourishing.fund/announcements and homepage table; jaan.info ledger for any 2025–2026 disbursements (NF-21; last-modified header is a cheap poll).

**L9. Which sub-fund at LaCentra-Sumerlin ("Frontier Fund") gave to METR, and its FYE Nov 2025 990-PF (NF-23).** Routes: lcsf.org site search "Frontier Fund"; ProPublica EIN 77-0416683 for the FYE 2025-11-30 filing (~Oct 2026).

**L10. Effektiv Spenden's 2024 allocations to METR (NF-24).** Routes: effektiv-spenden.org "Safeguarding the future" fund report 2024 (German site: effektiv-spenden.org/zukunft-schuetzen or the annual "Transparenzbericht"); the page is Cloudflare-403 to fetchers but opens in a browser.

**L11. Tallinn's paywalled 2026 interviews (G23 L50, L56–L58).** Delfi 2026-08-24 (Dec 2025 Viik interview) body; Äripäev radio early Jan 2026 (the source of the board-seat quote); Äripäev 2026-04-15/04-21 bodies. Why: any stake remark beyond "substantially diluted". Route: NP-14.

**L12. Fluidstack $1.5B round led by Jane Street (G21 L82).** Why: another Jane Street–Anthropic infrastructure link (Fluidstack builds Anthropic's TPU deployment). Route: Fluidstack's own release or Bloomberg/FT Sep 2026; the X post is secondary ("Source" unnamed).

**L13. Vox Future Perfect's funder disclosure (NF-16).** Why: BEMC (Anthropic investor) funds the AI-safety journalism vertical with an explicit AI-safety purpose text; relevant to amplifier/media figures, not to 10aa. Route: vox.com/future-perfect "supported by" page; BEMC TY2025 990-PF (~Nov 2026).

**L14. Second-outlet confirmation of Tuna's "no stake in OpenAI" sentence (NF-4).** Route: NP-3.

---

## 3. NOT PULLED

Every none-found / blocked / paywalled / 403 / login row where a source plausibly exists, with a manual route; or "genuinely absent".

**G15**
- NP-1. CNBC 2024-10-02 and 2025-03-31 live 403 (G15 header; L18, L20). Resolved via Wayback; the Wayback copies are saved under research/openai-rounds/. Manual: not needed.
- NP-2. Open Philanthropy 2017 OpenAI grant page not recovered live (header; L27). Manual: open https://coefficientgiving.org/grants/openai-general-support/ in a browser (JS-rendered); or https://web.archive.org/web/2024*/openphilanthropy.org/grants/openai-general-support/ and pick a 2024 capture. Already in ST72 from Wayback; low priority.
- NP-3. Forbes 2025-11-07 Tuna profile paywalled/captcha (header; L28). Manual: open https://www.forbes.com/sites/phoebeliu/2025/11/07/cari-tuna-billionaire-open-philanthropy-facebook/ in a browser; Ctrl-F "stake in OpenAI". Alternative: the forbes.com.au republication already used for ST33 (https://www.forbes.com.au/news/billionaires/this-billionaire-couple-has-a-plan-to-give-away-a-20-billion-facebook-fortune/) — search the same phrase there.
- NP-4. OpenAI S-1/F-1 principal-stockholder table (L36–L39). Genuinely absent: confidential submission (issuer, 2026-06-08); nothing on EDGAR full-text or company browse. Watch EDGAR company search "OpenAI Group" (https://www.sec.gov/cgi-bin/browse-edgar?company=OpenAI+Group&action=getcompany) after any public flip.
- NP-5. OpenAI Foundation AI Resilience >$130M grantee names (L51). Genuinely absent as of 2026-09-10. Manual: https://openaifoundation.org/news (check for a "resilience grantees" post); later, ProPublica EIN 81-0861541 (OpenAI, Inc.) 2025 Form 990 Schedule I.
- NP-6. 2026 People-First AI Fund awards (L47). Not yet announced (applicants notified by Oct 2026). Manual: same news page.
- NP-7. Bank-channel >$3B individuals and ARK ETF holders (L35). Genuinely absent: no public list exists. ARK's ETF holdings files (ark-funds.com daily holdings CSV) would show OpenAI as a line but not who holds the ETF.
- NP-8. @chrislehane no posts in window; @OpenAI/@FoundationOAI no METR mention (L57). Manual: https://x.com/search?q=from%3Achrislehane%20since%3A2026-09-09&f=live (cap was 10 hits/query; a browser scroll has no cap).

**G20**
- NP-9. NYT 2025-03-11 Google–Anthropic stake article blocked (header). Manual: https://www.nytimes.com/2025/03/11/technology/google-anthropic-investment.html (URL from press citations; verify) with a subscription, or paste into archive.ph search. Only needed to source IV13's 14%; the public RECAP declaration has the % redacted (NF-14), so the unredacted number is under seal — that part is genuinely absent.
- NP-10. CNN 2024-03-10 McClave piece via archive.is CAPTCHA (header). Live URL https://www.cnn.com/2024/03/10/politics/pro-biden-dark-money-group-invs/index.html is already quoted in ST52; no action.
- NP-11. Schmidt/Hillspire Anthropic stake figure (L26). Genuinely absent from issuer, court and Schmidt's own statements. Only future route: Anthropic's S-1 (if Hillspire is ≥5%, which is unlikely) or a Schmidt interview.
- NP-12. Schmidt Sciences / Schmidt Fund grants to METR-network orgs (L33). Partly structural: Schmidt Sciences LLC is not a 990 filer (M99). Manual: (i) https://philanthropy.org/990/grants-by/463460261 — the Eric and Wendy Schmidt Fund page lists only the top 100 of 518 grantees; page through or use ProPublica full-text search restricted to EIN 46-3460261 with q="Model Evaluation" / "Redwood Research" / "Constellation" / "Halcyon" / "MATS" / "Epoch" / "Transluce" / "Tarbell" / "Longview" / "Founders Pledge" (https://projects.propublica.org/nonprofits/full_text_search?q=...); (ii) schmidtsciences.org program pages for "Trustworthy AI" and "AI Safety Science" list institutional awardees; (iii) METR's grant amount itself is genuinely absent until METR or Schmidt Sciences publishes it (METR's 990 Schedule B is not public).
- NP-13. Schmidt 2026 statements on Anthropic/METR (L34). Manual: https://x.com/search?q=from%3Aericschmidt%20(Anthropic%20OR%20Amodei%20OR%20METR)&f=live scrolled in a browser (Grok's 10-hit cap); plus a Google News search "Eric Schmidt" Anthropic 2026 for interviews. Plausibly genuinely absent.
- NP-14. McClave/CERR stake figures (L42) and McClave grant to METR network (L43). Genuinely absent for stakes (no filer holds Anthropic shares: ST53). For CERR grants see L1 (routes exist).

**G21**
- NP-15. WSJ 2026-06-20 Jane Street profile paywalled after the lede (header; L52). Manual: https://www.wsj.com/tech/ai/jane-street-ai-wall-street-bdfcc81a with a WSJ login; or Factiva/ProQuest at a library; or archive.ph search of the URL (Wayback 20260620023742 has only the opening). Needed to move ST29 from second-hand (AI Weekly) to primary and to see whether WSJ states a share count or "% of private book".
- NP-16. Bloomberg 2026-04-24 live 403 and 2026-05-08 lede-only (header). Resolved via Wayback id_ captures 20260428093719 and 20260515123421 (L54–L55). No action.
- NP-17. EA Forum search for Jane Street + METR (header). Manual: https://forum.effectivealtruism.org/search?query=%22Jane%20Street%22%20METR in a browser (JS UI).
- NP-18. Founders Pledge /about and /members JS-thin (header). Manual: https://www.founderspledge.com/members in a browser, filter/search "Jane Street".
- NP-19. Vanguard Charitable DAF principal for the $4.0M (G25 L70 too). Genuinely absent: DAF sponsors never disclose advisors; METR's Schedule B is not public.
- NP-20. BEMC FY2025 990-PF (header). Not yet filed (TY2024 was submitted 2025-11-17; expect TY2025 ~Nov 2026). Manual: https://projects.propublica.org/nonprofits/organizations/854281986.
- NP-21. LinkedIn not searched (out of brief). Manual: LinkedIn people search "Jane Street" with keyword "METR" or "Model Evaluation and Threat Research"; and METR's team/advisors on LinkedIn for a Jane Street past employer.
- NP-22. Jane Street in Anthropic's 2026 employee tender; "second 2026 tender" (L62). Genuinely absent: no buyer list was published and no second 2026 tender was found (see C-6).
- NP-23. Jane Street + METR posts over 2,000 views since 2026-09-09 (L89). Cap-limited. Manual: https://x.com/search?q=%22Jane%20Street%22%20METR%20since%3A2026-09-09&f=live and scroll; sort by Top as well.

**G23**
- NP-24. SFF-2026 recommendations (L30, L33). Genuinely unpublished as of 2026-09-14. Manual: https://survivalandflourishing.fund/announcements and the homepage "Recent Grant Recommendations" table; try https://survivalandflourishing.fund/2026/main/recommendations again after the September announcement.
- NP-25. Tallinn's own X handle not resolved (header; L51). Genuinely absent in practice: Tallinn has no active verified X account that Grok could find; his public writing is on LessWrong as user "jaan". Manual: https://www.lesswrong.com/users/jaan (live; greaterwrong mirror showed nothing after 2025-12-03).
- NP-26. Äripäev 2026-04-15 and 2026-04-21 bodies paywalled (L56–L57); Delfi 2026-02-13 remainder (L58); Delfi/Arvamus 2026-08-24 Viik–Tallinn interview body (L50). Manual: aripaev.ee digital subscription (or Estonian National Library's e-access), then Ctrl-F "osalus" (stake) and "protsent"; Delfi "Kogupakett" subscription for arvamus.delfi.ee/artikkel/120605248. The Postimees 2026-02-22 republication already carries the two Tallinn quotes (ST40–ST41).
- NP-27. Original Äripäev radio segment, early Jan 2026 (L49 note: "original Äripäev page not separately retrieved"). Manual: https://www.aripaev.ee/raadio search "Jaan Tallinn" January 2026; the audio may carry more than the one sentence Postimees quoted.
- NP-28. ERR 2026 article with a Tallinn stake figure (L59). Genuinely absent (ERR names him in the owner circle without a figure).
- NP-29. SVCF $50,450 vs ledger $50,000 (L45). Genuinely unexplained by the ledger. Only route: ask SFF/SVCF; or note that SVCF sometimes adds a fee/adjustment — do not assert.
- NP-30. Ledger lines since 2026-09-01 (L34). Genuinely absent (file unchanged since 2025-12-20). Manual poll: `curl -I https://jaan.info/philanthropy/donations.csv` and compare Last-Modified (fetch-only).

**G25**
- NP-31. Vanguard Charitable FY2025 XML 404 on GivingTuesday mirror (header; L63). Already resolved in M87 from the ProPublica rendered Schedule I (row 15424). No action.
- NP-32. effektiv-spenden.org 403 Cloudflare (header; L44). Manual: open https://effektiv-spenden.org/en/safeguarding-the-future/ in a browser; look for 2024 allocation notes (L10).
- NP-33. Coefficient grants search 404/JS (header; L59). Manual: https://coefficientgiving.org/grants/ in a browser, search box "Model Evaluation" — expected 0 results (index snapshot J13 and the staff-suggestions page NF-17 agree).
- NP-34. Packard grants database JS (L37). Manual: https://www.packard.org/grants-and-investments/grants-database/ → keyword "Model Evaluation" (M68 retry already returned 0 of 0 on 2026-09-13). Likely genuinely absent until Packard's database updates; Packard's TY2025 990-PF (~Nov 2026) is the filing route.
- NP-35. Pew site search JS (L35). Manual: https://www.pewtrusts.org/en/search?q=METR; Pew's 990 for FYE June 2026 (filed ~May 2027) is the filing route. Plausibly genuinely absent until then.
- NP-36. Schmidt Sciences awardees page (L36). Manual: https://www.schmidtsciences.org/awardees/ and program pages (see NP-12).
- NP-37. Longview Frontier AI Fund disbursement report (L43). Genuinely absent to non-donors (private to $100K+ donors, stated on the page). Longview Philanthropy USA TY2025 990 (~Nov 2026) is the only public route (M111/M113 show TY2024 had no METR line).
- NP-38. Sijbrandij Foundation TY2025 990-PF (L34). Not yet filed; manual: https://projects.propublica.org/nonprofits/organizations/854270305 late 2026. METR first named Sijbrandij on 2025-12-16 (DM14), so the grant should appear in the TY2025 filing.
- NP-39. LaCentra-Sumerlin FYE Nov 2025 990-PF (L38). Not yet filed (~Oct 2026); manual: ProPublica EIN 77-0416683; plus lcsf.org "Frontier Fund" page (L9).
- NP-40. Astralis Foundation grantee list (L39). Not a US filer. Manual: UK Charity Commission register search "Astralis" (https://register-of-charities.charitycommission.gov.uk/) and Companies House; astralisfoundation.org/team for the principals. Plausibly genuinely absent (no grantee list published).
- NP-41. Expa.org grant (L40). The Expa 990-PF entity is tiny (M102); the METR gift likely came from Garrett Camp personally or another Expa vehicle. Genuinely absent on public records unless METR discloses.
- NP-42. AISI cash grant to METR (L41; M74). Manual: UK Contracts Finder https://www.contractsfinder.service.gov.uk/Search with supplier "Model Evaluation" / "METR"; gov.uk "AI Security Institute" grants pages (Systemic Safety Grants, Challenge Fund awardee lists); AISI's own "grants" page. Partnership is documented; a cash line may be genuinely absent.
- NP-43. Who committed what of the ~$71M (L69). Genuinely absent: METR's announcement does not allocate; METR's FY2025/FY2026 990s show totals only (Schedule B withheld). Partial route: each foundation's own 990 for the 2026 year (2027 filings).
- NP-44. Vanguard DAF principal (L70). See NP-19 — genuinely absent.
- NP-45. Patrick Collison / Arc Institute, Vitalik Buterin METR grants (L61–L62). Manual for Buterin: https://x.com/search?q=from%3AVitalikButerin%20METR&f=live; Kanro/Buterin grant pages. Otherwise plausibly genuinely absent (neither is named on metr.org/about).
- NP-46. 2026 "why I fund METR" donor posts (L72). Cap-limited. Manual: X searches from:zoink, from:geoffralston (verify handle), from:snewmanpv (Steve Newman; verify) with "METR"; EA Forum/LessWrong search "METR" 2026 by donors. Plausibly genuinely absent.
- NP-47. TED/Audacious statement naming METR's donors (L16, L31). Genuinely absent: Audacious FAQ says TED does not fund grantees and per-project donors are not named; the only filing-level Canary payment is Valhalla → RAND (M119). Route: Audacious partners' TY2025 990-PFs (WATCHLIST) — and note NF-25's implication that none of them shows a METR line through TY2024.

---

## 4. CONTRADICTIONS

**C-1. (Lane vs figure, material) CERR's network grants are absent from 10aa's "what rises" cell.** G20 L39–L41 / G15 L32 show CERR/Macroscopic (Anthropic Series A+B) funding Redwood, Longview, Apollo and Halcyon Venture Partners. The 10aa cell and the README's 10aa description name only "Moskovitz and Tuna's philanthropy … and Tallinn's SFF" as the Anthropic-linked funders of METR's network. Not a false statement, but the cell is incomplete and the KPI framing ("the couple whose foundation funds METR's parent, subcontractor, office, pooled funders and incubator") understates how many Anthropic Series A investors fund the same network (three of five: Moskovitz, Tallinn, CERR; Schmidt Sciences funds METR directly and Gleave personally; McClave/BEMC funds none of it).

**C-2. (Lane vs figure, scoping) 10aa's "That foundation funds none of METR's network."** G15 L51 shows the >$130M AI Resilience grantee list is unpublished; G15 L55 shows OpenAI Group PBC (not the Foundation) money reached ARC via UK AISI (evaluators.csv). The sentence is true of published lists and should say so.

**C-3. (Lane vs figure, scoping) 10aa KPI "0 of 6 … rounds of Oct 2024 and Mar 2025".** G15 extends the negative to Mar 2026 and the Oct 2025 tender (NF-1) but also documents the >$3B unnamed individual channel and ETF availability (NF-2) and the Hillspire/D.E. Shaw path (NF-3). "None on any record" remains accurate; the footnote's "indirect fund exposure … not checked" is now partly checked and should name what was found.

**C-4. (Within G15) OpenAI Foundation 26% (issuer, our-structure, L40) vs 27% (Brockman testimony via WIRED, L42).** Both are post-recapitalization statements; issuer is primary. Also within G15: L24's note describes the Oct 2025 secondary as "~$6.6B" while the Fortune quote says "approximately $6 billion". Use the quoted figure or cite the later Caproasia close explicitly.

**C-5. (Lane vs figure, precision) 10z Google line: "14% per court filings in the Google antitrust case (Mar 2025, via press)".** G20 L25 shows the public RECAP copy of the Tom Brown declaration redacts Google's percentage. The 14% therefore rests on press access to a sealed/unredacted figure, not on a readable public filing. Wording should be "14% per NYT's report of a court filing; the public filing redacts the figure".

**C-6. (Brief vs lane) G21's brief asks "whether Jane Street participated in the second 2026 tender".** G21 header/L62: only one 2026 employee tender was found (launched ~Feb 2026, completed 2026-04-08 at $350B); no second 2026 tender exists in the record. The brief's premise is unsupported; ST62 is consistent with G21.

**C-7. (Between lanes, presentation) SFF-2025 METR recommendation.** G25 L46 quotes the recommendations page: headline "$548,000" (Main $192K + Freedom $265K + Fairness $15K + Mean $76K) with "Speculation: ($120,000)†" and "Matching: {$428,000}‡". M39 and 10aa carry "$120,000 + $428,000 matching pledge" (from the homepage table). These are two presentations of the same line (the homepage shows speculation + match; the round page shows the full S-Process total). Decide which to display and say which; do not add them. The G23 brief's own summary ("$120K + $428K match (2025) to METR") follows the homepage form.

**C-8. (Between lanes, dates) Forbes/Tuna article: G15 L28 dates it 2025-11-07 (forbes.com US URL); ST33 and 10z say "Forbes, Nov 10 2025" (forbes.com.au republication).** Same Phoebe Liu article; pick one URL/date and note the other.

**C-9. (Between lanes, currency) OpenAI's Alignment Project commitment: G15 L55 says "$7.5M"; evaluators.csv says "GBP 5.6m".** Same commitment; use one and state the conversion source.

**C-10. (Lane vs existing row, cosmetic) G23's ARC ledger total $4,222,000 includes the $50,000 SFF-spec line that M82 records as SVCF's $50,450 Schedule I grant.** Not a contradiction in substance (M82 already flags the $450 gap; G23 L45 confirms the ledger cannot explain it) but any figure quoting "Tallinn → ARC $4.22M" should say "per his ledger" since the 990-side sum is $450 higher.

**C-11. (Lane vs lane, none) G21's Jane Street findings, G23's Tallinn findings and G20's Schmidt/McClave findings agree with ST20–ST55 in every particular checked; no stake figure in any lane conflicts with an existing row.**

**C-12. (Grok caveat worth carrying) G15 L50/L61 and G15 L45 warn that "Arc Institute" (biomedical, OpenAI Foundation Alzheimer's grantee) and "Arc of Madison County" (People-First grantee) are not Alignment Research Center.** Any automated grep of OpenAI Foundation lists for "ARC" will false-positive on both.

---

Files read (absolute): /mnt/f/projects/memes/ai-machine/10-metr/research/grok-out/{G15-openai-equity,G20-schmidt,G21-jane-street,G23-tallinn,G25-donors}.csv; /mnt/f/projects/memes/ai-machine/10-metr/research/grok-briefs/{G15-openai-equity-and-openai-foundation,G20-schmidt-hillspire-schmidt-sciences,G21-jane-street-individuals-mcclave,G23-tallinn-sff-2026,G25-metr-donor-list-and-channels}.md; /mnt/f/projects/memes/ai-machine/10-metr/research/{stakes,money_flows,shared_donors,finances,board,evaluators,investments,independence_fight,audacious-partners,tallinn-donations-ledger-2026-09-13}.csv; /mnt/f/projects/memes/ai-machine/10-metr/research/grok-out/{G3-metr-donor-mentions,G5-2026-raise,G5-jane-street}.csv; /mnt/f/projects/memes/ai-machine/10-metr/research/agents-2026-09-14/S11-stakes/REPORT.md; /mnt/f/projects/memes/ai-machine/10-metr/scripts/generate.py (fig_stakes, fig_asym); /mnt/f/projects/memes/ai-machine/10-metr/{README,CHANGELOG}.md; /mnt/f/projects/memes/ai-machine/10-metr/research/WATCHLIST.md.
