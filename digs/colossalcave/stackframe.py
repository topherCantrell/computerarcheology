
"""
This object contains all the local variables and program counter for
a running Fortran subroutine.

  - program_counter: Line number within the list of lines of the NEXT line to run
  - locals: 
  - 
"""

class StackFrame:

    # Calling a subroutine is pass by reference. The subroutine can modify the variables passed by the caller.
    
    # We ignore IMPLICIT. Our code only uses INTEGER(A-Z)

    # The ORG uses a float RAN but the 350 uses a defined INT function.

    # ORG uses one unnamed COMMON blocks. We'll name it "*" for convinience.

    # None of the COMMON blocks change the name of the variables

    # We treat the main program as a subroutine "*"

    # Each subroutine has a map of dict of variables.

    # Look for variables by name in the following order:
    # - The common blocks
    # - The subroutine's parameters    
    # - The subroutine's local variables    
    # - Create the local variable with value 0

    def  __init__(self, name, linenum):
        self.name = name # Just for debugging
        self.program_counter = linenum # Next line to execute
        
        self.var_types = {} # Type hint: name->type
        self.params = []  # Incoming parameters in order. List of tuples: (local_name, caller_name)
        self.commons = []  # Just a list of commons we can access (not really used)
        self.locals = {} # Actual storage name->value
        