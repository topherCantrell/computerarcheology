import json


class Rooms:
    
    def __init__(self,fname):        
        with open(fname) as f:
            self._raw_rooms = json.load(f)
            
    def find_room(self,name):
        for room in self._raw_rooms:
            if room['name'] == name:
                return room
            
        return None
    