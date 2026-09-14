import json, subprocess, time, os, sys
rows=json.load(open('manifest.json'))
ids=sorted({r['id'] for r in rows})
os.makedirs('json',exist_ok=True)
log=open('fetch.log','a')
def L(s): log.write(time.strftime('%H:%M:%S ')+s+'\n'); log.flush()
status={}
for n,i in enumerate(ids):
    p=f'json/{i}.json'
    if os.path.exists(p) and os.path.getsize(p)>0:
        status[i]='cached'; continue
    ok=False
    for attempt in range(3):
        t0=time.time()
        r=subprocess.run(['curl','-s','--max-time','20','-w','\n%{http_code}','-H','User-Agent: Mozilla/5.0 (recheck)','https://api.fxtwitter.com/i/status/'+i],capture_output=True,text=True)
        body,_,code=r.stdout.rpartition('\n')
        code=code.strip()
        if code=='200' or code=='404':
            try: d=json.loads(body)
            except Exception: d=None
            if d is not None:
                open(p,'w').write(json.dumps(d,ensure_ascii=False))
                status[i]=code; ok=True; break
        L(f'{i} attempt {attempt+1} http={code} len={len(body)}')
        if code in ('429','500','502','503','000') or code=='':
            time.sleep(30)
        else:
            time.sleep(2)
    if not ok: status[i]='BLOCKED'; L(f'{i} BLOCKED')
    el=time.time()-t0
    if el<0.5: time.sleep(0.5-el)
    if n%50==0: L(f'progress {n}/{len(ids)}')
json.dump(status,open('fetch_status.json','w'),indent=0)
from collections import Counter
L('done '+str(Counter(status.values())))
