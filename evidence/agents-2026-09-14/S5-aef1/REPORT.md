# S5-aef1 — METR Frontier Risk Report (May 19 2026): AEF-1 compliance table

Source: https://metr.org/blog/2026-05-19-frontier-risk-report/ (local copy: research/fr-verify/risk-report-20260519.html, 1.9 MB).
Section: Appendix A: Process details > "Operating conditions" (anchor #operating-conditions), Table A.1 "Comparison of this report's procedures to the AEF-1 standard."
Parsed 2026-09-14 with python regex over the `<table>` inside the figure (scripts/styles stripped, tags removed, entities unescaped). Two independent parses agree on all 40 rows.

Files:
- aef1_compliance.csv — 40 rows (AE01–AE40): 26 numbered items (Requirement/Recommendation) + 8 sub-items under 1.1 (access types) + 6 sub-questions under 2.4 (CoI disclosure questions) + 5 principle headers folded into principle_no/principle_title. 
- aef1_preamble.txt — the three verbatim paragraphs preceding the table (from the first AEF-1 mention in the Operating conditions section through the Constellation sentence).
- REPORT.md — this file.

Note on row AE19 ("Does a meaningful fraction of the evaluator's funding come from ..."): the page renders a single cell reading "No. Note that METR's work with nonpublic models and use of free tokens incentivize a cordial relationship with AI companies. See our website." The CSV stores "No" in `fulfilled` and the rest in `notes_evidence`.
Note on row AE23 ("Did the evaluator have any other conflicts of interest ..."): the page has no Yes/No; the cell reads verbatim "Several of the staff and collaborators directly involved in this pilot (at least 6) have close personal relationships with AI company staff." — stored verbatim in `fulfilled`.

## 1. Counts per principle (all 40 rows, verbatim cell values)

| Principle | Rows | Yes | Partial | No | Not requested | N/A | See notes | Other |
|---|---|---|---|---|---|---|---|---|
| 1: Secure Sufficient Access and Resources | 13 | 7 | 2 | 0 | 4 | 0 | 0 | 0 |
| 2: Minimized Conflicts of Interest | 12 | 5 | 0 | 6* | 0 | 0 | 0 | 1 (AE23) |
| 3: Analytic Autonomy | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 |
| 4: Transparent Methods and Results | 7 | 5 | 0 | 0 | 0 | 1 | 1 | 0 |
| 5: Protection of Sensitive Information | 4 | 3 | 0 | 1 | 0 | 0 | 0 | 0 |
| **Total** | **40** | **24** | **2** | **7** | **4** | **1** | **1** | **1** |

*Caution for the infographic: five of the six "No" cells in Principle 2 (AE18, AE20, AE21, AE22 and AE19's "No") are answers to disclosure questions where "No" is the favourable answer (not paid by the provider, no meaningful funding from it, no equity either way, no dual employment). Only ONE "No" in Principle 2 is a non-compliance: item 2.3 (no published CoI policy).

### Counts restricted to the 26 numbered Requirement/Recommendation items (the compliance-bearing rows)

| Principle | Items | Yes | Partial | No | Not requested | N/A | See notes |
|---|---|---|---|---|---|---|---|
| 1 | 5 (3 Req, 2 Rec) | 4 | 0 | 0 | 1 (1.5 legal safe harbor, Rec) | 0 | 0 |
| 2 | 6 (5 Req, 1 Rec) | 5 | 0 | 1 (2.3 Req) | 0 | 0 | 0 |
| 3 | 4 (2 Req, 2 Rec) | 4 | 0 | 0 | 0 | 0 | 0 |
| 4 | 7 (2 Req, 5 Rec) | 5 | 0 | 0 | 0 | 1 (4.4 Rec) | 1 (4.6 Req) |
| 5 | 4 (3 Req, 1 Rec) | 3 | 0 | 1 (5.4 Req) | 0 | 0 | 0 |
| **Total** | **26 (15 Req, 11 Rec)** | **21** | **0** | **2 (both Requirements)** | **1** | **1** | **1** |

Headline for the infographic: of 26 numbered AEF-1 items, METR reports 21 Yes, 2 No (2.3 no published CoI policy; 5.4 no responsible disclosure policy), 1 "See notes" (4.6 redaction authority), 1 Not requested (1.5 legal safe harbor), 1 N/A (4.4). The two Partial cells are 1.1 sub-items (scaffolding access; safeguard exemptions). Rows: 26 numbered + 8 sub-items of 1.1 + 6 sub-questions of 2.4 = 40.

## 2. All Partial, No and other non-Yes items (verbatim)

### Partial (2, both sub-items of 1.1)
- AE03 (1.1 sub-item): "The evaluator had access to the system's scaffolding." — Partial — "See sections on model access and the pilot questionnaire."
- AE04 (1.1 sub-item): "The evaluator had exemptions from system safeguards." — Partial — "See section on model access."

### No — non-compliance (2)
- AE15, item 2.3, Requirement: "The evaluator has published a conflict of interest policy, and it was applied to the evaluation." — No — "See above description."
- AE40, item 5.4, Requirement: "The evaluator established and followed a responsible disclosure policy." — No — "METR has not established a specific responsible disclosure policy."

### No — favourable answers to the 2.4 disclosure sub-questions (5)
- AE18: "Was the evaluator paid by the system provider or its direct competitor to conduct the evaluation?" — No
- AE19: "Does a meaningful fraction of the evaluator's funding come from the system provider, its employees, or its direct competitors?" — "No. Note that METR's work with nonpublic models and use of free tokens incentivize a cordial relationship with AI companies. See our website."
- AE20: "Do the system provider, its employees, or its direct competitors own equity in the evaluator organization?" — No
- AE21: "Do evaluator staff who carried out the evaluation own equity in the system provider or its direct competitors?" — No
- AE22: "Do any evaluation staff working on the evaluation simultaneously work for the system provider or its direct competitors?" — No

### Other non-Yes cells
- AE23 (2.4 sub-question): "Did the evaluator have any other conflicts of interest relevant to the evaluation?" — "Several of the staff and collaborators directly involved in this pilot (at least 6) have close personal relationships with AI company staff."
- AE06 (1.1 sub-item): "The evaluator had finetuning access." — Not requested
- AE07 (1.1 sub-item): "The evaluator had access to model weights." — Not requested
- AE09 (1.1 sub-item): "The evaluator had access to relevant user data." — Not requested — "Companies shared information about their internal usage patterns. METR did not request or receive external user data."
- AE13, item 1.5, Recommendation: "The system provider provided legal safe harbor for actions by the evaluator that are within the agreed upon scope of the evaluation." — Not requested
- AE30, item 4.4, Recommendation: "The system provider did not misrepresent the evaluation's findings." — N/A — "METR presented its own findings."
- AE32, item 4.6, Requirement: "The system provider did not have authority to redact results to conceal concerning findings." — See notes — "Participants could exit the pilot silently. Participants that remained could redact certain findings, but could not redact the top-level redaction summary sentence. See section on redaction and anonymization."

Also worth quoting for the infographic (Yes rows with caveats in the notes):
- AE26, item 3.3, Recommendation: "The evaluator ran the evaluations themselves via direct system access." — Yes — "Some evaluations were conducted by participant companies."
- AE27, item 3.4, Requirement: "The evaluator retained editorial control over how they present the results of their evaluation." — Yes — "Participant companies did not have editorial control over the final public report, but did have control over what non-public information METR could incorporate into it."
- AE28, item 4.1, Requirement: "The evaluator shared sufficient methodological details to allow for independent review of the results." — Yes — "Not determinable by METR alone. See section on evaluation details."
- AE14, item 2.1, Requirement: "The evaluator did not receive compensation contingent on the results of the evaluation." — Yes — "METR did not request or receive compensation for this assessment. Participants provided complimentary access to their models."
- AE25, item 2.6, Recommendation: "The evaluator disclosed any separate agreements with the system provider that significantly impact the independence and trustworthiness of the evaluation." — Yes — "Note that METR's work with nonpublic models and use of free tokens incentivize a cordial relationship with AI companies. See our website."

## 3. Every sentence on the page mentioning "conflict of interest"/CoI, "funding independence", "Constellation", "social ties", or "recusal" (verbatim)

Search was over the whole page text (body, footnotes, appendices, embedded transcripts). Matches for "funding" outside this section were only agent-transcript noise ("seed funding announcements", "funding retroactive public goods") and are excluded. "Constellation", "social ties" and "recus*" each occur only in the Operating conditions section.

Operating conditions preamble (see aef1_preamble.txt):
1. "METR did not have an applicable personnel conflict of interest (CoI) policy in place at the start of this project, and as such we did not run a formal recusal or disclosures process."
2. "Given this, this pilot was not compliant with all of the requirements of the AEF-1 standard."
3. "Nonetheless we believe it is good practice to disclose compliance and non-compliance and hope other organizations conducting third-party risk assessments do so too."
4. "We think having a personnel CoI policy is an important part of building and maintaining independence, and we are actively working on developing such a policy."
5. "METR does have principles around maintaining institutional funding independence, including not accepting cash payments or donations from AI companies and AI lab executives." (the word "funding" is hyperlinked to https://metr.org/about#funding)
6. "Also note that some METR staff have strong social ties to employees of AI companies, and METR currently works out of a shared research center (Constellation) which hosts some AI lab staff." ("Constellation" is hyperlinked to https://constellation.org/)

Table A.1 cells:
7. Principle header: "2: Minimized Conflicts of Interest"
8. Item 2.3: "Requirement: The evaluator has published a conflict of interest policy, and it was applied to the evaluation." — No — "See above description."
9. Item 2.4: "Requirement: The evaluator clearly disclosed conflicts of interest relevant to the evaluation." — Yes
10. 2.4 sub-question: "Did the evaluator have any other conflicts of interest relevant to the evaluation?" — "Several of the staff and collaborators directly involved in this pilot (at least 6) have close personal relationships with AI company staff."
11. Item 2.5: "Requirement: The evaluator recused any individuals with a significant financial interest in the system provider from carrying out the evaluation." — Yes (no notes)
12. 2.4 sub-question / 2.6 note (appears twice): "Note that METR's work with nonpublic models and use of free tokens incentivize a cordial relationship with AI companies. See our website."

Related independence sentences elsewhere on the page (not matching the exact keywords but on point):
13. Intro: "We're grateful to Anthropic, Google, Meta, and OpenAI for participating in a process that involved more direct access to non-public information and more editorial independence than in previous external evaluation engagements.5"
14. Footnote 5: "Our pilot agreements with participating companies did not give them the right to approve this industry-level publication. This is a meaningful improvement over previous arrangements with companies that required us to submit certain evaluation reports for review and approval. However, this pilot was not designed to provide robust accountability: We gave participants the option to exit silently from the pilot at any point before approving any non-public information from them to include in the report. This means that any company could have withdrawn partway through the process for any reason."
15. Pilot process: "Participants received a draft approximately one week before publication but did not have approval rights over this final report."
16. Silent exit: "In keeping with this principle, we are not disclosing whether there were any companies that initially participated in the pilot and exited partway through. We offered this option to encourage companies to participate in a novel and potentially sensitive process. However, it means that the set of companies represented in this report may not represent the full set of companies who began engaging with the exercise: if any company withdrew partway through the pilot, we would not be permitted to disclose that."

## 4. Every sentence naming the model / lab access METR had (verbatim)

No sentence on the page contains the literal phrase "days of access"; access duration is given only via dates (below).

Pilot overview (main text, "Information gathering" phase):
- "Information gathering (late February through mid-March 2026). Each participant provided:"
- "Access to their model(s), including raw chains of thought. METR asked participants to share the model that represented their internal state of the art at the start of the assessment.6"
- "Responses to a detailed questionnaire we prepared, which asked for information about the capabilities and propensities of the shared model(s), how AI was used and monitored internally, and trends in the pace of progress."
- "Evaluations and private reports (early March through early April 2026). METR produced a company-specific private report for each participant, typically with evaluation results on the shared models, an analysis of their questionnaire answers, and tentative high-level recommendations.7"
- Footnote 6: "In some cases, METR gave a participant an explicit date and asked them to share whichever model was their strongest internally-deployed model as of at least that date or later. The earliest such date specified for any participant was Feb 16, 2026. Separately, the last date on which any participant shared a model with us was Mar 16, 2026."
- Footnote 7: "These reports were shared with companies starting on Mar 30, 2026. METR did not share these reports further with anyone."
- Footnote 9: "Participants were not granted control over results that METR could have produced with public access. This included evaluation scores and transcripts (without chain of thought) from public models."
- "All participants (Anthropic, Google, Meta, and OpenAI) stated that the model(s) they shared represented their internal state-of-the-art at some point in the mid-February to mid-March 2026 assessment window."
- Summary bullet (top of page): "Access to their most capable internal model(s) at the time of assessment, including raw chains of thought."

Appendix A > Model access (full section, verbatim):
- "We asked each participating company to share the model(s) that best represented its internal state of the art for use as an autonomous agent. Some companies shared multiple models. For companies whose most capable model was already publicly available, we used that model (with chain-of-thought access if not already visible). For companies that shared stronger internal models, we evaluated those instead."
- "All participating companies assured us that the shared models represented each company's internal state of the art around the time they were shared (though not all models were internally deployed). The final date that any model was shared with us was Mar 16, 2026. Some models we evaluated may have since become publicly available, but we are not confirming whether this is the case for any specific model."
- "For each shared model, we requested:"
- "API access with chain-of-thought visibility, so that we could examine the model's reasoning during evaluations and test chain-of-thought monitoring."
- "Rate limits of at least 4M input tokens per minute, 1M output tokens per minute, and 1K requests per minute, sufficient to run our time horizon benchmark and other evaluations."
- "Zero data retention (ZDR), if possible, to prevent our private evaluation tasks from contaminating future training. Regardless of ZDR, our agreement specified that companies are not permitted to train on our evaluation tasks."
- "We also asked each company whether we could run their model's outputs and chain of thought through third-party AI services (e.g., for automated monitoring research). Companies were not required to authorize this, and we adjusted our procedures based on each company's preferences."
- "Evaluation results on shared models fed into the aggregated benchmark statistics in this report, which represent estimated ranges for the current internal capability frontier without identifying which company any individual result came from."

Appendix A > Redaction and anonymization / Silent exit (access-relevant sentences):
- "Moreover, companies agreed that METR could use and publish any evaluation results that it would have been able to produce with public model access."
- "We also extracted key transcripts that relied on privileged access because they contained chains of thought or came from a non-public model."
- "Participants likewise gave written approval for the use of transcripts that relied on privileged access."
- "We would not incorporate evaluation results obtained through non-public model access in our aggregated statistics. (Naturally, we would still be able to report on evaluations conducted on publicly available models from any company.)"

Appendix A > Questionnaire (what METR said it would run, and what it asked for re scaffolding):
- "As described in [document describing the pilot process], Developer should give METR output and chain-of-thought access to a frontier model for evaluation (henceforth the shared model); see [model access guide] for details on how to select an appropriate model."
- "By default, we would evaluate the direct capabilities of the shared model using one of the following scaffolds: (a) the Inspect ReAct agent scaffold, (b) Triframe (a more custom-built scaffold that chooses from many alternative actions at each step and works especially well for some reasoning models), (c) Inspect implementations of external scaffolds. We currently have Claude Code and Codex CLI set up, but we would be happy to use another scaffold if Developer provides one."
- "Do you have scaffolds that make better use of large amounts of inference compute through e.g. test-time weight updates, using internal trained reward models to grade proposed model actions, or other techniques that METR couldn't replicate with the level of access in [model access guide]?"
- "If so, can you share relevant scaffolding, tools, or techniques that would help us better elicit direct capabilities?"
- "Do you have internal scaffolds or prompts that elicit strong covert capabilities?"
- "We would evaluate both with and without giving monitors access to the shared model's CoTs."

Table A.1 access rows (Principle 1, item 1.1 and sub-items):
- "Requirement: The evaluator secured sufficient technical access to assess the specific system characteristics being evaluated." — Yes — "See section on model access."
- "The evaluator had query access." — Yes
- "The evaluator had access to the system's scaffolding." — Partial — "See sections on model access and the pilot questionnaire."
- "The evaluator had exemptions from system safeguards." — Partial — "See section on model access."
- "The evaluator had access to intermediate system states." — Yes — "METR had access to chains of thought for all shared models. See section on model access."
- "The evaluator had finetuning access." — Not requested
- "The evaluator had access to model weights." — Not requested
- "The evaluator was granted access to other tools for elicitation or otherwise supporting external validity." — Yes — "See section on the pilot questionnaire."
- "The evaluator had access to relevant user data." — Not requested — "Companies shared information about their internal usage patterns. METR did not request or receive external user data."
- Item 1.3: "Requirement: The evaluator had access to sufficient computational resources to complete a thorough evaluation." — Yes — "See section on model access."
- Item 1.4: "Requirement: The evaluator had adequate time to carry out a thorough evaluation." — Yes — "METR chose its own evaluation schedule."
- Item 2.1 note: "METR did not request or receive compensation for this assessment. Participants provided complimentary access to their models."
- Item 5.2 note: "The report has a section that discusses how METR addressed agent attempts to game evaluations. See section on model access for protections against leakage."

Appendix B, per-company model-sharing sentences:
- Anthropic: "Anthropic shared two models (or model versions) with us: one which was deployed before the internal deployment cutoff date we gave the company and one deployed after our cutoff (which they were not required to share as part of the pilot expectations). We agreed to treat these as two distinct 'companies' for the purposes of our pilot. This meant that they received two distinct company-specific private reports. This also meant that we gave Anthropic the option to redact information about the latter model while otherwise remaining in the pilot (an option they did not choose to exercise). We no longer have access to the latter model."
- Anthropic: "Anthropic shared its initial responses to our questionnaire on Mar 13, 2026, and followed up with additional questionnaire answers covering their second shared model on Apr 1, 2026. METR delivered both private reports to Anthropic on Apr 6, 2026."
- Google: "Google shared the best internal model with us at the time for our assessment, sometime between Feb 16, 2026 and Mar 30, 2026."
- Google: "Google shared its responses to our questionnaire on Mar 13, 2026, and METR delivered the private report to Google on Mar 30, 2026."
- Meta: "Meta shared an intermediate checkpoint of a model as the best representation of its state of the art for autonomous use as of Mar 16, 2026. At the time of the questionnaire, the shared model checkpoint was not deployed internally or externally, and this checkpoint has not been deployed as an official model as of Apr 21, 2026."
- Meta: "Meta shared its responses to our questionnaire on Mar 24, 2026, and METR delivered the private report to Meta on Mar 31, 2026."
- OpenAI: "The model OpenAI shared with us for this exercise was internally deployed in approximately late February 2026. They reported that the gap between internal and external deployment was a few weeks for their most recent two models that were publicly deployed."
- OpenAI: "OpenAI shared its responses to our questionnaire on Mar 12, 2026, and METR delivered the private report to OpenAI on Mar 30, 2026."
- Section on chain-of-thought: "In the course of this exercise, we reviewed the raw chains of thought from most shared models, and they largely appeared legible;42"
- "Raw chains of thought for closed source models are not accessible by default."

## 5. Caveats
- The local HTML was saved 2026-09-14 00:47; no live fetch was performed (the task permitted fetch-only, but the local copy contained the complete table and all sections, so it was not needed).
- Row AE23 has a free-text answer rather than Yes/No; any Yes/No tally should treat it as "disclosed, unresolved" rather than as a No.
- "Partial" appears only on two access sub-items (scaffolding, safeguard exemptions); the numbered Requirement/Recommendation items have no Partial cells.
