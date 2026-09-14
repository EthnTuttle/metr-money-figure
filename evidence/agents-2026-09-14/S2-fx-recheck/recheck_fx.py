#!/usr/bin/env python3
"""Refetch every X post cited in the S2 CSVs via api.fxtwitter.com and compare
author / text / date / views against the stored rows.  Fetch-only; writes only
under agents-2026-09-14/S2-fx-recheck/.  Resumable: IDs with a saved JSON are
not refetched (BLOCKED markers are retried)."""
import csv, json, os, re, sys, time, difflib, urllib.request, urllib.error
from datetime import datetime, timezone

RES = '/mnt/f/projects/memes/ai-machine/10-metr/research'
OUT = os.path.join(RES, 'agents-2026-09-14', 'S2-fx-recheck')
JDIR = os.path.join(OUT, 'json')
os.makedirs(JDIR, exist_ok=True)
PAUSE, TIMEOUT, RETRY_SLEEP, MAX_TRIES = 0.5, 20, 30, 3
UA = 'Mozilla/5.0 (X11; Linux x86_64) memes-research-recheck/1.0'

FILES = ['sacks_thread.csv', 'x_amplifiers.csv', 'metr_posts.csv', 'arrivals.csv',
         'lab_mentions.csv', 'officials_mentions.csv', 'sep9.csv', 'independence_fight.csv']

def norm(s):
    return re.sub(r'\s+', ' ', (s or '')).strip()

def handle_from(row):
    if row.get('handle'):
        return row['handle'].strip().lstrip('@')
    m = re.search(r'@([A-Za-z0-9_]+)', row.get('actor', '') or '')
    if m:
        return m.group(1)
    m = re.search(r'x\.com/([A-Za-z0-9_]+)/status/', row.get('url', '') or '')
    return m.group(1) if m else ''

def load_rows():
    rows = []
    for f in FILES:
        with open(os.path.join(RES, f), encoding='utf-8', newline='') as fh:
            for r in csv.DictReader(fh):
                if 'id' in r and r['id'].strip():
                    sid = r['id'].strip()
                elif 'x.com/' in (r.get('url') or ''):
                    m = re.search(r'/status/(\d+)', r['url'])
                    if not m:
                        continue
                    sid = m.group(1)
                else:
                    continue
                handle = handle_from(r)
                if f == 'metr_posts.csv' and not handle:
                    handle = 'METR_Evals'
                text = r.get('text_200') or r.get('text_120') or r.get('metr_language') or r.get('event') or ''
                textcol = 'text_200' if r.get('text_200') else 'text_120' if r.get('text_120') else \
                          'metr_language' if r.get('metr_language') else 'event' if r.get('event') else ''
                utc = r.get('utc') or r.get('utc_time') or ''
                views = (r.get('views') or '').strip()
                rows.append(dict(file=f, row_id=r['row_id'], id=sid, handle=handle, text=text,
                                 textcol=textcol, utc=utc, views=views))
    return rows

# ---------------------------------------------------------------- fetching
def fetch_one(sid):
    url = f'https://api.fxtwitter.com/i/status/{sid}'
    last = None
    for attempt in range(1, MAX_TRIES + 1):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                body = resp.read().decode('utf-8', 'replace')
                return json.loads(body), resp.status
        except urllib.error.HTTPError as e:
            body = ''
            try:
                body = e.read().decode('utf-8', 'replace')
            except Exception:
                pass
            if e.code == 429:
                last = f'HTTP 429 (attempt {attempt})'
                time.sleep(RETRY_SLEEP)
                continue
            try:
                return json.loads(body), e.code
            except Exception:
                return {'code': e.code, 'message': body[:200] or e.reason}, e.code
        except (urllib.error.URLError, TimeoutError, ConnectionError, OSError, json.JSONDecodeError) as e:
            last = f'{type(e).__name__}: {e} (attempt {attempt})'
            time.sleep(RETRY_SLEEP)
            continue
    return {'code': 'BLOCKED', 'message': last}, 0

def fetch_all(ids):
    todo = []
    for sid in ids:
        p = os.path.join(JDIR, sid + '.json')
        if os.path.exists(p):
            try:
                d = json.load(open(p, encoding='utf-8'))
                if d.get('code') != 'BLOCKED':
                    continue
            except Exception:
                pass
        todo.append(sid)
    print(f'{len(ids)} unique ids, {len(todo)} to fetch', flush=True)
    for i, sid in enumerate(todo, 1):
        d, status = fetch_one(sid)
        d['_fetched_at'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
        d['_http_status'] = status
        with open(os.path.join(JDIR, sid + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(d, fh, ensure_ascii=False, indent=1)
        tag = d.get('code')
        print(f'[{i}/{len(todo)}] {sid} http={status} code={tag}', flush=True)
        time.sleep(PAUSE)

# ---------------------------------------------------------------- comparing
def fragments(text):
    """quoted fragments inside an event / metr_language cell, split on ellipses"""
    frs = []
    for q in re.findall(r"'([^']{12,})'|\"([^\"]{12,})\"|“([^”]{12,})”", text):
        for g in q:
            if g:
                frs.extend(p for p in re.split(r'\s*(?:\.\.\.|…)\s*', g) if len(norm(p)) >= 12)
    return frs

def text_match(stored, fetched, textcol):
    s, t = norm(stored), norm(fetched)
    sl, tl = s.lower(), t.lower()
    if not s:
        return 'no', 'no stored text'
    if sl[:100] == tl[:100]:
        return 'yes', ''
    if textcol in ('metr_language',):
        parts = [p for p in re.split(r'\s*(?:\.\.\.|…)\s*', s) if len(norm(p)) >= 12] or [s]
        hit = sum(1 for p in parts if norm(p).lower() in tl)
        if hit == len(parts):
            return 'yes', 'quoted fragment present'
        if hit:
            return 'partial', f'{hit}/{len(parts)} quoted fragments present'
    frs = fragments(s)
    if frs:
        hit = sum(1 for p in frs if norm(p).lower() in tl)
        if hit == len(frs):
            return 'yes', 'quoted fragment present'
        if hit:
            return 'partial', f'{hit}/{len(frs)} quoted fragments present'
    # tolerate t.co / link stripping and truncation differences
    strip = lambda x: re.sub(r'https?://\S+', '', x)
    a, b = norm(strip(sl)), norm(strip(tl))
    if a and (a[:100] == b[:100] or (len(a) >= 40 and a[:80] in b)):
        return 'yes', 'matches after link stripping'
    ratio = difflib.SequenceMatcher(None, sl[:200], tl[:200]).ratio()
    if ratio >= 0.6 or sl[:40] == tl[:40]:
        return 'partial', f'prefix similarity {ratio:.2f}'
    if textcol == 'event':
        return 'partial', 'event is a paraphrase, no quoted fragment to check'
    return 'no', f'prefix similarity {ratio:.2f}'

def parse_stored_date(u):
    u = (u or '').strip()
    m = re.match(r'(\d{4}-\d{2}-\d{2})', u)
    return m.group(1) if m else ''

def compare(rows):
    out = []
    for r in rows:
        p = os.path.join(JDIR, r['id'] + '.json')
        rec = dict(file=r['file'], row_id=r['row_id'], id=r['id'], author_match='', text_match='',
                   date_match='', stored_views=r['views'], fresh_views='', views_delta_pct='',
                   status='', note='')
        d = None
        if os.path.exists(p):
            try:
                d = json.load(open(p, encoding='utf-8'))
            except Exception:
                d = None
        if d is None or d.get('code') == 'BLOCKED':
            rec['status'] = 'BLOCKED'
            rec['note'] = (d or {}).get('message', 'no json saved') or 'fetch failed'
            out.append(rec); continue
        if not d.get('tweet'):
            code, msg = d.get('code'), d.get('message', '')
            if code in (404, '404') or 'NOT_FOUND' in str(msg):
                rec['status'] = 'DELETED'; rec['note'] = f'fxtwitter {code} {msg}: post deleted, or account suspended/private'
            elif code in (401, '401') or 'PRIVATE' in str(msg):
                rec['status'] = 'DELETED'; rec['note'] = f'fxtwitter {code} {msg}: account protected/private'
            else:
                rec['status'] = 'BLOCKED'; rec['note'] = f'fxtwitter {code} {msg}'
            out.append(rec); continue
        t = d['tweet']
        sn = (t.get('author') or {}).get('screen_name', '')
        rec['author_match'] = 'yes' if sn.lower() == r['handle'].lower() else 'no'
        notes = []
        if rec['author_match'] == 'no':
            notes.append(f'author @{sn} vs stored @{r["handle"]}')
        tm, tnote = text_match(r['text'], t.get('text', ''), r['textcol'])
        rec['text_match'] = tm
        if tm != 'yes':
            notes.append(f'text[{r["textcol"]}] {tnote}: fetched="{norm(t.get("text",""))[:90]}"')
        elif tnote:
            pass
        fd = ''
        try:
            fd = datetime.strptime(t['created_at'], '%a %b %d %H:%M:%S %z %Y').astimezone(timezone.utc).strftime('%Y-%m-%d')
        except Exception:
            try:
                fd = datetime.fromtimestamp(t['created_timestamp'], timezone.utc).strftime('%Y-%m-%d')
            except Exception:
                pass
        sd = parse_stored_date(r['utc'])
        rec['date_match'] = 'yes' if (sd and fd and sd == fd) else 'no'
        if rec['date_match'] == 'no':
            notes.append(f'date fetched {fd} vs stored {sd or r["utc"]}')
        fv = t.get('views')
        rec['fresh_views'] = '' if fv is None else str(fv)
        try:
            sv = int(float(r['views'].replace(',', '')))
            if fv is not None and sv > 0:
                rec['views_delta_pct'] = f'{(fv - sv) / sv * 100:.1f}'
            elif fv is not None and sv == 0:
                rec['views_delta_pct'] = ''
        except ValueError:
            pass
        bad = rec['author_match'] == 'no' or rec['text_match'] == 'no' or rec['date_match'] == 'no'
        rec['status'] = 'DIFFERS' if bad else 'OK'
        if rec['text_match'] == 'partial' and not bad:
            notes.append('partial text match only (see text note)')
        rec['note'] = ' | '.join(notes)
        out.append(rec)
    return out

def main():
    rows = load_rows()
    ids = sorted({r['id'] for r in rows})
    print(f'{len(rows)} rows across {len(FILES)} files', flush=True)
    if '--compare-only' not in sys.argv:
        fetch_all(ids)
    res = compare(rows)
    with open(os.path.join(OUT, 'recheck.csv'), 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['file', 'row_id', 'id', 'author_match', 'text_match', 'date_match',
                                           'stored_views', 'fresh_views', 'views_delta_pct', 'status', 'note'])
        w.writeheader(); w.writerows(res)
    from collections import Counter
    print(Counter((r['file'], r['status']) for r in res), flush=True)
    print('DONE', flush=True)

if __name__ == '__main__':
    main()
