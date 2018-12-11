import code.markdown_line
from code.directive_line import Directive

class MemoryTable:
    
    def __init__(self,filename):
        
        print(":"+filename+":")
        
        lines = code.markdown_line.load_file(filename)
        
        self.entries = []
                
        in_table = False
        skipped = 0
        for md in lines:
            if in_table:
                if not md.line.startswith('|'):
                    in_table = False
                else:
                    if skipped<2:
                        skipped+=1
                        continue
                    cols = md.line.split('|')
                    addr = cols[1].strip()
                    if addr=='':
                        continue
                    taddr = addr.split(':')
                    if len(taddr)<2:
                        taddr.append(taddr[0])
                    taddr[0] = int(taddr[0],16)
                    taddr[1] = int(taddr[1],16)                    
                    self.entries.append({
                        'range' : taddr,
                        'name'  : cols[2].strip(),
                        'description' : cols[3].strip()
                    }) 
            else:
                if type(md) is Directive and md.directive=='memory':
                    in_table = True
                    skipped = 0
     
    def find_entry(self,address):
        for e in self.entries:
            if address>= e['range'][0] and address<=e['range'][1]:
                return e
        return None    
    