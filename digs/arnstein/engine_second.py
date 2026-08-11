SECTIONS = {
    0x01: 'ADJECTIVES',
    0x02: 'SHORT_NAME',
    0x03: 'DESCRIPTION',
    0x04: 'COMMANDS',
    0x06: 'IF_SECOND_NOUN',
    0x07: 'IF_FIRST_NOUN',
    0x08: 'EVERY_TURN',
    0x09: 'HIT_POINTS',
    0x0A: 'UPON_DEATH',
    0x0B: 'IF_GIVEN_COMMAND',
    0x0C: 'WEIGHT',   
}

COMMANDS_RAAKATU = {
    0x00: ['move_and_look',                  'room_num'],
    0x01: ['is_in_pack_or_room',             'obj_num'],
    0x02: ['is_owned_by',                    'obj_num'],
    0x03: ['is_located',                     'room_num','obj_num'],
    0x04: ['print',                          '...'],
    0x05: ['is_leq_last_random',             'value'],
    0x06: ['print_inventory',                ],
    0x07: ['print_room_description',         ],
    0x08: ['is_noun1',                       'obj_num'],
    0x09: ['is_noun2',                       'obj_num'],
    0x0A: ['is_input_phrase',                'phrase_num'],
    0x0B: ['switch',                         'num', '...'],
    0x0C: ['fail',                           ],
    0x0D: ['group_AND',                      '...'],
    0x0E: ['group_OR',                       '...'],
    0x0F: ['pick_up_var_object',             ],
    0x10: ['drop_var_object',                ],
    0x11: ['print_noun1',                    ],
    0x12: ['print_noun2',                    ],
    0x13: ['process_phrase_by_room',         ],
    0x14: ['reverse_status',                 '...'],
    0x15: ['is_var_attributes',              'bits'],
    0x16: ['print_var',                      ],
    0x17: ['move_object_to',                 'obj_num','destination'],
    0x18: ['is_var_owned_by_active',         ],
    0x19: ['move_to_room',                   'room_num'],
    0x1A: ['set_var_to_noun1',               ],
    0x1B: ['set_var_to_noun2',               ],
    0x1C: ['set_var_object',                 'obj_num'],
    0x1D: ['attack_var',                     'value'],
    0x1E: ['swap_object_locations',          'obj_num1','obj_num2'],
    0x1F: ['print2',                         '...'],
    0x20: ['is_active_object',               'obj_num'],
    0x21: ['execute_phrase',                 'phrase_num','obj_num1','obj_num2'],
    0x22: ['is_less_equal_health',           'value'],
    0x23: ['heal_var',                       'value'],
    0x24: ['end_program',                    ],
    0x25: ['print_linefeed',                 ],
    0x26: ['print_score',                    ],
    0x27: ['load_game',                      ],
    0x28: ['save_game',                      ],
}

COMMANDS_BEDLAM = COMMANDS_RAAKATU | {
    0x29: ['toggle_var_open',                ],
    0x2A: ['toggle_var_lock',                ],
    0x2B: ['generate_random',                ],
    0x2C: ['set_active',                     'obj_num'],
    0x2D: ['is_var_object',                  'obj_num'],
}

COMMANDS_XENOS = COMMANDS_BEDLAM | {
    0x2E: ['is_var_ext_attributes',          'bits'],
    0x2F: ['load_section_from_disk',         'section_num'],
    0x30: ['set_current_room',               'room_num'],
    0x31: ['put_noun2_in_var_object',        ],
    0x32: ['put_noun1_in_var_object',        ],
    0x33: ['print_objects_on_var_object',    ],
    0x34: ['save_system_objects_to_disk',    ],
    0x35: ['load_system_objects_from_disk',  ],
    0x36: ['is_in_room_or_open_container',   'obj_num'],
    0x37: ['is_player_in_any_object',        ],
    0x38: ['bump_score',                     ],
    0x39: ['is_weight_70_or_less',           ],
    0x3A: ['clear_screen',                   ],
    0x3B: ['wait_for_key_123',               ],
}


ADDRESSES = {
    "TRS80": {        
        "RAAKATU": {
            "File": "/git/ComputerArcheology/content/trs80/raakatu/code.md",
            "ScriptCommands": (0x5066, 0x50B8),
            "PhraseList": (0x50B9, 0x52C1),
            "WordTable": (0x52C3, 0x5650),
            "ObjectData": (0x5651, 0x680F),
            "RoomScripts": (0x681F, 0x73FA),
            "GeneralScript": (0x73FB, 0x7BCB),
            "Subroutines": (0x7BCD, 0x7F9C),
        },
        "BEDLAM": {
            "File": "/git/ComputerArcheology/content/trs80/bedlam/code.md",
        },
        "XENOS": {
            "File": "/git/ComputerArcheology/content/trs80/xenos/code.md",
        }
    }, 
    "COCO": {        
        "RAAKATU": {
            "File": "/git/ComputerArcheology/content/coco/raakatu/code.md",
        },
        "BEDLAM": {
            "File": "/git/ComputerArcheology/content/coco/bedlam/code.md",
        }
    }
}

def read_code_file(file_name):
    ret = []
    with open(file_name, "r") as f:
        for line in f:
            ret.append(line.strip())
    return ret

def write_code_file(file_name, code):
    # Please, please, please use github to back this up first
    with open(file_name, "w") as f:
        for line in code:
            f.write(line + "\n")

def read_command_table(file_path, start_addr, end_addr, little_endian=False):
    ret = []
    with open(file_path, "r") as f:            
        g = ''
        while not g.startswith(start_addr):
            g = f.readline()
        g = g.strip()
        while True: # not g.startswith(end_addr):
            if not g: # Stop on blank lines too
                break
            if len(g)>4 and g[4] == ':':
                if little_endian:
                    addr = int(g[6:8] + g[9:11], 16)
                else:
                    addr = int(g[9:11] + g[6:8], 16)
                ret.append(addr)
                print(f'addr: {addr:04X}')    
                # Up to and including the end address
                if g.startswith(end_addr):
                    print('-----FOUND ',len(ret))
                    print('')
                    break        
            g = f.readline()
            g = g.strip()
    return ret

info = ADDRESSES["TRS80"]["PYRAMID_L1"]
code = read_code_file(info["File"])

ps = 0
while not code[ps].startswith(f'{info["ScriptCommands"][0]:04X}:'):
    ps += 1
pe = ps
while not code[pe].startswith(f'{info["ScriptCommands"][1]:04X}:'):
    pe += 1
pe += 1

command_table = []

cn = 1
x = ps
y = pe
while x < y:
    line = code[x]    
    if len(line) > 4 and line[4] == ':':
        addr = int(line[9:11] + line[6:8], 16)        
        command_table.append(addr)
        if addr:
            line = f'{line[:11]}        ; COM _{cn:02X}_{info["Commands"][cn][0]}({", ".join(info["Commands"][cn][1:])})'
            print(">>>",line)
        cn += 1
    x += 1
print(code[ps:pe])

