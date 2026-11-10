import forloader
import fortran_env

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
        
    def decode_line(self, line, linenum):
        
        # The program counter is incremented before calling this function             

        # if "'" in line:
        #     print(line)
        #     return
        # return

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
            print("if",line)
            i = find_close_paren(line, 2)+1
            # if '.AND.' in line or '.OR.' in line:
            #     print("if", line)
            self.decode_line(line[i:],linenum)
            return

        if line.startswith('END'):
            #print("end",line)
            return

        if line.startswith('RETURN'):
            #print("return",line)
            return

        if line.startswith('CALL'):
            #print("call",line)                
            # i = line.find('(')
            # if i<0:
            #     # Function takes nothing
            #     return
            # params = fortran_env.split_on_comma(line[i+1:-1])
            # for p in params:
            #     is_ref = True
            #     if '.' in p or "'" in p or p[0] == '-' or p[0].isdigit():
            #         is_ref = False
            #     if '(' in p:
            #         i = p.find('(')                                         
            #         j = find_close_paren(p, i)
            #         if p[j+1:]:
            #             is_ref = False
            #     else:
            #         if '+' in p or '-' in p:
            #             is_ref = False
            #         else:
            #             try:
            #                 int(p)
            #                 is_ref = False
            #             except ValueError:
            #                 pass
            #     mark = '  '
            #     if is_ref:
            #         mark='# '                
            #     print(mark,p)

            return

        if line.startswith('GOTO'):
            #print("goto",line)
            return

        if line.startswith('DATA'):
            #print("data",line)
            return

        if line.startswith('READ'):
            #print("read",line)
            return

        if line.startswith('FORMAT'):
            #print("format",line)
            #specs = fortran_env.split_on_comma(line[7:-1])
            #for spec in specs:
            #    print("  ", spec)
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
            #rint("type",line)
            return

        if line.startswith('ACCEPT'):
            #print("accept",line)
            return

        if line.startswith('OPEN'):
            #print("open",line)
            return

        #print(f'math {line}')
        

    def run(self):
        for section_name, section in self.sections.items():
            #print(f"-------- {section_name}")
            for line, linenum in section['lines']:
                self.decode_line(line, linenum)


if __name__ == '__main__':
    sections = forloader.load_fortran('../../content/ColossalCaveAdventure/raw/adventOrg.f')
    sur = Survey(sections)
    sur.run()

    print('----------------------------------------------------------------------------------')

    sections = forloader.load_fortran('../../content/ColossalCaveAdventure/raw/advent350.for')
    sur = Survey(sections)
    sur.run()
