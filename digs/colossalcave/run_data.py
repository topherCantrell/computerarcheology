import fortran_env

def run_data(line, frame):
    # DATA  (JSPKT(I),I=1,16)/24,29,0,31,0,31,38,38,42,42,43,46,77,71,73,75/
    # DATA  M2/0o4000000000,0o20000000,0o100000,0o400,0o2,0/
    # DATA  SETUP/0/,BLKLIN/.TRUE./
    # DATA  MSG/100*-1/
    # DATA  MASK,BLANK/0o774000000000,' '/

    # The survey shows no ',' or '/' in string quotes
    # I=1,n in 4 places -- all the same format

    line = line[4:]
    if line[0] == '(':
        i = line.index('(',1)
        name = line[1:i]
        data = line[i+12:-1].split(',')
        for i in range(len(data)):
            #print(type(frame.vars[name][i+1]))
            frame.vars[name][i+1].v = int(data[i])
        return

    parts = line.split('/,')
    for p in parts:
        if p[-1] == '/':
            p = p[:-1]
        vs,data = p.split('/')
        vs = fortran_env.split_on_comma(vs)
        data = fortran_env.split_on_comma(data)
        if len(vs) == len(data):
            for i in range(len(vs)):
                fortran_env.exec_fortran(f"{vs[i]}={data[i]}", frame)
            continue
        if len(vs) != 1:
            raise NotImplementedError(f"Complex DATA assignment not handled: {line}")
        name = vs[0]
        for i in range(len(data)):            
            #fortran_env.exec_fortran(f"{vs[0]}({i+1})={data[i]}", frame)
            d = data[i]
            # TODO we should be able to use exec_fortran for this
            if d.startswith('"'):
                d = int(d[1:], 8)
            else:
                d = int(d)
            frame.vars[name][i+1].v = d   
    return