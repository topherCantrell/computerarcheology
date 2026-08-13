from stackframe import StackFrame

class CodeLine:

    def __init__(self, code_line_num, line):

        self.comment = None
        self.label = None
        self.continue_mark = None
        self.code = None
        self.combined_code = None

        # Rules the two code files we have:
        # - If it starts with a number, the number is a label

        self.code_line_num = code_line_num
        self.line = line
        if self.line.endswith('\n'):
            self.line = self.line[:-1]

        # Blank lines and comments -- no code
        if self.line.startswith('C') or self.line.strip()=='':
            self.comment = self.line[1:].strip()
            return

        g = self.line

        if g[0].isnumeric():
            i = g.find('\t')
            self.label = int(g[:i])
            g = g[i+1:]
        else:
            g = g[1:]

        if g[0].isnumeric():            
            self.continue_mark = g[0]
            g = g[2:]
        self.code = g
        self.combined_code = self.code

class FortranRunner:

    def _for_STOP(self, code):
        self.running = False  # Return from the "run" method     
    def _for_IMPLICIT(self, code):
        return  # Don't care (everything is integer in this program)
    def _for_REAL(self, code):
        vars = code[5:].strip().split(',')
        for v in vars:
            self.stack[-1].var_types[v.strip()] = 'REAL'
        return
    def _for_LOGICAL(self, code):
        vars = code[8:].strip().split(',')
        for v in vars:
            self.stack[-1].var_types[v.strip()] = 'LOGICAL'
        return
    def _for_INTEGER(self, code):
        vars = code[8:].strip().split(',')
        for v in vars:
            self.stack[-1].var_types[v.strip()] = 'INTEGER'
        return        
            
    def _for_COMMON(self, code):
        if '/' in code:
            i = code.find('/')
            i = code.find('/', i+1)+1
        else:
            i = 7
        vars = code[i:].strip().split(',')
        for v in vars:
            self.stack[-1].commons.append(v.strip())
        return
    def _for_DIMENSION(self, code):
        # Create arrays and fill them with None. Fortran starts with 1, so
        # we add one element, and the first element will never be used.
        # SUBROUTINEs can use COMMON variables and thus re-dimension them. We
        # only initalize them once.
        code = code[9:].strip()
        # Can't split on "," because of multi-dimensional arrays. First, a little preprocessing to make that
        # a space. Then we can split on ",".
        code_new = ''
        level = 0
        for c in code:
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
            if c == ',' and level > 0:
                code_new += ' '
            else:
                code_new += c
        specs = code_new.split(',')
        for s in specs:
            i = s.find('(')
            dim = s[i+1:-1]
            s = s[:i]
            if s not in self.variables:
                dim = dim.split(' ')
                dim = [int(d) for d in dim]
                if len(dim) == 1:
                    self.variables[s] = [None]*(dim[0]+1)                    
                else:
                    # 2D arrays. FORTRAN lists column first
                    rows, cols = dim[1]+1, dim[0]+1
                    matrix = [[None for _ in range(cols)] for _ in range(rows)]
                    self.variables[s] = matrix      
      
    def _for_END(self, code):
        return  # Don't care       

    def _for_IF(self, code):        
        raise Exception(f'IF not implemented yet: {code}')    
    def _for_DATA(self, code):
        raise Exception(f'DATA not implemented yet: {code}')
    def _for_DO(self, code):
        raise Exception(f'DO not implemented yet: {code}')        
    def _for_GOTO(self, code):
        raise Exception(f'GOTO not implemented yet: {code}')
    def _for_PAUSE(self, code):
        raise Exception(f'PAUSE not implemented yet: {code}')
    def _for_READ(self, code):
        raise Exception(f'READ not implemented yet: {code}')
    def _for_FORMAT(self, code):
        raise Exception(f'FORMAT not implemented yet: {code}')
    def _for_CONTINUE(self, code):
        raise Exception(f'CONTINUE not implemented yet: {code}')
    def _for_CALL(self, code):
        raise Exception(f'CALL not implemented yet: {code}')
    def _for_TYPE(self, code):
        raise Exception(f'TYPE not implemented yet: {code}')
    def _for_SUBROUTINE(self, code):
        raise Exception(f'SUBROUTINE not implemented yet: {code}')
    def _for_RETURN(self, code):
        raise Exception(f'RETURN not implemented yet: {code}')
    def _for_expression(self, code):
        raise Exception(f'Expression not implemented yet: {code}')

    # Calling a subroutine is pass by reference. The subroutine can modify the variables passed by the caller.

    # We ignore IMPLICIT. Our code only uses INTEGER(A-Z)

    # The ORG uses a float RAN but the 350 uses a defined INT function.

    # ORG uses one unnamed COMMON blocks. We'll name it "*" for convinience.

    # None of the COMMON blocks change the name of the variables

    # We treat the main program as a subroutine "*"

    # Each subroutine has a map of dict of variables.

    # Look for variables by name in the following order:
    # - The common blocks
    # - The subroutine's parameters    
    # - The subroutine's local variables    
    # - Create the local variable with value 0

    def __init__(self, filename):
        self.lines = []
        linenum = 0
        self.labels = None
        self.variables = {}
        with open(filename, 'r') as f:
            for line in f:
                linenum += 1
                self.lines.append(CodeLine(linenum, line))   
        self.collect_continues()
        self.collect_labels()

        self.for_functions = {
            'IMPLICIT': self._for_IMPLICIT,
            'INTEGER': self._for_INTEGER,
            'REAL': self._for_REAL,
            'LOGICAL': self._for_LOGICAL,
            'COMMON': self._for_COMMON,
            'DIMENSION': self._for_DIMENSION,
            'DATA': self._for_DATA,
            'DO': self._for_DO,
            'IF(': self._for_IF,
            'STOP': self._for_STOP,
            'GOTO': self._for_GOTO,
            'PAUSE': self._for_PAUSE,
            'READ': self._for_READ,
            'FORMAT': self._for_FORMAT,
            'CONTINUE': self._for_CONTINUE,
            'CALL': self._for_CALL,
            'TYPE': self._for_TYPE,    
            'SUBROUTINE': self._for_SUBROUTINE,
            'RETURN': self._for_RETURN,
            'END': self._for_END
        }

        frame = StackFrame('*', 0)
        self.stack = [frame]

        self.running = False

    def collect_continues(self):
        start_line = None
        for line in self.lines:
            if line.continue_mark:
                start_line.combined_code += line.code
            else:
                start_line = line   

    def collect_labels(self):
        # Labels can repeat in different subroutines. We collect subroutines with "*" as the root level.
        current_subroutine = {}
        self.labels = {'*': (0, current_subroutine)}
        t = '*'
        for pos, line in enumerate(self.lines):           
            if line.code and line.code.startswith('SUBROUTINE'):
                t = line.code[10:].replace(' ', '')
                i = t.find('(')
                params = t[i+1:-1].split(',')
                for j,item in enumerate(params):
                    params[j] = item.strip()
                subname = t[:i]
                current_subroutine = {}
                self.labels[subname] = (pos, params, current_subroutine)
            else:
                if line.label:
                    current_subroutine[line.label] = pos     

    def run(self):
        self.running = True
        while self.running:            
            # Skp over comments and continues (already collected)
            pc = self.stack[-1].program_counter
            while True:
                if self.lines[pc].continue_mark:
                    pc += 1
                    continue
                if not self.lines[pc].combined_code:
                    pc += 1
                    continue
                break
            self.stack[-1].program_counter = pc

            code = self.lines[pc].combined_code
            parse = code.replace(' ', '')
            fnd = False
            for keyword, fn in self.for_functions.items():
                if parse.startswith(keyword):                    
                    fnd = True
                    fn(code)                    
                    break
            if not fnd:
                i = code.find('=')                
                self._for_expression(code)            
            self.stack[-1].program_counter += 1            


if __name__ == '__main__':
    runner = FortranRunner('../../content/ColossalCaveAdventure/raw/advent350.for')
    # runner = FortranRunner('../../content/ColossalCaveAdventure/raw/adventOrg.f')

    # for line in runner.lines:
    #     linenum = str(line.code_line_num).ljust(4)
    #     lab = ''
    #     if line.label:
    #         lab = f'{line.label}'
    #     lab = lab.ljust(5)
    #     mark = '-'
    #     if line.continue_mark:
    #         mark = line.continue_mark
    #     print(f'{linenum}:{lab}{mark}{line.code}  ---- {line.combined_code}')

    runner.run()

