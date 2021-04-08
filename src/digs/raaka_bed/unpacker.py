
UNPACK = [
#'11EC: 10 8E 12 A4         LDY     #$12A4                    ; 3 byte buffer for decode',
#'11F0: C6 03               LDB     #$03                      ; 3 characters ...',
#'11F2: F7 12 A1            STB     $12A1                     ; ... to unpack',
#'11F5: A6 80               LDA     ,X+                       ; Hold ...',
#'11F7: B7 01 DE            STA     $01DE                     ; {ram:tmp1DE} ... first byte', 
#'11FA: A6 80               LDA     ,X+                       ; Hold ...',
#'11FC: B7 01 DD            STA     $01DD                     ; {ram:tmp1DD} ... second byte', 
#'11FF: 31 23               LEAY    3,Y                       ; Start at the end of the buffer',
'1201: CE 00 28            LDU     #$0028                    ;',
'1204: FF 12 A2            STU     $12A2                     ; ',
'1207: 86 11               LDA     #$11                      ;',
'1209: B7 01 DA            STA     $01DA                     ; {ram:tmp1DA}', 
'120C: 7F 01 DB            CLR     $01DB                     ; {ram:tmp1DB} ',
'120F: 7F 01 DC            CLR     $01DC                     ; {ram:tmp1DC} ',
'1212: 79 01 DE            ROL     $01DE                     ; {ram:tmp1DE} ',
'1215: 79 01 DD            ROL     $01DD                     ; {ram:tmp1DD} ',
'1218: 7A 01 DA            DEC     $01DA                     ; {ram:tmp1DA} ',
'121B: 27 39               BEQ     $1256                     ; ',
'121D: 86 00               LDA     #$00                      ;',
'121F: 89 00               ADCA    #$00                      ; This algorithm is identical to the decompression',
'1221: 78 01 DC            ASL     $01DC                     ; {ram:tmp1DC} used in Pyramid2000. Check the comments there for',
'1224: 79 01 DB            ROL     $01DB                     ; {ram:tmp1DB} more detail.',
'1227: BB 01 DC            ADDA    $01DC                     ; {ram:tmp1DC} ',
'122A: B0 12 A3            SUBA    $12A3                     ; ',
'122D: B7 01 E0            STA     $01E0                     ; {ram:tmp1EO}', 
'1230: B6 01 DB            LDA     $01DB                     ; {ram:tmp1DB} ',
'1233: B2 12 A2            SBCA    $12A2                     ; ',
'1236: B7 01 DF            STA     $01DF                     ; {ram:tmp1DF}', 
'1239: 24 0B               BCC     $1246                     ; ',
'123B: FC 01 DF            LDD     $01DF                     ; {ram:tmp1DF}', 
'123E: F3 12 A2            ADDD    $12A2                     ; ',
'1241: FD 01 DB            STD     $01DB                     ; {ram:tmp1DB}', 
'1244: 20 06               BRA     $124C                     ; ',
'1246: FC 01 DF            LDD     $01DF                     ; {ram:tmp1DF}', 
'1249: FD 01 DB            STD     $01DB                     ; {ram:tmp1DB} ',
'124C: 25 04               BCS     $1252                     ; ',
'124E: 1A 01               ORCC    #$01                      ;',
'1250: 20 C0               BRA     $1212                     ; ',
'1252: 1C FE               ANDCC   #$FE                      ;',
'1254: 20 BC               BRA     $1212                     ; ',
'1256: FC 01 DB            LDD     $01DB                     ; {ram:tmp1DB}', 
'1259: C3 12 79            ADDD    #$1279                    ;',
#'125C: 1F 03               TFR     D,U                       ;',
#'125E: A6 C4               iLDA     ,U                        ;',
#'1260: A7 A2               iSTA     ,-Y                       ;',
'1262: 7A 12 A1            DEC     $12A1                     ; ',
'1265: 26 9A               BNE     $1201                     ; ',
'1267: 10 8E 12 A4         LDY     #$12A4                    ;',
#'126B: C6 03               LDB     #$03                      ;',
#'126D: A6 A0               LDA     ,Y+                       ;',
#'126F: BD 11 84            JSR     $1184                     ; {PrintCharacterAutoWrap} Print character',
#'1272: 5A                  DECB                              ;',
#'1273: 26 F8               BNE     $126D                     ; ',
#'1275: FC 01 AB            LDD     $01AB                     ; {ram:tmp1AB}', 
#'1278: 39                  RTS                               ;',
]

def goto(pc):
    pc = hex(pc).upper()[2:].rjust(4,'0')+':'
    for g in UNPACK:
        if g.startswith(pc):
            g = g[25:50].strip()
            i = g.find(' ')
            if i<0:
                return [g]
            else:
                return [g[:i],g[i+1:].strip()]            
    return None

CHARMAP = '?!2 "\'<>/03ABCDEFGHIJKLMNOPQRSTUVWXYZ-,.'
        
def unpack_bytes(a,b):
    reg = {}
    cf = 0
    zf = 0
    pc = 0x1201
    mem = {}
    mem[0x12A1] = 3    
    mem[0x01DE] = a
    mem[0x01DD] = b
    ret = []
    while True:
        g = goto(pc)
        #print(hex(pc),g,reg,mem,cf,zf)
        
        
        if g[0]=='LDY':
            # SPECIAL
            #print(ret)
            return CHARMAP[ret[2]]+CHARMAP[ret[1]]+CHARMAP[ret[0]]        
        
        
        elif g[0]=='DEC' and g[1].startswith('$'):
            addr = int(g[1][1:],16)
            m = mem[addr]
            m = m -1
            if m==-1:
                m = 255
            if m==0:
                zf = 1
            else:
                zf = 0
            mem[addr] = m
            pc+=3 
        
        
        
        elif g[0].startswith('LD') and g[0][2]=='A':              
            if g[1].startswith('#'):
                reg['A'] = int(g[1][2:],16)
                pc += 2
            elif g[1].startswith('$'):
                reg['A'] = mem[int(g[1][1:],16)]
                pc += 3
            else:
                raise Exception('Not implemented '+str(g))
        elif g[0].startswith('ST') and g[0][2]=='A' and g[1][0]=='$':
            mem[int(g[1][1:],16)] = reg['A']
            pc += 3            
            
        elif g[0]=='LDU' and g[1][0]=='#':
            reg['U'] = int(g[1][2:],16)
            pc+=3
        elif g[0]=='STU' and g[1][0]=='$':
            addr = int(g[1][1:],16)
            mem[addr] = int(reg['U']/256)
            mem[addr+1] = reg['U']&255
            pc += 3
            
        elif g[0]=='CLR' and g[1].startswith('$'):
            mem[int(g[1][1:],16)] = 0
            pc += 3
            
        elif g[0]=='ROL' and g[1].startswith('$'):
            addr = int(g[1][1:],16)
            m = mem[addr]
            m = m * 2
            if cf:
                m = m + 1
            if m>255:
                cf = 1
            else:
                cf = 0
            m = m & 255
            mem[addr]=m
            if m==0:
                zf = 1
            else:
                zf = 0
           
            pc += 3
        elif g[0]=='ASL' and g[1].startswith('$'):
            addr = int(g[1][1:],16)
            m = mem[addr]
            m = m * 2
            if m>255:
                cf = 1
            else:
                cf = 0
            m = m & 255
            mem[addr] = m        
            pc+=3    
        
        elif g[0]=='SBCA' and g[1].startswith('$'):
            v = mem[int(g[1][1:],16)]
            reg['A'] -= v
            if cf:
                reg['A'] -=1            
            if reg['A'] < 0:
                cf = 1
                reg['A']+=256
            else:
                cf = 0            
            pc += 3            
        elif g[0]=='ADCA' and g[1].startswith('#'):
            v = int(g[1][2:],16)
            reg['A'] += v
            if cf:
                reg['A'] += 1
            if reg['A'] > 255:
                cf = 1
            else:
                cf = 0
            reg['A'] = reg['A'] & 255
            pc += 2    
        elif g[0]=='ADDA' and g[1].startswith('$'):
            v = mem[int(g[1][1:],16)]
            reg['A'] += v            
            if reg['A'] > 255:
                cf = 1
            else:
                cf = 0
            reg['A'] = reg['A'] & 255
            pc += 3
        elif g[0]=='SUBA' and g[1].startswith('$'):
            v = mem[int(g[1][1:],16)]
            reg['A'] -= v            
            if reg['A'] < 0:
                cf = 1
                reg['A']+=256
            else:
                cf = 0            
            pc += 3
        
        elif g[0]=='LDD' and g[1].startswith('$'):
            v = int(g[1][1:],16)
            reg['A'] = mem[v]
            reg['B'] = mem[v+1]
            pc+=3
        elif g[0]=='STD' and g[1].startswith('$'):
            v = int(g[1][1:],16)
            dv = reg['A']*256 + reg['B']
            mem[v] = int(dv/256)
            mem[v+1] = dv&255
            pc += 3
            
        elif g[0]=='ADDD' and g[1].startswith('$'):
            addr = int(g[1][1:],16)
            va = mem[addr]*256 + mem[addr+1]
            dv = reg['A']*256 + reg['B']            
            dv += va
            if dv>65535:
                cf = 1
            else:
                cf = 0
            dv = dv & 0xFFFF
            reg['A'] = int(dv/256)
            reg['B'] = dv & 255
            pc += 3
        elif g[0]=='ADDD' and g[1].startswith('#'):
            # SPECIAL PROCESSING
            ret.append(reg['B'])
            pc = 0x1262
                    
        elif g[0]=='ORCC':
            cf = 1
            pc += 2
        elif g[0]=='ANDCC':
            cf = 0
            pc+=2
            
        
        elif g[0]=='BEQ' and g[1].startswith('$'):
            if zf:
                pc = int(g[1][1:],16)
            else:
                pc += 2
        elif g[0]=='BNE' and g[1].startswith('$'):
            if not zf:
                pc = int(g[1][1:],16)
            else:
                pc += 2
        elif g[0]=='BRA' and g[1].startswith('$'):
            pc = int(g[1][1:],16)    
        elif g[0]=='BCS' and g[1].startswith('$'):
            if cf:
                pc = int(g[1][1:],16)
            else:
                pc += 2
        elif g[0]=='BCC' and g[1].startswith('$'):
            if not cf:
                pc = int(g[1][1:],16)
            else:
                pc += 2
        
                   
        else:
            print(g)
            raise 'Stop'
        
def decode_message(msg):
    pos = 0
    ret = ''
    while pos<=(len(msg)-2):
        a = msg[pos]
        b = msg[pos+1]
        pos += 2
        m = unpack_bytes(a,b)
        ret = ret + m
    while pos<len(msg):
        ret = ret + chr(msg[pos])
        pos += 1
    return ret
        
if __name__ == '__main__':

    msg = [
        0x5F, 0xBE, 0x3B, 0x16, 0xD3, 0x93, 0x37, 0x6E, 0xD1, 0xB5, 0x97, 
        0xC6, 0x51, 0x18, 0x4F, 0xC2, 0x66, 0xC6, 0x9B, 0x15, 0x5B, 0xCA, 0xE4,
        0xB3, 0x66, 0x4D, 0xD6, 0x15, 0x82, 0x17, 0x59, 0x5E, 0x00, 0xB3, 0xD9 ,
        0x6A, 0x39, 0x4A 
        ] 
    
    msg2 = [
        0x5F, 0xBE, 0x3B, 0x16, 0xD3, 0x93, 0x4B, 0x7B, 0x48, 0x55, 0x2F,
        0x62, 0x19, 0x58, 0x82, 0x7B, 0x7B, 0x17, 0xD3, 0xB2, 0x13, 0xB8, 0x8E,
        0x48, 0x51, 0x18, 0x45, 0xC2, 0x85, 0x48, 0x14, 0xBC, 0x86, 0x5F, 0xD6,
        0x15, 0x2E
        ]
    
    msg3 = [
        0x50, 0xB8, 0xCB, 0x87, 0x6B, 0xBF, 0x5F, 0xBE, 0xA3, 0x15, 0x33,
        0x8E, 0x83, 0x7A, 0x5F, 0xBE, 0x57, 0x17, 0x1F, 0xB3, 0xB5, 0x9A, 0xD5,
        0xB5, 0x0E, 0x53, 0x44, 0xDB, 0x93, 0x9E, 0x21
        ]
    
    m = decode_message(msg)
    
    print(m)