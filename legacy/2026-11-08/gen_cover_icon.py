#!/usr/bin/env python3
"""程序化生成 Toy 封面与图标（不使用游戏内截图，避免素材文字/乱码带来的审核噪音）。"""
import math
import pathlib
import random
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "deliver"
OUT.mkdir(exist_ok=True)


def font(size, bold=True):
    p = "C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc"
    return ImageFont.truetype(p, size)


def ink_bg(w, h, seed=7):
    """夜雨墨色渐变 + 极淡雨丝，纯程序绘制。"""
    rnd = random.Random(seed)
    im = Image.new("RGB", (w, h))
    px = im.load()
    for y in range(h):
        t = y / h
        for x in range(w):
            r = x / w
            glow = max(0.0, 1 - math.hypot((r - 0.72) * 1.5, (t - 0.26) * 1.7))
            base = 16 + int(16 * t) + int(16 * glow)
            px[x, y] = (base + 3, base + 5, base + 11)
    d = ImageDraw.Draw(im, "RGBA")
    for _ in range(220):
        x = rnd.randint(0, w)
        y = rnd.randint(0, h)
        ln = rnd.randint(18, 70)
        d.line([(x, y), (x - ln * 0.22, y + ln)], fill=(205, 215, 225, 18), width=1)
    return im


def frame(d, w, h, pad, color, width=3):
    d.rectangle([pad, pad, w - pad, h - pad], outline=color, width=width)
    d.rectangle([pad + 8, pad + 8, w - pad - 8, h - pad - 8],
                outline=(*color[:3], 70) if len(color) == 4 else color, width=1)


CREAM = (238, 226, 202)
GOLD = (186, 150, 92)
RED = (168, 58, 52)

# ---------- 封面 1200 x 900 (4:3) ----------
W, H = 1200, 900
im = ink_bg(W, H)
d = ImageDraw.Draw(im, "RGBA")
frame(d, W, H, 34, GOLD + (255,), 3)
frame(d, W, H, 46, (186, 150, 92, 90), 1)

d.text((W / 2, 330), "杯 雪", font=font(190), fill=CREAM, anchor="mm")
d.line([(360, 452), (840, 452)], fill=GOLD + (200,), width=2)
d.text((W / 2, 520), "互 动 游 戏 集", font=font(56), fill=CREAM, anchor="mm")
d.text((W / 2, 610), "二十四关 · 七卷 · 四模式 · 三档难度", font=font(32, False),
       fill=(196, 190, 176), anchor="mm")
d.text((W / 2, 690), "离线可玩 · 机制化拆读 · 原创美术", font=font(26, False),
       fill=(170, 166, 158), anchor="mm")

# 朱砂印
d.rounded_rectangle([(W - 186, H - 186), (W - 96, H - 96)], radius=8, fill=RED)
d.text((W - 141, H - 141), "雪", font=font(66), fill=(248, 238, 218), anchor="mm")

cover = OUT / "cover.png"
im.save(cover, optimize=True)
print("封面", cover, im.size, cover.stat().st_size, "B")

# ---------- 图标 512 x 512 ----------
S = 512
ic = ink_bg(S, S, seed=19)
di = ImageDraw.Draw(ic, "RGBA")
di.rounded_rectangle([14, 14, S - 14, S - 14], radius=28, outline=GOLD + (255,), width=6)
di.rounded_rectangle([28, 28, S - 28, S - 28], radius=20, outline=(186, 150, 92, 110), width=2)
di.text((S / 2, 208), "雪", font=font(186), fill=CREAM, anchor="mm")
di.line([(128, 352), (384, 352)], fill=GOLD + (220,), width=3)
di.text((S / 2, 414), "杯 雪", font=font(54), fill=(214, 202, 178), anchor="mm")

icon = OUT / "icon.png"
ic.save(icon, optimize=True)
print("图标", icon, ic.size, icon.stat().st_size, "B")
