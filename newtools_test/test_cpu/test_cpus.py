import unittest

import cpu.cpu_common


class Test_CPUs(unittest.TestCase):

    def test_get_by_name(self):

        cp = cpu.cpu_common.CPU.get_cpu('6502')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('6803')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('6809')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('8052')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('DVG')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('Z80')
        self.assertTrue(cp != None)

        cp = cpu.cpu_common.CPU.get_cpu('Z80GB')
        self.assertTrue(cp != None)
