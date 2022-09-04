
files = [
    'Bank00.md',
    'Bank01.md',
    'Bank02.md',
    'Bank03.md',
    'Bank04.md',
    'Bank05.md',
    'Bank06.md',
    'Bank07.md',
    'Bank08.md',
    'Bank09.md',
    'Bank0A.md',
    'Bank0B.md',
    'Bank0C.md',
    'Bank0D.md',
    'Bank0E.md',
    'Bank0F.md',
    'Bank10.md',
    'Bank11.md',
    'Bank12.md',
    'Bank13.md',
    'Bank14.md',
    'Bank15.md',
    'Bank16.md',
    'Bank17.md',
    'Bank18.md',
    'Bank19.md',
    'Bank1A.md',
    'Bank1B.md',
    'Bank1C.md',
    'Bank1D.md',
    'Bank1E.md',
    'Bank1F.md',
]

for fn in files:
    with open('../../content/gameboy/zelda/'+fn) as f:
        lines = f.readlines()

        # 7FEB: E0 F4           LDFF00  ($F4),A
        # 7FEB: E0 F4           LD      ($FF00+$F4),A

    for i in range(len(lines)):
        line = lines[i]        
        if 'LDFF00' in line:
            #print(line.strip())
            line = line.replace('LDFF00','LD')
            line = line.replace('($', '($FF00+$')
            #print(line.strip())
            lines[i] = line
        
        if ' STOP    $' in line:
            line = line.replace('STOP    $',';STOP    $')
            lines[i] = line

        if 'LDHL' in line:
            
            line = line.replace('LDHL    SP,','LD    HL,SP+')
            lines[i] = line

    with open('../../content/gameboy/zelda/'+fn,'w') as f:
        lines = f.writelines(lines)