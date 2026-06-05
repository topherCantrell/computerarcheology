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

    def build_data_line(self, data):
        g = ''
        for b in data:
            g += f"{b:02X} "
        return g

    def decode_length(self, pos, data_fill):
        if self.data[pos] < 128:
            ret = self.data[pos]
            data_fill.append(self.data[pos])
            self.pos += 1
            return ret
        else:
            ret = (self.data[pos]-128)*256 + self.data[pos+1]
            data_fill.extend(self.data[pos:pos+2])
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
        length = self.decode_length(self.pos, line)
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
        length = self.decode_length(self.pos, line)
        end_of_command = self.pos+length
        fn_to_call = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SWITCH, Length: 0x{length:04X}, Function to call: 0x{fn_to_call:02X}', prt_level)
        if fn_to_call != 0x0A and fn_to_call != 0x03 and fn_to_call != 0x05: # TODO different descript below
            raise Exception(f"Unknown function to call in SWITCH command: 0x{fn_to_call:02X}")
        
        while self.pos < end_of_command:
            line = []
            origin = self.origin+self.pos
            phrase_num = self.get_byte(line)
            self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; Phrase number: 0x{phrase_num:02X}', prt_level+1)
            line = []
            origin = self.origin+self.pos
            length_of_phrase = self.decode_length(self.pos, line)
            self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; ELSE go to: 0x{self.origin+self.pos+length_of_phrase:04X}', prt_level+1)
            self.decode_command(prt_level+2)        
    
    def decode_while_pass(self, origin, line, prt_level):
        length = self.decode_length(self.pos, line)
        end_of_command = self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; WHILE PASS, Length: 0x{length:04X}', prt_level)
        while self.pos < end_of_command:
            self.decode_command(prt_level+1)
    
    def decode_while_fail(self, origin, line, prt_level):
        length = self.decode_length(self.pos, line)
        end_of_command = self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; WHILE FAIL, Length: 0x{length:04X}', prt_level)
        while self.pos < end_of_command:
            self.decode_command(prt_level+1)

    def decode_unknown1(self, origin, line, prt_level):
        data = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN1, Data: 0x{data:02X}', prt_level)

    def decode_unknown2(self, origin, line, prt_level):
        data = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN2 Data: 0x{data:02X}', prt_level)

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
    
    def drop_var(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; DROP VAR', prt_level)

    def decode_print2(self, origin, line, prt_level):
        length = self.decode_length(self.pos, line)
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

    def decode_set_var_to_second_noun(self, origin, line, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SET VAR TO SECOND NOUN', prt_level)  

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
        0x10: drop_var,
        0x14: decode_execute_and_reverse_status,
        0x17: decode_move_to,
        0x1B: decode_set_var_to_second_noun,
        0x1C: decode_set_var_object,
        0x1D: decode_attack_VAR,
        0x1F: decode_print2,
        0x2C: decode_set_active,
        0x2F: decode_unknown2,
        0x30: decode_unknown1,
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
        length = self.decode_length(self.pos, line)
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
        length = self.decode_length(self.pos, line)
        datab = self.get_byte(line)
        print()
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; Room Number: 0x{room_num:02X}, Length: 0x{length:04X}, Data: 0x{datab:02X}', prt_level)
        end_of_room = self.pos+length-1  # We already read one of these bytes       

        while self.pos < end_of_room:
            self.decode_section(prt_level+1) 

    def decode_script(self):
        line = []
        origin = self.origin+self.pos
        list_id = self.get_byte(line)
        length = self.decode_length(self.pos, line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; List ID: 0x{list_id:02X}, Length: 0x{length:04X}', 0)
        end_of_list = self.pos+length
        while self.pos < end_of_list:
            self.decode_room(0)
        