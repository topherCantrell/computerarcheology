from code_line import CodeLine

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
         
# Gather addresses of each label
all_labels = {}   
for i in range(len(lines)):
    line = lines[i]
    if type(line) != str:
        if line.label != None:
            if line.label in all_labels:
                raise Exception("Label '"+line.label+"' has multiple definitions.")
            
            # TODO look forward to next CodeLine with an address and use that
            
            all_labels[line.label] = 'TODO'