import fortran_env

def run_dimension(line, frame):
    line = line[9:]
    line = line[:-1].split('),')
    for entry in line:
        i = entry.index('(')
        name = entry[:i]
        dims = entry[i+1:].split(',')
        if name not in frame.vars:
            frame.vars[name] = []
            if len(dims) == 1:
                frame.vars[name].append(None)  # Fortran starts at 1 (not 0)             
                for _ in range(int(dims[0])):
                    frame.vars[name].append(fortran_env.MemoryVar())
            elif len(dims) == 2: # MUST be a 2D array ... that's all we support
                frame.vars[name].append(None)  # Fortran starts at 1 (not 0)
                for _ in range(int(dims[0])):
                    frame.vars[name].append([None])  # Fortran starts at 1
                    for _ in range(int(dims[1])):
                        frame.vars[name][-1].append(fortran_env.MemoryVar())
            else:
                raise NotImplementedError(f"Array with more than 2 dimensions not implemented: {line}")
    return