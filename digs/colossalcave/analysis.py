from fortran_file import FORTRANFile

def _extract_commons(line):
    ret = []
    if '/' in line:
        i = line.index('/ ')
        line = line[i+2:].strip()
    else:
        line = line[7:].strip()
    vals = line.split(',')
    for val in vals:
        ret.append(val.strip())
    return ret

def commons(file):
    # All COMMON vars are in the main function. No routine declares commons that are not in main.
    root = file.sections['*']
    root_commons = []
    for i in range(root.start_line, root.end_line):        
        line = file.lines[i]
        if not line.combined_code:
            continue
        if 'COMMON' in line.combined_code:
            cs = _extract_commons(line.combined_code)
            root_commons.extend(cs)

    print("Root COMMONS:", set(root_commons))

    for name,section in file.sections.items():
        if name == '*':
            continue
        sec_commons = []
        for i in range(section.start_line, section.end_line):        
            line = file.lines[i]
            if not line.combined_code:
                continue
            if 'COMMON' in line.combined_code:
                cs = _extract_commons(line.combined_code)
                sec_commons.extend(cs)
        print(f"{name} COMMONS:", set(sec_commons) - set(root_commons))

def dimensions(file):
    # ad350 has one 2D array, HINTS. The array is always accessed with X,Y -- never a pointer to one column
    # adOrg has one 2D array, LLINE. The array is always accessed with X,Y -- never a pointer to one column
    for line in file.lines:
        if not line.combined_code:
            continue
        if 'DIMENSION' in line.combined_code:
            print(line.combined_code)
                      

if __name__ == '__main__':
    # file = FORTRANFile('../../content/ColossalCaveAdventure/raw/advent350.for')
    file = FORTRANFile('../../content/ColossalCaveAdventure/raw/adventOrg.f')
    
    # dimensions(file)
    commons(file)
