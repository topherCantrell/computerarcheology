import opcodetools.cpu.base_assembly
import opcodetools.cpu.base_disassembly
import opcodetools.cpu.opcode

'''
  The CPU class is a list of individual opcodes. An opcode has several parts:
    - DATA the byte format of the opcode in memory
    - MNEMONIC the assembly language representation
    - USE how the individual parts (lower case letters) of the opcode bytes are used

  Example opcodes from different machines:

    DATA        MMNEMONIC     CPU   USE
    20 a0 a1    JSR a         6502  (a=code)
    90 aa       BCC a         6502  (a=code_pcr)
    21 aa       AND (a,X)     6502  (a=ram)
    69 aa       ADC #a        6502  (a=const)
    D3 aa       OUT (a),A     Z80   (a=port_w)
    6C a0 a1    JMP (a)       6502  (a=code)
    10 aa bb    JBC a,b       8502  (a=ram_bit,b=code)
    85 bb aa    MOV a,b       6502  (a=ram,b=ram)

  Lower-case letters identify substitution information in the opcode. The single letters in mnemonic map to
  multiple letters in the data list. The USE field explains how each substitution is used (see below).

  Multibyte substitutions list the order of the bytes. 0 is the least significant, 1 is next, and so on.
  A little-endian address would be: a0a1. A big-endian address would be: a1a0.

  The USE field explains how the field is used. The webifier uses this information to pick label links for
  the webified disassembly.

  The base uses are:
    - const (an immediate constant)
    - data  (address is a regular read/write memory access)
    - code  (address is a label in the code)
    - port  (address is a port read/write memory access)

  Direction qualifiers include (direction often matters for I/O addresses):
    - _r  The opcode reads from the address
    - _w  The opcode writes to the address
    - _rw The opcode reads from the address and then writes back to it

  The _pcr qualifier indicates the actual address is relative to the program counter.

  Some processors have their own substitution qualifiers.

  Qualifiers - 6809 specific
    _pair  Pair of registers
    _pshs  Register list (push to S)
    _puls  Register list (pull from S)
    _pshu  Register list (push to U)
    _pulu  Register list (pull from U)
    _bp    BasePage *

    * The 6809 has a BP register (not always 00). Thus address 0010 and address >10 could be different.
    Other processors have shortcuts for 1 byte addresses, but the upper byte is always 00 such
    that 0010 and >10 are the same.

  Qualifiers - 8051 specific
    _bit  Bit address
    _11   11_bit address (3 bits in opcode)

'''


class CPUException(Exception):
    pass


class CPU(opcodetools.cpu.base_assembly.BaseAssembly, opcodetools.cpu.base_disassembly.BaseDisassembly):

    cpu_singletons = {}

    def __init__(self, opcodes: list, little_endian=True):
        '''Create a basic CPU from a list of opcodes

        Args:
            opcodes (list): List of opcode objects
            little_endian (bool): True for little-endian machines (False for big-endian)
        '''

        self.little_endian = little_endian
        self._opcodes = []
        self._opcodes_info = opcodes
        self._quick_codes = {}  # Helps in searching for large opcode lists
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

    def make_opcode(self, info: dict) -> opcodetools.cpu.opcode.Opcode:
        '''Create an opcode from the given info.

        This is a factory method to allow for overrides

        Args:
            info (dict): the opcode information
        Returns:
            Opcode: factoried opcode
        '''
        return opcodetools.cpu.opcode.Opcode(info)

    def make_word(self, term: int) -> int:
        '''Convert an integer to a list of 2 bytes

        Args:
            term (int): the value to convert
        Returns:
            list: two byte-values in the CPU's endian order
        '''

        a = term & 0xFF       # Little
        b = (term >> 8) & 0xFF  # Big

        if self.little_endian:
            return [a, b]
        else:
            return [b, a]
