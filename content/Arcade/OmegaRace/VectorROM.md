![DVG Vector ROM](ORace.jpg)

# Omeg Race DVG Vector ROM

>>> cpu DVG

>>> binary 1000:roms/omega.e1 + roms/omega.f1

For info about the vector generator hardware and opcodes:<br>
[DVG Information](../Asteroids/DVG.html)

The player ship sprites are first and last in the ROM. Each picture draws the player just a
little rotated CCW from the original position (facing right). Pictures come in pairs. The first
picture is the thrust stream for the ship. The second picture is the ship. The thrust stream
is drawn right where the ship picture ends.

 Note that there is no perfectly vertical picture. In the game you can't point perfectly vertical.

```code
ShipsA:
; The first ship image below shows the thrust pattern.
```

# Player (Part 1) 

```html
<canvas width="1225" height="100"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-colors='["#FFFFFF","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#635629","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C","#FFE55C"]'
  data-origin="1000"
  data-command="baseScale=1,x=50,y=50,100E,1000,x=125,y=50,104E,x=200,y=50,1090,x=275,y=50,10D2,x=350,y=50,1116,x=425,y=50,1156,x=500,y=50,1192,x=575,y=50,11D2,x=650,y=50,1212,x=725,y=50,1250,x=800,y=50,1290,x=875,y=50,12D0,x=950,y=50,130C,x=1025,y=50,134C,x=1100,y=50,1390,x=1175,y=50,13D2">
</canvas>
```

```code
; Thrust fragment                                                               
1000: BF 30 FF 07     VEC     scale=3(/64) x=-3FF y=BF   i=0   (-15.98 ,   2.98 )
1004: BF 34 3F F6     VEC     scale=3(/64) x=-23F y=-BF  i=15  ( -8.98 ,  -2.98 )
1008: 7F 34 3F F2     VEC     scale=3(/64) x=23F  y=-7F  i=15  (  8.98 ,  -1.98 )
100C: 00 D0           RTS                         
; Player facing right
100E: 00 20 7F 02     VEC     scale=2(/128)x=27F  y=0    i=0   (  4.99 ,   0.00 )
1012: 3F 41 7F F6     VEC     scale=4(/32) x=-27F y=13F  i=15  (-19.96 ,   9.96 )
1016: 9F 46 5F F1     VEC     scale=4(/32) x=15F  y=-29F i=15  ( 10.96 , -20.96 )
101A: F2 F8           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
101C: 7F 34 7F F6     VEC     scale=3(/64) x=-27F y=-7F  i=15  ( -9.98 ,  -1.98 )
1020: FF 41 1F F2     VEC     scale=4(/32) x=21F  y=1FF  i=15  ( 16.96 ,  15.96 )
1024: 7F 25 7F F2     VEC     scale=2(/128)x=27F  y=-17F i=15  (  4.99 ,  -2.99 )
1028: FF 24 7F F6     VEC     scale=2(/128)x=-27F y=-FF  i=15  ( -4.99 ,  -1.99 )
102C: FF 41 1F F6     VEC     scale=4(/32) x=-21F y=1FF  i=15  (-16.96 ,  15.96 )
1030: 7F 34 7F F2     VEC     scale=3(/64) x=27F  y=-7F  i=15  (  9.98 ,  -1.98 )
1034: F6 F8           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
1036: 9F 46 5F F5     VEC     scale=4(/32) x=-15F y=-29F i=15  (-10.96 , -20.96 )
103A: 1F 41 7F F2     VEC     scale=4(/32) x=27F  y=11F  i=15  ( 19.96 ,   8.96 )
103E: 00 D0           RTS                         
;
1040: 3F 30 FF 07     VEC     scale=3(/64) x=-3FF y=3F   i=0   (-15.98 ,   0.98 )
1044: BF 34 3F F6     VEC     scale=3(/64) x=-23F y=-BF  i=15  ( -8.98 ,  -2.98 )
1048: 7F 34 3F F2     VEC     scale=3(/64) x=23F  y=-7F  i=15  (  8.98 ,  -1.98 )
104C: 00 D0           RTS                         
;
104E: 00 20 7F 02     VEC     scale=2(/128)x=27F  y=0    i=0   (  4.99 ,   0.00 )
1052: FF 40 9F F6     VEC     scale=4(/32) x=-29F y=FF   i=15  (-20.96 ,   7.96 )
1056: 5F 46 9F F1     VEC     scale=4(/32) x=19F  y=-25F i=15  ( 12.96 , -18.96 )
105A: F2 F8           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
105C: BF 34 7F F6     VEC     scale=3(/64) x=-27F y=-BF  i=15  ( -9.98 ,  -2.98 )
1060: 3F 42 FF F1     VEC     scale=4(/32) x=1FF  y=23F  i=15  ( 15.96 ,  17.96 )
1064: FF 24 7F F2     VEC     scale=2(/128)x=27F  y=-FF  i=15  (  4.99 ,  -1.99 )
1068: 7F 25 7F F6     VEC     scale=2(/128)x=-27F y=-17F i=15  ( -4.99 ,  -2.99 )
106C: BF 41 3F F6     VEC     scale=4(/32) x=-23F y=1BF  i=15  (-17.96 ,  13.96 )
1070: 3F 34 7F F2     VEC     scale=3(/64) x=27F  y=-3F  i=15  (  9.98 ,  -0.98 )
1074: 7F 24 FF F7     VEC     scale=2(/128)x=-3FF y=-7F  i=15  ( -7.99 ,  -0.99 )
1078: BF 46 1F F5     VEC     scale=4(/32) x=-11F y=-2BF i=15  ( -8.96 , -21.96 )
107C: 5F 41 5F F2     VEC     scale=4(/32) x=25F  y=15F  i=15  ( 18.96 ,  10.96 )
1080: 00 D0           RTS                         
;
1082: 00 30 FF 07     VEC     scale=3(/64) x=-3FF y=0    i=0   (-15.98 ,   0.00 )
1086: FF 25 FF F7     VEC     scale=2(/128)x=-3FF y=-1FF i=15  ( -7.99 ,  -3.99 )
108A: 3F 34 3F F2     VEC     scale=3(/64) x=23F  y=-3F  i=15  (  8.98 ,  -0.98 )
108E: 00 D0           RTS                         
;
1090: 7F 20 7F 02     VEC     scale=2(/128)x=27F  y=7F   i=0   (  4.99 ,   0.99 )
1094: BF 40 BF F6     VEC     scale=4(/32) x=-2BF y=BF   i=15  (-21.96 ,   5.96 )
1098: 5F 46 DF F1     VEC     scale=4(/32) x=1DF  y=-25F i=15  ( 14.96 , -18.96 )
109C: FF 20 FF F3     VEC     scale=2(/128)x=3FF  y=FF   i=15  (  7.99 ,   1.99 )
10A0: FF 34 3F F6     VEC     scale=3(/64) x=-23F y=-FF  i=15  ( -8.98 ,  -3.98 )
10A4: 5F 42 9F F1     VEC     scale=4(/32) x=19F  y=25F  i=15  ( 12.96 ,  18.96 )
10A8: F3 F5           SVEC    scale=0(/128)x=200  y=0    i=15  (  4.00 ,   0.00 )
10AA: 7F 25 7F F6     VEC     scale=2(/128)x=-27F y=-17F i=15  ( -4.99 ,  -2.99 )
10AE: 7F 41 7F F6     VEC     scale=4(/32) x=-27F y=17F  i=15  (-19.96 ,  11.96 )
10B2: 3F 30 BF F2     VEC     scale=3(/64) x=2BF  y=3F   i=15  ( 10.98 ,   0.98 )
10B6: FF 24 FF F7     VEC     scale=2(/128)x=-3FF y=-FF  i=15  ( -7.99 ,  -1.99 )
10BA: DF 46 DF F4     VEC     scale=4(/32) x=-DF  y=-2DF i=15  ( -6.96 , -22.96 )
10BE: 9F 41 3F F2     VEC     scale=4(/32) x=23F  y=19F  i=15  ( 17.96 ,  12.96 )
10C2: 00 D0           RTS                         
;
10C4: 3F 34 FF 07     VEC     scale=3(/64) x=-3FF y=-3F  i=0   (-15.98 ,  -0.98 )
10C8: FF 26 FF F7     VEC     scale=2(/128)x=-3FF y=-2FF i=15  ( -7.99 ,  -5.99 )
10CC: 00 30 7F F2     VEC     scale=3(/64) x=27F  y=0    i=15  (  9.98 ,   0.00 )
10D0: 00 D0           RTS                         
;
10D2: 7F 20 7F 02     VEC     scale=2(/128)x=27F  y=7F   i=0   (  4.99 ,   0.99 )
10D6: 7F 40 BF F6     VEC     scale=4(/32) x=-2BF y=7F   i=15  (-21.96 ,   3.96 )
10DA: 1F 46 1F F2     VEC     scale=4(/32) x=21F  y=-21F i=15  ( 16.96 , -16.96 )
10DE: 7F 21 7F F3     VEC     scale=2(/128)x=37F  y=17F  i=15  (  6.99 ,   2.99 )
10E2: 3F 35 3F F6     VEC     scale=3(/64) x=-23F y=-13F i=15  ( -8.98 ,  -4.98 )
10E6: 7F 42 7F F1     VEC     scale=4(/32) x=17F  y=27F  i=15  ( 11.96 ,  19.96 )
10EA: 7F 24 7F F2     VEC     scale=2(/128)x=27F  y=-7F  i=15  (  4.99 ,  -0.99 )
10EE: 7F 26 FF F5     VEC     scale=2(/128)x=-1FF y=-27F i=15  ( -3.99 ,  -4.99 )
10F2: 5F 41 9F F6     VEC     scale=4(/32) x=-29F y=15F  i=15  (-20.96 ,  10.96 )
10F6: 7F 30 7F F2     VEC     scale=3(/64) x=27F  y=7F   i=15  (  9.98 ,   1.98 )
10FA: 7F 25 7F F7     VEC     scale=2(/128)x=-37F y=-17F i=15  ( -6.99 ,  -2.99 )
10FE: DF 46 7F F4     VEC     scale=4(/32) x=-7F  y=-2DF i=15  ( -3.96 , -22.96 )
1102: 7F 33 FF F3     VEC     scale=3(/64) x=3FF  y=37F  i=15  ( 15.98 ,  13.98 )
1106: 00 D0           RTS                         
;
1108: BF 34 FF 07     VEC     scale=3(/64) x=-3FF y=-BF  i=0   (-15.98 ,  -2.98 )
110C: FF 26 7F F7     VEC     scale=2(/128)x=-37F y=-2FF i=15  ( -6.99 ,  -5.99 )
1110: 3F 30 7F F2     VEC     scale=3(/64) x=27F  y=3F   i=15  (  9.98 ,   0.98 )
1114: 00 D0           RTS                         
;
1116: FF 20 7F 02     VEC     scale=2(/128)x=27F  y=FF   i=0   (  4.99 ,   1.99 )
111A: 1F 40 DF F6     VEC     scale=4(/32) x=-2DF y=1F   i=15  (-22.96 ,   0.96 )
111E: DF 45 3F F2     VEC     scale=4(/32) x=23F  y=-1DF i=15  ( 17.96 , -14.96 )
1122: F2 F9           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
1124: 7F 27 FF F7     VEC     scale=2(/128)x=-3FF y=-37F i=15  ( -7.99 ,  -6.99 )
1128: BF 42 1F F1     VEC     scale=4(/32) x=11F  y=2BF  i=15  (  8.96 ,  21.96 )
112C: 7F 24 FF F2     VEC     scale=2(/128)x=2FF  y=-7F  i=15  (  5.99 ,  -0.99 )
1130: 7F 26 FF F5     VEC     scale=2(/128)x=-1FF y=-27F i=15  ( -3.99 ,  -4.99 )
1134: 1F 41 BF F6     VEC     scale=4(/32) x=-2BF y=11F  i=15  (-21.96 ,   8.96 )
1138: BF 30 BF F2     VEC     scale=3(/64) x=2BF  y=BF   i=15  ( 10.98 ,   2.98 )
113C: F6 FD           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
113E: DF 46 3F F4     VEC     scale=4(/32) x=-3F  y=-2DF i=15  ( -1.96 , -22.96 )
1142: FF 33 BF F3     VEC     scale=3(/64) x=3BF  y=3FF  i=15  ( 14.98 ,  15.98 )
1146: 00 D0           RTS                         
;
1148: FF 34 BF 07     VEC     scale=3(/64) x=-3BF y=-FF  i=0   (-14.98 ,  -3.98 )
114C: 7F 27 7F F7     VEC     scale=2(/128)x=-37F y=-37F i=15  ( -6.99 ,  -6.99 )
1150: 3F 30 3F F2     VEC     scale=3(/64) x=23F  y=3F   i=15  (  8.98 ,   0.98 )
1154: 00 D0           RTS                         
;
1156: 02 F1           SVEC    scale=0(/128)x=200  y=0    i=0   (  4.00 ,   0.00 )
1158: 1F 44 BF F6     VEC     scale=4(/32) x=-2BF y=-1F  i=15  (-21.96 ,  -0.96 )
115C: 9F 45 5F F2     VEC     scale=4(/32) x=25F  y=-19F i=15  ( 18.96 , -12.96 )
1160: F2 F9           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
1162: BF 35 3F F6     VEC     scale=3(/64) x=-23F y=-1BF i=15  ( -8.98 ,  -6.98 )
1166: DF 42 FF F0     VEC     scale=4(/32) x=FF   y=2DF  i=15  (  7.96 ,  22.96 )
116A: F3 F0           SVEC    scale=0(/128)x=200  y=0    i=15  (  4.00 ,   0.00 )
116C: 7F 26 7F F5     VEC     scale=2(/128)x=-17F y=-27F i=15  ( -2.99 ,  -4.99 )
1170: BF 40 DF F6     VEC     scale=4(/32) x=-2DF y=BF   i=15  (-22.96 ,   5.96 )
1174: BF 30 BF F2     VEC     scale=3(/64) x=2BF  y=BF   i=15  ( 10.98 ,   2.98 )
1178: F6 FD           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
117A: DF 46 1F F0     VEC     scale=4(/32) x=1F   y=-2DF i=15  (  0.96 , -22.96 )
117E: 1F 42 7F F1     VEC     scale=4(/32) x=17F  y=21F  i=15  ( 11.96 ,  16.96 )
1182: 00 D0           RTS                         
;
1184: 7F 35 BF 07     VEC     scale=3(/64) x=-3BF y=-17F i=0   (-14.98 ,  -5.98 )
1188: 7F 27 FF F6     VEC     scale=2(/128)x=-2FF y=-37F i=15  ( -5.99 ,  -6.99 )
118C: 7F 30 7F F2     VEC     scale=3(/64) x=27F  y=7F   i=15  (  9.98 ,   1.98 )
1190: 00 D0           RTS                         
;
1192: FF 12 FF 03     VEC     scale=1(/256)x=3FF  y=2FF  i=0   (  3.99 ,   2.99 )
1196: 5F 44 BF F6     VEC     scale=4(/32) x=-2BF y=-5F  i=15  (-21.96 ,  -2.96 )
119A: 7F 45 7F F2     VEC     scale=4(/32) x=27F  y=-17F i=15  ( 19.96 , -11.96 )
119E: 7F 22 FF F3     VEC     scale=2(/128)x=3FF  y=27F  i=15  (  7.99 ,   4.99 )
11A2: F6 FE           SVEC    scale=1(/64) x=-200 y=-200 i=15  ( -8.00 ,  -8.00 )
11A4: FF 42 9F F0     VEC     scale=4(/32) x=9F   y=2FF  i=15  (  4.96 ,  23.96 )
11A8: F3 F0           SVEC    scale=0(/128)x=200  y=0    i=15  (  4.00 ,   0.00 )
11AA: 7F 26 FF F4     VEC     scale=2(/128)x=-FF  y=-27F i=15  ( -1.99 ,  -4.99 )
11AE: 7F 40 FF F6     VEC     scale=4(/32) x=-2FF y=7F   i=15  (-23.96 ,   3.96 )
11B2: FF 30 BF F2     VEC     scale=3(/64) x=2BF  y=FF   i=15  ( 10.98 ,   3.98 )
11B6: 7F 26 FF F7     VEC     scale=2(/128)x=-3FF y=-27F i=15  ( -7.99 ,  -4.99 )
11BA: DF 46 5F F0     VEC     scale=4(/32) x=5F   y=-2DF i=15  (  2.96 , -22.96 )
11BE: 5F 42 5F F1     VEC     scale=4(/32) x=15F  y=25F  i=15  ( 10.96 ,  18.96 )
11C2: 00 D0           RTS                         
;
11C4: BF 35 7F 07     VEC     scale=3(/64) x=-37F y=-1BF i=0   (-13.98 ,  -6.98 )
11C8: FF 27 7F F6     VEC     scale=2(/128)x=-27F y=-3FF i=15  ( -4.99 ,  -7.99 )
11CC: BF 30 3F F2     VEC     scale=3(/64) x=23F  y=BF   i=15  (  8.98 ,   2.98 )
11D0: 00 D0           RTS                         
;
11D2: FF 12 FF 03     VEC     scale=1(/256)x=3FF  y=2FF  i=0   (  3.99 ,   2.99 )
11D6: 7F 44 BF F6     VEC     scale=4(/32) x=-2BF y=-7F  i=15  (-21.96 ,  -3.96 )
11DA: 3F 45 BF F2     VEC     scale=4(/32) x=2BF  y=-13F i=15  ( 21.96 ,  -9.96 )
11DE: 7F 22 7F F3     VEC     scale=2(/128)x=37F  y=27F  i=15  (  6.99 ,   4.99 )
11E2: F6 FE           SVEC    scale=1(/64) x=-200 y=-200 i=15  ( -8.00 ,  -8.00 )
11E4: DF 42 7F F0     VEC     scale=4(/32) x=7F   y=2DF  i=15  (  3.96 ,  22.96 )
11E8: 7F 20 7F F2     VEC     scale=2(/128)x=27F  y=7F   i=15  (  4.99 ,   0.99 )
11EC: 7F 26 FF F4     VEC     scale=2(/128)x=-FF  y=-27F i=15  ( -1.99 ,  -4.99 )
11F0: 1F 40 DF F6     VEC     scale=4(/32) x=-2DF y=1F   i=15  (-22.96 ,   0.96 )
11F4: 7F 31 3F F2     VEC     scale=3(/64) x=23F  y=17F  i=15  (  8.98 ,   5.98 )
11F8: F7 F7           SVEC    scale=0(/128)x=-200 y=-200 i=15  ( -4.00 ,  -4.00 )
11FA: DF 46 9F F0     VEC     scale=4(/32) x=9F   y=-2DF i=15  (  4.96 , -22.96 )
11FE: 7F 42 1F F1     VEC     scale=4(/32) x=11F  y=27F  i=15  (  8.96 ,  19.96 )
1202: 00 D0           RTS                         
;
1204: 3F 36 3F 07     VEC     scale=3(/64) x=-33F y=-23F i=0   (-12.98 ,  -8.98 )
1208: FF 27 FF F5     VEC     scale=2(/128)x=-1FF y=-3FF i=15  ( -3.99 ,  -7.99 )
120C: FF 21 FF F3     VEC     scale=2(/128)x=3FF  y=1FF  i=15  (  7.99 ,   3.99 )
1210: 00 D0           RTS                         
;
1212: 02 F2           SVEC    scale=0(/128)x=200  y=200  i=0   (  4.00 ,   4.00 )
1214: DF 44 9F F6     VEC     scale=4(/32) x=-29F y=-DF  i=15  (-20.96 ,  -6.96 )
1218: FF 44 BF F2     VEC     scale=4(/32) x=2BF  y=-FF  i=15  ( 21.96 ,  -7.96 )
121C: F3 F3           SVEC    scale=0(/128)x=200  y=200  i=15  (  4.00 ,   4.00 )
121E: 3F 36 7F F5     VEC     scale=3(/64) x=-17F y=-23F i=15  ( -5.98 ,  -8.98 )
1222: FF 42 1F F0     VEC     scale=4(/32) x=1F   y=2FF  i=15  (  0.96 ,  23.96 )
1226: 7F 20 7F F2     VEC     scale=2(/128)x=27F  y=7F   i=15  (  4.99 ,   0.99 )
122A: 7F 26 7F F4     VEC     scale=2(/128)x=-7F  y=-27F i=15  ( -0.99 ,  -4.99 )
122E: 1F 44 FF F6     VEC     scale=4(/32) x=-2FF y=-1F  i=15  (-23.96 ,  -0.96 )
1232: 7F 31 3F F2     VEC     scale=3(/64) x=23F  y=17F  i=15  (  8.98 ,   5.98 )
1236: F7 F7           SVEC    scale=0(/128)x=-200 y=-200 i=15  ( -4.00 ,  -4.00 )
1238: BF 46 FF F0     VEC     scale=4(/32) x=FF   y=-2BF i=15  (  7.96 , -21.96 )
123C: 9F 42 DF F0     VEC     scale=4(/32) x=DF   y=29F  i=15  (  6.96 ,  20.96 )
1240: 00 D0           RTS                         
;
1242: 7F 36 FF 06     VEC     scale=3(/64) x=-2FF y=-27F i=0   (-11.98 ,  -9.98 )
1246: 3F 36 BF F4     VEC     scale=3(/64) x=-BF  y=-23F i=15  ( -2.98 ,  -8.98 )
124A: 7F 22 FF F3     VEC     scale=2(/128)x=3FF  y=27F  i=15  (  7.99 ,   4.99 )
124E: 00 D0           RTS                         
;
1250: FF 13 FF 02     VEC     scale=1(/256)x=2FF  y=3FF  i=0   (  2.99 ,   3.99 )
1254: 1F 45 7F F6     VEC     scale=4(/32) x=-27F y=-11F i=15  (-19.96 ,  -8.96 )
1258: 9F 44 DF F2     VEC     scale=4(/32) x=2DF  y=-9F  i=15  ( 22.96 ,  -4.96 )
125C: F3 F3           SVEC    scale=0(/128)x=200  y=200  i=15  (  4.00 ,   4.00 )
125E: 3F 36 7F F5     VEC     scale=3(/64) x=-17F y=-23F i=15  ( -5.98 ,  -8.98 )
1262: DF 42 1F F4     VEC     scale=4(/32) x=-1F  y=2DF  i=15  ( -0.96 ,  22.96 )
1266: FF 20 7F F2     VEC     scale=2(/128)x=27F  y=FF   i=15  (  4.99 ,   1.99 )
126A: 7F 26 7F F4     VEC     scale=2(/128)x=-7F  y=-27F i=15  ( -0.99 ,  -4.99 )
126E: 7F 44 DF F6     VEC     scale=4(/32) x=-2DF y=-7F  i=15  (-22.96 ,  -3.96 )
1272: F2 FA           SVEC    scale=1(/64) x=200  y=200  i=15  (  8.00 ,   8.00 )
1274: 7F 27 7F F6     VEC     scale=2(/128)x=-27F y=-37F i=15  ( -4.99 ,  -6.99 )
1278: BF 46 3F F1     VEC     scale=4(/32) x=13F  y=-2BF i=15  (  9.96 , -21.96 )
127C: BF 42 7F F0     VEC     scale=4(/32) x=7F   y=2BF  i=15  (  3.96 ,  21.96 )
1280: 00 D0           RTS                         
;
1282: BF 36 BF 06     VEC     scale=3(/64) x=-2BF y=-2BF i=0   (-10.98 , -10.98 )
1286: 7F 36 7F F4     VEC     scale=3(/64) x=-7F  y=-27F i=15  ( -1.98 ,  -9.98 )
128A: FF 22 7F F3     VEC     scale=2(/128)x=37F  y=2FF  i=15  (  6.99 ,   5.99 )
128E: 00 D0           RTS                         
;
1290: FF 13 FF 02     VEC     scale=1(/256)x=2FF  y=3FF  i=0   (  2.99 ,   3.99 )
1294: 5F 45 5F F6     VEC     scale=4(/32) x=-25F y=-15F i=15  (-18.96 , -10.96 )
1298: 5F 44 DF F2     VEC     scale=4(/32) x=2DF  y=-5F  i=15  ( 22.96 ,  -2.96 )
129C: FF 23 7F F2     VEC     scale=2(/128)x=27F  y=3FF  i=15  (  4.99 ,   7.99 )
12A0: BF 36 FF F4     VEC     scale=3(/64) x=-FF  y=-2BF i=15  ( -3.98 , -10.98 )
12A4: FF 42 7F F4     VEC     scale=4(/32) x=-7F  y=2FF  i=15  ( -3.96 ,  23.96 )
12A8: FF 20 7F F2     VEC     scale=2(/128)x=27F  y=FF   i=15  (  4.99 ,   1.99 )
12AC: F0 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
12AE: 9F 44 FF F6     VEC     scale=4(/32) x=-2FF y=-9F  i=15  (-23.96 ,  -4.96 )
12B2: F2 FA           SVEC    scale=1(/64) x=200  y=200  i=15  (  8.00 ,   8.00 )
12B4: FF 27 7F F6     VEC     scale=2(/128)x=-27F y=-3FF i=15  ( -4.99 ,  -7.99 )
12B8: 7F 46 7F F1     VEC     scale=4(/32) x=17F  y=-27F i=15  ( 11.96 , -19.96 )
12BC: BF 42 5F F0     VEC     scale=4(/32) x=5F   y=2BF  i=15  (  2.96 ,  21.96 )
12C0: 00 D0           RTS                         
;
12C2: 3F 37 7F 06     VEC     scale=3(/64) x=-27F y=-33F i=0   ( -9.98 , -12.98 )
12C6: 3F 36 3F F4     VEC     scale=3(/64) x=-3F  y=-23F i=15  ( -0.98 ,  -8.98 )
12CA: 7F 23 7F F3     VEC     scale=2(/128)x=37F  y=37F  i=15  (  6.99 ,   6.99 )
12CE: 00 D0           RTS                         
;
12D0: 01 F2           SVEC    scale=0(/128)x=0    y=200  i=0   (  0.00 ,   4.00 )
12D2: 7F 45 1F F6     VEC     scale=4(/32) x=-21F y=-17F i=15  (-16.96 , -11.96 )
12D6: 1F 44 DF F2     VEC     scale=4(/32) x=2DF  y=-1F  i=15  ( 22.96 ,  -0.96 )
12DA: F1 FA           SVEC    scale=1(/64) x=0    y=200  i=15  (  0.00 ,   8.00 )
12DC: BF 36 BF F4     VEC     scale=3(/64) x=-BF  y=-2BF i=15  ( -2.98 , -10.98 )
12E0: DF 42 BF F4     VEC     scale=4(/32) x=-BF  y=2DF  i=15  ( -5.96 ,  22.96 )
12E4: 7F 21 7F F2     VEC     scale=2(/128)x=27F  y=17F  i=15  (  4.99 ,   2.99 )
12E8: F0 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
12EA: FF 44 DF F6     VEC     scale=4(/32) x=-2DF y=-FF  i=15  (-22.96 ,  -7.96 )
12EE: 3F 32 BF F1     VEC     scale=3(/64) x=1BF  y=23F  i=15  (  6.98 ,   8.98 )
12F2: F5 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
12F4: 5F 46 9F F1     VEC     scale=4(/32) x=19F  y=-25F i=15  ( 12.96 , -18.96 )
12F8: BF 42 1F F0     VEC     scale=4(/32) x=1F   y=2BF  i=15  (  0.96 ,  21.96 )
12FC: 00 D0           RTS                         
;
12FE: 3F 37 FF 05     VEC     scale=3(/64) x=-1FF y=-33F i=0   ( -7.98 , -12.98 )
1302: 7F 36 3F F4     VEC     scale=3(/64) x=-3F  y=-27F i=15  ( -0.98 ,  -9.98 )
1306: 7F 23 FF F2     VEC     scale=2(/128)x=2FF  y=37F  i=15  (  5.99 ,   6.99 )
130A: 00 D0           RTS                         
;
130C: 7F 22 FF 00     VEC     scale=2(/128)x=FF   y=27F  i=0   (  1.99 ,   4.99 )
1310: BF 37 FF F7     VEC     scale=3(/64) x=-3FF y=-3BF i=15  (-15.98 , -14.98 )
1314: 3F 40 DF F2     VEC     scale=4(/32) x=2DF  y=3F   i=15  ( 22.96 ,   1.96 )
1318: F1 FA           SVEC    scale=1(/64) x=0    y=200  i=15  (  0.00 ,   8.00 )
131A: BF 36 BF F4     VEC     scale=3(/64) x=-BF  y=-2BF i=15  ( -2.98 , -10.98 )
131E: BF 42 1F F5     VEC     scale=4(/32) x=-11F y=2BF  i=15  ( -8.96 ,  21.96 )
1322: FF 21 7F F2     VEC     scale=2(/128)x=27F  y=1FF  i=15  (  4.99 ,   3.99 )
1326: FF 26 7F F0     VEC     scale=2(/128)x=7F   y=-2FF i=15  (  0.99 ,  -5.99 )
132A: 1F 45 BF F6     VEC     scale=4(/32) x=-2BF y=-11F i=15  (-21.96 ,  -8.96 )
132E: FF 23 7F F3     VEC     scale=2(/128)x=37F  y=3FF  i=15  (  6.99 ,   7.99 )
1332: F5 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
1334: 3F 46 DF F1     VEC     scale=4(/32) x=1DF  y=-23F i=15  ( 14.96 , -17.96 )
1338: DF 42 1F F4     VEC     scale=4(/32) x=-1F  y=2DF  i=15  ( -0.96 ,  22.96 )
133C: 00 D0           RTS                         
;
133E: 7F 37 BF 05     VEC     scale=3(/64) x=-1BF y=-37F i=0   ( -6.98 , -13.98 )
1342: 7F 36 00 F0     VEC     scale=3(/64) x=0    y=-27F i=15  (  0.00 ,  -9.98 )
1346: FF 23 FF F2     VEC     scale=2(/128)x=2FF  y=3FF  i=15  (  5.99 ,   7.99 )
134A: 00 D0           RTS                         
;
134C: 7F 22 7F 00     VEC     scale=2(/128)x=7F   y=27F  i=0   (  0.99 ,   4.99 )
1350: FF 37 7F F7     VEC     scale=3(/64) x=-37F y=-3FF i=15  (-13.98 , -15.98 )
1354: 7F 40 DF F2     VEC     scale=4(/32) x=2DF  y=7F   i=15  ( 22.96 ,   3.96 )
1358: 7F 23 7F F1     VEC     scale=2(/128)x=17F  y=37F  i=15  (  2.99 ,   6.99 )
135C: 7F 36 7F F4     VEC     scale=3(/64) x=-7F  y=-27F i=15  ( -1.98 ,  -9.98 )
1360: 9F 42 5F F5     VEC     scale=4(/32) x=-15F y=29F  i=15  (-10.96 ,  20.96 )
1364: FF 21 7F F2     VEC     scale=2(/128)x=27F  y=1FF  i=15  (  4.99 ,   3.99 )
1368: 7F 26 7F F0     VEC     scale=2(/128)x=7F   y=-27F i=15  (  0.99 ,  -4.99 )
136C: 7F 45 7F F6     VEC     scale=4(/32) x=-27F y=-17F i=15  (-19.96 , -11.96 )
1370: 3F 32 3F F1     VEC     scale=3(/64) x=13F  y=23F  i=15  (  4.98 ,   8.98 )
1374: 7F 27 7F F5     VEC     scale=2(/128)x=-17F y=-37F i=15  ( -2.99 ,  -6.99 )
1378: 1F 46 1F F2     VEC     scale=4(/32) x=21F  y=-21F i=15  ( 16.96 , -16.96 )
137C: BF 42 7F F4     VEC     scale=4(/32) x=-7F  y=2BF  i=15  ( -3.96 ,  21.96 )
1380: 00 D0           RTS                         
;
1382: BF 37 3F 05     VEC     scale=3(/64) x=-13F y=-3BF i=0   ( -4.98 , -14.98 )
1386: 3F 36 3F F0     VEC     scale=3(/64) x=3F   y=-23F i=15  (  0.98 ,  -8.98 )
138A: FF 23 FF F1     VEC     scale=2(/128)x=1FF  y=3FF  i=15  (  3.99 ,   7.99 )
;
138E: 00 D0           RTS                         
1390: 7F 22 7F 00     VEC     scale=2(/128)x=7F   y=27F  i=0   (  0.99 ,   4.99 )
1394: 3F 46 9F F5     VEC     scale=4(/32) x=-19F y=-23F i=15  (-12.96 , -17.96 )
1398: DF 40 DF F2     VEC     scale=4(/32) x=2DF  y=DF   i=15  ( 22.96 ,   6.96 )
139C: FF 23 FF F0     VEC     scale=2(/128)x=FF   y=3FF  i=15  (  1.99 ,   7.99 )
13A0: BF 36 3F F4     VEC     scale=3(/64) x=-3F  y=-2BF i=15  ( -0.98 , -10.98 )
13A4: 7F 42 7F F5     VEC     scale=4(/32) x=-17F y=27F  i=15  (-11.96 ,  19.96 )
13A8: 7F 22 7F F1     VEC     scale=2(/128)x=17F  y=27F  i=15  (  2.99 ,   4.99 )
13AC: F1 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
13AE: 9F 45 5F F6     VEC     scale=4(/32) x=-25F y=-19F i=15  (-18.96 , -12.96 )
13B2: 3F 32 FF F0     VEC     scale=3(/64) x=FF   y=23F  i=15  (  3.98 ,   8.98 )
13B6: FF 27 FF F4     VEC     scale=2(/128)x=-FF  y=-3FF i=15  ( -1.99 ,  -7.99 )
13BA: DF 45 5F F2     VEC     scale=4(/32) x=25F  y=-1DF i=15  ( 18.96 , -14.96 )
13BE: BF 42 BF F4     VEC     scale=4(/32) x=-BF  y=2BF  i=15  ( -5.96 ,  21.96 )
13C2: 00 D0           RTS                         
;
13C4: FF 37 FF 04     VEC     scale=3(/64) x=-FF  y=-3FF i=0   ( -3.98 , -15.98 )
13C8: 3F 36 7F F0     VEC     scale=3(/64) x=7F   y=-23F i=15  (  1.98 ,  -8.98 )
13CC: 3F 32 BF F0     VEC     scale=3(/64) x=BF   y=23F  i=15  (  2.98 ,   8.98 )
13D0: 00 D0           RTS                         
;
13D2: 7F 22 00 00     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
13D6: 5F 46 5F F5     VEC     scale=4(/32) x=-15F y=-25F i=15  (-10.96 , -18.96 )
13DA: 1F 41 BF F2     VEC     scale=4(/32) x=2BF  y=11F  i=15  ( 21.96 ,   8.96 )
13DE: FF 23 7F F0     VEC     scale=2(/128)x=7F   y=3FF  i=15  (  0.99 ,   7.99 )
13E2: 7F 36 3F F0     VEC     scale=3(/64) x=3F   y=-27F i=15  (  0.98 ,  -9.98 )
13E6: 3F 42 BF F5     VEC     scale=4(/32) x=-1BF y=23F  i=15  (-13.96 ,  17.96 )
13EA: 7F 22 7F F1     VEC     scale=2(/128)x=17F  y=27F  i=15  (  2.99 ,   4.99 )
13EE: 7F 26 FF F0     VEC     scale=2(/128)x=FF   y=-27F i=15  (  1.99 ,  -4.99 )
13F2: FF 45 3F F6     VEC     scale=4(/32) x=-23F y=-1FF i=15  (-17.96 , -15.96 )
13F6: 7F 32 BF F0     VEC     scale=3(/64) x=BF   y=27F  i=15  (  2.98 ,   9.98 )
13FA: F0 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
13FC: 9F 45 5F F2     VEC     scale=4(/32) x=25F  y=-19F i=15  ( 18.96 , -12.96 )
1400: 9F 42 FF F4     VEC     scale=4(/32) x=-FF  y=29F  i=15  ( -7.96 ,  20.96 )
1404: 00 D0           RTS                         

; ?? not used
1406: 3C FF           SVEC    scale=3(/16) x=0    y=-200 i=3   (  0.00 , -32.00 )
```

# Enemy Triangle 

Circle enemy with triangle (just one picture)

```html
<canvas width="100" height="100"
  data-command="baseScale=1,x=50,y=50,1408">
</canvas>
```

```code
EnemyTri:
1408: 00 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
140A: BF 36 BF F1     VEC     scale=3(/64) x=1BF  y=-2BF i=15  (  6.98 , -10.98 )
140E: 00 30 3F F7     VEC     scale=3(/64) x=-33F y=0    i=15  (-12.98 ,   0.00 )
1412: BF 32 7F F1     VEC     scale=3(/64) x=17F  y=2BF  i=15  (  5.98 ,  10.98 )
1416: 7F 34 FF 03     VEC     scale=3(/64) x=3FF  y=-7F  i=0   ( 15.98 ,  -1.98 )
141A: 7F 32 7F A6     VEC     scale=3(/64) x=-27F y=27F  i=10  ( -9.98 ,   9.98 )
141E: 00 30 BF A6     VEC     scale=3(/64) x=-2BF y=0    i=10  (-10.98 ,   0.00 )
1422: 7F 36 7F A6     VEC     scale=3(/64) x=-27F y=-27F i=10  ( -9.98 ,  -9.98 )
1426: BF 36 00 A0     VEC     scale=3(/64) x=0    y=-2BF i=10  (  0.00 , -10.98 )
142A: 7F 36 7F A2     VEC     scale=3(/64) x=27F  y=-27F i=10  (  9.98 ,  -9.98 )
142E: 00 30 BF A2     VEC     scale=3(/64) x=2BF  y=0    i=10  ( 10.98 ,   0.00 )
1432: 7F 32 7F A2     VEC     scale=3(/64) x=27F  y=27F  i=10  (  9.98 ,   9.98 )
1436: 9F 42 3F C5     VEC     scale=4(/32) x=-13F y=29F  i=12  ( -9.96 ,  20.96 )
143A: 3F 45 9F C6     VEC     scale=4(/32) x=-29F y=-13F i=12  (-20.96 ,  -9.96 )
143E: 9F 46 3F C1     VEC     scale=4(/32) x=13F  y=-29F i=12  (  9.96 , -20.96 )
1442: 3F 41 9F C2     VEC     scale=4(/32) x=29F  y=13F  i=12  ( 20.96 ,   9.96 )
1446: BF 32 00 A0     VEC     scale=3(/64) x=0    y=2BF  i=10  (  0.00 ,  10.98 )
144A: 3F 41 9F C6     VEC     scale=4(/32) x=-29F y=13F  i=12  (-20.96 ,   9.96 )
144E: 9F 46 3F C5     VEC     scale=4(/32) x=-13F y=-29F i=12  ( -9.96 , -20.96 )
1452: 3F 45 9F C2     VEC     scale=4(/32) x=29F  y=-13F i=12  ( 20.96 ,  -9.96 )
1456: 9F 42 3F C1     VEC     scale=4(/32) x=13F  y=29F  i=12  (  9.96 ,  20.96 )
145A: 00 D0           RTS                         
```

# Enemy (no triangle) 

Circle enemy (no triangle). There are three pictures for animation.

```html
<canvas width="250" height="100"
  data-command="baseScale=1,x=50,y=50,145C,x=125,y=50,14A2,x=200,y=50,14E8">
</canvas>
```

```code
EnemyNoTri:
145C: 7F 31 FF 03     VEC     scale=3(/64) x=3FF  y=17F  i=0   ( 15.98 ,   5.98 )
1460: 7F 32 7F 66     VEC     scale=3(/64) x=-27F y=27F  i=6   ( -9.98 ,   9.98 )
1464: 00 30 BF 66     VEC     scale=3(/64) x=-2BF y=0    i=6   (-10.98 ,   0.00 )
1468: 7F 36 7F 66     VEC     scale=3(/64) x=-27F y=-27F i=6   ( -9.98 ,  -9.98 )
146C: BF 36 00 60     VEC     scale=3(/64) x=0    y=-2BF i=6   (  0.00 , -10.98 )
1470: 7F 36 7F 62     VEC     scale=3(/64) x=27F  y=-27F i=6   (  9.98 ,  -9.98 )
1474: 00 30 BF 62     VEC     scale=3(/64) x=2BF  y=0    i=6   ( 10.98 ,   0.00 )
1478: 7F 32 7F 62     VEC     scale=3(/64) x=27F  y=27F  i=6   (  9.98 ,   9.98 )
147C: 9F 42 3F 85     VEC     scale=4(/32) x=-13F y=29F  i=8   ( -9.96 ,  20.96 )
1480: 3F 45 9F 86     VEC     scale=4(/32) x=-29F y=-13F i=8   (-20.96 ,  -9.96 )
1484: 9F 46 3F 81     VEC     scale=4(/32) x=13F  y=-29F i=8   (  9.96 , -20.96 )
1488: 3F 41 9F 82     VEC     scale=4(/32) x=29F  y=13F  i=8   ( 20.96 ,   9.96 )
148C: BF 32 00 60     VEC     scale=3(/64) x=0    y=2BF  i=6   (  0.00 ,  10.98 )
1490: 3F 41 9F 86     VEC     scale=4(/32) x=-29F y=13F  i=8   (-20.96 ,   9.96 )
1494: 9F 46 3F 85     VEC     scale=4(/32) x=-13F y=-29F i=8   ( -9.96 , -20.96 )
1498: 3F 45 9F 82     VEC     scale=4(/32) x=29F  y=-13F i=8   ( 20.96 ,  -9.96 )
149C: 9F 42 3F 81     VEC     scale=4(/32) x=13F  y=29F  i=8   (  9.96 ,  20.96 )
14A0: 00 D0           RTS                         
;
14A2: 7F 32 7F 03     VEC     scale=3(/64) x=37F  y=27F  i=0   ( 13.98 ,   9.98 )
14A6: BF 31 3F 67     VEC     scale=3(/64) x=-33F y=1BF  i=6   (-12.98 ,   6.98 )
14AA: BF 34 7F 66     VEC     scale=3(/64) x=-27F y=-BF  i=6   ( -9.98 ,  -2.98 )
14AE: 3F 37 BF 65     VEC     scale=3(/64) x=-1BF y=-33F i=6   ( -6.98 , -12.98 )
14B2: 7F 36 BF 60     VEC     scale=3(/64) x=BF   y=-27F i=6   (  2.98 ,  -9.98 )
14B6: BF 35 3F 63     VEC     scale=3(/64) x=33F  y=-1BF i=6   ( 12.98 ,  -6.98 )
14BA: BF 30 7F 62     VEC     scale=3(/64) x=27F  y=BF   i=6   (  9.98 ,   2.98 )
14BE: 3F 33 BF 61     VEC     scale=3(/64) x=1BF  y=33F  i=6   (  6.98 ,  12.98 )
14C2: 1F 42 FF 85     VEC     scale=4(/32) x=-1FF y=21F  i=8   (-15.96 ,  16.96 )
14C6: FF 45 1F 86     VEC     scale=4(/32) x=-21F y=-1FF i=8   (-16.96 , -15.96 )
14CA: 1F 46 FF 81     VEC     scale=4(/32) x=1FF  y=-21F i=8   ( 15.96 , -16.96 )
14CE: FF 41 1F 82     VEC     scale=4(/32) x=21F  y=1FF  i=8   ( 16.96 ,  15.96 )
14D2: 7F 32 BF 64     VEC     scale=3(/64) x=-BF  y=27F  i=6   ( -2.98 ,   9.98 )
14D6: 7F 40 DF 86     VEC     scale=4(/32) x=-2DF y=7F   i=8   (-22.96 ,   3.96 )
14DA: DF 46 7F 84     VEC     scale=4(/32) x=-7F  y=-2DF i=8   ( -3.96 , -22.96 )
14DE: 7F 44 DF 82     VEC     scale=4(/32) x=2DF  y=-7F  i=8   ( 22.96 ,  -3.96 )
14E2: DF 42 7F 80     VEC     scale=4(/32) x=7F   y=2DF  i=8   (  3.96 ,  22.96 )
14E6: 00 D0           RTS                         
;
14E8: 7F 33 BF 02     VEC     scale=3(/64) x=2BF  y=37F  i=0   ( 10.98 ,  13.98 )
14EC: BF 30 3F 67     VEC     scale=3(/64) x=-33F y=BF   i=6   (-12.98 ,   2.98 )
14F0: 7F 35 BF 66     VEC     scale=3(/64) x=-2BF y=-17F i=6   (-10.98 ,  -5.98 )
14F4: 3F 37 BF 64     VEC     scale=3(/64) x=-BF  y=-33F i=6   ( -2.98 , -12.98 )
14F8: BF 36 7F 61     VEC     scale=3(/64) x=17F  y=-2BF i=6   (  5.98 , -10.98 )
14FC: BF 34 3F 63     VEC     scale=3(/64) x=33F  y=-BF  i=6   ( 12.98 ,  -2.98 )
1500: 7F 31 BF 62     VEC     scale=3(/64) x=2BF  y=17F  i=6   ( 10.98 ,   5.98 )
1504: 3F 33 BF 60     VEC     scale=3(/64) x=BF   y=33F  i=6   (  2.98 ,  12.98 )
1508: BF 41 5F 86     VEC     scale=4(/32) x=-25F y=1BF  i=8   (-18.96 ,  13.96 )
150C: 5F 46 BF 85     VEC     scale=4(/32) x=-1BF y=-25F i=8   (-13.96 , -18.96 )
1510: BF 45 5F 82     VEC     scale=4(/32) x=25F  y=-1BF i=8   ( 18.96 , -13.96 )
1514: 5F 42 BF 81     VEC     scale=4(/32) x=1BF  y=25F  i=8   ( 13.96 ,  18.96 )
1518: BF 32 7F 65     VEC     scale=3(/64) x=-17F y=2BF  i=6   ( -5.98 ,  10.98 )
151C: 5F 44 FF 86     VEC     scale=4(/32) x=-2FF y=-5F  i=8   (-23.96 ,  -2.96 )
1520: FF 46 5F 80     VEC     scale=4(/32) x=5F   y=-2FF i=8   (  2.96 , -23.96 )
1524: 5F 40 FF 82     VEC     scale=4(/32) x=2FF  y=5F   i=8   ( 23.96 ,   2.96 )
1528: FF 42 5F 84     VEC     scale=4(/32) x=-5F  y=2FF  i=8   ( -2.96 ,  23.96 )
152C: 00 D0           RTS                         
```

# Enemy Chaser 

Triangle, chasing ememy in different positions

```html
<canvas width="350" height="100"
  data-command="baseScale=1,x=50,y=50,152E,x=125,y=50,1554,x=200,y=50,157C,x=275,y=50,15A4">
</canvas>
```

```code
EnemyChase:
152E: FF 12 FF D2     VEC     scale=1(/256)x=2FF  y=2FF  i=13  (  2.99 ,   2.99 )
1532: BF 34 3F D3     VEC     scale=3(/64) x=33F  y=-BF  i=13  ( 12.98 ,  -2.98 )
1536: 00 40 DF D7     VEC     scale=4(/32) x=-3DF y=0    i=13  (-30.96 ,   0.00 )
153A: 7F 34 3F D3     VEC     scale=3(/64) x=33F  y=-7F  i=13  ( 12.98 ,  -1.98 )
153E: D1 F1           SVEC    scale=0(/128)x=0    y=0    i=13  (  0.00 ,   0.00 )
1540: D8 F2           SVEC    scale=2(/32) x=0    y=200  i=13  (  0.00 ,  16.00 )
1542: 3F 37 7F D4     VEC     scale=3(/64) x=-7F  y=-33F i=13  ( -1.98 , -12.98 )
1546: 7F 26 7F D2     VEC     scale=2(/128)x=27F  y=-27F i=13  (  4.99 ,  -4.99 )
154A: 3F 37 BF D4     VEC     scale=3(/64) x=-BF  y=-33F i=13  ( -2.98 , -12.98 )
154E: BF 33 00 D0     VEC     scale=3(/64) x=0    y=3BF  i=13  (  0.00 ,  14.98 )
1552: A7 EB           JMP     $0BA7 ($174E)       ; 
;
1554: D1 F2           SVEC    scale=0(/128)x=0    y=200  i=13  (  0.00 ,   4.00 )
1556: 7F 30 3F D3     VEC     scale=3(/64) x=33F  y=7F   i=13  ( 12.98 ,   1.98 )
155A: 5F 45 9F D7     VEC     scale=4(/32) x=-39F y=-15F i=13  (-28.96 , -10.96 )
155E: 7F 30 3F D3     VEC     scale=3(/64) x=33F  y=7F   i=13  ( 12.98 ,   1.98 )
1562: FF 12 FF D0     VEC     scale=1(/256)x=FF   y=2FF  i=13  (  0.99 ,   2.99 )
1566: BF 33 3F D5     VEC     scale=3(/64) x=-13F y=3BF  i=13  ( -4.98 ,  14.98 )
156A: 3F 37 7F D0     VEC     scale=3(/64) x=7F   y=-33F i=13  (  1.98 , -12.98 )
156E: 7F 25 7F D3     VEC     scale=2(/128)x=37F  y=-17F i=13  (  6.99 ,  -2.99 )
1572: 3F 37 7F D0     VEC     scale=3(/64) x=7F   y=-33F i=13  (  1.98 , -12.98 )
1576: 7F 33 7F D5     VEC     scale=3(/64) x=-17F y=37F  i=13  ( -5.98 ,  13.98 )
157A: A7 EB           JMP     $0BA7 ($174E)       ; 
;
157C: D0 F2           SVEC    scale=0(/128)x=0    y=200  i=13  (  0.00 ,   4.00 )
157E: BF 31 BF D2     VEC     scale=3(/64) x=2BF  y=1BF  i=13  ( 10.98 ,   6.98 )
1582: 9F 46 9F D6     VEC     scale=4(/32) x=-29F y=-29F i=13  (-20.96 , -20.96 )
1586: BF 31 7F D2     VEC     scale=3(/64) x=27F  y=1BF  i=13  (  9.98 ,   6.98 )
158A: FF 12 00 D0     VEC     scale=1(/256)x=0    y=2FF  i=13  (  0.00 ,   2.99 )
158E: BF 32 7F D6     VEC     scale=3(/64) x=-27F y=2BF  i=13  ( -9.98 ,  10.98 )
1592: BF 36 BF D1     VEC     scale=3(/64) x=1BF  y=-2BF i=13  (  6.98 , -10.98 )
1596: 00 20 7F D3     VEC     scale=2(/128)x=37F  y=0    i=13  (  6.99 ,   0.00 )
159A: 7F 36 BF D1     VEC     scale=3(/64) x=1BF  y=-27F i=13  (  6.98 ,  -9.98 )
159E: 7F 32 BF D6     VEC     scale=3(/64) x=-2BF y=27F  i=13  (-10.98 ,   9.98 )
15A2: A7 EB           JMP     $0BA7 ($174E)       ; 
;
15A4: FF 13 FF D4     VEC     scale=1(/256)x=-FF  y=3FF  i=13  ( -0.99 ,   3.99 )
15A8: BF 32 BF D1     VEC     scale=3(/64) x=1BF  y=2BF  i=13  (  6.98 ,  10.98 )
15AC: 9F 47 5F D5     VEC     scale=4(/32) x=-15F y=-39F i=13  (-10.96 , -28.96 )
15B0: BF 32 BF D1     VEC     scale=3(/64) x=1BF  y=2BF  i=13  (  6.98 ,  10.98 )
15B4: FF 12 FF D5     VEC     scale=1(/256)x=-1FF y=2FF  i=13  ( -1.99 ,   2.99 )
15B8: 7F 31 7F D7     VEC     scale=3(/64) x=-37F y=17F  i=13  (-13.98 ,   5.98 )
15BC: BF 35 BF D2     VEC     scale=3(/64) x=2BF  y=-1BF i=13  ( 10.98 ,  -6.98 )
15C0: 7F 21 7F D3     VEC     scale=2(/128)x=37F  y=17F  i=13  (  6.99 ,   2.99 )
15C4: BF 35 BF D2     VEC     scale=3(/64) x=2BF  y=-1BF i=13  ( 10.98 ,  -6.98 )
15C8: 3F 31 BF D7     VEC     scale=3(/64) x=-3BF y=13F  i=13  (-14.98 ,   4.98 )
15CC: A7 EB           JMP     $0BA7 ($174E)       ; 
```

# Lasers 

```code
Lasers:
; Laser shots at different angles (just single vectors)
;
15CE: 00 30 BF F7     VEC     scale=3(/64) x=-3BF y=0    i=15  (-14.98 ,   0.00 )
15D2: 00 D0           RTS                         
15D4: 3F 34 7F F7     VEC     scale=3(/64) x=-37F y=-3F  i=15  (-13.98 ,  -0.98 )
15D8: 00 D0           RTS                         
15DA: 7F 34 7F F7     VEC     scale=3(/64) x=-37F y=-7F  i=15  (-13.98 ,  -1.98 )
15DE: 00 D0           RTS                         
15E0: FF 34 3F F7     VEC     scale=3(/64) x=-33F y=-FF  i=15  (-12.98 ,  -3.98 )
15E4: 00 D0           RTS                         
15E6: 3F 35 3F F7     VEC     scale=3(/64) x=-33F y=-13F i=15  (-12.98 ,  -4.98 )
15EA: 00 D0           RTS                         
15EC: BF 35 FF F6     VEC     scale=3(/64) x=-2FF y=-1BF i=15  (-11.98 ,  -6.98 )
15F0: 00 D0           RTS                         
15F2: FF 35 BF F6     VEC     scale=3(/64) x=-2BF y=-1FF i=15  (-10.98 ,  -7.98 )
15F6: 00 D0           RTS                         
15F8: FF 35 7F F6     VEC     scale=3(/64) x=-27F y=-1FF i=15  ( -9.98 ,  -7.98 )
15FC: 00 D0           RTS                         
15FE: 3F 36 3F F6     VEC     scale=3(/64) x=-23F y=-23F i=15  ( -8.98 ,  -8.98 )
1602: 00 D0           RTS                         
1604: 7F 36 FF F5     VEC     scale=3(/64) x=-1FF y=-27F i=15  ( -7.98 ,  -9.98 )
1608: 00 D0           RTS                         
160A: BF 36 BF F5     VEC     scale=3(/64) x=-1BF y=-2BF i=15  ( -6.98 , -10.98 )
160E: 00 D0           RTS                         
1610: FF 36 3F F5     VEC     scale=3(/64) x=-13F y=-2FF i=15  ( -4.98 , -11.98 )
1614: 00 D0           RTS                         
1616: 3F 37 FF F4     VEC     scale=3(/64) x=-FF  y=-33F i=15  ( -3.98 , -12.98 )
161A: 00 D0           RTS                         
161C: 7F 37 7F F4     VEC     scale=3(/64) x=-7F  y=-37F i=15  ( -1.98 , -13.98 )
1620: 00 D0           RTS                         
1622: 7F 37 3F F4     VEC     scale=3(/64) x=-3F  y=-37F i=15  ( -0.98 , -13.98 )
1626: 00 D0           RTS                         
1628: BF 37 00 F0     VEC     scale=3(/64) x=0    y=-3BF i=15  (  0.00 , -14.98 )
162C: 00 D0           RTS                         
162E: BF 37 3F F0     VEC     scale=3(/64) x=3F   y=-3BF i=15  (  0.98 , -14.98 )
1632: 00 D0           RTS                         
1634: 7F 37 7F F0     VEC     scale=3(/64) x=7F   y=-37F i=15  (  1.98 , -13.98 )
1638: 00 D0           RTS                         
163A: 7F 37 BF F0     VEC     scale=3(/64) x=BF   y=-37F i=15  (  2.98 , -13.98 )
163E: 00 D0           RTS                         
1640: 3F 37 3F F1     VEC     scale=3(/64) x=13F  y=-33F i=15  (  4.98 , -12.98 )
1644: 00 D0           RTS                         
1646: FF 36 7F F1     VEC     scale=3(/64) x=17F  y=-2FF i=15  (  5.98 , -11.98 )
164A: 00 D0           RTS                         
164C: BF 36 FF F1     VEC     scale=3(/64) x=1FF  y=-2BF i=15  (  7.98 , -10.98 )
1650: 00 D0           RTS                         
1652: 7F 36 3F F2     VEC     scale=3(/64) x=23F  y=-27F i=15  (  8.98 ,  -9.98 )
1656: 00 D0           RTS                         
1658: 3F 36 7F F2     VEC     scale=3(/64) x=27F  y=-23F i=15  (  9.98 ,  -8.98 )
165C: 00 D0           RTS                         
165E: FF 35 BF F2     VEC     scale=3(/64) x=2BF  y=-1FF i=15  ( 10.98 ,  -7.98 )
1662: 00 D0           RTS                         
1664: FF 35 FF F2     VEC     scale=3(/64) x=2FF  y=-1FF i=15  ( 11.98 ,  -7.98 )
1668: 00 D0           RTS                         
166A: BF 35 3F F3     VEC     scale=3(/64) x=33F  y=-1BF i=15  ( 12.98 ,  -6.98 )
166E: 00 D0           RTS                         
1670: 3F 35 7F F3     VEC     scale=3(/64) x=37F  y=-13F i=15  ( 13.98 ,  -4.98 )
1674: 00 D0           RTS                         
1676: FF 34 7F F3     VEC     scale=3(/64) x=37F  y=-FF  i=15  ( 13.98 ,  -3.98 )
167A: 00 D0           RTS                         
167C: 7F 34 BF F3     VEC     scale=3(/64) x=3BF  y=-7F  i=15  ( 14.98 ,  -1.98 )
1680: 00 D0           RTS                         
1682: 3F 34 BF F3     VEC     scale=3(/64) x=3BF  y=-3F  i=15  ( 14.98 ,  -0.98 )
1686: 00 D0           RTS                         
1688: 00 30 FF F3     VEC     scale=3(/64) x=3FF  y=0    i=15  ( 15.98 ,   0.00 )
168C: 00 D0           RTS                         
168E: 00 30 FF F3     VEC     scale=3(/64) x=3FF  y=0    i=15  ( 15.98 ,   0.00 )
1692: 00 D0           RTS                         
1694: 7F 30 BF F3     VEC     scale=3(/64) x=3BF  y=7F   i=15  ( 14.98 ,   1.98 )
1698: 00 D0           RTS                         
169A: BF 30 BF F3     VEC     scale=3(/64) x=3BF  y=BF   i=15  ( 14.98 ,   2.98 )
169E: 00 D0           RTS                         
16A0: 3F 31 7F F3     VEC     scale=3(/64) x=37F  y=13F  i=15  ( 13.98 ,   4.98 )
16A4: 00 D0           RTS                         
16A6: 7F 31 7F F3     VEC     scale=3(/64) x=37F  y=17F  i=15  ( 13.98 ,   5.98 )
16AA: 00 D0           RTS                         
16AC: FF 31 3F F3     VEC     scale=3(/64) x=33F  y=1FF  i=15  ( 12.98 ,   7.98 )
16B0: 00 D0           RTS                         
16B2: 3F 32 FF F2     VEC     scale=3(/64) x=2FF  y=23F  i=15  ( 11.98 ,   8.98 )
16B6: 00 D0           RTS                         
16B8: 3F 32 BF F2     VEC     scale=3(/64) x=2BF  y=23F  i=15  ( 10.98 ,   8.98 )
16BC: 00 D0           RTS                         
16BE: 7F 32 7F F2     VEC     scale=3(/64) x=27F  y=27F  i=15  (  9.98 ,   9.98 )
16C2: 00 D0           RTS                         
16C4: BF 32 3F F2     VEC     scale=3(/64) x=23F  y=2BF  i=15  (  8.98 ,  10.98 )
16C8: 00 D0           RTS                         
16CA: FF 32 FF F1     VEC     scale=3(/64) x=1FF  y=2FF  i=15  (  7.98 ,  11.98 )
16CE: 00 D0           RTS                         
16D0: 3F 33 7F F1     VEC     scale=3(/64) x=17F  y=33F  i=15  (  5.98 ,  12.98 )
16D4: 00 D0           RTS                         
16D6: 7F 33 3F F1     VEC     scale=3(/64) x=13F  y=37F  i=15  (  4.98 ,  13.98 )
16DA: 00 D0           RTS                         
16DC: BF 33 BF F0     VEC     scale=3(/64) x=BF   y=3BF  i=15  (  2.98 ,  14.98 )
16E0: 00 D0           RTS                         
16E2: BF 33 7F F0     VEC     scale=3(/64) x=7F   y=3BF  i=15  (  1.98 ,  14.98 )
16E6: 00 D0           RTS                         
16E8: FF 33 00 F0     VEC     scale=3(/64) x=0    y=3FF  i=15  (  0.00 ,  15.98 )
16EC: 00 D0           RTS                         
16EE: FF 33 00 F0     VEC     scale=3(/64) x=0    y=3FF  i=15  (  0.00 ,  15.98 )
16F2: 00 D0           RTS                         
16F4: BF 33 3F F4     VEC     scale=3(/64) x=-3F  y=3BF  i=15  ( -0.98 ,  14.98 )
16F8: 00 D0           RTS                         
16FA: BF 33 7F F4     VEC     scale=3(/64) x=-7F  y=3BF  i=15  ( -1.98 ,  14.98 )
16FE: 00 D0           RTS                         
1700: 7F 33 FF F4     VEC     scale=3(/64) x=-FF  y=37F  i=15  ( -3.98 ,  13.98 )
1704: 00 D0           RTS                         
1706: 3F 33 3F F5     VEC     scale=3(/64) x=-13F y=33F  i=15  ( -4.98 ,  12.98 )
170A: 00 D0           RTS                         
170C: FF 32 BF F5     VEC     scale=3(/64) x=-1BF y=2FF  i=15  ( -6.98 ,  11.98 )
1710: 00 D0           RTS                         
1712: BF 32 FF F5     VEC     scale=3(/64) x=-1FF y=2BF  i=15  ( -7.98 ,  10.98 )
1716: 00 D0           RTS                         
1718: 7F 32 3F F6     VEC     scale=3(/64) x=-23F y=27F  i=15  ( -8.98 ,   9.98 )
171C: 00 D0           RTS                         
171E: 3F 32 7F F6     VEC     scale=3(/64) x=-27F y=23F  i=15  ( -9.98 ,   8.98 )
1722: 00 D0           RTS                         
1724: 3F 32 BF F6     VEC     scale=3(/64) x=-2BF y=23F  i=15  (-10.98 ,   8.98 )
1728: 00 D0           RTS                         
172A: FF 31 FF F6     VEC     scale=3(/64) x=-2FF y=1FF  i=15  (-11.98 ,   7.98 )
172E: 00 D0           RTS                         
1730: 7F 31 3F F7     VEC     scale=3(/64) x=-33F y=17F  i=15  (-12.98 ,   5.98 )
1734: 00 D0           RTS                         
1736: 3F 31 3F F7     VEC     scale=3(/64) x=-33F y=13F  i=15  (-12.98 ,   4.98 )
173A: 00 D0           RTS                         
173C: BF 30 7F F7     VEC     scale=3(/64) x=-37F y=BF   i=15  (-13.98 ,   2.98 )
1740: 00 D0           RTS                         
1742: 7F 30 7F F7     VEC     scale=3(/64) x=-37F y=7F   i=15  (-13.98 ,   1.98 )
1746: 00 D0           RTS                         
1748: 00 30 BF F7     VEC     scale=3(/64) x=-3BF y=0    i=15  (-14.98 ,   0.00 )
174C: 00 D0           RTS                         
```

# Triangles 

Single and double

```html
<canvas width="200" height="100"
  data-command="baseScale=1,x=50,y=50,174E,x=125,y=50,175E">
</canvas>
```

```code
Triangles:
; Triangle (up)
174E: 7F 35 FF 02     VEC     scale=3(/64) x=2FF  y=-17F i=0   ( 11.98 ,  -5.98 )
1752: FF 33 FF F6     VEC     scale=3(/64) x=-2FF y=3FF  i=15  (-11.98 ,  15.98 )
1756: FF 37 FF F6     VEC     scale=3(/64) x=-2FF y=-3FF i=15  (-11.98 , -15.98 )
175A: FB F0           SVEC    scale=2(/32) x=200  y=0    i=15  ( 16.00 ,   0.00 )
175C: 00 D0           RTS                         

; Triangles (up and down)
175E: 03 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1760: FF 33 FF F6     VEC     scale=3(/64) x=-2FF y=3FF  i=15  (-11.98 ,  15.98 )
1764: FF 37 FF F6     VEC     scale=3(/64) x=-2FF y=-3FF i=15  (-11.98 , -15.98 )
1768: FF 37 FF F2     VEC     scale=3(/64) x=2FF  y=-3FF i=15  ( 11.98 , -15.98 )
176C: FF 33 FF F2     VEC     scale=3(/64) x=2FF  y=3FF  i=15  ( 11.98 ,  15.98 )
1770: FF F0           SVEC    scale=2(/32) x=-200 y=0    i=15  (-16.00 ,   0.00 )
1772: 00 D0           RTS                         
```

# Explosion 

Multi-line explosion ... three pictures for animation

```html
<canvas width="400" height="200"
  data-command="baseScale=1,x=50,y=100,1774,x=150,y=100,17B0,x=300,y=100,1824">
</canvas>
```

```code
Explosion:
1774: BF 32 00 F0     VEC     scale=3(/64) x=0    y=2BF  i=15  (  0.00 ,  10.98 )
1778: BF 46 00 F0     VEC     scale=4(/32) x=0    y=-2BF i=15  (  0.00 , -21.96 )
177C: FF 21 7F 06     VEC     scale=2(/128)x=-27F y=1FF  i=0   ( -4.99 ,   3.99 )
1780: BF 33 3F F2     VEC     scale=3(/64) x=23F  y=3BF  i=15  (  8.98 ,  14.98 )
1784: 00 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
1786: F6 FE           SVEC    scale=1(/64) x=-200 y=-200 i=15  ( -8.00 ,  -8.00 )
1788: FF 20 7F 06     VEC     scale=2(/128)x=-27F y=FF   i=0   ( -4.99 ,   1.99 )
178C: DF 40 5F F2     VEC     scale=4(/32) x=25F  y=DF   i=15  ( 18.96 ,   6.96 )
1790: 7F 26 FF 00     VEC     scale=2(/128)x=FF   y=-27F i=0   (  1.99 ,  -4.99 )
1794: 00 40 BF F6     VEC     scale=4(/32) x=-2BF y=0    i=15  (-21.96 ,   0.00 )
1798: FF 13 FF 04     VEC     scale=1(/256)x=-FF  y=3FF  i=0   ( -0.99 ,   3.99 )
179C: FF 44 9F F2     VEC     scale=4(/32) x=29F  y=-FF  i=15  ( 20.96 ,  -7.96 )
17A0: 00 F7           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
17A2: 7F 33 7F F7     VEC     scale=3(/64) x=-37F y=37F  i=15  (-13.98 ,  13.98 )
17A6: 7F 22 00 00     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
17AA: FF 37 BF F1     VEC     scale=3(/64) x=1BF  y=-3FF i=15  (  6.98 , -15.98 )
17AE: 00 D0           RTS                         
;
17B0: BF 32 00 00     VEC     scale=3(/64) x=0    y=2BF  i=0   (  0.00 ,  10.98 )
17B4: 7F 32 00 50     VEC     scale=3(/64) x=0    y=27F  i=5   (  0.00 ,   9.98 )
17B8: 7F 26 FF 03     VEC     scale=2(/128)x=3FF  y=-27F i=0   (  7.99 ,  -4.99 )
17BC: 55 FE           SVEC    scale=1(/64) x=0    y=-200 i=5   (  0.00 ,  -8.00 )
17BE: 00 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
17C0: 53 FB           SVEC    scale=1(/64) x=200  y=200  i=5   (  8.00 ,   8.00 )
17C2: BF 36 7F 05     VEC     scale=3(/64) x=-17F y=-2BF i=0   ( -5.98 , -10.98 )
17C6: 7F 31 FF 52     VEC     scale=3(/64) x=2FF  y=17F  i=5   ( 11.98 ,   5.98 )
17CA: BF 36 7F 04     VEC     scale=3(/64) x=-7F  y=-2BF i=0   ( -1.98 , -10.98 )
17CE: 56 F8           SVEC    scale=1(/64) x=-200 y=0    i=5   ( -8.00 ,   0.00 )
17D0: 05 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
17D2: 7F 25 FF 53     VEC     scale=2(/128)x=3FF  y=-17F i=5   (  7.99 ,  -2.99 )
17D6: 3F 37 7F 00     VEC     scale=3(/64) x=7F   y=-33F i=0   (  1.98 , -12.98 )
17DA: 7F 32 7F 56     VEC     scale=3(/64) x=-27F y=27F  i=5   ( -9.98 ,   9.98 )
17DE: 7F 21 7F 07     VEC     scale=2(/128)x=-37F y=17F  i=0   ( -6.99 ,   2.99 )
17E2: 3F 36 FF 50     VEC     scale=3(/64) x=FF   y=-23F i=5   (  3.98 ,  -8.98 )
17E6: FF 25 7F 07     VEC     scale=2(/128)x=-37F y=-1FF i=0   ( -6.99 ,  -3.99 )
17EA: 50 FA           SVEC    scale=1(/64) x=0    y=200  i=5   (  0.00 ,   8.00 )
17EC: 7F 22 7F 06     VEC     scale=2(/128)x=-27F y=27F  i=0   ( -4.99 ,   4.99 )
17F0: 7F 27 7F 56     VEC     scale=2(/128)x=-27F y=-37F i=5   ( -4.99 ,  -6.99 )
17F4: 7F 21 FF 07     VEC     scale=2(/128)x=-3FF y=17F  i=0   ( -7.99 ,   2.99 )
17F8: FF 31 3F 53     VEC     scale=3(/64) x=33F  y=1FF  i=5   ( 12.98 ,   7.98 )
17FC: FF 10 FF 07     VEC     scale=1(/256)x=-3FF y=FF   i=0   ( -3.99 ,   0.99 )
1800: FF 24 7F 57     VEC     scale=2(/128)x=-37F y=-FF  i=5   ( -6.99 ,  -1.99 )
1804: FF 21 7F 07     VEC     scale=2(/128)x=-37F y=1FF  i=0   ( -6.99 ,   3.99 )
1808: 00 30 3F 53     VEC     scale=3(/64) x=33F  y=0    i=5   ( 12.98 ,   0.00 )
180C: FF 13 FF 04     VEC     scale=1(/256)x=-FF  y=3FF  i=0   ( -0.99 ,   3.99 )
1810: 7F 21 FF 57     VEC     scale=2(/128)x=-3FF y=17F  i=5   ( -7.99 ,   2.99 )
1814: 01 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
1816: BF 36 BF 52     VEC     scale=3(/64) x=2BF  y=-2BF i=5   ( 10.98 , -10.98 )
181A: 7F 22 00 00     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
181E: 7F 23 7F 55     VEC     scale=2(/128)x=-17F y=37F  i=5   ( -2.99 ,   6.99 )
1822: 00 D0           RTS                         
;
1824: 9F 42 00 00     VEC     scale=4(/32) x=0    y=29F  i=0   (  0.00 ,  20.96 )
1828: BF 32 00 F0     VEC     scale=3(/64) x=0    y=2BF  i=15  (  0.00 ,  10.98 )
182C: 03 FE           SVEC    scale=1(/64) x=200  y=-200 i=0   (  8.00 ,  -8.00 )
182E: F5 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
1830: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1832: FF 32 7F F2     VEC     scale=3(/64) x=27F  y=2FF  i=15  (  9.98 ,  11.98 )
1836: FF 36 7F 01     VEC     scale=3(/64) x=17F  y=-2FF i=0   (  5.98 , -11.98 )
183A: 3F 35 7F F6     VEC     scale=3(/64) x=-27F y=-13F i=15  ( -9.98 ,  -4.98 )
183E: BF 36 7F 04     VEC     scale=3(/64) x=-7F  y=-2BF i=0   ( -1.98 , -10.98 )
1842: 00 20 7F F3     VEC     scale=2(/128)x=37F  y=0    i=15  (  6.99 ,   0.00 )
1846: 01 FF           SVEC    scale=1(/64) x=0    y=-200 i=0   (  0.00 ,  -8.00 )
1848: 3F 31 3F F7     VEC     scale=3(/64) x=-33F y=13F  i=15  (-12.98 ,   4.98 )
184C: FF 36 3F 00     VEC     scale=3(/64) x=3F   y=-2FF i=0   (  0.98 , -11.98 )
1850: 7F 26 7F F2     VEC     scale=2(/128)x=27F  y=-27F i=15  (  4.99 ,  -4.99 )
1854: 7F 35 BF 06     VEC     scale=3(/64) x=-2BF y=-17F i=0   (-10.98 ,  -5.98 )
1858: 7F 33 7F F5     VEC     scale=3(/64) x=-17F y=37F  i=15  ( -5.98 ,  13.98 )
185C: FF 25 7F 07     VEC     scale=2(/128)x=-37F y=-1FF i=0   ( -6.99 ,  -3.99 )
1860: F0 FF           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
1862: 3F 42 3F 05     VEC     scale=4(/32) x=-13F y=23F  i=0   ( -9.96 ,  17.96 )
1866: 7F 27 7F F6     VEC     scale=2(/128)x=-27F y=-37F i=15  ( -4.99 ,  -6.99 )
186A: FF 30 3F 07     VEC     scale=3(/64) x=-33F y=FF   i=0   (-12.98 ,   3.98 )
186E: 7F 31 BF F2     VEC     scale=3(/64) x=2BF  y=17F  i=15  ( 10.98 ,   5.98 )
1872: 7F 23 7F 00     VEC     scale=2(/128)x=7F   y=37F  i=0   (  0.99 ,   6.99 )
1876: FF 34 FF F7     VEC     scale=3(/64) x=-3FF y=-FF  i=15  (-15.98 ,  -3.98 )
187A: 01 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
187C: F3 F0           SVEC    scale=0(/128)x=200  y=0    i=15  (  4.00 ,   0.00 )
187E: 7F 23 7F 01     VEC     scale=2(/128)x=17F  y=37F  i=0   (  2.99 ,   6.99 )
1882: F7 F1           SVEC    scale=0(/128)x=-200 y=0    i=15  ( -4.00 ,   0.00 )
1884: 7F 42 7F 04     VEC     scale=4(/32) x=-7F  y=27F  i=0   ( -3.96 ,  19.96 )
1888: 7F 37 7F F3     VEC     scale=3(/64) x=37F  y=-37F i=15  ( 13.98 , -13.98 )
188C: 7F 20 FF 03     VEC     scale=2(/128)x=3FF  y=7F   i=0   (  7.99 ,   0.99 )
1890: 7F 32 3F F5     VEC     scale=3(/64) x=-13F y=27F  i=15  ( -4.98 ,   9.98 )
1894: 3F 47 7F 01     VEC     scale=4(/32) x=17F  y=-33F i=0   ( 11.96 , -25.96 )
1898: 00 D0           RTS                         
```

# Letters 

Letters of the alphabet

```html
<canvas width="850" height="40"
  data-command="baseScale=1,x=20,y=30,189A,*,*,*,*,18EE,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*">
</canvas>
```

```code
Letters:
; A
;
189A: 90 FA           SVEC    scale=1(/64) x=0    y=200  i=9   (  0.00 ,   8.00 )
189C: 91 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
189E: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
18A0: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
18A2: 90 FE           SVEC    scale=1(/64) x=0    y=-200 i=9   (  0.00 ,  -8.00 )
18A4: FF 22 FF 07     VEC     scale=2(/128)x=-3FF y=2FF  i=0   ( -7.99 ,   5.99 )
18A8: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
18AA: FF 26 FF 03     VEC     scale=2(/128)x=3FF  y=-2FF i=0   (  7.99 ,  -5.99 )
18AE: 00 D0           RTS                         

; B
;
18B0: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
18B4: 93 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
18B6: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
18B8: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
18BA: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
18BC: 03 F0           SVEC    scale=0(/128)x=200  y=0    i=0   (  4.00 ,   0.00 )
18BE: 91 F6           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
18C0: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
18C2: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
18C4: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
18C6: 00 D0           RTS                         

; C
;
18C8: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
18CC: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
18CE: 7F 36 00 00     VEC     scale=3(/64) x=0    y=-27F i=0   (  0.00 ,  -9.98 )
18D2: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
18D4: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
18D6: 00 D0           RTS                         

; D
;
18D8: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
18DC: 93 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
18DE: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
18E0: 90 F7           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
18E2: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
18E4: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
18E6: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
18E8: 00 D0           RTS                         

; E
;
18EA: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
18EC: 06 F8           SVEC    scale=1(/64) x=-200 y=0    i=0   ( -8.00 ,   0.00 )
;
; F
18EE: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
18F2: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
18F4: 05 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
18F6: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
18F8: 7F 35 FF 03     VEC     scale=3(/64) x=3FF  y=-17F i=0   ( 15.98 ,  -5.98 )
18FC: 00 D0           RTS                         

; G
;
18FE: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
1902: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1904: 05 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
1906: 91 F0           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1908: 90 F7           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
190A: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
190C: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
190E: 00 D0           RTS                         

; H
;
1910: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
1914: 00 F6           SVEC    scale=0(/128)x=0    y=-200 i=0   (  0.00 ,  -4.00 )
1916: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1918: 00 F2           SVEC    scale=0(/128)x=0    y=200  i=0   (  0.00 ,   4.00 )
191A: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
191E: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1920: 00 D0           RTS                         

; I
;
1922: 01 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
1924: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
1926: 05 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
1928: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
192C: 05 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
192E: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
1930: 7F 36 7F 02     VEC     scale=3(/64) x=27F  y=-27F i=0   (  9.98 ,  -9.98 )
1934: 00 D0           RTS                         

; J
;
1936: 00 F1           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
1938: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
193A: 93 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
193C: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
1940: 7F 36 FF 01     VEC     scale=3(/64) x=1FF  y=-27F i=0   (  7.98 ,  -9.98 )
1944: 00 D0           RTS                         

; K
;
1946: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
194A: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
194C: 96 FD           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
194E: FF 26 FF 93     VEC     scale=2(/128)x=3FF  y=-2FF i=9   (  7.99 ,  -5.99 )
1952: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1954: 00 D0           RTS                         

; L
;
1956: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
195A: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
195E: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1960: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1962: 00 D0           RTS                         

; M
;
1964: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
1968: 92 F6           SVEC    scale=0(/128)x=200  y=-200 i=9   (  4.00 ,  -4.00 )
196A: 92 F2           SVEC    scale=0(/128)x=200  y=200  i=9   (  4.00 ,   4.00 )
196C: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
1970: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1972: 00 D0           RTS                         

; N
;
1974: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
1978: 92 FE           SVEC    scale=1(/64) x=200  y=-200 i=9   (  8.00 ,  -8.00 )
197A: 00 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
197C: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
1980: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1982: 00 D0           RTS                         

; O
;
1984: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
1988: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
198A: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
198E: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
1990: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
1992: 00 D0           RTS                         

; P
;
1994: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
1998: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
199A: 90 F6           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
199C: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
199E: 7F 35 FF 03     VEC     scale=3(/64) x=3FF  y=-17F i=0   ( 15.98 ,  -5.98 )
19A2: 00 D0           RTS                         

; Q
;
19A4: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
19A8: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
19AA: 90 FE           SVEC    scale=1(/64) x=0    y=-200 i=9   (  0.00 ,  -8.00 )
19AC: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
19AE: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
19B0: 03 F1           SVEC    scale=0(/128)x=200  y=0    i=0   (  4.00 ,   0.00 )
19B2: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
19B4: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
19B6: 00 D0           RTS                         

; R
;
19B8: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
19BC: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
19BE: 7F 26 00 90     VEC     scale=2(/128)x=0    y=-27F i=9   (  0.00 ,  -4.99 )
19C2: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
19C4: 7F 26 FF 93     VEC     scale=2(/128)x=3FF  y=-27F i=9   (  7.99 ,  -4.99 )
19C8: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
19CA: 00 D0           RTS                         

; S
;
19CC: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
19CE: 7F 22 00 90     VEC     scale=2(/128)x=0    y=27F  i=9   (  0.00 ,   4.99 )
19D2: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
19D4: 7F 22 00 90     VEC     scale=2(/128)x=0    y=27F  i=9   (  0.00 ,   4.99 )
19D8: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
19DA: 7F 36 FF 01     VEC     scale=3(/64) x=1FF  y=-27F i=0   (  7.98 ,  -9.98 )
19DE: 00 D0           RTS                         

; T
;
19E0: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
19E4: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
19E6: 06 F0           SVEC    scale=0(/128)x=-200 y=0    i=0   ( -4.00 ,   0.00 )
19E8: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
19EC: 03 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
19EE: 00 D0           RTS                         

; U
;
19F0: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
19F4: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
19F8: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
19FA: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
19FE: 7F 36 FF 01     VEC     scale=3(/64) x=1FF  y=-27F i=0   (  7.98 ,  -9.98 )
1A02: 00 D0           RTS                         

; V
;
1A04: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
1A08: 90 F7           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
1A0A: 92 F6           SVEC    scale=0(/128)x=200  y=-200 i=9   (  4.00 ,  -4.00 )
1A0C: 92 F2           SVEC    scale=0(/128)x=200  y=200  i=9   (  4.00 ,   4.00 )
1A0E: 90 F3           SVEC    scale=0(/128)x=0    y=200  i=9   (  0.00 ,   4.00 )
1A10: 7F 36 FF 01     VEC     scale=3(/64) x=1FF  y=-27F i=0   (  7.98 ,  -9.98 )
1A14: 00 D0           RTS                         

; W
;
1A16: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
1A1A: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
1A1E: 92 F2           SVEC    scale=0(/128)x=200  y=200  i=9   (  4.00 ,   4.00 )
1A20: 92 F6           SVEC    scale=0(/128)x=200  y=-200 i=9   (  4.00 ,  -4.00 )
1A22: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
1A26: 7F 36 FF 01     VEC     scale=3(/64) x=1FF  y=-27F i=0   (  7.98 ,  -9.98 )
1A2A: 00 D0           RTS                         

; X
;
1A2C: 7F 32 FF 91     VEC     scale=3(/64) x=1FF  y=27F  i=9   (  7.98 ,   9.98 )
1A30: 06 F8           SVEC    scale=1(/64) x=-200 y=0    i=0   ( -8.00 ,   0.00 )
1A32: 7F 36 FF 91     VEC     scale=3(/64) x=1FF  y=-27F i=9   (  7.98 ,  -9.98 )
1A36: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1A38: 00 D0           RTS                         

; Y
;
1A3A: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
1A3E: 7F 26 FF 91     VEC     scale=2(/128)x=1FF  y=-27F i=9   (  3.99 ,  -4.99 )
1A42: 7F 22 FF 91     VEC     scale=2(/128)x=1FF  y=27F  i=9   (  3.99 ,   4.99 )
1A46: 06 F6           SVEC    scale=0(/128)x=-200 y=-200 i=0   ( -4.00 ,  -4.00 )
1A48: 90 F7           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
1A4A: 03 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1A4C: 00 D0           RTS                         

; Z
;
1A4E: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
1A52: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1A54: 7F 36 FF 95     VEC     scale=3(/64) x=-1FF y=-27F i=9   ( -7.98 ,  -9.98 )
1A58: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1A5A: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1A5C: 00 D0           RTS                         
```

# Numbers 

Numbers and the "space" character

```html
<canvas width="350" height="40"
  data-command="baseScale=1,x=20,y=30,1A5E,*,*,*,*,*,*,*,*,*">
</canvas>
```

```code
Numbers:
; 0
;
1A5E: 01 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
1A60: 95 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1A62: 90 F3           SVEC    scale=0(/128)x=0    y=200  i=9   (  0.00 ,   4.00 )
1A64: 91 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1A66: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
1A68: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1A6A: 90 F7           SVEC    scale=0(/128)x=0    y=-200 i=9   (  0.00 ,  -4.00 )
1A6C: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1A6E: 96 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
1A70: 00 30 7F 03     VEC     scale=3(/64) x=37F  y=0    i=0   ( 13.98 ,   0.00 )
1A74: 00 D0           RTS                         

; 1
;
1A76: 7F 23 FF 00     VEC     scale=2(/128)x=FF   y=37F  i=0   (  1.99 ,   6.99 )
1A7A: FF 12 FF 91     VEC     scale=1(/256)x=1FF  y=2FF  i=9   (  1.99 ,   2.99 )
1A7E: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
1A82: 05 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
1A84: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
1A86: 00 30 7F 02     VEC     scale=3(/64) x=27F  y=0    i=0   (  9.98 ,   0.00 )
1A8A: 00 D0           RTS                         

; 2
;
1A8C: 00 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
1A8E: 91 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1A90: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
1A92: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1A94: FF 16 00 90     VEC     scale=1(/256)x=0    y=-2FF i=9   (  0.00 ,  -2.99 )
1A98: 96 FD           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
1A9A: FF 05 00 90     VEC     scale=0(/512)x=0    y=-1FF i=9   (  0.00 ,  -0.99 )
1A9E: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1AA0: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1AA2: 00 D0           RTS                         

; 3
;
1AA4: 00 FA           SVEC    scale=1(/64) x=0    y=200  i=0   (  0.00 ,   8.00 )
1AA6: 91 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1AA8: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
1AAA: 91 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1AAC: 90 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1AAE: FF 05 FF 97     VEC     scale=0(/512)x=-3FF y=-1FF i=9   ( -1.99 ,  -0.99 )
1AB2: 95 F0           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1AB4: 01 F0           SVEC    scale=0(/128)x=0    y=0    i=0   (  0.00 ,   0.00 )
1AB6: FF 05 FF 93     VEC     scale=0(/512)x=3FF  y=-1FF i=9   (  1.99 ,  -0.99 )
1ABA: 90 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1ABC: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1ABE: 96 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
1AC0: 95 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1AC2: 7F 34 FF 03     VEC     scale=3(/64) x=3FF  y=-7F  i=0   ( 15.98 ,  -1.98 )
1AC6: 00 D0           RTS                         

; 4
;
1AC8: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
1ACC: 7F 26 00 90     VEC     scale=2(/128)x=0    y=-27F i=9   (  0.00 ,  -4.99 )
1AD0: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1AD2: 7F 22 00 00     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
1AD6: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
1ADA: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1ADC: 00 D0           RTS                         

; 5
;
1ADE: 7F 32 FF 01     VEC     scale=3(/64) x=1FF  y=27F  i=0   (  7.98 ,   9.98 )
1AE2: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
1AE4: 7F 26 00 90     VEC     scale=2(/128)x=0    y=-27F i=9   (  0.00 ,  -4.99 )
1AE8: FF 01 FF 93     VEC     scale=0(/512)x=3FF  y=1FF  i=9   (  1.99 ,   0.99 )
1AEC: 92 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )
1AEE: FF 05 FF 93     VEC     scale=0(/512)x=3FF  y=-1FF i=9   (  1.99 ,  -0.99 )
1AF2: FF 16 00 90     VEC     scale=1(/256)x=0    y=-2FF i=9   (  0.00 ,  -2.99 )
1AF6: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1AF8: 96 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
1AFA: 95 F1           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1AFC: 7F 34 FF 03     VEC     scale=3(/64) x=3FF  y=-7F  i=0   ( 15.98 ,  -1.98 )
1B00: 00 D0           RTS                         

; 6
;
1B02: 7F 32 FF 01     VEC     scale=3(/64) x=1FF  y=27F  i=0   (  7.98 ,   9.98 )
1B06: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
1B08: 95 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1B0A: 90 FE           SVEC    scale=1(/64) x=0    y=-200 i=9   (  0.00 ,  -8.00 )
1B0C: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1B0E: 7F 22 00 90     VEC     scale=2(/128)x=0    y=27F  i=9   (  0.00 ,   4.99 )
1B12: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
1B14: 3F 35 FF 03     VEC     scale=3(/64) x=3FF  y=-13F i=0   ( 15.98 ,  -4.98 )
1B18: 00 D0           RTS                         

; 7
;
1B1A: 7F 32 00 00     VEC     scale=3(/64) x=0    y=27F  i=0   (  0.00 ,   9.98 )
1B1E: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1B20: 90 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1B22: 96 FE           SVEC    scale=1(/64) x=-200 y=-200 i=9   ( -8.00 ,  -8.00 )
;
; space
1B24: 0A F0           SVEC    scale=2(/32) x=200  y=0    i=0   ( 16.00 ,   0.00 )
1B26: 00 D0           RTS                         

; 8
;
1B28: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
1B2C: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1B2E: 7F 36 00 90     VEC     scale=3(/64) x=0    y=-27F i=9   (  0.00 ,  -9.98 )
1B32: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
1B34: 7F 22 00 00     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
1B38: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1B3A: 7F 26 FF 03     VEC     scale=2(/128)x=3FF  y=-27F i=0   (  7.99 ,  -4.99 )
1B3E: 00 D0           RTS                         

; 9
;
1B40: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1B42: 7F 32 00 90     VEC     scale=3(/64) x=0    y=27F  i=9   (  0.00 ,   9.98 )
1B46: 96 F8           SVEC    scale=1(/64) x=-200 y=0    i=9   ( -8.00 ,   0.00 )
1B48: 7F 26 00 90     VEC     scale=2(/128)x=0    y=-27F i=9   (  0.00 ,  -4.99 )
1B4C: 92 F8           SVEC    scale=1(/64) x=200  y=0    i=9   (  8.00 ,   0.00 )
1B4E: 7F 26 FF 03     VEC     scale=2(/128)x=3FF  y=-27F i=0   (  7.99 ,  -4.99 )
1B52: 00 D0           RTS                         
```

# Special Chars 

Punctuation and special characters

```html
<canvas width="350" height="100"
  data-command="baseScale=1,x=20,y=30,1B54,1B66,1B84,1B94,1B9A,1BA6">
</canvas>
```

```code
Special:
; .
;
1B54: FF 01 FF 91     VEC     scale=0(/512)x=1FF  y=1FF  i=9   (  0.99 ,   0.99 )
1B58: 00 00 FF 05     VEC     scale=0(/512)x=-1FF y=0    i=0   ( -0.99 ,   0.00 )
1B5C: FF 05 FF 91     VEC     scale=0(/512)x=1FF  y=-1FF i=9   (  0.99 ,  -0.99 )
1B60: 00 30 BF 03     VEC     scale=3(/64) x=3BF  y=0    i=0   ( 14.98 ,   0.00 )
1B64: 00 D0           RTS                         

; ,
;
1B66: 00 00 FF 01     VEC     scale=0(/512)x=1FF  y=0    i=0   (  0.99 ,   0.00 )
1B6A: 00 00 FF 95     VEC     scale=0(/512)x=-1FF y=0    i=9   ( -0.99 ,   0.00 )
1B6E: FF 01 00 90     VEC     scale=0(/512)x=0    y=1FF  i=9   (  0.00 ,   0.99 )
1B72: 00 00 FF 91     VEC     scale=0(/512)x=1FF  y=0    i=9   (  0.99 ,   0.00 )
1B76: 90 F5           SVEC    scale=0(/128)x=0    y=0    i=9   (  0.00 ,   0.00 )
1B78: 3F 30 BF 03     VEC     scale=3(/64) x=3BF  y=3F   i=0   ( 14.98 ,   0.98 )
1B7C: 00 D0           RTS                         

; CR/LF
;
1B7E: 7F 46 FF 05     VEC     scale=4(/32) x=-1FF y=-27F i=0   (-15.96 , -19.96 )
1B82: 00 D0           RTS                         

; Triangle (left)
;
1B84: 02 F8           SVEC    scale=1(/64) x=200  y=0    i=0   (  8.00 ,   0.00 )
1B86: 7F 22 FF C7     VEC     scale=2(/128)x=-3FF y=27F  i=12  ( -7.99 ,   4.99 )
1B8A: 7F 22 FF C3     VEC     scale=2(/128)x=3FF  y=27F  i=12  (  7.99 ,   4.99 )
1B8E: 7F 36 00 C0     VEC     scale=3(/64) x=0    y=-27F i=12  (  0.00 ,  -9.98 )
1B92: 00 D0           RTS                         

; =
;
1B94: 7F 23 7F 00     VEC     scale=2(/128)x=7F   y=37F  i=0   (  0.99 ,   6.99 )
1B98: 93 F0           SVEC    scale=0(/128)x=200  y=0    i=9   (  4.00 ,   0.00 )

; _
1B9A: FF 16 00 00     VEC     scale=1(/256)x=0    y=-2FF i=0   (  0.00 ,  -2.99 )
1B9E: 97 F0           SVEC    scale=0(/128)x=-200 y=0    i=9   ( -4.00 ,   0.00 )
1BA0: FF 34 BF 03     VEC     scale=3(/64) x=3BF  y=-FF  i=0   ( 14.98 ,  -3.98 )
1BA4: 00 D0           RTS                         

; Player (as character)
;
1BA6: 4F 54 1F 03     VEC     scale=5(/16) x=31F  y=-4F  i=0   ( 49.93 ,  -4.93 )
1BAA: E9 C9           JSR     $09E9 ($13D2)       ; 
1BAC: 00 D0           RTS                         


; ?? Perhaps ROM padding for some reason

1BAE: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BB2: 00 00 2D 00     VEC     scale=0(/512)x=2D   y=0    i=0   (  0.08 ,   0.00 )
1BB6: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BBA: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BBE: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BC2: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BC6: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BCA: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BCE: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BD2: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BD6: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BDA: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BDE: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BE2: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BE6: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BEA: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BEE: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BF2: 00 00 00 00     VEC     scale=0(/512)x=0    y=0    i=0   (  0.00 ,   0.00 )
1BF6: 00 00 BF 30     VEC     scale=0(/512)x=BF   y=0    i=3   (  0.37 ,   0.00 )
```

# Player (Part 2) 

More ship/thrust pictures like at start

```html
<canvas width="1225" height="100"
  data-command="baseScale=1,x=50,y=50,1C06,x=125,y=50,1C46,x=200,y=50,1C88,x=275,y=50,1CCA,x=350,y=50,1D0E,x=425,y=50,1D4E,x=500,y=50,1D8A,x=575,y=50,1DCA,x=650,y=50,1E0A,x=725,y=50,1E48,x=800,y=50,1E88,x=875,y=50,1EC8,x=950,y=50,1F04,x=1025,y=50,1F44,x=1100,y=50,1F88,x=1175,y=50,1FCA">
</canvas>
```

```code
ShipsB:
; Thrust pattern
1BFA: FF 03 BF 34     VEC     scale=0(/512)x=-BF  y=3FF  i=3   ( -0.37 ,   1.99 )
1BFE: 3F F2           SVEC    scale=2(/32) x=-200 y=200  i=3   (-16.00 ,  16.00 )
1C00: 7F 34 3F F6     VEC     scale=3(/64) x=-23F y=-7F  i=15  ( -8.98 ,  -1.98 )
1C04: 00 D0           RTS                         
; Player facing left
1C06: 00 20 7F 06     VEC     scale=2(/128)x=-27F y=0    i=0   ( -4.99 ,   0.00 )
1C0A: 3F 41 7F F2     VEC     scale=4(/32) x=27F  y=13F  i=15  ( 19.96 ,   9.96 )
1C0E: 9F 46 5F F5     VEC     scale=4(/32) x=-15F y=-29F i=15  (-10.96 , -20.96 )
1C12: F6 F8           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
1C14: 7F 34 7F F2     VEC     scale=3(/64) x=27F  y=-7F  i=15  (  9.98 ,  -1.98 )
1C18: FF 41 1F F6     VEC     scale=4(/32) x=-21F y=1FF  i=15  (-16.96 ,  15.96 )
1C1C: 7F 25 7F F6     VEC     scale=2(/128)x=-27F y=-17F i=15  ( -4.99 ,  -2.99 )
1C20: FF 24 7F F2     VEC     scale=2(/128)x=27F  y=-FF  i=15  (  4.99 ,  -1.99 )
1C24: FF 41 1F F2     VEC     scale=4(/32) x=21F  y=1FF  i=15  ( 16.96 ,  15.96 )
1C28: 7F 34 7F F6     VEC     scale=3(/64) x=-27F y=-7F  i=15  ( -9.98 ,  -1.98 )
1C2C: F2 F8           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
1C2E: 9F 46 5F F1     VEC     scale=4(/32) x=15F  y=-29F i=15  ( 10.96 , -20.96 )
1C32: 1F 41 7F F6     VEC     scale=4(/32) x=-27F y=11F  i=15  (-19.96 ,   8.96 )
1C36: 00 D0           RTS                         
;
1C38: 3F 30 FF 03     VEC     scale=3(/64) x=3FF  y=3F   i=0   ( 15.98 ,   0.98 )
1C3C: BF 34 3F F2     VEC     scale=3(/64) x=23F  y=-BF  i=15  (  8.98 ,  -2.98 )
1C40: 7F 34 3F F6     VEC     scale=3(/64) x=-23F y=-7F  i=15  ( -8.98 ,  -1.98 )
1C44: 00 D0           RTS                         
;
1C46: 00 20 7F 06     VEC     scale=2(/128)x=-27F y=0    i=0   ( -4.99 ,   0.00 )
1C4A: FF 40 9F F2     VEC     scale=4(/32) x=29F  y=FF   i=15  ( 20.96 ,   7.96 )
1C4E: 5F 46 9F F5     VEC     scale=4(/32) x=-19F y=-25F i=15  (-12.96 , -18.96 )
1C52: F6 F8           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
1C54: BF 34 7F F2     VEC     scale=3(/64) x=27F  y=-BF  i=15  (  9.98 ,  -2.98 )
1C58: 3F 42 FF F5     VEC     scale=4(/32) x=-1FF y=23F  i=15  (-15.96 ,  17.96 )
1C5C: FF 24 7F F6     VEC     scale=2(/128)x=-27F y=-FF  i=15  ( -4.99 ,  -1.99 )
1C60: 7F 25 7F F2     VEC     scale=2(/128)x=27F  y=-17F i=15  (  4.99 ,  -2.99 )
1C64: BF 41 3F F2     VEC     scale=4(/32) x=23F  y=1BF  i=15  ( 17.96 ,  13.96 )
1C68: 3F 34 7F F6     VEC     scale=3(/64) x=-27F y=-3F  i=15  ( -9.98 ,  -0.98 )
1C6C: 7F 24 FF F3     VEC     scale=2(/128)x=3FF  y=-7F  i=15  (  7.99 ,  -0.99 )
1C70: BF 46 1F F1     VEC     scale=4(/32) x=11F  y=-2BF i=15  (  8.96 , -21.96 )
1C74: 5F 41 5F F6     VEC     scale=4(/32) x=-25F y=15F  i=15  (-18.96 ,  10.96 )
1C78: 00 D0           RTS                         
;
1C7A: 00 30 FF 03     VEC     scale=3(/64) x=3FF  y=0    i=0   ( 15.98 ,   0.00 )
1C7E: FF 25 FF F3     VEC     scale=2(/128)x=3FF  y=-1FF i=15  (  7.99 ,  -3.99 )
1C82: 3F 34 3F F6     VEC     scale=3(/64) x=-23F y=-3F  i=15  ( -8.98 ,  -0.98 )
1C86: 00 D0           RTS                         
;
1C88: 7F 20 7F 06     VEC     scale=2(/128)x=-27F y=7F   i=0   ( -4.99 ,   0.99 )
1C8C: BF 40 BF F2     VEC     scale=4(/32) x=2BF  y=BF   i=15  ( 21.96 ,   5.96 )
1C90: 5F 46 DF F5     VEC     scale=4(/32) x=-1DF y=-25F i=15  (-14.96 , -18.96 )
1C94: FF 20 FF F7     VEC     scale=2(/128)x=-3FF y=FF   i=15  ( -7.99 ,   1.99 )
1C98: FF 34 3F F2     VEC     scale=3(/64) x=23F  y=-FF  i=15  (  8.98 ,  -3.98 )
1C9C: 5F 42 9F F5     VEC     scale=4(/32) x=-19F y=25F  i=15  (-12.96 ,  18.96 )
1CA0: F7 F5           SVEC    scale=0(/128)x=-200 y=0    i=15  ( -4.00 ,   0.00 )
1CA2: 7F 25 7F F2     VEC     scale=2(/128)x=27F  y=-17F i=15  (  4.99 ,  -2.99 )
1CA6: 7F 41 7F F2     VEC     scale=4(/32) x=27F  y=17F  i=15  ( 19.96 ,  11.96 )
1CAA: 3F 30 BF F6     VEC     scale=3(/64) x=-2BF y=3F   i=15  (-10.98 ,   0.98 )
1CAE: FF 24 FF F3     VEC     scale=2(/128)x=3FF  y=-FF  i=15  (  7.99 ,  -1.99 )
1CB2: DF 46 DF F0     VEC     scale=4(/32) x=DF   y=-2DF i=15  (  6.96 , -22.96 )
1CB6: 9F 41 3F F6     VEC     scale=4(/32) x=-23F y=19F  i=15  (-17.96 ,  12.96 )
1CBA: 00 D0           RTS                         
;
1CBC: 3F 34 FF 03     VEC     scale=3(/64) x=3FF  y=-3F  i=0   ( 15.98 ,  -0.98 )
1CC0: FF 26 FF F3     VEC     scale=2(/128)x=3FF  y=-2FF i=15  (  7.99 ,  -5.99 )
1CC4: 00 30 7F F6     VEC     scale=3(/64) x=-27F y=0    i=15  ( -9.98 ,   0.00 )
1CC8: 00 D0           RTS                         
;
1CCA: 7F 20 7F 06     VEC     scale=2(/128)x=-27F y=7F   i=0   ( -4.99 ,   0.99 )
1CCE: 7F 40 BF F2     VEC     scale=4(/32) x=2BF  y=7F   i=15  ( 21.96 ,   3.96 )
1CD2: 1F 46 1F F6     VEC     scale=4(/32) x=-21F y=-21F i=15  (-16.96 , -16.96 )
1CD6: 7F 21 7F F7     VEC     scale=2(/128)x=-37F y=17F  i=15  ( -6.99 ,   2.99 )
1CDA: 3F 35 3F F2     VEC     scale=3(/64) x=23F  y=-13F i=15  (  8.98 ,  -4.98 )
1CDE: 7F 42 7F F5     VEC     scale=4(/32) x=-17F y=27F  i=15  (-11.96 ,  19.96 )
1CE2: 7F 24 7F F6     VEC     scale=2(/128)x=-27F y=-7F  i=15  ( -4.99 ,  -0.99 )
1CE6: 7F 26 FF F1     VEC     scale=2(/128)x=1FF  y=-27F i=15  (  3.99 ,  -4.99 )
1CEA: 5F 41 9F F2     VEC     scale=4(/32) x=29F  y=15F  i=15  ( 20.96 ,  10.96 )
1CEE: 7F 30 7F F6     VEC     scale=3(/64) x=-27F y=7F   i=15  ( -9.98 ,   1.98 )
1CF2: 7F 25 7F F3     VEC     scale=2(/128)x=37F  y=-17F i=15  (  6.99 ,  -2.99 )
1CF6: DF 46 7F F0     VEC     scale=4(/32) x=7F   y=-2DF i=15  (  3.96 , -22.96 )
1CFA: 7F 33 FF F7     VEC     scale=3(/64) x=-3FF y=37F  i=15  (-15.98 ,  13.98 )
1CFE: 00 D0           RTS                         
;
1D00: BF 34 FF 03     VEC     scale=3(/64) x=3FF  y=-BF  i=0   ( 15.98 ,  -2.98 )
1D04: FF 26 7F F3     VEC     scale=2(/128)x=37F  y=-2FF i=15  (  6.99 ,  -5.99 )
1D08: 3F 30 7F F6     VEC     scale=3(/64) x=-27F y=3F   i=15  ( -9.98 ,   0.98 )
1D0C: 00 D0           RTS                         
;
1D0E: FF 20 7F 06     VEC     scale=2(/128)x=-27F y=FF   i=0   ( -4.99 ,   1.99 )
1D12: 1F 40 DF F2     VEC     scale=4(/32) x=2DF  y=1F   i=15  ( 22.96 ,   0.96 )
1D16: DF 45 3F F6     VEC     scale=4(/32) x=-23F y=-1DF i=15  (-17.96 , -14.96 )
1D1A: F6 F9           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
1D1C: 7F 27 FF F3     VEC     scale=2(/128)x=3FF  y=-37F i=15  (  7.99 ,  -6.99 )
1D20: BF 42 1F F5     VEC     scale=4(/32) x=-11F y=2BF  i=15  ( -8.96 ,  21.96 )
1D24: 7F 24 FF F6     VEC     scale=2(/128)x=-2FF y=-7F  i=15  ( -5.99 ,  -0.99 )
1D28: 7F 26 FF F1     VEC     scale=2(/128)x=1FF  y=-27F i=15  (  3.99 ,  -4.99 )
1D2C: 1F 41 BF F2     VEC     scale=4(/32) x=2BF  y=11F  i=15  ( 21.96 ,   8.96 )
1D30: BF 30 BF F6     VEC     scale=3(/64) x=-2BF y=BF   i=15  (-10.98 ,   2.98 )
1D34: F2 FD           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
1D36: DF 46 3F F0     VEC     scale=4(/32) x=3F   y=-2DF i=15  (  1.96 , -22.96 )
1D3A: FF 33 BF F7     VEC     scale=3(/64) x=-3BF y=3FF  i=15  (-14.98 ,  15.98 )
1D3E: 00 D0           RTS                         
;
1D40: FF 34 BF 03     VEC     scale=3(/64) x=3BF  y=-FF  i=0   ( 14.98 ,  -3.98 )
1D44: 7F 27 7F F3     VEC     scale=2(/128)x=37F  y=-37F i=15  (  6.99 ,  -6.99 )
1D48: 3F 30 3F F6     VEC     scale=3(/64) x=-23F y=3F   i=15  ( -8.98 ,   0.98 )
1D4C: 00 D0           RTS                         
;
1D4E: 06 F1           SVEC    scale=0(/128)x=-200 y=0    i=0   ( -4.00 ,   0.00 )
1D50: 1F 44 BF F2     VEC     scale=4(/32) x=2BF  y=-1F  i=15  ( 21.96 ,  -0.96 )
1D54: 9F 45 5F F6     VEC     scale=4(/32) x=-25F y=-19F i=15  (-18.96 , -12.96 )
1D58: F6 F9           SVEC    scale=1(/64) x=-200 y=0    i=15  ( -8.00 ,   0.00 )
1D5A: BF 35 3F F2     VEC     scale=3(/64) x=23F  y=-1BF i=15  (  8.98 ,  -6.98 )
1D5E: DF 42 FF F4     VEC     scale=4(/32) x=-FF  y=2DF  i=15  ( -7.96 ,  22.96 )
1D62: F7 F0           SVEC    scale=0(/128)x=-200 y=0    i=15  ( -4.00 ,   0.00 )
1D64: 7F 26 7F F1     VEC     scale=2(/128)x=17F  y=-27F i=15  (  2.99 ,  -4.99 )
1D68: BF 40 DF F2     VEC     scale=4(/32) x=2DF  y=BF   i=15  ( 22.96 ,   5.96 )
1D6C: BF 30 BF F6     VEC     scale=3(/64) x=-2BF y=BF   i=15  (-10.98 ,   2.98 )
1D70: F2 FD           SVEC    scale=1(/64) x=200  y=0    i=15  (  8.00 ,   0.00 )
1D72: DF 46 1F F4     VEC     scale=4(/32) x=-1F  y=-2DF i=15  ( -0.96 , -22.96 )
1D76: 1F 42 7F F5     VEC     scale=4(/32) x=-17F y=21F  i=15  (-11.96 ,  16.96 )
1D7A: 00 D0           RTS                         
;
1D7C: 7F 35 BF 03     VEC     scale=3(/64) x=3BF  y=-17F i=0   ( 14.98 ,  -5.98 )
1D80: 7F 27 FF F2     VEC     scale=2(/128)x=2FF  y=-37F i=15  (  5.99 ,  -6.99 )
1D84: 7F 30 7F F6     VEC     scale=3(/64) x=-27F y=7F   i=15  ( -9.98 ,   1.98 )
1D88: 00 D0           RTS                         
;
1D8A: FF 12 FF 07     VEC     scale=1(/256)x=-3FF y=2FF  i=0   ( -3.99 ,   2.99 )
1D8E: 5F 44 BF F2     VEC     scale=4(/32) x=2BF  y=-5F  i=15  ( 21.96 ,  -2.96 )
1D92: 7F 45 7F F6     VEC     scale=4(/32) x=-27F y=-17F i=15  (-19.96 , -11.96 )
1D96: 7F 22 FF F7     VEC     scale=2(/128)x=-3FF y=27F  i=15  ( -7.99 ,   4.99 )
1D9A: F2 FE           SVEC    scale=1(/64) x=200  y=-200 i=15  (  8.00 ,  -8.00 )
1D9C: FF 42 9F F4     VEC     scale=4(/32) x=-9F  y=2FF  i=15  ( -4.96 ,  23.96 )
1DA0: F7 F0           SVEC    scale=0(/128)x=-200 y=0    i=15  ( -4.00 ,   0.00 )
1DA2: 7F 26 FF F0     VEC     scale=2(/128)x=FF   y=-27F i=15  (  1.99 ,  -4.99 )
1DA6: 7F 40 FF F2     VEC     scale=4(/32) x=2FF  y=7F   i=15  ( 23.96 ,   3.96 )
1DAA: FF 30 BF F6     VEC     scale=3(/64) x=-2BF y=FF   i=15  (-10.98 ,   3.98 )
1DAE: 7F 26 FF F3     VEC     scale=2(/128)x=3FF  y=-27F i=15  (  7.99 ,  -4.99 )
1DB2: DF 46 5F F4     VEC     scale=4(/32) x=-5F  y=-2DF i=15  ( -2.96 , -22.96 )
1DB6: 5F 42 5F F5     VEC     scale=4(/32) x=-15F y=25F  i=15  (-10.96 ,  18.96 )
1DBA: 00 D0           RTS                         
;
1DBC: BF 35 7F 03     VEC     scale=3(/64) x=37F  y=-1BF i=0   ( 13.98 ,  -6.98 )
1DC0: FF 27 7F F2     VEC     scale=2(/128)x=27F  y=-3FF i=15  (  4.99 ,  -7.99 )
1DC4: BF 30 3F F6     VEC     scale=3(/64) x=-23F y=BF   i=15  ( -8.98 ,   2.98 )
1DC8: 00 D0           RTS                         
;
1DCA: FF 12 FF 07     VEC     scale=1(/256)x=-3FF y=2FF  i=0   ( -3.99 ,   2.99 )
1DCE: 7F 44 BF F2     VEC     scale=4(/32) x=2BF  y=-7F  i=15  ( 21.96 ,  -3.96 )
1DD2: 3F 45 BF F6     VEC     scale=4(/32) x=-2BF y=-13F i=15  (-21.96 ,  -9.96 )
1DD6: 7F 22 7F F7     VEC     scale=2(/128)x=-37F y=27F  i=15  ( -6.99 ,   4.99 )
1DDA: F2 FE           SVEC    scale=1(/64) x=200  y=-200 i=15  (  8.00 ,  -8.00 )
1DDC: DF 42 7F F4     VEC     scale=4(/32) x=-7F  y=2DF  i=15  ( -3.96 ,  22.96 )
1DE0: 7F 20 7F F6     VEC     scale=2(/128)x=-27F y=7F   i=15  ( -4.99 ,   0.99 )
1DE4: 7F 26 FF F0     VEC     scale=2(/128)x=FF   y=-27F i=15  (  1.99 ,  -4.99 )
1DE8: 1F 40 DF F2     VEC     scale=4(/32) x=2DF  y=1F   i=15  ( 22.96 ,   0.96 )
1DEC: 7F 31 3F F6     VEC     scale=3(/64) x=-23F y=17F  i=15  ( -8.98 ,   5.98 )
1DF0: F3 F7           SVEC    scale=0(/128)x=200  y=-200 i=15  (  4.00 ,  -4.00 )
1DF2: DF 46 9F F4     VEC     scale=4(/32) x=-9F  y=-2DF i=15  ( -4.96 , -22.96 )
1DF6: 7F 42 1F F5     VEC     scale=4(/32) x=-11F y=27F  i=15  ( -8.96 ,  19.96 )
1DFA: 00 D0           RTS                         
;
1DFC: 3F 36 3F 03     VEC     scale=3(/64) x=33F  y=-23F i=0   ( 12.98 ,  -8.98 )
1E00: FF 27 FF F1     VEC     scale=2(/128)x=1FF  y=-3FF i=15  (  3.99 ,  -7.99 )
1E04: FF 21 FF F7     VEC     scale=2(/128)x=-3FF y=1FF  i=15  ( -7.99 ,   3.99 )
1E08: 00 D0           RTS                         
;
1E0A: 06 F2           SVEC    scale=0(/128)x=-200 y=200  i=0   ( -4.00 ,   4.00 )
1E0C: DF 44 9F F2     VEC     scale=4(/32) x=29F  y=-DF  i=15  ( 20.96 ,  -6.96 )
1E10: FF 44 BF F6     VEC     scale=4(/32) x=-2BF y=-FF  i=15  (-21.96 ,  -7.96 )
1E14: F7 F3           SVEC    scale=0(/128)x=-200 y=200  i=15  ( -4.00 ,   4.00 )
1E16: 3F 36 7F F1     VEC     scale=3(/64) x=17F  y=-23F i=15  (  5.98 ,  -8.98 )
1E1A: FF 42 1F F4     VEC     scale=4(/32) x=-1F  y=2FF  i=15  ( -0.96 ,  23.96 )
1E1E: 7F 20 7F F6     VEC     scale=2(/128)x=-27F y=7F   i=15  ( -4.99 ,   0.99 )
1E22: 7F 26 7F F0     VEC     scale=2(/128)x=7F   y=-27F i=15  (  0.99 ,  -4.99 )
1E26: 1F 44 FF F2     VEC     scale=4(/32) x=2FF  y=-1F  i=15  ( 23.96 ,  -0.96 )
1E2A: 7F 31 3F F6     VEC     scale=3(/64) x=-23F y=17F  i=15  ( -8.98 ,   5.98 )
1E2E: F3 F7           SVEC    scale=0(/128)x=200  y=-200 i=15  (  4.00 ,  -4.00 )
1E30: BF 46 FF F4     VEC     scale=4(/32) x=-FF  y=-2BF i=15  ( -7.96 , -21.96 )
1E34: 9F 42 DF F4     VEC     scale=4(/32) x=-DF  y=29F  i=15  ( -6.96 ,  20.96 )
1E38: 00 D0           RTS                         
;
1E3A: 7F 36 FF 02     VEC     scale=3(/64) x=2FF  y=-27F i=0   ( 11.98 ,  -9.98 )
1E3E: 3F 36 BF F0     VEC     scale=3(/64) x=BF   y=-23F i=15  (  2.98 ,  -8.98 )
1E42: 7F 22 FF F7     VEC     scale=2(/128)x=-3FF y=27F  i=15  ( -7.99 ,   4.99 )
1E46: 00 D0           RTS                         
;
1E48: FF 13 FF 06     VEC     scale=1(/256)x=-2FF y=3FF  i=0   ( -2.99 ,   3.99 )
1E4C: 1F 45 7F F2     VEC     scale=4(/32) x=27F  y=-11F i=15  ( 19.96 ,  -8.96 )
1E50: 9F 44 DF F6     VEC     scale=4(/32) x=-2DF y=-9F  i=15  (-22.96 ,  -4.96 )
1E54: F7 F3           SVEC    scale=0(/128)x=-200 y=200  i=15  ( -4.00 ,   4.00 )
1E56: 3F 36 7F F1     VEC     scale=3(/64) x=17F  y=-23F i=15  (  5.98 ,  -8.98 )
1E5A: DF 42 1F F0     VEC     scale=4(/32) x=1F   y=2DF  i=15  (  0.96 ,  22.96 )
1E5E: FF 20 7F F6     VEC     scale=2(/128)x=-27F y=FF   i=15  ( -4.99 ,   1.99 )
1E62: 7F 26 7F F0     VEC     scale=2(/128)x=7F   y=-27F i=15  (  0.99 ,  -4.99 )
1E66: 7F 44 DF F2     VEC     scale=4(/32) x=2DF  y=-7F  i=15  ( 22.96 ,  -3.96 )
1E6A: F6 FA           SVEC    scale=1(/64) x=-200 y=200  i=15  ( -8.00 ,   8.00 )
1E6C: 7F 27 7F F2     VEC     scale=2(/128)x=27F  y=-37F i=15  (  4.99 ,  -6.99 )
1E70: BF 46 3F F5     VEC     scale=4(/32) x=-13F y=-2BF i=15  ( -9.96 , -21.96 )
1E74: BF 42 7F F4     VEC     scale=4(/32) x=-7F  y=2BF  i=15  ( -3.96 ,  21.96 )
1E78: 00 D0           RTS                         
;
1E7A: BF 36 BF 02     VEC     scale=3(/64) x=2BF  y=-2BF i=0   ( 10.98 , -10.98 )
1E7E: 7F 36 7F F0     VEC     scale=3(/64) x=7F   y=-27F i=15  (  1.98 ,  -9.98 )
1E82: FF 22 7F F7     VEC     scale=2(/128)x=-37F y=2FF  i=15  ( -6.99 ,   5.99 )
1E86: 00 D0           RTS                         
;
1E88: FF 13 FF 06     VEC     scale=1(/256)x=-2FF y=3FF  i=0   ( -2.99 ,   3.99 )
1E8C: 5F 45 5F F2     VEC     scale=4(/32) x=25F  y=-15F i=15  ( 18.96 , -10.96 )
1E90: 5F 44 DF F6     VEC     scale=4(/32) x=-2DF y=-5F  i=15  (-22.96 ,  -2.96 )
1E94: FF 23 7F F6     VEC     scale=2(/128)x=-27F y=3FF  i=15  ( -4.99 ,   7.99 )
1E98: BF 36 FF F0     VEC     scale=3(/64) x=FF   y=-2BF i=15  (  3.98 , -10.98 )
1E9C: FF 42 7F F0     VEC     scale=4(/32) x=7F   y=2FF  i=15  (  3.96 ,  23.96 )
1EA0: FF 20 7F F6     VEC     scale=2(/128)x=-27F y=FF   i=15  ( -4.99 ,   1.99 )
1EA4: F4 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
1EA6: 9F 44 FF F2     VEC     scale=4(/32) x=2FF  y=-9F  i=15  ( 23.96 ,  -4.96 )
1EAA: F6 FA           SVEC    scale=1(/64) x=-200 y=200  i=15  ( -8.00 ,   8.00 )
1EAC: FF 27 7F F2     VEC     scale=2(/128)x=27F  y=-3FF i=15  (  4.99 ,  -7.99 )
1EB0: 7F 46 7F F5     VEC     scale=4(/32) x=-17F y=-27F i=15  (-11.96 , -19.96 )
1EB4: BF 42 5F F4     VEC     scale=4(/32) x=-5F  y=2BF  i=15  ( -2.96 ,  21.96 )
1EB8: 00 D0           RTS                         
;
1EBA: 3F 37 7F 02     VEC     scale=3(/64) x=27F  y=-33F i=0   (  9.98 , -12.98 )
1EBE: 3F 36 3F F0     VEC     scale=3(/64) x=3F   y=-23F i=15  (  0.98 ,  -8.98 )
1EC2: 7F 23 7F F7     VEC     scale=2(/128)x=-37F y=37F  i=15  ( -6.99 ,   6.99 )
1EC6: 00 D0           RTS                         
;
1EC8: 05 F2           SVEC    scale=0(/128)x=0    y=200  i=0   (  0.00 ,   4.00 )
1ECA: 7F 45 1F F2     VEC     scale=4(/32) x=21F  y=-17F i=15  ( 16.96 , -11.96 )
1ECE: 1F 44 DF F6     VEC     scale=4(/32) x=-2DF y=-1F  i=15  (-22.96 ,  -0.96 )
1ED2: F5 FA           SVEC    scale=1(/64) x=0    y=200  i=15  (  0.00 ,   8.00 )
1ED4: BF 36 BF F0     VEC     scale=3(/64) x=BF   y=-2BF i=15  (  2.98 , -10.98 )
1ED8: DF 42 BF F0     VEC     scale=4(/32) x=BF   y=2DF  i=15  (  5.96 ,  22.96 )
1EDC: 7F 21 7F F6     VEC     scale=2(/128)x=-27F y=17F  i=15  ( -4.99 ,   2.99 )
1EE0: F4 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
1EE2: FF 44 DF F2     VEC     scale=4(/32) x=2DF  y=-FF  i=15  ( 22.96 ,  -7.96 )
1EE6: 3F 32 BF F5     VEC     scale=3(/64) x=-1BF y=23F  i=15  ( -6.98 ,   8.98 )
1EEA: F1 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
1EEC: 5F 46 9F F5     VEC     scale=4(/32) x=-19F y=-25F i=15  (-12.96 , -18.96 )
1EF0: BF 42 1F F4     VEC     scale=4(/32) x=-1F  y=2BF  i=15  ( -0.96 ,  21.96 )
1EF4: 00 D0           RTS                         
;
1EF6: 3F 37 FF 01     VEC     scale=3(/64) x=1FF  y=-33F i=0   (  7.98 , -12.98 )
1EFA: 7F 36 3F F0     VEC     scale=3(/64) x=3F   y=-27F i=15  (  0.98 ,  -9.98 )
1EFE: 7F 23 FF F6     VEC     scale=2(/128)x=-2FF y=37F  i=15  ( -5.99 ,   6.99 )
1F02: 00 D0           RTS                         
;
1F04: 7F 22 FF 04     VEC     scale=2(/128)x=-FF  y=27F  i=0   ( -1.99 ,   4.99 )
1F08: BF 37 FF F3     VEC     scale=3(/64) x=3FF  y=-3BF i=15  ( 15.98 , -14.98 )
1F0C: 3F 40 DF F6     VEC     scale=4(/32) x=-2DF y=3F   i=15  (-22.96 ,   1.96 )
1F10: F5 FA           SVEC    scale=1(/64) x=0    y=200  i=15  (  0.00 ,   8.00 )
1F12: BF 36 BF F0     VEC     scale=3(/64) x=BF   y=-2BF i=15  (  2.98 , -10.98 )
1F16: BF 42 1F F1     VEC     scale=4(/32) x=11F  y=2BF  i=15  (  8.96 ,  21.96 )
1F1A: FF 21 7F F6     VEC     scale=2(/128)x=-27F y=1FF  i=15  ( -4.99 ,   3.99 )
1F1E: FF 26 7F F4     VEC     scale=2(/128)x=-7F  y=-2FF i=15  ( -0.99 ,  -5.99 )
1F22: 1F 45 BF F2     VEC     scale=4(/32) x=2BF  y=-11F i=15  ( 21.96 ,  -8.96 )
1F26: FF 23 7F F7     VEC     scale=2(/128)x=-37F y=3FF  i=15  ( -6.99 ,   7.99 )
1F2A: F1 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
1F2C: 3F 46 DF F5     VEC     scale=4(/32) x=-1DF y=-23F i=15  (-14.96 , -17.96 )
1F30: DF 42 1F F0     VEC     scale=4(/32) x=1F   y=2DF  i=15  (  0.96 ,  22.96 )
1F34: 00 D0           RTS                         
;
1F36: 7F 37 BF 01     VEC     scale=3(/64) x=1BF  y=-37F i=0   (  6.98 , -13.98 )
1F3A: 7F 36 00 F4     VEC     scale=3(/64) x=0    y=-27F i=15  (  0.00 ,  -9.98 )
1F3E: FF 23 FF F6     VEC     scale=2(/128)x=-2FF y=3FF  i=15  ( -5.99 ,   7.99 )
1F42: 00 D0           RTS                         
;
1F44: 7F 22 7F 04     VEC     scale=2(/128)x=-7F  y=27F  i=0   ( -0.99 ,   4.99 )
1F48: FF 37 7F F3     VEC     scale=3(/64) x=37F  y=-3FF i=15  ( 13.98 , -15.98 )
1F4C: 7F 40 DF F6     VEC     scale=4(/32) x=-2DF y=7F   i=15  (-22.96 ,   3.96 )
1F50: 7F 23 7F F5     VEC     scale=2(/128)x=-17F y=37F  i=15  ( -2.99 ,   6.99 )
1F54: 7F 36 7F F0     VEC     scale=3(/64) x=7F   y=-27F i=15  (  1.98 ,  -9.98 )
1F58: 9F 42 5F F1     VEC     scale=4(/32) x=15F  y=29F  i=15  ( 10.96 ,  20.96 )
1F5C: FF 21 7F F6     VEC     scale=2(/128)x=-27F y=1FF  i=15  ( -4.99 ,   3.99 )
1F60: 7F 26 7F F4     VEC     scale=2(/128)x=-7F  y=-27F i=15  ( -0.99 ,  -4.99 )
1F64: 7F 45 7F F2     VEC     scale=4(/32) x=27F  y=-17F i=15  ( 19.96 , -11.96 )
1F68: 3F 32 3F F5     VEC     scale=3(/64) x=-13F y=23F  i=15  ( -4.98 ,   8.98 )
1F6C: 7F 27 7F F1     VEC     scale=2(/128)x=17F  y=-37F i=15  (  2.99 ,  -6.99 )
1F70: 1F 46 1F F6     VEC     scale=4(/32) x=-21F y=-21F i=15  (-16.96 , -16.96 )
1F74: BF 42 7F F0     VEC     scale=4(/32) x=7F   y=2BF  i=15  (  3.96 ,  21.96 )
1F78: 00 D0           RTS                         
;
1F7A: BF 37 3F 01     VEC     scale=3(/64) x=13F  y=-3BF i=0   (  4.98 , -14.98 )
1F7E: 3F 36 3F F4     VEC     scale=3(/64) x=-3F  y=-23F i=15  ( -0.98 ,  -8.98 )
1F82: FF 23 FF F5     VEC     scale=2(/128)x=-1FF y=3FF  i=15  ( -3.99 ,   7.99 )
1F86: 00 D0           RTS                         
;
1F88: 7F 22 7F 04     VEC     scale=2(/128)x=-7F  y=27F  i=0   ( -0.99 ,   4.99 )
1F8C: 3F 46 9F F1     VEC     scale=4(/32) x=19F  y=-23F i=15  ( 12.96 , -17.96 )
1F90: DF 40 DF F6     VEC     scale=4(/32) x=-2DF y=DF   i=15  (-22.96 ,   6.96 )
1F94: FF 23 FF F4     VEC     scale=2(/128)x=-FF  y=3FF  i=15  ( -1.99 ,   7.99 )
1F98: BF 36 3F F0     VEC     scale=3(/64) x=3F   y=-2BF i=15  (  0.98 , -10.98 )
1F9C: 7F 42 7F F1     VEC     scale=4(/32) x=17F  y=27F  i=15  ( 11.96 ,  19.96 )
1FA0: 7F 22 7F F5     VEC     scale=2(/128)x=-17F y=27F  i=15  ( -2.99 ,   4.99 )
1FA4: F5 F7           SVEC    scale=0(/128)x=0    y=-200 i=15  (  0.00 ,  -4.00 )
1FA6: 9F 45 5F F2     VEC     scale=4(/32) x=25F  y=-19F i=15  ( 18.96 , -12.96 )
1FAA: 3F 32 FF F4     VEC     scale=3(/64) x=-FF  y=23F  i=15  ( -3.98 ,   8.98 )
1FAE: FF 27 FF F0     VEC     scale=2(/128)x=FF   y=-3FF i=15  (  1.99 ,  -7.99 )
1FB2: DF 45 5F F6     VEC     scale=4(/32) x=-25F y=-1DF i=15  (-18.96 , -14.96 )
1FB6: BF 42 BF F0     VEC     scale=4(/32) x=BF   y=2BF  i=15  (  5.96 ,  21.96 )
1FBA: 00 D0           RTS                         
;
1FBC: FF 37 FF 00     VEC     scale=3(/64) x=FF   y=-3FF i=0   (  3.98 , -15.98 )
1FC0: 3F 36 7F F4     VEC     scale=3(/64) x=-7F  y=-23F i=15  ( -1.98 ,  -8.98 )
1FC4: 3F 32 BF F4     VEC     scale=3(/64) x=-BF  y=23F  i=15  ( -2.98 ,   8.98 )
1FC8: 00 D0           RTS                         
;
1FCA: 7F 22 00 04     VEC     scale=2(/128)x=0    y=27F  i=0   (  0.00 ,   4.99 )
1FCE: 5F 46 5F F1     VEC     scale=4(/32) x=15F  y=-25F i=15  ( 10.96 , -18.96 )
1FD2: 1F 41 BF F6     VEC     scale=4(/32) x=-2BF y=11F  i=15  (-21.96 ,   8.96 )
1FD6: FF 23 7F F4     VEC     scale=2(/128)x=-7F  y=3FF  i=15  ( -0.99 ,   7.99 )
1FDA: 7F 36 3F F4     VEC     scale=3(/64) x=-3F  y=-27F i=15  ( -0.98 ,  -9.98 )
1FDE: 3F 42 BF F1     VEC     scale=4(/32) x=1BF  y=23F  i=15  ( 13.96 ,  17.96 )
1FE2: 7F 22 7F F5     VEC     scale=2(/128)x=-17F y=27F  i=15  ( -2.99 ,   4.99 )
1FE6: 7F 26 FF F4     VEC     scale=2(/128)x=-FF  y=-27F i=15  ( -1.99 ,  -4.99 )
1FEA: FF 45 3F F2     VEC     scale=4(/32) x=23F  y=-1FF i=15  ( 17.96 , -15.96 )
1FEE: 7F 32 BF F4     VEC     scale=3(/64) x=-BF  y=27F  i=15  ( -2.98 ,   9.98 )
1FF2: F4 FE           SVEC    scale=1(/64) x=0    y=-200 i=15  (  0.00 ,  -8.00 )
1FF4: 9F 45 5F F6     VEC     scale=4(/32) x=-25F y=-19F i=15  (-18.96 , -12.96 )
1FF8: 9F 42 FF F0     VEC     scale=4(/32) x=FF   y=29F  i=15  (  7.96 ,  20.96 )
1FFC: 00 D0           RTS                         

; ?? not used
1FFE: FB FF           SVEC    scale=3(/16) x=200  y=-200 i=15  ( 32.00 , -32.00 )
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

