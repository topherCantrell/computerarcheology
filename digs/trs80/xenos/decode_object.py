import script_cursor
import language
import unpack
import names_of_things


def decode_section_09(cursor, end_of_sec):
    origin, line = cursor.start_new_line()
    hp_max = cursor.get_byte(line)
    hp_current = cursor.get_byte(line)
    cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; max_hit_points={hp_max} current_hit_points={hp_current}',2)

def decode_section_script(cursor, end_of_sec, disk_number):
    cursor.decode_command_list(end_of_sec, disk_number, 2)

def decode_section_01(cursor, end_of_sec):
    dlen = end_of_sec - cursor.pos
    for _ in range(dlen):
        origin, line = cursor.start_new_line()
        value = cursor.get_byte(line)
        text = language.get_adjective(value)
        cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; {text}',2)

def decode_section_0C(cursor, end_of_sec):
    origin, line = cursor.start_new_line()
    weight = cursor.get_byte(line)
    cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; weight={weight}',2)

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

def decode_object(cursor, obj_text, map_data_file):

    # Object header (word, length)

    origin, line = cursor.start_new_line()
    word_num  = cursor.get_byte(line)    
    mlength = cursor.decode_length(line)
    end_pos = mlength+cursor.pos
    if word_num == 0x00:
        word_text = '-none-'
    elif word_num == 0x01:
        word_text = '-player-'
    else:
        word_text = language.get_noun(word_num)
    end_of = cursor.origin + cursor.pos + mlength
    cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; Word_num=0x{word_num:02X} {word_text}, length=0x{mlength:04X} (to 0x{end_of:04X})',0)
    
    # Object data (location, points, data bits)

    origin, line = cursor.start_new_line()
    location = cursor.get_byte(line)    
    data = cursor.get_byte(line)
    dbits = cursor.get_byte(line)    
    attributes_text = names_of_things.get_attribute_name(dbits)
    ext_text = names_of_things.get_ext_attribute_name(data&0xF0)
    location_text = names_of_things.get_destination(data&15, location)
    cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; Location=0x{location:02X}, disk_section={data&15}, ext_attr={ext_text}, attributes={attributes_text}',0)

    map_data_file.write(f'{obj_text.ljust(40)}{location_text.ljust(32)}{ext_text.ljust(32)}{attributes_text.ljust(20)}\n')

    # Multiple sections

    while cursor.pos < end_pos:
        origin, line = cursor.start_new_line()
        section_num = cursor.get_byte(line)
        section_text = names_of_things.get_section_name(section_num)
        mlength = cursor.decode_length(line)
        end_of_sec = cursor.pos+mlength        

        end_of = cursor.origin + cursor.pos + mlength
        print(';')
        cursor.print_with_level(f'{origin:04X}: {cursor.build_data_line(line)} ; Section={section_num:02X}:{section_text}, length=0x{mlength:04X} (to 0x{end_of:04X})',1)

        if section_num == 0x01:
            decode_section_01(cursor, end_of_sec)
        elif section_num == 0x02:
            decode_section_02(cursor, end_of_sec)        
        elif section_num == 0x09:
            decode_section_09(cursor, end_of_sec)
        elif section_num == 0x0C:
            decode_section_0C(cursor, end_of_sec)
        elif section_num in [0x03, 0x04, 0x06, 0x07, 0x08, 0x0A, 0x0B]:            
            decode_section_script(cursor, end_of_sec, 1)
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

    end_of = cursor.origin + cursor.pos + mlength

    # List header

    print(f'{origin:04X}: {cursor.build_data_line(line)} ; List_ID=0x{lid:02X}, length=0x{mlength:04X} (to 0x{end_of:04X})')
    print()

    map_data_file = open('map_obj_data.txt', 'w')

    objnum = 0
    while cursor.pos < end_of_objects:
        objnum += 1    
        obj_text = names_of_things.get_object_name(objnum)
        print(f'; -------------- Object {obj_text} --------------')
        decode_object(cursor, obj_text, map_data_file)
        print()

    if cursor.pos > end_of_objects:
        raise Exception(f'Overshot {end_of_objects:04X}, stopped at {cursor.pos:04X}')
