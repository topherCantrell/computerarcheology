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
memory = Memory(cfg)
cpu = CPU(memory, cfg)

cpu.run()