import unittest

import assembler.asm

import cpu.cpu_manager


class Test_Assembly(unittest.TestCase):

    def test_8052_simple(self):
        cp = cpu.cpu_manager.get_cpu_by_name('8052')
        cp.init_assembly()
        
        asm = assembler.asm.Assembler('test8052.asm')
                
        g = cp.find_opcode_for_text(asm.code[2]['text'],asm)
        self.assertTrue(g.mnemonic == 'JMP @A+DPTR')
        print(g.mnemonic)
    
    def test_8052_simple_2(self):
        cp = cpu.cpu_manager.get_cpu_by_name('8052')
        cp.init_assembly()
        
        asm = assembler.asm.Assembler('test8052.asm')
                
        g = cp.find_opcode_for_text(asm.code[3]['text'],asm)
        self.assertTrue(g.mnemonic == 'MOV A,#b')
    
    def test_6809_mode_1(self):
        cp = cpu.cpu_manager.get_cpu_by_name('6809')
        cp.init_assembly()
        
        asm = assembler.asm.Assembler('test6809.asm')
                
        g = cp.find_opcode_for_text(asm.code[2]['text'],asm)