import code.markdown_line
from code.table_line import Table

class MemoryTable:
    
    def __init__(self,filename):
        
        #print(":"+filename+":")
        
        lines = code.markdown_line.load_file(filename)
        
        self.entries = []
        
        for md in lines:
            if type(md) is Table and md.is_memory:
                for m in md.lines[2:]:
                    cols = m.line.split('|')[1:-1]
                    addr = cols[0].strip()
                    if addr=='':
                        continue
                    taddr = addr.split(':')
                    if len(taddr)<2:
                        taddr.append(taddr[0])
                    taddr[0] = int(taddr[0],16)
                    taddr[1] = int(taddr[1],16)                    
                    self.entries.append({
                        'range' : taddr,
                        'name'  : cols[1].strip(),
                        'description' : cols[2].strip()
                    })        
     
    def find_entry(self,address):
        for e in self.entries:
            if address>= e['range'][0] and address<=e['range'][1]:
                return e
        return None    
    