
import engine_com

class Cursor:
    def __init__(self, binary_data,origin):
        self.binary_data = binary_data
        self.origin = origin
        self.addr = origin

    def set_address(self,addr):
        self.addr = addr

    def get_byte(self,addr=None):
        if addr is not None:
            self.addr = addr
        ret = self.binary_data[self.addr-self.origin]
        self.addr += 1
        return ret


class FirstScripter:

    def __init__(self, info):
        self.info = info
        self.packed_strings = engine_com.get_packed_strings(info)
        self.room_info = engine_com.get_room_info(info)
        self.script_comments = engine_com.collect_script_comments(info)
        self.binary_data = engine_com.read_binary(info)               

    def get_room_text(self, room_num):
        if room_num==0:
            return 'RM_00_nowhere'
        if room_num==0xFF:
            return 'BACKPACK'
        return f'RM_{room_num:02X}_{self.info["Rooms"][room_num]}'
    
    def get_object_text(self, obj_num):
        return f'OBJ_{obj_num:02X}_{self.info["Objects"][obj_num]}'

    def handle_script_comments(self, addr, line_data, line_text, print_level, new_lines):
        d_text = ''
        for d in line_data:
            d_text += f'{d:02X} '
        d_text = d_text.ljust(10)        
        line_text = ' '*(print_level*4) + line_text
        nl = f'{addr:04X}: {d_text} ; {line_text}'
        if addr in self.script_comments['line_comments']:
            for t in self.script_comments['line_comments'][addr]:
                new_lines.append(t)
        if addr in self.script_comments['end_comments']:
            nl = nl + self.script_comments['end_comments'][addr]
        new_lines.append(nl)      

    def decode_01_move_look(self, cn, addr, new_lines, print_level):
        rn = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+self.get_room_text(rn)+')'                
        self.handle_script_comments(addr, [cn,rn], com_text, print_level, new_lines)
        return addr+2
    
    def decode_02_obj_in_pack(self, cn, addr, new_lines, print_level):
        obj_num = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+self.get_object_text(obj_num)+')'                
        self.handle_script_comments(addr, [cn,obj_num], com_text, print_level, new_lines)
        return addr+2
    
    def decode_03_obj_in_room_pack(self, cn, addr, new_lines, print_level):
        obj_num = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+self.get_object_text(obj_num)+')'                
        self.handle_script_comments(addr, [cn,obj_num], com_text, print_level, new_lines)
        return addr+2
    
    def decode_04_print(self, cn, addr, new_lines, print_level):
        a = self.cursor.get_byte()
        b = self.cursor.get_byte()
        if self.info['IsLittleEndian']:
            ptr = a + (b<<8)
        else:
            ptr = (a<<8) + b
        ps_data = self.packed_strings[ptr]        
        txt = f'(PS_{ps_data['ps_num']:02X}) {ps_data['text'][0]}'
        self.handle_script_comments(addr, [cn,a,b], self.info["Commands"][cn][0]+txt, print_level, new_lines)
        for txt in ps_data['text'][1:]:
            new_lines.append(';                  '+' '*(print_level*4)+'             '+txt)
        return addr+3
    
    def decode_05_print_score_stop(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_07_stop_pass(self, cn, addr, new_lines, print_level):
        sz = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+' ...'
        self.handle_script_comments(addr, [cn,sz], com_text, print_level, new_lines)

        self.decode_script(addr+2, new_lines, sz-1, print_level+1)
        return addr+sz+1
    
    def decode_08_print_score(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_09_end_game(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
        
    def decode_0A_assert_random(self, cn, addr, new_lines, print_level):
        value = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+f'0x{value:02X}'+')'
        self.handle_script_comments(addr, [cn,value], com_text, print_level, new_lines)
        return addr+2
    
    def decode_0B_drop_object(self, cn, addr, new_lines, print_level):
        obj_num = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+self.get_object_text(obj_num)+')'                
        self.handle_script_comments(addr, [cn,obj_num], com_text, print_level, new_lines)
        return addr+2
    
    def decode_0C_move_to_last(self, cn, addr, new_lines, print_level):
        rn = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+self.get_room_text(rn)+')'
        self.handle_script_comments(addr, [cn,rn], com_text, print_level, new_lines)
        return addr+2
    
    def decode_0D_just_emerald(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_0E_move_to_last_room(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_0F_print_inventory(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_10_print_room(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_11_matches_user_input(self, cn, addr, new_lines, print_level):
        obj_num = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+self.get_object_text(obj_num)+')'                
        self.handle_script_comments(addr, [cn,obj_num], com_text, print_level, new_lines)
        return addr+2
    
    def decode_12_get_object(self, cn, addr, new_lines, print_level):
        obj_num = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+self.get_object_text(obj_num)+')'                
        self.handle_script_comments(addr, [cn,obj_num], com_text, print_level, new_lines)
        return addr+2
    
    def decode_14_ok(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_15_move_to_room(self, cn, addr, new_lines, print_level):
        obn = self.cursor.get_byte()        
        rn = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+self.get_object_text(obn)+', '+self.get_room_text(rn)+')'                
        self.handle_script_comments(addr, [cn,obn,rn], com_text, print_level, new_lines)
        return addr+3
    
    def decode_16_get_user_input(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_17_drop_users_object(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_18_move_object_to_current(self, cn, addr, new_lines, print_level):
        obj_num = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+self.get_object_text(obj_num)+')'                
        self.handle_script_comments(addr, [cn,obj_num], com_text, print_level, new_lines)
        return addr+2
    
    def decode_19_put_object_in(self, cn, addr, new_lines, print_level):
        obj_num1 = self.cursor.get_byte()
        obj_num2 = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+self.get_object_text(obj_num1)+', '+self.get_object_text(obj_num2)+')'                
        self.handle_script_comments(addr, [cn,obj_num1,obj_num2], com_text, print_level, new_lines)
        return addr+3
    
    def decode_1A_is_in_current(self, cn, addr, new_lines, print_level):
        obj_num = self.cursor.get_byte()
        com_text = self.info["Commands"][cn][0]+'('+self.get_object_text(obj_num)+')'                
        self.handle_script_comments(addr, [cn,obj_num], com_text, print_level, new_lines)
        return addr+2
    
    def decode_1B_load_game(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_1C_save_game(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_1D_scramble(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1
    
    def decode_load_second_floor(self, cn, addr, new_lines, print_level):
        self.handle_script_comments(addr, [cn], self.info["Commands"][cn][0]+'()', print_level, new_lines)
        return addr+1

    def decode_command_unknown(self, cn, addr, new_lines, print_level):
        for t in new_lines:
            print(t)
        print(f'Unknown command at {addr:04X} {self.binary_data[addr-self.info["Origin"]]:02X}')
        raise "NOT IMPLEMENTED"
    
    COMMAND_MAP_HAUNTED_HOUSE = {
        0x01: decode_01_move_look,
        0x02: decode_02_obj_in_pack,
        0x03: decode_03_obj_in_room_pack,
        0x04: decode_04_print,
        0x05: decode_10_print_room,
        0x06: decode_07_stop_pass,
        0x07: decode_09_end_game,
        0x08: decode_0B_drop_object,
        0x09: decode_0F_print_inventory,
        0x0A: decode_11_matches_user_input,
        0x0B: decode_12_get_object,
        0x0C: decode_14_ok,
        0x0D: decode_15_move_to_room,
        0x0E: decode_16_get_user_input,
        0x0F: decode_17_drop_users_object,
        0x10: decode_1A_is_in_current,
        # Just for Haunted House, not in Pyramid
        0x11: decode_load_second_floor
    }
    
    COMMAND_MAP = {
        0x01: decode_01_move_look,
        0x02: decode_02_obj_in_pack,
        0x03: decode_03_obj_in_room_pack,
        0x04: decode_04_print,
        0x05: decode_05_print_score_stop,
        0x06: decode_command_unknown,
        0x07: decode_07_stop_pass,
        0x08: decode_08_print_score,
        0x09: decode_09_end_game,
        0x0A: decode_0A_assert_random,
        0x0B: decode_0B_drop_object,
        0x0C: decode_0C_move_to_last,
        0x0D: decode_0D_just_emerald,
        0x0E: decode_0E_move_to_last_room,
        0x0F: decode_0F_print_inventory,
        0x10: decode_10_print_room,
        0x11: decode_11_matches_user_input,
        0x12: decode_12_get_object,
        0x13: decode_command_unknown,
        0x14: decode_14_ok,
        0x15: decode_15_move_to_room,
        0x16: decode_16_get_user_input,
        0x17: decode_17_drop_users_object,
        0x18: decode_18_move_object_to_current,
        0x19: decode_19_put_object_in,
        0x1A: decode_1A_is_in_current,
        0x1B: decode_1B_load_game,
        0x1C: decode_1C_save_game,
        0x1D: decode_1D_scramble,
    }       

    def decode_script(self, addr, new_lines, script_length, print_level):
        end_addr = addr + script_length
        while addr < end_addr:
            # print(f'addr={addr:04X}')
            com = self.cursor.get_byte()
            if 'HauntedHouse' in self.info['File']:
                addr = self.COMMAND_MAP_HAUNTED_HOUSE[com](self, com, addr, new_lines, print_level)
            else:
                addr = self.COMMAND_MAP[com](self, com, addr, new_lines, print_level)
        return addr
    
    def decode_map_script(self, addr, new_lines):
        self.cursor = Cursor(self.binary_data,self.info["Origin"])
        self.cursor.set_address(addr)
        
        while True:
            word_num = self.cursor.get_byte()
            if word_num==0x00:
                self.handle_script_comments(addr, [0], '', 0, new_lines)
                addr += 1
                break            

            word_text = self.info["Words"]["verbs"][word_num][0]
            # print(">>>",word_text)
            script_len = self.cursor.get_byte()                          

            self.handle_script_comments(addr, [word_num, script_len], word_text, 0, new_lines)

            addr = self.decode_script(addr+2, new_lines, script_len-1, 1)        
    
        return addr