import json

class Objects:
    
    def __init__(self,objects_name):
                
        with open(objects_name) as f:
            self._raw_objects = json.load(f)
            
        self.player_number = 0x1D-1
        self.player = self._raw_objects[self.player_number]
        self.o = {}
        for ob in self._raw_objects:
            self.o[ob['name']] = ob
    
    def has_bit(self,obj,check_bits):        
        c_bit = check_bits[1:].replace('.','')
        if len(c_bit)!=1:
            raise Exception('Expected exactly one bit:'+check_bits+':')
        #print('#',obj['bits'][1:],c_bit)
        return c_bit in obj['bits'][1:]
        
    
    def get_object_nearby(self,_adjective,name):
        player_room = self.player['location']
        ret = []
        for obj in self._raw_objects:
            if obj['word'] == name:
                # TODO what about objects held by other objects that are here?
                if obj['location'] == self.player_number:
                    ret.append(obj)
                    continue
                if obj['location'] == player_room:
                    ret.append(obj)
                    continue            
        return ret
        