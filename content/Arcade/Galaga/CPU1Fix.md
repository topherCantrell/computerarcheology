![CPU1 Fix](Galaga.jpg)

#CPU1 Official Fix

>>> cpu Z80

>>> binary 0000:roms/CPU1FIX.bin

```code
; 3N + 3M + 3L + 3K

; This is the patched ROM for CPU1 released for the Arcade.

0000: 3E 10           LD      A,$10               
0002: 32 00 71        LD      ($7100),A           
0005: C3 C4 02        JP      $02C4               ; {}
0008: 87              ADD     A,A                 
0009: 30 05           JR      NC,$10              ; {}
000B: 24              INC     H                   
000C: C3 10 00        JP      $0010               ; {}
000F: FF              RST     0X38                
0010: 85              ADD     A,L                 
0011: 6F              LD      L,A                 
0012: D0              RET     NC                  
0013: 24              INC     H                   
0014: C9              RET                         
0015: FF              RST     0X38                
0016: FF              RST     0X38                
0017: FF              RST     0X38                
0018: 77              LD      (HL),A              
0019: 23              INC     HL                  
001A: 10 FC           DJNZ    $18                 ; {}
001C: C9              RET                         
001D: FF              RST     0X38                
001E: FF              RST     0X38                
001F: FF              RST     0X38                
0020: 7B              LD      A,E                 
0021: D6 20           SUB     $20                 
0023: 5F              LD      E,A                 
0024: D0              RET     NC                  
0025: 15              DEC     D                   
0026: C9              RET                         
0027: FF              RST     0X38                
0028: 21 00 91        LD      HL,$9100            
002B: 06 F0           LD      B,$F0               
002D: AF              XOR     A                   
002E: DF              RST     0X18                
002F: C9              RET                         
0030: 37              SCF                         
0031: 08              EX      AF,AF'              
0032: C3 B5 13        JP      $13B5               ; {}
0035: FF              RST     0X38                
0036: FF              RST     0X38                
0037: FF              RST     0X38                
0038: C3 37 02        JP      $0237               ; {}
003B: E9              JP      (HL)                
003C: 21 00 93        LD      HL,$9300            
003F: 06 80           LD      B,$80               
0041: AF              XOR     A                   
0042: DF              RST     0X18                
0043: 21 00 9B        LD      HL,$9B00            
0046: 06 80           LD      B,$80               
0048: DF              RST     0X18                
0049: 21 00 88        LD      HL,$8800            
004C: 3E 80           LD      A,$80               
004E: 06 80           LD      B,$80               
0050: DF              RST     0X18                
0051: C9              RET                         
0052: FF              RST     0X38                
0053: FF              RST     0X38                
0054: FF              RST     0X38                
0055: FF              RST     0X38                
0056: FF              RST     0X38                
0057: FF              RST     0X38                
0058: FF              RST     0X38                
0059: FF              RST     0X38                
005A: FF              RST     0X38                
005B: FF              RST     0X38                
005C: FF              RST     0X38                
005D: FF              RST     0X38                
005E: FF              RST     0X38                
005F: FF              RST     0X38                
0060: FF              RST     0X38                
0061: FF              RST     0X38                
0062: FF              RST     0X38                
0063: FF              RST     0X38                
0064: FF              RST     0X38                
0065: FF              RST     0X38                
0066: D9              EXX                         
0067: ED A0           LDI                         
0069: EA 8F 00        JP      PE,$008F            ; {}
006C: F5              PUSH    AF                  
006D: 21 00 71        LD      HL,$7100            
0070: 36 10           LD      (HL),$10            
0072: 3A B9 9A        LD      A,($9AB9)           
0075: A7              AND     A                   
0076: 28 16           JR      Z,$8E               ; {}
0078: AF              XOR     A                   
0079: 32 B9 9A        LD      ($9AB9),A           
007C: 21 92 00        LD      HL,$0092            
007F: 11 00 70        LD      DE,$7000            
0082: 01 04 00        LD      BC,$0004            
0085: D9              EXX                         
0086: 3E A8           LD      A,$A8               
0088: 32 00 71        LD      ($7100),A           
008B: F1              POP     AF                  
008C: ED 45           RETN                        
008E: F1              POP     AF                  
008F: D9              EXX                         
0090: ED 45           RETN                        
0092: 10 10           DJNZ    $A4                 ; {}
0094: 20 20           JR      NZ,$B6              ; {}
0096: 27              DAA                         
0097: 08              EX      AF,AF'              
0098: 28 08           JR      Z,$A2               ; {}
009A: B2              OR      D                   
009B: 17              RLA                         
009C: 00              NOP                         
009D: 17              RLA                         
009E: 86              ADD     A,(HL)              
009F: 1A              LD      A,(DE)              
00A0: 57              LD      D,A                 
00A1: 08              EX      AF,AF'              
00A2: 27              DAA                         
00A3: 08              EX      AF,AF'              
00A4: 27              DAA                         
00A5: 08              EX      AF,AF'              
00A6: 24              INC     H                   
00A7: 29              ADD     HL,HL               
00A8: EC 1D 9E        CALL    PE,$9E1D            
00AB: 2A B9 1D        LD      HL,($1DB9)          ; {}
00AE: EB              EX      DE,HL               
00AF: 23              INC     HL                  
00B0: AA              XOR     D                   
00B1: 1E 38           LD      E,$38               
00B3: 1D              DEC     E                   
00B4: 35              DEC     (HL)                
00B5: 09              ADD     HL,BC               
00B6: 6B              LD      L,E                 
00B7: 1B              DEC     DE                  
00B8: B2              OR      D                   
00B9: 19              ADD     HL,DE               
00BA: 7C              LD      A,H                 
00BB: 1D              DEC     E                   
00BC: 27              DAA                         
00BD: 08              EX      AF,AF'              
00BE: 8F              ADC     A,A                 
00BF: 1F              RRA                         
00C0: 0E 1F           LD      C,$1F               
00C2: 27              DAA                         
00C3: 08              EX      AF,AF'              
00C4: D8              RET     C                   
00C5: 1D              DEC     E                   
00C6: 30 22           JR      NC,$EA              ; {}
00C8: D9              EXX                         
00C9: 21 27 08        LD      HL,$0827            
00CC: 27              DAA                         
00CD: 08              EX      AF,AF'              
00CE: F2 20 00        JP      P,$0020             ; {}
00D1: 20 27           JR      NZ,$FA              ; {}
00D3: 08              EX      AF,AF'              
00D4: 77              LD      (HL),A              
00D5: 09              ADD     HL,BC               
00D6: 11 ED 83        LD      DE,$83ED            
00D9: 21 B9 02        LD      HL,$02B9            
00DC: 01 05 00        LD      BC,$0005            
00DF: ED B0           LDIR                        
00E1: 1E CB           LD      E,$CB               
00E3: 21 EB 00        LD      HL,$00EB            
00E6: 0E 11           LD      C,$11               
00E8: ED B0           LDIR                        
00EA: C9              RET                         
00EB: 0E 1B           LD      C,$1B               
00ED: 18 0C           JR      $FB                 ; {}
00EF: 1C              INC     E                   
00F0: 24              INC     H                   
00F1: 11 10 12        LD      DE,$1210            
00F4: 11 24 24        LD      DE,$2424            
00F7: 24              INC     H                   
00F8: 24              INC     H                   
00F9: 19              ADD     HL,DE               
00FA: 1E 01           LD      E,$01               
00FC: FF              RST     0X38                
00FD: FF              RST     0X38                
00FE: FF              RST     0X38                
00FF: FF              RST     0X38                
0100: 14              INC     D                   
0101: 06 14           LD      B,$14               
0103: 0C              INC     C                   
0104: 14              INC     D                   
0105: 08              EX      AF,AF'              
0106: 14              INC     D                   
0107: 0A              LD      A,(BC)              
0108: 1C              INC     E                   
0109: 00              NOP                         
010A: 1C              INC     E                   
010B: 12              LD      (DE),A              
010C: 1E 00           LD      E,$00               
010E: 1E 12           LD      E,$12               
0110: 1C              INC     E                   
0111: 02              LD      (BC),A              
0112: 1C              INC     E                   
0113: 10 1E           DJNZ    $133                ; {}
0115: 02              LD      (BC),A              
0116: 1E 10           LD      E,$10               
0118: 1C              INC     E                   
0119: 04              INC     B                   
011A: 1C              INC     E                   
011B: 0E 1E           LD      C,$1E               
011D: 04              INC     B                   
011E: 1E 0E           LD      E,$0E               
0120: 1C              INC     E                   
0121: 06 1C           LD      B,$1C               
0123: 0C              INC     C                   
0124: 1E 06           LD      E,$06               
0126: 1E 0C           LD      E,$0C               
0128: 1C              INC     E                   
0129: 08              EX      AF,AF'              
012A: 1C              INC     E                   
012B: 0A              LD      A,(BC)              
012C: 1E 08           LD      E,$08               
012E: 1E 0A           LD      E,$0A               
0130: 16 06           LD      D,$06               
0132: 16 0C           LD      D,$0C               
0134: 16 08           LD      D,$08               
0136: 16 0A           LD      D,$0A               
0138: 18 00           JR      $13A                ; {}
013A: 18 12           JR      $14E                ; {}
013C: 1A              LD      A,(DE)              
013D: 00              NOP                         
013E: 1A              LD      A,(DE)              
013F: 12              LD      (DE),A              
0140: 18 02           JR      $144                ; {}
0142: 18 10           JR      $154                ; {}
0144: 1A              LD      A,(DE)              
0145: 02              LD      (BC),A              
0146: 1A              LD      A,(DE)              
0147: 10 18           DJNZ    $161                ; {}
0149: 04              INC     B                   
014A: 18 0E           JR      $15A                ; {}
014C: 1A              LD      A,(DE)              
014D: 04              INC     B                   
014E: 1A              LD      A,(DE)              
014F: 0E 18           LD      C,$18               
0151: 06 18           LD      B,$18               
0153: 0C              INC     C                   
0154: 1A              LD      A,(DE)              
0155: 06 1A           LD      B,$1A               
0157: 0C              INC     C                   
0158: 18 08           JR      $162                ; {}
015A: 18 0A           JR      $166                ; {}
015C: 1A              LD      A,(DE)              
015D: 08              EX      AF,AF'              
015E: 1A              LD      A,(DE)              
015F: 0A              LD      A,(BC)              
0160: 21 40 80        LD      HL,$8040            
0163: 11 41 80        LD      DE,$8041            
0166: 01 7F 03        LD      BC,$037F            
0169: 36 24           LD      (HL),$24            
016B: ED B0           LDIR                        
016D: 21 40 84        LD      HL,$8440            
0170: 11 41 84        LD      DE,$8441            
0173: 01 7F 03        LD      BC,$037F            
0176: 36 00           LD      (HL),$00            
0178: ED B0           LDIR                        
017A: 3E 04           LD      A,$04               
017C: 06 20           LD      B,$20               
017E: DF              RST     0X18                
017F: 3E 4E           LD      A,$4E               
0181: 06 20           LD      B,$20               
0183: DF              RST     0X18                
0184: C9              RET                         
0185: 21 21 98        LD      HL,$9821            
0188: 34              INC     (HL)                
0189: 7E              LD      A,(HL)              
018A: 3C              INC     A                   
018B: E6 03           AND     $03                 
018D: 32 25 98        LD      ($9825),A           
0190: 28 10           JR      Z,$1A2              ; {}
0192: 0E 06           LD      C,$06               
0194: F7              RST     0X30                
0195: EB              EX      DE,HL               
0196: 3A 21 98        LD      A,($9821)           
0199: 6F              LD      L,A                 
019A: 26 00           LD      H,$00               
019C: CD 53 0A        CALL    $0A53               ; {}
019F: AF              XOR     A                   
01A0: 18 0A           JR      $1AC                ; {}
01A2: 0E 07           LD      C,$07               
01A4: F7              RST     0X30                
01A5: 3E 01           LD      A,$01               
01A7: 32 AD 9A        LD      ($9AAD),A           
01AA: 3E 08           LD      A,$08               
01AC: 32 A8 92        LD      ($92A8),A           
01AF: 3E 03           LD      A,$03               
01B1: 32 AE 92        LD      ($92AE),A           
01B4: 32 0B 92        LD      ($920B),A           
01B7: 3A 25 98        LD      A,($9825)           
01BA: A7              AND     A                   
01BB: 08              EX      AF,AF'              
01BC: CD 7F 11        CALL    $117F               ; {}
01BF: 3A AE 92        LD      A,($92AE)           
01C2: A7              AND     A                   
01C3: 20 FA           JR      NZ,$1BF             ; {}
01C5: 3E 78           LD      A,$78               
01C7: 32 AE 92        LD      ($92AE),A           
01CA: CD A4 28        CALL    $28A4               ; {}
01CD: CD B0 25        CALL    $25B0               ; {}
01D0: 3E 02           LD      A,$02               
01D2: 32 AC 92        LD      ($92AC),A           
01D5: AF              XOR     A                   
01D6: CD D5 12        CALL    $12D5               ; {}
01D9: AF              XOR     A                   
01DA: 06 30           LD      B,$30               
01DC: 21 00 92        LD      HL,$9200            
01DF: 77              LD      (HL),A              
01E0: 2C              INC     L                   
01E1: 2C              INC     L                   
01E2: 10 FB           DJNZ    $1DF                ; {}
01E4: 32 09 90        LD      ($9009),A           
01E7: 32 10 90        LD      ($9010),A           
01EA: 32 04 90        LD      ($9004),A           
01ED: 32 88 92        LD      ($9288),A           
01F0: 32 2C 98        LD      ($982C),A           
01F3: 32 41 98        LD      ($9841),A           
01F6: 32 42 98        LD      ($9842),A           
01F9: 32 26 98        LD      ($9826),A           
01FC: 32 B0 99        LD      ($99B0),A           
01FF: 32 24 98        LD      ($9824),A           
0202: 3C              INC     A                   
0203: 32 2D 98        LD      ($982D),A           
0206: 32 6D 98        LD      ($986D),A           
0209: 32 28 98        LD      ($9828),A           
020C: 32 0B 90        LD      ($900B),A           
020F: 32 08 90        LD      ($9008),A           
0212: 32 0A 90        LD      ($900A),A           
0215: CD 00 2C        CALL    $2C00               ; {}
0218: 21 30 98        LD      HL,$9830            
021B: 11 B5 01        LD      DE,$01B5            
021E: 06 04           LD      B,$04               
0220: 72              LD      (HL),D              
0221: 2C              INC     L                   
0222: 73              LD      (HL),E              
0223: 2C              INC     L                   
0224: 10 FA           DJNZ    $220                ; {}
0226: 3A 05 68        LD      A,($6805)           
0229: CB 4F           BIT     1,A                 
022B: C0              RET     NZ                  
022C: 0E 0B           LD      C,$0B               
022E: 21 B0 83        LD      HL,$83B0            
0231: CD B3 13        CALL    $13B3               ; {}
0234: C3 85 01        JP      $0185               ; {}
0237: F5              PUSH    AF                  
0238: 08              EX      AF,AF'              
0239: F5              PUSH    AF                  
023A: C5              PUSH    BC                  
023B: D5              PUSH    DE                  
023C: E5              PUSH    HL                  
023D: DD E5           PUSH    IX                  
023F: FD E5           PUSH    IY                  
0241: 3A 04 68        LD      A,($6804)           
0244: 57              LD      D,A                 
0245: 3A A0 92        LD      A,($92A0)           
0248: E6 1C           AND     $1C                 
024A: 4F              LD      C,A                 
024B: 0F              RRCA                        
024C: A9              XOR     C                   
024D: E6 18           AND     $18                 
024F: 4F              LD      C,A                 
0250: 3A BE 99        LD      A,($99BE)           
0253: CB 4A           BIT     1,D                 
0255: 20 02           JR      NZ,$259             ; {}
0257: 3E 07           LD      A,$07               
0259: E6 07           AND     $07                 
025B: B1              OR      C                   
025C: 06 05           LD      B,$05               
025E: 21 00 A0        LD      HL,$A000            
0261: 77              LD      (HL),A              
0262: 2C              INC     L                   
0263: 0F              RRCA                        
0264: 10 FB           DJNZ    $261                ; {}
0266: 32 30 68        LD      ($6830),A           
0269: AF              XOR     A                   
026A: 32 20 68        LD      ($6820),A           
026D: CB 4A           BIT     1,D                 
026F: CA A8 02        JP      Z,$02A8             ; {}
0272: 4F              LD      C,A                 
0273: 21 00 90        LD      HL,$9000            
0276: 79              LD      A,C                 
0277: 85              ADD     A,L                 
0278: 6F              LD      L,A                 
0279: 7E              LD      A,(HL)              
027A: A7              AND     A                   
027B: 20 03           JR      NZ,$280             ; {}
027D: 0C              INC     C                   
027E: 18 F3           JR      $273                ; {}
0280: 47              LD      B,A                 
0281: 21 96 00        LD      HL,$0096            
0284: 79              LD      A,C                 
0285: CB 27           SLA     A                   
0287: 85              ADD     A,L                 
0288: 6F              LD      L,A                 
0289: 5E              LD      E,(HL)              
028A: 23              INC     HL                  
028B: 56              LD      D,(HL)              
028C: EB              EX      DE,HL               
028D: C5              PUSH    BC                  
028E: CD 3B 00        CALL    $003B               ; {}
0291: C1              POP     BC                  
0292: 78              LD      A,B                 
0293: 81              ADD     A,C                 
0294: 4F              LD      C,A                 
0295: E6 E0           AND     $E0                 
0297: 28 DA           JR      Z,$273              ; {}
0299: 21 00 70        LD      HL,$7000            
029C: 11 B5 99        LD      DE,$99B5            
029F: 01 03 00        LD      BC,$0003            
02A2: D9              EXX                         
02A3: 3E 71           LD      A,$71               
02A5: 32 00 71        LD      ($7100),A           
02A8: 3E 01           LD      A,$01               
02AA: 32 20 68        LD      ($6820),A           
02AD: FD E1           POP     IY                  
02AF: DD E1           POP     IX                  
02B1: E1              POP     HL                  
02B2: D1              POP     DE                  
02B3: C1              POP     BC                  
02B4: F1              POP     AF                  
02B5: 08              EX      AF,AF'              
02B6: F1              POP     AF                  
02B7: FB              EI                          
02B8: C9              RET                         
02B9: 00              NOP                         
02BA: 00              NOP                         
02BB: 00              NOP                         
02BC: 00              NOP                         
02BD: 02              LD      (BC),A              
02BE: 24              INC     H                   
02BF: 17              RLA                         
02C0: 0A              LD      A,(BC)              
02C1: 16 0C           LD      D,$0C               
02C3: 18 ED           JR      $2B2                ; {}
02C5: 56              LD      D,(HL)              
02C6: AF              XOR     A                   
02C7: 21 E0 99        LD      HL,$99E0            
02CA: 06 10           LD      B,$10               
02CC: 77              LD      (HL),A              
02CD: 23              INC     HL                  
02CE: 10 FC           DJNZ    $2CC                ; {}
02D0: C3 6C 33        JP      $336C               ; {}
02D3: 31 A0 90        LD      SP,$90A0            
02D6: AF              XOR     A                   
02D7: 21 AC 92        LD      HL,$92AC            
02DA: 06 04           LD      B,$04               
02DC: DF              RST     0X18                
02DD: 21 A0 9A        LD      HL,$9AA0            
02E0: 06 20           LD      B,$20               
02E2: DF              RST     0X18                
02E3: 32 07 A0        LD      ($A007),A           
02E6: 32 15 92        LD      ($9215),A           
02E9: 32 B9 99        LD      ($99B9),A           
02EC: 3D              DEC     A                   
02ED: 21 CA 92        LD      HL,$92CA            
02F0: 06 10           LD      B,$10               
02F2: DF              RST     0X18                
02F3: 3E 01           LD      A,$01               
02F5: 32 20 68        LD      ($6820),A           
02F8: 21 C0 83        LD      HL,$83C0            
02FB: 06 40           LD      B,$40               
02FD: 3E 24           LD      A,$24               
02FF: DF              RST     0X18                
0300: 26 80           LD      H,$80               
0302: 06 40           LD      B,$40               
0304: DF              RST     0X18                
0305: 21 00 84        LD      HL,$8400            
0308: 06 40           LD      B,$40               
030A: 3E 03           LD      A,$03               
030C: DF              RST     0X18                
030D: CD 60 01        CALL    $0160               ; {}
0310: 11 20 8A        LD      DE,$8A20            
0313: 3E 05           LD      A,$05               
0315: 06 00           LD      B,$00               
0317: 21 B9 02        LD      HL,$02B9            
031A: 0E 06           LD      C,$06               
031C: ED B0           LDIR                        
031E: 3D              DEC     A                   
031F: 20 F6           JR      NZ,$317             ; {}
0321: 21 BF 02        LD      HL,$02BF            
0324: 3E 2A           LD      A,$2A               
0326: 06 05           LD      B,$05               
0328: 0E FF           LD      C,$FF               
032A: ED A0           LDI                         
032C: 2B              DEC     HL                  
032D: 12              LD      (DE),A              
032E: 1C              INC     E                   
032F: ED A0           LDI                         
0331: 10 F7           DJNZ    $32A                ; {}
0333: 3E 01           LD      A,$01               
0335: 32 01 92        LD      ($9201),A           
0338: 21 05 A0        LD      HL,$A005            
033B: 36 00           LD      (HL),$00            
033D: 77              LD      (HL),A              
033E: CD 3C 00        CALL    $003C               ; {}
0341: CD D6 00        CALL    $00D6               ; {}
0344: CD 42 12        CALL    $1242               ; {}
0347: EF              RST     0X28                
0348: 3E 20           LD      A,$20               
034A: 32 1E 90        LD      ($901E),A           
034D: 3A B5 99        LD      A,($99B5)           
0350: 32 B8 99        LD      ($99B8),A           
0353: AF              XOR     A                   
0354: 32 1E 90        LD      ($901E),A           
0357: 32 20 90        LD      ($9020),A           
035A: AF              XOR     A                   
035B: 32 07 A0        LD      ($A007),A           
035E: 32 15 92        LD      ($9215),A           
0361: 32 12 90        LD      ($9012),A           
0364: 06 80           LD      B,$80               
0366: 21 00 92        LD      HL,$9200            
0369: DF              RST     0X18                
036A: 3E 06           LD      A,$06               
036C: 32 BE 99        LD      ($99BE),A           
036F: EF              RST     0X28                
0370: CD 3C 00        CALL    $003C               ; {}
0373: CD 42 12        CALL    $1242               ; {}
0376: 3A B8 99        LD      A,($99B8)           
0379: A7              AND     A                   
037A: 3E 01           LD      A,$01               
037C: 28 02           JR      Z,$380              ; {}
037E: 3E 02           LD      A,$02               
0380: 32 01 92        LD      ($9201),A           
0383: 20 18           JR      NZ,$39D             ; {}
0385: AF              XOR     A                   
0386: 32 03 92        LD      ($9203),A           
0389: 3C              INC     A                   
038A: 32 02 90        LD      ($9002),A           
038D: 3A 01 92        LD      A,($9201)           
0390: 3D              DEC     A                   
0391: 28 FA           JR      Z,$38D              ; {}
0393: CD 42 12        CALL    $1242               ; {}
0396: CD 60 01        CALL    $0160               ; {}
0399: EF              RST     0X28                
039A: CD 3C 00        CALL    $003C               ; {}
039D: AF              XOR     A                   
039E: 32 0B 92        LD      ($920B),A           
03A1: 0E 13           LD      C,$13               
03A3: F7              RST     0X30                
03A4: 0E 01           LD      C,$01               
03A6: F7              RST     0X30                
03A7: 21 52 04        LD      HL,$0452            
03AA: 22 80 92        LD      ($9280),HL          
03AD: 3A 80 99        LD      A,($9980)           
03B0: FE FF           CP      $FF                 
03B2: 28 24           JR      Z,$3D8              ; {}
03B4: 5F              LD      E,A                 
03B5: 0E 1B           LD      C,$1B               
03B7: CD 3D 04        CALL    $043D               ; {}
03BA: 3A 81 99        LD      A,($9981)           
03BD: FE FF           CP      $FF                 
03BF: 28 17           JR      Z,$3D8              ; {}
03C1: E6 7F           AND     $7F                 
03C3: 5F              LD      E,A                 
03C4: 0E 1C           LD      C,$1C               
03C6: CD 3D 04        CALL    $043D               ; {}
03C9: 3A 81 99        LD      A,($9981)           
03CC: CB 7F           BIT     7,A                 
03CE: 20 08           JR      NZ,$3D8             ; {}
03D0: E6 7F           AND     $7F                 
03D2: 5F              LD      E,A                 
03D3: 0E 1D           LD      C,$1D               
03D5: CD 3D 04        CALL    $043D               ; {}
03D8: 3A 01 92        LD      A,($9201)           
03DB: FE 02           CP      $02                 
03DD: 28 F9           JR      Z,$3D8              ; {}
03DF: 32 B7 9A        LD      ($9AB7),A           
03E2: CD 60 01        CALL    $0160               ; {}
03E5: CD 3C 00        CALL    $003C               ; {}
03E8: 21 05 A0        LD      HL,$A005            
03EB: 36 00           LD      (HL),$00            
03ED: 36 01           LD      (HL),$01            
03EF: 21 20 98        LD      HL,$9820            
03F2: AF              XOR     A                   
03F3: 06 A0           LD      B,$A0               
03F5: DF              RST     0X18                
03F6: 32 B7 9A        LD      ($9AB7),A           
03F9: 32 B9 99        LD      ($99B9),A           
03FC: 3C              INC     A                   
03FD: 32 AB 9A        LD      ($9AAB),A           
0400: 32 12 90        LD      ($9012),A           
0403: 32 F2 98        LD      ($98F2),A           
0406: CD 66 04        CALL    $0466               ; {}
0409: CD 7B 12        CALL    $127B               ; {}
040C: 0E 04           LD      C,$04               
040E: F7              RST     0X30                
040F: 21 AF 92        LD      HL,$92AF            
0412: 36 08           LD      (HL),$08            
0414: 7E              LD      A,(HL)              
0415: A7              AND     A                   
0416: 20 FC           JR      NZ,$414             ; {}
0418: 21 90 92        LD      HL,$9290            
041B: 06 10           LD      B,$10               
041D: DF              RST     0X18                
041E: 06 30           LD      B,$30               
0420: 21 B0 98        LD      HL,$98B0            
0423: DF              RST     0X18                
0424: 21 B0 83        LD      HL,$83B0            
0427: 0E 0B           LD      C,$0B               
0429: CD B3 13        CALL    $13B3               ; {}
042C: 3E 01           LD      A,$01               
042E: 32 80 98        LD      ($9880),A           
0431: 3A 80 99        LD      A,($9980)           
0434: 32 3E 98        LD      ($983E),A           
0437: 32 7E 98        LD      ($987E),A           

043A: C3 0F 06        JP      $060F               ; {}
043D: F7              RST     0X30                
043E: EB              EX      DE,HL               
043F: 7B              LD      A,E                 
0440: C6 40           ADD     $40                 
0442: 5F              LD      E,A                 
0443: 26 00           LD      H,$00               
0445: CD 53 0A        CALL    $0A53               ; {}
0448: EB              EX      DE,HL               
0449: 0E 1E           LD      C,$1E               
044B: CD B3 13        CALL    $13B3               ; {}
044E: CD 9E 12        CALL    $129E               ; {}
0451: C9              RET                         
0452: 00              NOP                         
0453: 81              ADD     A,C                 
0454: 19              ADD     HL,DE               
0455: 56              LD      D,(HL)              
0456: 02              LD      (BC),A              
0457: 81              ADD     A,C                 
0458: 19              ADD     HL,DE               
0459: 62              LD      H,D                 
045A: 04              INC     B                   
045B: 81              ADD     A,C                 
045C: 19              ADD     HL,DE               
045D: 6E              LD      L,(HL)              
045E: CD 28 07        CALL    $0728               ; {}

0461: CD 0B 08        CALL    $080B               ; {}
0464: 18 F8           JR      $45E                ; {}
0466: 3A 82 99        LD      A,($9982)           
0469: 32 20 98        LD      ($9820),A           
046C: 32 60 98        LD      ($9860),A           
046F: 11 F8 83        LD      DE,$83F8            
0472: 21 95 04        LD      HL,$0495            
0475: CD 86 04        CALL    $0486               ; {}
0478: 11 E3 83        LD      DE,$83E3            
047B: 21 95 04        LD      HL,$0495            
047E: 3A B3 99        LD      A,($99B3)           
0481: A7              AND     A                   
0482: 20 02           JR      NZ,$486             ; {}
0484: 23              INC     HL                  
0485: 23              INC     HL                  
0486: 0E 07           LD      C,$07               
0488: ED B0           LDIR                        
048A: 21 97 04        LD      HL,$0497            
048D: 11 C3 83        LD      DE,$83C3            
0490: 0E 04           LD      C,$04               
0492: ED B0           LDIR                        
0494: C9              RET                         
0495: 00              NOP                         
0496: 00              NOP                         
0497: 24              INC     H                   
0498: 24              INC     H                   
0499: 24              INC     H                   
049A: 24              INC     H                   
049B: 24              INC     H                   
049C: 24              INC     H                   
049D: 24              INC     H                   
049E: E1              POP     HL                  
049F: 21 AF 92        LD      HL,$92AF            
04A2: 36 04           LD      (HL),$04            
04A4: 3A 1D 90        LD      A,($901D)           
04A7: A7              AND     A                   
04A8: 28 17           JR      Z,$4C1              ; {}
04AA: AF              XOR     A                   
04AB: 32 13 92        LD      ($9213),A           
04AE: 3C              INC     A                   
04AF: 32 25 90        LD      ($9025),A           
04B2: 3A A7 92        LD      A,($92A7)           
04B5: A7              AND     A                   
04B6: C2 5E 04        JP      NZ,$045E            ; {}
04B9: 3A 1D 90        LD      A,($901D)           
04BC: A7              AND     A                   
04BD: 20 FA           JR      NZ,$4B9             ; {}
04BF: 18 1B           JR      $4DC                ; {}
04C1: 7E              LD      A,(HL)              
04C2: A7              AND     A                   
04C3: 20 DF           JR      NZ,$4A4             ; {}
04C5: CD 28 07        CALL    $0728               ; {}
04C8: 3A A7 92        LD      A,($92A7)           
04CB: 32 43 98        LD      ($9843),A           
04CE: 4F              LD      C,A                 
04CF: 3A 13 92        LD      A,($9213)           
04D2: B1              OR      C                   
04D3: 20 0D           JR      NZ,$4E2             ; {}
04D5: 3A 25 98        LD      A,($9825)           
04D8: A7              AND     A                   
04D9: CA 50 06        JP      Z,$0650             ; {}
04DC: CD 85 01        CALL    $0185               ; {}
04DF: C3 32 06        JP      $0632               ; {}
04E2: 21 20 98        LD      HL,$9820            
04E5: 7E              LD      A,(HL)              
04E6: 35              DEC     (HL)                
04E7: A7              AND     A                   
04E8: C2 79 05        JP      NZ,$0579            ; {}
04EB: 3A B3 99        LD      A,($99B3)           
04EE: A7              AND     A                   
04EF: 28 0C           JR      Z,$4FD              ; {}
04F1: 21 4E 82        LD      HL,$824E            
04F4: 3A 40 98        LD      A,($9840)           
04F7: C6 04           ADD     $04                 
04F9: 4F              LD      C,A                 
04FA: CD B3 13        CALL    $13B3               ; {}
04FD: 0E 02           LD      C,$02               
04FF: F7              RST     0X30                
0500: CD 31 13        CALL    $1331               ; {}
0503: CD 31 13        CALL    $1331               ; {}
0506: 21 18 90        LD      HL,$9018            
0509: 7E              LD      A,(HL)              
050A: A7              AND     A                   
050B: 20 FC           JR      NZ,$509             ; {}
050D: EF              RST     0X28                
050E: CD 3C 00        CALL    $003C               ; {}
0511: CD 60 01        CALL    $0160               ; {}
0514: 0E 15           LD      C,$15               
0516: F7              RST     0X30                
0517: 0E 16           LD      C,$16               
0519: F7              RST     0X30                
051A: 11 32 81        LD      DE,$8132            
051D: 2A 46 98        LD      HL,($9846)          
0520: CD 53 0A        CALL    $0A53               ; {}
0523: 0E 18           LD      C,$18               
0525: F7              RST     0X30                
0526: 11 35 81        LD      DE,$8135            
0529: 2A 44 98        LD      HL,($9844)          
052C: CD 53 0A        CALL    $0A53               ; {}
052F: 0E 19           LD      C,$19               
0531: F7              RST     0X30                
0532: CD 72 0A        CALL    $0A72               ; {}
0535: EB              EX      DE,HL               
0536: 0E 1A           LD      C,$1A               
0538: CD B3 13        CALL    $13B3               ; {}
053B: 21 AE 92        LD      HL,$92AE            
053E: 36 0E           LD      (HL),$0E            
0540: 7E              LD      A,(HL)              
0541: A7              AND     A                   
0542: 20 FC           JR      NZ,$540             ; {}
0544: CD 60 01        CALL    $0160               ; {}
0547: CD 00 30        CALL    $3000               ; {}
054A: AF              XOR     A                   
054B: 32 B0 9A        LD      ($9AB0),A           
054E: 21 AC 9A        LD      HL,$9AAC            
0551: 11 B6 9A        LD      DE,$9AB6            
0554: 1A              LD      A,(DE)              
0555: 46              LD      B,(HL)              
0556: B0              OR      B                   
0557: 28 09           JR      Z,$562              ; {}
0559: 04              INC     B                   
055A: 05              DEC     B                   
055B: 28 02           JR      Z,$55F              ; {}
055D: 36 01           LD      (HL),$01            
055F: 76              HALT                        
0560: 18 F2           JR      $554                ; {}
0562: CD 60 01        CALL    $0160               ; {}
0565: 3A B3 99        LD      A,($99B3)           
0568: A7              AND     A                   
0569: CA DE 06        JP      Z,$06DE             ; {}
056C: 3A 60 98        LD      A,($9860)           
056F: 3C              INC     A                   
0570: CA DE 06        JP      Z,$06DE             ; {}
0573: 3A 13 92        LD      A,($9213)           
0576: 3D              DEC     A                   
0577: 20 15           JR      NZ,$58E             ; {}
0579: 3A B3 99        LD      A,($99B3)           
057C: A7              AND     A                   
057D: CA 04 06        JP      Z,$0604             ; {}
0580: 3A 60 98        LD      A,($9860)           
0583: 3C              INC     A                   
0584: CA 12 06        JP      Z,$0612             ; {}
0587: 3A 13 92        LD      A,($9213)           
058A: 3D              DEC     A                   
058B: C2 12 06        JP      NZ,$0612            ; {}
058E: 3A A7 92        LD      A,($92A7)           
0591: A7              AND     A                   
0592: 28 06           JR      Z,$59A              ; {}
0594: 3A 87 92        LD      A,($9287)           
0597: A7              AND     A                   
0598: 20 FA           JR      NZ,$594             ; {}
059A: AF              XOR     A                   
059B: 32 B4 99        LD      ($99B4),A           
059E: 3C              INC     A                   
059F: 21 0E 90        LD      HL,$900E            
05A2: 77              LD      (HL),A              
05A3: 7E              LD      A,(HL)              
05A4: A7              AND     A                   
05A5: 20 FC           JR      NZ,$5A3             ; {}
05A7: 3A A0 9A        LD      A,($9AA0)           
05AA: 32 48 98        LD      ($9848),A           
05AD: 3A AE 92        LD      A,($92AE)           
05B0: 32 3F 98        LD      ($983F),A           
05B3: CD 0C 11        CALL    $110C               ; {}
05B6: CD 00 2C        CALL    $2C00               ; {}
05B9: 3A 3F 98        LD      A,($983F)           
05BC: 32 AE 92        LD      ($92AE),A           
05BF: 3A 48 98        LD      A,($9848)           
05C2: 32 A0 9A        LD      ($9AA0),A           
05C5: CD 7E 13        CALL    $137E               ; {}
05C8: 3A 43 98        LD      A,($9843)           
05CB: A7              AND     A                   
05CC: 28 03           JR      Z,$5D1              ; {}
05CE: CD B0 25        CALL    $25B0               ; {}
05D1: 3A 40 98        LD      A,($9840)           
05D4: 4F              LD      C,A                 
05D5: 3A 83 99        LD      A,($9983)           
05D8: A1              AND     C                   
05D9: 32 07 A0        LD      ($A007),A           
05DC: 32 15 92        LD      ($9215),A           
05DF: 3E 3F           LD      A,$3F               
05E1: CD D5 12        CALL    $12D5               ; {}
05E4: 37              SCF                         
05E5: 08              EX      AF,AF'              
05E6: CD 7F 11        CALL    $117F               ; {}
05E9: 3A 43 98        LD      A,($9843)           
05EC: A7              AND     A                   
05ED: 28 20           JR      Z,$60F              ; {}
05EF: 0E 03           LD      C,$03               
05F1: F7              RST     0X30                
05F2: 3E 80           LD      A,$80               
05F4: 32 B4 99        LD      ($99B4),A           
05F7: 21 0E 90        LD      HL,$900E            
05FA: 3E 01           LD      A,$01               
05FC: 77              LD      (HL),A              
05FD: 7E              LD      A,(HL)              
05FE: A7              AND     A                   
05FF: 20 FC           JR      NZ,$5FD             ; {}
0601: C3 12 06        JP      $0612               ; {}
0604: 3A 43 98        LD      A,($9843)           
0607: A7              AND     A                   
0608: 20 14           JR      NZ,$61E             ; {}
060A: CD 85 01        CALL    $0185               ; {}
060D: 18 0F           JR      $61E                ; {}
060F: CD 85 01        CALL    $0185               ; {}
0612: 3A 40 98        LD      A,($9840)           
0615: C6 04           ADD     $04                 
0617: 4F              LD      C,A                 
0618: 21 6E 82        LD      HL,$826E            
061B: CD B3 13        CALL    $13B3               ; {}
061E: CD 3D 13        CALL    $133D               ; {}
0621: 3A AE 92        LD      A,($92AE)           
0624: C6 1E           ADD     $1E                 
0626: FE 78           CP      $78                 
0628: 38 02           JR      C,$62C              ; {}
062A: 3E 78           LD      A,$78               
062C: 32 AE 92        LD      ($92AE),A           
062F: CD 31 13        CALL    $1331               ; {}
0632: 3E 01           LD      A,$01               
0634: 32 15 90        LD      ($9015),A           
0637: 32 25 90        LD      ($9025),A           
063A: 32 42 98        LD      ($9842),A           
063D: 0E 0B           LD      C,$0B               
063F: 21 B0 83        LD      HL,$83B0            
0642: CD B3 13        CALL    $13B3               ; {}
0645: 0E 0B           LD      C,$0B               
0647: 21 AE 83        LD      HL,$83AE            
064A: CD B3 13        CALL    $13B3               ; {}
064D: C3 5E 04        JP      $045E               ; {}
0650: 3A 88 92        LD      A,($9288)           
0653: 5F              LD      E,A                 
0654: 21 AE 9A        LD      HL,$9AAE            
0657: FE 28           CP      $28                 
0659: 20 03           JR      NZ,$65E             ; {}
065B: 21 B4 9A        LD      HL,$9AB4            
065E: 36 01           LD      (HL),$01            
0660: CD 31 13        CALL    $1331               ; {}
0663: 0E 08           LD      C,$08               
0665: F7              RST     0X30                
0666: CD 31 13        CALL    $1331               ; {}
0669: 6B              LD      L,E                 
066A: 26 00           LD      H,$00               
066C: 11 10 81        LD      DE,$8110            
066F: CD 53 0A        CALL    $0A53               ; {}
0672: CD 31 13        CALL    $1331               ; {}
0675: 3A 88 92        LD      A,($9288)           
0678: FE 28           CP      $28                 
067A: 28 1D           JR      Z,$699              ; {}
067C: 0E 09           LD      C,$09               
067E: F7              RST     0X30                
067F: CD 31 13        CALL    $1331               ; {}
0682: EB              EX      DE,HL               
0683: 3A 88 92        LD      A,($9288)           
0686: A7              AND     A                   
0687: 28 0A           JR      Z,$693              ; {}
0689: 6F              LD      L,A                 
068A: 26 00           LD      H,$00               
068C: CD 53 0A        CALL    $0A53               ; {}
068F: AF              XOR     A                   
0690: 12              LD      (DE),A              
0691: E7              RST     0X20                
0692: AF              XOR     A                   
0693: 12              LD      (DE),A              
0694: 3A 88 92        LD      A,($9288)           
0697: 18 21           JR      $6BA                ; {}
0699: 06 07           LD      B,$07               
069B: 3A A0 92        LD      A,($92A0)           
069E: E6 0F           AND     $0F                 
06A0: 20 F9           JR      NZ,$69B             ; {}
06A2: 0E 0B           LD      C,$0B               
06A4: CB 40           BIT     0,B                 
06A6: 28 01           JR      Z,$6A9              ; {}
06A8: 0C              INC     C                   
06A9: C5              PUSH    BC                  
06AA: F7              RST     0X30                
06AB: C1              POP     BC                  
06AC: 3A A0 92        LD      A,($92A0)           
06AF: E6 0F           AND     $0F                 
06B1: 28 F9           JR      Z,$6AC              ; {}
06B3: 10 E6           DJNZ    $69B                ; {}
06B5: 0E 0D           LD      C,$0D               
06B7: F7              RST     0X30                
06B8: 3E 64           LD      A,$64               
06BA: 21 9F 92        LD      HL,$929F            
06BD: 86              ADD     A,(HL)              
06BE: 77              LD      (HL),A              
06BF: CD 28 07        CALL    $0728               ; {}
06C2: CD 31 13        CALL    $1331               ; {}
06C5: CD 31 13        CALL    $1331               ; {}
06C8: 21 B0 83        LD      HL,$83B0            
06CB: 0E 0B           LD      C,$0B               
06CD: CD B3 13        CALL    $13B3               ; {}
06D0: 21 B3 83        LD      HL,$83B3            
06D3: 0E 0B           LD      C,$0B               
06D5: CD B3 13        CALL    $13B3               ; {}
06D8: 0E 0B           LD      C,$0B               
06DA: F7              RST     0X30                
06DB: C3 DC 04        JP      $04DC               ; {}
06DE: 76              HALT                        
06DF: F3              DI                          
06E0: 3A 00 71        LD      A,($7100)           
06E3: FE 10           CP      $10                 
06E5: 20 F9           JR      NZ,$6E0             ; {}
06E7: 21 25 07        LD      HL,$0725            
06EA: 11 00 70        LD      DE,$7000            
06ED: 01 03 00        LD      BC,$0003            
06F0: D9              EXX                         
06F1: 3E 61           LD      A,$61               
06F3: 32 00 71        LD      ($7100),A           
06F6: 76              HALT                        
06F7: AF              XOR     A                   
06F8: CD 3C 09        CALL    $093C               ; {}
06FB: FB              EI                          
06FC: AF              XOR     A                   
06FD: 06 20           LD      B,$20               
06FF: 21 A0 9A        LD      HL,$9AA0            
0702: DF              RST     0X18                
0703: 11 F9 83        LD      DE,$83F9            
0706: CD 27 0A        CALL    $0A27               ; {}
0709: 11 E4 83        LD      DE,$83E4            
070C: CD 27 0A        CALL    $0A27               ; {}
070F: 3A B3 99        LD      A,($99B3)           
0712: 3C              INC     A                   
0713: 21 E1 99        LD      HL,$99E1            
0716: 86              ADD     A,(HL)              
0717: 27              DAA                         
0718: 77              LD      (HL),A              
0719: D2 5A 03        JP      NC,$035A            ; {}
071C: 2B              DEC     HL                  
071D: 7E              LD      A,(HL)              
071E: C6 01           ADD     $01                 
0720: 27              DAA                         
0721: 77              LD      (HL),A              
0722: C3 5A 03        JP      $035A               ; {}
0725: 02              LD      (BC),A              
0726: 02              LD      (BC),A              
0727: 02              LD      (BC),A              
0728: 3A 40 98        LD      A,($9840)           
072B: A7              AND     A                   
072C: 3E F9           LD      A,$F9               
072E: 28 02           JR      Z,$732              ; {}
0730: 3E E4           LD      A,$E4               
0732: DD 6F           LD      IXL,A               
0734: 06 10           LD      B,$10               
0736: 21 90 92        LD      HL,$9290            
0739: EB              EX      DE,HL               
073A: 21 FA 07        LD      HL,$07FA            
073D: 78              LD      A,B                 
073E: D7              RST     0X10                
073F: 4E              LD      C,(HL)              
0740: EB              EX      DE,HL               
0741: 7E              LD      A,(HL)              
0742: A7              AND     A                   
0743: 28 1D           JR      Z,$762              ; {}
0745: 35              DEC     (HL)                
0746: EB              EX      DE,HL               
0747: 26 83           LD      H,$83               
0749: DD 7D           LD      A,IXL               
074B: 6F              LD      L,A                 
074C: 79              LD      A,C                 
074D: E6 0F           AND     $0F                 
074F: CD D8 07        CALL    $07D8               ; {}
0752: DD 7D           LD      A,IXL               
0754: 3C              INC     A                   
0755: 6F              LD      L,A                 
0756: 79              LD      A,C                 
0757: 07              RLCA                        
0758: 07              RLCA                        
0759: 07              RLCA                        
075A: 07              RLCA                        
075B: E6 0F           AND     $0F                 
075D: CD D8 07        CALL    $07D8               ; {}
0760: 18 DE           JR      $740                ; {}
0762: 2C              INC     L                   
0763: 10 D4           DJNZ    $739                ; {}
0765: DD 7D           LD      A,IXL               
0767: C6 04           ADD     $04                 
0769: 5F              LD      E,A                 
076A: 21 F2 83        LD      HL,$83F2            
076D: 16 83           LD      D,$83               
076F: 06 06           LD      B,$06               
0771: 1A              LD      A,(DE)              
0772: 96              SUB     (HL)                
0773: C6 09           ADD     $09                 
0775: FE E5           CP      $E5                 
0777: 30 0F           JR      NC,$788             ; {}
0779: D6 0A           SUB     $0A                 
077B: FE 09           CP      $09                 
077D: 38 09           JR      C,$788              ; {}
077F: 3C              INC     A                   
0780: 20 0C           JR      NZ,$78E             ; {}
0782: 2D              DEC     L                   
0783: 1D              DEC     E                   
0784: 10 EB           DJNZ    $771                ; {}
0786: 18 06           JR      $78E                ; {}
0788: 1A              LD      A,(DE)              
0789: 77              LD      (HL),A              
078A: 2D              DEC     L                   
078B: 1D              DEC     E                   
078C: 10 FA           DJNZ    $788                ; {}
078E: DD 7D           LD      A,IXL               
0790: C6 04           ADD     $04                 
0792: 6F              LD      L,A                 
0793: 7E              LD      A,(HL)              
0794: FE 24           CP      $24                 
0796: 20 01           JR      NZ,$799             ; {}
0798: AF              XOR     A                   
0799: E6 3F           AND     $3F                 
079B: 07              RLCA                        
079C: 4F              LD      C,A                 
079D: 07              RLCA                        
079E: 07              RLCA                        
079F: 81              ADD     A,C                 
07A0: 4F              LD      C,A                 
07A1: 2D              DEC     L                   
07A2: 7E              LD      A,(HL)              
07A3: FE 24           CP      $24                 
07A5: 20 01           JR      NZ,$7A8             ; {}
07A7: AF              XOR     A                   
07A8: 81              ADD     A,C                 
07A9: 21 3E 98        LD      HL,$983E            
07AC: BE              CP      (HL)                
07AD: C0              RET     NZ                  
07AE: 3A 81 99        LD      A,($9981)           
07B1: 47              LD      B,A                 
07B2: E6 7F           AND     $7F                 
07B4: 4F              LD      C,A                 
07B5: 7E              LD      A,(HL)              
07B6: B9              CP      C                   
07B7: 30 03           JR      NC,$7BC             ; {}
07B9: 79              LD      A,C                 
07BA: 18 01           JR      $7BD                ; {}
07BC: 80              ADD     A,B                 
07BD: 77              LD      (HL),A              
07BE: 32 AA 9A        LD      ($9AAA),A           
07C1: 21 20 98        LD      HL,$9820            
07C4: 34              INC     (HL)                
07C5: CD 7E 13        CALL    $137E               ; {}
07C8: 21 EB 99        LD      HL,$99EB            
07CB: 7E              LD      A,(HL)              
07CC: C6 01           ADD     $01                 
07CE: 27              DAA                         
07CF: 77              LD      (HL),A              
07D0: D0              RET     NC                  
07D1: 2D              DEC     L                   
07D2: 7E              LD      A,(HL)              
07D3: C6 01           ADD     $01                 
07D5: 27              DAA                         
07D6: 77              LD      (HL),A              
07D7: C9              RET                         
07D8: A7              AND     A                   
07D9: C8              RET     Z                   
07DA: 86              ADD     A,(HL)              
07DB: FE 24           CP      $24                 
07DD: 38 02           JR      C,$7E1              ; {}
07DF: D6 24           SUB     $24                 
07E1: FE 0A           CP      $0A                 
07E3: 30 02           JR      NC,$7E7             ; {}
07E5: 77              LD      (HL),A              
07E6: C9              RET                         
07E7: D6 0A           SUB     $0A                 
07E9: 77              LD      (HL),A              
07EA: 2C              INC     L                   
07EB: 7E              LD      A,(HL)              
07EC: FE 24           CP      $24                 
07EE: 20 01           JR      NZ,$7F1             ; {}
07F0: AF              XOR     A                   
07F1: FE 09           CP      $09                 
07F3: 28 03           JR      Z,$7F8              ; {}
07F5: 3C              INC     A                   
07F6: 77              LD      (HL),A              
07F7: C9              RET                         
07F8: AF              XOR     A                   
07F9: 18 EE           JR      $7E9                ; {}
07FB: 10 00           DJNZ    $7FD                ; {}
07FD: 00              NOP                         
07FE: 00              NOP                         
07FF: 00              NOP                         
0800: 00              NOP                         
0801: 00              NOP                         
0802: 00              NOP                         
0803: 50              LD      D,B                 
0804: 08              EX      AF,AF'              
0805: 08              EX      AF,AF'              
0806: 08              EX      AF,AF'              
0807: 05              DEC     B                   
0808: 08              EX      AF,AF'              
0809: 15              DEC     D                   
080A: 00              NOP                         
080B: 3A 08 90        LD      A,($9008)           
080E: 47              LD      B,A                 
080F: 3A A7 92        LD      A,($92A7)           
0812: B0              OR      B                   
0813: 20 06           JR      NZ,$81B             ; {}
0815: 32 A0 9A        LD      ($9AA0),A           
0818: C3 9E 04        JP      $049E               ; {}
081B: 3A 13 92        LD      A,($9213)           
081E: A7              AND     A                   
081F: C8              RET     Z                   
0820: AF              XOR     A                   
0821: 32 42 98        LD      ($9842),A           
0824: C3 9E 04        JP      $049E               ; {}
0827: C9              RET                         
0828: 3E 01           LD      A,$01               
082A: 32 D6 92        LD      ($92D6),A           
082D: 21 40 8B        LD      HL,$8B40            
0830: 11 C0 8B        LD      DE,$8BC0            
0833: 01 40 00        LD      BC,$0040            
0836: ED B0           LDIR                        
0838: 21 40 93        LD      HL,$9340            
083B: 11 C0 93        LD      DE,$93C0            
083E: 0E 40           LD      C,$40               
0840: ED B0           LDIR                        
0842: 21 40 9B        LD      HL,$9B40            
0845: 11 C0 9B        LD      DE,$9BC0            
0848: 0E 40           LD      C,$40               
084A: ED B0           LDIR                        
084C: AF              XOR     A                   
084D: 32 D6 92        LD      ($92D6),A           
0850: 3A D7 92        LD      A,($92D7)           
0853: 3D              DEC     A                   
0854: 28 FA           JR      Z,$850              ; {}
0856: C9              RET                         
0857: 3A AE 92        LD      A,($92AE)           
085A: 47              LD      B,A                 
085B: FE 3C           CP      $3C                 
085D: 30 06           JR      NC,$865             ; {}
085F: 3A C5 99        LD      A,($99C5)           
0862: 32 C4 99        LD      ($99C4),A           
0865: 3A A7 92        LD      A,($92A7)           
0868: 4F              LD      C,A                 
0869: 3A C0 99        LD      A,($99C0)           
086C: 21 09 09        LD      HL,$0909            
086F: CD BE 08        CALL    $08BE               ; {}
0872: 32 C8 92        LD      ($92C8),A           
0875: 3A AA 92        LD      A,($92AA)           
0878: A7              AND     A                   
0879: 28 0D           JR      Z,$888              ; {}
087B: 21 C4 92        LD      HL,$92C4            
087E: 3E 02           LD      A,$02               
0880: 06 03           LD      B,$03               
0882: DF              RST     0X18                
0883: AF              XOR     A                   
0884: 32 A0 9A        LD      ($9AA0),A           
0887: C9              RET                         
0888: 3A C1 99        LD      A,($99C1)           
088B: 21 29 09        LD      HL,$0929            
088E: CD BE 08        CALL    $08BE               ; {}
0891: 32 C4 92        LD      ($92C4),A           
0894: 3A C2 99        LD      A,($99C2)           
0897: 21 CD 08        LD      HL,$08CD            
089A: CD AD 08        CALL    $08AD               ; {}
089D: 32 C5 92        LD      ($92C5),A           
08A0: 3A C3 99        LD      A,($99C3)           
08A3: 21 EB 08        LD      HL,$08EB            
08A6: CD AD 08        CALL    $08AD               ; {}
08A9: 32 C6 92        LD      ($92C6),A           
08AC: C9              RET                         
08AD: 5F              LD      E,A                 
08AE: CB 27           SLA     A                   
08B0: 83              ADD     A,E                 
08B1: D7              RST     0X10                
08B2: 78              LD      A,B                 
08B3: FE 28           CP      $28                 
08B5: 30 01           JR      NC,$8B8             ; {}
08B7: 23              INC     HL                  
08B8: A7              AND     A                   
08B9: 20 01           JR      NZ,$8BC             ; {}
08BB: 23              INC     HL                  
08BC: 7E              LD      A,(HL)              
08BD: C9              RET                         
08BE: CB 27           SLA     A                   
08C0: CF              RST     0X08                
08C1: EB              EX      DE,HL               
08C2: 61              LD      H,C                 
08C3: 3E 0A           LD      A,$0A               
08C5: CD 61 10        CALL    $1061               ; {}
08C8: EB              EX      DE,HL               
08C9: 7A              LD      A,D                 
08CA: D7              RST     0X10                
08CB: 7E              LD      A,(HL)              
08CC: C9              RET                         
08CD: 09              ADD     HL,BC               
08CE: 07              RLCA                        
08CF: 05              DEC     B                   
08D0: 08              EX      AF,AF'              
08D1: 06 04           LD      B,$04               
08D3: 07              RLCA                        
08D4: 05              DEC     B                   
08D5: 04              INC     B                   
08D6: 06 04           LD      B,$04               
08D8: 03              INC     BC                  
08D9: 05              DEC     B                   
08DA: 03              INC     BC                  
08DB: 03              INC     BC                  
08DC: 04              INC     B                   
08DD: 03              INC     BC                  
08DE: 03              INC     BC                  
08DF: 04              INC     B                   
08E0: 02              LD      (BC),A              
08E1: 02              LD      (BC),A              
08E2: 03              INC     BC                  
08E3: 03              INC     BC                  
08E4: 02              LD      (BC),A              
08E5: 03              INC     BC                  
08E6: 02              LD      (BC),A              
08E7: 02              LD      (BC),A              
08E8: 02              LD      (BC),A              
08E9: 02              LD      (BC),A              
08EA: 02              LD      (BC),A              
08EB: 06 05           LD      B,$05               
08ED: 04              INC     B                   
08EE: 05              DEC     B                   
08EF: 04              INC     B                   
08F0: 03              INC     BC                  
08F1: 05              DEC     B                   
08F2: 03              INC     BC                  
08F3: 03              INC     BC                  
08F4: 04              INC     B                   
08F5: 03              INC     BC                  
08F6: 02              LD      (BC),A              
08F7: 04              INC     B                   
08F8: 02              LD      (BC),A              
08F9: 02              LD      (BC),A              
08FA: 03              INC     BC                  
08FB: 03              INC     BC                  
08FC: 02              LD      (BC),A              
08FD: 03              INC     BC                  
08FE: 02              LD      (BC),A              
08FF: 01 02 02        LD      BC,$0202            
0902: 01 02 01        LD      BC,$0102            
0905: 01 01 01        LD      BC,$0101            
0908: 01 03 03        LD      BC,$0303            
090B: 01 01 03        LD      BC,$0301            
090E: 03              INC     BC                  
090F: 03              INC     BC                  
0910: 01 07 03        LD      BC,$0307            
0913: 03              INC     BC                  
0914: 01 07 03        LD      BC,$0307            
0917: 03              INC     BC                  
0918: 03              INC     BC                  
0919: 07              RLCA                        
091A: 07              RLCA                        
091B: 03              INC     BC                  
091C: 03              INC     BC                  
091D: 0F              RRCA                        
091E: 07              RLCA                        
091F: 03              INC     BC                  
0920: 03              INC     BC                  
0921: 0F              RRCA                        
0922: 07              RLCA                        
0923: 07              RLCA                        
0924: 03              INC     BC                  
0925: 0F              RRCA                        
0926: 07              RLCA                        
0927: 07              RLCA                        
0928: 07              RLCA                        
0929: 06 0A           LD      B,$0A               
092B: 0F              RRCA                        
092C: 0F              RRCA                        
092D: 04              INC     B                   
092E: 08              EX      AF,AF'              
092F: 0D              DEC     C                   
0930: 0D              DEC     C                   
0931: 04              INC     B                   
0932: 06 0A           LD      B,$0A               
0934: 0A              LD      A,(BC)              
0935: 3A A0 92        LD      A,($92A0)           
0938: 07              RLCA                        
0939: 07              RLCA                        
093A: 07              RLCA                        
093B: 07              RLCA                        
093C: 4F              LD      C,A                 
093D: 3A 01 92        LD      A,($9201)           
0940: FE 03           CP      $03                 
0942: C0              RET     NZ                  
0943: 3A 40 98        LD      A,($9840)           
0946: 47              LD      B,A                 
0947: 2F              CPL                         
0948: A1              AND     C                   
0949: 21 6E 09        LD      HL,$096E            
094C: 11 D9 83        LD      DE,$83D9            
094F: CD 5F 09        CALL    $095F               ; {}
0952: 3A B3 99        LD      A,($99B3)           
0955: A7              AND     A                   
0956: C8              RET     Z                   
0957: 78              LD      A,B                 
0958: A1              AND     C                   
0959: 21 71 09        LD      HL,$0971            
095C: 11 C4 83        LD      DE,$83C4            
095F: C5              PUSH    BC                  
0960: E6 01           AND     $01                 
0962: 28 03           JR      Z,$967              ; {}
0964: 21 74 09        LD      HL,$0974            
0967: 01 03 00        LD      BC,$0003            
096A: ED B0           LDIR                        
096C: C1              POP     BC                  
096D: C9              RET                         
096E: 19              ADD     HL,DE               
096F: 1E 01           LD      E,$01               
0971: 19              ADD     HL,DE               
0972: 1E 02           LD      E,$02               
0974: 24              INC     H                   
0975: 24              INC     H                   
0976: 24              INC     H                   
0977: 3A B5 99        LD      A,($99B5)           
097A: FE BB           CP      $BB                 
097C: CA 6C 33        JP      Z,$336C             ; {}
097F: 3A 01 92        LD      A,($9201)           
0982: FE 03           CP      $03                 
0984: 20 19           JR      NZ,$99F             ; {}
0986: 21 E9 99        LD      HL,$99E9            
0989: 7E              LD      A,(HL)              
098A: C6 01           ADD     $01                 
098C: 27              DAA                         
098D: FE 60           CP      $60                 
098F: 20 01           JR      NZ,$992             ; {}
0991: AF              XOR     A                   
0992: 06 04           LD      B,$04               
0994: 3F              CCF                         
0995: 77              LD      (HL),A              
0996: 2D              DEC     L                   
0997: 7E              LD      A,(HL)              
0998: CE 00           ADC     $00                 
099A: 27              DAA                         
099B: 10 F8           DJNZ    $995                ; {}
099D: 18 42           JR      $9E1                ; {}
099F: 3A B8 99        LD      A,($99B8)           
09A2: FE A0           CP      $A0                 
09A4: 11 3C 80        LD      DE,$803C            
09A7: 28 30           JR      Z,$9D9              ; {}
09A9: 3A B5 99        LD      A,($99B5)           
09AC: 21 CF 09        LD      HL,$09CF            
09AF: 01 06 00        LD      BC,$0006            
09B2: ED B8           LDDR                        
09B4: 1D              DEC     E                   
09B5: 4F              LD      C,A                 
09B6: 07              RLCA                        
09B7: 07              RLCA                        
09B8: 07              RLCA                        
09B9: 07              RLCA                        
09BA: E6 0F           AND     $0F                 
09BC: 28 02           JR      Z,$9C0              ; {}
09BE: 12              LD      (DE),A              
09BF: 1D              DEC     E                   
09C0: 79              LD      A,C                 
09C1: E6 0F           AND     $0F                 
09C3: 12              LD      (DE),A              
09C4: 1D              DEC     E                   
09C5: 3E 24           LD      A,$24               
09C7: 12              LD      (DE),A              
09C8: 18 17           JR      $9E1                ; {}
09CA: 1D              DEC     E                   
09CB: 12              LD      (DE),A              
09CC: 0D              DEC     C                   
09CD: 0E 1B           LD      C,$1B               
09CF: 0C              INC     C                   
09D0: 22 0A 15        LD      ($150A),HL          ; {}
09D3: 19              ADD     HL,DE               
09D4: 24              INC     H                   
09D5: 0E 0E           LD      C,$0E               
09D7: 1B              DEC     DE                  
09D8: 0F              RRCA                        
09D9: 21 D8 09        LD      HL,$09D8            
09DC: 01 09 00        LD      BC,$0009            
09DF: ED B8           LDDR                        
09E1: 3A 01 92        LD      A,($9201)           
09E4: A7              AND     A                   
09E5: C8              RET     Z                   
09E6: 3D              DEC     A                   
09E7: 20 16           JR      NZ,$9FF             ; {}
09E9: 3A B5 99        LD      A,($99B5)           
09EC: A7              AND     A                   
09ED: 28 10           JR      Z,$9FF              ; {}
09EF: 3E 02           LD      A,$02               
09F1: 32 01 92        LD      ($9201),A           
09F4: AF              XOR     A                   
09F5: 21 A0 9A        LD      HL,$9AA0            
09F8: 06 08           LD      B,$08               
09FA: DF              RST     0X18                
09FB: 2C              INC     L                   
09FC: 06 0F           LD      B,$0F               
09FE: DF              RST     0X18                
09FF: 3A B5 99        LD      A,($99B5)           
0A02: 4F              LD      C,A                 
0A03: 3A B8 99        LD      A,($99B8)           
0A06: 47              LD      B,A                 
0A07: 91              SUB     C                   
0A08: C8              RET     Z                   
0A09: 38 0F           JR      C,$A1A              ; {}
0A0B: 27              DAA                         
0A0C: 3D              DEC     A                   
0A0D: 32 B3 99        LD      ($99B3),A           
0A10: 79              LD      A,C                 
0A11: 32 B8 99        LD      ($99B8),A           
0A14: 3E 03           LD      A,$03               
0A16: 32 01 92        LD      ($9201),A           
0A19: C9              RET                         
0A1A: 79              LD      A,C                 
0A1B: 32 B8 99        LD      ($99B8),A           
0A1E: FE A0           CP      $A0                 
0A20: C8              RET     Z                   
0A21: 90              SUB     B                   
0A22: 27              DAA                         
0A23: 32 79 9A        LD      ($9A79),A           
0A26: C9              RET                         
0A27: 21 03 91        LD      HL,$9103            
0A2A: 06 05           LD      B,$05               
0A2C: 1A              LD      A,(DE)              
0A2D: 1C              INC     E                   
0A2E: FE 24           CP      $24                 
0A30: 20 01           JR      NZ,$A33             ; {}
0A32: AF              XOR     A                   
0A33: ED 67           RRD                         
0A35: CB 40           BIT     0,B                 
0A37: 20 01           JR      NZ,$A3A             ; {}
0A39: 2D              DEC     L                   
0A3A: 10 F0           DJNZ    $A2C                ; {}
0A3C: AF              XOR     A                   
0A3D: ED 67           RRD                         
0A3F: 2D              DEC     L                   
0A40: 36 00           LD      (HL),$00            
0A42: 2E 03           LD      L,$03               
0A44: 11 E5 99        LD      DE,$99E5            
0A47: 06 04           LD      B,$04               
0A49: A7              AND     A                   
0A4A: 1A              LD      A,(DE)              
0A4B: 8E              ADC     A,(HL)              
0A4C: 27              DAA                         
0A4D: 12              LD      (DE),A              
0A4E: 1D              DEC     E                   
0A4F: 2D              DEC     L                   
0A50: 10 F8           DJNZ    $A4A                ; {}
0A52: C9              RET                         
0A53: 06 01           LD      B,$01               
0A55: 25              DEC     H                   
0A56: 24              INC     H                   
0A57: 20 05           JR      NZ,$A5E             ; {}
0A59: 7D              LD      A,L                 
0A5A: FE 0A           CP      $0A                 
0A5C: 38 0A           JR      C,$A68              ; {}
0A5E: 3E 0A           LD      A,$0A               
0A60: CD 61 10        CALL    $1061               ; {}
0A63: F5              PUSH    AF                  
0A64: 04              INC     B                   
0A65: 18 EE           JR      $A55                ; {}
0A67: F1              POP     AF                  
0A68: CD 6E 0A        CALL    $0A6E               ; {}
0A6B: 10 FA           DJNZ    $A67                ; {}
0A6D: C9              RET                         
0A6E: 12              LD      (DE),A              
0A6F: C3 20 00        JP      $0020               ; {}
0A72: 2A 44 98        LD      HL,($9844)          
0A75: ED 5B 46 98     LD      DE,($9846)          
0A79: 7A              LD      A,D                 
0A7A: B3              OR      E                   
0A7B: 20 05           JR      NZ,$A82             ; {}
0A7D: 11 00 00        LD      DE,$0000            
0A80: 18 51           JR      $AD3                ; {}
0A82: CB 7A           BIT     7,D                 
0A84: 20 0A           JR      NZ,$A90             ; {}
0A86: CB 7C           BIT     7,H                 
0A88: 20 06           JR      NZ,$A90             ; {}
0A8A: 29              ADD     HL,HL               
0A8B: EB              EX      DE,HL               
0A8C: 29              ADD     HL,HL               
0A8D: EB              EX      DE,HL               
0A8E: 18 F2           JR      $A82                ; {}
0A90: 7A              LD      A,D                 
0A91: CD 61 10        CALL    $1061               ; {}
0A94: E5              PUSH    HL                  
0A95: 67              LD      H,A                 
0A96: 2E 00           LD      L,$00               
0A98: 7A              LD      A,D                 
0A99: CD 61 10        CALL    $1061               ; {}
0A9C: E3              EX      (SP),HL             
0A9D: 11 B0 99        LD      DE,$99B0            
0AA0: 06 04           LD      B,$04               
0AA2: 7C              LD      A,H                 
0AA3: 26 00           LD      H,$00               
0AA5: EB              EX      DE,HL               
0AA6: ED 6F           RLD                         
0AA8: CB 40           BIT     0,B                 
0AAA: 28 01           JR      Z,$AAD              ; {}
0AAC: 2C              INC     L                   
0AAD: EB              EX      DE,HL               
0AAE: CD 06 0B        CALL    $0B06               ; {}
0AB1: 08              EX      AF,AF'              
0AB2: E3              EX      (SP),HL             
0AB3: CD 06 0B        CALL    $0B06               ; {}
0AB6: E3              EX      (SP),HL             
0AB7: D7              RST     0X10                
0AB8: 08              EX      AF,AF'              
0AB9: 84              ADD     A,H                 
0ABA: 26 00           LD      H,$00               
0ABC: 10 E7           DJNZ    $AA5                ; {}
0ABE: D1              POP     DE                  
0ABF: FE 05           CP      $05                 
0AC1: 38 14           JR      C,$AD7              ; {}
0AC3: ED 5B B0 99     LD      DE,($99B0)          
0AC7: 7A              LD      A,D                 
0AC8: C6 01           ADD     $01                 
0ACA: 27              DAA                         
0ACB: 57              LD      D,A                 
0ACC: 30 05           JR      NC,$AD3             ; {}
0ACE: 7B              LD      A,E                 
0ACF: C6 01           ADD     $01                 
0AD1: 27              DAA                         
0AD2: 5F              LD      E,A                 
0AD3: ED 53 B0 99     LD      ($99B0),DE          
0AD7: 06 04           LD      B,$04               
0AD9: 0E 00           LD      C,$00               
0ADB: 21 B0 99        LD      HL,$99B0            
0ADE: 11 38 81        LD      DE,$8138            
0AE1: 05              DEC     B                   
0AE2: 20 04           JR      NZ,$AE8             ; {}
0AE4: 3E 2A           LD      A,$2A               
0AE6: 12              LD      (DE),A              
0AE7: E7              RST     0X20                
0AE8: 04              INC     B                   
0AE9: AF              XOR     A                   
0AEA: ED 6F           RLD                         
0AEC: CB 40           BIT     0,B                 
0AEE: 28 01           JR      Z,$AF1              ; {}
0AF0: 2C              INC     L                   
0AF1: A7              AND     A                   
0AF2: 20 04           JR      NZ,$AF8             ; {}
0AF4: CB 41           BIT     0,C                 
0AF6: 28 04           JR      Z,$AFC              ; {}
0AF8: CB C1           SET     0,C                 
0AFA: 12              LD      (DE),A              
0AFB: E7              RST     0X20                
0AFC: 78              LD      A,B                 
0AFD: FE 03           CP      $03                 
0AFF: 20 02           JR      NZ,$B03             ; {}
0B01: CB C1           SET     0,C                 
0B03: 10 DC           DJNZ    $AE1                ; {}
0B05: C9              RET                         
0B06: 3E 0A           LD      A,$0A               
0B08: CD 4E 10        CALL    $104E               ; {}
0B0B: 7C              LD      A,H                 
0B0C: 26 00           LD      H,$00               
0B0E: C9              RET                         
0B0F: FF              RST     0X38                
0B10: FF              RST     0X38                
0B11: FF              RST     0X38                
0B12: FF              RST     0X38                
0B13: FF              RST     0X38                
0B14: FF              RST     0X38                
0B15: FF              RST     0X38                
0B16: FF              RST     0X38                
0B17: FF              RST     0X38                
0B18: FF              RST     0X38                
0B19: FF              RST     0X38                
0B1A: FF              RST     0X38                
0B1B: FF              RST     0X38                
0B1C: FF              RST     0X38                
0B1D: FF              RST     0X38                
0B1E: FF              RST     0X38                
0B1F: FF              RST     0X38                
0B20: FF              RST     0X38                
0B21: FF              RST     0X38                
0B22: FF              RST     0X38                
0B23: FF              RST     0X38                
0B24: FF              RST     0X38                
0B25: FF              RST     0X38                
0B26: FF              RST     0X38                
0B27: FF              RST     0X38                
0B28: FF              RST     0X38                
0B29: FF              RST     0X38                
0B2A: FF              RST     0X38                
0B2B: FF              RST     0X38                
0B2C: FF              RST     0X38                
0B2D: FF              RST     0X38                
0B2E: FF              RST     0X38                
0B2F: FF              RST     0X38                
0B30: FF              RST     0X38                
0B31: FF              RST     0X38                
0B32: FF              RST     0X38                
0B33: FF              RST     0X38                
0B34: FF              RST     0X38                
0B35: FF              RST     0X38                
0B36: FF              RST     0X38                
0B37: FF              RST     0X38                
0B38: FF              RST     0X38                
0B39: FF              RST     0X38                
0B3A: FF              RST     0X38                
0B3B: FF              RST     0X38                
0B3C: FF              RST     0X38                
0B3D: FF              RST     0X38                
0B3E: FF              RST     0X38                
0B3F: FF              RST     0X38                
0B40: FF              RST     0X38                
0B41: FF              RST     0X38                
0B42: FF              RST     0X38                
0B43: FF              RST     0X38                
0B44: FF              RST     0X38                
0B45: FF              RST     0X38                
0B46: FF              RST     0X38                
0B47: FF              RST     0X38                
0B48: FF              RST     0X38                
0B49: FF              RST     0X38                
0B4A: FF              RST     0X38                
0B4B: FF              RST     0X38                
0B4C: FF              RST     0X38                
0B4D: FF              RST     0X38                
0B4E: FF              RST     0X38                
0B4F: FF              RST     0X38                
0B50: FF              RST     0X38                
0B51: FF              RST     0X38                
0B52: FF              RST     0X38                
0B53: FF              RST     0X38                
0B54: FF              RST     0X38                
0B55: FF              RST     0X38                
0B56: FF              RST     0X38                
0B57: FF              RST     0X38                
0B58: FF              RST     0X38                
0B59: FF              RST     0X38                
0B5A: FF              RST     0X38                
0B5B: FF              RST     0X38                
0B5C: FF              RST     0X38                
0B5D: FF              RST     0X38                
0B5E: FF              RST     0X38                
0B5F: FF              RST     0X38                
0B60: FF              RST     0X38                
0B61: FF              RST     0X38                
0B62: FF              RST     0X38                
0B63: FF              RST     0X38                
0B64: FF              RST     0X38                
0B65: FF              RST     0X38                
0B66: FF              RST     0X38                
0B67: FF              RST     0X38                
0B68: FF              RST     0X38                
0B69: FF              RST     0X38                
0B6A: FF              RST     0X38                
0B6B: FF              RST     0X38                
0B6C: FF              RST     0X38                
0B6D: FF              RST     0X38                
0B6E: FF              RST     0X38                
0B6F: FF              RST     0X38                
0B70: FF              RST     0X38                
0B71: FF              RST     0X38                
0B72: FF              RST     0X38                
0B73: FF              RST     0X38                
0B74: FF              RST     0X38                
0B75: FF              RST     0X38                
0B76: FF              RST     0X38                
0B77: FF              RST     0X38                
0B78: FF              RST     0X38                
0B79: FF              RST     0X38                
0B7A: FF              RST     0X38                
0B7B: FF              RST     0X38                
0B7C: FF              RST     0X38                
0B7D: FF              RST     0X38                
0B7E: FF              RST     0X38                
0B7F: FF              RST     0X38                
0B80: FF              RST     0X38                
0B81: FF              RST     0X38                
0B82: FF              RST     0X38                
0B83: FF              RST     0X38                
0B84: FF              RST     0X38                
0B85: FF              RST     0X38                
0B86: FF              RST     0X38                
0B87: FF              RST     0X38                
0B88: FF              RST     0X38                
0B89: FF              RST     0X38                
0B8A: FF              RST     0X38                
0B8B: FF              RST     0X38                
0B8C: FF              RST     0X38                
0B8D: FF              RST     0X38                
0B8E: FF              RST     0X38                
0B8F: FF              RST     0X38                
0B90: FF              RST     0X38                
0B91: FF              RST     0X38                
0B92: FF              RST     0X38                
0B93: FF              RST     0X38                
0B94: FF              RST     0X38                
0B95: FF              RST     0X38                
0B96: FF              RST     0X38                
0B97: FF              RST     0X38                
0B98: FF              RST     0X38                
0B99: FF              RST     0X38                
0B9A: FF              RST     0X38                
0B9B: FF              RST     0X38                
0B9C: FF              RST     0X38                
0B9D: FF              RST     0X38                
0B9E: FF              RST     0X38                
0B9F: FF              RST     0X38                
0BA0: FF              RST     0X38                
0BA1: FF              RST     0X38                
0BA2: FF              RST     0X38                
0BA3: FF              RST     0X38                
0BA4: FF              RST     0X38                
0BA5: FF              RST     0X38                
0BA6: FF              RST     0X38                
0BA7: FF              RST     0X38                
0BA8: FF              RST     0X38                
0BA9: FF              RST     0X38                
0BAA: FF              RST     0X38                
0BAB: FF              RST     0X38                
0BAC: FF              RST     0X38                
0BAD: FF              RST     0X38                
0BAE: FF              RST     0X38                
0BAF: FF              RST     0X38                
0BB0: FF              RST     0X38                
0BB1: FF              RST     0X38                
0BB2: FF              RST     0X38                
0BB3: FF              RST     0X38                
0BB4: FF              RST     0X38                
0BB5: FF              RST     0X38                
0BB6: FF              RST     0X38                
0BB7: FF              RST     0X38                
0BB8: FF              RST     0X38                
0BB9: FF              RST     0X38                
0BBA: FF              RST     0X38                
0BBB: FF              RST     0X38                
0BBC: FF              RST     0X38                
0BBD: FF              RST     0X38                
0BBE: FF              RST     0X38                
0BBF: FF              RST     0X38                
0BC0: FF              RST     0X38                
0BC1: FF              RST     0X38                
0BC2: FF              RST     0X38                
0BC3: FF              RST     0X38                
0BC4: FF              RST     0X38                
0BC5: FF              RST     0X38                
0BC6: FF              RST     0X38                
0BC7: FF              RST     0X38                
0BC8: FF              RST     0X38                
0BC9: FF              RST     0X38                
0BCA: FF              RST     0X38                
0BCB: FF              RST     0X38                
0BCC: FF              RST     0X38                
0BCD: FF              RST     0X38                
0BCE: FF              RST     0X38                
0BCF: FF              RST     0X38                
0BD0: FF              RST     0X38                
0BD1: FF              RST     0X38                
0BD2: FF              RST     0X38                
0BD3: FF              RST     0X38                
0BD4: FF              RST     0X38                
0BD5: FF              RST     0X38                
0BD6: FF              RST     0X38                
0BD7: FF              RST     0X38                
0BD8: FF              RST     0X38                
0BD9: FF              RST     0X38                
0BDA: FF              RST     0X38                
0BDB: FF              RST     0X38                
0BDC: FF              RST     0X38                
0BDD: FF              RST     0X38                
0BDE: FF              RST     0X38                
0BDF: FF              RST     0X38                
0BE0: FF              RST     0X38                
0BE1: FF              RST     0X38                
0BE2: FF              RST     0X38                
0BE3: FF              RST     0X38                
0BE4: FF              RST     0X38                
0BE5: FF              RST     0X38                
0BE6: FF              RST     0X38                
0BE7: FF              RST     0X38                
0BE8: FF              RST     0X38                
0BE9: FF              RST     0X38                
0BEA: FF              RST     0X38                
0BEB: FF              RST     0X38                
0BEC: FF              RST     0X38                
0BED: FF              RST     0X38                
0BEE: FF              RST     0X38                
0BEF: FF              RST     0X38                
0BF0: FF              RST     0X38                
0BF1: FF              RST     0X38                
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
0C00: FF              RST     0X38                
0C01: FF              RST     0X38                
0C02: FF              RST     0X38                
0C03: FF              RST     0X38                
0C04: FF              RST     0X38                
0C05: FF              RST     0X38                
0C06: FF              RST     0X38                
0C07: FF              RST     0X38                
0C08: FF              RST     0X38                
0C09: FF              RST     0X38                
0C0A: FF              RST     0X38                
0C0B: FF              RST     0X38                
0C0C: FF              RST     0X38                
0C0D: FF              RST     0X38                
0C0E: FF              RST     0X38                
0C0F: FF              RST     0X38                
0C10: FF              RST     0X38                
0C11: FF              RST     0X38                
0C12: FF              RST     0X38                
0C13: FF              RST     0X38                
0C14: FF              RST     0X38                
0C15: FF              RST     0X38                
0C16: FF              RST     0X38                
0C17: FF              RST     0X38                
0C18: FF              RST     0X38                
0C19: FF              RST     0X38                
0C1A: FF              RST     0X38                
0C1B: FF              RST     0X38                
0C1C: FF              RST     0X38                
0C1D: FF              RST     0X38                
0C1E: FF              RST     0X38                
0C1F: FF              RST     0X38                
0C20: FF              RST     0X38                
0C21: FF              RST     0X38                
0C22: FF              RST     0X38                
0C23: FF              RST     0X38                
0C24: FF              RST     0X38                
0C25: FF              RST     0X38                
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
0C40: FF              RST     0X38                
0C41: FF              RST     0X38                
0C42: FF              RST     0X38                
0C43: FF              RST     0X38                
0C44: FF              RST     0X38                
0C45: FF              RST     0X38                
0C46: FF              RST     0X38                
0C47: FF              RST     0X38                
0C48: FF              RST     0X38                
0C49: FF              RST     0X38                
0C4A: FF              RST     0X38                
0C4B: FF              RST     0X38                
0C4C: FF              RST     0X38                
0C4D: FF              RST     0X38                
0C4E: FF              RST     0X38                
0C4F: FF              RST     0X38                
0C50: FF              RST     0X38                
0C51: FF              RST     0X38                
0C52: FF              RST     0X38                
0C53: FF              RST     0X38                
0C54: FF              RST     0X38                
0C55: FF              RST     0X38                
0C56: FF              RST     0X38                
0C57: FF              RST     0X38                
0C58: FF              RST     0X38                
0C59: FF              RST     0X38                
0C5A: FF              RST     0X38                
0C5B: FF              RST     0X38                
0C5C: FF              RST     0X38                
0C5D: FF              RST     0X38                
0C5E: FF              RST     0X38                
0C5F: FF              RST     0X38                
0C60: FF              RST     0X38                
0C61: FF              RST     0X38                
0C62: FF              RST     0X38                
0C63: FF              RST     0X38                
0C64: FF              RST     0X38                
0C65: FF              RST     0X38                
0C66: FF              RST     0X38                
0C67: FF              RST     0X38                
0C68: FF              RST     0X38                
0C69: FF              RST     0X38                
0C6A: FF              RST     0X38                
0C6B: FF              RST     0X38                
0C6C: FF              RST     0X38                
0C6D: FF              RST     0X38                
0C6E: FF              RST     0X38                
0C6F: FF              RST     0X38                
0C70: FF              RST     0X38                
0C71: FF              RST     0X38                
0C72: FF              RST     0X38                
0C73: FF              RST     0X38                
0C74: FF              RST     0X38                
0C75: FF              RST     0X38                
0C76: FF              RST     0X38                
0C77: FF              RST     0X38                
0C78: FF              RST     0X38                
0C79: FF              RST     0X38                
0C7A: FF              RST     0X38                
0C7B: FF              RST     0X38                
0C7C: FF              RST     0X38                
0C7D: FF              RST     0X38                
0C7E: FF              RST     0X38                
0C7F: FF              RST     0X38                
0C80: FF              RST     0X38                
0C81: FF              RST     0X38                
0C82: FF              RST     0X38                
0C83: FF              RST     0X38                
0C84: FF              RST     0X38                
0C85: FF              RST     0X38                
0C86: FF              RST     0X38                
0C87: FF              RST     0X38                
0C88: FF              RST     0X38                
0C89: FF              RST     0X38                
0C8A: FF              RST     0X38                
0C8B: FF              RST     0X38                
0C8C: FF              RST     0X38                
0C8D: FF              RST     0X38                
0C8E: FF              RST     0X38                
0C8F: FF              RST     0X38                
0C90: FF              RST     0X38                
0C91: FF              RST     0X38                
0C92: FF              RST     0X38                
0C93: FF              RST     0X38                
0C94: FF              RST     0X38                
0C95: FF              RST     0X38                
0C96: FF              RST     0X38                
0C97: FF              RST     0X38                
0C98: FF              RST     0X38                
0C99: FF              RST     0X38                
0C9A: FF              RST     0X38                
0C9B: FF              RST     0X38                
0C9C: FF              RST     0X38                
0C9D: FF              RST     0X38                
0C9E: FF              RST     0X38                
0C9F: FF              RST     0X38                
0CA0: FF              RST     0X38                
0CA1: FF              RST     0X38                
0CA2: FF              RST     0X38                
0CA3: FF              RST     0X38                
0CA4: FF              RST     0X38                
0CA5: FF              RST     0X38                
0CA6: FF              RST     0X38                
0CA7: FF              RST     0X38                
0CA8: FF              RST     0X38                
0CA9: FF              RST     0X38                
0CAA: FF              RST     0X38                
0CAB: FF              RST     0X38                
0CAC: FF              RST     0X38                
0CAD: FF              RST     0X38                
0CAE: FF              RST     0X38                
0CAF: FF              RST     0X38                
0CB0: FF              RST     0X38                
0CB1: FF              RST     0X38                
0CB2: FF              RST     0X38                
0CB3: FF              RST     0X38                
0CB4: FF              RST     0X38                
0CB5: FF              RST     0X38                
0CB6: FF              RST     0X38                
0CB7: FF              RST     0X38                
0CB8: FF              RST     0X38                
0CB9: FF              RST     0X38                
0CBA: FF              RST     0X38                
0CBB: FF              RST     0X38                
0CBC: FF              RST     0X38                
0CBD: FF              RST     0X38                
0CBE: FF              RST     0X38                
0CBF: FF              RST     0X38                
0CC0: FF              RST     0X38                
0CC1: FF              RST     0X38                
0CC2: FF              RST     0X38                
0CC3: FF              RST     0X38                
0CC4: FF              RST     0X38                
0CC5: FF              RST     0X38                
0CC6: FF              RST     0X38                
0CC7: FF              RST     0X38                
0CC8: FF              RST     0X38                
0CC9: FF              RST     0X38                
0CCA: FF              RST     0X38                
0CCB: FF              RST     0X38                
0CCC: FF              RST     0X38                
0CCD: FF              RST     0X38                
0CCE: FF              RST     0X38                
0CCF: FF              RST     0X38                
0CD0: FF              RST     0X38                
0CD1: FF              RST     0X38                
0CD2: FF              RST     0X38                
0CD3: FF              RST     0X38                
0CD4: FF              RST     0X38                
0CD5: FF              RST     0X38                
0CD6: FF              RST     0X38                
0CD7: FF              RST     0X38                
0CD8: FF              RST     0X38                
0CD9: FF              RST     0X38                
0CDA: FF              RST     0X38                
0CDB: FF              RST     0X38                
0CDC: FF              RST     0X38                
0CDD: FF              RST     0X38                
0CDE: FF              RST     0X38                
0CDF: FF              RST     0X38                
0CE0: FF              RST     0X38                
0CE1: FF              RST     0X38                
0CE2: FF              RST     0X38                
0CE3: FF              RST     0X38                
0CE4: FF              RST     0X38                
0CE5: FF              RST     0X38                
0CE6: FF              RST     0X38                
0CE7: FF              RST     0X38                
0CE8: FF              RST     0X38                
0CE9: FF              RST     0X38                
0CEA: FF              RST     0X38                
0CEB: FF              RST     0X38                
0CEC: FF              RST     0X38                
0CED: FF              RST     0X38                
0CEE: FF              RST     0X38                
0CEF: FF              RST     0X38                
0CF0: FF              RST     0X38                
0CF1: FF              RST     0X38                
0CF2: FF              RST     0X38                
0CF3: FF              RST     0X38                
0CF4: FF              RST     0X38                
0CF5: FF              RST     0X38                
0CF6: FF              RST     0X38                
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
0D08: FF              RST     0X38                
0D09: FF              RST     0X38                
0D0A: FF              RST     0X38                
0D0B: FF              RST     0X38                
0D0C: FF              RST     0X38                
0D0D: FF              RST     0X38                
0D0E: FF              RST     0X38                
0D0F: FF              RST     0X38                
0D10: FF              RST     0X38                
0D11: FF              RST     0X38                
0D12: FF              RST     0X38                
0D13: FF              RST     0X38                
0D14: FF              RST     0X38                
0D15: FF              RST     0X38                
0D16: FF              RST     0X38                
0D17: FF              RST     0X38                
0D18: FF              RST     0X38                
0D19: FF              RST     0X38                
0D1A: FF              RST     0X38                
0D1B: FF              RST     0X38                
0D1C: FF              RST     0X38                
0D1D: FF              RST     0X38                
0D1E: FF              RST     0X38                
0D1F: FF              RST     0X38                
0D20: FF              RST     0X38                
0D21: FF              RST     0X38                
0D22: FF              RST     0X38                
0D23: FF              RST     0X38                
0D24: FF              RST     0X38                
0D25: FF              RST     0X38                
0D26: FF              RST     0X38                
0D27: FF              RST     0X38                
0D28: FF              RST     0X38                
0D29: FF              RST     0X38                
0D2A: FF              RST     0X38                
0D2B: FF              RST     0X38                
0D2C: FF              RST     0X38                
0D2D: FF              RST     0X38                
0D2E: FF              RST     0X38                
0D2F: FF              RST     0X38                
0D30: FF              RST     0X38                
0D31: FF              RST     0X38                
0D32: FF              RST     0X38                
0D33: FF              RST     0X38                
0D34: FF              RST     0X38                
0D35: FF              RST     0X38                
0D36: FF              RST     0X38                
0D37: FF              RST     0X38                
0D38: FF              RST     0X38                
0D39: FF              RST     0X38                
0D3A: FF              RST     0X38                
0D3B: FF              RST     0X38                
0D3C: FF              RST     0X38                
0D3D: FF              RST     0X38                
0D3E: FF              RST     0X38                
0D3F: FF              RST     0X38                
0D40: FF              RST     0X38                
0D41: FF              RST     0X38                
0D42: FF              RST     0X38                
0D43: FF              RST     0X38                
0D44: FF              RST     0X38                
0D45: FF              RST     0X38                
0D46: FF              RST     0X38                
0D47: FF              RST     0X38                
0D48: FF              RST     0X38                
0D49: FF              RST     0X38                
0D4A: FF              RST     0X38                
0D4B: FF              RST     0X38                
0D4C: FF              RST     0X38                
0D4D: FF              RST     0X38                
0D4E: FF              RST     0X38                
0D4F: FF              RST     0X38                
0D50: FF              RST     0X38                
0D51: FF              RST     0X38                
0D52: FF              RST     0X38                
0D53: FF              RST     0X38                
0D54: FF              RST     0X38                
0D55: FF              RST     0X38                
0D56: FF              RST     0X38                
0D57: FF              RST     0X38                
0D58: FF              RST     0X38                
0D59: FF              RST     0X38                
0D5A: FF              RST     0X38                
0D5B: FF              RST     0X38                
0D5C: FF              RST     0X38                
0D5D: FF              RST     0X38                
0D5E: FF              RST     0X38                
0D5F: FF              RST     0X38                
0D60: FF              RST     0X38                
0D61: FF              RST     0X38                
0D62: FF              RST     0X38                
0D63: FF              RST     0X38                
0D64: FF              RST     0X38                
0D65: FF              RST     0X38                
0D66: FF              RST     0X38                
0D67: FF              RST     0X38                
0D68: FF              RST     0X38                
0D69: FF              RST     0X38                
0D6A: FF              RST     0X38                
0D6B: FF              RST     0X38                
0D6C: FF              RST     0X38                
0D6D: FF              RST     0X38                
0D6E: FF              RST     0X38                
0D6F: FF              RST     0X38                
0D70: FF              RST     0X38                
0D71: FF              RST     0X38                
0D72: FF              RST     0X38                
0D73: FF              RST     0X38                
0D74: FF              RST     0X38                
0D75: FF              RST     0X38                
0D76: FF              RST     0X38                
0D77: FF              RST     0X38                
0D78: FF              RST     0X38                
0D79: FF              RST     0X38                
0D7A: FF              RST     0X38                
0D7B: FF              RST     0X38                
0D7C: FF              RST     0X38                
0D7D: FF              RST     0X38                
0D7E: FF              RST     0X38                
0D7F: FF              RST     0X38                
0D80: FF              RST     0X38                
0D81: FF              RST     0X38                
0D82: FF              RST     0X38                
0D83: FF              RST     0X38                
0D84: FF              RST     0X38                
0D85: FF              RST     0X38                
0D86: FF              RST     0X38                
0D87: FF              RST     0X38                
0D88: FF              RST     0X38                
0D89: FF              RST     0X38                
0D8A: FF              RST     0X38                
0D8B: FF              RST     0X38                
0D8C: FF              RST     0X38                
0D8D: FF              RST     0X38                
0D8E: FF              RST     0X38                
0D8F: FF              RST     0X38                
0D90: FF              RST     0X38                
0D91: FF              RST     0X38                
0D92: FF              RST     0X38                
0D93: FF              RST     0X38                
0D94: FF              RST     0X38                
0D95: FF              RST     0X38                
0D96: FF              RST     0X38                
0D97: FF              RST     0X38                
0D98: FF              RST     0X38                
0D99: FF              RST     0X38                
0D9A: FF              RST     0X38                
0D9B: FF              RST     0X38                
0D9C: FF              RST     0X38                
0D9D: FF              RST     0X38                
0D9E: FF              RST     0X38                
0D9F: FF              RST     0X38                
0DA0: FF              RST     0X38                
0DA1: FF              RST     0X38                
0DA2: FF              RST     0X38                
0DA3: FF              RST     0X38                
0DA4: FF              RST     0X38                
0DA5: FF              RST     0X38                
0DA6: FF              RST     0X38                
0DA7: FF              RST     0X38                
0DA8: FF              RST     0X38                
0DA9: FF              RST     0X38                
0DAA: FF              RST     0X38                
0DAB: FF              RST     0X38                
0DAC: FF              RST     0X38                
0DAD: FF              RST     0X38                
0DAE: FF              RST     0X38                
0DAF: FF              RST     0X38                
0DB0: FF              RST     0X38                
0DB1: FF              RST     0X38                
0DB2: FF              RST     0X38                
0DB3: FF              RST     0X38                
0DB4: FF              RST     0X38                
0DB5: FF              RST     0X38                
0DB6: FF              RST     0X38                
0DB7: FF              RST     0X38                
0DB8: FF              RST     0X38                
0DB9: FF              RST     0X38                
0DBA: FF              RST     0X38                
0DBB: FF              RST     0X38                
0DBC: FF              RST     0X38                
0DBD: FF              RST     0X38                
0DBE: FF              RST     0X38                
0DBF: FF              RST     0X38                
0DC0: FF              RST     0X38                
0DC1: FF              RST     0X38                
0DC2: FF              RST     0X38                
0DC3: FF              RST     0X38                
0DC4: FF              RST     0X38                
0DC5: FF              RST     0X38                
0DC6: FF              RST     0X38                
0DC7: FF              RST     0X38                
0DC8: FF              RST     0X38                
0DC9: FF              RST     0X38                
0DCA: FF              RST     0X38                
0DCB: FF              RST     0X38                
0DCC: FF              RST     0X38                
0DCD: FF              RST     0X38                
0DCE: FF              RST     0X38                
0DCF: FF              RST     0X38                
0DD0: FF              RST     0X38                
0DD1: FF              RST     0X38                
0DD2: FF              RST     0X38                
0DD3: FF              RST     0X38                
0DD4: FF              RST     0X38                
0DD5: FF              RST     0X38                
0DD6: FF              RST     0X38                
0DD7: FF              RST     0X38                
0DD8: FF              RST     0X38                
0DD9: FF              RST     0X38                
0DDA: FF              RST     0X38                
0DDB: FF              RST     0X38                
0DDC: FF              RST     0X38                
0DDD: FF              RST     0X38                
0DDE: FF              RST     0X38                
0DDF: FF              RST     0X38                
0DE0: FF              RST     0X38                
0DE1: FF              RST     0X38                
0DE2: FF              RST     0X38                
0DE3: FF              RST     0X38                
0DE4: FF              RST     0X38                
0DE5: FF              RST     0X38                
0DE6: FF              RST     0X38                
0DE7: FF              RST     0X38                
0DE8: FF              RST     0X38                
0DE9: FF              RST     0X38                
0DEA: FF              RST     0X38                
0DEB: FF              RST     0X38                
0DEC: FF              RST     0X38                
0DED: FF              RST     0X38                
0DEE: FF              RST     0X38                
0DEF: FF              RST     0X38                
0DF0: FF              RST     0X38                
0DF1: FF              RST     0X38                
0DF2: FF              RST     0X38                
0DF3: FF              RST     0X38                
0DF4: FF              RST     0X38                
0DF5: FF              RST     0X38                
0DF6: FF              RST     0X38                
0DF7: FF              RST     0X38                
0DF8: FF              RST     0X38                
0DF9: FF              RST     0X38                
0DFA: FF              RST     0X38                
0DFB: FF              RST     0X38                
0DFC: FF              RST     0X38                
0DFD: FF              RST     0X38                
0DFE: FF              RST     0X38                
0DFF: FF              RST     0X38                
0E00: FF              RST     0X38                
0E01: FF              RST     0X38                
0E02: FF              RST     0X38                
0E03: FF              RST     0X38                
0E04: FF              RST     0X38                
0E05: FF              RST     0X38                
0E06: FF              RST     0X38                
0E07: FF              RST     0X38                
0E08: FF              RST     0X38                
0E09: FF              RST     0X38                
0E0A: FF              RST     0X38                
0E0B: FF              RST     0X38                
0E0C: FF              RST     0X38                
0E0D: FF              RST     0X38                
0E0E: FF              RST     0X38                
0E0F: FF              RST     0X38                
0E10: FF              RST     0X38                
0E11: FF              RST     0X38                
0E12: FF              RST     0X38                
0E13: FF              RST     0X38                
0E14: FF              RST     0X38                
0E15: FF              RST     0X38                
0E16: FF              RST     0X38                
0E17: FF              RST     0X38                
0E18: FF              RST     0X38                
0E19: FF              RST     0X38                
0E1A: FF              RST     0X38                
0E1B: FF              RST     0X38                
0E1C: FF              RST     0X38                
0E1D: FF              RST     0X38                
0E1E: FF              RST     0X38                
0E1F: FF              RST     0X38                
0E20: FF              RST     0X38                
0E21: FF              RST     0X38                
0E22: FF              RST     0X38                
0E23: FF              RST     0X38                
0E24: FF              RST     0X38                
0E25: FF              RST     0X38                
0E26: FF              RST     0X38                
0E27: FF              RST     0X38                
0E28: FF              RST     0X38                
0E29: FF              RST     0X38                
0E2A: FF              RST     0X38                
0E2B: FF              RST     0X38                
0E2C: FF              RST     0X38                
0E2D: FF              RST     0X38                
0E2E: FF              RST     0X38                
0E2F: FF              RST     0X38                
0E30: FF              RST     0X38                
0E31: FF              RST     0X38                
0E32: FF              RST     0X38                
0E33: FF              RST     0X38                
0E34: FF              RST     0X38                
0E35: FF              RST     0X38                
0E36: FF              RST     0X38                
0E37: FF              RST     0X38                
0E38: FF              RST     0X38                
0E39: FF              RST     0X38                
0E3A: FF              RST     0X38                
0E3B: FF              RST     0X38                
0E3C: FF              RST     0X38                
0E3D: FF              RST     0X38                
0E3E: FF              RST     0X38                
0E3F: FF              RST     0X38                
0E40: FF              RST     0X38                
0E41: FF              RST     0X38                
0E42: FF              RST     0X38                
0E43: FF              RST     0X38                
0E44: FF              RST     0X38                
0E45: FF              RST     0X38                
0E46: FF              RST     0X38                
0E47: FF              RST     0X38                
0E48: FF              RST     0X38                
0E49: FF              RST     0X38                
0E4A: FF              RST     0X38                
0E4B: FF              RST     0X38                
0E4C: FF              RST     0X38                
0E4D: FF              RST     0X38                
0E4E: FF              RST     0X38                
0E4F: FF              RST     0X38                
0E50: FF              RST     0X38                
0E51: FF              RST     0X38                
0E52: FF              RST     0X38                
0E53: FF              RST     0X38                
0E54: FF              RST     0X38                
0E55: FF              RST     0X38                
0E56: FF              RST     0X38                
0E57: FF              RST     0X38                
0E58: FF              RST     0X38                
0E59: FF              RST     0X38                
0E5A: FF              RST     0X38                
0E5B: FF              RST     0X38                
0E5C: FF              RST     0X38                
0E5D: FF              RST     0X38                
0E5E: FF              RST     0X38                
0E5F: FF              RST     0X38                
0E60: FF              RST     0X38                
0E61: FF              RST     0X38                
0E62: FF              RST     0X38                
0E63: FF              RST     0X38                
0E64: FF              RST     0X38                
0E65: FF              RST     0X38                
0E66: FF              RST     0X38                
0E67: FF              RST     0X38                
0E68: FF              RST     0X38                
0E69: FF              RST     0X38                
0E6A: FF              RST     0X38                
0E6B: FF              RST     0X38                
0E6C: FF              RST     0X38                
0E6D: FF              RST     0X38                
0E6E: FF              RST     0X38                
0E6F: FF              RST     0X38                
0E70: FF              RST     0X38                
0E71: FF              RST     0X38                
0E72: FF              RST     0X38                
0E73: FF              RST     0X38                
0E74: FF              RST     0X38                
0E75: FF              RST     0X38                
0E76: FF              RST     0X38                
0E77: FF              RST     0X38                
0E78: FF              RST     0X38                
0E79: FF              RST     0X38                
0E7A: FF              RST     0X38                
0E7B: FF              RST     0X38                
0E7C: FF              RST     0X38                
0E7D: FF              RST     0X38                
0E7E: FF              RST     0X38                
0E7F: FF              RST     0X38                
0E80: FF              RST     0X38                
0E81: FF              RST     0X38                
0E82: FF              RST     0X38                
0E83: FF              RST     0X38                
0E84: FF              RST     0X38                
0E85: FF              RST     0X38                
0E86: FF              RST     0X38                
0E87: FF              RST     0X38                
0E88: FF              RST     0X38                
0E89: FF              RST     0X38                
0E8A: FF              RST     0X38                
0E8B: FF              RST     0X38                
0E8C: FF              RST     0X38                
0E8D: FF              RST     0X38                
0E8E: FF              RST     0X38                
0E8F: FF              RST     0X38                
0E90: FF              RST     0X38                
0E91: FF              RST     0X38                
0E92: FF              RST     0X38                
0E93: FF              RST     0X38                
0E94: FF              RST     0X38                
0E95: FF              RST     0X38                
0E96: FF              RST     0X38                
0E97: FF              RST     0X38                
0E98: FF              RST     0X38                
0E99: FF              RST     0X38                
0E9A: FF              RST     0X38                
0E9B: FF              RST     0X38                
0E9C: FF              RST     0X38                
0E9D: FF              RST     0X38                
0E9E: FF              RST     0X38                
0E9F: FF              RST     0X38                
0EA0: FF              RST     0X38                
0EA1: FF              RST     0X38                
0EA2: FF              RST     0X38                
0EA3: FF              RST     0X38                
0EA4: FF              RST     0X38                
0EA5: FF              RST     0X38                
0EA6: FF              RST     0X38                
0EA7: FF              RST     0X38                
0EA8: FF              RST     0X38                
0EA9: FF              RST     0X38                
0EAA: FF              RST     0X38                
0EAB: FF              RST     0X38                
0EAC: FF              RST     0X38                
0EAD: FF              RST     0X38                
0EAE: FF              RST     0X38                
0EAF: FF              RST     0X38                
0EB0: FF              RST     0X38                
0EB1: FF              RST     0X38                
0EB2: FF              RST     0X38                
0EB3: FF              RST     0X38                
0EB4: FF              RST     0X38                
0EB5: FF              RST     0X38                
0EB6: FF              RST     0X38                
0EB7: FF              RST     0X38                
0EB8: FF              RST     0X38                
0EB9: FF              RST     0X38                
0EBA: FF              RST     0X38                
0EBB: FF              RST     0X38                
0EBC: FF              RST     0X38                
0EBD: FF              RST     0X38                
0EBE: FF              RST     0X38                
0EBF: FF              RST     0X38                
0EC0: FF              RST     0X38                
0EC1: FF              RST     0X38                
0EC2: FF              RST     0X38                
0EC3: FF              RST     0X38                
0EC4: FF              RST     0X38                
0EC5: FF              RST     0X38                
0EC6: FF              RST     0X38                
0EC7: FF              RST     0X38                
0EC8: FF              RST     0X38                
0EC9: FF              RST     0X38                
0ECA: FF              RST     0X38                
0ECB: FF              RST     0X38                
0ECC: FF              RST     0X38                
0ECD: FF              RST     0X38                
0ECE: FF              RST     0X38                
0ECF: FF              RST     0X38                
0ED0: FF              RST     0X38                
0ED1: FF              RST     0X38                
0ED2: FF              RST     0X38                
0ED3: FF              RST     0X38                
0ED4: FF              RST     0X38                
0ED5: FF              RST     0X38                
0ED6: FF              RST     0X38                
0ED7: FF              RST     0X38                
0ED8: FF              RST     0X38                
0ED9: FF              RST     0X38                
0EDA: FF              RST     0X38                
0EDB: FF              RST     0X38                
0EDC: FF              RST     0X38                
0EDD: FF              RST     0X38                
0EDE: FF              RST     0X38                
0EDF: FF              RST     0X38                
0EE0: FF              RST     0X38                
0EE1: FF              RST     0X38                
0EE2: FF              RST     0X38                
0EE3: FF              RST     0X38                
0EE4: FF              RST     0X38                
0EE5: FF              RST     0X38                
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
0F00: FF              RST     0X38                
0F01: FF              RST     0X38                
0F02: FF              RST     0X38                
0F03: FF              RST     0X38                
0F04: FF              RST     0X38                
0F05: FF              RST     0X38                
0F06: FF              RST     0X38                
0F07: FF              RST     0X38                
0F08: FF              RST     0X38                
0F09: FF              RST     0X38                
0F0A: FF              RST     0X38                
0F0B: FF              RST     0X38                
0F0C: FF              RST     0X38                
0F0D: FF              RST     0X38                
0F0E: FF              RST     0X38                
0F0F: FF              RST     0X38                
0F10: FF              RST     0X38                
0F11: FF              RST     0X38                
0F12: FF              RST     0X38                
0F13: FF              RST     0X38                
0F14: FF              RST     0X38                
0F15: FF              RST     0X38                
0F16: FF              RST     0X38                
0F17: FF              RST     0X38                
0F18: FF              RST     0X38                
0F19: FF              RST     0X38                
0F1A: FF              RST     0X38                
0F1B: FF              RST     0X38                
0F1C: FF              RST     0X38                
0F1D: FF              RST     0X38                
0F1E: FF              RST     0X38                
0F1F: FF              RST     0X38                
0F20: FF              RST     0X38                
0F21: FF              RST     0X38                
0F22: FF              RST     0X38                
0F23: FF              RST     0X38                
0F24: FF              RST     0X38                
0F25: FF              RST     0X38                
0F26: FF              RST     0X38                
0F27: FF              RST     0X38                
0F28: FF              RST     0X38                
0F29: FF              RST     0X38                
0F2A: FF              RST     0X38                
0F2B: FF              RST     0X38                
0F2C: FF              RST     0X38                
0F2D: FF              RST     0X38                
0F2E: FF              RST     0X38                
0F2F: FF              RST     0X38                
0F30: FF              RST     0X38                
0F31: FF              RST     0X38                
0F32: FF              RST     0X38                
0F33: FF              RST     0X38                
0F34: FF              RST     0X38                
0F35: FF              RST     0X38                
0F36: FF              RST     0X38                
0F37: FF              RST     0X38                
0F38: FF              RST     0X38                
0F39: FF              RST     0X38                
0F3A: FF              RST     0X38                
0F3B: FF              RST     0X38                
0F3C: FF              RST     0X38                
0F3D: FF              RST     0X38                
0F3E: FF              RST     0X38                
0F3F: FF              RST     0X38                
0F40: FF              RST     0X38                
0F41: FF              RST     0X38                
0F42: FF              RST     0X38                
0F43: FF              RST     0X38                
0F44: FF              RST     0X38                
0F45: FF              RST     0X38                
0F46: FF              RST     0X38                
0F47: FF              RST     0X38                
0F48: FF              RST     0X38                
0F49: FF              RST     0X38                
0F4A: FF              RST     0X38                
0F4B: FF              RST     0X38                
0F4C: FF              RST     0X38                
0F4D: FF              RST     0X38                
0F4E: FF              RST     0X38                
0F4F: FF              RST     0X38                
0F50: FF              RST     0X38                
0F51: FF              RST     0X38                
0F52: FF              RST     0X38                
0F53: FF              RST     0X38                
0F54: FF              RST     0X38                
0F55: FF              RST     0X38                
0F56: FF              RST     0X38                
0F57: FF              RST     0X38                
0F58: FF              RST     0X38                
0F59: FF              RST     0X38                
0F5A: FF              RST     0X38                
0F5B: FF              RST     0X38                
0F5C: FF              RST     0X38                
0F5D: FF              RST     0X38                
0F5E: FF              RST     0X38                
0F5F: FF              RST     0X38                
0F60: FF              RST     0X38                
0F61: FF              RST     0X38                
0F62: FF              RST     0X38                
0F63: FF              RST     0X38                
0F64: FF              RST     0X38                
0F65: FF              RST     0X38                
0F66: FF              RST     0X38                
0F67: FF              RST     0X38                
0F68: FF              RST     0X38                
0F69: FF              RST     0X38                
0F6A: FF              RST     0X38                
0F6B: FF              RST     0X38                
0F6C: FF              RST     0X38                
0F6D: FF              RST     0X38                
0F6E: FF              RST     0X38                
0F6F: FF              RST     0X38                
0F70: FF              RST     0X38                
0F71: FF              RST     0X38                
0F72: FF              RST     0X38                
0F73: FF              RST     0X38                
0F74: FF              RST     0X38                
0F75: FF              RST     0X38                
0F76: FF              RST     0X38                
0F77: FF              RST     0X38                
0F78: FF              RST     0X38                
0F79: FF              RST     0X38                
0F7A: FF              RST     0X38                
0F7B: FF              RST     0X38                
0F7C: FF              RST     0X38                
0F7D: FF              RST     0X38                
0F7E: FF              RST     0X38                
0F7F: FF              RST     0X38                
0F80: FF              RST     0X38                
0F81: FF              RST     0X38                
0F82: FF              RST     0X38                
0F83: FF              RST     0X38                
0F84: FF              RST     0X38                
0F85: FF              RST     0X38                
0F86: FF              RST     0X38                
0F87: FF              RST     0X38                
0F88: FF              RST     0X38                
0F89: FF              RST     0X38                
0F8A: FF              RST     0X38                
0F8B: FF              RST     0X38                
0F8C: FF              RST     0X38                
0F8D: FF              RST     0X38                
0F8E: FF              RST     0X38                
0F8F: FF              RST     0X38                
0F90: FF              RST     0X38                
0F91: FF              RST     0X38                
0F92: FF              RST     0X38                
0F93: FF              RST     0X38                
0F94: FF              RST     0X38                
0F95: FF              RST     0X38                
0F96: FF              RST     0X38                
0F97: FF              RST     0X38                
0F98: FF              RST     0X38                
0F99: FF              RST     0X38                
0F9A: FF              RST     0X38                
0F9B: FF              RST     0X38                
0F9C: FF              RST     0X38                
0F9D: FF              RST     0X38                
0F9E: FF              RST     0X38                
0F9F: FF              RST     0X38                
0FA0: FF              RST     0X38                
0FA1: FF              RST     0X38                
0FA2: FF              RST     0X38                
0FA3: FF              RST     0X38                
0FA4: FF              RST     0X38                
0FA5: FF              RST     0X38                
0FA6: FF              RST     0X38                
0FA7: FF              RST     0X38                
0FA8: FF              RST     0X38                
0FA9: FF              RST     0X38                
0FAA: FF              RST     0X38                
0FAB: FF              RST     0X38                
0FAC: FF              RST     0X38                
0FAD: FF              RST     0X38                
0FAE: FF              RST     0X38                
0FAF: FF              RST     0X38                
0FB0: FF              RST     0X38                
0FB1: FF              RST     0X38                
0FB2: FF              RST     0X38                
0FB3: FF              RST     0X38                
0FB4: FF              RST     0X38                
0FB5: FF              RST     0X38                
0FB6: FF              RST     0X38                
0FB7: FF              RST     0X38                
0FB8: FF              RST     0X38                
0FB9: FF              RST     0X38                
0FBA: FF              RST     0X38                
0FBB: FF              RST     0X38                
0FBC: FF              RST     0X38                
0FBD: FF              RST     0X38                
0FBE: FF              RST     0X38                
0FBF: FF              RST     0X38                
0FC0: FF              RST     0X38                
0FC1: FF              RST     0X38                
0FC2: FF              RST     0X38                
0FC3: FF              RST     0X38                
0FC4: FF              RST     0X38                
0FC5: FF              RST     0X38                
0FC6: FF              RST     0X38                
0FC7: FF              RST     0X38                
0FC8: FF              RST     0X38                
0FC9: FF              RST     0X38                
0FCA: FF              RST     0X38                
0FCB: FF              RST     0X38                
0FCC: FF              RST     0X38                
0FCD: FF              RST     0X38                
0FCE: FF              RST     0X38                
0FCF: FF              RST     0X38                
0FD0: FF              RST     0X38                
0FD1: FF              RST     0X38                
0FD2: FF              RST     0X38                
0FD3: FF              RST     0X38                
0FD4: FF              RST     0X38                
0FD5: FF              RST     0X38                
0FD6: FF              RST     0X38                
0FD7: FF              RST     0X38                
0FD8: FF              RST     0X38                
0FD9: FF              RST     0X38                
0FDA: FF              RST     0X38                
0FDB: FF              RST     0X38                
0FDC: FF              RST     0X38                
0FDD: FF              RST     0X38                
0FDE: FF              RST     0X38                
0FDF: FF              RST     0X38                
0FE0: FF              RST     0X38                
0FE1: FF              RST     0X38                
0FE2: FF              RST     0X38                
0FE3: FF              RST     0X38                
0FE4: FF              RST     0X38                
0FE5: FF              RST     0X38                
0FE6: FF              RST     0X38                
0FE7: FF              RST     0X38                
0FE8: FF              RST     0X38                
0FE9: FF              RST     0X38                
0FEA: FF              RST     0X38                
0FEB: FF              RST     0X38                
0FEC: FF              RST     0X38                
0FED: FF              RST     0X38                
0FEE: FF              RST     0X38                
0FEF: FF              RST     0X38                
0FF0: FF              RST     0X38                
0FF1: FF              RST     0X38                
0FF2: FF              RST     0X38                
0FF3: FF              RST     0X38                
0FF4: FF              RST     0X38                
0FF5: FF              RST     0X38                
0FF6: FF              RST     0X38                
0FF7: FF              RST     0X38                
0FF8: FF              RST     0X38                
0FF9: FF              RST     0X38                
0FFA: FF              RST     0X38                
0FFB: FF              RST     0X38                
0FFC: FF              RST     0X38                
0FFD: FF              RST     0X38                
0FFE: FF              RST     0X38                
0FFF: 60              LD      H,B                 
1000: E5              PUSH    HL                  
1001: ED 5F           LD      A,R                 
1003: 67              LD      H,A                 
1004: 3A A0 92        LD      A,($92A0)           
1007: 84              ADD     A,H                 
1008: 6F              LD      L,A                 
1009: 26 01           LD      H,$01               
100B: 7E              LD      A,(HL)              
100C: 67              LD      H,A                 
100D: ED 5F           LD      A,R                 
100F: 84              ADD     A,H                 
1010: E1              POP     HL                  
1011: C9              RET                         
1012: C5              PUSH    BC                  
1013: D5              PUSH    DE                  
1014: 7B              LD      A,E                 
1015: 95              SUB     L                   
1016: 06 00           LD      B,$00               
1018: 30 04           JR      NC,$101E            ; {}
101A: CB C0           SET     0,B                 
101C: ED 44           NEG                         
101E: 4F              LD      C,A                 
101F: 7A              LD      A,D                 
1020: 94              SUB     H                   
1021: 30 0A           JR      NC,$102D            ; {}
1023: 57              LD      D,A                 
1024: 78              LD      A,B                 
1025: EE 01           XOR     $01                 
1027: F6 02           OR      $02                 
1029: 47              LD      B,A                 
102A: 7A              LD      A,D                 
102B: ED 44           NEG                         
102D: B9              CP      C                   
102E: F5              PUSH    AF                  
102F: 17              RLA                         
1030: A8              XOR     B                   
1031: 1F              RRA                         
1032: 3F              CCF                         
1033: CB 10           RL      B                   
1035: F1              POP     AF                  
1036: 30 03           JR      NC,$103B            ; {}
1038: 51              LD      D,C                 
1039: 4F              LD      C,A                 
103A: 7A              LD      A,D                 
103B: 61              LD      H,C                 
103C: 2E 00           LD      L,$00               
103E: CD 61 10        CALL    $1061               ; {}
1041: 7C              LD      A,H                 
1042: A8              XOR     B                   
1043: E6 01           AND     $01                 
1045: 28 03           JR      Z,$104A             ; {}
1047: 7D              LD      A,L                 
1048: 2F              CPL                         
1049: 6F              LD      L,A                 
104A: 60              LD      H,B                 
104B: D1              POP     DE                  
104C: C1              POP     BC                  
104D: C9              RET                         
104E: D5              PUSH    DE                  
104F: EB              EX      DE,HL               
1050: 21 00 00        LD      HL,$0000            
1053: CB 3F           SRL     A                   
1055: 30 01           JR      NC,$1058            ; {}
1057: 19              ADD     HL,DE               
1058: CB 23           SLA     E                   
105A: CB 12           RL      D                   
105C: A7              AND     A                   
105D: 20 F4           JR      NZ,$1053            ; {}
105F: D1              POP     DE                  
1060: C9              RET                         
1061: C5              PUSH    BC                  
1062: 4F              LD      C,A                 
1063: AF              XOR     A                   
1064: 06 11           LD      B,$11               
1066: 8F              ADC     A,A                 
1067: 38 0B           JR      C,$1074             ; {}
1069: B9              CP      C                   
106A: 38 01           JR      C,$106D             ; {}
106C: 91              SUB     C                   
106D: 3F              CCF                         
106E: ED 6A           ADC     HL,HL               
1070: 10 F4           DJNZ    $1066               ; {}
1072: C1              POP     BC                  
1073: C9              RET                         
1074: 91              SUB     C                   
1075: 37              SCF                         
1076: C3 6E 10        JP      $106E               ; {}
1079: 7D              LD      A,L                 
107A: E6 80           AND     $80                 
107C: 3C              INC     A                   
107D: 08              EX      AF,AF'              
107E: CB BD           RES     7,L                 
1080: C3 8A 10        JP      $108A               ; {}
1083: 7D              LD      A,L                 
1084: 0F              RRCA                        
1085: 0F              RRCA                        
1086: E6 80           AND     $80                 
1088: 3C              INC     A                   
1089: 08              EX      AF,AF'              
108A: D5              PUSH    DE                  
108B: 11 14 00        LD      DE,$0014            
108E: 06 0C           LD      B,$0C               
1090: DD 21 00 91     LD      IX,$9100            
1094: DD CB 13 46     BIT     0,(IX+$13)          
1098: 28 06           JR      Z,$10A0             ; {}
109A: DD 19           ADD     IX,DE               
109C: 10 F6           DJNZ    $1094               ; {}
109E: D1              POP     DE                  
109F: C9              RET                         
10A0: D1              POP     DE                  
10A1: DD 73 08        LD      (IX+$08),E          
10A4: DD 72 09        LD      (IX+$09),D          
10A7: DD 36 0D 01     LD      (IX+$0D),$01        
10AB: DD 36 04 00     LD      (IX+$04),$00        
10AF: DD 36 05 01     LD      (IX+$05),$01        
10B3: 4D              LD      C,L                 
10B4: DD 71 10        LD      (IX+$10),C          
10B7: 08              EX      AF,AF'              
10B8: 57              LD      D,A                 
10B9: 36 09           LD      (HL),$09            
10BB: DD 7D           LD      A,IXL               
10BD: 2C              INC     L                   
10BE: 77              LD      (HL),A              
10BF: 3A 15 92        LD      A,($9215)           
10C2: 5F              LD      E,A                 
10C3: 69              LD      L,C                 
10C4: 26 93           LD      H,$93               
10C6: 4E              LD      C,(HL)              
10C7: 2C              INC     L                   
10C8: 46              LD      B,(HL)              
10C9: 26 9B           LD      H,$9B               
10CB: 7E              LD      A,(HL)              
10CC: 0F              RRCA                        
10CD: CB 18           RR      B                   
10CF: CB 43           BIT     0,E                 
10D1: 20 09           JR      NZ,$10DC            ; {}
10D3: 08              EX      AF,AF'              
10D4: 78              LD      A,B                 
10D5: C6 50           ADD     $50                 
10D7: ED 44           NEG                         
10D9: 47              LD      B,A                 
10DA: 08              EX      AF,AF'              
10DB: 3F              CCF                         
10DC: DD 70 01        LD      (IX+$01),B          
10DF: 1F              RRA                         
10E0: E6 80           AND     $80                 
10E2: DD 77 00        LD      (IX+$00),A          
10E5: 79              LD      A,C                 
10E6: CB 43           BIT     0,E                 
10E8: 28 03           JR      Z,$10ED             ; {}
10EA: C6 0D           ADD     $0D                 
10EC: 2F              CPL                         
10ED: CB 3F           SRL     A                   
10EF: DD 77 03        LD      (IX+$03),A          
10F2: 1F              RRA                         
10F3: E6 80           AND     $80                 
10F5: DD 77 02        LD      (IX+$02),A          
10F8: DD 72 13        LD      (IX+$13),D          
10FB: DD 36 0E 1E     LD      (IX+$0E),$1E        
10FF: 3A 0B 92        LD      A,($920B)           
1102: A7              AND     A                   
1103: 28 03           JR      Z,$1108             ; {}
1105: 3A C8 92        LD      A,($92C8)           
1108: DD 77 0F        LD      (IX+$0F),A          
110B: C9              RET                         
110C: 3E 1F           LD      A,$1F               
110E: 32 00 90        LD      ($9000),A           
1111: 32 E0 98        LD      ($98E0),A           
1114: 21 20 98        LD      HL,$9820            
1117: 11 60 98        LD      DE,$9860            
111A: 06 40           LD      B,$40               
111C: 4E              LD      C,(HL)              
111D: 1A              LD      A,(DE)              
111E: 77              LD      (HL),A              
111F: 79              LD      A,C                 
1120: 12              LD      (DE),A              
1121: 2C              INC     L                   
1122: 1C              INC     E                   
1123: 10 F7           DJNZ    $111C               ; {}
1125: 21 00 88        LD      HL,$8800            
1128: 11 B0 98        LD      DE,$98B0            
112B: 06 30           LD      B,$30               
112D: 7E              LD      A,(HL)              
112E: 4F              LD      C,A                 
112F: 26 8B           LD      H,$8B               
1131: 7E              LD      A,(HL)              
1132: E6 7F           AND     $7F                 
1134: 0D              DEC     C                   
1135: 20 0B           JR      NZ,$1142            ; {}
1137: E6 78           AND     $78                 
1139: 4F              LD      C,A                 
113A: 2C              INC     L                   
113B: 7E              LD      A,(HL)              
113C: 2D              DEC     L                   
113D: E6 07           AND     $07                 
113F: B1              OR      C                   
1140: F6 80           OR      $80                 
1142: EB              EX      DE,HL               
1143: 4E              LD      C,(HL)              
1144: 77              LD      (HL),A              
1145: EB              EX      DE,HL               
1146: CB 79           BIT     7,C                 
1148: 28 10           JR      Z,$115A             ; {}
114A: 79              LD      A,C                 
114B: E6 78           AND     $78                 
114D: C6 06           ADD     $06                 
114F: 77              LD      (HL),A              
1150: 2C              INC     L                   
1151: 79              LD      A,C                 
1152: E6 07           AND     $07                 
1154: 77              LD      (HL),A              
1155: 2D              DEC     L                   
1156: 3E 01           LD      A,$01               
1158: 18 07           JR      $1161               ; {}
115A: 71              LD      (HL),C              
115B: 26 93           LD      H,$93               
115D: 36 00           LD      (HL),$00            
115F: 3E 80           LD      A,$80               
1161: 26 88           LD      H,$88               
1163: 77              LD      (HL),A              
1164: 13              INC     DE                  
1165: 2C              INC     L                   
1166: 2C              INC     L                   
1167: 10 C4           DJNZ    $112D               ; {}
1169: 21 00 90        LD      HL,$9000            
116C: 11 E0 98        LD      DE,$98E0            
116F: 06 20           LD      B,$20               
1171: 4E              LD      C,(HL)              
1172: 1A              LD      A,(DE)              
1173: 77              LD      (HL),A              
1174: 79              LD      A,C                 
1175: 12              LD      (DE),A              
1176: 2C              INC     L                   
1177: 1C              INC     E                   
1178: 10 F7           DJNZ    $1171               ; {}
117A: AF              XOR     A                   
117B: 32 00 90        LD      ($9000),A           
117E: C9              RET                         
117F: 21 02 80        LD      HL,$8002            
1182: 06 12           LD      B,$12               
1184: 7E              LD      A,(HL)              
1185: FE 4A           CP      $4A                 
1187: 30 02           JR      NC,$118B            ; {}
1189: 36 24           LD      (HL),$24            
118B: 2C              INC     L                   
118C: 10 F6           DJNZ    $1184               ; {}
118E: 2E 22           LD      L,$22               
1190: 06 12           LD      B,$12               
1192: 7E              LD      A,(HL)              
1193: FE 4A           CP      $4A                 
1195: 30 02           JR      NC,$1199            ; {}
1197: 36 24           LD      (HL),$24            
1199: 2C              INC     L                   
119A: 10 F6           DJNZ    $1192               ; {}
119C: 3A 21 98        LD      A,($9821)           
119F: 06 00           LD      B,$00               
11A1: 21 01 80        LD      HL,$8001            
11A4: FE 32           CP      $32                 
11A6: 38 07           JR      C,$11AF             ; {}
11A8: D6 32           SUB     $32                 
11AA: 04              INC     B                   
11AB: 2C              INC     L                   
11AC: 2C              INC     L                   
11AD: 18 F5           JR      $11A4               ; {}
11AF: EB              EX      DE,HL               
11B0: 6F              LD      L,A                 
11B1: 26 00           LD      H,$00               
11B3: 3E 0A           LD      A,$0A               
11B5: CD 61 10        CALL    $1061               ; {}
11B8: 67              LD      H,A                 
11B9: E5              PUSH    HL                  
11BA: EB              EX      DE,HL               
11BB: FE 05           CP      $05                 
11BD: 38 02           JR      C,$11C1             ; {}
11BF: D6 04           SUB     $04                 
11C1: 4F              LD      C,A                 
11C2: 7B              LD      A,E                 
11C3: CB 47           BIT     0,A                 
11C5: 28 02           JR      Z,$11C9             ; {}
11C7: 3E 02           LD      A,$02               
11C9: 81              ADD     A,C                 
11CA: D7              RST     0X10                
11CB: 04              INC     B                   
11CC: 10 20           DJNZ    $11EE               ; {}
11CE: C1              POP     BC                  
11CF: 79              LD      A,C                 
11D0: CD F5 11        CALL    $11F5               ; {}
11D3: 78              LD      A,B                 
11D4: FE 05           CP      $05                 
11D6: 38 08           JR      C,$11E0             ; {}
11D8: 16 38           LD      D,$38               
11DA: CD 13 12        CALL    $1213               ; {}
11DD: 78              LD      A,B                 
11DE: D6 05           SUB     $05                 
11E0: 47              LD      B,A                 
11E1: 04              INC     B                   
11E2: 10 03           DJNZ    $11E7               ; {}
11E4: C3 7E 13        JP      $137E               ; {}
11E7: 16 36           LD      D,$36               
11E9: CD 13 12        CALL    $1213               ; {}
11EC: 18 F4           JR      $11E2               ; {}
11EE: 3E 04           LD      A,$04               
11F0: CD FB 11        CALL    $11FB               ; {}
11F3: 18 D7           JR      $11CC               ; {}
11F5: A7              AND     A                   
11F6: C8              RET     Z                   
11F7: FE 04           CP      $04                 
11F9: 28 07           JR      Z,$1202             ; {}
11FB: 07              RLCA                        
11FC: 07              RLCA                        
11FD: C6 36           ADD     $36                 
11FF: 57              LD      D,A                 
1200: 18 0A           JR      $120C               ; {}
1202: 16 42           LD      D,$42               
1204: CD 13 12        CALL    $1213               ; {}
1207: CD 28 12        CALL    $1228               ; {}
120A: 16 3A           LD      D,$3A               
120C: CD 13 12        CALL    $1213               ; {}
120F: CD 28 12        CALL    $1228               ; {}
1212: C9              RET                         
1213: 08              EX      AF,AF'              
1214: 38 11           JR      C,$1227             ; {}
1216: 08              EX      AF,AF'              
1217: 3A A0 92        LD      A,($92A0)           
121A: C6 08           ADD     $08                 
121C: 5F              LD      E,A                 
121D: 3A A0 92        LD      A,($92A0)           
1220: 93              SUB     E                   
1221: 20 FA           JR      NZ,$121D            ; {}
1223: 08              EX      AF,AF'              
1224: 32 B5 9A        LD      ($9AB5),A           
1227: 08              EX      AF,AF'              
1228: 72              LD      (HL),D              
1229: 14              INC     D                   
122A: CB ED           SET     5,L                 
122C: 72              LD      (HL),D              
122D: 14              INC     D                   
122E: CB D4           SET     2,H                 
1230: 7A              LD      A,D                 
1231: E6 0C           AND     $0C                 
1233: FE 08           CP      $08                 
1235: 3E 01           LD      A,$01               
1237: 28 01           JR      Z,$123A             ; {}
1239: 3C              INC     A                   
123A: 77              LD      (HL),A              
123B: CB AD           RES     5,L                 
123D: 77              LD      (HL),A              
123E: CB 94           RES     2,H                 
1240: 2D              DEC     L                   
1241: C9              RET                         
1242: 21 5B 12        LD      HL,$125B            
1245: 11 00 90        LD      DE,$9000            
1248: 01 20 00        LD      BC,$0020            
124B: C5              PUSH    BC                  
124C: E5              PUSH    HL                  
124D: ED B0           LDIR                        
124F: E1              POP     HL                  
1250: C1              POP     BC                  
1251: 11 E0 98        LD      DE,$98E0            
1254: ED B0           LDIR                        
1256: AF              XOR     A                   
1257: 32 00 90        LD      ($9000),A           
125A: C9              RET                         
125B: 1F              RRA                         
125C: 01 00 00        LD      BC,$0000            
125F: 00              NOP                         
1260: 01 00 00        LD      BC,$0000            
1263: 00              NOP                         
1264: 00              NOP                         
1265: 00              NOP                         
1266: 00              NOP                         
1267: 01 01 00        LD      BC,$0001            
126A: 01 00 00        LD      BC,$0000            
126D: 00              NOP                         
126E: 00              NOP                         
126F: 00              NOP                         
1270: 00              NOP                         
1271: 00              NOP                         
1272: 01 00 00        LD      BC,$0000            
1275: 00              NOP                         
1276: 00              NOP                         
1277: 00              NOP                         
1278: 00              NOP                         
1279: 00              NOP                         
127A: 0A              LD      A,(BC)              
127B: 21 64 8B        LD      HL,$8B64            
127E: 11 30 09        LD      DE,$0930            
1281: 0E 00           LD      C,$00               
1283: 06 0A           LD      B,$0A               
1285: 73              LD      (HL),E              
1286: 26 93           LD      H,$93               
1288: 36 00           LD      (HL),$00            
128A: 26 9B           LD      H,$9B               
128C: 71              LD      (HL),C              
128D: 26 8B           LD      H,$8B               
128F: 2C              INC     L                   
1290: 72              LD      (HL),D              
1291: 2C              INC     L                   
1292: 78              LD      A,B                 
1293: FE 09           CP      $09                 
1295: 20 04           JR      NZ,$129B            ; {}
1297: 0E 01           LD      C,$01               
1299: 16 0B           LD      D,$0B               
129B: 10 E8           DJNZ    $1285               ; {}
129D: C9              RET                         
129E: 26 8B           LD      H,$8B               
12A0: ED 5B 80 92     LD      DE,($9280)          
12A4: 1A              LD      A,(DE)              
12A5: 6F              LD      L,A                 
12A6: 13              INC     DE                  
12A7: 1A              LD      A,(DE)              
12A8: 4F              LD      C,A                 
12A9: E6 78           AND     $78                 
12AB: C6 06           ADD     $06                 
12AD: 77              LD      (HL),A              
12AE: 2C              INC     L                   
12AF: 79              LD      A,C                 
12B0: E6 07           AND     $07                 
12B2: CB 79           BIT     7,C                 
12B4: 28 02           JR      Z,$12B8             ; {}
12B6: F6 08           OR      $08                 
12B8: 77              LD      (HL),A              
12B9: 13              INC     DE                  
12BA: 2D              DEC     L                   
12BB: 26 88           LD      H,$88               
12BD: 36 01           LD      (HL),$01            
12BF: 26 93           LD      H,$93               
12C1: 1A              LD      A,(DE)              
12C2: 77              LD      (HL),A              
12C3: 13              INC     DE                  
12C4: 2C              INC     L                   
12C5: 1A              LD      A,(DE)              
12C6: CB 27           SLA     A                   
12C8: 77              LD      (HL),A              
12C9: 3E 00           LD      A,$00               
12CB: 17              RLA                         
12CC: 26 9B           LD      H,$9B               
12CE: 77              LD      (HL),A              
12CF: 13              INC     DE                  
12D0: ED 53 80 92     LD      ($9280),DE          
12D4: C9              RET                         
12D5: DD 6F           LD      IXL,A               
12D7: 3A 15 92        LD      A,($9215)           
12DA: 4F              LD      C,A                 
12DB: 21 00 99        LD      HL,$9900            
12DE: 11 21 13        LD      DE,$1321            
12E1: 06 10           LD      B,$10               
12E3: 36 00           LD      (HL),$00            
12E5: 2C              INC     L                   
12E6: 1A              LD      A,(DE)              
12E7: 13              INC     DE                  
12E8: 77              LD      (HL),A              
12E9: 2C              INC     L                   
12EA: 10 F7           DJNZ    $12E3               ; {}
12EC: 21 00 98        LD      HL,$9800            
12EF: 11 21 13        LD      DE,$1321            
12F2: 06 0A           LD      B,$0A               
12F4: 1A              LD      A,(DE)              
12F5: 13              INC     DE                  
12F6: CB 41           BIT     0,C                 
12F8: 28 03           JR      Z,$12FD             ; {}
12FA: C6 0D           ADD     $0D                 
12FC: 2F              CPL                         
12FD: 77              LD      (HL),A              
12FE: 2C              INC     L                   
12FF: 2C              INC     L                   
1300: 10 F2           DJNZ    $12F4               ; {}
1302: 06 06           LD      B,$06               
1304: 1A              LD      A,(DE)              
1305: DD 85           ADD     A,IXL               
1307: 13              INC     DE                  
1308: CB 41           BIT     0,C                 
130A: 20 03           JR      NZ,$130F            ; {}
130C: C6 4F           ADD     $4F                 
130E: 2F              CPL                         
130F: CB 27           SLA     A                   
1311: 77              LD      (HL),A              
1312: 2C              INC     L                   
1313: 3E 00           LD      A,$00               
1315: 17              RLA                         
1316: 77              LD      (HL),A              
1317: 2C              INC     L                   
1318: 10 EA           DJNZ    $1304               ; {}
131A: 3A 15 92        LD      A,($9215)           
131D: 32 0F 92        LD      ($920F),A           
1320: C9              RET                         
1321: 31 41 51        LD      SP,$5141            
1324: 61              LD      H,C                 
1325: 71              LD      (HL),C              
1326: 81              ADD     A,C                 
1327: 91              SUB     C                   
1328: A1              AND     C                   
1329: B1              OR      C                   
132A: C1              POP     BC                  
132B: 92              SUB     D                   
132C: 8A              ADC     A,D                 
132D: 82              ADD     A,D                 
132E: 7C              LD      A,H                 
132F: 76              HALT                        
1330: 70              LD      (HL),B              
1331: E5              PUSH    HL                  
1332: 21 AF 92        LD      HL,$92AF            
1335: 36 03           LD      (HL),$03            
1337: 7E              LD      A,(HL)              
1338: A7              AND     A                   
1339: 20 FC           JR      NZ,$1337            ; {}
133B: E1              POP     HL                  
133C: C9              RET                         
133D: 3E 01           LD      A,$01               
133F: 32 14 90        LD      ($9014),A           
1342: 3A 70 82        LD      A,($8270)           
1345: FE 24           CP      $24                 
1347: 20 03           JR      NZ,$134C            ; {}
1349: 0E 03           LD      C,$03               
134B: F7              RST     0X30                
134C: 3A 87 92        LD      A,($9287)           
134F: A7              AND     A                   
1350: 20 FA           JR      NZ,$134C            ; {}
1352: CD 7E 13        CALL    $137E               ; {}
1355: 21 06 09        LD      HL,$0906            
1358: 22 62 8B        LD      ($8B62),HL          
135B: 21 62 93        LD      HL,$9362            
135E: 3A 15 92        LD      A,($9215)           
1361: E6 01           AND     $01                 
1363: 3E 29           LD      A,$29               
1365: 0E 01           LD      C,$01               
1367: 28 03           JR      Z,$136C             ; {}
1369: C6 0E           ADD     $0E                 
136B: 0D              DEC     C                   
136C: 36 7A           LD      (HL),$7A            
136E: 2C              INC     L                   
136F: 77              LD      (HL),A              
1370: 26 9B           LD      H,$9B               
1372: 71              LD      (HL),C              
1373: 2D              DEC     L                   
1374: AF              XOR     A                   
1375: 77              LD      (HL),A              
1376: 32 13 92        LD      ($9213),A           
1379: 3C              INC     A                   
137A: 32 B9 99        LD      ($99B9),A           
137D: C9              RET                         
137E: 3A 20 98        LD      A,($9820)           
1381: 2F              CPL                         
1382: C6 09           ADD     $09                 
1384: 5F              LD      E,A                 
1385: 16 49           LD      D,$49               
1387: 21 1D 80        LD      HL,$801D            
138A: CD 98 13        CALL    $1398               ; {}
138D: 2D              DEC     L                   
138E: CD 98 13        CALL    $1398               ; {}
1391: CB ED           SET     5,L                 
1393: 2C              INC     L                   
1394: CD 98 13        CALL    $1398               ; {}
1397: 2D              DEC     L                   
1398: E5              PUSH    HL                  
1399: 14              INC     D                   
139A: 4A              LD      C,D                 
139B: 06 08           LD      B,$08               
139D: 78              LD      A,B                 
139E: BB              CP      E                   
139F: 20 02           JR      NZ,$13A3            ; {}
13A1: 0E 24           LD      C,$24               
13A3: 7E              LD      A,(HL)              
13A4: FE 36           CP      $36                 
13A6: 38 04           JR      C,$13AC             ; {}
13A8: FE 4A           CP      $4A                 
13AA: 38 01           JR      C,$13AD             ; {}
13AC: 71              LD      (HL),C              
13AD: 2D              DEC     L                   
13AE: 2D              DEC     L                   
13AF: 10 EC           DJNZ    $139D               ; {}
13B1: E1              POP     HL                  
13B2: C9              RET                         
13B3: A7              AND     A                   
13B4: 08              EX      AF,AF'              
13B5: D5              PUSH    DE                  
13B6: EB              EX      DE,HL               
13B7: 79              LD      A,C                 
13B8: 21 EF 13        LD      HL,$13EF            
13BB: CF              RST     0X08                
13BC: 7E              LD      A,(HL)              
13BD: 23              INC     HL                  
13BE: 66              LD      H,(HL)              
13BF: 6F              LD      L,A                 
13C0: 08              EX      AF,AF'              
13C1: 30 06           JR      NC,$13C9            ; {}
13C3: 2B              DEC     HL                  
13C4: 2B              DEC     HL                  
13C5: 5E              LD      E,(HL)              
13C6: 23              INC     HL                  
13C7: 56              LD      D,(HL)              
13C8: 23              INC     HL                  
13C9: 4E              LD      C,(HL)              
13CA: 23              INC     HL                  
13CB: EB              EX      DE,HL               
13CC: 1A              LD      A,(DE)              
13CD: FE 2F           CP      $2F                 
13CF: 28 1E           JR      Z,$13EF             ; {}
13D1: D6 30           SUB     $30                 
13D3: 30 04           JR      NC,$13D9            ; {}
13D5: 3E 24           LD      A,$24               
13D7: 18 06           JR      $13DF               ; {}
13D9: FE 11           CP      $11                 
13DB: 38 02           JR      C,$13DF             ; {}
13DD: D6 07           SUB     $07                 
13DF: 77              LD      (HL),A              
13E0: CB D4           SET     2,H                 
13E2: 71              LD      (HL),C              
13E3: CB 94           RES     2,H                 
13E5: 13              INC     DE                  
13E6: 7D              LD      A,L                 
13E7: D6 20           SUB     $20                 
13E9: 6F              LD      L,A                 
13EA: 30 E0           JR      NC,$13CC            ; {}
13EC: 25              DEC     H                   
13ED: 18 DD           JR      $13CC               ; {}
13EF: D1              POP     DE                  
13F0: C9              RET                         
13F1: 2F              CPL                         
13F2: 14              INC     D                   
13F3: 44              LD      B,H                 
13F4: 14              INC     D                   
13F5: 51              LD      D,C                 
13F6: 14              INC     D                   
13F7: 5C              LD      E,H                 
13F8: 14              INC     D                   
13F9: 66              LD      H,(HL)              
13FA: 14              INC     D                   
13FB: 72              LD      (HL),D              
13FC: 14              INC     D                   
13FD: 7C              LD      A,H                 
13FE: 14              INC     D                   
13FF: 91              SUB     C                   
1400: 14              INC     D                   
1401: A3              AND     E                   
1402: 14              INC     D                   
1403: AE              XOR     (HL)                
1404: 14              INC     D                   
1405: C2 14 E1        JP      NZ,$E114            
1408: 14              INC     D                   
1409: EE 14           XOR     $14                 
140B: 09              ADD     HL,BC               
140C: 15              DEC     D                   
140D: 13              INC     DE                  
140E: 15              DEC     D                   
140F: 22 15 2F        LD      ($2F15),HL          ; {}
1412: 15              DEC     D                   
1413: 3C              INC     A                   
1414: 15              DEC     D                   
1415: 40              LD      B,B                 
1416: 15              DEC     D                   
1417: 59              LD      E,C                 
1418: 15              DEC     D                   
1419: 5D              LD      E,L                 
141A: 15              DEC     D                   
141B: 6A              LD      L,D                 
141C: 15              DEC     D                   
141D: 81              ADD     A,C                 
141E: 15              DEC     D                   
141F: 8F              ADC     A,A                 
1420: 15              DEC     D                   
1421: A8              XOR     B                   
1422: 15              DEC     D                   
1423: BF              CP      A                   
1424: 15              DEC     D                   
1425: C5              PUSH    BC                  
1426: 15              DEC     D                   
1427: D9              EXX                         
1428: 15              DEC     D                   
1429: ED                                 
142A: 15              DEC     D                   
142B: FF              RST     0X38                
142C: 15              DEC     D                   
142D: EB              EX      DE,HL               
142E: 82              ADD     A,D                 
142F: 00              NOP                         
1430: 50              LD      D,B                 
1431: 55              LD      D,L                 
1432: 53              LD      D,E                 
1433: 48              LD      C,B                 
1434: 20 53           JR      NZ,$1489            ; {}
1436: 54              LD      D,H                 
1437: 41              LD      B,C                 
1438: 52              LD      D,D                 
1439: 54              LD      D,H                 
143A: 20 42           JR      NZ,$147E            ; {}
143C: 55              LD      D,L                 
143D: 54              LD      D,H                 
143E: 54              LD      D,H                 
143F: 4F              LD      C,A                 
1440: 4E              LD      C,(HL)              
1441: 2F              CPL                         
1442: 70              LD      (HL),B              
1443: 82              ADD     A,D                 
1444: 00              NOP                         
1445: 47              LD      B,A                 
1446: 41              LD      B,C                 
1447: 4D              LD      C,L                 
1448: 45              LD      B,L                 
1449: 20 4F           JR      NZ,$149A            ; {}
144B: 56              LD      D,(HL)              
144C: 45              LD      B,L                 
144D: 52              LD      D,D                 
144E: 2F              CPL                         
144F: 70              LD      (HL),B              
1450: 82              ADD     A,D                 
1451: 00              NOP                         
1452: 52              LD      D,D                 
1453: 45              LD      B,L                 
1454: 41              LD      B,C                 
1455: 44              LD      B,H                 
1456: 59              LD      E,C                 
1457: 20 21           JR      NZ,$147A            ; {}
1459: 2F              CPL                         
145A: 50              LD      D,B                 
145B: 82              ADD     A,D                 
145C: 00              NOP                         
145D: 50              LD      D,B                 
145E: 4C              LD      C,H                 
145F: 41              LD      B,C                 
1460: 59              LD      E,C                 
1461: 45              LD      B,L                 
1462: 52              LD      D,D                 
1463: 20 31           JR      NZ,$1496            ; {}
1465: 2F              CPL                         
1466: 00              NOP                         
1467: 50              LD      D,B                 
1468: 4C              LD      C,H                 
1469: 41              LD      B,C                 
146A: 59              LD      E,C                 
146B: 45              LD      B,L                 
146C: 52              LD      D,D                 
146D: 20 32           JR      NZ,$14A1            ; {}
146F: 2F              CPL                         
1470: 70              LD      (HL),B              
1471: 82              ADD     A,D                 
1472: 00              NOP                         
1473: 53              LD      D,E                 
1474: 54              LD      D,H                 
1475: 41              LD      B,C                 
1476: 47              LD      B,A                 
1477: 45              LD      B,L                 
1478: 20 2F           JR      NZ,$14A9            ; {}
147A: 10 83           DJNZ    $13FF               ; {}
147C: 00              NOP                         
147D: 43              LD      B,E                 
147E: 48              LD      C,B                 
147F: 41              LD      B,C                 
1480: 4C              LD      C,H                 
1481: 4C              LD      C,H                 
1482: 45              LD      B,L                 
1483: 4E              LD      C,(HL)              
1484: 47              LD      B,A                 
1485: 49              LD      C,C                 
1486: 4E              LD      C,(HL)              
1487: 47              LD      B,A                 
1488: 20 53           JR      NZ,$14DD            ; {}
148A: 54              LD      D,H                 
148B: 41              LD      B,C                 
148C: 47              LD      B,A                 
148D: 45              LD      B,L                 
148E: 2F              CPL                         
148F: 10 83           DJNZ    $1414               ; {}
1491: 00              NOP                         
1492: 4E              LD      C,(HL)              
1493: 55              LD      D,L                 
1494: 4D              LD      C,L                 
1495: 42              LD      B,D                 
1496: 45              LD      B,L                 
1497: 52              LD      D,D                 
1498: 20 4F           JR      NZ,$14E9            ; {}
149A: 46              LD      B,(HL)              
149B: 20 48           JR      NZ,$14E5            ; {}
149D: 49              LD      C,C                 
149E: 54              LD      D,H                 
149F: 53              LD      D,E                 
14A0: 2F              CPL                         
14A1: B3              OR      E                   
14A2: 82              ADD     A,D                 
14A3: 00              NOP                         
14A4: 42              LD      B,D                 
14A5: 4F              LD      C,A                 
14A6: 4E              LD      C,(HL)              
14A7: 55              LD      D,L                 
14A8: 53              LD      D,E                 
14A9: 20 20           JR      NZ,$14CB            ; {}
14AB: 2F              CPL                         
14AC: F1              POP     AF                  
14AD: 82              ADD     A,D                 
14AE: 04              INC     B                   
14AF: 46              LD      B,(HL)              
14B0: 49              LD      C,C                 
14B1: 47              LD      B,A                 
14B2: 48              LD      C,B                 
14B3: 54              LD      D,H                 
14B4: 45              LD      B,L                 
14B5: 52              LD      D,D                 
14B6: 20 43           JR      NZ,$14FB            ; {}
14B8: 41              LD      B,C                 
14B9: 50              LD      D,B                 
14BA: 54              LD      D,H                 
14BB: 55              LD      D,L                 
14BC: 52              LD      D,D                 
14BD: 45              LD      B,L                 
14BE: 44              LD      B,H                 
14BF: 2F              CPL                         
14C0: AD              XOR     L                   
14C1: 83              ADD     A,E                 
14C2: 00              NOP                         
14C3: 20 20           JR      NZ,$14E5            ; {}
14C5: 20 20           JR      NZ,$14E7            ; {}
14C7: 20 20           JR      NZ,$14E9            ; {}
14C9: 20 20           JR      NZ,$14EB            ; {}
14CB: 20 20           JR      NZ,$14ED            ; {}
14CD: 20 20           JR      NZ,$14EF            ; {}
14CF: 20 20           JR      NZ,$14F1            ; {}
14D1: 20 20           JR      NZ,$14F3            ; {}
14D3: 20 20           JR      NZ,$14F5            ; {}
14D5: 20 20           JR      NZ,$14F7            ; {}
14D7: 20 20           JR      NZ,$14F9            ; {}
14D9: 20 20           JR      NZ,$14FB            ; {}
14DB: 20 20           JR      NZ,$14FD            ; {}
14DD: 20 2F           JR      NZ,$150E            ; {}
14DF: 6D              LD      L,L                 
14E0: 82              ADD     A,D                 
14E1: 04              INC     B                   
14E2: 50              LD      D,B                 
14E3: 45              LD      B,L                 
14E4: 52              LD      D,D                 
14E5: 46              LD      B,(HL)              
14E6: 45              LD      B,L                 
14E7: 43              LD      B,E                 
14E8: 54              LD      D,H                 
14E9: 20 63           JR      NZ,$154E            ; {}
14EB: 2F              CPL                         
14EC: 73              LD      (HL),E              
14ED: 83              ADD     A,E                 
14EE: 05              DEC     B                   
14EF: 53              LD      D,E                 
14F0: 50              LD      D,B                 
14F1: 45              LD      B,L                 
14F2: 43              LD      B,E                 
14F3: 49              LD      C,C                 
14F4: 41              LD      B,C                 
14F5: 4C              LD      C,H                 
14F6: 20 42           JR      NZ,$153A            ; {}
14F8: 4F              LD      C,A                 
14F9: 4E              LD      C,(HL)              
14FA: 55              LD      D,L                 
14FB: 53              LD      D,E                 
14FC: 20 31           JR      NZ,$152F            ; {}
14FE: 30 30           JR      NC,$1530            ; {}
1500: 30 30           JR      NC,$1532            ; {}
1502: 20 50           JR      NZ,$1554            ; {}
1504: 54              LD      D,H                 
1505: 53              LD      D,E                 
1506: 2F              CPL                         
1507: 42              LD      B,D                 
1508: 82              ADD     A,D                 
1509: 00              NOP                         
150A: 47              LD      B,A                 
150B: 41              LD      B,C                 
150C: 4C              LD      C,H                 
150D: 41              LD      B,C                 
150E: 47              LD      B,A                 
150F: 41              LD      B,C                 
1510: 2F              CPL                         
1511: A5              AND     L                   
1512: 82              ADD     A,D                 
1513: 00              NOP                         
1514: 5D              LD      E,L                 
1515: 5D              LD      E,L                 
1516: 20 53           JR      NZ,$156B            ; {}
1518: 43              LD      B,E                 
1519: 4F              LD      C,A                 
151A: 52              LD      D,D                 
151B: 45              LD      B,L                 
151C: 20 5D           JR      NZ,$157B            ; {}
151E: 5D              LD      E,L                 
151F: 2F              CPL                         
1520: 28 82           JR      Z,$14A4             ; {}
1522: 00              NOP                         
1523: 35              DEC     (HL)                
1524: 30 20           JR      NC,$1546            ; {}
1526: 20 20           JR      NZ,$1548            ; {}
1528: 20 31           JR      NZ,$155B            ; {}
152A: 30 30           JR      NC,$155C            ; {}
152C: 2F              CPL                         
152D: 2A 82 00        LD      HL,($0082)          ; {}
1530: 38 30           JR      C,$1562             ; {}
1532: 20 20           JR      NZ,$1554            ; {}
1534: 20 20           JR      NZ,$1556            ; {}
1536: 31 36 30        LD      SP,$3036            
1539: 2F              CPL                         
153A: 2B              DEC     HL                  
153B: 82              ADD     A,D                 
153C: 00              NOP                         
153D: 2F              CPL                         
153E: 3B              DEC     SP                  
153F: 83              ADD     A,E                 
1540: 03              INC     BC                  
1541: 65              LD      H,L                 
1542: 20 31           JR      NZ,$1575            ; {}
1544: 39              ADD     HL,SP               
1545: 38 31           JR      C,$1578             ; {}
1547: 20 4D           JR      NZ,$1596            ; {}
1549: 49              LD      C,C                 
154A: 44              LD      B,H                 
154B: 57              LD      D,A                 
154C: 41              LD      B,C                 
154D: 59              LD      E,C                 
154E: 20 4D           JR      NZ,$159D            ; {}
1550: 46              LD      B,(HL)              
1551: 47              LD      B,A                 
1552: 61              LD      H,C                 
1553: 43              LD      B,E                 
1554: 4F              LD      C,A                 
1555: 61              LD      H,C                 
1556: 2F              CPL                         
1557: 5E              LD      E,(HL)              
1558: 82              ADD     A,D                 
1559: 04              INC     B                   
155A: 2F              CPL                         
155B: 8F              ADC     A,A                 
155C: 82              ADD     A,D                 
155D: 04              INC     B                   
155E: 5D              LD      E,L                 
155F: 52              LD      D,D                 
1560: 45              LD      B,L                 
1561: 53              LD      D,E                 
1562: 55              LD      D,L                 
1563: 4C              LD      C,H                 
1564: 54              LD      D,H                 
1565: 53              LD      D,E                 
1566: 5D              LD      E,L                 
1567: 2F              CPL                         
1568: 32 83 05        LD      ($0583),A           ; {}
156B: 53              LD      D,E                 
156C: 48              LD      C,B                 
156D: 4F              LD      C,A                 
156E: 54              LD      D,H                 
156F: 53              LD      D,E                 
1570: 20 46           JR      NZ,$15B8            ; {}
1572: 49              LD      C,C                 
1573: 52              LD      D,D                 
1574: 45              LD      B,L                 
1575: 44              LD      B,H                 
1576: 20 20           JR      NZ,$1598            ; {}
1578: 20 20           JR      NZ,$159A            ; {}
157A: 20 20           JR      NZ,$159C            ; {}
157C: 20 20           JR      NZ,$159E            ; {}
157E: 20 20           JR      NZ,$15A0            ; {}
1580: 2F              CPL                         
1581: 05              DEC     B                   
1582: 20 20           JR      NZ,$15A4            ; {}
1584: 4D              LD      C,L                 
1585: 49              LD      C,C                 
1586: 53              LD      D,E                 
1587: 53              LD      D,E                 
1588: 49              LD      C,C                 
1589: 4C              LD      C,H                 
158A: 45              LD      B,L                 
158B: 53              LD      D,E                 
158C: 2F              CPL                         
158D: 35              DEC     (HL)                
158E: 83              ADD     A,E                 
158F: 05              DEC     B                   
1590: 4E              LD      C,(HL)              
1591: 55              LD      D,L                 
1592: 4D              LD      C,L                 
1593: 42              LD      B,D                 
1594: 45              LD      B,L                 
1595: 52              LD      D,D                 
1596: 20 4F           JR      NZ,$15E7            ; {}
1598: 46              LD      B,(HL)              
1599: 20 48           JR      NZ,$15E3            ; {}
159B: 49              LD      C,C                 
159C: 54              LD      D,H                 
159D: 53              LD      D,E                 
159E: 20 20           JR      NZ,$15C0            ; {}
15A0: 20 20           JR      NZ,$15C2            ; {}
15A2: 20 20           JR      NZ,$15C4            ; {}
15A4: 20 2F           JR      NZ,$15D5            ; {}
15A6: 38 83           JR      C,$152B             ; {}
15A8: 03              INC     BC                  
15A9: 48              LD      C,B                 
15AA: 49              LD      C,C                 
15AB: 54              LD      D,H                 
15AC: 5D              LD      E,L                 
15AD: 4D              LD      C,L                 
15AE: 49              LD      C,C                 
15AF: 53              LD      D,E                 
15B0: 53              LD      D,E                 
15B1: 20 52           JR      NZ,$1605            ; {}
15B3: 41              LD      B,C                 
15B4: 54              LD      D,H                 
15B5: 49              LD      C,C                 
15B6: 4F              LD      C,A                 
15B7: 20 20           JR      NZ,$15D9            ; {}
15B9: 20 20           JR      NZ,$15DB            ; {}
15BB: 20 20           JR      NZ,$15DD            ; {}
15BD: 20 2F           JR      NZ,$15EE            ; {}
15BF: 03              INC     BC                  
15C0: 24              INC     H                   
15C1: 60              LD      H,B                 
15C2: 2F              CPL                         
15C3: 2F              CPL                         
15C4: 83              ADD     A,E                 
15C5: 05              DEC     B                   
15C6: 31 53 54        LD      SP,$5453            
15C9: 20 42           JR      NZ,$160D            ; {}
15CB: 4F              LD      C,A                 
15CC: 4E              LD      C,(HL)              
15CD: 55              LD      D,L                 
15CE: 53              LD      D,E                 
15CF: 20 46           JR      NZ,$1617            ; {}
15D1: 4F              LD      C,A                 
15D2: 52              LD      D,D                 
15D3: 20 20           JR      NZ,$15F5            ; {}
15D5: 20 2F           JR      NZ,$1606            ; {}
15D7: 32 83 05        LD      ($0583),A           ; {}
15DA: 32 4E 44        LD      ($444E),A           
15DD: 20 42           JR      NZ,$1621            ; {}
15DF: 4F              LD      C,A                 
15E0: 4E              LD      C,(HL)              
15E1: 55              LD      D,L                 
15E2: 53              LD      D,E                 
15E3: 20 46           JR      NZ,$162B            ; {}
15E5: 4F              LD      C,A                 
15E6: 52              LD      D,D                 
15E7: 20 20           JR      NZ,$1609            ; {}
15E9: 20 2F           JR      NZ,$161A            ; {}
15EB: 35              DEC     (HL)                
15EC: 83              ADD     A,E                 
15ED: 05              DEC     B                   
15EE: 41              LD      B,C                 
15EF: 4E              LD      C,(HL)              
15F0: 44              LD      B,H                 
15F1: 20 46           JR      NZ,$1639            ; {}
15F3: 4F              LD      C,A                 
15F4: 52              LD      D,D                 
15F5: 20 45           JR      NZ,$163C            ; {}
15F7: 56              LD      D,(HL)              
15F8: 45              LD      B,L                 
15F9: 52              LD      D,D                 
15FA: 59              LD      E,C                 
15FB: 20 20           JR      NZ,$161D            ; {}
15FD: 20 2F           JR      NZ,$162E            ; {}
15FF: 05              DEC     B                   
1600: 30 30           JR      NC,$1632            ; {}
1602: 30 30           JR      NC,$1634            ; {}
1604: 20 50           JR      NZ,$1656            ; {}
1606: 54              LD      D,H                 
1607: 53              LD      D,E                 
1608: 2F              CPL                         
1609: FF              RST     0X38                
160A: FF              RST     0X38                
160B: FF              RST     0X38                
160C: FF              RST     0X38                
160D: FF              RST     0X38                
160E: FF              RST     0X38                
160F: FF              RST     0X38                
1610: FF              RST     0X38                
1611: FF              RST     0X38                
1612: FF              RST     0X38                
1613: FF              RST     0X38                
1614: FF              RST     0X38                
1615: FF              RST     0X38                
1616: FF              RST     0X38                
1617: FF              RST     0X38                
1618: FF              RST     0X38                
1619: FF              RST     0X38                
161A: FF              RST     0X38                
161B: FF              RST     0X38                
161C: FF              RST     0X38                
161D: FF              RST     0X38                
161E: FF              RST     0X38                
161F: FF              RST     0X38                
1620: FF              RST     0X38                
1621: FF              RST     0X38                
1622: FF              RST     0X38                
1623: FF              RST     0X38                
1624: FF              RST     0X38                
1625: FF              RST     0X38                
1626: FF              RST     0X38                
1627: FF              RST     0X38                
1628: FF              RST     0X38                
1629: FF              RST     0X38                
162A: FF              RST     0X38                
162B: FF              RST     0X38                
162C: FF              RST     0X38                
162D: FF              RST     0X38                
162E: FF              RST     0X38                
162F: FF              RST     0X38                
1630: FF              RST     0X38                
1631: FF              RST     0X38                
1632: FF              RST     0X38                
1633: FF              RST     0X38                
1634: FF              RST     0X38                
1635: FF              RST     0X38                
1636: FF              RST     0X38                
1637: FF              RST     0X38                
1638: FF              RST     0X38                
1639: FF              RST     0X38                
163A: FF              RST     0X38                
163B: FF              RST     0X38                
163C: FF              RST     0X38                
163D: FF              RST     0X38                
163E: FF              RST     0X38                
163F: FF              RST     0X38                
1640: FF              RST     0X38                
1641: FF              RST     0X38                
1642: FF              RST     0X38                
1643: FF              RST     0X38                
1644: FF              RST     0X38                
1645: FF              RST     0X38                
1646: FF              RST     0X38                
1647: FF              RST     0X38                
1648: FF              RST     0X38                
1649: FF              RST     0X38                
164A: FF              RST     0X38                
164B: FF              RST     0X38                
164C: FF              RST     0X38                
164D: FF              RST     0X38                
164E: FF              RST     0X38                
164F: FF              RST     0X38                
1650: FF              RST     0X38                
1651: FF              RST     0X38                
1652: FF              RST     0X38                
1653: FF              RST     0X38                
1654: FF              RST     0X38                
1655: FF              RST     0X38                
1656: FF              RST     0X38                
1657: FF              RST     0X38                
1658: FF              RST     0X38                
1659: FF              RST     0X38                
165A: FF              RST     0X38                
165B: FF              RST     0X38                
165C: FF              RST     0X38                
165D: FF              RST     0X38                
165E: FF              RST     0X38                
165F: FF              RST     0X38                
1660: FF              RST     0X38                
1661: FF              RST     0X38                
1662: FF              RST     0X38                
1663: FF              RST     0X38                
1664: FF              RST     0X38                
1665: FF              RST     0X38                
1666: FF              RST     0X38                
1667: FF              RST     0X38                
1668: FF              RST     0X38                
1669: FF              RST     0X38                
166A: FF              RST     0X38                
166B: FF              RST     0X38                
166C: FF              RST     0X38                
166D: FF              RST     0X38                
166E: FF              RST     0X38                
166F: FF              RST     0X38                
1670: FF              RST     0X38                
1671: FF              RST     0X38                
1672: FF              RST     0X38                
1673: FF              RST     0X38                
1674: FF              RST     0X38                
1675: FF              RST     0X38                
1676: FF              RST     0X38                
1677: FF              RST     0X38                
1678: FF              RST     0X38                
1679: FF              RST     0X38                
167A: FF              RST     0X38                
167B: FF              RST     0X38                
167C: FF              RST     0X38                
167D: FF              RST     0X38                
167E: FF              RST     0X38                
167F: FF              RST     0X38                
1680: FF              RST     0X38                
1681: FF              RST     0X38                
1682: FF              RST     0X38                
1683: FF              RST     0X38                
1684: FF              RST     0X38                
1685: FF              RST     0X38                
1686: FF              RST     0X38                
1687: FF              RST     0X38                
1688: FF              RST     0X38                
1689: FF              RST     0X38                
168A: FF              RST     0X38                
168B: FF              RST     0X38                
168C: FF              RST     0X38                
168D: FF              RST     0X38                
168E: FF              RST     0X38                
168F: FF              RST     0X38                
1690: FF              RST     0X38                
1691: FF              RST     0X38                
1692: FF              RST     0X38                
1693: FF              RST     0X38                
1694: FF              RST     0X38                
1695: FF              RST     0X38                
1696: FF              RST     0X38                
1697: FF              RST     0X38                
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
16A3: FF              RST     0X38                
16A4: FF              RST     0X38                
16A5: FF              RST     0X38                
16A6: FF              RST     0X38                
16A7: FF              RST     0X38                
16A8: FF              RST     0X38                
16A9: FF              RST     0X38                
16AA: FF              RST     0X38                
16AB: FF              RST     0X38                
16AC: FF              RST     0X38                
16AD: FF              RST     0X38                
16AE: FF              RST     0X38                
16AF: FF              RST     0X38                
16B0: FF              RST     0X38                
16B1: FF              RST     0X38                
16B2: FF              RST     0X38                
16B3: FF              RST     0X38                
16B4: FF              RST     0X38                
16B5: FF              RST     0X38                
16B6: FF              RST     0X38                
16B7: FF              RST     0X38                
16B8: FF              RST     0X38                
16B9: FF              RST     0X38                
16BA: FF              RST     0X38                
16BB: FF              RST     0X38                
16BC: FF              RST     0X38                
16BD: FF              RST     0X38                
16BE: FF              RST     0X38                
16BF: FF              RST     0X38                
16C0: FF              RST     0X38                
16C1: FF              RST     0X38                
16C2: FF              RST     0X38                
16C3: FF              RST     0X38                
16C4: FF              RST     0X38                
16C5: FF              RST     0X38                
16C6: FF              RST     0X38                
16C7: FF              RST     0X38                
16C8: FF              RST     0X38                
16C9: FF              RST     0X38                
16CA: FF              RST     0X38                
16CB: FF              RST     0X38                
16CC: FF              RST     0X38                
16CD: FF              RST     0X38                
16CE: FF              RST     0X38                
16CF: FF              RST     0X38                
16D0: FF              RST     0X38                
16D1: FF              RST     0X38                
16D2: FF              RST     0X38                
16D3: FF              RST     0X38                
16D4: FF              RST     0X38                
16D5: FF              RST     0X38                
16D6: FF              RST     0X38                
16D7: FF              RST     0X38                
16D8: FF              RST     0X38                
16D9: FF              RST     0X38                
16DA: FF              RST     0X38                
16DB: FF              RST     0X38                
16DC: FF              RST     0X38                
16DD: FF              RST     0X38                
16DE: FF              RST     0X38                
16DF: FF              RST     0X38                
16E0: FF              RST     0X38                
16E1: FF              RST     0X38                
16E2: FF              RST     0X38                
16E3: FF              RST     0X38                
16E4: FF              RST     0X38                
16E5: FF              RST     0X38                
16E6: FF              RST     0X38                
16E7: FF              RST     0X38                
16E8: FF              RST     0X38                
16E9: FF              RST     0X38                
16EA: FF              RST     0X38                
16EB: FF              RST     0X38                
16EC: FF              RST     0X38                
16ED: FF              RST     0X38                
16EE: FF              RST     0X38                
16EF: FF              RST     0X38                
16F0: FF              RST     0X38                
16F1: FF              RST     0X38                
16F2: FF              RST     0X38                
16F3: FF              RST     0X38                
16F4: FF              RST     0X38                
16F5: FF              RST     0X38                
16F6: FF              RST     0X38                
16F7: FF              RST     0X38                
16F8: FF              RST     0X38                
16F9: FF              RST     0X38                
16FA: FF              RST     0X38                
16FB: FF              RST     0X38                
16FC: FF              RST     0X38                
16FD: FF              RST     0X38                
16FE: FF              RST     0X38                
16FF: FF              RST     0X38                
1700: ED 5B 82 92     LD      DE,($9282)          
1704: 1A              LD      A,(DE)              
1705: 07              RLCA                        
1706: 07              RLCA                        
1707: 07              RLCA                        
1708: E6 07           AND     $07                 
170A: 21 13 17        LD      HL,$1713            
170D: CF              RST     0X08                
170E: 7E              LD      A,(HL)              
170F: 23              INC     HL                  
1710: 66              LD      H,(HL)              
1711: 6F              LD      L,A                 
1712: E9              JP      (HL)                
1713: 66              LD      H,(HL)              
1714: 17              RLA                         
1715: 66              LD      H,(HL)              
1716: 17              RLA                         
1717: 1F              RRA                         
1718: 17              RLA                         
1719: 66              LD      H,(HL)              
171A: 17              RLA                         
171B: 34              INC     (HL)                
171C: 17              RLA                         
171D: 2D              DEC     L                   
171E: 17              RLA                         
171F: 3A A0 92        LD      A,($92A0)           
1722: E6 0F           AND     $0F                 
1724: C0              RET     NZ                  
1725: 21 07 92        LD      HL,$9207            
1728: 35              DEC     (HL)                
1729: C0              RET     NZ                  
172A: C3 66 17        JP      $1766               ; {}
172D: CD 19 1F        CALL    $1F19               ; {}
1730: ED 5B 82 92     LD      DE,($9282)          
1734: 1A              LD      A,(DE)              
1735: 21 27 98        LD      HL,$9827            
1738: 5E              LD      E,(HL)              
1739: CB 47           BIT     0,A                 
173B: 20 04           JR      NZ,$1741            ; {}
173D: E6 0A           AND     $0A                 
173F: 18 14           JR      $1755               ; {}
1741: 3A 09 92        LD      A,($9209)           
1744: 6F              LD      L,A                 
1745: 26 93           LD      H,$93               
1747: 3A 62 93        LD      A,($9362)           
174A: 96              SUB     (HL)                
174B: 3E 0A           LD      A,$0A               
174D: 28 06           JR      Z,$1755             ; {}
174F: 3E 08           LD      A,$08               
1751: 38 02           JR      C,$1755             ; {}
1753: 3E 02           LD      A,$02               
1755: CD 9C 1F        CALL    $1F9C               ; {}
1758: 3A A0 92        LD      A,($92A0)           
175B: E6 03           AND     $03                 
175D: C0              RET     NZ                  
175E: 21 07 92        LD      HL,$9207            
1761: 35              DEC     (HL)                
1762: C0              RET     NZ                  
1763: CD 19 1F        CALL    $1F19               ; {}
1766: ED 5B 82 92     LD      DE,($9282)          
176A: 1A              LD      A,(DE)              
176B: E6 C0           AND     $C0                 
176D: FE 80           CP      $80                 
176F: 20 01           JR      NZ,$1772            ; {}
1771: 13              INC     DE                  
1772: 13              INC     DE                  
1773: 1A              LD      A,(DE)              
1774: ED 53 82 92     LD      ($9282),DE          
1778: 07              RLCA                        
1779: 07              RLCA                        
177A: 07              RLCA                        
177B: E6 07           AND     $07                 
177D: 21 86 17        LD      HL,$1786            
1780: CF              RST     0X08                
1781: 7E              LD      A,(HL)              
1782: 23              INC     HL                  
1783: 66              LD      H,(HL)              
1784: 6F              LD      L,A                 
1785: E9              JP      (HL)                
1786: 94              SUB     H                   
1787: 17              RLA                         
1788: 94              SUB     H                   
1789: 17              RLA                         
178A: A1              AND     C                   
178B: 17              RLA                         
178C: A8              XOR     B                   
178D: 17              RLA                         
178E: AE              XOR     (HL)                
178F: 17              RLA                         
1790: AE              XOR     (HL)                
1791: 17              RLA                         
1792: 9C              SBC     H                   
1793: 17              RLA                         
1794: 1A              LD      A,(DE)              
1795: 07              RLCA                        
1796: E6 7E           AND     $7E                 
1798: 32 09 92        LD      ($9209),A           
179B: C9              RET                         
179C: AF              XOR     A                   
179D: 32 03 90        LD      ($9003),A           
17A0: C9              RET                         
17A1: 1A              LD      A,(DE)              
17A2: E6 1F           AND     $1F                 
17A4: 32 07 92        LD      ($9207),A           
17A7: C9              RET                         
17A8: 1A              LD      A,(DE)              
17A9: E6 1F           AND     $1F                 
17AB: 4F              LD      C,A                 
17AC: F7              RST     0X30                
17AD: C9              RET                         
17AE: 13              INC     DE                  
17AF: 1A              LD      A,(DE)              
17B0: 18 F2           JR      $17A4               ; {}
17B2: 3A 01 92        LD      A,($9201)           
17B5: 3D              DEC     A                   
17B6: C0              RET     NZ                  
17B7: 3A 03 92        LD      A,($9203)           
17BA: 21 C3 17        LD      HL,$17C3            
17BD: CF              RST     0X08                
17BE: 5E              LD      E,(HL)              
17BF: 23              INC     HL                  
17C0: 56              LD      D,(HL)              
17C1: EB              EX      DE,HL               
17C2: E9              JP      (HL)                
17C3: 40              LD      B,B                 
17C4: 19              ADD     HL,DE               
17C5: 48              LD      C,B                 
17C6: 19              ADD     HL,DE               
17C7: 84              ADD     A,H                 
17C8: 19              ADD     HL,DE               
17C9: D9              EXX                         
17CA: 18 D1           JR      $179D               ; {}
17CC: 18 AC           JR      $177A               ; {}
17CE: 18 40           JR      $1810               ; {}
17D0: 19              ADD     HL,DE               
17D1: F5              PUSH    AF                  
17D2: 17              RLA                         
17D3: 52              LD      D,D                 
17D4: 18 D1           JR      $17A7               ; {}
17D6: 18 08           JR      $17E0               ; {}
17D8: 18 D1           JR      $17AB               ; {}
17DA: 18 40           JR      $181C               ; {}
17DC: 18 40           JR      $181E               ; {}
17DE: 19              ADD     HL,DE               
17DF: E1              POP     HL                  
17E0: 17              RLA                         
17E1: 3A AF 92        LD      A,($92AF)           
17E4: A7              AND     A                   
17E5: 28 05           JR      Z,$17EC             ; {}
17E7: 3D              DEC     A                   
17E8: CA A7 19        JP      Z,$19A7             ; {}
17EB: C9              RET                         
17EC: CD 14 32        CALL    $3214               ; {}
17EF: 3E 0A           LD      A,$0A               
17F1: 32 AF 92        LD      ($92AF),A           
17F4: C9              RET                         
17F5: 3A A0 92        LD      A,($92A0)           
17F8: E6 1F           AND     $1F                 
17FA: FE 1F           CP      $1F                 
17FC: C0              RET     NZ                  
17FD: 3E 01           LD      A,$01               
17FF: 32 05 90        LD      ($9005),A           
1802: 0E 02           LD      C,$02               
1804: F7              RST     0X30                
1805: C3 A7 19        JP      $19A7               ; {}
1808: CD 4C 13        CALL    $134C               ; {}
180B: 21 1F 18        LD      HL,$181F            
180E: 22 82 92        LD      ($9282),HL          
1811: 3E 01           LD      A,$01               
1813: 32 03 90        LD      ($9003),A           
1816: 32 15 90        LD      ($9015),A           
1819: 32 25 90        LD      ($9025),A           
181C: C3 A7 19        JP      $19A7               ; {}
181F: 08              EX      AF,AF'              
1820: 18 8A           JR      $17AC               ; {}
1822: 08              EX      AF,AF'              
1823: 88              ADC     A,B                 
1824: 06 81           LD      B,$81               
1826: 28 81           JR      Z,$17A9             ; {}
1828: 05              DEC     B                   
1829: 54              LD      D,H                 
182A: 1A              LD      A,(DE)              
182B: 88              ADC     A,B                 
182C: 12              LD      (DE),A              
182D: 81              ADD     A,C                 
182E: 0F              RRCA                        
182F: A2              AND     D                   
1830: 16 AA           LD      D,$AA               
1832: 14              INC     D                   
1833: 88              ADC     A,B                 
1834: 18 88           JR      $17BE               ; {}
1836: 10 43           DJNZ    $187B               ; {}
1838: 82              ADD     A,D                 
1839: 10 88           DJNZ    $17C3               ; {}
183B: 06 A2           LD      B,$A2               
183D: 20 56           JR      NZ,$1895            ; {}
183F: C0              RET     NZ                  
1840: EF              RST     0X28                
1841: CD 42 12        CALL    $1242               ; {}
1844: AF              XOR     A                   
1845: 32 10 90        LD      ($9010),A           
1848: 32 0B 92        LD      ($920B),A           
184B: 3C              INC     A                   
184C: 32 02 90        LD      ($9002),A           
184F: C3 A7 19        JP      $19A7               ; {}
1852: AF              XOR     A                   
1853: 32 2B 98        LD      ($982B),A           
1856: 3C              INC     A                   
1857: 32 B7 9A        LD      ($9AB7),A           
185A: 32 21 98        LD      ($9821),A           
185D: 32 03 90        LD      ($9003),A           
1860: 32 15 90        LD      ($9015),A           
1863: 32 25 98        LD      ($9825),A           
1866: 21 87 18        LD      HL,$1887            
1869: 22 82 92        LD      ($9282),HL          
186C: CD C5 01        CALL    $01C5               ; {}
186F: CD 4C 13        CALL    $134C               ; {}
1872: 3E 01           LD      A,$01               
1874: 32 0B 92        LD      ($920B),A           
1877: 32 42 98        LD      ($9842),A           
187A: 32 2C 98        LD      ($982C),A           
187D: 3C              INC     A                   
187E: 32 C4 99        LD      ($99C4),A           
1881: 32 C5 99        LD      ($99C5),A           
1884: C3 A7 19        JP      $19A7               ; {}
1887: 02              LD      (BC),A              
1888: 8A              ADC     A,D                 
1889: 04              INC     B                   
188A: 82              ADD     A,D                 
188B: 07              RLCA                        
188C: AA              XOR     D                   
188D: 28 88           JR      Z,$1817             ; {}
188F: 10 AA           DJNZ    $183B               ; {}
1891: 38 82           JR      C,$1815             ; {}
1893: 12              LD      (DE),A              
1894: AA              XOR     D                   
1895: 20 88           JR      NZ,$181F            ; {}
1897: 14              INC     D                   
1898: AA              XOR     D                   
1899: 20 82           JR      NZ,$181D            ; {}
189B: 06 A8           LD      B,$A8               
189D: 0E A2           LD      C,$A2               
189F: 17              RLA                         
18A0: 88              ADC     A,B                 
18A1: 12              LD      (DE),A              
18A2: A2              AND     D                   
18A3: 14              INC     D                   
18A4: 18 88           JR      $182E               ; {}
18A6: 1B              DEC     DE                  
18A7: 81              ADD     A,C                 
18A8: 2A 5F 4C        LD      HL,($4C5F)          
18AB: C0              RET     NZ                  
18AC: 3A AE 92        LD      A,($92AE)           
18AF: A7              AND     A                   
18B0: 28 09           JR      Z,$18BB             ; {}
18B2: 3D              DEC     A                   
18B3: CA A7 19        JP      Z,$19A7             ; {}
18B6: FE 05           CP      $05                 
18B8: 28 0C           JR      Z,$18C6             ; {}
18BA: C9              RET                         
18BB: 3E 34           LD      A,$34               
18BD: 32 34 92        LD      ($9234),A           
18C0: 3E 09           LD      A,$09               
18C2: 32 AE 92        LD      ($92AE),A           
18C5: C9              RET                         
18C6: AF              XOR     A                   
18C7: 32 62 93        LD      ($9362),A           
18CA: 0E 13           LD      C,$13               
18CC: F7              RST     0X30                
18CD: 0E 14           LD      C,$14               
18CF: F7              RST     0X30                
18D0: C9              RET                         
18D1: 3A 03 90        LD      A,($9003)           
18D4: A7              AND     A                   
18D5: CA A7 19        JP      Z,$19A7             ; {}
18D8: C9              RET                         
18D9: 06 07           LD      B,$07               
18DB: CD 9E 12        CALL    $129E               ; {}
18DE: 10 FB           DJNZ    $18DB               ; {}
18E0: AF              XOR     A                   
18E1: 32 20 98        LD      ($9820),A           
18E4: 32 05 90        LD      ($9005),A           
18E7: CD 4C 13        CALL    $134C               ; {}
18EA: 21 0D FF        LD      HL,$FF0D            
18ED: 22 C5 92        LD      ($92C5),HL          
18F0: 22 C4 92        LD      ($92C4),HL          
18F3: 22 C1 92        LD      ($92C1),HL          
18F6: 22 C0 92        LD      ($92C0),HL          
18F9: 21 28 19        LD      HL,$1928            
18FC: 22 82 92        LD      ($9282),HL          
18FF: AF              XOR     A                   
1900: 06 10           LD      B,$10               
1902: 21 CA 92        LD      HL,$92CA            
1905: DF              RST     0X18                
1906: 32 27 98        LD      ($9827),A           
1909: 32 0B 92        LD      ($920B),A           
190C: 3C              INC     A                   
190D: 32 2B 98        LD      ($982B),A           
1910: 32 10 90        LD      ($9010),A           
1913: 32 0B 90        LD      ($900B),A           
1916: 32 03 90        LD      ($9003),A           
1919: 3A 03 68        LD      A,($6803)           
191C: 0F              RRCA                        
191D: E6 01           AND     $01                 
191F: 32 B7 9A        LD      ($9AB7),A           
1922: CD 7B 12        CALL    $127B               ; {}
1925: C3 A7 19        JP      $19A7               ; {}
1928: 08              EX      AF,AF'              
1929: 1B              DEC     DE                  
192A: 81              ADD     A,C                 
192B: 3D              DEC     A                   
192C: 81              ADD     A,C                 
192D: 0A              LD      A,(BC)              
192E: 42              LD      B,D                 
192F: 19              ADD     HL,DE               
1930: 81              ADD     A,C                 
1931: 28 81           JR      Z,$18B4             ; {}
1933: 08              EX      AF,AF'              
1934: 18 81           JR      $18B7               ; {}
1936: 2E 81           LD      L,$81               
1938: 03              INC     BC                  
1939: 1A              LD      A,(DE)              
193A: 81              ADD     A,C                 
193B: 11 81 05        LD      DE,$0581            
193E: 42              LD      B,D                 
193F: C0              RET     NZ                  
1940: CD 60 01        CALL    $0160               ; {}
1943: CD 3C 00        CALL    $003C               ; {}
1946: 18 5F           JR      $19A7               ; {}
1948: 21 5C 19        LD      HL,$195C            
194B: 22 80 92        LD      ($9280),HL          
194E: AF              XOR     A                   
194F: 32 05 92        LD      ($9205),A           
1952: 32 A8 92        LD      ($92A8),A           
1955: 3E 02           LD      A,$02               
1957: 32 AE 92        LD      ($92AE),A           
195A: 18 4B           JR      $19A7               ; {}
195C: 08              EX      AF,AF'              
195D: 1B              DEC     DE                  
195E: 44              LD      B,H                 
195F: 3A 0A 12        LD      A,($120A)           ; {}
1962: 44              LD      B,H                 
1963: 42              LD      B,D                 
1964: 0C              INC     C                   
1965: 08              EX      AF,AF'              
1966: 7C              LD      A,H                 
1967: 50              LD      D,B                 
1968: 34              INC     (HL)                
1969: 08              EX      AF,AF'              
196A: 34              INC     (HL)                
196B: 5C              LD      E,H                 
196C: 30 08           JR      NC,$1976            ; {}
196E: 64              LD      H,H                 
196F: 5C              LD      E,H                 
1970: 32 08 94        LD      ($9408),A           
1973: 5C              LD      E,H                 
1974: 4A              LD      C,D                 
1975: 12              LD      (DE),A              
1976: A4              AND     H                   
1977: 64              LD      H,H                 
1978: 36 08           LD      (HL),$08            
197A: C4 5C 58        CALL    NZ,$585C            
197D: 12              LD      (DE),A              
197E: B4              OR      H                   
197F: 64              LD      H,H                 
1980: 52              LD      D,D                 
1981: 12              LD      (DE),A              
1982: D4 64 3A        CALL    NC,$3A64            ; {}
1985: AE              XOR     (HL)                
1986: 92              SUB     D                   
1987: A7              AND     A                   
1988: C0              RET     NZ                  
1989: 3E 02           LD      A,$02               
198B: 32 AE 92        LD      ($92AE),A           
198E: 3A 05 92        LD      A,($9205)           
1991: FE 05           CP      $05                 
1993: 28 12           JR      Z,$19A7             ; {}
1995: 3C              INC     A                   
1996: 32 05 92        LD      ($9205),A           
1999: C6 0D           ADD     $0D                 
199B: 4F              LD      C,A                 
199C: F7              RST     0X30                
199D: 3A 05 92        LD      A,($9205)           
19A0: FE 03           CP      $03                 
19A2: D8              RET     C                   
19A3: CD 9E 12        CALL    $129E               ; {}
19A6: C9              RET                         
19A7: 21 03 92        LD      HL,$9203            
19AA: 34              INC     (HL)                
19AB: 7E              LD      A,(HL)              
19AC: FE 0F           CP      $0F                 
19AE: C0              RET     NZ                  
19AF: 36 00           LD      (HL),$00            
19B1: C9              RET                         
19B2: 3A 8E 92        LD      A,($928E)           
19B5: A7              AND     A                   
19B6: 20 1A           JR      NZ,$19D2            ; {}
19B8: 21 AD 92        LD      HL,$92AD            
19BB: B6              OR      (HL)                
19BC: 28 28           JR      Z,$19E6             ; {}
19BE: FE 04           CP      $04                 
19C0: 20 05           JR      NZ,$19C7            ; {}
19C2: 3D              DEC     A                   
19C3: 77              LD      (HL),A              
19C4: 32 A9 9A        LD      ($9AA9),A           
19C7: 3A 29 98        LD      A,($9829)           
19CA: C6 0D           ADD     $0D                 
19CC: 6F              LD      L,A                 
19CD: 26 91           LD      H,$91               
19CF: 36 04           LD      (HL),$04            
19D1: C9              RET                         
19D2: 0E 0A           LD      C,$0A               
19D4: F7              RST     0X30                
19D5: 3E 06           LD      A,$06               
19D7: 32 AD 92        LD      ($92AD),A           
19DA: 3C              INC     A                   
19DB: 32 63 8B        LD      ($8B63),A           
19DE: AF              XOR     A                   
19DF: 32 8B 92        LD      ($928B),A           
19E2: 32 8E 92        LD      ($928E),A           
19E5: C9              RET                         
19E6: 3A D1 82        LD      A,($82D1)           
19E9: FE 24           CP      $24                 
19EB: 28 29           JR      Z,$1A16             ; {}
19ED: 21 62 93        LD      HL,$9362            
19F0: 3A 28 98        LD      A,($9828)           
19F3: E6 07           AND     $07                 
19F5: 5F              LD      E,A                 
19F6: 54              LD      D,H                 
19F7: 7E              LD      A,(HL)              
19F8: 12              LD      (DE),A              
19F9: 36 00           LD      (HL),$00            
19FB: 2C              INC     L                   
19FC: 1C              INC     E                   
19FD: 7E              LD      A,(HL)              
19FE: 12              LD      (DE),A              
19FF: 26 9B           LD      H,$9B               
1A01: 54              LD      D,H                 
1A02: ED A8           LDD                         
1A04: ED A0           LDI                         
1A06: 26 8B           LD      H,$8B               
1A08: 6B              LD      L,E                 
1A09: 36 07           LD      (HL),$07            
1A0B: 2D              DEC     L                   
1A0C: 36 07           LD      (HL),$07            
1A0E: 0E 0B           LD      C,$0B               
1A10: 21 B1 83        LD      HL,$83B1            
1A13: CD B3 13        CALL    $13B3               ; {}
1A16: 3A 28 98        LD      A,($9828)           
1A19: 6F              LD      L,A                 
1A1A: E6 07           AND     $07                 
1A1C: 5F              LD      E,A                 
1A1D: 26 88           LD      H,$88               
1A1F: 3A 15 92        LD      A,($9215)           
1A22: 4F              LD      C,A                 
1A23: 7E              LD      A,(HL)              
1A24: FE 09           CP      $09                 
1A26: 20 1D           JR      NZ,$1A45            ; {}
1A28: 26 93           LD      H,$93               
1A2A: 54              LD      D,H                 
1A2B: 7E              LD      A,(HL)              
1A2C: 12              LD      (DE),A              
1A2D: 2C              INC     L                   
1A2E: 1C              INC     E                   
1A2F: 3E 10           LD      A,$10               
1A31: CB 41           BIT     0,C                 
1A33: 28 02           JR      Z,$1A37             ; {}
1A35: ED 44           NEG                         
1A37: 47              LD      B,A                 
1A38: 86              ADD     A,(HL)              
1A39: 12              LD      (DE),A              
1A3A: 1F              RRA                         
1A3B: A8              XOR     B                   
1A3C: 07              RLCA                        
1A3D: E6 01           AND     $01                 
1A3F: 26 9B           LD      H,$9B               
1A41: 54              LD      D,H                 
1A42: AE              XOR     (HL)                
1A43: 12              LD      (DE),A              
1A44: C9              RET                         
1A45: 21 8B 92        LD      HL,$928B            
1A48: 7E              LD      A,(HL)              
1A49: A7              AND     A                   
1A4A: 20 05           JR      NZ,$1A51            ; {}
1A4C: 16 8B           LD      D,$8B               
1A4E: 3E 06           LD      A,$06               
1A50: 12              LD      (DE),A              
1A51: 34              INC     (HL)                
1A52: FE 24           CP      $24                 
1A54: 28 1A           JR      Z,$1A70             ; {}
1A56: 06 01           LD      B,$01               
1A58: CB 41           BIT     0,C                 
1A5A: 20 02           JR      NZ,$1A5E            ; {}
1A5C: 05              DEC     B                   
1A5D: 05              DEC     B                   
1A5E: 6B              LD      L,E                 
1A5F: 2C              INC     L                   
1A60: 26 93           LD      H,$93               
1A62: 78              LD      A,B                 
1A63: 86              ADD     A,(HL)              
1A64: 77              LD      (HL),A              
1A65: 1F              RRA                         
1A66: A8              XOR     B                   
1A67: 07              RLCA                        
1A68: D0              RET     NC                  
1A69: 26 9B           LD      H,$9B               
1A6B: 7E              LD      A,(HL)              
1A6C: EE 01           XOR     $01                 
1A6E: 77              LD      (HL),A              
1A6F: C9              RET                         
1A70: AF              XOR     A                   
1A71: 32 11 90        LD      ($9011),A           
1A74: 32 A9 9A        LD      ($9AA9),A           
1A77: 16 88           LD      D,$88               
1A79: 3C              INC     A                   
1A7A: 12              LD      (DE),A              
1A7B: 32 28 98        LD      ($9828),A           
1A7E: 32 B9 99        LD      ($99B9),A           
1A81: 3C              INC     A                   
1A82: 32 13 92        LD      ($9213),A           
1A85: C9              RET                         
1A86: 3A CA 99        LD      A,($99CA)           
1A89: 4F              LD      C,A                 
1A8A: 3A A7 92        LD      A,($92A7)           
1A8D: B9              CP      C                   
1A8E: D0              RET     NC                  
1A8F: 3A 41 98        LD      A,($9841)           
1A92: A7              AND     A                   
1A93: 20 46           JR      NZ,$1ADB            ; {}
1A95: 21 07 88        LD      HL,$8807            
1A98: 01 FF 14        LD      BC,$14FF            
1A9B: 3E 01           LD      A,$01               
1A9D: 2C              INC     L                   
1A9E: ED A1           CPI                         
1AA0: 28 0F           JR      Z,$1AB1             ; {}
1AA2: 10 F9           DJNZ    $1A9D               ; {}
1AA4: 21 3F 88        LD      HL,$883F            
1AA7: 06 10           LD      B,$10               
1AA9: 2C              INC     L                   
1AAA: ED A1           CPI                         
1AAC: 28 03           JR      Z,$1AB1             ; {}
1AAE: 10 F9           DJNZ    $1AA9               ; {}
1AB0: C9              RET                         
1AB1: 3E C0           LD      A,$C0               
1AB3: 32 41 98        LD      ($9841),A           
1AB6: 2D              DEC     L                   
1AB7: 5D              LD      E,L                 
1AB8: 16 8B           LD      D,$8B               
1ABA: 1C              INC     E                   
1ABB: 1A              LD      A,(DE)              
1ABC: 1D              DEC     E                   
1ABD: 4F              LD      C,A                 
1ABE: 3A 21 98        LD      A,($9821)           
1AC1: CB 3F           SRL     A                   
1AC3: CB 3F           SRL     A                   
1AC5: 6F              LD      L,A                 
1AC6: 26 00           LD      H,$00               
1AC8: 3E 03           LD      A,$03               
1ACA: CD 61 10        CALL    $1061               ; {}
1ACD: C6 04           ADD     $04                 
1ACF: 21 2D 98        LD      HL,$982D            
1AD2: 73              LD      (HL),E              
1AD3: 2C              INC     L                   
1AD4: 71              LD      (HL),C              
1AD5: 2C              INC     L                   
1AD6: 77              LD      (HL),A              
1AD7: 32 B2 9A        LD      ($9AB2),A           
1ADA: C9              RET                         
1ADB: 3C              INC     A                   
1ADC: 28 1C           JR      Z,$1AFA             ; {}
1ADE: 32 41 98        LD      ($9841),A           
1AE1: 08              EX      AF,AF'              
1AE2: 21 2D 98        LD      HL,$982D            
1AE5: 5E              LD      E,(HL)              
1AE6: 16 88           LD      D,$88               
1AE8: 1A              LD      A,(DE)              
1AE9: 3D              DEC     A                   
1AEA: C2 5A 1B        JP      NZ,$1B5A            ; {}
1AED: 16 8B           LD      D,$8B               
1AEF: 2C              INC     L                   
1AF0: 08              EX      AF,AF'              
1AF1: CB 67           BIT     4,A                 
1AF3: 28 01           JR      Z,$1AF6             ; {}
1AF5: 2C              INC     L                   
1AF6: 7E              LD      A,(HL)              
1AF7: 1C              INC     E                   
1AF8: 12              LD      (DE),A              
1AF9: C9              RET                         
1AFA: 3A 15 90        LD      A,($9015)           
1AFD: A7              AND     A                   
1AFE: 20 06           JR      NZ,$1B06            ; {}
1B00: 3E E0           LD      A,$E0               
1B02: 32 41 98        LD      ($9841),A           
1B05: C9              RET                         
1B06: 3A 2D 98        LD      A,($982D)           
1B09: 6F              LD      L,A                 
1B0A: 26 88           LD      H,$88               
1B0C: 7E              LD      A,(HL)              
1B0D: 3D              DEC     A                   
1B0E: 20 4A           JR      NZ,$1B5A            ; {}
1B10: 26 92           LD      H,$92               
1B12: 7E              LD      A,(HL)              
1B13: CB 7F           BIT     7,A                 
1B15: 20 43           JR      NZ,$1B5A            ; {}
1B17: 3A 2F 98        LD      A,($982F)           
1B1A: D6 04           SUB     $04                 
1B1C: 21 5F 1B        LD      HL,$1B5F            
1B1F: CF              RST     0X08                
1B20: 11 B0 99        LD      DE,$99B0            
1B23: 3E 03           LD      A,$03               
1B25: 12              LD      (DE),A              
1B26: 1C              INC     E                   
1B27: ED A0           LDI                         
1B29: ED A0           LDI                         
1B2B: 3A 2F 98        LD      A,($982F)           
1B2E: D6 04           SUB     $04                 
1B30: E6 0F           AND     $0F                 
1B32: 4F              LD      C,A                 
1B33: 21 65 1B        LD      HL,$1B65            
1B36: CF              RST     0X08                
1B37: 5E              LD      E,(HL)              
1B38: 23              INC     HL                  
1B39: 56              LD      D,(HL)              
1B3A: 26 8B           LD      H,$8B               
1B3C: 3A 2D 98        LD      A,($982D)           
1B3F: 6F              LD      L,A                 
1B40: 79              LD      A,C                 
1B41: 07              RLCA                        
1B42: 07              RLCA                        
1B43: 07              RLCA                        
1B44: C6 56           ADD     $56                 
1B46: 4E              LD      C,(HL)              
1B47: 77              LD      (HL),A              
1B48: 79              LD      A,C                 
1B49: E6 F8           AND     $F8                 
1B4B: 4F              LD      C,A                 
1B4C: 3A 2E 98        LD      A,($982E)           
1B4F: E6 07           AND     $07                 
1B51: B1              OR      C                   
1B52: 32 2E 98        LD      ($982E),A           
1B55: 26 88           LD      H,$88               
1B57: CD 83 10        CALL    $1083               ; {}
1B5A: AF              XOR     A                   
1B5B: 32 04 90        LD      ($9004),A           
1B5E: C9              RET                         
1B5F: 1E BD           LD      E,$BD               
1B61: 0A              LD      A,(BC)              
1B62: B8              CP      B                   
1B63: 14              INC     D                   
1B64: BC              CP      H                   
1B65: EA 04 73        JP      PE,$7304            
1B68: 04              INC     B                   
1B69: AB              XOR     E                   
1B6A: 04              INC     B                   
1B6B: 3A 0B 92        LD      A,($920B)           
1B6E: A7              AND     A                   
1B6F: 28 0A           JR      Z,$1B7B             ; {}
1B71: 3A 15 90        LD      A,($9015)           
1B74: 4F              LD      C,A                 
1B75: 3A 1D 90        LD      A,($901D)           
1B78: 2F              CPL                         
1B79: A1              AND     C                   
1B7A: C8              RET     Z                   
1B7B: 06 04           LD      B,$04               
1B7D: 21 CA 92        LD      HL,$92CA            
1B80: 7E              LD      A,(HL)              
1B81: 3C              INC     A                   
1B82: 20 0D           JR      NZ,$1B91            ; {}
1B84: 2C              INC     L                   
1B85: 2C              INC     L                   
1B86: 2C              INC     L                   
1B87: 10 F7           DJNZ    $1B80               ; {}
1B89: 3A A0 92        LD      A,($92A0)           
1B8C: E6 0F           AND     $0F                 
1B8E: 28 1E           JR      Z,$1BAE             ; {}
1B90: C9              RET                         
1B91: 36 FF           LD      (HL),$FF            
1B93: 3D              DEC     A                   
1B94: 16 88           LD      D,$88               
1B96: 5F              LD      E,A                 
1B97: CB BB           RES     7,E                 
1B99: 08              EX      AF,AF'              
1B9A: 1A              LD      A,(DE)              
1B9B: 3D              DEC     A                   
1B9C: C0              RET     NZ                  
1B9D: 2C              INC     L                   
1B9E: 5E              LD      E,(HL)              
1B9F: 2C              INC     L                   
1BA0: 56              LD      D,(HL)              
1BA1: 08              EX      AF,AF'              
1BA2: 6F              LD      L,A                 
1BA3: 26 88           LD      H,$88               
1BA5: CD 79 10        CALL    $1079               ; {}
1BA8: 3E 01           LD      A,$01               
1BAA: 32 B3 9A        LD      ($9AB3),A           
1BAD: C9              RET                         
1BAE: 21 C0 92        LD      HL,$92C0            
1BB1: 06 03           LD      B,$03               
1BB3: 35              DEC     (HL)                
1BB4: 28 04           JR      Z,$1BBA             ; {}
1BB6: 2C              INC     L                   
1BB7: 10 FA           DJNZ    $1BB3               ; {}
1BB9: C9              RET                         
1BBA: 3A C4 99        LD      A,($99C4)           
1BBD: 4F              LD      C,A                 
1BBE: 3A 87 92        LD      A,($9287)           
1BC1: B9              CP      C                   
1BC2: 38 02           JR      C,$1BC6             ; {}
1BC4: 34              INC     (HL)                
1BC5: C9              RET                         
1BC6: CB D5           SET     2,L                 
1BC8: 7E              LD      A,(HL)              
1BC9: CB 95           RES     2,L                 
1BCB: 77              LD      (HL),A              
1BCC: 78              LD      A,B                 
1BCD: 3D              DEC     A                   
1BCE: 21 D7 1B        LD      HL,$1BD7            
1BD1: CF              RST     0X08                
1BD2: 7E              LD      A,(HL)              
1BD3: 23              INC     HL                  
1BD4: 66              LD      H,(HL)              
1BD5: 6F              LD      L,A                 
1BD6: E9              JP      (HL)                
1BD7: DD 1B           DEC     DE                  
1BD9: FD 1B           DEC     DE                  
1BDB: 07              RLCA                        
1BDC: 1C              INC     E                   
1BDD: 06 14           LD      B,$14               
1BDF: 21 08 88        LD      HL,$8808            
1BE2: 11 4F 03        LD      DE,$034F            
1BE5: 3A 2D 98        LD      A,($982D)           
1BE8: 4F              LD      C,A                 
1BE9: 7E              LD      A,(HL)              
1BEA: 3D              DEC     A                   
1BEB: 20 04           JR      NZ,$1BF1            ; {}
1BED: 79              LD      A,C                 
1BEE: BD              CP      L                   
1BEF: 20 05           JR      NZ,$1BF6            ; {}
1BF1: 2C              INC     L                   
1BF2: 2C              INC     L                   
1BF3: 10 F4           DJNZ    $1BE9               ; {}
1BF5: C9              RET                         
1BF6: 32 B3 9A        LD      ($9AB3),A           
1BF9: CD 83 10        CALL    $1083               ; {}
1BFC: C9              RET                         
1BFD: 06 10           LD      B,$10               
1BFF: 21 40 88        LD      HL,$8840            
1C02: 11 A9 03        LD      DE,$03A9            
1C05: 18 DE           JR      $1BE5               ; {}
1C07: 3A 2B 98        LD      A,($982B)           
1C0A: A7              AND     A                   
1C0B: 20 29           JR      NZ,$1C36            ; {}
1C0D: 21 2C 98        LD      HL,$982C            
1C10: 34              INC     (HL)                
1C11: CB 46           BIT     0,(HL)              
1C13: 20 21           JR      NZ,$1C36            ; {}
1C15: DD 2E 02        LD      IXL,$02             
1C18: FD 21 54 04     LD      IY,$0454            
1C1C: 11 30 88        LD      DE,$8830            
1C1F: 06 04           LD      B,$04               
1C21: 1A              LD      A,(DE)              
1C22: 3D              DEC     A                   
1C23: 28 05           JR      Z,$1C2A             ; {}
1C25: 1C              INC     E                   
1C26: 1C              INC     E                   
1C27: 10 F8           DJNZ    $1C21               ; {}
1C29: C9              RET                         
1C2A: 3E 01           LD      A,$01               
1C2C: 32 2B 98        LD      ($982B),A           
1C2F: 7B              LD      A,E                 
1C30: 32 28 98        LD      ($9828),A           
1C33: C3 B4 1C        JP      $1CB4               ; {}
1C36: 21 32 1D        LD      HL,$1D32            
1C39: 16 88           LD      D,$88               
1C3B: 01 00 06        LD      BC,$0600            
1C3E: 5E              LD      E,(HL)              
1C3F: 23              INC     HL                  
1C40: 3A 2D 98        LD      A,($982D)           
1C43: BB              CP      E                   
1C44: 28 04           JR      Z,$1C4A             ; {}
1C46: 1A              LD      A,(DE)              
1C47: 3D              DEC     A                   
1C48: D6 01           SUB     $01                 
1C4A: CB 11           RL      C                   
1C4C: 10 F0           DJNZ    $1C3E               ; {}
1C4E: DD 2E 00        LD      IXL,$00             
1C51: 06 04           LD      B,$04               
1C53: DD 61           LD      IXH,C               
1C55: 79              LD      A,C                 
1C56: E6 07           AND     $07                 
1C58: FE 04           CP      $04                 
1C5A: 28 05           JR      Z,$1C61             ; {}
1C5C: FE 03           CP      $03                 
1C5E: D4 93 1C        CALL    NC,$1C93            ; {}
1C61: CB 19           RR      C                   
1C63: 10 F0           DJNZ    $1C55               ; {}
1C65: DD 2C           INC     IXL                 
1C67: DD 4C           LD      C,IXH               
1C69: 06 04           LD      B,$04               
1C6B: 79              LD      A,C                 
1C6C: E6 07           AND     $07                 
1C6E: C4 93 1C        CALL    NZ,$1C93            ; {}
1C71: CB 19           RR      C                   
1C73: 10 F6           DJNZ    $1C6B               ; {}
1C75: DD 2C           INC     IXL                 
1C77: 11 30 88        LD      DE,$8830            
1C7A: 06 04           LD      B,$04               
1C7C: 1A              LD      A,(DE)              
1C7D: 3D              DEC     A                   
1C7E: 28 26           JR      Z,$1CA6             ; {}
1C80: 1C              INC     E                   
1C81: 1C              INC     E                   
1C82: 10 F8           DJNZ    $1C7C               ; {}
1C84: 21 00 88        LD      HL,$8800            
1C87: 06 04           LD      B,$04               
1C89: 7E              LD      A,(HL)              
1C8A: 3D              DEC     A                   
1C8B: CA 2B 1D        JP      Z,$1D2B             ; {}
1C8E: 2C              INC     L                   
1C8F: 2C              INC     L                   
1C90: 10 F7           DJNZ    $1C89               ; {}
1C92: C9              RET                         
1C93: 78              LD      A,B                 
1C94: CB 4F           BIT     1,A                 
1C96: 28 02           JR      Z,$1C9A             ; {}
1C98: EE 01           XOR     $01                 
1C9A: E6 03           AND     $03                 
1C9C: CB 27           SLA     A                   
1C9E: C6 30           ADD     $30                 
1CA0: 5F              LD      E,A                 
1CA1: 1A              LD      A,(DE)              
1CA2: FE 01           CP      $01                 
1CA4: C0              RET     NZ                  
1CA5: E1              POP     HL                  
1CA6: FD 21 11 04     LD      IY,$0411            
1CAA: 3A 0B 92        LD      A,($920B)           
1CAD: A7              AND     A                   
1CAE: 20 04           JR      NZ,$1CB4            ; {}
1CB0: FD 21 F1 00     LD      IY,$00F1            
1CB4: 7B              LD      A,E                 
1CB5: 0F              RRCA                        
1CB6: 0F              RRCA                        
1CB7: 7B              LD      A,E                 
1CB8: 17              RLA                         
1CB9: 0F              RRCA                        
1CBA: 32 CA 92        LD      ($92CA),A           
1CBD: 08              EX      AF,AF'              
1CBE: FD 22 CB 92     LD      ($92CB),IY          
1CC2: 04              INC     B                   
1CC3: 7B              LD      A,E                 
1CC4: E6 07           AND     $07                 
1CC6: 21 30 98        LD      HL,$9830            
1CC9: D7              RST     0X10                
1CCA: DD 7D           LD      A,IXL               
1CCC: EB              EX      DE,HL               
1CCD: 21 03 1D        LD      HL,$1D03            
1CD0: CF              RST     0X08                
1CD1: 7E              LD      A,(HL)              
1CD2: 12              LD      (DE),A              
1CD3: 23              INC     HL                  
1CD4: 1C              INC     E                   
1CD5: 7E              LD      A,(HL)              
1CD6: 12              LD      (DE),A              
1CD7: DD 7D           LD      A,IXL               
1CD9: FE 02           CP      $02                 
1CDB: 28 0C           JR      Z,$1CE9             ; {}
1CDD: 11 CD 92        LD      DE,$92CD            
1CE0: 3D              DEC     A                   
1CE1: 28 03           JR      Z,$1CE6             ; {}
1CE3: CD 09 1D        CALL    $1D09               ; {}
1CE6: CD 09 1D        CALL    $1D09               ; {}
1CE9: 3A CA 92        LD      A,($92CA)           
1CEC: E6 07           AND     $07                 
1CEE: 6F              LD      L,A                 
1CEF: 26 88           LD      H,$88               
1CF1: 7E              LD      A,(HL)              
1CF2: 3D              DEC     A                   
1CF3: C0              RET     NZ                  
1CF4: 4D              LD      C,L                 
1CF5: 21 CA 92        LD      HL,$92CA            
1CF8: 2C              INC     L                   
1CF9: 2C              INC     L                   
1CFA: 2C              INC     L                   
1CFB: 7E              LD      A,(HL)              
1CFC: 3C              INC     A                   
1CFD: 20 F9           JR      NZ,$1CF8            ; {}
1CFF: 08              EX      AF,AF'              
1D00: 79              LD      A,C                 
1D01: 18 19           JR      $1D1C               ; {}
1D03: 0D              DEC     C                   
1D04: BA              CP      D                   
1D05: 05              DEC     B                   
1D06: B7              OR      A                   
1D07: 01 B5 CB        LD      BC,$CBB5            
1D0A: 09              ADD     HL,BC               
1D0B: 38 06           JR      C,$1D13             ; {}
1D0D: 05              DEC     B                   
1D0E: CB 09           RRC     C                   
1D10: 38 01           JR      C,$1D13             ; {}
1D12: 05              DEC     B                   
1D13: 78              LD      A,B                 
1D14: 05              DEC     B                   
1D15: 21 32 1D        LD      HL,$1D32            
1D18: D7              RST     0X10                
1D19: 08              EX      AF,AF'              
1D1A: 7E              LD      A,(HL)              
1D1B: EB              EX      DE,HL               
1D1C: 17              RLA                         
1D1D: 0F              RRCA                        
1D1E: 77              LD      (HL),A              
1D1F: 08              EX      AF,AF'              
1D20: 2C              INC     L                   
1D21: FD 7D           LD      A,IYL               
1D23: 77              LD      (HL),A              
1D24: 2C              INC     L                   
1D25: FD 7C           LD      A,IYH               
1D27: 77              LD      (HL),A              
1D28: 2C              INC     L                   
1D29: EB              EX      DE,HL               
1D2A: C9              RET                         
1D2B: 11 44 04        LD      DE,$0444            
1D2E: CD 83 10        CALL    $1083               ; {}
1D31: C9              RET                         
1D32: 4A              LD      C,D                 
1D33: 52              LD      D,D                 
1D34: 5A              LD      E,D                 
1D35: 58              LD      E,B                 
1D36: 50              LD      D,B                 
1D37: 48              LD      C,B                 
1D38: 21 B4 99        LD      HL,$99B4            
1D3B: 7E              LD      A,(HL)              
1D3C: E6 7F           AND     $7F                 
1D3E: D6 7E           SUB     $7E                 
1D40: 28 36           JR      Z,$1D78             ; {}
1D42: 4E              LD      C,(HL)              
1D43: 34              INC     (HL)                
1D44: 3A 15 92        LD      A,($9215)           
1D47: CB 01           RLC     C                   
1D49: A9              XOR     C                   
1D4A: 0F              RRCA                        
1D4B: 3E 01           LD      A,$01               
1D4D: 38 02           JR      C,$1D51             ; {}
1D4F: ED 44           NEG                         
1D51: 4F              LD      C,A                 
1D52: 21 14 98        LD      HL,$9814            
1D55: 06 06           LD      B,$06               
1D57: 7E              LD      A,(HL)              
1D58: 81              ADD     A,C                 
1D59: 77              LD      (HL),A              
1D5A: 1F              RRA                         
1D5B: A9              XOR     C                   
1D5C: 2C              INC     L                   
1D5D: 07              RLCA                        
1D5E: 30 04           JR      NC,$1D64            ; {}
1D60: 7E              LD      A,(HL)              
1D61: EE 01           XOR     $01                 
1D63: 77              LD      (HL),A              
1D64: 2C              INC     L                   
1D65: 10 F0           DJNZ    $1D57               ; {}
1D67: 3A A0 92        LD      A,($92A0)           
1D6A: E6 FC           AND     $FC                 
1D6C: 3C              INC     A                   
1D6D: F5              PUSH    AF                  
1D6E: CD EE 23        CALL    $23EE               ; {}
1D71: F1              POP     AF                  
1D72: C6 02           ADD     $02                 
1D74: CD EE 23        CALL    $23EE               ; {}
1D77: C9              RET                         
1D78: 32 0E 90        LD      ($900E),A           
1D7B: C9              RET                         
1D7C: 3A 15 92        LD      A,($9215)           
1D7F: 47              LD      B,A                 
1D80: 21 B9 99        LD      HL,$99B9            
1D83: 7E              LD      A,(HL)              
1D84: 2C              INC     L                   
1D85: A7              AND     A                   
1D86: 28 26           JR      Z,$1DAE             ; {}
1D88: 7E              LD      A,(HL)              
1D89: A7              AND     A                   
1D8A: 3E FD           LD      A,$FD               
1D8C: 20 13           JR      NZ,$1DA1            ; {}
1D8E: 2C              INC     L                   
1D8F: 7E              LD      A,(HL)              
1D90: 2C              INC     L                   
1D91: BE              CP      (HL)                
1D92: 28 01           JR      Z,$1D95             ; {}
1D94: 34              INC     (HL)                
1D95: 7E              LD      A,(HL)              
1D96: 2C              INC     L                   
1D97: 86              ADD     A,(HL)              
1D98: 4F              LD      C,A                 
1D99: E6 3F           AND     $3F                 
1D9B: 77              LD      (HL),A              
1D9C: 79              LD      A,C                 
1D9D: 07              RLCA                        
1D9E: 07              RLCA                        
1D9F: E6 03           AND     $03                 
1DA1: CB 40           BIT     0,B                 
1DA3: 20 02           JR      NZ,$1DA7            ; {}
1DA5: ED 44           NEG                         
1DA7: 3D              DEC     A                   
1DA8: E6 07           AND     $07                 
1DAA: 32 BE 99        LD      ($99BE),A           
1DAD: C9              RET                         
1DAE: AF              XOR     A                   
1DAF: 77              LD      (HL),A              
1DB0: 2C              INC     L                   
1DB1: 2C              INC     L                   
1DB2: 77              LD      (HL),A              
1DB3: 2C              INC     L                   
1DB4: 77              LD      (HL),A              
1DB5: 3E 07           LD      A,$07               
1DB7: 18 F1           JR      $1DAA               ; {}
1DB9: 21 00 92        LD      HL,$9200            
1DBC: 06 30           LD      B,$30               
1DBE: CB 7E           BIT     7,(HL)              
1DC0: 20 05           JR      NZ,$1DC7            ; {}
1DC2: 2C              INC     L                   
1DC3: 2C              INC     L                   
1DC4: 10 F8           DJNZ    $1DBE               ; {}
1DC6: C9              RET                         
1DC7: CB BE           RES     7,(HL)              
1DC9: 26 88           LD      H,$88               
1DCB: 36 04           LD      (HL),$04            
1DCD: 2C              INC     L                   
1DCE: 36 40           LD      (HL),$40            
1DD0: 26 8B           LD      H,$8B               
1DD2: 36 0A           LD      (HL),$0A            
1DD4: 26 92           LD      H,$92               
1DD6: 18 EB           JR      $1DC3               ; {}
1DD8: 3A A2 92        LD      A,($92A2)           
1DDB: E6 01           AND     $01                 
1DDD: C0              RET     NZ                  
1DDE: 21 AC 92        LD      HL,$92AC            
1DE1: 06 04           LD      B,$04               
1DE3: 7E              LD      A,(HL)              
1DE4: A7              AND     A                   
1DE5: 28 01           JR      Z,$1DE8             ; {}
1DE7: 35              DEC     (HL)                
1DE8: 2C              INC     L                   
1DE9: 10 F8           DJNZ    $1DE3               ; {}
1DEB: C9              RET                         
1DEC: 3A A0 92        LD      A,($92A0)           
1DEF: E6 03           AND     $03                 
1DF1: C0              RET     NZ                  
1DF2: 21 0F 92        LD      HL,$920F            
1DF5: 7E              LD      A,(HL)              
1DF6: 5F              LD      E,A                 
1DF7: 16 FF           LD      D,$FF               
1DF9: CB 7F           BIT     7,A                 
1DFB: 20 05           JR      NZ,$1E02            ; {}
1DFD: 14              INC     D                   
1DFE: 14              INC     D                   
1DFF: 34              INC     (HL)                
1E00: 18 01           JR      $1E03               ; {}
1E02: 35              DEC     (HL)                
1E03: FE 1F           CP      $1F                 
1E05: 20 02           JR      NZ,$1E09            ; {}
1E07: CB FE           SET     7,(HL)              
1E09: FE 81           CP      $81                 
1E0B: 20 02           JR      NZ,$1E0F            ; {}
1E0D: CB BE           RES     7,(HL)              
1E0F: 4E              LD      C,(HL)              
1E10: E6 07           AND     $07                 
1E12: 7A              LD      A,D                 
1E13: 32 11 92        LD      ($9211),A           
1E16: 7B              LD      A,E                 
1E17: 20 10           JR      NZ,$1E29            ; {}
1E19: 21 6A 1E        LD      HL,$1E6A            
1E1C: 79              LD      A,C                 
1E1D: E6 18           AND     $18                 
1E1F: CF              RST     0X08                
1E20: 7B              LD      A,E                 
1E21: 11 20 99        LD      DE,$9920            
1E24: 01 10 00        LD      BC,$0010            
1E27: ED B0           LDIR                        
1E29: 21 15 92        LD      HL,$9215            
1E2C: 07              RLCA                        
1E2D: AE              XOR     (HL)                
1E2E: 0F              RRCA                        
1E2F: 21 20 99        LD      HL,$9920            
1E32: 11 00 99        LD      DE,$9900            
1E35: 30 05           JR      NC,$1E3C            ; {}
1E37: 01 FF 01        LD      BC,$01FF            
1E3A: 18 03           JR      $1E3F               ; {}
1E3C: 01 01 FF        LD      BC,$FF01            
1E3F: DD 2E 05        LD      IXL,$05             
1E42: CD 49 1E        CALL    $1E49               ; {}
1E45: 41              LD      B,C                 
1E46: DD 2E 0B        LD      IXL,$0B             
1E49: CB 0E           RRC     (HL)                
1E4B: 30 15           JR      NC,$1E62            ; {}
1E4D: 1A              LD      A,(DE)              
1E4E: 80              ADD     A,B                 
1E4F: 12              LD      (DE),A              
1E50: 16 98           LD      D,$98               
1E52: 1A              LD      A,(DE)              
1E53: 80              ADD     A,B                 
1E54: 12              LD      (DE),A              
1E55: 1F              RRA                         
1E56: A8              XOR     B                   
1E57: 07              RLCA                        
1E58: 30 06           JR      NC,$1E60            ; {}
1E5A: 1C              INC     E                   
1E5B: 1A              LD      A,(DE)              
1E5C: EE 01           XOR     $01                 
1E5E: 12              LD      (DE),A              
1E5F: 1D              DEC     E                   
1E60: 16 99           LD      D,$99               
1E62: 1C              INC     E                   
1E63: 1C              INC     E                   
1E64: 2C              INC     L                   
1E65: DD 2D           DEC     IXL                 
1E67: 20 E0           JR      NZ,$1E49            ; {}
1E69: C9              RET                         
1E6A: FF              RST     0X38                
1E6B: 77              LD      (HL),A              
1E6C: 55              LD      D,L                 
1E6D: 14              INC     D                   
1E6E: 10 10           DJNZ    $1E80               ; {}
1E70: 14              INC     D                   
1E71: 55              LD      D,L                 
1E72: 77              LD      (HL),A              
1E73: FF              RST     0X38                
1E74: 00              NOP                         
1E75: 10 14           DJNZ    $1E8B               ; {}
1E77: 55              LD      D,L                 
1E78: 77              LD      (HL),A              
1E79: FF              RST     0X38                
1E7A: FF              RST     0X38                
1E7B: 77              LD      (HL),A              
1E7C: 55              LD      D,L                 
1E7D: 51              LD      D,C                 
1E7E: 10 10           DJNZ    $1E90               ; {}
1E80: 51              LD      D,C                 
1E81: 55              LD      D,L                 
1E82: 77              LD      (HL),A              
1E83: FF              RST     0X38                
1E84: 00              NOP                         
1E85: 10 51           DJNZ    $1ED8               ; {}
1E87: 55              LD      D,L                 
1E88: 77              LD      (HL),A              
1E89: FF              RST     0X38                
1E8A: FF              RST     0X38                
1E8B: 77              LD      (HL),A              
1E8C: 57              LD      D,A                 
1E8D: 15              DEC     D                   
1E8E: 10 10           DJNZ    $1EA0               ; {}
1E90: 15              DEC     D                   
1E91: 57              LD      D,A                 
1E92: 77              LD      (HL),A              
1E93: FF              RST     0X38                
1E94: 00              NOP                         
1E95: 10 15           DJNZ    $1EAC               ; {}
1E97: 57              LD      D,A                 
1E98: 77              LD      (HL),A              
1E99: FF              RST     0X38                
1E9A: FF              RST     0X38                
1E9B: F7              RST     0X30                
1E9C: D5              PUSH    DE                  
1E9D: 91              SUB     C                   
1E9E: 10 10           DJNZ    $1EB0               ; {}
1EA0: 91              SUB     C                   
1EA1: D5              PUSH    DE                  
1EA2: F7              RST     0X30                
1EA3: FF              RST     0X38                
1EA4: 00              NOP                         
1EA5: 10 91           DJNZ    $1E38               ; {}
1EA7: D5              PUSH    DE                  
1EA8: F7              RST     0X30                
1EA9: FF              RST     0X38                
1EAA: 3A A0 92        LD      A,($92A0)           
1EAD: E6 01           AND     $01                 
1EAF: C6 02           ADD     $02                 
1EB1: 47              LD      B,A                 
1EB2: 3A 15 92        LD      A,($9215)           
1EB5: A7              AND     A                   
1EB6: 78              LD      A,B                 
1EB7: 28 02           JR      Z,$1EBB             ; {}
1EB9: ED 44           NEG                         
1EBB: DD 67           LD      IXH,A               
1EBD: 2E 68           LD      L,$68               
1EBF: 11 B0 92        LD      DE,$92B0            
1EC2: DD 2E 08        LD      IXL,$08             
1EC5: 26 8B           LD      H,$8B               
1EC7: 7E              LD      A,(HL)              
1EC8: FE 30           CP      $30                 
1ECA: 20 39           JR      NZ,$1F05            ; {}
1ECC: 26 93           LD      H,$93               
1ECE: 7E              LD      A,(HL)              
1ECF: A7              AND     A                   
1ED0: 28 33           JR      Z,$1F05             ; {}
1ED2: EB              EX      DE,HL               
1ED3: 46              LD      B,(HL)              
1ED4: 78              LD      A,B                 
1ED5: E6 7E           AND     $7E                 
1ED7: 2C              INC     L                   
1ED8: 86              ADD     A,(HL)              
1ED9: 4F              LD      C,A                 
1EDA: E6 1F           AND     $1F                 
1EDC: 77              LD      (HL),A              
1EDD: 2C              INC     L                   
1EDE: 79              LD      A,C                 
1EDF: 07              RLCA                        
1EE0: 07              RLCA                        
1EE1: 07              RLCA                        
1EE2: E6 07           AND     $07                 
1EE4: CB 78           BIT     7,B                 
1EE6: 28 02           JR      Z,$1EEA             ; {}
1EE8: ED 44           NEG                         
1EEA: EB              EX      DE,HL               
1EEB: 86              ADD     A,(HL)              
1EEC: 77              LD      (HL),A              
1EED: 2C              INC     L                   
1EEE: 7E              LD      A,(HL)              
1EEF: DD 84           ADD     A,IXH               
1EF1: 77              LD      (HL),A              
1EF2: 1F              RRA                         
1EF3: DD AC           XOR     IXH                 
1EF5: 07              RLCA                        
1EF6: 30 07           JR      NC,$1EFF            ; {}
1EF8: 26 9B           LD      H,$9B               
1EFA: CB 0E           RRC     (HL)                
1EFC: 3F              CCF                         
1EFD: CB 16           RL      (HL)                
1EFF: 2C              INC     L                   
1F00: DD 2D           DEC     IXL                 
1F02: 20 C1           JR      NZ,$1EC5            ; {}
1F04: C9              RET                         


1F05: 26 88           LD      H,$88               
1F07: 36 80           LD      (HL),$80            
1F09: 2C              INC     L                   
1F0A: 1C              INC     E                   
1F0B: 1C              INC     E                   
1F0C: 18 F1           JR      $1EFF               ; {}
           
1F0E: 3A 15 92        LD      A,($9215)           
1F11: C6 B6           ADD     $B6                 
1F13: 6F              LD      L,A                 
1F14: 26 99           LD      H,$99               
1F16: CB 66           BIT     4,(HL)              
1F18: C0              RET     NZ                  
1F19: 21 64 93        LD      HL,$9364            
1F1C: 11 A4 92        LD      DE,$92A4            
1F1F: AF              XOR     A                   
1F20: BE              CP      (HL)                
1F21: 28 05           JR      Z,$1F28             ; {}
1F23: 2E 66           LD      L,$66               
1F25: 1C              INC     E                   
1F26: BE              CP      (HL)                
1F27: C0              RET     NZ                  
1F28: D5              PUSH    DE                  
1F29: EB              EX      DE,HL               
1F2A: 21 63 9B        LD      HL,$9B63            
1F2D: 54              LD      D,H                 
1F2E: 1C              INC     E                   
1F2F: CB 56           BIT     2,(HL)              
1F31: 28 02           JR      Z,$1F35             ; {}
1F33: D1              POP     DE                  
1F34: C9              RET                         
1F35: ED A8           LDD                         
1F37: 26 93           LD      H,$93               
1F39: 54              LD      D,H                 
1F3A: ED A0           LDI                         
1F3C: ED A8           LDD                         
1F3E: 26 9B           LD      H,$9B               
1F40: 54              LD      D,H                 
1F41: 46              LD      B,(HL)              
1F42: EB              EX      DE,HL               
1F43: 3A 27 98        LD      A,($9827)           
1F46: E6 01           AND     $01                 
1F48: 07              RLCA                        
1F49: 07              RLCA                        
1F4A: 07              RLCA                        
1F4B: B0              OR      B                   
1F4C: 77              LD      (HL),A              
1F4D: 16 8B           LD      D,$8B               
1F4F: 1A              LD      A,(DE)              
1F50: 62              LD      H,D                 
1F51: E6 07           AND     $07                 
1F53: 0E 30           LD      C,$30               
1F55: FE 05           CP      $05                 
1F57: 30 07           JR      NC,$1F60            ; {}
1F59: 0C              INC     C                   
1F5A: FE 02           CP      $02                 
1F5C: 30 02           JR      NC,$1F60            ; {}
1F5E: 0C              INC     C                   
1F5F: 0C              INC     C                   
1F60: 71              LD      (HL),C              
1F61: FE 04           CP      $04                 
1F63: 38 03           JR      C,$1F68             ; {}
1F65: 2F              CPL                         
1F66: C6 47           ADD     $47                 
1F68: CB 27           SLA     A                   
1F6A: 4F              LD      C,A                 
1F6B: 78              LD      A,B                 
1F6C: 0F              RRCA                        
1F6D: 0F              RRCA                        
1F6E: 0F              RRCA                        
1F6F: E6 60           AND     $60                 
1F71: 47              LD      B,A                 
1F72: 3A 15 92        LD      A,($9215)           
1F75: A7              AND     A                   
1F76: 78              LD      A,B                 
1F77: 20 02           JR      NZ,$1F7B            ; {}
1F79: EE 60           XOR     $60                 
1F7B: B1              OR      C                   
1F7C: D1              POP     DE                  
1F7D: 12              LD      (DE),A              
1F7E: 26 88           LD      H,$88               
1F80: 36 06           LD      (HL),$06            
1F82: 3E 01           LD      A,$01               
1F84: 32 AF 9A        LD      ($9AAF),A           
1F87: 2A 46 98        LD      HL,($9846)          
1F8A: 23              INC     HL                  
1F8B: 22 46 98        LD      ($9846),HL          
1F8E: C9              RET                         
1F8F: 3A 27 98        LD      A,($9827)           
1F92: 5F              LD      E,A                 
1F93: 3A 15 92        LD      A,($9215)           
1F96: C6 B6           ADD     $B6                 
1F98: 6F              LD      L,A                 
1F99: 26 99           LD      H,$99               
1F9B: 7E              LD      A,(HL)              
1F9C: E6 0A           AND     $0A                 
1F9E: FE 0A           CP      $0A                 
1FA0: 28 37           JR      Z,$1FD9             ; {}
1FA2: 21 15 92        LD      HL,$9215            
1FA5: CB 46           BIT     0,(HL)              
1FA7: 28 02           JR      Z,$1FAB             ; {}
1FA9: EE 0A           XOR     $0A                 
1FAB: 21 A3 92        LD      HL,$92A3            
1FAE: 47              LD      B,A                 
1FAF: 0E 01           LD      C,$01               
1FB1: 7E              LD      A,(HL)              
1FB2: EE 01           XOR     $01                 
1FB4: 77              LD      (HL),A              
1FB5: 20 01           JR      NZ,$1FB8            ; {}
1FB7: 0C              INC     C                   
1FB8: 21 62 93        LD      HL,$9362            
1FBB: 7E              LD      A,(HL)              
1FBC: A7              AND     A                   
1FBD: C8              RET     Z                   
1FBE: CB 48           BIT     1,B                 
1FC0: 20 0F           JR      NZ,$1FD1            ; {}
1FC2: 7E              LD      A,(HL)              
1FC3: FE D1           CP      $D1                 
1FC5: 38 03           JR      C,$1FCA             ; {}
1FC7: CB 43           BIT     0,E                 
1FC9: C0              RET     NZ                  
1FCA: FE E1           CP      $E1                 
1FCC: D0              RET     NC                  
1FCD: 81              ADD     A,C                 
1FCE: 77              LD      (HL),A              
1FCF: 18 0D           JR      $1FDE               ; {}
1FD1: 7E              LD      A,(HL)              
1FD2: FE 12           CP      $12                 
1FD4: D8              RET     C                   
1FD5: 91              SUB     C                   
1FD6: 77              LD      (HL),A              
1FD7: 18 05           JR      $1FDE               ; {}
1FD9: AF              XOR     A                   
1FDA: 32 A3 92        LD      ($92A3),A           
1FDD: C9              RET                         
1FDE: CB 43           BIT     0,E                 
1FE0: C8              RET     Z                   
1FE1: C6 0F           ADD     $0F                 
1FE3: 32 60 93        LD      ($9360),A           
1FE6: C9              RET                         
1FE7: FF              RST     0X38                
1FE8: FF              RST     0X38                
1FE9: FF              RST     0X38                
1FEA: FF              RST     0X38                
1FEB: FF              RST     0X38                
1FEC: FF              RST     0X38                
1FED: FF              RST     0X38                
1FEE: FF              RST     0X38                
1FEF: FF              RST     0X38                
1FF0: FF              RST     0X38                
1FF1: FF              RST     0X38                
1FF2: FF              RST     0X38                
1FF3: FF              RST     0X38                
1FF4: FF              RST     0X38                
1FF5: FF              RST     0X38                
1FF6: FF              RST     0X38                
1FF7: FF              RST     0X38                
1FF8: FF              RST     0X38                
1FF9: FF              RST     0X38                
1FFA: FF              RST     0X38                
1FFB: FF              RST     0X38                
1FFC: FF              RST     0X38                
1FFD: FF              RST     0X38                
1FFE: FF              RST     0X38                
1FFF: 10 3A           DJNZ    $203B               ; {}
2001: 28 98           JR      Z,$1F9B             ; {}
2003: 6F              LD      L,A                 
2004: 26 88           LD      H,$88               
2006: 7E              LD      A,(HL)              
2007: A7              AND     A                   
2008: C2 BF 20        JP      NZ,$20BF            ; {}
200B: 3A 8B 92        LD      A,($928B)           
200E: A7              AND     A                   
200F: CA C7 20        JP      Z,$20C7             ; {}
2012: 3D              DEC     A                   
2013: CA D1 20        JP      Z,$20D1             ; {}
2016: 26 93           LD      H,$93               
2018: 7E              LD      A,(HL)              
2019: FE 80           CP      $80                 
201B: 28 09           JR      Z,$2026             ; {}
201D: F2 23 20        JP      P,$2023             ; {}
2020: 34              INC     (HL)                
2021: 18 3B           JR      $205E               ; {}
2023: 35              DEC     (HL)                
2024: 18 38           JR      $205E               ; {}
2026: 2C              INC     L                   
2027: 3A 15 92        LD      A,($9215)           
202A: A7              AND     A                   
202B: 20 1F           JR      NZ,$204C            ; {}
202D: 7E              LD      A,(HL)              
202E: FE 29           CP      $29                 
2030: 20 0F           JR      NZ,$2041            ; {}
2032: 26 9B           LD      H,$9B               
2034: 7E              LD      A,(HL)              
2035: 26 93           LD      H,$93               
2037: 3D              DEC     A                   
2038: 20 07           JR      NZ,$2041            ; {}
203A: 3E 03           LD      A,$03               
203C: 32 8B 92        LD      ($928B),A           
203F: 18 1D           JR      $205E               ; {}
2041: 34              INC     (HL)                
2042: 20 1A           JR      NZ,$205E            ; {}
2044: 26 9B           LD      H,$9B               
2046: 7E              LD      A,(HL)              
2047: EE 01           XOR     $01                 
2049: 77              LD      (HL),A              
204A: 18 12           JR      $205E               ; {}
204C: 7E              LD      A,(HL)              
204D: FE 37           CP      $37                 
204F: 20 08           JR      NZ,$2059            ; {}
2051: 26 9B           LD      H,$9B               
2053: 7E              LD      A,(HL)              
2054: 26 93           LD      H,$93               
2056: A7              AND     A                   
2057: 28 E1           JR      Z,$203A             ; {}
2059: 35              DEC     (HL)                
205A: 7E              LD      A,(HL)              
205B: 3C              INC     A                   
205C: 28 E6           JR      Z,$2044             ; {}
205E: 21 62 8B        LD      HL,$8B62            
2061: 7E              LD      A,(HL)              
2062: D6 06           SUB     $06                 
2064: 4F              LD      C,A                 
2065: 26 93           LD      H,$93               
2067: 20 0C           JR      NZ,$2075            ; {}
2069: 7E              LD      A,(HL)              
206A: FE 71           CP      $71                 
206C: 28 07           JR      Z,$2075             ; {}
206E: F2 73 20        JP      P,$2073             ; {}
2071: 34              INC     (HL)                
2072: C9              RET                         
2073: 35              DEC     (HL)                
2074: C9              RET                         
2075: 3A 8B 92        LD      A,($928B)           
2078: FE 03           CP      $03                 
207A: C0              RET     NZ                  
207B: 3A 28 98        LD      A,($9828)           
207E: 6F              LD      L,A                 
207F: 36 00           LD      (HL),$00            
2081: 2C              INC     L                   
2082: 0D              DEC     C                   
2083: 0C              INC     C                   
2084: 28 09           JR      Z,$208F             ; {}
2086: 11 63 93        LD      DE,$9363            
2089: AF              XOR     A                   
208A: 32 2B 98        LD      ($982B),A           
208D: 18 08           JR      $2097               ; {}
208F: 3E 01           LD      A,$01               
2091: 32 27 98        LD      ($9827),A           
2094: 11 61 93        LD      DE,$9361            
2097: 7E              LD      A,(HL)              
2098: 12              LD      (DE),A              
2099: 26 9B           LD      H,$9B               
209B: 54              LD      D,H                 
209C: 7E              LD      A,(HL)              
209D: 12              LD      (DE),A              
209E: 2D              DEC     L                   
209F: 26 88           LD      H,$88               
20A1: 36 80           LD      (HL),$80            
20A3: 26 8B           LD      H,$8B               
20A5: 6B              LD      L,E                 
20A6: 2D              DEC     L                   
20A7: 36 06           LD      (HL),$06            
20A9: 2C              INC     L                   
20AA: 36 09           LD      (HL),$09            
20AC: 2D              DEC     L                   
20AD: 26 93           LD      H,$93               
20AF: 36 80           LD      (HL),$80            
20B1: 3E 01           LD      A,$01               
20B3: 32 14 90        LD      ($9014),A           
20B6: 32 15 90        LD      ($9015),A           
20B9: 32 25 90        LD      ($9025),A           
20BC: 32 B9 99        LD      ($99B9),A           
20BF: AF              XOR     A                   
20C0: 32 1D 90        LD      ($901D),A           
20C3: 32 B1 9A        LD      ($9AB1),A           
20C6: C9              RET                         
20C7: 3C              INC     A                   
20C8: 32 8B 92        LD      ($928B),A           
20CB: 3E 02           LD      A,$02               
20CD: 32 AD 92        LD      ($92AD),A           
20D0: C9              RET                         
20D1: 26 9B           LD      H,$9B               
20D3: 3A AD 92        LD      A,($92AD)           
20D6: 5F              LD      E,A                 
20D7: 3A 87 92        LD      A,($9287)           
20DA: B3              OR      E                   
20DB: 32 8D 92        LD      ($928D),A           
20DE: CD 96 21        CALL    $2196               ; {}
20E1: 05              DEC     B                   
20E2: C0              RET     NZ                  
20E3: 32 14 90        LD      ($9014),A           
20E6: 32 15 90        LD      ($9015),A           
20E9: 32 25 90        LD      ($9025),A           
20EC: 3E 02           LD      A,$02               
20EE: 32 8B 92        LD      ($928B),A           
20F1: C9              RET                         
20F2: 21 62 8B        LD      HL,$8B62            
20F5: 7E              LD      A,(HL)              
20F6: FE 40           CP      $40                 
20F8: 38 08           JR      C,$2102             ; {}
20FA: AF              XOR     A                   
20FB: 32 1C 90        LD      ($901C),A           
20FE: 32 BA 99        LD      ($99BA),A           
2101: C9              RET                         
2102: 26 9B           LD      H,$9B               
2104: CD 96 21        CALL    $2196               ; {}
2107: CB 40           BIT     0,B                 
2109: 20 54           JR      NZ,$215F            ; {}
210B: 3A 8B 92        LD      A,($928B)           
210E: CB 7F           BIT     7,A                 
2110: 20 59           JR      NZ,$216B            ; {}
2112: 3A 8D 92        LD      A,($928D)           
2115: A7              AND     A                   
2116: C8              RET     Z                   
2117: 26 93           LD      H,$93               
2119: 3A 28 98        LD      A,($9828)           
211C: 5F              LD      E,A                 
211D: 54              LD      D,H                 
211E: 1A              LD      A,(DE)              
211F: BE              CP      (HL)                
2120: 28 07           JR      Z,$2129             ; {}
2122: F2 28 21        JP      P,$2128             ; {}
2125: 35              DEC     (HL)                
2126: 18 01           JR      $2129               ; {}
2128: 34              INC     (HL)                
2129: 2C              INC     L                   
212A: 3A 15 92        LD      A,($9215)           
212D: A7              AND     A                   
212E: 28 0B           JR      Z,$213B             ; {}
2130: 34              INC     (HL)                
2131: 7E              LD      A,(HL)              
2132: FE 7A           CP      $7A                 
2134: 28 24           JR      Z,$215A             ; {}
2136: FE 80           CP      $80                 
2138: 28 16           JR      Z,$2150             ; {}
213A: C9              RET                         
213B: 35              DEC     (HL)                
213C: 7E              LD      A,(HL)              
213D: 3C              INC     A                   
213E: 20 08           JR      NZ,$2148            ; {}
2140: 26 9B           LD      H,$9B               
2142: 7E              LD      A,(HL)              
2143: EE 01           XOR     $01                 
2145: 77              LD      (HL),A              
2146: 26 93           LD      H,$93               
2148: 7E              LD      A,(HL)              
2149: FE E6           CP      $E6                 
214B: 28 0D           JR      Z,$215A             ; {}
214D: FE E0           CP      $E0                 
214F: C0              RET     NZ                  
2150: AF              XOR     A                   
2151: 32 8D 92        LD      ($928D),A           
2154: 3E 07           LD      A,$07               
2156: 32 63 8B        LD      ($8B63),A           
2159: C9              RET                         
215A: AF              XOR     A                   
215B: 32 15 90        LD      ($9015),A           
215E: C9              RET                         
215F: 3A 15 90        LD      A,($9015)           
2162: A7              AND     A                   
2163: 20 06           JR      NZ,$216B            ; {}
2165: 3C              INC     A                   
2166: 32 0D 92        LD      ($920D),A           
2169: 18 22           JR      $218D               ; {}
216B: 26 93           LD      H,$93               
216D: 2C              INC     L                   
216E: 3A 15 92        LD      A,($9215)           
2171: A7              AND     A                   
2172: 28 07           JR      Z,$217B             ; {}
2174: 7E              LD      A,(HL)              
2175: FE 37           CP      $37                 
2177: 28 12           JR      Z,$218B             ; {}
2179: 35              DEC     (HL)                
217A: C9              RET                         
217B: 7E              LD      A,(HL)              
217C: FE 29           CP      $29                 
217E: 28 0B           JR      Z,$218B             ; {}
2180: 34              INC     (HL)                
2181: C0              RET     NZ                  
2182: 26 9B           LD      H,$9B               
2184: 7E              LD      A,(HL)              
2185: EE 01           XOR     $01                 
2187: 77              LD      (HL),A              
2188: 26 93           LD      H,$93               
218A: C9              RET                         
218B: 05              DEC     B                   
218C: C0              RET     NZ                  
218D: AF              XOR     A                   
218E: 32 1C 90        LD      ($901C),A           
2191: 3C              INC     A                   
2192: 32 25 90        LD      ($9025),A           
2195: C9              RET                         
2196: 7E              LD      A,(HL)              
2197: 4F              LD      C,A                 
2198: CB 3F           SRL     A                   
219A: A9              XOR     C                   
219B: 4F              LD      C,A                 
219C: 26 8B           LD      H,$8B               
219E: 06 00           LD      B,$00               
21A0: 7E              LD      A,(HL)              
21A1: E6 07           AND     $07                 
21A3: FE 06           CP      $06                 
21A5: 20 0E           JR      NZ,$21B5            ; {}
21A7: 0D              DEC     C                   
21A8: 0C              INC     C                   
21A9: 20 0A           JR      NZ,$21B5            ; {}
21AB: 08              EX      AF,AF'              
21AC: 3A 8D 92        LD      A,($928D)           
21AF: A7              AND     A                   
21B0: 20 02           JR      NZ,$21B4            ; {}
21B2: 04              INC     B                   
21B3: C9              RET                         
21B4: 08              EX      AF,AF'              
21B5: CB 41           BIT     0,C                 
21B7: 20 07           JR      NZ,$21C0            ; {}
21B9: FE 06           CP      $06                 
21BB: 28 09           JR      Z,$21C6             ; {}
21BD: 34              INC     (HL)                
21BE: 18 0E           JR      $21CE               ; {}
21C0: A7              AND     A                   
21C1: 28 03           JR      Z,$21C6             ; {}
21C3: 35              DEC     (HL)                
21C4: 18 08           JR      $21CE               ; {}
21C6: 0D              DEC     C                   
21C7: F2 B5 21        JP      P,$21B5             ; {}
21CA: 0E 03           LD      C,$03               
21CC: 18 E7           JR      $21B5               ; {}
21CE: 79              LD      A,C                 
21CF: CB 4F           BIT     1,A                 
21D1: 28 02           JR      Z,$21D5             ; {}
21D3: EE 01           XOR     $01                 
21D5: 26 9B           LD      H,$9B               
21D7: 77              LD      (HL),A              
21D8: C9              RET                         
21D9: 21 28 98        LD      HL,$9828            
21DC: 5E              LD      E,(HL)              
21DD: 16 88           LD      D,$88               
21DF: 1A              LD      A,(DE)              
21E0: FE 09           CP      $09                 
21E2: 20 44           JR      NZ,$2228            ; {}
21E4: 2C              INC     L                   
21E5: 7E              LD      A,(HL)              
21E6: DD 6F           LD      IXL,A               
21E8: DD 26 91        LD      IXH,$91             
21EB: DD 7E 0A        LD      A,(IX+$0A)          
21EE: A7              AND     A                   
21EF: C0              RET     NZ                  
21F0: 3E 0C           LD      A,$0C               
21F2: DD CB 05 46     BIT     0,(IX+$05)          
21F6: 28 02           JR      Z,$21FA             ; {}
21F8: ED 44           NEG                         
21FA: DD 77 0C        LD      (IX+$0C),A          
21FD: DD 7E 05        LD      A,(IX+$05)          
2200: 0F              RRCA                        
2201: DD 7E 04        LD      A,(IX+$04)          
2204: 1F              RRA                         
2205: D6 78           SUB     $78                 
2207: FE 10           CP      $10                 
2209: D0              RET     NC                  
220A: 3A C6 99        LD      A,($99C6)           
220D: 32 2A 98        LD      ($982A),A           
2210: AF              XOR     A                   
2211: DD 77 0C        LD      (IX+$0C),A          
2214: 32 19 90        LD      ($9019),A           
2217: 32 8B 92        LD      ($928B),A           
221A: 32 0D 92        LD      ($920D),A           
221D: 3C              INC     A                   
221E: 32 18 90        LD      ($9018),A           
2221: 32 8C 92        LD      ($928C),A           
2224: 32 8D 92        LD      ($928D),A           
2227: C9              RET                         
2228: AF              XOR     A                   
2229: 32 19 90        LD      ($9019),A           
222C: 32 2B 98        LD      ($982B),A           
222F: C9              RET                         
2230: 3A A0 92        LD      A,($92A0)           
2233: 4F              LD      C,A                 
2234: E6 03           AND     $03                 
2236: 20 2D           JR      NZ,$2265            ; {}
2238: 3A 8A 92        LD      A,($928A)           
223B: ED 44           NEG                         
223D: D6 18           SUB     $18                 
223F: 26 21           LD      H,$21               
2241: 07              RLCA                        
2242: CB 14           RL      H                   
2244: 07              RLCA                        
2245: CB 14           RL      H                   
2247: E6 E0           AND     $E0                 
2249: C6 15           ADD     $15                 
224B: 6F              LD      L,A                 
224C: 79              LD      A,C                 
224D: 0F              RRCA                        
224E: 0F              RRCA                        
224F: E6 03           AND     $03                 
2251: 20 01           JR      NZ,$2254            ; {}
2253: 3C              INC     A                   
2254: C6 17           ADD     $17                 
2256: 11 16 00        LD      DE,$0016            
2259: 0E 06           LD      C,$06               
225B: 06 0A           LD      B,$0A               
225D: 77              LD      (HL),A              
225E: 2C              INC     L                   
225F: 10 FC           DJNZ    $225D               ; {}
2261: 19              ADD     HL,DE               
2262: 0D              DEC     C                   
2263: 20 F6           JR      NZ,$225B            ; {}
2265: 21 8B 92        LD      HL,$928B            
2268: CB 7E           BIT     7,(HL)              
226A: 20 0C           JR      NZ,$2278            ; {}
226C: 3A 28 98        LD      A,($9828)           
226F: 5F              LD      E,A                 
2270: 16 88           LD      D,$88               
2272: 1A              LD      A,(DE)              
2273: FE 09           CP      $09                 
2275: C2 35 23        JP      NZ,$2335            ; {}
2278: 21 8C 92        LD      HL,$928C            
227B: 35              DEC     (HL)                
227C: C2 4B 23        JP      NZ,$234B            ; {}
227F: 3A 2A 98        LD      A,($982A)           
2282: 77              LD      (HL),A              
2283: 21 8B 92        LD      HL,$928B            
2286: CB 7E           BIT     7,(HL)              
2288: 20 2F           JR      NZ,$22B9            ; {}
228A: 32 A5 9A        LD      ($9AA5),A           
228D: 3A 29 98        LD      A,($9829)           
2290: C6 0D           ADD     $0D                 
2292: 5F              LD      E,A                 
2293: 16 91           LD      D,$91               
2295: 3E FF           LD      A,$FF               
2297: 12              LD      (DE),A              
2298: 34              INC     (HL)                
2299: 7E              LD      A,(HL)              
229A: E6 0F           AND     $0F                 
229C: FE 0B           CP      $0B                 
229E: 28 40           JR      Z,$22E0             ; {}
22A0: CB 76           BIT     6,(HL)              
22A2: 20 2B           JR      NZ,$22CF            ; {}
22A4: F5              PUSH    AF                  
22A5: 4F              LD      C,A                 
22A6: 07              RLCA                        
22A7: 81              ADD     A,C                 
22A8: 21 A9 23        LD      HL,$23A9            
22AB: CF              RST     0X08                
22AC: F1              POP     AF                  
22AD: CD 98 23        CALL    $2398               ; {}
22B0: 06 06           LD      B,$06               
22B2: 7E              LD      A,(HL)              
22B3: 12              LD      (DE),A              
22B4: 23              INC     HL                  
22B5: E7              RST     0X20                
22B6: 10 FA           DJNZ    $22B2               ; {}
22B8: C9              RET                         
22B9: 34              INC     (HL)                
22BA: 7E              LD      A,(HL)              
22BB: E6 0F           AND     $0F                 
22BD: FE 0B           CP      $0B                 
22BF: 20 12           JR      NZ,$22D3            ; {}
22C1: AF              XOR     A                   
22C2: 32 18 90        LD      ($9018),A           
22C5: 32 A5 9A        LD      ($9AA5),A           
22C8: 32 A6 9A        LD      ($9AA6),A           
22CB: 32 2B 98        LD      ($982B),A           
22CE: C9              RET                         
22CF: ED 44           NEG                         
22D1: C6 0B           ADD     $0B                 
22D3: CD 98 23        CALL    $2398               ; {}
22D6: 06 06           LD      B,$06               
22D8: 0E 24           LD      C,$24               
22DA: 79              LD      A,C                 
22DB: 12              LD      (DE),A              
22DC: E7              RST     0X20                
22DD: 10 FB           DJNZ    $22DA               ; {}
22DF: C9              RET                         
22E0: CB 76           BIT     6,(HL)              
22E2: 28 46           JR      Z,$232A             ; {}
22E4: 3A 0D 92        LD      A,($920D)           
22E7: A7              AND     A                   
22E8: 28 07           JR      Z,$22F1             ; {}
22EA: CB 6E           BIT     5,(HL)              
22EC: 20 03           JR      NZ,$22F1            ; {}
22EE: 36 68           LD      (HL),$68            
22F0: C9              RET                         
22F1: AF              XOR     A                   
22F2: 32 18 90        LD      ($9018),A           
22F5: 32 A5 9A        LD      ($9AA5),A           
22F8: 32 A6 9A        LD      ($9AA6),A           
22FB: 3A 0D 92        LD      A,($920D)           
22FE: A7              AND     A                   
22FF: 3A 29 98        LD      A,($9829)           
2302: 20 0F           JR      NZ,$2313            ; {}
2304: C6 0D           ADD     $0D                 
2306: 5F              LD      E,A                 
2307: 16 91           LD      D,$91               
2309: AF              XOR     A                   
230A: 32 2B 98        LD      ($982B),A           
230D: 3C              INC     A                   
230E: 32 28 98        LD      ($9828),A           
2311: 12              LD      (DE),A              
2312: C9              RET                         
2313: C6 08           ADD     $08                 
2315: 6F              LD      L,A                 
2316: 26 91           LD      H,$91               
2318: 11 6B 04        LD      DE,$046B            
231B: 73              LD      (HL),E              
231C: 2C              INC     L                   
231D: 72              LD      (HL),D              
231E: AF              XOR     A                   
231F: 32 BA 99        LD      ($99BA),A           
2322: 3C              INC     A                   
2323: 32 11 90        LD      ($9011),A           
2326: 32 8E 92        LD      ($928E),A           
2329: C9              RET                         
232A: 3E 40           LD      A,$40               
232C: 32 8C 92        LD      ($928C),A           
232F: 3E 40           LD      A,$40               
2331: 32 8B 92        LD      ($928B),A           
2334: C9              RET                         
2335: 3E 03           LD      A,$03               
2337: 32 2A 98        LD      ($982A),A           
233A: 36 80           LD      (HL),$80            
233C: AF              XOR     A                   
233D: 32 8D 92        LD      ($928D),A           
2340: 32 BA 99        LD      ($99BA),A           
2343: 3C              INC     A                   
2344: 32 8C 92        LD      ($928C),A           
2347: 32 14 90        LD      ($9014),A           
234A: C9              RET                         
234B: 3A 8B 92        LD      A,($928B)           
234E: FE 40           CP      $40                 
2350: C0              RET     NZ                  
2351: 3A 15 92        LD      A,($9215)           
2354: 4F              LD      C,A                 
2355: 3A 62 93        LD      A,($9362)           
2358: CB 41           BIT     0,C                 
235A: 28 04           JR      Z,$2360             ; {}
235C: C6 0E           ADD     $0E                 
235E: ED 44           NEG                         
2360: 47              LD      B,A                 
2361: 3A 8A 92        LD      A,($928A)           
2364: 90              SUB     B                   
2365: C6 1B           ADD     $1B                 
2367: FE 36           CP      $36                 
2369: D0              RET     NC                  
236A: 3A 01 92        LD      A,($9201)           
236D: 3D              DEC     A                   
236E: 28 0B           JR      Z,$237B             ; {}
2370: 3A 14 90        LD      A,($9014)           
2373: 4F              LD      C,A                 
2374: 3A 13 92        LD      A,($9213)           
2377: EE 01           XOR     $01                 
2379: A1              AND     C                   
237A: C8              RET     Z                   
237B: AF              XOR     A                   
237C: 32 14 90        LD      ($9014),A           
237F: 32 A5 9A        LD      ($9AA5),A           
2382: 32 25 90        LD      ($9025),A           
2385: 32 13 92        LD      ($9213),A           
2388: 3C              INC     A                   
2389: 32 1C 90        LD      ($901C),A           
238C: 32 A6 9A        LD      ($9AA6),A           
238F: 32 BA 99        LD      ($99BA),A           
2392: 3E 0A           LD      A,$0A               
2394: 32 2A 98        LD      ($982A),A           
2397: C9              RET                         
2398: 4F              LD      C,A                 
2399: 3A 8A 92        LD      A,($928A)           
239C: ED 44           NEG                         
239E: C6 10           ADD     $10                 
23A0: 16 20           LD      D,$20               
23A2: 07              RLCA                        
23A3: CB 12           RL      D                   
23A5: 07              RLCA                        
23A6: CB 12           RL      D                   
23A8: E6 E0           AND     $E0                 
23AA: C6 14           ADD     $14                 
23AC: 81              ADD     A,C                 
23AD: 5F              LD      E,A                 
23AE: C9              RET                         
23AF: 24              INC     H                   
23B0: 4E              LD      C,(HL)              
23B1: 4F              LD      C,A                 
23B2: 50              LD      D,B                 
23B3: 51              LD      D,C                 
23B4: 24              INC     H                   
23B5: 24              INC     H                   
23B6: 52              LD      D,D                 
23B7: 53              LD      D,E                 
23B8: 54              LD      D,H                 
23B9: 55              LD      D,L                 
23BA: 24              INC     H                   
23BB: 24              INC     H                   
23BC: 56              LD      D,(HL)              
23BD: 57              LD      D,A                 
23BE: 58              LD      E,B                 
23BF: 59              LD      E,C                 
23C0: 24              INC     H                   
23C1: 24              INC     H                   
23C2: 5A              LD      E,D                 
23C3: 5B              LD      E,E                 
23C4: 5C              LD      E,H                 
23C5: 5D              LD      E,L                 
23C6: 24              INC     H                   
23C7: 24              INC     H                   
23C8: 5E              LD      E,(HL)              
23C9: 5F              LD      E,A                 
23CA: 60              LD      H,B                 
23CB: 61              LD      H,C                 
23CC: 24              INC     H                   
23CD: 62              LD      H,D                 
23CE: 63              LD      H,E                 
23CF: 64              LD      H,H                 
23D0: 65              LD      H,L                 
23D1: 66              LD      H,(HL)              
23D2: 67              LD      H,A                 
23D3: 68              LD      L,B                 
23D4: 69              LD      L,C                 
23D5: 6A              LD      L,D                 
23D6: 6B              LD      L,E                 
23D7: 6C              LD      L,H                 
23D8: 6D              LD      L,L                 
23D9: 6E              LD      L,(HL)              
23DA: 6F              LD      L,A                 
23DB: 70              LD      (HL),B              
23DC: 71              LD      (HL),C              
23DD: 72              LD      (HL),D              
23DE: 73              LD      (HL),E              
23DF: 74              LD      (HL),H              
23E0: 75              LD      (HL),L              
23E1: 76              HALT                        
23E2: 77              LD      (HL),A              
23E3: 78              LD      A,B                 
23E4: 79              LD      A,C                 
23E5: 7A              LD      A,D                 
23E6: 7B              LD      A,E                 
23E7: 7C              LD      A,H                 
23E8: 7D              LD      A,L                 
23E9: 7E              LD      A,(HL)              
23EA: 7F              LD      A,A                 
23EB: 3A A0 92        LD      A,($92A0)           
23EE: CB 47           BIT     0,A                 
23F0: CA A4 25        JP      Z,$25A4             ; {}
23F3: E6 02           AND     $02                 
23F5: 5F              LD      E,A                 
23F6: 3A A6 92        LD      A,($92A6)           
23F9: DD 6F           LD      IXL,A               
23FB: 06 20           LD      B,$20               
23FD: 16 88           LD      D,$88               
23FF: 1A              LD      A,(DE)              
2400: CB 27           SLA     A                   
2402: 38 20           JR      C,$2424             ; {}
2404: 21 0D 24        LD      HL,$240D            
2407: D7              RST     0X10                
2408: 7E              LD      A,(HL)              
2409: 23              INC     HL                  
240A: 66              LD      H,(HL)              
240B: 6F              LD      L,A                 
240C: E9              JP      (HL)                
240D: 24              INC     H                   
240E: 24              INC     H                   
240F: 96              SUB     (HL)                
2410: 24              INC     H                   
2411: 6D              LD      L,L                 
2412: 24              INC     H                   
2413: 5B              LD      E,E                 
2414: 25              DEC     H                   
2415: C0              RET     NZ                  
2416: 24              INC     H                   
2417: 43              LD      B,E                 
2418: 25              DEC     H                   
2419: 5B              LD      E,E                 
241A: 25              DEC     H                   
241B: 9E              SBC     (HL)                
241C: 25              DEC     H                   
241D: 4A              LD      C,D                 
241E: 24              INC     H                   
241F: 30 24           JR      NC,$2445            ; {}
2421: 1D              DEC     E                   
2422: DD 2C           INC     IXL                 
2424: 3E 04           LD      A,$04               
2426: 83              ADD     A,E                 
2427: 5F              LD      E,A                 
2428: 10 D3           DJNZ    $23FD               ; {}
242A: DD 7D           LD      A,IXL               
242C: 32 A6 92        LD      ($92A6),A           
242F: C9              RET                         
2430: 6B              LD      L,E                 
2431: 26 01           LD      H,$01               
2433: 4E              LD      C,(HL)              
2434: 2C              INC     L                   
2435: 6E              LD      L,(HL)              
2436: 26 99           LD      H,$99               
2438: 7E              LD      A,(HL)              
2439: 08              EX      AF,AF'              
243A: 69              LD      L,C                 
243B: 4E              LD      C,(HL)              
243C: 1C              INC     E                   
243D: 1A              LD      A,(DE)              
243E: C6 11           ADD     $11                 
2440: 6F              LD      L,A                 
2441: 26 91           LD      H,$91               
2443: 08              EX      AF,AF'              
2444: 77              LD      (HL),A              
2445: 2C              INC     L                   
2446: 71              LD      (HL),C              
2447: C3 21 24        JP      $2421               ; {}
244A: 26 8B           LD      H,$8B               
244C: 6B              LD      L,E                 
244D: 1C              INC     E                   
244E: 1A              LD      A,(DE)              
244F: 3D              DEC     A                   
2450: 28 0D           JR      Z,$245F             ; {}
2452: 12              LD      (DE),A              
2453: 1D              DEC     E                   
2454: E6 03           AND     $03                 
2456: 20 CC           JR      NZ,$2424            ; {}
2458: 7E              LD      A,(HL)              
2459: C6 04           ADD     $04                 
245B: 77              LD      (HL),A              
245C: C3 24 24        JP      $2424               ; {}
245F: 26 93           LD      H,$93               
2461: AF              XOR     A                   
2462: 77              LD      (HL),A              
2463: 26 9B           LD      H,$9B               
2465: 77              LD      (HL),A              
2466: 1D              DEC     E                   
2467: 3E 80           LD      A,$80               
2469: 12              LD      (DE),A              
246A: C3 24 24        JP      $2424               ; {}
246D: 26 9B           LD      H,$9B               
246F: 6B              LD      L,E                 
2470: 7E              LD      A,(HL)              
2471: E6 01           AND     $01                 
2473: 26 8B           LD      H,$8B               
2475: 20 0A           JR      NZ,$2481            ; {}
2477: 7E              LD      A,(HL)              
2478: E6 07           AND     $07                 
247A: FE 06           CP      $06                 
247C: 28 13           JR      Z,$2491             ; {}
247E: 34              INC     (HL)                
247F: 18 28           JR      $24A9               ; {}
2481: 7E              LD      A,(HL)              
2482: E6 07           AND     $07                 
2484: 20 08           JR      NZ,$248E            ; {}
2486: 26 9B           LD      H,$9B               
2488: CB 86           RES     0,(HL)              
248A: 26 8B           LD      H,$8B               
248C: 18 1B           JR      $24A9               ; {}
248E: 35              DEC     (HL)                
248F: 18 18           JR      $24A9               ; {}
2491: 3E 01           LD      A,$01               
2493: 12              LD      (DE),A              
2494: 18 13           JR      $24A9               ; {}
2496: 26 8B           LD      H,$8B               
2498: 6B              LD      L,E                 
2499: 3A A2 92        LD      A,($92A2)           
249C: CB 0E           RRC     (HL)                
249E: 0F              RRCA                        
249F: 0F              RRCA                        
24A0: CB 16           RL      (HL)                
24A2: 3A 0B 92        LD      A,($920B)           
24A5: A7              AND     A                   
24A6: CA 22 24        JP      Z,$2422             ; {}
24A9: 26 01           LD      H,$01               
24AB: 4E              LD      C,(HL)              
24AC: 2C              INC     L                   
24AD: 6E              LD      L,(HL)              
24AE: 26 98           LD      H,$98               
24B0: 7E              LD      A,(HL)              
24B1: 16 93           LD      D,$93               
24B3: 12              LD      (DE),A              
24B4: 1C              INC     E                   
24B5: 69              LD      L,C                 
24B6: 7E              LD      A,(HL)              
24B7: 12              LD      (DE),A              
24B8: 16 9B           LD      D,$9B               
24BA: 2C              INC     L                   
24BB: 7E              LD      A,(HL)              
24BC: 12              LD      (DE),A              
24BD: C3 21 24        JP      $2421               ; {}
24C0: 6B              LD      L,E                 
24C1: 1C              INC     E                   
24C2: 1A              LD      A,(DE)              
24C3: FE 45           CP      $45                 
24C5: 28 2D           JR      Z,$24F4             ; {}
24C7: 3C              INC     A                   
24C8: 12              LD      (DE),A              
24C9: 1D              DEC     E                   
24CA: FE 45           CP      $45                 
24CC: 20 02           JR      NZ,$24D0            ; {}
24CE: C6 03           ADD     $03                 
24D0: FE 44           CP      $44                 
24D2: 20 1A           JR      NZ,$24EE            ; {}
24D4: 26 93           LD      H,$93               
24D6: 08              EX      AF,AF'              
24D7: 7E              LD      A,(HL)              
24D8: D6 08           SUB     $08                 
24DA: 77              LD      (HL),A              
24DB: 2C              INC     L                   
24DC: 7E              LD      A,(HL)              
24DD: D6 08           SUB     $08                 
24DF: 77              LD      (HL),A              
24E0: 30 06           JR      NC,$24E8            ; {}
24E2: 26 9B           LD      H,$9B               
24E4: 7E              LD      A,(HL)              
24E5: EE 01           XOR     $01                 
24E7: 77              LD      (HL),A              
24E8: 2D              DEC     L                   
24E9: 26 9B           LD      H,$9B               
24EB: 36 0C           LD      (HL),$0C            
24ED: 08              EX      AF,AF'              
24EE: 26 8B           LD      H,$8B               
24F0: 77              LD      (HL),A              
24F1: C3 24 24        JP      $2424               ; {}
24F4: 1D              DEC     E                   
24F5: 26 92           LD      H,$92               
24F7: 7E              LD      A,(HL)              
24F8: FE 01           CP      $01                 
24FA: 20 0F           JR      NZ,$250B            ; {}
24FC: 26 93           LD      H,$93               
24FE: 36 00           LD      (HL),$00            
2500: 26 9B           LD      H,$9B               
2502: 36 00           LD      (HL),$00            
2504: 26 88           LD      H,$88               
2506: 36 80           LD      (HL),$80            
2508: C3 24 24        JP      $2424               ; {}
250B: 26 8B           LD      H,$8B               
250D: 77              LD      (HL),A              
250E: FE 37           CP      $37                 
2510: 38 0A           JR      C,$251C             ; {}
2512: 0E 0D           LD      C,$0D               
2514: 2C              INC     L                   
2515: FE 3A           CP      $3A                 
2517: 38 01           JR      C,$251A             ; {}
2519: 0C              INC     C                   
251A: 71              LD      (HL),C              
251B: 2D              DEC     L                   
251C: 26 93           LD      H,$93               
251E: 0E 08           LD      C,$08               
2520: FE 3B           CP      $3B                 
2522: 30 06           JR      NC,$252A            ; {}
2524: 0E 00           LD      C,$00               
2526: 7E              LD      A,(HL)              
2527: C6 08           ADD     $08                 
2529: 77              LD      (HL),A              
252A: 2C              INC     L                   
252B: 7E              LD      A,(HL)              
252C: C6 08           ADD     $08                 
252E: 77              LD      (HL),A              
252F: 26 9B           LD      H,$9B               
2531: 30 04           JR      NC,$2537            ; {}
2533: 7E              LD      A,(HL)              
2534: EE 01           XOR     $01                 
2536: 77              LD      (HL),A              
2537: 2D              DEC     L                   
2538: 71              LD      (HL),C              
2539: 26 88           LD      H,$88               
253B: 36 05           LD      (HL),$05            
253D: 2C              INC     L                   
253E: 36 13           LD      (HL),$13            
2540: C3 24 24        JP      $2424               ; {}
2543: 6B              LD      L,E                 
2544: 2C              INC     L                   
2545: 62              LD      H,D                 
2546: 35              DEC     (HL)                
2547: C2 24 24        JP      NZ,$2424            ; {}
254A: 2D              DEC     L                   
254B: 36 80           LD      (HL),$80            
254D: 26 93           LD      H,$93               
254F: 36 00           LD      (HL),$00            
2551: 26 9B           LD      H,$9B               
2553: 36 00           LD      (HL),$00            
2555: 3E 80           LD      A,$80               
2557: 12              LD      (DE),A              
2558: C3 24 24        JP      $2424               ; {}
255B: 26 93           LD      H,$93               
255D: 6B              LD      L,E                 
255E: CB FD           SET     7,L                 
2560: 7E              LD      A,(HL)              
2561: FE F4           CP      $F4                 
2563: 30 1A           JR      NC,$257F            ; {}
2565: 2C              INC     L                   
2566: 4E              LD      C,(HL)              
2567: 26 9B           LD      H,$9B               
2569: 7E              LD      A,(HL)              
256A: 2D              DEC     L                   
256B: 0F              RRCA                        
256C: 79              LD      A,C                 
256D: 1F              RRA                         
256E: FE 0B           CP      $0B                 
2570: 38 0D           JR      C,$257F             ; {}
2572: FE A5           CP      $A5                 
2574: 30 09           JR      NC,$257F            ; {}
2576: 1A              LD      A,(DE)              
2577: FE 06           CP      $06                 
2579: C2 22 24        JP      NZ,$2422            ; {}
257C: C3 24 24        JP      $2424               ; {}
257F: CB BD           RES     7,L                 
2581: 1A              LD      A,(DE)              
2582: FE 03           CP      $03                 
2584: 28 0A           JR      Z,$2590             ; {}
2586: 3E 80           LD      A,$80               
2588: 12              LD      (DE),A              
2589: 26 93           LD      H,$93               
258B: 36 00           LD      (HL),$00            
258D: C3 24 24        JP      $2424               ; {}
2590: 1C              INC     E                   
2591: 1A              LD      A,(DE)              
2592: 1D              DEC     E                   
2593: C6 13           ADD     $13                 
2595: 6F              LD      L,A                 
2596: 26 91           LD      H,$91               
2598: 36 00           LD      (HL),$00            
259A: 6B              LD      L,E                 
259B: C3 86 25        JP      $2586               ; {}
259E: 3E 03           LD      A,$03               
25A0: 12              LD      (DE),A              
25A1: C3 22 24        JP      $2422               ; {}
25A4: CB 4F           BIT     1,A                 
25A6: C8              RET     Z                   
25A7: 21 A6 92        LD      HL,$92A6            
25AA: 7E              LD      A,(HL)              
25AB: 36 00           LD      (HL),$00            
25AD: 2C              INC     L                   
25AE: 77              LD      (HL),A              
25AF: C9              RET                         
25B0: 21 7C 28        LD      HL,$287C            
25B3: 22 E0 92        LD      ($92E0),HL          
25B6: 3A 21 98        LD      A,($9821)           
25B9: 4F              LD      C,A                 
25BA: FE 17           CP      $17                 
25BC: 38 04           JR      C,$25C2             ; {}
25BE: D6 04           SUB     $04                 
25C0: 18 F8           JR      $25BA               ; {}
25C2: 47              LD      B,A                 
25C3: 3C              INC     A                   
25C4: E6 03           AND     $03                 
25C6: 28 19           JR      Z,$25E1             ; {}
25C8: 3A 84 99        LD      A,($9984)           
25CB: 2E 11           LD      L,$11               
25CD: CD 4E 10        CALL    $104E               ; {}
25D0: 7D              LD      A,L                 
25D1: 21 B6 26        LD      HL,$26B6            
25D4: D7              RST     0X10                
25D5: 11 02 27        LD      DE,$2702            
25D8: 78              LD      A,B                 
25D9: CB 38           SRL     B                   
25DB: CB 38           SRL     B                   
25DD: 90              SUB     B                   
25DE: 3D              DEC     A                   
25DF: 18 0D           JR      $25EE               ; {}
25E1: 21 FA 26        LD      HL,$26FA            
25E4: 79              LD      A,C                 
25E5: CB 3F           SRL     A                   
25E7: CB 3F           SRL     A                   
25E9: E6 07           AND     $07                 
25EB: 11 EC 27        LD      DE,$27EC            
25EE: D7              RST     0X10                
25EF: 7E              LD      A,(HL)              
25F0: EB              EX      DE,HL               
25F1: D7              RST     0X10                
25F2: 7E              LD      A,(HL)              
25F3: 23              INC     HL                  
25F4: 32 E2 92        LD      ($92E2),A           
25F7: 7E              LD      A,(HL)              
25F8: 23              INC     HL                  
25F9: 32 E3 92        LD      ($92E3),A           
25FC: 11 20 89        LD      DE,$8920            
25FF: 3E 7E           LD      A,$7E               
2601: 12              LD      (DE),A              
2602: 1C              INC     E                   
2603: 7E              LD      A,(HL)              
2604: 23              INC     HL                  
2605: FE FF           CP      $FF                 
2607: CA 8F 26        JP      Z,$268F             ; {}
260A: 4F              LD      C,A                 
260B: D5              PUSH    DE                  
260C: E5              PUSH    HL                  
260D: 21 00 91        LD      HL,$9100            
2610: 3E FF           LD      A,$FF               
2612: 06 10           LD      B,$10               
2614: DF              RST     0X18                
2615: 79              LD      A,C                 
2616: E6 0F           AND     $0F                 
2618: 28 2A           JR      Z,$2644             ; {}
261A: 47              LD      B,A                 
261B: CB 3F           SRL     A                   
261D: C6 04           ADD     $04                 
261F: 5F              LD      E,A                 
2620: CD 00 10        CALL    $1000               ; {}
2623: 6F              LD      L,A                 
2624: 26 00           LD      H,$00               
2626: 7B              LD      A,E                 
2627: CD 61 10        CALL    $1061               ; {}
262A: CB 40           BIT     0,B                 
262C: 28 02           JR      Z,$2630             ; {}
262E: CB DF           SET     3,A                 
2630: 26 91           LD      H,$91               
2632: 6F              LD      L,A                 
2633: 7E              LD      A,(HL)              
2634: 3C              INC     A                   
2635: 20 E9           JR      NZ,$2620            ; {}
2637: 78              LD      A,B                 
2638: 07              RLCA                        
2639: CB 01           RLC     C                   
263B: 30 02           JR      NC,$263F            ; {}
263D: F6 40           OR      $40                 
263F: F6 38           OR      $38                 
2641: 77              LD      (HL),A              
2642: 10 DC           DJNZ    $2620               ; {}
2644: 21 00 91        LD      HL,$9100            
2647: ED 5B E0 92     LD      DE,($92E0)          
264B: 06 08           LD      B,$08               
264D: 7E              LD      A,(HL)              
264E: FE FF           CP      $FF                 
2650: 28 03           JR      Z,$2655             ; {}
2652: 23              INC     HL                  
2653: 18 F8           JR      $264D               ; {}
2655: 1A              LD      A,(DE)              
2656: 77              LD      (HL),A              
2657: 13              INC     DE                  
2658: 23              INC     HL                  
2659: 78              LD      A,B                 
265A: FE 05           CP      $05                 
265C: 20 02           JR      NZ,$2660            ; {}
265E: 2E 08           LD      L,$08               
2660: 10 EB           DJNZ    $264D               ; {}
2662: ED 53 E0 92     LD      ($92E0),DE          
2666: E1              POP     HL                  
2667: D1              POP     DE                  
2668: 46              LD      B,(HL)              
2669: 23              INC     HL                  
266A: 4E              LD      C,(HL)              
266B: 23              INC     HL                  
266C: E5              PUSH    HL                  
266D: 21 00 91        LD      HL,$9100            
2670: 78              LD      A,B                 
2671: 12              LD      (DE),A              
2672: 7E              LD      A,(HL)              
2673: FE FF           CP      $FF                 
2675: 28 10           JR      Z,$2687             ; {}
2677: 1C              INC     E                   
2678: 12              LD      (DE),A              
2679: 1C              INC     E                   
267A: 79              LD      A,C                 
267B: 12              LD      (DE),A              
267C: 1C              INC     E                   
267D: CB DD           SET     3,L                 
267F: 7E              LD      A,(HL)              
2680: 12              LD      (DE),A              
2681: 1C              INC     E                   
2682: CB 9D           RES     3,L                 
2684: 23              INC     HL                  
2685: 18 E9           JR      $2670               ; {}
2687: 3E 7E           LD      A,$7E               
2689: 12              LD      (DE),A              
268A: 1C              INC     E                   
268B: E1              POP     HL                  
268C: C3 03 26        JP      $2603               ; {}
268F: 1D              DEC     E                   
2690: 3A 2B 98        LD      A,($982B)           
2693: 47              LD      B,A                 
2694: 3A 27 98        LD      A,($9827)           
2697: 3D              DEC     A                   
2698: A0              AND     B                   
2699: 28 17           JR      Z,$26B2             ; {}
269B: 3A 25 98        LD      A,($9825)           
269E: A7              AND     A                   
269F: 28 11           JR      Z,$26B2             ; {}
26A1: 62              LD      H,D                 
26A2: 7B              LD      A,E                 
26A3: D6 04           SUB     $04                 
26A5: 6F              LD      L,A                 
26A6: 7E              LD      A,(HL)              
26A7: 12              LD      (DE),A              
26A8: 1C              INC     E                   
26A9: 3E 04           LD      A,$04               
26AB: 12              LD      (DE),A              
26AC: 1C              INC     E                   
26AD: 3E 87           LD      A,$87               
26AF: 32 04 8B        LD      ($8B04),A           
26B2: 3E 7F           LD      A,$7F               
26B4: 12              LD      (DE),A              
26B5: C9              RET                         
26B6: 00              NOP                         
26B7: 12              LD      (DE),A              
26B8: 24              INC     H                   
26B9: 36 00           LD      (HL),$00            
26BB: 48              LD      C,B                 
26BC: 6C              LD      L,H                 
26BD: 5A              LD      E,D                 
26BE: 48              LD      C,B                 
26BF: 6C              LD      L,H                 
26C0: 00              NOP                         
26C1: 7E              LD      A,(HL)              
26C2: A2              AND     D                   
26C3: 90              SUB     B                   
26C4: B4              OR      H                   
26C5: D8              RET     C                   
26C6: C6 00           ADD     $00                 
26C8: 12              LD      (DE),A              
26C9: 48              LD      C,B                 
26CA: 6C              LD      L,H                 
26CB: 5A              LD      E,D                 
26CC: 7E              LD      A,(HL)              
26CD: A2              AND     D                   
26CE: 00              NOP                         
26CF: 7E              LD      A,(HL)              
26D0: D8              RET     C                   
26D1: C6 B4           ADD     $B4                 
26D3: D8              RET     C                   
26D4: C6 B4           ADD     $B4                 
26D6: D8              RET     C                   
26D7: C6 00           ADD     $00                 
26D9: 12              LD      (DE),A              
26DA: 7E              LD      A,(HL)              
26DB: A2              AND     D                   
26DC: 90              SUB     B                   
26DD: 7E              LD      A,(HL)              
26DE: D8              RET     C                   
26DF: C6 B4           ADD     $B4                 
26E1: D8              RET     C                   
26E2: C6 B4           ADD     $B4                 
26E4: D8              RET     C                   
26E5: C6 B4           ADD     $B4                 
26E7: D8              RET     C                   
26E8: C6 00           ADD     $00                 
26EA: 12              LD      (DE),A              
26EB: 48              LD      C,B                 
26EC: 36 24           LD      (HL),$24            
26EE: 48              LD      C,B                 
26EF: 6C              LD      L,H                 
26F0: 00              NOP                         
26F1: 7E              LD      A,(HL)              
26F2: A2              AND     D                   
26F3: 90              SUB     B                   
26F4: B4              OR      H                   
26F5: D8              RET     C                   
26F6: 00              NOP                         
26F7: B4              OR      H                   
26F8: D8              RET     C                   
26F9: C6 00           ADD     $00                 
26FB: 12              LD      (DE),A              
26FC: 24              INC     H                   
26FD: 36 48           LD      (HL),$48            
26FF: 5A              LD      E,D                 
2700: 6C              LD      L,H                 
2701: 7E              LD      A,(HL)              
2702: 14              INC     D                   
2703: 00              NOP                         
2704: 00              NOP                         
2705: 00              NOP                         
2706: C0              RET     NZ                  
2707: 00              NOP                         
2708: 01 01 00        LD      BC,$0001            
270B: 41              LD      B,C                 
270C: 41              LD      B,C                 
270D: 00              NOP                         
270E: 40              LD      B,B                 
270F: 40              LD      B,B                 
2710: 00              NOP                         
2711: 00              NOP                         
2712: 00              NOP                         
2713: FF              RST     0X38                
2714: 14              INC     D                   
2715: 01 00 42        LD      BC,$4200            
2718: 82              ADD     A,D                 
2719: 00              NOP                         
271A: 03              INC     BC                  
271B: 85              ADD     A,L                 
271C: 00              NOP                         
271D: 43              LD      B,E                 
271E: C5              PUSH    BC                  
271F: 00              NOP                         
2720: 42              LD      B,D                 
2721: C4 00 02        CALL    NZ,$0200            ; {}
2724: 84              ADD     A,H                 
2725: FF              RST     0X38                
2726: 14              INC     D                   
2727: 01 82 00        LD      BC,$0082            
272A: C0              RET     NZ                  
272B: 00              NOP                         
272C: 01 01 00        LD      BC,$0001            
272F: 41              LD      B,C                 
2730: 41              LD      B,C                 
2731: 02              LD      (BC),A              
2732: 40              LD      B,B                 
2733: 40              LD      B,B                 
2734: 02              LD      (BC),A              
2735: 00              NOP                         
2736: 00              NOP                         
2737: FF              RST     0X38                
2738: 14              INC     D                   
2739: 01 82 02        LD      BC,$0282            
273C: C2 00 03        JP      NZ,$0300            ; {}
273F: 85              ADD     A,L                 
2740: 00              NOP                         
2741: 43              LD      B,E                 
2742: C5              PUSH    BC                  
2743: 02              LD      (BC),A              
2744: 42              LD      B,D                 
2745: C4 02 02        CALL    NZ,$0202            ; {}
2748: 84              ADD     A,H                 
2749: FF              RST     0X38                
274A: 14              INC     D                   
274B: 01 82 00        LD      BC,$0082            
274E: C0              RET     NZ                  
274F: 00              NOP                         
2750: 01 C1 00        LD      BC,$00C1            
2753: 41              LD      B,C                 
2754: 81              ADD     A,C                 
2755: 02              LD      (BC),A              
2756: 40              LD      B,B                 
2757: 80              ADD     A,B                 
2758: 02              LD      (BC),A              
2759: 40              LD      B,B                 
275A: 80              ADD     A,B                 
275B: FF              RST     0X38                
275C: 14              INC     D                   
275D: 01 82 00        LD      BC,$0082            
2760: C0              RET     NZ                  
2761: 42              LD      B,D                 
2762: 01 01 F2        LD      BC,$F201            
2765: 41              LD      B,C                 
2766: 41              LD      B,C                 
2767: 02              LD      (BC),A              
2768: 40              LD      B,B                 
2769: 40              LD      B,B                 
276A: 02              LD      (BC),A              
276B: 00              NOP                         
276C: 00              NOP                         
276D: FF              RST     0X38                
276E: 14              INC     D                   
276F: 01 A4 02        LD      BC,$02A4            
2772: C2 52 03        JP      NZ,$0352            ; {}
2775: 85              ADD     A,L                 
2776: F2 43 C5        JP      P,$C543             
2779: 02              LD      (BC),A              
277A: 42              LD      B,D                 
277B: C4 02 02        CALL    NZ,$0202            ; {}
277E: 84              ADD     A,H                 
277F: FF              RST     0X38                
2780: 14              INC     D                   
2781: 01 82 00        LD      BC,$0082            
2784: C0              RET     NZ                  
2785: 52              LD      D,D                 
2786: 01 C1 F2        LD      BC,$F2C1            
2789: 41              LD      B,C                 
278A: 81              ADD     A,C                 
278B: 02              LD      (BC),A              
278C: 40              LD      B,B                 
278D: 80              ADD     A,B                 
278E: 02              LD      (BC),A              
278F: 40              LD      B,B                 
2790: 80              ADD     A,B                 
2791: FF              RST     0X38                
2792: 14              INC     D                   
2793: 01 A4 00        LD      BC,$00A4            
2796: C0              RET     NZ                  
2797: 42              LD      B,D                 
2798: 01 01 F4        LD      BC,$F401            
279B: 41              LD      B,C                 
279C: 41              LD      B,C                 
279D: 04              INC     B                   
279E: 40              LD      B,B                 
279F: 40              LD      B,B                 
27A0: 04              INC     B                   
27A1: 00              NOP                         
27A2: 00              NOP                         
27A3: FF              RST     0X38                
27A4: 14              INC     D                   
27A5: 01 A4 02        LD      BC,$02A4            
27A8: C2 52 03        JP      NZ,$0352            ; {}
27AB: 85              ADD     A,L                 
27AC: F4 43 C5        CALL    P,$C543             
27AF: 04              INC     B                   
27B0: 42              LD      B,D                 
27B1: C4 04 02        CALL    NZ,$0204            ; {}
27B4: 84              ADD     A,H                 
27B5: FF              RST     0X38                
27B6: 14              INC     D                   
27B7: 03              INC     BC                  
27B8: A4              AND     H                   
27B9: 00              NOP                         
27BA: C0              RET     NZ                  
27BB: 54              LD      D,H                 
27BC: 01 C1 F4        LD      BC,$F4C1            
27BF: 41              LD      B,C                 
27C0: 81              ADD     A,C                 
27C1: 04              INC     B                   
27C2: 40              LD      B,B                 
27C3: 80              ADD     A,B                 
27C4: 04              INC     B                   
27C5: 40              LD      B,B                 
27C6: 80              ADD     A,B                 
27C7: FF              RST     0X38                
27C8: 14              INC     D                   
27C9: 03              INC     BC                  
27CA: A4              AND     H                   
27CB: 00              NOP                         
27CC: C0              RET     NZ                  
27CD: 54              LD      D,H                 
27CE: 01 01 F4        LD      BC,$F401            
27D1: 41              LD      B,C                 
27D2: 41              LD      B,C                 
27D3: 04              INC     B                   
27D4: 40              LD      B,B                 
27D5: 40              LD      B,B                 
27D6: 04              INC     B                   
27D7: 00              NOP                         
27D8: 00              NOP                         
27D9: FF              RST     0X38                
27DA: 14              INC     D                   
27DB: 03              INC     BC                  
27DC: A4              AND     H                   
27DD: 02              LD      (BC),A              
27DE: C2 54 03        JP      NZ,$0354            ; {}
27E1: 85              ADD     A,L                 
27E2: F4 43 C5        CALL    P,$C543             
27E5: 04              INC     B                   
27E6: 42              LD      B,D                 
27E7: C4 04 02        CALL    NZ,$0204            ; {}
27EA: 84              ADD     A,H                 
27EB: FF              RST     0X38                
27EC: FF              RST     0X38                
27ED: 00              NOP                         
27EE: 00              NOP                         
27EF: 06 C6           LD      B,$C6               
27F1: 00              NOP                         
27F2: 07              RLCA                        
27F3: 07              RLCA                        
27F4: 00              NOP                         
27F5: 47              LD      B,A                 
27F6: 47              LD      B,A                 
27F7: 00              NOP                         
27F8: 46              LD      B,(HL)              
27F9: 46              LD      B,(HL)              
27FA: 00              NOP                         
27FB: 06 06           LD      B,$06               
27FD: FF              RST     0X38                
27FE: FF              RST     0X38                
27FF: 00              NOP                         
2800: 00              NOP                         
2801: 08              EX      AF,AF'              
2802: C8              RET     Z                   
2803: 00              NOP                         
2804: 09              ADD     HL,BC               
2805: C9              RET                         
2806: 00              NOP                         
2807: 09              ADD     HL,BC               
2808: C9              RET                         
2809: 00              NOP                         
280A: 48              LD      C,B                 
280B: 48              LD      C,B                 
280C: 00              NOP                         
280D: 08              EX      AF,AF'              
280E: 08              EX      AF,AF'              
280F: FF              RST     0X38                
2810: FF              RST     0X38                
2811: 00              NOP                         
2812: 00              NOP                         
2813: 0A              LD      A,(BC)              
2814: 4A              LD      C,D                 
2815: 00              NOP                         
2816: 0B              DEC     BC                  
2817: CB 00           RLC     B                   
2819: 0B              DEC     BC                  
281A: CB 00           RLC     B                   
281C: 0A              LD      A,(BC)              
281D: 4A              LD      C,D                 
281E: 00              NOP                         
281F: 16 56           LD      D,$56               
2821: FF              RST     0X38                
2822: FF              RST     0X38                
2823: 00              NOP                         
2824: 00              NOP                         
2825: 0C              INC     C                   
2826: CC 00 0D        CALL    Z,$0D00             ; {}
2829: 0D              DEC     C                   
282A: 00              NOP                         
282B: 4D              LD      C,L                 
282C: 4D              LD      C,L                 
282D: 00              NOP                         
282E: 0C              INC     C                   
282F: CC 00 17        CALL    Z,$1700             ; {}
2832: D7              RST     0X10                
2833: FF              RST     0X38                
2834: FF              RST     0X38                
2835: 00              NOP                         
2836: 00              NOP                         
2837: 0E 0E           LD      C,$0E               
2839: 00              NOP                         
283A: 0F              RRCA                        
283B: 0F              RRCA                        
283C: 00              NOP                         
283D: 4F              LD      C,A                 
283E: 4F              LD      C,A                 
283F: 00              NOP                         
2840: 0E 0E           LD      C,$0E               
2842: 00              NOP                         
2843: 4E              LD      C,(HL)              
2844: 4E              LD      C,(HL)              
2845: FF              RST     0X38                
2846: FF              RST     0X38                
2847: 00              NOP                         
2848: 00              NOP                         
2849: 10 10           DJNZ    $285B               ; {}
284B: 00              NOP                         
284C: 11 D1 00        LD      DE,$00D1            
284F: 11 D1 00        LD      DE,$00D1            
2852: 50              LD      D,B                 
2853: 50              LD      D,B                 
2854: 00              NOP                         
2855: 10 10           DJNZ    $2867               ; {}
2857: FF              RST     0X38                
2858: FF              RST     0X38                
2859: 00              NOP                         
285A: 00              NOP                         
285B: 12              LD      (DE),A              
285C: 12              LD      (DE),A              
285D: 00              NOP                         
285E: 13              INC     DE                  
285F: 13              INC     DE                  
2860: 00              NOP                         
2861: 53              LD      D,E                 
2862: 53              LD      D,E                 
2863: 00              NOP                         
2864: 52              LD      D,D                 
2865: 52              LD      D,D                 
2866: 00              NOP                         
2867: 12              LD      (DE),A              
2868: 12              LD      (DE),A              
2869: FF              RST     0X38                
286A: FF              RST     0X38                
286B: 00              NOP                         
286C: 00              NOP                         
286D: 14              INC     D                   
286E: D4 00 15        CALL    NC,$1500            ; {}
2871: 15              DEC     D                   
2872: 00              NOP                         
2873: 55              LD      D,L                 
2874: 55              LD      D,L                 
2875: 00              NOP                         
2876: 14              INC     D                   
2877: D4 00 14        CALL    NC,$1400            ; {}
287A: D4 FF 58        CALL    NC,$58FF            
287D: 5A              LD      E,D                 
287E: 5C              LD      E,H                 
287F: 5E              LD      E,(HL)              
2880: 28 2A           JR      Z,$28AC             ; {}
2882: 2C              INC     L                   
2883: 2E 30           LD      L,$30               
2885: 34              INC     (HL)                
2886: 36 32           LD      (HL),$32            
2888: 50              LD      D,B                 
2889: 52              LD      D,D                 
288A: 54              LD      D,H                 
288B: 56              LD      D,(HL)              
288C: 42              LD      B,D                 
288D: 46              LD      B,(HL)              
288E: 40              LD      B,B                 
288F: 44              LD      B,H                 
2890: 4A              LD      C,D                 
2891: 4E              LD      C,(HL)              
2892: 48              LD      C,B                 
2893: 4C              LD      C,H                 
2894: 1A              LD      A,(DE)              
2895: 1E 20           LD      E,$20               
2897: 24              INC     H                   
2898: 22 26 18        LD      ($1826),HL          ; {}
289B: 1C              INC     E                   
289C: 08              EX      AF,AF'              
289D: 0C              INC     C                   
289E: 12              LD      (DE),A              
289F: 16 10           LD      D,$10               
28A1: 14              INC     D                   
28A2: 0A              LD      A,(BC)              
28A3: 0E 21           LD      C,$21               
28A5: 20 89           JR      NZ,$2830            ; {}
28A7: 22 22 98        LD      ($9822),HL          
28AA: FD 21 16 29     LD      IY,$2916            
28AE: 3A 25 98        LD      A,($9825)           
28B1: A7              AND     A                   
28B2: 20 27           JR      NZ,$28DB            ; {}
28B4: 3A 21 98        LD      A,($9821)           
28B7: 0F              RRCA                        
28B8: 0F              RRCA                        
28B9: 4F              LD      C,A                 
28BA: 0F              RRCA                        
28BB: 47              LD      B,A                 
28BC: E6 1C           AND     $1C                 
28BE: 78              LD      A,B                 
28BF: 28 02           JR      Z,$28C3             ; {}
28C1: 3E 03           LD      A,$03               
28C3: E6 03           AND     $03                 
28C5: 21 0E 29        LD      HL,$290E            
28C8: CF              RST     0X08                
28C9: 11 84 92        LD      DE,$9284            
28CC: 79              LD      A,C                 
28CD: ED A0           LDI                         
28CF: ED A0           LDI                         
28D1: 21 1C 29        LD      HL,$291C            
28D4: E6 07           AND     $07                 
28D6: D7              RST     0X10                
28D7: 56              LD      D,(HL)              
28D8: 5A              LD      E,D                 
28D9: 18 03           JR      $28DE               ; {}
28DB: 11 24 36        LD      DE,$3624            
28DE: 21 08 8B        LD      HL,$8B08            
28E1: DD 2E 01        LD      IXL,$01             
28E4: 06 14           LD      B,$14               
28E6: DD 62           LD      IXH,D               
28E8: CD F7 28        CALL    $28F7               ; {}
28EB: 06 08           LD      B,$08               
28ED: DD 26 10        LD      IXH,$10             
28F0: CD F7 28        CALL    $28F7               ; {}
28F3: 06 10           LD      B,$10               
28F5: DD 63           LD      IXH,E               
28F7: DD 2D           DEC     IXL                 
28F9: 20 08           JR      NZ,$2903            ; {}
28FB: FD 4E 00        LD      C,(IY+$00)          
28FE: FD 23           INC     IY                  
2900: DD 2E 08        LD      IXL,$08             
2903: CB 01           RLC     C                   
2905: DD 7C           LD      A,IXH               
2907: 1F              RRA                         
2908: 77              LD      (HL),A              
2909: 2C              INC     L                   
290A: 2C              INC     L                   
290B: 10 EA           DJNZ    $28F7               ; {}
290D: C9              RET                         
290E: 0A              LD      A,(BC)              
290F: B8              CP      B                   
2910: 0F              RRCA                        
2911: B9              CP      C                   
2912: 14              INC     D                   
2913: BC              CP      H                   
2914: 1E BD           LD      E,$BD               
2916: A5              AND     L                   
2917: 5A              LD      E,D                 
2918: A9              XOR     C                   
2919: 0F              RRCA                        
291A: 0A              LD      A,(BC)              
291B: 50              LD      D,B                 
291C: 36 24           LD      (HL),$24            
291E: D4 BA E4        CALL    NC,$E4BA            
2921: CC A8 F4        CALL    Z,$F4A8             
2924: 2A 22 98        LD      HL,($9822)          
2927: 7E              LD      A,(HL)              
2928: FE 7F           CP      $7F                 
292A: CA 37 2A        JP      Z,$2A37             ; {}
292D: FE 7E           CP      $7E                 
292F: 20 30           JR      NZ,$2961            ; {}
2931: 3A 42 98        LD      A,($9842)           
2934: A7              AND     A                   
2935: C8              RET     Z                   
2936: 3A 87 92        LD      A,($9287)           
2939: A7              AND     A                   
293A: 20 1F           JR      NZ,$295B            ; {}
293C: 3A 25 98        LD      A,($9825)           
293F: 47              LD      B,A                 
2940: A7              AND     A                   
2941: 20 0F           JR      NZ,$2952            ; {}
2943: 3A AC 92        LD      A,($92AC)           
2946: FE 01           CP      $01                 
2948: 20 06           JR      NZ,$2950            ; {}
294A: 3E 08           LD      A,$08               
294C: 32 A8 92        LD      ($92A8),A           
294F: C9              RET                         
2950: A7              AND     A                   
2951: C0              RET     NZ                  
2952: 23              INC     HL                  
2953: 22 22 98        LD      ($9822),HL          
2956: 21 26 98        LD      HL,$9826            
2959: 34              INC     (HL)                
295A: C9              RET                         
295B: 3E 02           LD      A,$02               
295D: 32 AC 92        LD      ($92AC),A           
2960: C9              RET                         
2961: 4F              LD      C,A                 
2962: CB 7F           BIT     7,A                 
2964: 20 06           JR      NZ,$296C            ; {}
2966: 3A A0 92        LD      A,($92A0)           
2969: E6 07           AND     $07                 
296B: C0              RET     NZ                  
296C: CB 21           SLA     C                   
296E: 06 0C           LD      B,$0C               
2970: 11 14 00        LD      DE,$0014            
2973: DD 21 00 91     LD      IX,$9100            
2977: DD CB 13 46     BIT     0,(IX+$13)          
297B: 28 05           JR      Z,$2982             ; {}
297D: DD 19           ADD     IX,DE               
297F: 10 F6           DJNZ    $2977               ; {}
2981: C9              RET                         
2982: 23              INC     HL                  
2983: 7E              LD      A,(HL)              
2984: 47              LD      B,A                 
2985: E6 78           AND     $78                 
2987: FE 78           CP      $78                 
2989: 78              LD      A,B                 
298A: 20 02           JR      NZ,$298E            ; {}
298C: CB B7           RES     6,A                 
298E: DD 77 10        LD      (IX+$10),A          
2991: 23              INC     HL                  
2992: 22 22 98        LD      ($9822),HL          
2995: 26 88           LD      H,$88               
2997: 6F              LD      L,A                 
2998: 36 07           LD      (HL),$07            
299A: 2C              INC     L                   
299B: DD 5D           LD      E,IXL               
299D: 73              LD      (HL),E              
299E: 26 93           LD      H,$93               
29A0: E6 38           AND     $38                 
29A2: FE 38           CP      $38                 
29A4: 28 1B           JR      Z,$29C1             ; {}
29A6: 2D              DEC     L                   
29A7: 26 8B           LD      H,$8B               
29A9: 7E              LD      A,(HL)              
29AA: 57              LD      D,A                 
29AB: E6 78           AND     $78                 
29AD: 77              LD      (HL),A              
29AE: 2C              INC     L                   
29AF: 7A              LD      A,D                 
29B0: E6 07           AND     $07                 
29B2: CB 7A           BIT     7,D                 
29B4: 77              LD      (HL),A              
29B5: 3E 00           LD      A,$00               
29B7: 28 03           JR      Z,$29BC             ; {}
29B9: 3A E3 92        LD      A,($92E3)           
29BC: DD 77 0F        LD      (IX+$0F),A          
29BF: 18 1E           JR      $29DF               ; {}
29C1: 11 10 02        LD      DE,$0210            
29C4: CB 70           BIT     6,B                 
29C6: 20 0D           JR      NZ,$29D5            ; {}
29C8: 11 18 03        LD      DE,$0318            
29CB: 3A 26 98        LD      A,($9826)           
29CE: FE 02           CP      $02                 
29D0: 20 03           JR      NZ,$29D5            ; {}
29D2: 11 08 00        LD      DE,$0008            
29D5: 26 8B           LD      H,$8B               
29D7: 72              LD      (HL),D              
29D8: 2D              DEC     L                   
29D9: 73              LD      (HL),E              
29DA: 2C              INC     L                   
29DB: DD 36 0F 00     LD      (IX+$0F),$00        
29DF: 51              LD      D,C                 
29E0: CB B9           RES     7,C                 
29E2: 06 08           LD      B,$08               
29E4: CB 49           BIT     1,C                 
29E6: 28 02           JR      Z,$29EA             ; {}
29E8: 06 44           LD      B,$44               
29EA: DD 70 0E        LD      (IX+$0E),B          
29ED: 06 00           LD      B,$00               
29EF: 21 4A 2A        LD      HL,$2A4A            
29F2: 09              ADD     HL,BC               
29F3: 7E              LD      A,(HL)              
29F4: 23              INC     HL                  
29F5: DD 77 08        LD      (IX+$08),A          
29F8: AF              XOR     A                   
29F9: ED 6F           RLD                         
29FB: 47              LD      B,A                 
29FC: 7E              LD      A,(HL)              
29FD: E6 1F           AND     $1F                 
29FF: DD 77 09        LD      (IX+$09),A          
2A02: 78              LD      A,B                 
2A03: E6 0E           AND     $0E                 
2A05: 47              LD      B,A                 
2A06: 07              RLCA                        
2A07: 80              ADD     A,B                 
2A08: 21 7A 2A        LD      HL,$2A7A            
2A0B: D7              RST     0X10                
2A0C: CB 7A           BIT     7,D                 
2A0E: 28 03           JR      Z,$2A13             ; {}
2A10: 23              INC     HL                  
2A11: 23              INC     HL                  
2A12: 23              INC     HL                  
2A13: 7E              LD      A,(HL)              
2A14: 23              INC     HL                  
2A15: DD 77 01        LD      (IX+$01),A          
2A18: 7E              LD      A,(HL)              
2A19: 23              INC     HL                  
2A1A: DD 77 03        LD      (IX+$03),A          
2A1D: 7E              LD      A,(HL)              
2A1E: 23              INC     HL                  
2A1F: DD 77 05        LD      (IX+$05),A          
2A22: AF              XOR     A                   
2A23: DD 77 00        LD      (IX+$00),A          
2A26: DD 77 02        LD      (IX+$02),A          
2A29: DD 77 04        LD      (IX+$04),A          
2A2C: 3C              INC     A                   
2A2D: DD 77 0D        LD      (IX+$0D),A          
2A30: B2              OR      D                   
2A31: E6 81           AND     $81                 
2A33: DD 77 13        LD      (IX+$13),A          
2A36: C9              RET                         
2A37: 3A 87 92        LD      A,($9287)           
2A3A: A7              AND     A                   
2A3B: C0              RET     NZ                  
2A3C: 32 08 90        LD      ($9008),A           
2A3F: 3C              INC     A                   
2A40: 32 04 90        LD      ($9004),A           
2A43: 32 10 90        LD      ($9010),A           
2A46: 32 24 98        LD      ($9824),A           
2A49: C9              RET                         
2A4A: 1D              DEC     E                   
2A4B: 00              NOP                         
2A4C: 67              LD      H,A                 
2A4D: 20 9F           JR      NZ,$29EE            ; {}
2A4F: 40              LD      B,B                 
2A50: D4 20 7B        CALL    NC,$7B20            
2A53: 01 B0 61        LD      BC,$61B0            
2A56: E8              RET     PE                  
2A57: 01 F5 21        LD      BC,$21F5            
2A5A: 0B              DEC     BC                  
2A5B: 02              LD      (BC),A              
2A5C: 1B              DEC     DE                  
2A5D: 22 2B 82        LD      ($822B),HL          
2A60: 41              LD      B,C                 
2A61: 22 5D 82        LD      ($825D),HL          
2A64: 79              LD      A,C                 
2A65: 22 9E 02        LD      ($029E),HL          ; {}
2A68: BA              CP      D                   
2A69: 22 D9 02        LD      ($02D9),HL          ; {}
2A6C: FB              EI                          
2A6D: 22 1D 03        LD      ($031D),HL          ; {}
2A70: 33              INC     SP                  
2A71: 23              INC     HL                  
2A72: DA 0F F0        JP      C,$F00F             
2A75: 2F              CPL                         
2A76: 2B              DEC     HL                  
2A77: A2              AND     D                   
2A78: 5D              LD      E,L                 
2A79: A2              AND     D                   
2A7A: 9B              SBC     E                   
2A7B: 34              INC     (HL)                
2A7C: 03              INC     BC                  
2A7D: 9B              SBC     E                   
2A7E: 44              LD      B,H                 
2A7F: 03              INC     BC                  
2A80: 23              INC     HL                  
2A81: 00              NOP                         
2A82: 00              NOP                         
2A83: 23              INC     HL                  
2A84: 78              LD      A,B                 
2A85: 02              LD      (BC),A              
2A86: 9B              SBC     E                   
2A87: 2C              INC     L                   
2A88: 03              INC     BC                  
2A89: 9B              SBC     E                   
2A8A: 4C              LD      C,H                 
2A8B: 03              INC     BC                  
2A8C: 2B              DEC     HL                  
2A8D: 00              NOP                         
2A8E: 00              NOP                         
2A8F: 2B              DEC     HL                  
2A90: 78              LD      A,B                 
2A91: 02              LD      (BC),A              
2A92: 9B              SBC     E                   
2A93: 34              INC     (HL)                
2A94: 03              INC     BC                  
2A95: 9B              SBC     E                   
2A96: 34              INC     (HL)                
2A97: 03              INC     BC                  
2A98: 9B              SBC     E                   
2A99: 44              LD      B,H                 
2A9A: 03              INC     BC                  
2A9B: 9B              SBC     E                   
2A9C: 44              LD      B,H                 
2A9D: 03              INC     BC                  
2A9E: 3A A0 92        LD      A,($92A0)           
2AA1: 3D              DEC     A                   
2AA2: E6 03           AND     $03                 
2AA4: C0              RET     NZ                  
2AA5: 3A A7 92        LD      A,($92A7)           
2AA8: 47              LD      B,A                 
2AA9: 3A 08 90        LD      A,($9008)           
2AAC: B0              OR      B                   
2AAD: 28 48           JR      Z,$2AF7             ; {}
2AAF: 3A 0F 92        LD      A,($920F)           
2AB2: A7              AND     A                   
2AB3: 0E 01           LD      C,$01               
2AB5: 28 02           JR      Z,$2AB9             ; {}
2AB7: 0D              DEC     C                   
2AB8: 0D              DEC     C                   
2AB9: 2E 00           LD      L,$00               
2ABB: 06 0A           LD      B,$0A               
2ABD: 26 99           LD      H,$99               
2ABF: 7E              LD      A,(HL)              
2AC0: 81              ADD     A,C                 
2AC1: 77              LD      (HL),A              
2AC2: 26 98           LD      H,$98               
2AC4: 7E              LD      A,(HL)              
2AC5: 81              ADD     A,C                 
2AC6: 77              LD      (HL),A              
2AC7: 2C              INC     L                   
2AC8: 2C              INC     L                   
2AC9: 10 F2           DJNZ    $2ABD               ; {}
2ACB: 3A 24 98        LD      A,($9824)           
2ACE: A7              AND     A                   
2ACF: 3A 00 99        LD      A,($9900)           
2AD2: 28 03           JR      Z,$2AD7             ; {}
2AD4: A7              AND     A                   
2AD5: 28 11           JR      Z,$2AE8             ; {}
2AD7: FE 20           CP      $20                 
2AD9: 20 06           JR      NZ,$2AE1            ; {}
2ADB: 3E 01           LD      A,$01               
2ADD: 32 0F 92        LD      ($920F),A           
2AE0: C9              RET                         
2AE1: D6 E0           SUB     $E0                 
2AE3: C0              RET     NZ                  
2AE4: 32 0F 92        LD      ($920F),A           
2AE7: C9              RET                         
2AE8: AF              XOR     A                   
2AE9: 32 0F 92        LD      ($920F),A           
2AEC: 32 0A 90        LD      ($900A),A           
2AEF: 3C              INC     A                   
2AF0: 32 A0 9A        LD      ($9AA0),A           
2AF3: 32 09 90        LD      ($9009),A           
2AF6: C9              RET                         
2AF7: 32 0A 90        LD      ($900A),A           
2AFA: C9              RET                         
2AFB: FF              RST     0X38                
2AFC: FF              RST     0X38                
2AFD: FF              RST     0X38                
2AFE: FF              RST     0X38                
2AFF: FF              RST     0X38                
2B00: FF              RST     0X38                
2B01: FF              RST     0X38                
2B02: FF              RST     0X38                
2B03: FF              RST     0X38                
2B04: FF              RST     0X38                
2B05: FF              RST     0X38                
2B06: FF              RST     0X38                
2B07: FF              RST     0X38                
2B08: FF              RST     0X38                
2B09: FF              RST     0X38                
2B0A: FF              RST     0X38                
2B0B: FF              RST     0X38                
2B0C: FF              RST     0X38                
2B0D: FF              RST     0X38                
2B0E: FF              RST     0X38                
2B0F: FF              RST     0X38                
2B10: FF              RST     0X38                
2B11: FF              RST     0X38                
2B12: FF              RST     0X38                
2B13: FF              RST     0X38                
2B14: FF              RST     0X38                
2B15: FF              RST     0X38                
2B16: FF              RST     0X38                
2B17: FF              RST     0X38                
2B18: FF              RST     0X38                
2B19: FF              RST     0X38                
2B1A: FF              RST     0X38                
2B1B: FF              RST     0X38                
2B1C: FF              RST     0X38                
2B1D: FF              RST     0X38                
2B1E: FF              RST     0X38                
2B1F: FF              RST     0X38                
2B20: FF              RST     0X38                
2B21: FF              RST     0X38                
2B22: FF              RST     0X38                
2B23: FF              RST     0X38                
2B24: FF              RST     0X38                
2B25: FF              RST     0X38                
2B26: FF              RST     0X38                
2B27: FF              RST     0X38                
2B28: FF              RST     0X38                
2B29: FF              RST     0X38                
2B2A: FF              RST     0X38                
2B2B: FF              RST     0X38                
2B2C: FF              RST     0X38                
2B2D: FF              RST     0X38                
2B2E: FF              RST     0X38                
2B2F: FF              RST     0X38                
2B30: FF              RST     0X38                
2B31: FF              RST     0X38                
2B32: FF              RST     0X38                
2B33: FF              RST     0X38                
2B34: FF              RST     0X38                
2B35: FF              RST     0X38                
2B36: FF              RST     0X38                
2B37: FF              RST     0X38                
2B38: FF              RST     0X38                
2B39: FF              RST     0X38                
2B3A: FF              RST     0X38                
2B3B: FF              RST     0X38                
2B3C: FF              RST     0X38                
2B3D: FF              RST     0X38                
2B3E: FF              RST     0X38                
2B3F: FF              RST     0X38                
2B40: FF              RST     0X38                
2B41: FF              RST     0X38                
2B42: FF              RST     0X38                
2B43: FF              RST     0X38                
2B44: FF              RST     0X38                
2B45: FF              RST     0X38                
2B46: FF              RST     0X38                
2B47: FF              RST     0X38                
2B48: FF              RST     0X38                
2B49: FF              RST     0X38                
2B4A: FF              RST     0X38                
2B4B: FF              RST     0X38                
2B4C: FF              RST     0X38                
2B4D: FF              RST     0X38                
2B4E: FF              RST     0X38                
2B4F: FF              RST     0X38                
2B50: FF              RST     0X38                
2B51: FF              RST     0X38                
2B52: FF              RST     0X38                
2B53: FF              RST     0X38                
2B54: FF              RST     0X38                
2B55: FF              RST     0X38                
2B56: FF              RST     0X38                
2B57: FF              RST     0X38                
2B58: FF              RST     0X38                
2B59: FF              RST     0X38                
2B5A: FF              RST     0X38                
2B5B: FF              RST     0X38                
2B5C: FF              RST     0X38                
2B5D: FF              RST     0X38                
2B5E: FF              RST     0X38                
2B5F: FF              RST     0X38                
2B60: FF              RST     0X38                
2B61: FF              RST     0X38                
2B62: FF              RST     0X38                
2B63: FF              RST     0X38                
2B64: FF              RST     0X38                
2B65: FF              RST     0X38                
2B66: FF              RST     0X38                
2B67: FF              RST     0X38                
2B68: FF              RST     0X38                
2B69: FF              RST     0X38                
2B6A: FF              RST     0X38                
2B6B: FF              RST     0X38                
2B6C: FF              RST     0X38                
2B6D: FF              RST     0X38                
2B6E: FF              RST     0X38                
2B6F: FF              RST     0X38                
2B70: FF              RST     0X38                
2B71: FF              RST     0X38                
2B72: FF              RST     0X38                
2B73: FF              RST     0X38                
2B74: FF              RST     0X38                
2B75: FF              RST     0X38                
2B76: FF              RST     0X38                
2B77: FF              RST     0X38                
2B78: FF              RST     0X38                
2B79: FF              RST     0X38                
2B7A: FF              RST     0X38                
2B7B: FF              RST     0X38                
2B7C: FF              RST     0X38                
2B7D: FF              RST     0X38                
2B7E: FF              RST     0X38                
2B7F: FF              RST     0X38                
2B80: FF              RST     0X38                
2B81: FF              RST     0X38                
2B82: FF              RST     0X38                
2B83: FF              RST     0X38                
2B84: FF              RST     0X38                
2B85: FF              RST     0X38                
2B86: FF              RST     0X38                
2B87: FF              RST     0X38                
2B88: FF              RST     0X38                
2B89: FF              RST     0X38                
2B8A: FF              RST     0X38                
2B8B: FF              RST     0X38                
2B8C: FF              RST     0X38                
2B8D: FF              RST     0X38                
2B8E: FF              RST     0X38                
2B8F: FF              RST     0X38                
2B90: FF              RST     0X38                
2B91: FF              RST     0X38                
2B92: FF              RST     0X38                
2B93: FF              RST     0X38                
2B94: FF              RST     0X38                
2B95: FF              RST     0X38                
2B96: FF              RST     0X38                
2B97: FF              RST     0X38                
2B98: FF              RST     0X38                
2B99: FF              RST     0X38                
2B9A: FF              RST     0X38                
2B9B: FF              RST     0X38                
2B9C: FF              RST     0X38                
2B9D: FF              RST     0X38                
2B9E: FF              RST     0X38                
2B9F: FF              RST     0X38                
2BA0: FF              RST     0X38                
2BA1: FF              RST     0X38                
2BA2: FF              RST     0X38                
2BA3: FF              RST     0X38                
2BA4: FF              RST     0X38                
2BA5: FF              RST     0X38                
2BA6: FF              RST     0X38                
2BA7: FF              RST     0X38                
2BA8: FF              RST     0X38                
2BA9: FF              RST     0X38                
2BAA: FF              RST     0X38                
2BAB: FF              RST     0X38                
2BAC: FF              RST     0X38                
2BAD: FF              RST     0X38                
2BAE: FF              RST     0X38                
2BAF: FF              RST     0X38                
2BB0: FF              RST     0X38                
2BB1: FF              RST     0X38                
2BB2: FF              RST     0X38                
2BB3: FF              RST     0X38                
2BB4: FF              RST     0X38                
2BB5: FF              RST     0X38                
2BB6: FF              RST     0X38                
2BB7: FF              RST     0X38                
2BB8: FF              RST     0X38                
2BB9: FF              RST     0X38                
2BBA: FF              RST     0X38                
2BBB: FF              RST     0X38                
2BBC: FF              RST     0X38                
2BBD: FF              RST     0X38                
2BBE: FF              RST     0X38                
2BBF: FF              RST     0X38                
2BC0: FF              RST     0X38                
2BC1: FF              RST     0X38                
2BC2: FF              RST     0X38                
2BC3: FF              RST     0X38                
2BC4: FF              RST     0X38                
2BC5: FF              RST     0X38                
2BC6: FF              RST     0X38                
2BC7: FF              RST     0X38                
2BC8: FF              RST     0X38                
2BC9: FF              RST     0X38                
2BCA: FF              RST     0X38                
2BCB: FF              RST     0X38                
2BCC: FF              RST     0X38                
2BCD: FF              RST     0X38                
2BCE: FF              RST     0X38                
2BCF: FF              RST     0X38                
2BD0: FF              RST     0X38                
2BD1: FF              RST     0X38                
2BD2: FF              RST     0X38                
2BD3: FF              RST     0X38                
2BD4: FF              RST     0X38                
2BD5: FF              RST     0X38                
2BD6: FF              RST     0X38                
2BD7: FF              RST     0X38                
2BD8: FF              RST     0X38                
2BD9: FF              RST     0X38                
2BDA: FF              RST     0X38                
2BDB: FF              RST     0X38                
2BDC: FF              RST     0X38                
2BDD: FF              RST     0X38                
2BDE: FF              RST     0X38                
2BDF: FF              RST     0X38                
2BE0: FF              RST     0X38                
2BE1: FF              RST     0X38                
2BE2: FF              RST     0X38                
2BE3: FF              RST     0X38                
2BE4: FF              RST     0X38                
2BE5: FF              RST     0X38                
2BE6: FF              RST     0X38                
2BE7: FF              RST     0X38                
2BE8: FF              RST     0X38                
2BE9: FF              RST     0X38                
2BEA: FF              RST     0X38                
2BEB: FF              RST     0X38                
2BEC: FF              RST     0X38                
2BED: FF              RST     0X38                
2BEE: FF              RST     0X38                
2BEF: FF              RST     0X38                
2BF0: FF              RST     0X38                
2BF1: FF              RST     0X38                
2BF2: FF              RST     0X38                
2BF3: FF              RST     0X38                
2BF4: FF              RST     0X38                
2BF5: FF              RST     0X38                
2BF6: FF              RST     0X38                
2BF7: FF              RST     0X38                
2BF8: FF              RST     0X38                
2BF9: FF              RST     0X38                
2BFA: FF              RST     0X38                
2BFB: FF              RST     0X38                
2BFC: FF              RST     0X38                
2BFD: FF              RST     0X38                
2BFE: FF              RST     0X38                
2BFF: FF              RST     0X38                
2C00: 3A 21 98        LD      A,($9821)           
2C03: FE 1B           CP      $1B                 
2C05: 38 04           JR      C,$2C0B             ; {}
2C07: D6 04           SUB     $04                 
2C09: 18 F8           JR      $2C03               ; {}
2C0B: 3D              DEC     A                   
2C0C: 6F              LD      L,A                 
2C0D: 07              RLCA                        
2C0E: 07              RLCA                        
2C0F: 85              ADD     A,L                 
2C10: 5F              LD      E,A                 
2C11: 3A 84 99        LD      A,($9984)           
2C14: 21 65 2C        LD      HL,$2C65            
2C17: CF              RST     0X08                
2C18: 7E              LD      A,(HL)              
2C19: 23              INC     HL                  
2C1A: 66              LD      H,(HL)              
2C1B: 6F              LD      L,A                 
2C1C: 7B              LD      A,E                 
2C1D: D7              RST     0X10                
2C1E: 11 C0 99        LD      DE,$99C0            
2C21: 06 05           LD      B,$05               
2C23: 7E              LD      A,(HL)              
2C24: 4F              LD      C,A                 
2C25: 07              RLCA                        
2C26: 07              RLCA                        
2C27: 07              RLCA                        
2C28: 07              RLCA                        
2C29: E6 0F           AND     $0F                 
2C2B: 12              LD      (DE),A              
2C2C: 1C              INC     E                   
2C2D: 79              LD      A,C                 
2C2E: E6 0F           AND     $0F                 
2C30: 12              LD      (DE),A              
2C31: 1C              INC     E                   
2C32: 23              INC     HL                  
2C33: 10 EE           DJNZ    $2C23               ; {}
2C35: 3A 21 98        LD      A,($9821)           
2C38: FE 03           CP      $03                 
2C3A: 30 03           JR      NC,$2C3F            ; {}
2C3C: AF              XOR     A                   
2C3D: 18 07           JR      $2C46               ; {}
2C3F: F6 FC           OR      $FC                 
2C41: 3C              INC     A                   
2C42: 28 02           JR      Z,$2C46             ; {}
2C44: 3E 0A           LD      A,$0A               
2C46: 12              LD      (DE),A              
2C47: 01 16 02        LD      BC,$0216            
2C4A: ED 43 C1 92     LD      ($92C1),BC          
2C4E: ED 43 C0 92     LD      ($92C0),BC          
2C52: 3A 21 98        LD      A,($9821)           
2C55: FE 10           CP      $10                 
2C57: 38 02           JR      C,$2C5B             ; {}
2C59: 3E 10           LD      A,$10               
2C5B: 07              RLCA                        
2C5C: 07              RLCA                        
2C5D: E6 70           AND     $70                 
2C5F: C6 40           ADD     $40                 
2C61: 32 BB 99        LD      ($99BB),A           
2C64: C9              RET                         
2C65: EF              RST     0X28                
2C66: 2C              INC     L                   
2C67: 71              LD      (HL),C              
2C68: 2D              DEC     L                   
2C69: F3              DI                          
2C6A: 2D              DEC     L                   
2C6B: 6D              LD      L,L                 
2C6C: 2C              INC     L                   
2C6D: 00              NOP                         
2C6E: 00              NOP                         
2C6F: 22 C6 00        LD      ($00C6),HL          ; {}
2C72: 00              NOP                         
2C73: 11 23 C7        LD      DE,$C723            
2C76: 00              NOP                         
2C77: 00              NOP                         
2C78: 00              NOP                         
2C79: 00              NOP                         
2C7A: C0              RET     NZ                  
2C7B: 00              NOP                         
2C7C: 11 12 23        LD      DE,$2312            
2C7F: 97              SUB     A                   
2C80: 00              NOP                         
2C81: 11 23 23        LD      DE,$2323            
2C84: 98              SBC     B                   
2C85: 00              NOP                         
2C86: 21 24 33        LD      HL,$3324            
2C89: 98              SBC     B                   
2C8A: 00              NOP                         
2C8B: 00              NOP                         
2C8C: 00              NOP                         
2C8D: 00              NOP                         
2C8E: 90              SUB     B                   
2C8F: 00              NOP                         
2C90: 22 25 33        LD      ($3325),HL          ; {}
2C93: 99              SBC     C                   
2C94: 10 22           DJNZ    $2CB8               ; {}
2C96: 36 34           LD      (HL),$34            
2C98: 69              LD      L,C                 
2C99: 10 10           DJNZ    $2CAB               ; {}
2C9B: 11 23 97        LD      DE,$9723            
2C9E: 00              NOP                         
2C9F: 00              NOP                         
2CA0: 00              NOP                         
2CA1: 00              NOP                         
2CA2: 60              LD      H,B                 
2CA3: 00              NOP                         
2CA4: 32 46 34        LD      ($3446),A           ; {}
2CA7: 67              LD      H,A                 
2CA8: 11 32 67        LD      DE,$6732            
2CAB: 44              LD      B,H                 
2CAC: 68              LD      L,B                 
2CAD: 11 32 67        LD      DE,$6732            
2CB0: 45              LD      B,L                 
2CB1: 68              LD      L,B                 
2CB2: 11 00 00        LD      DE,$0000            
2CB5: 00              NOP                         
2CB6: 60              LD      H,B                 
2CB7: 00              NOP                         
2CB8: 42              LD      B,D                 
2CB9: 78              LD      A,B                 
2CBA: 45              LD      B,L                 
2CBB: 69              LD      L,C                 
2CBC: 11 42 78        LD      DE,$7842            
2CBF: 45              LD      B,L                 
2CC0: 69              LD      L,C                 
2CC1: 11 11 22        LD      DE,$2211            
2CC4: 23              INC     HL                  
2CC5: 97              SUB     A                   
2CC6: 11 00 00        LD      DE,$0000            
2CC9: 00              NOP                         
2CCA: 60              LD      H,B                 
2CCB: 00              NOP                         
2CCC: 52              LD      D,D                 
2CCD: 88              ADC     A,B                 
2CCE: 46              LD      B,(HL)              
2CCF: 3A 11 52        LD      A,($5211)           
2CD2: 88              ADC     A,B                 
2CD3: 56              LD      D,(HL)              
2CD4: 3A 11 52        LD      A,($5211)           
2CD7: 88              ADC     A,B                 
2CD8: 56              LD      D,(HL)              
2CD9: 3C              INC     A                   
2CDA: 11 00 00        LD      DE,$0000            
2CDD: 00              NOP                         
2CDE: 30 00           JR      NC,$2CE0            ; {}
2CE0: 62              LD      H,D                 
2CE1: 89              ADC     A,C                 
2CE2: 57              LD      D,A                 
2CE3: 3C              INC     A                   
2CE4: 11 62 99        LD      DE,$9962            
2CE7: 57              LD      D,A                 
2CE8: 3C              INC     A                   
2CE9: 11 62 99        LD      DE,$9962            
2CEC: 57              LD      D,A                 
2CED: 3C              INC     A                   
2CEE: 11 00 00        LD      DE,$0000            
2CF1: 12              LD      (DE),A              
2CF2: C6 00           ADD     $00                 
2CF4: 00              NOP                         
2CF5: 11 22 C6        LD      DE,$C622            
2CF8: 00              NOP                         
2CF9: 00              NOP                         
2CFA: 00              NOP                         
2CFB: 00              NOP                         
2CFC: C0              RET     NZ                  
2CFD: 00              NOP                         
2CFE: 11 12 23        LD      DE,$2312            
2D01: 97              SUB     A                   
2D02: 00              NOP                         
2D03: 11 12 23        LD      DE,$2312            
2D06: 97              SUB     A                   
2D07: 00              NOP                         
2D08: 00              NOP                         
2D09: 11 23 C7        LD      DE,$C723            
2D0C: 00              NOP                         
2D0D: 00              NOP                         
2D0E: 00              NOP                         
2D0F: 00              NOP                         
2D10: 90              SUB     B                   
2D11: 00              NOP                         
2D12: 21 23 33        LD      HL,$3323            
2D15: 98              SBC     B                   
2D16: 10 21           DJNZ    $2D39               ; {}
2D18: 24              INC     H                   
2D19: 33              INC     SP                  
2D1A: 98              SBC     B                   
2D1B: 10 21           DJNZ    $2D3E               ; {}
2D1D: 25              DEC     H                   
2D1E: 34              INC     (HL)                
2D1F: 98              SBC     B                   
2D20: 10 00           DJNZ    $2D22               ; {}
2D22: 00              NOP                         
2D23: 00              NOP                         
2D24: 60              LD      H,B                 
2D25: 00              NOP                         
2D26: 22 25 34        LD      ($3425),HL          ; {}
2D29: 68              LD      L,B                 
2D2A: 11 32 36        LD      DE,$3632            
2D2D: 44              LD      B,H                 
2D2E: 68              LD      L,B                 
2D2F: 11 11 11        LD      DE,$1111            
2D32: 23              INC     HL                  
2D33: 67              LD      H,A                 
2D34: 01 00 00        LD      BC,$0000            
2D37: 00              NOP                         
2D38: 60              LD      H,B                 
2D39: 00              NOP                         
2D3A: 32 36 45        LD      ($4536),A           
2D3D: 68              LD      L,B                 
2D3E: 11 32 46        LD      DE,$4632            
2D41: 45              LD      B,L                 
2D42: 69              LD      L,C                 
2D43: 11 32 67        LD      DE,$6732            
2D46: 45              LD      B,L                 
2D47: 69              LD      L,C                 
2D48: 11 00 00        LD      DE,$0000            
2D4B: 00              NOP                         
2D4C: 60              LD      H,B                 
2D4D: 00              NOP                         
2D4E: 42              LD      B,D                 
2D4F: 67              LD      H,A                 
2D50: 46              LD      B,(HL)              
2D51: 3A 11 42        LD      A,($4211)           
2D54: 78              LD      A,B                 
2D55: 56              LD      D,(HL)              
2D56: 3A 11 52        LD      A,($5211)           
2D59: 78              LD      A,B                 
2D5A: 56              LD      D,(HL)              
2D5B: 3A 11 00        LD      A,($0011)           ; {}
2D5E: 00              NOP                         
2D5F: 00              NOP                         
2D60: 30 00           JR      NC,$2D62            ; {}
2D62: 52              LD      D,D                 
2D63: 88              ADC     A,B                 
2D64: 56              LD      D,(HL)              
2D65: 3C              INC     A                   
2D66: 11 62 99        LD      DE,$9962            
2D69: 57              LD      D,A                 
2D6A: 3C              INC     A                   
2D6B: 11 62 99        LD      DE,$9962            
2D6E: 57              LD      D,A                 
2D6F: 3C              INC     A                   
2D70: 11 00 00        LD      DE,$0000            
2D73: 23              INC     HL                  
2D74: C6 00           ADD     $00                 
2D76: 10 11           DJNZ    $2D89               ; {}
2D78: 23              INC     HL                  
2D79: 97              SUB     A                   
2D7A: 00              NOP                         
2D7B: 00              NOP                         
2D7C: 00              NOP                         
2D7D: 00              NOP                         
2D7E: C0              RET     NZ                  
2D7F: 00              NOP                         
2D80: 11 12 33        LD      DE,$3312            
2D83: 98              SBC     B                   
2D84: 00              NOP                         
2D85: 21 23 34        LD      HL,$3423            
2D88: 68              LD      L,B                 
2D89: 00              NOP                         
2D8A: 21 24 34        LD      HL,$3424            
2D8D: 68              LD      L,B                 
2D8E: 00              NOP                         
2D8F: 00              NOP                         
2D90: 00              NOP                         
2D91: 00              NOP                         
2D92: 90              SUB     B                   
2D93: 00              NOP                         
2D94: 32 36 34        LD      ($3436),A           ; {}
2D97: 67              LD      H,A                 
2D98: 10 32           DJNZ    $2DCC               ; {}
2D9A: 46              LD      B,(HL)              
2D9B: 44              LD      B,H                 
2D9C: 68              LD      L,B                 
2D9D: 10 11           DJNZ    $2DB0               ; {}
2D9F: 11 23 97        LD      DE,$9723            
2DA2: 10 00           DJNZ    $2DA4               ; {}
2DA4: 00              NOP                         
2DA5: 00              NOP                         
2DA6: 60              LD      H,B                 
2DA7: 00              NOP                         
2DA8: 42              LD      B,D                 
2DA9: 67              LD      H,A                 
2DAA: 45              LD      B,L                 
2DAB: 68              LD      L,B                 
2DAC: 11 42 67        LD      DE,$6742            
2DAF: 45              LD      B,L                 
2DB0: 69              LD      L,C                 
2DB1: 11 42 78        LD      DE,$7842            
2DB4: 46              LD      B,(HL)              
2DB5: 69              LD      L,C                 
2DB6: 11 00 00        LD      DE,$0000            
2DB9: 00              NOP                         
2DBA: 60              LD      H,B                 
2DBB: 00              NOP                         
2DBC: 52              LD      D,D                 
2DBD: 78              LD      A,B                 
2DBE: 46              LD      B,(HL)              
2DBF: 3A 11 52        LD      A,($5211)           
2DC2: 88              ADC     A,B                 
2DC3: 56              LD      D,(HL)              
2DC4: 3A 11 52        LD      A,($5211)           
2DC7: 88              ADC     A,B                 
2DC8: 56              LD      D,(HL)              
2DC9: 3A 11 00        LD      A,($0011)           ; {}
2DCC: 00              NOP                         
2DCD: 00              NOP                         
2DCE: 60              LD      H,B                 
2DCF: 00              NOP                         
2DD0: 62              LD      H,D                 
2DD1: 88              ADC     A,B                 
2DD2: 56              LD      D,(HL)              
2DD3: 3C              INC     A                   
2DD4: 11 62 89        LD      DE,$8962            
2DD7: 57              LD      D,A                 
2DD8: 3C              INC     A                   
2DD9: 11 62 89        LD      DE,$8962            
2DDC: 57              LD      D,A                 
2DDD: 3E 11           LD      A,$11               
2DDF: 00              NOP                         
2DE0: 00              NOP                         
2DE1: 00              NOP                         
2DE2: 30 00           JR      NC,$2DE4            ; {}
2DE4: 72              LD      (HL),D              
2DE5: 99              SBC     C                   
2DE6: 57              LD      D,A                 
2DE7: 3E 11           LD      A,$11               
2DE9: 72              LD      (HL),D              
2DEA: 99              SBC     C                   
2DEB: 68              LD      L,B                 
2DEC: 3E 11           LD      A,$11               
2DEE: 72              LD      (HL),D              
2DEF: 99              SBC     C                   
2DF0: 68              LD      L,B                 
2DF1: 3E 11           LD      A,$11               
2DF3: 00              NOP                         
2DF4: 00              NOP                         
2DF5: 23              INC     HL                  
2DF6: C6 00           ADD     $00                 
2DF8: 10 11           DJNZ    $2E0B               ; {}
2DFA: 23              INC     HL                  
2DFB: 97              SUB     A                   
2DFC: 00              NOP                         
2DFD: 00              NOP                         
2DFE: 00              NOP                         
2DFF: 00              NOP                         
2E00: C0              RET     NZ                  
2E01: 00              NOP                         
2E02: 11 12 34        LD      DE,$3412            
2E05: 98              SBC     B                   
2E06: 00              NOP                         
2E07: 21 23 34        LD      HL,$3423            
2E0A: 68              LD      L,B                 
2E0B: 00              NOP                         
2E0C: 21 24 34        LD      HL,$3424            
2E0F: 68              LD      L,B                 
2E10: 00              NOP                         
2E11: 00              NOP                         
2E12: 00              NOP                         
2E13: 00              NOP                         
2E14: 90              SUB     B                   
2E15: 00              NOP                         
2E16: 32 36 45        LD      ($4536),A           
2E19: 67              LD      H,A                 
2E1A: 11 32 46        LD      DE,$4632            
2E1D: 46              LD      B,(HL)              
2E1E: 68              LD      L,B                 
2E1F: 11 32 56        LD      DE,$5632            
2E22: 46              LD      B,(HL)              
2E23: 69              LD      L,C                 
2E24: 11 00 00        LD      DE,$0000            
2E27: 00              NOP                         
2E28: 60              LD      H,B                 
2E29: 00              NOP                         
2E2A: 42              LD      B,D                 
2E2B: 67              LD      H,A                 
2E2C: 56              LD      D,(HL)              
2E2D: 6A              LD      L,D                 
2E2E: 11 42 67        LD      DE,$6742            
2E31: 56              LD      D,(HL)              
2E32: 6A              LD      L,D                 
2E33: 11 42 78        LD      DE,$7842            
2E36: 57              LD      D,A                 
2E37: 6A              LD      L,D                 
2E38: 11 00 00        LD      DE,$0000            
2E3B: 00              NOP                         
2E3C: 60              LD      H,B                 
2E3D: 00              NOP                         
2E3E: 52              LD      D,D                 
2E3F: 78              LD      A,B                 
2E40: 57              LD      D,A                 
2E41: 3A 11 52        LD      A,($5211)           
2E44: 88              ADC     A,B                 
2E45: 57              LD      D,A                 
2E46: 3A 11 52        LD      A,($5211)           
2E49: 88              ADC     A,B                 
2E4A: 68              LD      L,B                 
2E4B: 3C              INC     A                   
2E4C: 11 00 00        LD      DE,$0000            
2E4F: 00              NOP                         
2E50: 60              LD      H,B                 
2E51: 00              NOP                         
2E52: 62              LD      H,D                 
2E53: 88              ADC     A,B                 
2E54: 68              LD      L,B                 
2E55: 3C              INC     A                   
2E56: 11 62 89        LD      DE,$8962            
2E59: 68              LD      L,B                 
2E5A: 3C              INC     A                   
2E5B: 11 62 89        LD      DE,$8962            
2E5E: 68              LD      L,B                 
2E5F: 3E 11           LD      A,$11               
2E61: 00              NOP                         
2E62: 00              NOP                         
2E63: 00              NOP                         
2E64: 30 00           JR      NC,$2E66            ; {}
2E66: 72              LD      (HL),D              
2E67: 99              SBC     C                   
2E68: 68              LD      L,B                 
2E69: 3E 11           LD      A,$11               
2E6B: 72              LD      (HL),D              
2E6C: 99              SBC     C                   
2E6D: 68              LD      L,B                 
2E6E: 3E 11           LD      A,$11               
2E70: 72              LD      (HL),D              
2E71: 99              SBC     C                   
2E72: 68              LD      L,B                 
2E73: 3E 11           LD      A,$11               
2E75: FF              RST     0X38                
2E76: FF              RST     0X38                
2E77: FF              RST     0X38                
2E78: FF              RST     0X38                
2E79: FF              RST     0X38                
2E7A: FF              RST     0X38                
2E7B: FF              RST     0X38                
2E7C: FF              RST     0X38                
2E7D: FF              RST     0X38                
2E7E: FF              RST     0X38                
2E7F: FF              RST     0X38                
2E80: FF              RST     0X38                
2E81: FF              RST     0X38                
2E82: FF              RST     0X38                
2E83: FF              RST     0X38                
2E84: FF              RST     0X38                
2E85: FF              RST     0X38                
2E86: FF              RST     0X38                
2E87: FF              RST     0X38                
2E88: FF              RST     0X38                
2E89: FF              RST     0X38                
2E8A: FF              RST     0X38                
2E8B: FF              RST     0X38                
2E8C: FF              RST     0X38                
2E8D: FF              RST     0X38                
2E8E: FF              RST     0X38                
2E8F: FF              RST     0X38                
2E90: FF              RST     0X38                
2E91: FF              RST     0X38                
2E92: FF              RST     0X38                
2E93: FF              RST     0X38                
2E94: FF              RST     0X38                
2E95: FF              RST     0X38                
2E96: FF              RST     0X38                
2E97: FF              RST     0X38                
2E98: FF              RST     0X38                
2E99: FF              RST     0X38                
2E9A: FF              RST     0X38                
2E9B: FF              RST     0X38                
2E9C: FF              RST     0X38                
2E9D: FF              RST     0X38                
2E9E: FF              RST     0X38                
2E9F: FF              RST     0X38                
2EA0: FF              RST     0X38                
2EA1: FF              RST     0X38                
2EA2: FF              RST     0X38                
2EA3: FF              RST     0X38                
2EA4: FF              RST     0X38                
2EA5: FF              RST     0X38                
2EA6: FF              RST     0X38                
2EA7: FF              RST     0X38                
2EA8: FF              RST     0X38                
2EA9: FF              RST     0X38                
2EAA: FF              RST     0X38                
2EAB: FF              RST     0X38                
2EAC: FF              RST     0X38                
2EAD: FF              RST     0X38                
2EAE: FF              RST     0X38                
2EAF: FF              RST     0X38                
2EB0: FF              RST     0X38                
2EB1: FF              RST     0X38                
2EB2: FF              RST     0X38                
2EB3: FF              RST     0X38                
2EB4: FF              RST     0X38                
2EB5: FF              RST     0X38                
2EB6: FF              RST     0X38                
2EB7: FF              RST     0X38                
2EB8: FF              RST     0X38                
2EB9: FF              RST     0X38                
2EBA: FF              RST     0X38                
2EBB: FF              RST     0X38                
2EBC: FF              RST     0X38                
2EBD: FF              RST     0X38                
2EBE: FF              RST     0X38                
2EBF: FF              RST     0X38                
2EC0: FF              RST     0X38                
2EC1: FF              RST     0X38                
2EC2: FF              RST     0X38                
2EC3: FF              RST     0X38                
2EC4: FF              RST     0X38                
2EC5: FF              RST     0X38                
2EC6: FF              RST     0X38                
2EC7: FF              RST     0X38                
2EC8: FF              RST     0X38                
2EC9: FF              RST     0X38                
2ECA: FF              RST     0X38                
2ECB: FF              RST     0X38                
2ECC: FF              RST     0X38                
2ECD: FF              RST     0X38                
2ECE: FF              RST     0X38                
2ECF: FF              RST     0X38                
2ED0: FF              RST     0X38                
2ED1: FF              RST     0X38                
2ED2: FF              RST     0X38                
2ED3: FF              RST     0X38                
2ED4: FF              RST     0X38                
2ED5: FF              RST     0X38                
2ED6: FF              RST     0X38                
2ED7: FF              RST     0X38                
2ED8: FF              RST     0X38                
2ED9: FF              RST     0X38                
2EDA: FF              RST     0X38                
2EDB: FF              RST     0X38                
2EDC: FF              RST     0X38                
2EDD: FF              RST     0X38                
2EDE: FF              RST     0X38                
2EDF: FF              RST     0X38                
2EE0: FF              RST     0X38                
2EE1: FF              RST     0X38                
2EE2: FF              RST     0X38                
2EE3: FF              RST     0X38                
2EE4: FF              RST     0X38                
2EE5: FF              RST     0X38                
2EE6: FF              RST     0X38                
2EE7: FF              RST     0X38                
2EE8: FF              RST     0X38                
2EE9: FF              RST     0X38                
2EEA: FF              RST     0X38                
2EEB: FF              RST     0X38                
2EEC: FF              RST     0X38                
2EED: FF              RST     0X38                
2EEE: FF              RST     0X38                
2EEF: FF              RST     0X38                
2EF0: FF              RST     0X38                
2EF1: FF              RST     0X38                
2EF2: FF              RST     0X38                
2EF3: FF              RST     0X38                
2EF4: FF              RST     0X38                
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
2F00: FF              RST     0X38                
2F01: FF              RST     0X38                
2F02: FF              RST     0X38                
2F03: FF              RST     0X38                
2F04: FF              RST     0X38                
2F05: FF              RST     0X38                
2F06: FF              RST     0X38                
2F07: FF              RST     0X38                
2F08: FF              RST     0X38                
2F09: FF              RST     0X38                
2F0A: FF              RST     0X38                
2F0B: FF              RST     0X38                
2F0C: FF              RST     0X38                
2F0D: FF              RST     0X38                
2F0E: FF              RST     0X38                
2F0F: FF              RST     0X38                
2F10: FF              RST     0X38                
2F11: FF              RST     0X38                
2F12: FF              RST     0X38                
2F13: FF              RST     0X38                
2F14: FF              RST     0X38                
2F15: FF              RST     0X38                
2F16: FF              RST     0X38                
2F17: FF              RST     0X38                
2F18: FF              RST     0X38                
2F19: FF              RST     0X38                
2F1A: FF              RST     0X38                
2F1B: FF              RST     0X38                
2F1C: FF              RST     0X38                
2F1D: FF              RST     0X38                
2F1E: FF              RST     0X38                
2F1F: FF              RST     0X38                
2F20: FF              RST     0X38                
2F21: FF              RST     0X38                
2F22: FF              RST     0X38                
2F23: FF              RST     0X38                
2F24: FF              RST     0X38                
2F25: FF              RST     0X38                
2F26: FF              RST     0X38                
2F27: FF              RST     0X38                
2F28: FF              RST     0X38                
2F29: FF              RST     0X38                
2F2A: FF              RST     0X38                
2F2B: FF              RST     0X38                
2F2C: FF              RST     0X38                
2F2D: FF              RST     0X38                
2F2E: FF              RST     0X38                
2F2F: FF              RST     0X38                
2F30: FF              RST     0X38                
2F31: FF              RST     0X38                
2F32: FF              RST     0X38                
2F33: FF              RST     0X38                
2F34: FF              RST     0X38                
2F35: FF              RST     0X38                
2F36: FF              RST     0X38                
2F37: FF              RST     0X38                
2F38: FF              RST     0X38                
2F39: FF              RST     0X38                
2F3A: FF              RST     0X38                
2F3B: FF              RST     0X38                
2F3C: FF              RST     0X38                
2F3D: FF              RST     0X38                
2F3E: FF              RST     0X38                
2F3F: FF              RST     0X38                
2F40: FF              RST     0X38                
2F41: FF              RST     0X38                
2F42: FF              RST     0X38                
2F43: FF              RST     0X38                
2F44: FF              RST     0X38                
2F45: FF              RST     0X38                
2F46: FF              RST     0X38                
2F47: FF              RST     0X38                
2F48: FF              RST     0X38                
2F49: FF              RST     0X38                
2F4A: FF              RST     0X38                
2F4B: FF              RST     0X38                
2F4C: FF              RST     0X38                
2F4D: FF              RST     0X38                
2F4E: FF              RST     0X38                
2F4F: FF              RST     0X38                
2F50: FF              RST     0X38                
2F51: FF              RST     0X38                
2F52: FF              RST     0X38                
2F53: FF              RST     0X38                
2F54: FF              RST     0X38                
2F55: FF              RST     0X38                
2F56: FF              RST     0X38                
2F57: FF              RST     0X38                
2F58: FF              RST     0X38                
2F59: FF              RST     0X38                
2F5A: FF              RST     0X38                
2F5B: FF              RST     0X38                
2F5C: FF              RST     0X38                
2F5D: FF              RST     0X38                
2F5E: FF              RST     0X38                
2F5F: FF              RST     0X38                
2F60: FF              RST     0X38                
2F61: FF              RST     0X38                
2F62: FF              RST     0X38                
2F63: FF              RST     0X38                
2F64: FF              RST     0X38                
2F65: FF              RST     0X38                
2F66: FF              RST     0X38                
2F67: FF              RST     0X38                
2F68: FF              RST     0X38                
2F69: FF              RST     0X38                
2F6A: FF              RST     0X38                
2F6B: FF              RST     0X38                
2F6C: FF              RST     0X38                
2F6D: FF              RST     0X38                
2F6E: FF              RST     0X38                
2F6F: FF              RST     0X38                
2F70: FF              RST     0X38                
2F71: FF              RST     0X38                
2F72: FF              RST     0X38                
2F73: FF              RST     0X38                
2F74: FF              RST     0X38                
2F75: FF              RST     0X38                
2F76: FF              RST     0X38                
2F77: FF              RST     0X38                
2F78: FF              RST     0X38                
2F79: FF              RST     0X38                
2F7A: FF              RST     0X38                
2F7B: FF              RST     0X38                
2F7C: FF              RST     0X38                
2F7D: FF              RST     0X38                
2F7E: FF              RST     0X38                
2F7F: FF              RST     0X38                
2F80: FF              RST     0X38                
2F81: FF              RST     0X38                
2F82: FF              RST     0X38                
2F83: FF              RST     0X38                
2F84: FF              RST     0X38                
2F85: FF              RST     0X38                
2F86: FF              RST     0X38                
2F87: FF              RST     0X38                
2F88: FF              RST     0X38                
2F89: FF              RST     0X38                
2F8A: FF              RST     0X38                
2F8B: FF              RST     0X38                
2F8C: FF              RST     0X38                
2F8D: FF              RST     0X38                
2F8E: FF              RST     0X38                
2F8F: FF              RST     0X38                
2F90: FF              RST     0X38                
2F91: FF              RST     0X38                
2F92: FF              RST     0X38                
2F93: FF              RST     0X38                
2F94: FF              RST     0X38                
2F95: FF              RST     0X38                
2F96: FF              RST     0X38                
2F97: FF              RST     0X38                
2F98: FF              RST     0X38                
2F99: FF              RST     0X38                
2F9A: FF              RST     0X38                
2F9B: FF              RST     0X38                
2F9C: FF              RST     0X38                
2F9D: FF              RST     0X38                
2F9E: FF              RST     0X38                
2F9F: FF              RST     0X38                
2FA0: FF              RST     0X38                
2FA1: FF              RST     0X38                
2FA2: FF              RST     0X38                
2FA3: FF              RST     0X38                
2FA4: FF              RST     0X38                
2FA5: FF              RST     0X38                
2FA6: FF              RST     0X38                
2FA7: FF              RST     0X38                
2FA8: FF              RST     0X38                
2FA9: FF              RST     0X38                
2FAA: FF              RST     0X38                
2FAB: FF              RST     0X38                
2FAC: FF              RST     0X38                
2FAD: FF              RST     0X38                
2FAE: FF              RST     0X38                
2FAF: FF              RST     0X38                
2FB0: FF              RST     0X38                
2FB1: FF              RST     0X38                
2FB2: FF              RST     0X38                
2FB3: FF              RST     0X38                
2FB4: FF              RST     0X38                
2FB5: FF              RST     0X38                
2FB6: FF              RST     0X38                
2FB7: FF              RST     0X38                
2FB8: FF              RST     0X38                
2FB9: FF              RST     0X38                
2FBA: FF              RST     0X38                
2FBB: FF              RST     0X38                
2FBC: FF              RST     0X38                
2FBD: FF              RST     0X38                
2FBE: FF              RST     0X38                
2FBF: FF              RST     0X38                
2FC0: FF              RST     0X38                
2FC1: FF              RST     0X38                
2FC2: FF              RST     0X38                
2FC3: FF              RST     0X38                
2FC4: FF              RST     0X38                
2FC5: FF              RST     0X38                
2FC6: FF              RST     0X38                
2FC7: FF              RST     0X38                
2FC8: FF              RST     0X38                
2FC9: FF              RST     0X38                
2FCA: FF              RST     0X38                
2FCB: FF              RST     0X38                
2FCC: FF              RST     0X38                
2FCD: FF              RST     0X38                
2FCE: FF              RST     0X38                
2FCF: FF              RST     0X38                
2FD0: FF              RST     0X38                
2FD1: FF              RST     0X38                
2FD2: FF              RST     0X38                
2FD3: FF              RST     0X38                
2FD4: FF              RST     0X38                
2FD5: FF              RST     0X38                
2FD6: FF              RST     0X38                
2FD7: FF              RST     0X38                
2FD8: FF              RST     0X38                
2FD9: FF              RST     0X38                
2FDA: FF              RST     0X38                
2FDB: FF              RST     0X38                
2FDC: FF              RST     0X38                
2FDD: FF              RST     0X38                
2FDE: FF              RST     0X38                
2FDF: FF              RST     0X38                
2FE0: FF              RST     0X38                
2FE1: FF              RST     0X38                
2FE2: FF              RST     0X38                
2FE3: FF              RST     0X38                
2FE4: FF              RST     0X38                
2FE5: FF              RST     0X38                
2FE6: FF              RST     0X38                
2FE7: FF              RST     0X38                
2FE8: FF              RST     0X38                
2FE9: FF              RST     0X38                
2FEA: FF              RST     0X38                
2FEB: FF              RST     0X38                
2FEC: FF              RST     0X38                
2FED: FF              RST     0X38                
2FEE: FF              RST     0X38                
2FEF: FF              RST     0X38                
2FF0: FF              RST     0X38                
2FF1: FF              RST     0X38                
2FF2: FF              RST     0X38                
2FF3: FF              RST     0X38                
2FF4: FF              RST     0X38                
2FF5: FF              RST     0X38                
2FF6: FF              RST     0X38                
2FF7: FF              RST     0X38                
2FF8: FF              RST     0X38                
2FF9: FF              RST     0X38                
2FFA: FF              RST     0X38                
2FFB: FF              RST     0X38                
2FFC: FF              RST     0X38                
2FFD: FF              RST     0X38                
2FFE: FF              RST     0X38                
2FFF: 50              LD      D,B                 
3000: 21 FD 83        LD      HL,$83FD            
3003: 3A 40 98        LD      A,($9840)           
3006: A7              AND     A                   
3007: 28 03           JR      Z,$300C             ; {}
3009: 21 E8 83        LD      HL,$83E8            
300C: 22 00 8A        LD      ($8A00),HL          
300F: 11 3D 8A        LD      DE,$8A3D            
3012: CD F7 31        CALL    $31F7               ; {}
3015: D0              RET     NC                  
3016: 11 37 8A        LD      DE,$8A37            
3019: CD F7 31        CALL    $31F7               ; {}
301C: 3E 05           LD      A,$05               
301E: 30 27           JR      NC,$3047            ; {}
3020: 11 31 8A        LD      DE,$8A31            
3023: CD F7 31        CALL    $31F7               ; {}
3026: 3E 04           LD      A,$04               
3028: 30 1D           JR      NC,$3047            ; {}
302A: 11 2B 8A        LD      DE,$8A2B            
302D: CD F7 31        CALL    $31F7               ; {}
3030: 3E 03           LD      A,$03               
3032: 30 13           JR      NC,$3047            ; {}
3034: 11 25 8A        LD      DE,$8A25            
3037: CD F7 31        CALL    $31F7               ; {}
303A: 3E 02           LD      A,$02               
303C: 30 09           JR      NC,$3047            ; {}
303E: 3E FF           LD      A,$FF               
3040: 32 AC 9A        LD      ($9AAC),A           
3043: 3E 01           LD      A,$01               
3045: 18 03           JR      $304A               ; {}
3047: 32 B0 9A        LD      ($9AB0),A           
304A: 32 11 8A        LD      ($8A11),A           
304D: 21 A6 31        LD      HL,$31A6            
3050: 3D              DEC     A                   
3051: CF              RST     0X08                
3052: CD 18 31        CALL    $3118               ; {}
3055: 3A 11 8A        LD      A,($8A11)           
3058: 21 A1 31        LD      HL,$31A1            
305B: 3D              DEC     A                   
305C: D7              RST     0X10                
305D: 7E              LD      A,(HL)              
305E: 21 49 8A        LD      HL,$8A49            
3061: 11 4C 8A        LD      DE,$8A4C            
3064: A7              AND     A                   
3065: 28 05           JR      Z,$306C             ; {}
3067: 4F              LD      C,A                 
3068: 06 00           LD      B,$00               
306A: ED B8           LDDR                        
306C: 06 03           LD      B,$03               
306E: 3E 24           LD      A,$24               
3070: 22 04 8A        LD      ($8A04),HL          
3073: 2C              INC     L                   
3074: 77              LD      (HL),A              
3075: 10 FC           DJNZ    $3073               ; {}
3077: 3E 49           LD      A,$49               
3079: 32 10 8A        LD      ($8A10),A           
307C: 21 7F 32        LD      HL,$327F            
307F: CD 28 33        CALL    $3328               ; {}
3082: CD 1B 33        CALL    $331B               ; {}
3085: CD 28 33        CALL    $3328               ; {}
3088: 11 09 83        LD      DE,$8309            
308B: 2A 00 8A        LD      HL,($8A00)          
308E: CD 75 32        CALL    $3275               ; {}
3091: 21 49 81        LD      HL,$8149            
3094: 11 E0 FF        LD      DE,$FFE0            
3097: 36 0A           LD      (HL),$0A            
3099: 19              ADD     HL,DE               
309A: 36 0A           LD      (HL),$0A            
309C: 19              ADD     HL,DE               
309D: 36 0A           LD      (HL),$0A            
309F: CD 1D 32        CALL    $321D               ; {}
30A2: CD 80 31        CALL    $3180               ; {}
30A5: 3E 04           LD      A,$04               
30A7: 32 AE 92        LD      ($92AE),A           
30AA: 3A AE 92        LD      A,($92AE)           
30AD: A7              AND     A                   
30AE: 20 FA           JR      NZ,$30AA            ; {}
30B0: 3E 28           LD      A,$28               
30B2: 32 AE 92        LD      ($92AE),A           
30B5: CD 1D 32        CALL    $321D               ; {}
30B8: CD 80 31        CALL    $3180               ; {}
30BB: 3A A0 92        LD      A,($92A0)           
30BE: 4F              LD      C,A                 
30BF: CD ED 32        CALL    $32ED               ; {}
30C2: 3A A0 92        LD      A,($92A0)           
30C5: B9              CP      C                   
30C6: 28 F7           JR      Z,$30BF             ; {}
30C8: 4F              LD      C,A                 
30C9: E6 0F           AND     $0F                 
30CB: CC 41 31        CALL    Z,$3141             ; {}
30CE: 21 B6 99        LD      HL,$99B6            
30D1: 3A 15 92        LD      A,($9215)           
30D4: A7              AND     A                   
30D5: 28 01           JR      Z,$30D8             ; {}
30D7: 23              INC     HL                  
30D8: CB 66           BIT     4,(HL)              
30DA: CA 4C 31        JP      Z,$314C             ; {}
30DD: 7E              LD      A,(HL)              
30DE: E6 0A           AND     $0A                 
30E0: 21 02 8A        LD      HL,$8A02            
30E3: 11 03 8A        LD      DE,$8A03            
30E6: BE              CP      (HL)                
30E7: 28 04           JR      Z,$30ED             ; {}
30E9: 77              LD      (HL),A              
30EA: 3E FD           LD      A,$FD               
30EC: 12              LD      (DE),A              
30ED: 1A              LD      A,(DE)              
30EE: 3C              INC     A                   
30EF: 12              LD      (DE),A              
30F0: E6 0F           AND     $0F                 
30F2: 20 CB           JR      NZ,$30BF            ; {}
30F4: 7E              LD      A,(HL)              
30F5: FE 08           CP      $08                 
30F7: 28 24           JR      Z,$311D             ; {}
30F9: FE 02           CP      $02                 
30FB: 20 C2           JR      NZ,$30BF            ; {}
30FD: 3E 28           LD      A,$28               
30FF: 32 AE 92        LD      ($92AE),A           
3102: 3A 10 8A        LD      A,($8A10)           
3105: 6F              LD      L,A                 
3106: 26 81           LD      H,$81               
3108: 7E              LD      A,(HL)              
3109: 3D              DEC     A                   
310A: FE 09           CP      $09                 
310C: CC 38 31        CALL    Z,$3138             ; {}
310F: FE 29           CP      $29                 
3111: CC 3B 31        CALL    Z,$313B             ; {}
3114: 77              LD      (HL),A              
3115: C3 BF 30        JP      $30BF               ; {}
3118: 7E              LD      A,(HL)              
3119: 23              INC     HL                  
311A: 66              LD      H,(HL)              
311B: 6F              LD      L,A                 
311C: E9              JP      (HL)                
311D: 3A 10 8A        LD      A,($8A10)           
3120: 6F              LD      L,A                 
3121: 26 81           LD      H,$81               
3123: 3E 28           LD      A,$28               
3125: 32 AE 92        LD      ($92AE),A           
3128: 7E              LD      A,(HL)              
3129: 3C              INC     A                   
312A: FE 2B           CP      $2B                 
312C: CC 3E 31        CALL    Z,$313E             ; {}
312F: FE 25           CP      $25                 
3131: CC 38 31        CALL    Z,$3138             ; {}
3134: 77              LD      (HL),A              
3135: C3 BF 30        JP      $30BF               ; {}
3138: 3E 2A           LD      A,$2A               
313A: C9              RET                         
313B: 3E 24           LD      A,$24               
313D: C9              RET                         
313E: 3E 0A           LD      A,$0A               
3140: C9              RET                         
3141: 3A 10 8A        LD      A,($8A10)           
3144: 6F              LD      L,A                 
3145: 26 85           LD      H,$85               
3147: 7E              LD      A,(HL)              
3148: EE 05           XOR     $05                 
314A: 77              LD      (HL),A              
314B: C9              RET                         
314C: 3A 10 8A        LD      A,($8A10)           
314F: 6F              LD      L,A                 
3150: 26 85           LD      H,$85               
3152: 36 00           LD      (HL),$00            
3154: 26 81           LD      H,$81               
3156: 4E              LD      C,(HL)              
3157: 3E 28           LD      A,$28               
3159: 32 AE 92        LD      ($92AE),A           
315C: 2A 04 8A        LD      HL,($8A04)          
315F: 23              INC     HL                  
3160: 71              LD      (HL),C              
3161: 22 04 8A        LD      ($8A04),HL          
3164: 21 10 8A        LD      HL,$8A10            
3167: 7E              LD      A,(HL)              
3168: D6 20           SUB     $20                 
316A: 77              LD      (HL),A              
316B: D2 B5 30        JP      NC,$30B5            ; {}
316E: CD 1D 32        CALL    $321D               ; {}
3171: CD 80 31        CALL    $3180               ; {}
3174: 3E 4C           LD      A,$4C               
3176: 32 A0 92        LD      ($92A0),A           
3179: 3A A0 92        LD      A,($92A0)           
317C: A7              AND     A                   
317D: 20 FA           JR      NZ,$3179            ; {}
317F: C9              RET                         
3180: 3A 11 8A        LD      A,($8A11)           
3183: 21 97 31        LD      HL,$3197            
3186: 3D              DEC     A                   
3187: CF              RST     0X08                
3188: 7E              LD      A,(HL)              
3189: 23              INC     HL                  
318A: 66              LD      H,(HL)              
318B: 6F              LD      L,A                 
318C: 06 16           LD      B,$16               
318E: 11 E0 FF        LD      DE,$FFE0            
3191: 36 05           LD      (HL),$05            
3193: 19              ADD     HL,DE               
3194: 10 FB           DJNZ    $3191               ; {}
3196: C9              RET                         
3197: 74              LD      (HL),H              
3198: 87              ADD     A,A                 
3199: 76              HALT                        
319A: 87              ADD     A,A                 
319B: 78              LD      A,B                 
319C: 87              ADD     A,A                 
319D: 7A              LD      A,D                 
319E: 87              ADD     A,A                 
319F: 7C              LD      A,H                 
31A0: 87              ADD     A,A                 
31A1: 0C              INC     C                   
31A2: 09              ADD     HL,BC               
31A3: 06 03           LD      B,$03               
31A5: 00              NOP                         
31A6: B0              OR      B                   
31A7: 31 B4 31        LD      SP,$31B4            
31AA: B8              CP      B                   
31AB: 31 CE 31        LD      SP,$31CE            
31AE: D9              EXX                         
31AF: 31 3E 12        LD      SP,$123E            
31B2: 18 06           JR      $31BA               ; {}
31B4: 3E 0C           LD      A,$0C               
31B6: 18 02           JR      $31BA               ; {}
31B8: 3E 06           LD      A,$06               
31BA: 21 37 8A        LD      HL,$8A37            
31BD: 11 3D 8A        LD      DE,$8A3D            
31C0: 01 06 00        LD      BC,$0006            
31C3: ED B8           LDDR                        
31C5: 11 37 8A        LD      DE,$8A37            
31C8: 4F              LD      C,A                 
31C9: ED B8           LDDR                        
31CB: C3 D9 31        JP      $31D9               ; {}
31CE: 11 3D 8A        LD      DE,$8A3D            
31D1: 21 37 8A        LD      HL,$8A37            
31D4: 01 06 00        LD      BC,$0006            
31D7: ED B8           LDDR                        
31D9: 3A 11 8A        LD      A,($8A11)           
31DC: 3D              DEC     A                   
31DD: 21 ED 31        LD      HL,$31ED            
31E0: CF              RST     0X08                
31E1: 5E              LD      E,(HL)              
31E2: 23              INC     HL                  
31E3: 56              LD      D,(HL)              
31E4: 2A 00 8A        LD      HL,($8A00)          
31E7: 01 06 00        LD      BC,$0006            
31EA: ED B8           LDDR                        
31EC: C9              RET                         
31ED: 25              DEC     H                   
31EE: 8A              ADC     A,D                 
31EF: 2B              DEC     HL                  
31F0: 8A              ADC     A,D                 
31F1: 31 8A 37        LD      SP,$378A            
31F4: 8A              ADC     A,D                 
31F5: 3D              DEC     A                   
31F6: 8A              ADC     A,D                 
31F7: 2A 00 8A        LD      HL,($8A00)          
31FA: 06 06           LD      B,$06               
31FC: 1A              LD      A,(DE)              
31FD: FE 24           CP      $24                 
31FF: 28 0D           JR      Z,$320E             ; {}
3201: 7E              LD      A,(HL)              
3202: FE 24           CP      $24                 
3204: C8              RET     Z                   
3205: 1A              LD      A,(DE)              
3206: BE              CP      (HL)                
3207: C0              RET     NZ                  
3208: 2D              DEC     L                   
3209: 1D              DEC     E                   
320A: 10 F0           DJNZ    $31FC               ; {}
320C: AF              XOR     A                   
320D: C9              RET                         
320E: BE              CP      (HL)                
320F: 28 F7           JR      Z,$3208             ; {}
3211: AF              XOR     A                   
3212: 18 F2           JR      $3206               ; {}
3214: 21 45 33        LD      HL,$3345            
3217: CD 28 33        CALL    $3328               ; {}
321A: CD 28 33        CALL    $3328               ; {}
321D: 21 B4 32        LD      HL,$32B4            
3220: CD 1B 33        CALL    $331B               ; {}
3223: 06 01           LD      B,$01               
3225: CD 31 32        CALL    $3231               ; {}
3228: CD 31 32        CALL    $3231               ; {}
322B: CD 31 32        CALL    $3231               ; {}
322E: CD 31 32        CALL    $3231               ; {}
3231: 78              LD      A,B                 
3232: 3D              DEC     A                   
3233: 87              ADD     A,A                 
3234: 87              ADD     A,A                 
3235: 87              ADD     A,A                 
3236: 21 C5 32        LD      HL,$32C5            
3239: D7              RST     0X10                
323A: 5E              LD      E,(HL)              
323B: 23              INC     HL                  
323C: 56              LD      D,(HL)              
323D: 23              INC     HL                  
323E: 78              LD      A,B                 
323F: 12              LD      (DE),A              
3240: CD 73 32        CALL    $3273               ; {}
3243: CD 70 32        CALL    $3270               ; {}
3246: CD 70 32        CALL    $3270               ; {}
3249: CD 73 32        CALL    $3273               ; {}
324C: CD 73 32        CALL    $3273               ; {}
324F: 7E              LD      A,(HL)              
3250: 23              INC     HL                  
3251: 4E              LD      C,(HL)              
3252: 23              INC     HL                  
3253: E5              PUSH    HL                  
3254: 61              LD      H,C                 
3255: 6F              LD      L,A                 
3256: CD 75 32        CALL    $3275               ; {}
3259: 7B              LD      A,E                 
325A: D6 C0           SUB     $C0                 
325C: 5F              LD      E,A                 
325D: 30 01           JR      NC,$3260            ; {}
325F: 15              DEC     D                   
3260: E1              POP     HL                  
3261: 7E              LD      A,(HL)              
3262: 23              INC     HL                  
3263: 66              LD      H,(HL)              
3264: 6F              LD      L,A                 
3265: CD 70 32        CALL    $3270               ; {}
3268: CD 70 32        CALL    $3270               ; {}
326B: CD 70 32        CALL    $3270               ; {}
326E: 04              INC     B                   
326F: C9              RET                         
3270: 7E              LD      A,(HL)              
3271: 12              LD      (DE),A              
3272: 23              INC     HL                  
3273: E7              RST     0X20                
3274: C9              RET                         
3275: 0E 06           LD      C,$06               
3277: 7E              LD      A,(HL)              
3278: 12              LD      (DE),A              
3279: 2B              DEC     HL                  
327A: E7              RST     0X20                
327B: 0D              DEC     C                   
327C: 20 F9           JR      NZ,$3277            ; {}
327E: C9              RET                         
327F: 24              INC     H                   
3280: 83              ADD     A,E                 
3281: 15              DEC     D                   
3282: 04              INC     B                   
3283: 0E 17           LD      C,$17               
3285: 1D              DEC     E                   
3286: 0E 1B           LD      C,$1B               
3288: 24              INC     H                   
3289: 22 18 1E        LD      ($1E18),HL          ; {}
328C: 1B              DEC     DE                  
328D: 24              INC     H                   
328E: 12              LD      (DE),A              
328F: 17              RLA                         
3290: 12              LD      (DE),A              
3291: 1D              DEC     E                   
3292: 12              LD      (DE),A              
3293: 0A              LD      A,(BC)              
3294: 15              DEC     D                   
3295: 1C              INC     E                   
3296: 24              INC     H                   
3297: 2C              INC     L                   
3298: E7              RST     0X20                
3299: 82              ADD     A,D                 
329A: 10 1C           DJNZ    $32B8               ; {}
329C: 0C              INC     C                   
329D: 18 1B           JR      $32BA               ; {}
329F: 0E 24           LD      C,$24               
32A1: 24              INC     H                   
32A2: 24              INC     H                   
32A3: 24              INC     H                   
32A4: 24              INC     H                   
32A5: 24              INC     H                   
32A6: 24              INC     H                   
32A7: 17              RLA                         
32A8: 0A              LD      A,(BC)              
32A9: 16 0E           LD      D,$0E               
32AB: 50              LD      D,B                 
32AC: 82              ADD     A,D                 
32AD: 05              DEC     B                   
32AE: 04              INC     B                   
32AF: 1D              DEC     E                   
32B0: 18 19           JR      $32CB               ; {}
32B2: 24              INC     H                   
32B3: 05              DEC     B                   
32B4: 92              SUB     D                   
32B5: 82              ADD     A,D                 
32B6: 0E 1C           LD      C,$1C               
32B8: 0C              INC     C                   
32B9: 18 1B           JR      $32D6               ; {}
32BB: 0E 24           LD      C,$24               
32BD: 24              INC     H                   
32BE: 24              INC     H                   
32BF: 24              INC     H                   
32C0: 24              INC     H                   
32C1: 17              RLA                         
32C2: 0A              LD      A,(BC)              
32C3: 16 0E           LD      D,$0E               
32C5: 54              LD      D,H                 
32C6: 83              ADD     A,E                 
32C7: 1C              INC     E                   
32C8: 1D              DEC     E                   
32C9: 25              DEC     H                   
32CA: 8A              ADC     A,D                 
32CB: 3E 8A           LD      A,$8A               
32CD: 56              LD      D,(HL)              
32CE: 83              ADD     A,E                 
32CF: 17              RLA                         
32D0: 0D              DEC     C                   
32D1: 2B              DEC     HL                  
32D2: 8A              ADC     A,D                 
32D3: 41              LD      B,C                 
32D4: 8A              ADC     A,D                 
32D5: 58              LD      E,B                 
32D6: 83              ADD     A,E                 
32D7: 1B              DEC     DE                  
32D8: 0D              DEC     C                   
32D9: 31 8A 44        LD      SP,$448A            
32DC: 8A              ADC     A,D                 
32DD: 5A              LD      E,D                 
32DE: 83              ADD     A,E                 
32DF: 1D              DEC     E                   
32E0: 11 37 8A        LD      DE,$8A37            
32E3: 47              LD      B,A                 
32E4: 8A              ADC     A,D                 
32E5: 5C              LD      E,H                 
32E6: 83              ADD     A,E                 
32E7: 1D              DEC     E                   
32E8: 11 3D 8A        LD      DE,$8A3D            
32EB: 4A              LD      C,D                 
32EC: 8A              ADC     A,D                 
32ED: 3A B5 99        LD      A,($99B5)           
32F0: FE A0           CP      $A0                 
32F2: 28 07           JR      Z,$32FB             ; {}
32F4: 47              LD      B,A                 
32F5: 3A B8 99        LD      A,($99B8)           
32F8: B8              CP      B                   
32F9: 38 05           JR      C,$3300             ; {}
32FB: 3A AE 92        LD      A,($92AE)           
32FE: A7              AND     A                   
32FF: C0              RET     NZ                  
3300: E1              POP     HL                  
3301: 26 81           LD      H,$81               
3303: 3A 10 8A        LD      A,($8A10)           
3306: 6F              LD      L,A                 
3307: ED 5B 04 8A     LD      DE,($8A04)          
330B: 13              INC     DE                  
330C: ED A0           LDI                         
330E: 3E DF           LD      A,$DF               
3310: 25              DEC     H                   
3311: 85              ADD     A,L                 
3312: 30 01           JR      NC,$3315            ; {}
3314: 24              INC     H                   
3315: 6F              LD      L,A                 
3316: CB 44           BIT     0,H                 
3318: 20 F2           JR      NZ,$330C            ; {}
331A: C9              RET                         
331B: 5E              LD      E,(HL)              
331C: 23              INC     HL                  
331D: 56              LD      D,(HL)              
331E: 23              INC     HL                  
331F: 46              LD      B,(HL)              
3320: 23              INC     HL                  
3321: 7E              LD      A,(HL)              
3322: 12              LD      (DE),A              
3323: 23              INC     HL                  
3324: E7              RST     0X20                
3325: 10 FA           DJNZ    $3321               ; {}
3327: C9              RET                         
3328: 5E              LD      E,(HL)              
3329: 23              INC     HL                  
332A: 56              LD      D,(HL)              
332B: 23              INC     HL                  
332C: 46              LD      B,(HL)              
332D: 23              INC     HL                  
332E: 4E              LD      C,(HL)              
332F: 23              INC     HL                  
3330: EB              EX      DE,HL               
3331: 1A              LD      A,(DE)              
3332: 77              LD      (HL),A              
3333: CB D4           SET     2,H                 
3335: 71              LD      (HL),C              
3336: CB 94           RES     2,H                 
3338: 13              INC     DE                  
3339: 3E E0           LD      A,$E0               
333B: 25              DEC     H                   
333C: 85              ADD     A,L                 
333D: 30 01           JR      NC,$3340            ; {}
333F: 24              INC     H                   
3340: 6F              LD      L,A                 
3341: 10 EE           DJNZ    $3331               ; {}
3343: EB              EX      DE,HL               
3344: C9              RET                         
3345: 25              DEC     H                   
3346: 83              ADD     A,E                 
3347: 13              INC     DE                  
3348: 02              LD      (BC),A              
3349: 1D              DEC     E                   
334A: 11 0E 24        LD      DE,$240E            
334D: 10 0A           DJNZ    $3359               ; {}
334F: 15              DEC     D                   
3350: 0A              LD      A,(BC)              
3351: 0C              INC     C                   
3352: 1D              DEC     E                   
3353: 12              LD      (DE),A              
3354: 0C              INC     C                   
3355: 24              INC     H                   
3356: 11 0E 1B        LD      DE,$1B0E            
3359: 18 0E           JR      $3369               ; {}
335B: 1C              INC     E                   
335C: CC 82 0C        CALL    Z,$0C82             ; {}
335F: 04              INC     B                   
3360: 26 26           LD      H,$26               
3362: 24              INC     H                   
3363: 0B              DEC     BC                  
3364: 0E 1C           LD      C,$1C               
3366: 1D              DEC     E                   
3367: 24              INC     H                   
3368: 05              DEC     B                   
3369: 24              INC     H                   
336A: 26 26           LD      H,$26               
336C: AF              XOR     A                   
336D: 32 23 68        LD      ($6823),A           
3370: 3C              INC     A                   
3371: 32 22 68        LD      ($6822),A           
3374: F3              DI                          
3375: 32 30 68        LD      ($6830),A           
3378: 06 0A           LD      B,$0A               
337A: D9              EXX                         
337B: 11 00 80        LD      DE,$8000            
337E: 21 00 00        LD      HL,$0000            
3381: 01 00 04        LD      BC,$0400            
3384: 7D              LD      A,L                 
3385: AC              XOR     H                   
3386: 2F              CPL                         
3387: 87              ADD     A,A                 
3388: 87              ADD     A,A                 
3389: ED 6A           ADC     HL,HL               
338B: 7D              LD      A,L                 
338C: 32 30 68        LD      ($6830),A           
338F: 12              LD      (DE),A              
3390: 13              INC     DE                  
3391: 0B              DEC     BC                  
3392: 78              LD      A,B                 
3393: B1              OR      C                   
3394: 20 EE           JR      NZ,$3384            ; {}
3396: 11 00 80        LD      DE,$8000            
3399: 21 00 00        LD      HL,$0000            
339C: 01 00 04        LD      BC,$0400            
339F: 7D              LD      A,L                 
33A0: AC              XOR     H                   
33A1: 2F              CPL                         
33A2: 87              ADD     A,A                 
33A3: 87              ADD     A,A                 
33A4: ED 6A           ADC     HL,HL               
33A6: 1A              LD      A,(DE)              
33A7: AD              XOR     L                   
33A8: C2 C0 34        JP      NZ,$34C0            ; {}
33AB: 13              INC     DE                  
33AC: 32 30 68        LD      ($6830),A           
33AF: 0B              DEC     BC                  
33B0: 78              LD      A,B                 
33B1: B1              OR      C                   
33B2: 20 EB           JR      NZ,$339F            ; {}
33B4: 11 00 80        LD      DE,$8000            
33B7: 21 55 55        LD      HL,$5555            
33BA: 01 00 04        LD      BC,$0400            
33BD: 7D              LD      A,L                 
33BE: AC              XOR     H                   
33BF: 2F              CPL                         
33C0: 87              ADD     A,A                 
33C1: 87              ADD     A,A                 
33C2: ED 6A           ADC     HL,HL               
33C4: 7D              LD      A,L                 
33C5: 32 30 68        LD      ($6830),A           
33C8: 12              LD      (DE),A              
33C9: 13              INC     DE                  
33CA: 0B              DEC     BC                  
33CB: 78              LD      A,B                 
33CC: B1              OR      C                   
33CD: 20 EE           JR      NZ,$33BD            ; {}
33CF: 11 00 80        LD      DE,$8000            
33D2: 21 55 55        LD      HL,$5555            
33D5: 01 00 04        LD      BC,$0400            
33D8: 7D              LD      A,L                 
33D9: AC              XOR     H                   
33DA: 2F              CPL                         
33DB: 87              ADD     A,A                 
33DC: 87              ADD     A,A                 
33DD: ED 6A           ADC     HL,HL               
33DF: 1A              LD      A,(DE)              
33E0: AD              XOR     L                   
33E1: C2 C0 34        JP      NZ,$34C0            ; {}
33E4: 13              INC     DE                  
33E5: 32 30 68        LD      ($6830),A           
33E8: 0B              DEC     BC                  
33E9: 78              LD      A,B                 
33EA: B1              OR      C                   
33EB: 20 EB           JR      NZ,$33D8            ; {}
33ED: 11 00 80        LD      DE,$8000            
33F0: 21 AA AA        LD      HL,$AAAA            
33F3: 01 00 04        LD      BC,$0400            
33F6: 7D              LD      A,L                 
33F7: AC              XOR     H                   
33F8: 2F              CPL                         
33F9: 87              ADD     A,A                 
33FA: 87              ADD     A,A                 
33FB: ED 6A           ADC     HL,HL               
33FD: 7D              LD      A,L                 
33FE: 32 30 68        LD      ($6830),A           
3401: 12              LD      (DE),A              
3402: 13              INC     DE                  
3403: 0B              DEC     BC                  
3404: 78              LD      A,B                 
3405: B1              OR      C                   
3406: 20 EE           JR      NZ,$33F6            ; {}
3408: 11 00 80        LD      DE,$8000            
340B: 21 AA AA        LD      HL,$AAAA            
340E: 01 00 04        LD      BC,$0400            
3411: 7D              LD      A,L                 
3412: AC              XOR     H                   
3413: 2F              CPL                         
3414: 87              ADD     A,A                 
3415: 87              ADD     A,A                 
3416: ED 6A           ADC     HL,HL               
3418: 1A              LD      A,(DE)              
3419: AD              XOR     L                   
341A: C2 C0 34        JP      NZ,$34C0            ; {}
341D: 13              INC     DE                  
341E: 32 30 68        LD      ($6830),A           
3421: 0B              DEC     BC                  
3422: 78              LD      A,B                 
3423: B1              OR      C                   
3424: 20 EB           JR      NZ,$3411            ; {}
3426: D9              EXX                         
3427: 05              DEC     B                   
3428: C2 7A 33        JP      NZ,$337A            ; {}
342B: 31 00 84        LD      SP,$8400            
342E: 11 00 84        LD      DE,$8400            
3431: CD 7F 34        CALL    $347F               ; {}
3434: 11 00 88        LD      DE,$8800            
3437: CD 7F 34        CALL    $347F               ; {}
343A: 11 00 90        LD      DE,$9000            
343D: CD 7F 34        CALL    $347F               ; {}
3440: 21 E0 99        LD      HL,$99E0            
3443: 11 00 90        LD      DE,$9000            
3446: 01 20 00        LD      BC,$0020            
3449: ED B0           LDIR                        
344B: 11 00 98        LD      DE,$9800            
344E: CD 7F 34        CALL    $347F               ; {}
3451: 21 00 90        LD      HL,$9000            
3454: 11 E0 99        LD      DE,$99E0            
3457: 01 20 00        LD      BC,$0020            
345A: ED B0           LDIR                        
345C: 31 00 8B        LD      SP,$8B00            
345F: 11 00 80        LD      DE,$8000            
3462: CD 7F 34        CALL    $347F               ; {}
3465: CD 58 39        CALL    $3958               ; {}
3468: 21 81 3B        LD      HL,$3B81            
346B: CD 1B 33        CALL    $331B               ; {}
346E: 32 30 68        LD      ($6830),A           
3471: CD 3C 3A        CALL    $3A3C               ; {}
3474: 3E 07           LD      A,$07               
3476: 32 20 90        LD      ($9020),A           
3479: CD 72 39        CALL    $3972               ; {}
347C: C3 50 35        JP      $3550               ; {}
347F: 06 1E           LD      B,$1E               
3481: 21 00 00        LD      HL,$0000            
3484: C5              PUSH    BC                  
3485: CD 8C 34        CALL    $348C               ; {}
3488: C1              POP     BC                  
3489: 10 F9           DJNZ    $3484               ; {}
348B: C9              RET                         
348C: D5              PUSH    DE                  
348D: E5              PUSH    HL                  
348E: 01 00 04        LD      BC,$0400            
3491: 7D              LD      A,L                 
3492: AC              XOR     H                   
3493: 2F              CPL                         
3494: 87              ADD     A,A                 
3495: 87              ADD     A,A                 
3496: ED 6A           ADC     HL,HL               
3498: 7D              LD      A,L                 
3499: 32 30 68        LD      ($6830),A           
349C: 12              LD      (DE),A              
349D: 13              INC     DE                  
349E: 0B              DEC     BC                  
349F: 78              LD      A,B                 
34A0: B1              OR      C                   
34A1: 20 EE           JR      NZ,$3491            ; {}
34A3: E1              POP     HL                  
34A4: D1              POP     DE                  
34A5: D5              PUSH    DE                  
34A6: 01 00 04        LD      BC,$0400            
34A9: 7D              LD      A,L                 
34AA: AC              XOR     H                   
34AB: 2F              CPL                         
34AC: 87              ADD     A,A                 
34AD: 87              ADD     A,A                 
34AE: ED 6A           ADC     HL,HL               
34B0: 1A              LD      A,(DE)              
34B1: AD              XOR     L                   
34B2: C2 C0 34        JP      NZ,$34C0            ; {}
34B5: 13              INC     DE                  
34B6: 32 30 68        LD      ($6830),A           
34B9: 0B              DEC     BC                  
34BA: 78              LD      A,B                 
34BB: B1              OR      C                   
34BC: 20 EB           JR      NZ,$34A9            ; {}
34BE: D1              POP     DE                  
34BF: C9              RET                         
34C0: 47              LD      B,A                 
34C1: 7A              LD      A,D                 
34C2: 1F              RRA                         
34C3: 1F              RRA                         
34C4: E6 07           AND     $07                 
34C6: FE 04           CP      $04                 
34C8: 38 01           JR      C,$34CB             ; {}
34CA: 3D              DEC     A                   
34CB: FE 05           CP      $05                 
34CD: 38 01           JR      C,$34D0             ; {}
34CF: 3D              DEC     A                   
34D0: 5F              LD      E,A                 
34D1: 78              LD      A,B                 
34D2: 16 15           LD      D,$15               
34D4: E6 0F           AND     $0F                 
34D6: 20 02           JR      NZ,$34DA            ; {}
34D8: 16 11           LD      D,$11               
34DA: 32 30 68        LD      ($6830),A           
34DD: D9              EXX                         
34DE: 21 00 80        LD      HL,$8000            
34E1: 11 01 80        LD      DE,$8001            
34E4: 01 00 04        LD      BC,$0400            
34E7: 36 24           LD      (HL),$24            
34E9: ED B0           LDIR                        
34EB: 36 00           LD      (HL),$00            
34ED: 01 FF 03        LD      BC,$03FF            
34F0: ED B0           LDIR                        
34F2: 32 30 68        LD      ($6830),A           
34F5: D9              EXX                         
34F6: 21 E2 82        LD      HL,$82E2            
34F9: 36 1B           LD      (HL),$1B            
34FB: 3E E0           LD      A,$E0               
34FD: 25              DEC     H                   
34FE: D7              RST     0X10                
34FF: 36 0A           LD      (HL),$0A            
3501: 3E E0           LD      A,$E0               
3503: 25              DEC     H                   
3504: D7              RST     0X10                
3505: 36 16           LD      (HL),$16            
3507: 3E A0           LD      A,$A0               
3509: 25              DEC     H                   
350A: D7              RST     0X10                
350B: 73              LD      (HL),E              
350C: 3E E0           LD      A,$E0               
350E: 25              DEC     H                   
350F: D7              RST     0X10                
3510: 72              LD      (HL),D              
3511: 21 80 93        LD      HL,$9380            
3514: 06 80           LD      B,$80               
3516: 36 F1           LD      (HL),$F1            
3518: 23              INC     HL                  
3519: 10 FB           DJNZ    $3516               ; {}
351B: 32 30 68        LD      ($6830),A           
351E: C3 1B 35        JP      $351B               ; {}
3521: E5              PUSH    HL                  
3522: EB              EX      DE,HL               
3523: 16 10           LD      D,$10               
3525: AF              XOR     A                   
3526: 47              LD      B,A                 
3527: 86              ADD     A,(HL)              
3528: 32 30 68        LD      ($6830),A           
352B: 23              INC     HL                  
352C: 10 F9           DJNZ    $3527               ; {}
352E: 15              DEC     D                   
352F: 20 F6           JR      NZ,$3527            ; {}
3531: EB              EX      DE,HL               
3532: E1              POP     HL                  
3533: B9              CP      C                   
3534: C8              RET     Z                   
3535: 21 8B 3B        LD      HL,$3B8B            
3538: CD 1B 33        CALL    $331B               ; {}
353B: 11 44 82        LD      DE,$8244            
353E: 21 02 91        LD      HL,$9102            
3541: AF              XOR     A                   
3542: ED 6F           RLD                         
3544: 12              LD      (DE),A              
3545: E7              RST     0X20                
3546: AF              XOR     A                   
3547: ED 6F           RLD                         
3549: 12              LD      (DE),A              
354A: 32 30 68        LD      ($6830),A           
354D: C3 4A 35        JP      $354A               ; {}
3550: 21 00 91        LD      HL,$9100            
3553: 36 00           LD      (HL),$00            
3555: 23              INC     HL                  
3556: 36 00           LD      (HL),$00            
3558: 23              INC     HL                  
3559: 36 01           LD      (HL),$01            
355B: AF              XOR     A                   
355C: 32 70 92        LD      ($9270),A           
355F: 3C              INC     A                   
3560: 32 23 68        LD      ($6823),A           
3563: 11 00 00        LD      DE,$0000            
3566: 0E 00           LD      C,$00               
3568: CD 21 35        CALL    $3521               ; {}
356B: 34              INC     (HL)                
356C: 0E 00           LD      C,$00               
356E: CD 21 35        CALL    $3521               ; {}
3571: 34              INC     (HL)                
3572: 0E 00           LD      C,$00               
3574: CD 21 35        CALL    $3521               ; {}
3577: 34              INC     (HL)                
3578: 0E 00           LD      C,$00               
357A: CD 21 35        CALL    $3521               ; {}
357D: 36 FF           LD      (HL),$FF            
357F: 3A 00 91        LD      A,($9100)           
3582: 32 30 68        LD      ($6830),A           
3585: A7              AND     A                   
3586: 28 F7           JR      Z,$357F             ; {}
3588: 3C              INC     A                   
3589: 28 07           JR      Z,$3592             ; {}
358B: 3D              DEC     A                   
358C: 32 02 91        LD      ($9102),A           
358F: C3 35 35        JP      $3535               ; {}
3592: 3A 01 91        LD      A,($9101)           
3595: 32 30 68        LD      ($6830),A           
3598: A7              AND     A                   
3599: 28 F7           JR      Z,$3592             ; {}
359B: 3C              INC     A                   
359C: 28 17           JR      Z,$35B5             ; {}
359E: 3D              DEC     A                   
359F: 32 02 91        LD      ($9102),A           
35A2: C3 35 35        JP      $3535               ; {}
35A5: 05              DEC     B                   
35A6: 05              DEC     B                   
35A7: 05              DEC     B                   
35A8: 05              DEC     B                   
35A9: 30 40           JR      NC,$35EB            ; {}
35AB: 00              NOP                         
35AC: 02              LD      (BC),A              
35AD: DF              RST     0X18                
35AE: 40              LD      B,B                 
35AF: 30 30           JR      NC,$35E1            ; {}
35B1: 03              INC     BC                  
35B2: DF              RST     0X18                
35B3: 10 20           DJNZ    $35D5               ; {}
35B5: 21 8B 3B        LD      HL,$3B8B            
35B8: CD 1B 33        CALL    $331B               ; {}
35BB: CD F4 37        CALL    $37F4               ; {}
35BE: 21 00 91        LD      HL,$9100            
35C1: 06 03           LD      B,$03               
35C3: 36 00           LD      (HL),$00            
35C5: 23              INC     HL                  
35C6: 10 FB           DJNZ    $35C3               ; {}
35C8: 3E 20           LD      A,$20               
35CA: 32 00 90        LD      ($9000),A           
35CD: 21 A5 35        LD      HL,$35A5            
35D0: 11 00 70        LD      DE,$7000            
35D3: 01 04 00        LD      BC,$0004            
35D6: D9              EXX                         
35D7: 3E A1           LD      A,$A1               
35D9: 32 00 71        LD      ($7100),A           
35DC: 32 30 68        LD      ($6830),A           
35DF: CD EC 37        CALL    $37EC               ; {}
35E2: AF              XOR     A                   
35E3: 32 30 68        LD      ($6830),A           
35E6: 32 A0 92        LD      ($92A0),A           
35E9: 3A A0 92        LD      A,($92A0)           
35EC: FE 02           CP      $02                 
35EE: 20 F9           JR      NZ,$35E9            ; {}
35F0: 21 A9 35        LD      HL,$35A9            
35F3: 11 00 70        LD      DE,$7000            
35F6: 01 0C 00        LD      BC,$000C            
35F9: D9              EXX                         
35FA: 3E A8           LD      A,$A8               
35FC: 32 00 71        LD      ($7100),A           
35FF: 32 30 68        LD      ($6830),A           
3602: CD EC 37        CALL    $37EC               ; {}
3605: 32 30 68        LD      ($6830),A           
3608: ED 56           IM      1                   
360A: 21 20 68        LD      HL,$6820            
360D: 36 00           LD      (HL),$00            
360F: 36 01           LD      (HL),$01            
3611: FB              EI                          
3612: CD F2 39        CALL    $39F2               ; {}
3615: AF              XOR     A                   
3616: 32 A0 92        LD      ($92A0),A           
3619: 3A A0 92        LD      A,($92A0)           
361C: E6 08           AND     $08                 
361E: 28 F9           JR      Z,$3619             ; {}
3620: 3A A0 92        LD      A,($92A0)           
3623: 4F              LD      C,A                 
3624: 3A A0 92        LD      A,($92A0)           
3627: B9              CP      C                   
3628: 28 FA           JR      Z,$3624             ; {}
362A: 21 16 91        LD      HL,$9116            
362D: 11 17 91        LD      DE,$9117            
3630: 01 07 00        LD      BC,$0007            
3633: ED B8           LDDR                        
3635: EB              EX      DE,HL               
3636: 11 B5 99        LD      DE,$99B5            
3639: 1A              LD      A,(DE)              
363A: CB 7F           BIT     7,A                 
363C: C2 BA 36        JP      NZ,$36BA            ; {}
363F: 77              LD      (HL),A              
3640: 23              INC     HL                  
3641: B6              OR      (HL)                
3642: 23              INC     HL                  
3643: 2F              CPL                         
3644: A6              AND     (HL)                
3645: 23              INC     HL                  
3646: A6              AND     (HL)                
3647: 77              LD      (HL),A              
3648: 47              LD      B,A                 
3649: 23              INC     HL                  
364A: 13              INC     DE                  
364B: 1A              LD      A,(DE)              
364C: 77              LD      (HL),A              
364D: 23              INC     HL                  
364E: B6              OR      (HL)                
364F: 23              INC     HL                  
3650: 2F              CPL                         
3651: A6              AND     (HL)                
3652: 23              INC     HL                  
3653: A6              AND     (HL)                
3654: 77              LD      (HL),A              
3655: 6F              LD      L,A                 
3656: 60              LD      H,B                 
3657: 06 10           LD      B,$10               
3659: 29              ADD     HL,HL               
365A: DC D6 39        CALL    C,$39D6             ; {}
365D: 10 FA           DJNZ    $3659               ; {}
365F: CD F4 37        CALL    $37F4               ; {}
3662: 2A 72 92        LD      HL,($9272)          
3665: 7C              LD      A,H                 
3666: B5              OR      L                   
3667: 28 09           JR      Z,$3672             ; {}
3669: 2B              DEC     HL                  
366A: 22 72 92        LD      ($9272),HL          
366D: 7C              LD      A,H                 
366E: B5              OR      L                   
366F: CC BB 39        CALL    Z,$39BB             ; {}
3672: 3A 10 91        LD      A,($9110)           
3675: 1F              RRA                         
3676: 30 07           JR      NC,$367F            ; {}
3678: AF              XOR     A                   
3679: 32 71 92        LD      ($9271),A           
367C: C3 20 36        JP      $3620               ; {}
367F: 3A 17 91        LD      A,($9117)           
3682: E6 0F           AND     $0F                 
3684: CA 20 36        JP      Z,$3620             ; {}
3687: 4F              LD      C,A                 
3688: 21 82 37        LD      HL,$3782            
368B: 11 71 92        LD      DE,$9271            
368E: 1A              LD      A,(DE)              
368F: D7              RST     0X10                
3690: 7E              LD      A,(HL)              
3691: B9              CP      C                   
3692: 28 05           JR      Z,$3699             ; {}
3694: AF              XOR     A                   
3695: 12              LD      (DE),A              
3696: C3 20 36        JP      $3620               ; {}
3699: EB              EX      DE,HL               
369A: 34              INC     (HL)                
369B: 13              INC     DE                  
369C: 1A              LD      A,(DE)              
369D: 3C              INC     A                   
369E: C2 20 36        JP      NZ,$3620            ; {}
36A1: CD 58 39        CALL    $3958               ; {}
36A4: CD 72 39        CALL    $3972               ; {}
36A7: 11 98 37        LD      DE,$3798            
36AA: 21 42 80        LD      HL,$8042            
36AD: 06 1C           LD      B,$1C               
36AF: CD 66 37        CALL    $3766               ; {}
36B2: 10 FB           DJNZ    $36AF               ; {}
36B4: 3A B5 99        LD      A,($99B5)           
36B7: 87              ADD     A,A                 
36B8: 30 FA           JR      NC,$36B4            ; {}
36BA: AF              XOR     A                   
36BB: 32 A0 92        LD      ($92A0),A           
36BE: 3A A0 92        LD      A,($92A0)           
36C1: FE 08           CP      $08                 
36C3: 38 F9           JR      C,$36BE             ; {}
36C5: 3A B5 99        LD      A,($99B5)           
36C8: 87              ADD     A,A                 
36C9: D2 20 36        JP      NC,$3620            ; {}
36CC: CD 72 39        CALL    $3972               ; {}
36CF: 21 00 80        LD      HL,$8000            
36D2: 06 10           LD      B,$10               
36D4: 36 28           LD      (HL),$28            
36D6: 23              INC     HL                  
36D7: 36 27           LD      (HL),$27            
36D9: 23              INC     HL                  
36DA: 10 F8           DJNZ    $36D4               ; {}
36DC: 06 10           LD      B,$10               
36DE: 36 2D           LD      (HL),$2D            
36E0: 23              INC     HL                  
36E1: 36 2B           LD      (HL),$2B            
36E3: 23              INC     HL                  
36E4: 10 F8           DJNZ    $36DE               ; {}
36E6: 06 10           LD      B,$10               
36E8: 36 28           LD      (HL),$28            
36EA: 23              INC     HL                  
36EB: 36 2D           LD      (HL),$2D            
36ED: 23              INC     HL                  
36EE: 10 F8           DJNZ    $36E8               ; {}
36F0: 06 10           LD      B,$10               
36F2: 36 27           LD      (HL),$27            
36F4: 23              INC     HL                  
36F5: 36 2B           LD      (HL),$2B            
36F7: 23              INC     HL                  
36F8: 10 F8           DJNZ    $36F2               ; {}
36FA: EB              EX      DE,HL               
36FB: 21 40 80        LD      HL,$8040            
36FE: 01 40 03        LD      BC,$0340            
3701: ED B0           LDIR                        
3703: 21 00 80        LD      HL,$8000            
3706: 01 40 00        LD      BC,$0040            
3709: ED B0           LDIR                        
370B: AF              XOR     A                   
370C: 32 A0 92        LD      ($92A0),A           
370F: 3A A0 92        LD      A,($92A0)           
3712: 87              ADD     A,A                 
3713: 30 FA           JR      NC,$370F            ; {}
3715: 3A B5 99        LD      A,($99B5)           
3718: 87              ADD     A,A                 
3719: 30 FA           JR      NC,$3715            ; {}
371B: F3              DI                          
371C: CD EC 37        CALL    $37EC               ; {}
371F: 3E FE           LD      A,$FE               
3721: 32 A0 92        LD      ($92A0),A           
3724: 3A A0 92        LD      A,($92A0)           
3727: A7              AND     A                   
3728: 20 FA           JR      NZ,$3724            ; {}
372A: 32 30 68        LD      ($6830),A           
372D: 21 80 92        LD      HL,$9280            
3730: 11 00 70        LD      DE,$7000            
3733: 01 08 00        LD      BC,$0008            
3736: D9              EXX                         
3737: 3E E1           LD      A,$E1               
3739: 32 00 71        LD      ($7100),A           
373C: CD EC 37        CALL    $37EC               ; {}
373F: 21 00 70        LD      HL,$7000            
3742: 11 88 92        LD      DE,$9288            
3745: 01 03 00        LD      BC,$0003            
3748: D9              EXX                         
3749: 3E B1           LD      A,$B1               
374B: 32 00 71        LD      ($7100),A           
374E: CD EC 37        CALL    $37EC               ; {}
3751: 3A 88 92        LD      A,($9288)           
3754: FE A1           CP      $A1                 
3756: 30 D5           JR      NC,$372D            ; {}
3758: E6 0F           AND     $0F                 
375A: FE 0A           CP      $0A                 
375C: 30 CF           JR      NC,$372D            ; {}
375E: FB              EI                          
375F: AF              XOR     A                   
3760: 32 10 82        LD      ($8210),A           
3763: C3 D3 02        JP      $02D3               ; {}
3766: CD 74 37        CALL    $3774               ; {}
3769: CD 74 37        CALL    $3774               ; {}
376C: CD 74 37        CALL    $3774               ; {}
376F: 3E 05           LD      A,$05               
3771: C3 10 00        JP      $0010               ; {}
3774: 1A              LD      A,(DE)              
3775: 0E 08           LD      C,$08               
3777: 87              ADD     A,A                 
3778: 30 01           JR      NC,$377B            ; {}
377A: 34              INC     (HL)                
377B: 23              INC     HL                  
377C: 0D              DEC     C                   
377D: 20 F8           JR      NZ,$3777            ; {}
377F: 13              INC     DE                  
3780: 23              INC     HL                  
3781: C9              RET                         
3782: 02              LD      (BC),A              
3783: 02              LD      (BC),A              
3784: 02              LD      (BC),A              
3785: 02              LD      (BC),A              
3786: 02              LD      (BC),A              
3787: 08              EX      AF,AF'              
3788: 08              EX      AF,AF'              
3789: 08              EX      AF,AF'              
378A: 08              EX      AF,AF'              
378B: 08              EX      AF,AF'              
378C: 08              EX      AF,AF'              
378D: 02              LD      (BC),A              
378E: 02              LD      (BC),A              
378F: 02              LD      (BC),A              
3790: 08              EX      AF,AF'              
3791: 08              EX      AF,AF'              
3792: 08              EX      AF,AF'              
3793: 08              EX      AF,AF'              
3794: 08              EX      AF,AF'              
3795: 08              EX      AF,AF'              
3796: 08              EX      AF,AF'              
3797: FF              RST     0X38                
3798: 01 3E 00        LD      BC,$003E            
379B: 7F              LD      A,A                 
379C: 41              LD      B,C                 
379D: 00              NOP                         
379E: 21 41 00        LD      HL,$0041            
37A1: 00              NOP                         
37A2: 41              LD      B,C                 
37A3: 00              NOP                         
37A4: 36 3E           LD      (HL),$3E            
37A6: 00              NOP                         
37A7: 49              LD      C,C                 
37A8: 00              NOP                         
37A9: 03              INC     BC                  
37AA: 49              LD      C,C                 
37AB: 22 03 49        LD      ($4903),HL          
37AE: 41              LD      B,C                 
37AF: 00              NOP                         
37B0: 36 41           LD      (HL),$41            
37B2: 3E 00           LD      A,$00               
37B4: 3E 41           LD      A,$41               
37B6: 3E 00           LD      A,$00               
37B8: 41              LD      B,C                 
37B9: 49              LD      C,C                 
37BA: 7F              LD      A,A                 
37BB: 41              LD      B,C                 
37BC: 49              LD      C,C                 
37BD: 20 7F           JR      NZ,$383E            ; {}
37BF: 49              LD      C,C                 
37C0: 18 00           JR      $37C2               ; {}
37C2: 32 20 40        LD      ($4020),A           
37C5: 00              NOP                         
37C6: 7F              LD      A,A                 
37C7: 40              LD      B,B                 
37C8: 01 00 7F        LD      BC,$7F00            
37CB: 7F              LD      A,A                 
37CC: 3F              CCF                         
37CD: 40              LD      B,B                 
37CE: 21 44 40        LD      HL,$4044            
37D1: 00              NOP                         
37D2: 44              LD      B,H                 
37D3: 00              NOP                         
37D4: 3C              INC     A                   
37D5: 44              LD      B,H                 
37D6: 01 42 3F        LD      BC,$3F42            
37D9: 01 81 00        LD      BC,$0081            
37DC: 01 A5 7F        LD      BC,$7FA5            
37DF: 01 A5 04        LD      BC,$04A5            
37E2: 7F              LD      A,A                 
37E3: 99              SBC     C                   
37E4: 08              EX      AF,AF'              
37E5: 00              NOP                         
37E6: 42              LD      B,D                 
37E7: 10 00           DJNZ    $37E9               ; {}
37E9: 3C              INC     A                   
37EA: 7F              LD      A,A                 
37EB: 00              NOP                         
37EC: 3A 00 71        LD      A,($7100)           
37EF: FE 10           CP      $10                 
37F1: C8              RET     Z                   
37F2: 18 F8           JR      $37EC               ; {}
37F4: 3A 07 68        LD      A,($6807)           
37F7: 1F              RRA                         
37F8: 3C              INC     A                   
37F9: E6 01           AND     $01                 
37FB: 32 83 99        LD      ($9983),A           
37FE: 21 CC 3A        LD      HL,$3ACC            
3801: CF              RST     0X08                
3802: CD 61 3A        CALL    $3A61               ; {}
3805: 3A B5 99        LD      A,($99B5)           
3808: 0E 00           LD      C,$00               
380A: E6 0C           AND     $0C                 
380C: 20 01           JR      NZ,$380F            ; {}
380E: 0C              INC     C                   
380F: 79              LD      A,C                 
3810: 32 07 A0        LD      ($A007),A           
3813: 21 00 68        LD      HL,$6800            
3816: 7E              LD      A,(HL)              
3817: 1F              RRA                         
3818: E6 01           AND     $01                 
381A: 4F              LD      C,A                 
381B: 23              INC     HL                  
381C: 7E              LD      A,(HL)              
381D: E6 02           AND     $02                 
381F: B1              OR      C                   
3820: 32 84 99        LD      ($9984),A           
3823: 21 68 3A        LD      HL,$3A68            
3826: D7              RST     0X10                
3827: 11 2C 82        LD      DE,$822C            
382A: ED A0           LDI                         
382C: 21 E4 3A        LD      HL,$3AE4            
382F: CD 1B 33        CALL    $331B               ; {}
3832: 21 06 68        LD      HL,$6806            
3835: 7E              LD      A,(HL)              
3836: 23              INC     HL                  
3837: 4E              LD      C,(HL)              
3838: CB 19           RR      C                   
383A: 8F              ADC     A,A                 
383B: E6 03           AND     $03                 
383D: 3C              INC     A                   
383E: 32 82 99        LD      ($9982),A           
3841: 3C              INC     A                   
3842: 32 EA 82        LD      ($82EA),A           
3845: 21 EB 3A        LD      HL,$3AEB            
3848: CD 1B 33        CALL    $331B               ; {}
384B: 21 C4 3A        LD      HL,$3AC4            
384E: 11 80 92        LD      DE,$9280            
3851: 01 08 00        LD      BC,$0008            
3854: ED B0           LDIR                        
3856: 21 00 68        LD      HL,$6800            
3859: 06 03           LD      B,$03               
385B: AF              XOR     A                   
385C: 4E              LD      C,(HL)              
385D: CB 19           RR      C                   
385F: 8F              ADC     A,A                 
3860: 23              INC     HL                  
3861: 10 F9           DJNZ    $385C               ; {}
3863: E6 07           AND     $07                 
3865: 28 34           JR      Z,$389B             ; {}
3867: 3D              DEC     A                   
3868: 87              ADD     A,A                 
3869: 87              ADD     A,A                 
386A: 87              ADD     A,A                 
386B: 21 6C 3A        LD      HL,$3A6C            
386E: D7              RST     0X10                
386F: 11 81 92        LD      DE,$9281            
3872: 01 04 00        LD      BC,$0004            
3875: ED B0           LDIR                        
3877: 11 E8 82        LD      DE,$82E8            
387A: ED A0           LDI                         
387C: 11 28 82        LD      DE,$8228            
387F: ED A0           LDI                         
3881: 11 E8 81        LD      DE,$81E8            
3884: ED A0           LDI                         
3886: 11 E8 80        LD      DE,$80E8            
3889: ED A0           LDI                         
388B: 3E 24           LD      A,$24               
388D: 32 08 82        LD      ($8208),A           
3890: 21 F6 3A        LD      HL,$3AF6            
3893: CD 1B 33        CALL    $331B               ; {}
3896: CD 1B 33        CALL    $331B               ; {}
3899: 18 10           JR      $38AB               ; {}
389B: 21 81 92        LD      HL,$9281            
389E: 06 04           LD      B,$04               
38A0: 36 00           LD      (HL),$00            
38A2: 23              INC     HL                  
38A3: 10 FB           DJNZ    $38A0               ; {}
38A5: 21 07 3B        LD      HL,$3B07            
38A8: CD 1B 33        CALL    $331B               ; {}
38AB: 21 03 68        LD      HL,$6803            
38AE: 06 03           LD      B,$03               
38B0: AF              XOR     A                   
38B1: 4E              LD      C,(HL)              
38B2: CB 19           RR      C                   
38B4: 8F              ADC     A,A                 
38B5: 23              INC     HL                  
38B6: 10 F9           DJNZ    $38B1               ; {}
38B8: E6 07           AND     $07                 
38BA: CA 2D 39        JP      Z,$392D             ; {}
38BD: 4F              LD      C,A                 
38BE: 3A 82 99        LD      A,($9982)           
38C1: E6 04           AND     $04                 
38C3: 87              ADD     A,A                 
38C4: 81              ADD     A,C                 
38C5: 87              ADD     A,A                 
38C6: 21 A4 3A        LD      HL,$3AA4            
38C9: D7              RST     0X10                
38CA: 11 80 99        LD      DE,$9980            
38CD: ED A0           LDI                         
38CF: ED A0           LDI                         
38D1: 2B              DEC     HL                  
38D2: 0E 01           LD      C,$01               
38D4: CD DA 38        CALL    $38DA               ; {}
38D7: 2B              DEC     HL                  
38D8: 0E 00           LD      C,$00               
38DA: 7E              LD      A,(HL)              
38DB: 3C              INC     A                   
38DC: CA 3B 39        JP      Z,$393B             ; {}
38DF: 79              LD      A,C                 
38E0: 87              ADD     A,A                 
38E1: E5              PUSH    HL                  
38E2: 21 1D 3B        LD      HL,$3B1D            
38E5: D7              RST     0X10                
38E6: 7E              LD      A,(HL)              
38E7: 23              INC     HL                  
38E8: 66              LD      H,(HL)              
38E9: 6F              LD      L,A                 
38EA: C5              PUSH    BC                  
38EB: CD 1B 33        CALL    $331B               ; {}
38EE: CD 1B 33        CALL    $331B               ; {}
38F1: C1              POP     BC                  
38F2: E1              POP     HL                  
38F3: 7E              LD      A,(HL)              
38F4: E6 7F           AND     $7F                 
38F6: EB              EX      DE,HL               
38F7: 21 F0 81        LD      HL,$81F0            
38FA: 41              LD      B,C                 
38FB: 10 02           DJNZ    $38FF               ; {}
38FD: 23              INC     HL                  
38FE: 23              INC     HL                  
38FF: CD 1E 39        CALL    $391E               ; {}
3902: EB              EX      DE,HL               
3903: 0D              DEC     C                   
3904: C0              RET     NZ                  
3905: EB              EX      DE,HL               
3906: 1A              LD      A,(DE)              
3907: CB 7F           BIT     7,A                 
3909: C2 49 39        JP      NZ,$3949            ; {}
390C: 21 F4 81        LD      HL,$81F4            
390F: CD 1E 39        CALL    $391E               ; {}
3912: D5              PUSH    DE                  
3913: 21 50 3B        LD      HL,$3B50            
3916: CD 1B 33        CALL    $331B               ; {}
3919: CD 1B 33        CALL    $331B               ; {}
391C: E1              POP     HL                  
391D: C9              RET                         
391E: FE 0A           CP      $0A                 
3920: 06 24           LD      B,$24               
3922: 38 04           JR      C,$3928             ; {}
3924: 06 01           LD      B,$01               
3926: D6 0A           SUB     $0A                 
3928: 70              LD      (HL),B              
3929: CB AD           RES     5,L                 
392B: 77              LD      (HL),A              
392C: C9              RET                         
392D: 21 67 3B        LD      HL,$3B67            
3930: CD 1B 33        CALL    $331B               ; {}
3933: 21 80 99        LD      HL,$9980            
3936: 36 FF           LD      (HL),$FF            
3938: 23              INC     HL                  
3939: 36 FF           LD      (HL),$FF            
393B: EB              EX      DE,HL               
393C: 21 32 83        LD      HL,$8332            
393F: 06 16           LD      B,$16               
3941: 36 24           LD      (HL),$24            
3943: 3E E0           LD      A,$E0               
3945: 25              DEC     H                   
3946: D7              RST     0X10                
3947: 10 F8           DJNZ    $3941               ; {}
3949: 21 34 83        LD      HL,$8334            
394C: 06 16           LD      B,$16               
394E: 36 24           LD      (HL),$24            
3950: 3E E0           LD      A,$E0               
3952: 25              DEC     H                   
3953: D7              RST     0X10                
3954: 10 F8           DJNZ    $394E               ; {}
3956: EB              EX      DE,HL               
3957: C9              RET                         
3958: 21 00 80        LD      HL,$8000            
395B: 11 01 80        LD      DE,$8001            
395E: 01 00 04        LD      BC,$0400            
3961: 36 24           LD      (HL),$24            
3963: ED B0           LDIR                        
3965: 36 03           LD      (HL),$03            
3967: 01 FF 03        LD      BC,$03FF            
396A: ED B0           LDIR                        
396C: 3E 07           LD      A,$07               
396E: 32 BE 99        LD      ($99BE),A           
3971: C9              RET                         
3972: 21 80 93        LD      HL,$9380            
3975: 06 80           LD      B,$80               
3977: 36 F1           LD      (HL),$F1            
3979: 23              INC     HL                  
397A: 10 FB           DJNZ    $3977               ; {}
397C: C9              RET                         
397D: 21 E0 99        LD      HL,$99E0            
3980: 11 5E 83        LD      DE,$835E            
3983: 0E 02           LD      C,$02               
3985: 06 01           LD      B,$01               
3987: CD 97 39        CALL    $3997               ; {}
398A: 06 03           LD      B,$03               
398C: CD 97 39        CALL    $3997               ; {}
398F: 06 02           LD      B,$02               
3991: CD 97 39        CALL    $3997               ; {}
3994: 23              INC     HL                  
3995: 06 01           LD      B,$01               
3997: CD AA 39        CALL    $39AA               ; {}
399A: CD A0 39        CALL    $39A0               ; {}
399D: 10 FB           DJNZ    $399A               ; {}
399F: C9              RET                         
39A0: 3E 99           LD      A,$99               
39A2: 96              SUB     (HL)                
39A3: 1F              RRA                         
39A4: 1F              RRA                         
39A5: 1F              RRA                         
39A6: 1F              RRA                         
39A7: CD AE 39        CALL    $39AE               ; {}
39AA: 3E 99           LD      A,$99               
39AC: 96              SUB     (HL)                
39AD: 23              INC     HL                  
39AE: E6 0F           AND     $0F                 
39B0: 12              LD      (DE),A              
39B1: E7              RST     0X20                
39B2: 0D              DEC     C                   
39B3: C0              RET     NZ                  
39B4: 3E 2A           LD      A,$2A               
39B6: 0E 04           LD      C,$04               
39B8: 12              LD      (DE),A              
39B9: E7              RST     0X20                
39BA: C9              RET                         
39BB: 21 5E 83        LD      HL,$835E            
39BE: 06 17           LD      B,$17               
39C0: 11 E0 FF        LD      DE,$FFE0            
39C3: 36 24           LD      (HL),$24            
39C5: 19              ADD     HL,DE               
39C6: 10 FB           DJNZ    $39C3               ; {}
39C8: C9              RET                         
39C9: E5              PUSH    HL                  
39CA: CD 7D 39        CALL    $397D               ; {}
39CD: 21 84 03        LD      HL,$0384            
39D0: 22 72 92        LD      ($9272),HL          
39D3: E1              POP     HL                  
39D4: C1              POP     BC                  
39D5: C9              RET                         
39D6: C5              PUSH    BC                  
39D7: 78              LD      A,B                 
39D8: FE 0F           CP      $0F                 
39DA: 28 ED           JR      Z,$39C9             ; {}
39DC: FE 02           CP      $02                 
39DE: 28 15           JR      Z,$39F5             ; {}
39E0: FE 04           CP      $04                 
39E2: 20 3D           JR      NZ,$3A21            ; {}
39E4: 3A 70 92        LD      A,($9270)           
39E7: D6 01           SUB     $01                 
39E9: 30 02           JR      NC,$39ED            ; {}
39EB: 3E 11           LD      A,$11               
39ED: 32 70 92        LD      ($9270),A           
39F0: 18 0A           JR      $39FC               ; {}
39F2: C5              PUSH    BC                  
39F3: 18 07           JR      $39FC               ; {}
39F5: 3A 70 92        LD      A,($9270)           
39F8: 3C              INC     A                   
39F9: 32 70 92        LD      ($9270),A           
39FC: 3A 70 92        LD      A,($9270)           
39FF: FE 12           CP      $12                 
3A01: 38 01           JR      C,$3A04             ; {}
3A03: AF              XOR     A                   
3A04: 32 70 92        LD      ($9270),A           
3A07: E5              PUSH    HL                  
3A08: 0E 00           LD      C,$00               
3A0A: FE 0A           CP      $0A                 
3A0C: 38 03           JR      C,$3A11             ; {}
3A0E: 0C              INC     C                   
3A0F: D6 0A           SUB     $0A                 
3A11: 21 2E 82        LD      HL,$822E            
3A14: 71              LD      (HL),C              
3A15: 2E 0E           LD      L,$0E               
3A17: 77              LD      (HL),A              
3A18: 21 47 3A        LD      HL,$3A47            
3A1B: CD 1B 33        CALL    $331B               ; {}
3A1E: E1              POP     HL                  
3A1F: C1              POP     BC                  
3A20: C9              RET                         
3A21: 3A 70 92        LD      A,($9270)           
3A24: FE 12           CP      $12                 
3A26: 38 01           JR      C,$3A29             ; {}
3A28: AF              XOR     A                   
3A29: 32 70 92        LD      ($9270),A           
3A2C: EB              EX      DE,HL               
3A2D: CD 3C 3A        CALL    $3A3C               ; {}
3A30: 21 4F 3A        LD      HL,$3A4F            
3A33: D7              RST     0X10                
3A34: 6E              LD      L,(HL)              
3A35: 26 9A           LD      H,$9A               
3A37: 36 01           LD      (HL),$01            
3A39: EB              EX      DE,HL               
3A3A: C1              POP     BC                  
3A3B: C9              RET                         
3A3C: 21 A0 9A        LD      HL,$9AA0            
3A3F: 06 40           LD      B,$40               
3A41: 36 00           LD      (HL),$00            
3A43: 23              INC     HL                  
3A44: 10 FB           DJNZ    $3A41               ; {}
3A46: C9              RET                         
3A47: EE 82           XOR     $82                 
3A49: 05              DEC     B                   
3A4A: 1C              INC     E                   
3A4B: 18 1E           JR      $3A6B               ; {}
3A4D: 17              RLA                         
3A4E: 0D              DEC     C                   
3A4F: A1              AND     C                   
3A50: A2              AND     D                   
3A51: A3              AND     E                   
3A52: A4              AND     H                   
3A53: A7              AND     A                   
3A54: AA              XOR     D                   
3A55: AB              XOR     E                   
3A56: AC              XOR     H                   
3A57: AD              XOR     L                   
3A58: AE              XOR     (HL)                
3A59: AF              XOR     A                   
3A5A: B0              OR      B                   
3A5B: B2              OR      D                   
3A5C: B3              OR      E                   
3A5D: B4              OR      H                   
3A5E: B5              OR      L                   
3A5F: B6              OR      (HL)                
3A60: B9              CP      C                   
3A61: 7E              LD      A,(HL)              
3A62: 23              INC     HL                  
3A63: 66              LD      H,(HL)              
3A64: 6F              LD      L,A                 
3A65: C3 1B 33        JP      $331B               ; {}
3A68: 0B              DEC     BC                  
3A69: 0C              INC     C                   
3A6A: 0D              DEC     C                   
3A6B: 0A              LD      A,(BC)              
3A6C: 04              INC     B                   
3A6D: 01 04 01        LD      BC,$0104            
3A70: 04              INC     B                   
3A71: 1C              INC     E                   
3A72: 01 24 03        LD      BC,$0324            
3A75: 01 03 01        LD      BC,$0103            
3A78: 03              INC     BC                  
3A79: 1C              INC     E                   
3A7A: 01 24 02        LD      BC,$0224            
3A7D: 01 02 01        LD      BC,$0102            
3A80: 02              LD      (BC),A              
3A81: 1C              INC     E                   
3A82: 01 24 02        LD      BC,$0224            
3A85: 03              INC     BC                  
3A86: 02              LD      (BC),A              
3A87: 03              INC     BC                  
3A88: 02              LD      (BC),A              
3A89: 1C              INC     E                   
3A8A: 03              INC     BC                  
3A8B: 1C              INC     E                   
3A8C: 01 03 01        LD      BC,$0103            
3A8F: 03              INC     BC                  
3A90: 01 24 03        LD      BC,$0324            
3A93: 1C              INC     E                   
3A94: 01 02 01        LD      BC,$0102            
3A97: 02              LD      (BC),A              
3A98: 01 24 02        LD      BC,$0224            
3A9B: 1C              INC     E                   
3A9C: 01 01 01        LD      BC,$0101            
3A9F: 01 01 24        LD      BC,$2401            
3AA2: 01 24 FF        LD      BC,$FF24            
3AA5: FF              RST     0X38                
3AA6: 02              LD      (BC),A              
3AA7: 06 02           LD      B,$02               
3AA9: 07              RLCA                        
3AAA: 02              LD      (BC),A              
3AAB: 08              EX      AF,AF'              
3AAC: 03              INC     BC                  
3AAD: 0A              LD      A,(BC)              
3AAE: 03              INC     BC                  
3AAF: 0C              INC     C                   
3AB0: 02              LD      (BC),A              
3AB1: 86              ADD     A,(HL)              
3AB2: 03              INC     BC                  
3AB3: 88              ADC     A,B                 
3AB4: FF              RST     0X38                
3AB5: FF              RST     0X38                
3AB6: 03              INC     BC                  
3AB7: 0A              LD      A,(BC)              
3AB8: 03              INC     BC                  
3AB9: 0C              INC     C                   
3ABA: 03              INC     BC                  
3ABB: 0F              RRCA                        
3ABC: 03              INC     BC                  
3ABD: 8A              ADC     A,D                 
3ABE: 03              INC     BC                  
3ABF: 8C              ADC     A,H                 
3AC0: 03              INC     BC                  
3AC1: 8F              ADC     A,A                 
3AC2: 03              INC     BC                  
3AC3: FF              RST     0X38                
3AC4: 01 01 01        LD      BC,$0101            
3AC7: 01 01 02        LD      BC,$0201            
3ACA: 03              INC     BC                  
3ACB: 00              NOP                         
3ACC: D0              RET     NC                  
3ACD: 3A DA 3A        LD      A,($3ADA)           ; {}
3AD0: E6 82           AND     $82                 
3AD2: 07              RLCA                        
3AD3: 1E 19           LD      E,$19               
3AD5: 1B              DEC     DE                  
3AD6: 12              LD      (DE),A              
3AD7: 10 11           DJNZ    $3AEA               ; {}
3AD9: 1D              DEC     E                   
3ADA: E6 82           AND     $82                 
3ADC: 07              RLCA                        
3ADD: 1D              DEC     E                   
3ADE: 0A              LD      A,(BC)              
3ADF: 0B              DEC     BC                  
3AE0: 15              DEC     D                   
3AE1: 0E 24           LD      C,$24               
3AE3: 24              INC     H                   
3AE4: EC 82 04        CALL    PE,$0482            ; {}
3AE7: 1B              DEC     DE                  
3AE8: 0A              LD      A,(BC)              
3AE9: 17              RLA                         
3AEA: 14              INC     D                   
3AEB: AA              XOR     D                   
3AEC: 82              ADD     A,D                 
3AED: 08              EX      AF,AF'              
3AEE: 0F              RRCA                        
3AEF: 12              LD      (DE),A              
3AF0: 10 11           DJNZ    $3B03               ; {}
3AF2: 1D              DEC     E                   
3AF3: 0E 1B           LD      C,$1B               
3AF5: 1C              INC     E                   
3AF6: C8              RET     Z                   
3AF7: 82              ADD     A,D                 
3AF8: 05              DEC     B                   
3AF9: 24              INC     H                   
3AFA: 0C              INC     C                   
3AFB: 18 12           JR      $3B0F               ; {}
3AFD: 17              RLA                         
3AFE: A8              XOR     B                   
3AFF: 81              ADD     A,C                 
3B00: 06 0C           LD      B,$0C               
3B02: 1B              DEC     DE                  
3B03: 0E 0D           LD      C,$0D               
3B05: 12              LD      (DE),A              
3B06: 1D              DEC     E                   
3B07: E8              RET     PE                  
3B08: 82              ADD     A,D                 
3B09: 12              LD      (DE),A              
3B0A: 0F              RRCA                        
3B0B: 1B              DEC     DE                  
3B0C: 0E 0E           LD      C,$0E               
3B0E: 24              INC     H                   
3B0F: 19              ADD     HL,DE               
3B10: 15              DEC     D                   
3B11: 0A              LD      A,(BC)              
3B12: 22 24 24        LD      ($2424),HL          ; {}
3B15: 24              INC     H                   
3B16: 24              INC     H                   
3B17: 24              INC     H                   
3B18: 24              INC     H                   
3B19: 24              INC     H                   
3B1A: 24              INC     H                   
3B1B: 24              INC     H                   
3B1C: 24              INC     H                   
3B1D: 21 3B 39        LD      HL,$393B            
3B20: 3B              DEC     SP                  
3B21: 30 83           JR      NC,$3AA6            ; {}
3B23: 0A              LD      A,(BC)              
3B24: 01 1C 1D        LD      BC,$1D1C            
3B27: 24              INC     H                   
3B28: 0B              DEC     BC                  
3B29: 18 17           JR      $3B42               ; {}
3B2B: 1E 1C           LD      E,$1C               
3B2D: 24              INC     H                   
3B2E: B0              OR      B                   
3B2F: 81              ADD     A,C                 
3B30: 08              EX      AF,AF'              
3B31: 00              NOP                         
3B32: 00              NOP                         
3B33: 00              NOP                         
3B34: 00              NOP                         
3B35: 24              INC     H                   
3B36: 19              ADD     HL,DE               
3B37: 1D              DEC     E                   
3B38: 1C              INC     E                   
3B39: 32 83 09        LD      ($0983),A           ; {}
3B3C: 02              LD      (BC),A              
3B3D: 17              RLA                         
3B3E: 0D              DEC     C                   
3B3F: 24              INC     H                   
3B40: 0B              DEC     BC                  
3B41: 18 17           JR      $3B5A               ; {}
3B43: 1E 1C           LD      E,$1C               
3B45: B2              OR      D                   
3B46: 81              ADD     A,C                 
3B47: 08              EX      AF,AF'              
3B48: 00              NOP                         
3B49: 00              NOP                         
3B4A: 00              NOP                         
3B4B: 00              NOP                         
3B4C: 24              INC     H                   
3B4D: 19              ADD     HL,DE               
3B4E: 1D              DEC     E                   
3B4F: 1C              INC     E                   
3B50: 34              INC     (HL)                
3B51: 83              ADD     A,E                 
3B52: 09              ADD     HL,BC               
3B53: 0A              LD      A,(BC)              
3B54: 17              RLA                         
3B55: 0D              DEC     C                   
3B56: 24              INC     H                   
3B57: 0E 1F           LD      C,$1F               
3B59: 0E 1B           LD      C,$1B               
3B5B: 22 B4 81        LD      ($81B4),HL          
3B5E: 08              EX      AF,AF'              
3B5F: 00              NOP                         
3B60: 00              NOP                         
3B61: 00              NOP                         
3B62: 00              NOP                         
3B63: 24              INC     H                   
3B64: 19              ADD     HL,DE               
3B65: 1D              DEC     E                   
3B66: 1C              INC     E                   
3B67: 30 83           JR      NC,$3AEC            ; {}
3B69: 16 0B           LD      D,$0B               
3B6B: 18 17           JR      $3B84               ; {}
3B6D: 1E 1C           LD      E,$1C               
3B6F: 24              INC     H                   
3B70: 17              RLA                         
3B71: 18 1D           JR      $3B90               ; {}
3B73: 11 12 17        LD      DE,$1712            
3B76: 10 24           DJNZ    $3B9C               ; {}
3B78: 24              INC     H                   
3B79: 24              INC     H                   
3B7A: 24              INC     H                   
3B7B: 24              INC     H                   
3B7C: 24              INC     H                   
3B7D: 24              INC     H                   
3B7E: 24              INC     H                   
3B7F: 24              INC     H                   
3B80: 24              INC     H                   
3B81: E2 82 07        JP      PO,$0782            ; {}
3B84: 1B              DEC     DE                  
3B85: 0A              LD      A,(BC)              
3B86: 16 24           LD      D,$24               
3B88: 24              INC     H                   
3B89: 18 14           JR      $3B9F               ; {}
3B8B: E4 82 07        CALL    PO,$0782            ; {}
3B8E: 1B              DEC     DE                  
3B8F: 18 16           JR      $3BA7               ; {}
3B91: 24              INC     H                   
3B92: 24              INC     H                   
3B93: 18 14           JR      $3BA9               ; {}
3B95: FF              RST     0X38                
3B96: FF              RST     0X38                
3B97: FF              RST     0X38                
3B98: FF              RST     0X38                
3B99: FF              RST     0X38                
3B9A: FF              RST     0X38                
3B9B: FF              RST     0X38                
3B9C: FF              RST     0X38                
3B9D: FF              RST     0X38                
3B9E: FF              RST     0X38                
3B9F: FF              RST     0X38                
3BA0: FF              RST     0X38                
3BA1: FF              RST     0X38                
3BA2: FF              RST     0X38                
3BA3: FF              RST     0X38                
3BA4: FF              RST     0X38                
3BA5: FF              RST     0X38                
3BA6: FF              RST     0X38                
3BA7: FF              RST     0X38                
3BA8: FF              RST     0X38                
3BA9: FF              RST     0X38                
3BAA: FF              RST     0X38                
3BAB: FF              RST     0X38                
3BAC: FF              RST     0X38                
3BAD: FF              RST     0X38                
3BAE: FF              RST     0X38                
3BAF: FF              RST     0X38                
3BB0: FF              RST     0X38                
3BB1: FF              RST     0X38                
3BB2: FF              RST     0X38                
3BB3: FF              RST     0X38                
3BB4: FF              RST     0X38                
3BB5: FF              RST     0X38                
3BB6: FF              RST     0X38                
3BB7: FF              RST     0X38                
3BB8: FF              RST     0X38                
3BB9: FF              RST     0X38                
3BBA: FF              RST     0X38                
3BBB: FF              RST     0X38                
3BBC: FF              RST     0X38                
3BBD: FF              RST     0X38                
3BBE: FF              RST     0X38                
3BBF: FF              RST     0X38                
3BC0: FF              RST     0X38                
3BC1: FF              RST     0X38                
3BC2: FF              RST     0X38                
3BC3: FF              RST     0X38                
3BC4: FF              RST     0X38                
3BC5: FF              RST     0X38                
3BC6: FF              RST     0X38                
3BC7: FF              RST     0X38                
3BC8: FF              RST     0X38                
3BC9: FF              RST     0X38                
3BCA: FF              RST     0X38                
3BCB: FF              RST     0X38                
3BCC: FF              RST     0X38                
3BCD: FF              RST     0X38                
3BCE: FF              RST     0X38                
3BCF: FF              RST     0X38                
3BD0: FF              RST     0X38                
3BD1: FF              RST     0X38                
3BD2: FF              RST     0X38                
3BD3: FF              RST     0X38                
3BD4: FF              RST     0X38                
3BD5: FF              RST     0X38                
3BD6: FF              RST     0X38                
3BD7: FF              RST     0X38                
3BD8: FF              RST     0X38                
3BD9: FF              RST     0X38                
3BDA: FF              RST     0X38                
3BDB: FF              RST     0X38                
3BDC: FF              RST     0X38                
3BDD: FF              RST     0X38                
3BDE: FF              RST     0X38                
3BDF: FF              RST     0X38                
3BE0: FF              RST     0X38                
3BE1: FF              RST     0X38                
3BE2: FF              RST     0X38                
3BE3: FF              RST     0X38                
3BE4: FF              RST     0X38                
3BE5: FF              RST     0X38                
3BE6: FF              RST     0X38                
3BE7: FF              RST     0X38                
3BE8: FF              RST     0X38                
3BE9: FF              RST     0X38                
3BEA: FF              RST     0X38                
3BEB: FF              RST     0X38                
3BEC: FF              RST     0X38                
3BED: FF              RST     0X38                
3BEE: FF              RST     0X38                
3BEF: FF              RST     0X38                
3BF0: FF              RST     0X38                
3BF1: FF              RST     0X38                
3BF2: FF              RST     0X38                
3BF3: FF              RST     0X38                
3BF4: FF              RST     0X38                
3BF5: FF              RST     0X38                
3BF6: FF              RST     0X38                
3BF7: FF              RST     0X38                
3BF8: FF              RST     0X38                
3BF9: FF              RST     0X38                
3BFA: FF              RST     0X38                
3BFB: FF              RST     0X38                
3BFC: FF              RST     0X38                
3BFD: FF              RST     0X38                
3BFE: FF              RST     0X38                
3BFF: FF              RST     0X38                
3C00: FF              RST     0X38                
3C01: FF              RST     0X38                
3C02: FF              RST     0X38                
3C03: FF              RST     0X38                
3C04: FF              RST     0X38                
3C05: FF              RST     0X38                
3C06: FF              RST     0X38                
3C07: FF              RST     0X38                
3C08: FF              RST     0X38                
3C09: FF              RST     0X38                
3C0A: FF              RST     0X38                
3C0B: FF              RST     0X38                
3C0C: FF              RST     0X38                
3C0D: FF              RST     0X38                
3C0E: FF              RST     0X38                
3C0F: FF              RST     0X38                
3C10: FF              RST     0X38                
3C11: FF              RST     0X38                
3C12: FF              RST     0X38                
3C13: FF              RST     0X38                
3C14: FF              RST     0X38                
3C15: FF              RST     0X38                
3C16: FF              RST     0X38                
3C17: FF              RST     0X38                
3C18: FF              RST     0X38                
3C19: FF              RST     0X38                
3C1A: FF              RST     0X38                
3C1B: FF              RST     0X38                
3C1C: FF              RST     0X38                
3C1D: FF              RST     0X38                
3C1E: FF              RST     0X38                
3C1F: FF              RST     0X38                
3C20: FF              RST     0X38                
3C21: FF              RST     0X38                
3C22: FF              RST     0X38                
3C23: FF              RST     0X38                
3C24: FF              RST     0X38                
3C25: FF              RST     0X38                
3C26: FF              RST     0X38                
3C27: FF              RST     0X38                
3C28: FF              RST     0X38                
3C29: FF              RST     0X38                
3C2A: FF              RST     0X38                
3C2B: FF              RST     0X38                
3C2C: FF              RST     0X38                
3C2D: FF              RST     0X38                
3C2E: FF              RST     0X38                
3C2F: FF              RST     0X38                
3C30: FF              RST     0X38                
3C31: FF              RST     0X38                
3C32: FF              RST     0X38                
3C33: FF              RST     0X38                
3C34: FF              RST     0X38                
3C35: FF              RST     0X38                
3C36: FF              RST     0X38                
3C37: FF              RST     0X38                
3C38: FF              RST     0X38                
3C39: FF              RST     0X38                
3C3A: FF              RST     0X38                
3C3B: FF              RST     0X38                
3C3C: FF              RST     0X38                
3C3D: FF              RST     0X38                
3C3E: FF              RST     0X38                
3C3F: FF              RST     0X38                
3C40: FF              RST     0X38                
3C41: FF              RST     0X38                
3C42: FF              RST     0X38                
3C43: FF              RST     0X38                
3C44: FF              RST     0X38                
3C45: FF              RST     0X38                
3C46: FF              RST     0X38                
3C47: FF              RST     0X38                
3C48: FF              RST     0X38                
3C49: FF              RST     0X38                
3C4A: FF              RST     0X38                
3C4B: FF              RST     0X38                
3C4C: FF              RST     0X38                
3C4D: FF              RST     0X38                
3C4E: FF              RST     0X38                
3C4F: FF              RST     0X38                
3C50: FF              RST     0X38                
3C51: FF              RST     0X38                
3C52: FF              RST     0X38                
3C53: FF              RST     0X38                
3C54: FF              RST     0X38                
3C55: FF              RST     0X38                
3C56: FF              RST     0X38                
3C57: FF              RST     0X38                
3C58: FF              RST     0X38                
3C59: FF              RST     0X38                
3C5A: FF              RST     0X38                
3C5B: FF              RST     0X38                
3C5C: FF              RST     0X38                
3C5D: FF              RST     0X38                
3C5E: FF              RST     0X38                
3C5F: FF              RST     0X38                
3C60: FF              RST     0X38                
3C61: FF              RST     0X38                
3C62: FF              RST     0X38                
3C63: FF              RST     0X38                
3C64: FF              RST     0X38                
3C65: FF              RST     0X38                
3C66: FF              RST     0X38                
3C67: FF              RST     0X38                
3C68: FF              RST     0X38                
3C69: FF              RST     0X38                
3C6A: FF              RST     0X38                
3C6B: FF              RST     0X38                
3C6C: FF              RST     0X38                
3C6D: FF              RST     0X38                
3C6E: FF              RST     0X38                
3C6F: FF              RST     0X38                
3C70: FF              RST     0X38                
3C71: FF              RST     0X38                
3C72: FF              RST     0X38                
3C73: FF              RST     0X38                
3C74: FF              RST     0X38                
3C75: FF              RST     0X38                
3C76: FF              RST     0X38                
3C77: FF              RST     0X38                
3C78: FF              RST     0X38                
3C79: FF              RST     0X38                
3C7A: FF              RST     0X38                
3C7B: FF              RST     0X38                
3C7C: FF              RST     0X38                
3C7D: FF              RST     0X38                
3C7E: FF              RST     0X38                
3C7F: FF              RST     0X38                
3C80: FF              RST     0X38                
3C81: FF              RST     0X38                
3C82: FF              RST     0X38                
3C83: FF              RST     0X38                
3C84: FF              RST     0X38                
3C85: FF              RST     0X38                
3C86: FF              RST     0X38                
3C87: FF              RST     0X38                
3C88: FF              RST     0X38                
3C89: FF              RST     0X38                
3C8A: FF              RST     0X38                
3C8B: FF              RST     0X38                
3C8C: FF              RST     0X38                
3C8D: FF              RST     0X38                
3C8E: FF              RST     0X38                
3C8F: FF              RST     0X38                
3C90: FF              RST     0X38                
3C91: FF              RST     0X38                
3C92: FF              RST     0X38                
3C93: FF              RST     0X38                
3C94: FF              RST     0X38                
3C95: FF              RST     0X38                
3C96: FF              RST     0X38                
3C97: FF              RST     0X38                
3C98: FF              RST     0X38                
3C99: FF              RST     0X38                
3C9A: FF              RST     0X38                
3C9B: FF              RST     0X38                
3C9C: FF              RST     0X38                
3C9D: FF              RST     0X38                
3C9E: FF              RST     0X38                
3C9F: FF              RST     0X38                
3CA0: FF              RST     0X38                
3CA1: FF              RST     0X38                
3CA2: FF              RST     0X38                
3CA3: FF              RST     0X38                
3CA4: FF              RST     0X38                
3CA5: FF              RST     0X38                
3CA6: FF              RST     0X38                
3CA7: FF              RST     0X38                
3CA8: FF              RST     0X38                
3CA9: FF              RST     0X38                
3CAA: FF              RST     0X38                
3CAB: FF              RST     0X38                
3CAC: FF              RST     0X38                
3CAD: FF              RST     0X38                
3CAE: FF              RST     0X38                
3CAF: FF              RST     0X38                
3CB0: FF              RST     0X38                
3CB1: FF              RST     0X38                
3CB2: FF              RST     0X38                
3CB3: FF              RST     0X38                
3CB4: FF              RST     0X38                
3CB5: FF              RST     0X38                
3CB6: FF              RST     0X38                
3CB7: FF              RST     0X38                
3CB8: FF              RST     0X38                
3CB9: FF              RST     0X38                
3CBA: FF              RST     0X38                
3CBB: FF              RST     0X38                
3CBC: FF              RST     0X38                
3CBD: FF              RST     0X38                
3CBE: FF              RST     0X38                
3CBF: FF              RST     0X38                
3CC0: FF              RST     0X38                
3CC1: FF              RST     0X38                
3CC2: FF              RST     0X38                
3CC3: FF              RST     0X38                
3CC4: FF              RST     0X38                
3CC5: FF              RST     0X38                
3CC6: FF              RST     0X38                
3CC7: FF              RST     0X38                
3CC8: FF              RST     0X38                
3CC9: FF              RST     0X38                
3CCA: FF              RST     0X38                
3CCB: FF              RST     0X38                
3CCC: FF              RST     0X38                
3CCD: FF              RST     0X38                
3CCE: FF              RST     0X38                
3CCF: FF              RST     0X38                
3CD0: FF              RST     0X38                
3CD1: FF              RST     0X38                
3CD2: FF              RST     0X38                
3CD3: FF              RST     0X38                
3CD4: FF              RST     0X38                
3CD5: FF              RST     0X38                
3CD6: FF              RST     0X38                
3CD7: FF              RST     0X38                
3CD8: FF              RST     0X38                
3CD9: FF              RST     0X38                
3CDA: FF              RST     0X38                
3CDB: FF              RST     0X38                
3CDC: FF              RST     0X38                
3CDD: FF              RST     0X38                
3CDE: FF              RST     0X38                
3CDF: FF              RST     0X38                
3CE0: FF              RST     0X38                
3CE1: FF              RST     0X38                
3CE2: FF              RST     0X38                
3CE3: FF              RST     0X38                
3CE4: FF              RST     0X38                
3CE5: FF              RST     0X38                
3CE6: FF              RST     0X38                
3CE7: FF              RST     0X38                
3CE8: FF              RST     0X38                
3CE9: FF              RST     0X38                
3CEA: FF              RST     0X38                
3CEB: FF              RST     0X38                
3CEC: FF              RST     0X38                
3CED: FF              RST     0X38                
3CEE: FF              RST     0X38                
3CEF: FF              RST     0X38                
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
3D00: FF              RST     0X38                
3D01: FF              RST     0X38                
3D02: FF              RST     0X38                
3D03: FF              RST     0X38                
3D04: FF              RST     0X38                
3D05: FF              RST     0X38                
3D06: FF              RST     0X38                
3D07: FF              RST     0X38                
3D08: FF              RST     0X38                
3D09: FF              RST     0X38                
3D0A: FF              RST     0X38                
3D0B: FF              RST     0X38                
3D0C: FF              RST     0X38                
3D0D: FF              RST     0X38                
3D0E: FF              RST     0X38                
3D0F: FF              RST     0X38                
3D10: FF              RST     0X38                
3D11: FF              RST     0X38                
3D12: FF              RST     0X38                
3D13: FF              RST     0X38                
3D14: FF              RST     0X38                
3D15: FF              RST     0X38                
3D16: FF              RST     0X38                
3D17: FF              RST     0X38                
3D18: FF              RST     0X38                
3D19: FF              RST     0X38                
3D1A: FF              RST     0X38                
3D1B: FF              RST     0X38                
3D1C: FF              RST     0X38                
3D1D: FF              RST     0X38                
3D1E: FF              RST     0X38                
3D1F: FF              RST     0X38                
3D20: FF              RST     0X38                
3D21: FF              RST     0X38                
3D22: FF              RST     0X38                
3D23: FF              RST     0X38                
3D24: FF              RST     0X38                
3D25: FF              RST     0X38                
3D26: FF              RST     0X38                
3D27: FF              RST     0X38                
3D28: FF              RST     0X38                
3D29: FF              RST     0X38                
3D2A: FF              RST     0X38                
3D2B: FF              RST     0X38                
3D2C: FF              RST     0X38                
3D2D: FF              RST     0X38                
3D2E: FF              RST     0X38                
3D2F: FF              RST     0X38                
3D30: FF              RST     0X38                
3D31: FF              RST     0X38                
3D32: FF              RST     0X38                
3D33: FF              RST     0X38                
3D34: FF              RST     0X38                
3D35: FF              RST     0X38                
3D36: FF              RST     0X38                
3D37: FF              RST     0X38                
3D38: FF              RST     0X38                
3D39: FF              RST     0X38                
3D3A: FF              RST     0X38                
3D3B: FF              RST     0X38                
3D3C: FF              RST     0X38                
3D3D: FF              RST     0X38                
3D3E: FF              RST     0X38                
3D3F: FF              RST     0X38                
3D40: FF              RST     0X38                
3D41: FF              RST     0X38                
3D42: FF              RST     0X38                
3D43: FF              RST     0X38                
3D44: FF              RST     0X38                
3D45: FF              RST     0X38                
3D46: FF              RST     0X38                
3D47: FF              RST     0X38                
3D48: FF              RST     0X38                
3D49: FF              RST     0X38                
3D4A: FF              RST     0X38                
3D4B: FF              RST     0X38                
3D4C: FF              RST     0X38                
3D4D: FF              RST     0X38                
3D4E: FF              RST     0X38                
3D4F: FF              RST     0X38                
3D50: FF              RST     0X38                
3D51: FF              RST     0X38                
3D52: FF              RST     0X38                
3D53: FF              RST     0X38                
3D54: FF              RST     0X38                
3D55: FF              RST     0X38                
3D56: FF              RST     0X38                
3D57: FF              RST     0X38                
3D58: FF              RST     0X38                
3D59: FF              RST     0X38                
3D5A: FF              RST     0X38                
3D5B: FF              RST     0X38                
3D5C: FF              RST     0X38                
3D5D: FF              RST     0X38                
3D5E: FF              RST     0X38                
3D5F: FF              RST     0X38                
3D60: FF              RST     0X38                
3D61: FF              RST     0X38                
3D62: FF              RST     0X38                
3D63: FF              RST     0X38                
3D64: FF              RST     0X38                
3D65: FF              RST     0X38                
3D66: FF              RST     0X38                
3D67: FF              RST     0X38                
3D68: FF              RST     0X38                
3D69: FF              RST     0X38                
3D6A: FF              RST     0X38                
3D6B: FF              RST     0X38                
3D6C: FF              RST     0X38                
3D6D: FF              RST     0X38                
3D6E: FF              RST     0X38                
3D6F: FF              RST     0X38                
3D70: FF              RST     0X38                
3D71: FF              RST     0X38                
3D72: FF              RST     0X38                
3D73: FF              RST     0X38                
3D74: FF              RST     0X38                
3D75: FF              RST     0X38                
3D76: FF              RST     0X38                
3D77: FF              RST     0X38                
3D78: FF              RST     0X38                
3D79: FF              RST     0X38                
3D7A: FF              RST     0X38                
3D7B: FF              RST     0X38                
3D7C: FF              RST     0X38                
3D7D: FF              RST     0X38                
3D7E: FF              RST     0X38                
3D7F: FF              RST     0X38                
3D80: FF              RST     0X38                
3D81: FF              RST     0X38                
3D82: FF              RST     0X38                
3D83: FF              RST     0X38                
3D84: FF              RST     0X38                
3D85: FF              RST     0X38                
3D86: FF              RST     0X38                
3D87: FF              RST     0X38                
3D88: FF              RST     0X38                
3D89: FF              RST     0X38                
3D8A: FF              RST     0X38                
3D8B: FF              RST     0X38                
3D8C: FF              RST     0X38                
3D8D: FF              RST     0X38                
3D8E: FF              RST     0X38                
3D8F: FF              RST     0X38                
3D90: FF              RST     0X38                
3D91: FF              RST     0X38                
3D92: FF              RST     0X38                
3D93: FF              RST     0X38                
3D94: FF              RST     0X38                
3D95: FF              RST     0X38                
3D96: FF              RST     0X38                
3D97: FF              RST     0X38                
3D98: FF              RST     0X38                
3D99: FF              RST     0X38                
3D9A: FF              RST     0X38                
3D9B: FF              RST     0X38                
3D9C: FF              RST     0X38                
3D9D: FF              RST     0X38                
3D9E: FF              RST     0X38                
3D9F: FF              RST     0X38                
3DA0: FF              RST     0X38                
3DA1: FF              RST     0X38                
3DA2: FF              RST     0X38                
3DA3: FF              RST     0X38                
3DA4: FF              RST     0X38                
3DA5: FF              RST     0X38                
3DA6: FF              RST     0X38                
3DA7: FF              RST     0X38                
3DA8: FF              RST     0X38                
3DA9: FF              RST     0X38                
3DAA: FF              RST     0X38                
3DAB: FF              RST     0X38                
3DAC: FF              RST     0X38                
3DAD: FF              RST     0X38                
3DAE: FF              RST     0X38                
3DAF: FF              RST     0X38                
3DB0: FF              RST     0X38                
3DB1: FF              RST     0X38                
3DB2: FF              RST     0X38                
3DB3: FF              RST     0X38                
3DB4: FF              RST     0X38                
3DB5: FF              RST     0X38                
3DB6: FF              RST     0X38                
3DB7: FF              RST     0X38                
3DB8: FF              RST     0X38                
3DB9: FF              RST     0X38                
3DBA: FF              RST     0X38                
3DBB: FF              RST     0X38                
3DBC: FF              RST     0X38                
3DBD: FF              RST     0X38                
3DBE: FF              RST     0X38                
3DBF: FF              RST     0X38                
3DC0: FF              RST     0X38                
3DC1: FF              RST     0X38                
3DC2: FF              RST     0X38                
3DC3: FF              RST     0X38                
3DC4: FF              RST     0X38                
3DC5: FF              RST     0X38                
3DC6: FF              RST     0X38                
3DC7: FF              RST     0X38                
3DC8: FF              RST     0X38                
3DC9: FF              RST     0X38                
3DCA: FF              RST     0X38                
3DCB: FF              RST     0X38                
3DCC: FF              RST     0X38                
3DCD: FF              RST     0X38                
3DCE: FF              RST     0X38                
3DCF: FF              RST     0X38                
3DD0: FF              RST     0X38                
3DD1: FF              RST     0X38                
3DD2: FF              RST     0X38                
3DD3: FF              RST     0X38                
3DD4: FF              RST     0X38                
3DD5: FF              RST     0X38                
3DD6: FF              RST     0X38                
3DD7: FF              RST     0X38                
3DD8: FF              RST     0X38                
3DD9: FF              RST     0X38                
3DDA: FF              RST     0X38                
3DDB: FF              RST     0X38                
3DDC: FF              RST     0X38                
3DDD: FF              RST     0X38                
3DDE: FF              RST     0X38                
3DDF: FF              RST     0X38                
3DE0: FF              RST     0X38                
3DE1: FF              RST     0X38                
3DE2: FF              RST     0X38                
3DE3: FF              RST     0X38                
3DE4: FF              RST     0X38                
3DE5: FF              RST     0X38                
3DE6: FF              RST     0X38                
3DE7: FF              RST     0X38                
3DE8: FF              RST     0X38                
3DE9: FF              RST     0X38                
3DEA: FF              RST     0X38                
3DEB: FF              RST     0X38                
3DEC: FF              RST     0X38                
3DED: FF              RST     0X38                
3DEE: FF              RST     0X38                
3DEF: FF              RST     0X38                
3DF0: FF              RST     0X38                
3DF1: FF              RST     0X38                
3DF2: FF              RST     0X38                
3DF3: FF              RST     0X38                
3DF4: FF              RST     0X38                
3DF5: FF              RST     0X38                
3DF6: FF              RST     0X38                
3DF7: FF              RST     0X38                
3DF8: FF              RST     0X38                
3DF9: FF              RST     0X38                
3DFA: FF              RST     0X38                
3DFB: FF              RST     0X38                
3DFC: FF              RST     0X38                
3DFD: FF              RST     0X38                
3DFE: FF              RST     0X38                
3DFF: FF              RST     0X38                
3E00: FF              RST     0X38                
3E01: FF              RST     0X38                
3E02: FF              RST     0X38                
3E03: FF              RST     0X38                
3E04: FF              RST     0X38                
3E05: FF              RST     0X38                
3E06: FF              RST     0X38                
3E07: FF              RST     0X38                
3E08: FF              RST     0X38                
3E09: FF              RST     0X38                
3E0A: FF              RST     0X38                
3E0B: FF              RST     0X38                
3E0C: FF              RST     0X38                
3E0D: FF              RST     0X38                
3E0E: FF              RST     0X38                
3E0F: FF              RST     0X38                
3E10: FF              RST     0X38                
3E11: FF              RST     0X38                
3E12: FF              RST     0X38                
3E13: FF              RST     0X38                
3E14: FF              RST     0X38                
3E15: FF              RST     0X38                
3E16: FF              RST     0X38                
3E17: FF              RST     0X38                
3E18: FF              RST     0X38                
3E19: FF              RST     0X38                
3E1A: FF              RST     0X38                
3E1B: FF              RST     0X38                
3E1C: FF              RST     0X38                
3E1D: FF              RST     0X38                
3E1E: FF              RST     0X38                
3E1F: FF              RST     0X38                
3E20: FF              RST     0X38                
3E21: FF              RST     0X38                
3E22: FF              RST     0X38                
3E23: FF              RST     0X38                
3E24: FF              RST     0X38                
3E25: FF              RST     0X38                
3E26: FF              RST     0X38                
3E27: FF              RST     0X38                
3E28: FF              RST     0X38                
3E29: FF              RST     0X38                
3E2A: FF              RST     0X38                
3E2B: FF              RST     0X38                
3E2C: FF              RST     0X38                
3E2D: FF              RST     0X38                
3E2E: FF              RST     0X38                
3E2F: FF              RST     0X38                
3E30: FF              RST     0X38                
3E31: FF              RST     0X38                
3E32: FF              RST     0X38                
3E33: FF              RST     0X38                
3E34: FF              RST     0X38                
3E35: FF              RST     0X38                
3E36: FF              RST     0X38                
3E37: FF              RST     0X38                
3E38: FF              RST     0X38                
3E39: FF              RST     0X38                
3E3A: FF              RST     0X38                
3E3B: FF              RST     0X38                
3E3C: FF              RST     0X38                
3E3D: FF              RST     0X38                
3E3E: FF              RST     0X38                
3E3F: FF              RST     0X38                
3E40: FF              RST     0X38                
3E41: FF              RST     0X38                
3E42: FF              RST     0X38                
3E43: FF              RST     0X38                
3E44: FF              RST     0X38                
3E45: FF              RST     0X38                
3E46: FF              RST     0X38                
3E47: FF              RST     0X38                
3E48: FF              RST     0X38                
3E49: FF              RST     0X38                
3E4A: FF              RST     0X38                
3E4B: FF              RST     0X38                
3E4C: FF              RST     0X38                
3E4D: FF              RST     0X38                
3E4E: FF              RST     0X38                
3E4F: FF              RST     0X38                
3E50: FF              RST     0X38                
3E51: FF              RST     0X38                
3E52: FF              RST     0X38                
3E53: FF              RST     0X38                
3E54: FF              RST     0X38                
3E55: FF              RST     0X38                
3E56: FF              RST     0X38                
3E57: FF              RST     0X38                
3E58: FF              RST     0X38                
3E59: FF              RST     0X38                
3E5A: FF              RST     0X38                
3E5B: FF              RST     0X38                
3E5C: FF              RST     0X38                
3E5D: FF              RST     0X38                
3E5E: FF              RST     0X38                
3E5F: FF              RST     0X38                
3E60: FF              RST     0X38                
3E61: FF              RST     0X38                
3E62: FF              RST     0X38                
3E63: FF              RST     0X38                
3E64: FF              RST     0X38                
3E65: FF              RST     0X38                
3E66: FF              RST     0X38                
3E67: FF              RST     0X38                
3E68: FF              RST     0X38                
3E69: FF              RST     0X38                
3E6A: FF              RST     0X38                
3E6B: FF              RST     0X38                
3E6C: FF              RST     0X38                
3E6D: FF              RST     0X38                
3E6E: FF              RST     0X38                
3E6F: FF              RST     0X38                
3E70: FF              RST     0X38                
3E71: FF              RST     0X38                
3E72: FF              RST     0X38                
3E73: FF              RST     0X38                
3E74: FF              RST     0X38                
3E75: FF              RST     0X38                
3E76: FF              RST     0X38                
3E77: FF              RST     0X38                
3E78: FF              RST     0X38                
3E79: FF              RST     0X38                
3E7A: FF              RST     0X38                
3E7B: FF              RST     0X38                
3E7C: FF              RST     0X38                
3E7D: FF              RST     0X38                
3E7E: FF              RST     0X38                
3E7F: FF              RST     0X38                
3E80: FF              RST     0X38                
3E81: FF              RST     0X38                
3E82: FF              RST     0X38                
3E83: FF              RST     0X38                
3E84: FF              RST     0X38                
3E85: FF              RST     0X38                
3E86: FF              RST     0X38                
3E87: FF              RST     0X38                
3E88: FF              RST     0X38                
3E89: FF              RST     0X38                
3E8A: FF              RST     0X38                
3E8B: FF              RST     0X38                
3E8C: FF              RST     0X38                
3E8D: FF              RST     0X38                
3E8E: FF              RST     0X38                
3E8F: FF              RST     0X38                
3E90: FF              RST     0X38                
3E91: FF              RST     0X38                
3E92: FF              RST     0X38                
3E93: FF              RST     0X38                
3E94: FF              RST     0X38                
3E95: FF              RST     0X38                
3E96: FF              RST     0X38                
3E97: FF              RST     0X38                
3E98: FF              RST     0X38                
3E99: FF              RST     0X38                
3E9A: FF              RST     0X38                
3E9B: FF              RST     0X38                
3E9C: FF              RST     0X38                
3E9D: FF              RST     0X38                
3E9E: FF              RST     0X38                
3E9F: FF              RST     0X38                
3EA0: FF              RST     0X38                
3EA1: FF              RST     0X38                
3EA2: FF              RST     0X38                
3EA3: FF              RST     0X38                
3EA4: FF              RST     0X38                
3EA5: FF              RST     0X38                
3EA6: FF              RST     0X38                
3EA7: FF              RST     0X38                
3EA8: FF              RST     0X38                
3EA9: FF              RST     0X38                
3EAA: FF              RST     0X38                
3EAB: FF              RST     0X38                
3EAC: FF              RST     0X38                
3EAD: FF              RST     0X38                
3EAE: FF              RST     0X38                
3EAF: FF              RST     0X38                
3EB0: FF              RST     0X38                
3EB1: FF              RST     0X38                
3EB2: FF              RST     0X38                
3EB3: FF              RST     0X38                
3EB4: FF              RST     0X38                
3EB5: FF              RST     0X38                
3EB6: FF              RST     0X38                
3EB7: FF              RST     0X38                
3EB8: FF              RST     0X38                
3EB9: FF              RST     0X38                
3EBA: FF              RST     0X38                
3EBB: FF              RST     0X38                
3EBC: FF              RST     0X38                
3EBD: FF              RST     0X38                
3EBE: FF              RST     0X38                
3EBF: FF              RST     0X38                
3EC0: FF              RST     0X38                
3EC1: FF              RST     0X38                
3EC2: FF              RST     0X38                
3EC3: FF              RST     0X38                
3EC4: FF              RST     0X38                
3EC5: FF              RST     0X38                
3EC6: FF              RST     0X38                
3EC7: FF              RST     0X38                
3EC8: FF              RST     0X38                
3EC9: FF              RST     0X38                
3ECA: FF              RST     0X38                
3ECB: FF              RST     0X38                
3ECC: FF              RST     0X38                
3ECD: FF              RST     0X38                
3ECE: FF              RST     0X38                
3ECF: FF              RST     0X38                
3ED0: FF              RST     0X38                
3ED1: FF              RST     0X38                
3ED2: FF              RST     0X38                
3ED3: FF              RST     0X38                
3ED4: FF              RST     0X38                
3ED5: FF              RST     0X38                
3ED6: FF              RST     0X38                
3ED7: FF              RST     0X38                
3ED8: FF              RST     0X38                
3ED9: FF              RST     0X38                
3EDA: FF              RST     0X38                
3EDB: FF              RST     0X38                
3EDC: FF              RST     0X38                
3EDD: FF              RST     0X38                
3EDE: FF              RST     0X38                
3EDF: FF              RST     0X38                
3EE0: FF              RST     0X38                
3EE1: FF              RST     0X38                
3EE2: FF              RST     0X38                
3EE3: FF              RST     0X38                
3EE4: FF              RST     0X38                
3EE5: FF              RST     0X38                
3EE6: FF              RST     0X38                
3EE7: FF              RST     0X38                
3EE8: FF              RST     0X38                
3EE9: FF              RST     0X38                
3EEA: FF              RST     0X38                
3EEB: FF              RST     0X38                
3EEC: FF              RST     0X38                
3EED: FF              RST     0X38                
3EEE: FF              RST     0X38                
3EEF: FF              RST     0X38                
3EF0: FF              RST     0X38                
3EF1: FF              RST     0X38                
3EF2: FF              RST     0X38                
3EF3: FF              RST     0X38                
3EF4: FF              RST     0X38                
3EF5: FF              RST     0X38                
3EF6: FF              RST     0X38                
3EF7: FF              RST     0X38                
3EF8: FF              RST     0X38                
3EF9: FF              RST     0X38                
3EFA: FF              RST     0X38                
3EFB: FF              RST     0X38                
3EFC: FF              RST     0X38                
3EFD: FF              RST     0X38                
3EFE: FF              RST     0X38                
3EFF: FF              RST     0X38                
3F00: FF              RST     0X38                
3F01: FF              RST     0X38                
3F02: FF              RST     0X38                
3F03: FF              RST     0X38                
3F04: FF              RST     0X38                
3F05: FF              RST     0X38                
3F06: FF              RST     0X38                
3F07: FF              RST     0X38                
3F08: FF              RST     0X38                
3F09: FF              RST     0X38                
3F0A: FF              RST     0X38                
3F0B: FF              RST     0X38                
3F0C: FF              RST     0X38                
3F0D: FF              RST     0X38                
3F0E: FF              RST     0X38                
3F0F: FF              RST     0X38                
3F10: FF              RST     0X38                
3F11: FF              RST     0X38                
3F12: FF              RST     0X38                
3F13: FF              RST     0X38                
3F14: FF              RST     0X38                
3F15: FF              RST     0X38                
3F16: FF              RST     0X38                
3F17: FF              RST     0X38                
3F18: FF              RST     0X38                
3F19: FF              RST     0X38                
3F1A: FF              RST     0X38                
3F1B: FF              RST     0X38                
3F1C: FF              RST     0X38                
3F1D: FF              RST     0X38                
3F1E: FF              RST     0X38                
3F1F: FF              RST     0X38                
3F20: FF              RST     0X38                
3F21: FF              RST     0X38                
3F22: FF              RST     0X38                
3F23: FF              RST     0X38                
3F24: FF              RST     0X38                
3F25: FF              RST     0X38                
3F26: FF              RST     0X38                
3F27: FF              RST     0X38                
3F28: FF              RST     0X38                
3F29: FF              RST     0X38                
3F2A: FF              RST     0X38                
3F2B: FF              RST     0X38                
3F2C: FF              RST     0X38                
3F2D: FF              RST     0X38                
3F2E: FF              RST     0X38                
3F2F: FF              RST     0X38                
3F30: FF              RST     0X38                
3F31: FF              RST     0X38                
3F32: FF              RST     0X38                
3F33: FF              RST     0X38                
3F34: FF              RST     0X38                
3F35: FF              RST     0X38                
3F36: FF              RST     0X38                
3F37: FF              RST     0X38                
3F38: FF              RST     0X38                
3F39: FF              RST     0X38                
3F3A: FF              RST     0X38                
3F3B: FF              RST     0X38                
3F3C: FF              RST     0X38                
3F3D: FF              RST     0X38                
3F3E: FF              RST     0X38                
3F3F: FF              RST     0X38                
3F40: FF              RST     0X38                
3F41: FF              RST     0X38                
3F42: FF              RST     0X38                
3F43: FF              RST     0X38                
3F44: FF              RST     0X38                
3F45: FF              RST     0X38                
3F46: FF              RST     0X38                
3F47: FF              RST     0X38                
3F48: FF              RST     0X38                
3F49: FF              RST     0X38                
3F4A: FF              RST     0X38                
3F4B: FF              RST     0X38                
3F4C: FF              RST     0X38                
3F4D: FF              RST     0X38                
3F4E: FF              RST     0X38                
3F4F: FF              RST     0X38                
3F50: FF              RST     0X38                
3F51: FF              RST     0X38                
3F52: FF              RST     0X38                
3F53: FF              RST     0X38                
3F54: FF              RST     0X38                
3F55: FF              RST     0X38                
3F56: FF              RST     0X38                
3F57: FF              RST     0X38                
3F58: FF              RST     0X38                
3F59: FF              RST     0X38                
3F5A: FF              RST     0X38                
3F5B: FF              RST     0X38                
3F5C: FF              RST     0X38                
3F5D: FF              RST     0X38                
3F5E: FF              RST     0X38                
3F5F: FF              RST     0X38                
3F60: FF              RST     0X38                
3F61: FF              RST     0X38                
3F62: FF              RST     0X38                
3F63: FF              RST     0X38                
3F64: FF              RST     0X38                
3F65: FF              RST     0X38                
3F66: FF              RST     0X38                
3F67: FF              RST     0X38                
3F68: FF              RST     0X38                
3F69: FF              RST     0X38                
3F6A: FF              RST     0X38                
3F6B: FF              RST     0X38                
3F6C: FF              RST     0X38                
3F6D: FF              RST     0X38                
3F6E: FF              RST     0X38                
3F6F: FF              RST     0X38                
3F70: FF              RST     0X38                
3F71: FF              RST     0X38                
3F72: FF              RST     0X38                
3F73: FF              RST     0X38                
3F74: FF              RST     0X38                
3F75: FF              RST     0X38                
3F76: FF              RST     0X38                
3F77: FF              RST     0X38                
3F78: FF              RST     0X38                
3F79: FF              RST     0X38                
3F7A: FF              RST     0X38                
3F7B: FF              RST     0X38                
3F7C: FF              RST     0X38                
3F7D: FF              RST     0X38                
3F7E: FF              RST     0X38                
3F7F: FF              RST     0X38                
3F80: FF              RST     0X38                
3F81: FF              RST     0X38                
3F82: FF              RST     0X38                
3F83: FF              RST     0X38                
3F84: FF              RST     0X38                
3F85: FF              RST     0X38                
3F86: FF              RST     0X38                
3F87: FF              RST     0X38                
3F88: FF              RST     0X38                
3F89: FF              RST     0X38                
3F8A: FF              RST     0X38                
3F8B: FF              RST     0X38                
3F8C: FF              RST     0X38                
3F8D: FF              RST     0X38                
3F8E: FF              RST     0X38                
3F8F: FF              RST     0X38                
3F90: FF              RST     0X38                
3F91: FF              RST     0X38                
3F92: FF              RST     0X38                
3F93: FF              RST     0X38                
3F94: FF              RST     0X38                
3F95: FF              RST     0X38                
3F96: FF              RST     0X38                
3F97: FF              RST     0X38                
3F98: FF              RST     0X38                
3F99: FF              RST     0X38                
3F9A: FF              RST     0X38                
3F9B: FF              RST     0X38                
3F9C: FF              RST     0X38                
3F9D: FF              RST     0X38                
3F9E: FF              RST     0X38                
3F9F: FF              RST     0X38                
3FA0: FF              RST     0X38                
3FA1: FF              RST     0X38                
3FA2: FF              RST     0X38                
3FA3: FF              RST     0X38                
3FA4: FF              RST     0X38                
3FA5: FF              RST     0X38                
3FA6: FF              RST     0X38                
3FA7: FF              RST     0X38                
3FA8: FF              RST     0X38                
3FA9: FF              RST     0X38                
3FAA: FF              RST     0X38                
3FAB: FF              RST     0X38                
3FAC: FF              RST     0X38                
3FAD: FF              RST     0X38                
3FAE: FF              RST     0X38                
3FAF: FF              RST     0X38                
3FB0: FF              RST     0X38                
3FB1: FF              RST     0X38                
3FB2: FF              RST     0X38                
3FB3: FF              RST     0X38                
3FB4: FF              RST     0X38                
3FB5: FF              RST     0X38                
3FB6: FF              RST     0X38                
3FB7: FF              RST     0X38                
3FB8: FF              RST     0X38                
3FB9: FF              RST     0X38                
3FBA: FF              RST     0X38                
3FBB: FF              RST     0X38                
3FBC: FF              RST     0X38                
3FBD: FF              RST     0X38                
3FBE: FF              RST     0X38                
3FBF: FF              RST     0X38                
3FC0: FF              RST     0X38                
3FC1: FF              RST     0X38                
3FC2: FF              RST     0X38                
3FC3: FF              RST     0X38                
3FC4: FF              RST     0X38                
3FC5: FF              RST     0X38                
3FC6: FF              RST     0X38                
3FC7: FF              RST     0X38                
3FC8: FF              RST     0X38                
3FC9: FF              RST     0X38                
3FCA: FF              RST     0X38                
3FCB: FF              RST     0X38                
3FCC: FF              RST     0X38                
3FCD: FF              RST     0X38                
3FCE: FF              RST     0X38                
3FCF: FF              RST     0X38                
3FD0: FF              RST     0X38                
3FD1: FF              RST     0X38                
3FD2: FF              RST     0X38                
3FD3: FF              RST     0X38                
3FD4: FF              RST     0X38                
3FD5: FF              RST     0X38                
3FD6: FF              RST     0X38                
3FD7: FF              RST     0X38                
3FD8: FF              RST     0X38                
3FD9: FF              RST     0X38                
3FDA: FF              RST     0X38                
3FDB: FF              RST     0X38                
3FDC: FF              RST     0X38                
3FDD: FF              RST     0X38                
3FDE: FF              RST     0X38                
3FDF: FF              RST     0X38                
3FE0: FF              RST     0X38                
3FE1: FF              RST     0X38                
3FE2: FF              RST     0X38                
3FE3: FF              RST     0X38                
3FE4: FF              RST     0X38                
3FE5: FF              RST     0X38                
3FE6: FF              RST     0X38                
3FE7: FF              RST     0X38                
3FE8: FF              RST     0X38                
3FE9: FF              RST     0X38                
3FEA: FF              RST     0X38                
3FEB: FF              RST     0X38                
3FEC: FF              RST     0X38                
3FED: FF              RST     0X38                
3FEE: FF              RST     0X38                
3FEF: FF              RST     0X38                
3FF0: FF              RST     0X38                
3FF1: FF              RST     0X38                
3FF2: FF              RST     0X38                
3FF3: FF              RST     0X38                
3FF4: FF              RST     0X38                
3FF5: FF              RST     0X38                
3FF6: FF              RST     0X38                
3FF7: FF              RST     0X38                
3FF8: FF              RST     0X38                
3FF9: FF              RST     0X38                
3FFA: FF              RST     0X38                
3FFB: FF              RST     0X38                
3FFC: FF              RST     0X38                
3FFD: FF              RST     0X38                
3FFE: FF              RST     0X38                
3FFF: DA 00 00        JP      C,$0000             ; {}
```

