

ROOMS = {
    0x01: 'BEFORE_ENTRANCE',
    0x02: 'IN_ENTRANCE',    
    0x03: 'DESERT1',
    0x04: 'DESERT2',
    0x05: 'DESERT3',
    0x06: 'DESERT4',
    0x07: 'BENEATH_A_HOLE',
    0x08: 'CRAWLING_OVER_PEBBLES',
    0x09: 'BROKEN_POTTERY',
    0x0A: 'AWKWARD_SLOPING',
    0x0B: 'SPLENDID_CHAMBER',
    0x0C: 'SMALL_PIT_WHITE_MIST',
    0x0D: 'STEPS_LEAD_UP_DOME',
    0x0E: 'LOW_ROOM_HIEROGLYPH',
    0x0F: 'EAST_BANK_BOTTOMLESS_PIT',
    0x10: 'PHARAOHS_CHAMBER',
    0x11: 'SOUTH_SIDE_CHAMBER',
    0x12: 'HALL_OF_GODS',
    0x13: 'LITTLE_PASSAGE_SIX_FEET',
    0x14: 'EAST_END_LONG_HALL',
    0x15: 'WEST_END_FEATURELESS_HALL',
    0x16: 'CROSSOVER',
    0x17: 'DEAD_END',
    0x18: 'THRONE_CHAMBER',
    0x19: 'LOW_NS_PASSAGE',
    0x1A: 'PANEL_NORTH_WALL',
    0x1B: 'CHAMBER_OF_ANUBIS',
    0x1C: 'TWISTY_PASSAGES1',
    0x1D: 'TWISTY_PASSAGES2',
    0x1E: 'TWISTY_PASSAGES3',
    0x1F: 'TWISTY_PASSAGES4',
    0x20: 'TWISTY_PASSAGES5',
    0x21: 'TWISTY_PASSAGES6',
    0x22: 'TWISTY_PASSAGES7',
    0x23: 'TWISTY_PASSAGES8',
    0x24: 'TWISTY_PASSAGES9',
    0x25: 'TWISTY_PASSAGES10',
    0x26: 'TWISTY_PASSAGES11',
    0x27: 'TWISTY_PASSAGES12',
    0x28: 'TWISTY_PASSAGES13',
    0x29: 'TWISTY_PASSAGES14',
    0x2A: 'DEAD_END1',
    0x2B: 'DEAD_END2',
    0x2C: 'DEAD_END3',
    0x2D: 'DEAD_END4',
    0x2E: 'DEAD_END5',
    0x2F: 'DEAD_END6',
    0x30: 'DEAD_END7',
    0x31: 'DEAD_END8',
    0x32: 'DEAD_END9',
    0x33: 'DEAD_END10',
    0x34: 'BRINK_OF_LARGE_PIT',
    0x35: 'DEAD_END11',
    0x36: 'DIRTY_BROKEN_PASSAGE',
    0x37: 'BRINK_OF_CLEAN_PIT',
    0x38: 'PIT_LITTLE_STREAM',
    0x39: 'ROOM_OF_BES',
    0x3A: 'COMPLEX_JUNCTION',
    0x3B: 'ANTEROOM_OF_SEKER',
    0x3C: 'LAND_OF_DEAD',
    0x3D: 'ANCIENT_DRAWINGS',
    0x3E: 'MOON_GOD',
    0x3F: 'RAGGED_WALLS',
    0x40: 'CUL_DE_SAC',
    0x41: 'CHAMBER_OF_HORUS',
    0x42: 'FALLEN_SLAB',
    # 0x43: '',
    0x44: 'CHAMBER_OF_NEKHEBET',
    # 0x45: '',
    0x46: 'BLOCKED_FALLEN_BLOCK',
    0x47: 'CHAMBER_OF_OSIRIS',
    0x48: 'PRIESTS_BEDROOM',
    0x49: 'HIGH_PRIEST',
    # 0x4A: '',
    # 0x4B: '',
    0x4C: 'EERIE_GREEN_LIGHT',
    0x4D: 'PROFUSION_OF_LEAVES',
    0x4E: 'WEAST_END_TWOPIT',
    0x4F: 'BOTTOM_EASTERN_PIT',
    0x50: 'WEST_END_TWOPIT',
    0x51: 'BOTTOM_WEST_PIT',
}

OBJECTS = {
    0x01: 'BRIDGE_ROOM_0E',
    0x02: 'BRIDGE_ROOM_12',
    # 0x03: '',
    # 0x04: '',
    0x05: '',
    0x06: 'VENDING_MACHINE',
    0x07: 'PLANT_SMALL',
    0x08: 'PLANT_MEDIUM',
    0x09: 'PLANT_LARGE',
    # 0x0A: '',
    0x0B: 'SERPENT',
    # 0x0C: '',
    # 0x0D: '',
    0x0E: 'LAMP_OFF',
    0x0F: 'LAMP_ON',
    0x10: 'BOX',
    0x11: 'SCEPTER',
    0x12: 'PILLOW',
    0x13: 'BIRD',
    0x14: 'BIRD_IN_BOX',
    0x15: 'POTTERY',
    0x16: 'PEARL',
    0x17: 'SARCOPH_FULL',
    0x18: 'SARCOPH_EMPTY',
    0x19: 'MAGAZINES',
    0x1A: 'FOOD',
    0x1B: 'BOTTLE',
    0x1C: 'WATER',
    # 0x1D: '',
    0x1E: 'STREAM_ROOM_38',
    0x1F: 'EMERALD',
    0x20: 'VASE_ON_PILLOW',
    0x21: 'VASE',
    0x22: 'KEY',
    0x23: 'BATTERIES_FRESH',
    0x24: 'BATTERIES_WORN',
    0x25: 'GOLD',
    0x26: 'DIAMONDS',
    0x27: 'SILVER',
    0x28: 'JEWELRY',
    0x29: 'COINS',
    0x2A: 'CHEST',
    0x2B: 'NEST_EGGS',
    0x2C: 'LAMP_DEAD',
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
        
    