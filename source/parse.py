import re,json,sys
s=open(sys.argv[1],encoding='utf-8').read()
out={}
for bk in ['Matt','Mark','Luke','John']:
    a=s.index('<div type="book" osisID="%s"'%bk); b=s.index('</div>',a)
    g=s[a:b]
    chs=[]; red=False; ital=False; para=False; cur=None
    for m in re.finditer(r'<[^>]+>|[^<]+',g):
        t=m.group(0)
        if t.startswith('<'):
            if t.startswith('<chapter ') and 'sID=' in t: chs.append([])
            elif t.startswith('<p>') or t=='<p>': para=True
            elif t.startswith('<verse ') and 'sID=' in t:
                cur=('¶' if para else '')+('{' if red else ''); para=False
            elif t.startswith('<verse ') and 'eID=' in t:
                if red: cur+='}'
                v=re.sub(r'\s+',' ',cur).replace('{}','').replace('{ ',' {').replace(' }','} ').strip()
                chs[-1].append(v); cur=None
            elif t.startswith('<q ') and 'who="Jesus"' in t and 'sID=' in t:
                red=True
                if cur is not None: cur+='{'
            elif t.startswith('<q ') and 'eID=' in t:
                if red and cur is not None: cur+='}'
                red=False
            elif t.startswith('<q '):
                pass
            elif t.startswith('<transChange'):
                if cur is not None: cur+='['
            elif t.startswith('</transChange'):
                if cur is not None: cur+=']'
        else:
            if cur is not None: cur+=t
    out[bk]=chs
for k,v in out.items(): print(k,len(v),sum(map(len,v)))
json.dump(out,open('gospels.json','w'),ensure_ascii=False,separators=(',',':'))
print(out['Matt'][4][2], out['John'][2][15], out['John'][10][34], out['Luke'][22][33])
