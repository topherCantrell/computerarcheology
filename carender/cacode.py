import os


def is_hex_2(txt):
    if len(txt) != 2:
        return False
    for c in txt.upper():
        if c not in '0123456789ABCDEF':
            return False
    return True


def is_hex_4(txt):
    if len(txt) != 4:
        return False
    for c in txt.upper():
        if c not in '0123456789ABCDEF':
            return False
    return True


def load_binary_files(spec, directory):
    origin = 0
    
    i = spec.find(':')
    if i >= 0:
        origin = int(spec[0:i], 16)
        spec = spec[i + 1:]    
    files = spec.split('+')
    ret = b''
    for file in files:
        
        mang = None
        i = file.find('*')
        if i >= 0:
            mang = file[i + 1:].strip()
            file = file[:i]
        
        rge = None
        i = file.find('[')
        if i >= 0 and file[-1] == ']':
            j = file.find(':', i)
            rge = [int(file[i + 1:j], 16), int(file[j + 1:-1], 16)]
            file = file[0:i]            
                
        with open(os.path.join(directory, file), 'rb') as f:
            data = f.read()
            
        if rge:
            data = data[rge[0]:rge[1]]
        
        if mang:
            if mang == 'swap(0,1)':            
                d = bytearray(data)
                for i in range(len(d)):
                    b0 = (d[i] & 1) << 1
                    b1 = (d[i] & 2) >> 1
                    d[i] = d[i] & 252 | b0 | b1           
                data = bytes(d)
            else:
                raise Exception('Unknown mangler ' + mang)            
            
        ret += data
    
    return {'origin':origin, 'data':ret}


def split_disassembly_line(txt):
    comment = None
    data = None
    opcode = None
    address = None
    label = None
    
    if txt.endswith('\n'):
        txt = txt[:-1]
    
    # Take out any trailing comment
    i = txt.find(';')
    if i >= 0:
        comment = txt[i + 1:]
        txt = txt[:i].strip()                
    if txt:       
    
        # Take off any leading address
        if len(txt) > 4 and is_hex_4(txt[:4]) and txt[4] == ':':
            address = int(txt[0:4], 16)
            txt = txt[5:].strip()
            
        # Take off any leading label
        i = txt.find(':')
        if i >= 0:
            label = txt[:i].strip()
            txt = txt[i + 1:].strip()
        
        bt = txt.strip().split()
    
        data = []
        has_op = False
        for d in bt:
            if is_hex_2(d):
                data.append(int(d, 16))
            else:
                has_op = True
                break
            
        if has_op:
            i = txt.find(d)
            opcode = txt[i:]
        
    return {'address':address, 'comment':comment, 'data':data, 'opcode':opcode, 'label':label}


def parse_binary(lines, origin_gaps=[]):

    origin = -1
    addr = -1
    ret = []

    for line in lines:
        i = line.find(';')
        if i >= 0:
            line = line[0:i]
        line = line.strip()

        if not line:
            continue

        if len(line) < 5:
            continue

        if line[4] != ':':
            continue

        if not is_hex_4(line[0:4]):
            continue

        naddr = int(line[0:4], 16)
        if addr < 0:
            origin = naddr
            addr = naddr

        data = line[5:].split()

        duse = []
        for d in data:
            if is_hex_2(d):
                duse.append(d)
            else:
                break

        if addr in origin_gaps:
            addr = naddr

        if addr != naddr:
            raise Exception(f'Gap in origin at {hex(addr)}')

        for d in duse:
            ret.append(int(d, 16))
            addr += 1

    return origin, ret
