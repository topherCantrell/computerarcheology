import logging
import random

LOGGER = logging.getLogger(__name__)

class MemoryVar:
    def __init__(self):
        self.v = 0
    def __repr__(self):
        return f"MemoryVar{id(self)}({self.v})"

class StackFrame:
    def __init__(self, runner, section_name):
        self.runner = runner
        self.section_name = section_name
        self.vars = {}
        self.vars['MOD'] = FORTRAN_MOD
        self.vars['RAN'] = FORTRAN_RAN
        self.lines = runner.sections[section_name]['lines']
        self.labels = runner.sections[section_name]['labels']
        self.decoded_formats = runner.sections[section_name]['decoded_formats']
        self.pc = 0

def FORTRAN_RAN(a):
    return random.random()

def FORTRAN_MOD(a, b):
    return a % b

def parse_loop_parts(line):
    line = line[1:-1]
    parts = split_on_comma(line)
    v,start = parts[1].split('=')
    return parts[0], v, start, parts[2]

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
    token = ''
    depth = 0
    in_literal = False

    while pos<len(expr):
        c = expr[pos]
        pos += 1
        if c == "'":
            token += c
            in_literal = not in_literal            
            continue
        if in_literal:
            token += c
            continue
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
        elif c == ',' and depth == 0:
            ret.append(token)
            token = ''
            continue
        token += c
    if token:
        ret.append(token)    
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
        if expr[pos].isalpha() and expr[pos].isupper():
            start = pos
            pos += 1
            while pos < len(expr) and (expr[pos].isalnum()):
                pos += 1
            ret.append( (expr[start:pos],start, pos))
            continue
        # Skip math
        pos += 1                
    return ret

def get_fortran_ref(expr, frame):
    ex = fortran_to_python(expr, frame)    
    ex = ex[:-2]
    LOGGER.debug(f"REFERENCE >>>{ex}<<<")
    exec(f'ZZZREFZZZ={ex}', frame.vars)
    return frame.vars['ZZZREFZZZ']

def get_fortran_value(expr,frame):
    exec_fortran(f'ZZZVALUEZZZ={expr}', frame)
    return frame.vars['ZZZVALUEZZZ'].v

def exec_fortran(expr, frame):
    LOGGER.debug(f"EXECUTING FORTRAN >>>{expr}<<<")
    exec(fortran_to_python(expr, frame), frame.vars)

def fortran_to_python(expr, frame):
    # String constants are really integers
    while "'" in expr:
        i = expr.find("'", 0)
        j = expr.find("'", i+1)
        a5 = expr[i+1:j]
        expr = expr[:i] + str(five_to_int(a5)) + expr[j+1:]
        
    # I used the "survey" to make sure this covers the code we have.
    if '.XOR.' in expr or '"' in expr or 'MASK' in expr or 'SHIFT' in expr:
        expr = expr.replace('.AND.', '&').replace('.OR.', '|')
    else:
        expr = expr.replace('.AND.', ' and ').replace('.OR.', ' or ')
    expr = expr.replace('.EQ.', '==').replace('.NE.', '!=').replace('.LT.', '<').replace('.LE.', '<=').replace('.GT.', '>').replace('.GE.', '>=')
    expr = expr.replace('.NOT.', ' not ').replace('.XOR.', '^')
    expr = expr.replace('"', '0o')
    expr = expr.replace('/', '//')
    tokens = find_tokens(expr)
    for name, start, end in reversed(tokens):
        if end < len(expr) and expr[end] == '(':
            var_name = expr[start:end]
            if var_name == 'RAN' or var_name == 'MOD':
                continue
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
    LOGGER.debug(f"FORTRAN TO PYTHON >>>{expr}<<<")
    return expr

def pop_int(line):
    dp = 0
    while True:
        if dp >= len(line):
            dp += 1
            break
        if not line[dp].isdigit() and not line[dp]=='-':
            break
        dp += 1
    value = int(line[:dp])
    while dp < len(line) and (line[dp]==' ' or line[dp]=='\t'):
        dp += 1
    return value, line[dp:]

def five_to_int(s):
    if len(s)>5:
        raise Exception("A5 inteter too long")
    s = s.ljust(5, ' ')
    build = [0,0,0,0,0]
    for i, c in enumerate(s):
        build[i] = ord(c)
    ret = 0
    for b in build:
        ret = ret*128 + b    
    return ret << 1  # LSB is unused    

def int_to_five(s):
    s = s >> 1  # LSB is unused
    build = [0,0,0,0,0]
    for i in range(4, -1, -1):
        build[i] = s % 128
        s = s // 128
    return ''.join(chr(b) for b in build if b != 0)