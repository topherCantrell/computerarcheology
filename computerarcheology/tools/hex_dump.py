from computerarcheology.util import util

with open('content/arcade/phoenix/roms/bgtiles.bin','rb') as f:
    data = f.read()

origin = 0  # Like 0xC000
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

