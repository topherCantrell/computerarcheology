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

        if (line.startswith('IMPLICIT') or line.startswith('LOGICAL') or line.startswith('REAL') or 
            line.startswith('INTEGER') or line.startswith('EXTERNAL')):
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
                        frame.vars[name].append(None)  # Fortran starts at 1 (not 0)             
                        for _ in range(int(dims[0])):
                            frame.vars[name].append(MemoryVar())
                    elif len(dims) == 2: # MUST be a 2D array ... that's all we support
                        frame.vars[name].append(None)  # Fortran starts at 1 (not 0)
                        for _ in range(int(dims[0])):
                            frame.vars[name].append([None])  # Fortran starts at 1
                            for _ in range(int(dims[1])):
                                frame.vars[name][-1].append(MemoryVar())
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

        if line.startswith('DATA'):
            # DATA  (JSPKT(I),I=1,16)/24,29,0,31,0,31,38,38,42,42,43,46,77,71,73,75/
            # DATA  M2/0o4000000000,0o20000000,0o100000,0o400,0o2,0/
            # DATA  SETUP/0/,BLKLIN/.TRUE./
            # DATA  MSG/100*-1/
            # DATA  MASK,BLANK/0o774000000000,' '/

            # The survey shows no ',' or '/' in string quotes
            # I=1,n in 4 places -- all the same format

            line = line[4:]
            if line[0] == '(':
                i = line.index('(',1)
                name = line[1:i]
                data = line[i+12:-1].split(',')
                for i in range(len(data)):
                    print(type(frame.vars[name][i+1]))
                    frame.vars[name][i+1].v = int(data[i])
                return
            print("data",line)
            # Split on "/,"
            # For each, strip off trailing "/" if it is there
            # Var_names before "/" and data after
            # If "," in var_names, handle one way
            # Else another
            raise NotImplementedError("MORE TO DO IN DATA statement")            
            return

        if line.startswith('END'):
            raise NotImplementedError("END statement encountered")
            #print("end",line)
            return

        if line.startswith('RETURN'):
            raise NotImplementedError("RETURN statement encountered")
            #print("return",line)
            return

        if line.startswith('CALL'):
            raise NotImplementedError("CALL statement encountered")
            #print("call",line)
            return

        if line.startswith('GOTO'):
            raise NotImplementedError("GOTO statement encountered")
            #print("goto",line)
            return

        if line.startswith('READ'):
            raise NotImplementedError("READ statement encountered")
            #print("read",line)
            return

        if line.startswith('FORMAT'):
            raise NotImplementedError("FORMAT statement encountered")
            #print("format",line)
            return

        if line.startswith('DO') and line[2].isdigit():
            raise NotImplementedError("DO statement encountered")
            #print("do",line)
            return

        if line.startswith('CONTINUE'):
            raise NotImplementedError("CONTINUE statement encountered")
            #print("continue",line)
            return

        if line.startswith('STOP'):
            raise NotImplementedError("STOP statement encountered")
            #print("stop",line)
            return

        if line.startswith('PAUSE'):
            raise NotImplementedError("PAUSE statement encountered")
            #print("pause",line)
            return

        if line.startswith('TYPE'):
            raise NotImplementedError("TYPE statement encountered")
            #print("type",line)
            return

        if line.startswith('ACCEPT'):
            raise NotImplementedError("ACCEPT statement encountered")
            #print("accept",line)
            return

        if line.startswith('OPEN'):
            raise NotImplementedError("OPEN statement encountered")
            #print("open",line)
            return
        
        expr = self.translate_for_eval(line, frame)   
        exec(expr, frame.vars)

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
