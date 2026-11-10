import fortran_env

def run_accept(line, frame):
    g = input().upper()

    parts = fortran_env.split_on_comma(line[6:])    
    specs = frame.decoded_formats[parts[0]] 

    if specs != ['A5','A5','A5','A5']:
        # TODO when we get to the 350 version
        raise NotImplementedError("Only specific ACCEPT formats are supported")

    # g = g.ljust(20,' ')  # This is the way fortran does these

    if len(parts)!=2 or '=' not in parts[1]:
        raise ValueError("Invalid ACCEPT statement format")

    store, var, start, end = fortran_env.parse_loop_parts(parts[1])
    start = fortran_env.get_fortran_value(start, frame)
    end = fortran_env.get_fortran_value(end, frame)
    data = []
    for i in range(5):
        v = g[i*5:(i+1)*5]
        if not v:
            v = ' '
        data.append(fortran_env.five_to_int(v))
    # print(">>>>>", data)
    # for d in data:
        # print("  :", fortran_env.int_to_five(d))

    pos = 0
    fortran_env.exec_fortran(f'{var}={start}', frame)
    while True:        
        fortran_env.exec_fortran(f'{store}={data[pos]}', frame)
        pos += 1
        fortran_env.exec_fortran(f'{var}={var}+1', frame)
        c = fortran_env.get_fortran_value(var, frame)
        if c > end:
            break