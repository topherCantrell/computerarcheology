from computerarcheology.util import util

origin = 0  # Like 0xC000

CHARS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ[]()*0123456789.-c  ?'

def print_data_run(data, addr, length):
    print(f'{util.hex4(addr-origin)}:', end='')
    pos = addr - origin
    for i in range(length):
        print(f' {util.hex2(data[pos])}', end='')
        pos += 1
    print()
    
with open('content/arcade/galaga/roms/2600j.bin','rb') as f:
    data = f.read()

tab = 0

for x in range(32):
    st = tab + x*32
    print_data_run(data, st,2)
    print_data_run(data, st+2,4)
    print('; "',end='')
    for i in range(26):
        c =  data[st + 6 + i]
        if c < len(CHARS):
            c = CHARS[c]
        else:
            c = '%'
        print(c,end='')
    print('"')
    print_data_run(data, st+6,26)


def print_data_block():
    start = 0  # Like 0xCF11
    end = len(data)  # Like 0xD000

    per_row = 8

    pos = start-origin
    end = end-origin
    cols = 0

    while pos < end:
        if cols==0:
            print(f'{util.hex4(pos)}:',end='')
        v = data[pos]
        print(f' {util.hex2(v)}', end='')
        pos+=1
        cols+=1
        if cols == per_row:
            cols = 0
            print()

