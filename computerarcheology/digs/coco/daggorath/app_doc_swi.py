
FILE_NAME = '../../../../content/CoCo/Daggorath/Code.md'

lines = []
with open(FILE_NAME) as f:
    lines = f.readlines()
    
lines = [x.strip() for x in lines]

for x in range(len(lines)):
    if lines[x] == '# SWI Handler':
        while not lines[x].startswith('| 00 '):
            x+=1
        break

docs = lines[x:x+29]
print(docs)
        
    

x = 0
while x<len(lines):
    line = lines[x]
    x+=1
    if len(line)>5 and line[4:8]==': 3F' and line[8:].strip().startswith('SWI '):
        print(line)        
        line = lines[x]
        x+=1
        print(line)
    else:
        #print(line)        
        pass