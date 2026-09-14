
class CodeLine:

    def __init__(self, code_line_num, line):

        self.comment = None
        self.label = None
        self.continue_mark = None
        self.code = None
        self.combined_code = None        

        self.code_line_num = code_line_num
        self.line = line
        if self.line.endswith('\n'):
            self.line = self.line[:-1]
        
        cn = self.line.count('\t')
        if cn > 0:
            if cn != 1:
                raise Exception(f'Unexpected number of tabs in line: {self.line}')
            
        self.line = self.line.replace('\t', ' ')

        # Blank lines and comments -- no code
        if self.line.startswith('C') or self.line.strip()=='':
            self.comment = self.line[1:].strip()
            return

        g = self.line

        if g[0].isnumeric():
            i = g.find(' ')
            self.label = int(g[:i])
            g = g[i+1:]
        g = g.strip()

        if g[0].isnumeric():
            i = g.find(' ')
            self.continue_mark = int(g[:i])
            g = g[i+1:]
        self.code = g
        self.combined_code = self.code

class FortranRunner:

    def _for_IMPLICIT(self, program_counter, code):
        return  # Don't care (everything is integer in this program)
    def _for_REAL(self, program_counter, code):
        return  # Don't care (RAN is the only REAL function we call)
    def _for_COMMON(self, program_counter, code):
        # TODO check on this. looks like we need to keep them separated
        return  # Don't care (we treat all variables as global - this code doesn't shadow)
    def _for_DIMENSION(self, program_counter, code):
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
    def _for_END(self, program_counter, code):
        return  # Don't care
    def _for_STOP(self, program_counter, code):
        self.running = False  # Return from the "run" method        

    def _for_IF(self, program_counter, code):
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
        cmd = code[e_end+1:].strip()
        print(">>>",expr,':::',cmd,'::',expr2)
        raise Exception(f'IF not implemented yet: {code}')
    
    def _for_DATA(self, program_counter, code):
        raise Exception(f'DATA not implemented yet: {code}')
    def _for_DO(self, program_counter, code):
        raise Exception(f'DO not implemented yet: {code}')        
    def _for_GOTO(self, program_counter, code):
        raise Exception(f'GOTO not implemented yet: {code}')
    def _for_PAUSE(self, program_counter, code):
        raise Exception(f'PAUSE not implemented yet: {code}')
    def _for_READ(self, program_counter, code):
        raise Exception(f'READ not implemented yet: {code}')
    def _for_FORMAT(self, program_counter, code):
        raise Exception(f'FORMAT not implemented yet: {code}')
    def _for_CONTINUE(self, program_counter, code):
        raise Exception(f'CONTINUE not implemented yet: {code}')
    def _for_CALL(self, program_counter, code):
        raise Exception(f'CALL not implemented yet: {code}')
    def _for_TYPE(self, program_counter, code):
        raise Exception(f'TYPE not implemented yet: {code}')
    def _for_SUBROUTINE(self, program_counter, code):
        raise Exception(f'SUBROUTINE not implemented yet: {code}')
    def _for_RETURN(self, program_counter, code):
        raise Exception(f'RETURN not implemented yet: {code}')
    def _for_expression(self, program_counter, code):
        raise Exception(f'Expression not implemented yet: {code}')

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
            'REAL': self._for_REAL,
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
        program_counter = 0
        self.running = True
        while self.running:
            line = self.lines[program_counter]
            if not line.code:
                program_counter += 1
                continue
            if line.continue_mark:
                program_counter += 1
                continue
            code = line.combined_code
            parse = code.replace(' ', '')
            fnd = False
            for keyword, fn in self.for_functions.items():
                if parse.startswith(keyword):                    
                    fnd = True
                    fn(program_counter, code)                    
                    break
            if not fnd:
                i = code.find('=')                
                self._for_expression(program_counter, code)            
            program_counter += 1


if __name__ == '__main__':
    # runner = FortranRunner('../../content/ColossalCaveAdventure/raw/advent350.for')
    runner = FortranRunner('../../content/ColossalCaveAdventure/raw/adventOrg.f')

    runner.run()
