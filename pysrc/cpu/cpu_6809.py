import os
import json

class CPU_6809:
    
    def __init__(self):

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'6809.js')) as f:
            data = json.load(f)
            
        self.opcodes = []
        self._data_map = {}
        
        # The "post" forms will be rippled through regular mnemonics
        self.posts = []
        for entry in data:
            if 'post' in entry:
                self.posts.append(entry)
                
        # Expand the "post" mnemonics
        for entry in data:
            if 'mnem' in entry:
                if 'y' in entry['mnem']:
                    for post in self.posts:
                        new_mnem = entry['mnem'].replace('y',post['post'])
                        new_code = entry['code'].replace('yy',post['code'])
                        new_entry = {'mnem' : new_mnem, 'code' : new_code, 'bus':entry['bus']}
                        self.opcodes.append(new_entry)
                else:
                    self.opcodes.append(entry)
                    
        for op in self.opcodes:
            g = op['code'][:2]
            if g in self._data_map:
                self._data_map[g].append(op)
            else:
                self._data_map[g] = [op]        
    
    def get_opcode(self,mnem):
        for entry in self.opcodes:
            if entry['mnem']==mnem:
                return entry
        return None
    
    def get_alias(self,op):
        if 'alias' in op:
            return op['alias']
        else:
            return None
        
    def is_bus_x(self,op):
        return 'x' in op['bus']
            
    def is_bus_r(self,op):
        return 'r' in op['bus']
    
    def is_bus_w(self,op):
        return 'w' in op['bus']
    
    def is_bus_rw(self,op):
        return self.is_bus_r(op) and self.is_bus_w(op)
    
    def is_memory_reference(self,op):
        s = op['code']
        if 'p' in s or 's' in s or 't' in s or 'r' in s:
            return True
        return False
    
    def _does_op_fit(self,g,t):
        if len(g) != len(t):
            return False
        for i in range(len(g)):
            if t[i].islower():
                continue
            if g[i]!=t[i]:
                return False
        return True
    
    def pick_opcode_from_aliases(self,mnem,opcodes):
        for op in opcodes:
            if op['mnem'].startswith(mnem[0]):
                return op
        return None
        
    def get_opcode_from_data(self,data):        
        ret = []
        g = ''
        for d in data:
            g = g + '{:02X}'.format(d)
        if not g[:2] in self._data_map:
            return []
        for op in self._data_map[g[:2]]:
            if self._does_op_fit(g,op['code']):
                ret.append(op)
        return ret
        

