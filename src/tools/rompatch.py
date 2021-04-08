import os
import tools.binary as BIN

pf = '../../content/CoCo/Daggorath/rompatch.txt'

dr = os.path.dirname(pf)

lines = []
with open('../../content/CoCo/Daggorath/rompatch.txt') as f:
    for g in f:        
        if ';' in g:
            g = g[0:g.index(';')]
        g = g.strip()
        if g:
            lines.append(g)

first = lines[0].split(' ')

with open(os.path.join(dr,first[0]),'rb') as f:
    data = list(f.read())
   
for line in lines[1:]:
    org,dat = BIN.line_to_data(line)
    if dat:
        p = org - int(first[2],16)
        print(p,len(dat))
        for b in dat:            
            data[p] = b
            p+=1

with open(os.path.join(dr,first[1]),'wb') as f:
    f.write(bytes(data))
    