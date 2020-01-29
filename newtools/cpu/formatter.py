
import cpu.cpu_8052 as CPU


for op in CPU.OPCODES:
    if 'mnem' in op:
        m = op['mnem']
    elif 'mnemonic' in op:
        m = op['mnemonic']
        
    c = op['code']
    
    b = op['bus']
    
    m = '"'+m+'",'
    m = m.ljust(20)
        
    print('{"mnemonic":'+m+'},')