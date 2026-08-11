import sections
import words
import rooms
import messages

START = [3,3,8,10,11,14,13,9,15,18,19,17,27,28,29,30,0,0,3,3]

OBJ_DESC = {
    1: 'KEYS',
    2: 'LAMP',
    3: 'GRATE',
    4: 'CAGE',
    5: 'ROD',
    6: 'STEPS',
    7: 'BIRD',
    8: 'GRATE2',
    9: 'STEPS2',
    10: 'NUGGET',
    11: 'SNAKE',
    12: 'BRIDGE',
    13: 'DIAMONDS',
    14: 'SILVER',
    15: 'JEWELRY',
    16: 'COINS',
    17: '??17??',
    18: '??18??',
    19: 'FOOD',
    20: 'BOTTLE'   
}

for key,value in OBJ_DESC.items():
    print(f'{key:02X}: {START[key-1]:02X} {value}')