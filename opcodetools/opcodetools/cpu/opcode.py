class Opcode():

    '''All the information about a single opcode

    Opcodes objects are super-simple. They are just structures.
    '''

    def __init__(self, info: dict):
        self.cpu = None
        self.frags = None  # For assembly
        self.info = info
        self.mnemonic = info['mnemonic']
        self.code = []
        code = info['code']
        cts = {}  # Byte sizes for each spec
        for i in range(0, len(code), 2):
            frag = code[i:i + 2]
            if frag.islower():
                self.code.append(frag)
                if not frag[0] in cts:
                    cts[frag[0]] = 1
                else:
                    cts[frag[0]] += 1
            else:
                self.code.append(int(frag, 16))
        self.use = {}
        use = info['use']
        if use:
            use = use.split(',')
            for u in use:
                i = u.index('=')
                sp = u[:i].strip()
                specs = u[i + 1:].strip().split('_')
                specs.append('s' + str(cts[sp]))
                self.use[sp] = specs
