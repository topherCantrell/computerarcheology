
class Directive:
    
    def __init__(self,line):
        self.original = line
        self.directive = line.line.strip()[3:].strip()        
