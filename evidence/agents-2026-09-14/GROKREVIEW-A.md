# GROKREVIEW-A — review of Grok lanes G14, G16, G24, G26, G27 (2026-09-14)

Scope: `research/grok-out/G14-moskovitz-vehicle.csv`, `G16-anthropic-s1.csv`, `G24-coefficient-conflict.csv`, `G26-tuna-moskovitz-words.csv`, `G27-coefficient-structure.csv`, read in full against their briefs and against `research/stakes.csv` (ST01–ST85) and `research/money_flows.csv` (M01–M124). "Verified" below means I re-fetched the source myself this run (curl, Wayback `id_` captures, Bluesky public API, X syndication endpoint, r.jina.ai); "Grok-only" means I could not re-fetch and the row rests on Grok's fetch. No file other than this one was written. No @kevinnbass post is used anywhere.

Row references: `G14/B/2025-12-18` = lane G14, task B, row dated 2025-12-18 (the CSVs have no row ids).

---

## 1. NEW FACTS

Ordered by how much each changes. "Known?" states what stakes.csv / money_flows.csv already hold.

### (a) Which vehicle holds the Anthropic stake

**NF1. Berger: the stake was donated, "and not to us".** — `G14/B/2025-12-18`; also `G27/D/2025-12-18`. VERIFIED (X syndication endpoint: text, author @albrgr, 2025-12-18T15:04:45Z, 18 likes; reply to @KKumar_ai_plans 2001618501132521902 "How much is this motivated by Open Phil's investment in Anthropic?", itself a reply to Berger's 2025-12-17 post arguing against a data-center construction ban).
- Who: Alexander Berger, CEO, Coefficient Giving.
- URL: https://x.com/albrgr/status/2001669972171661401
- Quote: "It's not. Also: 1. Open Phil never invested in Anthropic, dustin did early on. 2. He's since donated his stake (and not to us). 3. We're called Coefficient Giving now."
- Known? No (0 hits for the status id, "albrgr", or "donated his stake" in stakes/money_flows).
- What it changes: (i) It is the first Coefficient statement on where the stake went, and it is a negative: not to Coefficient. If "us" covers the Coefficient entities (Research 81-0737472, Advisors 99-2255770, Action Fund 81-2644663, Policy Fund 39-4232601), then ST83/ST84's "remaining candidates" list collapses to a donor-advised fund, a split-interest trust, or an entity not yet enumerated, and the WATCHLIST Schedule M check on the three Coefficient 990s should be expected to come back empty. (ii) "Donated" (also Forbes' word in NF5) implies a completed charitable gift, not a transfer into an LLC he still owns. Caveats: Berger's "us" may mean only the advisory organisation and not Good Ventures Foundation (which he does not speak for), but GVF is already excluded on the record by its FY2025 Schedule B (ST78). It is a 544-view reply, not a formal disclosure.

**NF2. Moskovitz: "GV is itself a beneficiary of that wave (via Anthropic...)".** — `G26/D/2026-08-26`. VERIFIED (public.api.bsky.app getPostThread; createdAt 2026-08-26T13:19:23.610Z; reply to @forthrast.com asking whether Good Ventures is "drawing down their existing pot earlier in anticipation of the new AI money", under Moskovitz's 2026-07-23 post on Coefficient's 2026 budget surge).
- Who: Dustin Moskovitz (@moskov.goodventures.org).
- URL: https://bsky.app/profile/moskov.goodventures.org/post/3mtygcpxluc2b
- Quote: "This is Good Ventures rather than new funders but it also reflects the fact that GV is itself a beneficiary of that wave (via Anthropic and a number of other investments). We happen to be a lot more liquid given a diversified portfolio than newer funders who need to wait for a big liquidity event."
- Known? No (0 hits for "bsky", the post id, or "beneficiary of that wave").
- What it changes: Moskovitz's own words place the Anthropic exposure at "GV". That conflicts on its face with ST78 (Good Ventures Foundation's FY2025 Schedule B lists no private-stock gift) unless one of these holds: (1) "GV" is shorthand for the couple's whole philanthropic complex, including donor-advised funds (Forbes: "plus more in donor-advised funds", NF3); (2) the exposure is indirect, through the FY2025 990-PF's unnamed "VENTURE CAPITAL" ($259.6M) / "PRIVATE EQUITY" ($1.34B) categories (ST79); (3) the shares reached GVF after 2025-06-30, so they would first appear on the FY2026 990-PF (Jul 2025–Jun 2026; due ~May 2027) — but Tuna dated the move to "early 2025"; (4) the holder is a GV-controlled entity that is not the Foundation. Either way it is the strongest pointer yet toward "a Good Ventures DAF" and it moves the FY2026 GVF 990-PF up the WATCHLIST. It also contradicts nothing Tuna said: she never named the vehicle.

**NF3. Forbes (US original): the couple hold donor-advised funds alongside GVF; GVF's largest holdings do not include Anthropic.** — `G26/A/2025-11-07` (two rows). VERIFIED on disk (`research/agents-2026-09-14/S11-stakes/docs/forbes-us-2025-11-07-tuna.txt`, Wayback 20251107132055).
- Who: Phoebe Liu / Forbes, reporting Tuna.
- URL: https://www.forbes.com/sites/phoebeliu/2025/11/07/cari-tuna-billionaire-open-philanthropy-facebook/ (Wayback https://web.archive.org/web/20251107132055/…)
- Quotes: "They have another $11 billion—Moskovitz's personal fortune—and approximately another $10 billion already in their private foundation, the Good Ventures Foundation, plus more in donor-advised funds." / "Most of the couple's giving flows through GVF and donor-advised funds" / "among the foundation's largest holdings are its first impact investment Impossible Foods, semiconductor companies TSMC and ASML, Nvidia, and Microsoft."
- Known? The article is ST32/ST33's source but only the vehicle sentence is quoted; the DAF sentences and the holdings list are not in any row.
- What it changes: Confirms from Tuna's own interview that DAFs exist in the structure — the one vehicle class ST83 says "would never show it". With NF1 (not Coefficient) and ST78 (not GVF), a DAF is now the leading candidate. The holdings list, given to Forbes in Nov 2025, omits Anthropic, consistent with ST78/ST79.

**NF4. Coefficient's own structure page names DAFs as grant-awarding entities and names "Coefficient Giving LLC".** — `G24/C/2026-09-14` and `G27/A/2026-09-14` (three rows); AP `G27/A/2025-11-18`. Grok-only (two lanes independently report "Live WebFetch 200" with identical text; my curl got 403 and the Wayback 2026-07 capture is JS-rendered with no body text).
- Who: Coefficient Giving governance page; Associated Press.
- URLs: https://coefficientgiving.org/governance/ ; https://apnews.com/article/open-philanthropy-cari-tuna-dustin-moskovitz-effective-altruism-0e9e93d9ed9e094f32e4070ecc5b9b2b
- Quotes: "The grants we recommend are awarded by a variety of entities, including Coefficient Giving Advisors, Inc (a 501(c)(3) public charity), donor-advised funds, the Coefficient Giving Action Fund (a 501(c)(4) social welfare organization), and the Good Ventures Foundation." / "Staff who investigate and recommend grants or investments, distribute funds to grantees, and provide operations support work at Coefficient Giving LLC." / AP: "Coefficient Giving is incorporated as a limited liability company that also has several affiliated tax-exempt nonprofit groups."
- Known? ST81 enumerates seven Moskovitz/Tuna entities; neither Coefficient Giving LLC nor any DAF is among them.
- What it changes: Two entity classes are missing from the enumeration. The LLC is not a "nonprofit vehicle" in the tax sense, but if Tuna's word was loose it is an asset-capable entity whose members are unknown. The Policy Fund is absent from Coefficient's own list of grant-awarding entities, consistent with ST84 (990-N shell).

**NF5. Forbes "True Net Worth" (Apr 2026): Moskovitz "donated" the stake; "an estimated stake of less than 0.8%".** — `G14/D/2026-04-20`. VERIFIED (Wayback https://web.archive.org/web/20260421043155/https://www.forbes.com/sites/mattdurot/2026/04/20/reranking-the-worlds-billionaires-by-wealth--and-altruism/ , fetched with `--compressed`; the live page is 403).
- Who: Matt Durot and Chase Peterson-Withorn / Forbes.
- Quote: "Dustin Moskovitz ADJUSTED NET WORTH: $35.9 bil (+$10.3 bil) RANK: #64 (vs. #316) The Asana and Facebook cofounder has been dumping shares into philanthropy for years to help fund causes such as malaria prevention and AI safety. Last year he donated his early investment in AI giant Anthropic: an estimated stake of less than 0.8% that has already skyrocketed in value amid the AI boom."
- Known? No (0 hits for "0.8%", "True Net Worth", "mattdurot").
- What it changes: (i) The only percentage bound for Moskovitz from a named outlet: < 0.8%. At the $965B Series H post-money (ST69) that is < $7.7B; at $380B (Series G) < $3.0B. (ii) Forbes uses "donated", matching Berger (NF1). (iii) It contradicts ST37 (Longterm Wiki 0.8–2.5%): Forbes' ceiling is the wiki's floor. (iv) The +$10.3B add-back is all lifetime giving, not the Anthropic block, so it cannot be read as a stake value. Also bears on (c).

**NF6. Methodology: Forbes excludes assets donated to foundations/DAFs; Bloomberg excludes closely held assets whose ownership cannot be verified.** — `G14/D/2026-09-13` (Bloomberg methodology, "As of September 13, 2026"), `G14/D/2025-05-15` (Helen Brown Group restating Forbes 400 methodology; forbes.com 2025 methodology page 403). Grok-only.
- URLs: https://www.bloomberg.com/billionaires/methodology/ ; https://www.helenbrowngroup.com/demystifying-the-forbes-400-and-the-bloomberg-billionaires-index/
- Quotes: "When ownership of closely held assets cannot be verified, they aren't included in the calculations." / "excludes any funds donated to charitable foundations or donor-advised funds."
- Known? No.
- What it changes: ST34/ST35 record that neither profile mentions Anthropic. These rules say that silence is expected once the stake is donated, so the profiles are not evidence about the stake's size or existence. Footnote material for 10z.

**NF7. Forbes US original vs. later edits: wording that differs from the AU reprint.** — `G26/A/2025-11-07` (rows 2, 4, 8) and `G26/A/2025-11-10`. VERIFIED on disk (S11 US txt vs AU txt).
- Nov 7 US original: "Tuna stresses that neither the couple nor their foundation own a stake in OpenAI now." ; "which Tuna spun out of GiveWell in 2016" ; "though they 'generally don't identify with the label.'" — After the 2025-11-11 update and in the AU reprint: "Neither the couple nor their foundation own a stake in OpenAI." ; "2017" ; "although Tuna prefers to 'emphasize the ideas over the label.'" The Anthropic-vehicle sentence is identical in every version.
- Known? ST33's note says the US wording is "identical to the Australian reprint" — true of the vehicle sentence only; see Contradictions C4.
- What it changes: A row-note correction. The dropped "now" is worth noting: as first published it implied a past OpenAI stake, which ST72 (Open Phil's 2017 grant "is not an investment") would contradict; the edit removed the implication.

### (b) Coefficient / Open Phil / Good Ventures acknowledging the Anthropic conflict

**NF8. Politico 2023: Moskovitz's on-record pledge and Open Phil's spokesperson on Muehlhauser.** — `G24/D/2023-10-13` (four rows) and `G14/B/2023-10-13`. VERIFIED (r.jina.ai render of the Politico page; direct fetch is Cloudflare-blocked).
- Who: Dustin Moskovitz (statement to Politico); Mike Levine (Open Philanthropy spokesperson); Brendan Bordelon / Politico.
- URL: https://www.politico.com/news/2023/10/13/open-philanthropy-funding-ai-policy-00121362
- Quotes: "In a statement to POLITICO, Moskovitz pledged that any monetary returns from his investment in Anthropic 'will be entirely redirected back into our philanthropic work.'" / "'My goal in investing [in Anthropic] stems from the exact same place as our non-profit work: addressing safety and security issues around transformative AI coming to market,' said Moskovitz" / Levine: the 2017 OpenAI grant was "to support work on AI safety, not an equity investment"; Muehlhauser "'holds no financial interest' in Anthropic despite sitting on its board." / Politico's own sentence (in a Deb Raji paragraph): "OpenAI and Anthropic, two firms with significant financial and personal links to Moskovitz and Open Philanthropy."
- Known? No ("politico" 0 hits in stakes/money_flows).
- What it changes: The earliest on-record Moskovitz statement about Anthropic returns, 15 months before the "early 2025" transfer: the pledge predates the vehicle. It is also the funder's first public acknowledgement of the conflict framing, made through a spokesperson.

**NF9. Karnofsky's own conflict statements (Open Phil co-founder; spouse is Anthropic's president).** — `G24/B/2024-04-29` (three rows), `G24/B/2023-02-23`. VERIFIED (EA Forum pages fetched live).
- URLs: https://forum.effectivealtruism.org/posts/7gzgwgwefwBku2cnL/joining-the-carnegie-endowment-for-international-peace (post + comment LZPgeESHa9aQqtfRh); https://forum.effectivealtruism.org/posts/aJwcgm2nqiZu6zq2S/taking-a-leave-of-absence-from-open-philanthropy-to-work-on (comment JJhnJWZo3e4jmBMjf)
- Quotes: 2024-04-29: "I also think Open Philanthropy would benefit from less ambiguity about my role in its funding decisions (especially given the fact that I'm married to the President of a major AI company)." / "My spouse isn't currently planning to divest the full amount of her equity. ... (b) The equity has important voting rights, such that divesting or donating it in full could have governance implications." / "The bottom line is that I have a significant conflict of interest that isn't going away". 2023-02-23: "80% of her equity in Anthropic is (not legally bindingly) pledged for donation. None of her equity in OpenAI is."
- Known? board.csv B12 and staff_origins S42/S44 record his METR-advisor and Anthropic roles; no row carries the equity/conflict statements.
- What it changes: Fills the "funder acknowledges the conflict" cell of 10aa with the co-founder's own words, and documents that the spousal Anthropic equity carries voting rights and was retained.

**NF10. Muehlhauser: Anthropic board member while Open Phil's AI-policy lead, "no shares".** — `G24/B/2023-04-19`. VERIFIED (EA Forum linkpost; the openphilanthropy.org original now 301s to Coefficient's homepage).
- URL: https://forum.effectivealtruism.org/posts/iiRGCydMX7aiEjvGm/12-tentative-ideas-for-us-ai-policy-luke-muehlhauser
- Quote: "Besides my day job at Open Philanthropy, I am also a Board member at Anthropic, though I have no shares in the company and am not compensated by it. Again, these opinions are my own, not Anthropic's." Same post, policy idea: "some evaluation by an independent auditor meeting certain criteria."
- Known? No row records the Anthropic board seat (money_flows M121 and S4 findings name him only as a Coefficient grantmaker).
- What it changes: A Coefficient managing director proposed independent-auditor policy in 2023 while sitting on Anthropic's board — a self-disclosed link relevant to 10aa. When he left the board is not in any lane (see Lead L7).

**NF11. Semafor 2026-09-03: Berger denies Coefficient is "the Anthropic Foundation"; Semafor calls Coefficient "a favorite of Anthropic executives".** — `G24/D/2026-09-03` (two rows), `G14/B/2026-09-03`, `G27/D/2026-09-03`. VERIFIED (live).
- URL: https://www.semafor.com/article/09/03/2026/coefficient-givings-ceo-on-silicon-valley-40-billion-philanthropy-boom
- Quotes: Ben Smith: "There's obviously hostility between the CEOs of Anthropic and OpenAI, and some impression that you guys are the 'Anthropic Foundation.'" Berger: "We're definitely not the Anthropic Foundation. I don't think we have the same personal stakes in those discussions as the other players." Semafor: "Coefficient Giving, a favorite of Anthropic executives, is expected to be one of the two main vehicles for this new philanthropy, along with the giant new OpenAI Foundation." Berger, same passage: "[Anthropic's donors are] just bunch of individuals."
- Known? No (transmission.csv TR35 and independence_fight.csv IF26 cite only Semafor's Sep 12 piece).
- What it changes: The CEO's most recent public denial of Anthropic alignment, made without mentioning the founder's Anthropic block in an unnamed nonprofit; "personal stakes" is his own phrase.

**NF12. Moskovitz on an Asana earnings call: "I'm involved with Anthropic a lot".** — `G26/C/2024-05-30` (two rows), `G26/C/2024-03-11`. Grok-only (stockanalysis.com transcripts; not re-fetched).
- URL: https://stockanalysis.com/stocks/asan/transcripts/175178-q1-2025/
- Quotes (answering analyst Josh Baer on how his "early involvement and investments in those companies" advantage Asana): "I'm involved with Anthropic a lot, and we share a board member with OpenAI, and you know, I talk to the labs" / "I think I probably know, like, 15 or 20 individual employees in Anthropic now."
- Known? No.
- What it changes: Moskovitz's own description, on a public-company call, of the depth of his Anthropic involvement in 2024 — the personal side of the conflict, in his words rather than a reporter's. (The Q4 FY2024 call names Anthropic only as an LLM partner.)

**NF13. Moskovitz: "We fund people like METR and Redwood".** — `G26/D/2026-09-11`. Grok-only (Bluesky; same account as NF2, so fetchable by the same API).
- URL: https://bsky.app/profile/moskov.goodventures.org/post/3mvaqtffuwc2o
- Quote: "At the current moment we need more outside auditing and investigation. We fund people like METR and Redwood who have been the ones writing the reports on the agent swarms and talking to the press to educate the public."
- Known? No.
- What it changes: The Anthropic-stake holder personally claims METR as "we fund", two days after the Sep 9 announcements — usable directly in 10aa. Note money_flows M104/M105 record no Good Ventures Foundation or Coefficient-entity 990 grant to METR; his "we" is the complex (DAF/pooled channels), which the row note should say.

**NF14. Karnofsky, as Anthropic staff, on the impartiality bar for external reviewers.** — `G24/B/2026-02-24`. Grok-only.
- URL: https://forum.effectivealtruism.org/posts/DGZNAGL2FNJfftwgE/responsible-scaling-policy-v3-1
- Quote: "We want our external reviewer to meet a high bar of impartiality (not just 'no equity in Anthropic' but a broad lack of any connections that could present a conflict of interest in reality or perception)."
- Known? No ("impartiality" appears only in saved docs, not in any row).
- What it changes: Anthropic's own stated standard for reviewer independence, written by the former Open Phil CEO; the natural yardstick for 10aa's structure.

**NF15. Carlsmith on leaving Open Phil for Anthropic: equity distorts.** — `G24/B/2025-11-03`. Grok-only.
- URL: https://forum.effectivealtruism.org/posts/EFF6wSRm9h7Xc6RMt/leaving-open-philanthropy-going-to-anthropic
- Quote: "there are also concerns about direct financial incentives distorting one's views/behavior – for example, ending up reliant on a particular sort of salary, or holding equity that makes you less inclined to push in directions that could harm an AI company's commercial success"
- Known? No row (Carlsmith appears only as a $40k payee in the Open Phil CY2024 990/RRF-1).
- What it changes: Minor; a Coefficient-to-Anthropic mover stating the equity-incentive problem in Coefficient-vetted text ("shared with Open Phil and Anthropic comms").

### (c) Anthropic S-1 status and investors' stake sizes

**NF16. Anthropic's own Rule 135 notice: confidential draft S-1, 2026-06-01; no public S-1 on EDGAR.** — `G16/A/2026-06-01` and four EDGAR negative rows `G16/A/2026-09-14`. VERIFIED (anthropic.com live; EDGAR queries are Grok's, consistent with ST77's method).
- URL: https://www.anthropic.com/news/confidential-draft-s1-sec
- Quote: "Today, Anthropic, PBC confidentially submitted a draft registration statement on Form S-1 to the U.S. Securities and Exchange Commission for a proposed initial public offering of our common stock. ... The number of shares to be offered and the price have not yet been set."
- Known? Partly: investments.csv IV10 note and WATCHLIST mention the 2026-06-01 draft; stakes.csv ST77 rests on WSJ second-hand and has no issuer URL. EDGAR: no "Anthropic, PBC" CIK; 35 name matches are all SPVs; 24 S-1 full-text hits for "Anthropic" in 2026 are all other filers (SpaceX, Cerebras, Oura…).
- What it changes: Replaces the WSJ paraphrase with the issuer's notice; confirms no principal-stockholder table exists publicly, so every Moskovitz/Tallinn/Schmidt/McClave/CERR percentage remains unpublished.

**NF17. NYT Sep 3 2026: Menlo, Lightspeed, Iconiq "now own 1 percent to 2 percent"; ~$130B from ~300 investors.** — `G16/B/2026-09-14` (NYT row). Grok-only, search snippet; the Wayback capture I fetched has no article body.
- URL: https://www.nytimes.com/2026/09/03/technology/anthropic-ipo-investors-winners.html
- Known? No.
- What it changes: A scale comparator for 10z: lead VCs with billion-dollar cheques hold 1–2% each, which makes Forbes' "< 0.8%" for a 2021 Series A participant (NF5) coherent. Not a figure for any named early investor.

**NF18. Situational Awareness LP holds an Anthropic stake "valued at $5 billion, according to Bloomberg"; Jane Street is an early SA backer.** — `G16/B/2026-07-30`. VERIFIED (TechCrunch live).
- URL: https://techcrunch.com/2026/07/30/ai-hedge-fund-situational-awareness-may-have-sold-its-public-portfolio-but-it-still-has-its-anthropic-shares/
- Quotes: "it continues to hold a stake in Anthropic that's right now valued at $5 billion, according to Bloomberg" / "Early backers of the fund include quant-trading firm Jane Street, Stripe co-founders Patrick and John Collison, and Meta executives Daniel Gross and Nat Friedman."
- Known? SA appears only as a Series H participant inside ST26's quote.
- What it changes: Jane Street has indirect Anthropic exposure through SA on top of its direct holding (ST20–ST30). Not a Jane Street number and should not be booked as one.

**NF19. Estonian press 2026 on Tallinn (no numbers).** — `G16/C/2026-08-24` (Delfi: interview recorded Dec 2025, published under a lede saying Anthropic "may go public in October ... at a giant two trillion dollar market value" and calling Tallinn the man who would become "officially the richest Estonian" after the IPO); `G16/C/2026-01-05` (Äripäev names him Entrepreneur of the Year, headline "modest billionaire"); `G16/C/2026-09-13` (ERR restating WSJ: Anthropic could raise up to $100B). Grok-only.
- Known? ST40–ST42 hold the Postimees Feb 2026 material; these three are new but add no share count, percentage or dollar figure. Tallinn still "has not agreed to say how large his stake is".

**NF20. Coefficient Giving Policy Fund: IRS BMF fields.** — `G27/B/2026-01-01` (three rows), `G27/C/2026-01-01`. VERIFIED (ProPublica API: ruling_date 2026-01-01, subsection 4, filing_requirement_code 2, tax_period 2025-12, asset_amount 0, income_amount 0, NTEE W99; IRS TEOS ePostSearch: 990-N for tax period 2025-01-01 to 2025-12-31, UNDER_50K "T", officer TOM VAN LOBEN SELS, filed 2026-05-04).
- Known? ST84 has the 990-N, the officer and the 2025-09-12 determination letter. New: BMF ruling month 2026-01, NTEE W99, zero assets/income, Cause IQ AKA "Open Philanthropy Policy Fund", LDA and Cal-Access negatives.
- What it changes: Confirms ST84's exclusion of the Policy Fund as the vehicle. See Contradictions C3 on the formation date.

Not new, recorded for completeness: NY Post 2025-11-09 (`G24/D/2025-11-09`) restates Forbes two days later and is not an independent source; Forge Series H-1 $589.01 (`G16` note) is share_ladder.csv LD14; TIME 2024-09-05 (`G26/C`) attributes the 2021 Anthropic investment to "Tuna's and her husband's" engagement in TIME's own copy, with Tuna's emailed statement silent on it.

---

## 2. LEADS (ranked)

**L1. Test the DAF hypothesis directly.** NF1 (not Coefficient) + ST78 (not GVF) + NF3 (the couple hold DAFs) + NF2 ("GV ... via Anthropic") converge on a Good Ventures-advised DAF. Routes: (a) Wayback copies of Open Philanthropy grant pages 2015–2025 for the sponsor's name (many carried a line that the grant was made via a donor-advised fund); (b) the GVF 990-PF Part XV grant lists for payments to a community foundation or a sponsor; (c) the sponsor's own Form 990 Schedule M for calendar 2025 — a DAF sponsor reports non-cash gifts by type in aggregate, so a large "closely held stock" line at a small sponsor would be visible even without the donor's name. Why first: it is the only candidate class every verified statement is consistent with, and (c) is checkable by Nov 2026.

**L2. Good Ventures Foundation FY2026 990-PF (Jul 2025–Jun 2026) and the FYE-2025 RRF-1.** Because of NF2, check Schedule B for closely held stock or an LLC/partnership interest and Part II line 13 / the investments-other schedule for a new named line; check the California registry for an "Audited Financial Statements" upload (ST85 notes none attached so far). Due ~May 2027 (990-PF) / already due with extension to 2026-05-15 (RRF-1 FYE 2025-06-30; ST85 says not yet seen).

**L3. Full walk of Moskovitz's Bluesky feed (8,250 posts; G26 walked ~1,500).** Public API, no auth: `public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?actor=did:plc:z7oad4td5k4tfb4dttzjym7r&limit=100&cursor=…`, filter for Anthropic, stake, shares, DAF, donor-advised, vehicle, donated, Good Ventures. Why: his X history appears to be deleted (G14 recovered one post since 2021; his EA Forum account is deleted), so Bluesky is his only surviving first-person channel, and NF2 shows he does talk about it there.

**L4. Ask Coefficient what "not to us" covers.** A one-line press question to Coefficient's contact address (from the site's contact page) — does "us" mean all four Coefficient entities, and is the vehicle a DAF? Also ask Forbes (Phoebe Liu / Matt Durot) for the basis of "$500 million" and "less than 0.8%" and whether Tuna named the vehicle off-record. Low cost; the answer either names the vehicle or is itself quotable.

**L5. Dustin A Moskovitz Remainder Interest Trust.** It gave GVF $1,395,695,354 of publicly traded securities on 2025-06-30 (ST78). A split-interest trust files Form 5227, which is open to public inspection apart from Schedule A, but is not in the e-file indexes; obtain via IRS TEOS "copies of returns" request or Form 4506-A. Why: a charitable remainder trust is tax-exempt and could loosely be called a "nonprofit vehicle"; if it received Anthropic shares in early 2025 the 5227 balance sheet would show a closely held holding. Also check whether the trust itself was created in 2025.

**L6. Coefficient Giving LLC's members and formation.** California SOS bizfile Statement of Information for "Coefficient Giving LLC" / "Open Philanthropy Project LLC" (lists managers/members) and Delaware entity search. Why: NF4 shows an LLC in the structure that ST81 does not enumerate; if it is member-owned by Moskovitz/Tuna it is an asset-capable holder.

**L7. Muehlhauser's Anthropic board tenure and exit.** NF10 documents the 2023 seat; no lane records when it ended or what he said (G24 notes lukemuehlhauser.com was Cloudflare-blocked and his resignation text was "out of page class"). Route: lukemuehlhauser.com in a browser; Wayback; Anthropic's board announcements. Why: the board overlap dates matter for 10aa's timeline.

**L8. The deleted Moskovitz tweet on Anthropic "not pushing the frontier".** G26 says it exists and is X-lane; G14 (X lane) did not record it. Routes: archive.today search for `twitter.com/moskov` and `x.com/moskov`; Wayback captures of the profile; quote-tweets via `x.com/search?q=moskov%20frontier%20Anthropic`. Why: his own words on Anthropic's role, and evidence of the deletion pattern.

**L9. Three interviews G26 listed but did not check for Anthropic content:** Stratechery 2025-10-20 Q&A (paywalled), Tim Ferriss #686 (2023-08-10; tim.blog transcript is free), Stanford PACS 2026-04-06. Why: the brief asked for "every" interview; these were named as hits and left unread.

**L10. NYT Sep 3 2026 body.** For the 1–2% comparators and any sentence on Moskovitz/Tallinn/Schmidt. Route: nytimes.com with subscription, or archive.ph (Wayback capture exists but has no body). Why: named-outlet comparators for 10z.

**L11. Karnofsky's related question, lower priority:** whether Daniela Amodei's pledged 80% has moved to a vehicle — same structure as the Moskovitz transfer and would show the pattern; not needed for 10aa.

---

## 3. NOT PULLED

Every none-found / blocked / paywalled / 403 / login row, with a manual route or a judgment that the item is genuinely absent.

### G14
- **Task A, @moskov X history 2021–2026** — "none found"; only one post recovered (2025-07-24). Route: logged-in X advanced search `from:moskov Anthropic` (Latest), then `from:moskov since:2021-05-01 until:2022-01-01` in yearly slices; Wayback captures of `twitter.com/moskov` (profile pages captured pre-2023 show tweet text); archive.today. Likely mostly deleted (see L3, L8), so expect thin results; not "genuinely absent" until the archives are checked.
- **Task A, Cari Tuna X (@CariTuna)** — last own post 2011. Genuinely absent.
- **Task B, any Coefficient/GV/Berger/Karnofsky/Oehlsen/Muehlhauser statement naming the vehicle** — none found. Berger's "not to us" (NF1) is the closest. Route: L4 (ask). Otherwise genuinely absent on the public record as of 2026-09-14.
- **Task C, Delaware/California filings naming a Moskovitz/Tuna entity as Anthropic shareholder** — none found. Delaware and California entity records do not list shareholders of a private corporation: genuinely absent by design. FEC: genuinely absent (not a disclosure venue). CauseIQ/Candid: mirror the 990s already read; genuinely absent.
- **Task D, forbes.com originals (Tuna profile 2025-11-07; True Net Worth 2026-04-20; 2025 Forbes 400 methodology 2025-09-09)** — 403/CAPTCHA. Route: Wayback `id_` captures fetched with `curl --compressed` (Forbes captures are gzip bodies — the plain fetch looks empty): Tuna profile 20251107132055 and 20251111210456; True Net Worth 20260421043155 (verified this run, NF5); methodology `web.archive.org/web/2025*/forbes.com/sites/mattdurot/2025/09/09/2025-forbes-400-methodology-how-we-crunched-the-numbers-in-2025/`.
- **Task D, Bloomberg Moskovitz profile body** — paywalled beyond the summary. Route: bloomberg.com/billionaires/profiles/dustin-a-moskovitz/ in a browser (the net-worth analysis section is visible without a terminal); ST35 already holds a May 2026 capture.

### G16
- **Task A, public Anthropic S-1** — none; issuer confirms confidential draft (NF16). Genuinely absent until the public flip. Route to catch it: EDGAR full-text `efts.sec.gov/LATEST/search-index?q="Anthropic, PBC"&forms=S-1,DRS,S-1/A` weekly; a DRS becomes public no later than 15 days before the roadshow.
- **Task B, NYT 2026-09-03 investors piece** — JS/CAPTCHA; snippet only. Route: L10.
- **Task B, Reuters 2026-08-14 (Jane Street $15B July)** — JS-blocked. Route: reuters.com in a browser; it concerns SA/AI-stock exposure, not an Anthropic share count, so low value.
- **Task B, Bloomberg 2026-04-08 tender; 2026-07-23 Alphabet stake; The Information 2026-06-02 Salesforce $5B; WSJ 2026-06-20 Jane Street profile** — paywalled. Routes: bloomberg.com / theinformation.com / wsj.com logins; Wayback often has Bloomberg (ST27/ST28/ST62 were captured that way). None is expected to give a named early investor's share count.
- **Task B, second 2026 employee tender per-share price; Series H price per share** — none in named outlets. Series H-1 PPS is on Forge ($589.01, LD14) and Prime Unicorn Index (Delaware COI) — route: primeunicornindex.com "Anthropic Series H" post (paywalled; the free teaser sometimes carries the price). Tender PPS: The Information's tender coverage (login) is the likeliest carrier; otherwise genuinely absent.
- **Task B, secondary trades by named early investors** — none found; genuinely absent publicly.
- **Task C, Äripäev 2026-01-05 and 2026-04-21 bodies** — paywalled. Route: aripaev.ee subscription, or the Estonian National Library's digital archive (DIGAR) for the print edition. The 2026-01-05 profile is the likeliest place for a Tallinn stake remark.
- **Task C, Delfi 2026-08-24 interview body** — truncated after the lede. Route: arvamus.delfi.ee with Delfi subscription; the interview was recorded Dec 2025 by Linnar Viik at a closed event.
- **Task C, Tallinn X account / jaan.info stake figure** — none. jaan.info was read (no figure); no X account resolved. Genuinely absent.
- **Task D, X posts > 5,000 views since 2026-09-01 with the keywords** — none within the 10-hit cap. Route: logged-in X search `Anthropic (Moskovitz OR Tallinn) (stake OR shares OR IPO) min_faves:100 since:2026-09-01`.

### G24
- **Task A, Coefficient/Open Phil grant write-ups since 2021** — per-grant pages 404 after the Nov 2025 rebrand. Route: `web.archive.org/web/*/openphilanthropy.org/grants/*` (coefficient_pages.csv already documents the pattern), then text-search each capture for "Anthropic"; also `coefficientgiving.org/?s=Anthropic` in a browser.
- **Task A, COI policy / Tailwind FAQ naming Anthropic** — read; Anthropic not named. Genuinely absent.
- **Task A, lukemuehlhauser.com (board resignation text)** — Cloudflare. Route: browser; Wayback. See L7.
- **Task B, EA Forum/LW posts by Berger, Cotra, Oehlsen, Mendel, Zabel on Anthropic ties** — none found by author search. Route: EA Forum GraphQL `comments(terms:{userId:…})` per author, or `forum.effectivealtruism.org/search?query=Anthropic` filtered by author; LessWrong likewise. Probably genuinely absent for Berger/Oehlsen/Zabel; Cotra has written on evaluator work and is worth one more pass.
- **Task C, Good Ventures endowment-holdings statement / lab-investment policy** — none on goodventures.org. Genuinely absent; the 990-PF is the only holdings disclosure.
- **Task D, Washington Post Apr 21 2026** — nothing recovered. No WaPo file exists in research/press-pdfs either (18 files; none WaPo). Route: washingtonpost.com search "Open Philanthropy" OR "Coefficient Giving" for April 2026; if Kevin had a specific piece in mind, the URL is needed.
- **Task D, Bloomberg / The Information / Vox / Wired sentences calling Open Phil an Anthropic investor** — none found. Route: theinformation.com search "Open Philanthropy" "Anthropic" (login); Bloomberg search; probably genuinely absent as an outlet-own sentence (Politico's NF8 sentence is the only one found).
- **Task E, X posts > 2,000 views since Sep 9 tying the stake to METR** — none above floor. Route: logged-in search `METR (Moskovitz OR "Open Phil" OR Coefficient) Anthropic (stake OR investor) since:2026-09-09`. Below-floor posts are listed in the G24 header; Khlaaf's 76k-view post is IF14 and does not name the stake.
- **Task E, Coefficient staff replies** — none. Genuinely absent as of 2026-09-14.

### G26
- **Task B, Forbes Impact Summit video/transcript (2025-09-25)** — private event; recap only. Route: YouTube search "Forbes Impact Summit 2025 Cari Tuna"; forbes.com/video. Likely genuinely absent.
- **Task C, 80,000 Hours / Dwarkesh / Lex Fridman / Bloomberg / NYT / EA Global / LessWrong AMA / Substack interviews** — none found; the named venues carry no Tuna/Moskovitz interview since 2023. Genuinely absent for those venues. The three interviews G26 found but did not read are L9.
- **Task D, Threads @moskov** — JS-rendered; no post text recovered. Route: threads.net/@moskov in a browser, use the in-app search; or `threads.net/@moskov/post/…` permalinks from web search.
- **Task D, Bluesky beyond ~1,500 of 8,250 posts** — cursor walk not completed. Route: L3.
- **Task D, LessWrong** — no Moskovitz account. Genuinely absent.
- **Task D, EA Forum** — account deleted; comments survive as [anonymous] with contemporaneous attribution. Nothing further to pull.
- **forbes.com originals; TIME curl 406; archive.org availability API 429** — all worked around (Wayback, WebFetch, CDX); nothing outstanding.

### G27
- **Task A, Forbes 2025-11-18 rebrand piece body** — G27 says "not recovered beyond search extracts". It is already on disk: `research/agents-2026-09-14/S11-stakes/docs/forbes-us-2025-11-18-pooled.txt` (ST33 note says it does not mention the stake). Nothing to pull.
- **Task A, insidephilanthropy.com 2025-11-24 (403); apnews.com 2025-11-18 (Cloudflare)** — Route: browser; both are low value (neither names the vehicle).
- **Task B, Policy Fund California / Delaware formation record** — JS portals. Route: bizfileonline.sos.ca.gov → Search → "Open Philanthropy Policy Fund" and "Coefficient Giving Policy Fund" → open the entity → download the Articles and the latest Statement of Information (formation date, officers); Delaware `icis.corp.delaware.gov/ecorp/entitysearch/NameSearch.aspx`; California AG Registry of Charities (ca-rcf.evokeplatform.com, which Kevin has used for ST85) → search "Policy Fund" (c4s register there too). This settles Contradiction C3.
- **Task B, LDA / Cal-Access lobbying registration** — zero results; genuinely absent as of 2026-09-14. Recheck after the 2026-10-20 LDA quarter (WATCHLIST).
- **Task B, any Coefficient announcement of the Policy Fund** — none. Genuinely absent.
- **Task C, new Moskovitz/Tuna entity formed 2024-07-01 to 2025-06-30** — none found via ProPublica/BMF. Routes: California AG Registry search by "Moskovitz", "Tuna", "314 Lytton"; IRS TEOS determination-letters search by name "Good Ventures"; Delaware name search "Good Ventures"; and L5 (Form 5227). ProPublica's org search for "Moskovitz" returns only unrelated Moskowitz foundations, so a DAF or trust would not surface there.
- **Task D, Oehlsen / Muehlhauser / @coeff_giving statements since 2025 on the investment** — none. Genuinely absent on X; Oehlsen's 2026-09-09 scaling post (M121/M122) does not name it.

---

## 4. CONTRADICTIONS

**C1. Where the stake sits: three statements that do not obviously agree.**
- ST78 (IRS): Good Ventures Foundation received no private stock in FY2025 (Jul 2024–Jun 2025).
- NF1 (Berger, Dec 2025): "donated his stake (and not to us)".
- NF2 (Moskovitz, Aug 2026): "GV is itself a beneficiary of that wave (via Anthropic and a number of other investments)".
- ST37 (Longterm Wiki, unsourced): "already in Good Ventures nonprofit vehicle".
Reconcilable only if "GV" in NF2 means the Good Ventures complex including a DAF, or the exposure is indirect (VC/PE fund categories in ST79), or the shares reached GVF after 2025-06-30. ST83's "remaining candidates: Coefficient Research / Advisors / Action Fund" should be re-worded to reflect NF1, and the DAF class promoted from "would never show it" to "leading candidate; sponsor's Schedule M may show it" (L1).

**C2. Moskovitz's percentage: Forbes "< 0.8%" (NF5, Apr 2026) vs Longterm Wiki "0.8–2.5%" (ST37).** Forbes' ceiling is the wiki's floor. Forbes also implies the stake was still "his early investment" at the time of donation (no secondary sales), whereas ST32's $500M at the Nov 2025 $183B–$350B marks implies 0.14–0.27%; Forbes' April figure is a ceiling, not a point estimate, so the two Forbes numbers are consistent with each other. ST37 should be demoted further or dropped.

**C3. Policy Fund formation date: G27 vs ST84 / the IRS record.** G27 (`B/2026-01-01`, `C/2026-01-01`, header) says IRS ruling 2026-01 and Cause IQ "founded in 2026", hence "after the window". But: (a) the IRS determination letter on disk is dated 2025-09-12 (`research/irs-teos/FinalLetter_39-4232601_OPENPHILANTHROPYPOLICYFUND_09122025_00.pdf`, ST84); (b) the letter's name "Open Philanthropy Policy Fund" predates the 2025-11-18 rebrand; (c) the 990-N verified live this run covers tax period 2025-01-01 to 2025-12-31 — an entity cannot file for a period beginning 2025-01-01 if formed in 2026. So the BMF ruling month is not the formation date, Cause IQ's "2026" is derived from it, and the Policy Fund was formed in 2025 or earlier — possibly inside the 2024-07-01–2025-06-30 window G27 was asked about. ST84's exclusion of it as the vehicle (990-N, $0 assets) still stands; only G27's "after the window" is wrong. The CA SOS record (Not Pulled, G27 Task B) settles it.

**C4. ST33 note vs G26 Task A.** ST33: US original wording "identical to the Australian reprint". G26 (verified on disk): identical for the vehicle sentence; the adjacent OpenAI sentence, the GiveWell year, and the EA-label wording differ between the Nov 7 original and the post-Nov-11 update/AU reprint (NF7). Fix the ST33 note; consider dating ST32/ST33 to 2025-11-07 (US original) rather than 2025-11-10 (AU syndication).

**C5. Forbes net-worth figures across lanes.** G14 `D/2026-09-05` reports "$10.2B as of 9/5/26" (search extract); ST34 has $8.6B as of 9/5/26 (Wayback capture); G16 `B/2026-09-14` has $8.7B as of 9/14/26 (fetched). G14's $10.2B is an extract artifact and should not be used.

**C6. Bloomberg Asana share count.** G14 `D/2026-09-14` ("~130 million Class A and B shares per 2026 proxy") vs ST35 ("about 123 million", May 2026 capture). Not a conflict — the profile was updated — but ST35 is stale.

**C7. G26 vs G14 on the deleted Moskovitz tweet.** G26 (Task D caps) says a taken-down Moskovitz tweet about Anthropic not pushing the frontier "is X, not recorded here"; G14, the X lane, has no such row and reports no @moskov Anthropic post at all. Each lane points at the other; neither captured it (L8).

**C8. "We fund people like METR" (NF13) vs money_flows M104/M105.** Good Ventures Foundation's 990-PFs FY2022–FY2025 and the three Coefficient entities' 990s TY2022–TY2024 show no grant to METR. Moskovitz's "we" is therefore the complex (DAF/pooled routes recorded elsewhere in money_flows), not the Foundation directly; the row note should say so to avoid a reader inferring a 990 line that does not exist.

**C9. G27 coverage note vs disk.** G27 header says the Forbes Nov 18 2025 rebrand body was "not recovered beyond search extracts"; it is on disk (S11 docs). Not a factual conflict; a lane that did not check local files.

**C10. Berger's "Open Phil never invested in Anthropic" (NF1) vs Politico's "two firms with significant financial and personal links to Moskovitz and Open Philanthropy" (NF8).** Not a contradiction of fact — Politico's sentence is about links, Berger's about equity — but the two should be quoted together in 10aa so neither is read as refuting the other.

---

### Verification ledger (this run)
Verified live or via archive: NF1 (X syndication), NF2 (Bluesky API, with thread context), NF3 and NF7 (on-disk Wayback text), NF5 (Wayback 20260421043155, gzip body), NF8 (r.jina.ai), NF9 and NF10 (EA Forum live), NF11 (Semafor live), NF16 (anthropic.com live), NF18 (TechCrunch live), NF20 (ProPublica API + IRS TEOS live). Grok-only: NF4, NF6, NF12, NF13, NF14, NF15, NF17, NF19. Scratch copies of every fetched page are in the session scratchpad only; nothing was added to `research/`.
