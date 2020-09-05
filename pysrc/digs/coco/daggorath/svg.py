script = """
DFCA: 84 82         ; Move to absolute (130,132)
DFCC: 70 7A         ; Line to absolute (122,112)
DFCE: 5C 7C         ; Line to absolute (124,92)
DFD0: 5E 7E         ; Line to absolute (126,94)
DFD2: 5E 82         ; Line to absolute (130,94)
DFD4: 5C 84         ; Line to absolute (132,92)
DFD6: 70 82         ; Line to absolute (130,112)
DFD8: 80 8C         ; Line to absolute (140,128)
DFDA: 84 88         ; Line to absolute (136,132)
DFDC: 84 72         ; Line to absolute (114,132)
DFDE: 78 6C         ; Line to absolute (108,120)
DFE0: 6A 76         ; Line to absolute (118,106)
DFE2: 78 70         ; Line to absolute (112,120)
DFE4: 7C 74         ; Line to absolute (116,124)
DFE6: 7C 7E         ; Line to absolute (126,124)
DFE8: FF            ; Start new line
DFE9: 64 78         ; Move to absolute (120,100)
DFEB: FC            ; Draw short lines
DFEC: E0            ;     Short line to relative (0,-4)
DFED: E2            ;     Short line to relative (4,-4)
DFEE: EE            ;     Short line to relative (-4,-4)
DFEF: E0            ;     Short line to relative (0,-4)
DFF0: F1            ;     Short line to relative (2,-2)
DFF1: 22            ;     Short line to relative (4,4)
DFF2: EE            ;     Short line to relative (-4,-4)
DFF3: 06            ;     Short line to relative (12,0)
DFF4: 2E            ;     Short line to relative (-4,4)
DFF5: E2            ;     Short line to relative (4,-4)
DFF6: 11            ;     Short line to relative (2,2)
DFF7: 20            ;     Short line to relative (0,4)
DFF8: 2E            ;     Short line to relative (-4,4)
DFF9: 22            ;     Short line to relative (4,4)
DFFA: 20            ;     Short line to relative (0,4)
DFFB: 00            ;     End of short lines
DFFC: FE            ; End of image
"""

def get_coords(s):
    i = s.find('(')
    j = s.find(')')
    return s[i+1:j]

lines = script.split('\n')
ims = ''
for line in lines:    
    line = line.strip()
    i = line.find(';')
    if i==0:
        continue
    if i>=0:
        line = line[i+1:].strip()    
    if not line:
        continue
    if line.startswith('Move to absolute'):
        ims = ims + 'M '+get_coords(line)+' '
    elif line.startswith('Line to absolute'):
        ims = ims + 'L '+get_coords(line)+' '
    elif line == 'End of image':
        print('##',ims)
        ims = ''
    elif line == 'Start new line':
        pass
    elif line == 'Draw short lines':
        pass
    elif line == 'End of short lines':
        pass
    elif line.startswith('Short line to relative'):
        ims = ims + 'l '+get_coords(line)+' '
    else:
        raise Exception('Unknown '+line)