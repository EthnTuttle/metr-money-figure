"""Checks every figure exists and every row_id cited in a figure footnote/body exists in research CSVs. Exit 0 on pass."""
import csv, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ids=set()
for f in list((ROOT/'research').glob('*.csv'))+list((ROOT/'research'/'grok-out').glob('*.csv')):
    with open(f, newline='') as fh:
        lines=[l for l in fh if not l.startswith('#')]
        for r in csv.DictReader(lines):
            if r.get('row_id'): ids.add(r['row_id'].strip())
figs=sorted((ROOT/'figures').glob('metr-*.html'))
missing=[]; n=0
for h in figs:
    txt=re.sub(r' d="[^"]*"','',h.read_text())  # drop SVG path data, which contains tokens like C620
    for m in set(re.findall(r'\b([A-Z]{1,2}\d{2,3})\b', txt)):
        n+=1
        if m not in ids: missing.append((h.name,m))
pngs=[p for p in figs if p.with_suffix('.png').exists()]
print(f'figures={len(figs)} pngs={len(pngs)} row_ids_in_research={len(ids)} cited={n} missing={len(missing)}')
for x in missing[:20]: print('MISSING',x)
sys.exit(0 if len(figs)==len(pngs) and not missing else 1)
