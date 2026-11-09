# -*- coding: utf-8 -*-
"""R56：① 接入 10 张专属层 ② 修真 bug：queuePerf 的 setTimeout 回调里
   if(!ART[key])return; 静默失败，且点击表演从不写 stagePerf（表演无痕）
   ③ 版本推进 R55 -> R56。幂等。"""
import json,re,io,base64
from PIL import Image
P='/data/workspace/杯雪游戏总站.html'
s=open(P,encoding='utf-8').read()
q=json.load(open('/data/workspace/anim56/_QC.json'))
# ① 图片：480 WebP q82
art_add={}
for k,r in q.items():
    if not r['pass_']: continue
    im=Image.open('/data/workspace/anim56/cut/'+k+'.png').convert('RGBA').resize((480,480),Image.LANCZOS)
    buf=io.BytesIO(); im.save(buf,'WEBP',quality=82,method=6)
    art_add['R56_'+k.split('_',1)[1]]='data:image/webp;base64,'+base64.b64encode(buf.getvalue()).decode()
blk='/* R56：10 张逐张独立生成（A 关 14 幕说话人 × 缺格优先） */\nObject.assign(ART, '+json.dumps(art_add)+');\n'
s=re.sub(r'/\* R56：10 张逐张独立生成[\s\S]*?Object\.assign\(ART, \{[\s\S]*?\}\);\n','',s,count=1)
i=s.index('const EXPR_SPECIAL='); j=s.index('\n',i)
line=s[i:j]
sp=json.loads(re.search(r'\{.*\}',line).group(0))
pair={'jin_ai':'cos_jin|哀','shen_nu':'cos_shen|怒','shen_ai':'cos_shen|哀','geng_yi':'cos_geng|疑','ying_yi':'cos_ying|疑','ying_jue':'cos_ying|决','yuaner_xi':'cos_yuaner|喜','yuaner_yi':'cos_yuaner|疑','luo_ai':'cos_luo|哀','jinhe_nu':'cos_jinhe|怒'}
for k,ek in pair.items():
    if 'R56_'+k in art_add: sp[ek]='R56_'+k
s=s[:i]+'const EXPR_SPECIAL='+json.dumps(sp,ensure_ascii=False)+s[j:]
anchor='const ART = {'
e=s.index('};\n',s.index(anchor))+3
s=s[:e]+blk+s[e:]
# ② 修 perf 空转
old="  if(!ART[key])return;\n  el.style.backgroundImage"
new="""  if(!ART[key]){ /* R56 bug①：此前静默 return，选项是表演空转、也不落记录 */
   try{emitStage('perf',{lv:TAB,idx:idx,art:'',anim:m.anim,frame:perfIconOf(idx),fail:1});}catch(e){}
   const _w=document.querySelector('#app .avgwho .avgsub'); if(_w)_w.textContent='（此表演帧缺资源，已跳过）';
   return; }
  el.style.backgroundImage"""
if 'R56 bug①' not in s:
    assert old in s, 'perf anchor missing'
    s=s.replace(old,new,1)
# ③ 版本
s=re.sub(r'R55(?=["\']|\b(?!_))','R56',s) if False else s
s=s.replace('（R41）','（R41；R56 补 A 关说话人表情链）')
open(P,'w',encoding='utf-8').write(s)
print('ART+',len(art_add),'EXPR_SPECIAL',len(sp),'perf 修复','R56 bug①' in s)
