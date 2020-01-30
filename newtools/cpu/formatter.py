
#import cpu.cpu_8052 as CPU
#import cpu.cpu_6502 as CPU
#import cpu.cpu_6803 as CPU
import cpu.cpu_6809 as CPU

"""
for op in CPU.OPCODES:
    if 'mnem' in op:
        m = op['mnem']
    elif 'mnemonic' in op:
        m = op['mnemonic']
        
    c = op['code']
    
    if 'bus' in op:
        b = op['bus']
    elif 'use' in op:
        b = op['use']  
        
    b = '"'+b+'",'
    b = b.ljust(16)
    
    c = '"'+c+'",'
    c=c.ljust(20)
    
    m = '"'+m+'",'
    m = m.ljust(20)
    """
        
    #print('    {"mnemonic":'+m+'"code":'+c+    '"use":'+b+   '},')


for op in CPU.POSTS:
    m = op['post']        
    c = op['code']
    
    if 'use' in op:
        b = op['use']
    else:
        b = ''  
        
    b = '"'+b+'",'
    b = b.ljust(16)
    
    c = '"'+c+'",'
    c=c.ljust(20)
    
    m = '"'+m+'",'
    m = m.ljust(20)
        
    print('    {"post":'+m+'"code":'+c+    '"use":'+b+   '},')