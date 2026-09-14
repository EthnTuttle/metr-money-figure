# METR money figure — "Money that doesn't show up, with Anthropic"

One figure, and everything under it: the funders that reach METR (Model Evaluation and Threat Research) through its parent, its joint-project partner, its pooled-fund donor, a board member's organization, its contractor, its office and a journalism fellowship; the same funders' Anthropic equity; and the donated Moskovitz stake whose location no public filing identifies.

- `figures/metr-01b-money-that-doesnt-show-up-with-anthropic.{html,png,jpg}` — the figure (10a-anthropic).
- `figures/metr-01-money-that-doesnt-show-up.{html,png,jpg}` — the companion without the Anthropic panel (10a).
- `NOTES.md` — the full coverage notes the figure used to carry as its footnote. Read this before quoting a number.
- `research/*.csv` — every row the figure cites, by row id (money_flows M…, stakes ST…, investments IV…, audacious-partners AP…, budget G…, tarbell_funding TB…, tarbell_outlets TO…, redwood RW…, shared_donors J…, board B…, compute_inkind K…, staff_origins S…). Each row carries its source URL, a verbatim quote and a note.
- `research/STATE.md` — the consolidated open-question list, including where the donated stake could sit and what would settle it.
- `research/AUDIT-3A.md` … `AUDIT-3D.md` — four independent audits of this figure run on 2026-09-14 (money pipes; Anthropic and the stake; Canary and Tarbell; framing and layout), with their seeds `AUDIT-SEED-3*.md`. Their verdicts were applied to the figure in v0.44.
- `evidence/` — primary documents: Good Ventures Foundation's FY2024 and FY2025 Forms 990-PF (IRS e-file XML, Schedule B included), Coefficient's 2024 returns, SEC filings, Moskovitz's public statements (Bluesky API payloads, Stratechery archive), the audit evidence registers, and the agent review reports.
- `MANIFEST.csv` — path, size and SHA-256 for every evidence file, including the ones too large for the repo (the DAF-sponsor e-files, 436 MB; the IRS TEOS PDFs, 74 MB; large audit captures). Those are IRS public files; the manifest gives the object ids so anyone can pull them from `apps.irs.gov/pub/epostcard/990/xml/` and check the hash.
- `scripts/` — the render code. `generate.py` holds the whole pack's figures; this figure is `fig_money(anth=True)`. Rendering needs Python 3, Playwright with Chromium, and the research CSVs in place:

```
python3 scripts/generate.py metr-01b-money-that-doesnt-show-up-with-anthropic
python3 scripts/audit.py   # checks every cited row id exists
```

## Rules the figure follows

- Every number traces to a row id in `research/`. No number is on the figure without one.
- Money types are never summed with each other: Coefficient awards, SFF recommendations, the Audacious commitment, filed DAF grants and equity values stay separate, and the legend says which is which.
- Pipe width is 6 px + 1.4 px per $1M, no cap. The Anthropic equity band is a ceiling (Forbes' "less than 0.8%" × the $965B Series H post-money valuation), not a valuation, and is drawn at 1/30 of that scale because at full scale it would be five canvases wide.
- Negatives are bounded: "none found" means none in the sources named, with their dates.
- The accounts at SVCF and NPT that pay Coefficient-recommended grants are unattributed. No public document names their principals or the recipient of the donated Anthropic shares. The figure says so wherever it touches them.
- No motive is asserted about any person or organization. Only public people acting in public roles are named.

## Disclosure

Built by Kevin Bass (@kevinnbass), who has publicly criticized Anthropic and Coefficient Giving. Data collection and rendering were done with Claude Code (Anthropic) and audited with OpenAI Codex and xAI Grok agents; the audit reports and every agent's evidence are in this repo so the reader can check the work rather than trust the author or the tools. Corrections: open an issue with the row id.

## Version

v0.45, 2026-09-14. Changes are logged in the parent pack's CHANGELOG; the audits that shaped this version are in `research/AUDIT-3*.md`.
