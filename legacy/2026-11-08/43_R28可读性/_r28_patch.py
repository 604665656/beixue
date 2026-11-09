# -*- coding: utf-8 -*-
"""R28 补丁：storeCheck 对「纯字符串标量存档」误报；验证脚本正确设置 HC 与 tag 对比度口径。"""
import re, os
ROOT='/data/workspace'
MAIN=[ROOT+'/杯雪游戏总站.html',ROOT+'/杯雪离线总栈.html',ROOT+'/杯雪互动游戏集.html']
b=open(MAIN[0],encoding='utf-8').read()
old="""  try{JSON.parse(raw);}catch(e){bad.push({ns:ns,key:k,why:'非 JSON / 已损坏'});}"""
new="""  /* 标量存档（如皮肤名 'night'、数值 '1'）是合法的，只有以 JSON 结构起头却解析失败才算损坏 */
  const t=raw.trim();
  if(/^[\\[{\"']/.test(t)){try{JSON.parse(raw);}catch(e){bad.push({ns:ns,key:k,why:'JSON 结构损坏'});}}"""
assert old in b
b=b.replace(old,new,1)
for fp in MAIN:open(fp,'w',encoding='utf-8').write(b)
open(ROOT+'/_z.js','w',encoding='utf-8').write(re.findall(r'<script>(.*?)</script>',b,re.S)[-1])
print('storeCheck 标量口径已修')

vp=ROOT+'/_r28_verify.py';v=open(vp,encoding='utf-8').read()
# tag 对比度：用自己的背景色而非卡片背景
v=v.replace("""  const pick=(sel)=>{const el=card.querySelector(sel)||document.querySelector(sel);
    return el?{sel:sel,color:getComputedStyle(el).color,size:getComputedStyle(el).fontSize,
               ratio:ratio(getComputedStyle(el).color,bg)}:null};""",
"""  const pick=(sel)=>{const el=card.querySelector(sel)||document.querySelector(sel);
    if(!el)return null;const cs=getComputedStyle(el);
    const own=(cs.backgroundColor&&cs.backgroundColor!=='rgba(0, 0, 0, 0)')?cs.backgroundColor:bg;
    return {sel:sel,color:cs.color,bg:own,size:cs.fontSize,ratio:ratio(cs.color,own)};};""")
# hc 用真实开关
v=v.replace("pg.evaluate(\"()=>{document.body.classList.add('hc');DIFF='collate';render();document.querySelectorAll('details').forEach(d=>d.open=true);}\")",
            "pg.evaluate(\"()=>{HC=1;applyA11y();DIFF='collate';render();document.querySelectorAll('details').forEach(d=>d.open=true);}\")")
# 全局回归：清掉验证过程写入的标量键干扰前先单独断言
v=v.replace("store:storeCheck().ok,log:stageLogSummary().total,",
            "store:storeCheck(),log:stageLogSummary().total,")
open(vp,'w',encoding='utf-8').write(v)
print('验证脚本已同步')
