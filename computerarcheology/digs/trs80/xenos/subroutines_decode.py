import script_cursor
import language
import unpack

with open('content/trs80/xenos/roms/xenos.bin', 'rb') as f:
    RAW = f.read()

def decode_routine(cursor):
    # Routine header (id, length)

    origin, line = cursor.start_new_line()
    routine_num  = cursor.get_byte(line)
    mlength = cursor.decode_length(line)
    end_pos = mlength+cursor.pos
    print(f'; Routine ??{routine_num:02X}??')
    print(';')
    cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; Routine Number: 0x{routine_num:02X}, Length: 0x{mlength:04X}',0)

    cursor.decode_command_list(end_pos, 2)

    if cursor.pos != end_pos:
        raise Exception(f'Mismatch, stopped at {cursor.pos:04X}, expected end at {end_pos:04X}')

cursor = script_cursor.ScriptCursor(RAW, 0x5D00)
cursor.set_pos(0xB3AF)

origin, line = cursor.start_new_line()

lid = cursor.get_byte(line)
mlength = cursor.decode_length(line)
end_of_routines = mlength + cursor.pos

# List header

print(f'{origin:04X}: {cursor.build_data_line(line)} ; ID: 0x{lid:02X}, Length: 0x{mlength:04X}')

while cursor.pos < end_of_routines:   
    decode_routine(cursor)
    print() 

if cursor.pos > end_of_routines:
    raise Exception(f'Overshot {end_of_routines:04X}, stopped at {cursor.pos:04X}')


