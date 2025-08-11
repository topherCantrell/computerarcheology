![Asteroids DVG Vector ROM](Asteroids.jpg)

# Asteroids DVG Vector ROM

>>> cpu DVG

>>> binary 1000:roms/035127.02

OriginalBinary 035127.02 (Rev 2)

# Corrections 

Thanks to Sean D. Solle for pointing out mistakes in the disassembly for SVEC y= negative values.
Those have been corrected.

# TODO

Lots of info here about what the areas in the ROM are:
[http://arcarc.xmission.com/Tech/dvg.txt](http://arcarc.xmission.com/Tech/dvg.txt)

Thanks to [slx7R4GDZM](https://github.com/slx7R4GDZM) for many fixes and discoveries here.

# DVG Info

 For info about the vector generator hardware and opcodes:

[DVG Information](DVG.md)

# Test Pattern

Diamond pattern across screen with a parallel
line pattern in the center.

```html
<canvas width="520" height="520"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="1000"
  data-command="screenScale=0.5,1000">
</canvas>
```

```code
1000: 80 A0 00 00     LABS    scale=00(/512)           x=0       y=128
1004: 00 70 00 00     VEC     scale=07(/4)   bri=0     x=0       y=0       (0.0000, 0.0000)
1008: 00 90 FF 73     VEC     scale=09(/1)   bri=7     x=1023    y=0       (1023.0000, 0.0000)
100C: FF 92 00 70     VEC     scale=09(/1)   bri=7     x=0       y=767     (0.0000, 767.0000)
1010: 00 90 FF 77     VEC     scale=09(/1)   bri=7     x=-1023   y=0       (-1023.0000, 0.0000)
1014: FF 96 00 70     VEC     scale=09(/1)   bri=7     x=0       y=-767    (0.0000, -767.0000)
;
1018: FF 92 FF 72     VEC     scale=09(/1)   bri=7     x=767     y=767     (767.0000, 767.0000)
101C: 00 86 00 72     VEC     scale=08(/2)   bri=7     x=512     y=-512    (256.0000, -256.0000)
1020: FE 87 FE 77     VEC     scale=08(/2)   bri=7     x=-1022   y=-1022   (-511.0000, -511.0000)
1024: 00 92 00 76     VEC     scale=09(/1)   bri=7     x=-512    y=512     (-512.0000, 512.0000)
1028: FE 81 00 72     VEC     scale=08(/2)   bri=7     x=512     y=510     (256.0000, 255.0000)
102C: FF 96 FF 72     VEC     scale=09(/1)   bri=7     x=767     y=-767    (767.0000, -767.0000)
1030: 7F A3 FF 03     LABS    scale=00(/512)           x=1023    y=895
;
1034: 00 70 00 00     VEC     scale=07(/4)   bri=0     x=0       y=0       (0.0000, 0.0000)
1038: FF 96 FF 76     VEC     scale=09(/1)   bri=7     x=-767    y=-767    (-767.0000, -767.0000)
103C: FE 81 00 76     VEC     scale=08(/2)   bri=7     x=-512    y=510     (-256.0000, 255.0000)
1040: 00 92 00 72     VEC     scale=09(/1)   bri=7     x=512     y=512     (512.0000, 512.0000)
1044: FE 87 FE 73     VEC     scale=08(/2)   bri=7     x=1022    y=-1022   (511.0000, -511.0000)
1048: 00 86 00 76     VEC     scale=08(/2)   bri=7     x=-512    y=-512    (-256.0000, -256.0000)
104C: FF 92 FF 76     VEC     scale=09(/1)   bri=7     x=-767    y=767     (-767.0000, 767.0000)
1050: FC A1 F4 01     LABS    scale=00(/512)           x=500     y=508
;     
1054: 00 70 00 00     VEC     scale=07(/4)   bri=0     x=0       y=0       (0.0000, 0.0000)
1058: DB F0           SVEC    scale=02(*8)   bri=13    x=3       y=0       (24.0000, 0.0000)
105A: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
105C: CF F0           SVEC    scale=02(*8)   bri=12    x=-3      y=0       (-24.0000, 0.0000)
105E: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
1060: BB F0           SVEC    scale=02(*8)   bri=11    x=3       y=0       (24.0000, 0.0000)
1062: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
1064: AF F0           SVEC    scale=02(*8)   bri=10    x=-3      y=0       (-24.0000, 0.0000)
1066: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
1068: 9B F0           SVEC    scale=02(*8)   bri=9     x=3       y=0       (24.0000, 0.0000)
106A: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
106C: 8F F0           SVEC    scale=02(*8)   bri=8     x=-3      y=0       (-24.0000, 0.0000)
106E: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
1070: 7B F0           SVEC    scale=02(*8)   bri=7     x=3       y=0       (24.0000, 0.0000)
1072: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
1074: 6F F0           SVEC    scale=02(*8)   bri=6     x=-3      y=0       (-24.0000, 0.0000)
1076: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
1078: 5B F0           SVEC    scale=02(*8)   bri=5     x=3       y=0       (24.0000, 0.0000)
107A: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
107C: 4F F0           SVEC    scale=02(*8)   bri=4     x=-3      y=0       (-24.0000, 0.0000)
107E: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
1080: 3B F0           SVEC    scale=02(*8)   bri=3     x=3       y=0       (24.0000, 0.0000)
1082: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
1084: 2F F0           SVEC    scale=02(*8)   bri=2     x=-3      y=0       (-24.0000, 0.0000)
1086: 7C D0           RTS                         
```

# Bank Error 

```html
<canvas width="500" height="60"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="1000"
  data-command="x=20,y=45,baseScale=1,108C">
</canvas>
```

```code
; In Revision 1 of this ROM, the text is: "PAGE SELECT ERROR"

; "BANK ERROR"  In this Revision 2
1088: E4 A0 5E 11     LABS    scale=01(/256)           x=350     y=228
108C: 00 70 00 00     VEC     scale=07(/4)   bri=0     x=0       y=0       (0.0000, 0.0000)
1090: 80 CA           JSR     $0A80 ($1500)       ; 
1092: 78 CA           JSR     $0A78 ($14F0)       ; 
1094: D8 CA           JSR     $0AD8 ($15B0)       ; 
1096: C7 CA           JSR     $0AC7 ($158E)       ; 
1098: 2C CB           JSR     $0B2C ($1658)       ; 
109A: 9B CA           JSR     $0A9B ($1536)       ; 
109C: F3 CA           JSR     $0AF3 ($15E6)       ; 
109E: F3 CA           JSR     $0AF3 ($15E6)       ; 
10A0: DD CA           JSR     $0ADD ($15BA)       ; 
10A2: F3 EA           JMP     $0AF3 ($15E6)       ; 
```

# Credits 

```html
<canvas width="500" height="60"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="1000"
  data-command="x=20,y=45,baseScale=1,10B8">
</canvas>
```

```code
; In Revision 1 of this ROM the text is "ASTEROIDS BY ATARI"

; "c 1979 ATARI INC" In this Revision 2
10A4: 80 A0 90 01     LABS    scale=00(/512)           x=400     y=128
10A8: 00 70 00 00     VEC     scale=07(/4)   bri=0     x=0       y=0       (0.0000, 0.0000)
10AC: 73 F5           SVEC    scale=00(*2)   bri=7     x=3       y=-1      (6.0000, -2.0000)
10AE: 73 F1           SVEC    scale=00(*2)   bri=7     x=3       y=1       (6.0000, 2.0000)
10B0: 78 F1           SVEC    scale=02(*8)   bri=7     x=0       y=1       (0.0000, 8.0000)
10B2: 77 F1           SVEC    scale=00(*2)   bri=7     x=-3      y=1       (-6.0000, 2.0000)
10B4: 77 F5           SVEC    scale=00(*2)   bri=7     x=-3      y=-1      (-6.0000, -2.0000)
10B6: 78 F5           SVEC    scale=02(*8)   bri=7     x=0       y=-1      (0.0000, -8.0000)
10B8: 80 31 00 02     VEC     scale=03(/64)  bri=0     x=512     y=384     (8.0000, 6.0000)
10BC: 75 F8           SVEC    scale=01(*4)   bri=7     x=-1      y=0       (-4.0000, 0.0000)
10BE: 70 FD           SVEC    scale=01(*4)   bri=7     x=0       y=-1      (0.0000, -4.0000)
10C0: 71 F8           SVEC    scale=01(*4)   bri=7     x=1       y=0       (4.0000, 0.0000)
10C2: 02 FD           SVEC    scale=01(*4)   bri=0     x=2       y=-1      (8.0000, -4.0000)
10C4: 2E CB           JSR     $0B2E ($165C)       ; 
10C6: 63 CB           JSR     $0B63 ($16C6)       ; 
10C8: 56 CB           JSR     $0B56 ($16AC)       ; 
10CA: 63 CB           JSR     $0B63 ($16C6)       ; 
10CC: 2C CB           JSR     $0B2C ($1658)       ; 
10CE: 78 CA           JSR     $0A78 ($14F0)       ; 
10D0: 02 CB           JSR     $0B02 ($1604)       ; 
10D2: 78 CA           JSR     $0A78 ($14F0)       ; 
10D4: F3 CA           JSR     $0AF3 ($15E6)       ; 
10D6: BA CA           JSR     $0ABA ($1574)       ; 
10D8: 2C CB           JSR     $0B2C ($1658)       ; 
10DA: BA CA           JSR     $0ABA ($1574)       ; 
10DC: D8 CA           JSR     $0AD8 ($15B0)       ; 
10DE: 8D EA           JMP     $0A8D ($151A)       ; 

; Ship Explosion
10E0: C6 FF           SVEC    scale=01(*4)   bri=12    x=-2      y=-3      (-8.0000, -12.0000)
10E2: C1 FE           SVEC    scale=01(*4)   bri=12    x=1       y=-2      (4.0000, -8.0000)
10E4: C3 F1           SVEC    scale=00(*2)   bri=12    x=3       y=1       (6.0000, 2.0000)
10E6: CD F1           SVEC    scale=02(*8)   bri=12    x=-1      y=1       (-8.0000, 8.0000)
10E8: C7 F1           SVEC    scale=00(*2)   bri=12    x=-3      y=1       (-6.0000, 2.0000)
10EA: C1 FD           SVEC    scale=01(*4)   bri=12    x=1       y=-1      (4.0000, -4.0000)

; Ship explosion pieces velocity (x, y)
10EC: D8 1E ; (-40,  30)
10EE: 32 EC ; ( 50, -20)
10F0: 00 C4 ; (  0, -60)
10F2: 3C 14 ; ( 60,  20)
10F4: 0A 46 ; ( 10,  70)
10F6: D8 D8 ; (-40, -40)
```

# Shrapnel Patterns 

This is used when the player's shot hits something.

Notice that all four patterns are the same just slightly spread out. This is extremely
clever. You could use one pattern and vary the scale to make it look like it is
spreading out. But the scale jumps are powers-of-two. These slightly-scaled patterns
can be used to take up the gaps in the large scaling doubles!

```html
<canvas width="400" height="100"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="1000"
  data-command="baseScale=0,x=50,y=50,11A0,x=150,y=50,116A,x=250,y=50,112C,x=350,y=50,1100">
</canvas>
```

```code
; Jump table for 4
10F8: D0 C8           JSR     $08D0 ($11A0)       ; 
10FA: B5 C8           JSR     $08B5 ($116A)       ; 
10FC: 96 C8           JSR     $0896 ($112C)       ; 
10FE: 80 C8           JSR     $0880 ($1100)       ; 
;
; Shrapnel pattern 1
1100: 0D F8           SVEC    scale=03(*16)  bri=0     x=-1      y=0       (-16.0000, 0.0000)
1102: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1104: 0D FD           SVEC    scale=03(*16)  bri=0     x=-1      y=-1      (-16.0000, -16.0000)
1106: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1108: 09 FD           SVEC    scale=03(*16)  bri=0     x=1       y=-1      (16.0000, -16.0000)
110A: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
110C: 0B F1           SVEC    scale=02(*8)   bri=0     x=3       y=1       (24.0000, 8.0000)
110E: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1110: 0A F5           SVEC    scale=02(*8)   bri=0     x=2       y=-1      (16.0000, -8.0000)
1112: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1114: 08 F9           SVEC    scale=03(*16)  bri=0     x=0       y=1       (0.0000, 16.0000)
1116: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1118: 09 F3           SVEC    scale=02(*8)   bri=0     x=1       y=3       (8.0000, 24.0000)
111A: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
111C: 0D F3           SVEC    scale=02(*8)   bri=0     x=-1      y=3       (-8.0000, 24.0000)
111E: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1120: 80 54 00 06     VEC     scale=05(/16)  bri=0     x=-512    y=-128    (-32.0000, -8.0000)
1124: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1126: 0F F1           SVEC    scale=02(*8)   bri=0     x=-3      y=1       (-24.0000, 8.0000)
1128: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
112A: 00 D0           RTS                         
;
; Shrapnel pattern 2  
112C: 00 30 80 07     VEC     scale=03(/64)  bri=0     x=-896    y=0       (-14.0000, 0.0000)
1130: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1132: 80 37 80 07     VEC     scale=03(/64)  bri=0     x=-896    y=-896    (-14.0000, -14.0000)
1136: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1138: 80 37 80 03     VEC     scale=03(/64)  bri=0     x=896     y=-896    (14.0000, -14.0000)
113C: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
113E: E0 40 A0 02     VEC     scale=04(/32)  bri=0     x=672     y=224     (21.0000, 7.0000)
1142: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1144: C0 35 80 03     VEC     scale=03(/64)  bri=0     x=896     y=-448    (14.0000, -7.0000)
1148: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
114A: 80 33 00 00     VEC     scale=03(/64)  bri=0     x=0       y=896     (0.0000, 14.0000)
114E: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1150: A0 42 E0 00     VEC     scale=04(/32)  bri=0     x=224     y=672     (7.0000, 21.0000)
1154: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1156: A0 42 E0 04     VEC     scale=04(/32)  bri=0     x=-224    y=672     (-7.0000, 21.0000)
115A: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
115C: E0 44 80 07     VEC     scale=04(/32)  bri=0     x=-896    y=-224    (-28.0000, -7.0000)
1160: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1162: E0 40 A0 06     VEC     scale=04(/32)  bri=0     x=-672    y=224     (-21.0000, 7.0000)
1166: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1168: 00 D0           RTS                         
;
; Shrapnel pattern 3
116A: 07 F8           SVEC    scale=01(*4)   bri=0     x=-3      y=0       (-12.0000, 0.0000)
116C: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
116E: 07 FF           SVEC    scale=01(*4)   bri=0     x=-3      y=-3      (-12.0000, -12.0000)
1170: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1172: 03 FF           SVEC    scale=01(*4)   bri=0     x=3       y=-3      (12.0000, -12.0000)
1174: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1176: C0 40 40 02     VEC     scale=04(/32)  bri=0     x=576     y=192     (18.0000, 6.0000)
117A: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
117C: 80 35 00 03     VEC     scale=03(/64)  bri=0     x=768     y=-384    (12.0000, -6.0000)
1180: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1182: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
1184: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1186: 40 42 C0 00     VEC     scale=04(/32)  bri=0     x=192     y=576     (6.0000, 18.0000)
118A: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
118C: 40 42 C0 04     VEC     scale=04(/32)  bri=0     x=-192    y=576     (-6.0000, 18.0000)
1190: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1192: C0 44 00 07     VEC     scale=04(/32)  bri=0     x=-768    y=-192    (-24.0000, -6.0000)
1196: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
1198: C0 40 40 06     VEC     scale=04(/32)  bri=0     x=-576    y=192     (-18.0000, 6.0000)
119C: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
119E: 00 D0           RTS                         
;
; Shrapnel pattern 4
11A0: 00 30 80 06     VEC     scale=03(/64)  bri=0     x=-640    y=0       (-10.0000, 0.0000)
11A4: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
11A6: 80 36 80 06     VEC     scale=03(/64)  bri=0     x=-640    y=-640    (-10.0000, -10.0000)
11AA: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
11AC: 80 36 80 02     VEC     scale=03(/64)  bri=0     x=640     y=-640    (10.0000, -10.0000)
11B0: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
11B2: 40 31 C0 03     VEC     scale=03(/64)  bri=0     x=960     y=320     (15.0000, 5.0000)
11B6: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
11B8: 40 35 80 02     VEC     scale=03(/64)  bri=0     x=640     y=-320    (10.0000, -5.0000)
11BC: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
11BE: 80 32 00 00     VEC     scale=03(/64)  bri=0     x=0       y=640     (0.0000, 10.0000)
11C2: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
11C4: C0 33 40 01     VEC     scale=03(/64)  bri=0     x=320     y=960     (5.0000, 15.0000)
11C8: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
11CA: C0 33 40 05     VEC     scale=03(/64)  bri=0     x=-320    y=960     (-5.0000, 15.0000)
11CE: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
11D0: A0 44 80 06     VEC     scale=04(/32)  bri=0     x=-640    y=-160    (-20.0000, -5.0000)
11D4: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
11D6: 40 31 C0 07     VEC     scale=03(/64)  bri=0     x=-960    y=320     (-15.0000, 5.0000)
11DA: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
11DC: 00 D0           RTS                         
```

# Rock Patterns 

```html
<canvas width="400" height="100"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="1000"
  data-command="baseScale=0,x=50,y=50,11E6,x=150,y=50,11FE,x=250,y=50,121A,x=350,y=50,1234">
</canvas>
```

```code
; Jump table for 4  
11DE: F3 C8           JSR     $08F3 ($11E6)       ; 
11E0: FF C8           JSR     $08FF ($11FE)       ; 
11E2: 0D C9           JSR     $090D ($121A)       ; 
11E4: 1A C9           JSR     $091A ($1234)       ; 
;
; Rock Pattern 1
11E6: 08 F9           SVEC    scale=03(*16)  bri=0     x=0       y=1       (0.0000, 16.0000)
11E8: 79 F9           SVEC    scale=03(*16)  bri=7     x=1       y=1       (16.0000, 16.0000)
11EA: 79 FD           SVEC    scale=03(*16)  bri=7     x=1       y=-1      (16.0000, -16.0000)
11EC: 7D F6           SVEC    scale=02(*8)   bri=7     x=-1      y=-2      (-8.0000, -16.0000)
11EE: 79 F6           SVEC    scale=02(*8)   bri=7     x=1       y=-2      (8.0000, -16.0000)
11F0: 8F F6           SVEC    scale=02(*8)   bri=8     x=-3      y=-2      (-24.0000, -16.0000)
11F2: 8F F0           SVEC    scale=02(*8)   bri=8     x=-3      y=0       (-24.0000, 0.0000)
11F4: 7D F9           SVEC    scale=03(*16)  bri=7     x=-1      y=1       (-16.0000, 16.0000)
11F6: 78 FA           SVEC    scale=03(*16)  bri=7     x=0       y=2       (0.0000, 32.0000)
11F8: 79 F9           SVEC    scale=03(*16)  bri=7     x=1       y=1       (16.0000, 16.0000)
11FA: 79 FD           SVEC    scale=03(*16)  bri=7     x=1       y=-1      (16.0000, -16.0000)
11FC: 00 D0           RTS                         
;
; Rock Pattern 2
11FE: 0A F1           SVEC    scale=02(*8)   bri=0     x=2       y=1       (16.0000, 8.0000)
1200: 7A F1           SVEC    scale=02(*8)   bri=7     x=2       y=1       (16.0000, 8.0000)
1202: 7D F9           SVEC    scale=03(*16)  bri=7     x=-1      y=1       (-16.0000, 16.0000)
1204: 7E F5           SVEC    scale=02(*8)   bri=7     x=-2      y=-1      (-16.0000, -8.0000)
1206: 7E F1           SVEC    scale=02(*8)   bri=7     x=-2      y=1       (-16.0000, 8.0000)
1208: 7D FD           SVEC    scale=03(*16)  bri=7     x=-1      y=-1      (-16.0000, -16.0000)
120A: 79 F6           SVEC    scale=02(*8)   bri=7     x=1       y=-2      (8.0000, -16.0000)
120C: 7D F6           SVEC    scale=02(*8)   bri=7     x=-1      y=-2      (-8.0000, -16.0000)
120E: 79 FD           SVEC    scale=03(*16)  bri=7     x=1       y=-1      (16.0000, -16.0000)
1210: 79 F1           SVEC    scale=02(*8)   bri=7     x=1       y=1       (8.0000, 8.0000)
1212: 8B F5           SVEC    scale=02(*8)   bri=8     x=3       y=-1      (24.0000, -8.0000)
1214: 8A F3           SVEC    scale=02(*8)   bri=8     x=2       y=3       (16.0000, 24.0000)
1216: 7D F9           SVEC    scale=03(*16)  bri=7     x=-1      y=1       (-16.0000, 16.0000)
1218: 00 D0           RTS                         
;
; Rock Pattern 3  
121A: 0D F8           SVEC    scale=03(*16)  bri=0     x=-1      y=0       (-16.0000, 0.0000)
121C: 7E F5           SVEC    scale=02(*8)   bri=7     x=-2      y=-1      (-16.0000, -8.0000)
121E: 7A F7           SVEC    scale=02(*8)   bri=7     x=2       y=-3      (16.0000, -24.0000)
1220: 7A F3           SVEC    scale=02(*8)   bri=7     x=2       y=3       (16.0000, 24.0000)
1222: 78 F7           SVEC    scale=02(*8)   bri=7     x=0       y=-3      (0.0000, -24.0000)
1224: 79 F8           SVEC    scale=03(*16)  bri=7     x=1       y=0       (16.0000, 0.0000)
1226: 7A F3           SVEC    scale=02(*8)   bri=7     x=2       y=3       (16.0000, 24.0000)
1228: 78 F9           SVEC    scale=03(*16)  bri=7     x=0       y=1       (0.0000, 16.0000)
122A: 7E F3           SVEC    scale=02(*8)   bri=7     x=-2      y=3       (-16.0000, 24.0000)
122C: 7F F0           SVEC    scale=02(*8)   bri=7     x=-3      y=0       (-24.0000, 0.0000)
122E: 7F F7           SVEC    scale=02(*8)   bri=7     x=-3      y=-3      (-24.0000, -24.0000)
1230: 7A F5           SVEC    scale=02(*8)   bri=7     x=2       y=-1      (16.0000, -8.0000)
1232: 00 D0           RTS                         
;
; Rock Pattern 4
1234: 09 F0           SVEC    scale=02(*8)   bri=0     x=1       y=0       (8.0000, 0.0000)
1236: 7B F1           SVEC    scale=02(*8)   bri=7     x=3       y=1       (24.0000, 8.0000)
1238: 68 F1           SVEC    scale=02(*8)   bri=6     x=0       y=1       (0.0000, 8.0000)
123A: 7F F2           SVEC    scale=02(*8)   bri=7     x=-3      y=2       (-24.0000, 16.0000)
123C: 7F F0           SVEC    scale=02(*8)   bri=7     x=-3      y=0       (-24.0000, 0.0000)
123E: 69 F6           SVEC    scale=02(*8)   bri=6     x=1       y=-2      (8.0000, -16.0000)
1240: 7F F0           SVEC    scale=02(*8)   bri=7     x=-3      y=0       (-24.0000, 0.0000)
1242: 78 F7           SVEC    scale=02(*8)   bri=7     x=0       y=-3      (0.0000, -24.0000)
1244: 7A F7           SVEC    scale=02(*8)   bri=7     x=2       y=-3      (16.0000, -24.0000)
1246: 7B F1           SVEC    scale=02(*8)   bri=7     x=3       y=1       (24.0000, 8.0000)
1248: 69 F5           SVEC    scale=02(*8)   bri=6     x=1       y=-1      (8.0000, -8.0000)
124A: 69 F9           SVEC    scale=03(*16)  bri=6     x=1       y=1       (16.0000, 16.0000)
124C: 7F F2           SVEC    scale=02(*8)   bri=7     x=-3      y=2       (-24.0000, 16.0000)
124E: 00 D0           RTS                         
```

# UFO 

```html
<canvas width="100" height="75"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="1000"
  data-command="x=50,y=40,baseScale=0,1252">
</canvas>
```

```code
; Jump table for 1
1250: 29 C9           JSR     $0929 ($1252)       ; 
;
1252: 0E F1           SVEC    scale=02(*8)   bri=0     x=-2      y=1       (-16.0000, 8.0000)
1254: CA F8           SVEC    scale=03(*16)  bri=12    x=2       y=0       (32.0000, 0.0000)
1256: 0B F6           SVEC    scale=02(*8)   bri=0     x=3       y=-2      (24.0000, -16.0000)
1258: 00 60 80 D6     VEC     scale=06(/8)   bri=13    x=-640    y=0       (-80.0000, 0.0000)
125C: DB F6           SVEC    scale=02(*8)   bri=13    x=3       y=-2      (24.0000, -16.0000)
125E: CA F8           SVEC    scale=03(*16)  bri=12    x=2       y=0       (32.0000, 0.0000)
1260: DB F2           SVEC    scale=02(*8)   bri=13    x=3       y=2       (24.0000, 16.0000)
1262: DF F2           SVEC    scale=02(*8)   bri=13    x=-3      y=2       (-24.0000, 16.0000)
1264: CD F2           SVEC    scale=02(*8)   bri=12    x=-1      y=2       (-8.0000, 16.0000)
1266: CD F8           SVEC    scale=03(*16)  bri=12    x=-1      y=0       (-16.0000, 0.0000)
1268: CD F6           SVEC    scale=02(*8)   bri=12    x=-1      y=-2      (-8.0000, -16.0000)
126A: DF F6           SVEC    scale=02(*8)   bri=13    x=-3      y=-2      (-24.0000, -16.0000)
126C: 00 D0           RTS                         
```

# Player Ships 

```code
; Table for ships and thrusts based on player's direction.
; The addresses are where the ROM appears in the main CPU's
; memory map (begins at 5000). Thus 5292 - 5000 + 0800 = 0A92.
; The thrust pattern for each ship follows the ship itself.
;
126E: 90 52 ; [ShipDir0](#ShipDir0)
1270: A8 52 ; [ShipDir4](#ShipDir4)
1272: CC 52 ; [ShipDir8](#ShipDir8)
1274: F0 52 ; [ShipDir12](#ShipDir12)
1276: 14 53 ; [ShipDir16](#ShipDir16)
1278: 36 53 ; [ShipDir20](#ShipDir20)
127A: 5A 53 ; [ShipDir24](#ShipDir24)
127C: 7E 53 ; [ShipDir28](#ShipDir28)
127E: A2 53 ; [ShipDir32](#ShipDir32)
1280: C6 53 ; [ShipDir36](#ShipDir36)
1282: EA 53 ; [ShipDir40](#ShipDir40)
1284: 0E 54 ; [ShipDir44](#ShipDir44)
1286: 32 54 ; [ShipDir48](#ShipDir48)
1288: 56 54 ; [ShipDir52](#ShipDir52)
128A: 7A 54 ; [ShipDir56](#ShipDir56)
128C: 9E 54 ; [ShipDir60](#ShipDir60)
128E: C2 54 ; [ShipDir64](#ShipDir64)
```

```html
<canvas width="1060" height="100"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="1000"
  data-command="baseScale=-1,
    x=50,y=50,1290,12A2,    
    x=110,y=50,12A8,
    x=170,y=50,12CC,
    x=230,y=50,12F0,
    x=290,y=50,1314,
    x=350,y=50,1336,
    x=410,y=50,135A,
    x=470,y=50,137E,
    x=530,y=50,13A2,
    x=590,y=50,13C6,
    x=650,y=50,13EA,
    x=710,y=50,140E,
    x=770,y=50,1432,
    x=830,y=50,1456,
    x=890,y=50,147A,
    x=950,y=50,149E,
    x=1010,y=50,14C2,14D4
  ">
</canvas>
```

```code
ShipDir0:
1290: 0F F6           SVEC    scale=02(*8)   bri=0     x=-3      y=-2      (-24.0000, -16.0000)
1292: C8 FA           SVEC    scale=03(*16)  bri=12    x=0       y=2       (0.0000, 32.0000)
1294: BD F9           SVEC    scale=03(*16)  bri=11    x=-1      y=1       (-16.0000, 16.0000)
1296: 00 65 00 C3     VEC     scale=06(/8)   bri=12    x=768     y=-256    (96.0000, -32.0000)
129A: 00 65 00 C7     VEC     scale=06(/8)   bri=12    x=-768    y=-256    (-96.0000, -32.0000)
129E: B9 F9           SVEC    scale=03(*16)  bri=11    x=1       y=1       (16.0000, 16.0000)
12A0: 00 D0           RTS                         
ThrustDir0:  
12A2: CE F9           SVEC    scale=03(*16)  bri=12    x=-2      y=1       (-32.0000, 16.0000)
12A4: CA F9           SVEC    scale=03(*16)  bri=12    x=2       y=1       (32.0000, 16.0000)
12A6: 00 D0           RTS                         

ShipDir4:
12A8: 40 46 C0 06     VEC     scale=04(/32)  bri=0     x=-704    y=-576    (-22.0000, -18.0000)
12AC: 00 52 30 C4     VEC     scale=05(/16)  bri=12    x=-48     y=512     (-3.0000, 32.0000)
12B0: C0 41 20 C6     VEC     scale=04(/32)  bri=12    x=-544    y=448     (-17.0000, 14.0000)
12B4: B0 64 18 C3     VEC     scale=06(/8)   bri=12    x=792     y=-176    (99.0000, -22.0000)
12B8: 48 65 E0 C6     VEC     scale=06(/8)   bri=12    x=-736    y=-328    (-92.0000, -41.0000)
12BC: 20 42 C0 C1     VEC     scale=04(/32)  bri=12    x=448     y=544     (14.0000, 17.0000)
12C0: 00 D0           RTS                         
ThrustDir4:  
12C2: D0 50 10 C6     VEC     scale=05(/16)  bri=12    x=-528    y=208     (-33.0000, 13.0000)
12C6: 60 42 C0 C3     VEC     scale=04(/32)  bri=12    x=960     y=608     (30.0000, 19.0000)
12CA: 00 D0           RTS                         

ShipDir8:  
12CC: 80 46 80 06     VEC     scale=04(/32)  bri=0     x=-640    y=-640    (-20.0000, -20.0000)
12D0: E0 43 C0 C4     VEC     scale=04(/32)  bri=12    x=-192    y=992     (-6.0000, 31.0000)
12D4: A0 41 60 C6     VEC     scale=04(/32)  bri=12    x=-608    y=416     (-19.0000, 13.0000)
12D8: 68 64 20 C3     VEC     scale=06(/8)   bri=12    x=800     y=-104    (100.0000, -13.0000)
12DC: 90 65 C0 C6     VEC     scale=06(/8)   bri=12    x=-704    y=-400    (-88.0000, -50.0000)
12E0: 60 42 A0 C1     VEC     scale=04(/32)  bri=12    x=416     y=608     (13.0000, 19.0000)
12E4: 00 D0           RTS                         
ThrustDir8:
12E6: 90 50 30 C6     VEC     scale=05(/16)  bri=12    x=-560    y=144     (-35.0000, 9.0000)
12EA: C0 42 80 C3     VEC     scale=04(/32)  bri=12    x=896     y=704     (28.0000, 22.0000)
12EE: 00 D0           RTS                         

ShipDir12:
12F0: C0 46 40 06     VEC     scale=04(/32)  bri=0     x=-576    y=-704    (-18.0000, -22.0000)
12F4: E0 43 20 C5     VEC     scale=04(/32)  bri=12    x=-288    y=992     (-9.0000, 31.0000)
12F8: 60 41 80 C6     VEC     scale=04(/32)  bri=12    x=-640    y=352     (-20.0000, 11.0000)
12FC: 18 64 28 C3     VEC     scale=06(/8)   bri=12    x=808     y=-24     (101.0000, -3.0000)
1300: D0 65 98 C6     VEC     scale=06(/8)   bri=12    x=-664    y=-464    (-83.0000, -58.0000)
1304: 80 42 60 C1     VEC     scale=04(/32)  bri=12    x=352     y=640     (11.0000, 20.0000)
1308: 00 D0           RTS                         
ThrustDir12:
130A: 60 50 30 C6     VEC     scale=05(/16)  bri=12    x=-560    y=96      (-35.0000, 6.0000)
130E: 20 43 40 C3     VEC     scale=04(/32)  bri=12    x=832     y=800     (26.0000, 25.0000)
1312: 00 D0           RTS                         

ShipDir16:
1314: 0E F7           SVEC    scale=02(*8)   bri=0     x=-2      y=-3      (-16.0000, -24.0000)
1316: C0 43 80 C5     VEC     scale=04(/32)  bri=12    x=-384    y=960     (-12.0000, 30.0000)
131A: 20 41 A0 C6     VEC     scale=04(/32)  bri=12    x=-672    y=288     (-21.0000, 9.0000)
131E: 38 60 28 C3     VEC     scale=06(/8)   bri=12    x=808     y=56      (101.0000, 7.0000)
1322: 10 66 60 C6     VEC     scale=06(/8)   bri=12    x=-608    y=-528    (-76.0000, -66.0000)
1326: A0 42 20 C1     VEC     scale=04(/32)  bri=12    x=288     y=672     (9.0000, 21.0000)
132A: 00 D0           RTS                         
ThrustDir16:
132C: 30 50 40 C6     VEC     scale=05(/16)  bri=12    x=-576    y=48      (-36.0000, 3.0000)
1330: 60 43 E0 C2     VEC     scale=04(/32)  bri=12    x=736     y=864     (23.0000, 27.0000)
1334: 00 D0           RTS                         

ShipDir20:  
1336: 20 47 C0 05     VEC     scale=04(/32)  bri=0     x=-448    y=-800    (-14.0000, -25.0000)
133A: 80 43 E0 C5     VEC     scale=04(/32)  bri=12    x=-480    y=896     (-15.0000, 28.0000)
133E: E0 40 C0 C6     VEC     scale=04(/32)  bri=12    x=-704    y=224     (-22.0000, 7.0000)
1342: 88 60 20 C3     VEC     scale=06(/8)   bri=12    x=800     y=136     (100.0000, 17.0000)
1346: 48 66 30 C6     VEC     scale=06(/8)   bri=12    x=-560    y=-584    (-70.0000, -73.0000)
134A: C0 42 E0 C0     VEC     scale=04(/32)  bri=12    x=224     y=704     (7.0000, 22.0000)
134E: 00 D0           RTS                         
ThrustDir20:
1350: 10 54 40 C6     VEC     scale=05(/16)  bri=12    x=-576    y=-16     (-36.0000, -1.0000)
1354: A0 43 A0 C2     VEC     scale=04(/32)  bri=12    x=672     y=928     (21.0000, 29.0000)
1358: 00 D0           RTS                         

ShipDir24:  
135A: 60 47 60 05     VEC     scale=04(/32)  bri=0     x=-352    y=-864    (-11.0000, -27.0000)
135E: 60 43 40 C6     VEC     scale=04(/32)  bri=12    x=-576    y=864     (-18.0000, 27.0000)
1362: 80 40 C0 C6     VEC     scale=04(/32)  bri=12    x=-704    y=128     (-22.0000, 4.0000)
1366: D8 60 10 C3     VEC     scale=06(/8)   bri=12    x=784     y=216     (98.0000, 27.0000)
136A: 80 66 F0 C5     VEC     scale=06(/8)   bri=12    x=-496    y=-640    (-62.0000, -80.0000)
136E: C0 42 80 C0     VEC     scale=04(/32)  bri=12    x=128     y=704     (4.0000, 22.0000)
1372: 00 D0           RTS                         
ThrustDir24:
1374: 40 54 30 C6     VEC     scale=05(/16)  bri=12    x=-560    y=-64     (-35.0000, -4.0000)
1378: E0 43 40 C2     VEC     scale=04(/32)  bri=12    x=576     y=992     (18.0000, 31.0000)
137C: 00 D0           RTS                         

ShipDir28:  
137E: 80 47 00 05     VEC     scale=04(/32)  bri=0     x=-256    y=-896    (-8.0000, -28.0000)
1382: 20 43 80 C6     VEC     scale=04(/32)  bri=12    x=-640    y=800     (-20.0000, 25.0000)
1386: 40 40 E0 C6     VEC     scale=04(/32)  bri=12    x=-736    y=64      (-23.0000, 2.0000)
138A: 20 61 F8 C2     VEC     scale=06(/8)   bri=12    x=760     y=288     (95.0000, 36.0000)
138E: B0 66 B0 C5     VEC     scale=06(/8)   bri=12    x=-432    y=-688    (-54.0000, -86.0000)
1392: E0 42 40 C0     VEC     scale=04(/32)  bri=12    x=64      y=736     (2.0000, 23.0000)
1396: 00 D0           RTS                         
ThrustDir28:
1398: 80 54 30 C6     VEC     scale=05(/16)  bri=12    x=-560    y=-128    (-35.0000, -8.0000)
139C: 10 52 F0 C0     VEC     scale=05(/16)  bri=12    x=240     y=528     (15.0000, 33.0000)
13A0: 00 D0           RTS                         

ShipDir32:  
13A2: 80 47 C0 04     VEC     scale=04(/32)  bri=0     x=-192    y=-896    (-6.0000, -28.0000)
13A6: E0 42 E0 C6     VEC     scale=04(/32)  bri=12    x=-736    y=736     (-23.0000, 23.0000)
13AA: 00 40 E0 C6     VEC     scale=04(/32)  bri=12    x=-736    y=0       (-23.0000, 0.0000)
13AE: 68 61 D8 C2     VEC     scale=06(/8)   bri=12    x=728     y=360     (91.0000, 45.0000)
13B2: D8 66 68 C5     VEC     scale=06(/8)   bri=12    x=-360    y=-728    (-45.0000, -91.0000)
13B6: E0 42 00 C0     VEC     scale=04(/32)  bri=12    x=0       y=736     (0.0000, 23.0000)
13BA: 00 D0           RTS                         
ThrustDir32:
13BC: B0 54 20 C6     VEC     scale=05(/16)  bri=12    x=-544    y=-176    (-34.0000, -11.0000)
13C0: 20 52 B0 C0     VEC     scale=05(/16)  bri=12    x=176     y=544     (11.0000, 34.0000)
13C4: 00 D0           RTS                         

ShipDir36:  
13C6: A0 47 60 04     VEC     scale=04(/32)  bri=0     x=-96     y=-928    (-3.0000, -29.0000)
13CA: 80 42 20 C7     VEC     scale=04(/32)  bri=12    x=-800    y=640     (-25.0000, 20.0000)
13CE: 40 44 E0 C6     VEC     scale=04(/32)  bri=12    x=-736    y=-64     (-23.0000, -2.0000)
13D2: B0 61 B0 C2     VEC     scale=06(/8)   bri=12    x=688     y=432     (86.0000, 54.0000)
13D6: F8 66 20 C5     VEC     scale=06(/8)   bri=12    x=-288    y=-760    (-36.0000, -95.0000)
13DA: E0 42 40 C4     VEC     scale=04(/32)  bri=12    x=-64     y=736     (-2.0000, 23.0000)
13DE: 00 D0           RTS                         
ThrustDir36:
13E0: F0 54 10 C6     VEC     scale=05(/16)  bri=12    x=-528    y=-240    (-33.0000, -15.0000)
13E4: 30 52 80 C0     VEC     scale=05(/16)  bri=12    x=128     y=560     (8.0000, 35.0000)
13E8: 00 D0           RTS                         

ShipDir40:  
13EA: A0 47 00 00     VEC     scale=04(/32)  bri=0     x=0       y=-928    (0.0000, -29.0000)
13EE: 40 42 60 C7     VEC     scale=04(/32)  bri=12    x=-864    y=576     (-27.0000, 18.0000)
13F2: 80 44 C0 C6     VEC     scale=04(/32)  bri=12    x=-704    y=-128    (-22.0000, -4.0000)
13F6: F0 61 80 C2     VEC     scale=06(/8)   bri=12    x=640     y=496     (80.0000, 62.0000)
13FA: 10 67 D8 C4     VEC     scale=06(/8)   bri=12    x=-216    y=-784    (-27.0000, -98.0000)
13FE: C0 42 80 C4     VEC     scale=04(/32)  bri=12    x=-128    y=704     (-4.0000, 22.0000)
1402: 00 D0           RTS                         
ThrustDir40:
1404: 40 46 E0 C7     VEC     scale=04(/32)  bri=12    x=-992    y=-576    (-31.0000, -18.0000)
1408: 30 52 40 C0     VEC     scale=05(/16)  bri=12    x=64      y=560     (4.0000, 35.0000)
140C: 00 D0           RTS                         

ShipDir44: 
140E: A0 47 60 00     VEC     scale=04(/32)  bri=0     x=96      y=-928    (3.0000, -29.0000)
1412: E0 41 80 C7     VEC     scale=04(/32)  bri=12    x=-896    y=480     (-28.0000, 15.0000)
1416: E0 44 C0 C6     VEC     scale=04(/32)  bri=12    x=-704    y=-224    (-22.0000, -7.0000)
141A: 30 62 48 C2     VEC     scale=06(/8)   bri=12    x=584     y=560     (73.0000, 70.0000)
141E: 20 67 88 C4     VEC     scale=06(/8)   bri=12    x=-136    y=-800    (-17.0000, -100.0000)
1422: C0 42 E0 C4     VEC     scale=04(/32)  bri=12    x=-224    y=704     (-7.0000, 22.0000)
1426: 00 D0           RTS                         
ThrustDir44:
1428: A0 46 A0 C7     VEC     scale=04(/32)  bri=12    x=-928    y=-672    (-29.0000, -21.0000)
142C: 40 52 10 C0     VEC     scale=05(/16)  bri=12    x=16      y=576     (1.0000, 36.0000)
1430: 00 D0           RTS                         

ShipDir48:  
1432: 80 47 C0 00     VEC     scale=04(/32)  bri=0     x=192     y=-896    (6.0000, -28.0000)
1436: 80 41 C0 C7     VEC     scale=04(/32)  bri=12    x=-960    y=384     (-30.0000, 12.0000)
143A: 20 45 A0 C6     VEC     scale=04(/32)  bri=12    x=-672    y=-288    (-21.0000, -9.0000)
143E: 60 62 10 C2     VEC     scale=06(/8)   bri=12    x=528     y=608     (66.0000, 76.0000)
1442: 28 67 38 C4     VEC     scale=06(/8)   bri=12    x=-56     y=-808    (-7.0000, -101.0000)
1446: A0 42 20 C5     VEC     scale=04(/32)  bri=12    x=-288    y=672     (-9.0000, 21.0000)
144A: 00 D0           RTS                         
ThrustDir48:
144C: E0 46 60 C7     VEC     scale=04(/32)  bri=12    x=-864    y=-736    (-27.0000, -23.0000)
1450: 40 52 30 C4     VEC     scale=05(/16)  bri=12    x=-48     y=576     (-3.0000, 36.0000)
1454: 00 D0           RTS                         

ShipDir52:
1456: 80 47 00 01     VEC     scale=04(/32)  bri=0     x=256     y=-896    (8.0000, -28.0000)
145A: 20 41 E0 C7     VEC     scale=04(/32)  bri=12    x=-992    y=288     (-31.0000, 9.0000)
145E: 60 45 80 C6     VEC     scale=04(/32)  bri=12    x=-640    y=-352    (-20.0000, -11.0000)
1462: 98 62 D0 C1     VEC     scale=06(/8)   bri=12    x=464     y=664     (58.0000, 83.0000)
1466: 28 67 18 C0     VEC     scale=06(/8)   bri=12    x=24      y=-808    (3.0000, -101.0000)
146A: 80 42 60 C5     VEC     scale=04(/32)  bri=12    x=-352    y=640     (-11.0000, 20.0000)
146E: 00 D0           RTS                         
ThrustDir52:
1470: 40 47 20 C7     VEC     scale=04(/32)  bri=12    x=-800    y=-832    (-25.0000, -26.0000)
1474: 30 52 60 C4     VEC     scale=05(/16)  bri=12    x=-96     y=560     (-6.0000, 35.0000)
1478: 00 D0           RTS                         

ShipDir56:
147A: 60 47 60 01     VEC     scale=04(/32)  bri=0     x=352     y=-864    (11.0000, -27.0000)
147E: C0 40 E0 C7     VEC     scale=04(/32)  bri=12    x=-992    y=192     (-31.0000, 6.0000)
1482: A0 45 60 C6     VEC     scale=04(/32)  bri=12    x=-608    y=-416    (-19.0000, -13.0000)
1486: C0 62 90 C1     VEC     scale=06(/8)   bri=12    x=400     y=704     (50.0000, 88.0000)
148A: 20 67 68 C0     VEC     scale=06(/8)   bri=12    x=104     y=-800    (13.0000, -100.0000)
148E: 60 42 A0 C5     VEC     scale=04(/32)  bri=12    x=-416    y=608     (-13.0000, 19.0000)
1492: 00 D0           RTS                         
ThrustDir56:
1494: 80 47 C0 C6     VEC     scale=04(/32)  bri=12    x=-704    y=-896    (-22.0000, -28.0000)
1498: 30 52 90 C4     VEC     scale=05(/16)  bri=12    x=-144    y=560     (-9.0000, 35.0000)
149C: 00 D0           RTS                         

ShipDir60:  
149E: 20 47 C0 01     VEC     scale=04(/32)  bri=0     x=448     y=-800    (14.0000, -25.0000)
14A2: 30 50 00 C6     VEC     scale=05(/16)  bri=12    x=-512    y=48      (-32.0000, 3.0000)
14A6: C0 45 20 C6     VEC     scale=04(/32)  bri=12    x=-544    y=-448    (-17.0000, -14.0000)
14AA: E0 62 48 C1     VEC     scale=06(/8)   bri=12    x=328     y=736     (41.0000, 92.0000)
14AE: 18 67 B0 C0     VEC     scale=06(/8)   bri=12    x=176     y=-792    (22.0000, -99.0000)
14B2: 20 42 C0 C5     VEC     scale=04(/32)  bri=12    x=-448    y=544     (-14.0000, 17.0000)
14B6: 00 D0           RTS                         
ThrustDir60:
14B8: C0 47 60 C6     VEC     scale=04(/32)  bri=12    x=-608    y=-960    (-19.0000, -30.0000)
14BC: 10 52 D0 C4     VEC     scale=05(/16)  bri=12    x=-208    y=528     (-13.0000, 33.0000)
14C0: 00 D0           RTS                         

ShipDir64:
14C2: 0A F7           SVEC    scale=02(*8)   bri=0     x=2       y=-3      (16.0000, -24.0000)
14C4: CE F8           SVEC    scale=03(*16)  bri=12    x=-2      y=0       (-32.0000, 0.0000)
14C6: CD FD           SVEC    scale=03(*16)  bri=12    x=-1      y=-1      (-16.0000, -16.0000)
14C8: 00 63 00 C1     VEC     scale=06(/8)   bri=12    x=256     y=768     (32.0000, 96.0000)
14CC: 00 67 00 C1     VEC     scale=06(/8)   bri=12    x=256     y=-768    (32.0000, -96.0000)
14D0: CD F9           SVEC    scale=03(*16)  bri=12    x=-1      y=1       (-16.0000, 16.0000)
ThrustDir64:
14D2: 00 D0           RTS                         
14D4: CD FE           SVEC    scale=03(*16)  bri=12    x=-1      y=-2      (-16.0000, -32.0000)
14D6: CD FA           SVEC    scale=03(*16)  bri=12    x=-1      y=2       (-16.0000, 32.0000)
14D8: 00 D0           RTS                         
```

# Lives 

 Ships in reserve. These are defined so you can draw them one right after the other (three drawn here).

```html
<canvas width="200" height="100"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="1000"
  data-command="x=50,y=50,baseScale=-1,14DA,14DA,14DA">
</canvas>
```

```code  
14DA: 0E F7           SVEC    scale=02(*8)   bri=0     x=-2      y=-3      (-16.0000, -24.0000)
14DC: 7A F8           SVEC    scale=03(*16)  bri=7     x=2       y=0       (32.0000, 0.0000)
14DE: 79 FD           SVEC    scale=03(*16)  bri=7     x=1       y=-1      (16.0000, -16.0000)
14E0: 00 63 00 75     VEC     scale=06(/8)   bri=7     x=-256    y=768     (-32.0000, 96.0000)
14E4: 00 67 00 75     VEC     scale=06(/8)   bri=7     x=-256    y=-768    (-32.0000, -96.0000)
14E8: 79 F9           SVEC    scale=03(*16)  bri=7     x=1       y=1       (16.0000, 16.0000)
14EA: C0 60 80 02     VEC     scale=06(/8)   bri=0     x=640     y=192     (80.0000, 24.0000)
14EE: 9F D0           RTS                         
```

# Characters 

```html
<canvas width="500" height="120"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="1000"
  data-command="x=30,y=45,baseScale=1,14F0,1500,151A,1526,1536,1546,1554,1566,1574,1582,158E,159A,15A4,15B0,15BA,15C6,15D4,15E6,x=30,y=90,15F6,1604,1610,161C,1626,1634,163E,164C,1658,165C,1664,1674,1682,1690,169E,16AC,16B6,16C6">
</canvas>
```

```code
; "A"
14F0: 70 FA           SVEC    scale=01(*4)   bri=7     x=0       y=2       (0.0000, 8.0000)
14F2: 72 F2           SVEC    scale=00(*2)   bri=7     x=2       y=2       (4.0000, 4.0000)
14F4: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
14F6: 70 FE           SVEC    scale=01(*4)   bri=7     x=0       y=-2      (0.0000, -8.0000)
14F8: 06 F9           SVEC    scale=01(*4)   bri=0     x=-2      y=1       (-8.0000, 4.0000)
14FA: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
14FC: 02 F6           SVEC    scale=00(*2)   bri=0     x=2       y=-2      (4.0000, -4.0000)
14FE: 00 D0           RTS                         

; "B"
1500: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1502: 73 F0           SVEC    scale=00(*2)   bri=7     x=3       y=0       (6.0000, 0.0000)
1504: 71 F5           SVEC    scale=00(*2)   bri=7     x=1       y=-1      (2.0000, -2.0000)
1506: 70 F5           SVEC    scale=00(*2)   bri=7     x=0       y=-1      (0.0000, -2.0000)
1508: 75 F5           SVEC    scale=00(*2)   bri=7     x=-1      y=-1      (-2.0000, -2.0000)
150A: 77 F0           SVEC    scale=00(*2)   bri=7     x=-3      y=0       (-6.0000, 0.0000)
150C: 03 F0           SVEC    scale=00(*2)   bri=0     x=3       y=0       (6.0000, 0.0000)
150E: 71 F5           SVEC    scale=00(*2)   bri=7     x=1       y=-1      (2.0000, -2.0000)
1510: 70 F5           SVEC    scale=00(*2)   bri=7     x=0       y=-1      (0.0000, -2.0000)
1512: 75 F5           SVEC    scale=00(*2)   bri=7     x=-1      y=-1      (-2.0000, -2.0000)
1514: 77 F0           SVEC    scale=00(*2)   bri=7     x=-3      y=0       (-6.0000, 0.0000)
1516: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
1518: 00 D0           RTS                         

; "C"
151A: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
151C: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
151E: 06 FF           SVEC    scale=01(*4)   bri=0     x=-2      y=-3      (-8.0000, -12.0000)
1520: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1522: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
1524: 00 D0           RTS                         
  
; "D"
1526: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1528: 72 F0           SVEC    scale=00(*2)   bri=7     x=2       y=0       (4.0000, 0.0000)
152A: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
152C: 70 F6           SVEC    scale=00(*2)   bri=7     x=0       y=-2      (0.0000, -4.0000)
152E: 76 F6           SVEC    scale=00(*2)   bri=7     x=-2      y=-2      (-4.0000, -4.0000)
1530: 76 F0           SVEC    scale=00(*2)   bri=7     x=-2      y=0       (-4.0000, 0.0000)
1532: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
1534: 00 D0           RTS                         

; "E"
1536: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1538: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
153A: 05 F7           SVEC    scale=00(*2)   bri=0     x=-1      y=-3      (-2.0000, -6.0000)
153C: 77 F0           SVEC    scale=00(*2)   bri=7     x=-3      y=0       (-6.0000, 0.0000)
153E: 00 F7           SVEC    scale=00(*2)   bri=0     x=0       y=-3      (0.0000, -6.0000)
1540: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1542: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
1544: 00 D0           RTS                         

; "F"
1546: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1548: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
154A: 05 F7           SVEC    scale=00(*2)   bri=0     x=-1      y=-3      (-2.0000, -6.0000)
154C: 77 F0           SVEC    scale=00(*2)   bri=7     x=-3      y=0       (-6.0000, 0.0000)
154E: 00 F7           SVEC    scale=00(*2)   bri=0     x=0       y=-3      (0.0000, -6.0000)
1550: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
1552: 00 D0           RTS                         

; "G"
1554: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1556: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1558: 70 F6           SVEC    scale=00(*2)   bri=7     x=0       y=-2      (0.0000, -4.0000)
155A: 06 F6           SVEC    scale=00(*2)   bri=0     x=-2      y=-2      (-4.0000, -4.0000)
155C: 72 F0           SVEC    scale=00(*2)   bri=7     x=2       y=0       (4.0000, 0.0000)
155E: 70 F6           SVEC    scale=00(*2)   bri=7     x=0       y=-2      (0.0000, -4.0000)
1560: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
1562: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
1564: 00 D0           RTS                         

; "H"  
1566: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1568: 00 F7           SVEC    scale=00(*2)   bri=0     x=0       y=-3      (0.0000, -6.0000)
156A: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
156C: 00 F3           SVEC    scale=00(*2)   bri=0     x=0       y=3       (0.0000, 6.0000)
156E: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
1570: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
1572: 00 D0           RTS                         

; "I"  
1574: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1576: 06 F0           SVEC    scale=00(*2)   bri=0     x=-2      y=0       (-4.0000, 0.0000)
1578: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
157A: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
157C: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
157E: 03 FF           SVEC    scale=01(*4)   bri=0     x=3       y=-3      (12.0000, -12.0000)
1580: 00 D0           RTS                         

; "J"
1582: 00 F2           SVEC    scale=00(*2)   bri=0     x=0       y=2       (0.0000, 4.0000)
1584: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
1586: 72 F0           SVEC    scale=00(*2)   bri=7     x=2       y=0       (4.0000, 0.0000)
1588: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
158A: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
158C: 00 D0           RTS                         

; "K"  
158E: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1590: 03 F0           SVEC    scale=00(*2)   bri=0     x=3       y=0       (6.0000, 0.0000)
1592: 77 F7           SVEC    scale=00(*2)   bri=7     x=-3      y=-3      (-6.0000, -6.0000)
1594: 73 F7           SVEC    scale=00(*2)   bri=7     x=3       y=-3      (6.0000, -6.0000)
1596: 03 F0           SVEC    scale=00(*2)   bri=0     x=3       y=0       (6.0000, 0.0000)
1598: 00 D0           RTS                         

; "L"  
159A: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
159C: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
159E: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
15A0: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
15A2: 00 D0           RTS                         

; "M"
15A4: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
15A6: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
15A8: 72 F2           SVEC    scale=00(*2)   bri=7     x=2       y=2       (4.0000, 4.0000)
15AA: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
15AC: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
15AE: 00 D0           RTS                         

; "N"  
15B0: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
15B2: 72 FF           SVEC    scale=01(*4)   bri=7     x=2       y=-3      (8.0000, -12.0000)
15B4: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
15B6: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
15B8: 00 D0           RTS                         

; "O"  
15BA: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
15BC: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
15BE: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
15C0: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
15C2: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
15C4: 00 D0           RTS                         

; "P"
15C6: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
15C8: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
15CA: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
15CC: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
15CE: 03 F7           SVEC    scale=00(*2)   bri=0     x=3       y=-3      (6.0000, -6.0000)
15D0: 03 F0           SVEC    scale=00(*2)   bri=0     x=3       y=0       (6.0000, 0.0000)
15D2: 00 D0           RTS                         

; "Q"  
15D4: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
15D6: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
15D8: 70 FE           SVEC    scale=01(*4)   bri=7     x=0       y=-2      (0.0000, -8.0000)
15DA: 76 F6           SVEC    scale=00(*2)   bri=7     x=-2      y=-2      (-4.0000, -4.0000)
15DC: 76 F0           SVEC    scale=00(*2)   bri=7     x=-2      y=0       (-4.0000, 0.0000)
15DE: 02 F2           SVEC    scale=00(*2)   bri=0     x=2       y=2       (4.0000, 4.0000)
15E0: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
15E2: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
15E4: 00 D0           RTS                         

; "R"
15E6: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
15E8: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
15EA: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
15EC: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
15EE: 01 F0           SVEC    scale=00(*2)   bri=0     x=1       y=0       (2.0000, 0.0000)
15F0: 73 F7           SVEC    scale=00(*2)   bri=7     x=3       y=-3      (6.0000, -6.0000)
15F2: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
15F4: 00 D0           RTS                         

; "S"
15F6: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
15F8: 70 F3           SVEC    scale=00(*2)   bri=7     x=0       y=3       (0.0000, 6.0000)
15FA: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
15FC: 70 F3           SVEC    scale=00(*2)   bri=7     x=0       y=3       (0.0000, 6.0000)
15FE: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1600: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
1602: 00 D0           RTS                         

; "T"
1604: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
1606: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1608: 06 F0           SVEC    scale=00(*2)   bri=0     x=-2      y=0       (-4.0000, 0.0000)
160A: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
160C: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
160E: 00 D0           RTS                         

; "U"
1610: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
1612: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
1614: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1616: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1618: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
161A: 00 D0           RTS                         

; "V"
161C: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
161E: 71 FF           SVEC    scale=01(*4)   bri=7     x=1       y=-3      (4.0000, -12.0000)
1620: 71 FB           SVEC    scale=01(*4)   bri=7     x=1       y=3       (4.0000, 12.0000)
1622: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
1624: 00 D0           RTS                         

; "W"
1626: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
1628: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
162A: 72 F2           SVEC    scale=00(*2)   bri=7     x=2       y=2       (4.0000, 4.0000)
162C: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
162E: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1630: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
1632: 00 D0           RTS                         
  
; "X"
1634: 72 FB           SVEC    scale=01(*4)   bri=7     x=2       y=3       (8.0000, 12.0000)
1636: 06 F8           SVEC    scale=01(*4)   bri=0     x=-2      y=0       (-8.0000, 0.0000)
1638: 72 FF           SVEC    scale=01(*4)   bri=7     x=2       y=-3      (8.0000, -12.0000)
163A: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
163C: 00 D0           RTS                         

; "Y"
163E: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
1640: 70 FA           SVEC    scale=01(*4)   bri=7     x=0       y=2       (0.0000, 8.0000)
1642: 76 F2           SVEC    scale=00(*2)   bri=7     x=-2      y=2       (-4.0000, 4.0000)
1644: 02 F8           SVEC    scale=01(*4)   bri=0     x=2       y=0       (8.0000, 0.0000)
1646: 76 F6           SVEC    scale=00(*2)   bri=7     x=-2      y=-2      (-4.0000, -4.0000)
1648: 02 FE           SVEC    scale=01(*4)   bri=0     x=2       y=-2      (8.0000, -8.0000)
164A: 00 D0           RTS                         

; "Z"
164C: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
164E: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1650: 76 FF           SVEC    scale=01(*4)   bri=7     x=-2      y=-3      (-8.0000, -12.0000)
1652: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1654: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
1656: 00 D0           RTS                         

; SPACE
1658: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
165A: 00 D0           RTS                         

; "1"
165C: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
165E: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1660: 02 FF           SVEC    scale=01(*4)   bri=0     x=2       y=-3      (8.0000, -12.0000)
1662: 00 D0           RTS                         

; "2"
1664: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
1666: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1668: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
166A: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
166C: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
166E: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1670: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
1672: 00 D0           RTS                         
  
; "3"
1674: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1676: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
1678: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
167A: 00 F7           SVEC    scale=00(*2)   bri=0     x=0       y=-3      (0.0000, -6.0000)
167C: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
167E: 02 F7           SVEC    scale=00(*2)   bri=0     x=2       y=-3      (4.0000, -6.0000)
1680: 00 D0           RTS                         
  
; "4"
1682: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
1684: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
1686: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1688: 00 F3           SVEC    scale=00(*2)   bri=0     x=0       y=3       (0.0000, 6.0000)
168A: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
168C: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
168E: 00 D0           RTS                         

; "5"
1690: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
1692: 70 F3           SVEC    scale=00(*2)   bri=7     x=0       y=3       (0.0000, 6.0000)
1694: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
1696: 70 F3           SVEC    scale=00(*2)   bri=7     x=0       y=3       (0.0000, 6.0000)
1698: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
169A: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
169C: 00 D0           RTS                         

; "6"
169E: 00 F3           SVEC    scale=00(*2)   bri=0     x=0       y=3       (0.0000, 6.0000)
16A0: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
16A2: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
16A4: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
16A6: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
16A8: 03 FF           SVEC    scale=01(*4)   bri=0     x=3       y=-3      (12.0000, -12.0000)
16AA: 00 D0           RTS                         

; "7"
16AC: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
16AE: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
16B0: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
16B2: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
16B4: 00 D0           RTS                         

; "8"  
16B6: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
16B8: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
16BA: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
16BC: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
16BE: 00 F3           SVEC    scale=00(*2)   bri=0     x=0       y=3       (0.0000, 6.0000)
16C0: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
16C2: 02 F7           SVEC    scale=00(*2)   bri=0     x=2       y=-3      (4.0000, -6.0000)
16C4: 00 D0           RTS                         

; "9"  
16C6: 02 F8           SVEC    scale=01(*4)   bri=0     x=2       y=0       (8.0000, 0.0000)
16C8: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
16CA: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
16CC: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
16CE: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
16D0: 02 F7           SVEC    scale=00(*2)   bri=0     x=2       y=-3      (4.0000, -6.0000)
16D2: 00 D0           RTS                         

 ; Cross reference table for character data 
16D4: 2C CB           JSR     $0B2C ($1658)       ; SPACE 1
16D6: DD CA           JSR     $0ADD ($15BA)       ; O and 0 ... same pattern
16D8: 2E CB           JSR     $0B2E ($165C)       ; 1
16DA: 32 CB           JSR     $0B32 ($1664)       ; 2
16DC: 3A CB           JSR     $0B3A ($1674)       ; 3
16DE: 41 CB           JSR     $0B41 ($1682)       ; 4
16E0: 48 CB           JSR     $0B48 ($1690)       ; 5
16E2: 4F CB           JSR     $0B4F ($169E)       ; 6
16E4: 56 CB           JSR     $0B56 ($16AC)       ; 7 2
16E6: 5B CB           JSR     $0B5B ($16B6)       ; 8 3
16E8: 63 CB           JSR     $0B63 ($16C6)       ; 9 4
16EA: 78 CA           JSR     $0A78 ($14F0)       ; A 5
16EC: 80 CA           JSR     $0A80 ($1500)       ; B 6
16EE: 8D CA           JSR     $0A8D ($151A)       ; C 7
16F0: 93 CA           JSR     $0A93 ($1526)       ; D 8
16F2: 9B CA           JSR     $0A9B ($1536)       ; E 9
16F4: A3 CA           JSR     $0AA3 ($1546)       ; F 10
16F6: AA CA           JSR     $0AAA ($1554)       ; G 11
16F8: B3 CA           JSR     $0AB3 ($1566)       ; H 12
16FA: BA CA           JSR     $0ABA ($1574)       ; I 13
16FC: C1 CA           JSR     $0AC1 ($1582)       ; J 14
16FE: C7 CA           JSR     $0AC7 ($158E)       ; K 15
1700: CD CA           JSR     $0ACD ($159A)       ; L 16
1702: D2 CA           JSR     $0AD2 ($15A4)       ; M 17
1704: D8 CA           JSR     $0AD8 ($15B0)       ; N 18
1706: DD CA           JSR     $0ADD ($15BA)       ; O 19
1708: E3 CA           JSR     $0AE3 ($15C6)       ; P 20
170A: EA CA           JSR     $0AEA ($15D4)       ; Q 21
170C: F3 CA           JSR     $0AF3 ($15E6)       ; R 22
170E: FB CA           JSR     $0AFB ($15F6)       ; S 23
1710: 02 CB           JSR     $0B02 ($1604)       ; T 24
1712: 08 CB           JSR     $0B08 ($1610)       ; U 25
1714: 0E CB           JSR     $0B0E ($161C)       ; V 26
1716: 13 CB           JSR     $0B13 ($1626)       ; W 27
1718: 1A CB           JSR     $0B1A ($1634)       ; X 28
171A: 1F CB           JSR     $0B1F ($163E)       ; Y 29
171C: 26 CB           JSR     $0B26 ($164C)       ; Z 30
```

# Messages

```code
; Message offsets
171E: 0B  ; HIGH SCORES 
171F: 13  ; PLAYER
1720: 19  ; YOUR SCORE IS ONE OF THE TEN BEST 
1721: 2F  ; PEASE ENTER YOUR INITIALS
1722: 41  ; PUSH ROTATE TO SELECT LETTER 
1723: 55  ; PUSH HYPERSPACE WHEN LETTER IS CORRECT 
1724: 6F  ; PUSH START 
1725: 77  ; GAME OVER
1726: 7D  ; 1 COIN 2 PLAYS 
1727: 87  ; 1 COIN 1 PLAY 
1728: 91  ; 2 COINS 1 PLAY 
```

 Messages are packed with 3 characters in 2 bytes (3 5-bit characters).
 The upper 15 bits are used. If the last bit is set then the message terminates.
 If the last bit is clear then the next two bytes are parsed UNLESS the parser
 finds a 00000 character. That pattern terminates the message too.

 Here is the character map for a 5 bit character (00-1F):<br>
 "@_012ABCDEFGHIJKLMNOPQRSTUVWXYZ"<br>
 Again ... a 0 ("@") terminates the message

```code
; HIGH SCORES
; 01100_01101_01011_0 01100_00001_10111_0 00111_10011_10110_0 01001_10111_00000_0
; H     I     G       H     _     S       C     O     R       E     S     @ 
1729: 63 56 60 6E 3C EC 4D C0

; PLAYER_
; 10100_10000_00101_0 11101_01001_10110_0 00001_00000_00000_0 
; P     L     A       Y     E     R       _     @     @  
1731: A4 0A EA 6C 08 00 

; YOUR SCORE IS ONE OF THE TEN BEST
; 11101_10011_11001_0 10110_00001_10111_0 00111_10011_10110_0 01001_00001_01101_0 10111_00001_10011_0 10010_01001_00001_0 10011_01010_00001_0 11000_01100_01001_0 00001_11000_01001_0 10010_00001_00110_0 01001_10111_11000_1 
; Y     O     U       R     _     S       C     O     R       E     _     I       S     _     O       N     E     _       O     F     _       T     H     E       _     T     E       N     _     B       E     S     T     @ 
1737: EC F2 B0 6E 3C EC 48 5A B8 66 92 42 9A
1744: 82 C3 12 0E 12 90 4C 4D F1 

; PEASE ENTER YOUR INITIALS
; 10100_10000_01001_0 00101_10111_01001_0 00001_01001_10010_0 11000_01001_10110_0 00001_11101_10011_0 11001_10110_00001_0 01101_10010_01101_0 11000_01101_00101_0 10000_10111_00000_0 
; P     L     E       A     S     E       _     E     N       T     E     R       _     Y     O       U     R     _       I     N     I       T     I     A       L     S     @     
174D: A4 12 2D D2 0A 64 C2 6C 0F 66 CD 
1758: 82 6C 9A C3 4A 85 C0
 
; PUSH ROTATE TO SELECT LETTER
; 10100_11001_10111_0 01100_00001_10110_0 10011_11000_00101_0 11000_01001_00001_0 11000_10011_00001_0 10111_01001_10000_0 01001_00111_11000_0 00001_10000_01001_0 11000_11000_01001_0 10110_00000_00000_0 
; P     U     S       H     _     R       O     T     A       T     E     _       T     O     _       S     E     L       E     C     T       _     L     E       T     T     E       R     @     @     
175F: A6 6E 60 6C 9E 0A C2 42 C4 C2 BA
176A: 60 49 F0 0C 12 C6 12 B0 00 

; PUSH HYPERSPACE WHEN LETTER IS CORRECT
; 10100_11001_10111_0 01100_00001_01100_0 11101_10100_01001_0 10110_10111_10100_0 00101_00111_01001_0 00001_11011_01100_0 01001_10010_00001_0 10000_01001_11000_0 11000_01001_10110_0 00001_01101_10111_0 00001_00111_10011_0 10110_10110_01001_0 00111_11000_00000_0 
; P     U     S       H     _     H       Y     P     E       R     S     P       A     C     E       _     W     H       E     N     _       L     E     T       T     E     R       _     I     S       _     C     O       R     R     E       C     T     @     
1773: A6 6E 60 58 ED 12 B5 E8 29 D2 0E
177E: D8 4C 82 82 70 C2 6C 0B 6E 09 E6 B5
178A: 92 3E 00 

; PUSH START
; 10100_11001_10111_0 01100_00001_10111_0 11000_00101_10110_0 11000_00000_00000_0 
; P     U     S       H           S       T     A     R       T     @     @     
178D: A6 6E 60 6E C1 6C C0 00 

; GAME OVER
; 01011_00101_10001_0 01001_00001_10011_0 11010_01001_10110_1 
; G     A     M       E     _     O       V     E     R     @     
1795: 59 62 48 66 D2 6D 

; 1 COIN 2 PLAYS
; 00011_00001_00111_0 10011_01101_10010_0 00001_00100_00001_0 10100_10000_00101_0 11101_10111_00000_0 
; 1     _     C       O     I     N       _     2     _       P     L     A       Y     S     @    
179B: 18 4E 9B 64 09 02 A4 0A ED C0 

; 1 COIN 1 PLAY
; 00011_00001_00111_0 10011_01101_10010_0 00001_00011_00001_0 10100_10000_00101_0 11101_00000_00000_0 
; 1     _     C       O     I     N       _     1     _       P     L     A       Y     @     @ 
17A5: 18 4E 9B 64 08 C2 A4 0A E8  00 

; 2 COINS 1 PLAY
; 00100_00001_00111_0 10011_01101_10010_0 10111_00001_00011_0 00001_10100_10000_0 00101_11101_00000_0 
; 2     _     C       O     I     N       S     _     1       _     P     L       A     Y     @     
17AF: 20 4E 9B 64 B8 46 0D 20 2F 40 
```

# Sine lookup table

```code
; Used for vertical thrust (offset by 64 to get cosine for horizontal thrust)
17B9: 00 03 06
17BC: 09 0C 10 13
17C0: 16 19 1C 1F
17C4: 22 25 28 2B
17C8: 2E 31 33 36
17CC: 39 3C 3F 41
17D0: 44 47 49 4C
17D4: 4E 51 53 55
17D8: 58 5A 5C 5E
17DC: 60 62 64 66
17E0: 68 6A 6B 6D
17E4: 6F 70 71 73
17E8: 74 75 76 78
17EC: 79 7A 7A 7B
17F0: 7C 7D 7D 7E
17F4: 7E 7E 7F 7F
17F8: 7F 7F 

; Extra space
17FA: 00 00 00 00 00 00
```

```html
<script src="/js/Binary.js"></script>
<script src="/js/DVG.js"></script>
<script src="/js/Canvas.js"></script>
<script>
    window.onload = function() {   
        DVG.data = Binary.readBinary('VectorROM.md.bin')     
        Canvas.redrawGraphics()       
    }    
</script>
```

