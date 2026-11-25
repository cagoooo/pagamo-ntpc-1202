"""產生 favicon、PWA 圖示與 1200×630 社群預覽圖（效率儀表板風）。用法：python scripts/make_icons_og.py"""
from PIL import Image, ImageDraw, ImageFont
BG, LIME, INK, MUTED, LINE = (12, 16, 20), (198, 244, 50), (238, 242, 245), (154, 166, 178), (42, 52, 64)
MONO = 'C:/Windows/Fonts/consolab.ttf'
BOLD, REG = 'C:/Windows/Fonts/msjhbd.ttc', 'C:/Windows/Fonts/msjh.ttc'

def icon(size, pad=0.0):
    im = Image.new('RGB', (size, size), BG)
    d = ImageDraw.Draw(im)
    inner = int(size * (1 - pad * 2))
    off = (size - inner) // 2
    f = ImageFont.truetype(MONO, int(inner * 0.5))
    t = '×2'
    w = d.textlength(t, font=f)
    bb = d.textbbox((0, 0), t, font=f)
    d.text(((size - w) / 2, (size - (bb[3] - bb[1])) / 2 - bb[1]), t, font=f, fill=LIME)
    d.rectangle((off, size - off - max(2, inner // 14), size - off, size - off), fill=LIME)
    return im

import os
os.makedirs('images/app', exist_ok=True)
icon(192).save('images/app/icon-192.png'); icon(512).save('images/app/icon-512.png')
icon(192, .12).save('images/app/icon-192-maskable.png'); icon(512, .12).save('images/app/icon-512-maskable.png')
icon(180).save('apple-touch-icon.png')
icon(64).save('favicon.ico', sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])
open('favicon.svg', 'w', encoding='utf-8').write(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="10" fill="#0c1014"/>'
    '<text x="32" y="42" font-family="Consolas,monospace" font-weight="700" font-size="30" fill="#c6f432" text-anchor="middle">×2</text>'
    '<rect x="10" y="52" width="44" height="4" fill="#c6f432"/></svg>')

og = Image.new('RGB', (1200, 630), BG)
d = ImageDraw.Draw(og)
for x in range(0, 1200, 40): d.line((x, 0, x, 630), fill=(18, 24, 28))
for y in range(0, 630, 40): d.line((0, y, 1200, y), fill=(18, 24, 28))
d.text((64, 52), 'NTPC TEACHER WORKSHOP · 2026.12.02 WED 14:00–16:00', font=ImageFont.truetype(MONO, 24), fill=LIME)
d.text((64, 140), '教學效率升級', font=ImageFont.truetype(BOLD, 88), fill=INK)
d.text((64, 250), 'PaGamO 實用攻略', font=ImageFont.truetype(BOLD, 88), fill=INK)
d.text((64, 372), '出題效率翻倍', font=ImageFont.truetype(BOLD, 52), fill=LIME)
big = ImageFont.truetype(MONO, 230)
w = d.textlength('×2', font=big)
d.text((1200 - 60 - w, 150), '×2', font=big, fill=LIME)
d.line((64, 500, 1136, 500), fill=LINE, width=2)
d.text((64, 525), '講師　阿凱老師・桃園市龍潭區石門國民小學 資訊組長｜新北市教師線上研習', font=ImageFont.truetype(REG, 28), fill=MUTED)
og.save('og-image.jpg', quality=88, optimize=True)
print('ok')
