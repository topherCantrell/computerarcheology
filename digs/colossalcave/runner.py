import forloader

class StackFrame:
    def __init__(self, runner, section_name):
        self.runner = runner
        self.section_name = section_name
        self.vars = {}
        self.lines = runner.sections[section_name]['lines']
        self.labels = runner.sections[section_name]['labels']
        self.pc = 0

class MemoryVar:
    def __init__(self):
        self.v = 0

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

def fortran_to_python(expr, frame, hints=[]):
    expr = expr.replace('.EQ.', '==').replace('.NE.', '!=').replace('.LT.', '<').replace('.LE.', '<=').replace('.GT.', '>').replace('.GE.', '>=')
    expr = expr.replace('.NOT.', ' not ').replace('.XOR.', '^')
    pos = 0
    while True:
        is_and = True
        i = expr.find('.AND.')
        j = i+5
        if i<0:
            is_and = False
            i = expr.find('.OR.')
            j = i+4
            if i<0:
                # No more .AND. or .OR. found
                break
        h = hints[0][pos]
        pos += 1  
        if h == 'L':
            rep = ' and ' if is_and else ' or '
        else:  # arithmetic
            rep = '&' if is_and else '|'
        expr = expr[:i] + rep + expr[j:] 
    tokens = find_tokens(expr)
    for name, start, end in reversed(tokens):
        if end < len(expr) and expr[end] == '(':
            var_name = expr[start:end]
            if not var_name in frame.vars:
                raise NameError(f"Variable {var_name} not found in frame ... probably a function call or def")
            j = find_close_paren(expr, end) 
            expr = expr[:end] + '[' + expr[end+1:j] + '].v' + expr[j+1:]
            # TODO 2D arrays will bomb and we'll have to fix here
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

class Runner:
    def __init__(self, sections, data_lines):
        self.sections = sections
        self.stack = [StackFrame(self, '*')]
        self.loop_stack = []
        self.running = False
        self.data_lines = data_lines
        self.data_lines_pos = 0    

    def execute_line(self, frame, line, hints=None):
        # The program counter is incremented before calling this function

        if hints==None:            
            # When processing the TRUE part of an IF, we recurse into this and
            # pass the hints with us.
            i = line.find(';;')
            if i>=0:
                hints = line[i+2:].split(':')
                line = line[:i]
            else:
                hints = []

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
            a = fortran_to_python(a, frame, hints)                        
            print(">>>>>>>>>>>",a)
            val = eval(a, frame.vars)
            if val:
                # Execute the rest of the line
                self.execute_line(frame, b, hints[1:])  # The first hint was for the IF expression
                return
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
                    #print(type(frame.vars[name][i+1]))
                    frame.vars[name][i+1].v = int(data[i])
                return
            #print("data",line)
            # Split on "/,"
            # For each, strip off trailing "/" if it is there
            # Var_names before "/" and data after
            # If "," in var_names, handle one way
            # Else another
            raise NotImplementedError("MORE TO DO IN DATA statement")            
            return

        if line.startswith('DO') and line[2].isdigit():
            # fortran always calculates the loop bounds once before entering the loop
            # DO I=1,5 will run with I values 1,2,3,4,5 (inclusive)
            i = 2
            while line[i].isdigit():
                i += 1
            label = line[2:i]
            j = line.index('=',i)
            var = line[i:j]
            k = line.index(',',j)
            start = line[j+1:k]
            end = line[k+1:]
            if start.isdigit():
                start = int(start)
            else:
                start = frame.vars[start].v
            if end.isdigit():
                end = int(end)
            else:
                end = frame.vars[end].v
            if var not in frame.vars:
                frame.vars[var] = MemoryVar()
            frame.vars[var].v = start
            if start > end:
                # Allowed in fortran, but I haven't coded for it. I am assuming at least
                # one trip (the loop increment happens elsewhere)
                raise ValueError(f"DO loop start {start} greater than end {end}")
            self.loop_stack.append((frame.labels[label], var, frame.pc, end))
            return

        if line.startswith('READ'):
            i = line.index(',')
            j = line.index(')',i)
            vars = split_on_comma(line[j+1:])
            format_line = frame.lines[frame.labels[line[i+1:j]]]
            format_specs = split_on_comma(format_line[7:-1])
            data_line = self.data_lines[self.data_lines_pos]
            self.data_lines_pos += 1
            # Specs for read are all one of these: G, A5, xG, xA5. 
            parsed_values = []
            for spec in format_specs:                
                i = spec.find('G')
                if i<0:
                    i = spec.find('A')
                t = spec[i]  # Either A or G
                reps = 1
                a5 = False
                if i>0:
                    reps = int(spec[:i])
                if t == 'G':
                    while reps>0 and data_line:
                        reps -= 1
                        g, data_line = pop_int(data_line)
                        parsed_values.append(g)                    
                else:                    
                    while reps>0:
                        if not data_line:
                            # If there is no more data, pad with spaces
                            data_line = ' ' 
                        reps -= 1
                        pv = data_line[:5]
                        parsed_values.append(pv)
                        data_line = data_line[5:] 
            for i, var in enumerate(vars):
                if '=' in var:
                    raise NotImplementedError("var with '=' not implemented "+var)
                s = f'{var}={parsed_values[i]}'
                expr = fortran_to_python(s, frame)   
                exec(expr, frame.vars)
                      
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
            i = line.index('(',4)
            subroutine_name = line[4:i].strip()
            if subroutine_name == 'IFILE':
                self.file_pos = 0
                return
            raise NotImplementedError("CALL statement encountered")
            #print("call",line)
            return

        if line.startswith('GOTO'):
            line = line[4:]
            if line[0] == '(':
                i = line.index(')')
                dest = line[1:i].split(',')
                cond = line[i+1:]                
                expr = fortran_to_python(cond, frame)   
                exec('__RESULT__='+expr, frame.vars)
                i = frame.vars['__RESULT__']-1
                if i<0 or i>=len(dest):
                    # fall into next fortran line
                    return
                dest_label = dest[i]
            else:
                dest_label = line
            frame.pc = frame.labels[dest_label]            
            return       

        if line.startswith('FORMAT'):
            #raise NotImplementedError("FORMAT statement encountered")
            #print("format",line)
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
        
        expr = fortran_to_python(line, frame)   
        exec(expr, frame.vars)

    def run(self):
        self.running = True
        frame = self.stack[0]        
        while self.running:
            print(f"Current section: {frame.section_name}, PC: {frame.pc}, Line: {frame.lines[frame.pc]}")
            line = frame.lines[frame.pc]
            old_pc = frame.pc
            frame.pc += 1
            self.execute_line(frame, line)
            while self.loop_stack:
                # Multiple nested loops can end on the same line
                # We must check the end of all nests
                bottom_pc, var, loop_pc, end = self.loop_stack[-1]
                if old_pc != bottom_pc:
                    # Not at the end of the loop ... keep going
                    break
                # Increment the loop variable
                var = frame.vars[var]
                var.v += 1
                if var.v <= end:
                    # More iterations to do ... go to the top of the loop
                    frame.pc = loop_pc
                    break
                # End of loop ... check forother loops on the stack
                del self.loop_stack[-1]


if __name__ == '__main__':

    for_names = ('../../content/colossalcaveadventure/raw/adventOrg.f',
                 '../../content/colossalcaveadventure/raw/adventOrg.dat')

    # for_names = ('../../content/colossalcaveadventure/raw/advent350.for',
    #              '../../content/colossalcaveadventure/raw/advent350.dat')

    sections = forloader.load_fortran(for_names[0])
    data_lines = []
    with open(for_names[1], 'r') as f:
        for line in f:
            if not line.strip():
                continue
            data_lines.append(line.strip())

    runner = Runner(sections,data_lines)
    runner.run()
