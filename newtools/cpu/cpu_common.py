from cpu.opcode import Opcode

'''
 
  Example opcodes:
  
    DATA       MMNEMONIC     CPU   USE
    10 a0 a1 : JSR a         6502  (a=code)
    90 aa    : BCC a         6502  (a=code_pcr)
    21 aa    : AND (a,X)     6502  (a=ram)
    69 aa    : ADC #a        6502  (a=const)
    D3 aa    : OUT (a),A     Z80   (a=port_w)
    6C a0 a1 : JMP (a)       6502  (a=code)
    10 aa bb : JBC a,b       6502  (a=ram_bit,b=code)  
    85 bb aa : MOV a,b       6502  (a=ram,b=ram)
    
  The actual substitution letters don't matter (as long as they are lower-case). The letters map to byte
  positions in the opcode data.
  
  Multibyte substitutions list the order of the bytes. 0 is the least significant, 1 is next, and so on.
  A little-endian address would be: a0a1
  
  The "use" field describes how the substitutions are used:
    - const (an immediate constant)
    - ram   (address is a regular read/write memory access)
    - code  (address is a code destination for jumps)
    - port  (address is a port read/write memory access)
    
  Direction qualifiers include (direction often matters for I/O addresses):
    - _r  The address is read from
    - _w  The address is written to
    - _rw The adress is read and written back to

  The _pcr qualifier indicates the actual address is relative to the program counter.
   
  Some processors have their own substitution qualifiers.
  
  Qualifiers - 6809 specific
    _pair  Pair of registers
    _pshs  Register list (push to S)
    _puls  Register list (pull from S)
    _pshu  Register list (push to U)
    _pulu  Register list (pull from U)
  
  Qualifiers - 8051 specific  
    _bit  Bit address
    _11   11_bit address (3 bits in opcode)
 

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

    #
    #
    # Disassembly needs
    #
    #

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

    def binary_to_string_fill(self, address: int, binary: list, opcode: Opcode, fills: dict, ind: int):
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
                self.binary_to_string_fill(address, binary, opcode, fills, i)

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

    #
    #
    # Assembly needs
    #
    #

    def make_frags(self):
        '''Make opcode fragments for assembly

        The assembly processes needs the mnemonic broken up into fragments for matching.

        This method fills out the fragments for all opcodes. We assume that single lowercase
        letters represent things needing filled in.
        '''

        for op in self._opcodes:
            txt = op.mnemonic
            txt = self.remove_unneeded_whitespace(txt)
            op.frags = ['']
            for i in range(len(txt)):
                c = txt[i]
                if c.islower():
                    op.frags.append(c)
                    if i < (len(txt) - 1):
                        # More to go -- start a new string for the more
                        op.frags.append('')
                else:
                    op.frags[-1] = op.frags[-1] + c

    def is_space_needed(self, text: str, pos: int):
        '''Return true if the target character in the string is needed.

        Args:
            text (str): the string
            pos (int): position in the string
        Returns:
            boolean: True if the character is needed or False if not


        Only whitespace can be not-needed. Spaces between letters and numbers is always needed.
        The rest can go.
        '''
        if text[pos] != ' ':
            # Just in case
            return True
        if (text[pos - 1].isalpha() or text[pos - 1].isdigit()) and (text[pos + 1].isalpha() or text[pos + 1].isdigit()):
            return True
        return False

    def remove_unneeded_whitespace(self, text: str):
        '''Remove unneeded whitespace from a string

        Args:
            text (str): the string

        Returns:
            str: the processed string
        '''
        match = text
        while True:
            g = match.replace('  ', ' ')
            if g == match:
                break
            match = g
        nmatch = ''
        for i in range(len(match)):
            c = match[i]
            if self.is_space_needed(match, i):
                nmatch = nmatch + c
        return nmatch

    def find_opcode_for_text(self, text: str, assembler):
        '''Find the one opcode that matches this line of text

        Args:
            text (str): the line of code
            assembler (Assembler): contains any defines

        Returns:
            Opcode: the requested opcode (or None)
        '''

        # Addressing mode overrides
        if '>' in text:
            size_override = 2
            text = text.replace('>', '')
        elif '<' in text:
            size_override = 1
            text = text.replace('<', '')
        else:
            size_override = 0

        # Ignorable whitespace
        nmatch = self.remove_unneeded_whitespace(text)

        ret = []
        for op in self._opcodes:
            frags = op.frags
            if len(frags) == 1:
                if frags[0] == nmatch.upper():
                    ret.append([op, None])
            elif len(frags) == 2:
                if nmatch.upper().startswith(frags[0]) and len(nmatch) > len(frags[0]):
                    ret.append([op, nmatch[len(frags[0]):]])
            elif len(frags) == 3:
                if nmatch.upper().startswith(frags[0]) and nmatch.upper().endswith(frags[2]):
                    ret.append([op, nmatch[len(frags[0]):-len(frags[2])]])

        if not ret:
            return []

        if len(ret) == 1:
            return ret[0]

        num_small = 1000
        num_large = 0
        for r in ret:
            x = len(r[0].frags)
            if x < num_small:
                num_small = x
            if x > num_large:
                num_large = x

        # if num_small is 1, it means we have an exact match -- use that
        # otherwise use the match with the largest fragments
        if num_small == 1:
            num_large = num_small

        for x in range(len(ret) - 1, -1, -1):
            if len(ret[x][0].frags) != num_large:
                del ret[x]

        if len(ret) == 1:
            return ret[0]

        if len(ret) == 2 and ret[0][0].frags[0] == ret[1][0].frags[0]:
            if size_override == 0:
                try:
                    val = assembler.parse_numeric(ret[0][1])
                except:
                    val = 256
                if val < 256:
                    size_override = 1
                else:
                    size_override = 2
            if size_override == 1:
                if len(ret[0][0].code) < len(ret[1][0].code):
                    return ret[0]
                else:
                    return ret[1]
            elif size_override == 2:
                if len(ret[0][0].code) > len(ret[1][0].code):
                    return ret[0]
                else:
                    return ret[1]

        return []
