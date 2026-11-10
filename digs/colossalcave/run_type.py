
import fortran_env

def run_type(line, frame):

    parts = fortran_env.split_on_comma(line[4:])    
    specs = frame.decoded_formats[parts[0]] 

    data = []
    for part in parts[1:]:
        if '=' in part:
            var, lv, end = fortran_env.split_on_comma(part[1:-1])
            i = lv.find('=')
            start = lv[i+1:]
            v = lv[:i]
            # Init the loop
            fortran_env.exec_fortran(lv, frame)
            # End value
            end = fortran_env.get_fortran_value(end, frame)
            while fortran_env.get_fortran_value(v, frame) <= end:
                val = fortran_env.get_fortran_value(var, frame)
                data.append(val)              
                fortran_env.exec_fortran(f'{v}={v}+1', frame)            
        else:
            data.append(fortran_env.get_fortran_value(part, frame))

    pos = 0
    s = ''
    for d in data:
        if specs[pos] == 'A5':
            s += fortran_env.int_to_five(d)
        else:
            raise ValueError(f"Unsupported format spec: {specs[pos]}")
    print(s)
