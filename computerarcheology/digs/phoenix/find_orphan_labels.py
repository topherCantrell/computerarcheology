with open('./content/arcade/phoenix/code.md') as f:
    for line in f:

        line = line.strip()

        if '3310' in line:
            print('<<<<<',line)
        
        if line and line[0] == ';' and line[-1] == ':':
            print(line)
            continue
        if ';' in line:
            line = line[:line.index(';')]        
        line = line.strip()
        if line and line[-1] == ':':
            print(line)
            continue
        if line and line[0] == ';' and line[-1] == ':':
            print(line)
            continue