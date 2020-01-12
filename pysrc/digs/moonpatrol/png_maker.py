from _sqlite3 import Row

import png

import tools.binary


def _get_binary_string(value):
    a = bin(value)[2:]
    while len(a) < 8:
        a = '0' + a
    return a


class BackgroundStrategy:

    def get_tile_size(self):
        return 256, 64

    def get_tile_data(self, num, im_data):
        #ret = [0] * 256 * 64
        ret = []
        for x in range(4096):
            a = _get_binary_string(im_data[x])
            ret.append(int(a[4] + a[0], 2))
            ret.append(int(a[5] + a[1], 2))
            ret.append(int(a[6] + a[2], 2))
            ret.append(int(a[7] + a[3], 2))
        return ret


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
            a = _get_binary_string(plane1[x])
            b = _get_binary_string(plane2[x])
            for y in range(8):
                ming = a[y] + b[y]
                ret.append(int(ming, 2))
        return ret

    def get_tile_size(self):
        return 16, 16

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

moon_patrol_im_sets = [
    [moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m20'], moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m70']],
    [moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['mC0'], moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['mA0']],
    [moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m00'], moon_patrol_bg_colors['m77'], moon_patrol_bg_colors['m70']],
]

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

images = []

images1 = [
    [
        'GFX3', BackgroundStrategy(), moon_patrol_im_sets,
        ['bgMountains', '0', 1],
    ],
    [
        'GFX4', BackgroundStrategy(), moon_patrol_im_sets,
        ['bgHills', '0', 0],
    ],
    [
        'GFX5', BackgroundStrategy(), moon_patrol_im_sets,
        ['bgCity', '0', 2],
    ],
]

images2 = [[
    'GFX2', SpriteStrategy(), moon_patrol_sp_sets,
    ['buggy', '1,2/3,4', 0],
    ['redBuggy', '1,2/3,4', 12],
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
    ['craterExplosionA', '4E', 1],
    ['craterExplosionB', '4F,50/51,52', 1],
    ['craterExplosionC', '53,54/55,56', 1],
    ['craterExplosionD', '57,58/59,5A', 1],
    ['craterExplosionE', '5B,5C/5D,5E/5F,60', 1],
    ['alienShotGroundA', '61', 3],
    ['alienShotGroundB', '62', 3],
    ['alienShotGroundC', '63', 3],
    ['alienShotGroundD', '64,65/66,67', 3],
    ['alienShotGroundE', '68,69/6A,6B', 3],
    ['rubbleA', '6C/6D', 3],
    ['rubbleB', '6E/6F', 3],
    ['shotsHitting', '7A', 1],
    ['score300', '7D', 14],
    ['score500', '7D', 15],
    ['score800', '7E', 14],
    ['score1000', '7E', 15],
    ['unknown', '3C', 1],
    ['plantLeavesA', '70', 2],
    ['plantLeavesB', '73', 2],
    ['plantLeavesC', '74', 2],
    ['plantLeavesD', '75', 2],
    ['plantA', '71,72', 8],
    ['plantB', '76,77', 8],
    ['plantC', '78,79', 8],
]]


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

def get_png_data(data,colors,pixel_size):
    img = []
    for y in range(len(data)):
        for yy in range(pixel_size):
            row = ()
            for x in range(len(data[y])):
                for xx in range(pixel_size):
                    row = row + colors[data[y][x]]
            img.append(row)
    return img
    

def make_png(data, colors, pixel_size, fname):    
    img = get_png_data(data,colors,pixel_size)
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
        for x in range(len(im_layout)):
            im_layout[x] = im_layout[x].split(',')
            for y in range(len(im_layout[x])):
                im_layout[x][y] = int(im_layout[x][y], 16)
        for y in range(len(im_layout)):
            for x in range(len(im_layout[y])):
                im_layout[y][x] = set_strategy.get_tile_data(im_layout[y][x], im_data)

        rows = len(im_layout) * ts[1]
        cols = len(im_layout[0]) * ts[0]

        pix_data = []
        for c in range(rows):
            pix_data.append([0] * cols)

        for tile_row in range(len(im_layout)):
            for tile_col in range(len(im_layout[tile_row])):
                for ro in range(ts[1]):
                    for co in range(ts[0]):
                        d = im_layout[tile_row][tile_col][ro * ts[0] + co]
                        pix_data[tile_row * ts[1] + ro][tile_col * ts[0] + co] = d

        make_png(pix_data, set_color_set[im_set], 5, im_name + '.png')

def get_tile_data(data,number):
    ret = []
    
    dataA = data[number * 8:number * 8 + 8]  # BinaryData.getData(tileAddress*8,8);
    dataB = data[number * 8 + 4096:number * 8 + 4096 + 8]  # BinaryData.getData(tileAddress*8+4096,8);

    for x in range(8):
        row = []
        a = bin(dataA[x])[2:]
        while len(a) < 8:
            a = '0' + a
        b = bin(dataB[x])[2:]
        while len(b) < 8:
            b = '0' + b
        row.append(int(a[0] + b[0], 2))
        row.append(int(a[1] + b[1], 2))
        row.append(int(a[2] + b[2], 2))
        row.append(int(a[3] + b[3], 2))
        row.append(int(a[4] + b[4], 2))
        row.append(int(a[5] + b[5], 2))
        row.append(int(a[6] + b[6], 2))
        row.append(int(a[7] + b[7], 2))
        ret.append(row)
        
    return ret
    
def make_tile(data, number, color): 
       
    ret = get_tile_data(data,number)
    
    tn = f'tile_{hex(number)[2:].upper()}.png'
    make_png(ret, moon_patrol_txt_sets[color], 5,tn )


im_data = tools.binary.get_binary('../../../content/Arcade/MoonPatrol/GFX1.md', 0)

cs = 0x0F

for x in range(0x68,0x102):
    if x==0x71:
        cs = 0x11
    elif x==0x7C:
        cs = 0x13
    elif x==0x7F:
        cs = 0x12
    elif x==0x81:
        cs = 0x13
    elif x==0x85:
        cs = 0x0F
    elif x==0x86:
        cs = 0x14
    elif x==0x87:
        cs = 0x12
    elif x==0xA0:
        cs = 0x04
    make_tile(im_data, x, cs)
    
for x in range(0x1B0,0x200):
    make_tile(im_data,x,0)
    
def process_tile_picture(txt):
    txt = txt.replace('\n','')
    txt = txt.replace(' ','')
    rows = txt.split('|')
    ret = []
    cs = 0
    for row in rows:
        ret.append(row.split(','))
    for y in range(len(ret)):
        for x in range(len(ret[y])):            
            c = ret[y][x]
            i = c.find('@')
            if i>=0:
                cs = int(c[i+1:],16)
                c = c[0:i]
            ret[y][x] = (int(c,16),cs)
    return ret

def make_tile_picture(data,txt,colors,pixel_size,name):
    tiles = process_tile_picture(txt)    
    
    for y in range(len(tiles)):
        for x in range(len(tiles[y])):
            dat = get_tile_data(im_data,tiles[y][x][0])
            cs = tiles[y][x][1]
            tiles[y][x] = get_png_data(dat,colors[cs],pixel_size)
            
    final_data = []    
    for y in range(len(tiles)):        
        for yy in range(len(tiles[y][0])):
            row = ()
            for x in range(len(tiles[y])):
                row = row + tiles[y][x][yy]
            final_data.append(row)
            
    with open(name, 'wb') as f:
        w = png.Writer(len(tiles[0]) * 8 * pixel_size, len(tiles) * 8 * pixel_size, greyscale=False, transparent=(0, 0, 0))
        w.write(f, final_data)

sp = '''
    9A@0F, 68, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A | 
    9A, 69, 6A, 6B, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A |
    6C, 6D, 6E, 6F, 70, 71@11, 72, 73, 74, 75, 76, 77, 78, 79, 7A, 7B, 9A |
    7C@13, 7D, 7E, 7F@12, 80, 81@13, 82, 83, 84, 85@0F, 86@14, 87@12, 88, 89, 8A, 8B, 8C |
    F3, F3, F3, F3, F3, F3, 8D, 8E, 8F, 90, 91, F3, F3, F3, F3, F3, F3'''
                
moon_t = '''
   1B0@0, 1B5, 1B9, 1BE, 1C3, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A, 9A |
   1B1, 1B6, 1BA, 1BF, 1C4, 1C7, 1CB, 1CD, 1D0, 1D3, 1D6, 1D8, 1D9, 1DB |
   1B2, 1B7, 1BB, 1C0, 1C5, 1C8, 1BF, 1BC, 1D1, 1D4, 1D7, 1C0, 1BC, 1C1 |
   1B3, 1B8, 1BC, 1C1, 1C6, 1C9, 1CC, 1CE, 1D2, 1D5, 1BC, 1C1, 1C5, 1DC |
   1B4,  9A, 1BD, 1C2, 1BD, 1CA,  9A, 1CF, 1CA, 1C2, 1BD, 1C2, 1DA,  9A'''
        
patrol_t = '''
   1B0@0,1DD,1E0,1E3,100,100,100,100,1F3,1F7,100,100,100,100,100,100,1C5,1C3 |
   1B1,  1DE,1E1,1E4,1E6,1E9,1ED,1F0,1F4,1F8,1B2,1FD,1FE,1D0,1D3,1D6,1BF, 9F |
   1B2,  1DF,1E2,1E5,1B2,1EA,1EE,1F1,1F5,1F9,1B3,1B8,1BC,1D1,1D4,1D7,1C0, 9F |
   1B3,  1B8, 9F, 9F,1E7,1EB,1EF,1F2,1BF,1B0,1FB, 9F,1CE,1D2,1D5,1BC,1FF, 9F |
   1B4,   9F, 9F, 9F,1E8,1EC,1B4, 9F, 9F,1FA,1FC, 9F,1CF,1CA,1C2,1BD,1EC, 9F'''

make_tile_picture(im_data,sp,moon_patrol_txt_sets,5,'starting.png')
make_tile_picture(im_data,moon_t,moon_patrol_txt_sets,5,'moon.png')
make_tile_picture(im_data,patrol_t,moon_patrol_txt_sets,5,'patrol.png')
