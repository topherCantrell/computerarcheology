![Sprite Colors](MoonPatrol.jpg)

>>> binary 0000:roms/mpc-1.1f

# Sprite Colors

| ROM      | Size | Content  | Ofs  | CRC      | SHA1                                     |
| -------- | ---- | -------- | ---- | -------- | ---------------------------------------- |
| mpc-1.1f |   32 | spr_pal  |    0 | 26979b13 | 8c41a8cce4f3384c392a9f7a223a50d7be0e14a5 |

This PROM lists a set of colors (16) used in Moon Patrol sprites. The
first color is "transparent" allowing the background to show through.

There is room in this table for 32 color definitions. 

The PROM4 table maps slots in individual color-sets to these 
colors. Color-set-0 described in PROM4, for instance, references 
addresses 0, 1, 2, and 3 here. Color-set-0 thus contains transparent, 
near-black, red/violet, and turquoise.

The color 0C (purple) is not referenced by any color set.

```code
;          R  G  B
0000: 00 ;           ---- transparent
0001: 01 ; 00 00 1A  `<FONT style="BACKGROUND-COLOR:#00001A">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` near black
0002: C6 ; C1 00 AE  `<FONT style="BACKGROUND-COLOR:#C100AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` red/violet
0003: 37 ; 00 AE C8  `<FONT style="BACKGROUND-COLOR:#00AEC8">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` turquoise 
0004: B8 ; 84 C8 00  `<FONT style="BACKGROUND-COLOR:#84C800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` yellow/green
0005: C0 ; C1 00 00  `<FONT style="BACKGROUND-COLOR:#C10000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` light red
0006: 38 ; 00 C8 00  `<FONT style="BACKGROUND-COLOR:#00C800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` green
0007: 80 ; 84 00 00  `<FONT style="BACKGROUND-COLOR:#840000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` red
0008: FF ; C1 C8 C8  `<FONT style="BACKGROUND-COLOR:#C1C8C8">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` white
0009: F8 ; C1 C8 00  `<FONT style="BACKGROUND-COLOR:#C1C800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` yellow
000A: 98 ; 84 51 00  `<FONT style="BACKGROUND-COLOR:#845100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` brown
000B: 50 ; 3E 37 00  `<FONT style="BACKGROUND-COLOR:#3E3700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` dark tan
000C: 47 ; 3E 00 C8  `<FONT style="BACKGROUND-COLOR:#3E00C8">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` purple (not used in any color set)
000D: E8 ; C1 90 00  `<FONT style="BACKGROUND-COLOR:#C19000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` gold
000E: 6F ; 62 90 C8  `<FONT style="BACKGROUND-COLOR:#6290C8">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` sky blue
000F: 18 ; 00 51 00  `<FONT style="BACKGROUND-COLOR:#005100">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` dark green

; Unused (transparent)
; 
0010: 00 00 00 00 
0014: 00 00 00 00 
0018: 00 00 00 00 
001C: 00 00 00 00 
```

