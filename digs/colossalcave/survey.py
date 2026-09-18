import forloader

def find_close_paren(s, start):
    # This only works if there are no "()" in string literals.
    depth = 0
    for i in range(start, len(s)):
        if s[i] == '(':
            depth += 1
        elif s[i] == ')':
            depth -= 1
            if depth == 0:
                return i
    return -1

class Survey:   
    def __init__(self, sections):
        self.sections = sections
        
    def decode_line(self, line):
        # The program counter is incremented before calling this function

        if (line.startswith('IMPLICIT') or line.startswith('LOGICAL') or line.startswith('REAL') or 
            line.startswith('INTEGER') or line.startswith('EXTERNAL')):
            #print("type",line)
            return

        if line.startswith('COMMON'):
            #print("common",line)
            return
            
        if line.startswith('DIMENSION'):
            #print("dimension",line)
            return

        if line.startswith('IF('):
            #print("if",line)
            # i = find_close_paren(line, 2)+1
            #print("if", line[:i])
            # self.decode_line(line[i:])
            return

        if line.startswith('END'):
            #print("end",line)
            return

        if line.startswith('RETURN'):
            #print("return",line)
            return

        if line.startswith('CALL'):
            #print("call",line)
            return

        if line.startswith('GOTO'):
            #print("goto",line)
            return

        if line.startswith('DATA'):
            print("data",line)
            return

        if line.startswith('READ'):
            #print("read",line)
            return

        if line.startswith('FORMAT'):
            #print("format",line)
            return

        if line.startswith('DO') and line[2].isdigit():
            #print("do",line)
            return

        if line.startswith('CONTINUE'):
            #print("continue",line)
            return

        if line.startswith('STOP'):
            #print("stop",line)
            return

        if line.startswith('PAUSE'):
            #print("pause",line)
            return

        if line.startswith('TYPE'):
            #print("type",line)
            return

        if line.startswith('ACCEPT'):
            #print("accept",line)
            return

        if line.startswith('OPEN'):
            #print("open",line)
            return

        # i = line.index('=')
        # print(f'math {line[:i].ljust(20)} = {line[i+1:]}')        
        

    def run(self):
        for section_name, section in self.sections.items():
            print(f"-------- {section_name}")
            for line in section['lines']:
                self.decode_line(line)


if __name__ == '__main__':
    sections = forloader.load_fortran('../../content/ColossalCaveAdventure/raw/adventOrg.f')
    sur = Survey(sections)
    sur.run()

    print('----------------------------------------------------------------------------------')

    sections = forloader.load_fortran('../../content/ColossalCaveAdventure/raw/advent350.for')
    sur = Survey(sections)
    sur.run()
