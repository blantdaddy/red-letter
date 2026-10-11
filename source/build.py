import json,re
d=json.load(open('gospels.json')); ot=json.load(open('ot.json'))
fix=lambda t:re.sub(r'\[\s+','[',re.sub(r'\s+\]','] ',t)).replace(']  ','] ').replace('¶ ','¶').strip()
d={b:[[fix(v) for v in c] for c in chs] for b,chs in d.items()}
ot={k:fix(v) for k,v in ot.items()}
data='const G='+json.dumps(d,ensure_ascii=False,separators=(',',':'))+';\nconst OT='+json.dumps(ot,ensure_ascii=False,separators=(',',':'))+';'
t=open('template.html').read().replace('/*__DATA__*/',data).replace('/*__CONTENT__*/',open('content.js').read())
open('red-letter.html','w').write(t)
print(len(t))
