
class MemoryTable:
    
    def __init__(self,filename):
        
        self.entries = []
        
        with open(filename,'r') as f:
            lines = f.readlines()
            
        in_table = False
        skipped = 0
        for line in lines:
            if in_table:
                if not line[0].startswith('|'):
                    in_table = False
                else:
                    if skipped<2:
                        skipped+=1
                        continue
                    cols = line.split('|')
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
                if line.startswith('>>> memory'):
                    in_table = True
                    skipped = 0
     
    def find_entry(self,address):
        for e in self.entries:
            if address>= e['range'][0] and address<=e['range'][1]:
                return e
        return None    
    