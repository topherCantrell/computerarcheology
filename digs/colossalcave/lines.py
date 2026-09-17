current_section = {
    'type': 'main',
    'args': None,
    'return_type': None,
    'lines': [],
    'labels': {}
}
sections = {'*' : current_section}

with open('../../content/colossalcaveadventure/raw/adventOrg.f', 'r') as f:
#with open('../../content/colossalcaveadventure/raw/advent350.for', 'r') as f:
#with open('../../content/colossalcaveadventure/raw/advent350.dat', 'r') as f:
#with open('../../content/colossalcaveadventure/raw/adventOrg.dat', 'r') as f:    
    for line in f:
        line = line[:-1]
        line = line.replace(chr(0x0C), '') 
        if not line.strip() or line.startswith('C'):
            # Ignore comments and blank lines
            continue               
        # If first character is a number, then this is a label. The end is the first non number
        label = None
        if line and line[0].isdigit():
            end = 0
            while end < len(line) and line[end].isdigit():
                end += 1
            label = line[:end]
            line = line[end:]
            current_section['labels'][label] = len(current_section['lines'])
        # Skip to next real character
        while line.startswith(' ') or line.startswith('\t'):
            line = line[1:]
        # If this is a continuation line, append to the last line in the current section
        continue_char = None        
        if line and line[0].isdigit():
            current_section['lines'][-1] += line[1:]            
            continue        
        # Start other sections
        if line.startswith('LOGICAL FUNCTION') or line.startswith('INTEGER FUNCTION') or line.startswith('SUBROUTINE'):
            if line.startswith('SUBROUTINE'):
                type = 'subroutine'
                ret_type = None
                line = line[len('SUBROUTINE'):]
            else:
                type = 'function'
                ret_type = line.split()[0]
                line = line[line.index('FUNCTION')+8:]
            i = line.find('(')
            if i<0:
                name = line
                args = []
            else:
                name = line[:i]
                args = line[i+1:line.index(')')].split(',')
            current_section = {
                'name': name,
                'type': type,
                'return_type': ret_type,
                'args': args,
                'lines': [],
                'labels': {}
            }
            sections[name] = current_section
            continue

        current_section['lines'].append(line)

class StackFrame:
    def __init__(self, section_name):
        self.section_name = section_name
        self.vars = {}
        self.lines = sections[section_name]['lines']
        self.pc = 0

class MemoryVar:
    def __init__(self):
        self.v = 0

def get_var(frame, name):
    if name not in frame.vars:
        frame.vars[name] = MemoryVar()
    return frame.vars[name]

stack = [StackFrame('*')]

# for name, section in sections.items():
#     print(f"Section: {name}, Type: {section['type']}, Return Type: {section['return_type']}, Args: {section['args']}")
#     pos = 0
#     for line in section['lines']:
#         print(f"  {pos} {line}")
#         pos += 1
#     for label, line_num in section['labels'].items():
#         print(f"  Label: {label} at line {line_num}")

frame = stack[-1]
while True:
    print(f"Current section: {frame.section_name}, PC: {frame.pc}, Line: {frame.lines[frame.pc]}")
    line = frame.lines[frame.pc]
    if line.startswith('IMPLICIT ') or line.startswith('LOGICAL ') or line.startswith('REAL ') or line.startswith('INTEGER '):
        frame.pc += 1
        continue

    if line.startswith('COMMON'):
        if frame.section_name == '*':
            # Ignore these lists in the root section
            frame.pc += 1
            continue
        else:
            # In other sections, copy the pointers from the root
            raise NotImplementedError(f"COMMON block in section {frame.section_name} not implemented")

    if line.startswith('DIMENSION'):
        line = line[9:].replace(' ', '')
        line = line[:-1].split('),')
        for entry in line:
            i = entry.index('(')
            name = entry[:i]
            dims = entry[i+1:].split(',')
            if name not in frame.vars:
                frame.vars[name] = []
                if len(dims) == 1:                    
                    for _ in range(int(dims[0])+1):
                        frame.vars[name].append([0])
                elif len(dims) == 2: # MUST be a 2D array ... that's all we support
                    for _ in range(int(dims[0])+1):
                        frame.vars[name].append([0])
                        for _ in range(int(dims[1])+1):
                            frame.vars[name][-1].append([0])
                else:
                    raise NotImplementedError(f"Array with more than 2 dimensions not implemented: {line}")
        frame.pc += 1
        continue

    raise NotImplementedError(f"Line not implemented: {line}")

    frame.pc += 1
