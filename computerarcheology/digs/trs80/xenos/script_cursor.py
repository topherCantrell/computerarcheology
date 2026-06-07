import unpack

class ScriptCursor:

    SECTION_TYPES = {
        3: 'DESCRIPTION',
        4: 'COMMANDS',
    }    

    def __init__(self, data, origin):
        self.data = data
        self.origin = origin
        self.pos = 0

    def set_pos(self, pos):
        self.pos = pos - self.origin

    def start_new_line(self):
        return self.origin+self.pos, []

    def build_data_line(self, data):
        g = ''
        for b in data:
            g += f"{b:02X} "
        return g

    def decode_length(self, data_fill):
        if self.data[self.pos] < 128:
            ret = self.data[self.pos]
            data_fill.append(self.data[self.pos])
            self.pos += 1
            return ret
        else:
            ret = (self.data[self.pos]-128)*256 + self.data[self.pos+1]
            data_fill.extend(self.data[self.pos:self.pos+2])
            self.pos += 2
            return ret
        
    def get_byte(self, data_fill):
        ret = self.data[self.pos]
        data_fill.append(ret)
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
    
    def decode_word_list(self):
        while True:
            line = []
            origin = self.origin+self.pos
            a = self.get_byte(line)
            if a == 0:
                print(f'{origin:04X}: {self.build_data_line(line)} ; End of list')
                return
            txt = ''
            for _ in range(a):
                b = self.get_byte(line)
                txt += chr(b)
            word_num = self.get_byte(line)
            print(f'{origin:04X}: {self.build_data_line(line)} ; {txt}')

    def decode_print_command(self, origin, line, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT, Length: 0x{length:04X}', prt_level)        
        g = unpack.unpack(self.pos, self.data, length)
        print(";")
        print("; "+g)  # TODO break this up like the game does
        print(";")
        origin += len(line)
        line = []        
        while self.pos < end_of_command:
            self.get_byte(line)
        self.print_data_run(origin, line, prt_level+1)    

    def decode_switch(self, origin, line, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        fn_to_call = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SWITCH, Length: 0x{length:04X}, Function to call: 0x{fn_to_call:02X}', prt_level)
        if fn_to_call != 0x0A and fn_to_call != 0x03 and fn_to_call != 0x05 and fn_to_call != 0x22: # TODO different descript below
            raise Exception(f"Unknown function to call in SWITCH command: 0x{fn_to_call:02X}")
        
        while self.pos < end_of_command:
            line = []
            origin = self.origin+self.pos
            phrase_num = self.get_byte(line)
            self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; Phrase number: 0x{phrase_num:02X}', prt_level+1)
            line = []
            origin = self.origin+self.pos
            length_of_phrase = self.decode_length(line)
            self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; ELSE go to: 0x{self.origin+self.pos+length_of_phrase:04X}', prt_level+1)
            self.decode_command(prt_level+2)        
    
    def decode_while_pass(self, origin, line, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; WHILE PASS, Length: 0x{length:04X}', prt_level)
        while self.pos < end_of_command:
            self.decode_command(prt_level+1)
    
    def decode_while_fail(self, origin, line, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; WHILE FAIL, Length: 0x{length:04X}', prt_level)
        while self.pos < end_of_command:
            self.decode_command(prt_level+1)

    def decode_unknown30(self, origin, line, prt_level):
        data = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN30, Data: 0x{data:02X}', prt_level)

    def decode_unknown2F(self, origin, line, prt_level):
        data = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN2F Data: 0x{data:02X}', prt_level)

    def decode_move_to(self, origin, line, prt_level):
        obj_num = self.get_byte(line)
        dest_room = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; MOVE TO, Object number: 0x{obj_num:02X}, Destination room: 0x{dest_room:02X}', prt_level)

    def decode_is_less_equal_last_random(self, origin, line, prt_level):
        value = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS LESS OR EQUAL TO LAST RANDOM, Value: 0x{value:02X}', prt_level)

    def decode_move_and_look(self, origin, line, prt_level):
        dest_room = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; MOVE AND LOOK, Destination room: 0x{dest_room:02X}', prt_level)

    def decode_execute_and_reverse_status(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; EXECUTE AND REVERSE STATUS', prt_level)

    def decode_set_var_object(self, origin, line, prt_level):
        obj_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SET VAR OBJECT, Object number: 0x{obj_num:02X}', prt_level)

    def decode_compare_to_second_noun(self, origin, line, prt_level):
        word_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; COMPARE TO SECOND NOUN, Word number: 0x{word_num:02X}', prt_level)

    def decode_is_in_pack_or_current_room(self, origin, line, prt_level):
        obj_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS IN PACK OR CURRENT ROOM, Object number: 0x{obj_num:02X}', prt_level)

    def decode_is_located(self, origin, line, prt_level):
        room_num = self.get_byte(line)
        obj_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS LOCATED, Room number: 0x{room_num:02X}, Object number: 0x{obj_num:02X}', prt_level)

    def decode_is_owned(self, origin, line, prt_level):
        obj_num = self.get_byte(line)
        a = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS OWNED BY, A=0x{a:02X}, Object number: 0x{obj_num:02X}', prt_level)

    def decode_print_room_description(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT ROOM DESCRIPTION', prt_level)

    def decode_is_first_noun(self, origin, line, prt_level):
        word_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS FIRST NOUN, Word number: 0x{word_num:02X}', prt_level)

    def decode_attack_VAR(self, origin, line, prt_level):
        points = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; ATTACK VAR, Points: 0x{points:02X}', prt_level)

    def decode_fail(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; FAIL', prt_level)

    def decode_is_input_phrase(self, origin, line, prt_level):
        phrase_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS INPUT PHRASE, Phrase number: 0x{phrase_num:02X}', prt_level)

    def decode_set_active(self, origin, line, prt_level):
        obj_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SET ACTIVE, Object number: 0x{obj_num:02X}', prt_level)
    
    def decode_drop_var(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; DROP VAR', prt_level)

    def decode_exit_program(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; EXIT PROGRAM', prt_level)

    def decode_print2(self, origin, line, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT, Length: 0x{length:04X}', prt_level)        
        g = unpack.unpack(self.pos, self.data, length)
        print(";")
        print("; "+g)  # TODO break this up like the game does
        print(";")
        origin += len(line)
        line = []        
        while self.pos < end_of_command:
            self.get_byte(line)
        self.print_data_run(origin, line, prt_level+1)  

    def decode_set_var_to_first_noun(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SET VAR TO FIRST NOUN', prt_level)
        
    def decode_set_var_to_second_noun(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SET VAR TO SECOND NOUN', prt_level)  

    def decode_print_linefeed(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT LINEFEED', prt_level)

    def decode_unknown38(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN38', prt_level)

    def decode_unknown2D(self, origin, line, prt_level):
        value = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN2D, Value: 0x{value:02X}', prt_level)

    def decode_unknown2E(self, origin, line, prt_level):
        value = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN2E, Value: 0x{value:02X}', prt_level)

    def decode_unknown2A(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN2A', prt_level)

    def decode_unknown33(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN33', prt_level)
    def decode_unknown34(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN34', prt_level)
    def decode_unknown35(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN35', prt_level)
    def decode_unknown0F(self, origin, line, prt_level):        
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN0F', prt_level)
    def decode_unknown39(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN39', prt_level)
    def decode_unknown36(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN36', prt_level)
    def decode_unknown37(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN37', prt_level)


    def decode_swap(self, origin, line, prt_level):
        a = self.get_byte(line)
        b = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SWAP, A: 0x{a:02X}, B: 0x{b:02X}', prt_level)

    def decode_heal_var(self, origin, line, prt_level):
        points = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; HEAL VAR, Points: 0x{points:02X}', prt_level)

    def decode_print_open_var(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT OPEN VAR', prt_level)

    def decode_print_second_noun(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT SECOND NOUN', prt_level)

    def decode_execute_phrase(self, origin, line, prt_level):
        phrase_num = self.get_byte(line)
        first_noun = self.get_byte(line)
        second_noun = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; EXECUTE PHRASE, Phrase number: 0x{phrase_num:02X}, First noun: 0x{first_noun:02X}, Second noun: 0x{second_noun:02X}', prt_level)
    
    def decode_is_active_this(self, origin, line, prt_level):
        obj_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS ACTIVE THIS, Object number: 0x{obj_num:02X}', prt_level)

    def decode_check_var(self, origin, line, prt_level):
        value = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; CHECK VAR, Value: 0x{value:02X}', prt_level)

    def decode_is_var_owned_by_active(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS VAR OWNED BY ACTIVE', prt_level)

    def decode_clear_screen(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; CLEAR SCREEN', prt_level)

    def decode_print_first_noun(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT FIRST NOUN', prt_level)

    def decode_print_var(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT VAR', prt_level)

    def decode_wait_for_key123(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; WAIT FOR KEY 1, 2, OR 3', prt_level)

    def decode_print_score(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT SCORE', prt_level)


    COMMANDS = {
        0x00: decode_move_and_look,
        0x01: decode_is_in_pack_or_current_room,
        0x02: decode_is_owned,
        0x03: decode_is_located,
        0x04: decode_print_command,
        0x05: decode_is_less_equal_last_random,    
        0x07: decode_print_room_description, 
        0x08: decode_is_first_noun,
        0x09: decode_compare_to_second_noun,   
        0x0A: decode_is_input_phrase,
        0x0B: decode_switch,
        0x0C: decode_fail,
        0x0D: decode_while_pass,
        0x0E: decode_while_fail,
        0x0F: decode_unknown0F,
        0x10: decode_drop_var,
        0x11: decode_print_first_noun,
        0x12: decode_print_second_noun,
        0x14: decode_execute_and_reverse_status,
        0x15: decode_check_var, 
        0x16: decode_print_var,
        0x17: decode_move_to,
        0x18: decode_is_var_owned_by_active,
        0x1A: decode_set_var_to_first_noun,
        0x1B: decode_set_var_to_second_noun,
        0x1C: decode_set_var_object,
        0x1D: decode_attack_VAR,
        0x1E: decode_swap,
        0x1F: decode_print2,
        0x20: decode_is_active_this,
        0x21: decode_execute_phrase,
        0x23: decode_heal_var,
        0x24: decode_exit_program,
        0x25: decode_print_linefeed,
        0x26: decode_print_score,
        0x29: decode_print_open_var,
        0x2A: decode_unknown2A,
        0x2C: decode_set_active,
        0x2D: decode_unknown2D,
        0x2E: decode_unknown2E,
        0x2F: decode_unknown2F,
        0x30: decode_unknown30,
        0x33: decode_unknown33,
        0x34: decode_unknown34,
        0x35: decode_unknown35,
        0x36: decode_unknown36,
        0x37: decode_unknown37,
        0x38: decode_unknown38,
        0x39: decode_unknown39,
        0x3A: decode_clear_screen,
        0x3B: decode_wait_for_key123,
    } 

    def print_with_level(self, text, prt_level):
        a  = text.find(':')
        if a<0:
            print(">>>>>",text)
            raise "STOP"
        b = text.find(';')
        if b>=0:
            data_part = text[a+2:b].strip()
            comment_part = text[b+1:].strip()
        else:
            data_part = text[a+2:].strip()
            comment_part = ''
        g = text[:6]+' '*(prt_level*3)+data_part
        g = g.ljust(35)
        if comment_part:
            comment_part = ' '*(prt_level*2) + comment_part
        print(g+' ; '+comment_part)        

    def decode_command(self, prt_level):
        line = []
        origin = self.origin+self.pos
        command = self.get_byte(line)
        if command >= 0x80:
            self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; COMMAND 0x{command:02X}', prt_level)                
            return

        if command not in self.COMMANDS:                
            raise Exception(f'Unknown command {command:02X} at {origin:04X}')
        
        fn = self.COMMANDS[command]
        fn(self, origin, line, prt_level)
    
    def decode_section(self, prt_level):
        line = []
        origin = self.origin+self.pos
        section_type = self.get_byte(line)
        length = self.decode_length(line)
        end_of_section = self.pos+length

        st = self.SECTION_TYPES.get(section_type, f'??{section_type:02X}??')
        print(';')
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; Section {st}, Length: 0x{length:04X}', prt_level)
        
        while self.pos < end_of_section:                        
            self.decode_command(prt_level+1)
            
        if self.pos != end_of_section:
            self.print_with_level(f'WARNING: Section ended at {end_of_section:04X} but cursor is at {self.pos:04X}', prt_level)

    
    def decode_room(self, prt_level):
        line = []
        origin = self.origin+self.pos
        room_num = self.get_byte(line)
        length = self.decode_length(line)
        datab = self.get_byte(line)
        print()
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; Room Number: 0x{room_num:02X}, Length: 0x{length:04X}, Data: 0x{datab:02X}', prt_level)
        end_of_room = self.pos+length-1  # We already read one of these bytes       

        while self.pos < end_of_room:
            self.decode_section(prt_level+1) 

    def decode_command_list(self, end_of_list, prt_level):
        while self.pos < end_of_list:
            self.decode_command(prt_level)
        if self.pos > end_of_list:
            self.print_with_level(f'WARNING: Command list ended at {end_of_list:04X} but cursor is at {self.pos:04X}', prt_level)

    def decode_script(self):
        line = []
        origin = self.origin+self.pos
        list_id = self.get_byte(line)
        length = self.decode_length(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; List ID: 0x{list_id:02X}, Length: 0x{length:04X}', 0)
        end_of_list = self.pos+length
        while self.pos < end_of_list:
            self.decode_room(0)
        