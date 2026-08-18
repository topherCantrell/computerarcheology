from callframe import CallFrame
from fortran_file import FORTRANFile


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
        call_frame = self.stack[-1]
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
            # If we don't know about a variable (parameter or common) we need to create it.
            if call_frame.get_var(s,auto_create=False) is None:
                dim = dim.split(' ')
                dim = [int(d) for d in dim]
                if len(dim) == 1:
                    call_frame.locals[s] = [None]*(dim[0]+1)                    
                else:
                    # 2D arrays. FORTRAN lists column first
                    rows, cols = dim[1]+1, dim[0]+1
                    matrix = [[None for _ in range(cols)] for _ in range(rows)]
                    call_frame.locals[s] = matrix            

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

    def _for_IF(self, code):        
        # This breaks with parentheses in a string constant in an expression        
        e_start = code.find('(')
        e_end = CallFrame.find_close_paren(code, e_start)        
        expr = code[e_start+1:e_end]        
        cmd = code[e_end+1:].strip()
        result = self.stack[-1].evaluate_expression(expr)        
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
    def _for_RETURN(self, code):
        raise Exception(f'RETURN not implemented yet: {code}')

    def _is_statement_function(self, code):
        # This MIGHT be a regular assignment. If the name has been declared (common, etc) then
        # this is not a function. If there are no parentheses before the = then this is not a 
        # function. If we've executed another compiled command, then it is not a function.
        if self.stack[-1].past_statement_functions:
            return False
        # TODO get the left-hand name. if we know it, return False

        

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

    DECLARE_COMMANDS = [
        'IMPLICIT', 'INTEGER', 'REAL', 'LOGICAL', 'COMMON', 'DIMENSION','DATA', 
    ]

    def __init__(self, filename):
        self.fortran = FORTRANFile(filename)        

        self.for_functions = {
            'IMPLICIT': self._for_IMPLICIT,
            'INTEGER': self._for_INTEGER,
            'REAL': self._for_REAL,
            'LOGICAL': self._for_LOGICAL,
            'COMMON': self._for_COMMON,
            'DIMENSION': self._for_DIMENSION,
            'DATA': self._for_DATA,
            #
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
            'RETURN': self._for_RETURN,
        }

        frame = CallFrame('*', 0)
        self.stack = [frame]

        self.running = False    

    def step(self, code):
        print(">>>> HERE",code)
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

            name = ''
            pos = 0
            while code[pos].isalpha() and code[pos].isupper():
                name += code[pos]
                pos += 1
            print(">>>", name)
            raise "STOP"


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
                line = self.fortran.lines[pc]
                if line.continue_mark:
                    pc += 1
                    continue
                if not line.combined_code:
                    pc += 1
                    continue
                break
            self.stack[-1].program_counter = pc
            code = line.combined_code
            self.stack[-1].program_counter += 1 
            
            self.step(code)        
                       

def search_code():
    for line in runner.lines:
        if line.comment or line.continue_mark:
            continue
        if not line.combined_code:
            continue
        if line.combined_code.startswith('FORMAT'):
            print('>>>', line.combined_code)                          

if __name__ == '__main__':
    runner = FortranRunner('../../content/ColossalCaveAdventure/raw/advent350.for')
    # runner = FortranRunner('../../content/ColossalCaveAdventure/raw/adventOrg.f')
    
    # search_code()
    runner.run()
