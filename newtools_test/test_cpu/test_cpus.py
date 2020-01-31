import unittest

import cpu.cpu_manager


class Test_CPUs(unittest.TestCase):

    def test_get_by_name(self):

        cp = cpu.cpu_manager.get_cpu_by_name('6502')
        self.assertTrue(cp != None)

        cp = cpu.cpu_manager.get_cpu_by_name('6803')
        self.assertTrue(cp != None)

        cp = cpu.cpu_manager.get_cpu_by_name('6809')
        self.assertTrue(cp != None)

        cp = cpu.cpu_manager.get_cpu_by_name('8052')
        self.assertTrue(cp != None)

        cp = cpu.cpu_manager.get_cpu_by_name('DVG')
        self.assertTrue(cp != None)

        #cp = cpu.cpu_manager.get_cpu_by_name('Z80')
        #self.assertTrue(cp != None)

        #cp = cpu.cpu_manager.get_cpu_by_name('Z80GB')
        #self.assertTrue(cp != None)
        
    def opcode_fillin_sanity(self,cp):        
        for op in cp._opcodes:
            lets = []
            for c in op.code:
                if isinstance(c,str):
                    if not c[0] in lets:
                        lets.append(c[0])
            bs = op.use                
            if not lets:
                #print("##",lets,'##',bs,'##',op.mnemonic)
                self.assertTrue(bs=={})
                continue                
            self.assertTrue(len(lets),len(bs))
            for let in lets:
                #print('##',let,'##',bs)
                self.assertTrue(let in bs)
                
    def test_opcode_sanity(self):
        cp = cpu.cpu_manager.get_cpu_by_name('6502')
        self.opcode_fillin_sanity(cp)
        cp = cpu.cpu_manager.get_cpu_by_name('6803')
        self.opcode_fillin_sanity(cp)
        cp = cpu.cpu_manager.get_cpu_by_name('6809')
        self.opcode_fillin_sanity(cp)
        cp = cpu.cpu_manager.get_cpu_by_name('8052')
        self.opcode_fillin_sanity(cp)
        cp = cpu.cpu_manager.get_cpu_by_name('DVG')
        self.opcode_fillin_sanity(cp)
        
        

    """
    def test_disassembly(self):

        cp = cpu.cpu_manager.get_cpu_by_name('6809')
        opc = cp.find_opcodes_for_binary([0x10, 0xA3, 0x9D, 1, 2])
        self.assertTrue(len(opc) == 1)
        self.assertTrue(opc[0].mnemonic == 'CMPD [k,PC]')

    def test_binary_to_string(self):

        cp = cpu.cpu_manager.get_cpu_by_name('6809')

        binary = [0x10, 0xA3, 0x9D, 1, 2]
        opc = cp.find_opcodes_for_binary(binary)[0]

        fills = cp.get_mnemonic_fills(opc, 0x1000, binary)
        out = cp.binary_to_string(opc, 0x1000, binary, fills)

    def test_one_byte_relative(self):

        cp = cpu.cpu_manager.get_cpu_by_name('6809')
        binary = [0x26, 0xF9]
        opc = cp.find_opcodes_for_binary(binary)[0]
        fills = cp.get_mnemonic_fills(opc, 0xC050, binary)

        out = cp.binary_to_string(opc, 0xC050, binary, fills)    

    def test_two_byte_relative(self):

        cp = cpu.cpu_manager.get_cpu_by_name('6809')
        binary = [0x10, 0x26, 0xDE, 0xAF]
        opc = cp.find_opcodes_for_binary(binary)[0]
        fills = cp.get_mnemonic_fills(opc, 0xC174, binary)

        out = cp.binary_to_string(opc, 0xC174, binary, fills)
    """

