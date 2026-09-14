# S1 donor-rule verification — 2026-09-14

Scope: the 17 rows of research/donor_rule.csv marked "Grok G8 lane, not refetched" (DR01, DR02, DR03, DR04, DR06, DR09, DR11, DR13, DR14, DR16, DR17, DR20, DR21, DR23, DR24, DR25, DR27). Every URL was refetched with curl (Chrome UA, --compressed; Wayback rows via the raw `id_` form) and saved here as `<row_id>-<short>.html`; extracted text alongside as `.txt`. Row-level results are in `verification.csv`.

Tally: 15 CONFIRMED, 1 DIFFERS (DR14, date only), 1 BLOCKED (DR16, NYT).

## One line per row

- DR01 CONFIRMED — 20240423101403 about is a template placeholder ("(Replace) We're dedicated to learning how to give as well as possible"); no Funding section, none of the four phrases.
- DR02 CONFIRMED — 20240423121005 donate exists (HTTP 200); every.org instructions only; 'cannot accept' / 'frontier AI company employees' / 'compensation from AI companies' / 'not accepted funding' all absent.
- DR03 CONFIRMED — 2024 Annual Report PDF: "total 2024 budget of $10 million" and "we seek to raise and deploy $15 million" verbatim; no employee-donation or 'cannot accept' rule anywhere in the text.
- DR04 CONFIRMED — 20241231011203 about: Partnerships says companies "have also provided access and compute credits to support evaluation research"; no Funding / 'How is METR funded?' section, no 'not accepted funding', no employee rule.
- DR06 CONFIRMED — TechCrunch (Julie Bort, 2025-04-17): SAIF, "$100,000 checks as a SAFE ... with a $10 million cap". The row's "no lab employment recovered" clause is an absence claim the article neither supports nor contradicts.
- DR09 CONFIRMED — X thread (Sep 23 2025) contains "To date, we have not accepted funding from frontier AI labs." plus the metr.org/donate and giving@metr.org post; no employee-gift ban anywhere on the page.
- DR11 CONFIRMED — 20251002100351 donate: "Support from a wide range of independent donors ..." body and "To date, September 2025, we have not accepted compensation from AI companies ... However, companies have provided access and compute credits ..." footnote, both verbatim.
- DR13 CONFIRMED — 20260412023104 CHM profile: "Technical Lead, OpenAI" with the 2018/2019/Minecraft-and-LLMs bio; the 2025-12-10 capture (20251210202132) is identical.
- DR14 DIFFERS (date only) — arXiv 2412.16720: Farhi is listed under "Supporting Leadership" as claimed, but v2 is dated 30 Apr 2026 (abs: "[v2] Thu, 30 Apr 2026 02:46:40 UTC"; HTML header "v2 [cs.AI] 30 Apr 2026"), not 29 Apr 2026. Suggest changing the row date to 2026-04-30 (or note "29 Apr Pacific / 30 Apr UTC").
- DR16 BLOCKED — nytimes.com returns 403 to curl; Wayback holds only a 403 capture (20260623175004) and a revisit record, and all four Wayback fetches returned the NYT "Not Authorized" page. Nothing in the row could be checked.
- DR17 CONFIRMED — 20260703210324 donate: redesigned page with "We keep our evaluations independent and trustworthy by relying on support from a wide range of independent donors."; no employee parenthesis, no compensation footnote. (See wording-change note 2: the redesign is from February 2026, not July.)
- DR20 CONFIRMED — 20260804024601 donate carries "(METR cannot accept donations made by or at the direction of frontier AI company employees.)" under the every.org button; CDX confirms no donate capture of any digest between 20260703210324 and 20260804024601.
- DR21 CONFIRMED — 20260804074910 about: "(Note: METR cannot accept donations ... frontier AI company employees.)", Farhi/Ralston/Field/Newman named, and "significant free tokens" replacing "free compute credits" (last 'compute credits' about capture is 20260719232759).
- DR23 CONFIRMED — @METR_Evals post (Aug 14 2026, 11:13 PM as rendered): "We have not accepted funding from these companies, and we do not accept donations made by or at the direction of their staff. However, frontier AI companies currently provide a significant amount of free tokens ..." verbatim.
- DR24 CONFIRMED — @BethMayBarnes post (Aug 26 2026, 8:51 PM): "We haven't taken any funding from OpenAI or other AI companies (although they provide us free model access for eval execution and research)." Reply to @VarunGodbole; the linked about card carries the employee-donation note.
- DR25 CONFIRMED — Business Insider, Stephen Council, published 2026-09-11T23:01Z, headline "Ex-OpenAI researcher's nonprofit METR lands in AI's doom debate". Exact sentence: "While METR doesn't take money from the frontier AI labs or their employees, it accepts compute grants and works with them to analyze unreleased models."
- DR27 CONFIRMED (Epoch part) — epoch.ai/about/team lists Steve Newman under Board of directors. The OpenReview clause could not be re-checked (profile page is a JS shell; api2.openreview.net 403).

## Known gap closed: first donate capture with "compensation from AI companies"

CDX for metr.org/donate, 2025-04-01 to 2025-07-15, status 200 (`cdx-donate-20250401-20250715.json`): 13 captures, 12 unique digests. All 10 not-previously-fetched unique digests were fetched (`cdx-donate-2025MMDDhhmmss.html/.txt`) and every one returned 200.

- 20250401090802 — no footnote (already verified as DR05).
- **20250418224241 — EARLIEST capture containing the footnote**: "To date, April 2025, we have not accepted compensation from AI companies for the evaluations we have conducted." Body: "METR's work is funded entirely by donations like yours ... Being independently funded is also part of how we ensure that our research is as accurate as possible."
- 20250423215940, 20250501190757, 20250519102423, 20250524072658, 20250602162402, 20250609151201, 20250623135041, 20250701112553, 20250710175120, 20250711110620 — all carry the identical April-2025 footnote; no capture in the window has 'cannot accept' or the employee phrase.

So the compensation footnote first appears between 2025-04-01 and 2025-04-18 (consistent with its own "April 2025" dating), not 2025-07-11 as DR07's "first recovered" implies. DR07's source-column wording "first recovered compensation footnote" should be revised to point at 20250418224241, and DR07's note "2025-05/06 unique-digest HTML not all recovered" is now closed.

## Wording changes the Grok rows missed (from the unique-digest sweeps in `cdx-sweep-flags.csv`)

Sweep coverage: about page 2025-12-16 to 2026-09-13 (76 of 79 unique-digest captures recovered, listed in `about-cdx/`), donate page 2025-07-11 to 2026-09-04 (37 of 40 recovered, `donate-cdx/`). Three captures never returned (curl timeouts after 5 tries, not blocks): donate-cdx/20260830084232 donate-cdx/20260831014258 donate-cdx/20260904040318 ; each is bracketed by captures with identical flags, so no transition depends on them.

1. **David Farhi is never absent after 2025-12-16.** All 76 recovered about captures from 20251216013159 through 20260913105654 name him. No capture drops him.
2. **Donate redesign / footnote removal is February 2026, not July.** The "compensation from AI companies" footnote is present on every donate capture from 20250418224241 through 20260205085442. The redesigned "Donate to METR" page with no footnote first appears at 20260211194137. DR17 (2026-07-03) is therefore not the first footnote-less capture; the row's date should be read as "a" redesigned capture, with first-seen 2026-02-11.
3. **Donate body wording change 2025-10-02.** "METR's work is funded entirely by donations like yours ... Being independently funded ..." (Apr-Sep 2025) becomes "Donations like yours are crucial ... Support from a wide range of independent donors ..." at 20251002100351, and the footnote gains "However, companies have provided access and compute credits to enable evaluations and evaluation research." Last capture with the old wording: 20250910151728. DR11 is indeed the first capture with the new wording.
4. **Employee ban on the about page: first 20260719171236, confirmed; no earlier capture.** All 64 about captures from 20251216 through 20260714200544 lack the sentence; all 12 from 20260719171236 on carry it. DR18/DR19 stand.
5. **Employee ban on the donate page: first 20260804024601, confirmed.** 32 donate captures through 20260703210324 lack it; the 5 from 20260804024601 on carry it. DR20 stands.
6. **"free compute credits" to "free tokens" on the about page: between 20260719232759 and 20260804074910**, confirmed (DR21 stands). The donate page never uses either "free tokens" or "not accepted funding from AI companies".
7. The about page never carried the "compensation from AI companies" footnote or the "independent donors" phrase; those are donate-page-only wordings.

## Files

- `verification.csv` — row-level verdicts.
- `DR*-*.html/.txt` — the 17 fetched sources (+ DR03 PDF, DR13 2025-12-10 capture, DR14 abs page, DR16 Wayback attempts, DR27 OpenReview attempts).
- `cdx-donate-20250401-20250715.json`, `cdx-donate-2025*.html/.txt` — the May-June 2025 gap.
- `cdx-about-20251201-20260914.json`, `cdx-donate-20250711-20260914.json`, `about-cdx/`, `donate-cdx/`, `cdx-sweep-flags.csv` — the sweeps behind the wording-change notes.
- Note: `*.html.err` files are empty stderr side-files created by the shell environment around each curl call, not by the verification script; `DR25-businessinsider.html` is a byte-identical duplicate of `DR25-businessinsider-barnes.html` (same environment artifact).
