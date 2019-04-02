import json
import os

opcodes = None

def load_lines(filename):
    with open(filename, 'r') as f:
        raw_lines = f.readlines()

    ret = []
    pos = 0
    for line in raw_lines:
        pos += 1
        n = line.strip()
        if n.startswith('.include'):
            # TODO error checking/reporting
            n = n[8:].strip()
            ret = ret + load_lines(n)
            continue
        ret.append({
            'file_name': filename,
            'line_number': pos,
            'text': n
        })
    return ret


def remove_comments_and_blanks(lines):
    ret = []
    for line in lines:
        n = line['text']
        i = n.find(';')
        if i >= 0:
            n = n[0:i].strip()
        if n:
            line['original_text'] = line['text']
            line['text'] = n
            ret.append(line)
    return ret

def _load_CPU(name):
    global opcodes
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name)) as f:
        opcodes = json.load(f)     
    # TODO parse the opcodes into fragment string for matching
    
def _find_opcode(text):
    match = text.upper()
    nmatch = ''
    for i in range(len(match)):
        c = match[i]
        #if is_needed()
    # Keep only whitespace between letters/numbers
    # Run the list  

def _dir_data(line, labels, defines, pass_number):
    n = line['text'][1:].split(',')
    if pass_number == 0:
        line['data'] = [0] * len(n)
    else:
        line['data'] = []
        for v in n:
            line['data'].append(_get_numeric(v, labels, defines))


def _get_numeric(s, labels, defines):
    z = {**labels, **defines}
    v = eval(s, None, z)
    return v


def _print_listing(lines, labels, defines):
    print('#### Labels')
    keys = labels.keys()
    keys = sorted(keys)
    for label in keys:
        print('{:16} = 0x{:04X}'.format(label,labels[label]))
    print()
    print('#### Defines')
    keys = defines.keys()
    keys = sorted(keys)
    for define in keys:
        v = defines[define]
        if isinstance(v,str):
            print('{:16} = {}'.format(define,defines[define]))
        else:
            print('{:16} = 0x{:04X}'.format(define,defines[define]))
    print()
        
    for line in lines:
        addr = ''
        if 'address' in line:
            addr = '{:04X}:'.format(line['address'])
        data = ''
        if 'data' in line:
            for d in line['data']:
                data = data + '{:02X} '.format(d)
        data = data.strip()
        print('{} {:16} {}'.format(addr,data,line['original_text']))
              
def _write_binary(lines):
    # TODO
    pass


def assemble(lines):

    labels = {}
    defines = {}

    for pass_number in range(2):

        address = 0

        for line in lines:
            n = line['text']
            if n.startswith('.'):
                # Directive

                # Define
                if '=' in n:
                    # TODO could be a string with an "=" in it
                    i = n.index('=')
                    v = n[i + 1:].strip()
                    n = n[1:i].strip()
                    if pass_number == 2 and (n in labels or n in defines):
                        raise Exception('Multiply defined: ' + n)
                    if n.startswith('_'):
                        if n=='_CPU':
                            _load_CPU(v+'.js')
                    else:
                        v = _get_numeric(v, labels, defines)
                    defines[n] = v

                # Data
                elif n.startswith('. '):  # TODO or n.startswith('.W')
                    _dir_data(line, labels, defines, pass_number)
                    line['address'] = address

                else:
                    raise Exception('Unknown directive: ' + n)

            elif n.endswith(':'):
                # Label (or origin)
                if pass_number == 1:  # second pass only
                    n = n[:-1].strip()
                    if n in labels or n in defines:
                        raise Exception('Multiply defined: ' + n)

                    try:
                        # A number ... this is an origin
                        if n.upper().startswith('0X'):
                            address = int(n[2:], 16)
                        else:
                            address = int(n)
                    except:
                        # Not a number ... this is a label to remember
                        labels[n] = address

            else:
                line['address'] = address
                # Opcode
                if pass_number == 0:
                    # TODO
                    line['data'] = [7, 8, 9]
                else:
                    # TODO
                    line['data'] = [7, 8, 9]

            if 'data' in line:
                address = address + len(line['data'])

    return (labels, defines)


if __name__ == '__main__':

    lines = remove_comments_and_blanks(load_lines('hello.asm'))
    (labels, defines) = assemble(lines)

    _print_listing(lines, labels, defines)
