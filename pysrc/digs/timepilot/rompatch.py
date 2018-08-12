   
def line_to_data(line):
    
    if ';' in line:
        line = line[0:line.index(';')]
    
    line = line.strip()
        
    if len(line)<5:
        return None
    
    if line[4] != ':':
        return None
    
    try:
        addr = int(line[0:4],16)
    except ValueError:
        return None
    
    line = line[5:].strip()
    pos = 0
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
    
    return ret
    
with open("../../../content/arcade/timepilot/soundcode.mark") as file:
    content = file.readlines()
        
data = bytearray()
for line in content:
    # TODO make sure the address is right
    s = line_to_data(line)
    if s!=None:
        data.extend(s)
        
#
with open("../../../content/arcade/timepilot/roms/TM7",mode='rb') as file:
    olddata = file.read()
# TODO fail if different sizes
if olddata != data:
    print("Data is different")
#
        
with open("d:/mame/roms/timeplt/TM7",mode="wb") as out:
    out.write(data)