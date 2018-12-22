
class Directive:
    
    def __init__(self,md):
        
        self.original = md
        self.directive = md.line.strip()[3:].strip()        
