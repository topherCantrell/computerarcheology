def line_to_data(line):
    
    if ';' in line:
        line = line[0:line.index(';')]
    
    line = line.strip()
        
    if len(line)<5:
        return None,None
    
    if line[4] != ':':
        return None,None
    
    try:
        org = int(line[0:4],16)
    except ValueError:
        return None,None
        
    line = line[5:].strip()    
    ret = bytearray()
    
    while True:
        if len(line)<2:
            break
        if len(line)>2 and line[2]!=' ':
            break
        try:
            val = int(line[0:2],16)
        except ValueError:
            break
        ret.append(val)
        line = line[2:].strip()
    
    return org,ret

def get_binary(file_name, origin):
    with open(file_name) as file:
        content = file.readlines()
        
    data = bytearray()
    
    for line in content:
        org,d = line_to_data(line)
        if d!=None:
            if org!=origin:
                raise Exception("Origin does not match. Expected "+hex(origin)+" but got "+hex(org))
            data.extend(d)
            origin = origin + len(d)
            
    return data    

def compare_source_to_binary(file_name_src, file_name_bin, origin):
    with open(file_name_bin,mode='rb') as file:
        bindata = file.read()
    srcdata = get_binary(file_name_src,origin)
    
    return len(bindata)==len(srcdata),(bindata==srcdata)