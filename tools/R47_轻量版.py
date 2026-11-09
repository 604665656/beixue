# -*- coding: utf-8 -*-
"""生成「轻量版」单文件：全部内嵌 WebP 重编码到 224px/q40，GIF 逐帧动画原样保留，
   同时压缩 DATA JSON 空白。不加外链、不改任何 JS 逻辑，元宝可直接点开。"""
import re, base64, io, json, os
from PIL import Image

SRC = '/data/workspace/杯雪游戏总站.html'
DST = '/data/workspace/杯雪游戏总站_轻量版.html'
s = open(SRC, encoding='utf-8').read()
orig_bytes = os.path.getsize(SRC)

URI = re.compile(r'data:image/(?:webp|gif);base64,[A-Za-z0-9+/=]+')
cache = {}
stat = {'webp': 0, 'gif_keep': 0, 'bytes_before': 0, 'bytes_after': 0}


def shrink(u):
    if u in cache:
        return cache[u]
    stat['bytes_before'] += len(u)
    if u.startswith('data:image/gif'):
        # 6 组逐帧动画保留原始帧、透明索引、duration 与 loop，不做任何缩放或重排
        out = u
        stat['gif_keep'] += 1
    else:
        raw = base64.b64decode(u.split(',', 1)[1])
        im = Image.open(io.BytesIO(raw)).convert('RGBA')
        w, h = im.size
        if max(w, h) > 224:
            k = 224 / max(w, h)
            im = im.resize((max(1, round(w * k)), max(1, round(h * k))), Image.LANCZOS)
        b = io.BytesIO()
        im.save(b, 'WEBP', quality=40, method=6)
        out = 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()
        stat['webp'] += 1
    cache[u] = out
    stat['bytes_after'] += len(out)
    return out


s = URI.sub(lambda m: shrink(m.group(0)), s)

# DATA JSON 去空白（纯 JSON，无字符串字面量风险）
m = re.search(r'(<script type="application/json" id="DATA">)([\s\S]*?)(</script>)', s)
if m:
    try:
        compact = json.dumps(json.loads(m.group(2)), ensure_ascii=False, separators=(',', ':'))
        s = s[:m.start(2)] + compact + s[m.end(2):]
        stat['data_json'] = [len(m.group(2)), len(compact)]
    except Exception as e:
        stat['data_json'] = 'SKIP ' + repr(e)

# 仅改标题做版本标识，不动 DOM 结构
s = re.sub(r'<title>(.*?)</title>',
           lambda m: '<title>' + m.group(1) + ' · 轻量版</title>', s, count=1)
s = s.replace('<html', '<!-- 杯雪轻量版：内嵌 WebP 224px/q40，逐帧 GIF 原样保留，无外置依赖 -->\n<html', 1)

open(DST, 'w', encoding='utf-8').write(s)
new_bytes = os.path.getsize(DST)
print('WebP 重编码 %d 张｜GIF 原样保留 %d 组｜唯一 URI %d' %
      (stat['webp'], stat['gif_keep'], len(cache)))
print('图片 base64 字符 %.2f MB -> %.2f MB' %
      (stat['bytes_before'] / 1048576, stat['bytes_after'] / 1048576))
print('DATA JSON', stat.get('data_json'))
print('HTML %.2f MB -> %.2f MB  (减少 %.1f%%)' %
      (orig_bytes / 1048576, new_bytes / 1048576, 100 * (1 - new_bytes / orig_bytes)))
print('外链检查 script src=', s.count('<script src='), ' href=http=', s.count('href="http'),
      ' url(http=', s.count('url(http'))
print('尾部完整', s.rstrip().endswith('</html>'))
