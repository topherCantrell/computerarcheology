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
      
#import json  
#print(json.dumps(content,indent=4,sort_keys=True))
#print(dirs)
#print(files)
for f in files:
    if f.endswith('.js'):
        print(f)