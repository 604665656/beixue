# -*- coding: utf-8 -*-
"""R55 patch：
   ① bug①：R54 注入时未删除旧的 R53 assign 块，主站与轻量版都留下两份
      「R54：10 张…」注释块（其中一份实为 R53 内容），误导排障且白占体积。
      这里按行号把「非最新一份、且注释标错版本」的旧块注释订正为真实轮次。
   ② 接入 10 张 R55 AI 原画（ART + EXPR_SPECIAL）
   ③ 版本推进 R54 -> R55（脚注 + CSV 文件名）
   幂等：可重复执行。"""
import json, re, sys

P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig = len(s)
log = []

META = json.load(open('/data/workspace/anim50/_QC.json'))['META']
EMB = json.load(open('/data/workspace/anim50/_EMB.json'))
PAIR = {v['exprkey']: k for k, v in META.items()}

# ---------- ① 旧块版本标注订正 ----------
# 定位所有「/* R5x：10 张逐张独立生成」注释块（含其后一行 Object.assign）
blocks = [(m.start(), m.group(1)) for m in
          re.finditer(r'/\*\s*(R5\d)：10 张逐张独立生成', s)]
if len(blocks) >= 2:
    # 按首个 ART 键判定每个块的真实轮次
    lines = s.split('\n')
    fixed = 0
    for idx, line in enumerate(lines):
        m = re.match(r'^/\*\s*(R5\d)：10 张逐张独立生成', line)
        if not m:
            continue
        # 找该注释后第一条 Object.assign 行的键前缀
        real = None
        for j in range(idx + 1, min(idx + 4, len(lines))):
            mm = re.match(r'^Object\.assign\(ART,\s*\{"([^"]+)"', lines[j])
            if mm:
                real = mm.group(1).split('_')[0].upper()
                break
        tagged = m.group(1).upper()
        if real and real != tagged:
            lines[idx] = line.replace(tagged, real, 1)
            fixed += 1
    s = '\n'.join(lines)
    log.append('OK  旧注入块版本标注订正 %d 处（共 %d 块，按首个 ART 键判定真实轮次）'
               % (fixed, len(blocks)))
else:
    log.append('OK  注入块版本标注无需订正（块数 %d）' % len(blocks))

# ---------- ② 接入 10 张 ----------
a = s.index('const EXPR_SPECIAL=')
b = s.index(';', a) + 1
cur = json.loads(s[s.index('{', a):b - 1])
before = len(cur)
for ek, k in PAIR.items():
    cur[ek] = k
s = s[:a] + 'const EXPR_SPECIAL=' + json.dumps(cur, ensure_ascii=False) + ';' + s[b:]
log.append('OK  EXPR_SPECIAL %d -> %d（R55 10 格，幂等覆盖）' % (before, len(cur)))

# 移除旧的 R55 assign 块（若有），再插一次
s = re.sub(r'/\* R55：10 张逐张独立生成[\s\S]*?Object\.assign\(ART, \{[\s\S]*?\}\);\n', '', s, count=1)
assign = ('/* R55：10 张逐张独立生成；基准为用户三视图裁出的正面单只。\n'
          '   不进 PROC_ART（AI 原画）；水印源头预清 + 悬浮碎块通用清理。 */\n'
          'Object.assign(ART, ' + json.dumps(EMB, ensure_ascii=False) + ');\n')
art = s.index('const ART = ')
e = s.index('};', art) + 2
s = s[:e] + '\n' + assign + s[e:]
log.append('OK  10 张 WebP 注入 ART（幂等）')

# ---------- ③ 版本推进 ----------
s = s.replace("R54：当前筛选 ", "R55：当前筛选 ", 1)
s = s.replace("杯雪表情谱系_R54_", "杯雪表情谱系_R55_", 1)
log.append('OK  版本 -> R55（脚注 + CSV 文件名）')

open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)' % (orig, len(s), len(s) - orig))
print('TAIL_OK', s.rstrip().endswith('</html>'))
