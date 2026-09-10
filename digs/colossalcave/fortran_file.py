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

class FORTRANSection:
    def __init__(self, name, unit_type, params, ret_type):
        self.name = name
        self.unit_type = unit_type
        self.params = params # For functions and subroutines
        self.ret_type = ret_type  # For functions
        #        
        self.lines = []
        self.labels = {}        
        self.formats = {}
        self.statement_functions = {}        
        self.dimensions = {}
        self.commons = []
        self.type_hints = {}
        self.locals = {} # The starting point for variables with each stack frame

class FORTRANFile:

    def process_type_hint(self, code, section):
        i = code.find(' ')
        ty = code[:i]
        code = code[i+1:].split(',')
        for name in code:
            name = name.strip()            
            if not name:
                raise ValueError(f"Empty variable name in type hint {code}")
            section.type_hints[name] = ty        

    def process_common(self, code, section):            
            i = code.find('/ ')
            if i<0:
                i = code.find(' ')
            code = code[i+1:].split(',')
            base = self.sections['*'] 
            for name in code:               
                # Create the variable if not already in the base. If we are not in the base and
                # it doesn't exist in the base, error                
                name = name.strip()      
                section.commons.append(name)      
                if not name:
                    raise ValueError(f"Empty variable name in COMMON {code}")
                if name in base.locals:
                    # Already created -- nothing to do
                    continue
                if section.name != '*':
                    raise ValueError(f"COMMON variable {name} not in base section")
                base.locals[name] = [0]  # Assume this is not an array until We dimension things later

    def get_default_for_new_var(self, name, section):
        if name in section.type_hints:
            ty = section.type_hints[name]
            if ty == 'LOGICAL':
                return False
            if ty == 'REAL':
                return 0.0
            if ty == 'INTEGER':
                return 0
        return 0  # Default to integer
    
    def process_dimension(self, code, section):
            # Create arrays and fill them with None. Fortran starts with 1, so
            # we add one element, and the first element will never be used.
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
                dim = s[i+1:-1].split(' ')
                dim = [int(d) for d in dim]
                s = s[:i]
                section.dimensions[s] = dim
                if s in section.commons:
                    ad = self.sections['*']
                    if ad.locals[s] != [0]:
                        # We run into common variables that are dimensioned in multiple sections. 
                        # Only dimension them once.
                        continue
                else:
                    ad = section
                    if s in ad.locals:
                        # Local variables -- dimensioned one time
                        raise ValueError(f"Variable {s} already exists in section {section.name}")
                # Create this array
                if len(dim) == 1:
                    ad.locals[s] = [None]
                    default_value = self.get_default_for_new_var(s, section)
                    for i in range(dim[0]):
                        ad.locals[s].append([default_value])
                else:
                    # 2D arrays. FORTRAN lists column first
                    rows, cols = dim[1]+1, dim[0]+1
                    default_value = self.get_default_for_new_var(s, section)
                    ad.locals[s] = [None]  # Index starts at 1
                    for _ in range(rows):
                        ad.locals[s].append([None])
                        for c in range(cols):
                            ad.locals[s][-1].append([default_value])

    def get_first_word(self, code):
        code = code.strip()
        ret = ''
        pos = 0
        while pos < len(code) and (code[pos].isalpha() or code[pos].isnumeric()): 
            ret += code[pos]
            pos += 1
        return ret

    def parse_data_constant(self, s):
        if s.startswith("'"):
            return s[1:-1]  # Just a string
        if s == '.TRUE.':
            return True
        if s == '.FALSE.':
            return False
        if s.startswith('"'):
            return int(s[1:],8)  # An octal number
        return int(s)  # A decimal number
    
    def process_data(self, code, section):
        if 'I=' in code:
            # The early program initializes some data this way. Always 1 dimension.
            name = code[5:code.find('(I)')]
            values = code[code.find('/')+1:-1].split(',')                
            if name in section.commons:
                ad = self.sections['*']
            else:
                ad = section
            for i, v in enumerate(values):
                ad.locals[name][i+1] = int(v)
            return            
        # First and 2nd programs initialize data this way
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
            if '*' in clist:
                # Just one instance of this
                i = clist.find('*')
                count = int(clist[:i])
                value = self.parse_data_constant(clist[i+1:])
                clist = [value]*count
            else:
                clist = [self.parse_data_constant(c) for c in clist.split(',')]
            if len(vars) > 1:
                for i, name in enumerate(vars):
                    name = name.strip()
                    if name in section.commons:
                        ad = self.sections['*']
                    else:
                        ad = section
                    ad.locals[name] = [clist[i]]
            elif len(clist) == 1:
                name = vars[0].strip()
                if name in section.commons:
                    ad = self.sections['*']
                else:
                    ad = section
                ad.locals[name] = [clist[0]]  # Just one value
            else:                    
                name = vars[0].strip()
                if name in section.commons:
                    ad = self.sections['*']
                else:
                    ad = section
                for i, value in enumerate(clist):
                    ad.locals[name][i+1] = [value]                              

    def process_statement_function(self, code, section):
        i = code.find('(')
        j = code.find(')=')
        name = code[:i].strip()
        params = code[i+1:j].split(',')
        body = code[j+2:].strip()
        section.statement_functions[name] = (params, body)

    def __init__(self, filename):

        # Basic loading. Every line (fortran card) is a CodeLine. We figure out
        # blank lines, comments, labels, and continuations.

        self.lines = []
        linenum = 0                        
        with open(filename, 'r') as f:
            for line in f:
                linenum += 1
                self.lines.append(CodeLine(linenum, line))

        # Pull all the continuations into the "combined_code" field of the previous line.
        # After this, we can ignore lines with continuation marks.

        start_line = None
        for line in self.lines:
            if line.continue_mark:
                start_line.combined_code += line.code
            else:
                start_line = line         

        # A fortran file has multiple sections, all ending with an "END" statement.
        # The first section is the "MAIN" section. This code identifies the separate
        # sections.
                
        current_section = FORTRANSection('*', 'main', [], None)        
        self.sections = {'*': current_section}  # The base section for COMMON variables  
        
        for line in self.lines:
            if line.continue_mark or not line.code:
                continue
            if line.code.startswith('END'):
                current_section = None                
                continue
            if current_section is None:
                # Start of a new section
                name = line.combined_code
                unit_type = 'main'
                ret_type = None
                i = name.find('(')            
                if i>-1:
                    params = name[i+1:-1].split(',')
                    name = name[:i].strip()
                if 'SUBROUTINE' in name:
                    unit_type = 'subroutine'
                    name = name[11:].strip()
                elif 'FUNCTION' in name:                
                    unit_type = 'function'
                    i = name.find('FUNCTION')
                    ret_type = name[:i-1].strip()
                    name = name[i+9:].strip()                
                current_section = FORTRANSection(name, unit_type, params, ret_type)
                self.sections[name] = current_section
                continue
            
            code = line.combined_code
            if code.startswith('IMPLICIT '):
                # Ignore these -- it's always INTEGER(A-Z) in these programs.
                pass
            elif code.startswith('LOGICAL') or code.startswith('REAL') or code.startswith('INTEGER'):
                self.process_type_hint(code, current_section)
            elif code.startswith('COMMON'):
                self.process_common(code, current_section)
            elif code.startswith('DIMENSION'):
                self.process_dimension(code, current_section)
            elif code.startswith('FORMAT'):
                current_section.formats[line.label] = code
            elif code.startswith('DATA'):
                self.process_data(code, current_section)
            else:
                sf=False
                i = code.find(')=')
                if i>0:                
                    w = self.get_first_word(code)
                    if code[len(w)]=='(' and code.find(')') == i:
                        if w not in current_section.commons and w not in current_section.locals:
                            # This is a statement function declaration
                            self.process_statement_function(code, current_section)
                            sf=True
                if not sf:
                    # Just a plain old executable statement                        
                    current_section.lines.append(line)

        # Make a map of labels to lines for quick access.
        for section in self.sections.values():
            for i, line in enumerate(section.lines):
                if line.label is not None:
                    section.labels[line.label] = (line, i)

def one_per_line_2(data):
    ret = ''
    for k, v in data.items():
        ret += f"\n    {k}: {v}"
    return ret

def one_per_line(data):
    ret = ''
    for i in data:
        ret += f"\n    {i}"
    return ret

def print_info(file):

    for name, section in file.sections.items():
        print('----------------------------------')
        print(f"Section {name} ({section.unit_type}) {section.params} {section.ret_type}")
        print(f"  Type hints: {section.type_hints}")
        print(f"  Statement functions: {one_per_line_2(section.statement_functions)}")
        print(f"  Commons: {section.commons}")
        print(f"  Locals: {one_per_line_2(section.locals)}")
        print(f"  Dimensions: {section.dimensions}")
        print(f"  Formats: {section.formats}")
        print(f"  Lines:")
        for line in section.lines:
            print(f"    {line.label}:{line.combined_code}")

def search_code(file):
    for name, section in file.sections.items():
        for line in section.lines:
            # if 'CALL' in line.combined_code:
            #     i = line.combined_code.find('CALL')
            #     print(line.combined_code[i:])
            if 'READ' in line.combined_code:
                i = line.combined_code.find('READ')
                print(line.combined_code[i:])
                  

if __name__ == "__main__":
    #file = FORTRANFile('../../content/ColossalCaveAdventure/raw/advent350.for')    
    file = FORTRANFile('../../content/ColossalCaveAdventure/raw/adventOrg.f')

    #print_info(file)
    search_code(file)

    