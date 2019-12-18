import png
import tools.binary


class SpriteStrategy:

    def _get_binary_string(self, value):
        a = bin(value)[2:]
        while len(a) < 8:
            a = '0' + a
        return a

    def _get_sprite_quadrant_data(self, tile_address, im_data):
        ret = []
        plane1 = im_data[tile_address:tile_address + 8]
        plane2 = im_data[tile_address + 0x1000:tile_address + 0x1000 + 8]
        for x in range(8):
            a = self._get_binary_string(plane1[x])
            b = self._get_binary_string(plane2[x])
            for y in range(8):
                ming = a[y] + b[y]
                ret.append(int(ming, 2))
        return ret

    def get_tile_size(self):
        return 16

    def get_tile_data(self, num, im_data):
        ret = []
        a = self._get_sprite_quadrant_data(num * 32, im_data)
        b = self._get_sprite_quadrant_data(num * 32 + 8, im_data)
        c = self._get_sprite_quadrant_data(num * 32 + 16, im_data)
        d = self._get_sprite_quadrant_data(num * 32 + 24, im_data)
        cnta = 0
        cntb = 0
        for y in range(8):
            for x in range(8):
                ret.append(a[cnta])
                cnta += 1
            for x in range(8):
                ret.append(c[cntb])
                cntb += 1
        cnta = 0
        cntb = 0
        for y in range(8):
            for x in range(8):
                ret.append(b[cnta])
                cnta += 1
            for x in range(8):
                ret.append(d[cntb])
                cntb += 1
        return ret


moon_patrol_bg_colors = {
    'm00': (0, 0, 0),
    'm20': (0, 151, 0),
    'm70': (0, 222, 81),
    'm77': (255, 222, 81),
    'mC0': (0, 0, 255),
    'mA0': (0, 151, 174),
}

moon_patrol_bg_sets = [
    [moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m20'], moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m70']],
    [moon_patrol_bg_colors['mC0'], moon_patrol_bg_colors['m20'], moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m70']],
    [moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m20'], moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m70']],
    [moon_patrol_bg_colors['mA0'], moon_patrol_bg_colors['m20'], moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m70']],
    [moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m77'], moon_patrol_bg_colors['m70']],
    [moon_patrol_bg_colors['mC0'], moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m77'], moon_patrol_bg_colors['m70']],
    [moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m77'], moon_patrol_bg_colors['m70']],
    [moon_patrol_bg_colors['mA0'], moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m77'], moon_patrol_bg_colors['m70']],
]

moon_patrol_sp_colors = {
    'm00': (0, 0, 0),
    'm01': (0x00, 0x00, 0x1A),
    'm02': (0xC1, 0x00, 0xAE),
    'm03': (0x00, 0xAE, 0xC8),
    'm04': (0x84, 0xC8, 0x00),
    'm05': (0xC1, 0x00, 0x00),
    'm06': (0x00, 0xC8, 0x00),
    'm07': (0x84, 0x00, 0x00),
    'm08': (0xC1, 0xC8, 0xC8),
    'm09': (0xC1, 0xC8, 0x00),
    'm0A': (0x84, 0x51, 0x00),
    'm0B': (0x3E, 0x37, 0x00),
    'm0C': (0x3E, 0x00, 0xC8),
    'm0D': (0xC1, 0x90, 0x00),
    'm0E': (0x62, 0x90, 0xC8),
    'm0F': (0x00, 0x51, 0x00),
}

moon_patrol_sp_sets = [
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m01'], moon_patrol_sp_colors['m02'], moon_patrol_sp_colors['m03']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m04'], moon_patrol_sp_colors['m02'], moon_patrol_sp_colors['m05']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m05'], moon_patrol_sp_colors['m06'], moon_patrol_sp_colors['m07']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m07'], moon_patrol_sp_colors['m08'], moon_patrol_sp_colors['m09']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m0A'], moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m0B']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m00']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m00']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m09'], moon_patrol_sp_colors['m0E'], moon_patrol_sp_colors['m05']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m05'], moon_patrol_sp_colors['m03'], moon_patrol_sp_colors['m0F']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m09'], moon_patrol_sp_colors['m01'], moon_patrol_sp_colors['m05']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m01'], moon_patrol_sp_colors['m08'], moon_patrol_sp_colors['m00']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m01'], moon_patrol_sp_colors['m05'], moon_patrol_sp_colors['m00']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m01'], moon_patrol_sp_colors['m05'], moon_patrol_sp_colors['m03']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m04'], moon_patrol_sp_colors['m0D'], moon_patrol_sp_colors['m05']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m05'], moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m05']],
    [moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m00'], moon_patrol_sp_colors['m05'], moon_patrol_sp_colors['m05']],
]

moon_patrol_txt_colors = {
    'm00': (0, 0, 0),
    'm01': (0x21, 0x00, 0x00),
    'm07': (0xFF, 0x00, 0x00),
    'm0F': (0xFF, 0x21, 0x00),
    'm28': (0x00, 0xB8, 0x00),
    'm3F': (0xFF, 0xFF, 0x00),
    'm5C': (0x97, 0x68, 0x51),
    'm67': (0xFF, 0x97, 0x51),
    'm87': (0xFF, 0x00, 0xAE),
    'm91': (0x21, 0x47, 0xAE),
    'm9D': (0xB8, 0x68, 0xAE),
    'mBD': (0xB8, 0xFF, 0xAE),
    'mC8': (0x00, 0x21, 0xFF),
    'mE8': (0x00, 0xB8, 0xFF),
    'mFF': (0xFF, 0xFF, 0xFF),
}

moon_patrol_txt_sets = [
    [moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['mE8'], moon_patrol_txt_colors['mFF'], moon_patrol_txt_colors['m0F'], ],
    [moon_patrol_txt_colors['mC8'], moon_patrol_txt_colors['m0F'], moon_patrol_txt_colors['m3F'], moon_patrol_txt_colors['mC8'], ],
    [moon_patrol_txt_colors['mE8'], moon_patrol_txt_colors['m01'], moon_patrol_txt_colors['m0F'], moon_patrol_txt_colors['mC8'], ],
    [moon_patrol_txt_colors['mE8'], moon_patrol_txt_colors['m28'], moon_patrol_txt_colors['m87'], moon_patrol_txt_colors['m00'], ],
    [moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m67'], moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m5C'], ],
    [moon_patrol_txt_colors['m67'], moon_patrol_txt_colors['m01'], moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m00'], ],
    [moon_patrol_txt_colors['mC8'], moon_patrol_txt_colors['m87'], moon_patrol_txt_colors['m01'], moon_patrol_txt_colors['mE8'], ],
    [moon_patrol_txt_colors['mE8'], moon_patrol_txt_colors['m87'], moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m00'], ],
    [moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['mFF'], moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m00'], ],
    [moon_patrol_txt_colors['mC8'], moon_patrol_txt_colors['m01'], moon_patrol_txt_colors['m0F'], moon_patrol_txt_colors['m00'], ],
    [moon_patrol_txt_colors['mE8'], moon_patrol_txt_colors['m87'], moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m00'], ],
    [moon_patrol_txt_colors['m9D'], moon_patrol_txt_colors['m87'], moon_patrol_txt_colors['m91'], moon_patrol_txt_colors['mE8'], ],
    [moon_patrol_txt_colors['m9D'], moon_patrol_txt_colors['m0F'], moon_patrol_txt_colors['m3F'], moon_patrol_txt_colors['m9D'], ],
    [moon_patrol_txt_colors['mE8'], moon_patrol_txt_colors['m01'], moon_patrol_txt_colors['m0F'], moon_patrol_txt_colors['m9D'], ],
    [moon_patrol_txt_colors['m9D'], moon_patrol_txt_colors['m01'], moon_patrol_txt_colors['m0F'], moon_patrol_txt_colors['m00'], ],
    [moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m01'], moon_patrol_txt_colors['mBD'], moon_patrol_txt_colors['mE8'], ],
    [moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m67'], moon_patrol_txt_colors['mBD'], moon_patrol_txt_colors['mE8'], ],
    [moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m07'], moon_patrol_txt_colors['mBD'], moon_patrol_txt_colors['mE8'], ],
    [moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m67'], moon_patrol_txt_colors['mBD'], moon_patrol_txt_colors['mE8'], ],
    [moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m67'], moon_patrol_txt_colors['mBD'], moon_patrol_txt_colors['m01'], ],
    [moon_patrol_txt_colors['m00'], moon_patrol_txt_colors['m67'], moon_patrol_txt_colors['mE8'], moon_patrol_txt_colors['m01'], ],
]

images = [
    [
        'GFX2', SpriteStrategy(), moon_patrol_sp_sets,
        ['buggy', '1,2/3,4', 0],
        ['wheelLargeA', '5', 0],
        ['wheelLargeB', '6', 0],
        ['wheelSmallA', '7', 0],
        ['wheelSmallB', '8', 0],
        ['buggyCrashA', '9,A/B,C', 0],
        ['buggyCrashB', 'D,E/F,10', 0],
        ['buggyExplosionA', '11,12,13/14,15,16', 1],
        ['buggyExplosionB', '17,18,19/1A,1B,1C', 1],
        ['buggyExplosionC', '1D,1E,1F/20,21,22', 1],
        ['buggyExplosionD', '23,24', 1],
        ['buggyExplosionE', '25,26', 1],
        ['buggyExplosionF', '27', 1],

        ['playerShotA', '28', 1],
        ['playerShotB', '29', 1],
        ['playerShotC', '2A', 1],
        ['playerShotD', '2B', 1],
        ['playerShotE', '2C', 1],

        ['rockA', '2D', 4],
        ['rockB', '2E', 4],
        ['rockC', '2F', 4],
        ['rockD', '30', 4],

        ['boulderA', '31', 4],
        ['boulderB', '32', 4],
        ['boulderC', '33', 4],
        ['boulderD', '34', 4],
        ['boulderE', '36', 4],
        ['boulderF', '37', 4],

        ['tank', '38', 9],
        ['tankShot', '39', 9],

        ['speederA', '3A,3B', 9],
        ['speederB', '7B,3B', 9],
        ['speederC', '7C,3B', 9],

        ['mine', '3D', 0xA],

        ['explodingRockA', '3E', 1],
        ['explodingRockB', '3F', 1],
        ['explodingRockC', '40', 1],
        ['explodingRockDA', '41', 1],

        ['alien1', '42', 7],
        ['alien2A', '43', 7],
        ['alien2B', '44', 7],
        ['alien3A', '45', 7],
        ['alien3B', '46', 7],
        ['alien3C', '47', 7],

        ['alienExplosionA', '48', 1],
        ['alienExplosionB', '49', 1],
        ['alienExplosionC', '4A', 1],

        ['alienBubbleShot', '35', 0],
        ['alienShotA', '4B', 1],
        ['alienShotB', '4C', 1],
        ['alienShotC', '4D', 1],


    ],
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


for sprite_set in images:
    set_fname = sprite_set[0]
    set_strategy = sprite_set[1]
    set_color_set = sprite_set[2]
    ts = set_strategy.get_tile_size()
    im_data = tools.binary.get_binary('../../content/Arcade/MoonPatrol/' + set_fname + '.md', 0)
    for image in sprite_set[3:]:
        im_name = image[0]
        im_layout = image[1]
        im_set = image[2]
        im_layout = im_layout.split('/')
        # print(im_layout)
        for x in range(len(im_layout)):
            im_layout[x] = im_layout[x].split(',')
            for y in range(len(im_layout[x])):
                im_layout[x][y] = int(im_layout[x][y], 16)
        for y in range(len(im_layout)):
            for x in range(len(im_layout[y])):
                im_layout[y][x] = set_strategy.get_tile_data(im_layout[y][x], im_data)

        rows = len(im_layout) * ts
        cols = len(im_layout[0]) * ts

        pix_data = []
        for c in range(rows):
            pix_data.append([0] * cols)

        for tile_row in range(len(im_layout)):
            for tile_col in range(len(im_layout[tile_row])):
                for ro in range(ts):
                    for co in range(ts):
                        pix_data[tile_row * ts + ro][tile_col * ts + co] = im_layout[tile_row][tile_col][ro * ts + co]

        make_png(pix_data, set_color_set[im_set], 5, im_name + '.png')


#make_png(text_to_data(tank, 16, 16), colors, 5, 'test.png')
