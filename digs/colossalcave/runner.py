from callframe import CallFrame
from fortran_file import FORTRANFile
import logging

LOGGER = logging.getLogger(__name__)


class FortranRunner:

    def _for_STOP(self, code):
        self.running = False  # Return from the "run" method     
    def _for_IMPLICIT(self, code):
        return
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
            # If we don't know about a variable (parameter or common) we need to create it
            # in our call frame. 
            if call_frame.get_var(s,auto_create=False) is None:
                LOGGER.debug(f"Creating local array {s} with dimensions {dim}")
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
            self.stack[-1].set_var(v, val)

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
    def _for_CONTINUE(self, code):
        raise Exception(f'CONTINUE not implemented yet: {code}')
    def _for_CALL(self, code):
        raise Exception(f'CALL not implemented yet: {code}')
    def _for_TYPE(self, code):
        # Always of the form "TYPE n,....."
        g = code.find(',')
        if g<0:
            g = len(code)
        label = int(code[5:g])
        params = code[g+1:].strip()
        format = self.stack[-1].formats[label].combined_code
        raise Exception(f'TYPE not implemented yet: {code}, :{label}:, :{params}:, :{format}:')    
    def _for_RETURN(self, code):
        raise Exception(f'RETURN not implemented yet: {code}')

    def _is_statement_function(self, token, params):
        # This MIGHT be a regular assignment. If the name has been declared (common or locals) then
        # this is not a function. If there are no parentheses before the = then this is not a 
        # function. If we've executed another compiled command, then it is not a function.
        if self.stack[-1].past_statement_functions:
            return False
        if not params.startswith('('):
            return False
        if self.stack[-1].get_var(token, auto_create=False) is None:
            # We have parameters and it isn't a variable we know -- must be a statement function.
            return True
        # This is an array variable we know -- not a statement function.
        return False
        

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
    
    def _for_expression(self, left, right):
        # The fortran code does assign with variable index, but it is always simple
        # lookups -- not math expressions to evaluate.
        # i = code.find('=')
        # left = code[:i].strip()
        # right = code[i+1:].strip()
        # self.evaluate_math(right)
        raise Exception(f'Expression not implemented yet: {left} = {right}')

    def evaluate_math(self, expr):
        print (">>>>>",expr)    

    DECLARE_COMMANDS = [
        'IMPLICIT', 'INTEGER', 'REAL', 'LOGICAL', 'COMMON', 'DIMENSION','DATA'
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
            'CONTINUE': self._for_CONTINUE,
            'CALL': self._for_CALL,
            'TYPE': self._for_TYPE,
            'RETURN': self._for_RETURN,
        }

        frame = CallFrame(self.fortran.sections['*'], 0, rootframe=None)
        self.stack = [frame]

        self.running = False    

    def step(self, code):
        parse = code.replace(' ', '')
        fnd = False
        for keyword, fn in self.for_functions.items():
            if parse.startswith(keyword):         
                if keyword not in self.DECLARE_COMMANDS:
                    # No more statement functions are coming.
                    self.stack[-1].past_statement_functions = True
                fnd = True
                fn(code)                    
                break
        if not fnd:
            # This MUST be an assignment or a statement function. There will always
            # be a TOKEN up front.
            i = code.find('=')
            left = code[:i].strip()
            right = code[i+1:].strip()
            token = ''
            pos = 0
            while (pos < len(left) and ((left[pos].isalpha() and left[pos].isupper()) or left[pos].isnumeric())):
                token += left[pos]
                pos += 1
            if self._is_statement_function(token, left[pos:]):
                params = left[pos+1:-1].split(',')
                self.stack[-1].statement_functions[token] = (params, right)
                LOGGER.debug(f"Statement function {token} with params {params} and right side {right}")
            else:
                self._for_expression(left,right)
                # No more statement functions are coming
                self.stack[-1].past_statement_functions = True
           

    def run(self):
        self.running = True
        while self.running:            
            # Skp over comments and continues (already collected)
            pc = self.stack[-1].program_counter
            code = self.stack[-1].lines[pc].combined_code
            pc += 1
            self.stack[-1].program_counter = pc               
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
    logging.basicConfig(level=logging.DEBUG)

    runner = FortranRunner('../../content/ColossalCaveAdventure/raw/advent350.for')
    # runner = FortranRunner('../../content/ColossalCaveAdventure/raw/adventOrg.f')
    
    # search_code()
    runner.run()
