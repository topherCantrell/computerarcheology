with open('content/CoCo/popcorn/roms/popcorn.bin', 'rb') as f:
    binary = f.read()


pos = 0
for i in range(0x5B7, 0x06c1):
    byte = binary[i]
    bits = [(byte >> bit) & 1 for bit in range(0, 8)]
    g = (''.join(['1' if bit else '.' for bit in bits]))
    d = hex(byte).upper()[2:]
    d = d.rjust(2, '0')
    print(hex(0xC000+i).upper()[2:],d,'; ', g)
    pos += 1
    if pos % 7 == 0:
        print()
   
