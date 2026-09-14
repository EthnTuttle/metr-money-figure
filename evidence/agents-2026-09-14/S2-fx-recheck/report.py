import csv, json, os
from collections import Counter, defaultdict
rs=list(csv.DictReader(open('recheck.csv')))
man={ (r['file'],r['row_id']):r for r in json.load(open('manifest.json')) }
files=['sacks_thread.csv','x_amplifiers.csv','metr_posts.csv','arrivals.csv','lab_mentions.csv','officials_mentions.csv','sep9.csv','independence_fight.csv']
L=[]
L.append('# S2 fxtwitter recheck — 2026-09-14\n')
L.append(f'Refetched every X status cited in eight research CSVs through api.fxtwitter.com (rows: {len(rs)}, unique IDs: {len({r["id"] for r in rs})}). Raw payloads in `json/<id>.json`; row-level results in `recheck.csv`.\n')
L.append('Excluded from sep9.csv because the url is not an X status: D10, D11, D12, D13, D19 (web articles) and D16 (profile link https://x.com/HoldenKarnofsky, no status id). independence_fight.csv rows without an x.com url were skipped per brief.\n')
L.append('Status key: OK = author, date and text all consistent (text_match yes or partial); DIFFERS = one of author/date/text disagrees; DELETED = fxtwitter returned no tweet (removed post or suspended/protected account); BLOCKED = no usable response after 3 tries.\n')
L.append('## Counts per file\n')
L.append('| file | rows | OK | DIFFERS | DELETED | BLOCKED | text=yes | text=partial |')
L.append('|---|---|---|---|---|---|---|---|')
tot=Counter()
for f in files:
    sub=[r for r in rs if r['file']==f]; c=Counter(r['status'] for r in sub); t=Counter(r['text_match'] for r in sub)
    L.append(f"| {f} | {len(sub)} | {c['OK']} | {c['DIFFERS']} | {c['DELETED']} | {c['BLOCKED']} | {t['yes']} | {t['partial']} |")
    tot.update(c)
L.append(f"| **all** | {len(rs)} | {tot['OK']} | {tot['DIFFERS']} | {tot['DELETED']} | {tot['BLOCKED']} | {sum(1 for r in rs if r['text_match']=='yes')} | {sum(1 for r in rs if r['text_match']=='partial')} |\n")
bad=[r for r in rs if r['status'] in ('DIFFERS','DELETED','BLOCKED')]
L.append('## DIFFERS / DELETED / BLOCKED rows\n')
if not bad: L.append('None.\n')
else:
    L.append('| file | row | id | handle in row | author | text | date | status | what differs |'); L.append('|---|---|---|---|---|---|---|---|---|')
    for r in bad:
        m=man[(r['file'],r['row_id'])]
        L.append(f"| {r['file']} | {r['row_id']} | {r['id']} | @{m['handle']} | {r['author_match']} | {r['text_match']} | {r['date_match']} | {r['status']} | {r['note']} |")
    L.append('')
part=[r for r in rs if r['status']=='OK' and r['text_match']=='partial']
if part:
    L.append('## Text = partial (status OK, listed for transparency)\n')
    L.append('| file | row | id | note |'); L.append('|---|---|---|---|')
    for r in part: L.append(f"| {r['file']} | {r['row_id']} | {r['id']} | {r['note']} |")
    L.append('')
L.append('## Ten largest view increases (absolute)\n')
def num(x):
    try: return float(x)
    except: return None
inc=[r for r in rs if num(r['stored_views']) is not None and num(r['fresh_views']) is not None]
seen=set(); top=[]
for r in sorted(inc,key=lambda r:num(r['fresh_views'])-num(r['stored_views']),reverse=True):
    if r['id'] in seen: continue
    seen.add(r['id']); top.append(r)
    if len(top)==10: break
L.append('| file | row | id | handle | stored views | fresh views | delta | delta % |'); L.append('|---|---|---|---|---|---|---|---|')
for r in top:
    m=man[(r['file'],r['row_id'])]; s=num(r['stored_views']); f=num(r['fresh_views'])
    L.append(f"| {r['file']} | {r['row_id']} | {r['id']} | @{m['handle']} | {int(s):,} | {int(f):,} | +{int(f-s):,} | {r['views_delta_pct']} |")
L.append('')
L.append('## Ten largest view increases (percent, stored views >= 1,000)\n')
seen=set(); topp=[]
for r in sorted([r for r in inc if num(r['stored_views'])>=1000],key=lambda r:num(r['views_delta_pct'] or 0),reverse=True):
    if r['id'] in seen: continue
    seen.add(r['id']); topp.append(r)
    if len(topp)==10: break
L.append('| file | row | id | handle | stored views | fresh views | delta % |'); L.append('|---|---|---|---|---|---|---|')
for r in topp:
    m=man[(r['file'],r['row_id'])]
    L.append(f"| {r['file']} | {r['row_id']} | {r['id']} | @{m['handle']} | {int(num(r['stored_views'])):,} | {int(num(r['fresh_views'])):,} | {r['views_delta_pct']} |")
L.append('')
dec=[r for r in inc if num(r['fresh_views'])<num(r['stored_views'])]
L.append(f'## Views that went down\n\n{len(dec)} rows have fresh views below stored views' + (':' if dec else '.'))
if dec:
    L.append(''); L.append('| file | row | id | stored | fresh |'); L.append('|---|---|---|---|---|')
    for r in dec: L.append(f"| {r['file']} | {r['row_id']} | {r['id']} | {r['stored_views']} | {r['fresh_views']} |")
L.append('')
dele=[r for r in rs if r['status']=='DELETED']
L.append('## Deleted posts / suspended or protected accounts\n')
if not dele: L.append('None: every fetched ID returned a live tweet.')
else:
    for r in dele:
        m=man[(r['file'],r['row_id'])]
        L.append(f"- {r['file']} {r['row_id']} id {r['id']} @{m['handle']}: {r['note']}")
prot=[r for r in rs if 'protected' in r['note']]
if prot:
    L.append('\nAccounts now protected (tweet still returned):'); 
    for r in prot: L.append(f"- {r['file']} {r['row_id']} id {r['id']}")
L.append('')
L.append('## Method\n')
L.append('- Fetch: `curl --max-time 20 https://api.fxtwitter.com/i/status/<id>`, ~2 requests/s, 30 s back-off on 429/5xx/timeouts, 3 tries then BLOCKED. Log in `fetch.log`, per-ID HTTP result in `fetch_status.json`.')
L.append('- author_match: fetched `tweet.author.screen_name` vs row handle (metr_posts.csv has no handle column so METR_Evals is assumed; sep9/independence_fight handle taken from the `(@handle)` in `actor`, falling back to the url path), case-insensitive.')
L.append('- text_match: stored text_200 / text_120 / event / metr_language vs fetched `tweet.text` after HTML-unescape, NFKC, quote/ellipsis folding, URL removal, leading @mention removal, whitespace collapse, lower-case. yes = first 100 chars match or every quoted fragment (split on ...) appears in the fetched text; partial = only a shorter window or a subset of fragments appears; no = nothing found.')
L.append('- date_match: UTC date (YYYY-MM-DD) of `tweet.created_timestamp` vs the date part of the row utc/utc_time.')
L.append('- views: `tweet.views` at fetch time vs the row views; delta % relative to stored.')
open('REPORT.md','w').write('\n'.join(L)+'\n')
print('report written',len(L),'lines')
