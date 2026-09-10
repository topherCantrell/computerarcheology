import sections
import words
import rooms
import messages

OBJ_DESC = {}
for obj in sections.SECTIONS[5]:
    info = obj.split('\t') 
    OBJ_DESC[int(info[0])] = info[1]     
    if len(info[0]) > 2:
        continue  

for obj in sections.SECTIONS[7]:
    info = obj.split('\t')    
    obj_id = int(info[0])
    obj_first = int(info[1])
    obj_second = None
    if len(info) > 2:
        obj_second = int(info[2])    

    room_1 = f'{obj_first}'
    if obj_second is None:
        room_2 = '  '
    elif obj_second == 0:
        room_2 = 'nowhere '
    elif obj_second == -1:
        room_2 = 'pack '
    else:
        room_2 = f'{obj_second}'

    desc = OBJ_DESC.get(obj_id, f'??{obj_id}??')

    print(f'{obj_id}: {room_1} {room_2}    {desc}')

    # print('>>>', obj_id, obj_first, obj_second)
