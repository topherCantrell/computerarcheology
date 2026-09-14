from callframe import CallFrame
from fortran_file import FORTRANFile
import logging

LOGGER = logging.getLogger(__name__)


class FortranRunner:

    def _for_STOP(self, code):
        self.running = False  # Return from the "run" method    

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
        # DO 1006 K=1,14
        # DO 1102 I=1,LOCSIZ
        # DO 1042 TABNDX=1,TABSIZ
        frame = self.stack[-1]
        parts = code.split()
        label = int(parts[1])
        i = parts[2].find('=')
        var = parts[2][:i]
        a,b = parts[2][i+1:].split(',')
        frame.set_var(var, frame.evaluate_expression(a))
        frame.loops.append([frame.program_counter, label, var, b])
    def _for_GOTO(self, code):
        frame = self.stack[-1]
        code = code[4:].strip()
        if '(' in code:
            i = code.find('(')
            j = code.find(')')
            list_of_labels = code[i+1:j].split(',')
            expr = code[j+1:].strip()
            val = frame.evaluate_expression(expr) - 1
            if val < 0 or val >= len(list_of_labels):
                print("** warning: computed GOTO out of range", code, list_of_labels, expr, val)
                return  # Fall into next statement
            else:
                lab = int(list_of_labels[val].strip())
                dest = frame.section.labels[lab]
                frame.program_counter = dest[1]
                return            
        lab = int(code)
        frame = self.stack[-1]
        dest = frame.section.labels[lab]
        frame.program_counter = dest[1]
    def _for_PAUSE(self, code):
        raise Exception(f'PAUSE not implemented yet: {code}')
    def _for_READ(self, code):
        frame = self.stack[-1]
        i = code.find('(')
        j = code.find(')')
        name = code[:i].strip()
        parts = code[i+1:j].split(',')
        fillin = code[j+1:].strip()
        if parts[0] != '1':
            raise Exception('Expected unit=1 '+code)
        format = frame.formats[int(parts[1])]
        i = format.find('(')
        if i<0 or not format.endswith(')'):
            raise Exception(f'Expected a format with parentheses: {format}')
        format = format[i+1:-1]

        #TODO temporary
        data_line = self.database.read()
        if format=='G' and fillin=='SECT':
            frame.set_var('SECT', int(data_line))            
            return

        print(">>>",data_line)
        raise Exception(f'READ not implemented yet: {code} with format {format} and fillin {fillin}')
    def _for_CONTINUE(self, code):
        # In fortran, "continue" is a no-op -- not a loop control
        pass
    def _for_CALL(self, code):
        i = code.find('(')
        if i<0:
            params = []
            name = code[4:].strip()
        else:
            name = code[4:i].strip()            
            params = code[i+1:-1].split(',')
        if name=='IFILE':
            return  # Original code uses this to open the data file  
        raise Exception(f'CALL not implemented yet: {code}:{name} with params {params}')
    def _for_OPEN(self, code):
        # Nothing to do
        pass
    def _string_from_format(self, fmt, params):
        ret = ''
        fmt = fmt.strip()
        if not fmt.startswith("'") or fmt.count("'")!= 2 or not fmt.endswith("'"):
            raise Exception(f"TODO work on formatting :{fmt}:")
        return fmt[1:-1]
    def _for_TYPE(self, code):
        # Always of the form "TYPE n,....."
        g = code.find(',')
        if g<0:
            g = len(code)
        label = int(code[5:g])
        params = code[g+1:].strip()
        format = self.stack[-1].formats[label]
        i = format.find('(')
        # TODO params and do loops
        s = self._string_from_format(format[i+1:-1],params)        
        print(s)
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
    
    def _for_expression(self, left, right):
        # STEXT(LOC)=LINUSE
        # SETUP=1
        # The fortran code does assign with variable index, but it is always simple
        # lookups -- not math expressions to evaluate.
        if left.count('(') > 1 or right.count('(') > 1:
            raise Exception(f'Expression not implemented for :{left}:{right}:')

        frame = self.stack[-1]
        val = frame.evaluate_expression(right)

        ind = None
        i = left.find('(')
        if i >= 0:
            ind = [frame.evaluate_expression(left[i+1:-1])]
            left = left[:i].strip()

        frame.set_var(left, val, index=ind)

        # self.evaluate_math(right)
        #raise Exception(f'Expression :{left}:{ind}:{right}:{val}')

   
    def __init__(self, file,database):
        self.fortran = file
        self.database = database

        self.for_functions = {
            'CONTINUE': self._for_CONTINUE,
            'STOP': self._for_STOP,
            'GOTO': self._for_GOTO,
            'OPEN': self._for_OPEN,            
            'DO': self._for_DO,
            'IF(': self._for_IF,   
            #    
            'READ': self._for_READ,     
            'PAUSE': self._for_PAUSE,                        
            'CALL': self._for_CALL,
            'RETURN': self._for_RETURN,
            'TYPE': self._for_TYPE,            
        }

        frame = CallFrame(self.fortran.sections['*'], 0, rootframe=None)
        self.stack = [frame]

        self.running = False    

    def step(self, code):
        # TODO use code in the call frame
        parse = code.replace(' ', '')
        fnd = False
        for keyword, fn in self.for_functions.items():
            if parse.startswith(keyword):                         
                fnd = True
                fn(code)                    
                break
        if not fnd:
            # This MUST be an assignment or a statement function. There will always
            # be a TOKEN up front.
            i = code.find('=')
            left = code[:i].strip()
            right = code[i+1:].strip()
            self._for_expression(left,right)                       

    def run(self):
        self.running = True
        while self.running:            
            frame = self.stack[-1]
            # Skp over comments and continues (already collected)
            pc = frame.program_counter
            code = frame.lines[pc].combined_code
            pc += 1
            frame.program_counter = pc               
            self.step(code)      
            if frame.loops and frame.lines[pc-1].label == frame.loops[-1][1]:                
                # We just executed the last line of a loop. Check if we are done.
                start, _, var, toval = frame.loops[-1]
                val = frame.get_var(var)[0]+1
                frame.set_var(var, val)
                if val <= frame.evaluate_expression(toval):
                    # Not done yet -- twiddle the loop variable and go back to the start                    
                    frame.program_counter = start+1
                else:
                    # Done -- pop the loop entry off the stack and continue
                    frame.loops.pop()

class DataFile:
    def __init__(self, fname):
        self.fname = fname
        self.lines = []
        with open(fname) as f:
            for line in f:
                self.lines.append(line.strip())
        self.pos = 0

    def read(self):
        ret = self.lines[self.pos]
        self.pos += 1
        return ret

                       

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    file = FORTRANFile('../../content/ColossalCaveAdventure/raw/advent350.for')
    data_file = "../../content/ColossalCaveAdventure/raw/advent350.dat"

    #file = FORTRANFile('../../content/ColossalCaveAdventure/raw/adventOrg.f')
    #data_file = "../../content/ColossalCaveAdventure/raw/adventOrg.dat"

    data = DataFile(data_file)     

    runner = FortranRunner(file, data)
    runner.run()
