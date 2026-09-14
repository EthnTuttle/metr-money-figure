import json, csv, re, html, unicodedata, os, datetime
rows=json.load(open('manifest.json'))
fstat=json.load(open('fetch_status.json')) if os.path.exists('fetch_status.json') else {}
URL=re.compile(r'https?://\S+')
def norm(s):
    s=html.unescape(s or ''); s=unicodedata.normalize('NFKC',s)
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('…','...')
    s=URL.sub('',s)
    s=re.sub(r'^(\s*@\w+)+\s*','',s)
    s=re.sub(r'\s+',' ',s).strip().lower()
    return s
def fragments(s):
    # quoted fragments in event/metr_language style cells
    q=re.findall(r"'([^']{12,})'|\"([^\"]{12,})\"",s or '')
    out=[]
    for a,b in q:
        for piece in re.split(r'\.\.\.|…',a or b):
            piece=norm(piece).strip(' .,;:')
            if len(piece)>=12: out.append(piece)
    return out
def text_match(stored,fetched):
    ns,nf=norm(stored),norm(fetched)
    if not ns: return 'partial','stored text empty'
    a=ns[:100].rstrip(' .')
    if nf.startswith(a) or a in nf: return 'yes',''
    frs=fragments(stored)
    if frs:
        hit=[f for f in frs if f in nf]
        if len(hit)==len(frs): return 'yes',''
        if hit: return 'partial',f'{len(hit)}/{len(frs)} quoted fragments found'
        # try looser: 25-char windows of each fragment
        for f in frs:
            if any(f[i:i+25] in nf for i in range(0,max(1,len(f)-25),5)): return 'partial','fragment partly found'
        return 'no','quoted fragments not in fetched text'
    # no quotes: check first 40 chars, or any 30-char window of stored text
    if nf.startswith(ns[:40]) or ns[:40] in nf: return 'partial','first 40 chars match, diverges later'
    for i in range(0,max(1,len(ns)-30),10):
        if ns[i:i+30] in nf: return 'partial','a 30-char window of stored text found'
    return 'no','stored text not found in fetched text'
def row_date(u):
    m=re.match(r'(\d{4}-\d{2}-\d{2})',u or ''); return m.group(1) if m else ''
out=[]
for r in rows:
    p=f"json/{r['id']}.json"
    rec=dict(file=r['file'],row_id=r['row_id'],id=r['id'],author_match='',text_match='',date_match='',stored_views=r['views'],fresh_views='',views_delta_pct='',status='',note='')
    if not os.path.exists(p):
        rec['status']='BLOCKED'; rec['note']='no fxtwitter response after 3 tries'; out.append(rec); continue
    d=json.load(open(p))
    if d.get('code')!=200 or 'tweet' not in d:
        rec['status']='DELETED'; rec['note']=f"fxtwitter code {d.get('code')} {d.get('message')}"
        out.append(rec); continue
    t=d['tweet']; au=t.get('author',{}) or {}
    sn=au.get('screen_name','') or ''
    rec['author_match']='yes' if sn.lower()==r['handle'].lower() else 'no'
    notes=[]
    if rec['author_match']=='no': notes.append(f"author @{sn} vs row @{r['handle']}")
    tm,tn=text_match(r['text'],t.get('text',''))
    rec['text_match']=tm
    if tn: notes.append(tn)
    fd=''
    try: fd=datetime.datetime.fromtimestamp(t['created_timestamp'],datetime.timezone.utc).strftime('%Y-%m-%d')
    except Exception: pass
    rd=row_date(r['utc'])
    rec['date_match']='yes' if fd and fd==rd else 'no'
    if rec['date_match']=='no': notes.append(f'fetched date {fd} vs row {rd}')
    fv=t.get('views'); rec['fresh_views']=fv if fv is not None else ''
    try:
        sv=float(r['views'])
        if fv is not None and sv>0: rec['views_delta_pct']=f"{(fv-sv)/sv*100:.1f}"
    except Exception: pass
    if au.get('protected'): notes.append('author account protected')
    rec['status']='OK' if (rec['author_match']=='yes' and tm in('yes','partial') and rec['date_match']=='yes') else 'DIFFERS'
    if tm=='partial' and rec['status']=='OK': rec['status']='OK'
    rec['note']='; '.join(notes)
    out.append(rec)
cols=['file','row_id','id','author_match','text_match','date_match','stored_views','fresh_views','views_delta_pct','status','note']
with open('recheck.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(out)
from collections import Counter
print(Counter(r['status'] for r in out)); print(Counter(r['text_match'] for r in out))
