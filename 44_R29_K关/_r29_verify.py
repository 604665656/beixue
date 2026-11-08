# -*- coding: utf-8 -*-
"""R29 回归：K 关 10 槽换脸、名牌、24 关配图、R28 可读性、默认开关、横屏、溢出。"""
import json, os
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont

ROOT='/data/workspace';URL='file://'+ROOT+'/杯雪游戏总站.html'
res={};shots=[]
with sync_playwright() as p:
    br=p.chromium.launch(headless=True,executable_path='/usr/bin/google-chrome',
        args=['--no-sandbox','--disable-web-security','--allow-file-access-from-files'])
    ctx=br.new_context(viewport={'width':420,'height':900},device_scale_factor=1)
    pg=ctx.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(URL,wait_until='load');pg.wait_for_timeout(1000)

    res['K']=pg.evaluate("""()=>{
      if(typeof K_CAST==='undefined')return 'missing';
      const ks=Object.values(K_CAST);
      TAB='K';
      return {slots:ks.length,allInART:ks.every(k=>!!ART[k]),
              names:ks.map(k=>castMeta(k)[0]),
              fallbackHashi:ks.filter(k=>castMeta(k)[0]==='哈士喵').length,
              stage:(()=>{try{return stageFor('K')}catch(e){return 'ERR:'+e}})(),
              art:Object.keys(ART).length};}""")
    res['allLevels']=pg.evaluate("""()=>{
      const ids=D.meta.levels.map(l=>l.id),bad=[];
      for(const k of ids){try{const s=stageFor(k);if(!s||!ART[s.cast])bad.push(k)}catch(e){bad.push(k+':ERR')}}
      return {count:ids.length,bad:bad};}""")
    res['store']=pg.evaluate("()=>storeCheck()")
    res['audio']=pg.evaluate("()=>[localStorage.getItem('beixue_bgm_v2'),localStorage.getItem('beixue_sfx_v2')]")
    res['overflow_portrait']=pg.evaluate("()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth})")

    # 进 K 关
    pg.evaluate("()=>{setTab('K');render();}");pg.wait_for_timeout(700)
    res['K_stage']=pg.evaluate("""()=>{
      const el=document.querySelector('#app .stagecut'),who=document.querySelector('#app .stagewho');
      return {hasCut:!!el,art:el?el.dataset.art:null,who:who?who.textContent:null};}""")
    pg.screenshot(path=ROOT+'/_r29_1_K.png');shots.append(('第十一关 K · 竖屏',ROOT+'/_r29_1_K.png'))

    # 夜雨皮肤下 R28 选中卡可读性仍在
    pg.evaluate("()=>{document.documentElement.setAttribute('data-skin','night');DIFF='collate';render();document.querySelectorAll('details').forEach(d=>d.open=true);}")
    pg.wait_for_timeout(400)
    res['r28_night']=pg.evaluate("""()=>{
      const c=document.querySelector('.d4i.on');if(!c)return 'no card';
      return {bg:getComputedStyle(c).backgroundColor,color:getComputedStyle(c).color,
              lead:getComputedStyle(c.querySelector('.lead')).color};}""")

    # 真横屏
    pg.evaluate("()=>{document.documentElement.classList.add('rot-landscape')}")
    pg.wait_for_timeout(500)
    res['overflow_land']=pg.evaluate("()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,bodyTransform:getComputedStyle(document.body).transform})")
    pg.screenshot(path=ROOT+'/_r29_2_land.png');shots.append(('真横屏 · K 关',ROOT+'/_r29_2_land.png'))
    pg.evaluate("()=>{document.documentElement.classList.remove('rot-landscape')}")

    # 物理横屏
    pg2=ctx.new_page();pg2.set_viewport_size({'width':900,'height':420})
    pg2.on('pageerror',lambda e:errs.append('pg2:'+str(e)))
    pg2.goto(URL,wait_until='load');pg2.wait_for_timeout(800)
    res['overflow_900x420']=pg2.evaluate("()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth})")
    pg2.screenshot(path=ROOT+'/_r29_3_900.png');shots.append(('物理横屏 900×420',ROOT+'/_r29_3_900.png'))
    pg2.close();pg.close();br.close()
res['pageerrors']=errs[:8]
print(json.dumps(res,ensure_ascii=False,indent=2))
open(ROOT+'/_r29_verify.json','w',encoding='utf-8').write(json.dumps(res,ensure_ascii=False,indent=2))

try:fnt=ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',14)
except:fnt=ImageFont.load_default()
cw,ch=300,560
canvas=Image.new('RGB',(cw*3,ch+34),(245,241,232));d=ImageDraw.Draw(canvas)
for i,(lab,path) in enumerate(shots[:3]):
    im=Image.open(path).convert('RGB');im.thumbnail((cw-12,ch-30),Image.LANCZOS)
    canvas.paste(im,(i*cw+(cw-im.width)//2,6))
    d.text((i*cw+10,ch+6),lab,fill=(43,42,38),font=fnt)
canvas.save(ROOT+'/_r29_回归对比.jpg',quality=88,optimize=True)
print('对比图已出')
