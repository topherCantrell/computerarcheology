import unpack
import language
import decode_object

class ScriptCursor:

    SECTION_TYPES = {
        3: 'DESCRIPTION',
        4: 'COMMANDS',
    }    

    ROOMS = {
        "1": {
            0x00: 'nowhere',            
            0x80: '1_HIGHWAY_WEST',
            0x81: '1_WEST_OF_STATION1',
            0x82: '1_FRONT_OF_STATION',
            0x83: '1_GAS_STATION',
            0x84: '1_WEST_OF_STATION2',
            0x85: '1_SOUTHWEST_OF_STATION',
            0x86: '1_JUNKYARD',
            0x87: '1_SOUTHEAST_OF_STATION',
            0x88: '1_EAST_OF_STATION',
            0x89: '1_CITY_LIMIT',
            0x8C: '1_SOUTHWEST_OF_SHERIFF',
            0xAD: '1_NORTH_OF_HIGHWAY1',
            0xAE: '1_NORTH_OF_HIGHWAY2',
            0xAF: '1_NORTH_OF_HIGHWAY3',
            0xB0: '1_DESERT_SOUTH1',
            0xDA: '1_RESTROOM',
        },
        "2": {
            0x8A: '2_WEST_OF_TOWN',
            0x8B: '2_WEST_OF_SHERIFF',
            0x8D: '2_MAIN_STREET_WEST',
            0x8E: '2_SHERIFFS_OFFICE',
            0x8F: '2_SOUTH_OF_SHERIFF',
            0x92: '2_SOUTH_OF_WEST_ALLEY',
            0x9F: '2_NORTHWEST_OF_SALOON',
            0xA0: '2_WEST_SIDE_OF_SALOON',
            0xA1: '2_NORTH_OF_SALOON',
            0xA2: '2_SALOON',
            0xA3: '2_NORTH_OF_WEST_ALLEY',
            0xA4: '2_WEST_ALLEY_NORTH',
            0xB6: '2_DESERT_NORTH1',
            0xB7: '2_DESERT_PATH',
            0xDB: '2_STORM_SHELTER',
        },
        "3": {
            0x90: '3_WEST_ALLEY_INTERSECTION',
            0x91: '3_WEST_ALLEY_SOUTH',
            0x93: '3_TOWN_CENTER',
            0x94: '3_SLIMS_GROCERY',
            0x95: '3_SOUTH_OF_SLIMS',
            0x96: '3_EAST_ALLEY_INTERSECTION',
            0x97: '3_EAST_ALLEY_SOUTH',
            0x98: '3_SOUTH_OF_EAST_ALLEY',
            0xA5: '3_NORTH_OF_BOBS',
            0xA6: '3_HARDWARE_SOUTH',
            0xA7: '3_NORTH_OF_EAST_ALLEY',
            0xA8: '3_EAST_ALLEY_NORTH',
            0xB1: '3_DESERT_SOUTH2',
            0xB3: '3_DESERT',
            0xB8: '3_DESERT_NORTH2',
            0xDC: '3_HARDWARE_NORTH',
        },
        "4": {
            0x99: '4_MAIN_STREET_EAST',
            0x9A: '4_BANK',
            0x9B: '4_SOUTH_OF_BANK',
            0x9C: '4_EAST_OF_TOWN',
            0x9D: '4_EAST_OF_BANK',
            0x9E: '4_SOUTHEAST_OF_BANK',
            0xA9: '4_NORTH_OF_HOTEL',
            0xAA: '4_HOTEL_LOBBY',
            0xAB: '4_NORTHEAST_OF_HOTEL',
            0xAC: '4_EAST_OF_HOTEL',
            0xB2: '4_DESERT_SOUTH3',
            0xB4: '4_HIGHWAY_EAST',
            0xB5: '4_SOUTH_OF_HIGHWAY',
            0xB9: '4_NORTH_OF_HIGHWAY',
            0xDD: '4_HALLWAY',
            0xDE: '4_NORTH_ROOM',
            0xDF: '4_SOUTH_ROOM',
        },
        "5": {
            0x98: '5_??98??',
            0x99: '5_??99??',
            0x9A: '5_??9A??',
            0x9B: '5_NARROW_PATH',
            0x9C: '5_CANYON_FLOOR',
            0x9D: '5_UFO_CRATER',
            0x9E: '5_STRANGE_FOOTPRINTS',
            0x9F: '5_??9F??',
            0xA0: '5_ERRATIC_FOOTPRINTS',
            0xA1: '5_WEAVING_FOOTPRINTS',
            0xA2: '5_STRANGE_FOOTPRINTS1',
            0xA3: '5_??A3??',
            0xA4: '5_??A4??',
            0xA5: '5_??A5??',
            0xA6: '5_??A6??',
            0xBA: '5_??BA??',
            0xBB: '5_??BB??',
            0xBC: '5_??BC??',
            0xBD: '5_FOOTPRINTS_LEAD',
            0xBE: '5_STRANGE_FOOTPRINTS2',
            0xBF: '5_WEARY_FOOTPRINTS',
            0xC0: '5_STAGGERING_FOOTPRINTS',
            0xC1: '5_CRAWL_MARKS',
            0xC2: '5_??C2??',
            0xC3: '5_??C3??',
            0xC4: '5_??C4??',
            0xD3: '5_??D3??',
            0xD4: '5_??D4??',
            0xD5: '5_??D5??',
            0xD6: '5_??D6??',
            0xD7: '5_??D7??',
            0xD8: '5_??D8??',
            0xD9: '5_??D9??',
            0xDA: '5_??DA??',
            0xDB: '5_??DB??',
            0xDC: '5_??DC??',
            0xDD: '5_HIGHWAY_CURVES',
            0xDE: '5_HIGHWAY_LEADS',
            0xDF: '5_??DF??',
            0xE0: '5_??E0??',
            0xE1: '5_??E1??',
            0xE2: '5_??E2??',
            0xE8: '5_??E8??',
            0xE9: '5_??E9??',
            0xEA: '5_??EA??',
            0xEB: '5_??EB??',
            0xEC: '5_??EC??',
            0xED: '5_??ED??',
            0xEE: '5_??EE??',
            0xEF: '5_??EF??',
            0xF0: '5_??F0??',
            0xF1: '5_SMALL_TRAIL1',
            0xF2: '5_TWISTY_TRAIL',
            0xF3: '5_TRAIL_ALSO_FORKS',
            0xF4: '5_??F4??',
            0xF5: '5_??F5??',
            0xF6: '5_SMALL_TRAIL2',
            0xF7: '5_??F7??',
            0xF8: '5_??F8??',
            0xF9: '5_??F9??',
            0xFA: '5_??FA??',
        },        
        "6": {
            0x81: '6_??81??',
            0x82: '6_??82??',
            0x83: '6_??83??',
            0x84: '6_??84??',
            0x85: '6_??85??',
            0x86: '6_??86??',
            0x87: '6_??87??',
            0x88: '6_??88??',
            0x89: '6_??89??',
            0x8A: '6_??8A??',
            0x8B: '6_??8B??',
            0x8C: '6_??8C??',
            0x8D: '6_??8D??',
            0x8E: '6_??8E??',
            0x8F: '6_??8F??',
            0x90: '6_??90??',
            0x91: '6_??91??',
            0x92: '6_??92??',
            0x93: '6_??93??',
            0x94: '6_??94??',
            0x95: '6_??95??',
            0x96: '6_??96??',
            0x97: '6_??97??',
            0xA7: '6_??A7??',
            0xA8: '6_??A8??',
            0xA9: '6_??A9??',
            0xAA: '6_??AA??',
            0xAB: '6_??AB??',
            0xAC: '6_??AC??',
            0xAD: '6_??AD??',
            0xAE: '6_??AE??',
            0xAF: '6_??AF??',
            0xB0: '6_SMALL_OASIS',
            0xB1: '6_??B1??',
            0xB2: '6_??B2??',
            0xB3: '6_??B3??',
            0xB4: '6_??B4??',
            0xB5: '6_??B5??',
            0xB6: '6_??B6??',
            0xB7: '6_??B7??',
            0xB8: '6_??B8??',
            0xB9: '6_??B9??',
            0xC5: '6_??C5??',
            0xC6: '6_HIGHWAY_TURNS',
            0xC7: '6_??C7??',
            0xC8: '6_??C8??',
            0xC9: '6_??C9??',
            0xCA: '6_??CA??',
            0xCB: '6_??CB??',
            0xCC: '6_??CC??',
            0xCD: '6_??CD??',
            0xCE: '6_??CE??',
            0xCF: '6_??CF??',
            0xD0: '6_??D0??',
            0xD1: '6_??D1??',
            0xD2: '6_??D2??',
            0xE3: '6_??E3??',
            0xE4: '6_??E4??',
            0xE5: '6_??E5??',
            0xE6: '6_??E6??',
            0xE7: '6_??E7??',
            0xF7: '6_??F7??',
            0xF8: '6_??F8??',
            0xF9: '6_??F9??',
            0xFA: '6_??FA??',
        },
        "7": {
            0x80: '7_??80??',
            0x82: '7_SREENJARMA_LOUNGE',
            0x83: '7_??83??',
            0x85: '7_PURBLEEBLE_SLEEPING',
            0x87: '7_??87??',
            0x89: '7_MAIKGO_CONTROL',
            0x8B: '7_??8B??',
            0x8D: '7_NAHLUDJ_LIBRARY',
            0x93: '7_??93??',
            0x94: '7_EZPRUNJ_BOMBS',
            0x95: '7_SNOOXBUR_GAS',
            0x96: '7_??96??',
            0x97: '7_ECTOBLASM_BIO',
            0x98: '7_??98??',
            0x99: '7_KEEPRINJ_STORAGE',
        },
        "8": {
            0x84: '8_??84??',
            0x86: '8_FOOGLURN_GALLEY',
            0x88: '8_??88??',
            0x8A: '8_SPLURB_RECREATION',
            0x8C: '8_??8C??',
            0x8E: '8_KURABEL_SICK_BAY',
            0x8F: '8_??8F??',
            0x90: '8_ENURGLE_POWER',
            0x91: '8_??91??',
            0x92: '8_MOTOVATOM_ENGINES',
            0x9A: '8_??9A??',
            0x9B: '8_PLASTOTRO_GUN',
            0x9C: '8_ARMSMITAN_WEAPONRY',
            0x9D: '8_??9D??',
            0x9E: '8_??9E??',
        },
        "9": {
            0x81: '9_SURFACE',
            0x82: '9_CARNEGIE HALL',
            0x83: '9_GRAND CENTRAL STATION',
            0x84: '9_DISCO',
            0x85: '9_MUSEUM',
            0x86: '9_BIOLOGICAL LABS',
            0x87: '9_NURSERY',
            0x88: '9_GREEN HOUSE',
            0x89: '9_LIBRARY',
            0x8A: '9_GENERATOR',
            0x8B: '9_PITTSBURG',
            0x8C: '9_DETROIT',     
        }
    }

    # I want room names to be unique across the whole game.
    for sec in ROOMS:
        for dn in ROOMS[sec]:
            cnt = 0
            g = ROOMS[sec][dn][2:]
            if g.startswith('??'):
                continue
            for sec2 in ROOMS:
                for dn2 in ROOMS[sec2]:
                    g2 = ROOMS[sec2][dn2][2:]
                    if g == g2:
                        cnt += 1
            if cnt > 1:
                raise Exception(f"Room name {g} is not unique")       
        

    def __init__(self, data, origin):
        self.data = data
        self.origin = origin
        self.pos = 0

    def set_pos(self, pos):
        self.pos = pos - self.origin

    def start_new_line(self):
        return self.origin+self.pos, []
    
    def desc_room(self, disk_number, room_num):
        
        if room_num==0x01:
            return f'{room_num:02X}_PLAYER'
        
        if room_num==0x00:
            return f'{room_num:02X}_nowhere'
        
        if room_num<0x80:
            # TODO look up object name
            return f'obj_{room_num:02X}'                
        
        room_sec = self.ROOMS[str(disk_number)]
        
        if room_num in room_sec:
            return f'{room_num:02X}_{room_sec[room_num]}'
        
        return f'??{room_num:02X}??'
        
    def desc_object(self, obj_num):
        if obj_num in decode_object.OBJECT_NAME:
            return f'{obj_num:02X}_{decode_object.OBJECT_NAME[obj_num]}'
        else:
            return f'??{obj_num:02X}??'

    def desc_subroutine(self, sub_num):
        pass

    def desc_section(self, com_num):
        pass
    
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
        #                                                             | 60
        # HIGHWAY WEST. YOU ARE STANDING ON THE HIGHWAY, IN THE DISTANCE TO THE EAST YOU CAN SEE A SMALL TOWN. THERE APPEARS TO BE A GAS STATION ON THE SOUTH SIDE OF THE ROAD ABOUT HALF WAY BETWEEN YOU AND THE TOWN. TO THE WEST, THE HIGHWAY STRETCHES TO THE HORIZON.
        # WEST OF STATION. YOU ARE ON THE ROAD WEST OF THE GAS STATION. FROM HERE YOU CAN SEE A MESSAGE PAINTED ON THE WEST WALL OF THE GAS STATION.
        # FRONT OF STATION. YOU ARE STANDING IN FRONT OF THE LAST CHANCE GAS STATION. TO THE EAST YOU CAN MAKE OUT INDIVIDUAL BUILDINGS IN TOWN. TO THE WEST THE ROAD DISAPPEARS INTO A SEEMINGLY ENDLESS DESERT. A DOOR LEADS SOUTH INTO THE STATION.
        
        return ret

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

    def decode_print_command(self, origin, line, _, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT, Length: 0x{length:04X}', prt_level)        
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

    def decode_switch(self, origin, line, disk_number, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        fn_to_call = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SWITCH, Length: 0x{length:04X}, Function to call: 0x{fn_to_call:02X}', prt_level)
        if fn_to_call != 0x0A and fn_to_call != 0x03 and fn_to_call != 0x05 and fn_to_call != 0x22 and fn_to_call != 0x08: # TODO different descript below
            raise Exception(f"Unknown function to call in SWITCH command: 0x{fn_to_call:02X}")
        
        while self.pos < end_of_command:
            line = []
            origin = self.origin+self.pos
            phrase_num = self.get_byte(line)
            phrase_text = language.PHRASES.get(phrase_num, [f'??{phrase_num:02X}??'])[0]
            self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; Phrase 0x{phrase_num:02X}: "{phrase_text}"', prt_level+1)
            line = []
            origin = self.origin+self.pos
            length_of_phrase = self.decode_length(line)
            self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; ELSE go to: 0x{self.origin+self.pos+length_of_phrase:04X}', prt_level+1)
            self.decode_command(disk_number, prt_level+2)        
    
    def decode_while_pass(self, origin, line, disk_number, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; WHILE PASS, Length: 0x{length:04X}', prt_level)
        while self.pos < end_of_command:
            self.decode_command(disk_number, prt_level+1)
    
    def decode_while_fail(self, origin, line, disk_number, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; WHILE FAIL, Length: 0x{length:04X}', prt_level)
        while self.pos < end_of_command:
            self.decode_command(disk_number, prt_level+1)

    def decode_set_current_room(self, origin, line, disk_number, prt_level):
        room_num = self.get_byte(line)
        if self.data[self.pos] == 0x17 and self.data[self.pos+3] == 0x2F:
            # Followed by a MOVE TO and a LOAD SECTION
            disk_number = self.data[self.pos+4]      
        elif self.data[self.pos] == 0x2F:
            # Followed by a LOAD SECTION
            disk_number = self.data[self.pos+1]    
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SET CURRENT ROOM, room={self.desc_room(disk_number, room_num)}', prt_level)

    def decode_load_section_from_disk(self, origin, line, _, prt_level):
        data = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; LOAD SECTION FROM DISK, Section: 0x{data:02X}', prt_level)

    def decode_move_to(self, origin, line, disk_number,prt_level):
        obj_num = self.get_byte(line)
        dest_room = self.get_byte(line)
        # The room is always in the current section (TODO excpet for the weird object case)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; MOVE TO, obj={self.desc_object(obj_num)}, room={self.desc_room(disk_number, dest_room)}', prt_level)

    def decode_is_less_equal_last_random(self, origin, line, _, prt_level):
        value = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS LESS OR EQUAL TO LAST RANDOM, Value: 0x{value:02X}', prt_level)

    def decode_move_and_look(self, origin, line, disk_number, prt_level):
        dest_room = self.get_byte(line)
        # The room is always in the current section
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; MOVE AND LOOK, room={self.desc_room(disk_number,dest_room)}', prt_level)

    def decode_execute_and_reverse_status(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; EXECUTE AND REVERSE STATUS', prt_level)

    def decode_set_var_object(self, origin, line, _, prt_level):
        obj_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SET VAR OBJECT, obj={self.desc_object(obj_num)}', prt_level)

    def decode_compare_to_second_noun(self, origin, line, _, prt_level):
        word_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; COMPARE TO SECOND NOUN, Word number: 0x{word_num:02X}', prt_level)

    def decode_is_in_pack_or_current_room(self, origin, line, _, prt_level):
        obj_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS IN PACK OR CURRENT ROOM, obj={self.desc_object(obj_num)}', prt_level)

    def decode_is_located(self, origin, line, disk_number, prt_level):
        room_num = self.get_byte(line)
        obj_num = self.get_byte(line)
        # The room is always in the current section (TODO excpet for the weird object case)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS LOCATED, room={self.desc_room(disk_number, room_num)}, obj={self.desc_object(obj_num)}', prt_level)

    def decode_is_owned(self, origin, line, _, prt_level):
        obj_num = self.get_byte(line)
        a = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS OWNED BY, A=0x{a:02X}, obj={self.desc_object(obj_num)}', prt_level)

    def decode_print_room_description(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT ROOM DESCRIPTION', prt_level)

    def decode_is_first_noun(self, origin, line, _, prt_level):
        word_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS FIRST NOUN, Word number: 0x{word_num:02X}', prt_level)

    def decode_attack_VAR(self, origin, line, _, prt_level):
        points = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; ATTACK VAR, Points: {points}', prt_level)

    def decode_fail(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; FAIL', prt_level)

    def decode_is_input_phrase(self, origin, line, _, prt_level):
        phrase_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS INPUT PHRASE, Phrase number: 0x{phrase_num:02X}', prt_level)

    def decode_set_active(self, origin, line, _, prt_level):
        obj_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SET ACTIVE, obj={self.desc_object(obj_num)}', prt_level)
    
    def decode_drop_var(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; DROP VAR', prt_level)

    def decode_exit_program(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; EXIT PROGRAM', prt_level)

    def decode_print2(self, origin, line, _, prt_level):
        length = self.decode_length(line)
        end_of_command = self.pos+length
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT, Length: 0x{length:04X}', prt_level)        
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

    def decode_set_var_to_first_noun(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SET VAR TO FIRST NOUN', prt_level)
        
    def decode_set_var_to_second_noun(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SET VAR TO SECOND NOUN', prt_level)  

    def decode_print_linefeed(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT LINEFEED', prt_level)

    def decode_bump_score(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; BUMP SCORE 10%', prt_level)

    def decode_unknown2D(self, origin, line, _, prt_level):
        value = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN2D, Value: 0x{value:02X}', prt_level)

    def decode_unknown2E(self, origin, line, _, prt_level):
        value = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN2E, Value: 0x{value:02X}', prt_level)

    def decode_unknown2A(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN2A', prt_level)

    def decode_unknown31(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN31', prt_level)
    def decode_unknown32(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN32', prt_level)
    def decode_unknown33(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN33', prt_level)
    def decode_unknown34(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN34', prt_level)
    def decode_unknown35(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN35', prt_level)
    def decode_unknown0F(self, origin, line, _, prt_level):        
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN0F', prt_level)
    def decode_unknown39(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN39', prt_level)
    def decode_unknown36(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN36', prt_level)
    def decode_unknown37(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN37', prt_level)
    def decode_unknown13(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN13', prt_level)
    def decode_unknown27(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN27', prt_level)
    def decode_unknown28(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; UNKNOWN28', prt_level)


    def decode_swap(self, origin, line, _, prt_level):
        a = self.get_byte(line)
        b = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; SWAP, obj1={self.desc_object(a)}, obj2={self.desc_object(b)}', prt_level)

    def decode_heal_var(self, origin, line, _, prt_level):
        points = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; HEAL VAR, Points: {points}', prt_level)

    def decode_print_open_var(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT OPEN VAR', prt_level)

    def decode_print_second_noun(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT SECOND NOUN', prt_level)

    def decode_execute_phrase(self, origin, line, _, prt_level):
        phrase_num = self.get_byte(line)
        first_noun = self.get_byte(line)
        second_noun = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; EXECUTE PHRASE, Phrase number: 0x{phrase_num:02X}, First noun: 0x{first_noun:02X}, Second noun: 0x{second_noun:02X}', prt_level)
    
    def decode_is_active_this(self, origin, line, _, prt_level):
        obj_num = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS ACTIVE THIS, obj={self.desc_object(obj_num)}', prt_level)

    def decode_check_var(self, origin, line, _, prt_level):
        value = self.get_byte(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; CHECK VAR, Value: 0x{value:02X}', prt_level)

    def decode_is_var_owned_by_active(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; IS VAR OWNED BY ACTIVE', prt_level)

    def decode_clear_screen(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; CLEAR SCREEN', prt_level)

    def decode_print_first_noun(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT FIRST NOUN', prt_level)

    def decode_print_var(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT VAR', prt_level)

    def decode_wait_for_key123(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; WAIT FOR KEY 1, 2, OR 3', prt_level)

    def decode_print_score(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT SCORE', prt_level)

    def decode_print_inventory(self, origin, line, _, prt_level):
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; PRINT INVENTORY', prt_level)    

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
        0x0F: decode_unknown0F,
        0x10: decode_drop_var,
        0x11: decode_print_first_noun,
        0x12: decode_print_second_noun,
        0x13: decode_unknown13,
        0x14: decode_execute_and_reverse_status,
        0x15: decode_check_var, 
        0x16: decode_print_var,
        0x17: decode_move_to,
        0x18: decode_is_var_owned_by_active,
        # 0x19
        0x1A: decode_set_var_to_first_noun,
        0x1B: decode_set_var_to_second_noun,
        0x1C: decode_set_var_object,
        0x1D: decode_attack_VAR,
        0x1E: decode_swap,
        0x1F: decode_print2,
        0x20: decode_is_active_this,
        0x21: decode_execute_phrase,
        # 0x22
        0x23: decode_heal_var,
        0x24: decode_exit_program,
        0x25: decode_print_linefeed,
        0x26: decode_print_score,
        0x27: decode_unknown27,
        0x28: decode_unknown28,
        0x29: decode_print_open_var,
        0x2A: decode_unknown2A,
        # 0x2B
        0x2C: decode_set_active,
        0x2D: decode_unknown2D,
        0x2E: decode_unknown2E,
        0x2F: decode_load_section_from_disk,
        0x30: decode_set_current_room,
        0x31: decode_unknown31,
        0x32: decode_unknown32,
        0x33: decode_unknown33,
        0x34: decode_unknown34,
        0x35: decode_unknown35,
        0x36: decode_unknown36,
        0x37: decode_unknown37,
        0x38: decode_bump_score,
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

    def decode_command(self, disk_number, prt_level):
        line = []
        origin = self.origin+self.pos
        command = self.get_byte(line)
        if command >= 0x80:
            # This command is a routine call
            self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; ROUTINE 0x{command:02X}', prt_level)                
            return

        if command not in self.COMMANDS:                
            raise Exception(f'Unknown command {command:02X} at {origin:04X}')
        
        fn = self.COMMANDS[command]
        fn(self, origin, line, disk_number, prt_level)
    
    def decode_section(self, disk_number, prt_level):
        line = []
        origin = self.origin+self.pos
        section_type = self.get_byte(line)
        length = self.decode_length(line)
        end_of_section = self.pos+length

        st = self.SECTION_TYPES.get(section_type, f'??{section_type:02X}??')
        print(';')
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; Section {st}, Length: 0x{length:04X}', prt_level)
        
        while self.pos < end_of_section:                        
            self.decode_command(disk_number,prt_level+1)
            
        if self.pos != end_of_section:
            self.print_with_level(f'WARNING: Section ended at {end_of_section:04X} but cursor is at {self.pos:04X}', prt_level)

    
    def decode_room(self, disk_number, prt_level):
        line = []
        origin = self.origin+self.pos
        room_num = self.get_byte(line)
        length = self.decode_length(line)
        datab = self.get_byte(line)
        print()
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; room={self.desc_room(disk_number,room_num)}, Length: 0x{length:04X}, Data: 0x{datab:02X}', prt_level)
        end_of_room = self.pos+length-1  # We already read one of these bytes       

        while self.pos < end_of_room:
            self.decode_section(disk_number, prt_level+1)
        if self.pos != end_of_room:
            self.print_with_level(f'WARNING: Room ended at {end_of_room:04X} but cursor is at {self.pos:04X}', prt_level)

    def decode_command_list(self, end_of_list, disk_number, prt_level):
        while self.pos < end_of_list:
            self.decode_command(disk_number, prt_level)
        if self.pos > end_of_list:
            self.print_with_level(f'WARNING: Command list ended at {end_of_list:04X} but cursor is at {self.pos:04X}', prt_level)

    def decode_script(self, disk_number):
        line = []
        origin = self.origin+self.pos
        list_id = self.get_byte(line)
        length = self.decode_length(line)
        self.print_with_level(f'{origin:04X}: {self.build_data_line(line)} ; List ID: 0x{list_id:02X}, Length: 0x{length:04X}', 0)
        end_of_list = self.pos+length
        while self.pos < end_of_list:
            self.decode_room(disk_number, 0)
        if self.pos != end_of_list:
            self.print_with_level(f'WARNING: Script ended at {end_of_list:04X} but cursor is at {self.pos:04X}', 0)
        

