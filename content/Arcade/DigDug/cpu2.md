![DigDug](digdug.jpg)

# DigDug CPU2 Code

>>> cpu Z80

>>> binary 0000:roms/dd1.5b + roms/dd1.6b

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
0000: F3              DI                          
0001: ED 56           IM      1                   
0003: C3 68 00        JP      $0068               ; {}
0006: 00              NOP                         
0007: 00              NOP                         
0008: 87              ADD     A,A                 
0009: 30 05           JR      NC,$123B            ; {}
000B: 24              INC     H                   
000C: C3 10 00        JP      $0010               ; {}
000F: 00              NOP                         
0010: 85              ADD     A,L                 
0011: 6F              LD      L,A                 
0012: D0              RET     NC                  
0013: 24              INC     H                   
0014: C9              RET                         
0015: 00              NOP                         
0016: 00              NOP                         
0017: 00              NOP                         
0018: 00              NOP                         
0019: 00              NOP                         
001A: 00              NOP                         
001B: 00              NOP                         
001C: 00              NOP                         
001D: 00              NOP                         
001E: 00              NOP                         
001F: 00              NOP                         
0020: 00              NOP                         
0021: 00              NOP                         
0022: 00              NOP                         
0023: 00              NOP                         
0024: 00              NOP                         
0025: 00              NOP                         
0026: 00              NOP                         
0027: 00              NOP                         
0028: 00              NOP                         
0029: 00              NOP                         
002A: 00              NOP                         
002B: 00              NOP                         
002C: 00              NOP                         
002D: 00              NOP                         
002E: 00              NOP                         
002F: 00              NOP                         
0030: 00              NOP                         
0031: 00              NOP                         
0032: 00              NOP                         
0033: 00              NOP                         
0034: 00              NOP                         
0035: 00              NOP                         
0036: 00              NOP                         
0037: 00              NOP                         
0038: E5              PUSH    HL                  
0039: D5              PUSH    DE                  
003A: C5              PUSH    BC                  
003B: F5              PUSH    AF                  
003C: CD 80 00        CALL    $0080               ; {}
003F: F1              POP     AF                  
0040: C1              POP     BC                  
0041: D1              POP     DE                  
0042: E1              POP     HL                  
0043: FB              EI                          
0044: C9              RET                         
0045: FF              RST     0X38                
0046: FF              RST     0X38                
0047: FF              RST     0X38                
0048: FF              RST     0X38                
0049: FF              RST     0X38                
004A: FF              RST     0X38                
004B: FF              RST     0X38                
004C: FF              RST     0X38                
004D: FF              RST     0X38                
004E: FF              RST     0X38                
004F: FF              RST     0X38                
0050: FF              RST     0X38                
0051: FF              RST     0X38                
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
0066: ED 45           RETN                        
0068: AF              XOR     A                   
0069: 32 21 68        LD      ($6821),A           
006C: 31 80 9A        LD      SP,$9A80            
006F: CD 03 1F        CALL    $1F03               ; {}
0072: 3E 01           LD      A,$01               
0074: 32 21 68        LD      ($6821),A           
0077: FB              EI                          
0078: 31 80 9A        LD      SP,$9A80            
007B: CD D8 1D        CALL    $1DD8               ; {}
007E: 18 F8           JR      $122E               ; {}
0080: AF              XOR     A                   
0081: 32 21 68        LD      ($6821),A           
0084: 32 02 A0        LD      ($A002),A           
0087: 3A 9A 87        LD      A,($879A)           
008A: A7              AND     A                   
008B: C2 DF 02        JP      NZ,$02DF            ; {}
008E: CD 4C 0E        CALL    $0E4C               ; {}
0091: CD 9F 1B        CALL    $1B9F               ; {}
0094: 3A CF 87        LD      A,($87CF)           
0097: CB 6F           BIT     5,A                 
0099: CA D0 02        JP      Z,$02D0             ; {}
009C: 3A 8C 89        LD      A,($898C)           
009F: A7              AND     A                   
00A0: 20 02           JR      NZ,$1238            ; {}
00A2: 3E 05           LD      A,$05               
00A4: 32 09 84        LD      ($8409),A           
00A7: 21 E5 89        LD      HL,$89E5            
00AA: 11 EF 89        LD      DE,$89EF            
00AD: 06 04           LD      B,$04               
00AF: C5              PUSH    BC                  
00B0: CD 6F 04        CALL    $046F               ; {}
00B3: C1              POP     BC                  
00B4: 10 F9           DJNZ    $122F               ; {}
00B6: 3A E2 89        LD      A,($89E2)           
00B9: E6 0F           AND     $0F                 
00BB: 32 E2 89        LD      ($89E2),A           
00BE: 3A F3 89        LD      A,($89F3)           
00C1: FE 3C           CP      $3C                 
00C3: 20 12           JR      NZ,$1248            ; {}
00C5: AF              XOR     A                   
00C6: 32 F3 89        LD      ($89F3),A           
00C9: 21 E8 89        LD      HL,$89E8            
00CC: 06 03           LD      B,$03               
00CE: 37              SCF                         
00CF: 7E              LD      A,(HL)              
00D0: CE 00           ADC     $00                 
00D2: 27              DAA                         
00D3: 77              LD      (HL),A              
00D4: 2B              DEC     HL                  
00D5: 10 F8           DJNZ    $122E               ; {}
00D7: 21 CC 87        LD      HL,$87CC            
00DA: CB 4E           BIT     1,(HL)              
00DC: 28 05           JR      Z,$123B             ; {}
00DE: CB 56           BIT     2,(HL)              
00E0: CA D0 02        JP      Z,$02D0             ; {}
00E3: 00              NOP                         
00E4: 3A 57 86        LD      A,($8657)           
00E7: E6 03           AND     $03                 
00E9: C2 9B 04        JP      NZ,$049B            ; {}
00EC: 21 85 87        LD      HL,$8785            
00EF: 11 00 84        LD      DE,$8400            
00F2: 1A              LD      A,(DE)              
00F3: CB 4F           BIT     1,A                 
00F5: 20 06           JR      NZ,$123C            ; {}
00F7: CB 56           BIT     2,(HL)              
00F9: 20 33           JR      NZ,$1269            ; {}
00FB: 18 10           JR      $1246               ; {}
00FD: CB 5E           BIT     3,(HL)              
00FF: 20 33           JR      NZ,$1269            ; {}
0101: 3A 81 9A        LD      A,($9A81)           
0104: FE 00           CP      $00                 
0106: CA D0 02        JP      Z,$02D0             ; {}
0109: CB DE           SET     3,(HL)              
010B: 18 0A           JR      $1240               ; {}
010D: 3A 81 9A        LD      A,($9A81)           
0110: FE 00           CP      $00                 
0112: CA D0 02        JP      Z,$02D0             ; {}
0115: CB D6           SET     2,(HL)              
0117: 21 87 04        LD      HL,$0487            
011A: 22 5A 86        LD      ($865A),HL          
011D: 3E 0A           LD      A,$0A               
011F: 32 5C 86        LD      ($865C),A           
0122: 21 00 00        LD      HL,$0000            
0125: 22 5E 86        LD      ($865E),HL          
0128: CD 51 03        CALL    $0351               ; {}
012B: C3 D0 02        JP      $02D0               ; {}
012E: CB 46           BIT     0,(HL)              
0130: 20 0A           JR      NZ,$1240            ; {}
0132: 18 04           JR      $123A               ; {}
0134: CB 4E           BIT     1,(HL)              
0136: 20 04           JR      NZ,$123A            ; {}
0138: CB FE           SET     7,(HL)              
013A: 18 23           JR      $1259               ; {}
013C: CB BE           RES     7,(HL)              
013E: 3A D5 85        LD      A,($85D5)           
0141: A7              AND     A                   
0142: C2 E5 02        JP      NZ,$02E5            ; {}
0145: 21 00 84        LD      HL,$8400            
0148: CB 6E           BIT     5,(HL)              
014A: CA E5 02        JP      Z,$02E5             ; {}
014D: 23              INC     HL                  
014E: CB 7E           BIT     7,(HL)              
0150: 28 03           JR      Z,$1239             ; {}
0152: C3 E5 02        JP      $02E5               ; {}
0155: CB 6E           BIT     5,(HL)              
0157: 20 06           JR      NZ,$123C            ; {}
0159: CD 51 03        CALL    $0351               ; {}
015C: C3 E5 02        JP      $02E5               ; {}
015F: CD 51 12        CALL    $1251               ; {}
0162: 3A 01 84        LD      A,($8401)           
0165: CB 7F           BIT     7,A                 
0167: C2 D0 02        JP      NZ,$02D0            ; {}
016A: 3A 85 87        LD      A,($8785)           
016D: CB 7F           BIT     7,A                 
016F: 20 0F           JR      NZ,$1245            ; {}
0171: 3A 6F 89        LD      A,($896F)           
0174: CB 47           BIT     0,A                 
0176: CA D0 02        JP      Z,$02D0             ; {}
0179: 3A 57 86        LD      A,($8657)           
017C: CB 4F           BIT     1,A                 
017E: 28 40           JR      Z,$1276             ; {}
0180: 3A 5C 86        LD      A,($865C)           
0183: A7              AND     A                   
0184: CA DF 02        JP      Z,$02DF             ; {}
0187: 2A 5E 86        LD      HL,($865E)          
018A: 7D              LD      A,L                 
018B: B4              OR      H                   
018C: 20 25           JR      NZ,$125B            ; {}
018E: 2A 5A 86        LD      HL,($865A)          
0191: 7E              LD      A,(HL)              
0192: 32 77 86        LD      ($8677),A           
0195: 23              INC     HL                  
0196: 56              LD      D,(HL)              
0197: 23              INC     HL                  
0198: 5E              LD      E,(HL)              
0199: ED 53 5E 86     LD      ($865E),DE          
019D: 23              INC     HL                  
019E: 22 5A 86        LD      ($865A),HL          
01A1: 3A 5C 86        LD      A,($865C)           
01A4: 3D              DEC     A                   
01A5: 32 5C 86        LD      ($865C),A           
01A8: 7B              LD      A,E                 
01A9: B2              OR      D                   
01AA: 20 07           JR      NZ,$123D            ; {}
01AC: AF              XOR     A                   
01AD: 32 5C 86        LD      ($865C),A           
01B0: C3 DF 02        JP      $02DF               ; {}
01B3: 2A 5E 86        LD      HL,($865E)          
01B6: 2B              DEC     HL                  
01B7: 22 5E 86        LD      ($865E),HL          
01BA: 3A 77 86        LD      A,($8677)           
01BD: 32 70 89        LD      ($8970),A           
01C0: 3A 01 84        LD      A,($8401)           
01C3: CB 5F           BIT     3,A                 
01C5: F5              PUSH    AF                  
01C6: C4 4E 10        CALL    NZ,$104E            ; {}
01C9: F1              POP     AF                  
01CA: C2 9D 02        JP      NZ,$029D            ; {}
01CD: 3A 46 86        LD      A,($8646)           
01D0: CB 47           BIT     0,A                 
01D2: C2 35 02        JP      NZ,$0235            ; {}
01D5: 21 03 84        LD      HL,$8403            
01D8: CB 56           BIT     2,(HL)              
01DA: 28 4F           JR      Z,$1285             ; {}
01DC: 3A 85 87        LD      A,($8785)           
01DF: CB 7F           BIT     7,A                 
01E1: 20 07           JR      NZ,$123D            ; {}
01E3: 3A 57 86        LD      A,($8657)           
01E6: CB 4F           BIT     1,A                 
01E8: 28 05           JR      Z,$123B             ; {}
01EA: 3A 70 89        LD      A,($8970)           
01ED: 18 03           JR      $1239               ; {}
01EF: 3A B0 85        LD      A,($85B0)           
01F2: 4F              LD      C,A                 
01F3: E6 0F           AND     $0F                 
01F5: FE 08           CP      $08                 
01F7: CA 4E 02        JP      Z,$024E             ; {}
01FA: 79              LD      A,C                 
01FB: CB 6F           BIT     5,A                 
01FD: 28 4F           JR      Z,$1285             ; {}
01FF: 21 9F 87        LD      HL,$879F            
0202: 7E              LD      A,(HL)              
0203: E6 0F           AND     $0F                 
0205: FE 00           CP      $00                 
0207: 28 03           JR      Z,$1239             ; {}
0209: 35              DEC     (HL)                
020A: 18 47           JR      $127D               ; {}
020C: 21 03 84        LD      HL,$8403            
020F: CB 96           RES     2,(HL)              
0211: 23              INC     HL                  
0212: CB 96           RES     2,(HL)              
0214: AF              XOR     A                   
0215: 32 41 86        LD      ($8641),A           
0218: 32 A0 98        LD      ($98A0),A           
021B: 32 A1 98        LD      ($98A1),A           
021E: 21 82 98        LD      HL,$9882            
0221: 06 08           LD      B,$08               
0223: 36 00           LD      (HL),$00            
0225: 23              INC     HL                  
0226: 32 30 68        LD      ($6830),A           
0229: 10 F8           DJNZ    $122E               ; {}
022B: CD C7 10        CALL    $10C7               ; {}
022E: 21 04 84        LD      HL,$8404            
0231: CB 96           RES     2,(HL)              
0233: 18 68           JR      $129E               ; {}
0235: AF              XOR     A                   
0236: 32 A0 98        LD      ($98A0),A           
0239: 32 A1 98        LD      ($98A1),A           
023C: 3A AE 85        LD      A,($85AE)           
023F: CB 4F           BIT     1,A                 
0241: 28 04           JR      Z,$123A             ; {}
0243: 3E 1D           LD      A,$1D               
0245: 18 02           JR      $1238               ; {}
0247: 3E 1C           LD      A,$1C               
0249: 32 22 98        LD      ($9822),A           
024C: 18 4F           JR      $1285               ; {}
024E: 3E 01           LD      A,$01               
0250: 32 9F 87        LD      ($879F),A           
0253: 3A A2 98        LD      A,($98A2)           
0256: 32 A0 98        LD      ($98A0),A           
0259: 3A A3 98        LD      A,($98A3)           
025C: 32 A1 98        LD      ($98A1),A           
025F: 3A 22 99        LD      A,($9922)           
0262: 32 20 99        LD      ($9920),A           
0265: 3E 07           LD      A,$07               
0267: 32 21 98        LD      ($9821),A           
026A: 3A 03 84        LD      A,($8403)           
026D: CB 5F           BIT     3,A                 
026F: 20 17           JR      NZ,$124D            ; {}
0271: 3A E4 87        LD      A,($87E4)           
0274: CB 4F           BIT     1,A                 
0276: 28 08           JR      Z,$123E             ; {}
0278: 11 0E 0C        LD      DE,$0C0E            
027B: CD 0E 04        CALL    $040E               ; {}
027E: 18 1D           JR      $1253               ; {}
0280: 11 0A 08        LD      DE,$080A            
0283: CD 0E 04        CALL    $040E               ; {}
0286: 18 15           JR      $124B               ; {}
0288: 3A AE 85        LD      A,($85AE)           
028B: CB 4F           BIT     1,A                 
028D: 28 08           JR      Z,$123E             ; {}
028F: 11 0F 0D        LD      DE,$0D0F            
0292: CD 0E 04        CALL    $040E               ; {}
0295: 18 06           JR      $123C               ; {}
0297: 11 0B 09        LD      DE,$090B            
029A: CD 0E 04        CALL    $040E               ; {}
029D: CD 0E 13        CALL    $130E               ; {}
02A0: CD 67 19        CALL    $1967               ; {}
02A3: 3A 46 86        LD      A,($8646)           
02A6: CB 47           BIT     0,A                 
02A8: 20 1C           JR      NZ,$1252            ; {}
02AA: CB 4F           BIT     1,A                 
02AC: 20 18           JR      NZ,$124E            ; {}
02AE: 21 01 84        LD      HL,$8401            
02B1: CB 66           BIT     4,(HL)              
02B3: 20 11           JR      NZ,$1247            ; {}
02B5: CD 15 03        CALL    $0315               ; {}
02B8: 3A A2 98        LD      A,($98A2)           
02BB: 32 80 98        LD      ($9880),A           
02BE: 3A A3 98        LD      A,($98A3)           
02C1: 32 81 98        LD      ($9881),A           
02C4: 18 0A           JR      $1240               ; {}
02C6: AF              XOR     A                   
02C7: 32 80 98        LD      ($9880),A           
02CA: 32 81 98        LD      ($9881),A           
02CD: CD 15 03        CALL    $0315               ; {}
02D0: 32 30 68        LD      ($6830),A           
02D3: 21 56 86        LD      HL,$8656            
02D6: CB 5E           BIT     3,(HL)              
02D8: 28 05           JR      Z,$123B             ; {}
02DA: CB 9E           RES     3,(HL)              
02DC: CD EA 02        CALL    $02EA               ; {}
02DF: 3E 01           LD      A,$01               
02E1: 32 21 68        LD      ($6821),A           
02E4: C9              RET                         
02E5: CD 67 19        CALL    $1967               ; {}
02E8: 18 E6           JR      $121C               ; {}
02EA: 2A DC 85        LD      HL,($85DC)          
02ED: E5              PUSH    HL                  
02EE: FD E1           POP     IY                  
02F0: 2A DA 85        LD      HL,($85DA)          
02F3: E5              PUSH    HL                  
02F4: DD E1           POP     IX                  
02F6: 2A D6 85        LD      HL,($85D6)          
02F9: ED 5B D8 85     LD      DE,($85D8)          
02FD: 3A AE 85        LD      A,($85AE)           
0300: E6 0F           AND     $0F                 
0302: CA 4D 15        JP      Z,$154D             ; {}
0305: FE 02           CP      $02                 
0307: CA 62 15        JP      Z,$1562             ; {}
030A: FE 04           CP      $04                 
030C: CA 19 15        JP      Z,$1519             ; {}
030F: FE 06           CP      $06                 
0311: CA 35 15        JP      Z,$1535             ; {}
0314: C9              RET                         
0315: 3A 46 86        LD      A,($8646)           
0318: E6 03           AND     $03                 
031A: 20 30           JR      NZ,$1266            ; {}
031C: 3A 01 84        LD      A,($8401)           
031F: CB 7F           BIT     7,A                 
0321: 20 29           JR      NZ,$125F            ; {}
0323: 3A 03 84        LD      A,($8403)           
0326: CB 57           BIT     2,A                 
0328: 20 22           JR      NZ,$1258            ; {}
032A: 3A 85 87        LD      A,($8785)           
032D: CB 7F           BIT     7,A                 
032F: 20 0C           JR      NZ,$1242            ; {}
0331: 3A 57 86        LD      A,($8657)           
0334: CB 4F           BIT     1,A                 
0336: 20 05           JR      NZ,$123B            ; {}
0338: 3A B0 85        LD      A,($85B0)           
033B: 18 03           JR      $1239               ; {}
033D: 3A 70 89        LD      A,($8970)           
0340: E6 0F           AND     $0F                 
0342: FE 08           CP      $08                 
0344: 28 06           JR      Z,$123C             ; {}
0346: 3E 01           LD      A,$01               
0348: 32 91 9A        LD      ($9A91),A           
034B: C9              RET                         
034C: AF              XOR     A                   
034D: 32 91 9A        LD      ($9A91),A           
0350: C9              RET                         
0351: 3A 00 84        LD      A,($8400)           
0354: CB 4F           BIT     1,A                 
0356: 20 05           JR      NZ,$123B            ; {}
0358: 3A 0D 84        LD      A,($840D)           
035B: 18 03           JR      $1239               ; {}
035D: 3A 0E 84        LD      A,($840E)           
0360: 11 01 00        LD      DE,$0001            
0363: A7              AND     A                   
0364: 28 0F           JR      Z,$1245             ; {}
0366: 1F              RRA                         
0367: 47              LD      B,A                 
0368: 30 04           JR      NC,$123A            ; {}
036A: 7A              LD      A,D                 
036B: 83              ADD     A,E                 
036C: 27              DAA                         
036D: 57              LD      D,A                 
036E: 7B              LD      A,E                 
036F: 87              ADD     A,A                 
0370: 27              DAA                         
0371: 5F              LD      E,A                 
0372: 78              LD      A,B                 
0373: 18 EE           JR      $1224               ; {}
0375: 21 D5 98        LD      HL,$98D5            
0378: DD 21 55 98     LD      IX,$9855            
037C: FD 21 28 04     LD      IY,$0428            
0380: CD 58 04        CALL    $0458               ; {}
0383: DD 21 54 98     LD      IX,$9854            
0387: 21 D4 98        LD      HL,$98D4            
038A: 7A              LD      A,D                 
038B: E6 0F           AND     $0F                 
038D: 5F              LD      E,A                 
038E: 7A              LD      A,D                 
038F: E6 F0           AND     $F0                 
0391: 4F              LD      C,A                 
0392: 16 00           LD      D,$00               
0394: FE 70           CP      $70                 
0396: 38 04           JR      C,$123A             ; {}
0398: 1E 08           LD      E,$08               
039A: 0E 60           LD      C,$60               
039C: 79              LD      A,C                 
039D: FD 21 3A 04     LD      IY,$043A            
03A1: FE 00           CP      $00                 
03A3: 28 2C           JR      Z,$1262             ; {}
03A5: FD 21 52 04     LD      IY,$0452            
03A9: FE 10           CP      $10                 
03AB: 28 24           JR      Z,$125A             ; {}
03AD: FD 21 4C 04     LD      IY,$044C            
03B1: FE 20           CP      $20                 
03B3: 28 1C           JR      Z,$1252             ; {}
03B5: FD 21 46 04     LD      IY,$0446            
03B9: FE 30           CP      $30                 
03BB: 28 14           JR      Z,$124A             ; {}
03BD: FD 21 40 04     LD      IY,$0440            
03C1: FE 40           CP      $40                 
03C3: 28 0C           JR      Z,$1242             ; {}
03C5: FD 21 34 04     LD      IY,$0434            
03C9: FE 50           CP      $50                 
03CB: 28 04           JR      Z,$123A             ; {}
03CD: FD 21 2E 04     LD      IY,$042E            
03D1: CD 58 04        CALL    $0458               ; {}
03D4: 21 8A 98        LD      HL,$988A            
03D7: 06 09           LD      B,$09               
03D9: 3E 61           LD      A,$61               
03DB: 91              SUB     C                   
03DC: 77              LD      (HL),A              
03DD: 23              INC     HL                  
03DE: 36 08           LD      (HL),$08            
03E0: 23              INC     HL                  
03E1: C6 10           ADD     $10                 
03E3: 10 F7           DJNZ    $122D               ; {}
03E5: 21 16 04        LD      HL,$0416            
03E8: 19              ADD     HL,DE               
03E9: 11 0A 98        LD      DE,$980A            
03EC: 06 09           LD      B,$09               
03EE: 7E              LD      A,(HL)              
03EF: 12              LD      (DE),A              
03F0: 23              INC     HL                  
03F1: 13              INC     DE                  
03F2: 3E 19           LD      A,$19               
03F4: 12              LD      (DE),A              
03F5: 13              INC     DE                  
03F6: 10 F6           DJNZ    $122C               ; {}
03F8: 3A 00 84        LD      A,($8400)           
03FB: CB 4F           BIT     1,A                 
03FD: C8              RET     Z                   
03FE: CB 57           BIT     2,A                 
0400: C8              RET     Z                   
0401: 21 D4 98        LD      HL,$98D4            
0404: 06 06           LD      B,$06               
0406: 3E 10           LD      A,$10               
0408: 86              ADD     A,(HL)              
0409: 77              LD      (HL),A              
040A: 23              INC     HL                  
040B: 10 F9           DJNZ    $122F               ; {}
040D: C9              RET                         
040E: 21 20 98        LD      HL,$9820            
0411: 73              LD      (HL),E              
0412: 23              INC     HL                  
0413: 23              INC     HL                  
0414: 72              LD      (HL),D              
0415: C9              RET                         
0416: 32 32 32        LD      ($3232),A           
0419: 32 32 32        LD      ($3232),A           
041C: 32 32 32        LD      ($3232),A           
041F: 69              LD      L,C                 
0420: 69              LD      L,C                 
0421: 69              LD      L,C                 
0422: 69              LD      L,C                 
0423: 69              LD      L,C                 
0424: 69              LD      L,C                 
0425: 69              LD      L,C                 
0426: 69              LD      L,C                 
0427: 69              LD      L,C                 
0428: 00              NOP                         
0429: 00              NOP                         
042A: 00              NOP                         
042B: 18 18           JR      $124E               ; {}
042D: 18 D1           JR      $1207               ; {}
042F: B1              OR      C                   
0430: 91              SUB     C                   
0431: CE CE           ADC     $CE                 
0433: CE E1           ADC     $E1                 
0435: C1              POP     BC                  
0436: A1              AND     C                   
0437: CE CE           ADC     $CE                 
0439: CE 00           ADC     $00                 
043B: 00              NOP                         
043C: 00              NOP                         
043D: 32 32 32        LD      ($3232),A           
0440: 00              NOP                         
0441: D1              POP     DE                  
0442: B1              OR      C                   
0443: 32 CE CE        LD      ($CECE),A           
0446: 00              NOP                         
0447: E1              POP     HL                  
0448: C1              POP     BC                  
0449: 32 CE CE        LD      ($CECE),A           
044C: 00              NOP                         
044D: 00              NOP                         
044E: D1              POP     DE                  
044F: 32 32 CE        LD      ($CE32),A           
0452: 00              NOP                         
0453: 00              NOP                         
0454: E1              POP     HL                  
0455: 32 32 CE        LD      ($CE32),A           
0458: 06 03           LD      B,$03               
045A: FD 7E 03        LD      A,(IY+$03)          
045D: DD 77 00        LD      (IX+$00),A          
0460: FD 7E 00        LD      A,(IY+$00)          
0463: 77              LD      (HL),A              
0464: 23              INC     HL                  
0465: 23              INC     HL                  
0466: FD 23           INC     IY                  
0468: DD 23           INC     IX                  
046A: DD 23           INC     IX                  
046C: 10 EC           DJNZ    $1222               ; {}
046E: C9              RET                         
046F: 1A              LD      A,(DE)              
0470: CB 3F           SRL     A                   
0472: CB 3F           SRL     A                   
0474: CB 3F           SRL     A                   
0476: CB 3F           SRL     A                   
0478: 47              LD      B,A                 
0479: 13              INC     DE                  
047A: 1A              LD      A,(DE)              
047B: CB 27           SLA     A                   
047D: CB 27           SLA     A                   
047F: CB 27           SLA     A                   
0481: CB 27           SLA     A                   
0483: B0              OR      B                   
0484: 77              LD      (HL),A              
0485: 2B              DEC     HL                  
0486: C9              RET                         
0487: 36 00           LD      (HL),$00            
0489: 01 38 00        LD      BC,$0038            
048C: 1E 36           LD      E,$36               
048E: 00              NOP                         
048F: 64              LD      H,H                 
0490: 34              INC     (HL)                
0491: 00              NOP                         
0492: E4 32 00        CALL    PO,$0032            ; {}
0495: 08              EX      AF,AF'              
0496: 38 01           JR      C,$1237             ; {}
0498: 00              NOP                         
0499: FF              RST     0X38                
049A: FF              RST     0X38                
049B: 21 87 87        LD      HL,$8787            
049E: 36 FF           LD      (HL),$FF            
04A0: 21 57 86        LD      HL,$8657            
04A3: CB 46           BIT     0,(HL)              
04A5: CA 17 05        JP      Z,$0517             ; {}
04A8: CB CE           SET     1,(HL)              
04AA: CB 76           BIT     6,(HL)              
04AC: 20 0A           JR      NZ,$1240            ; {}
04AE: CB F6           SET     6,(HL)              
04B0: 21 58 86        LD      HL,$8658            
04B3: 36 00           LD      (HL),$00            
04B5: C3 17 05        JP      $0517               ; {}
04B8: 21 58 86        LD      HL,$8658            
04BB: 7E              LD      A,(HL)              
04BC: E6 0F           AND     $0F                 
04BE: 47              LD      B,A                 
04BF: CB 66           BIT     4,(HL)              
04C1: 20 2B           JR      NZ,$1261            ; {}
04C3: 78              LD      A,B                 
04C4: A7              AND     A                   
04C5: CA 26 05        JP      Z,$0526             ; {}
04C8: 3D              DEC     A                   
04C9: CA A2 06        JP      Z,$06A2             ; {}
04CC: 3D              DEC     A                   
04CD: CA 0D 07        JP      Z,$070D             ; {}
04D0: 3D              DEC     A                   
04D1: CA 48 07        JP      Z,$0748             ; {}
04D4: 3D              DEC     A                   
04D5: 3D              DEC     A                   
04D6: 3D              DEC     A                   
04D7: CA 5D 07        JP      Z,$075D             ; {}
04DA: 3D              DEC     A                   
04DB: CA 85 07        JP      Z,$0785             ; {}
04DE: 3D              DEC     A                   
04DF: CA C0 07        JP      Z,$07C0             ; {}
04E2: 3D              DEC     A                   
04E3: CA 5E 08        JP      Z,$085E             ; {}
04E6: 3D              DEC     A                   
04E7: CA 7D 08        JP      Z,$087D             ; {}
04EA: 36 00           LD      (HL),$00            
04EC: 18 29           JR      $125F               ; {}
04EE: 78              LD      A,B                 
04EF: A7              AND     A                   
04F0: CA 82 08        JP      Z,$0882             ; {}
04F3: 3D              DEC     A                   
04F4: CA B5 09        JP      Z,$09B5             ; {}
04F7: 3D              DEC     A                   
04F8: CA 18 0A        JP      Z,$0A18             ; {}
04FB: 3D              DEC     A                   
04FC: CA BC 0B        JP      Z,$0BBC             ; {}
04FF: 3D              DEC     A                   
0500: 3D              DEC     A                   
0501: 3D              DEC     A                   
0502: CA BF 0B        JP      Z,$0BBF             ; {}
0505: 3D              DEC     A                   
0506: CA C7 0B        JP      Z,$0BC7             ; {}
0509: 3D              DEC     A                   
050A: CA DC 0B        JP      Z,$0BDC             ; {}
050D: 3D              DEC     A                   
050E: CA EB 0B        JP      Z,$0BEB             ; {}
0511: 3D              DEC     A                   
0512: CA F3 0B        JP      Z,$0BF3             ; {}
0515: 36 00           LD      (HL),$00            
0517: 21 57 86        LD      HL,$8657            
051A: CB 46           BIT     0,(HL)              
051C: 20 02           JR      NZ,$1238            ; {}
051E: 36 00           LD      (HL),$00            
0520: 3E 01           LD      A,$01               
0522: 32 21 68        LD      ($6821),A           
0525: C9              RET                         
0526: CB E6           SET     4,(HL)              
0528: 21 80 98        LD      HL,$9880            
052B: 06 80           LD      B,$80               
052D: 36 00           LD      (HL),$00            
052F: 23              INC     HL                  
0530: 10 FB           DJNZ    $1231               ; {}
0532: 21 00 A0        LD      HL,$A000            
0535: 36 01           LD      (HL),$01            
0537: 23              INC     HL                  
0538: 36 01           LD      (HL),$01            
053A: 23              INC     HL                  
053B: 23              INC     HL                  
053C: 36 00           LD      (HL),$00            
053E: 21 10 80        LD      HL,$8010            
0541: 11 30 80        LD      DE,$8030            
0544: 06 10           LD      B,$10               
0546: 3E 7F           LD      A,$7F               
0548: 77              LD      (HL),A              
0549: 12              LD      (DE),A              
054A: 23              INC     HL                  
054B: 13              INC     DE                  
054C: 10 F8           DJNZ    $122E               ; {}
054E: 11 1B 80        LD      DE,$801B            
0551: 21 9C 05        LD      HL,$059C            
0554: 06 06           LD      B,$06               
0556: 7E              LD      A,(HL)              
0557: 12              LD      (DE),A              
0558: 23              INC     HL                  
0559: 1B              DEC     DE                  
055A: 10 FA           DJNZ    $1230               ; {}
055C: 21 13 80        LD      HL,$8013            
055F: 36 10           LD      (HL),$10            
0561: 21 40 80        LD      HL,$8040            
0564: 01 80 03        LD      BC,$0380            
0567: 36 7F           LD      (HL),$7F            
0569: 23              INC     HL                  
056A: 0B              DEC     BC                  
056B: 32 30 68        LD      ($6830),A           
056E: 79              LD      A,C                 
056F: B0              OR      B                   
0570: 20 F5           JR      NZ,$122B            ; {}
0572: 21 68 86        LD      HL,$8668            
0575: 06 07           LD      B,$07               
0577: 36 00           LD      (HL),$00            
0579: 23              INC     HL                  
057A: 10 FB           DJNZ    $1231               ; {}
057C: 21 59 86        LD      HL,$8659            
057F: 36 01           LD      (HL),$01            
0581: 21 40 98        LD      HL,$9840            
0584: 06 0A           LD      B,$0A               
0586: 0E 86           LD      C,$86               
0588: 71              LD      (HL),C              
0589: 0C              INC     C                   
058A: 23              INC     HL                  
058B: 36 0B           LD      (HL),$0B            
058D: 23              INC     HL                  
058E: 10 F8           DJNZ    $122E               ; {}
0590: 21 40 99        LD      HL,$9940            
0593: 06 14           LD      B,$14               
0595: 36 00           LD      (HL),$00            
0597: 23              INC     HL                  
0598: 10 FB           DJNZ    $1231               ; {}
059A: 18 1A           JR      $1250               ; {}
059C: 1C              INC     E                   
059D: 2B              DEC     HL                  
059E: 1E 1D           LD      E,$1D               
05A0: 22 2D 31        LD      ($312D),HL          
05A3: 10 51           DJNZ    $1287               ; {}
05A5: 10 71           DJNZ    $12A7               ; {}
05A7: 10 91           DJNZ    $11C7               ; {}
05A9: 10 B1           DJNZ    $11E7               ; {}
05AB: 10 31           DJNZ    $1267               ; {}
05AD: 30 51           JR      NC,$1287            ; {}
05AF: 30 71           JR      NC,$12A7            ; {}
05B1: 30 91           JR      NC,$11C7            ; {}
05B3: 30 B1           JR      NC,$11E7            ; {}
05B5: 30 21           JR      NC,$1257            ; {}
05B7: A2              AND     D                   
05B8: 05              DEC     B                   
05B9: 11 C0 98        LD      DE,$98C0            
05BC: 01 14 00        LD      BC,$0014            
05BF: ED B0           LDIR                        
05C1: 3E F1           LD      A,$F1               
05C3: 32 80 98        LD      ($9880),A           
05C6: 32 A2 98        LD      ($98A2),A           
05C9: 32 E4 98        LD      ($98E4),A           
05CC: 32 EC 98        LD      ($98EC),A           
05CF: 21 D4 98        LD      HL,$98D4            
05D2: CD 9A 06        CALL    $069A               ; {}
05D5: 3E 10           LD      A,$10               
05D7: 32 81 98        LD      ($9881),A           
05DA: 32 A3 98        LD      ($98A3),A           
05DD: 32 E5 98        LD      ($98E5),A           
05E0: 32 ED 98        LD      ($98ED),A           
05E3: 21 D5 98        LD      HL,$98D5            
05E6: CD 9A 06        CALL    $069A               ; {}
05E9: 3E 02           LD      A,$02               
05EB: 32 22 98        LD      ($9822),A           
05EE: 21 22 99        LD      HL,$9922            
05F1: CD 9A 06        CALL    $069A               ; {}
05F4: 32 64 99        LD      ($9964),A           
05F7: 32 6C 99        LD      ($996C),A           
05FA: 32 6D 98        LD      ($986D),A           
05FD: AF              XOR     A                   
05FE: 32 23 98        LD      ($9823),A           
0601: 21 54 99        LD      HL,$9954            
0604: CD 9A 06        CALL    $069A               ; {}
0607: 3E 20           LD      A,$20               
0609: 32 64 98        LD      ($9864),A           
060C: 3E 01           LD      A,$01               
060E: 32 65 98        LD      ($9865),A           
0611: 3E 24           LD      A,$24               
0613: 32 6C 98        LD      ($986C),A           
0616: 3E 05           LD      A,$05               
0618: 32 25 98        LD      ($9825),A           
061B: 32 27 98        LD      ($9827),A           
061E: 32 29 98        LD      ($9829),A           
0621: 3E 09           LD      A,$09               
0623: 21 55 98        LD      HL,$9855            
0626: CD 9A 06        CALL    $069A               ; {}
0629: 21 DD 06        LD      HL,$06DD            
062C: 11 8A 98        LD      DE,$988A            
062F: 01 18 00        LD      BC,$0018            
0632: C5              PUSH    BC                  
0633: ED B0           LDIR                        
0635: C1              POP     BC                  
0636: 21 F5 06        LD      HL,$06F5            
0639: 11 0A 98        LD      DE,$980A            
063C: ED B0           LDIR                        
063E: 21 0A 99        LD      HL,$990A            
0641: 06 0C           LD      B,$0C               
0643: 36 00           LD      (HL),$00            
0645: 23              INC     HL                  
0646: 23              INC     HL                  
0647: 10 FA           DJNZ    $1230               ; {}
0649: 21 54 98        LD      HL,$9854            
064C: 06 04           LD      B,$04               
064E: 3E 48           LD      A,$48               
0650: 77              LD      (HL),A              
0651: 3C              INC     A                   
0652: 23              INC     HL                  
0653: 23              INC     HL                  
0654: 10 FA           DJNZ    $1230               ; {}
0656: 21 F6 0B        LD      HL,$0BF6            
0659: 22 5A 86        LD      ($865A),HL          
065C: 21 48 0C        LD      HL,$0C48            
065F: 22 5C 86        LD      ($865C),HL          
0662: 21 2C 0C        LD      HL,$0C2C            
0665: 22 5E 86        LD      ($865E),HL          
0668: 21 04 0C        LD      HL,$0C04            
066B: 22 60 86        LD      ($8660),HL          
066E: 21 0E 0C        LD      HL,$0C0E            
0671: 22 62 86        LD      ($8662),HL          
0674: 21 18 0C        LD      HL,$0C18            
0677: 22 64 86        LD      ($8664),HL          
067A: 21 22 0C        LD      HL,$0C22            
067D: 22 66 86        LD      ($8666),HL          
0680: 21 C0 83        LD      HL,$83C0            
0683: 06 3F           LD      B,$3F               
0685: 7E              LD      A,(HL)              
0686: FE 8C           CP      $8C                 
0688: 20 02           JR      NZ,$1238            ; {}
068A: 36 0C           LD      (HL),$0C            
068C: 23              INC     HL                  
068D: 10 F6           DJNZ    $122C               ; {}
068F: 3E 00           LD      A,$00               
0691: 32 04 A0        LD      ($A004),A           
0694: 32 05 A0        LD      ($A005),A           
0697: C3 17 05        JP      $0517               ; {}
069A: 06 04           LD      B,$04               
069C: 77              LD      (HL),A              
069D: 23              INC     HL                  
069E: 23              INC     HL                  
069F: 10 FB           DJNZ    $1231               ; {}
06A1: C9              RET                         
06A2: CB E6           SET     4,(HL)              
06A4: 21 03 A0        LD      HL,$A003            
06A7: 36 01           LD      (HL),$01            
06A9: 21 40 80        LD      HL,$8040            
06AC: 01 80 03        LD      BC,$0380            
06AF: 36 7D           LD      (HL),$7D            
06B1: 7D              LD      A,L                 
06B2: E6 1F           AND     $1F                 
06B4: FE 04           CP      $04                 
06B6: 30 02           JR      NC,$1238            ; {}
06B8: 36 8C           LD      (HL),$8C            
06BA: 23              INC     HL                  
06BB: 0B              DEC     BC                  
06BC: 79              LD      A,C                 
06BD: B0              OR      B                   
06BE: 20 EF           JR      NZ,$1225            ; {}
06C0: 21 84 80        LD      HL,$8084            
06C3: 11 20 00        LD      DE,$0020            
06C6: 0E 08           LD      C,$08               
06C8: 06 18           LD      B,$18               
06CA: E5              PUSH    HL                  
06CB: 36 7F           LD      (HL),$7F            
06CD: 19              ADD     HL,DE               
06CE: 10 FB           DJNZ    $1231               ; {}
06D0: E1              POP     HL                  
06D1: 23              INC     HL                  
06D2: 0D              DEC     C                   
06D3: 20 F3           JR      NZ,$1229            ; {}
06D5: 21 76 86        LD      HL,$8676            
06D8: 36 00           LD      (HL),$00            
06DA: C3 17 05        JP      $0517               ; {}
06DD: 21 90 41        LD      HL,$4190            
06E0: 90              SUB     B                   
06E1: A9              XOR     C                   
06E2: 90              SUB     B                   
06E3: C9              RET                         
06E4: 90              SUB     B                   
06E5: 21 B0 41        LD      HL,$41B0            
06E8: B0              OR      B                   
06E9: A9              XOR     C                   
06EA: B0              OR      B                   
06EB: C9              RET                         
06EC: B0              OR      B                   
06ED: 21 B0 89        LD      HL,$89B0            
06F0: B0              OR      B                   
06F1: B9              CP      C                   
06F2: 90              SUB     B                   
06F3: 31 90 C0        LD      SP,$C090            
06F6: 1A              LD      A,(DE)              
06F7: C1              POP     BC                  
06F8: 1A              LD      A,(DE)              
06F9: C2 1B C3        JP      NZ,$C31B            
06FC: 1B              DEC     DE                  
06FD: C4 1A C5        CALL    NZ,$C51A            
0700: 1A              LD      A,(DE)              
0701: C6 1B           ADD     $1B                 
0703: C7              RST     0X00                
0704: 1B              DEC     DE                  
0705: C8              RET     Z                   
0706: 1C              INC     E                   
0707: CB 1A           RR      D                   
0709: CC 1C CD        CALL    Z,$CD1C             
070C: 1C              INC     E                   
070D: CB E6           SET     4,(HL)              
070F: 21 76 86        LD      HL,$8676            
0712: 36 00           LD      (HL),$00            
0714: AF              XOR     A                   
0715: 32 E4 98        LD      ($98E4),A           
0718: 32 E5 98        LD      ($98E5),A           
071B: 32 EC 98        LD      ($98EC),A           
071E: 32 ED 98        LD      ($98ED),A           
0721: 32 A2 98        LD      ($98A2),A           
0724: 32 A3 98        LD      ($98A3),A           
0727: 32 80 98        LD      ($9880),A           
072A: 32 81 98        LD      ($9881),A           
072D: 21 0A 98        LD      HL,$980A            
0730: 11 8A 98        LD      DE,$988A            
0733: 06 18           LD      B,$18               
0735: 3E 00           LD      A,$00               
0737: 0E 32           LD      C,$32               
0739: 71              LD      (HL),C              
073A: 12              LD      (DE),A              
073B: 23              INC     HL                  
073C: 13              INC     DE                  
073D: 10 FA           DJNZ    $1230               ; {}
073F: 21 5F 80        LD      HL,$805F            
0742: 22 5A 86        LD      ($865A),HL          
0745: C3 17 05        JP      $0517               ; {}
0748: CB E6           SET     4,(HL)              
074A: 21 00 99        LD      HL,$9900            
074D: 06 80           LD      B,$80               
074F: 36 00           LD      (HL),$00            
0751: 23              INC     HL                  
0752: 10 FB           DJNZ    $1231               ; {}
0754: 21 00 00        LD      HL,$0000            
0757: 22 5A 86        LD      ($865A),HL          
075A: C3 17 05        JP      $0517               ; {}
075D: CB E6           SET     4,(HL)              
075F: 06 80           LD      B,$80               
0761: 21 00 98        LD      HL,$9800            
0764: 11 80 98        LD      DE,$9880            
0767: DD 21 00 99     LD      IX,$9900            
076B: AF              XOR     A                   
076C: 77              LD      (HL),A              
076D: 12              LD      (DE),A              
076E: DD 77 00        LD      (IX+$00),A          
0771: 23              INC     HL                  
0772: 13              INC     DE                  
0773: DD 23           INC     IX                  
0775: 10 F4           DJNZ    $122A               ; {}
0777: 21 00 A0        LD      HL,$A000            
077A: AF              XOR     A                   
077B: 77              LD      (HL),A              
077C: 23              INC     HL                  
077D: 77              LD      (HL),A              
077E: 23              INC     HL                  
077F: 77              LD      (HL),A              
0780: 23              INC     HL                  
0781: 77              LD      (HL),A              
0782: C3 17 05        JP      $0517               ; {}
0785: CB E6           SET     4,(HL)              
0787: 21 0D 84        LD      HL,$840D            
078A: 11 A9 87        LD      DE,$87A9            
078D: 7E              LD      A,(HL)              
078E: 12              LD      (DE),A              
078F: 4F              LD      C,A                 
0790: 23              INC     HL                  
0791: 13              INC     DE                  
0792: 7E              LD      A,(HL)              
0793: 12              LD      (DE),A              
0794: 79              LD      A,C                 
0795: 13              INC     DE                  
0796: 12              LD      (DE),A              
0797: 21 76 86        LD      HL,$8676            
079A: 36 10           LD      (HL),$10            
079C: 23              INC     HL                  
079D: 36 00           LD      (HL),$00            
079F: 21 80 87        LD      HL,$8780            
07A2: 34              INC     (HL)                
07A3: CB 46           BIT     0,(HL)              
07A5: 20 05           JR      NZ,$123B            ; {}
07A7: 21 E3 15        LD      HL,$15E3            
07AA: 18 03           JR      $1239               ; {}
07AC: 21 6D 16        LD      HL,$166D            
07AF: 22 5A 86        LD      ($865A),HL          
07B2: 3E 7E           LD      A,$7E               
07B4: 32 5C 86        LD      ($865C),A           
07B7: 21 00 00        LD      HL,$0000            
07BA: 22 5E 86        LD      ($865E),HL          
07BD: C3 17 05        JP      $0517               ; {}
07C0: CB E6           SET     4,(HL)              
07C2: 21 0D 84        LD      HL,$840D            
07C5: 11 A9 87        LD      DE,$87A9            
07C8: 1A              LD      A,(DE)              
07C9: 77              LD      (HL),A              
07CA: 23              INC     HL                  
07CB: 13              INC     DE                  
07CC: 1A              LD      A,(DE)              
07CD: 77              LD      (HL),A              
07CE: 21 40 80        LD      HL,$8040            
07D1: 01 80 03        LD      BC,$0380            
07D4: 36 0C           LD      (HL),$0C            
07D6: 23              INC     HL                  
07D7: 0B              DEC     BC                  
07D8: 79              LD      A,C                 
07D9: B0              OR      B                   
07DA: 20 F8           JR      NZ,$122E            ; {}
07DC: 21 80 98        LD      HL,$9880            
07DF: 06 80           LD      B,$80               
07E1: 36 00           LD      (HL),$00            
07E3: 23              INC     HL                  
07E4: 10 FB           DJNZ    $1231               ; {}
07E6: 21 00 98        LD      HL,$9800            
07E9: 06 40           LD      B,$40               
07EB: 36 32           LD      (HL),$32            
07ED: 23              INC     HL                  
07EE: 36 00           LD      (HL),$00            
07F0: 23              INC     HL                  
07F1: 10 F8           DJNZ    $122E               ; {}
07F3: 21 C0 83        LD      HL,$83C0            
07F6: 06 3F           LD      B,$3F               
07F8: 7E              LD      A,(HL)              
07F9: FE 8C           CP      $8C                 
07FB: 20 02           JR      NZ,$1238            ; {}
07FD: 36 0C           LD      (HL),$0C            
07FF: 32 30 68        LD      ($6830),A           
0802: 23              INC     HL                  
0803: 10 F3           DJNZ    $1229               ; {}
0805: 21 A2 05        LD      HL,$05A2            
0808: 11 C0 98        LD      DE,$98C0            
080B: 01 14 00        LD      BC,$0014            
080E: ED B0           LDIR                        
0810: 21 40 98        LD      HL,$9840            
0813: 06 0A           LD      B,$0A               
0815: 0E 86           LD      C,$86               
0817: 71              LD      (HL),C              
0818: 0C              INC     C                   
0819: 23              INC     HL                  
081A: 36 0B           LD      (HL),$0B            
081C: 23              INC     HL                  
081D: 10 F8           DJNZ    $122E               ; {}
081F: 21 40 99        LD      HL,$9940            
0822: 06 14           LD      B,$14               
0824: 36 00           LD      (HL),$00            
0826: 23              INC     HL                  
0827: 10 FB           DJNZ    $1231               ; {}
0829: 21 2B 81        LD      HL,$812B            
082C: 11 20 00        LD      DE,$0020            
082F: 06 0E           LD      B,$0E               
0831: DD 21 50 08     LD      IX,$0850            
0835: DD 7E 00        LD      A,(IX+$00)          
0838: 77              LD      (HL),A              
0839: DD 23           INC     IX                  
083B: 19              ADD     HL,DE               
083C: 10 F7           DJNZ    $122D               ; {}
083E: 21 03 A0        LD      HL,$A003            
0841: 36 01           LD      (HL),$01            
0843: 21 5E 86        LD      HL,$865E            
0846: 36 FF           LD      (HL),$FF            
0848: 21 CC 87        LD      HL,$87CC            
084B: CB C6           SET     0,(HL)              
084D: C3 17 05        JP      $0517               ; {}
0850: 7F              LD      A,A                 
0851: 7F              LD      A,A                 
0852: 7F              LD      A,A                 
0853: 7F              LD      A,A                 
0854: 15              DEC     D                   
0855: 7F              LD      A,A                 
0856: 2D              DEC     L                   
0857: 2C              INC     L                   
0858: 1E 1B           LD      E,$1B               
085A: 7F              LD      A,A                 
085B: 7F              LD      A,A                 
085C: 7F              LD      A,A                 
085D: 7F              LD      A,A                 
085E: CB E6           SET     4,(HL)              
0860: 3E 01           LD      A,$01               
0862: 2A 00 A0        LD      HL,($A000)          
0865: 77              LD      (HL),A              
0866: 23              INC     HL                  
0867: 77              LD      (HL),A              
0868: 23              INC     HL                  
0869: 23              INC     HL                  
086A: 36 00           LD      (HL),$00            
086C: 21 40 80        LD      HL,$8040            
086F: 01 80 03        LD      BC,$0380            
0872: 36 7F           LD      (HL),$7F            
0874: 23              INC     HL                  
0875: 0B              DEC     BC                  
0876: 79              LD      A,C                 
0877: B0              OR      B                   
0878: 20 F8           JR      NZ,$122E            ; {}
087A: C3 17 05        JP      $0517               ; {}
087D: CB E6           SET     4,(HL)              
087F: C3 17 05        JP      $0517               ; {}
0882: 21 4E 0C        LD      HL,$0C4E            
0885: 3A 59 86        LD      A,($8659)           
0888: 96              SUB     (HL)                
0889: 32 59 86        LD      ($8659),A           
088C: D2 17 05        JP      NC,$0517            ; {}
088F: 3A 68 86        LD      A,($8668)           
0892: A7              AND     A                   
0893: 20 27           JR      NZ,$125D            ; {}
0895: 2A 5A 86        LD      HL,($865A)          
0898: 7E              LD      A,(HL)              
0899: 32 6F 86        LD      ($866F),A           
089C: 23              INC     HL                  
089D: 7E              LD      A,(HL)              
089E: 23              INC     HL                  
089F: 22 5A 86        LD      ($865A),HL          
08A2: FE 09           CP      $09                 
08A4: 20 13           JR      NZ,$1249            ; {}
08A6: 32 68 86        LD      ($8668),A           
08A9: 3E 8C           LD      A,$8C               
08AB: 32 82 80        LD      ($8082),A           
08AE: 32 A2 80        LD      ($80A2),A           
08B1: 32 83 80        LD      ($8083),A           
08B4: 32 A3 80        LD      ($80A3),A           
08B7: 18 03           JR      $1239               ; {}
08B9: 32 68 86        LD      ($8668),A           
08BC: 3A 68 86        LD      A,($8668)           
08BF: 3D              DEC     A                   
08C0: 32 68 86        LD      ($8668),A           
08C3: CD 4F 0C        CALL    $0C4F               ; {}
08C6: 3A A2 98        LD      A,($98A2)           
08C9: 32 80 98        LD      ($9880),A           
08CC: 3A A3 98        LD      A,($98A3)           
08CF: 32 81 98        LD      ($9881),A           
08D2: FE 10           CP      $10                 
08D4: 20 08           JR      NZ,$123E            ; {}
08D6: 21 80 98        LD      HL,$9880            
08D9: 36 00           LD      (HL),$00            
08DB: 23              INC     HL                  
08DC: 36 00           LD      (HL),$00            
08DE: 3E 38           LD      A,$38               
08E0: 32 00 98        LD      ($9800),A           
08E3: 3E 06           LD      A,$06               
08E5: 32 01 98        LD      ($9801),A           
08E8: 3A A3 98        LD      A,($98A3)           
08EB: FE 10           CP      $10                 
08ED: 28 03           JR      Z,$1239             ; {}
08EF: CD 0E 13        CALL    $130E               ; {}
08F2: 3A 69 86        LD      A,($8669)           
08F5: A7              AND     A                   
08F6: 20 10           JR      NZ,$1246            ; {}
08F8: 2A 5C 86        LD      HL,($865C)          
08FB: 7E              LD      A,(HL)              
08FC: 32 70 86        LD      ($8670),A           
08FF: 23              INC     HL                  
0900: 7E              LD      A,(HL)              
0901: 23              INC     HL                  
0902: 22 5C 86        LD      ($865C),HL          
0905: 32 69 86        LD      ($8669),A           
0908: 3A 69 86        LD      A,($8669)           
090B: 3D              DEC     A                   
090C: 32 69 86        LD      ($8669),A           
090F: CD EE 0C        CALL    $0CEE               ; {}
0912: 3A 6A 86        LD      A,($866A)           
0915: A7              AND     A                   
0916: 20 10           JR      NZ,$1246            ; {}
0918: 2A 5E 86        LD      HL,($865E)          
091B: 7E              LD      A,(HL)              
091C: 32 71 86        LD      ($8671),A           
091F: 23              INC     HL                  
0920: 7E              LD      A,(HL)              
0921: 23              INC     HL                  
0922: 22 5E 86        LD      ($865E),HL          
0925: 32 6A 86        LD      ($866A),A           
0928: 3A 6A 86        LD      A,($866A)           
092B: 3D              DEC     A                   
092C: 32 6A 86        LD      ($866A),A           
092F: CD 4D 0D        CALL    $0D4D               ; {}
0932: 3A 6B 86        LD      A,($866B)           
0935: A7              AND     A                   
0936: 20 10           JR      NZ,$1246            ; {}
0938: 2A 60 86        LD      HL,($8660)          
093B: 7E              LD      A,(HL)              
093C: 32 72 86        LD      ($8672),A           
093F: 23              INC     HL                  
0940: 7E              LD      A,(HL)              
0941: 23              INC     HL                  
0942: 22 60 86        LD      ($8660),HL          
0945: 32 6B 86        LD      ($866B),A           
0948: 3A 6B 86        LD      A,($866B)           
094B: 3D              DEC     A                   
094C: 32 6B 86        LD      ($866B),A           
094F: CD FB 0C        CALL    $0CFB               ; {}
0952: 3A 6C 86        LD      A,($866C)           
0955: A7              AND     A                   
0956: 20 10           JR      NZ,$1246            ; {}
0958: 2A 62 86        LD      HL,($8662)          
095B: 7E              LD      A,(HL)              
095C: 32 73 86        LD      ($8673),A           
095F: 23              INC     HL                  
0960: 7E              LD      A,(HL)              
0961: 23              INC     HL                  
0962: 22 62 86        LD      ($8662),HL          
0965: 32 6C 86        LD      ($866C),A           
0968: 3A 6C 86        LD      A,($866C)           
096B: 3D              DEC     A                   
096C: 32 6C 86        LD      ($866C),A           
096F: CD 08 0D        CALL    $0D08               ; {}
0972: 3A 6D 86        LD      A,($866D)           
0975: A7              AND     A                   
0976: 20 10           JR      NZ,$1246            ; {}
0978: 2A 64 86        LD      HL,($8664)          
097B: 7E              LD      A,(HL)              
097C: 32 74 86        LD      ($8674),A           
097F: 23              INC     HL                  
0980: 7E              LD      A,(HL)              
0981: 23              INC     HL                  
0982: 22 64 86        LD      ($8664),HL          
0985: 32 6D 86        LD      ($866D),A           
0988: 3A 6D 86        LD      A,($866D)           
098B: 3D              DEC     A                   
098C: 32 6D 86        LD      ($866D),A           
098F: CD 15 0D        CALL    $0D15               ; {}
0992: 3A 6E 86        LD      A,($866E)           
0995: A7              AND     A                   
0996: 20 10           JR      NZ,$1246            ; {}
0998: 2A 66 86        LD      HL,($8666)          
099B: 7E              LD      A,(HL)              
099C: 32 75 86        LD      ($8675),A           
099F: 23              INC     HL                  
09A0: 7E              LD      A,(HL)              
09A1: 23              INC     HL                  
09A2: 22 66 86        LD      ($8666),HL          
09A5: 32 6E 86        LD      ($866E),A           
09A8: 3A 6E 86        LD      A,($866E)           
09AB: 3D              DEC     A                   
09AC: 32 6E 86        LD      ($866E),A           
09AF: CD 22 0D        CALL    $0D22               ; {}
09B2: C3 17 05        JP      $0517               ; {}
09B5: 21 76 86        LD      HL,$8676            
09B8: 34              INC     (HL)                
09B9: 7E              LD      A,(HL)              
09BA: FE 05           CP      $05                 
09BC: 30 0F           JR      NC,$1245            ; {}
09BE: F5              PUSH    AF                  
09BF: 21 C1 98        LD      HL,$98C1            
09C2: 06 0A           LD      B,$0A               
09C4: 34              INC     (HL)                
09C5: 34              INC     (HL)                
09C6: 34              INC     (HL)                
09C7: 34              INC     (HL)                
09C8: 23              INC     HL                  
09C9: 23              INC     HL                  
09CA: 10 F8           DJNZ    $122E               ; {}
09CC: F1              POP     AF                  
09CD: FE 05           CP      $05                 
09CF: 38 15           JR      C,$124B             ; {}
09D1: FE 09           CP      $09                 
09D3: 30 11           JR      NC,$1247            ; {}
09D5: F5              PUSH    AF                  
09D6: 21 E5 98        LD      HL,$98E5            
09D9: 11 ED 98        LD      DE,$98ED            
09DC: 34              INC     (HL)                
09DD: 34              INC     (HL)                
09DE: 34              INC     (HL)                
09DF: 34              INC     (HL)                
09E0: EB              EX      DE,HL               
09E1: 34              INC     (HL)                
09E2: 34              INC     (HL)                
09E3: 34              INC     (HL)                
09E4: 34              INC     (HL)                
09E5: F1              POP     AF                  
09E6: FE 09           CP      $09                 
09E8: 20 0A           JR      NZ,$1240            ; {}
09EA: 21 64 98        LD      HL,$9864            
09ED: 36 23           LD      (HL),$23            
09EF: 21 6C 98        LD      HL,$986C            
09F2: 36 27           LD      (HL),$27            
09F4: FE 05           CP      $05                 
09F6: 38 13           JR      C,$1249             ; {}
09F8: FE 37           CP      $37                 
09FA: 30 0F           JR      NC,$1245            ; {}
09FC: F5              PUSH    AF                  
09FD: 21 D5 98        LD      HL,$98D5            
0A00: 06 04           LD      B,$04               
0A02: 34              INC     (HL)                
0A03: 34              INC     (HL)                
0A04: 34              INC     (HL)                
0A05: 34              INC     (HL)                
0A06: 23              INC     HL                  
0A07: 23              INC     HL                  
0A08: 10 F8           DJNZ    $122E               ; {}
0A0A: F1              POP     AF                  
0A0B: FE 72           CP      $72                 
0A0D: C2 FB 0D        JP      NZ,$0DFB            ; {}
0A10: 21 58 86        LD      HL,$8658            
0A13: 36 02           LD      (HL),$02            
0A15: C3 FB 0D        JP      $0DFB               ; {}
0A18: 21 76 86        LD      HL,$8676            
0A1B: 34              INC     (HL)                
0A1C: CB 46           BIT     0,(HL)              
0A1E: CA 17 05        JP      Z,$0517             ; {}
0A21: 2A 5A 86        LD      HL,($865A)          
0A24: 11 3F 80        LD      DE,$803F            
0A27: A7              AND     A                   
0A28: ED 52           SBC     HL,DE               
0A2A: 20 02           JR      NZ,$1238            ; {}
0A2C: 18 1B           JR      $1251               ; {}
0A2E: 2A 5A 86        LD      HL,($865A)          
0A31: 11 F0 87        LD      DE,$87F0            
0A34: 1A              LD      A,(DE)              
0A35: CB DF           SET     3,A                 
0A37: 12              LD      (DE),A              
0A38: 11 20 00        LD      DE,$0020            
0A3B: 06 1C           LD      B,$1C               
0A3D: 36 7F           LD      (HL),$7F            
0A3F: 19              ADD     HL,DE               
0A40: 10 FB           DJNZ    $1231               ; {}
0A42: 2A 5A 86        LD      HL,($865A)          
0A45: 2B              DEC     HL                  
0A46: 22 5A 86        LD      ($865A),HL          
0A49: 21 76 86        LD      HL,$8676            
0A4C: 7E              LD      A,(HL)              
0A4D: FE 07           CP      $07                 
0A4F: 20 28           JR      NZ,$125E            ; {}
0A51: AF              XOR     A                   
0A52: 21 D4 98        LD      HL,$98D4            
0A55: 06 08           LD      B,$08               
0A57: 77              LD      (HL),A              
0A58: 23              INC     HL                  
0A59: 10 FC           DJNZ    $1232               ; {}
0A5B: 21 D4 93        LD      HL,$93D4            
0A5E: 06 08           LD      B,$08               
0A60: 77              LD      (HL),A              
0A61: 23              INC     HL                  
0A62: 10 FC           DJNZ    $1232               ; {}
0A64: 21 72 0A        LD      HL,$0A72            
0A67: 11 9C 81        LD      DE,$819C            
0A6A: 06 07           LD      B,$07               
0A6C: CD 3B 0E        CALL    $0E3B               ; {}
0A6F: C3 17 05        JP      $0517               ; {}
0A72: BF              CP      A                   
0A73: BE              CP      (HL)                
0A74: BD              CP      L                   
0A75: BC              CP      H                   
0A76: BB              CP      E                   
0A77: BA              CP      D                   
0A78: B9              CP      C                   
0A79: FE 0B           CP      $0B                 
0A7B: 20 1F           JR      NZ,$1255            ; {}
0A7D: 21 8B 0A        LD      HL,$0A8B            
0A80: 11 FA 80        LD      DE,$80FA            
0A83: 06 11           LD      B,$11               
0A85: CD 3B 0E        CALL    $0E3B               ; {}
0A88: C3 17 05        JP      $0517               ; {}
0A8B: 35              DEC     (HL)                
0A8C: 1D              DEC     E                   
0A8D: 2D              DEC     L                   
0A8E: 25              DEC     H                   
0A8F: 7F              LD      A,A                 
0A90: 28 1C           JR      Z,$1252             ; {}
0A92: 26 1A           LD      H,$1A               
0A94: 27              DAA                         
0A95: 7F              LD      A,A                 
0A96: 12              LD      (DE),A              
0A97: 18 19           JR      $124F               ; {}
0A99: 11 7F 38        LD      DE,$387F            
0A9C: FE 15           CP      $15                 
0A9E: 20 20           JR      NZ,$1256            ; {}
0AA0: 21 AE 0A        LD      HL,$0AAE            
0AA3: 11 D5 80        LD      DE,$80D5            
0AA6: 06 12           LD      B,$12               
0AA8: CD 3B 0E        CALL    $0E3B               ; {}
0AAB: C3 17 05        JP      $0517               ; {}
0AAE: 6B              LD      L,E                 
0AAF: 5A              LD      E,D                 
0AB0: 60              LD      H,B                 
0AB1: 72              LD      (HL),D              
0AB2: 5F              LD      E,A                 
0AB3: 7F              LD      A,A                 
0AB4: 7F              LD      A,A                 
0AB5: 7F              LD      A,A                 
0AB6: 7F              LD      A,A                 
0AB7: 7F              LD      A,A                 
0AB8: 7F              LD      A,A                 
0AB9: 7F              LD      A,A                 
0ABA: 7F              LD      A,A                 
0ABB: 5A              LD      E,D                 
0ABC: 64              LD      H,H                 
0ABD: 68              LD      L,B                 
0ABE: 68              LD      L,B                 
0ABF: 69              LD      L,C                 
0AC0: FE 23           CP      $23                 
0AC2: 20 17           JR      NZ,$124D            ; {}
0AC4: 21 D2 0A        LD      HL,$0AD2            
0AC7: 11 6E 81        LD      DE,$816E            
0ACA: 06 09           LD      B,$09               
0ACC: CD 3B 0E        CALL    $0E3B               ; {}
0ACF: C3 17 05        JP      $0517               ; {}
0AD2: 6B              LD      L,E                 
0AD3: 5E              LD      E,(HL)              
0AD4: 6D              LD      L,L                 
0AD5: 5C              LD      E,H                 
0AD6: 5A              LD      E,D                 
0AD7: 6B              LD      L,E                 
0AD8: 5A              LD      E,D                 
0AD9: 61              LD      H,C                 
0ADA: 5C              LD      E,H                 
0ADB: FE 61           CP      $61                 
0ADD: 20 33           JR      NZ,$1269            ; {}
0ADF: 21 F0 87        LD      HL,$87F0            
0AE2: CB 9E           RES     3,(HL)              
0AE4: AF              XOR     A                   
0AE5: 32 64 99        LD      ($9964),A           
0AE8: 3C              INC     A                   
0AE9: 32 65 98        LD      ($9865),A           
0AEC: 3C              INC     A                   
0AED: 32 6D 98        LD      ($986D),A           
0AF0: 32 6C 99        LD      ($996C),A           
0AF3: 3E 90           LD      A,$90               
0AF5: 32 E5 98        LD      ($98E5),A           
0AF8: 32 ED 98        LD      ($98ED),A           
0AFB: 3E B2           LD      A,$B2               
0AFD: 32 EC 98        LD      ($98EC),A           
0B00: 3E 52           LD      A,$52               
0B02: 32 E4 98        LD      ($98E4),A           
0B05: 3E 20           LD      A,$20               
0B07: 32 64 98        LD      ($9864),A           
0B0A: 3E 24           LD      A,$24               
0B0C: 32 6C 98        LD      ($986C),A           
0B0F: C3 17 05        JP      $0517               ; {}
0B12: 21 6D 98        LD      HL,$986D            
0B15: FE 77           CP      $77                 
0B17: 20 05           JR      NZ,$123B            ; {}
0B19: 36 0C           LD      (HL),$0C            
0B1B: C3 17 05        JP      $0517               ; {}
0B1E: FE 7F           CP      $7F                 
0B20: 20 05           JR      NZ,$123B            ; {}
0B22: 36 02           LD      (HL),$02            
0B24: C3 17 05        JP      $0517               ; {}
0B27: FE 87           CP      $87                 
0B29: 20 02           JR      NZ,$1238            ; {}
0B2B: 18 EC           JR      $1222               ; {}
0B2D: FE 8F           CP      $8F                 
0B2F: 20 02           JR      NZ,$1238            ; {}
0B31: 18 EF           JR      $1225               ; {}
0B33: FE B3           CP      $B3                 
0B35: 20 13           JR      NZ,$1249            ; {}
0B37: 36 02           LD      (HL),$02            
0B39: DD 21 A4 98     LD      IX,$98A4            
0B3D: 06 06           LD      B,$06               
0B3F: DD 36 00 00     LD      (IX+$00),$00        
0B43: DD 23           INC     IX                  
0B45: 10 F8           DJNZ    $122E               ; {}
0B47: C3 17 05        JP      $0517               ; {}
0B4A: DD 21 24 98     LD      IX,$9824            
0B4E: FD 21 A4 98     LD      IY,$98A4            
0B52: 11 EC 98        LD      DE,$98EC            
0B55: FE 97           CP      $97                 
0B57: 20 2D           JR      NZ,$1263            ; {}
0B59: 36 0C           LD      (HL),$0C            
0B5B: 1A              LD      A,(DE)              
0B5C: D6 10           SUB     $10                 
0B5E: FD 77 00        LD      (IY+$00),A          
0B61: D6 10           SUB     $10                 
0B63: FD 77 02        LD      (IY+$02),A          
0B66: D6 10           SUB     $10                 
0B68: FD 77 04        LD      (IY+$04),A          
0B6B: 13              INC     DE                  
0B6C: 1A              LD      A,(DE)              
0B6D: FD 77 01        LD      (IY+$01),A          
0B70: FD 77 03        LD      (IY+$03),A          
0B73: FD 77 05        LD      (IY+$05),A          
0B76: 3E 2C           LD      A,$2C               
0B78: DD 77 00        LD      (IX+$00),A          
0B7B: 3E 32           LD      A,$32               
0B7D: DD 77 02        LD      (IX+$02),A          
0B80: DD 77 04        LD      (IX+$04),A          
0B83: C3 17 05        JP      $0517               ; {}
0B86: FE 9D           CP      $9D                 
0B88: 20 11           JR      NZ,$1247            ; {}
0B8A: 3E 2D           LD      A,$2D               
0B8C: DD 77 00        LD      (IX+$00),A          
0B8F: 3C              INC     A                   
0B90: DD 77 02        LD      (IX+$02),A          
0B93: 3E 32           LD      A,$32               
0B95: DD 77 04        LD      (IX+$04),A          
0B98: C3 17 05        JP      $0517               ; {}
0B9B: FE A3           CP      $A3                 
0B9D: 20 10           JR      NZ,$1246            ; {}
0B9F: 3E 2F           LD      A,$2F               
0BA1: DD 77 00        LD      (IX+$00),A          
0BA4: 3C              INC     A                   
0BA5: DD 77 02        LD      (IX+$02),A          
0BA8: 3C              INC     A                   
0BA9: DD 77 04        LD      (IX+$04),A          
0BAC: C3 17 05        JP      $0517               ; {}
0BAF: FE FF           CP      $FF                 
0BB1: C2 17 05        JP      NZ,$0517            ; {}
0BB4: 21 58 86        LD      HL,$8658            
0BB7: 36 03           LD      (HL),$03            
0BB9: C3 17 05        JP      $0517               ; {}
0BBC: C3 00 17        JP      $1700               ; {}
0BBF: 21 58 86        LD      HL,$8658            
0BC2: 36 07           LD      (HL),$07            
0BC4: C3 17 05        JP      $0517               ; {}
0BC7: 3A 76 86        LD      A,($8676)           
0BCA: FE 80           CP      $80                 
0BCC: CA 5F 01        JP      Z,$015F             ; {}
0BCF: FE 90           CP      $90                 
0BD1: C2 17 05        JP      NZ,$0517            ; {}
0BD4: 21 58 86        LD      HL,$8658            
0BD7: 36 08           LD      (HL),$08            
0BD9: C3 5F 07        JP      $075F               ; {}
0BDC: 21 5E 86        LD      HL,$865E            
0BDF: 35              DEC     (HL)                
0BE0: C2 17 05        JP      NZ,$0517            ; {}
0BE3: 21 58 86        LD      HL,$8658            
0BE6: 36 09           LD      (HL),$09            
0BE8: C3 17 05        JP      $0517               ; {}
0BEB: 21 58 86        LD      HL,$8658            
0BEE: 36 00           LD      (HL),$00            
0BF0: C3 17 05        JP      $0517               ; {}
0BF3: C3 17 05        JP      $0517               ; {}
0BF6: 13              INC     DE                  
0BF7: 68              LD      L,B                 
0BF8: 12              LD      (DE),A              
0BF9: 20 11           JR      NZ,$1247            ; {}
0BFB: 58              LD      E,B                 
0BFC: 10 20           DJNZ    $1256               ; {}
0BFE: 11 09 13        LD      DE,$1309            
0C01: 01 20 00        LD      BC,$0020            
0C04: 00              NOP                         
0C05: 78              LD      A,B                 
0C06: 10 28           DJNZ    $125E               ; {}
0C08: 00              NOP                         
0C09: 10 10           DJNZ    $1246               ; {}
0C0B: 20 00           JR      NZ,$1236            ; {}
0C0D: FA 00 80        JP      M,$8000             
0C10: 10 20           DJNZ    $1256               ; {}
0C12: 00              NOP                         
0C13: 10 10           DJNZ    $1246               ; {}
0C15: 20 00           JR      NZ,$1236            ; {}
0C17: FA 00 88        JP      M,$8800             
0C1A: 10 18           DJNZ    $124E               ; {}
0C1C: 00              NOP                         
0C1D: 10 10           DJNZ    $1246               ; {}
0C1F: 20 00           JR      NZ,$1236            ; {}
0C21: FA 00 90        JP      M,$9000             
0C24: 10 10           DJNZ    $1246               ; {}
0C26: 00              NOP                         
0C27: 10 10           DJNZ    $1246               ; {}
0C29: 20 00           JR      NZ,$1236            ; {}
0C2B: FA 00 68        JP      M,$6800             
0C2E: 10 38           DJNZ    $126E               ; {}
0C30: 31 02 30        LD      SP,$3002            
0C33: 02              LD      (BC),A              
0C34: 31 02 30        LD      SP,$3002            
0C37: 02              LD      (BC),A              
0C38: 31 02 21        LD      SP,$2102            
0C3B: 01 22 01        LD      BC,$0122            
0C3E: 23              INC     HL                  
0C3F: 03              INC     BC                  
0C40: 20 01           JR      NZ,$1237            ; {}
0C42: 30 01           JR      NC,$1237            ; {}
0C44: 10 1F           DJNZ    $1255               ; {}
0C46: 00              NOP                         
0C47: FA 00 B0        JP      M,$B000             
0C4A: 10 20           DJNZ    $1256               ; {}
0C4C: 00              NOP                         
0C4D: FA 40 3A        JP      M,$3A40             
0C50: 6F              LD      L,A                 
0C51: 86              ADD     A,(HL)              
0C52: E6 F0           AND     $F0                 
0C54: FE 20           CP      $20                 
0C56: 20 06           JR      NZ,$123C            ; {}
0C58: 21 58 86        LD      HL,$8658            
0C5B: 36 01           LD      (HL),$01            
0C5D: C9              RET                         
0C5E: FE 10           CP      $10                 
0C60: C0              RET     NZ                  
0C61: 3A AE 85        LD      A,($85AE)           
0C64: 32 AF 85        LD      ($85AF),A           
0C67: 21 22 98        LD      HL,$9822            
0C6A: 11 22 99        LD      DE,$9922            
0C6D: 3A 6F 86        LD      A,($866F)           
0C70: E6 03           AND     $03                 
0C72: 20 15           JR      NZ,$124B            ; {}
0C74: 36 00           LD      (HL),$00            
0C76: AF              XOR     A                   
0C77: 12              LD      (DE),A              
0C78: 21 A3 98        LD      HL,$98A3            
0C7B: 35              DEC     (HL)                
0C7C: 35              DEC     (HL)                
0C7D: AF              XOR     A                   
0C7E: 32 AE 85        LD      ($85AE),A           
0C81: 3E 04           LD      A,$04               
0C83: 32 8B 80        LD      ($808B),A           
0C86: C3 D4 0C        JP      $0CD4               ; {}
0C89: FE 01           CP      $01                 
0C8B: 20 15           JR      NZ,$124B            ; {}
0C8D: 36 02           LD      (HL),$02            
0C8F: AF              XOR     A                   
0C90: 12              LD      (DE),A              
0C91: 21 A2 98        LD      HL,$98A2            
0C94: 34              INC     (HL)                
0C95: 34              INC     (HL)                
0C96: 3E 02           LD      A,$02               
0C98: 32 AE 85        LD      ($85AE),A           
0C9B: 3E 05           LD      A,$05               
0C9D: 32 6B 83        LD      ($836B),A           
0CA0: 18 32           JR      $1268               ; {}
0CA2: FE 02           CP      $02                 
0CA4: 20 1F           JR      NZ,$1255            ; {}
0CA6: 36 00           LD      (HL),$00            
0CA8: 3E 01           LD      A,$01               
0CAA: 12              LD      (DE),A              
0CAB: 21 A3 98        LD      HL,$98A3            
0CAE: 34              INC     (HL)                
0CAF: 34              INC     (HL)                
0CB0: 3E 04           LD      A,$04               
0CB2: 32 AE 85        LD      ($85AE),A           
0CB5: 3E 8C           LD      A,$8C               
0CB7: 32 63 83        LD      ($8363),A           
0CBA: 32 43 83        LD      ($8343),A           
0CBD: 32 62 83        LD      ($8362),A           
0CC0: 32 42 83        LD      ($8342),A           
0CC3: 18 0F           JR      $1245               ; {}
0CC5: 36 02           LD      (HL),$02            
0CC7: 3E 02           LD      A,$02               
0CC9: 12              LD      (DE),A              
0CCA: 21 A2 98        LD      HL,$98A2            
0CCD: 35              DEC     (HL)                
0CCE: 35              DEC     (HL)                
0CCF: 3E 06           LD      A,$06               
0CD1: 32 AE 85        LD      ($85AE),A           
0CD4: 3A A3 98        LD      A,($98A3)           
0CD7: FE 10           CP      $10                 
0CD9: 20 07           JR      NZ,$123D            ; {}
0CDB: 21 22 98        LD      HL,$9822            
0CDE: 34              INC     (HL)                
0CDF: 34              INC     (HL)                
0CE0: 34              INC     (HL)                
0CE1: 34              INC     (HL)                
0CE2: 21 76 86        LD      HL,$8676            
0CE5: 34              INC     (HL)                
0CE6: CB 46           BIT     0,(HL)              
0CE8: C0              RET     NZ                  
0CE9: 21 22 98        LD      HL,$9822            
0CEC: 34              INC     (HL)                
0CED: C9              RET                         
0CEE: 3A 70 86        LD      A,($8670)           
0CF1: 21 E4 98        LD      HL,$98E4            
0CF4: 11 64 98        LD      DE,$9864            
0CF7: CD 2F 0D        CALL    $0D2F               ; {}
0CFA: C9              RET                         
0CFB: 3A 72 86        LD      A,($8672)           
0CFE: 21 D4 98        LD      HL,$98D4            
0D01: 11 54 98        LD      DE,$9854            
0D04: CD 47 0D        CALL    $0D47               ; {}
0D07: C9              RET                         
0D08: 3A 73 86        LD      A,($8673)           
0D0B: 21 D6 98        LD      HL,$98D6            
0D0E: 11 56 98        LD      DE,$9856            
0D11: CD 47 0D        CALL    $0D47               ; {}
0D14: C9              RET                         
0D15: 3A 74 86        LD      A,($8674)           
0D18: 21 D8 98        LD      HL,$98D8            
0D1B: 11 58 98        LD      DE,$9858            
0D1E: CD 47 0D        CALL    $0D47               ; {}
0D21: C9              RET                         
0D22: 3A 75 86        LD      A,($8675)           
0D25: 21 DA 98        LD      HL,$98DA            
0D28: 11 5A 98        LD      DE,$985A            
0D2B: CD 47 0D        CALL    $0D47               ; {}
0D2E: C9              RET                         
0D2F: F5              PUSH    AF                  
0D30: 3E 21           LD      A,$21               
0D32: 12              LD      (DE),A              
0D33: 01 77 86        LD      BC,$8677            
0D36: 0A              LD      A,(BC)              
0D37: 3C              INC     A                   
0D38: 02              LD      (BC),A              
0D39: E6 07           AND     $07                 
0D3B: FE 02           CP      $02                 
0D3D: 30 03           JR      NC,$1239            ; {}
0D3F: 1A              LD      A,(DE)              
0D40: 3D              DEC     A                   
0D41: 12              LD      (DE),A              
0D42: F1              POP     AF                  
0D43: CD 47 0D        CALL    $0D47               ; {}
0D46: C9              RET                         
0D47: E6 F0           AND     $F0                 
0D49: C8              RET     Z                   
0D4A: 35              DEC     (HL)                
0D4B: 35              DEC     (HL)                
0D4C: C9              RET                         
0D4D: 21 6C 98        LD      HL,$986C            
0D50: 36 24           LD      (HL),$24            
0D52: 11 78 86        LD      DE,$8678            
0D55: 1A              LD      A,(DE)              
0D56: 3C              INC     A                   
0D57: 12              LD      (DE),A              
0D58: CB 57           BIT     2,A                 
0D5A: 20 01           JR      NZ,$1237            ; {}
0D5C: 34              INC     (HL)                
0D5D: 3A 71 86        LD      A,($8671)           
0D60: E6 F0           AND     $F0                 
0D62: C8              RET     Z                   
0D63: FE 10           CP      $10                 
0D65: 20 06           JR      NZ,$123C            ; {}
0D67: 21 EC 98        LD      HL,$98EC            
0D6A: 35              DEC     (HL)                
0D6B: 35              DEC     (HL)                
0D6C: C9              RET                         
0D6D: FE 30           CP      $30                 
0D6F: 20 10           JR      NZ,$1246            ; {}
0D71: 3A 71 86        LD      A,($8671)           
0D74: 21 6D 98        LD      HL,$986D            
0D77: CB 47           BIT     0,A                 
0D79: 20 03           JR      NZ,$1239            ; {}
0D7B: 36 02           LD      (HL),$02            
0D7D: C9              RET                         
0D7E: 36 0C           LD      (HL),$0C            
0D80: C9              RET                         
0D81: DD 21 A4 98     LD      IX,$98A4            
0D85: 3A EC 98        LD      A,($98EC)           
0D88: D6 10           SUB     $10                 
0D8A: DD 77 00        LD      (IX+$00),A          
0D8D: D6 10           SUB     $10                 
0D8F: DD 77 02        LD      (IX+$02),A          
0D92: D6 10           SUB     $10                 
0D94: DD 77 04        LD      (IX+$04),A          
0D97: 3A ED 98        LD      A,($98ED)           
0D9A: DD 77 01        LD      (IX+$01),A          
0D9D: DD 77 03        LD      (IX+$03),A          
0DA0: DD 77 05        LD      (IX+$05),A          
0DA3: DD 21 24 98     LD      IX,$9824            
0DA7: 3A 71 86        LD      A,($8671)           
0DAA: E6 0F           AND     $0F                 
0DAC: 20 1A           JR      NZ,$1250            ; {}
0DAE: 3E 32           LD      A,$32               
0DB0: DD 77 00        LD      (IX+$00),A          
0DB3: DD 77 02        LD      (IX+$02),A          
0DB6: DD 77 04        LD      (IX+$04),A          
0DB9: DD 21 A4 98     LD      IX,$98A4            
0DBD: 06 06           LD      B,$06               
0DBF: DD 36 00 00     LD      (IX+$00),$00        
0DC3: DD 23           INC     IX                  
0DC5: 10 F8           DJNZ    $122E               ; {}
0DC7: C9              RET                         
0DC8: FE 01           CP      $01                 
0DCA: 20 0E           JR      NZ,$1244            ; {}
0DCC: 3E 2C           LD      A,$2C               
0DCE: DD 77 00        LD      (IX+$00),A          
0DD1: 3E 32           LD      A,$32               
0DD3: DD 77 02        LD      (IX+$02),A          
0DD6: DD 77 04        LD      (IX+$04),A          
0DD9: C9              RET                         
0DDA: FE 02           CP      $02                 
0DDC: 20 0F           JR      NZ,$1245            ; {}
0DDE: 3E 2D           LD      A,$2D               
0DE0: DD 77 00        LD      (IX+$00),A          
0DE3: 3C              INC     A                   
0DE4: DD 77 02        LD      (IX+$02),A          
0DE7: 3E 32           LD      A,$32               
0DE9: DD 77 04        LD      (IX+$04),A          
0DEC: C9              RET                         
0DED: 3E 2F           LD      A,$2F               
0DEF: DD 77 00        LD      (IX+$00),A          
0DF2: 3C              INC     A                   
0DF3: DD 77 02        LD      (IX+$02),A          
0DF6: 3C              INC     A                   
0DF7: DD 77 04        LD      (IX+$04),A          
0DFA: C9              RET                         
0DFB: FE 06           CP      $06                 
0DFD: DA 17 05        JP      C,$0517             ; {}
0E00: FE 17           CP      $17                 
0E02: 30 10           JR      NC,$1246            ; {}
0E04: 3A 76 86        LD      A,($8676)           
0E07: CB 47           BIT     0,A                 
0E09: CA 17 05        JP      Z,$0517             ; {}
0E0C: 0E FF           LD      C,$FF               
0E0E: CD 2E 0E        CALL    $0E2E               ; {}
0E11: C3 17 05        JP      $0517               ; {}
0E14: FE 1A           CP      $1A                 
0E16: DA 17 05        JP      C,$0517             ; {}
0E19: FE 29           CP      $29                 
0E1B: D2 17 05        JP      NC,$0517            ; {}
0E1E: 3A 76 86        LD      A,($8676)           
0E21: CB 47           BIT     0,A                 
0E23: CA 17 05        JP      Z,$0517             ; {}
0E26: 0E 01           LD      C,$01               
0E28: CD 2E 0E        CALL    $0E2E               ; {}
0E2B: C3 17 05        JP      $0517               ; {}
0E2E: 21 C1 98        LD      HL,$98C1            
0E31: 06 0A           LD      B,$0A               
0E33: 7E              LD      A,(HL)              
0E34: 81              ADD     A,C                 
0E35: 77              LD      (HL),A              
0E36: 23              INC     HL                  
0E37: 23              INC     HL                  
0E38: 10 F9           DJNZ    $122F               ; {}
0E3A: C9              RET                         
0E3B: EB              EX      DE,HL               
0E3C: D5              PUSH    DE                  
0E3D: DD E1           POP     IX                  
0E3F: 11 20 00        LD      DE,$0020            
0E42: DD 7E 00        LD      A,(IX+$00)          
0E45: DD 23           INC     IX                  
0E47: 77              LD      (HL),A              
0E48: 19              ADD     HL,DE               
0E49: 10 F7           DJNZ    $122D               ; {}
0E4B: C9              RET                         
0E4C: 21 80 98        LD      HL,$9880            
0E4F: 11 80 93        LD      DE,$9380            
0E52: 06 40           LD      B,$40               
0E54: 3A F0 87        LD      A,($87F0)           
0E57: CB 5F           BIT     3,A                 
0E59: C0              RET     NZ                  
0E5A: 3A 00 84        LD      A,($8400)           
0E5D: CB 4F           BIT     1,A                 
0E5F: 28 06           JR      Z,$123C             ; {}
0E61: CB 57           BIT     2,A                 
0E63: 28 02           JR      Z,$1238             ; {}
0E65: 18 0D           JR      $1243               ; {}
0E67: 7E              LD      A,(HL)              
0E68: 12              LD      (DE),A              
0E69: 23              INC     HL                  
0E6A: 13              INC     DE                  
0E6B: 7E              LD      A,(HL)              
0E6C: C6 37           ADD     $37                 
0E6E: 12              LD      (DE),A              
0E6F: 23              INC     HL                  
0E70: 13              INC     DE                  
0E71: 10 F4           DJNZ    $122A               ; {}
0E73: C9              RET                         
0E74: 3E F2           LD      A,$F2               
0E76: 96              SUB     (HL)                
0E77: 12              LD      (DE),A              
0E78: 13              INC     DE                  
0E79: 23              INC     HL                  
0E7A: 3E 27           LD      A,$27               
0E7C: 96              SUB     (HL)                
0E7D: 12              LD      (DE),A              
0E7E: 23              INC     HL                  
0E7F: 13              INC     DE                  
0E80: 10 F2           DJNZ    $1228               ; {}
0E82: C9              RET                         
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
0FFF: FF              RST     0X38                
1000: 3A 85 87        LD      A,($8785)           
1003: CB 7F           BIT     7,A                 
1005: 20 07           JR      NZ,$123D            ; {}
1007: 3A 57 86        LD      A,($8657)           
100A: CB 4F           BIT     1,A                 
100C: 28 05           JR      Z,$123B             ; {}
100E: 21 70 89        LD      HL,$8970            
1011: 18 03           JR      $1239               ; {}
1013: 21 B0 85        LD      HL,$85B0            
1016: 7E              LD      A,(HL)              
1017: E6 0E           AND     $0E                 
1019: E5              PUSH    HL                  
101A: 7E              LD      A,(HL)              
101B: E6 0F           AND     $0F                 
101D: FE 08           CP      $08                 
101F: 20 07           JR      NZ,$123D            ; {}
1021: 21 AE 85        LD      HL,$85AE            
1024: CB F6           SET     6,(HL)              
1026: E1              POP     HL                  
1027: C9              RET                         
1028: 21 AE 85        LD      HL,$85AE            
102B: 7E              LD      A,(HL)              
102C: 23              INC     HL                  
102D: E6 3F           AND     $3F                 
102F: 77              LD      (HL),A              
1030: E1              POP     HL                  
1031: 7E              LD      A,(HL)              
1032: E6 3F           AND     $3F                 
1034: 32 AE 85        LD      ($85AE),A           
1037: E6 0F           AND     $0F                 
1039: 6F              LD      L,A                 
103A: 3A AF 85        LD      A,($85AF)           
103D: E6 0F           AND     $0F                 
103F: BD              CP      L                   
1040: 20 06           JR      NZ,$123C            ; {}
1042: 21 AE 85        LD      HL,$85AE            
1045: CB BE           RES     7,(HL)              
1047: C9              RET                         
1048: 21 AE 85        LD      HL,$85AE            
104B: CB FE           SET     7,(HL)              
104D: C9              RET                         
104E: 21 01 84        LD      HL,$8401            
1051: CB 5E           BIT     3,(HL)              
1053: 28 30           JR      Z,$1266             ; {}
1055: 21 AE 85        LD      HL,$85AE            
1058: 7E              LD      A,(HL)              
1059: 21 22 98        LD      HL,$9822            
105C: 11 22 99        LD      DE,$9922            
105F: E6 0F           AND     $0F                 
1061: 28 0D           JR      Z,$1243             ; {}
1063: FE 04           CP      $04                 
1065: 28 0E           JR      Z,$1244             ; {}
1067: FE 02           CP      $02                 
1069: 28 10           JR      Z,$1246             ; {}
106B: FE 06           CP      $06                 
106D: 28 10           JR      Z,$1246             ; {}
106F: C9              RET                         
1070: 36 10           LD      (HL),$10            
1072: AF              XOR     A                   
1073: 12              LD      (DE),A              
1074: C9              RET                         
1075: 36 10           LD      (HL),$10            
1077: 3E 01           LD      A,$01               
1079: 12              LD      (DE),A              
107A: C9              RET                         
107B: 36 11           LD      (HL),$11            
107D: 18 F3           JR      $1229               ; {}
107F: 36 11           LD      (HL),$11            
1081: 3E 02           LD      A,$02               
1083: 12              LD      (DE),A              
1084: C9              RET                         
1085: 21 AE 85        LD      HL,$85AE            
1088: 7E              LD      A,(HL)              
1089: 21 22 98        LD      HL,$9822            
108C: 11 22 99        LD      DE,$9922            
108F: 01 00 00        LD      BC,$0000            
1092: E6 0F           AND     $0F                 
1094: 28 13           JR      Z,$1249             ; {}
1096: 03              INC     BC                  
1097: FE 04           CP      $04                 
1099: 28 0E           JR      Z,$1244             ; {}
109B: 01 00 02        LD      BC,$0200            
109E: FE 02           CP      $02                 
10A0: 28 07           JR      Z,$123D             ; {}
10A2: 03              INC     BC                  
10A3: 03              INC     BC                  
10A4: FE 06           CP      $06                 
10A6: 28 01           JR      Z,$1237             ; {}
10A8: C9              RET                         
10A9: 70              LD      (HL),B              
10AA: 79              LD      A,C                 
10AB: 12              LD      (DE),A              
10AC: 3A 01 84        LD      A,($8401)           
10AF: CB 67           BIT     4,A                 
10B1: C8              RET     Z                   
10B2: 34              INC     (HL)                
10B3: 34              INC     (HL)                
10B4: 34              INC     (HL)                
10B5: 34              INC     (HL)                
10B6: C9              RET                         
10B7: 3A AE 85        LD      A,($85AE)           
10BA: E6 0F           AND     $0F                 
10BC: 20 1A           JR      NZ,$1250            ; {}
10BE: 3E 02           LD      A,$02               
10C0: 32 AE 85        LD      ($85AE),A           
10C3: CD 4E 10        CALL    $104E               ; {}
10C6: C9              RET                         
10C7: CD 00 10        CALL    $1000               ; {}
10CA: AF              XOR     A                   
10CB: 32 A0 98        LD      ($98A0),A           
10CE: 32 A1 98        LD      ($98A1),A           
10D1: 3A A3 98        LD      A,($98A3)           
10D4: FE 08           CP      $08                 
10D6: 28 DF           JR      Z,$1215             ; {}
10D8: CD 1F 11        CALL    $111F               ; {}
10DB: CD 8F 11        CALL    $118F               ; {}
10DE: CD EA 11        CALL    $11EA               ; {}
10E1: 21 AE 85        LD      HL,$85AE            
10E4: 7E              LD      A,(HL)              
10E5: E6 0F           AND     $0F                 
10E7: FE 08           CP      $08                 
10E9: 28 47           JR      Z,$127D             ; {}
10EB: 7E              LD      A,(HL)              
10EC: CB 76           BIT     6,(HL)              
10EE: 20 42           JR      NZ,$1278            ; {}
10F0: 3A B3 85        LD      A,($85B3)           
10F3: 21 B1 85        LD      HL,$85B1            
10F6: 96              SUB     (HL)                
10F7: 32 B3 85        LD      ($85B3),A           
10FA: D0              RET     NC                  
10FB: 3A AE 85        LD      A,($85AE)           
10FE: CB 7F           BIT     7,A                 
1100: 28 04           JR      Z,$123A             ; {}
1102: CD 4E 10        CALL    $104E               ; {}
1105: C9              RET                         
1106: CD 4E 10        CALL    $104E               ; {}
1109: 21 B2 85        LD      HL,$85B2            
110C: 34              INC     (HL)                
110D: CB 46           BIT     0,(HL)              
110F: 28 04           JR      Z,$123A             ; {}
1111: 21 22 98        LD      HL,$9822            
1114: 34              INC     (HL)                
1115: 3A 01 84        LD      A,($8401)           
1118: CB 57           BIT     2,A                 
111A: C0              RET     NZ                  
111B: CD 36 11        CALL    $1136               ; {}
111E: C9              RET                         
111F: 3A 01 84        LD      A,($8401)           
1122: CB 67           BIT     4,A                 
1124: 20 06           JR      NZ,$123C            ; {}
1126: 3E 40           LD      A,$40               
1128: 32 B1 85        LD      ($85B1),A           
112B: C9              RET                         
112C: 3E 50           LD      A,$50               
112E: 32 B1 85        LD      ($85B1),A           
1131: C9              RET                         
1132: CD 4E 10        CALL    $104E               ; {}
1135: C9              RET                         
1136: 21 AE 85        LD      HL,$85AE            
1139: 7E              LD      A,(HL)              
113A: 21 A3 98        LD      HL,$98A3            
113D: E6 0F           AND     $0F                 
113F: 28 25           JR      Z,$125B             ; {}
1141: FE 04           CP      $04                 
1143: 28 13           JR      Z,$1249             ; {}
1145: 2B              DEC     HL                  
1146: FE 02           CP      $02                 
1148: 28 0E           JR      Z,$1244             ; {}
114A: FE 06           CP      $06                 
114C: 28 18           JR      Z,$124E             ; {}
114E: C9              RET                         
114F: 3A A3 98        LD      A,($98A3)           
1152: 5F              LD      E,A                 
1153: 3A A2 98        LD      A,($98A2)           
1156: 57              LD      D,A                 
1157: C9              RET                         
1158: 34              INC     (HL)                
1159: 34              INC     (HL)                
115A: CD 4F 11        CALL    $114F               ; {}
115D: CD 74 11        CALL    $1174               ; {}
1160: CB 49           BIT     1,C                 
1162: C8              RET     Z                   
1163: 35              DEC     (HL)                
1164: 35              DEC     (HL)                
1165: C9              RET                         
1166: 35              DEC     (HL)                
1167: 35              DEC     (HL)                
1168: CD 4F 11        CALL    $114F               ; {}
116B: CD 74 11        CALL    $1174               ; {}
116E: CB 49           BIT     1,C                 
1170: C8              RET     Z                   
1171: 34              INC     (HL)                
1172: 34              INC     (HL)                
1173: C9              RET                         
1174: F5              PUSH    AF                  
1175: CB 89           RES     1,C                 
1177: 7A              LD      A,D                 
1178: FE 11           CP      $11                 
117A: 38 0F           JR      C,$1245             ; {}
117C: FE E2           CP      $E2                 
117E: 30 0B           JR      NC,$1241            ; {}
1180: 7B              LD      A,E                 
1181: FE 08           CP      $08                 
1183: 38 06           JR      C,$123C             ; {}
1185: FE F1           CP      $F1                 
1187: 30 02           JR      NC,$1238            ; {}
1189: F1              POP     AF                  
118A: C9              RET                         
118B: CB C9           SET     1,C                 
118D: F1              POP     AF                  
118E: C9              RET                         
118F: E5              PUSH    HL                  
1190: C5              PUSH    BC                  
1191: 21 AE 85        LD      HL,$85AE            
1194: 7E              LD      A,(HL)              
1195: E6 0F           AND     $0F                 
1197: 28 04           JR      Z,$123A             ; {}
1199: FE 04           CP      $04                 
119B: 20 0B           JR      NZ,$1241            ; {}
119D: 3A A2 98        LD      A,($98A2)           
11A0: E6 0F           AND     $0F                 
11A2: FE 01           CP      $01                 
11A4: 28 26           JR      Z,$125C             ; {}
11A6: 18 19           JR      $124F               ; {}
11A8: FE 02           CP      $02                 
11AA: 28 04           JR      Z,$123A             ; {}
11AC: FE 06           CP      $06                 
11AE: 20 1C           JR      NZ,$1252            ; {}
11B0: 3A A3 98        LD      A,($98A3)           
11B3: FE 20           CP      $20                 
11B5: 30 06           JR      NC,$123C            ; {}
11B7: FE 08           CP      $08                 
11B9: 28 11           JR      Z,$1247             ; {}
11BB: 18 04           JR      $123A               ; {}
11BD: E6 0F           AND     $0F                 
11BF: 28 0B           JR      Z,$1241             ; {}
11C1: 23              INC     HL                  
11C2: 7E              LD      A,(HL)              
11C3: E6 0F           AND     $0F                 
11C5: 2B              DEC     HL                  
11C6: 77              LD      (HL),A              
11C7: CB 87           RES     0,A                 
11C9: C1              POP     BC                  
11CA: E1              POP     HL                  
11CB: C9              RET                         
11CC: 3A 57 86        LD      A,($8657)           
11CF: CB 4F           BIT     1,A                 
11D1: 20 13           JR      NZ,$1249            ; {}
11D3: 3A AE 85        LD      A,($85AE)           
11D6: E6 0F           AND     $0F                 
11D8: 4F              LD      C,A                 
11D9: 3A AF 85        LD      A,($85AF)           
11DC: E6 0F           AND     $0F                 
11DE: B9              CP      C                   
11DF: 28 05           JR      Z,$123B             ; {}
11E1: 21 B3 85        LD      HL,$85B3            
11E4: 36 02           LD      (HL),$02            
11E6: CB C7           SET     0,A                 
11E8: 18 DF           JR      $1215               ; {}
11EA: 3A AE 85        LD      A,($85AE)           
11ED: 21 A2 98        LD      HL,$98A2            
11F0: 11 E1 85        LD      DE,$85E1            
11F3: E6 0F           AND     $0F                 
11F5: 28 0D           JR      Z,$1243             ; {}
11F7: FE 04           CP      $04                 
11F9: 28 13           JR      Z,$1249             ; {}
11FB: FE 02           CP      $02                 
11FD: 28 19           JR      Z,$124F             ; {}
11FF: FE 06           CP      $06                 
1201: 28 1F           JR      Z,$1255             ; {}
1203: C9              RET                         
1204: 7E              LD      A,(HL)              
1205: 12              LD      (DE),A              
1206: 23              INC     HL                  
1207: 1B              DEC     DE                  
1208: 7E              LD      A,(HL)              
1209: D6 10           SUB     $10                 
120B: 12              LD      (DE),A              
120C: 18 1C           JR      $1252               ; {}
120E: 7E              LD      A,(HL)              
120F: 12              LD      (DE),A              
1210: 23              INC     HL                  
1211: 1B              DEC     DE                  
1212: 7E              LD      A,(HL)              
1213: C6 10           ADD     $10                 
1215: 12              LD      (DE),A              
1216: 18 12           JR      $1248               ; {}
1218: 7E              LD      A,(HL)              
1219: C6 10           ADD     $10                 
121B: 12              LD      (DE),A              
121C: 23              INC     HL                  
121D: 1B              DEC     DE                  
121E: 7E              LD      A,(HL)              
121F: 12              LD      (DE),A              
1220: 18 08           JR      $123E               ; {}
1222: 7E              LD      A,(HL)              
1223: D6 10           SUB     $10                 
1225: 12              LD      (DE),A              
1226: 23              INC     HL                  
1227: 1B              DEC     DE                  
1228: 7E              LD      A,(HL)              
1229: 12              LD      (DE),A              
122A: 21 65 84        LD      HL,$8465            
122D: 06 08           LD      B,$08               
122F: 11 08 00        LD      DE,$0008            
1232: E5              PUSH    HL                  
1233: 3A E1 85        LD      A,($85E1)           
1236: BE              CP      (HL)                
1237: 20 0E           JR      NZ,$1244            ; {}
1239: 3A E0 85        LD      A,($85E0)           
123C: 23              INC     HL                  
123D: BE              CP      (HL)                
123E: 20 07           JR      NZ,$123D            ; {}
1240: E1              POP     HL                  
1241: 21 01 84        LD      HL,$8401            
1244: CB D6           SET     2,(HL)              
1246: C9              RET                         
1247: 21 01 84        LD      HL,$8401            
124A: CB 96           RES     2,(HL)              
124C: E1              POP     HL                  
124D: 19              ADD     HL,DE               
124E: 10 E2           DJNZ    $1218               ; {}
1250: C9              RET                         
1251: 3A 57 86        LD      A,($8657)           
1254: CB 4F           BIT     1,A                 
1256: 28 1C           JR      Z,$1252             ; {}
1258: 21 28 85        LD      HL,$8528            
125B: 11 10 00        LD      DE,$0010            
125E: 06 08           LD      B,$08               
1260: 0E 08           LD      C,$08               
1262: CB 7E           BIT     7,(HL)              
1264: 28 01           JR      Z,$1237             ; {}
1266: 0D              DEC     C                   
1267: 19              ADD     HL,DE               
1268: 10 F8           DJNZ    $122E               ; {}
126A: 79              LD      A,C                 
126B: FE 01           CP      $01                 
126D: 20 05           JR      NZ,$123B            ; {}
126F: 21 76 86        LD      HL,$8676            
1272: 36 90           LD      (HL),$90            
1274: 2A 25 86        LD      HL,($8625)          
1277: 11 60 09        LD      DE,$0960            
127A: A7              AND     A                   
127B: ED 52           SBC     HL,DE               
127D: 20 05           JR      NZ,$123B            ; {}
127F: 21 53 86        LD      HL,$8653            
1282: CB CE           SET     1,(HL)              
1284: 2A 25 86        LD      HL,($8625)          
1287: 7C              LD      A,H                 
1288: A7              AND     A                   
1289: 20 27           JR      NZ,$125D            ; {}
128B: 7D              LD      A,L                 
128C: FE 96           CP      $96                 
128E: 28 0A           JR      Z,$1240             ; {}
1290: A7              AND     A                   
1291: 20 1F           JR      NZ,$1255            ; {}
1293: 21 46 86        LD      HL,$8646            
1296: CB DE           SET     3,(HL)              
1298: 18 1C           JR      $1252               ; {}
129A: 3A 4A 86        LD      A,($864A)           
129D: CB 6F           BIT     5,A                 
129F: 20 11           JR      NZ,$1247            ; {}
12A1: CB EF           SET     5,A                 
12A3: 32 4A 86        LD      ($864A),A           
12A6: 3A F0 87        LD      A,($87F0)           
12A9: CB 47           BIT     0,A                 
12AB: 20 05           JR      NZ,$123B            ; {}
12AD: 3E 01           LD      A,$01               
12AF: 32 89 9A        LD      ($9A89),A           
12B2: 2B              DEC     HL                  
12B3: 22 25 86        LD      ($8625),HL          
12B6: 21 4A 86        LD      HL,$864A            
12B9: CB 66           BIT     4,(HL)              
12BB: C0              RET     NZ                  
12BC: 21 28 85        LD      HL,$8528            
12BF: 06 08           LD      B,$08               
12C1: 0E 08           LD      C,$08               
12C3: 11 10 00        LD      DE,$0010            
12C6: CB 7E           BIT     7,(HL)              
12C8: 28 01           JR      Z,$1237             ; {}
12CA: 0D              DEC     C                   
12CB: 19              ADD     HL,DE               
12CC: 10 F8           DJNZ    $122E               ; {}
12CE: 79              LD      A,C                 
12CF: A7              AND     A                   
12D0: C8              RET     Z                   
12D1: 21 00 84        LD      HL,$8400            
12D4: 3A 0D 84        LD      A,($840D)           
12D7: CB 4E           BIT     1,(HL)              
12D9: 28 03           JR      Z,$1239             ; {}
12DB: 3A 0E 84        LD      A,($840E)           
12DE: 06 02           LD      B,$02               
12E0: FE 04           CP      $04                 
12E2: 38 1B           JR      C,$1251             ; {}
12E4: 04              INC     B                   
12E5: FE 08           CP      $08                 
12E7: 38 16           JR      C,$124C             ; {}
12E9: 04              INC     B                   
12EA: FE 0C           CP      $0C                 
12EC: 38 11           JR      C,$1247             ; {}
12EE: 04              INC     B                   
12EF: FE 10           CP      $10                 
12F1: 38 0C           JR      C,$1242             ; {}
12F3: 04              INC     B                   
12F4: FE 14           CP      $14                 
12F6: 38 07           JR      C,$123D             ; {}
12F8: 04              INC     B                   
12F9: FE 18           CP      $18                 
12FB: 38 02           JR      C,$1238             ; {}
12FD: 18 03           JR      $1239               ; {}
12FF: 79              LD      A,C                 
1300: B8              CP      B                   
1301: D0              RET     NC                  
1302: 21 04 01        LD      HL,$0104            
1305: 22 25 86        LD      ($8625),HL          
1308: 21 4A 86        LD      HL,$864A            
130B: CB E6           SET     4,(HL)              
130D: C9              RET                         
130E: 2A D6 85        LD      HL,($85D6)          
1311: 22 DE 85        LD      ($85DE),HL          
1314: 3A A2 98        LD      A,($98A2)           
1317: 57              LD      D,A                 
1318: 3A A3 98        LD      A,($98A3)           
131B: 5F              LD      E,A                 
131C: CD 93 13        CALL    $1393               ; {}
131F: CD 53 13        CALL    $1353               ; {}
1322: 2A D6 85        LD      HL,($85D6)          
1325: 3A DE 85        LD      A,($85DE)           
1328: BD              CP      L                   
1329: 20 06           JR      NZ,$123C            ; {}
132B: 3A DF 85        LD      A,($85DF)           
132E: BC              CP      H                   
132F: 28 0C           JR      Z,$1242             ; {}
1331: 3A 46 86        LD      A,($8646)           
1334: CB 47           BIT     0,A                 
1336: C0              RET     NZ                  
1337: CD 0A 14        CALL    $140A               ; {}
133A: CD 0A 14        CALL    $140A               ; {}
133D: 3A 46 86        LD      A,($8646)           
1340: CB 47           BIT     0,A                 
1342: C0              RET     NZ                  
1343: 3A AE 85        LD      A,($85AE)           
1346: E6 07           AND     $07                 
1348: 47              LD      B,A                 
1349: 3A AF 85        LD      A,($85AF)           
134C: E6 07           AND     $07                 
134E: B8              CP      B                   
134F: C4 EF 14        CALL    NZ,$14EF            ; {}
1352: C9              RET                         
1353: 06 00           LD      B,$00               
1355: 2A D6 85        LD      HL,($85D6)          
1358: CD 04 14        CALL    $1404               ; {}
135B: 2A D8 85        LD      HL,($85D8)          
135E: CD 04 14        CALL    $1404               ; {}
1361: 2A DA 85        LD      HL,($85DA)          
1364: CD 04 14        CALL    $1404               ; {}
1367: 2A DC 85        LD      HL,($85DC)          
136A: CD 04 14        CALL    $1404               ; {}
136D: 78              LD      A,B                 
136E: 21 01 84        LD      HL,$8401            
1371: CB A6           RES     4,(HL)              
1373: A7              AND     A                   
1374: C0              RET     NZ                  
1375: CB E6           SET     4,(HL)              
1377: C9              RET                         
1378: CD CB 13        CALL    $13CB               ; {}
137B: DD 21 FA 85     LD      IX,$85FA            
137F: 18 2C           JR      $1262               ; {}
1381: CD CB 13        CALL    $13CB               ; {}
1384: DD 21 02 86     LD      IX,$8602            
1388: 18 23           JR      $1259               ; {}
138A: CD CB 13        CALL    $13CB               ; {}
138D: DD 21 0A 86     LD      IX,$860A            
1391: 18 1A           JR      $1250               ; {}
1393: 3A AE 85        LD      A,($85AE)           
1396: E6 0F           AND     $0F                 
1398: 28 0C           JR      Z,$1242             ; {}
139A: FE 06           CP      $06                 
139C: 28 08           JR      Z,$123E             ; {}
139E: 3E 06           LD      A,$06               
13A0: 82              ADD     A,D                 
13A1: 57              LD      D,A                 
13A2: 3E 06           LD      A,$06               
13A4: 83              ADD     A,E                 
13A5: 5F              LD      E,A                 
13A6: CD CB 13        CALL    $13CB               ; {}
13A9: DD 21 D6 85     LD      IX,$85D6            
13AD: DD 75 00        LD      (IX+$00),L          
13B0: DD 74 01        LD      (IX+$01),H          
13B3: CD FD 13        CALL    $13FD               ; {}
13B6: DD 73 02        LD      (IX+$02),E          
13B9: DD 72 03        LD      (IX+$03),D          
13BC: 23              INC     HL                  
13BD: DD 75 04        LD      (IX+$04),L          
13C0: DD 74 05        LD      (IX+$05),H          
13C3: 13              INC     DE                  
13C4: DD 73 06        LD      (IX+$06),E          
13C7: DD 72 07        LD      (IX+$07),D          
13CA: C9              RET                         
13CB: 7A              LD      A,D                 
13CC: D6 11           SUB     $11                 
13CE: CB 3F           SRL     A                   
13D0: CB 3F           SRL     A                   
13D2: 57              LD      D,A                 
13D3: CB 3F           SRL     A                   
13D5: CB 27           SLA     A                   
13D7: CB 27           SLA     A                   
13D9: CB 27           SLA     A                   
13DB: CB 27           SLA     A                   
13DD: CB 27           SLA     A                   
13DF: 6F              LD      L,A                 
13E0: 7A              LD      A,D                 
13E1: CB 3F           SRL     A                   
13E3: CB 3F           SRL     A                   
13E5: CB 3F           SRL     A                   
13E7: CB 3F           SRL     A                   
13E9: 67              LD      H,A                 
13EA: 16 00           LD      D,$00               
13EC: CB 3B           SRL     E                   
13EE: CB 3B           SRL     E                   
13F0: CB 3B           SRL     E                   
13F2: A7              AND     A                   
13F3: ED 52           SBC     HL,DE               
13F5: EB              EX      DE,HL               
13F6: 21 A0 83        LD      HL,$83A0            
13F9: A7              AND     A                   
13FA: ED 52           SBC     HL,DE               
13FC: C9              RET                         
13FD: 11 E0 FF        LD      DE,$FFE0            
1400: EB              EX      DE,HL               
1401: 19              ADD     HL,DE               
1402: EB              EX      DE,HL               
1403: C9              RET                         
1404: 7E              LD      A,(HL)              
1405: FE 7F           CP      $7F                 
1407: C0              RET     NZ                  
1408: 04              INC     B                   
1409: C9              RET                         
140A: 2A D6 85        LD      HL,($85D6)          
140D: E5              PUSH    HL                  
140E: DD E1           POP     IX                  
1410: ED 4B D8 85     LD      BC,($85D8)          
1414: 2A DA 85        LD      HL,($85DA)          
1417: ED 5B DC 85     LD      DE,($85DC)          
141B: 3A AE 85        LD      A,($85AE)           
141E: E6 0F           AND     $0F                 
1420: 28 10           JR      Z,$1246             ; {}
1422: FE 04           CP      $04                 
1424: CA DC 14        JP      Z,$14DC             ; {}
1427: FE 02           CP      $02                 
1429: CA D4 14        JP      Z,$14D4             ; {}
142C: FE 06           CP      $06                 
142E: CA 85 14        JP      Z,$1485             ; {}
1431: C9              RET                         
1432: 7E              LD      A,(HL)              
1433: FE 08           CP      $08                 
1435: CA E4 14        JP      Z,$14E4             ; {}
1438: FE 09           CP      $09                 
143A: CA E4 14        JP      Z,$14E4             ; {}
143D: FE 0C           CP      $0C                 
143F: 28 1B           JR      Z,$1251             ; {}
1441: FE 8D           CP      $8D                 
1443: 38 04           JR      C,$123A             ; {}
1445: FE 90           CP      $90                 
1447: 38 13           JR      C,$1249             ; {}
1449: FE 8C           CP      $8C                 
144B: 28 0F           JR      Z,$1245             ; {}
144D: FE 7F           CP      $7F                 
144F: CC CB 15        CALL    Z,$15CB             ; {}
1452: FE 7E           CP      $7E                 
1454: 20 04           JR      NZ,$123A            ; {}
1456: 36 8C           LD      (HL),$8C            
1458: 18 02           JR      $1238               ; {}
145A: 36 03           LD      (HL),$03            
145C: 1A              LD      A,(DE)              
145D: FE 08           CP      $08                 
145F: CA E7 14        JP      Z,$14E7             ; {}
1462: FE 09           CP      $09                 
1464: CA E7 14        JP      Z,$14E7             ; {}
1467: FE 0C           CP      $0C                 
1469: C8              RET     Z                   
146A: FE 8D           CP      $8D                 
146C: 38 03           JR      C,$1239             ; {}
146E: FE 90           CP      $90                 
1470: D8              RET     C                   
1471: FE 8C           CP      $8C                 
1473: C8              RET     Z                   
1474: FE 7F           CP      $7F                 
1476: CC CB 15        CALL    Z,$15CB             ; {}
1479: FE 7E           CP      $7E                 
147B: 20 04           JR      NZ,$123A            ; {}
147D: 3E 8C           LD      A,$8C               
147F: 12              LD      (DE),A              
1480: C9              RET                         
1481: 3E 02           LD      A,$02               
1483: 12              LD      (DE),A              
1484: C9              RET                         
1485: 0A              LD      A,(BC)              
1486: FE 02           CP      $02                 
1488: 28 61           JR      Z,$1297             ; {}
148A: FE 03           CP      $03                 
148C: 28 5D           JR      Z,$1293             ; {}
148E: FE 7F           CP      $7F                 
1490: 28 16           JR      Z,$124C             ; {}
1492: FE 0C           CP      $0C                 
1494: 28 18           JR      Z,$124E             ; {}
1496: FE 8C           CP      $8C                 
1498: 28 14           JR      Z,$124A             ; {}
149A: FE 7E           CP      $7E                 
149C: 28 10           JR      Z,$1246             ; {}
149E: FE 8D           CP      $8D                 
14A0: 38 04           JR      C,$123A             ; {}
14A2: FE 90           CP      $90                 
14A4: 38 08           JR      C,$123E             ; {}
14A6: FE 7F           CP      $7F                 
14A8: CC CB 15        CALL    Z,$15CB             ; {}
14AB: 3E 08           LD      A,$08               
14AD: 02              LD      (BC),A              
14AE: 1A              LD      A,(DE)              
14AF: FE 02           CP      $02                 
14B1: 28 34           JR      Z,$126A             ; {}
14B3: FE 03           CP      $03                 
14B5: 28 30           JR      Z,$1266             ; {}
14B7: FE 7F           CP      $7F                 
14B9: 28 12           JR      Z,$1248             ; {}
14BB: FE 0C           CP      $0C                 
14BD: C8              RET     Z                   
14BE: FE 8C           CP      $8C                 
14C0: C8              RET     Z                   
14C1: FE 7E           CP      $7E                 
14C3: C8              RET     Z                   
14C4: FE 8D           CP      $8D                 
14C6: 38 03           JR      C,$1239             ; {}
14C8: FE 90           CP      $90                 
14CA: D8              RET     C                   
14CB: FE 7F           CP      $7F                 
14CD: CC CB 15        CALL    Z,$15CB             ; {}
14D0: 3E 09           LD      A,$09               
14D2: 12              LD      (DE),A              
14D3: C9              RET                         
14D4: DD E5           PUSH    IX                  
14D6: C1              POP     BC                  
14D7: E5              PUSH    HL                  
14D8: D1              POP     DE                  
14D9: C3 85 14        JP      $1485               ; {}
14DC: DD E5           PUSH    IX                  
14DE: E1              POP     HL                  
14DF: C5              PUSH    BC                  
14E0: D1              POP     DE                  
14E1: C3 32 14        JP      $1432               ; {}
14E4: 36 0C           LD      (HL),$0C            
14E6: C9              RET                         
14E7: 3E 0C           LD      A,$0C               
14E9: 12              LD      (DE),A              
14EA: C9              RET                         
14EB: 3E 0C           LD      A,$0C               
14ED: 02              LD      (BC),A              
14EE: C9              RET                         
14EF: CD D3 15        CALL    $15D3               ; {}
14F2: 2A DC 85        LD      HL,($85DC)          
14F5: E5              PUSH    HL                  
14F6: FD E1           POP     IY                  
14F8: 2A DA 85        LD      HL,($85DA)          
14FB: E5              PUSH    HL                  
14FC: DD E1           POP     IX                  
14FE: 2A D6 85        LD      HL,($85D6)          
1501: ED 5B D8 85     LD      DE,($85D8)          
1505: 3A AE 85        LD      A,($85AE)           
1508: E6 0F           AND     $0F                 
150A: 28 0D           JR      Z,$1243             ; {}
150C: FE 02           CP      $02                 
150E: 28 25           JR      Z,$125B             ; {}
1510: FE 04           CP      $04                 
1512: 28 39           JR      Z,$126F             ; {}
1514: FE 06           CP      $06                 
1516: 28 4A           JR      Z,$1280             ; {}
1518: C9              RET                         
1519: DD 7E 00        LD      A,(IX+$00)          
151C: CD 7B 15        CALL    $157B               ; {}
151F: CB 47           BIT     0,A                 
1521: 28 04           JR      Z,$123A             ; {}
1523: DD 36 00 05     LD      (IX+$00),$05        
1527: FD 7E 00        LD      A,(IY+$00)          
152A: CD 7B 15        CALL    $157B               ; {}
152D: CB 47           BIT     0,A                 
152F: C8              RET     Z                   
1530: FD 36 00 04     LD      (IY+$00),$04        
1534: C9              RET                         
1535: 7E              LD      A,(HL)              
1536: CD 7B 15        CALL    $157B               ; {}
1539: CB 47           BIT     0,A                 
153B: 28 02           JR      Z,$1238             ; {}
153D: 36 06           LD      (HL),$06            
153F: DD 7E 00        LD      A,(IX+$00)          
1542: CD 7B 15        CALL    $157B               ; {}
1545: CB 47           BIT     0,A                 
1547: C8              RET     Z                   
1548: DD 36 00 07     LD      (IX+$00),$07        
154C: C9              RET                         
154D: 7E              LD      A,(HL)              
154E: CD 7B 15        CALL    $157B               ; {}
1551: CB 47           BIT     0,A                 
1553: 28 02           JR      Z,$1238             ; {}
1555: 36 01           LD      (HL),$01            
1557: 1A              LD      A,(DE)              
1558: CD 7B 15        CALL    $157B               ; {}
155B: CB 47           BIT     0,A                 
155D: C8              RET     Z                   
155E: 3E 00           LD      A,$00               
1560: 12              LD      (DE),A              
1561: C9              RET                         
1562: 1A              LD      A,(DE)              
1563: CD 7B 15        CALL    $157B               ; {}
1566: CB 47           BIT     0,A                 
1568: 28 03           JR      Z,$1239             ; {}
156A: 3E 0A           LD      A,$0A               
156C: 12              LD      (DE),A              
156D: FD 7E 00        LD      A,(IY+$00)          
1570: CD 7B 15        CALL    $157B               ; {}
1573: CB 47           BIT     0,A                 
1575: C8              RET     Z                   
1576: FD 36 00 0B     LD      (IY+$00),$0B        
157A: C9              RET                         
157B: F5              PUSH    AF                  
157C: 3A 01 84        LD      A,($8401)           
157F: CB 7F           BIT     7,A                 
1581: 20 10           JR      NZ,$1246            ; {}
1583: 3A AE 85        LD      A,($85AE)           
1586: C6 04           ADD     $04                 
1588: E6 07           AND     $07                 
158A: 47              LD      B,A                 
158B: 3A AF 85        LD      A,($85AF)           
158E: E6 07           AND     $07                 
1590: B8              CP      B                   
1591: 20 0B           JR      NZ,$1241            ; {}
1593: F1              POP     AF                  
1594: FE 7F           CP      $7F                 
1596: CC CB 15        CALL    Z,$15CB             ; {}
1599: 28 2D           JR      Z,$1263             ; {}
159B: CB 87           RES     0,A                 
159D: C9              RET                         
159E: F1              POP     AF                  
159F: FE 7F           CP      $7F                 
15A1: CC CB 15        CALL    Z,$15CB             ; {}
15A4: 28 22           JR      Z,$1258             ; {}
15A6: A7              AND     A                   
15A7: 28 1F           JR      Z,$1255             ; {}
15A9: FE 01           CP      $01                 
15AB: 28 1B           JR      Z,$1251             ; {}
15AD: FE 04           CP      $04                 
15AF: 28 17           JR      Z,$124D             ; {}
15B1: FE 05           CP      $05                 
15B3: 28 13           JR      Z,$1249             ; {}
15B5: FE 06           CP      $06                 
15B7: 28 0F           JR      Z,$1245             ; {}
15B9: FE 07           CP      $07                 
15BB: 28 0B           JR      Z,$1241             ; {}
15BD: FE 0A           CP      $0A                 
15BF: 28 07           JR      Z,$123D             ; {}
15C1: FE 0B           CP      $0B                 
15C3: 28 03           JR      Z,$1239             ; {}
15C5: CB 87           RES     0,A                 
15C7: C9              RET                         
15C8: CB C7           SET     0,A                 
15CA: C9              RET                         
15CB: E5              PUSH    HL                  
15CC: 21 56 86        LD      HL,$8656            
15CF: CB D6           SET     2,(HL)              
15D1: E1              POP     HL                  
15D2: C9              RET                         
15D3: 3A A2 98        LD      A,($98A2)           
15D6: 57              LD      D,A                 
15D7: 3A A3 98        LD      A,($98A3)           
15DA: 5F              LD      E,A                 
15DB: 3A AF 85        LD      A,($85AF)           
15DE: C3 96 13        JP      $1396               ; {}
15E1: 38 00           JR      C,$1236             ; {}
15E3: 38 00           JR      C,$1236             ; {}
15E5: 25              DEC     H                   
15E6: 32 00 13        LD      ($1300),A           ; {}
15E9: 38 00           JR      C,$1236             ; {}
15EB: 02              LD      (BC),A              
15EC: 30 00           JR      NC,$1236            ; {}
15EE: 3B              DEC     SP                  
15EF: 10 00           DJNZ    $1236               ; {}
15F1: 01 00 00        LD      BC,$0000            
15F4: 01 10 00        LD      BC,$0010            
15F7: 69              LD      L,C                 
15F8: 30 00           JR      NC,$1236            ; {}
15FA: 3F              CCF                         
15FB: 38 00           JR      C,$1236             ; {}
15FD: 01 32 00        LD      BC,$0032            
1600: 77              LD      (HL),A              
1601: 12              LD      (DE),A              
1602: 00              NOP                         
1603: 01 02 00        LD      BC,$0002            
1606: 01 12 00        LD      BC,$0012            
1609: 75              LD      (HL),L              
160A: 32 00 35        LD      ($3500),A           
160D: 38 00           JR      C,$1236             ; {}
160F: 01 34 01        LD      BC,$0134            
1612: 5E              LD      E,(HL)              
1613: 38 00           JR      C,$1236             ; {}
1615: 01 36 00        LD      BC,$0036            
1618: 4B              LD      C,E                 
1619: 30 00           JR      NC,$1236            ; {}
161B: 28 38           JR      Z,$126E             ; {}
161D: 00              NOP                         
161E: 01 36 00        LD      BC,$0036            
1621: 8C              ADC     A,H                 
1622: 38 00           JR      C,$1236             ; {}
1624: 01 30 00        LD      BC,$0030            
1627: 3E 38           LD      A,$38               
1629: 00              NOP                         
162A: 01 36 00        LD      BC,$0036            
162D: 7B              LD      A,E                 
162E: 38 00           JR      C,$1236             ; {}
1630: 02              LD      (BC),A              
1631: 30 00           JR      NC,$1236            ; {}
1633: 05              DEC     B                   
1634: 38 00           JR      C,$1236             ; {}
1636: 01 36 00        LD      BC,$0036            
1639: 27              DAA                         
163A: 38 00           JR      C,$1236             ; {}
163C: 02              LD      (BC),A              
163D: 34              INC     (HL)                
163E: 00              NOP                         
163F: 73              LD      (HL),E              
1640: 38 00           JR      C,$1236             ; {}
1642: 01 32 01        LD      BC,$0132            
1645: 7E              LD      A,(HL)              
1646: 32 00 02        LD      ($0200),A           ; {}
1649: 30 00           JR      NC,$1236            ; {}
164B: 42              LD      B,D                 
164C: 38 00           JR      C,$1236             ; {}
164E: 01 36 00        LD      BC,$0036            
1651: 9A              SBC     D                   
1652: 30 00           JR      NC,$1236            ; {}
1654: 89              ADC     A,C                 
1655: 38 00           JR      C,$1236             ; {}
1657: 07              RLCA                        
1658: 30 00           JR      NC,$1236            ; {}
165A: 7B              LD      A,E                 
165B: 38 00           JR      C,$1236             ; {}
165D: 02              LD      (BC),A              
165E: 34              INC     (HL)                
165F: 00              NOP                         
1660: 02              LD      (BC),A              
1661: 14              INC     D                   
1662: 00              NOP                         
1663: 01 04 00        LD      BC,$0004            
1666: 01 14 00        LD      BC,$0014            
1669: 03              INC     BC                  
166A: 18 00           JR      $1236               ; {}
166C: 79              LD      A,C                 
166D: 38 00           JR      C,$1236             ; {}
166F: 2D              DEC     L                   
1670: 36 00           LD      (HL),$00            
1672: 6D              LD      L,L                 
1673: 38 00           JR      C,$1236             ; {}
1675: 01 34 00        LD      BC,$0034            
1678: EE 38           XOR     $38                 
167A: 00              NOP                         
167B: 04              INC     B                   
167C: 30 00           JR      NC,$1236            ; {}
167E: 3C              INC     A                   
167F: 38 00           JR      C,$1236             ; {}
1681: 02              LD      (BC),A              
1682: 18 00           JR      $1236               ; {}
1684: 01 08 00        LD      BC,$0008            
1687: 01 18 00        LD      BC,$0018            
168A: 2E 14           LD      L,$14               
168C: 00              NOP                         
168D: 04              INC     B                   
168E: 34              INC     (HL)                
168F: 00              NOP                         
1690: 0C              INC     C                   
1691: 38 00           JR      C,$1236             ; {}
1693: 01 30 00        LD      BC,$0030            
1696: 02              LD      (BC),A              
1697: 10 00           DJNZ    $1236               ; {}
1699: 01 00 00        LD      BC,$0000            
169C: 01 10 00        LD      BC,$0010            
169F: 13              INC     DE                  
16A0: 30 00           JR      NC,$1236            ; {}
16A2: 9D              SBC     L                   
16A3: 38 00           JR      C,$1236             ; {}
16A5: 02              LD      (BC),A              
16A6: 34              INC     (HL)                
16A7: 00              NOP                         
16A8: 03              INC     BC                  
16A9: 14              INC     D                   
16AA: 00              NOP                         
16AB: 01 04 00        LD      BC,$0004            
16AE: 01 14 00        LD      BC,$0014            
16B1: 04              INC     B                   
16B2: 18 00           JR      $1236               ; {}
16B4: 33              INC     SP                  
16B5: 10 00           DJNZ    $1236               ; {}
16B7: 03              INC     BC                  
16B8: 30 00           JR      NC,$1236            ; {}
16BA: 60              LD      H,B                 
16BB: 38 00           JR      C,$1236             ; {}
16BD: 01 36 00        LD      BC,$0036            
16C0: 10 38           DJNZ    $126E               ; {}
16C2: 00              NOP                         
16C3: 01 30 00        LD      BC,$0030            
16C6: 24              INC     H                   
16C7: 32 00 85        LD      ($8500),A           
16CA: 38 00           JR      C,$1236             ; {}
16CC: 01 34 01        LD      BC,$0134            
16CF: 71              LD      (HL),C              
16D0: 38 00           JR      C,$1236             ; {}
16D2: 03              INC     BC                  
16D3: 36 00           LD      (HL),$00            
16D5: 5B              LD      E,E                 
16D6: 38 00           JR      C,$1236             ; {}
16D8: 03              INC     BC                  
16D9: 32 00 0F        LD      ($0F00),A           ; {}
16DC: 38 00           JR      C,$1236             ; {}
16DE: 01 30 00        LD      BC,$0030            
16E1: CF              RST     0X08                
16E2: 38 00           JR      C,$1236             ; {}
16E4: 01 32 00        LD      BC,$0032            
16E7: 76              HALT                        
16E8: 38 00           JR      C,$1236             ; {}
16EA: 01 30 00        LD      BC,$0030            
16ED: 47              LD      B,A                 
16EE: 38 00           JR      C,$1236             ; {}
16F0: 1F              RRA                         
16F1: 30 00           JR      NC,$1236            ; {}
16F3: 11 38 00        LD      DE,$0038            
16F6: 01 36 00        LD      BC,$0036            
16F9: 26 38           LD      H,$38               
16FB: 00              NOP                         
16FC: 01 32 00        LD      BC,$0032            
16FF: B1              OR      C                   
1700: 2A 5A 86        LD      HL,($865A)          
1703: 23              INC     HL                  
1704: 22 5A 86        LD      ($865A),HL          
1707: 7C              LD      A,H                 
1708: FE 03           CP      $03                 
170A: 20 0E           JR      NZ,$1244            ; {}
170C: 7D              LD      A,L                 
170D: FE 1A           CP      $1A                 
170F: C2 17 05        JP      NZ,$0517            ; {}
1712: 21 58 86        LD      HL,$8658            
1715: 36 06           LD      (HL),$06            
1717: C3 17 05        JP      $0517               ; {}
171A: FE 02           CP      $02                 
171C: 20 1D           JR      NZ,$1253            ; {}
171E: 7D              LD      A,L                 
171F: FE DE           CP      $DE                 
1721: CA 81 18        JP      Z,$1881             ; {}
1724: FE 32           CP      $32                 
1726: CA 21 19        JP      Z,$1921             ; {}
1729: FE 22           CP      $22                 
172B: CA 17 19        JP      Z,$1917             ; {}
172E: FE 12           CP      $12                 
1730: CA 2D 18        JP      Z,$182D             ; {}
1733: FE 02           CP      $02                 
1735: CA FB 18        JP      Z,$18FB             ; {}
1738: C3 17 05        JP      $0517               ; {}
173B: FE 01           CP      $01                 
173D: 20 2F           JR      NZ,$1265            ; {}
173F: 7D              LD      A,L                 
1740: FE F2           CP      $F2                 
1742: CA 2D 18        JP      Z,$182D             ; {}
1745: FE E2           CP      $E2                 
1747: CA 09 19        JP      Z,$1909             ; {}
174A: FE BE           CP      $BE                 
174C: CA F0 18        JP      Z,$18F0             ; {}
174F: D2 17 05        JP      NC,$0517            ; {}
1752: FE BA           CP      $BA                 
1754: D2 E7 17        JP      NC,$17E7            ; {}
1757: FE B2           CP      $B2                 
1759: D2 EC 17        JP      NC,$17EC            ; {}
175C: FE AA           CP      $AA                 
175E: D2 F1 17        JP      NC,$17F1            ; {}
1761: FE A9           CP      $A9                 
1763: CA A3 18        JP      Z,$18A3             ; {}
1766: FE 6D           CP      $6D                 
1768: CA 81 18        JP      Z,$1881             ; {}
176B: C3 17 05        JP      $0517               ; {}
176E: 7D              LD      A,L                 
176F: FE C2           CP      $C2                 
1771: CA 47 18        JP      Z,$1847             ; {}
1774: FE B2           CP      $B2                 
1776: CA 33 18        JP      Z,$1833             ; {}
1779: FE A2           CP      $A2                 
177B: CA 2D 18        JP      Z,$182D             ; {}
177E: FE 92           CP      $92                 
1780: CA 04 18        JP      Z,$1804             ; {}
1783: FE 82           CP      $82                 
1785: CA 2D 18        JP      Z,$182D             ; {}
1788: FE 72           CP      $72                 
178A: CA 16 18        JP      Z,$1816             ; {}
178D: FE 52           CP      $52                 
178F: CA F9 17        JP      Z,$17F9             ; {}
1792: D2 17 05        JP      NC,$0517            ; {}
1795: FE 4F           CP      $4F                 
1797: 30 3C           JR      NC,$1272            ; {}
1799: FE 47           CP      $47                 
179B: 30 3D           JR      NC,$1273            ; {}
179D: FE 3F           CP      $3F                 
179F: 30 3E           JR      NC,$1274            ; {}
17A1: FE 3E           CP      $3E                 
17A3: CA 9F 18        JP      Z,$189F             ; {}
17A6: FE 02           CP      $02                 
17A8: 28 03           JR      Z,$1239             ; {}
17AA: C3 17 05        JP      $0517               ; {}
17AD: 21 A2 98        LD      HL,$98A2            
17B0: 36 82           LD      (HL),$82            
17B2: 23              INC     HL                  
17B3: 36 90           LD      (HL),$90            
17B5: 21 22 98        LD      HL,$9822            
17B8: 36 06           LD      (HL),$06            
17BA: 23              INC     HL                  
17BB: 36 00           LD      (HL),$00            
17BD: 21 22 99        LD      HL,$9922            
17C0: 36 02           LD      (HL),$02            
17C2: 21 88 98        LD      HL,$9888            
17C5: 36 82           LD      (HL),$82            
17C7: 23              INC     HL                  
17C8: 36 90           LD      (HL),$90            
17CA: 21 08 98        LD      HL,$9808            
17CD: 36 13           LD      (HL),$13            
17CF: 23              INC     HL                  
17D0: 36 06           LD      (HL),$06            
17D2: C3 17 05        JP      $0517               ; {}
17D5: 21 82 98        LD      HL,$9882            
17D8: 35              DEC     (HL)                
17D9: 35              DEC     (HL)                
17DA: 21 84 98        LD      HL,$9884            
17DD: 35              DEC     (HL)                
17DE: 35              DEC     (HL)                
17DF: 21 86 98        LD      HL,$9886            
17E2: 35              DEC     (HL)                
17E3: 35              DEC     (HL)                
17E4: C3 17 05        JP      $0517               ; {}
17E7: 21 82 98        LD      HL,$9882            
17EA: 34              INC     (HL)                
17EB: 34              INC     (HL)                
17EC: 21 84 98        LD      HL,$9884            
17EF: 34              INC     (HL)                
17F0: 34              INC     (HL)                
17F1: 21 86 98        LD      HL,$9886            
17F4: 34              INC     (HL)                
17F5: 34              INC     (HL)                
17F6: C3 17 05        JP      $0517               ; {}
17F9: CD 61 19        CALL    $1961               ; {}
17FC: 21 64 98        LD      HL,$9864            
17FF: 36 23           LD      (HL),$23            
1801: C3 17 05        JP      $0517               ; {}
1804: CD 5B 19        CALL    $195B               ; {}
1807: 21 64 98        LD      HL,$9864            
180A: 36 81           LD      (HL),$81            
180C: 21 E5 98        LD      HL,$98E5            
180F: 7E              LD      A,(HL)              
1810: D6 03           SUB     $03                 
1812: 77              LD      (HL),A              
1813: C3 17 05        JP      $0517               ; {}
1816: CD 5B 19        CALL    $195B               ; {}
1819: 21 64 98        LD      HL,$9864            
181C: 36 80           LD      (HL),$80            
181E: 21 E4 98        LD      HL,$98E4            
1821: 7E              LD      A,(HL)              
1822: D6 08           SUB     $08                 
1824: 77              LD      (HL),A              
1825: 23              INC     HL                  
1826: 7E              LD      A,(HL)              
1827: D6 04           SUB     $04                 
1829: 77              LD      (HL),A              
182A: C3 17 05        JP      $0517               ; {}
182D: CD 61 19        CALL    $1961               ; {}
1830: C3 17 05        JP      $0517               ; {}
1833: CD 5B 19        CALL    $195B               ; {}
1836: 21 64 98        LD      HL,$9864            
1839: 34              INC     (HL)                
183A: 21 82 98        LD      HL,$9882            
183D: 06 06           LD      B,$06               
183F: 36 00           LD      (HL),$00            
1841: 23              INC     HL                  
1842: 10 FB           DJNZ    $1231               ; {}
1844: C3 17 05        JP      $0517               ; {}
1847: 21 F4 98        LD      HL,$98F4            
184A: 06 04           LD      B,$04               
184C: 0E 90           LD      C,$90               
184E: 3E 37           LD      A,$37               
1850: 77              LD      (HL),A              
1851: C6 10           ADD     $10                 
1853: 23              INC     HL                  
1854: 71              LD      (HL),C              
1855: 23              INC     HL                  
1856: 10 F8           DJNZ    $122E               ; {}
1858: 36 51           LD      (HL),$51            
185A: 23              INC     HL                  
185B: 71              LD      (HL),C              
185C: 21 64 98        LD      HL,$9864            
185F: 36 32           LD      (HL),$32            
1861: 21 E4 98        LD      HL,$98E4            
1864: 36 00           LD      (HL),$00            
1866: 23              INC     HL                  
1867: 36 00           LD      (HL),$00            
1869: 21 77 18        LD      HL,$1877            
186C: 11 74 98        LD      DE,$9874            
186F: 01 0A 00        LD      BC,$000A            
1872: ED B0           LDIR                        
1874: C3 8E 18        JP      $188E               ; {}
1877: 39              ADD     HL,SP               
1878: 0A              LD      A,(BC)              
1879: 47              LD      B,A                 
187A: 0A              LD      A,(BC)              
187B: 3C              INC     A                   
187C: 0A              LD      A,(BC)              
187D: 47              LD      B,A                 
187E: 0A              LD      A,(BC)              
187F: 65              LD      H,L                 
1880: 00              NOP                         
1881: 21 F4 98        LD      HL,$98F4            
1884: 06 0A           LD      B,$0A               
1886: 36 00           LD      (HL),$00            
1888: 23              INC     HL                  
1889: 10 FB           DJNZ    $1231               ; {}
188B: C3 17 05        JP      $0517               ; {}
188E: 21 22 98        LD      HL,$9822            
1891: 36 06           LD      (HL),$06            
1893: 21 22 99        LD      HL,$9922            
1896: 36 00           LD      (HL),$00            
1898: 2B              DEC     HL                  
1899: 2B              DEC     HL                  
189A: 36 00           LD      (HL),$00            
189C: C3 17 05        JP      $0517               ; {}
189F: 06 02           LD      B,$02               
18A1: 18 02           JR      $1238               ; {}
18A3: 06 00           LD      B,$00               
18A5: 21 22 98        LD      HL,$9822            
18A8: 36 11           LD      (HL),$11            
18AA: DD 21 82 98     LD      IX,$9882            
18AE: FD 21 02 98     LD      IY,$9802            
18B2: 3E 82           LD      A,$82               
18B4: 0E 90           LD      C,$90               
18B6: DD 77 00        LD      (IX+$00),A          
18B9: DD 77 02        LD      (IX+$02),A          
18BC: DD 77 04        LD      (IX+$04),A          
18BF: DD 71 01        LD      (IX+$01),C          
18C2: DD 71 03        LD      (IX+$03),C          
18C5: DD 71 05        LD      (IX+$05),C          
18C8: FD 36 00 37     LD      (IY+$00),$37        
18CC: FD 36 02 37     LD      (IY+$02),$37        
18D0: FD 36 04 36     LD      (IY+$04),$36        
18D4: FD 36 01 08     LD      (IY+$01),$08        
18D8: FD 36 03 08     LD      (IY+$03),$08        
18DC: FD 36 05 08     LD      (IY+$05),$08        
18E0: DD 21 02 99     LD      IX,$9902            
18E4: DD 70 00        LD      (IX+$00),B          
18E7: DD 70 02        LD      (IX+$02),B          
18EA: DD 70 04        LD      (IX+$04),B          
18ED: C3 17 05        JP      $0517               ; {}
18F0: CD 61 19        CALL    $1961               ; {}
18F3: 21 6C 98        LD      HL,$986C            
18F6: 36 27           LD      (HL),$27            
18F8: C3 17 05        JP      $0517               ; {}
18FB: CD 5B 19        CALL    $195B               ; {}
18FE: 21 6C 98        LD      HL,$986C            
1901: 36 84           LD      (HL),$84            
1903: 21 ED 98        LD      HL,$98ED            
1906: C3 0F 18        JP      $180F               ; {}
1909: CD 5B 19        CALL    $195B               ; {}
190C: 21 6C 98        LD      HL,$986C            
190F: 36 83           LD      (HL),$83            
1911: 21 EC 98        LD      HL,$98EC            
1914: C3 21 18        JP      $1821               ; {}
1917: CD 5B 19        CALL    $195B               ; {}
191A: 21 6C 98        LD      HL,$986C            
191D: 34              INC     (HL)                
191E: C3 3A 18        JP      $183A               ; {}
1921: 21 6C 98        LD      HL,$986C            
1924: 36 32           LD      (HL),$32            
1926: 21 EC 98        LD      HL,$98EC            
1929: 36 00           LD      (HL),$00            
192B: 23              INC     HL                  
192C: 36 00           LD      (HL),$00            
192E: 21 F4 98        LD      HL,$98F4            
1931: 06 04           LD      B,$04               
1933: 0E 90           LD      C,$90               
1935: 3E 97           LD      A,$97               
1937: 77              LD      (HL),A              
1938: C6 10           ADD     $10                 
193A: 23              INC     HL                  
193B: 71              LD      (HL),C              
193C: 23              INC     HL                  
193D: 10 F8           DJNZ    $122E               ; {}
193F: 36 B1           LD      (HL),$B1            
1941: 23              INC     HL                  
1942: 71              LD      (HL),C              
1943: 21 51 19        LD      HL,$1951            
1946: 11 74 98        LD      DE,$9874            
1949: 01 0A 00        LD      BC,$000A            
194C: ED B0           LDIR                        
194E: C3 8E 18        JP      $188E               ; {}
1951: 39              ADD     HL,SP               
1952: 0A              LD      A,(BC)              
1953: 47              LD      B,A                 
1954: 0A              LD      A,(BC)              
1955: 3F              CCF                         
1956: 0A              LD      A,(BC)              
1957: 47              LD      B,A                 
1958: 0A              LD      A,(BC)              
1959: 65              LD      H,L                 
195A: 00              NOP                         
195B: 21 22 98        LD      HL,$9822            
195E: 36 0D           LD      (HL),$0D            
1960: C9              RET                         
1961: 21 22 98        LD      HL,$9822            
1964: 36 0C           LD      (HL),$0C            
1966: C9              RET                         
1967: 21 6C 89        LD      HL,$896C            
196A: CB 4E           BIT     1,(HL)              
196C: C2 E3 19        JP      NZ,$19E3            ; {}
196F: CB 46           BIT     0,(HL)              
1971: 20 30           JR      NZ,$1266            ; {}
1973: 21 F0 87        LD      HL,$87F0            
1976: CB 46           BIT     0,(HL)              
1978: 20 51           JR      NZ,$1287            ; {}
197A: 21 6D 89        LD      HL,$896D            
197D: 36 00           LD      (HL),$00            
197F: 21 28 85        LD      HL,$8528            
1982: 0E 00           LD      C,$00               
1984: 06 08           LD      B,$08               
1986: 32 30 68        LD      ($6830),A           
1989: 11 10 00        LD      DE,$0010            
198C: CB 7E           BIT     7,(HL)              
198E: 28 01           JR      Z,$1237             ; {}
1990: 0C              INC     C                   
1991: 19              ADD     HL,DE               
1992: 32 30 68        LD      ($6830),A           
1995: 10 F5           DJNZ    $122B               ; {}
1997: 79              LD      A,C                 
1998: FE 07           CP      $07                 
199A: 20 2F           JR      NZ,$1265            ; {}
199C: 21 F0 87        LD      HL,$87F0            
199F: CB C6           SET     0,(HL)              
19A1: 18 40           JR      $1276               ; {}
19A3: 21 A1 83        LD      HL,$83A1            
19A6: 36 7E           LD      (HL),$7E            
19A8: 23              INC     HL                  
19A9: 7E              LD      A,(HL)              
19AA: FE 0E           CP      $0E                 
19AC: 28 04           JR      Z,$123A             ; {}
19AE: FE 0F           CP      $0F                 
19B0: 20 02           JR      NZ,$1238            ; {}
19B2: 36 7E           LD      (HL),$7E            
19B4: 11 20 00        LD      DE,$0020            
19B7: 19              ADD     HL,DE               
19B8: 3E 7E           LD      A,$7E               
19BA: 77              LD      (HL),A              
19BB: 2B              DEC     HL                  
19BC: 77              LD      (HL),A              
19BD: 19              ADD     HL,DE               
19BE: 77              LD      (HL),A              
19BF: 23              INC     HL                  
19C0: 77              LD      (HL),A              
19C1: 21 86 9A        LD      HL,$9A86            
19C4: 36 01           LD      (HL),$01            
19C6: 21 6C 89        LD      HL,$896C            
19C9: CB CE           SET     1,(HL)              
19CB: 00              NOP                         
19CC: 3A F0 87        LD      A,($87F0)           
19CF: CB 47           BIT     0,A                 
19D1: 28 10           JR      Z,$1246             ; {}
19D3: 21 6D 89        LD      HL,$896D            
19D6: 7E              LD      A,(HL)              
19D7: FE 1E           CP      $1E                 
19D9: 20 07           JR      NZ,$123D            ; {}
19DB: 21 6C 89        LD      HL,$896C            
19DE: CB C6           SET     0,(HL)              
19E0: 18 01           JR      $1237               ; {}
19E2: 34              INC     (HL)                
19E3: 00              NOP                         
19E4: 3A 00 84        LD      A,($8400)           
19E7: CB 4F           BIT     1,A                 
19E9: 20 0E           JR      NZ,$1244            ; {}
19EB: 2A D4 87        LD      HL,($87D4)          
19EE: 22 ED 87        LD      ($87ED),HL          
19F1: 3A DA 87        LD      A,($87DA)           
19F4: 32 EB 87        LD      ($87EB),A           
19F7: 18 0C           JR      $1242               ; {}
19F9: 3A D8 87        LD      A,($87D8)           
19FC: 32 EB 87        LD      ($87EB),A           
19FF: 2A D2 87        LD      HL,($87D2)          
1A02: 22 ED 87        LD      ($87ED),HL          
1A05: 3A 99 87        LD      A,($8799)           
1A08: 21 EB 87        LD      HL,$87EB            
1A0B: CB 47           BIT     0,A                 
1A0D: 28 06           JR      Z,$123C             ; {}
1A0F: CB 87           RES     0,A                 
1A11: 32 99 87        LD      ($8799),A           
1A14: 34              INC     (HL)                
1A15: 00              NOP                         
1A16: 3A EB 87        LD      A,($87EB)           
1A19: FE 02           CP      $02                 
1A1B: 20 21           JR      NZ,$1257            ; {}
1A1D: 21 F0 87        LD      HL,$87F0            
1A20: CB EE           SET     5,(HL)              
1A22: CD 1E 1B        CALL    $1B1E               ; {}
1A25: 21 EF 87        LD      HL,$87EF            
1A28: 36 46           LD      (HL),$46            
1A2A: 21 F0 87        LD      HL,$87F0            
1A2D: CB B6           RES     6,(HL)              
1A2F: 21 9E 98        LD      HL,$989E            
1A32: 36 71           LD      (HL),$71            
1A34: 23              INC     HL                  
1A35: 36 80           LD      (HL),$80            
1A37: 21 EB 87        LD      HL,$87EB            
1A3A: 34              INC     (HL)                
1A3B: C3 02 1B        JP      $1B02               ; {}
1A3E: 3A F0 87        LD      A,($87F0)           
1A41: CB 6F           BIT     5,A                 
1A43: 28 1F           JR      Z,$1255             ; {}
1A45: 2A ED 87        LD      HL,($87ED)          
1A48: 23              INC     HL                  
1A49: 22 ED 87        LD      ($87ED),HL          
1A4C: 11 58 02        LD      DE,$0258            
1A4F: A7              AND     A                   
1A50: ED 52           SBC     HL,DE               
1A52: 20 10           JR      NZ,$1246            ; {}
1A54: 21 9E 98        LD      HL,$989E            
1A57: 36 00           LD      (HL),$00            
1A59: 23              INC     HL                  
1A5A: 36 E0           LD      (HL),$E0            
1A5C: 21 F0 87        LD      HL,$87F0            
1A5F: CB AE           RES     5,(HL)              
1A61: C3 02 1B        JP      $1B02               ; {}
1A64: 3A 01 84        LD      A,($8401)           
1A67: CB 7F           BIT     7,A                 
1A69: C0              RET     NZ                  
1A6A: 3A 00 84        LD      A,($8400)           
1A6D: CB 6F           BIT     5,A                 
1A6F: 20 06           JR      NZ,$123C            ; {}
1A71: 3A 57 86        LD      A,($8657)           
1A74: CB 4F           BIT     1,A                 
1A76: C8              RET     Z                   
1A77: 21 9E 98        LD      HL,$989E            
1A7A: 11 A2 98        LD      DE,$98A2            
1A7D: 1A              LD      A,(DE)              
1A7E: BE              CP      (HL)                
1A7F: 20 0E           JR      NZ,$1244            ; {}
1A81: 23              INC     HL                  
1A82: 13              INC     DE                  
1A83: 1A              LD      A,(DE)              
1A84: BE              CP      (HL)                
1A85: 20 08           JR      NZ,$123E            ; {}
1A87: 3A F0 87        LD      A,($87F0)           
1A8A: CB F7           SET     6,A                 
1A8C: 32 F0 87        LD      ($87F0),A           
1A8F: 3A F0 87        LD      A,($87F0)           
1A92: CB 77           BIT     6,A                 
1A94: CA 02 1B        JP      Z,$1B02             ; {}
1A97: 21 EF 87        LD      HL,$87EF            
1A9A: 7E              LD      A,(HL)              
1A9B: A7              AND     A                   
1A9C: CA 02 1B        JP      Z,$1B02             ; {}
1A9F: 35              DEC     (HL)                
1AA0: 7E              LD      A,(HL)              
1AA1: FE 44           CP      $44                 
1AA3: 20 3C           JR      NZ,$1272            ; {}
1AA5: 21 93 9A        LD      HL,$9A93            
1AA8: 36 01           LD      (HL),$01            
1AAA: 21 A7 87        LD      HL,$87A7            
1AAD: CB C6           SET     0,(HL)              
1AAF: 3A E6 87        LD      A,($87E6)           
1AB2: 32 76 98        LD      ($9876),A           
1AB5: AF              XOR     A                   
1AB6: 32 77 98        LD      ($9877),A           
1AB9: 21 7E 98        LD      HL,$987E            
1ABC: 36 64           LD      (HL),$64            
1ABE: 23              INC     HL                  
1ABF: 36 00           LD      (HL),$00            
1AC1: 3A 9E 98        LD      A,($989E)           
1AC4: D6 08           SUB     $08                 
1AC6: 32 F6 98        LD      ($98F6),A           
1AC9: C6 10           ADD     $10                 
1ACB: 32 FE 98        LD      ($98FE),A           
1ACE: 3A 9F 98        LD      A,($989F)           
1AD1: 32 F7 98        LD      ($98F7),A           
1AD4: 32 FF 98        LD      ($98FF),A           
1AD7: 21 9E 98        LD      HL,$989E            
1ADA: 36 00           LD      (HL),$00            
1ADC: 23              INC     HL                  
1ADD: 36 E0           LD      (HL),$E0            
1ADF: 18 21           JR      $1257               ; {}
1AE1: FE 02           CP      $02                 
1AE3: 20 12           JR      NZ,$1248            ; {}
1AE5: 21 F6 98        LD      HL,$98F6            
1AE8: 36 00           LD      (HL),$00            
1AEA: 23              INC     HL                  
1AEB: 36 00           LD      (HL),$00            
1AED: 21 FE 98        LD      HL,$98FE            
1AF0: 36 00           LD      (HL),$00            
1AF2: 23              INC     HL                  
1AF3: 36 00           LD      (HL),$00            
1AF5: 18 0B           JR      $1241               ; {}
1AF7: FE 01           CP      $01                 
1AF9: 20 07           JR      NZ,$123D            ; {}
1AFB: 36 00           LD      (HL),$00            
1AFD: 21 F0 87        LD      HL,$87F0            
1B00: CB B6           RES     6,(HL)              
1B02: 3A 00 84        LD      A,($8400)           
1B05: CB 4F           BIT     1,A                 
1B07: 2A ED 87        LD      HL,($87ED)          
1B0A: 3A EB 87        LD      A,($87EB)           
1B0D: 20 08           JR      NZ,$123E            ; {}
1B0F: 32 DA 87        LD      ($87DA),A           
1B12: 22 D4 87        LD      ($87D4),HL          
1B15: 18 06           JR      $123C               ; {}
1B17: 32 D8 87        LD      ($87D8),A           
1B1A: 22 D2 87        LD      ($87D2),HL          
1B1D: C9              RET                         
1B1E: 3A 00 84        LD      A,($8400)           
1B21: CB 4F           BIT     1,A                 
1B23: 20 05           JR      NZ,$123B            ; {}
1B25: 21 0D 84        LD      HL,$840D            
1B28: 18 03           JR      $1239               ; {}
1B2A: 21 0E 84        LD      HL,$840E            
1B2D: 7E              LD      A,(HL)              
1B2E: 21 E8 87        LD      HL,$87E8            
1B31: FE 12           CP      $12                 
1B33: 38 02           JR      C,$1238             ; {}
1B35: 3E 12           LD      A,$12               
1B37: 77              LD      (HL),A              
1B38: D6 01           SUB     $01                 
1B3A: 87              ADD     A,A                 
1B3B: 87              ADD     A,A                 
1B3C: 5F              LD      E,A                 
1B3D: 16 00           LD      D,$00               
1B3F: 21 57 1B        LD      HL,$1B57            
1B42: 19              ADD     HL,DE               
1B43: 7E              LD      A,(HL)              
1B44: 32 1E 98        LD      ($981E),A           
1B47: 23              INC     HL                  
1B48: 7E              LD      A,(HL)              
1B49: 32 1F 98        LD      ($981F),A           
1B4C: 23              INC     HL                  
1B4D: 7E              LD      A,(HL)              
1B4E: 32 E7 87        LD      ($87E7),A           
1B51: 23              INC     HL                  
1B52: 7E              LD      A,(HL)              
1B53: 32 E6 87        LD      ($87E6),A           
1B56: C9              RET                         
1B57: 53              LD      D,E                 
1B58: 0E 04           LD      C,$04               
1B5A: 5D              LD      E,L                 
1B5B: 55              LD      D,L                 
1B5C: 10 06           DJNZ    $123C               ; {}
1B5E: 5E              LD      E,(HL)              
1B5F: 58              LD      E,B                 
1B60: 12              LD      (DE),A              
1B61: 08              EX      AF,AF'              
1B62: 5F              LD      E,A                 
1B63: 54              LD      D,H                 
1B64: 0F              RRCA                        
1B65: 10 60           DJNZ    $1296               ; {}
1B67: 54              LD      D,H                 
1B68: 0F              RRCA                        
1B69: 10 60           DJNZ    $1296               ; {}
1B6B: 57              LD      D,A                 
1B6C: 11 20 4E        LD      DE,$4E20            
1B6F: 57              LD      D,A                 
1B70: 11 20 4E        LD      DE,$4E20            
1B73: 56              LD      D,(HL)              
1B74: 10 30           DJNZ    $1266               ; {}
1B76: 4F              LD      C,A                 
1B77: 56              LD      D,(HL)              
1B78: 10 30           DJNZ    $1266               ; {}
1B7A: 4F              LD      C,A                 
1B7B: 59              LD      E,C                 
1B7C: 13              INC     DE                  
1B7D: 40              LD      B,B                 
1B7E: 61              LD      H,C                 
1B7F: 59              LD      E,C                 
1B80: 13              INC     DE                  
1B81: 40              LD      B,B                 
1B82: 61              LD      H,C                 
1B83: 5A              LD      E,D                 
1B84: 14              INC     D                   
1B85: 50              LD      D,B                 
1B86: 50              LD      D,B                 
1B87: 5A              LD      E,D                 
1B88: 14              INC     D                   
1B89: 50              LD      D,B                 
1B8A: 50              LD      D,B                 
1B8B: 52              LD      D,D                 
1B8C: 0D              DEC     C                   
1B8D: 60              LD      H,B                 
1B8E: 62              LD      H,D                 
1B8F: 52              LD      D,D                 
1B90: 0D              DEC     C                   
1B91: 60              LD      H,B                 
1B92: 62              LD      H,D                 
1B93: 5B              LD      E,E                 
1B94: 15              DEC     D                   
1B95: 70              LD      (HL),B              
1B96: 51              LD      D,C                 
1B97: 5B              LD      E,E                 
1B98: 15              DEC     D                   
1B99: 70              LD      (HL),B              
1B9A: 51              LD      D,C                 
1B9B: 5C              LD      E,H                 
1B9C: 16 80           LD      D,$80               
1B9E: 63              LD      H,E                 
1B9F: 3A 57 86        LD      A,($8657)           
1BA2: CB 4F           BIT     1,A                 
1BA4: 28 04           JR      Z,$123A             ; {}
1BA6: 3E 02           LD      A,$02               
1BA8: 18 05           JR      $123B               ; {}
1BAA: 3A 8D 89        LD      A,($898D)           
1BAD: E6 03           AND     $03                 
1BAF: 87              ADD     A,A                 
1BB0: 87              ADD     A,A                 
1BB1: 87              ADD     A,A                 
1BB2: 87              ADD     A,A                 
1BB3: 6F              LD      L,A                 
1BB4: 26 00           LD      H,$00               
1BB6: 3A 10 84        LD      A,($8410)           
1BB9: 3D              DEC     A                   
1BBA: 5F              LD      E,A                 
1BBB: 16 00           LD      D,$00               
1BBD: 19              ADD     HL,DE               
1BBE: EB              EX      DE,HL               
1BBF: 21 FA 1B        LD      HL,$1BFA            
1BC2: 19              ADD     HL,DE               
1BC3: 7E              LD      A,(HL)              
1BC4: 32 BD 87        LD      ($87BD),A           
1BC7: 3A 00 84        LD      A,($8400)           
1BCA: CB 4F           BIT     1,A                 
1BCC: 20 05           JR      NZ,$123B            ; {}
1BCE: 3A 0D 84        LD      A,($840D)           
1BD1: 18 03           JR      $1239               ; {}
1BD3: 3A 0E 84        LD      A,($840E)           
1BD6: 21 BD 87        LD      HL,$87BD            
1BD9: D6 1E           SUB     $1E                 
1BDB: 38 02           JR      C,$1238             ; {}
1BDD: 86              ADD     A,(HL)              
1BDE: 77              LD      (HL),A              
1BDF: 21 3A 1C        LD      HL,$1C3A            
1BE2: 06 06           LD      B,$06               
1BE4: DD 21 A0 87     LD      IX,$87A0            
1BE8: E5              PUSH    HL                  
1BE9: 19              ADD     HL,DE               
1BEA: 7E              LD      A,(HL)              
1BEB: E1              POP     HL                  
1BEC: DD 77 00        LD      (IX+$00),A          
1BEF: D5              PUSH    DE                  
1BF0: 11 40 00        LD      DE,$0040            
1BF3: 19              ADD     HL,DE               
1BF4: D1              POP     DE                  
1BF5: DD 23           INC     IX                  
1BF7: 10 EF           DJNZ    $1225               ; {}
1BF9: C9              RET                         
1BFA: 73              LD      (HL),E              
1BFB: 73              LD      (HL),E              
1BFC: 78              LD      A,B                 
1BFD: 78              LD      A,B                 
1BFE: 78              LD      A,B                 
1BFF: 80              ADD     A,B                 
1C00: 80              ADD     A,B                 
1C01: 80              ADD     A,B                 
1C02: 84              ADD     A,H                 
1C03: 84              ADD     A,H                 
1C04: 84              ADD     A,H                 
1C05: 84              ADD     A,H                 
1C06: 87              ADD     A,A                 
1C07: 8C              ADC     A,H                 
1C08: 96              SUB     (HL)                
1C09: 80              ADD     A,B                 
1C0A: 78              LD      A,B                 
1C0B: 78              LD      A,B                 
1C0C: 78              LD      A,B                 
1C0D: 78              LD      A,B                 
1C0E: 78              LD      A,B                 
1C0F: 80              ADD     A,B                 
1C10: 80              ADD     A,B                 
1C11: 84              ADD     A,H                 
1C12: 84              ADD     A,H                 
1C13: 84              ADD     A,H                 
1C14: 84              ADD     A,H                 
1C15: 84              ADD     A,H                 
1C16: 87              ADD     A,A                 
1C17: 8C              ADC     A,H                 
1C18: 96              SUB     (HL)                
1C19: 80              ADD     A,B                 
1C1A: 7C              LD      A,H                 
1C1B: 7C              LD      A,H                 
1C1C: 7C              LD      A,H                 
1C1D: 7C              LD      A,H                 
1C1E: 7C              LD      A,H                 
1C1F: 80              ADD     A,B                 
1C20: 80              ADD     A,B                 
1C21: 84              ADD     A,H                 
1C22: 84              ADD     A,H                 
1C23: 84              ADD     A,H                 
1C24: 84              ADD     A,H                 
1C25: 84              ADD     A,H                 
1C26: 87              ADD     A,A                 
1C27: 8C              ADC     A,H                 
1C28: 96              SUB     (HL)                
1C29: 80              ADD     A,B                 
1C2A: 7E              LD      A,(HL)              
1C2B: 7E              LD      A,(HL)              
1C2C: 7E              LD      A,(HL)              
1C2D: 7E              LD      A,(HL)              
1C2E: 7E              LD      A,(HL)              
1C2F: 87              ADD     A,A                 
1C30: 87              ADD     A,A                 
1C31: 87              ADD     A,A                 
1C32: 87              ADD     A,A                 
1C33: 87              ADD     A,A                 
1C34: 87              ADD     A,A                 
1C35: 8A              ADC     A,D                 
1C36: 8C              ADC     A,H                 
1C37: 90              SUB     B                   
1C38: 96              SUB     (HL)                
1C39: 80              ADD     A,B                 
1C3A: 7C              LD      A,H                 
1C3B: 80              ADD     A,B                 
1C3C: 80              ADD     A,B                 
1C3D: 85              ADD     A,L                 
1C3E: 89              ADC     A,C                 
1C3F: 92              SUB     D                   
1C40: 96              SUB     (HL)                
1C41: 9A              SBC     D                   
1C42: 9F              SBC     A                   
1C43: 9F              SBC     A                   
1C44: A3              AND     E                   
1C45: A3              AND     E                   
1C46: A3              AND     E                   
1C47: A3              AND     E                   
1C48: A8              XOR     B                   
1C49: 80              ADD     A,B                 
1C4A: 80              ADD     A,B                 
1C4B: 85              ADD     A,L                 
1C4C: 89              ADC     A,C                 
1C4D: 89              ADC     A,C                 
1C4E: 8D              ADC     A,L                 
1C4F: 96              SUB     (HL)                
1C50: 96              SUB     (HL)                
1C51: 9A              SBC     D                   
1C52: 9F              SBC     A                   
1C53: 9F              SBC     A                   
1C54: A3              AND     E                   
1C55: A3              AND     E                   
1C56: A3              AND     E                   
1C57: A3              AND     E                   
1C58: A8              XOR     B                   
1C59: 80              ADD     A,B                 
1C5A: 89              ADC     A,C                 
1C5B: 8D              ADC     A,L                 
1C5C: 91              SUB     C                   
1C5D: 92              SUB     D                   
1C5E: 92              SUB     D                   
1C5F: 9A              SBC     D                   
1C60: 9A              SBC     D                   
1C61: 9F              SBC     A                   
1C62: 9F              SBC     A                   
1C63: A3              AND     E                   
1C64: A3              AND     E                   
1C65: A3              AND     E                   
1C66: A3              AND     E                   
1C67: A3              AND     E                   
1C68: A8              XOR     B                   
1C69: 80              ADD     A,B                 
1C6A: 92              SUB     D                   
1C6B: 92              SUB     D                   
1C6C: 96              SUB     (HL)                
1C6D: 96              SUB     (HL)                
1C6E: 9A              SBC     D                   
1C6F: 9F              SBC     A                   
1C70: 9F              SBC     A                   
1C71: A3              AND     E                   
1C72: A3              AND     E                   
1C73: A8              XOR     B                   
1C74: A8              XOR     B                   
1C75: A8              XOR     B                   
1C76: AC              XOR     H                   
1C77: AC              XOR     H                   
1C78: B4              OR      H                   
1C79: 80              ADD     A,B                 
1C7A: 80              ADD     A,B                 
1C7B: 89              ADC     A,C                 
1C7C: 8D              ADC     A,L                 
1C7D: 92              SUB     D                   
1C7E: 9A              SBC     D                   
1C7F: A3              AND     E                   
1C80: A8              XOR     B                   
1C81: AC              XOR     H                   
1C82: AC              XOR     H                   
1C83: AC              XOR     H                   
1C84: B0              OR      B                   
1C85: B4              OR      H                   
1C86: B4              OR      H                   
1C87: B8              CP      B                   
1C88: BC              CP      H                   
1C89: 80              ADD     A,B                 
1C8A: 85              ADD     A,L                 
1C8B: 8D              ADC     A,L                 
1C8C: 96              SUB     (HL)                
1C8D: 9A              SBC     D                   
1C8E: 9F              SBC     A                   
1C8F: A8              XOR     B                   
1C90: A8              XOR     B                   
1C91: AC              XOR     H                   
1C92: AC              XOR     H                   
1C93: B0              OR      B                   
1C94: B0              OR      B                   
1C95: B4              OR      H                   
1C96: B4              OR      H                   
1C97: B8              CP      B                   
1C98: BC              CP      H                   
1C99: 80              ADD     A,B                 
1C9A: 92              SUB     D                   
1C9B: 96              SUB     (HL)                
1C9C: 9A              SBC     D                   
1C9D: 9F              SBC     A                   
1C9E: A3              AND     E                   
1C9F: A8              XOR     B                   
1CA0: A8              XOR     B                   
1CA1: AC              XOR     H                   
1CA2: AC              XOR     H                   
1CA3: B0              OR      B                   
1CA4: B0              OR      B                   
1CA5: B4              OR      H                   
1CA6: B4              OR      H                   
1CA7: B8              CP      B                   
1CA8: BC              CP      H                   
1CA9: 80              ADD     A,B                 
1CAA: 9A              SBC     D                   
1CAB: 9F              SBC     A                   
1CAC: A3              AND     E                   
1CAD: A3              AND     E                   
1CAE: A8              XOR     B                   
1CAF: AC              XOR     H                   
1CB0: B0              OR      B                   
1CB1: B4              OR      H                   
1CB2: B4              OR      H                   
1CB3: B4              OR      H                   
1CB4: B8              CP      B                   
1CB5: B8              CP      B                   
1CB6: BC              CP      H                   
1CB7: C1              POP     BC                  
1CB8: C5              PUSH    BC                  
1CB9: 80              ADD     A,B                 
1CBA: AC              XOR     H                   
1CBB: B0              OR      B                   
1CBC: B4              OR      H                   
1CBD: B4              OR      H                   
1CBE: BC              CP      H                   
1CBF: C1              POP     BC                  
1CC0: C5              PUSH    BC                  
1CC1: CA CE D2        JP      Z,$D2CE             
1CC4: D2 DB DB        JP      NC,$DBDB            
1CC7: DF              RST     0X18                
1CC8: DF              RST     0X18                
1CC9: 80              ADD     A,B                 
1CCA: B0              OR      B                   
1CCB: B4              OR      H                   
1CCC: B8              CP      B                   
1CCD: BC              CP      H                   
1CCE: C1              POP     BC                  
1CCF: CA CA CE        JP      Z,$CECA             
1CD2: CE D2           ADC     $D2                 
1CD4: D7              RST     0X10                
1CD5: DB DB           IN      A,($DB)             ; {}
1CD7: DF              RST     0X18                
1CD8: DF              RST     0X18                
1CD9: 80              ADD     A,B                 
1CDA: B8              CP      B                   
1CDB: BC              CP      H                   
1CDC: C1              POP     BC                  
1CDD: C5              PUSH    BC                  
1CDE: CA CE CE        JP      Z,$CECE             
1CE1: D2 D2 D7        JP      NC,$D7D2            
1CE4: D7              RST     0X10                
1CE5: D2 D2 DF        JP      NC,$DFD2            
1CE8: DF              RST     0X18                
1CE9: 80              ADD     A,B                 
1CEA: C1              POP     BC                  
1CEB: C5              PUSH    BC                  
1CEC: CA CA CE        JP      Z,$CECA             
1CEF: D2 D7 DB        JP      NC,$DBD7            
1CF2: DB DB           IN      A,($DB)             ; {}
1CF4: DF              RST     0X18                
1CF5: DF              RST     0X18                
1CF6: DF              RST     0X18                
1CF7: DF              RST     0X18                
1CF8: DF              RST     0X18                
1CF9: 80              ADD     A,B                 
1CFA: 85              ADD     A,L                 
1CFB: 89              ADC     A,C                 
1CFC: 89              ADC     A,C                 
1CFD: 8D              ADC     A,L                 
1CFE: 8D              ADC     A,L                 
1CFF: 9A              SBC     D                   
1D00: 9F              SBC     A                   
1D01: A3              AND     E                   
1D02: A8              XOR     B                   
1D03: A8              XOR     B                   
1D04: AC              XOR     H                   
1D05: AC              XOR     H                   
1D06: AC              XOR     H                   
1D07: AC              XOR     H                   
1D08: B0              OR      B                   
1D09: 80              ADD     A,B                 
1D0A: 89              ADC     A,C                 
1D0B: 8D              ADC     A,L                 
1D0C: 92              SUB     D                   
1D0D: 92              SUB     D                   
1D0E: 96              SUB     (HL)                
1D0F: 9F              SBC     A                   
1D10: 9F              SBC     A                   
1D11: A3              AND     E                   
1D12: A8              XOR     B                   
1D13: A8              XOR     B                   
1D14: AC              XOR     H                   
1D15: AC              XOR     H                   
1D16: AC              XOR     H                   
1D17: AC              XOR     H                   
1D18: B0              OR      B                   
1D19: 80              ADD     A,B                 
1D1A: 92              SUB     D                   
1D1B: 96              SUB     (HL)                
1D1C: 9A              SBC     D                   
1D1D: 9A              SBC     D                   
1D1E: A4              AND     H                   
1D1F: A3              AND     E                   
1D20: A3              AND     E                   
1D21: A8              XOR     B                   
1D22: A8              XOR     B                   
1D23: AC              XOR     H                   
1D24: AC              XOR     H                   
1D25: AC              XOR     H                   
1D26: AC              XOR     H                   
1D27: AC              XOR     H                   
1D28: B0              OR      B                   
1D29: 80              ADD     A,B                 
1D2A: 9F              SBC     A                   
1D2B: 9F              SBC     A                   
1D2C: A3              AND     E                   
1D2D: A3              AND     E                   
1D2E: A8              XOR     B                   
1D2F: AC              XOR     H                   
1D30: B0              OR      B                   
1D31: B0              OR      B                   
1D32: B0              OR      B                   
1D33: B4              OR      H                   
1D34: B4              OR      H                   
1D35: B4              OR      H                   
1D36: B8              CP      B                   
1D37: B8              CP      B                   
1D38: C1              POP     BC                  
1D39: 80              ADD     A,B                 
1D3A: 8D              ADC     A,L                 
1D3B: 96              SUB     (HL)                
1D3C: 9A              SBC     D                   
1D3D: 9F              SBC     A                   
1D3E: A8              XOR     B                   
1D3F: B0              OR      B                   
1D40: B4              OR      H                   
1D41: B4              OR      H                   
1D42: B8              CP      B                   
1D43: B8              CP      B                   
1D44: BC              CP      H                   
1D45: C1              POP     BC                  
1D46: C1              POP     BC                  
1D47: C5              PUSH    BC                  
1D48: CA 80 92        JP      Z,$9280             
1D4B: 9A              SBC     D                   
1D4C: A3              AND     E                   
1D4D: A8              XOR     B                   
1D4E: AC              XOR     H                   
1D4F: B4              OR      H                   
1D50: B4              OR      H                   
1D51: B8              CP      B                   
1D52: B8              CP      B                   
1D53: BC              CP      H                   
1D54: BC              CP      H                   
1D55: C1              POP     BC                  
1D56: C1              POP     BC                  
1D57: C5              PUSH    BC                  
1D58: CA 80 9F        JP      Z,$9F80             
1D5B: A3              AND     E                   
1D5C: A8              XOR     B                   
1D5D: AC              XOR     H                   
1D5E: B0              OR      B                   
1D5F: B4              OR      H                   
1D60: B4              OR      H                   
1D61: B8              CP      B                   
1D62: B8              CP      B                   
1D63: BC              CP      H                   
1D64: BC              CP      H                   
1D65: C1              POP     BC                  
1D66: C1              POP     BC                  
1D67: C5              PUSH    BC                  
1D68: CA 80 A8        JP      Z,$A880             
1D6B: AC              XOR     H                   
1D6C: B0              OR      B                   
1D6D: B0              OR      B                   
1D6E: B4              OR      H                   
1D6F: B8              CP      B                   
1D70: BC              CP      H                   
1D71: C1              POP     BC                  
1D72: C1              POP     BC                  
1D73: C1              POP     BC                  
1D74: C5              PUSH    BC                  
1D75: C5              PUSH    BC                  
1D76: CA CE D2        JP      Z,$D2CE             
1D79: 80              ADD     A,B                 
1D7A: B7              OR      A                   
1D7B: BB              CP      E                   
1D7C: BF              CP      A                   
1D7D: BF              CP      A                   
1D7E: C7              RST     0X00                
1D7F: CC D0 D5        CALL    Z,$D5D0             
1D82: D9              EXX                         
1D83: DD ; ????
1D84: DD ; ????
1D85: E2 E6 EA        JP      PO,$EAE6            
1D88: EA 80 BB        JP      PE,$BB80            
1D8B: BF              CP      A                   
1D8C: C3 C7 CC        JP      $CCC7               
1D8F: D5              PUSH    DE                  
1D90: D5              PUSH    DE                  
1D91: D9              EXX                         
1D92: D9              EXX                         
1D93: DD ; ????
1D94: E2 E6 E6        JP      PO,$E6E6            
1D97: EA EA 80        JP      PE,$80EA            
1D9A: C3 C7 CF        JP      $CFC7               
1D9D: D1              POP     DE                  
1D9E: D5              PUSH    DE                  
1D9F: D9              EXX                         
1DA0: D9              EXX                         
1DA1: DD ; ????
1DA2: DD ; ????
1DA3: E2 E2 E6        JP      PO,$E6E2            
1DA6: E6 EA           AND     $EA                 
1DA8: EA 80 CC        JP      PE,$CC80            
1DAB: D0              RET     NC                  
1DAC: D5              PUSH    DE                  
1DAD: D5              PUSH    DE                  
1DAE: D9              EXX                         
1DAF: DD ; ????
1DB0: E2 E6 E6        JP      PO,$E6E6            
1DB3: E6 EA           AND     $EA                 
1DB5: EA EA EA        JP      PE,$EAEA            
1DB8: EA 80 40        JP      PE,$4080            
1DBB: 40              LD      B,B                 
1DBC: 40              LD      B,B                 
1DBD: 40              LD      B,B                 
1DBE: 44              LD      B,H                 
1DBF: 44              LD      B,H                 
1DC0: 44              LD      B,H                 
1DC1: 44              LD      B,H                 
1DC2: 44              LD      B,H                 
1DC3: 44              LD      B,H                 
1DC4: 44              LD      B,H                 
1DC5: 44              LD      B,H                 
1DC6: 44              LD      B,H                 
1DC7: 46              LD      B,(HL)              
1DC8: 48              LD      C,B                 
1DC9: 51              LD      D,C                 
1DCA: 51              LD      D,C                 
1DCB: 51              LD      D,C                 
1DCC: 51              LD      D,C                 
1DCD: 51              LD      D,C                 
1DCE: 53              LD      D,E                 
1DCF: 53              LD      D,E                 
1DD0: 53              LD      D,E                 
1DD1: 53              LD      D,E                 
1DD2: 53              LD      D,E                 
1DD3: 53              LD      D,E                 
1DD4: 53              LD      D,E                 
1DD5: 53              LD      D,E                 
1DD6: 53              LD      D,E                 
1DD7: 55              LD      D,L                 
1DD8: 3A CF 89        LD      A,($89CF)           
1DDB: A7              AND     A                   
1DDC: 20 0F           JR      NZ,$1245            ; {}
1DDE: 3A 3D 9B        LD      A,($9B3D)           
1DE1: FE 05           CP      $05                 
1DE3: D0              RET     NC                  
1DE4: 21 F2 1D        LD      HL,$1DF2            
1DE7: CF              RST     0X08                
1DE8: 7E              LD      A,(HL)              
1DE9: 23              INC     HL                  
1DEA: 66              LD      H,(HL)              
1DEB: 6F              LD      L,A                 
1DEC: E9              JP      (HL)                
1DED: AF              XOR     A                   
1DEE: 32 3D 9B        LD      ($9B3D),A           
1DF1: C9              RET                         
1DF2: FC 1D 36        CALL    M,$361D             
1DF5: 1E 6B           LD      E,$6B               
1DF7: 1E 07           LD      E,$07               
1DF9: 1E FD           LD      E,$FD               
1DFB: 1D              DEC     E                   
1DFC: C9              RET                         
1DFD: CD A7 1E        CALL    $1EA7               ; {}
1E00: 20 05           JR      NZ,$123B            ; {}
1E02: AF              XOR     A                   
1E03: 32 3D 9B        LD      ($9B3D),A           
1E06: C9              RET                         
1E07: 21 DA 1E        LD      HL,$1EDA            
1E0A: CD 76 1E        CALL    $1E76               ; {}
1E0D: 11 30 B8        LD      DE,$B830            
1E10: 06 04           LD      B,$04               
1E12: CD 7B 1E        CALL    $1E7B               ; {}
1E15: 11 DA 1E        LD      DE,$1EDA            
1E18: 21 00 B8        LD      HL,$B800            
1E1B: 06 25           LD      B,$25               
1E1D: CD AF 1E        CALL    $1EAF               ; {}
1E20: CC A7 1E        CALL    Z,$1EA7             ; {}
1E23: 32 CF 89        LD      ($89CF),A           
1E26: 21 DA 1E        LD      HL,$1EDA            
1E29: 11 A0 89        LD      DE,$89A0            
1E2C: 01 25 00        LD      BC,$0025            
1E2F: ED B0           LDIR                        
1E31: AF              XOR     A                   
1E32: 32 3D 9B        LD      ($9B3D),A           
1E35: C9              RET                         
1E36: 21 00 B8        LD      HL,$B800            
1E39: 11 A0 89        LD      DE,$89A0            
1E3C: 06 25           LD      B,$25               
1E3E: 36 00           LD      (HL),$00            
1E40: 3E 08           LD      A,$08               
1E42: 32 40 B8        LD      ($B840),A           
1E45: 3C              INC     A                   
1E46: 32 40 B8        LD      ($B840),A           
1E49: 00              NOP                         
1E4A: 3E 08           LD      A,$08               
1E4C: 32 40 B8        LD      ($B840),A           
1E4F: 3E 0C           LD      A,$0C               
1E51: 00              NOP                         
1E52: 32 40 B8        LD      ($B840),A           
1E55: 3E 0D           LD      A,$0D               
1E57: 32 40 B8        LD      ($B840),A           
1E5A: 00              NOP                         
1E5B: 0E 01           LD      C,$01               
1E5D: ED A0           LDI                         
1E5F: 3E 04           LD      A,$04               
1E61: 32 40 B8        LD      ($B840),A           
1E64: 10 D8           DJNZ    $120E               ; {}
1E66: AF              XOR     A                   
1E67: 32 3D 9B        LD      ($9B3D),A           
1E6A: C9              RET                         
1E6B: CD 73 1E        CALL    $1E73               ; {}
1E6E: AF              XOR     A                   
1E6F: 32 3D 9B        LD      ($9B3D),A           
1E72: C9              RET                         
1E73: 21 A0 89        LD      HL,$89A0            
1E76: 11 00 B8        LD      DE,$B800            
1E79: 06 25           LD      B,$25               
1E7B: 0E 01           LD      C,$01               
1E7D: ED A0           LDI                         
1E7F: 3E 0E           LD      A,$0E               
1E81: 32 40 B8        LD      ($B840),A           
1E84: CD 9C 1E        CALL    $1E9C               ; {}
1E87: 3E 04           LD      A,$04               
1E89: 32 40 B8        LD      ($B840),A           
1E8C: 3E 0A           LD      A,$0A               
1E8E: 32 40 B8        LD      ($B840),A           
1E91: CD 9C 1E        CALL    $1E9C               ; {}
1E94: 3E 04           LD      A,$04               
1E96: 32 40 B8        LD      ($B840),A           
1E99: 10 E0           DJNZ    $1216               ; {}
1E9B: C9              RET                         
1E9C: C5              PUSH    BC                  
1E9D: 01 DB 24        LD      BC,$24DB            
1EA0: 0D              DEC     C                   
1EA1: 20 FD           JR      NZ,$1233            ; {}
1EA3: 10 FB           DJNZ    $1231               ; {}
1EA5: C1              POP     BC                  
1EA6: C9              RET                         
1EA7: 21 30 B8        LD      HL,$B830            
1EAA: 11 FF 1E        LD      DE,$1EFF            
1EAD: 06 04           LD      B,$04               
1EAF: 36 00           LD      (HL),$00            
1EB1: 3E 08           LD      A,$08               
1EB3: 32 40 B8        LD      ($B840),A           
1EB6: 3C              INC     A                   
1EB7: 32 40 B8        LD      ($B840),A           
1EBA: 00              NOP                         
1EBB: 3E 08           LD      A,$08               
1EBD: 32 40 B8        LD      ($B840),A           
1EC0: 3E 0C           LD      A,$0C               
1EC2: 00              NOP                         
1EC3: 32 40 B8        LD      ($B840),A           
1EC6: 3E 0D           LD      A,$0D               
1EC8: 32 40 B8        LD      ($B840),A           
1ECB: 00              NOP                         
1ECC: 1A              LD      A,(DE)              
1ECD: AE              XOR     (HL)                
1ECE: C0              RET     NZ                  
1ECF: 23              INC     HL                  
1ED0: 13              INC     DE                  
1ED1: 3E 04           LD      A,$04               
1ED3: 32 40 B8        LD      ($B840),A           
1ED6: 10 D7           DJNZ    $120D               ; {}
1ED8: AF              XOR     A                   
1ED9: C9              RET                         
1EDA: 01 00 00        LD      BC,$0000            
1EDD: 01 00 00        LD      BC,$0000            
1EE0: 01 00 00        LD      BC,$0000            
1EE3: 01 00 00        LD      BC,$0000            
1EE6: 01 00 00        LD      BC,$0000            
1EE9: 00              NOP                         
1EEA: 28 35           JR      Z,$126B             ; {}
1EEC: 28 1C           JR      Z,$1252             ; {}
1EEE: 35              DEC     (HL)                
1EEF: 1C              INC     E                   
1EF0: 26 35           LD      H,$35               
1EF2: 26 1A           LD      H,$1A               
1EF4: 35              DEC     (HL)                
1EF5: 1A              LD      A,(DE)              
1EF6: 27              DAA                         
1EF7: 35              DEC     (HL)                
1EF8: 27              DAA                         
1EF9: 00              NOP                         
1EFA: 01 01 01        LD      BC,$0101            
1EFD: 01 01 A5        LD      BC,$A501            
1F00: C3 EE 18        JP      $18EE               ; {}
1F03: 21 00 00        LD      HL,$0000            
1F06: F3              DI                          
1F07: 11 FE 1F        LD      DE,$1FFE            
1F0A: 06 10           LD      B,$10               
1F0C: AF              XOR     A                   
1F0D: 86              ADD     A,(HL)              
1F0E: 2C              INC     L                   
1F0F: 20 FC           JR      NZ,$1232            ; {}
1F11: 24              INC     H                   
1F12: 10 F9           DJNZ    $122F               ; {}
1F14: EB              EX      DE,HL               
1F15: BE              CP      (HL)                
1F16: 20 10           JR      NZ,$1246            ; {}
1F18: EB              EX      DE,HL               
1F19: 1C              INC     E                   
1F1A: 20 EE           JR      NZ,$1224            ; {}
1F1C: 3E FF           LD      A,$FF               
1F1E: 32 00 8A        LD      ($8A00),A           
1F21: 3A 00 8A        LD      A,($8A00)           
1F24: A7              AND     A                   
1F25: 20 FA           JR      NZ,$1230            ; {}
1F27: C9              RET                         
1F28: 3E 06           LD      A,$06               
1F2A: 85              ADD     A,L                 
1F2B: 32 00 8A        LD      ($8A00),A           
1F2E: 18 F8           JR      $122E               ; {}
1F30: FF              RST     0X38                
1F31: FF              RST     0X38                
1F32: FF              RST     0X38                
1F33: FF              RST     0X38                
1F34: FF              RST     0X38                
1F35: FF              RST     0X38                
1F36: FF              RST     0X38                
1F37: FF              RST     0X38                
1F38: FF              RST     0X38                
1F39: FF              RST     0X38                
1F3A: FF              RST     0X38                
1F3B: FF              RST     0X38                
1F3C: FF              RST     0X38                
1F3D: FF              RST     0X38                
1F3E: FF              RST     0X38                
1F3F: FF              RST     0X38                
1F40: FF              RST     0X38                
1F41: FF              RST     0X38                
1F42: FF              RST     0X38                
1F43: FF              RST     0X38                
1F44: FF              RST     0X38                
1F45: FF              RST     0X38                
1F46: FF              RST     0X38                
1F47: FF              RST     0X38                
1F48: FF              RST     0X38                
1F49: FF              RST     0X38                
1F4A: FF              RST     0X38                
1F4B: FF              RST     0X38                
1F4C: FF              RST     0X38                
1F4D: FF              RST     0X38                
1F4E: FF              RST     0X38                
1F4F: FF              RST     0X38                
1F50: FF              RST     0X38                
1F51: FF              RST     0X38                
1F52: FF              RST     0X38                
1F53: FF              RST     0X38                
1F54: FF              RST     0X38                
1F55: FF              RST     0X38                
1F56: FF              RST     0X38                
1F57: FF              RST     0X38                
1F58: FF              RST     0X38                
1F59: FF              RST     0X38                
1F5A: FF              RST     0X38                
1F5B: FF              RST     0X38                
1F5C: FF              RST     0X38                
1F5D: FF              RST     0X38                
1F5E: FF              RST     0X38                
1F5F: FF              RST     0X38                
1F60: FF              RST     0X38                
1F61: FF              RST     0X38                
1F62: FF              RST     0X38                
1F63: FF              RST     0X38                
1F64: FF              RST     0X38                
1F65: FF              RST     0X38                
1F66: FF              RST     0X38                
1F67: FF              RST     0X38                
1F68: FF              RST     0X38                
1F69: FF              RST     0X38                
1F6A: FF              RST     0X38                
1F6B: FF              RST     0X38                
1F6C: FF              RST     0X38                
1F6D: FF              RST     0X38                
1F6E: FF              RST     0X38                
1F6F: FF              RST     0X38                
1F70: FF              RST     0X38                
1F71: FF              RST     0X38                
1F72: FF              RST     0X38                
1F73: FF              RST     0X38                
1F74: FF              RST     0X38                
1F75: FF              RST     0X38                
1F76: FF              RST     0X38                
1F77: FF              RST     0X38                
1F78: FF              RST     0X38                
1F79: FF              RST     0X38                
1F7A: FF              RST     0X38                
1F7B: FF              RST     0X38                
1F7C: FF              RST     0X38                
1F7D: FF              RST     0X38                
1F7E: FF              RST     0X38                
1F7F: FF              RST     0X38                
1F80: FF              RST     0X38                
1F81: FF              RST     0X38                
1F82: FF              RST     0X38                
1F83: FF              RST     0X38                
1F84: FF              RST     0X38                
1F85: FF              RST     0X38                
1F86: FF              RST     0X38                
1F87: FF              RST     0X38                
1F88: FF              RST     0X38                
1F89: FF              RST     0X38                
1F8A: FF              RST     0X38                
1F8B: FF              RST     0X38                
1F8C: FF              RST     0X38                
1F8D: FF              RST     0X38                
1F8E: FF              RST     0X38                
1F8F: FF              RST     0X38                
1F90: FF              RST     0X38                
1F91: FF              RST     0X38                
1F92: FF              RST     0X38                
1F93: FF              RST     0X38                
1F94: FF              RST     0X38                
1F95: FF              RST     0X38                
1F96: FF              RST     0X38                
1F97: FF              RST     0X38                
1F98: FF              RST     0X38                
1F99: FF              RST     0X38                
1F9A: FF              RST     0X38                
1F9B: FF              RST     0X38                
1F9C: FF              RST     0X38                
1F9D: FF              RST     0X38                
1F9E: FF              RST     0X38                
1F9F: FF              RST     0X38                
1FA0: FF              RST     0X38                
1FA1: FF              RST     0X38                
1FA2: FF              RST     0X38                
1FA3: FF              RST     0X38                
1FA4: FF              RST     0X38                
1FA5: FF              RST     0X38                
1FA6: FF              RST     0X38                
1FA7: FF              RST     0X38                
1FA8: FF              RST     0X38                
1FA9: FF              RST     0X38                
1FAA: FF              RST     0X38                
1FAB: FF              RST     0X38                
1FAC: FF              RST     0X38                
1FAD: FF              RST     0X38                
1FAE: FF              RST     0X38                
1FAF: FF              RST     0X38                
1FB0: FF              RST     0X38                
1FB1: FF              RST     0X38                
1FB2: FF              RST     0X38                
1FB3: FF              RST     0X38                
1FB4: FF              RST     0X38                
1FB5: FF              RST     0X38                
1FB6: FF              RST     0X38                
1FB7: FF              RST     0X38                
1FB8: FF              RST     0X38                
1FB9: FF              RST     0X38                
1FBA: FF              RST     0X38                
1FBB: FF              RST     0X38                
1FBC: FF              RST     0X38                
1FBD: FF              RST     0X38                
1FBE: FF              RST     0X38                
1FBF: FF              RST     0X38                
1FC0: FF              RST     0X38                
1FC1: FF              RST     0X38                
1FC2: FF              RST     0X38                
1FC3: FF              RST     0X38                
1FC4: FF              RST     0X38                
1FC5: FF              RST     0X38                
1FC6: FF              RST     0X38                
1FC7: FF              RST     0X38                
1FC8: FF              RST     0X38                
1FC9: FF              RST     0X38                
1FCA: FF              RST     0X38                
1FCB: FF              RST     0X38                
1FCC: FF              RST     0X38                
1FCD: FF              RST     0X38                
1FCE: FF              RST     0X38                
1FCF: FF              RST     0X38                
1FD0: FF              RST     0X38                
1FD1: FF              RST     0X38                
1FD2: FF              RST     0X38                
1FD3: FF              RST     0X38                
1FD4: FF              RST     0X38                
1FD5: FF              RST     0X38                
1FD6: FF              RST     0X38                
1FD7: FF              RST     0X38                
1FD8: FF              RST     0X38                
1FD9: FF              RST     0X38                
1FDA: FF              RST     0X38                
1FDB: FF              RST     0X38                
1FDC: FF              RST     0X38                
1FDD: FF              RST     0X38                
1FDE: FF              RST     0X38                
1FDF: FF              RST     0X38                
1FE0: FF              RST     0X38                
1FE1: FF              RST     0X38                
1FE2: FF              RST     0X38                
1FE3: FF              RST     0X38                
1FE4: FF              RST     0X38                
1FE5: FF              RST     0X38                
1FE6: FF              RST     0X38                
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
1FFD: 13              INC     DE                  
1FFE: 09              ADD     HL,BC               
1FFF: E1              POP     HL                  
```

