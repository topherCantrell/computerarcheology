![Frogger Main Board](Frogger.jpg)

# Frogger Main Board

>>> cpu Z80

>>> binary 0000:roms/frogger.26 + roms/frogger.27 + roms/frsm3.7

>>> memoryTable hard 

[Hardware Info](Hardware.md)

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

```code

; Patches for listening to sounds
;
;0000: 3E 18           LD      A,$18               ; Sound command (1-18)       
;0002: 32 02 D0        LD      ($D002),A           ; Trigger the sound
;0005: 3A 00 88        LD      A,($8800)           ; {hard.watchdog} Feed the watchdog
;0008: C3 05 00        JP      $0005               ; Loop forever

0000: 3A 00 40        LD      A,($4000)           ; Is there ...
0003: FE 55           CP      $55                 ; ... an expansion ROM ?
0005: CA 01 40        JP      Z,$4001             ; Yes ... jump to it
0008: 3A 00 88        LD      A,($8800)           ; {hard.watchdog} Feed the watchdog
000B: 31 00 88        LD      SP,$8800            ; Stack at top of RAM
000E: C3 A3 02        JP      $02A3               ; {code.Initialize}

0011: FF FF FF FF FF FF FF                  
       
0018: 4F              LD      C,A                 
0019: 3A FE 83        LD      A,($83FE)           
001C: B7              OR      A                   
001D: C8              RET     Z                   
001E: E5              PUSH    HL                  
001F: 21 00 83        LD      HL,$8300            
0022: 34              INC     (HL)                
0023: 7E              LD      A,(HL)              
0024: 6F              LD      L,A                 
0025: 71              LD      (HL),C              
0026: E1              POP     HL                  
0027: C9              RET                         
```

# Print a string across the screen (down a column)

```code
; Copy across screen left to right (down a column)
; DE = string
; HL = screen start
; B = number of characters
PrintString:
0028: 1A              LD      A,(DE)              ; Character to ...
0029: 77              LD      (HL),A              ; ... screen
002A: 7D              LD      A,L                 ; Screen LSB
002B: D6 20           SUB     $20                 ; Move up ...
002D: 6F              LD      L,A                 ; ... one row
002E: 30 01           JR      NC,$31              ; {} No borrow
0030: 25              DEC     H                   ; Borrow from the MSB
0031: 13              INC     DE                  ; Next character
0032: 10 F4           DJNZ    $28                 ; {code.PrintString} Do all B-count characters
0034: C9              RET                         
                  
0035: FF FF FF 
```

# Clear Screen

There are 32 rows of 32 columns. This clears the screen from right to left one
column at a time with a noticeable delay between columns.

?? Is the screen rotated?

```code      
ClearScreen:
0038: 11 10 20        LD      DE,$2010            ; 32 columns
003B: 21 00 A8        LD      HL,$A800            ; Start of video RAM
003E: 06 20           LD      B,$20               ; 32 characters in column
0040: 73              LD      (HL),E              ; Character $10 ... space
0041: 23              INC     HL                  ; Next on screen
0042: 10 FC           DJNZ    $40                 ; {} Do all 32 characters
0044: 0E 15           LD      C,$15               ; Outer delay value
0046: 10 FE           DJNZ    $46                 ; {} Inner delay ... 256 times
0048: 0D              DEC     C                   ; All in outer done?
0049: 20 FB           JR      NZ,$46              ; {} No ... keep delaying
004B: 15              DEC     D                   ; All columns done?
004C: 20 F0           JR      NZ,$3E              ; {} No ... do next
004E: C9              RET                         ; Done
        
004F: FF FF FF FF FF FF FF FF FF FF FF          
005A: FF FF FF FF FF FF FF FF FF FF FF FF
          
InterruptService:
0066: F5              PUSH    AF                  
0067: E5              PUSH    HL                  
0068: D5              PUSH    DE                  
0069: C5              PUSH    BC                  
006A: DD E5           PUSH    IX                  
006C: FD E5           PUSH    IY                  
006E: 3A 00 88        LD      A,($8800)           ; {hard.watchdog}
0071: AF              XOR     A                   
0072: 32 08 B8        LD      ($B808),A           ; {hard.IRQENABLE} Disable interrupts
0075: CD F0 2C        CALL    $2CF0               ; {}
0078: 21 07 80        LD      HL,$8007            
007B: 11 07 B0        LD      DE,$B007            
007E: 7E              LD      A,(HL)              
007F: 12              LD      (DE),A              
0080: 2C              INC     L                   
0081: 1C              INC     E                   
0082: 06 1C           LD      B,$1C               
0084: 7E              LD      A,(HL)              
0085: 0F              RRCA                        
0086: 0F              RRCA                        
0087: 0F              RRCA                        
0088: 0F              RRCA                        
0089: 12              LD      (DE),A              
008A: 2C              INC     L                   
008B: 1C              INC     E                   
008C: 7E              LD      A,(HL)              
008D: 12              LD      (DE),A              
008E: 2C              INC     L                   
008F: 1C              INC     E                   
0090: 10 F2           DJNZ    $84                 ; {}
0092: 0E 08           LD      C,$08               
0094: 3A 2F 84        LD      A,($842F)           
0097: B7              OR      A                   
0098: 28 05           JR      Z,$9F               ; {}
009A: 0E 06           LD      C,$06               
009C: 1E 48           LD      E,$48               
009E: 6B              LD      L,E                 
009F: 7E              LD      A,(HL)              
00A0: 0F              RRCA                        
00A1: 0F              RRCA                        
00A2: 0F              RRCA                        
00A3: 0F              RRCA                        
00A4: 12              LD      (DE),A              
00A5: 2C              INC     L                   
00A6: 1C              INC     E                   
00A7: 06 03           LD      B,$03               
00A9: 7E              LD      A,(HL)              
00AA: 12              LD      (DE),A              
00AB: 2C              INC     L                   
00AC: 1C              INC     E                   
00AD: 10 FA           DJNZ    $A9                 ; {}
00AF: 0D              DEC     C                   
00B0: 20 ED           JR      NZ,$9F              ; {}
00B2: 21 7F 83        LD      HL,$837F            
00B5: 7E              LD      A,(HL)              
00B6: B7              OR      A                   
00B7: 28 07           JR      Z,$C0               ; {}
00B9: 35              DEC     (HL)                
00BA: 20 04           JR      NZ,$C0              ; {}
00BC: AF              XOR     A                   
00BD: 32 1C B8        LD      ($B81C),A           ; {hard.COINCNT1}
00C0: 21 7E 83        LD      HL,$837E            
00C3: 7E              LD      A,(HL)              
00C4: B7              OR      A                   
00C5: 28 07           JR      Z,$CE               ; {}
00C7: 35              DEC     (HL)                
00C8: 20 04           JR      NZ,$CE              ; {}
00CA: AF              XOR     A                   
00CB: 32 18 B8        LD      ($B818),A           ; {hard.COINCNT0}
00CE: 3A 04 E0        LD      A,($E004)           ; {hard.PPI8255+2004}
00D1: E6 08           AND     $08                 
00D3: CA FC 00        JP      Z,$00FC             ; {}
00D6: 3A FE 83        LD      A,($83FE)           
00D9: A7              AND     A                   
00DA: CA FC 00        JP      Z,$00FC             ; {}
00DD: 3A FD 83        LD      A,($83FD)           
00E0: A7              AND     A                   
00E1: 28 19           JR      Z,$FC               ; {}
00E3: 3D              DEC     A                   
00E4: 28 16           JR      Z,$FC               ; {}
00E6: 0E 02           LD      C,$02               
00E8: 21 43 80        LD      HL,$8043            
00EB: 11 43 B0        LD      DE,$B043            
00EE: 7E              LD      A,(HL)              
00EF: 81              ADD     A,C                 
00F0: 12              LD      (DE),A              
00F1: 0E 02           LD      C,$02               
00F3: 21 47 80        LD      HL,$8047            
00F6: 11 47 B0        LD      DE,$B047            
00F9: 7E              LD      A,(HL)              
00FA: 81              ADD     A,C                 
00FB: 12              LD      (DE),A              
;
00FC: 3A FE 83        LD      A,($83FE)           
00FF: B7              OR      A                   
0100: CA 22 01        JP      Z,$0122             ; {}
0103: CD AC 07        CALL    $07AC               ; {}
0106: 3A EA 83        LD      A,($83EA)           
0109: B7              OR      A                   
010A: CA 45 02        JP      Z,$0245             ; {}
010D: 2A D2 83        LD      HL,($83D2)          
0110: 7C              LD      A,H                 
0111: B5              OR      L                   
0112: CA 71 01        JP      Z,$0171             ; {}
0115: 2B              DEC     HL                  
0116: 22 D2 83        LD      ($83D2),HL          
0119: CD B7 14        CALL    $14B7               ; {}
011C: CD 02 18        CALL    $1802               ; {}
011F: C3 45 02        JP      $0245               ; {}
;
0122: 3A D6 83        LD      A,($83D6)           
0125: FE 02           CP      $02                 
0127: D2 58 01        JP      NC,$0158            ; {}
012A: B7              OR      A                   
012B: CC 7A 0E        CALL    Z,$0E7A             ; {}
012E: CD 41 23        CALL    $2341               ; {}
0131: AF              XOR     A                   
0132: 32 CD 83        LD      ($83CD),A           
0135: 32 CF 83        LD      ($83CF),A           
0138: 32 B5 83        LD      ($83B5),A           
013B: 67              LD      H,A                 
013C: 6F              LD      L,A                 
013D: 22 93 82        LD      ($8293),HL          
0140: 21 5C 82        LD      HL,$825C            
0143: 11 5D 82        LD      DE,$825D            
0146: 01 0B 00        LD      BC,$000B            
0149: 70              LD      (HL),B              
014A: ED B0           LDIR                        
014C: 21 AF 83        LD      HL,$83AF            
014F: 36 80           LD      (HL),$80            
0151: 2C              INC     L                   
0152: 77              LD      (HL),A              
0153: 2C              INC     L                   
0154: 77              LD      (HL),A              
0155: C3 45 02        JP      $0245               ; {}
0158: 21 D8 83        LD      HL,$83D8            
015B: 7E              LD      A,(HL)              
015C: B7              OR      A                   
015D: CA 45 02        JP      Z,$0245             ; {}
0160: 35              DEC     (HL)                
0161: C2 45 02        JP      NZ,$0245            ; {}
0164: 2D              DEC     L                   
0165: 7E              LD      A,(HL)              
0166: B7              OR      A                   
0167: C2 45 02        JP      NZ,$0245            ; {}
016A: 21 D6 83        LD      HL,$83D6            
016D: 35              DEC     (HL)                
016E: C3 45 02        JP      $0245               ; {}
0171: 2A 82 83        LD      HL,($8382)          
0174: 7C              LD      A,H                 
0175: B5              OR      L                   
0176: 28 12           JR      Z,$18A              ; {}
0178: 2B              DEC     HL                  
0179: 22 82 83        LD      ($8382),HL          
017C: 7C              LD      A,H                 
017D: B5              OR      L                   
017E: 20 0A           JR      NZ,$18A             ; {}
0180: 3E 0F           LD      A,$0F               
0182: DF              RST     $18                 
0183: 3E B0           LD      A,$B0               
0185: DF              RST     $18                 
0186: AF              XOR     A                   
0187: 32 71 83        LD      ($8371),A           
018A: 3A FD 83        LD      A,($83FD)           
018D: 3D              DEC     A                   
018E: C2 74 02        JP      NZ,$0274            ; {}
0191: 3A 5C 82        LD      A,($825C)           
0194: FE 05           CP      $05                 
0196: CA 5E 02        JP      Z,$025E             ; {}
0199: 3A 98 82        LD      A,($8298)           
019C: A7              AND     A                   
019D: 28 07           JR      Z,$1A6              ; {}
019F: 3D              DEC     A                   
01A0: 32 98 82        LD      ($8298),A           
01A3: C3 E2 01        JP      $01E2               ; {}
01A6: 3A 97 82        LD      A,($8297)           
01A9: A7              AND     A                   
01AA: C2 57 02        JP      NZ,$0257            ; {}
01AD: 2A 9D 82        LD      HL,($829D)          
01B0: 7C              LD      A,H                 
01B1: B5              OR      L                   
01B2: 20 2E           JR      NZ,$1E2             ; {}
01B4: CD 70 08        CALL    $0870               ; {}
01B7: CD 55 1A        CALL    $1A55               ; {}
01BA: 3A B5 83        LD      A,($83B5)           
01BD: B7              OR      A                   
01BE: 20 22           JR      NZ,$1E2             ; {}
01C0: 3C              INC     A                   
01C1: 32 B5 83        LD      ($83B5),A           
01C4: 3E FF           LD      A,$FF               
01C6: 32 84 83        LD      ($8384),A           
01C9: 3A 80 83        LD      A,($8380)           
01CC: B7              OR      A                   
01CD: 28 13           JR      Z,$1E2              ; {}
01CF: AF              XOR     A                   
01D0: 32 80 83        LD      ($8380),A           
01D3: 21 40 00        LD      HL,$0040            
01D6: 22 82 83        LD      ($8382),HL          
01D9: 11 7B 2F        LD      DE,$2F7B            
01DC: 21 51 AA        LD      HL,$AA51            
01DF: 06 07           LD      B,$07               
01E1: EF              RST     $28                 
01E2: 3A 84 83        LD      A,($8384)           
01E5: B7              OR      A                   
01E6: 28 0A           JR      Z,$1F2              ; {}
01E8: 3D              DEC     A                   
01E9: 32 84 83        LD      ($8384),A           
01EC: 21 50 A8        LD      HL,$A850            
01EF: CC E2 19        CALL    Z,$19E2             ; {}
01F2: CD 05 20        CALL    $2005               ; {}
01F5: CD 02 18        CALL    $1802               ; {}
01F8: 3A 07 81        LD      A,($8107)           
01FB: A7              AND     A                   
01FC: 28 07           JR      Z,$205              ; {}
01FE: 3A 09 81        LD      A,($8109)           
0201: 3D              DEC     A                   
0202: 32 09 81        LD      ($8109),A           
0205: 3A 08 81        LD      A,($8108)           
0208: A7              AND     A                   
0209: 28 07           JR      Z,$212              ; {}
020B: 3A 24 81        LD      A,($8124)           
020E: 3D              DEC     A                   
020F: 32 24 81        LD      ($8124),A           
0212: CD BF 11        CALL    $11BF               ; {}
0215: 3A 07 81        LD      A,($8107)           
0218: A7              AND     A                   
0219: 28 07           JR      Z,$222              ; {}
021B: 3A 09 81        LD      A,($8109)           
021E: 3C              INC     A                   
021F: 32 09 81        LD      ($8109),A           
0222: 3A 08 81        LD      A,($8108)           
0225: A7              AND     A                   
0226: 28 07           JR      Z,$22F              ; {}
0228: 3A 24 81        LD      A,($8124)           
022B: 3C              INC     A                   
022C: 32 24 81        LD      ($8124),A           
022F: CD F8 16        CALL    $16F8               ; {}
0232: CD B7 14        CALL    $14B7               ; {}
0235: CD 70 29        CALL    $2970               ; {}
0238: CD C7 1F        CALL    $1FC7               ; {}
023B: CD 92 02        CALL    $0292               ; {}
023E: 3A 97 82        LD      A,($8297)           
0241: A7              AND     A                   
0242: C4 A2 06        CALL    NZ,$06A2            ; {}
0245: 3A 00 88        LD      A,($8800)           ; {hard.watchdog}
0248: FD E1           POP     IY                  
024A: DD E1           POP     IX                  
024C: C1              POP     BC                  
024D: D1              POP     DE                  
024E: E1              POP     HL                  
024F: 3E 01           LD      A,$01               
0251: 32 08 B8        LD      ($B808),A           ; {hard.IRQENABLE} Enable interrupts
0254: F1              POP     AF                  
0255: ED 45           RETN                        

0257: 3D              DEC     A                   
0258: 32 97 82        LD      ($8297),A           
025B: C3 E2 01        JP      $01E2               ; {}
025E: 21 5E 82        LD      HL,$825E            
0261: 11 5F 82        LD      DE,$825F            
0264: 01 04 00        LD      BC,$0004            
0267: 70              LD      (HL),B              
0268: ED B0           LDIR                        
026A: AF              XOR     A                   
026B: 32 5C 82        LD      ($825C),A           
026E: CD D3 05        CALL    $05D3               ; {}
0271: C3 45 02        JP      $0245               ; {}
0274: 3A 5D 82        LD      A,($825D)           
0277: FE 05           CP      $05                 
0279: C2 99 01        JP      NZ,$0199            ; {}
027C: 21 63 82        LD      HL,$8263            
027F: 11 64 82        LD      DE,$8264            
0282: 01 04 00        LD      BC,$0004            
0285: 70              LD      (HL),B              
0286: ED B0           LDIR                        
0288: AF              XOR     A                   
0289: 32 5D 82        LD      ($825D),A           
028C: CD D3 05        CALL    $05D3               ; {}
028F: C3 45 02        JP      $0245               ; {}
0292: 2A 9D 82        LD      HL,($829D)          
0295: 7C              LD      A,H                 
0296: B5              OR      L                   
0297: C8              RET     Z                   
0298: 2B              DEC     HL                  
0299: 22 9D 82        LD      ($829D),HL          
029C: 7C              LD      A,H                 
029D: B5              OR      L                   
029E: C0              RET     NZ                  
029F: 32 AE 83        LD      ($83AE),A           
02A2: C9              RET                         

Initialize:  
02A3: AF              XOR     A                   
02A4: 32 08 B8        LD      ($B808),A           ; {hard.IRQENABLE} Disable interrupts
02A7: 32 05 88        LD      ($8805),A           
02AA: 32 10 B8        LD      ($B810),A           ; {hard.FLIPX}
02AD: 32 0C B8        LD      ($B80C),A           ; {hard.FLIPY}
02B0: 21 00 80        LD      HL,$8000            
02B3: 11 01 80        LD      DE,$8001            
02B6: 01 FF 07        LD      BC,$07FF            
02B9: 75              LD      (HL),L              
02BA: ED B0           LDIR                        
02BC: 21 00 B0        LD      HL,$B000            
02BF: 01 00 00        LD      BC,$0000            
02C2: 71              LD      (HL),C              
02C3: 2C              INC     L                   
02C4: 10 FC           DJNZ    $2C2                ; {}
02C6: 3A 02 E0        LD      A,($E002)           ; {hard.PPI8255+2002}
02C9: 16 2E           LD      D,$2E               
02CB: E6 03           AND     $03                 
02CD: 5F              LD      E,A                 
02CE: 1A              LD      A,(DE)              
02CF: 32 E4 83        LD      ($83E4),A           
02D2: 3A 04 E0        LD      A,($E004)           ; {hard.PPI8255+2004}
02D5: 67              LD      H,A                 
02D6: CB 5C           BIT     3,H                 
02D8: 28 05           JR      Z,$2DF              ; {}
02DA: 3E 01           LD      A,$01               
02DC: 32 C2 83        LD      ($83C2),A           
02DF: 7C              LD      A,H                 
02E0: E6 06           AND     $06                 
02E2: 32 D4 83        LD      ($83D4),A           
02E5: 21 0A 2E        LD      HL,$2E0A            
02E8: 11 EB 83        LD      DE,$83EB            
02EB: 01 12 00        LD      BC,$0012            
02EE: ED B0           LDIR                        
02F0: CD 48 10        CALL    $1048               ; {}
02F3: 3E 01           LD      A,$01               
02F5: 32 70 83        LD      ($8370),A           
02F8: 32 08 B8        LD      ($B808),A           ; {hard.IRQENABLE} Enable interrupts
02FB: FF              RST     $38                 ; Clear the screen
02FC: AF              XOR     A                   
02FD: 32 01 B0        LD      ($B001),A           ; {hard.SPRITERAM+1}
0300: 3E 06           LD      A,$06               
0302: 32 03 B0        LD      ($B003),A           ; {hard.SPRITERAM+3}
0305: 21 00 01        LD      HL,$0100            
0308: 22 C7 83        LD      ($83C7),HL          
030B: 3E 15           LD      A,$15               
030D: 32 81 83        LD      ($8381),A           
0310: 21 B1 2E        LD      HL,$2EB1            
0313: 11 00 84        LD      DE,$8400            
0316: 01 20 00        LD      BC,$0020            
0319: ED B0           LDIR                        
031B: 21 06 E0        LD      HL,$E006            
031E: 36 9B           LD      (HL),$9B            
0320: 21 06 D0        LD      HL,$D006            
0323: 36 88           LD      (HL),$88            
0325: 3E 18           LD      A,$18               
0327: 32 D9 83        LD      ($83D9),A           
032A: 32 02 D0        LD      ($D002),A           ; {hard.PPI8255+1002}
032D: AF              XOR     A                   
032E: CD 94 07        CALL    $0794               ; {}
0331: 3A D9 83        LD      A,($83D9)           
0334: E6 EF           AND     $EF                 
0336: 32 D9 83        LD      ($83D9),A           
0339: 32 02 D0        LD      ($D002),A           ; {hard.PPI8255+1002}
033C: 3E FF           LD      A,$FF               
033E: CD 94 07        CALL    $0794               ; {}
0341: 3A D6 83        LD      A,($83D6)           
0344: FE 02           CP      $02                 
0346: D4 11 0D        CALL    NC,$0D11            ; {}
0349: CD 1F 0B        CALL    $0B1F               ; {}
034C: 3A D6 83        LD      A,($83D6)           
034F: 3D              DEC     A                   
0350: C4 67 0B        CALL    NZ,$0B67            ; {}
0353: CD 0F 23        CALL    $230F               ; {}
0356: 3E 02           LD      A,$02               
0358: 21 54 82        LD      HL,$8254            
035B: 77              LD      (HL),A              
035C: 23              INC     HL                  
035D: 77              LD      (HL),A              
035E: 3E 09           LD      A,$09               
0360: 23              INC     HL                  
0361: 77              LD      (HL),A              
0362: 23              INC     HL                  
0363: 77              LD      (HL),A              
0364: 23              INC     HL                  
0365: 77              LD      (HL),A              
0366: 23              INC     HL                  
0367: 77              LD      (HL),A              
0368: 2A C7 83        LD      HL,($83C7)          
036B: 7C              LD      A,H                 
036C: B5              OR      L                   
036D: 2B              DEC     HL                  
036E: 20 FB           JR      NZ,$36B             ; {}
0370: 3A FE 83        LD      A,($83FE)           
0373: B7              OR      A                   
0374: C2 0B 04        JP      NZ,$040B            ; {}
0377: 3A B3 83        LD      A,($83B3)           
037A: B7              OR      A                   
037B: 20 C4           JR      NZ,$341             ; {}
037D: 3A 02 E0        LD      A,($E002)           ; {hard.PPI8255+2002}
0380: 07              RLCA                        
0381: 30 07           JR      NC,$38A             ; {}
0383: 07              RLCA                        
0384: 38 BB           JR      C,$341              ; {}
0386: 0E 02           LD      C,$02               
0388: 18 02           JR      $38C                ; {}
038A: 0E 01           LD      C,$01               
038C: 3A E1 83        LD      A,($83E1)           
038F: B9              CP      C                   
0390: 38 AF           JR      C,$341              ; {}
0392: 91              SUB     C                   
0393: 27              DAA                         
0394: 32 E1 83        LD      ($83E1),A           
0397: 79              LD      A,C                 
0398: 32 70 83        LD      ($8370),A           
039B: 21 00 85        LD      HL,$8500            
039E: 11 01 85        LD      DE,$8501            
03A1: 01 FF 01        LD      BC,$01FF            
03A4: 75              LD      (HL),L              
03A5: ED B0           LDIR                        
03A7: 32 FE 83        LD      ($83FE),A           
03AA: 3E 01           LD      A,$01               
03AC: 32 FD 83        LD      ($83FD),A           
03AF: 32 B3 83        LD      ($83B3),A           
03B2: 67              LD      H,A                 
03B3: 6F              LD      L,A                 
03B4: 32 B7 83        LD      ($83B7),A           
03B7: 22 B8 83        LD      ($83B8),HL          
03BA: CD 0A 0B        CALL    $0B0A               ; {}
03BD: 3E 03           LD      A,$03               
03BF: 32 3D 80        LD      ($803D),A           
03C2: CD D9 07        CALL    $07D9               ; {}
03C5: AF              XOR     A                   
03C6: 32 71 80        LD      ($8071),A           
03C9: DF              RST     $18                 ; Reset sounds
03CA: 3E 09           LD      A,$09               ; Intro song ...
03CC: DF              RST     $18                 ; ... voice A
03CD: 3E 0A           LD      A,$0A               ; Intro song ...
03CF: DF              RST     $18                 ; ... voice B
03D0: 3E 0B           LD      A,$0B               ; Intro song ...
03D2: DF              RST     $18                 ; ... voice C
03D3: 21 20 00        LD      HL,$0020            
03D6: 22 9D 82        LD      ($829D),HL          
03D9: 21 A0 01        LD      HL,$01A0            
03DC: 22 82 83        LD      ($8382),HL          
03DF: 21 00 00        LD      HL,$0000            
03E2: 22 D2 83        LD      ($83D2),HL          
03E5: CD E6 07        CALL    $07E6               ; {}
03E8: FF              RST     $38                 ; Clear the screen
03E9: CD 3D 22        CALL    $223D               ; {}
03EC: AF              XOR     A                   
03ED: 67              LD      H,A                 
03EE: 6F              LD      L,A                 
03EF: 32 2F 84        LD      ($842F),A           
03F2: 32 2D 84        LD      ($842D),A           
03F5: 22 93 82        LD      ($8293),HL          
03F8: 21 40 84        LD      HL,$8440            
03FB: 11 41 84        LD      DE,$8441            
03FE: 01 4F 00        LD      BC,$004F            
0401: 70              LD      (HL),B              
0402: ED B0           LDIR                        
0404: 32 04 80        LD      ($8004),A           
0407: 3C              INC     A                   
0408: 32 5A 82        LD      ($825A),A           
040B: 3A EA 83        LD      A,($83EA)           
040E: B7              OR      A                   
040F: C2 57 04        JP      NZ,$0457            ; {}
0412: 3A CD 83        LD      A,($83CD)           
0415: B7              OR      A                   
0416: 20 0D           JR      NZ,$425             ; {}
0418: 3A FE 83        LD      A,($83FE)           
041B: 3D              DEC     A                   
041C: 28 04           JR      Z,$422              ; {}
041E: FF              RST     $38                 ; Clear the screen
041F: CD EE 06        CALL    $06EE               ; {}
0422: CD 1F 0B        CALL    $0B1F               ; {}
0425: 3A 6D 82        LD      A,($826D)           
0428: A7              AND     A                   
0429: C4 F0 05        CALL    NZ,$05F0            ; {}
042C: CD 42 09        CALL    $0942               ; {}
042F: 32 EA 83        LD      ($83EA),A           
0432: CD 16 0A        CALL    $0A16               ; {}
0435: 21 9E 83        LD      HL,$839E            
0438: 36 20           LD      (HL),$20            
043A: 2D              DEC     L                   
043B: 36 10           LD      (HL),$10            
043D: 2D              DEC     L                   
043E: 36 20           LD      (HL),$20            
0440: 3A FE 83        LD      A,($83FE)           
0443: 3D              DEC     A                   
0444: C4 C1 07        CALL    NZ,$07C1            ; {}
0447: AF              XOR     A                   
0448: 32 6D 82        LD      ($826D),A           
044B: 3A CD 83        LD      A,($83CD)           
044E: 32 B6 83        LD      ($83B6),A           
0451: CD 48 0A        CALL    $0A48               ; {}
0454: C3 68 03        JP      $0368               ; {}
0457: CD 1F 0B        CALL    $0B1F               ; {}
045A: 3A CE 83        LD      A,($83CE)           
045D: B7              OR      A                   
045E: CA 68 03        JP      Z,$0368             ; {}
0461: CD 04 08        CALL    $0804               ; {}
0464: CD E6 07        CALL    $07E6               ; {}
0467: AF              XOR     A                   
0468: 21 9A 83        LD      HL,$839A            
046B: 77              LD      (HL),A              
046C: 2C              INC     L                   
046D: 77              LD      (HL),A              
046E: 32 CC 83        LD      ($83CC),A           
0471: 32 EA 83        LD      ($83EA),A           
0474: 21 A0 83        LD      HL,$83A0            
0477: 11 A1 83        LD      DE,$83A1            
047A: 01 0D 00        LD      BC,$000D            
047D: 77              LD      (HL),A              
047E: ED B0           LDIR                        
0480: 3E 80           LD      A,$80               
0482: DF              RST     $18                 
0483: 3A CF 83        LD      A,($83CF)           
0486: B7              OR      A                   
0487: 20 06           JR      NZ,$48F             ; {}
0489: CD 22 08        CALL    $0822               ; {}
048C: C3 68 03        JP      $0368               ; {}
048F: CD 59 0F        CALL    $0F59               ; {}
0492: 3E 0C           LD      A,$0C               
0494: DF              RST     $18                 
0495: 3E 0D           LD      A,$0D               
0497: DF              RST     $18                 
0498: 2A C5 83        LD      HL,($83C5)          
049B: 2B              DEC     HL                  
049C: 22 C5 83        LD      ($83C5),HL          
049F: 7C              LD      A,H                 
04A0: B5              OR      L                   
04A1: 20 F8           JR      NZ,$49B             ; {}
04A3: 3A FE 83        LD      A,($83FE)           
04A6: 3D              DEC     A                   
04A7: CA 47 05        JP      Z,$0547             ; {}
04AA: 3A FD 83        LD      A,($83FD)           
04AD: 3D              DEC     A                   
04AE: C2 F3 04        JP      NZ,$04F3            ; {}
04B1: 21 C9 83        LD      HL,$83C9            
04B4: 36 01           LD      (HL),$01            
04B6: 23              INC     HL                  
04B7: 7E              LD      A,(HL)              
04B8: B7              OR      A                   
04B9: C2 34 05        JP      NZ,$0534            ; {}
04BC: FF              RST     $38                 ; Clear the screen
04BD: CD 22 08        CALL    $0822               ; {}
04C0: 3E 01           LD      A,$01               
04C2: 32 FE 83        LD      ($83FE),A           
04C5: 32 5C 82        LD      ($825C),A           
04C8: 21 5E 82        LD      HL,$825E            
04CB: 11 5F 82        LD      DE,$825F            
04CE: 01 04 00        LD      BC,$0004            
04D1: 36 00           LD      (HL),$00            
04D3: ED B0           LDIR                        
04D5: 21 00 86        LD      HL,$8600            
04D8: 11 FF 80        LD      DE,$80FF            
04DB: 01 B7 00        LD      BC,$00B7            
04DE: ED B0           LDIR                        
04E0: 21 C0 85        LD      HL,$85C0            
04E3: 11 0C 80        LD      DE,$800C            
04E6: 01 2B 00        LD      BC,$002B            
04E9: ED B0           LDIR                        
04EB: 3E 01           LD      A,$01               
04ED: 32 3F 80        LD      ($803F),A           
04F0: C3 68 03        JP      $0368               ; {}
04F3: 21 CA 83        LD      HL,$83CA            
04F6: 36 01           LD      (HL),$01            
04F8: 2B              DEC     HL                  
04F9: 7E              LD      A,(HL)              
04FA: B7              OR      A                   
04FB: C2 57 05        JP      NZ,$0557            ; {}
04FE: FF              RST     $38                 ; Clear the screen
04FF: CD 22 08        CALL    $0822               ; {}
0502: 3E 01           LD      A,$01               
0504: 32 FE 83        LD      ($83FE),A           
0507: 32 5D 82        LD      ($825D),A           
050A: 21 63 82        LD      HL,$8263            
050D: 11 64 82        LD      DE,$8264            
0510: 01 04 00        LD      BC,$0004            
0513: 70              LD      (HL),B              
0514: ED B0           LDIR                        
0516: 21 C0 86        LD      HL,$86C0            
0519: 11 0C 80        LD      DE,$800C            
051C: 01 2B 00        LD      BC,$002B            
051F: ED B0           LDIR                        
0521: 3E 01           LD      A,$01               
0523: 32 3F 80        LD      ($803F),A           
0526: 21 00 85        LD      HL,$8500            
0529: 11 FF 80        LD      DE,$80FF            
052C: 01 B7 00        LD      BC,$00B7            
052F: ED B0           LDIR                        
0531: C3 68 03        JP      $0368               ; {}
0534: AF              XOR     A                   
0535: 32 5C 82        LD      ($825C),A           
0538: 21 5E 82        LD      HL,$825E            
053B: 11 5F 82        LD      DE,$825F            
053E: 01 04 00        LD      BC,$0004            
0541: 70              LD      (HL),B              
0542: ED B0           LDIR                        
0544: C3 67 05        JP      $0567               ; {}
0547: AF              XOR     A                   
0548: 32 5C 82        LD      ($825C),A           
054B: 21 5E 82        LD      HL,$825E            
054E: 11 5F 82        LD      DE,$825F            
0551: 01 04 00        LD      BC,$0004            
0554: 70              LD      (HL),B              
0555: ED B0           LDIR                        
0557: AF              XOR     A                   
0558: 32 5D 82        LD      ($825D),A           
055B: 21 63 82        LD      HL,$8263            
055E: 11 64 82        LD      DE,$8264            
0561: 01 04 00        LD      BC,$0004            
0564: 70              LD      (HL),B              
0565: ED B0           LDIR                        
0567: FF              RST     $38                 ; Clear the screen
0568: CD E6 07        CALL    $07E6               ; {}
056B: CD 67 0B        CALL    $0B67               ; {}
056E: CD 69 0F        CALL    $0F69               ; {}
0571: CD 1F 0B        CALL    $0B1F               ; {}
0574: 21 00 81        LD      HL,$8100            
0577: 11 01 81        LD      DE,$8101            
057A: 01 5F 01        LD      BC,$015F            
057D: 75              LD      (HL),L              
057E: ED B0           LDIR                        
0580: 21 00 80        LD      HL,$8000            
0583: 11 01 80        LD      DE,$8001            
0586: 01 04 00        LD      BC,$0004            
0589: 70              LD      (HL),B              
058A: ED B0           LDIR                        
058C: 21 0C 80        LD      HL,$800C            
058F: 11 0D 80        LD      DE,$800D            
0592: 01 2E 00        LD      BC,$002E            
0595: 70              LD      (HL),B              
0596: ED B0           LDIR                        
0598: AF              XOR     A                   
0599: 32 C3 83        LD      ($83C3),A           
059C: 32 FE 83        LD      ($83FE),A           
059F: 32 BF 83        LD      ($83BF),A           
05A2: 21 C9 83        LD      HL,$83C9            
05A5: 77              LD      (HL),A              
05A6: 2C              INC     L                   
05A7: 77              LD      (HL),A              
05A8: 67              LD      H,A                 
05A9: 6F              LD      L,A                 
05AA: 32 10 B8        LD      ($B810),A           ; {hard.FLIPX}
05AD: 32 0C B8        LD      ($B80C),A           ; {hard.FLIPY}
05B0: 22 93 82        LD      ($8293),HL          
05B3: 32 BB 83        LD      ($83BB),A           
05B6: 32 CB 83        LD      ($83CB),A           
05B9: 32 D8 83        LD      ($83D8),A           
05BC: 32 C4 83        LD      ($83C4),A           
05BF: 32 BA 83        LD      ($83BA),A           
05C2: 32 95 82        LD      ($8295),A           
05C5: 32 5B 82        LD      ($825B),A           
05C8: 3E 03           LD      A,$03               
05CA: 32 D6 83        LD      ($83D6),A           
05CD: CD EB 07        CALL    $07EB               ; {}
05D0: C3 68 03        JP      $0368               ; {}
05D3: 3E 01           LD      A,$01               
05D5: 32 6D 82        LD      ($826D),A           
05D8: 32 5A 82        LD      ($825A),A           
05DB: 32 CD 83        LD      ($83CD),A           
05DE: AF              XOR     A                   
05DF: 32 5B 82        LD      ($825B),A           
05E2: 32 EA 83        LD      ($83EA),A           
05E5: 3E FF           LD      A,$FF               
05E7: 32 97 82        LD      ($8297),A           
05EA: 3E 40           LD      A,$40               
05EC: 32 98 82        LD      ($8298),A           
05EF: C9              RET                         
05F0: 3E 10           LD      A,$10               
05F2: DF              RST     $18                 
05F3: 3E 30           LD      A,$30               
05F5: DF              RST     $18                 
05F6: 3A FD 83        LD      A,($83FD)           
05F9: 3D              DEC     A                   
05FA: 20 0C           JR      NZ,$608             ; {}
05FC: 21 93 82        LD      HL,$8293            
05FF: 34              INC     (HL)                
0600: 7E              LD      A,(HL)              
0601: D6 05           SUB     $05                 
0603: 20 0D           JR      NZ,$612             ; {}
0605: 77              LD      (HL),A              
0606: 18 0A           JR      $612                ; {}
0608: 21 94 82        LD      HL,$8294            
060B: 34              INC     (HL)                
060C: 7E              LD      A,(HL)              
060D: D6 05           SUB     $05                 
060F: 20 01           JR      NZ,$612             ; {}
0611: 77              LD      (HL),A              
0612: CD 29 06        CALL    $0629               ; {}
0615: CD 4B 06        CALL    $064B               ; {}
0618: CD 3D 22        CALL    $223D               ; {}
061B: CD 02 1A        CALL    $1A02               ; {}
061E: 3E 01           LD      A,$01               
0620: 32 80 83        LD      ($8380),A           
0623: 11 00 01        LD      DE,$0100            
0626: C3 E0 08        JP      $08E0               ; {}
0629: CD E6 07        CALL    $07E6               ; {}
062C: 21 9A 83        LD      HL,$839A            
062F: AF              XOR     A                   
0630: 77              LD      (HL),A              
0631: 2C              INC     L                   
0632: 77              LD      (HL),A              
0633: 3C              INC     A                   
0634: 32 CC 83        LD      ($83CC),A           
0637: 3E 20           LD      A,$20               
0639: 21 06 A8        LD      HL,$A806            
063C: CD 79 07        CALL    $0779               ; {}
063F: 2C              INC     L                   
0640: 2C              INC     L                   
0641: CD 79 07        CALL    $0779               ; {}
0644: 0E 0A           LD      C,$0A               
0646: 09              ADD     HL,BC               
0647: 3D              DEC     A                   
0648: 20 F2           JR      NZ,$63C             ; {}
064A: C9              RET                         
064B: 21 0C 80        LD      HL,$800C            
064E: 11 0D 80        LD      DE,$800D            
0651: 01 2B 00        LD      BC,$002B            
0654: 70              LD      (HL),B              
0655: ED B0           LDIR                        
0657: 21 0C 80        LD      HL,$800C            
065A: 11 0C B0        LD      DE,$B00C            
065D: 01 2B 00        LD      BC,$002B            
0660: ED B0           LDIR                        
0662: 21 00 81        LD      HL,$8100            
0665: 11 01 81        LD      DE,$8101            
0668: 01 62 00        LD      BC,$0062            
066B: 36 00           LD      (HL),$00            
066D: ED B0           LDIR                        
066F: C9              RET                         
0670: 21 64 AB        LD      HL,$AB64            
0673: CD 95 06        CALL    $0695               ; {}
0676: 21 A4 AA        LD      HL,$AAA4            
0679: CD 95 06        CALL    $0695               ; {}
067C: 21 E4 A9        LD      HL,$A9E4            
067F: CD 95 06        CALL    $0695               ; {}
0682: 21 24 A9        LD      HL,$A924            
0685: CD 95 06        CALL    $0695               ; {}
0688: 21 64 A8        LD      HL,$A864            
068B: CD 95 06        CALL    $0695               ; {}
068E: AF              XOR     A                   
068F: 32 2F 84        LD      ($842F),A           
0692: C3 5F 0A        JP      $0A5F               ; {}
0695: 3E 10           LD      A,$10               
0697: 77              LD      (HL),A              
0698: 23              INC     HL                  
0699: 77              LD      (HL),A              
069A: 01 1F 00        LD      BC,$001F            
069D: 09              ADD     HL,BC               
069E: 77              LD      (HL),A              
069F: 23              INC     HL                  
06A0: 77              LD      (HL),A              
06A1: C9              RET                         
06A2: FE C0           CP      $C0                 
06A4: CA C1 06        JP      Z,$06C1             ; {}
06A7: FE 90           CP      $90                 
06A9: CA C7 06        JP      Z,$06C7             ; {}
06AC: FE 70           CP      $70                 
06AE: CA CD 06        JP      Z,$06CD             ; {}
06B1: FE 50           CP      $50                 
06B3: CA D3 06        JP      Z,$06D3             ; {}
06B6: FE 30           CP      $30                 
06B8: CA D9 06        JP      Z,$06D9             ; {}
06BB: FE 10           CP      $10                 
06BD: CA 70 06        JP      Z,$0670             ; {}
06C0: C9              RET                         
06C1: 21 64 AB        LD      HL,$AB64            
06C4: C3 DF 06        JP      $06DF               ; {}
06C7: 21 A4 AA        LD      HL,$AAA4            
06CA: C3 DF 06        JP      $06DF               ; {}
06CD: 21 E4 A9        LD      HL,$A9E4            
06D0: C3 DF 06        JP      $06DF               ; {}
06D3: 21 24 A9        LD      HL,$A924            
06D6: C3 DF 06        JP      $06DF               ; {}
06D9: 21 64 A8        LD      HL,$A864            
06DC: C3 DF 06        JP      $06DF               ; {}
06DF: 36 FC           LD      (HL),$FC            
06E1: 23              INC     HL                  
06E2: 36 FD           LD      (HL),$FD            
06E4: 01 1F 00        LD      BC,$001F            
06E7: 09              ADD     HL,BC               
06E8: 36 FE           LD      (HL),$FE            
06EA: 23              INC     HL                  
06EB: 36 FF           LD      (HL),$FF            
06ED: C9              RET                         
06EE: 3A FD 83        LD      A,($83FD)           
06F1: 3D              DEC     A                   
06F2: 20 32           JR      NZ,$726             ; {}
06F4: 21 0C 80        LD      HL,$800C            
06F7: 11 C0 85        LD      DE,$85C0            
06FA: 01 2B 00        LD      BC,$002B            
06FD: ED B0           LDIR                        
06FF: 21 FF 80        LD      HL,$80FF            
0702: 11 00 86        LD      DE,$8600            
0705: 01 B7 00        LD      BC,$00B7            
0708: ED B0           LDIR                        
070A: 21 C0 86        LD      HL,$86C0            
070D: 11 0C 80        LD      DE,$800C            
0710: 01 2B 00        LD      BC,$002B            
0713: ED B0           LDIR                        
0715: 3E 01           LD      A,$01               
0717: 32 3F 80        LD      ($803F),A           
071A: 21 00 85        LD      HL,$8500            
071D: 11 FF 80        LD      DE,$80FF            
0720: 01 B7 00        LD      BC,$00B7            
0723: ED B0           LDIR                        
0725: C9              RET                         
0726: 21 FF 80        LD      HL,$80FF            
0729: 11 00 85        LD      DE,$8500            
072C: 01 B7 00        LD      BC,$00B7            
072F: ED B0           LDIR                        
0731: 21 0C 80        LD      HL,$800C            
0734: 11 C0 86        LD      DE,$86C0            
0737: 01 2B 00        LD      BC,$002B            
073A: ED B0           LDIR                        
073C: 21 00 86        LD      HL,$8600            
073F: 11 FF 80        LD      DE,$80FF            
0742: 01 B7 00        LD      BC,$00B7            
0745: ED B0           LDIR                        
0747: 21 C0 85        LD      HL,$85C0            
074A: 11 0C 80        LD      DE,$800C            
074D: 01 2B 00        LD      BC,$002B            
0750: ED B0           LDIR                        
0752: 3E 01           LD      A,$01               
0754: 32 3F 80        LD      ($803F),A           
0757: 3A 95 82        LD      A,($8295)           
075A: A7              AND     A                   
075B: C0              RET     NZ                  
075C: AF              XOR     A                   
075D: 32 5B 82        LD      ($825B),A           
0760: 3E 01           LD      A,$01               
0762: 32 95 82        LD      ($8295),A           
0765: C9              RET                         
0766: 21 02 A8        LD      HL,$A802            
0769: 11 10 20        LD      DE,$2010            
076C: 0E 04           LD      C,$04               
076E: 06 1C           LD      B,$1C               
0770: 73              LD      (HL),E              
0771: 23              INC     HL                  
0772: 10 FC           DJNZ    $770                ; {}
0774: 09              ADD     HL,BC               
0775: 15              DEC     D                   
0776: 20 F6           JR      NZ,$76E             ; {}
0778: C9              RET                         
0779: 01 10 0A        LD      BC,$0A10            
077C: 71              LD      (HL),C              
077D: 23              INC     HL                  
077E: 10 FC           DJNZ    $77C                ; {}
0780: C9              RET                         
0781: 21 08 A8        LD      HL,$A808            
0784: 11 10 20        LD      DE,$2010            
0787: 0E 0A           LD      C,$0A               
0789: 06 16           LD      B,$16               
078B: 73              LD      (HL),E              
078C: 23              INC     HL                  
078D: 10 FC           DJNZ    $78B                ; {}
078F: 09              ADD     HL,BC               
0790: 15              DEC     D                   
0791: 20 F6           JR      NZ,$789             ; {}
0793: C9              RET                         
0794: 32 00 D0        LD      ($D000),A           ; {hard.PPI8255+1000}
0797: 3A D9 83        LD      A,($83D9)           
079A: E6 F7           AND     $F7                 
079C: 32 02 D0        LD      ($D002),A           ; {hard.PPI8255+1002}
079F: 00              NOP                         
07A0: 00              NOP                         
07A1: 00              NOP                         
07A2: 00              NOP                         
07A3: 3A D9 83        LD      A,($83D9)           
07A6: F6 08           OR      $08                 
07A8: 32 02 D0        LD      ($D002),A           ; {hard.PPI8255+1002}
07AB: C9              RET                         
07AC: 21 00 83        LD      HL,$8300            
07AF: 7E              LD      A,(HL)              
07B0: B7              OR      A                   
07B1: C8              RET     Z                   
07B2: 35              DEC     (HL)                
07B3: 4F              LD      C,A                 
07B4: 2C              INC     L                   
07B5: 7E              LD      A,(HL)              
07B6: CD 94 07        CALL    $0794               ; {}
07B9: 54              LD      D,H                 
07BA: 5D              LD      E,L                 
07BB: 2C              INC     L                   
07BC: 06 00           LD      B,$00               
07BE: ED B0           LDIR                        
07C0: C9              RET                         
07C1: 3A FD 83        LD      A,($83FD)           
07C4: 3D              DEC     A                   
07C5: CA CE 07        JP      Z,$07CE             ; {}
07C8: 3E 01           LD      A,$01               
07CA: 32 5B 82        LD      ($825B),A           
07CD: C9              RET                         
07CE: 3A 6D 82        LD      A,($826D)           
07D1: A7              AND     A                   
07D2: C8              RET     Z                   
07D3: 3E 01           LD      A,$01               
07D5: 32 5B 82        LD      ($825B),A           
07D8: C9              RET                         
07D9: 21 00 83        LD      HL,$8300            
07DC: 11 01 83        LD      DE,$8301            
07DF: 01 2F 00        LD      BC,$002F            
07E2: 70              LD      (HL),B              
07E3: ED B0           LDIR                        
07E5: C9              RET                         
07E6: 3A FE 83        LD      A,($83FE)           
07E9: 3D              DEC     A                   
07EA: C8              RET     Z                   
07EB: AF              XOR     A                   
07EC: 21 44 80        LD      HL,$8044            
07EF: 11 45 80        LD      DE,$8045            
07F2: 01 1F 00        LD      BC,$001F            
07F5: 70              LD      (HL),B              
07F6: ED B0           LDIR                        
07F8: 21 20 84        LD      HL,$8420            
07FB: 11 21 84        LD      DE,$8421            
07FE: 0E 0B           LD      C,$0B               
0800: 77              LD      (HL),A              
0801: ED B0           LDIR                        
0803: C9              RET                         
0804: 21 44 80        LD      HL,$8044            
0807: AF              XOR     A                   
0808: 36 01           LD      (HL),$01            
080A: 2C              INC     L                   
080B: 77              LD      (HL),A              
080C: 2C              INC     L                   
080D: 2C              INC     L                   
080E: 77              LD      (HL),A              
080F: 3A FE 83        LD      A,($83FE)           
0812: FE 02           CP      $02                 
0814: C0              RET     NZ                  
0815: 21 40 00        LD      HL,$0040            
0818: 22 D2 83        LD      ($83D2),HL          
081B: 21 40 00        LD      HL,$0040            
081E: 22 DA 83        LD      ($83DA),HL          
0821: C9              RET                         
0822: AF              XOR     A                   
0823: 32 71 83        LD      ($8371),A           
0826: 3A FE 83        LD      A,($83FE)           
0829: 3D              DEC     A                   
082A: C8              RET     Z                   
082B: 3A FD 83        LD      A,($83FD)           
082E: EE 03           XOR     $03                 
0830: 32 FD 83        LD      ($83FD),A           
0833: 21 B8 83        LD      HL,$83B8            
0836: 3D              DEC     A                   
0837: 28 01           JR      Z,$83A              ; {}
0839: 2C              INC     L                   
083A: 7E              LD      A,(HL)              
083B: 32 B7 83        LD      ($83B7),A           
083E: AF              XOR     A                   
083F: 32 B6 83        LD      ($83B6),A           
0842: 3C              INC     A                   
0843: 32 5A 82        LD      ($825A),A           
0846: 3A C2 83        LD      A,($83C2)           
0849: B7              OR      A                   
084A: C8              RET     Z                   
084B: 3A CB 83        LD      A,($83CB)           
084E: EE 01           XOR     $01                 
0850: 32 CB 83        LD      ($83CB),A           
0853: 67              LD      H,A                 
0854: 32 10 B8        LD      ($B810),A           ; {hard.FLIPX}
0857: 32 0C B8        LD      ($B80C),A           ; {hard.FLIPY}
085A: C9              RET                         
085B: 21 51 AA        LD      HL,$AA51            
085E: 11 6E 2F        LD      DE,$2F6E            
0861: 06 04           LD      B,$04               
0863: EF              RST     $28                 
0864: 11 12 2F        LD      DE,$2F12            
0867: 06 05           LD      B,$05               
0869: EF              RST     $28                 
086A: 3E 01           LD      A,$01               
086C: 32 04 80        LD      ($8004),A           
086F: C9              RET                         
0870: 3A CD 83        LD      A,($83CD)           
0873: B7              OR      A                   
0874: C0              RET     NZ                  
0875: 3A 04 80        LD      A,($8004)           
0878: B7              OR      A                   
0879: C0              RET     NZ                  
087A: 3A AE 83        LD      A,($83AE)           
087D: B7              OR      A                   
087E: 20 07           JR      NZ,$887             ; {}
0880: 3C              INC     A                   
0881: 32 AE 83        LD      ($83AE),A           
0884: 3E 06           LD      A,$06               
0886: DF              RST     $18                 
0887: CD BA 0A        CALL    $0ABA               ; {}
088A: 3A DF 83        LD      A,($83DF)           
088D: B7              OR      A                   
088E: 20 35           JR      NZ,$8C5             ; {}
0890: 21 DC 83        LD      HL,$83DC            
0893: 35              DEC     (HL)                
0894: C0              RET     NZ                  
0895: 36 20           LD      (HL),$20            
0897: 23              INC     HL                  
0898: 7E              LD      A,(HL)              
0899: B7              OR      A                   
089A: CA 5B 08        JP      Z,$085B             ; {}
089D: 3D              DEC     A                   
089E: 77              LD      (HL),A              ; PATCH NOP out to stop timer
089F: 2C              INC     L                   
08A0: 7E              LD      A,(HL)              
08A1: 3D              DEC     A                   
08A2: 27              DAA                         
08A3: 77              LD      (HL),A              ; PATCH NOP out to stop timer
08A4: 2D              DEC     L                   
08A5: FE 10           CP      $10                 
08A7: 20 07           JR      NZ,$8B0             ; {}
08A9: 3E 05           LD      A,$05               
08AB: DF              RST     $18                 
08AC: AF              XOR     A                   
08AD: 32 3F 80        LD      ($803F),A           
08B0: 66              LD      H,(HL)              
08B1: 7C              LD      A,H                 
08B2: E6 03           AND     $03                 
08B4: 4F              LD      C,A                 
08B5: AC              XOR     H                   
08B6: 07              RLCA                        
08B7: 07              RLCA                        
08B8: 6F              LD      L,A                 
08B9: 26 00           LD      H,$00               
08BB: 29              ADD     HL,HL               
08BC: 11 DF A8        LD      DE,$A8DF            
08BF: 19              ADD     HL,DE               
08C0: 3E 10           LD      A,$10               
08C2: 91              SUB     C                   
08C3: 77              LD      (HL),A              
08C4: C9              RET                         
08C5: 3A E0 83        LD      A,($83E0)           
08C8: B7              OR      A                   
08C9: C0              RET     NZ                  
08CA: 3C              INC     A                   
08CB: 32 E0 83        LD      ($83E0),A           
08CE: 21 51 AA        LD      HL,$AA51            
08D1: 11 6E 2F        LD      DE,$2F6E            
08D4: 06 05           LD      B,$05               
08D6: EF              RST     $28                 
08D7: 3A DE 83        LD      A,($83DE)           
08DA: 5F              LD      E,A                 
08DB: 16 00           LD      D,$00               
08DD: CD A0 0B        CALL    $0BA0               ; {}
08E0: 3A FE 83        LD      A,($83FE)           
08E3: B7              OR      A                   
08E4: C8              RET     Z                   
08E5: 3A FD 83        LD      A,($83FD)           
08E8: 3D              DEC     A                   
08E9: 28 05           JR      Z,$8F0              ; {}
08EB: 21 EB 83        LD      HL,$83EB            
08EE: 18 03           JR      $8F3                ; {}
08F0: 21 ED 83        LD      HL,$83ED            
08F3: 7B              LD      A,E                 
08F4: 86              ADD     A,(HL)              
08F5: 27              DAA                         
08F6: 77              LD      (HL),A              
08F7: 5F              LD      E,A                 
08F8: 23              INC     HL                  
08F9: 7A              LD      A,D                 
08FA: 8E              ADC     A,(HL)              
08FB: 27              DAA                         
08FC: 77              LD      (HL),A              
08FD: 57              LD      D,A                 
08FE: 3A FD 83        LD      A,($83FD)           
0901: 3D              DEC     A                   
0902: 20 09           JR      NZ,$90D             ; {}
0904: 01 E7 83        LD      BC,$83E7            
0907: 0A              LD      A,(BC)              
0908: B7              OR      A                   
0909: 20 2B           JR      NZ,$936             ; {}
090B: 18 07           JR      $914                ; {}
090D: 01 E8 83        LD      BC,$83E8            
0910: 0A              LD      A,(BC)              
0911: B7              OR      A                   
0912: 20 22           JR      NZ,$936             ; {}
0914: 2A 08 2E        LD      HL,($2E08)          ; {}
0917: ED 52           SBC     HL,DE               
0919: 28 02           JR      Z,$91D              ; {}
091B: 30 19           JR      NC,$936             ; {}
091D: 32 CF 83        LD      ($83CF),A           
0920: 3C              INC     A                   
0921: 02              LD      (BC),A              
0922: 0D              DEC     C                   
0923: 0D              DEC     C                   
0924: 0A              LD      A,(BC)              
0925: 3C              INC     A                   
0926: 02              LD      (BC),A              
0927: 21 DE AB        LD      HL,$ABDE            
092A: 01 E0 FF        LD      BC,$FFE0            
092D: 09              ADD     HL,BC               
092E: 3D              DEC     A                   
092F: 20 FC           JR      NZ,$92D             ; {}
0931: 36 4D           LD      (HL),$4D            
0933: 3E 07           LD      A,$07               
0935: DF              RST     $18                 
0936: 2A EF 83        LD      HL,($83EF)          
0939: B7              OR      A                   
093A: ED 52           SBC     HL,DE               
093C: D0              RET     NC                  
093D: ED 53 EF 83     LD      ($83EF),DE          
0941: C9              RET                         
0942: AF              XOR     A                   
0943: 32 CE 83        LD      ($83CE),A           
0946: 3A CD 83        LD      A,($83CD)           
0949: B7              OR      A                   
094A: 20 04           JR      NZ,$950             ; {}
094C: AF              XOR     A                   
094D: 32 CF 83        LD      ($83CF),A           
0950: 3A FE 83        LD      A,($83FE)           
0953: B7              OR      A                   
0954: 28 74           JR      Z,$9CA              ; {}
0956: 3A FD 83        LD      A,($83FD)           
0959: 3D              DEC     A                   
095A: 20 05           JR      NZ,$961             ; {}
095C: 21 E5 83        LD      HL,$83E5            
095F: 18 03           JR      $964                ; {}
0961: 21 E6 83        LD      HL,$83E6            
0964: 3A CD 83        LD      A,($83CD)           
0967: B7              OR      A                   
0968: 20 08           JR      NZ,$972             ; {}
096A: 35              DEC     (HL)                
096B: 20 05           JR      NZ,$972             ; {}
096D: 3E 01           LD      A,$01               
096F: 32 CF 83        LD      ($83CF),A           
0972: CD 52 19        CALL    $1952               ; {}
0975: 3A CD 83        LD      A,($83CD)           
0978: B7              OR      A                   
0979: 20 0A           JR      NZ,$985             ; {}
097B: 3C              INC     A                   
097C: 32 B5 83        LD      ($83B5),A           
097F: 21 50 A8        LD      HL,$A850            
0982: CD E2 19        CALL    $19E2               ; {}
0985: 3A 6C 82        LD      A,($826C)           
0988: EE 01           XOR     $01                 
098A: 32 B5 83        LD      ($83B5),A           
098D: 3A FD 83        LD      A,($83FD)           
0990: 3D              DEC     A                   
0991: C2 D2 09        JP      NZ,$09D2            ; {}
0994: 21 5E 82        LD      HL,$825E            
0997: CD DB 09        CALL    $09DB               ; {}
099A: 3A 5A 82        LD      A,($825A)           
099D: A7              AND     A                   
099E: 28 0A           JR      Z,$9AA              ; {}
09A0: CD 3D 22        CALL    $223D               ; {}
09A3: CD AF 0F        CALL    $0FAF               ; {}
09A6: AF              XOR     A                   
09A7: 32 5A 82        LD      ($825A),A           
09AA: 21 44 80        LD      HL,$8044            
09AD: 36 80           LD      (HL),$80            
09AF: 2C              INC     L                   
09B0: 36 1E           LD      (HL),$1E            
09B2: 2C              INC     L                   
09B3: 36 03           LD      (HL),$03            
09B5: 2C              INC     L                   
09B6: 36 E0           LD      (HL),$E0            
09B8: AF              XOR     A                   
09B9: 32 CD 83        LD      ($83CD),A           
09BC: 32 2D 84        LD      ($842D),A           
09BF: 32 2C 84        LD      ($842C),A           
09C2: 32 69 82        LD      ($8269),A           
09C5: 3C              INC     A                   
09C6: 32 C3 83        LD      ($83C3),A           
09C9: C9              RET                         
09CA: 3A CD 83        LD      A,($83CD)           
09CD: B7              OR      A                   
09CE: C8              RET     Z                   
09CF: C3 AA 09        JP      $09AA               ; {}
09D2: 21 63 82        LD      HL,$8263            
09D5: CD DB 09        CALL    $09DB               ; {}
09D8: C3 9A 09        JP      $099A               ; {}
09DB: AF              XOR     A                   
09DC: B6              OR      (HL)                
09DD: 11 64 AB        LD      DE,$AB64            
09E0: C4 05 0A        CALL    NZ,$0A05            ; {}
09E3: 23              INC     HL                  
09E4: AF              XOR     A                   
09E5: B6              OR      (HL)                
09E6: 11 A4 AA        LD      DE,$AAA4            
09E9: C4 05 0A        CALL    NZ,$0A05            ; {}
09EC: 23              INC     HL                  
09ED: AF              XOR     A                   
09EE: B6              OR      (HL)                
09EF: 11 E4 A9        LD      DE,$A9E4            
09F2: C4 05 0A        CALL    NZ,$0A05            ; {}
09F5: 23              INC     HL                  
09F6: AF              XOR     A                   
09F7: B6              OR      (HL)                
09F8: 11 24 A9        LD      DE,$A924            
09FB: C4 05 0A        CALL    NZ,$0A05            ; {}
09FE: 23              INC     HL                  
09FF: AF              XOR     A                   
0A00: B6              OR      (HL)                
0A01: 11 64 A8        LD      DE,$A864            
0A04: C8              RET     Z                   
0A05: EB              EX      DE,HL               
0A06: 36 6C           LD      (HL),$6C            
0A08: 23              INC     HL                  
0A09: 36 6D           LD      (HL),$6D            
0A0B: 01 1F 00        LD      BC,$001F            
0A0E: 09              ADD     HL,BC               
0A0F: 36 6E           LD      (HL),$6E            
0A11: 23              INC     HL                  
0A12: 36 6F           LD      (HL),$6F            
0A14: EB              EX      DE,HL               
0A15: C9              RET                         
0A16: 3A E4 83        LD      A,($83E4)           
0A19: 3C              INC     A                   
0A1A: C8              RET     Z                   
0A1B: 3A FE 83        LD      A,($83FE)           
0A1E: B7              OR      A                   
0A1F: 20 05           JR      NZ,$A26             ; {}
0A21: 21 E4 83        LD      HL,$83E4            
0A24: 18 0E           JR      $A34                ; {}
0A26: 3A FD 83        LD      A,($83FD)           
0A29: 3D              DEC     A                   
0A2A: 20 05           JR      NZ,$A31             ; {}
0A2C: 21 E5 83        LD      HL,$83E5            
0A2F: 18 03           JR      $A34                ; {}
0A31: 21 E6 83        LD      HL,$83E6            
0A34: 46              LD      B,(HL)              
0A35: 78              LD      A,B                 
0A36: B7              OR      A                   
0A37: 3E 4D           LD      A,$4D               
0A39: 11 E0 FF        LD      DE,$FFE0            
0A3C: 21 BE AB        LD      HL,$ABBE            
0A3F: 28 04           JR      Z,$A45              ; {}
0A41: 77              LD      (HL),A              
0A42: 19              ADD     HL,DE               
0A43: 10 FC           DJNZ    $A41                ; {}
0A45: 36 10           LD      (HL),$10            
0A47: C9              RET                         
0A48: 3A B7 83        LD      A,($83B7)           
0A4B: 21 7E A8        LD      HL,$A87E            
0A4E: 11 20 00        LD      DE,$0020            
0A51: FE 0F           CP      $0F                 
0A53: 38 02           JR      C,$A57              ; {}
0A55: 3E 0F           LD      A,$0F               
0A57: 47              LD      B,A                 
0A58: 0E 4C           LD      C,$4C               
0A5A: 71              LD      (HL),C              
0A5B: 19              ADD     HL,DE               
0A5C: 10 FC           DJNZ    $A5A                ; {}
0A5E: C9              RET                         
0A5F: AF              XOR     A                   
0A60: 32 CC 83        LD      ($83CC),A           
0A63: 21 B8 83        LD      HL,$83B8            
0A66: 3A FD 83        LD      A,($83FD)           
0A69: 3D              DEC     A                   
0A6A: 28 01           JR      Z,$A6D              ; {}
0A6C: 2C              INC     L                   
0A6D: 34              INC     (HL)                
0A6E: 7E              LD      A,(HL)              
0A6F: 32 B7 83        LD      ($83B7),A           
0A72: FE 10           CP      $10                 
0A74: D0              RET     NC                  
0A75: 26 00           LD      H,$00               
0A77: 11 5E A8        LD      DE,$A85E            
0A7A: 87              ADD     A,A                 
0A7B: 87              ADD     A,A                 
0A7C: 87              ADD     A,A                 
0A7D: 87              ADD     A,A                 
0A7E: 6F              LD      L,A                 
0A7F: 29              ADD     HL,HL               
0A80: 19              ADD     HL,DE               
0A81: 36 4C           LD      (HL),$4C            
0A83: C9              RET                         
0A84: 06 05           LD      B,$05               
0A86: 21 F2 83        LD      HL,$83F2            
0A89: 7A              LD      A,D                 
0A8A: BE              CP      (HL)                
0A8B: 38 27           JR      C,$AB4              ; {}
0A8D: 28 19           JR      Z,$AA8              ; {}
0A8F: 78              LD      A,B                 
0A90: 3D              DEC     A                   
0A91: 28 0F           JR      Z,$AA2              ; {}
0A93: 87              ADD     A,A                 
0A94: 4F              LD      C,A                 
0A95: 06 00           LD      B,$00               
0A97: D5              PUSH    DE                  
0A98: 11 FA 83        LD      DE,$83FA            
0A9B: 21 F8 83        LD      HL,$83F8            
0A9E: ED B8           LDDR                        
0AA0: EB              EX      DE,HL               
0AA1: D1              POP     DE                  
0AA2: 72              LD      (HL),D              
0AA3: 2D              DEC     L                   
0AA4: 73              LD      (HL),E              
0AA5: 87              ADD     A,A                 
0AA6: 3C              INC     A                   
0AA7: C9              RET                         
0AA8: 2D              DEC     L                   
0AA9: 7E              LD      A,(HL)              
0AAA: 2C              INC     L                   
0AAB: BB              CP      E                   
0AAC: 38 E1           JR      C,$A8F              ; {}
0AAE: 20 04           JR      NZ,$AB4             ; {}
0AB0: 78              LD      A,B                 
0AB1: 3D              DEC     A                   
0AB2: 28 F1           JR      Z,$AA5              ; {}
0AB4: 2C              INC     L                   
0AB5: 2C              INC     L                   
0AB6: 10 D1           DJNZ    $A89                ; {}
0AB8: AF              XOR     A                   
0AB9: C9              RET                         
0ABA: 3A 2D 84        LD      A,($842D)           
0ABD: B7              OR      A                   
0ABE: C0              RET     NZ                  
0ABF: 3C              INC     A                   
0AC0: 32 2D 84        LD      ($842D),A           
0AC3: 3E 03           LD      A,$03               
0AC5: 32 3F 80        LD      ($803F),A           
0AC8: AF              XOR     A                   
0AC9: 32 E0 83        LD      ($83E0),A           
0ACC: 21 BF A8        LD      HL,$A8BF            
0ACF: 11 6E 2F        LD      DE,$2F6E            
0AD2: 06 04           LD      B,$04               
0AD4: EF              RST     $28                 
0AD5: 21 DF A8        LD      HL,$A8DF            
0AD8: 11 20 00        LD      DE,$0020            
0ADB: 01 0C 0F        LD      BC,$0F0C            
0ADE: 71              LD      (HL),C              
0ADF: 19              ADD     HL,DE               
0AE0: 10 FC           DJNZ    $ADE                ; {}
0AE2: 21 20 3C        LD      HL,$3C20            
0AE5: 22 DC 83        LD      ($83DC),HL          
0AE8: 3E 60           LD      A,$60               
0AEA: 32 DE 83        LD      ($83DE),A           
0AED: C9              RET                         
0AEE: E5              PUSH    HL                  
0AEF: D5              PUSH    DE                  
0AF0: 21 00 84        LD      HL,$8400            
0AF3: 35              DEC     (HL)                
0AF4: 20 02           JR      NZ,$AF8             ; {}
0AF6: 36 1F           LD      (HL),$1F            
0AF8: 54              LD      D,H                 
0AF9: 5E              LD      E,(HL)              
0AFA: 7B              LD      A,E                 
0AFB: C6 0D           ADD     $0D                 
0AFD: FE 20           CP      $20                 
0AFF: 38 02           JR      C,$B03              ; {}
0B01: D6 1F           SUB     $1F                 
0B03: 6F              LD      L,A                 
0B04: 1A              LD      A,(DE)              
0B05: AE              XOR     (HL)                
0B06: 77              LD      (HL),A              
0B07: D1              POP     DE                  
0B08: E1              POP     HL                  
0B09: C9              RET                         
0B0A: 21 00 00        LD      HL,$0000            
0B0D: 22 ED 83        LD      ($83ED),HL          
0B10: 22 EB 83        LD      ($83EB),HL          
0B13: 22 E7 83        LD      ($83E7),HL          
0B16: 3A E4 83        LD      A,($83E4)           
0B19: 67              LD      H,A                 
0B1A: 6F              LD      L,A                 
0B1B: 22 E5 83        LD      ($83E5),HL          
0B1E: C9              RET                         
0B1F: 11 E2 2E        LD      DE,$2EE2            
0B22: 21 60 AA        LD      HL,$AA60            
0B25: 06 08           LD      B,$08               
0B27: EF              RST     $28                 
0B28: 21 41 AA        LD      HL,$AA41            
0B2B: ED 5B EF 83     LD      DE,($83EF)          
0B2F: CD 95 0B        CALL    $0B95               ; {}
0B32: 3E 01           LD      A,$01               
0B34: 21 20 AB        LD      HL,$AB20            
0B37: CD A9 0B        CALL    $0BA9               ; {}
0B3A: 11 DF 2E        LD      DE,$2EDF            
0B3D: 06 03           LD      B,$03               
0B3F: EF              RST     $28                 
0B40: 21 41 AB        LD      HL,$AB41            
0B43: ED 5B ED 83     LD      DE,($83ED)          
0B47: CD 95 0B        CALL    $0B95               ; {}
0B4A: 3A 70 83        LD      A,($8370)           
0B4D: 3D              DEC     A                   
0B4E: C8              RET     Z                   
0B4F: 3E 02           LD      A,$02               
0B51: 21 00 A9        LD      HL,$A900            
0B54: CD A9 0B        CALL    $0BA9               ; {}
0B57: 11 DF 2E        LD      DE,$2EDF            
0B5A: 06 03           LD      B,$03               
0B5C: EF              RST     $28                 
0B5D: 21 21 A9        LD      HL,$A921            
0B60: ED 5B EB 83     LD      DE,($83EB)          
0B64: C3 95 0B        JP      $0B95               ; {}
0B67: 3A B4 83        LD      A,($83B4)           
0B6A: B7              OR      A                   
0B6B: 20 11           JR      NZ,$B7E             ; {}
0B6D: 3C              INC     A                   
0B6E: 32 B4 83        LD      ($83B4),A           
0B71: 21 1F A8        LD      HL,$A81F            
0B74: 11 20 00        LD      DE,$0020            
0B77: 01 10 20        LD      BC,$2010            
0B7A: 71              LD      (HL),C              
0B7B: 19              ADD     HL,DE               
0B7C: 10 FC           DJNZ    $B7A                ; {}
0B7E: 11 68 2F        LD      DE,$2F68            
0B81: 21 7F A9        LD      HL,$A97F            
0B84: 06 06           LD      B,$06               
0B86: EF              RST     $28                 
0B87: 3E 01           LD      A,$01               
0B89: 32 3F 80        LD      ($803F),A           
0B8C: 21 9F A8        LD      HL,$A89F            
0B8F: 3A E1 83        LD      A,($83E1)           
0B92: C3 A0 0B        JP      $0BA0               ; {}
0B95: CD 9B 0B        CALL    $0B9B               ; {}
0B98: AF              XOR     A                   
0B99: 18 0E           JR      $BA9                ; {}
0B9B: 7A              LD      A,D                 
0B9C: CD A0 0B        CALL    $0BA0               ; {}
0B9F: 7B              LD      A,E                 
0BA0: 4F              LD      C,A                 
0BA1: 0F              RRCA                        
0BA2: 0F              RRCA                        
0BA3: 0F              RRCA                        
0BA4: 0F              RRCA                        
0BA5: CD A9 0B        CALL    $0BA9               ; {}
0BA8: 79              LD      A,C                 
0BA9: E6 0F           AND     $0F                 
0BAB: 77              LD      (HL),A              
0BAC: 7D              LD      A,L                 
0BAD: D6 20           SUB     $20                 
0BAF: 6F              LD      L,A                 
0BB0: D0              RET     NC                  
0BB1: 25              DEC     H                   
0BB2: C9              RET                         
0BB3: 21 D8 83        LD      HL,$83D8            
0BB6: 35              DEC     (HL)                
0BB7: 2D              DEC     L                   
0BB8: AF              XOR     A                   
0BB9: 77              LD      (HL),A              
0BBA: 32 B3 83        LD      ($83B3),A           
0BBD: CD 81 07        CALL    $0781               ; {}
0BC0: 3E 03           LD      A,$03               
0BC2: 32 19 80        LD      ($8019),A           
0BC5: 21 1F 80        LD      HL,$801F            
0BC8: 06 05           LD      B,$05               
0BCA: AF              XOR     A                   
0BCB: 77              LD      (HL),A              
0BCC: 2C              INC     L                   
0BCD: 2C              INC     L                   
0BCE: 2C              INC     L                   
0BCF: 2C              INC     L                   
0BD0: 10 F9           DJNZ    $BCB                ; {}
0BD2: CD 3D 0C        CALL    $0C3D               ; {}
0BD5: 21 AC AA        LD      HL,$AAAC            
0BD8: 11 E5 2E        LD      DE,$2EE5            
0BDB: 06 0D           LD      B,$0D               
0BDD: EF              RST     $28                 
0BDE: 3E 01           LD      A,$01               
0BE0: 26 AA           LD      H,$AA               
0BE2: ED 47           LD      I,A                 
0BE4: 87              ADD     A,A                 
0BE5: C6 CD           ADD     $CD                 
0BE7: 6F              LD      L,A                 
0BE8: ED 57           LD      A,I                 
0BEA: CD A9 0B        CALL    $0BA9               ; {}
0BED: ED 57           LD      A,I                 
0BEF: 08              EX      AF,AF'              
0BF0: 06 03           LD      B,$03               
0BF2: EF              RST     $28                 
0BF3: D9              EXX                         
0BF4: 21 EF 83        LD      HL,$83EF            
0BF7: 08              EX      AF,AF'              
0BF8: 47              LD      B,A                 
0BF9: 2C              INC     L                   
0BFA: 2C              INC     L                   
0BFB: 10 FC           DJNZ    $BF9                ; {}
0BFD: 5E              LD      E,(HL)              
0BFE: 2C              INC     L                   
0BFF: 56              LD      D,(HL)              
0C00: 26 A9           LD      H,$A9               
0C02: 87              ADD     A,A                 
0C03: C6 ED           ADD     $ED                 
0C05: 6F              LD      L,A                 
0C06: CD 95 0B        CALL    $0B95               ; {}
0C09: 11 BA 2F        LD      DE,$2FBA            
0C0C: 06 04           LD      B,$04               
0C0E: EF              RST     $28                 
0C0F: ED 57           LD      A,I                 
0C11: D9              EXX                         
0C12: 3C              INC     A                   
0C13: FE 06           CP      $06                 
0C15: 20 C9           JR      NZ,$BE0             ; {}
0C17: 11 4D 2F        LD      DE,$2F4D            
0C1A: 21 FC AA        LD      HL,$AAFC            
0C1D: 06 0F           LD      B,$0F               
0C1F: AF              XOR     A                   
0C20: 32 39 80        LD      ($8039),A           
0C23: EF              RST     $28                 
0C24: C9              RET                         
0C25: 7A              LD      A,D                 
0C26: CD 2A 0C        CALL    $0C2A               ; {}
0C29: 7B              LD      A,E                 
0C2A: 4F              LD      C,A                 
0C2B: E6 0F           AND     $0F                 
0C2D: CD 35 0C        CALL    $0C35               ; {}
0C30: 79              LD      A,C                 
0C31: 0F              RRCA                        
0C32: 0F              RRCA                        
0C33: 0F              RRCA                        
0C34: 0F              RRCA                        
0C35: 77              LD      (HL),A              
0C36: 7D              LD      A,L                 
0C37: D6 20           SUB     $20                 
0C39: 6F              LD      L,A                 
0C3A: D0              RET     NC                  
0C3B: 25              DEC     H                   
0C3C: C9              RET                         
0C3D: 26 80           LD      H,$80               
0C3F: ED 4B FB 83     LD      BC,($83FB)          
0C43: 11 04 30        LD      DE,$3004            
0C46: CD 4A 0C        CALL    $0C4A               ; {}
0C49: 48              LD      C,B                 
0C4A: 7A              LD      A,D                 
0C4B: 91              SUB     C                   
0C4C: BA              CP      D                   
0C4D: C8              RET     Z                   
0C4E: 6F              LD      L,A                 
0C4F: 73              LD      (HL),E              
0C50: C9              RET                         
0C51: 21 76 AB        LD      HL,$AB76            
0C54: 11 9E 2F        LD      DE,$2F9E            
0C57: 06 0A           LD      B,$0A               
0C59: EF              RST     $28                 
0C5A: 21 77 AB        LD      HL,$AB77            
0C5D: 3E 10           LD      A,$10               
0C5F: CD A0 0B        CALL    $0BA0               ; {}
0C62: 11 BA 2F        LD      DE,$2FBA            
0C65: 06 04           LD      B,$04               
0C67: EF              RST     $28                 
0C68: 06 13           LD      B,$13               
0C6A: EF              RST     $28                 
0C6B: 18 4D           JR      $CBA                ; {}
0C6D: 21 D8 83        LD      HL,$83D8            
0C70: 2D              DEC     L                   
0C71: 7E              LD      A,(HL)              
0C72: B7              OR      A                   
0C73: 20 02           JR      NZ,$C77             ; {}
0C75: 36 05           LD      (HL),$05            
0C77: 35              DEC     (HL)                
0C78: 7E              LD      A,(HL)              
0C79: 87              ADD     A,A                 
0C7A: 21 82 0C        LD      HL,$0C82            
0C7D: 5F              LD      E,A                 
0C7E: 16 00           LD      D,$00               
0C80: 19              ADD     HL,DE               
0C81: E9              JP      (HL)                
0C82: 18 3C           JR      $CC0                ; {}
0C84: 18 CB           JR      $C51                ; {}
0C86: 18 63           JR      $CEB                ; {}
0C88: 18 3C           JR      $CC6                ; {}
0C8A: 3E 06           LD      A,$06               
0C8C: 32 1D 80        LD      ($801D),A           
0C8F: 32 23 80        LD      ($8023),A           
0C92: 32 29 80        LD      ($8029),A           
0C95: 32 2F 80        LD      ($802F),A           
0C98: 3E 03           LD      A,$03               
0C9A: 32 1B 80        LD      ($801B),A           
0C9D: 32 21 80        LD      ($8021),A           
0CA0: 32 27 80        LD      ($8027),A           
0CA3: 32 2D 80        LD      ($802D),A           
0CA6: 3E 10           LD      A,$10               
0CA8: 21 6D AB        LD      HL,$AB6D            
0CAB: CD A0 0B        CALL    $0BA0               ; {}
0CAE: 11 BA 2F        LD      DE,$2FBA            
0CB1: 06 04           LD      B,$04               
0CB3: EF              RST     $28                 
0CB4: 11 D1 2E        LD      DE,$2ED1            
0CB7: 06 0E           LD      B,$0E               
0CB9: EF              RST     $28                 
0CBA: 21 D8 83        LD      HL,$83D8            
0CBD: 36 80           LD      (HL),$80            
0CBF: C9              RET                         
0CC0: 21 D8 83        LD      HL,$83D8            
0CC3: 36 C0           LD      (HL),$C0            
0CC5: C9              RET                         
0CC6: 21 70 AB        LD      HL,$AB70            
0CC9: 3E 50           LD      A,$50               
0CCB: CD A0 0B        CALL    $0BA0               ; {}
0CCE: 11 BA 2F        LD      DE,$2FBA            
0CD1: 06 04           LD      B,$04               
0CD3: EF              RST     $28                 
0CD4: 11 43 2F        LD      DE,$2F43            
0CD7: 06 0A           LD      B,$0A               
0CD9: EF              RST     $28                 
0CDA: 11 AE 2F        LD      DE,$2FAE            
0CDD: 06 05           LD      B,$05               
0CDF: EF              RST     $28                 
0CE0: 21 71 AB        LD      HL,$AB71            
0CE3: 11 17 2F        LD      DE,$2F17            
0CE6: 06 13           LD      B,$13               
0CE8: EF              RST     $28                 
0CE9: 18 CF           JR      $CBA                ; {}
0CEB: 21 73 AB        LD      HL,$AB73            
0CEE: 11 00 10        LD      DE,$1000            
0CF1: CD 9B 0B        CALL    $0B9B               ; {}
0CF4: 11 BA 2F        LD      DE,$2FBA            
0CF7: 06 04           LD      B,$04               
0CF9: EF              RST     $28                 
0CFA: 11 39 2F        LD      DE,$2F39            
0CFD: 06 0A           LD      B,$0A               
0CFF: EF              RST     $28                 
0D00: 11 AE 2F        LD      DE,$2FAE            
0D03: 06 06           LD      B,$06               
0D05: EF              RST     $28                 
0D06: 21 74 AB        LD      HL,$AB74            
0D09: 11 2A 2F        LD      DE,$2F2A            
0D0C: 06 0F           LD      B,$0F               
0D0E: EF              RST     $28                 
0D0F: 18 A9           JR      $CBA                ; {}
0D11: 3A D8 83        LD      A,($83D8)           
0D14: B7              OR      A                   
0D15: C0              RET     NZ                  
0D16: 3A D6 83        LD      A,($83D6)           
0D19: FE 03           CP      $03                 
0D1B: CA B3 0B        JP      Z,$0BB3             ; {}
0D1E: 3A E1 83        LD      A,($83E1)           
0D21: B7              OR      A                   
0D22: C2 4C 0D        JP      NZ,$0D4C            ; {}
0D25: 3A D6 83        LD      A,($83D6)           
0D28: FE 04           CP      $04                 
0D2A: CA 6D 0C        JP      Z,$0C6D             ; {}
0D2D: FE 02           CP      $02                 
0D2F: CA 88 2D        JP      Z,$2D88             ; {}
0D32: FE 05           CP      $05                 
0D34: C0              RET     NZ                  
0D35: 21 D8 83        LD      HL,$83D8            
0D38: 36 30           LD      (HL),$30            
0D3A: 2D              DEC     L                   
0D3B: AF              XOR     A                   
0D3C: 77              LD      (HL),A              
0D3D: 32 15 80        LD      ($8015),A           
0D40: 11 01 2F        LD      DE,$2F01            
0D43: 21 CA AA        LD      HL,$AACA            
0D46: 06 0D           LD      B,$0D               
0D48: EF              RST     $28                 
0D49: C3 17 0C        JP      $0C17               ; {}
0D4C: CD E6 07        CALL    $07E6               ; {}
0D4F: 3A BA 83        LD      A,($83BA)           
0D52: B7              OR      A                   
0D53: C0              RET     NZ                  
0D54: 67              LD      H,A                 
0D55: 6F              LD      L,A                 
0D56: 22 93 82        LD      ($8293),HL          
0D59: 22 B3 81        LD      ($81B3),HL          
0D5C: 32 5B 82        LD      ($825B),A           
0D5F: 32 9A 82        LD      ($829A),A           
0D62: 3C              INC     A                   
0D63: 32 BA 83        LD      ($83BA),A           
0D66: CD 3D 22        CALL    $223D               ; {}
0D69: CD 04 08        CALL    $0804               ; {}
0D6C: CD 66 07        CALL    $0766               ; {}
0D6F: CD 4B 06        CALL    $064B               ; {}
0D72: 3E 04           LD      A,$04               
0D74: 32 1B 80        LD      ($801B),A           
0D77: 3E 06           LD      A,$06               
0D79: 32 29 80        LD      ($8029),A           
0D7C: 21 28 AA        LD      HL,$AA28            
0D7F: 11 77 2F        LD      DE,$2F77            
0D82: 06 04           LD      B,$04               
0D84: EF              RST     $28                 
0D85: 21 AD AA        LD      HL,$AAAD            
0D88: 1C              INC     E                   
0D89: 06 0C           LD      B,$0C               
0D8B: EF              RST     $28                 
0D8C: CD B9 0D        CALL    $0DB9               ; {}
0D8F: 21 74 AB        LD      HL,$AB74            
0D92: 11 88 2F        LD      DE,$2F88            
0D95: 06 03           LD      B,$03               
0D97: EF              RST     $28                 
0D98: 11 A8 2F        LD      DE,$2FA8            
0D9B: 06 06           LD      B,$06               
0D9D: EF              RST     $28                 
0D9E: 11 AE 2F        LD      DE,$2FAE            
0DA1: 06 05           LD      B,$05               
0DA3: EF              RST     $28                 
0DA4: 13              INC     DE                  
0DA5: 06 07           LD      B,$07               
0DA7: EF              RST     $28                 
0DA8: 21 94 A9        LD      HL,$A994            
0DAB: ED 5B 08 2E     LD      DE,($2E08)          ; {}
0DAF: CD 95 0B        CALL    $0B95               ; {}
0DB2: 11 BA 2F        LD      DE,$2FBA            
0DB5: 06 04           LD      B,$04               
0DB7: EF              RST     $28                 
0DB8: C9              RET                         
0DB9: 3A E1 83        LD      A,($83E1)           
0DBC: 11 88 2F        LD      DE,$2F88            
0DBF: 3D              DEC     A                   
0DC0: 28 11           JR      Z,$DD3              ; {}
0DC2: 3E 03           LD      A,$03               
0DC4: 32 23 80        LD      ($8023),A           
0DC7: 21 11 AB        LD      HL,$AB11            
0DCA: 06 04           LD      B,$04               
0DCC: EF              RST     $28                 
0DCD: 06 0D           LD      B,$0D               
0DCF: EF              RST     $28                 
0DD0: 36 23           LD      (HL),$23            
0DD2: C9              RET                         
                     
0DD3: 21 F1 AA        LD      HL,$AAF1            
0DD6: 06 04           LD      B,$04               
0DD8: EF              RST     $28                 
0DD9: 11 93 2F        LD      DE,$2F93            
0DDC: 06 0B           LD      B,$0B               
0DDE: EF              RST     $28                 
0DDF: C9              RET                         

0DE0: 3E 03           LD      A,$03               
0DE2: 32 0D 80        LD      ($800D),A           
0DE5: 32 0F 80        LD      ($800F),A           
0DE8: 3A BC 83        LD      A,($83BC)           
0DEB: 3D              DEC     A                   
0DEC: 32 BC 83        LD      ($83BC),A           
0DEF: C0              RET     NZ                  
0DF0: 3E 20           LD      A,$20               
0DF2: 32 BC 83        LD      ($83BC),A           
0DF5: 3A D7 83        LD      A,($83D7)           ; Splash letter number
0DF8: 87              ADD     A,A                 ; Times 2 (2 bytes each)
0DF9: 16 00           LD      D,$00               ; MSB = 0
0DFB: 5F              LD      E,A                 ; DE is now offset
0DFC: 21 FF 0D        LD      HL,$0DFF            ; Start number at 1 ... back up one slot
0DFF: 19              ADD     HL,DE               ; Point to letter routine
0E00: E9              JP      (HL)                ; Execute the routine

0E01: 18 46           JR      $E49                ; {} "R" (This is count 7)
0E03: 18 3A           JR      $E3F                ; {} "E"
0E05: 18 2E           JR      $E35                ; {} "G"
0E07: 18 22           JR      $E2B                ; {} "G"
0E09: 18 16           JR      $E21                ; {} "O"
0E0B: 18 0A           JR      $E17                ; {} "R"
;                                            ; "F"
0E0D: 21 06 AB        LD      HL,$AB06            ; Screen RAM
0E10: 11 40 80        LD      DE,$8040            
0E13: 3E D4           LD      A,$D4               ; Big "F"
0E15: 18 3A           JR      $E51                ; {}

0E17: 21 A6 AA        LD      HL,$AAA6            ; Screen RAM
0E1A: 11 44 80        LD      DE,$8044            
0E1D: 3E D8           LD      A,$D8               ; Big "R"
0E1F: 18 30           JR      $E51                ; {}
            
0E21: 21 46 AA        LD      HL,$AA46            ; Screen RAM
0E24: 11 48 80        LD      DE,$8048            
0E27: 3E DC           LD      A,$DC               ; Big "O"
0E29: 18 26           JR      $E51                ; {}
            
0E2B: 21 E6 A9        LD      HL,$A9E6            ; Screen RAM
0E2E: 11 4C 80        LD      DE,$804C            
0E31: 3E F4           LD      A,$F4               ; Big "G"
0E33: 18 1C           JR      $E51                ; {}
            
0E35: 21 86 A9        LD      HL,$A986            ; Screen RAM
0E38: 11 50 80        LD      DE,$8050            
0E3B: 3E F4           LD      A,$F4               ; Big "G"
0E3D: 18 12           JR      $E51                ; {}
            
0E3F: 21 26 A9        LD      HL,$A926            ; Screen RAM
0E42: 11 54 80        LD      DE,$8054            
0E45: 3E F8           LD      A,$F8               ; Big "E"
0E47: 18 08           JR      $E51                ; {}

0E49: 21 C6 A8        LD      HL,$A8C6            ; Screen RAM
0E4C: 11 58 80        LD      DE,$8058            
0E4F: 3E D8           LD      A,$D8               ; Big "R"
;
0E51: 01 1F 00        LD      BC,$001F            ; 31 -- offset to jump to next row
0E54: 77              LD      (HL),A              ; Store 1st tile
0E55: 3C              INC     A                   ; Next tile number
0E56: 2C              INC     L                   ; Next spot on screen
0E57: 77              LD      (HL),A              ; Store 2nd tile
0E58: 3C              INC     A                   ; Next tile number
0E59: 09              ADD     HL,BC               ; Next row
0E5A: 77              LD      (HL),A              ; Store 3rd tile
0E5B: 3C              INC     A                   ; Next tile number
0E5C: 2C              INC     L                   ; Next spot on screen
0E5D: 77              LD      (HL),A              ; Store 4th tile
0E5E: EB              EX      DE,HL               
0E5F: 01 00 04        LD      BC,$0400            ; B=4 (count) C=0 (value)
0E62: 71              LD      (HL),C              ; Zero out ??
0E63: 2C              INC     L                   ; Do ...
0E64: 10 FC           DJNZ    $E62                ; {} ... all ??
0E66: 21 D7 83        LD      HL,$83D7            
0E69: 35              DEC     (HL)                
0E6A: C0              RET     NZ                  
0E6B: 36 07           LD      (HL),$07            
0E6D: AF              XOR     A                   
0E6E: 32 BF 83        LD      ($83BF),A           
0E71: 32 BB 83        LD      ($83BB),A           
0E74: 3E 05           LD      A,$05               
0E76: 32 D6 83        LD      ($83D6),A           
0E79: C9              RET                         

0E7A: 3A E1 83        LD      A,($83E1)           
0E7D: B7              OR      A                   
0E7E: 20 F4           JR      NZ,$E74             ; {}
0E80: 21 BF 83        LD      HL,$83BF            
0E83: 7E              LD      A,(HL)              
0E84: B7              OR      A                   
0E85: 20 2D           JR      NZ,$EB4             ; {}
0E87: CD 66 07        CALL    $0766               ; {}
0E8A: CD 4B 06        CALL    $064B               ; {}
0E8D: 21 40 80        LD      HL,$8040            
0E90: 01 03 07        LD      BC,$0703            
0E93: 11 00 81        LD      DE,$8100            
0E96: 73              LD      (HL),E              
0E97: 2C              INC     L                   
0E98: 2C              INC     L                   
0E99: 71              LD      (HL),C              
0E9A: 2C              INC     L                   
0E9B: 72              LD      (HL),D              
0E9C: 2C              INC     L                   
0E9D: 10 F7           DJNZ    $E96                ; {}
0E9F: 21 04 05        LD      HL,$0504            
0EA2: 22 BD 83        LD      ($83BD),HL          
0EA5: 21 D7 83        LD      HL,$83D7            
0EA8: 36 07           LD      (HL),$07            
0EAA: 21 BC 83        LD      HL,$83BC            
0EAD: 36 20           LD      (HL),$20            
0EAF: 21 BF 83        LD      HL,$83BF            
0EB2: 34              INC     (HL)                
0EB3: C9              RET                         
0EB4: 3D              DEC     A                   
0EB5: 20 5F           JR      NZ,$F16             ; {}
0EB7: 3A D7 83        LD      A,($83D7)           
0EBA: 87              ADD     A,A                 
0EBB: 16 00           LD      D,$00               
0EBD: 5F              LD      E,A                 
0EBE: 21 C1 0E        LD      HL,$0EC1            
0EC1: 19              ADD     HL,DE               
0EC2: E9              JP      (HL)                
0EC3: 18 34           JR      $EF9                ; {}
0EC5: 18 2B           JR      $EF2                ; {}
0EC7: 18 22           JR      $EEB                ; {}
0EC9: 18 19           JR      $EE4                ; {}
0ECB: 18 10           JR      $EDD                ; {}
0ECD: 18 07           JR      $ED6                ; {}
0ECF: 21 40 80        LD      HL,$8040            
0ED2: 06 31           LD      B,$31               
0ED4: 18 28           JR      $EFE                ; {}
0ED6: 21 44 80        LD      HL,$8044            
0ED9: 06 49           LD      B,$49               
0EDB: 18 21           JR      $EFE                ; {}
0EDD: 21 48 80        LD      HL,$8048            
0EE0: 06 61           LD      B,$61               
0EE2: 18 1A           JR      $EFE                ; {}
0EE4: 21 4C 80        LD      HL,$804C            
0EE7: 06 79           LD      B,$79               
0EE9: 18 13           JR      $EFE                ; {}
0EEB: 21 50 80        LD      HL,$8050            
0EEE: 06 91           LD      B,$91               
0EF0: 18 0C           JR      $EFE                ; {}
0EF2: 21 54 80        LD      HL,$8054            
0EF5: 06 A9           LD      B,$A9               
0EF7: 18 05           JR      $EFE                ; {}
0EF9: 21 58 80        LD      HL,$8058            
0EFC: 06 C1           LD      B,$C1               
0EFE: CD 3E 0F        CALL    $0F3E               ; {}
0F01: 4F              LD      C,A                 
0F02: 35              DEC     (HL)                
0F03: 35              DEC     (HL)                
0F04: 35              DEC     (HL)                
0F05: 35              DEC     (HL)                
0F06: 7E              LD      A,(HL)              
0F07: 2C              INC     L                   
0F08: 71              LD      (HL),C              
0F09: B8              CP      B                   
0F0A: D0              RET     NC                  
0F0B: 36 1E           LD      (HL),$1E            
0F0D: 21 D7 83        LD      HL,$83D7            
0F10: 35              DEC     (HL)                
0F11: C0              RET     NZ                  
0F12: 36 14           LD      (HL),$14            
0F14: 18 99           JR      $EAF                ; {}
0F16: 3D              DEC     A                   
0F17: C2 E0 0D        JP      NZ,$0DE0            ; {}
0F1A: CD 3E 0F        CALL    $0F3E               ; {}
0F1D: D6 03           SUB     $03                 
0F1F: 4F              LD      C,A                 
0F20: 3A D7 83        LD      A,($83D7)           
0F23: B7              OR      A                   
0F24: CA A5 0E        JP      Z,$0EA5             ; {}
0F27: 06 07           LD      B,$07               
0F29: 11 06 00        LD      DE,$0006            
0F2C: 21 43 80        LD      HL,$8043            
0F2F: 35              DEC     (HL)                
0F30: 35              DEC     (HL)                
0F31: 35              DEC     (HL)                
0F32: 35              DEC     (HL)                
0F33: 2D              DEC     L                   
0F34: 2D              DEC     L                   
0F35: 71              LD      (HL),C              
0F36: 19              ADD     HL,DE               
0F37: 10 F6           DJNZ    $F2F                ; {}
0F39: 3D              DEC     A                   
0F3A: 32 D7 83        LD      ($83D7),A           
0F3D: C9              RET                         
0F3E: E5              PUSH    HL                  
0F3F: 21 BD 83        LD      HL,$83BD            
0F42: 35              DEC     (HL)                
0F43: 20 11           JR      NZ,$F56             ; {}
0F45: 36 08           LD      (HL),$08            
0F47: 2C              INC     L                   
0F48: 35              DEC     (HL)                
0F49: 20 02           JR      NZ,$F4D             ; {}
0F4B: 36 04           LD      (HL),$04            
0F4D: 7E              LD      A,(HL)              
0F4E: 21 1B 2E        LD      HL,$2E1B            
0F51: 85              ADD     A,L                 
0F52: 6F              LD      L,A                 
0F53: 7E              LD      A,(HL)              
0F54: E1              POP     HL                  
0F55: C9              RET                         
0F56: F1              POP     AF                  
0F57: F1              POP     AF                  
0F58: C9              RET                         
0F59: 21 50 A8        LD      HL,$A850            
0F5C: CD E2 19        CALL    $19E2               ; {}
0F5F: 21 70 AA        LD      HL,$AA70            
0F62: 11 0E 2F        LD      DE,$2F0E            
0F65: 06 09           LD      B,$09               
0F67: EF              RST     $28                 
0F68: C9              RET                         
0F69: ED 5B ED 83     LD      DE,($83ED)          
0F6D: 2A EB 83        LD      HL,($83EB)          
0F70: 44              LD      B,H                 
0F71: 4D              LD      C,L                 
0F72: B7              OR      A                   
0F73: ED 52           SBC     HL,DE               
0F75: 38 05           JR      C,$F7C              ; {}
0F77: D5              PUSH    DE                  
0F78: C5              PUSH    BC                  
0F79: D1              POP     DE                  
0F7A: 18 01           JR      $F7D                ; {}
0F7C: C5              PUSH    BC                  
0F7D: CD 84 0A        CALL    $0A84               ; {}
0F80: D1              POP     DE                  
0F81: F5              PUSH    AF                  
0F82: CD 84 0A        CALL    $0A84               ; {}
0F85: 67              LD      H,A                 
0F86: F1              POP     AF                  
0F87: 6F              LD      L,A                 
0F88: 22 FB 83        LD      ($83FB),HL          
0F8B: C9              RET                         
0F8C: 3A 18 81        LD      A,($8118)           
0F8F: A7              AND     A                   
0F90: C8              RET     Z                   
0F91: 11 06 A8        LD      DE,$A806            
0F94: 06 08           LD      B,$08               
0F96: 21 13 14        LD      HL,$1413            
0F99: 7E              LD      A,(HL)              
0F9A: 12              LD      (DE),A              
0F9B: 23              INC     HL                  
0F9C: 13              INC     DE                  
0F9D: 7E              LD      A,(HL)              
0F9E: 12              LD      (DE),A              
0F9F: 23              INC     HL                  
0FA0: C5              PUSH    BC                  
0FA1: 01 1F 00        LD      BC,$001F            
0FA4: EB              EX      DE,HL               
0FA5: 09              ADD     HL,BC               
0FA6: EB              EX      DE,HL               
0FA7: C1              POP     BC                  
0FA8: 10 EF           DJNZ    $F99                ; {}
0FAA: AF              XOR     A                   
0FAB: 32 18 81        LD      ($8118),A           
0FAE: C9              RET                         
0FAF: 2A 00 80        LD      HL,($8000)          
0FB2: 01 BE 0F        LD      BC,$0FBE            
0FB5: 26 00           LD      H,$00               
0FB7: 29              ADD     HL,HL               
0FB8: 09              ADD     HL,BC               
0FB9: 4E              LD      C,(HL)              
0FBA: 23              INC     HL                  
0FBB: 66              LD      H,(HL)              
0FBC: 69              LD      L,C                 
0FBD: E9              JP      (HL)                
0FBE: D4 0F 58        CALL    NC,$580F            
0FC1: 10 7B           DJNZ    $103E               ; {}
0FC3: 10 9B           DJNZ    $F60                ; {}
0FC5: 10 BB           DJNZ    $F82                ; {}
0FC7: 10 DB           DJNZ    $FA4                ; {}
0FC9: 10 F8           DJNZ    $FC3                ; {}
0FCB: 10 18           DJNZ    $FE5                ; {}
0FCD: 11 38 11        LD      DE,$1138            
0FD0: 58              LD      E,B                 
0FD1: 11 78 11        LD      DE,$1178            
0FD4: 21 70 82        LD      HL,$8270            
0FD7: 7E              LD      A,(HL)              
0FD8: 23              INC     HL                  
0FD9: 46              LD      B,(HL)              
0FDA: 23              INC     HL                  
0FDB: 4E              LD      C,(HL)              
0FDC: 2A ED 13        LD      HL,($13ED)          ; {}
0FDF: 11 03 14        LD      DE,$1403            
0FE2: DD 21 00 81     LD      IX,$8100            
0FE6: FD 21 00 81     LD      IY,$8100            
0FEA: 32 B1 81        LD      ($81B1),A           
0FED: ED 53 01 80     LD      ($8001),DE          
0FF1: E5              PUSH    HL                  
0FF2: C5              PUSH    BC                  
0FF3: D5              PUSH    DE                  
0FF4: CD 98 11        CALL    $1198               ; {}
0FF7: 3A 5B 82        LD      A,($825B)           
0FFA: A7              AND     A                   
0FFB: 20 0B           JR      NZ,$1008            ; {}
0FFD: 79              LD      A,C                 
0FFE: 2F              CPL                         
0FFF: 3C              INC     A                   
1000: DD 77 01        LD      (IX+$01),A          
1003: DD 23           INC     IX                  
1005: FD 34 00        INC     (IY+$00)            
1008: D1              POP     DE                  
1009: C1              POP     BC                  
100A: E1              POP     HL                  
100B: 78              LD      A,B                 
100C: 32 03 80        LD      ($8003),A           
100F: 1A              LD      A,(DE)              
1010: 77              LD      (HL),A              
1011: 23              INC     HL                  
1012: 13              INC     DE                  
1013: 1A              LD      A,(DE)              
1014: 77              LD      (HL),A              
1015: 2B              DEC     HL                  
1016: D5              PUSH    DE                  
1017: 11 20 00        LD      DE,$0020            
101A: 19              ADD     HL,DE               
101B: D1              POP     DE                  
101C: 10 1A           DJNZ    $1038               ; {}
101E: 3A B1 81        LD      A,($81B1)           
1021: 5F              LD      E,A                 
1022: 16 00           LD      D,$00               
1024: 19              ADD     HL,DE               
1025: 0D              DEC     C                   
1026: C2 3C 10        JP      NZ,$103C            ; {}
1029: 21 00 80        LD      HL,$8000            
102C: 34              INC     (HL)                
102D: 7E              LD      A,(HL)              
102E: FE 0B           CP      $0B                 
1030: DA AF 0F        JP      C,$0FAF             ; {}
1033: AF              XOR     A                   
1034: 77              LD      (HL),A              
1035: C3 47 10        JP      $1047               ; {}
1038: 13              INC     DE                  
1039: C3 0F 10        JP      $100F               ; {}
103C: ED 5B 01 80     LD      DE,($8001)          
1040: 3A 03 80        LD      A,($8003)           
1043: 47              LD      B,A                 
1044: C3 F1 0F        JP      $0FF1               ; {}
1047: C9              RET                         
1048: 01 FF EF        LD      BC,$EFFF            
104B: 3A 00 88        LD      A,($8800)           ; {hard.watchdog}
104E: 0B              DEC     BC                  
104F: 78              LD      A,B                 
1050: A7              AND     A                   
1051: 20 F8           JR      NZ,$104B            ; {}
1053: 79              LD      A,C                 
1054: A7              AND     A                   
1055: 20 F4           JR      NZ,$104B            ; {}
1057: C9              RET                         
1058: CD 8C 0F        CALL    $0F8C               ; {}
105B: 21 73 82        LD      HL,$8273            
105E: 7E              LD      A,(HL)              
105F: 23              INC     HL                  
1060: 46              LD      B,(HL)              
1061: 23              INC     HL                  
1062: 4E              LD      C,(HL)              
1063: 2A EF 13        LD      HL,($13EF)          ; {}
1066: 11 23 14        LD      DE,$1423            
1069: DD 21 09 81     LD      IX,$8109            
106D: FD 21 09 81     LD      IY,$8109            
1071: 32 B1 81        LD      ($81B1),A           
1074: ED 53 01 80     LD      ($8001),DE          
1078: C3 F1 0F        JP      $0FF1               ; {}
107B: 21 76 82        LD      HL,$8276            
107E: 7E              LD      A,(HL)              
107F: 23              INC     HL                  
1080: 46              LD      B,(HL)              
1081: 23              INC     HL                  
1082: 4E              LD      C,(HL)              
1083: 2A F1 13        LD      HL,($13F1)          ; {}
1086: 11 3B 14        LD      DE,$143B            
1089: DD 21 12 81     LD      IX,$8112            
108D: FD 21 12 81     LD      IY,$8112            
1091: 32 B1 81        LD      ($81B1),A           
1094: ED 53 01 80     LD      ($8001),DE          
1098: C3 F1 0F        JP      $0FF1               ; {}
109B: 21 79 82        LD      HL,$8279            
109E: 7E              LD      A,(HL)              
109F: 23              INC     HL                  
10A0: 46              LD      B,(HL)              
10A1: 23              INC     HL                  
10A2: 4E              LD      C,(HL)              
10A3: 2A F3 13        LD      HL,($13F3)          ; {}
10A6: 11 53 14        LD      DE,$1453            
10A9: DD 21 1B 81     LD      IX,$811B            
10AD: FD 21 1B 81     LD      IY,$811B            
10B1: 32 B1 81        LD      ($81B1),A           
10B4: ED 53 01 80     LD      ($8001),DE          
10B8: C3 F1 0F        JP      $0FF1               ; {}
10BB: 21 7C 82        LD      HL,$827C            
10BE: 7E              LD      A,(HL)              
10BF: 23              INC     HL                  
10C0: 46              LD      B,(HL)              
10C1: 23              INC     HL                  
10C2: 4E              LD      C,(HL)              
10C3: 2A F5 13        LD      HL,($13F5)          ; {}
10C6: 11 5F 14        LD      DE,$145F            
10C9: DD 21 24 81     LD      IX,$8124            
10CD: FD 21 24 81     LD      IY,$8124            
10D1: 32 B1 81        LD      ($81B1),A           
10D4: ED 53 01 80     LD      ($8001),DE          
10D8: C3 F1 0F        JP      $0FF1               ; {}
10DB: C3 29 10        JP      $1029               ; {}
10DE: 11 9B 14        LD      DE,$149B            
10E1: 01 04 02        LD      BC,$0204            
10E4: DD 21 2D 81     LD      IX,$812D            
10E8: FD 21 2D 81     LD      IY,$812D            
10EC: 3E 80           LD      A,$80               
10EE: 32 B1 81        LD      ($81B1),A           
10F1: ED 53 01 80     LD      ($8001),DE          
10F5: C3 F1 0F        JP      $0FF1               ; {}
10F8: 21 82 82        LD      HL,$8282            
10FB: 7E              LD      A,(HL)              
10FC: 23              INC     HL                  
10FD: 46              LD      B,(HL)              
10FE: 23              INC     HL                  
10FF: 4E              LD      C,(HL)              
1100: 2A F9 13        LD      HL,($13F9)          ; {}
1103: 11 9F 14        LD      DE,$149F            
1106: DD 21 36 81     LD      IX,$8136            
110A: FD 21 36 81     LD      IY,$8136            
110E: 32 B1 81        LD      ($81B1),A           
1111: ED 53 01 80     LD      ($8001),DE          
1115: C3 F1 0F        JP      $0FF1               ; {}
1118: 21 85 82        LD      HL,$8285            
111B: 7E              LD      A,(HL)              
111C: 23              INC     HL                  
111D: 46              LD      B,(HL)              
111E: 23              INC     HL                  
111F: 4E              LD      C,(HL)              
1120: 2A FB 13        LD      HL,($13FB)          ; {}
1123: 11 A7 14        LD      DE,$14A7            
1126: DD 21 3F 81     LD      IX,$813F            
112A: FD 21 3F 81     LD      IY,$813F            
112E: 32 B1 81        LD      ($81B1),A           
1131: ED 53 01 80     LD      ($8001),DE          
1135: C3 F1 0F        JP      $0FF1               ; {}
1138: 21 88 82        LD      HL,$8288            
113B: 7E              LD      A,(HL)              
113C: 23              INC     HL                  
113D: 46              LD      B,(HL)              
113E: 23              INC     HL                  
113F: 4E              LD      C,(HL)              
1140: 2A FD 13        LD      HL,($13FD)          ; {}
1143: 11 AB 14        LD      DE,$14AB            
1146: DD 21 48 81     LD      IX,$8148            
114A: FD 21 48 81     LD      IY,$8148            
114E: 32 B1 81        LD      ($81B1),A           
1151: ED 53 01 80     LD      ($8001),DE          
1155: C3 F1 0F        JP      $0FF1               ; {}
1158: 21 8B 82        LD      HL,$828B            
115B: 7E              LD      A,(HL)              
115C: 23              INC     HL                  
115D: 46              LD      B,(HL)              
115E: 23              INC     HL                  
115F: 4E              LD      C,(HL)              
1160: 2A FF 13        LD      HL,($13FF)          ; {}
1163: 11 AF 14        LD      DE,$14AF            
1166: DD 21 51 81     LD      IX,$8151            
116A: FD 21 51 81     LD      IY,$8151            
116E: 32 B1 81        LD      ($81B1),A           
1171: ED 53 01 80     LD      ($8001),DE          
1175: C3 F1 0F        JP      $0FF1               ; {}
1178: 21 8E 82        LD      HL,$828E            
117B: 7E              LD      A,(HL)              
117C: 23              INC     HL                  
117D: 46              LD      B,(HL)              
117E: 23              INC     HL                  
117F: 4E              LD      C,(HL)              
1180: 2A 01 14        LD      HL,($1401)          ; {}
1183: 11 B3 14        LD      DE,$14B3            
1186: DD 21 5A 81     LD      IX,$815A            
118A: FD 21 5A 81     LD      IY,$815A            
118E: 32 B1 81        LD      ($81B1),A           
1191: ED 53 01 80     LD      ($8001),DE          
1195: C3 F1 0F        JP      $0FF1               ; {}
1198: 11 00 A8        LD      DE,$A800            
119B: ED 52           SBC     HL,DE               
119D: 7D              LD      A,L                 
119E: 01 00 06        LD      BC,$0600            
11A1: E6 E0           AND     $E0                 
11A3: 6F              LD      L,A                 
11A4: 7C              LD      A,H                 
11A5: E6 04           AND     $04                 
11A7: CA B0 11        JP      Z,$11B0             ; {}
11AA: CB 01           RLC     C                   
11AC: 0C              INC     C                   
11AD: C3 B2 11        JP      $11B2               ; {}
11B0: CB 01           RLC     C                   
11B2: CB 05           RLC     L                   
11B4: CB 14           RL      H                   
11B6: 10 EC           DJNZ    $11A4               ; {}
11B8: CB 01           RLC     C                   
11BA: CB 01           RLC     C                   
11BC: CB 01           RLC     C                   
11BE: C9              RET                         
11BF: 3A CD 83        LD      A,($83CD)           
11C2: B7              OR      A                   
11C3: C0              RET     NZ                  
11C4: 3A 04 80        LD      A,($8004)           
11C7: A7              AND     A                   
11C8: C0              RET     NZ                  
11C9: 21 47 80        LD      HL,$8047            
11CC: 7E              LD      A,(HL)              
11CD: 4F              LD      C,A                 
11CE: E6 0F           AND     $0F                 
11D0: FE 09           CP      $09                 
11D2: D2 09 12        JP      NC,$1209            ; {}
11D5: 79              LD      A,C                 
11D6: E6 F0           AND     $F0                 
11D8: 0F              RRCA                        
11D9: 0F              RRCA                        
11DA: 0F              RRCA                        
11DB: 0F              RRCA                        
11DC: 6F              LD      L,A                 
11DD: 26 00           LD      H,$00               
11DF: 01 E9 11        LD      BC,$11E9            
11E2: 29              ADD     HL,HL               
11E3: 09              ADD     HL,BC               
11E4: 4E              LD      C,(HL)              
11E5: 23              INC     HL                  
11E6: 66              LD      H,(HL)              
11E7: 69              LD      L,C                 
11E8: E9              JP      (HL)                
11E9: 09              ADD     HL,BC               
11EA: 12              LD      (DE),A              
11EB: 0C              INC     C                   
11EC: 12              LD      (DE),A              
11ED: 0F              RRCA                        
11EE: 12              LD      (DE),A              
11EF: 12              LD      (DE),A              
11F0: 12              LD      (DE),A              
11F1: 1A              LD      A,(DE)              
11F2: 12              LD      (DE),A              
11F3: 22 12 2A        LD      ($2A12),HL          ; {}
11F6: 12              LD      (DE),A              
11F7: 32 12 3A        LD      ($3A12),A           
11FA: 12              LD      (DE),A              
11FB: 42              LD      B,D                 
11FC: 12              LD      (DE),A              
11FD: 4A              LD      C,D                 
11FE: 12              LD      (DE),A              
11FF: 52              LD      D,D                 
1200: 12              LD      (DE),A              
1201: 5A              LD      E,D                 
1202: 12              LD      (DE),A              
1203: 62              LD      H,D                 
1204: 12              LD      (DE),A              
1205: 6A              LD      L,D                 
1206: 12              LD      (DE),A              
1207: 6D              LD      L,L                 
1208: 12              LD      (DE),A              
1209: C3 E4 12        JP      $12E4               ; {}
120C: C3 E4 12        JP      $12E4               ; {}
120F: C3 E4 12        JP      $12E4               ; {}
1212: 21 00 81        LD      HL,$8100            
1215: 0E 3C           LD      C,$3C               
1217: C3 70 12        JP      $1270               ; {}
121A: 21 09 81        LD      HL,$8109            
121D: 0E 1F           LD      C,$1F               
121F: C3 70 12        JP      $1270               ; {}
1222: 21 12 81        LD      HL,$8112            
1225: 0E 5C           LD      C,$5C               
1227: C3 70 12        JP      $1270               ; {}
122A: 21 1B 81        LD      HL,$811B            
122D: 0E 2C           LD      C,$2C               
122F: C3 70 12        JP      $1270               ; {}
1232: 21 24 81        LD      HL,$8124            
1235: 0E 2F           LD      C,$2F               
1237: C3 70 12        JP      $1270               ; {}
123A: C3 E4 12        JP      $12E4               ; {}
123D: 0E 17           LD      C,$17               
123F: C3 70 12        JP      $1270               ; {}
1242: 21 36 81        LD      HL,$8136            
1245: 0E 22           LD      C,$22               
1247: C3 70 12        JP      $1270               ; {}
124A: 21 3F 81        LD      HL,$813F            
124D: 0E 12           LD      C,$12               
124F: C3 70 12        JP      $1270               ; {}
1252: 21 48 81        LD      HL,$8148            
1255: 0E 12           LD      C,$12               
1257: C3 70 12        JP      $1270               ; {}
125A: 21 51 81        LD      HL,$8151            
125D: 0E 12           LD      C,$12               
125F: C3 70 12        JP      $1270               ; {}
1262: 21 5A 81        LD      HL,$815A            
1265: 0E 12           LD      C,$12               
1267: C3 70 12        JP      $1270               ; {}
126A: C3 E4 12        JP      $12E4               ; {}
126D: C3 E4 12        JP      $12E4               ; {}
1270: 3A 47 80        LD      A,($8047)           
1273: FE 80           CP      $80                 
1275: DA 99 12        JP      C,$1299             ; {}
1278: 3A 44 80        LD      A,($8044)           
127B: C6 03           ADD     $03                 
127D: 57              LD      D,A                 
127E: 81              ADD     A,C                 
127F: 5F              LD      E,A                 
1280: 46              LD      B,(HL)              
1281: DA A1 12        JP      C,$12A1             ; {}
1284: 23              INC     HL                  
1285: 7E              LD      A,(HL)              
1286: BA              CP      D                   
1287: DA B6 12        JP      C,$12B6             ; {}
128A: BB              CP      E                   
128B: D2 B6 12        JP      NC,$12B6            ; {}
128E: 3A 47 80        LD      A,($8047)           
1291: FE 80           CP      $80                 
1293: DA E4 12        JP      C,$12E4             ; {}
1296: C3 D0 12        JP      $12D0               ; {}
1299: 3A 44 80        LD      A,($8044)           
129C: C6 0C           ADD     $0C                 
129E: C3 7D 12        JP      $127D               ; {}
12A1: 23              INC     HL                  
12A2: 7E              LD      A,(HL)              
12A3: BA              CP      D                   
12A4: D2 AB 12        JP      NC,$12AB            ; {}
12A7: BB              CP      E                   
12A8: D2 C3 12        JP      NC,$12C3            ; {}
12AB: 3A 47 80        LD      A,($8047)           
12AE: FE 80           CP      $80                 
12B0: DA E4 12        JP      C,$12E4             ; {}
12B3: C3 D0 12        JP      $12D0               ; {}
12B6: 10 CC           DJNZ    $1284               ; {}
12B8: 3A 47 80        LD      A,($8047)           
12BB: FE 80           CP      $80                 
12BD: DA D0 12        JP      C,$12D0             ; {}
12C0: C3 E4 12        JP      $12E4               ; {}
12C3: 10 DC           DJNZ    $12A1               ; {}
12C5: 3A 47 80        LD      A,($8047)           
12C8: FE 80           CP      $80                 
12CA: DA D0 12        JP      C,$12D0             ; {}
12CD: C3 E4 12        JP      $12E4               ; {}
12D0: 3E 01           LD      A,$01               
12D2: 32 04 80        LD      ($8004),A           
12D5: 3A 47 80        LD      A,($8047)           
12D8: FE 80           CP      $80                 
12DA: D0              RET     NC                  
12DB: FE 30           CP      $30                 
12DD: D8              RET     C                   
12DE: 3E 01           LD      A,$01               
12E0: 32 9C 82        LD      ($829C),A           
12E3: C9              RET                         
12E4: 3A 04 80        LD      A,($8004)           
12E7: A7              AND     A                   
12E8: C0              RET     NZ                  
12E9: 21 47 80        LD      HL,$8047            
12EC: 7E              LD      A,(HL)              
12ED: C6 0F           ADD     $0F                 
12EF: 4F              LD      C,A                 
12F0: E6 0F           AND     $0F                 
12F2: FE 05           CP      $05                 
12F4: DA 2B 13        JP      C,$132B             ; {}
12F7: 79              LD      A,C                 
12F8: E6 F0           AND     $F0                 
12FA: 0F              RRCA                        
12FB: 0F              RRCA                        
12FC: 0F              RRCA                        
12FD: 0F              RRCA                        
12FE: 6F              LD      L,A                 
12FF: 26 00           LD      H,$00               
1301: 01 0B 13        LD      BC,$130B            
1304: 29              ADD     HL,HL               
1305: 09              ADD     HL,BC               
1306: 4E              LD      C,(HL)              
1307: 23              INC     HL                  
1308: 66              LD      H,(HL)              
1309: 69              LD      L,C                 
130A: E9              JP      (HL)                
130B: 2B              DEC     HL                  
130C: 13              INC     DE                  
130D: 2E 13           LD      L,$13               
130F: 31 13 34        LD      SP,$3413            
1312: 13              INC     DE                  
1313: 3C              INC     A                   
1314: 13              INC     DE                  
1315: 44              LD      B,H                 
1316: 13              INC     DE                  
1317: 4C              LD      C,H                 
1318: 13              INC     DE                  
1319: 54              LD      D,H                 
131A: 13              INC     DE                  
131B: 5C              LD      E,H                 
131C: 13              INC     DE                  
131D: 64              LD      H,H                 
131E: 13              INC     DE                  
131F: 6C              LD      L,H                 
1320: 13              INC     DE                  
1321: 74              LD      (HL),H              
1322: 13              INC     DE                  
1323: 7C              LD      A,H                 
1324: 13              INC     DE                  
1325: 84              ADD     A,H                 
1326: 13              INC     DE                  
1327: 8C              ADC     A,H                 
1328: 13              INC     DE                  
1329: 8C              ADC     A,H                 
132A: 13              INC     DE                  
132B: C3 E1 13        JP      $13E1               ; {}
132E: C3 E1 13        JP      $13E1               ; {}
1331: C3 E1 13        JP      $13E1               ; {}
1334: 21 00 81        LD      HL,$8100            
1337: 0E 3C           LD      C,$3C               
1339: C3 8F 13        JP      $138F               ; {}
133C: 21 09 81        LD      HL,$8109            
133F: 0E 1F           LD      C,$1F               
1341: C3 8F 13        JP      $138F               ; {}
1344: 21 12 81        LD      HL,$8112            
1347: 0E 5C           LD      C,$5C               
1349: C3 8F 13        JP      $138F               ; {}
134C: 21 1B 81        LD      HL,$811B            
134F: 0E 2C           LD      C,$2C               
1351: C3 8F 13        JP      $138F               ; {}
1354: 21 24 81        LD      HL,$8124            
1357: 0E 2F           LD      C,$2F               
1359: C3 8F 13        JP      $138F               ; {}
135C: C3 E1 13        JP      $13E1               ; {}
135F: 0E 17           LD      C,$17               
1361: C3 8F 13        JP      $138F               ; {}
1364: 21 36 81        LD      HL,$8136            
1367: 0E 22           LD      C,$22               
1369: C3 8F 13        JP      $138F               ; {}
136C: 21 3F 81        LD      HL,$813F            
136F: 0E 12           LD      C,$12               
1371: C3 8F 13        JP      $138F               ; {}
1374: 21 48 81        LD      HL,$8148            
1377: 0E 12           LD      C,$12               
1379: C3 8F 13        JP      $138F               ; {}
137C: 21 51 81        LD      HL,$8151            
137F: 0E 12           LD      C,$12               
1381: C3 8F 13        JP      $138F               ; {}
1384: 21 5A 81        LD      HL,$815A            
1387: 0E 12           LD      C,$12               
1389: C3 8F 13        JP      $138F               ; {}
138C: C3 E1 13        JP      $13E1               ; {}
138F: 3A 2F 80        LD      A,($802F)           
1392: FE 80           CP      $80                 
1394: DA B9 13        JP      C,$13B9             ; {}
1397: 3A 44 80        LD      A,($8044)           
139A: C6 03           ADD     $03                 
139C: 57              LD      D,A                 
139D: 81              ADD     A,C                 
139E: 5F              LD      E,A                 
139F: 46              LD      B,(HL)              
13A0: DA C1 13        JP      C,$13C1             ; {}
13A3: 23              INC     HL                  
13A4: 7E              LD      A,(HL)              
13A5: BA              CP      D                   
13A6: DA D7 13        JP      C,$13D7             ; {}
13A9: BB              CP      E                   
13AA: D2 D7 13        JP      NC,$13D7            ; {}
13AD: 3A 47 80        LD      A,($8047)           
13B0: FE 80           CP      $80                 
13B2: D8              RET     C                   
13B3: 3E 01           LD      A,$01               
13B5: 32 04 80        LD      ($8004),A           
13B8: C9              RET                         
13B9: 3A 44 80        LD      A,($8044)           
13BC: C6 0C           ADD     $0C                 
13BE: C3 9C 13        JP      $139C               ; {}
13C1: 23              INC     HL                  
13C2: 7E              LD      A,(HL)              
13C3: BA              CP      D                   
13C4: D2 CB 13        JP      NC,$13CB            ; {}
13C7: BB              CP      E                   
13C8: D2 E2 13        JP      NC,$13E2            ; {}
13CB: 3A 47 80        LD      A,($8047)           
13CE: FE 80           CP      $80                 
13D0: D8              RET     C                   
13D1: 3E 01           LD      A,$01               
13D3: 32 04 80        LD      ($8004),A           
13D6: C9              RET                         
13D7: 10 CA           DJNZ    $13A3               ; {}
13D9: 3A 47 80        LD      A,($8047)           
13DC: FE 80           CP      $80                 
13DE: DA D0 12        JP      C,$12D0             ; {}
13E1: C9              RET                         
13E2: 10 DD           DJNZ    $13C1               ; {}
13E4: 3A 47 80        LD      A,($8047)           
13E7: FE 80           CP      $80                 
13E9: DA D0 12        JP      C,$12D0             ; {}
13EC: C9              RET                         
13ED: 06 A8           LD      B,$A8               
13EF: 08              EX      AF,AF'              
13F0: A8              XOR     B                   
13F1: 0A              LD      A,(BC)              
13F2: A8              XOR     B                   
13F3: 0C              INC     C                   
13F4: A8              XOR     B                   
13F5: 0E A8           LD      C,$A8               
13F7: 10 A8           DJNZ    $13A1               ; {}
13F9: 12              LD      (DE),A              
13FA: A8              XOR     B                   
13FB: 14              INC     D                   
13FC: A8              XOR     B                   
13FD: 16 A8           LD      D,$A8               
13FF: 18 A8           JR      $13A9               ; {}
1401: 1A              LD      A,(DE)              
1402: A8              XOR     B                   
1403: 5C              LD      E,H                 
1404: 5D              LD      E,L                 
1405: 5E              LD      E,(HL)              
1406: 5F              LD      E,A                 
1407: 58              LD      E,B                 
1408: 59              LD      E,C                 
1409: 5A              LD      E,D                 
140A: 5B              LD      E,E                 
140B: 58              LD      E,B                 
140C: 59              LD      E,C                 
140D: 5A              LD      E,D                 
140E: 5B              LD      E,E                 
140F: 54              LD      D,H                 
1410: 55              LD      D,L                 
1411: 56              LD      D,(HL)              
1412: 57              LD      D,A                 
1413: 10 10           DJNZ    $1425               ; {}
1415: 10 10           DJNZ    $1427               ; {}
1417: D0              RET     NC                  
1418: D1              POP     DE                  
1419: D2 D3 CC        JP      NC,$CCD3            ; {hard.PPI8255+CD3}
141C: CD CE CF        CALL    $CFCE               ; {hard.PPI8255+FCE}
141F: C8              RET     Z                   
1420: C9              RET                         
1421: CA CB 34        JP      Z,$34CB             
1424: 35              DEC     (HL)                
1425: 36 37           LD      (HL),$37            
1427: 34              INC     (HL)                
1428: 35              DEC     (HL)                
1429: 36 37           LD      (HL),$37            
142B: 38 39           JR      C,$1466             ; {}
142D: 3A 3B 38        LD      A,($383B)           
1430: 39              ADD     HL,SP               
1431: 3A 3B 3C        LD      A,($3C3B)           
1434: 3D              DEC     A                   
1435: 3E 3F           LD      A,$3F               
1437: 3C              INC     A                   
1438: 3D              DEC     A                   
1439: 3E 3F           LD      A,$3F               
143B: 5C              LD      E,H                 
143C: 5D              LD      E,L                 
143D: 5E              LD      E,(HL)              
143E: 5F              LD      E,A                 
143F: 58              LD      E,B                 
1440: 59              LD      E,C                 
1441: 5A              LD      E,D                 
1442: 5B              LD      E,E                 
1443: 58              LD      E,B                 
1444: 59              LD      E,C                 
1445: 5A              LD      E,D                 
1446: 5B              LD      E,E                 
1447: 58              LD      E,B                 
1448: 59              LD      E,C                 
1449: 5A              LD      E,D                 
144A: 5B              LD      E,E                 
144B: 58              LD      E,B                 
144C: 59              LD      E,C                 
144D: 5A              LD      E,D                 
144E: 5B              LD      E,E                 
144F: 54              LD      D,H                 
1450: 55              LD      D,L                 
1451: 56              LD      D,(HL)              
1452: 57              LD      D,A                 
1453: 5C              LD      E,H                 
1454: 5D              LD      E,L                 
1455: 5E              LD      E,(HL)              
1456: 5F              LD      E,A                 
1457: 58              LD      E,B                 
1458: 59              LD      E,C                 
1459: 5A              LD      E,D                 
145A: 5B              LD      E,E                 
145B: 54              LD      D,H                 
145C: 55              LD      D,L                 
145D: 56              LD      D,(HL)              
145E: 57              LD      D,A                 
145F: 34              INC     (HL)                
1460: 35              DEC     (HL)                
1461: 36 37           LD      (HL),$37            
1463: 34              INC     (HL)                
1464: 35              DEC     (HL)                
1465: 36 37           LD      (HL),$37            
1467: 34              INC     (HL)                
1468: 35              DEC     (HL)                
1469: 36 37           LD      (HL),$37            
146B: 34              INC     (HL)                
146C: 35              DEC     (HL)                
146D: 36 37           LD      (HL),$37            
146F: 34              INC     (HL)                
1470: 35              DEC     (HL)                
1471: 36 37           LD      (HL),$37            
1473: 38 39           JR      C,$14AE             ; {}
1475: 3A 3B 38        LD      A,($383B)           
1478: 39              ADD     HL,SP               
1479: 3A 3B 38        LD      A,($383B)           
147C: 39              ADD     HL,SP               
147D: 3A 3B 38        LD      A,($383B)           
1480: 39              ADD     HL,SP               
1481: 3A 3B 38        LD      A,($383B)           
1484: 39              ADD     HL,SP               
1485: 3A 3B 3C        LD      A,($3C3B)           
1488: 3D              DEC     A                   
1489: 3E 3F           LD      A,$3F               
148B: 3C              INC     A                   
148C: 3D              DEC     A                   
148D: 3E 3F           LD      A,$3F               
148F: 3C              INC     A                   
1490: 3D              DEC     A                   
1491: 3E 3F           LD      A,$3F               
1493: 3C              INC     A                   
1494: 3D              DEC     A                   
1495: 3E 3F           LD      A,$3F               
1497: 3C              INC     A                   
1498: 3D              DEC     A                   
1499: 3E 3F           LD      A,$3F               
149B: 47              LD      B,A                 
149C: 47              LD      B,A                 
149D: 47              LD      B,A                 
149E: 47              LD      B,A                 
149F: AC              XOR     H                   
14A0: AD              XOR     L                   
14A1: AE              XOR     (HL)                
14A2: AF              XOR     A                   
14A3: A8              XOR     B                   
14A4: A9              XOR     C                   
14A5: AA              XOR     D                   
14A6: AB              XOR     E                   
14A7: A0              AND     B                   
14A8: A1              AND     C                   
14A9: A2              AND     D                   
14AA: A3              AND     E                   
14AB: 30 31           JR      NC,$14DE            ; {}
14AD: 32 33 A4        LD      ($A433),A           
14B0: A5              AND     L                   
14B1: A6              AND     (HL)                
14B2: A7              AND     A                   
14B3: 50              LD      D,B                 
14B4: 51              LD      D,C                 
14B5: 52              LD      D,D                 
14B6: 53              LD      D,E                 
14B7: 3A FF 80        LD      A,($80FF)           
14BA: 01 C7 14        LD      BC,$14C7            
14BD: 26 00           LD      H,$00               
14BF: 87              ADD     A,A                 
14C0: 6F              LD      L,A                 
14C1: 09              ADD     HL,BC               
14C2: 4E              LD      C,(HL)              
14C3: 23              INC     HL                  
14C4: 66              LD      H,(HL)              
14C5: 69              LD      L,C                 
14C6: E9              JP      (HL)                
14C7: DD                                  
14C8: 14              INC     D                   
14C9: EE 14           XOR     $14                 
14CB: FF              RST     $38                 
14CC: 14              INC     D                   
14CD: 10 15           DJNZ    $14E4               ; {}
14CF: 21 15 32        LD      HL,$3215            
14D2: 15              DEC     D                   
14D3: 43              LD      B,E                 
14D4: 15              DEC     D                   
14D5: 54              LD      D,H                 
14D6: 15              DEC     D                   
14D7: 65              LD      H,L                 
14D8: 15              DEC     D                   
14D9: 76              HALT                        
14DA: 15              DEC     D                   
14DB: 87              ADD     A,A                 
14DC: 15              DEC     D                   
14DD: 21 9B 81        LD      HL,$819B            
14E0: 11 00 81        LD      DE,$8100            
14E3: DD 21 0C 80     LD      IX,$800C            
14E7: FD 21 A6 81     LD      IY,$81A6            
14EB: C3 98 15        JP      $1598               ; {}
14EE: 21 9C 81        LD      HL,$819C            
14F1: 11 09 81        LD      DE,$8109            
14F4: DD 21 10 80     LD      IX,$8010            
14F8: FD 21 A7 81     LD      IY,$81A7            
14FC: C3 3E 16        JP      $163E               ; {}
14FF: 21 9D 81        LD      HL,$819D            
1502: 11 12 81        LD      DE,$8112            
1505: DD 21 14 80     LD      IX,$8014            
1509: FD 21 A8 81     LD      IY,$81A8            
150D: C3 98 15        JP      $1598               ; {}
1510: 21 9E 81        LD      HL,$819E            
1513: 11 1B 81        LD      DE,$811B            
1516: DD 21 18 80     LD      IX,$8018            
151A: FD 21 A9 81     LD      IY,$81A9            
151E: C3 98 15        JP      $1598               ; {}
1521: 21 9F 81        LD      HL,$819F            
1524: 11 24 81        LD      DE,$8124            
1527: DD 21 1C 80     LD      IX,$801C            
152B: FD 21 AA 81     LD      IY,$81AA            
152F: C3 3E 16        JP      $163E               ; {}
1532: C3 DE 15        JP      $15DE               ; {}
1535: 11 2D 81        LD      DE,$812D            
1538: DD 21 20 80     LD      IX,$8020            
153C: FD 21 AB 81     LD      IY,$81AB            
1540: C3 98 15        JP      $1598               ; {}
1543: 21 A1 81        LD      HL,$81A1            
1546: 11 36 81        LD      DE,$8136            
1549: DD 21 24 80     LD      IX,$8024            
154D: FD 21 AC 81     LD      IY,$81AC            
1551: C3 3E 16        JP      $163E               ; {}
1554: 21 A2 81        LD      HL,$81A2            
1557: 11 3F 81        LD      DE,$813F            
155A: DD 21 28 80     LD      IX,$8028            
155E: FD 21 AD 81     LD      IY,$81AD            
1562: C3 98 15        JP      $1598               ; {}
1565: 21 A3 81        LD      HL,$81A3            
1568: 11 48 81        LD      DE,$8148            
156B: DD 21 2C 80     LD      IX,$802C            
156F: FD 21 AE 81     LD      IY,$81AE            
1573: C3 3E 16        JP      $163E               ; {}
1576: 21 A4 81        LD      HL,$81A4            
1579: 11 51 81        LD      DE,$8151            
157C: DD 21 30 80     LD      IX,$8030            
1580: FD 21 AF 81     LD      IY,$81AF            
1584: C3 98 15        JP      $1598               ; {}
1587: 21 A5 81        LD      HL,$81A5            
158A: 11 5A 81        LD      DE,$815A            
158D: DD 21 34 80     LD      IX,$8034            
1591: FD 21 B0 81     LD      IY,$81B0            
1595: C3 3E 16        JP      $163E               ; {}
1598: FD 7E 00        LD      A,(IY+$00)          
159B: 4F              LD      C,A                 
159C: A7              AND     A                   
159D: C2 D4 16        JP      NZ,$16D4            ; {}
15A0: 7E              LD      A,(HL)              
15A1: 47              LD      B,A                 
15A2: E6 0F           AND     $0F                 
15A4: 4F              LD      C,A                 
15A5: 78              LD      A,B                 
15A6: E6 10           AND     $10                 
15A8: C2 D4 16        JP      NZ,$16D4            ; {}
15AB: 1A              LD      A,(DE)              
15AC: 47              LD      B,A                 
15AD: 13              INC     DE                  
15AE: 1A              LD      A,(DE)              
15AF: 81              ADD     A,C                 
15B0: 12              LD      (DE),A              
15B1: 10 FA           DJNZ    $15AD               ; {}
15B3: DD 7E 00        LD      A,(IX+$00)          
15B6: 81              ADD     A,C                 
15B7: DD 77 00        LD      (IX+$00),A          
15BA: DD 77 02        LD      (IX+$02),A          
15BD: 3A 47 80        LD      A,($8047)           
15C0: FE 30           CP      $30                 
15C2: DA DA 15        JP      C,$15DA             ; {}
15C5: 3A 47 80        LD      A,($8047)           
15C8: FE 73           CP      $73                 
15CA: D2 DA 15        JP      NC,$15DA            ; {}
15CD: 47              LD      B,A                 
15CE: E6 0F           AND     $0F                 
15D0: FE 03           CP      $03                 
15D2: DA EB 15        JP      C,$15EB             ; {}
15D5: FE 0C           CP      $0C                 
15D7: D2 1F 16        JP      NC,$161F            ; {}
15DA: FD 36 00 00     LD      (IY+$00),$00        
15DE: 21 FF 80        LD      HL,$80FF            
15E1: 34              INC     (HL)                
15E2: 7E              LD      A,(HL)              
15E3: FE 0B           CP      $0B                 
15E5: DA B7 14        JP      C,$14B7             ; {}
15E8: 36 00           LD      (HL),$00            
15EA: C9              RET                         
15EB: 78              LD      A,B                 
15EC: E6 F0           AND     $F0                 
15EE: 08              EX      AF,AF'              
15EF: 08              EX      AF,AF'              
15F0: D6 30           SUB     $30                 
15F2: 0F              RRCA                        
15F3: 0F              RRCA                        
15F4: 0F              RRCA                        
15F5: 0F              RRCA                        
15F6: 47              LD      B,A                 
15F7: 3A FF 80        LD      A,($80FF)           
15FA: B8              CP      B                   
15FB: C2 DA 15        JP      NZ,$15DA            ; {}
15FE: 3A 47 80        LD      A,($8047)           
1601: FE 30           CP      $30                 
1603: DA DA 15        JP      C,$15DA             ; {}
1606: 3A 44 80        LD      A,($8044)           
1609: 81              ADD     A,C                 
160A: 32 44 80        LD      ($8044),A           
160D: FE 08           CP      $08                 
160F: DA 17 16        JP      C,$1617             ; {}
1612: FE E7           CP      $E7                 
1614: DA DA 15        JP      C,$15DA             ; {}
1617: 3E 01           LD      A,$01               
1619: 32 04 80        LD      ($8004),A           
161C: C3 DA 15        JP      $15DA               ; {}
161F: 78              LD      A,B                 
1620: E6 F0           AND     $F0                 
1622: C6 10           ADD     $10                 
1624: 08              EX      AF,AF'              
1625: 08              EX      AF,AF'              
1626: D6 30           SUB     $30                 
1628: 0F              RRCA                        
1629: 0F              RRCA                        
162A: 0F              RRCA                        
162B: 0F              RRCA                        
162C: 47              LD      B,A                 
162D: 3A FF 80        LD      A,($80FF)           
1630: B8              CP      B                   
1631: C2 DA 15        JP      NZ,$15DA            ; {}
1634: 3A 44 80        LD      A,($8044)           
1637: 81              ADD     A,C                 
1638: 32 44 80        LD      ($8044),A           
163B: C3 DA 15        JP      $15DA               ; {}
163E: FD 7E 00        LD      A,(IY+$00)          
1641: 4F              LD      C,A                 
1642: A7              AND     A                   
1643: C2 E6 16        JP      NZ,$16E6            ; {}
1646: 7E              LD      A,(HL)              
1647: 47              LD      B,A                 
1648: E6 0F           AND     $0F                 
164A: 4F              LD      C,A                 
164B: 78              LD      A,B                 
164C: E6 10           AND     $10                 
164E: C2 E6 16        JP      NZ,$16E6            ; {}
1651: 1A              LD      A,(DE)              
1652: 47              LD      B,A                 
1653: 13              INC     DE                  
1654: 1A              LD      A,(DE)              
1655: 91              SUB     C                   
1656: 12              LD      (DE),A              
1657: 10 FA           DJNZ    $1653               ; {}
1659: DD 7E 00        LD      A,(IX+$00)          
165C: 91              SUB     C                   
165D: DD 77 00        LD      (IX+$00),A          
1660: DD 77 02        LD      (IX+$02),A          
1663: 3A 47 80        LD      A,($8047)           
1666: FE 73           CP      $73                 
1668: D2 78 16        JP      NC,$1678            ; {}
166B: 47              LD      B,A                 
166C: E6 0F           AND     $0F                 
166E: FE 03           CP      $03                 
1670: DA 89 16        JP      C,$1689             ; {}
1673: FE 0C           CP      $0C                 
1675: D2 B5 16        JP      NC,$16B5            ; {}
1678: FD 36 00 00     LD      (IY+$00),$00        
167C: 21 FF 80        LD      HL,$80FF            
167F: 34              INC     (HL)                
1680: 7E              LD      A,(HL)              
1681: FE 0B           CP      $0B                 
1683: DA B7 14        JP      C,$14B7             ; {}
1686: 36 00           LD      (HL),$00            
1688: C9              RET                         
1689: 78              LD      A,B                 
168A: E6 F0           AND     $F0                 
168C: 08              EX      AF,AF'              
168D: 08              EX      AF,AF'              
168E: D6 30           SUB     $30                 
1690: 0F              RRCA                        
1691: 0F              RRCA                        
1692: 0F              RRCA                        
1693: 0F              RRCA                        
1694: 47              LD      B,A                 
1695: 3A FF 80        LD      A,($80FF)           
1698: B8              CP      B                   
1699: C2 78 16        JP      NZ,$1678            ; {}
169C: 3A 44 80        LD      A,($8044)           
169F: 91              SUB     C                   
16A0: 32 44 80        LD      ($8044),A           
16A3: FE 08           CP      $08                 
16A5: DA AD 16        JP      C,$16AD             ; {}
16A8: FE E7           CP      $E7                 
16AA: DA 78 16        JP      C,$1678             ; {}
16AD: 3E 01           LD      A,$01               
16AF: 32 04 80        LD      ($8004),A           
16B2: C3 78 16        JP      $1678               ; {}
16B5: 78              LD      A,B                 
16B6: E6 F0           AND     $F0                 
16B8: C6 10           ADD     $10                 
16BA: 08              EX      AF,AF'              
16BB: 08              EX      AF,AF'              
16BC: D6 30           SUB     $30                 
16BE: 0F              RRCA                        
16BF: 0F              RRCA                        
16C0: 0F              RRCA                        
16C1: 0F              RRCA                        
16C2: 47              LD      B,A                 
16C3: 3A FF 80        LD      A,($80FF)           
16C6: B8              CP      B                   
16C7: C2 78 16        JP      NZ,$1678            ; {}
16CA: 3A 44 80        LD      A,($8044)           
16CD: 91              SUB     C                   
16CE: 32 44 80        LD      ($8044),A           
16D1: C3 78 16        JP      $1678               ; {}
16D4: 79              LD      A,C                 
16D5: FE 01           CP      $01                 
16D7: C2 DF 16        JP      NZ,$16DF            ; {}
16DA: 0E 01           LD      C,$01               
16DC: C3 AB 15        JP      $15AB               ; {}
16DF: 0D              DEC     C                   
16E0: FD 71 00        LD      (IY+$00),C          
16E3: C3 DE 15        JP      $15DE               ; {}
16E6: 79              LD      A,C                 
16E7: FE 01           CP      $01                 
16E9: C2 F1 16        JP      NZ,$16F1            ; {}
16EC: 0E 01           LD      C,$01               
16EE: C3 51 16        JP      $1651               ; {}
16F1: 0D              DEC     C                   
16F2: FD 71 00        LD      (IY+$00),C          
16F5: C3 7C 16        JP      $167C               ; {}
16F8: 3A 04 80        LD      A,($8004)           
16FB: A7              AND     A                   
16FC: C8              RET     Z                   
16FD: 3A 50 81        LD      A,($8150)           
1700: CB 47           BIT     0,A                 
1702: 28 05           JR      Z,$1709             ; {}
1704: 3E 01           LD      A,$01               
1706: 32 18 81        LD      ($8118),A           
1709: 3A 20 81        LD      A,($8120)           
170C: A7              AND     A                   
170D: 28 03           JR      Z,$1712             ; {}
170F: 32 21 81        LD      ($8121),A           
1712: CD CE 25        CALL    $25CE               ; {}
1715: CD B3 27        CALL    $27B3               ; {}
1718: 3A 47 82        LD      A,($8247)           
171B: 3C              INC     A                   
171C: 32 47 82        LD      ($8247),A           
171F: D6 10           SUB     $10                 
1721: C0              RET     NZ                  
1722: 32 47 82        LD      ($8247),A           
1725: 3E 07           LD      A,$07               
1727: 32 46 80        LD      ($8046),A           
172A: 21 44 80        LD      HL,$8044            
172D: 3A B2 81        LD      A,($81B2)           
1730: 3C              INC     A                   
1731: 32 B2 81        LD      ($81B2),A           
1734: 4F              LD      C,A                 
1735: 3A 9C 82        LD      A,($829C)           
1738: A7              AND     A                   
1739: C2 7D 17        JP      NZ,$177D            ; {}
173C: 79              LD      A,C                 
173D: FE 06           CP      $06                 
173F: 20 44           JR      NZ,$1785            ; {}
1741: CD 04 08        CALL    $0804               ; {}
1744: AF              XOR     A                   
1745: 32 B2 81        LD      ($81B2),A           
1748: 32 04 80        LD      ($8004),A           
174B: 32 47 82        LD      ($8247),A           
174E: 32 69 82        LD      ($8269),A           
1751: 32 9C 82        LD      ($829C),A           
1754: 21 48 82        LD      HL,$8248            
1757: 11 49 82        LD      DE,$8249            
175A: 01 0B 00        LD      BC,$000B            
175D: 77              LD      (HL),A              
175E: ED B0           LDIR                        
1760: 3C              INC     A                   
1761: 32 CE 83        LD      ($83CE),A           
1764: 3A D6 83        LD      A,($83D6)           
1767: 3D              DEC     A                   
1768: 20 12           JR      NZ,$177C            ; {}
176A: 3A FE 83        LD      A,($83FE)           
176D: A7              AND     A                   
176E: 20 0C           JR      NZ,$177C            ; {}
1770: 32 D6 83        LD      ($83D6),A           
1773: 32 99 82        LD      ($8299),A           
1776: 32 9A 82        LD      ($829A),A           
1779: 32 5B 82        LD      ($825B),A           
177C: C9              RET                         
177D: 79              LD      A,C                 
177E: FE 05           CP      $05                 
1780: 20 03           JR      NZ,$1785            ; {}
1782: C3 41 17        JP      $1741               ; {}
1785: 3A 9C 82        LD      A,($829C)           
1788: A7              AND     A                   
1789: C2 C4 17        JP      NZ,$17C4            ; {}
178C: 23              INC     HL                  
178D: 3A B2 81        LD      A,($81B2)           
1790: 3D              DEC     A                   
1791: 28 0B           JR      Z,$179E             ; {}
1793: 3D              DEC     A                   
1794: 28 15           JR      Z,$17AB             ; {}
1796: 3D              DEC     A                   
1797: 28 15           JR      Z,$17AE             ; {}
1799: 3D              DEC     A                   
179A: 28 15           JR      Z,$17B1             ; {}
179C: 18 16           JR      $17B4               ; {}
179E: 36 39           LD      (HL),$39            
17A0: AF              XOR     A                   
17A1: 67              LD      H,A                 
17A2: 6F              LD      L,A                 
17A3: 22 82 83        LD      ($8382),HL          
17A6: DF              RST     $18                 
17A7: 3E 03           LD      A,$03               
17A9: DF              RST     $18                 
17AA: C9              RET                         
17AB: 36 39           LD      (HL),$39            
17AD: C9              RET                         
17AE: 36 3A           LD      (HL),$3A            
17B0: C9              RET                         
17B1: 36 3B           LD      (HL),$3B            
17B3: C9              RET                         
17B4: 36 3C           LD      (HL),$3C            
17B6: AF              XOR     A                   
17B7: 32 AE 83        LD      ($83AE),A           
17BA: CD 56 28        CALL    $2856               ; {}
17BD: 21 D8 00        LD      HL,$00D8            
17C0: 22 82 83        LD      ($8382),HL          
17C3: C9              RET                         
17C4: 23              INC     HL                  
17C5: 3A B2 81        LD      A,($81B2)           
17C8: 3D              DEC     A                   
17C9: 28 08           JR      Z,$17D3             ; {}
17CB: 3D              DEC     A                   
17CC: 28 12           JR      Z,$17E0             ; {}
17CE: 3D              DEC     A                   
17CF: 28 12           JR      Z,$17E3             ; {}
17D1: 18 13           JR      $17E6               ; {}
17D3: 36 22           LD      (HL),$22            
17D5: AF              XOR     A                   
17D6: 67              LD      H,A                 
17D7: 6F              LD      L,A                 
17D8: 22 82 83        LD      ($8382),HL          
17DB: DF              RST     $18                 
17DC: 3E 02           LD      A,$02               
17DE: DF              RST     $18                 
17DF: C9              RET                         
17E0: 36 23           LD      (HL),$23            
17E2: C9              RET                         
17E3: 36 24           LD      (HL),$24            
17E5: C9              RET                         
17E6: 36 3C           LD      (HL),$3C            
17E8: AF              XOR     A                   
17E9: 32 AE 83        LD      ($83AE),A           
17EC: 32 10 81        LD      ($8110),A           
17EF: 32 07 81        LD      ($8107),A           
17F2: 32 1A 81        LD      ($811A),A           
17F5: 32 19 81        LD      ($8119),A           
17F8: CD 56 28        CALL    $2856               ; {}
17FB: 21 D8 00        LD      HL,$00D8            
17FE: 22 82 83        LD      ($8382),HL          
1801: C9              RET                         
1802: 3A 4F 81        LD      A,($814F)           
1805: A7              AND     A                   
1806: C0              RET     NZ                  
1807: 3A 5B 81        LD      A,($815B)           
180A: A7              AND     A                   
180B: C0              RET     NZ                  
180C: 3A B4 81        LD      A,($81B4)           
180F: A7              AND     A                   
1810: C2 32 18        JP      NZ,$1832            ; {}
1813: 67              LD      H,A                 
1814: 3A B3 81        LD      A,($81B3)           
1817: 6F              LD      L,A                 
1818: 11 41 18        LD      DE,$1841            
181B: 29              ADD     HL,HL               
181C: 19              ADD     HL,DE               
181D: 4E              LD      C,(HL)              
181E: 23              INC     HL                  
181F: 66              LD      H,(HL)              
1820: 69              LD      L,C                 
1821: EB              EX      DE,HL               
1822: 21 B3 81        LD      HL,$81B3            
1825: 34              INC     (HL)                
1826: 7E              LD      A,(HL)              
1827: 23              INC     HL                  
1828: 36 15           LD      (HL),$15            
182A: D6 0A           SUB     $0A                 
182C: C2 37 18        JP      NZ,$1837            ; {}
182F: 2B              DEC     HL                  
1830: 77              LD      (HL),A              
1831: C9              RET                         
1832: 21 B4 81        LD      HL,$81B4            
1835: 35              DEC     (HL)                
1836: C9              RET                         
1837: EB              EX      DE,HL               
1838: 11 9B 81        LD      DE,$819B            
183B: 01 0B 00        LD      BC,$000B            
183E: ED B0           LDIR                        
1840: C9              RET                         
1841: 6B              LD      L,E                 
1842: 18 76           JR      $18BA               ; {}
1844: 18 81           JR      $17C7               ; {}
1846: 18 8C           JR      $17D4               ; {}
1848: 18 97           JR      $17E1               ; {}
184A: 18 A2           JR      $17EE               ; {}
184C: 18 AD           JR      $17FB               ; {}
184E: 18 B8           JR      $1808               ; {}
1850: 18 C3           JR      $1815               ; {}
1852: 18 CE           JR      $1822               ; {}
1854: 18 D9           JR      $182F               ; {}
1856: 18 E4           JR      $183C               ; {}
1858: 18 EF           JR      $1849               ; {}
185A: 18 FA           JR      $1856               ; {}
185C: 18 05           JR      $1863               ; {}
185E: 19              ADD     HL,DE               
185F: 10 19           DJNZ    $187A               ; {}
1861: 1B              DEC     DE                  
1862: 19              ADD     HL,DE               
1863: 26 19           LD      H,$19               
1865: 31 19 3C        LD      SP,$3C19            
1868: 19              ADD     HL,DE               
1869: 47              LD      B,A                 
186A: 19              ADD     HL,DE               
186B: 13              INC     DE                  
186C: 12              LD      (DE),A              
186D: 11 16 12        LD      DE,$1216            
1870: 00              NOP                         
1871: 12              LD      (DE),A              
1872: 13              INC     DE                  
1873: 14              INC     D                   
1874: 15              DEC     D                   
1875: 16 12           LD      D,$12               
1877: 13              INC     DE                  
1878: 12              LD      (DE),A              
1879: 15              DEC     D                   
187A: 01 00 13        LD      BC,$1300            
187D: 02              LD      (BC),A              
187E: 12              LD      (DE),A              
187F: 13              INC     DE                  
1880: 12              LD      (DE),A              
1881: 12              LD      (DE),A              
1882: 12              LD      (DE),A              
1883: 13              INC     DE                  
1884: 14              INC     D                   
1885: 12              LD      (DE),A              
1886: 00              NOP                         
1887: 12              LD      (DE),A              
1888: 01 13 12        LD      BC,$1213            
188B: 13              INC     DE                  
188C: 12              LD      (DE),A              
188D: 01 12 13        LD      BC,$1312            
1890: 13              INC     DE                  
1891: 00              NOP                         
1892: 12              LD      (DE),A              
1893: 02              LD      (BC),A              
1894: 12              LD      (DE),A              
1895: 01 14 13        LD      BC,$1314            
1898: 12              LD      (DE),A              
1899: 01 12 12        LD      BC,$1212            
189C: 00              NOP                         
189D: 12              LD      (DE),A              
189E: 01 01 12        LD      BC,$1201            
18A1: 13              INC     DE                  
18A2: 13              INC     DE                  
18A3: 01 12 13        LD      BC,$1312            
18A6: 13              INC     DE                  
18A7: 00              NOP                         
18A8: 01 02 12        LD      BC,$1202            
18AB: 13              INC     DE                  
18AC: 12              LD      (DE),A              
18AD: 12              LD      (DE),A              
18AE: 12              LD      (DE),A              
18AF: 13              INC     DE                  
18B0: 12              LD      (DE),A              
18B1: 12              LD      (DE),A              
18B2: 00              NOP                         
18B3: 12              LD      (DE),A              
18B4: 01 13 12        LD      BC,$1213            
18B7: 13              INC     DE                  
18B8: 13              INC     DE                  
18B9: 13              INC     DE                  
18BA: 12              LD      (DE),A              
18BB: 13              INC     DE                  
18BC: 01 00 13        LD      BC,$1300            
18BF: 02              LD      (BC),A              
18C0: 12              LD      (DE),A              
18C1: 01 12 12        LD      BC,$1212            
18C4: 12              LD      (DE),A              
18C5: 13              INC     DE                  
18C6: 12              LD      (DE),A              
18C7: 12              LD      (DE),A              
18C8: 00              NOP                         
18C9: 12              LD      (DE),A              
18CA: 01 01 12        LD      BC,$1201            
18CD: 13              INC     DE                  
18CE: 13              INC     DE                  
18CF: 01 12 01        LD      BC,$0112            
18D2: 13              INC     DE                  
18D3: 00              NOP                         
18D4: 01 02 12        LD      BC,$1202            
18D7: 13              INC     DE                  
18D8: 13              INC     DE                  
18D9: 12              LD      (DE),A              
18DA: 12              LD      (DE),A              
18DB: 01 12 12        LD      BC,$1212            
18DE: 00              NOP                         
18DF: 01 01 13        LD      BC,$1301            
18E2: 12              LD      (DE),A              
18E3: 12              LD      (DE),A              
18E4: 01 13 01        LD      BC,$0113            
18E7: 13              INC     DE                  
18E8: 01 00 12        LD      BC,$1200            
18EB: 01 12 01        LD      BC,$0112            
18EE: 01 12 12        LD      BC,$1212            
18F1: 01 12 12        LD      BC,$1212            
18F4: 00              NOP                         
18F5: 01 02 13        LD      BC,$1302            
18F8: 12              LD      (DE),A              
18F9: 01 01 12        LD      BC,$1201            
18FC: 01 12 01        LD      BC,$0112            
18FF: 00              NOP                         
1900: 01 03 12        LD      BC,$1203            
1903: 01 12 12        LD      BC,$1212            
1906: 12              LD      (DE),A              
1907: 01 12 12        LD      BC,$1212            
190A: 00              NOP                         
190B: 01 02 13        LD      BC,$1302            
190E: 12              LD      (DE),A              
190F: 12              LD      (DE),A              
1910: 01 01 12        LD      BC,$1201            
1913: 01 12 00        LD      BC,$0012            
1916: 01 01 12        LD      BC,$1201            
1919: 01 01 01        LD      BC,$0101            
191C: 01 12 01        LD      BC,$0112            
191F: 12              LD      (DE),A              
1920: 00              NOP                         
1921: 01 01 12        LD      BC,$1201            
1924: 01 01 12        LD      BC,$1201            
1927: 01 13 12        LD      BC,$1213            
192A: 01 00 12        LD      BC,$1200            
192D: 02              LD      (BC),A              
192E: 01 12 12        LD      BC,$1212            
1931: 01 12 14        LD      BC,$1412            
1934: 01 12 00        LD      BC,$0012            
1937: 01 03 12        LD      BC,$1203            
193A: 13              INC     DE                  
193B: 01 12 01        LD      BC,$0112            
193E: 13              INC     DE                  
193F: 12              LD      (DE),A              
1940: 13              INC     DE                  
1941: 00              NOP                         
1942: 12              LD      (DE),A              
1943: 02              LD      (BC),A              
1944: 13              INC     DE                  
1945: 12              LD      (DE),A              
1946: 12              LD      (DE),A              
1947: 13              INC     DE                  
1948: 12              LD      (DE),A              
1949: 12              LD      (DE),A              
194A: 13              INC     DE                  
194B: 12              LD      (DE),A              
194C: 00              NOP                         
194D: 13              INC     DE                  
194E: 01 14 13        LD      BC,$1314            
1951: 14              INC     D                   
1952: 21 43 A8        LD      HL,$A843            
1955: 0E 05           LD      C,$05               
1957: 11 F6 19        LD      DE,$19F6            
195A: 06 04           LD      B,$04               
195C: 1A              LD      A,(DE)              
195D: 77              LD      (HL),A              
195E: 13              INC     DE                  
195F: C5              PUSH    BC                  
1960: 01 20 00        LD      BC,$0020            
1963: 09              ADD     HL,BC               
1964: C1              POP     BC                  
1965: 10 F5           DJNZ    $195C               ; {}
1967: 11 40 00        LD      DE,$0040            
196A: 19              ADD     HL,DE               
196B: 0D              DEC     C                   
196C: C2 57 19        JP      NZ,$1957            ; {}
196F: 21 A4 A8        LD      HL,$A8A4            
1972: 0E 04           LD      C,$04               
1974: 11 FA 19        LD      DE,$19FA            
1977: 06 04           LD      B,$04               
1979: 1A              LD      A,(DE)              
197A: 77              LD      (HL),A              
197B: 13              INC     DE                  
197C: C5              PUSH    BC                  
197D: 01 20 00        LD      BC,$0020            
1980: 09              ADD     HL,BC               
1981: C1              POP     BC                  
1982: 10 F5           DJNZ    $1979               ; {}
1984: 11 40 00        LD      DE,$0040            
1987: 19              ADD     HL,DE               
1988: 0D              DEC     C                   
1989: C2 74 19        JP      NZ,$1974            ; {}
198C: 21 A5 A8        LD      HL,$A8A5            
198F: 0E 04           LD      C,$04               
1991: 11 FE 19        LD      DE,$19FE            
1994: 06 04           LD      B,$04               
1996: 1A              LD      A,(DE)              
1997: 77              LD      (HL),A              
1998: 13              INC     DE                  
1999: C5              PUSH    BC                  
199A: 01 20 00        LD      BC,$0020            
199D: 09              ADD     HL,BC               
199E: C1              POP     BC                  
199F: 10 F5           DJNZ    $1996               ; {}
19A1: 11 40 00        LD      DE,$0040            
19A4: 19              ADD     HL,DE               
19A5: 0D              DEC     C                   
19A6: C2 91 19        JP      NZ,$1991            ; {}
19A9: 21 C3 A8        LD      HL,$A8C3            
19AC: 06 04           LD      B,$04               
19AE: 36 47           LD      (HL),$47            
19B0: 11 20 00        LD      DE,$0020            
19B3: 19              ADD     HL,DE               
19B4: 36 47           LD      (HL),$47            
19B6: 11 A0 00        LD      DE,$00A0            
19B9: 19              ADD     HL,DE               
19BA: 10 F2           DJNZ    $19AE               ; {}
19BC: 21 44 A8        LD      HL,$A844            
19BF: 36 41           LD      (HL),$41            
19C1: 23              INC     HL                  
19C2: 36 42           LD      (HL),$42            
19C4: 01 5F 03        LD      BC,$035F            
19C7: 09              ADD     HL,BC               
19C8: 36 45           LD      (HL),$45            
19CA: 23              INC     HL                  
19CB: 36 46           LD      (HL),$46            
19CD: 21 5C A8        LD      HL,$A85C            
19D0: CD E2 19        CALL    $19E2               ; {}
19D3: 21 07 80        LD      HL,$8007            
19D6: 3E 01           LD      A,$01               
19D8: 77              LD      (HL),A              
19D9: 2C              INC     L                   
19DA: 2C              INC     L                   
19DB: 77              LD      (HL),A              
19DC: 2C              INC     L                   
19DD: 2C              INC     L                   
19DE: 77              LD      (HL),A              
19DF: C3 02 1A        JP      $1A02               ; {}
19E2: 06 0E           LD      B,$0E               
19E4: 36 48           LD      (HL),$48            
19E6: 23              INC     HL                  
19E7: 36 49           LD      (HL),$49            
19E9: 11 1F 00        LD      DE,$001F            
19EC: 19              ADD     HL,DE               
19ED: 36 4A           LD      (HL),$4A            
19EF: 23              INC     HL                  
19F0: 36 4B           LD      (HL),$4B            
19F2: 19              ADD     HL,DE               
19F3: 10 EF           DJNZ    $19E4               ; {}
19F5: C9              RET                         
19F6: 40              LD      B,B                 
19F7: 43              LD      B,E                 
19F8: 43              LD      B,E                 
19F9: 44              LD      B,H                 
19FA: 45              LD      B,L                 
19FB: 47              LD      B,A                 
19FC: 47              LD      B,A                 
19FD: 41              LD      B,C                 
19FE: 46              LD      B,(HL)              
19FF: 43              LD      B,E                 
1A00: 43              LD      B,E                 
1A01: 42              LD      B,D                 
1A02: 3E 05           LD      A,$05               
1A04: 32 25 80        LD      ($8025),A           
1A07: 32 27 80        LD      ($8027),A           
1A0A: 3E 04           LD      A,$04               
1A0C: 32 2D 80        LD      ($802D),A           
1A0F: 32 2F 80        LD      ($802F),A           
1A12: 3E 07           LD      A,$07               
1A14: 32 35 80        LD      ($8035),A           
1A17: 32 37 80        LD      ($8037),A           
1A1A: 3E 06           LD      A,$06               
1A1C: 32 21 80        LD      ($8021),A           
1A1F: 32 23 80        LD      ($8023),A           
1A22: 32 39 80        LD      ($8039),A           
1A25: 32 3B 80        LD      ($803B),A           
1A28: 3E 05           LD      A,$05               
1A2A: 06 0A           LD      B,$0A               
1A2C: 21 0D 80        LD      HL,$800D            
1A2F: 77              LD      (HL),A              
1A30: 23              INC     HL                  
1A31: 23              INC     HL                  
1A32: 10 FB           DJNZ    $1A2F               ; {}
1A34: 32 29 80        LD      ($8029),A           
1A37: 32 2B 80        LD      ($802B),A           
1A3A: 32 31 80        LD      ($8031),A           
1A3D: 32 33 80        LD      ($8033),A           
1A40: 3E 02           LD      A,$02               
1A42: 32 0D 80        LD      ($800D),A           
1A45: 32 0F 80        LD      ($800F),A           
1A48: 32 15 80        LD      ($8015),A           
1A4B: 32 17 80        LD      ($8017),A           
1A4E: 32 19 80        LD      ($8019),A           
1A51: 32 1B 80        LD      ($801B),A           
1A54: C9              RET                         
1A55: 3A FE 83        LD      A,($83FE)           
1A58: B7              OR      A                   
1A59: 28 34           JR      Z,$1A8F             ; {}
1A5B: CD BB 28        CALL    $28BB               ; {}
1A5E: CD 1D 29        CALL    $291D               ; {}
1A61: CD EA 27        CALL    $27EA               ; {}
1A64: CD A6 26        CALL    $26A6               ; {}
1A67: CD 06 29        CALL    $2906               ; {}
1A6A: 3A 40 83        LD      A,($8340)           
1A6D: A7              AND     A                   
1A6E: C4 9F 1A        CALL    NZ,$1A9F            ; {}
1A71: CD EB 23        CALL    $23EB               ; {}
1A74: 3A B7 83        LD      A,($83B7)           
1A77: CB 47           BIT     0,A                 
1A79: CA AD 1A        JP      Z,$1AAD             ; {}
1A7C: 3A 22 81        LD      A,($8122)           
1A7F: 3C              INC     A                   
1A80: 32 22 81        LD      ($8122),A           
1A83: A7              AND     A                   
1A84: CC FA 23        CALL    Z,$23FA             ; {}
1A87: 3A 22 81        LD      A,($8122)           
1A8A: FE 70           CP      $70                 
1A8C: CC CE 25        CALL    Z,$25CE             ; {}
1A8F: 3A 47 80        LD      A,($8047)           
1A92: FE 31           CP      $31                 
1A94: DA FF 1C        JP      C,$1CFF             ; {}
1A97: 3A FE 83        LD      A,($83FE)           
1A9A: B7              OR      A                   
1A9B: C8              RET     Z                   
1A9C: C3 CB 1A        JP      $1ACB               ; {}
1A9F: 3D              DEC     A                   
1AA0: 32 40 83        LD      ($8340),A           
1AA3: FE 01           CP      $01                 
1AA5: C0              RET     NZ                  
1AA6: CD 9A 26        CALL    $269A               ; {}
1AA9: CD DE 27        CALL    $27DE               ; {}
1AAC: C9              RET                         
1AAD: 3A 22 81        LD      A,($8122)           
1AB0: 3C              INC     A                   
1AB1: 32 22 81        LD      ($8122),A           
1AB4: A7              AND     A                   
1AB5: CC 96 24        CALL    Z,$2496             ; {}
1AB8: 3A 22 81        LD      A,($8122)           
1ABB: FE 50           CP      $50                 
1ABD: CC 32 25        CALL    Z,$2532             ; {}
1AC0: 3A 22 81        LD      A,($8122)           
1AC3: FE B0           CP      $B0                 
1AC5: CC CE 25        CALL    Z,$25CE             ; {}
1AC8: C3 8F 1A        JP      $1A8F               ; {}
1ACB: 3A 6C 82        LD      A,($826C)           
1ACE: A7              AND     A                   
1ACF: C0              RET     NZ                  
1AD0: 3A 68 82        LD      A,($8268)           
1AD3: A7              AND     A                   
1AD4: 28 08           JR      Z,$1ADE             ; {}
1AD6: 3D              DEC     A                   
1AD7: 32 68 82        LD      ($8268),A           
1ADA: CD EB 23        CALL    $23EB               ; {}
1ADD: C9              RET                         
1ADE: 3A 04 80        LD      A,($8004)           
1AE1: A7              AND     A                   
1AE2: C0              RET     NZ                  
1AE3: 21 44 80        LD      HL,$8044            
1AE6: 11 47 80        LD      DE,$8047            
1AE9: 3A 04 E0        LD      A,($E004)           ; {hard.PPI8255+2004}
1AEC: CB 5F           BIT     3,A                 
1AEE: 28 07           JR      Z,$1AF7             ; {}
1AF0: 3A FD 83        LD      A,($83FD)           
1AF3: 3D              DEC     A                   
1AF4: C2 74 1B        JP      NZ,$1B74            ; {}
1AF7: 3A 00 E0        LD      A,($E000)           ; {hard.PPI8255+2000}
1AFA: 4F              LD      C,A                 
1AFB: 3A 48 82        LD      A,($8248)           
1AFE: A7              AND     A                   
1AFF: C2 BA 1B        JP      NZ,$1BBA            ; {}
1B02: 3A 04 E0        LD      A,($E004)           ; {hard.PPI8255+2004}
1B05: CB 5F           BIT     3,A                 
1B07: 28 07           JR      Z,$1B10             ; {}
1B09: 3A FD 83        LD      A,($83FD)           
1B0C: 3D              DEC     A                   
1B0D: C2 7B 1B        JP      NZ,$1B7B            ; {}
1B10: 3A 04 E0        LD      A,($E004)           ; {hard.PPI8255+2004}
1B13: CB 77           BIT     6,A                 
1B15: CA 8B 1B        JP      Z,$1B8B             ; {}
1B18: AF              XOR     A                   
1B19: 32 4C 82        LD      ($824C),A           
1B1C: 32 50 82        LD      ($8250),A           
1B1F: 3A 49 82        LD      A,($8249)           
1B22: A7              AND     A                   
1B23: C2 0D 1C        JP      NZ,$1C0D            ; {}
1B26: 3A 4A 82        LD      A,($824A)           
1B29: 47              LD      B,A                 
1B2A: 3A 4B 82        LD      A,($824B)           
1B2D: 80              ADD     A,B                 
1B2E: 20 1D           JR      NZ,$1B4D            ; {}
1B30: 3A 04 E0        LD      A,($E004)           ; {hard.PPI8255+2004}
1B33: CB 5F           BIT     3,A                 
1B35: 28 07           JR      Z,$1B3E             ; {}
1B37: 3A FD 83        LD      A,($83FD)           
1B3A: 3D              DEC     A                   
1B3B: C2 83 1B        JP      NZ,$1B83            ; {}
1B3E: 3A 04 E0        LD      A,($E004)           ; {hard.PPI8255+2004}
1B41: CB 67           BIT     4,A                 
1B43: CA E4 1B        JP      Z,$1BE4             ; {}
1B46: AF              XOR     A                   
1B47: 32 4D 82        LD      ($824D),A           
1B4A: 32 51 82        LD      ($8251),A           
1B4D: 3A 4A 82        LD      A,($824A)           
1B50: A7              AND     A                   
1B51: C2 76 1C        JP      NZ,$1C76            ; {}
1B54: CB 61           BIT     4,C                 
1B56: CA 41 1C        JP      Z,$1C41             ; {}
1B59: AF              XOR     A                   
1B5A: 32 4E 82        LD      ($824E),A           
1B5D: 32 52 82        LD      ($8252),A           
1B60: 3A 4B 82        LD      A,($824B)           
1B63: A7              AND     A                   
1B64: C2 D5 1C        JP      NZ,$1CD5            ; {}
1B67: CB 69           BIT     5,C                 
1B69: CA A0 1C        JP      Z,$1CA0             ; {}
1B6C: AF              XOR     A                   
1B6D: 32 4F 82        LD      ($824F),A           
1B70: 32 53 82        LD      ($8253),A           
1B73: C9              RET                         
1B74: 3A 02 E0        LD      A,($E002)           ; {hard.PPI8255+2002}
1B77: 4F              LD      C,A                 
1B78: C3 FB 1A        JP      $1AFB               ; {}
1B7B: 3A 04 E0        LD      A,($E004)           ; {hard.PPI8255+2004}
1B7E: CB 47           BIT     0,A                 
1B80: C3 15 1B        JP      $1B15               ; {}
1B83: 3A 00 E0        LD      A,($E000)           ; {hard.PPI8255+2000}
1B86: CB 47           BIT     0,A                 
1B88: C3 43 1B        JP      $1B43               ; {}
1B8B: 3A 47 80        LD      A,($8047)           
1B8E: FE F0           CP      $F0                 
1B90: D0              RET     NC                  
1B91: 3A 50 82        LD      A,($8250)           
1B94: A7              AND     A                   
1B95: 20 10           JR      NZ,$1BA7            ; {}
1B97: 3E 04           LD      A,$04               
1B99: DF              RST     $18                 
1B9A: 23              INC     HL                  
1B9B: 7E              LD      A,(HL)              
1B9C: 2B              DEC     HL                  
1B9D: FE DE           CP      $DE                 
1B9F: CA B4 1B        JP      Z,$1BB4             ; {}
1BA2: 3E DE           LD      A,$DE               
1BA4: 32 45 80        LD      ($8045),A           
1BA7: 3A 50 82        LD      A,($8250)           
1BAA: 3C              INC     A                   
1BAB: 32 50 82        LD      ($8250),A           
1BAE: B7              OR      A                   
1BAF: C8              RET     Z                   
1BB0: AF              XOR     A                   
1BB1: 32 50 82        LD      ($8250),A           
1BB4: 3A 56 82        LD      A,($8256)           
1BB7: 32 50 82        LD      ($8250),A           
1BBA: 3A 4C 82        LD      A,($824C)           
1BBD: A7              AND     A                   
1BBE: C0              RET     NZ                  
1BBF: 3C              INC     A                   
1BC0: 32 48 82        LD      ($8248),A           
1BC3: 3A 50 82        LD      A,($8250)           
1BC6: 3D              DEC     A                   
1BC7: 32 50 82        LD      ($8250),A           
1BCA: C2 D8 1B        JP      NZ,$1BD8            ; {}
1BCD: 32 48 82        LD      ($8248),A           
1BD0: 3C              INC     A                   
1BD1: 32 4C 82        LD      ($824C),A           
1BD4: 23              INC     HL                  
1BD5: 36 DE           LD      (HL),$DE            
1BD7: C9              RET                         
1BD8: EB              EX      DE,HL               
1BD9: 3A 54 82        LD      A,($8254)           
1BDC: 86              ADD     A,(HL)              
1BDD: 77              LD      (HL),A              
1BDE: EB              EX      DE,HL               
1BDF: 23              INC     HL                  
1BE0: 3E DC           LD      A,$DC               
1BE2: 77              LD      (HL),A              
1BE3: C9              RET                         
1BE4: 3A 51 82        LD      A,($8251)           
1BE7: A7              AND     A                   
1BE8: 20 10           JR      NZ,$1BFA            ; {}
1BEA: 3E 04           LD      A,$04               
1BEC: DF              RST     $18                 
1BED: 23              INC     HL                  
1BEE: 7E              LD      A,(HL)              
1BEF: 2B              DEC     HL                  
1BF0: FE 1E           CP      $1E                 
1BF2: CA 07 1C        JP      Z,$1C07             ; {}
1BF5: 3E 1E           LD      A,$1E               
1BF7: 32 45 80        LD      ($8045),A           
1BFA: 3A 51 82        LD      A,($8251)           
1BFD: 3C              INC     A                   
1BFE: 32 51 82        LD      ($8251),A           
1C01: B7              OR      A                   
1C02: C8              RET     Z                   
1C03: AF              XOR     A                   
1C04: 32 51 82        LD      ($8251),A           
1C07: 3A 57 82        LD      A,($8257)           
1C0A: 32 51 82        LD      ($8251),A           
1C0D: CD EB 23        CALL    $23EB               ; {}
1C10: 3A 4D 82        LD      A,($824D)           
1C13: A7              AND     A                   
1C14: C0              RET     NZ                  
1C15: 3C              INC     A                   
1C16: 32 49 82        LD      ($8249),A           
1C19: 3A 51 82        LD      A,($8251)           
1C1C: 3D              DEC     A                   
1C1D: 32 51 82        LD      ($8251),A           
1C20: C2 33 1C        JP      NZ,$1C33            ; {}
1C23: 32 49 82        LD      ($8249),A           
1C26: 3C              INC     A                   
1C27: 32 4D 82        LD      ($824D),A           
1C2A: 23              INC     HL                  
1C2B: 36 1E           LD      (HL),$1E            
1C2D: D5              PUSH    DE                  
1C2E: CD D6 1F        CALL    $1FD6               ; {}
1C31: D1              POP     DE                  
1C32: C9              RET                         
1C33: EB              EX      DE,HL               
1C34: 3A 54 82        LD      A,($8254)           
1C37: 47              LD      B,A                 
1C38: 7E              LD      A,(HL)              
1C39: 90              SUB     B                   
1C3A: 77              LD      (HL),A              
1C3B: EB              EX      DE,HL               
1C3C: 23              INC     HL                  
1C3D: 3E 1C           LD      A,$1C               
1C3F: 77              LD      (HL),A              
1C40: C9              RET                         
1C41: 3A 47 80        LD      A,($8047)           
1C44: FE 30           CP      $30                 
1C46: D8              RET     C                   
1C47: 3A 44 80        LD      A,($8044)           
1C4A: FE E0           CP      $E0                 
1C4C: D0              RET     NC                  
1C4D: 3A 52 82        LD      A,($8252)           
1C50: A7              AND     A                   
1C51: 20 10           JR      NZ,$1C63            ; {}
1C53: 3E 04           LD      A,$04               
1C55: DF              RST     $18                 
1C56: 23              INC     HL                  
1C57: 7E              LD      A,(HL)              
1C58: 2B              DEC     HL                  
1C59: FE A1           CP      $A1                 
1C5B: CA 70 1C        JP      Z,$1C70             ; {}
1C5E: 3E A1           LD      A,$A1               
1C60: 32 45 80        LD      ($8045),A           
1C63: 3A 52 82        LD      A,($8252)           
1C66: 3C              INC     A                   
1C67: 32 52 82        LD      ($8252),A           
1C6A: B7              OR      A                   
1C6B: C8              RET     Z                   
1C6C: AF              XOR     A                   
1C6D: 32 52 82        LD      ($8252),A           
1C70: 3A 58 82        LD      A,($8258)           
1C73: 32 52 82        LD      ($8252),A           
1C76: 3A 4E 82        LD      A,($824E)           
1C79: A7              AND     A                   
1C7A: C0              RET     NZ                  
1C7B: 3C              INC     A                   
1C7C: 32 4A 82        LD      ($824A),A           
1C7F: 3A 52 82        LD      A,($8252)           
1C82: 3D              DEC     A                   
1C83: 32 52 82        LD      ($8252),A           
1C86: C2 94 1C        JP      NZ,$1C94            ; {}
1C89: 32 4A 82        LD      ($824A),A           
1C8C: 3C              INC     A                   
1C8D: 32 4E 82        LD      ($824E),A           
1C90: 23              INC     HL                  
1C91: 36 A1           LD      (HL),$A1            
1C93: C9              RET                         
1C94: 3A 55 82        LD      A,($8255)           
1C97: 47              LD      B,A                 
1C98: 7E              LD      A,(HL)              
1C99: 80              ADD     A,B                 
1C9A: 77              LD      (HL),A              
1C9B: 23              INC     HL                  
1C9C: 3E 9F           LD      A,$9F               
1C9E: 77              LD      (HL),A              
1C9F: C9              RET                         
1CA0: 3A 47 80        LD      A,($8047)           
1CA3: FE 30           CP      $30                 
1CA5: D8              RET     C                   
1CA6: 3A 44 80        LD      A,($8044)           
1CA9: FE 20           CP      $20                 
1CAB: D8              RET     C                   
1CAC: 3A 53 82        LD      A,($8253)           
1CAF: A7              AND     A                   
1CB0: 20 10           JR      NZ,$1CC2            ; {}
1CB2: 3E 04           LD      A,$04               
1CB4: DF              RST     $18                 
1CB5: 23              INC     HL                  
1CB6: 7E              LD      A,(HL)              
1CB7: 2B              DEC     HL                  
1CB8: FE 21           CP      $21                 
1CBA: CA CF 1C        JP      Z,$1CCF             ; {}
1CBD: 3E 21           LD      A,$21               
1CBF: 32 45 80        LD      ($8045),A           
1CC2: 3A 53 82        LD      A,($8253)           
1CC5: 3C              INC     A                   
1CC6: 32 53 82        LD      ($8253),A           
1CC9: B7              OR      A                   
1CCA: C8              RET     Z                   
1CCB: AF              XOR     A                   
1CCC: 32 53 82        LD      ($8253),A           
1CCF: 3A 59 82        LD      A,($8259)           
1CD2: 32 53 82        LD      ($8253),A           
1CD5: 3A 4F 82        LD      A,($824F)           
1CD8: A7              AND     A                   
1CD9: C0              RET     NZ                  
1CDA: 3C              INC     A                   
1CDB: 32 4B 82        LD      ($824B),A           
1CDE: 3A 53 82        LD      A,($8253)           
1CE1: 3D              DEC     A                   
1CE2: 32 53 82        LD      ($8253),A           
1CE5: C2 F3 1C        JP      NZ,$1CF3            ; {}
1CE8: 32 4B 82        LD      ($824B),A           
1CEB: 3C              INC     A                   
1CEC: 32 4F 82        LD      ($824F),A           
1CEF: 23              INC     HL                  
1CF0: 36 21           LD      (HL),$21            
1CF2: C9              RET                         
1CF3: 3A 55 82        LD      A,($8255)           
1CF6: 47              LD      B,A                 
1CF7: 7E              LD      A,(HL)              
1CF8: 90              SUB     B                   
1CF9: 77              LD      (HL),A              
1CFA: 23              INC     HL                  
1CFB: 3E 1F           LD      A,$1F               
1CFD: 77              LD      (HL),A              
1CFE: C9              RET                         
1CFF: 3A 44 80        LD      A,($8044)           
1D02: FE 15           CP      $15                 
1D04: DA 77 1D        JP      C,$1D77             ; {}
1D07: FE 1C           CP      $1C                 
1D09: CA 87 1D        JP      Z,$1D87             ; {}
1D0C: DA 87 1D        JP      C,$1D87             ; {}
1D0F: FE 2E           CP      $2E                 
1D11: DA 77 1D        JP      C,$1D77             ; {}
1D14: FE 35           CP      $35                 
1D16: CA 77 1D        JP      Z,$1D77             ; {}
1D19: DA 77 1D        JP      C,$1D77             ; {}
1D1C: FE 45           CP      $45                 
1D1E: DA 77 1D        JP      C,$1D77             ; {}
1D21: FE 4C           CP      $4C                 
1D23: CA D8 1D        JP      Z,$1DD8             ; {}
1D26: DA D8 1D        JP      C,$1DD8             ; {}
1D29: FE 5E           CP      $5E                 
1D2B: DA 77 1D        JP      C,$1D77             ; {}
1D2E: FE 65           CP      $65                 
1D30: CA 77 1D        JP      Z,$1D77             ; {}
1D33: DA 77 1D        JP      C,$1D77             ; {}
1D36: FE 75           CP      $75                 
1D38: DA 77 1D        JP      C,$1D77             ; {}
1D3B: FE 7C           CP      $7C                 
1D3D: CA 29 1E        JP      Z,$1E29             ; {}
1D40: DA 29 1E        JP      C,$1E29             ; {}
1D43: FE 8E           CP      $8E                 
1D45: DA 77 1D        JP      C,$1D77             ; {}
1D48: FE 95           CP      $95                 
1D4A: CA 77 1D        JP      Z,$1D77             ; {}
1D4D: DA 77 1D        JP      C,$1D77             ; {}
1D50: FE A5           CP      $A5                 
1D52: DA 77 1D        JP      C,$1D77             ; {}
1D55: FE AC           CP      $AC                 
1D57: CA 7A 1E        JP      Z,$1E7A             ; {}
1D5A: DA 7A 1E        JP      C,$1E7A             ; {}
1D5D: FE BE           CP      $BE                 
1D5F: DA 77 1D        JP      C,$1D77             ; {}
1D62: FE C5           CP      $C5                 
1D64: CA 77 1D        JP      Z,$1D77             ; {}
1D67: DA 77 1D        JP      C,$1D77             ; {}
1D6A: FE D5           CP      $D5                 
1D6C: DA 77 1D        JP      C,$1D77             ; {}
1D6F: FE DC           CP      $DC                 
1D71: CA CB 1E        JP      Z,$1ECB             ; {}
1D74: DA CB 1E        JP      C,$1ECB             ; {}
1D77: 3A 47 80        LD      A,($8047)           
1D7A: FE 2A           CP      $2A                 
1D7C: D2 CB 1A        JP      NC,$1ACB            ; {}
1D7F: 3E 01           LD      A,$01               
1D81: 32 04 80        LD      ($8004),A           
1D84: C3 CB 1A        JP      $1ACB               ; {}
1D87: 3A FD 83        LD      A,($83FD)           
1D8A: 3D              DEC     A                   
1D8B: 20 3C           JR      NZ,$1DC9            ; {}
1D8D: 3A 5E 82        LD      A,($825E)           
1D90: A7              AND     A                   
1D91: C0              RET     NZ                  
1D92: 3A 47 80        LD      A,($8047)           
1D95: FE 2A           CP      $2A                 
1D97: D2 CB 1A        JP      NC,$1ACB            ; {}
1D9A: 06 18           LD      B,$18               
1D9C: 3A 21 81        LD      A,($8121)           
1D9F: D6 01           SUB     $01                 
1DA1: CC 73 26        CALL    Z,$2673             ; {}
1DA4: 21 64 AB        LD      HL,$AB64            
1DA7: CD 1C 1F        CALL    $1F1C               ; {}
1DAA: 3A 34 81        LD      A,($8134)           
1DAD: A7              AND     A                   
1DAE: 28 09           JR      Z,$1DB9             ; {}
1DB0: 06 18           LD      B,$18               
1DB2: CD CB 27        CALL    $27CB               ; {}
1DB5: AF              XOR     A                   
1DB6: 32 34 81        LD      ($8134),A           
1DB9: 3A FD 83        LD      A,($83FD)           
1DBC: 3D              DEC     A                   
1DBD: 20 0F           JR      NZ,$1DCE            ; {}
1DBF: 3E 01           LD      A,$01               
1DC1: 32 5E 82        LD      ($825E),A           
1DC4: 21 5C 82        LD      HL,$825C            
1DC7: 34              INC     (HL)                
1DC8: C9              RET                         
1DC9: 3A 63 82        LD      A,($8263)           
1DCC: 18 C2           JR      $1D90               ; {}
1DCE: 3E 01           LD      A,$01               
1DD0: 32 63 82        LD      ($8263),A           
1DD3: 21 5D 82        LD      HL,$825D            
1DD6: 34              INC     (HL)                
1DD7: C9              RET                         
1DD8: 3A FD 83        LD      A,($83FD)           
1DDB: 3D              DEC     A                   
1DDC: 20 3C           JR      NZ,$1E1A            ; {}
1DDE: 3A 5F 82        LD      A,($825F)           
1DE1: A7              AND     A                   
1DE2: C0              RET     NZ                  
1DE3: 3A 47 80        LD      A,($8047)           
1DE6: FE 2A           CP      $2A                 
1DE8: D2 CB 1A        JP      NC,$1ACB            ; {}
1DEB: 06 48           LD      B,$48               
1DED: 3A 21 81        LD      A,($8121)           
1DF0: D6 02           SUB     $02                 
1DF2: CC 73 26        CALL    Z,$2673             ; {}
1DF5: 21 A4 AA        LD      HL,$AAA4            
1DF8: CD 1C 1F        CALL    $1F1C               ; {}
1DFB: 3A 34 81        LD      A,($8134)           
1DFE: A7              AND     A                   
1DFF: 28 09           JR      Z,$1E0A             ; {}
1E01: 06 48           LD      B,$48               
1E03: CD CB 27        CALL    $27CB               ; {}
1E06: AF              XOR     A                   
1E07: 32 34 81        LD      ($8134),A           
1E0A: 3A FD 83        LD      A,($83FD)           
1E0D: 3D              DEC     A                   
1E0E: 20 0F           JR      NZ,$1E1F            ; {}
1E10: 3E 01           LD      A,$01               
1E12: 32 5F 82        LD      ($825F),A           
1E15: 21 5C 82        LD      HL,$825C            
1E18: 34              INC     (HL)                
1E19: C9              RET                         
1E1A: 3A 64 82        LD      A,($8264)           
1E1D: 18 C2           JR      $1DE1               ; {}
1E1F: 3E 01           LD      A,$01               
1E21: 32 64 82        LD      ($8264),A           
1E24: 21 5D 82        LD      HL,$825D            
1E27: 34              INC     (HL)                
1E28: C9              RET                         
1E29: 3A FD 83        LD      A,($83FD)           
1E2C: 3D              DEC     A                   
1E2D: 20 3C           JR      NZ,$1E6B            ; {}
1E2F: 3A 60 82        LD      A,($8260)           
1E32: A7              AND     A                   
1E33: C0              RET     NZ                  
1E34: 3A 47 80        LD      A,($8047)           
1E37: FE 2A           CP      $2A                 
1E39: D2 CB 1A        JP      NC,$1ACB            ; {}
1E3C: 06 78           LD      B,$78               
1E3E: 3A 21 81        LD      A,($8121)           
1E41: D6 03           SUB     $03                 
1E43: CC 73 26        CALL    Z,$2673             ; {}
1E46: 21 E4 A9        LD      HL,$A9E4            
1E49: CD 1C 1F        CALL    $1F1C               ; {}
1E4C: 3A 34 81        LD      A,($8134)           
1E4F: A7              AND     A                   
1E50: 28 09           JR      Z,$1E5B             ; {}
1E52: 06 78           LD      B,$78               
1E54: CD CB 27        CALL    $27CB               ; {}
1E57: AF              XOR     A                   
1E58: 32 34 81        LD      ($8134),A           
1E5B: 3A FD 83        LD      A,($83FD)           
1E5E: 3D              DEC     A                   
1E5F: 20 0F           JR      NZ,$1E70            ; {}
1E61: 3E 01           LD      A,$01               
1E63: 32 60 82        LD      ($8260),A           
1E66: 21 5C 82        LD      HL,$825C            
1E69: 34              INC     (HL)                
1E6A: C9              RET                         
1E6B: 3A 65 82        LD      A,($8265)           
1E6E: 18 C2           JR      $1E32               ; {}
1E70: 3E 01           LD      A,$01               
1E72: 32 65 82        LD      ($8265),A           
1E75: 21 5D 82        LD      HL,$825D            
1E78: 34              INC     (HL)                
1E79: C9              RET                         
1E7A: 3A FD 83        LD      A,($83FD)           
1E7D: 3D              DEC     A                   
1E7E: 20 3C           JR      NZ,$1EBC            ; {}
1E80: 3A 61 82        LD      A,($8261)           
1E83: A7              AND     A                   
1E84: C0              RET     NZ                  
1E85: 3A 47 80        LD      A,($8047)           
1E88: FE 2A           CP      $2A                 
1E8A: D2 CB 1A        JP      NC,$1ACB            ; {}
1E8D: 06 A8           LD      B,$A8               
1E8F: 3A 21 81        LD      A,($8121)           
1E92: D6 04           SUB     $04                 
1E94: CC 73 26        CALL    Z,$2673             ; {}
1E97: 21 24 A9        LD      HL,$A924            
1E9A: CD 1C 1F        CALL    $1F1C               ; {}
1E9D: 3A 34 81        LD      A,($8134)           
1EA0: A7              AND     A                   
1EA1: 28 09           JR      Z,$1EAC             ; {}
1EA3: 06 A8           LD      B,$A8               
1EA5: CD CB 27        CALL    $27CB               ; {}
1EA8: AF              XOR     A                   
1EA9: 32 34 81        LD      ($8134),A           
1EAC: 3A FD 83        LD      A,($83FD)           
1EAF: 3D              DEC     A                   
1EB0: 20 0F           JR      NZ,$1EC1            ; {}
1EB2: 3E 01           LD      A,$01               
1EB4: 32 61 82        LD      ($8261),A           
1EB7: 21 5C 82        LD      HL,$825C            
1EBA: 34              INC     (HL)                
1EBB: C9              RET                         
1EBC: 3A 66 82        LD      A,($8266)           
1EBF: 18 C2           JR      $1E83               ; {}
1EC1: 3E 01           LD      A,$01               
1EC3: 32 66 82        LD      ($8266),A           
1EC6: 21 5D 82        LD      HL,$825D            
1EC9: 34              INC     (HL)                
1ECA: C9              RET                         
1ECB: 3A FD 83        LD      A,($83FD)           
1ECE: 3D              DEC     A                   
1ECF: 20 3C           JR      NZ,$1F0D            ; {}
1ED1: 3A 62 82        LD      A,($8262)           
1ED4: A7              AND     A                   
1ED5: C0              RET     NZ                  
1ED6: 3A 47 80        LD      A,($8047)           
1ED9: FE 2A           CP      $2A                 
1EDB: D2 CB 1A        JP      NC,$1ACB            ; {}
1EDE: 06 D8           LD      B,$D8               
1EE0: 3A 21 81        LD      A,($8121)           
1EE3: D6 05           SUB     $05                 
1EE5: CC 73 26        CALL    Z,$2673             ; {}
1EE8: 21 64 A8        LD      HL,$A864            
1EEB: CD 1C 1F        CALL    $1F1C               ; {}
1EEE: 3A 34 81        LD      A,($8134)           
1EF1: A7              AND     A                   
1EF2: 28 09           JR      Z,$1EFD             ; {}
1EF4: 06 D8           LD      B,$D8               
1EF6: CD CB 27        CALL    $27CB               ; {}
1EF9: AF              XOR     A                   
1EFA: 32 34 81        LD      ($8134),A           
1EFD: 3A FD 83        LD      A,($83FD)           
1F00: 3D              DEC     A                   
1F01: 20 0F           JR      NZ,$1F12            ; {}
1F03: 3E 01           LD      A,$01               
1F05: 32 62 82        LD      ($8262),A           
1F08: 21 5C 82        LD      HL,$825C            
1F0B: 34              INC     (HL)                
1F0C: C9              RET                         
1F0D: 3A 67 82        LD      A,($8267)           
1F10: 18 C2           JR      $1ED4               ; {}
1F12: 3E 01           LD      A,$01               
1F14: 32 67 82        LD      ($8267),A           
1F17: 21 5D 82        LD      HL,$825D            
1F1A: 34              INC     (HL)                
1F1B: C9              RET                         
1F1C: 3A 34 81        LD      A,($8134)           
1F1F: A7              AND     A                   
1F20: 28 09           JR      Z,$1F2B             ; {}
1F22: 11 20 00        LD      DE,$0020            
1F25: CD E0 08        CALL    $08E0               ; {}
1F28: CD BC 27        CALL    $27BC               ; {}
1F2B: 36 6C           LD      (HL),$6C            
1F2D: 23              INC     HL                  
1F2E: 36 6D           LD      (HL),$6D            
1F30: 01 1F 00        LD      BC,$001F            
1F33: 09              ADD     HL,BC               
1F34: 36 6E           LD      (HL),$6E            
1F36: 23              INC     HL                  
1F37: 36 6F           LD      (HL),$6F            
1F39: E5              PUSH    HL                  
1F3A: D5              PUSH    DE                  
1F3B: 11 05 00        LD      DE,$0005            
1F3E: CD E0 08        CALL    $08E0               ; {}
1F41: CD C5 08        CALL    $08C5               ; {}
1F44: 3A FE 83        LD      A,($83FE)           
1F47: B7              OR      A                   
1F48: 28 4A           JR      Z,$1F94             ; {}
1F4A: AF              XOR     A                   
1F4B: 67              LD      H,A                 
1F4C: 6F              LD      L,A                 
1F4D: 22 82 83        LD      ($8382),HL          
1F50: DF              RST     $18                 
1F51: 3E F0           LD      A,$F0               
1F53: DF              RST     $18                 
1F54: 3A FD 83        LD      A,($83FD)           
1F57: 21 5C 82        LD      HL,$825C            
1F5A: 3D              DEC     A                   
1F5B: 28 01           JR      Z,$1F5E             ; {}
1F5D: 2C              INC     L                   
1F5E: 7E              LD      A,(HL)              
1F5F: FE 04           CP      $04                 
1F61: 28 1E           JR      Z,$1F81             ; {}
1F63: 3E 08           LD      A,$08               
1F65: DF              RST     $18                 
1F66: 3E 0E           LD      A,$0E               
1F68: DF              RST     $18                 
1F69: 21 81 83        LD      HL,$8381            
1F6C: 35              DEC     (HL)                
1F6D: 20 02           JR      NZ,$1F71            ; {}
1F6F: 36 14           LD      (HL),$14            
1F71: 7E              LD      A,(HL)              
1F72: 21 87 2E        LD      HL,$2E87            
1F75: 87              ADD     A,A                 
1F76: 85              ADD     A,L                 
1F77: 6F              LD      L,A                 
1F78: 7E              LD      A,(HL)              
1F79: 2C              INC     L                   
1F7A: 66              LD      H,(HL)              
1F7B: 6F              LD      L,A                 
1F7C: 22 82 83        LD      ($8382),HL          
1F7F: 18 13           JR      $1F94               ; {}
1F81: 32 2F 84        LD      ($842F),A           
1F84: CD E6 07        CALL    $07E6               ; {}
1F87: 21 40 B0        LD      HL,$B040            
1F8A: 01 00 18        LD      BC,$1800            
1F8D: 71              LD      (HL),C              
1F8E: 2C              INC     L                   
1F8F: 10 FC           DJNZ    $1F8D               ; {}
1F91: CD BC 27        CALL    $27BC               ; {}
1F94: 3E 20           LD      A,$20               
1F96: 32 6A 82        LD      ($826A),A           
1F99: 3E 80           LD      A,$80               
1F9B: DF              RST     $18                 
1F9C: 21 44 80        LD      HL,$8044            
1F9F: AF              XOR     A                   
1FA0: 77              LD      (HL),A              
1FA1: 23              INC     HL                  
1FA2: 77              LD      (HL),A              
1FA3: 23              INC     HL                  
1FA4: 77              LD      (HL),A              
1FA5: 23              INC     HL                  
1FA6: 36 F0           LD      (HL),$F0            
1FA8: D1              POP     DE                  
1FA9: E1              POP     HL                  
1FAA: AF              XOR     A                   
1FAB: 32 9B 82        LD      ($829B),A           
1FAE: 32 EA 83        LD      ($83EA),A           
1FB1: 32 4D 82        LD      ($824D),A           
1FB4: 32 49 82        LD      ($8249),A           
1FB7: 32 51 82        LD      ($8251),A           
1FBA: 3C              INC     A                   
1FBB: 32 6C 82        LD      ($826C),A           
1FBE: 32 CD 83        LD      ($83CD),A           
1FC1: 3E 10           LD      A,$10               
1FC3: 32 68 82        LD      ($8268),A           
1FC6: C9              RET                         
1FC7: 3A 6C 82        LD      A,($826C)           
1FCA: A7              AND     A                   
1FCB: C8              RET     Z                   
1FCC: 21 6A 82        LD      HL,$826A            
1FCF: 35              DEC     (HL)                
1FD0: C0              RET     NZ                  
1FD1: AF              XOR     A                   
1FD2: 32 6C 82        LD      ($826C),A           
1FD5: C9              RET                         
1FD6: 3A 47 80        LD      A,($8047)           
1FD9: FE 30           CP      $30                 
1FDB: D8              RET     C                   
1FDC: FE D0           CP      $D0                 
1FDE: 4F              LD      C,A                 
1FDF: 28 17           JR      Z,$1FF8             ; {}
1FE1: D0              RET     NC                  
1FE2: 3A 69 82        LD      A,($8269)           
1FE5: B9              CP      C                   
1FE6: D8              RET     C                   
1FE7: C8              RET     Z                   
1FE8: 79              LD      A,C                 
1FE9: 32 69 82        LD      ($8269),A           
1FEC: 11 01 00        LD      DE,$0001            
1FEF: FE 80           CP      $80                 
1FF1: C8              RET     Z                   
1FF2: E5              PUSH    HL                  
1FF3: CD E0 08        CALL    $08E0               ; {}
1FF6: E1              POP     HL                  
1FF7: C9              RET                         
1FF8: 3A 69 82        LD      A,($8269)           
1FFB: A7              AND     A                   
1FFC: 20 E4           JR      NZ,$1FE2            ; {}
1FFE: 3E E0           LD      A,$E0               
2000: 32 69 82        LD      ($8269),A           
2003: 18 DD           JR      $1FE2               ; {}
2005: DD 21 73 82     LD      IX,$8273            
2009: DD 7E 02        LD      A,(IX+$02)          
200C: 32 1A 81        LD      ($811A),A           
200F: 3A 10 81        LD      A,($8110)           
2012: 3C              INC     A                   
2013: 32 10 81        LD      ($8110),A           
2016: FE 50           CP      $50                 
2018: D4 FB 20        CALL    NC,$20FB            ; {}
201B: DD 21 7C 82     LD      IX,$827C            
201F: DD 7E 02        LD      A,(IX+$02)          
2022: 32 19 81        LD      ($8119),A           
2025: 3A 11 81        LD      A,($8111)           
2028: 3C              INC     A                   
2029: 3C              INC     A                   
202A: 32 11 81        LD      ($8111),A           
202D: FE A0           CP      $A0                 
202F: DC 9C 21        CALL    C,$219C             ; {}
2032: 3A 6E 82        LD      A,($826E)           
2035: 3C              INC     A                   
2036: 32 6E 82        LD      ($826E),A           
2039: FE 10           CP      $10                 
203B: CA 49 20        JP      Z,$2049             ; {}
203E: FE 20           CP      $20                 
2040: CA 6F 20        JP      Z,$206F             ; {}
2043: FE 30           CP      $30                 
2045: CA 95 20        JP      Z,$2095             ; {}
2048: C9              RET                         
2049: 21 73 82        LD      HL,$8273            
204C: 7E              LD      A,(HL)              
204D: 23              INC     HL                  
204E: 46              LD      B,(HL)              
204F: 21 1A 81        LD      HL,$811A            
2052: 4E              LD      C,(HL)              
2053: 11 23 14        LD      DE,$1423            
2056: 32 B1 81        LD      ($81B1),A           
2059: CD CC 20        CALL    $20CC               ; {}
205C: 21 7C 82        LD      HL,$827C            
205F: 7E              LD      A,(HL)              
2060: 23              INC     HL                  
2061: 46              LD      B,(HL)              
2062: 21 19 81        LD      HL,$8119            
2065: 4E              LD      C,(HL)              
2066: 11 5F 14        LD      DE,$145F            
2069: 32 B1 81        LD      ($81B1),A           
206C: C3 BF 20        JP      $20BF               ; {}
206F: 21 73 82        LD      HL,$8273            
2072: 7E              LD      A,(HL)              
2073: 23              INC     HL                  
2074: 46              LD      B,(HL)              
2075: 21 1A 81        LD      HL,$811A            
2078: 4E              LD      C,(HL)              
2079: 11 2B 14        LD      DE,$142B            
207C: 32 B1 81        LD      ($81B1),A           
207F: CD CC 20        CALL    $20CC               ; {}
2082: 21 7C 82        LD      HL,$827C            
2085: 7E              LD      A,(HL)              
2086: 23              INC     HL                  
2087: 46              LD      B,(HL)              
2088: 21 19 81        LD      HL,$8119            
208B: 4E              LD      C,(HL)              
208C: 11 73 14        LD      DE,$1473            
208F: 32 B1 81        LD      ($81B1),A           
2092: C3 BF 20        JP      $20BF               ; {}
2095: 21 73 82        LD      HL,$8273            
2098: 7E              LD      A,(HL)              
2099: 23              INC     HL                  
209A: 46              LD      B,(HL)              
209B: 21 1A 81        LD      HL,$811A            
209E: 4E              LD      C,(HL)              
209F: 11 33 14        LD      DE,$1433            
20A2: 32 B1 81        LD      ($81B1),A           
20A5: AF              XOR     A                   
20A6: 32 6E 82        LD      ($826E),A           
20A9: CD CC 20        CALL    $20CC               ; {}
20AC: 21 7C 82        LD      HL,$827C            
20AF: 7E              LD      A,(HL)              
20B0: 23              INC     HL                  
20B1: 46              LD      B,(HL)              
20B2: 21 19 81        LD      HL,$8119            
20B5: 4E              LD      C,(HL)              
20B6: 11 87 14        LD      DE,$1487            
20B9: 32 B1 81        LD      ($81B1),A           
20BC: C3 BF 20        JP      $20BF               ; {}
20BF: 2A F5 13        LD      HL,($13F5)          ; {}
20C2: ED 53 01 80     LD      ($8001),DE          
20C6: 78              LD      A,B                 
20C7: 32 03 80        LD      ($8003),A           
20CA: 18 0B           JR      $20D7               ; {}
20CC: 2A EF 13        LD      HL,($13EF)          ; {}
20CF: ED 53 01 80     LD      ($8001),DE          
20D3: 78              LD      A,B                 
20D4: 32 03 80        LD      ($8003),A           
20D7: 1A              LD      A,(DE)              
20D8: 77              LD      (HL),A              
20D9: 23              INC     HL                  
20DA: 13              INC     DE                  
20DB: 1A              LD      A,(DE)              
20DC: 77              LD      (HL),A              
20DD: 2B              DEC     HL                  
20DE: D5              PUSH    DE                  
20DF: 11 20 00        LD      DE,$0020            
20E2: 19              ADD     HL,DE               
20E3: D1              POP     DE                  
20E4: 13              INC     DE                  
20E5: 10 F0           DJNZ    $20D7               ; {}
20E7: 3A B1 81        LD      A,($81B1)           
20EA: 5F              LD      E,A                 
20EB: 16 00           LD      D,$00               
20ED: 19              ADD     HL,DE               
20EE: 3A 03 80        LD      A,($8003)           
20F1: 47              LD      B,A                 
20F2: ED 5B 01 80     LD      DE,($8001)          
20F6: 0D              DEC     C                   
20F7: C2 D7 20        JP      NZ,$20D7            ; {}
20FA: C9              RET                         
20FB: DD 21 73 82     LD      IX,$8273            
20FF: AF              XOR     A                   
2100: 67              LD      H,A                 
2101: DD 46 01        LD      B,(IX+$01)          
2104: C6 20           ADD     $20                 
2106: 10 FC           DJNZ    $2104               ; {}
2108: 4F              LD      C,A                 
2109: DD 6E 00        LD      L,(IX+$00)          
210C: 09              ADD     HL,BC               
210D: 5D              LD      E,L                 
210E: 54              LD      D,H                 
210F: AF              XOR     A                   
2110: 6F              LD      L,A                 
2111: 67              LD      H,A                 
2112: DD 46 02        LD      B,(IX+$02)          
2115: 05              DEC     B                   
2116: 19              ADD     HL,DE               
2117: 10 FD           DJNZ    $2116               ; {}
2119: 11 08 A8        LD      DE,$A808            
211C: 19              ADD     HL,DE               
211D: 0E 02           LD      C,$02               
211F: 3A 10 81        LD      A,($8110)           
2122: FE 50           CP      $50                 
2124: CA 3E 21        JP      Z,$213E             ; {}
2127: FE 80           CP      $80                 
2129: CA 4C 21        JP      Z,$214C             ; {}
212C: FE A0           CP      $A0                 
212E: CA 65 21        JP      Z,$2165             ; {}
2131: FE B0           CP      $B0                 
2133: CA 4C 21        JP      Z,$214C             ; {}
2136: FE D0           CP      $D0                 
2138: CA 3E 21        JP      Z,$213E             ; {}
213B: C3 88 21        JP      $2188               ; {}
213E: 06 02           LD      B,$02               
2140: 11 90 21        LD      DE,$2190            
2143: CD 78 21        CALL    $2178               ; {}
2146: 0D              DEC     C                   
2147: 20 F5           JR      NZ,$213E            ; {}
2149: C3 88 21        JP      $2188               ; {}
214C: 06 02           LD      B,$02               
214E: 11 94 21        LD      DE,$2194            
2151: CD 78 21        CALL    $2178               ; {}
2154: 0D              DEC     C                   
2155: 20 F5           JR      NZ,$214C            ; {}
2157: 3A 07 81        LD      A,($8107)           
215A: A7              AND     A                   
215B: CA 88 21        JP      Z,$2188             ; {}
215E: AF              XOR     A                   
215F: 32 07 81        LD      ($8107),A           
2162: C3 88 21        JP      $2188               ; {}
2165: 06 02           LD      B,$02               
2167: 11 98 21        LD      DE,$2198            
216A: CD 78 21        CALL    $2178               ; {}
216D: 0D              DEC     C                   
216E: 20 F5           JR      NZ,$2165            ; {}
2170: 3E 01           LD      A,$01               
2172: 32 07 81        LD      ($8107),A           
2175: C3 88 21        JP      $2188               ; {}
2178: 1A              LD      A,(DE)              
2179: 77              LD      (HL),A              
217A: 13              INC     DE                  
217B: 23              INC     HL                  
217C: 1A              LD      A,(DE)              
217D: 77              LD      (HL),A              
217E: 13              INC     DE                  
217F: D5              PUSH    DE                  
2180: 11 1F 00        LD      DE,$001F            
2183: 19              ADD     HL,DE               
2184: D1              POP     DE                  
2185: 10 F1           DJNZ    $2178               ; {}
2187: C9              RET                         
2188: DD 7E 02        LD      A,(IX+$02)          
218B: 3D              DEC     A                   
218C: 32 1A 81        LD      ($811A),A           
218F: C9              RET                         
2190: 94              SUB     H                   
2191: 95              SUB     L                   
2192: 96              SUB     (HL)                
2193: 97              SUB     A                   
2194: 98              SBC     B                   
2195: 99              SBC     C                   
2196: 9A              SBC     D                   
2197: 9B              SBC     E                   
2198: 10 10           DJNZ    $21AA               ; {}
219A: 10 10           DJNZ    $21AC               ; {}
219C: DD 21 7C 82     LD      IX,$827C            
21A0: AF              XOR     A                   
21A1: 67              LD      H,A                 
21A2: DD 46 01        LD      B,(IX+$01)          
21A5: C6 20           ADD     $20                 
21A7: 10 FC           DJNZ    $21A5               ; {}
21A9: 4F              LD      C,A                 
21AA: DD 6E 00        LD      L,(IX+$00)          
21AD: 09              ADD     HL,BC               
21AE: 5D              LD      E,L                 
21AF: 54              LD      D,H                 
21B0: AF              XOR     A                   
21B1: 6F              LD      L,A                 
21B2: 67              LD      H,A                 
21B3: DD 46 02        LD      B,(IX+$02)          
21B6: 05              DEC     B                   
21B7: 19              ADD     HL,DE               
21B8: 10 FD           DJNZ    $21B7               ; {}
21BA: 11 0E A8        LD      DE,$A80E            
21BD: 19              ADD     HL,DE               
21BE: 0E 03           LD      C,$03               
21C0: 3A 11 81        LD      A,($8111)           
21C3: FE 00           CP      $00                 
21C5: CA DF 21        JP      Z,$21DF             ; {}
21C8: FE 30           CP      $30                 
21CA: CA ED 21        JP      Z,$21ED             ; {}
21CD: FE 50           CP      $50                 
21CF: CA 06 22        JP      Z,$2206             ; {}
21D2: FE 60           CP      $60                 
21D4: CA ED 21        JP      Z,$21ED             ; {}
21D7: FE 70           CP      $70                 
21D9: CA DF 21        JP      Z,$21DF             ; {}
21DC: C3 29 22        JP      $2229               ; {}
21DF: 06 02           LD      B,$02               
21E1: 11 31 22        LD      DE,$2231            
21E4: CD 19 22        CALL    $2219               ; {}
21E7: 0D              DEC     C                   
21E8: 20 F5           JR      NZ,$21DF            ; {}
21EA: C3 29 22        JP      $2229               ; {}
21ED: 06 02           LD      B,$02               
21EF: 11 35 22        LD      DE,$2235            
21F2: CD 19 22        CALL    $2219               ; {}
21F5: 0D              DEC     C                   
21F6: 20 F5           JR      NZ,$21ED            ; {}
21F8: 3A 08 81        LD      A,($8108)           
21FB: A7              AND     A                   
21FC: CA 29 22        JP      Z,$2229             ; {}
21FF: AF              XOR     A                   
2200: 32 08 81        LD      ($8108),A           
2203: C3 29 22        JP      $2229               ; {}
2206: 06 02           LD      B,$02               
2208: 11 39 22        LD      DE,$2239            
220B: CD 19 22        CALL    $2219               ; {}
220E: 0D              DEC     C                   
220F: 20 F5           JR      NZ,$2206            ; {}
2211: 3E 01           LD      A,$01               
2213: 32 08 81        LD      ($8108),A           
2216: C3 29 22        JP      $2229               ; {}
2219: 1A              LD      A,(DE)              
221A: 77              LD      (HL),A              
221B: 13              INC     DE                  
221C: 23              INC     HL                  
221D: 1A              LD      A,(DE)              
221E: 77              LD      (HL),A              
221F: 13              INC     DE                  
2220: D5              PUSH    DE                  
2221: 11 1F 00        LD      DE,$001F            
2224: 19              ADD     HL,DE               
2225: D1              POP     DE                  
2226: 10 F1           DJNZ    $2219               ; {}
2228: C9              RET                         
2229: DD 7E 02        LD      A,(IX+$02)          
222C: 3D              DEC     A                   
222D: 32 19 81        LD      ($8119),A           
2230: C9              RET                         
2231: 94              SUB     H                   
2232: 95              SUB     L                   
2233: 96              SUB     (HL)                
2234: 97              SUB     A                   
2235: 98              SBC     B                   
2236: 99              SBC     C                   
2237: 9A              SBC     D                   
2238: 9B              SBC     E                   
2239: 10 10           DJNZ    $224B               ; {}
223B: 10 10           DJNZ    $224D               ; {}
223D: D9              EXX                         
223E: 21 93 82        LD      HL,$8293            
2241: 3A FD 83        LD      A,($83FD)           
2244: 3D              DEC     A                   
2245: 28 01           JR      Z,$2248             ; {}
2247: 2C              INC     L                   
2248: 7E              LD      A,(HL)              
2249: 01 60 22        LD      BC,$2260            
224C: 26 00           LD      H,$00               
224E: 6F              LD      L,A                 
224F: 85              ADD     A,L                 
2250: 6F              LD      L,A                 
2251: 09              ADD     HL,BC               
2252: 5E              LD      E,(HL)              
2253: 23              INC     HL                  
2254: 56              LD      D,(HL)              
2255: EB              EX      DE,HL               
2256: 11 70 82        LD      DE,$8270            
2259: 01 21 00        LD      BC,$0021            
225C: ED B0           LDIR                        
225E: D9              EXX                         
225F: C9              RET                         
2260: 6A              LD      L,D                 
2261: 22 8B 22        LD      ($228B),HL          ; {}
2264: AC              XOR     H                   
2265: 22 CD 22        LD      ($22CD),HL          ; {}
2268: EE 22           XOR     $22                 
226A: 60              LD      H,B                 
226B: 08              EX      AF,AF'              
226C: 03              INC     BC                  
226D: 60              LD      H,B                 
226E: 04              INC     B                   
226F: 04              INC     B                   
2270: 80              ADD     A,B                 
2271: 0C              INC     C                   
2272: 02              LD      (BC),A              
2273: 80              ADD     A,B                 
2274: 06 03           LD      B,$03               
2276: 40              LD      B,B                 
2277: 06 04           LD      B,$04               
2279: 80              ADD     A,B                 
227A: 02              LD      (BC),A              
227B: 04              INC     B                   
227C: E0              RET     PO                  
227D: 04              INC     B                   
227E: 02              LD      (BC),A              
227F: 60              LD      H,B                 
2280: 02              LD      (BC),A              
2281: 01 C0 02        LD      BC,$02C0            
2284: 03              INC     BC                  
2285: C0              RET     NZ                  
2286: 02              LD      (BC),A              
2287: 03              INC     BC                  
2288: E0              RET     PO                  
2289: 02              LD      (BC),A              
228A: 03              INC     BC                  
228B: 60              LD      H,B                 
228C: 08              EX      AF,AF'              
228D: 03              INC     BC                  
228E: 40              LD      B,B                 
228F: 04              INC     B                   
2290: 05              DEC     B                   
2291: 80              ADD     A,B                 
2292: 0C              INC     C                   
2293: 01 60 06        LD      BC,$0660            
2296: 03              INC     BC                  
2297: C0              RET     NZ                  
2298: 06 03           LD      B,$03               
229A: 80              ADD     A,B                 
229B: 02              LD      (BC),A              
229C: 04              INC     B                   
229D: E0              RET     PO                  
229E: 04              INC     B                   
229F: 03              INC     BC                  
22A0: 60              LD      H,B                 
22A1: 02              LD      (BC),A              
22A2: 02              LD      (BC),A              
22A3: E0              RET     PO                  
22A4: 02              LD      (BC),A              
22A5: 04              INC     B                   
22A6: C0              RET     NZ                  
22A7: 02              LD      (BC),A              
22A8: 04              INC     B                   
22A9: E0              RET     PO                  
22AA: 02              LD      (BC),A              
22AB: 04              INC     B                   
22AC: 60              LD      H,B                 
22AD: 08              EX      AF,AF'              
22AE: 02              LD      (BC),A              
22AF: 80              ADD     A,B                 
22B0: 04              INC     B                   
22B1: 04              INC     B                   
22B2: 80              ADD     A,B                 
22B3: 0C              INC     C                   
22B4: 01 C0 06        LD      BC,$06C0            
22B7: 03              INC     BC                  
22B8: 60              LD      H,B                 
22B9: 06 03           LD      B,$03               
22BB: 80              ADD     A,B                 
22BC: 02              LD      (BC),A              
22BD: 04              INC     B                   
22BE: A0              AND     B                   
22BF: 04              INC     B                   
22C0: 03              INC     BC                  
22C1: E0              RET     PO                  
22C2: 02              LD      (BC),A              
22C3: 02              LD      (BC),A              
22C4: A0              AND     B                   
22C5: 02              LD      (BC),A              
22C6: 05              DEC     B                   
22C7: E0              RET     PO                  
22C8: 02              LD      (BC),A              
22C9: 04              INC     B                   
22CA: C0              RET     NZ                  
22CB: 02              LD      (BC),A              
22CC: 04              INC     B                   
22CD: 60              LD      H,B                 
22CE: 08              EX      AF,AF'              
22CF: 02              LD      (BC),A              
22D0: A0              AND     B                   
22D1: 04              INC     B                   
22D2: 03              INC     BC                  
22D3: 80              ADD     A,B                 
22D4: 0C              INC     C                   
22D5: 01 E0 06        LD      BC,$06E0            
22D8: 02              LD      (BC),A              
22D9: 80              ADD     A,B                 
22DA: 06 03           LD      B,$03               
22DC: 80              ADD     A,B                 
22DD: 02              LD      (BC),A              
22DE: 04              INC     B                   
22DF: 80              ADD     A,B                 
22E0: 04              INC     B                   
22E1: 04              INC     B                   
22E2: C0              RET     NZ                  
22E3: 02              LD      (BC),A              
22E4: 03              INC     BC                  
22E5: E0              RET     PO                  
22E6: 02              LD      (BC),A              
22E7: 04              INC     B                   
22E8: A0              AND     B                   
22E9: 02              LD      (BC),A              
22EA: 04              INC     B                   
22EB: E0              RET     PO                  
22EC: 02              LD      (BC),A              
22ED: 04              INC     B                   
22EE: 60              LD      H,B                 
22EF: 08              EX      AF,AF'              
22F0: 01 E0 04        LD      BC,$04E0            
22F3: 03              INC     BC                  
22F4: 80              ADD     A,B                 
22F5: 0C              INC     C                   
22F6: 01 A0 06        LD      BC,$06A0            
22F9: 02              LD      (BC),A              
22FA: E0              RET     PO                  
22FB: 06 02           LD      B,$02               
22FD: 80              ADD     A,B                 
22FE: 02              LD      (BC),A              
22FF: 04              INC     B                   
2300: 60              LD      H,B                 
2301: 04              INC     B                   
2302: 03              INC     BC                  
2303: A0              AND     B                   
2304: 02              LD      (BC),A              
2305: 04              INC     B                   
2306: 80              ADD     A,B                 
2307: 02              LD      (BC),A              
2308: 05              DEC     B                   
2309: C0              RET     NZ                  
230A: 02              LD      (BC),A              
230B: 04              INC     B                   
230C: A0              AND     B                   
230D: 02              LD      (BC),A              
230E: 05              DEC     B                   
230F: 3A D6 83        LD      A,($83D6)           
2312: 3D              DEC     A                   
2313: C0              RET     NZ                  
2314: 3A 9B 82        LD      A,($829B)           
2317: A7              AND     A                   
2318: C0              RET     NZ                  
2319: 32 B4 83        LD      ($83B4),A           
231C: CD BA 0A        CALL    $0ABA               ; {}
231F: CD 29 06        CALL    $0629               ; {}
2322: CD 3D 22        CALL    $223D               ; {}
2325: AF              XOR     A                   
2326: 32 5B 82        LD      ($825B),A           
2329: CD 52 19        CALL    $1952               ; {}
232C: 21 50 A8        LD      HL,$A850            
232F: CD E2 19        CALL    $19E2               ; {}
2332: CD AA 09        CALL    $09AA               ; {}
2335: CD AF 0F        CALL    $0FAF               ; {}
2338: 3E 01           LD      A,$01               
233A: 32 5B 82        LD      ($825B),A           
233D: 32 9B 82        LD      ($829B),A           
2340: C9              RET                         
2341: 3A D6 83        LD      A,($83D6)           
2344: 3D              DEC     A                   
2345: C0              RET     NZ                  
2346: 3A 9B 82        LD      A,($829B)           
2349: A7              AND     A                   
234A: C8              RET     Z                   
234B: CD 6D 23        CALL    $236D               ; {}
234E: CD 55 1A        CALL    $1A55               ; {}
2351: CD B7 23        CALL    $23B7               ; {}
2354: CD 42 09        CALL    $0942               ; {}
2357: CD 70 08        CALL    $0870               ; {}
235A: CD 05 20        CALL    $2005               ; {}
235D: CD 02 18        CALL    $1802               ; {}
2360: CD BF 11        CALL    $11BF               ; {}
2363: CD F8 16        CALL    $16F8               ; {}
2366: CD C7 1F        CALL    $1FC7               ; {}
2369: CD B7 14        CALL    $14B7               ; {}
236C: C9              RET                         
236D: 3A 6C 82        LD      A,($826C)           
2370: B7              OR      A                   
2371: C0              RET     NZ                  
2372: 3A 04 80        LD      A,($8004)           
2375: A7              AND     A                   
2376: C0              RET     NZ                  
2377: 3A 99 82        LD      A,($8299)           
237A: A7              AND     A                   
237B: C2 E6 23        JP      NZ,$23E6            ; {}
237E: 11 47 80        LD      DE,$8047            
2381: 3E 30           LD      A,$30               
2383: 32 99 82        LD      ($8299),A           
2386: 21 9A 82        LD      HL,$829A            
2389: 34              INC     (HL)                
238A: 4E              LD      C,(HL)              
238B: 06 00           LD      B,$00               
238D: 21 68 2E        LD      HL,$2E68            
2390: 09              ADD     HL,BC               
2391: 4E              LD      C,(HL)              
2392: 0C              INC     C                   
2393: CA AC 23        JP      Z,$23AC             ; {}
2396: 21 9C 23        LD      HL,$239C            
2399: 09              ADD     HL,BC               
239A: E5              PUSH    HL                  
239B: 21 44 80        LD      HL,$8044            
239E: C9              RET                         
239F: C3 A0 1C        JP      $1CA0               ; {}
23A2: C3 41 1C        JP      $1C41               ; {}
23A5: C3 E4 1B        JP      $1BE4               ; {}
23A8: C3 8B 1B        JP      $1B8B               ; {}
23AB: C9              RET                         
23AC: AF              XOR     A                   
23AD: 32 9A 82        LD      ($829A),A           
23B0: 32 99 82        LD      ($8299),A           
23B3: 32 5B 82        LD      ($825B),A           
23B6: C9              RET                         
23B7: 21 44 80        LD      HL,$8044            
23BA: 11 47 80        LD      DE,$8047            
23BD: 3A 48 82        LD      A,($8248)           
23C0: A7              AND     A                   
23C1: C2 BA 1B        JP      NZ,$1BBA            ; {}
23C4: 32 4C 82        LD      ($824C),A           
23C7: 3A 49 82        LD      A,($8249)           
23CA: A7              AND     A                   
23CB: C2 0D 1C        JP      NZ,$1C0D            ; {}
23CE: 32 4D 82        LD      ($824D),A           
23D1: 3A 4A 82        LD      A,($824A)           
23D4: A7              AND     A                   
23D5: C2 76 1C        JP      NZ,$1C76            ; {}
23D8: 32 4E 82        LD      ($824E),A           
23DB: 3A 4B 82        LD      A,($824B)           
23DE: A7              AND     A                   
23DF: C2 D5 1C        JP      NZ,$1CD5            ; {}
23E2: 32 4F 82        LD      ($824F),A           
23E5: C9              RET                         
23E6: 3D              DEC     A                   
23E7: 32 99 82        LD      ($8299),A           
23EA: C9              RET                         
23EB: 3A 23 81        LD      A,($8123)           
23EE: 3C              INC     A                   
23EF: 32 23 81        LD      ($8123),A           
23F2: FE 06           CP      $06                 
23F4: D8              RET     C                   
23F5: AF              XOR     A                   
23F6: 32 23 81        LD      ($8123),A           
23F9: C9              RET                         
23FA: 3A FD 83        LD      A,($83FD)           
23FD: 4F              LD      C,A                 
23FE: 3A 23 81        LD      A,($8123)           
2401: 32 21 81        LD      ($8121),A           
2404: FE 01           CP      $01                 
2406: CA 1E 24        JP      Z,$241E             ; {}
2409: FE 02           CP      $02                 
240B: CA 33 24        JP      Z,$2433             ; {}
240E: FE 03           CP      $03                 
2410: CA 48 24        JP      Z,$2448             ; {}
2413: FE 04           CP      $04                 
2415: CA 5D 24        JP      Z,$245D             ; {}
2418: FE 05           CP      $05                 
241A: CA 72 24        JP      Z,$2472             ; {}
241D: C9              RET                         
241E: 0D              DEC     C                   
241F: 20 0B           JR      NZ,$242C            ; {}
2421: 3A 5E 82        LD      A,($825E)           
2424: A7              AND     A                   
2425: C0              RET     NZ                  
2426: 21 64 AB        LD      HL,$AB64            
2429: C3 87 24        JP      $2487               ; {}
242C: 3A 63 82        LD      A,($8263)           
242F: A7              AND     A                   
2430: C0              RET     NZ                  
2431: 18 F3           JR      $2426               ; {}
2433: 0D              DEC     C                   
2434: 20 0B           JR      NZ,$2441            ; {}
2436: 3A 5F 82        LD      A,($825F)           
2439: A7              AND     A                   
243A: C0              RET     NZ                  
243B: 21 A4 AA        LD      HL,$AAA4            
243E: C3 87 24        JP      $2487               ; {}
2441: 3A 64 82        LD      A,($8264)           
2444: A7              AND     A                   
2445: C0              RET     NZ                  
2446: 18 F3           JR      $243B               ; {}
2448: 0D              DEC     C                   
2449: 20 0B           JR      NZ,$2456            ; {}
244B: 3A 60 82        LD      A,($8260)           
244E: A7              AND     A                   
244F: C0              RET     NZ                  
2450: 21 E4 A9        LD      HL,$A9E4            
2453: C3 87 24        JP      $2487               ; {}
2456: 3A 65 82        LD      A,($8265)           
2459: A7              AND     A                   
245A: C0              RET     NZ                  
245B: 18 F3           JR      $2450               ; {}
245D: 0D              DEC     C                   
245E: 20 0B           JR      NZ,$246B            ; {}
2460: 3A 61 82        LD      A,($8261)           
2463: A7              AND     A                   
2464: C0              RET     NZ                  
2465: 21 24 A9        LD      HL,$A924            
2468: C3 87 24        JP      $2487               ; {}
246B: 3A 66 82        LD      A,($8266)           
246E: A7              AND     A                   
246F: C0              RET     NZ                  
2470: 18 F3           JR      $2465               ; {}
2472: 0D              DEC     C                   
2473: 20 0B           JR      NZ,$2480            ; {}
2475: 3A 62 82        LD      A,($8262)           
2478: A7              AND     A                   
2479: C0              RET     NZ                  
247A: 21 64 A8        LD      HL,$A864            
247D: C3 87 24        JP      $2487               ; {}
2480: 3A 67 82        LD      A,($8267)           
2483: A7              AND     A                   
2484: C0              RET     NZ                  
2485: 18 F3           JR      $247A               ; {}
2487: 36 2C           LD      (HL),$2C            
2489: 23              INC     HL                  
248A: 36 2D           LD      (HL),$2D            
248C: 01 1F 00        LD      BC,$001F            
248F: 09              ADD     HL,BC               
2490: 36 2E           LD      (HL),$2E            
2492: 23              INC     HL                  
2493: 36 2F           LD      (HL),$2F            
2495: C9              RET                         
2496: 3A FD 83        LD      A,($83FD)           
2499: 4F              LD      C,A                 
249A: 3A 23 81        LD      A,($8123)           
249D: 32 20 81        LD      ($8120),A           
24A0: FE 01           CP      $01                 
24A2: CA BA 24        JP      Z,$24BA             ; {}
24A5: FE 02           CP      $02                 
24A7: CA CF 24        JP      Z,$24CF             ; {}
24AA: FE 03           CP      $03                 
24AC: CA E4 24        JP      Z,$24E4             ; {}
24AF: FE 04           CP      $04                 
24B1: CA F9 24        JP      Z,$24F9             ; {}
24B4: FE 05           CP      $05                 
24B6: CA 0E 25        JP      Z,$250E             ; {}
24B9: C9              RET                         
24BA: 0D              DEC     C                   
24BB: 20 0B           JR      NZ,$24C8            ; {}
24BD: 3A 5E 82        LD      A,($825E)           
24C0: A7              AND     A                   
24C1: C0              RET     NZ                  
24C2: 21 64 AB        LD      HL,$AB64            
24C5: C3 23 25        JP      $2523               ; {}
24C8: 3A 63 82        LD      A,($8263)           
24CB: A7              AND     A                   
24CC: C0              RET     NZ                  
24CD: 18 F3           JR      $24C2               ; {}
24CF: 0D              DEC     C                   
24D0: 20 0B           JR      NZ,$24DD            ; {}
24D2: 3A 5F 82        LD      A,($825F)           
24D5: A7              AND     A                   
24D6: C0              RET     NZ                  
24D7: 21 A4 AA        LD      HL,$AAA4            
24DA: C3 23 25        JP      $2523               ; {}
24DD: 3A 64 82        LD      A,($8264)           
24E0: A7              AND     A                   
24E1: C0              RET     NZ                  
24E2: 18 F3           JR      $24D7               ; {}
24E4: 0D              DEC     C                   
24E5: 20 0B           JR      NZ,$24F2            ; {}
24E7: 3A 60 82        LD      A,($8260)           
24EA: A7              AND     A                   
24EB: C0              RET     NZ                  
24EC: 21 E4 A9        LD      HL,$A9E4            
24EF: C3 23 25        JP      $2523               ; {}
24F2: 3A 65 82        LD      A,($8265)           
24F5: A7              AND     A                   
24F6: C0              RET     NZ                  
24F7: 18 F3           JR      $24EC               ; {}
24F9: 0D              DEC     C                   
24FA: 20 0B           JR      NZ,$2507            ; {}
24FC: 3A 61 82        LD      A,($8261)           
24FF: A7              AND     A                   
2500: C0              RET     NZ                  
2501: 21 24 A9        LD      HL,$A924            
2504: C3 23 25        JP      $2523               ; {}
2507: 3A 66 82        LD      A,($8266)           
250A: A7              AND     A                   
250B: C0              RET     NZ                  
250C: 18 F3           JR      $2501               ; {}
250E: 0D              DEC     C                   
250F: 20 0B           JR      NZ,$251C            ; {}
2511: 3A 62 82        LD      A,($8262)           
2514: A7              AND     A                   
2515: C0              RET     NZ                  
2516: 21 64 A8        LD      HL,$A864            
2519: C3 23 25        JP      $2523               ; {}
251C: 3A 67 82        LD      A,($8267)           
251F: A7              AND     A                   
2520: C0              RET     NZ                  
2521: 18 F3           JR      $2516               ; {}
2523: 36 10           LD      (HL),$10            
2525: 23              INC     HL                  
2526: 36 10           LD      (HL),$10            
2528: 01 1F 00        LD      BC,$001F            
252B: 09              ADD     HL,BC               
252C: 36 D0           LD      (HL),$D0            
252E: 23              INC     HL                  
252F: 36 D1           LD      (HL),$D1            
2531: C9              RET                         
2532: 3A FD 83        LD      A,($83FD)           
2535: 4F              LD      C,A                 
2536: 3A 20 81        LD      A,($8120)           
2539: 32 21 81        LD      ($8121),A           
253C: FE 01           CP      $01                 
253E: CA 56 25        JP      Z,$2556             ; {}
2541: FE 02           CP      $02                 
2543: CA 6B 25        JP      Z,$256B             ; {}
2546: FE 03           CP      $03                 
2548: CA 80 25        JP      Z,$2580             ; {}
254B: FE 04           CP      $04                 
254D: CA 95 25        JP      Z,$2595             ; {}
2550: FE 05           CP      $05                 
2552: CA AA 25        JP      Z,$25AA             ; {}
2555: C9              RET                         
2556: 0D              DEC     C                   
2557: 20 0B           JR      NZ,$2564            ; {}
2559: 3A 5E 82        LD      A,($825E)           
255C: A7              AND     A                   
255D: C0              RET     NZ                  
255E: 21 64 AB        LD      HL,$AB64            
2561: C3 BF 25        JP      $25BF               ; {}
2564: 3A 63 82        LD      A,($8263)           
2567: A7              AND     A                   
2568: C0              RET     NZ                  
2569: 18 F3           JR      $255E               ; {}
256B: 0D              DEC     C                   
256C: 20 0B           JR      NZ,$2579            ; {}
256E: 3A 5F 82        LD      A,($825F)           
2571: A7              AND     A                   
2572: C0              RET     NZ                  
2573: 21 A4 AA        LD      HL,$AAA4            
2576: C3 BF 25        JP      $25BF               ; {}
2579: 3A 64 82        LD      A,($8264)           
257C: A7              AND     A                   
257D: C0              RET     NZ                  
257E: 18 F3           JR      $2573               ; {}
2580: 0D              DEC     C                   
2581: 20 0B           JR      NZ,$258E            ; {}
2583: 3A 60 82        LD      A,($8260)           
2586: A7              AND     A                   
2587: C0              RET     NZ                  
2588: 21 E4 A9        LD      HL,$A9E4            
258B: C3 BF 25        JP      $25BF               ; {}
258E: 3A 65 82        LD      A,($8265)           
2591: A7              AND     A                   
2592: C0              RET     NZ                  
2593: 18 F3           JR      $2588               ; {}
2595: 0D              DEC     C                   
2596: 20 0B           JR      NZ,$25A3            ; {}
2598: 3A 61 82        LD      A,($8261)           
259B: A7              AND     A                   
259C: C0              RET     NZ                  
259D: 21 24 A9        LD      HL,$A924            
25A0: C3 BF 25        JP      $25BF               ; {}
25A3: 3A 66 82        LD      A,($8266)           
25A6: A7              AND     A                   
25A7: C0              RET     NZ                  
25A8: 18 F3           JR      $259D               ; {}
25AA: 0D              DEC     C                   
25AB: 20 0B           JR      NZ,$25B8            ; {}
25AD: 3A 62 82        LD      A,($8262)           
25B0: A7              AND     A                   
25B1: C0              RET     NZ                  
25B2: 21 64 A8        LD      HL,$A864            
25B5: C3 BF 25        JP      $25BF               ; {}
25B8: 3A 67 82        LD      A,($8267)           
25BB: A7              AND     A                   
25BC: C0              RET     NZ                  
25BD: 18 F3           JR      $25B2               ; {}
25BF: 36 D0           LD      (HL),$D0            
25C1: 23              INC     HL                  
25C2: 36 D1           LD      (HL),$D1            
25C4: 01 1F 00        LD      BC,$001F            
25C7: 09              ADD     HL,BC               
25C8: 36 D2           LD      (HL),$D2            
25CA: 23              INC     HL                  
25CB: 36 D3           LD      (HL),$D3            
25CD: C9              RET                         
25CE: 3A FD 83        LD      A,($83FD)           
25D1: 4F              LD      C,A                 
25D2: 3A 21 81        LD      A,($8121)           
25D5: FE 01           CP      $01                 
25D7: CA EF 25        JP      Z,$25EF             ; {}
25DA: FE 02           CP      $02                 
25DC: CA 04 26        JP      Z,$2604             ; {}
25DF: FE 03           CP      $03                 
25E1: CA 19 26        JP      Z,$2619             ; {}
25E4: FE 04           CP      $04                 
25E6: CA 2E 26        JP      Z,$262E             ; {}
25E9: FE 05           CP      $05                 
25EB: CA 43 26        JP      Z,$2643             ; {}
25EE: C9              RET                         
25EF: 0D              DEC     C                   
25F0: 20 0B           JR      NZ,$25FD            ; {}
25F2: 3A 5E 82        LD      A,($825E)           
25F5: A7              AND     A                   
25F6: C0              RET     NZ                  
25F7: 21 64 AB        LD      HL,$AB64            
25FA: C3 58 26        JP      $2658               ; {}
25FD: 3A 63 82        LD      A,($8263)           
2600: A7              AND     A                   
2601: C0              RET     NZ                  
2602: 18 F3           JR      $25F7               ; {}
2604: 0D              DEC     C                   
2605: 20 0B           JR      NZ,$2612            ; {}
2607: 3A 5F 82        LD      A,($825F)           
260A: A7              AND     A                   
260B: C0              RET     NZ                  
260C: 21 A4 AA        LD      HL,$AAA4            
260F: C3 58 26        JP      $2658               ; {}
2612: 3A 64 82        LD      A,($8264)           
2615: A7              AND     A                   
2616: C0              RET     NZ                  
2617: 18 F3           JR      $260C               ; {}
2619: 0D              DEC     C                   
261A: 20 0B           JR      NZ,$2627            ; {}
261C: 3A 60 82        LD      A,($8260)           
261F: A7              AND     A                   
2620: C0              RET     NZ                  
2621: 21 E4 A9        LD      HL,$A9E4            
2624: C3 58 26        JP      $2658               ; {}
2627: 3A 65 82        LD      A,($8265)           
262A: A7              AND     A                   
262B: C0              RET     NZ                  
262C: 18 F3           JR      $2621               ; {}
262E: 0D              DEC     C                   
262F: 20 0B           JR      NZ,$263C            ; {}
2631: 3A 61 82        LD      A,($8261)           
2634: A7              AND     A                   
2635: C0              RET     NZ                  
2636: 21 24 A9        LD      HL,$A924            
2639: C3 58 26        JP      $2658               ; {}
263C: 3A 66 82        LD      A,($8266)           
263F: A7              AND     A                   
2640: C0              RET     NZ                  
2641: 18 F3           JR      $2636               ; {}
2643: 0D              DEC     C                   
2644: 20 0B           JR      NZ,$2651            ; {}
2646: 3A 62 82        LD      A,($8262)           
2649: A7              AND     A                   
264A: C0              RET     NZ                  
264B: 21 64 A8        LD      HL,$A864            
264E: C3 58 26        JP      $2658               ; {}
2651: 3A 67 82        LD      A,($8267)           
2654: A7              AND     A                   
2655: C0              RET     NZ                  
2656: 18 F3           JR      $264B               ; {}
2658: 36 10           LD      (HL),$10            
265A: 23              INC     HL                  
265B: 36 10           LD      (HL),$10            
265D: 01 1F 00        LD      BC,$001F            
2660: 09              ADD     HL,BC               
2661: 36 10           LD      (HL),$10            
2663: 23              INC     HL                  
2664: 36 10           LD      (HL),$10            
2666: 3A 04 80        LD      A,($8004)           
2669: A7              AND     A                   
266A: C0              RET     NZ                  
266B: AF              XOR     A                   
266C: 32 21 81        LD      ($8121),A           
266F: 32 20 81        LD      ($8120),A           
2672: C9              RET                         
2673: 3A 20 81        LD      A,($8120)           
2676: A7              AND     A                   
2677: C2 93 26        JP      NZ,$2693            ; {}
267A: 21 5C 80        LD      HL,$805C            
267D: 70              LD      (HL),B              
267E: 23              INC     HL                  
267F: 36 19           LD      (HL),$19            
2681: 23              INC     HL                  
2682: 36 03           LD      (HL),$03            
2684: 23              INC     HL                  
2685: 36 20           LD      (HL),$20            
2687: 3E A0           LD      A,$A0               
2689: 32 40 83        LD      ($8340),A           
268C: 11 20 00        LD      DE,$0020            
268F: CD E0 08        CALL    $08E0               ; {}
2692: C9              RET                         
2693: 3E 01           LD      A,$01               
2695: 32 04 80        LD      ($8004),A           
2698: E1              POP     HL                  
2699: C9              RET                         
269A: 21 5C 80        LD      HL,$805C            
269D: AF              XOR     A                   
269E: 77              LD      (HL),A              
269F: 23              INC     HL                  
26A0: 77              LD      (HL),A              
26A1: 23              INC     HL                  
26A2: 77              LD      (HL),A              
26A3: 23              INC     HL                  
26A4: 77              LD      (HL),A              
26A5: C9              RET                         
26A6: 3A 34 81        LD      A,($8134)           
26A9: A7              AND     A                   
26AA: C2 F0 26        JP      NZ,$26F0            ; {}
26AD: DD 21 1B 81     LD      IX,$811B            
26B1: DD 7E 01        LD      A,(IX+$01)          
26B4: A7              AND     A                   
26B5: CC 0D 27        CALL    Z,$270D             ; {}
26B8: 3A 3D 81        LD      A,($813D)           
26BB: CB 47           BIT     0,A                 
26BD: C2 B3 27        JP      NZ,$27B3            ; {}
26C0: 3A 35 81        LD      A,($8135)           
26C3: A7              AND     A                   
26C4: 20 01           JR      NZ,$26C7            ; {}
26C6: C9              RET                         
26C7: 3A 34 81        LD      A,($8134)           
26CA: A7              AND     A                   
26CB: 20 23           JR      NZ,$26F0            ; {}
26CD: CD 2F 27        CALL    $272F               ; {}
26D0: 3A 47 80        LD      A,($8047)           
26D3: FE 5A           CP      $5A                 
26D5: D8              RET     C                   
26D6: FE 68           CP      $68                 
26D8: D0              RET     NC                  
26D9: 3A 40 80        LD      A,($8040)           
26DC: 47              LD      B,A                 
26DD: 3A 44 80        LD      A,($8044)           
26E0: C6 04           ADD     $04                 
26E2: B8              CP      B                   
26E3: D8              RET     C                   
26E4: D6 08           SUB     $08                 
26E6: B8              CP      B                   
26E7: D0              RET     NC                  
26E8: 3E 01           LD      A,$01               
26EA: 32 34 81        LD      ($8134),A           
26ED: 3E 18           LD      A,$18               
26EF: DF              RST     $18                 
26F0: DD 21 44 80     LD      IX,$8044            
26F4: FD 21 40 80     LD      IY,$8040            
26F8: DD 7E 00        LD      A,(IX+$00)          
26FB: FD 77 00        LD      (IY+$00),A          
26FE: DD 7E 01        LD      A,(IX+$01)          
2701: FD 77 01        LD      (IY+$01),A          
2704: DD 7E 03        LD      A,(IX+$03)          
2707: C6 02           ADD     $02                 
2709: FD 77 03        LD      (IY+$03),A          
270C: C9              RET                         
270D: 3A 35 81        LD      A,($8135)           
2710: A7              AND     A                   
2711: C0              RET     NZ                  
2712: 21 3D 81        LD      HL,$813D            
2715: 34              INC     (HL)                
2716: 21 41 80        LD      HL,$8041            
2719: 36 1E           LD      (HL),$1E            
271B: 23              INC     HL                  
271C: 36 04           LD      (HL),$04            
271E: 23              INC     HL                  
271F: 36 60           LD      (HL),$60            
2721: 3E 01           LD      A,$01               
2723: 32 35 81        LD      ($8135),A           
2726: 32 3D 83        LD      ($833D),A           
2729: 3E 3C           LD      A,$3C               
272B: 32 3E 83        LD      ($833E),A           
272E: C9              RET                         
272F: 21 3E 83        LD      HL,$833E            
2732: 7E              LD      A,(HL)              
2733: A7              AND     A                   
2734: 28 2B           JR      Z,$2761             ; {}
2736: 35              DEC     (HL)                
2737: 3E 3C           LD      A,$3C               
2739: CB 3F           SRL     A                   
273B: BE              CP      (HL)                
273C: 20 0F           JR      NZ,$274D            ; {}
273E: 2B              DEC     HL                  
273F: 7E              LD      A,(HL)              
2740: A7              AND     A                   
2741: 3E 21           LD      A,$21               
2743: 32 41 80        LD      ($8041),A           
2746: F0              RET     P                   
2747: 3E A1           LD      A,$A1               
2749: 32 41 80        LD      ($8041),A           
274C: C9              RET                         
274D: 2B              DEC     HL                  
274E: 7E              LD      A,(HL)              
274F: E6 7F           AND     $7F                 
2751: 21 9F 27        LD      HL,$279F            
2754: 3C              INC     A                   
2755: CD 9A 27        CALL    $279A               ; {}
2758: 7E              LD      A,(HL)              
2759: 21 1C 81        LD      HL,$811C            
275C: 86              ADD     A,(HL)              
275D: 32 40 80        LD      ($8040),A           
2760: C9              RET                         
2761: 2B              DEC     HL                  
2762: 7E              LD      A,(HL)              
2763: A7              AND     A                   
2764: F2 69 27        JP      P,$2769             ; {}
2767: 35              DEC     (HL)                
2768: 35              DEC     (HL)                
2769: 34              INC     (HL)                
276A: 7E              LD      A,(HL)              
276B: E6 7F           AND     $7F                 
276D: 21 9F 27        LD      HL,$279F            
2770: CD 9A 27        CALL    $279A               ; {}
2773: 7E              LD      A,(HL)              
2774: FE 01           CP      $01                 
2776: 38 0A           JR      C,$2782             ; {}
2778: 28 1A           JR      Z,$2794             ; {}
277A: 21 1C 81        LD      HL,$811C            
277D: 86              ADD     A,(HL)              
277E: 32 40 80        LD      ($8040),A           
2781: C9              RET                         
2782: 21 3D 83        LD      HL,$833D            
2785: 7E              LD      A,(HL)              
2786: EE 80           XOR     $80                 
2788: 77              LD      (HL),A              
2789: 3E 3C           LD      A,$3C               
278B: 32 3E 83        LD      ($833E),A           
278E: 3E 1E           LD      A,$1E               
2790: 32 41 80        LD      ($8041),A           
2793: C9              RET                         
2794: 3E 3C           LD      A,$3C               
2796: 32 3E 83        LD      ($833E),A           
2799: C9              RET                         
279A: 85              ADD     A,L                 
279B: 6F              LD      L,A                 
279C: D0              RET     NC                  
279D: 24              INC     H                   
279E: C9              RET                         
279F: 00              NOP                         
27A0: EE EC           XOR     $EC                 
27A2: EA E8 E6        JP      PE,$E6E8            ; {hard.PPI8255+26E8}
27A5: E4 E2 E0        CALL    PO,$E0E2            ; {hard.PPI8255+20E2}
27A8: 01 DE DC        LD      BC,$DCDE            
27AB: DA D8 D6        JP      C,$D6D8             ; {hard.PPI8255+16D8}
27AE: D4 D2 D0        CALL    NC,$D0D2            ; {hard.PPI8255+10D2}
27B1: 00              NOP                         
27B2: D0              RET     NC                  
27B3: 3A 35 81        LD      A,($8135)           
27B6: A7              AND     A                   
27B7: C8              RET     Z                   
27B8: AF              XOR     A                   
27B9: 32 34 81        LD      ($8134),A           
27BC: 21 40 80        LD      HL,$8040            
27BF: AF              XOR     A                   
27C0: 77              LD      (HL),A              
27C1: 23              INC     HL                  
27C2: 77              LD      (HL),A              
27C3: 23              INC     HL                  
27C4: 77              LD      (HL),A              
27C5: 23              INC     HL                  
27C6: 77              LD      (HL),A              
27C7: 32 35 81        LD      ($8135),A           
27CA: C9              RET                         
27CB: 21 40 80        LD      HL,$8040            
27CE: 70              LD      (HL),B              
27CF: 23              INC     HL                  
27D0: 36 19           LD      (HL),$19            
27D2: 23              INC     HL                  
27D3: 36 03           LD      (HL),$03            
27D5: 23              INC     HL                  
27D6: 36 10           LD      (HL),$10            
27D8: 3E A0           LD      A,$A0               
27DA: 32 40 83        LD      ($8340),A           
27DD: C9              RET                         
27DE: 21 40 80        LD      HL,$8040            
27E1: AF              XOR     A                   
27E2: 77              LD      (HL),A              
27E3: 23              INC     HL                  
27E4: 77              LD      (HL),A              
27E5: 23              INC     HL                  
27E6: 77              LD      (HL),A              
27E7: 23              INC     HL                  
27E8: 77              LD      (HL),A              
27E9: C9              RET                         
27EA: 3A B7 83        LD      A,($83B7)           
27ED: FE 02           CP      $02                 
27EF: DA 73 28        JP      C,$2873             ; {}
27F2: FE 05           CP      $05                 
27F4: D2 74 28        JP      NC,$2874            ; {}
27F7: 3A 01 81        LD      A,($8101)           
27FA: A7              AND     A                   
27FB: CC 8C 28        CALL    Z,$288C             ; {}
27FE: 3A 4F 81        LD      A,($814F)           
2801: A7              AND     A                   
2802: C8              RET     Z                   
2803: 21 46 81        LD      HL,$8146            
2806: 7E              LD      A,(HL)              
2807: 23              INC     HL                  
2808: BE              CP      (HL)                
2809: C2 B0 28        JP      NZ,$28B0            ; {}
280C: 35              DEC     (HL)                
280D: 11 06 A8        LD      DE,$A806            
2810: 3A 50 81        LD      A,($8150)           
2813: CB 47           BIT     0,A                 
2815: CA 6D 28        JP      Z,$286D             ; {}
2818: 21 13 14        LD      HL,$1413            
281B: AF              XOR     A                   
281C: 47              LD      B,A                 
281D: 3A 4E 81        LD      A,($814E)           
2820: 4F              LD      C,A                 
2821: 3C              INC     A                   
2822: 3C              INC     A                   
2823: 32 4E 81        LD      ($814E),A           
2826: 09              ADD     HL,BC               
2827: 06 00           LD      B,$00               
2829: EB              EX      DE,HL               
282A: 3A 45 81        LD      A,($8145)           
282D: 4F              LD      C,A                 
282E: 09              ADD     HL,BC               
282F: EB              EX      DE,HL               
2830: 0E 20           LD      C,$20               
2832: 3A 45 81        LD      A,($8145)           
2835: 81              ADD     A,C                 
2836: 32 45 81        LD      ($8145),A           
2839: 7E              LD      A,(HL)              
283A: 12              LD      (DE),A              
283B: 23              INC     HL                  
283C: 13              INC     DE                  
283D: 7E              LD      A,(HL)              
283E: 12              LD      (DE),A              
283F: 3A 4E 81        LD      A,($814E)           
2842: FE 10           CP      $10                 
2844: D8              RET     C                   
2845: AF              XOR     A                   
2846: 32 4F 81        LD      ($814F),A           
2849: 32 4E 81        LD      ($814E),A           
284C: 32 45 81        LD      ($8145),A           
284F: 32 46 81        LD      ($8146),A           
2852: 32 47 81        LD      ($8147),A           
2855: C9              RET                         
2856: 3A FE 83        LD      A,($83FE)           
2859: FE 02           CP      $02                 
285B: C0              RET     NZ                  
285C: AF              XOR     A                   
285D: 32 4F 81        LD      ($814F),A           
2860: 32 4E 81        LD      ($814E),A           
2863: 32 45 81        LD      ($8145),A           
2866: 32 46 81        LD      ($8146),A           
2869: 32 47 81        LD      ($8147),A           
286C: C9              RET                         
286D: 21 03 14        LD      HL,$1403            
2870: C3 1B 28        JP      $281B               ; {}
2873: C9              RET                         
2874: 3A 01 81        LD      A,($8101)           
2877: A7              AND     A                   
2878: CC 7E 28        CALL    Z,$287E             ; {}
287B: C3 FE 27        JP      $27FE               ; {}
287E: 3A 4F 81        LD      A,($814F)           
2881: A7              AND     A                   
2882: C0              RET     NZ                  
2883: 3E 01           LD      A,$01               
2885: 32 50 81        LD      ($8150),A           
2888: CD 9C 28        CALL    $289C               ; {}
288B: C9              RET                         
288C: 3A 4F 81        LD      A,($814F)           
288F: A7              AND     A                   
2890: C0              RET     NZ                  
2891: 3A 50 81        LD      A,($8150)           
2894: 3C              INC     A                   
2895: 32 50 81        LD      ($8150),A           
2898: CD 9C 28        CALL    $289C               ; {}
289B: C9              RET                         
289C: 3A 9B 81        LD      A,($819B)           
289F: E6 0F           AND     $0F                 
28A1: 87              ADD     A,A                 
28A2: 87              ADD     A,A                 
28A3: 87              ADD     A,A                 
28A4: 21 46 81        LD      HL,$8146            
28A7: 77              LD      (HL),A              
28A8: 23              INC     HL                  
28A9: 77              LD      (HL),A              
28AA: 3E 01           LD      A,$01               
28AC: 32 4F 81        LD      ($814F),A           
28AF: C9              RET                         
28B0: 7E              LD      A,(HL)              
28B1: A7              AND     A                   
28B2: 28 02           JR      Z,$28B6             ; {}
28B4: 35              DEC     (HL)                
28B5: C9              RET                         
28B6: 3A 46 81        LD      A,($8146)           
28B9: 77              LD      (HL),A              
28BA: C9              RET                         
28BB: 3A 50 81        LD      A,($8150)           
28BE: CB 47           BIT     0,A                 
28C0: C8              RET     Z                   
28C1: 3A B7 83        LD      A,($83B7)           
28C4: FE 02           CP      $02                 
28C6: D8              RET     C                   
28C7: 3A 47 80        LD      A,($8047)           
28CA: C6 08           ADD     $08                 
28CC: FE 2A           CP      $2A                 
28CE: D8              RET     C                   
28CF: FE 3B           CP      $3B                 
28D1: D0              RET     NC                  
28D2: 3A 44 80        LD      A,($8044)           
28D5: C6 08           ADD     $08                 
28D7: 47              LD      B,A                 
28D8: 3A 01 81        LD      A,($8101)           
28DB: 4F              LD      C,A                 
28DC: C6 08           ADD     $08                 
28DE: B8              CP      B                   
28DF: D8              RET     C                   
28E0: 79              LD      A,C                 
28E1: D6 20           SUB     $20                 
28E3: B8              CP      B                   
28E4: D0              RET     NC                  
28E5: 79              LD      A,C                 
28E6: D6 08           SUB     $08                 
28E8: B8              CP      B                   
28E9: 30 04           JR      NC,$28EF            ; {}
28EB: CD D0 12        CALL    $12D0               ; {}
28EE: C9              RET                         
28EF: 3E 01           LD      A,$01               
28F1: 32 04 80        LD      ($8004),A           
28F4: 21 46 A8        LD      HL,$A846            
28F7: 36 68           LD      (HL),$68            
28F9: 23              INC     HL                  
28FA: 36 69           LD      (HL),$69            
28FC: 01 1F 00        LD      BC,$001F            
28FF: 09              ADD     HL,BC               
2900: 36 6A           LD      (HL),$6A            
2902: 23              INC     HL                  
2903: 36 6B           LD      (HL),$6B            
2905: C9              RET                         
2906: 3A FE 83        LD      A,($83FE)           
2909: A7              AND     A                   
290A: C8              RET     Z                   
290B: 3A A2 81        LD      A,($81A2)           
290E: FE 0F           CP      $0F                 
2910: D0              RET     NC                  
2911: FE 02           CP      $02                 
2913: D8              RET     C                   
2914: 3A 40 81        LD      A,($8140)           
2917: A7              AND     A                   
2918: C0              RET     NZ                  
2919: 3E D0           LD      A,$D0               
291B: DF              RST     $18                 
291C: C9              RET                         
291D: 3A 01 81        LD      A,($8101)           
2920: A7              AND     A                   
2921: 20 05           JR      NZ,$2928            ; {}
2923: AF              XOR     A                   
2924: 32 3F 83        LD      ($833F),A           
2927: C9              RET                         
2928: 3A 50 81        LD      A,($8150)           
292B: CB 47           BIT     0,A                 
292D: C8              RET     Z                   
292E: 3A 4F 81        LD      A,($814F)           
2931: A7              AND     A                   
2932: C0              RET     NZ                  
2933: 21 3F 83        LD      HL,$833F            
2936: 34              INC     (HL)                
2937: 7E              LD      A,(HL)              
2938: FE 40           CP      $40                 
293A: 28 05           JR      Z,$2941             ; {}
293C: FE 70           CP      $70                 
293E: 28 13           JR      Z,$2953             ; {}
2940: C9              RET                         
2941: 21 46 A8        LD      HL,$A846            
2944: 36 68           LD      (HL),$68            
2946: 23              INC     HL                  
2947: 36 69           LD      (HL),$69            
2949: 01 1F 00        LD      BC,$001F            
294C: 09              ADD     HL,BC               
294D: 36 6A           LD      (HL),$6A            
294F: 23              INC     HL                  
2950: 36 6B           LD      (HL),$6B            
2952: C9              RET                         
2953: 21 46 A8        LD      HL,$A846            
2956: 36 D0           LD      (HL),$D0            
2958: 23              INC     HL                  
2959: 36 D1           LD      (HL),$D1            
295B: 01 1F 00        LD      BC,$001F            
295E: 09              ADD     HL,BC               
295F: 36 D2           LD      (HL),$D2            
2961: 23              INC     HL                  
2962: 36 D3           LD      (HL),$D3            
2964: AF              XOR     A                   
2965: 32 3F 83        LD      ($833F),A           
2968: C9              RET                         
2969: FF              RST     $38                 
296A: FF              RST     $38                 
296B: FF              RST     $38                 
296C: FF              RST     $38                 
296D: FF              RST     $38                 
296E: FF              RST     $38                 
296F: FF              RST     $38                 
2970: 3A B7 83        LD      A,($83B7)           
2973: FE 03           CP      $03                 
2975: 38 2A           JR      C,$29A1             ; {}
2977: 3A FD 83        LD      A,($83FD)           
297A: 3D              DEC     A                   
297B: 20 06           JR      NZ,$2983            ; {}
297D: DD 21 40 84     LD      IX,$8440            
2981: 18 04           JR      $2987               ; {}
2983: DD 21 60 84     LD      IX,$8460            
2987: FD 21 48 80     LD      IY,$8048            
298B: CD B9 29        CALL    $29B9               ; {}
298E: 3A B7 83        LD      A,($83B7)           
2991: FE 06           CP      $06                 
2993: 38 07           JR      C,$299C             ; {}
2995: 11 10 00        LD      DE,$0010            
2998: DD 19           ADD     IX,DE               
299A: FD 21 50 80     LD      IY,$8050            
299E: CD B9 29        CALL    $29B9               ; {}
29A1: 3A FD 83        LD      A,($83FD)           
29A4: 3D              DEC     A                   
29A5: 20 06           JR      NZ,$29AD            ; {}
29A7: DD 21 80 84     LD      IX,$8480            
29AB: 18 04           JR      $29B1               ; {}
29AD: DD 21 90 84     LD      IX,$8490            
29B1: FD 21 58 80     LD      IY,$8058            
29B5: CD 83 2B        CALL    $2B83               ; {}
29B8: C9              RET                         
29B9: CD 6A 2A        CALL    $2A6A               ; {}
29BC: CD C9 29        CALL    $29C9               ; {}
29BF: CD F9 29        CALL    $29F9               ; {}
29C2: CD F3 2A        CALL    $2AF3               ; {}
29C5: CD 58 2B        CALL    $2B58               ; {}
29C8: C9              RET                         
29C9: DD 35 08        DEC     (IX+$08)            
29CC: C0              RET     NZ                  
29CD: DD 36 08 0C     LD      (IX+$08),$0C        
29D1: DD 7E 06        LD      A,(IX+$06)          
29D4: B7              OR      A                   
29D5: C8              RET     Z                   
29D6: 3D              DEC     A                   
29D7: 20 02           JR      NZ,$29DB            ; {}
29D9: 3E 04           LD      A,$04               
29DB: DD 77 06        LD      (IX+$06),A          
29DE: 6F              LD      L,A                 
29DF: 26 00           LD      H,$00               
29E1: 11 D5 2C        LD      DE,$2CD5            
29E4: 19              ADD     HL,DE               
29E5: 7E              LD      A,(HL)              
29E6: DD B6 05        OR      (IX+$05)            
29E9: FD 77 01        LD      (IY+$01),A          
29EC: 3C              INC     A                   
29ED: FD 77 05        LD      (IY+$05),A          
29F0: FD 36 02 04     LD      (IY+$02),$04        
29F4: FD 36 06 04     LD      (IY+$06),$04        
29F8: C9              RET                         
29F9: DD 7E 06        LD      A,(IX+$06)          
29FC: B7              OR      A                   
29FD: C8              RET     Z                   
29FE: 3A 2C 84        LD      A,($842C)           
2A01: B7              OR      A                   
2A02: C0              RET     NZ                  
2A03: DD 35 09        DEC     (IX+$09)            
2A06: C0              RET     NZ                  
2A07: DD 36 09 08     LD      (IX+$09),$08        
2A0B: FD 7E 03        LD      A,(IY+$03)          
2A0E: FE 60           CP      $60                 
2A10: 30 2A           JR      NC,$2A3C            ; {}
2A12: DD 36 07 01     LD      (IX+$07),$01        
2A16: DD 7E 05        LD      A,(IX+$05)          
2A19: B7              OR      A                   
2A1A: C2 2D 2A        JP      NZ,$2A2D            ; {}
2A1D: 3A 14 80        LD      A,($8014)           
2A20: DD 96 00        SUB     (IX+$00)            
2A23: D8              RET     C                   
2A24: FD BE 00        CP      (IY+$00)            
2A27: 30 2A           JR      NC,$2A53            ; {}
2A29: DD 34 02        INC     (IX+$02)            
2A2C: C9              RET                         
2A2D: 3A 14 80        LD      A,($8014)           
2A30: DD 96 01        SUB     (IX+$01)            
2A33: FD BE 00        CP      (IY+$00)            
2A36: 38 1B           JR      C,$2A53             ; {}
2A38: DD 35 02        DEC     (IX+$02)            
2A3B: C9              RET                         
2A3C: DD 36 07 01     LD      (IX+$07),$01        
2A40: DD 7E 05        LD      A,(IX+$05)          
2A43: B7              OR      A                   
2A44: 28 04           JR      Z,$2A4A             ; {}
2A46: 3E 02           LD      A,$02               
2A48: 18 02           JR      $2A4C               ; {}
2A4A: 3E FE           LD      A,$FE               
2A4C: DD 86 03        ADD     A,(IX+$03)          
2A4F: DD 77 03        LD      (IX+$03),A          
2A52: C9              RET                         
2A53: DD 7E 05        LD      A,(IX+$05)          
2A56: EE 80           XOR     $80                 
2A58: DD 77 05        LD      (IX+$05),A          
2A5B: FD 7E 04        LD      A,(IY+$04)          
2A5E: FD 77 00        LD      (IY+$00),A          
2A61: FD 7E 01        LD      A,(IY+$01)          
2A64: EE 80           XOR     $80                 
2A66: FD 77 01        LD      (IY+$01),A          
2A69: C9              RET                         
2A6A: 3A B7 83        LD      A,($83B7)           
2A6D: FE 03           CP      $03                 
2A6F: D8              RET     C                   
2A70: 4F              LD      C,A                 
2A71: DD 35 0A        DEC     (IX+$0A)            
2A74: C0              RET     NZ                  
2A75: DD 7E 06        LD      A,(IX+$06)          
2A78: B7              OR      A                   
2A79: C0              RET     NZ                  
2A7A: CD EE 0A        CALL    $0AEE               ; {}
2A7D: 47              LD      B,A                 
2A7E: 79              LD      A,C                 
2A7F: 87              ADD     A,A                 
2A80: 87              ADD     A,A                 
2A81: 87              ADD     A,A                 
2A82: C6 80           ADD     $80                 
2A84: B8              CP      B                   
2A85: D8              RET     C                   
2A86: CD EE 0A        CALL    $0AEE               ; {}
2A89: E6 03           AND     $03                 
2A8B: 28 1D           JR      Z,$2AAA             ; {}
2A8D: 0E 40           LD      C,$40               
2A8F: 21 76 82        LD      HL,$8276            
2A92: 7E              LD      A,(HL)              
2A93: 0F              RRCA                        
2A94: 0F              RRCA                        
2A95: C6 24           ADD     $24                 
2A97: 57              LD      D,A                 
2A98: 2C              INC     L                   
2A99: 2C              INC     L                   
2A9A: 46              LD      B,(HL)              
2A9B: 3A 14 80        LD      A,($8014)           
2A9E: D6 10           SUB     $10                 
2AA0: 38 08           JR      C,$2AAA             ; {}
2AA2: 91              SUB     C                   
2AA3: 38 19           JR      C,$2ABE             ; {}
2AA5: 92              SUB     D                   
2AA6: 38 02           JR      C,$2AAA             ; {}
2AA8: 10 F8           DJNZ    $2AA2               ; {}
2AAA: DD 36 04 7E     LD      (IX+$04),$7E        
2AAE: CD EE 0A        CALL    $0AEE               ; {}
2AB1: 0F              RRCA                        
2AB2: 38 1E           JR      C,$2AD2             ; {}
2AB4: DD 36 05 00     LD      (IX+$05),$00        
2AB8: DD 36 03 F0     LD      (IX+$03),$F0        
2ABC: 18 1C           JR      $2ADA               ; {}
2ABE: 81              ADD     A,C                 
2ABF: 47              LD      B,A                 
2AC0: 3A 14 80        LD      A,($8014)           
2AC3: DD 77 02        LD      (IX+$02),A          
2AC6: 90              SUB     B                   
2AC7: DD 77 01        LD      (IX+$01),A          
2ACA: 81              ADD     A,C                 
2ACB: DD 77 00        LD      (IX+$00),A          
2ACE: DD 36 04 4E     LD      (IX+$04),$4E        
2AD2: DD 36 05 80     LD      (IX+$05),$80        
2AD6: DD 36 03 00     LD      (IX+$03),$00        
2ADA: DD 36 06 01     LD      (IX+$06),$01        
2ADE: DD 36 08 0B     LD      (IX+$08),$0B        
2AE2: DD 36 09 08     LD      (IX+$09),$08        
2AE6: 3A 71 83        LD      A,($8371)           
2AE9: B7              OR      A                   
2AEA: C0              RET     NZ                  
2AEB: 3C              INC     A                   
2AEC: 32 71 83        LD      ($8371),A           
2AEF: 3E 90           LD      A,$90               
2AF1: DF              RST     $18                 
2AF2: C9              RET                         
2AF3: DD 7E 06        LD      A,(IX+$06)          
2AF6: B7              OR      A                   
2AF7: C8              RET     Z                   
2AF8: CD E6 2A        CALL    $2AE6               ; {}
2AFB: DD 7E 04        LD      A,(IX+$04)          
2AFE: FE 60           CP      $60                 
2B00: 30 0C           JR      NC,$2B0E            ; {}
2B02: 3A 14 80        LD      A,($8014)           
2B05: DD 96 02        SUB     (IX+$02)            
2B08: 4F              LD      C,A                 
2B09: FD 77 00        LD      (IY+$00),A          
2B0C: 18 06           JR      $2B14               ; {}
2B0E: DD 4E 03        LD      C,(IX+$03)          
2B11: FD 71 00        LD      (IY+$00),C          
2B14: DD 7E 04        LD      A,(IX+$04)          
2B17: FD 77 03        LD      (IY+$03),A          
2B1A: FD 77 07        LD      (IY+$07),A          
2B1D: DD 7E 05        LD      A,(IX+$05)          
2B20: B7              OR      A                   
2B21: 20 0A           JR      NZ,$2B2D            ; {}
2B23: 3E 0F           LD      A,$0F               
2B25: 81              ADD     A,C                 
2B26: FD 77 04        LD      (IY+$04),A          
2B29: 3C              INC     A                   
2B2A: C0              RET     NZ                  
2B2B: 18 09           JR      $2B36               ; {}
2B2D: 3E F1           LD      A,$F1               
2B2F: 81              ADD     A,C                 
2B30: FD 77 04        LD      (IY+$04),A          
2B33: 79              LD      A,C                 
2B34: B7              OR      A                   
2B35: C0              RET     NZ                  
2B36: DD 7E 07        LD      A,(IX+$07)          
2B39: B7              OR      A                   
2B3A: C8              RET     Z                   
2B3B: DD E5           PUSH    IX                  
2B3D: E1              POP     HL                  
2B3E: 54              LD      D,H                 
2B3F: 5D              LD      E,L                 
2B40: 1C              INC     E                   
2B41: 01 0F 00        LD      BC,$000F            
2B44: 70              LD      (HL),B              
2B45: ED B0           LDIR                        
2B47: 01 07 00        LD      BC,$0007            
2B4A: FD E5           PUSH    IY                  
2B4C: E1              POP     HL                  
2B4D: 54              LD      D,H                 
2B4E: 5D              LD      E,L                 
2B4F: 1C              INC     E                   
2B50: 70              LD      (HL),B              
2B51: ED B0           LDIR                        
2B53: DD 36 0A 20     LD      (IX+$0A),$20        
2B57: C9              RET                         
2B58: DD 7E 06        LD      A,(IX+$06)          
2B5B: B7              OR      A                   
2B5C: C8              RET     Z                   
2B5D: DD 7E 04        LD      A,(IX+$04)          
2B60: C6 02           ADD     $02                 
2B62: 21 47 80        LD      HL,$8047            
2B65: BE              CP      (HL)                
2B66: C0              RET     NZ                  
2B67: DD 7E 05        LD      A,(IX+$05)          
2B6A: B7              OR      A                   
2B6B: FD 7E 00        LD      A,(IY+$00)          
2B6E: 21 44 80        LD      HL,$8044            
2B71: 28 02           JR      Z,$2B75             ; {}
2B73: C6 10           ADD     $10                 
2B75: 96              SUB     (HL)                
2B76: D8              RET     C                   
2B77: FE 10           CP      $10                 
2B79: D0              RET     NC                  
2B7A: 3E 01           LD      A,$01               
2B7C: 32 04 80        LD      ($8004),A           
2B7F: 32 2C 84        LD      ($842C),A           
2B82: C9              RET                         
2B83: CD 13 2C        CALL    $2C13               ; {}
2B86: CD AB 2B        CALL    $2BAB               ; {}
2B89: CD 93 2B        CALL    $2B93               ; {}
2B8C: CD A8 2C        CALL    $2CA8               ; {}
2B8F: CD FB 2B        CALL    $2BFB               ; {}
2B92: C9              RET                         
2B93: DD 7E 06        LD      A,(IX+$06)          
2B96: B7              OR      A                   
2B97: C8              RET     Z                   
2B98: DD 6E 0B        LD      L,(IX+$0B)          
2B9B: 26 80           LD      H,$80               
2B9D: 7E              LD      A,(HL)              
2B9E: DD 96 02        SUB     (IX+$02)            
2BA1: FD 77 00        LD      (IY+$00),A          
2BA4: DD 7E 04        LD      A,(IX+$04)          
2BA7: FD 77 03        LD      (IY+$03),A          
2BAA: C9              RET                         
2BAB: DD 7E 06        LD      A,(IX+$06)          
2BAE: B7              OR      A                   
2BAF: C8              RET     Z                   
2BB0: DD 35 09        DEC     (IX+$09)            
2BB3: C0              RET     NZ                  
2BB4: DD 36 09 08     LD      (IX+$09),$08        
2BB8: DD 6E 0B        LD      L,(IX+$0B)          
2BBB: 26 80           LD      H,$80               
2BBD: DD 7E 05        LD      A,(IX+$05)          
2BC0: B7              OR      A                   
2BC1: 28 0D           JR      Z,$2BD0             ; {}
2BC3: 7E              LD      A,(HL)              
2BC4: DD 96 00        SUB     (IX+$00)            
2BC7: FD BE 00        CP      (IY+$00)            
2BCA: 30 11           JR      NC,$2BDD            ; {}
2BCC: DD 34 02        INC     (IX+$02)            
2BCF: C9              RET                         
2BD0: 7E              LD      A,(HL)              
2BD1: DD 96 01        SUB     (IX+$01)            
2BD4: FD BE 00        CP      (IY+$00)            
2BD7: 38 04           JR      C,$2BDD             ; {}
2BD9: DD 35 02        DEC     (IX+$02)            
2BDC: C9              RET                         
2BDD: 3A 04 80        LD      A,($8004)           
2BE0: B7              OR      A                   
2BE1: C0              RET     NZ                  
2BE2: DD E5           PUSH    IX                  
2BE4: E1              POP     HL                  
2BE5: 54              LD      D,H                 
2BE6: 5D              LD      E,L                 
2BE7: 1C              INC     E                   
2BE8: 01 0F 00        LD      BC,$000F            
2BEB: 70              LD      (HL),B              
2BEC: ED B0           LDIR                        
2BEE: 21 58 80        LD      HL,$8058            
2BF1: 11 59 80        LD      DE,$8059            
2BF4: 01 03 00        LD      BC,$0003            
2BF7: 70              LD      (HL),B              
2BF8: ED B0           LDIR                        
2BFA: C9              RET                         
2BFB: DD 7E 06        LD      A,(IX+$06)          
2BFE: B7              OR      A                   
2BFF: C8              RET     Z                   
2C00: 21 D9 2C        LD      HL,$2CD9            
2C03: 4F              LD      C,A                 
2C04: 06 00           LD      B,$00               
2C06: 09              ADD     HL,BC               
2C07: 7E              LD      A,(HL)              
2C08: DD B6 05        OR      (IX+$05)            
2C0B: FD 77 01        LD      (IY+$01),A          
2C0E: FD 36 02 02     LD      (IY+$02),$02        
2C12: C9              RET                         
2C13: 3A B7 83        LD      A,($83B7)           
2C16: FE 03           CP      $03                 
2C18: D8              RET     C                   
2C19: 4F              LD      C,A                 
2C1A: DD 7E 06        LD      A,(IX+$06)          
2C1D: B7              OR      A                   
2C1E: C0              RET     NZ                  
2C1F: CD EE 0A        CALL    $0AEE               ; {}
2C22: 47              LD      B,A                 
2C23: 79              LD      A,C                 
2C24: 87              ADD     A,A                 
2C25: 87              ADD     A,A                 
2C26: 87              ADD     A,A                 
2C27: C6 80           ADD     $80                 
2C29: B8              CP      B                   
2C2A: D8              RET     C                   
2C2B: 0E 40           LD      C,$40               
2C2D: CD EE 0A        CALL    $0AEE               ; {}
2C30: E6 07           AND     $07                 
2C32: FE 05           CP      $05                 
2C34: D0              RET     NC                  
2C35: 4F              LD      C,A                 
2C36: 0F              RRCA                        
2C37: 0F              RRCA                        
2C38: 0F              RRCA                        
2C39: 0F              RRCA                        
2C3A: C6 30           ADD     $30                 
2C3C: DD 77 04        LD      (IX+$04),A          
2C3F: CD EE 0A        CALL    $0AEE               ; {}
2C42: 47              LD      B,A                 
2C43: 79              LD      A,C                 
2C44: 87              ADD     A,A                 
2C45: 5F              LD      E,A                 
2C46: 16 00           LD      D,$00               
2C48: 21 E6 2C        LD      HL,$2CE6            
2C4B: 19              ADD     HL,DE               
2C4C: 5E              LD      E,(HL)              
2C4D: 2C              INC     L                   
2C4E: 6E              LD      L,(HL)              
2C4F: 26 80           LD      H,$80               
2C51: DD 75 0B        LD      (IX+$0B),L          
2C54: 7E              LD      A,(HL)              
2C55: 57              LD      D,A                 
2C56: 79              LD      A,C                 
2C57: 87              ADD     A,A                 
2C58: 4F              LD      C,A                 
2C59: 06 00           LD      B,$00               
2C5B: 21 DC 2C        LD      HL,$2CDC            
2C5E: 09              ADD     HL,BC               
2C5F: 4E              LD      C,(HL)              
2C60: 2C              INC     L                   
2C61: 66              LD      H,(HL)              
2C62: 69              LD      L,C                 
2C63: 7E              LD      A,(HL)              
2C64: 0F              RRCA                        
2C65: 0F              RRCA                        
2C66: D6 10           SUB     $10                 
2C68: 4F              LD      C,A                 
2C69: 2C              INC     L                   
2C6A: 2C              INC     L                   
2C6B: 46              LD      B,(HL)              
2C6C: 7A              LD      A,D                 
2C6D: 93              SUB     E                   
2C6E: D8              RET     C                   
2C6F: 91              SUB     C                   
2C70: 38 02           JR      C,$2C74             ; {}
2C72: 10 F9           DJNZ    $2C6D               ; {}
2C74: 81              ADD     A,C                 
2C75: 47              LD      B,A                 
2C76: DD 6E 0B        LD      L,(IX+$0B)          
2C79: 26 80           LD      H,$80               
2C7B: 7E              LD      A,(HL)              
2C7C: DD 77 02        LD      (IX+$02),A          
2C7F: 90              SUB     B                   
2C80: DD 77 01        LD      (IX+$01),A          
2C83: 81              ADD     A,C                 
2C84: DD 77 00        LD      (IX+$00),A          
2C87: CD EE 0A        CALL    $0AEE               ; {}
2C8A: 0F              RRCA                        
2C8B: 38 0A           JR      C,$2C97             ; {}
2C8D: DD 36 05 80     LD      (IX+$05),$80        
2C91: DD 36 03 F0     LD      (IX+$03),$F0        
2C95: 18 08           JR      $2C9F               ; {}
2C97: DD 36 05 00     LD      (IX+$05),$00        
2C9B: DD 36 03 00     LD      (IX+$03),$00        
2C9F: DD 36 06 01     LD      (IX+$06),$01        
2CA3: DD 36 09 08     LD      (IX+$09),$08        
2CA7: C9              RET                         
2CA8: DD 7E 06        LD      A,(IX+$06)          
2CAB: B7              OR      A                   
2CAC: C8              RET     Z                   
2CAD: DD 7E 04        LD      A,(IX+$04)          
2CB0: 21 47 80        LD      HL,$8047            
2CB3: BE              CP      (HL)                
2CB4: C0              RET     NZ                  
2CB5: DD 7E 05        LD      A,(IX+$05)          
2CB8: B7              OR      A                   
2CB9: FD 7E 00        LD      A,(IY+$00)          
2CBC: 21 44 80        LD      HL,$8044            
2CBF: 20 04           JR      NZ,$2CC5            ; {}
2CC1: C6 14           ADD     $14                 
2CC3: 18 02           JR      $2CC7               ; {}
2CC5: D6 04           SUB     $04                 
2CC7: 96              SUB     (HL)                
2CC8: D8              RET     C                   
2CC9: FE 10           CP      $10                 
2CCB: D0              RET     NC                  
2CCC: 3E 01           LD      A,$01               
2CCE: 32 04 80        LD      ($8004),A           
2CD1: DD 36 06 02     LD      (IX+$06),$02        
2CD5: C9              RET                         
2CD6: 2C              INC     L                   
2CD7: 2E 30           LD      L,$30               
2CD9: 2E 27           LD      L,$27               
2CDB: 38 70           JR      C,$2D4D             ; {}
2CDD: 82              ADD     A,D                 
2CDE: 73              LD      (HL),E              
2CDF: 82              ADD     A,D                 
2CE0: 76              HALT                        
2CE1: 82              ADD     A,D                 
2CE2: 79              LD      A,C                 
2CE3: 82              ADD     A,D                 
2CE4: 7C              LD      A,H                 
2CE5: 82              ADD     A,D                 
2CE6: 50              LD      D,B                 
2CE7: 0C              INC     C                   
2CE8: 30 10           JR      NC,$2CFA            ; {}
2CEA: 70              LD      (HL),B              
2CEB: 14              INC     D                   
2CEC: 40              LD      B,B                 
2CED: 18 40           JR      $2D2F               ; {}
2CEF: 1C              INC     E                   
2CF0: 21 E2 83        LD      HL,$83E2            
2CF3: 7E              LD      A,(HL)              
2CF4: B7              OR      A                   
2CF5: 3A 00 E0        LD      A,($E000)           ; {hard.PPI8255+2000}
2CF8: 2F              CPL                         
2CF9: 20 04           JR      NZ,$2CFF            ; {}
2CFB: E6 C4           AND     $C4                 
2CFD: 77              LD      (HL),A              
2CFE: C9              RET                         
2CFF: E6 C4           AND     $C4                 
2D01: C0              RET     NZ                  
2D02: 3C              INC     A                   
2D03: CD 94 07        CALL    $0794               ; {}
2D06: AF              XOR     A                   
2D07: ED 5B D4 83     LD      DE,($83D4)          
2D0B: CB 76           BIT     6,(HL)              
2D0D: C2 2B 2D        JP      NZ,$2D2B            ; {}
2D10: CB 56           BIT     2,(HL)              
2D12: 77              LD      (HL),A              
2D13: 20 09           JR      NZ,$2D1E            ; {}
2D15: 3C              INC     A                   
2D16: 32 18 B8        LD      ($B818),A           ; {hard.COINCNT0}
2D19: 3E 04           LD      A,$04               
2D1B: 32 7E 83        LD      ($837E),A           
2D1E: 21 23 2D        LD      HL,$2D23            
2D21: 19              ADD     HL,DE               
2D22: E9              JP      (HL)                
2D23: 18 24           JR      $2D49               ; {}
2D25: 18 1B           JR      $2D42               ; {}
2D27: 18 19           JR      $2D42               ; {}
2D29: 18 1E           JR      $2D49               ; {}
2D2B: 77              LD      (HL),A              
2D2C: 3C              INC     A                   
2D2D: 32 1C B8        LD      ($B81C),A           ; {hard.COINCNT1}
2D30: 3E 04           LD      A,$04               
2D32: 32 7F 83        LD      ($837F),A           
2D35: 21 3A 2D        LD      HL,$2D3A            
2D38: 19              ADD     HL,DE               
2D39: E9              JP      (HL)                
2D3A: 18 0D           JR      $2D49               ; {}
2D3C: 18 04           JR      $2D42               ; {}
2D3E: 18 11           JR      $2D51               ; {}
2D40: 18 13           JR      $2D55               ; {}
2D42: 21 E3 83        LD      HL,$83E3            
2D45: 34              INC     (HL)                
2D46: CB 46           BIT     0,(HL)              
2D48: C0              RET     NZ                  
2D49: 0E 01           LD      C,$01               
2D4B: 18 0A           JR      $2D57               ; {}
2D4D: 0E 02           LD      C,$02               
2D4F: 18 06           JR      $2D57               ; {}
2D51: 0E 03           LD      C,$03               
2D53: 18 02           JR      $2D57               ; {}
2D55: 0E 06           LD      C,$06               
2D57: 3A E1 83        LD      A,($83E1)           
2D5A: 81              ADD     A,C                 
2D5B: 27              DAA                         
2D5C: 30 02           JR      NC,$2D60            ; {}
2D5E: 3E 99           LD      A,$99               
2D60: 32 E1 83        LD      ($83E1),A           
2D63: 3A FE 83        LD      A,($83FE)           
2D66: B7              OR      A                   
2D67: C0              RET     NZ                  
2D68: 3A D6 83        LD      A,($83D6)           
2D6B: FE 05           CP      $05                 
2D6D: CC B9 0D        CALL    Z,$0DB9             ; {}
2D70: 3E 05           LD      A,$05               
2D72: 32 D6 83        LD      ($83D6),A           
2D75: AF              XOR     A                   
2D76: 32 D8 83        LD      ($83D8),A           
2D79: 21 40 80        LD      HL,$8040            
2D7C: 11 41 80        LD      DE,$8041            
2D7F: 01 1F 00        LD      BC,$001F            
2D82: 70              LD      (HL),B              
2D83: ED B0           LDIR                        
2D85: C3 67 0B        JP      $0B67               ; {}
2D88: 21 D8 83        LD      HL,$83D8            
2D8B: 36 FF           LD      (HL),$FF            
2D8D: CD 66 07        CALL    $0766               ; {}
2D90: AF              XOR     A                   
2D91: 32 9B 82        LD      ($829B),A           
2D94: 32 21 80        LD      ($8021),A           
2D97: 3E 05           LD      A,$05               
2D99: 32 1B 80        LD      ($801B),A           
2D9C: 3E 03           LD      A,$03               
2D9E: 32 2B 80        LD      ($802B),A           
2DA1: 11 5C 2F        LD      DE,$2F5C            
2DA4: 21 8D AA        LD      HL,$AA8D            
2DA7: 06 0B           LD      B,$0B               
2DA9: EF              RST     $28                 
2DAA: 3A E4 83        LD      A,($83E4)           
2DAD: FE 0A           CP      $0A                 
2DAF: D0              RET     NC                  
2DB0: 21 15 AB        LD      HL,$AB15            
2DB3: CD A9 0B        CALL    $0BA9               ; {}
2DB6: 11 AE 2F        LD      DE,$2FAE            
2DB9: 06 07           LD      B,$07               
2DBB: EF              RST     $28                 
2DBC: 11 73 2F        LD      DE,$2F73            
2DBF: 06 04           LD      B,$04               
2DC1: EF              RST     $28                 
2DC2: 11 92 2F        LD      DE,$2F92            
2DC5: 06 07           LD      B,$07               
2DC7: EF              RST     $28                 
2DC8: C9              RET                         
2DC9: FF              RST     $38                 
2DCA: FF              RST     $38                 
2DCB: FF              RST     $38                 
2DCC: FF              RST     $38                 
2DCD: FF              RST     $38                 
2DCE: FF              RST     $38                 
2DCF: FF              RST     $38                 
2DD0: FF              RST     $38                 
2DD1: FF              RST     $38                 
2DD2: FF              RST     $38                 
2DD3: FF              RST     $38                 
2DD4: FF              RST     $38                 
2DD5: FF              RST     $38                 
2DD6: FF              RST     $38                 
2DD7: FF              RST     $38                 
2DD8: FF              RST     $38                 
2DD9: FF              RST     $38                 
2DDA: FF              RST     $38                 
2DDB: FF              RST     $38                 
2DDC: FF              RST     $38                 
2DDD: FF              RST     $38                 
2DDE: FF              RST     $38                 
2DDF: FF              RST     $38                 
2DE0: FF              RST     $38                 
2DE1: FF              RST     $38                 
2DE2: FF              RST     $38                 
2DE3: FF              RST     $38                 
2DE4: FF              RST     $38                 
2DE5: FF              RST     $38                 
2DE6: FF              RST     $38                 
2DE7: FF              RST     $38                 
2DE8: FF              RST     $38                 
2DE9: FF              RST     $38                 
2DEA: FF              RST     $38                 
2DEB: FF              RST     $38                 
2DEC: FF              RST     $38                 
2DED: FF              RST     $38                 
2DEE: FF              RST     $38                 
2DEF: FF              RST     $38                 
2DF0: FF              RST     $38                 
2DF1: FF              RST     $38                 
2DF2: FF              RST     $38                 
2DF3: FF              RST     $38                 
2DF4: FF              RST     $38                 
2DF5: FF              RST     $38                 
2DF6: FF              RST     $38                 
2DF7: FF              RST     $38                 
2DF8: FF              RST     $38                 
2DF9: FF              RST     $38                 
2DFA: FF              RST     $38                 
2DFB: FF              RST     $38                 
2DFC: FF              RST     $38                 
2DFD: FF              RST     $38                 
2DFE: FF              RST     $38                 
2DFF: FF              RST     $38                 
2E00: 03              INC     BC                  
2E01: 05              DEC     B                   
2E02: 07              RLCA                        
2E03: FF              RST     $38                 
2E04: 00              NOP                         
2E05: 02              LD      (BC),A              
2E06: 04              INC     B                   
2E07: 06 00           LD      B,$00               
2E09: 20 00           JR      NZ,$2E0B            ; {}
2E0B: 00              NOP                         
2E0C: 58              LD      E,B                 
2E0D: 01 63 04        LD      BC,$0463            
2E10: 63              LD      H,E                 
2E11: 04              INC     B                   
2E12: 05              DEC     B                   
2E13: 02              LD      (BC),A              
2E14: 97              SUB     A                   
2E15: 01 58 01        LD      BC,$0158            
2E18: 27              DAA                         
2E19: 01 05 00        LD      BC,$0005            
2E1C: 1F              RRA                         
2E1D: 20 21           JR      NZ,$2E40            ; {}
2E1F: 20 25           JR      NZ,$2E46            ; {}
2E21: 26 27           LD      H,$27               
2E23: 26 2C           LD      H,$2C               
2E25: 2D              DEC     L                   
2E26: 2E 2D           LD      L,$2D               
2E28: 2F              CPL                         
2E29: 30 31           JR      NC,$2E5C            ; {}
2E2B: 30 2C           JR      NC,$2E59            ; {}
2E2D: 2E 30           LD      L,$30               
2E2F: 2E 2D           LD      L,$2D               
2E31: 2F              CPL                         
2E32: 31 2F 25        LD      SP,$252F            
2E35: 26 27           LD      H,$27               
2E37: 2C              INC     L                   
2E38: 2D              DEC     L                   
2E39: 2E 2F           LD      L,$2F               
2E3B: 30 31           JR      NC,$2E6E            ; {}
2E3D: 2C              INC     L                   
2E3E: 2E 30           LD      L,$30               
2E40: 2D              DEC     L                   
2E41: 2F              CPL                         
2E42: 31 04 04        LD      SP,$0404            
2E45: 04              INC     B                   
2E46: 08              EX      AF,AF'              
2E47: 08              EX      AF,AF'              
2E48: 08              EX      AF,AF'              
2E49: 08              EX      AF,AF'              
2E4A: 08              EX      AF,AF'              
2E4B: 08              EX      AF,AF'              
2E4C: 10 10           DJNZ    $2E5E               ; {}
2E4E: 10 02           DJNZ    $2E52               ; {}
2E50: 03              INC     BC                  
2E51: 03              INC     BC                  
2E52: 05              DEC     B                   
2E53: 05              DEC     B                   
2E54: 06 08           LD      B,$08               
2E56: 09              ADD     HL,BC               
2E57: 54              LD      D,H                 
2E58: 58              LD      E,B                 
2E59: 5A              LD      E,D                 
2E5A: 5E              LD      E,(HL)              
2E5B: 56              LD      D,(HL)              
2E5C: 5C              LD      E,H                 
2E5D: 03              INC     BC                  
2E5E: 03              INC     BC                  
2E5F: 06 08           LD      B,$08               
2E61: 10 18           DJNZ    $2E7B               ; {}
2E63: 30 50           JR      NC,$2EB5            ; {}
2E65: 60              LD      H,B                 
2E66: 80              ADD     A,B                 
2E67: C0              RET     NZ                  
2E68: E0              RET     PO                  
2E69: 05              DEC     B                   
2E6A: 02              LD      (BC),A              
2E6B: 02              LD      (BC),A              
2E6C: 02              LD      (BC),A              
2E6D: 08              EX      AF,AF'              
2E6E: 08              EX      AF,AF'              
2E6F: 05              DEC     B                   
2E70: 08              EX      AF,AF'              
2E71: 02              LD      (BC),A              
2E72: 08              EX      AF,AF'              
2E73: 08              EX      AF,AF'              
2E74: 08              EX      AF,AF'              
2E75: 0E 08           LD      C,$08               
2E77: 08              EX      AF,AF'              
2E78: 0E 08           LD      C,$08               
2E7A: 0E 08           LD      C,$08               
2E7C: 0E 08           LD      C,$08               
2E7E: 0E 08           LD      C,$08               
2E80: 05              DEC     B                   
2E81: 05              DEC     B                   
2E82: 08              EX      AF,AF'              
2E83: 05              DEC     B                   
2E84: 02              LD      (BC),A              
2E85: 0B              DEC     BC                  
2E86: 05              DEC     B                   
2E87: 08              EX      AF,AF'              
2E88: FF              RST     $38                 
2E89: C0              RET     NZ                  
2E8A: 02              LD      (BC),A              
2E8B: 00              NOP                         
2E8C: 03              INC     BC                  
2E8D: 00              NOP                         
2E8E: 03              INC     BC                  
2E8F: 80              ADD     A,B                 
2E90: 01 80 02        LD      BC,$0280            
2E93: 80              ADD     A,B                 
2E94: 02              LD      (BC),A              
2E95: 00              NOP                         
2E96: 02              LD      (BC),A              
2E97: 00              NOP                         
2E98: 02              LD      (BC),A              
2E99: 80              ADD     A,B                 
2E9A: 03              INC     BC                  
2E9B: E0              RET     PO                  
2E9C: 02              LD      (BC),A              
2E9D: 20 02           JR      NZ,$2EA1            ; {}
2E9F: 20 02           JR      NZ,$2EA3            ; {}
2EA1: 20 02           JR      NZ,$2EA5            ; {}
2EA3: 00              NOP                         
2EA4: 03              INC     BC                  
2EA5: 80              ADD     A,B                 
2EA6: 02              LD      (BC),A              
2EA7: C0              RET     NZ                  
2EA8: 02              LD      (BC),A              
2EA9: C0              RET     NZ                  
2EAA: 02              LD      (BC),A              
2EAB: 80              ADD     A,B                 
2EAC: 03              INC     BC                  
2EAD: 20 02           JR      NZ,$2EB1            ; {}
2EAF: 20 02           JR      NZ,$2EB3            ; {}
2EB1: 10 39           DJNZ    $2EEC               ; {}
2EB3: 40              LD      B,B                 
2EB4: D7              RST     $10                 
2EB5: A7              AND     A                   
2EB6: 0F              RRCA                        
2EB7: 3C              INC     A                   
2EB8: 36 10           LD      (HL),$10            
2EBA: 39              ADD     HL,SP               
2EBB: 40              LD      B,B                 
2EBC: D7              RST     $10                 
2EBD: A7              AND     A                   
2EBE: 0F              RRCA                        
2EBF: 3C              INC     A                   
2EC0: 36 10           LD      (HL),$10            
2EC2: 39              ADD     HL,SP               
2EC3: 40              LD      B,B                 
2EC4: D7              RST     $10                 
2EC5: A7              AND     A                   
2EC6: 0F              RRCA                        
2EC7: 3C              INC     A                   
2EC8: 36 10           LD      (HL),$10            
2ECA: 39              ADD     HL,SP               
2ECB: 40              LD      B,B                 
2ECC: D7              RST     $10                 
2ECD: A7              AND     A                   
2ECE: 0F              RRCA                        
2ECF: 3C              INC     A                   
2ED0: 36 10           LD      (HL),$10            
2ED2: 16 1F           LD      D,$1F               
2ED4: 22 10 15        LD      ($1510),HL          ; {}
2ED7: 11 13 18        LD      DE,$1813            
2EDA: 10 23           DJNZ    $2EFF               ; {}
2EDC: 24              INC     H                   
2EDD: 15              DEC     D                   
2EDE: 20 2B           JR      NZ,$2F0B            ; {}
2EE0: 25              DEC     H                   
2EE1: 20 18           JR      NZ,$2EFB            ; {}
2EE3: 19              ADD     HL,DE               
2EE4: 2B              DEC     HL                  
2EE5: 23              INC     HL                  
2EE6: 13              INC     DE                  
2EE7: 1F              RRA                         
2EE8: 22 15 10        LD      ($1015),HL          ; {}
2EEB: 22 11 1E        LD      ($1E11),HL          ; {}
2EEE: 1B              DEC     DE                  
2EEF: 19              ADD     HL,DE               
2EF0: 1E 17           LD      E,$17               
2EF2: 10 23           DJNZ    $2F17               ; {}
2EF4: 24              INC     H                   
2EF5: 10 1E           DJNZ    $2F15               ; {}
2EF7: 14              INC     D                   
2EF8: 10 22           DJNZ    $2F1C               ; {}
2EFA: 14              INC     D                   
2EFB: 10 24           DJNZ    $2F21               ; {}
2EFD: 18 10           JR      $2F0F               ; {}
2EFF: 24              INC     H                   
2F00: 18 2B           JR      $2F2D               ; {}
2F02: 20 1F           JR      NZ,$2F23            ; {}
2F04: 19              ADD     HL,DE               
2F05: 1E 24           LD      E,$24               
2F07: 10 24           DJNZ    $2F2D               ; {}
2F09: 11 12 1C        LD      DE,$1C12            
2F0C: 15              DEC     D                   
2F0D: 2B              DEC     HL                  
2F0E: 17              RLA                         
2F0F: 11 1D 15        LD      DE,$151D            
2F12: 10 1F           DJNZ    $2F33               ; {}
2F14: 26 15           LD      H,$15               
2F16: 22 11 22        LD      ($2211),HL          ; {}
2F19: 22 19 26        LD      ($2619),HL          ; {}
2F1C: 15              DEC     D                   
2F1D: 14              INC     D                   
2F1E: 10 18           DJNZ    $2F38               ; {}
2F20: 1F              RRA                         
2F21: 1D              DEC     E                   
2F22: 15              DEC     D                   
2F23: 10 23           DJNZ    $2F48               ; {}
2F25: 11 16 15        LD      DE,$1516            
2F28: 1C              INC     E                   
2F29: 29              ADD     HL,HL               
2F2A: 19              ADD     HL,DE               
2F2B: 1E 24           LD      E,$24               
2F2D: 1F              RRA                         
2F2E: 10 16           DJNZ    $2F46               ; {}
2F30: 19              ADD     HL,DE               
2F31: 29              ADD     HL,HL               
2F32: 15              DEC     D                   
2F33: 10 18           DJNZ    $2F4D               ; {}
2F35: 1F              RRA                         
2F36: 1D              DEC     E                   
2F37: 15              DEC     D                   
2F38: 23              INC     HL                  
2F39: 10 12           DJNZ    $2F4D               ; {}
2F3B: 29              ADD     HL,HL               
2F3C: 10 23           DJNZ    $2F61               ; {}
2F3E: 11 26 19        LD      DE,$1926            
2F41: 1E 17           LD      E,$17               
2F43: 10 16           DJNZ    $2F5B               ; {}
2F45: 1F              RRA                         
2F46: 22 10 15        LD      ($1510),HL          ; {}
2F49: 26 15           LD      H,$15               
2F4B: 22 29 1B        LD      ($1B29),HL          ; {}
2F4E: 1F              RRA                         
2F4F: 1E 11           LD      E,$11               
2F51: 1D              DEC     E                   
2F52: 19              ADD     HL,DE               
2F53: 10 10           DJNZ    $2F65               ; {}
2F55: 4E              LD      C,(HL)              
2F56: 10 10           DJNZ    $2F68               ; {}
2F58: 01 09 08        LD      BC,$0809            
2F5B: 01 19 1E        LD      BC,$1E19            
2F5E: 23              INC     HL                  
2F5F: 15              DEC     D                   
2F60: 22 24 10        LD      ($1024),HL          ; {}
2F63: 13              INC     DE                  
2F64: 1F              RRA                         
2F65: 19              ADD     HL,DE               
2F66: 1E 23           LD      E,$23               
2F68: 13              INC     DE                  
2F69: 22 15 14        LD      ($1415),HL          ; {}
2F6C: 19              ADD     HL,DE               
2F6D: 24              INC     H                   
2F6E: 24              INC     H                   
2F6F: 19              ADD     HL,DE               
2F70: 1D              DEC     E                   
2F71: 15              DEC     D                   
2F72: 10 10           DJNZ    $2F84               ; {}
2F74: 20 15           JR      NZ,$2F8B            ; {}
2F76: 22 20 25        LD      ($2520),HL          ; {}
2F79: 23              INC     HL                  
2F7A: 18 10           JR      $2F8C               ; {}
2F7C: 23              INC     HL                  
2F7D: 24              INC     H                   
2F7E: 11 22 24        LD      DE,$2422            
2F81: 10 12           DJNZ    $2F95               ; {}
2F83: 25              DEC     H                   
2F84: 24              INC     H                   
2F85: 24              INC     H                   
2F86: 1F              RRA                         
2F87: 1E 1F           LD      E,$1F               
2F89: 1E 15           LD      E,$15               
2F8B: 10 1F           DJNZ    $2FAC               ; {}
2F8D: 22 10 24        LD      ($2410),HL          ; {}
2F90: 27              DAA                         
2F91: 1F              RRA                         
2F92: 10 20           DJNZ    $2FB4               ; {}
2F94: 1C              INC     E                   
2F95: 11 29 15        LD      DE,$1529            
2F98: 22 10 1F        LD      ($1F10),HL          ; {}
2F9B: 1E 1C           LD      E,$1C               
2F9D: 29              ADD     HL,HL               
2F9E: 20 1C           JR      NZ,$2FBC            ; {}
2FA0: 25              DEC     H                   
2FA1: 23              INC     HL                  
2FA2: 10 12           DJNZ    $2FB6               ; {}
2FA4: 1F              RRA                         
2FA5: 1E 25           LD      E,$25               
2FA7: 23              INC     HL                  
2FA8: 10 15           DJNZ    $2FBF               ; {}
2FAA: 28 24           JR      Z,$2FD0             ; {}
2FAC: 22 11 10        LD      ($1011),HL          ; {}
2FAF: 16 22           LD      D,$22               
2FB1: 1F              RRA                         
2FB2: 17              RLA                         
2FB3: 23              INC     HL                  
2FB4: 10 11           DJNZ    $2FC7               ; {}
2FB6: 16 24           LD      D,$24               
2FB8: 15              DEC     D                   
2FB9: 22 10 20        LD      ($2010),HL          ; {}
2FBC: 24              INC     H                   
2FBD: 23              INC     HL                  
2FBE: 10 28           DJNZ    $2FE8               ; {}
2FC0: 10 22           DJNZ    $2FE4               ; {}
2FC2: 15              DEC     D                   
2FC3: 1D              DEC     E                   
2FC4: 11 19 1E        LD      DE,$1E19            
2FC7: 19              ADD     HL,DE               
2FC8: 1E 17           LD      E,$17               
2FCA: 10 23           DJNZ    $2FEF               ; {}
2FCC: 15              DEC     D                   
2FCD: 13              INC     DE                  
2FCE: 1F              RRA                         
2FCF: 1E 14           LD      E,$14               
      
2FD1: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF     
2FE1: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF          
2FF1: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF        
```

