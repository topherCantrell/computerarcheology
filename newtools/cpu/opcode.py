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

        # Spacing for the disassembly fields
        spa = self.get_field_spacing()

        # Address
        add = '{:04X}'.format(address)

        # Data
        ds = ''
        for i in range(len(binary)):
            ds = ds + '{:02X} '.format(binary[i])
        ds = ds.ljust(spa['data'], ' ')

        # All the fill ins
        fills = {}
        tbs = []
        for i in range(len(binary)):
            g = self._code[i]
            if isinstance(g, str):
                # Call out to the specific CPU in case it has specials
                self._cpu._binary_to_string_fill(address, binary, self, fills, tbs, i)

        # Fill in the mnemonic
        mn = self.get_mnemonic()
        for f in fills:
            if f in tbs:
                # Numeric fill ins
                if isinstance(tbs[f], int):
                    nv = '${:04X}'.format(fills[f])
                else:
                    nv = '${:02X}'.format(fills[f])
            else:
                # String fill ins
                nv = tbs[f]
            mn = mn.replace(f, nv)

        # Two-word mnemonic spacing
        i = mn.find(' ')
        if i >= 0:
            a = mn[0:i]
            b = mn[i + 1:]
            mn = a.ljust(spa['mnemonic'][0]) + b.ljust(spa['mnemonic'][1])
        else:
            mn = mn.ljust(spa['mnemonic'][0] + spa['mnemonic'][1])

        # We need location information to replace with links, etc

        # TODO:How about things like this: 'DJNZ $102,$200' where the first is data and the second code

        # Final form
        return f'{add}: {ds}{mn}'
