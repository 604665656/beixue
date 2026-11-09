# -*- coding: utf-8 -*-
"""轻量版一致性门禁：主站改过之后，轻量版必须跟着重出，否则静默不同步。
   校验：内嵌键集合一致 / 关键 JS 逻辑一致 / 轻量图 ≤224px / 无外链无音频。"""
import re, json, base64, io, os, sys
from PIL import Image

FULL = '/data/workspace/杯雪游戏总站.html'
LITE = '/data/workspace/杯雪游戏总站_轻量版.html'
OUT = '/data/workspace/44_表情管理/R48_轻量版一致性门禁.json'
R = {'checks': []}


def ck(n, c, d=''):
    R['checks'].append({'name': n, 'ok': bool(c), 'detail': str(d)})


a = open(FULL, encoding='utf-8').read()
b = open(LITE, encoding='utf-8').read()

KEY = re.compile(r'["\']([A-Za-z0-9_]+)["\']\s*:\s*"data:image/(?:webp|gif|png|jpeg);base64,')
ka, kb = set(KEY.findall(a)), set(KEY.findall(b))
ck('内嵌键集合一致', ka == kb, '主站 %d / 轻量 %d，差 %s' % (len(ka), len(kb), sorted(ka ^ kb)[:8]))

# 关键逻辑函数文本必须逐字一致（轻量版只压资源，不许改 JS）
FNS = ['function exprResolve(', 'function exprMoodFor(', 'function exprStat(',
       'function exprCanon(', 'function exprCrossCount(', 'function stageFor(',
       'function queuePerf(', 'function exprPanelHTML(', 'function exprExport(']
diff = []
for fn in FNS:
    ia, ib = a.find(fn), b.find(fn)
    if ia < 0 or ib < 0:
        diff.append(fn + ':missing')
        continue
    end = '\nfunction '
    ta = a[ia:a.find(end, ia + 10)] if a.find(end, ia + 10) > 0 else a[ia:ia + 1600]
    tb = b[ib:b.find(end, ib + 10)] if b.find(end, ib + 10) > 0 else b[ib:ib + 1600]
    if ta != tb:
        diff.append(fn)
ck('关键 JS 逻辑逐字一致', not diff, diff)

URI = re.compile(r'data:image/(?:webp|gif|png|jpeg);base64,[A-Za-z0-9+/=]+')
uris = set(URI.findall(b))
over, bad = [], []
for u in uris:
    try:
        im = Image.open(io.BytesIO(base64.b64decode(u.split(',', 1)[1])))
        if u.startswith('data:image/webp') and max(im.size) > 224:
            over.append(str(im.size))
    except Exception as e:
        bad.append(repr(e)[:50])
ck('轻量版内嵌图全部可解码', not bad, bad[:3])
ck('轻量版 WebP 均 ≤224px', not over, over[:3])
ck('轻量版 GIF 组数 6', sum(1 for u in uris if u.startswith('data:image/gif')) == 6)
ck('轻量版无外链', '<script src=' not in b and 'href="http' not in b and 'url(http' not in b)
ck('轻量版无音频', 'new Audio(' not in b and not re.search(r'data:audio/[a-z0-9.+-]+;base64,', b, re.I))
ck('轻量版显著更小', os.path.getsize(LITE) < os.path.getsize(FULL) * .5,
   '%.2f / %.2f MB' % (os.path.getsize(LITE) / 1048576, os.path.getsize(FULL) / 1048576))
ck('轻量版标题标识', '轻量版' in re.search(r'<title>(.*?)</title>', b, re.S).group(1))

R['summary'] = {'total': len(R['checks']), 'passed': sum(1 for c in R['checks'] if c['ok']),
                'failed': sum(1 for c in R['checks'] if not c['ok'])}
json.dump(R, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for c in R['checks']:
    print(('PASS ' if c['ok'] else 'FAIL ') + c['name'] + ('  ' + c['detail'] if c['detail'] else ''))
print(json.dumps(R['summary'], ensure_ascii=False))
sys.exit(0 if R['summary']['failed'] == 0 else 1)
