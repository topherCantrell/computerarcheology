class Opcode():

    '''All the information about a single opcode

    Opcodes objects are super-simple. They are just structures.
    '''

    def __init__(self, info: dict):
        self.cpu = None
        self.frags = None  # For assembly
        self.info = info
        self.mnemonic = info['mnemonic']
        self.bus = info['use']
        self.code = []
        code = info['code']
        for i in range(0, len(code), 2):
            frag = code[i:i + 2]
            if frag.islower():
                self.code.append(frag)
            else:
                self.code.append(int(frag, 16))
