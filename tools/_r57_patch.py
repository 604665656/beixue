import json,re,base64,io,os
from PIL import Image
H=open('杯雪游戏总站.html',encoding='utf-8').read()
qc=json.load(open('anim57/_QC.json'))
spec=json.load(open('44_表情管理/R57_队列.json'))
def webp(path,q=40,size=224):
    im=Image.open(path).convert('RGBA'); im.thumbnail((size,size))
    b=io.BytesIO(); im.save(b,'WEBP',quality=q,method=4)
    return 'data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
add={}; sheet=[]
for k,v in spec.items():
    if not qc.get(k,{}).get('pass_'): continue
    p=f"anim57/cut/{k}.png"
    add[v['key']]=webp(p); sheet.append((k,v['key'],v['cast'],v['mood']))
# 1) ART 注入：插到 EXPR_SPECIAL 定义之前（顶层）
block="/* R57：8 张逐张独立生成（只换表情），仅注入通过质检的层 */\nObject.assign(ART,{"
block+=",".join(f'"{k}":"{u}"' for k,u in add.items())
block+="});\n"
i=H.index('const EXPR_SPECIAL')
# 找到该 statement 所在行首
ls=H.rfind('\n',0,i)+1
H=H[:ls]+block+H[ls:]
# 2) EXPR_SPECIAL 登记
m=re.search(r'const EXPR_SPECIAL\s*=\s*\{',H)
j=H.index('\n',m.end())+1
reg="".join(f' "{k}":{{cast:"{c}",mood:"{mo}",src:"专属"}},\n' for _,k,c,mo in sheet)
H=H[:j]+reg+H[j:]
# 3) bug①：A 关首帧说话人只取 A_CAST，忽略幕内 who
old="""  if(k==='A'){ bg=A_BG[S.A.node]||'rain'; cast=A_CAST[S.A.node]||'cos_shen'; }"""
new="""  if(k==='A'){ bg=A_BG[S.A.node]||'rain';
   /* R57 bug①：A 关必须按「幕内说话人」取立绘，否则像 s2「三娘低声报菜名」仍显示沈放 */
   const _sc=(D.A.scenes[S.A.node]||{}).who||'';
   let _hit=null;
   for(const c in A_CAST_ROLE){ if(_sc.indexOf(A_CAST_ROLE[c])>=0||_sc.indexOf(c.split('_')[1].charAt(0).toUpperCase()+c.split('_')[1].slice(1))>=0){_hit=c;break;} }
   if(_hit)cast=_hit; else cast=A_CAST[S.A.node]||'cos_shen'; }"""
assert old in H; H=H.replace(old,new)
anchor='const A_BG={'
H=H.replace(anchor,"""const A_CAST_ROLE={cos_jin:'荆三娘',cos_shen:'沈放',cos_ying:'小英子',cos_geng:'耿苍怀',
 cos_yuaner:'袁二',cos_luo:'骆寒',cos_jinhe:'金和尚',cos_qinwen:'秦稳',cos_jiao:'焦泗隐',cos_du:'杜淮山',cos_tian:'田子单'};\n"""+anchor,1)
# 4) bug②：queuePerf 表演人优先用当前幕说话人
old2="""  const base=stageFor(TAB).cast||'';"""
new2="""  /* R57 bug②：表演人优先取当前幕说话人，否则第一幕明明是三娘说话却演成骆寒 */
  let base=stageFor(TAB).cast||'';
  try{
   const _sn=(TAB==='A'&&S.A)?(D.A.scenes[S.A.node]||{}).who||'':'';
   if(_sn){ for(const c in A_CAST_ROLE){ if(_sn.indexOf(A_CAST_ROLE[c])>=0){ base=c; break; } } }
  }catch(e){}"""
assert old2 in H; H=H.replace(old2,new2)
open('杯雪游戏总站.html','w',encoding='utf-8').write(H)
print("injected",len(add),sheet)
for k in qc:
    if not qc[k]['pass_']: print("SKIP",k,qc[k]['hole_px'])
