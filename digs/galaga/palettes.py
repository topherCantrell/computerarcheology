data = '''0000: 0F 08 0E 02 
0004: 0F 05 0B 0C 
0008: 0F 00 0B 01 
000C: 0F 01 0B 02
0010: 0F 08 0D 02 
0014: 0F 06 01 04 
0018: 0F 09 01 05 
001C: 0F 07 0B 01
0020: 0F 01 06 0B 
0024: 0F 01 0B 00 
0028: 0F 01 02 00 
002C: 0F 00 01 06
0030: 0F 00 00 06 
0034: 0F 03 0B 09 
0038: 0F 06 02 00 
003C: 00 00 00 00'''

colors = [
    "#DEDEDE",
    "#FF0000",
    "#FFFF00",
    "#FF9700",
    "#FFB800",
    "#FF00DE",
    "#00FFDE",
    "#B8B8DE",
    "#DE4700",
    "#00FF00",
    "#219700",
    "#0068DE",
    "#9700DE",
    "#0000DE",
    "#009797",
    "#000000",
    "#DEDEDE",
    "#FF0000",
    "#FFFF00",
    "#FF9700",
    "#000000",
    "#FF00DE",
    "#00FFDE",
    "#00B8DE",
    "#000000",
    "#00FF00",
    "#000000",
    "#0068DE",
    "#B800DE",
    "#0000DE",
    "#000000",
    "#000000",
]

data = data.split('\n')
cn = 0
for d in data:
    d = d.strip()
    e = d.split()
    
    c0 = colors[int(e[1], 16)]
    c1 = colors[int(e[2], 16)]
    c2 = colors[int(e[3], 16)]
    c3 = colors[int(e[4], 16)]

    cnn = hex(cn)[2:].upper()
    while len(cnn) < 2:
        cnn = '0' + cnn

    print(f'{d}    ; {cnn}:  `<FONT style="BACKGROUND-COLOR:{c0}">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:{c1}">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:{c2}">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:{c3}">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`')

    cn+=1
