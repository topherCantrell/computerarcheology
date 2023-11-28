from computerarcheology.util import util

with open('content/arcade/phoenix/roms/proms.bin','rb') as f:
    data = f.read()

comb = []

for i in range(256):
    x = bin(data[i])[2:].rjust(8,'0')
    y = bin(data[i+256])[2:].rjust(8,'0')
    bit0 = int(x[7])
    bit1 = int(y[7])
    red = 0x55*bit0 + 0xaa*bit1

    bit0 = int(x[5])
    bit1 = int(y[5])
    green = 0x55*bit0 + 0xaa*bit1

    bit0 = int(x[6])
    bit1 = int(y[6])
    blue = 0x55*bit0 + 0xaa*bit1

    print(util.hex2(red), util.hex2(green), util.hex2(blue))


