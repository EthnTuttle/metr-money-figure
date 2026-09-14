"""Shared render + tokens for the Coxon provenance figures (same surface as anthropic-investors set)."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT/'figures'
BG='#f7f4ee'; INK='#191b1a'; MUTED='#666960'; GRID='#e3dfd5'; AXIS='#c3c2b7'
BLUE='#2a78d6'; ORANGE='#eb6834'; AQUA='#1baf7a'; YELLOW='#eda100'; RED='#e34948'
BLUE250='#86b6ef'; BLUE450='#2a78d6'; GRAY='#b2b4aa'; LGRAY='#dcd9cf'
GOOD='#0ca30c'; GOODTXT='#006300'; CRIT='#d03b3b'; WARN='#fab219'; WARNTXT='#8a5a00'

def esc(s): return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def fmt_views(v):
    v=float(v)
    if v>=1e6: return f'{v/1e6:.1f}M' if v<10e6 else f'{v/1e6:.0f}M'
    if v>=1e3: return f'{v/1e3:.0f}K'
    return f'{v:.0f}'

def money(v):
    v=float(v)
    if v>=1e6: return f'${v/1e6:,.1f}M' if v<100e6 else f'${v/1e6:,.0f}M'
    if v>=1e3: return f'${v/1e3:,.0f}K'
    return f'${v:,.0f}'

def render(stem, document, width, height):
    FIGURES.mkdir(exist_ok=True)
    path=FIGURES/(stem+'.html'); path.write_text(document)
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':width,'height':height},device_scale_factor=2)
        pg.goto(path.as_uri(),wait_until='networkidle'); pg.evaluate('document.fonts.ready')
        ov=pg.evaluate('({w:document.documentElement.scrollWidth,h:document.documentElement.scrollHeight})')
        assert ov['w']<=width and ov['h']<=height, (stem,ov)
        box=pg.locator('.footnote').bounding_box(); assert box and box['y']+box['height']<=height,(stem,box)
        pg.screenshot(path=str(FIGURES/(stem+'.png'))); b.close()
    im=Image.open(FIGURES/(stem+'.png')).convert('RGB'); im.save(FIGURES/(stem+'.jpg'),quality=94)
    print('rendered',stem,im.size)

def shell(title,kicker,subtitle,body,footnote,width,height,extra_css=''):
    import re
    kicker=re.sub(r'^\s*Figure\s+\S+(?:\s*\([^)]*\))?\s*[·:—-]\s*','',kicker)   # no figure numbering on the rendered kicker
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{esc(title)}</title><style>
*{{box-sizing:border-box}}html,body{{margin:0;width:{width}px;height:{height}px;background:{BG}}}
body{{padding:46px 60px 32px;font-family:Arial,Helvetica,sans-serif;color:{INK};display:flex;flex-direction:column}}
.kicker{{font-size:17px;letter-spacing:2.8px;text-transform:uppercase;color:{MUTED};font-weight:bold}}
h1{{font-size:48px;letter-spacing:-1.4px;margin:12px 0 10px;line-height:1.07}}
.subtitle{{font-size:23px;line-height:1.35;color:{MUTED};margin:0 0 16px;max-width:1900px}}
.legend{{display:flex;gap:28px;font-size:19px;color:{INK};margin:0 0 10px;flex-wrap:wrap}}
.legend span{{display:inline-flex;align-items:center;gap:9px}}.sw{{width:18px;height:18px;border-radius:4px;display:inline-block}}
.footnote{{margin-top:auto;border-top:1px solid #cdcfc6;padding-top:14px;font-size:16px;line-height:1.45;color:{MUTED}}}
.footnote b{{color:{INK}}}svg{{display:block}}text{{font-family:Arial,Helvetica,sans-serif}}
.kpis{{display:flex;gap:26px;margin:4px 0 18px}}.kpi{{background:#efece4;border-radius:10px;padding:16px 22px;min-width:300px}}
.kpi .l{{font-size:16px;color:{MUTED};letter-spacing:1px;text-transform:uppercase;font-weight:bold}}.kpi .v{{font-size:44px;font-weight:bold;letter-spacing:-1px;margin-top:4px}}
.kpi .d{{font-size:17px;color:{MUTED};margin-top:4px}}{extra_css}
</style></head><body><div class="kicker">{esc(kicker)}</div><h1>{title}</h1><p class="subtitle">{subtitle}</p>{body}<div class="footnote">{footnote}</div></body></html>'''

def legend(items):
    return '<div class="legend">'+''.join(f'<span><i class="sw" style="background:{c}"></i>{esc(t)}</span>' for c,t in items)+'</div>'


_ID=r'[A-Z]{1,2}\d{2,3}(?:[–-][A-Z]{0,2}\d{2,3})?'
def strip_ids(text):
    """Remove visible row-id tags like (ST91), (ST32–ST33, IV10), ', ST124)' from figure text; the ids are kept elsewhere for the audit.
    Only text between tags is touched: SVG attributes (path data such as M700,200 C915,110) must never be edited."""
    import re
    parts=re.split(r'(<[^>]+>)', text)
    return ''.join(p if p.startswith('<') else _strip_ids_text(p) for p in parts)
STRIP_IDS=False; STRIPPED_IDS=set()
def _strip_ids_text(text):
    import re
    STRIPPED_IDS.update(collect_ids(text))
    text=re.sub(r'\s*\((?:'+_ID+r'(?:[,;]\s*)?)+\)', '', text)          # (ST91) / (ST32–ST33, ST92, IV10)
    text=re.sub(r',\s*(?:'+_ID+r')(?:,\s*'+_ID+r')*(?=\))', '', text)      # (Tuna chairs it, ST124)
    text=re.sub(r';\s*(?:'+_ID+r')(?:,\s*'+_ID+r')*(?=\))', '', text)
    text=re.sub(r'\s*\b(?:rows?\s+)?'+_ID+r'(?:,\s*'+_ID+r')*\b(?=[.;,)])', '', text)  # stray "ST54–ST55" before punctuation
    text=re.sub(r'\s*\b(?:see\s+)?'+_ID+r'(?:\s*[,;/]\s*'+_ID+r')*\b', '', text)       # any remaining bare id
    return text
def collect_ids(text):
    import re
    text=re.sub(r'<[^>]+>',' ',text)   # text only: SVG path data like L562 must not count
    return sorted(set(re.findall(r'\b(?:ST|RW|IV|AP|TB|TO|LD|HF|EV|DR|IF|SK|AE|PY|M|G|J|K|S|B|N|D|X|C)\d{2,3}(?:[–-][A-Z]{0,2}\d{2,3})?\b', text)))
