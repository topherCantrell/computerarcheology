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

    def _parse_term(self, term):
        if term == '.TRUE.':
            return True
        if term == '.FALSE.':
            return False
        if term[0] == "'":
            return term[1:-1]  # Character string
        if term[0] == '"':
            return int(term[1:], 8)  # Octal number
        return int(term)  # Decimal number        
    
    def _for_DATA(self, code):
        code = code[5:].strip()
        pos = 0
        data_specs = []
        while True:
            vlist = ''                
            while code[pos] != '/':
                vlist += code[pos]
                pos += 1
            pos += 1
            clist = ''
            while code[pos] != '/':
                clist += code[pos]
                pos += 1
            data_specs.append((vlist, clist))
            pos += 1
            if pos >= len(code):
                break
            i = code.find(',', pos)
            if i < 0:
                raise Exception(f'Unexpected end of DATA statement: {code}')
            pos = i+1
        for vlist, clist in data_specs:
            vars = vlist.split(',')
            vals = clist.split(',')
            if len(vars) > 1:
                raise Exception(f'Must implement this one case {code}')
            if len(vals) > 1:
                raise Exception(f'Must implement this case too {code}')
            v = vars[0].strip()
            val = self._parse_term(vals[0].strip())
            self.set_var(v, val)

    def _fill_vars_in_expr(self, expr, frame):
        pass

    def _for_IF(self, code):        
        # This breaks with parentheses in a string constant in an expression        
        i = code.find('(')
        e_start = i
        level = 1
        while level > 0:
            i += 1
            if code[i] == '(':
                level += 1
            elif code[i] == ')':
                level -= 1
        e_end = i
        expr = code[e_start+1:e_end]
        expr2 = expr.replace('.EQ.', '==').replace('.NE.', '!=').replace('.LT.', '<').replace('.LE.', '<=').replace('.GT.', '>').replace('.GE.', '>=')
        expr2 = expr2.replace('.AND.', ' and ').replace('.OR.', ' or ')
        # This breaks with double quotes in a string constant in an expression (octal)
        expr2 = expr2.replace('"', '0o')
        expr2 = self._fill_vars_in_expr(expr2, self.stack[-1])
        cmd = code[e_end+1:].strip()
        print(">>>",expr,':::',cmd,'::',expr2)
        # TODO function calls in the expression to fortran functions
        # TODO change system calls to lower case with "self." prefix
        # TODO now any capital letter in the expression is a variable. If the character after the variable
        # is a "(" then convert it to a python "[]". Fill out the locals map
        result = eval(expr2, None, {'SETUP': 0})
        if result:
            self.step(cmd)          
    
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

    def _for_statement_function(self, code):
        i = code.find('=')
        left = code[:i].strip()
        right = code[i+1:].strip()
        i = left.find('(')
        params = left[i+1:-1].split(',')
        left = left[:i].strip()
        
        for j,item in enumerate(params):
            params[j] = item.strip()
        self.statement_functions[left] = (params, right)        
    
    def _for_expression(self, code):
        # The fortran code does assign with variable index, but it is always simple
        # lookups -- not math expressions to evaluate.
        i = code.find('=')
        left = code[:i].strip()
        right = code[i+1:].strip()
        self.evaluate_math(right)
        raise Exception(f'Expression not implemented yet: {code}')

    def evaluate_math(self, expr):
        print (">>>>>",expr)    

    def __init__(self, filename):
        self.lines = []
        linenum = 0
        self._if_given = False  # True with the first IF statement (signals end of statement functions)
        self.statement_functions = {}
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

    def set_var(self, varname, value):
        frame = self.stack[-1]
        if varname in frame.commons:
            # print(">>> SETVAR COMMON", varname, value)
            base_frame = self.stack[0]
            base_frame.locals[varname] = value            
        elif varname in frame.params:
            raise Exception(f'Set PARAM not implemented yet: {varname} = {value}')           
        else:
            # print(">>> SETVAR LOCAL", varname, value)
            frame.locals[varname] = value            
        

    def get_var(self, varname):
        print(">>> GETVAR", varname)
        return 0

    def step(self, code):
        parse = code.replace(' ', '')
        fnd = False
        for keyword, fn in self.for_functions.items():
            if parse.startswith(keyword):         
                if keyword == 'IF(':
                    self._if_given = True           
                fnd = True
                fn(code)                    
                break
        if not fnd:
            # A little bit of a hack here to fit the code we have. We know that
            # any "=" expression before an IF is a statement function. After the
            # first IF, there are no more statement functions.
            if not self._if_given:
                self._for_statement_function(code)
            else:               
                self._for_expression(code)   

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
            self.stack[-1].program_counter += 1 
            
            self.step(code)        
                       


if __name__ == '__main__':
    runner = FortranRunner('../../content/ColossalCaveAdventure/raw/advent350.for')
    # runner = FortranRunner('../../content/ColossalCaveAdventure/raw/adventOrg.f')

    # for line in runner.lines:
    #     if line.comment or line.continue_mark:
    #         continue
    #     if not line.combined_code:
    #         continue
    #     if line.combined_code.startswith('DATA '):
    #         print('>>>', line.combined_code)
    #         runner._for_DATA(line.combined_code)
    #         print('')               

    runner.run()
