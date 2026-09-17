def remove_ignorable_spaces(s):
    ret = ''
    pos = 0
    while pos < len(s):
        if s[pos] == "'":
            start = pos
            pos = s.find("'", pos+1)+1
            ret += s[start:pos]
            continue
        if s[pos] == ' ':
            pos += 1
            continue
        if s[pos] == '\t':
            pos += 1
            continue
        # Other things we want to handle outside of string literals. In FORTRAN,
        # the single quote before a number indicates octal
        if s[pos] == '"':
            ret += '0o'
            pos += 1
            continue
        ret += s[pos]
        pos += 1
    return ret
    
def load_fortran(filename):
    current_section = {
        'type': 'main',
        'args': None,
        'return_type': None,
        'lines': [],
        'labels': {}
    }
    sections = {'*' : current_section}

    with open(filename, 'r') as f:   
        for line in f:
            line = line[:-1]
            line = line.replace(chr(0x0C), '') 
            if not line.strip() or line.startswith('C'):
                # Ignore comments and blank lines
                continue               
            # If first character is a number, then this is a label. The end is the first non number
            label = None
            if line and line[0].isdigit():
                end = 0
                while end < len(line) and line[end].isdigit():
                    end += 1
                label = line[:end]
                line = line[end:]
                current_section['labels'][label] = len(current_section['lines'])
            # Skip to next real character
            while line.startswith(' ') or line.startswith('\t'):
                line = line[1:]
            # If this is a continuation line, append to the last line in the current section
            continue_char = None        
            if line and line[0].isdigit():
                current_section['lines'][-1] += line[1:]            
                continue        
            # Start other sections
            if line.startswith('LOGICAL FUNCTION') or line.startswith('INTEGER FUNCTION') or line.startswith('SUBROUTINE'):
                if line.startswith('SUBROUTINE'):
                    type = 'subroutine'
                    ret_type = None
                    line = line[len('SUBROUTINE'):]
                else:
                    type = 'function'
                    ret_type = line.split()[0]
                    line = line[line.index('FUNCTION')+8:]
                i = line.find('(')
                if i<0:
                    name = line
                    args = []
                else:
                    name = line[:i]
                    args = line[i+1:line.index(')')].split(',')
                current_section = {
                    'name': name,
                    'type': type,
                    'return_type': ret_type,
                    'args': args,
                    'lines': [],
                    'labels': {}
                }
                sections[name] = current_section
                continue
            
            current_section['lines'].append(line)

    for sec in sections.values():
        sec['lines'] = [remove_ignorable_spaces(line) for line in sec['lines']]

    return sections

def find_close_paren(s, start):
    # This only works if there are no "()" in string literals.
    depth = 0
    for i in range(start, len(s)):
        if s[i] == '(':
            depth += 1
        elif s[i] == ')':
            depth -= 1
            if depth == 0:
                return i
    return -1

if __name__ == '__main__':
    #sections = load_fortran('../../content/colossalcaveadventure/raw/adventOrg.f')
    sections = load_fortran('../../content/colossalcaveadventure/raw/advent350.for')
    for name, section in sections.items():
        for line in section['lines']:
            if line.startswith('IF(') or line.startswith('IF ('):
                i = line.index('(')
                j = find_close_paren(line, i)
                a = line[i+1:j]
                b = line[j+1:]

                # FORTRAN uses .AND. and .OR. for logical and bitwise operators.
                # We need to know the difference. This matches all six cases of
                # bitwise operators in the IF expressions of the code we have.
                if '.XOR.' in a or '"' in a:
                    a = a.replace('.AND.', '&')
                a = a.replace('H.AND.SHIFT', 'H&SHIFT')
                #
                a = a.replace('.EQ.', '==').replace('.NE.', '!=').replace('.LT.', '<').replace('.LE.', '<=').replace('.GT.', '>').replace('.GE.', '>=')
                a = a.replace('.AND.', ' and ').replace('.OR.', ' or ').replace('.NOT.', ' not ')
                a = a.replace('.XOR.', ' ^ ')
                print(a)
