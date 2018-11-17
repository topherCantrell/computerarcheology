from os import walk

content = {}
files = []
dirs = []

def extract_path(s,isdir):
    s = s.replace('\\','/')
    ss = s.split('/')
        
    p = content
    r = '/'
    for c in ss[2:-1]:
        if not c in p:
            p[c] = {}
            p = p[c]            
        else:
            p = p[c]
        r = r + c + '/'
    if isdir:
        p[ss[-1]] = {}
        r = r + ss[-1]
        if not r in dirs:
            dirs.append(r)
    else:
        p[ss[-1]] = ''
        files.append(r+ss[-1])

for (dirpath, dirnames, filenames) in walk('..\\content'):
    for d in dirnames:
        extract_path(dirpath+'/'+d,True)
    for f in filenames:
        extract_path(dirpath+'/'+f,False)
        
def find_orphans(p):
    for s in p:
        o = p[s]
        if isinstance(o,str):
            continue
        if len(o) == 0:
            print('Orphan '+s)
        find_orphans(o)
            

      
#import json  
#print(json.dumps(content,indent=4,sort_keys=True))
#print(dirs)
#print(files)
for f in files:
    if f.endswith('.md'):
        print(f)
        
find_orphans(content)

#print(content['js'])