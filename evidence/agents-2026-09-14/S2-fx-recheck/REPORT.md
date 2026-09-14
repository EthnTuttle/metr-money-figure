# S2 fxtwitter recheck — 2026-09-14

Refetched every X status cited in the eight S2 CSVs through `https://api.fxtwitter.com/i/status/<id>` (script: `recheck_fx.py`, 0.5 s pause, 20 s timeout, 30 s sleep and up to 3 tries on 429/connection errors). Payloads: `json/<id>.json` (611 unique IDs, 627 CSV rows; 16 IDs are cited by more than one file). Fetch window 2026-09-14 ~06:55–07:05 UTC. Results: `recheck.csv`.

Checks per row: author screen_name == stored handle (case-insensitive); stored text (`text_200` / `text_120` / `metr_language` / `event`) vs fetched text — `yes` = first 100 chars equal after whitespace normalisation, or every quoted fragment present; `partial` = some fragments present / paraphrased `event` cell / high prefix similarity; `no` = neither; created_at date == stored UTC date; fresh `views` vs stored `views`. `status` = DIFFERS if any of author/text/date is `no`.

Note on the directory: a parallel worker also wrote `fetch.py`, `compare.py`, `report.py`, `build_manifest.py`, `manifest.json`, `fetch_status.json` and an early `recheck.csv` (01:55, 543 rows BLOCKED because its JSONs had not landed yet). 510 of the 611 payloads were saved by that worker's fetcher (`_http_status: null`), the remaining 101 by `recheck_fx.py` (`_http_status: 200`); all 611 are ordinary fxtwitter payloads. The `recheck.csv` now on disk was rewritten by `recheck_fx.py --compare-only` after all 611 payloads were present and supersedes the 01:55 file.

## Counts per file

| file | rows | OK | DIFFERS | DELETED | BLOCKED | text partial |
|---|---:|---:|---:|---:|---:|---:|
| sacks_thread.csv | 86 | 86 | 0 | 0 | 0 | 0 |
| x_amplifiers.csv | 113 | 111 | 2 | 0 | 0 | 0 |
| metr_posts.csv | 306 | 306 | 0 | 0 | 0 | 0 |
| arrivals.csv | 11 | 11 | 0 | 0 | 0 | 0 |
| lab_mentions.csv | 10 | 10 | 0 | 0 | 0 | 0 |
| officials_mentions.csv | 1 | 1 | 0 | 0 | 0 | 0 |
| sep9.csv | 14 | 14 | 0 | 0 | 0 | 8 |
| independence_fight.csv | 86 | 84 | 1 | 1 | 0 | 9 |
| **total** | 627 | 623 | 3 | 1 | 0 | 17 |

Author match: 626/626 fetched rows `yes`. Date match: 626/626 `yes`. No BLOCKED rows (every ID returned HTTP 200 or a definitive 404; no 429s or connection errors were hit).

## DIFFERS / DELETED rows

### independence_fight.csv IF33 — DELETED — 2099148649091465466 (@matthewstoller, 2026-09-13 14:50 UTC)
fxtwitter returns `{"code":404,"message":"NOT_FOUND","tweet":null}` on both `/i/status/<id>` and `/matthewstoller/status/<id>`. The account itself is live: `api.fxtwitter.com/matthewstoller` returns 200, 166,174 tweets, not protected — so this is a **deleted post, not a suspended account**. Stored views 8,385 (last seen). The earlier capture survives at `research/x-payloads/2099148649091465466.json` (text: "Yes this whole panic is an obvious ruse to end Anthropic's cash burn. That said if the spending really does slow that has implications for the chip sector. Would be funny if Anthropic popped the bubble before its IPO."; views 8,385; created Sun Sep 13 14:50:12 UTC 2026). If the row is used in a figure, cite it as deleted-since-capture with the archived payload as the source.

### independence_fight.csv IF06 — DIFFERS (text) — 2098480585119572317 (@JoeJBenton, 2026-09-11 18:35 UTC)
Author and date match. Stored `metr_language` = "I'll be joining @METR_Evals to do independent evaluations of these risks." That sentence is **not in the post the URL points to**. The fetched post is the opener of Benton's Sep 11 thread ("I left Anthropic's safety team two weeks ago. Now feels like a good moment to explain why. …"; 2,616,903 views). It is also not in his Sep 9 quote-post D02 (2097529404754948390: "Evaluating those risks, and changing incentive structures so we can address them, is why I'm joining METR."). The quoted sentence is presumably a later post in the Sep 11 thread; fxtwitter does not return thread children, so the row's URL should be re-pointed to the specific status that contains the sentence, or the quote replaced with the opener's wording. `names_metr` = yes remains true of the thread but unverified for this status id.

### x_amplifiers.csv X16 — DIFFERS (text, mechanical) — 2097770962557026650 (@IterIntellectus, 2026-09-09 19:35 UTC)
### x_amplifiers.csv X93 — DIFFERS (text, mechanical) — 2097773479412015598 (@llm_wizard, 2026-09-09 19:45 UTC)
Both are media-only quote-posts of Anthropic's 2097762642958135398. The stored `text_120` is just the media t.co link (`https://t.co/avuypJu34f`, `https://t.co/iLepILE8ut`); fxtwitter strips the media link so the fetched `text` is empty, and the first-100-chars test fails with nothing to compare. Author, date, quote target (`quote.url` = the Anthropic post) and media presence all check out; fresh views 32,900 (stored 32,900) and 1,534 (stored 1,534). These are not content discrepancies — they are flagged only because the rows carry no words. If a caption is ever needed, the stored text is useless and the quoted post/media should be described instead.

## Partial text matches (17 rows, all status OK)

These are rows whose stored cell is a paraphrase or an editorial `event` summary rather than a verbatim excerpt, so the 100-char test cannot pass; they are listed so nobody mistakes `partial` for a problem. Quoted fragments were checked where the cell had them.

- sep9.csv D03, D04, D06, D08, D09; independence_fight.csv IF20, IF55, IF60, IF66 — `event` is an editorial summary with no verbatim quote; fetched text is consistent with the summary.
- sep9.csv D05 (@dwarkesh_sp) — fragment "ordain [METR] the evaluator" has an editorial bracket; fetched: "…ordain it 'the evaluator'". Consistent.
- sep9.csv D14 (@BethMayBarnes), D18 (@AnthropicAI) — the `event` cell is a long research note quoting several *other* posts; the fragment for this status id is present verbatim. Consistent.
- independence_fight.csv IF56 (@suchenzang, sim 0.73), IF58 (@So8res, 0.87), IF65 (@elonmusk, 0.88), IF93 (@MikeMcCormick_, 0.98) — near-verbatim with punctuation/ellipsis differences. Consistent.
- independence_fight.csv IF103 (@theonejvo) — 2/3 fragments; the third fails only on curly vs straight quotes around "experts". Consistent.

## Views

625 rows have both stored and fresh views; none declined; 192 unchanged (mostly older metr_posts rows). Missing: IF04 has no stored views (fresh 152,999 for 2097707668920205580, same post as sep9 D05); IF33 has no fresh views (deleted). Median change by file: sacks_thread 18.5 %, officials_mentions 14.0 %, independence_fight 1.4 %, sep9 0.5 %, arrivals 0.3 %, x_amplifiers 0.1 %, metr_posts 0.0 %, lab_mentions 0.0 % — i.e. only the Sep 13 Sacks-thread material is still moving.

### Ten largest view increases (absolute)

| file | row | id | stored | fresh | delta |
|---|---|---|---:|---:|---:|
| independence_fight.csv | IF08 | 2098773920774074715 | 67,050,961 | 69,565,536 | +2,514,575 (3.8 %) |
| independence_fight.csv | IF28 | 2098973625252708460 | 7,133,727 | 8,238,817 | +1,105,090 (15.5 %) |
| officials_mentions.csv | OM01 | 2098973625252708460 | 7,226,564 | 8,238,817 | +1,012,253 (14.0 %) |
| sep9.csv | D01 | 2097476196791709843 | 170,289,991 | 170,828,657 | +538,666 (0.3 %) |
| independence_fight.csv | IF17 | 2098811563415150910 | 15,483,235 | 15,911,921 | +428,686 (2.8 %) |
| independence_fight.csv | IF12 | 2098789109980332057 | 10,883,514 | 11,250,785 | +367,271 (3.4 %) |
| independence_fight.csv | IF48 | 2099170698887315833 | 961,521 | 1,226,528 | +265,007 (27.6 %) |
| sep9.csv | D09 | 2097765966088487290 | 153,629 | 333,625 | +179,996 (117.2 %) |
| independence_fight.csv | IF02 | 2097765966088487290 | 229,399 | 333,625 | +104,226 (45.4 %) |
| metr_posts.csv | MP305 | 2097765966088487290 | 239,688 | 333,625 | +93,937 (39.2 %) |

(IF28 and OM01 are the same Sacks post 2098973625252708460, stored at two different capture times; D09, IF02 and MP305 are the same METR post 2097765966088487290.)

### Ten largest view increases (percentage, stored >= 1,000)

| file | row | id | stored | fresh | delta |
|---|---|---|---:|---:|---:|
| sacks_thread.csv | SK63 | 2099250910614696205 | 2,782 | 6,492 | +3,710 (133.4 %) |
| sacks_thread.csv | SK56 | 2099220766504222732 | 3,318 | 7,249 | +3,931 (118.5 %) |
| sacks_thread.csv | SK14 | 2099171966192324721 | 26,499 | 57,869 | +31,370 (118.4 %) |
| sep9.csv | D09 | 2097765966088487290 | 153,629 | 333,625 | +179,996 (117.2 %) |
| x_amplifiers.csv | X91 | 2099185204204093441 | 1,591 | 3,390 | +1,799 (113.1 %) |
| x_amplifiers.csv | X09 | 2099205059896561937 | 80,889 | 164,227 | +83,338 (103.0 %) |
| arrivals.csv | AR11 | 2099241828126220588 | 9,373 | 17,719 | +8,346 (89.0 %) |
| x_amplifiers.csv | X105 | 2099202058163232980 | 1,174 | 2,218 | +1,044 (88.9 %) |
| x_amplifiers.csv | X89 | 2099212730809147445 | 1,692 | 2,877 | +1,185 (70.0 %) |
| sacks_thread.csv | SK49 | 2099224756038033415 | 4,962 | 8,242 | +3,280 (66.1 %) |

## Deleted or suspended

- Deleted: 2099148649091465466 (@matthewstoller, independence_fight IF33) — see above. Account live.
- Suspended accounts: none. All 610 other statuses resolved with their expected author; no 401 (protected) or suspended-account responses.
- Two posts (X16, X93) have no text at all (media-only quote-posts) but still exist.

