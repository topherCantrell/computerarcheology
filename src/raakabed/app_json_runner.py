import json

from inputs import Inputs
from objects import Objects
from rooms import Rooms


objs = Objects('objects_raaka_trs80.json')
inp = Inputs('words_raaka_trs80.json','phrases_raaka_trs80.json',objs)
rms = Rooms('rooms_raaka_trs80.json')



cur = rms.find_room(objs.player['location'])

print(cur['description'])

i = input('> ')

d = inp.decode(i)
print(d.frags)
print(d.error_message)
print(d.phrase)
    
#objs.o['SERPENT_LIVE']['location'] = objs.player['location'] # Serpent
#objs.o['SWORD']['location'] = objs.player_number # Sword

#d = inp.decode('  Hit the   serpent  with sword   ')

# GAME FLOW:

# - Print the room description
# - Get the phrase/input
# - Execute general script (it calls into the rooms)
# - Run all objects "turn" scripts