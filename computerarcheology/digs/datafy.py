# fname = 'd:/git/computerarcheology/content/atari2600/burgertime/btBank7.bin'
fname = 'd:/git/computerarcheology/content/trs80/xenos/roms/usvdobjs.bin'

origin = 0x0000

with open(fname, 'rb') as f:
    data = f.read()

cnt = 16
pos = 0
while pos < len(data):
    if cnt >= 16:
        cnt = 0
        g = hex(pos + origin).upper()[2:]
        print()
        print(g + ':', end='')
    g = hex(data[pos]).upper()[2:]
    if len(g) < 2:
        g = '0' + g
    print(' ' + g, end='')

    pos += 1
    cnt += 1
