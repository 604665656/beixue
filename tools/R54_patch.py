# -*- coding: utf-8 -*-
"""R54 patch：
   ① 修真 bug「ROLE_POOL 静态、每轮新增专属层从不入池」——从 EXPR_SPECIAL 动态合并
   ② 接入 10 张 R54 AI 原画（ART + EXPR_SPECIAL）
   ③ 版本 R53 -> R54（脚注 + CSV 文件名）
   幂等：可重复执行。"""
import json, re

P = '/data/workspace/杯雪游戏总站.html'
s = open(P, encoding='utf-8').read()
orig = len(s)
log = []

NEW = json.load(open('/data/workspace/anim49/_QC.json'))['META']
EMB = json.load(open('/data/workspace/anim49/_EMB.json'))
PAIR = {v['exprkey']: k for k, v in NEW.items()}

# ---------- ① 真 bug：角色池不吸收专属层 ----------
# ROLE_POOL 是静态表，R43–R52 每轮新增的专属层都没进池，
# 「复用只从本角色池取」实际用的是旧池，exprCrossCount 的池校验也偏窄。
# 改为在 EXPR 构建前、按 EXPR_SPECIAL 一次性动态合并，后续轮次自动生效。
SYNC = ("/* R54 bug①（R53 修，R54 沿用）：ROLE_POOL 为静态表，历轮新增专属层从不入池；\n"
        "   面板宣称「复用只从本角色池取」，池子却停在旧层。这里在 EXPR 构建前\n"
        "   按 EXPR_SPECIAL 动态并入本角色池，一次覆盖 R43–R54 全部专属层，\n"
        "   以后每轮接入自动生效，不再逐轮补表。 */\n"
        "const R54_POOL_SYNC=(()=>{let n=0;\n"
        " for(const [ek,art] of Object.entries(EXPR_SPECIAL)){\n"
        "  const c=ek.split('|')[0]; if(!ROLE_POOL[c])ROLE_POOL[c]=[];\n"
        "  if(typeof ART!=='undefined'&&ART[art]&&!ROLE_POOL[c].includes(art)){\n"
        "   ROLE_POOL[c].push(art); n++;\n"
        "  }\n"
        " } return n;})();\n")
if 'const R54_POOL_SYNC=' in s:
    log.append('OK  R54_POOL_SYNC 已存在（幂等跳过）')
else:
    anchor = 'const EXPR=[];'
    assert anchor in s, 'EXPR 构建锚点未命中'
    s = s.replace(anchor, SYNC + anchor, 1)
    log.append('OK  R54_POOL_SYNC 注入（角色池动态吸收专属层）')

# ---------- ② 接入 10 张 ----------
a = s.index('const EXPR_SPECIAL=')
b = s.index(';', a) + 1
cur = json.loads(s[s.index('{', a):b - 1])
before = len(cur)
for ek, k in PAIR.items():
    cur[ek] = k
s = s[:a] + 'const EXPR_SPECIAL=' + json.dumps(cur, ensure_ascii=False) + ';' + s[b:]
log.append('OK  EXPR_SPECIAL %d -> %d（R54 10 格，幂等覆盖）' % (before, len(cur)))

# 先移除旧的 R53 assign 块，再插一次（幂等）
s = re.sub(r'/\* R54：10 张逐张独立生成[\s\S]*?Object\.assign\(ART, \{[\s\S]*?\}\);\n', '', s, count=1)
assign = ('/* R54：10 张逐张独立生成；基准为用户三视图裁出的正面单只。\n'
          '   不进 PROC_ART（AI 原画）；水印源头预清 + 悬浮碎块通用清理。 */\n'
          'Object.assign(ART, ' + json.dumps(EMB, ensure_ascii=False) + ');\n')
art = s.index('const ART = ')
e = s.index('};', art) + 2
s = s[:e] + '\n' + assign + s[e:]
log.append('OK  10 张 WebP 注入 ART（幂等）')

# ---------- ③ 版本推进 ----------
s = s.replace("R53：当前筛选 ", "R54：当前筛选 ", 1)
s = s.replace("杯雪表情谱系_R53_", "杯雪表情谱系_R54_", 1)
log.append('OK  版本 -> R54（脚注 + CSV 文件名）')

open(P, 'w', encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)' % (orig, len(s), len(s) - orig))
print('TAIL_OK', s.rstrip().endswith('</html>'))
