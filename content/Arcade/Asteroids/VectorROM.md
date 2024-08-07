![Asteroids DVG Vector ROM](Asteroids.jpg)

# Asteroids DVG Vector ROM

>>> cpu DVG

>>> binary 0800:roms/035127.02

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
  data-origin="0800"
  data-command="screenScale=0.5,0800">
</canvas>
```

```code
0800: 80 A0 00 00     CUR     scale=00(/512)           x=0       y=128
0804: 00 70 00 00     VEC     scale=07(/4)   bri=0     x=0       y=0       (0.0000, 0.0000)
0808: 00 90 FF 73     VEC     scale=09(/1)   bri=7     x=1023    y=0       (1023.0000, 0.0000)
080C: FF 92 00 70     VEC     scale=09(/1)   bri=7     x=0       y=767     (0.0000, 767.0000)
0810: 00 90 FF 77     VEC     scale=09(/1)   bri=7     x=-1023   y=0       (-1023.0000, 0.0000)
0814: FF 96 00 70     VEC     scale=09(/1)   bri=7     x=0       y=-767    (0.0000, -767.0000)
;
0818: FF 92 FF 72     VEC     scale=09(/1)   bri=7     x=767     y=767     (767.0000, 767.0000)
081C: 00 86 00 72     VEC     scale=08(/2)   bri=7     x=512     y=-512    (256.0000, -256.0000)
0820: FE 87 FE 77     VEC     scale=08(/2)   bri=7     x=-1022   y=-1022   (-511.0000, -511.0000)
0824: 00 92 00 76     VEC     scale=09(/1)   bri=7     x=-512    y=512     (-512.0000, 512.0000)
0828: FE 81 00 72     VEC     scale=08(/2)   bri=7     x=512     y=510     (256.0000, 255.0000)
082C: FF 96 FF 72     VEC     scale=09(/1)   bri=7     x=767     y=-767    (767.0000, -767.0000)
0830: 7F A3 FF 03     CUR     scale=00(/512)           x=1023    y=895
;
0834: 00 70 00 00     VEC     scale=07(/4)   bri=0     x=0       y=0       (0.0000, 0.0000)
0838: FF 96 FF 76     VEC     scale=09(/1)   bri=7     x=-767    y=-767    (-767.0000, -767.0000)
083C: FE 81 00 76     VEC     scale=08(/2)   bri=7     x=-512    y=510     (-256.0000, 255.0000)
0840: 00 92 00 72     VEC     scale=09(/1)   bri=7     x=512     y=512     (512.0000, 512.0000)
0844: FE 87 FE 73     VEC     scale=08(/2)   bri=7     x=1022    y=-1022   (511.0000, -511.0000)
0848: 00 86 00 76     VEC     scale=08(/2)   bri=7     x=-512    y=-512    (-256.0000, -256.0000)
084C: FF 92 FF 76     VEC     scale=09(/1)   bri=7     x=-767    y=767     (-767.0000, 767.0000)
0850: FC A1 F4 01     CUR     scale=00(/512)           x=500     y=508
;     
0854: 00 70 00 00     VEC     scale=07(/4)   bri=0     x=0       y=0       (0.0000, 0.0000)
0858: DB F0           SVEC    scale=02(*8)   bri=13    x=3       y=0       (24.0000, 0.0000)
085A: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
085C: CF F0           SVEC    scale=02(*8)   bri=12    x=-3      y=0       (-24.0000, 0.0000)
085E: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
0860: BB F0           SVEC    scale=02(*8)   bri=11    x=3       y=0       (24.0000, 0.0000)
0862: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
0864: AF F0           SVEC    scale=02(*8)   bri=10    x=-3      y=0       (-24.0000, 0.0000)
0866: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
0868: 9B F0           SVEC    scale=02(*8)   bri=9     x=3       y=0       (24.0000, 0.0000)
086A: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
086C: 8F F0           SVEC    scale=02(*8)   bri=8     x=-3      y=0       (-24.0000, 0.0000)
086E: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
0870: 7B F0           SVEC    scale=02(*8)   bri=7     x=3       y=0       (24.0000, 0.0000)
0872: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
0874: 6F F0           SVEC    scale=02(*8)   bri=6     x=-3      y=0       (-24.0000, 0.0000)
0876: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
0878: 5B F0           SVEC    scale=02(*8)   bri=5     x=3       y=0       (24.0000, 0.0000)
087A: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
087C: 4F F0           SVEC    scale=02(*8)   bri=4     x=-3      y=0       (-24.0000, 0.0000)
087E: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
0880: 3B F0           SVEC    scale=02(*8)   bri=3     x=3       y=0       (24.0000, 0.0000)
0882: 00 F9           SVEC    scale=01(*4)   bri=0     x=0       y=1       (0.0000, 4.0000)
0884: 2F F0           SVEC    scale=02(*8)   bri=2     x=-3      y=0       (-24.0000, 0.0000)
0886: 7C D0           RTS                         
```

# Bank Error 

```html
<canvas width="500" height="60"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="0800"
  data-command="x=20,y=45,baseScale=1,088C">
</canvas>
```

```code
; In Revision 1 of this ROM, the text is: "PAGE SELECT ERROR"

; "BANK ERROR"  In this Revision 2
0888: E4 A0 5E 11     CUR     scale=01(/256)           x=350     y=228
088C: 00 70 00 00     VEC     scale=07(/4)   bri=0     x=0       y=0       (0.0000, 0.0000)
0890: 80 CA           JSR     $0D00               ; {}
0892: 78 CA           JSR     $0CF0               ; {}
0894: D8 CA           JSR     $0DB0               ; {}
0896: C7 CA           JSR     $0D8E               ; {}
0898: 2C CB           JSR     $0E58               ; {}
089A: 9B CA           JSR     $0D36               ; {}
089C: F3 CA           JSR     $0DE6               ; {}
089E: F3 CA           JSR     $0DE6               ; {}
08A0: DD CA           JSR     $0DBA               ; {}
08A2: F3 EA           JMP     $0DE6               ; {}
```

# Credits 

```html
<canvas width="500" height="60"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="0800"
  data-command="x=20,y=45,baseScale=1,08B8">
</canvas>
```

```code
; In Revision 1 of this ROM the text is "ASTEROIDS BY ATARI"

; "c 1979 ATARI INC" In this Revision 2
08A4: 80 A0 90 01     CUR     scale=00(/512)           x=400     y=128
08A8: 00 70 00 00     VEC     scale=07(/4)   bri=0     x=0       y=0       (0.0000, 0.0000)
08AC: 73 F5           SVEC    scale=00(*2)   bri=7     x=3       y=-1      (6.0000, -2.0000)
08AE: 73 F1           SVEC    scale=00(*2)   bri=7     x=3       y=1       (6.0000, 2.0000)
08B0: 78 F1           SVEC    scale=02(*8)   bri=7     x=0       y=1       (0.0000, 8.0000)
08B2: 77 F1           SVEC    scale=00(*2)   bri=7     x=-3      y=1       (-6.0000, 2.0000)
08B4: 77 F5           SVEC    scale=00(*2)   bri=7     x=-3      y=-1      (-6.0000, -2.0000)
08B6: 78 F5           SVEC    scale=02(*8)   bri=7     x=0       y=-1      (0.0000, -8.0000)
08B8: 80 31 00 02     VEC     scale=03(/64)  bri=0     x=512     y=384     (8.0000, 6.0000)
08BC: 75 F8           SVEC    scale=01(*4)   bri=7     x=-1      y=0       (-4.0000, 0.0000)
08BE: 70 FD           SVEC    scale=01(*4)   bri=7     x=0       y=-1      (0.0000, -4.0000)
08C0: 71 F8           SVEC    scale=01(*4)   bri=7     x=1       y=0       (4.0000, 0.0000)
08C2: 02 FD           SVEC    scale=01(*4)   bri=0     x=2       y=-1      (8.0000, -4.0000)
08C4: 2E CB           JSR     $0E5C               ; {}
08C6: 63 CB           JSR     $0EC6               ; {}
08C8: 56 CB           JSR     $0EAC               ; {}
08CA: 63 CB           JSR     $0EC6               ; {}
08CC: 2C CB           JSR     $0E58               ; {}
08CE: 78 CA           JSR     $0CF0               ; {}
08D0: 02 CB           JSR     $0E04               ; {}
08D2: 78 CA           JSR     $0CF0               ; {}
08D4: F3 CA           JSR     $0DE6               ; {}
08D6: BA CA           JSR     $0D74               ; {}
08D8: 2C CB           JSR     $0E58               ; {}
08DA: BA CA           JSR     $0D74               ; {}
08DC: D8 CA           JSR     $0DB0               ; {}
08DE: 8D EA           JMP     $0D1A               ; {}

; Ship Explosion
08E0: C6 FF           SVEC    scale=01(*4)   bri=12    x=-2      y=-3      (-8.0000, -12.0000)
08E2: C1 FE           SVEC    scale=01(*4)   bri=12    x=1       y=-2      (4.0000, -8.0000)
08E4: C3 F1           SVEC    scale=00(*2)   bri=12    x=3       y=1       (6.0000, 2.0000)
08E6: CD F1           SVEC    scale=02(*8)   bri=12    x=-1      y=1       (-8.0000, 8.0000)
08E8: C7 F1           SVEC    scale=00(*2)   bri=12    x=-3      y=1       (-6.0000, 2.0000)
08EA: C1 FD           SVEC    scale=01(*4)   bri=12    x=1       y=-1      (4.0000, -4.0000)

; Ship explosion pieces velocity (x, y)
08EC: D8 1E ; (-40,  30)
08EE: 32 EC ; ( 50, -20)
08F0: 00 C4 ; (  0, -60)
08F2: 3C 14 ; ( 60,  20)
08F4: 0A 46 ; ( 10,  70)
08F6: D8 D8 ; (-40, -40)
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
  data-origin="0800"
  data-command="baseScale=0,x=50,y=50,09A0,x=150,y=50,096A,x=250,y=50,092C,x=350,y=50,0900">
</canvas>
```

```code
; Jump table for 4
08F8: D0 C8           JSR     $09A0               ; {}
08FA: B5 C8           JSR     $096A               ; {}
08FC: 96 C8           JSR     $092C               ; {}
08FE: 80 C8           JSR     $0900               ; {}
;
; Shrapnel pattern 1
0900: 0D F8           SVEC    scale=03(*16)  bri=0     x=-1      y=0       (-16.0000, 0.0000)
0902: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0904: 0D FD           SVEC    scale=03(*16)  bri=0     x=-1      y=-1      (-16.0000, -16.0000)
0906: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0908: 09 FD           SVEC    scale=03(*16)  bri=0     x=1       y=-1      (16.0000, -16.0000)
090A: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
090C: 0B F1           SVEC    scale=02(*8)   bri=0     x=3       y=1       (24.0000, 8.0000)
090E: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0910: 0A F5           SVEC    scale=02(*8)   bri=0     x=2       y=-1      (16.0000, -8.0000)
0912: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0914: 08 F9           SVEC    scale=03(*16)  bri=0     x=0       y=1       (0.0000, 16.0000)
0916: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0918: 09 F3           SVEC    scale=02(*8)   bri=0     x=1       y=3       (8.0000, 24.0000)
091A: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
091C: 0D F3           SVEC    scale=02(*8)   bri=0     x=-1      y=3       (-8.0000, 24.0000)
091E: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0920: 80 54 00 06     VEC     scale=05(/16)  bri=0     x=-512    y=-128    (-32.0000, -8.0000)
0924: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0926: 0F F1           SVEC    scale=02(*8)   bri=0     x=-3      y=1       (-24.0000, 8.0000)
0928: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
092A: 00 D0           RTS                         
;
; Shrapnel pattern 2  
092C: 00 30 80 07     VEC     scale=03(/64)  bri=0     x=-896    y=0       (-14.0000, 0.0000)
0930: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0932: 80 37 80 07     VEC     scale=03(/64)  bri=0     x=-896    y=-896    (-14.0000, -14.0000)
0936: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0938: 80 37 80 03     VEC     scale=03(/64)  bri=0     x=896     y=-896    (14.0000, -14.0000)
093C: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
093E: E0 40 A0 02     VEC     scale=04(/32)  bri=0     x=672     y=224     (21.0000, 7.0000)
0942: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0944: C0 35 80 03     VEC     scale=03(/64)  bri=0     x=896     y=-448    (14.0000, -7.0000)
0948: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
094A: 80 33 00 00     VEC     scale=03(/64)  bri=0     x=0       y=896     (0.0000, 14.0000)
094E: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0950: A0 42 E0 00     VEC     scale=04(/32)  bri=0     x=224     y=672     (7.0000, 21.0000)
0954: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0956: A0 42 E0 04     VEC     scale=04(/32)  bri=0     x=-224    y=672     (-7.0000, 21.0000)
095A: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
095C: E0 44 80 07     VEC     scale=04(/32)  bri=0     x=-896    y=-224    (-28.0000, -7.0000)
0960: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0962: E0 40 A0 06     VEC     scale=04(/32)  bri=0     x=-672    y=224     (-21.0000, 7.0000)
0966: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0968: 00 D0           RTS                         
;
; Shrapnel pattern 3
096A: 07 F8           SVEC    scale=01(*4)   bri=0     x=-3      y=0       (-12.0000, 0.0000)
096C: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
096E: 07 FF           SVEC    scale=01(*4)   bri=0     x=-3      y=-3      (-12.0000, -12.0000)
0970: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0972: 03 FF           SVEC    scale=01(*4)   bri=0     x=3       y=-3      (12.0000, -12.0000)
0974: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0976: C0 40 40 02     VEC     scale=04(/32)  bri=0     x=576     y=192     (18.0000, 6.0000)
097A: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
097C: 80 35 00 03     VEC     scale=03(/64)  bri=0     x=768     y=-384    (12.0000, -6.0000)
0980: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0982: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
0984: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0986: 40 42 C0 00     VEC     scale=04(/32)  bri=0     x=192     y=576     (6.0000, 18.0000)
098A: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
098C: 40 42 C0 04     VEC     scale=04(/32)  bri=0     x=-192    y=576     (-6.0000, 18.0000)
0990: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0992: C0 44 00 07     VEC     scale=04(/32)  bri=0     x=-768    y=-192    (-24.0000, -6.0000)
0996: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
0998: C0 40 40 06     VEC     scale=04(/32)  bri=0     x=-576    y=192     (-18.0000, 6.0000)
099C: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
099E: 00 D0           RTS                         
;
; Shrapnel pattern 4
09A0: 00 30 80 06     VEC     scale=03(/64)  bri=0     x=-640    y=0       (-10.0000, 0.0000)
09A4: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
09A6: 80 36 80 06     VEC     scale=03(/64)  bri=0     x=-640    y=-640    (-10.0000, -10.0000)
09AA: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
09AC: 80 36 80 02     VEC     scale=03(/64)  bri=0     x=640     y=-640    (10.0000, -10.0000)
09B0: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
09B2: 40 31 C0 03     VEC     scale=03(/64)  bri=0     x=960     y=320     (15.0000, 5.0000)
09B6: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
09B8: 40 35 80 02     VEC     scale=03(/64)  bri=0     x=640     y=-320    (10.0000, -5.0000)
09BC: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
09BE: 80 32 00 00     VEC     scale=03(/64)  bri=0     x=0       y=640     (0.0000, 10.0000)
09C2: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
09C4: C0 33 40 01     VEC     scale=03(/64)  bri=0     x=320     y=960     (5.0000, 15.0000)
09C8: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
09CA: C0 33 40 05     VEC     scale=03(/64)  bri=0     x=-320    y=960     (-5.0000, 15.0000)
09CE: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
09D0: A0 44 80 06     VEC     scale=04(/32)  bri=0     x=-640    y=-160    (-20.0000, -5.0000)
09D4: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
09D6: 40 31 C0 07     VEC     scale=03(/64)  bri=0     x=-960    y=320     (-15.0000, 5.0000)
09DA: 78 F8           SVEC    scale=03(*16)  bri=7     x=0       y=0       (0.0000, 0.0000)
09DC: 00 D0           RTS                         
```

# Rock Patterns 

```html
<canvas width="400" height="100"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="0800"
  data-command="baseScale=0,x=50,y=50,09E6,x=150,y=50,09FE,x=250,y=50,0A1A,x=350,y=50,0A34">
</canvas>
```

```code
; Jump table for 4  
09DE: F3 C8           JSR     $09E6               ; {}
09E0: FF C8           JSR     $09FE               ; {}
09E2: 0D C9           JSR     $0A1A               ; {}
09E4: 1A C9           JSR     $0A34               ; {}
;
; Rock Pattern 1
09E6: 08 F9           SVEC    scale=03(*16)  bri=0     x=0       y=1       (0.0000, 16.0000)
09E8: 79 F9           SVEC    scale=03(*16)  bri=7     x=1       y=1       (16.0000, 16.0000)
09EA: 79 FD           SVEC    scale=03(*16)  bri=7     x=1       y=-1      (16.0000, -16.0000)
09EC: 7D F6           SVEC    scale=02(*8)   bri=7     x=-1      y=-2      (-8.0000, -16.0000)
09EE: 79 F6           SVEC    scale=02(*8)   bri=7     x=1       y=-2      (8.0000, -16.0000)
09F0: 8F F6           SVEC    scale=02(*8)   bri=8     x=-3      y=-2      (-24.0000, -16.0000)
09F2: 8F F0           SVEC    scale=02(*8)   bri=8     x=-3      y=0       (-24.0000, 0.0000)
09F4: 7D F9           SVEC    scale=03(*16)  bri=7     x=-1      y=1       (-16.0000, 16.0000)
09F6: 78 FA           SVEC    scale=03(*16)  bri=7     x=0       y=2       (0.0000, 32.0000)
09F8: 79 F9           SVEC    scale=03(*16)  bri=7     x=1       y=1       (16.0000, 16.0000)
09FA: 79 FD           SVEC    scale=03(*16)  bri=7     x=1       y=-1      (16.0000, -16.0000)
09FC: 00 D0           RTS                         
;
; Rock Pattern 2
09FE: 0A F1           SVEC    scale=02(*8)   bri=0     x=2       y=1       (16.0000, 8.0000)
0A00: 7A F1           SVEC    scale=02(*8)   bri=7     x=2       y=1       (16.0000, 8.0000)
0A02: 7D F9           SVEC    scale=03(*16)  bri=7     x=-1      y=1       (-16.0000, 16.0000)
0A04: 7E F5           SVEC    scale=02(*8)   bri=7     x=-2      y=-1      (-16.0000, -8.0000)
0A06: 7E F1           SVEC    scale=02(*8)   bri=7     x=-2      y=1       (-16.0000, 8.0000)
0A08: 7D FD           SVEC    scale=03(*16)  bri=7     x=-1      y=-1      (-16.0000, -16.0000)
0A0A: 79 F6           SVEC    scale=02(*8)   bri=7     x=1       y=-2      (8.0000, -16.0000)
0A0C: 7D F6           SVEC    scale=02(*8)   bri=7     x=-1      y=-2      (-8.0000, -16.0000)
0A0E: 79 FD           SVEC    scale=03(*16)  bri=7     x=1       y=-1      (16.0000, -16.0000)
0A10: 79 F1           SVEC    scale=02(*8)   bri=7     x=1       y=1       (8.0000, 8.0000)
0A12: 8B F5           SVEC    scale=02(*8)   bri=8     x=3       y=-1      (24.0000, -8.0000)
0A14: 8A F3           SVEC    scale=02(*8)   bri=8     x=2       y=3       (16.0000, 24.0000)
0A16: 7D F9           SVEC    scale=03(*16)  bri=7     x=-1      y=1       (-16.0000, 16.0000)
0A18: 00 D0           RTS                         
;
; Rock Pattern 3  
0A1A: 0D F8           SVEC    scale=03(*16)  bri=0     x=-1      y=0       (-16.0000, 0.0000)
0A1C: 7E F5           SVEC    scale=02(*8)   bri=7     x=-2      y=-1      (-16.0000, -8.0000)
0A1E: 7A F7           SVEC    scale=02(*8)   bri=7     x=2       y=-3      (16.0000, -24.0000)
0A20: 7A F3           SVEC    scale=02(*8)   bri=7     x=2       y=3       (16.0000, 24.0000)
0A22: 78 F7           SVEC    scale=02(*8)   bri=7     x=0       y=-3      (0.0000, -24.0000)
0A24: 79 F8           SVEC    scale=03(*16)  bri=7     x=1       y=0       (16.0000, 0.0000)
0A26: 7A F3           SVEC    scale=02(*8)   bri=7     x=2       y=3       (16.0000, 24.0000)
0A28: 78 F9           SVEC    scale=03(*16)  bri=7     x=0       y=1       (0.0000, 16.0000)
0A2A: 7E F3           SVEC    scale=02(*8)   bri=7     x=-2      y=3       (-16.0000, 24.0000)
0A2C: 7F F0           SVEC    scale=02(*8)   bri=7     x=-3      y=0       (-24.0000, 0.0000)
0A2E: 7F F7           SVEC    scale=02(*8)   bri=7     x=-3      y=-3      (-24.0000, -24.0000)
0A30: 7A F5           SVEC    scale=02(*8)   bri=7     x=2       y=-1      (16.0000, -8.0000)
0A32: 00 D0           RTS                         
;
; Rock Pattern 4
0A34: 09 F0           SVEC    scale=02(*8)   bri=0     x=1       y=0       (8.0000, 0.0000)
0A36: 7B F1           SVEC    scale=02(*8)   bri=7     x=3       y=1       (24.0000, 8.0000)
0A38: 68 F1           SVEC    scale=02(*8)   bri=6     x=0       y=1       (0.0000, 8.0000)
0A3A: 7F F2           SVEC    scale=02(*8)   bri=7     x=-3      y=2       (-24.0000, 16.0000)
0A3C: 7F F0           SVEC    scale=02(*8)   bri=7     x=-3      y=0       (-24.0000, 0.0000)
0A3E: 69 F6           SVEC    scale=02(*8)   bri=6     x=1       y=-2      (8.0000, -16.0000)
0A40: 7F F0           SVEC    scale=02(*8)   bri=7     x=-3      y=0       (-24.0000, 0.0000)
0A42: 78 F7           SVEC    scale=02(*8)   bri=7     x=0       y=-3      (0.0000, -24.0000)
0A44: 7A F7           SVEC    scale=02(*8)   bri=7     x=2       y=-3      (16.0000, -24.0000)
0A46: 7B F1           SVEC    scale=02(*8)   bri=7     x=3       y=1       (24.0000, 8.0000)
0A48: 69 F5           SVEC    scale=02(*8)   bri=6     x=1       y=-1      (8.0000, -8.0000)
0A4A: 69 F9           SVEC    scale=03(*16)  bri=6     x=1       y=1       (16.0000, 16.0000)
0A4C: 7F F2           SVEC    scale=02(*8)   bri=7     x=-3      y=2       (-24.0000, 16.0000)
0A4E: 00 D0           RTS                         
```

# UFO 

```html
<canvas width="100" height="75"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="0800"
  data-command="x=50,y=40,baseScale=0,0A52">
</canvas>
```

```code
; Jump table for 1
0A50: 29 C9           JSR     $0A52               ; {}
;
0A52: 0E F1           SVEC    scale=02(*8)   bri=0     x=-2      y=1       (-16.0000, 8.0000)
0A54: CA F8           SVEC    scale=03(*16)  bri=12    x=2       y=0       (32.0000, 0.0000)
0A56: 0B F6           SVEC    scale=02(*8)   bri=0     x=3       y=-2      (24.0000, -16.0000)
0A58: 00 60 80 D6     VEC     scale=06(/8)   bri=13    x=-640    y=0       (-80.0000, 0.0000)
0A5C: DB F6           SVEC    scale=02(*8)   bri=13    x=3       y=-2      (24.0000, -16.0000)
0A5E: CA F8           SVEC    scale=03(*16)  bri=12    x=2       y=0       (32.0000, 0.0000)
0A60: DB F2           SVEC    scale=02(*8)   bri=13    x=3       y=2       (24.0000, 16.0000)
0A62: DF F2           SVEC    scale=02(*8)   bri=13    x=-3      y=2       (-24.0000, 16.0000)
0A64: CD F2           SVEC    scale=02(*8)   bri=12    x=-1      y=2       (-8.0000, 16.0000)
0A66: CD F8           SVEC    scale=03(*16)  bri=12    x=-1      y=0       (-16.0000, 0.0000)
0A68: CD F6           SVEC    scale=02(*8)   bri=12    x=-1      y=-2      (-8.0000, -16.0000)
0A6A: DF F6           SVEC    scale=02(*8)   bri=13    x=-3      y=-2      (-24.0000, -16.0000)
0A6C: 00 D0           RTS                         
```

# Player Ships 

```code
; Table for ships and thrusts based on player's direction.
; The addresses are where the ROM appears in the main CPU's
; memory map (begins at 5000). Thus 5292 - 5000 + 0800 = 0A92.
; The thrust pattern for each ship follows the ship itself.
;
0A6E: 90 52 ; [ShipDir0](#ShipDir0)
0A70: A8 52 ; [ShipDir4](#ShipDir4)
0A72: CC 52 ; [ShipDir8](#ShipDir8)
0A74: F0 52 ; [ShipDir12](#ShipDir12)
0A76: 14 53 ; [ShipDir16](#ShipDir16)
0A78: 36 53 ; [ShipDir20](#ShipDir20)
0A7A: 5A 53 ; [ShipDir24](#ShipDir24)
0A7C: 7E 53 ; [ShipDir28](#ShipDir28)
0A7E: A2 53 ; [ShipDir32](#ShipDir32)
0A80: C6 53 ; [ShipDir36](#ShipDir36)
0A82: EA 53 ; [ShipDir40](#ShipDir40)
0A84: 0E 54 ; [ShipDir44](#ShipDir44)
0A86: 32 54 ; [ShipDir48](#ShipDir48)
0A88: 56 54 ; [ShipDir52](#ShipDir52)
0A8A: 7A 54 ; [ShipDir56](#ShipDir56)
0A8C: 9E 54 ; [ShipDir60](#ShipDir60)
0A8E: C2 54 ; [ShipDir64](#ShipDir64)
```

```html
<canvas width="1060" height="100"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="0800"
  data-command="baseScale=-1,
    x=50,y=50,A90,AA2,    
    x=110,y=50,0AA8,
    x=170,y=50,0ACC,
    x=230,y=50,0AF0,
    x=290,y=50,0B14,
    x=350,y=50,0B36,
    x=410,y=50,0B5A,
    x=470,y=50,0B7E,
    x=530,y=50,0BA2,
    x=590,y=50,0BC6,
    x=650,y=50,0BEA,
    x=710,y=50,0C0E,
    x=770,y=50,0C32,
    x=830,y=50,0C56,
    x=890,y=50,0C7A,
    x=950,y=50,0C9E,
    x=1010,y=50,0CC2,0CD4
  ">
</canvas>
```

```code
ShipDir0:
0A90: 0F F6           SVEC    scale=02(*8)   bri=0     x=-3      y=-2      (-24.0000, -16.0000)
0A92: C8 FA           SVEC    scale=03(*16)  bri=12    x=0       y=2       (0.0000, 32.0000)
0A94: BD F9           SVEC    scale=03(*16)  bri=11    x=-1      y=1       (-16.0000, 16.0000)
0A96: 00 65 00 C3     VEC     scale=06(/8)   bri=12    x=768     y=-256    (96.0000, -32.0000)
0A9A: 00 65 00 C7     VEC     scale=06(/8)   bri=12    x=-768    y=-256    (-96.0000, -32.0000)
0A9E: B9 F9           SVEC    scale=03(*16)  bri=11    x=1       y=1       (16.0000, 16.0000)
0AA0: 00 D0           RTS                         
ThrustDir0:  
0AA2: CE F9           SVEC    scale=03(*16)  bri=12    x=-2      y=1       (-32.0000, 16.0000)
0AA4: CA F9           SVEC    scale=03(*16)  bri=12    x=2       y=1       (32.0000, 16.0000)
0AA6: 00 D0           RTS                         

ShipDir4:
0AA8: 40 46 C0 06     VEC     scale=04(/32)  bri=0     x=-704    y=-576    (-22.0000, -18.0000)
0AAC: 00 52 30 C4     VEC     scale=05(/16)  bri=12    x=-48     y=512     (-3.0000, 32.0000)
0AB0: C0 41 20 C6     VEC     scale=04(/32)  bri=12    x=-544    y=448     (-17.0000, 14.0000)
0AB4: B0 64 18 C3     VEC     scale=06(/8)   bri=12    x=792     y=-176    (99.0000, -22.0000)
0AB8: 48 65 E0 C6     VEC     scale=06(/8)   bri=12    x=-736    y=-328    (-92.0000, -41.0000)
0ABC: 20 42 C0 C1     VEC     scale=04(/32)  bri=12    x=448     y=544     (14.0000, 17.0000)
0AC0: 00 D0           RTS                         
ThrustDir4:  
0AC2: D0 50 10 C6     VEC     scale=05(/16)  bri=12    x=-528    y=208     (-33.0000, 13.0000)
0AC6: 60 42 C0 C3     VEC     scale=04(/32)  bri=12    x=960     y=608     (30.0000, 19.0000)
0ACA: 00 D0           RTS                         

ShipDir8:  
0ACC: 80 46 80 06     VEC     scale=04(/32)  bri=0     x=-640    y=-640    (-20.0000, -20.0000)
0AD0: E0 43 C0 C4     VEC     scale=04(/32)  bri=12    x=-192    y=992     (-6.0000, 31.0000)
0AD4: A0 41 60 C6     VEC     scale=04(/32)  bri=12    x=-608    y=416     (-19.0000, 13.0000)
0AD8: 68 64 20 C3     VEC     scale=06(/8)   bri=12    x=800     y=-104    (100.0000, -13.0000)
0ADC: 90 65 C0 C6     VEC     scale=06(/8)   bri=12    x=-704    y=-400    (-88.0000, -50.0000)
0AE0: 60 42 A0 C1     VEC     scale=04(/32)  bri=12    x=416     y=608     (13.0000, 19.0000)
0AE4: 00 D0           RTS                         
ThrustDir8:
0AE6: 90 50 30 C6     VEC     scale=05(/16)  bri=12    x=-560    y=144     (-35.0000, 9.0000)
0AEA: C0 42 80 C3     VEC     scale=04(/32)  bri=12    x=896     y=704     (28.0000, 22.0000)
0AEE: 00 D0           RTS                         

ShipDir12:
0AF0: C0 46 40 06     VEC     scale=04(/32)  bri=0     x=-576    y=-704    (-18.0000, -22.0000)
0AF4: E0 43 20 C5     VEC     scale=04(/32)  bri=12    x=-288    y=992     (-9.0000, 31.0000)
0AF8: 60 41 80 C6     VEC     scale=04(/32)  bri=12    x=-640    y=352     (-20.0000, 11.0000)
0AFC: 18 64 28 C3     VEC     scale=06(/8)   bri=12    x=808     y=-24     (101.0000, -3.0000)
0B00: D0 65 98 C6     VEC     scale=06(/8)   bri=12    x=-664    y=-464    (-83.0000, -58.0000)
0B04: 80 42 60 C1     VEC     scale=04(/32)  bri=12    x=352     y=640     (11.0000, 20.0000)
0B08: 00 D0           RTS                         
ThrustDir12:
0B0A: 60 50 30 C6     VEC     scale=05(/16)  bri=12    x=-560    y=96      (-35.0000, 6.0000)
0B0E: 20 43 40 C3     VEC     scale=04(/32)  bri=12    x=832     y=800     (26.0000, 25.0000)
0B12: 00 D0           RTS                         

ShipDir16:
0B14: 0E F7           SVEC    scale=02(*8)   bri=0     x=-2      y=-3      (-16.0000, -24.0000)
0B16: C0 43 80 C5     VEC     scale=04(/32)  bri=12    x=-384    y=960     (-12.0000, 30.0000)
0B1A: 20 41 A0 C6     VEC     scale=04(/32)  bri=12    x=-672    y=288     (-21.0000, 9.0000)
0B1E: 38 60 28 C3     VEC     scale=06(/8)   bri=12    x=808     y=56      (101.0000, 7.0000)
0B22: 10 66 60 C6     VEC     scale=06(/8)   bri=12    x=-608    y=-528    (-76.0000, -66.0000)
0B26: A0 42 20 C1     VEC     scale=04(/32)  bri=12    x=288     y=672     (9.0000, 21.0000)
0B2A: 00 D0           RTS                         
ThrustDir16:
0B2C: 30 50 40 C6     VEC     scale=05(/16)  bri=12    x=-576    y=48      (-36.0000, 3.0000)
0B30: 60 43 E0 C2     VEC     scale=04(/32)  bri=12    x=736     y=864     (23.0000, 27.0000)
0B34: 00 D0           RTS                         

ShipDir20:  
0B36: 20 47 C0 05     VEC     scale=04(/32)  bri=0     x=-448    y=-800    (-14.0000, -25.0000)
0B3A: 80 43 E0 C5     VEC     scale=04(/32)  bri=12    x=-480    y=896     (-15.0000, 28.0000)
0B3E: E0 40 C0 C6     VEC     scale=04(/32)  bri=12    x=-704    y=224     (-22.0000, 7.0000)
0B42: 88 60 20 C3     VEC     scale=06(/8)   bri=12    x=800     y=136     (100.0000, 17.0000)
0B46: 48 66 30 C6     VEC     scale=06(/8)   bri=12    x=-560    y=-584    (-70.0000, -73.0000)
0B4A: C0 42 E0 C0     VEC     scale=04(/32)  bri=12    x=224     y=704     (7.0000, 22.0000)
0B4E: 00 D0           RTS                         
ThrustDir20:
0B50: 10 54 40 C6     VEC     scale=05(/16)  bri=12    x=-576    y=-16     (-36.0000, -1.0000)
0B54: A0 43 A0 C2     VEC     scale=04(/32)  bri=12    x=672     y=928     (21.0000, 29.0000)
0B58: 00 D0           RTS                         

ShipDir24:  
0B5A: 60 47 60 05     VEC     scale=04(/32)  bri=0     x=-352    y=-864    (-11.0000, -27.0000)
0B5E: 60 43 40 C6     VEC     scale=04(/32)  bri=12    x=-576    y=864     (-18.0000, 27.0000)
0B62: 80 40 C0 C6     VEC     scale=04(/32)  bri=12    x=-704    y=128     (-22.0000, 4.0000)
0B66: D8 60 10 C3     VEC     scale=06(/8)   bri=12    x=784     y=216     (98.0000, 27.0000)
0B6A: 80 66 F0 C5     VEC     scale=06(/8)   bri=12    x=-496    y=-640    (-62.0000, -80.0000)
0B6E: C0 42 80 C0     VEC     scale=04(/32)  bri=12    x=128     y=704     (4.0000, 22.0000)
0B72: 00 D0           RTS                         
ThrustDir24:
0B74: 40 54 30 C6     VEC     scale=05(/16)  bri=12    x=-560    y=-64     (-35.0000, -4.0000)
0B78: E0 43 40 C2     VEC     scale=04(/32)  bri=12    x=576     y=992     (18.0000, 31.0000)
0B7C: 00 D0           RTS                         

ShipDir28:  
0B7E: 80 47 00 05     VEC     scale=04(/32)  bri=0     x=-256    y=-896    (-8.0000, -28.0000)
0B82: 20 43 80 C6     VEC     scale=04(/32)  bri=12    x=-640    y=800     (-20.0000, 25.0000)
0B86: 40 40 E0 C6     VEC     scale=04(/32)  bri=12    x=-736    y=64      (-23.0000, 2.0000)
0B8A: 20 61 F8 C2     VEC     scale=06(/8)   bri=12    x=760     y=288     (95.0000, 36.0000)
0B8E: B0 66 B0 C5     VEC     scale=06(/8)   bri=12    x=-432    y=-688    (-54.0000, -86.0000)
0B92: E0 42 40 C0     VEC     scale=04(/32)  bri=12    x=64      y=736     (2.0000, 23.0000)
0B96: 00 D0           RTS                         
ThrustDir28:
0B98: 80 54 30 C6     VEC     scale=05(/16)  bri=12    x=-560    y=-128    (-35.0000, -8.0000)
0B9C: 10 52 F0 C0     VEC     scale=05(/16)  bri=12    x=240     y=528     (15.0000, 33.0000)
0BA0: 00 D0           RTS                         

ShipDir32:  
0BA2: 80 47 C0 04     VEC     scale=04(/32)  bri=0     x=-192    y=-896    (-6.0000, -28.0000)
0BA6: E0 42 E0 C6     VEC     scale=04(/32)  bri=12    x=-736    y=736     (-23.0000, 23.0000)
0BAA: 00 40 E0 C6     VEC     scale=04(/32)  bri=12    x=-736    y=0       (-23.0000, 0.0000)
0BAE: 68 61 D8 C2     VEC     scale=06(/8)   bri=12    x=728     y=360     (91.0000, 45.0000)
0BB2: D8 66 68 C5     VEC     scale=06(/8)   bri=12    x=-360    y=-728    (-45.0000, -91.0000)
0BB6: E0 42 00 C0     VEC     scale=04(/32)  bri=12    x=0       y=736     (0.0000, 23.0000)
0BBA: 00 D0           RTS                         
ThrustDir32:
0BBC: B0 54 20 C6     VEC     scale=05(/16)  bri=12    x=-544    y=-176    (-34.0000, -11.0000)
0BC0: 20 52 B0 C0     VEC     scale=05(/16)  bri=12    x=176     y=544     (11.0000, 34.0000)
0BC4: 00 D0           RTS                         

ShipDir36:  
0BC6: A0 47 60 04     VEC     scale=04(/32)  bri=0     x=-96     y=-928    (-3.0000, -29.0000)
0BCA: 80 42 20 C7     VEC     scale=04(/32)  bri=12    x=-800    y=640     (-25.0000, 20.0000)
0BCE: 40 44 E0 C6     VEC     scale=04(/32)  bri=12    x=-736    y=-64     (-23.0000, -2.0000)
0BD2: B0 61 B0 C2     VEC     scale=06(/8)   bri=12    x=688     y=432     (86.0000, 54.0000)
0BD6: F8 66 20 C5     VEC     scale=06(/8)   bri=12    x=-288    y=-760    (-36.0000, -95.0000)
0BDA: E0 42 40 C4     VEC     scale=04(/32)  bri=12    x=-64     y=736     (-2.0000, 23.0000)
0BDE: 00 D0           RTS                         
ThrustDir36:
0BE0: F0 54 10 C6     VEC     scale=05(/16)  bri=12    x=-528    y=-240    (-33.0000, -15.0000)
0BE4: 30 52 80 C0     VEC     scale=05(/16)  bri=12    x=128     y=560     (8.0000, 35.0000)
0BE8: 00 D0           RTS                         

ShipDir40:  
0BEA: A0 47 00 00     VEC     scale=04(/32)  bri=0     x=0       y=-928    (0.0000, -29.0000)
0BEE: 40 42 60 C7     VEC     scale=04(/32)  bri=12    x=-864    y=576     (-27.0000, 18.0000)
0BF2: 80 44 C0 C6     VEC     scale=04(/32)  bri=12    x=-704    y=-128    (-22.0000, -4.0000)
0BF6: F0 61 80 C2     VEC     scale=06(/8)   bri=12    x=640     y=496     (80.0000, 62.0000)
0BFA: 10 67 D8 C4     VEC     scale=06(/8)   bri=12    x=-216    y=-784    (-27.0000, -98.0000)
0BFE: C0 42 80 C4     VEC     scale=04(/32)  bri=12    x=-128    y=704     (-4.0000, 22.0000)
0C02: 00 D0           RTS                         
ThrustDir40:
0C04: 40 46 E0 C7     VEC     scale=04(/32)  bri=12    x=-992    y=-576    (-31.0000, -18.0000)
0C08: 30 52 40 C0     VEC     scale=05(/16)  bri=12    x=64      y=560     (4.0000, 35.0000)
0C0C: 00 D0           RTS                         

ShipDir44: 
0C0E: A0 47 60 00     VEC     scale=04(/32)  bri=0     x=96      y=-928    (3.0000, -29.0000)
0C12: E0 41 80 C7     VEC     scale=04(/32)  bri=12    x=-896    y=480     (-28.0000, 15.0000)
0C16: E0 44 C0 C6     VEC     scale=04(/32)  bri=12    x=-704    y=-224    (-22.0000, -7.0000)
0C1A: 30 62 48 C2     VEC     scale=06(/8)   bri=12    x=584     y=560     (73.0000, 70.0000)
0C1E: 20 67 88 C4     VEC     scale=06(/8)   bri=12    x=-136    y=-800    (-17.0000, -100.0000)
0C22: C0 42 E0 C4     VEC     scale=04(/32)  bri=12    x=-224    y=704     (-7.0000, 22.0000)
0C26: 00 D0           RTS                         
ThrustDir44:
0C28: A0 46 A0 C7     VEC     scale=04(/32)  bri=12    x=-928    y=-672    (-29.0000, -21.0000)
0C2C: 40 52 10 C0     VEC     scale=05(/16)  bri=12    x=16      y=576     (1.0000, 36.0000)
0C30: 00 D0           RTS                         

ShipDir48:  
0C32: 80 47 C0 00     VEC     scale=04(/32)  bri=0     x=192     y=-896    (6.0000, -28.0000)
0C36: 80 41 C0 C7     VEC     scale=04(/32)  bri=12    x=-960    y=384     (-30.0000, 12.0000)
0C3A: 20 45 A0 C6     VEC     scale=04(/32)  bri=12    x=-672    y=-288    (-21.0000, -9.0000)
0C3E: 60 62 10 C2     VEC     scale=06(/8)   bri=12    x=528     y=608     (66.0000, 76.0000)
0C42: 28 67 38 C4     VEC     scale=06(/8)   bri=12    x=-56     y=-808    (-7.0000, -101.0000)
0C46: A0 42 20 C5     VEC     scale=04(/32)  bri=12    x=-288    y=672     (-9.0000, 21.0000)
0C4A: 00 D0           RTS                         
ThrustDir48:
0C4C: E0 46 60 C7     VEC     scale=04(/32)  bri=12    x=-864    y=-736    (-27.0000, -23.0000)
0C50: 40 52 30 C4     VEC     scale=05(/16)  bri=12    x=-48     y=576     (-3.0000, 36.0000)
0C54: 00 D0           RTS                         

ShipDir52:
0C56: 80 47 00 01     VEC     scale=04(/32)  bri=0     x=256     y=-896    (8.0000, -28.0000)
0C5A: 20 41 E0 C7     VEC     scale=04(/32)  bri=12    x=-992    y=288     (-31.0000, 9.0000)
0C5E: 60 45 80 C6     VEC     scale=04(/32)  bri=12    x=-640    y=-352    (-20.0000, -11.0000)
0C62: 98 62 D0 C1     VEC     scale=06(/8)   bri=12    x=464     y=664     (58.0000, 83.0000)
0C66: 28 67 18 C0     VEC     scale=06(/8)   bri=12    x=24      y=-808    (3.0000, -101.0000)
0C6A: 80 42 60 C5     VEC     scale=04(/32)  bri=12    x=-352    y=640     (-11.0000, 20.0000)
0C6E: 00 D0           RTS                         
ThrustDir52:
0C70: 40 47 20 C7     VEC     scale=04(/32)  bri=12    x=-800    y=-832    (-25.0000, -26.0000)
0C74: 30 52 60 C4     VEC     scale=05(/16)  bri=12    x=-96     y=560     (-6.0000, 35.0000)
0C78: 00 D0           RTS                         

ShipDir56:
0C7A: 60 47 60 01     VEC     scale=04(/32)  bri=0     x=352     y=-864    (11.0000, -27.0000)
0C7E: C0 40 E0 C7     VEC     scale=04(/32)  bri=12    x=-992    y=192     (-31.0000, 6.0000)
0C82: A0 45 60 C6     VEC     scale=04(/32)  bri=12    x=-608    y=-416    (-19.0000, -13.0000)
0C86: C0 62 90 C1     VEC     scale=06(/8)   bri=12    x=400     y=704     (50.0000, 88.0000)
0C8A: 20 67 68 C0     VEC     scale=06(/8)   bri=12    x=104     y=-800    (13.0000, -100.0000)
0C8E: 60 42 A0 C5     VEC     scale=04(/32)  bri=12    x=-416    y=608     (-13.0000, 19.0000)
0C92: 00 D0           RTS                         
ThrustDir56:
0C94: 80 47 C0 C6     VEC     scale=04(/32)  bri=12    x=-704    y=-896    (-22.0000, -28.0000)
0C98: 30 52 90 C4     VEC     scale=05(/16)  bri=12    x=-144    y=560     (-9.0000, 35.0000)
0C9C: 00 D0           RTS                         

ShipDir60:  
0C9E: 20 47 C0 01     VEC     scale=04(/32)  bri=0     x=448     y=-800    (14.0000, -25.0000)
0CA2: 30 50 00 C6     VEC     scale=05(/16)  bri=12    x=-512    y=48      (-32.0000, 3.0000)
0CA6: C0 45 20 C6     VEC     scale=04(/32)  bri=12    x=-544    y=-448    (-17.0000, -14.0000)
0CAA: E0 62 48 C1     VEC     scale=06(/8)   bri=12    x=328     y=736     (41.0000, 92.0000)
0CAE: 18 67 B0 C0     VEC     scale=06(/8)   bri=12    x=176     y=-792    (22.0000, -99.0000)
0CB2: 20 42 C0 C5     VEC     scale=04(/32)  bri=12    x=-448    y=544     (-14.0000, 17.0000)
0CB6: 00 D0           RTS                         
ThrustDir60:
0CB8: C0 47 60 C6     VEC     scale=04(/32)  bri=12    x=-608    y=-960    (-19.0000, -30.0000)
0CBC: 10 52 D0 C4     VEC     scale=05(/16)  bri=12    x=-208    y=528     (-13.0000, 33.0000)
0CC0: 00 D0           RTS                         

ShipDir64:
0CC2: 0A F7           SVEC    scale=02(*8)   bri=0     x=2       y=-3      (16.0000, -24.0000)
0CC4: CE F8           SVEC    scale=03(*16)  bri=12    x=-2      y=0       (-32.0000, 0.0000)
0CC6: CD FD           SVEC    scale=03(*16)  bri=12    x=-1      y=-1      (-16.0000, -16.0000)
0CC8: 00 63 00 C1     VEC     scale=06(/8)   bri=12    x=256     y=768     (32.0000, 96.0000)
0CCC: 00 67 00 C1     VEC     scale=06(/8)   bri=12    x=256     y=-768    (32.0000, -96.0000)
0CD0: CD F9           SVEC    scale=03(*16)  bri=12    x=-1      y=1       (-16.0000, 16.0000)
ThrustDir64:
0CD2: 00 D0           RTS                         
0CD4: CD FE           SVEC    scale=03(*16)  bri=12    x=-1      y=-2      (-16.0000, -32.0000)
0CD6: CD FA           SVEC    scale=03(*16)  bri=12    x=-1      y=2       (-16.0000, 32.0000)
0CD8: 00 D0           RTS                         
```

# Lives 

 Ships in reserve. These are defined so you can draw them one right after the other (three drawn here).

```html
<canvas width="200" height="100"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="0800"
  data-command="x=50,y=50,baseScale=-1,0CDA,0CDA,0CDA">
</canvas>
```

```code  
0CDA: 0E F7           SVEC    scale=02(*8)   bri=0     x=-2      y=-3      (-16.0000, -24.0000)
0CDC: 7A F8           SVEC    scale=03(*16)  bri=7     x=2       y=0       (32.0000, 0.0000)
0CDE: 79 FD           SVEC    scale=03(*16)  bri=7     x=1       y=-1      (16.0000, -16.0000)
0CE0: 00 63 00 75     VEC     scale=06(/8)   bri=7     x=-256    y=768     (-32.0000, 96.0000)
0CE4: 00 67 00 75     VEC     scale=06(/8)   bri=7     x=-256    y=-768    (-32.0000, -96.0000)
0CE8: 79 F9           SVEC    scale=03(*16)  bri=7     x=1       y=1       (16.0000, 16.0000)
0CEA: C0 60 80 02     VEC     scale=06(/8)   bri=0     x=640     y=192     (80.0000, 24.0000)
0CEE: 9F D0           RTS                         
```

# Characters 

```html
<canvas width="500" height="120"
  data-canvasFunction="DVG.handleDVGCanvas"
  data-origin="0800"
  data-command="x=30,y=45,baseScale=1,0CF0,0D00,0D1A,0D26,0D36,0D46,0D54,0D66,0D74,0D82,0D8E,0D9A,0DA4,0DB0,0DBA,0DC6,0DD4,0DE6,x=30,y=90,0DF6,0E04,0E10,0E1C,0E26,0E34,0E3E,0E4C,0E58,0E5C,0E64,0E74,0E82,0E90,0E9E,0EAC,0EB6,0EC6">
</canvas>
```

```code
; "A"
0CF0: 70 FA           SVEC    scale=01(*4)   bri=7     x=0       y=2       (0.0000, 8.0000)
0CF2: 72 F2           SVEC    scale=00(*2)   bri=7     x=2       y=2       (4.0000, 4.0000)
0CF4: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
0CF6: 70 FE           SVEC    scale=01(*4)   bri=7     x=0       y=-2      (0.0000, -8.0000)
0CF8: 06 F9           SVEC    scale=01(*4)   bri=0     x=-2      y=1       (-8.0000, 4.0000)
0CFA: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0CFC: 02 F6           SVEC    scale=00(*2)   bri=0     x=2       y=-2      (4.0000, -4.0000)
0CFE: 00 D0           RTS                         

; "B"
0D00: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0D02: 73 F0           SVEC    scale=00(*2)   bri=7     x=3       y=0       (6.0000, 0.0000)
0D04: 71 F5           SVEC    scale=00(*2)   bri=7     x=1       y=-1      (2.0000, -2.0000)
0D06: 70 F5           SVEC    scale=00(*2)   bri=7     x=0       y=-1      (0.0000, -2.0000)
0D08: 75 F5           SVEC    scale=00(*2)   bri=7     x=-1      y=-1      (-2.0000, -2.0000)
0D0A: 77 F0           SVEC    scale=00(*2)   bri=7     x=-3      y=0       (-6.0000, 0.0000)
0D0C: 03 F0           SVEC    scale=00(*2)   bri=0     x=3       y=0       (6.0000, 0.0000)
0D0E: 71 F5           SVEC    scale=00(*2)   bri=7     x=1       y=-1      (2.0000, -2.0000)
0D10: 70 F5           SVEC    scale=00(*2)   bri=7     x=0       y=-1      (0.0000, -2.0000)
0D12: 75 F5           SVEC    scale=00(*2)   bri=7     x=-1      y=-1      (-2.0000, -2.0000)
0D14: 77 F0           SVEC    scale=00(*2)   bri=7     x=-3      y=0       (-6.0000, 0.0000)
0D16: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
0D18: 00 D0           RTS                         

; "C"
0D1A: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0D1C: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0D1E: 06 FF           SVEC    scale=01(*4)   bri=0     x=-2      y=-3      (-8.0000, -12.0000)
0D20: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0D22: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0D24: 00 D0           RTS                         
  
; "D"
0D26: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0D28: 72 F0           SVEC    scale=00(*2)   bri=7     x=2       y=0       (4.0000, 0.0000)
0D2A: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
0D2C: 70 F6           SVEC    scale=00(*2)   bri=7     x=0       y=-2      (0.0000, -4.0000)
0D2E: 76 F6           SVEC    scale=00(*2)   bri=7     x=-2      y=-2      (-4.0000, -4.0000)
0D30: 76 F0           SVEC    scale=00(*2)   bri=7     x=-2      y=0       (-4.0000, 0.0000)
0D32: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
0D34: 00 D0           RTS                         

; "E"
0D36: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0D38: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0D3A: 05 F7           SVEC    scale=00(*2)   bri=0     x=-1      y=-3      (-2.0000, -6.0000)
0D3C: 77 F0           SVEC    scale=00(*2)   bri=7     x=-3      y=0       (-6.0000, 0.0000)
0D3E: 00 F7           SVEC    scale=00(*2)   bri=0     x=0       y=-3      (0.0000, -6.0000)
0D40: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0D42: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0D44: 00 D0           RTS                         

; "F"
0D46: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0D48: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0D4A: 05 F7           SVEC    scale=00(*2)   bri=0     x=-1      y=-3      (-2.0000, -6.0000)
0D4C: 77 F0           SVEC    scale=00(*2)   bri=7     x=-3      y=0       (-6.0000, 0.0000)
0D4E: 00 F7           SVEC    scale=00(*2)   bri=0     x=0       y=-3      (0.0000, -6.0000)
0D50: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
0D52: 00 D0           RTS                         

; "G"
0D54: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0D56: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0D58: 70 F6           SVEC    scale=00(*2)   bri=7     x=0       y=-2      (0.0000, -4.0000)
0D5A: 06 F6           SVEC    scale=00(*2)   bri=0     x=-2      y=-2      (-4.0000, -4.0000)
0D5C: 72 F0           SVEC    scale=00(*2)   bri=7     x=2       y=0       (4.0000, 0.0000)
0D5E: 70 F6           SVEC    scale=00(*2)   bri=7     x=0       y=-2      (0.0000, -4.0000)
0D60: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0D62: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
0D64: 00 D0           RTS                         

; "H"  
0D66: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0D68: 00 F7           SVEC    scale=00(*2)   bri=0     x=0       y=-3      (0.0000, -6.0000)
0D6A: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0D6C: 00 F3           SVEC    scale=00(*2)   bri=0     x=0       y=3       (0.0000, 6.0000)
0D6E: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
0D70: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0D72: 00 D0           RTS                         

; "I"  
0D74: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0D76: 06 F0           SVEC    scale=00(*2)   bri=0     x=-2      y=0       (-4.0000, 0.0000)
0D78: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0D7A: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0D7C: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0D7E: 03 FF           SVEC    scale=01(*4)   bri=0     x=3       y=-3      (12.0000, -12.0000)
0D80: 00 D0           RTS                         

; "J"
0D82: 00 F2           SVEC    scale=00(*2)   bri=0     x=0       y=2       (0.0000, 4.0000)
0D84: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
0D86: 72 F0           SVEC    scale=00(*2)   bri=7     x=2       y=0       (4.0000, 0.0000)
0D88: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0D8A: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
0D8C: 00 D0           RTS                         

; "K"  
0D8E: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0D90: 03 F0           SVEC    scale=00(*2)   bri=0     x=3       y=0       (6.0000, 0.0000)
0D92: 77 F7           SVEC    scale=00(*2)   bri=7     x=-3      y=-3      (-6.0000, -6.0000)
0D94: 73 F7           SVEC    scale=00(*2)   bri=7     x=3       y=-3      (6.0000, -6.0000)
0D96: 03 F0           SVEC    scale=00(*2)   bri=0     x=3       y=0       (6.0000, 0.0000)
0D98: 00 D0           RTS                         

; "L"  
0D9A: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
0D9C: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
0D9E: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0DA0: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0DA2: 00 D0           RTS                         

; "M"
0DA4: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0DA6: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
0DA8: 72 F2           SVEC    scale=00(*2)   bri=7     x=2       y=2       (4.0000, 4.0000)
0DAA: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
0DAC: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0DAE: 00 D0           RTS                         

; "N"  
0DB0: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0DB2: 72 FF           SVEC    scale=01(*4)   bri=7     x=2       y=-3      (8.0000, -12.0000)
0DB4: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0DB6: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
0DB8: 00 D0           RTS                         

; "O"  
0DBA: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0DBC: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0DBE: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
0DC0: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0DC2: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
0DC4: 00 D0           RTS                         

; "P"
0DC6: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0DC8: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0DCA: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
0DCC: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0DCE: 03 F7           SVEC    scale=00(*2)   bri=0     x=3       y=-3      (6.0000, -6.0000)
0DD0: 03 F0           SVEC    scale=00(*2)   bri=0     x=3       y=0       (6.0000, 0.0000)
0DD2: 00 D0           RTS                         

; "Q"  
0DD4: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0DD6: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0DD8: 70 FE           SVEC    scale=01(*4)   bri=7     x=0       y=-2      (0.0000, -8.0000)
0DDA: 76 F6           SVEC    scale=00(*2)   bri=7     x=-2      y=-2      (-4.0000, -4.0000)
0DDC: 76 F0           SVEC    scale=00(*2)   bri=7     x=-2      y=0       (-4.0000, 0.0000)
0DDE: 02 F2           SVEC    scale=00(*2)   bri=0     x=2       y=2       (4.0000, 4.0000)
0DE0: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
0DE2: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0DE4: 00 D0           RTS                         

; "R"
0DE6: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0DE8: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0DEA: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
0DEC: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0DEE: 01 F0           SVEC    scale=00(*2)   bri=0     x=1       y=0       (2.0000, 0.0000)
0DF0: 73 F7           SVEC    scale=00(*2)   bri=7     x=3       y=-3      (6.0000, -6.0000)
0DF2: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0DF4: 00 D0           RTS                         

; "S"
0DF6: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0DF8: 70 F3           SVEC    scale=00(*2)   bri=7     x=0       y=3       (0.0000, 6.0000)
0DFA: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0DFC: 70 F3           SVEC    scale=00(*2)   bri=7     x=0       y=3       (0.0000, 6.0000)
0DFE: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E00: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
0E02: 00 D0           RTS                         

; "T"
0E04: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0E06: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0E08: 06 F0           SVEC    scale=00(*2)   bri=0     x=-2      y=0       (-4.0000, 0.0000)
0E0A: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E0C: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
0E0E: 00 D0           RTS                         

; "U"
0E10: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
0E12: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
0E14: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E16: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0E18: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
0E1A: 00 D0           RTS                         

; "V"
0E1C: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
0E1E: 71 FF           SVEC    scale=01(*4)   bri=7     x=1       y=-3      (4.0000, -12.0000)
0E20: 71 FB           SVEC    scale=01(*4)   bri=7     x=1       y=3       (4.0000, 12.0000)
0E22: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
0E24: 00 D0           RTS                         

; "W"
0E26: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
0E28: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
0E2A: 72 F2           SVEC    scale=00(*2)   bri=7     x=2       y=2       (4.0000, 4.0000)
0E2C: 72 F6           SVEC    scale=00(*2)   bri=7     x=2       y=-2      (4.0000, -4.0000)
0E2E: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0E30: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
0E32: 00 D0           RTS                         
  
; "X"
0E34: 72 FB           SVEC    scale=01(*4)   bri=7     x=2       y=3       (8.0000, 12.0000)
0E36: 06 F8           SVEC    scale=01(*4)   bri=0     x=-2      y=0       (-8.0000, 0.0000)
0E38: 72 FF           SVEC    scale=01(*4)   bri=7     x=2       y=-3      (8.0000, -12.0000)
0E3A: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0E3C: 00 D0           RTS                         

; "Y"
0E3E: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0E40: 70 FA           SVEC    scale=01(*4)   bri=7     x=0       y=2       (0.0000, 8.0000)
0E42: 76 F2           SVEC    scale=00(*2)   bri=7     x=-2      y=2       (-4.0000, 4.0000)
0E44: 02 F8           SVEC    scale=01(*4)   bri=0     x=2       y=0       (8.0000, 0.0000)
0E46: 76 F6           SVEC    scale=00(*2)   bri=7     x=-2      y=-2      (-4.0000, -4.0000)
0E48: 02 FE           SVEC    scale=01(*4)   bri=0     x=2       y=-2      (8.0000, -8.0000)
0E4A: 00 D0           RTS                         

; "Z"
0E4C: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
0E4E: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E50: 76 FF           SVEC    scale=01(*4)   bri=7     x=-2      y=-3      (-8.0000, -12.0000)
0E52: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E54: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0E56: 00 D0           RTS                         

; SPACE
0E58: 03 F8           SVEC    scale=01(*4)   bri=0     x=3       y=0       (12.0000, 0.0000)
0E5A: 00 D0           RTS                         

; "1"
0E5C: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0E5E: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0E60: 02 FF           SVEC    scale=01(*4)   bri=0     x=2       y=-3      (8.0000, -12.0000)
0E62: 00 D0           RTS                         

; "2"
0E64: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
0E66: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E68: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
0E6A: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0E6C: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
0E6E: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E70: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0E72: 00 D0           RTS                         
  
; "3"
0E74: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E76: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0E78: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0E7A: 00 F7           SVEC    scale=00(*2)   bri=0     x=0       y=-3      (0.0000, -6.0000)
0E7C: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E7E: 02 F7           SVEC    scale=00(*2)   bri=0     x=2       y=-3      (4.0000, -6.0000)
0E80: 00 D0           RTS                         
  
; "4"
0E82: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
0E84: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
0E86: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E88: 00 F3           SVEC    scale=00(*2)   bri=0     x=0       y=3       (0.0000, 6.0000)
0E8A: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
0E8C: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0E8E: 00 D0           RTS                         

; "5"
0E90: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E92: 70 F3           SVEC    scale=00(*2)   bri=7     x=0       y=3       (0.0000, 6.0000)
0E94: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0E96: 70 F3           SVEC    scale=00(*2)   bri=7     x=0       y=3       (0.0000, 6.0000)
0E98: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0E9A: 01 FF           SVEC    scale=01(*4)   bri=0     x=1       y=-3      (4.0000, -12.0000)
0E9C: 00 D0           RTS                         

; "6"
0E9E: 00 F3           SVEC    scale=00(*2)   bri=0     x=0       y=3       (0.0000, 6.0000)
0EA0: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0EA2: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
0EA4: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0EA6: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0EA8: 03 FF           SVEC    scale=01(*4)   bri=0     x=3       y=-3      (12.0000, -12.0000)
0EAA: 00 D0           RTS                         

; "7"
0EAC: 00 FB           SVEC    scale=01(*4)   bri=0     x=0       y=3       (0.0000, 12.0000)
0EAE: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0EB0: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
0EB2: 02 F0           SVEC    scale=00(*2)   bri=0     x=2       y=0       (4.0000, 0.0000)
0EB4: 00 D0           RTS                         

; "8"  
0EB6: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0EB8: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0EBA: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0EBC: 70 FF           SVEC    scale=01(*4)   bri=7     x=0       y=-3      (0.0000, -12.0000)
0EBE: 00 F3           SVEC    scale=00(*2)   bri=0     x=0       y=3       (0.0000, 6.0000)
0EC0: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0EC2: 02 F7           SVEC    scale=00(*2)   bri=0     x=2       y=-3      (4.0000, -6.0000)
0EC4: 00 D0           RTS                         

; "9"  
0EC6: 02 F8           SVEC    scale=01(*4)   bri=0     x=2       y=0       (8.0000, 0.0000)
0EC8: 70 FB           SVEC    scale=01(*4)   bri=7     x=0       y=3       (0.0000, 12.0000)
0ECA: 76 F8           SVEC    scale=01(*4)   bri=7     x=-2      y=0       (-8.0000, 0.0000)
0ECC: 70 F7           SVEC    scale=00(*2)   bri=7     x=0       y=-3      (0.0000, -6.0000)
0ECE: 72 F8           SVEC    scale=01(*4)   bri=7     x=2       y=0       (8.0000, 0.0000)
0ED0: 02 F7           SVEC    scale=00(*2)   bri=0     x=2       y=-3      (4.0000, -6.0000)
0ED2: 00 D0           RTS                         

 ; Cross reference table for character data 
0ED4: 2C CB           JSR     $0E58               ; {} SPACE 1
0ED6: DD CA           JSR     $0DBA               ; {} O and 0 ... same pattern
0ED8: 2E CB           JSR     $0E5C               ; {} 1
0EDA: 32 CB           JSR     $0E64               ; {} 2
0EDC: 3A CB           JSR     $0E74               ; {} 3
0EDE: 41 CB           JSR     $0E82               ; {} 4
0EE0: 48 CB           JSR     $0E90               ; {} 5
0EE2: 4F CB           JSR     $0E9E               ; {} 6
0EE4: 56 CB           JSR     $0EAC               ; {} 7 2
0EE6: 5B CB           JSR     $0EB6               ; {} 8 3
0EE8: 63 CB           JSR     $0EC6               ; {} 9 4
0EEA: 78 CA           JSR     $0CF0               ; {} A 5
0EEC: 80 CA           JSR     $0D00               ; {} B 6
0EEE: 8D CA           JSR     $0D1A               ; {} C 7
0EF0: 93 CA           JSR     $0D26               ; {} D 8
0EF2: 9B CA           JSR     $0D36               ; {} E 9
0EF4: A3 CA           JSR     $0D46               ; {} F 10
0EF6: AA CA           JSR     $0D54               ; {} G 11
0EF8: B3 CA           JSR     $0D66               ; {} H 12
0EFA: BA CA           JSR     $0D74               ; {} I 13
0EFC: C1 CA           JSR     $0D82               ; {} J 14
0EFE: C7 CA           JSR     $0D8E               ; {} K 15
0F00: CD CA           JSR     $0D9A               ; {} L 16
0F02: D2 CA           JSR     $0DA4               ; {} M 17
0F04: D8 CA           JSR     $0DB0               ; {} N 18
0F06: DD CA           JSR     $0DBA               ; {} O 19
0F08: E3 CA           JSR     $0DC6               ; {} P 20
0F0A: EA CA           JSR     $0DD4               ; {} Q 21
0F0C: F3 CA           JSR     $0DE6               ; {} R 22
0F0E: FB CA           JSR     $0DF6               ; {} S 23
0F10: 02 CB           JSR     $0E04               ; {} T 24
0F12: 08 CB           JSR     $0E10               ; {} U 25
0F14: 0E CB           JSR     $0E1C               ; {} V 26
0F16: 13 CB           JSR     $0E26               ; {} W 27
0F18: 1A CB           JSR     $0E34               ; {} X 28
0F1A: 1F CB           JSR     $0E3E               ; {} Y 29
0F1C: 26 CB           JSR     $0E4C               ; {} Z 30
```

# Messages

```code
; Message offsets
0F1E: 0B  ; HIGH SCORES 
0F1F: 13  ; PLAYER
0F20: 19  ; YOUR SCORE IS ONE OF THE TEN BEST 
0F21: 2F  ; PEASE ENTER YOUR INITIALS
0F22: 41  ; PUSH ROTATE TO SELECT LETTER 
0F23: 55  ; PUSH HYPERSPACE WHEN LETTER IS CORRECT 
0F24: 6F  ; PUSH START 
0F25: 77  ; GAME OVER
0F26: 7D  ; 1 COIN 2 PLAYS 
0F27: 87  ; 1 COIN 1 PLAY 
0F28: 91  ; 2 COINS 1 PLAY 
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
0F29: 63 56 60 6E 3C EC 4D C0

; PLAYER_
; 10100_10000_00101_0 11101_01001_10110_0 00001_00000_00000_0 
; P     L     A       Y     E     R       _     @     @  
0F31: A4 0A EA 6C 08 00 

; YOUR SCORE IS ONE OF THE TEN BEST
; 11101_10011_11001_0 10110_00001_10111_0 00111_10011_10110_0 01001_00001_01101_0 10111_00001_10011_0 10010_01001_00001_0 10011_01010_00001_0 11000_01100_01001_0 00001_11000_01001_0 10010_00001_00110_0 01001_10111_11000_1 
; Y     O     U       R     _     S       C     O     R       E     _     I       S     _     O       N     E     _       O     F     _       T     H     E       _     T     E       N     _     B       E     S     T     @ 
0F37: EC F2 B0 6E 3C EC 48 5A B8 66 92 42 9A
0F44: 82 C3 12 0E 12 90 4C 4D F1 

; PEASE ENTER YOUR INITIALS
; 10100_10000_01001_0 00101_10111_01001_0 00001_01001_10010_0 11000_01001_10110_0 00001_11101_10011_0 11001_10110_00001_0 01101_10010_01101_0 11000_01101_00101_0 10000_10111_00000_0 
; P     L     E       A     S     E       _     E     N       T     E     R       _     Y     O       U     R     _       I     N     I       T     I     A       L     S     @     
0F4D: A4 12 2D D2 0A 64 C2 6C 0F 66 CD 
0F58: 82 6C 9A C3 4A 85 C0
 
; PUSH ROTATE TO SELECT LETTER
; 10100_11001_10111_0 01100_00001_10110_0 10011_11000_00101_0 11000_01001_00001_0 11000_10011_00001_0 10111_01001_10000_0 01001_00111_11000_0 00001_10000_01001_0 11000_11000_01001_0 10110_00000_00000_0 
; P     U     S       H     _     R       O     T     A       T     E     _       T     O     _       S     E     L       E     C     T       _     L     E       T     T     E       R     @     @     
0F5F: A6 6E 60 6C 9E 0A C2 42 C4 C2 BA
0F6A: 60 49 F0 0C 12 C6 12 B0 00 

; PUSH HYPERSPACE WHEN LETTER IS CORRECT
; 10100_11001_10111_0 01100_00001_01100_0 11101_10100_01001_0 10110_10111_10100_0 00101_00111_01001_0 00001_11011_01100_0 01001_10010_00001_0 10000_01001_11000_0 11000_01001_10110_0 00001_01101_10111_0 00001_00111_10011_0 10110_10110_01001_0 00111_11000_00000_0 
; P     U     S       H     _     H       Y     P     E       R     S     P       A     C     E       _     W     H       E     N     _       L     E     T       T     E     R       _     I     S       _     C     O       R     R     E       C     T     @     
0F73: A6 6E 60 58 ED 12 B5 E8 29 D2 0E
0F7E: D8 4C 82 82 70 C2 6C 0B 6E 09 E6 B5
0F8A: 92 3E 00 

; PUSH START
; 10100_11001_10111_0 01100_00001_10111_0 11000_00101_10110_0 11000_00000_00000_0 
; P     U     S       H           S       T     A     R       T     @     @     
0F8D: A6 6E 60 6E C1 6C C0 00 

; GAME OVER
; 01011_00101_10001_0 01001_00001_10011_0 11010_01001_10110_1 
; G     A     M       E     _     O       V     E     R     @     
0F95: 59 62 48 66 D2 6D 

; 1 COIN 2 PLAYS
; 00011_00001_00111_0 10011_01101_10010_0 00001_00100_00001_0 10100_10000_00101_0 11101_10111_00000_0 
; 1     _     C       O     I     N       _     2     _       P     L     A       Y     S     @    
0F9B: 18 4E 9B 64 09 02 A4 0A ED C0 

; 1 COIN 1 PLAY
; 00011_00001_00111_0 10011_01101_10010_0 00001_00011_00001_0 10100_10000_00101_0 11101_00000_00000_0 
; 1     _     C       O     I     N       _     1     _       P     L     A       Y     @     @ 
0FA5: 18 4E 9B 64 08 C2 A4 0A E8  00 

; 2 COINS 1 PLAY
; 00100_00001_00111_0 10011_01101_10010_0 10111_00001_00011_0 00001_10100_10000_0 00101_11101_00000_0 
; 2     _     C       O     I     N       S     _     1       _     P     L       A     Y     @     
0FAF: 20 4E 9B 64 B8 46 0D 20 2F 40 
```

# Sine lookup table

```code
; Used for vertical thrust (offset by 64 to get cosine for horizontal thrust)
0FB9: 00 03 06
0FBC: 09 0C 10 13
0FC0: 16 19 1C 1F
0FC4: 22 25 28 2B
0FC8: 2E 31 33 36
0FCC: 39 3C 3F 41
0FD0: 44 47 49 4C
0FD4: 4E 51 53 55
0FD8: 58 5A 5C 5E
0FDC: 60 62 64 66
0FE0: 68 6A 6B 6D
0FE4: 6F 70 71 73
0FE8: 74 75 76 78
0FEC: 79 7A 7A 7B
0FF0: 7C 7D 7D 7E
0FF4: 7E 7E 7F 7F
0FF8: 7F 7F 

; Extra space
0FFA: 00 00 00 00 00 00
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

