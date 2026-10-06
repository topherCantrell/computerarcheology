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
    #print("data",line)
    # Split on "/,"
    # For each, strip off trailing "/" if it is there
    # Var_names before "/" and data after
    # If "," in var_names, handle one way
    # Else another
    raise NotImplementedError("MORE TO DO IN DATA statement")            
    return