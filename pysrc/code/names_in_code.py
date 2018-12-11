from code.code_line import CodeLine

with open('../../content/CoCo/Pyramid/Code.md') as f:
    lines = f.readlines()
    
in_code = False

for i in range(len(lines)):
    line = lines[i]
    if in_code:
        if line.startswith('```'):
            in_code = False
        else:
            lines[i] = CodeLine(line)                        
    else:        
        if line.startswith('```code'):
            in_code = True
         
# Gather addresses of each label in the code
code_labels = {}   
for i in range(len(lines)):
    line = lines[i]
    if type(line) != str:
        if line.label != None:
            if line.label in code_labels:
                raise Exception("Label '"+line.label+"' has multiple definitions.")
            nc = None
            for j in range(i+1,len(lines)):
                if type(lines[j]) != str and lines[j].address!=None:
                    nc = lines[j]
                    break
            if nc==None:
                raise Exception('No address after label '+line.label)
                        
            code_labels[line.label] = nc.address
            
# TODO Load the memory tables