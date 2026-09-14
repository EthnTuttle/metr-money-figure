import csv, re, json, sys
OUT='agents-2026-09-14/S2-fx-recheck/manifest.json'
rows=[]
def add(file,row_id,id_,handle,text,utc,views):
    rows.append(dict(file=file,row_id=row_id,id=id_,handle=(handle or '').strip().lstrip('@'),text=text or '',utc=utc or '',views=views or ''))
def rd(f): return list(csv.DictReader(open(f,encoding='utf-8-sig')))
for r in rd('sacks_thread.csv'): add('sacks_thread.csv',r['row_id'],r['id'],r['handle'],r['text_200'],r['utc'],r['views'])
for r in rd('x_amplifiers.csv'): add('x_amplifiers.csv',r['row_id'],r['id'],r['handle'],r.get('text_120') or r.get('text_200'),r['utc'],r['views'])
for r in rd('metr_posts.csv'): add('metr_posts.csv',r['row_id'],r['id'],'METR_Evals',r['text_200'],r['utc'],r['views'])
for r in rd('arrivals.csv'): add('arrivals.csv',r['row_id'],r['id'],r['handle'],r['text_200'],r['utc'],r['views'])
for r in rd('lab_mentions.csv'): add('lab_mentions.csv',r['row_id'],r['id'],r['handle'],r['text_200'],r['utc'],r['views'])
for r in rd('officials_mentions.csv'): add('officials_mentions.csv',r['row_id'],r['id'],r['handle'],r['text_200'],r['utc'],r['views'])
hre=re.compile(r'\(@([A-Za-z0-9_]+)\)')
for r in rd('sep9.csv'):
    m=re.search(r'/status/(\d+)',r['url'] or '')
    if not m: print('sep9 no id',r['row_id'],r['url']); continue
    h=hre.search(r['actor'] or ''); hu=re.search(r'x\.com/([A-Za-z0-9_]+)/status',r['url'])
    add('sep9.csv',r['row_id'],m.group(1),(h.group(1) if h else (hu.group(1) if hu else '')),r['event'],r['utc_time'],r['views'])
for r in rd('independence_fight.csv'):
    u=r['url'] or ''
    if 'x.com/' not in u: continue
    m=re.search(r'/status/(\d+)',u)
    if not m: print('IF no id',r['row_id'],u); continue
    h=hre.search(r['actor'] or ''); hu=re.search(r'x\.com/([A-Za-z0-9_]+)/status',u)
    add('independence_fight.csv',r['row_id'],m.group(1),(h.group(1) if h else (hu.group(1) if hu else '')),r['metr_language'] or r['event'],r['utc'],r['views'])
json.dump(rows,open(OUT,'w'),indent=0)
from collections import Counter
print(Counter(r['file'] for r in rows)); print('total rows',len(rows),'unique ids',len({r['id'] for r in rows}))
print('rows with empty handle:',[(r['file'],r['row_id']) for r in rows if not r['handle']])
