# S6-press REPORT — press/web sweep, 2026-09-13 12:00 UTC to 2026-09-14 07:35 UTC

Written 2026-09-14 07:40 UTC. Inputs: research/independence_fight.csv (IF01–IF113 as of 01:44 UTC), research/NOTES-independence.md. Outputs: items.csv (56 rows, PR01–PR56, in-window items and negative checks), context_items.csv (17 rows, CX01–CX17, items published before the window that bear on funding/security questions), docs/ (84 files: raw pages, JSON, EXTRACTS.md, FETCH-LOG.md).

## 1. What is new since IF42 (The Verge, Sep 13 19:41 UTC)

### 1a. Press that names METR in connection with Sacks or independence
Seven new press items repeat Sacks's METR sentence; none adds a funder name, a document, or a METR reply:
- Tech Insider (tech-insider.org), Sep 13 18:14 UTC (PR01) — "took direct aim at METR, the third-party evaluator Anthropic uses ... too intertwined with Anthropic's own investors and staff to serve as a neutral safety referee." It also predicts "METR's independence will become a recurring talking point in Washington through the rest of 2026."
- The Eastern Herald, Sep 14 02:23 UTC (PR02) — "Sacks questioned whether METR is genuinely independent given its institutional ties to Anthropic's investors and staff." It also misreports the essay as "granting METR ... permanent employee-level access" as a done commitment.
- ITmedia NEWS (Japan), Sep 13 23:14 UTC (PR03), and Digital Today (Korea), Sep 14 02:49 UTC (PR04), which cites ITmedia — the story is now in East Asian trade press, still with no funder named.
- Shelly Palmer (PR05), ZeroHedge via Bugle Call (PR06), Michael Parekh's ARD #162 (PR07) — quote the sentence verbatim.
- Neowin (PR08) and Forbes/Majic (PR09) are listed by Techmeme/search under the Sacks story but were not retrievable (three attempts each); search snippets show only the Sacks sentence.
- Techmeme's Sep 13 23:00 UTC Sacks block also lists NYT (silicon-valley-ai-slowdown), WSJ opinion ("The Great AI Slowdown"), NPR, HuffPost, Newsmax, Free Press (Cowen). NPR, HuffPost, Politico and the visible part of Cowen do not mention METR; NYT and WSJ could not be read (PR43–PR45). Whether the NYT piece names METR is the main open gap.

### 1b. Who funds METR — what the window's items actually say
No press item in the window names a METR funder. The funding claims in circulation are on Hacker News and are unsourced:
- HN 49672510 (essay thread), anon373839, Sep 13 13:52 UTC: "They are ex-Anthropic employees and others with direct financial interests in Anthropic." (PR11)
- HN 49678683, nullbio, Sep 13 11:00 UTC (an hour before the window) and 02:47 UTC: "METR's salaries are listing around 500k/yr ... where this non-profit with ~35 people is getting all of its money?"; "Dario's sister ... married to the co-founder of Open Philanthropy"; "Ajeya Cotra ... left Coefficient and joined METR"; "Alignment Research Center donated ~$4.5mil to METR"; "funded by all the same NGOs who are funded by Anthropic and its investors ... full of ex-Anthropic employees with massive equity stakes." Turn_Trout replied 19:47 UTC: "This conspiracy theory is truly crazy" and asked for a source on equity stakes; none was given. (PR12)
- The nearest press statement of METR's funding rule in the window is LiveNewsChat (PR20): "METR, an independent evaluation nonprofit that says it took no payment from OpenAI."
- Pre-window items that do name funders (context_items.csv): TNW Sep 4 (Coefficient's $36,566,000 to Redwood, not METR; "independent scrutiny of frontier AI is becoming a derivative of frontier AI valuations"); Business Insider via Jingletree, Aug (METR "doesn't take money from the frontier AI labs or their employees" but "accepts compute grants"; salaries "reaching $503,000"); ITBB Jun 3 ("predecessor received approximately $1.5 million from Open Philanthropy in 2022 ... current donors — including the Pew Charitable Trusts" — the Pew claim is not in our money_flows.csv and should be treated as unverified).
- Note the HN salary figure (~$500k) and the BI figure ($503,000) are consistent; the "~35 people" figure is the commenter's.

### 1c. Lab side — who gets "employee-like access"
Still nobody. New in window:
- Sam Altman, X, Sep 14 04:05 UTC (PR13): 1,900-character post; commits OpenAI to "explicit safety cases in advance of frontier reinforcement learning runs" and says "we are excited by ideas like independent auditors" and "we do not believe we need to wait for an anti-trust exemption or legislation." Names no evaluator. Bloomberg's Sep 14 write-up (PR14, read via Free Malaysia Today) also names none.
- Satya Nadella, X, Sep 13 19:36 UTC (PR16): welcomes "deliberate pacing" and "embedded evaluators"; governance "cannot be controlled by a handful of entities." Names no evaluator. Wire coverage (ANI/Tribune/Livemint, PR18; Unite.AI, PR17) adds nothing; Unite.AI restates METR as the essay's example.
- The Information, Sep 13 (PR27, paywalled; syndicated summaries): Anthropic/OpenAI/Google sub-CEO working groups "have met regularly since July" on an industry-led standards body; Altman told staff labs may need to build a testing/auditing body themselves. Stoller's BIG (PR28, Sep 14) reads this as "backchannel conversations about establishing an AI standards organization, which presumably would coordinate this cartel."
- openai.com/news and anthropic.com/news (PR56): no post naming evaluators through Sep 11 / Sep 10 respectively.
- Several outlets now state as fact what the essay only offered as an example: Eastern Herald ("granting METR ... permanent employee-level access"), Winzheng ("Amodei selected METR ... as one of the first on-site evaluators"), Karmactive ("Anthropic Signs METR For Outside Review" — actually the Aug 31 incident-review statement). LiveNewsChat (PR20) is the one piece that says the opposite plainly: "no date on it yet ... no named evaluator under contract, and no published scope of access."

### 1d. Coefficient Tailwind / Halcyon
Nothing in window. Coefficient's research index has no post after the Sep 9 items already on file; the Tailwind pages returned 403 to WebFetch today and were captured at 00:32 UTC (research/tailwind-initiatives-2026-09-14b.html). Halcyon's "Request for Founders" is dated Aug 6 2026 and lists "Independent organizations that test for dangerous capabilities and track whether frontier labs are following their safety commitments" as a priority (CX17). No press item in window links Tailwind or Halcyon to a new evaluator. (PR54)

### 1e. Security-community critique
No new press item in window. The Stack (IF36, Sep 13 16:24 UTC) remains the only outlet quoting Linares. Security trade press (Register, Dark Reading, SC Media, The Stack "vibe-coded app") covers only METR's own Aug 31 breach disclosure. HN 49685991 has one relevant new comment (filearts, Sep 14 02:09 UTC): "The auditor signed off on the model, so who is to blame? ... METR did. The public did. But it seems like the lab has crafted a system in which they remain blameless." Pre-window essays worth having on file: Andrew Wu Sep 5 ("slop-vestigation ... OpenAI controlled too much of the investigation") and Venkatesh Rao Aug 31 (quotes Khlaaf on "badly specified objectives operating inside badly secured environments"). (PR55, CX12, CX13)

### 1f. Newsletters and forums
No Sep 13–14 post on Sacks/METR from Zvi (latest Sep 12), Transformer (Sep 11), Platformer (Sep 11), Import AI (Sep 7), Dean Ball (Sep 1), Timothy Lee (Sep 10), Gary Marcus (two-cheers piece is IF37), Marginal Revolution ("Dario Calls for a Pause" Sep 12; nothing on Sacks), Astral Codex Ten (Open Thread 451 mentions the pact, not METR). LessWrong's new-post index for Sep 13–14 (20 posts) has nothing on METR/Sacks; EA Forum's last relevant post is the Sep 12 Amodei linkpost with four comments, none on METR. (PR52, PR53)

## 2. Is there any METR response?
No. As of 2026-09-14 07:35 UTC no statement by METR, Beth Barnes, Chris Painter or Hjalmar Wijk responding to Sacks, or to the "intertwined with Anthropic's investors and staff" claim, was located.
- Checked: metr.org/blog (latest Aug 31), metr.org/research (Aug 26), metr.substack.com archive API (Aug 14), metr.org homepage (no banner); X syndication timelines for @METR_Evals and @BethMayBarnes (empty/blocked); Beth Barnes's LessWrong activity (last April 2026); HN, LessWrong, EA Forum; every press item above.
- Search terms used: "METR Beth Barnes responds Sacks independence funding"; "METR Chris Painter OR Hjalmar Wijk OR Beth Barnes statement Sacks September 2026"; "METR declined to comment OR did not respond OR spokesperson OR said in a statement Sacks independent Anthropic"; "Beth Barnes OR @BethMayBarnes OR @METR_Evals Sacks intertwined reply September 13 2026"; "x.com METR_Evals OR BethMayBarnes OR ChrisPainterYup status September 13 2026 independence funding evaluators"; "Hjalmar Wijk OR Chris Painter METR September 2026 interview OR statement OR podcast".
- The only officer post touching the question remains Painter's Sep 14 04:06 UTC reply to Tim Hwang (IF64): "Can you elaborate on your definition/criteria for 'independent' and 'sustainably funded'? Also interested in reactions from others." It is a question, not a defence, and does not mention Sacks.
- No outlet reports asking METR for comment (no "declined to comment"/"did not respond" line found). The NYT and WSJ pieces could not be read; if either sought comment, that is where it would be.

## 3. Three most consequential items and why
1. Sam Altman's Sep 14 04:05 UTC post (PR13) — the first substantive OpenAI follow-up to "we will do the same" (Sep 12). It shifts the commitment from embedded evaluators to "safety cases in advance of frontier RL runs" and downgrades evaluators to "ideas like independent auditors" that OpenAI is "excited by." Two days after Amodei named METR, neither lab has named anyone, and OpenAI's language is drifting away from the badge-and-desk model. This is the fact the figure should carry: evaluator_access_named = none, as of Sep 14.
2. The Information's standards-body story (PR27) plus Stoller's reading of it (PR28) — establishes that the three labs were meeting on an industry-led testing/auditing body since July, before the essay, and that Altman told staff labs may build it themselves. It reframes "embedded evaluators such as METR" as one option inside a lab-designed structure, which is Sacks's cartel point made by a left-populist critic. It also ties to the Hassabis FINRA-style proposal already in finra_proposals.csv.
3. The transmission of Sacks's METR sentence into East Asian and market press with no funder ever named (PR01–PR07, ITmedia, Digital Today, Eastern Herald, Tech Insider) — nine outlets now carry "intertwined with Anthropic's investors and staff"; none identifies an investor, a staff tie, or a dollar figure, and none records a METR reply. The only specifics in circulation are unsourced HN comments (PR11, PR12) that conflate Coefficient/Open Philanthropy family ties, Cotra's employment history, ARC's ~$4.5M, and an equity-stake claim that was challenged in-thread and not sourced. For the infographic, the honest line is: the claim spread without evidence attached, and METR did not answer it.

## 4. Corrections and cautions for the existing rows
- IF44's "no response located" stands and can be re-dated to 2026-09-14 07:35 UTC with the search terms above.
- Aggregators (GitHub digest #152, AI Weekly, Free Press Journal) date the Benton/Engels move to "Sep 12"; NBC's original is Sep 10 22:33 UTC (rcna597086, saved). Sayer Ji says "September 2." Use NBC.
- Eastern Herald, Winzheng and Karmactive overstate the essay ("granting METR", "selected METR", "Signs METR"); do not cite them for the access claim.
- ITBB's "Pew Charitable Trusts" as a METR donor is not in our 990/ledger work; treat as unverified.
- crypto.news Sep 13 11:46 UTC (CX01) is 14 minutes pre-window but has the cleanest negative: "Neither company had publicly accepted Sacks' description as of Sept. 13" and OpenAI "supplied no implementation date, evaluator name or access terms."

## 5. Open gaps
- NYT Sep 13 "silicon-valley-ai-slowdown" and WSJ "The Great AI Slowdown": unread; both listed under the Sacks story. Kevin may be able to open the NYT gift link in a browser (unlocked_article_code=1.BFE.XpCg.V6X7lUaR9uFt).
- Bloomberg Sep 14 "AI Bosses Risk Clash" body: unread beyond the lede.
- Neowin and Forbes/Majic: unread.
- Semafor and Axios published nothing new on METR in window (their Sep 13 items are IF30/IF26); Reuters/FT/Verge/Wired/Politico are not searchable by the tool's domain filter, so coverage of those relied on Techmeme's index, which lists FT (Trump; Anthropic profitability) and WSJ/NYT items but no FT/Reuters item on Sacks-METR.
