
import code.markdown_utils


binary = code.markdown_utils.get_binary('../../content/CoCo/Downland/Code.md')

"""
p = 0xD908 - 0xC000

while p<(0xDA19-0xC000):
    print('{:04X}: {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X}'.format(
        p,binary[p],binary[p+1],binary[p+2],binary[p+3],binary[p+4],binary[p+5],binary[p+6]))
    for i in range(7):
        s = '{:08b}'.format(binary[p+i])
        s=s.replace('0','.')
        s=s.replace('1','*')
        print('; '+s)
    p += 7
"""

p = 0xD000 - 0xC000
chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_:.'

while True:
    d = ';    '
    s = '{:04X}:'.format(p+0xC000)
    while True:
        cn = binary[p]
        p = p + 1
        s = s + ' {:02X}'.format(cn)
        if cn != 0xFF and cn<len(chars):
            d = d + '  '+chars[cn]
            
        if cn == 0xFF:            
            print(d)
            print(s)
            print()    
            break
        
        
    