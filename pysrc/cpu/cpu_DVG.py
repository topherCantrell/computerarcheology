OPCODES = [
    {"mnem": "VEC SCALE=0, BRI=b, X=x, Y=y",
        "code": "0000_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx", "bus": ""},
    {"mnem": "VEC SCALE=1, BRI=b, X=x, Y=y",
        "code": "0001_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx", "bus": ""},
    {"mnem": "VEC SCALE=2, BRI=b, X=x, Y=y",
        "code": "0010_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx", "bus": ""},
    {"mnem": "VEC SCALE=3, BRI=b, X=x, Y=y",
        "code": "0011_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx", "bus": ""},
    {"mnem": "VEC SCALE=4, BRI=b, X=x, Y=y",
        "code": "0100_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx", "bus": ""},
    {"mnem": "VEC SCALE=5, BRI=b, X=x, Y=y",
        "code": "0101_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx", "bus": ""},
    {"mnem": "VEC SCALE=6, BRI=b, X=x, Y=y",
        "code": "0110_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx", "bus": ""},
    {"mnem": "VEC SCALE=7, BRI=b, X=x, Y=y",
        "code": "0111_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx", "bus": ""},
    {"mnem": "VEC SCALE=8, BRI=b, X=x, Y=y",
        "code": "1000_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx", "bus": ""},
    {"mnem": "VEC SCALE=9, BRI=b, X=x, Y=y",
        "code": "1001_0yyy_yyyy_yyyy bbbb_0xxx_xxxx_xxxx", "bus": ""},

    {"mnem": "CUR SCALE=s, X=t, Y=u",
        "code": "1010_00yy_yyyy_yyyy ssss_00xx_xxxx_xxxx", "bus": ""},

    {"mnem": "HALT",                          "code": "1011_0000_0000_0000", "bus": ""},

    {"mnem": "JSR a",                         "code": "1100_aaaa_aaaa_aaaa", "bus": "x"},

    {"mnem": "RTS",                           "code": "1101_0000_bbbb_bbbb", "bus": "x"},

    {"mnem": "JMP a",                         "code": "1110_aaaa_aaaa_aaaa", "bus": "x"},

    {"mnem": "SVEC SCALE=c, BRI=b, X=d, Y=e", "code": "1111_geee_bbbb_hxxx",
        "details": "h is upper bit of c, g is lower bit", "bus": ""}
]

import cpu.cpu_common


class CPU_DVG(cpu.cpu_common.CPU):

    def __init__(self):
        self._opcodes = []

        for entry in OPCODES:
            entry['code'] = entry['code'].replace('_', '').replace(' ', '')
            # Note that these are BIT fields ... not BYTE fields like other
            # CPUs
            self._opcodes.append(entry)

        self._make_data_map()

    def is_memory_reference(self, op):
        return (op['mnem'].startswith('JSR') or op['mnem'].startswith('JMP'))

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
        for op in self._opcodes:
            if self._does_op_fit(g, op['code']):
                ret.append(op)
        return ret


SINGLETON = CPU_DVG()


def get_cpu():
    return SINGLETON
