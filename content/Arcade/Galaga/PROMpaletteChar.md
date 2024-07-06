![PROM2](Galaga.jpg)

>>> binary roms/prom-4.2n

# Color palettes used for the character tiles

| ROM       | Size | Ofs  | CRC      | SHA1                                     |
| --------  | ---- | ---- | -------- | ---------------------------------------- |
| prom-4.2n | 256  |    0 | 59b6edab | 0281de86c236c88739297ff712e0a4f5c8bf8ab9 |

There are 4 colors per palette. The color values are indices into the colors in PROMcolors.

```code
0000: 0F 00 00 06    ; 00:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`
0004: 0F 0D 01 00    ; 01:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0000DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0008: 0F 02 0C 0D    ; 02:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#9700DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0000DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
000C: 0F 0B 01 00    ; 03:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0010: 0F 01 00 01    ; 04:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0014: 0F 00 00 02    ; 05:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0018: 0F 00 00 03    ; 06:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF9700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
001C: 0F 00 00 05    ; 07:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF00DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0020: 0F 00 00 09    ; 08:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0024: 00 00 00 00    ; 09:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0028: 00 00 00 00    ; 0A:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
002C: 00 00 00 00    ; 0B:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0030: 00 00 00 00    ; 0C:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0034: 00 00 00 00    ; 0D:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0038: 0F 00 00 00    ; 0E:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
003C: 00 00 00 00    ; 0F:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0040: 00 00 00 00    ; 10:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0044: 00 00 00 00    ; 11:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0048: 00 00 00 00    ; 12:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
004C: 00 00 00 00    ; 13:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0050: 00 00 00 00    ; 14:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0054: 00 00 00 00    ; 15:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0058: 00 00 00 00    ; 16:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
005C: 00 00 00 00    ; 17:  `<FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#DEDEDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0060: 0F 0B 07 06    ; 18:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#B8B8DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0064: 0F 06 0B 07    ; 19:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#B8B8DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0068: 0F 07 06 0B    ; 1A:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#B8B8DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
006C: 0F 0F 0F 01    ; 1B:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FF0000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0070: 0F 0F 0B 0F    ; 1C:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0074: 0F 02 0F 0F    ; 1D:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#FFFF00">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
0078: 0F 06 06 0B    ; 1E:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    
007C: 0F 06 0B 0B    ; 1F:  `<FONT style="BACKGROUND-COLOR:#000000">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00FFDE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#0068DE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>`    

; Solid-white (not used) from here down

0080: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
0090: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00A0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00B0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00C0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00D0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00E0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00F0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```code

