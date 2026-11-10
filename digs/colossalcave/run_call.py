import fortran_env

def run_call(runner, line, frame):
    i = line.index('(',4)
    subroutine_name = line[4:i].strip()
    if subroutine_name == 'IFILE':
        runner.file_pos = 0
        return

    section = runner.sections[subroutine_name]
    new_frame = fortran_env.StackFrame(runner,subroutine_name)
    runner.stack.append(new_frame)

    j = fortran_env.find_close_paren(line, i)
    passing = fortran_env.split_on_comma(line[i+1:j])

    for i, arg in enumerate(section['args']):
        p = passing[i]

        is_ref = True
        if '.' in p or "'" in p or p[0] == '-' or p[0].isdigit():
            is_ref = False
        if '(' in p:
            i = p.find('(')                                         
            j = fortran_env.find_close_paren(p, i)
            if p[j+1:]:
                is_ref = False
        else:
            if '+' in p or '-' in p:
                is_ref = False
            else:
                try:
                    int(p)
                    is_ref = False
                except ValueError:
                    pass
        if is_ref:
            ref = fortran_env.get_fortran_ref(p, frame)
            new_frame.vars[arg] = ref            
        else:
            s = f'{arg}={p}'
            fortran_env.exec_fortran(s,new_frame)
    
    return