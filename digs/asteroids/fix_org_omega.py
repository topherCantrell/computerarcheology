
fn = 'content/arcade/OmegaRace/VectorROM.md'

with open(fn,'r') as f:
    with open('update.md','w') as f2:
        for line in f:
            if len(line) > 4 and line[4] == ':':                
                addr = int(line[0:4], 16)
                addr = addr - 0x8000
                addr = hex(addr)[2:].rjust(4,'0').upper()
                line = addr + line[4:]
                if 'JSR     $' in line or 'JMP     $' in line:
                    i = line.index('$') + 1
                    addr = int(line[i:i+4], 16)
                    addr = addr - 0x8000                    
                    addr = addr // 2
                    addrn = hex(addr)[2:].rjust(4,'0').upper() + f" (${addr*2:04X})"
                    line = line[:i] + addrn + line[i+4:]
            f2.write(line)