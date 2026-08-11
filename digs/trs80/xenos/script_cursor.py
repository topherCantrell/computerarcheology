import unpack
import language
import decode_object
import decode_subroutines
import names_of_things

class ScriptCursor:            

    def __init__(self, data, origin):
        self.data = data
        self.origin = origin
        self.pos = 0

    def set_pos(self, pos):
        self.pos = pos - self.origin

    def start_new_line(self):
        return self.origin+self.pos, []   
    
    def text_word_wrap(self, text):
        ret = []
        while len(text) > 60:
            i = text.rfind(' ', 0, 60)
            if i<0:
                i = 60
            ret.append(text[:i])
            text = text[i:].strip()
        if text:
            ret.append(text)
                
        return ret

    def build_data_line(self, data):
        g = ''
        for b in data:
            g += f"{b:02X} "
        return g

    def decode_length(self, line):
        if self.data[self.pos] < 128:
            ret = self.data[self.pos]
            line.append(self.data[self.pos])
            self.pos += 1
            return ret
        else:
            ret = (self.data[self.pos]-128)*256 + self.data[self.pos+1]
            line.extend(self.data[self.pos:self.pos+2])
            self.pos += 2
            return ret
        
    def get_byte(self, line):
        ret = self.data[self.pos]
        line.append(ret)
        self.pos += 1
        return ret
    
    def print_data_run_ascii(self, origin, line, prt_level):
        p = 0        
        while p < len(line):
            q = min(p+16, len(line))
            g = ''
            for b in line[p:q]:
                if b < 32 or b > 126 or b == 96:
                    g += '.'
                else:
                    g += chr(b)
            self.print_with_level(f'{origin:04X}: {self.build_data_line(line[p:q])} ; {g}', prt_level)
            origin = origin + (q-p)
            p = q
    
    def print_data_run(self, origin, line, prt_level):
        p = 0
        while p < len(line):
            q = min(p+16, len(line))
            self.print_with_level(f'{origin:04X}: {self.build_data_line(line[p:q])}', prt_level)
            origin = origin + (q-p)
            p = q                    

    def decode_print_command(self, cmd_name, origin, line, _, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        end_of = self.origin+self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name} length=0x{length:04X} (to 0x{end_of:04X})', prt_level)        
        g = unpack.unpack(self.pos, self.data, length)
        
        origin += len(line)
        line = []        
        while self.pos < end_of_command:
            self.get_byte(line)
        self.print_data_run(origin, line, prt_level+1)  
        gg = self.text_word_wrap(g)
        print(";")
        for gg_line in gg:
             print(";        "+" "*(prt_level*3)+gg_line)
        print(";")

    SWITCH_WORDS = {
        0x03: ['COM_03_is_located(room_num, obj_num)','DEST,OBJ'],
        0x05: ['COM_05_is_less_equal_last_random(value)','VALUE'],
        0x08: ['COM_08_is_first_noun(word_num)','WORD'],
        0x0A: ['COM_0A_is_input_phrase(phrase_num)','PHRASE'],
        0x22: ['COM_22_is_less_equal_health(points)','HEALTH'],
    }

    def decode_switch(self, cmd_name, origin, line, disk_number, prt_level):
        start_of_command = self.pos - 1 + self.origin
        length = self.decode_length(line)
        end_of_command = self.pos+length
        fn_to_call = self.get_byte(line)        
        if fn_to_call != 0x0A and fn_to_call != 0x03 and fn_to_call != 0x05 and fn_to_call != 0x22 and fn_to_call != 0x08: 
            raise Exception(f"Unknown function to call in SWITCH command: 0x{fn_to_call:02X}")
        end_of = self.origin+self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name} length=0x{length:04X} (to 0x{end_of:04X}), function={self.SWITCH_WORDS[fn_to_call][0]}', prt_level)
        
        while self.pos < end_of_command:
            line = []
            origin = self.origin+self.pos
            value = self.get_byte(line)
            if fn_to_call == 0x03:
                obj_text = names_of_things.get_object_name(value)
                value2 = self.get_byte(line)
                obj_text2 = names_of_things.get_object_name(value2)
                length_of_phrase = self.decode_length(line)
                self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ;case COM_03_is_located(room_num, obj_num) room_num={obj_text}, obj_num={obj_text2}, length=0x{length_of_phrase:04X}', prt_level+1)
            elif fn_to_call == 0x05:
                length_of_phrase = self.decode_length(line)
                self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; case COM_05_is_less_equal_last_random(value={value}), length=0x{length_of_phrase:04X}', prt_level+1)
            elif fn_to_call == 0x08:   
                obj_text = names_of_things.get_object_name(value)                             
                length_of_phrase = self.decode_length(line)
                self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; case COM_08_is_first_noun(object_num={obj_text}), length=0x{length_of_phrase:04X}', prt_level+1)
            elif fn_to_call == 0x0A:
                phrase_num = value
                phrase_text = language.get_phrase(phrase_num)
                length_of_phrase = self.decode_length(line)
                self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; case COM_0A_is_input_phrase("{phrase_text}"), length=0x{length_of_phrase:04X}', prt_level+1)
            elif fn_to_call == 0x22:
                length_of_phrase = self.decode_length(line)
                self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; case COM_22_is_less_equal_health(points={value}), length=0x{length_of_phrase:04X}', prt_level+1)
            
            else:
                self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {self.SWITCH_WORDS[fn_to_call][1]}: 0x{value:02X}', prt_level+1)
                raise Exception(f"Unknown function to call in SWITCH command: 0x{fn_to_call:02X}")
            
            line = []
            origin = self.origin+self.pos
            # self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; ELSE goto=0x{self.origin+self.pos+length_of_phrase:04X}', prt_level+1)
            self.decode_command(disk_number, prt_level+2)
            self.print_with_level(f'end case', prt_level+1)

        self.print_with_level(f'end decode_switch at 0x{start_of_command:04X}', prt_level)        
    
    def decode_while_pass(self, cmd_name, origin, line, disk_number, prt_level):
        start_of_command = self.pos - 1 + self.origin
        length = self.decode_length(line)
        end_of_command = self.pos+length
        end_of = self.origin+self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name} length=0x{length:04X} (to 0x{end_of:04X})', prt_level)
        while self.pos < end_of_command:
            self.decode_command(disk_number, prt_level+1)

        self.print_with_level(f'end group_AND at 0x{start_of_command:04X}', prt_level)
    
    def decode_while_fail(self, cmd_name, origin, line, disk_number, prt_level):
        start_of_command = self.pos - 1 + self.origin
        length = self.decode_length(line)
        end_of_command = self.pos+length
        end_of = self.origin+self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name} length=0x{length:04X} (to 0x{end_of:04X})', prt_level)
        while self.pos < end_of_command:
            self.decode_command(disk_number, prt_level+1)

        self.print_with_level(f'end group_OR at 0x{start_of_command:04X}', prt_level)

    def decode_set_current_room(self, cmd_name, origin, line, disk_number, prt_level):
        room_num = self.get_byte(line)
        if self.data[self.pos] == 0x17 and self.data[self.pos+3] == 0x2F:
            # Followed by a MOVE TO and a LOAD SECTION
            disk_number = self.data[self.pos+4]      
        elif self.data[self.pos] == 0x2F:
            # Followed by a LOAD SECTION
            disk_number = self.data[self.pos+1]   
        room_text = names_of_things.get_room_name(disk_number, room_num) 
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(room={room_text})', prt_level)

    def decode_load_section_from_disk(self, cmd_name, origin, line, _, prt_level):
        data = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(section={data})', prt_level)

    def decode_move_to(self, cmd_name, origin, line, disk_number,prt_level):
        obj_num = self.get_byte(line)
        dest_room = self.get_byte(line)
        dest_text = names_of_things.get_destination(disk_number, dest_room)
        obj_text = names_of_things.get_object_name(obj_num)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(obj={obj_text}, destination={dest_text})', prt_level)

    def decode_is_less_equal_last_random(self, cmd_name, origin, line, _, prt_level):
        value = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(value={value})', prt_level)

    def decode_move_and_look(self, cmd_name, origin, line, disk_number, prt_level):
        dest_room = self.get_byte(line)
        dest_name = names_of_things.get_destination(disk_number, dest_room)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(room={dest_name})', prt_level)

    def decode_execute_and_reverse_status(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name} next command', prt_level)

    def decode_set_var_object(self, cmd_name, origin, line, _, prt_level):
        obj_num = self.get_byte(line)
        obj_text = names_of_things.get_object_name(obj_num)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(obj={obj_text})', prt_level)

    def decode_compare_to_second_noun(self, cmd_name, origin, line, _, prt_level):
        obj_num = self.get_byte(line)        
        obj_text = names_of_things.get_object_name(obj_num)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(obj={obj_text})', prt_level)

    def decode_is_in_pack_or_current_room(self, cmd_name, origin, line, _, prt_level):
        obj_num = self.get_byte(line)
        obj_text = names_of_things.get_object_name(obj_num)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(obj={obj_text})', prt_level)

    def decode_is_located(self, cmd_name, origin, line, disk_number, prt_level):
        room_num = self.get_byte(line)
        obj_num = self.get_byte(line)
        dest = names_of_things.get_destination(disk_number, room_num)
        obj_text = names_of_things.get_object_name(obj_num)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(owner={dest}, obj={obj_text})', prt_level)

    def decode_is_owned(self, cmd_name, origin, line, _, prt_level):
        obj_num = self.get_byte(line)
        obj_text = names_of_things.get_object_name(obj_num)
        owner = self.get_byte(line)
        owner_text = names_of_things.get_destination(0, owner)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(owner={owner_text}, obj={obj_text})', prt_level)

    def decode_print_room_description(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_is_first_noun(self, cmd_name, origin, line, _, prt_level):
        obj_num = self.get_byte(line)
        obj_text = names_of_things.get_object_name(obj_num)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(obj={obj_text})', prt_level)

    def decode_attack_VAR(self, cmd_name, origin, line, _, prt_level):
        points = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(points={points})', prt_level)

    def decode_fail(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_is_input_phrase(self, cmd_name, origin, line, _, prt_level):
        phrase_num = self.get_byte(line)
        phrase_text = language.get_phrase(phrase_num)        
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(phrase={phrase_text})', prt_level)

    def decode_set_active(self, cmd_name, origin, line, _, prt_level):
        obj_num = self.get_byte(line)
        obj_text = names_of_things.get_object_name(obj_num)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(obj={obj_text})', prt_level)
    
    def decode_drop_var(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_exit_program(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_process_phrase_by_room_first_second(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_print2(self, cmd_name, origin, line, _, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        end_of = self.origin+self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name} length=0x{length:04X} (to 0x{end_of:04X})', prt_level)
        g = unpack.unpack(self.pos, self.data, length)        
        origin += len(line)
        line = []        
        while self.pos < end_of_command:
            self.get_byte(line)
        self.print_data_run(origin, line, prt_level+1)  
        gg = self.text_word_wrap(g)
        print(";")
        for gg_line in gg:
            print(";        "+" "*(prt_level*3)+gg_line)
        print(";") 

    def decode_set_var_to_first_noun(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)
        
    def decode_set_var_to_second_noun(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_print_linefeed(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_bump_score(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_assert_player_is_in_an_object(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_pick_up_var_object(self, cmd_name, origin, line, _, prt_level):        
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_check_weight_70_or_less(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)
    
    def decode_swap(self, cmd_name, origin, line, _, prt_level):
        a = self.get_byte(line)
        a_text = names_of_things.get_object_name(a)
        b = self.get_byte(line)
        b_text = names_of_things.get_object_name(b)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(obj1={a_text}, obj2={b_text})', prt_level)

    def decode_heal_var(self, cmd_name, origin, line, _, prt_level):
        points = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(points={points})', prt_level)

    def decode_print_open_var(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_print_second_noun(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_execute_phrase(self, cmd_name, origin, line, _, prt_level):
        phrase_num = self.get_byte(line)
        phrase_text = language.get_phrase(phrase_num)
        first_noun = self.get_byte(line)
        a_text = names_of_things.get_object_name(first_noun)
        second_noun = self.get_byte(line)
        b_text = names_of_things.get_object_name(second_noun)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(phrase={phrase_text}, obj1={a_text}, obj2={b_text})', prt_level)
    
    def decode_is_active_this(self, cmd_name, origin, line, _, prt_level):
        obj_num = self.get_byte(line)
        obj_text = names_of_things.get_object_name(obj_num)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(obj={obj_text})', prt_level)

    def decode_check_var(self, cmd_name, origin, line, _, prt_level):
        value = self.get_byte(line)
        attributes_text = names_of_things.get_attribute_name(value)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(value={attributes_text})', prt_level)

    def decode_is_var_owned_by_active(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_clear_screen(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_print_first_noun(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_print_var(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_wait_for_key123(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_print_score(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_print_inventory(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_compare_to_var_object(self, cmd_name, origin, line, _, prt_level):
        obj_num = self.get_byte(line)        
        obj_text = names_of_things.get_object_name(obj_num)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(obj_num=0x{obj_num:02X}, obj_text="{obj_text}")', prt_level)

    def decode_toggle_lock_var(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_load_game(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)
    def decode_save_game(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)
    def decode_move_active_object(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)
    def decode_save_system_objects_to_disk(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)
    def decode_load_system_objects_from_disk(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_move_second_noun_to_var_object(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)
    def decode_move_first_noun_to_var_object(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)
    def decode_print_objects_on_var_object(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}()', prt_level)

    def decode_check_ext_attributes(self, cmd_name, origin, line, _, prt_level):
        value = self.get_byte(line)
        attributes_text = names_of_things.get_ext_attribute_name(value)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {cmd_name}(value={attributes_text})', prt_level)              
    def decode_unknown36(self, cmd_name, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN_COM_36', prt_level)        

    COMMANDS = {
        0x00: decode_move_and_look,
        0x01: decode_is_in_pack_or_current_room,
        0x02: decode_is_owned,
        0x03: decode_is_located,
        0x04: decode_print_command,
        0x05: decode_is_less_equal_last_random,    
        0x06: decode_print_inventory,
        0x07: decode_print_room_description, 
        0x08: decode_is_first_noun,
        0x09: decode_compare_to_second_noun,   
        0x0A: decode_is_input_phrase,
        0x0B: decode_switch,
        0x0C: decode_fail,
        0x0D: decode_while_pass,
        0x0E: decode_while_fail,
        0x0F: decode_pick_up_var_object,
        0x10: decode_drop_var,
        0x11: decode_print_first_noun,
        0x12: decode_print_second_noun,
        0x13: decode_process_phrase_by_room_first_second,
        0x14: decode_execute_and_reverse_status,
        0x15: decode_check_var, 
        0x16: decode_print_var,
        0x17: decode_move_to,
        0x18: decode_is_var_owned_by_active,
        0x19: decode_move_active_object,
        0x1A: decode_set_var_to_first_noun,
        0x1B: decode_set_var_to_second_noun,
        0x1C: decode_set_var_object,
        0x1D: decode_attack_VAR,
        0x1E: decode_swap,
        0x1F: decode_print2,
        0x20: decode_is_active_this,
        0x21: decode_execute_phrase,
        # 0x22: decode_is_less_equal_health, # Only called from SWITCH
        0x23: decode_heal_var,
        0x24: decode_exit_program,
        0x25: decode_print_linefeed,
        0x26: decode_print_score,
        0x27: decode_load_game,
        0x28: decode_save_game,
        0x29: decode_print_open_var,
        0x2A: decode_toggle_lock_var,
        # 0x2B: decode_random, # Never called from scripts
        0x2C: decode_set_active,
        0x2D: decode_compare_to_var_object,
        0x2E: decode_check_ext_attributes,
        0x2F: decode_load_section_from_disk,
        0x30: decode_set_current_room,
        0x31: decode_move_second_noun_to_var_object,
        0x32: decode_move_first_noun_to_var_object,
        0x33: decode_print_objects_on_var_object,
        0x34: decode_save_system_objects_to_disk,
        0x35: decode_load_system_objects_from_disk,
        0x36: decode_unknown36,
        0x37: decode_assert_player_is_in_an_object,
        0x38: decode_bump_score,
        0x39: decode_check_weight_70_or_less,
        0x3A: decode_clear_screen,
        0x3B: decode_wait_for_key123,
    } 

    def print_with_level(self, text, prt_level):
        a  = text.find(':')
        if a<0:
            print(';'.ljust(40) + ' ; ' + ' '*(prt_level*2) +text)
            return
        b = text.find(';')
        if b>=0:
            data_part = text[a+2:b].strip()
            comment_part = text[b+1:].strip()
        else:
            data_part = text[a+2:].strip()
            comment_part = ''
        g = text[:6]+' '*(prt_level*3)+data_part
        g = g.ljust(40)
        if comment_part:
            comment_part = ' '*(prt_level*2) + comment_part
            print(g+' ; '+comment_part)   
        else:
            print(g)     

    def decode_command(self, disk_number, prt_level):
        line = []
        origin = self.origin+self.pos
        command = self.get_byte(line)        
        if command >= 0x80:
            # This command is a routine call
            routine_text = names_of_things.get_routine_name(command)
            self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; {routine_text}', prt_level)
            return

        if command not in self.COMMANDS:                
            raise Exception(f'Unknown command {command:02X} at {origin:04X}')
        
        cmd_name = names_of_things.get_command_name(command)
        fn = self.COMMANDS[command]
        fn(self, cmd_name, origin, line, disk_number, prt_level)
    
    def decode_section(self, disk_number, prt_level):
        line = []
        origin = self.origin+self.pos
        section_type = self.get_byte(line)
        length = self.decode_length(line)
        end_of_section = self.pos+length
        end_of = self.origin+self.pos+length

        section_text = names_of_things.get_section_name(section_type)
        
        print(';')
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; ---- Section {section_text} length=0x{length:04X} (to 0x{end_of:04X})', prt_level)
        
        while self.pos < end_of_section:                        
            self.decode_command(disk_number,prt_level+1)
            
        if self.pos != end_of_section:
            self.print_with_level(f'WARNING: Section ended at {end_of_section:04X} but cursor is at {self.pos:04X}', prt_level)

    
    def decode_room(self, disk_number, prt_level):
        line = []
        origin = self.origin+self.pos
        room_num = self.get_byte(line)
        room_text = names_of_things.get_room_name(disk_number, room_num)
        length = self.decode_length(line)
        datab = self.get_byte(line)
        print()        
        print('; --------------------------------------------------------------------------------------------------------------------')
        print(';')
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; ----- Room 0x{room_num:02X} {room_text}, Length: 0x{length:04X}, Data: 0x{datab:02X}', prt_level)
        end_of_room = self.pos+length-1  # We already read one of these bytes       

        while self.pos < end_of_room:
            self.decode_section(disk_number, prt_level+1)
        if self.pos != end_of_room:
            self.print_with_level(f'WARNING: Room ended at {end_of_room:04X} but cursor is at {self.pos:04X}', prt_level)

    def decode_command_list(self, end_of_list, disk_number, prt_level):
        while self.pos < end_of_list:
            self.decode_command(disk_number, prt_level)
        if self.pos != end_of_list:
            self.print_with_level(f'WARNING: Command list ended at {end_of_list:04X} but cursor is at {self.pos:04X}', prt_level)

    def decode_script(self, disk_number):
        line = []
        origin = self.origin+self.pos
        list_id = self.get_byte(line)
        length = self.decode_length(line)
        end_of = self.origin+self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; List_ID=0x{list_id:02X}, length=0x{length:04X} (to 0x{end_of:04X})', 0)
        end_of_list = self.pos+length
        while self.pos < end_of_list:
            self.decode_room(disk_number, 0)
        if self.pos != end_of_list:
            self.print_with_level(f'WARNING: Script ended at {end_of_list:04X} but cursor is at {self.pos:04X}', 0)
        

