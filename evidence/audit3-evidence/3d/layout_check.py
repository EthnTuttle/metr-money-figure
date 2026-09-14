#!/usr/bin/env python3
"""Reproduce the seed's SVG layout checks against the rendered HTML."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path

from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
HTML = ROOT / "figures" / "metr-01b-money-that-doesnt-show-up-with-anthropic.html"
PNG = ROOT / "figures" / "metr-01b-money-that-doesnt-show-up-with-anthropic.png"


def intersects(text: dict, rect: dict) -> bool:
    return (
        text["bx"] < rect["x"] + rect["w"]
        and text["bx"] + text["bw"] > rect["x"]
        and text["by"] < rect["y"] + rect["h"]
        and text["by"] + text["bh"] > rect["y"]
    )


def owned(text: dict, rect: dict) -> bool:
    return abs(text["x"] - (rect["x"] + 22)) < 0.1 and rect["y"] < text["y"] < rect["y"] + rect["h"] + 20


def main() -> None:
    screenshot = OUT / "rendered-check.png"
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 2200, "height": 2600}, device_scale_factor=2)
        page.goto(HTML.as_uri(), wait_until="load")
        page.evaluate("document.fonts.ready")
        data = page.locator("svg").evaluate(
            """svg => {
              const nodes=[...svg.querySelectorAll('rect')]
                .filter(r=>r.getAttribute('opacity')==='0.13')
                .map((r,i)=>({i,x:+r.getAttribute('x'),y:+r.getAttribute('y'),w:+r.getAttribute('width'),h:+r.getAttribute('height')}));
              const texts=[...svg.querySelectorAll('text')].map((t,i)=>{const b=t.getBBox(); return {
                i,text:t.textContent,x:+t.getAttribute('x'),y:+t.getAttribute('y'),bx:b.x,by:b.y,bw:b.width,bh:b.height
              }});
              const path=[...svg.querySelectorAll('path')].find(p=>p.getAttribute('d').startsWith('M700,610 C950,610'));
              const points=[]; const length=path.getTotalLength();
              for(let i=0;i<=20000;i++){const p=path.getPointAtLength(length*i/20000);points.push([p.x,p.y]);}
              return {nodes,texts,points,strokeWidth:+path.getAttribute('stroke-width')};
            }"""
        )
        page.screenshot(path=str(screenshot))
        browser.close()

    node_rows = []
    for rect in data["nodes"]:
        own = [text for text in data["texts"] if owned(text, rect)]
        title = own[0]["text"] if own else "?"
        subtitle_lines = max(0, len(own) - 1)
        required = subtitle_lines * 21 + 62
        node_rows.append(
            {
                "node": title,
                "x": rect["x"],
                "y": rect["y"],
                "width": rect["w"],
                "height": rect["h"],
                "subtitle_lines": subtitle_lines,
                "required_height": required,
                "margin": rect["h"] - required,
                "verdict": "PASS" if required <= rect["h"] else "FAIL",
            }
        )
    with (OUT / "node-heights.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(node_rows[0]))
        writer.writeheader()
        writer.writerows(node_rows)

    collision_rows = []
    for text in data["texts"]:
        for rect in data["nodes"]:
            if intersects(text, rect) and not owned(text, rect):
                collision_rows.append(
                    {
                        "label": text["text"],
                        "text_bbox": f"[{text['bx']:.2f},{text['by']:.2f}]-[{text['bx']+text['bw']:.2f},{text['by']+text['bh']:.2f}]",
                        "node_index": rect["i"],
                        "overlap_bbox": f"[{max(text['bx'],rect['x']):.2f},{max(text['by'],rect['y']):.2f}]-[{min(text['bx']+text['bw'],rect['x']+rect['w']):.2f},{min(text['by']+text['bh'],rect['y']+rect['h']):.2f}]",
                    }
                )
    with (OUT / "label-collisions.csv").open("w", newline="", encoding="utf-8") as stream:
        fields = ["label", "text_bbox", "node_index", "overlap_bbox"]
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(collision_rows)

    longview = next(rect for rect in data["nodes"] if rect["x"] == 1130 and rect["y"] == 460)

    def distance(point: list[float]) -> float:
        x, y = point
        dx = max(longview["x"] - x, 0, x - (longview["x"] + longview["w"]))
        dy = max(longview["y"] - y, 0, y - (longview["y"] + longview["h"]))
        return (dx * dx + dy * dy) ** 0.5

    closest = min(data["points"], key=distance)
    center_distance = distance(closest)
    painted_clearance = center_distance - data["strokeWidth"] / 2

    original = Image.open(PNG).convert("RGB")
    check = Image.open(screenshot).convert("RGB")
    if original.size != check.size:
        changed_pixels = -1
        max_channel_delta = -1
    else:
        diff = ImageChops.difference(original, check)
        changed_pixels = sum(1 for pixel in diff.getdata() if pixel != (0, 0, 0))
        extrema = diff.getextrema()
        max_channel_delta = max(high for _, high in extrema)
    lines = [
        f"original_png_sha256={hashlib.sha256(PNG.read_bytes()).hexdigest()}",
        f"check_png_sha256={hashlib.sha256(screenshot.read_bytes()).hexdigest()}",
        f"original_size={original.size}",
        f"check_size={check.size}",
        f"changed_pixels={changed_pixels}",
        f"max_channel_delta={max_channel_delta}",
        f"node_failures={sum(row['verdict']=='FAIL' for row in node_rows)}",
        f"label_box_intersections={len(collision_rows)}",
        f"tallinn_metr_closest_center=({closest[0]:.2f},{closest[1]:.2f})",
        f"tallinn_metr_centerline_distance_to_longview={center_distance:.2f}",
        f"tallinn_metr_stroke_width={data['strokeWidth']:.2f}",
        f"tallinn_metr_painted_clearance_to_longview={painted_clearance:.2f}",
    ]
    (OUT / "layout-summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(" ".join(lines[-6:]))


if __name__ == "__main__":
    main()
