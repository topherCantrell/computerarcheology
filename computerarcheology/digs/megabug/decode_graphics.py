import sys

import code.markdown_utils


binary = code.markdown_utils.get_binary('../../../content/CoCo/megabug/Code.md')


pos = 0xC990

for z in range(16):

    r = [
        [['?'], ['?'], ['?']],
        [['?'], ['?'], ['?']],
        [['?'], ['?'], ['?']],
        [['?'], ['?'], ['?']],
        [['?'], ['?'], ['?']],
        [['?'], ['?'], ['?']],
    ]
    for x in range(3):
        print('{:04X}: '.format(pos + x * 6), end='')
        for y in range(6):
            dat = binary[pos - 0xC000 + x * 6 + y]
            print(' {:02X}'.format(dat), end='')
            ds = '{:08b}'.format(dat)
            ds = ds.replace('0', '.')
            ds = ds.replace('1', '#')
            r[y][x] = ds
        print()

    for y in range(6):
        print('; ', end='')
        g = ''
        for x in range(3):
            g = g + (r[y][x])
        h = ''
        for p in range(0, len(g), 2):
            a = g[p:p + 2]
            if a == '#.':
                a = '%'
            elif a == '.#':
                a = '#'
            elif a == '##':
                a = '*'
            else:
                a = '.'
            h = h + a
        print(h)

    pos += 6 * 3
    print()

sys.exit()


# ------------------------


pos = 0xCD7A

for z in range(68):
    r = []
    print('{:04X}: '.format(pos), end='')
    for y in range(9):
        dat = binary[pos - 0xC000 + y]
        print(' {:02X}'.format(dat), end='')
        ds = '{:08b}'.format(dat)
        ds = ds.replace('0', '.')
        ds = ds.replace('1', '#')
        r.append(ds)
    print()
    for y in range(9):
        print('; ' + r[y])
    print()
    pos += 9
