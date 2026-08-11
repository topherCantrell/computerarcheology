import binary_utils
from commands_pyramid import COMMANDS as COMMANDS_PYRAMID

COMMANDS = {}


class Commands:
    def __init__(self):
        # Only a few commands from Pyramid
        COMMANDS[0x01] = COMMANDS_PYRAMID[0x01]
        COMMANDS[0x02] = COMMANDS_PYRAMID[0x02]
        COMMANDS[0x03] = COMMANDS_PYRAMID[0x03]
        COMMANDS[0x04] = COMMANDS_PYRAMID[0x04]
        COMMANDS[0x05] = COMMANDS_PYRAMID[0x10]
        COMMANDS[0x06] = COMMANDS_PYRAMID[0x07]
        COMMANDS[0x07] = COMMANDS_PYRAMID[0x09]
        COMMANDS[0x08] = COMMANDS_PYRAMID[0x0B]
        COMMANDS[0x09] = COMMANDS_PYRAMID[0x0F]
        COMMANDS[0x0A] = COMMANDS_PYRAMID[0x11]
        COMMANDS[0x0B] = COMMANDS_PYRAMID[0x12]
        COMMANDS[0x0C] = COMMANDS_PYRAMID[0x14]
        COMMANDS[0x0D] = COMMANDS_PYRAMID[0x15]
        COMMANDS[0x0E] = COMMANDS_PYRAMID[0x16]
        COMMANDS[0x0F] = COMMANDS_PYRAMID[0x17]
        COMMANDS[0x10] = COMMANDS_PYRAMID[0x1A]
        # Just for Haunted House, not in Pyramid
        COMMANDS[0x11] = ['load_second_floor']

        self.code_address_trs80_house1 = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/trs80/hauntedhouse/Code1.md", 
            "48FD:", 
            "491D:")
        self.code_address_trs80_house2 = binary_utils.read_command_table(
            "d:/git/computerarcheology/content/trs80/hauntedhouse/Code2.md", 
            "494D:", 
            "496B:")        
    
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
        
    def get_command_address_trs80_house1(self, num):
        if num < len(self.code_address_trs80_house1):
            return self.code_address_trs80_house1[num]
        else:
            return None
    
    def get_command_address_trs80_house2(self, num):
        if num < len(self.code_address_trs80_house2):
            return self.code_address_trs80_house2[num]
        else:
            return None   
    

if __name__ == "__main__":
    c = Commands()