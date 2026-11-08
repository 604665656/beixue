# -*- coding: utf-8 -*-
"""R27 浏览器回归：DATA/JS、J关换脸与名牌、借鉴落地函数、默认开关、横屏、溢出。"""
import json, os
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont

ROOT = '/data/workspace'
URL = 'file://' + ROOT + '/杯雪游戏总站.html'
errs = []
res = {}
shots = []

with sync_playwright() as p:
    br = p.chromium.launch(headless=True, executable_path='/usr/bin/google-chrome', args=[
        '--no-sandbox', '--disable-web-security', '--allow-file-access-from-files'])
    ctx = br.new_context(viewport={'width': 420, 'height': 900}, device_scale_factor=1)
    pg = ctx.new_page()
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL, wait_until='load')
    pg.wait_for_timeout(1500)

    res['title'] = pg.title()
    res['DATA'] = pg.evaluate("""()=>{try{return Object.keys(
        JSON.parse(document.getElementById('DATA').textContent))}catch(e){return 'ERR:'+e}}""")
    res['ART'] = pg.evaluate("()=>typeof ART!=='undefined'?Object.keys(ART).length:-1")

    # 借鉴落地：三个命名空间 / 校验 / 命令日志
    res['STORE'] = pg.evaluate("""()=>{
      if(typeof STORE_NS==='undefined')return 'missing';
      const c=storeCheck();
      return {schema:STORE_SCHEMA,
              groups:Object.fromEntries(Object.entries(STORE_NS).map(([k,v])=>[k,v.length])),
              check:c, meta:!!localStorage.getItem(STORE_META_KEY)};}""")
    res['STAGELOG'] = pg.evaluate("""()=>{
      if(typeof STAGE_LOG==='undefined')return 'missing';
      emitStage('verify',{tag:'R27'});
      return stageLogSummary();}""")

    # J 关配图表与名牌
    res['J'] = pg.evaluate("""()=>{
      if(typeof J_CAST==='undefined')return 'missing';
      const ks=Object.values(J_CAST);
      return {slots:ks.length,
              allInART:ks.every(k=>!!ART[k]),
              names:ks.map(k=>{try{TAB='J';return castMeta(k)[0]}catch(e){return 'ERR'}}),
              fallbackHashi:ks.filter(k=>((CAST_META[k]||CAST.find(x=>x[0]===k)||['',''])[0]||'').indexOf('哈士喵')>=0).length,
              stageNow:(()=>{try{return stageFor('J')}catch(e){return 'ERR:'+e}})()};}""")

    # 默认四路音控全关
    res['AUDIO'] = pg.evaluate("""()=>{
      const g=(k)=>{try{return localStorage.getItem(k)}catch(e){return null}};
      return {bgm:g('beixue_bgm_v2'),sfx:g('beixue_sfx_v2'),
              tts:typeof TTS_ON!=='undefined'?TTS_ON:'n/a',
              asr:typeof ASR_ON!=='undefined'?ASR_ON:'n/a'};}""")

    # 溢出：竖屏
    res['overflow_portrait'] = pg.evaluate(
        "()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth})")

    pg.screenshot(path=ROOT + '/_r27_1_hall.png', full_page=False)
    shots.append(('大厅 · 竖屏', ROOT + '/_r27_1_hall.png'))

    # 进 J 关
    enter = pg.evaluate("""()=>{
      for(const fn of ['setTab','go','openLevel','enterLevel','startLevel']){
        if(typeof window[fn]==='function'){try{window[fn]('J');return fn}catch(e){}}
      }
      return 'none';}""")
    res['enter_J'] = enter
    pg.wait_for_timeout(900)
    res['J_stage'] = pg.evaluate("""()=>{
      const el=document.querySelector('#app .stagecut');
      const who=document.querySelector('#app .stagewho');
      return {hasCut:!!el, art:el?el.dataset.art:null, who:who?who.textContent:null,
              log:stageLogSummary(),
              meta:(()=>{const c=stageFor('J').cast;return {cast:c,name:castMeta(c)[0],sub:castMeta(c)[1]}})()};}""")
    pg.screenshot(path=ROOT + '/_r27_2_J.png', full_page=False)
    shots.append(('第十关 J · 舞台', ROOT + '/_r27_2_J.png'))

    # 真横屏
    pg.evaluate("()=>{document.documentElement.classList.add('rot-landscape')}")
    pg.wait_for_timeout(600)
    res['overflow_land'] = pg.evaluate(
        "()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,"
        "bodyTransform:getComputedStyle(document.body).transform})")
    pg.screenshot(path=ROOT + '/_r27_3_land.png', full_page=False)
    shots.append(('真横屏 · J 关', ROOT + '/_r27_3_land.png'))
    pg.evaluate("()=>{document.documentElement.classList.remove('rot-landscape')}")

    # 981x420 物理横屏另开一页
    pg2 = ctx.new_page()
    pg2.set_viewport_size({'width': 900, 'height': 420})
    pg2.on('pageerror', lambda e: errs.append('pg2:' + str(e)))
    pg2.goto(URL, wait_until='load')
    pg2.wait_for_timeout(900)
    res['overflow_900x420'] = pg2.evaluate(
        "()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth})")
    pg2.screenshot(path=ROOT + '/_r27_4_900.png', full_page=False)
    shots.append(('物理横屏 900×420', ROOT + '/_r27_4_900.png'))
    pg2.close()

    br.close()

res['pageerrors'] = errs[:10]
print(json.dumps(res, ensure_ascii=False, indent=2)[:4000])

# 拼对比图
try:
    fnt = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy-microhei.ttc', 15)
except Exception:
    fnt = ImageFont.load_default()
cellw, cellh = 300, 560
canvas = Image.new('RGB', (cellw * 4, cellh + 34), (245, 241, 232))
d = ImageDraw.Draw(canvas)
for i, (lab, path) in enumerate(shots):
    im = Image.open(path).convert('RGB')
    im.thumbnail((cellw - 12, cellh - 30), Image.LANCZOS)
    x = i * cellw + (cellw - im.width) // 2
    canvas.paste(im, (x, 6))
    d.text((i * cellw + 10, cellh + 6), lab, fill=(43, 42, 38), font=fnt)
canvas.save(ROOT + '/_r27_回归对比.jpg', quality=88, optimize=True)
print('对比图已出')

open(ROOT + '/_r27_verify.json', 'w', encoding='utf-8').write(
    json.dumps(res, ensure_ascii=False, indent=2))
