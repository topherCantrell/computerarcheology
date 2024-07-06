![PROM3](Galaga.jpg)

>>> binary roms/prom-3.1c

# Color palettes used for the sprite tiles

| ROM       | Size | Ofs  | CRC      | SHA1                                     |
| --------  | ---- | ---- | -------- | ---------------------------------------- |
| prom-3.1c | 256  |    0 | 4a04bb6b | cdd4bc1013f5c11984fdc4fd10e2d2e27120c1e5 |

There are 4 colors per palette. The color values are indices into the colors in PROMcolors.

```code
0000: 0F 08 0E 02    ; 00:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DE4700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#009797">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0004: 0F 05 0B 0C    ; 01:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF00DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#9700DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0008: 0F 00 0B 01    ; 02:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
000C: 0F 01 0B 02    ; 03:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0010: 0F 08 0D 02    ; 04:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DE4700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0000DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0014: 0F 06 01 04    ; 05:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFB800">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0018: 0F 09 01 05    ; 06:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF00DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
001C: 0F 07 0B 01    ; 07:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#B8B8DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0020: 0F 01 06 0B    ; 08:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0024: 0F 01 0B 00    ; 09:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0028: 0F 01 02 00    ; 0A:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
002C: 0F 00 01 06    ; 0B:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0030: 0F 00 00 06    ; 0C:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0034: 0F 03 0B 09    ; 0D:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF9700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0038: 0F 06 02 00    ; 0E:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
003C: 00 00 00 00    ; 0F:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    

; Solid-white (not used) from here down

0040: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0050: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0060: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0070: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0080: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0090: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00B0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

