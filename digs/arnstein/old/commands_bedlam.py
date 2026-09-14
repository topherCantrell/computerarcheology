import binary_utils

from commands_xenos import COMMANDS as COMMANDS_XENOS

ROUTINES = {
    0x81: 'PRINT_ANOTHER_PADDED_ROOM',
    0x82: 'PRINT_EAST_WEST_HALL',
    0x83: 'PRINT_NORTH_SOUTH_HALL',
    0x84: 'PRINT_SOUTH_WALL_GREEN_DOOR',
    0x85: 'PRINT_NORTH_WALL_RED_DOOR',
    0x86: 'PRINT_NORTH_WALL_GREEN_DOOR',
    0x87: 'PRINT_SOUTH_WALL_RED_DOOR',
    0x88: 'PRINT_EAST_WALL_BLUE_DOOR',
    0x89: 'PRINT_WEST_WALL_BLUE_DOOR',
    0x8A: 'PRINT_CLOSED',    
    0x8B: 'PRINT_PERIOD',
    0x8C: 'PRINT_THIS_IS_OR_YOU_ARE_IN',    
    0x8D: 'PRINT_OBJECT_IS_CLOSED',
    # 0x8E: '',
    0x8F: 'GET_OBJECT',
    0x90: 'CLIMB_USE_DIRECTIONS',
    0x91: 'PRINT_USE_DIRECTIONS',
    0x92: 'YOU_CANT_DO_THAT_TO_OBJECT',
    # 0x93: '',
    0x94: 'INITIALIZE_GAME',
    0x95: 'RANDOM_MOVE_AND_DROP',    
    0x96: 'PRINT_NAPOLEAN_INTRO',
    0x97: 'PRINT_NAPOLEAN',
    0x98: 'PRINT_PICASSO_INTRO',
    0x99: 'PRINT_PICASSO',
    0x9A: 'GIVE_COMMAND_TO_PERSON',
    0x9B: 'RANDOM_MOVE',
    0x9C: 'MOVE_HOUDINI_C',
    0x9D: 'PRINT_BLUE_PILL',
    0x9E: 'PRINT_OBJECT_ENTERS_ROOM',
    0x9F: 'PRINT_UNSHAVEN_MAN',     
    0xA0: 'PRINT_PILL_IN_HAMBURGER',
    0xA1: 'FEED_DOG_MEAT',
    0xA2: 'PRINT_ALREADY_HAVE_OBJECT',
    0xA3: 'AWAKEN_IN_ROOM',
    0xA4: 'PRINT_PICASSO_DOOR',
    0xA5: 'ATTEMPT_CLOSE',
    0xA6: 'ATTEMPT_OPEN',
    0xA7: 'ATTEMPT_UNLOCK',
    0xA8: 'PRINT_THE_FIRST_NOUN',
    0xA9: 'PRINT_THE_SECOND_NOUN',
    0xAA: 'PRINT_THE_VAR_NAME',
    0xAB: 'ATTACK_PERSON',
    0xAC: 'PRINT_VAR_IGNORES_COMMAND',
}

ATTRIBUTES = {
    # 0x80: '??',
    # 0x40: 'Weapon',
    # 0x20: 'Portable',
    # 0x10: 'Alive',
    # 0x08: 'Openable',
    # 0x04: 'Readable',
    # 0x02: 'Holder',
    # 0x01: 'Surface'
}

COMMANDS = {}

class Commands:
    def __init__(self):
        # Nothing after 0x2E and different 0x24 and 0x25
        for i in range(0x00,0x2E):
            COMMANDS[i] = COMMANDS_XENOS[i]
        COMMANDS[0x24] = ['endless_loop']  # Just an endless loop (no return to BASIC)
        self.code_address_trs80 = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/trs80/bedlam/Code.md", 
            "4FC8:", 
            "5022:")
        self.code_address_coco = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/coco/bedlam/Code.md", 
            "1357:", 
            "13B1:", little_endian=True)
    
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
        
    def get_command_address_trs80(self, num):
        if num < len(self.code_address_trs80):
            return self.code_address_trs80[num]
        else:
            return None
    
    def get_command_address_coco(self, num):
        if num < len(self.code_address_coco):
            return self.code_address_coco[num]
        else:
            return None

if __name__ == "__main__":
    c = Commands()
