
def read_code_file(file_name):
    ret = []
    with open(file_name, "r") as f:
        for line in f:
            ret.append(line.strip())
    return ret

def write_code_file(file_name, code):
    # Please, please, please use github to back this up first
    with open(file_name, "w") as f:
        for line in code:
            f.write(line + "\n")

def split_comment(line):
    i = line.find(';')
    if i > -1:
        return line[:i].rstrip(), line[i:].lstrip()
    else:
        return line, ''

def find_start_and_end(lines, start_addr, end_addr=None):
    if end_addr is None:
        end_addr = start_addr
    ps = 0
    while not lines[ps].startswith(f'{start_addr:04X}:'):
        ps += 1
    pe = ps
    while not lines[pe].startswith(f'{end_addr:04X}:'):
        pe += 1
    pe += 1
    return ps, pe

def parse_word(info, s):
    if info['IsLittleEndian']:
        return int(s[3:5]+s[0:2], 16)
    else:
        return int(s[0:2]+s[3:5], 16)
    
def read_binary(info):
    with open(info["ROM"], "rb") as f:
        return f.read()
        
    
def get_room_info(info):
    ps_info = get_packed_strings(info)

    lines = read_code_file(info["File"])
    ret = {}
    ps,pe = find_start_and_end(lines, info["RoomTable"][0], info["RoomTable"][1])
    rn = 0
    while ps < pe:
        line = lines[ps]
        ps += 1
        if line.startswith(';'):
            continue
        rn += 1
        ptr_desc = parse_word(info, line[6:11])
        ptr_script = parse_word(info, line[12:17])

        if ptr_script and ptr_desc:        
            ret[ptr_script] = {
                'description': ps_info[ptr_desc],
                'number': rn,
            }
    return ret

def get_address_for(lines, ps):
    while True:
        line = lines[ps]
        ps += 1
        if len(line) < 4 or line[4]!=':':
            continue
        return int(line[:4], 16)        

def get_packed_strings(info):
    ret = {}
    lines = read_code_file(info["File"])
    for i in range(len(lines)):
        if lines[i].startswith('PS_'):
            ps_num = int(lines[i][3:5], 16)
            addr = int(lines[i+1][:4], 16)            
            s_text = []
            j = i-1        
            while True:
                a = lines[j].strip()                
                j -= 1
                if not a or a==';' or a.startswith('; adventure.dat'):
                    break        
                s_text.insert(0,a[2:].strip())
            ret[addr] = {
                'text': s_text,
                'ps_num': ps_num,                
            }
    return ret
            
def collect_script_comments(info):
    lines = read_code_file(info["File"])
    ret = {
        'line_comments': {},
        'end_comments': {},
    }

    addr = 0
    for i in range(len(lines)-1,-1,-1):
        line = lines[i]
        if len(line)>6 and line[4]==':':
            addr = int(line[:4], 16)

        i = line.find(';;')
        if i==0:
            if addr in ret['line_comments']:
                ret['line_comments'][addr].insert(0,line)
            else:
                ret['line_comments'][addr] = [line]
        elif i>0:
            while line[i-1]==' ':
                i -= 1
            ret['end_comments'][addr] = line[i:]
    
    return ret    
