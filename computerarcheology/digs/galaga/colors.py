data = '''0000: F6
0001: 07
0002: 3F
0003: 27    
0004: 2F 
0005: C7    
0006: F8 
0007: ED    
0008: 16 
0009: 38    
000A: 21 
000B: D8    
000C: C4 
000D: C0    
000E: A0 
000F: 00    
0010: F6 
0011: 07    
0012: 3F 
0013: 27    
0014: 00 
0015: C7    
0016: F8 
0017: E8    
0018: 00 
0019: 38    
001A: 00 
001B: D8    
001C: C5 
001D: C0    
001E: 00 
001F: 00'''

def to_value(s):
    ret = 0
    if s[0] == '1':
        ret += 0x97
    if s[1] == '1':
        ret += 0x47
    if s[2] == '1':
        ret += 0x21
    return ret

data = data.split('\n')
cn = 0
for d in data:
    d = d.strip()
    e = d.split()
    b = bin(int(e[1], 16))[2:]
    while len(b) < 8:
        b = '0' + b
    red = b[5:]
    green = b[2:5]
    blue = b[:2]+'0'

    bb = b[0:2]+' '+b[2:5]+' '+b[5:]

    red = hex(to_value(red))[2:].upper()
    while len(red) < 2:
        red = '0' + red
    green = hex(to_value(green))[2:].upper()
    while len(green) < 2:
        green = '0' + green
    blue = hex(to_value(blue))[2:].upper()
    while len(blue) < 2:
        blue = '0' + blue
    cnn = hex(cn)[2:].upper()
    while len(cnn) < 2:
        cnn = '0' + cnn
    # print(f'{e[0]} {e[1]}    ; {cnn}: {bb}  #{red}{green}{blue}  <FONT style="BACKGROUND-COLOR:#{red}{green}{blue}">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>')
    print(f'"#{red}{green}{blue}",')

    cn+=1