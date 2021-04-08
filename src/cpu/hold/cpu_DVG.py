import json
import os


class CPU_DVG:

    def __init__(self):

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DVG.js')) as f:
            data = json.load(f)

        self.opcodes = []
        self._data_map = {}

        for entry in data:
            entry['code'] = entry['code'].replace('_', '').replace(' ', '')
            # Note that this are BIT fields ... not BYTE fields like other CPUs
            self.opcodes.append(entry)

    def get_opcode(self, mnem):
        for entry in self.opcodes:
            if entry['mnem'] == mnem:
                return entry
        return None

    def get_alias(self, op):
        if 'alias' in op:
            return op['alias']
        else:
            return None

    def is_bus_x(self, op):
        return 'x' in op['bus']

    def is_bus_r(self, op):
        return 'r' in op['bus']

    def is_bus_w(self, op):
        return 'w' in op['bus']

    def is_bus_rw(self, op):
        return self.is_bus_r(op) and self.is_bus_w(op)

    def is_memory_reference(self, op):
        return (op['mnem'].startswith('JSR') or op['mnem'].startswith('JMP'))

    def _does_op_fit(self, g, t):
        if len(g) != len(t):
            return False
        for i in range(len(g)):
            if t[i].islower():
                continue
            if g[i] != t[i]:
                return False
        return True

    def pick_opcode_from_aliases(self, mnem, opcodes):
        for op in opcodes:
            if op['mnem'].startswith(mnem[0]):
                return op
        return None

    def get_opcode_from_data(self, data):
        ret = []
        g = ''
        if len(data) == 2:
            g = '{:08b}{:08b}'.format(data[1], data[0])
        elif len(data) == 4:
            g = '{:08b}{:08b}{:08b}{:08b}'.format(
                data[1], data[0], data[3], data[2])
        else:
            return None
        for op in self.opcodes:
            if self._does_op_fit(g, op['code']):
                ret.append(op)
        return ret
