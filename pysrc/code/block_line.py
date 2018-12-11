class Block:
    
    def __init__(self,first):
        self.lines = []
        self.type = first.line.strip()[3:].strip()        
        
    def get_type(self):
        return self.type
    
    def add_line(self,line):
        self.lines.append(line)
        