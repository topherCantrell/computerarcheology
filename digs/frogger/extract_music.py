from computerarcheology.tools import binary

data = binary.get_binary('content/arcade/frogger/SoundCode.md',0)

notes_raw = """08D3: 6B 08   ;   51.90 1G#
08D5: F2 07   ;   54.98 1A
08D7: 80 07   ;   58.25 1A#
08D9: 14 07   ;   61.72 1B
08DB: AE 06   ;   65.40 2C
08DD: 4E 06   ;   69.29 2C#
08DF: F3 05   ;   73.43 2D
08E1: 9E 05   ;   77.78 2D#
08E3: 4E 05   ;   82.36 2E
08E5: 01 05   ;   87.31 2F
08E7: B9 04   ;   92.51 2F#
08E9: 76 04   ;   97.94 2G
08EB: 36 04   ;  103.75 2G#
08ED: F9 03   ;  109.97 2A
08EF: C0 03   ;  116.50 2A#
08F1: 8A 03   ;  123.45 2B
08F3: 57 03   ;  130.81 3C
08F5: 27 03   ;  138.59 3C#
08F7: FA 02   ;  146.78 3D
08F9: CF 02   ;  155.56 3D#
08FB: A7 02   ;  164.72 3E
08FD: 81 02   ;  174.49 3F
08FF: 5D 02   ;  184.87 3F#
0901: 3B 02   ;  195.88 3G
0903: 1B 02   ;  207.51 3G#
0905: FD 01   ;  219.74 3A
0907: E0 01   ;  233.01 3A#
0909: C5 01   ;  246.90 3B
090B: AC 01   ;  261.32 4C
090D: 94 01   ;  276.85 4C#
090F: 7D 01   ;  293.56 4D
0911: 68 01   ;  310.68 4D#
0913: 53 01   ;  329.93 4E
0915: 40 01   ;  349.52 4F
0917: 2E 01   ;  370.35 4F#
0919: 1D 01   ;  392.44 4G
091B: 0D 01   ;  415.79 4G#
091D: FE 00   ;  440.34 4A
091F: F0 00   ;  466.03 4A#
0921: E3 00   ;  492.72 4B
0923: D6 00   ;  522.65 5C
0925: CA 00   ;  553.70 5C#
0927: BE 00   ;  588.67 5D
0929: B4 00   ;  621.37 5D#
092B: AA 00   ;  657.93 5E
092D: A0 00   ;  699.05 5F
092F: 97 00   ;  740.71 5F#
0931: 8F 00   ;  782.15 5G
0933: 87 00   ;  828.50 5G#
0935: 7F 00   ;  880.69 5A
0937: 78 00   ;  932.06 5A#
0939: 71 00   ;  989.80 5B
093B: 6B 00   ; 1045.3  6C
093D: 65 00   ; 1107.4  6C#
093F: 5F 00   ; 1177.3  6D
0941: 5A 00   ; 1242.7  6D#
0943: 55 00   ; 1315.8  6E
0945: 50 00   ; 1398.1  6F
0947: 4C 00   ; 1471.6  6F#
0949: 47 00   ; 1575.3  6G"""

NOTE_TABLE = []
notes_raw = notes_raw.split('\n')
for note in notes_raw:
    note_data = note.split(' ')
    base = note_data[0][:-1]
    name =  note_data[-1]
    NOTE_TABLE.append((int(base,16),name))    
print(NOTE_TABLE)

note_sets_raw = """08B3: D3 08  ; 1=1G# ... 30=4C#          
08B5: D7 08  ; 1=1A# ... 30=4D#
08B7: DB 08  ; 1=2C  ... 30=4F                      
08B9: DF 08  ; 1=2D  ... 30=4G                         
08BB: E3 08  ; 1=2E  ... 30=4A
08BD: E7 08  ; 1=2F# ... 30=4B
08BF: EB 08  ; 1=2G# ... 30=5C#
08C1: EF 08  ; 1=2A# ... 30=5D#                        
08C3: F3 08  ; 1=3C  ... 30=5F
08C5: F7 08  ; 1=3D  ... 30=5G
08C7: FB 08  ; 1=3E  ... 30=5A
08C9: FF 08  ; 1=3F# ... 30=5B
08CB: 03 09  ; 1=3G# ... 30=6C#
08CD: 07 09  ; 1=3A# ... 30=6D#
08CF: 0B 09  ; 1=4C  ... 30=6F
08D1: 0F 09  ; 1=4D  ... 30=6G"""

NOTE_SETS = []
note_sets_raw = note_sets_raw.split('\n')
for note_set in note_sets_raw:
    set_data = note_set.split(' ')    
    NOTE_SETS.append(int(set_data[2]+set_data[1],16))
print(NOTE_SETS)
    


#binary = code.markdown_utils.get_binary('../../../content/arcade/frogger/SoundCode.md')