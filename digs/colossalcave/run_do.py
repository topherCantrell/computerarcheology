import fortran_env

def run_do(runner, line, frame):
    # fortran always calculates the loop bounds once before entering the loop
    # DO I=1,5 will run with I values 1,2,3,4,5 (inclusive)
    i = 2
    while line[i].isdigit():
        i += 1
    label = line[2:i]
    j = line.index('=',i)
    var = line[i:j]
    k = line.index(',',j)
    start = line[j+1:k]
    end = line[k+1:]
    if start.isdigit():
        start = int(start)
    else:
        start = frame.vars[start].v
    if end.isdigit():
        end = int(end)
    else:
        end = frame.vars[end].v
    if var not in frame.vars:
        frame.vars[var] = fortran_env.MemoryVar()
    frame.vars[var].v = start
    if start > end:
        # Allowed in fortran, but I haven't coded for it. I am assuming at least
        # one trip (the loop increment happens elsewhere)
        raise ValueError(f"DO loop start {start} greater than end {end}")
    runner.loop_stack.append((frame.labels[label], var, frame.pc, end))
    return
