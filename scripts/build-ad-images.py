#!/usr/bin/env python3
"""Compose Yandex Direct PNGs from scripts/.phone-capture.png (run capture-ad-phone.mjs first)."""
from pathlib import Path
from PIL import Image

BG = (251, 248, 243)
ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'landing' / 'assets' / '.phone-capture.png'
OUT = ROOT / 'landing' / 'assets'


def compose(out_w: int, out_h: int, path: Path, bottom_extra: float = 0.04) -> None:
    phone = Image.open(SRC).convert('RGB')
    canvas = Image.new('RGB', (out_w, out_h), BG)
    margin_top = int(min(out_w, out_h) * 0.10)
    margin_side = int(min(out_w, out_h) * 0.10)
    margin_bottom = int(min(out_w, out_h) * (0.10 + bottom_extra))
    max_h = out_h - margin_top - margin_bottom
    max_w = out_w - 2 * margin_side
    r = phone.width / phone.height
    nh = max_h
    nw = int(nh * r)
    if nw > max_w:
        nw = max_w
        nh = int(nw / r)
    ph = phone.resize((nw, nh), Image.Resampling.LANCZOS)
    x = (out_w - nw) // 2
    y = margin_top + (max_h - nh) // 2
    canvas.paste(ph, (x, y))
    canvas.save(path, 'PNG', optimize=True)
    print(path, f'{nw}x{nh}')


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f'Missing {SRC}. Run: node scripts/capture-ad-phone.mjs')
    compose(1080, 1080, OUT / 'ad-direct-1080x1080.png', bottom_extra=0.02)
    compose(1080, 607, OUT / 'ad-direct-1080x607.png', bottom_extra=0.06)
    compose(450, 450, OUT / 'ad-direct-450x450.png', bottom_extra=0.02)


if __name__ == '__main__':
    main()
