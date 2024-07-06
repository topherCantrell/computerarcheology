![PROM1](Galaga.jpg)

>>> binary roms/prom-5.5n

# Color values used in the sprites/character palettes

| ROM       | Size | Ofs  | CRC      | SHA1                                     |
| --------  | ---- | ---- | -------- | ---------------------------------------- |
| prom-5.5n | 32   |    0 | 54603c6b | 62f1279a784ab2f8218c4137c71a6dea13b4af155d9cb5b999a75d4f1eb9c71346accda00e6a3490 |

The PROMpaletteChar and PROMpaletteSprite files reference these colors by index.

The mame source describes the one-byte color format as: BB GGG RRR, where each color is 3 bits
(the LSB of blue is 0). Each of the 3 bits has a weight in the final byte value (MSB to LSB): 0x97, 0x47, 0x21.

The last 16 colors (10-1F) aren't used in any color set (characters or sprites). The 0A color isn't used either.

```code
0000: F6    ; 11 110 110  #DEDEDE  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0001: 07    ; 00 000 111  #FF0000  `<FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0002: 3F    ; 00 111 111  #FFFF00  `<FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0003: 27    ; 00 100 111  #FF9700  `<FONT style="BACKGROUND-COLOR:#FF9700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0004: 2F    ; 00 101 111  #FFB800  `<FONT style="BACKGROUND-COLOR:#FFB800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0005: C7    ; 11 000 111  #FF00DE  `<FONT style="BACKGROUND-COLOR:#FF00DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0006: F8    ; 11 111 000  #00FFDE  `<FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0007: ED    ; 11 101 101  #B8B8DE  `<FONT style="BACKGROUND-COLOR:#B8B8DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0008: 16    ; 00 010 110  #DE4700  `<FONT style="BACKGROUND-COLOR:#DE4700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0009: 38    ; 00 111 000  #00FF00  `<FONT style="BACKGROUND-COLOR:#00FF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
000A: 21    ; 00 100 001  #219700  `<FONT style="BACKGROUND-COLOR:#219700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>` (not used in palettes)
000B: D8    ; 11 011 000  #0068DE  `<FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
000C: C4    ; 11 000 100  #9700DE  `<FONT style="BACKGROUND-COLOR:#9700DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
000D: C0    ; 11 000 000  #0000DE  `<FONT style="BACKGROUND-COLOR:#0000DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
000E: A0    ; 10 100 000  #009797  `<FONT style="BACKGROUND-COLOR:#009797">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
000F: 00    ; 00 000 000  #000000  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`

0010: F6    ; 11 110 110  #DEDEDE  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0011: 07    ; 00 000 111  #FF0000  `<FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0012: 3F    ; 00 111 111  #FFFF00  `<FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0013: 27    ; 00 100 111  #FF9700  `<FONT style="BACKGROUND-COLOR:#FF9700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0014: 00    ; 00 000 000  #000000  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0015: C7    ; 11 000 111  #FF00DE  `<FONT style="BACKGROUND-COLOR:#FF00DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0016: F8    ; 11 111 000  #00FFDE  `<FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0017: E8    ; 11 101 000  #00B8DE  `<FONT style="BACKGROUND-COLOR:#00B8DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0018: 00    ; 00 000 000  #000000  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0019: 38    ; 00 111 000  #00FF00  `<FONT style="BACKGROUND-COLOR:#00FF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
001A: 00    ; 00 000 000  #000000  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
001B: D8    ; 11 011 000  #0068DE  `<FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
001C: C5    ; 11 000 101  #B800DE  `<FONT style="BACKGROUND-COLOR:#B800DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
001D: C0    ; 11 000 000  #0000DE  `<FONT style="BACKGROUND-COLOR:#0000DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
001E: 00    ; 00 000 000  #000000  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
001F: 00    ; 00 000 000  #000000  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
```

