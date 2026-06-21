import z80

class Xenos(z80.Z80Machine):
    def __init__(self):
        super().__init__()

        # The ROM area is filled with "RST 0". Any call to a ROM  function will
        # hit this breakpoint with return information on the stack. We will 
        # handle the function and return the caller.
        trs80_rom = bytes([0xC7] * 0x5D00)
        self.set_memory_block(0x0000, trs80_rom)          

        self.print_buffer = ''          
        
        # Load the main code
        with open('xenos.bin', 'rb') as f:            
            self.set_memory_block(0x5D00, f.read())       

        self.breakpoints = {
            0x0000: self.handle_rom_call,
            0x619F: self.flash_error,
            0x6252: self.handle_user_input,
            0x6A29: self.handle_load_section,
            0x6EBB: self.save_system_objects,
            0x6EC5: self.load_system_objects,
        }     
        for bp in self.breakpoints:
            self.set_breakpoint(bp)     

    def pop_return_address(self):
        ret = (self.memory[self.sp+1]<<8) + self.memory[self.sp]
        self.sp += 2
        return ret
    
    def push_return_address(self, addr):
        self.sp -= 2
        self.memory[self.sp] = addr & 0xFF
        self.memory[self.sp+1] = (addr>>8) & 0xFF

    def handle_breakpoint(self):
        pc = self.pc
        if pc in self.breakpoints:
            return self.breakpoints[pc]()        
        else:
            print(f'Hit unknown breakpoint at {pc:04X}')
            return False       
        
    def clear_trs80_botom_row(self):
        for i in range(64):
            self.memory[0x3FC0+i] = 0x20 # Space character
        self.memory[0x4020] = 0x20
        self.memory[0x4021] = 0x3F

    def handle_rom_call(self): # 0x0000 (RST 0)
        # One past the RST 0 address. Subtract 1 to get the target ROM call address.
        return_to = (self.memory[self.sp+1]<<8) + self.memory[self.sp]
        return_to -= 1

        if return_to == 0x002B: # GET KEY            
            self.a = ord('0') # Just a hardcoded 0
        elif return_to == 0x0033: # PRINT CHAR                     
            c = self.a
            #print(">>>",c,chr(c))   
            if c == 13:
                self.clear_trs80_botom_row()
                if not self.print_buffer:
                    print() # Blank line for a new paragraph
                while self.print_buffer:
                    pos = 62
                    if pos >= len(self.print_buffer):
                        pos = len(self.print_buffer)-1
                    while self.print_buffer[pos] != ' ':                        
                        pos -= 1
                    print(self.print_buffer[0:pos])
                    self.print_buffer = self.print_buffer[pos+1:]                                        
                self.print_buffer = ''
            else:
                self.print_buffer += chr(c)     
        elif return_to == 0x402D:
            # DOS exit program
            return False                      

        else:
            print(f'##### Hit ROM call to 0x{return_to:04X}, not handled')
            print(f'##### Called from: {self.memory[self.sp+3]:02X}{self.memory[self.sp+2]:02X}')
            return False

        # Drop the RST 0 return and return to the caller of the ROM routine.
        self.pop_return_address() # Drop the RST 0 return
        self.pc = self.pop_return_address() # Return to caller
        return True      

    def handle_load_section(self):
        section_num = chr(self.memory[0x6AEC])
        with open(f'section{section_num}.bin', 'rb') as f:
            data = f.read()
        self.set_memory_block(0x5200, data)    
        self.pc = 0x6A6F
        return True
    
    def handle_user_input(self):        
        inp = input()
        inp = inp.upper()
        for i in range(64):
            if i < len(inp):
                c = inp[i]
            else:
                c = ' '
            self.memory[0x3FC0+i] = ord(c)
        self.pc = 0x6277
        return True
    
    def flash_error(self):
        last = bytes(self.memory[0x3FC0:0x3FC0+64]).decode()
        last = last.strip()
        print(last)
        self.clear_trs80_botom_row()
        self.pc = 0x5D3B
        return True
    
    def save_system_objects(self):
        self.saved_objects = bytearray(self.memory[0x887A:0xB3AF])
        self.pc = 0x6F45
        return True
    
    def load_system_objects(self):
        self.set_memory_block(0x887A, self.saved_objects)
        self.pc = 0x6F45
        return True
        
    
        
m = Xenos()
m.pc = 0x5D00

while True:
    events = m.run()
    if events & m._BREAKPOINT_HIT:
        if not m.handle_breakpoint():
            break
    