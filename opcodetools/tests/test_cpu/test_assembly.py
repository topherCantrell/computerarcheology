import os
import unittest

import opcodetools.assembler.assembler
import opcodetools.cpu.cpu_manager

TEST_DIR = os.path.dirname(__file__)


class Test_Assembly(unittest.TestCase):

    def test_6502_simple(self):
        cp = opcodetools.cpu.cpu_manager.get_cpu_by_name('6502')
        cp.init_assembly()

        asm = opcodetools.assembler.assembler.Assembler(TEST_DIR + '/test6502.asm')

        _g, _i = cp.find_opcode_for_text(asm.code[2]['text'], asm)
        # self.assertTrue(g.mnemonic == 'JMP @A+DPTR')
        # print(g.mnemonic,i)

    def test_8052_simple(self):
        cp = opcodetools.cpu.cpu_manager.get_cpu_by_name('8052')
        cp.init_assembly()

        asm = opcodetools.assembler.assembler.Assembler(TEST_DIR + '/test8052.asm')

        g, _i = cp.find_opcode_for_text(asm.code[2]['text'], asm)
        self.assertTrue(g.mnemonic == 'JMP @A+DPTR')

    def test_8052_simple_2(self):
        cp = opcodetools.cpu.cpu_manager.get_cpu_by_name('8052')
        cp.init_assembly()

        asm = opcodetools.assembler.assembler.Assembler(TEST_DIR + '/test8052.asm')

        g, _i = cp.find_opcode_for_text(asm.code[3]['text'], asm)
        self.assertTrue(g.mnemonic == 'MOV A,#b')

    def test_6809_mode_1(self):
        cp = opcodetools.cpu.cpu_manager.get_cpu_by_name('6809')
        cp.init_assembly()

        asm = opcodetools.assembler.assembler.Assembler(TEST_DIR + '/test6809.asm')

        g, _i = cp.find_opcode_for_text(asm.code[3]['text'], asm)
        self.assertTrue(g.mnemonic == 'LDA p')

        g, _i = cp.find_opcode_for_text(asm.code[4]['text'], asm)
        self.assertTrue(g.mnemonic == 'LDA t')

        asm.defines['_default_base_page'] = 'true'
        g, _i = cp.find_opcode_for_text(asm.code[5]['text'], asm)
        self.assertTrue(g.mnemonic == 'LDA p')

        asm.defines['_default_base_page'] = 'false'
        g, _i = cp.find_opcode_for_text(asm.code[5]['text'], asm)
        self.assertTrue(g.mnemonic == 'LDA t')
