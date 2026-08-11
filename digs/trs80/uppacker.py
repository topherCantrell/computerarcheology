import z80

class PyramidZ80(z80.Z80Machine):

    def __init__(self):
        super().__init__()        

        with open('Pyramid1.bin', "rb") as f:
            self.set_memory_block(0x4200, f.read())

        # 4593 -- "CD 10 00 CALL $0010" print the char and set PC to 4596
        # 44AB -- "C8 RET Z" if zero is zero, done

        self.set_breakpoint(0x4593)
        self.set_breakpoint(0x4248)


    def handle_breakpoint(self):
        pc = self.pc
        if pc == 0x4593:
            c = self.a
            if c==13:
                self.text += '\n'
            else:
                self.text += chr(c)                
            self.pc = 0x4596
            return True        
        else:
            return False


m = PyramidZ80()

def unpack_message(address):  
    m.text = ''
    m.sp = 0x475C
    m.pc = 0x4242
    m.hl = address

    while True:
        events = m.run()
        if events & m._BREAKPOINT_HIT:
            if not m.handle_breakpoint():
                return m.text


print(unpack_message(0x70B8))
