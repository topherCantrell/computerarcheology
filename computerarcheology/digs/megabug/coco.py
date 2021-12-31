# https://pypi.org/project/MC6809/

from MC6809.components.cpu6809 import CPU
from MC6809.components.memory import Memory
from MC6809.core.configs import BaseConfig


CFG_DICT = {
    "verbosity":None,
    "trace":None,
}

class Config(BaseConfig):
    RAM_START = 0x0000
    RAM_END = 0x7FFF

    ROM_START = 0x8000
    ROM_END = 0xFFFF
       
cfg = Config(CFG_DICT)

# FF1C = FF00 = PIA0 A
# FF1E = FF02 = PIA0 B
# FF1D = FF01 = PIA0 cntrl A
# FF1F = FF03 = PIA0 cntrl B

# FF21 = PIA1 cntrl A 
# FF23 = PIA1 cntrl B
# FF20 = PIA A
# FF22 = PIA B

sam = [0] * 16

def get_sam_info():
    so = ''
    for n in sam:
        so = so + str(n)
    ret = {}
    ret['DISPLAY_MODE_CONTROL'] = int(so[0:3],2)
    ret['DISPLAY_OFFSET'] = int(so[3:10],2)
    ret['PAGE_1'] = int(so[10:11],2)
    ret['CPU_RATE'] = int(so[11:13],2)
    ret['MEMORY_SIZE'] = int(so[13:15],2)
    ret['MAP_TYPE'] = int(so[15:16],2)
    return ret

def write_PIA(cycles,b,addr,value):
    if addr>=0xFF00 and addr<=0xFF3F:
        addr = addr & 0xFFC3 #1111_1111_1100_0011   
    elif addr>=0xFFC0 and addr<=0xFFDF:   
        #print('Code at {:04X} wrote {:02X} to {:04X}'.format(b,value,addr))     
        addr = addr & 0x1F
        sam[addr>>1] = addr&1
        print(get_sam_info())
        #print('SAM {:02X} {:02X}'.format(addr>>2,addr&1))
        #so = ''
        #for n in sam:
        #    so = so + str(n)
        #print('SAM {}'.format(so))
    else:        
        print('Code at {:04X} wrote {:02X} to {:04X}'.format(b,value,addr))    
    
def read_PIA(cycles,b,addr):
    if addr>=0xFF00 and addr<=0xFF3F:
        addr = addr & 0xFFC3 #1111_1111_1100_0011
        return 0
    else:
        print('Code at {:04X} read {:02X}'.format(b,addr)) 
    

memory = Memory(cfg)
# The CoCo ROM will "accidentally" write to FFFF. Just ignore that as the hardware does.
memory.add_write_byte_callback(lambda a,b,c,d: 0,0xFFFF,0xFFFF)
memory.add_write_byte_callback(write_PIA,0xFF00,0xFFF0)
memory.add_read_byte_callback(read_PIA,0xFF00,0xFFF0)

with open('bas12.rom','rb') as f:
    basic_rom = f.read()
    memory.load(0xA000,basic_rom)
    memory.load(0xFFF0,basic_rom[-16:])
    
with open('extbas11.rom','rb') as f:
    ext_rom = f.read()
    memory.load(0x8000,ext_rom)
    

cpu = CPU(memory, cfg)
cpu.reset()

print(cpu.program_counter)

#print(memory.read_byte(0xFFFF ))
while True:
    cpu.run()
    cpu.irq()
    print(cpu.get_state())
