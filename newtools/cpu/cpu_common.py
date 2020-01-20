
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

    def __init__(self, opcodes):
        pass
