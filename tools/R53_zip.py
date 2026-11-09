# -*- coding: utf-8 -*-
"""R53 压缩包：工作区 1536 无损原图留在本地，包内收 720 JPG、透明层、
   逐帧 GIF/APNG、脚本与文档，控制在单文件体积上限内。"""
import os, zipfile, hashlib

WS = '/data/workspace'
OUT = WS + '/杯雪全套.zip'
if os.path.exists(OUT):
    os.remove(OUT)

dirs = ['40_资源管线', '44_表情管理', 'anim34', 'anim35', 'anim36',
        'anim46', 'anim47', 'anim48']
files = [n for n in os.listdir(WS) if os.path.isfile(os.path.join(WS, n))
         and n.endswith(('.md', '.csv', '.json', '.html'))
         and not n.startswith('_')]
SKIP_DIR = {'__pycache__'}
MAX_PNG = 1.5 * 1048576          # 1536 原图不进包（工作区保留无损原件）
BAD_SUFFIX = ('.pyc', '.txt')


def keep(p):
    n = os.path.basename(p)
    if n.startswith('_shot_') or n.startswith('_wm') or n.startswith('._'):
        return False
    if n.endswith(BAD_SUFFIX):
        return False
    if n.lower().endswith('.png') and os.path.getsize(p) > MAX_PNG:
        return False
    return True


items = []
for n in sorted(set(files)):
    p = os.path.join(WS, n)
    if keep(p):
        items.append(p)
for d0 in dirs:
    root = os.path.join(WS, d0)
    if not os.path.isdir(root):
        continue
    for base, ds, fs in os.walk(root):
        ds[:] = [x for x in ds if x not in SKIP_DIR]
        for fn in sorted(fs):
            p = os.path.join(base, fn)
            if keep(p):
                items.append(p)

with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for p in items:
        z.write(p, '杯雪全套/' + os.path.relpath(p, WS))

with zipfile.ZipFile(OUT) as z:
    names = z.namelist()
    audio = [n for n in names if n.lower().endswith(('.ogg', '.m4a', '.wav', '.mp3'))]
    assert not audio, audio[:3]
    for html in ['杯雪游戏总站.html', '杯雪游戏总站_轻量版.html']:
        assert '杯雪全套/' + html in names, html
    a = hashlib.sha1(z.read('杯雪全套/杯雪游戏总站_轻量版.html')).hexdigest()
    b = hashlib.sha1(open(WS + '/杯雪游戏总站_轻量版.html', 'rb').read()).hexdigest()
    assert a == b, '轻量版 SHA1 不一致'

mb = os.path.getsize(OUT) / 1048576
assert mb < 190, '包体超限 %.1f MB' % mb
print('ZIP', len(items), '条', round(mb, 1), 'MB | 音频', len(audio), '| 轻量版 SHA1 一致')
