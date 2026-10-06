import fortran_env

def run_read(runner, line, frame):
    i = line.index(',')
    j = line.index(')',i)
    vars = fortran_env.split_on_comma(line[j+1:])
    format_line = frame.lines[frame.labels[line[i+1:j]]][0]
    format_specs = fortran_env.split_on_comma(format_line[7:-1])
    data_line = runner.data_lines[runner.data_lines_pos]
    runner.data_lines_pos += 1
    # Specs for read are all one of these: G, A5, xG, xA5. 
    parsed_values = []
    for spec in format_specs:                
        i = spec.find('G')
        if i<0:
            i = spec.find('A')
        t = spec[i]  # Either A or G
        reps = 1
        a5 = False
        if i>0:
            reps = int(spec[:i])
        if t == 'G':
            while reps>0 and data_line:
                reps -= 1
                g, data_line = fortran_env.pop_int(data_line)
                # TODO handle less data than requested ... what filler value?
                parsed_values.append(g)                    
        else:                    
            while reps>0:
                if not data_line:
                    # If there is no more data, pad with spaces
                    data_line = ' ' 
                reps -= 1
                pv = data_line[:5]                        
                parsed_values.append(fortran_env.five_to_int(pv))
                data_line = data_line[5:] 
    dp = 0
    for var in vars:
        if '=' in var:
            var, lv, end = fortran_env.split_on_comma(var[1:-1])
            i = lv.find('=')
            start = lv[i+1:]
            v = lv[:i]
            # Init the loop
            fortran_env.exec_fortran(lv, frame)
            # End value
            end = fortran_env.get_fortran_value(end, frame)
            while fortran_env.get_fortran_value(v, frame) <= end:
                fortran_env.exec_fortran(f'{var}={parsed_values[dp]}', frame)
                dp += 1
                fortran_env.exec_fortran(f'{v}={v}+1', frame)                        
        else:
            fortran_env.exec_fortran(f'{var}={parsed_values[dp]}', frame)
            dp += 1                    
                
    return