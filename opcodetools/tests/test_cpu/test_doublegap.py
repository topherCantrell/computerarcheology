import os
import unittest

import opcodetools.assembler.assembler


TEST_DIR = os.path.dirname(__file__)


class Test_Assembly(unittest.TestCase):

    def test_assemble(self):

        asm = opcodetools.assembler.assembler.Assembler(TEST_DIR + '/DoubleGap.asm')

        asm.assemble()

        asm.write_listing('test.lst')
