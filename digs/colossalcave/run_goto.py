import fortran_env

def run_goto(line, frame):
    line = line[4:]
    if line[0] == '(':
        i = line.index(')')
        dest = line[1:i].split(',')
        cond = line[i+1:]                  
        i = fortran_env.get_fortran_value(cond, frame) - 1                
        if i<0 or i>=len(dest):
            # fall into next fortran line
            return
        dest_label = dest[i]
    else:
        dest_label = line
    frame.pc = frame.labels[dest_label]            
    return             