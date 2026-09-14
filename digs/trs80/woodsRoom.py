with open('../../../content/TRS80/Pyramid/Code.md') as f:
    lines = []
    for line in f:
        lines.append(line.strip())

for line in lines:
    i = line.find('woodsRoom')
    if i>=0:            
        rm = line[i+9:]
        try:
            rm = int(rm,10)
            #print(line[i:],rm)
            trs = f'WR_{rm:02X}'
            line = line[:i] + trs        
        except Exception:
            pass
    print(line)
    
