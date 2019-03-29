from _operator import pos

import code.markdown_utils


CONFIG = {
    'TRS80': {
        'origin': 0x4300,
        'code': '../../content/TRS80/Pyramid/Code.md',
        'WordTable': 0x56CE - 0x4300,
        'GeneralCommand': 0x59B0 - 0x4300,
        'ScriptNames': 0x509F,
        'BigEndian': False,
        'ObjNames': 0x5047,
        'RoomTable': 0x4888 - 0x4300,
        'AmbientLight': 0x4F45 - 0x4300,
        'RoomScripts': 0x49CC - 0x4300,
    },
    'CoCo': {
        'origin': 0x600,
        'code': '../../content/CoCo/Pyramid/Code.md',
        'WordTable': 0x3C40 - 0x600,
        'GeneralCommand': 0x1945 - 0x600,
        'ScriptNames': 0x0A17,
        'BigEndian': True,
        'ObjNames': 0x18ED,
        'RoomTable': 0x112E - 0x600,
        'AmbientLight': 0x17EB - 0x600,
        'RoomScripts': 0x1272 - 0x600,
    }
}

#CON = CONFIG['CoCo']
CON = CONFIG['TRS80']

binary = code.markdown_utils.get_binary(CON['code'])
_, _, code_only = code.markdown_utils.load_file(CON['code'])

# Load the word table

word_table = []
pos = CON['WordTable']


def readWord(pos):
    if CON['BigEndian']:
        return (binary[pos] << 8) + binary[pos + 1]
    else:
        return (binary[pos + 1] << 8) + binary[pos]


def padTo(s, leng):
    while len(s) < leng:
        s = s + ' '
    return s


def dataToAscii(data):
    ret = ''
    for i in data:
        ret = ret + chr(i)
    return ret


def printWordTable(wtable):
    for w in wtable:
        g = '{:04X}: {:02X}'.format(w['addr'], w['info'])
        for d in w['text_bytes']:
            g = g + ' {:02X}'.format(d)
        g = padTo(g, 32)
        for d in w['data']:
            g = g + '{:02X} '.format(d)
        g = padTo(g, 42) + '; '
        g = g + '{:02b}_{:03b}_{:03b} {}'.format(
            w['info_inf'], w['info_data'], w['info_text'], w['text'])
        print(g)


while binary[pos] != 0:
    info = binary[pos]
    info_inf = info >> 6
    info_data = (info >> 3) & 7
    info_text = info & 7
    word = {
        'addr': pos + CON['origin'],
        'text_bytes': binary[pos + 1:pos + 1 + info_text],
        'text': dataToAscii(binary[pos + 1:pos + 1 + info_text]),
        'data': binary[pos + 1 + info_text:pos + 1 + info_text + info_data],
        'info': info,
        'info_inf': info_inf,
        'info_data': info_data,
        'info_text': info_text,
    }
    pos = pos + 1 + info_text + info_data
    word_table.append(word)

script_names = []

# We assume this has already been disassembled and commented
pos = 0
while True:
    if code_only[pos].address and code_only[pos].address == CON['ScriptNames']:
        break
    pos += 1

for _ in range(29):
    g = code_only[pos].text.strip()
    i = g.rindex(' ')
    script_names.append(g[i + 1:])
    pos += 1

print(script_names)

obj_names = []
pos = 0
while True:
    if code_only[pos].address and code_only[pos].address == CON['ObjNames']:
        break
    pos += 1

for i in range(44):
    g = code_only[pos].text.strip()
    if not '#' in g:
        obj_names.append('#UNUSED_' + str(i + 1))
        pos += 1
        continue
    j = g.index('#')
    i = g.index(' ', j)
    obj_names.append(g[j:i])
    pos += 1

print(obj_names)
# printWordTable(word_table)

rooms = []
pos = CON['RoomTable']

for i in range(81):
    desc = readWord(pos)
    pos += 2
    script = readWord(pos)
    pos += 2
    rooms.append({
        'number': i + 1,
        'desc': desc,
        'script': script,
    })


def makeAmbientLight():
    pos = CON['AmbientLight']
    for i in range(81):
        print('{:04X}: {:02X} {:02X}    ;  {}'.format(
            pos + CON['origin'], binary[pos], binary[pos + 1], i + 1))
        pos += 2


pos = CON['AmbientLight']
for i in range(81):
    if binary[pos] == 0x40:
        rooms[i]['Light'] = True
    else:
        rooms[i]['Light'] = False
    pos += 2

# print(rooms)
# makeAmbientLight()


def getVerb(num):
    for word in word_table:
        if word['info_inf'] != 0 and word['data'][0] == num:
            return word
    return {'text': '??{:02X}??'.format(num)}


def getString(addr):
    pos = 0
    while True:
        if code_only[pos].address and code_only[pos].address == addr:
            break
        pos += 1
    pos -= 1
    ret = ''
    while code_only[pos].text.startswith(';'):
        ret = code_only[pos].text[2:] + ret
        pos -= 1
    return ret


def getObject(num):
    return obj_names[num - 1]


def getRoom(num):
    return "room_" + str(num)


def processScript(pos, end, level, lines):

    lev_pad = '    ' * level

    last = ','

    while True:

        if pos == end:
            return

        com = binary[pos]
        pos = pos + 1

        if com == 1:
            o = binary[pos]
            pos += 1
            rm = getRoom(o)
            lines.append('{:04X}: {:02X} {:02X}     ;{}    "{}","{}"{}'.format(
                pos - 2 + CON['origin'], com, o, lev_pad, script_names[com - 1], rm, last))

        elif com == 0x0A:
            o = binary[pos]
            pos += 1
            lines.append('{:04X}: {:02X} {:02X}     ;{}    "{}","{}"{}'.format(
                pos - 2 + CON['origin'], com, o, lev_pad, script_names[com - 1], o, last))

        elif com == 2 or com == 3 or com == 0x11 or com == 0x12 or com == 0x18 or com == 0x1A:
            o = binary[pos]
            pos += 1
            obj = getObject(o)
            lines.append('{:04X}: {:02X} {:02X}     ;{}    "{}","{}"{}'.format(
                pos - 2 + CON['origin'], com, o, lev_pad, script_names[com - 1], obj, last))

        elif com == 4:
            msg = readWord(pos)
            pos += 2
            msg_text = getString(msg)
            lines.append('{:04X}: 04 {:02X} {:02X}  ;{}    "{}","{}"{}'.format(
                pos - 3 + CON['origin'], binary[pos - 2], binary[pos - 1], lev_pad, script_names[com - 1], msg_text, last))

        elif com == 7:
            slen = binary[pos]
            npos = pos + slen
            pos += 1
            lines.append('{:04X}: {:02X} {:02X}     ;{}    "{}",['.format(
                pos - 2 + CON['origin'], com, slen, lev_pad, script_names[com - 1]))
            processScript(pos, npos, level + 1, lines)
            g = lines[-1]
            lines[-1] = g[:-1] + '],'
            pos = npos

        elif com == 0x0D or com == 5 or com == 9 or com == 8 or com == 0x0F or com == 0x10 or com == 0x14 or com == 0x0E or com == 0x16 or com == 0x17 or com == 0x1D or com == 0x1C or com == 0x1B:
            lines.append('{:04X}: {:02X}        ;{}    "{}"{}'.format(
                pos - 1 + CON['origin'], com, lev_pad, script_names[com - 1], last))

        elif com == 0x15:
            o = binary[pos]
            obj = getObject(o)
            pos += 1
            r = binary[pos]
            room = getRoom(r)
            pos += 1
            lines.append('{:04X}: {:02X} {:02X} {:02X}  ;{}    "{}","{}","{}"{}'.format(
                pos - 3 + CON['origin'], binary[pos - 3], binary[pos - 2], binary[pos - 1], lev_pad, script_names[com - 1], obj, room, last))

        elif com == 0x19:
            o = binary[pos]
            obj = getObject(o)
            pos += 1
            c = binary[pos]
            con = getObject(c)
            pos += 1
            lines.append('{:04X}: {:02X} {:02X} {:02X}  ;{}    "{}","{}","{}"{}'.format(
                pos - 3 + CON['origin'], binary[pos - 3], binary[pos - 2], binary[pos - 1], lev_pad, script_names[com - 1], obj, con, last))

        else:
            raise Exception('Unknown command {:02X}'.format(com))


def processScriptList(pos):

    lines = []
    while binary[pos] != 0:
        w = binary[pos]
        pos = pos + 1
        word = getVerb(w)
        leng = binary[pos]
        npos = pos + leng
        pos = pos + 1
        g = '{:04X}: {:02X} {:02X}'.format(pos - 2 + CON['origin'], w, leng)
        g = padTo(g, 16) + '; "' + word['text'] + '" : ['
        lines.append(g)
        processScript(pos, npos, 0, lines)
        g = lines[-1]
        lines[-1] = g[:-1] + '],'
        pos = npos

    return lines


def findRoomOfScript(pos):
    pos = pos + CON['origin']
    for room in rooms:
        if room['script'] == pos:
            return room
    return None


def printRooms():
    pos = CON['RoomScripts']
    while binary[pos] != 0xFF:
        room = findRoomOfScript(pos)

        # room_1 : {
        #   desc : "YOU ARE STANDING BEFORE THE ENTRANCE OF A PYRAMID. AROUND YOU IS A DESERT.",
        #   lit  : true,
        #   commands : {

        print('; "room_{}" : '.format(room['number']) + '{')
        print(';     "desc" : "' + getString(room['desc']) + '",')
        print(';     "commands" : {')

        lines = processScriptList(pos)
        for lin in lines:
            print(lin)

        pos = int(lin[0:4], 16) - CON['origin']
        lin = lin[5:lin.index(';')].strip().replace(' ', '')
        pos += int(len(lin) / 2)
        print('{:04X}: 00'.format(pos + CON['origin']))
        pos += 1

        print(';     }')
        print('; },')
        print()


printRooms()

#lines = processScriptList(CON['GeneralCommand'])
# for lin in lines:
#    print(lin)
