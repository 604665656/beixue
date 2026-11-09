
if(window.self!==window.top)document.body.classList.add('embedded');
const D = JSON.parse(document.getElementById('DATA').textContent);
const ART = {"cover":"./assets/845002dce80d0afc.jpg","A":"./assets/dd141f25d8a78c84.jpg","B":"./assets/2e3fafe3846bd413.jpg","C":"./assets/c4aec6b2359f911f.jpg","D":"./assets/304eb317acf4b0c3.jpg","cat":"./assets/b6f6e9238cf7995d.jpg","cat3":"./assets/62c3526b83bf4b77.jpg","catorg":"./assets/64049b9486815d6e.jpg","catav":"./assets/a026a4c1e5f4ea02.jpg","bg_rain":"./assets/59900e5a1c628b84.jpg","bg_huai":"./assets/a545875b8159a83a.jpg","bg_yuanmen":"./assets/80196b531e0db451.jpg","bg_qinhuai":"./assets/f1d8cbeb3116b58e.jpg","bg_qilipu":"./assets/b8f849908995e110.jpg","bg_dujiang":"./assets/3793d3a85a7fe33d.jpg","bg_shulou":"./assets/9d9e808948f90fdd.jpg","bg_haodenglou":"./assets/3f3fd1a2cec9581c.jpg","bg_bailuzhou":"./assets/4701cdf79ba3a71f.jpg","bg_dashipo":"./assets/8d059872109ba9b9.jpg","bg_moling":"./assets/daee341027433542.jpg","cos_luo":"./assets/24b304d325c455d5.webp","cos_shen":"./assets/04b39100be653f09.webp","cos_jin":"./assets/45161d536583ade2.webp","cos_geng":"./assets/92b0a1609caa408d.webp","cos_qinwen":"./assets/f851e4090f430083.webp","cos_jinhe":"./assets/e19b5407aea287ab.webp","cos_ying":"./assets/3325108811762088.webp","cos_yi":"./assets/a0a2eb7508818c28.webp","cos_du":"./assets/9343387fb694dede.webp","cos_jiao":"./assets/c3b98a7d2823e1c7.webp","cos_gbx":"./assets/4c57821ba4ddb96c.webp","cos_qu":"./assets/f58b5104c572098f.webp","cos_yuancl":"./assets/2ea8b93bc75082ed.webp","cos_yuaner":"./assets/8da1166f26330a55.webp","cos_xiao":"./assets/ce926f6a527ac022.webp","cos_zhu":"./assets/a6bb7a46bb212035.webp","fx_rain":"./assets/2b50dbeb112f4ae4.webp","fx_splash":"./assets/0d12a31584365771.webp","fx_snow":"./assets/486792b9c383ae25.webp","fx_ray":"./assets/924ed054b50c4f22.webp","fx_bird_up":"./assets/3bd6d2c0e940dc10.webp","fx_bird_flat":"./assets/ef1e72386d5bcf23.webp","fx_bird_down":"./assets/c21237429030af9d.webp","fx_reed":"./assets/8b89f987ec7a9004.webp","fx_lamp":"./assets/d77a8cdf6c4ac2bb.webp","fx_flag":"./assets/e66ab5a1d8932248.webp","fx_dust":"./assets/89f71c642b3b1310.webp","fx_wind":"./assets/d2acbe92df2b47ee.webp","fx_snowedge":"./assets/0f8fb3297f85f358.webp","fx_firefly":"./assets/22916337b37d3c89.webp","fx_flag2":"./assets/5219ed61185ac07c.webp","fx_flag3":"./assets/7de311289bddbd83.webp","cos_shen_argue":"./assets/7bcf7e8093431c0b.webp","cos_luo_draw":"./assets/734906f31e6b3e41.webp","cos_yi_grief":"./assets/b2131bf820417ec1.webp","cos_zhu_resolve":"./assets/dbdfdd5de5438e91.webp","cos_base":"./assets/30468998616795cc.webp","cos_wen":"./assets/6cdfd6dee4e977c1.webp","cos_mi":"./assets/28f526c5c754d7b8.webp","cos_shi":"./assets/4429ad57403798e9.webp","cos_zwl":"./assets/761bb701988731b4.webp","cos_tian":"./assets/7dbb16f32cd8b08f.webp","cos_tie":"./assets/a590f2d11a6a1697.webp","cos_shen_calm":"./assets/356490f91cbd901e.webp","cos_shen_shrug":"./assets/311133b45559819e.webp","cos_luo_nod":"./assets/7324f05cb8013ae3.webp","cos_luo_guard":"./assets/6d6ad0ed22c7ac4c.webp","cos_yi_cup":"./assets/3f7fd0ff16541eba.webp","cos_jin_guard":"./assets/3f8bd9b1783e0228.webp","cos_zhu_smile":"./assets/2857c64facf9fc61.webp","cos_zhu_turn":"./assets/9c9d7988507da1df.webp","cos_xiao_sigh":"./assets/15a2366a7bd69127.webp","cos_qinwen_wry":"./assets/c024607995bf0c58.webp","fx_ripple1":"./assets/dc60c6e2e5f9a281.webp","fx_ripple2":"./assets/4461f8e05f0ccc07.webp","fx_ripple3":"./assets/86a6f1a6e8bddf93.webp","fx_nod1":"./assets/9c588bfdaa04f354.webp","fx_nod2":"./assets/293b476f60257580.webp","fx_nod3":"./assets/525b1155f62a446c.webp","fx_shake1":"./assets/4c9d8c29f6fbfc7c.webp","fx_shake2":"./assets/95c43643a48a739f.webp","fx_shake3":"./assets/045a0ac25b601628.webp","fx_breath1":"./assets/9b89f06752f0b9f8.webp","fx_breath2":"./assets/049e7a4e3228c95d.webp","cos_yuancl_agree":"./assets/942c73213e96035a.webp","cos_wen_sly":"./assets/7943539421aad339.webp","cos_xiao_sing":"./assets/df808559d7b0a70f.webp","cos_geng_trust":"./assets/88c164b3ded465d4.webp","cos_qinwen_smash":"./assets/dabeb087bd86e168.webp","cos_jinhe_laugh":"./assets/32895b7b4d71c041.webp","cos_ying_sing":"./assets/14387dd1d4454939.webp","cos_tian_wink":"./assets/515a1a844642dffc.webp","act_draw":"./assets/91b2d8e955419040.webp","act_sheathe":"./assets/738e6eefbe52da3d.webp","act_write":"./assets/8d9e8c8925f62e06.webp","act_push":"./assets/0766c20259a07a18.webp","act_curtain":"./assets/3d40afefef21a06e.webp","act_jade":"./assets/836a675f4511e2fb.webp","act_ledger":"./assets/0b7cf7cf6138a580.webp","act_lamp":"./assets/995ef4f6ef0f23bf.webp","act_flag":"./assets/4e9741b6422d6d1c.webp","act_cup":"./assets/e8e94b950c3de16a.webp","act_slam":"./assets/0c9dd6163b15cdfb.webp","cos_yuancl_warm":"./assets/bf83927e2f6a13cc.webp","cos_qinwen_wry2":"./assets/29e46869b041e625.webp","cos_ying_clear":"./assets/90369d35db60225e.webp","cos_jinhe_calm":"./assets/440281758391142e.webp","cos_yuaner_vain":"./assets/ce1a7d3b714af927.webp","cos_wen_lose":"./assets/a12ca73861b3a963.webp","cos_zwl_firm":"./assets/da591ccdced3c7bc.webp","cos_tian_serious":"./assets/84c91c13a6f09680.webp","act_turn":"./assets/da2871a293b03b96.webp","act_umbrella":"./assets/93e60e39e154f235.webp","E_face_wink":"./assets/e981486c05ad0828.webp","E_face_tear":"./assets/aed2cdd1432d88d3.webp","E_act_cup":"./assets/694b7e24779137e6.webp","E_act_mirror":"./assets/1ea01daea0956ea0.webp","E_seq_open":"./assets/36c7694ac886c3d2.webp","E_seq_blink":"./assets/2942609e8bb70f88.webp","E_seq_talk":"./assets/a3db7d8cdb9511cf.webp","E_seq_nod":"./assets/f0abea3109d8b877.webp","E_seq_ear":"./assets/a52a9872917dbe62.webp","E_seq_tail":"./assets/338438dbdb60501c.webp","A_face_shen":"./assets/c606cabcf281ebf6.webp","A_face_argue":"./assets/4ef955529432c842.webp","A_face_jin":"./assets/1f0ff05b7b876951.webp","A_face_guard":"./assets/64c96550764d0d51.webp","A_face_ying":"./assets/21d98b33df6b674d.webp","A_face_geng":"./assets/e382ce73e0a91912.webp","A_face_luo":"./assets/fe8f7716b9c20398.webp","A_face_draw":"./assets/3474e4a6bc08dcc6.webp","A_seq_open":"./assets/a994e8285f16f01f.webp","A_seq_blink":"./assets/347adca57bea5649.webp","B_face_qinwen":"./assets/41bb756e26dcb91f.webp","B_face_luohan":"./assets/105f0ec9ff82443a.webp","B_face_du":"./assets/2650f35e3ade1e55.webp","B_face_jiao":"./assets/a3c8a426fc21f0b1.webp","B_face_yi":"./assets/496c5d48b9435f6c.webp","B_face_yuane":"./assets/68da44cae5a08da8.webp","B_act_push":"./assets/15e585dd9cf9954b.webp","B_act_smash":"./assets/92e6f1f18c118ee9.webp","B_seq_open":"./assets/ddb6c7cae132f050.webp","B_seq_blink":"./assets/ac6c155f1cc77ba3.webp","D_face_xiaoru":"./assets/16f7ce654c1a881c.webp","D_face_zhuyan":"./assets/76a54b5c3f54d18a.webp","D_face_yi":"./assets/e637618718f62ff4.webp","D_face_luohan":"./assets/1939857717e28fc1.webp","D_face_shen":"./assets/4a475c407f111611.webp","D_face_yuancl":"./assets/94ccc942f155608a.webp","D_act_write":"./assets/98039e324feaa93f.webp","D_act_lamp":"./assets/5ffe354d6c3badfe.webp","D_seq_open":"./assets/980f9c2ea1c9b518.webp","D_seq_blink":"./assets/bf8e4bfa421f0912.webp","F_seq_half":"./assets/b60f8db4375b75d0.webp","F_seq_quarter":"./assets/9b40f8d213be1492.webp","F_seq_threeq":"./assets/e69ab3b4d44ecf0c.webp","F_seq_nod_mid":"./assets/bd868666030cce05.webp","F_seq_talk_mid":"./assets/5c70fed63e054c34.webp","F_seq_ear_mid":"./assets/97491415f828bc07.webp","F_seq_tail_mid":"./assets/1df5f188e6754557.webp","F_seq_cross":"./assets/e2e44b72a6c0286d.webp","F_breath_in":"./assets/ca8293fad8ec7717.webp","F_breath_out":"./assets/71fce182cd2e2407.webp","G_face_verify":"./assets/17eaaf9ce8bd151f.webp","G_face_compare":"./assets/36de7b31a1d96e64.webp","G_face_brush":"./assets/e4d2010c7526c74a.webp","G_face_startled":"./assets/1e44ebf1263904e7.webp","G_face_close":"./assets/0c8e338bd637bd00.webp","G_face_smile":"./assets/6d74c07c63c93b4b.webp","G_act_turn":"./assets/80c2f0cfc8b81296.webp","G_act_scroll":"./assets/ca6d4e742b75af7c.webp","G_seq_blink":"./assets/9eddde13123dbe75.webp","G_seq_open":"./assets/595c5eb76c24d7a9.webp","H_cost_jin":"./assets/d0b075ee61a162a2.webp","H_cost_ying":"./assets/5510834fba4fe590.webp","H_cost_geng":"./assets/907ae20447df6970.webp","H_cost_yuaner":"./assets/f189c1906e83da7d.webp","H_cost_luo":"./assets/9c4238433edcc9de.webp","H_cost_jinhe":"./assets/2ee430502d157f99.webp","H_cost_qinwen":"./assets/2fa3f39093863a22.webp","H_cost_shi":"./assets/c68a3e22d1942e49.webp","H_cost_yuchi":"./assets/f388674b12ff5521.webp","G_cost_verify":"./assets/631c602ad09c270a.webp","G_cost_compare":"./assets/69830ed1d6829b25.webp","G_cost_brush":"./assets/4404d9e5ea73acbf.webp","G_cost_startled":"./assets/33dca65b5dfb9353.webp","G_cost_smile":"./assets/d61b5ecb427e4b5f.webp","G_cost_turn":"./assets/2d6caefb6c70752c.webp","G_cost_scroll":"./assets/a4bb3f1a93af8380.webp","G_cost_blink":"./assets/9fb21559e0c955e2.webp","G_cost_open":"./assets/14a5d949922f6192.webp","HR_geng":"./assets/77e86e08557545cf.webp","HR_qinwen":"./assets/0ac56933713e37c7.webp","HR_shen":"./assets/1f086a0f9f47afa8.webp","HR_xiao":"./assets/25f86cedbf6f34bd.webp","HR_yi":"./assets/5d4605349cf64c34.webp","HR_ying":"./assets/f234392bd6927191.webp","HR_yuancl":"./assets/7357c950e12c09fa.webp","R22_geng":"./assets/1b0e6e493468d4ac.webp","R22_jiao":"./assets/6a8f09db7addfe6a.webp","R22_jin":"./assets/76be78e6a4081e37.webp","R22_qinwen":"./assets/d04d3bc7c792a4fa.webp","R22_yuancl":"./assets/acac44bf08b0bca1.webp","R22_zhu":"./assets/61267c33415cb4a7.webp","R23_lip_zhu":"./assets/8e60708e20460303.webp","R23_lip_xiao":"./assets/0e7e533393d70ee6.webp","R23_build_yuancl":"./assets/6194d19fc62c631f.webp","R23_build_yi":"./assets/c520544440a27938.webp","R23_build_jinhe":"./assets/ab5c4321b82c4b44.webp","R23_act_carry":"./assets/0f2bda9b2211e814.webp","R22_du":"./assets/d95743c18bf7b3a7.webp","R22_jinhe":"./assets/cce4f66e40978199.webp","R22_luo":"./assets/1d61c26ffaec39fb.webp","R25_lip_zhu":"./assets/44faa82e1be60cc0.webp","R25_lip_xiao":"./assets/b37fa08da8ff8fc1.webp","R25_lip_ying":"./assets/cb80398c5917a7da.webp","R25_scar_yuancl":"./assets/81fb6b34d700cce9.webp","R25_scar_jiao":"./assets/d7d798def1cc3073.webp","R25_act_sleeve":"./assets/7c86a9dbf1edc18b.webp","R25_I_zhu":"./assets/b9f6bb8db6bc4a60.webp","R25_I_ying":"./assets/2643aac066cffd94.webp","R26_J_read":"./assets/c0c8bc789167d2c1.webp","R26_J_fit":"./assets/bc245f03f03c7b5e.webp","R26_J_brush":"./assets/c633b5fff7418c09.webp","R26_J_compare":"./assets/c66a6bb42fe4c304.webp","R26_J_startled":"./assets/bf7b4cfb5a250eaa.webp","R26_J_done":"./assets/668f2152830c1b79.webp","R26_J_turn":"./assets/ff6e2de8ca8cbdf7.webp","R26_J_lamp":"./assets/d3cf15c575f1ff45.webp","R29_K_read":"./assets/750f7b3a663b3a43.webp","R29_K_brush":"./assets/cd5f1124e872f4a3.webp","R29_K_compare":"./assets/af3887a110494e02.webp","R29_K_pause":"./assets/32a3154aea6a6990.webp","R29_K_ah":"./assets/30772b3c73a917d8.webp","R29_K_cup":"./assets/c39b4a589ef69ebe.webp","R29_K_bridge":"./assets/f8f8a11f8ad15120.webp","R29_K_check":"./assets/d56ce59fb22befe5.webp","R29_K_smile":"./assets/4f4ca7399cf65722.webp","R29_K_done":"./assets/ed5019b159c0827a.webp"};
const $ = (s,r=document)=>r.querySelector(s);
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const nl = s => esc(s).replace(/\n/g,'<br>');

/* ---------- storage ---------- */
/* 声音状态与难度先声明，供下面的读取逻辑使用 */
let BGM=0, SFX=0, DIFF='read';
const KEY='beixue_games_v1', MKEY='beixue_mode_v1', BKEY='beixue_bgm_v2', FKEY='beixue_sfx_v2',
      DKEY='beixue_diff_v1', PKEY='beixue_prog_v1', LKEY='beixue_last_v1', TKEY='beixue_streak_v1';
const QKEYS = D.meta.levels.filter(l=>'GHIJKLMNOPQRSTUVWX'.includes(l.id)).map(l=>l.id);
let MEM={}, PROG={}, STREAK={fail:0,perfect:0};
QKEYS.concat(['A','B','C','D','E','F']).forEach(k=>MEM[k]=null);
try{ const r=localStorage.getItem(TKEY); if(r)STREAK=Object.assign(STREAK,JSON.parse(r)||{}); }catch(e){}
try{ const r=localStorage.getItem(KEY); if(r) MEM=Object.assign(MEM,JSON.parse(r)); }catch(e){}
try{ const r=localStorage.getItem(PKEY); if(r) PROG=JSON.parse(r)||{}; }catch(e){}
try{ const v=localStorage.getItem(BKEY); if(v!==null)BGM=Math.min(2,Math.max(0,+v||0)); }catch(e){}
try{ const v=localStorage.getItem(FKEY); if(v!==null)SFX=(+v===1)?1:0; }catch(e){}
function save(k,v){ MEM[k]=v; try{localStorage.setItem(KEY,JSON.stringify(MEM));}catch(e){} }
function saveProg(){ try{localStorage.setItem(PKEY,JSON.stringify(PROG));}catch(e){} }
/* ---------- 借鉴 Ren'Py / Naninovel / ink：状态分层（P0） ----------
   旧键一个不改、数据零迁移，只建立命名空间索引 + schema 版本 + 校验。
   进度=业务数据；偏好=用户设置；视图=可随时丢弃并由内容状态重建。
   这是「视图状态被当成进度状态硬 clamp」（R24 横屏 bug）的根治入口。 */
const STORE_SCHEMA=1, STORE_META_KEY='beixue_store_meta_v1';
const STORE_NS={
 progress:['beixue_games_v1','beixue_prog_v1','beixue_last_v1','beixue_streak_v1'],
 preferences:['beixue_mode_v1','beixue_diff_v1','beixue_bgm_v2','beixue_sfx_v2','beixue_skin_v2',
   'beixue_breathe_v1','beixue_vib_v1','beixue_perf_gate_v1','beixue_fxmode_v1','beixue_wxpick_v1',
   'beixue_bubop_v1','beixue_tts_v1','beixue_asr_v1'],
 view:['beixue_spr_v1','beixue_bublay_v1','beixue_hallbg_v1','beixue_layout_v1']
};
function storeMeta(){
 try{
  const raw=localStorage.getItem(STORE_META_KEY);
  if(raw){const o=JSON.parse(raw);if(o&&o.schema===STORE_SCHEMA)return o;}
  const o={schema:STORE_SCHEMA,ns:STORE_NS,migratedFrom:'legacy-flat-keys',at:Date.now()};
  localStorage.setItem(STORE_META_KEY,JSON.stringify(o));return o;
 }catch(e){return {schema:STORE_SCHEMA,ns:STORE_NS,offline:true};}
}
function storeCheck(){
 const bad=[];let n=0;
 for(const ns of Object.keys(STORE_NS))for(const k of STORE_NS[ns]){
  let raw=null;try{raw=localStorage.getItem(k);}catch(e){continue}
  if(raw===null)continue;n++;
  /* 标量存档（如皮肤名 'night'、数值 '1'）是合法的，只有以 JSON 结构起头却解析失败才算损坏 */
  const t=raw.trim();
  if(/^[\[{"']/.test(t)){try{JSON.parse(raw);}catch(e){bad.push({ns:ns,key:k,why:'JSON 结构损坏'});}}
 }
 return {schema:STORE_SCHEMA,scanned:n,bad:bad,ok:bad.length===0};
}
function storeResetView(){
 let n=0;for(const k of STORE_NS.view){try{if(localStorage.getItem(k)!==null){localStorage.removeItem(k);n++;}}catch(e){}}
 return n;
}
storeMeta();

function markClear(k,stars,note){
 if(isRoam())return;
 /* 难度曲线：前三关不卡满星，留出「进入状态」的余量 */
 if(['E','A','B'].includes(k))stars=Math.min(stars,2);
 const p=PROG[k]||{stars:0,done:false};
 p.stars=Math.max(p.stars||0,stars); p.done=true; if(note)p.note=note;
 PROG[k]=p; saveProg();
 /* 动态升降档：连败两关给降档／加提示；连满星三关给升档 */
 if(stars<=1){STREAK.fail++;STREAK.perfect=0;}
 else if(stars>=3){STREAK.perfect++;STREAK.fail=0;}
 else {STREAK.fail=0;STREAK.perfect=0;}
 try{localStorage.setItem(TKEY,JSON.stringify(STREAK));}catch(e){}
 syncHctl();
}
function levelTail(k){
 let h='';
 const nextD={skim:'read',read:'collate',collate:null}[DIFF];
 if(STREAK.fail>=2&&DIFF!=='skim')
  h+=`<div class="steer"><b>连着两关只拿 1 星</b>　不必硬扛。可以降一档先把故事走顺，也可以保持难度、加一层脚手架。<div class="btnrow" style="margin-top:9px">
   <button class="btn ghost sm" data-act="diff_set" data-v="skim">降到 ◔ 浅读</button>
   <button class="btn ghost sm" data-act="mode_set" data-v="newbie">切到 ◈ 新手模式</button></div></div>`;
 else if(STREAK.perfect>=3&&nextD)
  h+=`<div class="steer"><b>连着三关满星</b>　当前 ${esc(diffInfo().name)}，要不要把题库开深一层？<div class="btnrow" style="margin-top:9px">
   <button class="btn ghost sm" data-act="diff_set" data-v="${nextD}">升到 ${esc(D.meta.diffs[nextD].icon+' '+D.meta.diffs[nextD].name)}</button></div></div>`;
 return h;
}
function totalStars(){ return D.meta.levels.reduce((s,l)=>s+((PROG[l.id]||{}).stars||0),0); }
function maxStars(){ return D.meta.levels.length*3; }
function clearedCount(){ return D.meta.levels.filter(l=>(PROG[l.id]||{}).done).length; }
function allCleared(){ return clearedCount()>=D.meta.levels.length; }
/* 难度：题库深度 / 星级阈值 / 挑战容忍 */
function tierMax(){ return ({skim:1,read:2,collate:3})[DIFF]||2; }
function qTier(q){ return q.tier||1; }
function quizFor(arr){ return arr.filter(q=>qTier(q)<=tierMax()); }
function starThresholds(){
 return ({skim:[0.55,0.8],read:[0.7,0.9],collate:[0.8,0.95]})[DIFF]||[0.7,0.9];
}
function starsByRatio(right,total){
 const [t2,t3]=starThresholds(), r=total?right/total:0;
 return r>=t3?3:r>=t2?2:1;
}
function challengeAllowance(){ return ({skim:2,read:1,collate:0})[DIFF]; }
function diffNote(){
 return ({skim:'浅读 · 只出基础题，判定最宽',
          read:'通读 · 基础＋进阶题，标准判定',
          collate:'校勘 · 全题库含考据题，判定最严'})[DIFF]||'';
}
function archUnlocked(def){
 if(!def.need)return true;
 if(def.need==='ALL')return allCleared();
 if(!!(PROG[def.need]||{}).done)return true;
 const vol=D.meta.volumes.find(v=>v.ids.includes(def.need)); /* 卷页由卷内任一关开启 */
 return vol?vol.ids.some(id=>(PROG[id]||{}).done):false;
}
function archUnlockedCount(){ return D.meta.archDefs.filter(archUnlocked).length; }
function archTotal(){ return D.meta.archDefs.length; }
function archNeedLabel(def){
 if(!def.need)return '';
 if(def.need==='ALL')return '二十四关全部通关';
 const l=D.meta.levels.find(x=>x.id===def.need);
 return l?(l.no+'《'+l.t+'》'):'对应关卡';
}
function unlockNote(k){
 const def=D.meta.archDefs.find(x=>x.need===k);
 return def?'🔓 已解锁档案《'+def.label+'》':'';
}
function grade(m){ return m===0?'S':m===1?'A':m===2?'B':'C'; }
let MODE='newbie';
try{ const m=localStorage.getItem(MKEY); if(['newbie','normal','challenge','roam'].includes(m))MODE=m; }catch(e){}
function isNew(){ return MODE==='newbie'; }
function isChallenge(){ return MODE==='challenge'; }
function isRoam(){ return MODE==='roam'; }
function showGuide(){ return MODE==='newbie'||DIFF==='skim'; }
function showPause(){ return MODE==='newbie'; }
function showRec(){ return MODE==='newbie'||DIFF==='skim'; } /* 浅读时 B 直接标建议动作 */
/* 难度也管前六关的脚手架：浅读放宽、校勘收紧 */
function askLimit(){
 if(isRoam())return Infinity;
 if(DIFF==='skim')return Infinity;
 if(DIFF==='collate')return 0;
 return (isNew())?Infinity:(isChallenge()?0:4);
}
function hintLimit(){
 if(isRoam())return Infinity;
 if(DIFF==='skim')return Infinity;
 if(DIFF==='collate')return 0;
 return (isNew())?Infinity:(isChallenge()?0:1);
}
function dQuiz(){ /* 博闻关：浅读取前 8 题，其余全 12 题 */
 return DIFF==='skim'?D.D.quiz.slice(0,8):D.D.quiz;
}
function modeInfo(){ return D.meta.modes[MODE]; }
function setMode(m){
 if(!D.meta.modes[m])return;
 MODE=m; try{localStorage.setItem(MKEY,m);}catch(e){}
 syncHctl(); renderModePanel(); render();
}
function diffInfo(){ return D.meta.diffs[DIFF]; }
function setDiff(k){
 if(!D.meta.diffs[k])return;
 DIFF=k; try{localStorage.setItem(DKEY,k);}catch(e){}
 syncHctl(); renderDiffPanel(); render();
}
function syncHctl(){
 const _setOpen=$('#a11yPanel')&&!$('#a11yPanel').hidden;
 const c=$('#modeChip'), bg=$('#bgmBtn'), fx=$('#sfxBtn'),
       p=$('#progChip'), dc=$('#diffChip'), m=modeInfo(), df=diffInfo(),
       tb=$('#ttsBtn'), ab=$('#asrBtn'), ay=$('#a11yBtn');
 if(c){ c.textContent=m.icon+' '+m.name; c.classList.toggle('on',isNew()); }
 if(bg){ bg.textContent=bgmLabel(); bg.title='关 → 随场景自动换音景 → 音景＋琴音（当前 '+sceneLabel+'）'; bg.classList.toggle('on',BGM>0); }
 if(fx){ fx.textContent=SFX?'♪ 音效·开':'♪ 音效·关'; fx.classList.toggle('on',SFX>0); }
 if(tb){ tb.textContent='🔊 朗读·'+(TTS?'开':'关'); tb.classList.toggle('on',TTS>0); }
 if(_setOpen)renderA11yPanel();
 if(ab){ ab.textContent='🎙 语音·'+(ASR?'开':'关'); ab.classList.toggle('on',ASR>0); }
 if(ay){ ay.classList.toggle('on',!!(HC||BIG||REDUCE)); ay.setAttribute('aria-pressed',!!(HC||BIG||REDUCE)?'true':'false'); }
 if(dc){ dc.textContent=df.icon+' '+df.name; dc.classList.toggle('on',DIFF!=='read'); }
 if(p){ p.textContent='★ '+totalStars()+'/'+maxStars(); }
 $('nav')&&$('nav').querySelectorAll('button').forEach(x=>x.classList.toggle('on',x.dataset.nav===TAB));
}
function renderDiffPanel(){
 const p=$('#diffPanel'); if(!p)return;
 p.innerHTML='<div class="mp-h">阅 读 难 度 · 二十四关通用</div>'+
  D.meta.diffOrder.map(k=>{const d=D.meta.diffs[k];
   return `<button class="mp-i ${DIFF===k?'on':''}" data-act="diff_set" data-v="${k}"><b>${d.icon} ${d.name}${DIFF===k?'　✓':''}</b><span>${esc(d.lead)}｜${esc(d.perks.join(' · '))}</span></button>`;
  }).join('')+'<div class="mp-h" style="padding:6px 4px 0;border-top:1px dashed var(--line)">难度管「考什么、判多严」，与模式（怎么读）互不干扰</div>';
}
function renderModePanel(){
 const p=$('#modePanel'); if(!p)return;
 p.innerHTML='<div class="mp-h">游 戏 模 式 · 二十四关通用</div>'+
  D.meta.modeOrder.map(k=>{const m=D.meta.modes[k];
   return `<button class="mp-i ${MODE===k?'on':''}" data-act="mode_set" data-v="${k}"><b>${m.icon} ${m.name}${MODE===k?'　✓':''}</b><span>${esc(m.lead)}｜${esc(m.perks.join(' · '))}</span></button>`;
  }).join('')+'<div class="mp-h" style="padding:6px 4px 0;border-top:1px dashed var(--line)">随时可改，正在玩的一局会立刻跟随</div>';
}

/* ---------- 离线合成声音（Web Audio，无外部音频） ----------
   BGM = 背景音 0 关 / 1 雨声 / 2 琴音＋雨声
   SFX = 点击音效 0 关 / 1 开
   两者完全独立：关掉背景音仍可有音效，关掉音效背景音照常。 */
let AC=null, rainSrc=null, rainGain=null, qinTimer=null;
try{ const v=localStorage.getItem(DKEY); if(v&&D.meta&&D.meta.diffs&&D.meta.diffs[v])DIFF=v; }catch(e){}
const PENTA=[261.63,293.66,329.63,392.00,440.00,523.25,587.33];
function initAC(){
 if(!AC){ const C=window.AudioContext||window.webkitAudioContext; if(!C)return false;
  AC=new C(); }
 if(AC.state==='suspended')AC.resume(); return true;
}
function noiseBuffer(){
 const len=Math.floor(AC.sampleRate*2), b=AC.createBuffer(1,len,AC.sampleRate), d=b.getChannelData(0);
 for(let i=0;i<len;i++)d[i]=(Math.random()*2-1)*0.32;
 return b;
}
/* 场景音景：同一套雨/水/风噪声，靠滤波与增益调出不同场景，实时合成无音频文件 */
const SCENE_SOUND={
 rain:[760,.4,.055,'雨驿'],qilipu:[620,.5,.050,'驿道秋雨'],haodenglou:[820,.35,.048,'临安夜雨'],
 shulou:[300,.3,.022,'书楼极静'],dujiang:[320,.7,.052,'渡口水声'],bailuzhou:[380,.6,.048,'芦荡风过'],
 huai:[480,.5,.046,'淮上夜帐'],yuanmen:[420,.6,.050,'辕门朔风'],dashipo:[360,.7,.048,'石阵风雪'],
 moling:[300,.6,.044,'秣陵雪风'],qinhuai:[700,.4,.046,'秦淮灯影']
};
let sceneFilter=null, sceneLabel='雨驿';
function startRain(bg){
 if(!AC)return;
 const cfg=SCENE_SOUND[bg]||SCENE_SOUND.rain;
 const src=AC.createBufferSource(); src.buffer=noiseBuffer(); src.loop=true;
 const lp=AC.createBiquadFilter(); lp.type='lowpass'; lp.frequency.value=cfg[0]; lp.Q.value=cfg[1];
 const g=AC.createGain(); g.gain.value=0;
 src.connect(lp); lp.connect(g); g.connect(AC.destination); src.start();
 g.gain.linearRampToValueAtTime(cfg[2],AC.currentTime+1.1);
 rainSrc=src; rainGain=g; sceneFilter=lp; sceneLabel=cfg[3];
}
/* 换关不重启节点，只平滑改滤波与音量，听感上像镜头推进 */
function retuneScene(bg){
 const cfg=SCENE_SOUND[bg]||SCENE_SOUND.rain;
 sceneLabel=cfg[3];
 const _k=sceneWeather(bg).amb;
 if(_k!==ambKind)startAmbient(bg);
 if(!AC||!sceneFilter||!rainGain)return;
 const t=AC.currentTime;
 try{
  sceneFilter.frequency.linearRampToValueAtTime(cfg[0],t+.9);
  sceneFilter.Q.linearRampToValueAtTime(cfg[1],t+.9);
  rainGain.gain.linearRampToValueAtTime(cfg[2],t+.9);
 }catch(e){}
}
function currentSceneBg(){
 try{ return stageFor(TAB).bg||'rain'; }catch(e){ return 'rain'; }
}
function fxOk(){ if(!SFX||!initAC())return; pluck(PENTA[2],.026,.30);
 setTimeout(()=>pluck(PENTA[4],.022,.42),95); }
function fxNo(){ if(!SFX||!initAC())return; pluck(PENTA[1],.030,.34);
 setTimeout(()=>pluck(PENTA[0],.020,.40),110); }
function pluck(freq,vol,dur){
 if(!AC)return;
 const t=AC.currentTime, o=AC.createOscillator(), g=AC.createGain(), lp=AC.createBiquadFilter();
 o.type='triangle'; o.frequency.value=freq;
 lp.type='lowpass'; lp.frequency.value=1500;
 g.gain.setValueAtTime(0.0001,t);
 g.gain.exponentialRampToValueAtTime(vol,t+.012);
 g.gain.exponentialRampToValueAtTime(.0001,t+dur);
 o.connect(lp); lp.connect(g); g.connect(AC.destination);
 o.start(t); o.stop(t+dur+.05);
}
function startQin(){
 let step=0;
 const tick=()=>{
  const seq=[0,2,4,3,1,5,4,2,0,3,6,4];
  const f=PENTA[seq[step%seq.length]];
  pluck(f,.045,1.5);
  if(step%4===2)setTimeout(()=>pluck(PENTA[(seq[(step+2)%seq.length]+2)%PENTA.length],.022,1.1),260);
  step++;
 };
 tick(); qinTimer=setInterval(tick,1250);
}
function stopAll(){
 if(qinTimer){clearInterval(qinTimer);qinTimer=null;}
 if(rainGain&&AC){try{rainGain.gain.linearRampToValueAtTime(.0001,AC.currentTime+.35);}catch(e){}}
 const old=rainSrc;
 if(old){setTimeout(()=>{try{old.stop();}catch(e){}},480); rainSrc=null;}
 sceneFilter=null; stopAmbient();
}
function setBGM(s){
 BGM=s; try{localStorage.setItem(BKEY,String(s));}catch(e){}
 stopAll();
 if(s>0){ if(!initAC()){BGM=0;} else { startRain(audioBg()); if(s>1)startQin(); startAmbient(audioBg()); } }
 else stopAmbient();
 syncHctl();
}
function cycleBGM(){ setBGM((BGM+1)%3); }
function bgmLabel(){
 if(!BGM)return '♫ 场景音·关';
 const amb=AMB_LABEL[sceneWeather(audioBg()).amb]||'';
 const pick=WXPICK&&WXPICK!=='auto'?(WXLIST.find(x=>x[0]===WXPICK)||['',''])[1].split(' · ')[0]:'';
 return '♫ '+(pick||sceneLabel)+(BGM>1?'＋琴':(amb?'·'+amb:''));
}
function setSFX(s){
 SFX=s; try{localStorage.setItem(FKEY,String(s));}catch(e){}
 if(SFX&&initAC())pluck(PENTA[4],.020,.22); /* 开启时试听一声 */
 syncHctl();
}
function toggleSFX(){ setSFX(SFX?0:1); }
function tickSound(){ if(SFX&&initAC())pluck(PENTA[4],.014,.16); }


/* ---------- 环境音：随天气自动出现，全部实时合成、无音频文件 ----------
   只有「场景音」开启时才播；切场景清掉旧调度再起新的，不会叠成一片。 */
let ambTimer=null, ambKind='';
function stopAmbient(){ if(ambTimer){clearTimeout(ambTimer);ambTimer=null;} ambKind=''; }
function chirp(){
 if(!AC||!SFX&&!BGM)return;
 const t=AC.currentTime, n=2+((Math.random()*3)|0);
 for(let i=0;i<n;i++){
  const o=AC.createOscillator(), g=AC.createGain();
  const f=1750+Math.random()*700, st=t+i*(.11+Math.random()*.07);
  o.type='sine';
  o.frequency.setValueAtTime(f,st);
  o.frequency.exponentialRampToValueAtTime(f*1.42,st+.045);
  o.frequency.exponentialRampToValueAtTime(f*.92,st+.10);
  g.gain.setValueAtTime(.0001,st);
  g.gain.exponentialRampToValueAtTime(.013,st+.018);
  g.gain.exponentialRampToValueAtTime(.0001,st+.135);
  o.connect(g);g.connect(AC.destination);o.start(st);o.stop(st+.16);
 }
}
function cricket(){
 if(!AC)return;
 const t=AC.currentTime;
 for(let i=0;i<3;i++){
  const o=AC.createOscillator(), g=AC.createGain(), st=t+i*.085;
  o.type='sine';o.frequency.value=4200+Math.random()*500;
  g.gain.setValueAtTime(.0001,st);
  g.gain.exponentialRampToValueAtTime(.006,st+.006);
  g.gain.exponentialRampToValueAtTime(.0001,st+.045);
  o.connect(g);g.connect(AC.destination);o.start(st);o.stop(st+.06);
 }
}
function pageRustle(){
 if(!AC)return;
 const t=AC.currentTime, src=AC.createBufferSource();
 src.buffer=noiseBuffer();
 const bp=AC.createBiquadFilter();bp.type='bandpass';bp.frequency.value=1100;bp.Q.value=.7;
 const g=AC.createGain();
 g.gain.setValueAtTime(.0001,t);
 g.gain.exponentialRampToValueAtTime(.008,t+.05);
 g.gain.exponentialRampToValueAtTime(.0001,t+.30);
 src.connect(bp);bp.connect(g);g.connect(AC.destination);src.start(t);src.stop(t+.34);
}
function farThunder(){
 if(!AC)return;
 const t=AC.currentTime, o=AC.createOscillator(), g=AC.createGain(), lp=AC.createBiquadFilter();
 o.type='sine';o.frequency.setValueAtTime(58,t);
 o.frequency.exponentialRampToValueAtTime(34,t+1.5);
 lp.type='lowpass';lp.frequency.value=130;
 g.gain.setValueAtTime(.0001,t);
 g.gain.exponentialRampToValueAtTime(.016,t+.35);
 g.gain.exponentialRampToValueAtTime(.0001,t+1.9);
 o.connect(lp);lp.connect(g);g.connect(AC.destination);o.start(t);o.stop(t+2.0);
}
function scheduleAmbient(kind){
 if(!BGM||!AC)return;
 const delays={birds:[2600,5200],night:[3200,6000],quiet:[7000,13000],
               wind:[5000,9000],rain:[9000,16000]}[kind]||[6000,11000];
 const wait=delays[0]+Math.random()*(delays[1]-delays[0]);
 ambTimer=setTimeout(()=>{
  if(!BGM||!AC){stopAmbient();return;}
  try{
   if(kind==='birds')chirp();
   else if(kind==='night')cricket();
   else if(kind==='quiet')pageRustle();
   else if(kind==='rain')farThunder();
   /* wind 已在噪声链里，靠滤波与增益起伏表现，不额外叠声 */
  }catch(e){}
  scheduleAmbient(kind);
 },wait);
}
function startAmbient(bg){
 stopAmbient();
 if(!BGM||!AC)return;
 const kind=sceneWeather(bg).amb; ambKind=kind;
 scheduleAmbient(kind);
}
const AMB_LABEL={birds:'晴日鸟鸣',night:'夜虫',quiet:'书楼静响',wind:'风声',rain:'远雷'};
/* R8：天气音景可手动选，且随通关数解锁；auto = 跟随当前场景 */
const WXLIST=[
 ['auto','自动跟随当前场景','',0],
 ['rain','秋雨 · 远雷','rain',0],
 ['quiet','书楼静响 · 翻页','shulou',0],
 ['birds','拂晓晴光 · 鸟鸣','dujiang',2],
 ['wind','辕门朔风','yuanmen',4],
 ['night','秦淮夜虫','qinhuai',6],
 ['snow','秣陵落雪 · 风雪','moling',8],
 ['haodenglou','临安夜雨','haodenglou',12]
];
const WXBG=Object.fromEntries(WXLIST.filter(x=>x[0]!=='auto').map(x=>[x[0],x[2]]));
const WXKEY='beixue_wxpick_v1', VIBKEY='beixue_vib_v1', LAYKEY='beixue_layout_v1', BLAYKEY='beixue_bublay_v1';
let WXPICK='', VIB=1, LAYOUT=0, BUBLAY={};
try{const _v=localStorage.getItem(WXKEY); if(_v&&WXLIST.some(x=>x[0]===_v))WXPICK=_v;}catch(e){}
try{const _v=localStorage.getItem(VIBKEY); if(_v!==null)VIB=(+_v===1)?1:0;}catch(e){}
try{const _v=localStorage.getItem(LAYKEY); if(_v!==null)LAYOUT=(+_v===1)?1:0;}catch(e){}
try{const _v=localStorage.getItem(BLAYKEY); if(_v)BUBLAY=JSON.parse(_v)||{};}catch(e){}
function wxUnlocked(x){ return clearedCount()>=x[3]; }
const BG_GATE={dujiang:2,bailuzhou:2,yuanmen:4,qinhuai:6,moling:8,dashipo:8,haodenglou:12};
function audioBg(){
 if(WXPICK&&WXPICK!=='auto')return WXBG[WXPICK]||'rain';
 const real=currentSceneBg(), gate=BG_GATE[real]||0;
 return (gate&&clearedCount()<gate)?'rain':real;   /* 自动跟随也按进度解锁 */
}
function vib(ms){ if(!VIB)return; try{ navigator.vibrate&&navigator.vibrate(ms); }catch(e){} }
function saveLayout(){ try{localStorage.setItem(LAYKEY,String(LAYOUT));localStorage.setItem(BLAYKEY,JSON.stringify(BUBLAY));}catch(e){} }

/* ---------- state ---------- */
let TAB='hall', ARCH='intro', LAST='E', ARCH_LOCK_MSG='';
try{ const l=localStorage.getItem(LKEY); if(l)LAST=l; }catch(e){}
const S={
 A:{stage:'intro',node:'s1',clues:[],asks:4,askCount:0,stance:[],echo:'',q:{},qi:0,trail:[],end:null,reveal:null,pause:null,roam:0,mistakes:0},
 B:{stage:'intro',turn:0,silver:'cart',focus:'six',sign:'ok',pact:'ok',known:false,sel:[],log:[],hint:1,end:null,pause:null,mistakes:0},
 D:{stage:'intro',i:0,score:0,streak:0,best:0,wrong:[],picked:null,showWhy:false,showHint:false,mistakes:0},
 C:{stage:'intro',k:0,g:5,b:5,p:5,log:[],end:null,mistakes:0},
 E:{stage:'intro',i:0,sc:{},picks:[],end:null},
 F:{stage:'intro',i:0,right:0,wrong:[],picked:null,showWhy:false,showHint:false,end:null,mistakes:0},
};
QKEYS.forEach(k=>S[k]=qFresh());
function remember(k){ LAST=k; try{localStorage.setItem(LKEY,k);}catch(e){} }

/* ---------- 界面皮肤 ---------- */
/* 三套皮肤只改观感，不动关卡数据、模式、难度、无障碍开关与朗读/语音默认值。 */
const SKINS=[
 ['auto','跟随系统','按手机深浅色自动切宣纸／夜雨，并跟随减少动效与高对比设置（推荐）'],
 ['paper','宣纸书卷','暖宣纸底、宋体标题、朱砂细线、册页式卡片。固定浅色。'],
 ['night','夜雨戏台','深墨底、暖灯金描边，场景板与透明角色层在暗底上更亮。固定深色。'],
 ['plain','轻简','早期观感：米白卡片、无衬线、大圆角。不习惯新皮可退回。']
];
const SKEY='beixue_skin_v2';
let SKIN='auto';
try{ const _s=localStorage.getItem(SKEY); if(_s&&SKINS.some(x=>x[0]===_s))SKIN=_s; }catch(e){}
function applySkin(){
 const _eff=(SKIN==='auto')?
   (window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches?'night':'paper'):SKIN;
 document.documentElement.setAttribute('data-skin',_eff);
 const btn=$('#skinBtn');
 if(btn){const n=(SKINS.find(x=>x[0]===SKIN)||SKINS[0])[1];
  btn.textContent='◐ 皮肤 · '+n;btn.title='切换界面皮肤（当前：'+n+'）';}
 if(!$('#skinPanel').hidden)renderSkinPanel();
}
function setSkin(v){
 if(!SKINS.some(x=>x[0]===v))return;
 SKIN=v; try{localStorage.setItem(SKEY,v);}catch(e){}
 applySkin(); render();
 announce('界面已切换为'+(SKINS.find(x=>x[0]===SKIN)[1]));
}
function renderSkinPanel(){
 const p=$('#skinPanel'); if(!p)return;
 const swatch={auto:['linear-gradient(90deg,#F0E9D9 50%,#141A1D 50%)','#42674A','#2C2820'],
               paper:['#F0E9D9','#9B3A2F','#2C2820'],
               night:['#141A1D','#D9A85C','#EDE6D7'],
               plain:['#F6F2E8','#4E7351','#2B2A26']};
 p.innerHTML='<h4>◐ 界面皮肤</h4><div class="mp-h">只改观感 · 四选一通用二十四关 · 设置会记住</div>'+
  SKINS.map(([k,n,d])=>{const c=swatch[k];
   return `<button class="sk-i ${SKIN===k?'on':''}" data-act="skin_set" data-v="${k}" aria-label="皮肤${n}，${d}">
    <span class="sk-sw" style="background:${c[0]}" aria-hidden="true"><i style="background:${c[1]}"></i><u style="background:${c[2]}"></u><s style="background:${c[2]}"></s></span>
    <span class="sk-tx"><b>${SKIN===k?'✓ ':''}${n}</b><span>${d}</span></span></button>`;}).join('')+
  '<div class="mp-h" style="padding-top:6px">高对比／大字号／减少动效仍以「无障碍」面板为准，三套皮肤下都有效。</div>';
}


/* ---------- AVG 演出：天气、光、飞鸟与场景音 ----------
   11 张背景板 -> 6 类天气动画 + 4 类环境音。纯 CSS 动画与 Web Audio 实时合成，无图片/音频文件。 */
const SCENE_WEATHER={
 rain:      {fx:'rain',  amb:'rain',  label:'秋雨'},
 qilipu:    {fx:'rain',  amb:'rain',  label:'驿道冷雨'},
 haodenglou:{fx:'rain',  amb:'rain',  label:'临安夜雨'},
 dujiang:   {fx:'sun',   amb:'birds', label:'拂晓晴光'},
 bailuzhou: {fx:'birds', amb:'birds', label:'芦荡晴日'},
 shulou:    {fx:'dust',  amb:'quiet', label:'书楼窗光'},
 moling:    {fx:'snow',  amb:'wind',  label:'秣陵落雪'},
 dashipo:   {fx:'snow',  amb:'wind',  label:'石阵风雪'},
 yuanmen:   {fx:'wind',  amb:'wind',  label:'辕门朔风'},
 huai:      {fx:'night', amb:'quiet', label:'淮上夜帐'},
 qinhuai:   {fx:'night', amb:'night', label:'秦淮灯夜'}
};
const FX_LABEL={rain:'雨丝',sun:'晨光与飞鸟',birds:'晴日飞鸟',dust:'窗光浮尘',snow:'落雪',wind:'朔风',night:'灯火浮絮'};
function sceneWeather(bg){ return SCENE_WEATHER[bg]||SCENE_WEATHER.rain; }


/* ---------- 横屏按钮：一键进横屏，或不转手机直接套横屏版式 ----------
   不持久化：每次打开默认竖屏。全屏与方向锁定失败不影响「强制版式」这条退路。 */
let LAND=0, FORCE=0, ROT=0, LAND_DISMISS=0;
const LAND_MQ=window.matchMedia?window.matchMedia('(orientation:landscape) and (max-height:560px)'):null;
function isPhysLandscape(){ return LAND_MQ?!!LAND_MQ.matches:false; }
function syncLandBtn(){
 const b2=$('#landBtn'); if(!b2)return;
 b2.textContent=LAND?'⛶ 退出横屏':(isPhysLandscape()?'▭ 横屏中':'⛶ 横屏');
 b2.setAttribute('aria-pressed',LAND?'true':'false');
 b2.title=LAND?'退出横屏模式并恢复竖屏版式（设备仍横屏时由系统方向自动适配）':
   (isPhysLandscape()?'已处于横屏；点击开启横屏模式并尝试锁定方向':'一键进入横屏：全屏并尝试锁定方向，或不转手机直接套横屏版式');
 b2.classList.toggle('on',!!LAND);
}
function renderLandTip(){
 const t=$('#landTip'); if(!t)return;
 if(!LAND||LAND_DISMISS){t.hidden=true;return;}
 t.hidden=false;
 const phys=isPhysLandscape();
 t.innerHTML=`<div class="lt-h"><b>⛶ 横屏模式已开${ROT?' · 画面已横过来':(phys?' · 设备已横屏':'')}</b>
   <button data-act="land_dismiss" aria-label="收起横屏提示">✕</button></div>
  <div class="lt-t">${ROT?'⛶ <b>已把整张画面横过来</b>：请把手机横着拿，文字与选项就是正向横向排版；不想转手机，点下面「不转画面」改用横向紧凑版式。':
   (phys?'设备已横屏，无需旋转；横向版式已生效。':'▭ 当前不旋转画面，只套横向紧凑版式；点「把画面横过来」可真横屏。')}</div>
  <div class="lt-b">
   <button data-act="land_rot" class="${ROT?'on':''}">${ROT?'▭ 不转画面（横向版式）':'⛶ 把画面横过来'}</button>
   <button data-act="land_dismiss">知道了</button>
   <button data-act="land_exit">退出横屏</button>
  </div>`;
}
function enterLand(){
 resetHallSpr();
 LAND=1; LAND_DISMISS=0; FORCE=1;
 document.documentElement.classList.add('force-landscape');
 /* R14：竖屏设备点横屏 = 真的把整张画布转 90°（宽高互换）。
    把手机横着拿，文字、题干、选项、名牌全部是正向横向排版。
    设备本来就横时不转，避免二次转歪；不想转手机的人用提示条的「不转画面」。 */
 ROT=isPhysLandscape()?0:1;
 document.documentElement.classList.toggle('rot-landscape',!!ROT);
 try{
  const el=document.documentElement;
  if(el.requestFullscreen&&!document.fullscreenElement)el.requestFullscreen().catch(()=>{});
 }catch(e){}
 try{
  if(screen.orientation&&screen.orientation.lock)screen.orientation.lock('landscape').catch(()=>{});
 }catch(e){}
 if(isPhysLandscape())LAND_DISMISS=1;   /* 本来就是横屏，不必再提示 */
 syncLandBtn(); renderLandTip(); render();
 announce(ROT?'已把整张画面横过来，请把手机横着拿；不想转手机就点提示条的「不转画面」':
  '设备已横屏，横向版式自动生效');
}
function exitLand(){
 resetHallSpr();
 LAND=0; FORCE=0; ROT=0; LAND_DISMISS=0;
 document.documentElement.classList.remove('force-landscape');
 document.documentElement.classList.remove('rot-landscape');
 try{ if(document.fullscreenElement&&document.exitFullscreen)document.exitFullscreen().catch(()=>{}); }catch(e){}
 try{ if(screen.orientation&&screen.orientation.unlock)screen.orientation.unlock(); }catch(e){}
 syncLandBtn(); renderLandTip(); render();
 announce(isPhysLandscape()?'已退出横屏模式；设备仍处于横屏，版式由系统方向自动决定':'已退出横屏，恢复竖屏版式');
}
function toggleLand(){ LAND?exitLand():enterLand(); }
function toggleRot(){
 resetHallSpr();
 if(isPhysLandscape()){
  ROT=0; document.documentElement.classList.remove('rot-landscape');
  renderLandTip(); announce('设备本来就是横屏，无需再旋转画面'); return;
 }
 ROT=ROT?0:1;
 document.documentElement.classList.toggle('rot-landscape',!!ROT);
 renderLandTip(); render();
 announce(ROT?'已把整张画面横过来，请把手机横着拿':'已改为不转画面，横向紧凑版式生效');
}
function isLevelTab(k){ return !!D.meta.levels.find(l=>l.id===k)||k==='coming'; }
if(LAND_MQ&&LAND_MQ.addEventListener){
 LAND_MQ.addEventListener('change',e=>{
  if(LAND){
   /* R14：设备自己横过来时撤掉旋转避免二次转歪；回竖屏再自动转回来 */
   ROT=e.matches?0:1;
   document.documentElement.classList.toggle('rot-landscape',!!ROT);
   LAND_DISMISS=e.matches?1:0;
   renderLandTip(); render();
   announce(e.matches?'设备已横屏，旋转已撤销，版式自动生效':'设备回到竖屏，已重新把画面横过来，请把手机横着拿');
  }
  syncLandBtn();
 });
}


let PANEL_TABS=0;
/* ---------- 呼吸感：角色不再完全静止 ---------- */
const BRKEY='beixue_breathe_v1', PGKEY='beixue_perf_gate_v1';
let BREATHE=1, PERF_GATE=0, COMING='';
/* R13：一个天气只跑一套层。旧 CSS 两层斜线 + 后来补的厚涂素材层同时跑，
   就是截图里「两种形态的雨」。默认只放素材层，CSS 退场。 */
const FXKEY='beixue_fxmode_v1';
let FXMODE='art';
try{const v=localStorage.getItem(FXKEY);if(v&&['art','css','both'].indexOf(v)>=0)FXMODE=v;}catch(e){}
function setFxMode(v){
 if(['art','css','both'].indexOf(v)<0)return;
 FXMODE=v; try{localStorage.setItem(FXKEY,v);}catch(e){}
 const nm={art:'素材优先（一套雨）',css:'CSS 兜底',both:'双份叠加（旧行为）'}[v];
 announce('天气层已切为'+nm);
}
try{const v=localStorage.getItem(BRKEY);if(v!==null)BREATHE=+v?1:0;}catch(e){}
try{const v=localStorage.getItem(PGKEY);if(v!==null)PERF_GATE=+v?1:0;}catch(e){}
function setBreathe(v){
 BREATHE=v?1:0;try{localStorage.setItem(BRKEY,BREATHE);}catch(e){}
 document.body.classList.toggle('no-breathe',!BREATHE);
 announce('角色呼吸感已'+(BREATHE?'开启':'关闭'));
}
function perfDone(k,cat){ return !!(D.perf.done||{})[k+'|'+cat]; }
function perfMissing(k){
 return (D.perf.need[k]||[]).filter(c=>!perfDone(k,c));
}
function perfReady(k){ return perfMissing(k).length===0; }
function setPerfGate(v){
 PERF_GATE=v?1:0;try{localStorage.setItem(PGKEY,PERF_GATE);}catch(e){}
 announce(PERF_GATE?'已切到「仅完整演出」：筹备中的关卡会锁住':'已切到「基础优先」：筹备中的关卡可用基础演出');
 render();
}
function perfLocked(k){ return !!PERF_GATE && !perfReady(k); }
function openComing(k){
 COMING=k; setTab('coming');
 announce('《'+(D.meta.levels.find(l=>l.id===k)||{}).t+'》完整演出尚在筹备，敬请期待');
}
const CAT_BATCH={'天气粒子':'批次 2','角色表情':'批次 3','角色动作':'批次 4',
 '场景板':'批次 5','序列帧':'批次 6','呼吸分层':'批次 6','语音包':'批次 7'};


/* ---------- 批次 2：把 CSS 粒子换成厚涂透明素材层 ----------
   旧 CSS 斜线/圆点仍保留作底，素材层叠在上面，关掉素材也不会塌。 */
const FX_ART={
 rain:[['fx_rain','tile'],['fx_splash','ground']],
 sun:[['fx_ray','ray'],['fx_bird_up','bird'],['fx_dust','dust']],
 birds:[['fx_bird_flat','bird'],['fx_reed','ground']],
 snow:[['fx_snow','tile'],['fx_snowedge','snowedge']],
 wind:[['fx_flag','flagseq'],['fx_flag2','flagseq'],['fx_flag3','flagseq'],['fx_wind','wind']],
 night:[['fx_lamp','lamp'],['fx_firefly','firefly']],
 dust:[['fx_dust','dust'],['fx_wind','wind']]
};
function fxArt(k){
 return (FX_ART[k]||[]).map(([a,m])=>`<i class="fx-art" data-fx="${a}" data-mode="${m}"></i>`).join('');
}

/* ---------- nav ---------- */
const nav=$('#nav');
nav.innerHTML='<button data-nav="hall" class="on">◆ 大厅</button>'+
 '<button class="navtoggle" data-act="nav_toggle" aria-expanded="false" aria-label="展开或收起全部页签">▦ 页签</button>'+
 D.meta.tabs.map(t=>`<button class="navmore" data-nav="${t[0]}">${t[1]}</button>`).join('')+
 '<button class="navmore" data-nav="arch">档案</button>';
function setTab(t){
 /* R14：进关卡保持当前旋转状态，画面横过来后所有页签都是横向阅读 */
 TAB=t;
 nav.classList.remove('open');
 const _nt=$('#nav .navtoggle'); if(_nt){_nt.setAttribute('aria-expanded','false');_nt.textContent='▦ 页签';}
 nav.querySelectorAll('button').forEach(b=>b.classList.toggle('on',b.dataset.nav===t));
 render(); window.scrollTo({top:0,behavior:'instant'});
 try{ document.body.scrollTop=0; document.body.scrollLeft=0; }catch(e){}
}
nav.onclick=e=>{const b=e.target.closest('[data-nav]');if(b)setTab(b.dataset.nav);};

/* ================= 朗读 / 语音控制 / 无障碍 =================
   朗读模式与语音控制均默认关闭，且不持久化：每次打开都是"关"，
   需要用户明确点开（语音还需麦克风授权）。视觉偏好可持久化。 */
const TTS_CAP = ('speechSynthesis' in window);
const SR_CTOR = window.SpeechRecognition || window.webkitSpeechRecognition;
const AKEY_HC='beixue_hc_v1', AKEY_BIG='beixue_big_v1', AKEY_RED='beixue_reduce_v1',
      AKEY_RATE='beixue_rate_v1';
let TTS=0, ASR=0, HC=0, BIG=0, REDUCE=0, RATE=1, TTSAUTO=1, ASR_MSG='', ttsTimer=null, rec=null;
/* R4：气泡透明度 0 清透 / 1 均衡 / 2 厚实；立绘 0 半身（下半在气泡里）/ 1 全身 */
let BUB=1, POSE=0, BUBF=.40;
try{ const _v=localStorage.getItem('beixue_bub_v1'); if(_v!==null)BUB=[0,1,2].includes(+_v)?+_v:1; }catch(e){}
/* R6：气泡透明度连续值 .10–.90，三档预设只是快捷值 */
try{ const _v=localStorage.getItem('beixue_bubf_v1'); if(_v!==null){const n=+_v;if(n>=.10&&n<=.90)BUBF=n;} }catch(e){}
try{ const _v=localStorage.getItem('beixue_pose_v1'); if(_v!==null)POSE=(+_v===1)?1:0; }catch(e){}
try{ const v=localStorage.getItem(AKEY_HC);   if(v!==null)HC=(+v===1)?1:0; }catch(e){}
try{ const v=localStorage.getItem(AKEY_BIG);  if(v!==null)BIG=(+v===1)?1:0; }catch(e){}
try{ const v=localStorage.getItem(AKEY_RED);  if(v!==null)REDUCE=(+v===1)?1:0; }catch(e){}
try{ const v=localStorage.getItem(AKEY_RATE); if(v!==null)RATE=[0.8,1,1.2].includes(+v)?+v:1; }catch(e){}


/* ---------- R5：跟随手机系统设置 ---------- */
if(window.matchMedia){
 const _dark=matchMedia('(prefers-color-scheme: dark)');
 if(_dark.addEventListener)_dark.addEventListener('change',()=>{
   if(SKIN==='auto'){applySkin(); try{render();}catch(e){}}
 });
 try{
  if(matchMedia('(prefers-reduced-motion: reduce)').matches &&
     localStorage.getItem(AKEY_RED)===null){REDUCE=1;applyA11y();}
  if(matchMedia('(prefers-contrast: more)').matches &&
     localStorage.getItem(AKEY_HC)===null){HC=1;applyA11y();}
 }catch(e){}
}

function announce(msg){ const l=$('#live'); if(l)l.textContent=msg; }
function applyA11y(){
 document.body.classList.toggle('hc',!!HC);
 document.body.classList.toggle('big',!!BIG);
 document.body.classList.toggle('reduce',!!REDUCE);
 const rs=document.documentElement.style;
 rs.setProperty('--bubA',Math.max(.04,BUBF*.60).toFixed(3));
 rs.setProperty('--bubB',BUBF.toFixed(3));
 rs.setProperty('--bubC',Math.min(.94,BUBF+.16).toFixed(3));
 document.body.classList.toggle('pose-half',POSE===0);
 document.body.classList.toggle('pose-full',POSE===1);
}


/* ---------- R7：场景板 / 人物按通关进度逐步解锁 ---------- */
const HBGKEY='beixue_hallbg_v1';
let HH_BG='rain';
try{ const _v=localStorage.getItem(HBGKEY); if(_v)HH_BG=_v; }catch(e){}
function bgNeed(i){ return i<3?0:(i-2)*2; }               /* 初始 3 张，此后每通 2 关开 1 张 */
function bgUnlocked(i){ return clearedCount()>=bgNeed(i); }
function bgIdx(v){ return BGLIST.findIndex(x=>x[0]===v); }
function castNeed(i,total){ return i<4?0:Math.ceil((i-3)*24/Math.max(1,total-3)); }
function castUnlocked(i,total){ return clearedCount()>=castNeed(i,total); }
function bgCount(){ return BGLIST.filter((x,i)=>bgUnlocked(i)).length; }
/* 表演表情层属于关卡演出，不占引导员/换装台的可选人物位，始终可用 */
const OPT_MOODS=[
 {n:'沉吟颔首',anim:'nod',arts:['cos_shen_calm','cos_luo_nod','cos_yi_cup']},
 {n:'无奈摇头',anim:'shake',arts:['cos_shen_shrug','cos_qinwen_wry','cos_zhu_turn']},
 {n:'警觉按剑',anim:'guard',arts:['cos_luo_guard','cos_jin_guard','cos_zhu_smile']},
 {n:'怅然低眉',anim:'lean',arts:['cos_xiao_sigh','cos_zhu_turn','cos_luo_nod']},
 {n:'将歌未歌',anim:'lean',arts:['cos_xiao_sing','cos_ying_sing','cos_zhu_resolve']},
 {n:'按剑决绝',anim:'guard',arts:['cos_zhu_resolve','cos_qinwen_smash','cos_geng_trust']},
 {n:'佯狂一笑',anim:'shake',arts:['cos_jinhe_laugh','cos_tian_wink','cos_wen_sly']},
 {n:'旧盟相惜',anim:'nod',arts:['cos_yuancl_agree','cos_yi_cup','cos_luo_nod']}
];

/* ---------- R6：角色名牌（名字 + 昵称/花名/职务） ---------- */
const CAST_META={
 cos_base:['哈士喵','本色 · 作者授权吉祥物 / 本站引导员'],
 cos_shen:['沈放','「被传成沈大侠」· 舒城文士 / 淮上钱谷'],
 cos_luo:['骆寒','弧剑 · 不过江的剑客 / 五部贯穿线'],
 cos_jin:['荆三娘','荆紫 · 蓬门掌门 / 紫荆木钗'],
 cos_yi:['易敛','易杯酒 · 木杯之约 / 淮上义军组织者'],
 cos_zhu:['朱妍','浅绯舞袖 · 秦淮 / 《停云》一脉'],
 cos_xiao:['萧如','揉蓝衫子 · 江船九姓 / 顺风古渡'],
 cos_geng:['耿苍怀','大侠 · 雨驿托孤 / 「三不可」'],
 cos_qinwen:['秦稳','稳如泰山 · 临安镖局总镖头'],
 cos_jinhe:['金和尚','佯狂 · 逃死令入义军'],
 cos_ying:['小英子','短笛 · 雨驿卖唱 / 易敛传信'],
 cos_du:['杜淮山','洞明手 · 淮上老狐狸 / 逃死令'],
 cos_jiao:['焦泗隐','练达剑 · 信鸽情报 / 淮上'],
 cos_gbx:['庚不信','苏北抗金 · 易敛道义之交'],
 cos_qu:['瞿百龄','散家产 · 淮上旧盟'],
 cos_yuancl:['袁辰龙','三十二尉之首 · 缇骑统领 / 辕门'],
 cos_yuaner:['袁二','缇骑 · 困马集 / 袁辰龙之弟'],
 cos_wen:['文翰林','文家 · 杀袁之局 / 文亭阁'],
 cos_mi:['米俨','宗室双岐 · 第三方 / 白鹭洲'],
 cos_shi:['石燃','狐骑「石敢当」· 化名石敢当'],
 cos_zwl:['赵无量','九姓宗室 · 白鹭洲 / 赵旭'],
 cos_tian:['田笑','《络绎》· 番外《借红灯》'],
 cos_tie:['铁萼英','倔强 · 江湖后辈'],
 cos_shen_argue:['沈放 · 强辩','表情变体 · 一时口快'],
 cos_luo_draw:['骆寒 · 出剑','表情变体 · 弧剑出鞘'],
 cos_yi_grief:['易敛 · 沉痛','表情变体 · 木杯之重'],
 cos_zhu_resolve:['朱妍 · 决绝','表情变体 · 将落未落'],
  H_cost_jin:["荆三娘", "荆紫 · 蓬门掌门 / 墨紫劲装"],
  H_cost_shen:["沈放", "「被传成沈大侠」· 舒城文士 / 淮上钱谷"],
  H_cost_ying:["小英子", "短笛 · 雨驿卖唱 / 易敛传信"],
  H_cost_geng:["耿苍怀", "大侠 · 雨驿托孤 / 「三不可」"],
  H_cost_yuaner:["袁二", "缇骑 · 困马集 / 袁辰龙之弟"],
  H_cost_luo:["骆寒", "弧剑 · 不过江的剑客 / 五部贯穿线"],
  H_cost_jinhe:["金和尚", "佯狂 · 逃死令入义军"],
  H_cost_qinwen:["秦稳", "稳如泰山 · 临安镖局总镖头"],
  H_cost_shi:["石燃", "狐骑「石敢当」· 化名石敢当"],
  H_cost_yuchi:["尉迟渺", "双车尉 · 辕门十一人"],
  G_cost_verify:["校书郎", "细校 · 版本异文"],
  G_cost_compare:["校书郎", "比对异文"],
  G_cost_brush:["校书郎", "朱笔圈点"],
  G_cost_startled:["校书郎", "发现错字"],
  G_cost_smile:["校书郎", "校定释然"],
  G_cost_turn:["校书郎", "翻页"],
  G_cost_scroll:["校书郎", "展卷"],
  G_cost_blink:["校书郎", "眨眼落帧"],
  G_cost_open:["校书郎", "睁眼起帧"],
  B_face_du:["杜淮山", "洞明手 · 淮上老狐狸 / 逃死令（一致性代用）"],
  B_face_yuane:["文翰林", "文家 · 杀袁之局 / 文亭阁（一致性代用）"],
  A_face_jin:["荆三娘", "荆紫 · 蓬门掌门 / 紫荆木钗"],
  HR_geng:["耿苍怀", "深灰束带 · 赭褐旧袍"],
  HR_qinwen:["秦稳", "赭褐布巾 · 灰布短打"],
  HR_shen:["沈放", "青灰文士软巾 · 青衫"],
  HR_xiao:["萧如", "揉蓝包头布 · 揉蓝衫子"],
  HR_yi:["易敛", "素木簪低髻 · 青灰长衫"],
  HR_ying:["小英子", "藕荷单丫髻 · 碎花小袄"],
  HR_yuancl:["袁辰龙", "玄色矮幞头 · 缇骑玄袍"],
  R22_geng:["耿苍怀", "赭褐旧袍 · 深灰络腮短须"],
  R22_jiao:["焦泗隐", "灰青劲装 · 深灰束带"],
  R22_jin:["荆三娘", "墨紫劲装 · 深褐单高髻假发"],
  R22_qinwen:["秦稳", "灰布短打 · 深褐八字短须"],
  R22_yuancl:["袁辰龙", "缇骑玄袍 · 矮幞头 · 短须"],
  R22_zhu:["朱妍", "暖赭舞袖 · 单环髻假发"],
  R23_lip_zhu:["朱妍", "暖赭舞袖 · 单环髻 · 淡朱砂唇（唇色未显）"],
  R23_lip_xiao:["萧如", "揉蓝衫子 · 包头布 · 淡豆沙唇（唇色未显）"],
  R23_build_yuancl:["袁辰龙", "缇骑玄袍 · 阔肩披肩（体态暗示）"],
  R23_build_yi:["易敛", "窄袖青灰长衫 · 束腰（体态暗示）"],
  R23_build_jinhe:["金和尚", "赭褐宽袍 · 袒腹（体态暗示）"],
  R23_act_carry:["秦稳", "负箱 · 深灰褐短打"],
  R22_du:["杜淮山", "深褐旧袍 · 花白长须"],
  R22_jinhe:["金和尚", "赭褐僧衣 · 浓黑短茬胡"],
  R22_luo:["骆寒", "玄黑披风 · 深褐长披发假发"],
  R25_lip_zhu:["朱妍", "暖赭舞袖 · 单环髻 · 深赭红唇"],
  R25_lip_xiao:["萧如", "揉蓝衫子 · 包头布 · 深赭红唇"],
  R25_lip_ying:["小英子", "藕荷小袄 · 单丫髻 · 深赭红唇"],
  R25_scar_yuancl:["袁辰龙", "缇骑玄袍 · 幞头短须 · 眉骨疤"],
  R25_scar_jiao:["焦泗隐", "灰青劲装 · 束带 · 脸颊疤"],
  R25_act_sleeve:["袁二", "缇骑袍 · 拂袖"],
  R25_I_zhu:["朱妍", "暖赭舞袖 · 回眸"],
  R25_I_ying:["小英子", "藕荷小袄 · 唱词"],
  R26_J_read:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 展卷细读"],
  R26_J_fit:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 拼合回目"],
  R26_J_brush:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 朱笔圈题"],
  R26_J_compare:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 比对目录"],
  R26_J_startled:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 发现缺章"],
  R26_J_done:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 校定释然"],
  R26_J_turn:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 翻页"],
  R26_J_lamp:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 执灯照卷"],
  R29_K_read:["萧如", "揉蓝衫子 · 包头布 · 深赭红唇 / K 关「展卷细读」· 程序化情境变体（源 R25_lip_xiao）"],
  R29_K_brush:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 展卷细读 / K 关「拈笔笺注」· 程序化情境变体（源 R26_J_read）"],
  R29_K_compare:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 比对目录 / K 关「两卷并读」· 程序化情境变体（源 R26_J_compare）"],
  R29_K_pause:["朱妍", "暖赭舞袖 · 回眸 / K 关「停云凝思」· 程序化情境变体（源 R25_I_zhu）"],
  R29_K_ah:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 发现缺章 / K 关「恍然得句」· 程序化情境变体（源 R26_J_startled）"],
  R29_K_cup:["易敛", "窄袖青灰长衫 · 束腰（体态暗示） / K 关「金荷酌客」· 程序化情境变体（源 R23_build_yi）"],
  R29_K_bridge:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 翻页 / K 关「长桥题壁」· 程序化情境变体（源 R26_J_turn）"],
  R29_K_check:["易敛", "细校 · 版本异文 / K 关「指认异文」· 程序化情境变体（源 G_cost_verify）"],
  R29_K_smile:["朱妍", "暖赭舞袖 · 单环髻 · 深赭红唇 / K 关「会心」· 程序化情境变体（源 R25_lip_zhu）"],
  R29_K_done:["易敛", "易杯酒 · 淮上义军组织者 / 校书郎扮相 · 校定释然 / K 关「合卷落印」· 程序化情境变体（源 R26_J_done）"],
};
/* R21：名牌反查。此前 origCast() 把 cos_* 重定向到 R19/R20 穿衣版或 R15 代用层，
   而 CAST_META 只登记了老 cos_* key，导致 11 张卡点开后名牌统一落到「哈士喵」兜底
   （用户截图里的墨紫劲装荆三娘正是 H_cost_jin）。这里做一层反查：
   先查美术层本身，再沿 COSTUME_REMAP / CONSISTENCY_REMAP 反推逻辑角色 key，最后才兜底。 */
/* J 关两张代用层：名牌统一，副标题如实标注为 R20 存量层，不冒充新生成 */
const J_DEPUTY={
 'G_cost_verify':['易敛','易杯酒 · 淮上义军组织者 / 校书郎扮相 · 细校（R20 存量层代用）'],
 'G_cost_compare':['易敛','易杯酒 · 淮上义军组织者 / 校书郎扮相 · 异文并陈（R20 存量层代用）']
};
function castMeta(k){
 if(typeof TAB!=='undefined'&&TAB==='J'&&J_DEPUTY[k])return J_DEPUTY[k];
 if(CAST_META[k])return CAST_META[k];
 const rev=CATCOST.find(x=>origCast(x[2])===k);
 if(rev){ const base=CAST_META[rev[2]]; if(base)return [base[0],base[1]]; }
 return ['哈士喵','本色 · 作者授权吉祥物 / 本站引导员'];
}

/* 引导员：24 关各有对应的一张脸；模式兜底；答错/通关临时变脸 */
let CATFIX='', CATMOOD_ON=true;
const MOOD={key:'',t:0};
const SEEN_END=new Set();
const LEVEL_AVATAR={
 E:'cos_zhu',A:'cos_shen',B:'cos_jin',C:'cos_yi',D:'cos_qinwen',F:'cos_wen',
 G:'cos_xiao',H:'cos_mi',I:'cos_yuaner',J:'cos_yi',K:'cos_xiao',L:'cos_zhu',
 M:'cos_shen',N:'cos_shi',O:'cos_zwl',P:'cos_luo',Q:'cos_jiao',R:'cos_gbx',
 S:'cos_yi',T:'cos_tian',U:'cos_zhu',V:'cos_ying',W:'cos_xiao',X:'cos_tian'
};
/* ---------- 关卡舞台：场景背景板 + 透明角色层 ----------
   每一屏（intro / 幕 / 答题 / 结算）都有一张「舞台」，不再只有 intro 的水墨题图。
   A 关按幕换说话人的脸；E 结算按结果角色换脸；情绪反馈与手动固定同步生效。 */
const STAGE_BG={
 E:'shulou',A:'rain',B:'dujiang',C:'huai',D:'shulou',F:'haodenglou',
 G:'shulou',H:'yuanmen',I:'qinhuai',J:'shulou',K:'qinhuai',L:'moling',
 M:'haodenglou',N:'yuanmen',O:'bailuzhou',P:'dashipo',Q:'dashipo',R:'bailuzhou',
 S:'shulou',T:'shulou',U:'qinhuai',V:'qinhuai',W:'shulou',X:'shulou'
};
/* 雨驿一夜 14 幕：按说话人换脸，幕内场景也随雨驿→驿道→渡口移动 */

/* ---------- 作者原稿平涂风格：旧厚涂层一律回退 ----------
   用户确认：厚涂风格「保存但不用」。旧 17 层源图归档，游戏里只显示
   已按原稿重画的 6 个角色 + 4 个表情变体，共 10 张。 */
const ORIG_FALLBACK={};  /* R5：23 层原稿风全齐，不再需要回退 */
/* R15 一致性收尾：检查器判「不一致／偏离」的 11 张历史层仍在游戏里显示。
   这里在显示层统一重定向到已通过一致性检查的 40 张存量层，源图照旧归档、不删不重抠。
   优先同角色通过版；无同角色者按神态／动作近似代用，CAST 标签注明「一致性代用」。 */
const CONSISTENCY_REMAP={"cos_du": "B_face_du", "cos_wen": "B_face_yuane", "cos_jin_guard": "A_face_guard", "cos_jinhe_laugh": "B_act_smash", "act_slam": "B_act_smash", "cos_yuancl_warm": "D_face_yuancl", "cos_qinwen_wry2": "B_face_qinwen", "cos_yuaner_vain": "B_face_yuane", "cos_wen_lose": "D_face_yuancl", "cos_tian_serious": "E_face_wink", "act_umbrella": "D_act_lamp"};
/* R19：行头重映射。用户指出「荆三娘怎么不穿衣服」——原检查器无「服装」维度，
   裸猫＋道具一直判合格。这里把无行头层重定向到本轮穿衣版；本色 cos_base 有意保留裸猫。 */
const COSTUME_REMAP={"cos_jin":"R22_jin","cos_ying":"R25_lip_ying","cos_geng":"R22_geng","cos_yuaner":"R25_act_sleeve","cos_luo":"R22_luo","cos_jinhe":"R23_build_jinhe","cos_qinwen":"R22_qinwen","cos_shi":"H_cost_shi","cos_luo_nod":"H_cost_luo","cos_luo_draw":"H_cost_luo","cos_luo_guard":"H_cost_luo","cos_ying_sing":"H_cost_ying","cos_ying_clear":"H_cost_ying","A_face_shen":"cos_shen","A_face_argue":"cos_shen","A_face_ying":"H_cost_ying","A_face_luo":"H_cost_luo","A_face_geng":"H_cost_geng","A_face_jin":"A_face_jin","A_face_draw":"H_cost_luo","A_face_yuane":"H_cost_yuaner","A_face_jinhe":"H_cost_jinhe","A_face_qinwen":"H_cost_qinwen","A_face_guard":"H_cost_shi","cos_shen":"HR_shen","cos_xiao":"R25_lip_xiao","cos_yi":"R23_build_yi","cos_yuancl":"R25_scar_yuancl","cos_jiao":"R25_scar_jiao","cos_zhu":"R25_lip_zhu","cos_du":"R22_du"};
function origCast(c){ return COSTUME_REMAP[c]||CONSISTENCY_REMAP[c]||ORIG_FALLBACK[c]||c; }

const A_CAST={
 s1:'cos_jin',s2:'cos_jin',s3:'cos_shen',s4:'cos_ying',s5:'cos_ying',
 s6:'cos_jin',s7:'cos_geng',s8:'cos_yuaner',s9:'cos_yuaner',s10:'cos_luo',
 s11:'cos_jinhe',s12:'cos_jinhe',s13:'cos_qinwen',s14:'cos_shen'
};
const A_BG={
 s1:'qilipu',s2:'rain',s3:'rain',s4:'rain',s5:'rain',s6:'rain',s7:'rain',
 s8:'rain',s9:'rain',s10:'rain',s11:'dujiang',s12:'dujiang',s13:'dujiang',s14:'dujiang'
};
const ROLE_CAST={'骆寒':'cos_luo','易敛':'cos_yi','沈放':'cos_shen','荆三娘':'cos_jin',
 '袁辰龙':'cos_yuancl','萧如':'cos_xiao','耿苍怀':'cos_geng','秦稳':'cos_qinwen'};
/* R15 第五关 C 淮上旧盟：五关资源棋逐关换脸，结算换朱妍。
   全部指向已通过一致性检查的存量层，不重复内嵌图片数据。 */
const C_CAST={"0": "B_face_yi", "1": "B_face_du", "2": "B_face_jiao", "3": "D_face_xiaoru", "4": "B_face_yuane", "5": "D_face_zhuyan"};
/* R16 第六关 F 谣言审判：6 桩公案逐案换脸，结算换朱妍；序列帧连播用本轮衍生帧。 */
const F_CAST={"0": "A_face_shen", "1": "D_face_luohan", "2": "B_face_qinwen", "3": "D_face_shen", "4": "D_face_yuancl", "5": "E_face_wink", "6": "D_face_zhuyan"};
/* R18 第七关 G 校书局：10 道版本/异文题逐题换脸，全部为本轮 AI 生成并通过一致性检查。 */
/* R20：G 校书局 10 槽全换穿衣版。index 4「掩卷沉吟」本批 G_cost_close 判偏离不接入，
   暂用 R19 已通过且已穿衣的 H_cost_geng 代用，登记簿标「待重画」，不冒充新生成。 */
const G_CAST={"0": "G_cost_verify", "1": "G_cost_compare", "2": "G_cost_brush", "3": "G_cost_startled", "4": "H_cost_geng", "5": "G_cost_smile", "6": "G_cost_turn", "7": "G_cost_scroll", "8": "G_cost_blink", "9": "G_cost_open"};
/* R19 第八关 H 辕门簿：10 题逐题换脸，全部为穿衣版。 */
const I_CAST={"0":"R25_I_zhu","1":"R25_I_ying","2":"R25_lip_xiao","3":"R25_scar_yuancl","4":"R25_scar_jiao","5":"R25_act_sleeve","6":"R25_lip_zhu","7":"R23_build_yi","8":"R22_jin","9":"R25_lip_ying"};
const J_CAST={"0":"R26_J_read","1":"R26_J_fit","2":"G_cost_verify","3":"R26_J_brush","4":"R26_J_compare","5":"G_cost_compare","6":"R26_J_startled","7":"R26_J_done","8":"R26_J_turn","9":"R26_J_lamp"};
const K_CAST={"0":"R29_K_read","1":"R29_K_brush","2":"R29_K_compare","3":"R29_K_pause","4":"R29_K_ah","5":"R29_K_cup","6":"R29_K_bridge","7":"R29_K_check","8":"R29_K_smile","9":"R29_K_done"};
const H_CAST={"0": "H_cost_shi", "1": "H_cost_yuchi", "2": "H_cost_yuaner", "3": "H_cost_luo", "4": "H_cost_jin", "5": "H_cost_qinwen", "6": "H_cost_geng", "7": "cos_shen", "8": "H_cost_jinhe", "9": "H_cost_ying"};

/* ---------- 借鉴 WebGAL / Monogatari：舞台命令日志（P0） ----------
   只记录意图、不重放副作用、不改现有渲染路径；命令序列可用于回放与自动测试。
   完整命令解释器见《开源AVG与视觉小说引擎借鉴调研》P1。 */
const STAGE_LOG=[], STAGE_LOG_MAX=240;
function emitStage(type,p){
 try{STAGE_LOG.push(Object.assign({t:Date.now(),type:type},p||{}));
  if(STAGE_LOG.length>STAGE_LOG_MAX)STAGE_LOG.shift();}catch(e){}
}
function stageLogSummary(){
 const c={};for(const e of STAGE_LOG)c[e.type]=(c[e.type]||0)+1;
 return {total:STAGE_LOG.length,types:c,last:STAGE_LOG[STAGE_LOG.length-1]||null};
}

function stageFor(k){
 let bg=STAGE_BG[k]||'rain';
 let cast=LEVEL_AVATAR[k]||'cos_base';
 if(k==='A'){ bg=A_BG[S.A.node]||'rain'; cast=A_CAST[S.A.node]||'cos_shen'; }
 if(k==='C'){ const ck=S.C?Math.min(5,Math.max(0,S.C.k||0)):0; cast=C_CAST[ck]||'B_face_yi'; }
 if(k==='F'){ const fk=S.F?Math.min(6,Math.max(0,S.F.i||0)):0; cast=F_CAST[fk]||'A_face_shen'; }
 if(k==='G'){ const gi=S.G?Math.min(9,Math.max(0,S.G.i||0)):0; cast=G_CAST[gi]||'G_face_verify'; }
 if(k==='H'){ const hi=S.H?Math.min(9,Math.max(0,S.H.i||0)):0; cast=H_CAST[hi]||'H_cost_shi'; }
 if(k==='I'){ const ii=S.I?Math.min(9,Math.max(0,S.I.i||0)):0; cast=I_CAST[ii]||'R25_I_zhu'; }
 if(k==='J'){ const ji=S.J?Math.min(9,Math.max(0,S.J.i||0)):0; cast=J_CAST[ji]||'R26_J_read'; }
 if(k==='K'){ const ki=S.K?Math.min(9,Math.max(0,S.K.i||0)):0; cast=K_CAST[ki]||'R29_K_read'; }
 if(k==='E'&&S.E.stage==='end'&&S.E.top){
  const r=D.E.roles[S.E.top]; if(r&&ROLE_CAST[r.n])cast=ROLE_CAST[r.n];
 }
 if(VBG_OVER[k])bg=VBG_OVER[k];
 if(CATFIX){ const rr=CATCOST.find(x=>x[0]===CATFIX); if(rr)cast=rr[2]; }
 else if(MOOD.key)cast=MOOD.key;
 if(VCAST_OVER[k])cast=VCAST_OVER[k];
 emitStage('resolve',{lv:k,bg:bg,cast:origCast(cast)});
 return {bg:bg,cast:origCast(cast)};
}
/* 同一张场景板按「关 + 幕」取三种景别与色温，等于把 11 张板用出 33 种取景 */
const SCENE_VIEW=[
 ['center 42%','none'],['center 68%','saturate(.88) brightness(.94)'],
 ['left 38%','sepia(.10) contrast(1.04)']
];
function viewSeed(k){
 const s=k+':'+(k==='A'?S.A.node:'')+':'+(S[k]&&S[k].i!==undefined?S[k].i:'');
 let h=0; for(let i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))|0;
 return Math.abs(h)%SCENE_VIEW.length;
}
function stageBlock(k,compact){
 const s=stageFor(k);
 const bl=(BGLIST.find(x=>x[0]===s.bg)||['',''])[1];
 const cl=(CAST.find(x=>x[0]===s.cast)||['',''])[1];
 const vw=SCENE_VIEW[viewSeed(k)];
 const wx=sceneWeather(s.bg);
 const _pend=perfMissing(k).length>0;
 return `<div class="stage ${compact?'sm':''}" role="img" data-weather="${wx.fx}" data-perf="${_pend?'pending':'ready'}"
   aria-label="场景：${esc(bl)}，${esc(wx.label)}，${esc(FX_LABEL[wx.fx])}；角色：哈士喵扮作${esc(cl)}${_pend?'；完整演出筹备中':''}">
   <div class="stagebg" data-bg="bg_${s.bg}"
     style="background-position:${vw[0]};filter:${vw[1]}"></div>
   <div class="stagefx fx-${wx.fx}" data-layer="${FXMODE}" aria-hidden="true">
    <i class="fx-a"></i><i class="fx-b"></i><i class="fx-c"></i>
    ${fxArt(wx.fx)}
    <span class="bird b1"></span><span class="bird b2"></span><span class="bird b3"></span>
    <span class="glow"></span><span class="spark s1"></span><span class="spark s2"></span><span class="spark s3"></span>
   </div>
   <div class="stagecut" data-art="${s.cast}"></div>
   <div class="stagevign" aria-hidden="true"></div>
   <div class="avgwho"><span class="avgdot"></span>
    <i class="perficon" role="img" aria-label="当前角色头像；表演时轮播点头、摇头或呼吸小帧"></i><b>${esc(whoLine(s.cast))}</b>
    <em class="avgsub">${esc(castMeta(s.cast)[1])}</em>
    <em>◈ ${esc(bl)}　${esc(wx.label)}${_pend?'　· 演出筹备中':''}　·　✥ 拖立绘／双指缩放</em></div>
   <button class="zoombtn stage-zoom" data-act="zoom_sprite" aria-label="全屏查看当前场景与立绘">⤢ 看大图</button>
   <div class="zpair"><button class="zoombtn" data-act="spr_zoom" data-v="0.85" aria-label="缩小立绘">－</button><button class="zoombtn" data-act="spr_zoom" data-v="1.18" aria-label="放大立绘">＋</button></div>
   <div class="sprhit" aria-hidden="true" title="拖动立绘 · 双指缩放"></div>
   <div class="stagecap"><span class="stageloc">◈ ${esc(bl)}</span>
    <span class="stagewho">${esc(whoLine(s.cast))}</span></div></div>`;
}
/* 情绪反馈不整页重绘，只换舞台上的那张脸，点击后立即看得见 */
function refreshStageCast(){
 const el=document.querySelector('#app .stagecut'); if(!el)return;
 const s=stageFor(TAB);
 emitStage('apply',{lv:TAB,bg:s.bg,cast:s.cast});
 if(ART[s.cast]){el.dataset.art=s.cast;el.style.backgroundImage="url('"+ART[s.cast]+"')";}
 const cl=(CAST.find(x=>x[0]===s.cast)||['',''])[1];
 const who=document.querySelector('#app .stagewho'); if(who)who.textContent=whoLine(s.cast);
 const sub=document.querySelector('#app .avgwho .avgsub'); if(sub)sub.textContent=castMeta(s.cast)[1];
 const wb=document.querySelector('#app .avgwho b'); if(wb)wb.textContent=whoLine(s.cast);
 if(ART[s.cast])document.documentElement.style.setProperty('--catav',"url('"+ART[s.cast]+"')");
 const st=document.querySelector('#app .stage');
 if(st)st.setAttribute('aria-label','场景：'+(BGLIST.find(x=>x[0]===s.bg)||['',''])[1]+'；角色：哈士喵扮作'+cl);
}
function stagePulse(kind){
 const st=document.querySelector('#app .stage'); if(!st)return;
 st.classList.remove('ok','no'); void st.offsetWidth; st.classList.add(kind);
 setTimeout(()=>st.classList.remove(kind),640);
}

const CATCOST=[
 ['auto','自动','cos_base'],
 ['base','本色','cos_base'],
 ['shen','沈放','cos_shen'],['luo','骆寒','cos_luo'],['jin','荆三娘','cos_jin'],
 ['yi','易敛','cos_yi'],['zhu','朱妍','cos_zhu'],['xiao','萧如','cos_xiao'],
 ['geng','耿苍怀','cos_geng'],['qinwen','秦稳','cos_qinwen'],['jinhe','金和尚','cos_jinhe'],
 ['ying','小英子','cos_ying'],['du','杜淮山','cos_du'],['jiao','焦泗隐','cos_jiao'],
 ['gbx','庚不信','cos_gbx'],['qu','瞿百龄','cos_qu'],
 ['yuancl','袁辰龙','cos_yuancl'],['yuaner','袁二','cos_yuaner'],
 ['wen','文翰林','cos_wen'],['mi','米俨','cos_mi'],['shi','石燃','cos_shi'],
 ['zwl','赵无量','cos_zwl'],['tian','田笑','cos_tian'],['tie','铁萼英','cos_tie'],
 ['shen_argue','沈放·强辩','cos_shen_argue'],['luo_draw','骆寒·出剑','cos_luo_draw'],
 ['yi_grief','易敛·沉痛','cos_yi_grief'],['zhu_resolve','朱妍·决绝','cos_zhu_resolve']
];
/* 换装台：11 背景 × 23 角色；第 3 项推荐背景，第 4 项 2=原生纯抠（23 层已全部统一） */
const BGLIST=[
 ['rain','雨驿雨夜'],['huai','淮上夜帐'],['yuanmen','辕门月夜'],['qinhuai','秦淮灯影'],
 ['qilipu','七里铺驿道'],['dujiang','拂晓渡口'],['shulou','校书局书楼'],['haodenglou','好登楼'],
 ['bailuzhou','白鹭洲芦荡'],['dashipo','大石坡石阵'],['moling','秣陵冬紫金山']
];
const CAST=[
 ['cos_base','本色 · 吐舌笑','rain'],
 ['cos_shen','沈放 · 错愕','rain'],['cos_luo','骆寒 · 清冷','rain'],
 ['cos_jin','荆三娘 · 冷冽','rain'],['cos_yi','易敛 · 倦笑','huai'],
 ['cos_zhu','朱妍 · 含泪','qinhuai'],['cos_xiao','萧如 · 寂寥','qinhuai'],
 ['cos_geng','耿苍怀 · 沉郁','rain'],['cos_qinwen','秦稳 · 苦笑','rain'],
 ['cos_jinhe','金和尚 · 佯狂','rain'],['cos_ying','小英子 · 怯喜','rain'],
 ['cos_du','杜淮山 · 笃定 · 通过版','huai'],['cos_jiao','焦泗隐 · 峭拔','huai'],
 ['cos_gbx','庚不信 · 激昂','huai'],['cos_qu','瞿百龄 · 苍老','huai'],
 ['cos_yuancl','袁辰龙 · 威严','yuanmen'],['cos_yuaner','袁二 · 倨傲','yuanmen'],
 ['cos_wen','文翰林 · 阴鸷 · 一致性代用','shulou'],['cos_mi','米俨 · 沉静','shulou'],
 ['cos_shi','石燃 · 机警','yuanmen'],['cos_zwl','赵无量 · 苍凉','bailuzhou'],
 ['cos_tian','田笑 · 坏笑','qinhuai'],['cos_tie','铁萼英 · 倔强','qinhuai'],
 ['cos_shen_argue','沈放 · 强辩','rain'],['cos_luo_draw','骆寒 · 出剑','rain'],
 ['cos_yi_grief','易敛 · 沉痛','huai'],['cos_zhu_resolve','朱妍 · 决绝','qinhuai'],
 ['cos_shen_calm','沈放 · 沉吟','rain'],['cos_shen_shrug','沈放 · 无奈','rain'],
 ['cos_luo_nod','骆寒 · 颔首','rain'],['cos_luo_guard','骆寒 · 按剑','rain'],
 ['cos_yi_cup','易敛 · 举杯','huai'],['cos_jin_guard','荆三娘 · 横刀 · 通过版','rain'],
 ['cos_zhu_smile','朱妍 · 破涕','qinhuai'],['cos_zhu_turn','朱妍 · 回眸','qinhuai'],
 ['cos_xiao_sigh','萧如 · 低眉','qinhuai'],['cos_qinwen_wry','秦稳 · 苦笑','rain'],
 ['cos_yuancl_agree','袁辰龙 · 惺惺相惜','yuanmen'],
 ['cos_wen_sly','文翰林 · 阴鸷转笑','haodenglou'],
 ['cos_xiao_sing','萧如 · 将歌','qinhuai'],
 ['cos_geng_trust','耿苍怀 · 托孤','rain'],
 ['cos_qinwen_smash','秦稳 · 砸招牌','dujiang'],
 ['cos_jinhe_laugh','金和尚 · 放声大笑 · 一致性代用','rain'],
 ['cos_ying_sing','小英子 · 唱词','rain'],
 ['cos_tian_wink','田笑 · 挤眼坏笑','shulou'],
 ['act_draw','骆寒 · 出剑','rain'],
 ['act_sheathe','骆寒 · 收剑','rain'],
 ['act_write','沈放 · 题壁','shulou'],
 ['act_push','秦稳 · 推车','dujiang'],
 ['act_curtain','小英子 · 掀帘','rain'],
 ['act_jade','耿苍怀 · 递玉','rain'],
 ['act_ledger','易敛 · 翻账','huai'],
 ['act_lamp','朱妍 · 执灯','qinhuai'],
 ['act_flag','袁辰龙 · 掀旗','yuanmen'],
 ['act_cup','易敛 · 举杯','huai'],
 ['act_slam','田笑 · 按案 · 一致性代用','shulou'],
 ['cos_yuancl_warm','袁辰龙 · 惺惺相惜（过渡） · 通过版','yuanmen'],
 ['cos_qinwen_wry2','秦稳 · 绷住转苦笑 · 通过版','rain'],
 ['cos_ying_clear','小英子 · 清亮唱词','rain'],
 ['cos_jinhe_calm','金和尚 · 狂态收敛','rain'],
 ['cos_yuaner_vain','袁二 · 倨傲不甘 · 通过版','yuanmen'],
 ['cos_wen_lose','文翰林 · 败局 · 一致性代用','shulou'],
 ['cos_zwl_firm','赵无量 · 决绝','bailuzhou'],
 ['cos_tian_serious','田笑 · 正色 · 一致性代用','shulou'],
 ['act_turn','回眸','qinhuai'],
 ['act_umbrella','雨中撑伞 · 一致性代用','rain'],
 ['E_face_wink','一关 · 本色眨眼','shulou'],
 ['E_face_tear','一关 · 含泪笑','qinhuai'],
 ['E_act_cup','一关 · 捧木杯','huai'],
 ['E_act_mirror','一关 · 照镜','shulou'],
 ['E_seq_open','一关 · 睁眼帧','shulou'],
 ['E_seq_blink','一关 · 闭眼帧','shulou'],
 ['E_seq_talk','一关 · 说话帧','shulou'],
 ['E_seq_nod','一关 · 点头帧','shulou'],
 ['E_seq_ear','一关 · 耳动帧','shulou'],
 ['E_seq_tail','一关 · 尾摆帧','shulou'],
 ['A_face_shen','二关 · 沈放错愕','rain'],
 ['A_face_argue','二关 · 沈放强辩','rain'],
 ['A_face_jin','二关 · 三娘冷冽','rain'],
 ['A_face_guard','二关 · 三娘横刀','rain'],
 ['A_face_ying','二关 · 小英子唱词','rain'],
 ['A_face_geng','二关 · 耿苍怀托孤','rain'],
 ['A_face_luo','二关 · 骆寒清冷','rain'],
 ['A_face_draw','二关 · 骆寒按剑','rain'],
 ['A_seq_open','二关 · 睁眼帧','rain'],
 ['A_seq_blink','二关 · 闭眼帧','rain'],
 ['B_face_qinwen','三关 · 秦稳翻账','dujiang'],
 ['B_face_luohan','三关 · 骆寒按剑','dujiang'],
 ['B_face_du','三关 · 杜淮山笃定','huai'],
 ['B_face_jiao','三关 · 焦泗隐抱剑','huai'],
 ['B_face_yi','三关 · 易敛举杯','huai'],
 ['B_face_yuane','三关 · 袁二拂袖','yuanmen'],
 ['B_act_push','三关 · 推独轮车','dujiang'],
 ['B_act_smash','三关 · 砸招牌','dujiang'],
 ['B_seq_open','三关 · 睁眼帧','dujiang'],
 ['B_seq_blink','三关 · 闭眼帧','dujiang'],
 ['D_face_xiaoru','四关 · 萧如将歌','qinhuai'],
 ['D_face_zhuyan','四关 · 朱妍含泪','qinhuai'],
 ['D_face_yi','四关 · 易敛沉痛','huai'],
 ['D_face_luohan','四关 · 骆寒收剑','dujiang'],
 ['D_face_shen','四关 · 沈放释然','shulou'],
 ['D_face_yuancl','四关 · 袁辰龙威严','yuanmen'],
 ['D_act_write','四关 · 题壁执笔','qilipu'],
 ['D_act_lamp','四关 · 执灯照卷','shulou'],
 ['D_seq_open','四关 · 睁眼帧','shulou'],
 ['D_seq_blink','四关 · 闭眼帧','shulou'],
 ['F_seq_half','半闭眼中间帧','haodenglou'],
 ['F_seq_quarter','眨眼起帧','rain'],
 ['F_seq_threeq','眨眼落帧','dujiang'],
 ['F_seq_nod_mid','点头中间帧','shulou'],
 ['F_seq_talk_mid','开口中间帧','huai'],
 ['F_seq_ear_mid','耳朵动中间帧','qilipu'],
 ['F_seq_tail_mid','尾巴动中间帧','yuanmen'],
 ['F_seq_cross','跨关姿态过渡帧','qinhuai'],
 ['F_breath_in','吸气帧·胸腔微抬','shulou'],
 ['F_breath_out','呼气帧·回落','shulou'],
 ['G_face_verify','G关 · 细校 · 专注','shulou'],
 ['G_face_compare','G关 · 比对异文 · 狐疑','shulou'],
 ['G_face_brush','G关 · 朱笔圈点 · 审慎','shulou'],
 ['G_face_startled','G关 · 发现错字 · 错愕','shulou'],
 ['G_face_close','G关 · 掩卷沉吟','shulou'],
 ['G_face_smile','G关 · 校定释然 · 轻笑','shulou'],
 ['G_act_turn','G关 · 翻页','shulou'],
 ['G_act_scroll','G关 · 展卷','shulou'],
 ['G_seq_blink','G关 · 校书眨眼落帧','shulou'],
 ['G_seq_open','G关 · 校书睁眼起帧','shulou'],
 ['H_cost_jin','穿衣版 · 荆三娘 · 墨紫劲装','rain'],
 ['H_cost_ying','穿衣版 · 小英子 · 藕荷碎花小袄','rain'],
 ['H_cost_geng','穿衣版 · 耿苍怀 · 赭褐旧袍','rain'],
 ['H_cost_yuaner','穿衣版 · 袁二 · 缇骑朱袍','yuanmen'],
 ['H_cost_luo','穿衣版 · 骆寒 · 玄黑披风','dujiang'],
 ['H_cost_jinhe','穿衣版 · 金和尚 · 赭黄僧衣','rain'],
 ['H_cost_qinwen','穿衣版 · 秦稳 · 灰布短打','dujiang'],
 ['H_cost_shi','穿衣版 · 石燃 · 狐骑短甲','yuanmen'],
 ['H_cost_yuchi','穿衣版 · 尉迟渺 · 玄甲双车','yuanmen'],
 ['G_cost_verify','G关 · 校书郎 · 细校 · 专注','shulou'],
 ['G_cost_compare','G关 · 校书郎 · 比对异文 · 狐疑','shulou'],
 ['G_cost_brush','G关 · 校书郎 · 朱笔圈点 · 审慎','shulou'],
 ['G_cost_startled','G关 · 校书郎 · 发现错字 · 错愕','shulou'],
 ['G_cost_smile','G关 · 校书郎 · 校定释然 · 轻笑','shulou'],
 ['G_cost_turn','G关 · 校书郎 · 翻页','shulou'],
 ['G_cost_scroll','G关 · 校书郎 · 展卷','shulou'],
 ['G_cost_blink','G关 · 校书郎 · 校书眨眼落帧','shulou'],
 ['G_cost_open','G关 · 校书郎 · 校书睁眼起帧','shulou'],
 ['HR_geng','耿苍怀 · 深灰束带 · 赭褐旧袍','rain'],
 ['HR_qinwen','秦稳 · 赭褐布巾 · 灰布短打','dujiang'],
 ['HR_shen','沈放 · 青灰文士软巾 · 青衫','rain'],
 ['HR_xiao','萧如 · 揉蓝包头布 · 揉蓝衫子','qinhuai'],
 ['HR_yi','易敛 · 素木簪低髻 · 青灰长衫','huai'],
 ['HR_ying','小英子 · 藕荷单丫髻 · 碎花小袄','rain'],
 ['HR_yuancl','袁辰龙 · 玄色矮幞头 · 缇骑玄袍','yuanmen'],
 ['R22_geng','耿苍怀 · 深灰络腮短须','rain'],
 ['R22_jiao','焦泗隐 · 深灰束带','huai'],
 ['R22_jin','荆三娘 · 深褐单高髻假发','rain'],
 ['R22_qinwen','秦稳 · 深褐八字短须','dujiang'],
 ['R22_yuancl','袁辰龙 · 短须','yuanmen'],
 ['R22_zhu','朱妍 · 单环髻假发','qinhuai'],
 ['R23_lip_zhu','朱妍 · 淡朱砂唇（唇色未显）','qinhuai'],
 ['R23_lip_xiao','萧如 · 淡豆沙唇（唇色未显）','qinhuai'],
 ['R23_build_yuancl','袁辰龙 · 阔肩披肩（体态暗示）','yuanmen'],
 ['R23_build_yi','易敛 · 束腰（体态暗示）','huai'],
 ['R23_build_jinhe','金和尚 · 袒腹（体态暗示）','rain'],
 ['R23_act_carry','秦稳 · 深灰褐短打','dujiang'],
 ['R22_du','杜淮山 · 花白长须','huai'],
 ['R22_jinhe','金和尚 · 浓黑短茬胡','rain'],
 ['R22_luo','骆寒 · 深褐长披发假发','rain'],
 ['R25_lip_zhu','朱妍 · 深赭红唇','qinhuai'],
 ['R25_lip_xiao','萧如 · 深赭红唇','qinhuai'],
 ['R25_lip_ying','小英子 · 深赭红唇','rain'],
 ['R25_scar_yuancl','袁辰龙 · 眉骨疤','yuanmen'],
 ['R25_scar_jiao','焦泗隐 · 脸颊疤','huai'],
 ['R25_act_sleeve','袁二 · 拂袖','yuanmen'],
 ['R25_I_zhu','朱妍 · 回眸','qinhuai'],
 ['R25_I_ying','小英子 · 唱词','rain'],
 ['R26_J_read','易敛 · 展卷细读','shulou'],
 ['R26_J_fit','易敛 · 拼合回目','shulou'],
 ['R26_J_brush','易敛 · 朱笔圈题','shulou'],
 ['R26_J_compare','易敛 · 比对目录','shulou'],
 ['R26_J_startled','易敛 · 发现缺章','shulou'],
 ['R26_J_done','易敛 · 校定释然','shulou'],
 ['R26_J_turn','易敛 · 翻页','shulou'],
 ['R26_J_lamp','易敛 · 执灯照卷','shulou'],
 ['R29_K_read','萧如 · 展卷细读','shulou'],
 ['R29_K_brush','易敛 · 拈笔笺注','shulou'],
 ['R29_K_compare','易敛 · 两卷并读','shulou'],
 ['R29_K_pause','朱妍 · 停云凝思','shulou'],
 ['R29_K_ah','易敛 · 恍然得句','shulou'],
 ['R29_K_cup','易敛 · 金荷酌客','shulou'],
 ['R29_K_bridge','易敛 · 长桥题壁','shulou'],
 ['R29_K_check','校书郎 · 指认异文','shulou'],
 ['R29_K_smile','朱妍 · 会心','shulou'],
 ['R29_K_done','易敛 · 合卷落印','shulou'],];
let DRESS={bg:'rain',who:'cos_base'};
function dressStage(){
 const _who=origCast(DRESS.who);
 const cur=CAST.find(x=>x[0]===_who)||CAST[0];
 const bgl=(BGLIST.find(x=>x[0]===DRESS.bg)||BGLIST[0])[1];
 return `<div class="dresswrap">
  <div class="dresspreview" role="img" aria-label="换装台预览：${esc(cur[1])}，背景${bgl}">
   <div class="dbg" data-bg="bg_${DRESS.bg}"></div>
   <div class="dcut" data-art="${_who}"></div>
   <div class="dcap"><b>${esc(castMeta(_who)[0])} · ${esc(cur[1])}</b><span>${bgl}　原生纯抠</span></div>
  </div>
  <div class="dressctl">
   <div class="dressrow"><span class="dl">背景</span><div class="dressbtns">${BGLIST.map(([v,l],i)=>{
    const u=bgUnlocked(i); return `<button class="${DRESS.bg===v?'on':''} ${u?'':'lock'}" data-act="dress_bg" data-v="${v}"
     aria-label="${u?'背景':'🔒 通关第 '+bgNeed(i)+' 关解锁 '}${l}">${u?l:'🔒 '+l}</button>`; }).join('')}</div></div>
   <div class="dressrow"><span class="dl">角色</span><div class="dressbtns scroll">${CAST.map(([k,l],i)=>{
    const u=castUnlocked(i,CAST.length); return `<button class="who ${DRESS.who===k?'on':''} ${u?'':'lock'}" data-act="dress_who" data-v="${k}"
     aria-label="${u?'角色':'🔒 通关第 '+castNeed(i,CAST.length)+' 关解锁 '}${l}">${u?l:'🔒 '+l}</button>`; }).join('')}</div></div>
   <p class="dressstat">11 张背景 × ${CAST.length} 个透明角色；当前 ${esc(cur[1])} @ ${bgl}。<b>场景 ${bgCount()}/11 已解锁</b>，人物随通关数逐步开放；锁住的灰色按钮点下去只提示解锁条件。</p>
   <p class="dressnote">全部为原生纯抠：纯品红底重新生成、实心封闭、色键＋填洞＋去色溢，内部孔洞数为 0。选项表演专用的 10 张表情层属于关卡演出，不占这里的可选位。</p>
  </div></div>`;
}
function renderDress(){ const m=$('#dressMount'); if(!m)return; m.innerHTML=dressStage(); decorate(); }
function fixedKey(){ const r=CATCOST.find(x=>x[0]===CATFIX); return r?r[2]:'cos_base'; }
function avatarKey(){
 if(CATFIX)return fixedKey();          /* 手动固定优先于短暂情绪反馈 */
 if(MOOD.key)return MOOD.key;
 if(TAB!=='hall'&&LEVEL_AVATAR[TAB])return LEVEL_AVATAR[TAB];
 if(isChallenge())return 'cos_luo';
 if(isRoam())return 'cos_xiao';
 if(isNew())return 'cos_yi';
 return 'cos_base';
}
function applyCatAv(){ document.documentElement.style.setProperty('--catav',"url('"+ART[origCast(avatarKey())]+"')"); }
function setMood(k,ms){
 if(!CATMOOD_ON||!k)return;
 MOOD.key=k; applyCatAv(); refreshStageCast(); clearTimeout(MOOD.t);
 MOOD.t=setTimeout(()=>{MOOD.key='';applyCatAv();refreshStageCast();},ms);
}
function catBar(){
 const cur=CATFIX||'auto';
 return `<div class="catbar slim" aria-label="哈士喵引导员表情选择，点卡片看大图">
  <div class="cb-scroll">${CATCOST.map(([v,label,key],i)=>{
   const u=castUnlocked(i,CATCOST.length), need=castNeed(i,CATCOST.length);
   return `<button class="${v==='auto'?'auto':''} ${cur===v?'on':''} ${u?'':'lock'}" data-act="cat_fix" data-v="${v}"
     ${v==='auto'||!u?'':`style="background-image:url('${ART[key]}')"`}
     aria-label="${u?'预览并固定 ':'🔒 通关第 '+need+' 关解锁 '}${label}${cur===v?'，当前':''}" title="${label}">${v==='auto'?'自动':(u?'':'🔒')}</button>`;
  }).join('')}</div>
  <span class="cb-hint">点卡片换人 · 🔒 随进度解锁 · ⤢ 放大</span>
 </div>`;
}

/* ---------- R4：点角色卡出大图预览 ---------- */
function catPeekKey(v){
 if(v==='auto'||!v)return origCast(avatarKey());
 const r=CATCOST.find(x=>x[0]===v); return r?r[2]:'cos_shen';
}
function openCatPeek(v){ return; }
function closeCatPeek(){ const p=$('#catPeek'); if(p)p.hidden=true; }

/* ---------- 朗读（Web Speech TTS） ---------- */

/* ---------- 人声表演：系统声线区分 + 可导入语音包 ----------
   三层：① 系统 TTS 按角色改 pitch/rate（零素材、不是表演）
        ② 外部导入真人语音包（真表演，会话内有效）
        ③ 云端 TTS / wasm 引擎不做（违反离线单文件约束） */
const VOICE_LINE={
 narrator:{pitch:1.00,rate:1.00,name:'旁白'},
 cos_luohan:{pitch:.78,rate:.90,name:'骆寒 · 清冷'},
 cos_yilian:{pitch:.92,rate:.94,name:'易敛 · 倦暖'},
 cos_shen:{pitch:1.14,rate:1.08,name:'沈放 · 文士'},
 cos_jinsanniang:{pitch:.96,rate:.96,name:'荆三娘 · 冷冽'},
 cos_xiaoru:{pitch:1.10,rate:.92,name:'萧如 · 寂寥'},
 cos_zhuyan:{pitch:1.22,rate:1.04,name:'朱妍 · 明丽'},
 cos_yuanchenlong:{pitch:.72,rate:.88,name:'袁辰龙 · 威严'},
 cos_wenhanlin:{pitch:.84,rate:.92,name:'文翰林 · 阴鸷'},
 cos_qinwen:{pitch:.98,rate:.98,name:'秦稳 · 稳'},
 cos_gengcanghuai:{pitch:.82,rate:.90,name:'耿苍怀 · 沉郁'},
 cos_tianxiao:{pitch:1.18,rate:1.10,name:'田笑 · 跳脱'},
 cos_base:{pitch:1.04,rate:1.00,name:'哈士喵 · 本色'}
};
let PERFORM=0, VOICE_PACK=null, VOICE_AUD=null;
function voiceConf(cast){ return VOICE_LINE[cast]||VOICE_LINE.narrator; }
function lineId(){
 try{ const s=S[TAB]; return TAB+':'+(s?(s.node!==undefined?s.node:(s.i!==undefined?s.i:'0')):'0'); }
 catch(e){ return TAB+':0'; }
}
function currentCast(){ try{ return stageFor(TAB).cast||'cos_base'; }catch(e){ return 'cos_base'; } }
function splitLines(txt){
 return (txt.match(/[^。！？；\n]+[。！？；]?/g)||[]).map(s=>s.trim())
   .filter(s=>s.length>2).slice(0,14);
}
function stopVoicePack(){ if(VOICE_AUD){try{VOICE_AUD.pause();VOICE_AUD.currentTime=0;}catch(e){} VOICE_AUD=null;} }
function playClip(src){
 if(!src)return false;
 try{ stopVoicePack(); VOICE_AUD=new Audio(src); VOICE_AUD.play().catch(()=>{}); return true; }
 catch(e){ return false; }
}
function packClip(id,cast){
 const c=VOICE_PACK&&VOICE_PACK.clips||{};
 return c[id]||c['cast|'+cast]||null;
}
function performLines(txt,cast){
 try{
  window.speechSynthesis.cancel(); stopVoicePack();
  const id=lineId();
  const clip=packClip(id,cast);
  if(clip){ if(playClip(clip))return true; }   /* 有真人语音包就优先播，不回退 TTS */
  const lines=splitLines(txt);
  if(!lines.length)return false;
  lines.forEach(s=>{
   const quoted=/[「『“”"']/.test(s);
   const conf=voiceConf(quoted?cast:'narrator');
   const u=new SpeechSynthesisUtterance(s);
   u.lang='zh-CN'; u.rate=RATE*conf.rate; u.pitch=conf.pitch; u.volume=1;
   const v=pickVoice(); if(v)u.voice=v;
   window.speechSynthesis.speak(u);
  });
  return true;
 }catch(e){ return false; }
}
function setPerform(v){
 PERFORM=v?1:0; announce('人声表演已'+(PERFORM?'开启：按角色分句朗读':'关闭：恢复整屏朗读'));
}
function importVoicePack(file){
 if(!file)return;
 const fr=new FileReader();
 fr.onload=()=>{
  try{
   const j=JSON.parse(fr.result);
   if(!j||typeof j.clips!=='object'||!j.clips)throw new Error('格式不对');
   VOICE_PACK=j;
   const n=Object.keys(j.clips).length;
   announce('已导入语音包「'+(j.name||'未命名')+'」，共 '+n+' 段');
   renderA11yPanel();
  }catch(e){ announce('语音包导入失败：需要含 clips 对象的 JSON 文件'); }
 };
 fr.onerror=()=>announce('语音包读取失败');
 fr.readAsText(file);
}
function demoVoice(){
 const cast=currentCast();
 const clip=packClip('demo|'+cast,cast)||packClip(lineId(),cast);
 if(clip&&playClip(clip)){announce('试听语音包：'+voiceConf(cast).name);return;}
 if(!TTS){toggleTTS(1);}
 const u=new SpeechSynthesisUtterance('这一夜的雨，还没落完。');
 u.lang='zh-CN';u.rate=RATE*voiceConf(cast).rate;u.pitch=voiceConf(cast).pitch;
 const v=pickVoice();if(v)u.voice=v;
 try{window.speechSynthesis.cancel();window.speechSynthesis.speak(u);}catch(e){}
 announce('试听声线：'+voiceConf(cast).name+'（系统 TTS，非真人表演）');
}

function pickVoice(){
 try{
  const vs=window.speechSynthesis.getVoices()||[];
  return vs.find(v=>/zh[-_]?CN|Chinese|Mandarin|中文|普通话/i.test((v.lang||'')+' '+(v.name||'')))
      || vs.find(v=>/^zh/i.test(v.lang||'')) || null;
 }catch(e){return null;}
}
function ttsText(){
 const app=$('#app'); if(!app)return '';
 let t=(app.innerText||app.textContent||'')
   .replace(/\s*\n\s*/g,'。').replace(/[ \t]{2,}/g,' ').trim();
 return t.slice(0,700);
}
function speak(txt,force,cast){
 if(!TTS||!TTS_CAP||!txt)return;
 if(!force&&!TTSAUTO)return;
 try{
  if(PERFORM){ if(performLines(txt,cast||currentCast()))return; }
  window.speechSynthesis.cancel(); stopVoicePack();
  const u=new SpeechSynthesisUtterance(txt);
  u.lang='zh-CN'; u.rate=RATE; u.pitch=1; u.volume=1;
  const v=pickVoice(); if(v)u.voice=v;
  window.speechSynthesis.speak(u);
 }catch(e){}
}
function ttsStop(){ try{window.speechSynthesis&&window.speechSynthesis.cancel();}catch(e){} stopVoicePack(); }
function ttsReadNow(){
 if(!TTS_CAP){announce('当前浏览器不支持语音合成');return;}
 if(!TTS){toggleTTS(1);} 
 setTimeout(()=>speak(ttsText(),true,currentCast()),100);
 announce(PERFORM?'正在按角色分句朗读本屏':'正在朗读本屏');
}
function toggleTTS(force){
 TTS=(force===undefined)?(TTS?0:1):(force?1:0);
 if(TTS&&!TTS_CAP){ TTS=0; announce('当前浏览器不支持语音合成，朗读保持关闭'); }
 if(TTS){ announce('朗读已开启'); setTimeout(()=>speak(ttsText(),true,currentCast()),120); }
 else { ttsStop(); announce('朗读已关闭'); }
 syncHctl(); renderA11yPanel();
}
/* ---------- 语音控制（Web Speech Recognition） ---------- */
function asrSay(html){ ASR_MSG=html; const el=$('#asrState'); if(el)el.innerHTML=html;
 announce(String(html).replace(/<[^>]*>/g,'')); }
const CMDHELP='可以说：开始 / 下一题 / 选一（到选四）/ 回大厅 / 朗读开 / 朗读关 / 重读 / 停止朗读 / 背景音 / 音效 / 高对比 / 大字 / 帮助。';
function clickFirst(sels){
 for(const q of sels){ const b=document.querySelector(q);
  if(b&&!b.disabled&&!b.hasAttribute('disabled')){b.click();return true;} }
 return false;
}
function clickOption(n){
 const sel='#app .opt:not(:disabled),#app [data-act$="_ans"]:not(:disabled),'+
           '#app [data-act="A_choose"]:not(:disabled),#app [data-act="C_opt"]:not(:disabled),'+
           '#app [data-act="E_ans"]:not(:disabled),#app [data-act="F_ans"]:not(:disabled)';
 const list=[...new Set([...document.querySelectorAll(sel)])];
 if(list[n-1]){list[n-1].click();announce('已选第 '+n+' 项');}
 else announce('当前屏没有第 '+n+' 个可选项');
}
function handleCommand(raw){
 const t=String(raw).replace(/[\s，。！？、,.!?]/g,'');
 asrSay('听到：<b>'+esc(raw)+'</b>');
 const NM={'一':1,'二':2,'三':3,'四':4,'1':1,'2':2,'3':3,'4':4};
 if(/帮助|命令|能说什么|怎么说/.test(t)){ PANEL_TAB='asr'; openA11yPanel(); asrSay('<b>语音命令表</b>　'+CMDHELP); return; }
 if(/回大厅|大厅|返回|首页/.test(t)){ setTab('hall'); return; }
 if(/下一题|下一个|继续|下一步|前进/.test(t)){
  if(!clickFirst(['#app [data-act$="_next"]','#app [data-act="A_next"]','#app [data-act="B_next"]','#app .btn:not(.ghost)']))
   announce('当前屏没有「下一题」按钮');
  return;
 }
 if(/朗读开|打开朗读|开启朗读|开始朗读/.test(t)){ toggleTTS(1); return; }
 if(/朗读关|关闭朗读|别读|停止朗读|安静/.test(t)){ toggleTTS(0); ttsStop(); return; }
 if(/重读|再读|读一遍|念一遍/.test(t)){ ttsReadNow(); return; }
 if(/背景音|雨声|音乐|琴音/.test(t)){ cycleBGM(); return; }
 if(/音效|按键音|点击音/.test(t)){ toggleSFX(); return; }
 if(/高对比|对比度|反差/.test(t)){ toggleA11y('hc'); return; }
 if(/大字|放大|字大|字号/.test(t)){ toggleA11y('big'); return; }
 if(/减少动效|不要动画|静效/.test(t)){ toggleA11y('reduce'); return; }
 if(/开始|出发|进入|开玩/.test(t)){
  if(!clickFirst(['#app [data-act$="_start"]','#app .btn:not(.ghost)']))announce('当前屏没有「开始」按钮');
  return;
 }
 const m=t.match(/[一二三四1-4]/);
 if(m&&NM[m[0]]){ clickOption(NM[m[0]]); return; }
 announce('没听懂这句，可以说「帮助」看命令表');
}
function startASR(){
 if(!SR_CTOR){
  asrSay('<b>当前浏览器不支持语音识别</b>　仍可用键盘 1–4 选项、N 下一题、H 回大厅、R 重读，或直接点按。');
  ASR=0; return;
 }
 try{
  rec=new SR_CTOR(); rec.lang='zh-CN'; rec.continuous=true;
  rec.interimResults=false; rec.maxAlternatives=1;
  rec.onresult=e=>{ for(let i=e.resultIndex;i<e.results.length;i++)
    if(e.results[i].isFinal)handleCommand(e.results[i][0].transcript.trim()); };
  rec.onerror=e=>{
   const msg={'not-allowed':'麦克风权限被拒绝','service-not-allowed':'语音服务未授权',
    'no-speech':'没听清，再说一次','network':'本地文件下可能无法联网识别',
    'audio-capture':'找不到麦克风','aborted':'识别已中止'}[e.error]||e.error;
   asrSay('<b>语音识别提示</b>　'+esc(msg)+'；键盘与点按照常可用。');
  };
  rec.onend=()=>{ if(ASR){ try{rec.start();}catch(e){} } };
  rec.start(); ASR=1;
  asrSay('<b>🎙 语音控制已开启</b>　'+CMDHELP);
  announce('语音控制已开启');
 }catch(e){ ASR=0; asrSay('<b>无法启动语音识别</b>　'+esc(e.name)+'；键盘与点按照常可用。'); }
}
function stopASR(){
 ASR=0; try{rec&&rec.stop();}catch(e){} rec=null;
 asrSay('语音控制已关闭。朗读、背景音、音效仍按各自开关运行。');
 announce('语音控制已关闭');
}
function toggleASR(force){
 const want=(force===undefined)?(ASR?0:1):(force?1:0);
 if(want)startASR(); else stopASR();
 syncHctl(); renderA11yPanel();
}
/* ---------- 无障碍开关与面板 ---------- */
function toggleA11y(k){
 if(k==='hc'){HC=HC?0:1;try{localStorage.setItem(AKEY_HC,HC);}catch(e){}}
 else if(k==='big'){BIG=BIG?0:1;try{localStorage.setItem(AKEY_BIG,BIG);}catch(e){}}
 else if(k==='reduce'){REDUCE=REDUCE?0:1;try{localStorage.setItem(AKEY_RED,REDUCE);}catch(e){}}
 applyA11y(); renderA11yPanel();
 announce(({hc:'高对比',big:'大字号',reduce:'减少动效'})[k]+(k==='hc'?(HC?'已开':'已关'):k==='big'?(BIG?'已开':'已关'):(REDUCE?'已开':'已关')));
}
function setRate(v){
 RATE=[0.8,1,1.2].includes(+v)?+v:1;
 try{localStorage.setItem(AKEY_RATE,RATE);}catch(e){}
 renderA11yPanel(); announce('朗读语速 '+RATE+' 倍'); if(TTS)ttsReadNow();
}
function toggleAuto(){ TTSAUTO=TTSAUTO?0:1; renderA11yPanel();
 announce('自动跟屏朗读'+(TTSAUTO?'已开':'已关')); }

/* ---------- 设置面板：四个卡片页，一屏只给一组；可关、可滚、可 Esc ---------- */
let PANEL_TAB='sound';
const PANEL_IDS=['modePanel','diffPanel','skinPanel','a11yPanel'];
function closePanels(){ PANEL_IDS.forEach(id=>{const o=$('#'+id);if(o)o.hidden=true;}); }
function anyPanelOpen(){ return PANEL_IDS.some(id=>{const o=$('#'+id);return o&&!o.hidden;}); }
function openPanel(id){
 closePanels(); const p=$('#'+id); if(p)p.hidden=false;
 if(id==='a11yPanel')renderA11yPanel();
 if(id==='modePanel')renderModePanel();
 if(id==='diffPanel')renderDiffPanel();
 if(id==='skinPanel')renderSkinPanel();
}
function togglePanel(id){ const p=$('#'+id); if(p&&!p.hidden)closePanels(); else openPanel(id); }
function panelHead(title){
 return `<div class="pnl-h"><b>${title}</b>
  <button data-act="panel_close" aria-label="关闭设置面板" title="关闭（也可按 Esc 或点面板外）">✕ 关闭</button></div>`;
}
function openA11yPanel(){ openPanel('a11yPanel'); }

/* 四张卡：声音 / 朗读 / 视觉 / 语音。每卡最多 6 个按钮，不再一次铺 20 个 */
function renderA11yPanel(){
 const p=$('#a11yPanel'); if(!p)return;
 const b=(act,on,label,extra)=>`<button class="${on?'on':''}" data-act="${act}" ${extra||''}>${label}</button>`;
 const tabs=[['sound','声音','♫'],['read','朗读','🔊'],['view','视觉','◑'],['asr','语音','🎙']];
 const _cur=tabs.find(t=>t[0]===PANEL_TAB)||tabs[0];
 const _tabbtns=tabs.map(([k,l,ic])=>
   `<button role="tab" aria-selected="${PANEL_TAB===k}" class="${PANEL_TAB===k?'on':''}"
     data-act="panel_tab" data-v="${k}">${ic} ${l}</button>`).join('');
 /* 换卡行默认隐藏：不把四张卡的切换按钮摊在用户脸上 */
 const tabbar=`<div class="pnl-tabwrap"><button class="pnl-tabtoggle" data-act="panel_tabs"
   aria-expanded="${PANEL_TABS?'true':'false'}">${PANEL_TABS?'▴ 收起换卡':'⋯ 换卡 · 当前 '+_cur[1]}</button>
   ${PANEL_TABS?`<div class="pnl-tabs" role="tablist" aria-label="设置分类">${_tabbtns}</div>`:''}</div>`;
 let body='';
 if(PANEL_TAB==='sound'){
  body=`<div class="grp"><b>两路背景 · 一路音效</b>
   <div class="actl">
    ${b('bgm',BGM>0,'♫ 背景 / 场景音 · '+['关','随场景','＋琴'][BGM],'title="关 → 随场景自动换音景 → 音景＋琴音"')}
    ${b('sfx',SFX>0,'♪ 点选音效 · '+(SFX?'开':'关'),'title="点击拨弦，独立于背景音"')}
   </div>
   <div class="asrstate">场景音默认<b>跟着天气自动换声</b>：秋雨落雨、拂晓与芦荡有<b>鸟鸣</b>、落雪／辕门听风、书楼偶有翻页、秦淮夜虫。点选项另有轻拨弦、答对上行／答错下行。与朗读、语音互不串扰。</div>
   <div class="wxgrp"><b>◈ 天气音可选 · 随进度解锁</b>
    <div class="wxlist">${WXLIST.map(x=>{
      const u=wxUnlocked(x), on=(WXPICK||'auto')===x[0];
      return `<button class="${on?'on':''} ${u?'':'lock'}" data-act="wx_set" data-v="${x[0]}"
        aria-label="${u?'天气音 ':'🔒 通关第 '+x[3]+' 关解锁 '}${x[1]}">${u?'':'🔒 '}${esc(x[1])}${u?'':' <em>'+x[3]+'关</em>'}</button>`;
     }).join('')}</div>
    <div class="asrstate">已解锁 <b>${WXLIST.filter(wxUnlocked).length}/${WXLIST.length}</b> 种。<b>自动跟随同样按进度开放</b>：未解锁的场景（拂晓鸟鸣 2 关、辕门朔风 4 关、秦淮夜虫 6 关、落雪风雪 8 关、临安夜雨 12 关）先回退到秋雨音景。锁住的点下去只播报条件；手动选中的音景会覆盖自动跟随，header 显示它的名字。全部实时合成、无音频文件。</div>
   </div></div>
   <div class="grp"><b>四路开关互不串扰</b>
   <div class="actl">
    ${b('tts',TTS>0,'🔊 朗读 · '+(TTS?'开':'关'))}
    ${b('asr',ASR>0,'🎙 语音 · '+(ASR?'开':'关'))}
   </div><div class="asrstate">朗读、语音每次打开都默认关闭且不记住；背景音、音效、高对比会记住。</div></div>`;
 }else if(PANEL_TAB==='read'){
  body=`<div class="grp"><b>朗读控制</b>
   <div class="actl">
    ${b('tts',TTS>0,'🔊 朗读 · '+(TTS?'开':'关'))}
    ${b('tts_read',0,'🔁 重读本屏')}
    ${b('tts_pause',0,'⏸ 暂停')}
    ${b('tts_stop',0,'⏹ 停止')}
    ${b('tts_auto',TTSAUTO>0,'自动跟屏 · '+(TTSAUTO?'开':'关'))}
    ${b('tts_resume',0,'▶ 继续')}
   </div></div>
   <div class="grp"><b>语速</b><div class="actl three">
    ${b('rate_set',RATE===0.8,'0.8 慢','data-v="0.8"')}
    ${b('rate_set',RATE===1,'1.0 中','data-v="1"')}
    ${b('rate_set',RATE===1.2,'1.2 快','data-v="1.2"')}
   </div><div class="asrstate"><code>R</code> 重读、<code>Esc</code> 停止朗读（面板开着时先关面板）。</div></div>
   <div class="grp"><b>◈ 人声表演</b><div class="actl">
    ${b('perf_set',PERFORM>0,'分句扮演 · '+(PERFORM?'开':'关'))}
    ${b('vp_demo',0,'▶ 试听当前角色')}
   </div><div class="asrstate">开启后不再整屏平读：按句切开，<b>引号内台词用当前角色声线，叙述用旁白声线</b>；骆寒低沉、沈放清亮、朱妍明丽等靠 <code>pitch / rate</code> 区分。<b>这是声线区分，不是真人表演</b>，且依赖系统是否装了中文语音。</div></div>
   <div class="grp"><b>📦 语音包（真表演）</b><div class="actl">
    ${b('vp_import',0,'导入 JSON 语音包')}
    ${b('vp_clear',VOICE_PACK?1:0,'移除')}
   </div>
   <input type="file" id="vpFile" accept=".json,application/json" hidden aria-label="选择语音包 JSON 文件">
   <div class="asrstate">${VOICE_PACK?'<b>已导入「'+esc(VOICE_PACK.name||'未命名')+'」· '+Object.keys(VOICE_PACK.clips).length+' 段</b>；命中当前幕的 clip 会直接播真人音频，未命中回退系统声线。':'当前无语音包。'}<br>
    格式：<code>{"name":"...","clips":{"A:n1":"data:audio/mpeg;base64,..."}}</code>，键用 <code>关卡:幕</code> 或 <code>cast|角色ID</code>。导入仅保存在本次会话，<b>不写进单文件 HTML</b>——音频 base64 会让文件膨胀，且真人录音需要授权。云端 TTS / wasm 引擎不做：前者要联网与密钥，后者体积几十 MB，都破坏离线单文件。</div></div>`;
 }else if(PANEL_TAB==='view'){
  body=`<div class="grp"><b>视觉与键盘</b><div class="actl">
    ${b('a11y_toggle',HC>0,'◑ 高对比 · '+(HC?'开':'关'),'data-v="hc"')}
    ${b('a11y_toggle',BIG>0,'🔍 大字号 · '+(BIG?'开':'关'),'data-v="big"')}
    ${b('a11y_toggle',REDUCE>0,'🍃 减少动效 · '+(REDUCE?'开':'关'),'data-v="reduce"')}
    ${b('avg_set',AVGON>0,'◈ AVG 画面 · '+(AVGON?'开':'关'))}
    ${b('breathe_set',BREATHE>0,'◈ 角色呼吸 · '+(BREATHE?'开':'关'))}
    ${b('a11y_help',0,'⌨ 键盘说明')}
    ${b('cat_mood',CATMOOD_ON>0,'◈ 情绪反馈 · '+(CATMOOD_ON?'开':'关'))}
   </div>
   <div class="grp"><b>气泡与立绘</b><div class="actl three">
    ${[0,1,2].map(i=>b('bubble_set',BUB===i,['◌ 清透','◐ 均衡','● 厚实'][i],'data-v="'+i+'"')).join('')}
    ${b('pose_set',POSE===0,'◧ 半身 · 下半在气泡里','data-v="0"')}
    ${b('pose_set',POSE===1,'▣ 全身','data-v="1"')}
   </div>
   <div class="bubrange"><label for="bubR">◐ 自行调透明度　<b id="bubPct">40%</b></label>
    <input type="range" id="bubR" min="10" max="90" step="1" value="${Math.round(BUBF*100)}"
      data-act="bubble_range" aria-label="气泡透明度百分比">
    <div class="rangelegend"><span>更透 · 看得见背景</span><span>更实 · 字更稳</span></div>
   </div>
   <div class="actl"><button data-act="sprite_reset">↺ 立绘复位</button>
    ${b('vib_set',VIB>0,'◈ 震动 · '+(VIB?'开':'关'))}
    ${b('layout_set',LAYOUT>0,'✥ 气泡自定义 · '+(LAYOUT?'开':'关'))}
   </div><div class="asrstate">点立绘／拖动起止会短震（可关）。开「气泡自定义」后每个文字气泡右上角出现 ✥：拖它摆位、＋/－ 调宽、↕ 调高；同一时刻只能操作一个，其余自动让位且矩形不重叠；上下不限，左右不会超出屏幕。</div>
   <div class="asrstate">气泡横向扁平、半透明能看见背景与立绘；三档是快捷值，滑杆可连续调到 10%–90%，文字始终用不透明墨色＋浅色描边保证读得清。立绘可用手指拖动、双指缩放，拖动时有轻微起伏动画；点「⤢ 看大图」进全屏查看器，同样可双指缩放与拖动。</div></div>
   <div class="grp"><b>◈ 天气层 · 一套雨</b><div class="actl three">
    ${[['art','◈ 素材优先（默认）'],['css','◇ CSS 兜底'],['both','◈◈ 双份叠加']].map(x=>b('fx_set',FXMODE===x[0],x[1],'data-v="'+x[0]+'"')).join('')}
   </div><div class="asrstate">早期雨是 <b>CSS 两层斜线</b>（104° 深蓝 + 100° 亮白，各跑各的速度），后来补了厚涂雨滴／水花素材层，两套叠在一起就成了「两种形态同时表演」。现在<b>默认素材优先</b>：CSS 斜线、水洼、SVG 鸟全部退场，只留素材层；<b>CSS 兜底</b>只在素材未加载时用；<b>双份叠加</b>保留旧效果供对比。雪、飞鸟、灯火同理，同一时刻只跑一套。设置会记住。</div></div>
   <div class="asrstate">AVG 画面把文字与选项叠进场景气泡，并播放当前天气动画（雨／雪／晨光／飞鸟／灯火）。<b>角色呼吸</b>让分层角色缓慢起伏、不再是完全静态贴图；真正的胸腔／耳朵／尾巴分层呼吸还要等生图。<code>减少动效</code> 与 <code>高对比</code> 会停掉它。</div></div>
   <div class="grp"><b>演出门槛</b><div class="actl">
    ${b('perf_gate',PERF_GATE>0,PERF_GATE?'◈ 仅完整演出（筹备中锁住）':'◈ 基础优先（默认）')}
   </div><div class="asrstate">当前 <b>${D.meta.levels.filter(l=>perfReady(l.id)).length}/${D.meta.levels.length}</b> 关有完整演出。基础优先：筹备中的关卡照常可玩，卡面标「演出筹备中 · 敬请期待」；仅完整演出：这些关卡真锁住，点开给「敬请期待」页并列出还缺哪几类、第几批补。</div></div>
   <div class="grp"><b>界面皮肤</b><div class="actl skin4">
    ${SKINS.map(([k,n])=>b('skin_set',SKIN===k,n,'data-v="'+k+'"')).join('')}
   </div><div class="asrstate">只改观感，不动关卡与无障碍。header 的「◐ 皮肤」也可切。</div></div>`;
 }else{
  body=`<div class="grp"><b>🎙 语音控制</b><div class="actl">
    ${b('asr',ASR>0,'语音 · '+(ASR?'开':'关'))}
    ${b('a11y_help',0,'⌨ 键盘说明')}
   </div><div id="asrState" class="asrstate">${ASR_MSG||(SR_CTOR?'语音控制默认关闭；点此开启并授权麦克风。':'<b>当前浏览器不支持语音识别</b>　键盘与点按完全可用，所有游戏不依赖语音。')}</div></div>
   <div class="grp"><b>可以说</b><ol class="cmdlist">
    <li>开始 / 出发</li><li>下一题 / 继续</li><li>选一 ～ 选四</li>
    <li>回大厅 / 返回</li><li>朗读开 / 朗读关 / 重读</li>
    <li>背景音 / 音效 / 高对比 / 大字 / 帮助</li></ol>
   <div class="asrstate">需 Chrome / Edge 并授权麦克风；本地 <code>file://</code> 若受限，用本地 http 服务打开即可。不支持时键盘 1–4 选项、N 下一题、H 大厅、R 重读照常可用。</div></div>`;
 }
 const quick=`<div class="setquick">
   <details class="setfold"><summary>模式 · ${modeInfo().icon} ${modeInfo().name}（点开展开）</summary>
    <div class="setgrid">${D.meta.modeOrder.map(k=>{
      const m=D.meta.modes[k];
      return `<button class="${MODE===k?'on':''}" data-act="mode_set" data-v="${k}">${m.icon} ${m.name}${MODE===k?'　✓':''}</button>`;
    }).join('')}</div></details>
   <details class="setfold"><summary>难度 · ${diffInfo().icon} ${diffInfo().name}（点开展开）</summary>
    <div class="setgrid">${D.meta.diffOrder.map(k=>{
      const d=D.meta.diffs[k];
      return `<button class="${DIFF===k?'on':''}" data-act="diff_set" data-v="${k}">${d.icon} ${d.name}${DIFF===k?'　✓':''}</button>`;
    }).join('')}</div></details>
   <div class="setrow">
    ${b('sfx',SFX>0,'♪ 音效 · '+(SFX?'开':'关'))}
    ${b('tts',TTS>0,'🔊 朗读 · '+(TTS?'开':'关'))}
    ${b('asr',ASR>0,'🎙 语音 · '+(ASR?'开':'关'))}
   </div>
   <details class="setfold"><summary>皮肤 · ${(SKINS.find(s=>s[0]===SKIN)||SKINS[0])[1]}（点开展开）</summary>
    <div class="setgrid">${SKINS.map(([k,n])=>b('skin_set',SKIN===k,n,'data-v="'+k+'"')).join('')}</div></details>
  </div>`;
 p.innerHTML=`<div class="settop">
   <div><b>⚙ 设置</b><span>${modeInfo().icon} ${modeInfo().name} · ${diffInfo().icon} ${diffInfo().name}　｜　点开折叠项可展开，内容长了上下拖动</span></div>
   <button class="setclose" data-act="panel_close" aria-label="退出设置，回到游戏">✕ 退出</button>
  </div>
  <div class="setscroll" id="setScroll" role="dialog" aria-label="设置内容，可上下拖动">
   ${quick}${tabbar}<div class="pnl-body" role="tabpanel">${body}</div>
   <div class="setnote">关闭方式：右上「✕ 退出」、底部大按钮、按 Esc，三种都回到游戏。朗读与语音默认关闭、不记住设置。</div>
  </div>
  <div class="setfoot"><button class="setclose big" data-act="panel_close">✕ 关闭设置 · 回到游戏</button></div>`;
}


/* ---------- AVG 演出层：文字与选项都叠在画面上 ----------
   只移动 DOM 一次，不改关卡数据；所有事件仍走 body 委托，朗读 innerText 仍能读到全文。 */
const AKEY_AVG='beixue_avg_v1';
let AVGON=1;
try{ const v=localStorage.getItem(AKEY_AVG); if(v!==null)AVGON=(+v===1)?1:0; }catch(e){}
function setAVG(v){
 AVGON=v?1:0; try{localStorage.setItem(AKEY_AVG,AVGON);}catch(e){}
 render(); announce('AVG 画面演出已'+(AVGON?'开启':'关闭'));
}
function applyAVG(){
 const app=$('#app'); if(!app)return;
 if(!AVGON||!D.meta.levels.some(l=>l.id===TAB))return;
 const st=app.querySelector('.stage'); if(!st)return;
 st.classList.add('stagefull');           /* 背景独立铺满整个视口，不再被内容区裁成一块 */
 const wx=sceneWeather(stageFor(TAB).bg);
 const frame=document.createElement('div');
 frame.className='avgframe fx-'+wx.fx;
 frame.setAttribute('data-weather',wx.fx);
 st.parentNode.insertBefore(frame,st);
 frame.appendChild(st);
 const sibs=[...app.children].filter(el=>el!==frame);
 const MERGE=['prog','inkdiv','disclaim','hint','music-note','hallmore','btnrow',
  'bar','note','guide','hintbox','clue','revealbox','pick','walk','trail',
  'scene','review','roamnote','lockcard','animstat'];
 let first=true, last=null, pending=[];
 sibs.forEach(el=>{
  if(el.id==='dressMount')return;
  /* 所有说明/进度/幕文/按钮行并进同一个气泡，屏幕上只留一个对话框 */
  const merge=MERGE.some(c=>el.classList.contains(c))||
     (!el.textContent.trim()&&!el.querySelector('button,img,[data-bg],[data-art]'));
  if(merge){ pending.push(el); return; }
  el.classList.add('avgblock');
  if(first){el.classList.add('avgbubble');first=false;}
  /* 气泡之前攒下的碎块前置进气泡 */
  pending.forEach(x=>el.prepend(x)); pending=[];
  frame.appendChild(el); last=el;
 });
 /* 整屏都是说明/幕文时，自己造一个气泡把碎块收进去，避免裸文字 */
 if(first&&pending.length){
  const box=document.createElement('div');
  box.className='avgblock avgbubble';
  pending.forEach(x=>box.appendChild(x)); pending=[];
  frame.appendChild(box); last=box; first=false;
 }
 /* 气泡之后攒下的碎块收进最后一个气泡，避免裸条 */
 pending.forEach(x=>(last||frame).appendChild(x));
 frame.setAttribute('aria-label','场景画面：'+wx.label+'，'+FX_LABEL[wx.fx]+'；下方为对话与选项');
}

/* ---------- 渲染后：装饰、读屏标注、自动朗读 ---------- */
function decorate(){
 applyA11y();
 document.querySelectorAll('[data-art]').forEach(el=>{
  const k=origCast(el.dataset.art); if(ART[k])el.style.backgroundImage="url('"+ART[k]+"')";
 });
 document.querySelectorAll('[data-bg]').forEach(el=>{
  const k=el.dataset.bg; if(ART[k])el.style.backgroundImage="url('"+ART[k]+"')";
 });
 document.querySelectorAll('.fx-art[data-fx]').forEach(el=>{
  const k=el.dataset.fx; if(ART[k])el.style.backgroundImage="url('"+ART[k]+"')";
 });
 document.querySelectorAll('#app button,nav button,header button').forEach(btn=>{
  if(!btn.getAttribute('aria-label')){
   const t=(btn.innerText||btn.textContent||'').trim().replace(/\s+/g,' ').slice(0,64);
   if(t)btn.setAttribute('aria-label',t);
  }
 });
 document.querySelectorAll('.artbanner,.endart').forEach(el=>el.setAttribute('aria-hidden','true'));
}
function afterRender(){
 applyCatAv();
 for(const _l of D.meta.levels){
  const _k=_l.id; let _st=null;
  try{ _st=(['A','B','C','D','E','F'].includes(_k)||QKEYS.includes(_k))?S[_k].stage:null; }catch(e){}
  if(_st==='end'&&!SEEN_END.has(_k)){ SEEN_END.add(_k); setMood('cos_zhu_resolve',2600); }
 }
 decorate();
 const lv=D.meta.levels.find(l=>l.id===TAB);
 announce(TAB==='hall'?('游戏大厅，'+D.meta.levels.length+' 关，累计星 '+totalStars()+' / '+maxStars()):
          TAB==='arch'?'档案页':('当前关卡：'+(lv?lv.t:TAB)));
 if(TTS&&TTSAUTO&&TTS_CAP){ clearTimeout(ttsTimer); ttsTimer=setTimeout(()=>speak(ttsText(),false,currentCast()),180); }
 if(TAB==='arch'&&ARCH==='cat')renderDress();
}
/* ---------- 键盘快捷键（不依赖语音） ---------- */
document.addEventListener('keydown',e=>{
 if(e.target&&e.target.matches&&e.target.matches('input,textarea,[contenteditable="true"]'))return;
 const k=String(e.key||'').toLowerCase();
 if(k==='escape'){ const _pk=$('#catPeek'); if(_pk&&!_pk.hidden){closeCatPeek();announce('已关闭角色预览');return;}
  if(anyPanelOpen()){closePanels();announce('已关闭设置面板');return;} ttsStop();announce('已停止朗读');return; }
 if(k==='r'){ttsReadNow();e.preventDefault();return;}
 if(k==='h'){setTab('hall');e.preventDefault();return;}
 if(k==='n'){
  if(clickFirst(['#app [data-act$="_next"]','#app [data-act="A_next"]','#app [data-act="B_next"]','#app .btn:not(.ghost)']))e.preventDefault();
  return;
 }
 if(/^[1-4]$/.test(k)){ clickOption(+k); e.preventDefault(); }
});
/* 焦点跟随朗读：朗读开启时，Tab 到哪读到哪 */
document.addEventListener('focusin',e=>{
 if(!TTS||!TTS_CAP||!e.target)return;
 const el=e.target; if(!el.matches||!el.matches('button,a[href],[tabindex]'))return;
 const label=(el.getAttribute('aria-label')||el.textContent||'').trim().replace(/\s+/g,' ').slice(0,90);
 if(label){ clearTimeout(ttsTimer); ttsTimer=setTimeout(()=>speak(label,true),90); }
});

/* ---------- dispatch ---------- */
document.addEventListener('change',e=>{
 if(e.target&&e.target.id==='vpFile'&&e.target.files&&e.target.files[0]){
  importVoicePack(e.target.files[0]); e.target.value='';
 }
});
document.body.addEventListener('click',e=>{
 /* 点面板外一律收起；点面板开关按钮不在这里关，交给各自分支 toggle */
 const _inPanel=e.target.closest('.modepanel');
 const _isPanelBtn=e.target.closest('[data-act$="_panel"]');
 if(!_inPanel&&!_isPanelBtn&&anyPanelOpen())closePanels();
 const t=e.target.closest('[data-act]'); if(!t)return;
 const a=t.dataset.act, v=t.dataset.v;
 /* R17：立绘缩放按钮兜底（多指不支持或不想捏合时也能调） */
 if(a==='spr_zoom'){
  SPR.s=Math.max(.6,Math.min(2.2,SPR.s*(+v||1)));applySpr();saveSpr();vib(8);
  announce('立绘缩放 '+Math.round(SPR.s*100)+'%');return;
 }
 /* 点选反馈：按下即给一层朱砂描边，180ms 后收；读屏同时播报 */
 if(t.matches('.opt,.eopt,.act,.m4,.mode,.d4,.d4i,.lvl,.btn,.sk-i,.pnl-tabs button')){
  t.classList.add('pressed'); setTimeout(()=>t.classList.remove('pressed'),190);
  const rp=document.createElement('i'); rp.className='rippleart global';
  rp.style.left=Math.max(0,(e.clientX||innerWidth/2)-30)+'px';
  rp.style.top=Math.max(0,(e.clientY||innerHeight/2)-30)+'px';
  document.body.appendChild(rp); setTimeout(()=>rp.remove(),230);
 }
 if(a==='land'){ toggleLand(); return; }
 if(a==='land_exit'){ exitLand(); return; }
 if(a==='land_rot'){ toggleRot(); return; }
 if(a==='land_dismiss'){ LAND_DISMISS=1; renderLandTip(); return; }
 if(a==='panel_close'){ closePanels(); announce('已关闭设置面板'); return; }
 if(a==='panel_tab'){ PANEL_TAB=v; PANEL_TABS=0; renderA11yPanel(); return; }
 if(a==='panel_tabs'){ PANEL_TABS=PANEL_TABS?0:1; renderA11yPanel(); return; }
 if(a==='perf_set'){ setPerform(PERFORM?0:1); renderA11yPanel(); return; }
 if(a==='vp_import'){ const f=$('#vpFile'); if(f)f.click(); return; }
 if(a==='vp_clear'){ VOICE_PACK=null; stopVoicePack(); renderA11yPanel(); announce('已移除语音包，恢复系统声线'); return; }
 if(a==='vp_demo'){ demoVoice(); return; }
 if(a==='avg_set'){ setAVG(AVGON?0:1); renderA11yPanel(); return; }
 /* 情绪反馈：单选答错瞬间换沈放的错愕脸 */
 if(CATMOOD_ON&&/_ans$/.test(a)&&/^\d+$/.test(String(v||''))){
  const _k=a.slice(0,-4); let _ok=null;
  try{
   if(QKEYS.includes(_k)){ const _q=qList(_k)[S[_k].i]; if(_q&&qType(_q)==='single')_ok=(+v===_q.a); }
   else if(_k==='D'){ const _q=dQuiz()[S.D.i]; if(_q)_ok=(+v===_q.a); }
   else if(_k==='F'){ const _q=D.F.cases[S.F.i]; if(_q)_ok=(+v===_q.a); }
  }catch(e){}
  if(_ok===false){ setMood('cos_shen_argue',2600); fxNo(); setTimeout(()=>stagePulse('no'),20); }
  else if(_ok===true){ fxOk(); setTimeout(()=>stagePulse('ok'),20); }
 }
 if(a==='cat_mood'){ CATMOOD_ON=!CATMOOD_ON; if(!CATMOOD_ON){MOOD.key='';clearTimeout(MOOD.t);} render();
  announce('情绪反馈已'+(CATMOOD_ON?'开启':'关闭')); return; }
 if(a==='dress_bg'){ const bi=bgIdx(v);
  if(!bgUnlocked(bi)){announce('🔒 通关第 '+bgNeed(bi)+' 关解锁该场景');return;}
  DRESS.bg=v; renderDress(); announce('背景已换为'+(BGLIST[bi]||['',''])[1]); return; }
 if(a==='dress_who'){ const ci=CAST.findIndex(x=>x[0]===v);
  if(!castUnlocked(ci,CAST.length)){announce('🔒 通关第 '+castNeed(ci,CAST.length)+' 关解锁该角色');return;}
  DRESS.who=v; renderDress(); announce('角色已换为'+(CAST[ci]||['',''])[1]); return; }
 if(a==='skin_panel'){ togglePanel('skinPanel'); return; }
 if(a==='skin_set'){ setSkin(v); if(!$('#a11yPanel').hidden)renderA11yPanel(); else closePanels(); return; }
 if(a==='mode_panel'){ togglePanel('modePanel'); return; }
 if(a==='mode_set'){ setMode(v); if(!$('#a11yPanel').hidden)renderA11yPanel(); else closePanels(); return; }
 if(a==='diff_panel'){ togglePanel('diffPanel'); return; }
 if(a==='diff_set'){ setDiff(v); if(!$('#a11yPanel').hidden)renderA11yPanel(); else closePanels(); return; }
 if(a==='cat_fix'){
  const ci=CATCOST.findIndex(x=>x[0]===v);
  if(v!=='auto'&&!castUnlocked(ci,CATCOST.length)){
   announce('🔒 '+(CATCOST[ci]||['','这位角色'])[1]+' 尚未解锁，通关第 '+castNeed(ci,CATCOST.length)+' 关开放'); return; }
  CATFIX=(v==='auto')?'':v; render();
  const _hc=document.querySelector('.hh-cut'); if(_hc){_hc.classList.add('swap');setTimeout(()=>_hc.classList.remove('swap'),640);}
  const _nm=CATFIX?CATCOST.find(x=>x[0]===CATFIX)[1]:'跟随场景';
  announce('大厅主视觉与引导员已换为 '+_nm+'，不再弹窗'); return; }
 if(a==='hall_bg'){
  const bi=bgIdx(v);
  if(!bgUnlocked(bi)){ announce('🔒 场景「'+(BGLIST[bi]||['',''])[1]+'」通关第 '+bgNeed(bi)+' 关解锁'); return; }
  HH_BG=v; try{localStorage.setItem(HBGKEY,v);}catch(e){}
  render();
  const _bg=document.querySelector('.hh-bg'); if(_bg){_bg.classList.add('swapbg');setTimeout(()=>_bg.classList.remove('swapbg'),640);}
  announce('预览场景已换为 '+(BGLIST[bi]||['',''])[1]); return; }
 if(a==='nav_toggle'){
  const n=$('#nav'), t2=$('#nav .navtoggle');
  n.classList.toggle('open');
  const op=n.classList.contains('open');
  if(t2){t2.setAttribute('aria-expanded',op?'true':'false');t2.textContent=op?'▴ 收起':'▦ 页签';}
  announce(op?'全部页签已展开':'页签已收起'); return;
 }
 if(a==='bubble_set'){ BUB=[0,1,2].includes(+v)?+v:1; BUBF=[.22,.40,.62][BUB];
  try{localStorage.setItem('beixue_bub_v1',BUB);localStorage.setItem('beixue_bubf_v1',BUBF);}catch(e){}
  applyA11y(); renderA11yPanel(); announce('气泡已设为'+['清透','均衡','厚实'][BUB]); return; }
 if(a==='sprite_reset'){ SPR={x:0,y:0,s:1}; saveSpr(); applySpr();
  announce('立绘已复位'); renderA11yPanel(); return; }
 if(a==='zoom_hall'){ openHallFull(); return; }
 if(a==='hall_reset'){ resetHallSpr(); announce('立绘已回到场景中央'); vib(12); return; }
 if(a==='zoom_sprite'){ openStageFull(); return; }
 if(a==='viewer_close'){ closeViewer(); return; }
 if(a==='viewer_in'){ VSTATE.mode==='comp'?vZoomComp(1.2,'bg'):vZoom(1.2); return; }
 if(a==='viewer_out'){ VSTATE.mode==='comp'?vZoomComp(1/1.2,'bg'):vZoom(1/1.2); return; }
 if(a==='viewer_reset'){ VSTATE.mode==='comp'?vResetComp():vReset(); return; }
 if(a==='v_picker_close'){ vPicker.hidden=true; return; }
 if(a==='v_pick_bg'){
  const bi=bgIdx(v); if(!bgUnlocked(bi)){announce('🔒 通关第 '+bgNeed(bi)+' 关解锁');return;}
  VSTATE.bg=v;VSTATE.dirty=1;vApplyLayers();vPicker.hidden=true;vib(12);
  announce('全屏场景已换为 '+(BGLIST[bi]||['',''])[1]); return; }
 if(a==='v_pick_cast'){
  const ci=CAST.findIndex(x=>x[0]===v); if(ci<0)return;
  if(!(ci>=CATCOST.length||castUnlocked(ci,CAST.length))){
   announce('🔒 通关第 '+castNeed(ci,CAST.length)+' 关解锁');return;}
  VSTATE.cast=v;VSTATE.dirty=1;vApplyLayers();vPicker.hidden=true;vib(12);
  announce('全屏立绘已换为 '+(CAST[ci]||['',''])[1]); return; }
 if(a==='pose_set'){ POSE=(+v===1)?1:0;
  try{localStorage.setItem('beixue_pose_v1',POSE);}catch(e){}
  applyA11y(); renderA11yPanel(); announce(POSE?'立绘为全身':'立绘为半身，下半在气泡里'); return; }
 if(a==='a11y_panel'){ togglePanel('a11yPanel'); PANEL_TABS=0; renderA11yPanel(); return; }
 if(a==='settings'){ openPanel('a11yPanel'); PANEL_TABS=0; renderA11yPanel();
   setTimeout(()=>{const s=$('#setScroll');if(s){s.scrollTop=0;}},30);
   announce('已打开设置界面，右上或底部可退出'); return; }
 if(a==='hmore'){
  const m=$('#hmore'); if(!m)return;
  m.hidden=!m.hidden;
  const btn=$('#moreBtn');
  btn.setAttribute('aria-expanded',m.hidden?'false':'true');
  btn.textContent=m.hidden?'⋯ 更多':'⋯ 收起';
  announce(m.hidden?'次要开关已收起':'次要开关已展开');
  return;
 }
 if(a==='a11y_help'){ announce('键盘：1 到 4 选择选项，N 下一题，H 回大厅，R 重读本屏，Esc 停止朗读，Tab 顺次聚焦。'); return; }
 if(a==='bgm'){ cycleBGM(); if(!$('#a11yPanel').hidden)renderA11yPanel(); return; }
 if(a==='sfx'){ toggleSFX(); if(!$('#a11yPanel').hidden)renderA11yPanel(); return; }
 if(a==='wx_set'){
  const it=WXLIST.find(x=>x[0]===v); if(!it)return;
  if(v!=='auto'&&!wxUnlocked(it)){announce('🔒 '+it[1]+' 通关第 '+it[3]+' 关解锁');return;}
  WXPICK=v; try{localStorage.setItem(WXKEY,v);}catch(e){}
  if(BGM===0)setBGM(1); else retuneScene(audioBg());
  syncHctl(); if(!$('#a11yPanel').hidden)renderA11yPanel();
  announce('天气音已设为 '+(v==='auto'?'自动跟随场景':it[1])); vib(10); return; }
 if(a==='vib_set'){ VIB=VIB?0:1; try{localStorage.setItem(VIBKEY,String(VIB));}catch(e){}
  if(VIB)vib(16); announce('震动反馈已'+(VIB?'开启':'关闭')); renderA11yPanel(); return; }
 if(a==='layout_set'){ LAYOUT=LAYOUT?0:1; saveLayout(); applyBubbleLayout();
  announce('气泡自定义已'+(LAYOUT?'开启：拖 ✥ 摆位，＋/－ 调宽，↕ 调高，组件互斥':'关闭：恢复默认排版'));
  renderA11yPanel(); return; }
 if(a==='bub_w_dec'||a==='bub_w_inc'||a==='bub_h'||a==='bub_reset'){
  const box=t.closest('.avgblock'); if(!box)return;
  const key=TAB+':'+box.dataset.bi, s=BUBLAY[key]||{x:0,y:0,w:0,h:0};
  if(a==='bub_reset'){ delete BUBLAY[key]; }
  else if(a==='bub_h'){ s.h=[0,Math.round(innerHeight*.30),Math.round(innerHeight*.50),Math.round(innerHeight*.70)][((([0,Math.round(innerHeight*.30),Math.round(innerHeight*.50),Math.round(innerHeight*.70)].indexOf(s.h)+1)%4))]; BUBLAY[key]=s; }
  else { const base=s.w||Math.min(innerWidth-16,box.offsetWidth||320);
    s.w=Math.max(180,Math.min(innerWidth-16,base+(a==='bub_w_inc'?28:-28))); BUBLAY[key]=s; }
  saveLayout(); applyBubbleLayout(); vib(8); return; }
 if(a==='tts'){ toggleTTS(); return; }
 if(a==='asr'){ toggleASR(); return; }
 if(a==='tts_read'){ ttsReadNow(); return; }
 if(a==='tts_pause'){ try{window.speechSynthesis&&window.speechSynthesis.pause();}catch(e){} announce('朗读已暂停'); return; }
 if(a==='tts_resume'){ try{window.speechSynthesis&&window.speechSynthesis.resume();}catch(e){} announce('朗读继续'); return; }
 if(a==='tts_stop'){ ttsStop(); announce('已停止朗读'); return; }
 if(a==='tts_auto'){ toggleAuto(); return; }
 if(a==='rate_set'){ setRate(v); return; }
 if(a==='a11y_toggle'){ toggleA11y(v); return; }
 if(t.matches('.opt,.act,.btn,.m4,.mode,.eopt,.lvl,.d4'))tickSound();
 if(a==='go'){
  if(D.meta.levels.some(l=>l.id===v)&&perfLocked(v)){openComing(v);return;}
  setTab(v);return;
 }
 if(a==='fx_set'){ setFxMode(v); renderA11yPanel(); render(); return; }
 if(a==='breathe_set'){ setBreathe(BREATHE?0:1); renderA11yPanel(); return; }
 if(a==='perf_gate'){ setPerfGate(PERF_GATE?0:1); renderA11yPanel(); return; }
 if(a==='coming_base'){ setPerfGate(0); setTab(COMING||'hall'); return; }
 if(a==='coming_back'){ setTab('hall'); return; }
 if(a==='A_mode'){ setMode(v); S.A=A_fresh(); render(); }
 else if(a==='A_start'){ S.A=A_fresh(); render(); }
 else if(a==='A_reset'){A_reset();}
 else if(a==='A_back'){ setTab('hall'); setTimeout(()=>{const e=$('#modeHero');if(e)e.scrollIntoView({behavior:'smooth',block:'center'});},60); }
 else if(a==='A_choose')A_choose(v);
 else if(a==='A_act')A_act(v);
 else if(a==='A_next')A_next();
 else if(a==='A_q')A_q(v);
 else if(a==='A_roam')A_roam(v);
 else if(a==='B_start'){S.B.stage='play';render();}
 else if(a==='B_reset'){S.B={stage:'play',turn:0,silver:'cart',focus:'six',sign:'ok',pact:'ok',known:false,sel:[],log:[],hint:hintLimit(),end:null,pause:null,mistakes:0};render();}
 else if(a==='B_sel')B_sel(v);
 else if(a==='B_run')B_run();
 else if(a==='B_hint')B_hint();
 else if(a==='B_next')B_next();
 else if(a==='D_start'){S.D={stage:'play',i:0,score:0,streak:0,best:0,wrong:[],picked:null,showWhy:false,showHint:false,mistakes:0};render();}
 else if(a==='D_reset'){S.D.stage='intro';render();}
 else if(a==='D_ans')D_ans(+v);
 else if(a==='D_next')D_next();
 else if(a==='D_hint'){S.D.showHint=!S.D.showHint;render();}
 else if(a==='D_jump')D_jump(+v);
 else if(a==='C_start'){S.C={stage:'play',k:0,g:5,b:5,p:5,log:[],end:null,mistakes:0};render();}
 else if(a==='C_reset'){S.C.stage='intro';render();}
 else if(a==='C_opt')C_opt(+v);
 else if(a==='E_start'){S.E={stage:'play',i:0,sc:{},picks:[],end:null};render();}
 else if(a==='E_reset'){S.E.stage='intro';render();}
 else if(a==='E_ans')E_ans(+v);
 else if(a==='E_next')E_next();
 else if(a==='E_back'){S.E.i=Math.max(0,S.E.i-1);S.E.stage='play';render();}
 else if(a==='F_start'){S.F={stage:'play',i:0,right:0,wrong:[],picked:null,showWhy:false,showHint:false,end:null,mistakes:0};render();}
 else if(a==='F_reset'){S.F.stage='intro';render();}
 else if(a==='F_ans')F_ans(+v);
 else if(a==='F_next')F_next();
 else if(a==='F_hint'){S.F.showHint=!S.F.showHint;render();}
 else if(QKEYS.includes(String(a).split('_')[0])){
  const kk=String(a).split('_')[0], op=String(a).slice(kk.length+1);
  if(op==='start'){S[kk]=qFresh();render();}
  else if(op==='reset'){S[kk].stage='intro';render();}
  else if(op==='ans')Q_ans(kk,v);
  else if(op==='next')Q_next(kk);
  else if(op==='hint'){S[kk].showHint=!S[kk].showHint;render();}
  else if(op==='undo')Q_undo(kk);
  else if(op==='clear')Q_clear(kk);
 }
 else if(a==='arch_tab'){ARCH=v;render();}
});

function renderComing(){
 const l=D.meta.levels.find(x=>x.id===COMING)||D.meta.levels[0];
 const miss=perfMissing(l.id), need=D.perf.need[l.id]||[];
 const lis=miss.map(c=>'<li><b>'+esc(c)+'</b>　'+esc(CAT_BATCH[c]||'待排期')+'</li>').join('');
 return `<div class="comingcard">
  <div class="comingseal" aria-hidden="true">◈</div>
  <div class="lab">第 ${esc(l.no)} 关 · ${esc(l.t)}</div>
  <h2>完整演出，敬请期待</h2>
  <p>这一关的动画表演素材还缺 <b>${miss.length}</b> 类，共需 ${need.length} 类。
   基础演出（CSS 天气、静态角色层、呼吸感、系统朗读）已经能跑，但「表演」还没做完，
   所以「仅完整演出」模式下先锁住，不拿半成品冒充完成。</p>
  <div class="cominglist"><b>还缺这些</b><ul>${lis}</ul></div>
  <p class="comingnote">素材已逐项登记在档案「动画素材登记」；后续按批次生图／录语音包，
   补一类就把这一关的对应项点亮，全部补齐才自动解锁。</p>
  <div class="btnrow">
   <button class="btn" data-act="coming_base">切回基础优先 · 用基础演出进入</button>
   <button class="btn ghost" data-act="coming_back">回大厅</button>
  </div></div>`;
}
function render(){
 const app=$('#app');
 document.body.classList.toggle('in-level',D.meta.levels.some(l=>l.id===TAB));
 if(TAB==='hall'){app.innerHTML=renderHall();}
 else if(TAB==='coming'){app.innerHTML=renderComing();}
 else if(TAB==='A'){app.innerHTML=renderA();}
 else if(TAB==='B'){app.innerHTML=renderB();}
 else if(TAB==='D'){app.innerHTML=renderD();}
 else if(TAB==='C'){app.innerHTML=renderC();}
 else if(TAB==='E'){app.innerHTML=renderE();}
 else if(TAB==='F'){app.innerHTML=renderF();}
 else if(QKEYS.includes(TAB)){app.innerHTML=renderQ(TAB);}
 else if(TAB==='arch'){app.innerHTML=renderArchive(); mountRead();}
 if(D.meta.levels.some(l=>l.id===TAB)){
  remember(TAB);
  let _h=app.innerHTML;
  const _re=/<div class="(?:artbanner|endart)"[^>]*><\/div>\s*(?:<div class="artcap">[\s\S]*?<\/div>)?/;
  const _has=_re.test(_h);
  const _st=stageBlock(TAB,_has?0:1);
  app.innerHTML=_has?_h.replace(_re,_st):_st+_h;
 }
 $('#foot').innerHTML='二十四关游戏均为机制化解读，不含小说原文，也不指向盗版全文站。考据题依据公开可核资料与通行版本，异文处并列存疑。<br>'+
  '朗读 / 语音控制默认关闭；场景音、音效、朗读、语音四路开关互不影响。设置面板四张卡片可分页，点面板外／Esc／✕ 都能收起。<br>'+
  '逐字阅读：微信读书《杯雪（全集）》、当当云阅读《杯雪（全二册）》、新世界出版社 2011 年全二册纸质本。';
 afterRender();
 applyAVG();
 applyBubbleLayout();
 if(TAB==='hall')ensureHallVisible();   /* 切回大厅时猫一定在场景框里 */
 if(D.meta.levels.some(l=>l.id===TAB)){
  const _s=stageFor(TAB);
  document.documentElement.style.setProperty('--catav',"url('"+(ART[_s.cast]||ART.cos_base)+"')");
  ensureSpriteVisible();
 }
 if(BGM>0)retuneScene(audioBg());
 if(BGM>0){ const bg=$('#bgmBtn'); if(bg)bg.textContent=bgmLabel(); }
}
function starHTML(n,max){max=max||3;let s='';for(let i=0;i<max;i++)s+=i<n?'★':'<span class="off">★</span>';return s;}
function resultBox(k,stars,note,extra){
 if(isRoam())return `<div class="roamnote"><b>漫游模式 · 不结算</b>　${esc(note)}　不写星、不评级，也不解锁档案。想开资料页，切到新手／普通／挑战再走一遍。</div>`;
 const mis=extra||0;
 let h=`<div class="gradebox"><div class="starbox">${starHTML(stars)}</div>
  <div><b>本关 ${stars} 星</b>　${esc(note)}　·　累计 ★ ${totalStars()}/${maxStars()}　·　${esc(diffNote())}</div>`;
 if(isChallenge())h+=`<div style="margin-top:9px"><span class="grade">挑战评级 <b>${grade(mis)}</b></span>　失误 ${mis} 次（S 零失误／A 1 次／B 2 次／C 3 次以上）　校勘难度零容忍</div>`;
 h+=`</div><div class="unlockline">${esc(unlockNote(k))}${allCleared()?'　·　档案 '+archUnlockedCount()+'/'+archTotal()+' 全部开启':''}</div>`;
 h+=levelTail(k);
 return h;
}

/* ---------- home ---------- */
function modesBlock(){
 return `<div class="modehero" id="modeHero">
  <div class="mh-h"><b>${modeInfo().icon} 选择游戏模式</b><span>二十四关通用 · 随时可改</span></div>
  <div class="mh-lead">同一个故事，四种读法。选一次，二十四关全部跟着变；挑战给评级，漫游不判定。</div>
  <div class="modes4">${D.meta.modeOrder.map(k=>{const m=D.meta.modes[k];
   return `<button class="m4 ${MODE===k?'on':''}" data-act="mode_set" data-v="${k}">
    ${MODE===k?'<span class="chk">✓ 当前</span>':''}
    <div class="top"><span class="ico">${m.icon}</span><b>${m.name}</b>${m.tag?`<span class="tag">${m.tag}</span>`:''}</div>
    <div class="lead">${esc(m.lead)}</div><ul>${m.perks.map(p=>`<li>${esc(p)}</li>`).join('')}</ul></button>`;
  }).join('')}</div>
  <div class="mh-note">${esc(modeInfo().desc)}</div>
 </div>`;
}
function diffsBlock(){
 return `<div class="modehero" id="diffHero" style="border-color:var(--purple)">
  <div class="mh-h"><b>${diffInfo().icon} 选择阅读难度</b><span>二十四关通用 · 与模式互不干扰</span></div>
  <div class="mh-lead">模式管「怎么读」，难度管「考什么、判多严」。第七关起十六关的考据题只有校勘难度才全开。</div>
  <div class="d4">${D.meta.diffOrder.map(k=>{const d=D.meta.diffs[k];
   return `<button class="d4i ${DIFF===k?'on':''}" data-act="diff_set" data-v="${k}">
    ${DIFF===k?'<span class="chk">✓ 当前</span>':''}
    <div class="top"><span class="ico">${d.icon}</span><b>${d.name}</b><span class="tag">${d.key}</span></div>
    <div class="lead">${esc(d.lead)}</div><ul>${d.perks.map(p=>`<li>${esc(p)}</li>`).join('')}</ul></button>`;
  }).join('')}</div>
  <div class="mh-note">${esc(diffInfo().desc)}　当前：${esc(diffNote())}</div>
 </div>`;
}
function sceneBar(){
 if(bgIdx(HH_BG)<0)HH_BG='rain';
 const bi=Math.max(0,bgIdx(HH_BG));
 if(!bgUnlocked(bi))HH_BG='rain';
 return `<div class="scenebar"><div class="sb-scroll">${BGLIST.map(([v,l],i)=>{
  const u=bgUnlocked(i);
  return `<button class="${HH_BG===v?'on':''} ${u?'':'lock'}" data-act="hall_bg" data-v="${v}"
    ${u?'':`aria-label="${l}：通关第 ${bgNeed(i)} 关解锁"`}>${u?l:'🔒 '+l}</button>`;
 }).join('')}</div><span class="sb-hint">场景 ${bgCount()}/11 已解锁</span></div>`;
}
function renderHall(){
 const ts=totalStars(), done=clearedCount(), au=archUnlockedCount(), at=archTotal();
 const _ck=origCast(VCAST_OVER.hall||(CATFIX?fixedKey():avatarKey())), _cm=castMeta(_ck);
 const _bi=Math.max(0,bgIdx(HH_BG)), _bl=(BGLIST[_bi]||['','雨驿雨夜'])[1];
 if(!bgUnlocked(_bi))HH_BG='rain';
 return `<div class="hallhero2">
  <div class="hh-txt">
   <h2>先认人，再进雨驿；二十四关，七卷江湖</h2>
   <p>《杯雪》本来就靠信息差运转：人人只在转述、人人只看见一角、六车石头骗过全场、真动手的人不成名。第一关先照见自己落在哪一类侠气上，再进那一夜的雨。</p>
   <div class="quote">「这世上，必败的仗就不用打了吗？」<br>二十四关都不问你赢没赢，只问你看没看清楚。</div>
   <div class="btnrow"><span class="pill">二十四关 · 七卷</span><span class="pill">档案逐步解锁 · 单文件离线</span></div>
   <div class="sig">哈士喵 · 作者原稿平涂风　｜　${modeInfo().icon} ${modeInfo().name} · ${diffInfo().icon} ${diffInfo().name}</div>
  </div>
  <div class="hh-cat">
   <div class="hh-plate"><b>${esc(_cm[0])}</b><span>${esc(_cm[1])}</span><i>@${esc(_bl)}</i></div>
   ${sceneBar()}
   <div class="hh-preview" role="img" aria-label="当前引导员大图预览：点下方角色卡可换人，上方选场景">
    <div class="hh-bg" data-bg="bg_${HH_BG}"></div>
    <div class="hh-cut" data-hhit data-art="${_ck}"></div>
    <button class="zoombtn hh-zoom" data-act="zoom_hall" aria-label="全屏查看场景与立绘">⤢</button>
    <button class="zoombtn hh-reset" data-act="hall_reset" aria-label="把立绘放回场景中央">↺</button>
   </div>
   <div class="catcredit">作者原稿 · 平涂风格　｜　<a data-act="go" data-v="arch" style="color:var(--purple);cursor:pointer">看角色设定</a></div>
  </div>
 </div>
 ${catBar()}
 <div class="hallquick">
  <button class="btn" data-act="go" data-v="${LAST}">▶ 继续上次 · ${esc((D.meta.levels.find(l=>l.id===LAST)||{}).t||'你是《杯雪》里的谁')}</button>
  <button class="btn ghost" data-act="go" data-v="E">从头开始</button>
 </div>
 <details class="hallfold"><summary>▦ 展开全部　关卡地图 · 进度 · 模式 · 难度 · 说明</summary>
 <div class="progwrap"><div class="row"><span>关卡进度</span><b>${done}/${D.meta.levels.length} 关　★ ${ts}/${maxStars()}</b></div>
  <div class="track"><i style="width:${Math.round(ts/maxStars()*100)}%"></i></div>
  <div class="row" style="margin:9px 0 5px"><span>档案解锁</span><b>${au}/${at} 页</b></div>
  <div class="track"><i style="width:${Math.round(au/at*100)}%;background:var(--blue)"></i></div>
  <div class="row" style="margin:9px 0 0;font-size:10.5px;color:var(--muted)"><span>通关一关，开一页资料；漫游不写星也不解锁</span><span>${esc(diffNote())}</span></div></div>
 <div class="perfbar"><span>◈ 动画表演</span>
  <b>${D.meta.levels.filter(l=>perfReady(l.id)).length}/${D.meta.levels.length} 关完整</b>
  <span class="perfnote">基础演出已可用 · 完整演出待生图与语音包 · <button data-act="perf_gate">${PERF_GATE?'切回基础优先':'仅开放完整演出'}</button></span></div>
 <div class="hallhead"><b>关卡地图 · 七卷 ${D.meta.levels.length} 关</b><span>建议按序 · 也可直接跳</span></div>
 ${D.meta.volumes.map(vol=>{
  const ls=vol.ids.map(id=>D.meta.levels.find(l=>l.id===id)).filter(Boolean);
  const vd=ls.filter(l=>(PROG[l.id]||{}).done).length;
  const card=l=>{
   const p=PROG[l.id]||{}, st=p.stars||0;
   const def=D.meta.archDefs.find(x=>x.need===l.id)||
             (l.arch?D.meta.archDefs.find(x=>x.id===l.arch):null);
   const un=def?archUnlocked(def):false;
   const _miss=perfMissing(l.id), _lock=perfLocked(l.id);
   const _cls='lvl '+(p.done?'done ':'')+(_lock?'locked ':(_miss.length?'pending ':''));
   return `<button class="${_cls}" data-act="go" data-v="${l.id}" style="--bg:url('${ART[l.art]}')"
     ${_lock?'aria-label="'+esc(l.t)+'：完整演出筹备中，敬请期待"':''}>
    <span class="keycap">${l.key}</span>
    <div class="l1"><span class="no">${l.no} · ${l.time} · ${'◆'.repeat(l.diff||1)}${'◇'.repeat(3-(l.diff||1))}</span>
     <h3>${esc(l.t)}</h3><span class="state ${p.done?'ok':''}">${p.done?'已通关':'未通关'}</span></div>
    <div class="l2">${_miss.length?`<span class="perftag ${_lock?'lock':''}">${_lock?'🔒':'◈'} ${_lock?'完整演出 · 敬请期待':'演出筹备中'} <em>缺 ${_miss.length} 类</em></span>`:'<span class="perftag ok">◈ 演出齐备</span>'}
     <span class="stars">${starHTML(st)}</span></div></button>`;
  };
  const undone=ls.filter(l=>!(PROG[l.id]||{}).done), fin=ls.filter(l=>(PROG[l.id]||{}).done);
  return `<div class="volhead"><b>${esc(vol.t)}</b><span>${esc(vol.sub)}　·　${vd}/${ls.length} 关</span></div>
  <div class="lvlmap tight">${undone.map(card).join('')}</div>
  ${fin.length?`<details class="donedet"><summary>✓ 已通关 ${fin.length} 关 · 点开查看</summary><div class="lvlmap tight">${fin.map(card).join('')}</div></details>`:''}`;
 }).join('')}
 ${modesBlock()}
 ${diffsBlock()}
 <div class="btnrow" style="margin-top:12px"><button class="btn" data-act="go" data-v="${LAST}">继续上次 · ${esc((D.meta.levels.find(l=>l.id===LAST)||{}).t||'你是《杯雪》里的谁')}</button>
  <button class="btn ghost" data-act="go" data-v="arch">翻档案 · ${au}/${at} 页已开</button></div>
 <details class="hallmore"><summary>读法与说明</summary>
  <p>七卷按「入局 → 章句 → 人事 → 武学 → 世道 → 改编 → 补遗」排：卷一打底并留两处翻底，卷二到卷五把词源、人事、武学、史实逐层拆开，卷六专练「把改编新增的还给改编」，卷七把上一轮标「资料不足」的逐项填平。第七关起建议先把难度切到「● 校勘」；前三关不卡满星，是故意留的进入余量。</p>
  <p>顶部 <b>♫ 场景音</b> 与 <b>♪ 音效</b> 是两个独立开关；天晴有鸟鸣、雨夜有远雷，换关自动平滑过渡。全部实时合成、无音频文件、默认都关。朗读与语音默认关闭。</p>
 </details>
 </details>`;
}

/* ---------- A：逐幕文字冒险 ---------- */
function A_fresh(){
 return {stage:'play',node:D.A.start,clues:[],asks:askLimit(),askCount:0,stance:[],
  echo:'',q:{},qi:0,trail:[],end:null,reveal:null,pause:null,roam:0,mistakes:0};
}
function A_reset(){ S.A=A_fresh(); render(); }
function A_isNew(){ return showGuide(); }
function askLeft(){ return (isNew()||isRoam())?Infinity:S.A.asks; }
function artBanner(key,caption){
 return `<div class="artbanner" style="background-image:url('${ART[key]}')"></div>
  <div class="artcap">${esc(caption)}</div>`;
}
function A_guide(sc){
 if(!showGuide()||!sc||!sc.tip)return '';
 return `<div class="guide"><b>这一步在干什么</b>　${esc(sc.tip)}</div>`;
}
function A_go(to){
 if(to==='verdict'){
  if(isRoam()){ S.A.stage='roamend'; render(); return; }
  S.A.stage='verdict';S.A.qi=0;S.A.echo='';
 } else S.A.node=to;
 render();
}
function A_pause(to,payload){
 S.A.pause=Object.assign({to:to},payload);
 S.A.node='__pause'; S.A.echo=''; render();
}
function A_next(){
 if(S.A.node==='__reveal'){
  const r=S.A.reveal; S.A.reveal=null; A_go(r?r.to:'s2'); return;
 }
 const p=S.A.pause; if(!p)return;
 S.A.pause=null; A_go(p.to);
}
function A_roam(v){
 const keys=Object.keys(D.A.scenes);
 let i=keys.indexOf(S.A.node); if(i<0)i=0;
 if(v==='prev')i=Math.max(0,i-1);
 else if(v==='next')i=Math.min(keys.length-1,i+1);
 else if(v.indexOf('goto:')===0)i=Math.max(0,Math.min(keys.length-1,+v.split(':')[1]));
 S.A.node=keys[i]; S.A.echo=''; S.A.reveal=null; S.A.pause=null; render();
}
function A_choose(v){
 const [sid,idx]=v.split('|');
 const sc=D.A.scenes[sid]; if(!sc)return;
 const o=sc.opts[+idx]; if(!o)return;
 if(o.stance)S.A.stance.push(o.stance);
 S.A.trail.push(sc.t);
 if(showPause()){
  A_pause(o.to,{kind:'choice',pick:o.t,say:o.say||'',
   note:o.stance?'这道态度题已经被记下，最后会见分晓。':'这一幕只是让你看清店里都有谁。'});
 }else{ S.A.echo=o.say||''; A_go(o.to); }
}
function A_act(v){
 const [act,cid,to]=v.split('|');
 const sc=D.A.scenes[S.A.node]; if(!sc)return;
 if(act==='ask'){
  if(askLeft()<=0)return;
  if(!isNew()&&!isRoam())S.A.asks--;
  S.A.askCount++;
  S.A.clues.push(cid); S.A.trail.push(sc.t); S.A.echo='';
  S.A.reveal={text:sc.reveal||'',clue:sc.clueText||'',to:to};
  S.A.node='__reveal'; render(); return;
 }
 S.A.clues.push(cid); S.A.trail.push(sc.t); S.A.echo='';
 if(showPause())A_pause(to,{kind:'take',clue:sc.clueText||'',quote:sc.quote||''});
 else A_go(to);
}
function A_q(v){
 const [qid,val]=v.split('|');
 S.A.q[qid]=val; S.A.qi++;
 if(isChallenge()){
  const q=D.A.verdict[S.A.qi-1]; if(q&&q.a!==val)S.A.mistakes++;
 }
 if(S.A.qi>=D.A.verdict.length)A_finish(); else render();
}
function A_finish(){
 const q=S.A.q, correct=(q.q1==='luo'&&q.q2==='baggage');
 const quiet=S.A.stance.filter(x=>x==='quiet').length;
 const defend=S.A.stance.filter(x=>x==='defend').length;
 let k;
 if(correct&&quiet>=2)k='true';
 else if(correct)k='half';
 else if(q.q1==='shen'||defend>=2)k='fame';
 else k='wrong';
 S.A.end=k; S.A.stage='end';
 let stars=1;
 if(correct)stars=2;
 if(correct&&quiet>=2&&S.A.mistakes===0)stars=3;
 if(isChallenge()&&S.A.mistakes>challengeAllowance())stars=Math.min(stars,2);
 if(DIFF==='collate'&&S.A.mistakes>0)stars=1; /* 校勘：断定错一题就不给满星 */
 S.A.stars=stars;
 markClear('A',stars,A_endLabel(k));
 save('A',modeInfo().name+' · 已通关'); render();
}
function A_endLabel(k){return ({'true':'真结局','half':'半知','fame':'虚名','wrong':'误判'})[k]||k;}
function A_bar(label){
 const quiet=S.A.stance.filter(x=>x==='quiet').length;
 const hold=S.A.node==='__reveal'||S.A.node==='__pause';
 const n=hold?S.A.trail.length:Math.min(S.A.trail.length+1,D.A.total);
 const first=label?`<span class="pill">${label}</span>`:`<span class="pill">第 <b>${n}/${D.A.total}</b> 幕</span>`;
 const mode=`<span class="modechip ${showGuide()?'':'n'}">${modeInfo().icon} ${modeInfo().name}</span>`;
 const lim=askLimit();
 const ask=(lim===Infinity)?`<span class="pill">追问 <b>不限</b> · ${S.A.askCount} 次</span>`
  :`<span class="pill">追问 <b>${lim===0?'关闭':S.A.asks+' 次剩余'}</b></span>`;
 return `<div class="bar">${first}${mode}
  <span class="pill">听闻簿 <b>${S.A.clues.length}/10</b></span>${ask}
  <span class="pill">不辩 <b>${quiet}/3</b></span></div>`;
}
function A_trail(){
 if(!S.A.trail.length)return '';
 return `<details class="trail"><summary>回看已过的 ${S.A.trail.length} 幕</summary>
  ${S.A.trail.map((t,i)=>`<div><span>${i+1}</span>${esc(t)}</div>`).join('')}</details>`;
}
function renderA(){
 const A=S.A, d=D.A;
 if(A.stage==='intro')return `${artBanner('A','水墨意境 · 铜陵困马集的秋雨一夜')}
  <div class="hero"><h2>第二关 · 雨驿一夜</h2>
  <div class="kind" style="font-size:12px;color:var(--blue);margin-bottom:10px">逐幕文字冒险　／　约 8 分钟　／　14 幕</div>
  <p>${nl(d.intro)}</p>
  <div class="note" style="margin-top:4px"><b>怎么玩</b>　一屏只有一幕、一个选择，不再一次铺开清单。新手模式选完会停一屏看回执，点「继续」才走下一幕。</div>
  <div class="bar" style="margin:0 0 10px"><span class="pill">当前模式</span>
   <span class="modechip ${showGuide()?'':'n'}">${modeInfo().icon} ${modeInfo().name}</span>
   <span class="pill">★ ${(PROG.A||{}).stars||0}/3</span><span class="pill">二十四关通用</span></div>
  <div class="modes">${D.meta.modeOrder.map(k=>{
   const m=D.meta.modes[k];
   return `<button class="mode ${MODE===k?'rec':''}" data-act="A_mode" data-v="${k}" style="${MODE===k?'border-color:var(--green);box-shadow:0 0 0 2px rgba(78,115,81,.12)':''}"><b>${m.icon} ${m.name}${MODE===k?'　✓ 当前':''}</b><span class="d">${esc(m.lead)}</span></button>`;
  }).join('')}</div>
  <div class="btnrow"><button class="btn" data-act="A_start">进店，坐下</button>
   <button class="btn ghost" data-act="A_back">回大厅改模式</button></div></div>`;

 if(A.stage==='end'){
  const e=d.ends[A.end];
  const quiet=A.stance.filter(x=>x==='quiet').length;
  return `<div class="endart" style="background-image:url('${ART.A}')"></div>
  <div class="end"><h2>${e.t}</h2><p>${nl(e.d)}</p></div>
  ${resultBox('A',A.stars||1,A_endLabel(A.end),A.mistakes)}
  <div class="review"><div><b>其一</b>　正解：骆寒。${A.q.q1==='luo'?'✔ 你答对了':'✘ 你选了别的'}</div>
   <div><b>其二</b>　正解：铺盖行李与被夺回的那一车。${A.q.q2==='baggage'?'✔ 你答对了':'✘ 六车是石头，江底是演的'}</div>
   <div><b>态度</b>　三次「要不要辩解」里，你选了 ${quiet} 次不辩。</div>
   <div><b>走过</b>　${A.trail.length} 幕，记下 ${A.clues.length} 条听闻，追问 ${A.askCount} 次。</div>
   <div><b>复盘</b>　秦稳故意砸招牌 → 六车石头作饵 → 骆寒弃银引开缇骑 → 金条藏在铺盖里过江。全书最大的一次叙述欺骗，就藏在「于心不忍」四个字后面。</div></div>
  ${showGuide()?`<div class="walk"><h4>逐幕复盘 · 这一夜是怎么骗过你的</h4>
   ${d.walkthrough.map(w=>`<div><b>${esc(w[0])}</b><span>${esc(w[1])}</span></div>`).join('')}</div>`:''}
  <div class="btnrow" style="margin-top:14px"><button class="btn" data-act="A_reset">再走一夜</button>
  <button class="btn ghost sm" data-act="A_back">换模式</button>
  <button class="btn ghost" data-act="go" data-v="B">下一关 · 六车石头</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
 }
 if(A.stage==='roamend'){
  return `<div class="endart" style="background-image:url('${ART.A}')"></div>
  <div class="end"><h2>这一夜走完了</h2><p>${nl(d.intro.split('\n')[0])}</p>
   <p>漫游模式不给断定、不结算、不写星。你要是想看看自己会断成什么样，回大厅切到新手或挑战再走一遍。</p></div>
  <div class="roamnote"><b>漫游笔记</b>　十四幕里，真正动手的人一直没替自己说过一句；被叫了一整夜「沈大侠」的那个人，也一次没辩。虚名留在江南，银子过了江。</div>
  <div class="btnrow"><button class="btn" data-act="A_reset">从头再翻</button>
   <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
 }

 if(A.stage==='verdict'){
  const q=d.verdict[A.qi];
  return `${A_bar('断　定 · '+(A.qi+1)+'/2')}
  <div class="note"><b>断定 · ${A.qi+1}/2</b>　天亮了，雨停了。不必向任何人解释，只回答这一件。</div>
  ${showGuide()&&d.hints[A.qi]?`<div class="hintbox"><b>先别急着选</b>　${esc(d.hints[A.qi])}（不给答案，只给个方向。）</div>`:''}
  <div class="scene"><div class="no">断　定</div><h2>${q.q}</h2>
   <div class="opts">${q.opts.map(o=>`<button class="opt" data-act="A_q" data-v="${q.id}|${o[1]}">${esc(o[0])}</button>`).join('')}</div></div>
  ${A_trail()}
  <div class="btnrow"><button class="btn ghost sm" data-act="A_reset">重来</button></div>`;
 }

 /* 追问回答：单独一屏 */
 if(A.node==='__reveal'){
  const r=A.reveal||{text:'',clue:'',to:'s2'};
  return `${A_bar('追　问 · 第 '+A.trail.length+'/'+d.total+' 幕')}
  <div class="scene"><div class="no">追　问</div><h2>多问出来的那一句</h2>
   <div class="revealbox">${esc(r.text)}</div>
   ${r.clue?`<div class="clue"><em>同时听出的</em>　${esc(r.clue)}</div>`:''}
   <div class="opts" style="margin-top:14px"><button class="opt" data-act="A_next">继续听下去　→</button></div></div>
  ${A_trail()}`;
 }

 /* 新手模式回执：选完先停一屏 */
 if(A.node==='__pause'){
  const p=A.pause||{to:'s2',kind:'take'};
  let body='';
  if(p.kind==='choice'){
   body=`<div class="pick"><b>你选了</b>　${esc(p.pick)}</div>`+
    (p.say?`<div class="revealbox">${esc(p.say)}</div>`:'')+
    (p.note?`<div class="clue"><em>记一笔</em>　${esc(p.note)}</div>`:'');
  }else{
   body=`<div class="pick"><b>记下了</b>　「${esc(p.quote)}」</div>`+
    `<div class="clue"><em>同时听出的</em>　${esc(p.clue)}</div>`;
  }
  return `${A_bar('回　执 · 第 '+A.trail.length+'/'+d.total+' 幕')}
  <div class="pause"><div class="no">这一幕的回执　·　看清楚再走</div><h2>先停一下</h2>${body}
   <div class="opts next"><button class="opt" data-act="A_next">继续听下去　→</button></div></div>
  ${A_trail()}
  <div class="btnrow"><button class="btn ghost sm" data-act="A_reset">重来</button></div>`;
 }

 const sc=d.scenes[A.node];
 if(!sc)return `<div class="note">这一幕走丢了。<button class="btn sm" data-act="A_reset">重来</button></div>`;

 /* 漫游：只读翻页，不判定、不结算 */
 if(isRoam()){
  const keys=Object.keys(d.scenes), idx=keys.indexOf(A.node);
  let h=`${A_bar('漫　游 · 第 '+(idx+1)+'/'+d.total+' 幕')}
   <div class="roamnote"><b>漫游模式</b>　这一夜只翻看，不做选择、不写星。用下面的按钮前后走，点幕号直接跳。</div>
   <div class="scene"><div class="no">第 ${idx+1} 幕　／　${d.total} 幕</div><h2>${esc(sc.t)}</h2>
   ${(sc.p||[]).map(p=>`<p>${esc(p)}</p>`).join('')}`;
  if(sc.who)h+=`<div class="who">${esc(sc.who)}</div><span class="cred">${esc(sc.cred)}</span>
   <div class="squote">「${esc(sc.quote)}」</div>`;
  if(sc.clueText)h+=`<div class="clue"><em>这一幕埋的</em>　${esc(sc.clueText)}</div>`;
  h+=`</div><div class="roamnav">
   <button class="btn ghost sm" data-act="A_roam" data-v="prev" ${idx<=0?'disabled':''}>← 上一幕</button>
   <button class="btn ghost sm" data-act="A_roam" data-v="next" ${idx>=d.total-1?'disabled':''}>下一幕 →</button></div>
   <div class="bar">${keys.map((k,i)=>`<button class="pill ${i===idx?'hot':''}" data-act="A_roam" data-v="goto:${i}" style="cursor:pointer;${i===idx?'background:var(--green)':''}">${i+1}</button>`).join('')}</div>
   <div class="btnrow"><button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
  return h;
 }

 let h=`${A_bar()}${A_guide(sc)}`;
 if(A.echo)h+=`<div class="echo">余音　${esc(A.echo)}</div>`;
 h+=`<div class="scene"><div class="no">第 ${Math.min(A.trail.length+1,d.total)} 幕　／　${d.total} 幕</div>
  <h2>${esc(sc.t)}</h2>
  ${(sc.p||[]).map(p=>`<p>${esc(p)}</p>`).join('')}`;
 if(sc.who){
  h+=`<div class="who">${esc(sc.who)}</div><span class="cred">${esc(sc.cred)}</span>
   <div class="squote">「${esc(sc.quote)}」</div>`;
 }
 if(sc.clue){
  const canAsk=askLeft()>0;
  const sub=canAsk?(askLimit()===Infinity?'不扣次数，多出一屏回答':'消耗 1 次追问，多出一屏回答'):'追问已用尽／已关闭';
  const next=showPause()?'收进听闻簿，停一屏看回执':'收进听闻簿，往下走';
  h+=`<div class="opts" style="margin-top:16px">
   <button class="opt" data-act="A_act" data-v="take|${sc.clue}|${sc.to}">把这句记下<span class="d">${next}</span></button>
   <button class="opt" data-act="A_act" data-v="ask|${sc.clue}|${sc.to}" ${canAsk?'':'disabled'}>${esc(sc.askLabel||'追问')}<span class="d">${sub}</span></button></div>`;
 }else{
  h+=`<div class="opts" style="margin-top:16px">${sc.opts.map((o,i)=>
    `<button class="opt" data-act="A_choose" data-v="${A.node}|${i}">${esc(o.t)}${showPause()?'<span class="d">选完会停一屏，看回执再继续</span>':''}</button>`).join('')}</div>`;
 }
 h+=`</div>${A_trail()}
  <div class="btnrow"><button class="btn ghost sm" data-act="A_reset">重来</button>
  <button class="btn ghost sm" data-act="A_back">换模式</button>
  <button class="btn ghost sm" data-act="go" data-v="hall">回大厅</button></div>`;
 return h;
}

/* ---------- B ---------- */
function B_sel(id){
 const s=S.B.sel, i=s.indexOf(id);
 if(i>=0)s.splice(i,1);
 else if(s.length<2)s.push(id);
 render();
}
function B_hint(){
 if(hintLimit()===0)return;
 if(hintLimit()!==Infinity&&S.B.hint<=0)return;
 if(hintLimit()!==Infinity)S.B.hint--;
 S.B.log.push(['提示','「稳如泰山」不是说从不失手，是这回甘愿让人以为他失了手。弃银也是演的。']); render();
}
function B_next(){
 const p=S.B.pause; S.B.pause=null; S.B.stage='play';
 if(p&&p.final)B_end(); else render();
}
function B_run(){
 if(S.B.sel.length!==2)return;
 const order=['qin_lose','qin_guard','luo_drop','luo_take','luo_river','jin_push','shen_book','du_pact'];
 const picks=order.filter(x=>S.B.sel.includes(x));
 let L=[];
 picks.forEach(a=>{
  switch(a){
   case 'luo_drop': S.B.focus='luo'; L.push('少年当众弃了镖银。缇骑的眼睛全跟着他走。');break;
   case 'luo_take': S.B.focus='luo'; S.B.silver='cart'; L.push('少年夺回最后一车，行踪彻底暴露。');break;
   case 'luo_river': S.B.focus='river'; L.push('骆驼入江。缇骑沿岸打捞，认定银子沉了底。');break;
   case 'qin_lose': S.B.sign='broken'; L.push('秦稳没吭声，任由「稳如泰山」的招牌被砸。');break;
   case 'qin_guard': S.B.focus='six'; S.B.pact='risk'; L.push('秦稳死护明镖，缇骑盯紧六车，旧盟转危。');break;
   case 'du_pact': S.B.pact='ok'; L.push('杜焦二老用逃死令收了散众，旧盟没破。');break;
   case 'shen_book': S.B.known=true; L.push('沈放清完账：六车全是石头，真金不在车上。');break;
   case 'jin_push':
     if(S.B.sign==='broken'){S.B.silver='baggage';L.push('铺盖小车被推上渡船，金条藏在棉被里。');}
     else L.push('没人敢动那辆车——招牌还立着。');break;
  }
 });
 if(S.B.silver==='baggage'){
  S.B.silver='crossed'; L.push('天亮，小车过了江。缇骑还在别处扑空。');
 }
 S.B.turn++;
 L.forEach(x=>S.B.log.push(['第'+S.B.turn+'回合',x]));
 S.B.sel=[];
 S.B.pause={turn:S.B.turn,lines:L,final:S.B.turn>=3};
 if(showPause()){ S.B.stage='pause'; render(); }
 else if(S.B.turn>=3)B_end();
 else render();
}
function B_end(){
 const s=S.B; let k;
 if(s.silver!=='crossed')k='fail';
 else if(s.pact==='risk')k='pact';
 else if(!s.known)k='blind';
 else if(s.focus==='river'||s.focus==='six')k='perfect';
 else k='blind';
 s.end=k; s.stage='end';
 if(k==='fail'&&isChallenge())s.mistakes++;
 let stars=k==='perfect'?3:(k==='fail'?1:2);
 if(isChallenge()&&s.mistakes>challengeAllowance())stars=Math.min(stars,2);
 s.stars=stars;
 markClear('B',stars,D.B.ends[k].t);
 save('B',modeInfo().name+' · '+(k==='perfect'?'完美通关':'已通关')); render();
}
function B_modeBar(){
 return `<span class="modechip ${showGuide()?'':'n'}">${modeInfo().icon} ${modeInfo().name}</span>`;
}
function renderB(){
 const B=S.B,d=D.B;
 if(B.stage==='intro')return `${artBanner('B','水墨意境 · 拂晓渡口，六车石头')}
  <div class="hero"><h2>第三关 · 六车石头</h2>
  <div class="kind" style="font-size:12px;color:var(--blue);margin-bottom:10px">暗镖调度　／　约 6 分钟　／　三回合</div>
  <p>${nl(d.intro)}</p>
  <div class="bar" style="margin:0 0 10px"><span class="pill">当前模式</span>${B_modeBar()}
   <span class="pill">★ ${(PROG.B||{}).stars||0}/3</span>
   <span class="pill">${showGuide()?'逐回合引导 · 回执 · 提示不限':isChallenge()?'零提示 · 按失误评级':isRoam()?'不写星 · 只观察':'点完即走 · 提示 1 次'}</span></div>
  ${showGuide()?'<div class="note" style="margin-top:4px"><b>新手模式怎么走</b>　每回合先有一句「这一回合在干什么」；动作池里会标出两个<b>建议</b>（只标，不替你选）；执行后停一屏看这回合发生了什么，再点继续。</div>':''}
  ${isChallenge()?'<div class="hintbox"><b>挑战模式</b>　无引导、无建议、无提示，答错记失误；结算给 S／A／B／C。</div>':''}
  <div class="btnrow" style="margin-top:12px"><button class="btn" data-act="B_start">开始调度</button>
  <button class="btn ghost" data-act="A_back">去改模式</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div></div>`;
 if(B.stage==='end'&&isRoam()){
  return `<div class="endart" style="background-image:url('${ART.B}')"></div>
  <div class="end"><h2>这一趟走完了</h2><p>漫游模式不给判定、不写星。三回合怎么走都由你，下面只是一份观察笔记。</p></div>
  <div class="roamnote"><b>观察笔记</b>　真银 ${B.silver==='crossed'?'过了江':'还在岸这边'}；缇骑 ${B.focus==='river'?'在捞江底':B.focus==='six'?'盯着六车':'跟着少年'}；招牌 ${B.sign==='broken'?'已砸':'还立着'}。四个变量彼此牵动，正是这局的全部。</div>
  <div class="log" style="margin-top:12px">${B.log.map(x=>`<div><span class="t">${x[0]}</span>${esc(x[1])}</div>`).join('')}</div>
  <div class="btnrow"><button class="btn" data-act="B_reset">再走一趟</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
 }
 if(B.stage==='end'){
  const e=d.ends[B.end];
  return `<div class="endart" style="background-image:url('${ART.B}')"></div>
  <div class="end"><h2>${e.t}</h2><p>${nl(e.d)}</p></div>
  ${resultBox('B',B.stars||1,e.t,B.mistakes)}
  <div class="review"><div><b>真银</b>　${B.silver==='crossed'?'已过江':'仍在岸这边'}</div>
   <div><b>缇骑</b>　${B.focus==='river'?'在捞江底':B.focus==='six'?'盯着六车石头':'跟着少年'}</div>
   <div><b>旧盟</b>　${B.pact==='ok'?'未破':'转危'}</div>
   <div><b>你看穿了吗</b>　${B.known?'清过账，知道六车是石头':'全程跟着别人走'}</div></div>
  ${showGuide()?`<div class="walk"><h4>逐环节复盘 · 这趟暗镖怎么成局</h4>
   ${d.review.map(w=>`<div><b>${esc(w[0])}</b><span>${esc(w[1])}</span></div>`).join('')}</div>`:''}
  <div class="log" style="margin-top:12px">${B.log.map(x=>`<div><span class="t">${x[0]}</span>${esc(x[1])}</div>`).join('')}</div>
  <div class="btnrow"><button class="btn" data-act="B_reset">再走一趟</button>
  <button class="btn ghost" data-act="go" data-v="D">下一关 · 博闻</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
 }
 /* 新手模式：回合回执屏 */
 if(B.stage==='pause'){
  const p=B.pause||{turn:B.turn,lines:[],final:false};
  return `<div class="bar"><span class="pill">回　执 · 第 ${p.turn}/3 回合</span>${B_modeBar()}</div>
  <div class="pause"><div class="no">这一回合发生了什么　·　看清楚再走</div><h2>先停一下</h2>
   ${p.lines.length?p.lines.map(x=>`<div class="pick">${esc(x)}</div>`).join(''):'<div class="pick">这一回合没有动静。</div>'}
   <div class="clue"><em>眼下的局面</em>　真银 ${B.silver==='crossed'?'已过江':B.silver==='baggage'?'在铺盖小车':'还在镖车上'}；缇骑 ${B.focus==='river'?'在捞江底':B.focus==='six'?'盯着六车':'跟着少年'}；招牌 ${B.sign==='broken'?'已砸':'还立着'}。</div>
   <div class="opts next"><button class="opt" data-act="B_next">${p.final?'看结算　→':'继续下一回合　→'}</button></div></div>
  <div class="btnrow"><button class="btn ghost sm" data-act="B_reset">重来</button></div>`;
 }
 const labels={cart:'镖车上',baggage:'铺盖小车',crossed:'已过江'};
 const fl={six:'六车',luo:'少年',river:'江底'};
 const rec=showRec()?(d.recommend[B.turn]||[]):[];
 const hl=hintLimit();
 let h=`<div class="bar">${B_modeBar()}<span class="pill">回合 <b>${B.turn+1}/3</b></span>
  <span class="pill">真银 <b>${labels[B.silver]}</b></span>
  <span class="pill">缇骑注意力 <b>${fl[B.focus]}</b></span>
  <span class="pill">招牌 <b>${B.sign==='broken'?'已砸':'还立着'}</b></span>
  <span class="pill ${B.pact==='risk'?'hot':''}" style="${B.pact==='risk'?'background:var(--red)':''}">旧盟 <b>${B.pact==='ok'?'稳':'危'}</b></span>
  <span class="pill">已清账 <b>${B.known?'是':'否'}</b></span></div>`;
 if(showGuide())h+=`<div class="guide"><b>这一回合在干什么</b>　${esc(d.guides[B.turn]||'')}</div>`;
 h+=`<div class="note">本回合选 <b>2 个动作</b>（已选 ${B.sel.length}/2）。${hl===Infinity?'提示不限次数；绿框是建议，不是答案。':hl===0?'提示已关闭（挑战模式）。':'提示还有 '+B.hint+' 次。'}</div>`;
 if(showRec()&&rec.length)h+=`<div class="rechint">◆ 已标出本回合两个建议动作，仍由你自己点选。</div>`;
 h+=`<div class="acts">${d.acts.map(a=>{
   const dis=(a.id==='luo_river'&&B.turn===0)?'disabled':'';
   return `<button class="act ${B.sel.includes(a.id)?'sel':''} ${rec.includes(a.id)?'rec':''}" data-act="B_sel" data-v="${a.id}" ${dis}>
    <span class="w">${a.who}${rec.includes(a.id)?' · 建议':''}${a.id==='luo_river'&&B.turn===0?' · 第二回合起':''}</span>
    <span class="t">${a.t}</span><span class="d">${a.d}</span></button>`;}).join('')}</div>`;
 if(B.log.length)h+=`<div class="log" style="margin-top:12px">${B.log.map(x=>`<div><span class="t">${x[0]}</span>${esc(x[1])}</div>`).join('')}</div>`;
 h+=`<div class="btnrow" style="margin-top:12px"><button class="btn" data-act="B_run" ${B.sel.length!==2?'disabled':''}>执行本回合</button>
  <button class="btn ghost sm" data-act="B_hint" ${(hl===0||(hl!==Infinity&&B.hint<=0))?'disabled':''}>${hl===Infinity?'看一句提示':'用一次提示'}</button>
  <button class="btn ghost sm" data-act="B_reset">重来</button>
  <button class="btn ghost sm" data-act="go" data-v="hall">回大厅</button></div>`;
 return h;
}

/* ---------- D ---------- */
function D_ans(i){
 if(S.D.showWhy)return;
 const q=dQuiz()[S.D.i]; S.D.picked=i; S.D.showWhy=true;
 if(i===q.a){S.D.streak++;S.D.score+=10+Math.min(S.D.streak-1,3)*5;}
 else {S.D.streak=0;S.D.wrong.push({q:q.q,a:q.opts[q.a],why:q.why,yours:q.opts[i]});if(isChallenge())S.D.mistakes++;}
 render();
}
function D_next(){
 if(isRoam()){ S.D.i=(S.D.i+1)%dQuiz().length; S.D.picked=null;S.D.showWhy=false;S.D.showHint=false;render();return; }
 if(S.D.i>=dQuiz().length-1){
  S.D.stage='end'; S.D.best=Math.round(S.D.score/(dQuiz().length*10+30)*100);
  const right=dQuiz().length-S.D.wrong.length;
  let stars=starsByRatio(right,dQuiz().length);
  if(isChallenge()&&S.D.mistakes>challengeAllowance())stars=Math.min(stars,2);
  S.D.stars=stars;
  markClear('D',stars,'答对 '+right+'/'+dQuiz().length);
  save('D','最佳 '+S.D.score+' 分'); render();
 } else {S.D.i++;S.D.picked=null;S.D.showWhy=false;S.D.showHint=false;render();}
}
function D_jump(v){
 const n=dQuiz().length;
 if(v==='prev')S.D.i=Math.max(0,S.D.i-1);
 else if(v==='next')S.D.i=Math.min(n-1,S.D.i+1);
 else S.D.i=Math.max(0,Math.min(n-1,+v));
 S.D.picked=null;S.D.showWhy=false;S.D.showHint=false;render();
}
function renderD(){
 const S_=S.D,d=D.D;
 const chip=`<span class="modechip ${showGuide()?'':'n'}">${modeInfo().icon} ${modeInfo().name}</span>`;
 if(S_.stage==='intro')return `${artBanner('D','水墨意境 · 秣陵冬雪，一盏孤灯')}
  <div class="hero"><h2>第四关 · 杯雪博闻</h2>
  <div class="kind" style="font-size:12px;color:var(--gold);margin-bottom:10px">轻量闯关　／　约 5 分钟　／　${dQuiz().length} 题（${esc(diffNote())}）</div>
  <p>${nl(d.intro)}</p>
  <div class="bar" style="margin:0 0 10px"><span class="pill">当前模式</span>${chip}
   <span class="pill">★ ${(PROG.D||{}).stars||0}/3</span>
   <span class="pill">${showGuide()?'每题可看方向提示':isChallenge()?'零提示 · 按失误评级':isRoam()?'可跳题 · 不结算':'直接作答'}</span></div>
  ${showGuide()?'<div class="note" style="margin-top:4px"><b>新手模式</b>　每题可点「给个方向」看一句提示，只指方向、不给答案；答完照常给解释与错题回顾。</div>':''}
  ${isRoam()?'<div class="roamnote"><b>漫游模式</b>　可前后跳题、只看解释，不计分、不写星、不进结算。</div>':''}
  <div class="btnrow" style="margin-top:12px"><button class="btn" data-act="D_start">开始答题</button>
  <button class="btn ghost" data-act="A_back">去改模式</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div></div>`;
 if(S_.stage==='end'&&isRoam()){
  return `<div class="endart" style="background-image:url('${ART.D}')"></div>
  <div class="end" style="border-top-color:var(--gold)"><h2>题库翻完了</h2><p>漫游模式不计分、不写星、不结算。点题号随时回看，解释一直在这儿。</p></div>
  <div class="btnrow"><button class="btn" data-act="D_start">再翻一轮</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
 }
 if(S_.stage==='end'){
  return `<div class="endart" style="background-image:url('${ART.D}')"></div>
  <div class="end" style="border-top-color:var(--gold)"><h2>得分 ${S_.score}</h2>
   <p>答对 ${dQuiz().length-S_.wrong.length}/${dQuiz().length} 题。${S_.wrong.length===0?'全对——词源、考订、结构都没被绕进去。':'错题已收在下面，回头翻一遍比多刷一轮有用。'}</p></div>
  ${resultBox('D',S_.stars||1,'答对 '+(dQuiz().length-S_.wrong.length)+'/'+dQuiz().length,S_.mistakes)}
  ${S_.wrong.length?`<div class="review"><b>错题回顾</b>${S_.wrong.map(w=>`<div><b>${esc(w.q)}</b><br>正解：${esc(w.a)}　（你选了 ${esc(w.yours)}）<br><span style="color:var(--muted)">${esc(w.why)}</span></div>`).join('')}</div>`:''}
  <div class="btnrow" style="margin-top:14px"><button class="btn" data-act="D_start">再刷一轮</button>
  <button class="btn ghost" data-act="go" data-v="C">下一关 · 淮上旧盟</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
 }
 const q=dQuiz()[S_.i];
 const pct=Math.round(S_.i/dQuiz().length*100);
 let h=`<div class="bar">${chip}<span class="pill">${S_.i+1} / ${dQuiz().length}</span>
  <span class="pill">得分 <b>${S_.score}</b></span><span class="pill">连对 <b>${S_.streak}</b></span></div>
  <div class="prog"><i style="width:${pct}%"></i></div>`;
 if(isRoam())h+=`<div class="roamnote"><b>漫游模式</b>　点题号直接跳，答完只看解释；不结算、不写星。</div>`;
 if(showGuide()&&S_.showHint&&!S_.showWhy)
  h+=`<div class="hintbox"><b>给个方向</b>　${esc(d.hints[S_.i]||'')}（不告诉答案。）</div>`;
 h+=`<div class="card"><div class="sec">${q.sec}</div><div class="qtitle">${q.q}</div>
  <div class="opts">${q.opts.map((o,i)=>{
   let cl=S_.picked===i?'sel':'';
   if(S_.showWhy){if(i===q.a)cl='right';else if(i===S_.picked)cl='wrong';}
   return `<button class="opt ${cl}" data-act="D_ans" data-v="${i}" ${S_.showWhy?'disabled':''}>${esc(o)}</button>`;}).join('')}</div>
  ${S_.showWhy?`<div class="explain"><b>${S_.picked===q.a?'答对了':'正解：'+esc(q.opts[q.a])}</b><br>${esc(q.why)}</div>`:''}</div>`;
 if(isRoam()){
  h+=`<div class="roamnav"><button class="btn ghost sm" data-act="D_jump" data-v="prev" ${S_.i<=0?'disabled':''}>← 上一题</button>
   <button class="btn ghost sm" data-act="D_jump" data-v="next" ${S_.i>=dQuiz().length-1?'disabled':''}>下一题 →</button></div>
   <div class="bar">${dQuiz().map((_,i)=>`<button class="pill ${i===S_.i?'hot':''}" data-act="D_jump" data-v="${i}" style="cursor:pointer;${i===S_.i?'background:var(--green)':''}">${i+1}</button>`).join('')}</div>
   <div class="btnrow"><button class="btn ghost sm" data-act="go" data-v="hall">回大厅</button></div>`;
  return h;
 }
 h+=`<div class="btnrow"><button class="btn" data-act="D_next" ${S_.showWhy?'':'disabled'}>${S_.i>=dQuiz().length-1?'看结果':'下一题'}</button>
  ${showGuide()&&!S_.showWhy?`<button class="btn ghost sm" data-act="D_hint">${S_.showHint?'收起方向':'给个方向'}</button>`:''}
  <button class="btn ghost sm" data-act="D_reset">退出</button>
  <button class="btn ghost sm" data-act="go" data-v="hall">回大厅</button></div>`;
 return h;
}

/* ---------- C ---------- */
function C_opt(i){
 const lv=D.C.levels[S.C.k], o=lv.opts[i], e=o.e;
 S.C.g=Math.max(0,Math.min(10,S.C.g+e[0]));
 S.C.b=Math.max(0,Math.min(10,S.C.b+e[1]));
 S.C.p=Math.max(0,Math.min(10,S.C.p+e[2]));
 S.C.log.push([lv.t,o.t,o.n]);
 const zeroEnd=(key,label)=>{
  S.C.end=key;S.C.stage='end';S.C.stars=1;
  if(isChallenge())S.C.mistakes++;
  markClear('C',1,label);save('C',label);render();
 };
 if(S.C.g===0){zeroEnd('zero_g','淮上断粮');return;}
 if(S.C.b===0){zeroEnd('zero_b','无人再赴一杯酒');return;}
 if(S.C.p===0){zeroEnd('zero_p','缇骑过江');return;}
 S.C.k++;
 if(S.C.k>=D.C.levels.length)C_end(); else render();
}
function C_end(){
 const {g,b,p}=S.C; let k;
 if(g>=7&&b>=7&&p>=7)k='best';
 else if(b>=7&&g<4)k='bonds';
 else if(g>=7&&b<4)k='grain';
 else if(p>=7&&g<5&&b<5)k='pact';
 else k='flat';
 S.C.end=k;S.C.stage='end';
 let stars=k==='best'?3:2;
 if(isChallenge()&&S.C.mistakes>challengeAllowance())stars=Math.min(stars,2);
 S.C.stars=stars;
 markClear('C',stars,D.C.ends[k].t);save('C',D.C.ends[k].t);render();
}
function stat(k,v,col){return `<div class="stat"><div class="k">${k}</div><div class="v" style="color:${col}">${v}</div>
 <div class="track"><i style="width:${v*10}%;background:${col}"></i></div></div>`;}
function renderC(){
 const C=S.C,d=D.C;
 const chip=`<span class="modechip ${showGuide()?'':'n'}">${modeInfo().icon} ${modeInfo().name}</span>`;
 if(C.stage==='intro')return `${artBanner('C','水墨意境 · 淮上秋深，账本与木杯')}
  <div class="hero"><h2>第五关 · 淮上旧盟</h2>
  <div class="kind" style="font-size:12px;color:var(--green);margin-bottom:10px">五关资源棋　／　约 7 分钟</div>
  <p>${nl(d.intro)}</p>
  <div class="bar" style="margin:0 0 10px"><span class="pill">当前模式</span>${chip}
   <span class="pill">★ ${(PROG.C||{}).stars||0}/3</span>
   <span class="pill">${showGuide()?'每关给一句「在考什么」':isChallenge()?'零提示 · 按失误评级':isRoam()?'不写星 · 只观察':'直接算账'}</span></div>
  ${showGuide()?'<div class="note" style="margin-top:4px"><b>新手模式</b>　每关多一句「这一关在考什么」，讲清三本账为什么不可能同时涨；结算仍按三本账的<b>形状</b>给结局，不按总分。</div>':''}
  <div class="btnrow" style="margin-top:12px"><button class="btn" data-act="C_start">接下这三本账</button>
  <button class="btn ghost" data-act="A_back">去改模式</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div></div>`;
 if(C.stage==='end'&&isRoam()){
  return `<div class="endart" style="background-image:url('${ART.C}')"></div>
  <div class="end"><h2>五关走完了</h2><p>漫游模式不给结局、不写星。三本账最后停在这个形状上，看看就好。</p></div>
  <div class="stats">${stat('钱粮',C.g,'var(--blue)')}${stat('人情',C.b,'var(--red)')}${stat('盟约',C.p,'var(--green)')}</div>
  <div class="roamnote"><b>观察笔记</b>　结算不看总分看形状：五部不是连续日记，是同一历史压力反复测试不同人物。</div>
  <div class="review"><b>五关走过</b>${C.log.map(x=>`<div><b>${esc(x[0])}</b>　${esc(x[1])}<br><span style="color:var(--muted)">${esc(x[2])}</span></div>`).join('')}</div>
  <div class="btnrow" style="margin-top:14px"><button class="btn" data-act="C_start">再算一遍</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
 }
 if(C.stage==='end'){
  const e=d.ends[C.end];
  return `<div class="endart" style="background-image:url('${ART.C}')"></div>
  <div class="end" style="border-top-color:var(--green)"><h2>${e.t}</h2><p>${nl(e.d)}</p></div>
  ${resultBox('C',C.stars||1,e.t,C.mistakes)}
  <div class="stats">${stat('钱粮',C.g,'var(--blue)')}${stat('人情',C.b,'var(--red)')}${stat('盟约',C.p,'var(--green)')}</div>
  <div class="review"><b>五关走过</b>${C.log.map(x=>`<div><b>${esc(x[0])}</b>　${esc(x[1])}<br><span style="color:var(--muted)">${esc(x[2])}</span></div>`).join('')}</div>
  <div class="btnrow" style="margin-top:14px"><button class="btn" data-act="C_start">再算一遍</button>
  <button class="btn ghost" data-act="go" data-v="F">下一关 · 谣言审判</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
 }
 const lv=d.levels[C.k];
 let h=`<div class="bar">${chip}<span class="pill">第 <b>${C.k+1}/5</b> 关</span><span class="pill">任一归零即提前结束</span></div>`;
 if(showGuide())h+=`<div class="ctip"><b>这一关在考什么</b>　${esc(d.tips[C.k]||'')}</div>`;
 h+=`<div class="stats">${stat('钱粮',C.g,'var(--blue)')}${stat('人情',C.b,'var(--red)')}${stat('盟约',C.p,'var(--green)')}</div>
  <div class="card"><div class="sec">${lv.t}</div><div class="qtitle">${lv.s}</div>
  <div class="opts">${lv.opts.map((o,i)=>`<button class="opt" data-act="C_opt" data-v="${i}">${o.t}<span class="d">${o.d}</span></button>`).join('')}</div></div>`;
 if(C.log.length)h+=`<div class="log">${C.log.map(x=>`<div><span class="t">${esc(x[0])}</span>${esc(x[1])}　<span style="color:var(--muted)">${esc(x[2])}</span></div>`).join('')}</div>`;
 h+=`<div class="btnrow" style="margin-top:10px"><button class="btn ghost sm" data-act="C_start">重开</button>
  <button class="btn ghost sm" data-act="go" data-v="hall">回大厅</button></div>`;
 return h;
}

/* ---------- E 你是《杯雪》里的谁 ---------- */
function E_ans(i){
 const q=D.E.quiz[S.E.i]; if(!q)return;
 const w=q.opts[i].w||{};
 Object.keys(w).forEach(k=>S.E.sc[k]=(S.E.sc[k]||0)+w[k]);
 S.E.picks[S.E.i]=i;
 S.E.i++;
 if(S.E.i>=D.E.quiz.length)E_finish(); else render();
}
function E_next(){ if(S.E.i>=D.E.quiz.length)E_finish(); else render(); }
function E_finish(){
 const sc=S.E.sc, order=Object.keys(D.E.roles).sort((a,b)=>(sc[b]||0)-(sc[a]||0));
 S.E.top=order[0]; S.E.second=order[1]; S.E.end=true; S.E.stage='end';
 let stars=2; if(isChallenge())stars=Math.min(stars,2);
 S.E.stars=stars;
 markClear('E',stars,D.E.roles[order[0]].n);
 save('E',modeInfo().name+' · 已完成'); render();
}
function renderE(){
 const E=S.E,d=D.E;
 const chip=`<span class="modechip ${showGuide()?'':'n'}">${modeInfo().icon} ${modeInfo().name}</span>`;
 if(E.stage==='intro')return `${artBanner('cover','水墨意境 · 一只将化未化的雪')}
  <div class="hero"><h2>第一关 · 你是《杯雪》里的谁</h2>
  <div class="kind" style="font-size:12px;color:var(--purple);margin-bottom:10px">角色人格测试　／　约 6 分钟　／　12 题</div>
  <p>${nl(d.intro)}</p>
  <div class="bar" style="margin:0 0 10px">${chip}<span class="pill">12 题 · 八种侠气</span></div>
  <div class="disclaim">这是文学趣味映射，不是心理测评或诊断，不定义你是谁；不收集任何个人资料。漫游模式不贴「最像谁」的标签，只给这一轮的落点。</div>
  <div class="btnrow" style="margin-top:12px"><button class="btn" data-act="E_start">开始照一照</button>
  <button class="btn ghost" data-act="A_back">去改模式</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div></div>`;
 if(E.stage==='end'){
  const r=d.roles[E.top], r2=d.roles[E.second]||r;
  const roam=isRoam();
  return `<div class="endart" style="background-image:url('${ART.cover}')"></div>
  ${roam?`<div class="rolecard"><div class="lab">漫游模式 · 这一轮的落点</div>
   <h2>只是这一轮走到这里</h2>
   <div class="judge">十二题里，你把最多力气留给了「${esc(r.t)}」这类处境。</div>
   <div class="roamnote" style="margin:0">不写星、不评级，也不说你像谁、该读哪一部。这是一轮选择分布，不是关于你的结论；换一批心境再答，落点大概又会不同。</div></div>`
  :`<div class="rolecard"><div class="lab">你最靠近　·　《杯雪》角色</div>
   <h2>${esc(r.n)}</h2><div class="judge">${esc(r.t)}</div>
   <ul>${r.lines.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>
   <div class="kv"><b>最该先读</b>　${esc(r.read)}<br><b>原著气质</b>　${esc(r.air)}</div></div>
  <div class="shadow"><b>另一面</b>　第二落点是 <b>${esc(r2.n)}</b>：${esc(r2.t)}。两种侠气常在同一个人身上换班，不必只认一个。</div>`}
  ${roam?'':resultBox('E',E.stars||2,'完成 12 题 · 落点 '+r.n,0)}
  <div class="disclaim">文学趣味映射，仅供自我观察与选读顺序参考，不是心理测评、诊断或人格定论；不据此推断现实经历、能力或关系。</div>
  <div class="btnrow"><button class="btn" data-act="E_start">再照一次</button>
   <button class="btn ghost" data-act="E_back">回看上一题</button>
   <button class="btn ghost" data-act="go" data-v="A">下一关 · 雨驿一夜</button>
   <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
 }
 const q=d.quiz[E.i], pct=Math.round(E.i/d.quiz.length*100);
 return `<div class="bar">${chip}<span class="pill">${E.i+1} / ${d.quiz.length}</span></div>
  <div class="prog"><i style="width:${pct}%"></i></div>
  <div class="card"><div class="sec">情境 ${E.i+1}</div><div class="qtitle">${esc(q.q)}</div>
   <div class="opts" style="margin-top:12px">${q.opts.map((o,i)=>
    `<button class="eopt" data-act="E_ans" data-v="${i}">${esc(o.t)}</button>`).join('')}</div></div>
  <div class="disclaim">没有对错，也不给分。选最像你第一反应的那一个。</div>
  <div class="btnrow">${E.i>0?'<button class="btn ghost sm" data-act="E_back">← 上一题</button>':''}
   <button class="btn ghost sm" data-act="E_reset">退出</button>
   <button class="btn ghost sm" data-act="go" data-v="hall">回大厅</button></div>`;
}

/* ---------- F 谣言审判 ---------- */
function F_ans(i){
 const c=D.F.cases[S.F.i]; S.F.picked=i; S.F.showWhy=true;
 if(i===c.a)S.F.right++; else {S.F.wrong.push({t:c.t,q:c.q,a:c.opts[c.a],yours:c.opts[i],why:c.why});if(isChallenge())S.F.mistakes++;}
 render();
}
function F_next(){
 if(S.F.i>=D.F.cases.length-1){
  S.F.stage='end'; S.F.end=true;
  let stars=starsByRatio(S.F.right,D.F.cases.length);
  if(isChallenge()&&S.F.mistakes>challengeAllowance())stars=Math.min(stars,2);
  S.F.stars=stars;
  markClear('F',stars,'判准 '+S.F.right+'/'+D.F.cases.length);
  save('F',modeInfo().name+' · 已完成'); render();
 } else {S.F.i++;S.F.picked=null;S.F.showWhy=false;S.F.showHint=false;render();}
}
function renderF(){
 const F=S.F,d=D.F;
 const chip=`<span class="modechip ${showGuide()?'':'n'}">${modeInfo().icon} ${modeInfo().name}</span>`;
 if(F.stage==='intro')return `${artBanner('A','水墨意境 · 同一场雨，三种说法')}
  <div class="hero"><h2>第六关 · 谣言审判</h2>
  <div class="kind" style="font-size:12px;color:var(--blue);margin-bottom:10px">多焦点判断　／　约 4 分钟　／　6 桩公案</div>
  <p>${nl(d.intro)}</p>
  <div class="bar" style="margin:0 0 10px"><span class="pill">当前模式</span>${chip}
   <span class="pill">★ ${(PROG.F||{}).stars||0}/3</span>
   <span class="pill">${showGuide()?'可看一条方向提示':isChallenge()?'零提示 · 按失误评级':'直接判断'}</span></div>
  <div class="btnrow" style="margin-top:12px"><button class="btn" data-act="F_start">升堂</button>
  <button class="btn ghost" data-act="A_back">去改模式</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div></div>`;
 if(F.stage==='end'&&isRoam()){
  return `<div class="endart" style="background-image:url('${ART.A}')"></div>
  <div class="end"><h2>六桩公案翻完了</h2><p>漫游模式不判对错、不写星。下面只是每桩公案里「哪条最稳」的读法，看完就走。</p></div>
  <div class="review">${d.cases.map(c=>`<div><b>${esc(c.t)}</b>　最稳：${esc(c.opts[c.a])}<br><span style="color:var(--muted)">${esc(c.why)}</span></div>`).join('')}</div>
  <div class="btnrow" style="margin-top:14px"><button class="btn" data-act="F_start">再翻一遍</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
 }
 if(F.stage==='end'){
  return `<div class="endart" style="background-image:url('${ART.A}')"></div>
  <div class="end"><h2>判准 ${F.right} / ${d.cases.length}</h2>
   <p>${F.right===d.cases.length?'六桩都没被转述带跑——雨驿那夜没给过上帝视角，你也没硬站回去。':'同一件事在不同人嘴里是不同的事，能做的只是拆开、别替任何一边补齐。'}</p></div>
  ${resultBox('F',F.stars||1,'判准 '+F.right+'/'+d.cases.length,F.mistakes)}
  ${F.wrong.length?`<div class="review"><b>没判准的</b>${F.wrong.map(w=>`<div><b>${esc(w.t)}</b>　${esc(w.q)}<br>正解：${esc(w.a)}　（你选了 ${esc(w.yours)}）<br><span style="color:var(--muted)">${esc(w.why)}</span></div>`).join('')}</div>`:''}
  <div class="btnrow" style="margin-top:14px"><button class="btn" data-act="F_start">再审一遍</button>
  <button class="btn ghost" data-act="go" data-v="G">下一关 · 校书局（建议先切 ● 校勘）</button>
  <button class="btn ghost" data-act="go" data-v="hall">回大厅 · 看总进度</button></div>`;
 }
 const c=d.cases[F.i], pct=Math.round(F.i/d.cases.length*100);
 let h=`<div class="bar">${chip}<span class="pill">公案 ${F.i+1} / ${d.cases.length}</span>
  <span class="pill">判准 <b>${F.right}</b></span></div>
  <div class="prog"><i style="width:${pct}%"></i></div>
  <div class="card"><div class="sec">${esc(c.t)}</div>
   <div class="voices"><div class="lab">摆在案上的几条转述</div>
    ${c.voices.map((v,i)=>`<div><em>其${'一二三'[i]||i+1}</em>${esc(v)}</div>`).join('')}</div>
   <div class="qtitle">${esc(c.q)}</div>
   <div class="opts" style="margin-top:10px">${c.opts.map((o,i)=>{
    let cl=F.picked===i?'sel':'';
    if(F.showWhy){if(i===c.a)cl='right';else if(i===F.picked)cl='wrong';}
    return `<button class="opt ${cl}" data-act="F_ans" data-v="${i}" ${F.showWhy?'disabled':''}>${esc(o)}</button>`;}).join('')}</div>
   ${F.showWhy?`<div class="explain"><b>${F.picked===c.a?'判准了':'正解：'+esc(c.opts[c.a])}</b><br>${esc(c.why)}</div>`:''}</div>`;
 if(F.showHint&&!F.showWhy&&showGuide())
  h=`<div class="hintbox"><b>给个方向</b>　先把几条转述拆成「谁说的、他要什么」，再看哪一条没有替谁补齐。</div>`+h;
 h+=`<div class="btnrow"><button class="btn" data-act="F_next" ${F.showWhy?'':'disabled'}>${F.i>=d.cases.length-1?'看结果':'下一桩'}</button>
  ${showGuide()&&!F.showWhy?`<button class="btn ghost sm" data-act="F_hint">${F.showHint?'收起方向':'给个方向'}</button>`:''}
  <button class="btn ghost sm" data-act="F_reset">退出</button>
  <button class="btn ghost sm" data-act="go" data-v="hall">回大厅</button></div>`;
 return h;
}

/* ---------- 通用 Q 引擎：单选 / 排序 / 归类三种操作形态 ---------- */
function qFresh(){
 return {stage:'play',i:0,right:0,wrong:[],picked:null,showWhy:false,showHint:false,end:null,mistakes:0,
         seq:[],assign:{},pickItem:null};
}
function qList(k){ return quizFor(D[k].quiz); }
function qType(q){ return q.type||'single'; }
function qItems(q){
 if(!q.items)return [];
 return qType(q)==='match'?q.items.map(x=>x[0]):q.items;
}
function qSlots(q){ return q.slots||[]; }
function qAnswerText(q){
 if(qType(q)==='order')return q.answer.map(i=>qItems(q)[i]).join(' → ');
 if(qType(q)==='match')return q.items.map(it=>it[0]+' → '+it[1]).join('｜');
 return q.opts[q.a];
}
function qYoursText(k,q){
 const S_=S[k];
 if(qType(q)==='order')return S_.seq.map(i=>qItems(q)[i]).join(' → ')||'（没排完）';
 if(qType(q)==='match'){
  const sl=qSlots(q);
  return q.items.map((it,i)=>it[0]+' → '+(S_.assign[i]===undefined?'未放':sl[S_.assign[i]]||'未放')).join('｜');
 }
 return q.opts[S_.picked]||'（未选）';
}
function qDone(k,q){
 const S_=S[k], t=qType(q);
 if(t==='order')return S_.seq.length===qItems(q).length;
 if(t==='match')return Object.keys(S_.assign).length===qItems(q).length;
 return S_.picked!==null;
}
function qCorrect(k,q){
 const S_=S[k], t=qType(q);
 if(t==='order')return JSON.stringify(S_.seq)===JSON.stringify(q.answer);
 if(t==='match')return q.items.every((it,i)=>S_.assign[i]===qSlots(q).indexOf(it[1]));
 return S_.picked===q.a;
}
function Q_finish(k,q){
 const S_=S[k], ok=qCorrect(k,q);
 S_.showWhy=true;
 if(ok)S_.right++;
 else {
  S_.wrong.push({t:q.sec,q:q.q,a:qAnswerText(q),yours:qYoursText(k,q),why:q.why});
  if(isChallenge())S_.mistakes++;
 }
 render();
}
function Q_ans(k,v){
 const L=qList(k), q=L[S[k].i]; if(!q||S[k].showWhy)return;
 const S_=S[k], t=qType(q);
 if(t==='order'){
  const i=+v; if(isNaN(i)||S_.seq.includes(i))return;
  S_.seq.push(i);
  if(qDone(k,q))Q_finish(k,q); else render();
  return;
 }
 if(t==='match'){
  const sv=String(v);
  if(sv.indexOf('s:')===0){
   const j=+sv.slice(2);
   if(S_.pickItem===null||S_.assign[S_.pickItem]!==undefined||isNaN(j))return;
   S_.assign[S_.pickItem]=j; S_.pickItem=null;
   if(qDone(k,q))Q_finish(k,q); else render();
  }else{
   const i=+sv;
   if(isNaN(i)||S_.assign[i]!==undefined)return;
   S_.pickItem=i; render();
  }
  return;
 }
 S_.picked=+v; Q_finish(k,q);
}
function Q_undo(k){
 const S_=S[k], q=qList(k)[S_.i]; if(!q||S_.showWhy)return;
 if(qType(q)==='order')S_.seq.pop();
 else if(qType(q)==='match'){
  const ks=Object.keys(S_.assign); if(ks.length)delete S_.assign[ks[ks.length-1]];
  S_.pickItem=null;
 }
 render();
}
function Q_clear(k){
 const S_=S[k]; S_.seq=[]; S_.assign={}; S_.pickItem=null; render();
}
function Q_next(k){
 const L=qList(k);
 if(S[k].i>=L.length-1){
  S[k].stage='end'; S[k].end=true;
  let stars=starsByRatio(S[k].right,L.length);
  if(isChallenge()&&S[k].mistakes>challengeAllowance())stars=Math.min(stars,2);
  S[k].stars=stars;
  markClear(k,stars,'判准 '+S[k].right+'/'+L.length+' · '+diffInfo().name);
  save(k,diffInfo().name+' · 已完成'); render();
 } else {
  S[k].i++;S[k].picked=null;S[k].showWhy=false;S[k].showHint=false;
  S[k].seq=[];S[k].assign={};S[k].pickItem=null;render();
 }
}
function Q_hintText(k){
 const L=qList(k), q=L[S[k].i];
 const bank=D[k].hints||[];
 let base=bank[Math.min(S[k].i,bank.length-1)]||'先分清「原著／改编」「原名／结集名」，再看选项里有没有把两件事并成一桩。';
 if(qType(q)==='order')base='排序题：先找首尾，再排中间；点错了用「退一步」。　'+base;
 if(qType(q)==='match')base='归类题：先点左边条目，再点右边槽位；放错了用「退一步」。　'+base;
 return base;
}
function Q_optsHTML(k,q){
 const S_=S[k], t=qType(q), locked=S_.showWhy;
 if(t==='order'){
  const its=qItems(q);
  let h=`<div class="ordseq"><b>你排的顺序</b>　${S_.seq.length?S_.seq.map((i,n)=>`<span class="ordchip">${n+1}. ${esc(its[i])}</span>`).join(''):'<span class="muted">还没开始，逐条点下面</span>'}</div>`;
  h+='<div class="opts">'+its.map((it,i)=>{
   const used=S_.seq.includes(i), n=S_.seq.indexOf(i)+1;
   return `<button class="opt ${used?'sel':''}" data-act="${k}_ans" data-v="${i}" ${used||locked?'disabled':''}>${used?'<b>'+n+'.</b> ':''}${esc(it)}</button>`;
  }).join('')+'</div>';
  if(!locked)h+=`<div class="btnrow smrow"><button class="btn ghost sm" data-act="${k}_undo">退一步</button><button class="btn ghost sm" data-act="${k}_clear">清空重排</button></div>`;
  return h;
 }
 if(t==='match'){
  const its=qItems(q), sl=qSlots(q);
  let h='<div class="matchwrap"><div class="mcol"><div class="lab">条目（先点）</div>'+its.map((it,i)=>{
   const done=S_.assign[i]!==undefined, pick=S_.pickItem===i;
   return `<button class="opt ${pick?'pick':''} ${done?'sel':''}" data-act="${k}_ans" data-v="${i}" ${done||locked?'disabled':''}>${esc(it)}${done?'　→ '+esc(sl[S_.assign[i]]):''}</button>`;
  }).join('')+'</div><div class="mcol"><div class="lab">槽位（再点）</div>'+
   sl.map((s,j)=>`<button class="opt slot" data-act="${k}_ans" data-v="s:${j}" ${locked?'disabled':''}>${esc(s)}</button>`).join('')+'</div></div>';
  if(!locked)h+=`<div class="btnrow smrow"><button class="btn ghost sm" data-act="${k}_undo">退一步</button><button class="btn ghost sm" data-act="${k}_clear">清空重放</button></div>`;
  return h;
 }
 return '<div class="opts" style="margin-top:10px">'+q.opts.map((o,i)=>{
  let cl=S_.picked===i?'sel':'';
  if(locked){if(i===q.a)cl='right';else if(i===S_.picked)cl='wrong';}
  return `<button class="opt ${cl}" data-act="${k}_ans" data-v="${i}" ${locked?'disabled':''}>${esc(o)}</button>`;
 }).join('')+'</div>';
}
function renderQ(k){
 const S_=S[k], d=D[k], L=qList(k);
 const chip=`<span class="modechip ${showGuide()?'':'n'}">${modeInfo().icon} ${modeInfo().name}</span>`;
 const dchip=`<span class="modechip" style="background:var(--purple);color:#fff">${diffInfo().icon} ${diffInfo().name} · ${L.length} 题</span>`;
 if(S_.stage==='intro')return `${artBanner(d.art,'水墨意境 · '+d.sub)}
  <div class="hero"><h2>${esc(d.title)}</h2>
  <div class="kind" style="font-size:12px;color:var(--purple);margin-bottom:10px">${esc(d.sub)}　／　${L.length} 题（${esc(diffNote())}）　／　${esc(d.form||'辨认')}</div>
  <p>${nl(d.intro)}</p>
  <div class="bar" style="margin:0 0 10px"><span class="pill">当前模式</span>${chip}${dchip}
   <span class="pill">★ ${(PROG[k]||{}).stars||0}/3</span></div>
  <div class="note"><b>难度怎么影响这一关</b>　浅读只出 ${D[k].quiz.filter(q=>qTier(q)<=1).length} 道基础题，通读 ${D[k].quiz.filter(q=>qTier(q)<=2).length} 道，校勘才开全部 ${D[k].quiz.length} 道（含连载、异文、人事与改编考据）。星级阈值也随难度收紧。</div>
  <div class="btnrow" style="margin-top:12px"><button class="btn" data-act="${k}_start">开始</button>
   <button class="btn ghost" data-act="go" data-v="hall">回大厅改难度</button></div></div>`;
 if(S_.stage==='end'){
  if(isRoam())return `<div class="endart" style="background-image:url('${ART[d.art]}')"></div>
   <div class="end"><h2>${esc(d.title)} · 翻完了</h2><p>漫游模式不判定、不写星。下面把这一档难度下每题的最稳读法列齐，看完就走。</p></div>
   <div class="review">${L.map(q=>`<div><b>${esc(q.sec)}｜${esc(q.q)}</b><br>最稳：${esc(qAnswerText(q))}<br><span style="color:var(--muted)">${esc(q.why)}</span></div>`).join('')}</div>
   <div class="btnrow" style="margin-top:14px"><button class="btn" data-act="${k}_start">再翻一遍</button>
    <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
  return `<div class="endart" style="background-image:url('${ART[d.art]}')"></div>
  <div class="end"><h2>判准 ${S_.right} / ${L.length}</h2>
   <p>${S_.right===L.length?'这一档全对了。考据题最忌替资料补齐，你没补。':'错的几题留着比分数有用：二手转述最爱把两桩并成一桩。'}</p></div>
  ${resultBox(k,S_.stars||1,'判准 '+S_.right+'/'+L.length+' · '+diffInfo().name,S_.mistakes)}
  ${S_.wrong.length?`<div class="review"><b>没判准的</b>${S_.wrong.map(w=>`<div><b>${esc(w.t)}｜${esc(w.q)}</b><br>正解：${esc(w.a)}　（你选了 ${esc(w.yours)}）<br><span style="color:var(--muted)">${esc(w.why)}</span></div>`).join('')}</div>`:''}
  <div class="btnrow" style="margin-top:14px"><button class="btn" data-act="${k}_start">再来</button>
   ${k==='G'?'<button class="btn ghost" data-act="go" data-v="H">下一关 · 辕门簿</button>':k==='H'?'<button class="btn ghost" data-act="go" data-v="I">下一关 · 改编鉴</button>':''}
   <button class="btn ghost" data-act="go" data-v="hall">回大厅</button></div>`;
 }
 const q=L[S_.i], pct=Math.round(S_.i/L.length*100);
 let h=`<div class="bar">${chip}${dchip}<span class="pill">${S_.i+1} / ${L.length}</span>
  <span class="pill">判准 <b>${S_.right}</b></span><span class="pill">tier ${qTier(q)}</span>
  <span class="pill">${({'single':'单选','order':'排序','match':'归类'})[qType(q)]}</span></div>
  <div class="prog"><i style="width:${pct}%"></i></div>`;
 if(S_.showHint&&!S_.showWhy&&showGuide())
  h+=`<div class="hintbox"><b>给个方向</b>　${esc(Q_hintText(k))}</div>`;
 h+=`<div class="card"><div class="sec">${esc(q.sec)}　·　第 ${qTier(q)} 层</div><div class="qtitle">${esc(q.q)}</div>
  ${Q_optsHTML(k,q)}
  ${S_.showWhy?`<div class="explain"><b>${qCorrect(k,q)?'判准了':'正解：'+esc(qAnswerText(q))}</b>${qCorrect(k,q)?'':'　（你的：'+esc(qYoursText(k,q))+'）'}<br>${esc(q.why)}</div>`:''}</div>`;
 h+=`<div class="btnrow"><button class="btn" data-act="${k}_next" ${S_.showWhy?'':'disabled'}>${S_.i>=L.length-1?'看结果':'下一题'}</button>
  ${showGuide()&&!S_.showWhy?`<button class="btn ghost sm" data-act="${k}_hint">${S_.showHint?'收起方向':'给个方向'}</button>`:''}
  <button class="btn ghost sm" data-act="${k}_reset">退出</button>
  <button class="btn ghost sm" data-act="go" data-v="hall">回大厅</button></div>`;
 return h;
}

/* ---------- 档案：随关卡逐步解锁 ---------- */
function renderArchive(){
 const au=archUnlockedCount(), at=archTotal();
 const cur=D.meta.archDefs.find(x=>x.id===ARCH)||D.meta.archDefs[0];
 const un=archUnlocked(cur);
 let body='';
 if(!un){
  const firstTodo=D.meta.levels.find(l=>!(PROG[l.id]||{}).done);
  const go=cur.need==='ALL'?(firstTodo?firstTodo.id:'V'):cur.need;
  body=`<div class="lockcard"><span class="ico">🔒</span>
   <h3>《${esc(cur.label)}》尚未解锁</h3>
   <p>档案不一次全摊开。通关对应关卡，这一页才亮；资料本身早就离线收在里面了，只是按读的顺序慢慢给。</p>
   <div class="need">需要：${esc(archNeedLabel(cur))}</div>
   <div class="btnrow" style="margin-top:14px;justify-content:center">
    <button class="btn" data-act="go" data-v="${go}">去走这一关</button></div></div>`;
 }else if(cur.id==='intro'){
  body=`<h2>档案怎么开</h2>
   <p>这套拆读不一次全摊开。二十四关按卷逐步开页——先认人，再听雨，最后才轮到版本、人事、改编与待补清单。</p>
   <p>顺序是照阅读走的：人物谱系 → 时间轴 → 地理 → 真词笺 → 番外 → 电影 → 版本年表 → 辕门簿 → 改编对照 → <b>章句卷 · 人物卷 · 武学卷 · 世道卷 · 改编卷</b> → 待补。后五卷是本轮续检索后新补的，每卷由该卷首关开启；全部离线内嵌，不含小说原文。</p>
   <h3>解锁表</h3>
   ${D.meta.archDefs.filter(d=>d.need).map(d=>{
    const l=D.meta.levels.find(x=>x.id===d.need);
    const done=d.need==='ALL'?allCleared():archUnlocked(d);
    return `<div class="archrow ${done?'op':''}"><span>${done?'🔓':'🔒'} ${esc(d.label)}</span>
     <span>${d.need==='ALL'?'二十四关全通':esc(l?l.no+'《'+l.t+'》':'')}</span></div>`;
   }).join('')}
   <p style="font-size:11px;color:var(--muted);margin-top:12px">漫游模式不写星、也不解锁档案；想开资料页，切到新手／普通／挑战再走一遍对应关卡即可。已解锁的页不会重新锁上。</p>`;
 }else if(cur.id==='read'){
  body='<div class="embed-note" style="font-size:11px;color:var(--muted);margin-bottom:8px">交互拆读站已内嵌离线运行：点人物看关系、展开逐回讲稿、翻速查表。关系图默认缩到一屏可见，可放大后左右拖动。</div><iframe id="if-read" title="交互拆读站" scrolling="no"></iframe>';
 }else{
  body=(D.archive&&D.archive[cur.id])||
       (D.archiveExtra&&D.archiveExtra[cur.id])||
       '<div class="note">这一页暂无内容。</div>';
 }
 return `<div class="hero"><h2>档案 · 逐步解锁</h2>
  <p>游戏之外留的一间书房。通关一关，开一页；全部离线内嵌，不含小说原文。</p></div>
  <div class="archprog"><div class="row"><span>已解锁</span><b>${au} / ${at} 页</b></div>
   <div class="track"><i style="width:${Math.round(au/at*100)}%"></i></div></div>
  <div class="archtabs">${D.meta.archDefs.map(d=>`<button data-act="arch_tab" data-v="${d.id}" class="${ARCH===d.id?'on':''} ${archUnlocked(d)?'':'locked'}">${esc(d.label)}</button>`).join('')}</div>
  <div class="archbody">${body}</div>
  <div class="btnrow" style="margin-top:12px"><button class="btn" data-act="go" data-v="hall">回大厅继续玩</button></div>`;
}
function mountRead(){
 if(ARCH!=='read')return;
 const f=$('#if-read'); if(!f)return;
 try{
  const bin=atob(D.readB64), bytes=Uint8Array.from(bin,c=>c.charCodeAt(0));
  f.onload=()=>{ try{ const d=f.contentDocument;
   if(d)f.style.height=(Math.max(520,d.documentElement.scrollHeight||d.body.scrollHeight)+24)+'px'; }catch(e){} };
  f.srcdoc=new TextDecoder('utf-8').decode(bytes);
 }catch(e){ f.srcdoc='<p style="padding:20px">拆读站载入失败，请回大厅重试。</p>'; }
}

/* 拆读站放大/缩放后同步 iframe 高度 */
window.addEventListener('message',e=>{
 if(e.data&&e.data.k==='bx-read-h'){
  const f=$('#if-read'); if(f)f.style.height=(Math.max(520,+e.data.h||520)+24)+'px';
 }
});

applyA11y(); applySkin(); document.body.classList.toggle('no-breathe',!BREATHE); syncLandBtn(); renderLandTip(); syncHctl(); renderModePanel(); renderDiffPanel(); renderSkinPanel();
/* 朗读与语音控制默认关闭、不持久化；这里只把面板内容备好，用户点开时再渲染 */
renderA11yPanel();
/* 上次若开着背景音，需用户首次交互后才能恢复（浏览器自动播放限制） */
if(BGM>0){ document.body.addEventListener('click',function once(){ setBGM(BGM); document.body.removeEventListener('click',once); },{once:true}); }

/* ---------- R6：图片查看器（双指缩放 / 拖动 / 双击复位） ---------- */
const bxV=$('#bxViewer'), bxImg=$('#bxvImg'), bxStage=$('#bxvStage');
let VS={s:1,x:0,y:0}, vPts=new Map(), vLast=null, vDist=0;
function vApply(){ bxImg.style.transform='translate('+VS.x+'px,'+VS.y+'px) scale('+VS.s+')'; }
function vZoom(f){ VS.s=Math.max(.4,Math.min(6,VS.s*f)); vApply(); }
function vReset(){ VS={s:1,x:0,y:0}; vApply(); }

const vBg=$('#vBg'), vCut=$('#vCut'), vHitBg=$('#vHitBg'), vHitCast=$('#vHitCast'), vPicker=$('#vPicker');
let VSTATE={mode:'img',bg:'rain',cast:'cos_base',from:'hall',dirty:0,
  bgT:{x:0,y:0,s:1},castT:{x:0,y:0,s:1}};
let VCAST_OVER={}, VBG_OVER={};   /* 长按选择后对当前关卡/大厅的临时覆盖（会话内） */
function vApplyComp(){
 if(vBg)vBg.style.transform='translate('+VSTATE.bgT.x+'px,'+VSTATE.bgT.y+'px) scale('+VSTATE.bgT.s+')';
 if(vCut)vCut.style.transform='translate('+VSTATE.castT.x+'px,'+VSTATE.castT.y+'px) scale('+VSTATE.castT.s+')';
}
function vApplyLayers(){
 if(!vBg||!vCut)return;
 const isComp=VSTATE.mode==='comp';
 vBg.hidden=!isComp;vCut.hidden=!isComp;
 vHitBg.hidden=!isComp;vHitCast.hidden=!isComp;
 bxImg.hidden=isComp;
 bxV.classList.toggle('composite',isComp);
 if(isComp){
  vBg.style.backgroundImage="url('"+(ART['bg_'+VSTATE.bg]||ART.bg_rain)+"')";
  vCut.style.backgroundImage="url('"+(ART[VSTATE.cast]||ART.cos_base)+"')";
  vApplyComp();
 }
 document.body.classList.toggle('viewer-open',!bxV.hidden);
}
function openComposite(bgKey,castKey,label,from){
 suspendRotForViewer();
 VSTATE={mode:'comp',bg:bgKey||'rain',cast:origCast(castKey||'cos_base'),from:from||'hall',dirty:0,
  bgT:{x:0,y:0,s:1},castT:{x:0,y:0,s:1}};
 $('#bxvLabel').textContent=label||'场景与立绘';
 bxV.hidden=false; bxV.classList.add('fullbleed');
 vApplyLayers(); vib(12);
 try{document.body.style.overflow='hidden';}catch(e){}
}
function closeViewer(){
 restoreRotForViewer();
 const wasComp=VSTATE.mode==='comp';
 bxV.hidden=true; bxV.classList.remove('fullbleed','composite');
 bxImg.removeAttribute('src'); bxImg.hidden=false; vPicker.hidden=true;
 document.body.classList.remove('viewer-open');
 try{document.body.style.overflow='';}catch(e){}
 if(wasComp&&VSTATE.dirty){
  if(VSTATE.from==='hall'){
   HH_BG=VSTATE.bg; try{localStorage.setItem(HBGKEY,VSTATE.bg);}catch(e){}
   VCAST_OVER.hall=VSTATE.cast;      /* 新表情不在引导员表里也能生效 */
   const hit=CATCOST.find(x=>x[2]===VSTATE.cast);
   if(hit)CATFIX=hit[0];
  }else{
   VBG_OVER[VSTATE.from]=VSTATE.bg; VCAST_OVER[VSTATE.from]=VSTATE.cast;
  }
  render();
 }
}

/* R8：全屏查看时把「当前选中的场景板 + 角色层」合成一张按视口比例的画面 */
function composeFull(bgKey,castKey,label){
 return new Promise(res=>{
  const cv=document.createElement('canvas');
  const W=Math.min(1440,Math.max(720,innerWidth*2)), H=Math.min(2800,Math.max(1080,innerHeight*2));
  cv.width=W; cv.height=H; const ctx=cv.getContext('2d');
  const bg=new Image(), fg=new Image(); let n=0;
  const done=()=>{
   if(++n<2)return;
   ctx.fillStyle='#1B1916';ctx.fillRect(0,0,W,H);
   const sc=Math.max(W/bg.width,H/bg.height), bw=bg.width*sc, bh=bg.height*sc;
   ctx.drawImage(bg,(W-bw)/2,(H-bh)/2,bw,bh);
   const tw=W*.86, th=H*.66, fs=Math.min(tw/fg.width,th/fg.height);
   const fw=fg.width*fs, fh=fg.height*fs;
   ctx.drawImage(fg,(W-fw)/2,H-fh-H*.035,fw,fh);
   res(cv.toDataURL('image/jpeg',.88));
  };
  bg.onload=done; fg.onload=done; bg.onerror=done; fg.onerror=done;
  bg.src=ART['bg_'+bgKey]||ART.bg_rain; fg.src=ART[castKey]||ART.cos_base;
 });
}
function openHallFull(){
 const ck=VCAST_OVER.hall||origCast(CATFIX?fixedKey():avatarKey());
 const bl=(BGLIST.find(x=>x[0]===HH_BG)||['','雨驿雨夜'])[1];
 const lab='场景 '+bl+' · '+(CAST.find(x=>x[0]===ck)||['','本色'])[1];
 openComposite(HH_BG,ck,lab,'hall');
}
function openStageFull(){
 const s=stageFor(TAB);
 const bl=(BGLIST.find(x=>x[0]===s.bg)||['','雨驿雨夜'])[1];
 const lab='场景 '+bl+' · '+(CAST.find(x=>x[0]===s.cast)||['','本色'])[1];
 openComposite(s.bg,s.cast,lab,TAB);
}
function openViewer(src,label,fullbleed){
 if(!src)return;
 suspendRotForViewer();
 $('#bxvLabel').textContent=label||'图片查看';
 VSTATE.mode='img';bxImg.src=src;bxImg.alt=label||'可缩放图片';
 bxV.classList.toggle('fullbleed',!!fullbleed);
 bxV.hidden=false;vApplyLayers();vReset();
 try{document.body.style.overflow='hidden';}catch(e){}
}


/* ---------- R9：长按场景 / 立绘 → 选择面板 ---------- */
function openVPicker(which){
 if(VSTATE.mode!=='comp')return;
 let items='';
 if(which==='bg'){
  items=BGLIST.map(([v,l],i)=>{
   const u=bgUnlocked(i);
   return `<button class="vpick ${VSTATE.bg===v?'on':''} ${u?'':'lock'}" data-act="v_pick_bg" data-v="${v}"
    ${u?`style="background-image:url('${ART['bg_'+v]||''}')"`:''}
    aria-label="${u?'场景 '+l:'🔒 通关第 '+bgNeed(i)+' 关解锁'}">${u?esc(l):'🔒 '+l+' <em>'+bgNeed(i)+'关</em>'}</button>`;
  }).join('');
 }else{
  items=CAST.map(([k,l],i)=>{
   /* 前 27 项是可引导员人物（按进度解锁）；其后是表演表情层，始终可用 */
   const u=(i>=CATCOST.length)||castUnlocked(i,CAST.length);
   return `<button class="vpick cast ${VSTATE.cast===k?'on':''} ${u?'':'lock'}" data-act="v_pick_cast" data-v="${k}"
    ${u?`style="background-image:url('${ART[k]||''}')"`:''}
    aria-label="${u?'人物表情 '+l:'🔒 通关第 '+castNeed(i,CAST.length)+' 关解锁'}">${u?esc(l):'🔒 '+l}</button>`;
  }).join('');
 }
 vPicker.innerHTML=`<div class="vph"><b>◈ 长按 · 选${which==='bg'?'场景':'人物表情'}</b>
   <button data-act="v_picker_close" aria-label="关闭选择面板">✕</button></div>
  <div class="vpgrid">${items}</div>
  <div class="vpf">选完立即换到全屏画面，关闭查看器后同步到${VSTATE.from==='hall'?'大厅':'当前关卡'}；🔒 随通关进度开放。</div>`;
 vPicker.hidden=false; vib(16);
}

function openViewerFrom(sel){
 const el=document.querySelector(sel||'.stagecut'); if(!el)return;
 const bg=getComputedStyle(el).backgroundImage;
 const m=bg&&bg.match(/url\(["']?(.*?)["']?\)/);
 const src=(m?m[1]:el.getAttribute('src'))||'';
 const lab=(el.getAttribute('aria-label')||'角色立绘').slice(0,50);
 openViewer(src,lab);
}
let VDRAG={pts:new Map(),which:'bg',dist:0,moved:false,long:null,start:null};
function vTarget(e){ return e.target.closest('#vHitCast')?'cast':'bg'; }
function vCancelLong(){ if(VDRAG.long){clearTimeout(VDRAG.long);VDRAG.long=null;} }
function vT(which){ return which==='cast'?VSTATE.castT:VSTATE.bgT; }
function vSpring(which){
 const t=vT(which);
 const el=which==='cast'?vCut:vBg; if(!el)return;
 el.classList.add('vspring');setTimeout(()=>el.classList.remove('vspring'),340);
}
function vZoomComp(f,which){
 const t=vT(which); t.s=Math.max(.45,Math.min(4,t.s*f)); vApplyComp(); vSpring(which);
}
function vResetComp(){ VSTATE.bgT={x:0,y:0,s:1};VSTATE.castT={x:0,y:0,s:1};vApplyComp(); }
/* R10：旋转横屏时 fixed 查看器会跟着 body 转 90°，界面侧倒、坐标错乱。
   打开查看器期间临时摘掉旋转类，让全屏永远按设备正向显示；关闭时原样恢复。 */
let VIEWER_SAVED_ROT=0;
function suspendRotForViewer(){
 if(document.documentElement.classList.contains('rot-landscape')){
  VIEWER_SAVED_ROT=1; document.documentElement.classList.remove('rot-landscape');
 }
}
function restoreRotForViewer(){
 if(VIEWER_SAVED_ROT){ VIEWER_SAVED_ROT=0; document.documentElement.classList.add('rot-landscape'); }
}
function vLimits(){
 const st=bxStage||document.querySelector('#bxvStage');
 const W=st?st.clientWidth:innerWidth, H=st?st.clientHeight:innerHeight;
 return {x:W*.42,y:H*.36};
}
function vClampLayer(which){
 const t=vT(which), lim=vLimits();
 const x=Math.max(-lim.x,Math.min(lim.x,t.x)), y=Math.max(-lim.y,Math.min(lim.y,t.y));
 if(x!==t.x||y!==t.y){t.x=x;t.y=y;vApplyComp();vSpring(which);}
}
function vClampAll(){ vClampLayer('bg');vClampLayer('cast'); }
if(bxStage){
 /* R17：之前只在 comp（双层合成）模式处理 pointer，openViewer 默认的 img 模式
    （点大厅预览图／关系图／人物立绘进的都是它）只有滚轮缩放，双指完全无效。 */
 bxStage.addEventListener('pointerdown',e=>{
  if(VSTATE.mode!=='comp'&&VSTATE.mode!=='img')return;
  if(!vPicker.hidden){vPicker.hidden=true;}
  const which=vTarget(e);
  if(VDRAG.pts.size===0){ VDRAG.which=which; VDRAG.moved=false;
   VDRAG.start={x:e.clientX,y:e.clientY};
   if(VSTATE.mode==='comp')
    VDRAG.long=setTimeout(()=>{ if(!VDRAG.moved){openVPicker(which);vib(14);} },540);
  }
  VDRAG.pts.set(e.pointerId,{x:e.clientX,y:e.clientY});
  try{bxStage.setPointerCapture(e.pointerId);}catch(err){}
  if(VDRAG.pts.size===2){const p=[...VDRAG.pts.values()];VDRAG.dist=Math.hypot(p[0].x-p[1].x,p[0].y-p[1].y);}
 },true);
 bxStage.addEventListener('pointermove',e=>{
  if(VSTATE.mode!=='comp'&&VSTATE.mode!=='img')return;
  const p=VDRAG.pts.get(e.pointerId); if(!p)return;
  const dX=e.clientX-p.x, dY=e.clientY-p.y;
  p.x=e.clientX;p.y=e.clientY;
  if(Math.abs(dX)+Math.abs(dY)>2){VDRAG.moved=true;vCancelLong();}
  const q=[...VDRAG.pts.values()];
  const d=VDRAG.pts.size>=2?Math.hypot(q[0].x-q[1].x,q[0].y-q[1].y):0;
  if(VDRAG.pts.size>=2){
   /* 两点距离旋转不变，不用换轴 */
   if(VSTATE.mode==='img'){
    if(VDRAG.dist>0){VS.s=Math.max(.4,Math.min(6,VS.s*d/VDRAG.dist));vApply();}
   }else{
    const t=vT(VDRAG.which);
    if(VDRAG.dist>0){t.s=Math.max(.45,Math.min(4,t.s*d/VDRAG.dist));vApplyComp();}
   }
   VDRAG.dist=d; return;
  }
  const rot=document.documentElement.classList.contains('rot-landscape');
  const dx=rot?dY:dX, dy=rot?-dX:dY;
  if(VSTATE.mode==='img'){ VS.x+=dx;VS.y+=dy;vApply(); }
  else{
   const t=vT(VDRAG.which), lim=vLimits();
   t.x=Math.max(-lim.x,Math.min(lim.x,t.x+dx));
   t.y=Math.max(-lim.y,Math.min(lim.y,t.y+dy));
   vApplyComp();
  }
 },true);
 ['pointerup','pointercancel'].forEach(ev=>bxStage.addEventListener(ev,e=>{
  VDRAG.pts.delete(e.pointerId);vCancelLong();
  if(VDRAG.pts.size===0){
   VDRAG.dist=0;VDRAG.moved=false;
   if(VSTATE.mode==='comp')vClampAll();
   vib(10);
  }
 },true));
 bxStage.addEventListener('wheel',e=>{e.preventDefault();
  if(VSTATE.mode==='comp')vZoomComp(e.deltaY<0?1.12:1/1.12,'bg');else vZoom(e.deltaY<0?1.12:1/1.12);
 },{passive:false});
 bxStage.addEventListener('dblclick',()=>{
  if(VSTATE.mode==='comp'){vResetComp();vib(12);}else vReset();
 });
}

/* 点击任意可缩放图片（大厅主视觉、角色设定图等）进查看器 */
document.addEventListener('click',e=>{
 const z=e.target.closest('[data-zoomable]'); if(!z||e.target.closest('[data-act]'))return;
 const bg=getComputedStyle(z).backgroundImage, m=bg&&bg.match(/url\(["']?(.*?)["']?\)/);
 const src=(m?m[1]:z.getAttribute('src'))||'';
 if(src)openViewer(src,(z.getAttribute('aria-label')||'图片查看').slice(0,50));
});

/* R24：名牌拼接去重 —— CAST 第二项（如「荆三娘 · 深褐单高髻假发」）已含角色名，
   再拼 castMeta[0] 会变成「荆三娘 · 荆三娘 · 深褐单高髻假发」。 */
function whoLine(cast){
 const nm=(castMeta(cast)||['',''])[0];
 const cl=(CAST.find(x=>x[0]===cast)||['',''])[1];
 if(!nm)return cl||'哈士喵';
 if(cl&&cl.indexOf(nm)===0)return cl;
 return nm+(cl?' · '+cl:'');
}
/* ---------- R6：立绘拖动 + 双指缩放 + 拖动小动画 ---------- */
const SPRKEY='beixue_spr_v1';
function bubbleTop(){
 const q=document.querySelector('#app .avgframe>.avgbubble');
 if(q){const r=q.getBoundingClientRect();if(r.height>40)return r.top;}
 return innerHeight*0.62;
}
function sprSafeDeltas(dx,dy){
 /* R17：旋转画布下屏幕矩形与局部坐标不同系，阻尼会越扯越远，直接放行 */
 if(document.documentElement.classList.contains('rot-landscape'))return {dx:dx,dy:dy};
 const el=document.querySelector('#app .stagecut'); if(!el)return {dx:dx,dy:dy};
 const r=el.getBoundingClientRect(), W=innerWidth, H=innerHeight, bt=bubbleTop();
 const damp=.22;
 let ox=0,oy=0;
 if(r.left+dx < -W*.08)ox=(-W*.08-r.left)-dx;
 if(r.right+dx > W*1.08)ox=(W*1.08-r.right)-dx;
 if(r.top+dy < -H*.04)oy=(-H*.04-r.top)-dy;
 if(r.bottom+dy > bt+(H-bt)*.18)oy=(bt+(H-bt)*.18-r.bottom)-dy;
 return {dx:dx+(ox?ox*damp:0),dy:dy+(oy?oy*damp:0)};
}
function clampSpr(){
 const el=document.querySelector('#app .stagecut'); if(!el)return false;
 const rot=document.documentElement.classList.contains('rot-landscape');
 if(rot){ /* R24：旋转后 getBoundingClientRect 是屏幕矩形、与 SPR 局部坐标不同系。
            旧写法每次松手 SPR.x*=.35 会把拖动立刻拉回 → 表现为「拖不动」。
            改用 .stage 的局部尺寸做软边界，倍率与位置都保留。 */
   const st=document.querySelector('#app .avgframe>.stage');
   const LW=(st&&st.clientWidth)||900, LH=(st&&st.clientHeight)||420;
   const limX=LW*.16, limY=LH*.14;
   const nx=Math.max(-limX,Math.min(limX,SPR.x)), ny=Math.max(-limY,Math.min(limY,SPR.y));
   if(nx===SPR.x&&ny===SPR.y)return false;
   SPR.x=nx;SPR.y=ny;applySpr();saveSpr();
   el.classList.add('springing');setTimeout(()=>el.classList.remove('springing'),360);
   return true;
 }
 const r=el.getBoundingClientRect(), W=innerWidth, H=innerHeight, bt=bubbleTop();
 let dX=0,dY=0;
 if(r.left < -W*.08)dX=-W*.08-r.left;
 else if(r.right > W*1.08)dX=W*1.08-r.right;
 if(r.top < -H*.04)dY=-H*.04-r.top;
 else if(r.bottom > bt+(H-bt)*.18)dY=bt+(H-bt)*.18-r.bottom;
 if(!dX&&!dY)return false;
 SPR.x+=dX;SPR.y+=dY;
 applySpr();saveSpr();
 el.classList.add('springing');setTimeout(()=>el.classList.remove('springing'),360);
 return true;
}
function ensureSpriteVisible(){
 const el=document.querySelector('#app .stagecut'); if(!el)return;
 const rot=document.documentElement.classList.contains('rot-landscape');
 if(rot){ /* R24：旋转后设备 innerWidth/innerHeight 与局部画布宽高互换，
            旧逻辑会误判「不可见」并把 SPR 复位；只在偏移过大时归零，保留倍率。 */
   const st=document.querySelector('#app .avgframe>.stage');
   const LW=(st&&st.clientWidth)||900, LH=(st&&st.clientHeight)||420;
   if(Math.abs(SPR.x)>LW*.16||Math.abs(SPR.y)>LH*.14){
    SPR={x:0,y:0,s:SPR.s};applySpr();saveSpr();
    el.classList.add('springing');setTimeout(()=>el.classList.remove('springing'),360);
   }
   return;
 }
 const r=el.getBoundingClientRect(), W=innerWidth, H=innerHeight, bt=bubbleTop();
 const visible=Math.max(0,Math.min(r.right,W)-Math.max(r.left,0))*Math.max(0,Math.min(r.bottom,H)-Math.max(r.top,0));
 const area=Math.max(1,r.width*r.height);
 if(visible/area<.28 || r.top>bt || r.bottom<0 || r.right<0 || r.left>W){
  SPR={x:0,y:0,s:SPR.s};applySpr();saveSpr();   /* R17：复位位置但保留双指缩放倍率 */
  el.classList.add('springing');setTimeout(()=>el.classList.remove('springing'),360);
 }
}
let SPR={x:0,y:0,s:1};
try{const _v=localStorage.getItem(SPRKEY);if(_v){const o=JSON.parse(_v);
 if(o&&typeof o.x==='number')SPR={x:o.x,y:o.y,s:Math.max(.6,Math.min(2.2,o.s||1))};}}catch(e){}
function saveSpr(){try{localStorage.setItem(SPRKEY,JSON.stringify(SPR));}catch(e){}}
function applySpr(){
 const rs=document.documentElement.style;
 rs.setProperty('--sx',SPR.x+'px');rs.setProperty('--sy',SPR.y+'px');rs.setProperty('--ss',SPR.s);
}
applySpr();
let sPts=new Map(), sLast=null, sDist=0, sMoved=false, sTimer=null;
function spriteEl(t){return t&&t.closest?t.closest('.sprhit'):null;}
document.addEventListener('pointerdown',e=>{
 /* R17：第一根手指必须落在热区；第二根只要还在舞台内就接受。
    之前 ACTIVE_DRAG 把第二根直接 return，sPts 永远 size=1，双指分支从不执行。 */
 const el=spriteEl(e.target);
 if(sPts.size===0){
  if(!el||ACTIVE_DRAG)return;
 }else{
  if(sPts.size>=2)return;
  if(!(e.target.closest&&e.target.closest('.avgframe')))return;
 }
 const capEl=el||document.querySelector('#app .sprhit');
 sPts.set(e.pointerId,{x:e.clientX,y:e.clientY});sMoved=false;
 ACTIVE_DRAG=1; vib(8);
 try{if(capEl)capEl.setPointerCapture(e.pointerId);}catch(err){}
 if(sPts.size===2){const p=[...sPts.values()];sDist=Math.hypot(p[0].x-p[1].x,p[0].y-p[1].y);
  const sc=document.querySelector('#app .stagecut');if(sc)sc.classList.remove('dragging');}
},true);
document.addEventListener('pointermove',e=>{
 const p=sPts.get(e.pointerId); if(!p)return;
 const dX=e.clientX-p.x, dY=e.clientY-p.y;
 p.x=e.clientX;p.y=e.clientY;
 const rot=document.documentElement.classList.contains('rot-landscape');
 const dx=rot?dY:dX, dy=rot?-dX:dY;   /* 画布转 90° 后设备坐标要换轴 */
 if(sPts.size===1){
  if(Math.abs(dX)+Math.abs(dY)>1)sMoved=true;
  const safe=sprSafeDeltas(dx,dy);      /* 设备位移 → 允许的 SPR 位移（软阻尼） */
  SPR.x+=safe.dx;SPR.y+=safe.dy;applySpr();
  const el=document.querySelector('#app .stagecut');
  if(el){el.classList.add('dragging');clearTimeout(sTimer);
   document.documentElement.style.setProperty('--tilt',Math.max(-5,Math.min(5,dx*0.09)).toFixed(1)+'deg');
   sTimer=setTimeout(()=>{el.classList.remove('dragging');
    document.documentElement.style.setProperty('--tilt','0deg');},420);}
 }else if(sPts.size===2){
  /* 两点距离在 90° 旋转下不变，无需换轴；只缩放，不做单指位移 */
  const q=[...sPts.values()], d=Math.hypot(q[0].x-q[1].x,q[0].y-q[1].y);
  if(sDist>0){SPR.s=Math.max(.6,Math.min(2.2,SPR.s*(d/sDist)));applySpr();}
  sDist=d; sMoved=true;
  const sc=document.querySelector('#app .stagecut');if(sc)sc.classList.remove('dragging');
 }
},true);
['pointerup','pointercancel'].forEach(ev=>document.addEventListener(ev,e=>{
 if(!sPts.has(e.pointerId))return;
 sPts.delete(e.pointerId);
 if(sPts.size>0){ sDist=0; return; }   /* 还有手指按着，等最后一根抬起再收尾 */
 sDist=0;
 const el=document.querySelector('#app .stagecut');
 if(el)el.classList.remove('dragging');
 document.documentElement.style.setProperty('--tilt','0deg');
 ACTIVE_DRAG=0; vib(10);
 if(sMoved){
  clampSpr();                          /* 越界就弹回来（横屏保留倍率） */
  saveSpr();
  if(el){el.classList.add('settled');setTimeout(()=>el.classList.remove('settled'),640);}
  announce('立绘缩放至 '+Math.round(SPR.s*100)+'%，设置里可复位');
 }else if(el){   /* 轻点立绘：弹跳回应 + 震动，不是拖动 */
  el.classList.add('tapped');setTimeout(()=>el.classList.remove('tapped'),640);
  vib(14);
 }
 sMoved=false;
},true));
/* 双击立绘进查看器 */
document.addEventListener('dblclick',e=>{ if(spriteEl(e.target))openStageFull(); });

/* ---------- R7：每个选项都有立绘表演跟进 ---------- */
let PERF_T=null, PERF_BACK=null;
function queuePerf(idx){
 clearTimeout(PERF_T);
 PERF_T=setTimeout(()=>{
  const el=document.querySelector('#app .stagecut'); if(!el)return;
  const m=OPT_MOODS[((idx%4)+4)%4];
  const lv=Math.max(0,D.meta.levels.findIndex(l=>l.id===TAB));
  let mi=(lv+idx)%m.arts.length, key=m.arts[mi];
  const base=stageFor(TAB).cast||'';
  const root=k=>k.split('_').slice(0,2).join('_');   /* 尽量换成与当前立绘不同的人物，表演才看得见 */
  if(root(key)===root(base)){ mi=(mi+1)%m.arts.length; key=m.arts[mi]; }
  if(!ART[key])return;
  el.style.backgroundImage="url('"+ART[key]+"')";
  emitStage('perf',{lv:TAB,idx:idx,art:key,anim:m.anim});
  el.classList.remove('perf-nod','perf-shake','perf-guard','perf-lean');
  el.classList.add('perf-'+m.anim);
  const ic=document.querySelector('#app .perficon');
  if(ic){ ic.className='perficon '+(m.anim==='nod'?'ic-nod':m.anim==='shake'?'ic-shake':'ic-breath');
    setTimeout(()=>{ic.className='perficon';},2300); }
  const sub=document.querySelector('#app .avgwho .avgsub'); if(sub)sub.textContent='选项表演 · '+m.n;
  const who=document.querySelector('#app .avgwho b');
  if(who)who.textContent=whoLine(key);
  clearTimeout(PERF_BACK);
  PERF_BACK=setTimeout(()=>{
   el.classList.remove('perf-nod','perf-shake','perf-guard','perf-lean');
   refreshStageCast();
  },2300);
 },48);
}
document.addEventListener('click',e=>{
 const t=e.target.closest('[data-act]'); if(!t||t.disabled)return;
 const a=t.dataset.act||'';
 if(!/(_ans|_choose|_q|_sel|_opt|_act)$/.test(a))return;
 const box=t.closest('.opts,.actl,.matchwrap,.btnrow')||t.parentElement;
 const kids=box?[...box.children].filter(x=>x.matches('button')):[];
 let idx=kids.indexOf(t); if(idx<0){const n=parseInt(t.dataset.v,10);idx=isNaN(n)?0:((n%4)+4)%4;}
 queuePerf(idx);
},true);


/* ---------- R8：大厅作者原稿可直接拖动/双指缩放，且不出任何方框 ---------- */
let ACTIVE_DRAG=0;
let HPTS=new Map(), HDIST=0, HMOVED=false, HSPR={x:0,y:0,s:1}, HSUP=0;
function resetHallSpr(){ HSPR={x:0,y:0,s:1}; applyHSpr(); }
function hallBounds(){
 const pv=document.querySelector('.hh-preview');
 const W=pv?pv.clientWidth:innerWidth*.86, H=pv?pv.clientHeight:innerHeight*.30;
 return {x:W*.22,y:H*.18};
}
function clampHallSpr(spring){
 const lim=hallBounds();
 HSPR.x=Math.max(-lim.x,Math.min(lim.x,HSPR.x));
 HSPR.y=Math.max(-lim.y,Math.min(lim.y,HSPR.y));
 HSPR.s=Math.max(.8,Math.min(1.6,HSPR.s));
 applyHSpr();
 if(spring){
  const el=document.querySelector('.hh-cut');
  if(el){el.classList.add('hh-return');setTimeout(()=>el.classList.remove('hh-return'),340);}
 }
}
function ensureHallVisible(){
 const pv=document.querySelector('.hh-preview'), cut=document.querySelector('.hh-cut');
 if(!pv||!cut)return;
 const p=pv.getBoundingClientRect(), c=cut.getBoundingClientRect();
 const vis=Math.max(0,Math.min(c.right,p.right)-Math.max(c.left,p.left))*
           Math.max(0,Math.min(c.bottom,p.bottom)-Math.max(c.top,p.top));
 if(vis/Math.max(1,c.width*c.height)<.35){
  HSPR={x:0,y:0,s:HSPR.s};applyHSpr();   /* R17：保留倍率 */
  cut.classList.add('hh-return');setTimeout(()=>cut.classList.remove('hh-return'),340);
 }
}
function hallEl(t){return t&&t.closest?t.closest('[data-hhit]'):null;}
function applyHSpr(){
 const rs=document.documentElement.style;
 rs.setProperty('--hx',HSPR.x+'px');rs.setProperty('--hy',HSPR.y+'px');rs.setProperty('--hs',HSPR.s);
}
document.addEventListener('pointerdown',e=>{
 /* R17：第二根手指只要还在预览框内就接受，不再被 ACTIVE_DRAG 挡掉 */
 const el=hallEl(e.target);
 if(HPTS.size===0){ if(!el||ACTIVE_DRAG)return; }
 else{ if(HPTS.size>=2)return;
       if(!(e.target.closest&&e.target.closest('.hh-preview')))return; }
 HPTS.set(e.pointerId,{x:e.clientX,y:e.clientY});HMOVED=false;ACTIVE_DRAG=1;vib(8);
 if(HPTS.size===2){const p=[...HPTS.values()];HDIST=Math.hypot(p[0].x-p[1].x,p[0].y-p[1].y);}
},true);
document.addEventListener('pointermove',e=>{
 const p=HPTS.get(e.pointerId); if(!p)return;
 const dx=e.clientX-p.x,dy=e.clientY-p.y;p.x=e.clientX;p.y=e.clientY;
 if(HPTS.size===1){ if(Math.abs(dx)+Math.abs(dy)>1)HMOVED=true;
  HSPR.x+=dx;HSPR.y+=dy;clampHallSpr(false); }
 else{const q=[...HPTS.values()],d=Math.hypot(q[0].x-q[1].x,q[0].y-q[1].y);
  if(HDIST>0){HSPR.s=Math.max(.8,Math.min(1.6,HSPR.s*d/HDIST));clampHallSpr(false);}
  HDIST=d;HMOVED=true;}
},true);
['pointerup','pointercancel'].forEach(ev=>document.addEventListener(ev,e=>{
 if(!HPTS.has(e.pointerId))return;
 HPTS.delete(e.pointerId);
 if(HPTS.size>0){ HDIST=0; return; }   /* 等最后一根抬起 */
 HDIST=0;ACTIVE_DRAG=0;vib(10);
 if(!HMOVED){ HSUP=1; openHallFull(); setTimeout(()=>HSUP=0,320); }
 else {
   const lim=hallBounds();
   if(Math.abs(HSPR.x)>lim.x*.55||Math.abs(HSPR.y)>lim.y*.55){
    HSPR={x:0,y:0,s:HSPR.s};               /* 拖太远回中心，但保留双指缩放倍率 */
   }
   clampHallSpr(true); ensureHallVisible();
 }
 HMOVED=false;
},true));

/* ---------- R8：所有文字气泡可自定义摆位 / 宽高，组件互斥，左右不出屏 ---------- */
function bubKey(el){ return TAB+':'+el.dataset.bi; }
function applyBubbleLayout(){
 document.body.classList.toggle('layout-on',!!LAYOUT);
 const fr=document.querySelector('#app .avgframe'); if(!fr)return;
 const blocks=[...fr.children].filter(x=>x.classList&&x.classList.contains('avgblock'));
 blocks.forEach((el,i)=>{
  el.dataset.bi=i;
  const s=BUBLAY[bubKey(el)]||{x:0,y:0,w:0,h:0};
  const old=el.querySelector('.bhandle');
  if(LAYOUT){
   el.classList.add('layout');
   el.style.width=s.w?Math.min(s.w,innerWidth-16)+'px':'';
   el.style.maxHeight=s.h?s.h+'px':'';
   el.style.transform='translate('+s.x+'px,'+s.y+'px)';
   if(!old){
    const h=document.createElement('div');h.className='bhandle';
    h.innerHTML='<button class="bgrip" aria-label="拖动摆位">✥</button>'+
      '<button data-act="bub_w_dec" aria-label="调窄">－</button>'+
      '<button data-act="bub_w_inc" aria-label="调宽">＋</button>'+
      '<button data-act="bub_h" aria-label="调高">↕</button>'+
      '<button data-act="bub_reset" aria-label="复位本气泡">↺</button>';
    el.appendChild(h);
   }
  }else{
   el.classList.remove('layout');el.style.width='';el.style.maxHeight='';el.style.transform='';
   if(old)old.remove();
  }
 });
}
let BDRAG=null;
document.addEventListener('pointerdown',e=>{
 const g=e.target.closest('.bgrip'); if(!g||!LAYOUT||ACTIVE_DRAG)return;
 const el=g.closest('.avgblock'); if(!el)return;
 const s=BUBLAY[bubKey(el)]||{x:0,y:0,w:0,h:0};
 BDRAG={el:el,x0:s.x,y0:s.y,px:e.clientX,py:e.clientY,pid:e.pointerId};
 ACTIVE_DRAG=1; vib(8);
 [...document.querySelectorAll('#app .avgblock')].forEach(x=>{if(x!==el)x.classList.add('bub-busy');});
},true);
document.addEventListener('pointermove',e=>{
 if(!BDRAG||e.pointerId!==BDRAG.pid)return;
 const dx=e.clientX-BDRAG.px, dy=e.clientY-BDRAG.py;
 const el=BDRAG.el, key=bubKey(el), s=BUBLAY[key]||{x:0,y:0,w:0,h:0};
 const w=el.offsetWidth, lo=-el.offsetLeft, hi=innerWidth-el.offsetLeft-w;
 s.x=Math.max(lo,Math.min(hi,BDRAG.x0+dx));   /* 左右 clamp 到屏幕内 */
 s.y=BDRAG.y0+dy;                             /* 上下不限 */
 /* 组件互斥：与其他气泡矩形相交就沿 y 推开，最多 6 轮 */
 let r={l:el.offsetLeft+s.x,t:el.offsetTop+s.y,r:el.offsetLeft+s.x+w,b:el.offsetTop+s.y+el.offsetHeight};
 for(let n=0;n<6;n++){
  let hit=null;
  [...document.querySelectorAll('#app .avgblock')].forEach(o=>{
   if(o===el||hit)return;
   const q=o.getBoundingClientRect();
   if(r.l<q.right&&r.r>q.left&&r.t<q.bottom&&r.b>q.top)hit=q;
  });
  if(!hit)break;
  const push=hit.bottom-r.t+8;
  s.y+=push;r.t+=push;r.b+=push;
 }
 BUBLAY[key]=s;
 el.style.transform='translate('+s.x+'px,'+s.y+'px)';
},true);
['pointerup','pointercancel'].forEach(ev=>document.addEventListener(ev,e=>{
 if(!BDRAG||e.pointerId!==BDRAG.pid)return;
 saveLayout(); ACTIVE_DRAG=0; BDRAG=null; vib(10);
 [...document.querySelectorAll('#app .avgblock')].forEach(x=>x.classList.remove('bub-busy'));
 announce('气泡位置已保存，左右不会超出屏幕');
},true));

/* 连续透明度滑杆 */
document.addEventListener('input',e=>{
 if(!e.target||e.target.id!=='bubR')return;
 BUBF=Math.max(.10,Math.min(.90,+e.target.value/100));
 try{localStorage.setItem('beixue_bubf_v1',BUBF);}catch(err){}
 applyA11y();
 const p=$('#bubPct');if(p)p.textContent=Math.round(BUBF*100)+'%';
});

render();
