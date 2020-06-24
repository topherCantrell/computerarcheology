
def extract_code(lines):
    origin = None
    start = None
    binary = []
    for line in lines:
        i = line.find(';')
        if i>=0:
            line = line[0:i]
        line = line.strip()
        if not line:
            continue
        
        if line.startswith('$$$'):
            origin = None
            continue
        
        if line[4]!=':':
            raise Exception('Bad format '+line)
        
        org = int(line[0:4],16)
        line = line[5:].strip()
        
        dat = []        
        while line:
            if len(line)>2 and line[2]!=' ':
                raise Exception('Bad format '+line)
            dat.append(int(line[0:2],16))
            line = line[3:].strip()
            
        if origin is None:
            origin = org
            start = org
            
        if origin!=org:
            raise Exception('Origin exception '+line)
        
        origin = origin + len(dat)   
        binary = binary + dat         
        
    return start,binary
        
if __name__ == '__main__':
    with open('generated.txt') as f:
        lines = f.readlines()
            
    extract_code(lines)