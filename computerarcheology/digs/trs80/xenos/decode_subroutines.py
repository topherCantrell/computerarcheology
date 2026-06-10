import script_cursor

DESCRIPTIONS = {
    0x80: 'PRINT_SHOTGUN_HERE',
    0x81: 'PRINT_DOOR_HERE',
    0x8B: 'PRINT_PERIOD',
    # 0x8D
    # 0x8F
    # 0x90
    0x91: 'PRINT_USE_DIRECTIONS',
    # 0x92
    0x94: 'INIT_GAME',  # Moves to HIGHWAY_WEST in section 1
    0x95: 'PRINT_TRAIL_MEANDERS',
    0x96: 'PRINT_VAST_CANYON',
    0x97: 'PRINT_CERTAIN_DEATH',
    0x98: 'PRINT_LAKE',
    0x99: 'DIE_CANYON_PLUNGE',
    0x9A: 'PRINT_CANYON_PREVENTS',
    0x9B: 'PRINT_EMPTY_HIGHWAY',
    # 0x9C
    # 0x9D
    # 0x9E
    # 0x9F
    # 0xA0
    # 0xA1
    # 0xA2
    0xA3: 'PRINT_WELCOME_MESSAGE',  # Moves to HIGHWAY_WEST in section 1
    # 0xA5
    # 0xA6
    # 0xA8
    # 0xA9
    # 0xAA
    0xAB: 'PRINT_STILL_IN_DESERT',
    # 0xAC
    # 0xAD
    # 0xAE
    # 0xAF    
    # 0xB0
    # 0xB1
    # 0xB2
    0xB3: 'PRINT_DISK_ERROR',
    0xB4: 'PRINT_AND',
    0xB5: 'PRINT_BY_YOUR_COMMAND',
    0xB6: 'PRINT_TWO_SAME_SPACE',
    # 0xB7
    0xB8: 'PRINT_GARBAGE_GAMES',
    0xB9: 'PRINT_JUKEBOX',
    # 0xBA
    # 0xBB
    # 0xBC
    0xBD: 'PRINT_SHAGGY_CREATURE',
    0xBE: 'PRINT_FORCE_FIELD',
    # 0xBF
    # 0xC0
    # 0xC1
    # 0xC2
    # 0xC3
    # 0xC4
    # 0xC5
    0xC6: 'PROMPT_FOR_DRIVE_NUMBER',
    # 0xC7
    # 0xC8
    0xC9: 'PRINT_COMPLETED_PERCENT', 
    0xCA: 'DIE_ENERGY_BEAM',
}

def decode_routine(cursor):
    # Routine header (id, length)

    origin, line = cursor.start_new_line()
    routine_num  = cursor.get_byte(line)
    mlength = cursor.decode_length(line)
    end_pos = mlength+cursor.pos
    if routine_num in DESCRIPTIONS:
        print(f'; Routine {routine_num:02X}:{DESCRIPTIONS[routine_num]}')
    else:
        print(f'; Routine ??{routine_num:02X}??')
    print(';')
    cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; Routine Number: 0x{routine_num:02X}, Length: 0x{mlength:04X}',0)

    # There are two routines that reference room descriptions. They are both used to initialize the game and thus both
    # are for disk_number=1.
    cursor.decode_command_list(end_pos, 1, 2)

    if cursor.pos != end_pos:
        raise Exception(f'Mismatch, stopped at {cursor.pos:04X}, expected end at {end_pos:04X}')

if __name__ == '__main__':

    with open('d:/git/computerarcheology/content/trs80/xenos/roms/xenos.bin', 'rb') as f:
        RAW = f.read()

    cursor = script_cursor.ScriptCursor(RAW, 0x5D00)
    cursor.set_pos(0xB3AF)

    origin, line = cursor.start_new_line()

    lid = cursor.get_byte(line)
    mlength = cursor.decode_length(line)
    end_of_routines = mlength + cursor.pos

    # List header

    print(f'{origin:04X}: {cursor.build_data_line(line)} ; ID: 0x{lid:02X}, Length: 0x{mlength:04X}')
    print(';')

    while cursor.pos < end_of_routines:   
        decode_routine(cursor)
        print() 

    if cursor.pos > end_of_routines:
        raise Exception(f'Overshot {end_of_routines:04X}, stopped at {cursor.pos:04X}')


