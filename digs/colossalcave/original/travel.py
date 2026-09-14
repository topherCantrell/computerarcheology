import sections
import words
import rooms
import messages

TRAVEL = {}

org_data = sections.SECTIONS[3]

for record in org_data:
    info = record.split('\t')
    source_room = int(info[0])
    d = info[1].rjust(10,'0')  # cccccccddd
    dest_cond = int(d[:7])
    dest_room = int(d[7:])
    verbs = info[2:]

    all_words = []
    for w in verbs:
        w = int(w)
        wds = words.WORDS.get(w,[f'??{w}??'])        
        # for ww in wds:
        #    all_words.append(ww)
        all_words.append(wds)
    
    if source_room not in TRAVEL:
        TRAVEL[source_room] = []
    TRAVEL[source_room].append((dest_room, dest_cond, all_words))

for rn in range(1,0x50):
    if rn not in TRAVEL:
        print(f'Room {rn} not found in TRAVEL dictionary.')
        continue
    desc = rooms.ROOMS[rn]['long']
    trav = TRAVEL[rn]
    print(f'---------------- #{rn} ----------------')
    print('\n'.join(desc))
    next_else = False    
    for dest, cond, all_words in trav:       
        if dest >= 300:
            dest_txt = f'.s{dest}'            
        else:
            dest_txt = f'.{int(dest)}'
        dest_txt = dest_txt.ljust(5)        

        words_txt = f'{all_words}'
        if words_txt.startswith('[['):
            words_txt = words_txt[1:-1]
        if words_txt == "['??1??']":
            words_txt = 'go'
        print(f'    {dest_txt}  <---- {words_txt}')
    print('')



