import os
from more_itertools.more import last

deploy = '../../deploy'
last_deploy = '../../lastDeploy'
#new_deploy = '../../newonlydeploy'

files = []
last_files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(deploy):
    for file in f:
        files.append(os.path.join(r, file)[len(deploy)+1:])  
for r, d, f in os.walk(last_deploy):
    for file in f:
        last_files.append(os.path.join(r, file)[len(last_deploy)+1:])        

added = []
deleted = []
changed = []

for f in files:
    if f not in last_files:
        added.append(f)
for f in last_files:
    if f not in files:
        deleted.append(f)
        
#print('Added',added)
print('Deleted',deleted)

for file in files:
    if file not in last_files:
        print('Added',file)
        changed.append(file);
        continue
    with open(os.path.join(deploy,file),'rb') as f:
        bin = f.read()
    with open(os.path.join(last_deploy,file),'rb') as f:
        last_bin = f.read()
    if bin != last_bin:
        print('Changed:',file)
        changed.append(file)
        
print('Changed',changed)

for file in files:
    if file not in changed:
        os.remove(os.path.join(deploy,file))              
