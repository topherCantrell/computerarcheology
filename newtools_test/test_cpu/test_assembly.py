import unittest

import assembler.asm

import cpu.cpu_manager


class Test_Assembly(unittest.TestCase):

    def test_8052_simple(self):
        cp = cpu.cpu_manager.get_cpu_by_name('8052')
        
        asm = assembler.asm.Assembler('test8052.asm')
                
        g = cp.find_opcode_for_text(asm.code[2]['text'],asm)