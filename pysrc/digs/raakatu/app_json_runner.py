
import json

with open('rooms.json') as f:
    rooms = json.load(f)
    
print(rooms)