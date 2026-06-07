import script_cursor
import language
import unpack

with open('content/trs80/xenos/roms/xenos.bin', 'rb') as f:
    RAW = f.read()

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

def decode_section_09(cursor, end_of_sec):
    origin, line = cursor.start_new_line()
    hp_max = cursor.get_byte(line)
    hp_current = cursor.get_byte(line)
    cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; Hit Points: {hp_current}/{hp_max}',2)

def decode_section_script(cursor, end_of_sec):
    cursor.decode_command_list(end_of_sec, 2)

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
    word_text = language.WORDS[1].get(word_num, [f'??{word_num:02X}??'])[0]    
    cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; Word Number: 0x{word_num:02X} "{word_text}", Length: 0x{mlength:04X}',0)
    
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
            decode_section_script(cursor, end_of_sec)
        elif section_num == 0x09:
            decode_section_09(cursor, end_of_sec)
        else:
            decode_generic_section(cursor, end_of_sec)

    if cursor.pos > end_pos:
        raise Exception(f'Overshot end of object, stopped at {cursor.pos:04X}, expected end at {end_pos:04X}')

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


