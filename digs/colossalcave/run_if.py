import fortran_env

def run_if(runner, line, linenum, frame):
    i = line.index('(')
    j = fortran_env.find_close_paren(line, i)
    a = line[i+1:j]
    b = line[j+1:]
    val = fortran_env.exec_fortran(a, frame)            
    if val:
        # Execute the rest of the line
        runner.execute_line(frame, b, linenum)  
        return
    else:
        # Skip to the next line
        return
    