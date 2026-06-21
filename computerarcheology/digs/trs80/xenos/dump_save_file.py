
import names_of_things

with open('d:/git/computerarcheology/content/trs80/xenos/roms/ssvdobjs.dat', 'rb') as f:
        data = f.read()

# TODO object attributes dumper in names_of_things
# TODO show hitpoints here
pos = 0
obj_num = 0
while pos < len(data):
    fd = False
    line = f'{pos:04X}: {data[pos+0]:02X} {data[pos+1]:02X} {data[pos+2]:02X}'
    p = pos
    pos += 3
    if pos < len(data) and data[pos] == 2:
        line += f' {data[pos+0]:02X} {data[pos+1]:02X} {data[pos+2]:02X}'
        pos += 3
        fd = True

    obj_num += 1
    obj_text = names_of_things.get_object_name(obj_num)
    obj_text = obj_text.ljust(35)

    room_number = data[p+0]    
    ds = data[p+1]& 0x0F
    room_text = names_of_things.get_destination(ds,room_number)
    room_text = room_text.ljust(30)
    a2 = data[p+1] & 0xF0
    atts = data[p+2]

    ext_atts_text = f'{a2:08b}'
    ext_atts_text = ext_atts_text[0:4]+'....'
    atts_text = f'{atts:08b}'
    
    line = line.ljust(25)
    line += f'; {obj_text} Location: {room_number:02X} {room_text} ext_atts={ext_atts_text} attributes={atts_text}'
    print(line)
    
