class MemoryVar:
    def __init__(self):
        self.v = 0

class StackFrame:
    def __init__(self, runner, section_name):
        self.runner = runner
        self.section_name = section_name
        self.vars = {}
        self.lines = runner.sections[section_name]['lines']
        self.labels = runner.sections[section_name]['labels']
        self.pc = 0

def find_close_paren(s, start):
    # This only works if there are no "()" in string literals.
    depth = 0
    for i in range(start, len(s)):
        if s[i] == "'":
            # Skip over string literals -- they might contain "()"
            i = s.find("'", i+1)+1
            continue
        if s[i] == '(':
            depth += 1
        elif s[i] == ')':
            depth -= 1
            if depth == 0:
                return i
    return -1

def split_on_comma(expr):
    pos = 0
    ret = []
    while True:
        depth = 0
        start = pos
        for i in range(pos, len(expr)):
            if expr[i] == "'":
                # Skip over string literals -- they might contain "," or "()"
                i = expr.find("'", i+1)+1
                continue
            if expr[i] == '(':
                depth += 1
            elif expr[i] == ')':
                depth -= 1
            elif expr[i] == ',' and depth == 0:
                ret.append(expr[start:i].strip())
                pos = i + 1
                break
        else:
            ret.append(expr[start:].strip())
            break
    return ret

def find_tokens(expr):
    ret = []
    pos = 0        
    while pos < len(expr):
        # Skip string literals
        if expr[pos] == "'":
            start = pos
            pos = expr.find("'", pos+1)+1
            continue
        # Ignore spaces
        if expr[pos] == ' ':
            pos += 1
            continue
        # Start of a token
        if expr[pos].isalpha():
            start = pos
            pos += 1
            while pos < len(expr) and (expr[pos].isalnum()):
                pos += 1
            ret.append( (expr[start:pos],start, pos))
            continue
        # Skip math
        pos += 1                
    return ret

def get_fortran_value(expr,frame):
    exec_fortran(f'zzzvaluezzz={expr}', frame)
    return frame.vars['zzzvaluezzz'].v

def exec_fortran(expr, frame):
    print(f">>>>>EXECUTING:{expr}:")
    exec(fortran_to_python(expr, frame), frame.vars)

def fortran_to_python(expr, frame):
    # String constants are really integers
    while "'" in expr:
        i = expr.find("'", 0)
        j = expr.find("'", i+1)
        a5 = expr[i+1:j]
        expr = expr[:i] + str(five_to_int(a5)) + expr[j+1:]
        
    # I used the "survey" to make sure this covers the code we have.
    if '.XOR.' in expr or '0o' in expr or 'MASK' in expr or 'SHIFT' in expr:
        expr = expr.replace('.AND.', '&').replace('.OR.', '|')
    else:
        expr = expr.replace('.AND.', ' and ').replace('.OR.', ' or ')
    expr = expr.replace('.EQ.', '==').replace('.NE.', '!=').replace('.LT.', '<').replace('.LE.', '<=').replace('.GT.', '>').replace('.GE.', '>=')
    expr = expr.replace('.NOT.', ' not ').replace('.XOR.', '^')    
    tokens = find_tokens(expr)
    for name, start, end in reversed(tokens):
        if end < len(expr) and expr[end] == '(':
            var_name = expr[start:end]
            if not var_name in frame.vars:
                raise NameError(f"Variable {var_name} not found in frame ... probably a function call or def")
            j = find_close_paren(expr, end) 
            middle = expr[end+1:j]
            middle = middle.replace(',', '][')
            expr = expr[:end] + '[' + middle + '].v' + expr[j+1:]            
            continue
        expr = expr[:start] + name + '.v' + expr[end:]
        if name not in frame.vars:
            frame.vars[name] = MemoryVar()
    print(">>>",expr)
    return expr

def pop_int(line):
    dp = 0
    while True:
        if dp >= len(line):
            dp += 1
            break
        if not line[dp].isdigit():
            break
        dp += 1
    value = int(line[:dp])
    while dp < len(line) and (line[dp]==' ' or line[dp]=='\t'):
        dp += 1
    return value, line[dp:]

def five_to_int(s):
    if len(s)>5:
        raise Exception("A5 inteter too long")
    build = [0,0,0,0,0]
    for i, c in enumerate(s):
        build[i] = ord(c)
    ret = 0
    for b in build:
        ret = ret*128 + b    
    return ret << 1  # LSB is unused    

def int_to_five(s):
    pass