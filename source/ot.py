import re,json,sys
s=open(sys.argv[1],encoding='utf-8').read()
want={'Exod.3.14','Isa.7.14','Mic.5.2','Hos.11.1','Isa.40.3','Isa.61.1','Isa.61.2','Zech.9.9','Ps.118.22','Ps.118.23','Isa.53.4','Isa.53.5','Isa.53.6','Ps.22.18','Ps.22.1','Ps.16.10','Deut.6.4','Deut.6.5','Lev.19.18','Isa.9.6','Ps.22.16'}
out={}
for vid in want:
    a=s.index('<verse osisID="%s" sID'%vid); b=s.index('<verse eID',a)
    t=s[a:b]; t=re.sub(r'^<verse[^>]*>','',t)
    t=re.sub(r'<transChange[^>]*>','[',t); t=t.replace('</transChange>',']')
    t=re.sub(r'<divineName>(.*?)</divineName>',lambda m:m.group(1).upper(),t)
    t=re.sub(r'<[^>]+>','',t); t=re.sub(r'\s+',' ',t).strip()
    out[vid]=t
json.dump(out,open('ot.json','w'),ensure_ascii=False)
for k in sorted(out): print(k,out[k])
