
class CodeLine:

    def __init__(self, code_line_num, line):

        self.comment = None
        self.label = None
        self.continue_mark = None
        self.code = None

        self.code_line_num = code_line_num
        self.line = line[:-1]

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
        self.code = g.strip()
        print(":", self.label, ':',self.continue_mark, ':',self.code)


class FortranRunner:

    def __init__(self, filename):
        self.lines = []
        linenum = 0
        with open(filename, 'r') as f:
            for line in f:
                linenum += 1
                self.lines.append(CodeLine(linenum, line))                


if __name__ == '__main__':
    runner = FortranRunner('adventure.f')
    # print(runner.lines)