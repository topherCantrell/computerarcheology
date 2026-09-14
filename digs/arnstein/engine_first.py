import specifics_pyramid
import specifics_hauntedhouse1
import specifics_hauntedhouse2
import engine_com
from engine_first_scripter import FirstScripter

COMMANDS_PYRAMID = {
0x01:     ['move_look',                          'room_num'],
0x02:     ['is_in_pack',                         'obj_num'],
0x03:     ['is_in_pack_or_current_room',         'obj_num'],
0x04:     ['print','ps_ptr'                      ],
0x05:     ['death_and_resurrect'                 ],
0x06:     None,
0x07:     ['stop_if_pass'                        ],
0x08:     ['print_score'                         ],
0x09:     ['end_of_game'                         ],
0x0A:     ['pyramid_crawl_move_random',          'value'],
0x0B:     ['drop_object_print_ok',               'obj_num'],
0x0C:     ['move_to_room_if_was_last',           'room_num'],
0x0D:     ['is_pack_just_emerald'                ],
0x0E:     ['move_to_last_room'                   ],
0x0F:     ['print_inventory'                     ],
0x10:     ['print_room_description'              ],
0x11:     ['is_object_user_input',               'obj_num'],
0x12:     ['get_from_room_print_ok',             'obj_num'],
0x13:     None,
0x14:     ['print_ok'                            ],
0x15:     ['move_object_to_room',                'obj_num','room_num'],
0x16:     ['get_users_object_print_ok'           ],
0x17:     ['drop_users_object_print_ok'          ],
0x18:     ['move_object_to_current_room',        'obj_num'],
0x19:     ['put_object_in_container_print_ok',   'obj_num','obj_num'],
0x1A:     ['is_in_current_room',                 'obj_num'],
0x1B:     ['load_game'                           ],
0x1C:     ['save_game'                           ],
0x1D:     ['scramble_directions_print_ack'       ],
}

COMMANDS_HAUNTEDHOUSE = {
    0x01: COMMANDS_PYRAMID[0x01],
    0x02: COMMANDS_PYRAMID[0x02],
    0x03: COMMANDS_PYRAMID[0x03],
    0x04: COMMANDS_PYRAMID[0x04],
    0x05: COMMANDS_PYRAMID[0x10],
    0x06: COMMANDS_PYRAMID[0x07],
    0x07: COMMANDS_PYRAMID[0x09],
    0x08: COMMANDS_PYRAMID[0x0B],
    0x09: COMMANDS_PYRAMID[0x0F],
    0x0A: COMMANDS_PYRAMID[0x11],
    0x0B: COMMANDS_PYRAMID[0x12],
    0x0C: COMMANDS_PYRAMID[0x14],
    0x0D: COMMANDS_PYRAMID[0x15],
    0x0E: COMMANDS_PYRAMID[0x16],
    0x0F: COMMANDS_PYRAMID[0x17],
    0x10: COMMANDS_PYRAMID[0x1A],
    # Just for Haunted House, not in Pyramid
    0x11: ['load_second_floor']
}

ADDRESSES = {
    "TRS80": {
        "PYRAMID_L1": {
            "File": "../../../content/TRS80/Pyramid/Code1.md",
            "ROM": "../../../content/TRS80/Pyramid/roms/Pyramid1.bin",
            "Origin": 0x4200,
            "IsLittleEndian": True,
            "Commands": COMMANDS_PYRAMID,
            "Rooms": specifics_pyramid.ROOMS,
            "Objects": specifics_pyramid.OBJECTS,
            "Words": specifics_pyramid.WORDS,
            "RoomTable": (0x4825, 0x4965),            
            "AmbientLightTable": (0x4EE2, 0x4F82),
            "ObjectData": (0x4F84, 0x4FDA),
            "ObjectDescriptions": (0x4FE4, 0x503A),
            "ScriptCommands": (0x503C, 0x5074),
            "WordTable": (0x5622, 0x5903),
            "RoomScripts": (0x4969, 0x4EE0),
            "GeneralScript": (0x5904, 0x5B2E)
        },
        "PYRAMID_L2": {
            "File": "../../../content/TRS80/Pyramid/Code.md",
            "ROM": "../../../content/TRS80/Pyramid/roms/Pyramid.bin",
            "Origin": 0x4300,
            "IsLittleEndian": True,
            "Commands": COMMANDS_PYRAMID,
            "Rooms": specifics_pyramid.ROOMS,
            "Objects": specifics_pyramid.OBJECTS,
            "Words": specifics_pyramid.WORDS,
            "RoomTable": (0x4888, 0x49C8),            
            "AmbientLightTable": (0x4F45, 0x4FE5),
            "ObjectData": (0x4FE7, 0x503D),
            "ObjectDescriptions": (0x5047, 0x509D),
            "ScriptCommands": (0x509F, 0x50D7),
            "WordTable": (0x56CE, 0x59AF),
            "RoomScripts": (0x49CC, 0x4F43),
            "GeneralScript": (0x59B0, 0x5BDA)
        },
        "HAUNTEDHOUSE1": {
            "File": "../../../content/TRS80/HauntedHouse/Code1.md",
            "ROM": "../../../content/TRS80/HauntedHouse/roms/Code1.bin",
            "Origin": 0x42E9,
            "IsLittleEndian": True,
            "Commands": COMMANDS_HAUNTEDHOUSE,
            "Rooms": specifics_hauntedhouse1.ROOMS,
            "Objects": specifics_hauntedhouse1.OBJECTS,
            "Words": specifics_hauntedhouse1.WORDS,
            "RoomTable": (0x477F, 0x47BB),            
            "AmbientLightTable": None,
            "ObjectData": (0x48C8, 0x48E0),
            "ObjectDescriptions": (0x48E3, 0x48FB),
            "ScriptCommands": (0x48FD, 0x491D),
            "WordTable": (0x4A4B, 0x4AF1),
            "RoomScripts": (0x47BF, 0x48C7),
            "GeneralScript": (0x4AF2, 0x4B34)
        },
        "HAUNTEDHOUSE2": {
            "File": "../../../content/TRS80/HauntedHouse/Code2.md",
            "ROM": "../../../content/TRS80/HauntedHouse/roms/Code2.bin",
            "Origin": 0x435E,
            "IsLittleEndian": True,
            "Commands": COMMANDS_HAUNTEDHOUSE,
            "Rooms": specifics_hauntedhouse2.ROOMS,
            "Objects": specifics_hauntedhouse2.OBJECTS,
            "Words": specifics_hauntedhouse2.WORDS,
            "RoomTable": (0x4782, 0x479E),            
            "AmbientLightTable": None,
            "ObjectData": (0x4915, 0x492D),
            "ObjectDescriptions": (0x4933, 0x494B),
            "ScriptCommands": (0x494D, 0x496B),
            "WordTable": (0x4A9A, 0x4B19),
            "RoomScripts": (0x47A2, 0x4914),
            "GeneralScript": (0x4B1A, 0x4B50)
        },        
    }, 
    "COCO": {
        "PYRAMID": {
            "File": "../../../content/CoCo/Pyramid/Code.md",
            "ROM": "../../../content/CoCo/Pyramid/roms/pyramid.bin",
            "Origin": 0x0600,
            "IsLittleEndian": False,
            "Commands": COMMANDS_PYRAMID,
            "Rooms": specifics_pyramid.ROOMS,
            "Objects": specifics_pyramid.OBJECTS,
            "Words": specifics_pyramid.WORDS,
            "RoomTable": (0x112E, 0x126E),            
            "AmbientLightTable": (0x17EB, 0x188B),
            "ObjectData": (0x188D, 0x18E3),
            "ObjectDescriptions": (0x18ED, 0x1943),
            "ScriptCommands": (0x0A17, 0x0A4F),
            "WordTable": (0x3C40, 0x3F15),
            "RoomScripts": (0x1272, 0x17E9),
            "GeneralScript": (0x1945, 0x1B65)
        },        
    }
}

def update_command_names(info):
    lines = engine_com.read_code_file(info["File"])

    # Update the command table itself
    ps, pe = engine_com.find_start_and_end(lines, info["ScriptCommands"][0], info["ScriptCommands"][1])
    if lines[ps-1] != 'ScriptCommands:':
        raise Exception(f'Expected ScriptCommands: label at {info["ScriptCommands"][0]:04X} (line {ps})')
    addresses = {}
    while ps < pe:
        line = lines[ps]
        ps += 1
        i = line.find('COM_')
        if i>-1:
            cn = int(line[i+4:i+6], 16)
            if info['IsLittleEndian']:
                addresses[cn] = int(line[9:11] + line[6:8], 16)                
            else:
                addresses[cn] = int(line[6:8] + line[9:11], 16)                                        
            nline = f'{line[:11]}        ; COM_{cn:02X}_{info["Commands"][cn][0]}({", ".join(info["Commands"][cn][1:])})'
            print(">>>", line, nline)
            lines[ps-1] = nline    

    # Update the individual command routines
    for i, addr in addresses.items():
        if not info['IsLittleEndian'] and (i == 0x05 or i == 0x09):
            # Special syntax for these two in the CoCo because they are one command
            continue
        # The label 
        ps,pe = engine_com.find_start_and_end(lines, addr, addr)
        lab = lines[ps-1]
        if lab.startswith('COM_') and lab.endswith(':'):
            labn = f'COM_{i:02X}_{info["Commands"][i][0]}:'
            lines[ps-1] = labn
            print('>>>',lab,labn)
        else:
            raise Exception(f'Label not found for command at {addr:04X} (line {ps})')
        
        # The markdown
        while not lines[ps].startswith('# COM_'):
            ps -= 1
        if not lines[ps].startswith(f'# COM_{i:02X}_'):
            raise Exception(f'Markdown not found for command at {addr:04X} (line {ps})')
        lines[ps] = f'# COM_{i:02X}_{info["Commands"][i][0]}({", ".join(info["Commands"][i][1:])})'
        print('>>>', lines[ps])

        # TODO updae all the comments and headers for all the commands. Make TRS80LV2 Pyramid the reference

    engine_com.write_code_file(info["File"], lines)

def update_room_names(info):
    # RoomTable
    lines = engine_com.read_code_file(info["File"])
    ps,pe = engine_com.find_start_and_end(lines, info["RoomTable"][0], info["RoomTable"][1])

    if lines[ps-2] != 'RoomTable:':        
        raise Exception(f'Expected RoomTable: label at {info["RoomTable"][0]:04X} (line {ps-2})')

    room_ps = {}
    rn = 0
    while ps < pe:
        line = lines[ps]
        ps += 1
        if line.startswith(';'):            
            continue
        rn += 1
        if line[4]!=':' or line[18]!=';':
            raise Exception(f'Expected room table entry at {info["RoomTable"][0]:04X} (line {ps})')
        
        if line[6:17] == '00 00 00 00':
            rm_text = '                                '
            ps_text = '     '
            com_text = line[19:].strip()
        else:          
            rm_text = f'RM_{rn:02X}_{info["Rooms"][rn].ljust(26)}'  
            i = line.rfind('PS_')
            ps_text = line[i:i+5]
            if ps_text in room_ps:
                room_ps[ps_text].append(f'RM_{rn:02X}')
            else:
                room_ps[ps_text] = [rm_text.strip()]
            com_text = line[i+5:].strip()
        nl = f'{line[:17]} ; {rm_text} {ps_text}    {com_text}'        
        print(">>>",nl)
        lines[ps-1] = nl

    # AmbientLight table

    if info["AmbientLightTable"] is not None:

        ps,pe = engine_com.find_start_and_end(lines, info["AmbientLightTable"][0], info["AmbientLightTable"][1])
        if lines[ps-2] != 'AmbientLightTable:':        
            raise Exception(f'Expected AmbientLightTable: label at {info["AmbientLightTable"][0]:04X} (line {ps-2})')
        
        rn = 0
        while ps < pe:
            line = lines[ps]
            ps += 1
            if line.startswith(';'):            
                continue
            rn += 1
            if line[4]!=':':
                raise Exception(f'Expected room table entry at {info["RoomTable"][0]:04X} (line {ps})')
            i = line.find(';')
            com_text = line[i+1:].strip()
            i = com_text.find(' ')
            if i > -1:
                com_text = com_text[i+1:].strip()
            else:
                com_text = ''
            if rn in info["Rooms"]:
                rm_text = f'RM_{rn:02X}_{info["Rooms"][rn].ljust(26)}'
            else:
                rm_text = f'RM_{rn:02X}_{"".ljust(26)}'
            nl = f'{line[:11]} ; {rm_text}    {com_text}'
            print(">>>",nl)
            lines[ps-1] = nl

    # PS_xx room description comments

    for ps_text, room_nums in room_ps.items():
        for i in range(len(lines)):
            if lines[i].startswith(f'{ps_text}:'):
                break
        line = lines[i]
        nl = f'{line[:6]} ; {", ".join(room_nums)}'        
        print(">>>", nl)
        lines[i] = nl        

    # RoomScripts (elsewhere)
    # Objects (elsewhere)
    # GeneralScript (elsewhere)

    engine_com.write_code_file(info["File"], lines) 

def update_objects(info):
    lines = engine_com.read_code_file(info["File"])
    ps,pe = engine_com.find_start_and_end(lines, info["ObjectData"][0], info["ObjectData"][1])

    onum = 0
    while ps < pe:
        line = lines[ps]
        
        ps += 1
        if line.startswith(';'):            
            continue
        if line[4]!=':' or line[12]!=';':
            raise Exception(f'Expected object data entry at {info["ObjectData"][0]:04X} (line {ps})')
        
        onum += 1
        if onum not in info["Objects"]:
            continue

        obj_text = f'OBJ_{onum:02X}_{info["Objects"][onum]}'

        data = line[13:].strip()
        if not data:
            continue

        rn  = int(line[9:11], 16)
        if rn==0:
            rn_text = '*'
        else:
            rn_text = f'RM_{rn:02X}_{info["Rooms"][rn]}'
        

        nl = f'{line[:22]} {obj_text.ljust(24)} {rn_text}'
        
        print(">>>",nl)
        lines[ps-1] = nl        

    # object descriptions

    ps,pe = engine_com.find_start_and_end(lines, info["ObjectDescriptions"][0], info["ObjectDescriptions"][1])
    if lines[ps-2] != 'ObjectDescriptions:':        
        raise Exception(f'Expected ObjectDescriptions: label at {info["ObjectDescriptions"][0]:04X} (line {ps-2})')
    
    onum = 0
    while ps < pe:
        line = lines[ps]
        ps += 1
        if line.startswith(';'):
            continue
        onum += 1
        if onum not in info["Objects"]:
            continue

        obj_text = f'OBJ_{onum:02X}_{info["Objects"][onum]}'

        i = line.find('PS_')
        if i<0:
            continue
        
        end_text = line[i:].strip()
        nl = f'{line[:11]} ; {obj_text.ljust(24)}    {end_text}'

        print(">>>",nl)
        lines[ps-1] = nl

    engine_com.write_code_file(info["File"], lines)

def update_room_scripts(info):

    coms = engine_com.collect_script_comments(info)

    ps_info = engine_com.get_packed_strings(info)
    room_ptrs = engine_com.get_room_info(info)

    lines = engine_com.read_code_file(info["File"])    

    pso,peo = engine_com.find_start_and_end(lines, info["RoomScripts"][0], info["RoomScripts"][1])
    while lines[pso].strip():
        pso -= 1
    pso += 1

    new_lines = []

    scripter = FirstScripter(info)
    addr = engine_com.get_address_for(lines,pso)
    end_addr = engine_com.get_address_for(lines,peo)

    while addr < end_addr:        
        ps,pe = engine_com.find_start_and_end(lines, addr, addr)        
        while True:
            ps -= 1
            line = lines[ps]
            i = line.find(';')
            comment = ''
            if i > -1:
                comment = line[i:].strip()
                line = line[:i]
            if line.strip().endswith(':'):
                break        
            
        sc_info = room_ptrs[addr]
        rn = sc_info['number']
        new_lines.append(f'Script_RM_{rn:02X}_{info["Rooms"][rn]}: {comment}')
        # print('>>>',nl)
        pi = sc_info['description']
        new_lines.append(f'; PS_{pi['ps_num']:02X}')        
        # print('>>>',nl)
        if 'Haunted' in info['File']:
            tt = pi['text'][:]
            tt[0] = 'you_are_at_the_'+tt[0]
        else:
            tt = pi['text']
        for t in tt:
            # print('>>>', '; '+t)
            new_lines.append('; '+t)
        new_lines.append(';') 

        addr = scripter.decode_map_script(addr, new_lines)        

        if addr < end_addr:
            new_lines.append('')          

    rep_lines = lines[:pso] + new_lines + lines[peo:]
    engine_com.write_code_file(info["File"], rep_lines)    

def update_general_script(info):
    # coms = engine_com.collect_script_comments(info)

    # ps_info = engine_com.get_packed_strings(info)
    # room_ptrs = engine_com.get_room_info(info)

    lines = engine_com.read_code_file(info["File"])    

    pso,peo = engine_com.find_start_and_end(lines, info["GeneralScript"][0], info["GeneralScript"][1])
    
    new_lines = []

    scripter = FirstScripter(info)
    addr = engine_com.get_address_for(lines,pso)

    addr = scripter.decode_map_script(addr, new_lines)

    rep_lines = lines[:pso] + new_lines + lines[peo:]
    engine_com.write_code_file(info["File"], rep_lines)    
    


info = ADDRESSES["TRS80"]["PYRAMID_L2"]
update_command_names(info)
update_room_names(info)
update_objects(info)
update_room_scripts(info)
update_general_script(info)

info = ADDRESSES["TRS80"]["PYRAMID_L1"]
update_command_names(info)
update_room_names(info)
update_objects(info)
update_room_scripts(info)
update_room_scripts(info)
update_general_script(info)

info = ADDRESSES["COCO"]["PYRAMID"]
update_command_names(info)
update_room_names(info)
update_objects(info)
update_room_scripts(info)
update_room_scripts(info)
update_general_script(info)

info = ADDRESSES["TRS80"]["HAUNTEDHOUSE1"]
update_command_names(info)
update_room_names(info)
update_objects(info)
update_room_scripts(info)
update_room_scripts(info)
update_general_script(info)

info = ADDRESSES["TRS80"]["HAUNTEDHOUSE2"]
update_command_names(info)
update_room_names(info)
update_objects(info)
update_room_scripts(info)
update_room_scripts(info)
update_general_script(info)
