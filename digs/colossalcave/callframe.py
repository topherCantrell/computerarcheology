import logging

LOGGER = logging.getLogger(__name__)


class CallFrame:

    """    
    All variable storage is in the "locals" dict through the call stack. All COMMON variable refer to the
    root call frame (in the "adventure" implementation).

    Fortran is a pass-by-reference language. The "locals" dict holds mutable containers for variables. I use a
    single entry list for each variable.

    Fortran arrays begin at 1. I use a "None" in entry 0 of each array to simplify the indexing.

    Each routine can define single-statement functions that apply only within the routine.
    
    """

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

    def __init__(self, section, linenum, rootframe):
        self.section = section  # Just for debugging
        self.program_counter = linenum  # Next line to execute        
        self.lines = section.lines  # The lines of code in this subroutine
        self.rootframe = rootframe  # The root call frame (the main program)

        self.var_types = {}  # Type hint: name->type
        self.params = [] # The incoming parameters
        self.commons = []  # The declared COMMON vars
        self.locals = {}  # Actual storage name->value

        self.past_statement_functions = False

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


    def get_var(self, name, index=None, auto_create=True):
        # Check if the name is in the root COMMON. If so use that.
        # Otherwise, it has to be in the current call frame
        d = self.locals
        if self.rootframe and name in self.commons:
            d = self.rootframe.locals
        if name in d:
            ret = d[name]
            if index is not None:
                for i in index:
                    ret = ret[i]
            return ret
        if not auto_create:
            # The caller is checking if the variable exists
            return None
        if index is not None:
            # The DIMENSION statement creates these
            raise Exception("Can't auto-create an array variable", name, index)
        self.locals[name] = [0]
        return self.locals[name]        

    def set_var(self, name, value, index=None):
        ptr = self.get_var(name, index)
        ptr[0] = value

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
            value = self.get_var(name)[0]
            refs[name] = value

        LOGGER.debug(f"Evaluating expression: {expr2} with refs: {refs}")
        
        result = eval(expr2, None, refs)
        return result
