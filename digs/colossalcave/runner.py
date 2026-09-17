import forloader

class StackFrame:
    def __init__(self, section_name):
        self.section_name = section_name
        self.vars = {}
        self.lines = sections[section_name]['lines']
        self.pc = 0

class MemoryVar:
    def __init__(self):
        self.v = 0

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

class Runner:
    def __init__(self, sections):
        self.sections = sections
        self.stack = [StackFrame('*')]
        self.running = False

    def translate_for_eval(self,expr, frame):
        tokens = find_tokens(expr)
        for name, start, end in reversed(tokens):
            if end< len(expr) and expr[end] == '(':                        
                raise NotImplementedError("Array or function call not implemented")
            expr = expr[:start] + name + '.v' + expr[end:]
            if name not in frame.vars:
                frame.vars[name] = MemoryVar()
        return expr        

    def execute_line(self, frame, line):
        # The program counter is incremented before calling this function

        if line.startswith('IMPLICIT') or line.startswith('LOGICAL') or line.startswith('REAL') or line.startswith('INTEGER'):
            return

        if line.startswith('COMMON'):
            if frame.section_name == '*':
                # Ignore these lists in the root section
                return
            else:
                # In other sections, copy the pointers from the root
                raise NotImplementedError(f"COMMON block in section {frame.section_name} not implemented")

        if line.startswith('DIMENSION'):
            line = line[9:]
            line = line[:-1].split('),')
            for entry in line:
                i = entry.index('(')
                name = entry[:i]
                dims = entry[i+1:].split(',')
                if name not in frame.vars:
                    frame.vars[name] = []
                    if len(dims) == 1:                    
                        for _ in range(int(dims[0])+1):
                            frame.vars[name].append([MemoryVar()])
                    elif len(dims) == 2: # MUST be a 2D array ... that's all we support
                        for _ in range(int(dims[0])+1):
                            frame.vars[name].append([MemoryVar()])
                            for _ in range(int(dims[1])+1):
                                frame.vars[name][-1].append([MemoryVar()])
                    else:
                        raise NotImplementedError(f"Array with more than 2 dimensions not implemented: {line}")
            return

        if line.startswith('IF('):
            i = line.index('(')
            j = find_close_paren(line, i)
            a = line[i+1:j]
            b = line[j+1:]
            # FORTRAN uses .AND. and .OR. for logical and bitwise operators.
            # We need to know the difference. This matches all six cases of
            # bitwise operators in the IF expressions of the code we have.
            # TODO even in the 350?
            if '.XOR.' in a or '0o' in a:
                a = a.replace('.AND.', '&')
            a = a.replace('H.AND.SHIFT', 'H&SHIFT')
            #
            a = a.replace('.EQ.', '==').replace('.NE.', '!=').replace('.LT.', '<').replace('.LE.', '<=').replace('.GT.', '>').replace('.GE.', '>=')
            a = a.replace('.AND.', ' and ').replace('.OR.', ' or ').replace('.NOT.', ' not ')
            a = a.replace('.XOR.', ' ^ ')
            tokens = find_tokens(a)
            # TODO run these in reverse order
            for name, start, end in reversed(tokens):
                if end< len(a) and a[end] == '(':                        
                    raise NotImplementedError("Array or function call not implemented")
                a = a[:start] + name + '.v' + a[end:]
                if name not in frame.vars:
                    frame.vars[name] = MemoryVar()
                     
            val = eval(a, frame.vars)
            if val:
                # Execute the rest of the line
                self.execute_line(frame, b)
            else:
                # Skip to the next line
                return
        
        expr = self.translate_for_eval(line, frame)   

        exec(expr, frame.vars)


        #raise NotImplementedError(f"Line not implemented: {line}")

    def run(self):
        self.running = True
        frame = self.stack[0]        
        while self.running:
            print(f"Current section: {frame.section_name}, PC: {frame.pc}, Line: {frame.lines[frame.pc]}")
            line = frame.lines[frame.pc]
            frame.pc += 1
            self.execute_line(frame, line)


if __name__ == '__main__':
    sections = forloader.load_fortran('../../content/colossalcaveadventure/raw/adventOrg.f')
    #sections = load_fortran('../../content/colossalcaveadventure/raw/advent350.for')
    runner = Runner(sections)
    runner.run()
