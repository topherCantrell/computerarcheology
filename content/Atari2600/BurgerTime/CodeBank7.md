![Burger Time](A2600BT.jpg)

# Burger Time Bank 7

>>> cpu 6502

>>> memoryTable hard 
[Hardware Info](../Stella.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

```code
; Bank 7 (Fixed bank)

; A 256-byte block of RAM maps to this 512-byte memory
; space. The first 256 bytes is where you write. The
; second 256 bytes is where you read.
;
; You select one of 4 256-byte blocks to map here by
; accessing FFE8, FFE9, FFEA, FFEB
F800: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F810: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F820: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F830: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F840: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F850: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F860: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F870: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F880: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F890: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8B0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8D0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F8F0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

F900: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F910: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F920: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F930: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F940: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F950: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F960: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F970: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F980: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F990: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9B0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9D0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
F9F0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

FA00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FA70: 00 00 00 00 00 00 00 22 22 22 22 22 22 22 22 22
FA80: 22 62 62 62 62 E0 E0 E0 E0 00 00 00 00 00 00 00
FA90: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FAA0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FAB0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FAC0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FAD0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FAE0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FAF0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FB00: 00 F0 F0 F0 C0 00 00 00 80 00 00 00 00 80 00 00
FB10: 00 00 80 00 00 00 00 80 00 00 F0 00 F0 00 00 60
FB20: 00 80 00 00 60 F0 80 00 00 60 60 80 00 F0 60 60
FB30: 80 F0 C0 F0 60 E0 60 C0 00 60 00 60 C0 00 60 00
FB40: 60 F0 00 60 00 F0 C0 00 F0 00 60 C0 F0 00 00 60
FB50: C0 60 00 E0 60 F0 60 00 80 F0 C0 60 00 80 60 C0
FB60: 60 00 80 60 C0 60 00 80 60 F0 F0 F0 F0 F0 00 00
FB70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FB80: 00 FF FF FF FF 00 C3 06 80 19 00 C3 06 80 19 00
FB90: C3 1F 80 19 00 C3 06 80 1B 00 FF 06 FF 18 00 18
FBA0: 06 99 18 00 18 FF 99 18 00 18 06 99 18 FF 18 06
FBB0: 99 FF 19 FF 1F FF 01 19 C3 00 19 01 19 C3 00 19
FBC0: 01 FF C3 00 3F FF 19 C3 FF 19 01 19 FF 06 19 01
FBD0: 19 18 06 FF 01 FF 18 1F 81 FF 19 18 06 81 01 19
FBE0: 18 06 81 01 19 18 06 81 01 FF FF FF FF FF 00 00
FBF0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FC00: C0 FF 00 FF FF 80 30 00 18 81 80 30 00 18 81 80
FC10: 30 FF 18 81 80 30 18 18 FF FC FF 18 FF 00 98 06
FC20: 18 01 00 98 06 18 01 00 98 06 18 01 00 FF 06 18
FC30: 01 03 99 FF FF 03 01 99 30 18 01 01 99 30 18 01
FC40: 01 9B 30 18 FF FF 99 30 18 19 81 99 FF 18 19 81
FC50: 99 06 18 1B 81 FF 06 FF 19 FF 99 06 18 19 19 99
FC60: 06 18 19 19 99 06 18 19 19 FF FF FE FF FF 00 00
FC70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
FC80: 7E 66 66 66 66 7E 7E 18 18 18 18 78 7E 60 7E 06
FC90: 66 7E 7E 06 06 7C 06 7E 06 06 7E 66 66 66 7E 66
FCA0: 06 7E 60 7E 7E 66 66 7E 60 7E 20 30 18 0C 06 7E
FCB0: 7E 66 66 3C 66 7E 7E 06 7E 66 66 7E 24 24 FF 24
FCC0: FF 24 3C 66 66 66 66 66 60 60 7E 66 66 7E

; Just data above?

FCCE: AD E0 FF        LDA     $FFE0 ; Switch in bank 0
FCD1: 20 B6 F1        JSR     $F1B6  
FCD4: AD E6 FF        LDA     $FFE6                   ; Switch in bank 6
FCD7: 20 09 F4        JSR     $F409                   
FCDA: 85 2C           STA     $2C                   ; CXCLR clear all collision flags
FCDC: AD 84 02        LDA     $0284                   ; ??? Time to draw the visible screen?
FCDF: 10 FB           BPL     $FCDC                   ; ??? No ... keep waiting
FCE1: 85 02           STA     $02                   ; WSYNC
FCE3: A2 03           LDX     #$03                  ; Start the ...
FCE5: 86 00           STX     $00                   ; ... VSYNC
FCE7: 85 02           STA     $02                   ; WSYNC
FCE9: AD E6 FF        LDA     $FFE6                   ; Switch in bank 6
FCEC: 20 CB F3        JSR     $F3CB                   
FCEF: 85 02           STA     $02                   ; WSYNC
FCF1: 86 00           STX     $00                   ; X has 0 at this point ... release the VSYNC
FCF3: A9 22           LDA     #$22                  ; 34 ticks = 2176 machine cycles ...
FCF5: 8D 96 02        STA     $0296                 ; ... 2176/(228/3) = 28.6 scanlines
FCF8: 24 F6           BIT     $F6                   
FCFA: 70 06           BVS     $FD02                   
FCFC: AD E1 FF        LDA     $FFE1                   ; Switch in bank 1
FCFF: 20 35 F0        JSR     $F035                   
FD02: AD E0 FF        LDA     $FFE0                   ; Switch in bank 0
FD05: 20 31 F5        JSR     $F531                   
FD08: AD E4 FF        LDA     $FFE4                   ; Switch in bank 4
FD0B: 20 5D F6        JSR     $F65D                   
FD0E: AD 84 02        LDA     $0284                   ; Time to draw the visible screen?
FD11: 10 FB           BPL     $FD0E                   ; No ... keep waiting

FD13: 20 27 FD        JSR     $FD27                   
FD16: 4C 18 FF        JMP     $FF18
                   
FD19: AD E1 FF        LDA     $FFE1                   ; Switch in bank 1
FD1C: 20 4D F3        JSR     $F34D                   
FD1F: AD E5 FF        LDA     $FFE5                   ; Switch in bank 5
FD22: 60              RTS 
                        
FD23: 00 00 00 00                 
         
FD27: 20 D7 F6        JSR     $F6D7                   
FD2A: A9 DF           LDA     #$DF                  
FD2C: 85 06           STA     $06                   ; COLUP0
FD2E: 85 07           STA     $07                   ; COLUP1
FD30: AD 58 F9        LDA     $F958                   
FD33: 85 F2           STA     $F2                   
FD35: A5 D1           LDA     $D1                   
FD37: 85 F3           STA     $F3                   
FD39: A2 03           LDX     #$03                  
FD3B: 20 96 F7        JSR     $F796                   
FD3E: A0 05           LDY     #$05                  
FD40: 20 4F F7        JSR     $F74F                   
FD43: A9 0D           LDA     #$0D                  
FD45: 85 06           STA     $06                   ; COLUP0
FD47: A9 35           LDA     #$35                  
FD49: 85 07           STA     $07                   ; COLUP1
FD4B: A9 31           LDA     #$31                  
FD4D: 85 0A           STA     $0A                   ; CTRLPF
FD4F: AD E6 FF        LDA     $FFE6                   ; Switch in bank 6
FD52: 20 AF F3        JSR     $F3AF                   
FD55: AD E5 FF        LDA     $FFE5                   ; Switch in bank 5
FD58: A0 01           LDY     #$01                  
FD5A: 20 22 F4        JSR     $F422                   
FD5D: AD E4 FF        LDA     $FFE4                   ; Switch in bank 4
FD60: AD 0A F9        LDA     $F90A                   
FD63: 10 05           BPL     $FD6A                   
FD65: A9 08           LDA     #$08                  ; Reflect ...
FD67: 85 0B           STA     $0B                   ; ... REFP0 player 1
FD69: EA              NOP                         
FD6A: 85 02           STA     $02                   ; WSYNC
FD6C: EA              NOP                         
FD6D: EA              NOP                         
FD6E: A0 78           LDY     #$78                  
FD70: B1 C9           LDA     ($C9),Y               
FD72: 4C 16 FE        JMP     $FE16                   
FD75: A9 00           LDA     #$00                  ; For clearing
FD77: 85 0A           STA     $0A                   ; CTRLPF
FD79: 85 02           STA     $02                   ; WSYNC
FD7B: 85 0D           STA     $0D                   ; PF0
FD7D: 85 0E           STA     $0E                   ; PF1
FD7F: 85 0F           STA     $0F                   ; PF2
FD81: 85 1D           STA     $1D                   ; ENAM0
FD83: 85 1E           STA     $1E                   ; ENAM1
FD85: 85 1F           STA     $1F                   ; ENABL
FD87: 85 1B           STA     $1B                   ; GRP0
FD89: 85 1C           STA     $1C                   ; GRP1
FD8B: A9 1F           LDA     #$1F                  
FD8D: 85 08           STA     $08                   ; COLUPF
FD8F: A0 12           LDY     #$12                  
FD91: A2 03           LDX     #$03                  
FD93: 86 C7           STX     $C7                   
FD95: A2 00           LDX     #$00                  
FD97: F0 12           BEQ     $FDAB                   
FD99: A9 03           LDA     #$03                  
FD9B: 85 02           STA     $02                   ; WSYNC
FD9D: 85 C7           STA     $C7                   
FD9F: A9 00           LDA     #$00                  ; Clear
FDA1: 85 0E           STA     $0E                   ; PF1
FDA3: 85 0F           STA     $0F                   ; PF2
FDA5: BD E8 F7        LDA     $F7E8,X                 
FDA8: 85 08           STA     $08                   ; COLUPF
FDAA: 88              DEY                         
FDAB: 85 02           STA     $02                   ; WSYNC
FDAD: B9 EC F7        LDA     $F7EC,Y                 
FDB0: 3D 72 F9        AND     $F972,X                 
FDB3: 85 0E           STA     $0E                   ; PF1
FDB5: B9 EC F7        LDA     $F7EC,Y                 
FDB8: 3D 77 F9        AND     $F977,X                 
FDBB: 85 0F           STA     $0F                   ; PF2
FDBD: EA              NOP                         
FDBE: EA              NOP                         
FDBF: B9 EC F7        LDA     $F7EC,Y                 
FDC2: 3D 7C F9        AND     $F97C,X                 
FDC5: 85 0E           STA     $0E                   ; PF1
FDC7: B9 EC F7        LDA     $F7EC,Y                 
FDCA: 3D 81 F9        AND     $F981,X                 
FDCD: 85 0F           STA     $0F                   ; PF2
FDCF: 88              DEY                         
FDD0: 30 08           BMI     $FDDA                   
FDD2: C6 C7           DEC     $C7                   
FDD4: 10 D5           BPL     $FDAB                   
FDD6: E8              INX                         
FDD7: 4C 99 FD        JMP     $FD99                   
FDDA: 85 02           STA     $02                   ; WSYNC
FDDC: A9 92           LDA     #$92                  
FDDE: 85 08           STA     $08                   ; COLUPF
FDE0: A9 42           LDA     #$42                  
FDE2: 85 0E           STA     $0E                   ; PF1
FDE4: 85 0F           STA     $0F                   ; PF2
FDE6: 85 02           STA     $02                   ; WSYNC
FDE8: A9 3C           LDA     #$3C                  
FDEA: 85 0E           STA     $0E                   ; PF1
FDEC: 85 0F           STA     $0F                   ; PF2
FDEE: 85 02           STA     $02                   ; WSYNC
FDF0: A9 00           LDA     #$00                  
FDF2: 85 0E           STA     $0E                   ; PF1
FDF4: 85 0F           STA     $0F                   ; PF2
FDF6: A0 00           LDY     #$00                  
FDF8: 85 02           STA     $02                   ; WSYNC
FDFA: 88              DEY                         
FDFB: 10 FB           BPL     $FDF8                   
FDFD: AD E5 FF        LDA     $FFE5                   ; Switch in bank 5
FE00: 60              RTS                         

FE01: 4C 75 FD        JMP     $FD75       
;            
FE04: A9 00           LDA     #$00                  
FE06: 85 85           STA     $85                   
FE08: A5 C7           LDA     $C7                   
FE0A: 4C 43 FE        JMP     $FE43
                   
FE0D: A9 00           LDA     #$00                  
FE0F: 85 87           STA     $87                   
FE11: A5 C7           LDA     $C7                   
FE13: 4C 76 FE        JMP     $FE76
                   
FE16: 85 02           STA     $02                   ; WSYNC
FE18: 85 0D           STA     $0D                   
FE1A: A5 B1           LDA     $B1                   
FE1C: 85 0A           STA     $0A                   
FE1E: B1 E4           LDA     ($E4),Y               
FE20: 85 1B           STA     $1B                   
FE22: B1 CB           LDA     ($CB),Y               
FE24: 85 0E           STA     $0E                   
FE26: B1 CD           LDA     ($CD),Y               
FE28: 85 0F           STA     $0F                   
FE2A: B1 EA           LDA     ($EA),Y               
FE2C: 85 1E           STA     $1E                   
FE2E: B1 EC           LDA     ($EC),Y               
FE30: 85 1F           STA     $1F                   
FE32: 88              DEY                         
FE33: 30 CC           BMI     $FE01                   
FE35: 98              TYA                         
FE36: A6 89           LDX     $89                   
FE38: D5 8D           CMP     $8D,X                 
FE3A: B0 C8           BCS     $FE04                   
FE3C: B5 A1           LDA     $A1,X                 
FE3E: 85 85           STA     $85                   
FE40: E8              INX                         
FE41: 86 89           STX     $89                   
FE43: A9 00           LDA     #$00                  
FE45: 85 0D           STA     $0D                   
FE47: A5 B2           LDA     $B2                   
FE49: 85 0A           STA     $0A                   
FE4B: B1 E4           LDA     ($E4),Y               
FE4D: 85 1B           STA     $1B                   
FE4F: A5 81           LDA     $81                   
FE51: 85 0E           STA     $0E                   
FE53: A5 82           LDA     $82                   
FE55: 85 0F           STA     $0F                   
FE57: B1 E2           LDA     ($E2),Y               
FE59: 85 1C           STA     $1C                   
FE5B: A5 83           LDA     $83                   
FE5D: 85 0E           STA     $0E                   
FE5F: B1 E8           LDA     ($E8),Y               
FE61: 85 1D           STA     $1D                   
FE63: A5 84           LDA     $84                   
FE65: 88              DEY                         
FE66: 85 0F           STA     $0F                   
FE68: 98              TYA                         
FE69: A6 8B           LDX     $8B                   
FE6B: D5 97           CMP     $97,X                 
FE6D: B0 9E           BCS     $FE0D                   
FE6F: B5 A9           LDA     $A9,X                 
FE71: 85 87           STA     $87                   
FE73: E8              INX                         
FE74: 86 8B           STX     $8B                   
FE76: B1 E4           LDA     ($E4),Y               
FE78: 85 1B           STA     $1B                   
FE7A: A5 81           LDA     $81                   
FE7C: 85 0E           STA     $0E                   
FE7E: B1 E2           LDA     ($E2),Y               
FE80: 85 1C           STA     $1C                   
FE82: A5 82           LDA     $82                   
FE84: 85 0F           STA     $0F                   
FE86: B1 EA           LDA     ($EA),Y               
FE88: 85 1E           STA     $1E                   
FE8A: A5 83           LDA     $83                   
FE8C: 85 0E           STA     $0E                   
FE8E: 88              DEY                         
FE8F: A5 84           LDA     $84                   
FE91: 85 0F           STA     $0F                   
FE93: B1 EC           LDA     ($EC),Y               
FE95: 85 1F           STA     $1F                   
FE97: A6 8A           LDX     $8A                   
FE99: 98              TYA                         
FE9A: D5 92           CMP     $92,X                 
FE9C: B0 58           BCS     $FEF6                   
FE9E: B5 A5           LDA     $A5,X                 
FEA0: 85 86           STA     $86                   
FEA2: E8              INX                         
FEA3: 86 8A           STX     $8A                   
FEA5: A5 81           LDA     $81                   
FEA7: 85 0E           STA     $0E                   
FEA9: B1 E4           LDA     ($E4),Y               
FEAB: 85 1B           STA     $1B                   
FEAD: A5 82           LDA     $82                   
FEAF: 85 0F           STA     $0F                   
FEB1: B1 E2           LDA     ($E2),Y               
FEB3: 85 1C           STA     $1C                   
FEB5: A5 83           LDA     $83                   
FEB7: 85 0E           STA     $0E                   
FEB9: 88              DEY                         
FEBA: A5 84           LDA     $84                   
FEBC: 85 0F           STA     $0F                   
FEBE: 98              TYA                         
FEBF: A6 8C           LDX     $8C                   
FEC1: D5 9C           CMP     $9C,X                 
FEC3: B0 3A           BCS     $FEFF                   
FEC5: B5 AD           LDA     $AD,X                 
FEC7: 85 88           STA     $88                   
FEC9: E8              INX                         
FECA: 86 8C           STX     $8C                   
FECC: B1 E4           LDA     ($E4),Y               
FECE: 85 1B           STA     $1B                   
FED0: A5 81           LDA     $81                   
FED2: 85 0E           STA     $0E                   
FED4: A5 82           LDA     $82                   
FED6: 85 0F           STA     $0F                   
FED8: A5 85           LDA     $85                   
FEDA: 85 81           STA     $81                   
FEDC: A5 86           LDA     $86                   
FEDE: 85 82           STA     $82                   
FEE0: A5 83           LDA     $83                   
FEE2: 85 0E           STA     $0E                   
FEE4: A5 87           LDA     $87                   
FEE6: 85 83           STA     $83                   
FEE8: A5 84           LDA     $84                   
FEEA: 85 0F           STA     $0F                   
FEEC: A5 88           LDA     $88                   
FEEE: 85 84           STA     $84                   
FEF0: 88              DEY                         
FEF1: B1 C9           LDA     ($C9),Y               
FEF3: 4C 16 FE        JMP     $FE16                   
FEF6: A9 00           LDA     #$00                  
FEF8: 85 86           STA     $86                   
FEFA: A5 C7           LDA     $C7                   
FEFC: 4C A5 FE        JMP     $FEA5                   
FEFF: A9 00           LDA     #$00                  
FF01: 85 88           STA     $88                   
FF03: A5 C7           LDA     $C7                   
FF05: 4C CC FE        JMP     $FECC      
             
; Startup comes here

Startup:
FF08: D8              CLD                         ; Clear decimal math flag
FF09: A2 FF           LDX     #$FF                ; Stack start at ...
FF0B: 9A              TXS                         ; ... end of RAM
FF0C: AD E5 FF        LDA     $FFE5               ; Switch in bank 5 (F000..F7FF)
FF0F: AD E8 FF        LDA     $FFE8               ; Set RAM to READ
FF12: 20 00 F0        JSR     $F000               ; bank5:F000             
FF15: 20 19 FD        JSR     $FD19                   

FF18: 85 02           STA     $02                   ; WSYNC
FF1A: 20 99 F6        JSR     $F699                   
FF1D: F0 64           BEQ     $FF83                   
FF1F: 90 E7           BCC     $FF08                   
FF21: 70 34           BVS     $FF57                   
FF23: E6 DE           INC     $DE                   
FF25: AD 56 F9        LDA     $F956                   
FF28: 29 10           AND     #$10                  
FF2A: F0 0A           BEQ     $FF36                   
FF2C: 24 80           BIT     $80                   
FF2E: 30 27           BMI     $FF57                   
FF30: 20 BA F6        JSR     $F6BA                   
FF33: 4C D4 FC        JMP     $FCD4                   
FF36: 2C 56 F9        BIT     $F956                   
FF39: 10 1F           BPL     $FF5A                   
FF3B: 24 80           BIT     $80                   
FF3D: 30 18           BMI     $FF57                   
FF3F: 20 27 F7        JSR     $F727                   
FF42: B0 1F           BCS     $FF63                   
FF44: 2C 09 F9        BIT     $F909                   
FF47: 10 0E           BPL     $FF57                   
FF49: 20 35 F7        JSR     $F735                   
FF4C: 10 28           BPL     $FF76                   
FF4E: A5 DE           LDA     $DE                   
FF50: 29 7F           AND     #$7F                  
FF52: D0 03           BNE     $FF57                   
FF54: 20 E2 F6        JSR     $F6E2                   
FF57: 4C D4 FC        JMP     $FCD4                   
FF5A: 2C 56 F9        BIT     $F956                   
FF5D: 50 2D           BVC     $FF8C                   
FF5F: 24 80           BIT     $80                   
FF61: 50 03           BVC     $FF66                   
FF63: 4C CE FC        JMP     $FCCE                   
FF66: 20 27 F7        JSR     $F727                   
FF69: B0 F8           BCS     $FF63                   
FF6B: 20 11 F7        JSR     $F711                   
FF6E: 10 06           BPL     $FF76                   
FF70: 20 0C F6        JSR     $F60C                   
FF73: 4C 83 FF        JMP     $FF83                   
FF76: AD 56 F9        LDA     $F956                   
FF79: 29 8F           AND     #$8F                  
FF7B: 8D 56 F8        STA     $F856                   
FF7E: 20 FD F5        JSR     $F5FD                   
FF81: D0 D4           BNE     $FF57                   
FF83: AD E1 FF        LDA     $FFE1                   ; Switch in bank 1
FF86: 20 4D F3        JSR     $F34D                   
FF89: 4C D4 FC        JMP     $FCD4                   
FF8C: AD E0 FF        LDA     $FFE0                   ; Switch in bank 0
FF8F: 20 4D F6        JSR     $F64D                   
FF92: A5 DE           LDA     $DE                   
FF94: D0 0F           BNE     $FFA5                   
FF96: AD E1 FF        LDA     $FFE1                   ; Switch in bank 1
FF99: 20 5C F2        JSR     $F25C                   
FF9C: AD E6 FF        LDA     $FFE6                   ; Switch in bank 6
FF9F: 20 22 F7        JSR     $F722                   
FFA2: 4C DA FC        JMP     $FCDA                   
FFA5: 20 B6 F6        JSR     $F6B6                   
FFA8: 90 06           BCC     $FFB0                   
FFAA: AD E5 FF        LDA     $FFE5                   ; Switch in bank 5
FFAD: 20 D9 F2        JSR     $F2D9                   
FFB0: AD E6 FF        LDA     $FFE6                   ; Switch in bank 6
FFB3: 20 04 F0        JSR     $F004                   
FFB6: A5 DE           LDA     $DE                   
FFB8: 29 03           AND     #$03                  
FFBA: D0 06           BNE     $FFC2                   
FFBC: AD E5 FF        LDA     $FFE5                   ; Switch in bank 5
FFBF: 20 03 F4        JSR     $F403                   
FFC2: AD 56 F9        LDA     $F956                   
FFC5: 29 01           AND     #$01                  
FFC7: D0 8E           BNE     $FF57                   
FFC9: A5 DE           LDA     $DE                   
FFCB: 29 03           AND     #$03                  
FFCD: D0 0C           BNE     $FFDB                   
FFCF: 20 FF F2        JSR     $F2FF                   
FFD2: 20 64 F5        JSR     $F564                   
FFD5: AD E0 FF        LDA     $FFE0                   ; Switch in bank 0
FFD8: 20 02 F0        JSR     $F002                   
FFDB: 4C CE FC        JMP     $FCCE
                   
FFDE: 00 00    
                    
FFE0: 00 ; Read here to switch ROM bank 0 into F000 - F7FF
FFE1: 00 ; ... bank 1
FFE2: 00 ; ... bank 2                      
FFE3: 00 ; ... bank 3                         
FFE4: 00 ; ... bank 4           
FFE5: 00 ; ... bank 5 
FFE6: 00 ; ... bank 6 
FFE7: 00 ; ... 1K of RAM (first 1K is for WRITE, second 1K is for READ) 
;                      
FFE8: 00 ; Read here to switch 256 bytes of RAM (bank 0) into F800 - F9FF. First 256 WRITE, 2nd 256 READ                   
FFE9: 00 ; bank 1                         
FFEA: 00 ; bank 2                         
FFEB: 00 ; bank 3
                        
FFEC: 00 00 00 00 00 00 00 00 00 00 00 00 00 00    
```

# Vectors

```code                  
FFFA: 08 FF ; NMI to FF08 (not available on the 6507)
FFFC: 08 FF ; Reset to FF08
FFFE: 08 FF ; IRQ to FF08 (not available on the 6507)
```