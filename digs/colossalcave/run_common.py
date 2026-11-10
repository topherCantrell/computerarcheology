import fortran_env

def run_common(runner, line,frame):
    if frame.section_name == '*':
        # Ignore these lists in the root section
        return
    else:
        # In other sections, copy the pointers from the root
        if line[6] == '/':
            i = line.find('/',7)
            line = line[i+1:]
        else:
            line = line[6:]
        base_frame = runner.stack[0]
        for v in line.split(','):
            frame.vars[v] = base_frame.vars[v]
        