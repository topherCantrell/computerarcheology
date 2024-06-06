data = """3B60:
1F 7C F0 01 C0 
07 7F FC F0 07 C0 1F FF FC 03 F0 
0F C0 3F FC 1F F0 07 FE 3F F8 0F FF FF FC 1F FF 
FC 1F FC 1F F0 7F F0 7F C0 FF 01 C0 FF 01 00 FF 
07 00 FF 07 FC 1F FC 1F F0 7F F0 7F C0 FF 01 C0 
FF 01 00 FF 07 FF 07 FC 1F F8 0F F0 C0 03 FF FF 
03 E0 03 E0 0F 80 0F 00 3C 00 1E 3F 00 FC F0 00 
7F FE 00 F0 03 E0 00 00 0F 80 00 00 3F 00 FE 30 
00 06 FF 00 F8 00 00 03 E0 00 E0 08 20 04 C0 01 
E0 03 F8 0F 07 E0 3F 03 FF FF FF 3F FC FF F8 FF 
FF 07 E0 1F F0 FF FC FF 07 1E FC 1F 1F 7F FF FF 

;**************************************************
;bird character block shapes table (using character set B)
3C00:
E8 00 E9 00 C4 C6 C5 C7 EA 00 EB 00 00 00       ;bird shape #24

3C0E:
EC 00 E9 00 C8 CA C9 CB EA 00 ED 00 00 00       ;#28

3C1C:
EE 00 EF 00 CC CF CD D0 CE D1 F0 00 F1 00       ;#29

3C2A:
F2 00 EF 00 D2 00 D3 D5 D4 D6 F0 00 F3 00       ;#30

3C38:
E8 00 E9 00 C4 C6 C5 C7 00 00                   ;#24 without right wing

3C42:
EC 00 E9 00 C8 CA C9 CB 00 00                   ;#28 without right wing

3C4C:
EE 00 EF 00 CC CF CD D0 DD D1                   ;#29 without right wing and regrowing ($DD)

3C56:
F2 00 EF 00 D2 00 D3 D5 DD D6                   ;#30 without right wing and regrowing ($DD)

3C60:
00 00 00 00 C4 C6 C5 C7 EA 00 EB 00 00 00       ;#24 without left wing

3C6E:
00 00 00 00 DB CA C9 CB EA 00 ED 00 00 00       ;#28 without left wing and regrowing ($DB)

3C7C:
00 00 00 00 DC CF CD D0 CE D1 F0 00 F1 00       ;#29 without left wing and regrowing ($DC)

3C8A:
00 00 00 00 00 00 D3 D5 D4 D6 F0 00 F3 00       ;#30 without left wing

3C98:
00 00 00 00 C4 C6 C5 C7 00 00                   ;#24 without left and right wing

3CA2:
00 00 00 00 DB CA C9 CB 00 00                   ;#28 without left and right wing and regrowing ($DB)

3CAC:
00 00 00 00 DC CF CD D0 DD D1                   ;#29 without left and right wing and regrowing ($DC,$DD)

3CB6:
00 00 00 00 00 00 D3 D5 DD D6                   ;#30 without left and right wing and regrowing ($DD)

3CC0:
00 00 DE E2 AB B2 AC B3 DF E3 00 00             ;#21

3CCC:
00 00 00 E5 B4 B6 B5 B7 E4 E6 00 00             ;#25

3CD8:
00 00 00 00 B8 BB B9 BC BA BD 00 00             ;#26

3CE4:
00 00 00 00 BE C1 BF C2 C0 C3 00 E7             ;#27

3CF0:
FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF ;not used

3D00:
00 00 FA FC D7 D9 D8 DA FB FD 00 00             ;#22

3D0C:
F4 F6 F5 00 C4 C6 C5 C7 F7 00 F8 F9             ;#23

3D18:
00 00 00 00 A7 A9 A8 AA 00 00                   ;#17

3D22:
00 00 00 00 AB AD AC AE 00 00                   ;#18

3D2C:
00 00 DE 00 AB B0 AC B1 DF 00                   ;#19

3D36:
00 00 DE E0 AB B2 AC B3 DF E1                   ;#20

3D40:
00 00 9D 00 9E 00 00 00                         ;#12

3D48:
00 00 9F 00 A0 00 00 00                         ;#13

3D50:
00 00 00 00 9C 00 00 00                         ;#11

3D58:
00 00 00 00 A3 A5 A4 A6                         ;#16

3D60:
00 00 9C 00 00 00                               ;#11 one pos moved to the left

3D66:
00 00 9D 00 9E 00                               ;#12 (but 3x2)

3D6C:
00 00 9F 00 A0 00                               ;#13

3D72:
00 00 A1 00 A2 00                               ;#14

3D78:
00 00 96 00 00 00                               ;#7

3D7E:
00 00 97 00 93 00                               ;#8

3D84:
00 00 98 00 99 00                               ;#9

3D8A:
00 00 9A 00 9B 00                               ;#10

3D90:
00 00 90 00 00 00                               ;#3

3D96:
00 00 91 00 00 00                               ;#4

3D9C:
00 00 92 00 93 00                               ;#5

3DA2:
00 00 94 00 95 00                               ;#6

3DA8:
00 00 01 00                                     ;like small star

3DAC:
00 00 08 00                                     ;like medium star

3DB0:
00 00 0A 00                                     ;like big star

3DB4:
00 00 0B 00 0C 0C 0E FF                         ;group of stars

3DBC:
0D 0E 0D FF                                     ;group of stars

;**************************************************
;command buffer table ?
3DC0:
06 70 
07 70 
08 70 
08 70 
08 70 
07 78 
06 80 
05 88 
04 90 
03 98 
02 A0 
01 A8 
02 70 
03 70 
04 70 
05 70 

;**************************************************
; sinus motion like, y pos table used by big birds
3DE0:
40 40 40 40 40 40 40 34 2C 26 20 1C 18 14 12 0F 
0D 0B 09 08 07 06 05 04 03 02 02 02 02 02 02 02 
01 02 04 08 10 20 40 80 

;**************************************************
;address table for bird character block shapes (grouped by animation pattern)
3E08:
3D A8 ;like small star                  2x2
3D AC ;like medium star                 2x2
3D B0 ;like big star                    2x2

3D B4 ;group of stars

;growing up
3D 90 ;#3                               3x2
3D 96 ;#4                               3x2
3D 9C ;#5                               3x2
3D A2 ;#6                               3x2
3D 78 ;#7                               3x2
3D 7E ;#8                               3x2
3D 84 ;#9                               3x2
3D 8A ;#10                              3x2
3D 60 ;#11 one pos moved to the left    3x2
3D 66 ;#12 (but 3x2)                    3x2
3D 6C ;#13                              3x2
3D 72 ;#14                              3x2

3D 40 ;#12                              4x2
3D 48 ;#13                              4x2
3D 50 ;#11                              4x2
3D 58 ;#16                              4x2

3D 18 ;#17                              5x2
3D 22 ;#18                              5x2
3D 2C ;#19                              5x2
3D 36 ;#20                              5x2

3C C0 ;#21                              6x2
3D 00 ;#22                              6x2
3D 0C ;#23                              6x2

3C 00 ;#24                              7x2

;get smaller and move to left
3D 58 ;#16                              4x2
3D 50 ;#11                              4x2
3D 48 ;#13                              4x2
3D 40 ;#12                              4x2

;get smaller
3D 36 ;#20                              5x2
3D 2C ;#19                              5x2
3D 22 ;#18                              5x2
3D 18 ;#17                              5x2

;wings going down
3C 00 ;#24                              7x2
3D 0C ;#23                              6x2
3D 00 ;#22                              6x2
3C C0 ;#21                              6x2

;wings up and move to right
3C 00 ;#24                              7x2
3C 0E ;#28                              7x2
3C 1C ;#29                              7x2
3C 2A ;#30                              7x2

;wings up and move to right
3C 38 ;#24 without right wing           5x2
3C 42 ;#28 without right wing           5x2
3C 4C ;#29 without right wing reg.      5x2
3C 56 ;#30 without right wing reg.      5x2

;wings up and move to right
3C 60 ;#24 without left wing            7x2
3C 6E ;#28 without left wing reg.       7x2
3C 7C ;#29 without left wing reg.       7x2
3C 8A ;#30 without left wing            7x2

;wings up and move to right
3C 98 ;#24 without left/right wing      5x2
3C A2 ;#28 without left/right wing reg  5x2
3C AC ;#29 without left/right wing reg  5x2
3C B6 ;#30 without left/right wing reg  5x2

;wings down and move to right
3C C0 ;#21                              6x2
3C CC ;#25                              6x2
3C D8 ;#26                              6x2
3C E4 ;#27                              6x2
"""

org = 0x3b60

def count_bytes(line):
    if ';' in line:
        line = line[:line.index(';')]
    line = line.strip()
    line = line.replace(' ','')
    return len(line) // 2

def hex4(n):
    return hex(n)[2:].upper().zfill(4)

lines = data.split("\n")
for line in lines:
    if not line.strip():
        print(line)
        continue
    if line.startswith(';'):
        print(line)
        continue
    if ':' in line:
        print(';',line)
        continue
    print(hex4(org)+': '+line.strip())
    org += count_bytes(line)
