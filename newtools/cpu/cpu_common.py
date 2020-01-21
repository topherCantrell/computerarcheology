
'''
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


class Opcode():

    def __init__(self, info: dict):
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

    def get_mnemonic(self):
        return self._mnemonic

    def get_code(self):
        return self._code

    def get_bus(self):
        # TODO: maybe accessors like 'is_read'
        return self._bus


class CPU:

    cpu_singletons = {}

    def get_cpu(name: str):
        '''Get the CPU by name

        Args:
            name (str): The CPU's name
        Returns:
            CPU : The CPU object (or None)
        '''

        if name in CPU.cpu_singletons:
            return CPU.cpu_singletons[name]

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
            self._opcodes.append(opc)
            key = opc.get_code()[0]
            if not isinstance(key, int):
                raise CPUException('First code byte must be a number')
            if key in self._quick_codes:
                self._quick_codes[key].append(opc)
            else:
                self._quick_codes[key] = [opc]

    def make_opcode(self, info: dict)->Opcode:
        '''Create an opcode from the given info.

        This is a method to allow for overrides

        Args:
            info (dict): the opcode information
        Returns:
            Opcode: factoried opcode
        '''

        return Opcode(info)

    def find_opcodes_for_binary(self, binary: list, start: int=0, exact: bool=False)->list:
        '''Find the opcode that matches the binary (a disassembly operation)

        Args:
            binary (list[int]): the bytes to disassemble
            start (int): starting point in the bytes [default is 0]
            exact (bool): True if the opcode must match the given bytes exactly [default is False]
        Returns:
            list[Opcode]: The opcodes information (TODO: maybe an object?)
        '''

        possible = self._quick_codes[binary[0]]

        ret = []

        for oc in possible:
            code = oc.get_code()
            pos = 0
            could_be = True
            for b in range(len(code)):
                if b >= len(binary) + start:
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
