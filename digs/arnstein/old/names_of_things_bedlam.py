
ROOMS = {
    0x81: 'MAINTENANCE_ROOM',
    0x82: 'DISPENSARY',
    0x83: 'EXAMINATION_ROOM',
    0x84: 'WEST_END_HALLWAY',
    0x85: 'PADDED_ROOM_A',
    0x86: 'PADDED_ROOM_B',
    0x87: 'EAST_WEST_HALL_A',
    0x88: 'SMALL_SQUARE_ROOM',
    0x89: 'PADDED_ROOM_C',
    0x8A: 'EAST_WEST_HALL_B',
    0x8B: 'PADDED_ROOM_D',
    0x8C: 'EAST_END_HALLWAY',
    0x8D: 'PADDED_ROOM_E',
    0x8E: 'ELECTROSHOCK_ROOM',
    0x8F: 'NORTH_END_HALLWAY',
    0x90: 'PADDED_ROOM_F',
    0x91: 'NORTH_SOUTH_HALL',
    0x92: 'KITCHEN',
    0x93: 'KENNEL',
    0x94: 'PADDED_ROOM_G',
    0x95: 'OFFICE',
    0x96: 'SOUTH_END_HALLWAY',
    0x97: 'DINING_ROOM',
    0x98: 'RECREATION_ROOM',
    0x99: 'STORAGE_SHED',
}

OBJECTS = {
    0x01: 'GREEN_DOOR_A',
    0x02: 'GREEN_DOOR_B',
    0x03: 'RED_DOOR_A',
    0x04: 'RED_DOOR_B',
    0x05: 'GREEN_DOOR_C',
    0x06: 'GREEN_DOOR_D',
    0x07: 'RED_DOOR_C',
    0x08: 'RED_DOOR_D',
    0x09: 'GREEN_DOOR_E',
    0x0A: 'GREEN_DOOR_F',
    0x0B: 'RED_DOOR_E',
    0x0C: 'GREEN_DOOR_G',
    0x0D: 'GREEN_DOOR_H',
    0x0E: 'RED_DOOR_F',
    0x0F: 'BLUE_DOOR_A',
    0x10: 'BLUE_DOOR_B',
    0x11: 'BLUE_DOOR_C',
    0x12: 'BLUE_DOOR_D',
    0x13: 'PLAYER',
    0x14: 'RED_KEY_A',
    0x15: 'BLUE_PILL_A',
    0x16: 'WINDOW_HOOK',
    0x17: 'CABINET',
    0x18: 'REFRIGERATOR',
    0x19: 'HAMBURGER_MEAT',
    0x1A: 'GUARD_DOG',
    0x1B: 'GREEN_KEY_A',
    0x1C: 'RAY_A',
    0x1D: 'RAY_B',
    0x1E: 'NAPOLEAN_A',
    0x1F: 'OBJECT_1F??',
    0x20: 'NAPOLEAN_B',
    0x21: 'OBJECT_21??',
    0x22: 'PICASSO_A',
    0x23: 'OBJECT_23??',
    0x24: 'PICASSO_B',
    0x25: 'OBJECT_25??',
    0x26: 'MERLIN_A',
    0x27: 'MERLIN_B',
    0x28: 'UNCONSCIOUS_DOCTOR_A',
    0x29: 'UNCONSCIOUS_DOCTOR_B',
    0x2A: 'HOUDINI_A',
    0x2B: 'HOUDINI_B',
    0x2C: 'HOUDINI_C',
    0x2D: 'WOMAN',
    0x2E: 'DOCTOR',
    0x2F: 'WALLS',
    0x30: 'ROOM',
    0x31: 'FLOOR',
    0x32: 'EXIT',
    0x33: 'CORNER',
    0x34: 'HALLWAY',
    0x35: 'ENTRANCE',
    0x36: 'CEILING',
    0x37: 'HANDS',
    0x38: 'SYSTEM',
    0x39: 'BLUE_PILL_B',
    0x3A: 'OBJECT_3A??',
    0x3B: 'RED_KEY_B',
    0x3C: 'DEAD_DOG',
    0x3D: 'SECRET_DOOR',
    0x3E: 'PAINTED_DOOR_A',
    0x3F: 'PAINTED_DOOR_B',
    0x40: 'GREEN_DOOR_I',
    0x41: 'GREEN_KEY_B',
    0x42: 'OBJECT_42??',
}

def get_attribute_name(value):
    # attributes=?QW.S...(liQuid, Weapon, Surface)
    ret_bits = ''
    ret_words = []
    for bit, name in ATTRIBUTES.items():
        if value & bit:
            for p in name:
                if p=='?' or p.isupper():
                    ret_bits += p
                    break
            ret_words.append(name)
        else:
            ret_bits += '.'
    return f'{ret_bits}({",".join(ret_words)})'

def get_section_name(section):
    return f'SECTION_{section:02X}_{SECTIONS[section]}'

def get_room_name(section, room):
    disk_section = ROOMS[section]
    if room not in disk_section:
        return f'RM_{section}_{room:02X}_??'
    name = disk_section[room]
    return f'RM_{section}_{name}'

def get_command_name(command):
    return f'COM_{command:02X}_{COMMANDS[command]}'

def get_routine_name(routine):
    if routine not in ROUTINES:
        return f'FN_{routine:02X}_??'
    return f'FN_{routine:02X}_{ROUTINES[routine]}'

def get_object_name(object):
    if object==0:
        return 'nothing'
    if object not in OBJECTS:
        return f'OBJ_{object:02X}_??'
    return f'OBJ_{object:02X}_{OBJECTS[object]}'

def get_destination(section, room_num):
        
        if room_num==0:
            return 'nowhere'        
        
        if room_num>=0x80:
            return get_room_name(section, room_num)
        else:
            return get_object_name(room_num)
        
    