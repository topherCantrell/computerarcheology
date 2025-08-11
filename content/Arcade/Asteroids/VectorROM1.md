![Asteroids DVG Vector ROM](Asteroids.jpg)

# Asteroids DVG Vector ROM

```
; OriginalBinary 035127.01 (Rev 1)

;;= TODO =

;; Lots of info here about what the areas in the ROM are:
;; [http://arcarc.xmission.com/Tech/dvg.txt http://arcarc.xmission.com/Tech/dvg.txt]

;; Thanks to [https://github.com/slx7R4GDZM slx7R4GDZM] for many fixes and discoveries here.

;;= DVG Info =

;; For info about the vector generator hardware and opcodes:
;;
;; [/Arcade/DVG.html DVG Information]

;;= Test Pattern =

; Diamond pattern across screen with a parallel
; line pattern in the center.

;;{{{html
;;<canvas width="520" height="520"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="screenScale=0.5,0800">
;;</canvas>
;;}}}

1000: 80 A0 00 00    LABS scale=00(/512)   y=128  x=0                 
1004: 00 70 00 00    VEC  scale=07(/4)    bri=00  x=0       y=0      (0.00, 0.00)
1008: 00 90 ff 73    VEC  scale=09(/1)    bri=07  x=1023    y=0      (1023.00, 0.00)
100C: ff 92 00 70    VEC  scale=09(/1)    bri=07  x=0       y=767    (0.00, 767.00)
1010: 00 90 ff 77    VEC  scale=09(/1)    bri=07  x=-1023   y=0      (-1023.00, 0.00)
1014: ff 96 00 70    VEC  scale=09(/1)    bri=07  x=0       y=-767   (0.00, -767.00)
;
1018: ff 92 ff 72    VEC  scale=09(/1)    bri=07  x=767     y=767    (767.00, 767.00)
101C: 00 86 00 72    VEC  scale=08(/2)    bri=07  x=512     y=-512   (256.00, -256.00)
1020: fe 87 fe 77    VEC  scale=08(/2)    bri=07  x=-1022   y=-1022  (-511.00, -511.00)
1024: 00 92 00 76    VEC  scale=09(/1)    bri=07  x=-512    y=512    (-512.00, 512.00)
1028: fe 81 00 72    VEC  scale=08(/2)    bri=07  x=512     y=510    (256.00, 255.00)
102C: ff 96 ff 72    VEC  scale=09(/1)    bri=07  x=767     y=-767   (767.00, -767.00)
;
1030: 7f a3 ff 03    LABS scale=00(/512)  y=895  x=1023
1034: 00 70 00 00    VEC  scale=07(/4)    bri=00  x=0       y=0      (0.00, 0.00)
1038: ff 96 ff 76    VEC  scale=09(/1)    bri=07  x=-767    y=-767   (-767.00, -767.00)
103C: fe 81 00 76    VEC  scale=08(/2)    bri=07  x=-512    y=510    (-256.00, 255.00)
1040: 00 92 00 72    VEC  scale=09(/1)    bri=07  x=512     y=512    (512.00, 512.00)
1044: fe 87 fe 73    VEC  scale=08(/2)    bri=07  x=1022    y=-1022  (511.00, -511.00)
1048: 00 86 00 76    VEC  scale=08(/2)    bri=07  x=-512    y=-512   (-256.00, -256.00)
104C: ff 92 ff 76    VEC  scale=09(/1)    bri=07  x=-767    y=767    (-767.00, 767.00)
;
1050: fc a1 f4 01    LABS scale=00(/512)  y=508  x=500
1054: 00 70 00 00    VEC  scale=07(/4)    bri=00  x=0       y=0      (0.00, 0.00)
1058: db f0          SVEC scale=02(/128)  bri=13  x=3       y=0      (0.02, 0.00)
105A: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
105C: cf f0          SVEC scale=02(/128)  bri=12  x=-3      y=0      (-0.02, 0.00)
105E: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
1060: bb f0          SVEC scale=02(/128)  bri=11  x=3       y=0      (0.02, 0.00)
1062: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
1064: af f0          SVEC scale=02(/128)  bri=10  x=-3      y=0      (-0.02, 0.00)
1066: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
1068: 9b f0          SVEC scale=02(/128)  bri=09  x=3       y=0      (0.02, 0.00)
106A: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
106C: 8f f0          SVEC scale=02(/128)  bri=08  x=-3      y=0      (-0.02, 0.00)
106E: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
1070: 7b f0          SVEC scale=02(/128)  bri=07  x=3       y=0      (0.02, 0.00)
1072: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
1074: 6f f0          SVEC scale=02(/128)  bri=06  x=-3      y=0      (-0.02, 0.00)
1076: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
1078: 5b f0          SVEC scale=02(/128)  bri=05  x=3       y=0      (0.02, 0.00)
107A: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
107C: 4f f0          SVEC scale=02(/128)  bri=04  x=-3      y=0      (-0.02, 0.00)
107E: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
1080: 3b f0          SVEC scale=02(/128)  bri=03  x=3       y=0      (0.02, 0.00)
1082: 00 f9          SVEC scale=01(/256)  bri=00  x=0       y=1      (0.00, 0.00)
1084: 2f f0          SVEC scale=02(/128)  bri=02  x=-3      y=0      (-0.02, 0.00)
1086: 4c d0          RTS                                               ; ?? 0x4c

;;= Page Select Error =

;;{{{html
;;<canvas width="500" height="60"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="x=20,y=45,baseScale=1,088C">
;;</canvas>
;;}}}

; "PAGE SELECT ERROR"
1088: e4 a0 2c 11    LABS scale=01(/256)  y=228  x=300                 
108C: 00 70 00 00    VEC  scale=07(/4)    bri=00  x=0       y=0      (0.00, 0.00)
1090: e4 ca          JSR  $0DC8                                        ; {} P
1092: 79 ca          JSR  $0CF2                                        ; {} A
1094: ab ca          JSR  $0D56                                        ; {} G
1096: 9c ca          JSR  $0D38                                        ; {} E
1098: 2d cb          JSR  $0E5A                                        ; {} SPACE
109A: fc ca          JSR  $0DF8                                        ; {} S
109C: 9c ca          JSR  $0D38                                        ; {} E
109E: ce ca          JSR  $0D9C                                        ; {} L
10A0: 9c ca          JSR  $0D38                                        ; {} E
10A2: 8e ca          JSR  $0D1C                                        ; {} C
10A4: 03 cb          JSR  $0E06                                        ; {} T
10A6: 2d cb          JSR  $0E5A                                        ; {} SPACE
10A8: 9c ca          JSR  $0D38                                        ; {} E
10AA: f4 ca          JSR  $0DE8                                        ; {} R
10AC: f4 ca          JSR  $0DE8                                        ; {} R
10AE: de ca          JSR  $0DBC                                        ; {} O
10B0: f4 ca          JSR  $0DE8                                        ; {} R
10B2: 00 d0          RTS                                               

;;= Credits =

;;{{{html
;;<canvas width="500" height="60"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="x=20,y=45,baseScale=1,08B8">
;;</canvas>
;;}}}

; "ASTEROIDS BY ATARI"
10B4: 80 a0 7c 01    LABS scale=00(/512)  y=128  x=380                 
10B8: 00 70 00 00    VEC  scale=07(/4)    bri=00  x=0       y=0      (0.00, 0.00)
10BC: 79 ca          JSR  $0CF2                                        ; {} A
10BE: fc ca          JSR  $0DF8                                        ; {} S
10C0: 03 cb          JSR  $0E06                                        ; {} T
10C2: 9c ca          JSR  $0D38                                        ; {} E
10C4: f4 ca          JSR  $0DE8                                        ; {} R
10C6: de ca          JSR  $0DBC                                        ; {} O
10C8: bb ca          JSR  $0D76                                        ; {} I
10CA: 94 ca          JSR  $0D28                                        ; {} D
10CC: fc ca          JSR  $0DF8                                        ; {} S
10CE: 2d cb          JSR  $0E5A                                        ; {} SPACE
10D0: 81 ca          JSR  $0D02                                        ; {} B
10D2: 20 cb          JSR  $0E40                                        ; {} Y
10D4: 2d cb          JSR  $0E5A                                        ; {} SPACE
10D6: 79 ca          JSR  $0CF2                                        ; {} A
10D8: 03 cb          JSR  $0E06                                        ; {} T
10DA: 79 ca          JSR  $0CF2                                        ; {} A
10DC: f4 ca          JSR  $0DE8                                        ; {} R
10DE: bb ca          JSR  $0D76                                        ; {} I
10E0: 00 d0          RTS                                               

; Ship Explosion
10E2: c6 ff          SVEC scale=01(/256)  bri=12  x=-2      y=-3     (-0.01, -0.01)
10E4: c1 fe          SVEC scale=01(/256)  bri=12  x=1       y=-2     (0.00, -0.01)
10E6: c3 f1          SVEC scale=00(/512)  bri=12  x=3       y=1      (0.01, 0.00)
10E8: cd f1          SVEC scale=02(/128)  bri=12  x=-1      y=1      (-0.01, 0.01)
10EA: c7 f1          SVEC scale=00(/512)  bri=12  x=-3      y=1      (-0.01, 0.00)
10EC: c1 fd          SVEC scale=01(/256)  bri=12  x=1       y=-1     (0.00, -0.00)
10EE: d8 1e 32 ec    VEC  scale=01(/256)  bri=14  x=-50     y=-728   (-0.20, -2.84)
10F2: 00 c4          JSR  $0000                                        ; Do routine at start of vector RAM
10F4: 3c 14 0a 46    VEC  scale=01(/256)  bri=04  x=-522    y=-60    (-2.04, -0.23)
10F8: d8 d8          RTS                                               ; ?? 0x8d8


;;= Shrapnel Patterns =

;; This is used when the player's shot hits something.
;;
;; Notice that all four patterns are the same just slightly spread out. This is extremely
;; clever. You could use one pattern and vary the scale to make it look like it is
;; spreading out. But the scale jumps are powers-of-two. These slightly-scaled patterns
;; can be used to take up the gaps in the large scaling doubles!

;;{{{html
;;<canvas width="420" height="100"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="baseScale=0,x=50,y=50,09A2,x=150,y=50,096C,x=250,y=50,092E,x=350,y=50,0902">
;;</canvas>
;;}}}

; Jump table for 4
10FA: d1 c8          JSR  $09A2                                        ; {}
10FC: b6 c8          JSR  $096C                                        ; {}
10FE: 97 c8          JSR  $092E                                        ; {}
1100: 81 c8          JSR  $0902                                        ; {}
;
; Shrapnel pattern 1
1102: 0d f8          SVEC scale=03(/64)   bri=00  x=-1      y=0      (-0.02, 0.00)
1104: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1106: 0d fd          SVEC scale=03(/64)   bri=00  x=-1      y=-1     (-0.02, -0.02)
1108: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
110A: 09 fd          SVEC scale=03(/64)   bri=00  x=1       y=-1     (0.02, -0.02)
110C: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
110E: 0B f1          SVEC scale=02(/128)  bri=00  x=3       y=1      (0.02, 0.01)
1110: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1112: 0a f5          SVEC scale=02(/128)  bri=00  x=2       y=-1     (0.02, -0.01)
1114: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1116: 08 f9          SVEC scale=03(/64)   bri=00  x=0       y=1      (0.00, 0.02)
1118: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
111A: 09 f3          SVEC scale=02(/128)  bri=00  x=1       y=3      (0.01, 0.02)
111C: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
111E: 0d f3          SVEC scale=02(/128)  bri=00  x=-1      y=3      (-0.01, 0.02)
1120: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1122: 80 54 00 06    VEC  scale=05(/16)   bri=00  x=-512    y=-128   (-32.00, -8.00)
1126: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1128: 0f f1          SVEC scale=02(/128)  bri=00  x=-3      y=1      (-0.02, 0.01)
112A: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
112C: 00 d0          RTS                                               
;
; Shrapnel pattern 2
112E: 00 30 80 07    VEC  scale=03(/64)   bri=00  x=-896    y=0      (-14.00, 0.00)
1132: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1134: 80 37 80 07    VEC  scale=03(/64)   bri=00  x=-896    y=-896   (-14.00, -14.00)
1138: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
113A: 80 37 80 03    VEC  scale=03(/64)   bri=00  x=896     y=-896   (14.00, -14.00)
113E: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1140: e0 40 a0 02    VEC  scale=04(/32)   bri=00  x=672     y=224    (21.00, 7.00)
1144: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1146: c0 35 80 03    VEC  scale=03(/64)   bri=00  x=896     y=-448   (14.00, -7.00)
114A: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
114C: 80 33 00 00    VEC  scale=03(/64)   bri=00  x=0       y=896    (0.00, 14.00)
1150: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1152: a0 42 e0 00    VEC  scale=04(/32)   bri=00  x=224     y=672    (7.00, 21.00)
1156: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1158: a0 42 e0 04    VEC  scale=04(/32)   br 
115C: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
115E: e0 44 80 07    VEC  scale=04(/32)   bri=00  x=-896    y=-224   (-28.00, -7.00)
1162: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1164: e0 40 a0 06    VEC  scale=04(/32)   bri=00  x=-672    y=224    (-21.00, 7.00)
1168: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
116A: 00 d0          RTS                                               
;
; Shrapnel pattern 3
116C: 07 f8          SVEC scale=01(/256)  bri=00  x=-3      y=0      (-0.01, 0.00)
116E: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1170: 07 ff          SVEC scale=01(/256)  bri=00  x=-3      y=-3     (-0.01, -0.01)
1172: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1174: 03 ff          SVEC scale=01(/256)  bri=00  x=3       y=-3     (0.01, -0.01)
1176: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1178: c0 40 40 02    VEC  scale=04(/32)   bri=00  x=576     y=192    (18.00, 6.00)
117C: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
117E: 80 35 00 03    VEC  scale=03(/64)   bri=00  x=768     y=-384   (12.00, -6.00)
1182: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1184: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
1186: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1188: 40 42 c0 00    VEC  scale=04(/32)   bri=00  x=192     y=576    (6.00, 18.00)
118C: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
118E: 40 42 c0 04    VEC  scale=04(/32)   bri=00  x=-192    y=576    (-6.00, 18.00)
1192: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
1194: c0 44 00 07    VEC  scale=04(/32)   bri=00  x=-768    y=-192   (-24.00, -6.00)
1198: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
119A: c0 40 40 06    VEC  scale=04(/32)   bri=00  x=-576    y=192    (-18.00, 6.00)
119E: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
11A0: 00 d0          RTS                                               
;
; Shrapnel pattern 4
11A2: 00 30 80 06    VEC  scale=03(/64)   bri=00  x=-640    y=0      (-10.00, 0.00)
11A6: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
11A8: 80 36 80 06    VEC  scale=03(/64)   bri=00  x=-640    y=-640   (-10.00, -10.00)
11AC: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
11AE: 80 36 80 02    VEC  scale=03(/64)   bri=00  x=640     y=-640   (10.00, -10.00)
11B2: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
11B4: 40 31 c0 03    VEC  scale=03(/64)   bri=00  x=960     y=320    (15.00, 5.00)
11B8: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
11BA: 40 35 80 02    VEC  scale=03(/64)   bri=00  x=640     y=-320   (10.00, -5.00)
11BE: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
11C0: 80 32 00 00    VEC  scale=03(/64)   bri=00  x=0       y=640    (0.00, 10.00)
11C4: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
11C6: c0 33 40 01    VEC  scale=03(/64)   bri=00  x=320     y=960    (5.00, 15.00)
11CA: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
11CC: c0 33 40 05    VEC  scale=03(/64)   bri=00  x=-320    y=960    (-5.00, 15.00)
11D0: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
11D2: a0 44 80 06    VEC  scale=04(/32)   bri=00  x=-640    y=-160   (-20.00, -5.00)
11D6: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
11D8: 40 31 c0 07    VEC  scale=03(/64)   bri=00  x=-960    y=320    (-15.00, 5.00)
11DC: 78 f8          SVEC scale=03(/64)   bri=07  x=0       y=0      (0.00, 0.00)
11DE: 00 d0          RTS                                               

;;= Rock Patterns =

;;{{{html
;;<canvas width="400" height="100"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="baseScale=0,x=50,y=50,09E8,x=150,y=50,0A00,x=250,y=50,0A1C,x=350,y=50,0A36">
;;</canvas>
;;}}}

; Jump table for 4
11E0: f4 c8          JSR  $09E8                                        ; {}
11E2: 00 c9          JSR  $0A00                                        ; {}
11E4: 0e c9          JSR  $0A1C                                        ; {}
11E6: 1b c9          JSR  $0A36                                        ; {}
;
; Rock Pattern 1
11E8: 08 f9          SVEC scale=03(/64)   bri=00  x=0       y=1      (0.00, 0.02)
11EA: 79 f9          SVEC scale=03(/64)   bri=07  x=1       y=1      (0.02, 0.02)
11EC: 79 fd          SVEC scale=03(/64)   bri=07  x=1       y=-1     (0.02, -0.02)
11EE: 7d f6          SVEC scale=02(/128)  bri=07  x=-1      y=-2     (-0.01, -0.02)
11F0: 79 f6          SVEC scale=02(/128)  bri=07  x=1       y=-2     (0.01, -0.02)
11F2: 8f f6          SVEC scale=02(/128)  bri=08  x=-3      y=-2     (-0.02, -0.02)
11F4: 8f f0          SVEC scale=02(/128)  bri=08  x=-3      y=0      (-0.02, 0.00)
11F6: 7d f9          SVEC scale=03(/64)   bri=07  x=-1      y=1      (-0.02, 0.02)
11F8: 78 fa          SVEC scale=03(/64)   bri=07  x=0       y=2      (0.00, 0.03)
11FA: 79 f9          SVEC scale=03(/64)   bri=07  x=1       y=1      (0.02, 0.02)
11FC: 79 fd          SVEC scale=03(/64)   bri=07  x=1       y=-1     (0.02, -0.02)
11FE: 00 d0          RTS                                               
;
; Rock Pattern 2
1200: 0a f1          SVEC scale=02(/128)  bri=00  x=2       y=1      (0.02, 0.01)
1202: 7a f1          SVEC scale=02(/128)  bri=07  x=2       y=1      (0.02, 0.01)
1204: 7d f9          SVEC scale=03(/64)   bri=07  x=-1      y=1      (-0.02, 0.02)
1206: 7e f5          SVEC scale=02(/128)  bri=07  x=-2      y=-1     (-0.02, -0.01)
1208: 7e f1          SVEC scale=02(/128)  bri=07  x=-2      y=1      (-0.02, 0.01)
120A: 7d fd          SVEC scale=03(/64)   bri=07  x=-1      y=-1     (-0.02, -0.02)
120C: 79 f6          SVEC scale=02(/128)  bri=07  x=1       y=-2     (0.01, -0.02)
120E: 7d f6          SVEC scale=02(/128)  bri=07  x=-1      y=-2     (-0.01, -0.02)
1210: 79 fd          SVEC scale=03(/64)   bri=07  x=1       y=-1     (0.02, -0.02)
1212: 79 f1          SVEC scale=02(/128)  bri=07  x=1       y=1      (0.01, 0.01)
1214: 8b f5          SVEC scale=02(/128)  bri=08  x=3       y=-1     (0.02, -0.01)
1216: 8a f3          SVEC scale=02(/128)  bri=08  x=2       y=3      (0.02, 0.02)
1218: 7d f9          SVEC scale=03(/64)   bri=07  x=-1      y=1      (-0.02, 0.02)
121A: 00 d0          RTS                                               
;
; Rock Pattern 3
121C: 0d f8          SVEC scale=03(/64)   bri=00  x=-1      y=0      (-0.02, 0.00)
121E: 7e f5          SVEC scale=02(/128)  bri=07  x=-2      y=-1     (-0.02, -0.01)
1220: 7a f7          SVEC scale=02(/128)  bri=07  x=2       y=-3     (0.02, -0.02)
1222: 7a f3          SVEC scale=02(/128)  bri=07  x=2       y=3      (0.02, 0.02)
1224: 78 f7          SVEC scale=02(/128)  bri=07  x=0       y=-3     (0.00, -0.02)
1226: 79 f8          SVEC scale=03(/64)   bri=07  x=1       y=0      (0.02, 0.00)
1228: 7a f3          SVEC scale=02(/128)  bri=07  x=2       y=3      (0.02, 0.02)
122A: 78 f9          SVEC scale=03(/64)   bri=07  x=0       y=1      (0.00, 0.02)
122C: 7e f3          SVEC scale=02(/128)  bri=07  x=-2      y=3      (-0.02, 0.02)
122E: 7f f0          SVEC scale=02(/128)  bri=07  x=-3      y=0      (-0.02, 0.00)
1230: 7f f7          SVEC scale=02(/128)  bri=07  x=-3      y=-3     (-0.02, -0.02)
1232: 7a f5          SVEC scale=02(/128)  bri=07  x=2       y=-1     (0.02, -0.01)
1234: 00 d0          RTS                                               
;
; Rock Pattern 4
1236: 09 f0          SVEC scale=02(/128)  bri=00  x=1       y=0      (0.01, 0.00)
1238: 7b f1          SVEC scale=02(/128)  bri=07  x=3       y=1      (0.02, 0.01)
123A: 68 f1          SVEC scale=02(/128)  bri=06  x=0       y=1      (0.00, 0.01)
123C: 7f f2          SVEC scale=02(/128)  bri=07  x=-3      y=2      (-0.02, 0.02)
123E: 7f f0          SVEC scale=02(/128)  bri=07  x=-3      y=0      (-0.02, 0.00)
1240: 69 f6          SVEC scale=02(/128)  bri=06  x=1       y=-2     (0.01, -0.02)
1242: 7f f0          SVEC scale=02(/128)  bri=07  x=-3      y=0      (-0.02, 0.00)
1244: 78 f7          SVEC scale=02(/128)  bri=07  x=0       y=-3     (0.00, -0.02)
1246: 7a f7          SVEC scale=02(/128)  bri=07  x=2       y=-3     (0.02, -0.02)
1248: 7b f1          SVEC scale=02(/128)  bri=07  x=3       y=1      (0.02, 0.01)
124A: 69 f5          SVEC scale=02(/128)  bri=06  x=1       y=-1     (0.01, -0.01)
124C: 69 f9          SVEC scale=03(/64)   bri=06  x=1       y=1      (0.02, 0.02)
124E: 7f f2          SVEC scale=02(/128)  bri=07  x=-3      y=2      (-0.02, 0.02)
1250: 00 d0          RTS                                               

;;= UFO =
;;{{{html
;;<canvas width="100" height="75"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="x=50,y=40,baseScale=0,0A54">
;;</canvas>
;;}}}

; Jump table for 1
1252: 2a c9          JSR  $0A54       
;                                  
1254: 0e f1          SVEC scale=02(/128)  bri=00  x=-2      y=1      (-0.02, 0.01)
1256: ca f8          SVEC scale=03(/64)   bri=12  x=2       y=0      (0.03, 0.00)
1258: 0B f6          SVEC scale=02(/128)  bri=00  x=3       y=-2     (0.02, -0.02)
125A: 00 60 80 d6    VEC  scale=06(/8)    bri=13  x=-640    y=0      (-80.00, 0.00)
125E: db f6          SVEC scale=02(/128)  bri=13  x=3       y=-2     (0.02, -0.02)
1260: ca f8          SVEC scale=03(/64)   bri=12  x=2       y=0      (0.03, 0.00)
1262: db f2          SVEC scale=02(/128)  bri=13  x=3       y=2      (0.02, 0.02)
1264: df f2          SVEC scale=02(/128)  bri=13  x=-3      y=2      (-0.02, 0.02)
1266: cd f2          SVEC scale=02(/128)  bri=12  x=-1      y=2      (-0.01, 0.02)
1268: cd f8          SVEC scale=03(/64)   bri=12  x=-1      y=0      (-0.02, 0.00)
126A: cd f6          SVEC scale=02(/128)  bri=12  x=-1      y=-2     (-0.01, -0.02)
126C: df f6          SVEC scale=02(/128)  bri=13  x=-3      y=-2     (-0.02, -0.02)
126E: 00 d0          RTS                                               

;;= Player Ships =

; Table for ships and thrusts based on player's direction.
; The addresses are where the ROM appears in the main CPU's
; memory map (begins at 5000). Thus 5292 - 5000 + 0800 = 0A92.
; The thrust pattern for each ship follows the ship itself.
;
1270: 92 52  ;{{#ShipDir0:ShipDir0:0}}
1272: aa 52  ;{{#ShipDir4:ShipDir4:0}}
1274: ce 52  ;{{#ShipDir8:ShipDir8:0}} 
1276: f2 52  ;{{#ShipDir12:ShipDir12:0}}
1278: 16 53  ;{{#ShipDir16:ShipDir16:0}}
127A: 38 53  ;{{#ShipDir20:ShipDir20:0}}
127C: 5c 53  ;{{#ShipDir24:ShipDir24:0}}
127E: 80 53  ;{{#ShipDir28:ShipDir28:0}}
1280: a4 53  ;{{#ShipDir32:ShipDir32:0}}
1282: c8 53  ;{{#ShipDir36:ShipDir36:0}}
1284: ec 53  ;{{#ShipDir40:ShipDir40:0}}
1286: 10 54  ;{{#ShipDir44:ShipDir44:0}}
1288: 34 54  ;{{#ShipDir48:ShipDir48:0}}
128A: 58 54  ;{{#ShipDir52:ShipDir52:0}}
128C: 7c 54  ;{{#ShipDir56:ShipDir56:0}}
128E: a0 54  ;{{#ShipDir60:ShipDir60:0}}
1290: c4 54  ;{{#ShipDir64:ShipDir64:0}}

;;{{{html
;;<canvas width="1060" height="100"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="baseScale=-1,
;;    x=50,y=50,A92,AA4,    
;;    x=110,y=50,0AAA,
;;    x=170,y=50,0ACE,
;;    x=230,y=50,0AF2,
;;    x=290,y=50,0B16,
;;    x=350,y=50,0B38,
;;    x=410,y=50,0B5C,
;;    x=470,y=50,0B80,
;;    x=530,y=50,0BA4,
;;    x=590,y=50,0BC8,
;;    x=650,y=50,0BEC,
;;    x=710,y=50,0C10,
;;    x=770,y=50,0C34,
;;    x=830,y=50,0C58,
;;    x=890,y=50,0C7C,
;;    x=950,y=50,0CA0,
;;    x=1010,y=50,0CC4,0CD6
;;  ">
;;</canvas>
;;}}}

ShipDir0:
1292: 0f f6          SVEC scale=02(/128)  bri=00  x=-3      y=-2     (-0.02, -0.02)
1294: c8 fa          SVEC scale=03(/64)   bri=12  x=0       y=2      (0.00, 0.03)
1296: bd f9          SVEC scale=03(/64)   bri=11  x=-1      y=1      (-0.02, 0.02)
1298: 00 65 00 c3    VEC  scale=06(/8)    bri=12  x=768     y=-256   (96.00, -32.00)
129C: 00 65 00 c7    VEC  scale=06(/8)    bri=12  x=-768    y=-256   (-96.00, -32.00)
12A0: b9 f9          SVEC scale=03(/64)   bri=11  x=1       y=1      (0.02, 0.02)
12A2: 00 d0          RTS                                               
ThrustDir0:
12A4: ce f9          SVEC scale=03(/64)   bri=12  x=-2      y=1      (-0.03, 0.02)
12A6: ca f9          SVEC scale=03(/64)   bri=12  x=2       y=1      (0.03, 0.02)
12A8: 00 d0          RTS                                               

ShipDir4:
12AA: 40 46 c0 06    VEC  scale=04(/32)   bri=00  x=-704    y=-576   (-22.00, -18.00)
12AE: 00 52 30 c4    VEC  scale=05(/16)   bri=12  x=-48     y=512    (-3.00, 32.00)
12B2: c0 41 20 c6    VEC  scale=04(/32)   bri=12  x=-544    y=448    (-17.00, 14.00)
12B6: b0 64 18 c3    VEC  scale=06(/8)    bri=12  x=792     y=-176   (99.00, -22.00)
12BA: 48 65 e0 c6    VEC  scale=06(/8)    bri=12  x=-736    y=-328   (-92.00, -41.00)
12BE: 20 42 c0 c1    VEC  scale=04(/32)   bri=12  x=448     y=544    (14.00, 17.00)
12C2: 00 d0          RTS                                               
ThrustDir4:
12C4: d0 50 10 c6    VEC  scale=05(/16)   bri=12  x=-528    y=208    (-33.00, 13.00)
12C8: 60 42 c0 c3    VEC  scale=04(/32)   bri=12  x=960     y=608    (30.00, 19.00)
12CC: 00 d0          RTS                                               

ShipDir8:
12CE: 80 46 80 06    VEC  scale=04(/32)   bri=00  x=-640    y=-640   (-20.00, -20.00)
12D2: e0 43 c0 c4    VEC  scale=04(/32)   bri=12  x=-192    y=992    (-6.00, 31.00)
12D6: a0 41 60 c6    VEC  scale=04(/32)   bri=12  x=-608    y=416    (-19.00, 13.00)
12DA: 68 64 20 c3    VEC  scale=06(/8)    bri=12  x=800     y=-104   (100.00, -13.00)
12DE: 90 65 c0 c6    VEC  scale=06(/8)    bri=12  x=-704    y=-400   (-88.00, -50.00)
12E2: 60 42 a0 c1    VEC  scale=04(/32)   bri=12  x=416     y=608    (13.00, 19.00)
12E6: 00 d0          RTS                                               
ThrustDir8:
12E8: 90 50 30 c6    VEC  scale=05(/16)   bri=12  x=-560    y=144    (-35.00, 9.00)
12EC: c0 42 80 c3    VEC  scale=04(/32)   bri=12  x=896     y=704    (28.00, 22.00)
12F0: 00 d0          RTS                                               

ShipDir12:
12F2: c0 46 40 06    VEC  scale=04(/32)   bri=00  x=-576    y=-704   (-18.00, -22.00)
12F6: e0 43 20 c5    VEC  scale=04(/32)   bri=12  x=-288    y=992    (-9.00, 31.00)
12FA: 60 41 80 c6    VEC  scale=04(/32)   bri=12  x=-640    y=352    (-20.00, 11.00)
12FE: 18 64 28 c3    VEC  scale=06(/8)    bri=12  x=808     y=-24    (101.00, -3.00)
1302: d0 65 98 c6    VEC  scale=06(/8)    bri=12  x=-664    y=-464   (-83.00, -58.00)
1306: 80 42 60 c1    VEC  scale=04(/32)   bri=12  x=352     y=640    (11.00, 20.00)
130A: 00 d0          RTS                                               
ThrustDir12:
130C: 60 50 30 c6    VEC  scale=05(/16)   bri=12  x=-560    y=96     (-35.00, 6.00)
1310: 20 43 40 c3    VEC  scale=04(/32)   bri=12  x=832     y=800    (26.00, 25.00)
1314: 00 d0          RTS                                               

ShipDir16:
1316: 0e f7          SVEC scale=02(/128)  bri=00  x=-2      y=-3     (-0.02, -0.02)
1318: c0 43 80 c5    VEC  scale=04(/32)   bri=12  x=-384    y=960    (-12.00, 30.00)
131C: 20 41 a0 c6    VEC  scale=04(/32)   bri=12  x=-672    y=288    (-21.00, 9.00)
1320: 38 60 28 c3    VEC  scale=06(/8)    bri=12  x=808     y=56     (101.00, 7.00)
1324: 10 66 60 c6    VEC  scale=06(/8)    bri=12  x=-608    y=-528   (-76.00, -66.00)
1328: a0 42 20 c1    VEC  scale=04(/32)   bri=12  x=288     y=672    (9.00, 21.00)
132C: 00 d0          RTS                                               
ThrustDir16:
132E: 30 50 40 c6    VEC  scale=05(/16)   bri=12  x=-576    y=48     (-36.00, 3.00)
1332: 60 43 e0 c2    VEC  scale=04(/32)   bri=12  x=736     y=864    (23.00, 27.00)
1336: 00 d0          RTS                                               

ShipDir20:
1338: 20 47 c0 05    VEC  scale=04(/32)   bri=00  x=-448    y=-800   (-14.00, -25.00)
133C: 80 43 e0 c5    VEC  scale=04(/32)   bri=12  x=-480    y=896    (-15.00, 28.00)
1340: e0 40 c0 c6    VEC  scale=04(/32)   bri=12  x=-704    y=224    (-22.00, 7.00)
1344: 88 60 20 c3    VEC  scale=06(/8)    bri=12  x=800     y=136    (100.00, 17.00)
1348: 48 66 30 c6    VEC  scale=06(/8)    bri=12  x=-560    y=-584   (-70.00, -73.00)
134C: c0 42 e0 c0    VEC  scale=04(/32)   bri=12  x=224     y=704    (7.00, 22.00)
1350: 00 d0          RTS                                               
ThrustDir20:
1352: 10 54 40 c6    VEC  scale=05(/16)   bri=12  x=-576    y=-16    (-36.00, -1.00)
1356: a0 43 a0 c2    VEC  scale=04(/32)   bri=12  x=672     y=928    (21.00, 29.00)
135A: 00 d0          RTS                                               

ShipDir24:
135C: 60 47 60 05    VEC  scale=04(/32)   bri=00  x=-352    y=-864   (-11.00, -27.00)
1360: 60 43 40 c6    VEC  scale=04(/32)   bri=12  x=-576    y=864    (-18.00, 27.00)
1364: 80 40 c0 c6    VEC  scale=04(/32)   bri=12  x=-704    y=128    (-22.00, 4.00)
1368: d8 60 10 c3    VEC  scale=06(/8)    bri=12  x=784     y=216    (98.00, 27.00)
136C: 80 66 f0 c5    VEC  scale=06(/8)    bri=12  x=-496    y=-640   (-62.00, -80.00)
1370: c0 42 80 c0    VEC  scale=04(/32)   bri=12  x=128     y=704    (4.00, 22.00)
1374: 00 d0          RTS                                               
ThrustDir24:
1376: 40 54 30 c6    VEC  scale=05(/16)   bri=12  x=-560    y=-64    (-35.00, -4.00)
137A: e0 43 40 c2    VEC  scale=04(/32)   bri=12  x=576     y=992    (18.00, 31.00)
137E: 00 d0          RTS                                               

ShipDir28:
1380: 80 47 00 05    VEC  scale=04(/32)   bri=00  x=-256    y=-896   (-8.00, -28.00)
1384: 20 43 80 c6    VEC  scale=04(/32)   bri=12  x=-640    y=800    (-20.00, 25.00)
1388: 40 40 e0 c6    VEC  scale=04(/32)   bri=12  x=-736    y=64     (-23.00, 2.00)
138C: 20 61 f8 c2    VEC  scale=06(/8)    bri=12  x=760     y=288    (95.00, 36.00)
1390: b0 66 b0 c5    VEC  scale=06(/8)    bri=12  x=-432    y=-688   (-54.00, -86.00)
1394: e0 42 40 c0    VEC  scale=04(/32)   bri=12  x=64      y=736    (2.00, 23.00)
1398: 00 d0          RTS                                               
ThrustDir28:
139A: 80 54 30 c6    VEC  scale=05(/16)   bri=12  x=-560    y=-128   (-35.00, -8.00)
139E: 10 52 f0 c0    VEC  scale=05(/16)   bri=12  x=240     y=528    (15.00, 33.00)
13A2: 00 d0          RTS                                               

ShipDir32:
13A4: 80 47 c0 04    VEC  scale=04(/32)   bri=00  x=-192    y=-896   (-6.00, -28.00)
13A8: e0 42 e0 c6    VEC  scale=04(/32)   bri=12  x=-736    y=736    (-23.00, 23.00)
13AC: 00 40 e0 c6    VEC  scale=04(/32)   bri=12  x=-736    y=0      (-23.00, 0.00)
13B0: 68 61 d8 c2    VEC  scale=06(/8)    bri=12  x=728     y=360    (91.00, 45.00)
13B4: d8 66 68 c5    VEC  scale=06(/8)    bri=12  x=-360    y=-728   (-45.00, -91.00)
13B8: e0 42 00 c0    VEC  scale=04(/32)   bri=12  x=0       y=736    (0.00, 23.00)
13BC: 00 d0          RTS                                               
ThrustDir32:
13BE: b0 54 20 c6    VEC  scale=05(/16)   bri=12  x=-544    y=-176   (-34.00, -11.00)
13C2: 20 52 b0 c0    VEC  scale=05(/16)   bri=12  x=176     y=544    (11.00, 34.00)
13C6: 00 d0          RTS                                               

ShipDir36:
13C8: a0 47 60 04    VEC  scale=04(/32)   bri=00  x=-96     y=-928   (-3.00, -29.00)
13CC: 80 42 20 c7    VEC  scale=04(/32)   bri=12  x=-800    y=640    (-25.00, 20.00)
13D0: 40 44 e0 c6    VEC  scale=04(/32)   bri=12  x=-736    y=-64    (-23.00, -2.00)
13D4: b0 61 b0 c2    VEC  scale=06(/8)    bri=12  x=688     y=432    (86.00, 54.00)
13D8: f8 66 20 c5    VEC  scale=06(/8)    bri=12  x=-288    y=-760   (-36.00, -95.00)
13DC: e0 42 40 c4    VEC  scale=04(/32)   bri=12  x=-64     y=736    (-2.00, 23.00)
13E0: 00 d0          RTS                                               
ThrustDir36:
13E2: f0 54 10 c6    VEC  scale=05(/16)   bri=12  x=-528    y=-240   (-33.00, -15.00)
13E6: 30 52 80 c0    VEC  scale=05(/16)   bri=12  x=128     y=560    (8.00, 35.00)
13EA: 00 d0          RTS                                               

ShipDir40:
13EC: a0 47 00 00    VEC  scale=04(/32)   bri=00  x=0       y=-928   (0.00, -29.00)
13F0: 40 42 60 c7    VEC  scale=04(/32)   bri=12  x=-864    y=576    (-27.00, 18.00)
13F4: 80 44 c0 c6    VEC  scale=04(/32)   bri=12  x=-704    y=-128   (-22.00, -4.00)
13F8: f0 61 80 c2    VEC  scale=06(/8)    bri=12  x=640     y=496    (80.00, 62.00)
13FC: 10 67 d8 c4    VEC  scale=06(/8)    bri=12  x=-216    y=-784   (-27.00, -98.00)
1400: c0 42 80 c4    VEC  scale=04(/32)   bri=12  x=-128    y=704    (-4.00, 22.00)
1404: 00 d0          RTS                                               
ThrustDir40:
1406: 40 46 e0 c7    VEC  scale=04(/32)   bri=12  x=-992    y=-576   (-31.00, -18.00)
140A: 30 52 40 c0    VEC  scale=05(/16)   bri=12  x=64      y=560    (4.00, 35.00)
140E: 00 d0          RTS                                               

ShipDir44:
1410: a0 47 60 00    VEC  scale=04(/32)   bri=00  x=96      y=-928   (3.00, -29.00)
1414: e0 41 80 c7    VEC  scale=04(/32)   bri=12  x=-896    y=480    (-28.00, 15.00)
1418: e0 44 c0 c6    VEC  scale=04(/32)   bri=12  x=-704    y=-224   (-22.00, -7.00)
141C: 30 62 48 c2    VEC  scale=06(/8)    bri=12  x=584     y=560    (73.00, 70.00)
1420: 20 67 88 c4    VEC  scale=06(/8)    bri=12  x=-136    y=-800   (-17.00, -100.00)
1424: c0 42 e0 c4    VEC  scale=04(/32)   bri=12  x=-224    y=704    (-7.00, 22.00)
1428: 00 d0          RTS                                               
ThrustDir44:
142A: a0 46 a0 c7    VEC  scale=04(/32)   bri=12  x=-928    y=-672   (-29.00, -21.00)
142E: 40 52 10 c0    VEC  scale=05(/16)   bri=12  x=16      y=576    (1.00, 36.00)
1432: 00 d0          RTS                                               

ShipDir48:
1434: 80 47 c0 00    VEC  scale=04(/32)   bri=00  x=192     y=-896   (6.00, -28.00)
1438: 80 41 c0 c7    VEC  scale=04(/32)   bri=12  x=-960    y=384    (-30.00, 12.00)
143C: 20 45 a0 c6    VEC  scale=04(/32)   bri=12  x=-672    y=-288   (-21.00, -9.00)
1440: 60 62 10 c2    VEC  scale=06(/8)    bri=12  x=528     y=608    (66.00, 76.00)
1444: 28 67 38 c4    VEC  scale=06(/8)    bri=12  x=-56     y=-808   (-7.00, -101.00)
1448: a0 42 20 c5    VEC  scale=04(/32)   bri=12  x=-288    y=672    (-9.00, 21.00)
144C: 00 d0          RTS                                               
ThrustDir48:
144E: e0 46 60 c7    VEC  scale=04(/32)   bri=12  x=-864    y=-736   (-27.00, -23.00)
1452: 40 52 30 c4    VEC  scale=05(/16)   bri=12  x=-48     y=576    (-3.00, 36.00)
1456: 00 d0          RTS                                               

ShipDir52:
1458: 80 47 00 01    VEC  scale=04(/32)   bri=00  x=256     y=-896   (8.00, -28.00)
145C: 20 41 e0 c7    VEC  scale=04(/32)   bri=12  x=-992    y=288    (-31.00, 9.00)
1460: 60 45 80 c6    VEC  scale=04(/32)   bri=12  x=-640    y=-352   (-20.00, -11.00)
1464: 98 62 d0 c1    VEC  scale=06(/8)    bri=12  x=464     y=664    (58.00, 83.00)
1468: 28 67 18 c0    VEC  scale=06(/8)    bri=12  x=24      y=-808   (3.00, -101.00)
146C: 80 42 60 c5    VEC  scale=04(/32)   bri=12  x=-352    y=640    (-11.00, 20.00)
1470: 00 d0          RTS                                               
ThrustDir52:
1472: 40 47 20 c7    VEC  scale=04(/32)   bri=12  x=-800    y=-832   (-25.00, -26.00)
1476: 30 52 60 c4    VEC  scale=05(/16)   bri=12  x=-96     y=560    (-6.00, 35.00)
147A: 00 d0          RTS                                               

ShipDir56:
147C: 60 47 60 01    VEC  scale=04(/32)   bri=00  x=352     y=-864   (11.00, -27.00)
1480: c0 40 e0 c7    VEC  scale=04(/32)   bri=12  x=-992    y=192    (-31.00, 6.00)
1484: a0 45 60 c6    VEC  scale=04(/32)   bri=12  x=-608    y=-416   (-19.00, -13.00)
1488: c0 62 90 c1    VEC  scale=06(/8)    bri=12  x=400     y=704    (50.00, 88.00)
148C: 20 67 68 c0    VEC  scale=06(/8)    bri=12  x=104     y=-800   (13.00, -100.00)
1490: 60 42 a0 c5    VEC  scale=04(/32)   bri=12  x=-416    y=608    (-13.00, 19.00)
1494: 00 d0          RTS                                               
ThrustDir56:
1496: 80 47 c0 c6    VEC  scale=04(/32)   bri=12  x=-704    y=-896   (-22.00, -28.00)
149A: 30 52 90 c4    VEC  scale=05(/16)   bri=12  x=-144    y=560    (-9.00, 35.00)
149E: 00 d0          RTS                                               

ShipDir60:
14A0: 20 47 c0 01    VEC  scale=04(/32)   bri=00  x=448     y=-800   (14.00, -25.00)
14A4: 30 50 00 c6    VEC  scale=05(/16)   bri=12  x=-512    y=48     (-32.00, 3.00)
14A8: c0 45 20 c6    VEC  scale=04(/32)   bri=12  x=-544    y=-448   (-17.00, -14.00)
14AC: e0 62 48 c1    VEC  scale=06(/8)    bri=12  x=328     y=736    (41.00, 92.00)
14B0: 18 67 b0 c0    VEC  scale=06(/8)    bri=12  x=176     y=-792   (22.00, -99.00)
14B4: 20 42 c0 c5    VEC  scale=04(/32)   bri=12  x=-448    y=544    (-14.00, 17.00)
14B8: 00 d0          RTS                                               
ThrustDir60:
14BA: c0 47 60 c6    VEC  scale=04(/32)   bri=12  x=-608    y=-960   (-19.00, -30.00)
14BE: 10 52 d0 c4    VEC  scale=05(/16)   bri=12  x=-208    y=528    (-13.00, 33.00)
14C2: 00 d0          RTS                                               

ShipDir64:
14C4: 0a f7          SVEC scale=02(/128)  bri=00  x=2       y=-3     (0.02, -0.02)
14C6: ce f8          SVEC scale=03(/64)   bri=12  x=-2      y=0      (-0.03, 0.00)
14C8: cd fd          SVEC scale=03(/64)   bri=12  x=-1      y=-1     (-0.02, -0.02)
14CA: 00 63 00 c1    VEC  scale=06(/8)    bri=12  x=256     y=768    (32.00, 96.00)
14CE: 00 67 00 c1    VEC  scale=06(/8)    bri=12  x=256     y=-768   (32.00, -96.00)
14D2: cd f9          SVEC scale=03(/64)   bri=12  x=-1      y=1      (-0.02, 0.02)
14D4: 00 d0          RTS                                               
ThrustDir64:
14D6: cd fe          SVEC scale=03(/64)   bri=12  x=-1      y=-2     (-0.02, -0.03)
14D8: cd fa          SVEC scale=03(/64)   bri=12  x=-1      y=2      (-0.02, 0.03)
14DA: 00 d0          RTS                                               

;;= Lives =

;; Ships in reserve. These are defined so you can draw them one right after the other (three drawn here).

;;{{{html
;;<canvas width="200" height="100"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="x=50,y=50,baseScale=-1,0CDC,0CDC,0CDC">
;;</canvas>
;;}}}

14DC: 0e f7          SVEC scale=02(/128)  bri=00  x=-2      y=-3     (-0.02, -0.02)
14DE: 7a f8          SVEC scale=03(/64)   bri=07  x=2       y=0      (0.03, 0.00)
14E0: 79 fd          SVEC scale=03(/64)   bri=07  x=1       y=-1     (0.02, -0.02)
14E2: 00 63 00 75    VEC  scale=06(/8)    bri=07  x=-256    y=768    (-32.00, 96.00)
14E6: 00 67 00 75    VEC  scale=06(/8)    bri=07  x=-256    y=-768   (-32.00, -96.00)
14EA: 79 f9          SVEC scale=03(/64)   bri=07  x=1       y=1      (0.02, 0.02)
14EC: c0 60 80 02    VEC  scale=06(/8)    bri=00  x=640     y=192    (80.00, 24.00)
14F0: 32 d0          RTS                                             ; ?? 0x32

;;= Characters =

;;{{{html
;;<canvas width="500" height="120"
;;  data-canvasFunction="DVG.handleDVGCanvas"
;;  data-origin="0800"
;;  data-command="x=30,y=45,baseScale=1,0CF2,0D02,0D1C,0D28,0D38,0D48,0D56,0D68,0D76,0D84,0D90,0D9C,0DA6,0DB2,0DBC,0DC8,0DD6,0DE8,x=30,y=90,0DF8,0E06,0E12,0E1E,0E28,0E36,0E40,0E4E,0E5A,0E5E,0E66,0E76,0E84,0E92,0EA0,0EAE,0EB8,0EC8">
;;</canvas>
;;}}}

; "A"
14F2: 70 fa          SVEC scale=01(/256)  bri=07  x=0       y=2      (0.00, 0.01)
14F4: 72 f2          SVEC scale=00(/512)  bri=07  x=2       y=2      (0.00, 0.00)
14F6: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
14F8: 70 fe          SVEC scale=01(/256)  bri=07  x=0       y=-2     (0.00, -0.01)
14FA: 06 f9          SVEC scale=01(/256)  bri=00  x=-2      y=1      (-0.01, 0.00)
14FC: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
14FE: 02 f6          SVEC scale=00(/512)  bri=00  x=2       y=-2     (0.00, -0.00)
1500: 00 d0          RTS                                               

; "B"
1502: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
1504: 73 f0          SVEC scale=00(/512)  bri=07  x=3       y=0      (0.01, 0.00)
1506: 61 f5          SVEC scale=00(/512)  bri=06  x=1       y=-1     (0.00, -0.00)
1508: 60 f5          SVEC scale=00(/512)  bri=06  x=0       y=-1     (0.00, -0.00)
150A: 65 f5          SVEC scale=00(/512)  bri=06  x=-1      y=-1     (-0.00, -0.00)
150C: 77 f0          SVEC scale=00(/512)  bri=07  x=-3      y=0      (-0.01, 0.00)
150E: 03 f0          SVEC scale=00(/512)  bri=00  x=3       y=0      (0.01, 0.00)
1510: 61 f5          SVEC scale=00(/512)  bri=06  x=1       y=-1     (0.00, -0.00)
1512: 60 f5          SVEC scale=00(/512)  bri=06  x=0       y=-1     (0.00, -0.00)
1514: 65 f5          SVEC scale=00(/512)  bri=06  x=-1      y=-1     (-0.00, -0.00)
1516: 77 f0          SVEC scale=00(/512)  bri=07  x=-3      y=0      (-0.01, 0.00)
1518: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
151A: 00 d0          RTS                                               

; "C"
151C: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
151E: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1520: 06 ff          SVEC scale=01(/256)  bri=00  x=-2      y=-3     (-0.01, -0.01)
1522: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1524: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
1526: 00 d0          RTS                                               

; "D"
1528: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
152A: 72 f0          SVEC scale=00(/512)  bri=07  x=2       y=0      (0.00, 0.00)
152C: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
152E: 70 f6          SVEC scale=00(/512)  bri=07  x=0       y=-2     (0.00, -0.00)
1530: 76 f6          SVEC scale=00(/512)  bri=07  x=-2      y=-2     (-0.00, -0.00)
1532: 76 f0          SVEC scale=00(/512)  bri=07  x=-2      y=0      (-0.00, 0.00)
1534: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
1536: 00 d0          RTS                                               

; "E"
1538: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
153A: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
153C: 05 f7          SVEC scale=00(/512)  bri=00  x=-1      y=-3     (-0.00, -0.01)
153E: 77 f0          SVEC scale=00(/512)  bri=07  x=-3      y=0      (-0.01, 0.00)
1540: 00 f7          SVEC scale=00(/512)  bri=00  x=0       y=-3     (0.00, -0.01)
1542: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1544: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
1546: 00 d0          RTS                                               

; "F"
1548: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
154A: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
154C: 05 f7          SVEC scale=00(/512)  bri=00  x=-1      y=-3     (-0.00, -0.01)
154E: 77 f0          SVEC scale=00(/512)  bri=07  x=-3      y=0      (-0.01, 0.00)
1550: 00 f7          SVEC scale=00(/512)  bri=00  x=0       y=-3     (0.00, -0.01)
1552: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
1554: 00 d0          RTS                                               

; "G"
1556: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
1558: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
155A: 70 f6          SVEC scale=00(/512)  bri=07  x=0       y=-2     (0.00, -0.00)
155C: 06 f6          SVEC scale=00(/512)  bri=00  x=-2      y=-2     (-0.00, -0.00)
155E: 72 f0          SVEC scale=00(/512)  bri=07  x=2       y=0      (0.00, 0.00)
1560: 70 f6          SVEC scale=00(/512)  bri=07  x=0       y=-2     (0.00, -0.00)
1562: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
1564: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
1566: 00 d0          RTS                                               

; "H"
1568: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
156A: 00 f7          SVEC scale=00(/512)  bri=00  x=0       y=-3     (0.00, -0.01)
156C: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
156E: 00 f3          SVEC scale=00(/512)  bri=00  x=0       y=3      (0.00, 0.01)
1570: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
1572: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
1574: 00 d0          RTS                                               

; "I"
1576: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1578: 06 f0          SVEC scale=00(/512)  bri=00  x=-2      y=0      (-0.00, 0.00)
157A: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
157C: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
157E: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
1580: 03 ff          SVEC scale=01(/256)  bri=00  x=3       y=-3     (0.01, -0.01)
1582: 00 d0          RTS                                               

; "J"
1584: 00 f2          SVEC scale=00(/512)  bri=00  x=0       y=2      (0.00, 0.00)
1586: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
1588: 72 f0          SVEC scale=00(/512)  bri=07  x=2       y=0      (0.00, 0.00)
158A: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
158C: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
158E: 00 d0          RTS                                               

; "K"
1590: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
1592: 03 f0          SVEC scale=00(/512)  bri=00  x=3       y=0      (0.01, 0.00)
1594: 77 f7          SVEC scale=00(/512)  bri=07  x=-3      y=-3     (-0.01, -0.01)
1596: 73 f7          SVEC scale=00(/512)  bri=07  x=3       y=-3     (0.01, -0.01)
1598: 03 f0          SVEC scale=00(/512)  bri=00  x=3       y=0      (0.01, 0.00)
159A: 00 d0          RTS                                               

; "L"
159C: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
159E: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
15A0: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
15A2: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
15A4: 00 d0          RTS                                               

; "M"
15A6: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
15A8: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
15AA: 72 f2          SVEC scale=00(/512)  bri=07  x=2       y=2      (0.00, 0.00)
15AC: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
15AE: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
15B0: 00 d0          RTS                                               

; "N"
15B2: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
15B4: 72 ff          SVEC scale=01(/256)  bri=07  x=2       y=-3     (0.01, -0.01)
15B6: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
15B8: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
15BA: 00 d0          RTS                                               

; "O"
15BC: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
15BE: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
15C0: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
15C2: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
15C4: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
15C6: 00 d0          RTS                                               

; "P"
15C8: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
15CA: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
15CC: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
15CE: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
15D0: 03 f7          SVEC scale=00(/512)  bri=00  x=3       y=-3     (0.01, -0.01)
15D2: 03 f0          SVEC scale=00(/512)  bri=00  x=3       y=0      (0.01, 0.00)
15D4: 00 d0          RTS                                               

; "Q"
15D6: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
15D8: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
15DA: 70 fe          SVEC scale=01(/256)  bri=07  x=0       y=-2     (0.00, -0.01)
15DC: 76 f6          SVEC scale=00(/512)  bri=07  x=-2      y=-2     (-0.00, -0.00)
15DE: 76 f0          SVEC scale=00(/512)  bri=07  x=-2      y=0      (-0.00, 0.00)
15E0: 02 f2          SVEC scale=00(/512)  bri=00  x=2       y=2      (0.00, 0.00)
15E2: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
15E4: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
15E6: 00 d0          RTS                                               

; "R"
15E8: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
15EA: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
15EC: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
15EE: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
15F0: 01 f0          SVEC scale=00(/512)  bri=00  x=1       y=0      (0.00, 0.00)
15F2: 73 f7          SVEC scale=00(/512)  bri=07  x=3       y=-3     (0.01, -0.01)
15F4: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
15F6: 00 d0          RTS                                               

; "S"
15F8: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
15FA: 70 f3          SVEC scale=00(/512)  bri=07  x=0       y=3      (0.00, 0.01)
15FC: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
15FE: 70 f3          SVEC scale=00(/512)  bri=07  x=0       y=3      (0.00, 0.01)
1600: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1602: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
1604: 00 d0          RTS                                               

; "T"
1606: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
1608: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
160A: 06 f0          SVEC scale=00(/512)  bri=00  x=-2      y=0      (-0.00, 0.00)
160C: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
160E: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
1610: 00 d0          RTS                                               

; "U"
1612: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
1614: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
1616: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1618: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
161A: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
161C: 00 d0          RTS                                               

; "V"
161E: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
1620: 71 ff          SVEC scale=01(/256)  bri=07  x=1       y=-3     (0.00, -0.01)
1622: 71 fb          SVEC scale=01(/256)  bri=07  x=1       y=3      (0.00, 0.01)
1624: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
1626: 00 d0          RTS                                               

; "W"
1628: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
162A: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
162C: 72 f2          SVEC scale=00(/512)  bri=07  x=2       y=2      (0.00, 0.00)
162E: 72 f6          SVEC scale=00(/512)  bri=07  x=2       y=-2     (0.00, -0.00)
1630: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
1632: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
1634: 00 d0          RTS                                               

; "X"
1636: 72 fb          SVEC scale=01(/256)  bri=07  x=2       y=3      (0.01, 0.01)
1638: 06 f8          SVEC scale=01(/256)  bri=00  x=-2      y=0      (-0.01, 0.00)
163A: 72 ff          SVEC scale=01(/256)  bri=07  x=2       y=-3     (0.01, -0.01)
163C: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
163E: 00 d0          RTS                                               

; "Y"
1640: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
1642: 70 fa          SVEC scale=01(/256)  bri=07  x=0       y=2      (0.00, 0.01)
1644: 76 f2          SVEC scale=00(/512)  bri=07  x=-2      y=2      (-0.00, 0.00)
1646: 02 f8          SVEC scale=01(/256)  bri=00  x=2       y=0      (0.01, 0.00)
1648: 76 f6          SVEC scale=00(/512)  bri=07  x=-2      y=-2     (-0.00, -0.00)
164A: 02 fe          SVEC scale=01(/256)  bri=00  x=2       y=-2     (0.01, -0.01)
164C: 00 d0          RTS                                               

; "Z"
164E: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
1650: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1652: 76 ff          SVEC scale=01(/256)  bri=07  x=-2      y=-3     (-0.01, -0.01)
1654: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1656: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
1658: 00 d0          RTS                                               

; SPACE
165A: 03 f8          SVEC scale=01(/256)  bri=00  x=3       y=0      (0.01, 0.00)
165C: 00 d0          RTS                                               

; "1"
165E: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
1660: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
1662: 02 ff          SVEC scale=01(/256)  bri=00  x=2       y=-3     (0.01, -0.01)
1664: 00 d0          RTS                                               

; "2"
1666: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
1668: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
166A: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
166C: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
166E: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
1670: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1672: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
1674: 00 d0          RTS                                               

; "3"
1676: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1678: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
167A: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
167C: 00 f7          SVEC scale=00(/512)  bri=00  x=0       y=-3     (0.00, -0.01)
167E: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1680: 02 f7          SVEC scale=00(/512)  bri=00  x=2       y=-3     (0.00, -0.01)
1682: 00 d0          RTS                                               

; "4"
1684: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
1686: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
1688: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
168A: 00 f3          SVEC scale=00(/512)  bri=00  x=0       y=3      (0.00, 0.01)
168C: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
168E: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
1690: 00 d0          RTS                                               

; "5"
1692: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
1694: 70 f3          SVEC scale=00(/512)  bri=07  x=0       y=3      (0.00, 0.01)
1696: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
1698: 70 f3          SVEC scale=00(/512)  bri=07  x=0       y=3      (0.00, 0.01)
169A: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
169C: 01 ff          SVEC scale=01(/256)  bri=00  x=1       y=-3     (0.00, -0.01)
169E: 00 d0          RTS                                               

; "6"
16A0: 00 f3          SVEC scale=00(/512)  bri=00  x=0       y=3      (0.00, 0.01)
16A2: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
16A4: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
16A6: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
16A8: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
16AA: 03 ff          SVEC scale=01(/256)  bri=00  x=3       y=-3     (0.01, -0.01)
16AC: 00 d0          RTS                                               

; "7"
16AE: 00 fb          SVEC scale=01(/256)  bri=00  x=0       y=3      (0.00, 0.01)
16B0: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
16B2: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
16B4: 02 f0          SVEC scale=00(/512)  bri=00  x=2       y=0      (0.00, 0.00)
16B6: 00 d0          RTS                                               

; "8"
16B8: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
16BA: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
16BC: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
16BE: 70 ff          SVEC scale=01(/256)  bri=07  x=0       y=-3     (0.00, -0.01)
16C0: 00 f3          SVEC scale=00(/512)  bri=00  x=0       y=3      (0.00, 0.01)
16C2: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
16C4: 02 f7          SVEC scale=00(/512)  bri=00  x=2       y=-3     (0.00, -0.01)
16C6: 00 d0          RTS                                               

; "9"
16C8: 02 f8          SVEC scale=01(/256)  bri=00  x=2       y=0      (0.01, 0.00)
16CA: 70 fb          SVEC scale=01(/256)  bri=07  x=0       y=3      (0.00, 0.01)
16CC: 76 f8          SVEC scale=01(/256)  bri=07  x=-2      y=0      (-0.01, 0.00)
16CE: 70 f7          SVEC scale=00(/512)  bri=07  x=0       y=-3     (0.00, -0.01)
16D0: 72 f8          SVEC scale=01(/256)  bri=07  x=2       y=0      (0.01, 0.00)
16D2: 02 f7          SVEC scale=00(/512)  bri=00  x=2       y=-3     (0.00, -0.01)
16D4: 00 d0          RTS                                               

; Cross reference table for character data
16D6: 2d cb          JSR  $0E5A                                        ; {} SPACE 1
16D8: de ca          JSR  $0DBC                                        ; {} O and 0 ... same pattern
16DA: 2f cb          JSR  $0E5E                                        ; {} 1
16DC: 33 cb          JSR  $0E66                                        ; {} 2
16DE: 3b cb          JSR  $0E76                                        ; {} 3
16E0: 42 cb          JSR  $0E84                                        ; {} 4
16E2: 49 cb          JSR  $0E92                                        ; {} 5
16E4: 50 cb          JSR  $0EA0                                        ; {} 6 
16E6: 57 cb          JSR  $0EAE                                        ; {} 7 2
16E8: 5c cb          JSR  $0EB8                                        ; {} 8 3
16EA: 64 cb          JSR  $0EC8                                        ; {} 9 4
16EC: 79 ca          JSR  $0CF2                                        ; {} A 5
16EE: 81 ca          JSR  $0D02                                        ; {} B 6
16F0: 8e ca          JSR  $0D1C                                        ; {} C 7
16F2: 94 ca          JSR  $0D28                                        ; {} D 8
16F4: 9c ca          JSR  $0D38                                        ; {} E 9
16F6: a4 ca          JSR  $0D48                                        ; {} F 10
16F8: ab ca          JSR  $0D56                                        ; {} G 11
16FA: b4 ca          JSR  $0D68                                        ; {} H 12
16FC: bb ca          JSR  $0D76                                        ; {} I 13
16FE: c2 ca          JSR  $0D84                                        ; {} J 14
1700: c8 ca          JSR  $0D90                                        ; {} K 15
1702: ce ca          JSR  $0D9C                                        ; {} L 16
1704: d3 ca          JSR  $0DA6                                        ; {} M 17
1706: d9 ca          JSR  $0DB2                                        ; {} N 18
1708: de ca          JSR  $0DBC                                        ; {} O 19
170A: e4 ca          JSR  $0DC8                                        ; {} P 20
170C: eb ca          JSR  $0DD6                                        ; {} Q 21
170E: f4 ca          JSR  $0DE8                                        ; {} R 22
1710: fc ca          JSR  $0DF8                                        ; {} S 23
1712: 03 cb          JSR  $0E06                                        ; {} T 24
1714: 09 cb          JSR  $0E12                                        ; {} U 25
1716: 0f cb          JSR  $0E1E                                        ; {} V 26
1718: 14 cb          JSR  $0E28                                        ; {} W 27
171A: 1b cb          JSR  $0E36                                        ; {} X 28
171C: 20 cb          JSR  $0E40                                        ; {} Y 29
171E: 27 cb          JSR  $0E4E                                        ; {} Z 30

;; = Messages =
; Message offsets
1720: 0B  ; HIGH SCORES
1721: 13  ; PLAYER
1722: 19  ; YOUR SCORE IS ONE OF THE TEN BEST
1723: 2f  ; PEASE ENTER YOUR INITIALS
1724: 41  ; PUSH ROTATE TO SELECT LETTER
1725: 55  ; PUSH HYPERSPACE WHEN LETTER IS CORRECT
1726: 6f  ; PUSH START
1727: 77  ; GAME OVER
1728: 7d  ; 1 COIN 2 PLAYS
1729: 87  ; 1 COIN 1 PLAY
172A: 91  ; 2 COINS 1 PLAY

;; Messages are packed with 3 characters in 2 bytes (3 5-bit characters).
;; The upper 15 bits are used. If the last bit is set then the message terminates.
;; If the last bit is clear then the next two bytes are parsed UNLESS the parser
;; finds a 00000 character. That pattern terminates the message too.
;;
;; Here is the character map for a 5 bit character (00-1F):[[BR]]
;; "@_012ABCDEFGHIJKLMNOPQRSTUVWXYZ"
;; Again ... a 0 ("@") terminates the message

; HIGH SCORES
; 01100_01101_01011_0 01100_00001_10111_0 00111_10011_10110_0 01001_10111_00000_0
; H     I     G       H     _     S       C     O     R       E     S     @ 
172B: 63 56 60 6e 3c ec 4d c0 
 
; PLAYER_
; 10100_10000_00101_0 11101_01001_10110_0 00001_00000_00000_0 
; P     L     A       Y     E     R       _     @     @  
1733: a4 0a ea 6c 08 00

; YOUR SCORE IS ONE OF THE TEN BEST
; 11101_10011_11001_0 10110_00001_10111_0 00111_10011_10110_0 01001_00001_01101_0 10111_00001_10011_0 10010_01001_00001_0 10011_01010_00001_0 11000_01100_01001_0 00001_11000_01001_0 10010_00001_00110_0 01001_10111_11000_1 
; Y     O     U       R     _     S       C     O     R       E     _     I       S     _     O       N     E     _       O     F     _       T     H     E       _     T     E       N     _     B       E     S     T     @ 
1739: ec f2 b0 6e 3c ec 48 5a b8 66 92 42 9a 82 c3 12 0e 12 90 4c 4d f1

; PEASE ENTER YOUR INITIALS
; 10100_10000_01001_0 00101_10111_01001_0 00001_01001_10010_0 11000_01001_10110_0 00001_11101_10011_0 11001_10110_00001_0 01101_10010_01101_0 11000_01101_00101_0 10000_10111_00000_0 
; P     L     E       A     S     E       _     E     N       T     E     R       _     Y     O       U     R     _       I     N     I       T     I     A       L     S     @     
174F: a4 12 2d d2 0a 64 c2 6c 0f 66 cd 82 6c 9a c3 4a 85 c0

; PUSH ROTATE TO SELECT LETTER
; 10100_11001_10111_0 01100_00001_10110_0 10011_11000_00101_0 11000_01001_00001_0 11000_10011_00001_0 10111_01001_10000_0 01001_00111_11000_0 00001_10000_01001_0 11000_11000_01001_0 10110_00000_00000_0 
; P     U     S       H     _     R       O     T     A       T     E     _       T     O     _       S     E     L       E     C     T       _     L     E       T     T     E       R     @     @     
1761: a6 6e 60 6c 9e 0a c2 42 c4 c2 ba 60 49 f0 0c 12 c6 12 b0 00

; PUSH HYPERSPACE WHEN LETTER IS CORRECT
; 10100_11001_10111_0 01100_00001_01100_0 11101_10100_01001_0 10110_10111_10100_0 00101_00111_01001_0 00001_11011_01100_0 01001_10010_00001_0 10000_01001_11000_0 11000_01001_10110_0 00001_01101_10111_0 00001_00111_10011_0 10110_10110_01001_0 00111_11000_00000_0 
; P     U     S       H     _     H       Y     P     E       R     S     P       A     C     E       _     W     H       E     N     _       L     E     T       T     E     R       _     I     S       _     C     O       R     R     E       C     T     @     
1775: a6 6e 60 58 ed 12 b5 e8 29 d2 0e d8 4c 82 82 70 c2 6c 0B 6e 09 e6 b5 92 3e 00

; PUSH START
; 10100_11001_10111_0 01100_00001_10111_0 11000_00101_10110_0 11000_00000_00000_0 
; P     U     S       H           S       T     A     R       T     @     @     
178F: a6 6e 60 6e c1 6c c0 00

; GAME OVER
; 01011_00101_10001_0 01001_00001_10011_0 11010_01001_10110_1 
; G     A     M       E     _     O       V     E     R     @     
1797: 59 62 48 66 d2 6d

; 1 COIN 2 PLAYS
; 00011_00001_00111_0 10011_01101_10010_0 00001_00100_00001_0 10100_10000_00101_0 11101_10111_00000_0 
; 1     _     C       O     I     N       _     2     _       P     L     A       Y     S     @    
179D: 18 4e 9b 64 09 02 a4 0a ed c0

; 1 COIN 1 PLAY
; 00011_00001_00111_0 10011_01101_10010_0 00001_00011_00001_0 10100_10000_00101_0 11101_00000_00000_0 
; 1     _     C       O     I     N       _     1     _       P     L     A       Y     @     @ 
17A7: 18 4e 9b 64 08 c2 a4 0a e8 00

; 2 COINS 1 PLAY
; 00100_00001_00111_0 10011_01101_10010_0 10111_00001_00011_0 00001_10100_10000_0 00101_11101_00000_0 
; 2     _     C       O     I     N       S     _     1       _     P     L       A     Y     @     
17B1: 20 4e 9b 64 b8 46 0d 20 2f 40

;; = Sine lookup table =
; Used for vertical thrust (offset by 64 to get cosine for horizontal thrust)
17BB: 00 03 06 09 0c 10 13 16
17C3: 19 1c 1f 22 25 28 2b 2e
17CB: 31 33 36 39 3c 3f 41 44
17D3: 47 49 4c 4e 51 53 55 58
17DB: 5a 5c 5e 60 62 64 66 68
17E3: 6a 6b 6d 6f 70 71 73 74
17EB: 75 76 78 79 7a 7a 7b 7c
17F3: 7d 7d 7e 7e 7e 7f 7f 7f
17FB: 7f

; Extra space
17FC: 00 00 00 00
```

```html
<script src="/js/Binary.js"></script>
<script src="/js/DVG.js"></script>
<script src="/js/Canvas.js"></script>
<script>
    window.onload = function() {   
        DVG.data = Binary.readBinary('VectorROM1.md.bin')     
        Canvas.redrawGraphics()       
    }    
</script>
```