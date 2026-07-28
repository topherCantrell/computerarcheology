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
        print(f'Room {rn:02X} not found in TRAVEL dictionary.')
        continue
    desc = rooms.ROOMS[rn]['long']
    trav = TRAVEL[rn]
    print(f'---------------- {rn:02X} ----------------')
    print('\n'.join(desc))
    next_else = False    
    for dest, cond, all_words in trav:
        msg = ''
        if dest > 500:
            dest_txt = f'mesg_{dest-500}'
            msg = ' '.join(messages.MESSAGES[dest-500])
        elif dest > 300:
            dest_txt = f'goto_{dest-300}'
        else:
            dest_txt = f'{int(dest):02X}'
        dest_txt = dest_txt.ljust(8)

        if cond == 0:
            if next_else:
                cond_txt = 'else'
                next_else = False
            else:
                cond_txt = '<---'
        elif cond < 100:
            cond_txt = f'{int(cond)}%'
            next_else = True
        elif cond == 100:
            next_else = True
            cond_txt = 'no dwvs'
        elif cond < 200:
            cond_txt = f'has {int(cond)-100}'
            next_else = True
        elif cond < 300:
            next_else = True
            cond_txt = f'available {int(cond)-200}'        
        elif cond < 400:
            next_else = True
            cond_txt = f'prop({int(cond)%100}) NOT 0'
        elif cond < 500:
            next_else = True
            cond_txt = f'prop({int(cond)%100}) NOT 1'
        elif cond < 600:
            next_else = True
            cond_txt = f'prop({int(cond)%100}) NOT 2'
        elif cond < 700:
            next_else = True
            cond_txt = f'prop({int(cond)%100}) NOT 3'
        elif cond < 800:
            next_else = True
            cond_txt = f'prop({int(cond)%100}) NOT 4'
        else:
            if cond>=700:
                raise "OOPS"
            cond_txt = f'{int(cond):03X}'       

        words_txt = f'{all_words}'
        if words_txt.startswith('[['):
            words_txt = words_txt[1:-1]
        print(f'    {dest_txt} {cond_txt} {words_txt} {msg}')
    print('')



