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

class FORTRANSection:
    def __init__(self, name, unit_type, params, ret_type, start_line, end_line):
        self.name = name
        self.start_line = start_line
        self.end_line = end_line
        self.unit_type = unit_type
        self.params = params
        self.ret_type = ret_type
        self.labels = {}

class FORTRANFile:
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
        self.collect_continues()

        # A fortran file can have several sections, all ending with an "END" statement.
        # The first section is the "MAIN" section. This code identifies the separate
        # sections.

        parts = []
        current_section = ["*",0,-1]
        parts.append(current_section)
        
        for pos,line in enumerate(self.lines):
            if line.continue_mark or not line.code:
                continue
            if line.code.startswith('END'):
                current_section[2] = pos
                current_section = None
                continue
            if current_section is None:
                current_section = [line.code.strip(),pos,-1]
                parts.append(current_section)
                continue

        self.sections = {}

        for name, start, end in parts:            
            params = []
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
            sec = FORTRANSection(name, unit_type, params, ret_type, start, end)
            self.sections[name] = sec

        # Make a map of subroutines and their labels.
        self.collect_labels()

    def collect_labels(self):
        for name,section in self.sections.items():
            for i in range(section.start_line, section.end_line):
                line = self.lines[i]
                if line.label is not None:
                    section.labels[line.label] = i                    
            
    def collect_continues(self):
        start_line = None
        for line in self.lines:
            if line.continue_mark:
                start_line.combined_code += line.code
            else:
                start_line = line                       

if __name__ == "__main__":
    file = FORTRANFile('../../content/ColossalCaveAdventure/raw/advent350.for')
    # file = FORTRANFile('../../content/ColossalCaveAdventure/raw/adventOrg.f')
    