"""
This object contains all the local variables and program counter for
a running Fortran subroutine.

  - program_counter: Line number within the list of lines of the NEXT line to run
  - locals: 
  - 
"""


class CallFrame:

    # Calling a subroutine is pass by reference. The subroutine can modify the variables passed by the caller.

    # We ignore IMPLICIT. Our code only uses INTEGER(A-Z)

    # The ORG uses a float RAN but the 350 uses a defined INT function.

    # ORG uses one unnamed COMMON block. We'll name it "*" for convinience.

    # None of the COMMON blocks change the name of the variables

    # We treat the main program as a subroutine "*"

    # Each subroutine has a map of dict of variables.

    # Look for variables by name in the following order:
    # - The common blocks
    # - The subroutine's parameters
    # - The subroutine's local variables
    # - Create the local variable with value 0

    def __init__(self, name, linenum):
        self.name = name  # Just for debugging
        self.program_counter = linenum  # Next line to execute
        self.past_statement_functions = False

        self.var_types = {}  # Type hint: name->type
        # Incoming parameters in order. List of tuples: (local_name, caller_name)
        self.params = []
        # Just a list of commons we can access (not really used)
        self.commons = []

        self.locals = {}  # Actual storage name->value
        self.statement_functions = {}

    @staticmethod
    def find_close_paren(expr, start):
        # ADVENT SPECIFIC: This only works because there are no close parens in string constants.
        depth = 1
        pos = start+1
        while pos < len(expr):
            if expr[pos] == '(':
                depth += 1
            elif expr[pos] == ')':
                depth -= 1
                if depth == 0:
                    return pos
            pos += 1
        raise ValueError("No matching closing parenthesis found")


    def get_var(self, name, auto_create=True):
        # Look for variables by name in the following order:
        # - The common blocks
        # - The subroutine's parameters
        # - The subroutine's local variables
        # - Create the local variable with value 0
        # TODO
        return 0

    def set_var(self, name, value):
        pass

    def evaluate_expression(self, expr):
        expr2 = expr.replace('.EQ.', '==').replace('.NE.', '!=').replace(
            '.LT.', '<').replace('.LE.', '<=').replace('.GT.', '>').replace('.GE.', '>=')
        expr2 = expr2.replace('.AND.', ' and ').replace('.OR.', ' or ')
        # This breaks with double quotes in a string constant in an expression (octal)
        expr2 = expr2.replace('"', '0o')

        flat_fills = []

        pos = 0

        while pos < len(expr2):
            c = expr2[pos]
            pos += 1
            if c.isalpha() and c.isupper():
                i = pos
                while i < len(expr2) and expr2[i].isalpha() and expr2[i].isupper():
                    i += 1
                if i < len(expr2) and expr2[i] == '(':
                    # Functions, statement-functions, and array refs TODO
                    raise Exception("TODO Work to do here", expr2)
                flat_fills.append(expr2[pos-1:i])
                pos = i
            else:
                pos += 1

        refs = {}
        for name in flat_fills:
            value = self.get_var(name)
            refs[name] = value

        print(">>>", expr2, refs)
        result = eval(expr2, None, refs)
        return result
