with open('content/trs80/xenos/roms/xenos.bin', 'rb') as f:
    data = f.read()
ORIGIN = 0x5D00

with open('content/trs80/xenos/Code.md', 'r') as f:
    lines = f.readlines()

def read_word_list(pos):
    ret = {}
    while len(lines[pos])>10:
        g = lines[pos][35:].strip()
        num = g[:2]
        word = g[5:]
        if num not in ret:
            ret[num] = []
        ret[num].append(word)
        pos += 1
    return ret

pos = 0
START_VERB = '762D'
START_NOUN = '790A'
START_ADJ = '7BBC'
START_PREP = '7CDB'
while not lines[pos].startswith(START_VERB):
    pos += 1
verbs = read_word_list(pos)

while not lines[pos].startswith(START_NOUN):
    pos += 1
nouns = read_word_list(pos)

while not lines[pos].startswith(START_ADJ):
    pos += 1
adjectives = read_word_list(pos)

while not lines[pos].startswith(START_PREP):
    pos += 1
prepositions = read_word_list(pos)

# print(verbs)
# print(nouns)
# print(adjectives)
# print(prepositions)

pos = 0x72E1

obits = 'uvCPA?OL'

def print_phrase_line(pos):
    g = f"{pos:04X}: "
    for i in range(5):
        g += f"{data[pos-ORIGIN+i]:02X} "
    
    phrase_num = data[pos-ORIGIN+4]
    verb = verbs.get(f"{data[pos-ORIGIN]:02X}",['??'])[0]
    verb = verb.ljust(8)
    prepositions['00'] = ['*']
    prep = prepositions.get(f"{data[pos-ORIGIN+1]:02X}",['??'])[0]
    prep = prep.ljust(8)

    ob1 = data[pos-ORIGIN+2]
    ob2 = data[pos-ORIGIN+3]

    if ob1 ==0:
        ob1 = '*       '
    else:
        h = f'{ob1:08b}'
        ob1 = ''
        for i in range(8):
            if h[i] == '1':
                ob1 += obits[i]
            else:
                ob1 += '.'


    if ob2 ==0:
        ob2 = '   *    '
    else:
        h = f'{ob2:08b}'
        ob2 = ''
        for i in range(8):
            if h[i] == '1':
                ob2 += obits[i]
            else:
                ob2 += '.'


    g = g + f'    ; {phrase_num:02X}:  {verb} {ob1}   {prep} {ob2}'    
    print(g)

while data[pos-ORIGIN] != 0x00:
    print_phrase_line(pos)
    pos += 5