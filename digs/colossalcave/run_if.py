import fortran_env

def run_if(runner, line, linenum, frame):
    i = line.index('(')
    j = fortran_env.find_close_paren(line, i)
    a = line[i+1:j]
    b = line[j+1:]

    if a=='RES.LT.0':
        res = frame.vars['RES'].v
        if res>=0b1000_0000_0000_0000_0000_0000_0000_0000_0000:
            val = True
        else:
            val = False
    else:
        val = fortran_env.get_fortran_value(a, frame)

    parts = fortran_env.split_on_comma(b)
    if len(parts) == 3:        
        # This is an ancient <0, ==0, >0 construct        
        if val<0:
            frame.pc = frame.labels[parts[0]]            
        elif val==0:
            frame.pc = frame.labels[parts[1]]           
        else:
            frame.pc = frame.labels[parts[2]]
        return            
    else:    
        if val:
            # Execute the rest of the line
            runner.execute_line(frame, b, linenum)  
            return
        else:
            # Skip to the next line
            return
    