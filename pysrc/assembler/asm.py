
def load_lines(filename):
    with open(filename,'r') as f:
        raw_lines = f.readlines()
        
    ret = []
    pos = 0
    for line in raw_lines:
        pos += 1
        n = line.strip()
        if n.startswith('.include'):
            # TODO error checking/reporting
            # TODO allow spaces between "." and "include"
            n = n[8:].strip()
            ret = ret + load_lines(n)
            continue
        ret.append({
            'file_name' : filename,
            'line_number': pos,
            'text' : n
            })
    return ret 

def remove_comments_and_blanks(lines):
    ret = []
    for line in lines:
        n = line['text']
        i = n.find(';')
        if i>=0:
            n = n[0:i].strip()
        if n:
            line['original_text'] = line['text']
            line['text'] = n
            ret.append(line)
    return ret

def assemble(lines):
    for line in lines:
        n = line['text']
        if n.startswith('.'):
            # Directive
            print('Directive',n) 
        elif n.endswith(':'):
            # Label
            print('Label',n)
        else:
            # Opcode
            print('Opcode',n)


if __name__ == '__main__':
    
    lines = remove_comments_and_blanks(load_lines('hello.asm'))
    assemble(lines)
    
    