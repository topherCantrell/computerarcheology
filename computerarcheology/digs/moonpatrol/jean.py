# Help merge the disassembly from Jean-Francios

mine = "d:/git/computerarcheology/content/arcade/moonpatrol/code.md"
jean = "d:/git/computerarcheology/content/arcade/moonpatrol/fabre/mpatrol_z80_2.asm"


mine_lines = []
with open(mine) as m:
    for line in m:
        line = line.strip()
        if not line:
            continue
        mine_lines.append(line)

jean_lines = []
with open(jean) as j:
    for line in j:
        line = line.strip()
        if not line:
            continue
        jean_lines.append(line)

def extract_labels(mine,jeans):
    my = _extract_labs(mine)
    js = _extract_labs(jeans)

    for addr,lab in js.items():
        if addr not in my:
            print('Jean has',lab)

   

def _extract_labs(lines):
    address = 0
    ret = {}
    for line in lines:
        if len(line)>4 and line[4]==':':
            address = int(line[:4],16)
        else:
            g = line
            i = g.find(';')
            if i>=0:
                g = g[:i].strip()
            i = g.find(' ')
            if i>=0:
                g = g[:i].strip()
            if g.endswith(':'):
                ret[address] = g[:-1]
    return ret
                

def match_comments(mine,jean):
    my_entries = {}
    for line in mine:
        if len(line)>4 and line[4]==':':
            address = line[:4]
            i = line.find(';')
            if i>=0:
                comment = line[i+1:].strip()
                code = line[5:i].strip()
            else:
                comment = ''
                code = line[5:]
            my_entries[address] = (address,code,comment)
    jean_entries = {}
    for line in jean:
        if len(line)>4 and line[4]==':':
            address = line[:4]
            i = line.find(';')
            if i>=0:
                comment = line[i+1:].strip()
                code = line[5:i].strip()
            else:
                comment = ''
                code = line[5:]
            jean_entries[address] = (address,code,comment)

    for address in range(0x0000,0x4000):
        adr = hex(address).upper()[2:].rjust(4,'0')
        if adr not in jean_entries:
            continue
        j = jean_entries[adr]
        if adr not in my_entries:
            print('Jean has but I dont',j)
        m = my_entries[adr]
        mc = m[2]
        i = mc.find('{')
        if i>=0:
            k = mc.find('}')
            mc = mc[0:i] + mc[k+2:]
        if mc != j[2]:
            print(m[0],mc,j[2])
        
j = extract_labels(mine_lines, jean_lines)
print(j)
# match_comments(mine_lines,jean_lines)
        
