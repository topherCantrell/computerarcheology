![Image Colors](MoonPatrol.jpg)

# Image Background Colors

| ROM      | Size | Content  | Ofs  | CRC      | SHA1                                     |
| -------- | ---- | -------- | ---- | -------- | ---------------------------------------- |
| mpc-3.1m |   32 | bg_pal   |    0 | 6a57eff2 | 2d1c12dab5915da2ccd466e39436c88be434d634 |

This ROM defines the colors used for the image backgrounds (not the text background).

```
; The comments in MAME say:
;
; /* the palette is a 32x8 PROM with many colors repeated. The address of */
; /* the colors to pick is as follows: */
; /* xbb00: mountains */
; /* 0xxbb: hills */
; /* 1xxbb: city */

; Pixel colors by experimenting
;             00    01     10     11
; Hills:      --    20     00     70
; Mountains:  --    C0     00     A0
; City:       --    00     77     70

; Colors used in color sets:
;
; 20    00 97 00 <FONT style="BACKGROUND-COLOR:#009700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; 70    00 DE 51 <FONT style="BACKGROUND-COLOR:#00DE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; 77    FF DE 51 <FONT style="BACKGROUND-COLOR:#FFDE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; C0    00 00 FF <FONT style="BACKGROUND-COLOR:#0000FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
; A0    00 97 AE <FONT style="BACKGROUND-COLOR:#0097AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
```

```plainCode
0000: 00 20 00 70 ; ---- <FONT style="BACKGROUND-COLOR:#009700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- <FONT style="BACKGROUND-COLOR:#00DE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0004: C0 20 00 70 ; <FONT style="BACKGROUND-COLOR:#0000FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#009700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- <FONT style="BACKGROUND-COLOR:#00DE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0008: 00 20 00 70 ; ---- <FONT style="BACKGROUND-COLOR: 009700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- <FONT style="BACKGROUND-COLOR:#00DE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
000C: A0 20 00 70 ; <FONT style="BACKGROUND-COLOR:#0097AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#009700">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- <FONT style="BACKGROUND-COLOR:#00DE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
;
0010: 00 00 77 70 ; ---- ---- <FONT style="BACKGROUND-COLOR:#FFDE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00DE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0014: C0 00 77 70 ; <FONT style="BACKGROUND-COLOR:#0000FF">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- <FONT style="BACKGROUND-COLOR:#FFDE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00DE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
0018: 00 00 77 70 ; ---- ---- <FONT style="BACKGROUND-COLOR:#FFDE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00DE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
001C: A0 00 77 70 ; <FONT style="BACKGROUND-COLOR:#0097AE">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> ---- <FONT style="BACKGROUND-COLOR:#FFDE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT> <FONT style="BACKGROUND-COLOR:#00DE51">&nbsp;&nbsp;&nbsp;&nbsp;</FONT>
```
