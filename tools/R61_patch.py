# -*- coding: utf-8 -*-
"""R61：把 9 张新层插到 ART 注入区末尾（`\n\nconst $ = (s,r=` 之前）。
   安全约束：锚点必须落在【最后一个 <script> 块内】且与 EXPR_SPECIAL 之间
   不存在 </script> 边界——避免重演 R58「插进字面量中间」导致整页脚本失效。
   幂等：重复执行先移除旧 R61 块再插入。"""
import json, re

MAIN='/data/workspace/杯雪游戏总站.html'
emb=json.load(open('/data/workspace/anim61/_EMB.json'))
# 键名必须与 EXPR_SPECIAL 的「角色键|表情」完全一致，否则会被 R54_POOL_SYNC
# 静默当作新角色池条目吞掉、不报任何错（本轮首次接入就踩了这个坑）
JOBS=[('R61_base_ai','cos_base|哀'),('R61_base_jing','cos_base|惊'),
      ('R61_base_yi','cos_base|疑'),('R61_base_zui','cos_base|醉'),
      ('R61_geng_jing','cos_geng|惊'),('R61_geng_zui','cos_geng|醉'),
      ('R61_jinhe_ai','cos_jinhe|哀'),('R61_jinhe_jing','cos_jinhe|惊'),
      ('R61_qinwen_nu','cos_qinwen|怒')]
NOTE='/* R61：9 张逐张独立 AI 图生图（只换表情），插在 ART 注入区末尾、EXPR_SPECIAL 字面量之后 */'
B0,B1='/* R61-ART-BLOCK */','/* R61-ART-END */'

s=open(MAIN,encoding='utf-8').read()
if B0 in s:                       # 幂等：先摘掉旧块
    s=re.sub(re.escape(B0)+r'.*?'+re.escape(B1),'',s,flags=re.S)
    print('旧 R61 块已移除，重新插入')

anchor='\n\nconst $ = (s,r='
i=s.find(anchor)
assert i>0, 'anchor not found'
last_close=s.rfind('</script>')
open_blk=s.rfind('<script',0,last_close)
assert open_blk < i < last_close, 'anchor 不在最后一个 script 块内'
assert '</script>' not in s[s.find('const EXPR_SPECIAL='):i], 'anchor 与 EXPR_SPECIAL 之间有 script 边界'

# 同时做两件事：① 注入图层到 ART；② 把谱系键指向新层（这才是「专属格」生效的关键）
blk=('Object.assign(ART,{'+','.join('"%s":"%s"'%(k[0],emb[k[0]]) for k in JOBS)+'});'
     +'Object.assign(EXPR_SPECIAL,{'+','.join('"%s":"%s"'%(k[1],k[0]) for k in JOBS)+'});')
new=s[:i]+'\n\n'+NOTE+'\n'+B0+'\n'+blk+'\n'+B1+s[i:]
open(MAIN,'w',encoding='utf-8').write(new)
print('inserted at %d, size %d -> %d, layers=%d'%(i,len(s),len(new),len(JOBS)))
