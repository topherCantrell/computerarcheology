import binary_utils

COMMANDS = {
0x01:     ['move_look',                          'room_num'],
0x02:     ['is_in_pack',                         'obj_num'],
0x03:     ['is_in_pack_or_current_room',         'obj_num'],
0x04:     ['print','ps_num'                      ],
0x05:     ['death_and_resurrect'                 ],
0x06:     None,
0x07:     ['stop_if_pass'                        ],
0x08:     ['print_score'                         ],
0x09:     ['print_score_and_endless_loop'        ],
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

class Commands:
    def __init__(self):
        self.code_address_trs80_lv2 = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/trs80/pyramid/Code.md", 
            "509F:", 
            "50D7:")
        self.code_address_trs80_lv1 = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/trs80/pyramid/Code1.md", 
            "503C:", 
            "5074:")
        self.code_address_coco = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/coco/pyramid/Code.md", 
            "0A17:", 
            "0A4F:", little_endian=True)
    
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
        
    def get_command_address_trs80_lv1(self, num):
        if num < len(self.code_address_trs80_lv1):
            return self.code_address_trs80_lv1[num]
        else:
            return None
    
    def get_command_address_trs80_lv2(self, num):
        if num < len(self.code_address_trs80_lv2):
            return self.code_address_trs80_lv2[num]
        else:
            return None
    
    def get_command_address_coco(self, num):
        if num < len(self.code_address_coco):
            return self.code_address_coco[num]
        else:
            return None

if __name__ == "__main__":
    c = Commands()