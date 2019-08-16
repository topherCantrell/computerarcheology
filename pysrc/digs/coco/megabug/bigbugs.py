import code.markdown_utils

binary = code.markdown_utils.get_binary('../../../../content/CoCo/MegaBug/Code.md')

#addr = 0xCAB0
#addr = 0xCB50
#addr = 0xCBF0

visgrid = []
for y in range(32):
    visgrid.append(['?'] * 5 * 4)

pixchars = {
    '00': '.',
    '01': '+',
    '10': '$',
    '11': '#'
}

for x in range(5):
    for y in range(32):
        pixs = binary[(addr - 0xC000) + x * 32 + y]
        g = bin(pixs)[2:]
        while len(g) < 8:
            g = '0' + g
        for z in range(4):
            p = g[z * 2:z * 2 + 2]
            visgrid[y][x * 4 + z] = pixchars[p]

for x in range(5):
    g = '{:04X}:'.format(addr + x * 32)
    for y in range(32):
        g = g + ' {:02X}'.format(binary[(addr - 0xC000) + x * 32 + y])
    print(g)


for r in visgrid:
    print('; ', end='')
    for c in r:
        print(c, end='')
    print()
