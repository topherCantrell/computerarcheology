from dataclasses import dataclass
import json


@dataclass
class Object:
    name: str    
    word: str    
    location: str    
    bits: str
    max_points: int = 0
    current_points: int = 0
    short_name: str = None
    score: int = None
    description : str = None
    held_by_name : str = None
    handler_if_first_noun: list = None
    handler_if_second_noun: list = None
    handler_every_turn: list = None    
    handler_on_death: list = None

class Objects:
    
    def __init__(self,objects_name):
                
        self._objects = []
        
        with open(objects_name) as f:
            raw_objects = json.load(f)
            
        for ob in raw_objects:
            self._objects.append(Object(**ob))
            
        self.active_object = None
        self.var_object = None
        self.player_object = self.get_object_by_name('PLAYER')
                    
    def get_object(self,obj_num):
        return self._objects[obj_num]
    
    def get_object_by_name(self,obj_name):
        for ob in self._objects:
            if ob.name == obj_name:
                return ob
        return None
    
    def is_object_in_room_or_held_by_active(self, ob, room_name):
        # CoCo Bedlam 08EB
                     
        if ob.location == room_name:
            # Object is in target room -- TRUE
            return True
        
        if ob.location == 'NOWHERE':
            # Object is nowhere -- FALSE
            return False
        
        if ob.location == 'EVERYWHERE':
            # Object is everywhere -- TRUE
            return True
        
        if not ob.held_by_name:            
            # Object is not being held -- FALSE
            return False
        
        assert(ob.location is None)
        if ob.held_by_name == self.active_object.name:
            # Object is being held by target object -- TRUE
            return True
        
        # Recurse the check using the contained object
        ob = self.get_object_by_name(ob.held_by_name)   
        return self.is_object_in_room_or_held_by_active(ob, room_name)  

    def has_bit(self,obj,check_bits):        
        c_bit = check_bits[1:].replace('.','')
        if len(c_bit)!=1:
            raise Exception('Expected exactly one bit:'+check_bits+':')
        #print('#',obj['bits'][1:],c_bit)
        return c_bit in obj['bits'][1:]        
