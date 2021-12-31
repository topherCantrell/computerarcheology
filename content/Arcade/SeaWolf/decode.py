

with open('content/arcade/seawolf/roms/seawolf.bin','rb') as f:
    data = f.read()

i = data.find(b'BONUS')
print(i)
print(data)

raise Exception('oops')

c = 0
for pos in range(0x0D3D,0x1000):
    g = bin(data[pos])[2:].rjust(8,'0')
    g = g.replace('0','.')
    addr = hex(pos)[2:].rjust(4,'0').upper()
    b = hex(data[pos])[2:].rjust(2,'0').upper()
    pos+=1
    c+=1
    if c==11:
        print()
        c=1
    print(addr+': '+b+'  ; '+g)
