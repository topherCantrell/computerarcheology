
class ASMException(Exception):
    def __init__(self, message, line):
        super().__init__(message)
        self.line = line
