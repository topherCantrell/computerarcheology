
with open("../../../content/arcade/timepilot/roms/TM7",mode='rb') as file:
    data = file.read()
    
mus_ptr = 0xB82
mus_ptr = 0xBB2
mus_ptr = 0xBE2
mus_ptr = 0xC08

mus_ptr = 0xC2E
mus_ptr = 0xC70
mus_ptr = 0xCAD
mus_ptr = 0xCEB
mus_ptr = 0xD04

mus_ptr = 0xD46

def hex_str(value,n=2):
    s = hex(value)[2:]
    while len(s)<n:
        s = '0'+s
    return s.upper()

BASE_NOTE_PTRS = [
    ['02EE', 'G#1', 0],
    ['02F2', 'A#1', 2],
    ['02F6', 'C2',  4],
    ['02FA', 'D2',  6],
    ['02FE', 'E2',  8],
    ['0302', 'F#2', 10],
    ['0306', 'G#2', 12],
    ['030A', 'A#2', 14],
    ['030E', 'C3',  16],
    ['0312', 'D3',  18],
    ['0316', 'E3',  20],
    ['031A', 'F#3', 22],
    ['031E', 'G#3', 24],
    ['0322', 'A#3', 26],
    ['0326', 'C4',  28],
    ['032A', 'D4',  30]    
]    
    
NOTES = ['LOW','A1','A#1','B1',
         'C2','C#2', 'D2', 'D#2','E2','F2','F#2','G2','G#2','A2','A#2','B2', 
         'C3','C#3', 'D3', 'D#3','E3','F3','F#3','G3','G#3','A3','A#3','B3',
         'C4','C#4', 'D4', 'D#4','E4','F4','F#4','G4','G#4','A4','A#4','B4',
         'C5','C#5', 'D5', 'D#5','E5','F5','F#5','G5','G#5','A5','A#5','B5',
         'C6','C#6', 'D6', 'D#6','E6','F6','F#6','HIGH']

base_note = None
base_note_name = None

while True:
    
    p = mus_ptr
    
    cmd = int(data[mus_ptr]);mus_ptr+=1    
    
    delay = cmd>>5
    note = cmd & 0x1F
    
    if note==0x1F:
        if delay==0:
            b = data[mus_ptr];mus_ptr+=1
            base = BASE_NOTE_PTRS[b]
            base_note_name = base[1]
            base_note = base[2]            
            print("%s: %s %s ; MusCmd0: Set base note pointer to %s (%s)" %
                  (hex_str(p,4),hex_str(cmd),hex_str(b),base[0],base[1]))            
        elif delay==1:
            b = data[mus_ptr];mus_ptr+=1 
            print("%s: %s %s ; MusCmd1: Set base delay to %s" %
                  (hex_str(p,4),hex_str(cmd),hex_str(b),hex_str(b)))
        elif delay==2:
            b = data[mus_ptr];mus_ptr+=1 
            print("%s: %s %s ; MusCmd2: Set initial note volume to %s" %
                  (hex_str(p,4),hex_str(cmd),hex_str(b),hex_str(b)))
        elif delay==3:
            b = data[mus_ptr];mus_ptr+=1 
            bv = b
            if bv>127:
                bv = bv - 256
            print("%s: %s %s ; MusCmd3: Set volume modification to %s" %
                  (hex_str(p,4),hex_str(cmd),hex_str(b),bv))
            
        elif delay==5:
            b = data[mus_ptr];mus_ptr+=1            
            print("%s: %s %s ; MusCmd5: ??? %s" %
                  (hex_str(p,4),hex_str(cmd),hex_str(b),hex_str(b)))
        elif delay==6:
            b = data[mus_ptr];mus_ptr+=1
            c = data[mus_ptr];mus_ptr+=1
            print("%s: %s %s %s ; MusCmd6: GOTO %s" %
                  (hex_str(p,4),hex_str(cmd),hex_str(b),hex_str(c),
                   hex_str((c<<8) | b,4) ))
            break
        elif delay==7:
            print("%s: %s    ; END" %
                  (hex_str(p,4),hex_str(cmd)))
            break
        else:
            print("Unknown music "+str(delay))
            break          
                    
    else:
        if note==0:
            print("%s: %s    ; delay=%s, note=%s" % 
              (hex_str(p,4), hex_str(cmd),str(delay),'rest') )
        else:
            print("%s: %s    ; delay=%s, note=%s+%s: %s" % 
                  (hex_str(p,4), hex_str(cmd),str(delay),
                   base_note_name,str(note-1),
                   NOTES[base_note+note-1]))        

"""
TM1 C3 B1 07 FF ... F1 F1 F1 F1
TM2 F1 F1 F1 F1 ... A7 CA 0B 40
TM3 3C 20 05 CD ... FF 00 00 01
TM4 00 11 33 67 ... 00 00 00 00
TM5 00 00 00 00 ... 00 00 00 00
TM6 88 99 99 99 ... 0F 8F EF FF
TM7 21 00 30 06 ... FF FF FF FF

Sound = TM7
""" 