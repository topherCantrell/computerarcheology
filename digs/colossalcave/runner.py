
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

    def collect_continues(self):
        start_line = None
        for line in self.lines:
            if line.continue_mark:
                start_line.combined_code += line.code
            else:
                start_line = line     


if __name__ == '__main__':
    runner = FortranRunner('../../content/ColossalCaveAdventure/raw/advent350.for')
    # runner = FortranRunner('../../content/ColossalCaveAdventure/raw/adventOrg.f')

    for line in runner.lines:
        linenum = str(line.code_line_num).ljust(4)
        lab = ''
        if line.label:
            lab = f'{line.label}'
        lab = lab.ljust(5)
        mark = '-'
        if line.continue_mark:
            mark = line.continue_mark
        print(f'{linenum}:{lab}{mark}{line.code}  ---- {line.combined_code}')

