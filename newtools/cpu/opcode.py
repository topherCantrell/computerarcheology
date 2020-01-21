class Opcode():

    def __init__(self, info: dict):
        self._cpu = None
        self._info = info
        self._mnemonic = info['mnem']
        self._bus = info['bus']
        self._code = []
        code = info['code']
        for i in range(0, len(code), 2):
            frag = code[i:i + 2]
            if frag.islower():
                self._code.append(frag)
            else:
                self._code.append(int(frag, 16))

    def get_field_spacing(self):
        return {
            'data': 16,
            'mnemonic': [8, 20]
        }

    def get_mnemonic(self):
        return self._mnemonic

    def get_code(self):
        return self._code

    def get_bus(self):
        # TODO: maybe accessors like 'is_read'
        return self._bus

    def binary_to_string(self, address: int, binary: list):
        # For example [0x10, 0xA3, 0x9D, 1, 2]
        # 1000: 10 A3 9D 01 02      CMPD   [$0102,PC]

        spa = self.get_field_spacing()

        add = '{:04X}'.format(address)

        ds = ''
        for d in binary:
            ds = ds + '{:02X} '.format(d)

        ds = ds.ljust(spa['data'], ' ')

        return f'{add}: {ds}'
