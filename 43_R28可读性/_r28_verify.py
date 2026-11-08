# -*- coding: utf-8 -*-
"""R28 回归：三套皮肤下选中卡文字对比度（WCAG）、前后截图、无溢出。"""
import json, os, zipfile
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont

ROOT='/data/workspace'
OLD='file:///data/workspace/_r28_before.html'
NEW='file:///data/workspace/杯雪游戏总站.html'

LUM_JS = r"""()=>{
  const lum=(c)=>{
    const m=c.match(/[\d.]+/g);if(!m)return null;
    let [r,g,b]=m.slice(0,3).map(Number);
    const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};
    return .2126*f(r)+.7152*f(g)+.0722*f(b);
  };
  const bgOf=(el)=>{
    let n=el;
    while(n&&n!==document.documentElement){
      const c=getComputedStyle(n).backgroundColor;
      if(c&&c!=='rgba(0, 0, 0, 0)'&&c!=='transparent')return c;
      n=n.parentElement;
    }
    return getComputedStyle(document.body).backgroundColor;
  };
  const ratio=(a,b)=>{const x=lum(a),y=lum(b);if(x===null||y===null)return null;
    return +(((Math.max(x,y)+.05)/(Math.min(x,y)+.05)).toFixed(2));};
  const card=document.querySelector('.d4i.on');
  if(!card)return {err:'no .d4i.on'};
  const bg=getComputedStyle(card).backgroundColor;
  const pick=(sel)=>{const el=card.querySelector(sel)||document.querySelector(sel);
    if(!el)return null;const cs=getComputedStyle(el);
    const own=(cs.backgroundColor&&cs.backgroundColor!=='rgba(0, 0, 0, 0)')?cs.backgroundColor:bg;
    return {sel:sel,color:cs.color,bg:own,size:cs.fontSize,ratio:ratio(cs.color,own)};};
  return {skin:document.documentElement.getAttribute('data-skin')||'paper',
          cardBg:bg,cardColor:getComputedStyle(card).color,
          items:[pick('b'),pick('.lead'),pick('ul'),pick('li'),pick('.tag'),pick('.chk'),pick('.ico')],
          heroLead:(()=>{const e=document.querySelector('.mh-lead');if(!e)return null;
            return {color:getComputedStyle(e).color,ratio:ratio(getComputedStyle(e).color,bgOf(e))};})()};
}"""

def setup(pg, skin, diff='collate'):
    pg.evaluate("""([skin,diff])=>{
      document.documentElement.setAttribute('data-skin',skin);
      try{localStorage.setItem('beixue_skin_v2',skin)}catch(e){}
      try{localStorage.setItem('beixue_diff_v1',diff)}catch(e){}
      document.querySelectorAll('details').forEach(d=>d.open=true);
    }""", [skin, diff])

out={}
with sync_playwright() as p:
    br=p.chromium.launch(headless=True, executable_path='/usr/bin/google-chrome',
        args=['--no-sandbox','--disable-web-security','--allow-file-access-from-files'])
    ctx=br.new_context(viewport={'width':420,'height':900},device_scale_factor=1)

    # 旧版（修复前）夜雨 + 校勘
    pg=ctx.new_page();pg.goto(OLD,wait_until='load');pg.wait_for_timeout(700)
    setup(pg,'night');pg.evaluate("()=>{DIFF='collate';if(typeof render==='function')render();document.querySelectorAll('details').forEach(d=>d.open=true);}")
    pg.wait_for_timeout(400)
    out['before_night']=pg.evaluate(LUM_JS)
    pg.locator('#diffHero').screenshot(path=ROOT+'/_r28_before_night.png')
    pg.close()

    # 新版三套皮肤
    shots=[]
    for skin in ['night','paper','plain']:
        pg=ctx.new_page();pg.goto(NEW,wait_until='load');pg.wait_for_timeout(700)
        setup(pg,skin);pg.evaluate("()=>{DIFF='collate';if(typeof render==='function')render();document.querySelectorAll('details').forEach(d=>d.open=true);}")
        pg.wait_for_timeout(400)
        out[skin]=pg.evaluate(LUM_JS)
        out[skin]['overflow']=pg.evaluate("()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth})")
        fp=ROOT+'/_r28_'+skin+'.png'
        pg.locator('#diffHero').screenshot(path=fp)
        shots.append((skin,fp))
        pg.close()

    # 高对比
    pg=ctx.new_page();pg.goto(NEW,wait_until='load');pg.wait_for_timeout(700)
    setup(pg,'night');pg.evaluate("()=>{HC=1;applyA11y();DIFF='collate';render();document.querySelectorAll('details').forEach(d=>d.open=true);}")
    pg.wait_for_timeout(350)
    out['hc']=pg.evaluate(LUM_JS)
    fp=ROOT+'/_r28_hc.png';pg.locator('#diffHero').screenshot(path=fp)
    shots.append(('高对比',fp))
    pg.close()

    # 全局回归
    pg=ctx.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(NEW,wait_until='load');pg.wait_for_timeout(800)
    out['global']=pg.evaluate("""()=>{
      const ids=D.meta.levels.map(l=>l.id),bad=[];
      for(const k of ids){try{const s=stageFor(k);if(!s||!ART[s.cast])bad.push(k)}catch(e){bad.push(k+':ERR')}}
      return {levels:ids.length,bad:bad,art:Object.keys(ART).length,
              store:storeCheck(),log:stageLogSummary().total,
              audio:[localStorage.getItem('beixue_bgm_v2'),localStorage.getItem('beixue_sfx_v2')]};}""")
    out['pageerrors']=errs[:8]
    pg.close();br.close()

print(json.dumps(out,ensure_ascii=False,indent=2)[:6000])
open(ROOT+'/_r28_verify.json','w',encoding='utf-8').write(json.dumps(out,ensure_ascii=False,indent=2))

# 拼前后对比图
try:fnt=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',14)
except:fnt=ImageFont.load_default()
allshots=[('修复前 · 夜雨',ROOT+'/_r28_before_night.png')]+shots
ims=[Image.open(p).convert('RGB') for _,p in allshots]
w=max(i.width for i in ims);h=max(i.height for i in ims)
cw=w+16;canvas=Image.new('RGB',(cw*len(ims),h+40),(245,241,232));d=ImageDraw.Draw(canvas)
for idx,(lab,im) in enumerate(zip([x[0] for x in allshots],ims)):
    canvas.paste(im,(idx*cw+8,8))
    d.text((idx*cw+10,h+12),lab,fill=(43,42,38),font=fnt)
canvas.save(ROOT+'/_r28_可读性对比.jpg',quality=90,optimize=True)
print('对比图',canvas.size)
