fname = 'btBank0.bin'

origin = 0xF000

start = 0xF36C
end = 0xF800

with open(fname, 'rb') as f:
    data = f.read()

cnt = 16
while start < end:
    if cnt >= 16:
        cnt = 0
        g = hex(start).upper()[2:]
        print()
        print(g + ':', end='')
    g = hex(data[start - origin]).upper()[2:]
    if len(g) < 2:
        g = '0' + g
    print(' ' + g, end='')

    start += 1
    cnt += 1
