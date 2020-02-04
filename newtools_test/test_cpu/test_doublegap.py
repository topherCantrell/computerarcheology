import unittest

import assembler.asm


class Test_Assembly(unittest.TestCase):

    def test_assemble(self):
        
        asm = assembler.asm.Assembler('DoubleGap.asm')
        
        asm.assemble()
        
        asm.write_listing('test.lst')