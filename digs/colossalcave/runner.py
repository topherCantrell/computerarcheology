import logging
import sys

import forloader
import fortran_env

import run_dimension
import run_if
import run_data
import run_do
import run_read
import run_common
import run_goto
import run_call
import run_pause
import run_type
import run_accept


LOGGER = logging.getLogger(__name__)

class Runner:
    def __init__(self, sections, data_lines):
        self.sections = sections
        self.stack = [fortran_env.StackFrame(self, '*')]
        self.loop_stack = []
        self.running = False
        self.data_lines = data_lines
        self.data_lines_pos = 0    
        self.breakpoints = {}

    def execute_line(self, frame, line, linenum):
        
        # The program counter is incremented before calling this function                

        if (line.startswith('IMPLICIT') or line.startswith('LOGICAL') or line.startswith('REAL') or 
            line.startswith('INTEGER') or line.startswith('EXTERNAL')):
            return
        
        if line.startswith('FORMAT'):            
            return        
        
        if line.startswith('CONTINUE'):
            return  

        if line.startswith('STOP'):
            self.running = False
            return

        if line.startswith('RETURN'):
            # TODO do we return from functions? If so we need to copy the ret value
            #raise NotImplementedError(f"RETURN statement encountered: {linenum} {line}")
            del self.stack[-1]
            return

        #

        if line.startswith('COMMON'):
            return run_common.run_common(self, line, frame)

        if line.startswith('DIMENSION'):
            return run_dimension.run_dimension(line, frame)

        if line.startswith('IF('):
            return run_if.run_if(self, line, linenum, frame)                 

        if line.startswith('DATA'):
            return run_data.run_data(line, frame)

        if line.startswith('DO') and line[2].isdigit():
            return run_do.run_do(self, line, frame)

        if line.startswith('READ'):
            return run_read.run_read(self, line, frame)

        if line.startswith('CALL'):
            return run_call.run_call(self, line, frame)

        if line.startswith('GOTO'):
            return run_goto.run_goto(line, frame)

        if line.startswith('TYPE'):
            return run_type.run_type(line, frame)

        if line.startswith('PAUSE'):
            return run_pause.run_pause(line)

        if line.startswith('ACCEPT'):
            return run_accept.run_accept(line, frame)

        #
        # TODO not implemented yet
        #           

        if line.startswith('END'):
            raise NotImplementedError(f"END statement encountered: {linenum} {line}")
            #print("end",line)
            return                             

        if line.startswith('OPEN'):
            raise NotImplementedError(f"OPEN statement encountered: {linenum} {line}")
            #print("open",line)
            return

        # This is a math expression
        fortran_env.exec_fortran(line, frame)

    def step(self):
        if not self.running:
            return
        
        frame = self.stack[-1]
        LOGGER.debug(f"Current section: {frame.section_name}, PC: {frame.pc}, Line: {frame.lines[frame.pc]}")
        line, linenum = frame.lines[frame.pc]
        old_pc = frame.pc
        frame.pc += 1

        if linenum in self.breakpoints:
            LOGGER.debug(f"Hit breakpoint at line {linenum}")
            self.breakpoints[linenum](self, frame, line, linenum)

        self.execute_line(frame, line, linenum)
        while self.loop_stack:
            # Multiple nested loops can end on the same line
            # We must check the end of all nests
            bottom_pc, var, loop_pc, end = self.loop_stack[-1]
            if old_pc != bottom_pc:
                # Not at the end of the loop ... keep going
                break
            # Increment the loop variable
            var = frame.vars[var]
            var.v += 1
            if var.v <= end:
                # More iterations to do ... go to the top of the loop
                frame.pc = loop_pc
                break
            # End of loop ... check forother loops on the stack
            del self.loop_stack[-1]


    def run(self):
        self.running = True                
        while self.running:
            frame = self.stack[0]            
            line, linenum = frame.lines[frame.pc]            
            if linenum in self.breakpoints:                
                LOGGER.debug(f"Hit breakpoint at line {linenum}")
                self.breakpoints[linenum](self, frame, line, linenum)
            self.step()

if __name__ == '__main__':
    
    def brk_shift(runner, frame, line, linenum):
        print(">>VAL>",frame.vars['VAL'],fortran_env.int_to_five(frame.vars['VAL'].v))
        print(">>DIST>",frame.vars['DIST'])
        print(">>RES>",frame.vars['RES'],fortran_env.int_to_five(frame.vars['RES'].v))
        
        sys.exit()


    def echo_var(frame, var_name):
        print(f">>>{var_name}", frame.vars[var_name], fortran_env.int_to_five(frame.vars[var_name].v))

    def brk_transitive(runner, frame, line, linenum):
        echo_var(frame,'JVERB')
        echo_var(frame,'JOBJ')
        sys.exit()

    def brk_getin(runner, frame, line, linenum):

        inp = ''
        for i in range(4):
            inp += fortran_env.int_to_five(frame.vars['A'][i+1].v)
        inps = inp.strip().split(' ')
        if len(inps)>1:
            frame.vars['TWOW'].v = 1
            frame.vars['B'].v = fortran_env.five_to_int(inps[0])
            frame.vars['C'].v = fortran_env.five_to_int(inps[1])
            frame.vars['D'].v = fortran_env.five_to_int(inp[5:10])
        else:
            frame.vars['TWOW'].v = 0
            frame.vars['B'].v = fortran_env.five_to_int(inps[0])
            frame.vars['D'].v = fortran_env.five_to_int(inp[5:10])


        # print(">>>>>"+inp)

        # echo_var(frame, 'XX')
        # echo_var(frame, 'YY')
        # echo_var(frame, 'MASK')
        # echo_var(frame, 'C')                

        # print("STOP")
        # sys.exit()

    logging.basicConfig(level=logging.INFO)

    for_names = ('../../content/colossalcaveadventure/raw/adventOrg.f',
                 '../../content/colossalcaveadventure/raw/adventOrg.dat')

    # for_names = ('../../content/colossalcaveadventure/raw/advent350.for',
    #              '../../content/colossalcaveadventure/raw/advent350.dat')

    sections = forloader.load_fortran(for_names[0])
    data_lines = []
    with open(for_names[1], 'r') as f:
        for line in f:
            if not line.strip():
                continue
            data_lines.append(line.strip())

    runner = Runner(sections,data_lines)

    runner.breakpoints[816] = brk_getin
    runner.breakpoints[468] = brk_transitive

    runner.run()
