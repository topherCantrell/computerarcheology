
"""
This object contains all the local variables and program counter for
a running Fortran subroutine.

  - program_counter: Line number within the list of lines of the NEXT line to run
  - locals: 
  - 
"""

class StackFrame:
    def  __init__(self, name, linenum):
        self.name = name
        self.program_counter = linenum
        self.var_types = {}
        self.commons = []
        