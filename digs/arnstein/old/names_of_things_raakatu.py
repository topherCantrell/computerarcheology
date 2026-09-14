
ROOMS = {
    0x81: 'ROOM_GRANITE_WALLS',
    0x82: 'ROOM_ORIENTAL_RUG',
    0x83: 'DARK_PASSAGE',
    0x84: 'TOP_OF_PASSAGE',
    0x85: 'T_SHAPED_ROOM_1',
    0x86: 'GRAY_STONE_WALLS_1',
    0x87: 'ROUND_ROOM_HIGH_WALLS_1',
    0x88: 'TRIANGULAR_ROOM',
    0x89: 'SOUTH_END_CENTRAL_HALL',
    0x8A: 'T_SHAPED_ROOM_2',
    0x8B: 'GREY_STONE_WALLS_2',      # Two different spellings of "gray", "grey"
    0x8C: 'ROUND_ROOM_HIGH_WALLS_2',
    0x8D: 'PETITE_CHAMBER',
    0x8E: 'SMELLS_OF_DECAYING_FLESH',
    0x8F: 'TALL_ROOM',
    0x90: 'NORTH_END_CENTRAL_HALL',
    0x91: 'VAULT',
    0x92: 'ENTRANCE_LONG_DARK_TUNNEL_WEST',
    0x93: 'DARK_TUNNEL',
    0x94: 'ENTRANCE_LONG_DARK_TUNNEL_EAST',
    0x95: 'LARGE_ROOM',
    0x96: 'DENSE_DARK_DAMP_JUNGLE',
    0x97: 'DARK_DENSE_DAMP_JUNGLE',
    0x98: 'SEE_EAST_WALL',
    0x99: 'STANDS_SOUTH_WALL',
    0x9A: 'SEE_BRONZE_GATES',
    0x9B: 'SEE_NORTH_WALL',
    0x9C: 'STANDING_WEST_ENTRANCE',
    0x9D: 'AT_NORTH_WALL',
    0x9E: 'AT_EAST_WALL',
    0x9F: 'AT_SOUTH_WALL',
    0xA0: 'VERY_SMALL_ROOM',
    0xA1: 'SMALL_ROOM',
    0xA2: 'DARK_DAMP_DENSE_JUNGLE',
    0xA3: 'DENSE_DAMP_DARK_JUNGLE',
    0xA4: 'DAMP_DARK_DENSE_JUNGLE',
    0xA5: 'SECRET_PASSAGE',
    0xA6: 'END_OF_PASSAGE',
}

OBJECTS = {
    0x01: 'BOTTLE',
    0x02: 'POTION',
    0x03: 'RUG',
    0x04: 'DOOR_1',
    0x05: 'FOOD',
    0x06: 'STATUE_FACING_EAST',
    0x07: 'STATUE_FACING_WEST',
    0x08: 'RING',
    0x09: 'SWORD',
    0x0A: 'GARGOYLE_1',
    0x0B: 'ALTAR',
    0x0C: 'IDOL',
    0x0D: 'GATE',
    0x0E: 'LEVER_DROWNS',
    0x0F: 'LEVER_BEJEWELED',
    0x10: 'PLAQUE_PULL_LEVER',
    0x11: 'CANDLE_UNLIT',
    0x12: 'CANDLE_LIT',
    0x13: 'PLAQUE_INTO_TUNNEL',
    0x14: 'LAMP_BURNING',
    0x15: 'SERPENT_COILED',
    0x16: 'SERPENT_DEAD',
    0x17: 'HANDS',
    0x18: 'COIN',
    0x19: 'SLOT',
    0x1A: 'PLAQUE_FOR_PRICE',
    0x1B: 'DOOR_2',
    0x1C: 'DOOR_3',
    0x1D: 'PLAYER',
    0x1E: 'GARGOYLE_2',
    0x1F: 'GARGOYLE_3',
    0x20: 'WALL',
    0x21: 'VINE',
    0x22: 'CHOPSTICK',
    0x23: 'GUARD',
    0x24: 'GUARD_WARNING',
    0x25: 'GEM_1',
    0x26: 'GEM_2',
    0x27: 'ROOM',
    0x28: 'LAMP',
    0x29: 'FLOOR',
    0x2A: 'EXIT',
    0x2B: 'PASSAGE',
    0x2C: 'HOLE',
    0x2D: 'CORRIDOR',
    0x2E: 'CORNER',
    0x2F: 'BOW',
    0x30: 'ARROW',
    0x31: 'HALLWAY',
    0x32: 'CHAMBER',
    0x33: 'VAULT',
    0x34: 'ENTRANCE',
    0x35: 'TUNNEL',
    0x36: 'JUNGLE',
    0x37: 'TEMPLE',
    0x38: 'SERPENTS',
    0x39: 'PIT',
    0x3A: 'CEILING',
    0x3B: 'ALTAR',
    0x3C: 'AMBIENT_SOUNDS',
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
        
    