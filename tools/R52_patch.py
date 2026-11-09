# -*- coding: utf-8 -*-
"""R52 patch：
   ① 修真 bug「9 个层键名牌回退哈士喵」——castMeta 加别名兜底
   ② 修真 bug「10 个层键 exprCanon 错归 cos_base」——加显式层键别名表
   ③ 接入 10 张 R52 AI 原画
   ④ 版本 R51 -> R52
   幂等：可重复执行。"""
import json, re

P='/data/workspace/杯雪游戏总站.html'
s=open(P,encoding='utf-8').read(); orig=len(s); log=[]

# ---------- ①+② 共用别名表，插在 CAST_META 定义之前（最早可用，零 TDZ 风险） ----------
ALIAS={
 # 名牌表漏登记、castMeta 兜底成「哈士喵」的 9 项
 'B_face_yi':'cos_yi', 'B_face_jiao':'cos_jiao', 'B_face_qinwen':'cos_qinwen',
 'D_face_shen':'cos_shen', 'D_face_yuancl':'cos_yuancl',
 'D_face_xiaoru':'cos_xiao', 'D_face_zhuyan':'cos_zhu', 'D_face_luohan':'cos_luo',
 'E_face_wink':'cos_tian',
 # 名牌已登记但中文名不在 EXPR_CASTS，canon 错归 cos_base 的 10 项
 'H_cost_yuchi':'cos_yuancl',
 'G_cost_verify':'cos_xiao','G_cost_compare':'cos_xiao','G_cost_brush':'cos_xiao',
 'G_cost_startled':'cos_xiao','G_cost_smile':'cos_xiao','G_cost_turn':'cos_xiao',
 'G_cost_scroll':'cos_xiao','G_cost_blink':'cos_xiao','G_cost_open':'cos_xiao',
}
ALIAS_SRC=("/* R52 层键到逻辑角色的别名表。\n"
 "   B_face、D_face、E_face 等 R5–R16 老层键，名牌表只登记了部分，\n"
 "   castMeta 未命中就兜底成「哈士喵」（C 关默认立绘 B_face_yi 即中招）；\n"
 "   G_cost 系列（校书郎扮相）与 H_cost_yuchi（尉迟渺）名牌已登记，但中文名\n"
 "   不在 EXPR_CASTS，exprCanon 会错归 cos_base，接管后串成本色猫。\n"
 "   按 LEVEL_AVATAR(G:'cos_xiao') 与辕门线显式归位，可审计、不猜测剧情。\n"
 "   有意的历史代用 B_face_yuane→文翰林 保持不动。 */\n"
 "const R52_LAYER_ALIAS="+json.dumps(ALIAS,ensure_ascii=False)+";\n")

if 'const R52_LAYER_ALIAS=' in s:
    s=re.sub(r'/\* R52 层键[\s\S]*?const R52_LAYER_ALIAS=\{[\s\S]*?\};\n','',s,count=1)
anchor='const CAST_META={'
assert anchor in s
s=s.replace(anchor,ALIAS_SRC+anchor,1)
log.append('OK  R52_LAYER_ALIAS 注入（%d 条）'%len(ALIAS))

# ---------- ① castMeta：直接查不到时按别名表规整 ----------
OLD_META=""" if(CAST_META[k])return CAST_META[k];
 const rev=CATCOST.find(x=>origCast(x[2])===k);"""
NEW_META=""" if(CAST_META[k])return CAST_META[k];
 /* R52：层键未在名牌表直接登记时，按显式别名规整回逻辑角色键再查，
    修 9 项回退「哈士喵」。只查别名表，不调用 exprCanon，避免定义顺序问题。 */
 if(typeof R52_LAYER_ALIAS!=='undefined'&&R52_LAYER_ALIAS[k]
    &&CAST_META[R52_LAYER_ALIAS[k]])return CAST_META[R52_LAYER_ALIAS[k]];
 const rev=CATCOST.find(x=>origCast(x[2])===k);"""
if 'R52_LAYER_ALIAS[k]' in s:
    log.append('OK  castMeta 别名兜底已存在（幂等跳过）')
else:
    assert OLD_META in s,'castMeta 插入点未命中'
    s=s.replace(OLD_META,NEW_META,1)
    log.append('OK  castMeta 别名兜底（修名牌回退哈士喵）')

# ---------- ② exprCanon：开头先查别名表 ----------
OLD_CANON="""function exprCanon(cast){
 const ids=new Set(EXPR_CASTS.map(c=>c[0]));"""
NEW_CANON="""function exprCanon(cast){
 /* R52：显式层键别名优先，修 10 项错归 cos_base（接管后串本色猫） */
 if(typeof R52_LAYER_ALIAS!=='undefined'&&R52_LAYER_ALIAS[cast])return R52_LAYER_ALIAS[cast];
 const ids=new Set(EXPR_CASTS.map(c=>c[0]));"""
if 'R52_LAYER_ALIAS[cast]' in s:
    log.append('OK  exprCanon 别名优先已存在（幂等跳过）')
else:
    assert OLD_CANON in s,'exprCanon 插入点未命中'
    s=s.replace(OLD_CANON,NEW_CANON,1)
    log.append('OK  exprCanon 别名优先（修 canon 错归 cos_base）')

# ---------- ③ 声线表：旧全名 vs 短码脱节，20 位角色回退旁白 ----------
VOICE_FIX = ("/* R52：VOICE_LINE 沿用 R6 旧全名(cos_luohan/cos_xiaoru...)，\n"
 "   而 CAST_META/EXPR_CASTS 用短码(cos_luo/cos_xiao...)，\n"
 "   除沈放/秦稳/本色外 20 位角色 TTS 一直回退「旁白」。补短码别名，\n"
 "   并让 voiceConf 按 exprCanon 规整层键，G 关校书郎也能取到萧如声线。 */\n"
 "const VOICE_ALIAS={cos_luo:'cos_luohan',cos_yi:'cos_yilian',cos_jin:'cos_jinsanniang',\n"
 " cos_xiao:'cos_xiaoru',cos_zhu:'cos_zhuyan',cos_yuancl:'cos_yuanchenlong',\n"
 " cos_wen:'cos_wenhanlin',cos_geng:'cos_gengcanghuai',cos_tian:'cos_tianxiao'};\n"
 "for(const [k,v] of Object.entries(VOICE_ALIAS)){if(VOICE_LINE[v]&&!VOICE_LINE[k])VOICE_LINE[k]=VOICE_LINE[v];}\n")
OLD_V = "function voiceConf(cast){ return VOICE_LINE[cast]||VOICE_LINE.narrator; }"
NEW_V = ("function voiceConf(cast){\n"
 " if(VOICE_LINE[cast])return VOICE_LINE[cast];\n"
 " try{ const cn=exprCanon(cast); if(VOICE_LINE[cn])return VOICE_LINE[cn]; }catch(e){}\n"
 " return VOICE_LINE.narrator;\n"
 "}")
if 'const VOICE_ALIAS=' not in s:
    s=s.replace(OLD_V, VOICE_FIX+NEW_V, 1)
    log.append('OK  VOICE_ALIAS 9 条 + voiceConf canon 兜底（修 20 位角色回退旁白）')
else:
    log.append('OK  声线修复已存在（幂等跳过）')

# ---------- ④ 接入 10 张 ----------
NEW=json.load(open('/data/workspace/anim47/_QC.json'))['META']
EMB=json.load(open('/data/workspace/anim47/_EMB.json'))
PAIR={v['exprkey']:k for k,v in NEW.items()}

a=s.index('const EXPR_SPECIAL='); b=s.index(';',a)+1
cur=json.loads(s[s.index('{',a):b-1]); before=len(cur)
for ek,k in PAIR.items(): cur[ek]=k
s=s[:a]+'const EXPR_SPECIAL='+json.dumps(cur,ensure_ascii=False)+';'+s[b:]
log.append('OK  EXPR_SPECIAL %d -> %d（R52 10 格，幂等覆盖）'%(before,len(cur)))

# 先移除旧的 R52 assign 块，再插一次（幂等）
s=re.sub(r'/\* R52：10 张逐张独立生成[\s\S]*?Object\.assign\(ART, \{[\s\S]*?\}\);\n','',s,count=1)
assign=('/* R52：10 张逐张独立生成；基准为用户三视图裁出的正面单只。\n'
        '   不进 PROC_ART（AI 原画）；水印源头预清 + 悬浮碎块通用清理。 */\n'
        'Object.assign(ART, '+json.dumps(EMB,ensure_ascii=False)+');\n')
art=s.index('const ART = '); e=s.index('};',art)+2
s=s[:e]+'\n'+assign+s[e:]
log.append('OK  10 张 WebP 注入 ART（幂等）')

# ---------- ⑤ 版本推进 ----------
s=s.replace("R51：当前筛选 ","R52：当前筛选 ",1)
s=s.replace("杯雪表情谱系_R51_","杯雪表情谱系_R52_",1)
log.append('OK  版本 -> R52（脚注 + CSV 文件名）')

open(P,'w',encoding='utf-8').write(s)
print('\n'.join(log))
print('HTML %d -> %d (delta %+d)'%(orig,len(s),len(s)-orig))
print('TAIL_OK',s.rstrip().endswith('</html>'))
