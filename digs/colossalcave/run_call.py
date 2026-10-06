import fortran_env

def run_call(runner, line, frame):
    i = line.index('(',4)
    subroutine_name = line[4:i].strip()
    if subroutine_name == 'IFILE':
        runner.file_pos = 0
        return
    raise NotImplementedError("CALL statement encountered")
    #print("call",line)
    return