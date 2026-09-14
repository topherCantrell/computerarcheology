origin = 0xC000

with open('content/coco/doubleback/roms/doubleback.bin','rb') as f:
    data = f.read()

def hex2(v):
    return hex(v)[2:].rjust(2,'0').upper()

def hex4(v):
    return hex(v)[2:].rjust(4,'0').upper()

DTAB = [
    ' N','NE',' E','SE',' S','SW',' W','NW'
]

pos = 0xCEC3 - origin
while True:
    a = data[pos]
    b = data[pos+1]
    pos += 2
    if a==0 and b==0:
        break
    print(hex4(pos+origin-2)+': '+hex2(a)+' '+hex2(b),end='')
    a = bin(a)[2:].rjust(8,'0')
    b = bin(b)[2:].rjust(8,'0')
    c = a+b
    print('   ; '+c[0]+' '+c[1:4]+' '+c[4:7]+' '+c[7:10]+' '+c[10:13]+' '+c[13:16],end='')
    aa = int(c[13:16],2)
    bb = int(c[10:13],2)
    cc = int(c[7:10],2)
    dd = int(c[4:7],2)
    ee = int(c[1:4],2)
    print('   '+DTAB[aa]+' '+DTAB[bb]+' '+DTAB[cc]+' '+DTAB[dd]+' '+DTAB[ee])

