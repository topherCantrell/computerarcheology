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

class Runner:
    def __init__(self, sections, data_lines):
        self.sections = sections
        self.stack = [fortran_env.StackFrame(self, '*')]
        self.loop_stack = []
        self.running = False
        self.data_lines = data_lines
        self.data_lines_pos = 0    

    def execute_line(self, frame, line, linenum):
        
        # The program counter is incremented before calling this function                

        if (line.startswith('IMPLICIT') or line.startswith('LOGICAL') or line.startswith('REAL') or 
            line.startswith('INTEGER') or line.startswith('EXTERNAL')):
            return
        
        if line.startswith('FORMAT'):            
            return        
        
        if line.startswith('CONTINUE'):
            return  

        if line.startswith('COMMON'):
            return run_common.run_common(line, frame)

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

        #
        # TODO not implemented yet
        #   

        if line.startswith('END'):
            raise NotImplementedError("END statement encountered")
            #print("end",line)
            return

        if line.startswith('RETURN'):
            raise NotImplementedError("RETURN statement encountered")
            #print("return",line)
            return        

        if line.startswith('STOP'):
            raise Exception(f"{linenum}:STOP statement encountered")            

        if line.startswith('PAUSE'):
            raise NotImplementedError("PAUSE statement encountered")
            #print("pause",line)
            return

        if line.startswith('TYPE'):
            raise NotImplementedError("TYPE statement encountered")
            #print("type",line)
            return

        if line.startswith('ACCEPT'):
            raise NotImplementedError("ACCEPT statement encountered")
            #print("accept",line)
            return

        if line.startswith('OPEN'):
            raise NotImplementedError("OPEN statement encountered")
            #print("open",line)
            return

        # This is a math expression
        fortran_env.exec_fortran(line, frame)

    def run(self):
        self.running = True
        frame = self.stack[0]        
        while self.running:
            print(f"Current section: {frame.section_name}, PC: {frame.pc}, Line: {frame.lines[frame.pc]}")
            line, linenum = frame.lines[frame.pc]
            old_pc = frame.pc
            frame.pc += 1
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


if __name__ == '__main__':

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
    runner.run()
