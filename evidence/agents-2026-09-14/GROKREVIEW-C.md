# GROKREVIEW-C — review of Grok lanes G17, G18, G28, G33, G34 (2026-09-14)

Scope: research/grok-out/G17-farhi.csv (36 rows), G18-investigation-watch.csv (16 rows + 45-line header), G28-anthropic-governance.csv (63 rows), G33-metr-people.csv (33 rows), G34-embedded-evaluators.csv (14 rows), read in full against their briefs. Every candidate finding was grepped against donor_rule.csv, independence_fight.csv, hf_case.csv, staff_origins.csv, board.csv, arrivals.csv, sep9.csv, christiano.csv, and (because the greps led there) evaluators.csv, lab_statements.csv, evals.csv, redwood.csv, money_flows.csv, stakes.csv, pay.csv, budget.csv, finra_proposals.csv, press_sweep.csv, transmission.csv, officials_mentions.csv, x-metr-*-grok-*.csv, WATCHLIST.md.

Row citation convention (the lane CSVs have no row_id column): `G17-B/about` = lane G17, task B, row identified by url/handle; X rows by status id. Lane fetch times: G17 11:49Z, G18 11:52Z, G28 12:09Z, G33 12:08Z, G34 12:13Z (all 2026-09-14). No fetching was done by this review; no file other than this one was written.

Figure ids per README: 10c Christiano's hats; 10d evaluator's board; 10f same-day three moves; 10g who gets ordained; 10h revolving door; 10i ask the regulator; 10k same donors both sides; 10m the subcontractor; 10n independence fight; 10o the candidates; 10s the rule and the donor; 10t security revolt; 10u METR grades itself; 10v where the sentence went; 10w what METR pays; 10x terms of the first investigation; 10y accuser's ledger; 10z/10aa stakes.

---

## 1. NEW FACTS (verified-looking; not already in the research CSVs)

Ordered by how much they change a figure. "Verified-looking" = live issuer page, PDF, or the person's own post, re-fetched by the lane with a URL and UTC time. Secondary press is marked.

### 1.1 Farhi (G17)

**NF-01. Farhi's own words to WIRED, and the $3,000 super-PAC gift that puts him in a federal filing.**
- G17-A/wired (row 2), 2026-07-15, David Farhi (statement to WIRED, Maxwell Zeff), https://www.wired.com/story/openai-employees-donations-guardrails-alliance-leading-the-future/
- Quote: "As a leader of AI research at OpenAI for many years, it became abundantly clear to me that AI is going to present our world with both unprecedented opportunities and challenges," Farhi said in a statement to WIRED.
- Also G17-A/wired (row 1), same URL: "David Farhi, a former OpenAI research manager who left the company last summer after seven years, donated $3,000 to the super PAC and will appear in the group's July filing."
- Existing: DR36 records WIRED's departure claim only. Neither Farhi's own statement nor the Guardrails Alliance $3,000 / "July filing" sentence is in any CSV (grep "Guardrails Alliance": 0 hits).
- Changes: 10s (the rule and the donor) footnote and DR36: Farhi's only known first-person statement describes his OpenAI role in the past ("for many years") but states no departure date or current employer. The "July filing" sentence is the route to a primary record (see LEAD-01): FEC Schedule A itemizations carry the contributor's self-reported employer and occupation on the contribution date.

**NF-02. LinkedIn public card still headlines "David Farhi - OpenAI" on 2026-09-14.**
- G17-A/linkedin, 2026-09-14, https://www.linkedin.com/in/david-farhi-13824175, page title "David Farhi - OpenAI | LinkedIn"; Mountain View; Harvard 2010-2016; experience titles and OpenAI dates login-walled.
- Existing: DR26 covers the CHM profile only.
- Changes: DR-row candidate (DR37) beside DR26: a second public self-presentation still reading "OpenAI" fourteen months after the WIRED-reported departure. Same evidentiary class as CHM (stale-or-current, unresolved); belongs in the 10s "what the record shows" list, not as proof of employment.

**NF-03. Live about/donate pages unchanged vs the Sep 13 baseline (supporter names, employee-ban sentence).**
- G17-C/about and G17-C/donate, 2026-09-14 11:49Z; page_changed = no on both; donate carries the ban sentence but no supporter list.
- Existing: DR34 sweep ends 2026-09-13. This extends it one day. Minor; log as DR34 checked_utc update.

### 1.2 The investigation since Sep 9 (G18, G28, G33)

**NF-04. Anthropic pre-announced the METR review on Jul 30 and Aug 31 — with a different access scope.**
- G28-B/investigating-incidents, 2026-07-30, Anthropic, https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals
- Quote: "We are also in dialogue with METR, an independent AI evaluation organization, to conduct a third-party review, including access to all transcripts and sampling access to the relevant models."
- G28-B/improving-alignment, 2026-08-31, Anthropic, https://www.anthropic.com/news/improving-alignment-security-efforts
- Quote: "We are conducting an in-depth analysis of both incidents. We are also planning to work with METR for an independent review. We want to ensure both studies are thorough, and will share more in the coming weeks."
- Existing: lab_statements.csv has L20 (Sep 9) only; evals.csv E38 is Sep 9; sep9.csv starts Sep 9 00:04. Grep on both URLs and "in dialogue with METR": 0 hits.
- Changes: 10f (same-day three moves) and 10x (terms of the first investigation). The Sep 9 agreement had a six-week public runway; "same day" is true of the announcement, not the engagement. And the Jul 30 offer named "sampling access to the relevant models"; the Sep 9 page (HF90-92, IF01) names transcripts and employees but not model sampling. Whether sampling access survived into the signed terms is a concrete question for METR's terms-of-engagement report (LEAD-08). New lab_statements rows L21-L22.

**NF-05. Anthropic's written conflict-of-interest standard for external reviewers (RSP v3.4 §3.6.1, §3.6.3).**
- G28-C/rsp-3.6.1 (three rows), 2026-07-08, Anthropic RSP v3.4 PDF, https://cdn.sanity.io/files/4zrzovbb/website/0bacdc8440ea96e62a8766d99ebe1d4eea6d5f3a.pdf
- Quote (§3.6.1): "Do not have conflicts of interest with respect to Anthropic. At a minimum, a reviewing organization itself may not have a financial interest in Anthropic; and the individuals involved in conducting the review, as well as anyone above them in the reporting chain within their organization, may not hav[e ...]" (truncated at 300 by the lane; note field adds: "In selecting external reviewers, we will consult with the Board and obtain the approval of the LTBT.")
- Quote (adjacent bullet): "Have reputational and other incentives making them likely to be candid ... external review parties should not be teams whose revenue, reputation and success depend entirely on Anthropic"
- Quote (§3.6.3): reviewers "will not be restricted in what they can publish" beyond confidential-information obligations.
- Existing: lab_statements L17 records only that v3.x has 0 METR hits. No CSV holds the §3.6 text (grep "financial interest in Anthropic", "external reviewer", "3.6.1": 0 hits).
- Changes: 10x and 10u. This is the lab-side counterpart to METR's AEF-1 requirement 2.3 (published COI policy, answered "No" per 10u): Anthropic's own rule bars a financial interest in Anthropic for the reviewing org, the reviewers, and their reporting chain, and requires LTBT approval of the reviewer selection. Two direct tests follow (LEAD-03): was the Sep 9 METR engagement selected under §3.6 with LTBT approval, and do any investigation-team members (ex-Anthropic hires; Redwood subcontractors) hold Anthropic equity. Also feeds 10n/10y: Sacks's "intertwined with Anthropic's investors" (OM01) is a claim about METR's funders, which §3.6.1 does not reach (it runs reviewer-to-Anthropic, not Anthropic-investor-to-reviewer).

**NF-06. Greenblatt states the investigation's scope is METR's Jul 28 methodology post.**
- G18-A id 2098802371715592261, 2026-09-12T15:54:13Z, @RyanGreenblatt, https://x.com/RyanGreenblatt/status/2098802371715592261
- Quote: "The scope of the investigation is: https://metr.org/blog/2026-07-28-investigating-ai-propensities-after-incidents/"
- Existing: the id sits in x-metr-2-grok-2026-09-13.csv row 33 but has no independence_fight/hf_case row; sep9 D17 has METR's own "cover all of the questions" post. 
- Changes: 10x: a named investigator (Redwood chief scientist, subcontracted; IF54) defines scope by reference to the Jul 28 post (updated Sep 5, i.e. four days before the agreement). Pair with D17. HF-row candidate under "terms".

**NF-07. METR's president: public declarations of access arrangements are "sometimes the limiting factor"; hiring authority constrained.**
- G33-E/painter, 2026-09-09T16:41:02Z, Chris Painter (President), https://x.com/ChrisPainterYup/status/2097726989096329470, 473 views
- Quote: "The ambition of proposals we put forward, across our work in aggregate (if not misalignment investigations specifically), is primarily constrained by staff capacity. Clarity/formality/public declarations of access or independent oversight arrangements is sometimes the limiting factor"
- Existing: x-metr-grok-2026-09-13.csv row 34 holds the text; no IF row (sep9 D15 is a different Painter post the same morning).
- Changes: 10x / 10n: METR's own officer, hours before the Anthropic announcement, naming formal public access declarations as a bottleneck. IF-row candidate.

**NF-08. Embedded-investigation team size, from METR's own postings: "1-4 other METR staff".**
- G33-D/cyberforensics, live 2026-09-14, https://jobs.lever.co/metr/b1a2f73f-f927-4f8b-b1b3-b2e57604b5fd
- Quote: "Incident investigation: You'll be embedded in a frontier AI lab for up to several weeks at a time, likely alongside 1-4 other METR staff."
- Same sentence in G33-D/embedded-assessments (https://jobs.lever.co/metr/69792e29-e72c-44a2-8305-82cb40ab17c5). G33-D/security-engineering adds: "Security at METR is becoming its own dedicated team, and you would be one of its first hires. ... We also may pursue incident investigations embedded in frontier labs".
- Existing: pay.csv PY49-PY57 hold the salary ranges from the same postings but not the team-size or security-team sentences (grep "1-4 other": 0 hits).
- Changes: 10x and 10m: METR's own stated embedded team is 2-5 people; matches Logan Graham's "The 3 METR investigators" (IF71) and Redwood's "several staff" subcontract (IF15). 10t: the dedicated security team is being formed now (posting live since at least Aug 1 per PY61, so it predates the Sep 12-13 infosec critique rather than answering it).

**NF-09. Benton's own record of his Anthropic role.**
- G33-C/benton-substack, 2026-09-11, Joe Benton, https://jbenton1.substack.com/p/why-i-left-anthropics-safety-team
- Quote: "Two weeks ago, I left the safety team at Anthropic. I will soon be joining METR, an independent organization that evaluates how safe AI companies' systems are."
- Note field, from joejbenton.github.io/research: "I used to manage the Scalable Oversight team at Anthropic" and "research lead for the Anthropic Fellows Program".
- Existing: IF06/AR09 hold the X post; S13 says "led a safety research team" sourced to NBC. The Substack URL and the team/programme names are new.
- Changes: 10h (revolving door) S13: replace NBC paraphrase with his own description; and note "will soon be joining" (Sep 11) — he had not started (see CONTRADICTION C-05).

### 1.3 Evaluator badges and responses (G18, G34)

**NF-10. Apollo Research's head of research asks for embedded-evaluator access.**
- G34-B/meinke, 2026-09-14T10:08:23Z, Alex Meinke (Head of Research, Apollo Research), https://x.com/AlexMeinke/status/2099440112249528501, 51 views
- Quote: "AI developers should be able to confidently and credibly answer some pretty basic questions such as: 'Did your agents ever attempt to undermine their own safety training?' Apollo is trying to answer this question. Embedded Evaluator access would definitely make it substantially easier"
- Existing: no Apollo response in independence_fight.csv or finra_proposals.csv (grep "meinke", "apollo" in those files: 0 hits); evaluators.csv EV02 has Apollo's profile only.
- Changes: 10o (the candidates): Apollo is the only listed evaluator org besides Hugging Face (IF13/IF16) with an officer publicly asking in; METR, Redwood, FAR.AI, Transluce, Epoch, UK AISI, CAISI, AIUC, Halcyon, LMArena all silent on the proposal as of 12:13Z (G34-B none-found row). Low reach (51 views) — cite as an org-officer statement, not as public discourse.

**NF-11. Sriram Krishnan: evaluator funding should not come from the existing ecosystem "including Coefficient"; Coefficient's CEO replies with Tailwind.**
- G34-D/sriramk note field: follow-up id 2098855574578274779 (21,369 views): "says funding should not come from existing ecosystem sources including Coefficient"; and Alexander Berger (Coefficient Giving CEO) id 2098854995785560090 (18,975 views) quote-posts Sriram "pointing to Tailwind".
- Existing: IF18 holds Sriram's first post (2098851577050046478) only; grep for either follow-up id or "Alexander Berger" in independence_fight/money_flows: 0 hits.
- Caveat: the lane recorded both as paraphrase in a note, not verbatim text. Treat as a lead until fetched (NOT PULLED NP-15).
- Changes if confirmed: 10o and 10f Tailwind footnote: a former White House AI adviser naming Coefficient as a funder evaluators should not depend on, answered within minutes by Coefficient's CEO offering Coefficient money (Tailwind, M123). Also 10n.

**NF-12. No later Anthropic/Amodei clarification on who qualifies as an embedded evaluator, how they are paid, or conflict rules.**
- G34-A/none-found, checked 2026-09-14T12:13:02Z: from:DarioAmodei since Sep 12 = essay post only; from:AnthropicAI (evaluator OR METR OR embedded OR pace) = 0; anthropic.com/news latest Aug 31; web search: none.
- Existing: IF09 summarises the essay; no CSV row records the absence of pay/eligibility/COI terms.
- Changes: 10g / 10x: the essay's only COI-adjacent terms are editorial (publish without Anthropic editorial control; narrow redactions; reviewers may say a redaction mattered — G28-C/pace-the-frontier rows). Who pays the badge-holders is unstated. Negative finding worth an IF row so the figure can say "unstated" with a checked time.

**NF-13. Politico: California has enacted an outside-evaluator registry with ethics rules, and an IVO-qualification law.**
- G34-C/politico, 2026-09-12T22:02Z, Politico (Chase DiFeliciantonio), https://www.politico.com/news/2026/09/12/sam-altman-openai-ipo-01073565 (secondary press)
- Quote: "Notably, California Gov. Gavin Newsom recently signed a measure into law that would create a state registry and ethics rules for outside AI evaluators. A separate law he signed would task the state with establishing criteria for and checking the qualifications of so-called Independent Verification Organizations and their expertise in assessing the risks posed by AI systems."
- Existing: finra_proposals.csv F10 is the federal FRONTIER Act (IVOs); F14/IF03/sep9 D12 record OpenAI on Sep 9 "backing" CA SB 813 and AB 1405 — as bills. No CSV records either as signed (grep "Newsom", "registry": 0 relevant hits).
- Changes: 10i (ask the regulator) and finra_proposals.csv: a state "registry and ethics rules for outside AI evaluators" is an ordination mechanism already in law, in METR's home state. Bill numbers and signing dates are not in the lane (LEAD-05). Timeline tension with IF03 in C-08.

### 1.4 Anthropic governance ties (G28)

**NF-14. Jaan Tallinn describes himself as an Anthropic board observer who declined a board seat.**
- G28-A/tallinn, statement Jan 2026 (Äripäeva raadio) reported 2026-02-22, Postimees Majandus, https://majandus.postimees.ee/8418603/tabel-jaan-tallinna-osalusega-anthropicu-vaartus-on-nuud-enam-kui-kolmandik-triljonit (secondary press, Estonian)
- Quote: "Samas on Tallinnal ilmselt piisavalt suur osalus, et ta võiks olla ka ettevõtte nõukogu liige, aga on nõukogu vaatleja. «Ma nimelt ei tahtnud nõukogu liikmeks astuda, kuna mu põhitöö on ikka AI-riskide vähendamine, seetõttu ei tahtnud ma olla nii tugevalt seotud ühe sellise juhtiva ettevõttega,» ütl[es]" (gloss: his stake is apparently large enough for a board seat, but he is a board observer; he did not want to be a board member because his main work is reducing AI risk).
- Existing: stakes.csv ST38-ST39 record Tallinn as Series A lead and Series B participant; no CSV records an observer seat (grep "observer": only Christiano's OpenAI seat C11).
- Changes: 10z/10aa stake rows and 10k: the Series A lead sits in Anthropic board meetings as an observer while funding (via SFF/SF DAF: money_flows, LawZero donors in G33-B/bengio) the orbit METR's advisors and grantors share. Add to board-ties or stakes as a sourced row; issuer pages list no observers (G28-A/observers none-found), so this stays press-attributed to Tallinn's own radio remarks.

**NF-15. Luke Muehlhauser was an Anthropic director until 2024-05-29, leaving "to focus on his work at Open Philanthropy".**
- G28-A/muehlhauser, 2024-05-29, Anthropic, https://www.anthropic.com/news/jay-kreps-appointed-to-board-of-directors
- Quote: "Separately, Luke Muehlhauser has decided to step down from his Board role to focus on his work at Open Philanthropy."
- Existing: IF134 records Muehlhauser (Coefficient managing director, AI governance) urging people to apply to METR on Sep 12; M121 records him as grantmaker on the $68M Epoch renewal. His Anthropic board seat is in no CSV.
- Changes: 10k (same donors both sides): the Coefficient officer publicly recruiting for METR sat on Anthropic's board until 16 months ago. IF134 note + board-ties row.

**NF-16. Anthropic's current board and LTBT roster carries no METR/ARC/Redwood/Coefficient/SFF/Constellation role; observers are not published; Kreps has silently dropped off.**
- G28-A/company, 2026-09-14, https://www.anthropic.com/company: Board = Dario Amodei, Daniela Amodei, Yasmin Razavi, Reed Hastings, Chris Liddell, Vas Narasimhan; LTBT = Neil Buddy Shah, Richard Fontaine, Ben Bernanke. Jay Kreps (LTBT-appointed 2024-05-29; still listed 2026-04-14) absent with no departure post. Cuéllar left the LTBT 2026-08-04 to become Chief Global Affairs Officer. Matheny left Dec 2023 "to preempt any potential conflicts of interest ... with RAND" (RAND = METR's Canary partner, EV18/M124).
- Existing: only Christiano's LTBT seat (C05) is on file. None of the current names appear anywhere.
- Changes: 10y (accuser's ledger) and 10n: a sourced negative for the "intertwined ... staff" half of Sacks's sentence at the governance level — the tie runs through former seats (Christiano, Muehlhauser) and investors/observer (Tallinn), not through any current director or trustee. Also relevant to NF-05: the LTBT that must approve external reviewers is Shah, Fontaine, Bernanke.

**NF-17. Karnofsky in his own words: role, family equity, the RSP's METR origin, and the Jan 2025 start.**
- G28-D (five rows), recorded 2025-07-25/28, published 2025-10-30, 80,000 Hours #226, https://80000hours.org/podcast/episodes/holden-karnofsky-concrete-ai-safety-frontier-ai-companies/
  - "My title is 'member of technical staff' ... I report to the chief science officer, Jared [Kaplan], and my job is basically to advise the company on preparing for risks from advanced AI."
  - "One is I'm married to the president and cofounder of Anthropic. I also work there. I'm not exactly a neutral party here."
  - "So back in 2023, I was talking with Paul Christiano and the folks at METR and feeling that there was some energy at AI companies to be seen as responsible and safe and to make some voluntary commitments"
  - "This financial thing is completely reasonable to treat as an extra big thing — especially for me, because my wife's a cofounder and there's a lot of equity."
  - "I'm connected by family and work at Anthropic. So not everything is great to be getting money from Open Philanthropy — that can create a real and perceived conflict of interest, which I think is going away with time as I'm not there now."
- G28-D/lesswrong, 2026-02-24, https://www.lesswrong.com/posts/HzKuzrKfaDJvQqmjh/responsible-scaling-policy-v3: "I went to Anthropic full-time in January of 2025 with the RSP as my primary focus." (recovered from search snippets; full page 429 — NP-11)
- G28-D/greaterwrong, 2026-03-12 comment: "(Some more detailed suggested language for such a commitment is provided by METR, a nonprofit that works on AI evaluations.)"
- Existing: board.csv B12 and staff_origins S42/S44 give the advisor dates and Jan 2025 move from Wayback/Wikipedia; no Karnofsky quote is on file.
- Changes: 10h (S44 gets a first-person date), 10c (RSP origin: Christiano + "the folks at METR" + Karnofsky, 2023), 10k. Synthesis to flag, not assert: the RSP v3 line that Karnofsky says he "led the way in developing" is the document carrying the §3.6.1 external-reviewer COI rule (NF-05); a former METR advisor wrote the standard under which METR would be selected. Whether §3.6 was in v3.0 or added later needs the v3.0 PDF (LEAD-03).

**NF-18. RSP v2.1 and v2.2 keep the "framework introduced by ... METR" credit; the 2024 third-party-testing policy page never names METR.**
- G28-B/rsp-2.1 (2025-03-31) and /rsp-2.2 (2025-05-14): same sentence as L07. G28-B/third-party-testing (2024-03-25): "the retrieved text does not contain the string METR" (names Gryphon Scientific).
- Existing: L07 (v2.0) and L17 (v3.x zero hits). v2.1/v2.2 and the third-party-testing negative are new but small.
- Changes: 10b/L-rows: the METR credit lived Oct 2024 - May 2025 across three versions and vanished at v3.0 (Apr 2026). Minor.

### 1.5 METR people (G33)

**NF-19. AR11 advisor identified: Chase Hasbrouck, Army Cyber Command, retiring Oct 2026; not on the live team page.**
- G33-B/hasbrouck and G33-C/hasbrouck-linkedin, 2026-09-13T21:00:28Z (X) and ~21:08Z (LinkedIn public post), https://x.com/ChaseHasbrouck/status/2099241828126220588 ; https://www.linkedin.com/posts/chasehasbrouck_after-a-20-year-career-in-the-us-army-activity-7505007583167041536-rwu0
- Quote: "After a 20-year career in the U.S. Army, most recently leading digital forensics and malware analysis at Army Cyber Command, I'm excited to join @METR_Evals as an advisor."
- X bio at fetch: "U.S. Army Cyber officer, retiring Oct 2026." Not listed under Advisors on metr.org/about at 12:08Z (G33-A).
- Existing: arrivals.csv AR11 has the post text (truncated) and handle; board.csv has no row; the brief itself did not have the name.
- Changes: 10d (board/advisors) B18 candidate; 10h: first government-forensics arrival, and the first advisor announced by the person before the issuer page lists him. No lab/funder tie found on the announcement (G33-B tie_type "none found").

**NF-20. Gleave also sits on the boards of the Safe AI Forum and the London Initiative for Safe AI; AIUC's team page says its team "spent time at Anthropic".**
- G33-B/gleave note: live gleave.me: "board member of the Safe AI Forum, the London Initiative for Safe AI and METR".
- G33-B/dattani note: live aiuc.com/team (published 2026-09-11 01:04Z): "Our team ... spent time at Anthropic, McKinsey insurance, METR, and Center for AI Safety"; investors include "an Anthropic co-founder".
- Existing: B05/B17 (Gleave) list FAR.AI, DeepMind, Coefficient, AISF; no SAIF/LISA seats. B06/B15/M132 (Dattani) name Ben Mann as investor; the "spent time at Anthropic" team line is new.
- Changes: 10d minor additions. The AIUC line means Dattani's current company has ex-Anthropic staff and an Anthropic co-founder investor — a "reporting chain" question under NF-05 only if Dattani were involved in a review, which nothing shows.

**NF-21. Bengio's LawZero lists NVIDIA as a supporter (15 Jul 2026) alongside Coefficient and the SF DAF.**
- G33-B/bengio note, live lawzero.org/en. Existing B09 lists Tallinn, Schmidt, Open Phil, FLI, SVCF. NVIDIA is new; minor for 10d.

### 1.6 Items checked and found already on file (no action)
Anthropic Sep 9 post/page (IF01, HF90-92, L20); METR's future-tense ToE promise (IF02, D09, D17); Barnes recruiting (IF05); Benton Sep 11 (IF06/AR09); Amodei post and essay (IF08/IF09); Redwood subcontract (IF15/RW36); Greenblatt on team (IF54); Logan Graham "3 investigators" and "thousand METRs" (IF71/IF69); Drake Thomas recruiting (IF70); Altman/Hassabis/Nadella (IF17/IF20/IF129); Musk peer-review (IF65); Delangue/Wolf (IF13/IF16/EV15); Sacks (OM01/IF28/SL24); NYT Huang-Isaac (IF140/PR43/TR16); Speaker Johnson (IF66); Sriram's first post (IF18); Engels (IF50/AR07/AR10/S14); Kwa (AR04/S46); Mascorro stale bio (B16); Dattani/AIUC/Halcyon (B06/B15/M132/M133); Radford (B07); Lever ranges (PY49-PY57); BI 35-person / $503k (G08/G09/PY69); METR Sep 13 blog footnotes (HF81-83/IF149/RW59); RSP v1.0/v2.0 credits (L03/L07); v3.x no METR (L17); risk-report pilot reviews (L18/L19/E25/E26); Mythos/Fable system cards (E27/E36); Claude 3.5 addenda (E03/E06); Christiano LTBT (C05); Karnofsky advisor dates (B12/S42/S44); Painter to Hwang (IF64).

---

## 2. LEADS (ranked)

**LEAD-01. FEC Schedule A for Guardrails Alliance's July 2026 filing — Farhi's self-reported employer on a federal record.** WIRED (NF-01) says he "will appear in the group's July filing." Itemized receipts list employer and occupation as of the gift. This is the primary confirmation WATCHLIST asks for on DR36 and would settle the 10s overlap question with a dated self-declaration (either "OpenAI" or something else, as of June/July 2026). Route in NP-02.

**LEAD-02. Chris Painter's "conflicts of interest" reply (id 2099364498406604876).** G18's header and G34-B both mention it (in the Tim Hwang thread, after IF64) and neither lane captured its text. It is the only known METR-officer post using the phrase during the fight. Route in NP-09.

**LEAD-03. Test the Sep 9 engagement against Anthropic's own RSP §3.6 (NF-05).** Three concrete questions: (a) was METR selected as an RSP "external reviewer" with LTBT approval (Shah/Fontaine/Bernanke), or is the Sep 9 agreement outside §3.6; (b) does any member of the investigation team hold Anthropic equity — Benton left Anthropic ~Aug 28 (vested equity is typical) and is joining "embedded assessment"; Redwood subcontractors; (c) was §3.6.1 present in RSP v3.0 (Feb 2026, Karnofsky-led) or added in v3.1-3.4. Sources: RSP v3.0 PDF from anthropic.com/responsible-scaling-policy history; METR's forthcoming ToE (~Nov 4); direct question to METR/Anthropic press. Feeds 10x, 10u, 10c.

**LEAD-04. Sriram's "not Coefficient" follow-up and Berger's Tailwind reply, verbatim (NF-11).** A named exchange between a former White House adviser and Coefficient's CEO on who should fund evaluators, both above 18k views, currently paraphrased only. Route in NP-15. Feeds 10o/10f.

**LEAD-05. The California evaluator-registry law (NF-13): bill numbers, signing date, text.** Candidates are SB 813 and AB 1405 (IF03/F14). leginfo.legislature.ca.gov → search bill → "Status" tab for "Chaptered" date, and the chaptered text for COI/funding-disclosure requirements on registered evaluators. Check whether Michael Chen (ex-METR policy, now Cal OES AI science adviser, S47) is in the implementing office. Feeds 10i and resolves C-08.

**LEAD-06. Anthropic's Jul 30 "sampling access to the relevant models" vs the Sep 9 terms (NF-04).** If the signed terms dropped model sampling, that is a scope narrowing between offer and agreement; if kept, the Sep 9 page under-describes access. Only METR's ToE report can settle it; log the question now for the ~Nov 4 comparison against HF01-HF21.

**LEAD-07. Tallinn's board-observer seat in English or from the original audio (NF-14).** Äripäeva raadio, early Jan 2026; Postimees 2026-02-22 is the only recovered print. An English confirmation (interview, Metaplanet page, any S-1 exhibit listing observer rights) would let 10z/10aa cite it without an Estonian gloss.

**LEAD-08. Benton's status and role on the Anthropic investigation.** His Sep 2 post says "embedded assessment of AI risks"; Sep 11 says "independent evaluations"; both say he has not started. If he is staffed on the Anthropic investigation, he would be investigating the employer he left three weeks earlier. Watch metr.org/about and the ToE team list; ask METR. Feeds 10h/10x.

**LEAD-09. Jay Kreps's departure and the LTBT-majority claim (NF-16).** The Apr 14 2026 post claimed a Trust-appointed majority with seven directors; the live page lists six without Kreps and no departure post. Whether Trust-appointed directors are still a majority bears on who approves external reviewers. Route: anthropic.com/news search "board"; Confluent filings/press; Wayback of /company between Apr 14 and Sep 14.

**LEAD-10. Microsoft "MAI Code of Conduct" (Nadella said it would publish 2026-09-14 for consultation; G18 header).** May name evaluator organisations or access terms for Microsoft's models. Route in NP-10.

**LEAD-11. Muehlhauser's Anthropic board tenure dates (NF-15).** Start date is not in the lane (only the May 2024 exit). The 2023 LTBT post or the 2021-23 Anthropic news archive should give it; then 10k can draw "Anthropic director → Coefficient MD → 'apply to METR'" with dates.

**LEAD-12. Wayback body diff of the Sep 9 Anthropic page (17 captures, changing digests; G28-B/cdx).** The lane could not render the SPA. Route in NP-12. If the METR paragraph changed after publication, 10x should say so.

**LEAD-13. Hasbrouck (NF-19): whether he takes the seat before his October retirement, and whether metr.org adds him.** A serving Army officer advising a private evaluator of lab incidents is a disclosure question in its own right; his bio says "All posts personal, not official." Watch metr.org/about; his own posts.

**LEAD-14. Jack Clark's quote-post of the essay (G18-A id 2098780956966764691, 116,764 views).** Not on file; does not name METR; low priority. Only worth an IF row if 10n adds a lab-cofounder panel.

---

## 3. NOT PULLED (rows marked none found / blocked / paywalled / 403 / login where a source plausibly exists)

Each item: lane row → manual route, or "genuinely absent".

**NP-01. G17-A/linkedin — Farhi's OpenAI end date (login wall).** Route: log in to LinkedIn, open https://www.linkedin.com/in/david-farhi-13824175, scroll to Experience; the OpenAI entry shows a date range ("2018 – Present" or "2018 – 2025"). Save the page as PDF with the visible timestamp. This is self-maintained and may be stale, so it complements rather than replaces NP-02.

**NP-02. G17-B/990 and G17 header "FEC ... browser not supported" — Farhi's METR amount vs his federal filing.** METR amount: genuinely absent (Schedule B contributor names/amounts are legally redacted in public copies; the annual report text has no Farhi). Federal filing: https://www.fec.gov/data/receipts/individual-contributions/?contributor_name=farhi%2C+david&two_year_transaction_period=2026 in a browser; if empty, find the committee first at https://www.fec.gov/data/committees/?q=guardrails+alliance, open its "Raising" tab, filter itemized receipts by name "Farhi", and read the Employer / Occupation columns on the July 2026 report line. Also check the "Leading the Future" committee named in WIRED's headline.

**NP-03. G17 header — OpenReview profile (browser verification).** Route: open https://openreview.net/profile?id=~David_Farhi1 in a normal browser; the Career & Education block lists "OpenAI — Researcher — 2018 – Present" per the search snippet. Self-maintained; date it.

**NP-04. G17 header — github.com/dfarhi ("You can't perform that action at this time").** Route: open in browser; the profile "company" field and the contribution graph give a rough activity signal. Low value.

**NP-05. G17-A/forum, /personal_site, /x — Farhi's own posts, site, handle.** Genuinely absent as far as the lane could see: no personal site, no matching X handle, EA Forum search empty, LessWrong search behind a Vercel checkpoint. Manual LessWrong route: https://www.lesswrong.com/search?query=David%20Farhi in a browser (the checkpoint clears with JS). Expect nothing.

**NP-06. G17-B/annual_report — METR 2024 annual report PDF (>10 MB cap).** Not needed: research/metr-2024-annual-report.txt already exists and has no "Farhi". Genuinely absent for an amount.

**NP-07. G18-B and G28-C — METR's terms of engagement / interim report.** Genuinely absent at fetch (metr.org/blog latest 2026-08-31; substack latest 2026-08-14; METR's Sep 9 post is future-tense). Manual watch: https://metr.org/blog and https://metr.substack.com/archive; WATCHLIST already dates it ~2026-11-04.

**NP-08. G18-C — openai.com evaluator naming for the Sep 12 commitment.** Genuinely absent at fetch (IF45 concurs). Manual: https://openai.com/news in a browser, filter "Safety"; and Altman's "more to share soon" thread replies at https://x.com/sama/status/2098811563415150910.

**NP-09. G18 header / G33-E / G34-B — Painter's conflicts-of-interest reply, id 2099364498406604876 (mentioned three times, never captured).** Route: https://x.com/ChrisPainterYup/status/2099364498406604876 in a browser, or https://api.fxtwitter.com/i/status/2099364498406604876 (JSON; the project's usual refetch path). Also pull the parent Hwang post it replies to.

**NP-10. G18 header — Microsoft MAI Code of Conduct (Nadella: publishes 2026-09-14 for consultation).** Route: https://blogs.microsoft.com/ and https://microsoft.ai/news in a browser, search "Code of Conduct"; or Nadella's own thread https://x.com/satyanadella/status/2099220712024408084 for the link. Check for evaluator-org names or access terms.

**NP-11. G28-D/lesswrong — Karnofsky's RSP v3 post (Vercel 429; quotes from search snippets).** Route: https://www.lesswrong.com/posts/HzKuzrKfaDJvQqmjh/responsible-scaling-policy-v3 in a browser, or the mirror https://www.greaterwrong.com/posts/HzKuzrKfaDJvQqmjh (which the lane reached for the Mar 12 comment). Verify the three quoted sentences verbatim before any figure cites them.

**NP-12. G28-B/cdx — Wayback body diff of the Sep 9 Anthropic page (id_ snapshots are JS shells).** Route: open the rendered (non-id_) captures in a browser: https://web.archive.org/web/20260909190507/https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents and https://web.archive.org/web/20260913181025/https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents ; select-all/copy the article text from each and diff. Alternatively https://web.archive.org/web/changes/https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents shows per-capture change highlights.

**NP-13. G28-A/observers — Anthropic board observers.** Genuinely absent from issuer pages. Alternatives: the Anthropic S-1 when public (director and 5%-holder tables; observer rights sometimes appear in investor-agreement exhibits) — already on WATCHLIST; the Postimees article for Tallinn (NF-14) is the only named observer.

**NP-14. G28-D — @HoldenKarnofsky X and any statement on Open Phil's Anthropic stake.** Genuinely absent: protected, dormant account (sep9 D16 agrees); no first-person statement on the stake in the recovered transcript.

**NP-15. G34-D/sriramk note — Sriram follow-up 2098855574578274779 and Berger 2098854995785560090 (paraphrased, not quoted).** Route: https://api.fxtwitter.com/i/status/2098855574578274779 and https://api.fxtwitter.com/i/status/2098854995785560090, or the X URLs under @sriramk and @albrgr. Record views at fetch.

**NP-16. G34-C — paywalled/blocked press.**
- NYT Huang/Isaac: local print capture already exists (research/press-pdfs/nyt-2026-09-13-silicon-valley-ai-slowdown.txt); nothing to do.
- NYT https://www.nytimes.com/2026/09/13/technology/anthropic-ceo-slower-ai-development.html: CAPTCHA. Route: open in a logged-in browser; Ctrl-F "METR", "Redwood", "evaluator"; save as PDF to research/press-pdfs/. (Check whether this is IF141/IF142 already read.)
- Bloomberg https://www.bloomberg.com/news/articles/2026-09-12/anthropic-ceo-says-it-s-time-to-slow-pace-of-improving-ai-models: lede only. Route: Bloomberg subscription, or https://archive.ph/ + paste the URL; Ctrl-F "METR".
- FT https://www.ft.com/content/31220b59-b0c6-401c-a146-2b7b5d138837 and https://www.ft.com/content/b3d01493-f0f5-491b-bcf8-2d414539fbe7: subscribe wall. Route: FT subscription or archive.ph; Ctrl-F "METR", "evaluator".
- The Information, Sep 12 "Altman and Musk Back Amodei's Call...": 403. Route: theinformation.com subscription; IF130 already has a Sep 13 Information item via Stoller — check whether it is the same piece.
- Vox, Andrew Prokop "The week the AI freakout went mainstream" (Sep 12): jina blocked, not paywalled. Route: https://www.vox.com/innovation in a browser, open the piece, Ctrl-F "METR".
- WSJ: no Sep 12+ evaluator piece found; IF145-IF148 (four WSJ items read) name no METR. Genuinely absent at fetch.
- Transformer / Platformer: no Sep 12+ piece at fetch. Route: https://www.transformernews.ai/archive and https://www.platformer.news/archive/ after Sep 14; Transformer's weekly usually lands Friday.

**NP-17. G33 header — LinkedIn profiles of Benton, Engels, Hasbrouck (login wall).** Route: logged-in LinkedIn search "Joe Benton Anthropic", "Josh Engels DeepMind", https://www.linkedin.com/in/chasehasbrouck; Experience blocks give start months for METR and end months for the prior lab — the dates S13/S14 lack.

**NP-18. G33-D — numeric headcount.** Genuinely absent from issuer pages. The LinkedIn company page "65 employees" is a self-affiliation count (includes contractors, alumni who have not updated, and advisors); the about-page count of 37 named staff is the issuer figure. Nothing to fetch; see C-03.

**NP-19. G18-D and G34-D — X keyword caps.** The 10-hit-per-query cap means the "none found" for officials since Sep 13 12:00Z and the >20k-view census are lower bounds. Manual route: X advanced search in a browser, `from:DavidSacks since:2026-09-13` etc., scroll fully. Not a source gap per se.

**NP-20. G28 header — Postimees body only "lede through observer quote".** Route: open the Postimees URL in a browser (may need a subscription for the table); browser-translate; the table reportedly values Tallinn's stake — relevant to 10z if it gives a share count or percentage with a source.

---

## 4. CONTRADICTIONS (with existing rows, or between lanes)

**C-01. Farhi employment: three public artefacts still say OpenAI; WIRED says he left summer 2025.** G17-A/linkedin ("David Farhi - OpenAI", 2026-09-14), G17 header OpenReview snippet ("2018 – Present"), DR26 (CHM "Technical Lead, OpenAI", live 2026-09-14) vs DR36/G17-A/wired ("left the company last summer after seven years", Jul 15 2026). All three "current" artefacts are self- or third-party-maintained profiles that are routinely stale; WIRED is attributed reporting with a Farhi statement in the same article. Not resolvable from these; LEAD-01 is the tiebreaker. Figure 10s should keep presenting both.

**C-02. @grok asserts Farhi is "a private Jane Street-linked donor" (G17-D id 2098998445365174593, 9 views).** Contradicts DR13/DR14/DR29/DR36 (OpenAI, 2018-2025) and is unsupported by any source on file; the same bot's other two replies correctly cite METR's page. Treat as an AI-generated error circulating in the Musk "Dario is right" thread, not a source. Worth one line in transmission.csv only if 10v tracks machine-generated restatements.

**C-03. Headcount: "approximately 35-person lab" (BI, budget.csv G08) vs 37 named staff on the live about page (G33-A) vs LinkedIn "Company size 11-50" and "65 employees" (G33-D note).** The issuer count (37 named, excluding 5 advisors, 1 Epoch collaborator, 1 contractor) is the defensible figure; BI's 35 is compatible; LinkedIn's 65 is a self-affiliation count. 10w/10l should cite the issuer count with the Sep 14 date rather than BI.

**C-04. Salary ceiling: BI "reach $503,000" (G09/PY69) vs live Lever $687,759 (PY49, G33-D).** Already flagged in pay.csv (PY58 shows $503,116 was the June-August posting cap). G33 confirms BI's figure was stale the day it ran (BI published Sep 11; the $687,759 posting was live by Aug 27, PY64). No change needed beyond noting BI's staleness in 10w.

**C-05. Benton's status: staff_origins S13 lists him as "Technical Staff (incident investigations)", joined 2026-09, sourced to NBC; his own Sep 11 posts say "I'll be joining" / "I will soon be joining" and the live about page does not list him (G33-A, G33-C).** Same for S14 Engels (bio says "Member of technical staff @ METR" so he has started; still not on the about page). S13 should read "announced; start date not stated; not on issuer page as of 2026-09-14". PR29 (Sayer Ji: "joined METR September 2") and PR46 ("resigned September 12") remain wrong on both dates, as press_sweep already notes.

**C-06. Views drift across pulls of the same posts.** METR_Evals 2097765966088487290: 153,629 (sep9 D09) → 229,399 (IF02/RW35) → 408,986 (G18) → 414,119 (G33). Sacks 2098973625252708460: 7,226,564 (OM01) → 8,614,153 (G34). Hasbrouck 2099241828126220588: 9,373 (AR11) → 20,478 (G33). Benton 2098480585119572317: 2,597,027 (AR09) → 2,626,038 (G33). Not contradictions, but any figure printing a view count needs the checked_utc beside it; several IF rows carry counts without one.

**C-07. NYT says critics questioned ties to "two organizations mentioned by Dr. Amodei, the nonprofit groups METR and Redwood Research" (G34-C/nyt, IF140); the essay names METR exactly once and never names Redwood (IF09; G18-C/dario-pace-the-frontier; G18 header "No other listed org ... is named").** The NYT sentence conflates the Sep 12 essay with the Sep 9 investigation (where Redwood is a subcontractor, IF15). transmission.csv TR16 should mark the Redwood attribution as the outlet's, not Amodei's.

**C-08. California evaluator laws: Politico (Sep 12) says Newsom "recently signed" a registry-and-ethics law and an IVO-criteria law (NF-13); IF03/F14/sep9 D12 (Sep 9) record OpenAI "backing" CA SB 813 and AB 1405 as if pending.** Either the bills were signed between Sep 9 and Sep 12, or they were already signed and OpenAI's Sep 9 post endorsed enacted law, or Politico's "recently" reaches back further. LEAD-05 resolves it; until then F14/IF03 should not say "pending".

**C-09. G33-B lists Mascorro's prior_or_next_org as "Independent (self-described); previously a16z partner" while metr.org/team still says "is a Partner at Andreessen Horowitz".** Already recorded as B16; G33 re-confirms the issuer page is stale as of 12:08Z. No new conflict.

**C-10. Anthropic's LTBT-majority claim vs the live roster.** Narasimhan post (2026-04-14): "Trust-appointed directors now make up a majority of the Board" with seven directors listed; live /company (2026-09-14) lists six, without Kreps (LTBT-appointed). With Kreps gone, the identified Trust-appointed directors are Hastings and Narasimhan (and Liddell only if his appointment post, which does not say who appointed him, was a Trust appointment). Internal to Anthropic's pages; matters for NF-05 (LTBT approval of reviewers). LEAD-09.

**C-11. Fontaine's LTBT start: news post dated 2025-06-07 vs LTBT page footnote "joined in May 2025" (G28-A/fontaine note).** Trivial; use the footnote date with the news URL.

**C-12. Anthropic's offered access scope narrowed or was under-described between Jul 30 and Sep 9.** Jul 30: "access to all transcripts and sampling access to the relevant models" (NF-04). Sep 9: "transcripts beyond the window ... and to Anthropic employees" (HF90/IF01) with no mention of model sampling. Not a contradiction in the strict sense (the later text may simply omit it), but 10x currently presents the Sep 9 text as the access description; it should note the earlier, broader offer and the open question (LEAD-06).

**C-13. Redwood's role differs by lane and that is correct, but easy to misread.** G18-C none-found says Redwood is "named only as METR subcontractors on the Sep 9 investigation, not as an employee-level-access evaluator for the Sep 12 commitment"; G33-C/redwood and IF15 say the same. The NYT (C-07) and several syndicated pieces (PR06, PR46) blur the two. 10m and 10g should keep the two roles in separate cells.

---

Summary counts: 21 new-fact items (NF-01 to NF-21; the strongest for figures are NF-04, NF-05, NF-11, NF-13, NF-14, NF-15, NF-17, NF-19), 14 leads, 20 not-pulled routes (of which 7 are genuinely absent), 13 contradictions (3 already recorded: C-04, C-05 partly, C-09).
