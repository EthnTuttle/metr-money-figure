# Sources tried and not retrievable (S11-stakes, 2026-09-14)

Fetch-only session; no host retried more than 3 times. WebSearch budget was exhausted after the first 10 queries, so everything after that was located by direct URL, Wayback CDX lookups, CourtListener RECAP search, ProPublica Nonprofit Explorer, and links embedded in already-fetched pages.

| Source | What was wanted | Result |
|---|---|---|
| app.dealroom.co note "Jaan Tallinn: The Quiet Force Behind AI's Biggest Bets" | "$623M post" Series A valuation and "roughly 250x" return claim | Cloudflare challenge on direct, r.jina.ai and WebFetch; not in Wayback CDX. Only the search-engine snippet exists (recorded in stakes.csv as unverified). |
| forbes.com/profile/jaan-tallinn/ | Forbes net-worth attribution | "The Wayback Machine has not archived that URL" - Forbes appears to carry no Tallinn profile. |
| bloomberg.com/billionaires/profiles/eric-e-schmidt/ | Bloomberg methodology note | Wayback capture is Bloomberg's "Are you a robot?" page. |
| Äripäev original interview (autumn 2025) and Äripäeva raadio (Jan 2026) with Tallinn | Direct quotes on Metaplanet dilution / board observer | aripaev.ee search page returned no article list; CDX prefix searches found no aripaev.ee URL with "anthropic". The quotes survive second-hand in Postimees 2026-02-22 (docs/postimees-tallinn.html). |
| ERR (news.err.ee) | Tallinn/Anthropic coverage | search page empty; CDX query timed out (504). |
| Kroll FTX docket "Sale Documents" listing | Full list of Anthropic sale filings | Page is JS-rendered; docket keyword search redirects. Individual PDFs were reachable by id (Doc 6952, 7590, 7782-1, 16380) and Doc 10241 came from CourtListener RECAP. |
| sec.gov Amazon 10-Q (Q2 2026) | raw HTML | sec.gov refuses undeclared curl; WebFetch quotes saved in amzn-10q-2026q2-webfetch-notes.txt. |
| The Information 2025-05-02 buyback story | $56.09 per share original | Wayback capture is paywalled shell (headline only, saved). Price taken from Maginative's summary of it. |
| WSJ 2026-06-20 Jane Street profile | Anthropic stake wording | URL unknown; CDX for wsj.com "jane-street" found nothing. Secondary: AI Weekly 2026-06-21. |
| Bloomberg 2026-05-18 "Anthropic sends jolt through the market for buying shares in the hottest pre-IPO startups" | tender/secondary per-share prices | Wayback capture is robot page. |
| CNBC 2025-01-21 Hillspire | (retrieved) | OK. |
| Business Insider 2026-08-31 | (retrieved, incl. articleBody) | OK. |
| ProPublica search "Emerging Risk Research" / "Macroscopic Ventures" | US 990 for CERR/Macroscopic | zero organizations returned (may be non-US or differently named). |
| SDNY Docs 510 and 532 (Ellison / Singh forfeiture orders) | text | scanned PDFs; pages were read visually (Read tool) and transcribed; no OCR tool available. |
