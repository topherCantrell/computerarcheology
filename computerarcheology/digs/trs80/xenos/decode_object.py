import script_cursor
import language
import unpack

SECTION_DESC = {
    0x00: '??UNKNOWN_00??',
    0x01: '??UNKNOWN_01??',
    0x02: 'SHORT_NAME',
    0x03: 'DESCRIPTION',
    0x06: '??UNKNOWN_06??',
    0x07: 'IF_FIRST_NOUN',
    0x08: '??UNKNOWN_08??',
    0x09: 'HIT_POINTS',
    0x0A: 'UPON_DEATH',
    0x0C: '??UNKNOWN_0C??',
    0x10: '??UNKNOWN_10??',
    0x1D: '??UNKNOWN_1D??',
    0x5C: '??UNKNOWN_5C??',
    0x5E: '??UNKNOWN_5E??',
    0x66: '??UNKNOWN_66??',
    0x6F: '??UNKNOWN_6F??',    
}

OBJECT_NAME = {
    0x01: "PLAYER",

    0x02: "DOOR",
    0x03: "DOOR",
    0x04: "DOOR",
    0x05: "DOOR",
    0x06: "SALOON_DOOR",
    0x07: "DOOR",
    0x08: "SHERIFFS_DOOR",
    0x09: "DOOR",
    0x0A: "DOOR",
    0x0B: "SLIMS_DOOR",
    0x0C: "BOBS_DOOR",
    0x0D: "DOOR",
    0x0E: "HOTEL_DOOR",
    0x0F: "DOOR",
    0x10: "BANK_DOOR",
    0x11: "DOOR",
    0x12: "DOOR",
    0x13: "DOOR",
    0x14: "UNDERGROUND_DOOR",
    0x15: "DOOR",
    0x16: "RED_DOOR",
    0x17: "DOOR",
    0x18: "BLUE_DOOR",
    0x19: "DOOR",

    0x1A: "MASTER_KEY",
    0x1B: "BRASS_KEY_SHERIFF",
    0x1C: "SKELETON_KEY",
    0x1D: "STEEL_KEY_BANK",
    0x1E: "RED_KEY_SLIMS",
    0x1F: "SMALL_KEY_CAB",
    
    0x20: "DESK",
    0x21: "TOP_DRAWER",
    0x22: "MIDDLE_DRAWER",
    0x23: "BOTTOM_DRAWER",
    0x24: "CROWBAR",
    0x25: "WANTED_POSTER",
    0x26: "GUN_CABINET",
    0x27: "SHOTGUN",
    0x28: "SHOTGUN",
    # 0x29
    # 0x2A
    0x2B: "GAS_PUMP",
    0x2C: "PADLOCK",
    0x2D: "JACK-O-MATIC",
    0x2E: "RUSTY_JEEP",
    0x2F: "FLAT_TIRE",
    0x30: "SPARE_TIRE",
    0x31: "SPHORX",
    0x32: "SHOVEL",
    0x33: "RATTLE_SNAKE",
    0x34: "DEAD_SNAKE",
    # 0x35,
    0x36: "FOOD",
    0x37: "STEEL_SAFE",
    0x38: "MONEY",
    0x39: "DYNAMITE",
    0x3A: "CONTROL_PANEL",
    0x3B: "RADIO",
    0x3C: "RADIO",
    0x3D: "BOTTLE",
    # 0x3E
    0x3F: "YELLOW_BUTTON",
    0x40: "RED_BUTTON",
    0x41: "BLUE_BUTTON",
    0x42: "ORANGE_BUTTON",
    0x43: "BROWN_LIQUID",
    0x44: "BAR",
    0x45: "SINK",
    0x46: "WATER",
    0x47: "COUNTER",
    0x48: "DRESSER",
    0x49: "TABLE",
    0x4A: "HOOD",
    #0x4B
    0x4C: "BLASTED_SAFE",
    0x4D: "DOOR",
    0x4E: "BOULDER",
    0x4F: "RADIO",
    0x50: "DRESSER",
    0x51: "CHAIR",
    0x52: "CHAIR",
    0x53: "BED",
    0x54: "BED",
    0x55: "MOUND_SAND",
    0x56: "SIGN",
    0x57: "MESSAGE",
    0x58: "NEON_SIGN",
    0x59: "AQUARIUM",
    0x5A: "ENTRANCE_CLEAR",
    0x5B: "LIMIT_SIGN",
    0x5C: "PAIR_HANDS",
    0x5D: "BARRED_WINDOW_OUTSIDE",
    0x5E: "BARRED_WINDOW_INSIDE",
    0x5F: "SHELTER",
    0x60: "SHELTER",
    0x61: "GROUND",
    0x62: "SHAGGY_CREATURE",
    0x63: "GREY_CUBE",
    0x64: "WHITE_CUBE",
    0x65: "TABLE",
    0x66: "RECESS",
    0x67: "HOLE",
    0x68: "HOLE_BOULDERS",
    0x69: "PICTURE",
    0x6A: "GLASS_CYLINDER",
    0x6B: "WHITE_BUTTON_LIGHTS",
    0x6C: "MAROON_BUTTON",
    0x6D: "LIGHTS",
    0x6E: "CONSOLE",
    0x6F: "CHAIR",
    0x70: "WHITE_BUTTON_SCREEN",
    0x71: "GREEN_BUTTON_WEAPON",
    0x72: "VIEWING_SCREEN",
    0x73: "DISPLAY_EARTH",
    0x74: "DISPLAY_MOON",
    0x75: "DISPLAY_MOTHER_SHIP",
    0x76: "CHAIR",
    0x77: "HANDGRIP",
    0x78: "CHAIR",
    0x79: "LARGE_CUBE",
    0x7A: "HOLE_WISER",
    0x7B: "TABLE",
    0x7C: "TRANSPARENT_VIAL",
    0x7D: "TSOM_SOLUTION",
    0x7E: "PEDESTAL",
    0x7F: "TWO_INCH_HOLE",
    0x80: "WISDOM",
    0x81: "GREEN_CUBE",
    0x82: "ROD_WITH_SPHERE",
    # 0x83
    # 0x84
    0x85: "CYLINDER_BOMB",
    0x86: "CYLINDER_POISON",
    0x87: "CYLINDER_ANTS",
    0x88: "CYLINDERS_UNABLE",
    0x89: "ALIEN_ANTS",
    0x8A: "DEAD_ALIEN",
    0x8B: "SQUIRMING_ALIEN",
    0x8C: "PROSPECTOR",
    # 0x8D
    0x8E: "MACHINE",
    0x8F: "WHITE_BUTTON_ENGINES",
    0x90: "CHAIR",
    0x91: "POISON",
    0x92: "SCORE", 
    0x93: "DOOR_ESNEL",   
    0x94: "GOOLUB",
    0x95: "DOOR_ESNEL",
    0x96: "DOOR_ESNEL",
    0x97: "SMALL_UKORK_KEY",
    0x98: "BLURNUM_RADIO",
    0x99: "SHIP",
    0x9A: "WALL",
    # 0x9B
    0x9C: "SHIP",
    0x9D: 'THIRST_TRACKER',
}

def decode_section_09(cursor, end_of_sec):
    origin, line = cursor.start_new_line()
    hp_max = cursor.get_byte(line)
    hp_current = cursor.get_byte(line)
    cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; Hit Points: {hp_current}/{hp_max}',2)

def decode_section_script(cursor, end_of_sec, disk_number):
    cursor.decode_command_list(end_of_sec, disk_number, 2)

def decode_section_02(cursor, end_of_sec):
    dlen = end_of_sec - cursor.pos
    text = unpack.unpack(cursor.pos, cursor.data, dlen)
    print(';           '+text)

    origin, line = cursor.start_new_line()
    while cursor.pos < end_of_sec:
        cursor.get_byte(line)
    cursor.print_data_run(origin, line,2)  

def decode_generic_section(cursor, end_of_sec):    
    origin, line = cursor.start_new_line()
    while cursor.pos < end_of_sec:
        cursor.get_byte(line)
    cursor.print_data_run(origin, line,2)        
    

def decode_object(cursor):

    # Object header (word, length)

    origin, line = cursor.start_new_line()
    word_num  = cursor.get_byte(line)
    mlength = cursor.decode_length(line)
    end_pos = mlength+cursor.pos
    if word_num == 0x00:
        word_text = '-none-'
    else:
        word_text = '"' + language.WORDS[1].get(word_num, [f'??{word_num:02X}??'])[0] + '"'
    cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; Word Number: 0x{word_num:02X} {word_text}, Length: 0x{mlength:04X}',0)
    
    # Object data (location, points, data bits)

    origin, line = cursor.start_new_line()
    location = cursor.get_byte(line)
    points = cursor.get_byte(line)
    dbits = cursor.get_byte(line)
    cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; Location: 0x{location:02X}, Points: {points}, Data Bits: 0b{dbits:08b}',0)

    # Multiple sections

    while cursor.pos < end_pos:
        origin, line = cursor.start_new_line()
        section_num = cursor.get_byte(line)
        mlength = cursor.decode_length(line)
        end_of_sec = cursor.pos+mlength

        if section_num not in SECTION_DESC:
            raise Exception(f'Unknown section type: 0x{section_num:02X}')    

        cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; Section {section_num}: {SECTION_DESC[section_num]}, Length: 0x{mlength:04X}',1)

        if section_num == 0x02:
            decode_section_02(cursor, end_of_sec)
        elif section_num in [0x03, 0x06, 0x07, 0x08, 0x0A]:
            # TODO Some weirdness going on with the objects. Some reference room numbers that
            # could be in multiple disk sections.
            decode_section_script(cursor, end_of_sec, 1)
        elif section_num == 0x09:
            decode_section_09(cursor, end_of_sec)
        else:
            decode_generic_section(cursor, end_of_sec)

    if cursor.pos > end_pos:
        raise Exception(f'Overshot end of object, stopped at {cursor.pos:04X}, expected end at {end_pos:04X}')

if __name__ == '__main__':
    with open('d:/git/computerarcheology/content/trs80/xenos/roms/xenos.bin', 'rb') as f:
        RAW = f.read()

    cursor = script_cursor.ScriptCursor(RAW, 0x5D00)
    cursor.set_pos(0x887A)

    origin, line = cursor.start_new_line()

    lid = cursor.get_byte(line)
    mlength = cursor.decode_length(line)
    end_of_objects = mlength + cursor.pos

    # List header

    print(f'{origin:04X}: {cursor.build_data_line(line)} ; ID: 0x{lid:02X}, Length: 0x{mlength:04X}')

    objnum = 0
    while cursor.pos < end_of_objects:
        objnum += 1    
        print(f'; Object {objnum:02X}')
        decode_object(cursor)
        print()

    if cursor.pos > end_of_objects:
        raise Exception(f'Overshot {end_of_objects:04X}, stopped at {cursor.pos:04X}')
