# -*- coding: utf-8 -*-
"""发布前资源门禁：读 杯雪资源清单.csv，查重复哈希、尺寸异常、命名与必填字段。
用法：python 资源清单门禁.py  →  退出码 0 才允许打包单文件 HTML。"""
import csv,sys,os,collections
P=os.path.join(os.path.dirname(os.path.abspath(__file__)),'杯雪资源清单.csv')
rows=list(csv.DictReader(open(P,encoding='utf-8-sig')))
err=[];warn=[]
need=['key','category','mime','w','h','bytes','sha1','consistency']
for i,r in enumerate(rows):
    for k in need:
        if not r.get(k):err.append('第%d行缺 %s'%(i+2,k))
    if not r.get('key','').replace('_','').isalnum():err.append('命名异常 %s'%r.get('key'))
    try:
        w,h,bs=int(r['w']),int(r['h']),int(r['bytes'])
        if w<=0 or h<=0:err.append('尺寸为 0：%s'%r['key'])
        if bs>400000:warn.append('单层 >400KB：%s (%dKB)'%(r['key'],bs//1024))
    except Exception:err.append('数值不可解析：%s'%r.get('key'))
dup=[(h,[r['key'] for r in rows if r['sha1']==h]) for h,c in collections.Counter(r['sha1'] for r in rows).items() if c>1]
for h,ks in dup:err.append('重复哈希 %s → %s'%(h,','.join(ks)))
print('资源清单 %d 层；错误 %d；警告 %d'%(len(rows),len(err),len(warn)))
for e in err[:20]:print('  ERR ',e)
for w in warn[:8]:print('  WARN',w)
sys.exit(1 if err else 0)
