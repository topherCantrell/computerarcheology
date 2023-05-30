def binary_8(value):
    return bin(value)[2:].rjust(8,'0')


def dump_split(data):
    for num in range(0,256):
        print(num)
        for y in range(8):
            a = data[num*8+y]
            b = data[2048+num*8+y]
            aa = binary_8(a)
            bb = binary_8(b)
            cc = ''
            for x in range(8):
                cc = cc + str(int(aa[x])*2 + int(bb[x]))
            print(cc.replace('0','.'))
        print()
            


with open('content/arcade/phoenix/roms/fgtiles.bin', 'rb') as f:
    data = f.read()

dump_split(data)
