

origin = 0xC000

with open('../../../../content/coco/doubleback/roms/doubleback.bin','rb') as f:
    data = f.read()

def hex2(v):
    return hex(v)[2:].rjust(2,'0').upper()

def hex4(v):
    return hex(v)[2:].rjust(4,'0').upper()

rep = ['','','','','','','','']
def extract_image(pos):
    pos -= origin
    image = list(data[pos:pos+16])
    bits = []
    for i in range(0,16,2):
        row = ''
        for j in range(2):
            a = image[i+j]
            a = bin(a)[2:].rjust(8,'0')
            row += a
        bits.append(row)
    for i in range(8):
        d = bits[i]
        addr = origin+pos+i*2
        a = image[i*2]
        b = image[i*2+1]
        g = hex4(addr)+': '+hex2(a)+' '+hex2(b)+' ; '        
        for j in range(0,16,2):
            a = int(d[j:j+2],2)
            if(a):
                g = g + str(a)
                rep[i] += str(a)
            else:
                g = g + '.'     
                rep[i] += '.'       
        print(g)

start = 0xCE23
length = 10

for i in range(length):
    extract_image(start+i*16)
    print()

a = '\n'.join(rep)
print(a)
print()
a = a.replace('3','.')
print(a)