ORIGIN = 0x800

DIVISORS = ["(/512)","(/256)","(/128)","(/64) ","(/32) ","(/16) ","(/8)  ","(/4)  ","(/2)  ","(/1)  "]
DIVVAL = [512.0, 256.0, 128.0, 64.0, 32.0, 16.0, 8.0, 4.0, 2.0, 1.0]

def padTo(s,length):
    while len(s)<length:
        s = s + " "
    return s

with open("VectorROM.mark") as f:
    raw = f.readlines()
    
for r in raw:
    r = r.strip()
    if not r.startswith("0") and not r.startswith("9"):
        print r
        continue
    
    i = ""
    if ";" in r:
        i = r[r.index(";"):].strip()
    first = r[0:17].strip()
    dat = [-1,-1,-1,-1]
    dat[0] = int(r[6:8],16)
    dat[1] = int(r[9:11],16)
    if(r[12]!=' '):
        dat[2] = int(r[12:14],16)
        dat[3] = int(r[15:17],16)
        
    com = (dat[1]>>4) & 0x0F
        
    if(com<10):
        vcom = "VEC"
        scale = (dat[1]>>4) & 0x0F
        bri = (dat[3]>>4) & 0x0F
        ys = ""
        if (dat[1]&4)>0:
            ys = "-"
        xs = ""
        if (dat[3]&4)>0:
            xs = "-"
        y = (dat[1]<<8 | dat[0]) & 0x3FF;
        x = (dat[3]<<8 | dat[2]) & 0x3FF;
        
        xn = x / DIVVAL[scale]
        yn = y / DIVVAL[scale]
        if(len(xs)>0):
            xn = -xn
        if(len(ys)>0):
            yn = -yn
        
        yv = padTo("%s%d" % (ys,y), 6)
        xv = padTo("%s%d" % (xs,x), 6)
        vcom = vcom + "  scale=%02d%s  bri=%02d  x=%s  y=%s (%4.2f, %4.2f)" % (scale,DIVISORS[scale],bri,xv,yv,xn,yn)        
        
    if(com==15):
        vcom = "SVEC"
        bri = (dat[0]>>4) & 0x0F
        scale = (((dat[0]>>3)&0x01)<<1) | ((dat[1]>>3)&1)
        ys = ""
        if (dat[1]&4)>0 :
            ys = "-"
        xs = ""
        if (dat[0]&4)>0 :
            xs = "-"
        y = dat[1]&3
        x = dat[0]&3
        
        xn = x / DIVVAL[scale]
        yn = y / DIVVAL[scale]
        if(len(xs)>0):
            xn = -xn
        if(len(ys)>0):
            yn = -yn
        
        yv = padTo("%s%d" % (ys,y), 6)
        xv = padTo("%s%d" % (xs,x), 6)
        vcom = vcom + " scale=%02d%s  bri=%02d  x=%s  y=%s (%4.2f, %4.2f)" % (scale,DIVISORS[scale],bri,xv,yv,xn,yn)      
        
    if(com==10):
        vcom = "LABS"
        scale = (dat[3]>>4) & 0x0F
        x = (dat[1]<<8 | dat[0]) & 0xFFF
        y = (dat[3]<<8 | dat[2]) & 0xFFF
        vcom = vcom + " scale=%02d%s  x=%d  y=%d" % (scale,DIVISORS[scale],x,y)
    if(com==11):
        vcom = "HALT"
    if(com==12):
        vcom = "JSR"
        loc = (dat[1]<<8 | dat[0]) & 0xFFF
        loc = (loc - ORIGIN)*2 + ORIGIN
        vcom = vcom + "  $%04X" % loc
    if(com==13):
        vcom = "RTS"
    if(com==14):
        vcom = "JMP"
        loc = (dat[1]<<8 | dat[0]) & 0xFFF
        loc = (loc - ORIGIN)*2 + ORIGIN
        vcom = vcom + "  $%04X" % loc
    
    
    while len(first)<20:
        first = first + " "
        
    while len(vcom)<50:
        vcom = vcom + " "
        
         
    print first + " "+ vcom + i