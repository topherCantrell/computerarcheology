import binary_utils

from commands_xenos import COMMANDS as COMMANDS_XENOS


COMMANDS = {}

ROUTINES = {
    0x81: 'RESET_GAME',
    0x82: 'DEATH_BY_STATUE',
    0x83: 'MANIPULATE',
    0x84: 'PRINT_PERIOD',
    0x85: 'PRINT_GUARDS_MARCH_RIGHT',
    0x86: 'PRINT_GUARDS_AROUND_CORNER',
    0x87: 'PRINT_GUARDS_DISAPPEAR_LEFT',
    0x88: 'PRINT_THE_NOUN_IS_NOT_BURNING',
    0x89: 'PRINT_CANT_JUMP_THAT_FAR',
    0x8A: 'DEATH_BY_RUG_SPIKE',
    0x8B: 'DEATH_BY_HIDDEN_RUG_SPIKE',
    0x8C: 'PRINT_DISCOVER_PIT',
    0x8D: 'PRINT_STATUE_TOO_HEAVY',
    0x8E: 'PRINT_MOVE_ALTER',
    0x8F: 'ENTER_SECRET_PASSAGE', 
    0x90: 'PRINT_ALTER_MOVES_BACK',    
    0x91: 'SEAL_UP_HOLE',
    0x92: 'PRINT_SCORE',
    0x93: 'INVALID_CLIMB_IN_OR_OUT',
    0x94: 'PRINT_USE_DIRECTIONS',
    0x95: 'RESET_DUNGEON',    
}

class Commands:
    def __init__(self):
         # Nothing after 0x28 and different 0x24 and 0x25
        for i in range(0x00,0x28):
            COMMANDS[i] = COMMANDS_XENOS[i]
        COMMANDS[0x24] = ['endless_loop']  # Just an endless loop (no return to BASIC)
        self.code_address_trs80 = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/trs80/raakatu/Code.md", 
            "5066:", 
            "50B6:")
        self.code_address_coco = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/coco/raakatu/Code.md", 
            "12E5:", 
            "1331:", little_endian=True)
    
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