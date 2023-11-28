
with open('content/arcade/frogger/SoundCode.md') as f:
    lines = f.readlines()

SONGS = [
    ["47 0A","6A 0A","8D 0A", "Main song intro", 10], # 120
    ["34 10","CA 10","-",     "Main song", 12], # 180 (120)
    ["CE 0A","E7 0A","-",     "Game over", 15], # 240
    ["FB 0A","19 0B","-",     "Level complete", 12], # 180
    ["15 0C","-","-",         "New life begins", 14], # 180
    ["B5 0B","E6 0B","-", "F1", 13], # 180
    ["2A 0C","55 0C","-", "F2", 13],   
    ["7E 0C","BA 0C","-", "F3", 13],
    ["EE 0C","1A 0D","-", "F4", 13],
    ["43 0D","7B 0D","-", "F5", 13],
    ["9F 0D","D2 0D","-", "F6", 13],
    ["03 0E","5C 0E","-", "F7", 13],
    ["81 0E","B0 0E","-", "F8", 13],
    ["DD 0E","13 0F","-", "F9", 13],
    ["47 0F","78 0F","-", "F10", 13],
    ["A7 0F","E2 0F","-", "F11", 12],
    ["74 11","C7 11","-", "F12", 13],
    ["F1 11","17 12","-", "F13", 13],
    ["18 12","40 12","-", "F14", 13],
    ["66 12","92 12","-", "F15", 13],
    ["BE 12","DD 12","-", "F16", 13],
    ["F6 12","19 13","-", "F17", 13],
    ["3A 13","7A 13","-", "F18", 13],
    ["B8 13","EC 13","-", "F19", 13],
    ["1E 14","48 14","-", "F20", 13],
]

DUR_MAP = {
    "2^3":  "16",
    "2^4":  "8",
    "2^5":  "4",
    "2^6":  "2",
    "2^7":  "1",
}

def extract_song_data(spot):
    spot = spot[3:5]+spot[0:2]+":"
    pos = 0
    while not lines[pos].startswith(spot):
        pos += 1
    
    notes = ""
    first = True
    while ': FF' not in lines[pos]:
        g = lines[pos].strip()
        pos += 1
        if '; NOTE ' in g:
            if first:
                first = False
                continue
            i = g.find(';')
            g = g[i+2:]
            g = g.split(' ')
            octave = g[1][0]
            note = g[1][1:]
            dur = DUR_MAP[g[-1]]
            # print(note, octave, dur)
            notes = notes + f'{dur}{note}{octave} '
        elif '; REST ' in g:            
            i = g.find(';')
            g = g[i+2:]
            g = g.split(' ')
            dur = DUR_MAP[g[-1]]
            notes = notes + f'{dur}R '
    return notes

s = extract_song_data("34 10")
print(s)

# for home in SONGS[5:]:
#     # va = home[0]
#     vb = home[1]
#     s = extract_song_data(vb)    
#     print(s)
#     print("2R 16C2 C C C 2R ")