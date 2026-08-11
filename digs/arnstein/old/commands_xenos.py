import binary_utils

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

COMMANDS = {
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
    0x24: ['exit_program',                   ],
    0x25: ['print_linefeed',                 ],
    0x26: ['print_score',                    ],
    0x27: ['load_game',                      ],
    0x28: ['save_game',                      ],
    0x29: ['toggle_var_open',                ],
    0x2A: ['toggle_var_lock',                ],
    0x2B: ['generate_random',                ],
    0x2C: ['set_active',                     'obj_num'],
    0x2D: ['is_var_object',                  'obj_num'],
    # Xenos only
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

ROUTINES = {
    0x81: 'PRINT_DOOR_HERE',
    0x80: 'PRINT_SHOTGUN_HERE',    
    0x8B: 'PRINT_PERIOD',
    0x8D: 'IS_CLOSED',
    0x8F: 'GET_OBJECT',
    0x90: 'PRINT_ERROR_CLIMB_ENTER',
    0x91: 'PRINT_USE_DIRECTIONS',
    0x92: 'PRINT_TRIED_BUT_COULDNT',
    0x94: 'INITIALIZE_GAME',  # Moves to HIGHWAY_WEST in section 1
    0x95: 'PRINT_TRAIL_MEANDERS',
    0x96: 'PRINT_VAST_CANYON',
    0x97: 'PRINT_CERTAIN_DEATH',
    0x98: 'PRINT_LAKE',
    0x99: 'DIE_CANYON_PLUNGE',
    0x9A: 'PRINT_CANYON_PREVENTS',
    0x9B: 'PRINT_EMPTY_HIGHWAY',
    0x9C: 'PRINT_AIRLOCK_TWO_BUTTONS',
    0x9D: 'PRINT_EXIT_YELLOW_BUTTON',
    0x9E: 'REMOVE_OVAL_FROM_ROOM',
    0x9F: 'OVAL_YELLOW_BUTTON',
    0xA0: 'OVAL_RED_BUTTON',
    0xA1: 'OVAL_BLUE_BUTTON',
    0xA2: 'PRINT_ALREADY_HAVE_THE_var',
    0xA3: 'PRINT_WELCOME_MESSAGE',  # Moves to HIGHWAY_WEST in section 1
    0xA5: 'IS_OPEN',
    0xA6: 'OPEN',
    0xA8: 'PRINT_noun1',
    0xA9: 'PRINT_noun2',
    0xAA: 'PRINT_THE_var',
    0xAB: 'PRINT_STILL_IN_DESERT',
    0xAC: 'HANDLE_ORANGE_BUTTON',
    0xAD: 'HANDLE_OVAL',
    0xAE: 'PRINT_PUSH_BUTTON',
    0xAF: 'PRINT_I_SEE_NO_noun1_HERE',
    0xB0: 'PRINT_AIRLOCK_THREE_BUTTONS',
    0xB1: 'PRINT_var_CONTAINS',
    0xB2: 'PRINT_ON_var_CAN_BE_SEEN',
    0xB3: 'PRINT_DISK_ERROR',
    0xB4: 'PRINT_AND',
    0xB5: 'PRINT_BY_YOUR_COMMAND',
    0xB6: 'PRINT_TWO_SAME_SPACE',
    0xB7: 'PRINT_HAVE_TO_OPEN_var',
    0xB8: 'PRINT_GARBAGE_GAMES',
    0xB9: 'PRINT_JUKEBOX',
    0xBA: 'OPEN_UNLOCK',
    0xBB: 'PRINT_LOOK_IN_AT',
    0xBC: 'SHOOT_DROP_SHELL',
    0xBD: 'PRINT_SHAGGY_CREATURE',
    0xBE: 'PRINT_FORCE_FIELD',
    0xBF: 'IS_LIQUID_REACHABLE',
    0xC0: 'ARE_NOUNS_GIVEN',
    0xC1: 'PRINT_CANT_REACH_var',
    0xC2: 'PRINT_CANT_BUDGE_noun1',
    0xC3: 'IS_PLAYER_LACKING_WISDOM',
    0xC4: 'IS_PHRASE_AN_AFFECT',
    0xC5: 'ENTER_CLIMB_OUT',
    0xC6: 'PROMPT_FOR_DRIVE_NUMBER',
    0xC7: 'IS_OBJECT_RIBULN',
    0xC8: 'BACK_TO_TOWN',
    0xC9: 'PRINT_COMPLETED_PERCENT', 
    0xCA: 'DIE_ENERGY_BEAM',
}

EXT_ATTRIBUTES = {
    0x80: 'Glass',
    0x40: 'Locked',
    0x20: 'Closed',
    0x10: 'liQuid'
}

ATTRIBUTES = {
    0x80: '??',
    0x40: 'Weapon',
    0x20: 'Portable',
    0x10: 'Alive',
    0x08: 'Openable',
    0x04: 'Readable',
    0x02: 'Holder',
    0x01: 'Surface'
}


class Commands:
    def __init__(self):
        self.code_address = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/trs80/xenos/Code.md", 
            "7268:", 
            "72DE:")
    
    def get_command_name(self, num):
        if num in COMMANDS:
            return COMMANDS[num][0]
        else:
            return None
    
    def get_command_args(self, num):
        if num in COMMANDS:
            return COMMANDS[num][1:]
        else:
            return None
        
    def get_section_name(self, section):
        return f'SECTION_{section:02X}_{SECTIONS[section]}'

    def get_command_name(self, command):
        return f'COM_{command:02X}_{COMMANDS[command]}'

    def get_routine_name(self, routine):
        if routine not in ROUTINES:
            return f'FN_{routine:02X}_??'
        return f'FN_{routine:02X}_{ROUTINES[routine]}'
        
    def get_command_address(self, num):
        if num < len(self.code_address):
            return self.code_address[num]
        else:
            return None
        
    def get_ext_attribute_name(self, value):
        ret_bits = ''
        ret_words = []
        for bit, name in EXT_ATTRIBUTES.items():
            if value & bit:
                for p in name:
                    if p=='?' or p.isupper():
                        ret_bits += p
                        break
                ret_words.append(name)
            else:
                ret_bits += '.'
        return f'{ret_bits}----({",".join(ret_words)})'

    def get_attribute_name(self, value):
        # attributes=?QW.S...(liQuid, Weapon, Surface)
        ret_bits = ''
        ret_words = []
        for bit, name in ATTRIBUTES.items():
            if value & bit:
                for p in name:
                    if p=='?' or p.isupper():
                        ret_bits += p
                        break
                ret_words.append(name)
            else:
                ret_bits += '.'
        return f'{ret_bits}({",".join(ret_words)})'

if __name__ == "__main__":
    c = Commands()
