![Phoenix](Phoenix.jpg)

# Phoenix

>>> cpu Z80

>>> binary 0000:roms/ic45 +  roms/ic46 + roms/ic47 + roms/ic48 + roms/h5-ic49.5a + roms/h6-ic50.6a + roms/h7-ic51.7a + roms/h8-ic52.8a

>>> memoryTable hard 

[Hardware Info](Hardware.md)

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

```code
0000: 00              NOP                         ; Start/restart and interrupts end up at 0008
0001: 00              NOP                         
0002: 00              NOP                         
0003: 00              NOP                         
0004: 00              NOP                         
0005: 00              NOP                         
0006: 00              NOP                         
0007: 00              NOP                         

0008: 31 FF 4B        LD      SP,$4BFF            ; Top-ish of RAM
;
000B: 26 50           LD      H,$50               ; 50xx video register
000D: 36 00           LD      (HL),$00            ; Select the first bank of RAM
000F: CD 50 00        CALL    $0050               ; {code.InitSoundScreen} Turn sound off and clear both screen areas
;

0012: 21 00 18        LD      HL,$1800            ; Screen draw info
0015: 0E 03           LD      C,$03               ; 3 columns (rotated to 3 rows)
0017: CD D0 01        CALL    $01D0               ; {} Draw the first 3 rows of the background (scores and coins);
001A: CD 80 00        CALL    $0080               ; {code.WaitVBlankCoin} Wait for VBlank and count any coins
001D: 3A A2 43        LD      A,($43A2)           ; {ram.M43A2}
0020: A7              AND     A                   
0021: CA 2D 00        JP      Z,$002D             ; {}
0024: CD 00 04        CALL    $0400               ; {}
0027: CD 00 27        CALL    $2700               ; {}
002A: C3 1A 00        JP      $001A               ; {}

002D: 3E 0F           LD      A,$0F               
002F: 26 60           LD      H,$60               ; 60xx sound A
0031: 77              LD      (HL),A              
0032: 26 68           LD      H,$68               ; 68xx sound B
0034: 77              LD      (HL),A              
0035: CD 77 03        CALL    $0377               ; {}
0038: 00              NOP                         
0039: CD E0 17        CALL    $17E0               ; {}
003C: A7              AND     A                   
003D: CA 46 00        JP      Z,$0046             ; {}
0040: CD 88 02        CALL    $0288               ; {}
0043: C3 1A 00        JP      $001A               ; {}
;
0046: CD E3 00        CALL    $00E3               ; {}
0049: C3 1A 00        JP      $001A               ; {}

004C: FF FF FF FF  

; Initialize the sound (off) and screen (clear)
InitSoundScreen:
0050: 26 68           LD      H,$68               ; 68xx sound B
0052: 36 00           LD      (HL),$00            ; Sound off
0054: 26 60           LD      H,$60               ; 60xx sound A
0056: 36 00           LD      (HL),$00            ; Sound off
0058: 26 58           LD      H,$58               ; 58xx scroll register
005A: 36 00           LD      (HL),$00            ; First memory bank
005C: CD 6B 00        CALL    $006B               ; {code.ClearScreenPlane} Clear the plane
005F: 26 50           LD      H,$50               ; 50xx video register
0061: 36 01           LD      (HL),$01            ; Second memory bank
0063: CD 6B 00        CALL    $006B               ; {code.ClearScreenPlane} Clear the plane
0066: 26 50           LD      H,$50               ; 50xx video register
0068: 36 00           LD      (HL),$00            ; Back to first memory bank
006A: C9              RET                         ; Done

; Clear a screen plane (foreground or background)
; Set the lower bit of the video register to pick fore/back.
; 4000 - 4BF8 (inclusive)
;
ClearScreenPlane:
006B: 21 F8 4B        LD      HL,$4BF8            ; Highest point
006E: 3E 3F           LD      A,$3F               ; Stop when H reaches 3F
0070: 36 00           LD      (HL),$00            ; Clear the memory
0072: 2B              DEC     HL                  ; Point to next
0073: BC              CP      H                   ; All done?
0074: C2 70 00        JP      NZ,$0070            ; {} No ... go back for all
0077: C9              RET                         ; Done

0078: CD 96 01        CALL    $0196               ; {}
007B: C3 F0 06        JP      $06F0               ; {}

007E: FF FF

; Wait for the vertical blanking and then handle coin counting
;
WaitVBlankCoin:
0080: 26 78           LD      H,$78               ; 78xx DSW0 Check ...
0082: 7E              LD      A,(HL)              ; ... screen blanking flag
0083: E6 80           AND     $80                 ; Wait for it ...
0085: CA 80 00        JP      Z,$0080             ; {code.WaitVBlankCoin} ... to set
0088: 7E              LD      A,(HL)              ; Check screen blanking flag
0089: E6 80           AND     $80                 ; Wait for it ...
008B: C2 88 00        JP      NZ,$0088            ; {} ... to clear (0=in blanking)
;
008E: 26 70           LD      H,$70               ; 70xx IN0 Current value ...
0090: 7E              LD      A,(HL)              ; ... of IN0 inputs
0091: 21 A0 43        LD      HL,$43A0            ; Value from ...
0094: 46              LD      B,(HL)              ; ... last read
0095: 77              LD      (HL),A              ; Store new value
0096: 2C              INC     L                   ; To 43A1
0097: 70              LD      (HL),B              ; Store old value
0098: 2E 9B           LD      L,$9B               ; Bump the ...
009A: CD 00 02        CALL    $0200               ; {code.AddOneToMem} ... ?? counter
009D: 2E 8F           LD      L,$8F               ; Get number ...
009F: 7E              LD      A,(HL)              ; ... of coins
;
; !! There are two digits for "coins" on the screen, but only the one's digit is
; !! changed. Once you get to 9, the code stops counting. It takes the coin
; !! from you, but it doesn't give you credit.
;
00A0: FE 09           CP      $09                 ; Already 9?
00A2: C8              RET     Z                   ; Yes ... nothing more to check
00A3: D2 00 00        JP      NC,$0000            ; {} More than 9? OOPS -- soft reset
00A6: 06 01           LD      B,$01               ; Coin bit of the input register
00A8: CD BB 00        CALL    $00BB               ; {code.CheckInputBits} Has the coin input gone from 1 to 0?
00AB: C8              RET     Z                   ; No ... no coins inserted ... done
00AC: 2E 8F           LD      L,$8F               ; Add one ...
00AE: 34              INC     (HL)                ; ... to coin count
00AF: 7E              LD      A,(HL)              ; Current value ...
00B0: C6 20           ADD     $20                 ; ... to number tile
00B2: 32 42 41        LD      ($4142),A           ; Change number of coins on screen
00B5: C9              RET                         ; Done

; Never called
00B6: 00              NOP                         
00B7: C9              RET                         

00B8: FF FF FF             

; Check to see if a particular bit(s) in the input register has changed
; from 1 to 0 since last we checked. Return NZ if transitioned from 1 to 0.
;
CheckInputBits:
00BB: 21 A0 43        LD      HL,$43A0            ; Get current ...
00BE: 7E              LD      A,(HL)              ; ... input value
00BF: 2F              CPL                         ; Flip the current bits
00C0: A0              AND     B                   ; Mask off all but the ones we are checking
00C1: 2C              INC     L                   ; Point to last input value
00C2: A6              AND     (HL)                ; Zero unles new bit is 0 and old is 1
00C3: C9              RET                         ; Return state

00C4: 7E              LD      A,(HL)              
00C5: E6 0F           AND     $0F                 
00C7: F6 20           OR      $20                 
00C9: 12              LD      (DE),A              
00CA: CD 10 02        CALL    $0210               ; {code.AddOneRow}
00CD: 05              DEC     B                   
00CE: C8              RET     Z                   
00CF: 7E              LD      A,(HL)              
00D0: 0F              RRCA                        
00D1: 0F              RRCA                        
00D2: 0F              RRCA                        
00D3: 0F              RRCA                        
00D4: E6 0F           AND     $0F                 
00D6: F6 20           OR      $20                 
00D8: 12              LD      (DE),A              
00D9: CD 10 02        CALL    $0210               ; {code.AddOneRow}
00DC: 2B              DEC     HL                  
00DD: 05              DEC     B                   
00DE: C2 C4 00        JP      NZ,$00C4            ; {}
00E1: C9              RET                         

00E2: FF             

00E3: 21 99 43        LD      HL,$4399            
00E6: CD 00 02        CALL    $0200               ; {code.AddOneToMem}
00E9: 01 01 00        LD      BC,$0001            
00EC: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
00EF: CA E1 01        JP      Z,$01E1             ; {}
00F2: 01 02 00        LD      BC,$0002            
00F5: 11 1F 01        LD      DE,$011F            
00F8: CD 60 02        CALL    $0260               ; {code.SubtractIfEnough}
00FB: D2 96 01        JP      NC,$0196            ; {}
00FE: 01 20 01        LD      BC,$0120            
0101: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
0104: CA CA 0B        JP      Z,$0BCA             ; {}
0107: 0E B0           LD      C,$B0               
0109: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
010C: CA E1 01        JP      Z,$01E1             ; {}
010F: 0E B8           LD      C,$B8               
0111: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
0114: CA 80 05        JP      Z,$0580             ; {}
0117: 0E C0           LD      C,$C0               
0119: 11 DF 02        LD      DE,$02DF            
011C: CD 60 02        CALL    $0260               ; {code.SubtractIfEnough}
011F: D2 78 00        JP      NC,$0078            ; {}
0122: 01 00 03        LD      BC,$0300            
0125: 11 AF 03        LD      DE,$03AF            
0128: CD 60 02        CALL    $0260               ; {code.SubtractIfEnough}
012B: D2 DC 21        JP      NC,$21DC            ; {}
012E: 01 E6 03        LD      BC,$03E6            
0131: 11 FF FF        LD      DE,$FFFF            
0134: CD 60 02        CALL    $0260               ; {code.SubtractIfEnough}
0137: D2 B0 03        JP      NC,$03B0            ; {}
013A: C9              RET                         

013B: FF FF FF FF FF    

0140: CD A0 03        CALL    $03A0               ; {}
0143: CD 80 00        CALL    $0080               ; {code.WaitVBlankCoin}
0146: CD 80 03        CALL    $0380               ; {}
0149: 21 A3 43        LD      HL,$43A3            
014C: 36 02           LD      (HL),$02            
014E: 2C              INC     L                   
014F: 36 00           LD      (HL),$00            
0151: 00              NOP                         
0152: 00              NOP                         
0153: 00              NOP                         
0154: 2E B8           LD      L,$B8               
0156: 06 08           LD      B,$08               
0158: CD D8 05        CALL    $05D8               ; {}
015B: 2E BA           LD      L,$BA               
015D: 36 10           LD      (HL),$10            
015F: 2E BE           LD      L,$BE               
0161: 3A 00 78        LD      A,($7800)           ; 78xx DSW0
0164: E6 0C           AND     $0C                 ; Bonus lives
0166: 07              RLCA                        
0167: 07              RLCA                        
0168: C6 30           ADD     $30                 
016A: 77              LD      (HL),A              
016B: 26 58           LD      H,$58               ; 58xx scroll register
016D: 36 00           LD      (HL),$00            
016F: CD 80 00        CALL    $0080               ; {code.WaitVBlankCoin}
0172: C9              RET                         
0173: 7E              LD      A,(HL)              
0174: E6 7F           AND     $7F                 
0176: 06 CE           LD      B,$CE               
0178: FE 1F           CP      $1F                 
017A: D8              RET     C                   
017B: 06 FE           LD      B,$FE               
017D: C8              RET     Z                   
017E: 06 AE           LD      B,$AE               
0180: FE 5F           CP      $5F                 
0182: D8              RET     C                   
0183: 06 FE           LD      B,$FE               
0185: C8              RET     Z                   
0186: 06 CE           LD      B,$CE               
0188: FE 7F           CP      $7F                 
018A: D8              RET     C                   
018B: 06 FE           LD      B,$FE               
018D: 2D              DEC     L                   
018E: 7E              LD      A,(HL)              
018F: FE 09           CP      $09                 
0191: C0              RET     NZ                  
0192: 06 7E           LD      B,$7E               
0194: C9              RET                         
0195: FF              RST     0X38                
0196: 7E              LD      A,(HL)              
0197: E6 1F           AND     $1F                 
0199: FE 06           CP      $06                 
019B: D8              RET     C                   
019C: 5F              LD      E,A                 
019D: 7E              LD      A,(HL)              
019E: E6 E0           AND     $E0                 
01A0: 4F              LD      C,A                 
01A1: 2D              DEC     L                   
01A2: 46              LD      B,(HL)              
01A3: 2E A8           LD      L,$A8               
01A5: 70              LD      (HL),B              
01A6: 2C              INC     L                   
01A7: 71              LD      (HL),C              
01A8: 01 60 18        LD      BC,$1860            
01AB: CD 06 02        CALL    $0206               ; {code.AddBCtoMem}
01AE: 7E              LD      A,(HL)              
01AF: 2D              DEC     L                   
01B0: 66              LD      H,(HL)              
01B1: 6F              LD      L,A                 
01B2: 7B              LD      A,E                 
01B3: 56              LD      D,(HL)              
01B4: 2C              INC     L                   
01B5: 5E              LD      E,(HL)              
01B6: 2D              DEC     L                   
01B7: 4F              LD      C,A                 
01B8: 85              ADD     A,L                 
01B9: 6F              LD      L,A                 
01BA: 79              LD      A,C                 
01BB: D6 06           SUB     $06                 
01BD: 4F              LD      C,A                 
01BE: CA C8 01        JP      Z,$01C8             ; {}
01C1: CD 17 02        CALL    $0217               ; {code.SubtractOneRow}
01C4: 0D              DEC     C                   
01C5: C2 C1 01        JP      NZ,$01C1            ; {}
01C8: 7E              LD      A,(HL)              
01C9: 12              LD      (DE),A              
01CA: C3 E0 14        JP      $14E0               ; {}
01CD: C2 C0 01        JP      NZ,$01C0            ; {}

01D0: 56              LD      D,(HL)              ; Get ...
01D1: 2C              INC     L                   ; ... the ...
01D2: 5E              LD      E,(HL)              ; ... screen coord
01D3: 7D              LD      A,L                 ; Add 5 ...
01D4: C6 05           ADD     $05                 ; ... go get ...
01D6: 6F              LD      L,A                 ; ... data
01D7: 06 1A           LD      B,$1A               ; 26 columns
01D9: CD ED 01        CALL    $01ED               ; {code.DrawColumn} Draw next column
01DC: 0D              DEC     C                   ; All columns done?
01DD: C2 D0 01        JP      NZ,$01D0            ; {} No ... draw all columns
01E0: C9              RET                         ; Done

01E1: CD 40 01        CALL    $0140               ; {}
01E4: 21 60 19        LD      HL,$1960            
01E7: 0E 03           LD      C,$03               
01E9: C3 D0 01        JP      $01D0               ; {}
;
01EC: FF               

; Remember the screen is rotated. 
; The draws a column in screen memory (row on the screen)
;
DrawColumn:
01ED: 7E              LD      A,(HL)              ; Copy the data ...
01EE: 12              LD      (DE),A              ; .. to the screen
01EF: 23              INC     HL                  ; Next in data
01F0: CD 17 02        CALL    $0217               ; {code.SubtractOneRow} Move DE to next row
01F3: 05              DEC     B                   ; All drawn?
01F4: C2 ED 01        JP      NZ,$01ED            ; {code.DrawColumn} Draw them all
01F7: C9              RET                         ; Done

; Pad to 0200
01F8: FF FF FF FF FF FF FF FF               

; Two-byte +1 to (HL-1) : (HL).
;
AddOneToMem:
0200: 34              INC     (HL)                ; Add one to LSB
0201: C0              RET     NZ                  ; We didn't overflow ... done
0202: 2D              DEC     L                   ; Back up to MSB
0203: 34              INC     (HL)                ; Carry into the MSB
0204: 2C              INC     L                   ; Restore point to LSB
0205: C9              RET                         ; Done

; Two-byte addition. BC is added to (HL-1) : (HL).
;
AddBCtoMem:
0206: 7E              LD      A,(HL)              ; Get the lower byte
0207: 81              ADD     A,C                 ; Add C to the lower
0208: 77              LD      (HL),A              ; Store the new lower
0209: 2D              DEC     L                   ; Back up to upper byte
020A: 7E              LD      A,(HL)              ; Add B and carry ...
020B: 88              ADC     A,B                 ; ... to upper byte
020C: 77              LD      (HL),A              ; Store the new upper byte
020D: 2C              INC     L                   ; Restore pointer to LSB
020E: C9              RET                         ; Done

020F: FF

; Add 32 (one row) to DE (two bytes)
;
AddOneRow:
0210: 7B              LD      A,E                 ; Add ...
0211: C6 20           ADD     $20                 ; ... 32 to ...
0213: 5F              LD      E,A                 ; ... E
0214: D0              RET     NC                  ; No carry ... we are done
0215: 14              INC     D                   ; Carry into D
0216: C9              RET                         ; Done

; Subtract 32 (one rom) from DE (two bytes)
SubtractOneRow:
0217: 7B              LD      A,E                 ; Subtract ...
0218: D6 20           SUB     $20                 ; ... 32 from ...
021A: 5F              LD      E,A                 ; ... E
021B: D0              RET     NC                  ; No borrow ... we are done
021C: 15              DEC     D                   ; Borrow from D
021D: C9              RET                         ; Done

021E: FF FF

; 3-byte (6 digit) BCD addition. Add BC*10 to (HL-2):(HL-1):(HL). 
; The games keeps the lowest digit of the scores to 0.
;
AddToScore:
0220: AF              XOR     A                   ; !! Pointless. We are about to change A and the flags
0221: 7E              LD      A,(HL)              ; Lowest 2 digits
0222: 81              ADD     A,C                 ; Add C to score
0223: 27              DAA                         ; Adjust for binary coded decimal
0224: 77              LD      (HL),A              ; Update lowest 2 digits
0225: 2D              DEC     L                   ; Point to middle 2 digits
0226: 7E              LD      A,(HL)              ; Add B to ...
0227: 88              ADC     A,B                 ; ... score
0228: 27              DAA                         ; Adjust for BCD
0229: 77              LD      (HL),A              ; Store the middle 2 digits
022A: 2D              DEC     L                   ; Point to the upper 2 digits
022B: 7E              LD      A,(HL)              ; Add in ...
022C: CE 00           ADC     $00                 ; ... any carry
022E: 27              DAA                         ; Adjust for binary coded decimal
022F: 77              LD      (HL),A              ; Store the upper 2 digits
0230: 2C              INC     L                   ; Restore ...
0231: 2C              INC     L                   ; ... pointer
0232: C9              RET                         ; Done

0233: FF FF FF          

; 3-byte (6 digit) BCD subtraction. This is never called.
;
; !! We have score ADDER above. I like the symmetry of a score SUBTRACTER, but
; !! this is never called. Scores never decrease
;
0236: 37              SCF                         ; Take ...
0237: 3E 99           LD      A,$99               ; ... the BCD ...
0239: CE 00           ADC     $00                 ; ... add-complement ...
023B: 91              SUB     C                   ; ... of C
023C: 86              ADD     A,(HL)              ; Lower two digits
023D: 27              DAA                         ; Adjust for BCD
023E: 77              LD      (HL),A              ; Update lower two digits
023F: 2D              DEC     L                   ; Point to middle digits
0240: 3E 99           LD      A,$99               ; Take the BCD ...
0242: CE 00           ADC     $00                 ; ... add-complement ...
0244: 90              SUB     B                   ; ... of C
0245: 86              ADD     A,(HL)              ; Middle two digits
0246: 27              DAA                         ; Adjust for BCD
0247: 77              LD      (HL),A              ; Update middle two digits
0248: 2D              DEC     L                   ; Point to upper digits
0249: 3E 99           LD      A,$99               ; Take the BCD add-complement ...
024B: CE 00           ADC     $00                 ; ... of any carry
024D: 86              ADD     A,(HL)              ; Upper two digits
024E: 27              DAA                         ; Adjust for BCD
024F: 77              LD      (HL),A              ; Update upper two digits
0250: 2C              INC     L                   ; Restore ...
0251: 2C              INC     L                   ; ... pointer
0252: C9              RET                         ; Done

0253: FF FF FF FF FF         

; Two byte compare of BC to memory at (HL-1):(HL)
;
CompareBCtoMem:
0258: 7E              LD      A,(HL)              ; Value from memory
0259: B9              CP      C                   ; Are the lower values the same?
025A: C0              RET     NZ                  ; No ... return not-zero
025B: 2D              DEC     L                   ; Point to MSB
025C: 7E              LD      A,(HL)              ; Get the MSB value
025D: 2C              INC     L                   ; Restore the pointer
025E: B8              CP      B                   ; Compare the MSBs
025F: C9              RET                         ; Return the flags

; Subtract DE from memory if memory is greater/equal to BC.
;
SubtractIfEnough:
0260: CD 70 02        CALL    $0270               ; {code.SubtractFromMemory} Try subtraction. Is memory larger (or equal) to BC?
0263: D8              RET     C                   ; No ... ignore request
0264: CD 77 02        CALL    $0277               ; {code.SubtractToMemory} Yes ... subtract DE from memory
0267: C9              RET                         ; Done

0268: FF FF FF FF FF FF FF FF          

; Two byte subtraction of memory from BC. BC = BC -  (HL-1):(HL)
;
SubtractFromMemory:
0270: 7E              LD      A,(HL)              ; Get the low byte
0271: 91              SUB     C                   ; Subtract from C
0272: 2D              DEC     L                   ; Point to upper byte
0273: 7E              LD      A,(HL)              ; Get the upper byte
0274: 98              SBC     B                   ; Subtract from B (with borrow)
0275: 2C              INC     L                   ; Restore pointer
0276: C9              RET                         ; Done

; Two byte subtraction of DE from memory. (HL-1):(HL) = (HL-1):(HL) - DE
SubtractToMemory:
0277: 7B              LD      A,E                 ; Lower byte
0278: 96              SUB     (HL)                ; Subtract it from memory
0279: 2D              DEC     L                   ; Point to upper byte
027A: 7A              LD      A,D                 ; Value to A
027B: 9E              SBC     (HL)                ; Subtract upper byte from memory (with borrow)
027C: 2C              INC     L                   ; Restore pointer
027D: C9              RET                         ; Done

027E: FF FF

; Two byte compare of HL to BC
;
CompareHLtoBC:
0280: 7D              LD      A,L                 ; Compare lower ...
0281: B9              CP      C                   ; ... bytes
0282: C0              RET     NZ                  ; Not the same ... return NZ
0283: 7C              LD      A,H                 ; Compare upper ...
0284: B8              CP      B                   ; ... bytes
0285: C9              RET                         ; Return the check

0286: FF FF

0288: CD 40 01        CALL    $0140               ; {}
028B: 21 C0 19        LD      HL,$19C0            
028E: 0E 02           LD      C,$02               
0290: CD D0 01        CALL    $01D0               ; {}
0293: 0E 02           LD      C,$02               
0295: CD E0 17        CALL    $17E0               ; {}
0298: FE 02           CP      $02                 
029A: DA A7 02        JP      C,$02A7             ; {}
029D: 21 A0 1B        LD      HL,$1BA0            
02A0: 0E 01           LD      C,$01               
02A2: CD D0 01        CALL    $01D0               ; {}
02A5: 0E 06           LD      C,$06               
02A7: 3A 00 70        LD      A,($7000)           ; 70xx IN0
02AA: 2F              CPL                         
02AB: A1              AND     C                   
02AC: C8              RET     Z                   
02AD: CD CB 02        CALL    $02CB               ; {}
02B0: CD F0 02        CALL    $02F0               ; {}
02B3: CD 2E 03        CALL    $032E               ; {}
02B6: CD 50 03        CALL    $0350               ; {}
02B9: CD 40 01        CALL    $0140               ; {}
02BC: 26 50           LD      H,$50               ; 50xx video register
02BE: 36 01           LD      (HL),$01            
02C0: CD 40 01        CALL    $0140               ; {}
02C3: 26 50           LD      H,$50               ; 50xx video register
02C5: 36 00           LD      (HL),$00            
02C7: C9              RET                         
02C8: FF              RST     0X38                
02C9: FF              RST     0X38                
02CA: FF              RST     0X38                
02CB: 0E 01           LD      C,$01               
02CD: FE 02           CP      $02                 
02CF: CA D4 02        JP      Z,$02D4             ; {}
02D2: 0E 02           LD      C,$02               
02D4: 21 A2 43        LD      HL,$43A2            
02D7: 71              LD      (HL),C              
02D8: 3A 00 78        LD      A,($7800)           ; 78xx DSW0
02DB: E6 10           AND     $10                 ; Coinage
02DD: CA E3 02        JP      Z,$02E3             ; {}
02E0: 79              LD      A,C                 
02E1: 07              RLCA                        
02E2: 4F              LD      C,A                 
02E3: 2E 8F           LD      L,$8F               
02E5: 7E              LD      A,(HL)              
02E6: 91              SUB     C                   
02E7: 77              LD      (HL),A              
02E8: C6 20           ADD     $20                 
02EA: 32 42 41        LD      ($4142),A           
02ED: C9              RET                         
02EE: FF              RST     0X38                
02EF: FF              RST     0X38                
02F0: 11 83 43        LD      DE,$4383            
02F3: 21 8B 43        LD      HL,$438B            
02F6: CD 14 03        CALL    $0314               ; {}
02F9: D4 20 03        CALL    NC,$0320            ; {}
02FC: 1E 87           LD      E,$87               
02FE: 2E 8B           LD      L,$8B               
0300: CD 14 03        CALL    $0314               ; {}
0303: D4 20 03        CALL    NC,$0320            ; {}
0306: 2E 8B           LD      L,$8B               
0308: 11 41 41        LD      DE,$4141            
030B: 06 06           LD      B,$06               
030D: CD C4 00        CALL    $00C4               ; {}
0310: C9              RET                         
0311: FF              RST     0X38                
0312: FF              RST     0X38                
0313: FF              RST     0X38                
0314: 1A              LD      A,(DE)              
0315: 96              SUB     (HL)                
0316: 1D              DEC     E                   
0317: 2D              DEC     L                   
0318: 1A              LD      A,(DE)              
0319: 9E              SBC     (HL)                
031A: 1D              DEC     E                   
031B: 2D              DEC     L                   
031C: 1A              LD      A,(DE)              
031D: 9E              SBC     (HL)                
031E: C9              RET                         
031F: FF              RST     0X38                
0320: 1A              LD      A,(DE)              
0321: 77              LD      (HL),A              
0322: 13              INC     DE                  
0323: 23              INC     HL                  
0324: 1A              LD      A,(DE)              
0325: 77              LD      (HL),A              
0326: 13              INC     DE                  
0327: 23              INC     HL                  
0328: 1A              LD      A,(DE)              
0329: 77              LD      (HL),A              
032A: C9              RET                         
032B: FF              RST     0X38                
032C: FF              RST     0X38                
032D: FF              RST     0X38                
032E: 21 80 43        LD      HL,$4380            
0331: 36 00           LD      (HL),$00            
0333: 23              INC     HL                  
0334: 7D              LD      A,L                 
0335: FE 88           CP      $88                 
0337: C2 31 03        JP      NZ,$0331            ; {}
033A: 2E 83           LD      L,$83               
033C: 11 61 42        LD      DE,$4261            
033F: 06 06           LD      B,$06               
0341: CD C4 00        CALL    $00C4               ; {}
0344: 2E 87           LD      L,$87               
0346: 11 21 40        LD      DE,$4021            
0349: 06 06           LD      B,$06               
034B: CD C4 00        CALL    $00C4               ; {}
034E: C9              RET                         
034F: FF              RST     0X38                
0350: 3A 00 78        LD      A,($7800)           ; 78xx DSW0
0353: E6 03           AND     $03                 ; Lives
0355: C6 03           ADD     $03                 
0357: 47              LD      B,A                 
0358: 21 90 43        LD      HL,$4390            
035B: 70              LD      (HL),B              
035C: 2E A2           LD      L,$A2               
035E: 7E              LD      A,(HL)              
035F: FE 01           CP      $01                 
0361: CA 67 03        JP      Z,$0367             ; {}
0364: 2E 91           LD      L,$91               
0366: 70              LD      (HL),B              
0367: 2E 90           LD      L,$90               
0369: 7E              LD      A,(HL)              
036A: F6 20           OR      $20                 
036C: 32 A2 42        LD      ($42A2),A           
036F: 2C              INC     L                   
0370: 7E              LD      A,(HL)              
0371: F6 20           OR      $20                 
0373: 32 62 40        LD      ($4062),A           
0376: C9              RET                         

0377: 21 8C 43        LD      HL,$438C            
037A: 77              LD      (HL),A              
037B: 2C              INC     L                   
037C: 77              LD      (HL),A              
037D: C9              RET                         

037E: FF FF

0380: 21 3F 43        LD      HL,$433F            
0383: 11 1F 00        LD      DE,$001F            
0386: 01 3F 03        LD      BC,$033F            
0389: 72              LD      (HL),D              
038A: 2B              DEC     HL                  
038B: 72              LD      (HL),D              
038C: 2B              DEC     HL                  
038D: 7D              LD      A,L                 
038E: A3              AND     E                   
038F: B8              CP      B                   
0390: C2 89 03        JP      NZ,$0389            ; {}
0393: 72              LD      (HL),D              
0394: 2B              DEC     HL                  
0395: 2B              DEC     HL                  
0396: 2B              DEC     HL                  
0397: 2B              DEC     HL                  
0398: 7C              LD      A,H                 
0399: B9              CP      C                   
039A: C2 89 03        JP      NZ,$0389            ; {}
039D: C9              RET                         
039E: FF              RST     0X38                
039F: FF              RST     0X38                
03A0: 21 3F 4B        LD      HL,$4B3F            
03A3: 11 47 00        LD      DE,$0047            
03A6: 72              LD      (HL),D              
03A7: 2B              DEC     HL                  
03A8: 72              LD      (HL),D              
03A9: 2B              DEC     HL                  
03AA: 7C              LD      A,H                 
03AB: BB              CP      E                   
03AC: C2 A6 03        JP      NZ,$03A6            ; {}
03AF: C9              RET                         
03B0: 01 A0 07        LD      BC,$07A0            
03B3: CD 70 02        CALL    $0270               ; {code.SubtractFromMemory}
03B6: DA CE 03        JP      C,$03CE             ; {}
03B9: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
03BC: CA EB 03        JP      Z,$03EB             ; {}
03BF: 01 60 0B        LD      BC,$0B60            
03C2: CD 70 02        CALL    $0270               ; {code.SubtractFromMemory}
03C5: DA CE 03        JP      C,$03CE             ; {}
03C8: CD 58 02        CALL    $0258               ; {code.CompareBCtoMem}
03CB: CA E2 03        JP      Z,$03E2             ; {}
03CE: CD 73 01        CALL    $0173               ; {}
03D1: 21 A0 43        LD      HL,$43A0            
03D4: 7E              LD      A,(HL)              
03D5: E6 01           AND     $01                 
03D7: B0              OR      B                   
03D8: 77              LD      (HL),A              
03D9: C3 00 04        JP      $0400               ; {}
03DC: C3 00 04        JP      $0400               ; {}

03DF: FF FF FF

03E2: 01 08 01        LD      BC,$0108            
03E5: 11 00 10        LD      DE,$1000            
03E8: C3 F1 03        JP      $03F1               ; {}
03EB: 01 04 01        LD      BC,$0104            
03EE: 11 08 00        LD      DE,$0008            
03F1: 21 A4 43        LD      HL,$43A4            
03F4: 70              LD      (HL),B              
03F5: 2E B8           LD      L,$B8               
03F7: 71              LD      (HL),C              
03F8: 2E BA           LD      L,$BA               
03FA: 72              LD      (HL),D              
03FB: 2C              INC     L                   
03FC: 73              LD      (HL),E              
03FD: C9              RET                         

03FE: FF FF          

; Jump to ?? function by number in 43A4
0400: 21 0E 04        LD      HL,$040E            ; Jump table
0403: 3A A4 43        LD      A,($43A4)           ; {ram.M43A4} ??
0406: 07              RLCA                        ; *2
0407: 85              ADD     A,L                 ; Offset ...
0408: 6F              LD      L,A                 ; ... into the table
0409: 7E              LD      A,(HL)              ; MSB of destination
040A: 2C              INC     L                   ; Get the
040B: 6E              LD      L,(HL)              ; ... LSB of destination
040C: 67              LD      H,A                 ; Now point to function
040D: E9              JP      (HL)                ; Jump to function

; Notice these addresses are MSB:LSB (backwards from the processors endianness)
040E: 04 30 
0410: 04 AC                  
0412: 05 15                  
0414: 08 00       ; Restart
0416: 0A EA 
0418: 0B 60             
041A: 24 00                        
041C: 24 4C          

041E: 3A A3 43        LD      A,($43A3)           
0421: E6 01           AND     $01                 
0423: 47              LD      B,A                 
0424: 3A B8 43        LD      A,($43B8)           
0427: E6 02           AND     $02                 
0429: B0              OR      B                   
042A: 32 00 50        LD      ($5000),A           ; 50xx video register
042D: C9              RET                         
042E: 18 05           JR      $435                ; {}

; ?? Function 0
0430: 21 A4 43        LD      HL,$43A4            ; Next function to run ...
0433: 36 01           LD      (HL),$01            ; ... is 1 ??
0435: 2C              INC     L                   
0436: 36 80           LD      (HL),$80            
0438: 2E A3           LD      L,$A3               
043A: 7E              LD      A,(HL)              
043B: 36 00           LD      (HL),$00            
043D: FE 02           CP      $02                 
043F: C8              RET     Z                   
0440: 77              LD      (HL),A              
0441: 2D              DEC     L                   
0442: 7E              LD      A,(HL)              
0443: FE 01           CP      $01                 
0445: C8              RET     Z                   
0446: 2C              INC     L                   
0447: 7E              LD      A,(HL)              
0448: A7              AND     A                   
0449: CA A0 04        JP      Z,$04A0             ; {}
044C: 2E 90           LD      L,$90               
044E: 7E              LD      A,(HL)              
044F: A7              AND     A                   
0450: C8              RET     Z                   
0451: 2E A3           LD      L,$A3               
0453: 36 00           LD      (HL),$00            
0455: 01 00 01        LD      BC,$0100            
0458: CD 60 04        CALL    $0460               ; {}
045B: C9              RET                         

045C: FF              RST     0X38                
045D: FF              RST     0X38                
045E: FF              RST     0X38                
045F: FF              RST     0X38                

; Copy memory bank to bank
; B=from bank number, C=to bank number
; Starts at 4320
0460: 21 00 50        LD      HL,$5000            ; 50xx video register
0463: 11 20 43        LD      DE,$4320            
0466: 70              LD      (HL),B              
0467: 1A              LD      A,(DE)              
0468: 71              LD      (HL),C              
0469: 12              LD      (DE),A              
046A: 1C              INC     E                   
046B: 7B              LD      A,E                 
046C: E6 03           AND     $03                 
046E: C2 66 04        JP      NZ,$0466            ; {}
;
0471: 7B              LD      A,E                 
0472: E6 F0           AND     $F0                 
0474: D6 20           SUB     $20                 
0476: 5F              LD      E,A                 
0477: D2 66 04        JP      NC,$0466            ; {}
047A: 15              DEC     D                   
047B: 7A              LD      A,D                 
047C: FE 3F           CP      $3F                 
047E: C2 66 04        JP      NZ,$0466            ; {}
0481: 11 80 43        LD      DE,$4380            
0484: 70              LD      (HL),B              
0485: 1A              LD      A,(DE)              
0486: 71              LD      (HL),C              
0487: 12              LD      (DE),A              
0488: 1C              INC     E                   
0489: 7B              LD      A,E                 
048A: FE B8           CP      $B8                 
048C: C2 84 04        JP      NZ,$0484            ; {}
;
048F: 11 C0 4B        LD      DE,$4BC0            
0492: 70              LD      (HL),B              
0493: 1A              LD      A,(DE)              
0494: 71              LD      (HL),C              
0495: 12              LD      (DE),A              
0496: 1C              INC     E                   
0497: 7B              LD      A,E                 
0498: FE 00           CP      $00                 
049A: C2 92 04        JP      NZ,$0492            ; {}
049D: C9              RET                         

049E: FF FF

04A0: 2E A3           LD      L,$A3               
04A2: 36 01           LD      (HL),$01            
04A4: 01 01 00        LD      BC,$0001            
04A7: CD 60 04        CALL    $0460               ; {}
04AA: C9              RET                         

04AB: FF

; ?? Function 1
04AC: 21 A5 43        LD      HL,$43A5            
04AF: 35              DEC     (HL)                
04B0: 7E              LD      A,(HL)              
04B1: 2D              DEC     L                   
04B2: 36 02           LD      (HL),$02            
04B4: A7              AND     A                   
04B5: C8              RET     Z                   
04B6: 36 01           LD      (HL),$01            
04B8: FE 7F           CP      $7F                 
04BA: CA F0 07        JP      Z,$07F0             ; {}
04BD: 2E 9A           LD      L,$9A               
04BF: 36 00           LD      (HL),$00            
04C1: 2C              INC     L                   
04C2: 36 00           LD      (HL),$00            
04C4: E6 08           AND     $08                 
04C6: C2 E6 04        JP      NZ,$04E6            ; {}
04C9: CD E8 06        CALL    $06E8               ; {}
04CC: 00              NOP                         
04CD: 21 A3 43        LD      HL,$43A3            
04D0: 7E              LD      A,(HL)              
04D1: A7              AND     A                   
04D2: 2E 83           LD      L,$83               
04D4: 11 61 42        LD      DE,$4261            
04D7: CA DF 04        JP      Z,$04DF             ; {}
04DA: 2E 87           LD      L,$87               
04DC: 11 21 40        LD      DE,$4021            
04DF: 06 06           LD      B,$06               
04E1: CD C4 00        CALL    $00C4               ; {}
04E4: C9              RET                         
04E5: FF              RST     0X38                
04E6: 21 A3 43        LD      HL,$43A3            
04E9: 7E              LD      A,(HL)              
04EA: A7              AND     A                   
04EB: 11 61 42        LD      DE,$4261            
04EE: CA F4 04        JP      Z,$04F4             ; {}
04F1: 11 21 40        LD      DE,$4021            
04F4: 06 06           LD      B,$06               
04F6: CD FB 04        CALL    $04FB               ; {}
04F9: C9              RET                         
04FA: FF              RST     0X38                
04FB: 3E 00           LD      A,$00               
04FD: 12              LD      (DE),A              
04FE: CD 10 02        CALL    $0210               ; {code.AddOneRow}
0501: 05              DEC     B                   
0502: C2 FB 04        JP      NZ,$04FB            ; {}
0505: C9              RET                         
0506: 21 92 43        LD      HL,$4392            
0509: 06 06           LD      B,$06               
050B: CD D8 05        CALL    $05D8               ; {}
050E: 3A 50 4B        LD      A,($4B50)           
0511: 32 94 43        LD      ($4394),A           
0514: C9              RET                         

; ?? Function 2
0515: CD 1E 04        CALL    $041E               ; {}
0518: 21 A4 43        LD      HL,$43A4            
051B: 36 03           LD      (HL),$03            
051D: CD 80 05        CALL    $0580               ; {}
0520: CD 47 05        CALL    $0547               ; {}
0523: CD A0 09        CALL    $09A0               ; {}
0526: CD 32 05        CALL    $0532               ; {}
0529: CD 6C 0A        CALL    $0A6C               ; {}
052C: CD 06 05        CALL    $0506               ; {}
052F: C3 B0 32        JP      $32B0               ; {}
;
0532: 21 50 4B        LD      HL,$4B50            
0535: 06 A0           LD      B,$A0               
0537: CD D8 05        CALL    $05D8               ; {}
053A: CD EC 05        CALL    $05EC               ; {}
053D: CD 50 06        CALL    $0650               ; {}
0540: CD 10 06        CALL    $0610               ; {}
0543: C9              RET                         

0544: FF FF FF

0547: 21 60 05        LD      HL,$0560            
054A: 11 C0 43        LD      DE,$43C0            
054D: 06 20           LD      B,$20               
054F: CD E0 05        CALL    $05E0               ; {}
0552: 21 E0 43        LD      HL,$43E0            
0555: 06 20           LD      B,$20               
0557: CD D8 05        CALL    $05D8               ; {}
055A: C9              RET                         

055B: FF FF FF FF FF 

0560: 0C              INC     C                   
0561: 10 64           DJNZ    $5C7                ; {}
0563: D8              RET     C                   
0564: 00              NOP                         
0565: 50              LD      D,B                 
0566: 00              NOP                         
0567: D0              RET     NC                  
0568: 00              NOP                         
0569: 50              LD      D,B                 
056A: 00              NOP                         
056B: D0              RET     NC                  
056C: 00              NOP                         
056D: 58              LD      E,B                 
056E: 00              NOP                         
056F: 20 00           JR      NZ,$571             ; {}
0571: 58              LD      E,B                 
0572: 00              NOP                         
0573: 20 00           JR      NZ,$575             ; {}
0575: 58              LD      E,B                 
0576: 00              NOP                         
0577: 20 00           JR      NZ,$579             ; {}
0579: 58              LD      E,B                 
057A: 00              NOP                         
057B: 20 00           JR      NZ,$57D             ; {}
057D: 58              LD      E,B                 
057E: 00              NOP                         
057F: 20 21           JR      NZ,$5A2             ; {}
0581: 98              SBC     B                   
0582: 05              DEC     B                   
0583: 3A B8 43        LD      A,($43B8)           
0586: E6 0F           AND     $0F                 
0588: 85              ADD     A,L                 
0589: 6F              LD      L,A                 
058A: 6E              LD      L,(HL)              
058B: 26 05           LD      H,$05               
058D: 11 AB 43        LD      DE,$43AB            
0590: 06 0C           LD      B,$0C               
0592: CD E0 05        CALL    $05E0               ; {}
0595: C9              RET                         
0596: FF              RST     0X38                
0597: FF              RST     0X38                
0598: A8              XOR     B                   
0599: A8              XOR     B                   
059A: C0              RET     NZ                  
059B: C0              RET     NZ                  
059C: A8              XOR     B                   
059D: A8              XOR     B                   
059E: A8              XOR     B                   
059F: A8              XOR     B                   
05A0: B4              OR      H                   
05A1: CC B4 B4        CALL    Z,$B4B4             
05A4: A8              XOR     B                   
05A5: A8              XOR     B                   
05A6: A8              XOR     B                   
05A7: A8              XOR     B                   
05A8: 80              ADD     A,B                 
05A9: 7F              LD      A,A                 
05AA: 00              NOP                         
05AB: 00              NOP                         
05AC: 40              LD      B,B                 
05AD: 3F              CCF                         
05AE: 00              NOP                         
05AF: 1C              INC     E                   
05B0: 00              NOP                         
05B1: FF              RST     0X38                
05B2: FF              RST     0X38                
05B3: FF              RST     0X38                
05B4: 60              LD      H,B                 
05B5: 5F              LD      E,A                 
05B6: 01 02 30        LD      BC,$3002            
05B9: 2F              CPL                         
05BA: 00              NOP                         
05BB: 1C              INC     E                   
05BC: 00              NOP                         
05BD: C0              RET     NZ                  
05BE: FF              RST     0X38                
05BF: FF              RST     0X38                
05C0: 80              ADD     A,B                 
05C1: 7F              LD      A,A                 
05C2: 03              INC     BC                  
05C3: 04              INC     B                   
05C4: 40              LD      B,B                 
05C5: 3F              CCF                         
05C6: 00              NOP                         
05C7: 1F              RRA                         
05C8: 00              NOP                         
05C9: A0              AND     B                   
05CA: FF              RST     0X38                
05CB: FF              RST     0X38                
05CC: 60              LD      H,B                 
05CD: 60              LD      H,B                 
05CE: 05              DEC     B                   
05CF: 06 50           LD      B,$50               
05D1: 30 00           JR      NC,$5D3             ; {}
05D3: 1D              DEC     E                   
05D4: 00              NOP                         
05D5: 48              LD      C,B                 
05D6: FF              RST     0X38                
05D7: FF              RST     0X38                
05D8: AF              XOR     A                   
05D9: 77              LD      (HL),A              
05DA: 23              INC     HL                  
05DB: 05              DEC     B                   
05DC: C2 D9 05        JP      NZ,$05D9            ; {}
05DF: C9              RET                         
05E0: 7E              LD      A,(HL)              
05E1: 12              LD      (DE),A              
05E2: 23              INC     HL                  
05E3: 13              INC     DE                  
05E4: 05              DEC     B                   
05E5: C2 E0 05        JP      NZ,$05E0            ; {}
05E8: C9              RET                         
05E9: FF              RST     0X38                
05EA: FF              RST     0X38                
05EB: FF              RST     0X38                
05EC: 21 00 15        LD      HL,$1500            
05EF: 3A B8 43        LD      A,($43B8)           
05F2: E6 0F           AND     $0F                 
05F4: 07              RLCA                        
05F5: 85              ADD     A,L                 
05F6: 6F              LD      L,A                 
05F7: 56              LD      D,(HL)              
05F8: 23              INC     HL                  
05F9: 5E              LD      E,(HL)              
05FA: 21 70 4B        LD      HL,$4B70            
05FD: 3A BA 43        LD      A,($43BA)           
0600: 47              LD      B,A                 
0601: A7              AND     A                   
0602: C8              RET     Z                   
0603: 72              LD      (HL),D              
0604: 2C              INC     L                   
0605: 73              LD      (HL),E              
0606: 2C              INC     L                   
0607: 2C              INC     L                   
0608: 2C              INC     L                   
0609: 05              DEC     B                   
060A: C2 03 06        JP      NZ,$0603            ; {}
060D: C9              RET                         
060E: FF              RST     0X38                
060F: FF              RST     0X38                
0610: 21 3A 06        LD      HL,$063A            
0613: 3A B8 43        LD      A,($43B8)           
0616: 0F              RRCA                        
0617: E6 0F           AND     $0F                 
0619: 85              ADD     A,L                 
061A: 6F              LD      L,A                 
061B: 00              NOP                         
061C: 00              NOP                         
061D: 00              NOP                         
061E: 6E              LD      L,(HL)              
061F: 26 15           LD      H,$15               
0621: 11 72 4B        LD      DE,$4B72            
0624: 3A BA 43        LD      A,($43BA)           
0627: 47              LD      B,A                 
0628: A7              AND     A                   
0629: C8              RET     Z                   
062A: 7E              LD      A,(HL)              
062B: 12              LD      (DE),A              
062C: 23              INC     HL                  
062D: 13              INC     DE                  
062E: 7E              LD      A,(HL)              
062F: 12              LD      (DE),A              
0630: 23              INC     HL                  
0631: 13              INC     DE                  
0632: 13              INC     DE                  
0633: 13              INC     DE                  
0634: 05              DEC     B                   
0635: C2 2A 06        JP      NZ,$062A            ; {}
0638: C9              RET                         
0639: FF              RST     0X38                
063A: 60              LD      H,B                 
063B: 40              LD      B,B                 
063C: E0              RET     PO                  
063D: E0              RET     PO                  
063E: E0              RET     PO                  
063F: E0              RET     PO                  
0640: FF              RST     0X38                
0641: FF              RST     0X38                
0642: C0              RET     NZ                  
0643: A0              AND     B                   
0644: 80              ADD     A,B                 
0645: 80              ADD     A,B                 
0646: 80              ADD     A,B                 
0647: 80              ADD     A,B                 
0648: FF              RST     0X38                
0649: FF              RST     0X38                
064A: FF              RST     0X38                
064B: FF              RST     0X38                
064C: FF              RST     0X38                
064D: FF              RST     0X38                
064E: FF              RST     0X38                
064F: FF              RST     0X38                
0650: 21 20 15        LD      HL,$1520            
0653: 3A B8 43        LD      A,($43B8)           
0656: E6 0F           AND     $0F                 
0658: 07              RLCA                        
0659: 85              ADD     A,L                 
065A: 6F              LD      L,A                 
065B: 56              LD      D,(HL)              
065C: 23              INC     HL                  
065D: 5E              LD      E,(HL)              
065E: 21 50 4B        LD      HL,$4B50            
0661: 3A BA 43        LD      A,($43BA)           
0664: 47              LD      B,A                 
0665: A7              AND     A                   
0666: C8              RET     Z                   
0667: 72              LD      (HL),D              
0668: 2C              INC     L                   
0669: 73              LD      (HL),E              
066A: 2C              INC     L                   
066B: 05              DEC     B                   
066C: C2 67 06        JP      NZ,$0667            ; {}
066F: C9              RET                         
0670: 21 B1 43        LD      HL,$43B1            
0673: 46              LD      B,(HL)              
0674: 2E B9           LD      L,$B9               
0676: 4E              LD      C,(HL)              
0677: 79              LD      A,C                 
0678: 90              SUB     B                   
0679: 77              LD      (HL),A              
067A: 21 B9 43        LD      HL,$43B9            
067D: 7E              LD      A,(HL)              
067E: 35              DEC     (HL)                
067F: 32 00 58        LD      ($5800),A           ; 58xx scroll register
0682: E6 07           AND     $07                 
0684: C0              RET     NZ                  
0685: 01 47 20        LD      BC,$2047            
0688: 11 21 4B        LD      DE,$4B21            
068B: 7E              LD      A,(HL)              
068C: 0F              RRCA                        
068D: 0F              RRCA                        
068E: 0F              RRCA                        
068F: E6 1F           AND     $1F                 
0691: 83              ADD     A,E                 
0692: 5F              LD      E,A                 
0693: 2E B2           LD      L,$B2               
0695: 7E              LD      A,(HL)              
0696: 2C              INC     L                   
0697: 6E              LD      L,(HL)              
0698: 67              LD      H,A                 
0699: 7E              LD      A,(HL)              
069A: 12              LD      (DE),A              
069B: 2C              INC     L                   
069C: 7B              LD      A,E                 
069D: 90              SUB     B                   
069E: 5F              LD      E,A                 
069F: D2 99 06        JP      NC,$0699            ; {}
06A2: 15              DEC     D                   
06A3: 7A              LD      A,D                 
06A4: B9              CP      C                   
06A5: C2 99 06        JP      NZ,$0699            ; {}
06A8: 7D              LD      A,L                 
06A9: 32 B3 43        LD      ($43B3),A           
06AC: C9              RET                         
06AD: FF              RST     0X38                
06AE: FF              RST     0X38                
06AF: FF              RST     0X38                
06B0: 21 AB 43        LD      HL,$43AB            
06B3: 3A B9 43        LD      A,($43B9)           
06B6: 4F              LD      C,A                 
06B7: BE              CP      (HL)                
06B8: C0              RET     NZ                  
06B9: 7E              LD      A,(HL)              
06BA: 2C              INC     L                   
06BB: 86              ADD     A,(HL)              
06BC: 2D              DEC     L                   
06BD: 77              LD      (HL),A              
06BE: 2C              INC     L                   
06BF: 2C              INC     L                   
06C0: 34              INC     (HL)                
06C1: 46              LD      B,(HL)              
06C2: 2C              INC     L                   
06C3: 34              INC     (HL)                
06C4: 7E              LD      A,(HL)              
06C5: 21 20 1E        LD      HL,$1E20            
06C8: E6 1F           AND     $1F                 
06CA: 85              ADD     A,L                 
06CB: 6F              LD      L,A                 
06CC: 56              LD      D,(HL)              
06CD: C6 20           ADD     $20                 
06CF: 6F              LD      L,A                 
06D0: 5E              LD      E,(HL)              
06D1: 79              LD      A,C                 
06D2: 0F              RRCA                        
06D3: 0F              RRCA                        
06D4: 0F              RRCA                        
06D5: E6 1E           AND     $1E                 
06D7: 83              ADD     A,E                 
06D8: C6 02           ADD     $02                 
06DA: 5F              LD      E,A                 
06DB: 21 60 1E        LD      HL,$1E60            
06DE: 78              LD      A,B                 
06DF: E6 1F           AND     $1F                 
06E1: 85              ADD     A,L                 
06E2: 6F              LD      L,A                 
06E3: 6E              LD      L,(HL)              
06E4: CD DC 07        CALL    $07DC               ; {}
06E7: C9              RET                         
06E8: 21 00 18        LD      HL,$1800            
06EB: 0E 01           LD      C,$01               
06ED: C3 D0 01        JP      $01D0               ; {}
06F0: CD 7A 06        CALL    $067A               ; {}
06F3: CD 40 20        CALL    $2040               ; {}
06F6: C3 B0 06        JP      $06B0               ; {}
06F9: FF              RST     0X38                
06FA: FF              RST     0X38                
06FB: FF              RST     0X38                
06FC: FF              RST     0X38                
06FD: FF              RST     0X38                
06FE: FF              RST     0X38                
06FF: FF              RST     0X38                
0700: 01 C0 43        LD      BC,$43C0            
0703: 11 E0 43        LD      DE,$43E0            
0706: CD 18 07        CALL    $0718               ; {}
0709: 79              LD      A,C                 
070A: C6 04           ADD     $04                 
070C: 4F              LD      C,A                 
070D: C6 20           ADD     $20                 
070F: 5F              LD      E,A                 
0710: 50              LD      D,B                 
0711: FE EC           CP      $EC                 
0713: C2 06 07        JP      NZ,$0706            ; {}
0716: C9              RET                         
0717: C9              RET                         
0718: CD 20 07        CALL    $0720               ; {}
071B: C3 40 07        JP      $0740               ; {}
071E: E6 EF           AND     $EF                 
0720: 0A              LD      A,(BC)              
0721: 67              LD      H,A                 
0722: E6 10           AND     $10                 
0724: C8              RET     Z                   
0725: 7C              LD      A,H                 
0726: E6 EF           AND     $EF                 
0728: 02              LD      (BC),A              
0729: 07              RLCA                        
072A: 07              RLCA                        
072B: 07              RLCA                        
072C: E6 07           AND     $07                 
072E: C6 38           ADD     $38                 
0730: 6F              LD      L,A                 
0731: 26 07           LD      H,$07               
0733: 6E              LD      L,(HL)              
0734: E9              JP      (HL)                
0735: 6C              LD      L,H                 
0736: FF              RST     0X38                
0737: 8A              ADC     A,D                 
0738: 63              LD      H,E                 
0739: 79              LD      A,C                 
073A: FF              RST     0X38                
073B: 9E              SBC     (HL)                
073C: BE              CP      (HL)                
073D: FF              RST     0X38                
073E: FF              RST     0X38                
073F: FF              RST     0X38                
0740: 0A              LD      A,(BC)              
0741: 67              LD      H,A                 
0742: E6 08           AND     $08                 
0744: C8              RET     Z                   
0745: 7C              LD      A,H                 
0746: E6 07           AND     $07                 
0748: 67              LD      H,A                 
0749: 0F              RRCA                        
074A: 0F              RRCA                        
074B: 0F              RRCA                        
074C: B4              OR      H                   
074D: F6 18           OR      $18                 
074F: 02              LD      (BC),A              
0750: 03              INC     BC                  
0751: 7C              LD      A,H                 
0752: C6 5B           ADD     $5B                 
0754: 6F              LD      L,A                 
0755: 26 07           LD      H,$07               
0757: 6E              LD      L,(HL)              
0758: E9              JP      (HL)                
0759: 5E              LD      E,(HL)              
075A: 0A              LD      A,(BC)              
075B: 6D              LD      L,L                 
075C: 88              ADC     A,B                 
075D: FF              RST     0X38                
075E: AA              XOR     D                   
075F: D2 FF FF        JP      NC,$FFFF            
0762: FF              RST     0X38                
0763: EB              EX      DE,HL               
0764: 56              LD      D,(HL)              
0765: 23              INC     HL                  
0766: 5E              LD      E,(HL)              
0767: 2B              DEC     HL                  
0768: AF              XOR     A                   
0769: 12              LD      (DE),A              
076A: EB              EX      DE,HL               
076B: C9              RET                         
076C: EB              EX      DE,HL               
076D: EB              EX      DE,HL               
076E: 23              INC     HL                  
076F: 23              INC     HL                  
0770: 56              LD      D,(HL)              
0771: 23              INC     HL                  
0772: 5E              LD      E,(HL)              
0773: 0A              LD      A,(BC)              
0774: 12              LD      (DE),A              
0775: 0B              DEC     BC                  
0776: C9              RET                         
0777: 12              LD      (DE),A              
0778: 23              INC     HL                  
0779: EB              EX      DE,HL               
077A: 56              LD      D,(HL)              
077B: 23              INC     HL                  
077C: 5E              LD      E,(HL)              
077D: 2B              DEC     HL                  
077E: AF              XOR     A                   
077F: 12              LD      (DE),A              
0780: CD 17 02        CALL    $0217               ; {code.SubtractOneRow}
0783: AF              XOR     A                   
0784: 12              LD      (DE),A              
0785: EB              EX      DE,HL               
0786: C9              RET                         
0787: 23              INC     HL                  
0788: EB              EX      DE,HL               
0789: 23              INC     HL                  
078A: 23              INC     HL                  
078B: 56              LD      D,(HL)              
078C: 23              INC     HL                  
078D: 5E              LD      E,(HL)              
078E: 0A              LD      A,(BC)              
078F: 6F              LD      L,A                 
0790: 26 14           LD      H,$14               
0792: 7E              LD      A,(HL)              
0793: 12              LD      (DE),A              
0794: 23              INC     HL                  
0795: CD 17 02        CALL    $0217               ; {code.SubtractOneRow}
0798: 7E              LD      A,(HL)              
0799: 12              LD      (DE),A              
079A: 0B              DEC     BC                  
079B: C9              RET                         
079C: FF              RST     0X38                
079D: EB              EX      DE,HL               
079E: EB              EX      DE,HL               
079F: 56              LD      D,(HL)              
07A0: 23              INC     HL                  
07A1: 5E              LD      E,(HL)              
07A2: 2B              DEC     HL                  
07A3: AF              XOR     A                   
07A4: 12              LD      (DE),A              
07A5: 13              INC     DE                  
07A6: 12              LD      (DE),A              
07A7: EB              EX      DE,HL               
07A8: C9              RET                         
07A9: FF              RST     0X38                
07AA: EB              EX      DE,HL               
07AB: 23              INC     HL                  
07AC: 23              INC     HL                  
07AD: 56              LD      D,(HL)              
07AE: 23              INC     HL                  
07AF: 5E              LD      E,(HL)              
07B0: 0A              LD      A,(BC)              
07B1: 6F              LD      L,A                 
07B2: 26 14           LD      H,$14               
07B4: 7E              LD      A,(HL)              
07B5: 12              LD      (DE),A              
07B6: 23              INC     HL                  
07B7: 13              INC     DE                  
07B8: 7E              LD      A,(HL)              
07B9: 12              LD      (DE),A              
07BA: 0B              DEC     BC                  
07BB: C9              RET                         
07BC: 23              INC     HL                  
07BD: 13              INC     DE                  
07BE: EB              EX      DE,HL               
07BF: 56              LD      D,(HL)              
07C0: 23              INC     HL                  
07C1: 5E              LD      E,(HL)              
07C2: 2B              DEC     HL                  
07C3: AF              XOR     A                   
07C4: 12              LD      (DE),A              
07C5: 13              INC     DE                  
07C6: 12              LD      (DE),A              
07C7: CD 17 02        CALL    $0217               ; {code.SubtractOneRow}
07CA: AF              XOR     A                   
07CB: 12              LD      (DE),A              
07CC: 1B              DEC     DE                  
07CD: 12              LD      (DE),A              
07CE: EB              EX      DE,HL               
07CF: C9              RET                         
07D0: CD 4C EB        CALL    $EB4C               
07D3: 23              INC     HL                  
07D4: 23              INC     HL                  
07D5: 56              LD      D,(HL)              
07D6: 23              INC     HL                  
07D7: 5E              LD      E,(HL)              
07D8: 0A              LD      A,(BC)              
07D9: 6F              LD      L,A                 
07DA: 26 14           LD      H,$14               
07DC: 7E              LD      A,(HL)              
07DD: 12              LD      (DE),A              
07DE: 23              INC     HL                  
07DF: 13              INC     DE                  
07E0: 7E              LD      A,(HL)              
07E1: 12              LD      (DE),A              
07E2: 23              INC     HL                  
07E3: 1B              DEC     DE                  
07E4: CD 17 02        CALL    $0217               ; {code.SubtractOneRow}
07E7: 7E              LD      A,(HL)              
07E8: 12              LD      (DE),A              
07E9: 23              INC     HL                  
07EA: 13              INC     DE                  
07EB: 7E              LD      A,(HL)              
07EC: 12              LD      (DE),A              
07ED: 0B              DEC     BC                  
07EE: C9              RET                         
07EF: FF              RST     0X38                
07F0: 3A B9 43        LD      A,($43B9)           
07F3: 32 00 58        LD      ($5800),A           ; 58xx scroll register
07F6: CD 80 03        CALL    $0380               ; {}
07F9: C3 1E 04        JP      $041E               ; {}
07FC: FF              RST     0X38                
07FD: FF              RST     0X38                
07FE: FF              RST     0X38                
07FF: FF              RST     0X38                
0800: 21 14 08        LD      HL,$0814            
0803: 3A B8 43        LD      A,($43B8)           
0806: 07              RLCA                        
0807: E6 1E           AND     $1E                 
0809: 85              ADD     A,L                 
080A: 6F              LD      L,A                 
080B: 7E              LD      A,(HL)              
080C: 2C              INC     L                   
080D: 6E              LD      L,(HL)              
080E: 67              LD      H,A                 
080F: E9              JP      (HL)                
0810: FF              RST     0X38                
0811: FF              RST     0X38                
0812: FF              RST     0X38                
0813: FF              RST     0X38                
0814: 08              EX      AF,AF'              
0815: 34              INC     (HL)                
0816: 20 00           JR      NZ,$818             ; {}
0818: 08              EX      AF,AF'              
0819: 34              INC     (HL)                
081A: 20 00           JR      NZ,$81C             ; {}
081C: 22 30 34        LD      ($3430),HL          ; {}
081F: 00              NOP                         
0820: 22 30 34        LD      ($3430),HL          ; {}
0823: 00              NOP                         
0824: 22 30 22        LD      ($2230),HL          ; {}
0827: B4              OR      H                   
0828: 22 CA 20        LD      ($20CA),HL          ; {}
082B: 00              NOP                         
082C: 22 4C 22        LD      ($224C),HL          ; {}
082F: 4C              LD      C,H                 
0830: 22 4C 22        LD      ($224C),HL          ; {}
0833: 4C              LD      C,H                 
0834: CD F0 06        CALL    $06F0               ; {}
0837: 21 B4 43        LD      HL,$43B4            
083A: 35              DEC     (HL)                
083B: 7E              LD      A,(HL)              
083C: FE 15           CP      $15                 
083E: D0              RET     NC                  
083F: CD 5A 08        CALL    $085A               ; {}
0842: CD FA 05        CALL    $05FA               ; {}
0845: CD 50 0A        CALL    $0A50               ; {}
0848: 21 B4 43        LD      HL,$43B4            
084B: 7E              LD      A,(HL)              
084C: A7              AND     A                   
084D: C0              RET     NZ                  
084E: 2E B8           LD      L,$B8               
0850: 34              INC     (HL)                
0851: 2E A4           LD      L,$A4               
0853: 36 02           LD      (HL),$02            
0855: C9              RET                         
0856: FF              RST     0X38                
0857: FF              RST     0X38                
0858: FF              RST     0X38                
0859: FF              RST     0X38                
085A: 11 6C 08        LD      DE,$086C            
085D: FE 11           CP      $11                 
085F: D0              RET     NC                  
0860: 1E 6D           LD      E,$6D               
0862: FE 0D           CP      $0D                 
0864: D0              RET     NC                  
0865: 1E 6E           LD      E,$6E               
0867: FE 09           CP      $09                 
0869: D0              RET     NC                  
086A: 1E 6F           LD      E,$6F               
086C: FE 05           CP      $05                 
086E: D0              RET     NC                  
086F: 1E 68           LD      E,$68               
0871: C9              RET                         
0872: FF              RST     0X38                
0873: FF              RST     0X38                
0874: FF              RST     0X38                
0875: FF              RST     0X38                
0876: CD 00 07        CALL    $0700               ; {}
0879: CD 86 08        CALL    $0886               ; {}
087C: CD A0 08        CALL    $08A0               ; {}
087F: CD A0 09        CALL    $09A0               ; {}
0882: CD 7A 09        CALL    $097A               ; {}
0885: C9              RET                         
0886: 21 EB 43        LD      HL,$43EB            
0889: 06 03           LD      B,$03               
088B: 56              LD      D,(HL)              
088C: 2B              DEC     HL                  
088D: 5E              LD      E,(HL)              
088E: 2B              DEC     HL                  
088F: 72              LD      (HL),D              
0890: 2B              DEC     HL                  
0891: 73              LD      (HL),E              
0892: 2B              DEC     HL                  
0893: 05              DEC     B                   
0894: C2 8B 08        JP      NZ,$088B            ; {}
0897: C9              RET                         
0898: FF              RST     0X38                
0899: FF              RST     0X38                
089A: FF              RST     0X38                
089B: FF              RST     0X38                
089C: FF              RST     0X38                
089D: FF              RST     0X38                
089E: FF              RST     0X38                
089F: FF              RST     0X38                
08A0: CD C4 08        CALL    $08C4               ; {}
08A3: 21 C4 43        LD      HL,$43C4            
08A6: CD 30 09        CALL    $0930               ; {}
08A9: 3A B8 43        LD      A,($43B8)           
08AC: E6 0F           AND     $0F                 
08AE: FE 03           CP      $03                 
08B0: C0              RET     NZ                  
08B1: 21 C8 43        LD      HL,$43C8            
08B4: CD 30 09        CALL    $0930               ; {}
08B7: C9              RET                         
08B8: FF              RST     0X38                
08B9: FF              RST     0X38                
08BA: FF              RST     0X38                
08BB: FF              RST     0X38                
08BC: FF              RST     0X38                
08BD: FF              RST     0X38                
08BE: FF              RST     0X38                
08BF: FF              RST     0X38                
08C0: FF              RST     0X38                
08C1: FF              RST     0X38                
08C2: FF              RST     0X38                
08C3: FF              RST     0X38                
08C4: 21 C0 43        LD      HL,$43C0            
08C7: 7E              LD      A,(HL)              
08C8: E6 08           AND     $08                 
08CA: CA A0 0A        JP      Z,$0AA0             ; {}
08CD: 2E A6           LD      L,$A6               
08CF: 7E              LD      A,(HL)              
08D0: A7              AND     A                   
08D1: C2 EA 08        JP      NZ,$08EA            ; {}
08D4: 06 80           LD      B,$80               
08D6: CD BB 00        CALL    $00BB               ; {code.CheckInputBits}
08D9: CA EB 08        JP      Z,$08EB             ; {}
08DC: 2E 62           LD      L,$62               
08DE: 36 40           LD      (HL),$40            
08E0: 2E C0           LD      L,$C0               
08E2: 7E              LD      A,(HL)              
08E3: E6 F7           AND     $F7                 
08E5: 77              LD      (HL),A              
08E6: 2E A6           LD      L,$A6               
08E8: 36 FF           LD      (HL),$FF            
08EA: 35              DEC     (HL)                
08EB: 2E C2           LD      L,$C2               
08ED: CD 00 09        CALL    $0900               ; {}
08F0: 01 00 16        LD      BC,$1600            
08F3: C3 26 09        JP      $0926               ; {}
08F6: FF              RST     0X38                
08F7: FF              RST     0X38                
08F8: FF              RST     0X38                
08F9: FF              RST     0X38                
08FA: FF              RST     0X38                
08FB: FF              RST     0X38                
08FC: FF              RST     0X38                
08FD: FF              RST     0X38                
08FE: FF              RST     0X38                
08FF: FF              RST     0X38                
0900: 3A A0 43        LD      A,($43A0)           ; {ram.IN0Current}
0903: 2F              CPL                         
0904: E6 60           AND     $60                 
0906: C8              RET     Z                   
0907: E6 40           AND     $40                 
0909: CA 17 09        JP      Z,$0917             ; {}
090C: 7E              LD      A,(HL)              
090D: FE 0D           CP      $0D                 
090F: D8              RET     C                   
0910: 35              DEC     (HL)                
0911: 3E FF           LD      A,$FF               
0913: 32 60 43        LD      ($4360),A           
0916: C9              RET                         
0917: 7E              LD      A,(HL)              
0918: FE C0           CP      $C0                 
091A: D0              RET     NC                  
091B: 34              INC     (HL)                
091C: 3E FF           LD      A,$FF               
091E: 32 60 43        LD      ($4360),A           
0921: C9              RET                         
0922: FF              RST     0X38                
0923: FF              RST     0X38                
0924: FF              RST     0X38                
0925: FF              RST     0X38                
0926: 7E              LD      A,(HL)              
0927: E6 07           AND     $07                 
0929: 81              ADD     A,C                 
092A: 4F              LD      C,A                 
092B: 0A              LD      A,(BC)              
092C: 2D              DEC     L                   
092D: 77              LD      (HL),A              
092E: C9              RET                         
092F: FF              RST     0X38                
0930: 7E              LD      A,(HL)              
0931: E6 08           AND     $08                 
0933: C2 64 09        JP      NZ,$0964            ; {}
0936: EB              EX      DE,HL               
0937: 06 10           LD      B,$10               
0939: CD BB 00        CALL    $00BB               ; {code.CheckInputBits}
093C: C8              RET     Z                   
093D: 7E              LD      A,(HL)              
093E: E6 EF           AND     $EF                 
0940: 77              LD      (HL),A              
0941: 1A              LD      A,(DE)              
0942: F6 08           OR      $08                 
0944: 12              LD      (DE),A              
0945: 13              INC     DE                  
0946: 13              INC     DE                  
0947: 3A C2 43        LD      A,($43C2)           
094A: C6 04           ADD     $04                 
094C: 12              LD      (DE),A              
094D: 13              INC     DE                  
094E: 3A C3 43        LD      A,($43C3)           
0951: D6 08           SUB     $08                 
0953: 12              LD      (DE),A              
0954: 1B              DEC     DE                  
0955: EB              EX      DE,HL               
0956: 01 20 16        LD      BC,$1620            
0959: CD 26 09        CALL    $0926               ; {}
095C: 3E 30           LD      A,$30               
095E: 32 61 43        LD      ($4361),A           
0961: C9              RET                         
0962: FF              RST     0X38                
0963: FF              RST     0X38                
0964: 2C              INC     L                   
0965: 2C              INC     L                   
0966: 2C              INC     L                   
0967: 7E              LD      A,(HL)              
0968: D6 08           SUB     $08                 
096A: 77              LD      (HL),A              
096B: FE 1F           CP      $1F                 
096D: D0              RET     NC                  
096E: 2D              DEC     L                   
096F: 2D              DEC     L                   
0970: 2D              DEC     L                   
0971: 7E              LD      A,(HL)              
0972: E6 F7           AND     $F7                 
0974: 77              LD      (HL),A              
0975: C9              RET                         
0976: FF              RST     0X38                
0977: FF              RST     0X38                
0978: 7E              LD      A,(HL)              
0979: E6 3A           AND     $3A                 
097B: C2 43 47        JP      NZ,$4743            
097E: E6 07           AND     $07                 
0980: 07              RLCA                        
0981: 21 38 0B        LD      HL,$0B38            
0984: 85              ADD     A,L                 
0985: 6F              LD      L,A                 
0986: 78              LD      A,B                 
0987: 96              SUB     (HL)                
0988: 32 9E 43        LD      ($439E),A           
098B: 23              INC     HL                  
098C: 78              LD      A,B                 
098D: 86              ADD     A,(HL)              
098E: 32 9F 43        LD      ($439F),A           
0991: C9              RET                         
0992: 32 9F 43        LD      ($439F),A           
0995: C9              RET                         
0996: FF              RST     0X38                
0997: FF              RST     0X38                
0998: FF              RST     0X38                
0999: FF              RST     0X38                
099A: FF              RST     0X38                
099B: FF              RST     0X38                
099C: FF              RST     0X38                
099D: FF              RST     0X38                
099E: FF              RST     0X38                
099F: FF              RST     0X38                
09A0: 01 C2 43        LD      BC,$43C2            
09A3: 11 E2 43        LD      DE,$43E2            
09A6: CD BA 09        CALL    $09BA               ; {}
09A9: 03              INC     BC                  
09AA: 03              INC     BC                  
09AB: 03              INC     BC                  
09AC: 13              INC     DE                  
09AD: 13              INC     DE                  
09AE: 13              INC     DE                  
09AF: 79              LD      A,C                 
09B0: FE CE           CP      $CE                 
09B2: C2 A6 09        JP      NZ,$09A6            ; {}
09B5: C9              RET                         
09B6: FF              RST     0X38                
09B7: FF              RST     0X38                
09B8: FF              RST     0X38                
09B9: FF              RST     0X38                
09BA: 21 00 0A        LD      HL,$0A00            
09BD: 0A              LD      A,(BC)              
09BE: E6 F8           AND     $F8                 
09C0: 0F              RRCA                        
09C1: 0F              RRCA                        
09C2: 85              ADD     A,L                 
09C3: 6F              LD      L,A                 
09C4: 7E              LD      A,(HL)              
09C5: 12              LD      (DE),A              
09C6: 03              INC     BC                  
09C7: 13              INC     DE                  
09C8: 23              INC     HL                  
09C9: 0A              LD      A,(BC)              
09CA: E6 F8           AND     $F8                 
09CC: 0F              RRCA                        
09CD: 0F              RRCA                        
09CE: 0F              RRCA                        
09CF: 86              ADD     A,(HL)              
09D0: 12              LD      (DE),A              
09D1: C9              RET                         
09D2: FF              RST     0X38                
09D3: FF              RST     0X38                
09D4: FF              RST     0X38                
09D5: FF              RST     0X38                
09D6: FF              RST     0X38                
09D7: FF              RST     0X38                
09D8: FF              RST     0X38                
09D9: FF              RST     0X38                
09DA: FF              RST     0X38                
09DB: FF              RST     0X38                
09DC: FF              RST     0X38                
09DD: FF              RST     0X38                
09DE: FF              RST     0X38                
09DF: FF              RST     0X38                
09E0: FF              RST     0X38                
09E1: FF              RST     0X38                
09E2: FF              RST     0X38                
09E3: FF              RST     0X38                
09E4: FF              RST     0X38                
09E5: FF              RST     0X38                
09E6: FF              RST     0X38                
09E7: FF              RST     0X38                
09E8: FF              RST     0X38                
09E9: FF              RST     0X38                
09EA: FF              RST     0X38                
09EB: FF              RST     0X38                
09EC: FF              RST     0X38                
09ED: FF              RST     0X38                
09EE: FF              RST     0X38                
09EF: FF              RST     0X38                
09F0: FF              RST     0X38                
09F1: FF              RST     0X38                
09F2: FF              RST     0X38                
09F3: FF              RST     0X38                
09F4: FF              RST     0X38                
09F5: FF              RST     0X38                
09F6: FF              RST     0X38                
09F7: FF              RST     0X38                
09F8: FF              RST     0X38                
09F9: FF              RST     0X38                
09FA: FF              RST     0X38                
09FB: FF              RST     0X38                
09FC: FF              RST     0X38                
09FD: FF              RST     0X38                
09FE: FF              RST     0X38                
09FF: FF              RST     0X38                
0A00: 43              LD      B,E                 
0A01: 20 43           JR      NZ,$A46             ; {}
0A03: 00              NOP                         
0A04: 42              LD      B,D                 
0A05: E0              RET     PO                  
0A06: 42              LD      B,D                 
0A07: C0              RET     NZ                  
0A08: 42              LD      B,D                 
0A09: A0              AND     B                   
0A0A: 42              LD      B,D                 
0A0B: 80              ADD     A,B                 
0A0C: 42              LD      B,D                 
0A0D: 60              LD      H,B                 
0A0E: 42              LD      B,D                 
0A0F: 40              LD      B,B                 
0A10: 42              LD      B,D                 
0A11: 20 42           JR      NZ,$A55             ; {}
0A13: 00              NOP                         
0A14: 41              LD      B,C                 
0A15: E0              RET     PO                  
0A16: 41              LD      B,C                 
0A17: C0              RET     NZ                  
0A18: 41              LD      B,C                 
0A19: A0              AND     B                   
0A1A: 41              LD      B,C                 
0A1B: 80              ADD     A,B                 
0A1C: 41              LD      B,C                 
0A1D: 60              LD      H,B                 
0A1E: 41              LD      B,C                 
0A1F: 40              LD      B,B                 
0A20: 41              LD      B,C                 
0A21: 20 41           JR      NZ,$A64             ; {}
0A23: 00              NOP                         
0A24: 40              LD      B,B                 
0A25: E0              RET     PO                  
0A26: 40              LD      B,B                 
0A27: C0              RET     NZ                  
0A28: 40              LD      B,B                 
0A29: A0              AND     B                   
0A2A: 40              LD      B,B                 
0A2B: 80              ADD     A,B                 
0A2C: 40              LD      B,B                 
0A2D: 60              LD      H,B                 
0A2E: 40              LD      B,B                 
0A2F: 40              LD      B,B                 
0A30: 40              LD      B,B                 
0A31: 20 40           JR      NZ,$A73             ; {}
0A33: 00              NOP                         
0A34: 00              NOP                         
0A35: 00              NOP                         
0A36: 00              NOP                         
0A37: 00              NOP                         
0A38: 00              NOP                         
0A39: 00              NOP                         
0A3A: 00              NOP                         
0A3B: 00              NOP                         
0A3C: 00              NOP                         
0A3D: 00              NOP                         
0A3E: 00              NOP                         
0A3F: 00              NOP                         
0A40: AA              XOR     D                   
0A41: BA              CP      D                   
0A42: AB              XOR     E                   
0A43: BB              CP      E                   
0A44: 80              ADD     A,B                 
0A45: 90              SUB     B                   
0A46: 81              ADD     A,C                 
0A47: 91              SUB     C                   
0A48: 74              LD      (HL),H              
0A49: 7C              LD      A,H                 
0A4A: 75              LD      (HL),L              
0A4B: 7D              LD      A,L                 
0A4C: FF              RST     0X38                
0A4D: FF              RST     0X38                
0A4E: FF              RST     0X38                
0A4F: FF              RST     0X38                
0A50: 01 70 4B        LD      BC,$4B70            
0A53: 11 B0 4B        LD      DE,$4BB0            
0A56: C5              PUSH    BC                  
0A57: CD 18 07        CALL    $0718               ; {}
0A5A: C1              POP     BC                  
0A5B: 79              LD      A,C                 
0A5C: C6 04           ADD     $04                 
0A5E: 4F              LD      C,A                 
0A5F: C6 40           ADD     $40                 
0A61: 5F              LD      E,A                 
0A62: 50              LD      D,B                 
0A63: A7              AND     A                   
0A64: C2 56 0A        JP      NZ,$0A56            ; {}
0A67: C9              RET                         
0A68: FF              RST     0X38                
0A69: FF              RST     0X38                
0A6A: FF              RST     0X38                
0A6B: FF              RST     0X38                
0A6C: 01 70 4B        LD      BC,$4B70            
0A6F: 11 B3 4B        LD      DE,$4BB3            
0A72: C5              PUSH    BC                  
0A73: D5              PUSH    DE                  
0A74: 0A              LD      A,(BC)              
0A75: E6 18           AND     $18                 
0A77: CA 8A 0A        JP      Z,$0A8A             ; {}
0A7A: EB              EX      DE,HL               
0A7B: 56              LD      D,(HL)              
0A7C: 2B              DEC     HL                  
0A7D: 5E              LD      E,(HL)              
0A7E: 2B              DEC     HL                  
0A7F: 72              LD      (HL),D              
0A80: 2B              DEC     HL                  
0A81: 73              LD      (HL),E              
0A82: EB              EX      DE,HL               
0A83: 13              INC     DE                  
0A84: 13              INC     DE                  
0A85: 03              INC     BC                  
0A86: 03              INC     BC                  
0A87: CD BA 09        CALL    $09BA               ; {}
0A8A: D1              POP     DE                  
0A8B: C1              POP     BC                  
0A8C: 79              LD      A,C                 
0A8D: C6 04           ADD     $04                 
0A8F: 4F              LD      C,A                 
0A90: 7B              LD      A,E                 
0A91: C6 04           ADD     $04                 
0A93: 5F              LD      E,A                 
0A94: FE 03           CP      $03                 
0A96: C2 72 0A        JP      NZ,$0A72            ; {}
0A99: C9              RET                         
0A9A: FF              RST     0X38                
0A9B: FF              RST     0X38                
0A9C: FF              RST     0X38                
0A9D: FF              RST     0X38                
0A9E: FF              RST     0X38                
0A9F: FF              RST     0X38                
0AA0: 2E E2           LD      L,$E2               
0AA2: 56              LD      D,(HL)              
0AA3: 23              INC     HL                  
0AA4: 5E              LD      E,(HL)              
0AA5: CD 10 02        CALL    $0210               ; {code.AddOneRow}
0AA8: 1B              DEC     DE                  
0AA9: 01 04 04        LD      BC,$0404            
0AAC: 2E A6           LD      L,$A6               
0AAE: 35              DEC     (HL)                
0AAF: 7E              LD      A,(HL)              
0AB0: 21 F0 17        LD      HL,$17F0            
0AB3: FE C0           CP      $C0                 
0AB5: CA 48 0B        JP      Z,$0B48             ; {}
0AB8: 21 70 17        LD      HL,$1770            
0ABB: E6 0C           AND     $0C                 
0ABD: 07              RLCA                        
0ABE: 07              RLCA                        
0ABF: 85              ADD     A,L                 
0AC0: 6F              LD      L,A                 
0AC1: C3 D6 0A        JP      $0AD6               ; {}
0AC4: FF              RST     0X38                
0AC5: FF              RST     0X38                
0AC6: FF              RST     0X38                
0AC7: FF              RST     0X38                
0AC8: FF              RST     0X38                
0AC9: FF              RST     0X38                
0ACA: FF              RST     0X38                
0ACB: FF              RST     0X38                
0ACC: FF              RST     0X38                
0ACD: FF              RST     0X38                
0ACE: FF              RST     0X38                
0ACF: FF              RST     0X38                
0AD0: FF              RST     0X38                
0AD1: FF              RST     0X38                
0AD2: FF              RST     0X38                
0AD3: FF              RST     0X38                
0AD4: FF              RST     0X38                
0AD5: FF              RST     0X38                
0AD6: D5              PUSH    DE                  
0AD7: C5              PUSH    BC                  
0AD8: 7E              LD      A,(HL)              
0AD9: 12              LD      (DE),A              
0ADA: 23              INC     HL                  
0ADB: 13              INC     DE                  
0ADC: 05              DEC     B                   
0ADD: C2 D8 0A        JP      NZ,$0AD8            ; {}
0AE0: C1              POP     BC                  
0AE1: D1              POP     DE                  
0AE2: CD 17 02        CALL    $0217               ; {code.SubtractOneRow}
0AE5: 0D              DEC     C                   
0AE6: C2 D6 0A        JP      NZ,$0AD6            ; {}
0AE9: C9              RET                         

; ?? Function 4
0AEA: 21 B9 43        LD      HL,$43B9            
0AED: 7E              LD      A,(HL)              
0AEE: E6 F8           AND     $F8                 
0AF0: 77              LD      (HL),A              
0AF1: 32 00 58        LD      ($5800),A           ; 58xx scroll register
0AF4: 2E E2           LD      L,$E2               
0AF6: 56              LD      D,(HL)              
0AF7: 2C              INC     L                   
0AF8: 5E              LD      E,(HL)              
0AF9: CD 10 02        CALL    $0210               ; {code.AddOneRow}
0AFC: 1B              DEC     DE                  
0AFD: 00              NOP                         
0AFE: 2E A5           LD      L,$A5               
0B00: 35              DEC     (HL)                
0B01: 7E              LD      A,(HL)              
0B02: CA 15 0B        JP      Z,$0B15             ; {}
0B05: FE 20           CP      $20                 
0B07: DA A0 0B        JP      C,$0BA0             ; {}
0B0A: CA 80 03        JP      Z,$0380             ; {}
0B0D: C3 BA 0B        JP      $0BBA               ; {}
0B10: 70              LD      (HL),B              
0B11: 20 C3           JR      NZ,$AD6             ; {}
0B13: E8              RET     PE                  
0B14: 20 2D           JR      NZ,$B43             ; {}
0B16: 36 05           LD      (HL),$05            
0B18: 2D              DEC     L                   
0B19: 7E              LD      A,(HL)              
0B1A: C6 90           ADD     $90                 
0B1C: 6F              LD      L,A                 
0B1D: 7E              LD      A,(HL)              
0B1E: A7              AND     A                   
0B1F: C8              RET     Z                   
0B20: 35              DEC     (HL)                
0B21: E5              PUSH    HL                  
0B22: CD 67 03        CALL    $0367               ; {}
0B25: E1              POP     HL                  
0B26: 7E              LD      A,(HL)              
0B27: A7              AND     A                   
0B28: C8              RET     Z                   
0B29: 2E A4           LD      L,$A4               
0B2B: 36 00           LD      (HL),$00            
0B2D: C9              RET                         
0B2E: FF              RST     0X38                
0B2F: FF              RST     0X38                
0B30: FF              RST     0X38                
0B31: F0              RET     P                   
0B32: E0              RET     PO                  
0B33: B0              OR      B                   
0B34: C0              RET     NZ                  
0B35: D0              RET     NC                  
0B36: C0              RET     NZ                  
0B37: B0              OR      B                   
0B38: 00              NOP                         
0B39: 08              EX      AF,AF'              
0B3A: 01 09 02        LD      BC,$0209            
0B3D: 0A              LD      A,(BC)              
0B3E: 03              INC     BC                  
0B3F: 0B              DEC     BC                  
0B40: 03              INC     BC                  
0B41: 0B              DEC     BC                  
0B42: 02              LD      (BC),A              
0B43: 0A              LD      A,(BC)              
0B44: 01 09 00        LD      BC,$0009            
0B47: 08              EX      AF,AF'              
0B48: CD D6 0A        CALL    $0AD6               ; {}
0B4B: 21 C0 43        LD      HL,$43C0            
0B4E: 36 0C           LD      (HL),$0C            
0B50: 2C              INC     L                   
0B51: 36 0C           LD      (HL),$0C            
0B53: 2C              INC     L                   
0B54: 7E              LD      A,(HL)              
0B55: E6 F8           AND     $F8                 
0B57: F6 03           OR      $03                 
0B59: 77              LD      (HL),A              
0B5A: C9              RET                         
0B5B: FF              RST     0X38                
0B5C: FF              RST     0X38                
0B5D: FF              RST     0X38                
0B5E: FF              RST     0X38                
0B5F: FF              RST     0X38                
0B60: 21 A5 43        LD      HL,$43A5            
0B63: 34              INC     (HL)                
0B64: 7E              LD      A,(HL)              
0B65: FE 40           CP      $40                 
0B67: CA A0 03        JP      Z,$03A0             ; {}
0B6A: 21 00 1A        LD      HL,$1A00            
0B6D: 0E 01           LD      C,$01               
0B6F: FE 80           CP      $80                 
0B71: C2 95 0B        JP      NZ,$0B95            ; {}
0B74: 21 A4 43        LD      HL,$43A4            
0B77: 36 00           LD      (HL),$00            
0B79: 2E 90           LD      L,$90               
0B7B: 7E              LD      A,(HL)              
0B7C: 2C              INC     L                   
0B7D: B6              OR      (HL)                
0B7E: C0              RET     NZ                  
0B7F: AF              XOR     A                   
0B80: 2E 98           LD      L,$98               
0B82: 77              LD      (HL),A              
0B83: 2C              INC     L                   
0B84: 77              LD      (HL),A              
0B85: 2E A2           LD      L,$A2               
0B87: 77              LD      (HL),A              
0B88: 2C              INC     L                   
0B89: 7E              LD      A,(HL)              
0B8A: A7              AND     A                   
0B8B: C8              RET     Z                   
0B8C: 36 00           LD      (HL),$00            
0B8E: 01 00 01        LD      BC,$0100            
0B91: CD 60 04        CALL    $0460               ; {}
0B94: C9              RET                         
0B95: CD D0 01        CALL    $01D0               ; {}
0B98: CD E4 01        CALL    $01E4               ; {}
0B9B: C3 F0 1D        JP      $1DF0               ; {}
0B9E: FF              RST     0X38                
0B9F: FF              RST     0X38                
0BA0: 21 B8 43        LD      HL,$43B8            
0BA3: 7E              LD      A,(HL)              
0BA4: E6 0F           AND     $0F                 
0BA6: FE 04           CP      $04                 
0BA8: D8              RET     C                   
0BA9: FE 09           CP      $09                 
0BAB: D0              RET     NC                  
0BAC: 2C              INC     L                   
0BAD: AF              XOR     A                   
0BAE: 77              LD      (HL),A              
0BAF: 32 00 58        LD      ($5800),A           ; 58xx scroll register
0BB2: C3 A0 03        JP      $03A0               ; {}
0BB5: FF              RST     0X38                
0BB6: FF              RST     0X38                
0BB7: FF              RST     0X38                
0BB8: FF              RST     0X38                
0BB9: FF              RST     0X38                
0BBA: 47              LD      B,A                 
0BBB: 0F              RRCA                        
0BBC: D2 C0 0F        JP      NC,$0FC0            ; {}
0BBF: 0F              RRCA                        
0BC0: 78              LD      A,B                 
0BC1: DA 70 20        JP      C,$2070             ; {}
0BC4: C3 E8 20        JP      $20E8               ; {}
0BC7: FF              RST     0X38                
0BC8: FF              RST     0X38                
0BC9: FF              RST     0X38                
0BCA: 21 D0 42        LD      HL,$42D0            
0BCD: 01 DF FF        LD      BC,$FFDF            
0BD0: 36 64           LD      (HL),$64            
0BD2: 09              ADD     HL,BC               
0BD3: 23              INC     HL                  
0BD4: 36 65           LD      (HL),$65            
0BD6: 21 F2 42        LD      HL,$42F2            
0BD9: 11 40 0A        LD      DE,$0A40            
0BDC: CD 38 35        CALL    $3538               ; {}
0BDF: 21 15 4B        LD      HL,$4B15            
0BE2: 11 00 3C        LD      DE,$3C00            
0BE5: CD 28 35        CALL    $3528               ; {}
0BE8: 21 D8 4A        LD      HL,$4AD8            
0BEB: 11 48 0A        LD      DE,$0A48            
0BEE: CD 48 35        CALL    $3548               ; {}
0BF1: C9              RET                         
0BF2: FF              RST     0X38                
0BF3: FF              RST     0X38                
0BF4: FF              RST     0X38                
0BF5: FF              RST     0X38                
0BF6: FF              RST     0X38                
0BF7: FF              RST     0X38                
0BF8: FF              RST     0X38                
0BF9: FF              RST     0X38                
0BFA: FF              RST     0X38                
0BFB: FF              RST     0X38                
0BFC: FF              RST     0X38                
0BFD: FF              RST     0X38                
0BFE: FF              RST     0X38                
0BFF: FF              RST     0X38                
0C00: E5              PUSH    HL                  
0C01: 7D              LD      A,L                 
0C02: D6 72           SUB     $72                 
0C04: 0F              RRCA                        
0C05: C6 50           ADD     $50                 
0C07: 6F              LD      L,A                 
0C08: 7E              LD      A,(HL)              
0C09: 2C              INC     L                   
0C0A: 6E              LD      L,(HL)              
0C0B: 67              LD      H,A                 
0C0C: 11 04 0C        LD      DE,$0C04            
0C0F: 7E              LD      A,(HL)              
0C10: E1              POP     HL                  
0C11: FE 07           CP      $07                 
0C13: DA A4 0E        JP      C,$0EA4             ; {}
0C16: FE 09           CP      $09                 
0C18: D2 A4 0E        JP      NC,$0EA4            ; {}
0C1B: 11 20 10        LD      DE,$1020            
0C1E: 3E FF           LD      A,$FF               
0C20: 32 69 43        LD      ($4369),A           
0C23: C3 A4 0E        JP      $0EA4               ; {}
0C26: FF              RST     0X38                
0C27: FF              RST     0X38                
0C28: FF              RST     0X38                
0C29: FF              RST     0X38                
0C2A: FF              RST     0X38                
0C2B: FF              RST     0X38                
0C2C: FF              RST     0X38                
0C2D: FF              RST     0X38                
0C2E: FF              RST     0X38                
0C2F: FF              RST     0X38                
0C30: FF              RST     0X38                
0C31: FF              RST     0X38                
0C32: FF              RST     0X38                
0C33: FF              RST     0X38                
0C34: FF              RST     0X38                
0C35: FF              RST     0X38                
0C36: FF              RST     0X38                
0C37: FF              RST     0X38                
0C38: FF              RST     0X38                
0C39: FF              RST     0X38                
0C3A: FF              RST     0X38                
0C3B: FF              RST     0X38                
0C3C: FF              RST     0X38                
0C3D: FF              RST     0X38                
0C3E: FF              RST     0X38                
0C3F: FF              RST     0X38                
0C40: 21 FF 43        LD      HL,$43FF            
0C43: 06 05           LD      B,$05               
0C45: CD 8B 08        CALL    $088B               ; {}
0C48: CD 56 0C        CALL    $0C56               ; {}
0C4B: CD 6B 0C        CALL    $0C6B               ; {}
0C4E: CD D8 0C        CALL    $0CD8               ; {}
0C51: C9              RET                         
0C52: FF              RST     0X38                
0C53: FF              RST     0X38                
0C54: FF              RST     0X38                
0C55: FF              RST     0X38                
0C56: 21 CC 43        LD      HL,$43CC            
0C59: E5              PUSH    HL                  
0C5A: CD 84 0C        CALL    $0C84               ; {}
0C5D: E1              POP     HL                  
0C5E: 7D              LD      A,L                 
0C5F: C6 04           ADD     $04                 
0C61: 6F              LD      L,A                 
0C62: FE E0           CP      $E0                 
0C64: C2 59 0C        JP      NZ,$0C59            ; {}
0C67: C9              RET                         
0C68: FF              RST     0X38                
0C69: FF              RST     0X38                
0C6A: FF              RST     0X38                
0C6B: 01 CE 43        LD      BC,$43CE            
0C6E: 11 EE 43        LD      DE,$43EE            
0C71: CD BA 09        CALL    $09BA               ; {}
0C74: 03              INC     BC                  
0C75: 03              INC     BC                  
0C76: 03              INC     BC                  
0C77: 13              INC     DE                  
0C78: 13              INC     DE                  
0C79: 13              INC     DE                  
0C7A: 79              LD      A,C                 
0C7B: FE E2           CP      $E2                 
0C7D: C2 71 0C        JP      NZ,$0C71            ; {}
0C80: C9              RET                         
0C81: FF              RST     0X38                
0C82: FF              RST     0X38                
0C83: FF              RST     0X38                
0C84: 7E              LD      A,(HL)              
0C85: E6 08           AND     $08                 
0C87: C8              RET     Z                   
0C88: 00              NOP                         
0C89: 00              NOP                         
0C8A: 2C              INC     L                   
0C8B: 7E              LD      A,(HL)              
0C8C: EE 04           XOR     $04                 
0C8E: 77              LD      (HL),A              
0C8F: 2C              INC     L                   
0C90: 2C              INC     L                   
0C91: 7E              LD      A,(HL)              
0C92: C6 04           ADD     $04                 
0C94: 77              LD      (HL),A              
0C95: FE F9           CP      $F9                 
0C97: D2 6E 09        JP      NC,$096E            ; {}
0C9A: 2D              DEC     L                   
0C9B: CD B4 0C        CALL    $0CB4               ; {}
0C9E: 54              LD      D,H                 
0C9F: 7D              LD      A,L                 
0CA0: C6 20           ADD     $20                 
0CA2: 5F              LD      E,A                 
0CA3: EB              EX      DE,HL               
0CA4: 46              LD      B,(HL)              
0CA5: 23              INC     HL                  
0CA6: 4E              LD      C,(HL)              
0CA7: 0A              LD      A,(BC)              
0CA8: EB              EX      DE,HL               
0CA9: 2C              INC     L                   
0CAA: FE E8           CP      $E8                 
0CAC: D2 6E 09        JP      NC,$096E            ; {}
0CAF: C9              RET                         
0CB0: FF              RST     0X38                
0CB1: FF              RST     0X38                
0CB2: FF              RST     0X38                
0CB3: FF              RST     0X38                
0CB4: FE DC           CP      $DC                 
0CB6: D8              RET     C                   
0CB7: FE E9           CP      $E9                 
0CB9: D0              RET     NC                  
0CBA: 3A 9F 43        LD      A,($439F)           
0CBD: BE              CP      (HL)                
0CBE: D8              RET     C                   
0CBF: 3A 9E 43        LD      A,($439E)           
0CC2: BE              CP      (HL)                
0CC3: D0              RET     NC                  
0CC4: 3E 04           LD      A,$04               
0CC6: 32 A4 43        LD      ($43A4),A           ; {ram.M43A4}
0CC9: 3E 60           LD      A,$60               
0CCB: 32 A5 43        LD      ($43A5),A           ; {ram.M43A5}
0CCE: 3E 10           LD      A,$10               
0CD0: 32 63 43        LD      ($4363),A           
0CD3: C9              RET                         
0CD4: FF              RST     0X38                
0CD5: FF              RST     0X38                
0CD6: FF              RST     0X38                
0CD7: FF              RST     0X38                
0CD8: 01 CC 43        LD      BC,$43CC            
0CDB: 11 EC 43        LD      DE,$43EC            
0CDE: C5              PUSH    BC                  
0CDF: CD 18 07        CALL    $0718               ; {}
0CE2: C1              POP     BC                  
0CE3: 79              LD      A,C                 
0CE4: C6 04           ADD     $04                 
0CE6: 4F              LD      C,A                 
0CE7: C6 20           ADD     $20                 
0CE9: 5F              LD      E,A                 
0CEA: 50              LD      D,B                 
0CEB: A7              AND     A                   
0CEC: C2 DE 0C        JP      NZ,$0CDE            ; {}
0CEF: C9              RET                         
0CF0: FF              RST     0X38                
0CF1: FF              RST     0X38                
0CF2: FF              RST     0X38                
0CF3: FF              RST     0X38                
0CF4: D1              POP     DE                  
0CF5: C1              POP     BC                  
0CF6: C9              RET                         
0CF7: FF              RST     0X38                
0CF8: FF              RST     0X38                
0CF9: FF              RST     0X38                
0CFA: FF              RST     0X38                
0CFB: FF              RST     0X38                
0CFC: FF              RST     0X38                
0CFD: FF              RST     0X38                
0CFE: FF              RST     0X38                
0CFF: FF              RST     0X38                
0D00: FF              RST     0X38                
0D01: FF              RST     0X38                
0D02: FF              RST     0X38                
0D03: FF              RST     0X38                
0D04: FF              RST     0X38                
0D05: FF              RST     0X38                
0D06: FF              RST     0X38                
0D07: FF              RST     0X38                
0D08: 21 93 43        LD      HL,$4393            
0D0B: 34              INC     (HL)                
0D0C: 7E              LD      A,(HL)              
0D0D: E6 07           AND     $07                 
0D0F: C0              RET     NZ                  
0D10: 2C              INC     L                   
0D11: 2C              INC     L                   
0D12: 7E              LD      A,(HL)              
0D13: 3C              INC     A                   
0D14: E6 0F           AND     $0F                 
0D16: 77              LD      (HL),A              
0D17: C9              RET                         
0D18: FF              RST     0X38                
0D19: FF              RST     0X38                
0D1A: FF              RST     0X38                
0D1B: FF              RST     0X38                
0D1C: 01 70 4B        LD      BC,$4B70            
0D1F: 21 50 4B        LD      HL,$4B50            
0D22: CD 30 0D        CALL    $0D30               ; {}
0D25: 0C              INC     C                   
0D26: 0C              INC     C                   
0D27: 2C              INC     L                   
0D28: 3E B0           LD      A,$B0               
0D2A: B9              CP      C                   
0D2B: C2 22 0D        JP      NZ,$0D22            ; {}
0D2E: C9              RET                         
0D2F: FF              RST     0X38                
0D30: 56              LD      D,(HL)              
0D31: 23              INC     HL                  
0D32: 0A              LD      A,(BC)              
0D33: 03              INC     BC                  
0D34: 03              INC     BC                  
0D35: E6 08           AND     $08                 
0D37: C8              RET     Z                   
0D38: 5E              LD      E,(HL)              
0D39: EB              EX      DE,HL               
0D3A: 7E              LD      A,(HL)              
0D3B: 07              RLCA                        
0D3C: C6 00           ADD     $00                 
0D3E: 6F              LD      L,A                 
0D3F: 26 17           LD      H,$17               
0D41: AF              XOR     A                   
0D42: BE              CP      (HL)                
0D43: CA 4F 0D        JP      Z,$0D4F             ; {}
0D46: 23              INC     HL                  
0D47: BE              CP      (HL)                
0D48: CA 5E 0D        JP      Z,$0D5E             ; {}
0D4B: 2B              DEC     HL                  
0D4C: 0A              LD      A,(BC)              
0D4D: 86              ADD     A,(HL)              
0D4E: 02              LD      (BC),A              
0D4F: 03              INC     BC                  
0D50: 23              INC     HL                  
0D51: 0A              LD      A,(BC)              
0D52: 86              ADD     A,(HL)              
0D53: 02              LD      (BC),A              
0D54: 0B              DEC     BC                  
0D55: E6 07           AND     $07                 
0D57: EB              EX      DE,HL               
0D58: C0              RET     NZ                  
0D59: 34              INC     (HL)                
0D5A: C9              RET                         
0D5B: FF              RST     0X38                
0D5C: FF              RST     0X38                
0D5D: FF              RST     0X38                
0D5E: 2B              DEC     HL                  
0D5F: 0A              LD      A,(BC)              
0D60: 86              ADD     A,(HL)              
0D61: 02              LD      (BC),A              
0D62: E6 07           AND     $07                 
0D64: EB              EX      DE,HL               
0D65: C0              RET     NZ                  
0D66: 34              INC     (HL)                
0D67: C9              RET                         
0D68: FF              RST     0X38                
0D69: FF              RST     0X38                
0D6A: FF              RST     0X38                
0D6B: FF              RST     0X38                
0D6C: FF              RST     0X38                
0D6D: FF              RST     0X38                
0D6E: FF              RST     0X38                
0D6F: FF              RST     0X38                
0D70: 01 70 4B        LD      BC,$4B70            
0D73: 21 50 4B        LD      HL,$4B50            
0D76: CD 86 0D        CALL    $0D86               ; {}
0D79: 79              LD      A,C                 
0D7A: C6 04           ADD     $04                 
0D7C: 4F              LD      C,A                 
0D7D: 3E B0           LD      A,$B0               
0D7F: B9              CP      C                   
0D80: C2 76 0D        JP      NZ,$0D76            ; {}
0D83: C9              RET                         
0D84: FF              RST     0X38                
0D85: FF              RST     0X38                
0D86: 56              LD      D,(HL)              
0D87: 23              INC     HL                  
0D88: 5E              LD      E,(HL)              
0D89: 23              INC     HL                  
0D8A: 0A              LD      A,(BC)              
0D8B: E6 08           AND     $08                 
0D8D: C8              RET     Z                   
0D8E: EB              EX      DE,HL               
0D8F: 7E              LD      A,(HL)              
0D90: A7              AND     A                   
0D91: CC DE 0D        CALL    Z,$0DDE             ; {}
0D94: 6F              LD      L,A                 
0D95: 07              RLCA                        
0D96: 85              ADD     A,L                 
0D97: C6 A0           ADD     $A0                 
0D99: 6F              LD      L,A                 
0D9A: 26 16           LD      H,$16               
0D9C: 0A              LD      A,(BC)              
0D9D: E6 F8           AND     $F8                 
0D9F: B6              OR      (HL)                
0DA0: 02              LD      (BC),A              
0DA1: 03              INC     BC                  
0DA2: 03              INC     BC                  
0DA3: 03              INC     BC                  
0DA4: 23              INC     HL                  
0DA5: 7E              LD      A,(HL)              
0DA6: 23              INC     HL                  
0DA7: 0F              RRCA                        
0DA8: DA BB 0D        JP      C,$0DBB             ; {}
0DAB: 0F              RRCA                        
0DAC: DA CC 0D        JP      C,$0DCC             ; {}
0DAF: 0A              LD      A,(BC)              
0DB0: 0F              RRCA                        
0DB1: E6 03           AND     $03                 
0DB3: 86              ADD     A,(HL)              
0DB4: 0B              DEC     BC                  
0DB5: C3 D2 0D        JP      $0DD2               ; {}
0DB8: FF              RST     0X38                
0DB9: FF              RST     0X38                
0DBA: FF              RST     0X38                
0DBB: 0A              LD      A,(BC)              
0DBC: 0F              RRCA                        
0DBD: E6 03           AND     $03                 
0DBF: 86              ADD     A,(HL)              
0DC0: 67              LD      H,A                 
0DC1: 0B              DEC     BC                  
0DC2: 0A              LD      A,(BC)              
0DC3: E6 04           AND     $04                 
0DC5: 84              ADD     A,H                 
0DC6: C3 D2 0D        JP      $0DD2               ; {}
0DC9: FF              RST     0X38                
0DCA: FF              RST     0X38                
0DCB: FF              RST     0X38                
0DCC: 0B              DEC     BC                  
0DCD: 0A              LD      A,(BC)              
0DCE: 0F              RRCA                        
0DCF: E6 03           AND     $03                 
0DD1: 86              ADD     A,(HL)              
0DD2: 6F              LD      L,A                 
0DD3: 26 16           LD      H,$16               
0DD5: 7E              LD      A,(HL)              
0DD6: 0B              DEC     BC                  
0DD7: 02              LD      (BC),A              
0DD8: 0B              DEC     BC                  
0DD9: EB              EX      DE,HL               
0DDA: C9              RET                         
0DDB: FF              RST     0X38                
0DDC: FF              RST     0X38                
0DDD: FF              RST     0X38                
0DDE: 1B              DEC     DE                  
0DDF: 1B              DEC     DE                  
0DE0: 3A 94 43        LD      A,($4394)           
0DE3: 12              LD      (DE),A              
0DE4: 67              LD      H,A                 
0DE5: 13              INC     DE                  
0DE6: 3A 95 43        LD      A,($4395)           
0DE9: 12              LD      (DE),A              
0DEA: 6F              LD      L,A                 
0DEB: 13              INC     DE                  
0DEC: 7E              LD      A,(HL)              
0DED: C9              RET                         
0DEE: FF              RST     0X38                
0DEF: FF              RST     0X38                
0DF0: 01 C4 43        LD      BC,$43C4            
0DF3: 21 E6 43        LD      HL,$43E6            
0DF6: CD 10 0E        CALL    $0E10               ; {}
0DF9: 01 C8 43        LD      BC,$43C8            
0DFC: 21 EA 43        LD      HL,$43EA            
0DFF: C3 10 0E        JP      $0E10               ; {}
0E02: 01 CC 43        LD      BC,$43CC            
0E05: 21 EE 43        LD      HL,$43EE            
0E08: CD 10 0E        CALL    $0E10               ; {}
0E0B: C9              RET                         
0E0C: FF              RST     0X38                
0E0D: FF              RST     0X38                
0E0E: FF              RST     0X38                
0E0F: FF              RST     0X38                
0E10: 0A              LD      A,(BC)              
0E11: E6 08           AND     $08                 
0E13: C8              RET     Z                   
0E14: 56              LD      D,(HL)              
0E15: 2C              INC     L                   
0E16: 5E              LD      E,(HL)              
0E17: 1A              LD      A,(DE)              
0E18: FE C0           CP      $C0                 
0E1A: D0              RET     NC                  
0E1B: FE 60           CP      $60                 
0E1D: D8              RET     C                   
0E1E: FE 68           CP      $68                 
0E20: D2 39 0E        JP      NC,$0E39            ; {}
0E23: E6 07           AND     $07                 
0E25: 07              RLCA                        
0E26: 07              RLCA                        
0E27: C6 40           ADD     $40                 
0E29: 6F              LD      L,A                 
0E2A: 26 17           LD      H,$17               
0E2C: 03              INC     BC                  
0E2D: 03              INC     BC                  
0E2E: 0A              LD      A,(BC)              
0E2F: E6 07           AND     $07                 
0E31: BE              CP      (HL)                
0E32: D0              RET     NC                  
0E33: 23              INC     HL                  
0E34: BE              CP      (HL)                
0E35: D8              RET     C                   
0E36: C3 70 0E        JP      $0E70               ; {}
0E39: 03              INC     BC                  
0E3A: 03              INC     BC                  
0E3B: 0A              LD      A,(BC)              
0E3C: 57              LD      D,A                 
0E3D: 03              INC     BC                  
0E3E: 0A              LD      A,(BC)              
0E3F: E6 F8           AND     $F8                 
0E41: 5F              LD      E,A                 
0E42: 21 70 4B        LD      HL,$4B70            
0E45: 7E              LD      A,(HL)              
0E46: 23              INC     HL                  
0E47: 23              INC     HL                  
0E48: E6 08           AND     $08                 
0E4A: C4 58 0E        CALL    NZ,$0E58            ; {}
0E4D: 23              INC     HL                  
0E4E: 23              INC     HL                  
0E4F: 3E B0           LD      A,$B0               
0E51: BD              CP      L                   
0E52: C2 45 0E        JP      NZ,$0E45            ; {}
0E55: C9              RET                         
0E56: FF              RST     0X38                
0E57: FF              RST     0X38                
0E58: 7A              LD      A,D                 
0E59: BE              CP      (HL)                
0E5A: D8              RET     C                   
0E5B: 7E              LD      A,(HL)              
0E5C: C6 08           ADD     $08                 
0E5E: BA              CP      D                   
0E5F: D8              RET     C                   
0E60: 23              INC     HL                  
0E61: 7E              LD      A,(HL)              
0E62: 2B              DEC     HL                  
0E63: C6 04           ADD     $04                 
0E65: BB              CP      E                   
0E66: D8              RET     C                   
0E67: D6 0C           SUB     $0C                 
0E69: BB              CP      E                   
0E6A: D0              RET     NC                  
0E6B: C3 00 0C        JP      $0C00               ; {}
0E6E: FF              RST     0X38                
0E6F: FF              RST     0X38                
0E70: 23              INC     HL                  
0E71: 0A              LD      A,(BC)              
0E72: E6 F8           AND     $F8                 
0E74: 86              ADD     A,(HL)              
0E75: 57              LD      D,A                 
0E76: 03              INC     BC                  
0E77: 0A              LD      A,(BC)              
0E78: E6 F8           AND     $F8                 
0E7A: 5F              LD      E,A                 
0E7B: 21 70 4B        LD      HL,$4B70            
0E7E: 7E              LD      A,(HL)              
0E7F: 23              INC     HL                  
0E80: 23              INC     HL                  
0E81: E6 08           AND     $08                 
0E83: C4 90 0E        CALL    NZ,$0E90            ; {}
0E86: 23              INC     HL                  
0E87: 23              INC     HL                  
0E88: 3E B0           LD      A,$B0               
0E8A: BD              CP      L                   
0E8B: C2 7E 0E        JP      NZ,$0E7E            ; {}
0E8E: C9              RET                         
0E8F: FF              RST     0X38                
0E90: 7E              LD      A,(HL)              
0E91: C6 02           ADD     $02                 
0E93: BA              CP      D                   
0E94: D8              RET     C                   
0E95: D6 05           SUB     $05                 
0E97: BA              CP      D                   
0E98: D0              RET     NC                  
0E99: 23              INC     HL                  
0E9A: 7E              LD      A,(HL)              
0E9B: 2B              DEC     HL                  
0E9C: E6 F8           AND     $F8                 
0E9E: BB              CP      E                   
0E9F: C0              RET     NZ                  
0EA0: 11 02 0C        LD      DE,$0C02            
0EA3: 00              NOP                         
0EA4: 2B              DEC     HL                  
0EA5: 2B              DEC     HL                  
0EA6: 0B              DEC     BC                  
0EA7: 0B              DEC     BC                  
0EA8: 0B              DEC     BC                  
0EA9: 0A              LD      A,(BC)              
0EAA: E6 F7           AND     $F7                 
0EAC: 02              LD      (BC),A              
0EAD: 7E              LD      A,(HL)              
0EAE: E6 F7           AND     $F7                 
0EB0: 77              LD      (HL),A              
0EB1: 7D              LD      A,L                 
0EB2: C6 42           ADD     $42                 
0EB4: 6F              LD      L,A                 
0EB5: 46              LD      B,(HL)              
0EB6: 23              INC     HL                  
0EB7: 4E              LD      C,(HL)              
0EB8: 21 78 43        LD      HL,$4378            
0EBB: 7A              LD      A,D                 
0EBC: FE 10           CP      $10                 
0EBE: CA C3 0E        JP      Z,$0EC3             ; {}
0EC1: 2E 70           LD      L,$70               
0EC3: 7E              LD      A,(HL)              
0EC4: A7              AND     A                   
0EC5: CA D5 0E        JP      Z,$0ED5             ; {}
0EC8: 2C              INC     L                   
0EC9: 2C              INC     L                   
0ECA: 2C              INC     L                   
0ECB: 2C              INC     L                   
0ECC: 7E              LD      A,(HL)              
0ECD: A7              AND     A                   
0ECE: CA D5 0E        JP      Z,$0ED5             ; {}
0ED1: 2C              INC     L                   
0ED2: 2C              INC     L                   
0ED3: 2C              INC     L                   
0ED4: 2C              INC     L                   
0ED5: 72              LD      (HL),D              
0ED6: 2C              INC     L                   
0ED7: 73              LD      (HL),E              
0ED8: 2C              INC     L                   
0ED9: 70              LD      (HL),B              
0EDA: 2C              INC     L                   
0EDB: 71              LD      (HL),C              
0EDC: 2E 64           LD      L,$64               
0EDE: 36 FF           LD      (HL),$FF            
0EE0: 2E BA           LD      L,$BA               
0EE2: 35              DEC     (HL)                
0EE3: E1              POP     HL                  
0EE4: E1              POP     HL                  
0EE5: E9              JP      (HL)                
0EE6: FF              RST     0X38                
0EE7: FF              RST     0X38                
0EE8: FF              RST     0X38                
0EE9: FF              RST     0X38                
0EEA: FF              RST     0X38                
0EEB: FF              RST     0X38                
0EEC: FF              RST     0X38                
0EED: FF              RST     0X38                
0EEE: FF              RST     0X38                
0EEF: FF              RST     0X38                
0EF0: FF              RST     0X38                
0EF1: FF              RST     0X38                
0EF2: FF              RST     0X38                
0EF3: FF              RST     0X38                
0EF4: FF              RST     0X38                
0EF5: FF              RST     0X38                
0EF6: FF              RST     0X38                
0EF7: FF              RST     0X38                
0EF8: FF              RST     0X38                
0EF9: FF              RST     0X38                
0EFA: FF              RST     0X38                
0EFB: FF              RST     0X38                
0EFC: FF              RST     0X38                
0EFD: FF              RST     0X38                
0EFE: FF              RST     0X38                
0EFF: FF              RST     0X38                
0F00: 21 A6 43        LD      HL,$43A6            
0F03: 7E              LD      A,(HL)              
0F04: FE C0           CP      $C0                 
0F06: D2 74 0F        JP      NC,$0F74            ; {}
0F09: 2E E2           LD      L,$E2               
0F0B: 56              LD      D,(HL)              
0F0C: 2C              INC     L                   
0F0D: 5E              LD      E,(HL)              
0F0E: 01 02 02        LD      BC,$0202            
0F11: CD 56 0F        CALL    $0F56               ; {}
0F14: C8              RET     Z                   
0F15: 00              NOP                         
0F16: 00              NOP                         
0F17: 21 9E 43        LD      HL,$439E            
0F1A: 7E              LD      A,(HL)              
0F1B: D6 06           SUB     $06                 
0F1D: 47              LD      B,A                 
0F1E: 2C              INC     L                   
0F1F: 4E              LD      C,(HL)              
0F20: 21 70 4B        LD      HL,$4B70            
0F23: 7E              LD      A,(HL)              
0F24: 2C              INC     L                   
0F25: 2C              INC     L                   
0F26: E6 08           AND     $08                 
0F28: C4 38 0F        CALL    NZ,$0F38            ; {}
0F2B: 2C              INC     L                   
0F2C: 2C              INC     L                   
0F2D: 3E B0           LD      A,$B0               
0F2F: BD              CP      L                   
0F30: C2 23 0F        JP      NZ,$0F23            ; {}
0F33: C9              RET                         
0F34: FF              RST     0X38                
0F35: FF              RST     0X38                
0F36: FF              RST     0X38                
0F37: FF              RST     0X38                
0F38: 2C              INC     L                   
0F39: 7E              LD      A,(HL)              
0F3A: 2D              DEC     L                   
0F3B: FE D2           CP      $D2                 
0F3D: D8              RET     C                   
0F3E: FE E7           CP      $E7                 
0F40: D0              RET     NC                  
0F41: 7E              LD      A,(HL)              
0F42: B9              CP      C                   
0F43: D0              RET     NC                  
0F44: B8              CP      B                   
0F45: D8              RET     C                   
0F46: CD C4 0C        CALL    $0CC4               ; {}
0F49: 11 04 0D        LD      DE,$0D04            
0F4C: 2B              DEC     HL                  
0F4D: 2B              DEC     HL                  
0F4E: C3 AD 0E        JP      $0EAD               ; {}
0F51: AD              XOR     L                   
0F52: 0E FF           LD      C,$FF               
0F54: FF              RST     0X38                
0F55: FF              RST     0X38                
0F56: C5              PUSH    BC                  
0F57: D5              PUSH    DE                  
0F58: 1A              LD      A,(DE)              
0F59: FE 60           CP      $60                 
0F5B: DA 63 0F        JP      C,$0F63             ; {}
0F5E: FE C0           CP      $C0                 
0F60: DA F4 0C        JP      C,$0CF4             ; {}
0F63: 13              INC     DE                  
0F64: 05              DEC     B                   
0F65: C2 58 0F        JP      NZ,$0F58            ; {}
0F68: D1              POP     DE                  
0F69: C1              POP     BC                  
0F6A: CD 17 02        CALL    $0217               ; {code.SubtractOneRow}
0F6D: 0D              DEC     C                   
0F6E: C2 56 0F        JP      NZ,$0F56            ; {}
0F71: C9              RET                         
0F72: FF              RST     0X38                
0F73: FF              RST     0X38                
0F74: 2E E2           LD      L,$E2               
0F76: 56              LD      D,(HL)              
0F77: 2C              INC     L                   
0F78: 5E              LD      E,(HL)              
0F79: CD 17 02        CALL    $0217               ; {code.SubtractOneRow}
0F7C: 1B              DEC     DE                  
0F7D: 01 04 04        LD      BC,$0404            
0F80: CD 56 0F        CALL    $0F56               ; {}
0F83: C8              RET     Z                   
0F84: 00              NOP                         
0F85: 00              NOP                         
0F86: 3A C2 43        LD      A,($43C2)           
0F89: D6 0E           SUB     $0E                 
0F8B: 47              LD      B,A                 
0F8C: C6 2D           ADD     $2D                 
0F8E: 4F              LD      C,A                 
0F8F: 21 70 4B        LD      HL,$4B70            
0F92: 7E              LD      A,(HL)              
0F93: 2C              INC     L                   
0F94: 2C              INC     L                   
0F95: E6 08           AND     $08                 
0F97: C4 A6 0F        CALL    NZ,$0FA6            ; {}
0F9A: 2C              INC     L                   
0F9B: 2C              INC     L                   
0F9C: 3E B0           LD      A,$B0               
0F9E: BD              CP      L                   
0F9F: C2 92 0F        JP      NZ,$0F92            ; {}
0FA2: C9              RET                         
0FA3: FF              RST     0X38                
0FA4: FF              RST     0X38                
0FA5: FF              RST     0X38                
0FA6: 2C              INC     L                   
0FA7: 7E              LD      A,(HL)              
0FA8: 2D              DEC     L                   
0FA9: FE CA           CP      $CA                 
0FAB: D8              RET     C                   
0FAC: FE EF           CP      $EF                 
0FAE: D0              RET     NC                  
0FAF: 7E              LD      A,(HL)              
0FB0: B9              CP      C                   
0FB1: D0              RET     NC                  
0FB2: B8              CP      B                   
0FB3: D8              RET     C                   
0FB4: 11 02 0D        LD      DE,$0D02            
0FB7: 2B              DEC     HL                  
0FB8: 2B              DEC     HL                  
0FB9: C3 AD 0E        JP      $0EAD               ; {}
0FBC: AD              XOR     L                   
0FBD: 0E FF           LD      C,$FF               
0FBF: FF              RST     0X38                
0FC0: 21 70 43        LD      HL,$4370            
0FC3: CD D8 0F        CALL    $0FD8               ; {}
0FC6: 21 74 43        LD      HL,$4374            
0FC9: CD D8 0F        CALL    $0FD8               ; {}
0FCC: 21 78 43        LD      HL,$4378            
0FCF: CD 58 37        CALL    $3758               ; {}
0FD2: 21 7C 43        LD      HL,$437C            
0FD5: C3 58 37        JP      $3758               ; {}
0FD8: 7E              LD      A,(HL)              
0FD9: A7              AND     A                   
0FDA: C8              RET     Z                   
0FDB: 46              LD      B,(HL)              
0FDC: 35              DEC     (HL)                
0FDD: 2C              INC     L                   
0FDE: 2C              INC     L                   
0FDF: 56              LD      D,(HL)              
0FE0: 2C              INC     L                   
0FE1: 5E              LD      E,(HL)              
0FE2: 00              NOP                         
0FE3: CD 10 02        CALL    $0210               ; {code.AddOneRow}
0FE6: 78              LD      A,B                 
0FE7: E6 0E           AND     $0E                 
0FE9: 0F              RRCA                        
0FEA: C6 B0           ADD     $B0                 
0FEC: 6F              LD      L,A                 
0FED: 26 17           LD      H,$17               
0FEF: 6E              LD      L,(HL)              
0FF0: EB              EX      DE,HL               
0FF1: 01 DF FF        LD      BC,$FFDF            
0FF4: C3 40 35        JP      $3540               ; {}
0FF7: 68              LD      L,B                 
0FF8: 3E 05           LD      A,$05               
0FFA: 32 96 43        LD      ($4396),A           
0FFD: C3 A4 0E        JP      $0EA4               ; {}
1000: 01 01 01        LD      BC,$0101            
1003: 01 02 02        LD      BC,$0202            
1006: 02              LD      (BC),A              
1007: 02              LD      (BC),A              
1008: 02              LD      (BC),A              
1009: 02              LD      (BC),A              
100A: 02              LD      (BC),A              
100B: 02              LD      (BC),A              
100C: 01 01 01        LD      BC,$0101            
100F: 01 00 FF        LD      BC,$FF00            
1012: FF              RST     0X38                
1013: FF              RST     0X38                
1014: FF              RST     0X38                
1015: FF              RST     0X38                
1016: FF              RST     0X38                
1017: FF              RST     0X38                
1018: FF              RST     0X38                
1019: FF              RST     0X38                
101A: FF              RST     0X38                
101B: FF              RST     0X38                
101C: FF              RST     0X38                
101D: FF              RST     0X38                
101E: FF              RST     0X38                
101F: FF              RST     0X38                
1020: 10 11           DJNZ    $1033               ; {}
1022: 12              LD      (DE),A              
1023: 13              INC     DE                  
1024: 10 1D           DJNZ    $1043               ; {}
1026: 0D              DEC     C                   
1027: 0E 0B           LD      C,$0B               
1029: 0C              INC     C                   
102A: 0D              DEC     C                   
102B: 0E 0B           LD      C,$0B               
102D: 0C              INC     C                   
102E: 06 06           LD      B,$06               
1030: 1E 03           LD      E,$03               
1032: 1F              RRA                         
1033: 05              DEC     B                   
1034: 1C              INC     E                   
1035: 04              INC     B                   
1036: 1D              DEC     E                   
1037: 06 1E           LD      B,$1E               
1039: 03              INC     BC                  
103A: 03              INC     BC                  
103B: 03              INC     BC                  
103C: 03              INC     BC                  
103D: 03              INC     BC                  
103E: 1F              RRA                         
103F: 1C              INC     E                   
1040: 1D              DEC     E                   
1041: 1E 03           LD      E,$03               
1043: 03              INC     BC                  
1044: 03              INC     BC                  
1045: 03              INC     BC                  
1046: 03              INC     BC                  
1047: 1F              RRA                         
1048: 05              DEC     B                   
1049: 1C              INC     E                   
104A: 04              INC     B                   
104B: 1D              DEC     E                   
104C: 06 1E           LD      B,$1E               
104E: 03              INC     BC                  
104F: 1F              RRA                         
1050: 05              DEC     B                   
1051: 05              DEC     B                   
1052: 05              DEC     B                   
1053: 05              DEC     B                   
1054: 05              DEC     B                   
1055: 05              DEC     B                   
1056: 05              DEC     B                   
1057: 05              DEC     B                   
1058: 05              DEC     B                   
1059: 05              DEC     B                   
105A: 1C              INC     E                   
105B: 04              INC     B                   
105C: 04              INC     B                   
105D: 11 12 13        LD      DE,$1312            
1060: 00              NOP                         
1061: FF              RST     0X38                
1062: FF              RST     0X38                
1063: FF              RST     0X38                
1064: 0B              DEC     BC                  
1065: 1E 19           LD      E,$19               
1067: 06 06           LD      B,$06               
1069: 06 06           LD      B,$06               
106B: 06 06           LD      B,$06               
106D: 1E 1F           LD      E,$1F               
106F: 1C              INC     E                   
1070: 1D              DEC     E                   
1071: 06 06           LD      B,$06               
1073: 06 06           LD      B,$06               
1075: 06 1E           LD      B,$1E               
1077: 03              INC     BC                  
1078: 1F              RRA                         
1079: 05              DEC     B                   
107A: 1C              INC     E                   
107B: 04              INC     B                   
107C: 1D              DEC     E                   
107D: 06 06           LD      B,$06               
107F: 1A              LD      A,(DE)              
1080: 04              INC     B                   
1081: 1B              DEC     DE                  
1082: 05              DEC     B                   
1083: 18 19           JR      $109E               ; {}
1085: 06 1A           LD      B,$1A               
1087: 04              INC     B                   
1088: 1B              DEC     DE                  
1089: 05              DEC     B                   
108A: 05              DEC     B                   
108B: 1C              INC     E                   
108C: 04              INC     B                   
108D: 1D              DEC     E                   
108E: 06 1E           LD      B,$1E               
1090: 03              INC     BC                  
1091: 1F              RRA                         
1092: 05              DEC     B                   
1093: 05              DEC     B                   
1094: 05              DEC     B                   
1095: 05              DEC     B                   
1096: 05              DEC     B                   
1097: 1C              INC     E                   
1098: 1D              DEC     E                   
1099: 1E 1F           LD      E,$1F               
109B: 05              DEC     B                   
109C: 05              DEC     B                   
109D: 05              DEC     B                   
109E: 05              DEC     B                   
109F: 05              DEC     B                   
10A0: 05              DEC     B                   
10A1: 05              DEC     B                   
10A2: 18 1F           JR      $10C3               ; {}
10A4: 00              NOP                         
10A5: FF              RST     0X38                
10A6: FF              RST     0X38                
10A7: FF              RST     0X38                
10A8: 10 04           DJNZ    $10AE               ; {}
10AA: 04              INC     B                   
10AB: 1D              DEC     E                   
10AC: 0D              DEC     C                   
10AD: 0E 0B           LD      C,$0B               
10AF: 0C              INC     C                   
10B0: 0D              DEC     C                   
10B1: 0E 01           LD      C,$01               
10B3: 01 01 01        LD      BC,$0101            
10B6: 01 01 01        LD      BC,$0101            
10B9: 01 05 05        LD      BC,$0505            
10BC: 05              DEC     B                   
10BD: 05              DEC     B                   
10BE: 05              DEC     B                   
10BF: 1C              INC     E                   
10C0: 04              INC     B                   
10C1: 04              INC     B                   
10C2: 1D              DEC     E                   
10C3: 06 06           LD      B,$06               
10C5: 1E 03           LD      E,$03               
10C7: 03              INC     BC                  
10C8: 1F              RRA                         
10C9: 05              DEC     B                   
10CA: 05              DEC     B                   
10CB: 05              DEC     B                   
10CC: 1C              INC     E                   
10CD: 11 12 13        LD      DE,$1312            
10D0: 00              NOP                         
10D1: FF              RST     0X38                
10D2: FF              RST     0X38                
10D3: FF              RST     0X38                
10D4: 0B              DEC     BC                  
10D5: 0C              INC     C                   
10D6: 0D              DEC     C                   
10D7: 0E 0B           LD      C,$0B               
10D9: 0C              INC     C                   
10DA: 0D              DEC     C                   
10DB: 0E 0B           LD      C,$0B               
10DD: 0C              INC     C                   
10DE: 1A              LD      A,(DE)              
10DF: 1B              DEC     DE                  
10E0: 05              DEC     B                   
10E1: 18 19           JR      $10FC               ; {}
10E3: 06 0D           LD      B,$0D               
10E5: 0E 01           LD      C,$01               
10E7: 01 01 01        LD      BC,$0101            
10EA: 01 01 01        LD      BC,$0101            
10ED: 01 05 05        LD      BC,$0505            
10F0: 1C              INC     E                   
10F1: 1B              DEC     DE                  
10F2: 05              DEC     B                   
10F3: 05              DEC     B                   
10F4: 1C              INC     E                   
10F5: 04              INC     B                   
10F6: 1B              DEC     DE                  
10F7: 05              DEC     B                   
10F8: 05              DEC     B                   
10F9: 1C              INC     E                   
10FA: 04              INC     B                   
10FB: 1B              DEC     DE                  
10FC: 00              NOP                         
10FD: FF              RST     0X38                
10FE: FF              RST     0X38                
10FF: FF              RST     0X38                
1100: 0B              DEC     BC                  
1101: 0C              INC     C                   
1102: 0D              DEC     C                   
1103: 0E 0B           LD      C,$0B               
1105: 0C              INC     C                   
1106: 09              ADD     HL,BC               
1107: 09              ADD     HL,BC               
1108: 09              ADD     HL,BC               
1109: 09              ADD     HL,BC               
110A: 0A              LD      A,(BC)              
110B: 0A              LD      A,(BC)              
110C: 09              ADD     HL,BC               
110D: 09              ADD     HL,BC               
110E: 0A              LD      A,(BC)              
110F: 09              ADD     HL,BC               
1110: 16 17           LD      D,$17               
1112: 14              INC     D                   
1113: 07              RLCA                        
1114: 07              RLCA                        
1115: 07              RLCA                        
1116: 1C              INC     E                   
1117: 04              INC     B                   
1118: 1D              DEC     E                   
1119: 06 1E           LD      B,$1E               
111B: 03              INC     BC                  
111C: 1F              RRA                         
111D: 05              DEC     B                   
111E: 1C              INC     E                   
111F: 08              EX      AF,AF'              
1120: 08              EX      AF,AF'              
1121: 08              EX      AF,AF'              
1122: 08              EX      AF,AF'              
1123: 08              EX      AF,AF'              
1124: 08              EX      AF,AF'              
1125: 08              EX      AF,AF'              
1126: 08              EX      AF,AF'              
1127: 05              DEC     B                   
1128: 05              DEC     B                   
1129: 05              DEC     B                   
112A: 05              DEC     B                   
112B: 00              NOP                         
112C: FF              RST     0X38                
112D: FF              RST     0X38                
112E: FF              RST     0X38                
112F: FF              RST     0X38                
1130: 0B              DEC     BC                  
1131: 0C              INC     C                   
1132: 0D              DEC     C                   
1133: 0E 0B           LD      C,$0B               
1135: 0C              INC     C                   
1136: 0A              LD      A,(BC)              
1137: 0A              LD      A,(BC)              
1138: 0A              LD      A,(BC)              
1139: 0A              LD      A,(BC)              
113A: 09              ADD     HL,BC               
113B: 09              ADD     HL,BC               
113C: 0A              LD      A,(BC)              
113D: 0A              LD      A,(BC)              
113E: 09              ADD     HL,BC               
113F: 0A              LD      A,(BC)              
1140: 12              LD      (DE),A              
1141: 13              INC     DE                  
1142: 10 08           DJNZ    $114C               ; {}
1144: 08              EX      AF,AF'              
1145: 08              EX      AF,AF'              
1146: 18 07           JR      $114F               ; {}
1148: 07              RLCA                        
1149: 07              RLCA                        
114A: 07              RLCA                        
114B: 05              DEC     B                   
114C: 1C              INC     E                   
114D: 04              INC     B                   
114E: 1D              DEC     E                   
114F: 06 1E           LD      B,$1E               
1151: 03              INC     BC                  
1152: 1F              RRA                         
1153: 07              RLCA                        
1154: 07              RLCA                        
1155: 07              RLCA                        
1156: 07              RLCA                        
1157: 05              DEC     B                   
1158: 05              DEC     B                   
1159: 05              DEC     B                   
115A: 05              DEC     B                   
115B: 00              NOP                         
115C: FF              RST     0X38                
115D: FF              RST     0X38                
115E: FF              RST     0X38                
115F: FF              RST     0X38                
1160: 1C              INC     E                   
1161: 04              INC     B                   
1162: 04              INC     B                   
1163: 04              INC     B                   
1164: 1D              DEC     E                   
1165: 06 0D           LD      B,$0D               
1167: 0E 0B           LD      C,$0B               
1169: 0C              INC     C                   
116A: 06 06           LD      B,$06               
116C: 1E 15           LD      E,$15               
116E: 16 17           LD      D,$17               
1170: 14              INC     D                   
1171: 19              ADD     HL,DE               
1172: 06 1A           LD      B,$1A               
1174: 04              INC     B                   
1175: 1D              DEC     E                   
1176: 06 1E           LD      B,$1E               
1178: 03              INC     BC                  
1179: 19              ADD     HL,DE               
117A: 06 1A           LD      B,$1A               
117C: 04              INC     B                   
117D: 1D              DEC     E                   
117E: 1E 03           LD      E,$03               
1180: 1F              RRA                         
1181: 1C              INC     E                   
1182: 04              INC     B                   
1183: 1B              DEC     DE                  
1184: 05              DEC     B                   
1185: 18 03           JR      $118A               ; {}
1187: 1F              RRA                         
1188: 05              DEC     B                   
1189: 1C              INC     E                   
118A: 04              INC     B                   
118B: 1B              DEC     DE                  
118C: 05              DEC     B                   
118D: 18 03           JR      $1192               ; {}
118F: 15              DEC     D                   
1190: 16 17           LD      D,$17               
1192: 14              INC     D                   
1193: 1F              RRA                         
1194: 05              DEC     B                   
1195: 05              DEC     B                   
1196: 05              DEC     B                   
1197: 05              DEC     B                   
1198: 05              DEC     B                   
1199: 05              DEC     B                   
119A: 05              DEC     B                   
119B: 1C              INC     E                   
119C: 04              INC     B                   
119D: 1D              DEC     E                   
119E: 1A              LD      A,(DE)              
119F: 1B              DEC     DE                  
11A0: 00              NOP                         
11A1: FF              RST     0X38                
11A2: FF              RST     0X38                
11A3: FF              RST     0X38                
11A4: 0B              DEC     BC                  
11A5: 0C              INC     C                   
11A6: 0D              DEC     C                   
11A7: 0E 0B           LD      C,$0B               
11A9: 0C              INC     C                   
11AA: 0D              DEC     C                   
11AB: 0E 0B           LD      C,$0B               
11AD: 0C              INC     C                   
11AE: 0D              DEC     C                   
11AF: 0E 02           LD      C,$02               
11B1: 02              LD      (BC),A              
11B2: 02              LD      (BC),A              
11B3: 02              LD      (BC),A              
11B4: 02              LD      (BC),A              
11B5: 02              LD      (BC),A              
11B6: 02              LD      (BC),A              
11B7: 02              LD      (BC),A              
11B8: 05              DEC     B                   
11B9: 05              DEC     B                   
11BA: 18 03           JR      $11BF               ; {}
11BC: 19              ADD     HL,DE               
11BD: 1A              LD      A,(DE)              
11BE: 04              INC     B                   
11BF: 1B              DEC     DE                  
11C0: 05              DEC     B                   
11C1: 18 03           JR      $11C6               ; {}
11C3: 1F              RRA                         
11C4: 05              DEC     B                   
11C5: 18 03           JR      $11CA               ; {}
11C7: 1F              RRA                         
11C8: 05              DEC     B                   
11C9: 05              DEC     B                   
11CA: 18 1F           JR      $11EB               ; {}
11CC: 00              NOP                         
11CD: FF              RST     0X38                
11CE: FF              RST     0X38                
11CF: FF              RST     0X38                
11D0: 0B              DEC     BC                  
11D1: 0C              INC     C                   
11D2: 0D              DEC     C                   
11D3: 0E 0B           LD      C,$0B               
11D5: 0C              INC     C                   
11D6: 06 06           LD      B,$06               
11D8: 09              ADD     HL,BC               
11D9: 09              ADD     HL,BC               
11DA: 09              ADD     HL,BC               
11DB: 0A              LD      A,(BC)              
11DC: 09              ADD     HL,BC               
11DD: 09              ADD     HL,BC               
11DE: 0A              LD      A,(BC)              
11DF: 09              ADD     HL,BC               
11E0: 09              ADD     HL,BC               
11E1: 09              ADD     HL,BC               
11E2: 06 1A           LD      B,$1A               
11E4: 04              INC     B                   
11E5: 11 12 13        LD      DE,$1312            
11E8: 10 08           DJNZ    $11F2               ; {}
11EA: 08              EX      AF,AF'              
11EB: 08              EX      AF,AF'              
11EC: 07              RLCA                        
11ED: 07              RLCA                        
11EE: 07              RLCA                        
11EF: 08              EX      AF,AF'              
11F0: 08              EX      AF,AF'              
11F1: 08              EX      AF,AF'              
11F2: 05              DEC     B                   
11F3: 05              DEC     B                   
11F4: 05              DEC     B                   
11F5: 05              DEC     B                   
11F6: 05              DEC     B                   
11F7: 05              DEC     B                   
11F8: 05              DEC     B                   
11F9: 05              DEC     B                   
11FA: 05              DEC     B                   
11FB: 05              DEC     B                   
11FC: 05              DEC     B                   
11FD: 00              NOP                         
11FE: FF              RST     0X38                
11FF: FF              RST     0X38                
1200: 1C              INC     E                   
1201: 11 12 13        LD      DE,$1312            
1204: 10 04           DJNZ    $120A               ; {}
1206: 1D              DEC     E                   
1207: 0D              DEC     C                   
1208: 0E 0B           LD      C,$0B               
120A: 0C              INC     C                   
120B: 0D              DEC     C                   
120C: 0E 0B           LD      C,$0B               
120E: 0C              INC     C                   
120F: 1E 1F           LD      E,$1F               
1211: 05              DEC     B                   
1212: 18 19           JR      $122D               ; {}
1214: 0D              DEC     C                   
1215: 0E 0B           LD      C,$0B               
1217: 0C              INC     C                   
1218: 1E 1F           LD      E,$1F               
121A: 05              DEC     B                   
121B: 05              DEC     B                   
121C: 05              DEC     B                   
121D: 05              DEC     B                   
121E: 05              DEC     B                   
121F: 18 19           JR      $123A               ; {}
1221: 0D              DEC     C                   
1222: 0E 0B           LD      C,$0B               
1224: 0C              INC     C                   
1225: 06 1E           LD      B,$1E               
1227: 1F              RRA                         
1228: 05              DEC     B                   
1229: 05              DEC     B                   
122A: 05              DEC     B                   
122B: 05              DEC     B                   
122C: 18 19           JR      $1247               ; {}
122E: 06 1E           LD      B,$1E               
1230: 1F              RRA                         
1231: 05              DEC     B                   
1232: 05              DEC     B                   
1233: 05              DEC     B                   
1234: 05              DEC     B                   
1235: 05              DEC     B                   
1236: 05              DEC     B                   
1237: 05              DEC     B                   
1238: 05              DEC     B                   
1239: 1C              INC     E                   
123A: 04              INC     B                   
123B: 04              INC     B                   
123C: 1D              DEC     E                   
123D: 1A              LD      A,(DE)              
123E: 04              INC     B                   
123F: 1B              DEC     DE                  
1240: 00              NOP                         
1241: FF              RST     0X38                
1242: FF              RST     0X38                
1243: FF              RST     0X38                
1244: 18 03           JR      $1249               ; {}
1246: 03              INC     BC                  
1247: 19              ADD     HL,DE               
1248: 06 06           LD      B,$06               
124A: 06 06           LD      B,$06               
124C: 06 06           LD      B,$06               
124E: 06 06           LD      B,$06               
1250: 06 06           LD      B,$06               
1252: 06 06           LD      B,$06               
1254: 1A              LD      A,(DE)              
1255: 04              INC     B                   
1256: 1B              DEC     DE                  
1257: 05              DEC     B                   
1258: 1C              INC     E                   
1259: 04              INC     B                   
125A: 1D              DEC     E                   
125B: 06 1E           LD      B,$1E               
125D: 03              INC     BC                  
125E: 03              INC     BC                  
125F: 19              ADD     HL,DE               
1260: 06 1A           LD      B,$1A               
1262: 04              INC     B                   
1263: 04              INC     B                   
1264: 04              INC     B                   
1265: 1B              DEC     DE                  
1266: 05              DEC     B                   
1267: 18 03           JR      $126C               ; {}
1269: 03              INC     BC                  
126A: 1F              RRA                         
126B: 05              DEC     B                   
126C: 1C              INC     E                   
126D: 04              INC     B                   
126E: 1D              DEC     E                   
126F: 06 1A           LD      B,$1A               
1271: 04              INC     B                   
1272: 1B              DEC     DE                  
1273: 05              DEC     B                   
1274: 05              DEC     B                   
1275: 05              DEC     B                   
1276: 05              DEC     B                   
1277: 05              DEC     B                   
1278: 05              DEC     B                   
1279: 05              DEC     B                   
127A: 05              DEC     B                   
127B: 05              DEC     B                   
127C: 05              DEC     B                   
127D: 05              DEC     B                   
127E: 05              DEC     B                   
127F: 18 03           JR      $1284               ; {}
1281: 19              ADD     HL,DE               
1282: 1E 1F           LD      E,$1F               
1284: 00              NOP                         
1285: FF              RST     0X38                
1286: FF              RST     0X38                
1287: FF              RST     0X38                
1288: 0B              DEC     BC                  
1289: 0C              INC     C                   
128A: 1A              LD      A,(DE)              
128B: 1D              DEC     E                   
128C: 1E 03           LD      E,$03               
128E: 19              ADD     HL,DE               
128F: 06 1A           LD      B,$1A               
1291: 04              INC     B                   
1292: 04              INC     B                   
1293: 1D              DEC     E                   
1294: 06 1E           LD      B,$1E               
1296: 03              INC     BC                  
1297: 03              INC     BC                  
1298: 03              INC     BC                  
1299: 19              ADD     HL,DE               
129A: 06 06           LD      B,$06               
129C: 1A              LD      A,(DE)              
129D: 04              INC     B                   
129E: 04              INC     B                   
129F: 04              INC     B                   
12A0: 04              INC     B                   
12A1: 1D              DEC     E                   
12A2: 06 06           LD      B,$06               
12A4: 1E 03           LD      E,$03               
12A6: 03              INC     BC                  
12A7: 03              INC     BC                  
12A8: 03              INC     BC                  
12A9: 03              INC     BC                  
12AA: 03              INC     BC                  
12AB: 1F              RRA                         
12AC: 05              DEC     B                   
12AD: 05              DEC     B                   
12AE: 1C              INC     E                   
12AF: 04              INC     B                   
12B0: 04              INC     B                   
12B1: 04              INC     B                   
12B2: 04              INC     B                   
12B3: 1B              DEC     DE                  
12B4: 05              DEC     B                   
12B5: 05              DEC     B                   
12B6: 18 03           JR      $12BB               ; {}
12B8: 03              INC     BC                  
12B9: 03              INC     BC                  
12BA: 1F              RRA                         
12BB: 05              DEC     B                   
12BC: 1C              INC     E                   
12BD: 04              INC     B                   
12BE: 04              INC     B                   
12BF: 1B              DEC     DE                  
12C0: 05              DEC     B                   
12C1: 18 03           JR      $12C6               ; {}
12C3: 1F              RRA                         
12C4: 1C              INC     E                   
12C5: 1B              DEC     DE                  
12C6: 05              DEC     B                   
12C7: 05              DEC     B                   
12C8: 00              NOP                         
12C9: FF              RST     0X38                
12CA: 18 03           JR      $12CF               ; {}
12CC: 19              ADD     HL,DE               
12CD: 06 06           LD      B,$06               
12CF: 06 06           LD      B,$06               
12D1: 06 06           LD      B,$06               
12D3: 1A              LD      A,(DE)              
12D4: 1D              DEC     E                   
12D5: 1E 19           LD      E,$19               
12D7: 1A              LD      A,(DE)              
12D8: 1D              DEC     E                   
12D9: 06 1E           LD      B,$1E               
12DB: 19              ADD     HL,DE               
12DC: 06 1E           LD      B,$1E               
12DE: 15              DEC     D                   
12DF: 16 17           LD      D,$17               
12E1: 14              INC     D                   
12E2: 07              RLCA                        
12E3: 07              RLCA                        
12E4: 07              RLCA                        
12E5: 08              EX      AF,AF'              
12E6: 08              EX      AF,AF'              
12E7: 08              EX      AF,AF'              
12E8: 08              EX      AF,AF'              
12E9: 05              DEC     B                   
12EA: 05              DEC     B                   
12EB: 18 03           JR      $12F0               ; {}
12ED: 03              INC     BC                  
12EE: 19              ADD     HL,DE               
12EF: 06 06           LD      B,$06               
12F1: 1A              LD      A,(DE)              
12F2: 04              INC     B                   
12F3: 04              INC     B                   
12F4: 1B              DEC     DE                  
12F5: 08              EX      AF,AF'              
12F6: 08              EX      AF,AF'              
12F7: 08              EX      AF,AF'              
12F8: 08              EX      AF,AF'              
12F9: 05              DEC     B                   
12FA: 05              DEC     B                   
12FB: 05              DEC     B                   
12FC: 05              DEC     B                   
12FD: 18 1F           JR      $131E               ; {}
12FF: 00              NOP                         
1300: 0B              DEC     BC                  
1301: 0C              INC     C                   
1302: 0A              LD      A,(BC)              
1303: 0A              LD      A,(BC)              
1304: 09              ADD     HL,BC               
1305: 09              ADD     HL,BC               
1306: 09              ADD     HL,BC               
1307: 0A              LD      A,(BC)              
1308: 0A              LD      A,(BC)              
1309: 09              ADD     HL,BC               
130A: 09              ADD     HL,BC               
130B: 09              ADD     HL,BC               
130C: 0A              LD      A,(BC)              
130D: 09              ADD     HL,BC               
130E: 09              ADD     HL,BC               
130F: 16 17           LD      D,$17               
1311: 14              INC     D                   
1312: 07              RLCA                        
1313: 07              RLCA                        
1314: 07              RLCA                        
1315: 08              EX      AF,AF'              
1316: 08              EX      AF,AF'              
1317: 08              EX      AF,AF'              
1318: 08              EX      AF,AF'              
1319: 07              RLCA                        
131A: 07              RLCA                        
131B: 08              EX      AF,AF'              
131C: 08              EX      AF,AF'              
131D: 08              EX      AF,AF'              
131E: 08              EX      AF,AF'              
131F: 07              RLCA                        
1320: 08              EX      AF,AF'              
1321: 11 12 13        LD      DE,$1312            
1324: 00              NOP                         
1325: FF              RST     0X38                
1326: FF              RST     0X38                
1327: FF              RST     0X38                
1328: 0B              DEC     BC                  
1329: 0C              INC     C                   
132A: 09              ADD     HL,BC               
132B: 09              ADD     HL,BC               
132C: 0A              LD      A,(BC)              
132D: 09              ADD     HL,BC               
132E: 09              ADD     HL,BC               
132F: 0A              LD      A,(BC)              
1330: 0A              LD      A,(BC)              
1331: 0A              LD      A,(BC)              
1332: 0A              LD      A,(BC)              
1333: 09              ADD     HL,BC               
1334: 0A              LD      A,(BC)              
1335: 0A              LD      A,(BC)              
1336: 0A              LD      A,(BC)              
1337: 12              LD      (DE),A              
1338: 13              INC     DE                  
1339: 10 04           DJNZ    $133F               ; {}
133B: 04              INC     B                   
133C: 04              INC     B                   
133D: 1B              DEC     DE                  
133E: 18 03           JR      $1343               ; {}
1340: 03              INC     BC                  
1341: 07              RLCA                        
1342: 07              RLCA                        
1343: 08              EX      AF,AF'              
1344: 08              EX      AF,AF'              
1345: 07              RLCA                        
1346: 07              RLCA                        
1347: 08              EX      AF,AF'              
1348: 08              EX      AF,AF'              
1349: 07              RLCA                        
134A: 07              RLCA                        
134B: 07              RLCA                        
134C: 07              RLCA                        
134D: 07              RLCA                        
134E: 00              NOP                         
134F: FF              RST     0X38                
1350: FF              RST     0X38                
1351: FF              RST     0X38                
1352: FF              RST     0X38                
1353: FF              RST     0X38                
1354: 1C              INC     E                   
1355: 11 12 13        LD      DE,$1312            
1358: 10 1D           DJNZ    $1377               ; {}
135A: 0D              DEC     C                   
135B: 0E 0B           LD      C,$0B               
135D: 0C              INC     C                   
135E: 09              ADD     HL,BC               
135F: 0A              LD      A,(BC)              
1360: 09              ADD     HL,BC               
1361: 09              ADD     HL,BC               
1362: 0A              LD      A,(BC)              
1363: 09              ADD     HL,BC               
1364: 09              ADD     HL,BC               
1365: 09              ADD     HL,BC               
1366: 06 1A           LD      B,$1A               
1368: 04              INC     B                   
1369: 1B              DEC     DE                  
136A: 05              DEC     B                   
136B: 18 03           JR      $1370               ; {}
136D: 19              ADD     HL,DE               
136E: 09              ADD     HL,BC               
136F: 09              ADD     HL,BC               
1370: 0D              DEC     C                   
1371: 0E 0B           LD      C,$0B               
1373: 0C              INC     C                   
1374: 0D              DEC     C                   
1375: 0E 02           LD      C,$02               
1377: 02              LD      (BC),A              
1378: 02              LD      (BC),A              
1379: 02              LD      (BC),A              
137A: 02              LD      (BC),A              
137B: 02              LD      (BC),A              
137C: 02              LD      (BC),A              
137D: 02              LD      (BC),A              
137E: 02              LD      (BC),A              
137F: 02              LD      (BC),A              
1380: 02              LD      (BC),A              
1381: 02              LD      (BC),A              
1382: 08              EX      AF,AF'              
1383: 07              RLCA                        
1384: 07              RLCA                        
1385: 08              EX      AF,AF'              
1386: 07              RLCA                        
1387: 07              RLCA                        
1388: 08              EX      AF,AF'              
1389: 08              EX      AF,AF'              
138A: 07              RLCA                        
138B: 07              RLCA                        
138C: 07              RLCA                        
138D: 07              RLCA                        
138E: 07              RLCA                        
138F: 05              DEC     B                   
1390: 05              DEC     B                   
1391: 05              DEC     B                   
1392: 05              DEC     B                   
1393: 05              DEC     B                   
1394: 05              DEC     B                   
1395: 1C              INC     E                   
1396: 11 12 13        LD      DE,$1312            
1399: 00              NOP                         
139A: FF              RST     0X38                
139B: FF              RST     0X38                
139C: 0B              DEC     BC                  
139D: 0C              INC     C                   
139E: 0D              DEC     C                   
139F: 0E 0B           LD      C,$0B               
13A1: 0C              INC     C                   
13A2: 0D              DEC     C                   
13A3: 0E 0B           LD      C,$0B               
13A5: 0C              INC     C                   
13A6: 1A              LD      A,(DE)              
13A7: 1D              DEC     E                   
13A8: 06 1E           LD      B,$1E               
13AA: 19              ADD     HL,DE               
13AB: 06 06           LD      B,$06               
13AD: 1A              LD      A,(DE)              
13AE: 04              INC     B                   
13AF: 1B              DEC     DE                  
13B0: 1C              INC     E                   
13B1: 04              INC     B                   
13B2: 1D              DEC     E                   
13B3: 1A              LD      A,(DE)              
13B4: 04              INC     B                   
13B5: 1B              DEC     DE                  
13B6: 1C              INC     E                   
13B7: 04              INC     B                   
13B8: 1D              DEC     E                   
13B9: 1A              LD      A,(DE)              
13BA: 04              INC     B                   
13BB: 1B              DEC     DE                  
13BC: 05              DEC     B                   
13BD: 18 07           JR      $13C6               ; {}
13BF: 07              RLCA                        
13C0: 07              RLCA                        
13C1: 08              EX      AF,AF'              
13C2: 08              EX      AF,AF'              
13C3: 07              RLCA                        
13C4: 07              RLCA                        
13C5: 07              RLCA                        
13C6: 07              RLCA                        
13C7: 08              EX      AF,AF'              
13C8: 08              EX      AF,AF'              
13C9: 07              RLCA                        
13CA: 07              RLCA                        
13CB: 07              RLCA                        
13CC: 07              RLCA                        
13CD: 00              NOP                         
13CE: FF              RST     0X38                
13CF: FF              RST     0X38                
13D0: 14              INC     D                   
13D1: 03              INC     BC                  
13D2: 19              ADD     HL,DE               
13D3: 0D              DEC     C                   
13D4: 0E 0B           LD      C,$0B               
13D6: 0C              INC     C                   
13D7: 0A              LD      A,(BC)              
13D8: 0A              LD      A,(BC)              
13D9: 0A              LD      A,(BC)              
13DA: 09              ADD     HL,BC               
13DB: 0A              LD      A,(BC)              
13DC: 0A              LD      A,(BC)              
13DD: 0A              LD      A,(BC)              
13DE: 09              ADD     HL,BC               
13DF: 0A              LD      A,(BC)              
13E0: 0A              LD      A,(BC)              
13E1: 0A              LD      A,(BC)              
13E2: 06 1E           LD      B,$1E               
13E4: 15              DEC     D                   
13E5: 16 17           LD      D,$17               
13E7: 14              INC     D                   
13E8: 03              INC     BC                  
13E9: 1F              RRA                         
13EA: 05              DEC     B                   
13EB: 05              DEC     B                   
13EC: 08              EX      AF,AF'              
13ED: 07              RLCA                        
13EE: 07              RLCA                        
13EF: 07              RLCA                        
13F0: 08              EX      AF,AF'              
13F1: 07              RLCA                        
13F2: 07              RLCA                        
13F3: 07              RLCA                        
13F4: 08              EX      AF,AF'              
13F5: 08              EX      AF,AF'              
13F6: 05              DEC     B                   
13F7: 05              DEC     B                   
13F8: 05              DEC     B                   
13F9: 05              DEC     B                   
13FA: 05              DEC     B                   
13FB: 00              NOP                         
13FC: FF              RST     0X38                
13FD: FF              RST     0X38                
13FE: FF              RST     0X38                
13FF: FF              RST     0X38                
1400: 30 40           JR      NC,$1442            ; {}
1402: 31 41 32        LD      SP,$3241            
1405: 42              LD      B,D                 
1406: 33              INC     SP                  
1407: 43              LD      B,E                 
1408: 34              INC     (HL)                
1409: 44              LD      B,H                 
140A: 35              DEC     (HL)                
140B: 45              LD      B,L                 
140C: 36 46           LD      (HL),$46            
140E: 37              SCF                         
140F: 47              LD      B,A                 
1410: 38 48           JR      C,$145A             ; {}
1412: 39              ADD     HL,SP               
1413: 49              LD      C,C                 
1414: 3A 4A 3B        LD      A,($3B4A)           ; {}
1417: 4B              LD      C,E                 
1418: 3C              INC     A                   
1419: 4C              LD      C,H                 
141A: 3D              DEC     A                   
141B: 4D              LD      C,L                 
141C: 3E 4E           LD      A,$4E               
141E: 3F              CCF                         
141F: 4F              LD      C,A                 
1420: 60              LD      H,B                 
1421: 61              LD      H,C                 
1422: 62              LD      H,D                 
1423: 63              LD      H,E                 
1424: 64              LD      H,H                 
1425: 65              LD      H,L                 
1426: 66              LD      H,(HL)              
1427: 67              LD      H,A                 
1428: 69              LD      L,C                 
1429: 00              NOP                         
142A: 69              LD      L,C                 
142B: 00              NOP                         
142C: 7A              LD      A,D                 
142D: 7B              LD      A,E                 
142E: 7A              LD      A,D                 
142F: 7B              LD      A,E                 
1430: 6B              LD      L,E                 
1431: 00              NOP                         
1432: 6B              LD      L,E                 
1433: 00              NOP                         
1434: 8C              ADC     A,H                 
1435: 8D              ADC     A,L                 
1436: 8C              ADC     A,H                 
1437: 8D              ADC     A,L                 
1438: 68              LD      L,B                 
1439: 00              NOP                         
143A: 68              LD      L,B                 
143B: 00              NOP                         
143C: 8A              ADC     A,D                 
143D: 9A              SBC     D                   
143E: 8A              ADC     A,D                 
143F: 9A              SBC     D                   
1440: 6A              LD      L,D                 
1441: 00              NOP                         
1442: 6A              LD      L,D                 
1443: 00              NOP                         
1444: 8B              ADC     A,E                 
1445: 9B              SBC     E                   
1446: 8B              ADC     A,E                 
1447: 9B              SBC     E                   
1448: 68              LD      L,B                 
1449: 00              NOP                         
144A: 6B              LD      L,E                 
144B: 00              NOP                         
144C: 6A              LD      L,D                 
144D: 00              NOP                         
144E: 69              LD      L,C                 
144F: 00              NOP                         
1450: 76              HALT                        
1451: 77              LD      (HL),A              
1452: 74              LD      (HL),H              
1453: 75              LD      (HL),L              
1454: 72              LD      (HL),D              
1455: 73              LD      (HL),E              
1456: 70              LD      (HL),B              
1457: 71              LD      (HL),C              
1458: 68              LD      L,B                 
1459: 00              NOP                         
145A: 86              ADD     A,(HL)              
145B: 96              SUB     (HL)                
145C: 69              LD      L,C                 
145D: 00              NOP                         
145E: 87              ADD     A,A                 
145F: 97              SUB     A                   
1460: 6A              LD      L,D                 
1461: 00              NOP                         
1462: 88              ADC     A,B                 
1463: 98              SBC     B                   
1464: 6B              LD      L,E                 
1465: 00              NOP                         
1466: 89              ADC     A,C                 
1467: 99              SBC     C                   
1468: 68              LD      L,B                 
1469: 00              NOP                         
146A: 00              NOP                         
146B: 00              NOP                         
146C: A2              AND     D                   
146D: B2              OR      D                   
146E: A3              AND     E                   
146F: B3              OR      E                   
1470: 69              LD      L,C                 
1471: 00              NOP                         
1472: 00              NOP                         
1473: 00              NOP                         
1474: A4              AND     H                   
1475: B4              OR      H                   
1476: A5              AND     L                   
1477: B5              OR      L                   
1478: 6A              LD      L,D                 
1479: 00              NOP                         
147A: 00              NOP                         
147B: 00              NOP                         
147C: A6              AND     (HL)                
147D: B6              OR      (HL)                
147E: A7              AND     A                   
147F: B7              OR      A                   
1480: 6B              LD      L,E                 
1481: 00              NOP                         
1482: 00              NOP                         
1483: 00              NOP                         
1484: A8              XOR     B                   
1485: B8              CP      B                   
1486: A9              XOR     C                   
1487: B9              CP      C                   
1488: FF              RST     0X38                
1489: FF              RST     0X38                
148A: FF              RST     0X38                
148B: FF              RST     0X38                
148C: 8A              ADC     A,D                 
148D: 9A              SBC     D                   
148E: 00              NOP                         
148F: 00              NOP                         
1490: FF              RST     0X38                
1491: FF              RST     0X38                
1492: FF              RST     0X38                
1493: FF              RST     0X38                
1494: FF              RST     0X38                
1495: FF              RST     0X38                
1496: FF              RST     0X38                
1497: FF              RST     0X38                
1498: FF              RST     0X38                
1499: FF              RST     0X38                
149A: FF              RST     0X38                
149B: FF              RST     0X38                
149C: FF              RST     0X38                
149D: FF              RST     0X38                
149E: FF              RST     0X38                
149F: FF              RST     0X38                
14A0: 8B              ADC     A,E                 
14A1: 9B              SBC     E                   
14A2: 00              NOP                         
14A3: 00              NOP                         
14A4: FF              RST     0X38                
14A5: FF              RST     0X38                
14A6: FF              RST     0X38                
14A7: FF              RST     0X38                
14A8: 8E              ADC     A,(HL)              
14A9: 9E              SBC     (HL)                
14AA: 8F              ADC     A,A                 
14AB: 9F              SBC     A                   
14AC: A0              AND     B                   
14AD: B0              OR      B                   
14AE: A1              AND     C                   
14AF: B1              OR      C                   
14B0: 00              NOP                         
14B1: 00              NOP                         
14B2: 00              NOP                         
14B3: 00              NOP                         
14B4: FF              RST     0X38                
14B5: FF              RST     0X38                
14B6: FF              RST     0X38                
14B7: FF              RST     0X38                
14B8: FF              RST     0X38                
14B9: FF              RST     0X38                
14BA: FF              RST     0X38                
14BB: FF              RST     0X38                
14BC: FF              RST     0X38                
14BD: FF              RST     0X38                
14BE: FF              RST     0X38                
14BF: FF              RST     0X38                
14C0: 9C              SBC     H                   
14C1: 00              NOP                         
14C2: 00              NOP                         
14C3: 00              NOP                         
14C4: 84              ADD     A,H                 
14C5: 94              SUB     H                   
14C6: 85              ADD     A,L                 
14C7: 95              SUB     L                   
14C8: 82              ADD     A,D                 
14C9: 92              SUB     D                   
14CA: 83              ADD     A,E                 
14CB: 93              SUB     E                   
14CC: 80              ADD     A,B                 
14CD: 90              SUB     B                   
14CE: 81              ADD     A,C                 
14CF: 91              SUB     C                   
14D0: 9D              SBC     L                   
14D1: 00              NOP                         
14D2: 00              NOP                         
14D3: 00              NOP                         
14D4: AE              XOR     (HL)                
14D5: BE              CP      (HL)                
14D6: AF              XOR     A                   
14D7: BF              CP      A                   
14D8: AC              XOR     H                   
14D9: BC              CP      H                   
14DA: AD              XOR     L                   
14DB: 00              NOP                         
14DC: AA              XOR     D                   
14DD: BA              CP      D                   
14DE: AB              XOR     E                   
14DF: BB              CP      E                   
14E0: 47              LD      B,A                 
14E1: 3A 00 78        LD      A,($7800)           ; 78xx DSW0
14E4: E6 10           AND     $10                 ; Coinage
14E6: C8              RET     Z                   
14E7: EB              EX      DE,HL               
14E8: 7A              LD      A,D                 
14E9: FE 18           CP      $18                 
14EB: C0              RET     NZ                  
14EC: 7B              LD      A,E                 
14ED: FE 95           CP      $95                 
14EF: 36 22           LD      (HL),$22            
14F1: C8              RET     Z                   
14F2: FE 9A           CP      $9A                 
14F4: 36 13           LD      (HL),$13            
14F6: C8              RET     Z                   
14F7: FE B5           CP      $B5                 
14F9: 36 24           LD      (HL),$24            
14FB: C8              RET     Z                   
14FC: 70              LD      (HL),B              
14FD: C9              RET                         
14FE: FF              RST     0X38                
14FF: FF              RST     0X38                
1500: 08              EX      AF,AF'              
1501: 6C              LD      L,H                 
1502: 09              ADD     HL,BC               
1503: 60              LD      H,B                 
1504: 08              EX      AF,AF'              
1505: 6C              LD      L,H                 
1506: 09              ADD     HL,BC               
1507: 60              LD      H,B                 
1508: 08              EX      AF,AF'              
1509: 6C              LD      L,H                 
150A: 09              ADD     HL,BC               
150B: 60              LD      H,B                 
150C: 08              EX      AF,AF'              
150D: 6C              LD      L,H                 
150E: 09              ADD     HL,BC               
150F: 60              LD      H,B                 
1510: 08              EX      AF,AF'              
1511: 6C              LD      L,H                 
1512: 09              ADD     HL,BC               
1513: 60              LD      H,B                 
1514: 08              EX      AF,AF'              
1515: 6C              LD      L,H                 
1516: 09              ADD     HL,BC               
1517: 60              LD      H,B                 
1518: 08              EX      AF,AF'              
1519: 6C              LD      L,H                 
151A: 09              ADD     HL,BC               
151B: 60              LD      H,B                 
151C: 09              ADD     HL,BC               
151D: 60              LD      H,B                 
151E: 09              ADD     HL,BC               
151F: 60              LD      H,B                 
1520: 10 00           DJNZ    $1522               ; {}
1522: 10 00           DJNZ    $1524               ; {}
1524: 10 00           DJNZ    $1526               ; {}
1526: 10 00           DJNZ    $1528               ; {}
1528: 10 00           DJNZ    $152A               ; {}
152A: 10 00           DJNZ    $152C               ; {}
152C: 10 00           DJNZ    $152E               ; {}
152E: 10 00           DJNZ    $1530               ; {}
1530: 10 00           DJNZ    $1532               ; {}
1532: 10 00           DJNZ    $1534               ; {}
1534: 10 00           DJNZ    $1536               ; {}
1536: 10 00           DJNZ    $1538               ; {}
1538: 10 00           DJNZ    $153A               ; {}
153A: 10 00           DJNZ    $153C               ; {}
153C: 10 00           DJNZ    $153E               ; {}
153E: 10 00           DJNZ    $1540               ; {}
1540: 50              LD      D,B                 
1541: 20 70           JR      NZ,$15B3            ; {}
1543: 20 60           JR      NZ,$15A5            ; {}
1545: 28 60           JR      Z,$15A7             ; {}
1547: 38 50           JR      C,$1599             ; {}
1549: 40              LD      B,B                 
154A: 70              LD      (HL),B              
154B: 40              LD      B,B                 
154C: 40              LD      B,B                 
154D: 38 80           JR      C,$14CF             ; {}
154F: 38 30           JR      C,$1581             ; {}
1551: 30 90           JR      NC,$14E3            ; {}
1553: 30 20           JR      NC,$1575            ; {}
1555: 38 A0           JR      C,$14F7             ; {}
1557: 38 18           JR      C,$1571             ; {}
1559: 48              LD      C,B                 
155A: A8              XOR     B                   
155B: 48              LD      C,B                 
155C: 60              LD      H,B                 
155D: 48              LD      C,B                 
155E: 60              LD      H,B                 
155F: 58              LD      E,B                 
1560: 60              LD      H,B                 
1561: 48              LD      C,B                 
1562: 60              LD      H,B                 
1563: 58              LD      E,B                 
1564: 48              LD      C,B                 
1565: 58              LD      E,B                 
1566: 78              LD      A,B                 
1567: 58              LD      E,B                 
1568: 38 50           JR      C,$15BA             ; {}
156A: 88              ADC     A,B                 
156B: 50              LD      D,B                 
156C: 28 48           JR      Z,$15B6             ; {}
156E: 98              SBC     B                   
156F: 48              LD      C,B                 
1570: 18 40           JR      $15B2               ; {}
1572: A8              XOR     B                   
1573: 40              LD      B,B                 
1574: 18 30           JR      $15A6               ; {}
1576: A8              XOR     B                   
1577: 30 28           JR      NC,$15A1            ; {}
1579: 28 98           JR      Z,$1513             ; {}
157B: 28 38           JR      Z,$15B5             ; {}
157D: 20 88           JR      NZ,$1507            ; {}
157F: 20 60           JR      NZ,$15E1            ; {}
1581: 20 50           JR      NZ,$15D3            ; {}
1583: 20 70           JR      NZ,$15F5            ; {}
1585: 20 40           JR      NZ,$15C7            ; {}
1587: 28 80           JR      Z,$1509             ; {}
1589: 28 30           JR      Z,$15BB             ; {}
158B: 30 90           JR      NC,$151D            ; {}
158D: 30 20           JR      NC,$15AF            ; {}
158F: 38 A0           JR      C,$1531             ; {}
1591: 38 60           JR      C,$15F3             ; {}
1593: 58              LD      E,B                 
1594: 50              LD      D,B                 
1595: 58              LD      E,B                 
1596: 70              LD      (HL),B              
1597: 58              LD      E,B                 
1598: 40              LD      B,B                 
1599: 58              LD      E,B                 
159A: 80              ADD     A,B                 
159B: 58              LD      E,B                 
159C: 30 58           JR      NC,$15F6            ; {}
159E: 90              SUB     B                   
159F: 58              LD      E,B                 
15A0: 60              LD      H,B                 
15A1: 20 50           JR      NZ,$15F3            ; {}
15A3: 28 70           JR      Z,$1615             ; {}
15A5: 28 40           JR      Z,$15E7             ; {}
15A7: 30 80           JR      NC,$1529            ; {}
15A9: 30 30           JR      NC,$15DB            ; {}
15AB: 38 90           JR      C,$153D             ; {}
15AD: 38 20           JR      C,$15CF             ; {}
15AF: 40              LD      B,B                 
15B0: A0              AND     B                   
15B1: 40              LD      B,B                 
15B2: 60              LD      H,B                 
15B3: 58              LD      E,B                 
15B4: 50              LD      D,B                 
15B5: 58              LD      E,B                 
15B6: 70              LD      (HL),B              
15B7: 58              LD      E,B                 
15B8: 40              LD      B,B                 
15B9: 50              LD      D,B                 
15BA: 80              ADD     A,B                 
15BB: 50              LD      D,B                 
15BC: 30 48           JR      NC,$1606            ; {}
15BE: 90              SUB     B                   
15BF: 48              LD      C,B                 
15C0: 60              LD      H,B                 
15C1: 58              LD      E,B                 
15C2: 50              LD      D,B                 
15C3: 50              LD      D,B                 
15C4: 70              LD      (HL),B              
15C5: 50              LD      D,B                 
15C6: 60              LD      H,B                 
15C7: 48              LD      C,B                 
15C8: 40              LD      B,B                 
15C9: 48              LD      C,B                 
15CA: 80              ADD     A,B                 
15CB: 48              LD      C,B                 
15CC: 50              LD      D,B                 
15CD: 40              LD      B,B                 
15CE: 70              LD      (HL),B              
15CF: 40              LD      B,B                 
15D0: 40              LD      B,B                 
15D1: 38 80           JR      C,$1553             ; {}
15D3: 38 30           JR      C,$1605             ; {}
15D5: 30 90           JR      NC,$1567            ; {}
15D7: 30 20           JR      NC,$15F9            ; {}
15D9: 28 A0           JR      Z,$157B             ; {}
15DB: 28 10           JR      Z,$15ED             ; {}
15DD: 20 B0           JR      NZ,$158F            ; {}
15DF: 20 60           JR      NZ,$1641            ; {}
15E1: 20 50           JR      NZ,$1633            ; {}
15E3: 28 70           JR      Z,$1655             ; {}
15E5: 28 40           JR      Z,$1627             ; {}
15E7: 30 80           JR      NC,$1569            ; {}
15E9: 30 30           JR      NC,$161B            ; {}
15EB: 38 90           JR      C,$157D             ; {}
15ED: 38 20           JR      C,$160F             ; {}
15EF: 40              LD      B,B                 
15F0: A0              AND     B                   
15F1: 40              LD      B,B                 
15F2: 60              LD      H,B                 
15F3: 20 50           JR      NZ,$1645            ; {}
15F5: 28 70           JR      Z,$1667             ; {}
15F7: 28 40           JR      Z,$1639             ; {}
15F9: 30 80           JR      NC,$157B            ; {}
15FB: 30 30           JR      NC,$162D            ; {}
15FD: 38 90           JR      C,$158F             ; {}
15FF: 38 10           JR      C,$1611             ; {}
1601: 14              INC     D                   
1602: 18 1C           JR      $1620               ; {}
1604: 00              NOP                         
1605: 04              INC     B                   
1606: 08              EX      AF,AF'              
1607: 0C              INC     C                   
1608: 20 22           JR      NZ,$162C            ; {}
160A: 24              INC     H                   
160B: 26 28           LD      H,$28               
160D: 2A 2C 2E        LD      HL,($2E2C)          ; {}
1610: 30 32           JR      NC,$1644            ; {}
1612: 34              INC     (HL)                
1613: 36 38           LD      (HL),$38            
1615: 3A 3C 3E        LD      A,($3E3C)           ; {}
1618: 40              LD      B,B                 
1619: 42              LD      B,D                 
161A: 44              LD      B,H                 
161B: 46              LD      B,(HL)              
161C: 5C              LD      E,H                 
161D: 5C              LD      E,H                 
161E: 5E              LD      E,(HL)              
161F: 5E              LD      E,(HL)              
1620: 50              LD      D,B                 
1621: 51              LD      D,C                 
1622: 52              LD      D,D                 
1623: 53              LD      D,E                 
1624: 54              LD      D,H                 
1625: 55              LD      D,L                 
1626: 56              LD      D,(HL)              
1627: 57              LD      D,A                 
1628: FF              RST     0X38                
1629: FF              RST     0X38                
162A: FF              RST     0X38                
162B: FF              RST     0X38                
162C: FF              RST     0X38                
162D: FF              RST     0X38                
162E: FF              RST     0X38                
162F: FF              RST     0X38                
1630: 48              LD      C,B                 
1631: 48              LD      C,B                 
1632: 50              LD      D,B                 
1633: 50              LD      D,B                 
1634: 4A              LD      C,D                 
1635: 4A              LD      C,D                 
1636: 52              LD      D,D                 
1637: 52              LD      D,D                 
1638: 4C              LD      C,H                 
1639: 4C              LD      C,H                 
163A: 54              LD      D,H                 
163B: 54              LD      D,H                 
163C: 4E              LD      C,(HL)              
163D: 4E              LD      C,(HL)              
163E: 56              LD      D,(HL)              
163F: 56              LD      D,(HL)              
1640: 48              LD      C,B                 
1641: 48              LD      C,B                 
1642: 56              LD      D,(HL)              
1643: 56              LD      D,(HL)              
1644: 4E              LD      C,(HL)              
1645: 4E              LD      C,(HL)              
1646: 54              LD      D,H                 
1647: 54              LD      D,H                 
1648: 4C              LD      C,H                 
1649: 4C              LD      C,H                 
164A: 52              LD      D,D                 
164B: 52              LD      D,D                 
164C: 4A              LD      C,D                 
164D: 4A              LD      C,D                 
164E: 50              LD      D,B                 
164F: 50              LD      D,B                 
1650: 68              LD      L,B                 
1651: 68              LD      L,B                 
1652: 6C              LD      L,H                 
1653: 6C              LD      L,H                 
1654: 70              LD      (HL),B              
1655: 70              LD      (HL),B              
1656: 74              LD      (HL),H              
1657: 74              LD      (HL),H              
1658: 78              LD      A,B                 
1659: 78              LD      A,B                 
165A: 7C              LD      A,H                 
165B: 7C              LD      A,H                 
165C: 80              ADD     A,B                 
165D: 80              ADD     A,B                 
165E: 84              ADD     A,H                 
165F: 84              ADD     A,H                 
1660: 68              LD      L,B                 
1661: 68              LD      L,B                 
1662: 84              ADD     A,H                 
1663: 84              ADD     A,H                 
1664: 80              ADD     A,B                 
1665: 80              ADD     A,B                 
1666: 7C              LD      A,H                 
1667: 7C              LD      A,H                 
1668: 78              LD      A,B                 
1669: 78              LD      A,B                 
166A: 74              LD      (HL),H              
166B: 74              LD      (HL),H              
166C: 70              LD      (HL),B              
166D: 70              LD      (HL),B              
166E: 6C              LD      L,H                 
166F: 6C              LD      L,H                 
1670: 58              LD      E,B                 
1671: 58              LD      E,B                 
1672: 5A              LD      E,D                 
1673: 5A              LD      E,D                 
1674: 5C              LD      E,H                 
1675: 5C              LD      E,H                 
1676: 5E              LD      E,(HL)              
1677: 5E              LD      E,(HL)              
1678: 60              LD      H,B                 
1679: 60              LD      H,B                 
167A: 62              LD      H,D                 
167B: 62              LD      H,D                 
167C: 64              LD      H,H                 
167D: 64              LD      H,H                 
167E: 66              LD      H,(HL)              
167F: 66              LD      H,(HL)              
1680: 78              LD      A,B                 
1681: FF              RST     0X38                
1682: A0              AND     B                   
1683: FF              RST     0X38                
1684: FF              RST     0X38                
1685: A8              XOR     B                   
1686: FF              RST     0X38                
1687: AC              XOR     H                   
1688: C0              RET     NZ                  
1689: FF              RST     0X38                
168A: C8              RET     Z                   
168B: FF              RST     0X38                
168C: FF              RST     0X38                
168D: C4 FF CC        CALL    NZ,$CCFF            
1690: D0              RET     NC                  
1691: FF              RST     0X38                
1692: D8              RET     C                   
1693: FF              RST     0X38                
1694: FF              RST     0X38                
1695: D4 FF DC        CALL    NC,$DCFF            
1698: FF              RST     0X38                
1699: FF              RST     0X38                
169A: FF              RST     0X38                
169B: FF              RST     0X38                
169C: FF              RST     0X38                
169D: FF              RST     0X38                
169E: FF              RST     0X38                
169F: FF              RST     0X38                
16A0: FF              RST     0X38                
16A1: FF              RST     0X38                
16A2: FF              RST     0X38                
16A3: 01 02 08        LD      BC,$0802            
16A6: 01 02 08        LD      BC,$0802            
16A9: 01 02 0C        LD      BC,$0C02            
16AC: 01 02 10        LD      BC,$1002            
16AF: 03              INC     BC                  
16B0: 04              INC     B                   
16B1: 14              INC     D                   
16B2: 03              INC     BC                  
16B3: 04              INC     B                   
16B4: 18 04           JR      $16BA               ; {}
16B6: 01 88 04        LD      BC,$0488            
16B9: 01 90 04        LD      BC,$0490            
16BC: 01 80 04        LD      BC,$0480            
16BF: 01 80 03        LD      BC,$0380            
16C2: 04              INC     B                   
16C3: 70              LD      (HL),B              
16C4: 03              INC     BC                  
16C5: 04              INC     B                   
16C6: 74              LD      (HL),H              
16C7: 03              INC     BC                  
16C8: 04              INC     B                   
16C9: 78              LD      A,B                 
16CA: 03              INC     BC                  
16CB: 04              INC     B                   
16CC: 7C              LD      A,H                 
16CD: FF              RST     0X38                
16CE: FF              RST     0X38                
16CF: FF              RST     0X38                
16D0: 01 02 30        LD      BC,$3002            
16D3: 01 02 34        LD      BC,$3402            
16D6: 01 02 38        LD      BC,$3802            
16D9: 01 02 3C        LD      BC,$3C02            
16DC: 01 02 40        LD      BC,$4002            
16DF: 01 02 44        LD      BC,$4402            
16E2: 01 02 48        LD      BC,$4802            
16E5: 01 02 4C        LD      BC,$4C02            
16E8: 04              INC     B                   
16E9: 04              INC     B                   
16EA: 50              LD      D,B                 
16EB: 04              INC     B                   
16EC: 04              INC     B                   
16ED: 54              LD      D,H                 
16EE: 04              INC     B                   
16EF: 04              INC     B                   
16F0: 58              LD      E,B                 
16F1: 04              INC     B                   
16F2: 04              INC     B                   
16F3: 5C              LD      E,H                 
16F4: 04              INC     B                   
16F5: 04              INC     B                   
16F6: 60              LD      H,B                 
16F7: 04              INC     B                   
16F8: 04              INC     B                   
16F9: 64              LD      H,H                 
16FA: 04              INC     B                   
16FB: 04              INC     B                   
16FC: 68              LD      L,B                 
16FD: 04              INC     B                   
16FE: 04              INC     B                   
16FF: 6C              LD      L,H                 
1700: FF              RST     0X38                
1701: FF              RST     0X38                
1702: 01 00 FF        LD      BC,$FF00            
1705: 00              NOP                         
1706: 04              INC     B                   
1707: 00              NOP                         
1708: FC 00 00        CALL    M,$0000             ; {}
170B: FC 00 04        CALL    M,$0400             ; {}
170E: 04              INC     B                   
170F: FE FC           CP      $FC                 
1711: FE 04           CP      $04                 
1713: 02              LD      (BC),A              
1714: FC 02 00        CALL    M,$0002             ; {}
1717: 04              INC     B                   
1718: 00              NOP                         
1719: 04              INC     B                   
171A: 00              NOP                         
171B: 04              INC     B                   
171C: 00              NOP                         
171D: 04              INC     B                   
171E: FF              RST     0X38                
171F: FF              RST     0X38                
1720: FC 00 FC        CALL    M,$FC00             
1723: 00              NOP                         
1724: FC 00 FC        CALL    M,$FC00             
1727: 00              NOP                         
1728: 04              INC     B                   
1729: 00              NOP                         
172A: 04              INC     B                   
172B: 00              NOP                         
172C: 04              INC     B                   
172D: 00              NOP                         
172E: 04              INC     B                   
172F: 00              NOP                         
1730: 04              INC     B                   
1731: FC 04 04        CALL    M,$0404             ; {}
1734: FC 04 FC        CALL    M,$FC04             
1737: FC FC FC        CALL    M,$FCFC             
173A: FC 04 04        CALL    M,$0404             ; {}
173D: 04              INC     B                   
173E: 04              INC     B                   
173F: FC 08 00        CALL    M,$0008             ; {}
1742: 00              NOP                         
1743: FF              RST     0X38                
1744: 01 00 F8        LD      BC,$F800            
1747: FF              RST     0X38                
1748: 08              EX      AF,AF'              
1749: 01 02 FF        LD      BC,$FF02            
174C: 04              INC     B                   
174D: 00              NOP                         
174E: FA FF 08        JP      M,$08FF             ; {}
1751: 01 04 FF        LD      BC,$FF04            
1754: 08              EX      AF,AF'              
1755: 00              NOP                         
1756: FC FF 08        CALL    M,$08FF             ; {}
1759: 05              DEC     B                   
175A: 06 FF           LD      B,$FF               
175C: 08              EX      AF,AF'              
175D: 00              NOP                         
175E: FE FF           CP      $FF                 
1760: 10 10           DJNZ    $1772               ; {}
1762: 88              ADC     A,B                 
1763: 88              ADC     A,B                 
1764: 10 10           DJNZ    $1776               ; {}
1766: 10 10           DJNZ    $1778               ; {}
1768: FF              RST     0X38                
1769: FF              RST     0X38                
176A: FF              RST     0X38                
176B: FF              RST     0X38                
176C: FF              RST     0X38                
176D: FF              RST     0X38                
176E: FF              RST     0X38                
176F: FF              RST     0X38                
1770: EC FC FD        CALL    PE,$FDFC            
1773: F4 ED 30        CALL    P,$30ED             ; {}
1776: 40              LD      B,B                 
1777: F5              PUSH    AF                  
1778: EE 31           XOR     $31                 
177A: 41              LD      B,C                 
177B: F6 EF           OR      $EF                 
177D: FF              RST     0X38                
177E: FE F7           CP      $F7                 
1780: E8              RET     PE                  
1781: F8              RET     M                   
1782: F9              LD      SP,HL               
1783: F0              RET     P                   
1784: E9              JP      (HL)                
1785: 30 40           JR      NC,$17C7            ; {}
1787: F1              POP     AF                  
1788: EA 31 41        JP      PE,$4131            
178B: F2 EB FB        JP      P,$FBEB             
178E: FA F3 E8        JP      M,$E8F3             
1791: F8              RET     M                   
1792: F9              LD      SP,HL               
1793: F0              RET     P                   
1794: E9              JP      (HL)                
1795: E4 E6 F1        CALL    PO,$F1E6            
1798: EA E5 E7        JP      PE,$E7E5            
179B: F2 EB FB        JP      P,$FBEB             
179E: FA F3 00        JP      M,$00F3             ; {}
17A1: 00              NOP                         
17A2: 00              NOP                         
17A3: 00              NOP                         
17A4: 00              NOP                         
17A5: E4 E6 00        CALL    PO,$00E6            ; {}
17A8: 00              NOP                         
17A9: E5              PUSH    HL                  
17AA: E7              RST     0X20                
17AB: 00              NOP                         
17AC: 00              NOP                         
17AD: 00              NOP                         
17AE: 00              NOP                         
17AF: 00              NOP                         
17B0: F0              RET     P                   
17B1: CA C4 BE        JP      Z,$BEC4             
17B4: B8              CP      B                   
17B5: BE              CP      (HL)                
17B6: B8              CP      B                   
17B7: BE              CP      (HL)                
17B8: C8              RET     Z                   
17B9: D8              RET     C                   
17BA: C9              RET                         
17BB: D9              EXX                         
17BC: CA DA CB        JP      Z,$CBDA             
17BF: DB CC           IN      A,($CC)             ; {}
17C1: DC CD DD        CALL    C,$DDCD             
17C4: C0              RET     NZ                  
17C5: C1              POP     BC                  
17C6: C1              POP     BC                  
17C7: C2 00 C0        JP      NZ,$C000            
17CA: 00              NOP                         
17CB: 00              NOP                         
17CC: 00              NOP                         
17CD: C3 00 00        JP      $0000               ; {}
17D0: C4 D4 C5        CALL    NZ,$C5D4            
17D3: D5              PUSH    DE                  
17D4: C3 C3 C3        JP      $C3C3               
17D7: C3 C6 D6        JP      $D6C6               
17DA: C7              RST     0X00                
17DB: D7              RST     0X10                
17DC: FF              RST     0X38                
17DD: FF              RST     0X38                
17DE: FF              RST     0X38                
17DF: FF              RST     0X38                
17E0: 3A 00 78        LD      A,($7800)           ; 78xx DSW0
17E3: E6 10           AND     $10                 ; Coinage
17E5: 3A 8F 43        LD      A,($438F)           ; {ram.CoinCount}
17E8: C8              RET     Z                   
17E9: 0F              RRCA                        
17EA: E6 0F           AND     $0F                 
17EC: C9              RET                         
17ED: FF              RST     0X38                
17EE: FF              RST     0X38                
17EF: FF              RST     0X38                
17F0: 00              NOP                         
17F1: 00              NOP                         
17F2: 00              NOP                         
17F3: 00              NOP                         
17F4: 00              NOP                         
17F5: 00              NOP                         
17F6: 00              NOP                         
17F7: 00              NOP                         
17F8: 00              NOP                         
17F9: 00              NOP                         
17FA: 00              NOP                         
17FB: 00              NOP                         
17FC: 00              NOP                         
17FD: 00              NOP                         
17FE: 00              NOP                         
17FF: 00              NOP                         


1800: 43 20
1802: FF FF FF FF
; " SCORE1  HI-SCORE  SCORE2 "
1806: 00 13 03 0F 12 05 21 00 00 08 09 2B 13 03 0F 12 05 00 00 13 03 0F 12 05 22 00

1820: 43 21
1822: FF FF FF FF
; " 000000   000000   000000 "
1826: 00 20 20 20 20 20 20 00 00 00 20 20 20 20 20 20 00 00 00 20 20 20 20 20 20 00

1840: 43 22
1842: FF FF FF FF
; "   %0     COIN00     %0   "
1846: 00 00 00 7F 20 00 00 00 00 00 03 0F 09 0E 20 20 00 00 00 00 00 7F 20 00 00 00

1860: 43 25
1862: FF FF FF FF
; "       INSERT  COIN       "
1866: 00 00 00 00 00 00 00 09 0E 13 05 12 14 00 00 03 0F 09 0E 00 00 00 00 00 00 00

1880: 43 27
1882: FF FF FF FF
; "   * 1PLAYER   1COIN  *   "
1886: 00 00 00 1F 00 21 10 0C 01 19 05 12 00 00 00 21 03 0F 09 0E 00 00 1F 00 00 00

18A0: 43 29
18A2: FF FF FF FF
; "   * 2PLAYERS  2COINS *   "
18A6: 00 00 00 1F 00 22 10 0C 01 19 05 12 13 00 00 22 03 0F 09 0E 13 00 1F 00 00 00

18C0: 43 2E
18C2: FF FF FF FF
; "   SCORE AVERAGE TABLE    "
18C6: 00 00 00 13 03 0F 12 05 00 01 16 05 12 01 07 05 00 14 01 02 0C 05 00 00 00 00

18E0: 43 30
18E2: FF FF FF FF
; "        20 40 80          "
18E6: 00 00 00 00 00 00 00 00 22 20 00 24 20 00 28 20 00 00 00 00 00 00 00 00 00 00

1900: 43 33
1902: FF FF FF FF
; "        200               "
1906: 00 00 00 00 00 00 00 00 22 20 20 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

1920: 43 36
1922: FF FF FF FF
; "        50 100 ?[100-800] "
1926: 00 00 00 00 00 00 00 00 25 20 00 21 20 20 00 2F 1B 21 20 20 2B 28 20 20 1C 00

1940: 43 39
1942: FF FF FF FF
; "        1000-9000         "
1946: 00 00 00 00 00 00 00 00 21 20 20 20 2B 29 20 20 20 00 00 00 00 00 00 00 00 00

1960: 43 3C
1962: 00 00 32 21
; "PHOENIX% COPYRIGHT 1980   "
1966: 10 08 0F 05 0E 09 18 7E 00 03 0F 10 19 12 09 07 08 14 00 21 29 28 20 00 00 00

1980: 43 3D
1982: 02 05 21 28
; " AMSTAR ELECTRONICS CORP. "
1986: 00 01 0D 13 14 01 12 00 05 0C 05 03 14 12 0F 0E 09 03 13 00 03 0F 12 10 2A 00

19A0: 43 3E
19A2: FF FF FF FF
; "  PHOENIX AZ. U.S.A.      "
19A6: 00 00 10 08 0F 05 0E 09 18 00 01 1A 2A 00 15 2A 13 2A 01 2A 00 00 00 00 00 00

19C0: 43 28
19C2: FF FF FF FF
; "           PUSH           "
19C6: 00 00 00 00 00 00 00 00 00 00 00 10 15 13 08 00 00 00 00 00 00 00 00 00 00 00

19E0: 43 2C
19E2: FF FF FF FF
; "    ONLY 1PLAYER BUTTON   "
19E6: 00 00 00 00 0F 0E 0C 19 00 21 10 0C 01 19 05 12 00 02 15 14 14 0F 0E 00 00 00

1A00: 43 28
1A02: FF FF FF FF
; "        GAME  OVER        "
1A06: 00 00 00 00 00 00 00 00 07 01 0D 05 00 00 0F 16 05 12 00 00 00 00 00 00 00 00

1A20: 43 28
1A22: 00 FF FF FF
; "%%%%%%%%                %%"
1A26: 64 65 64 65 64 65 60 61 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 78 79

1A40: 43 29
1A42: FF FF FF FF
; "%%    %%                %%"
1A46: 64 65 00 00 00 00 64 65 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 7C 7D

1A60: 43 2A
1A62: FF FF FF FF
; "%%%%%%%%                  "
1A66: 64 65 64 65 64 65 60 61 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

1A80: 43 2B
1A82: FF FF FF FF
; "%%                        "
1A86: 64 65 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

1AA0: 43 2C
1AA2: FF FF FF FF
; "%% % % %%% %%% %% % % %  %"
1AA6: 64 65 00 68 00 68 00 68 68 68 00 68 64 65 00 62 63 00 68 00 68 00 68 00 00 68

1AC0: 43 2D
1AC2: FF FF FF FF
; "%% % % % % %   %% % % %%%%"
1AC6: 64 65 00 68 00 68 00 68 00 68 00 68 00 00 00 68 9D 00 68 00 68 00 76 77 70 71

1AE0: 43 2E
1AE2: FF FF FF FF
; "%% %%% % % %%% %%%% %  %% "
1AE6: 64 65 00 68 68 68 00 68 00 68 00 68 62 63 00 68 76 77 68 00 68 00 00 64 65 00

1B00: 43 2F
1B02: 00 00 00 00
; "%% % % % % %   % %% % %%%%"
1B06: 64 65 00 68 00 68 00 68 00 68 00 68 00 00 00 68 00 9D 68 00 68 00 74 75 72 73

1B20: 43 30
1B22: FF FF FF FF
; "%% % % %%% %%% % %% % %  %"
1B26: 64 65 00 68 00 68 00 68 68 68 00 68 64 65 00 68 00 66 67 00 68 00 68 00 00 68
           
1B40: 6C              LD      L,H                 
1B41: 6D              LD      L,L                 
1B42: 6E              LD      L,(HL)              
1B43: 6F              LD      L,A                 
1B44: FF              RST     0X38                
1B45: FF              RST     0X38                
1B46: FF              RST     0X38                
1B47: FF              RST     0X38                
1B48: 6C              LD      L,H                 
1B49: 6D              LD      L,L                 
1B4A: 6E              LD      L,(HL)              
1B4B: 6F              LD      L,A                 
1B4C: 64              LD      H,H                 
1B4D: 65              LD      H,L                 
1B4E: 66              LD      H,(HL)              
1B4F: 67              LD      H,A                 
1B50: 63              LD      H,E                 
1B51: FF              RST     0X38                
1B52: 63              LD      H,E                 
1B53: 61              LD      H,C                 
1B54: 67              LD      H,A                 
1B55: FF              RST     0X38                
1B56: 67              LD      H,A                 
1B57: 65              LD      H,L                 
1B58: 6B              LD      L,E                 
1B59: FF              RST     0X38                
1B5A: 6B              LD      L,E                 
1B5B: 69              LD      L,C                 
1B5C: 6F              LD      L,A                 
1B5D: FF              RST     0X38                
1B5E: 6F              LD      L,A                 
1B5F: 6D              LD      L,L                 
1B60: 80              ADD     A,B                 
1B61: 83              ADD     A,E                 
1B62: 83              ADD     A,E                 
1B63: 85              ADD     A,L                 
1B64: 81              ADD     A,C                 
1B65: 8C              ADC     A,H                 
1B66: 8C              ADC     A,H                 
1B67: 86              ADD     A,(HL)              
1B68: 81              ADD     A,C                 
1B69: 8C              ADC     A,H                 
1B6A: 8C              ADC     A,H                 
1B6B: 86              ADD     A,(HL)              
1B6C: 82              ADD     A,D                 
1B6D: 84              ADD     A,H                 
1B6E: 84              ADD     A,H                 
1B6F: 87              ADD     A,A                 
1B70: 00              NOP                         
1B71: 89              ADC     A,C                 
1B72: 89              ADC     A,C                 
1B73: 00              NOP                         
1B74: 88              ADC     A,B                 
1B75: 8D              ADC     A,L                 
1B76: 8D              ADC     A,L                 
1B77: 8B              ADC     A,E                 
1B78: 88              ADC     A,B                 
1B79: 8D              ADC     A,L                 
1B7A: 8D              ADC     A,L                 
1B7B: 8B              ADC     A,E                 
1B7C: 00              NOP                         
1B7D: 8A              ADC     A,D                 
1B7E: 8A              ADC     A,D                 
1B7F: 00              NOP                         
1B80: 00              NOP                         
1B81: 00              NOP                         
1B82: 00              NOP                         
1B83: 00              NOP                         
1B84: 00              NOP                         
1B85: 80              ADD     A,B                 
1B86: 85              ADD     A,L                 
1B87: 00              NOP                         
1B88: 00              NOP                         
1B89: 82              ADD     A,D                 
1B8A: 87              ADD     A,A                 
1B8B: 00              NOP                         
1B8C: 00              NOP                         
1B8D: 00              NOP                         
1B8E: 00              NOP                         
1B8F: 00              NOP                         
1B90: 1B              DEC     DE                  
1B91: 80              ADD     A,B                 
1B92: 1B              DEC     DE                  
1B93: 70              LD      (HL),B              
1B94: 1B              DEC     DE                  
1B95: 60              LD      H,B                 
1B96: 1B              DEC     DE                  
1B97: 70              LD      (HL),B              
1B98: 17              RLA                         
1B99: F0              RET     P                   
1B9A: 17              RLA                         
1B9B: F0              RET     P                   
1B9C: 17              RLA                         
1B9D: F0              RET     P                   
1B9E: 17              RLA                         
1B9F: F0              RET     P                   
1BA0: 43              LD      B,E                 
1BA1: 2C              INC     L                   
1BA2: 00              NOP                         
1BA3: 00              NOP                         
1BA4: 00              NOP                         
1BA5: 00              NOP                         
1BA6: 00              NOP                         
1BA7: 00              NOP                         
1BA8: 00              NOP                         
1BA9: 21 00 0F        LD      HL,$0F00            
1BAC: 12              LD      (DE),A              
1BAD: 00              NOP                         
1BAE: 22 10 0C        LD      ($0C10),HL          ; {}
1BB1: 01 19 05        LD      BC,$0519            
1BB4: 12              LD      (DE),A              
1BB5: 13              INC     DE                  
1BB6: 00              NOP                         
1BB7: 02              LD      (BC),A              
1BB8: 15              DEC     D                   
1BB9: 14              INC     D                   
1BBA: 14              INC     D                   
1BBB: 0F              RRCA                        
1BBC: 0E 00           LD      C,$00               
1BBE: 00              NOP                         
1BBF: 00              NOP                         
1BC0: 41              LD      B,C                 
1BC1: 54              LD      D,H                 
1BC2: 76              HALT                        
1BC3: 7E              LD      A,(HL)              
1BC4: 42              LD      B,D                 
1BC5: 55              LD      D,L                 
1BC6: 77              LD      (HL),A              
1BC7: 7F              LD      A,A                 
1BC8: 41              LD      B,C                 
1BC9: 56              LD      D,(HL)              
1BCA: 74              LD      (HL),H              
1BCB: 7C              LD      A,H                 
1BCC: 42              LD      B,D                 
1BCD: 57              LD      D,A                 
1BCE: 75              LD      (HL),L              
1BCF: 7D              LD      A,L                 
1BD0: 44              LD      B,H                 
1BD1: 51              LD      D,C                 
1BD2: 72              LD      (HL),D              
1BD3: 7A              LD      A,D                 
1BD4: 45              LD      B,L                 
1BD5: 52              LD      D,D                 
1BD6: 73              LD      (HL),E              
1BD7: 7B              LD      A,E                 
1BD8: 46              LD      B,(HL)              
1BD9: 51              LD      D,C                 
1BDA: 70              LD      (HL),B              
1BDB: 78              LD      A,B                 
1BDC: 47              LD      B,A                 
1BDD: 52              LD      D,D                 
1BDE: 71              LD      (HL),C              
1BDF: 79              LD      A,C                 
1BE0: 41              LD      B,C                 
1BE1: 51              LD      D,C                 
1BE2: 70              LD      (HL),B              
1BE3: 78              LD      A,B                 
1BE4: 42              LD      B,D                 
1BE5: 52              LD      D,D                 
1BE6: 71              LD      (HL),C              
1BE7: 79              LD      A,C                 
1BE8: 41              LD      B,C                 
1BE9: 51              LD      D,C                 
1BEA: 72              LD      (HL),D              
1BEB: 7A              LD      A,D                 
1BEC: 42              LD      B,D                 
1BED: 52              LD      D,D                 
1BEE: 73              LD      (HL),E              
1BEF: 7B              LD      A,E                 
1BF0: 41              LD      B,C                 
1BF1: 51              LD      D,C                 
1BF2: 74              LD      (HL),H              
1BF3: 7C              LD      A,H                 
1BF4: 42              LD      B,D                 
1BF5: 52              LD      D,D                 
1BF6: 75              LD      (HL),L              
1BF7: 7D              LD      A,L                 
1BF8: 41              LD      B,C                 
1BF9: 51              LD      D,C                 
1BFA: 76              HALT                        
1BFB: 7E              LD      A,(HL)              
1BFC: 42              LD      B,D                 
1BFD: 52              LD      D,D                 
1BFE: 77              LD      (HL),A              
1BFF: 7F              LD      A,A                 
1C00: 00              NOP                         
1C01: 01 00 06        LD      BC,$0600            
1C04: 00              NOP                         
1C05: 02              LD      (BC),A              
1C06: 03              INC     BC                  
1C07: 04              INC     B                   
1C08: 00              NOP                         
1C09: 01 00 08        LD      BC,$0800            
1C0C: 00              NOP                         
1C0D: 02              LD      (BC),A              
1C0E: 03              INC     BC                  
1C0F: 04              INC     B                   
1C10: 00              NOP                         
1C11: 00              NOP                         
1C12: 07              RLCA                        
1C13: 00              NOP                         
1C14: 01 02 00        LD      BC,$0002            
1C17: 09              ADD     HL,BC               
1C18: 00              NOP                         
1C19: 03              INC     BC                  
1C1A: 04              INC     B                   
1C1B: 00              NOP                         
1C1C: 00              NOP                         
1C1D: 03              INC     BC                  
1C1E: 04              INC     B                   
1C1F: 00              NOP                         
1C20: 00              NOP                         
1C21: 01 00 02        LD      BC,$0200            
1C24: 00              NOP                         
1C25: 03              INC     BC                  
1C26: 0A              LD      A,(BC)              
1C27: 00              NOP                         
1C28: 04              INC     B                   
1C29: 00              NOP                         
1C2A: 00              NOP                         
1C2B: 01 02 00        LD      BC,$0002            
1C2E: 06 00           LD      B,$00               
1C30: 03              INC     BC                  
1C31: 04              INC     B                   
1C32: 00              NOP                         
1C33: 00              NOP                         
1C34: 01 00 02        LD      BC,$0200            
1C37: 00              NOP                         
1C38: 03              INC     BC                  
1C39: 00              NOP                         
1C3A: 04              INC     B                   
1C3B: 00              NOP                         
1C3C: 03              INC     BC                  
1C3D: 05              DEC     B                   
1C3E: 00              NOP                         
1C3F: 00              NOP                         
1C40: 00              NOP                         
1C41: 00              NOP                         
1C42: 07              RLCA                        
1C43: 00              NOP                         
1C44: 01 00 02        LD      BC,$0200            
1C47: 00              NOP                         
1C48: 00              NOP                         
1C49: 05              DEC     B                   
1C4A: 00              NOP                         
1C4B: 00              NOP                         
1C4C: 03              INC     BC                  
1C4D: 00              NOP                         
1C4E: 04              INC     B                   
1C4F: 01 02 00        LD      BC,$0002            
1C52: 03              INC     BC                  
1C53: 00              NOP                         
1C54: 08              EX      AF,AF'              
1C55: 04              INC     B                   
1C56: 00              NOP                         
1C57: 01 02 06        LD      BC,$0602            
1C5A: 00              NOP                         
1C5B: 03              INC     BC                  
1C5C: 00              NOP                         
1C5D: 04              INC     B                   
1C5E: 00              NOP                         
1C5F: 02              LD      (BC),A              
1C60: 01 02 03        LD      BC,$0302            
1C63: 00              NOP                         
1C64: 05              DEC     B                   
1C65: 00              NOP                         
1C66: 00              NOP                         
1C67: 04              INC     B                   
1C68: 00              NOP                         
1C69: 01 02 00        LD      BC,$0002            
1C6C: 00              NOP                         
1C6D: 03              INC     BC                  
1C6E: 04              INC     B                   
1C6F: 0B              DEC     BC                  
1C70: 00              NOP                         
1C71: 01 00 02        LD      BC,$0200            
1C74: 00              NOP                         
1C75: 03              INC     BC                  
1C76: 00              NOP                         
1C77: 00              NOP                         
1C78: 04              INC     B                   
1C79: 00              NOP                         
1C7A: 00              NOP                         
1C7B: 09              ADD     HL,BC               
1C7C: 00              NOP                         
1C7D: 00              NOP                         
1C7E: 02              LD      (BC),A              
1C7F: 00              NOP                         
1C80: 07              RLCA                        
1C81: 00              NOP                         
1C82: 00              NOP                         
1C83: 01 00 00        LD      BC,$0000            
1C86: 02              LD      (BC),A              
1C87: 00              NOP                         
1C88: 00              NOP                         
1C89: 03              INC     BC                  
1C8A: 00              NOP                         
1C8B: 08              EX      AF,AF'              
1C8C: 04              INC     B                   
1C8D: 00              NOP                         
1C8E: 01 00 00        LD      BC,$0000            
1C91: 06 00           LD      B,$00               
1C93: 01 00 02        LD      BC,$0200            
1C96: 00              NOP                         
1C97: 01 03 04        LD      BC,$0403            
1C9A: 01 03 01        LD      BC,$0103            
1C9D: 02              LD      (BC),A              
1C9E: 03              INC     BC                  
1C9F: 04              INC     B                   
1CA0: 00              NOP                         
1CA1: 05              DEC     B                   
1CA2: 00              NOP                         
1CA3: 01 02 00        LD      BC,$0002            
1CA6: 09              ADD     HL,BC               
1CA7: 00              NOP                         
1CA8: 03              INC     BC                  
1CA9: 04              INC     B                   
1CAA: 00              NOP                         
1CAB: 01 00 01        LD      BC,$0100            
1CAE: 02              LD      (BC),A              
1CAF: 03              INC     BC                  
1CB0: 04              INC     B                   
1CB1: 00              NOP                         
1CB2: 02              LD      (BC),A              
1CB3: 00              NOP                         
1CB4: 00              NOP                         
1CB5: 01 02 00        LD      BC,$0002            
1CB8: 03              INC     BC                  
1CB9: 04              INC     B                   
1CBA: 00              NOP                         
1CBB: 06 00           LD      B,$00               
1CBD: 00              NOP                         
1CBE: 01 00 00        LD      BC,$0000            
1CC1: 01 02 00        LD      BC,$0002            
1CC4: 05              DEC     B                   
1CC5: 00              NOP                         
1CC6: 00              NOP                         
1CC7: 03              INC     BC                  
1CC8: 00              NOP                         
1CC9: 04              INC     B                   
1CCA: 00              NOP                         
1CCB: 07              RLCA                        
1CCC: 00              NOP                         
1CCD: 01 00 02        LD      BC,$0200            
1CD0: 00              NOP                         
1CD1: 00              NOP                         
1CD2: 03              INC     BC                  
1CD3: 00              NOP                         
1CD4: 04              INC     B                   
1CD5: 00              NOP                         
1CD6: 04              INC     B                   
1CD7: 00              NOP                         
1CD8: 0A              LD      A,(BC)              
1CD9: 00              NOP                         
1CDA: 01 00 02        LD      BC,$0200            
1CDD: 00              NOP                         
1CDE: 03              INC     BC                  
1CDF: 00              NOP                         
1CE0: 01 00 07        LD      BC,$0700            
1CE3: 00              NOP                         
1CE4: 02              LD      (BC),A              
1CE5: 00              NOP                         
1CE6: 03              INC     BC                  
1CE7: 04              INC     B                   
1CE8: 00              NOP                         
1CE9: 05              DEC     B                   
1CEA: 00              NOP                         
1CEB: 01 00 02        LD      BC,$0200            
1CEE: 00              NOP                         
1CEF: 00              NOP                         
1CF0: 08              EX      AF,AF'              
1CF1: 03              INC     BC                  
1CF2: 04              INC     B                   
1CF3: 00              NOP                         
1CF4: 01 00 02        LD      BC,$0200            
1CF7: 00              NOP                         
1CF8: 03              INC     BC                  
1CF9: 00              NOP                         
1CFA: 04              INC     B                   
1CFB: 00              NOP                         
1CFC: 00              NOP                         
1CFD: 06 00           LD      B,$00               
1CFF: 03              INC     BC                  
1D00: 0C              INC     C                   
1D01: 0D              DEC     C                   
1D02: 0C              INC     C                   
1D03: 0F              RRCA                        
1D04: 07              RLCA                        
1D05: 07              RLCA                        
1D06: 01 00 00        LD      BC,$0000            
1D09: 4C              LD      C,H                 
1D0A: 4D              LD      C,L                 
1D0B: 4E              LD      C,(HL)              
1D0C: 4F              LD      C,A                 
1D0D: 4F              LD      C,A                 
1D0E: 4E              LD      C,(HL)              
1D0F: 4D              LD      C,L                 
1D10: 4C              LD      C,H                 
1D11: 00              NOP                         
1D12: 00              NOP                         
1D13: 1F              RRA                         
1D14: 0E 06           LD      C,$06               
1D16: 0D              DEC     C                   
1D17: 01 0E 05        LD      BC,$050E            
1D1A: 08              EX      AF,AF'              
1D1B: 0C              INC     C                   
1D1C: 0E 0C           LD      C,$0C               
1D1E: 0A              LD      A,(BC)              
1D1F: 00              NOP                         
1D20: 00              NOP                         
1D21: 4D              LD      C,L                 
1D22: 4F              LD      C,A                 
1D23: 5E              LD      E,(HL)              
1D24: 5E              LD      E,(HL)              
1D25: 5E              LD      E,(HL)              
1D26: 5E              LD      E,(HL)              
1D27: 5E              LD      E,(HL)              
1D28: 5E              LD      E,(HL)              
1D29: 5E              LD      E,(HL)              
1D2A: 5E              LD      E,(HL)              
1D2B: 4F              LD      C,A                 
1D2C: 4D              LD      C,L                 
1D2D: 00              NOP                         
1D2E: 00              NOP                         
1D2F: 06 0B           LD      B,$0B               
1D31: 0D              DEC     C                   
1D32: 08              EX      AF,AF'              
1D33: 0E 03           LD      C,$03               
1D35: 02              LD      (BC),A              
1D36: 00              NOP                         
1D37: 01 00 4C        LD      BC,$4C00            
1D3A: 4F              LD      C,A                 
1D3B: 5E              LD      E,(HL)              
1D3C: 5E              LD      E,(HL)              
1D3D: 5E              LD      E,(HL)              
1D3E: 5E              LD      E,(HL)              
1D3F: 5E              LD      E,(HL)              
1D40: 5E              LD      E,(HL)              
1D41: 5E              LD      E,(HL)              
1D42: 5E              LD      E,(HL)              
1D43: 5E              LD      E,(HL)              
1D44: 5E              LD      E,(HL)              
1D45: 5E              LD      E,(HL)              
1D46: 5E              LD      E,(HL)              
1D47: 4F              LD      C,A                 
1D48: 4C              LD      C,H                 
1D49: 00              NOP                         
1D4A: 09              ADD     HL,BC               
1D4B: 07              RLCA                        
1D4C: 0A              LD      A,(BC)              
1D4D: 03              INC     BC                  
1D4E: 04              INC     B                   
1D4F: 00              NOP                         
1D50: 0A              LD      A,(BC)              
1D51: 00              NOP                         
1D52: 4D              LD      C,L                 
1D53: 5E              LD      E,(HL)              
1D54: 5E              LD      E,(HL)              
1D55: 5E              LD      E,(HL)              
1D56: 5E              LD      E,(HL)              
1D57: 5E              LD      E,(HL)              
1D58: 5E              LD      E,(HL)              
1D59: 5E              LD      E,(HL)              
1D5A: 5E              LD      E,(HL)              
1D5B: 5E              LD      E,(HL)              
1D5C: 5E              LD      E,(HL)              
1D5D: 5E              LD      E,(HL)              
1D5E: 5E              LD      E,(HL)              
1D5F: 5E              LD      E,(HL)              
1D60: 5E              LD      E,(HL)              
1D61: 5E              LD      E,(HL)              
1D62: 5E              LD      E,(HL)              
1D63: 4D              LD      C,L                 
1D64: 00              NOP                         
1D65: 00              NOP                         
1D66: 0E 0F           LD      C,$0F               
1D68: 08              EX      AF,AF'              
1D69: 08              EX      AF,AF'              
1D6A: 00              NOP                         
1D6B: 5C              LD      E,H                 
1D6C: 60              LD      H,B                 
1D6D: 6A              LD      L,D                 
1D6E: 60              LD      H,B                 
1D6F: 6A              LD      L,D                 
1D70: 60              LD      H,B                 
1D71: 6A              LD      L,D                 
1D72: 60              LD      H,B                 
1D73: 6A              LD      L,D                 
1D74: 60              LD      H,B                 
1D75: 6A              LD      L,D                 
1D76: 60              LD      H,B                 
1D77: 6A              LD      L,D                 
1D78: 60              LD      H,B                 
1D79: 6A              LD      L,D                 
1D7A: 60              LD      H,B                 
1D7B: 6A              LD      L,D                 
1D7C: 60              LD      H,B                 
1D7D: 6A              LD      L,D                 
1D7E: 5D              LD      E,L                 
1D7F: 00              NOP                         
1D80: 01 02 02        LD      BC,$0202            
1D83: 06 01           LD      B,$01               
1D85: 00              NOP                         
1D86: 00              NOP                         
1D87: 00              NOP                         
1D88: 58              LD      E,B                 
1D89: 59              LD      E,C                 
1D8A: 5A              LD      E,D                 
1D8B: 5B              LD      E,E                 
1D8C: 5B              LD      E,E                 
1D8D: 5B              LD      E,E                 
1D8E: 7E              LD      A,(HL)              
1D8F: 7F              LD      A,A                 
1D90: 5B              LD      E,E                 
1D91: 5B              LD      E,E                 
1D92: 5B              LD      E,E                 
1D93: 4A              LD      C,D                 
1D94: 49              LD      C,C                 
1D95: 48              LD      C,B                 
1D96: 00              NOP                         
1D97: 00              NOP                         
1D98: 00              NOP                         
1D99: 03              INC     BC                  
1D9A: 0E 0B           LD      C,$0B               
1D9C: 0D              DEC     C                   
1D9D: 05              DEC     B                   
1D9E: 04              INC     B                   
1D9F: 05              DEC     B                   
1DA0: 0A              LD      A,(BC)              
1DA1: 08              EX      AF,AF'              
1DA2: 00              NOP                         
1DA3: 00              NOP                         
1DA4: 58              LD      E,B                 
1DA5: 59              LD      E,C                 
1DA6: 5A              LD      E,D                 
1DA7: 4B              LD      C,E                 
1DA8: 76              HALT                        
1DA9: 77              LD      (HL),A              
1DAA: 4B              LD      C,E                 
1DAB: 4A              LD      C,D                 
1DAC: 49              LD      C,C                 
1DAD: 48              LD      C,B                 
1DAE: 00              NOP                         
1DAF: 00              NOP                         
1DB0: 01 03 0F        LD      BC,$0F03            
1DB3: 02              LD      (BC),A              
1DB4: 03              INC     BC                  
1DB5: 00              NOP                         
1DB6: 00              NOP                         
1DB7: 03              INC     BC                  
1DB8: 03              INC     BC                  
1DB9: 07              RLCA                        
1DBA: 02              LD      (BC),A              
1DBB: 0A              LD      A,(BC)              
1DBC: 03              INC     BC                  
1DBD: 07              RLCA                        
1DBE: 00              NOP                         
1DBF: 00              NOP                         
1DC0: 58              LD      E,B                 
1DC1: 50              LD      D,B                 
1DC2: 51              LD      D,C                 
1DC3: 52              LD      D,D                 
1DC4: 53              LD      D,E                 
1DC5: 48              LD      C,B                 
1DC6: 00              NOP                         
1DC7: 00              NOP                         
1DC8: 0B              DEC     BC                  
1DC9: 01 02 03        LD      BC,$0302            
1DCC: 0F              RRCA                        
1DCD: 0E 0C           LD      C,$0C               
1DCF: 02              LD      (BC),A              
1DD0: 05              DEC     B                   
1DD1: 0C              INC     C                   
1DD2: 06 00           LD      B,$00               
1DD4: 04              INC     B                   
1DD5: 06 07           LD      B,$07               
1DD7: 0E 0F           LD      C,$0F               
1DD9: 09              ADD     HL,BC               
1DDA: 00              NOP                         
1DDB: 40              LD      B,B                 
1DDC: 41              LD      B,C                 
1DDD: 42              LD      B,D                 
1DDE: 43              LD      B,E                 
1DDF: 00              NOP                         
1DE0: 07              RLCA                        
1DE1: 03              INC     BC                  
1DE2: 0A              LD      A,(BC)              
1DE3: 08              EX      AF,AF'              
1DE4: 0D              DEC     C                   
1DE5: 00              NOP                         
1DE6: 09              ADD     HL,BC               
1DE7: 0B              DEC     BC                  
1DE8: 0C              INC     C                   
1DE9: 0A              LD      A,(BC)              
1DEA: FF              RST     0X38                
1DEB: FF              RST     0X38                
1DEC: FF              RST     0X38                
1DED: FF              RST     0X38                
1DEE: FF              RST     0X38                
1DEF: FF              RST     0X38                
1DF0: 3A 1D 43        LD      A,($431D)           
1DF3: D6 01           SUB     $01                 
1DF5: C8              RET     Z                   
1DF6: 32 8F 43        LD      ($438F),A           ; {ram.CoinCount}
1DF9: 00              NOP                         
1DFA: 00              NOP                         
1DFB: 00              NOP                         
1DFC: 00              NOP                         
1DFD: 00              NOP                         
1DFE: 00              NOP                         
1DFF: 00              NOP                         
1E00: 20 30           JR      NZ,$1E32            ; {}
1E02: 21 31 22        LD      HL,$2231            
1E05: 32 23 33        LD      ($3323),A           ; {}
1E08: 24              INC     H                   
1E09: 34              INC     (HL)                
1E0A: 25              DEC     H                   
1E0B: 35              DEC     (HL)                
1E0C: 26 36           LD      H,$36               
1E0E: 27              DAA                         
1E0F: 37              SCF                         
1E10: 28 38           JR      Z,$1E4A             ; {}
1E12: 29              ADD     HL,HL               
1E13: 39              ADD     HL,SP               
1E14: 2A 3A 2B        LD      HL,($2B3A)          ; {}
1E17: 3B              DEC     SP                  
1E18: 2C              INC     L                   
1E19: 3C              INC     A                   
1E1A: 2D              DEC     L                   
1E1B: 3D              DEC     A                   
1E1C: 2E 3E           LD      L,$3E               
1E1E: 2F              CPL                         
1E1F: 3F              CCF                         
1E20: 49              LD      C,C                 
1E21: 48              LD      C,B                 
1E22: 4A              LD      C,D                 
1E23: 4B              LD      C,E                 
1E24: 4A              LD      C,D                 
1E25: 49              LD      C,C                 
1E26: 4A              LD      C,D                 
1E27: 49              LD      C,C                 
1E28: 48              LD      C,B                 
1E29: 4A              LD      C,D                 
1E2A: 48              LD      C,B                 
1E2B: 49              LD      C,C                 
1E2C: 4B              LD      C,E                 
1E2D: 48              LD      C,B                 
1E2E: 4A              LD      C,D                 
1E2F: 48              LD      C,B                 
1E30: 4A              LD      C,D                 
1E31: 49              LD      C,C                 
1E32: 4B              LD      C,E                 
1E33: 49              LD      C,C                 
1E34: 4B              LD      C,E                 
1E35: 4A              LD      C,D                 
1E36: 49              LD      C,C                 
1E37: 48              LD      C,B                 
1E38: 49              LD      C,C                 
1E39: 49              LD      C,C                 
1E3A: 4A              LD      C,D                 
1E3B: 4A              LD      C,D                 
1E3C: 48              LD      C,B                 
1E3D: 49              LD      C,C                 
1E3E: 4A              LD      C,D                 
1E3F: 48              LD      C,B                 
1E40: A0              AND     B                   
1E41: 60              LD      H,B                 
1E42: 40              LD      B,B                 
1E43: 00              NOP                         
1E44: E0              RET     PO                  
1E45: C0              RET     NZ                  
1E46: C0              RET     NZ                  
1E47: 60              LD      H,B                 
1E48: 80              ADD     A,B                 
1E49: 20 60           JR      NZ,$1EAB            ; {}
1E4B: 40              LD      B,B                 
1E4C: 20 40           JR      NZ,$1E8E            ; {}
1E4E: 00              NOP                         
1E4F: 80              ADD     A,B                 
1E50: 40              LD      B,B                 
1E51: 00              NOP                         
1E52: 20 E0           JR      NZ,$1E34            ; {}
1E54: 00              NOP                         
1E55: 60              LD      H,B                 
1E56: 00              NOP                         
1E57: A0              AND     B                   
1E58: E0              RET     PO                  
1E59: 20 80           JR      NZ,$1DDB            ; {}
1E5B: 00              NOP                         
1E5C: C0              RET     NZ                  
1E5D: 80              ADD     A,B                 
1E5E: A0              AND     B                   
1E5F: E0              RET     PO                  
1E60: 00              NOP                         
1E61: 04              INC     B                   
1E62: 08              EX      AF,AF'              
1E63: 0C              INC     C                   
1E64: 10 14           DJNZ    $1E7A               ; {}
1E66: 18 1C           JR      $1E84               ; {}
1E68: 00              NOP                         
1E69: 08              EX      AF,AF'              
1E6A: 10 18           DJNZ    $1E84               ; {}
1E6C: 04              INC     B                   
1E6D: 0C              INC     C                   
1E6E: 14              INC     D                   
1E6F: 1C              INC     E                   
1E70: 00              NOP                         
1E71: 0C              INC     C                   
1E72: 18 04           JR      $1E78               ; {}
1E74: 04              INC     B                   
1E75: 1C              INC     E                   
1E76: 08              EX      AF,AF'              
1E77: 14              INC     D                   
1E78: 00              NOP                         
1E79: 10 04           DJNZ    $1E7F               ; {}
1E7B: 14              INC     D                   
1E7C: 08              EX      AF,AF'              
1E7D: 18 0C           JR      $1E8B               ; {}
1E7F: 1C              INC     E                   
1E80: 10 11           DJNZ    $1E93               ; {}
1E82: 12              LD      (DE),A              
1E83: 13              INC     DE                  
1E84: 14              INC     D                   
1E85: 15              DEC     D                   
1E86: 16 17           LD      D,$17               
1E88: 18 19           JR      $1EA3               ; {}
1E8A: 1A              LD      A,(DE)              
1E8B: 1B              DEC     DE                  
1E8C: 1C              INC     E                   
1E8D: 1D              DEC     E                   
1E8E: 1E 1F           LD      E,$1F               
1E90: 10 12           DJNZ    $1EA4               ; {}
1E92: 14              INC     D                   
1E93: 16 18           LD      D,$18               
1E95: 1A              LD      A,(DE)              
1E96: 1C              INC     E                   
1E97: 1E 11           LD      E,$11               
1E99: 13              INC     DE                  
1E9A: 15              DEC     D                   
1E9B: 17              RLA                         
1E9C: 19              ADD     HL,DE               
1E9D: 1B              DEC     DE                  
1E9E: 1D              DEC     E                   
1E9F: 1F              RRA                         
1EA0: 4A              LD      C,D                 
1EA1: 4B              LD      C,E                 
1EA2: 49              LD      C,C                 
1EA3: 4A              LD      C,D                 
1EA4: 48              LD      C,B                 
1EA5: 4A              LD      C,D                 
1EA6: 48              LD      C,B                 
1EA7: 49              LD      C,C                 
1EA8: 49              LD      C,C                 
1EA9: 4A              LD      C,D                 
1EAA: 49              LD      C,C                 
1EAB: 4B              LD      C,E                 
1EAC: 48              LD      C,B                 
1EAD: 4B              LD      C,E                 
1EAE: 4A              LD      C,D                 
1EAF: 4A              LD      C,D                 
1EB0: 48              LD      C,B                 
1EB1: 49              LD      C,C                 
1EB2: 48              LD      C,B                 
1EB3: 4A              LD      C,D                 
1EB4: 48              LD      C,B                 
1EB5: 48              LD      C,B                 
1EB6: 49              LD      C,C                 
1EB7: 4A              LD      C,D                 
1EB8: 49              LD      C,C                 
1EB9: 49              LD      C,C                 
1EBA: 4A              LD      C,D                 
1EBB: 48              LD      C,B                 
1EBC: 4A              LD      C,D                 
1EBD: 49              LD      C,C                 
1EBE: 4B              LD      C,E                 
1EBF: 48              LD      C,B                 
1EC0: 00              NOP                         
1EC1: 20 60           JR      NZ,$1F23            ; {}
1EC3: 40              LD      B,B                 
1EC4: E0              RET     PO                  
1EC5: 80              ADD     A,B                 
1EC6: 20 60           JR      NZ,$1F28            ; {}
1EC8: 40              LD      B,B                 
1EC9: A0              AND     B                   
1ECA: 00              NOP                         
1ECB: 00              NOP                         
1ECC: 40              LD      B,B                 
1ECD: 20 C0           JR      NZ,$1E8F            ; {}
1ECF: 20 A0           JR      NZ,$1E71            ; {}
1ED1: 80              ADD     A,B                 
1ED2: E0              RET     PO                  
1ED3: 40              LD      B,B                 
1ED4: 60              LD      H,B                 
1ED5: C0              RET     NZ                  
1ED6: 20 A0           JR      NZ,$1E78            ; {}
1ED8: E0              RET     PO                  
1ED9: 40              LD      B,B                 
1EDA: 60              LD      H,B                 
1EDB: C0              RET     NZ                  
1EDC: 20 40           JR      NZ,$1F1E            ; {}
1EDE: 20 80           JR      NZ,$1E60            ; {}
1EE0: 11 3D 43        LD      DE,$433D            
1EE3: 01 1A 00        LD      BC,$001A            
1EE6: 1A              LD      A,(DE)              
1EE7: 80              ADD     A,B                 
1EE8: 47              LD      B,A                 
1EE9: CD 17 02        CALL    $0217               ; {code.SubtractOneRow}
1EEC: 0D              DEC     C                   
1EED: C2 E6 1E        JP      NZ,$1EE6            ; {}
1EF0: 1A              LD      A,(DE)              
1EF1: 80              ADD     A,B                 
1EF2: C6 27           ADD     $27                 
1EF4: 21 89 43        LD      HL,$4389            
1EF7: 86              ADD     A,(HL)              
1EF8: 77              LD      (HL),A              
1EF9: 00              NOP                         
1EFA: C9              RET                         
1EFB: FF              RST     0X38                
1EFC: FF              RST     0X38                
1EFD: FF              RST     0X38                
1EFE: FF              RST     0X38                
1EFF: FF              RST     0X38                
1F00: 00              NOP                         
1F01: 00              NOP                         
1F02: 00              NOP                         
1F03: 01 00 00        LD      BC,$0000            
1F06: 00              NOP                         
1F07: 02              LD      (BC),A              
1F08: 00              NOP                         
1F09: 00              NOP                         
1F0A: 00              NOP                         
1F0B: 00              NOP                         
1F0C: 03              INC     BC                  
1F0D: 00              NOP                         
1F0E: 00              NOP                         
1F0F: 00              NOP                         
1F10: 00              NOP                         
1F11: 04              INC     B                   
1F12: 00              NOP                         
1F13: 00              NOP                         
1F14: 00              NOP                         
1F15: 00              NOP                         
1F16: 01 00 00        LD      BC,$0000            
1F19: 00              NOP                         
1F1A: 05              DEC     B                   
1F1B: 00              NOP                         
1F1C: 02              LD      (BC),A              
1F1D: 00              NOP                         
1F1E: 03              INC     BC                  
1F1F: 00              NOP                         
1F20: 00              NOP                         
1F21: 00              NOP                         
1F22: 04              INC     B                   
1F23: 00              NOP                         
1F24: 07              RLCA                        
1F25: 00              NOP                         
1F26: 00              NOP                         
1F27: 00              NOP                         
1F28: 06 00           LD      B,$00               
1F2A: 01 00 02        LD      BC,$0200            
1F2D: 0C              INC     C                   
1F2E: 00              NOP                         
1F2F: 03              INC     BC                  
1F30: 04              INC     B                   
1F31: 00              NOP                         
1F32: 00              NOP                         
1F33: 01 00 08        LD      BC,$0800            
1F36: 00              NOP                         
1F37: 00              NOP                         
1F38: 02              LD      (BC),A              
1F39: 00              NOP                         
1F3A: 0C              INC     C                   
1F3B: 03              INC     BC                  
1F3C: 04              INC     B                   
1F3D: 0E 00           LD      C,$00               
1F3F: 00              NOP                         
1F40: 00              NOP                         
1F41: 01 02 00        LD      BC,$0002            
1F44: 0D              DEC     C                   
1F45: 03              INC     BC                  
1F46: 04              INC     B                   
1F47: 0F              RRCA                        
1F48: 01 0C 07        LD      BC,$070C            
1F4B: 0A              LD      A,(BC)              
1F4C: 02              LD      (BC),A              
1F4D: 0D              DEC     C                   
1F4E: 03              INC     BC                  
1F4F: 08              EX      AF,AF'              
1F50: 06 0C           LD      B,$0C               
1F52: 04              INC     B                   
1F53: 09              ADD     HL,BC               
1F54: 05              DEC     B                   
1F55: 0F              RRCA                        
1F56: 01 02 0D        LD      BC,$0D02            
1F59: 03              INC     BC                  
1F5A: 0C              INC     C                   
1F5B: 04              INC     B                   
1F5C: 0D              DEC     C                   
1F5D: 05              DEC     B                   
1F5E: 0F              RRCA                        
1F5F: 0C              INC     C                   
1F60: 01 02 0E        LD      BC,$0E02            
1F63: 0C              INC     C                   
1F64: 03              INC     BC                  
1F65: 0F              RRCA                        
1F66: 0D              DEC     C                   
1F67: 05              DEC     B                   
1F68: 0E 0D           LD      C,$0D               
1F6A: 0C              INC     C                   
1F6B: 0F              RRCA                        
1F6C: 0D              DEC     C                   
1F6D: 04              INC     B                   
1F6E: 0C              INC     C                   
1F6F: 01 0E 05        LD      BC,$050E            
1F72: 0F              RRCA                        
1F73: 0D              DEC     C                   
1F74: 07              RLCA                        
1F75: 0C              INC     C                   
1F76: 06 0E           LD      B,$0E               
1F78: 0D              DEC     C                   
1F79: 0F              RRCA                        
1F7A: 09              ADD     HL,BC               
1F7B: 0C              INC     C                   
1F7C: 0F              RRCA                        
1F7D: 0D              DEC     C                   
1F7E: 0E 0D           LD      C,$0D               
1F80: 02              LD      (BC),A              
1F81: 0D              DEC     C                   
1F82: 0C              INC     C                   
1F83: 0F              RRCA                        
1F84: 05              DEC     B                   
1F85: 0E 0D           LD      C,$0D               
1F87: 0C              INC     C                   
1F88: 0F              RRCA                        
1F89: 06 0E           LD      B,$0E               
1F8B: 0F              RRCA                        
1F8C: 0C              INC     C                   
1F8D: 0D              DEC     C                   
1F8E: 0F              RRCA                        
1F8F: 0C              INC     C                   
1F90: 06 0D           LD      B,$0D               
1F92: 04              INC     B                   
1F93: 0B              DEC     BC                  
1F94: 0C              INC     C                   
1F95: 0F              RRCA                        
1F96: 05              DEC     B                   
1F97: 0D              DEC     C                   
1F98: 05              DEC     B                   
1F99: 03              INC     BC                  
1F9A: 0E 07           LD      C,$07               
1F9C: 0C              INC     C                   
1F9D: 0D              DEC     C                   
1F9E: 04              INC     B                   
1F9F: 05              DEC     B                   
1FA0: 01 02 0E        LD      BC,$0E02            
1FA3: 03              INC     BC                  
1FA4: 0C              INC     C                   
1FA5: 04              INC     B                   
1FA6: 0F              RRCA                        
1FA7: 05              DEC     B                   
1FA8: 08              EX      AF,AF'              
1FA9: 0C              INC     C                   
1FAA: 07              RLCA                        
1FAB: 01 0D 04        LD      BC,$040D            
1FAE: 0E 02           LD      C,$02               
1FB0: 0C              INC     C                   
1FB1: 01 0F 03        LD      BC,$030F            
1FB4: 05              DEC     B                   
1FB5: 0D              DEC     C                   
1FB6: 00              NOP                         
1FB7: 0E 00           LD      C,$00               
1FB9: 09              ADD     HL,BC               
1FBA: 0C              INC     C                   
1FBB: 06 0D           LD      B,$0D               
1FBD: 00              NOP                         
1FBE: 01 02 01        LD      BC,$0102            
1FC1: 02              LD      (BC),A              
1FC2: 03              INC     BC                  
1FC3: 00              NOP                         
1FC4: 00              NOP                         
1FC5: 0D              DEC     C                   
1FC6: 00              NOP                         
1FC7: 0A              LD      A,(BC)              
1FC8: 00              NOP                         
1FC9: 00              NOP                         
1FCA: 00              NOP                         
1FCB: 0E 00           LD      C,$00               
1FCD: 05              DEC     B                   
1FCE: 00              NOP                         
1FCF: 08              EX      AF,AF'              
1FD0: 00              NOP                         
1FD1: 0C              INC     C                   
1FD2: 00              NOP                         
1FD3: 00              NOP                         
1FD4: 03              INC     BC                  
1FD5: 00              NOP                         
1FD6: 00              NOP                         
1FD7: 07              RLCA                        
1FD8: 00              NOP                         
1FD9: 00              NOP                         
1FDA: 00              NOP                         
1FDB: 04              INC     B                   
1FDC: 00              NOP                         
1FDD: 00              NOP                         
1FDE: 06 00           LD      B,$00               
1FE0: 00              NOP                         
1FE1: 00              NOP                         
1FE2: 00              NOP                         
1FE3: 01 00 00        LD      BC,$0000            
1FE6: 00              NOP                         
1FE7: 00              NOP                         
1FE8: 02              LD      (BC),A              
1FE9: 00              NOP                         
1FEA: 00              NOP                         
1FEB: 00              NOP                         
1FEC: 00              NOP                         
1FED: 03              INC     BC                  
1FEE: 00              NOP                         
1FEF: 00              NOP                         
1FF0: 00              NOP                         
1FF1: 04              INC     B                   
1FF2: 00              NOP                         
1FF3: 05              DEC     B                   
1FF4: 00              NOP                         
1FF5: 00              NOP                         
1FF6: 00              NOP                         
1FF7: 00              NOP                         
1FF8: 00              NOP                         
1FF9: 01 00 00        LD      BC,$0000            
1FFC: 00              NOP                         
1FFD: 00              NOP                         
1FFE: 02              LD      (BC),A              
1FFF: 00              NOP                         
2000: CD 76 08        CALL    $0876               ; {}
2003: CD F0 0D        CALL    $0DF0               ; {}
2006: CD A0 24        CALL    $24A0               ; {}
2009: 21 5F 43        LD      HL,$435F            
200C: 7E              LD      A,(HL)              
200D: E6 03           AND     $03                 
200F: 47              LD      B,A                 
2010: 34              INC     (HL)                
2011: 3A BA 43        LD      A,($43BA)           
2014: A7              AND     A                   
2015: CA BA 21        JP      Z,$21BA             ; {}
2018: FE 05           CP      $05                 
201A: D2 30 21        JP      NC,$2130            ; {}
201D: 2D              DEC     L                   
201E: 78              LD      A,B                 
201F: A7              AND     A                   
2020: C2 25 20        JP      NZ,$2025            ; {}
2023: 36 FF           LD      (HL),$FF            
2025: 7E              LD      A,(HL)              
2026: A7              AND     A                   
2027: CA 30 21        JP      Z,$2130             ; {}
202A: C3 46 21        JP      $2146               ; {}
202D: FF              RST     0X38                
202E: FF              RST     0X38                
202F: FF              RST     0X38                
2030: E6 03           AND     $03                 
2032: FE 01           CP      $01                 
2034: 11 50 1B        LD      DE,$1B50            
2037: C3 AC 23        JP      $23AC               ; {}
203A: FF              RST     0X38                
203B: FF              RST     0X38                
203C: FF              RST     0X38                
203D: FF              RST     0X38                
203E: FF              RST     0X38                
203F: FF              RST     0X38                
2040: 21 AF 43        LD      HL,$43AF            
2043: 3A B9 43        LD      A,($43B9)           
2046: 4F              LD      C,A                 
2047: BE              CP      (HL)                
2048: C0              RET     NZ                  
2049: 7E              LD      A,(HL)              
204A: 2C              INC     L                   
204B: 96              SUB     (HL)                
204C: 2D              DEC     L                   
204D: 77              LD      (HL),A              
204E: 2C              INC     L                   
204F: 2C              INC     L                   
2050: 34              INC     (HL)                
2051: 7E              LD      A,(HL)              
2052: 21 80 1E        LD      HL,$1E80            
2055: E6 1F           AND     $1F                 
2057: 85              ADD     A,L                 
2058: 6F              LD      L,A                 
2059: 46              LD      B,(HL)              
205A: C6 20           ADD     $20                 
205C: 6F              LD      L,A                 
205D: 56              LD      D,(HL)              
205E: C6 20           ADD     $20                 
2060: 6F              LD      L,A                 
2061: 5E              LD      E,(HL)              
2062: 79              LD      A,C                 
2063: 0F              RRCA                        
2064: 0F              RRCA                        
2065: 0F              RRCA                        
2066: E6 1F           AND     $1F                 
2068: 83              ADD     A,E                 
2069: 3C              INC     A                   
206A: 5F              LD      E,A                 
206B: 78              LD      A,B                 
206C: 12              LD      (DE),A              
206D: C9              RET                         
206E: C9              RET                         
206F: FF              RST     0X38                
2070: 7B              LD      A,E                 
2071: D6 0A           SUB     $0A                 
2073: C6 C0           ADD     $C0                 
2075: 4F              LD      C,A                 
2076: 7A              LD      A,D                 
2077: CE 00           ADC     $00                 
2079: 47              LD      B,A                 
207A: 7E              LD      A,(HL)              
207B: 11 00 28        LD      DE,$2800            
207E: 21 00 29        LD      HL,$2900            
2081: C3 85 20        JP      $2085               ; {}
2084: FF              RST     0X38                
2085: D6 20           SUB     $20                 
2087: 07              RLCA                        
2088: 07              RLCA                        
2089: 00              NOP                         
208A: E6 E0           AND     $E0                 
208C: 6F              LD      L,A                 
208D: 3E E0           LD      A,$E0               
208F: 95              SUB     L                   
2090: 6F              LD      L,A                 
2091: 3E 3F           LD      A,$3F               
2093: 91              SUB     C                   
2094: 3E 43           LD      A,$43               
2096: 98              SBC     B                   
2097: D2 B0 20        JP      NC,$20B0            ; {}
209A: 23              INC     HL                  
209B: 23              INC     HL                  
209C: 7B              LD      A,E                 
209D: C6 10           ADD     $10                 
209F: 5F              LD      E,A                 
20A0: 79              LD      A,C                 
20A1: D6 20           SUB     $20                 
20A3: 4F              LD      C,A                 
20A4: 78              LD      A,B                 
20A5: DE 00           SBC     $00                 
20A7: 47              LD      B,A                 
20A8: C3 91 20        JP      $2091               ; {}
20AB: FF              RST     0X38                
20AC: FF              RST     0X38                
20AD: FF              RST     0X38                
20AE: FF              RST     0X38                
20AF: FF              RST     0X38                
20B0: C5              PUSH    BC                  
20B1: 7E              LD      A,(HL)              
20B2: E3              EX      (SP),HL             
20B3: 06 08           LD      B,$08               
20B5: 36 00           LD      (HL),$00            
20B7: 0F              RRCA                        
20B8: D2 BF 20        JP      NC,$20BF            ; {}
20BB: EB              EX      DE,HL               
20BC: 4E              LD      C,(HL)              
20BD: EB              EX      DE,HL               
20BE: 71              LD      (HL),C              
20BF: 23              INC     HL                  
20C0: 13              INC     DE                  
20C1: 05              DEC     B                   
20C2: C2 B5 20        JP      NZ,$20B5            ; {}
20C5: E3              EX      (SP),HL             
20C6: 23              INC     HL                  
20C7: 7D              LD      A,L                 
20C8: 0F              RRCA                        
20C9: DA B1 20        JP      C,$20B1             ; {}
20CC: 7D              LD      A,L                 
20CD: E6 1F           AND     $1F                 
20CF: CA E1 20        JP      Z,$20E1             ; {}
20D2: E3              EX      (SP),HL             
20D3: 7D              LD      A,L                 
20D4: D6 30           SUB     $30                 
20D6: 6F              LD      L,A                 
20D7: 7C              LD      A,H                 
20D8: DE 00           SBC     $00                 
20DA: 67              LD      H,A                 
20DB: E3              EX      (SP),HL             
20DC: FE 3F           CP      $3F                 
20DE: C2 B1 20        JP      NZ,$20B1            ; {}
20E1: C1              POP     BC                  
20E2: C9              RET                         
20E3: 20 FF           JR      NZ,$20E4            ; {}
20E5: FF              RST     0X38                
20E6: FF              RST     0X38                
20E7: FF              RST     0X38                
20E8: 47              LD      B,A                 
20E9: 7A              LD      A,D                 
20EA: C6 08           ADD     $08                 
20EC: 57              LD      D,A                 
20ED: CD 1C 21        CALL    $211C               ; {}
20F0: 0F              RRCA                        
20F1: 0F              RRCA                        
20F2: 0F              RRCA                        
20F3: 83              ADD     A,E                 
20F4: E6 1F           AND     $1F                 
20F6: 4F              LD      C,A                 
20F7: 7B              LD      A,E                 
20F8: E6 E0           AND     $E0                 
20FA: B1              OR      C                   
20FB: 5F              LD      E,A                 
20FC: 78              LD      A,B                 
20FD: 0F              RRCA                        
20FE: 0F              RRCA                        
20FF: E6 0E           AND     $0E                 
2101: C6 90           ADD     $90                 
2103: 6F              LD      L,A                 
2104: 26 1B           LD      H,$1B               
2106: 7E              LD      A,(HL)              
2107: 2C              INC     L                   
2108: 6E              LD      L,(HL)              
2109: 67              LD      H,A                 
210A: 01 04 04        LD      BC,$0404            
210D: C3 D6 0A        JP      $0AD6               ; {}
2110: FF              RST     0X38                
2111: FF              RST     0X38                
2112: FF              RST     0X38                
2113: FF              RST     0X38                
2114: FF              RST     0X38                
2115: FF              RST     0X38                
2116: FF              RST     0X38                
2117: FF              RST     0X38                
2118: FF              RST     0X38                
2119: FF              RST     0X38                
211A: FF              RST     0X38                
211B: FF              RST     0X38                
211C: 21 B9 43        LD      HL,$43B9            
211F: 7E              LD      A,(HL)              
2120: FE 10           CP      $10                 
2122: D8              RET     C                   
2123: FE 30           CP      $30                 
2125: D0              RET     NC                  
2126: 3E 10           LD      A,$10               
2128: 77              LD      (HL),A              
2129: 32 00 58        LD      ($5800),A           ; 58xx scroll register
212C: C9              RET                         
212D: FF              RST     0X38                
212E: FF              RST     0X38                
212F: FF              RST     0X38                
2130: 78              LD      A,B                 
2131: A7              AND     A                   
2132: CA 50 21        JP      Z,$2150             ; {}
2135: FE 01           CP      $01                 
2137: CA 60 21        JP      Z,$2160             ; {}
213A: FE 02           CP      $02                 
213C: CA 70 21        JP      Z,$2170             ; {}
213F: C3 80 21        JP      $2180               ; {}
2142: 90              SUB     B                   
2143: A5              AND     L                   
2144: 50              LD      D,B                 
2145: 60              LD      H,B                 
2146: 78              LD      A,B                 
2147: 0F              RRCA                        
2148: D2 90 21        JP      NC,$2190            ; {}
214B: C3 A5 21        JP      $21A5               ; {}
214E: F0              RET     P                   
214F: F9              LD      SP,HL               
2150: CD 50 0A        CALL    $0A50               ; {}
2153: CD 00 30        CALL    $3000               ; {}
2156: C3 00 0F        JP      $0F00               ; {}
2159: FF              RST     0X38                
215A: FF              RST     0X38                
215B: FF              RST     0X38                
215C: FF              RST     0X38                
215D: FF              RST     0X38                
215E: FF              RST     0X38                
215F: FF              RST     0X38                
2160: CD C4 24        CALL    $24C4               ; {}
2163: CD 40 0C        CALL    $0C40               ; {}
2166: CD 1C 0D        CALL    $0D1C               ; {}
2169: C3 C0 0F        JP      $0FC0               ; {}
216C: FF              RST     0X38                
216D: FF              RST     0X38                
216E: FF              RST     0X38                
216F: FF              RST     0X38                
2170: CD 70 0D        CALL    $0D70               ; {}
2173: C3 60 25        JP      $2560               ; {}
2176: FF              RST     0X38                
2177: FF              RST     0X38                
2178: FF              RST     0X38                
2179: FF              RST     0X38                
217A: FF              RST     0X38                
217B: FF              RST     0X38                
217C: FF              RST     0X38                
217D: FF              RST     0X38                
217E: FF              RST     0X38                
217F: FF              RST     0X38                
2180: CD C4 24        CALL    $24C4               ; {}
2183: CD 40 0C        CALL    $0C40               ; {}
2186: CD 6C 0A        CALL    $0A6C               ; {}
2189: C3 C0 0F        JP      $0FC0               ; {}
218C: FF              RST     0X38                
218D: FF              RST     0X38                
218E: FF              RST     0X38                
218F: FF              RST     0X38                
2190: CD 50 0A        CALL    $0A50               ; {}
2193: CD 00 30        CALL    $3000               ; {}
2196: CD 00 0F        CALL    $0F00               ; {}
2199: CD 60 25        CALL    $2560               ; {}
219C: C3 40 0C        JP      $0C40               ; {}
219F: FF              RST     0X38                
21A0: FF              RST     0X38                
21A1: FF              RST     0X38                
21A2: FF              RST     0X38                
21A3: FF              RST     0X38                
21A4: FF              RST     0X38                
21A5: CD 1C 0D        CALL    $0D1C               ; {}
21A8: CD 70 0D        CALL    $0D70               ; {}
21AB: CD 6C 0A        CALL    $0A6C               ; {}
21AE: CD C0 0F        CALL    $0FC0               ; {}
21B1: C3 C4 24        JP      $24C4               ; {}
21B4: FF              RST     0X38                
21B5: FF              RST     0X38                
21B6: FF              RST     0X38                
21B7: FF              RST     0X38                
21B8: FF              RST     0X38                
21B9: FF              RST     0X38                
21BA: 78              LD      A,B                 
21BB: 0F              RRCA                        
21BC: D2 04 22        JP      NC,$2204            ; {}
21BF: CD 40 0C        CALL    $0C40               ; {}
21C2: CD C0 0F        CALL    $0FC0               ; {}
21C5: CD C4 24        CALL    $24C4               ; {}
21C8: 3A B8 43        LD      A,($43B8)           
21CB: E6 0F           AND     $0F                 
21CD: FE 0B           CP      $0B                 
21CF: DA 04 22        JP      C,$2204             ; {}
21D2: 3E 10           LD      A,$10               
21D4: 32 BA 43        LD      ($43BA),A           
21D7: C3 26 05        JP      $0526               ; {}
21DA: FF              RST     0X38                
21DB: FF              RST     0X38                
21DC: 7E              LD      A,(HL)              
21DD: 00              NOP                         
21DE: 47              LD      B,A                 
21DF: 21 73 4B        LD      HL,$4B73            
21E2: E6 07           AND     $07                 
21E4: 77              LD      (HL),A              
21E5: 2D              DEC     L                   
21E6: 36 EF           LD      (HL),$EF            
21E8: 2D              DEC     L                   
21E9: 36 49           LD      (HL),$49            
21EB: 2D              DEC     L                   
21EC: 78              LD      A,B                 
21ED: E6 F8           AND     $F8                 
21EF: 0F              RRCA                        
21F0: 0F              RRCA                        
21F1: 0F              RRCA                        
21F2: C6 3A           ADD     $3A                 
21F4: 5F              LD      E,A                 
21F5: 16 23           LD      D,$23               
21F7: 1A              LD      A,(DE)              
21F8: 77              LD      (HL),A              
21F9: CD C0 34        CALL    $34C0               ; {}
21FC: C3 E0 1E        JP      $1EE0               ; {}
21FF: FF              RST     0X38                
2200: FF              RST     0X38                
2201: FF              RST     0X38                
2202: FF              RST     0X38                
2203: FF              RST     0X38                
2204: 21 B6 43        LD      HL,$43B6            
2207: 35              DEC     (HL)                
2208: 7E              LD      A,(HL)              
2209: FE A0           CP      $A0                 
220B: D0              RET     NC                  
220C: 2E A4           LD      L,$A4               
220E: 36 02           LD      (HL),$02            
2210: 2E A6           LD      L,$A6               
2212: 36 00           LD      (HL),$00            
2214: 2E B8           LD      L,$B8               
2216: 34              INC     (HL)                
2217: 7E              LD      A,(HL)              
2218: E6 0E           AND     $0E                 
221A: 0F              RRCA                        
221B: C6 60           ADD     $60                 
221D: 5F              LD      E,A                 
221E: 16 17           LD      D,$17               
2220: 2C              INC     L                   
2221: 2C              INC     L                   
2222: 1A              LD      A,(DE)              
2223: A7              AND     A                   
2224: F2 2A 22        JP      P,$222A             ; {}
2227: 2C              INC     L                   
2228: E6 7F           AND     $7F                 
222A: 77              LD      (HL),A              
222B: C3 80 03        JP      $0380               ; {}
222E: FF              RST     0X38                
222F: FF              RST     0X38                
2230: 21 9C 43        LD      HL,$439C            
2233: 7E              LD      A,(HL)              
2234: 34              INC     (HL)                
2235: 00              NOP                         
2236: 0F              RRCA                        
2237: E6 3F           AND     $3F                 
2239: FE 0D           CP      $0D                 
223B: CA 92 22        JP      Z,$2292             ; {}
223E: 06 1F           LD      B,$1F               
2240: DA 60 22        JP      C,$2260             ; {}
2243: 06 00           LD      B,$00               
2245: D6 0E           SUB     $0E                 
2247: FE 0D           CP      $0D                 
2249: C2 60 22        JP      NZ,$2260            ; {}
224C: 21 B8 43        LD      HL,$43B8            
224F: 34              INC     (HL)                
2250: 2E A4           LD      L,$A4               
2252: 36 02           LD      (HL),$02            
2254: C9              RET                         
2255: 58              LD      E,B                 
2256: 2E A4           LD      L,$A4               
2258: 36 02           LD      (HL),$02            
225A: C9              RET                         
225B: FF              RST     0X38                
225C: FF              RST     0X38                
225D: FF              RST     0X38                
225E: FF              RST     0X38                
225F: FF              RST     0X38                
2260: 4F              LD      C,A                 
2261: 0F              RRCA                        
2262: 0F              RRCA                        
2263: 0F              RRCA                        
2264: 57              LD      D,A                 
2265: E6 1F           AND     $1F                 
2267: 5F              LD      E,A                 
2268: 7A              LD      A,D                 
2269: E6 E0           AND     $E0                 
226B: C6 B0           ADD     $B0                 
226D: 6F              LD      L,A                 
226E: 7B              LD      A,E                 
226F: CE 41           ADC     $41                 
2271: 67              LD      H,A                 
2272: 7D              LD      A,L                 
2273: 91              SUB     C                   
2274: 6F              LD      L,A                 
2275: 79              LD      A,C                 
2276: 3C              INC     A                   
2277: 4F              LD      C,A                 
2278: 07              RLCA                        
2279: 5F              LD      E,A                 
227A: 51              LD      D,C                 
227B: 70              LD      (HL),B              
227C: 23              INC     HL                  
227D: 70              LD      (HL),B              
227E: 23              INC     HL                  
227F: 15              DEC     D                   
2280: C2 7B 22        JP      NZ,$227B            ; {}
2283: 7D              LD      A,L                 
2284: 91              SUB     C                   
2285: 91              SUB     C                   
2286: D6 20           SUB     $20                 
2288: 6F              LD      L,A                 
2289: 7C              LD      A,H                 
228A: DE 00           SBC     $00                 
228C: 67              LD      H,A                 
228D: 1D              DEC     E                   
228E: C2 7A 22        JP      NZ,$227A            ; {}
2291: C9              RET                         
2292: 21 B8 43        LD      HL,$43B8            
2295: 7E              LD      A,(HL)              
2296: E6 08           AND     $08                 
2298: CA F0 22        JP      Z,$22F0             ; {}
229B: 21 00 1C        LD      HL,$1C00            
229E: 11 3F 4B        LD      DE,$4B3F            
22A1: 06 47           LD      B,$47               
22A3: 7E              LD      A,(HL)              
22A4: 12              LD      (DE),A              
22A5: 2C              INC     L                   
22A6: 1B              DEC     DE                  
22A7: 7E              LD      A,(HL)              
22A8: 12              LD      (DE),A              
22A9: 2C              INC     L                   
22AA: 1B              DEC     DE                  
22AB: 78              LD      A,B                 
22AC: BA              CP      D                   
22AD: C2 A3 22        JP      NZ,$22A3            ; {}
22B0: C3 E0 22        JP      $22E0               ; {}
22B3: FF              RST     0X38                
22B4: CD 7A 06        CALL    $067A               ; {}
22B7: 21 B4 43        LD      HL,$43B4            
22BA: 35              DEC     (HL)                
22BB: 7E              LD      A,(HL)              
22BC: FE 28           CP      $28                 
22BE: C2 48 08        JP      NZ,$0848            ; {}
22C1: 2E 67           LD      L,$67               
22C3: 36 FF           LD      (HL),$FF            
22C5: C9              RET                         
22C6: FF              RST     0X38                
22C7: FF              RST     0X38                
22C8: FF              RST     0X38                
22C9: FF              RST     0X38                
22CA: 21 B4 43        LD      HL,$43B4            
22CD: 7E              LD      A,(HL)              
22CE: FE C0           CP      $C0                 
22D0: C2 34 08        JP      NZ,$0834            ; {}
22D3: 36 30           LD      (HL),$30            
22D5: 2E 67           LD      L,$67               
22D7: 36 FF           LD      (HL),$FF            
22D9: 2E BC           LD      L,$BC               
22DB: 36 3F           LD      (HL),$3F            
22DD: C9              RET                         
22DE: FF              RST     0X38                
22DF: FF              RST     0X38                
22E0: 3E 71           LD      A,$71               
22E2: 32 B9 43        LD      ($43B9),A           
22E5: 32 00 58        LD      ($5800),A           ; 58xx scroll register
22E8: C9              RET                         
22E9: FF              RST     0X38                
22EA: FF              RST     0X38                
22EB: FF              RST     0X38                
22EC: FF              RST     0X38                
22ED: FF              RST     0X38                
22EE: FF              RST     0X38                
22EF: FF              RST     0X38                
22F0: CD A0 03        CALL    $03A0               ; {}
22F3: AF              XOR     A                   
22F4: C3 E2 22        JP      $22E2               ; {}
22F7: FF              RST     0X38                
22F8: FF              RST     0X38                
22F9: FF              RST     0X38                
22FA: 21 AA 4A        LD      HL,$4AAA            
22FD: 06 12           LD      B,$12               
22FF: 3A 8A 48        LD      A,($488A)           
2302: 4F              LD      C,A                 
2303: 79              LD      A,C                 
2304: E6 03           AND     $03                 
2306: 07              RLCA                        
2307: 07              RLCA                        
2308: 57              LD      D,A                 
2309: 4E              LD      C,(HL)              
230A: 79              LD      A,C                 
230B: E6 0C           AND     $0C                 
230D: 0F              RRCA                        
230E: 0F              RRCA                        
230F: B2              OR      D                   
2310: F6 60           OR      $60                 
2312: 77              LD      (HL),A              
2313: 7D              LD      A,L                 
2314: D6 20           SUB     $20                 
2316: 6F              LD      L,A                 
2317: D2 1B 23        JP      NC,$231B            ; {}
231A: 25              DEC     H                   
231B: 05              DEC     B                   
231C: C2 03 23        JP      NZ,$2303            ; {}
231F: C9              RET                         
2320: FF              RST     0X38                
2321: FF              RST     0X38                
2322: 21 A7 43        LD      HL,$43A7            
2325: 34              INC     (HL)                
2326: 7E              LD      A,(HL)              
2327: E6 07           AND     $07                 
2329: 07              RLCA                        
232A: 07              RLCA                        
232B: 07              RLCA                        
232C: C6 C0           ADD     $C0                 
232E: 6F              LD      L,A                 
232F: 26 1B           LD      H,$1B               
2331: 11 A6 49        LD      DE,$49A6            
2334: 01 02 04        LD      BC,$0402            
2337: C3 D6 0A        JP      $0AD6               ; {}
233A: 01 02 03        LD      BC,$0302            
233D: 04              INC     B                   
233E: 05              DEC     B                   
233F: 06 07           LD      B,$07               
2341: 0A              LD      A,(BC)              
2342: 07              RLCA                        
2343: 0A              LD      A,(BC)              
2344: 07              RLCA                        
2345: 0A              LD      A,(BC)              
2346: 07              RLCA                        
2347: 0A              LD      A,(BC)              
2348: 07              RLCA                        
2349: 0A              LD      A,(BC)              
234A: 09              ADD     HL,BC               
234B: 08              EX      AF,AF'              
234C: 04              INC     B                   
234D: 03              INC     BC                  
234E: 02              LD      (BC),A              
234F: 01 FF 1A        LD      BC,$1AFF            
2352: E6 08           AND     $08                 
2354: C8              RET     Z                   
2355: 7E              LD      A,(HL)              
2356: 2C              INC     L                   
2357: 6E              LD      L,(HL)              
2358: C6 08           ADD     $08                 
235A: 67              LD      H,A                 
235B: 3A B9 43        LD      A,($43B9)           
235E: 0F              RRCA                        
235F: 0F              RRCA                        
2360: 0F              RRCA                        
2361: 85              ADD     A,L                 
2362: E6 1F           AND     $1F                 
2364: 47              LD      B,A                 
2365: 7D              LD      A,L                 
2366: E6 E0           AND     $E0                 
2368: B0              OR      B                   
2369: 6F              LD      L,A                 
236A: 7E              LD      A,(HL)              
236B: 47              LD      B,A                 
236C: E6 FC           AND     $FC                 
236E: FE 4C           CP      $4C                 
2370: CA 7B 23        JP      Z,$237B             ; {}
2373: E6 F0           AND     $F0                 
2375: FE 60           CP      $60                 
2377: CA 98 23        JP      Z,$2398             ; {}
237A: C9              RET                         
237B: 1A              LD      A,(DE)              
237C: E6 F7           AND     $F7                 
237E: 12              LD      (DE),A              
237F: 3E FF           LD      A,$FF               
2381: 32 66 43        LD      ($4366),A           
2384: 78              LD      A,B                 
2385: 3D              DEC     A                   
2386: 77              LD      (HL),A              
2387: FE 4B           CP      $4B                 
2389: C0              RET     NZ                  
238A: 36 00           LD      (HL),$00            
238C: 2D              DEC     L                   
238D: 7E              LD      A,(HL)              
238E: FE 5E           CP      $5E                 
2390: C0              RET     NZ                  
2391: 36 4F           LD      (HL),$4F            
2393: C9              RET                         
2394: FF              RST     0X38                
2395: FF              RST     0X38                
2396: FF              RST     0X38                
2397: FF              RST     0X38                
2398: 1A              LD      A,(DE)              
2399: E6 F7           AND     $F7                 
239B: 12              LD      (DE),A              
239C: 1C              INC     E                   
239D: 1C              INC     E                   
239E: 1A              LD      A,(DE)              
239F: E6 04           AND     $04                 
23A1: 78              LD      A,B                 
23A2: C2 30 20        JP      NZ,$2030            ; {}
23A5: E6 0C           AND     $0C                 
23A7: FE 04           CP      $04                 
23A9: 11 40 1B        LD      DE,$1B40            
23AC: CA C0 23        JP      Z,$23C0             ; {}
23AF: 78              LD      A,B                 
23B0: E6 0F           AND     $0F                 
23B2: 83              ADD     A,E                 
23B3: 5F              LD      E,A                 
23B4: 1A              LD      A,(DE)              
23B5: 77              LD      (HL),A              
23B6: 3E FF           LD      A,$FF               
23B8: 32 66 43        LD      ($4366),A           
23BB: C9              RET                         
23BC: FF              RST     0X38                
23BD: FF              RST     0X38                
23BE: FF              RST     0X38                
23BF: FF              RST     0X38                
23C0: 2D              DEC     L                   
23C1: 7E              LD      A,(HL)              
23C2: E6 F0           AND     $F0                 
23C4: FE 70           CP      $70                 
23C6: C0              RET     NZ                  
23C7: 21 A4 43        LD      HL,$43A4            
23CA: 36 06           LD      (HL),$06            
23CC: 2C              INC     L                   
23CD: 36 60           LD      (HL),$60            
23CF: 2E 63           LD      L,$63               
23D1: 36 FF           LD      (HL),$FF            
23D3: C9              RET                         
23D4: FF              RST     0X38                
23D5: FF              RST     0X38                
23D6: 21 B8 43        LD      HL,$43B8            
23D9: 7E              LD      A,(HL)              
23DA: E6 0F           AND     $0F                 
23DC: FE 01           CP      $01                 
23DE: CA 98 3A        JP      Z,$3A98             ; {}
23E1: FE 03           CP      $03                 
23E3: CA 98 3A        JP      Z,$3A98             ; {}
23E6: FE 05           CP      $05                 
23E8: CA D0 3A        JP      Z,$3AD0             ; {}
23EB: FE 07           CP      $07                 
23ED: CA D0 3A        JP      Z,$3AD0             ; {}
23F0: FE 09           CP      $09                 
23F2: D8              RET     C                   
23F3: FE 0B           CP      $0B                 
23F5: DA 02 3B        JP      C,$3B02             ; {}
23F8: CD 02 3B        CALL    $3B02               ; {}
23FB: C3 98 3A        JP      $3A98               ; {}
23FE: FF              RST     0X38                
23FF: FF              RST     0X38                
2400: CD 2C 24        CALL    $242C               ; {}
2403: CA 52 25        JP      Z,$2552             ; {}
2406: FE 20           CP      $20                 
2408: DA 6A 24        JP      C,$246A             ; {}
240B: CA 20 25        JP      Z,$2520             ; {}
240E: 47              LD      B,A                 
240F: 0F              RRCA                        
2410: 00              NOP                         
2411: 78              LD      A,B                 
2412: D2 E8 20        JP      NC,$20E8            ; {}
2415: 7B              LD      A,E                 
2416: D6 05           SUB     $05                 
2418: C6 C0           ADD     $C0                 
241A: 4F              LD      C,A                 
241B: 7A              LD      A,D                 
241C: CE 00           ADC     $00                 
241E: 47              LD      B,A                 
241F: 7E              LD      A,(HL)              
2420: 11 00 2A        LD      DE,$2A00            
2423: 21 00 2B        LD      HL,$2B00            
2426: C3 85 20        JP      $2085               ; {}
2429: FF              RST     0X38                
242A: FF              RST     0X38                
242B: FF              RST     0X38                
242C: 21 B9 43        LD      HL,$43B9            
242F: 7E              LD      A,(HL)              
2430: E6 F8           AND     $F8                 
2432: 77              LD      (HL),A              
2433: 32 00 58        LD      ($5800),A           ; 58xx scroll register
2436: 11 C6 41        LD      DE,$41C6            
2439: 0F              RRCA                        
243A: 0F              RRCA                        
243B: 0F              RRCA                        
243C: 47              LD      B,A                 
243D: 7B              LD      A,E                 
243E: 90              SUB     B                   
243F: E6 1F           AND     $1F                 
2441: 47              LD      B,A                 
2442: 7B              LD      A,E                 
2443: E6 E0           AND     $E0                 
2445: B0              OR      B                   
2446: 5F              LD      E,A                 
2447: 2E A5           LD      L,$A5               
2449: 35              DEC     (HL)                
244A: 7E              LD      A,(HL)              
244B: C9              RET                         
244C: 21 A5 43        LD      HL,$43A5            
244F: 35              DEC     (HL)                
2450: 7E              LD      A,(HL)              
2451: 0F              RRCA                        
2452: DA F0 06        JP      C,$06F0             ; {}
2455: A7              AND     A                   
2456: C0              RET     NZ                  
2457: 2D              DEC     L                   
2458: 36 02           LD      (HL),$02            
245A: 2E B8           LD      L,$B8               
245C: 7E              LD      A,(HL)              
245D: E6 F0           AND     $F0                 
245F: C6 10           ADD     $10                 
2461: 77              LD      (HL),A              
2462: 2E BA           LD      L,$BA               
2464: 36 10           LD      (HL),$10            
2466: C3 80 03        JP      $0380               ; {}
2469: FF              RST     0X38                
246A: 01 14 09        LD      BC,$0914            
246D: 11 C6 4A        LD      DE,$4AC6            
2470: 21 00 1C        LD      HL,$1C00            
2473: C3 D6 0A        JP      $0AD6               ; {}
2476: 78              LD      A,B                 
2477: 81              ADD     A,C                 
2478: CD 95 24        CALL    $2495               ; {}
247B: 2E D3           LD      L,$D3               
247D: 77              LD      (HL),A              
247E: 21 BB 43        LD      HL,$43BB            
2481: 3E 08           LD      A,$08               
2483: 96              SUB     (HL)                
2484: 07              RLCA                        
2485: 2E 9A           LD      L,$9A               
2487: 86              ADD     A,(HL)              
2488: 07              RLCA                        
2489: 47              LD      B,A                 
248A: 2E 6F           LD      L,$6F               
248C: 7E              LD      A,(HL)              
248D: E6 1E           AND     $1E                 
248F: 80              ADD     A,B                 
2490: 32 D1 4B        LD      ($4BD1),A           
2493: C9              RET                         
2494: 1F              RRA                         
2495: 80              ADD     A,B                 
2496: 0D              DEC     C                   
2497: C8              RET     Z                   
2498: 80              ADD     A,B                 
2499: 0D              DEC     C                   
249A: C8              RET     Z                   
249B: 80              ADD     A,B                 
249C: 0D              DEC     C                   
249D: C8              RET     Z                   
249E: 87              ADD     A,A                 
249F: C9              RET                         
24A0: 3A B8 43        LD      A,($43B8)           
24A3: E6 0F           AND     $0F                 
24A5: FE 08           CP      $08                 
24A7: D8              RET     C                   
24A8: 11 C4 43        LD      DE,$43C4            
24AB: 21 E6 43        LD      HL,$43E6            
24AE: CD 51 23        CALL    $2351               ; {}
24B1: 3A 9B 43        LD      A,($439B)           ; {ram.Counter+1}
24B4: E6 03           AND     $03                 
24B6: FE 03           CP      $03                 
24B8: C0              RET     NZ                  
24B9: C3 F2 24        JP      $24F2               ; {}
24BC: CD 51 23        CALL    $2351               ; {}
24BF: C9              RET                         
24C0: FF              RST     0X38                
24C1: FF              RST     0X38                
24C2: FF              RST     0X38                
24C3: FF              RST     0X38                
24C4: 3A B8 43        LD      A,($43B8)           
24C7: E6 0F           AND     $0F                 
24C9: FE 08           CP      $08                 
24CB: DA F0 06        JP      C,$06F0             ; {}
24CE: CD E0 24        CALL    $24E0               ; {}
24D1: 21 AA 43        LD      HL,$43AA            
24D4: 34              INC     (HL)                
24D5: 7E              LD      A,(HL)              
24D6: E6 03           AND     $03                 
24D8: CA FA 22        JP      Z,$22FA             ; {}
24DB: C3 22 23        JP      $2322               ; {}
24DE: 24              INC     H                   
24DF: BF              CP      A                   
24E0: 3A AA 43        LD      A,($43AA)           
24E3: E6 0F           AND     $0F                 
24E5: C0              RET     NZ                  
24E6: 3A B9 43        LD      A,($43B9)           
24E9: FE A0           CP      $A0                 
24EB: D8              RET     C                   
24EC: C3 7A 06        JP      $067A               ; {}
24EF: FA 22 C3        JP      M,$C322             
24F2: CD AA 30        CALL    $30AA               ; {}
24F5: C6 60           ADD     $60                 
24F7: 00              NOP                         
24F8: 47              LD      B,A                 
24F9: 21 9B 43        LD      HL,$439B            
24FC: E6 0E           AND     $0E                 
24FE: A6              AND     (HL)                
24FF: C0              RET     NZ                  
2500: 3A 9E 43        LD      A,($439E)           
2503: B8              CP      B                   
2504: D0              RET     NC                  
2505: 3A 9F 43        LD      A,($439F)           
2508: B8              CP      B                   
2509: D8              RET     C                   
250A: 78              LD      A,B                 
250B: D6 04           SUB     $04                 
250D: 47              LD      B,A                 
250E: 3A B9 43        LD      A,($43B9)           
2511: 2F              CPL                         
2512: 3C              INC     A                   
2513: E6 F8           AND     $F8                 
2515: C6 48           ADD     $48                 
2517: 4F              LD      C,A                 
2518: E5              PUSH    HL                  
2519: E5              PUSH    HL                  
251A: C3 B7 25        JP      $25B7               ; {}
251D: FF              RST     0X38                
251E: FF              RST     0X38                
251F: FF              RST     0X38                
2520: D5              PUSH    DE                  
2521: CD 80 03        CALL    $0380               ; {}
2524: D1              POP     DE                  
2525: 3A B9 43        LD      A,($43B9)           
2528: C6 60           ADD     $60                 
252A: 0F              RRCA                        
252B: 47              LD      B,A                 
252C: 3A B8 43        LD      A,($43B8)           
252F: E6 F0           AND     $F0                 
2531: 80              ADD     A,B                 
2532: 06 90           LD      B,$90               
2534: DA 3D 25        JP      C,$253D             ; {}
2537: FE 90           CP      $90                 
2539: D2 3D 25        JP      NC,$253D            ; {}
253C: 47              LD      B,A                 
253D: AF              XOR     A                   
253E: 78              LD      A,B                 
253F: 27              DAA                         
2540: 21 9D 43        LD      HL,$439D            
2543: 77              LD      (HL),A              
2544: 2C              INC     L                   
2545: 36 00           LD      (HL),$00            
2547: 7B              LD      A,E                 
2548: D6 5E           SUB     $5E                 
254A: 5F              LD      E,A                 
254B: 06 04           LD      B,$04               
254D: C3 C4 00        JP      $00C4               ; {}
2550: 32 80 2E        LD      ($2E80),A           ; {}
2553: A4              AND     H                   
2554: 36 07           LD      (HL),$07            
2556: 2C              INC     L                   
2557: 36 40           LD      (HL),$40            
2559: 2E 6B           LD      L,$6B               
255B: 36 FF           LD      (HL),$FF            
255D: C9              RET                         
255E: FF              RST     0X38                
255F: FF              RST     0X38                
2560: 21 93 43        LD      HL,$4393            
2563: 7E              LD      A,(HL)              
2564: E6 01           AND     $01                 
2566: 07              RLCA                        
2567: 07              RLCA                        
2568: 07              RLCA                        
2569: 07              RLCA                        
256A: 07              RLCA                        
256B: C6 70           ADD     $70                 
256D: 6F              LD      L,A                 
256E: 26 4B           LD      H,$4B               
2570: 1E 08           LD      E,$08               
2572: 3A 57 43        LD      A,($4357)           
2575: 07              RLCA                        
2576: 07              RLCA                        
2577: 07              RLCA                        
2578: 00              NOP                         
2579: C6 AD           ADD     $AD                 
257B: 57              LD      D,A                 
257C: 3A 9F 43        LD      A,($439F)           
257F: C6 03           ADD     $03                 
2581: 4F              LD      C,A                 
2582: 3A 9E 43        LD      A,($439E)           
2585: D6 0A           SUB     $0A                 
2587: 47              LD      B,A                 
2588: E5              PUSH    HL                  
2589: CD 96 25        CALL    $2596               ; {}
258C: E1              POP     HL                  
258D: 7D              LD      A,L                 
258E: C6 04           ADD     $04                 
2590: 6F              LD      L,A                 
2591: 1D              DEC     E                   
2592: C2 88 25        JP      NZ,$2588            ; {}
2595: C9              RET                         
2596: 7E              LD      A,(HL)              
2597: E6 08           AND     $08                 
2599: C8              RET     Z                   
259A: 2C              INC     L                   
259B: 7E              LD      A,(HL)              
259C: FE 08           CP      $08                 
259E: C8              RET     Z                   
259F: FE 88           CP      $88                 
25A1: D0              RET     NC                  
25A2: 2C              INC     L                   
25A3: 7E              LD      A,(HL)              
25A4: B8              CP      B                   
25A5: D8              RET     C                   
25A6: B9              CP      C                   
25A7: D0              RET     NC                  
25A8: 2C              INC     L                   
25A9: 7E              LD      A,(HL)              
25AA: BA              CP      D                   
25AB: D0              RET     NC                  
25AC: FE 80           CP      $80                 
25AE: D8              RET     C                   
25AF: 00              NOP                         
25B0: 00              NOP                         
25B1: 00              NOP                         
25B2: 00              NOP                         
25B3: 00              NOP                         
25B4: 4F              LD      C,A                 
25B5: 2D              DEC     L                   
25B6: 46              LD      B,(HL)              
25B7: 3A B8 43        LD      A,($43B8)           
25BA: 16 03           LD      D,$03               
25BC: FE 10           CP      $10                 
25BE: DA CA 25        JP      C,$25CA             ; {}
25C1: 16 04           LD      D,$04               
25C3: FE 20           CP      $20                 
25C5: DA CA 25        JP      C,$25CA             ; {}
25C8: 16 05           LD      D,$05               
25CA: 21 CC 43        LD      HL,$43CC            
25CD: 7E              LD      A,(HL)              
25CE: E6 08           AND     $08                 
25D0: CA E0 25        JP      Z,$25E0             ; {}
25D3: 7D              LD      A,L                 
25D4: C6 04           ADD     $04                 
25D6: 6F              LD      L,A                 
25D7: 15              DEC     D                   
25D8: C2 CD 25        JP      NZ,$25CD            ; {}
25DB: E1              POP     HL                  
25DC: E1              POP     HL                  
25DD: C9              RET                         
25DE: FF              RST     0X38                
25DF: FF              RST     0X38                
25E0: 78              LD      A,B                 
25E1: C6 04           ADD     $04                 
25E3: 47              LD      B,A                 
25E4: 79              LD      A,C                 
25E5: C6 0C           ADD     $0C                 
25E7: 4F              LD      C,A                 
25E8: 36 08           LD      (HL),$08            
25EA: 2C              INC     L                   
25EB: 78              LD      A,B                 
25EC: 0F              RRCA                        
25ED: E6 03           AND     $03                 
25EF: 57              LD      D,A                 
25F0: 79              LD      A,C                 
25F1: E6 04           AND     $04                 
25F3: 82              ADD     A,D                 
25F4: C6 58           ADD     $58                 
25F6: 77              LD      (HL),A              
25F7: 2C              INC     L                   
25F8: 70              LD      (HL),B              
25F9: 2C              INC     L                   
25FA: 71              LD      (HL),C              
25FB: E1              POP     HL                  
25FC: E1              POP     HL                  
25FD: C9              RET                         
25FE: FF              RST     0X38                
25FF: FF              RST     0X38                
2600: 00              NOP                         
2601: 00              NOP                         
2602: 00              NOP                         
2603: 00              NOP                         
2604: 00              NOP                         
2605: 3A B9 43        LD      A,($43B9)           
2608: 2F              CPL                         
2609: 0F              RRCA                        
260A: 0F              RRCA                        
260B: 0F              RRCA                        
260C: E6 1F           AND     $1F                 
260E: 21 D2 4B        LD      HL,$4BD2            
2611: 77              LD      (HL),A              
2612: 2C              INC     L                   
2613: 3A D1 4B        LD      A,($4BD1)           
2616: BE              CP      (HL)                
2617: DA 50 26        JP      C,$2650             ; {}
261A: 3A D5 4B        LD      A,($4BD5)           
261D: 57              LD      D,A                 
261E: E6 03           AND     $03                 
2620: 5F              LD      E,A                 
2621: 3A 9B 43        LD      A,($439B)           ; {ram.Counter+1}
2624: 07              RLCA                        
2625: 07              RLCA                        
2626: E6 0C           AND     $0C                 
2628: 83              ADD     A,E                 
2629: C6 D0           ADD     $D0                 
262B: 6F              LD      L,A                 
262C: 26 3E           LD      H,$3E               
262E: 7A              LD      A,D                 
262F: 0F              RRCA                        
2630: 0F              RRCA                        
2631: E6 07           AND     $07                 
2633: 86              ADD     A,(HL)              
2634: 57              LD      D,A                 
2635: 3A B9 43        LD      A,($43B9)           
2638: 92              SUB     D                   
2639: 32 B9 43        LD      ($43B9),A           
263C: 32 00 58        LD      ($5800),A           ; 58xx scroll register
263F: 3A 9B 43        LD      A,($439B)           ; {ram.Counter+1}
2642: 0F              RRCA                        
2643: D2 D0 26        JP      NC,$26D0            ; {}
2646: CD 68 26        CALL    $2668               ; {}
2649: C3 AA 26        JP      $26AA               ; {}
264C: C2 3A 26        JP      NZ,$263A            ; {}
264F: 3A 2C 3A        LD      A,($3A2C)           ; {}
2652: 9B              SBC     E                   
2653: 43              LD      B,E                 
2654: 07              RLCA                        
2655: 07              RLCA                        
2656: E6 0C           AND     $0C                 
2658: 86              ADD     A,(HL)              
2659: C6 D0           ADD     $D0                 
265B: 6F              LD      L,A                 
265C: 26 3E           LD      H,$3E               
265E: 3A B9 43        LD      A,($43B9)           
2661: 86              ADD     A,(HL)              
2662: C3 39 26        JP      $2639               ; {}
2665: D2 AE 26        JP      NC,$26AE            ; {}
2668: 3A 6E 43        LD      A,($436E)           
266B: 00              NOP                         
266C: 47              LD      B,A                 
266D: 3A 9A 43        LD      A,($439A)           ; {ram.Counter}
2670: FE 18           CP      $18                 
2672: DA 76 26        JP      C,$2676             ; {}
2675: 04              INC     B                   
2676: FE 10           CP      $10                 
2678: DA 7C 26        JP      C,$267C             ; {}
267B: 04              INC     B                   
267C: 3A BA 43        LD      A,($43BA)           
267F: FE 03           CP      $03                 
2681: D2 85 26        JP      NC,$2685            ; {}
2684: 04              INC     B                   
2685: 3A D6 4B        LD      A,($4BD6)           
2688: C6 E0           ADD     $E0                 
268A: 6F              LD      L,A                 
268B: 26 3E           LD      H,$3E               
268D: 78              LD      A,B                 
268E: BE              CP      (HL)                
268F: DA 93 26        JP      C,$2693             ; {}
2692: 7E              LD      A,(HL)              
2693: 57              LD      D,A                 
2694: 3A BB 43        LD      A,($43BB)           
2697: FE 04           CP      $04                 
2699: D2 9D 26        JP      NC,$269D            ; {}
269C: 14              INC     D                   
269D: FE 02           CP      $02                 
269F: D2 A3 26        JP      NC,$26A3            ; {}
26A2: 14              INC     D                   
26A3: 7A              LD      A,D                 
26A4: 32 D5 4B        LD      ($4BD5),A           
26A7: C9              RET                         
26A8: 00              NOP                         
26A9: 58              LD      E,B                 
26AA: 21 D3 4B        LD      HL,$4BD3            
26AD: 7E              LD      A,(HL)              
26AE: 35              DEC     (HL)                
26AF: A7              AND     A                   
26B0: C0              RET     NZ                  
26B1: 34              INC     (HL)                
26B2: 2E D6           LD      L,$D6               
26B4: 7E              LD      A,(HL)              
26B5: FE 16           CP      $16                 
26B7: D0              RET     NC                  
26B8: FE 08           CP      $08                 
26BA: D8              RET     C                   
26BB: 2C              INC     L                   
26BC: 96              SUB     (HL)                
26BD: 07              RLCA                        
26BE: 47              LD      B,A                 
26BF: 3A 6F 43        LD      A,($436F)           
26C2: E6 03           AND     $03                 
26C4: 2E D4           LD      L,$D4               
26C6: 77              LD      (HL),A              
26C7: 2F              CPL                         
26C8: E6 03           AND     $03                 
26CA: 3C              INC     A                   
26CB: 4F              LD      C,A                 
26CC: C3 76 24        JP      $2476               ; {}
26CF: C9              RET                         
26D0: 21 A8 4B        LD      HL,$4BA8            
26D3: 01 00 08        LD      BC,$0800            
26D6: 11 00 80        LD      DE,$8000            
26D9: 7E              LD      A,(HL)              
26DA: A7              AND     A                   
26DB: CA E5 26        JP      Z,$26E5             ; {}
26DE: 7A              LD      A,D                 
26DF: 07              RLCA                        
26E0: D2 E4 26        JP      NC,$26E4            ; {}
26E3: 51              LD      D,C                 
26E4: 59              LD      E,C                 
26E5: 0C              INC     C                   
26E6: 7D              LD      A,L                 
26E7: 90              SUB     B                   
26E8: 6F              LD      L,A                 
26E9: FE 68           CP      $68                 
26EB: C2 D9 26        JP      NZ,$26D9            ; {}
26EE: 3A D2 4B        LD      A,($4BD2)           
26F1: 82              ADD     A,D                 
26F2: 83              ADD     A,E                 
26F3: E6 1F           AND     $1F                 
26F5: 32 D6 4B        LD      ($4BD6),A           
26F8: 7B              LD      A,E                 
26F9: 92              SUB     D                   
26FA: 32 D7 4B        LD      ($4BD7),A           
26FD: C9              RET                         
26FE: FF              RST     0X38                
26FF: FF              RST     0X38                


2700: 21 A2 43        LD      HL,$43A2            
2703: 7E              LD      A,(HL)              
2704: A7              AND     A                   
2705: C8              RET     Z                   
2706: 2C              INC     L                   
2707: 7E              LD      A,(HL)              
2708: E6 01           AND     $01                 
270A: 07              RLCA                        
270B: 07              RLCA                        
270C: C6 83           ADD     $83                 
270E: 6F              LD      L,A                 
270F: 3E FF           LD      A,$FF               
2711: 32 97 43        LD      ($4397),A           
2714: 11 70 43        LD      DE,$4370            
2717: CD 48 27        CALL    $2748               ; {}
271A: 1C              INC     E                   
271B: 1C              INC     E                   
271C: 1C              INC     E                   
271D: 7B              LD      A,E                 
271E: FE 80           CP      $80                 
2720: C2 17 27        JP      NZ,$2717            ; {}
2723: 1E 9D           LD      E,$9D               
2725: 3A A4 43        LD      A,($43A4)           ; {ram.M43A4}
2728: FE 06           CP      $06                 
272A: C2 39 27        JP      NZ,$2739            ; {}
272D: 1A              LD      A,(DE)              
272E: 47              LD      B,A                 
272F: 0E 00           LD      C,$00               
2731: CD 20 02        CALL    $0220               ; {code.AddToScore}
2734: AF              XOR     A                   
2735: 12              LD      (DE),A              
2736: 32 97 43        LD      ($4397),A           
2739: 3A 97 43        LD      A,($4397)           
273C: A7              AND     A                   
273D: CC 68 27        CALL    Z,$2768             ; {}
2740: CD A8 27        CALL    $27A8               ; {}
2743: C3 10 3A        JP      $3A10               ; {}
2746: FF              RST     0X38                
2747: FF              RST     0X38                
2748: 1A              LD      A,(DE)              
2749: 1C              INC     E                   
274A: FE 01           CP      $01                 
274C: C0              RET     NZ                  
274D: 1A              LD      A,(DE)              
274E: A7              AND     A                   
274F: C8              RET     Z                   
2750: 0F              RRCA                        
2751: 0F              RRCA                        
2752: 0F              RRCA                        
2753: 0F              RRCA                        
2754: 47              LD      B,A                 
2755: E6 F0           AND     $F0                 
2757: 4F              LD      C,A                 
2758: 78              LD      A,B                 
2759: E6 0F           AND     $0F                 
275B: 47              LD      B,A                 
275C: CD 20 02        CALL    $0220               ; {code.AddToScore}
275F: AF              XOR     A                   
2760: 12              LD      (DE),A              
2761: 32 97 43        LD      ($4397),A           
2764: C9              RET                         
2765: FF              RST     0X38                
2766: FF              RST     0X38                
2767: FF              RST     0X38                
2768: E5              PUSH    HL                  
2769: 11 61 42        LD      DE,$4261            
276C: 06 06           LD      B,$06               
276E: 3A A3 43        LD      A,($43A3)           
2771: A7              AND     A                   
2772: CA 78 27        JP      Z,$2778             ; {}
2775: 11 21 40        LD      DE,$4021            
2778: CD C4 00        CALL    $00C4               ; {}
277B: E1              POP     HL                  
277C: 11 BD 43        LD      DE,$43BD            
277F: EB              EX      DE,HL               
2780: 7E              LD      A,(HL)              
2781: 2C              INC     L                   
2782: B6              OR      (HL)                
2783: C8              RET     Z                   
2784: 2C              INC     L                   
2785: EB              EX      DE,HL               
2786: CD 14 03        CALL    $0314               ; {}
2789: D0              RET     NC                  
278A: 3A A3 43        LD      A,($43A3)           
278D: C6 90           ADD     $90                 
278F: 6F              LD      L,A                 
2790: 34              INC     (HL)                
2791: CD 67 03        CALL    $0367               ; {}
2794: 3E FF           LD      A,$FF               
2796: 32 6A 43        LD      ($436A),A           
2799: 2E BE           LD      L,$BE               
279B: 7E              LD      A,(HL)              
279C: 36 00           LD      (HL),$00            
279E: 0F              RRCA                        
279F: 0F              RRCA                        
27A0: 0F              RRCA                        
27A1: 0F              RRCA                        
27A2: 2D              DEC     L                   
27A3: 77              LD      (HL),A              
27A4: C9              RET                         
27A5: FF              RST     0X38                
27A6: FF              RST     0X38                
27A7: FF              RST     0X38                
27A8: 21 8C 43        LD      HL,$438C            
27AB: 7E              LD      A,(HL)              
27AC: 32 00 60        LD      ($6000),A           ; 60xx sound A
27AF: 2C              INC     L                   
27B0: 7E              LD      A,(HL)              
27B1: 32 00 68        LD      ($6800),A           ; 68xx sound B
27B4: F6 0F           OR      $0F                 
27B6: 77              LD      (HL),A              
27B7: 2D              DEC     L                   
27B8: 36 0F           LD      (HL),$0F            
27BA: C9              RET                         
27BB: FF              RST     0X38                
27BC: FF              RST     0X38                
27BD: 21 63 43        LD      HL,$4363            
27C0: 7E              LD      A,(HL)              
27C1: A7              AND     A                   
27C2: C2 E2 27        JP      NZ,$27E2            ; {}
27C5: 2E 61           LD      L,$61               
27C7: 7E              LD      A,(HL)              
27C8: A7              AND     A                   
27C9: C8              RET     Z                   
27CA: FE 19           CP      $19                 
27CC: D2 D8 27        JP      NC,$27D8            ; {}
27CF: 35              DEC     (HL)                
27D0: 2E 8C           LD      L,$8C               
27D2: 7E              LD      A,(HL)              
27D3: F6 40           OR      $40                 
27D5: 77              LD      (HL),A              
27D6: C9              RET                         
27D7: 77              LD      (HL),A              
27D8: 36 18           LD      (HL),$18            
27DA: 2E 8C           LD      L,$8C               
27DC: 7E              LD      A,(HL)              
27DD: E6 BF           AND     $BF                 
27DF: 77              LD      (HL),A              
27E0: C9              RET                         
27E1: 36 FE           LD      (HL),$FE            
27E3: 40              LD      B,B                 
27E4: DA E9 27        JP      C,$27E9             ; {}
27E7: 36 40           LD      (HL),$40            
27E9: 35              DEC     (HL)                
27EA: 2E 8C           LD      L,$8C               
27EC: 36 8F           LD      (HL),$8F            
27EE: C9              RET                         
27EF: FF              RST     0X38                
27F0: FF              RST     0X38                
27F1: FF              RST     0X38                
27F2: FF              RST     0X38                
27F3: FF              RST     0X38                
27F4: FF              RST     0X38                
27F5: FF              RST     0X38                
27F6: FF              RST     0X38                
27F7: FF              RST     0X38                
27F8: FF              RST     0X38                
27F9: FF              RST     0X38                
27FA: FF              RST     0X38                
27FB: FF              RST     0X38                
27FC: FF              RST     0X38                
27FD: FF              RST     0X38                
27FE: FF              RST     0X38                
27FF: FF              RST     0X38                
2800: 00              NOP                         
2801: 32 00 00        LD      ($0000),A           ; {}
2804: 00              NOP                         
2805: 00              NOP                         
2806: 00              NOP                         
2807: 00              NOP                         
2808: 00              NOP                         
2809: 00              NOP                         
280A: 00              NOP                         
280B: 00              NOP                         
280C: 00              NOP                         
280D: 00              NOP                         
280E: 42              LD      B,D                 
280F: 42              LD      B,D                 
2810: 00              NOP                         
2811: 00              NOP                         
2812: 00              NOP                         
2813: 00              NOP                         
2814: 00              NOP                         
2815: 00              NOP                         
2816: 00              NOP                         
2817: 00              NOP                         
2818: 00              NOP                         
2819: 00              NOP                         
281A: E1              POP     HL                  
281B: 00              NOP                         
281C: 00              NOP                         
281D: E2 00 00        JP      PO,$0000            ; {}
2820: 32 00 00        LD      ($0000),A           ; {}
2823: 00              NOP                         
2824: 00              NOP                         
2825: 00              NOP                         
2826: 00              NOP                         
2827: 00              NOP                         
2828: 00              NOP                         
2829: E0              RET     PO                  
282A: 00              NOP                         
282B: 00              NOP                         
282C: 40              LD      B,B                 
282D: 00              NOP                         
282E: 00              NOP                         
282F: C3 00 00        JP      $0000               ; {}
2832: 00              NOP                         
2833: 00              NOP                         
2834: 00              NOP                         
2835: 00              NOP                         
2836: DF              RST     0X18                
2837: 00              NOP                         
2838: 00              NOP                         
2839: E2 00 00        JP      PO,$0000            ; {}
283C: E0              RET     PO                  
283D: 00              NOP                         
283E: E1              POP     HL                  
283F: 00              NOP                         
2840: 00              NOP                         
2841: 30 00           JR      NC,$2843            ; {}
2843: 00              NOP                         
2844: 00              NOP                         
2845: 00              NOP                         
2846: DE 00           SBC     $00                 
2848: 00              NOP                         
2849: 00              NOP                         
284A: C2 00 40        JP      NZ,$4000            
284D: 00              NOP                         
284E: E0              RET     PO                  
284F: 00              NOP                         
2850: 00              NOP                         
2851: 00              NOP                         
2852: 00              NOP                         
2853: 30 00           JR      NC,$2855            ; {}
2855: 30 00           JR      NC,$2857            ; {}
2857: 5A              LD      E,D                 
2858: 00              NOP                         
2859: 00              NOP                         
285A: E1              POP     HL                  
285B: 00              NOP                         
285C: 40              LD      B,B                 
285D: 00              NOP                         
285E: E2 00 00        JP      PO,$0000            ; {}
2861: 00              NOP                         
2862: 00              NOP                         
2863: 00              NOP                         
2864: 00              NOP                         
2865: 00              NOP                         
2866: 00              NOP                         
2867: 30 C1           JR      NC,$282A            ; {}
2869: 3E 00           LD      A,$00               
286B: E0              RET     PO                  
286C: 00              NOP                         
286D: 40              LD      B,B                 
286E: C2 00 00        JP      NZ,$0000            ; {}
2871: 00              NOP                         
2872: 00              NOP                         
2873: 00              NOP                         
2874: 00              NOP                         
2875: 00              NOP                         
2876: 00              NOP                         
2877: 00              NOP                         
2878: 00              NOP                         
2879: 5A              LD      E,D                 
287A: C1              POP     BC                  
287B: 3E C8           LD      A,$C8               
287D: D8              RET     C                   
287E: 00              NOP                         
287F: 00              NOP                         
2880: E0              RET     PO                  
2881: E1              POP     HL                  
2882: C2 E2 E0        JP      NZ,$E0E2            
2885: 00              NOP                         
2886: E1              POP     HL                  
2887: 00              NOP                         
2888: C2 00 E2        JP      NZ,$E200            
288B: CE CA           ADC     $CA                 
288D: DA 00 00        JP      C,$0000             ; {}
2890: 00              NOP                         
2891: 00              NOP                         
2892: 00              NOP                         
2893: 00              NOP                         
2894: 00              NOP                         
2895: 00              NOP                         
2896: 00              NOP                         
2897: 00              NOP                         
2898: CF              RST     0X08                
2899: CF              RST     0X08                
289A: C3 3F C2        JP      $C23F               
289D: 41              LD      B,C                 
289E: E0              RET     PO                  
289F: 00              NOP                         
28A0: 00              NOP                         
28A1: 00              NOP                         
28A2: 00              NOP                         
28A3: 00              NOP                         
28A4: 00              NOP                         
28A5: 00              NOP                         
28A6: 00              NOP                         
28A7: DE 00           SBC     $00                 
28A9: 3F              CCF                         
28AA: 00              NOP                         
28AB: C2 41 00        JP      NZ,$0041            ; {}
28AE: E1              POP     HL                  
28AF: 00              NOP                         
28B0: 00              NOP                         
28B1: 00              NOP                         
28B2: 00              NOP                         
28B3: 00              NOP                         
28B4: 00              NOP                         
28B5: 3D              DEC     A                   
28B6: DF              RST     0X18                
28B7: 3D              DEC     A                   
28B8: 00              NOP                         
28B9: 00              NOP                         
28BA: E1              POP     HL                  
28BB: 00              NOP                         
28BC: 41              LD      B,C                 
28BD: 00              NOP                         
28BE: 00              NOP                         
28BF: C2 00 00        JP      NZ,$0000            ; {}
28C2: 00              NOP                         
28C3: 3D              DEC     A                   
28C4: 00              NOP                         
28C5: 00              NOP                         
28C6: 00              NOP                         
28C7: 00              NOP                         
28C8: 00              NOP                         
28C9: E0              RET     PO                  
28CA: 00              NOP                         
28CB: 00              NOP                         
28CC: 41              LD      B,C                 
28CD: 00              NOP                         
28CE: 00              NOP                         
28CF: E2 00 00        JP      PO,$0000            ; {}
28D2: 3D              DEC     A                   
28D3: 00              NOP                         
28D4: 00              NOP                         
28D5: 00              NOP                         
28D6: 00              NOP                         
28D7: 00              NOP                         
28D8: E2 00 00        JP      PO,$0000            ; {}
28DB: 00              NOP                         
28DC: 00              NOP                         
28DD: 4F              LD      C,A                 
28DE: 00              NOP                         
28DF: E0              RET     PO                  
28E0: 00              NOP                         
28E1: 3B              DEC     SP                  
28E2: 00              NOP                         
28E3: 00              NOP                         
28E4: 00              NOP                         
28E5: 00              NOP                         
28E6: 00              NOP                         
28E7: 00              NOP                         
28E8: 00              NOP                         
28E9: C2 00 00        JP      NZ,$0000            ; {}
28EC: 00              NOP                         
28ED: 4F              LD      C,A                 
28EE: 00              NOP                         
28EF: 00              NOP                         
28F0: 00              NOP                         
28F1: 00              NOP                         
28F2: 3B              DEC     SP                  
28F3: 00              NOP                         
28F4: 00              NOP                         
28F5: 00              NOP                         
28F6: 00              NOP                         
28F7: 00              NOP                         
28F8: 00              NOP                         
28F9: 00              NOP                         
28FA: 00              NOP                         
28FB: 00              NOP                         
28FC: 00              NOP                         
28FD: 00              NOP                         
28FE: 4D              LD      C,L                 
28FF: 4D              LD      C,L                 
2900: 00              NOP                         
2901: 00              NOP                         
2902: 00              NOP                         
2903: 00              NOP                         
2904: 00              NOP                         
2905: 00              NOP                         
2906: 00              NOP                         
2907: 00              NOP                         
2908: 00              NOP                         
2909: 00              NOP                         
290A: 00              NOP                         
290B: 00              NOP                         
290C: 00              NOP                         
290D: 20 00           JR      NZ,$290F            ; {}
290F: 38 00           JR      C,$2911             ; {}
2911: 34              INC     (HL)                
2912: 00              NOP                         
2913: 28 00           JR      Z,$2915             ; {}
2915: 00              NOP                         
2916: 00              NOP                         
2917: 00              NOP                         
2918: 00              NOP                         
2919: 00              NOP                         
291A: 00              NOP                         
291B: 00              NOP                         
291C: 00              NOP                         
291D: 00              NOP                         
291E: 00              NOP                         
291F: 00              NOP                         
2920: 00              NOP                         
2921: 00              NOP                         
2922: 00              NOP                         
2923: 00              NOP                         
2924: 00              NOP                         
2925: 00              NOP                         
2926: 00              NOP                         
2927: 00              NOP                         
2928: 00              NOP                         
2929: 00              NOP                         
292A: 00              NOP                         
292B: 10 00           DJNZ    $292D               ; {}
292D: 02              LD      (BC),A              
292E: 00              NOP                         
292F: 00              NOP                         
2930: 00              NOP                         
2931: 01 00 00        LD      BC,$0000            
2934: 12              LD      (DE),A              
2935: 00              NOP                         
2936: 00              NOP                         
2937: 00              NOP                         
2938: 00              NOP                         
2939: 00              NOP                         
293A: 00              NOP                         
293B: 00              NOP                         
293C: 00              NOP                         
293D: 00              NOP                         
293E: 00              NOP                         
293F: 00              NOP                         
2940: 00              NOP                         
2941: 00              NOP                         
2942: 00              NOP                         
2943: 00              NOP                         
2944: 00              NOP                         
2945: 00              NOP                         
2946: 00              NOP                         
2947: 00              NOP                         
2948: 00              NOP                         
2949: 10 00           DJNZ    $294B               ; {}
294B: 00              NOP                         
294C: 80              ADD     A,B                 
294D: 48              LD      C,B                 
294E: 00              NOP                         
294F: 04              INC     B                   
2950: 40              LD      B,B                 
2951: 08              EX      AF,AF'              
2952: 00              NOP                         
2953: 50              LD      D,B                 
2954: 00              NOP                         
2955: 00              NOP                         
2956: 80              ADD     A,B                 
2957: 10 00           DJNZ    $2959               ; {}
2959: 00              NOP                         
295A: 00              NOP                         
295B: 00              NOP                         
295C: 00              NOP                         
295D: 00              NOP                         
295E: 00              NOP                         
295F: 00              NOP                         
2960: 00              NOP                         
2961: 00              NOP                         
2962: 00              NOP                         
2963: 00              NOP                         
2964: 00              NOP                         
2965: 00              NOP                         
2966: 00              NOP                         
2967: 10 00           DJNZ    $2969               ; {}
2969: 00              NOP                         
296A: 20 44           JR      NZ,$29B0            ; {}
296C: 00              NOP                         
296D: 00              NOP                         
296E: 00              NOP                         
296F: 02              LD      (BC),A              
2970: 10 00           DJNZ    $2972               ; {}
2972: 00              NOP                         
2973: 04              INC     B                   
2974: 00              NOP                         
2975: 48              LD      C,B                 
2976: 20 00           JR      NZ,$2978            ; {}
2978: 00              NOP                         
2979: 10 00           DJNZ    $297B               ; {}
297B: 00              NOP                         
297C: 00              NOP                         
297D: 00              NOP                         
297E: 00              NOP                         
297F: 00              NOP                         
2980: 00              NOP                         
2981: 00              NOP                         
2982: 00              NOP                         
2983: 00              NOP                         
2984: 00              NOP                         
2985: 10 00           DJNZ    $2987               ; {}
2987: 00              NOP                         
2988: 00              NOP                         
2989: 44              LD      B,H                 
298A: 08              EX      AF,AF'              
298B: 00              NOP                         
298C: 00              NOP                         
298D: 01 00 00        LD      BC,$0000            
2990: 08              EX      AF,AF'              
2991: 00              NOP                         
2992: 00              NOP                         
2993: 02              LD      (BC),A              
2994: 00              NOP                         
2995: 00              NOP                         
2996: 00              NOP                         
2997: 84              ADD     A,H                 
2998: 08              EX      AF,AF'              
2999: 00              NOP                         
299A: 00              NOP                         
299B: 20 00           JR      NZ,$299D            ; {}
299D: 00              NOP                         
299E: 00              NOP                         
299F: 00              NOP                         
29A0: 00              NOP                         
29A1: 00              NOP                         
29A2: 00              NOP                         
29A3: 20 00           JR      NZ,$29A5            ; {}
29A5: 00              NOP                         
29A6: 00              NOP                         
29A7: 42              LD      B,D                 
29A8: 02              LD      (BC),A              
29A9: 00              NOP                         
29AA: 80              ADD     A,B                 
29AB: 00              NOP                         
29AC: 00              NOP                         
29AD: 00              NOP                         
29AE: 00              NOP                         
29AF: 00              NOP                         
29B0: 04              INC     B                   
29B1: 00              NOP                         
29B2: 00              NOP                         
29B3: 01 00 00        LD      BC,$0000            
29B6: 00              NOP                         
29B7: 00              NOP                         
29B8: 00              NOP                         
29B9: 82              ADD     A,D                 
29BA: 04              INC     B                   
29BB: 00              NOP                         
29BC: 00              NOP                         
29BD: 20 00           JR      NZ,$29BF            ; {}
29BF: 00              NOP                         
29C0: 00              NOP                         
29C1: 40              LD      B,B                 
29C2: 00              NOP                         
29C3: 00              NOP                         
29C4: 01 82 00        LD      BC,$0082            
29C7: 00              NOP                         
29C8: 40              LD      B,B                 
29C9: 00              NOP                         
29CA: 00              NOP                         
29CB: 00              NOP                         
29CC: 00              NOP                         
29CD: 00              NOP                         
29CE: 00              NOP                         
29CF: 00              NOP                         
29D0: 02              LD      (BC),A              
29D1: 00              NOP                         
29D2: 00              NOP                         
29D3: 00              NOP                         
29D4: 80              ADD     A,B                 
29D5: 00              NOP                         
29D6: 00              NOP                         
29D7: 00              NOP                         
29D8: 00              NOP                         
29D9: 00              NOP                         
29DA: 00              NOP                         
29DB: 81              ADD     A,C                 
29DC: 02              LD      (BC),A              
29DD: 00              NOP                         
29DE: 00              NOP                         
29DF: 40              LD      B,B                 
29E0: 02              LD      (BC),A              
29E1: 80              ADD     A,B                 
29E2: 00              NOP                         
29E3: 04              INC     B                   
29E4: 00              NOP                         
29E5: 00              NOP                         
29E6: 40              LD      B,B                 
29E7: 00              NOP                         
29E8: 00              NOP                         
29E9: 00              NOP                         
29EA: 00              NOP                         
29EB: 00              NOP                         
29EC: 00              NOP                         
29ED: 00              NOP                         
29EE: 00              NOP                         
29EF: 00              NOP                         
29F0: 01 00 00        LD      BC,$0000            
29F3: 00              NOP                         
29F4: 00              NOP                         
29F5: 00              NOP                         
29F6: 40              LD      B,B                 
29F7: 00              NOP                         
29F8: 00              NOP                         
29F9: 00              NOP                         
29FA: 00              NOP                         
29FB: 00              NOP                         
29FC: 00              NOP                         
29FD: 02              LD      (BC),A              
29FE: 04              INC     B                   
29FF: 08              EX      AF,AF'              
2A00: 00              NOP                         
2A01: 00              NOP                         
2A02: 00              NOP                         
2A03: 00              NOP                         
2A04: 00              NOP                         
2A05: 00              NOP                         
2A06: 00              NOP                         
2A07: D2 00 00        JP      NC,$0000            ; {}
2A0A: 00              NOP                         
2A0B: 00              NOP                         
2A0C: 00              NOP                         
2A0D: 00              NOP                         
2A0E: 00              NOP                         
2A0F: 00              NOP                         
2A10: 00              NOP                         
2A11: 00              NOP                         
2A12: 00              NOP                         
2A13: 00              NOP                         
2A14: 00              NOP                         
2A15: DE 00           SBC     $00                 
2A17: 5E              LD      E,(HL)              
2A18: E0              RET     PO                  
2A19: 00              NOP                         
2A1A: 00              NOP                         
2A1B: E1              POP     HL                  
2A1C: 00              NOP                         
2A1D: 00              NOP                         
2A1E: 00              NOP                         
2A1F: 00              NOP                         
2A20: 00              NOP                         
2A21: 00              NOP                         
2A22: C1              POP     BC                  
2A23: 00              NOP                         
2A24: 00              NOP                         
2A25: CF              RST     0X08                
2A26: 53              LD      D,E                 
2A27: E2 00 D2        JP      PO,$D200            
2A2A: E0              RET     PO                  
2A2B: 00              NOP                         
2A2C: 00              NOP                         
2A2D: D0              RET     NC                  
2A2E: 00              NOP                         
2A2F: 00              NOP                         
2A30: 00              NOP                         
2A31: 00              NOP                         
2A32: 00              NOP                         
2A33: DE 00           SBC     $00                 
2A35: CE 53           ADC     $53                 
2A37: E1              POP     HL                  
2A38: D1              POP     DE                  
2A39: E3              EX      (SP),HL             
2A3A: 00              NOP                         
2A3B: E1              POP     HL                  
2A3C: D3 00           OUT     ($00),A             ; {}
2A3E: 00              NOP                         
2A3F: 00              NOP                         
2A40: 00              NOP                         
2A41: 00              NOP                         
2A42: CF              RST     0X08                
2A43: C0              RET     NZ                  
2A44: DE DF           SBC     $DF                 
2A46: 53              LD      D,E                 
2A47: D3 E2           OUT     ($E2),A             ; {}
2A49: 00              NOP                         
2A4A: E2 D2 00        JP      PO,$00D2            ; {}
2A4D: 5E              LD      E,(HL)              
2A4E: E2 00 00        JP      PO,$0000            ; {}
2A51: 00              NOP                         
2A52: 00              NOP                         
2A53: CE C1           ADC     $C1                 
2A55: C2 DE D2        JP      NZ,$D2DE            
2A58: E1              POP     HL                  
2A59: E3              EX      (SP),HL             
2A5A: D1              POP     DE                  
2A5B: 00              NOP                         
2A5C: D2 00 00        JP      NC,$0000            ; {}
2A5F: 00              NOP                         
2A60: 00              NOP                         
2A61: 00              NOP                         
2A62: 00              NOP                         
2A63: 00              NOP                         
2A64: DF              RST     0X18                
2A65: DE C2           SBC     $C2                 
2A67: CF              RST     0X08                
2A68: E0              RET     PO                  
2A69: D0              RET     NC                  
2A6A: E2 E1 C2        JP      PO,$C2E1            
2A6D: C3 00 00        JP      $0000               ; {}
2A70: DF              RST     0X18                
2A71: DE CF           SBC     $CF                 
2A73: CE DF           ADC     $DF                 
2A75: DE CF           SBC     $CF                 
2A77: C8              RET     Z                   
2A78: D8              RET     C                   
2A79: 5E              LD      E,(HL)              
2A7A: CE 00           ADC     $00                 
2A7C: CF              RST     0X08                
2A7D: DE DF           SBC     $DF                 
2A7F: CE E0           ADC     $E0                 
2A81: E3              EX      (SP),HL             
2A82: E2 E1 00        JP      PO,$00E1            ; {}
2A85: E0              RET     PO                  
2A86: D1              POP     DE                  
2A87: CA DA D1        JP      Z,$D1DA             
2A8A: D2 D3 D0        JP      NC,$D0D3            
2A8D: D1              POP     DE                  
2A8E: D2 D3 00        JP      NC,$00D3            ; {}
2A91: 00              NOP                         
2A92: 00              NOP                         
2A93: 00              NOP                         
2A94: E3              EX      (SP),HL             
2A95: D2 CE D2        JP      NC,$D2CE            
2A98: E2 E0 D3        JP      PO,$D3E0            
2A9B: D1              POP     DE                  
2A9C: D3 00           OUT     ($00),A             ; {}
2A9E: 00              NOP                         
2A9F: 00              NOP                         
2AA0: 00              NOP                         
2AA1: 00              NOP                         
2AA2: 00              NOP                         
2AA3: E2 D3 CF        JP      PO,$CFD3            
2AA6: DF              RST     0X18                
2AA7: E1              POP     HL                  
2AA8: D0              RET     NC                  
2AA9: E3              EX      (SP),HL             
2AAA: E1              POP     HL                  
2AAB: D2 00 00        JP      NC,$0000            ; {}
2AAE: 00              NOP                         
2AAF: 00              NOP                         
2AB0: 00              NOP                         
2AB1: 00              NOP                         
2AB2: E1              POP     HL                  
2AB3: D0              RET     NC                  
2AB4: DE 00           SBC     $00                 
2AB6: DE E2           SBC     $E2                 
2AB8: 00              NOP                         
2AB9: D3 53           OUT     ($53),A             ; {}
2ABB: E2 5E C1        JP      PO,$C15E            
2ABE: C0              RET     NZ                  
2ABF: 00              NOP                         
2AC0: 00              NOP                         
2AC1: 00              NOP                         
2AC2: 00              NOP                         
2AC3: DF              RST     0X18                
2AC4: 00              NOP                         
2AC5: 00              NOP                         
2AC6: CF              RST     0X08                
2AC7: 5E              LD      E,(HL)              
2AC8: D1              POP     DE                  
2AC9: D2 00 53        JP      NC,$5300            
2ACC: E3              EX      (SP),HL             
2ACD: 00              NOP                         
2ACE: 00              NOP                         
2ACF: 00              NOP                         
2AD0: 00              NOP                         
2AD1: 00              NOP                         
2AD2: CE 00           ADC     $00                 
2AD4: CF              RST     0X08                
2AD5: 00              NOP                         
2AD6: CE D2           ADC     $D2                 
2AD8: D2 00 53        JP      NC,$5300            
2ADB: 00              NOP                         
2ADC: 5E              LD      E,(HL)              
2ADD: E0              RET     PO                  
2ADE: 00              NOP                         
2ADF: 00              NOP                         
2AE0: 00              NOP                         
2AE1: 00              NOP                         
2AE2: 00              NOP                         
2AE3: 00              NOP                         
2AE4: 00              NOP                         
2AE5: DE 00           SBC     $00                 
2AE7: E1              POP     HL                  
2AE8: D3 00           OUT     ($00),A             ; {}
2AEA: E2 00 00        JP      PO,$0000            ; {}
2AED: 00              NOP                         
2AEE: 00              NOP                         
2AEF: 00              NOP                         
2AF0: 00              NOP                         
2AF1: 00              NOP                         
2AF2: 00              NOP                         
2AF3: 00              NOP                         
2AF4: 00              NOP                         
2AF5: 00              NOP                         
2AF6: 00              NOP                         
2AF7: 5E              LD      E,(HL)              
2AF8: D0              RET     NC                  
2AF9: 00              NOP                         
2AFA: 00              NOP                         
2AFB: 00              NOP                         
2AFC: 00              NOP                         
2AFD: 00              NOP                         
2AFE: 00              NOP                         
2AFF: 00              NOP                         
2B00: 00              NOP                         
2B01: 00              NOP                         
2B02: 00              NOP                         
2B03: 00              NOP                         
2B04: 00              NOP                         
2B05: 00              NOP                         
2B06: 00              NOP                         
2B07: 00              NOP                         
2B08: 00              NOP                         
2B09: 00              NOP                         
2B0A: 80              ADD     A,B                 
2B0B: 01 40 02        LD      BC,$0240            
2B0E: 80              ADD     A,B                 
2B0F: 05              DEC     B                   
2B10: A0              AND     B                   
2B11: 01 40 02        LD      BC,$0240            
2B14: 00              NOP                         
2B15: 01 00 00        LD      BC,$0000            
2B18: 00              NOP                         
2B19: 00              NOP                         
2B1A: 00              NOP                         
2B1B: 00              NOP                         
2B1C: 00              NOP                         
2B1D: 00              NOP                         
2B1E: 00              NOP                         
2B1F: 00              NOP                         
2B20: 00              NOP                         
2B21: 00              NOP                         
2B22: 00              NOP                         
2B23: 00              NOP                         
2B24: 00              NOP                         
2B25: 00              NOP                         
2B26: 80              ADD     A,B                 
2B27: 00              NOP                         
2B28: 00              NOP                         
2B29: 01 20 04        LD      BC,$0420            
2B2C: 00              NOP                         
2B2D: 01 40 12        LD      BC,$1240            
2B30: 48              LD      C,B                 
2B31: 02              LD      (BC),A              
2B32: 80              ADD     A,B                 
2B33: 01 20 04        LD      BC,$0420            
2B36: 00              NOP                         
2B37: 00              NOP                         
2B38: 00              NOP                         
2B39: 01 00 00        LD      BC,$0000            
2B3C: 00              NOP                         
2B3D: 00              NOP                         
2B3E: 00              NOP                         
2B3F: 00              NOP                         
2B40: 00              NOP                         
2B41: 00              NOP                         
2B42: 00              NOP                         
2B43: 00              NOP                         
2B44: 80              ADD     A,B                 
2B45: 00              NOP                         
2B46: 00              NOP                         
2B47: 02              LD      (BC),A              
2B48: 10 08           DJNZ    $2B52               ; {}
2B4A: 00              NOP                         
2B4B: 01 80 04        LD      BC,$0480            
2B4E: A0              AND     B                   
2B4F: 21 84 05        LD      HL,$0584            
2B52: 20 02           JR      NZ,$2B56            ; {}
2B54: 80              ADD     A,B                 
2B55: 01 10 08        LD      BC,$0810            
2B58: 00              NOP                         
2B59: 00              NOP                         
2B5A: 00              NOP                         
2B5B: 01 00 00        LD      BC,$0000            
2B5E: 00              NOP                         
2B5F: 00              NOP                         
2B60: 00              NOP                         
2B61: 00              NOP                         
2B62: 80              ADD     A,B                 
2B63: 00              NOP                         
2B64: 00              NOP                         
2B65: 04              INC     B                   
2B66: 08              EX      AF,AF'              
2B67: 10 00           DJNZ    $2B69               ; {}
2B69: 01 40 00        LD      BC,$0040            
2B6C: 40              LD      B,B                 
2B6D: 0A              LD      A,(BC)              
2B6E: 10 40           DJNZ    $2BB0               ; {}
2B70: 02              LD      (BC),A              
2B71: 08              EX      AF,AF'              
2B72: 40              LD      B,B                 
2B73: 00              NOP                         
2B74: 10 04           DJNZ    $2B7A               ; {}
2B76: 80              ADD     A,B                 
2B77: 02              LD      (BC),A              
2B78: 08              EX      AF,AF'              
2B79: 10 00           DJNZ    $2B7B               ; {}
2B7B: 00              NOP                         
2B7C: 00              NOP                         
2B7D: 01 00 00        LD      BC,$0000            
2B80: 80              ADD     A,B                 
2B81: 00              NOP                         
2B82: 00              NOP                         
2B83: 08              EX      AF,AF'              
2B84: 04              INC     B                   
2B85: 20 00           JR      NZ,$2B87            ; {}
2B87: 02              LD      (BC),A              
2B88: 20 00           JR      NZ,$2B8A            ; {}
2B8A: 20 14           JR      NZ,$2BA0            ; {}
2B8C: 00              NOP                         
2B8D: 01 08 80        LD      BC,$8008            
2B90: 01 10 80        LD      BC,$8010            
2B93: 02              LD      (BC),A              
2B94: 20 00           JR      NZ,$2B96            ; {}
2B96: 08              EX      AF,AF'              
2B97: 04              INC     B                   
2B98: 80              ADD     A,B                 
2B99: 02              LD      (BC),A              
2B9A: 04              INC     B                   
2B9B: 20 00           JR      NZ,$2B9D            ; {}
2B9D: 00              NOP                         
2B9E: 00              NOP                         
2B9F: 01 01 01        LD      BC,$0101            
2BA2: 01 01 01        LD      BC,$0101            
2BA5: 04              INC     B                   
2BA6: 20 00           JR      NZ,$2BA8            ; {}
2BA8: 10 28           DJNZ    $2BD2               ; {}
2BAA: 80              ADD     A,B                 
2BAB: 02              LD      (BC),A              
2BAC: 04              INC     B                   
2BAD: 00              NOP                         
2BAE: 00              NOP                         
2BAF: 04              INC     B                   
2BB0: 20 20           JR      NZ,$2BD2            ; {}
2BB2: 00              NOP                         
2BB3: 04              INC     B                   
2BB4: 40              LD      B,B                 
2BB5: 01 10 00        LD      BC,$0010            
2BB8: 04              INC     B                   
2BB9: 08              EX      AF,AF'              
2BBA: 80              ADD     A,B                 
2BBB: 04              INC     B                   
2BBC: 00              NOP                         
2BBD: 00              NOP                         
2BBE: 00              NOP                         
2BBF: 00              NOP                         
2BC0: 00              NOP                         
2BC1: 00              NOP                         
2BC2: 00              NOP                         
2BC3: 08              EX      AF,AF'              
2BC4: 20 00           JR      NZ,$2BC6            ; {}
2BC6: 88              ADC     A,B                 
2BC7: 10 00           DJNZ    $2BC9               ; {}
2BC9: 44              LD      B,H                 
2BCA: 00              NOP                         
2BCB: 00              NOP                         
2BCC: 00              NOP                         
2BCD: 10 02           DJNZ    $2BD1               ; {}
2BCF: 00              NOP                         
2BD0: 08              EX      AF,AF'              
2BD1: 40              LD      B,B                 
2BD2: 00              NOP                         
2BD3: 00              NOP                         
2BD4: 00              NOP                         
2BD5: 08              EX      AF,AF'              
2BD6: 40              LD      B,B                 
2BD7: 00              NOP                         
2BD8: 08              EX      AF,AF'              
2BD9: 01 00 10        LD      BC,$1000            
2BDC: 80              ADD     A,B                 
2BDD: 04              INC     B                   
2BDE: 00              NOP                         
2BDF: 00              NOP                         
2BE0: 00              NOP                         
2BE1: 00              NOP                         
2BE2: 20 00           JR      NZ,$2BE4            ; {}
2BE4: 84              ADD     A,H                 
2BE5: 20 00           JR      NZ,$2BE7            ; {}
2BE7: 08              EX      AF,AF'              
2BE8: 00              NOP                         
2BE9: 00              NOP                         
2BEA: 00              NOP                         
2BEB: 00              NOP                         
2BEC: 00              NOP                         
2BED: 20 01           JR      NZ,$2BF0            ; {}
2BEF: 00              NOP                         
2BF0: 04              INC     B                   
2BF1: 80              ADD     A,B                 
2BF2: 00              NOP                         
2BF3: 00              NOP                         
2BF4: 00              NOP                         
2BF5: 00              NOP                         
2BF6: 00              NOP                         
2BF7: 10 40           DJNZ    $2C39               ; {}
2BF9: 00              NOP                         
2BFA: 04              INC     B                   
2BFB: 01 00 00        LD      BC,$0000            
2BFE: 80              ADD     A,B                 
2BFF: 00              NOP                         
2C00: 0B              DEC     BC                  
2C01: 0C              INC     C                   
2C02: 0D              DEC     C                   
2C03: 0E 0B           LD      C,$0B               
2C05: 0C              INC     C                   
2C06: 0A              LD      A,(BC)              
2C07: 0A              LD      A,(BC)              
2C08: 0A              LD      A,(BC)              
2C09: 0A              LD      A,(BC)              
2C0A: 0A              LD      A,(BC)              
2C0B: 0A              LD      A,(BC)              
2C0C: 0A              LD      A,(BC)              
2C0D: 06 06           LD      B,$06               
2C0F: 1E 03           LD      E,$03               
2C11: 03              INC     BC                  
2C12: 1F              RRA                         
2C13: 05              DEC     B                   
2C14: 05              DEC     B                   
2C15: 1C              INC     E                   
2C16: 04              INC     B                   
2C17: 04              INC     B                   
2C18: 04              INC     B                   
2C19: 1D              DEC     E                   
2C1A: 06 06           LD      B,$06               
2C1C: 1A              LD      A,(DE)              
2C1D: 04              INC     B                   
2C1E: 04              INC     B                   
2C1F: 04              INC     B                   
2C20: 1B              DEC     DE                  
2C21: 05              DEC     B                   
2C22: 05              DEC     B                   
2C23: 05              DEC     B                   
2C24: 05              DEC     B                   
2C25: 18 1F           JR      $2C46               ; {}
2C27: 07              RLCA                        
2C28: 07              RLCA                        
2C29: 07              RLCA                        
2C2A: 07              RLCA                        
2C2B: 07              RLCA                        
2C2C: 07              RLCA                        
2C2D: 07              RLCA                        
2C2E: 07              RLCA                        
2C2F: 07              RLCA                        
2C30: 00              NOP                         
2C31: FF              RST     0X38                
2C32: FF              RST     0X38                
2C33: FF              RST     0X38                
2C34: 05              DEC     B                   
2C35: 05              DEC     B                   
2C36: 1C              INC     E                   
2C37: 04              INC     B                   
2C38: 1D              DEC     E                   
2C39: 0A              LD      A,(BC)              
2C3A: 0A              LD      A,(BC)              
2C3B: 0A              LD      A,(BC)              
2C3C: 0A              LD      A,(BC)              
2C3D: 0A              LD      A,(BC)              
2C3E: 0A              LD      A,(BC)              
2C3F: 06 06           LD      B,$06               
2C41: 1E 03           LD      E,$03               
2C43: 03              INC     BC                  
2C44: 1F              RRA                         
2C45: 05              DEC     B                   
2C46: 1C              INC     E                   
2C47: 04              INC     B                   
2C48: 04              INC     B                   
2C49: 1D              DEC     E                   
2C4A: 0A              LD      A,(BC)              
2C4B: 06 06           LD      B,$06               
2C4D: 1E 03           LD      E,$03               
2C4F: 03              INC     BC                  
2C50: 1F              RRA                         
2C51: 05              DEC     B                   
2C52: 1C              INC     E                   
2C53: 04              INC     B                   
2C54: 04              INC     B                   
2C55: 1D              DEC     E                   
2C56: 0A              LD      A,(BC)              
2C57: 06 06           LD      B,$06               
2C59: 1E 03           LD      E,$03               
2C5B: 03              INC     BC                  
2C5C: 1F              RRA                         
2C5D: 05              DEC     B                   
2C5E: 1C              INC     E                   
2C5F: 04              INC     B                   
2C60: 04              INC     B                   
2C61: 1D              DEC     E                   
2C62: 0A              LD      A,(BC)              
2C63: 06 1E           LD      B,$1E               
2C65: 03              INC     BC                  
2C66: 1F              RRA                         
2C67: 05              DEC     B                   
2C68: 1C              INC     E                   
2C69: 04              INC     B                   
2C6A: 1D              DEC     E                   
2C6B: 06 1E           LD      B,$1E               
2C6D: 03              INC     BC                  
2C6E: 03              INC     BC                  
2C6F: 03              INC     BC                  
2C70: 03              INC     BC                  
2C71: 15              DEC     D                   
2C72: 16 17           LD      D,$17               
2C74: 01 01 05        LD      BC,$0501            
2C77: 05              DEC     B                   
2C78: 01 01 05        LD      BC,$0501            
2C7B: 05              DEC     B                   
2C7C: 01 01 05        LD      BC,$0501            
2C7F: 05              DEC     B                   
2C80: 01 01 05        LD      BC,$0501            
2C83: 05              DEC     B                   
2C84: 02              LD      (BC),A              
2C85: 02              LD      (BC),A              
2C86: 18 07           JR      $2C8F               ; {}
2C88: 07              RLCA                        
2C89: 07              RLCA                        
2C8A: 00              NOP                         
2C8B: FF              RST     0X38                
2C8C: FF              RST     0X38                
2C8D: FF              RST     0X38                
2C8E: FF              RST     0X38                
2C8F: FF              RST     0X38                
2C90: 1C              INC     E                   
2C91: 04              INC     B                   
2C92: 04              INC     B                   
2C93: 04              INC     B                   
2C94: 04              INC     B                   
2C95: 04              INC     B                   
2C96: 04              INC     B                   
2C97: 04              INC     B                   
2C98: 04              INC     B                   
2C99: 04              INC     B                   
2C9A: 04              INC     B                   
2C9B: 04              INC     B                   
2C9C: 04              INC     B                   
2C9D: 04              INC     B                   
2C9E: 04              INC     B                   
2C9F: 1D              DEC     E                   
2CA0: 06 06           LD      B,$06               
2CA2: 06 06           LD      B,$06               
2CA4: 06 06           LD      B,$06               
2CA6: 06 1E           LD      B,$1E               
2CA8: 03              INC     BC                  
2CA9: 03              INC     BC                  
2CAA: 03              INC     BC                  
2CAB: 03              INC     BC                  
2CAC: 03              INC     BC                  
2CAD: 03              INC     BC                  
2CAE: 1F              RRA                         
2CAF: 05              DEC     B                   
2CB0: 05              DEC     B                   
2CB1: 05              DEC     B                   
2CB2: 05              DEC     B                   
2CB3: 1C              INC     E                   
2CB4: 04              INC     B                   
2CB5: 04              INC     B                   
2CB6: 1D              DEC     E                   
2CB7: 06 09           LD      B,$09               
2CB9: 09              ADD     HL,BC               
2CBA: 09              ADD     HL,BC               
2CBB: 1E 03           LD      E,$03               
2CBD: 07              RLCA                        
2CBE: 07              RLCA                        
2CBF: 08              EX      AF,AF'              
2CC0: 08              EX      AF,AF'              
2CC1: 07              RLCA                        
2CC2: 07              RLCA                        
2CC3: 08              EX      AF,AF'              
2CC4: 07              RLCA                        
2CC5: 00              NOP                         
2CC6: FF              RST     0X38                
2CC7: FF              RST     0X38                
2CC8: 05              DEC     B                   
2CC9: 05              DEC     B                   
2CCA: 05              DEC     B                   
2CCB: 05              DEC     B                   
2CCC: 1C              INC     E                   
2CCD: 04              INC     B                   
2CCE: 04              INC     B                   
2CCF: 04              INC     B                   
2CD0: 04              INC     B                   
2CD1: 04              INC     B                   
2CD2: 04              INC     B                   
2CD3: 04              INC     B                   
2CD4: 04              INC     B                   
2CD5: 04              INC     B                   
2CD6: 04              INC     B                   
2CD7: 04              INC     B                   
2CD8: 04              INC     B                   
2CD9: 04              INC     B                   
2CDA: 04              INC     B                   
2CDB: 1D              DEC     E                   
2CDC: 09              ADD     HL,BC               
2CDD: 09              ADD     HL,BC               
2CDE: 09              ADD     HL,BC               
2CDF: 09              ADD     HL,BC               
2CE0: 0A              LD      A,(BC)              
2CE1: 0A              LD      A,(BC)              
2CE2: 0A              LD      A,(BC)              
2CE3: 09              ADD     HL,BC               
2CE4: 0A              LD      A,(BC)              
2CE5: 0A              LD      A,(BC)              
2CE6: 06 1E           LD      B,$1E               
2CE8: 03              INC     BC                  
2CE9: 03              INC     BC                  
2CEA: 03              INC     BC                  
2CEB: 1F              RRA                         
2CEC: 05              DEC     B                   
2CED: 05              DEC     B                   
2CEE: 18 03           JR      $2CF3               ; {}
2CF0: 19              ADD     HL,DE               
2CF1: 06 06           LD      B,$06               
2CF3: 1E 03           LD      E,$03               
2CF5: 03              INC     BC                  
2CF6: 1F              RRA                         
2CF7: 05              DEC     B                   
2CF8: 05              DEC     B                   
2CF9: 05              DEC     B                   
2CFA: 05              DEC     B                   
2CFB: 05              DEC     B                   
2CFC: 05              DEC     B                   
2CFD: 05              DEC     B                   
2CFE: 00              NOP                         
2CFF: FF              RST     0X38                
2D00: 0B              DEC     BC                  
2D01: 0C              INC     C                   
2D02: 0D              DEC     C                   
2D03: 0E 0B           LD      C,$0B               
2D05: 0C              INC     C                   
2D06: 06 1E           LD      B,$1E               
2D08: 03              INC     BC                  
2D09: 03              INC     BC                  
2D0A: 03              INC     BC                  
2D0B: 03              INC     BC                  
2D0C: 03              INC     BC                  
2D0D: 03              INC     BC                  
2D0E: 03              INC     BC                  
2D0F: 03              INC     BC                  
2D10: 03              INC     BC                  
2D11: 03              INC     BC                  
2D12: 03              INC     BC                  
2D13: 03              INC     BC                  
2D14: 03              INC     BC                  
2D15: 03              INC     BC                  
2D16: 1F              RRA                         
2D17: 05              DEC     B                   
2D18: 05              DEC     B                   
2D19: 1C              INC     E                   
2D1A: 04              INC     B                   
2D1B: 04              INC     B                   
2D1C: 04              INC     B                   
2D1D: 04              INC     B                   
2D1E: 04              INC     B                   
2D1F: 04              INC     B                   
2D20: 04              INC     B                   
2D21: 04              INC     B                   
2D22: 04              INC     B                   
2D23: 04              INC     B                   
2D24: 1D              DEC     E                   
2D25: 06 06           LD      B,$06               
2D27: 1E 03           LD      E,$03               
2D29: 03              INC     BC                  
2D2A: 03              INC     BC                  
2D2B: 03              INC     BC                  
2D2C: 03              INC     BC                  
2D2D: 03              INC     BC                  
2D2E: 1F              RRA                         
2D2F: 05              DEC     B                   
2D30: 05              DEC     B                   
2D31: 05              DEC     B                   
2D32: 05              DEC     B                   
2D33: 05              DEC     B                   
2D34: 1C              INC     E                   
2D35: 04              INC     B                   
2D36: 04              INC     B                   
2D37: 04              INC     B                   
2D38: 04              INC     B                   
2D39: 04              INC     B                   
2D3A: 04              INC     B                   
2D3B: 04              INC     B                   
2D3C: 04              INC     B                   
2D3D: 04              INC     B                   
2D3E: 04              INC     B                   
2D3F: 1B              DEC     DE                  
2D40: 00              NOP                         
2D41: FF              RST     0X38                
2D42: FF              RST     0X38                
2D43: FF              RST     0X38                
2D44: 05              DEC     B                   
2D45: 05              DEC     B                   
2D46: 05              DEC     B                   
2D47: 18 03           JR      $2D4C               ; {}
2D49: 03              INC     BC                  
2D4A: 03              INC     BC                  
2D4B: 03              INC     BC                  
2D4C: 03              INC     BC                  
2D4D: 03              INC     BC                  
2D4E: 03              INC     BC                  
2D4F: 03              INC     BC                  
2D50: 03              INC     BC                  
2D51: 19              ADD     HL,DE               
2D52: 06 06           LD      B,$06               
2D54: 1A              LD      A,(DE)              
2D55: 04              INC     B                   
2D56: 04              INC     B                   
2D57: 1B              DEC     DE                  
2D58: 05              DEC     B                   
2D59: 05              DEC     B                   
2D5A: 18 03           JR      $2D5F               ; {}
2D5C: 03              INC     BC                  
2D5D: 03              INC     BC                  
2D5E: 03              INC     BC                  
2D5F: 03              INC     BC                  
2D60: 03              INC     BC                  
2D61: 03              INC     BC                  
2D62: 19              ADD     HL,DE               
2D63: 06 06           LD      B,$06               
2D65: 06 06           LD      B,$06               
2D67: 06 06           LD      B,$06               
2D69: 06 06           LD      B,$06               
2D6B: 06 06           LD      B,$06               
2D6D: 1A              LD      A,(DE)              
2D6E: 04              INC     B                   
2D6F: 04              INC     B                   
2D70: 1B              DEC     DE                  
2D71: 05              DEC     B                   
2D72: 05              DEC     B                   
2D73: 1C              INC     E                   
2D74: 04              INC     B                   
2D75: 04              INC     B                   
2D76: 1D              DEC     E                   
2D77: 06 06           LD      B,$06               
2D79: 1A              LD      A,(DE)              
2D7A: 04              INC     B                   
2D7B: 04              INC     B                   
2D7C: 1B              DEC     DE                  
2D7D: 05              DEC     B                   
2D7E: 05              DEC     B                   
2D7F: 05              DEC     B                   
2D80: 05              DEC     B                   
2D81: 05              DEC     B                   
2D82: 05              DEC     B                   
2D83: 05              DEC     B                   
2D84: 00              NOP                         
2D85: FF              RST     0X38                
2D86: FF              RST     0X38                
2D87: FF              RST     0X38                
2D88: 1C              INC     E                   
2D89: 04              INC     B                   
2D8A: 04              INC     B                   
2D8B: 1D              DEC     E                   
2D8C: 06 06           LD      B,$06               
2D8E: 09              ADD     HL,BC               
2D8F: 0A              LD      A,(BC)              
2D90: 0A              LD      A,(BC)              
2D91: 09              ADD     HL,BC               
2D92: 09              ADD     HL,BC               
2D93: 09              ADD     HL,BC               
2D94: 16 17           LD      D,$17               
2D96: 14              INC     D                   
2D97: 03              INC     BC                  
2D98: 03              INC     BC                  
2D99: 03              INC     BC                  
2D9A: 1F              RRA                         
2D9B: 05              DEC     B                   
2D9C: 05              DEC     B                   
2D9D: 1C              INC     E                   
2D9E: 04              INC     B                   
2D9F: 04              INC     B                   
2DA0: 1D              DEC     E                   
2DA1: 06 06           LD      B,$06               
2DA3: 1E 03           LD      E,$03               
2DA5: 03              INC     BC                  
2DA6: 03              INC     BC                  
2DA7: 03              INC     BC                  
2DA8: 07              RLCA                        
2DA9: 07              RLCA                        
2DAA: 08              EX      AF,AF'              
2DAB: 08              EX      AF,AF'              
2DAC: 07              RLCA                        
2DAD: 07              RLCA                        
2DAE: 05              DEC     B                   
2DAF: 05              DEC     B                   
2DB0: 1C              INC     E                   
2DB1: 04              INC     B                   
2DB2: 04              INC     B                   
2DB3: 04              INC     B                   
2DB4: 04              INC     B                   
2DB5: 04              INC     B                   
2DB6: 04              INC     B                   
2DB7: 04              INC     B                   
2DB8: 1D              DEC     E                   
2DB9: 1A              LD      A,(DE)              
2DBA: 04              INC     B                   
2DBB: 1B              DEC     DE                  
2DBC: 00              NOP                         
2DBD: FF              RST     0X38                
2DBE: FF              RST     0X38                
2DBF: FF              RST     0X38                
2DC0: 14              INC     D                   
2DC1: 03              INC     BC                  
2DC2: 03              INC     BC                  
2DC3: 19              ADD     HL,DE               
2DC4: 06 0A           LD      B,$0A               
2DC6: 0A              LD      A,(BC)              
2DC7: 09              ADD     HL,BC               
2DC8: 09              ADD     HL,BC               
2DC9: 09              ADD     HL,BC               
2DCA: 0A              LD      A,(BC)              
2DCB: 12              LD      (DE),A              
2DCC: 13              INC     DE                  
2DCD: 10 11           DJNZ    $2DE0               ; {}
2DCF: 12              LD      (DE),A              
2DD0: 13              INC     DE                  
2DD1: 10 11           DJNZ    $2DE4               ; {}
2DD3: 12              LD      (DE),A              
2DD4: 13              INC     DE                  
2DD5: 10 04           DJNZ    $2DDB               ; {}
2DD7: 04              INC     B                   
2DD8: 04              INC     B                   
2DD9: 04              INC     B                   
2DDA: 1B              DEC     DE                  
2DDB: 05              DEC     B                   
2DDC: 18 03           JR      $2DE1               ; {}
2DDE: 19              ADD     HL,DE               
2DDF: 06 1A           LD      B,$1A               
2DE1: 04              INC     B                   
2DE2: 1B              DEC     DE                  
2DE3: 05              DEC     B                   
2DE4: 18 07           JR      $2DED               ; {}
2DE6: 07              RLCA                        
2DE7: 07              RLCA                        
2DE8: 08              EX      AF,AF'              
2DE9: 08              EX      AF,AF'              
2DEA: 07              RLCA                        
2DEB: 07              RLCA                        
2DEC: 07              RLCA                        
2DED: 03              INC     BC                  
2DEE: 03              INC     BC                  
2DEF: 19              ADD     HL,DE               
2DF0: 0D              DEC     C                   
2DF1: 0E 00           LD      C,$00               
2DF3: FF              RST     0X38                
2DF4: FF              RST     0X38                
2DF5: FF              RST     0X38                
2DF6: FF              RST     0X38                
2DF7: FF              RST     0X38                
2DF8: FF              RST     0X38                
2DF9: FF              RST     0X38                
2DFA: FF              RST     0X38                
2DFB: FF              RST     0X38                
2DFC: FF              RST     0X38                
2DFD: FF              RST     0X38                
2DFE: FF              RST     0X38                
2DFF: FF              RST     0X38                
2E00: 0B              DEC     BC                  
2E01: 0C              INC     C                   
2E02: 0D              DEC     C                   
2E03: 0E 02           LD      C,$02               
2E05: 02              LD      (BC),A              
2E06: 02              LD      (BC),A              
2E07: 02              LD      (BC),A              
2E08: 0B              DEC     BC                  
2E09: 0C              INC     C                   
2E0A: 0D              DEC     C                   
2E0B: 0E 01           LD      C,$01               
2E0D: 01 14 15        LD      BC,$1514            
2E10: 16 17           LD      D,$17               
2E12: 01 01 05        LD      BC,$0501            
2E15: 05              DEC     B                   
2E16: 05              DEC     B                   
2E17: 05              DEC     B                   
2E18: 02              LD      (BC),A              
2E19: 02              LD      (BC),A              
2E1A: 02              LD      (BC),A              
2E1B: 02              LD      (BC),A              
2E1C: 00              NOP                         
2E1D: FF              RST     0X38                
2E1E: FF              RST     0X38                
2E1F: FF              RST     0X38                
2E20: 0B              DEC     BC                  
2E21: 0C              INC     C                   
2E22: 0D              DEC     C                   
2E23: 0E 0B           LD      C,$0B               
2E25: 0C              INC     C                   
2E26: 0D              DEC     C                   
2E27: 0E 02           LD      C,$02               
2E29: 02              LD      (BC),A              
2E2A: 02              LD      (BC),A              
2E2B: 02              LD      (BC),A              
2E2C: 02              LD      (BC),A              
2E2D: 02              LD      (BC),A              
2E2E: 02              LD      (BC),A              
2E2F: 02              LD      (BC),A              
2E30: 05              DEC     B                   
2E31: 05              DEC     B                   
2E32: 01 05 05        LD      BC,$0505            
2E35: 01 05 05        LD      BC,$0505            
2E38: 01 05 05        LD      BC,$0505            
2E3B: 01 00 FF        LD      BC,$FF00            
2E3E: FF              RST     0X38                
2E3F: FF              RST     0X38                
2E40: 0B              DEC     BC                  
2E41: 0C              INC     C                   
2E42: 0D              DEC     C                   
2E43: 0E 01           LD      C,$01               
2E45: 01 01 18        LD      BC,$1801            
2E48: 03              INC     BC                  
2E49: 19              ADD     HL,DE               
2E4A: 06 06           LD      B,$06               
2E4C: 1A              LD      A,(DE)              
2E4D: 04              INC     B                   
2E4E: 1B              DEC     DE                  
2E4F: 05              DEC     B                   
2E50: 18 03           JR      $2E55               ; {}
2E52: 19              ADD     HL,DE               
2E53: 06 06           LD      B,$06               
2E55: 1A              LD      A,(DE)              
2E56: 04              INC     B                   
2E57: 04              INC     B                   
2E58: 04              INC     B                   
2E59: 04              INC     B                   
2E5A: 04              INC     B                   
2E5B: 04              INC     B                   
2E5C: 04              INC     B                   
2E5D: 04              INC     B                   
2E5E: 04              INC     B                   
2E5F: 1B              DEC     DE                  
2E60: 05              DEC     B                   
2E61: 05              DEC     B                   
2E62: 05              DEC     B                   
2E63: 01 01 01        LD      BC,$0101            
2E66: 01 01 00        LD      BC,$0001            
2E69: FF              RST     0X38                
2E6A: FF              RST     0X38                
2E6B: FF              RST     0X38                
2E6C: 0B              DEC     BC                  
2E6D: 0C              INC     C                   
2E6E: 0D              DEC     C                   
2E6F: 0E 01           LD      C,$01               
2E71: 01 0B 0C        LD      BC,$0C0B            
2E74: 0D              DEC     C                   
2E75: 0E 01           LD      C,$01               
2E77: 01 05 05        LD      BC,$0505            
2E7A: 05              DEC     B                   
2E7B: 05              DEC     B                   
2E7C: 01 01 0B        LD      BC,$0B01            
2E7F: 0C              INC     C                   
2E80: 0D              DEC     C                   
2E81: 0E 01           LD      C,$01               
2E83: 01 07 08        LD      BC,$0807            
2E86: 08              EX      AF,AF'              
2E87: 07              RLCA                        
2E88: 08              EX      AF,AF'              
2E89: 08              EX      AF,AF'              
2E8A: 08              EX      AF,AF'              
2E8B: 07              RLCA                        
2E8C: 00              NOP                         
2E8D: FF              RST     0X38                
2E8E: FF              RST     0X38                
2E8F: FF              RST     0X38                
2E90: 14              INC     D                   
2E91: 15              DEC     D                   
2E92: 16 17           LD      D,$17               
2E94: 14              INC     D                   
2E95: 15              DEC     D                   
2E96: 16 17           LD      D,$17               
2E98: 14              INC     D                   
2E99: 03              INC     BC                  
2E9A: 03              INC     BC                  
2E9B: 03              INC     BC                  
2E9C: 03              INC     BC                  
2E9D: 03              INC     BC                  
2E9E: 03              INC     BC                  
2E9F: 03              INC     BC                  
2EA0: 03              INC     BC                  
2EA1: 03              INC     BC                  
2EA2: 03              INC     BC                  
2EA3: 03              INC     BC                  
2EA4: 03              INC     BC                  
2EA5: 19              ADD     HL,DE               
2EA6: 09              ADD     HL,BC               
2EA7: 0A              LD      A,(BC)              
2EA8: 0A              LD      A,(BC)              
2EA9: 09              ADD     HL,BC               
2EAA: 09              ADD     HL,BC               
2EAB: 0A              LD      A,(BC)              
2EAC: 0A              LD      A,(BC)              
2EAD: 12              LD      (DE),A              
2EAE: 13              INC     DE                  
2EAF: 08              EX      AF,AF'              
2EB0: 08              EX      AF,AF'              
2EB1: 07              RLCA                        
2EB2: 07              RLCA                        
2EB3: 08              EX      AF,AF'              
2EB4: 08              EX      AF,AF'              
2EB5: 08              EX      AF,AF'              
2EB6: 08              EX      AF,AF'              
2EB7: 04              INC     B                   
2EB8: 04              INC     B                   
2EB9: 04              INC     B                   
2EBA: 11 12 13        LD      DE,$1312            
2EBD: 10 11           DJNZ    $2ED0               ; {}
2EBF: 12              LD      (DE),A              
2EC0: 13              INC     DE                  
2EC1: 00              NOP                         
2EC2: FF              RST     0X38                
2EC3: FF              RST     0X38                
2EC4: 10 11           DJNZ    $2ED7               ; {}
2EC6: 12              LD      (DE),A              
2EC7: 13              INC     DE                  
2EC8: 10 11           DJNZ    $2EDB               ; {}
2ECA: 12              LD      (DE),A              
2ECB: 13              INC     DE                  
2ECC: 10 04           DJNZ    $2ED2               ; {}
2ECE: 04              INC     B                   
2ECF: 04              INC     B                   
2ED0: 04              INC     B                   
2ED1: 04              INC     B                   
2ED2: 04              INC     B                   
2ED3: 04              INC     B                   
2ED4: 04              INC     B                   
2ED5: 04              INC     B                   
2ED6: 0A              LD      A,(BC)              
2ED7: 0A              LD      A,(BC)              
2ED8: 0A              LD      A,(BC)              
2ED9: 09              ADD     HL,BC               
2EDA: 0A              LD      A,(BC)              
2EDB: 09              ADD     HL,BC               
2EDC: 0A              LD      A,(BC)              
2EDD: 09              ADD     HL,BC               
2EDE: 16 17           LD      D,$17               
2EE0: 14              INC     D                   
2EE1: 03              INC     BC                  
2EE2: 03              INC     BC                  
2EE3: 03              INC     BC                  
2EE4: 07              RLCA                        
2EE5: 07              RLCA                        
2EE6: 07              RLCA                        
2EE7: 07              RLCA                        
2EE8: 03              INC     BC                  
2EE9: 19              ADD     HL,DE               
2EEA: 06 1A           LD      B,$1A               
2EEC: 04              INC     B                   
2EED: 1B              DEC     DE                  
2EEE: 05              DEC     B                   
2EEF: 18 07           JR      $2EF8               ; {}
2EF1: 07              RLCA                        
2EF2: 07              RLCA                        
2EF3: 07              RLCA                        
2EF4: 00              NOP                         
2EF5: FF              RST     0X38                
2EF6: FF              RST     0X38                
2EF7: FF              RST     0X38                
2EF8: FF              RST     0X38                
2EF9: FF              RST     0X38                
2EFA: FF              RST     0X38                
2EFB: FF              RST     0X38                
2EFC: FF              RST     0X38                
2EFD: FF              RST     0X38                
2EFE: FF              RST     0X38                
2EFF: FF              RST     0X38                
2F00: 05              DEC     B                   
2F01: 1C              INC     E                   
2F02: 04              INC     B                   
2F03: 1D              DEC     E                   
2F04: 06 06           LD      B,$06               
2F06: 06 06           LD      B,$06               
2F08: 06 09           LD      B,$09               
2F0A: 09              ADD     HL,BC               
2F0B: 09              ADD     HL,BC               
2F0C: 0A              LD      A,(BC)              
2F0D: 0A              LD      A,(BC)              
2F0E: 0A              LD      A,(BC)              
2F0F: 09              ADD     HL,BC               
2F10: 09              ADD     HL,BC               
2F11: 16 17           LD      D,$17               
2F13: 14              INC     D                   
2F14: 1F              RRA                         
2F15: 05              DEC     B                   
2F16: 18 03           JR      $2F1B               ; {}
2F18: 19              ADD     HL,DE               
2F19: 06 1E           LD      B,$1E               
2F1B: 03              INC     BC                  
2F1C: 1F              RRA                         
2F1D: 05              DEC     B                   
2F1E: 18 03           JR      $2F23               ; {}
2F20: 19              ADD     HL,DE               
2F21: 06 1E           LD      B,$1E               
2F23: 03              INC     BC                  
2F24: 1F              RRA                         
2F25: 05              DEC     B                   
2F26: 05              DEC     B                   
2F27: 1C              INC     E                   
2F28: 08              EX      AF,AF'              
2F29: 08              EX      AF,AF'              
2F2A: 08              EX      AF,AF'              
2F2B: 08              EX      AF,AF'              
2F2C: 08              EX      AF,AF'              
2F2D: 08              EX      AF,AF'              
2F2E: 08              EX      AF,AF'              
2F2F: 08              EX      AF,AF'              
2F30: 00              NOP                         
2F31: FF              RST     0X38                
2F32: FF              RST     0X38                
2F33: FF              RST     0X38                
2F34: 05              DEC     B                   
2F35: 18 03           JR      $2F3A               ; {}
2F37: 19              ADD     HL,DE               
2F38: 06 06           LD      B,$06               
2F3A: 06 06           LD      B,$06               
2F3C: 0A              LD      A,(BC)              
2F3D: 0A              LD      A,(BC)              
2F3E: 09              ADD     HL,BC               
2F3F: 09              ADD     HL,BC               
2F40: 0A              LD      A,(BC)              
2F41: 0A              LD      A,(BC)              
2F42: 09              ADD     HL,BC               
2F43: 0A              LD      A,(BC)              
2F44: 0A              LD      A,(BC)              
2F45: 12              LD      (DE),A              
2F46: 13              INC     DE                  
2F47: 10 1B           DJNZ    $2F64               ; {}
2F49: 05              DEC     B                   
2F4A: 1C              INC     E                   
2F4B: 04              INC     B                   
2F4C: 1D              DEC     E                   
2F4D: 1E 1F           LD      E,$1F               
2F4F: 1C              INC     E                   
2F50: 04              INC     B                   
2F51: 1D              DEC     E                   
2F52: 06 1A           LD      B,$1A               
2F54: 04              INC     B                   
2F55: 04              INC     B                   
2F56: 1B              DEC     DE                  
2F57: 05              DEC     B                   
2F58: 18 07           JR      $2F61               ; {}
2F5A: 07              RLCA                        
2F5B: 07              RLCA                        
2F5C: 07              RLCA                        
2F5D: 08              EX      AF,AF'              
2F5E: 07              RLCA                        
2F5F: 07              RLCA                        
2F60: 07              RLCA                        
2F61: 07              RLCA                        
2F62: 00              NOP                         
2F63: FF              RST     0X38                
2F64: 0B              DEC     BC                  
2F65: 0C              INC     C                   
2F66: 0D              DEC     C                   
2F67: 0E 0B           LD      C,$0B               
2F69: 0C              INC     C                   
2F6A: 1E 03           LD      E,$03               
2F6C: 19              ADD     HL,DE               
2F6D: 06 1E           LD      B,$1E               
2F6F: 03              INC     BC                  
2F70: 19              ADD     HL,DE               
2F71: 06 1E           LD      B,$1E               
2F73: 03              INC     BC                  
2F74: 19              ADD     HL,DE               
2F75: 06 1E           LD      B,$1E               
2F77: 1F              RRA                         
2F78: 1C              INC     E                   
2F79: 1D              DEC     E                   
2F7A: 1E 03           LD      E,$03               
2F7C: 03              INC     BC                  
2F7D: 03              INC     BC                  
2F7E: 1F              RRA                         
2F7F: 05              DEC     B                   
2F80: 18 03           JR      $2F85               ; {}
2F82: 19              ADD     HL,DE               
2F83: 06 1E           LD      B,$1E               
2F85: 03              INC     BC                  
2F86: 1F              RRA                         
2F87: 05              DEC     B                   
2F88: 08              EX      AF,AF'              
2F89: 08              EX      AF,AF'              
2F8A: 08              EX      AF,AF'              
2F8B: 08              EX      AF,AF'              
2F8C: 08              EX      AF,AF'              
2F8D: 08              EX      AF,AF'              
2F8E: 08              EX      AF,AF'              
2F8F: 07              RLCA                        
2F90: 07              RLCA                        
2F91: 08              EX      AF,AF'              
2F92: 08              EX      AF,AF'              
2F93: 08              EX      AF,AF'              
2F94: 08              EX      AF,AF'              
2F95: 08              EX      AF,AF'              
2F96: 00              NOP                         
2F97: FF              RST     0X38                
2F98: FF              RST     0X38                
2F99: FF              RST     0X38                
2F9A: FF              RST     0X38                
2F9B: FF              RST     0X38                
2F9C: FF              RST     0X38                
2F9D: FF              RST     0X38                
2F9E: FF              RST     0X38                
2F9F: FF              RST     0X38                
2FA0: 05              DEC     B                   
2FA1: 05              DEC     B                   
2FA2: 18 03           JR      $2FA7               ; {}
2FA4: 03              INC     BC                  
2FA5: 03              INC     BC                  
2FA6: 03              INC     BC                  
2FA7: 03              INC     BC                  
2FA8: 03              INC     BC                  
2FA9: 03              INC     BC                  
2FAA: 03              INC     BC                  
2FAB: 19              ADD     HL,DE               
2FAC: 06 06           LD      B,$06               
2FAE: 06 06           LD      B,$06               
2FB0: 06 06           LD      B,$06               
2FB2: 06 1A           LD      B,$1A               
2FB4: 04              INC     B                   
2FB5: 1B              DEC     DE                  
2FB6: 05              DEC     B                   
2FB7: 18 03           JR      $2FBC               ; {}
2FB9: 03              INC     BC                  
2FBA: 03              INC     BC                  
2FBB: 03              INC     BC                  
2FBC: 19              ADD     HL,DE               
2FBD: 06 06           LD      B,$06               
2FBF: 06 1A           LD      B,$1A               
2FC1: 04              INC     B                   
2FC2: 1B              DEC     DE                  
2FC3: 05              DEC     B                   
2FC4: 18 03           JR      $2FC9               ; {}
2FC6: 03              INC     BC                  
2FC7: 03              INC     BC                  
2FC8: 03              INC     BC                  
2FC9: 19              ADD     HL,DE               
2FCA: 06 06           LD      B,$06               
2FCC: 06 1A           LD      B,$1A               
2FCE: 04              INC     B                   
2FCF: 1B              DEC     DE                  
2FD0: 05              DEC     B                   
2FD1: 18 03           JR      $2FD6               ; {}
2FD3: 03              INC     BC                  
2FD4: 03              INC     BC                  
2FD5: 03              INC     BC                  
2FD6: 19              ADD     HL,DE               
2FD7: 06 06           LD      B,$06               
2FD9: 06 1A           LD      B,$1A               
2FDB: 04              INC     B                   
2FDC: 1B              DEC     DE                  
2FDD: 05              DEC     B                   
2FDE: 18 03           JR      $2FE3               ; {}
2FE0: 03              INC     BC                  
2FE1: 19              ADD     HL,DE               
2FE2: 06 06           LD      B,$06               
2FE4: 1A              LD      A,(DE)              
2FE5: 11 12 13        LD      DE,$1312            
2FE8: 02              LD      (BC),A              
2FE9: 02              LD      (BC),A              
2FEA: 02              LD      (BC),A              
2FEB: 05              DEC     B                   
2FEC: 05              DEC     B                   
2FED: 02              LD      (BC),A              
2FEE: 02              LD      (BC),A              
2FEF: 02              LD      (BC),A              
2FF0: 05              DEC     B                   
2FF1: 05              DEC     B                   
2FF2: 02              LD      (BC),A              
2FF3: 02              LD      (BC),A              
2FF4: 02              LD      (BC),A              
2FF5: 05              DEC     B                   
2FF6: 1C              INC     E                   
2FF7: 08              EX      AF,AF'              
2FF8: 08              EX      AF,AF'              
2FF9: 07              RLCA                        
2FFA: 07              RLCA                        
2FFB: 08              EX      AF,AF'              
2FFC: 08              EX      AF,AF'              
2FFD: 08              EX      AF,AF'              
2FFE: 00              NOP                         
2FFF: FF              RST     0X38                
3000: 21 93 43        LD      HL,$4393            
3003: 7E              LD      A,(HL)              
3004: 34              INC     (HL)                
3005: E6 07           AND     $07                 
3007: 21 18 30        LD      HL,$3018            
300A: 07              RLCA                        
300B: 85              ADD     A,L                 
300C: 6F              LD      L,A                 
300D: 7E              LD      A,(HL)              
300E: 23              INC     HL                  
300F: 6E              LD      L,(HL)              
3010: 67              LD      H,A                 
3011: E9              JP      (HL)                
3012: C9              RET                         
3013: FF              RST     0X38                
3014: FF              RST     0X38                
3015: FF              RST     0X38                
3016: FF              RST     0X38                
3017: FF              RST     0X38                
3018: 32 64 30        LD      ($3064),A           ; {}
301B: 28 30           JR      Z,$304D             ; {}
301D: BA              CP      D                   
301E: 31 24 31        LD      SP,$3124            
3021: 5A              LD      E,D                 
3022: 31 B4 32        LD      SP,$32B4            
3025: 2C              INC     L                   
3026: 30 12           JR      NC,$303A            ; {}
3028: 21 57 43        LD      HL,$4357            
302B: 7E              LD      A,(HL)              
302C: FE 03           CP      $03                 
302E: D0              RET     NC                  
302F: 2E 50           LD      L,$50               
3031: 7E              LD      A,(HL)              
3032: FE 04           CP      $04                 
3034: D0              RET     NC                  
3035: 2E 58           LD      L,$58               
3037: 7E              LD      A,(HL)              
3038: A7              AND     A                   
3039: CA 5C 30        JP      Z,$305C             ; {}
303C: 35              DEC     (HL)                
303D: C0              RET     NZ                  
303E: 2D              DEC     L                   
303F: 34              INC     (HL)                
3040: 2E 50           LD      L,$50               
3042: 36 04           LD      (HL),$04            
3044: 2E 53           LD      L,$53               
3046: 36 10           LD      (HL),$10            
3048: 2C              INC     L                   
3049: 36 50           LD      (HL),$50            
304B: 2E 51           LD      L,$51               
304D: 36 2E           LD      (HL),$2E            
304F: 2C              INC     L                   
3050: 36 00           LD      (HL),$00            
3052: 3A C2 43        LD      A,($43C2)           
3055: 0F              RRCA                        
3056: D8              RET     C                   
3057: 36 40           LD      (HL),$40            
3059: C9              RET                         
305A: FF              RST     0X38                
305B: FF              RST     0X38                
305C: CD 74 30        CALL    $3074               ; {}
305F: 21 57 43        LD      HL,$4357            
3062: 7E              LD      A,(HL)              
3063: 07              RLCA                        
3064: 07              RLCA                        
3065: 00              NOP                         
3066: 00              NOP                         
3067: 81              ADD     A,C                 
3068: C6 07           ADD     $07                 
306A: 2E 58           LD      L,$58               
306C: 77              LD      (HL),A              
306D: C9              RET                         
306E: FF              RST     0X38                
306F: FF              RST     0X38                
3070: FF              RST     0X38                
3071: FF              RST     0X38                
3072: FF              RST     0X38                
3073: FF              RST     0X38                
3074: 21 B8 43        LD      HL,$43B8            
3077: 7E              LD      A,(HL)              
3078: 0F              RRCA                        
3079: 00              NOP                         
307A: E6 07           AND     $07                 
307C: 47              LD      B,A                 
307D: 3E 07           LD      A,$07               
307F: 90              SUB     B                   
3080: 4F              LD      C,A                 
3081: 7E              LD      A,(HL)              
3082: FE 80           CP      $80                 
3084: DA 89 30        JP      C,$3089             ; {}
3087: 3E 70           LD      A,$70               
3089: 0F              RRCA                        
308A: 0F              RRCA                        
308B: 0F              RRCA                        
308C: 0F              RRCA                        
308D: E6 07           AND     $07                 
308F: 47              LD      B,A                 
3090: 3E 07           LD      A,$07               
3092: 90              SUB     B                   
3093: 81              ADD     A,C                 
3094: 4F              LD      C,A                 
3095: 3A BA 43        LD      A,($43BA)           
3098: D6 05           SUB     $05                 
309A: D2 9F 30        JP      NC,$309F            ; {}
309D: 3E 10           LD      A,$10               
309F: 81              ADD     A,C                 
30A0: 4F              LD      C,A                 
30A1: CD AA 30        CALL    $30AA               ; {}
30A4: E6 07           AND     $07                 
30A6: 81              ADD     A,C                 
30A7: 4F              LD      C,A                 
30A8: C9              RET                         
30A9: FF              RST     0X38                
30AA: 21 9B 43        LD      HL,$439B            
30AD: 7E              LD      A,(HL)              
30AE: 07              RLCA                        
30AF: 07              RLCA                        
30B0: 07              RLCA                        
30B1: E6 07           AND     $07                 
30B3: 2E C2           LD      L,$C2               
30B5: 86              ADD     A,(HL)              
30B6: E6 0F           AND     $0F                 
30B8: C9              RET                         
30B9: C0              RET     NZ                  
30BA: 21 58 43        LD      HL,$4358            
30BD: CD DA 30        CALL    $30DA               ; {}
30C0: CD DA 30        CALL    $30DA               ; {}
30C3: CD DA 30        CALL    $30DA               ; {}
30C6: 2E 50           LD      L,$50               
30C8: 7E              LD      A,(HL)              
30C9: A7              AND     A                   
30CA: C0              RET     NZ                  
30CB: 2E 55           LD      L,$55               
30CD: 7E              LD      A,(HL)              
30CE: A7              AND     A                   
30CF: CA E4 30        JP      Z,$30E4             ; {}
30D2: 35              DEC     (HL)                
30D3: C0              RET     NZ                  
30D4: 2E 50           LD      L,$50               
30D6: 36 01           LD      (HL),$01            
30D8: C9              RET                         
30D9: FE 2C           CP      $2C                 
30DB: 7E              LD      A,(HL)              
30DC: A7              AND     A                   
30DD: C8              RET     Z                   
30DE: 35              DEC     (HL)                
30DF: C9              RET                         
30E0: 7E              LD      A,(HL)              
30E1: FE 01           CP      $01                 
30E3: D0              RET     NC                  
30E4: CD 74 30        CALL    $3074               ; {}
30E7: 21 9A 43        LD      HL,$439A            
30EA: 7E              LD      A,(HL)              
30EB: FE 10           CP      $10                 
30ED: DA F2 30        JP      C,$30F2             ; {}
30F0: 3E 0F           LD      A,$0F               
30F2: 47              LD      B,A                 
30F3: 3E 0F           LD      A,$0F               
30F5: 90              SUB     B                   
30F6: 81              ADD     A,C                 
30F7: 4F              LD      C,A                 
30F8: 06 01           LD      B,$01               
30FA: 2E 58           LD      L,$58               
30FC: CD 12 31        CALL    $3112               ; {}
30FF: CD 12 31        CALL    $3112               ; {}
3102: CD 12 31        CALL    $3112               ; {}
3105: 79              LD      A,C                 
3106: 0F              RRCA                        
3107: 0F              RRCA                        
3108: E6 3F           AND     $3F                 
310A: C6 01           ADD     $01                 
310C: 2E 55           LD      L,$55               
310E: 77              LD      (HL),A              
310F: C9              RET                         
3110: 21 50 2C        LD      HL,$2C50            
3113: 7E              LD      A,(HL)              
3114: A7              AND     A                   
3115: C0              RET     NZ                  
3116: 79              LD      A,C                 
3117: 0F              RRCA                        
3118: E6 7F           AND     $7F                 
311A: 4F              LD      C,A                 
311B: 78              LD      A,B                 
311C: A7              AND     A                   
311D: C8              RET     Z                   
311E: 05              DEC     B                   
311F: 36 0C           LD      (HL),$0C            
3121: C9              RET                         
3122: 86              ADD     A,(HL)              
3123: 47              LD      B,A                 
3124: 21 50 43        LD      HL,$4350            
3127: 7E              LD      A,(HL)              
3128: FE 01           CP      $01                 
312A: C0              RET     NZ                  
312B: 36 02           LD      (HL),$02            
312D: 2E B8           LD      L,$B8               
312F: 7E              LD      A,(HL)              
3130: 0F              RRCA                        
3131: 0F              RRCA                        
3132: E6 0F           AND     $0F                 
3134: C6 05           ADD     $05                 
3136: FE 11           CP      $11                 
3138: DA 3D 31        JP      C,$313D             ; {}
313B: 3E 05           LD      A,$05               
313D: 2E 57           LD      L,$57               
313F: 96              SUB     (HL)                
3140: 47              LD      B,A                 
3141: CD AA 30        CALL    $30AA               ; {}
3144: 3C              INC     A                   
3145: B8              CP      B                   
3146: DA 4B 31        JP      C,$314B             ; {}
3149: 3E 01           LD      A,$01               
314B: 2E 53           LD      L,$53               
314D: 77              LD      (HL),A              
314E: C9              RET                         
314F: 0A              LD      A,(BC)              
3150: 0C              INC     C                   
3151: 0B              DEC     BC                  
3152: 0C              INC     C                   
3153: 0B              DEC     BC                  
3154: 0E 0F           LD      C,$0F               
3156: 0E 0F           LD      C,$0F               
3158: FF              RST     0X38                
3159: FF              RST     0X38                
315A: 21 50 43        LD      HL,$4350            
315D: 7E              LD      A,(HL)              
315E: FE 02           CP      $02                 
3160: C0              RET     NZ                  
3161: CD AA 30        CALL    $30AA               ; {}
3164: 00              NOP                         
3165: 47              LD      B,A                 
3166: 07              RLCA                        
3167: C6 50           ADD     $50                 
3169: 6F              LD      L,A                 
316A: 26 4B           LD      H,$4B               
316C: 78              LD      A,B                 
316D: 07              RLCA                        
316E: 07              RLCA                        
316F: C6 70           ADD     $70                 
3171: 5F              LD      E,A                 
3172: 16 4B           LD      D,$4B               
3174: 0E 10           LD      C,$10               
3176: 79              LD      A,C                 
3177: 90              SUB     B                   
3178: 47              LD      B,A                 
3179: CD 92 31        CALL    $3192               ; {}
317C: 13              INC     DE                  
317D: 13              INC     DE                  
317E: 13              INC     DE                  
317F: 13              INC     DE                  
3180: 23              INC     HL                  
3181: 23              INC     HL                  
3182: 05              DEC     B                   
3183: C2 8A 31        JP      NZ,$318A            ; {}
3186: 1E 70           LD      E,$70               
3188: 2E 50           LD      L,$50               
318A: 0D              DEC     C                   
318B: C2 79 31        JP      NZ,$3179            ; {}
318E: C9              RET                         
318F: FF              RST     0X38                
3190: FF              RST     0X38                
3191: FF              RST     0X38                
3192: 1A              LD      A,(DE)              
3193: E6 08           AND     $08                 
3195: C8              RET     Z                   
3196: 3A 94 43        LD      A,($4394)           
3199: BE              CP      (HL)                
319A: C0              RET     NZ                  
319B: 3A 56 43        LD      A,($4356)           
319E: 2C              INC     L                   
319F: 46              LD      B,(HL)              
31A0: 2D              DEC     L                   
31A1: B8              CP      B                   
31A2: C0              RET     NZ                  
31A3: 7D              LD      A,L                 
31A4: 32 54 43        LD      ($4354),A           
31A7: 3E 03           LD      A,$03               
31A9: 32 50 43        LD      ($4350),A           
31AC: E1              POP     HL                  
31AD: C9              RET                         
31AE: FF              RST     0X38                
31AF: FF              RST     0X38                
31B0: FF              RST     0X38                
31B1: FF              RST     0X38                
31B2: FF              RST     0X38                
31B3: FF              RST     0X38                
31B4: 3A 50 43        LD      A,($4350)           
31B7: FE 03           CP      $03                 
31B9: C0              RET     NZ                  
31BA: 3A 54 43        LD      A,($4354)           
31BD: D6 50           SUB     $50                 
31BF: 07              RLCA                        
31C0: C6 72           ADD     $72                 
31C2: 6F              LD      L,A                 
31C3: 26 4B           LD      H,$4B               
31C5: 46              LD      B,(HL)              
31C6: 2C              INC     L                   
31C7: 56              LD      D,(HL)              
31C8: 3A C2 43        LD      A,($43C2)           
31CB: 0E 04           LD      C,$04               
31CD: B8              CP      B                   
31CE: D2 D6 31        JP      NC,$31D6            ; {}
31D1: 4F              LD      C,A                 
31D2: 78              LD      A,B                 
31D3: 41              LD      B,C                 
31D4: 0E 00           LD      C,$00               
31D6: 90              SUB     B                   
31D7: 07              RLCA                        
31D8: 07              RLCA                        
31D9: 07              RLCA                        
31DA: E6 07           AND     $07                 
31DC: C6 00           ADD     $00                 
31DE: 6F              LD      L,A                 
31DF: 26 33           LD      H,$33               
31E1: 7E              LD      A,(HL)              
31E2: 81              ADD     A,C                 
31E3: 07              RLCA                        
31E4: 07              RLCA                        
31E5: 4F              LD      C,A                 
31E6: 00              NOP                         
31E7: 00              NOP                         
31E8: 00              NOP                         
31E9: 3A 57 43        LD      A,($4357)           
31EC: 47              LD      B,A                 
31ED: CD 10 32        CALL    $3210               ; {}
31F0: 79              LD      A,C                 
31F1: 80              ADD     A,B                 
31F2: C6 10           ADD     $10                 
31F4: 6F              LD      L,A                 
31F5: 26 33           LD      H,$33               
31F7: 4E              LD      C,(HL)              
31F8: CD AA 30        CALL    $30AA               ; {}
31FB: E6 06           AND     $06                 
31FD: 81              ADD     A,C                 
31FE: 6F              LD      L,A                 
31FF: 26 33           LD      H,$33               
3201: 7E              LD      A,(HL)              
3202: 2C              INC     L                   
3203: 46              LD      B,(HL)              
3204: 21 50 43        LD      HL,$4350            
3207: 36 05           LD      (HL),$05            
3209: 2C              INC     L                   
320A: 77              LD      (HL),A              
320B: 2C              INC     L                   
320C: 70              LD      (HL),B              
320D: C9              RET                         
320E: 81              ADD     A,C                 
320F: 6F              LD      L,A                 
3210: 3A 53 43        LD      A,($4353)           
3213: FE 01           CP      $01                 
3215: C0              RET     NZ                  
3216: 7A              LD      A,D                 
3217: 06 00           LD      B,$00               
3219: FE 58           CP      $58                 
321B: D8              RET     C                   
321C: 06 01           LD      B,$01               
321E: FE 78           CP      $78                 
3220: D8              RET     C                   
3221: 06 02           LD      B,$02               
3223: FE 98           CP      $98                 
3225: D8              RET     C                   
3226: 06 03           LD      B,$03               
3228: C9              RET                         
3229: C0              RET     NZ                  
322A: 21 50 3A        LD      HL,$3A50            
322D: 50              LD      D,B                 
322E: 43              LD      B,E                 
322F: FE 04           CP      $04                 
3231: C0              RET     NZ                  
3232: 21 50 4B        LD      HL,$4B50            
3235: 11 70 4B        LD      DE,$4B70            
3238: 3A 56 43        LD      A,($4356)           
323B: 4F              LD      C,A                 
323C: 3A 94 43        LD      A,($4394)           
323F: 47              LD      B,A                 
3240: 1A              LD      A,(DE)              
3241: E6 08           AND     $08                 
3243: CA 4E 32        JP      Z,$324E             ; {}
3246: 7E              LD      A,(HL)              
3247: B8              CP      B                   
3248: C0              RET     NZ                  
3249: 2C              INC     L                   
324A: 7E              LD      A,(HL)              
324B: 2D              DEC     L                   
324C: B9              CP      C                   
324D: C0              RET     NZ                  
324E: 2C              INC     L                   
324F: 2C              INC     L                   
3250: 7B              LD      A,E                 
3251: C6 04           ADD     $04                 
3253: 5F              LD      E,A                 
3254: FE B0           CP      $B0                 
3256: C2 40 32        JP      NZ,$3240            ; {}
3259: 3E 06           LD      A,$06               
325B: 32 50 43        LD      ($4350),A           
325E: C9              RET                         
325F: 3C              INC     A                   
3260: E6 0F           AND     $0F                 
3262: 77              LD      (HL),A              
3263: 2E 21           LD      L,$21               
3265: 95              SUB     L                   
3266: 43              LD      B,E                 
3267: 7E              LD      A,(HL)              
3268: 32 56 43        LD      ($4356),A           
326B: 3C              INC     A                   
326C: E6 0F           AND     $0F                 
326E: 77              LD      (HL),A              
326F: 2E 50           LD      L,$50               
3271: 7E              LD      A,(HL)              
3272: FE 05           CP      $05                 
3274: D8              RET     C                   
3275: 36 00           LD      (HL),$00            
3277: 2E 53           LD      L,$53               
3279: 4E              LD      C,(HL)              
327A: 2C              INC     L                   
327B: 6E              LD      L,(HL)              
327C: 26 4B           LD      H,$4B               
327E: 3A 56 43        LD      A,($4356)           
3281: 57              LD      D,A                 
3282: 3A 94 43        LD      A,($4394)           
3285: 5F              LD      E,A                 
3286: 7D              LD      A,L                 
3287: D6 50           SUB     $50                 
3289: 0F              RRCA                        
328A: 47              LD      B,A                 
328B: 3E 10           LD      A,$10               
328D: 90              SUB     B                   
328E: 47              LD      B,A                 
328F: 7E              LD      A,(HL)              
3290: 2C              INC     L                   
3291: BB              CP      E                   
3292: C2 A4 32        JP      NZ,$32A4            ; {}
3295: 7E              LD      A,(HL)              
3296: BA              CP      D                   
3297: C2 A4 32        JP      NZ,$32A4            ; {}
329A: 2D              DEC     L                   
329B: 3A 51 43        LD      A,($4351)           
329E: 77              LD      (HL),A              
329F: 2C              INC     L                   
32A0: 3A 52 43        LD      A,($4352)           
32A3: 77              LD      (HL),A              
32A4: 2C              INC     L                   
32A5: 05              DEC     B                   
32A6: C2 AB 32        JP      NZ,$32AB            ; {}
32A9: 2E 50           LD      L,$50               
32AB: 0D              DEC     C                   
32AC: C2 8F 32        JP      NZ,$328F            ; {}
32AF: C9              RET                         
32B0: 21 50 43        LD      HL,$4350            
32B3: 06 30           LD      B,$30               
32B5: CD D8 05        CALL    $05D8               ; {}
32B8: 2E 9A           LD      L,$9A               
32BA: 06 04           LD      B,$04               
32BC: CD D8 05        CALL    $05D8               ; {}
32BF: 3A BB 43        LD      A,($43BB)           
32C2: A7              AND     A                   
32C3: C8              RET     Z                   
32C4: 07              RLCA                        
32C5: 07              RLCA                        
32C6: 07              RLCA                        
32C7: 4F              LD      C,A                 
32C8: 21 70 4B        LD      HL,$4B70            
32CB: 06 40           LD      B,$40               
32CD: CD D8 05        CALL    $05D8               ; {}
32D0: 16 4B           LD      D,$4B               
32D2: 26 3F           LD      H,$3F               
32D4: 3E 40           LD      A,$40               
32D6: 91              SUB     C                   
32D7: C6 70           ADD     $70                 
32D9: 5F              LD      E,A                 
32DA: C6 10           ADD     $10                 
32DC: 6F              LD      L,A                 
32DD: 41              LD      B,C                 
32DE: 3A B8 43        LD      A,($43B8)           
32E1: 0F              RRCA                        
32E2: 0F              RRCA                        
32E3: D2 E0 05        JP      NC,$05E0            ; {}
32E6: 7D              LD      A,L                 
32E7: C6 40           ADD     $40                 
32E9: 6F              LD      L,A                 
32EA: C3 E0 05        JP      $05E0               ; {}
32ED: CD E0 05        CALL    $05E0               ; {}
32F0: C3 A0 03        JP      $03A0               ; {}
32F3: FF              RST     0X38                
32F4: FF              RST     0X38                
32F5: FF              RST     0X38                
32F6: FF              RST     0X38                
32F7: FF              RST     0X38                
32F8: FF              RST     0X38                
32F9: FF              RST     0X38                
32FA: FF              RST     0X38                
32FB: FF              RST     0X38                
32FC: FF              RST     0X38                
32FD: FF              RST     0X38                
32FE: FF              RST     0X38                
32FF: FF              RST     0X38                
3300: 00              NOP                         
3301: 01 02 02        LD      BC,$0202            
3304: 03              INC     BC                  
3305: 03              INC     BC                  
3306: 03              INC     BC                  
3307: 03              INC     BC                  
3308: FF              RST     0X38                
3309: FF              RST     0X38                
330A: FF              RST     0X38                
330B: FF              RST     0X38                
330C: FF              RST     0X38                
330D: FF              RST     0X38                
330E: FF              RST     0X38                
330F: FF              RST     0X38                
3310: 88              ADC     A,B                 
3311: 90              SUB     B                   
3312: 98              SBC     B                   
3313: A0              AND     B                   
3314: 68              LD      L,B                 
3315: 70              LD      (HL),B              
3316: 78              LD      A,B                 
3317: 80              ADD     A,B                 
3318: 48              LD      C,B                 
3319: 50              LD      D,B                 
331A: 58              LD      E,B                 
331B: 60              LD      H,B                 
331C: 48              LD      C,B                 
331D: 30 38           JR      NC,$3357            ; {}
331F: 40              LD      B,B                 
3320: 88              ADC     A,B                 
3321: 90              SUB     B                   
3322: 98              SBC     B                   
3323: A0              AND     B                   
3324: A8              XOR     B                   
3325: B0              OR      B                   
3326: B8              CP      B                   
3327: C0              RET     NZ                  
3328: C8              RET     Z                   
3329: D0              RET     NC                  
332A: D8              RET     C                   
332B: E0              RET     PO                  
332C: C8              RET     Z                   
332D: E8              RET     PE                  
332E: F0              RET     P                   
332F: F8              RET     M                   
3330: 11 30 2C        LD      DE,$2C30            
3333: 00              NOP                         
3334: 2F              CPL                         
3335: A0              AND     B                   
3336: 2C              INC     L                   
3337: 00              NOP                         
3338: 2E C4           LD      L,$C4               
333A: 2F              CPL                         
333B: A0              AND     B                   
333C: 2F              CPL                         
333D: 34              INC     (HL)                
333E: 2F              CPL                         
333F: A0              AND     B                   
3340: 2C              INC     L                   
3341: C8              RET     Z                   
3342: 2E C4           LD      L,$C4               
3344: 2E 20           LD      L,$20               
3346: 2E C4           LD      L,$C4               
3348: 11 30 13        LD      DE,$1330            
334B: 9C              SBC     H                   
334C: 13              INC     DE                  
334D: D0              RET     NC                  
334E: 2C              INC     L                   
334F: 00              NOP                         
3350: 11 30 13        LD      DE,$1330            
3353: 28 2C           JR      Z,$3381             ; {}
3355: 00              NOP                         
3356: 2F              CPL                         
3357: 34              INC     (HL)                
3358: 11 A4 2C        LD      DE,$2CA4            
335B: 90              SUB     B                   
335C: 2F              CPL                         
335D: 34              INC     (HL)                
335E: 2F              CPL                         
335F: A0              AND     B                   
3360: 2C              INC     L                   
3361: 90              SUB     B                   
3362: 2C              INC     L                   
3363: C8              RET     Z                   
3364: 2E 20           LD      L,$20               
3366: 2E C4           LD      L,$C4               
3368: 11 60 13        LD      DE,$1360            
336B: 54              LD      D,H                 
336C: 13              INC     DE                  
336D: 9C              SBC     H                   
336E: 13              INC     DE                  
336F: D0              RET     NC                  
3370: 10 20           DJNZ    $3392               ; {}
3372: 10 64           DJNZ    $33D8               ; {}
3374: 11 A4 13        LD      DE,$13A4            
3377: 28 10           JR      Z,$3389             ; {}
3379: 20 11           JR      NZ,$338C            ; {}
337B: A4              AND     H                   
337C: 12              LD      (DE),A              
337D: 00              NOP                         
337E: 2F              CPL                         
337F: 34              INC     (HL)                
3380: 2C              INC     L                   
3381: 90              SUB     B                   
3382: 2C              INC     L                   
3383: C8              RET     Z                   
3384: 2D              DEC     L                   
3385: C0              RET     NZ                  
3386: 2E 20           LD      L,$20               
3388: 11 60 12        LD      DE,$1260            
338B: 44              LD      B,H                 
338C: 12              LD      (DE),A              
338D: 88              ADC     A,B                 
338E: 13              INC     DE                  
338F: 54              LD      D,H                 
3390: 10 20           DJNZ    $33B2               ; {}
3392: 10 64           DJNZ    $33F8               ; {}
3394: 12              LD      (DE),A              
3395: 00              NOP                         
3396: 12              LD      (DE),A              
3397: 44              LD      B,H                 
3398: 10 20           DJNZ    $33BA               ; {}
339A: 12              LD      (DE),A              
339B: 00              NOP                         
339C: 10 20           DJNZ    $33BE               ; {}
339E: 12              LD      (DE),A              
339F: 00              NOP                         
33A0: 10 A8           DJNZ    $334A               ; {}
33A2: 2D              DEC     L                   
33A3: 88              ADC     A,B                 
33A4: 10 A8           DJNZ    $334E               ; {}
33A6: 2D              DEC     L                   
33A7: C0              RET     NZ                  
33A8: 11 D0 12        LD      DE,$12D0            
33AB: CA 13 00        JP      Z,$0013             ; {}
33AE: 13              INC     DE                  
33AF: 54              LD      D,H                 
33B0: 10 20           DJNZ    $33D2               ; {}
33B2: 10 64           DJNZ    $3418               ; {}
33B4: 10 D4           DJNZ    $338A               ; {}
33B6: 13              INC     DE                  
33B7: 00              NOP                         
33B8: 10 20           DJNZ    $33DA               ; {}
33BA: 10 D4           DJNZ    $3390               ; {}
33BC: 12              LD      (DE),A              
33BD: 00              NOP                         
33BE: 2F              CPL                         
33BF: 00              NOP                         
33C0: 2D              DEC     L                   
33C1: 00              NOP                         
33C2: 2D              DEC     L                   
33C3: 44              LD      B,H                 
33C4: 2D              DEC     L                   
33C5: 88              ADC     A,B                 
33C6: 2E 6C           LD      L,$6C               
33C8: 11 00 11        LD      DE,$1100            
33CB: D0              RET     NC                  
33CC: 12              LD      (DE),A              
33CD: CA 2F 64        JP      Z,$642F             
33D0: 11 00 13        LD      DE,$1300            
33D3: 00              NOP                         
33D4: 2F              CPL                         
33D5: 64              LD      H,H                 
33D6: 2F              CPL                         
33D7: 00              NOP                         
33D8: 10 D4           DJNZ    $33AE               ; {}
33DA: 2D              DEC     L                   
33DB: 00              NOP                         
33DC: 2F              CPL                         
33DD: 00              NOP                         
33DE: 2C              INC     L                   
33DF: 34              INC     (HL)                
33E0: 2D              DEC     L                   
33E1: 00              NOP                         
33E2: 2D              DEC     L                   
33E3: 44              LD      B,H                 
33E4: 2E 6C           LD      L,$6C               
33E6: 2E 90           LD      L,$90               
33E8: 11 00 2C        LD      DE,$2C00            
33EB: 34              INC     (HL)                
33EC: 2F              CPL                         
33ED: 64              LD      H,H                 
33EE: 2F              CPL                         
33EF: 64              LD      H,H                 
33F0: 2E 90           LD      L,$90               
33F2: 2F              CPL                         
33F3: 00              NOP                         
33F4: 2C              INC     L                   
33F5: 34              INC     (HL)                
33F6: 2C              INC     L                   
33F7: 34              INC     (HL)                
33F8: 2D              DEC     L                   
33F9: 44              LD      B,H                 
33FA: 2E 6C           LD      L,$6C               
33FC: 2E 90           LD      L,$90               
33FE: 2E 90           LD      L,$90               
3400: CD 76 08        CALL    $0876               ; {}
3403: CD 00 38        CALL    $3800               ; {}
3406: CD 00 26        CALL    $2600               ; {}
3409: CD 00 38        CALL    $3800               ; {}
340C: CD 80 39        CALL    $3980               ; {}
340F: 3A BB 43        LD      A,($43BB)           
3412: A7              AND     A                   
3413: CA 62 34        JP      Z,$3462             ; {}
3416: FE 04           CP      $04                 
3418: D2 38 34        JP      NC,$3438            ; {}
341B: CD 74 34        CALL    $3474               ; {}
341E: CD 86 34        CALL    $3486               ; {}
3421: CD 60 35        CALL    $3560               ; {}
3424: CD 98 34        CALL    $3498               ; {}
3427: CD AA 34        CALL    $34AA               ; {}
342A: 3A 9B 43        LD      A,($439B)           ; {ram.Counter+1}
342D: 0F              RRCA                        
342E: DA C0 0F        JP      C,$0FC0             ; {}
3431: CD 30 39        CALL    $3930               ; {}
3434: C3 40 0C        JP      $0C40               ; {}
3437: FF              RST     0X38                
3438: 3A 9B 43        LD      A,($439B)           ; {ram.Counter+1}
343B: 0F              RRCA                        
343C: DA 52 34        JP      C,$3452             ; {}
343F: CD 74 34        CALL    $3474               ; {}
3442: CD 60 35        CALL    $3560               ; {}
3445: CD 98 34        CALL    $3498               ; {}
3448: CD 30 39        CALL    $3930               ; {}
344B: C3 40 0C        JP      $0C40               ; {}
344E: FF              RST     0X38                
344F: FF              RST     0X38                
3450: FF              RST     0X38                
3451: FF              RST     0X38                
3452: CD 86 34        CALL    $3486               ; {}
3455: CD 60 35        CALL    $3560               ; {}
3458: CD AA 34        CALL    $34AA               ; {}
345B: C3 C0 0F        JP      $0FC0               ; {}
345E: FF              RST     0X38                
345F: FF              RST     0X38                
3460: FF              RST     0X38                
3461: FF              RST     0X38                
3462: 3A 9B 43        LD      A,($439B)           ; {ram.Counter+1}
3465: 0F              RRCA                        
3466: D8              RET     C                   
3467: CD 40 0C        CALL    $0C40               ; {}
346A: CD C0 0F        CALL    $0FC0               ; {}
346D: C3 04 22        JP      $2204               ; {}
3470: FF              RST     0X38                
3471: FF              RST     0X38                
3472: FF              RST     0X38                
3473: FF              RST     0X38                
3474: 21 70 4B        LD      HL,$4B70            
3477: E5              PUSH    HL                  
3478: CD C0 34        CALL    $34C0               ; {}
347B: E1              POP     HL                  
347C: 7D              LD      A,L                 
347D: C6 08           ADD     $08                 
347F: 6F              LD      L,A                 
3480: FE 90           CP      $90                 
3482: C2 77 34        JP      NZ,$3477            ; {}
3485: C9              RET                         
3486: 21 90 4B        LD      HL,$4B90            
3489: E5              PUSH    HL                  
348A: CD C0 34        CALL    $34C0               ; {}
348D: E1              POP     HL                  
348E: 7D              LD      A,L                 
348F: C6 08           ADD     $08                 
3491: 6F              LD      L,A                 
3492: FE B0           CP      $B0                 
3494: C2 89 34        JP      NZ,$3489            ; {}
3497: C9              RET                         
3498: 21 70 4B        LD      HL,$4B70            
349B: E5              PUSH    HL                  
349C: CD B0 35        CALL    $35B0               ; {}
349F: E1              POP     HL                  
34A0: 7D              LD      A,L                 
34A1: C6 08           ADD     $08                 
34A3: 6F              LD      L,A                 
34A4: FE 90           CP      $90                 
34A6: C2 9B 34        JP      NZ,$349B            ; {}
34A9: C9              RET                         
34AA: 21 90 4B        LD      HL,$4B90            
34AD: E5              PUSH    HL                  
34AE: CD B0 35        CALL    $35B0               ; {}
34B1: E1              POP     HL                  
34B2: 7D              LD      A,L                 
34B3: C6 08           ADD     $08                 
34B5: 6F              LD      L,A                 
34B6: FE B0           CP      $B0                 
34B8: C2 AD 34        JP      NZ,$34AD            ; {}
34BB: C9              RET                         
34BC: FF              RST     0X38                
34BD: FF              RST     0X38                
34BE: FF              RST     0X38                
34BF: FF              RST     0X38                
34C0: 7E              LD      A,(HL)              
34C1: A7              AND     A                   
34C2: C8              RET     Z                   
34C3: 47              LD      B,A                 
34C4: C6 C0           ADD     $C0                 
34C6: 5F              LD      E,A                 
34C7: 16 3E           LD      D,$3E               
34C9: 1A              LD      A,(DE)              
34CA: 4F              LD      C,A                 
34CB: 2C              INC     L                   
34CC: 56              LD      D,(HL)              
34CD: 2C              INC     L                   
34CE: 5E              LD      E,(HL)              
34CF: 2C              INC     L                   
34D0: 78              LD      A,B                 
34D1: 07              RLCA                        
34D2: 07              RLCA                        
34D3: 07              RLCA                        
34D4: 86              ADD     A,(HL)              
34D5: E6 7E           AND     $7E                 
34D7: 6F              LD      L,A                 
34D8: 26 3E           LD      H,$3E               
34DA: 7E              LD      A,(HL)              
34DB: 2C              INC     L                   
34DC: 6E              LD      L,(HL)              
34DD: 67              LD      H,A                 
34DE: 7A              LD      A,D                 
34DF: FE 4B           CP      $4B                 
34E1: C2 0C 35        JP      NZ,$350C            ; {}
34E4: 7B              LD      A,E                 
34E5: FE 50           CP      $50                 
34E7: DA 0C 35        JP      C,$350C             ; {}
34EA: 06 08           LD      B,$08               
34EC: 2C              INC     L                   
34ED: 2C              INC     L                   
34EE: D6 20           SUB     $20                 
34F0: 5F              LD      E,A                 
34F1: FE 50           CP      $50                 
34F3: DA 09 35        JP      C,$3509             ; {}
34F6: 06 10           LD      B,$10               
34F8: 2C              INC     L                   
34F9: 2C              INC     L                   
34FA: D6 20           SUB     $20                 
34FC: 5F              LD      E,A                 
34FD: FE 50           CP      $50                 
34FF: DA 09 35        JP      C,$3509             ; {}
3502: 06 18           LD      B,$18               
3504: 2C              INC     L                   
3505: 2C              INC     L                   
3506: D6 20           SUB     $20                 
3508: 5F              LD      E,A                 
3509: 79              LD      A,C                 
350A: 80              ADD     A,B                 
350B: 4F              LD      C,A                 
350C: 06 35           LD      B,$35               
350E: C5              PUSH    BC                  
350F: 01 DF FF        LD      BC,$FFDF            
3512: EB              EX      DE,HL               
3513: 36 00           LD      (HL),$00            
3515: 23              INC     HL                  
3516: 36 00           LD      (HL),$00            
3518: 09              ADD     HL,BC               
3519: C9              RET                         
351A: FF              RST     0X38                
351B: FF              RST     0X38                
351C: FF              RST     0X38                
351D: FF              RST     0X38                
351E: FF              RST     0X38                
351F: FF              RST     0X38                
3520: 1A              LD      A,(DE)              
3521: 77              LD      (HL),A              
3522: 13              INC     DE                  
3523: 23              INC     HL                  
3524: 1A              LD      A,(DE)              
3525: 77              LD      (HL),A              
3526: 13              INC     DE                  
3527: 09              ADD     HL,BC               
3528: 1A              LD      A,(DE)              
3529: 77              LD      (HL),A              
352A: 13              INC     DE                  
352B: 23              INC     HL                  
352C: 1A              LD      A,(DE)              
352D: 77              LD      (HL),A              
352E: 13              INC     DE                  
352F: 09              ADD     HL,BC               
3530: 1A              LD      A,(DE)              
3531: 77              LD      (HL),A              
3532: 13              INC     DE                  
3533: 23              INC     HL                  
3534: 1A              LD      A,(DE)              
3535: 77              LD      (HL),A              
3536: 13              INC     DE                  
3537: 09              ADD     HL,BC               
3538: 1A              LD      A,(DE)              
3539: 77              LD      (HL),A              
353A: 13              INC     DE                  
353B: 23              INC     HL                  
353C: 1A              LD      A,(DE)              
353D: 77              LD      (HL),A              
353E: 13              INC     DE                  
353F: 09              ADD     HL,BC               
3540: 1A              LD      A,(DE)              
3541: 77              LD      (HL),A              
3542: 13              INC     DE                  
3543: 23              INC     HL                  
3544: 1A              LD      A,(DE)              
3545: 77              LD      (HL),A              
3546: 13              INC     DE                  
3547: 09              ADD     HL,BC               
3548: 1A              LD      A,(DE)              
3549: 77              LD      (HL),A              
354A: 13              INC     DE                  
354B: 23              INC     HL                  
354C: 1A              LD      A,(DE)              
354D: 77              LD      (HL),A              
354E: 13              INC     DE                  
354F: 09              ADD     HL,BC               
3550: 1A              LD      A,(DE)              
3551: 77              LD      (HL),A              
3552: 13              INC     DE                  
3553: 23              INC     HL                  
3554: 1A              LD      A,(DE)              
3555: 77              LD      (HL),A              
3556: 13              INC     DE                  
3557: 09              ADD     HL,BC               
3558: 36 00           LD      (HL),$00            
355A: 23              INC     HL                  
355B: 36 00           LD      (HL),$00            
355D: C9              RET                         
355E: FF              RST     0X38                
355F: FF              RST     0X38                
3560: CD AA 30        CALL    $30AA               ; {}
3563: 47              LD      B,A                 
3564: 07              RLCA                        
3565: 07              RLCA                        
3566: 4F              LD      C,A                 
3567: 07              RLCA                        
3568: 07              RLCA                        
3569: B0              OR      B                   
356A: 32 6F 43        LD      ($436F),A           
356D: 3A B8 43        LD      A,($43B8)           
3570: FE 40           CP      $40                 
3572: DA 77 35        JP      C,$3577             ; {}
3575: 3E 30           LD      A,$30               
3577: E6 30           AND     $30                 
3579: 0F              RRCA                        
357A: 47              LD      B,A                 
357B: 3A BB 43        LD      A,($43BB)           
357E: 3D              DEC     A                   
357F: FE 04           CP      $04                 
3581: DA 86 35        JP      C,$3586             ; {}
3584: 3E 03           LD      A,$03               
3586: 07              RLCA                        
3587: B0              OR      B                   
3588: 47              LD      B,A                 
3589: 3A 9A 43        LD      A,($439A)           ; {ram.Counter}
358C: 07              RLCA                        
358D: 07              RLCA                        
358E: E6 20           AND     $20                 
3590: B0              OR      B                   
3591: C6 80           ADD     $80                 
3593: 6F              LD      L,A                 
3594: 26 3E           LD      H,$3E               
3596: 7E              LD      A,(HL)              
3597: 32 6E 43        LD      ($436E),A           
359A: 2C              INC     L                   
359B: 7E              LD      A,(HL)              
359C: 81              ADD     A,C                 
359D: E6 F8           AND     $F8                 
359F: 32 6D 43        LD      ($436D),A           
35A2: C9              RET                         
35A3: FF              RST     0X38                
35A4: FF              RST     0X38                
35A5: FF              RST     0X38                
35A6: FF              RST     0X38                
35A7: FF              RST     0X38                
35A8: FF              RST     0X38                
35A9: FF              RST     0X38                
35AA: FF              RST     0X38                
35AB: FF              RST     0X38                
35AC: FF              RST     0X38                
35AD: FF              RST     0X38                
35AE: FF              RST     0X38                
35AF: FF              RST     0X38                
35B0: 7E              LD      A,(HL)              
35B1: A7              AND     A                   
35B2: C8              RET     Z                   
35B3: 47              LD      B,A                 
35B4: 2C              INC     L                   
35B5: 2C              INC     L                   
35B6: 2C              INC     L                   
35B7: 2C              INC     L                   
35B8: 7E              LD      A,(HL)              
35B9: A7              AND     A                   
35BA: CA BE 35        JP      Z,$35BE             ; {}
35BD: 35              DEC     (HL)                
35BE: EB              EX      DE,HL               
35BF: D5              PUSH    DE                  
35C0: 78              LD      A,B                 
35C1: 07              RLCA                        
35C2: 07              RLCA                        
35C3: 07              RLCA                        
35C4: 6F              LD      L,A                 
35C5: 26 3F           LD      H,$3F               
35C7: 46              LD      B,(HL)              
35C8: 23              INC     HL                  
35C9: 4E              LD      C,(HL)              
35CA: C5              PUSH    BC                  
35CB: 23              INC     HL                  
35CC: 46              LD      B,(HL)              
35CD: 23              INC     HL                  
35CE: 4E              LD      C,(HL)              
35CF: C5              PUSH    BC                  
35D0: 23              INC     HL                  
35D1: 46              LD      B,(HL)              
35D2: 23              INC     HL                  
35D3: 4E              LD      C,(HL)              
35D4: C5              PUSH    BC                  
35D5: 23              INC     HL                  
35D6: 46              LD      B,(HL)              
35D7: 23              INC     HL                  
35D8: 4E              LD      C,(HL)              
35D9: C5              PUSH    BC                  
35DA: EB              EX      DE,HL               
35DB: C9              RET                         
35DC: FF              RST     0X38                
35DD: FF              RST     0X38                
35DE: FF              RST     0X38                
35DF: FF              RST     0X38                
35E0: 2C              INC     L                   
35E1: 2C              INC     L                   
35E2: 7E              LD      A,(HL)              
35E3: FE 10           CP      $10                 
35E5: D2 28 36        JP      NC,$3628            ; {}
35E8: 47              LD      B,A                 
35E9: 2D              DEC     L                   
35EA: 86              ADD     A,(HL)              
35EB: 77              LD      (HL),A              
35EC: 2D              DEC     L                   
35ED: 2D              DEC     L                   
35EE: 78              LD      A,B                 
35EF: 86              ADD     A,(HL)              
35F0: 77              LD      (HL),A              
35F1: FE 08           CP      $08                 
35F3: DA 6A 36        JP      C,$366A             ; {}
35F6: E6 07           AND     $07                 
35F8: 77              LD      (HL),A              
35F9: 2D              DEC     L                   
35FA: 7E              LD      A,(HL)              
35FB: D6 20           SUB     $20                 
35FD: 77              LD      (HL),A              
35FE: D2 04 36        JP      NC,$3604            ; {}
3601: 2D              DEC     L                   
3602: 35              DEC     (HL)                
3603: 2C              INC     L                   
3604: 2C              INC     L                   
3605: 2C              INC     L                   
3606: 2C              INC     L                   
3607: 4E              LD      C,(HL)              
3608: 2C              INC     L                   
3609: 2C              INC     L                   
360A: 7E              LD      A,(HL)              
360B: 2D              DEC     L                   
360C: 36 10           LD      (HL),$10            
360E: 91              SUB     C                   
360F: CA 72 36        JP      Z,$3672             ; {}
3612: 3D              DEC     A                   
3613: 0F              RRCA                        
3614: 0F              RRCA                        
3615: 0F              RRCA                        
3616: E6 1F           AND     $1F                 
3618: B8              CP      B                   
3619: 3C              INC     A                   
361A: 77              LD      (HL),A              
361B: D8              RET     C                   
361C: 3A 6E 43        LD      A,($436E)           
361F: 77              LD      (HL),A              
3620: B8              CP      B                   
3621: C8              RET     Z                   
3622: 04              INC     B                   
3623: 70              LD      (HL),B              
3624: C9              RET                         
3625: FF              RST     0X38                
3626: FF              RST     0X38                
3627: FF              RST     0X38                
3628: E6 0F           AND     $0F                 
362A: CA 44 37        JP      Z,$3744             ; {}
362D: 47              LD      B,A                 
362E: 2D              DEC     L                   
362F: 7E              LD      A,(HL)              
3630: 90              SUB     B                   
3631: 77              LD      (HL),A              
3632: 2D              DEC     L                   
3633: 2D              DEC     L                   
3634: 7E              LD      A,(HL)              
3635: 90              SUB     B                   
3636: 77              LD      (HL),A              
3637: D2 95 36        JP      NC,$3695            ; {}
363A: E6 07           AND     $07                 
363C: 77              LD      (HL),A              
363D: 2D              DEC     L                   
363E: 7E              LD      A,(HL)              
363F: C6 20           ADD     $20                 
3641: 77              LD      (HL),A              
3642: D2 48 36        JP      NC,$3648            ; {}
3645: 2D              DEC     L                   
3646: 34              INC     (HL)                
3647: 2C              INC     L                   
3648: 2C              INC     L                   
3649: 2C              INC     L                   
364A: 2C              INC     L                   
364B: 7E              LD      A,(HL)              
364C: 2C              INC     L                   
364D: 2C              INC     L                   
364E: 96              SUB     (HL)                
364F: 0F              RRCA                        
3650: 0F              RRCA                        
3651: 0F              RRCA                        
3652: E6 1F           AND     $1F                 
3654: B8              CP      B                   
3655: 3C              INC     A                   
3656: 2D              DEC     L                   
3657: DA 63 36        JP      C,$3663             ; {}
365A: 3A 6E 43        LD      A,($436E)           
365D: B8              CP      B                   
365E: CA 63 36        JP      Z,$3663             ; {}
3661: 78              LD      A,B                 
3662: 3C              INC     A                   
3663: F6 10           OR      $10                 
3665: 77              LD      (HL),A              
3666: C9              RET                         
3667: 77              LD      (HL),A              
3668: C9              RET                         
3669: FF              RST     0X38                
366A: 78              LD      A,B                 
366B: A7              AND     A                   
366C: C0              RET     NZ                  
366D: 2C              INC     L                   
366E: 2C              INC     L                   
366F: 2C              INC     L                   
3670: 34              INC     (HL)                
3671: C9              RET                         
3672: 2D              DEC     L                   
3673: 46              LD      B,(HL)              
3674: 2C              INC     L                   
3675: 2C              INC     L                   
3676: 3A C2 43        LD      A,($43C2)           
3679: E6 F8           AND     $F8                 
367B: B8              CP      B                   
367C: D2 80 36        JP      NC,$3680            ; {}
367F: 47              LD      B,A                 
3680: 3A 6D 43        LD      A,($436D)           
3683: 4F              LD      C,A                 
3684: C6 08           ADD     $08                 
3686: 32 6D 43        LD      ($436D),A           
3689: 78              LD      A,B                 
368A: 91              SUB     C                   
368B: 36 08           LD      (HL),$08            
368D: D8              RET     C                   
368E: FE 08           CP      $08                 
3690: D8              RET     C                   
3691: 77              LD      (HL),A              
3692: C9              RET                         
3693: D8              RET     C                   
3694: FE 2C           CP      $2C                 
3696: 2C              INC     L                   
3697: 46              LD      B,(HL)              
3698: 2C              INC     L                   
3699: 2C              INC     L                   
369A: 7E              LD      A,(HL)              
369B: B8              CP      B                   
369C: C0              RET     NZ                  
369D: 2D              DEC     L                   
369E: 36 00           LD      (HL),$00            
36A0: 2C              INC     L                   
36A1: 3A C2 43        LD      A,($43C2)           
36A4: E6 F8           AND     $F8                 
36A6: B8              CP      B                   
36A7: DA AB 36        JP      C,$36AB             ; {}
36AA: 47              LD      B,A                 
36AB: 3A 6D 43        LD      A,($436D)           
36AE: C6 08           ADD     $08                 
36B0: 32 6D 43        LD      ($436D),A           
36B3: 80              ADD     A,B                 
36B4: 36 C8           LD      (HL),$C8            
36B6: D8              RET     C                   
36B7: FE C8           CP      $C8                 
36B9: D0              RET     NC                  
36BA: 77              LD      (HL),A              
36BB: C9              RET                         
36BC: 77              LD      (HL),A              
36BD: C9              RET                         
36BE: FF              RST     0X38                
36BF: FF              RST     0X38                
36C0: 7E              LD      A,(HL)              
36C1: 0F              RRCA                        
36C2: D8              RET     C                   
36C3: 2D              DEC     L                   
36C4: 7E              LD      A,(HL)              
36C5: 3C              INC     A                   
36C6: E6 07           AND     $07                 
36C8: 77              LD      (HL),A              
36C9: C9              RET                         
36CA: FF              RST     0X38                
36CB: FF              RST     0X38                
36CC: D1              POP     DE                  
36CD: C1              POP     BC                  
36CE: E1              POP     HL                  
36CF: C9              RET                         
36D0: FF              RST     0X38                
36D1: FF              RST     0X38                
36D2: D1              POP     DE                  
36D3: C1              POP     BC                  
36D4: E1              POP     HL                  
36D5: 7E              LD      A,(HL)              
36D6: A7              AND     A                   
36D7: C0              RET     NZ                  
36D8: 70              LD      (HL),B              
36D9: 2D              DEC     L                   
36DA: 2D              DEC     L                   
36DB: 2D              DEC     L                   
36DC: 2D              DEC     L                   
36DD: 72              LD      (HL),D              
36DE: 3A 68 43        LD      A,($4368)           
36E1: F6 01           OR      $01                 
36E3: 32 68 43        LD      ($4368),A           
36E6: C9              RET                         
36E7: FF              RST     0X38                
36E8: FF              RST     0X38                
36E9: FF              RST     0X38                
36EA: D1              POP     DE                  
36EB: C1              POP     BC                  
36EC: E1              POP     HL                  
36ED: 7E              LD      A,(HL)              
36EE: A7              AND     A                   
36EF: C0              RET     NZ                  
36F0: 2C              INC     L                   
36F1: 2C              INC     L                   
36F2: 7E              LD      A,(HL)              
36F3: E6 0F           AND     $0F                 
36F5: C0              RET     NZ                  
36F6: 2D              DEC     L                   
36F7: 2D              DEC     L                   
36F8: 70              LD      (HL),B              
36F9: 2D              DEC     L                   
36FA: 2D              DEC     L                   
36FB: 2D              DEC     L                   
36FC: 2D              DEC     L                   
36FD: 72              LD      (HL),D              
36FE: 3A 68 43        LD      A,($4368)           
3701: F6 02           OR      $02                 
3703: 32 68 43        LD      ($4368),A           
3706: C9              RET                         
3707: FF              RST     0X38                
3708: FF              RST     0X38                
3709: FF              RST     0X38                
370A: D1              POP     DE                  
370B: C1              POP     BC                  
370C: E1              POP     HL                  
370D: 7E              LD      A,(HL)              
370E: A7              AND     A                   
370F: C0              RET     NZ                  
3710: 2C              INC     L                   
3711: 2C              INC     L                   
3712: 7E              LD      A,(HL)              
3713: E6 0F           AND     $0F                 
3715: C0              RET     NZ                  
3716: 2D              DEC     L                   
3717: 2D              DEC     L                   
3718: 70              LD      (HL),B              
3719: 2D              DEC     L                   
371A: 2D              DEC     L                   
371B: 2D              DEC     L                   
371C: 2D              DEC     L                   
371D: 72              LD      (HL),D              
371E: 3A 68 43        LD      A,($4368)           
3721: F6 04           OR      $04                 
3723: 32 68 43        LD      ($4368),A           
3726: 3A 6F 43        LD      A,($436F)           
3729: A3              AND     E                   
372A: E6 F0           AND     $F0                 
372C: C0              RET     NZ                  
372D: 7B              LD      A,E                 
372E: E6 0F           AND     $0F                 
3730: 77              LD      (HL),A              
3731: 2C              INC     L                   
3732: 2C              INC     L                   
3733: 2C              INC     L                   
3734: 2C              INC     L                   
3735: 71              LD      (HL),C              
3736: 3A 68 43        LD      A,($4368)           
3739: F6 08           OR      $08                 
373B: 32 68 43        LD      ($4368),A           
373E: C9              RET                         
373F: FF              RST     0X38                
3740: FF              RST     0X38                
3741: FF              RST     0X38                
3742: FF              RST     0X38                
3743: FF              RST     0X38                
3744: 36 11           LD      (HL),$11            
3746: 2D              DEC     L                   
3747: 35              DEC     (HL)                
3748: 2D              DEC     L                   
3749: 2D              DEC     L                   
374A: 36 07           LD      (HL),$07            
374C: 2D              DEC     L                   
374D: 7E              LD      A,(HL)              
374E: C6 20           ADD     $20                 
3750: 77              LD      (HL),A              
3751: D0              RET     NC                  
3752: 2D              DEC     L                   
3753: 34              INC     (HL)                
3754: C9              RET                         
3755: FF              RST     0X38                
3756: FF              RST     0X38                
3757: FF              RST     0X38                
3758: 7E              LD      A,(HL)              
3759: A7              AND     A                   
375A: C8              RET     Z                   
375B: 35              DEC     (HL)                
375C: CA CC 37        JP      Z,$37CC             ; {}
375F: 7E              LD      A,(HL)              
3760: 0F              RRCA                        
3761: D2 B0 37        JP      NC,$37B0            ; {}
3764: 3E 0F           LD      A,$0F               
3766: 96              SUB     (HL)                
3767: E6 0E           AND     $0E                 
3769: 07              RLCA                        
376A: 07              RLCA                        
376B: 07              RLCA                        
376C: 07              RLCA                        
376D: 2C              INC     L                   
376E: 2C              INC     L                   
376F: 56              LD      D,(HL)              
3770: 2C              INC     L                   
3771: 5E              LD      E,(HL)              
3772: F5              PUSH    AF                  
3773: D5              PUSH    DE                  
3774: 01 DF FF        LD      BC,$FFDF            
3777: CD 96 37        CALL    $3796               ; {}
377A: D1              POP     DE                  
377B: F1              POP     AF                  
377C: 2F              CPL                         
377D: 6F              LD      L,A                 
377E: 26 FF           LD      H,$FF               
3780: 23              INC     HL                  
3781: 19              ADD     HL,DE               
3782: EB              EX      DE,HL               
3783: 21 A0 BF        LD      HL,$BFA0            
3786: 19              ADD     HL,DE               
3787: D0              RET     NC                  
3788: EB              EX      DE,HL               
3789: 11 D6 17        LD      DE,$17D6            
378C: 36 00           LD      (HL),$00            
378E: 23              INC     HL                  
378F: 36 00           LD      (HL),$00            
3791: 09              ADD     HL,BC               
3792: C3 40 35        JP      $3540               ; {}
3795: FF              RST     0X38                
3796: C6 60           ADD     $60                 
3798: 6F              LD      L,A                 
3799: 26 00           LD      H,$00               
379B: D2 9F 37        JP      NC,$379F            ; {}
379E: 24              INC     H                   
379F: 19              ADD     HL,DE               
37A0: EB              EX      DE,HL               
37A1: 21 C0 BC        LD      HL,$BCC0            
37A4: 19              ADD     HL,DE               
37A5: D8              RET     C                   
37A6: EB              EX      DE,HL               
37A7: 11 D0 17        LD      DE,$17D0            
37AA: C3 40 35        JP      $3540               ; {}
37AD: FF              RST     0X38                
37AE: FF              RST     0X38                
37AF: FF              RST     0X38                
37B0: 2C              INC     L                   
37B1: 7E              LD      A,(HL)              
37B2: 27              DAA                         
37B3: 77              LD      (HL),A              
37B4: 2C              INC     L                   
37B5: 56              LD      D,(HL)              
37B6: 2C              INC     L                   
37B7: 5E              LD      E,(HL)              
37B8: 2D              DEC     L                   
37B9: 2D              DEC     L                   
37BA: 00              NOP                         
37BB: CD 17 02        CALL    $0217               ; {code.SubtractOneRow}
37BE: 3E 20           LD      A,$20               
37C0: 12              LD      (DE),A              
37C1: CD 10 02        CALL    $0210               ; {code.AddOneRow}
37C4: 06 02           LD      B,$02               
37C6: C3 C4 00        JP      $00C4               ; {}
37C9: FF              RST     0X38                
37CA: FF              RST     0X38                
37CB: FF              RST     0X38                
37CC: 2C              INC     L                   
37CD: 2C              INC     L                   
37CE: 2C              INC     L                   
37CF: 7E              LD      A,(HL)              
37D0: E6 1F           AND     $1F                 
37D2: C6 20           ADD     $20                 
37D4: 6F              LD      L,A                 
37D5: 26 43           LD      H,$43               
37D7: 01 DF FF        LD      BC,$FFDF            
37DA: 11 1A 00        LD      DE,$001A            
37DD: 72              LD      (HL),D              
37DE: 23              INC     HL                  
37DF: 72              LD      (HL),D              
37E0: 09              ADD     HL,BC               
37E1: 1D              DEC     E                   
37E2: C2 DD 37        JP      NZ,$37DD            ; {}
37E5: C9              RET                         
37E6: FF              RST     0X38                
37E7: FF              RST     0X38                
37E8: FF              RST     0X38                
37E9: FF              RST     0X38                
37EA: FF              RST     0X38                
37EB: FF              RST     0X38                
37EC: FF              RST     0X38                
37ED: FF              RST     0X38                
37EE: FF              RST     0X38                
37EF: FF              RST     0X38                
37F0: FF              RST     0X38                
37F1: FF              RST     0X38                
37F2: FF              RST     0X38                
37F3: FF              RST     0X38                
37F4: FF              RST     0X38                
37F5: FF              RST     0X38                
37F6: FF              RST     0X38                
37F7: FF              RST     0X38                
37F8: FF              RST     0X38                
37F9: FF              RST     0X38                
37FA: FF              RST     0X38                
37FB: FF              RST     0X38                
37FC: FF              RST     0X38                
37FD: FF              RST     0X38                
37FE: FF              RST     0X38                
37FF: FF              RST     0X38                
3800: 3A C4 43        LD      A,($43C4)           
3803: E6 08           AND     $08                 
3805: C8              RET     Z                   
3806: 3A E6 43        LD      A,($43E6)           
3809: C6 08           ADD     $08                 
380B: 57              LD      D,A                 
380C: 3A D2 4B        LD      A,($4BD2)           
380F: 5F              LD      E,A                 
3810: 3A E7 43        LD      A,($43E7)           
3813: E6 E0           AND     $E0                 
3815: 47              LD      B,A                 
3816: 3A E7 43        LD      A,($43E7)           
3819: 93              SUB     E                   
381A: 00              NOP                         
381B: E6 1F           AND     $1F                 
381D: B0              OR      B                   
381E: 5F              LD      E,A                 
381F: 1A              LD      A,(DE)              
3820: D6 90           SUB     $90                 
3822: D8              RET     C                   
3823: 47              LD      B,A                 
3824: 3A C6 43        LD      A,($43C6)           
3827: E6 07           AND     $07                 
3829: C6 00           ADD     $00                 
382B: 6F              LD      L,A                 
382C: 26 3E           LD      H,$3E               
382E: 4E              LD      C,(HL)              
382F: 7B              LD      A,E                 
3830: E6 0E           AND     $0E                 
3832: 07              RLCA                        
3833: 07              RLCA                        
3834: 5F              LD      E,A                 
3835: 3E A8           LD      A,$A8               
3837: 93              SUB     E                   
3838: 5F              LD      E,A                 
3839: 16 4B           LD      D,$4B               
383B: 78              LD      A,B                 
383C: FE 50           CP      $50                 
383E: DC 44 38        CALL    C,$3844             ; {}
3841: C3 1C 39        JP      $391C               ; {}
3844: C6 60           ADD     $60                 
3846: 6F              LD      L,A                 
3847: 26 3B           LD      H,$3B               
3849: 7E              LD      A,(HL)              
384A: A1              AND     C                   
384B: C8              RET     Z                   
384C: CD A1 38        CALL    $38A1               ; {}
384F: EB              EX      DE,HL               
3850: 7E              LD      A,(HL)              
3851: 36 00           LD      (HL),$00            
3853: 2C              INC     L                   
3854: 2C              INC     L                   
3855: 2C              INC     L                   
3856: 2C              INC     L                   
3857: 56              LD      D,(HL)              
3858: E1              POP     HL                  
3859: 21 BB 43        LD      HL,$43BB            
385C: 35              DEC     (HL)                
385D: FE 0B           CP      $0B                 
385F: DA 94 38        JP      C,$3894             ; {}
3862: 5F              LD      E,A                 
3863: 3E FF           LD      A,$FF               
3865: 32 69 43        LD      ($4369),A           
3868: 21 78 43        LD      HL,$4378            
386B: 01 10 10        LD      BC,$1010            
386E: 7B              LD      A,E                 
386F: FE 0F           CP      $0F                 
3871: CA FB 38        JP      Z,$38FB             ; {}
3874: 7A              LD      A,D                 
3875: 0F              RRCA                        
3876: E6 7C           AND     $7C                 
3878: C6 30           ADD     $30                 
387A: 4F              LD      C,A                 
387B: 7B              LD      A,E                 
387C: FE 0E           CP      $0E                 
387E: CA FB 38        JP      Z,$38FB             ; {}
3881: 79              LD      A,C                 
3882: 0F              RRCA                        
3883: 4F              LD      C,A                 
3884: 7B              LD      A,E                 
3885: FE 0C           CP      $0C                 
3887: D2 FB 38        JP      NC,$38FB            ; {}
388A: 79              LD      A,C                 
388B: 0F              RRCA                        
388C: 4F              LD      C,A                 
388D: C3 FB 38        JP      $38FB               ; {}
3890: FF              RST     0X38                
3891: FF              RST     0X38                
3892: FF              RST     0X38                
3893: FF              RST     0X38                
3894: 01 05 0D        LD      BC,$0D05            
3897: 3E FF           LD      A,$FF               
3899: 32 64 43        LD      ($4364),A           
389C: C3 F8 38        JP      $38F8               ; {}
389F: FF              RST     0X38                
38A0: FF              RST     0X38                
38A1: D5              PUSH    DE                  
38A2: 0E 20           LD      C,$20               
38A4: EB              EX      DE,HL               
38A5: 23              INC     HL                  
38A6: 56              LD      D,(HL)              
38A7: 23              INC     HL                  
38A8: 5E              LD      E,(HL)              
38A9: 3A 8C 19        LD      A,($198C)           ; {}
38AC: C6 DE           ADD     $DE                 
38AE: 6F              LD      L,A                 
38AF: 26 17           LD      H,$17               
38B1: CD DE 34        CALL    $34DE               ; {}
38B4: D1              POP     DE                  
38B5: C9              RET                         
38B6: 35              DEC     (HL)                
38B7: D1              POP     DE                  
38B8: C9              RET                         
38B9: FF              RST     0X38                
38BA: FF              RST     0X38                
38BB: FF              RST     0X38                
38BC: C6 B0           ADD     $B0                 
38BE: 6F              LD      L,A                 
38BF: 26 3B           LD      H,$3B               
38C1: 7E              LD      A,(HL)              
38C2: A1              AND     C                   
38C3: C8              RET     Z                   
38C4: CD A1 38        CALL    $38A1               ; {}
38C7: 1A              LD      A,(DE)              
38C8: D6 0B           SUB     $0B                 
38CA: DA E9 38        JP      C,$38E9             ; {}
38CD: FE 03           CP      $03                 
38CF: D2 E9 38        JP      NC,$38E9            ; {}
38D2: 47              LD      B,A                 
38D3: 62              LD      H,D                 
38D4: 7B              LD      A,E                 
38D5: C6 05           ADD     $05                 
38D7: 6F              LD      L,A                 
38D8: 3A C6 43        LD      A,($43C6)           
38DB: BE              CP      (HL)                
38DC: 17              RLA                         
38DD: 07              RLCA                        
38DE: 07              RLCA                        
38DF: E6 04           AND     $04                 
38E1: B0              OR      B                   
38E2: C6 B8           ADD     $B8                 
38E4: 6F              LD      L,A                 
38E5: 26 3D           LD      H,$3D               
38E7: 7E              LD      A,(HL)              
38E8: 12              LD      (DE),A              
38E9: 3E FF           LD      A,$FF               
38EB: 32 66 43        LD      ($4366),A           
38EE: 01 02 07        LD      BC,$0702            
38F1: C3 F8 38        JP      $38F8               ; {}
38F4: FF              RST     0X38                
38F5: FF              RST     0X38                
38F6: FF              RST     0X38                
38F7: FF              RST     0X38                
38F8: 21 70 43        LD      HL,$4370            
38FB: AF              XOR     A                   
38FC: BE              CP      (HL)                
38FD: CA 06 39        JP      Z,$3906             ; {}
3900: 2C              INC     L                   
3901: 2C              INC     L                   
3902: 2C              INC     L                   
3903: 2C              INC     L                   
3904: BE              CP      (HL)                
3905: C0              RET     NZ                  
3906: 70              LD      (HL),B              
3907: 2C              INC     L                   
3908: 71              LD      (HL),C              
3909: 2C              INC     L                   
390A: 3A E6 43        LD      A,($43E6)           
390D: 77              LD      (HL),A              
390E: 2C              INC     L                   
390F: 3A E7 43        LD      A,($43E7)           
3912: 77              LD      (HL),A              
3913: 3A C4 43        LD      A,($43C4)           
3916: E6 F7           AND     $F7                 
3918: 32 C4 43        LD      ($43C4),A           
391B: C9              RET                         
391C: 78              LD      A,B                 
391D: FE 20           CP      $20                 
391F: D2 BC 38        JP      NC,$38BC            ; {}
3922: C9              RET                         
3923: C8              RET     Z                   
3924: 35              DEC     (HL)                
3925: 2E 8D           LD      L,$8D               
3927: 7E              LD      A,(HL)              
3928: E6 3F           AND     $3F                 
392A: F6 80           OR      $80                 
392C: 77              LD      (HL),A              
392D: C9              RET                         
392E: C9              RET                         
392F: FF              RST     0X38                
3930: 3A D2 4B        LD      A,($4BD2)           
3933: E6 1E           AND     $1E                 
3935: C6 C0           ADD     $C0                 
3937: 6F              LD      L,A                 
3938: 26 3D           LD      H,$3D               
393A: 5E              LD      E,(HL)              
393B: 2C              INC     L                   
393C: 6E              LD      L,(HL)              
393D: 26 4B           LD      H,$4B               
393F: CD 00 3A        CALL    $3A00               ; {}
3942: 3A 9F 43        LD      A,($439F)           
3945: 82              ADD     A,D                 
3946: 4F              LD      C,A                 
3947: 3A 9E 43        LD      A,($439E)           
394A: 92              SUB     D                   
394B: 47              LD      B,A                 
394C: E5              PUSH    HL                  
394D: CD 5C 39        CALL    $395C               ; {}
3950: E1              POP     HL                  
3951: 7D              LD      A,L                 
3952: C6 08           ADD     $08                 
3954: 6F              LD      L,A                 
3955: 1D              DEC     E                   
3956: C2 4C 39        JP      NZ,$394C            ; {}
3959: C9              RET                         
395A: FF              RST     0X38                
395B: FF              RST     0X38                
395C: 7E              LD      A,(HL)              
395D: FE 05           CP      $05                 
395F: D8              RET     C                   
3960: 7D              LD      A,L                 
3961: C6 05           ADD     $05                 
3963: 6F              LD      L,A                 
3964: 7E              LD      A,(HL)              
3965: B8              CP      B                   
3966: D8              RET     C                   
3967: B9              CP      C                   
3968: D0              RET     NC                  
3969: D6 04           SUB     $04                 
396B: 47              LD      B,A                 
396C: 2D              DEC     L                   
396D: 2D              DEC     L                   
396E: 2D              DEC     L                   
396F: 3A D2 4B        LD      A,($4BD2)           
3972: 86              ADD     A,(HL)              
3973: E6 1F           AND     $1F                 
3975: 07              RLCA                        
3976: 07              RLCA                        
3977: 07              RLCA                        
3978: C6 08           ADD     $08                 
397A: 4F              LD      C,A                 
397B: C3 B7 25        JP      $25B7               ; {}
397E: FF              RST     0X38                
397F: FF              RST     0X38                
3980: 3A D2 4B        LD      A,($4BD2)           
3983: D6 0C           SUB     $0C                 
3985: D8              RET     C                   
3986: FE 10           CP      $10                 
3988: D0              RET     NC                  
3989: 21 C4 43        LD      HL,$43C4            
398C: 11 C0 4B        LD      DE,$4BC0            
398F: 06 04           LD      B,$04               
3991: CD E0 05        CALL    $05E0               ; {}
3994: 2E E6           LD      L,$E6               
3996: 06 02           LD      B,$02               
3998: CD E0 05        CALL    $05E0               ; {}
399B: 2E E2           LD      L,$E2               
399D: 11 E6 43        LD      DE,$43E6            
39A0: 06 02           LD      B,$02               
39A2: CD E0 05        CALL    $05E0               ; {}
39A5: 2E C4           LD      L,$C4               
39A7: 36 08           LD      (HL),$08            
39A9: 11 9E 43        LD      DE,$439E            
39AC: 3A 9B 43        LD      A,($439B)           ; {ram.Counter+1}
39AF: 0F              RRCA                        
39B0: DA BF 39        JP      C,$39BF             ; {}
39B3: 1C              INC     E                   
39B4: 2E E7           LD      L,$E7               
39B6: 7E              LD      A,(HL)              
39B7: D6 20           SUB     $20                 
39B9: 77              LD      (HL),A              
39BA: 2D              DEC     L                   
39BB: 7E              LD      A,(HL)              
39BC: DE 00           SBC     $00                 
39BE: 77              LD      (HL),A              
39BF: 1A              LD      A,(DE)              
39C0: 32 C6 43        LD      ($43C6),A           
39C3: CD 00 38        CALL    $3800               ; {}
39C6: 21 C4 43        LD      HL,$43C4            
39C9: 7E              LD      A,(HL)              
39CA: E6 08           AND     $08                 
39CC: CA F0 39        JP      Z,$39F0             ; {}
39CF: 21 E7 43        LD      HL,$43E7            
39D2: 34              INC     (HL)                
39D3: 7E              LD      A,(HL)              
39D4: E6 1F           AND     $1F                 
39D6: FE 1D           CP      $1D                 
39D8: DA C3 39        JP      C,$39C3             ; {}
39DB: 21 C0 4B        LD      HL,$4BC0            
39DE: 11 C4 43        LD      DE,$43C4            
39E1: 06 04           LD      B,$04               
39E3: CD E0 05        CALL    $05E0               ; {}
39E6: 1E E6           LD      E,$E6               
39E8: 06 02           LD      B,$02               
39EA: C3 E0 05        JP      $05E0               ; {}
39ED: FF              RST     0X38                
39EE: FF              RST     0X38                
39EF: FF              RST     0X38                
39F0: 2E A6           LD      L,$A6               
39F2: 7E              LD      A,(HL)              
39F3: FE C0           CP      $C0                 
39F5: DA C4 0C        JP      C,$0CC4             ; {}
39F8: D6 01           SUB     $01                 
39FA: 77              LD      (HL),A              
39FB: C3 DB 39        JP      $39DB               ; {}
39FE: FF              RST     0X38                
39FF: FF              RST     0X38                
3A00: 3A BB 43        LD      A,($43BB)           
3A03: D6 0C           SUB     $0C                 
3A05: 2F              CPL                         
3A06: 3C              INC     A                   
3A07: 57              LD      D,A                 
3A08: 3A 9B 43        LD      A,($439B)           ; {ram.Counter+1}
3A0B: 0F              RRCA                        
3A0C: 0F              RRCA                        
3A0D: D8              RET     C                   
3A0E: E1              POP     HL                  
3A0F: C9              RET                         
3A10: 21 B8 43        LD      HL,$43B8            
3A13: 7E              LD      A,(HL)              
3A14: A7              AND     A                   
3A15: C2 43 3B        JP      NZ,$3B43            ; {}
3A18: 2E 8D           LD      L,$8D               
3A1A: 36 CF           LD      (HL),$CF            
3A1C: C9              RET                         
3A1D: 21 69 43        LD      HL,$4369            
3A20: 7E              LD      A,(HL)              
3A21: A7              AND     A                   
3A22: CA 40 3A        JP      Z,$3A40             ; {}
3A25: FE 20           CP      $20                 
3A27: DA 2C 3A        JP      C,$3A2C             ; {}
3A2A: 36 20           LD      (HL),$20            
3A2C: 35              DEC     (HL)                
3A2D: 7E              LD      A,(HL)              
3A2E: 07              RLCA                        
3A2F: 07              RLCA                        
3A30: 00              NOP                         
3A31: 2F              CPL                         
3A32: E6 0E           AND     $0E                 
3A34: 2E 8D           LD      L,$8D               
3A36: 77              LD      (HL),A              
3A37: 2E 68           LD      L,$68               
3A39: 36 00           LD      (HL),$00            
3A3B: 2E 66           LD      L,$66               
3A3D: 36 00           LD      (HL),$00            
3A3F: C9              RET                         
3A40: 2E 64           LD      L,$64               
3A42: 7E              LD      A,(HL)              
3A43: A7              AND     A                   
3A44: CA 62 3A        JP      Z,$3A62             ; {}
3A47: FE 10           CP      $10                 
3A49: DA 4E 3A        JP      C,$3A4E             ; {}
3A4C: 36 10           LD      (HL),$10            
3A4E: 35              DEC     (HL)                
3A4F: 7E              LD      A,(HL)              
3A50: 0F              RRCA                        
3A51: 00              NOP                         
3A52: 00              NOP                         
3A53: 2F              CPL                         
3A54: E6 07           AND     $07                 
3A56: F6 10           OR      $10                 
3A58: 2E 8C           LD      L,$8C               
3A5A: 77              LD      (HL),A              
3A5B: 2E 66           LD      L,$66               
3A5D: 36 00           LD      (HL),$00            
3A5F: C9              RET                         
3A60: 0F              RRCA                        
3A61: 00              NOP                         
3A62: 2E 66           LD      L,$66               
3A64: 7E              LD      A,(HL)              
3A65: A7              AND     A                   
3A66: C8              RET     Z                   
3A67: FE 10           CP      $10                 
3A69: DA 78 3A        JP      C,$3A78             ; {}
3A6C: 36 10           LD      (HL),$10            
3A6E: 3A B8 43        LD      A,($43B8)           
3A71: E6 08           AND     $08                 
3A73: CA 78 3A        JP      Z,$3A78             ; {}
3A76: 36 05           LD      (HL),$05            
3A78: 35              DEC     (HL)                
3A79: 2E 8C           LD      L,$8C               
3A7B: 7E              LD      A,(HL)              
3A7C: E6 08           AND     $08                 
3A7E: F6 04           OR      $04                 
3A80: 77              LD      (HL),A              
3A81: C9              RET                         
3A82: 21 9A 43        LD      HL,$439A            
3A85: 7E              LD      A,(HL)              
3A86: FE 03           CP      $03                 
3A88: D8              RET     C                   
3A89: 2E 8D           LD      L,$8D               
3A8B: 7E              LD      A,(HL)              
3A8C: E6 3F           AND     $3F                 
3A8E: 77              LD      (HL),A              
3A8F: C9              RET                         
3A90: 21 6B 43        LD      HL,$436B            
3A93: 7E              LD      A,(HL)              
3A94: A7              AND     A                   
3A95: C3 23 39        JP      $3923               ; {}
3A98: 21 70 4B        LD      HL,$4B70            
3A9B: 01 00 08        LD      BC,$0800            
3A9E: 11 B0 03        LD      DE,$03B0            
3AA1: 7E              LD      A,(HL)              
3AA2: 2C              INC     L                   
3AA3: A0              AND     B                   
3AA4: CA AE 3A        JP      Z,$3AAE             ; {}
3AA7: 7E              LD      A,(HL)              
3AA8: FE 28           CP      $28                 
3AAA: DA AE 3A        JP      C,$3AAE             ; {}
3AAD: 0C              INC     C                   
3AAE: 7D              LD      A,L                 
3AAF: 82              ADD     A,D                 
3AB0: 6F              LD      L,A                 
3AB1: BB              CP      E                   
3AB2: C2 A1 3A        JP      NZ,$3AA1            ; {}
3AB5: 79              LD      A,C                 
3AB6: A7              AND     A                   
3AB7: C8              RET     Z                   
3AB8: FE 08           CP      $08                 
3ABA: DA BF 3A        JP      C,$3ABF             ; {}
3ABD: 3E 08           LD      A,$08               
3ABF: C6 25           ADD     $25                 
3AC1: 4F              LD      C,A                 
3AC2: 21 8C 43        LD      HL,$438C            
3AC5: 7E              LD      A,(HL)              
3AC6: E6 C0           AND     $C0                 
3AC8: B1              OR      C                   
3AC9: 77              LD      (HL),A              
3ACA: C9              RET                         

3ACB: FF              RST     0X38                
3ACC: FF              RST     0X38                
3ACD: FF              RST     0X38                
3ACE: FF              RST     0X38                
3ACF: FF              RST     0X38                
3AD0: 21 8E 43        LD      HL,$438E            
3AD3: 7E              LD      A,(HL)              
3AD4: E6 01           AND     $01                 
3AD6: 07              RLCA                        
3AD7: 07              RLCA                        
3AD8: F6 20           OR      $20                 
3ADA: 47              LD      B,A                 
3ADB: 2D              DEC     L                   
3ADC: 7E              LD      A,(HL)              
3ADD: E6 C0           AND     $C0                 
3ADF: B0              OR      B                   
3AE0: 77              LD      (HL),A              
3AE1: 2E 96           LD      L,$96               
3AE3: 7E              LD      A,(HL)              
3AE4: 34              INC     (HL)                
3AE5: A7              AND     A                   
3AE6: CA F8 3A        JP      Z,$3AF8             ; {}
3AE9: 3A D6 4B        LD      A,($4BD6)           
3AEC: C6 E0           ADD     $E0                 
3AEE: 5F              LD      E,A                 
3AEF: 16 3D           LD      D,$3D               
3AF1: 1A              LD      A,(DE)              
3AF2: BE              CP      (HL)                
3AF3: D0              RET     NC                  
3AF4: 36 00           LD      (HL),$00            
3AF6: C9              RET                         
3AF7: 5F              LD      E,A                 
3AF8: 2E 8E           LD      L,$8E               
3AFA: 34              INC     (HL)                
3AFB: 2D              DEC     L                   
3AFC: 7E              LD      A,(HL)              
3AFD: F6 10           OR      $10                 
3AFF: 77              LD      (HL),A              
3B00: C9              RET                         
3B01: 8E              ADC     A,(HL)              
3B02: 21 9A 43        LD      HL,$439A            
3B05: 7E              LD      A,(HL)              
3B06: FE 02           CP      $02                 
3B08: D0              RET     NC                  
3B09: 2C              INC     L                   
3B0A: 7E              LD      A,(HL)              
3B0B: 47              LD      B,A                 
3B0C: E6 60           AND     $60                 
3B0E: 2E 8D           LD      L,$8D               
3B10: 36 0A           LD      (HL),$0A            
3B12: C0              RET     NZ                  
3B13: 78              LD      A,B                 
3B14: E6 02           AND     $02                 
3B16: C6 1C           ADD     $1C                 
3B18: 77              LD      (HL),A              
3B19: C9              RET                         
3B1A: 78              LD      A,B                 
3B1B: 21 62 43        LD      HL,$4362            
3B1E: 7E              LD      A,(HL)              
3B1F: A7              AND     A                   
3B20: C8              RET     Z                   
3B21: FE 40           CP      $40                 
3B23: DA 28 3B        JP      C,$3B28             ; {}
3B26: 36 40           LD      (HL),$40            
3B28: 35              DEC     (HL)                
3B29: 7E              LD      A,(HL)              
3B2A: E6 06           AND     $06                 
3B2C: 07              RLCA                        
3B2D: 00              NOP                         
3B2E: 2E 8D           LD      L,$8D               
3B30: 77              LD      (HL),A              
3B31: C9              RET                         
3B32: FF              RST     0X38                
3B33: 21 6A 43        LD      HL,$436A            
3B36: 7E              LD      A,(HL)              
3B37: A7              AND     A                   
3B38: C8              RET     Z                   
3B39: 35              DEC     (HL)                
3B3A: E6 08           AND     $08                 
3B3C: F6 07           OR      $07                 
3B3E: 2E 8D           LD      L,$8D               
3B40: 77              LD      (HL),A              
3B41: C9              RET                         
3B42: 8D              ADC     A,L                 
3B43: 21 A4 43        LD      HL,$43A4            
3B46: 7E              LD      A,(HL)              
3B47: FE 03           CP      $03                 
3B49: CC D6 23        CALL    Z,$23D6             ; {}
3B4C: CD 33 3B        CALL    $3B33               ; {}
3B4F: CD 1B 3B        CALL    $3B1B               ; {}
3B52: CD 1D 3A        CALL    $3A1D               ; {}
3B55: CD BD 27        CALL    $27BD               ; {}
3B58: CD 82 3A        CALL    $3A82               ; {}
3B5B: C3 90 3A        JP      $3A90               ; {}
3B5E: FF              RST     0X38                
3B5F: FF              RST     0X38                
3B60: 1F              RRA                         
3B61: 7C              LD      A,H                 
3B62: F0              RET     P                   
3B63: 01 C0 07        LD      BC,$07C0            
3B66: 7F              LD      A,A                 
3B67: FC F0 07        CALL    M,$07F0             ; {}
3B6A: C0              RET     NZ                  
3B6B: 1F              RRA                         
3B6C: FF              RST     0X38                
3B6D: FC 03 F0        CALL    M,$F003             
3B70: 0F              RRCA                        
3B71: C0              RET     NZ                  
3B72: 3F              CCF                         
3B73: FC 1F F0        CALL    M,$F01F             
3B76: 07              RLCA                        
3B77: FE 3F           CP      $3F                 
3B79: F8              RET     M                   
3B7A: 0F              RRCA                        
3B7B: FF              RST     0X38                
3B7C: FF              RST     0X38                
3B7D: FC 1F FF        CALL    M,$FF1F             
3B80: FC 1F FC        CALL    M,$FC1F             
3B83: 1F              RRA                         
3B84: F0              RET     P                   
3B85: 7F              LD      A,A                 
3B86: F0              RET     P                   
3B87: 7F              LD      A,A                 
3B88: C0              RET     NZ                  
3B89: FF              RST     0X38                
3B8A: 01 C0 FF        LD      BC,$FFC0            
3B8D: 01 00 FF        LD      BC,$FF00            
3B90: 07              RLCA                        
3B91: 00              NOP                         
3B92: FF              RST     0X38                
3B93: 07              RLCA                        
3B94: FC 1F FC        CALL    M,$FC1F             
3B97: 1F              RRA                         
3B98: F0              RET     P                   
3B99: 7F              LD      A,A                 
3B9A: F0              RET     P                   
3B9B: 7F              LD      A,A                 
3B9C: C0              RET     NZ                  
3B9D: FF              RST     0X38                
3B9E: 01 C0 FF        LD      BC,$FFC0            
3BA1: 01 00 FF        LD      BC,$FF00            
3BA4: 07              RLCA                        
3BA5: FF              RST     0X38                
3BA6: 07              RLCA                        
3BA7: FC 1F F8        CALL    M,$F81F             
3BAA: 0F              RRCA                        
3BAB: F0              RET     P                   
3BAC: C0              RET     NZ                  
3BAD: 03              INC     BC                  
3BAE: FF              RST     0X38                
3BAF: FF              RST     0X38                
3BB0: 03              INC     BC                  
3BB1: E0              RET     PO                  
3BB2: 03              INC     BC                  
3BB3: E0              RET     PO                  
3BB4: 0F              RRCA                        
3BB5: 80              ADD     A,B                 
3BB6: 0F              RRCA                        
3BB7: 00              NOP                         
3BB8: 3C              INC     A                   
3BB9: 00              NOP                         
3BBA: 1E 3F           LD      E,$3F               
3BBC: 00              NOP                         
3BBD: FC F0 00        CALL    M,$00F0             ; {}
3BC0: 7F              LD      A,A                 
3BC1: FE 00           CP      $00                 
3BC3: F0              RET     P                   
3BC4: 03              INC     BC                  
3BC5: E0              RET     PO                  
3BC6: 00              NOP                         
3BC7: 00              NOP                         
3BC8: 0F              RRCA                        
3BC9: 80              ADD     A,B                 
3BCA: 00              NOP                         
3BCB: 00              NOP                         
3BCC: 3F              CCF                         
3BCD: 00              NOP                         
3BCE: FE 30           CP      $30                 
3BD0: 00              NOP                         
3BD1: 06 FF           LD      B,$FF               
3BD3: 00              NOP                         
3BD4: F8              RET     M                   
3BD5: 00              NOP                         
3BD6: 00              NOP                         
3BD7: 03              INC     BC                  
3BD8: E0              RET     PO                  
3BD9: 00              NOP                         
3BDA: E0              RET     PO                  
3BDB: 08              EX      AF,AF'              
3BDC: 20 04           JR      NZ,$3BE2            ; {}
3BDE: C0              RET     NZ                  
3BDF: 01 E0 03        LD      BC,$03E0            
3BE2: F8              RET     M                   
3BE3: 0F              RRCA                        
3BE4: 07              RLCA                        
3BE5: E0              RET     PO                  
3BE6: 3F              CCF                         
3BE7: 03              INC     BC                  
3BE8: FF              RST     0X38                
3BE9: FF              RST     0X38                
3BEA: FF              RST     0X38                
3BEB: 3F              CCF                         
3BEC: FC FF F8        CALL    M,$F8FF             
3BEF: FF              RST     0X38                
3BF0: FF              RST     0X38                
3BF1: 07              RLCA                        
3BF2: E0              RET     PO                  
3BF3: 1F              RRA                         
3BF4: F0              RET     P                   
3BF5: FF              RST     0X38                
3BF6: FC FF 07        CALL    M,$07FF             ; {}
3BF9: 1E FC           LD      E,$FC               
3BFB: 1F              RRA                         
3BFC: 1F              RRA                         
3BFD: 7F              LD      A,A                 
3BFE: FF              RST     0X38                
3BFF: FF              RST     0X38                
3C00: E8              RET     PE                  
3C01: 00              NOP                         
3C02: E9              JP      (HL)                
3C03: 00              NOP                         
3C04: C4 C6 C5        CALL    NZ,$C5C6            
3C07: C7              RST     0X00                
3C08: EA 00 EB        JP      PE,$EB00            
3C0B: 00              NOP                         
3C0C: 00              NOP                         
3C0D: 00              NOP                         
3C0E: EC 00 E9        CALL    PE,$E900            
3C11: 00              NOP                         
3C12: C8              RET     Z                   
3C13: CA C9 CB        JP      Z,$CBC9             
3C16: EA 00 ED        JP      PE,$ED00            
3C19: 00              NOP                         
3C1A: 00              NOP                         
3C1B: 00              NOP                         
3C1C: EE 00           XOR     $00                 
3C1E: EF              RST     0X28                
3C1F: 00              NOP                         
3C20: CC CF CD        CALL    Z,$CDCF             
3C23: D0              RET     NC                  
3C24: CE D1           ADC     $D1                 
3C26: F0              RET     P                   
3C27: 00              NOP                         
3C28: F1              POP     AF                  
3C29: 00              NOP                         
3C2A: F2 00 EF        JP      P,$EF00             
3C2D: 00              NOP                         
3C2E: D2 00 D3        JP      NC,$D300            
3C31: D5              PUSH    DE                  
3C32: D4 D6 F0        CALL    NC,$F0D6            
3C35: 00              NOP                         
3C36: F3              DI                          
3C37: 00              NOP                         
3C38: E8              RET     PE                  
3C39: 00              NOP                         
3C3A: E9              JP      (HL)                
3C3B: 00              NOP                         
3C3C: C4 C6 C5        CALL    NZ,$C5C6            
3C3F: C7              RST     0X00                
3C40: 00              NOP                         
3C41: 00              NOP                         
3C42: EC 00 E9        CALL    PE,$E900            
3C45: 00              NOP                         
3C46: C8              RET     Z                   
3C47: CA C9 CB        JP      Z,$CBC9             
3C4A: 00              NOP                         
3C4B: 00              NOP                         
3C4C: EE 00           XOR     $00                 
3C4E: EF              RST     0X28                
3C4F: 00              NOP                         
3C50: CC CF CD        CALL    Z,$CDCF             
3C53: D0              RET     NC                  
3C54: DD 
3C55: D1              POP     DE                  
3C56: F2 00 EF        JP      P,$EF00             
3C59: 00              NOP                         
3C5A: D2 00 D3        JP      NC,$D300            
3C5D: D5              PUSH    DE                  
3C5E: DD 
3C5F: D6 00           SUB     $00                 
3C61: 00              NOP                         
3C62: 00              NOP                         
3C63: 00              NOP                         
3C64: C4 C6 C5        CALL    NZ,$C5C6            
3C67: C7              RST     0X00                
3C68: EA 00 EB        JP      PE,$EB00            
3C6B: 00              NOP                         
3C6C: 00              NOP                         
3C6D: 00              NOP                         
3C6E: 00              NOP                         
3C6F: 00              NOP                         
3C70: 00              NOP                         
3C71: 00              NOP                         
3C72: DB CA           IN      A,($CA)             ; {}
3C74: C9              RET                         
3C75: CB EA           SET     5,D                 
3C77: 00              NOP                         
3C78: ED 
3C79: 00              NOP                         
3C7A: 00              NOP                         
3C7B: 00              NOP                         
3C7C: 00              NOP                         
3C7D: 00              NOP                         
3C7E: 00              NOP                         
3C7F: 00              NOP                         
3C80: DC CF CD        CALL    C,$CDCF             
3C83: D0              RET     NC                  
3C84: CE D1           ADC     $D1                 
3C86: F0              RET     P                   
3C87: 00              NOP                         
3C88: F1              POP     AF                  
3C89: 00              NOP                         
3C8A: 00              NOP                         
3C8B: 00              NOP                         
3C8C: 00              NOP                         
3C8D: 00              NOP                         
3C8E: 00              NOP                         
3C8F: 00              NOP                         
3C90: D3 D5           OUT     ($D5),A             ; {}
3C92: D4 D6 F0        CALL    NC,$F0D6            
3C95: 00              NOP                         
3C96: F3              DI                          
3C97: 00              NOP                         
3C98: 00              NOP                         
3C99: 00              NOP                         
3C9A: 00              NOP                         
3C9B: 00              NOP                         
3C9C: C4 C6 C5        CALL    NZ,$C5C6            
3C9F: C7              RST     0X00                
3CA0: 00              NOP                         
3CA1: 00              NOP                         
3CA2: 00              NOP                         
3CA3: 00              NOP                         
3CA4: 00              NOP                         
3CA5: 00              NOP                         
3CA6: DB CA           IN      A,($CA)             ; {}
3CA8: C9              RET                         
3CA9: CB 00           RLC     B                   
3CAB: 00              NOP                         
3CAC: 00              NOP                         
3CAD: 00              NOP                         
3CAE: 00              NOP                         
3CAF: 00              NOP                         
3CB0: DC CF CD        CALL    C,$CDCF             
3CB3: D0              RET     NC                  
3CB4: DD 
3CB5: D1              POP     DE                  
3CB6: 00              NOP                         
3CB7: 00              NOP                         
3CB8: 00              NOP                         
3CB9: 00              NOP                         
3CBA: 00              NOP                         
3CBB: 00              NOP                         
3CBC: D3 D5           OUT     ($D5),A             ; {}
3CBE: DD 
3CBF: D6 00           SUB     $00                 
3CC1: 00              NOP                         
3CC2: DE E2           SBC     $E2                 
3CC4: AB              XOR     E                   
3CC5: B2              OR      D                   
3CC6: AC              XOR     H                   
3CC7: B3              OR      E                   
3CC8: DF              RST     0X18                
3CC9: E3              EX      (SP),HL             
3CCA: 00              NOP                         
3CCB: 00              NOP                         
3CCC: 00              NOP                         
3CCD: 00              NOP                         
3CCE: 00              NOP                         
3CCF: E5              PUSH    HL                  
3CD0: B4              OR      H                   
3CD1: B6              OR      (HL)                
3CD2: B5              OR      L                   
3CD3: B7              OR      A                   
3CD4: E4 E6 00        CALL    PO,$00E6            ; {}
3CD7: 00              NOP                         
3CD8: 00              NOP                         
3CD9: 00              NOP                         
3CDA: 00              NOP                         
3CDB: 00              NOP                         
3CDC: B8              CP      B                   
3CDD: BB              CP      E                   
3CDE: B9              CP      C                   
3CDF: BC              CP      H                   
3CE0: BA              CP      D                   
3CE1: BD              CP      L                   
3CE2: 00              NOP                         
3CE3: 00              NOP                         
3CE4: 00              NOP                         
3CE5: 00              NOP                         
3CE6: 00              NOP                         
3CE7: 00              NOP                         
3CE8: BE              CP      (HL)                
3CE9: C1              POP     BC                  
3CEA: BF              CP      A                   
3CEB: C2 C0 C3        JP      NZ,$C3C0            
3CEE: 00              NOP                         
3CEF: E7              RST     0X20                
3CF0: FF              RST     0X38                
3CF1: FF              RST     0X38                
3CF2: FF              RST     0X38                
3CF3: FF              RST     0X38                
3CF4: FF              RST     0X38                
3CF5: FF              RST     0X38                
3CF6: FF              RST     0X38                
3CF7: FF              RST     0X38                
3CF8: FF              RST     0X38                
3CF9: FF              RST     0X38                
3CFA: FF              RST     0X38                
3CFB: FF              RST     0X38                
3CFC: FF              RST     0X38                
3CFD: FF              RST     0X38                
3CFE: FF              RST     0X38                
3CFF: FF              RST     0X38                
3D00: 00              NOP                         
3D01: 00              NOP                         
3D02: FA FC D7        JP      M,$D7FC             
3D05: D9              EXX                         
3D06: D8              RET     C                   
3D07: DA FB FD        JP      C,$FDFB             
3D0A: 00              NOP                         
3D0B: 00              NOP                         
3D0C: F4 F6 F5        CALL    P,$F5F6             
3D0F: 00              NOP                         
3D10: C4 C6 C5        CALL    NZ,$C5C6            
3D13: C7              RST     0X00                
3D14: F7              RST     0X30                
3D15: 00              NOP                         
3D16: F8              RET     M                   
3D17: F9              LD      SP,HL               
3D18: 00              NOP                         
3D19: 00              NOP                         
3D1A: 00              NOP                         
3D1B: 00              NOP                         
3D1C: A7              AND     A                   
3D1D: A9              XOR     C                   
3D1E: A8              XOR     B                   
3D1F: AA              XOR     D                   
3D20: 00              NOP                         
3D21: 00              NOP                         
3D22: 00              NOP                         
3D23: 00              NOP                         
3D24: 00              NOP                         
3D25: 00              NOP                         
3D26: AB              XOR     E                   
3D27: AD              XOR     L                   
3D28: AC              XOR     H                   
3D29: AE              XOR     (HL)                
3D2A: 00              NOP                         
3D2B: 00              NOP                         
3D2C: 00              NOP                         
3D2D: 00              NOP                         
3D2E: DE 00           SBC     $00                 
3D30: AB              XOR     E                   
3D31: B0              OR      B                   
3D32: AC              XOR     H                   
3D33: B1              OR      C                   
3D34: DF              RST     0X18                
3D35: 00              NOP                         
3D36: 00              NOP                         
3D37: 00              NOP                         
3D38: DE E0           SBC     $E0                 
3D3A: AB              XOR     E                   
3D3B: B2              OR      D                   
3D3C: AC              XOR     H                   
3D3D: B3              OR      E                   
3D3E: DF              RST     0X18                
3D3F: E1              POP     HL                  
3D40: 00              NOP                         
3D41: 00              NOP                         
3D42: 9D              SBC     L                   
3D43: 00              NOP                         
3D44: 9E              SBC     (HL)                
3D45: 00              NOP                         
3D46: 00              NOP                         
3D47: 00              NOP                         
3D48: 00              NOP                         
3D49: 00              NOP                         
3D4A: 9F              SBC     A                   
3D4B: 00              NOP                         
3D4C: A0              AND     B                   
3D4D: 00              NOP                         
3D4E: 00              NOP                         
3D4F: 00              NOP                         
3D50: 00              NOP                         
3D51: 00              NOP                         
3D52: 00              NOP                         
3D53: 00              NOP                         
3D54: 9C              SBC     H                   
3D55: 00              NOP                         
3D56: 00              NOP                         
3D57: 00              NOP                         
3D58: 00              NOP                         
3D59: 00              NOP                         
3D5A: 00              NOP                         
3D5B: 00              NOP                         
3D5C: A3              AND     E                   
3D5D: A5              AND     L                   
3D5E: A4              AND     H                   
3D5F: A6              AND     (HL)                
3D60: 00              NOP                         
3D61: 00              NOP                         
3D62: 9C              SBC     H                   
3D63: 00              NOP                         
3D64: 00              NOP                         
3D65: 00              NOP                         
3D66: 00              NOP                         
3D67: 00              NOP                         
3D68: 9D              SBC     L                   
3D69: 00              NOP                         
3D6A: 9E              SBC     (HL)                
3D6B: 00              NOP                         
3D6C: 00              NOP                         
3D6D: 00              NOP                         
3D6E: 9F              SBC     A                   
3D6F: 00              NOP                         
3D70: A0              AND     B                   
3D71: 00              NOP                         
3D72: 00              NOP                         
3D73: 00              NOP                         
3D74: A1              AND     C                   
3D75: 00              NOP                         
3D76: A2              AND     D                   
3D77: 00              NOP                         
3D78: 00              NOP                         
3D79: 00              NOP                         
3D7A: 96              SUB     (HL)                
3D7B: 00              NOP                         
3D7C: 00              NOP                         
3D7D: 00              NOP                         
3D7E: 00              NOP                         
3D7F: 00              NOP                         
3D80: 97              SUB     A                   
3D81: 00              NOP                         
3D82: 93              SUB     E                   
3D83: 00              NOP                         
3D84: 00              NOP                         
3D85: 00              NOP                         
3D86: 98              SBC     B                   
3D87: 00              NOP                         
3D88: 99              SBC     C                   
3D89: 00              NOP                         
3D8A: 00              NOP                         
3D8B: 00              NOP                         
3D8C: 9A              SBC     D                   
3D8D: 00              NOP                         
3D8E: 9B              SBC     E                   
3D8F: 00              NOP                         
3D90: 00              NOP                         
3D91: 00              NOP                         
3D92: 90              SUB     B                   
3D93: 00              NOP                         
3D94: 00              NOP                         
3D95: 00              NOP                         
3D96: 00              NOP                         
3D97: 00              NOP                         
3D98: 91              SUB     C                   
3D99: 00              NOP                         
3D9A: 00              NOP                         
3D9B: 00              NOP                         
3D9C: 00              NOP                         
3D9D: 00              NOP                         
3D9E: 92              SUB     D                   
3D9F: 00              NOP                         
3DA0: 93              SUB     E                   
3DA1: 00              NOP                         
3DA2: 00              NOP                         
3DA3: 00              NOP                         
3DA4: 94              SUB     H                   
3DA5: 00              NOP                         
3DA6: 95              SUB     L                   
3DA7: 00              NOP                         
3DA8: 00              NOP                         
3DA9: 00              NOP                         
3DAA: 01 00 00        LD      BC,$0000            
3DAD: 00              NOP                         
3DAE: 08              EX      AF,AF'              
3DAF: 00              NOP                         
3DB0: 00              NOP                         
3DB1: 00              NOP                         
3DB2: 0A              LD      A,(BC)              
3DB3: 00              NOP                         
3DB4: 00              NOP                         
3DB5: 00              NOP                         
3DB6: 0B              DEC     BC                  
3DB7: 00              NOP                         
3DB8: 0C              INC     C                   
3DB9: 0C              INC     C                   
3DBA: 0E FF           LD      C,$FF               
3DBC: 0D              DEC     C                   
3DBD: 0E 0D           LD      C,$0D               
3DBF: FF              RST     0X38                
3DC0: 06 70           LD      B,$70               
3DC2: 07              RLCA                        
3DC3: 70              LD      (HL),B              
3DC4: 08              EX      AF,AF'              
3DC5: 70              LD      (HL),B              
3DC6: 08              EX      AF,AF'              
3DC7: 70              LD      (HL),B              
3DC8: 08              EX      AF,AF'              
3DC9: 70              LD      (HL),B              
3DCA: 07              RLCA                        
3DCB: 78              LD      A,B                 
3DCC: 06 80           LD      B,$80               
3DCE: 05              DEC     B                   
3DCF: 88              ADC     A,B                 
3DD0: 04              INC     B                   
3DD1: 90              SUB     B                   
3DD2: 03              INC     BC                  
3DD3: 98              SBC     B                   
3DD4: 02              LD      (BC),A              
3DD5: A0              AND     B                   
3DD6: 01 A8 02        LD      BC,$02A8            
3DD9: 70              LD      (HL),B              
3DDA: 03              INC     BC                  
3DDB: 70              LD      (HL),B              
3DDC: 04              INC     B                   
3DDD: 70              LD      (HL),B              
3DDE: 05              DEC     B                   
3DDF: 70              LD      (HL),B              
3DE0: 40              LD      B,B                 
3DE1: 40              LD      B,B                 
3DE2: 40              LD      B,B                 
3DE3: 40              LD      B,B                 
3DE4: 40              LD      B,B                 
3DE5: 40              LD      B,B                 
3DE6: 40              LD      B,B                 
3DE7: 34              INC     (HL)                
3DE8: 2C              INC     L                   
3DE9: 26 20           LD      H,$20               
3DEB: 1C              INC     E                   
3DEC: 18 14           JR      $3E02               ; {}
3DEE: 12              LD      (DE),A              
3DEF: 0F              RRCA                        
3DF0: 0D              DEC     C                   
3DF1: 0B              DEC     BC                  
3DF2: 09              ADD     HL,BC               
3DF3: 08              EX      AF,AF'              
3DF4: 07              RLCA                        
3DF5: 06 05           LD      B,$05               
3DF7: 04              INC     B                   
3DF8: 03              INC     BC                  
3DF9: 02              LD      (BC),A              
3DFA: 02              LD      (BC),A              
3DFB: 02              LD      (BC),A              
3DFC: 02              LD      (BC),A              
3DFD: 02              LD      (BC),A              
3DFE: 02              LD      (BC),A              
3DFF: 02              LD      (BC),A              
3E00: 01 02 04        LD      BC,$0402            
3E03: 08              EX      AF,AF'              
3E04: 10 20           DJNZ    $3E26               ; {}
3E06: 40              LD      B,B                 
3E07: 80              ADD     A,B                 
3E08: 3D              DEC     A                   
3E09: A8              XOR     B                   
3E0A: 3D              DEC     A                   
3E0B: AC              XOR     H                   
3E0C: 3D              DEC     A                   
3E0D: B0              OR      B                   
3E0E: 3D              DEC     A                   
3E0F: B4              OR      H                   
3E10: 3D              DEC     A                   
3E11: 90              SUB     B                   
3E12: 3D              DEC     A                   
3E13: 96              SUB     (HL)                
3E14: 3D              DEC     A                   
3E15: 9C              SBC     H                   
3E16: 3D              DEC     A                   
3E17: A2              AND     D                   
3E18: 3D              DEC     A                   
3E19: 78              LD      A,B                 
3E1A: 3D              DEC     A                   
3E1B: 7E              LD      A,(HL)              
3E1C: 3D              DEC     A                   
3E1D: 84              ADD     A,H                 
3E1E: 3D              DEC     A                   
3E1F: 8A              ADC     A,D                 
3E20: 3D              DEC     A                   
3E21: 60              LD      H,B                 
3E22: 3D              DEC     A                   
3E23: 66              LD      H,(HL)              
3E24: 3D              DEC     A                   
3E25: 6C              LD      L,H                 
3E26: 3D              DEC     A                   
3E27: 72              LD      (HL),D              
3E28: 3D              DEC     A                   
3E29: 40              LD      B,B                 
3E2A: 3D              DEC     A                   
3E2B: 48              LD      C,B                 
3E2C: 3D              DEC     A                   
3E2D: 50              LD      D,B                 
3E2E: 3D              DEC     A                   
3E2F: 58              LD      E,B                 
3E30: 3D              DEC     A                   
3E31: 18 3D           JR      $3E70               ; {}
3E33: 22 3D 2C        LD      ($2C3D),HL          ; {}
3E36: 3D              DEC     A                   
3E37: 36 3C           LD      (HL),$3C            
3E39: C0              RET     NZ                  
3E3A: 3D              DEC     A                   
3E3B: 00              NOP                         
3E3C: 3D              DEC     A                   
3E3D: 0C              INC     C                   
3E3E: 3C              INC     A                   
3E3F: 00              NOP                         
3E40: 3D              DEC     A                   
3E41: 58              LD      E,B                 
3E42: 3D              DEC     A                   
3E43: 50              LD      D,B                 
3E44: 3D              DEC     A                   
3E45: 48              LD      C,B                 
3E46: 3D              DEC     A                   
3E47: 40              LD      B,B                 
3E48: 3D              DEC     A                   
3E49: 36 3D           LD      (HL),$3D            
3E4B: 2C              INC     L                   
3E4C: 3D              DEC     A                   
3E4D: 22 3D 18        LD      ($183D),HL          ; {}
3E50: 3C              INC     A                   
3E51: 00              NOP                         
3E52: 3D              DEC     A                   
3E53: 0C              INC     C                   
3E54: 3D              DEC     A                   
3E55: 00              NOP                         
3E56: 3C              INC     A                   
3E57: C0              RET     NZ                  
3E58: 3C              INC     A                   
3E59: 00              NOP                         
3E5A: 3C              INC     A                   
3E5B: 0E 3C           LD      C,$3C               
3E5D: 1C              INC     E                   
3E5E: 3C              INC     A                   
3E5F: 2A 3C 38        LD      HL,($383C)          ; {}
3E62: 3C              INC     A                   
3E63: 42              LD      B,D                 
3E64: 3C              INC     A                   
3E65: 4C              LD      C,H                 
3E66: 3C              INC     A                   
3E67: 56              LD      D,(HL)              
3E68: 3C              INC     A                   
3E69: 60              LD      H,B                 
3E6A: 3C              INC     A                   
3E6B: 6E              LD      L,(HL)              
3E6C: 3C              INC     A                   
3E6D: 7C              LD      A,H                 
3E6E: 3C              INC     A                   
3E6F: 8A              ADC     A,D                 
3E70: 3C              INC     A                   
3E71: 98              SBC     B                   
3E72: 3C              INC     A                   
3E73: A2              AND     D                   
3E74: 3C              INC     A                   
3E75: AC              XOR     H                   
3E76: 3C              INC     A                   
3E77: B6              OR      (HL)                
3E78: 3C              INC     A                   
3E79: C0              RET     NZ                  
3E7A: 3C              INC     A                   
3E7B: CC 3C D8        CALL    Z,$D83C             
3E7E: 3C              INC     A                   
3E7F: E4 05 40        CALL    PO,$4005            
3E82: 05              DEC     B                   
3E83: 20 04           JR      NZ,$3E89            ; {}
3E85: 30 04           JR      NC,$3E8B            ; {}
3E87: 10 06           DJNZ    $3E8F               ; {}
3E89: 48              LD      C,B                 
3E8A: 06 28           LD      B,$28               
3E8C: 05              DEC     B                   
3E8D: 38 05           JR      C,$3E94             ; {}
3E8F: 18 07           JR      $3E98               ; {}
3E91: 50              LD      D,B                 
3E92: 07              RLCA                        
3E93: 30 06           JR      NC,$3E9B            ; {}
3E95: 40              LD      B,B                 
3E96: 06 20           LD      B,$20               
3E98: 08              EX      AF,AF'              
3E99: 58              LD      E,B                 
3E9A: 08              EX      AF,AF'              
3E9B: 38 07           JR      C,$3EA4             ; {}
3E9D: 48              LD      C,B                 
3E9E: 07              RLCA                        
3E9F: 28 06           JR      Z,$3EA7             ; {}
3EA1: 10 05           DJNZ    $3EA8               ; {}
3EA3: 20 05           JR      NZ,$3EAA            ; {}
3EA5: 30 05           JR      NC,$3EAC            ; {}
3EA7: 40              LD      B,B                 
3EA8: 08              EX      AF,AF'              
3EA9: 18 07           JR      $3EB2               ; {}
3EAB: 28 07           JR      Z,$3EB4             ; {}
3EAD: 38 06           JR      C,$3EB5             ; {}
3EAF: 48              LD      C,B                 
3EB0: 08              EX      AF,AF'              
3EB1: 20 07           JR      NZ,$3EBA            ; {}
3EB3: 30 07           JR      NC,$3EBC            ; {}
3EB5: 40              LD      B,B                 
3EB6: 07              RLCA                        
3EB7: 50              LD      D,B                 
3EB8: 08              EX      AF,AF'              
3EB9: 30 08           JR      NC,$3EC3            ; {}
3EBB: 40              LD      B,B                 
3EBC: 08              EX      AF,AF'              
3EBD: 50              LD      D,B                 
3EBE: 08              EX      AF,AF'              
3EBF: 60              LD      H,B                 
3EC0: FF              RST     0X38                
3EC1: 48              LD      C,B                 
3EC2: 40              LD      B,B                 
3EC3: 40              LD      B,B                 
3EC4: 40              LD      B,B                 
3EC5: 38 30           JR      C,$3EF7             ; {}
3EC7: 28 38           JR      Z,$3F01             ; {}
3EC9: 30 28           JR      NC,$3EF3            ; {}
3ECB: 20 30           JR      NZ,$3EFD            ; {}
3ECD: 20 30           JR      NZ,$3EFF            ; {}
3ECF: 28 01           JR      Z,$3ED2             ; {}
3ED1: 01 01 01        LD      BC,$0101            
3ED4: 00              NOP                         
3ED5: 00              NOP                         
3ED6: 01 01 00        LD      BC,$0001            
3ED9: 01 01 01        LD      BC,$0101            
3EDC: 00              NOP                         
3EDD: 00              NOP                         
3EDE: 00              NOP                         
3EDF: 01 05 04        LD      BC,$0405            
3EE2: 03              INC     BC                  
3EE3: 02              LD      (BC),A              
3EE4: 01 00 00        LD      BC,$0000            
3EE7: 00              NOP                         
3EE8: 00              NOP                         
3EE9: 00              NOP                         
3EEA: 01 01 01        LD      BC,$0101            
3EED: 01 02 02        LD      BC,$0202            
3EF0: 02              LD      (BC),A              
3EF1: 02              LD      (BC),A              
3EF2: 03              INC     BC                  
3EF3: 03              INC     BC                  
3EF4: 03              INC     BC                  
3EF5: 04              INC     B                   
3EF6: 04              INC     B                   
3EF7: 04              INC     B                   
3EF8: 05              DEC     B                   
3EF9: 05              DEC     B                   
3EFA: 06 06           LD      B,$06               
3EFC: 07              RLCA                        
3EFD: 08              EX      AF,AF'              
3EFE: 07              RLCA                        
3EFF: 06 FF           LD      B,$FF               
3F01: FF              RST     0X38                
3F02: FF              RST     0X38                
3F03: FF              RST     0X38                
3F04: FF              RST     0X38                
3F05: FF              RST     0X38                
3F06: FF              RST     0X38                
3F07: FF              RST     0X38                
3F08: 20 FF           JR      NZ,$3F09            ; {}
3F0A: 02              LD      (BC),A              
3F0B: FF              RST     0X38                
3F0C: 36 D2           LD      (HL),$D2            
3F0E: 36 C0           LD      (HL),$C0            
3F10: 20 FF           JR      NZ,$3F11            ; {}
3F12: 03              INC     BC                  
3F13: FF              RST     0X38                
3F14: 36 D2           LD      (HL),$D2            
3F16: 35              DEC     (HL)                
3F17: E0              RET     PO                  
3F18: 30 FF           JR      NC,$3F19            ; {}
3F1A: 04              INC     B                   
3F1B: FF              RST     0X38                
3F1C: 36 D2           LD      (HL),$D2            
3F1E: 35              DEC     (HL)                
3F1F: E0              RET     PO                  
3F20: 10 FF           DJNZ    $3F21               ; {}
3F22: 05              DEC     B                   
3F23: FF              RST     0X38                
3F24: 36 EA           LD      (HL),$EA            
3F26: 35              DEC     (HL)                
3F27: E0              RET     PO                  
3F28: 10 FF           DJNZ    $3F29               ; {}
3F2A: 06 FF           LD      B,$FF               
3F2C: 36 EA           LD      (HL),$EA            
3F2E: 36 C0           LD      (HL),$C0            
3F30: 10 60           DJNZ    $3F92               ; {}
3F32: 07              RLCA                        
3F33: 1F              RRA                         
3F34: 37              SCF                         
3F35: 0A              LD      A,(BC)              
3F36: 36 C0           LD      (HL),$C0            
3F38: F0              RET     P                   
3F39: 10 0B           DJNZ    $3F46               ; {}
3F3B: 1A              LD      A,(DE)              
3F3C: 37              SCF                         
3F3D: 0A              LD      A,(BC)              
3F3E: 36 C0           LD      (HL),$C0            
3F40: 40              LD      B,B                 
3F41: FF              RST     0X38                
3F42: 04              INC     B                   
3F43: FF              RST     0X38                
3F44: 36 EA           LD      (HL),$EA            
3F46: 36 C0           LD      (HL),$C0            
3F48: 10 FF           DJNZ    $3F49               ; {}
3F4A: 08              EX      AF,AF'              
3F4B: FF              RST     0X38                
3F4C: 36 EA           LD      (HL),$EA            
3F4E: 36 C0           LD      (HL),$C0            
3F50: 40              LD      B,B                 
3F51: 10 0F           DJNZ    $3F62               ; {}
3F53: 17              RLA                         
3F54: 37              SCF                         
3F55: 0A              LD      A,(BC)              
3F56: 36 C0           LD      (HL),$C0            
3F58: 10 FF           DJNZ    $3F59               ; {}
3F5A: 0A              LD      A,(BC)              
3F5B: FF              RST     0X38                
3F5C: 36 EA           LD      (HL),$EA            
3F5E: 35              DEC     (HL)                
3F5F: E0              RET     PO                  
3F60: FF              RST     0X38                
3F61: FF              RST     0X38                
3F62: FF              RST     0X38                
3F63: FF              RST     0X38                
3F64: 36 CC           LD      (HL),$CC            
3F66: 35              DEC     (HL)                
3F67: E0              RET     PO                  
3F68: FF              RST     0X38                
3F69: FF              RST     0X38                
3F6A: FF              RST     0X38                
3F6B: FF              RST     0X38                
3F6C: 36 CC           LD      (HL),$CC            
3F6E: 35              DEC     (HL)                
3F6F: E0              RET     PO                  
3F70: 10 FF           DJNZ    $3F71               ; {}
3F72: 06 FF           LD      B,$FF               
3F74: 36 EA           LD      (HL),$EA            
3F76: 35              DEC     (HL)                
3F77: E0              RET     PO                  
3F78: 10 10           DJNZ    $3F8A               ; {}
3F7A: 07              RLCA                        
3F7B: 79              LD      A,C                 
3F7C: 37              SCF                         
3F7D: 0A              LD      A,(BC)              
3F7E: 35              DEC     (HL)                
3F7F: E0              RET     PO                  
3F80: 01 48 EE        LD      BC,$EE48            
3F83: 00              NOP                         
3F84: 10 B0           DJNZ    $3F36               ; {}
3F86: 10 20           DJNZ    $3FA8               ; {}
3F88: 01 49 2C        LD      BC,$2C49            
3F8B: 00              NOP                         
3F8C: 10 A0           DJNZ    $3F2E               ; {}
3F8E: 00              NOP                         
3F8F: B0              OR      B                   
3F90: 01 49 6A        LD      BC,$6A49            
3F93: 00              NOP                         
3F94: 10 90           DJNZ    $3F26               ; {}
3F96: 00              NOP                         
3F97: B8              CP      B                   
3F98: 01 49 A8        LD      BC,$A849            
3F9B: 00              NOP                         
3F9C: 10 80           DJNZ    $3F1E               ; {}
3F9E: 00              NOP                         
3F9F: C0              RET     NZ                  
3FA0: 01 49 E6        LD      BC,$E649            
3FA3: 00              NOP                         
3FA4: 10 70           DJNZ    $4016               
3FA6: 00              NOP                         
3FA7: C8              RET     Z                   
3FA8: 01 4A 24        LD      BC,$244A            
3FAB: 00              NOP                         
3FAC: 10 60           DJNZ    $400E               
3FAE: 00              NOP                         
3FAF: C8              RET     Z                   
3FB0: 01 4A 62        LD      BC,$624A            
3FB3: 00              NOP                         
3FB4: 10 50           DJNZ    $4006               
3FB6: 00              NOP                         
3FB7: C8              RET     Z                   
3FB8: 01 4A A0        LD      BC,$A04A            
3FBB: 00              NOP                         
3FBC: 10 40           DJNZ    $3FFE               ; {}
3FBE: 00              NOP                         
3FBF: C8              RET     Z                   
3FC0: 01 4A CE        LD      BC,$CE4A            
3FC3: 00              NOP                         
3FC4: 10 38           DJNZ    $3FFE               ; {}
3FC6: 00              NOP                         
3FC7: B0              OR      B                   
3FC8: 01 48 CC        LD      BC,$CC48            
3FCB: 00              NOP                         
3FCC: 10 B8           DJNZ    $3F86               ; {}
3FCE: 10 20           DJNZ    $3FF0               ; {}
3FD0: 01 4A CA        LD      BC,$CA4A            
3FD3: 00              NOP                         
3FD4: 10 38           DJNZ    $400E               
3FD6: 00              NOP                         
3FD7: B8              CP      B                   
3FD8: 01 48 C8        LD      BC,$C848            
3FDB: 00              NOP                         
3FDC: 10 B8           DJNZ    $3F96               ; {}
3FDE: 10 18           DJNZ    $3FF8               ; {}
3FE0: 01 4A C6        LD      BC,$C64A            
3FE3: 00              NOP                         
3FE4: 10 38           DJNZ    $401E               
3FE6: 00              NOP                         
3FE7: C0              RET     NZ                  
3FE8: 01 48 C4        LD      BC,$C448            
3FEB: 00              NOP                         
3FEC: 10 B8           DJNZ    $3FA6               ; {}
3FEE: 10 10           DJNZ    $4000               
3FF0: 01 4A C2        LD      BC,$C24A            
3FF3: 00              NOP                         
3FF4: 10 38           DJNZ    $402E               
3FF6: 00              NOP                         
3FF7: C8              RET     Z                   
3FF8: 01 48 C0        LD      BC,$C048            
3FFB: 00              NOP                         
3FFC: 10 B8           DJNZ    $3FB6               ; {}
3FFE: 10 08           DJNZ    $4008               
```

