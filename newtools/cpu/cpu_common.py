from cpu.opcode import Opcode

'''
  
  Most opcodes contain at most one fill-in, like "LDA #b" or "JSR r". These will have one bus
  description. Some have multiple like "MOV p,q". For these cases, the "bus" field is 
  formated as "p:w,q:r,etc"

  p - memory address (one byte)
  q - memory address (one byte) used for opcodes with multiple Ps
  t - memory address (two bytes)
  b - constant (one byte)
  w - constant (two byte)  
  r - memory branch relative offset (one byte)  
  s - memory branch relative offset (two byte)  
  
  The "bus" field shows how a memory address (p, q, t, r, s) is used:
  - "" mnemonic does not contain a memory address
  - "r" memory address is read
  - "w" memory address is written
  - "rw" memory address is read and written
  - "x" memory address is code (jump destination)
  
  * 6809 specific
  y - indexed form (6809)
  z - two register set (6809)
  x - push register set S (6809)
  y - pull register set S (6809)
  u - push register set U (6809)
  v - pull register set U (6809)
  
  * 8051 specific
  z - bit address (one byte)
  y - 11-bit address (one byte -- 3 bits in the opcode)  
  
  Two uses:
    - Assembly (text to code)
    - Disassembly (code to text)

'''


class CPUException(Exception):
    pass


class CPU:

    cpu_singletons = {}

    @staticmethod
    def get_cpu(name: str):
        '''Get the CPU singleton by name

        Args:
            name (str): The CPU's name
        Returns:
            CPU : The CPU object (or None)
        '''

        if name in CPU.cpu_singletons:
            return CPU.cpu_singletons[name]

        # Delayed imports ... only for the processors we need

        cp = None
        if name == '6502':
            import cpu.cpu_6502
            cp = cpu.cpu_6502.CPU_6502()
        elif name == '6803':
            import cpu.cpu_6803
            cp = cpu.cpu_6803.CPU_6803()
        elif name == '6809':
            import cpu.cpu_6809
            cp = cpu.cpu_6809.CPU_6809()
        elif name == '8052':
            import cpu.cpu_8052
            cp = cpu.cpu_8052.CPU_8052()
        elif name == 'DVG':
            import cpu.cpu_DVG
            cp = cpu.cpu_DVG.CPU_DVG()
        elif name == 'Z80':
            import cpu.cpu_Z80
            cp = cpu.cpu_Z80.CPU_Z80()
        elif name == 'Z80GB':
            import cpu.cpu_Z80GB
            cp = cpu.cpu_Z80GB.CPU_Z80GB()

        if cp:
            CPU.cpu_singletons[name] = cp

        return cp

    #

    def __init__(self, opcodes: list):
        self._opcodes = []
        self._opcodes_info = opcodes
        self._quick_codes = {}
        for op in opcodes:
            opc = self.make_opcode(op)
            opc._cpu = self
            self._opcodes.append(opc)
            key = opc.code[0]
            if not isinstance(key, int):
                raise CPUException('First code byte must be a number')
            if key in self._quick_codes:
                self._quick_codes[key].append(opc)
            else:
                self._quick_codes[key] = [opc]

            # Show opcodes with more than 1 fill-in
            #letters = []
            # for d in opc.code():
            #    if isinstance(d,str):
            #        if not d[0] in letters:
            #            letters.append(d[0])
            # if len(letters)>1:
            #    print(opc.get_mnemonic())

    def make_opcode(self, info: dict)->Opcode:
        '''Create an opcode from the given info.

        This is a factory method to allow for overrides

        Args:
            info (dict): the opcode information
        Returns:
            Opcode: factoried opcode
        '''
        return Opcode(info)

    def get_field_spacing(self):
        '''Return the field spacing for disassembly

        Returns:
            dict: spacing for parts of disassembly
        '''
        return {
            'address_size': 4,  # Number of digits
            'data': 16,  # Spacing reserved for the data section
            'mnemonic': [8, 20]  # Spacing for each part of the mnemonic
        }

    def binary_to_string(self, opcode: Opcode, address: int, binary: list, fills: dict):
        '''Make a disassembly string from the given info

        Args:
            opcode (Opcode): the opcode
            address (int): the address of the opcode
            binary (list): the opcode data
            fills (dict): the opcode fill-in information

        Returns:
            The complete disassembly string        
        '''

        # Spacing for the disassembly fields
        spa = self.get_field_spacing()

        # Address
        fs = '{:0' + str(spa['address_size']) + 'X}'
        add = fs.format(address)

        # Data
        ds = ''
        for i in range(len(binary)):
            ds = ds + '{:02X} '.format(binary[i])
        ds = ds.ljust(spa['data'], ' ')

        # Multi-word mnemonic spacing
        # TODO: use however many words are in the array ... or just the one if it isn't an array
        mn = opcode.mnemonic
        i = mn.find(' ')
        if i >= 0:
            a = mn[0:i]
            b = mn[i + 1:]
            mn = a.ljust(spa['mnemonic'][0]) + b.ljust(spa['mnemonic'][1])
        else:
            mn = mn.ljust(spa['mnemonic'][0] + spa['mnemonic'][1])

        # Build the basic form
        base = f'{add}: {ds}{mn}'

        for f in fills:
            fill_info = fills[f]
            i = base.find(f)
            if i >= 0:
                # TODO: visible spacing
                base = base.replace(f, fill_info['sub_value'])

        return base

    def _binary_to_string_fill(self, address: int, binary: list, opcode: Opcode, fills: dict, ind: int):
        '''Fill in an opcode data value

        Different processors might override this for their own special needs. The 
        "binary_to_string" defers to this method.

        Entries are added to fills for example:
            'p' : {
                'sub_value' : '$1024', # The actual value (string)
                'visual_size' : 5      # Number of printed characters in sub (might include HTML)
                'numeric_value' : 0    # Actual numeric value 
            }

        Args:
            address (int): the address of the opcode
            binary (list): the binary data for the opcode
            opcode (Opcode): the Opcode
            fills (dict): dictionary of fill-in values (add to this)            
            ind (int): bytes index of the fill-in (binary and opcode)

        '''
        # Find/make the fill-in entry
        spec = opcode.code[ind]
        if spec[0] not in fills:
            fills[spec[0]] = {'sub_value': '$00', 'visual_size': 3, 'numeric_value': 0}
            entry = fills[spec[0]]
        else:
            entry = fills[spec[0]]

        ov = entry['numeric_value']

        # New numeric value
        val = binary[ind]
        if spec[1] == 'm':
            val = val * 256
            entry['visual_size'] = 5
        val += ov
        entry['numeric_value'] = val

        # New substitution string
        fs = '${:0' + str(entry['visual_size'] - 1) + 'X}'

        if spec[0] == 'r':
            # One byte relative (from start of next instruction)
            fa = address + len(opcode.code)
            fa = fa + (val - 256)
            entry['relative_target'] = fa
            val = fa
        elif spec[0] == 's':
            # Two byte relative (from start of next instruction)
            fa = address + len(opcode.code)
            fa = fa + (val - 65536)
            entry['relative_target'] = fa
            val = fa

        entry['sub_value'] = fs.format(val)

    def get_mnemonic_fills(self, opcode: Opcode, address: int, binary: list):
        '''Get all the fill-in information for a given opcode

        Args:
            opcode (Opcode): the opcode
            address (int): the address of the opcode
            binary (list): the binary data for the opcode

        Returns:
            dict: all the fill ins
        '''

        code = opcode.code
        fills = {}
        for i in range(len(binary)):
            g = code[i]
            if isinstance(g, str):
                # Call out to the specific CPU in case it has specials
                self._binary_to_string_fill(address, binary, opcode, fills, i)

        return fills

    def find_opcodes_for_binary(self, binary: list, start: int=0, end: int=-1, exact: bool=False)->list:
        '''Find the opcodes that matches the binary (a disassembly operation)

        Args:
            binary (list[int]): the bytes to disassemble
            start (int): starting point in the bytes [default is 0]
            exact (bool): True if the opcode must match the given bytes exactly [default is False]
        Returns:
            list[Opcode]: The opcodes information 
        '''

        if end < 0:
            end = len(binary)

        possible = self._quick_codes[binary[0]]

        ret = []

        for oc in possible:
            if exact and len(oc.code) != (end - start):
                continue
            code = oc.code
            could_be = True
            for b in range(len(code)):
                if b >= end + start:
                    could_be = False
                    break
                if isinstance(code[b], str):
                    # Matches anything
                    continue
                if code[b] != binary[start + b]:
                    could_be = False
                    break
            if could_be:
                ret.append(oc)

        return ret
