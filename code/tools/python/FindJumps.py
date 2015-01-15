
from CodeLine import CodeLine

with open("../../../content/CoCo/Bedlam/Code.mark.bak") as f:
    raw = f.readlines()   
    
CODE_OPS = ["JSR","BCS","BLS","JMP","BNE","BEQ","BRA","BCS","BMI","BCC","LBCS","BSR","BHI","BPL","LBNE","BRN","LBSR","LBEQ","LBCC"]
RAM_OPS  = ["LDX","STX"]
    
newLines = []
for r in raw:               
    
    t = r.strip()   
                
    # Keep comment lines as-is
    if t.startswith(";"):
        newLines.append(r)
        continue
            
    # Keep blank lines as-is
    if t=="":
        newLines.append(r)
        continue
            
    # Must be code. Parse that.
    c = CodeLine()
    c.parse(r)
    
    if not c.opcode:
        newLines.append(r)
        continue
    
    ow = c.opcode.split(" ")    
    if ow[-1].startswith("$") and not "," in ow[-1]:
        if ow[0] in CODE_OPS:            
            i = c.original.index(";")
            if c.original[i+1] == "{":
                newLines.append(r)
                continue
            n = r[0:i+1]+"{}"+r[i+1:]            
            newLines.append(n)
            continue
        else:
            newLines.append(c.original)
            # Probably can do better
            continue
        
    if(ow[-1].startswith(">")):
        i = c.original.index(";")
        if c.original[i+1] == "{":
            newLines.append(r)
            continue
        n = r[0:i+1]+"{-}"+r[i+1:]            
        newLines.append(n)        
        continue
        
    newLines.append(c.original)
    
print len(raw),len(newLines)

for x in xrange(len(newLines)):
    if not newLines[x].endswith("\n"):
        print ":"+newLines[x]+":"

with open("Code.mark","w") as f:
    f.writelines(newLines)   
            
            