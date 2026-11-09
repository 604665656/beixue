# -*- coding: utf-8 -*-
"""R51 主站 patch：10 张真 AI 图生图接入 + 版本推进。
   本轮 AI 服务恢复，产物是 AI 原画（不进 PROC_ART，保持 20 项程序化层不变）。
   R50 修的 bug① 正好在此验证：新轮次真原画不会被误标成程序化。"""
import json

P='/data/workspace/杯雪游戏总站.html'
s=open(P,encoding='utf-8').read(); orig=len(s); log=[]

QC=json.load(open('/data/workspace/anim45/_QC.json'))  # not used, keep parity
NEW=json.load(open('/data/workspace/anim46/_QC.json'))['META']
EMB=json.load(open('/data/workspace/anim46/_EMB.json'))
PAIR={v['exprkey']:k for k,v in NEW.items()}

# 1) EXPR_SPECIAL 新增 10 项
a=s.index('const EXPR_SPECIAL='); b=s.index(';',a)+1
cur=json.loads(s[s.index('{',a):b-1])
before=len(cur)
for ek,k in PAIR.items():
    cur[ek]=k                                  # 幂等：已有则覆盖，不因重复执行报错
s=s[:a]+'const EXPR_SPECIAL='+json.dumps(cur,ensure_ascii=False)+';'+s[b:]
log.append('OK  EXPR_SPECIAL %d -> %d（R51 10 格已就位，幂等覆盖）'%(before,len(cur)))

# 2) 注入 10 张 WebP：先移除旧的 R51 assign 块，再插一次（幂等）
import re
s=re.sub(r'/\* R51：AI 图生图服务恢复[\s\S]*?Object\.assign\(ART, \{[\s\S]*?\}\);\n','',s,count=1)
assign=('/* R51：AI 图生图服务恢复，10 张逐张独立生成；基准为用户上传三视图裁出的正面单只。\n'
        '   不进 PROC_ART（这些是 AI 原画，不是程序化本体重绘）；水印已在源头预清。 */\n'
        'Object.assign(ART, '+json.dumps(EMB,ensure_ascii=False)+');\n')
art=s.index('const ART = '); e=s.index('};',art)+2
s=s[:e]+'\n'+assign+s[e:]
log.append('OK  10 张 WebP 注入 ART（幂等）')

# 3) 版本推进：兼容 R50 或已是 R51
s=s.replace("R50：当前筛选 ","R51：当前筛选 ",1)
s=s.replace("杯雪表情谱系_R50_","杯雪表情谱系_R51_",1)
log.append('OK  版本 -> R51（脚注 + CSV 文件名，兼容重复执行）')

open(P,'w',encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)'%(orig,len(s),len(s)-orig))
print('TAIL_OK',s.rstrip().endswith('</html>'))
print('PROC_ART 应仍为 20:', 'const PROC_ART=new Set(' in s)
