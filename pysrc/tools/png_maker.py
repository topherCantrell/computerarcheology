import png

tank = """
......11111.....
.....1111111....
222222211111....
2222222211111...
....111111111...
....111111111...
......3333......
......1111......
..11.112211..11.
.11113111131111.
1133111331113311
1333313333133331
1333313333133331
1133111331113311
.1111.1111.1111.
..11...11...11..
"""

colors = [
    (0, 0, 0),
    (193, 200, 0),
    (193, 0, 0),
    (0, 0, 26)
]


def text_to_data(data, width, height, mapping={'.': 0, '1': 1, '2': 2, '3': 3}):
    data = data.replace('\n', '')
    ret = []
    pos = 0
    for y in range(height):
        row = []
        for x in range(width):
            row.append(mapping[data[pos]])
            pos += 1
        ret.append(row)
    return ret


def make_png(data, colors, pixel_size, fname):
    img = []
    for y in range(len(data)):
        for yy in range(pixel_size):
            row = ()
            for x in range(len(data[y])):
                for xx in range(pixel_size):
                    row = row + colors[data[y][x]]
            img.append(row)
    with open(fname, 'wb') as f:
        w = png.Writer(len(data[0]) * pixel_size, len(data) * pixel_size, greyscale=False, transparent=(0, 0, 0))
        w.write(f, img)


make_png(text_to_data(tank, 16, 16), colors, 5, 'test.png')
