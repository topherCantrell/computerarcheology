
class MakeWebError(Exception):

    def __init__(self, message, fname, line=None):
        self.message = message
        self.fname = fname
        self.line = line
