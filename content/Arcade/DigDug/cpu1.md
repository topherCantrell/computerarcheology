![DigDug](digdug.jpg)

# DigDug CPU1 Code

>>> cpu Z80

>>> binary 0000:roms/136007.101 + roms/136007.102 + roms/136007.103 + roms/dd1.4b

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
0000: F3              DI                          
0001: ED 56           IM      1                   
0003: C3 E6 00        JP      $00E6               ; {}
0006: FD ; ????
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
0038: C3 80 02        JP      $0280               ; {}
003B: 00              NOP                         
003C: 00              NOP                         
003D: 00              NOP                         
003E: 00              NOP                         
003F: 00              NOP                         
0040: 00              NOP                         
0041: 00              NOP                         
0042: 00              NOP                         
0043: 00              NOP                         
0044: 00              NOP                         
0045: 00              NOP                         
0046: 00              NOP                         
0047: 00              NOP                         
0048: 00              NOP                         
0049: 00              NOP                         
004A: 00              NOP                         
004B: 00              NOP                         
004C: 00              NOP                         
004D: 00              NOP                         
004E: 00              NOP                         
004F: 00              NOP                         
0050: 00              NOP                         
0051: 00              NOP                         
0052: 00              NOP                         
0053: 00              NOP                         
0054: 00              NOP                         
0055: 00              NOP                         
0056: 00              NOP                         
0057: 00              NOP                         
0058: 00              NOP                         
0059: 00              NOP                         
005A: 21 00 60        LD      HL,$6000            
005D: 32 30 68        LD      ($6830),A           
0060: 2B              DEC     HL                  
0061: 7D              LD      A,L                 
0062: B4              OR      H                   
0063: 20 F8           JR      NZ,$122E            ; {}
0065: C9              RET                         
0066: D9              EXX                         
0067: ED A0           LDI                         
0069: EA 9E 00        JP      PE,$009E            ; {}
006C: F5              PUSH    AF                  
006D: 2A 00 89        LD      HL,($8900)          
0070: 7E              LD      A,(HL)              
0071: A7              AND     A                   
0072: CA 98 00        JP      Z,$0098             ; {}
0075: 36 00           LD      (HL),$00            
0077: F5              PUSH    AF                  
0078: 2C              INC     L                   
0079: 2C              INC     L                   
007A: 4E              LD      C,(HL)              
007B: 2C              INC     L                   
007C: 46              LD      B,(HL)              
007D: 2C              INC     L                   
007E: 5E              LD      E,(HL)              
007F: 2C              INC     L                   
0080: 56              LD      D,(HL)              
0081: 2C              INC     L                   
0082: 7E              LD      A,(HL)              
0083: 2C              INC     L                   
0084: 2C              INC     L                   
0085: 22 00 89        LD      ($8900),HL          
0088: 2D              DEC     L                   
0089: 66              LD      H,(HL)              
008A: 6F              LD      L,A                 
008B: 3E 10           LD      A,$10               
008D: 32 00 71        LD      ($7100),A           
0090: F1              POP     AF                  
0091: D9              EXX                         
0092: 32 00 71        LD      ($7100),A           
0095: F1              POP     AF                  
0096: ED 45           RETN                        
0098: 3E 10           LD      A,$10               
009A: 32 00 71        LD      ($7100),A           
009D: F1              POP     AF                  
009E: D9              EXX                         
009F: ED 45           RETN                        
00A1: 08              EX      AF,AF'              
00A2: F3              DI                          
00A3: 3A 00 71        LD      A,($7100)           
00A6: E6 E0           AND     $E0                 
00A8: 20 07           JR      NZ,$123D            ; {}
00AA: 08              EX      AF,AF'              
00AB: D9              EXX                         
00AC: 32 00 71        LD      ($7100),A           
00AF: FB              EI                          
00B0: C9              RET                         
00B1: E5              PUSH    HL                  
00B2: D5              PUSH    DE                  
00B3: EB              EX      DE,HL               
00B4: 2A 02 89        LD      HL,($8902)          
00B7: 7D              LD      A,L                 
00B8: C6 08           ADD     $08                 
00BA: 6F              LD      L,A                 
00BB: 22 02 89        LD      ($8902),HL          
00BE: 2D              DEC     L                   
00BF: 72              LD      (HL),D              
00C0: 2D              DEC     L                   
00C1: 73              LD      (HL),E              
00C2: 2D              DEC     L                   
00C3: D1              POP     DE                  
00C4: 72              LD      (HL),D              
00C5: 2D              DEC     L                   
00C6: 73              LD      (HL),E              
00C7: 2D              DEC     L                   
00C8: 70              LD      (HL),B              
00C9: 2D              DEC     L                   
00CA: 71              LD      (HL),C              
00CB: 32 30 68        LD      ($6830),A           
00CE: 2D              DEC     L                   
00CF: 2D              DEC     L                   
00D0: 08              EX      AF,AF'              
00D1: 77              LD      (HL),A              
00D2: 3A 00 71        LD      A,($7100)           
00D5: FE 10           CP      $10                 
00D7: 28 03           JR      Z,$1239             ; {}
00D9: E1              POP     HL                  
00DA: FB              EI                          
00DB: C9              RET                         
00DC: 7E              LD      A,(HL)              
00DD: 36 00           LD      (HL),$00            
00DF: 22 02 89        LD      ($8902),HL          
00E2: E1              POP     HL                  
00E3: C3 AA 00        JP      $00AA               ; {}
00E6: 3E 10           LD      A,$10               
00E8: 32 00 71        LD      ($7100),A           
00EB: 32 00 70        LD      ($7000),A           
00EE: 21 20 68        LD      HL,$6820            
00F1: 77              LD      (HL),A              
00F2: 23              INC     HL                  
00F3: 77              LD      (HL),A              
00F4: 23              INC     HL                  
00F5: 36 01           LD      (HL),$01            
00F7: 23              INC     HL                  
00F8: 77              LD      (HL),A              
00F9: 3C              INC     A                   
00FA: 32 30 68        LD      ($6830),A           
00FD: 23              INC     HL                  
00FE: 23              INC     HL                  
00FF: 3E FF           LD      A,$FF               
0101: 77              LD      (HL),A              
0102: 23              INC     HL                  
0103: 77              LD      (HL),A              
0104: 23              INC     HL                  
0105: 77              LD      (HL),A              
0106: AF              XOR     A                   
0107: 21 E0 89        LD      HL,$89E0            
010A: 06 0B           LD      B,$0B               
010C: 77              LD      (HL),A              
010D: 23              INC     HL                  
010E: 10 FC           DJNZ    $1232               ; {}
0110: 21 EF 89        LD      HL,$89EF            
0113: 06 04           LD      B,$04               
0115: 77              LD      (HL),A              
0116: 23              INC     HL                  
0117: 10 FC           DJNZ    $1232               ; {}
0119: C3 76 38        JP      $3876               ; {}
011C: F3              DI                          
011D: AF              XOR     A                   
011E: 32 20 68        LD      ($6820),A           
0121: 21 07 A0        LD      HL,$A007            
0124: 77              LD      (HL),A              
0125: 21 1B 9B        LD      HL,$9B1B            
0128: 36 10           LD      (HL),$10            
012A: 3E 88           LD      A,$88               
012C: 21 00 84        LD      HL,$8400            
012F: 36 00           LD      (HL),$00            
0131: 32 30 68        LD      ($6830),A           
0134: 23              INC     HL                  
0135: BC              CP      H                   
0136: 20 F7           JR      NZ,$122D            ; {}
0138: 3E 94           LD      A,$94               
013A: 21 00 90        LD      HL,$9000            
013D: 36 00           LD      (HL),$00            
013F: 32 30 68        LD      ($6830),A           
0142: 23              INC     HL                  
0143: BC              CP      H                   
0144: 20 F7           JR      NZ,$122D            ; {}
0146: 21 33 9B        LD      HL,$9B33            
0149: 36 00           LD      (HL),$00            
014B: 21 80 9A        LD      HL,$9A80            
014E: 06 20           LD      B,$20               
0150: 36 00           LD      (HL),$00            
0152: 32 30 68        LD      ($6830),A           
0155: 23              INC     HL                  
0156: 10 F8           DJNZ    $122E               ; {}
0158: 21 00 98        LD      HL,$9800            
015B: 01 80 01        LD      BC,$0180            
015E: 32 30 68        LD      ($6830),A           
0161: 36 00           LD      (HL),$00            
0163: 23              INC     HL                  
0164: 0B              DEC     BC                  
0165: 78              LD      A,B                 
0166: B1              OR      C                   
0167: 20 F5           JR      NZ,$122B            ; {}
0169: 3E 01           LD      A,$01               
016B: 32 23 68        LD      ($6823),A           
016E: 3A D0 89        LD      A,($89D0)           
0171: FE 00           CP      $00                 
0173: CA 00 00        JP      Z,$0000             ; {ram.$00}
0176: FE FF           CP      $FF                 
0178: 20 08           JR      NZ,$123E            ; {}
017A: 3E 00           LD      A,$00               
017C: 32 C0 87        LD      ($87C0),A           
017F: C3 B4 01        JP      $01B4               ; {}
0182: 21 AA 85        LD      HL,$85AA            
0185: 36 00           LD      (HL),$00            
0187: 23              INC     HL                  
0188: E6 0F           AND     $0F                 
018A: 77              LD      (HL),A              
018B: 3A D1 89        LD      A,($89D1)           
018E: FE FF           CP      $FF                 
0190: 20 08           JR      NZ,$123E            ; {}
0192: 3E 01           LD      A,$01               
0194: 32 C0 87        LD      ($87C0),A           
0197: C3 B4 01        JP      $01B4               ; {}
019A: 47              LD      B,A                 
019B: 21 AC 85        LD      HL,$85AC            
019E: 36 00           LD      (HL),$00            
01A0: 23              INC     HL                  
01A1: E6 0F           AND     $0F                 
01A3: 77              LD      (HL),A              
01A4: 78              LD      A,B                 
01A5: E6 F0           AND     $F0                 
01A7: FE 10           CP      $10                 
01A9: 20 04           JR      NZ,$123A            ; {}
01AB: 3E 02           LD      A,$02               
01AD: 18 02           JR      $1238               ; {}
01AF: 3E 03           LD      A,$03               
01B1: 32 C0 87        LD      ($87C0),A           
01B4: 31 00 9A        LD      SP,$9A00            
01B7: CD 5A 00        CALL    $005A               ; {}
01BA: 21 00 88        LD      HL,$8800            
01BD: 22 00 89        LD      ($8900),HL          
01C0: 22 02 89        LD      ($8902),HL          
01C3: AF              XOR     A                   
01C4: 21 00 A0        LD      HL,$A000            
01C7: 06 04           LD      B,$04               
01C9: 36 00           LD      (HL),$00            
01CB: 23              INC     HL                  
01CC: 10 FB           DJNZ    $1231               ; {}
01CE: CD 5A 00        CALL    $005A               ; {}
01D1: 21 04 89        LD      HL,$8904            
01D4: 06 04           LD      B,$04               
01D6: 36 02           LD      (HL),$02            
01D8: 23              INC     HL                  
01D9: 10 FB           DJNZ    $1231               ; {}
01DB: 21 04 89        LD      HL,$8904            
01DE: 11 00 70        LD      DE,$7000            
01E1: 01 04 00        LD      BC,$0004            
01E4: 3E C1           LD      A,$C1               
01E6: CD A1 00        CALL    $00A1               ; {}
01E9: CD A4 15        CALL    $15A4               ; {}
01EC: 21 00 80        LD      HL,$8000            
01EF: 06 40           LD      B,$40               
01F1: 36 7F           LD      (HL),$7F            
01F3: 23              INC     HL                  
01F4: 32 30 68        LD      ($6830),A           
01F7: 10 F8           DJNZ    $122E               ; {}
01F9: 21 ED 83        LD      HL,$83ED            
01FC: 11 09 00        LD      DE,$0009            
01FF: 06 02           LD      B,$02               
0201: 3E 10           LD      A,$10               
0203: 77              LD      (HL),A              
0204: 23              INC     HL                  
0205: 77              LD      (HL),A              
0206: 19              ADD     HL,DE               
0207: 10 FA           DJNZ    $1230               ; {}
0209: CD A1 19        CALL    $19A1               ; {}
020C: CD 4D 14        CALL    $144D               ; {}
020F: CD 30 14        CALL    $1430               ; {}
0212: 3E FF           LD      A,$FF               
0214: 32 87 87        LD      ($8787),A           
0217: 21 27 89        LD      HL,$8927            
021A: 11 AE 89        LD      DE,$89AE            
021D: 06 03           LD      B,$03               
021F: 1A              LD      A,(DE)              
0220: 77              LD      (HL),A              
0221: 23              INC     HL                  
0222: 1B              DEC     DE                  
0223: 10 FA           DJNZ    $1230               ; {}
0225: CD DC 14        CALL    $14DC               ; {}
0228: 3E 01           LD      A,$01               
022A: 21 A9 87        LD      HL,$87A9            
022D: 77              LD      (HL),A              
022E: 23              INC     HL                  
022F: 77              LD      (HL),A              
0230: 23              INC     HL                  
0231: 77              LD      (HL),A              
0232: 32 05 9A        LD      ($9A05),A           
0235: 32 20 68        LD      ($6820),A           
0238: FB              EI                          
0239: 31 00 9A        LD      SP,$9A00            
023C: 21 00 84        LD      HL,$8400            
023F: CB 4E           BIT     1,(HL)              
0241: 20 08           JR      NZ,$123E            ; {}
0243: 21 14 84        LD      HL,$8414            
0246: 3A 0D 84        LD      A,($840D)           
0249: 18 06           JR      $123C               ; {}
024B: 21 17 84        LD      HL,$8417            
024E: 3A 0E 84        LD      A,($840E)           
0251: 47              LD      B,A                 
0252: 3A CC 87        LD      A,($87CC)           
0255: CB 4F           BIT     1,A                 
0257: 28 19           JR      Z,$124F             ; {}
0259: CB 57           BIT     2,A                 
025B: 20 15           JR      NZ,$124B            ; {}
025D: 78              LD      A,B                 
025E: E5              PUSH    HL                  
025F: F5              PUSH    AF                  
0260: CD F2 0B        CALL    $0BF2               ; {}
0263: F1              POP     AF                  
0264: E1              POP     HL                  
0265: CD E8 32        CALL    $32E8               ; {}
0268: 21 03 A0        LD      HL,$A003            
026B: 36 00           LD      (HL),$00            
026D: 21 CC 87        LD      HL,$87CC            
0270: CB 8E           RES     1,(HL)              
0272: 21 CC 87        LD      HL,$87CC            
0275: CB 46           BIT     0,(HL)              
0277: 28 05           JR      Z,$123B             ; {}
0279: CB 86           RES     0,(HL)              
027B: CD DB 35        CALL    $35DB               ; {}
027E: 18 B8           JR      $11EE               ; {}
0280: DD E5           PUSH    IX                  
0282: FD E5           PUSH    IY                  
0284: E5              PUSH    HL                  
0285: D5              PUSH    DE                  
0286: C5              PUSH    BC                  
0287: F5              PUSH    AF                  
0288: AF              XOR     A                   
0289: 32 20 68        LD      ($6820),A           
028C: 32 30 68        LD      ($6830),A           
028F: 3A 9A 87        LD      A,($879A)           
0292: A7              AND     A                   
0293: 20 2B           JR      NZ,$1261            ; {}
0295: 21 00 98        LD      HL,$9800            
0298: 11 80 8B        LD      DE,$8B80            
029B: 01 80 00        LD      BC,$0080            
029E: C5              PUSH    BC                  
029F: ED B0           LDIR                        
02A1: C1              POP     BC                  
02A2: 21 00 99        LD      HL,$9900            
02A5: 11 80 9B        LD      DE,$9B80            
02A8: ED B0           LDIR                        
02AA: 3A CF 87        LD      A,($87CF)           
02AD: CB 6F           BIT     5,A                 
02AF: CA 27 0A        JP      Z,$0A27             ; {}
02B2: 3A 8E 89        LD      A,($898E)           
02B5: 21 00 84        LD      HL,$8400            
02B8: 2F              CPL                         
02B9: E6 04           AND     $04                 
02BB: B6              OR      (HL)                
02BC: 77              LD      (HL),A              
02BD: CD B1 0B        CALL    $0BB1               ; {}
02C0: 2A 23 84        LD      HL,($8423)          
02C3: 23              INC     HL                  
02C4: 22 23 84        LD      ($8423),HL          
02C7: 3A 9A 87        LD      A,($879A)           
02CA: A7              AND     A                   
02CB: 20 06           JR      NZ,$123C            ; {}
02CD: 3A A5 85        LD      A,($85A5)           
02D0: 32 A6 85        LD      ($85A6),A           
02D3: 21 00 70        LD      HL,$7000            
02D6: 11 A7 85        LD      DE,$85A7            
02D9: 01 03 00        LD      BC,$0003            
02DC: 3E 71           LD      A,$71               
02DE: CD A1 00        CALL    $00A1               ; {}
02E1: 3A 9A 87        LD      A,($879A)           
02E4: A7              AND     A                   
02E5: C2 27 0A        JP      NZ,$0A27            ; {}
02E8: 21 A7 87        LD      HL,$87A7            
02EB: CB 46           BIT     0,(HL)              
02ED: 28 26           JR      Z,$125C             ; {}
02EF: CB 86           RES     0,(HL)              
02F1: 21 11 84        LD      HL,$8411            
02F4: AF              XOR     A                   
02F5: 77              LD      (HL),A              
02F6: 23              INC     HL                  
02F7: 3A E7 87        LD      A,($87E7)           
02FA: 77              LD      (HL),A              
02FB: 23              INC     HL                  
02FC: AF              XOR     A                   
02FD: 77              LD      (HL),A              
02FE: CD C0 2F        CALL    $2FC0               ; {}
0301: 3A 57 86        LD      A,($8657)           
0304: CB 4F           BIT     1,A                 
0306: 20 0D           JR      NZ,$1243            ; {}
0308: CD 69 14        CALL    $1469               ; {}
030B: 3A 00 84        LD      A,($8400)           
030E: CB 5F           BIT     3,A                 
0310: 20 03           JR      NZ,$1239            ; {}
0312: CD DF 0B        CALL    $0BDF               ; {}
0315: 21 00 84        LD      HL,$8400            
0318: CB 4E           BIT     1,(HL)              
031A: 20 14           JR      NZ,$124A            ; {}
031C: 3A A8 85        LD      A,($85A8)           
031F: 47              LD      B,A                 
0320: E6 0F           AND     $0F                 
0322: FE 09           CP      $09                 
0324: 38 02           JR      C,$1238             ; {}
0326: CB 98           RES     3,B                 
0328: 78              LD      A,B                 
0329: CB 87           RES     0,A                 
032B: 32 B0 85        LD      ($85B0),A           
032E: 18 0C           JR      $1242               ; {}
0330: CB 56           BIT     2,(HL)              
0332: 28 E8           JR      Z,$121E             ; {}
0334: 3A A9 85        LD      A,($85A9)           
0337: 18 E6           JR      $121C               ; {}
0339: 32 B0 85        LD      ($85B0),A           
033C: 21 24 86        LD      HL,$8624            
033F: 11 B0 85        LD      DE,$85B0            
0342: 1A              LD      A,(DE)              
0343: E6 30           AND     $30                 
0345: 77              LD      (HL),A              
0346: 21 A5 85        LD      HL,$85A5            
0349: 11 A6 85        LD      DE,$85A6            
034C: 3A A7 85        LD      A,($85A7)           
034F: 77              LD      (HL),A              
0350: FE B0           CP      $B0                 
0352: D2 76 38        JP      NC,$3876            ; {}
0355: E6 0F           AND     $0F                 
0357: FE 0A           CP      $0A                 
0359: D2 76 38        JP      NC,$3876            ; {}
035C: 7E              LD      A,(HL)              
035D: A7              AND     A                   
035E: 20 0E           JR      NZ,$1244            ; {}
0360: 1A              LD      A,(DE)              
0361: A7              AND     A                   
0362: 20 0A           JR      NZ,$1240            ; {}
0364: 3A 00 84        LD      A,($8400)           
0367: CB 77           BIT     6,A                 
0369: CA 80 0A        JP      Z,$0A80             ; {}
036C: 18 5A           JR      $1290               ; {}
036E: 3A CC 87        LD      A,($87CC)           
0371: CB 4F           BIT     1,A                 
0373: 20 16           JR      NZ,$124C            ; {}
0375: CB 47           BIT     0,A                 
0377: 20 12           JR      NZ,$1248            ; {}
0379: 1A              LD      A,(DE)              
037A: 47              LD      B,A                 
037B: 7E              LD      A,(HL)              
037C: FE 90           CP      $90                 
037E: 30 0B           JR      NC,$1241            ; {}
0380: 90              SUB     B                   
0381: 27              DAA                         
0382: 4F              LD      C,A                 
0383: 38 06           JR      C,$123C             ; {}
0385: 28 04           JR      Z,$123A             ; {}
0387: 79              LD      A,C                 
0388: 32 33 9B        LD      ($9B33),A           
038B: 7E              LD      A,(HL)              
038C: EB              EX      DE,HL               
038D: BE              CP      (HL)                
038E: 30 30           JR      NC,$1266            ; {}
0390: 1A              LD      A,(DE)              
0391: FE 99           CP      $99                 
0393: 28 0A           JR      Z,$1240             ; {}
0395: FE 9F           CP      $9F                 
0397: 28 06           JR      Z,$123C             ; {}
0399: C6 01           ADD     $01                 
039B: 27              DAA                         
039C: BE              CP      (HL)                
039D: 20 14           JR      NZ,$124A            ; {}
039F: 21 00 84        LD      HL,$8400            
03A2: CB 86           RES     0,(HL)              
03A4: CB 8E           RES     1,(HL)              
03A6: CB F6           SET     6,(HL)              
03A8: 3E 01           LD      A,$01               
03AA: 21 E1 89        LD      HL,$89E1            
03AD: CD 24 12        CALL    $1224               ; {}
03B0: C3 27 0A        JP      $0A27               ; {}
03B3: 21 00 84        LD      HL,$8400            
03B6: CB C6           SET     0,(HL)              
03B8: CB 8E           RES     1,(HL)              
03BA: CB F6           SET     6,(HL)              
03BC: 3E 02           LD      A,$02               
03BE: 18 EA           JR      $1220               ; {}
03C0: 21 00 84        LD      HL,$8400            
03C3: CB 76           BIT     6,(HL)              
03C5: CA 03 0B        JP      Z,$0B03             ; {}
03C8: 21 57 86        LD      HL,$8657            
03CB: CB 86           RES     0,(HL)              
03CD: CB 4E           BIT     1,(HL)              
03CF: C2 27 0A        JP      NZ,$0A27            ; {}
03D2: 21 F3 89        LD      HL,$89F3            
03D5: 34              INC     (HL)                
03D6: 21 88 9A        LD      HL,$9A88            
03D9: 7E              LD      A,(HL)              
03DA: A7              AND     A                   
03DB: C2 27 0A        JP      NZ,$0A27            ; {}
03DE: 21 00 84        LD      HL,$8400            
03E1: CB 5E           BIT     3,(HL)              
03E3: C2 45 04        JP      NZ,$0445            ; {}
03E6: CB DE           SET     3,(HL)              
03E8: CD A4 15        CALL    $15A4               ; {}
03EB: CD 7A 17        CALL    $177A               ; {}
03EE: CD EB 17        CALL    $17EB               ; {}
03F1: CD 7D 18        CALL    $187D               ; {}
03F4: CD 90 18        CALL    $1890               ; {}
03F7: CD 5A 00        CALL    $005A               ; {}
03FA: 3A B0 85        LD      A,($85B0)           
03FD: CB 6F           BIT     5,A                 
03FF: 28 05           JR      Z,$123B             ; {}
0401: 21 87 87        LD      HL,$8787            
0404: 36 FF           LD      (HL),$FF            
0406: CD 22 0C        CALL    $0C22               ; {}
0409: 3A CF 87        LD      A,($87CF)           
040C: CB 5F           BIT     3,A                 
040E: 20 19           JR      NZ,$124F            ; {}
0410: 3A 87 87        LD      A,($8787)           
0413: CB 4F           BIT     1,A                 
0415: 20 12           JR      NZ,$1248            ; {}
0417: 3A 0E 84        LD      A,($840E)           
041A: 6F              LD      L,A                 
041B: 67              LD      H,A                 
041C: 32 0F 84        LD      ($840F),A           
041F: 22 27 86        LD      ($8627),HL          
0422: 21 85 87        LD      HL,$8785            
0425: 36 00           LD      (HL),$00            
0427: 18 10           JR      $1246               ; {}
0429: 3E 01           LD      A,$01               
042B: 32 0F 84        LD      ($840F),A           
042E: 21 01 01        LD      HL,$0101            
0431: 22 27 86        LD      ($8627),HL          
0434: 21 85 87        LD      HL,$8785            
0437: 36 00           LD      (HL),$00            
0439: CD AA 18        CALL    $18AA               ; {}
043C: CD AF 12        CALL    $12AF               ; {}
043F: CD 51 0C        CALL    $0C51               ; {}
0442: C3 27 0A        JP      $0A27               ; {}
0445: CB 7E           BIT     7,(HL)              
0447: 20 47           JR      NZ,$127D            ; {}
0449: CB FE           SET     7,(HL)              
044B: CD AC 17        CALL    $17AC               ; {}
044E: CD 15 0C        CALL    $0C15               ; {}
0451: CD 4F 15        CALL    $154F               ; {}
0454: 21 00 00        LD      HL,$0000            
0457: 3A 00 84        LD      A,($8400)           
045A: CB 4F           BIT     1,A                 
045C: 20 09           JR      NZ,$123F            ; {}
045E: AF              XOR     A                   
045F: 32 DA 87        LD      ($87DA),A           
0462: 22 D4 87        LD      ($87D4),HL          
0465: 18 07           JR      $123D               ; {}
0467: AF              XOR     A                   
0468: 32 D8 87        LD      ($87D8),A           
046B: 22 D2 87        LD      ($87D2),HL          
046E: 32 99 87        LD      ($8799),A           
0471: 32 EB 87        LD      ($87EB),A           
0474: 22 ED 87        LD      ($87ED),HL          
0477: 32 6D 89        LD      ($896D),A           
047A: 32 6C 89        LD      ($896C),A           
047D: 32 F0 87        LD      ($87F0),A           
0480: 21 9E 98        LD      HL,$989E            
0483: 77              LD      (HL),A              
0484: 23              INC     HL                  
0485: 36 E0           LD      (HL),$E0            
0487: CD A6 0B        CALL    $0BA6               ; {}
048A: CD B1 0B        CALL    $0BB1               ; {}
048D: C3 27 0A        JP      $0A27               ; {}
0490: 21 00 84        LD      HL,$8400            
0493: CB 66           BIT     4,(HL)              
0495: 20 33           JR      NZ,$1269            ; {}
0497: CB E6           SET     4,(HL)              
0499: CD F5 19        CALL    $19F5               ; {}
049C: 3A 27 86        LD      A,($8627)           
049F: 3D              DEC     A                   
04A0: 4F              LD      C,A                 
04A1: D6 0C           SUB     $0C                 
04A3: 30 FB           JR      NC,$1231            ; {}
04A5: 79              LD      A,C                 
04A6: 1F              RRA                         
04A7: 1F              RRA                         
04A8: 4F              LD      C,A                 
04A9: E6 01           AND     $01                 
04AB: 32 04 A0        LD      ($A004),A           
04AE: 79              LD      A,C                 
04AF: 1F              RRA                         
04B0: E6 01           AND     $01                 
04B2: 32 05 A0        LD      ($A005),A           
04B5: CD 05 0C        CALL    $0C05               ; {}
04B8: CD 09 14        CALL    $1409               ; {}
04BB: CD 43 18        CALL    $1843               ; {}
04BE: CD 4F 15        CALL    $154F               ; {}
04C1: CD A6 0B        CALL    $0BA6               ; {}
04C4: CD B1 0B        CALL    $0BB1               ; {}
04C7: C3 27 0A        JP      $0A27               ; {}
04CA: E5              PUSH    HL                  
04CB: 3A 57 86        LD      A,($8657)           
04CE: CB 4F           BIT     1,A                 
04D0: 20 06           JR      NZ,$123C            ; {}
04D2: CD 81 0C        CALL    $0C81               ; {}
04D5: CD 69 14        CALL    $1469               ; {}
04D8: E1              POP     HL                  
04D9: CB 6E           BIT     5,(HL)              
04DB: C2 C7 05        JP      NZ,$05C7            ; {}
04DE: CB EE           SET     5,(HL)              
04E0: 21 68 10        LD      HL,$1068            
04E3: 22 25 86        LD      ($8625),HL          
04E6: AF              XOR     A                   
04E7: 32 4A 86        LD      ($864A),A           
04EA: 32 53 86        LD      ($8653),A           
04ED: CD F5 19        CALL    $19F5               ; {}
04F0: CD 4F 15        CALL    $154F               ; {}
04F3: 21 4B 86        LD      HL,$864B            
04F6: 06 08           LD      B,$08               
04F8: 0E 02           LD      C,$02               
04FA: 3A 57 86        LD      A,($8657)           
04FD: CB 47           BIT     0,A                 
04FF: 20 11           JR      NZ,$1247            ; {}
0501: 3A 27 86        LD      A,($8627)           
0504: FE 14           CP      $14                 
0506: 38 0A           JR      C,$1240             ; {}
0508: FE 20           CP      $20                 
050A: 30 04           JR      NC,$123A            ; {}
050C: 0E 01           LD      C,$01               
050E: 18 02           JR      $1238               ; {}
0510: 0E 00           LD      C,$00               
0512: 3E 02           LD      A,$02               
0514: 77              LD      (HL),A              
0515: 23              INC     HL                  
0516: 91              SUB     C                   
0517: 10 FB           DJNZ    $1231               ; {}
0519: CD EA 11        CALL    $11EA               ; {}
051C: CD DE 11        CALL    $11DE               ; {}
051F: 21 A1 83        LD      HL,$83A1            
0522: 11 20 00        LD      DE,$0020            
0525: 19              ADD     HL,DE               
0526: 3E 7F           LD      A,$7F               
0528: 77              LD      (HL),A              
0529: 23              INC     HL                  
052A: 77              LD      (HL),A              
052B: 19              ADD     HL,DE               
052C: 77              LD      (HL),A              
052D: 2B              DEC     HL                  
052E: 77              LD      (HL),A              
052F: 21 9E 98        LD      HL,$989E            
0532: AF              XOR     A                   
0533: 77              LD      (HL),A              
0534: 23              INC     HL                  
0535: 36 E0           LD      (HL),$E0            
0537: 32 EF 87        LD      ($87EF),A           
053A: 32 F0 87        LD      ($87F0),A           
053D: 21 00 00        LD      HL,$0000            
0540: 22 D6 87        LD      ($87D6),HL          
0543: 32 6F 89        LD      ($896F),A           
0546: 32 6C 89        LD      ($896C),A           
0549: 32 A7 87        LD      ($87A7),A           
054C: 32 B3 85        LD      ($85B3),A           
054F: 32 22 99        LD      ($9922),A           
0552: 21 28 85        LD      HL,$8528            
0555: 11 10 00        LD      DE,$0010            
0558: 0E 00           LD      C,$00               
055A: 06 08           LD      B,$08               
055C: CB 7E           BIT     7,(HL)              
055E: 28 01           JR      Z,$1237             ; {}
0560: 0C              INC     C                   
0561: 19              ADD     HL,DE               
0562: 10 F8           DJNZ    $122E               ; {}
0564: 79              LD      A,C                 
0565: FE 08           CP      $08                 
0567: 20 0F           JR      NZ,$1245            ; {}
0569: CD 7B 1B        CALL    $1B7B               ; {}
056C: 21 6C 89        LD      HL,$896C            
056F: CB DE           SET     3,(HL)              
0571: 21 01 84        LD      HL,$8401            
0574: CB EE           SET     5,(HL)              
0576: 18 0E           JR      $1244               ; {}
0578: CD 2C 1B        CALL    $1B2C               ; {}
057B: CD 7B 1B        CALL    $1B7B               ; {}
057E: CD 43 18        CALL    $1843               ; {}
0581: 21 01 84        LD      HL,$8401            
0584: CB AE           RES     5,(HL)              
0586: 21 93 9A        LD      HL,$9A93            
0589: 36 00           LD      (HL),$00            
058B: 21 87 87        LD      HL,$8787            
058E: 36 FF           LD      (HL),$FF            
0590: CD A6 0B        CALL    $0BA6               ; {}
0593: CD B1 0B        CALL    $0BB1               ; {}
0596: 3E 02           LD      A,$02               
0598: 32 AE 85        LD      ($85AE),A           
059B: 32 AF 85        LD      ($85AF),A           
059E: 21 E0 01        LD      HL,$01E0            
05A1: 22 F2 85        LD      ($85F2),HL          
05A4: 21 01 84        LD      HL,$8401            
05A7: CB B6           RES     6,(HL)              
05A9: 32 30 68        LD      ($6830),A           
05AC: 21 00 00        LD      HL,$0000            
05AF: 22 F4 85        LD      ($85F4),HL          
05B2: 3A 57 86        LD      A,($8657)           
05B5: CB 4F           BIT     1,A                 
05B7: 28 05           JR      Z,$123B             ; {}
05B9: 3E 80           LD      A,$80               
05BB: 32 76 86        LD      ($8676),A           
05BE: CD A6 0B        CALL    $0BA6               ; {}
05C1: CD B1 0B        CALL    $0BB1               ; {}
05C4: C3 27 0A        JP      $0A27               ; {}
05C7: 3A 6C 89        LD      A,($896C)           
05CA: CB 5F           BIT     3,A                 
05CC: 20 61           JR      NZ,$1297            ; {}
05CE: 21 01 84        LD      HL,$8401            
05D1: CB 6E           BIT     5,(HL)              
05D3: 20 30           JR      NZ,$1266            ; {}
05D5: E5              PUSH    HL                  
05D6: CD 92 1C        CALL    $1C92               ; {}
05D9: 3E 78           LD      A,$78               
05DB: 32 D5 85        LD      ($85D5),A           
05DE: E1              POP     HL                  
05DF: CB EE           SET     5,(HL)              
05E1: 21 85 87        LD      HL,$8785            
05E4: 3A 00 84        LD      A,($8400)           
05E7: CB 4F           BIT     1,A                 
05E9: 20 0D           JR      NZ,$1243            ; {}
05EB: CB 46           BIT     0,(HL)              
05ED: C2 27 0A        JP      NZ,$0A27            ; {}
05F0: 3E 01           LD      A,$01               
05F2: 32 81 9A        LD      ($9A81),A           
05F5: C3 27 0A        JP      $0A27               ; {}
05F8: CB 4E           BIT     1,(HL)              
05FA: C2 27 0A        JP      NZ,$0A27            ; {}
05FD: 3E 01           LD      A,$01               
05FF: 32 81 9A        LD      ($9A81),A           
0602: C3 27 0A        JP      $0A27               ; {}
0605: 21 81 9A        LD      HL,$9A81            
0608: 7E              LD      A,(HL)              
0609: A7              AND     A                   
060A: C2 27 0A        JP      NZ,$0A27            ; {}
060D: 3A D5 85        LD      A,($85D5)           
0610: A7              AND     A                   
0611: 28 0C           JR      Z,$1242             ; {}
0613: FE 01           CP      $01                 
0615: CC D1 1C        CALL    Z,$1CD1             ; {}
0618: 21 D5 85        LD      HL,$85D5            
061B: 35              DEC     (HL)                
061C: C3 27 0A        JP      $0A27               ; {}
061F: 21 85 87        LD      HL,$8785            
0622: 3A 00 84        LD      A,($8400)           
0625: CB 4F           BIT     1,A                 
0627: 20 04           JR      NZ,$123A            ; {}
0629: CB C6           SET     0,(HL)              
062B: 18 02           JR      $1238               ; {}
062D: CB CE           SET     1,(HL)              
062F: 21 6C 89        LD      HL,$896C            
0632: CB DE           SET     3,(HL)              
0634: 3A 46 86        LD      A,($8646)           
0637: CB 4F           BIT     1,A                 
0639: 28 19           JR      Z,$124F             ; {}
063B: 21 86 9A        LD      HL,$9A86            
063E: 3E 00           LD      A,$00               
0640: 77              LD      (HL),A              
0641: 21 89 9A        LD      HL,$9A89            
0644: 77              LD      (HL),A              
0645: 21 47 86        LD      HL,$8647            
0648: 7E              LD      A,(HL)              
0649: A7              AND     A                   
064A: 20 07           JR      NZ,$123D            ; {}
064C: 21 01 84        LD      HL,$8401            
064F: CB FE           SET     7,(HL)              
0651: 18 01           JR      $1237               ; {}
0653: 35              DEC     (HL)                
0654: 21 6F 89        LD      HL,$896F            
0657: CB 46           BIT     0,(HL)              
0659: 20 15           JR      NZ,$124B            ; {}
065B: CB C6           SET     0,(HL)              
065D: 21 00 00        LD      HL,$0000            
0660: 22 23 84        LD      ($8423),HL          
0663: AF              XOR     A                   
0664: 21 B0 85        LD      HL,$85B0            
0667: CD 62 19        CALL    $1962               ; {}
066A: 21 F4 85        LD      HL,$85F4            
066D: 77              LD      (HL),A              
066E: 23              INC     HL                  
066F: 77              LD      (HL),A              
0670: 21 F0 87        LD      HL,$87F0            
0673: CB 4E           BIT     1,(HL)              
0675: C2 49 09        JP      NZ,$0949            ; {}
0678: 21 01 84        LD      HL,$8401            
067B: CB 7E           BIT     7,(HL)              
067D: CA 49 09        JP      Z,$0949             ; {}
0680: AF              XOR     A                   
0681: 32 92 9A        LD      ($9A92),A           
0684: 23              INC     HL                  
0685: CB 46           BIT     0,(HL)              
0687: C2 98 07        JP      NZ,$0798            ; {}
068A: 21 1C 86        LD      HL,$861C            
068D: 35              DEC     (HL)                
068E: 7E              LD      A,(HL)              
068F: FE 64           CP      $64                 
0691: C2 F7 06        JP      NZ,$06F7            ; {}
0694: 21 46 86        LD      HL,$8646            
0697: CB 4E           BIT     1,(HL)              
0699: 28 02           JR      Z,$1238             ; {}
069B: 36 80           LD      (HL),$80            
069D: 21 32 85        LD      HL,$8532            
06A0: 06 08           LD      B,$08               
06A2: 11 10 00        LD      DE,$0010            
06A5: 36 00           LD      (HL),$00            
06A7: 19              ADD     HL,DE               
06A8: 32 30 68        LD      ($6830),A           
06AB: 10 F8           DJNZ    $122E               ; {}
06AD: 21 9E 98        LD      HL,$989E            
06B0: 36 00           LD      (HL),$00            
06B2: 23              INC     HL                  
06B3: 36 E0           LD      (HL),$E0            
06B5: 21 26 85        LD      HL,$8526            
06B8: 06 08           LD      B,$08               
06BA: 11 0E 00        LD      DE,$000E            
06BD: CB B6           RES     6,(HL)              
06BF: 23              INC     HL                  
06C0: 23              INC     HL                  
06C1: CB B6           RES     6,(HL)              
06C3: 19              ADD     HL,DE               
06C4: 32 30 68        LD      ($6830),A           
06C7: 10 F4           DJNZ    $122A               ; {}
06C9: 21 2B 85        LD      HL,$852B            
06CC: 11 10 00        LD      DE,$0010            
06CF: 06 08           LD      B,$08               
06D1: 36 32           LD      (HL),$32            
06D3: 19              ADD     HL,DE               
06D4: 32 30 68        LD      ($6830),A           
06D7: 10 F8           DJNZ    $122E               ; {}
06D9: 21 4A 86        LD      HL,$864A            
06DC: 36 00           LD      (HL),$00            
06DE: CD 4F 15        CALL    $154F               ; {}
06E1: CD 87 0F        CALL    $0F87               ; {}
06E4: AF              XOR     A                   
06E5: 32 A0 98        LD      ($98A0),A           
06E8: 32 A1 98        LD      ($98A1),A           
06EB: 21 F4 98        LD      HL,$98F4            
06EE: 06 0C           LD      B,$0C               
06F0: 77              LD      (HL),A              
06F1: 23              INC     HL                  
06F2: 10 FC           DJNZ    $1232               ; {}
06F4: C3 27 0A        JP      $0A27               ; {}
06F7: FE 50           CP      $50                 
06F9: C2 1B 07        JP      NZ,$071B            ; {}
06FC: 3E 01           LD      A,$01               
06FE: 32 85 9A        LD      ($9A85),A           
0701: 21 22 98        LD      HL,$9822            
0704: 36 14           LD      (HL),$14            
0706: 21 46 86        LD      HL,$8646            
0709: CB 7E           BIT     7,(HL)              
070B: 28 09           JR      Z,$123F             ; {}
070D: CB BE           RES     7,(HL)              
070F: 21 1C 86        LD      HL,$861C            
0712: 36 22           LD      (HL),$22            
0714: 18 66           JR      $129C               ; {}
0716: CD D8 11        CALL    $11D8               ; {}
0719: 18 61           JR      $1297               ; {}
071B: FE 34           CP      $34                 
071D: 20 1A           JR      NZ,$1250            ; {}
071F: 21 22 98        LD      HL,$9822            
0722: 36 15           LD      (HL),$15            
0724: 21 DA 87        LD      HL,$87DA            
0727: 3A 00 84        LD      A,($8400)           
072A: CB 4F           BIT     1,A                 
072C: 28 03           JR      Z,$1239             ; {}
072E: 21 D8 87        LD      HL,$87D8            
0731: 7E              LD      A,(HL)              
0732: FE 02           CP      $02                 
0734: 20 46           JR      NZ,$127C            ; {}
0736: 34              INC     (HL)                
0737: 18 43           JR      $1279               ; {}
0739: FE 20           CP      $20                 
073B: 20 07           JR      NZ,$123D            ; {}
073D: 21 22 98        LD      HL,$9822            
0740: 36 16           LD      (HL),$16            
0742: 18 38           JR      $126E               ; {}
0744: FE 14           CP      $14                 
0746: 20 07           JR      NZ,$123D            ; {}
0748: 21 22 98        LD      HL,$9822            
074B: 36 17           LD      (HL),$17            
074D: 18 2D           JR      $1263               ; {}
074F: A7              AND     A                   
0750: C2 27 0A        JP      NZ,$0A27            ; {}
0753: 3A 57 86        LD      A,($8657)           
0756: CB 4F           BIT     1,A                 
0758: C2 C7 0B        JP      NZ,$0BC7            ; {}
075B: AF              XOR     A                   
075C: 32 80 98        LD      ($9880),A           
075F: 32 81 98        LD      ($9881),A           
0762: 21 22 98        LD      HL,$9822            
0765: 36 32           LD      (HL),$32            
0767: 21 A2 98        LD      HL,$98A2            
076A: 36 00           LD      (HL),$00            
076C: 23              INC     HL                  
076D: 36 50           LD      (HL),$50            
076F: 21 02 84        LD      HL,$8402            
0772: CB C6           SET     0,(HL)              
0774: 21 1C 86        LD      HL,$861C            
0777: 36 3C           LD      (HL),$3C            
0779: C3 27 0A        JP      $0A27               ; {}
077C: 3A AE 85        LD      A,($85AE)           
077F: CB 4F           BIT     1,A                 
0781: CA 27 0A        JP      Z,$0A27             ; {}
0784: 21 22 98        LD      HL,$9822            
0787: 7E              LD      A,(HL)              
0788: C6 04           ADD     $04                 
078A: 77              LD      (HL),A              
078B: 21 F4 98        LD      HL,$98F4            
078E: 06 0C           LD      B,$0C               
0790: 36 00           LD      (HL),$00            
0792: 23              INC     HL                  
0793: 10 FB           DJNZ    $1231               ; {}
0795: C3 27 0A        JP      $0A27               ; {}
0798: 21 1C 86        LD      HL,$861C            
079B: 7E              LD      A,(HL)              
079C: A7              AND     A                   
079D: 28 04           JR      Z,$123A             ; {}
079F: 35              DEC     (HL)                
07A0: C3 27 0A        JP      $0A27               ; {}
07A3: 21 00 84        LD      HL,$8400            
07A6: CB 4E           BIT     1,(HL)              
07A8: 20 0C           JR      NZ,$1242            ; {}
07AA: 3A 0A 84        LD      A,($840A)           
07AD: A7              AND     A                   
07AE: 20 13           JR      NZ,$1249            ; {}
07B0: 23              INC     HL                  
07B1: 23              INC     HL                  
07B2: CB CE           SET     1,(HL)              
07B4: 18 69           JR      $129F               ; {}
07B6: 3A 0B 84        LD      A,($840B)           
07B9: A7              AND     A                   
07BA: 20 51           JR      NZ,$1287            ; {}
07BC: 23              INC     HL                  
07BD: 23              INC     HL                  
07BE: CB D6           SET     2,(HL)              
07C0: C3 66 08        JP      $0866               ; {}
07C3: CB 46           BIT     0,(HL)              
07C5: 20 21           JR      NZ,$1257            ; {}
07C7: 21 00 84        LD      HL,$8400            
07CA: CB AE           RES     5,(HL)              
07CC: CB A6           RES     4,(HL)              
07CE: 23              INC     HL                  
07CF: 7E              LD      A,(HL)              
07D0: E6 57           AND     $57                 
07D2: 77              LD      (HL),A              
07D3: 23              INC     HL                  
07D4: 7E              LD      A,(HL)              
07D5: E6 E6           AND     $E6                 
07D7: 77              LD      (HL),A              
07D8: 23              INC     HL                  
07D9: CB 96           RES     2,(HL)              
07DB: CB 9E           RES     3,(HL)              
07DD: 23              INC     HL                  
07DE: CB B6           RES     6,(HL)              
07E0: 21 46 86        LD      HL,$8646            
07E3: 36 00           LD      (HL),$00            
07E5: C3 27 0A        JP      $0A27               ; {}
07E8: 23              INC     HL                  
07E9: 23              INC     HL                  
07EA: CB 56           BIT     2,(HL)              
07EC: 20 D9           JR      NZ,$120F            ; {}
07EE: 21 00 84        LD      HL,$8400            
07F1: 32 30 68        LD      ($6830),A           
07F4: CB 56           BIT     2,(HL)              
07F6: 28 05           JR      Z,$123B             ; {}
07F8: 21 07 A0        LD      HL,$A007            
07FB: 36 01           LD      (HL),$01            
07FD: 21 00 84        LD      HL,$8400            
0800: CB CE           SET     1,(HL)              
0802: CD 95 12        CALL    $1295               ; {}
0805: CD A2 12        CALL    $12A2               ; {}
0808: CD AF 12        CALL    $12AF               ; {}
080B: 18 BA           JR      $11F0               ; {}
080D: 21 02 84        LD      HL,$8402            
0810: CB 4E           BIT     1,(HL)              
0812: 20 B3           JR      NZ,$11E9            ; {}
0814: 2B              DEC     HL                  
0815: 2B              DEC     HL                  
0816: CB 8E           RES     1,(HL)              
0818: 21 07 A0        LD      HL,$A007            
081B: 36 00           LD      (HL),$00            
081D: 18 E3           JR      $1219               ; {}
081F: 21 00 84        LD      HL,$8400            
0822: CB 46           BIT     0,(HL)              
0824: CA B0 08        JP      Z,$08B0             ; {}
0827: 23              INC     HL                  
0828: 23              INC     HL                  
0829: CB 56           BIT     2,(HL)              
082B: C2 B0 08        JP      NZ,$08B0            ; {}
082E: 21 02 84        LD      HL,$8402            
0831: CB 5E           BIT     3,(HL)              
0833: 20 17           JR      NZ,$124D            ; {}
0835: 21 1D 86        LD      HL,$861D            
0838: 36 78           LD      (HL),$78            
083A: CD C7 12        CALL    $12C7               ; {}
083D: 21 02 84        LD      HL,$8402            
0840: CB DE           SET     3,(HL)              
0842: 21 CC 87        LD      HL,$87CC            
0845: CB CE           SET     1,(HL)              
0847: CB D6           SET     2,(HL)              
0849: C3 27 0A        JP      $0A27               ; {}
084C: 21 1D 86        LD      HL,$861D            
084F: 7E              LD      A,(HL)              
0850: A7              AND     A                   
0851: 28 04           JR      Z,$123A             ; {}
0853: 35              DEC     (HL)                
0854: C3 27 0A        JP      $0A27               ; {}
0857: 21 CC 87        LD      HL,$87CC            
085A: CB 96           RES     2,(HL)              
085C: CB 4E           BIT     1,(HL)              
085E: C2 27 0A        JP      NZ,$0A27            ; {}
0861: CD 49 13        CALL    $1349               ; {}
0864: 18 88           JR      $11BE               ; {}
0866: 21 02 84        LD      HL,$8402            
0869: CB 4E           BIT     1,(HL)              
086B: 20 43           JR      NZ,$1279            ; {}
086D: 21 02 84        LD      HL,$8402            
0870: CB 5E           BIT     3,(HL)              
0872: 20 17           JR      NZ,$124D            ; {}
0874: 21 1D 86        LD      HL,$861D            
0877: 36 78           LD      (HL),$78            
0879: CD D1 12        CALL    $12D1               ; {}
087C: 21 02 84        LD      HL,$8402            
087F: CB DE           SET     3,(HL)              
0881: 21 CC 87        LD      HL,$87CC            
0884: CB CE           SET     1,(HL)              
0886: CB D6           SET     2,(HL)              
0888: C3 27 0A        JP      $0A27               ; {}
088B: 21 1D 86        LD      HL,$861D            
088E: 7E              LD      A,(HL)              
088F: A7              AND     A                   
0890: 28 04           JR      Z,$123A             ; {}
0892: 35              DEC     (HL)                
0893: C3 27 0A        JP      $0A27               ; {}
0896: 21 CC 87        LD      HL,$87CC            
0899: CB 96           RES     2,(HL)              
089B: CB 4E           BIT     1,(HL)              
089D: C2 27 0A        JP      NZ,$0A27            ; {}
08A0: 21 00 84        LD      HL,$8400            
08A3: CB 8E           RES     1,(HL)              
08A5: CD 49 13        CALL    $1349               ; {}
08A8: 21 07 A0        LD      HL,$A007            
08AB: 36 00           LD      (HL),$00            
08AD: C3 02 08        JP      $0802               ; {}
08B0: 21 02 84        LD      HL,$8402            
08B3: CB 66           BIT     4,(HL)              
08B5: 20 1D           JR      NZ,$1253            ; {}
08B7: CB E6           SET     4,(HL)              
08B9: 21 83 9A        LD      HL,$9A83            
08BC: CB C6           SET     0,(HL)              
08BE: 21 1E 86        LD      HL,$861E            
08C1: 36 41           LD      (HL),$41            
08C3: 21 CC 87        LD      HL,$87CC            
08C6: CB CE           SET     1,(HL)              
08C8: CB D6           SET     2,(HL)              
08CA: AF              XOR     A                   
08CB: 32 58 86        LD      ($8658),A           
08CE: 32 57 86        LD      ($8657),A           
08D1: C3 27 0A        JP      $0A27               ; {}
08D4: 21 1E 86        LD      HL,$861E            
08D7: 7E              LD      A,(HL)              
08D8: A7              AND     A                   
08D9: 28 1D           JR      Z,$1253             ; {}
08DB: FE 38           CP      $38                 
08DD: 20 0A           JR      NZ,$1240            ; {}
08DF: E5              PUSH    HL                  
08E0: 21 83 9A        LD      HL,$9A83            
08E3: 7E              LD      A,(HL)              
08E4: E1              POP     HL                  
08E5: A7              AND     A                   
08E6: C2 27 0A        JP      NZ,$0A27            ; {}
08E9: E5              PUSH    HL                  
08EA: CD CD 12        CALL    $12CD               ; {}
08ED: E1              POP     HL                  
08EE: 35              DEC     (HL)                
08EF: CD 8B 18        CALL    $188B               ; {}
08F2: CD A5 18        CALL    $18A5               ; {}
08F5: C3 27 0A        JP      $0A27               ; {}
08F8: 21 CC 87        LD      HL,$87CC            
08FB: CB 96           RES     2,(HL)              
08FD: CB 4E           BIT     1,(HL)              
08FF: C2 27 0A        JP      NZ,$0A27            ; {}
0902: CD 49 13        CALL    $1349               ; {}
0905: 21 00 84        LD      HL,$8400            
0908: 7E              LD      A,(HL)              
0909: E6 01           AND     $01                 
090B: 77              LD      (HL),A              
090C: 23              INC     HL                  
090D: 06 06           LD      B,$06               
090F: 36 00           LD      (HL),$00            
0911: 23              INC     HL                  
0912: 10 FB           DJNZ    $1231               ; {}
0914: 3E 90           LD      A,$90               
0916: 32 76 86        LD      ($8676),A           
0919: 21 46 86        LD      HL,$8646            
091C: 36 00           LD      (HL),$00            
091E: 3A 0D 84        LD      A,($840D)           
0921: 32 A9 87        LD      ($87A9),A           
0924: 21 04 89        LD      HL,$8904            
0927: 06 04           LD      B,$04               
0929: 36 02           LD      (HL),$02            
092B: 23              INC     HL                  
092C: 10 FB           DJNZ    $1231               ; {}
092E: 21 04 89        LD      HL,$8904            
0931: 11 00 70        LD      DE,$7000            
0934: 01 04 00        LD      BC,$0004            
0937: 3E C1           LD      A,$C1               
0939: CD A1 00        CALL    $00A1               ; {}
093C: 21 87 87        LD      HL,$8787            
093F: 36 00           LD      (HL),$00            
0941: 21 07 A0        LD      HL,$A007            
0944: 36 00           LD      (HL),$00            
0946: C3 27 0A        JP      $0A27               ; {}
0949: 3A F5 98        LD      A,($98F5)           
094C: A7              AND     A                   
094D: C2 E6 09        JP      NZ,$09E6            ; {}
0950: 3A F7 98        LD      A,($98F7)           
0953: A7              AND     A                   
0954: C2 E6 09        JP      NZ,$09E6            ; {}
0957: 3A 22 98        LD      A,($9822)           
095A: FE 08           CP      $08                 
095C: CA E6 09        JP      Z,$09E6             ; {}
095F: FE 09           CP      $09                 
0961: CA E6 09        JP      Z,$09E6             ; {}
0964: FE 0C           CP      $0C                 
0966: CA E6 09        JP      Z,$09E6             ; {}
0969: FE 0D           CP      $0D                 
096B: CA E6 09        JP      Z,$09E6             ; {}
096E: 3A 87 9A        LD      A,($9A87)           
0971: A7              AND     A                   
0972: C2 E6 09        JP      NZ,$09E6            ; {}
0975: 3A 57 86        LD      A,($8657)           
0978: CB 4F           BIT     1,A                 
097A: 20 14           JR      NZ,$124A            ; {}
097C: 21 2B 85        LD      HL,$852B            
097F: 06 08           LD      B,$08               
0981: 11 10 00        LD      DE,$0010            
0984: 7E              LD      A,(HL)              
0985: FE 82           CP      $82                 
0987: 28 5D           JR      Z,$1293             ; {}
0989: FE 85           CP      $85                 
098B: 28 59           JR      Z,$128F             ; {}
098D: 19              ADD     HL,DE               
098E: 10 F4           DJNZ    $122A               ; {}
0990: 21 28 85        LD      HL,$8528            
0993: 06 08           LD      B,$08               
0995: 11 10 00        LD      DE,$0010            
0998: CB 7E           BIT     7,(HL)              
099A: 28 4A           JR      Z,$1280             ; {}
099C: CB B6           RES     6,(HL)              
099E: 19              ADD     HL,DE               
099F: 32 30 68        LD      ($6830),A           
09A2: 10 F4           DJNZ    $122A               ; {}
09A4: 3A 46 86        LD      A,($8646)           
09A7: CB 47           BIT     0,A                 
09A9: 20 3B           JR      NZ,$1271            ; {}
09AB: CD 8A 12        CALL    $128A               ; {}
09AE: AF              XOR     A                   
09AF: 32 A0 98        LD      ($98A0),A           
09B2: 32 A1 98        LD      ($98A1),A           
09B5: CD 87 0F        CALL    $0F87               ; {}
09B8: 21 46 86        LD      HL,$8646            
09BB: 36 00           LD      (HL),$00            
09BD: 21 88 9A        LD      HL,$9A88            
09C0: CB C6           SET     0,(HL)              
09C2: 21 00 84        LD      HL,$8400            
09C5: 7E              LD      A,(HL)              
09C6: E6 4F           AND     $4F                 
09C8: 77              LD      (HL),A              
09C9: 23              INC     HL                  
09CA: CB AE           RES     5,(HL)              
09CC: CB 9E           RES     3,(HL)              
09CE: 2B              DEC     HL                  
09CF: CB 4E           BIT     1,(HL)              
09D1: 20 0C           JR      NZ,$1242            ; {}
09D3: 21 0A 84        LD      HL,$840A            
09D6: 34              INC     (HL)                
09D7: 21 4A 86        LD      HL,$864A            
09DA: 36 00           LD      (HL),$00            
09DC: C3 27 0A        JP      $0A27               ; {}
09DF: 21 0B 84        LD      HL,$840B            
09E2: 34              INC     (HL)                
09E3: C3 27 0A        JP      $0A27               ; {}
09E6: CD A6 0B        CALL    $0BA6               ; {}
09E9: CD B1 0B        CALL    $0BB1               ; {}
09EC: 2A D6 87        LD      HL,($87D6)          
09EF: 23              INC     HL                  
09F0: 22 D6 87        LD      ($87D6),HL          
09F3: CD 30 14        CALL    $1430               ; {}
09F6: 3A 57 86        LD      A,($8657)           
09F9: CB 4F           BIT     1,A                 
09FB: 20 06           JR      NZ,$123C            ; {}
09FD: 3A 0D 84        LD      A,($840D)           
0A00: 32 05 9A        LD      ($9A05),A           
0A03: CD FE 1E        CALL    $1EFE               ; {}
0A06: CD 23 14        CALL    $1423               ; {}
0A09: 3A 46 86        LD      A,($8646)           
0A0C: CB 47           BIT     0,A                 
0A0E: 28 05           JR      Z,$123B             ; {}
0A10: CD 87 0F        CALL    $0F87               ; {}
0A13: 18 08           JR      $123E               ; {}
0A15: CD A2 0D        CALL    $0DA2               ; {}
0A18: 3E FF           LD      A,$FF               
0A1A: 32 23 68        LD      ($6823),A           
0A1D: 3A 46 86        LD      A,($8646)           
0A20: CB 47           BIT     0,A                 
0A22: 20 03           JR      NZ,$1239            ; {}
0A24: CD 4C 13        CALL    $134C               ; {}
0A27: 21 00 70        LD      HL,$7000            
0A2A: 11 CE 87        LD      DE,$87CE            
0A2D: 01 02 00        LD      BC,$0002            
0A30: 3E D2           LD      A,$D2               
0A32: CD A1 00        CALL    $00A1               ; {}
0A35: 32 30 68        LD      ($6830),A           
0A38: 3A 9A 87        LD      A,($879A)           
0A3B: A7              AND     A                   
0A3C: C2 71 0A        JP      NZ,$0A71            ; {}
0A3F: 3A 57 86        LD      A,($8657)           
0A42: CB 47           BIT     0,A                 
0A44: 28 09           JR      Z,$123F             ; {}
0A46: 3A 58 86        LD      A,($8658)           
0A49: E6 0F           AND     $0F                 
0A4B: FE 07           CP      $07                 
0A4D: 20 22           JR      NZ,$1258            ; {}
0A4F: CD 0B 1D        CALL    $1D0B               ; {}
0A52: 21 25 98        LD      HL,$9825            
0A55: 06 0C           LD      B,$0C               
0A57: 36 05           LD      (HL),$05            
0A59: 23              INC     HL                  
0A5A: 23              INC     HL                  
0A5B: 32 30 68        LD      ($6830),A           
0A5E: 10 F7           DJNZ    $122D               ; {}
0A60: 3A CC 87        LD      A,($87CC)           
0A63: CB 4F           BIT     1,A                 
0A65: C2 71 0A        JP      NZ,$0A71            ; {}
0A68: CD 90 1B        CALL    $1B90               ; {}
0A6B: CD AD 1B        CALL    $1BAD               ; {}
0A6E: CD E3 16        CALL    $16E3               ; {}
0A71: CB C7           SET     0,A                 
0A73: 32 20 68        LD      ($6820),A           
0A76: F1              POP     AF                  
0A77: C1              POP     BC                  
0A78: D1              POP     DE                  
0A79: E1              POP     HL                  
0A7A: FD E1           POP     IY                  
0A7C: DD E1           POP     IX                  
0A7E: FB              EI                          
0A7F: C9              RET                         
0A80: 21 87 87        LD      HL,$8787            
0A83: 3A 57 86        LD      A,($8657)           
0A86: CB 47           BIT     0,A                 
0A88: 20 0C           JR      NZ,$1242            ; {}
0A8A: 3A CF 87        LD      A,($87CF)           
0A8D: CB 5F           BIT     3,A                 
0A8F: 20 05           JR      NZ,$123B            ; {}
0A91: CB 4E           BIT     1,(HL)              
0A93: CA EA 1D        JP      Z,$1DEA             ; {}
0A96: 36 FF           LD      (HL),$FF            
0A98: 21 57 86        LD      HL,$8657            
0A9B: CB C6           SET     0,(HL)              
0A9D: CB 4E           BIT     1,(HL)              
0A9F: CA 27 0A        JP      Z,$0A27             ; {}
0AA2: CD CA 0B        CALL    $0BCA               ; {}
0AA5: 3A 58 86        LD      A,($8658)           
0AA8: FE 17           CP      $17                 
0AAA: C2 27 0A        JP      NZ,$0A27            ; {}
0AAD: 3A 76 86        LD      A,($8676)           
0AB0: FE 10           CP      $10                 
0AB2: C2 FB 0A        JP      NZ,$0AFB            ; {}
0AB5: AF              XOR     A                   
0AB6: 32 99 87        LD      ($8799),A           
0AB9: 32 6C 89        LD      ($896C),A           
0ABC: 32 F0 87        LD      ($87F0),A           
0ABF: CD 22 0C        CALL    $0C22               ; {}
0AC2: CD 15 0C        CALL    $0C15               ; {}
0AC5: 21 00 00        LD      HL,$0000            
0AC8: 22 D6 87        LD      ($87D6),HL          
0ACB: 21 9E 98        LD      HL,$989E            
0ACE: 36 00           LD      (HL),$00            
0AD0: 23              INC     HL                  
0AD1: 36 E0           LD      (HL),$E0            
0AD3: CD 05 0C        CALL    $0C05               ; {}
0AD6: 21 23 84        LD      HL,$8423            
0AD9: 36 FE           LD      (HL),$FE            
0ADB: CD 69 14        CALL    $1469               ; {}
0ADE: 21 23 84        LD      HL,$8423            
0AE1: 36 01           LD      (HL),$01            
0AE3: CD 69 14        CALL    $1469               ; {}
0AE6: 21 C0 83        LD      HL,$83C0            
0AE9: 06 3F           LD      B,$3F               
0AEB: 7E              LD      A,(HL)              
0AEC: FE 0C           CP      $0C                 
0AEE: 20 02           JR      NZ,$1238            ; {}
0AF0: 36 8C           LD      (HL),$8C            
0AF2: 32 30 68        LD      ($6830),A           
0AF5: 23              INC     HL                  
0AF6: 10 F3           DJNZ    $1229               ; {}
0AF8: C3 E0 04        JP      $04E0               ; {}
0AFB: FE 80           CP      $80                 
0AFD: CA 54 06        JP      Z,$0654             ; {}
0B00: C3 27 0A        JP      $0A27               ; {}
0B03: 21 87 87        LD      HL,$8787            
0B06: 3A CF 87        LD      A,($87CF)           
0B09: CB 5F           BIT     3,A                 
0B0B: 20 05           JR      NZ,$123B            ; {}
0B0D: CB 4E           BIT     1,(HL)              
0B0F: CA EA 1D        JP      Z,$1DEA             ; {}
0B12: 36 FF           LD      (HL),$FF            
0B14: CD 99 19        CALL    $1999               ; {}
0B17: 21 F0 87        LD      HL,$87F0            
0B1A: CB 9E           RES     3,(HL)              
0B1C: 21 93 9A        LD      HL,$9A93            
0B1F: 36 00           LD      (HL),$00            
0B21: 21 57 86        LD      HL,$8657            
0B24: CB 86           RES     0,(HL)              
0B26: CB 4E           BIT     1,(HL)              
0B28: C2 71 0A        JP      NZ,$0A71            ; {}
0B2B: CD CA 0B        CALL    $0BCA               ; {}
0B2E: 3A 01 84        LD      A,($8401)           
0B31: CB 4F           BIT     1,A                 
0B33: CA 5F 0B        JP      Z,$0B5F             ; {}
0B36: CD 8B 18        CALL    $188B               ; {}
0B39: CD A5 18        CALL    $18A5               ; {}
0B3C: CD F2 0B        CALL    $0BF2               ; {}
0B3F: 21 00 84        LD      HL,$8400            
0B42: 7E              LD      A,(HL)              
0B43: E6 07           AND     $07                 
0B45: 77              LD      (HL),A              
0B46: 23              INC     HL                  
0B47: 7E              LD      A,(HL)              
0B48: E6 02           AND     $02                 
0B4A: 77              LD      (HL),A              
0B4B: 06 03           LD      B,$03               
0B4D: 23              INC     HL                  
0B4E: 36 00           LD      (HL),$00            
0B50: 23              INC     HL                  
0B51: 10 FB           DJNZ    $1231               ; {}
0B53: CD 04 16        CALL    $1604               ; {}
0B56: CD D9 15        CALL    $15D9               ; {}
0B59: CD 8E 16        CALL    $168E               ; {}
0B5C: C3 71 0A        JP      $0A71               ; {}
0B5F: CB CF           SET     1,A                 
0B61: 32 01 84        LD      ($8401),A           
0B64: 21 80 98        LD      HL,$9880            
0B67: DD 21 00 99     LD      IX,$9900            
0B6B: 11 00 98        LD      DE,$9800            
0B6E: 06 80           LD      B,$80               
0B70: 36 00           LD      (HL),$00            
0B72: DD 36 00 00     LD      (IX+$00),$00        
0B76: 32 30 68        LD      ($6830),A           
0B79: 3E 32           LD      A,$32               
0B7B: 12              LD      (DE),A              
0B7C: DD 23           INC     IX                  
0B7E: 13              INC     DE                  
0B7F: 23              INC     HL                  
0B80: 10 EE           DJNZ    $1224               ; {}
0B82: 3E FE           LD      A,$FE               
0B84: 32 23 84        LD      ($8423),A           
0B87: CD 69 14        CALL    $1469               ; {}
0B8A: 3E 01           LD      A,$01               
0B8C: 32 23 84        LD      ($8423),A           
0B8F: CD 69 14        CALL    $1469               ; {}
0B92: CD DF 0B        CALL    $0BDF               ; {}
0B95: CD 95 15        CALL    $1595               ; {}
0B98: CD 23 16        CALL    $1623               ; {}
0B9B: CD 3E 16        CALL    $163E               ; {}
0B9E: 21 03 A0        LD      HL,$A003            
0BA1: CB C6           SET     0,(HL)              
0BA3: C3 71 0A        JP      $0A71               ; {}
0BA6: 21 00 A0        LD      HL,$A000            
0BA9: 06 04           LD      B,$04               
0BAB: 36 00           LD      (HL),$00            
0BAD: 23              INC     HL                  
0BAE: 10 FB           DJNZ    $1231               ; {}
0BB0: C9              RET                         
0BB1: 11 07 A0        LD      DE,$A007            
0BB4: 21 00 84        LD      HL,$8400            
0BB7: CB 4E           BIT     1,(HL)              
0BB9: 28 08           JR      Z,$123E             ; {}
0BBB: CB 56           BIT     2,(HL)              
0BBD: 28 04           JR      Z,$123A             ; {}
0BBF: EB              EX      DE,HL               
0BC0: 36 01           LD      (HL),$01            
0BC2: C9              RET                         
0BC3: EB              EX      DE,HL               
0BC4: 36 00           LD      (HL),$00            
0BC6: C9              RET                         
0BC7: C3 F8 08        JP      $08F8               ; {}
0BCA: CD 30 14        CALL    $1430               ; {}
0BCD: CD 4D 14        CALL    $144D               ; {}
0BD0: 21 17 84        LD      HL,$8417            
0BD3: 01 00 03        LD      BC,$0300            
0BD6: 3A 00 84        LD      A,($8400)           
0BD9: E6 01           AND     $01                 
0BDB: C2 59 14        JP      NZ,$1459            ; {}
0BDE: C9              RET                         
0BDF: 21 C0 83        LD      HL,$83C0            
0BE2: 06 3F           LD      B,$3F               
0BE4: 7E              LD      A,(HL)              
0BE5: FE 8C           CP      $8C                 
0BE7: 20 02           JR      NZ,$1238            ; {}
0BE9: 36 0C           LD      (HL),$0C            
0BEB: 32 30 68        LD      ($6830),A           
0BEE: 23              INC     HL                  
0BEF: 10 F3           DJNZ    $1229               ; {}
0BF1: C9              RET                         
0BF2: 21 00 98        LD      HL,$9800            
0BF5: 11 80 98        LD      DE,$9880            
0BF8: 06 80           LD      B,$80               
0BFA: 32 30 68        LD      ($6830),A           
0BFD: AF              XOR     A                   
0BFE: 77              LD      (HL),A              
0BFF: 12              LD      (DE),A              
0C00: 23              INC     HL                  
0C01: 13              INC     DE                  
0C02: 10 F6           DJNZ    $122C               ; {}
0C04: C9              RET                         
0C05: CD 37 1A        CALL    $1A37               ; {}
0C08: CD 92 1A        CALL    $1A92               ; {}
0C0B: CD 71 1A        CALL    $1A71               ; {}
0C0E: CD C4 1A        CALL    $1AC4               ; {}
0C11: CD 30 14        CALL    $1430               ; {}
0C14: C9              RET                         
0C15: CD 8B 18        CALL    $188B               ; {}
0C18: CD A5 18        CALL    $18A5               ; {}
0C1B: CD A1 19        CALL    $19A1               ; {}
0C1E: CD AA 18        CALL    $18AA               ; {}
0C21: C9              RET                         
0C22: CD AC 17        CALL    $17AC               ; {}
0C25: CD 3C 18        CALL    $183C               ; {}
0C28: CD 43 18        CALL    $1843               ; {}
0C2B: CD F6 17        CALL    $17F6               ; {}
0C2E: CD 4F 15        CALL    $154F               ; {}
0C31: AF              XOR     A                   
0C32: 32 A7 87        LD      ($87A7),A           
0C35: 32 BF 87        LD      ($87BF),A           
0C38: 32 9F 87        LD      ($879F),A           
0C3B: 32 EB 87        LD      ($87EB),A           
0C3E: 32 DA 87        LD      ($87DA),A           
0C41: 32 D8 87        LD      ($87D8),A           
0C44: 21 00 00        LD      HL,$0000            
0C47: 22 ED 87        LD      ($87ED),HL          
0C4A: 22 D4 87        LD      ($87D4),HL          
0C4D: 22 D2 87        LD      ($87D2),HL          
0C50: C9              RET                         
0C51: DD 21 2A 86     LD      IX,$862A            
0C55: 21 AA 85        LD      HL,$85AA            
0C58: CD 6F 0C        CALL    $0C6F               ; {}
0C5B: DD 21 2D 86     LD      IX,$862D            
0C5F: 21 AC 85        LD      HL,$85AC            
0C62: E5              PUSH    HL                  
0C63: CD 6F 0C        CALL    $0C6F               ; {}
0C66: E1              POP     HL                  
0C67: DD 21 30 86     LD      IX,$8630            
0C6B: CD 6F 0C        CALL    $0C6F               ; {}
0C6E: C9              RET                         
0C6F: DD 36 00 00     LD      (IX+$00),$00        
0C73: 7E              LD      A,(HL)              
0C74: 87              ADD     A,A                 
0C75: 87              ADD     A,A                 
0C76: 87              ADD     A,A                 
0C77: 87              ADD     A,A                 
0C78: DD 77 01        LD      (IX+$01),A          
0C7B: 23              INC     HL                  
0C7C: 7E              LD      A,(HL)              
0C7D: DD 77 02        LD      (IX+$02),A          
0C80: C9              RET                         
0C81: 3A 00 84        LD      A,($8400)           
0C84: CB 4F           BIT     1,A                 
0C86: 20 05           JR      NZ,$123B            ; {}
0C88: 21 16 84        LD      HL,$8416            
0C8B: 18 03           JR      $1239               ; {}
0C8D: 21 19 84        LD      HL,$8419            
0C90: 7E              LD      A,(HL)              
0C91: FE 90           CP      $90                 
0C93: D0              RET     NC                  
0C94: 3A 57 86        LD      A,($8657)           
0C97: CB 47           BIT     0,A                 
0C99: C0              RET     NZ                  
0C9A: 3A C0 87        LD      A,($87C0)           
0C9D: A7              AND     A                   
0C9E: C8              RET     Z                   
0C9F: 21 00 84        LD      HL,$8400            
0CA2: CB 4E           BIT     1,(HL)              
0CA4: 20 1A           JR      NZ,$1250            ; {}
0CA6: 21 14 84        LD      HL,$8414            
0CA9: 11 11 84        LD      DE,$8411            
0CAC: CD 54 0D        CALL    $0D54               ; {}
0CAF: 21 2D 86        LD      HL,$862D            
0CB2: 11 33 86        LD      DE,$8633            
0CB5: CD 54 0D        CALL    $0D54               ; {}
0CB8: 21 02 84        LD      HL,$8402            
0CBB: 22 F6 85        LD      ($85F6),HL          
0CBE: 18 18           JR      $124E               ; {}
0CC0: 21 17 84        LD      HL,$8417            
0CC3: 11 11 84        LD      DE,$8411            
0CC6: CD 54 0D        CALL    $0D54               ; {}
0CC9: 21 30 86        LD      HL,$8630            
0CCC: 11 33 86        LD      DE,$8633            
0CCF: CD 54 0D        CALL    $0D54               ; {}
0CD2: 21 03 84        LD      HL,$8403            
0CD5: 22 F6 85        LD      ($85F6),HL          
0CD8: CB 7E           BIT     7,(HL)              
0CDA: 20 20           JR      NZ,$1256            ; {}
0CDC: 21 11 84        LD      HL,$8411            
0CDF: 11 2A 86        LD      DE,$862A            
0CE2: CD 60 0D        CALL    $0D60               ; {}
0CE5: D8              RET     C                   
0CE6: 2A F6 85        LD      HL,($85F6)          
0CE9: CB FE           SET     7,(HL)              
0CEB: 21 87 9A        LD      HL,$9A87            
0CEE: CB C6           SET     0,(HL)              
0CF0: CD 6C 0D        CALL    $0D6C               ; {}
0CF3: 3E 01           LD      A,$01               
0CF5: 21 EA 89        LD      HL,$89EA            
0CF8: CD 24 12        CALL    $1224               ; {}
0CFB: C9              RET                         
0CFC: 21 11 84        LD      HL,$8411            
0CFF: 3A 00 84        LD      A,($8400)           
0D02: CB 4F           BIT     1,A                 
0D04: 20 08           JR      NZ,$123E            ; {}
0D06: 3A BF 87        LD      A,($87BF)           
0D09: CB 47           BIT     0,A                 
0D0B: C0              RET     NZ                  
0D0C: 18 06           JR      $123C               ; {}
0D0E: 3A BF 87        LD      A,($87BF)           
0D11: CB 4F           BIT     1,A                 
0D13: C0              RET     NZ                  
0D14: 3A C0 87        LD      A,($87C0)           
0D17: FE 01           CP      $01                 
0D19: C8              RET     Z                   
0D1A: 11 33 86        LD      DE,$8633            
0D1D: CD 60 0D        CALL    $0D60               ; {}
0D20: D8              RET     C                   
0D21: CD 6C 0D        CALL    $0D6C               ; {}
0D24: 21 87 9A        LD      HL,$9A87            
0D27: CB C6           SET     0,(HL)              
0D29: 3E 01           LD      A,$01               
0D2B: 21 EA 89        LD      HL,$89EA            
0D2E: CD 24 12        CALL    $1224               ; {}
0D31: DD 21 33 86     LD      IX,$8633            
0D35: 21 AC 85        LD      HL,$85AC            
0D38: CD 6F 0C        CALL    $0C6F               ; {}
0D3B: CD 84 0D        CALL    $0D84               ; {}
0D3E: 3A C0 87        LD      A,($87C0)           
0D41: FE 02           CP      $02                 
0D43: C0              RET     NZ                  
0D44: 21 BF 87        LD      HL,$87BF            
0D47: 3A 00 84        LD      A,($8400)           
0D4A: CB 4F           BIT     1,A                 
0D4C: 20 03           JR      NZ,$1239            ; {}
0D4E: CB C6           SET     0,(HL)              
0D50: C9              RET                         
0D51: CB CE           SET     1,(HL)              
0D53: C9              RET                         
0D54: 06 03           LD      B,$03               
0D56: 7E              LD      A,(HL)              
0D57: 12              LD      (DE),A              
0D58: 23              INC     HL                  
0D59: 13              INC     DE                  
0D5A: 32 30 68        LD      ($6830),A           
0D5D: 10 F7           DJNZ    $122D               ; {}
0D5F: C9              RET                         
0D60: 06 03           LD      B,$03               
0D62: EB              EX      DE,HL               
0D63: A7              AND     A                   
0D64: 1A              LD      A,(DE)              
0D65: 9E              SBC     (HL)                
0D66: 23              INC     HL                  
0D67: 13              INC     DE                  
0D68: 10 FA           DJNZ    $1230               ; {}
0D6A: EB              EX      DE,HL               
0D6B: C9              RET                         
0D6C: 21 00 84        LD      HL,$8400            
0D6F: CB 4E           BIT     1,(HL)              
0D71: 20 05           JR      NZ,$123B            ; {}
0D73: 21 0A 84        LD      HL,$840A            
0D76: 18 03           JR      $1239               ; {}
0D78: 21 0B 84        LD      HL,$840B            
0D7B: 34              INC     (HL)                
0D7C: 7E              LD      A,(HL)              
0D7D: 32 0C 84        LD      ($840C),A           
0D80: CD 43 18        CALL    $1843               ; {}
0D83: C9              RET                         
0D84: 21 00 84        LD      HL,$8400            
0D87: CB 4E           BIT     1,(HL)              
0D89: 20 05           JR      NZ,$123B            ; {}
0D8B: 21 2D 86        LD      HL,$862D            
0D8E: 18 03           JR      $1239               ; {}
0D90: 21 30 86        LD      HL,$8630            
0D93: 11 33 86        LD      DE,$8633            
0D96: 06 03           LD      B,$03               
0D98: A7              AND     A                   
0D99: 1A              LD      A,(DE)              
0D9A: 8E              ADC     A,(HL)              
0D9B: 27              DAA                         
0D9C: 77              LD      (HL),A              
0D9D: 13              INC     DE                  
0D9E: 23              INC     HL                  
0D9F: 10 F8           DJNZ    $122E               ; {}
0DA1: C9              RET                         
0DA2: 3A 01 84        LD      A,($8401)           
0DA5: CB 7F           BIT     7,A                 
0DA7: 20 51           JR      NZ,$1287            ; {}
0DA9: 3A 03 84        LD      A,($8403)           
0DAC: CB 57           BIT     2,A                 
0DAE: C2 34 0E        JP      NZ,$0E34            ; {}
0DB1: 21 01 84        LD      HL,$8401            
0DB4: CB 5E           BIT     3,(HL)              
0DB6: 20 36           JR      NZ,$126C            ; {}
0DB8: 3A 57 86        LD      A,($8657)           
0DBB: CB 4F           BIT     1,A                 
0DBD: 28 05           JR      Z,$123B             ; {}
0DBF: 3A 70 89        LD      A,($8970)           
0DC2: 18 03           JR      $1239               ; {}
0DC4: 3A B0 85        LD      A,($85B0)           
0DC7: CB 67           BIT     4,A                 
0DC9: C0              RET     NZ                  
0DCA: 21 01 84        LD      HL,$8401            
0DCD: CB DE           SET     3,(HL)              
0DCF: 3A 57 86        LD      A,($8657)           
0DD2: CB 4F           BIT     1,A                 
0DD4: 20 04           JR      NZ,$123A            ; {}
0DD6: 3E 32           LD      A,$32               
0DD8: 18 02           JR      $1238               ; {}
0DDA: 3E 36           LD      A,$36               
0DDC: 32 3E 86        LD      ($863E),A           
0DDF: CD 95 0F        CALL    $0F95               ; {}
0DE2: AF              XOR     A                   
0DE3: 32 9E 87        LD      ($879E),A           
0DE6: 21 8F 9A        LD      HL,$9A8F            
0DE9: 36 01           LD      (HL),$01            
0DEB: C9              RET                         
0DEC: 35              DEC     (HL)                
0DED: C9              RET                         
0DEE: 21 3E 86        LD      HL,$863E            
0DF1: 7E              LD      A,(HL)              
0DF2: FE 33           CP      $33                 
0DF4: 30 F6           JR      NC,$122C            ; {}
0DF6: FE 06           CP      $06                 
0DF8: 30 0E           JR      NC,$1244            ; {}
0DFA: CD 87 0F        CALL    $0F87               ; {}
0DFD: 21 01 84        LD      HL,$8401            
0E00: CB 9E           RES     3,(HL)              
0E02: 21 3E 86        LD      HL,$863E            
0E05: 36 00           LD      (HL),$00            
0E07: C9              RET                         
0E08: 22 42 86        LD      ($8642),HL          
0E0B: 3A 87 98        LD      A,($9887)           
0E0E: FE 08           CP      $08                 
0E10: 38 E8           JR      C,$121E             ; {}
0E12: 5F              LD      E,A                 
0E13: 3A 86 98        LD      A,($9886)           
0E16: 57              LD      D,A                 
0E17: CD 14 1C        CALL    $1C14               ; {}
0E1A: CD 39 10        CALL    $1039               ; {}
0E1D: 79              LD      A,C                 
0E1E: A7              AND     A                   
0E1F: 28 D9           JR      Z,$120F             ; {}
0E21: 21 04 84        LD      HL,$8404            
0E24: CB B6           RES     6,(HL)              
0E26: CD 07 12        CALL    $1207               ; {}
0E29: 3A 87 98        LD      A,($9887)           
0E2C: FE F2           CP      $F2                 
0E2E: 30 CA           JR      NC,$1200            ; {}
0E30: CD DE 10        CALL    $10DE               ; {}
0E33: C9              RET                         
0E34: 21 04 84        LD      HL,$8404            
0E37: CB 76           BIT     6,(HL)              
0E39: C0              RET     NZ                  
0E3A: CB 56           BIT     2,(HL)              
0E3C: 20 1E           JR      NZ,$1254            ; {}
0E3E: 2B              DEC     HL                  
0E3F: CB 9E           RES     3,(HL)              
0E41: 3A 57 86        LD      A,($8657)           
0E44: CB 4F           BIT     1,A                 
0E46: 28 05           JR      Z,$123B             ; {}
0E48: 3A 70 89        LD      A,($8970)           
0E4B: 18 03           JR      $1239               ; {}
0E4D: 3A B0 85        LD      A,($85B0)           
0E50: CB 6F           BIT     5,A                 
0E52: 20 03           JR      NZ,$1239            ; {}
0E54: 23              INC     HL                  
0E55: CB D6           SET     2,(HL)              
0E57: AF              XOR     A                   
0E58: 32 41 86        LD      ($8641),A           
0E5B: C9              RET                         
0E5C: 21 41 86        LD      HL,$8641            
0E5F: 34              INC     (HL)                
0E60: 7E              LD      A,(HL)              
0E61: E6 1F           AND     $1F                 
0E63: FE 09           CP      $09                 
0E65: 30 06           JR      NC,$123C            ; {}
0E67: 21 03 84        LD      HL,$8403            
0E6A: CB 9E           RES     3,(HL)              
0E6C: C9              RET                         
0E6D: 28 2B           JR      Z,$1261             ; {}
0E6F: FE 12           CP      $12                 
0E71: 28 21           JR      Z,$1257             ; {}
0E73: D8              RET     C                   
0E74: FE 1F           CP      $1F                 
0E76: 20 04           JR      NZ,$123A            ; {}
0E78: AF              XOR     A                   
0E79: 32 41 86        LD      ($8641),A           
0E7C: 3A 57 86        LD      A,($8657)           
0E7F: CB 4F           BIT     1,A                 
0E81: 28 05           JR      Z,$123B             ; {}
0E83: 3A 70 89        LD      A,($8970)           
0E86: 18 03           JR      $1239               ; {}
0E88: 3A B0 85        LD      A,($85B0)           
0E8B: CB 6F           BIT     5,A                 
0E8D: C8              RET     Z                   
0E8E: 21 04 84        LD      HL,$8404            
0E91: CB 96           RES     2,(HL)              
0E93: C9              RET                         
0E94: 21 03 84        LD      HL,$8403            
0E97: CB 9E           RES     3,(HL)              
0E99: C9              RET                         
0E9A: 21 03 84        LD      HL,$8403            
0E9D: CB DE           SET     3,(HL)              
0E9F: 21 D7 32        LD      HL,$32D7            
0EA2: 3A 10 84        LD      A,($8410)           
0EA5: 3D              DEC     A                   
0EA6: 5F              LD      E,A                 
0EA7: 16 00           LD      D,$00               
0EA9: 19              ADD     HL,DE               
0EAA: 7E              LD      A,(HL)              
0EAB: 2A C8 87        LD      HL,($87C8)          
0EAE: 11 0C 00        LD      DE,$000C            
0EB1: 19              ADD     HL,DE               
0EB2: 77              LD      (HL),A              
0EB3: 2A C8 87        LD      HL,($87C8)          
0EB6: 23              INC     HL                  
0EB7: 23              INC     HL                  
0EB8: CB 6E           BIT     5,(HL)              
0EBA: C2 CB 11        JP      NZ,$11CB            ; {}
0EBD: 3E 01           LD      A,$01               
0EBF: 32 90 9A        LD      ($9A90),A           
0EC2: 2B              DEC     HL                  
0EC3: 2B              DEC     HL                  
0EC4: 7E              LD      A,(HL)              
0EC5: E6 1C           AND     $1C                 
0EC7: 20 03           JR      NZ,$1239            ; {}
0EC9: CB D6           SET     2,(HL)              
0ECB: C9              RET                         
0ECC: CB 56           BIT     2,(HL)              
0ECE: 28 09           JR      Z,$123F             ; {}
0ED0: CB 96           RES     2,(HL)              
0ED2: CB DE           SET     3,(HL)              
0ED4: 23              INC     HL                  
0ED5: 23              INC     HL                  
0ED6: CB E6           SET     4,(HL)              
0ED8: C9              RET                         
0ED9: CB 5E           BIT     3,(HL)              
0EDB: 28 09           JR      Z,$123F             ; {}
0EDD: CB 9E           RES     3,(HL)              
0EDF: CB E6           SET     4,(HL)              
0EE1: 23              INC     HL                  
0EE2: 23              INC     HL                  
0EE3: CB E6           SET     4,(HL)              
0EE5: C9              RET                         
0EE6: CB 66           BIT     4,(HL)              
0EE8: C8              RET     Z                   
0EE9: CB A6           RES     4,(HL)              
0EEB: CB B6           RES     6,(HL)              
0EED: CB EE           SET     5,(HL)              
0EEF: 23              INC     HL                  
0EF0: 23              INC     HL                  
0EF1: 23              INC     HL                  
0EF2: CB FE           SET     7,(HL)              
0EF4: 3E 01           LD      A,$01               
0EF6: 32 8B 9A        LD      ($9A8B),A           
0EF9: 21 04 84        LD      HL,$8404            
0EFC: CB F6           SET     6,(HL)              
0EFE: 2A C8 87        LD      HL,($87C8)          
0F01: 11 0C 00        LD      DE,$000C            
0F04: 19              ADD     HL,DE               
0F05: 36 16           LD      (HL),$16            
0F07: 2A C8 87        LD      HL,($87C8)          
0F0A: CB 46           BIT     0,(HL)              
0F0C: C2 46 0F        JP      NZ,$0F46            ; {}
0F0F: CD 6A 12        CALL    $126A               ; {}
0F12: F5              PUSH    AF                  
0F13: 3C              INC     A                   
0F14: 6F              LD      L,A                 
0F15: 87              ADD     A,A                 
0F16: 85              ADD     A,L                 
0F17: 6F              LD      L,A                 
0F18: CD AD 2F        CALL    $2FAD               ; {}
0F1B: F1              POP     AF                  
0F1C: CD 4F 12        CALL    $124F               ; {}
0F1F: A7              AND     A                   
0F20: 20 0F           JR      NZ,$1245            ; {}
0F22: 36 39           LD      (HL),$39            
0F24: 3E 0A           LD      A,$0A               
0F26: 12              LD      (DE),A              
0F27: DD 36 00 00     LD      (IX+$00),$00        
0F2B: 21 F7 98        LD      HL,$98F7            
0F2E: 36 01           LD      (HL),$01            
0F30: C9              RET                         
0F31: 3D              DEC     A                   
0F32: 20 05           JR      NZ,$123B            ; {}
0F34: 36 3A           LD      (HL),$3A            
0F36: C3 24 0F        JP      $0F24               ; {}
0F39: 3D              DEC     A                   
0F3A: 20 05           JR      NZ,$123B            ; {}
0F3C: 36 3B           LD      (HL),$3B            
0F3E: C3 24 0F        JP      $0F24               ; {}
0F41: 36 3C           LD      (HL),$3C            
0F43: C3 24 0F        JP      $0F24               ; {}
0F46: 3A 10 84        LD      A,($8410)           
0F49: FE 0A           CP      $0A                 
0F4B: 30 04           JR      NC,$123A            ; {}
0F4D: 3C              INC     A                   
0F4E: 32 10 84        LD      ($8410),A           
0F51: 3A AE 85        LD      A,($85AE)           
0F54: CB 4F           BIT     1,A                 
0F56: CA 0F 0F        JP      Z,$0F0F             ; {}
0F59: CD 6A 12        CALL    $126A               ; {}
0F5C: F5              PUSH    AF                  
0F5D: 6F              LD      L,A                 
0F5E: 87              ADD     A,A                 
0F5F: 85              ADD     A,L                 
0F60: C6 0F           ADD     $0F                 
0F62: 6F              LD      L,A                 
0F63: CD AD 2F        CALL    $2FAD               ; {}
0F66: F1              POP     AF                  
0F67: CD 4F 12        CALL    $124F               ; {}
0F6A: A7              AND     A                   
0F6B: 20 05           JR      NZ,$123B            ; {}
0F6D: 36 3B           LD      (HL),$3B            
0F6F: C3 24 0F        JP      $0F24               ; {}
0F72: 3D              DEC     A                   
0F73: 20 05           JR      NZ,$123B            ; {}
0F75: 36 3D           LD      (HL),$3D            
0F77: C3 24 0F        JP      $0F24               ; {}
0F7A: 3D              DEC     A                   
0F7B: 20 05           JR      NZ,$123B            ; {}
0F7D: 36 3E           LD      (HL),$3E            
0F7F: C3 24 0F        JP      $0F24               ; {}
0F82: 36 3F           LD      (HL),$3F            
0F84: C3 24 0F        JP      $0F24               ; {}
0F87: 21 82 98        LD      HL,$9882            
0F8A: 06 08           LD      B,$08               
0F8C: 36 00           LD      (HL),$00            
0F8E: 23              INC     HL                  
0F8F: 32 30 68        LD      ($6830),A           
0F92: 10 F8           DJNZ    $122E               ; {}
0F94: C9              RET                         
0F95: 21 08 84        LD      HL,$8408            
0F98: CB C6           SET     0,(HL)              
0F9A: 11 02 98        LD      DE,$9802            
0F9D: DD 21 02 99     LD      IX,$9902            
0FA1: 01 08 00        LD      BC,$0008            
0FA4: FD 21 82 98     LD      IY,$9882            
0FA8: 3A AE 85        LD      A,($85AE)           
0FAB: 32 E4 87        LD      ($87E4),A           
0FAE: CB 4F           BIT     1,A                 
0FB0: 28 17           JR      Z,$124D             ; {}
0FB2: 21 B9 0F        LD      HL,$0FB9            
0FB5: ED B0           LDIR                        
0FB7: 18 15           JR      $124B               ; {}
0FB9: 37              SCF                         
0FBA: 08              EX      AF,AF'              
0FBB: 37              SCF                         
0FBC: 08              EX      AF,AF'              
0FBD: 36 08           LD      (HL),$08            
0FBF: 13              INC     DE                  
0FC0: 06 35           LD      B,$35               
0FC2: 08              EX      AF,AF'              
0FC3: 35              DEC     (HL)                
0FC4: 08              EX      AF,AF'              
0FC5: 34              INC     (HL)                
0FC6: 08              EX      AF,AF'              
0FC7: 12              LD      (DE),A              
0FC8: 06 21           LD      B,$21               
0FCA: C1              POP     BC                  
0FCB: 0F              RRCA                        
0FCC: ED B0           LDIR                        
0FCE: DD E5           PUSH    IX                  
0FD0: E1              POP     HL                  
0FD1: 3A 22 99        LD      A,($9922)           
0FD4: 06 04           LD      B,$04               
0FD6: 77              LD      (HL),A              
0FD7: 23              INC     HL                  
0FD8: 23              INC     HL                  
0FD9: 10 FB           DJNZ    $1231               ; {}
0FDB: FD E5           PUSH    IY                  
0FDD: E1              POP     HL                  
0FDE: 3A A2 98        LD      A,($98A2)           
0FE1: 4F              LD      C,A                 
0FE2: 3A A3 98        LD      A,($98A3)           
0FE5: 06 04           LD      B,$04               
0FE7: 71              LD      (HL),C              
0FE8: 23              INC     HL                  
0FE9: 77              LD      (HL),A              
0FEA: 23              INC     HL                  
0FEB: 10 FA           DJNZ    $1230               ; {}
0FED: C9              RET                         
0FEE: 21 82 98        LD      HL,$9882            
0FF1: FD 21 83 98     LD      IY,$9883            
0FF5: 18 10           JR      $1246               ; {}
0FF7: 21 84 98        LD      HL,$9884            
0FFA: FD 21 85 98     LD      IY,$9885            
0FFE: 18 07           JR      $123D               ; {}
1000: 21 86 98        LD      HL,$9886            
1003: FD 21 87 98     LD      IY,$9887            
1007: 3A 06 98        LD      A,($9806)           
100A: FE 34           CP      $34                 
100C: CA 18 10        JP      Z,$1018             ; {}
100F: 3A 06 99        LD      A,($9906)           
1012: E6 02           AND     $02                 
1014: 28 17           JR      Z,$124D             ; {}
1016: 18 09           JR      $123F               ; {}
1018: 3A 06 99        LD      A,($9906)           
101B: E6 01           AND     $01                 
101D: 28 11           JR      Z,$1247             ; {}
101F: 18 03           JR      $1239               ; {}
1021: 35              DEC     (HL)                
1022: 35              DEC     (HL)                
1023: C9              RET                         
1024: FD 7E 00        LD      A,(IY+$00)          
1027: 3C              INC     A                   
1028: 3C              INC     A                   
1029: FD 77 00        LD      (IY+$00),A          
102C: C9              RET                         
102D: 34              INC     (HL)                
102E: 34              INC     (HL)                
102F: C9              RET                         
1030: FD 7E 00        LD      A,(IY+$00)          
1033: 3D              DEC     A                   
1034: 3D              DEC     A                   
1035: FD 77 00        LD      (IY+$00),A          
1038: C9              RET                         
1039: 3A E4 87        LD      A,($87E4)           
103C: E6 07           AND     $07                 
103E: 28 11           JR      Z,$1247             ; {}
1040: FE 02           CP      $02                 
1042: 28 16           JR      Z,$124C             ; {}
1044: FE 04           CP      $04                 
1046: 28 1B           JR      Z,$1251             ; {}
1048: 2A 02 86        LD      HL,($8602)          
104B: ED 5B 06 86     LD      DE,($8606)          
104F: 18 5C           JR      $1292               ; {}
1051: 2A 02 86        LD      HL,($8602)          
1054: ED 5B 04 86     LD      DE,($8604)          
1058: 18 10           JR      $1246               ; {}
105A: 2A 04 86        LD      HL,($8604)          
105D: ED 5B 08 86     LD      DE,($8608)          
1061: 18 4A           JR      $1280               ; {}
1063: 2A 06 86        LD      HL,($8606)          
1066: ED 5B 08 86     LD      DE,($8608)          
106A: 3A 3E 86        LD      A,($863E)           
106D: FE 2C           CP      $2C                 
106F: 38 08           JR      C,$123E             ; {}
1071: 7E              LD      A,(HL)              
1072: FE 7F           CP      $7F                 
1074: 20 0A           JR      NZ,$1240            ; {}
1076: 0E 00           LD      C,$00               
1078: C9              RET                         
1079: CD 90 10        CALL    $1090               ; {}
107C: 79              LD      A,C                 
107D: FE 00           CP      $00                 
107F: C8              RET     Z                   
1080: EB              EX      DE,HL               
1081: 3A 3E 86        LD      A,($863E)           
1084: FE 2C           CP      $2C                 
1086: 38 08           JR      C,$123E             ; {}
1088: 7E              LD      A,(HL)              
1089: FE 7F           CP      $7F                 
108B: 20 1D           JR      NZ,$1253            ; {}
108D: 0E 00           LD      C,$00               
108F: C9              RET                         
1090: 7E              LD      A,(HL)              
1091: FE 02           CP      $02                 
1093: 28 15           JR      Z,$124B             ; {}
1095: FE 03           CP      $03                 
1097: 28 11           JR      Z,$1247             ; {}
1099: FE 8D           CP      $8D                 
109B: 28 0D           JR      Z,$1243             ; {}
109D: FE 7E           CP      $7E                 
109F: 28 09           JR      Z,$123F             ; {}
10A1: CB BF           RES     7,A                 
10A3: FE 0C           CP      $0C                 
10A5: 28 03           JR      Z,$1239             ; {}
10A7: 0E 00           LD      C,$00               
10A9: C9              RET                         
10AA: 0E 01           LD      C,$01               
10AC: C9              RET                         
10AD: 3A 3E 86        LD      A,($863E)           
10B0: FE 2C           CP      $2C                 
10B2: 38 08           JR      C,$123E             ; {}
10B4: 7E              LD      A,(HL)              
10B5: FE 7F           CP      $7F                 
10B7: 20 0A           JR      NZ,$1240            ; {}
10B9: 0E 00           LD      C,$00               
10BB: C9              RET                         
10BC: CD D3 10        CALL    $10D3               ; {}
10BF: 79              LD      A,C                 
10C0: FE 00           CP      $00                 
10C2: C8              RET     Z                   
10C3: EB              EX      DE,HL               
10C4: 3A 3E 86        LD      A,($863E)           
10C7: FE 2C           CP      $2C                 
10C9: 38 08           JR      C,$123E             ; {}
10CB: 7E              LD      A,(HL)              
10CC: FE 7F           CP      $7F                 
10CE: 20 DA           JR      NZ,$1210            ; {}
10D0: 0E 00           LD      C,$00               
10D2: C9              RET                         
10D3: 7E              LD      A,(HL)              
10D4: FE 08           CP      $08                 
10D6: 28 D2           JR      Z,$1208             ; {}
10D8: FE 09           CP      $09                 
10DA: 28 CE           JR      Z,$1204             ; {}
10DC: 18 BB           JR      $11F1               ; {}
10DE: 21 25 85        LD      HL,$8525            
10E1: 22 F6 85        LD      ($85F6),HL          
10E4: 06 08           LD      B,$08               
10E6: 3A E4 87        LD      A,($87E4)           
10E9: 4F              LD      C,A                 
10EA: DD 2A F6 85     LD      IX,($85F6)          
10EE: DD CB 00 7E     BIT     7,(IX+$00)          
10F2: 20 32           JR      NZ,$1268            ; {}
10F4: DD CB 03 7E     BIT     7,(IX+$03)          
10F8: 20 2C           JR      NZ,$1262            ; {}
10FA: 2A 86 98        LD      HL,($9886)          
10FD: DD 5E 04        LD      E,(IX+$04)          
1100: DD 56 05        LD      D,(IX+$05)          
1103: DD 7E 06        LD      A,(IX+$06)          
1106: FE 40           CP      $40                 
1108: 30 07           JR      NC,$123D            ; {}
110A: CD 75 11        CALL    $1175               ; {}
110D: 30 17           JR      NC,$124D            ; {}
110F: 18 22           JR      $1258               ; {}
1111: 3A 00 84        LD      A,($8400)           
1114: 2F              CPL                         
1115: E6 06           AND     $06                 
1117: 20 08           JR      NZ,$123E            ; {}
1119: 3E 10           LD      A,$10               
111B: 85              ADD     A,L                 
111C: 6F              LD      L,A                 
111D: 3E 10           LD      A,$10               
111F: 84              ADD     A,H                 
1120: 67              LD      H,A                 
1121: CD 9F 11        CALL    $119F               ; {}
1124: 38 0D           JR      C,$1243             ; {}
1126: 2A F6 85        LD      HL,($85F6)          
1129: 11 10 00        LD      DE,$0010            
112C: 19              ADD     HL,DE               
112D: 22 F6 85        LD      ($85F6),HL          
1130: 10 B8           DJNZ    $11EE               ; {}
1132: C9              RET                         
1133: 78              LD      A,B                 
1134: 32 9E 87        LD      ($879E),A           
1137: DD 22 C8 87     LD      ($87C8),IX          
113B: 21 03 84        LD      HL,$8403            
113E: CB D6           SET     2,(HL)              
1140: 21 01 84        LD      HL,$8401            
1143: CB 9E           RES     3,(HL)              
1145: 2A F6 85        LD      HL,($85F6)          
1148: CB B6           RES     6,(HL)              
114A: 11 0C 00        LD      DE,$000C            
114D: 19              ADD     HL,DE               
114E: 22 F6 85        LD      ($85F6),HL          
1151: 21 D7 32        LD      HL,$32D7            
1154: 3A 10 84        LD      A,($8410)           
1157: 3D              DEC     A                   
1158: 5F              LD      E,A                 
1159: 16 00           LD      D,$00               
115B: 19              ADD     HL,DE               
115C: 7E              LD      A,(HL)              
115D: DD 77 0C        LD      (IX+$0C),A          
1160: 21 03 84        LD      HL,$8403            
1163: CB 9E           RES     3,(HL)              
1165: CD 9F 0E        CALL    $0E9F               ; {}
1168: 3A 03 84        LD      A,($8403)           
116B: CB 57           BIT     2,A                 
116D: C8              RET     Z                   
116E: CD 07 12        CALL    $1207               ; {}
1171: CD 07 12        CALL    $1207               ; {}
1174: C9              RET                         
1175: CB 49           BIT     1,C                 
1177: 20 13           JR      NZ,$1249            ; {}
1179: 7D              LD      A,L                 
117A: 93              SUB     E                   
117B: C6 08           ADD     $08                 
117D: FE 0C           CP      $0C                 
117F: D0              RET     NC                  
1180: 7C              LD      A,H                 
1181: 92              SUB     D                   
1182: CB 51           BIT     2,C                 
1184: 28 01           JR      Z,$1237             ; {}
1186: 2F              CPL                         
1187: D6 02           SUB     $02                 
1189: FE 0C           CP      $0C                 
118B: C9              RET                         
118C: 7C              LD      A,H                 
118D: 92              SUB     D                   
118E: C6 08           ADD     $08                 
1190: FE 0C           CP      $0C                 
1192: D0              RET     NC                  
1193: 7D              LD      A,L                 
1194: 93              SUB     E                   
1195: CB 51           BIT     2,C                 
1197: 20 01           JR      NZ,$1237            ; {}
1199: 2F              CPL                         
119A: D6 02           SUB     $02                 
119C: FE 0C           CP      $0C                 
119E: C9              RET                         
119F: CB 49           BIT     1,C                 
11A1: 20 14           JR      NZ,$124A            ; {}
11A3: 7D              LD      A,L                 
11A4: 93              SUB     E                   
11A5: C6 03           ADD     $03                 
11A7: FE 12           CP      $12                 
11A9: D0              RET     NC                  
11AA: 7C              LD      A,H                 
11AB: 92              SUB     D                   
11AC: CB 51           BIT     2,C                 
11AE: 28 02           JR      Z,$1238             ; {}
11B0: C6 10           ADD     $10                 
11B2: D6 03           SUB     $03                 
11B4: FE 12           CP      $12                 
11B6: C9              RET                         
11B7: 7C              LD      A,H                 
11B8: 92              SUB     D                   
11B9: C6 07           ADD     $07                 
11BB: FE 12           CP      $12                 
11BD: D0              RET     NC                  
11BE: 7D              LD      A,L                 
11BF: 93              SUB     E                   
11C0: CB 51           BIT     2,C                 
11C2: 20 02           JR      NZ,$1238            ; {}
11C4: C6 10           ADD     $10                 
11C6: D6 07           SUB     $07                 
11C8: FE 12           CP      $12                 
11CA: C9              RET                         
11CB: 2A 03 84        LD      HL,($8403)          
11CE: CB 5E           BIT     3,(HL)              
11D0: C0              RET     NZ                  
11D1: CB 96           RES     2,(HL)              
11D3: 2B              DEC     HL                  
11D4: 2B              DEC     HL                  
11D5: CB DE           SET     3,(HL)              
11D7: C9              RET                         
11D8: 21 56 86        LD      HL,$8656            
11DB: CB DE           SET     3,(HL)              
11DD: C9              RET                         
11DE: 21 24 98        LD      HL,$9824            
11E1: 06 0C           LD      B,$0C               
11E3: 36 32           LD      (HL),$32            
11E5: 23              INC     HL                  
11E6: 23              INC     HL                  
11E7: 10 FA           DJNZ    $1230               ; {}
11E9: C9              RET                         
11EA: 21 00 84        LD      HL,$8400            
11ED: CB 4E           BIT     1,(HL)              
11EF: 20 0B           JR      NZ,$1241            ; {}
11F1: 21 0D 84        LD      HL,$840D            
11F4: 7E              LD      A,(HL)              
11F5: 23              INC     HL                  
11F6: 23              INC     HL                  
11F7: 77              LD      (HL),A              
11F8: 23              INC     HL                  
11F9: 77              LD      (HL),A              
11FA: 18 08           JR      $123E               ; {}
11FC: 21 0E 84        LD      HL,$840E            
11FF: 7E              LD      A,(HL)              
1200: 23              INC     HL                  
1201: 77              LD      (HL),A              
1202: 23              INC     HL                  
1203: 77              LD      (HL),A              
1204: C3 BB 19        JP      $19BB               ; {}
1207: 2A 42 86        LD      HL,($8642)          
120A: 7E              LD      A,(HL)              
120B: A7              AND     A                   
120C: C8              RET     Z                   
120D: 35              DEC     (HL)                
120E: 35              DEC     (HL)                
120F: 7E              LD      A,(HL)              
1210: FE 22           CP      $22                 
1212: D2 20 12        JP      NC,$1220            ; {}
1215: FE 12           CP      $12                 
1217: D2 1D 12        JP      NC,$121D            ; {}
121A: CD EE 0F        CALL    $0FEE               ; {}
121D: CD F7 0F        CALL    $0FF7               ; {}
1220: CD 00 10        CALL    $1000               ; {}
1223: C9              RET                         
1224: A7              AND     A                   
1225: 86              ADD     A,(HL)              
1226: 27              DAA                         
1227: 77              LD      (HL),A              
1228: 2B              DEC     HL                  
1229: 7E              LD      A,(HL)              
122A: CE 00           ADC     $00                 
122C: 27              DAA                         
122D: 77              LD      (HL),A              
122E: C9              RET                         
122F: C5              PUSH    BC                  
1230: F5              PUSH    AF                  
1231: 3A 00 84        LD      A,($8400)           
1234: CB 4F           BIT     1,A                 
1236: 28 14           JR      Z,$124A             ; {}
1238: CB 57           BIT     2,A                 
123A: 28 10           JR      Z,$1246             ; {}
123C: 2A F6 85        LD      HL,($85F6)          
123F: 11 04 00        LD      DE,$0004            
1242: 19              ADD     HL,DE               
1243: 7E              LD      A,(HL)              
1244: C6 10           ADD     $10                 
1246: 77              LD      (HL),A              
1247: 23              INC     HL                  
1248: 7E              LD      A,(HL)              
1249: C6 10           ADD     $10                 
124B: 77              LD      (HL),A              
124C: F1              POP     AF                  
124D: C1              POP     BC                  
124E: C9              RET                         
124F: DD 21 7E 99     LD      IX,$997E            
1253: 21 7E 98        LD      HL,$987E            
1256: 36 47           LD      (HL),$47            
1258: 23              INC     HL                  
1259: 36 0A           LD      (HL),$0A            
125B: DD 36 00 00     LD      (IX+$00),$00        
125F: DD 21 76 99     LD      IX,$9976            
1263: 21 76 98        LD      HL,$9876            
1266: 11 77 98        LD      DE,$9877            
1269: C9              RET                         
126A: 11 05 00        LD      DE,$0005            
126D: 19              ADD     HL,DE               
126E: 3A 00 84        LD      A,($8400)           
1271: CB 4F           BIT     1,A                 
1273: 28 09           JR      Z,$123F             ; {}
1275: CB 57           BIT     2,A                 
1277: 28 05           JR      Z,$123B             ; {}
1279: 7E              LD      A,(HL)              
127A: D6 10           SUB     $10                 
127C: 18 01           JR      $1237               ; {}
127E: 7E              LD      A,(HL)              
127F: FE 20           CP      $20                 
1281: 38 02           JR      C,$1238             ; {}
1283: D6 08           SUB     $08                 
1285: 07              RLCA                        
1286: 07              RLCA                        
1287: E6 03           AND     $03                 
1289: C9              RET                         
128A: 21 80 9A        LD      HL,$9A80            
128D: 06 20           LD      B,$20               
128F: 36 00           LD      (HL),$00            
1291: 23              INC     HL                  
1292: 10 FB           DJNZ    $1231               ; {}
1294: C9              RET                         
1295: 21 25 85        LD      HL,$8525            
1298: 11 A5 84        LD      DE,$84A5            
129B: 01 80 00        LD      BC,$0080            
129E: CD BC 12        CALL    $12BC               ; {}
12A1: C9              RET                         
12A2: 21 65 84        LD      HL,$8465            
12A5: 11 25 84        LD      DE,$8425            
12A8: 01 40 00        LD      BC,$0040            
12AB: CD BC 12        CALL    $12BC               ; {}
12AE: C9              RET                         
12AF: 21 40 80        LD      HL,$8040            
12B2: 11 00 90        LD      DE,$9000            
12B5: 01 80 03        LD      BC,$0380            
12B8: CD BC 12        CALL    $12BC               ; {}
12BB: C9              RET                         
12BC: 1A              LD      A,(DE)              
12BD: ED A0           LDI                         
12BF: 2B              DEC     HL                  
12C0: 77              LD      (HL),A              
12C1: 23              INC     HL                  
12C2: 79              LD      A,C                 
12C3: B0              OR      B                   
12C4: 20 F6           JR      NZ,$122C            ; {}
12C6: C9              RET                         
12C7: CD 17 13        CALL    $1317               ; {}
12CA: CD 31 13        CALL    $1331               ; {}
12CD: CD DA 12        CALL    $12DA               ; {}
12D0: C9              RET                         
12D1: CD 17 13        CALL    $1317               ; {}
12D4: CD 42 13        CALL    $1342               ; {}
12D7: C3 CD 12        JP      $12CD               ; {}
12DA: 21 03 13        LD      HL,$1303            
12DD: 11 F0 98        LD      DE,$98F0            
12E0: 01 08 00        LD      BC,$0008            
12E3: C5              PUSH    BC                  
12E4: ED B0           LDIR                        
12E6: C1              POP     BC                  
12E7: 21 FB 12        LD      HL,$12FB            
12EA: 11 70 98        LD      DE,$9870            
12ED: ED B0           LDIR                        
12EF: 21 70 99        LD      HL,$9970            
12F2: 06 04           LD      B,$04               
12F4: 36 00           LD      (HL),$00            
12F6: 23              INC     HL                  
12F7: 23              INC     HL                  
12F8: 10 FA           DJNZ    $1230               ; {}
12FA: C9              RET                         
12FB: 68              LD      L,B                 
12FC: 0C              INC     C                   
12FD: 71              LD      (HL),C              
12FE: 0C              INC     C                   
12FF: 70              LD      (HL),B              
1300: 0C              INC     C                   
1301: 6F              LD      L,A                 
1302: 0C              INC     C                   
1303: 91              SUB     C                   
1304: 98              SBC     B                   
1305: 81              ADD     A,C                 
1306: 98              SBC     B                   
1307: 69              LD      L,C                 
1308: 98              SBC     B                   
1309: 59              LD      E,C                 
130A: 98              SBC     B                   
130B: 79              LD      A,C                 
130C: 70              LD      (HL),B              
130D: 69              LD      L,C                 
130E: 70              LD      (HL),B              
130F: 59              LD      E,C                 
1310: 70              LD      (HL),B              
1311: 68              LD      L,B                 
1312: 0C              INC     C                   
1313: 67              LD      H,A                 
1314: 0C              INC     C                   
1315: 66              LD      H,(HL)              
1316: 0C              INC     C                   
1317: 21 0B 13        LD      HL,$130B            
131A: 11 FA 98        LD      DE,$98FA            
131D: 01 06 00        LD      BC,$0006            
1320: C5              PUSH    BC                  
1321: ED B0           LDIR                        
1323: C1              POP     BC                  
1324: 21 11 13        LD      HL,$1311            
1327: 11 7A 98        LD      DE,$987A            
132A: ED B0           LDIR                        
132C: 21 78 99        LD      HL,$9978            
132F: 18 C1           JR      $11F7               ; {}
1331: 21 78 98        LD      HL,$9878            
1334: 36 6A           LD      (HL),$6A            
1336: 23              INC     HL                  
1337: 36 0C           LD      (HL),$0C            
1339: 21 F8 98        LD      HL,$98F8            
133C: 36 89           LD      (HL),$89            
133E: 23              INC     HL                  
133F: 36 70           LD      (HL),$70            
1341: C9              RET                         
1342: 21 78 98        LD      HL,$9878            
1345: 36 6B           LD      (HL),$6B            
1347: 18 ED           JR      $1223               ; {}
1349: C3 D1 1C        JP      $1CD1               ; {}
134C: 21 29 85        LD      HL,$8529            
134F: 11 10 00        LD      DE,$0010            
1352: 06 08           LD      B,$08               
1354: 22 F6 85        LD      ($85F6),HL          
1357: 4E              LD      C,(HL)              
1358: 3A A2 98        LD      A,($98A2)           
135B: B9              CP      C                   
135C: DA 62 13        JP      C,$1362             ; {}
135F: 91              SUB     C                   
1360: 18 05           JR      $123B               ; {}
1362: D5              PUSH    DE                  
1363: 57              LD      D,A                 
1364: 79              LD      A,C                 
1365: 92              SUB     D                   
1366: D1              POP     DE                  
1367: 32 1A 86        LD      ($861A),A           
136A: 2A F6 85        LD      HL,($85F6)          
136D: 23              INC     HL                  
136E: 4E              LD      C,(HL)              
136F: 3A A3 98        LD      A,($98A3)           
1372: B9              CP      C                   
1373: DA 79 13        JP      C,$1379             ; {}
1376: 91              SUB     C                   
1377: 18 05           JR      $123B               ; {}
1379: D5              PUSH    DE                  
137A: 57              LD      D,A                 
137B: 79              LD      A,C                 
137C: 92              SUB     D                   
137D: D1              POP     DE                  
137E: 5F              LD      E,A                 
137F: 16 00           LD      D,$00               
1381: 3A 1A 86        LD      A,($861A)           
1384: 6F              LD      L,A                 
1385: 26 00           LD      H,$00               
1387: 19              ADD     HL,DE               
1388: 7C              LD      A,H                 
1389: A7              AND     A                   
138A: C2 FD 13        JP      NZ,$13FD            ; {}
138D: 7D              LD      A,L                 
138E: FE 0A           CP      $0A                 
1390: D2 FD 13        JP      NC,$13FD            ; {}
1393: 2A F6 85        LD      HL,($85F6)          
1396: 2B              DEC     HL                  
1397: 2B              DEC     HL                  
1398: 2B              DEC     HL                  
1399: 2B              DEC     HL                  
139A: 7E              LD      A,(HL)              
139B: E6 BC           AND     $BC                 
139D: C2 FD 13        JP      NZ,$13FD            ; {}
13A0: 21 4A 86        LD      HL,$864A            
13A3: CB 86           RES     0,(HL)              
13A5: 21 01 84        LD      HL,$8401            
13A8: CB 7E           BIT     7,(HL)              
13AA: C0              RET     NZ                  
13AB: CB FE           SET     7,(HL)              
13AD: 23              INC     HL                  
13AE: CB 86           RES     0,(HL)              
13B0: 21 4A 86        LD      HL,$864A            
13B3: CB 46           BIT     0,(HL)              
13B5: 20 1F           JR      NZ,$1255            ; {}
13B7: 2A F6 85        LD      HL,($85F6)          
13BA: 2B              DEC     HL                  
13BB: 2B              DEC     HL                  
13BC: 2B              DEC     HL                  
13BD: 2B              DEC     HL                  
13BE: CB 8E           RES     1,(HL)              
13C0: CB 46           BIT     0,(HL)              
13C2: F5              PUSH    AF                  
13C3: 11 06 00        LD      DE,$0006            
13C6: 19              ADD     HL,DE               
13C7: F1              POP     AF                  
13C8: 20 07           JR      NZ,$123D            ; {}
13CA: 36 20           LD      (HL),$20            
13CC: 23              INC     HL                  
13CD: 36 01           LD      (HL),$01            
13CF: 18 05           JR      $123B               ; {}
13D1: 36 24           LD      (HL),$24            
13D3: 23              INC     HL                  
13D4: 36 02           LD      (HL),$02            
13D6: 21 1C 86        LD      HL,$861C            
13D9: 36 A0           LD      (HL),$A0            
13DB: CD 8A 12        CALL    $128A               ; {}
13DE: 21 76 98        LD      HL,$9876            
13E1: 36 32           LD      (HL),$32            
13E3: 21 7E 98        LD      HL,$987E            
13E6: 36 32           LD      (HL),$32            
13E8: 3E 01           LD      A,$01               
13EA: 32 84 9A        LD      ($9A84),A           
13ED: 21 22 98        LD      HL,$9822            
13F0: 3A AE 85        LD      A,($85AE)           
13F3: CB 4F           BIT     1,A                 
13F5: 28 03           JR      Z,$1239             ; {}
13F7: 36 4D           LD      (HL),$4D            
13F9: C9              RET                         
13FA: 36 4C           LD      (HL),$4C            
13FC: C9              RET                         
13FD: 2A F6 85        LD      HL,($85F6)          
1400: 11 10 00        LD      DE,$0010            
1403: 19              ADD     HL,DE               
1404: 05              DEC     B                   
1405: C2 54 13        JP      NZ,$1354            ; {}
1408: C9              RET                         
1409: 21 00 84        LD      HL,$8400            
140C: CB 4E           BIT     1,(HL)              
140E: 20 07           JR      NZ,$123D            ; {}
1410: 3A 0A 84        LD      A,($840A)           
1413: 32 0C 84        LD      ($840C),A           
1416: C9              RET                         
1417: 3A 0B 84        LD      A,($840B)           
141A: 32 0C 84        LD      ($840C),A           
141D: C9              RET                         
141E: AF              XOR     A                   
141F: 32 92 9A        LD      ($9A92),A           
1422: C9              RET                         
1423: 3A 46 86        LD      A,($8646)           
1426: CB 47           BIT     0,A                 
1428: 20 F4           JR      NZ,$122A            ; {}
142A: 3E 01           LD      A,$01               
142C: 32 92 9A        LD      ($9A92),A           
142F: C9              RET                         
1430: 21 D4 83        LD      HL,$83D4            
1433: DD 21 43 14     LD      IX,$1443            
1437: 06 0A           LD      B,$0A               
1439: DD 7E 00        LD      A,(IX+$00)          
143C: 77              LD      (HL),A              
143D: 2B              DEC     HL                  
143E: DD 23           INC     IX                  
1440: 10 F7           DJNZ    $122D               ; {}
1442: C9              RET                         
1443: A1              AND     C                   
1444: A2              AND     D                   
1445: A0              AND     B                   
1446: A1              AND     C                   
1447: 7F              LD      A,A                 
1448: AC              XOR     H                   
1449: 9C              SBC     H                   
144A: A8              XOR     B                   
144B: AB              XOR     E                   
144C: 9E              SBC     (HL)                
144D: 21 DA 83        LD      HL,$83DA            
1450: DD 21 63 14     LD      IX,$1463            
1454: 06 03           LD      B,$03               
1456: C3 39 14        JP      $1439               ; {}
1459: 21 C7 83        LD      HL,$83C7            
145C: DD 21 66 14     LD      IX,$1466            
1460: C3 54 14        JP      $1454               ; {}
1463: 91              SUB     C                   
1464: AE              XOR     (HL)                
1465: A9              XOR     C                   
1466: 92              SUB     D                   
1467: AE              XOR     (HL)                
1468: A9              XOR     C                   
1469: CD 30 14        CALL    $1430               ; {}
146C: CD 81 14        CALL    $1481               ; {}
146F: CD DC 14        CALL    $14DC               ; {}
1472: 3A 00 84        LD      A,($8400)           
1475: CB 47           BIT     0,A                 
1477: CA 7D 14        JP      Z,$147D             ; {}
147A: CD F2 14        CALL    $14F2               ; {}
147D: CD E7 14        CALL    $14E7               ; {}
1480: C9              RET                         
1481: 3A 00 84        LD      A,($8400)           
1484: CB 47           BIT     0,A                 
1486: C2 9A 14        JP      NZ,$149A            ; {}
1489: CD D6 14        CALL    $14D6               ; {}
148C: 3A 23 84        LD      A,($8423)           
148F: CB 6F           BIT     5,A                 
1491: F5              PUSH    AF                  
1492: C4 4D 14        CALL    NZ,$144D            ; {}
1495: F1              POP     AF                  
1496: CC B6 14        CALL    Z,$14B6             ; {}
1499: C9              RET                         
149A: CB 4F           BIT     1,A                 
149C: C2 A5 14        JP      NZ,$14A5            ; {}
149F: CD 59 14        CALL    $1459               ; {}
14A2: C3 8C 14        JP      $148C               ; {}
14A5: CD 4D 14        CALL    $144D               ; {}
14A8: 3A 23 84        LD      A,($8423)           
14AB: CB 6F           BIT     5,A                 
14AD: F5              PUSH    AF                  
14AE: C4 59 14        CALL    NZ,$1459            ; {}
14B1: F1              POP     AF                  
14B2: CC D6 14        CALL    Z,$14D6             ; {}
14B5: C9              RET                         
14B6: 21 DA 83        LD      HL,$83DA            
14B9: 3A CC 87        LD      A,($87CC)           
14BC: CB 4F           BIT     1,A                 
14BE: CA CE 14        JP      Z,$14CE             ; {}
14C1: CB 57           BIT     2,A                 
14C3: C2 CE 14        JP      NZ,$14CE            ; {}
14C6: 3E 0C           LD      A,$0C               
14C8: 77              LD      (HL),A              
14C9: 2B              DEC     HL                  
14CA: 77              LD      (HL),A              
14CB: 2B              DEC     HL                  
14CC: 77              LD      (HL),A              
14CD: C9              RET                         
14CE: 3E 8C           LD      A,$8C               
14D0: 77              LD      (HL),A              
14D1: 2B              DEC     HL                  
14D2: 77              LD      (HL),A              
14D3: 2B              DEC     HL                  
14D4: 77              LD      (HL),A              
14D5: C9              RET                         
14D6: 21 C7 83        LD      HL,$83C7            
14D9: C3 B9 14        JP      $14B9               ; {}
14DC: 11 27 89        LD      DE,$8927            
14DF: DD 21 F2 83     LD      IX,$83F2            
14E3: CD FD 14        CALL    $14FD               ; {}
14E6: C9              RET                         
14E7: 11 14 84        LD      DE,$8414            
14EA: DD 21 FC 83     LD      IX,$83FC            
14EE: CD FD 14        CALL    $14FD               ; {}
14F1: C9              RET                         
14F2: 11 17 84        LD      DE,$8417            
14F5: DD 21 E9 83     LD      IX,$83E9            
14F9: CD FD 14        CALL    $14FD               ; {}
14FC: C9              RET                         
14FD: 21 1D 84        LD      HL,$841D            
1500: 06 03           LD      B,$03               
1502: 1A              LD      A,(DE)              
1503: E6 0F           AND     $0F                 
1505: 77              LD      (HL),A              
1506: 23              INC     HL                  
1507: 1A              LD      A,(DE)              
1508: CB 3F           SRL     A                   
150A: CB 3F           SRL     A                   
150C: CB 3F           SRL     A                   
150E: CB 3F           SRL     A                   
1510: 77              LD      (HL),A              
1511: 23              INC     HL                  
1512: 13              INC     DE                  
1513: 10 ED           DJNZ    $1223               ; {}
1515: 21 22 84        LD      HL,$8422            
1518: 06 04           LD      B,$04               
151A: 7E              LD      A,(HL)              
151B: A7              AND     A                   
151C: 20 18           JR      NZ,$124E            ; {}
151E: 3A CC 87        LD      A,($87CC)           
1521: CB 4F           BIT     1,A                 
1523: CA 30 15        JP      Z,$1530             ; {}
1526: CB 57           BIT     2,A                 
1528: C2 30 15        JP      NZ,$1530            ; {}
152B: 3E 0C           LD      A,$0C               
152D: C3 32 15        JP      $1532               ; {}
1530: 3E 8C           LD      A,$8C               
1532: 77              LD      (HL),A              
1533: 2B              DEC     HL                  
1534: 10 E4           DJNZ    $121A               ; {}
1536: 21 22 84        LD      HL,$8422            
1539: 06 06           LD      B,$06               
153B: 7E              LD      A,(HL)              
153C: FE 8C           CP      $8C                 
153E: 28 06           JR      Z,$123C             ; {}
1540: FE 0C           CP      $0C                 
1542: 28 02           JR      Z,$1238             ; {}
1544: C6 10           ADD     $10                 
1546: DD 77 00        LD      (IX+$00),A          
1549: 2B              DEC     HL                  
154A: DD 2B           DEC     IX                  
154C: 10 ED           DJNZ    $1223               ; {}
154E: C9              RET                         
154F: 21 A4 98        LD      HL,$98A4            
1552: 06 0C           LD      B,$0C               
1554: 36 00           LD      (HL),$00            
1556: 23              INC     HL                  
1557: 36 50           LD      (HL),$50            
1559: 23              INC     HL                  
155A: 10 F8           DJNZ    $122E               ; {}
155C: C9              RET                         
155D: DD 4E 00        LD      C,(IX+$00)          
1560: 3A A2 98        LD      A,($98A2)           
1563: B9              CP      C                   
1564: DA 6A 15        JP      C,$156A             ; {}
1567: 91              SUB     C                   
1568: 18 03           JR      $1239               ; {}
156A: 57              LD      D,A                 
156B: 79              LD      A,C                 
156C: 92              SUB     D                   
156D: FE 0B           CP      $0B                 
156F: D0              RET     NC                  
1570: FD 4E 00        LD      C,(IY+$00)          
1573: 3A A3 98        LD      A,($98A3)           
1576: B9              CP      C                   
1577: DA 7D 15        JP      C,$157D             ; {}
157A: 91              SUB     C                   
157B: 18 03           JR      $1239               ; {}
157D: 57              LD      D,A                 
157E: 79              LD      A,C                 
157F: 92              SUB     D                   
1580: FE 0B           CP      $0B                 
1582: D0              RET     NC                  
1583: 2A F6 85        LD      HL,($85F6)          
1586: 11 04 00        LD      DE,$0004            
1589: 19              ADD     HL,DE               
158A: 22 F6 85        LD      ($85F6),HL          
158D: 21 4A 86        LD      HL,$864A            
1590: CB C6           SET     0,(HL)              
1592: C3 A5 13        JP      $13A5               ; {}
1595: F5              PUSH    AF                  
1596: 21 00 80        LD      HL,$8000            
1599: 01 C0 03        LD      BC,$03C0            
159C: CD BD 15        CALL    $15BD               ; {}
159F: CD EA 11        CALL    $11EA               ; {}
15A2: F1              POP     AF                  
15A3: C9              RET                         
15A4: F5              PUSH    AF                  
15A5: 21 40 80        LD      HL,$8040            
15A8: 01 80 03        LD      BC,$0380            
15AB: CD BD 15        CALL    $15BD               ; {}
15AE: 21 C0 83        LD      HL,$83C0            
15B1: 06 3F           LD      B,$3F               
15B3: 36 7F           LD      (HL),$7F            
15B5: 32 30 68        LD      ($6830),A           
15B8: 23              INC     HL                  
15B9: 10 F8           DJNZ    $122E               ; {}
15BB: F1              POP     AF                  
15BC: C9              RET                         
15BD: 36 7F           LD      (HL),$7F            
15BF: 32 30 68        LD      ($6830),A           
15C2: 23              INC     HL                  
15C3: 0B              DEC     BC                  
15C4: 79              LD      A,C                 
15C5: B0              OR      B                   
15C6: 20 F5           JR      NZ,$122B            ; {}
15C8: C9              RET                         
15C9: F5              PUSH    AF                  
15CA: 11 20 00        LD      DE,$0020            
15CD: DD 7E 00        LD      A,(IX+$00)          
15D0: 77              LD      (HL),A              
15D1: DD 23           INC     IX                  
15D3: 19              ADD     HL,DE               
15D4: F1              POP     AF                  
15D5: 3D              DEC     A                   
15D6: 20 F1           JR      NZ,$1227            ; {}
15D8: C9              RET                         
15D9: F5              PUSH    AF                  
15DA: 21 5A 30        LD      HL,$305A            
15DD: 11 16 80        LD      DE,$8016            
15E0: 01 06 00        LD      BC,$0006            
15E3: ED B0           LDIR                        
15E5: 3A A5 85        LD      A,($85A5)           
15E8: 47              LD      B,A                 
15E9: E6 0F           AND     $0F                 
15EB: C6 10           ADD     $10                 
15ED: 32 13 80        LD      ($8013),A           
15F0: 78              LD      A,B                 
15F1: 0F              RRCA                        
15F2: 0F              RRCA                        
15F3: 0F              RRCA                        
15F4: 0F              RRCA                        
15F5: E6 0F           AND     $0F                 
15F7: 28 04           JR      Z,$123A             ; {}
15F9: C6 10           ADD     $10                 
15FB: 18 02           JR      $1238               ; {}
15FD: 3E 7F           LD      A,$7F               
15FF: 32 14 80        LD      ($8014),A           
1602: F1              POP     AF                  
1603: C9              RET                         
1604: 21 2D 81        LD      HL,$812D            
1607: 11 20 00        LD      DE,$0020            
160A: 3A A5 85        LD      A,($85A5)           
160D: FE 01           CP      $01                 
160F: 20 0A           JR      NZ,$1240            ; {}
1611: DD 21 67 30     LD      IX,$3067            
1615: 3E 0D           LD      A,$0D               
1617: CD C9 15        CALL    $15C9               ; {}
161A: C9              RET                         
161B: DD 21 74 30     LD      IX,$3074            
161F: 3E 0E           LD      A,$0E               
1621: 18 F4           JR      $122A               ; {}
1623: F5              PUSH    AF                  
1624: 21 FA 80        LD      HL,$80FA            
1627: 11 20 00        LD      DE,$0020            
162A: DD 21 82 30     LD      IX,$3082            
162E: 3E 11           LD      A,$11               
1630: CD C9 15        CALL    $15C9               ; {}
1633: 21 9C 81        LD      HL,$819C            
1636: DD 21 93 30     LD      IX,$3093            
163A: 3E 08           LD      A,$08               
163C: 18 4B           JR      $1281               ; {}
163E: F5              PUSH    AF                  
163F: 21 EA 80        LD      HL,$80EA            
1642: 11 20 00        LD      DE,$0020            
1645: DD 21 9B 30     LD      IX,$309B            
1649: 3E 11           LD      A,$11               
164B: CD C9 15        CALL    $15C9               ; {}
164E: 3A C0 87        LD      A,($87C0)           
1651: A7              AND     A                   
1652: 20 02           JR      NZ,$1238            ; {}
1654: F1              POP     AF                  
1655: C9              RET                         
1656: 21 B1 80        LD      HL,$80B1            
1659: DD 21 AC 30     LD      IX,$30AC            
165D: 3E 14           LD      A,$14               
165F: CD C9 15        CALL    $15C9               ; {}
1662: 3A C0 87        LD      A,($87C0)           
1665: FE 01           CP      $01                 
1667: 20 02           JR      NZ,$1238            ; {}
1669: F1              POP     AF                  
166A: C9              RET                         
166B: 21 B4 80        LD      HL,$80B4            
166E: DD 21 C0 30     LD      IX,$30C0            
1672: 3E 14           LD      A,$14               
1674: CD C9 15        CALL    $15C9               ; {}
1677: 3A C0 87        LD      A,($87C0)           
167A: FE 02           CP      $02                 
167C: 20 02           JR      NZ,$1238            ; {}
167E: F1              POP     AF                  
167F: C9              RET                         
1680: 21 B7 80        LD      HL,$80B7            
1683: DD 21 D4 30     LD      IX,$30D4            
1687: 3E 14           LD      A,$14               
1689: CD C9 15        CALL    $15C9               ; {}
168C: F1              POP     AF                  
168D: C9              RET                         
168E: F5              PUSH    AF                  
168F: 3A C0 87        LD      A,($87C0)           
1692: A7              AND     A                   
1693: 20 02           JR      NZ,$1238            ; {}
1695: F1              POP     AF                  
1696: C9              RET                         
1697: 11 20 00        LD      DE,$0020            
169A: 21 B1 81        LD      HL,$81B1            
169D: 01 AA 85        LD      BC,$85AA            
16A0: 0A              LD      A,(BC)              
16A1: C6 50           ADD     $50                 
16A3: 77              LD      (HL),A              
16A4: 03              INC     BC                  
16A5: 19              ADD     HL,DE               
16A6: 0A              LD      A,(BC)              
16A7: A7              AND     A                   
16A8: 28 05           JR      Z,$123B             ; {}
16AA: C6 50           ADD     $50                 
16AC: 77              LD      (HL),A              
16AD: 18 02           JR      $1238               ; {}
16AF: 36 7F           LD      (HL),$7F            
16B1: 3A C0 87        LD      A,($87C0)           
16B4: FE 01           CP      $01                 
16B6: 20 02           JR      NZ,$1238            ; {}
16B8: F1              POP     AF                  
16B9: C9              RET                         
16BA: 21 B4 81        LD      HL,$81B4            
16BD: CD D1 16        CALL    $16D1               ; {}
16C0: 3A C0 87        LD      A,($87C0)           
16C3: FE 02           CP      $02                 
16C5: 20 02           JR      NZ,$1238            ; {}
16C7: F1              POP     AF                  
16C8: C9              RET                         
16C9: 21 B7 81        LD      HL,$81B7            
16CC: CD D1 16        CALL    $16D1               ; {}
16CF: F1              POP     AF                  
16D0: C9              RET                         
16D1: 01 AC 85        LD      BC,$85AC            
16D4: 11 20 00        LD      DE,$0020            
16D7: 0A              LD      A,(BC)              
16D8: C6 50           ADD     $50                 
16DA: 77              LD      (HL),A              
16DB: 03              INC     BC                  
16DC: 19              ADD     HL,DE               
16DD: DD 19           ADD     IX,DE               
16DF: 0A              LD      A,(BC)              
16E0: C6 50           ADD     $50                 
16E2: 77              LD      (HL),A              
16E3: 21 32 85        LD      HL,$8532            
16E6: 11 64 99        LD      DE,$9964            
16E9: 06 08           LD      B,$08               
16EB: 7E              LD      A,(HL)              
16EC: 12              LD      (DE),A              
16ED: 13              INC     DE                  
16EE: 13              INC     DE                  
16EF: D5              PUSH    DE                  
16F0: 11 10 00        LD      DE,$0010            
16F3: 19              ADD     HL,DE               
16F4: D1              POP     DE                  
16F5: 10 F4           DJNZ    $122A               ; {}
16F7: C9              RET                         
16F8: 3A 00 84        LD      A,($8400)           
16FB: CB 4F           BIT     1,A                 
16FD: 20 05           JR      NZ,$123B            ; {}
16FF: 21 0D 84        LD      HL,$840D            
1702: 18 03           JR      $1239               ; {}
1704: 21 0E 84        LD      HL,$840E            
1707: 7E              LD      A,(HL)              
1708: 21 E8 87        LD      HL,$87E8            
170B: FE 12           CP      $12                 
170D: DA 12 17        JP      C,$1712             ; {}
1710: 3E 12           LD      A,$12               
1712: 77              LD      (HL),A              
1713: D6 01           SUB     $01                 
1715: 87              ADD     A,A                 
1716: 87              ADD     A,A                 
1717: 5F              LD      E,A                 
1718: 16 00           LD      D,$00               
171A: 21 32 17        LD      HL,$1732            
171D: 19              ADD     HL,DE               
171E: 7E              LD      A,(HL)              
171F: 32 1E 98        LD      ($981E),A           
1722: 23              INC     HL                  
1723: 7E              LD      A,(HL)              
1724: 32 1F 98        LD      ($981F),A           
1727: 23              INC     HL                  
1728: 7E              LD      A,(HL)              
1729: 32 E7 87        LD      ($87E7),A           
172C: 23              INC     HL                  
172D: 7E              LD      A,(HL)              
172E: 32 E6 87        LD      ($87E6),A           
1731: C9              RET                         
1732: 52              LD      D,D                 
1733: 0D              DEC     C                   
1734: 04              INC     B                   
1735: 5D              LD      E,L                 
1736: 53              LD      D,E                 
1737: 0E 06           LD      C,$06               
1739: 5E              LD      E,(HL)              
173A: 54              LD      D,H                 
173B: 0F              RRCA                        
173C: 08              EX      AF,AF'              
173D: 5F              LD      E,A                 
173E: 55              LD      D,L                 
173F: 10 10           DJNZ    $1246               ; {}
1741: 60              LD      H,B                 
1742: 55              LD      D,L                 
1743: 10 10           DJNZ    $1246               ; {}
1745: 60              LD      H,B                 
1746: 56              LD      D,(HL)              
1747: 10 20           DJNZ    $1256               ; {}
1749: 4E              LD      C,(HL)              
174A: 56              LD      D,(HL)              
174B: 10 20           DJNZ    $1256               ; {}
174D: 4E              LD      C,(HL)              
174E: 57              LD      D,A                 
174F: 11 30 4F        LD      DE,$4F30            
1752: 57              LD      D,A                 
1753: 11 30 4F        LD      DE,$4F30            
1756: 58              LD      E,B                 
1757: 12              LD      (DE),A              
1758: 40              LD      B,B                 
1759: 61              LD      H,C                 
175A: 58              LD      E,B                 
175B: 12              LD      (DE),A              
175C: 40              LD      B,B                 
175D: 61              LD      H,C                 
175E: 59              LD      E,C                 
175F: 13              INC     DE                  
1760: 50              LD      D,B                 
1761: 50              LD      D,B                 
1762: 59              LD      E,C                 
1763: 13              INC     DE                  
1764: 50              LD      D,B                 
1765: 50              LD      D,B                 
1766: 5A              LD      E,D                 
1767: 14              INC     D                   
1768: 60              LD      H,B                 
1769: 62              LD      H,D                 
176A: 5A              LD      E,D                 
176B: 14              INC     D                   
176C: 60              LD      H,B                 
176D: 62              LD      H,D                 
176E: 5B              LD      E,E                 
176F: 15              DEC     D                   
1770: 70              LD      (HL),B              
1771: 51              LD      D,C                 
1772: 5B              LD      E,E                 
1773: 15              DEC     D                   
1774: 70              LD      (HL),B              
1775: 51              LD      D,C                 
1776: 5C              LD      E,H                 
1777: 16 80           LD      D,$80               
1779: 63              LD      H,E                 
177A: 21 00 90        LD      HL,$9000            
177D: 7D              LD      A,L                 
177E: E6 1F           AND     $1F                 
1780: FE 03           CP      $03                 
1782: DA A0 17        JP      C,$17A0             ; {}
1785: 36 7F           LD      (HL),$7F            
1787: 23              INC     HL                  
1788: 32 30 68        LD      ($6830),A           
178B: 7D              LD      A,L                 
178C: FE 80           CP      $80                 
178E: 20 ED           JR      NZ,$1223            ; {}
1790: 7C              LD      A,H                 
1791: FE 93           CP      $93                 
1793: 20 E8           JR      NZ,$121E            ; {}
1795: 3E 8F           LD      A,$8F               
1797: 32 01 90        LD      ($9001),A           
179A: 3E 8E           LD      A,$8E               
179C: 32 61 93        LD      ($9361),A           
179F: C9              RET                         
17A0: FE 01           CP      $01                 
17A2: 20 04           JR      NZ,$123A            ; {}
17A4: 36 8D           LD      (HL),$8D            
17A6: 18 DF           JR      $1215               ; {}
17A8: 36 7E           LD      (HL),$7E            
17AA: 18 DB           JR      $1211               ; {}
17AC: 21 40 80        LD      HL,$8040            
17AF: 7D              LD      A,L                 
17B0: E6 1F           AND     $1F                 
17B2: FE 03           CP      $03                 
17B4: DA DF 17        JP      C,$17DF             ; {}
17B7: 36 7F           LD      (HL),$7F            
17B9: 23              INC     HL                  
17BA: 32 30 68        LD      ($6830),A           
17BD: 7D              LD      A,L                 
17BE: FE C0           CP      $C0                 
17C0: 20 ED           JR      NZ,$1223            ; {}
17C2: 7C              LD      A,H                 
17C3: FE 83           CP      $83                 
17C5: 20 E8           JR      NZ,$121E            ; {}
17C7: 3E 8F           LD      A,$8F               
17C9: 32 41 80        LD      ($8041),A           
17CC: 36 8E           LD      (HL),$8E            
17CE: 32 A1 83        LD      ($83A1),A           
17D1: 21 00 80        LD      HL,$8000            
17D4: 06 40           LD      B,$40               
17D6: 32 30 68        LD      ($6830),A           
17D9: 36 0C           LD      (HL),$0C            
17DB: 23              INC     HL                  
17DC: 10 F8           DJNZ    $122E               ; {}
17DE: C9              RET                         
17DF: FE 01           CP      $01                 
17E1: 20 04           JR      NZ,$123A            ; {}
17E3: 36 8D           LD      (HL),$8D            
17E5: 18 D2           JR      $1208               ; {}
17E7: 36 7E           LD      (HL),$7E            
17E9: 18 CE           JR      $1204               ; {}
17EB: 21 11 84        LD      HL,$8411            
17EE: 06 09           LD      B,$09               
17F0: 36 00           LD      (HL),$00            
17F2: 23              INC     HL                  
17F3: 10 FB           DJNZ    $1231               ; {}
17F5: C9              RET                         
17F6: 3A CF 87        LD      A,($87CF)           
17F9: CB 5F           BIT     3,A                 
17FB: 20 1F           JR      NZ,$1255            ; {}
17FD: 3A 87 87        LD      A,($8787)           
1800: CB 4F           BIT     1,A                 
1802: 20 18           JR      NZ,$124E            ; {}
1804: 21 0D 84        LD      HL,$840D            
1807: 7E              LD      A,(HL)              
1808: FE 00           CP      $00                 
180A: 28 01           JR      Z,$1237             ; {}
180C: 35              DEC     (HL)                
180D: 4E              LD      C,(HL)              
180E: 23              INC     HL                  
180F: 7E              LD      A,(HL)              
1810: FE 00           CP      $00                 
1812: 20 02           JR      NZ,$1238            ; {}
1814: 36 01           LD      (HL),$01            
1816: 23              INC     HL                  
1817: 71              LD      (HL),C              
1818: 23              INC     HL                  
1819: 71              LD      (HL),C              
181A: 18 0F           JR      $1245               ; {}
181C: 21 0D 84        LD      HL,$840D            
181F: 06 04           LD      B,$04               
1821: 36 00           LD      (HL),$00            
1823: 23              INC     HL                  
1824: 10 FB           DJNZ    $1231               ; {}
1826: 3E 01           LD      A,$01               
1828: 32 0E 84        LD      ($840E),A           
182B: 3A 57 86        LD      A,($8657)           
182E: CB 4F           BIT     1,A                 
1830: C8              RET     Z                   
1831: 06 04           LD      B,$04               
1833: 21 0D 84        LD      HL,$840D            
1836: 36 02           LD      (HL),$02            
1838: 23              INC     HL                  
1839: 10 FB           DJNZ    $1231               ; {}
183B: C9              RET                         
183C: 21 09 84        LD      HL,$8409            
183F: 7E              LD      A,(HL)              
1840: C3 62 19        JP      $1962               ; {}
1843: 21 0C 80        LD      HL,$800C            
1846: 11 2C 80        LD      DE,$802C            
1849: 06 14           LD      B,$14               
184B: 3E 0C           LD      A,$0C               
184D: 77              LD      (HL),A              
184E: 32 30 68        LD      ($6830),A           
1851: 12              LD      (DE),A              
1852: 23              INC     HL                  
1853: 13              INC     DE                  
1854: 10 F5           DJNZ    $122B               ; {}
1856: 3A 0C 84        LD      A,($840C)           
1859: FE 00           CP      $00                 
185B: C8              RET     Z                   
185C: FE 0A           CP      $0A                 
185E: 38 02           JR      C,$1238             ; {}
1860: 3E 09           LD      A,$09               
1862: 47              LD      B,A                 
1863: 21 1D 80        LD      HL,$801D            
1866: E5              PUSH    HL                  
1867: CD 70 18        CALL    $1870               ; {}
186A: E1              POP     HL                  
186B: 2B              DEC     HL                  
186C: 2B              DEC     HL                  
186D: 10 F7           DJNZ    $122D               ; {}
186F: C9              RET                         
1870: 11 20 00        LD      DE,$0020            
1873: 3E 7F           LD      A,$7F               
1875: 77              LD      (HL),A              
1876: 2B              DEC     HL                  
1877: 77              LD      (HL),A              
1878: 19              ADD     HL,DE               
1879: 77              LD      (HL),A              
187A: 23              INC     HL                  
187B: 77              LD      (HL),A              
187C: C9              RET                         
187D: 21 A5 84        LD      HL,$84A5            
1880: 06 80           LD      B,$80               
1882: 36 00           LD      (HL),$00            
1884: 23              INC     HL                  
1885: 32 30 68        LD      ($6830),A           
1888: 10 F8           DJNZ    $122E               ; {}
188A: C9              RET                         
188B: 21 25 85        LD      HL,$8525            
188E: 18 F0           JR      $1226               ; {}
1890: 21 25 84        LD      HL,$8425            
1893: 06 08           LD      B,$08               
1895: 3E 00           LD      A,$00               
1897: 77              LD      (HL),A              
1898: 23              INC     HL                  
1899: 36 90           LD      (HL),$90            
189B: CD 62 19        CALL    $1962               ; {}
189E: CD 62 19        CALL    $1962               ; {}
18A1: 23              INC     HL                  
18A2: 10 F1           DJNZ    $1227               ; {}
18A4: C9              RET                         
18A5: 21 65 84        LD      HL,$8465            
18A8: 18 E9           JR      $121F               ; {}
18AA: 21 60 31        LD      HL,$3160            
18AD: CD DC 1B        CALL    $1BDC               ; {}
18B0: 4F              LD      C,A                 
18B1: 87              ADD     A,A                 
18B2: 87              ADD     A,A                 
18B3: 87              ADD     A,A                 
18B4: 87              ADD     A,A                 
18B5: 5F              LD      E,A                 
18B6: 16 00           LD      D,$00               
18B8: 19              ADD     HL,DE               
18B9: 06 08           LD      B,$08               
18BB: E5              PUSH    HL                  
18BC: 5E              LD      E,(HL)              
18BD: 23              INC     HL                  
18BE: 56              LD      D,(HL)              
18BF: 7A              LD      A,D                 
18C0: A7              AND     A                   
18C1: 28 04           JR      Z,$123A             ; {}
18C3: EB              EX      DE,HL               
18C4: CD 26 19        CALL    $1926               ; {}
18C7: E1              POP     HL                  
18C8: 23              INC     HL                  
18C9: 23              INC     HL                  
18CA: 32 30 68        LD      ($6830),A           
18CD: 10 EC           DJNZ    $1222               ; {}
18CF: 21 D0 81        LD      HL,$81D0            
18D2: 3E 02           LD      A,$02               
18D4: 4F              LD      C,A                 
18D5: AF              XOR     A                   
18D6: CD 26 19        CALL    $1926               ; {}
18D9: 3A 57 86        LD      A,($8657)           
18DC: CB 4F           BIT     1,A                 
18DE: 20 12           JR      NZ,$1248            ; {}
18E0: 21 85 87        LD      HL,$8785            
18E3: 3A 00 84        LD      A,($8400)           
18E6: CB 4F           BIT     1,A                 
18E8: 20 05           JR      NZ,$123B            ; {}
18EA: CB 46           BIT     0,(HL)              
18EC: C8              RET     Z                   
18ED: 18 03           JR      $1239               ; {}
18EF: CB 4E           BIT     1,(HL)              
18F1: C8              RET     Z                   
18F2: 21 08 19        LD      HL,$1908            
18F5: 11 02 82        LD      DE,$8202            
18F8: 01 0F 00        LD      BC,$000F            
18FB: C5              PUSH    BC                  
18FC: ED B0           LDIR                        
18FE: C1              POP     BC                  
18FF: 21 17 19        LD      HL,$1917            
1902: 11 22 82        LD      DE,$8222            
1905: ED B0           LDIR                        
1907: C9              RET                         
1908: 8C              ADC     A,H                 
1909: 02              LD      (BC),A              
190A: 02              LD      (BC),A              
190B: 02              LD      (BC),A              
190C: 02              LD      (BC),A              
190D: 02              LD      (BC),A              
190E: 02              LD      (BC),A              
190F: 02              LD      (BC),A              
1910: 02              LD      (BC),A              
1911: 02              LD      (BC),A              
1912: 02              LD      (BC),A              
1913: 02              LD      (BC),A              
1914: 02              LD      (BC),A              
1915: 02              LD      (BC),A              
1916: 0C              INC     C                   
1917: 8C              ADC     A,H                 
1918: 03              INC     BC                  
1919: 03              INC     BC                  
191A: 03              INC     BC                  
191B: 03              INC     BC                  
191C: 03              INC     BC                  
191D: 03              INC     BC                  
191E: 03              INC     BC                  
191F: 03              INC     BC                  
1920: 03              INC     BC                  
1921: 03              INC     BC                  
1922: 03              INC     BC                  
1923: 03              INC     BC                  
1924: 03              INC     BC                  
1925: 0C              INC     C                   
1926: C5              PUSH    BC                  
1927: 78              LD      A,B                 
1928: FE 05           CP      $05                 
192A: DA 69 19        JP      C,$1969             ; {}
192D: E5              PUSH    HL                  
192E: 36 00           LD      (HL),$00            
1930: 3E 02           LD      A,$02               
1932: CD 62 19        CALL    $1962               ; {}
1935: 79              LD      A,C                 
1936: FE 00           CP      $00                 
1938: 20 05           JR      NZ,$123B            ; {}
193A: 3E 02           LD      A,$02               
193C: CD 60 19        CALL    $1960               ; {}
193F: 23              INC     HL                  
1940: 36 02           LD      (HL),$02            
1942: 23              INC     HL                  
1943: 36 04           LD      (HL),$04            
1945: E1              POP     HL                  
1946: 11 20 00        LD      DE,$0020            
1949: 19              ADD     HL,DE               
194A: 36 01           LD      (HL),$01            
194C: 3E 03           LD      A,$03               
194E: CD 60 19        CALL    $1960               ; {}
1951: 79              LD      A,C                 
1952: FE 00           CP      $00                 
1954: 20 05           JR      NZ,$123B            ; {}
1956: 3E 03           LD      A,$03               
1958: CD 60 19        CALL    $1960               ; {}
195B: 23              INC     HL                  
195C: 36 05           LD      (HL),$05            
195E: C1              POP     BC                  
195F: C9              RET                         
1960: 23              INC     HL                  
1961: 77              LD      (HL),A              
1962: 23              INC     HL                  
1963: 77              LD      (HL),A              
1964: 23              INC     HL                  
1965: 77              LD      (HL),A              
1966: 23              INC     HL                  
1967: 77              LD      (HL),A              
1968: C9              RET                         
1969: 11 20 00        LD      DE,$0020            
196C: 36 0A           LD      (HL),$0A            
196E: 23              INC     HL                  
196F: 36 0B           LD      (HL),$0B            
1971: 2B              DEC     HL                  
1972: 79              LD      A,C                 
1973: FE 00           CP      $00                 
1975: 20 06           JR      NZ,$123C            ; {}
1977: CD 91 19        CALL    $1991               ; {}
197A: CD 91 19        CALL    $1991               ; {}
197D: CD 91 19        CALL    $1991               ; {}
1980: CD 91 19        CALL    $1991               ; {}
1983: CD 91 19        CALL    $1991               ; {}
1986: CD 91 19        CALL    $1991               ; {}
1989: 19              ADD     HL,DE               
198A: 36 06           LD      (HL),$06            
198C: 23              INC     HL                  
198D: 36 07           LD      (HL),$07            
198F: C1              POP     BC                  
1990: C9              RET                         
1991: 19              ADD     HL,DE               
1992: 36 08           LD      (HL),$08            
1994: 23              INC     HL                  
1995: 36 09           LD      (HL),$09            
1997: 2B              DEC     HL                  
1998: C9              RET                         
1999: 21 05 9A        LD      HL,$9A05            
199C: 7E              LD      A,(HL)              
199D: 23              INC     HL                  
199E: 77              LD      (HL),A              
199F: 18 22           JR      $1258               ; {}
19A1: 21 00 84        LD      HL,$8400            
19A4: CB 4E           BIT     1,(HL)              
19A6: 20 0C           JR      NZ,$1242            ; {}
19A8: 21 0D 84        LD      HL,$840D            
19AB: 34              INC     (HL)                
19AC: 7E              LD      A,(HL)              
19AD: 23              INC     HL                  
19AE: 23              INC     HL                  
19AF: 77              LD      (HL),A              
19B0: 23              INC     HL                  
19B1: 77              LD      (HL),A              
19B2: 18 07           JR      $123D               ; {}
19B4: 21 0E 84        LD      HL,$840E            
19B7: 34              INC     (HL)                
19B8: 7E              LD      A,(HL)              
19B9: 18 F3           JR      $1229               ; {}
19BB: 3A 57 86        LD      A,($8657)           
19BE: CB 4F           BIT     1,A                 
19C0: 20 D7           JR      NZ,$120D            ; {}
19C2: 2B              DEC     HL                  
19C3: CD 1F 1A        CALL    $1A1F               ; {}
19C6: 7E              LD      A,(HL)              
19C7: E6 0F           AND     $0F                 
19C9: C6 10           ADD     $10                 
19CB: 32 23 80        LD      ($8023),A           
19CE: 7E              LD      A,(HL)              
19CF: 0F              RRCA                        
19D0: 0F              RRCA                        
19D1: 0F              RRCA                        
19D2: 0F              RRCA                        
19D3: E6 0F           AND     $0F                 
19D5: 28 07           JR      Z,$123D             ; {}
19D7: C6 10           ADD     $10                 
19D9: 32 24 80        LD      ($8024),A           
19DC: 18 05           JR      $123B               ; {}
19DE: 3E 7F           LD      A,$7F               
19E0: 32 24 80        LD      ($8024),A           
19E3: 21 08 80        LD      HL,$8008            
19E6: 06 07           LD      B,$07               
19E8: DD 21 60 30     LD      IX,$3060            
19EC: DD 7E 00        LD      A,(IX+$00)          
19EF: 77              LD      (HL),A              
19F0: 2B              DEC     HL                  
19F1: DD 23           INC     IX                  
19F3: 10 F7           DJNZ    $122D               ; {}
19F5: 21 00 84        LD      HL,$8400            
19F8: CB 4E           BIT     1,(HL)              
19FA: 20 0B           JR      NZ,$1241            ; {}
19FC: 21 0D 84        LD      HL,$840D            
19FF: 7E              LD      A,(HL)              
1A00: 23              INC     HL                  
1A01: 23              INC     HL                  
1A02: 77              LD      (HL),A              
1A03: 23              INC     HL                  
1A04: 77              LD      (HL),A              
1A05: 18 08           JR      $123E               ; {}
1A07: 21 0E 84        LD      HL,$840E            
1A0A: 7E              LD      A,(HL)              
1A0B: 23              INC     HL                  
1A0C: 77              LD      (HL),A              
1A0D: 23              INC     HL                  
1A0E: 77              LD      (HL),A              
1A0F: 21 0F 84        LD      HL,$840F            
1A12: 7E              LD      A,(HL)              
1A13: 32 27 86        LD      ($8627),A           
1A16: FE 0F           CP      $0F                 
1A18: D8              RET     C                   
1A19: 3E 0F           LD      A,$0F               
1A1B: 77              LD      (HL),A              
1A1C: 23              INC     HL                  
1A1D: 77              LD      (HL),A              
1A1E: C9              RET                         
1A1F: 11 01 00        LD      DE,$0001            
1A22: 7E              LD      A,(HL)              
1A23: A7              AND     A                   
1A24: 28 0F           JR      Z,$1245             ; {}
1A26: 1F              RRA                         
1A27: 47              LD      B,A                 
1A28: 30 04           JR      NC,$123A            ; {}
1A2A: 7A              LD      A,D                 
1A2B: 83              ADD     A,E                 
1A2C: 27              DAA                         
1A2D: 57              LD      D,A                 
1A2E: 7B              LD      A,E                 
1A2F: 87              ADD     A,A                 
1A30: 27              DAA                         
1A31: 5F              LD      E,A                 
1A32: 78              LD      A,B                 
1A33: 18 EE           JR      $1224               ; {}
1A35: 72              LD      (HL),D              
1A36: C9              RET                         
1A37: 21 50 32        LD      HL,$3250            
1A3A: CD DC 1B        CALL    $1BDC               ; {}
1A3D: 87              ADD     A,A                 
1A3E: 87              ADD     A,A                 
1A3F: 87              ADD     A,A                 
1A40: 5F              LD      E,A                 
1A41: 16 00           LD      D,$00               
1A43: 19              ADD     HL,DE               
1A44: 11 10 00        LD      DE,$0010            
1A47: E5              PUSH    HL                  
1A48: DD E1           POP     IX                  
1A4A: 21 29 85        LD      HL,$8529            
1A4D: 06 08           LD      B,$08               
1A4F: E5              PUSH    HL                  
1A50: DD 7E 00        LD      A,(IX+$00)          
1A53: 4F              LD      C,A                 
1A54: A7              AND     A                   
1A55: 28 10           JR      Z,$1246             ; {}
1A57: 79              LD      A,C                 
1A58: 87              ADD     A,A                 
1A59: 87              ADD     A,A                 
1A5A: 87              ADD     A,A                 
1A5B: 87              ADD     A,A                 
1A5C: 3C              INC     A                   
1A5D: 77              LD      (HL),A              
1A5E: 23              INC     HL                  
1A5F: 79              LD      A,C                 
1A60: DD 23           INC     IX                  
1A62: E6 F0           AND     $F0                 
1A64: 77              LD      (HL),A              
1A65: 18 05           JR      $123B               ; {}
1A67: DD 23           INC     IX                  
1A69: 2B              DEC     HL                  
1A6A: CB FE           SET     7,(HL)              
1A6C: E1              POP     HL                  
1A6D: 19              ADD     HL,DE               
1A6E: 10 DF           DJNZ    $1215               ; {}
1A70: C9              RET                         
1A71: 11 10 00        LD      DE,$0010            
1A74: 21 28 85        LD      HL,$8528            
1A77: 06 08           LD      B,$08               
1A79: E5              PUSH    HL                  
1A7A: CB 7E           BIT     7,(HL)              
1A7C: 28 06           JR      Z,$123C             ; {}
1A7E: 23              INC     HL                  
1A7F: 36 00           LD      (HL),$00            
1A81: 23              INC     HL                  
1A82: 36 00           LD      (HL),$00            
1A84: E1              POP     HL                  
1A85: E5              PUSH    HL                  
1A86: 2B              DEC     HL                  
1A87: 2B              DEC     HL                  
1A88: 2B              DEC     HL                  
1A89: 7E              LD      A,(HL)              
1A8A: E6 01           AND     $01                 
1A8C: 77              LD      (HL),A              
1A8D: E1              POP     HL                  
1A8E: 19              ADD     HL,DE               
1A8F: 10 E8           DJNZ    $121E               ; {}
1A91: C9              RET                         
1A92: 21 2B 85        LD      HL,$852B            
1A95: 11 10 00        LD      DE,$0010            
1A98: 06 08           LD      B,$08               
1A9A: E5              PUSH    HL                  
1A9B: 78              LD      A,B                 
1A9C: FE 05           CP      $05                 
1A9E: 38 07           JR      C,$123D             ; {}
1AA0: 36 20           LD      (HL),$20            
1AA2: 23              INC     HL                  
1AA3: 36 01           LD      (HL),$01            
1AA5: 18 15           JR      $124B               ; {}
1AA7: 22 F6 85        LD      ($85F6),HL          
1AAA: E1              POP     HL                  
1AAB: E5              PUSH    HL                  
1AAC: 2B              DEC     HL                  
1AAD: 2B              DEC     HL                  
1AAE: 2B              DEC     HL                  
1AAF: 2B              DEC     HL                  
1AB0: 2B              DEC     HL                  
1AB1: 2B              DEC     HL                  
1AB2: CB C6           SET     0,(HL)              
1AB4: 2A F6 85        LD      HL,($85F6)          
1AB7: 36 24           LD      (HL),$24            
1AB9: 23              INC     HL                  
1ABA: 36 02           LD      (HL),$02            
1ABC: 23              INC     HL                  
1ABD: 36 00           LD      (HL),$00            
1ABF: E1              POP     HL                  
1AC0: 19              ADD     HL,DE               
1AC1: 10 D7           DJNZ    $120D               ; {}
1AC3: C9              RET                         
1AC4: 21 E8 30        LD      HL,$30E8            
1AC7: CD DC 1B        CALL    $1BDC               ; {}
1ACA: 87              ADD     A,A                 
1ACB: 87              ADD     A,A                 
1ACC: 87              ADD     A,A                 
1ACD: 5F              LD      E,A                 
1ACE: 16 00           LD      D,$00               
1AD0: 19              ADD     HL,DE               
1AD1: E5              PUSH    HL                  
1AD2: DD E1           POP     IX                  
1AD4: 21 67 84        LD      HL,$8467            
1AD7: 11 08 00        LD      DE,$0008            
1ADA: 06 08           LD      B,$08               
1ADC: FD 21 65 84     LD      IY,$8465            
1AE0: FD E5           PUSH    IY                  
1AE2: CB 46           BIT     0,(HL)              
1AE4: 28 10           JR      Z,$1246             ; {}
1AE6: 36 FF           LD      (HL),$FF            
1AE8: FD 36 00 00     LD      (IY+$00),$00        
1AEC: FD 23           INC     IY                  
1AEE: FD 36 00 60     LD      (IY+$00),$60        
1AF2: DD 23           INC     IX                  
1AF4: 18 1A           JR      $1250               ; {}
1AF6: DD 7E 00        LD      A,(IX+$00)          
1AF9: A7              AND     A                   
1AFA: 28 EA           JR      Z,$1220             ; {}
1AFC: 87              ADD     A,A                 
1AFD: 87              ADD     A,A                 
1AFE: 87              ADD     A,A                 
1AFF: 87              ADD     A,A                 
1B00: 3C              INC     A                   
1B01: FD 77 00        LD      (IY+$00),A          
1B04: FD 23           INC     IY                  
1B06: DD 7E 00        LD      A,(IX+$00)          
1B09: E6 F0           AND     $F0                 
1B0B: FD 77 00        LD      (IY+$00),A          
1B0E: DD 23           INC     IX                  
1B10: FD E1           POP     IY                  
1B12: FD 19           ADD     IY,DE               
1B14: 19              ADD     HL,DE               
1B15: 10 C9           DJNZ    $11FF               ; {}
1B17: 21 3C 98        LD      HL,$983C            
1B1A: 11 3C 99        LD      DE,$993C            
1B1D: 06 08           LD      B,$08               
1B1F: 36 1E           LD      (HL),$1E            
1B21: 23              INC     HL                  
1B22: 36 04           LD      (HL),$04            
1B24: 23              INC     HL                  
1B25: AF              XOR     A                   
1B26: 12              LD      (DE),A              
1B27: 13              INC     DE                  
1B28: 13              INC     DE                  
1B29: 10 F4           DJNZ    $122A               ; {}
1B2B: C9              RET                         
1B2C: 3E 02           LD      A,$02               
1B2E: 32 22 98        LD      ($9822),A           
1B31: AF              XOR     A                   
1B32: 32 23 98        LD      ($9823),A           
1B35: 32 80 98        LD      ($9880),A           
1B38: 32 81 98        LD      ($9881),A           
1B3B: 3E 38           LD      A,$38               
1B3D: 32 00 98        LD      ($9800),A           
1B40: 3E 06           LD      A,$06               
1B42: 32 01 98        LD      ($9801),A           
1B45: 3A 57 86        LD      A,($8657)           
1B48: CB 4F           BIT     1,A                 
1B4A: 20 1F           JR      NZ,$1255            ; {}
1B4C: 21 85 87        LD      HL,$8785            
1B4F: 3A 00 84        LD      A,($8400)           
1B52: CB 4F           BIT     1,A                 
1B54: 20 06           JR      NZ,$123C            ; {}
1B56: CB 46           BIT     0,(HL)              
1B58: 20 11           JR      NZ,$1247            ; {}
1B5A: 18 04           JR      $123A               ; {}
1B5C: CB 4E           BIT     1,(HL)              
1B5E: 20 0B           JR      NZ,$1241            ; {}
1B60: 3E 08           LD      A,$08               
1B62: 32 A3 98        LD      ($98A3),A           
1B65: 3E B1           LD      A,$B1               
1B67: 32 A2 98        LD      ($98A2),A           
1B6A: C9              RET                         
1B6B: 3E 71           LD      A,$71               
1B6D: 32 A2 98        LD      ($98A2),A           
1B70: 3E 80           LD      A,$80               
1B72: 32 A3 98        LD      ($98A3),A           
1B75: 21 01 84        LD      HL,$8401            
1B78: CB E6           SET     4,(HL)              
1B7A: C9              RET                         
1B7B: 21 00 84        LD      HL,$8400            
1B7E: CB 4E           BIT     1,(HL)              
1B80: 20 05           JR      NZ,$123B            ; {}
1B82: 21 0A 84        LD      HL,$840A            
1B85: 18 03           JR      $1239               ; {}
1B87: 21 0B 84        LD      HL,$840B            
1B8A: 35              DEC     (HL)                
1B8B: 7E              LD      A,(HL)              
1B8C: 32 0C 84        LD      ($840C),A           
1B8F: C9              RET                         
1B90: 21 65 84        LD      HL,$8465            
1B93: 11 07 00        LD      DE,$0007            
1B96: 06 08           LD      B,$08               
1B98: DD 21 BC 98     LD      IX,$98BC            
1B9C: 7E              LD      A,(HL)              
1B9D: DD 77 00        LD      (IX+$00),A          
1BA0: 23              INC     HL                  
1BA1: DD 23           INC     IX                  
1BA3: 7E              LD      A,(HL)              
1BA4: DD 77 00        LD      (IX+$00),A          
1BA7: DD 23           INC     IX                  
1BA9: 19              ADD     HL,DE               
1BAA: 10 F0           DJNZ    $1226               ; {}
1BAC: C9              RET                         
1BAD: 21 29 85        LD      HL,$8529            
1BB0: 06 08           LD      B,$08               
1BB2: 11 0D 00        LD      DE,$000D            
1BB5: DD 21 64 98     LD      IX,$9864            
1BB9: FD 21 E4 98     LD      IY,$98E4            
1BBD: 7E              LD      A,(HL)              
1BBE: FD 77 00        LD      (IY+$00),A          
1BC1: FD 23           INC     IY                  
1BC3: 23              INC     HL                  
1BC4: 7E              LD      A,(HL)              
1BC5: FD 77 00        LD      (IY+$00),A          
1BC8: 23              INC     HL                  
1BC9: FD 23           INC     IY                  
1BCB: 7E              LD      A,(HL)              
1BCC: DD 77 00        LD      (IX+$00),A          
1BCF: 23              INC     HL                  
1BD0: DD 23           INC     IX                  
1BD2: 7E              LD      A,(HL)              
1BD3: DD 77 00        LD      (IX+$00),A          
1BD6: DD 23           INC     IX                  
1BD8: 19              ADD     HL,DE               
1BD9: 10 E2           DJNZ    $1218               ; {}
1BDB: C9              RET                         
1BDC: 3A 27 86        LD      A,($8627)           
1BDF: FE 10           CP      $10                 
1BE1: 38 04           JR      C,$123A             ; {}
1BE3: E6 03           AND     $03                 
1BE5: C6 0C           ADD     $0C                 
1BE7: 3D              DEC     A                   
1BE8: C9              RET                         
1BE9: 06 00           LD      B,$00               
1BEB: 2A D6 85        LD      HL,($85D6)          
1BEE: CD 8C 1C        CALL    $1C8C               ; {}
1BF1: 2A D8 85        LD      HL,($85D8)          
1BF4: CD 8C 1C        CALL    $1C8C               ; {}
1BF7: 2A DA 85        LD      HL,($85DA)          
1BFA: CD 8C 1C        CALL    $1C8C               ; {}
1BFD: 2A DC 85        LD      HL,($85DC)          
1C00: CD 8C 1C        CALL    $1C8C               ; {}
1C03: 78              LD      A,B                 
1C04: 21 01 84        LD      HL,$8401            
1C07: CB A6           RES     4,(HL)              
1C09: A7              AND     A                   
1C0A: C0              RET     NZ                  
1C0B: CB E6           SET     4,(HL)              
1C0D: C9              RET                         
1C0E: DD 21 FA 85     LD      IX,$85FA            
1C12: 18 23           JR      $1259               ; {}
1C14: DD 21 02 86     LD      IX,$8602            
1C18: 18 1D           JR      $1253               ; {}
1C1A: DD 21 0A 86     LD      IX,$860A            
1C1E: 18 17           JR      $124D               ; {}
1C20: 3A AE 85        LD      A,($85AE)           
1C23: E6 0F           AND     $0F                 
1C25: 28 0C           JR      Z,$1242             ; {}
1C27: FE 06           CP      $06                 
1C29: 28 08           JR      Z,$123E             ; {}
1C2B: 3E 06           LD      A,$06               
1C2D: 82              ADD     A,D                 
1C2E: 57              LD      D,A                 
1C2F: 3E 06           LD      A,$06               
1C31: 83              ADD     A,E                 
1C32: 5F              LD      E,A                 
1C33: DD 21 D6 85     LD      IX,$85D6            
1C37: CD 58 1C        CALL    $1C58               ; {}
1C3A: DD 75 00        LD      (IX+$00),L          
1C3D: DD 74 01        LD      (IX+$01),H          
1C40: CD 85 1C        CALL    $1C85               ; {}
1C43: DD 73 02        LD      (IX+$02),E          
1C46: DD 72 03        LD      (IX+$03),D          
1C49: 23              INC     HL                  
1C4A: DD 75 04        LD      (IX+$04),L          
1C4D: DD 74 05        LD      (IX+$05),H          
1C50: 13              INC     DE                  
1C51: DD 73 06        LD      (IX+$06),E          
1C54: DD 72 07        LD      (IX+$07),D          
1C57: C9              RET                         
1C58: 7A              LD      A,D                 
1C59: D6 11           SUB     $11                 
1C5B: CB 3F           SRL     A                   
1C5D: CB 3F           SRL     A                   
1C5F: 57              LD      D,A                 
1C60: CB 3F           SRL     A                   
1C62: 87              ADD     A,A                 
1C63: 87              ADD     A,A                 
1C64: 87              ADD     A,A                 
1C65: 87              ADD     A,A                 
1C66: 87              ADD     A,A                 
1C67: 6F              LD      L,A                 
1C68: 7A              LD      A,D                 
1C69: CB 3F           SRL     A                   
1C6B: CB 3F           SRL     A                   
1C6D: CB 3F           SRL     A                   
1C6F: CB 3F           SRL     A                   
1C71: 67              LD      H,A                 
1C72: 16 00           LD      D,$00               
1C74: CB 3B           SRL     E                   
1C76: CB 3B           SRL     E                   
1C78: CB 3B           SRL     E                   
1C7A: A7              AND     A                   
1C7B: ED 52           SBC     HL,DE               
1C7D: EB              EX      DE,HL               
1C7E: 21 A0 83        LD      HL,$83A0            
1C81: A7              AND     A                   
1C82: ED 52           SBC     HL,DE               
1C84: C9              RET                         
1C85: 11 E0 FF        LD      DE,$FFE0            
1C88: EB              EX      DE,HL               
1C89: 19              ADD     HL,DE               
1C8A: EB              EX      DE,HL               
1C8B: C9              RET                         
1C8C: 7E              LD      A,(HL)              
1C8D: FE 7F           CP      $7F                 
1C8F: C0              RET     NZ                  
1C90: 04              INC     B                   
1C91: C9              RET                         
1C92: CD 17 13        CALL    $1317               ; {}
1C95: 3A 00 84        LD      A,($8400)           
1C98: CB 4F           BIT     1,A                 
1C9A: 20 05           JR      NZ,$123B            ; {}
1C9C: CD 31 13        CALL    $1331               ; {}
1C9F: 18 03           JR      $1239               ; {}
1CA1: CD 42 13        CALL    $1342               ; {}
1CA4: 21 C5 1C        LD      HL,$1CC5            
1CA7: 11 DE 98        LD      DE,$98DE            
1CAA: 01 06 00        LD      BC,$0006            
1CAD: C5              PUSH    BC                  
1CAE: ED B0           LDIR                        
1CB0: C1              POP     BC                  
1CB1: 21 CB 1C        LD      HL,$1CCB            
1CB4: 11 5E 98        LD      DE,$985E            
1CB7: ED B0           LDIR                        
1CB9: 21 5E 99        LD      HL,$995E            
1CBC: 06 03           LD      B,$03               
1CBE: 36 00           LD      (HL),$00            
1CC0: 23              INC     HL                  
1CC1: 23              INC     HL                  
1CC2: 10 FA           DJNZ    $1230               ; {}
1CC4: C9              RET                         
1CC5: 81              ADD     A,C                 
1CC6: 98              SBC     B                   
1CC7: 71              LD      (HL),C              
1CC8: 98              SBC     B                   
1CC9: 61              LD      H,C                 
1CCA: 98              SBC     B                   
1CCB: 6E              LD      L,(HL)              
1CCC: 0C              INC     C                   
1CCD: 6D              LD      L,L                 
1CCE: 0C              INC     C                   
1CCF: 6C              LD      L,H                 
1CD0: 0C              INC     C                   
1CD1: 21 F0 98        LD      HL,$98F0            
1CD4: 06 10           LD      B,$10               
1CD6: 36 00           LD      (HL),$00            
1CD8: 23              INC     HL                  
1CD9: 10 FB           DJNZ    $1231               ; {}
1CDB: 21 70 98        LD      HL,$9870            
1CDE: 06 10           LD      B,$10               
1CE0: 36 00           LD      (HL),$00            
1CE2: 23              INC     HL                  
1CE3: 10 FB           DJNZ    $1231               ; {}
1CE5: 21 5E 98        LD      HL,$985E            
1CE8: 11 DE 98        LD      DE,$98DE            
1CEB: 06 06           LD      B,$06               
1CED: 3E 00           LD      A,$00               
1CEF: 77              LD      (HL),A              
1CF0: 12              LD      (DE),A              
1CF1: 23              INC     HL                  
1CF2: 13              INC     DE                  
1CF3: 10 F8           DJNZ    $122E               ; {}
1CF5: C9              RET                         
1CF6: E5              PUSH    HL                  
1CF7: D5              PUSH    DE                  
1CF8: F5              PUSH    AF                  
1CF9: 2A F4 85        LD      HL,($85F4)          
1CFC: ED 5B F4 85     LD      DE,($85F4)          
1D00: 29              ADD     HL,HL               
1D01: 29              ADD     HL,HL               
1D02: 19              ADD     HL,DE               
1D03: 23              INC     HL                  
1D04: 22 F4 85        LD      ($85F4),HL          
1D07: F1              POP     AF                  
1D08: D1              POP     DE                  
1D09: E1              POP     HL                  
1D0A: C9              RET                         
1D0B: DD E5           PUSH    IX                  
1D0D: FD E5           PUSH    IY                  
1D0F: E5              PUSH    HL                  
1D10: D5              PUSH    DE                  
1D11: C5              PUSH    BC                  
1D12: F5              PUSH    AF                  
1D13: 21 56 86        LD      HL,$8656            
1D16: CB 56           BIT     2,(HL)              
1D18: 28 1C           JR      Z,$1252             ; {}
1D1A: CB 96           RES     2,(HL)              
1D1C: 21 48 86        LD      HL,$8648            
1D1F: 3A A3 98        LD      A,($98A3)           
1D22: FE 18           CP      $18                 
1D24: D2 2B 1D        JP      NC,$1D2B            ; {}
1D27: 36 00           LD      (HL),$00            
1D29: 18 0B           JR      $1241               ; {}
1D2B: 34              INC     (HL)                
1D2C: 7E              LD      A,(HL)              
1D2D: FE 02           CP      $02                 
1D2F: 20 05           JR      NZ,$123B            ; {}
1D31: 36 00           LD      (HL),$00            
1D33: CD AB 2F        CALL    $2FAB               ; {}
1D36: F1              POP     AF                  
1D37: C1              POP     BC                  
1D38: D1              POP     DE                  
1D39: E1              POP     HL                  
1D3A: FD E1           POP     IY                  
1D3C: DD E1           POP     IX                  
1D3E: C9              RET                         
1D3F: 3A A2 98        LD      A,($98A2)           
1D42: 57              LD      D,A                 
1D43: 3A A3 98        LD      A,($98A3)           
1D46: 5F              LD      E,A                 
1D47: 3A AF 85        LD      A,($85AF)           
1D4A: C3 23 1C        JP      $1C23               ; {}
1D4D: 27              DAA                         
1D4E: 28 2D           JR      Z,$1263             ; {}
1D50: 2D              DEC     L                   
1D51: 2E 1B           LD      L,$1B               
1D53: 0C              INC     C                   
1D54: 29              ADD     HL,HL               
1D55: 26 2E           LD      H,$2E               
1D57: 29              ADD     HL,HL               
1D58: 0C              INC     C                   
1D59: 1D              DEC     E                   
1D5A: 25              DEC     H                   
1D5B: 28 21           JR      Z,$1257             ; {}
1D5D: 0C              INC     C                   
1D5E: 1D              DEC     E                   
1D5F: 27              DAA                         
1D60: 1A              LD      A,(DE)              
1D61: 0C              INC     C                   
1D62: 21 2C 2E        LD      HL,$2E2C            
1D65: 29              ADD     HL,HL               
1D66: 5E              LD      E,(HL)              
1D67: 66              LD      H,(HL)              
1D68: 62              LD      H,D                 
1D69: 6D              LD      L,L                 
1D6A: 35              DEC     (HL)                
1D6B: 10 0C           DJNZ    $1242               ; {}
1D6D: 2C              INC     L                   
1D6E: 2B              DEC     HL                  
1D6F: 1E 2D           LD      E,$2D               
1D71: 27              DAA                         
1D72: 1E 0C           LD      E,$0C               
1D74: 2D              DEC     L                   
1D75: 27              DAA                         
1D76: 2E 28           LD      L,$28               
1D78: 1C              INC     E                   
1D79: 0C              INC     C                   
1D7A: 1E 26           LD      E,$26               
1D7C: 22 2D 27        LD      ($272D),HL          ; {}
1D7F: 28 2D           JR      Z,$1263             ; {}
1D81: 2D              DEC     L                   
1D82: 2E 1B           LD      L,$1B               
1D84: 0C              INC     C                   
1D85: 2D              DEC     L                   
1D86: 2B              DEC     HL                  
1D87: 1A              LD      A,(DE)              
1D88: 2D              DEC     L                   
1D89: 2C              INC     L                   
1D8A: 0C              INC     C                   
1D8B: 21 2C 2E        LD      HL,$2E2C            
1D8E: 29              ADD     HL,HL               
1D8F: 0C              INC     C                   
1D90: 27              DAA                         
1D91: 1E 21           LD      E,$21               
1D93: 2D              DEC     L                   
1D94: 1E 2B           LD      E,$2B               
1D96: 28 1F           JR      Z,$1255             ; {}
1D98: 1E 1B           LD      E,$1B               
1D9A: 0C              INC     C                   
1D9B: 9E              SBC     (HL)                
1D9C: A6              AND     (HL)                
1D9D: 9A              SBC     D                   
1D9E: A0              AND     B                   
1D9F: 0C              INC     C                   
1DA0: 9E              SBC     (HL)                
1DA1: AE              XOR     (HL)                
1DA2: A7              AND     A                   
1DA3: A2              AND     D                   
1DA4: AD              XOR     L                   
1DA5: A7              AND     A                   
1DA6: A8              XOR     B                   
1DA7: 9C              SBC     H                   
1DA8: 0C              INC     C                   
1DA9: A8              XOR     B                   
1DAA: AD              XOR     L                   
1DAB: 0C              INC     C                   
1DAC: 0C              INC     C                   
1DAD: 0C              INC     C                   
1DAE: 0C              INC     C                   
1DAF: 0C              INC     C                   
1DB0: 0C              INC     C                   
1DB1: 0C              INC     C                   
1DB2: 0C              INC     C                   
1DB3: 0C              INC     C                   
1DB4: 0C              INC     C                   
1DB5: 0C              INC     C                   
1DB6: 0C              INC     C                   
1DB7: 0C              INC     C                   
1DB8: 0C              INC     C                   
1DB9: 0C              INC     C                   
1DBA: 0C              INC     C                   
1DBB: 0C              INC     C                   
1DBC: 0C              INC     C                   
1DBD: 0C              INC     C                   
1DBE: 0C              INC     C                   
1DBF: 0C              INC     C                   
1DC0: 1D              DEC     E                   
1DC1: 27              DAA                         
1DC2: 1A              LD      A,(DE)              
1DC3: 0C              INC     C                   
1DC4: 27              DAA                         
1DC5: 22 28 1C        LD      ($1C28),HL          ; {}
1DC8: 0C              INC     C                   
1DC9: 2D              DEC     L                   
1DCA: 2B              DEC     HL                  
1DCB: 1E 2C           LD      E,$2C               
1DCD: 27              DAA                         
1DCE: 22 6C 6B        LD      ($6B6C),HL          
1DD1: 5E              LD      E,(HL)              
1DD2: 72              LD      (HL),D              
1DD3: 5A              LD      E,D                 
1DD4: 65              LD      H,L                 
1DD5: 69              LD      L,C                 
1DD6: 0C              INC     C                   
1DD7: 52              LD      D,D                 
1DD8: 0C              INC     C                   
1DD9: 6B              LD      L,E                 
1DDA: 68              LD      L,B                 
1DDB: 0C              INC     C                   
1DDC: 51              LD      D,C                 
1DDD: 72              LD      (HL),D              
1DDE: 65              LD      H,L                 
1DDF: 67              LD      H,A                 
1DE0: 68              LD      L,B                 
1DE1: 0C              INC     C                   
1DE2: 6B              LD      L,E                 
1DE3: 5E              LD      E,(HL)              
1DE4: 72              LD      (HL),D              
1DE5: 5A              LD      E,D                 
1DE6: 65              LD      H,L                 
1DE7: 69              LD      L,C                 
1DE8: 0C              INC     C                   
1DE9: 51              LD      D,C                 
1DEA: CB 56           BIT     2,(HL)              
1DEC: C2 15 1E        JP      NZ,$1E15            ; {}
1DEF: CB D6           SET     2,(HL)              
1DF1: 26 17           LD      H,$17               
1DF3: 2E 3A           LD      L,$3A               
1DF5: 22 89 87        LD      ($8789),HL          
1DF8: 3E 01           LD      A,$01               
1DFA: 32 03 A0        LD      ($A003),A           
1DFD: CD 8B 18        CALL    $188B               ; {}
1E00: CD A5 18        CALL    $18A5               ; {}
1E03: CD F2 0B        CALL    $0BF2               ; {}
1E06: CD 95 15        CALL    $1595               ; {}
1E09: CD 69 14        CALL    $1469               ; {}
1E0C: CD CA 0B        CALL    $0BCA               ; {}
1E0F: CD DF 0B        CALL    $0BDF               ; {}
1E12: C3 71 0A        JP      $0A71               ; {}
1E15: CD D9 15        CALL    $15D9               ; {}
1E18: 2A 89 87        LD      HL,($8789)          
1E1B: 2C              INC     L                   
1E1C: 7D              LD      A,L                 
1E1D: FE 3C           CP      $3C                 
1E1F: 20 2D           JR      NZ,$1263            ; {}
1E21: 2E 00           LD      L,$00               
1E23: A7              AND     A                   
1E24: 25              DEC     H                   
1E25: 7C              LD      A,H                 
1E26: FE 0F           CP      $0F                 
1E28: 20 02           JR      NZ,$1238            ; {}
1E2A: 26 09           LD      H,$09               
1E2C: 7C              LD      A,H                 
1E2D: FE 40           CP      $40                 
1E2F: 38 08           JR      C,$123E             ; {}
1E31: 21 87 87        LD      HL,$8787            
1E34: CB CE           SET     1,(HL)              
1E36: C3 71 0A        JP      $0A71               ; {}
1E39: E6 0F           AND     $0F                 
1E3B: C6 50           ADD     $50                 
1E3D: 32 D7 81        LD      ($81D7),A           
1E40: 7C              LD      A,H                 
1E41: CB 3F           SRL     A                   
1E43: CB 3F           SRL     A                   
1E45: CB 3F           SRL     A                   
1E47: CB 3F           SRL     A                   
1E49: C6 50           ADD     $50                 
1E4B: 32 F7 81        LD      ($81F7),A           
1E4E: 22 89 87        LD      ($8789),HL          
1E51: 3E 04           LD      A,$04               
1E53: 21 57 82        LD      HL,$8257            
1E56: DD 21 66 1D     LD      IX,$1D66            
1E5A: CD C9 15        CALL    $15C9               ; {}
1E5D: 3E 14           LD      A,$14               
1E5F: 21 D4 80        LD      HL,$80D4            
1E62: DD 21 6A 1D     LD      IX,$1D6A            
1E66: CD C9 15        CALL    $15C9               ; {}
1E69: 3E 06           LD      A,$06               
1E6B: 21 92 82        LD      HL,$8292            
1E6E: DD 21 94 1D     LD      IX,$1D94            
1E72: CD C9 15        CALL    $15C9               ; {}
1E75: 3E 16           LD      A,$16               
1E77: 21 CE 80        LD      HL,$80CE            
1E7A: DD 21 7E 1D     LD      IX,$1D7E            
1E7E: CD C9 15        CALL    $15C9               ; {}
1E81: 3E 19           LD      A,$19               
1E83: 21 6C 80        LD      HL,$806C            
1E86: DD 21 4D 1D     LD      IX,$1D4D            
1E8A: CD C9 15        CALL    $15C9               ; {}
1E8D: 2A 89 87        LD      HL,($8789)          
1E90: 7D              LD      A,L                 
1E91: FE 1E           CP      $1E                 
1E93: 30 06           JR      NC,$123C            ; {}
1E95: DD 21 AD 1D     LD      IX,$1DAD            
1E99: 18 04           JR      $123A               ; {}
1E9B: DD 21 9A 1D     LD      IX,$1D9A            
1E9F: 21 E6 80        LD      HL,$80E6            
1EA2: 3E 13           LD      A,$13               
1EA4: CD C9 15        CALL    $15C9               ; {}
1EA7: 3A A5 85        LD      A,($85A5)           
1EAA: FE 00           CP      $00                 
1EAC: 20 06           JR      NZ,$123C            ; {}
1EAE: CD CA 1E        CALL    $1ECA               ; {}
1EB1: C3 71 0A        JP      $0A71               ; {}
1EB4: FE 01           CP      $01                 
1EB6: 20 09           JR      NZ,$123F            ; {}
1EB8: CD CA 1E        CALL    $1ECA               ; {}
1EBB: CD D7 1E        CALL    $1ED7               ; {}
1EBE: C3 71 0A        JP      $0A71               ; {}
1EC1: CD E4 1E        CALL    $1EE4               ; {}
1EC4: CD F1 1E        CALL    $1EF1               ; {}
1EC7: C3 71 0A        JP      $0A71               ; {}
1ECA: 3E 0F           LD      A,$0F               
1ECC: 21 2A 81        LD      HL,$812A            
1ECF: DD 21 C0 1D     LD      IX,$1DC0            
1ED3: CD C9 15        CALL    $15C9               ; {}
1ED6: C9              RET                         
1ED7: 3E 0D           LD      A,$0D               
1ED9: 21 30 81        LD      HL,$8130            
1EDC: DD 21 DD 1D     LD      IX,$1DDD            
1EE0: CD C9 15        CALL    $15C9               ; {}
1EE3: C9              RET                         
1EE4: 3E 0E           LD      A,$0E               
1EE6: 21 10 81        LD      HL,$8110            
1EE9: DD 21 CF 1D     LD      IX,$1DCF            
1EED: CD C9 15        CALL    $15C9               ; {}
1EF0: C9              RET                         
1EF1: 21 2A 81        LD      HL,$812A            
1EF4: 3E 0F           LD      A,$0F               
1EF6: DD 21 AD 1D     LD      IX,$1DAD            
1EFA: CD C9 15        CALL    $15C9               ; {}
1EFD: C9              RET                         
1EFE: 2A 23 84        LD      HL,($8423)          
1F01: 7D              LD      A,L                 
1F02: E6 03           AND     $03                 
1F04: FE 03           CP      $03                 
1F06: 28 10           JR      Z,$1246             ; {}
1F08: FE 02           CP      $02                 
1F0A: 28 1A           JR      Z,$1250             ; {}
1F0C: FE 01           CP      $01                 
1F0E: 28 24           JR      Z,$125A             ; {}
1F10: 21 6D 84        LD      HL,$846D            
1F13: CD 73 1F        CALL    $1F73               ; {}
1F16: 18 24           JR      $125A               ; {}
1F18: 21 75 84        LD      HL,$8475            
1F1B: CD 73 1F        CALL    $1F73               ; {}
1F1E: 21 7D 84        LD      HL,$847D            
1F21: CD 73 1F        CALL    $1F73               ; {}
1F24: 18 1B           JR      $1251               ; {}
1F26: 21 85 84        LD      HL,$8485            
1F29: CD 73 1F        CALL    $1F73               ; {}
1F2C: 21 8D 84        LD      HL,$848D            
1F2F: CD 73 1F        CALL    $1F73               ; {}
1F32: 18 08           JR      $123E               ; {}
1F34: 21 95 84        LD      HL,$8495            
1F37: CD 73 1F        CALL    $1F73               ; {}
1F3A: 18 05           JR      $123B               ; {}
1F3C: 21 25 85        LD      HL,$8525            
1F3F: 18 03           JR      $1239               ; {}
1F41: 21 65 85        LD      HL,$8565            
1F44: 11 10 00        LD      DE,$0010            
1F47: 06 04           LD      B,$04               
1F49: 78              LD      A,B                 
1F4A: 32 29 86        LD      ($8629),A           
1F4D: C5              PUSH    BC                  
1F4E: D5              PUSH    DE                  
1F4F: E5              PUSH    HL                  
1F50: A7              AND     A                   
1F51: 11 25 85        LD      DE,$8525            
1F54: ED 52           SBC     HL,DE               
1F56: 7D              LD      A,L                 
1F57: CB 3F           SRL     A                   
1F59: CB 3F           SRL     A                   
1F5B: CB 3F           SRL     A                   
1F5D: CB 3F           SRL     A                   
1F5F: 4F              LD      C,A                 
1F60: 3E 08           LD      A,$08               
1F62: A7              AND     A                   
1F63: 91              SUB     C                   
1F64: 32 9D 87        LD      ($879D),A           
1F67: E1              POP     HL                  
1F68: E5              PUSH    HL                  
1F69: CD 32 23        CALL    $2332               ; {}
1F6C: E1              POP     HL                  
1F6D: D1              POP     DE                  
1F6E: C1              POP     BC                  
1F6F: 19              ADD     HL,DE               
1F70: 10 D7           DJNZ    $120D               ; {}
1F72: C9              RET                         
1F73: E5              PUSH    HL                  
1F74: 23              INC     HL                  
1F75: 23              INC     HL                  
1F76: CB 66           BIT     4,(HL)              
1F78: 20 07           JR      NZ,$123D            ; {}
1F7A: CB 7E           BIT     7,(HL)              
1F7C: C2 B5 21        JP      NZ,$21B5            ; {}
1F7F: 18 02           JR      $1238               ; {}
1F81: E1              POP     HL                  
1F82: C9              RET                         
1F83: E1              POP     HL                  
1F84: E5              PUSH    HL                  
1F85: 56              LD      D,(HL)              
1F86: 7A              LD      A,D                 
1F87: A7              AND     A                   
1F88: 28 54           JR      Z,$128A             ; {}
1F8A: 23              INC     HL                  
1F8B: 5E              LD      E,(HL)              
1F8C: 7B              LD      A,E                 
1F8D: FE F0           CP      $F0                 
1F8F: 30 4D           JR      NC,$1283            ; {}
1F91: CD C4 22        CALL    $22C4               ; {}
1F94: 2A EA 85        LD      HL,($85EA)          
1F97: 7E              LD      A,(HL)              
1F98: FE 09           CP      $09                 
1F9A: 28 1E           JR      Z,$1254             ; {}
1F9C: FE 08           CP      $08                 
1F9E: 28 1A           JR      Z,$1250             ; {}
1FA0: FE 0C           CP      $0C                 
1FA2: 28 16           JR      Z,$124C             ; {}
1FA4: FE 03           CP      $03                 
1FA6: 28 12           JR      Z,$1248             ; {}
1FA8: FE 01           CP      $01                 
1FAA: 28 0E           JR      Z,$1244             ; {}
1FAC: FE 05           CP      $05                 
1FAE: 28 0A           JR      Z,$1240             ; {}
1FB0: FE 06           CP      $06                 
1FB2: 28 06           JR      Z,$123C             ; {}
1FB4: FE 07           CP      $07                 
1FB6: 28 02           JR      Z,$1238             ; {}
1FB8: 20 24           JR      NZ,$125A            ; {}
1FBA: 2A EC 85        LD      HL,($85EC)          
1FBD: 7E              LD      A,(HL)              
1FBE: FE 09           CP      $09                 
1FC0: 28 24           JR      Z,$125A             ; {}
1FC2: FE 08           CP      $08                 
1FC4: 28 20           JR      Z,$1256             ; {}
1FC6: FE 0C           CP      $0C                 
1FC8: 28 1C           JR      Z,$1252             ; {}
1FCA: FE 02           CP      $02                 
1FCC: 28 18           JR      Z,$124E             ; {}
1FCE: FE 00           CP      $00                 
1FD0: 28 14           JR      Z,$124A             ; {}
1FD2: FE 04           CP      $04                 
1FD4: 28 10           JR      Z,$1246             ; {}
1FD6: FE 0A           CP      $0A                 
1FD8: 28 0C           JR      Z,$1242             ; {}
1FDA: FE 0B           CP      $0B                 
1FDC: 28 08           JR      Z,$123E             ; {}
1FDE: E1              POP     HL                  
1FDF: E5              PUSH    HL                  
1FE0: 23              INC     HL                  
1FE1: 23              INC     HL                  
1FE2: CB 8E           RES     1,(HL)              
1FE4: 18 0D           JR      $1243               ; {}
1FE6: 21 F0 87        LD      HL,$87F0            
1FE9: CB CE           SET     1,(HL)              
1FEB: E1              POP     HL                  
1FEC: E5              PUSH    HL                  
1FED: 23              INC     HL                  
1FEE: 23              INC     HL                  
1FEF: CB C6           SET     0,(HL)              
1FF1: CB CE           SET     1,(HL)              
1FF3: CB 46           BIT     0,(HL)              
1FF5: 20 02           JR      NZ,$1238            ; {}
1FF7: E1              POP     HL                  
1FF8: C9              RET                         
1FF9: CB 4E           BIT     1,(HL)              
1FFB: CA B5 21        JP      Z,$21B5             ; {}
1FFE: CB 56           BIT     2,(HL)              
2000: 20 0A           JR      NZ,$1240            ; {}
2002: 23              INC     HL                  
2003: 23              INC     HL                  
2004: 36 0C           LD      (HL),$0C            
2006: 2B              DEC     HL                  
2007: 2B              DEC     HL                  
2008: CB D6           SET     2,(HL)              
200A: E1              POP     HL                  
200B: C9              RET                         
200C: 23              INC     HL                  
200D: 23              INC     HL                  
200E: 7E              LD      A,(HL)              
200F: FE 0C           CP      $0C                 
2011: 28 2B           JR      Z,$1261             ; {}
2013: FE 09           CP      $09                 
2015: 28 32           JR      Z,$1268             ; {}
2017: FE 06           CP      $06                 
2019: 28 23           JR      Z,$1259             ; {}
201B: FE 03           CP      $03                 
201D: 28 2A           JR      Z,$1260             ; {}
201F: FE 0A           CP      $0A                 
2021: 38 02           JR      C,$1238             ; {}
2023: 18 2D           JR      $1263               ; {}
2025: F5              PUSH    AF                  
2026: E5              PUSH    HL                  
2027: 21 33 85        LD      HL,$8533            
202A: 06 08           LD      B,$08               
202C: 11 10 00        LD      DE,$0010            
202F: 7E              LD      A,(HL)              
2030: E6 07           AND     $07                 
2032: 20 03           JR      NZ,$1239            ; {}
2034: C6 04           ADD     $04                 
2036: 77              LD      (HL),A              
2037: 19              ADD     HL,DE               
2038: 10 F5           DJNZ    $122B               ; {}
203A: E1              POP     HL                  
203B: F1              POP     AF                  
203C: 18 14           JR      $124A               ; {}
203E: E5              PUSH    HL                  
203F: F5              PUSH    AF                  
2040: CD 05 29        CALL    $2905               ; {}
2043: 36 1F           LD      (HL),$1F            
2045: F1              POP     AF                  
2046: E1              POP     HL                  
2047: 18 09           JR      $123F               ; {}
2049: E5              PUSH    HL                  
204A: F5              PUSH    AF                  
204B: CD 05 29        CALL    $2905               ; {}
204E: 36 1E           LD      (HL),$1E            
2050: F1              POP     AF                  
2051: E1              POP     HL                  
2052: A7              AND     A                   
2053: 28 0C           JR      Z,$1242             ; {}
2055: FE 01           CP      $01                 
2057: 20 05           JR      NZ,$123B            ; {}
2059: 3E 01           LD      A,$01               
205B: 32 8D 9A        LD      ($9A8D),A           
205E: 35              DEC     (HL)                
205F: E1              POP     HL                  
2060: C9              RET                         
2061: DD E1           POP     IX                  
2063: DD E5           PUSH    IX                  
2065: 3A 46 86        LD      A,($8646)           
2068: CB 47           BIT     0,A                 
206A: C2 A7 20        JP      NZ,$20A7            ; {}
206D: 21 A2 98        LD      HL,$98A2            
2070: DD 7E 00        LD      A,(IX+$00)          
2073: BE              CP      (HL)                
2074: 30 05           JR      NC,$123B            ; {}
2076: 4F              LD      C,A                 
2077: 7E              LD      A,(HL)              
2078: 91              SUB     C                   
2079: 18 01           JR      $1237               ; {}
207B: 96              SUB     (HL)                
207C: FE 07           CP      $07                 
207E: D2 B4 20        JP      NC,$20B4            ; {}
2081: 23              INC     HL                  
2082: DD 4E 01        LD      C,(IX+$01)          
2085: 7E              LD      A,(HL)              
2086: 91              SUB     C                   
2087: FE 12           CP      $12                 
2089: 30 29           JR      NC,$125F            ; {}
208B: AF              XOR     A                   
208C: 32 22 99        LD      ($9922),A           
208F: 21 46 86        LD      HL,$8646            
2092: CB C6           SET     0,(HL)              
2094: 3E 01           LD      A,$01               
2096: 32 8A 9A        LD      ($9A8A),A           
2099: DD 36 03 FF     LD      (IX+$03),$FF        
209D: 3A A3 98        LD      A,($98A3)           
20A0: D6 02           SUB     $02                 
20A2: 32 A3 98        LD      ($98A3),A           
20A5: 18 0D           JR      $1243               ; {}
20A7: 21 A3 98        LD      HL,$98A3            
20AA: 7E              LD      A,(HL)              
20AB: C6 08           ADD     $08                 
20AD: 77              LD      (HL),A              
20AE: FE EE           CP      $EE                 
20B0: 38 02           JR      C,$1238             ; {}
20B2: 36 EE           LD      (HL),$EE            
20B4: 21 25 85        LD      HL,$8525            
20B7: 22 F6 85        LD      ($85F6),HL          
20BA: 11 04 00        LD      DE,$0004            
20BD: 19              ADD     HL,DE               
20BE: 22 1A 86        LD      ($861A),HL          
20C1: 11 10 00        LD      DE,$0010            
20C4: 06 08           LD      B,$08               
20C6: 2A F6 85        LD      HL,($85F6)          
20C9: CB 7E           BIT     7,(HL)              
20CB: C2 94 21        JP      NZ,$2194            ; {}
20CE: D5              PUSH    DE                  
20CF: 11 06 00        LD      DE,$0006            
20D2: 19              ADD     HL,DE               
20D3: D1              POP     DE                  
20D4: 7E              LD      A,(HL)              
20D5: FE 3F           CP      $3F                 
20D7: 38 49           JR      C,$127F             ; {}
20D9: 2A 1A 86        LD      HL,($861A)          
20DC: 3A 00 84        LD      A,($8400)           
20DF: CB 4F           BIT     1,A                 
20E1: 28 04           JR      Z,$123A             ; {}
20E3: CB 57           BIT     2,A                 
20E5: 20 03           JR      NZ,$1239            ; {}
20E7: 7E              LD      A,(HL)              
20E8: 18 03           JR      $1239               ; {}
20EA: 7E              LD      A,(HL)              
20EB: D6 10           SUB     $10                 
20ED: 4F              LD      C,A                 
20EE: DD 7E 00        LD      A,(IX+$00)          
20F1: B9              CP      C                   
20F2: 30 0C           JR      NC,$1242            ; {}
20F4: 79              LD      A,C                 
20F5: DD 4E 00        LD      C,(IX+$00)          
20F8: 91              SUB     C                   
20F9: FE 09           CP      $09                 
20FB: D2 9C 21        JP      NC,$219C            ; {}
20FE: 18 06           JR      $123C               ; {}
2100: 91              SUB     C                   
2101: FE 19           CP      $19                 
2103: D2 9C 21        JP      NC,$219C            ; {}
2106: 23              INC     HL                  
2107: DD 4E 01        LD      C,(IX+$01)          
210A: 3A 00 84        LD      A,($8400)           
210D: CB 4F           BIT     1,A                 
210F: 28 04           JR      Z,$123A             ; {}
2111: CB 57           BIT     2,A                 
2113: 20 03           JR      NZ,$1239            ; {}
2115: 7E              LD      A,(HL)              
2116: 18 03           JR      $1239               ; {}
2118: 7E              LD      A,(HL)              
2119: D6 10           SUB     $10                 
211B: 91              SUB     C                   
211C: FE 0C           CP      $0C                 
211E: 30 7C           JR      NC,$12B2            ; {}
2120: 18 1F           JR      $1255               ; {}
2122: 2A 1A 86        LD      HL,($861A)          
2125: DD 7E 00        LD      A,(IX+$00)          
2128: BE              CP      (HL)                
2129: 30 05           JR      NC,$123B            ; {}
212B: 4F              LD      C,A                 
212C: 7E              LD      A,(HL)              
212D: 91              SUB     C                   
212E: 18 01           JR      $1237               ; {}
2130: 96              SUB     (HL)                
2131: FE 0C           CP      $0C                 
2133: 30 67           JR      NC,$129D            ; {}
2135: 23              INC     HL                  
2136: DD 4E 01        LD      C,(IX+$01)          
2139: 7E              LD      A,(HL)              
213A: 91              SUB     C                   
213B: FE 0C           CP      $0C                 
213D: 30 5D           JR      NC,$1293            ; {}
213F: 18 28           JR      $125E               ; {}
2141: DD 7E 01        LD      A,(IX+$01)          
2144: C6 08           ADD     $08                 
2146: 2A 1A 86        LD      HL,($861A)          
2149: 23              INC     HL                  
214A: 77              LD      (HL),A              
214B: 2B              DEC     HL                  
214C: 3A 00 84        LD      A,($8400)           
214F: CB 4F           BIT     1,A                 
2151: 28 0A           JR      Z,$1240             ; {}
2153: CB 57           BIT     2,A                 
2155: 28 06           JR      Z,$123C             ; {}
2157: 7E              LD      A,(HL)              
2158: D6 08           SUB     $08                 
215A: 77              LD      (HL),A              
215B: 18 04           JR      $123A               ; {}
215D: 7E              LD      A,(HL)              
215E: C6 08           ADD     $08                 
2160: 77              LD      (HL),A              
2161: D5              PUSH    DE                  
2162: 2A F6 85        LD      HL,($85F6)          
2165: CD F1 26        CALL    $26F1               ; {}
2168: D1              POP     DE                  
2169: 2A F6 85        LD      HL,($85F6)          
216C: 3E C3           LD      A,$C3               
216E: A6              AND     (HL)                
216F: 77              LD      (HL),A              
2170: CB FE           SET     7,(HL)              
2172: D5              PUSH    DE                  
2173: 11 0D 00        LD      DE,$000D            
2176: 19              ADD     HL,DE               
2177: D1              POP     DE                  
2178: CB 9E           RES     3,(HL)              
217A: CB 96           RES     2,(HL)              
217C: 3E 01           LD      A,$01               
217E: 32 8A 9A        LD      ($9A8A),A           
2181: 21 C5 87        LD      HL,$87C5            
2184: CB C6           SET     0,(HL)              
2186: DD 36 03 FF     LD      (IX+$03),$FF        
218A: 2A 1A 86        LD      HL,($861A)          
218D: 23              INC     HL                  
218E: 7E              LD      A,(HL)              
218F: D6 02           SUB     $02                 
2191: 77              LD      (HL),A              
2192: 18 08           JR      $123E               ; {}
2194: 2A 1A 86        LD      HL,($861A)          
2197: 23              INC     HL                  
2198: 7E              LD      A,(HL)              
2199: C6 08           ADD     $08                 
219B: 77              LD      (HL),A              
219C: 2A F6 85        LD      HL,($85F6)          
219F: 19              ADD     HL,DE               
21A0: 22 F6 85        LD      ($85F6),HL          
21A3: 2A 1A 86        LD      HL,($861A)          
21A6: 19              ADD     HL,DE               
21A7: 22 1A 86        LD      ($861A),HL          
21AA: 05              DEC     B                   
21AB: C2 C6 20        JP      NZ,$20C6            ; {}
21AE: E1              POP     HL                  
21AF: 23              INC     HL                  
21B0: 3E 08           LD      A,$08               
21B2: 86              ADD     A,(HL)              
21B3: 77              LD      (HL),A              
21B4: C9              RET                         
21B5: CB 5E           BIT     3,(HL)              
21B7: C2 64 22        JP      NZ,$2264            ; {}
21BA: CB DE           SET     3,(HL)              
21BC: CB FE           SET     7,(HL)              
21BE: 23              INC     HL                  
21BF: 23              INC     HL                  
21C0: 36 14           LD      (HL),$14            
21C2: E1              POP     HL                  
21C3: 11 03 00        LD      DE,$0003            
21C6: 19              ADD     HL,DE               
21C7: CB 46           BIT     0,(HL)              
21C9: 28 0D           JR      Z,$1243             ; {}
21CB: 2B              DEC     HL                  
21CC: 2B              DEC     HL                  
21CD: 3A 46 86        LD      A,($8646)           
21D0: CB 47           BIT     0,A                 
21D2: 20 04           JR      NZ,$123A            ; {}
21D4: 7E              LD      A,(HL)              
21D5: D6 08           SUB     $08                 
21D7: 77              LD      (HL),A              
21D8: 3E 01           LD      A,$01               
21DA: 32 8C 9A        LD      ($9A8C),A           
21DD: C9              RET                         
21DE: 21 C5 87        LD      HL,$87C5            
21E1: 36 00           LD      (HL),$00            
21E3: 21 25 85        LD      HL,$8525            
21E6: 11 10 00        LD      DE,$0010            
21E9: 0E 00           LD      C,$00               
21EB: 06 08           LD      B,$08               
21ED: 22 F6 85        LD      ($85F6),HL          
21F0: CB 7E           BIT     7,(HL)              
21F2: 28 0E           JR      Z,$1244             ; {}
21F4: 0C              INC     C                   
21F5: 36 00           LD      (HL),$00            
21F7: 23              INC     HL                  
21F8: 23              INC     HL                  
21F9: 23              INC     HL                  
21FA: CB FE           SET     7,(HL)              
21FC: 23              INC     HL                  
21FD: 36 00           LD      (HL),$00            
21FF: 23              INC     HL                  
2200: 36 00           LD      (HL),$00            
2202: 2A F6 85        LD      HL,($85F6)          
2205: 19              ADD     HL,DE               
2206: 22 F6 85        LD      ($85F6),HL          
2209: 10 E2           DJNZ    $1218               ; {}
220B: 21 47 86        LD      HL,$8647            
220E: 36 3C           LD      (HL),$3C            
2210: 21 1C 86        LD      HL,$861C            
2213: 36 C8           LD      (HL),$C8            
2215: 21 46 86        LD      HL,$8646            
2218: CB 46           BIT     0,(HL)              
221A: 28 02           JR      Z,$1238             ; {}
221C: CB CE           SET     1,(HL)              
221E: 79              LD      A,C                 
221F: A7              AND     A                   
2220: CA 62 22        JP      Z,$2262             ; {}
2223: 06 3E           LD      B,$3E               
2225: 80              ADD     A,B                 
2226: 32 74 98        LD      ($9874),A           
2229: 3E 47           LD      A,$47               
222B: 32 78 98        LD      ($9878),A           
222E: 3E 0A           LD      A,$0A               
2230: 32 75 98        LD      ($9875),A           
2233: 32 79 98        LD      ($9879),A           
2236: AF              XOR     A                   
2237: 32 74 99        LD      ($9974),A           
223A: 32 78 99        LD      ($9978),A           
223D: E1              POP     HL                  
223E: E5              PUSH    HL                  
223F: 7E              LD      A,(HL)              
2240: D6 08           SUB     $08                 
2242: 32 F4 98        LD      ($98F4),A           
2245: C6 10           ADD     $10                 
2247: 32 F8 98        LD      ($98F8),A           
224A: 36 00           LD      (HL),$00            
224C: 23              INC     HL                  
224D: 7E              LD      A,(HL)              
224E: 32 F5 98        LD      ($98F5),A           
2251: 32 F9 98        LD      ($98F9),A           
2254: 36 00           LD      (HL),$00            
2256: E1              POP     HL                  
2257: 79              LD      A,C                 
2258: 87              ADD     A,A                 
2259: C8              RET     Z                   
225A: 81              ADD     A,C                 
225B: C6 15           ADD     $15                 
225D: 6F              LD      L,A                 
225E: CD AD 2F        CALL    $2FAD               ; {}
2261: C9              RET                         
2262: E1              POP     HL                  
2263: C9              RET                         
2264: 23              INC     HL                  
2265: 23              INC     HL                  
2266: 7E              LD      A,(HL)              
2267: A7              AND     A                   
2268: 28 35           JR      Z,$126B             ; {}
226A: 35              DEC     (HL)                
226B: FE 04           CP      $04                 
226D: CA DE 21        JP      Z,$21DE             ; {}
2270: E5              PUSH    HL                  
2271: 21 C5 87        LD      HL,$87C5            
2274: CB 46           BIT     0,(HL)              
2276: 28 03           JR      Z,$1239             ; {}
2278: E1              POP     HL                  
2279: E1              POP     HL                  
227A: C9              RET                         
227B: E1              POP     HL                  
227C: FE 12           CP      $12                 
227E: 28 0A           JR      Z,$1240             ; {}
2280: FE 09           CP      $09                 
2282: 28 0D           JR      Z,$1243             ; {}
2284: FE 05           CP      $05                 
2286: 28 10           JR      Z,$1246             ; {}
2288: E1              POP     HL                  
2289: C9              RET                         
228A: CD 05 29        CALL    $2905               ; {}
228D: 36 74           LD      (HL),$74            
228F: E1              POP     HL                  
2290: C9              RET                         
2291: CD 05 29        CALL    $2905               ; {}
2294: 36 75           LD      (HL),$75            
2296: E1              POP     HL                  
2297: C9              RET                         
2298: CD 05 29        CALL    $2905               ; {}
229B: 36 32           LD      (HL),$32            
229D: E1              POP     HL                  
229E: C9              RET                         
229F: E1              POP     HL                  
22A0: AF              XOR     A                   
22A1: 77              LD      (HL),A              
22A2: 23              INC     HL                  
22A3: 36 90           LD      (HL),$90            
22A5: 23              INC     HL                  
22A6: 36 11           LD      (HL),$11            
22A8: CD 60 19        CALL    $1960               ; {}
22AB: 23              INC     HL                  
22AC: 77              LD      (HL),A              
22AD: 32 F4 98        LD      ($98F4),A           
22B0: 32 F5 98        LD      ($98F5),A           
22B3: 32 F8 98        LD      ($98F8),A           
22B6: 32 F9 98        LD      ($98F9),A           
22B9: 21 99 87        LD      HL,$8799            
22BC: CB C6           SET     0,(HL)              
22BE: 21 F0 87        LD      HL,$87F0            
22C1: CB 8E           RES     1,(HL)              
22C3: C9              RET                         
22C4: C5              PUSH    BC                  
22C5: E5              PUSH    HL                  
22C6: D5              PUSH    DE                  
22C7: CD 0E 1C        CALL    $1C0E               ; {}
22CA: 2A FE 85        LD      HL,($85FE)          
22CD: 23              INC     HL                  
22CE: 22 EA 85        LD      ($85EA),HL          
22D1: 2A 00 86        LD      HL,($8600)          
22D4: 23              INC     HL                  
22D5: 22 EC 85        LD      ($85EC),HL          
22D8: 2A EA 85        LD      HL,($85EA)          
22DB: 7E              LD      A,(HL)              
22DC: FE 7F           CP      $7F                 
22DE: 28 14           JR      Z,$124A             ; {}
22E0: 2A EC 85        LD      HL,($85EC)          
22E3: 7E              LD      A,(HL)              
22E4: FE 7F           CP      $7F                 
22E6: 28 0C           JR      Z,$1242             ; {}
22E8: 2A FE 85        LD      HL,($85FE)          
22EB: CD F8 22        CALL    $22F8               ; {}
22EE: 2A 00 86        LD      HL,($8600)          
22F1: CD F8 22        CALL    $22F8               ; {}
22F4: D1              POP     DE                  
22F5: E1              POP     HL                  
22F6: C1              POP     BC                  
22F7: C9              RET                         
22F8: E5              PUSH    HL                  
22F9: 2B              DEC     HL                  
22FA: 7E              LD      A,(HL)              
22FB: FE 7F           CP      $7F                 
22FD: 20 02           JR      NZ,$1238            ; {}
22FF: E1              POP     HL                  
2300: C9              RET                         
2301: 23              INC     HL                  
2302: 7E              LD      A,(HL)              
2303: FE 00           CP      $00                 
2305: 28 1F           JR      Z,$1255             ; {}
2307: 3D              DEC     A                   
2308: 28 20           JR      Z,$1256             ; {}
230A: 3D              DEC     A                   
230B: 3D              DEC     A                   
230C: 3D              DEC     A                   
230D: 28 17           JR      Z,$124D             ; {}
230F: 3D              DEC     A                   
2310: 28 18           JR      Z,$124E             ; {}
2312: 3D              DEC     A                   
2313: 28 15           JR      Z,$124B             ; {}
2315: 3D              DEC     A                   
2316: 28 12           JR      Z,$1248             ; {}
2318: 3D              DEC     A                   
2319: 28 13           JR      Z,$1249             ; {}
231B: 3D              DEC     A                   
231C: 28 10           JR      Z,$1246             ; {}
231E: 3D              DEC     A                   
231F: 28 05           JR      Z,$123B             ; {}
2321: 3D              DEC     A                   
2322: 28 02           JR      Z,$1238             ; {}
2324: E1              POP     HL                  
2325: C9              RET                         
2326: 36 02           LD      (HL),$02            
2328: E1              POP     HL                  
2329: C9              RET                         
232A: 36 03           LD      (HL),$03            
232C: E1              POP     HL                  
232D: C9              RET                         
232E: 36 0C           LD      (HL),$0C            
2330: E1              POP     HL                  
2331: C9              RET                         
2332: E5              PUSH    HL                  
2333: CD 87 26        CALL    $2687               ; {}
2336: E1              POP     HL                  
2337: 3A 01 84        LD      A,($8401)           
233A: CB 7F           BIT     7,A                 
233C: C0              RET     NZ                  
233D: CD 41 23        CALL    $2341               ; {}
2340: C9              RET                         
2341: E5              PUSH    HL                  
2342: 7E              LD      A,(HL)              
2343: E6 BC           AND     $BC                 
2345: C2 2A 25        JP      NZ,$252A            ; {}
2348: CB 4E           BIT     1,(HL)              
234A: CA 2A 29        JP      Z,$292A             ; {}
234D: 22 F6 85        LD      ($85F6),HL          
2350: 11 0B 00        LD      DE,$000B            
2353: 19              ADD     HL,DE               
2354: 7E              LD      A,(HL)              
2355: A7              AND     A                   
2356: 28 0E           JR      Z,$1244             ; {}
2358: FE 01           CP      $01                 
235A: 20 09           JR      NZ,$123F            ; {}
235C: ED 5B F6 85     LD      DE,($85F6)          
2360: EB              EX      DE,HL               
2361: 23              INC     HL                  
2362: CB 86           RES     0,(HL)              
2364: EB              EX      DE,HL               
2365: 35              DEC     (HL)                
2366: 2A F6 85        LD      HL,($85F6)          
2369: 23              INC     HL                  
236A: 23              INC     HL                  
236B: 23              INC     HL                  
236C: CB 7E           BIT     7,(HL)              
236E: 28 02           JR      Z,$1238             ; {}
2370: E1              POP     HL                  
2371: C9              RET                         
2372: 3A BD 87        LD      A,($87BD)           
2375: 47              LD      B,A                 
2376: 2A F6 85        LD      HL,($85F6)          
2379: 11 09 00        LD      DE,$0009            
237C: 19              ADD     HL,DE               
237D: 7E              LD      A,(HL)              
237E: 90              SUB     B                   
237F: 77              LD      (HL),A              
2380: 38 02           JR      C,$1238             ; {}
2382: E1              POP     HL                  
2383: C9              RET                         
2384: 2A F6 85        LD      HL,($85F6)          
2387: 11 04 00        LD      DE,$0004            
238A: 19              ADD     HL,DE               
238B: 7E              LD      A,(HL)              
238C: FE 01           CP      $01                 
238E: 20 05           JR      NZ,$123B            ; {}
2390: 2B              DEC     HL                  
2391: CB FE           SET     7,(HL)              
2393: E1              POP     HL                  
2394: C9              RET                         
2395: CD F6 1C        CALL    $1CF6               ; {}
2398: 2A F6 85        LD      HL,($85F6)          
239B: 23              INC     HL                  
239C: CB 8E           RES     1,(HL)              
239E: 2B              DEC     HL                  
239F: 11 04 00        LD      DE,$0004            
23A2: 19              ADD     HL,DE               
23A3: 46              LD      B,(HL)              
23A4: 23              INC     HL                  
23A5: 4E              LD      C,(HL)              
23A6: 2A F6 85        LD      HL,($85F6)          
23A9: 23              INC     HL                  
23AA: 23              INC     HL                  
23AB: 23              INC     HL                  
23AC: CB 76           BIT     6,(HL)              
23AE: C2 FB 23        JP      NZ,$23FB            ; {}
23B1: 3A F0 87        LD      A,($87F0)           
23B4: CB 47           BIT     0,A                 
23B6: C2 FB 23        JP      NZ,$23FB            ; {}
23B9: 3A A2 98        LD      A,($98A2)           
23BC: B8              CP      B                   
23BD: DA C3 23        JP      C,$23C3             ; {}
23C0: 90              SUB     B                   
23C1: 18 06           JR      $123C               ; {}
23C3: 3A A2 98        LD      A,($98A2)           
23C6: 57              LD      D,A                 
23C7: 78              LD      A,B                 
23C8: 92              SUB     D                   
23C9: FE 20           CP      $20                 
23CB: D2 FB 23        JP      NC,$23FB            ; {}
23CE: 3A A3 98        LD      A,($98A3)           
23D1: B9              CP      C                   
23D2: DA D8 23        JP      C,$23D8             ; {}
23D5: 91              SUB     C                   
23D6: 18 06           JR      $123C               ; {}
23D8: 3A A3 98        LD      A,($98A3)           
23DB: 57              LD      D,A                 
23DC: 79              LD      A,C                 
23DD: 92              SUB     D                   
23DE: FE 20           CP      $20                 
23E0: D2 FB 23        JP      NC,$23FB            ; {}
23E3: 2A F6 85        LD      HL,($85F6)          
23E6: 11 0F 00        LD      DE,$000F            
23E9: 19              ADD     HL,DE               
23EA: 3A A3 98        LD      A,($98A3)           
23ED: 77              LD      (HL),A              
23EE: 2B              DEC     HL                  
23EF: 3A A2 98        LD      A,($98A2)           
23F2: 77              LD      (HL),A              
23F3: 2A F6 85        LD      HL,($85F6)          
23F6: 23              INC     HL                  
23F7: 23              INC     HL                  
23F8: 23              INC     HL                  
23F9: CB F6           SET     6,(HL)              
23FB: 3A F4 85        LD      A,($85F4)           
23FE: CB 4F           BIT     1,A                 
2400: 28 4A           JR      Z,$1280             ; {}
2402: 2A F6 85        LD      HL,($85F6)          
2405: 23              INC     HL                  
2406: 23              INC     HL                  
2407: 23              INC     HL                  
2408: CB 76           BIT     6,(HL)              
240A: 28 0E           JR      Z,$1244             ; {}
240C: 3A F0 87        LD      A,($87F0)           
240F: CB 47           BIT     0,A                 
2411: 20 07           JR      NZ,$123D            ; {}
2413: 11 0C 00        LD      DE,$000C            
2416: 19              ADD     HL,DE               
2417: 7E              LD      A,(HL)              
2418: 18 0E           JR      $1244               ; {}
241A: 3A F0 87        LD      A,($87F0)           
241D: CB 47           BIT     0,A                 
241F: 28 04           JR      Z,$123A             ; {}
2421: 3E 08           LD      A,$08               
2423: 18 03           JR      $1239               ; {}
2425: 3A A3 98        LD      A,($98A3)           
2428: B9              CP      C                   
2429: DA 43 24        JP      C,$2443             ; {}
242C: CA 89 24        JP      Z,$2489             ; {}
242F: CD 38 24        CALL    $2438               ; {}
2432: 19              ADD     HL,DE               
2433: 34              INC     (HL)                
2434: 34              INC     (HL)                
2435: C3 89 24        JP      $2489               ; {}
2438: 2A F6 85        LD      HL,($85F6)          
243B: 23              INC     HL                  
243C: CB CE           SET     1,(HL)              
243E: 2B              DEC     HL                  
243F: 11 05 00        LD      DE,$0005            
2442: C9              RET                         
2443: CD 38 24        CALL    $2438               ; {}
2446: 19              ADD     HL,DE               
2447: 35              DEC     (HL)                
2448: 35              DEC     (HL)                
2449: C3 89 24        JP      $2489               ; {}
244C: 2A F6 85        LD      HL,($85F6)          
244F: 23              INC     HL                  
2450: 23              INC     HL                  
2451: 23              INC     HL                  
2452: CB 76           BIT     6,(HL)              
2454: 28 0E           JR      Z,$1244             ; {}
2456: 3A F0 87        LD      A,($87F0)           
2459: CB 47           BIT     0,A                 
245B: 20 07           JR      NZ,$123D            ; {}
245D: 11 0B 00        LD      DE,$000B            
2460: 19              ADD     HL,DE               
2461: 7E              LD      A,(HL)              
2462: 18 0E           JR      $1244               ; {}
2464: 3A F0 87        LD      A,($87F0)           
2467: CB 47           BIT     0,A                 
2469: 28 04           JR      Z,$123A             ; {}
246B: 3E 21           LD      A,$21               
246D: 18 03           JR      $1239               ; {}
246F: 3A A2 98        LD      A,($98A2)           
2472: B8              CP      B                   
2473: DA 81 24        JP      C,$2481             ; {}
2476: CA 89 24        JP      Z,$2489             ; {}
2479: 2A F6 85        LD      HL,($85F6)          
247C: 11 04 00        LD      DE,$0004            
247F: 18 B1           JR      $11E7               ; {}
2481: 2A F6 85        LD      HL,($85F6)          
2484: 11 04 00        LD      DE,$0004            
2487: 18 BD           JR      $11F3               ; {}
2489: 21 4A 86        LD      HL,$864A            
248C: CB F6           SET     6,(HL)              
248E: 2A F6 85        LD      HL,($85F6)          
2491: 23              INC     HL                  
2492: CB 46           BIT     0,(HL)              
2494: C2 FD 24        JP      NZ,$24FD            ; {}
2497: 06 00           LD      B,$00               
2499: 2A F6 85        LD      HL,($85F6)          
249C: 23              INC     HL                  
249D: CB 4E           BIT     1,(HL)              
249F: CC 9A 28        CALL    Z,$289A             ; {}
24A2: C4 B0 28        CALL    NZ,$28B0            ; {}
24A5: CB 40           BIT     0,B                 
24A7: CA FD 24        JP      Z,$24FD             ; {}
24AA: CD D4 28        CALL    $28D4               ; {}
24AD: CB 40           BIT     0,B                 
24AF: CA FD 24        JP      Z,$24FD             ; {}
24B2: 2A F6 85        LD      HL,($85F6)          
24B5: CB 8E           RES     1,(HL)              
24B7: 23              INC     HL                  
24B8: CB 4E           BIT     1,(HL)              
24BA: 20 28           JR      NZ,$125E            ; {}
24BC: 23              INC     HL                  
24BD: 23              INC     HL                  
24BE: 23              INC     HL                  
24BF: 23              INC     HL                  
24C0: 7E              LD      A,(HL)              
24C1: FE 20           CP      $20                 
24C3: D2 D0 24        JP      NC,$24D0            ; {}
24C6: FE 16           CP      $16                 
24C8: D2 D7 24        JP      NC,$24D7            ; {}
24CB: 36 08           LD      (HL),$08            
24CD: C3 18 25        JP      $2518               ; {}
24D0: E6 0F           AND     $0F                 
24D2: FE 08           CP      $08                 
24D4: DA E0 24        JP      C,$24E0             ; {}
24D7: 0E 10           LD      C,$10               
24D9: 7E              LD      A,(HL)              
24DA: E6 F0           AND     $F0                 
24DC: 81              ADD     A,C                 
24DD: 77              LD      (HL),A              
24DE: E1              POP     HL                  
24DF: C9              RET                         
24E0: 0E 00           LD      C,$00               
24E2: 18 F5           JR      $122B               ; {}
24E4: 23              INC     HL                  
24E5: 23              INC     HL                  
24E6: 23              INC     HL                  
24E7: 7E              LD      A,(HL)              
24E8: E6 0F           AND     $0F                 
24EA: FE 08           CP      $08                 
24EC: DA F8 24        JP      C,$24F8             ; {}
24EF: 7E              LD      A,(HL)              
24F0: E6 F0           AND     $F0                 
24F2: C6 11           ADD     $11                 
24F4: 77              LD      (HL),A              
24F5: C3 18 25        JP      $2518               ; {}
24F8: 7E              LD      A,(HL)              
24F9: E6 F0           AND     $F0                 
24FB: 3C              INC     A                   
24FC: 77              LD      (HL),A              
24FD: 21 4A 86        LD      HL,$864A            
2500: CB 76           BIT     6,(HL)              
2502: 28 14           JR      Z,$124A             ; {}
2504: CB B6           RES     6,(HL)              
2506: 2A F6 85        LD      HL,($85F6)          
2509: 23              INC     HL                  
250A: CB 4E           BIT     1,(HL)              
250C: 28 05           JR      Z,$123B             ; {}
250E: CB 8E           RES     1,(HL)              
2510: C3 8E 24        JP      $248E               ; {}
2513: CB CE           SET     1,(HL)              
2515: C3 8E 24        JP      $248E               ; {}
2518: E1              POP     HL                  
2519: C9              RET                         
251A: 7E              LD      A,(HL)              
251B: E6 7F           AND     $7F                 
251D: FE 10           CP      $10                 
251F: DA 28 25        JP      C,$2528             ; {}
2522: FE 7E           CP      $7E                 
2524: CA 28 25        JP      Z,$2528             ; {}
2527: C9              RET                         
2528: 0D              DEC     C                   
2529: C9              RET                         
252A: 22 F6 85        LD      ($85F6),HL          
252D: 2A F6 85        LD      HL,($85F6)          
2530: 23              INC     HL                  
2531: 23              INC     HL                  
2532: CB 66           BIT     4,(HL)              
2534: C2 C0 25        JP      NZ,$25C0            ; {}
2537: 2A F6 85        LD      HL,($85F6)          
253A: CB 46           BIT     0,(HL)              
253C: C2 30 26        JP      NZ,$2630            ; {}
253F: 2A F6 85        LD      HL,($85F6)          
2542: 7E              LD      A,(HL)              
2543: E6 3C           AND     $3C                 
2545: CA C0 25        JP      Z,$25C0             ; {}
2548: 11 0C 00        LD      DE,$000C            
254B: 19              ADD     HL,DE               
254C: 35              DEC     (HL)                
254D: 7E              LD      A,(HL)              
254E: FE 0D           CP      $0D                 
2550: C2 C2 25        JP      NZ,$25C2            ; {}
2553: 2A F6 85        LD      HL,($85F6)          
2556: CB 6E           BIT     5,(HL)              
2558: CA C0 25        JP      Z,$25C0             ; {}
255B: 11 04 00        LD      DE,$0004            
255E: 19              ADD     HL,DE               
255F: 3A 00 84        LD      A,($8400)           
2562: E6 06           AND     $06                 
2564: FE 06           CP      $06                 
2566: C2 7E 25        JP      NZ,$257E            ; {}
2569: 7E              LD      A,(HL)              
256A: 32 FE 98        LD      ($98FE),A           
256D: D6 10           SUB     $10                 
256F: 32 F6 98        LD      ($98F6),A           
2572: 23              INC     HL                  
2573: 7E              LD      A,(HL)              
2574: D6 09           SUB     $09                 
2576: 32 FF 98        LD      ($98FF),A           
2579: 32 F7 98        LD      ($98F7),A           
257C: 18 13           JR      $1249               ; {}
257E: 7E              LD      A,(HL)              
257F: 32 F6 98        LD      ($98F6),A           
2582: C6 10           ADD     $10                 
2584: 32 FE 98        LD      ($98FE),A           
2587: 23              INC     HL                  
2588: 7E              LD      A,(HL)              
2589: C6 07           ADD     $07                 
258B: 32 F7 98        LD      ($98F7),A           
258E: 32 FF 98        LD      ($98FF),A           
2591: 2A F6 85        LD      HL,($85F6)          
2594: CB EE           SET     5,(HL)              
2596: 23              INC     HL                  
2597: 23              INC     HL                  
2598: CB C6           SET     0,(HL)              
259A: 23              INC     HL                  
259B: CB FE           SET     7,(HL)              
259D: 2B              DEC     HL                  
259E: 2B              DEC     HL                  
259F: 2B              DEC     HL                  
25A0: 11 04 00        LD      DE,$0004            
25A3: 19              ADD     HL,DE               
25A4: 36 F1           LD      (HL),$F1            
25A6: 23              INC     HL                  
25A7: 36 00           LD      (HL),$00            
25A9: 23              INC     HL                  
25AA: 36 32           LD      (HL),$32            
25AC: 11 07 00        LD      DE,$0007            
25AF: 19              ADD     HL,DE               
25B0: CB 96           RES     2,(HL)              
25B2: CB 9E           RES     3,(HL)              
25B4: AF              XOR     A                   
25B5: 32 A0 98        LD      ($98A0),A           
25B8: 32 A1 98        LD      ($98A1),A           
25BB: 21 03 84        LD      HL,$8403            
25BE: CB 96           RES     2,(HL)              
25C0: E1              POP     HL                  
25C1: C9              RET                         
25C2: A7              AND     A                   
25C3: C2 C0 25        JP      NZ,$25C0            ; {}
25C6: 21 D7 32        LD      HL,$32D7            
25C9: 3A 10 84        LD      A,($8410)           
25CC: 3D              DEC     A                   
25CD: 5F              LD      E,A                 
25CE: 16 00           LD      D,$00               
25D0: 19              ADD     HL,DE               
25D1: 7E              LD      A,(HL)              
25D2: 2A F6 85        LD      HL,($85F6)          
25D5: 11 0C 00        LD      DE,$000C            
25D8: 19              ADD     HL,DE               
25D9: 77              LD      (HL),A              
25DA: 2A F6 85        LD      HL,($85F6)          
25DD: CB 56           BIT     2,(HL)              
25DF: 28 1B           JR      Z,$1251             ; {}
25E1: CB 96           RES     2,(HL)              
25E3: CB B6           RES     6,(HL)              
25E5: 21 9E 87        LD      HL,$879E            
25E8: 3A 9D 87        LD      A,($879D)           
25EB: BE              CP      (HL)                
25EC: 20 0C           JR      NZ,$1242            ; {}
25EE: CD 87 0F        CALL    $0F87               ; {}
25F1: 21 03 84        LD      HL,$8403            
25F4: CB 96           RES     2,(HL)              
25F6: 2B              DEC     HL                  
25F7: 2B              DEC     HL                  
25F8: CB 9E           RES     3,(HL)              
25FA: E1              POP     HL                  
25FB: C9              RET                         
25FC: CB 5E           BIT     3,(HL)              
25FE: 28 06           JR      Z,$123C             ; {}
2600: CB 9E           RES     3,(HL)              
2602: CB D6           SET     2,(HL)              
2604: 18 08           JR      $123E               ; {}
2606: CB 66           BIT     4,(HL)              
2608: 28 0A           JR      Z,$1240             ; {}
260A: CB A6           RES     4,(HL)              
260C: CB DE           SET     3,(HL)              
260E: 23              INC     HL                  
260F: 23              INC     HL                  
2610: CB EE           SET     5,(HL)              
2612: E1              POP     HL                  
2613: C9              RET                         
2614: CB 6E           BIT     5,(HL)              
2616: 20 02           JR      NZ,$1238            ; {}
2618: E1              POP     HL                  
2619: C9              RET                         
261A: CB AE           RES     5,(HL)              
261C: 21 04 84        LD      HL,$8404            
261F: CB B6           RES     6,(HL)              
2621: AF              XOR     A                   
2622: 32 F6 98        LD      ($98F6),A           
2625: 32 F7 98        LD      ($98F7),A           
2628: 32 FE 98        LD      ($98FE),A           
262B: 32 FF 98        LD      ($98FF),A           
262E: E1              POP     HL                  
262F: C9              RET                         
2630: 3A 29 86        LD      A,($8629)           
2633: E5              PUSH    HL                  
2634: C5              PUSH    BC                  
2635: 3D              DEC     A                   
2636: 28 10           JR      Z,$1246             ; {}
2638: 3D              DEC     A                   
2639: 28 12           JR      Z,$1248             ; {}
263B: 3D              DEC     A                   
263C: 20 05           JR      NZ,$123B            ; {}
263E: 21 A4 98        LD      HL,$98A4            
2641: 18 0D           JR      $1243               ; {}
2643: 21 B6 98        LD      HL,$98B6            
2646: 18 08           JR      $123E               ; {}
2648: 21 AA 98        LD      HL,$98AA            
264B: 18 03           JR      $1239               ; {}
264D: 21 B0 98        LD      HL,$98B0            
2650: 06 03           LD      B,$03               
2652: 36 00           LD      (HL),$00            
2654: 23              INC     HL                  
2655: 36 50           LD      (HL),$50            
2657: 23              INC     HL                  
2658: 10 F8           DJNZ    $122E               ; {}
265A: C1              POP     BC                  
265B: E1              POP     HL                  
265C: C3 3F 25        JP      $253F               ; {}
265F: 11 06 00        LD      DE,$0006            
2662: 19              ADD     HL,DE               
2663: 22 F6 85        LD      ($85F6),HL          
2666: 11 04 00        LD      DE,$0004            
2669: 19              ADD     HL,DE               
266A: 34              INC     (HL)                
266B: 7E              LD      A,(HL)              
266C: E6 0F           AND     $0F                 
266E: FE 08           CP      $08                 
2670: DA 7D 26        JP      C,$267D             ; {}
2673: 2A F6 85        LD      HL,($85F6)          
2676: 36 2A           LD      (HL),$2A            
2678: 23              INC     HL                  
2679: 36 03           LD      (HL),$03            
267B: E1              POP     HL                  
267C: C9              RET                         
267D: 2A F6 85        LD      HL,($85F6)          
2680: 36 2B           LD      (HL),$2B            
2682: 23              INC     HL                  
2683: 36 03           LD      (HL),$03            
2685: E1              POP     HL                  
2686: C9              RET                         
2687: E5              PUSH    HL                  
2688: 7E              LD      A,(HL)              
2689: E6 FC           AND     $FC                 
268B: C2 C0 26        JP      NZ,$26C0            ; {}
268E: CB 4E           BIT     1,(HL)              
2690: CA 26 28        JP      Z,$2826             ; {}
2693: CB 46           BIT     0,(HL)              
2695: C2 5F 26        JP      NZ,$265F            ; {}
2698: 11 06 00        LD      DE,$0006            
269B: 19              ADD     HL,DE               
269C: 22 F6 85        LD      ($85F6),HL          
269F: 11 04 00        LD      DE,$0004            
26A2: 19              ADD     HL,DE               
26A3: 34              INC     (HL)                
26A4: 7E              LD      A,(HL)              
26A5: E6 0F           AND     $0F                 
26A7: FE 08           CP      $08                 
26A9: DA B6 26        JP      C,$26B6             ; {}
26AC: 2A F6 85        LD      HL,($85F6)          
26AF: 36 28           LD      (HL),$28            
26B1: 23              INC     HL                  
26B2: 36 03           LD      (HL),$03            
26B4: E1              POP     HL                  
26B5: C9              RET                         
26B6: 2A F6 85        LD      HL,($85F6)          
26B9: 36 29           LD      (HL),$29            
26BB: 23              INC     HL                  
26BC: 36 03           LD      (HL),$03            
26BE: E1              POP     HL                  
26BF: C9              RET                         
26C0: CB 7F           BIT     7,A                 
26C2: 28 3C           JR      Z,$1272             ; {}
26C4: 3A 9E 87        LD      A,($879E)           
26C7: 57              LD      D,A                 
26C8: 3A 9D 87        LD      A,($879D)           
26CB: BA              CP      D                   
26CC: 20 13           JR      NZ,$1249            ; {}
26CE: E5              PUSH    HL                  
26CF: CD 87 0F        CALL    $0F87               ; {}
26D2: 21 01 84        LD      HL,$8401            
26D5: CB 9E           RES     3,(HL)              
26D7: 23              INC     HL                  
26D8: 23              INC     HL                  
26D9: CB 96           RES     2,(HL)              
26DB: 21 3E 86        LD      HL,$863E            
26DE: 36 00           LD      (HL),$00            
26E0: E1              POP     HL                  
26E1: CB 46           BIT     0,(HL)              
26E3: C2 F5 26        JP      NZ,$26F5            ; {}
26E6: 11 06 00        LD      DE,$0006            
26E9: 19              ADD     HL,DE               
26EA: 36 22           LD      (HL),$22            
26EC: 23              INC     HL                  
26ED: 36 01           LD      (HL),$01            
26EF: E1              POP     HL                  
26F0: C9              RET                         
26F1: E5              PUSH    HL                  
26F2: C3 E1 26        JP      $26E1               ; {}
26F5: 11 06 00        LD      DE,$0006            
26F8: 19              ADD     HL,DE               
26F9: 36 26           LD      (HL),$26            
26FB: 23              INC     HL                  
26FC: 36 02           LD      (HL),$02            
26FE: E1              POP     HL                  
26FF: C9              RET                         
2700: 22 F6 85        LD      ($85F6),HL          
2703: 11 07 00        LD      DE,$0007            
2706: 19              ADD     HL,DE               
2707: E5              PUSH    HL                  
2708: DD E1           POP     IX                  
270A: 2B              DEC     HL                  
270B: E5              PUSH    HL                  
270C: FD E1           POP     IY                  
270E: 2A F6 85        LD      HL,($85F6)          
2711: 23              INC     HL                  
2712: 23              INC     HL                  
2713: CB 46           BIT     0,(HL)              
2715: CA 1A 27        JP      Z,$271A             ; {}
2718: E1              POP     HL                  
2719: C9              RET                         
271A: 2A F6 85        LD      HL,($85F6)          
271D: CB 46           BIT     0,(HL)              
271F: C2 DD 27        JP      NZ,$27DD            ; {}
2722: DD 36 00 01     LD      (IX+$00),$01        
2726: CB 56           BIT     2,(HL)              
2728: 28 21           JR      Z,$1257             ; {}
272A: FD 36 00 23     LD      (IY+$00),$23        
272E: 23              INC     HL                  
272F: 23              INC     HL                  
2730: CB 6E           BIT     5,(HL)              
2732: C2 37 27        JP      NZ,$2737            ; {}
2735: E1              POP     HL                  
2736: C9              RET                         
2737: CB AE           RES     5,(HL)              
2739: 3A 00 84        LD      A,($8400)           
273C: E6 06           AND     $06                 
273E: FE 06           CP      $06                 
2740: CA 84 27        JP      Z,$2784             ; {}
2743: CD A2 27        CALL    $27A2               ; {}
2746: C6 04           ADD     $04                 
2748: 77              LD      (HL),A              
2749: E1              POP     HL                  
274A: C9              RET                         
274B: CB 5E           BIT     3,(HL)              
274D: 28 70           JR      Z,$12A6             ; {}
274F: FD 36 00 80     LD      (IY+$00),$80        
2753: 23              INC     HL                  
2754: 23              INC     HL                  
2755: CB 6E           BIT     5,(HL)              
2757: C2 61 27        JP      NZ,$2761            ; {}
275A: CB 66           BIT     4,(HL)              
275C: C2 70 27        JP      NZ,$2770            ; {}
275F: E1              POP     HL                  
2760: C9              RET                         
2761: CB AE           RES     5,(HL)              
2763: 2A F6 85        LD      HL,($85F6)          
2766: 11 05 00        LD      DE,$0005            
2769: 19              ADD     HL,DE               
276A: 7E              LD      A,(HL)              
276B: C6 04           ADD     $04                 
276D: 77              LD      (HL),A              
276E: E1              POP     HL                  
276F: C9              RET                         
2770: CB A6           RES     4,(HL)              
2772: 3A 00 84        LD      A,($8400)           
2775: E6 06           AND     $06                 
2777: FE 06           CP      $06                 
2779: CA 8C 27        JP      Z,$278C             ; {}
277C: CD 94 27        CALL    $2794               ; {}
277F: D6 04           SUB     $04                 
2781: 77              LD      (HL),A              
2782: E1              POP     HL                  
2783: C9              RET                         
2784: CD 94 27        CALL    $2794               ; {}
2787: D6 0C           SUB     $0C                 
2789: 77              LD      (HL),A              
278A: E1              POP     HL                  
278B: C9              RET                         
278C: CD A2 27        CALL    $27A2               ; {}
278F: C6 0C           ADD     $0C                 
2791: 77              LD      (HL),A              
2792: E1              POP     HL                  
2793: C9              RET                         
2794: 2A F6 85        LD      HL,($85F6)          
2797: 11 04 00        LD      DE,$0004            
279A: 19              ADD     HL,DE               
279B: 7E              LD      A,(HL)              
279C: D6 08           SUB     $08                 
279E: 77              LD      (HL),A              
279F: 23              INC     HL                  
27A0: 7E              LD      A,(HL)              
27A1: C9              RET                         
27A2: 2A F6 85        LD      HL,($85F6)          
27A5: 11 04 00        LD      DE,$0004            
27A8: 19              ADD     HL,DE               
27A9: 7E              LD      A,(HL)              
27AA: C6 08           ADD     $08                 
27AC: 77              LD      (HL),A              
27AD: 23              INC     HL                  
27AE: 7E              LD      A,(HL)              
27AF: C9              RET                         
27B0: CB A6           RES     4,(HL)              
27B2: 2A F6 85        LD      HL,($85F6)          
27B5: 11 05 00        LD      DE,$0005            
27B8: 19              ADD     HL,DE               
27B9: 7E              LD      A,(HL)              
27BA: D6 04           SUB     $04                 
27BC: 77              LD      (HL),A              
27BD: E1              POP     HL                  
27BE: C9              RET                         
27BF: CB 66           BIT     4,(HL)              
27C1: 28 0D           JR      Z,$1243             ; {}
27C3: FD 36 00 81     LD      (IY+$00),$81        
27C7: 23              INC     HL                  
27C8: 23              INC     HL                  
27C9: CB 66           BIT     4,(HL)              
27CB: C2 B0 27        JP      NZ,$27B0            ; {}
27CE: E1              POP     HL                  
27CF: C9              RET                         
27D0: CB 6E           BIT     5,(HL)              
27D2: 28 07           JR      Z,$123D             ; {}
27D4: FD 36 00 82     LD      (IY+$00),$82        
27D8: CD 87 0F        CALL    $0F87               ; {}
27DB: E1              POP     HL                  
27DC: C9              RET                         
27DD: DD 36 00 02     LD      (IX+$00),$02        
27E1: CB 56           BIT     2,(HL)              
27E3: 28 0D           JR      Z,$1243             ; {}
27E5: FD 36 00 27     LD      (IY+$00),$27        
27E9: 23              INC     HL                  
27EA: 23              INC     HL                  
27EB: CB 6E           BIT     5,(HL)              
27ED: C2 37 27        JP      NZ,$2737            ; {}
27F0: E1              POP     HL                  
27F1: C9              RET                         
27F2: CB 5E           BIT     3,(HL)              
27F4: 28 12           JR      Z,$1248             ; {}
27F6: FD 36 00 83     LD      (IY+$00),$83        
27FA: 23              INC     HL                  
27FB: 23              INC     HL                  
27FC: CB 6E           BIT     5,(HL)              
27FE: C2 61 27        JP      NZ,$2761            ; {}
2801: CB 66           BIT     4,(HL)              
2803: C2 70 27        JP      NZ,$2770            ; {}
2806: E1              POP     HL                  
2807: C9              RET                         
2808: CB 66           BIT     4,(HL)              
280A: 28 0D           JR      Z,$1243             ; {}
280C: FD 36 00 84     LD      (IY+$00),$84        
2810: 23              INC     HL                  
2811: 23              INC     HL                  
2812: CB 66           BIT     4,(HL)              
2814: C2 B0 27        JP      NZ,$27B0            ; {}
2817: E1              POP     HL                  
2818: C9              RET                         
2819: CB 6E           BIT     5,(HL)              
281B: 28 07           JR      Z,$123D             ; {}
281D: FD 36 00 85     LD      (IY+$00),$85        
2821: CD 87 0F        CALL    $0F87               ; {}
2824: E1              POP     HL                  
2825: C9              RET                         
2826: 3A 01 84        LD      A,($8401)           
2829: CB 7F           BIT     7,A                 
282B: 28 02           JR      Z,$1238             ; {}
282D: E1              POP     HL                  
282E: C9              RET                         
282F: 11 0E 00        LD      DE,$000E            
2832: 19              ADD     HL,DE               
2833: 7E              LD      A,(HL)              
2834: E6 07           AND     $07                 
2836: FE 02           CP      $02                 
2838: 28 09           JR      Z,$123F             ; {}
283A: FE 06           CP      $06                 
283C: 20 08           JR      NZ,$123E            ; {}
283E: 2B              DEC     HL                  
283F: 36 02           LD      (HL),$02            
2841: 18 03           JR      $1239               ; {}
2843: 2B              DEC     HL                  
2844: 36 00           LD      (HL),$00            
2846: E1              POP     HL                  
2847: E5              PUSH    HL                  
2848: CB 46           BIT     0,(HL)              
284A: 20 1C           JR      NZ,$1252            ; {}
284C: 11 06 00        LD      DE,$0006            
284F: CD 8D 28        CALL    $288D               ; {}
2852: FE 04           CP      $04                 
2854: DA 61 28        JP      C,$2861             ; {}
2857: 2A F6 85        LD      HL,($85F6)          
285A: 36 21           LD      (HL),$21            
285C: 23              INC     HL                  
285D: 36 01           LD      (HL),$01            
285F: E1              POP     HL                  
2860: C9              RET                         
2861: 2A F6 85        LD      HL,($85F6)          
2864: 36 20           LD      (HL),$20            
2866: 18 F4           JR      $122A               ; {}
2868: 23              INC     HL                  
2869: CB 76           BIT     6,(HL)              
286B: 28 02           JR      Z,$1238             ; {}
286D: E1              POP     HL                  
286E: C9              RET                         
286F: 11 05 00        LD      DE,$0005            
2872: CD 8D 28        CALL    $288D               ; {}
2875: E6 07           AND     $07                 
2877: FE 04           CP      $04                 
2879: DA 86 28        JP      C,$2886             ; {}
287C: 2A F6 85        LD      HL,($85F6)          
287F: 36 25           LD      (HL),$25            
2881: 23              INC     HL                  
2882: 36 02           LD      (HL),$02            
2884: E1              POP     HL                  
2885: C9              RET                         
2886: 2A F6 85        LD      HL,($85F6)          
2889: 36 24           LD      (HL),$24            
288B: 18 F4           JR      $122A               ; {}
288D: 19              ADD     HL,DE               
288E: 22 F6 85        LD      ($85F6),HL          
2891: 11 04 00        LD      DE,$0004            
2894: 19              ADD     HL,DE               
2895: 34              INC     (HL)                
2896: 7E              LD      A,(HL)              
2897: E6 0F           AND     $0F                 
2899: C9              RET                         
289A: E5              PUSH    HL                  
289B: F5              PUSH    AF                  
289C: 23              INC     HL                  
289D: 23              INC     HL                  
289E: 23              INC     HL                  
289F: 7E              LD      A,(HL)              
28A0: E6 0F           AND     $0F                 
28A2: FE 01           CP      $01                 
28A4: 28 05           JR      Z,$123B             ; {}
28A6: CB 80           RES     0,B                 
28A8: F1              POP     AF                  
28A9: E1              POP     HL                  
28AA: C9              RET                         
28AB: CB C0           SET     0,B                 
28AD: F1              POP     AF                  
28AE: E1              POP     HL                  
28AF: C9              RET                         
28B0: E5              PUSH    HL                  
28B1: F5              PUSH    AF                  
28B2: 23              INC     HL                  
28B3: 23              INC     HL                  
28B4: 23              INC     HL                  
28B5: 23              INC     HL                  
28B6: 7E              LD      A,(HL)              
28B7: 4F              LD      C,A                 
28B8: E6 0F           AND     $0F                 
28BA: 57              LD      D,A                 
28BB: 79              LD      A,C                 
28BC: FE 20           CP      $20                 
28BE: D2 CB 28        JP      NC,$28CB            ; {}
28C1: FE 08           CP      $08                 
28C3: CA CF 28        JP      Z,$28CF             ; {}
28C6: CB 80           RES     0,B                 
28C8: F1              POP     AF                  
28C9: E1              POP     HL                  
28CA: C9              RET                         
28CB: 7A              LD      A,D                 
28CC: A7              AND     A                   
28CD: 20 F7           JR      NZ,$122D            ; {}
28CF: CB C0           SET     0,B                 
28D1: F1              POP     AF                  
28D2: E1              POP     HL                  
28D3: C9              RET                         
28D4: 2A F6 85        LD      HL,($85F6)          
28D7: 11 04 00        LD      DE,$0004            
28DA: 19              ADD     HL,DE               
28DB: 56              LD      D,(HL)              
28DC: 23              INC     HL                  
28DD: 5E              LD      E,(HL)              
28DE: CD 0E 1C        CALL    $1C0E               ; {}
28E1: 0E 04           LD      C,$04               
28E3: 2A FA 85        LD      HL,($85FA)          
28E6: CD 1A 25        CALL    $251A               ; {}
28E9: 2A FC 85        LD      HL,($85FC)          
28EC: CD 1A 25        CALL    $251A               ; {}
28EF: 2A FE 85        LD      HL,($85FE)          
28F2: CD 1A 25        CALL    $251A               ; {}
28F5: 2A 00 86        LD      HL,($8600)          
28F8: CD 1A 25        CALL    $251A               ; {}
28FB: 79              LD      A,C                 
28FC: A7              AND     A                   
28FD: 28 03           JR      Z,$1239             ; {}
28FF: CB 80           RES     0,B                 
2901: C9              RET                         
2902: CB C0           SET     0,B                 
2904: C9              RET                         
2905: 11 69 84        LD      DE,$8469            
2908: A7              AND     A                   
2909: ED 52           SBC     HL,DE               
290B: 7D              LD      A,L                 
290C: CB 3F           SRL     A                   
290E: CB 3F           SRL     A                   
2910: 5F              LD      E,A                 
2911: 16 00           LD      D,$00               
2913: 21 3C 98        LD      HL,$983C            
2916: 19              ADD     HL,DE               
2917: C9              RET                         
2918: 3A BD 87        LD      A,($87BD)           
291B: 47              LD      B,A                 
291C: 2A F6 85        LD      HL,($85F6)          
291F: CB 46           BIT     0,(HL)              
2921: 28 04           JR      Z,$123A             ; {}
2923: 3E 0A           LD      A,$0A               
2925: 80              ADD     A,B                 
2926: 47              LD      B,A                 
2927: C3 A3 29        JP      $29A3               ; {}
292A: 22 F6 85        LD      ($85F6),HL          
292D: 11 04 00        LD      DE,$0004            
2930: 19              ADD     HL,DE               
2931: 7E              LD      A,(HL)              
2932: FE 01           CP      $01                 
2934: C2 3C 29        JP      NZ,$293C            ; {}
2937: 2B              DEC     HL                  
2938: CB FE           SET     7,(HL)              
293A: E1              POP     HL                  
293B: C9              RET                         
293C: 11 0B 00        LD      DE,$000B            
293F: 19              ADD     HL,DE               
2940: 22 1A 86        LD      ($861A),HL          
2943: 2A F6 85        LD      HL,($85F6)          
2946: 23              INC     HL                  
2947: 23              INC     HL                  
2948: CB A6           RES     4,(HL)              
294A: CB AE           RES     5,(HL)              
294C: 23              INC     HL                  
294D: CB B6           RES     6,(HL)              
294F: CB 7E           BIT     7,(HL)              
2951: 28 02           JR      Z,$1238             ; {}
2953: E1              POP     HL                  
2954: C9              RET                         
2955: 2A F6 85        LD      HL,($85F6)          
2958: 11 05 00        LD      DE,$0005            
295B: 19              ADD     HL,DE               
295C: 7E              LD      A,(HL)              
295D: FE 08           CP      $08                 
295F: CA 18 29        JP      Z,$2918             ; {}
2962: 3A 46 86        LD      A,($8646)           
2965: CB 5F           BIT     3,A                 
2967: 28 11           JR      Z,$1247             ; {}
2969: 2A F6 85        LD      HL,($85F6)          
296C: CB 46           BIT     0,(HL)              
296E: 28 05           JR      Z,$123B             ; {}
2970: 21 A5 87        LD      HL,$87A5            
2973: 18 2C           JR      $1262               ; {}
2975: 21 A2 87        LD      HL,$87A2            
2978: 18 27           JR      $125D               ; {}
297A: 3A 53 86        LD      A,($8653)           
297D: CB 4F           BIT     1,A                 
297F: 28 11           JR      Z,$1247             ; {}
2981: 2A F6 85        LD      HL,($85F6)          
2984: CB 46           BIT     0,(HL)              
2986: 28 05           JR      Z,$123B             ; {}
2988: 21 A4 87        LD      HL,$87A4            
298B: 18 14           JR      $124A               ; {}
298D: 21 A1 87        LD      HL,$87A1            
2990: 18 0F           JR      $1245               ; {}
2992: 2A F6 85        LD      HL,($85F6)          
2995: CB 46           BIT     0,(HL)              
2997: 28 05           JR      Z,$123B             ; {}
2999: 21 A3 87        LD      HL,$87A3            
299C: 18 03           JR      $1239               ; {}
299E: 21 A0 87        LD      HL,$87A0            
29A1: 00              NOP                         
29A2: 46              LD      B,(HL)              
29A3: 2A F6 85        LD      HL,($85F6)          
29A6: 11 0E 00        LD      DE,$000E            
29A9: 19              ADD     HL,DE               
29AA: 7E              LD      A,(HL)              
29AB: E6 07           AND     $07                 
29AD: FE 04           CP      $04                 
29AF: 20 19           JR      NZ,$124F            ; {}
29B1: 3A 57 86        LD      A,($8657)           
29B4: CB 4F           BIT     1,A                 
29B6: 20 07           JR      NZ,$123D            ; {}
29B8: 3A 0F 84        LD      A,($840F)           
29BB: FE 04           CP      $04                 
29BD: 38 0B           JR      C,$1241             ; {}
29BF: 3A E6 32        LD      A,($32E6)           ; {}
29C2: 80              ADD     A,B                 
29C3: 47              LD      B,A                 
29C4: FE 28           CP      $28                 
29C6: 30 02           JR      NC,$1238            ; {}
29C8: 06 FF           LD      B,$FF               
29CA: 2A F6 85        LD      HL,($85F6)          
29CD: 11 09 00        LD      DE,$0009            
29D0: 19              ADD     HL,DE               
29D1: 7E              LD      A,(HL)              
29D2: 90              SUB     B                   
29D3: 77              LD      (HL),A              
29D4: 38 02           JR      C,$1238             ; {}
29D6: E1              POP     HL                  
29D7: C9              RET                         
29D8: 2A F6 85        LD      HL,($85F6)          
29DB: 23              INC     HL                  
29DC: CD 9A 28        CALL    $289A               ; {}
29DF: CB 40           BIT     0,B                 
29E1: 20 0B           JR      NZ,$1241            ; {}
29E3: CD B0 28        CALL    $28B0               ; {}
29E6: CB 40           BIT     0,B                 
29E8: CA 69 2C        JP      Z,$2C69             ; {}
29EB: C3 DA 2C        JP      $2CDA               ; {}
29EE: CD B0 28        CALL    $28B0               ; {}
29F1: CB 40           BIT     0,B                 
29F3: CA DA 2C        JP      Z,$2CDA             ; {}
29F6: 23              INC     HL                  
29F7: 23              INC     HL                  
29F8: 23              INC     HL                  
29F9: 56              LD      D,(HL)              
29FA: 23              INC     HL                  
29FB: 5E              LD      E,(HL)              
29FC: CD 14 1C        CALL    $1C14               ; {}
29FF: 2A F6 85        LD      HL,($85F6)          
2A02: CB 46           BIT     0,(HL)              
2A04: CA 20 2C        JP      Z,$2C20             ; {}
2A07: 11 06 00        LD      DE,$0006            
2A0A: 19              ADD     HL,DE               
2A0B: 7E              LD      A,(HL)              
2A0C: FE 2A           CP      $2A                 
2A0E: CA 20 2C        JP      Z,$2C20             ; {}
2A11: FE 2B           CP      $2B                 
2A13: CA 20 2C        JP      Z,$2C20             ; {}
2A16: FE 27           CP      $27                 
2A18: C2 1D 2A        JP      NZ,$2A1D            ; {}
2A1B: 36 24           LD      (HL),$24            
2A1D: 2A 1A 86        LD      HL,($861A)          
2A20: 2B              DEC     HL                  
2A21: CB 4E           BIT     1,(HL)              
2A23: CA 20 2C        JP      Z,$2C20             ; {}
2A26: 2A F6 85        LD      HL,($85F6)          
2A29: 11 04 00        LD      DE,$0004            
2A2C: 19              ADD     HL,DE               
2A2D: 7E              LD      A,(HL)              
2A2E: FE D1           CP      $D1                 
2A30: D2 20 2C        JP      NC,$2C20            ; {}
2A33: FE 22           CP      $22                 
2A35: DA 20 2C        JP      C,$2C20             ; {}
2A38: CD CC 2E        CALL    $2ECC               ; {}
2A3B: 78              LD      A,B                 
2A3C: FE 03           CP      $03                 
2A3E: CA 20 2C        JP      Z,$2C20             ; {}
2A41: 2A F6 85        LD      HL,($85F6)          
2A44: 23              INC     HL                  
2A45: CB 76           BIT     6,(HL)              
2A47: C2 9C 2A        JP      NZ,$2A9C            ; {}
2A4A: 21 C8 32        LD      HL,$32C8            
2A4D: 3A 0F 84        LD      A,($840F)           
2A50: 3D              DEC     A                   
2A51: E6 0F           AND     $0F                 
2A53: 5F              LD      E,A                 
2A54: 16 00           LD      D,$00               
2A56: 19              ADD     HL,DE               
2A57: 46              LD      B,(HL)              
2A58: 2A F6 85        LD      HL,($85F6)          
2A5B: 11 04 00        LD      DE,$0004            
2A5E: 19              ADD     HL,DE               
2A5F: 3A A2 98        LD      A,($98A2)           
2A62: BE              CP      (HL)                
2A63: 38 03           JR      C,$1239             ; {}
2A65: 96              SUB     (HL)                
2A66: 18 03           JR      $1239               ; {}
2A68: 4F              LD      C,A                 
2A69: 7E              LD      A,(HL)              
2A6A: 91              SUB     C                   
2A6B: FE 3C           CP      $3C                 
2A6D: 30 15           JR      NC,$124B            ; {}
2A6F: 3A A3 98        LD      A,($98A3)           
2A72: 23              INC     HL                  
2A73: BE              CP      (HL)                
2A74: 38 03           JR      C,$1239             ; {}
2A76: 96              SUB     (HL)                
2A77: 18 03           JR      $1239               ; {}
2A79: 4F              LD      C,A                 
2A7A: 7E              LD      A,(HL)              
2A7B: 91              SUB     C                   
2A7C: FE 3C           CP      $3C                 
2A7E: 30 04           JR      NC,$123A            ; {}
2A80: 78              LD      A,B                 
2A81: 87              ADD     A,A                 
2A82: 87              ADD     A,A                 
2A83: 47              LD      B,A                 
2A84: CD F6 1C        CALL    $1CF6               ; {}
2A87: 3A F4 85        LD      A,($85F4)           
2A8A: 90              SUB     B                   
2A8B: D2 20 2C        JP      NC,$2C20            ; {}
2A8E: 2A F6 85        LD      HL,($85F6)          
2A91: 23              INC     HL                  
2A92: CB F6           SET     6,(HL)              
2A94: 11 0A 00        LD      DE,$000A            
2A97: 19              ADD     HL,DE               
2A98: 36 0E           LD      (HL),$0E            
2A9A: E1              POP     HL                  
2A9B: C9              RET                         
2A9C: DD 21 A4 98     LD      IX,$98A4            
2AA0: FD 21 A5 98     LD      IY,$98A5            
2AA4: 21 24 98        LD      HL,$9824            
2AA7: 01 24 99        LD      BC,$9924            
2AAA: 3A 29 86        LD      A,($8629)           
2AAD: FE 01           CP      $01                 
2AAF: 28 12           JR      Z,$1248             ; {}
2AB1: FE 02           CP      $02                 
2AB3: 28 09           JR      Z,$123F             ; {}
2AB5: FE 03           CP      $03                 
2AB7: 28 19           JR      Z,$124F             ; {}
2AB9: 11 12 00        LD      DE,$0012            
2ABC: 18 08           JR      $123E               ; {}
2ABE: 11 0C 00        LD      DE,$000C            
2AC1: 18 03           JR      $1239               ; {}
2AC3: 11 06 00        LD      DE,$0006            
2AC6: 19              ADD     HL,DE               
2AC7: E5              PUSH    HL                  
2AC8: C5              PUSH    BC                  
2AC9: E1              POP     HL                  
2ACA: 19              ADD     HL,DE               
2ACB: E5              PUSH    HL                  
2ACC: C1              POP     BC                  
2ACD: E1              POP     HL                  
2ACE: DD 19           ADD     IX,DE               
2AD0: FD 19           ADD     IY,DE               
2AD2: EB              EX      DE,HL               
2AD3: 2A 1A 86        LD      HL,($861A)          
2AD6: 2B              DEC     HL                  
2AD7: 7E              LD      A,(HL)              
2AD8: 2A F6 85        LD      HL,($85F6)          
2ADB: 23              INC     HL                  
2ADC: 23              INC     HL                  
2ADD: 23              INC     HL                  
2ADE: 23              INC     HL                  
2ADF: E6 07           AND     $07                 
2AE1: FE 02           CP      $02                 
2AE3: 28 1C           JR      Z,$1252             ; {}
2AE5: 7E              LD      A,(HL)              
2AE6: D6 10           SUB     $10                 
2AE8: DD 77 00        LD      (IX+$00),A          
2AEB: DD 23           INC     IX                  
2AED: DD 23           INC     IX                  
2AEF: D6 10           SUB     $10                 
2AF1: DD 77 00        LD      (IX+$00),A          
2AF4: DD 23           INC     IX                  
2AF6: DD 23           INC     IX                  
2AF8: D6 10           SUB     $10                 
2AFA: DD 77 00        LD      (IX+$00),A          
2AFD: 3E 02           LD      A,$02               
2AFF: 18 19           JR      $124F               ; {}
2B01: 7E              LD      A,(HL)              
2B02: C6 10           ADD     $10                 
2B04: DD 77 00        LD      (IX+$00),A          
2B07: DD 23           INC     IX                  
2B09: DD 23           INC     IX                  
2B0B: C6 10           ADD     $10                 
2B0D: DD 77 00        LD      (IX+$00),A          
2B10: DD 23           INC     IX                  
2B12: DD 23           INC     IX                  
2B14: C6 10           ADD     $10                 
2B16: DD 77 00        LD      (IX+$00),A          
2B19: AF              XOR     A                   
2B1A: 02              LD      (BC),A              
2B1B: 03              INC     BC                  
2B1C: 03              INC     BC                  
2B1D: 02              LD      (BC),A              
2B1E: 03              INC     BC                  
2B1F: 03              INC     BC                  
2B20: 02              LD      (BC),A              
2B21: 23              INC     HL                  
2B22: 7E              LD      A,(HL)              
2B23: FD 77 00        LD      (IY+$00),A          
2B26: FD 23           INC     IY                  
2B28: FD 23           INC     IY                  
2B2A: FD 77 00        LD      (IY+$00),A          
2B2D: FD 23           INC     IY                  
2B2F: FD 23           INC     IY                  
2B31: FD 77 00        LD      (IY+$00),A          
2B34: ED 53 27 86     LD      ($8627),DE          
2B38: 2A F6 85        LD      HL,($85F6)          
2B3B: 11 0B 00        LD      DE,$000B            
2B3E: 19              ADD     HL,DE               
2B3F: 35              DEC     (HL)                
2B40: 4E              LD      C,(HL)              
2B41: 2A F6 85        LD      HL,($85F6)          
2B44: 11 08 00        LD      DE,$0008            
2B47: 19              ADD     HL,DE               
2B48: 7E              LD      A,(HL)              
2B49: A7              AND     A                   
2B4A: 20 28           JR      NZ,$125E            ; {}
2B4C: 79              LD      A,C                 
2B4D: A7              AND     A                   
2B4E: 28 5D           JR      Z,$1293             ; {}
2B50: 3D              DEC     A                   
2B51: CA 0B 2C        JP      Z,$2C0B             ; {}
2B54: 3D              DEC     A                   
2B55: CA 0B 2C        JP      Z,$2C0B             ; {}
2B58: 3D              DEC     A                   
2B59: CA F0 2B        JP      Z,$2BF0             ; {}
2B5C: 3D              DEC     A                   
2B5D: 28 68           JR      Z,$129E             ; {}
2B5F: 3D              DEC     A                   
2B60: 28 3D           JR      Z,$1273             ; {}
2B62: 3D              DEC     A                   
2B63: 3D              DEC     A                   
2B64: 28 2E           JR      Z,$1264             ; {}
2B66: 3D              DEC     A                   
2B67: 3D              DEC     A                   
2B68: 28 35           JR      Z,$126B             ; {}
2B6A: 3D              DEC     A                   
2B6B: 3D              DEC     A                   
2B6C: 28 26           JR      Z,$125C             ; {}
2B6E: 3D              DEC     A                   
2B6F: 3D              DEC     A                   
2B70: 28 2D           JR      Z,$1263             ; {}
2B72: E1              POP     HL                  
2B73: C9              RET                         
2B74: FE 01           CP      $01                 
2B76: 20 0F           JR      NZ,$1245            ; {}
2B78: 79              LD      A,C                 
2B79: 3D              DEC     A                   
2B7A: 28 31           JR      Z,$1267             ; {}
2B7C: 3D              DEC     A                   
2B7D: 28 71           JR      Z,$12A7             ; {}
2B7F: 3D              DEC     A                   
2B80: 28 6E           JR      Z,$12A4             ; {}
2B82: 3D              DEC     A                   
2B83: 28 42           JR      Z,$1278             ; {}
2B85: 18 D8           JR      $120E               ; {}
2B87: 79              LD      A,C                 
2B88: 3D              DEC     A                   
2B89: 3D              DEC     A                   
2B8A: 28 21           JR      Z,$1257             ; {}
2B8C: 3D              DEC     A                   
2B8D: 28 38           JR      Z,$126E             ; {}
2B8F: 3D              DEC     A                   
2B90: 28 35           JR      Z,$126B             ; {}
2B92: 18 CB           JR      $1201               ; {}
2B94: 2A F6 85        LD      HL,($85F6)          
2B97: 11 07 00        LD      DE,$0007            
2B9A: 19              ADD     HL,DE               
2B9B: 36 02           LD      (HL),$02            
2B9D: 18 09           JR      $123F               ; {}
2B9F: 2A F6 85        LD      HL,($85F6)          
2BA2: 11 07 00        LD      DE,$0007            
2BA5: 19              ADD     HL,DE               
2BA6: 36 0C           LD      (HL),$0C            
2BA8: CD 95 2F        CALL    $2F95               ; {}
2BAB: E1              POP     HL                  
2BAC: C9              RET                         
2BAD: 2A F6 85        LD      HL,($85F6)          
2BB0: 23              INC     HL                  
2BB1: CB B6           RES     6,(HL)              
2BB3: CD 95 2F        CALL    $2F95               ; {}
2BB6: 2A 27 86        LD      HL,($8627)          
2BB9: 3E 32           LD      A,$32               
2BBB: 77              LD      (HL),A              
2BBC: 23              INC     HL                  
2BBD: 23              INC     HL                  
2BBE: 77              LD      (HL),A              
2BBF: 23              INC     HL                  
2BC0: 23              INC     HL                  
2BC1: 77              LD      (HL),A              
2BC2: CD 5D 15        CALL    $155D               ; {}
2BC5: E1              POP     HL                  
2BC6: C9              RET                         
2BC7: 2A 27 86        LD      HL,($8627)          
2BCA: 36 2C           LD      (HL),$2C            
2BCC: 23              INC     HL                  
2BCD: 36 05           LD      (HL),$05            
2BCF: 23              INC     HL                  
2BD0: 36 32           LD      (HL),$32            
2BD2: 23              INC     HL                  
2BD3: 23              INC     HL                  
2BD4: 36 32           LD      (HL),$32            
2BD6: DD 2B           DEC     IX                  
2BD8: DD 2B           DEC     IX                  
2BDA: DD 2B           DEC     IX                  
2BDC: DD 2B           DEC     IX                  
2BDE: FD 2B           DEC     IY                  
2BE0: FD 2B           DEC     IY                  
2BE2: FD 2B           DEC     IY                  
2BE4: FD 2B           DEC     IY                  
2BE6: CD 5D 15        CALL    $155D               ; {}
2BE9: 21 8E 9A        LD      HL,$9A8E            
2BEC: 36 01           LD      (HL),$01            
2BEE: E1              POP     HL                  
2BEF: C9              RET                         
2BF0: 2A 27 86        LD      HL,($8627)          
2BF3: 3E 05           LD      A,$05               
2BF5: 36 2D           LD      (HL),$2D            
2BF7: 23              INC     HL                  
2BF8: 77              LD      (HL),A              
2BF9: 23              INC     HL                  
2BFA: 36 2E           LD      (HL),$2E            
2BFC: 23              INC     HL                  
2BFD: 77              LD      (HL),A              
2BFE: 23              INC     HL                  
2BFF: 36 32           LD      (HL),$32            
2C01: DD 2B           DEC     IX                  
2C03: DD 2B           DEC     IX                  
2C05: FD 2B           DEC     IY                  
2C07: FD 2B           DEC     IY                  
2C09: 18 B7           JR      $11ED               ; {}
2C0B: 2A 27 86        LD      HL,($8627)          
2C0E: 3E 05           LD      A,$05               
2C10: 36 2F           LD      (HL),$2F            
2C12: 23              INC     HL                  
2C13: 77              LD      (HL),A              
2C14: 23              INC     HL                  
2C15: 36 30           LD      (HL),$30            
2C17: 23              INC     HL                  
2C18: 77              LD      (HL),A              
2C19: 23              INC     HL                  
2C1A: 36 31           LD      (HL),$31            
2C1C: 23              INC     HL                  
2C1D: 77              LD      (HL),A              
2C1E: 18 A2           JR      $11D8               ; {}
2C20: CD F6 1C        CALL    $1CF6               ; {}
2C23: 3A F4 85        LD      A,($85F4)           
2C26: CB 47           BIT     0,A                 
2C28: 20 12           JR      NZ,$1248            ; {}
2C2A: CD 32 2D        CALL    $2D32               ; {}
2C2D: CB 41           BIT     0,C                 
2C2F: C2 C6 2C        JP      NZ,$2CC6            ; {}
2C32: CD 5F 2D        CALL    $2D5F               ; {}
2C35: CB 41           BIT     0,C                 
2C37: C2 C6 2C        JP      NZ,$2CC6            ; {}
2C3A: 18 10           JR      $1246               ; {}
2C3C: CD 5F 2D        CALL    $2D5F               ; {}
2C3F: CB 41           BIT     0,C                 
2C41: C2 C6 2C        JP      NZ,$2CC6            ; {}
2C44: CD 32 2D        CALL    $2D32               ; {}
2C47: CB 41           BIT     0,C                 
2C49: C2 C6 2C        JP      NZ,$2CC6            ; {}
2C4C: 2A 1A 86        LD      HL,($861A)          
2C4F: 2B              DEC     HL                  
2C50: 7E              LD      A,(HL)              
2C51: 23              INC     HL                  
2C52: 77              LD      (HL),A              
2C53: CD A0 2D        CALL    $2DA0               ; {}
2C56: CB 41           BIT     0,C                 
2C58: C2 C6 2C        JP      NZ,$2CC6            ; {}
2C5B: CD F6 1C        CALL    $1CF6               ; {}
2C5E: 3A F4 85        LD      A,($85F4)           
2C61: E6 0F           AND     $0F                 
2C63: FE 0A           CP      $0A                 
2C65: 38 1E           JR      C,$1254             ; {}
2C67: 18 44           JR      $127A               ; {}
2C69: 2A F6 85        LD      HL,($85F6)          
2C6C: CB CE           SET     1,(HL)              
2C6E: 23              INC     HL                  
2C6F: CB C6           SET     0,(HL)              
2C71: 11 0A 00        LD      DE,$000A            
2C74: 19              ADD     HL,DE               
2C75: 36 28           LD      (HL),$28            
2C77: 23              INC     HL                  
2C78: 23              INC     HL                  
2C79: 23              INC     HL                  
2C7A: 7E              LD      A,(HL)              
2C7B: 3C              INC     A                   
2C7C: 3C              INC     A                   
2C7D: 77              LD      (HL),A              
2C7E: CD 72 2F        CALL    $2F72               ; {}
2C81: 36 03           LD      (HL),$03            
2C83: E1              POP     HL                  
2C84: C9              RET                         
2C85: 2A 1A 86        LD      HL,($861A)          
2C88: 2B              DEC     HL                  
2C89: 7E              LD      A,(HL)              
2C8A: 23              INC     HL                  
2C8B: 77              LD      (HL),A              
2C8C: 35              DEC     (HL)                
2C8D: 35              DEC     (HL)                
2C8E: CD A0 2D        CALL    $2DA0               ; {}
2C91: CB 41           BIT     0,C                 
2C93: F5              PUSH    AF                  
2C94: C4 8A 2F        CALL    NZ,$2F8A            ; {}
2C97: F1              POP     AF                  
2C98: 20 2C           JR      NZ,$1262            ; {}
2C9A: 2A 1A 86        LD      HL,($861A)          
2C9D: 34              INC     (HL)                
2C9E: 34              INC     (HL)                
2C9F: 34              INC     (HL)                
2CA0: 34              INC     (HL)                
2CA1: CD A0 2D        CALL    $2DA0               ; {}
2CA4: CB 41           BIT     0,C                 
2CA6: F5              PUSH    AF                  
2CA7: C4 90 2F        CALL    NZ,$2F90            ; {}
2CAA: F1              POP     AF                  
2CAB: 20 19           JR      NZ,$124F            ; {}
2CAD: 2A 1A 86        LD      HL,($861A)          
2CB0: 2B              DEC     HL                  
2CB1: 7E              LD      A,(HL)              
2CB2: 23              INC     HL                  
2CB3: 3C              INC     A                   
2CB4: 3C              INC     A                   
2CB5: 3C              INC     A                   
2CB6: 3C              INC     A                   
2CB7: 77              LD      (HL),A              
2CB8: CD A0 2D        CALL    $2DA0               ; {}
2CBB: CB 41           BIT     0,C                 
2CBD: F5              PUSH    AF                  
2CBE: C4 90 2F        CALL    NZ,$2F90            ; {}
2CC1: F1              POP     AF                  
2CC2: 20 02           JR      NZ,$1238            ; {}
2CC4: 18 A3           JR      $11D9               ; {}
2CC6: CD 72 2F        CALL    $2F72               ; {}
2CC9: 7E              LD      A,(HL)              
2CCA: FE 06           CP      $06                 
2CCC: 38 04           JR      C,$123A             ; {}
2CCE: FE C0           CP      $C0                 
2CD0: 38 97           JR      C,$11CD             ; {}
2CD2: 2A 1A 86        LD      HL,($861A)          
2CD5: 7E              LD      A,(HL)              
2CD6: E6 07           AND     $07                 
2CD8: 2B              DEC     HL                  
2CD9: 77              LD      (HL),A              
2CDA: 2A F6 85        LD      HL,($85F6)          
2CDD: 11 05 00        LD      DE,$0005            
2CE0: 19              ADD     HL,DE               
2CE1: 7E              LD      A,(HL)              
2CE2: FE 08           CP      $08                 
2CE4: 20 0F           JR      NZ,$1245            ; {}
2CE6: 3A F0 87        LD      A,($87F0)           
2CE9: CB 47           BIT     0,A                 
2CEB: 28 08           JR      Z,$123E             ; {}
2CED: 2A 1A 86        LD      HL,($861A)          
2CF0: 2B              DEC     HL                  
2CF1: 36 06           LD      (HL),$06            
2CF3: 18 11           JR      $1247               ; {}
2CF5: 2A 1A 86        LD      HL,($861A)          
2CF8: 2B              DEC     HL                  
2CF9: 7E              LD      A,(HL)              
2CFA: E6 07           AND     $07                 
2CFC: 28 1E           JR      Z,$1254             ; {}
2CFE: FE 02           CP      $02                 
2D00: 28 0F           JR      Z,$1245             ; {}
2D02: FE 04           CP      $04                 
2D04: 28 1B           JR      Z,$1251             ; {}
2D06: 11 04 00        LD      DE,$0004            
2D09: 2A F6 85        LD      HL,($85F6)          
2D0C: 19              ADD     HL,DE               
2D0D: 35              DEC     (HL)                
2D0E: 35              DEC     (HL)                
2D0F: E1              POP     HL                  
2D10: C9              RET                         
2D11: 11 04 00        LD      DE,$0004            
2D14: 2A F6 85        LD      HL,($85F6)          
2D17: 19              ADD     HL,DE               
2D18: 34              INC     (HL)                
2D19: 34              INC     (HL)                
2D1A: E1              POP     HL                  
2D1B: C9              RET                         
2D1C: 11 05 00        LD      DE,$0005            
2D1F: 18 E8           JR      $121E               ; {}
2D21: 2A F6 85        LD      HL,($85F6)          
2D24: 11 05 00        LD      DE,$0005            
2D27: 19              ADD     HL,DE               
2D28: 3A F0 87        LD      A,($87F0)           
2D2B: CB 47           BIT     0,A                 
2D2D: C2 69 2C        JP      NZ,$2C69            ; {}
2D30: 18 E6           JR      $121C               ; {}
2D32: 2A F6 85        LD      HL,($85F6)          
2D35: CB 46           BIT     0,(HL)              
2D37: C2 4D 2F        JP      NZ,$2F4D            ; {}
2D3A: 3A A2 98        LD      A,($98A2)           
2D3D: 21 F0 87        LD      HL,$87F0            
2D40: CB 46           BIT     0,(HL)              
2D42: CA 46 2D        JP      Z,$2D46             ; {}
2D45: AF              XOR     A                   
2D46: 2A F6 85        LD      HL,($85F6)          
2D49: 11 04 00        LD      DE,$0004            
2D4C: 19              ADD     HL,DE               
2D4D: BE              CP      (HL)                
2D4E: CA 99 2D        JP      Z,$2D99             ; {}
2D51: D2 59 2D        JP      NC,$2D59            ; {}
2D54: 3E 06           LD      A,$06               
2D56: C3 5B 2D        JP      $2D5B               ; {}
2D59: 3E 02           LD      A,$02               
2D5B: 23              INC     HL                  
2D5C: C3 88 2D        JP      $2D88               ; {}
2D5F: 2A F6 85        LD      HL,($85F6)          
2D62: CB 46           BIT     0,(HL)              
2D64: C2 60 2F        JP      NZ,$2F60            ; {}
2D67: 3A A3 98        LD      A,($98A3)           
2D6A: 21 F0 87        LD      HL,$87F0            
2D6D: CB 46           BIT     0,(HL)              
2D6F: CA 74 2D        JP      Z,$2D74             ; {}
2D72: 3E 08           LD      A,$08               
2D74: 2A F6 85        LD      HL,($85F6)          
2D77: 11 05 00        LD      DE,$0005            
2D7A: 19              ADD     HL,DE               
2D7B: BE              CP      (HL)                
2D7C: CA 99 2D        JP      Z,$2D99             ; {}
2D7F: D2 86 2D        JP      NC,$2D86            ; {}
2D82: AF              XOR     A                   
2D83: C3 88 2D        JP      $2D88               ; {}
2D86: 3E 04           LD      A,$04               
2D88: 11 0A 00        LD      DE,$000A            
2D8B: 19              ADD     HL,DE               
2D8C: 77              LD      (HL),A              
2D8D: E6 07           AND     $07                 
2D8F: 47              LD      B,A                 
2D90: 2B              DEC     HL                  
2D91: 7E              LD      A,(HL)              
2D92: C6 04           ADD     $04                 
2D94: E6 07           AND     $07                 
2D96: B8              CP      B                   
2D97: 20 03           JR      NZ,$1239            ; {}
2D99: 0E 00           LD      C,$00               
2D9B: C9              RET                         
2D9C: CD A0 2D        CALL    $2DA0               ; {}
2D9F: C9              RET                         
2DA0: 2A 1A 86        LD      HL,($861A)          
2DA3: 7E              LD      A,(HL)              
2DA4: E6 07           AND     $07                 
2DA6: 28 22           JR      Z,$1258             ; {}
2DA8: FE 02           CP      $02                 
2DAA: 28 35           JR      Z,$126B             ; {}
2DAC: FE 04           CP      $04                 
2DAE: 28 4B           JR      Z,$1281             ; {}
2DB0: 2A 02 86        LD      HL,($8602)          
2DB3: 22 12 86        LD      ($8612),HL          
2DB6: 11 20 00        LD      DE,$0020            
2DB9: 19              ADD     HL,DE               
2DBA: 22 16 86        LD      ($8616),HL          
2DBD: 2A 06 86        LD      HL,($8606)          
2DC0: 22 14 86        LD      ($8614),HL          
2DC3: 19              ADD     HL,DE               
2DC4: 22 18 86        LD      ($8618),HL          
2DC7: C3 5B 2E        JP      $2E5B               ; {}
2DCA: 2A 02 86        LD      HL,($8602)          
2DCD: 22 12 86        LD      ($8612),HL          
2DD0: 2B              DEC     HL                  
2DD1: 22 16 86        LD      ($8616),HL          
2DD4: 2A 04 86        LD      HL,($8604)          
2DD7: 22 14 86        LD      ($8614),HL          
2DDA: 2B              DEC     HL                  
2DDB: 22 18 86        LD      ($8618),HL          
2DDE: C3 19 2E        JP      $2E19               ; {}
2DE1: 2A 04 86        LD      HL,($8604)          
2DE4: 22 12 86        LD      ($8612),HL          
2DE7: 11 E0 FF        LD      DE,$FFE0            
2DEA: 19              ADD     HL,DE               
2DEB: 22 16 86        LD      ($8616),HL          
2DEE: 2A 08 86        LD      HL,($8608)          
2DF1: 22 14 86        LD      ($8614),HL          
2DF4: 19              ADD     HL,DE               
2DF5: 22 18 86        LD      ($8618),HL          
2DF8: C3 5B 2E        JP      $2E5B               ; {}
2DFB: 2A 06 86        LD      HL,($8606)          
2DFE: 22 12 86        LD      ($8612),HL          
2E01: 23              INC     HL                  
2E02: 22 16 86        LD      ($8616),HL          
2E05: 2A 08 86        LD      HL,($8608)          
2E08: 22 14 86        LD      ($8614),HL          
2E0B: 23              INC     HL                  
2E0C: 22 18 86        LD      ($8618),HL          
2E0F: 3A F0 87        LD      A,($87F0)           
2E12: CB 47           BIT     0,A                 
2E14: 28 03           JR      Z,$1239             ; {}
2E16: 0E 00           LD      C,$00               
2E18: C9              RET                         
2E19: 2A 12 86        LD      HL,($8612)          
2E1C: CD 3A 2E        CALL    $2E3A               ; {}
2E1F: 79              LD      A,C                 
2E20: FE 00           CP      $00                 
2E22: C8              RET     Z                   
2E23: 2A 14 86        LD      HL,($8614)          
2E26: CD 3A 2E        CALL    $2E3A               ; {}
2E29: 79              LD      A,C                 
2E2A: FE 00           CP      $00                 
2E2C: C8              RET     Z                   
2E2D: 2A 16 86        LD      HL,($8616)          
2E30: CD 3A 2E        CALL    $2E3A               ; {}
2E33: 79              LD      A,C                 
2E34: FE 00           CP      $00                 
2E36: C8              RET     Z                   
2E37: 2A 18 86        LD      HL,($8618)          
2E3A: 7E              LD      A,(HL)              
2E3B: FE 02           CP      $02                 
2E3D: 28 19           JR      Z,$124F             ; {}
2E3F: FE 03           CP      $03                 
2E41: 28 15           JR      Z,$124B             ; {}
2E43: FE 7E           CP      $7E                 
2E45: 28 11           JR      Z,$1247             ; {}
2E47: FE 8E           CP      $8E                 
2E49: 28 0D           JR      Z,$1243             ; {}
2E4B: FE 8F           CP      $8F                 
2E4D: 28 09           JR      Z,$123F             ; {}
2E4F: CB BF           RES     7,A                 
2E51: FE 0C           CP      $0C                 
2E53: 28 03           JR      Z,$1239             ; {}
2E55: 0E 00           LD      C,$00               
2E57: C9              RET                         
2E58: 0E 01           LD      C,$01               
2E5A: C9              RET                         
2E5B: 2A 12 86        LD      HL,($8612)          
2E5E: CD 7C 2E        CALL    $2E7C               ; {}
2E61: 79              LD      A,C                 
2E62: FE 00           CP      $00                 
2E64: C8              RET     Z                   
2E65: 2A 14 86        LD      HL,($8614)          
2E68: CD 7C 2E        CALL    $2E7C               ; {}
2E6B: 79              LD      A,C                 
2E6C: FE 00           CP      $00                 
2E6E: C8              RET     Z                   
2E6F: 2A 16 86        LD      HL,($8616)          
2E72: CD 7C 2E        CALL    $2E7C               ; {}
2E75: 79              LD      A,C                 
2E76: FE 00           CP      $00                 
2E78: C8              RET     Z                   
2E79: 2A 18 86        LD      HL,($8618)          
2E7C: 7E              LD      A,(HL)              
2E7D: FE 8D           CP      $8D                 
2E7F: CA 9B 2E        JP      Z,$2E9B             ; {}
2E82: FE 7E           CP      $7E                 
2E84: CA 9B 2E        JP      Z,$2E9B             ; {}
2E87: FE 08           CP      $08                 
2E89: CA 9B 2E        JP      Z,$2E9B             ; {}
2E8C: FE 09           CP      $09                 
2E8E: CA 9B 2E        JP      Z,$2E9B             ; {}
2E91: CB BF           RES     7,A                 
2E93: FE 0C           CP      $0C                 
2E95: CA 9B 2E        JP      Z,$2E9B             ; {}
2E98: 0E 00           LD      C,$00               
2E9A: C9              RET                         
2E9B: 0E 01           LD      C,$01               
2E9D: C9              RET                         
2E9E: 7E              LD      A,(HL)              
2E9F: FE 8C           CP      $8C                 
2EA1: CA C9 2E        JP      Z,$2EC9             ; {}
2EA4: FE 7E           CP      $7E                 
2EA6: CA C9 2E        JP      Z,$2EC9             ; {}
2EA9: FE 09           CP      $09                 
2EAB: CA C9 2E        JP      Z,$2EC9             ; {}
2EAE: FE 08           CP      $08                 
2EB0: CA C9 2E        JP      Z,$2EC9             ; {}
2EB3: FE 0C           CP      $0C                 
2EB5: CA C9 2E        JP      Z,$2EC9             ; {}
2EB8: FE 02           CP      $02                 
2EBA: CA C9 2E        JP      Z,$2EC9             ; {}
2EBD: FE 8D           CP      $8D                 
2EBF: CA C9 2E        JP      Z,$2EC9             ; {}
2EC2: FE 03           CP      $03                 
2EC4: CA C9 2E        JP      Z,$2EC9             ; {}
2EC7: AF              XOR     A                   
2EC8: C9              RET                         
2EC9: 3E 01           LD      A,$01               
2ECB: C9              RET                         
2ECC: E5              PUSH    HL                  
2ECD: 2A 1A 86        LD      HL,($861A)          
2ED0: 2B              DEC     HL                  
2ED1: 7E              LD      A,(HL)              
2ED2: E6 07           AND     $07                 
2ED4: FE 02           CP      $02                 
2ED6: CA E2 2E        JP      Z,$2EE2             ; {}
2ED9: FE 06           CP      $06                 
2EDB: CA F0 2E        JP      Z,$2EF0             ; {}
2EDE: 06 03           LD      B,$03               
2EE0: E1              POP     HL                  
2EE1: C9              RET                         
2EE2: 2A 02 86        LD      HL,($8602)          
2EE5: 22 36 86        LD      ($8636),HL          
2EE8: 2A 06 86        LD      HL,($8606)          
2EEB: 22 38 86        LD      ($8638),HL          
2EEE: 18 0C           JR      $1242               ; {}
2EF0: 2A 04 86        LD      HL,($8604)          
2EF3: 22 36 86        LD      ($8636),HL          
2EF6: 2A 08 86        LD      HL,($8608)          
2EF9: 22 38 86        LD      ($8638),HL          
2EFC: 06 03           LD      B,$03               
2EFE: 2A 1A 86        LD      HL,($861A)          
2F01: 2B              DEC     HL                  
2F02: 7E              LD      A,(HL)              
2F03: E6 07           AND     $07                 
2F05: FE 02           CP      $02                 
2F07: CA 12 2F        JP      Z,$2F12             ; {}
2F0A: FE 06           CP      $06                 
2F0C: CA 26 2F        JP      Z,$2F26             ; {}
2F0F: AF              XOR     A                   
2F10: E1              POP     HL                  
2F11: C9              RET                         
2F12: 11 C0 FF        LD      DE,$FFC0            
2F15: 2A 36 86        LD      HL,($8636)          
2F18: 19              ADD     HL,DE               
2F19: 22 36 86        LD      ($8636),HL          
2F1C: 2A 38 86        LD      HL,($8638)          
2F1F: 19              ADD     HL,DE               
2F20: 22 38 86        LD      ($8638),HL          
2F23: C3 2B 2F        JP      $2F2B               ; {}
2F26: 11 40 00        LD      DE,$0040            
2F29: 18 EA           JR      $1220               ; {}
2F2B: 2A 36 86        LD      HL,($8636)          
2F2E: CD 9E 2E        CALL    $2E9E               ; {}
2F31: CB 47           BIT     0,A                 
2F33: CA 43 2F        JP      Z,$2F43             ; {}
2F36: 2A 38 86        LD      HL,($8638)          
2F39: CD 9E 2E        CALL    $2E9E               ; {}
2F3C: CB 47           BIT     0,A                 
2F3E: CA 43 2F        JP      Z,$2F43             ; {}
2F41: 10 BB           DJNZ    $11F1               ; {}
2F43: 2A F6 85        LD      HL,($85F6)          
2F46: 11 08 00        LD      DE,$0008            
2F49: 19              ADD     HL,DE               
2F4A: 70              LD      (HL),B              
2F4B: E1              POP     HL                  
2F4C: C9              RET                         
2F4D: 3A A2 98        LD      A,($98A2)           
2F50: 2A F6 85        LD      HL,($85F6)          
2F53: 11 04 00        LD      DE,$0004            
2F56: 19              ADD     HL,DE               
2F57: BE              CP      (HL)                
2F58: D2 59 2D        JP      NC,$2D59            ; {}
2F5B: 3E 06           LD      A,$06               
2F5D: C3 5B 2D        JP      $2D5B               ; {}
2F60: 3A A3 98        LD      A,($98A3)           
2F63: 2A F6 85        LD      HL,($85F6)          
2F66: 11 05 00        LD      DE,$0005            
2F69: 19              ADD     HL,DE               
2F6A: BE              CP      (HL)                
2F6B: D2 86 2D        JP      NC,$2D86            ; {}
2F6E: AF              XOR     A                   
2F6F: C3 88 2D        JP      $2D88               ; {}
2F72: 2A F6 85        LD      HL,($85F6)          
2F75: 11 25 85        LD      DE,$8525            
2F78: A7              AND     A                   
2F79: ED 52           SBC     HL,DE               
2F7B: 7D              LD      A,L                 
2F7C: 0F              RRCA                        
2F7D: 0F              RRCA                        
2F7E: 0F              RRCA                        
2F7F: 0F              RRCA                        
2F80: E6 0F           AND     $0F                 
2F82: 5F              LD      E,A                 
2F83: 16 00           LD      D,$00               
2F85: 21 4B 86        LD      HL,$864B            
2F88: 19              ADD     HL,DE               
2F89: C9              RET                         
2F8A: CD 72 2F        CALL    $2F72               ; {}
2F8D: 36 03           LD      (HL),$03            
2F8F: C9              RET                         
2F90: CD 72 2F        CALL    $2F72               ; {}
2F93: 34              INC     (HL)                
2F94: C9              RET                         
2F95: 3E 50           LD      A,$50               
2F97: FD 77 00        LD      (IY+$00),A          
2F9A: FD 77 FE        LD      (IY+$FE),A          
2F9D: FD 77 FC        LD      (IY+$FC),A          
2FA0: AF              XOR     A                   
2FA1: DD 77 00        LD      (IX+$00),A          
2FA4: DD 77 FE        LD      (IX+$FE),A          
2FA7: DD 77 FC        LD      (IX+$FC),A          
2FAA: C9              RET                         
2FAB: 2E 00           LD      L,$00               
2FAD: 26 00           LD      H,$00               
2FAF: 11 23 30        LD      DE,$3023            
2FB2: 19              ADD     HL,DE               
2FB3: 11 11 84        LD      DE,$8411            
2FB6: 7E              LD      A,(HL)              
2FB7: 12              LD      (DE),A              
2FB8: 23              INC     HL                  
2FB9: 13              INC     DE                  
2FBA: 7E              LD      A,(HL)              
2FBB: 12              LD      (DE),A              
2FBC: 23              INC     HL                  
2FBD: 13              INC     DE                  
2FBE: 7E              LD      A,(HL)              
2FBF: 12              LD      (DE),A              
2FC0: 3A 57 86        LD      A,($8657)           
2FC3: CB 4F           BIT     1,A                 
2FC5: C0              RET     NZ                  
2FC6: 3A 81 9A        LD      A,($9A81)           
2FC9: FE 00           CP      $00                 
2FCB: C0              RET     NZ                  
2FCC: 11 11 84        LD      DE,$8411            
2FCF: 21 EF 89        LD      HL,$89EF            
2FD2: A7              AND     A                   
2FD3: 06 03           LD      B,$03               
2FD5: 1A              LD      A,(DE)              
2FD6: 8E              ADC     A,(HL)              
2FD7: 27              DAA                         
2FD8: 77              LD      (HL),A              
2FD9: 23              INC     HL                  
2FDA: 13              INC     DE                  
2FDB: 10 F8           DJNZ    $122E               ; {}
2FDD: 3E 00           LD      A,$00               
2FDF: 8E              ADC     A,(HL)              
2FE0: 27              DAA                         
2FE1: 77              LD      (HL),A              
2FE2: 3A 00 84        LD      A,($8400)           
2FE5: CB 4F           BIT     1,A                 
2FE7: 20 05           JR      NZ,$123B            ; {}
2FE9: 11 14 84        LD      DE,$8414            
2FEC: 18 03           JR      $1239               ; {}
2FEE: 11 17 84        LD      DE,$8417            
2FF1: 21 11 84        LD      HL,$8411            
2FF4: A7              AND     A                   
2FF5: 06 03           LD      B,$03               
2FF7: 1A              LD      A,(DE)              
2FF8: 8E              ADC     A,(HL)              
2FF9: 27              DAA                         
2FFA: 12              LD      (DE),A              
2FFB: 13              INC     DE                  
2FFC: 23              INC     HL                  
2FFD: 10 F8           DJNZ    $122E               ; {}
2FFF: 1B              DEC     DE                  
3000: EB              EX      DE,HL               
3001: 22 27 86        LD      ($8627),HL          
3004: 11 29 89        LD      DE,$8929            
3007: 06 03           LD      B,$03               
3009: 1A              LD      A,(DE)              
300A: BE              CP      (HL)                
300B: 20 05           JR      NZ,$123B            ; {}
300D: 2B              DEC     HL                  
300E: 1B              DEC     DE                  
300F: 10 F8           DJNZ    $122E               ; {}
3011: C9              RET                         
3012: D0              RET     NC                  
3013: 21 29 89        LD      HL,$8929            
3016: ED 5B 27 86     LD      DE,($8627)          
301A: 06 03           LD      B,$03               
301C: 1A              LD      A,(DE)              
301D: 77              LD      (HL),A              
301E: 2B              DEC     HL                  
301F: 1B              DEC     DE                  
3020: 10 FA           DJNZ    $1230               ; {}
3022: C9              RET                         
3023: 10 00           DJNZ    $1236               ; {}
3025: 00              NOP                         
3026: 00              NOP                         
3027: 02              LD      (BC),A              
3028: 00              NOP                         
3029: 00              NOP                         
302A: 03              INC     BC                  
302B: 00              NOP                         
302C: 00              NOP                         
302D: 04              INC     B                   
302E: 00              NOP                         
302F: 00              NOP                         
3030: 05              DEC     B                   
3031: 00              NOP                         
3032: 00              NOP                         
3033: 04              INC     B                   
3034: 00              NOP                         
3035: 00              NOP                         
3036: 06 00           LD      B,$00               
3038: 00              NOP                         
3039: 08              EX      AF,AF'              
303A: 00              NOP                         
303B: 00              NOP                         
303C: 10 00           DJNZ    $1236               ; {}
303E: 00              NOP                         
303F: 25              DEC     H                   
3040: 00              NOP                         
3041: 00              NOP                         
3042: 40              LD      B,B                 
3043: 00              NOP                         
3044: 00              NOP                         
3045: 60              LD      H,B                 
3046: 00              NOP                         
3047: 00              NOP                         
3048: 80              ADD     A,B                 
3049: 00              NOP                         
304A: 00              NOP                         
304B: 00              NOP                         
304C: 01 00 20        LD      BC,$2000            
304F: 01 00 50        LD      BC,$5000            
3052: 01 34 7F        LD      BC,$7F34            
3055: 32 1D 1A        LD      ($1A1D),A           ; {}
3058: 1E 2B           LD      E,$2B               
305A: 2D              DEC     L                   
305B: 22 1D 1E        LD      ($1E1D),HL          ; {}
305E: 2B              DEC     HL                  
305F: 1C              INC     E                   
3060: 7F              LD      A,A                 
3061: 2B              DEC     HL                  
3062: 28 2E           JR      Z,$1264             ; {}
3064: 27              DAA                         
3065: 1D              DEC     E                   
3066: 7F              LD      A,A                 
3067: 32 25 27        LD      ($2725),A           ; {}
306A: 28 7F           JR      Z,$12B5             ; {}
306C: 2B              DEC     HL                  
306D: 1E 32           LD      E,$32               
306F: 1A              LD      A,(DE)              
3070: 25              DEC     H                   
3071: 29              ADD     HL,HL               
3072: 7F              LD      A,A                 
3073: 51              LD      D,C                 
3074: 2C              INC     L                   
3075: 2B              DEC     HL                  
3076: 1E 32           LD      E,$32               
3078: 1A              LD      A,(DE)              
3079: 25              DEC     H                   
307A: 29              ADD     HL,HL               
307B: 7F              LD      A,A                 
307C: 52              LD      D,D                 
307D: 7F              LD      A,A                 
307E: 2B              DEC     HL                  
307F: 28 7F           JR      Z,$12B5             ; {}
3081: 51              LD      D,C                 
3082: 35              DEC     (HL)                
3083: 1D              DEC     E                   
3084: 2D              DEC     L                   
3085: 25              DEC     H                   
3086: 7F              LD      A,A                 
3087: 28 1C           JR      Z,$1252             ; {}
3089: 26 1A           LD      H,$1A               
308B: 27              DAA                         
308C: 7F              LD      A,A                 
308D: 12              LD      (DE),A              
308E: 18 19           JR      $124F               ; {}
3090: 11 7F 38        LD      DE,$387F            
3093: BF              CP      A                   
3094: BE              CP      (HL)                
3095: BD              CP      L                   
3096: BC              CP      H                   
3097: BB              CP      E                   
3098: BA              CP      D                   
3099: B9              CP      C                   
309A: 7F              LD      A,A                 
309B: 27              DAA                         
309C: 28 2D           JR      Z,$1263             ; {}
309E: 2D              DEC     L                   
309F: 2E 1B           LD      L,$1B               
30A1: 7F              LD      A,A                 
30A2: 2D              DEC     L                   
30A3: 2B              DEC     HL                  
30A4: 1A              LD      A,(DE)              
30A5: 2D              DEC     L                   
30A6: 2C              INC     L                   
30A7: 7F              LD      A,A                 
30A8: 21 2C 2E        LD      HL,$2E2C            
30AB: 29              ADD     HL,HL               
30AC: 35              DEC     (HL)                
30AD: 2C              INC     L                   
30AE: 2D              DEC     L                   
30AF: 29              ADD     HL,HL               
30B0: 7F              LD      A,A                 
30B1: 50              LD      D,B                 
30B2: 50              LD      D,B                 
30B3: 50              LD      D,B                 
30B4: 7F              LD      A,A                 
30B5: 7F              LD      A,A                 
30B6: 7F              LD      A,A                 
30B7: 2C              INC     L                   
30B8: 2E 27           LD      L,$27               
30BA: 28 1B           JR      Z,$1251             ; {}
30BC: 7F              LD      A,A                 
30BD: 2D              DEC     L                   
30BE: 2C              INC     L                   
30BF: 11 35 2C        LD      DE,$2C35            
30C2: 2D              DEC     L                   
30C3: 29              ADD     HL,HL               
30C4: 7F              LD      A,A                 
30C5: 50              LD      D,B                 
30C6: 50              LD      D,B                 
30C7: 50              LD      D,B                 
30C8: 7F              LD      A,A                 
30C9: 7F              LD      A,A                 
30CA: 7F              LD      A,A                 
30CB: 2C              INC     L                   
30CC: 2E 27           LD      L,$27               
30CE: 28 1B           JR      Z,$1251             ; {}
30D0: 7F              LD      A,A                 
30D1: 1D              DEC     E                   
30D2: 27              DAA                         
30D3: 12              LD      (DE),A              
30D4: 35              DEC     (HL)                
30D5: 2C              INC     L                   
30D6: 2D              DEC     L                   
30D7: 29              ADD     HL,HL               
30D8: 7F              LD      A,A                 
30D9: 50              LD      D,B                 
30DA: 50              LD      D,B                 
30DB: 50              LD      D,B                 
30DC: 7F              LD      A,A                 
30DD: 7F              LD      A,A                 
30DE: 7F              LD      A,A                 
30DF: 32 2B 1E        LD      ($1E2B),A           ; {}
30E2: 2F              CPL                         
30E3: 1E 7F           LD      E,$7F               
30E5: 1D              DEC     E                   
30E6: 27              DAA                         
30E7: 1A              LD      A,(DE)              
30E8: 00              NOP                         
30E9: 45              LD      B,L                 
30EA: AB              XOR     E                   
30EB: C4 00 00        CALL    NZ,$0000            ; {ram.$00}
30EE: 00              NOP                         
30EF: 00              NOP                         
30F0: 00              NOP                         
30F1: 33              INC     SP                  
30F2: 49              LD      C,C                 
30F3: 9D              SBC     L                   
30F4: C5              PUSH    BC                  
30F5: 00              NOP                         
30F6: 00              NOP                         
30F7: 00              NOP                         
30F8: 00              NOP                         
30F9: 33              INC     SP                  
30FA: 7C              LD      A,H                 
30FB: A4              AND     H                   
30FC: CD 00 00        CALL    $0000               ; {ram.$00}
30FF: 00              NOP                         
3100: 00              NOP                         
3101: 53              LD      D,E                 
3102: 6C              LD      L,H                 
3103: CD 94 3B        CALL    $3B94               ; {}
3106: 00              NOP                         
3107: 00              NOP                         
3108: 00              NOP                         
3109: 39              ADD     HL,SP               
310A: 4D              LD      C,L                 
310B: 73              LD      (HL),E              
310C: B6              OR      (HL)                
310D: CB 00           RLC     B                   
310F: 00              NOP                         
3110: 00              NOP                         
3111: A7              AND     A                   
3112: 38 7B           JR      C,$12B1             ; {}
3114: C3 00 00        JP      $0000               ; {ram.$00}
3117: 00              NOP                         
3118: 00              NOP                         
3119: 39              ADD     HL,SP               
311A: 62              LD      H,D                 
311B: 7D              LD      A,L                 
311C: BC              CP      H                   
311D: 00              NOP                         
311E: 00              NOP                         
311F: 00              NOP                         
3120: 00              NOP                         
3121: 7D              LD      A,L                 
3122: A6              AND     (HL)                
3123: 64              LD      H,H                 
3124: C8              RET     Z                   
3125: 00              NOP                         
3126: 00              NOP                         
3127: 00              NOP                         
3128: 00              NOP                         
3129: 4C              LD      C,H                 
312A: 38 8A           JR      C,$11C0             ; {}
312C: 82              ADD     A,D                 
312D: C6 00           ADD     $00                 
312F: 00              NOP                         
3130: 00              NOP                         
3131: 44              LD      B,H                 
3132: 9C              SBC     H                   
3133: C8              RET     Z                   
3134: 82              ADD     A,D                 
3135: 00              NOP                         
3136: 00              NOP                         
3137: 00              NOP                         
3138: 00              NOP                         
3139: 43              LD      B,E                 
313A: 4B              LD      C,E                 
313B: B6              OR      (HL)                
313C: CC 00 00        CALL    Z,$0000             ; {ram.$00}
313F: 00              NOP                         
3140: 00              NOP                         
3141: 49              LD      C,C                 
3142: 92              SUB     D                   
3143: 8B              ADC     A,E                 
3144: DA 00 00        JP      C,$0000             ; {ram.$00}
3147: 00              NOP                         
3148: 00              NOP                         
3149: 42              LD      B,D                 
314A: CA B3 39        JP      Z,$39B3             ; {}
314D: 00              NOP                         
314E: 00              NOP                         
314F: 00              NOP                         
3150: 00              NOP                         
3151: 5B              LD      E,E                 
3152: 93              SUB     E                   
3153: 42              LD      B,D                 
3154: C9              RET                         
3155: 00              NOP                         
3156: 00              NOP                         
3157: 00              NOP                         
3158: 00              NOP                         
3159: 62              LD      H,D                 
315A: C4 49 AA        CALL    NZ,$AA49            
315D: 00              NOP                         
315E: 00              NOP                         
315F: 00              NOP                         
3160: 46              LD      B,(HL)              
3161: 83              ADD     A,E                 
3162: 54              LD      D,H                 
3163: 81              ADD     A,C                 
3164: 00              NOP                         
3165: 00              NOP                         
3166: 00              NOP                         
3167: 00              NOP                         
3168: 86              ADD     A,(HL)              
3169: 80              ADD     A,B                 
316A: 56              LD      D,(HL)              
316B: 82              ADD     A,D                 
316C: 00              NOP                         
316D: 00              NOP                         
316E: 00              NOP                         
316F: 00              NOP                         
3170: 54              LD      D,H                 
3171: 83              ADD     A,E                 
3172: 00              NOP                         
3173: 00              NOP                         
3174: 00              NOP                         
3175: 00              NOP                         
3176: 00              NOP                         
3177: 00              NOP                         
3178: 94              SUB     H                   
3179: 81              ADD     A,C                 
317A: 88              ADC     A,B                 
317B: 80              ADD     A,B                 
317C: 98              SBC     B                   
317D: 80              ADD     A,B                 
317E: CE 82           ADC     $82                 
3180: C8              RET     Z                   
3181: 81              ADD     A,C                 
3182: 54              LD      D,H                 
3183: 82              ADD     A,D                 
3184: 00              NOP                         
3185: 00              NOP                         
3186: 00              NOP                         
3187: 00              NOP                         
3188: 1A              LD      A,(DE)              
3189: 81              ADD     A,C                 
318A: 86              ADD     A,(HL)              
318B: 80              ADD     A,B                 
318C: 00              NOP                         
318D: 00              NOP                         
318E: CC 82 D0        CALL    Z,$D082             
3191: 80              ADD     A,B                 
3192: C8              RET     Z                   
3193: 81              ADD     A,C                 
3194: 00              NOP                         
3195: 00              NOP                         
3196: 00              NOP                         
3197: 00              NOP                         
3198: 48              LD      C,B                 
3199: 82              ADD     A,D                 
319A: 56              LD      D,(HL)              
319B: 82              ADD     A,D                 
319C: 5A              LD      E,D                 
319D: 81              ADD     A,C                 
319E: 00              NOP                         
319F: 00              NOP                         
31A0: 48              LD      C,B                 
31A1: 82              ADD     A,D                 
31A2: 0E 81           LD      C,$81               
31A4: 46              LD      B,(HL)              
31A5: 81              ADD     A,C                 
31A6: 00              NOP                         
31A7: 00              NOP                         
31A8: 94              SUB     H                   
31A9: 82              ADD     A,D                 
31AA: C8              RET     Z                   
31AB: 82              ADD     A,D                 
31AC: 96              SUB     (HL)                
31AD: 80              ADD     A,B                 
31AE: 00              NOP                         
31AF: 00              NOP                         
31B0: 0C              INC     C                   
31B1: 83              ADD     A,E                 
31B2: 00              NOP                         
31B3: 00              NOP                         
31B4: 00              NOP                         
31B5: 00              NOP                         
31B6: 00              NOP                         
31B7: 00              NOP                         
31B8: D2 80 48        JP      NC,$4880            
31BB: 82              ADD     A,D                 
31BC: D4 82 D8        CALL    NC,$D882            
31BF: 81              ADD     A,C                 
31C0: 46              LD      B,(HL)              
31C1: 82              ADD     A,D                 
31C2: 00              NOP                         
31C3: 00              NOP                         
31C4: 00              NOP                         
31C5: 00              NOP                         
31C6: 00              NOP                         
31C7: 00              NOP                         
31C8: C8              RET     Z                   
31C9: 80              ADD     A,B                 
31CA: 18 81           JR      $11B7               ; {}
31CC: 94              SUB     H                   
31CD: 82              ADD     A,D                 
31CE: 00              NOP                         
31CF: 00              NOP                         
31D0: 48              LD      C,B                 
31D1: 82              ADD     A,D                 
31D2: 12              LD      (DE),A              
31D3: 83              ADD     A,E                 
31D4: 00              NOP                         
31D5: 00              NOP                         
31D6: 00              NOP                         
31D7: 00              NOP                         
31D8: 1A              LD      A,(DE)              
31D9: 82              ADD     A,D                 
31DA: C8              RET     Z                   
31DB: 82              ADD     A,D                 
31DC: CA 80 D6        JP      Z,$D680             
31DF: 80              ADD     A,B                 
31E0: 88              ADC     A,B                 
31E1: 82              ADD     A,D                 
31E2: 8C              ADC     A,H                 
31E3: 80              ADD     A,B                 
31E4: 00              NOP                         
31E5: 00              NOP                         
31E6: 00              NOP                         
31E7: 00              NOP                         
31E8: 98              SBC     B                   
31E9: 80              ADD     A,B                 
31EA: 0C              INC     C                   
31EB: 81              ADD     A,C                 
31EC: D8              RET     C                   
31ED: 82              ADD     A,D                 
31EE: D4 81 C6        CALL    NC,$C681            
31F1: 80              ADD     A,B                 
31F2: 4E              LD      C,(HL)              
31F3: 81              ADD     A,C                 
31F4: CC 82 00        CALL    Z,$0082             ; {}
31F7: 00              NOP                         
31F8: D8              RET     C                   
31F9: 80              ADD     A,B                 
31FA: 56              LD      D,(HL)              
31FB: 82              ADD     A,D                 
31FC: 4A              LD      C,D                 
31FD: 81              ADD     A,C                 
31FE: 00              NOP                         
31FF: 00              NOP                         
3200: 8E              ADC     A,(HL)              
3201: 80              ADD     A,B                 
3202: 4A              LD      C,D                 
3203: 81              ADD     A,C                 
3204: 14              INC     D                   
3205: 83              ADD     A,E                 
3206: 00              NOP                         
3207: 00              NOP                         
3208: 4A              LD      C,D                 
3209: 82              ADD     A,D                 
320A: CE 82           ADC     $82                 
320C: 00              NOP                         
320D: 00              NOP                         
320E: 00              NOP                         
320F: 00              NOP                         
3210: 8A              ADC     A,D                 
3211: 80              ADD     A,B                 
3212: 00              NOP                         
3213: 00              NOP                         
3214: 00              NOP                         
3215: 00              NOP                         
3216: 00              NOP                         
3217: 00              NOP                         
3218: D6 80           SUB     $80                 
321A: 4C              LD      C,H                 
321B: 81              ADD     A,C                 
321C: 18 82           JR      $11B8               ; {}
321E: 8A              ADC     A,D                 
321F: 82              ADD     A,D                 
3220: CE 80           ADC     $80                 
3222: CC 82 00        CALL    Z,$0082             ; {}
3225: 00              NOP                         
3226: 00              NOP                         
3227: 00              NOP                         
3228: C8              RET     Z                   
3229: 80              ADD     A,B                 
322A: D6 81           SUB     $81                 
322C: 9A              SBC     D                   
322D: 80              ADD     A,B                 
322E: 00              NOP                         
322F: 00              NOP                         
3230: C8              RET     Z                   
3231: 82              ADD     A,D                 
3232: 8A              ADC     A,D                 
3233: 80              ADD     A,B                 
3234: 00              NOP                         
3235: 00              NOP                         
3236: 00              NOP                         
3237: 00              NOP                         
3238: D2 80 48        JP      NC,$4880            
323B: 81              ADD     A,C                 
323C: 56              LD      D,(HL)              
323D: 82              ADD     A,D                 
323E: 00              NOP                         
323F: 00              NOP                         
3240: D4 81 48        CALL    NC,$4881            
3243: 82              ADD     A,D                 
3244: 54              LD      D,H                 
3245: 82              ADD     A,D                 
3246: 00              NOP                         
3247: 00              NOP                         
3248: 86              ADD     A,(HL)              
3249: 80              ADD     A,B                 
324A: CE 80           ADC     $80                 
324C: D0              RET     NC                  
324D: 82              ADD     A,D                 
324E: 00              NOP                         
324F: 00              NOP                         
3250: 32 3C DA        LD      ($DA3C),A           
3253: 00              NOP                         
3254: 00              NOP                         
3255: B4              OR      H                   
3256: 00              NOP                         
3257: 00              NOP                         
3258: A8              XOR     B                   
3259: 73              LD      (HL),E              
325A: B2              OR      D                   
325B: 00              NOP                         
325C: 00              NOP                         
325D: 00              NOP                         
325E: 4C              LD      C,H                 
325F: CC 58 63        CALL    Z,$6358             
3262: B6              OR      (HL)                
3263: 00              NOP                         
3264: 00              NOP                         
3265: 3C              INC     A                   
3266: DA 00 44        JP      C,$4400             
3269: D9              EXX                         
326A: 58              LD      E,B                 
326B: 00              NOP                         
326C: 00              NOP                         
326D: 8C              ADC     A,H                 
326E: B5              OR      L                   
326F: 00              NOP                         
3270: 4A              LD      C,D                 
3271: 56              LD      D,(HL)              
3272: 00              NOP                         
3273: 43              LD      B,E                 
3274: BC              CP      H                   
3275: 8B              ADC     A,E                 
3276: 00              NOP                         
3277: A4              AND     H                   
3278: 45              LD      B,L                 
3279: 45              LD      B,L                 
327A: 00              NOP                         
327B: 00              NOP                         
327C: 73              LD      (HL),E              
327D: 9B              SBC     E                   
327E: A3              AND     E                   
327F: C7              RST     0X00                
3280: 36 4B           LD      (HL),$4B            
3282: 46              LD      B,(HL)              
3283: A3              AND     E                   
3284: 4C              LD      C,H                 
3285: A5              AND     L                   
3286: 00              NOP                         
3287: CB 56           BIT     2,(HL)              
3289: 56              LD      D,(HL)              
328A: 5B              LD      E,E                 
328B: D6 00           SUB     $00                 
328D: BB              CP      E                   
328E: B3              OR      E                   
328F: 43              LD      B,E                 
3290: 7D              LD      A,L                 
3291: 55              LD      D,L                 
3292: 6A              LD      L,D                 
3293: 6A              LD      L,D                 
3294: C3 C3 A7        JP      $A7C3               
3297: CC 3C 59        CALL    Z,$593C             
329A: CB 3C           SRL     H                   
329C: 59              LD      E,C                 
329D: 74              LD      (HL),H              
329E: 7A              LD      A,D                 
329F: B5              OR      L                   
32A0: 73              LD      (HL),E              
32A1: 73              LD      (HL),E              
32A2: 7A              LD      A,D                 
32A3: 55              LD      D,L                 
32A4: 55              LD      D,L                 
32A5: 7D              LD      A,L                 
32A6: B3              OR      E                   
32A7: 7A              LD      A,D                 
32A8: 6D              LD      L,L                 
32A9: 54              LD      D,H                 
32AA: 69              LD      L,C                 
32AB: 69              LD      L,C                 
32AC: BB              CP      E                   
32AD: BB              CP      E                   
32AE: C6 54           ADD     $54                 
32B0: 4B              LD      C,E                 
32B1: 4B              LD      C,E                 
32B2: 7C              LD      A,H                 
32B3: 74              LD      (HL),H              
32B4: DB B8           IN      A,($B8)             ; {}
32B6: DB B8           IN      A,($B8)             ; {}
32B8: 6D              LD      L,L                 
32B9: 54              LD      D,H                 
32BA: 49              LD      C,C                 
32BB: 49              LD      C,C                 
32BC: 9A              SBC     D                   
32BD: 54              LD      D,H                 
32BE: B5              OR      L                   
32BF: B5              OR      L                   
32C0: 46              LD      B,(HL)              
32C1: 46              LD      B,(HL)              
32C2: 3C              INC     A                   
32C3: 7A              LD      A,D                 
32C4: 83              ADD     A,E                 
32C5: 83              ADD     A,E                 
32C6: B6              OR      (HL)                
32C7: B8              CP      B                   
32C8: 0C              INC     C                   
32C9: 14              INC     D                   
32CA: 0C              INC     C                   
32CB: 0F              RRCA                        
32CC: 11 0C 11        LD      DE,$110C            
32CF: 11 14 11        LD      DE,$1114            
32D2: 11 14 0C        LD      DE,$0C14            
32D5: 0C              INC     C                   
32D6: 14              INC     D                   
32D7: 24              INC     H                   
32D8: 24              INC     H                   
32D9: 20 20           JR      NZ,$1256            ; {}
32DB: 20 20           JR      NZ,$1256            ; {}
32DD: 1C              INC     E                   
32DE: 1C              INC     E                   
32DF: 1C              INC     E                   
32E0: 1C              INC     E                   
32E1: 1A              LD      A,(DE)              
32E2: 1A              LD      A,(DE)              
32E3: 1A              LD      A,(DE)              
32E4: 18 18           JR      $124E               ; {}
32E6: 1E 10           LD      E,$10               
32E8: ED 73 85 89     LD      ($8985),SP          
32EC: 32 88 89        LD      ($8988),A           
32EF: 3A A7 85        LD      A,($85A7)           
32F2: 32 87 89        LD      ($8987),A           
32F5: 11 82 89        LD      DE,$8982            
32F8: 06 03           LD      B,$03               
32FA: 7E              LD      A,(HL)              
32FB: 23              INC     HL                  
32FC: 12              LD      (DE),A              
32FD: 1B              DEC     DE                  
32FE: 10 FA           DJNZ    $1230               ; {}
3300: 3E 01           LD      A,$01               
3302: 32 3D 9B        LD      ($9B3D),A           
3305: 3A 3D 9B        LD      A,($9B3D)           
3308: A7              AND     A                   
3309: 20 FA           JR      NZ,$1230            ; {}
330B: 21 A0 89        LD      HL,$89A0            
330E: 06 05           LD      B,$05               
3310: 11 80 89        LD      DE,$8980            
3313: 0E 03           LD      C,$03               
3315: 1A              LD      A,(DE)              
3316: 96              SUB     (HL)                
3317: 38 14           JR      C,$124A             ; {}
3319: 20 07           JR      NZ,$123D            ; {}
331B: 23              INC     HL                  
331C: 13              INC     DE                  
331D: 0D              DEC     C                   
331E: 20 F5           JR      NZ,$122B            ; {}
3320: 18 0B           JR      $1241               ; {}
3322: 23              INC     HL                  
3323: 0D              DEC     C                   
3324: 20 FC           JR      NZ,$1232            ; {}
3326: 10 E8           DJNZ    $121E               ; {}
3328: CD 33 35        CALL    $3533               ; {}
332B: 06 00           LD      B,$00               
332D: 04              INC     B                   
332E: 78              LD      A,B                 
332F: 32 C5 89        LD      ($89C5),A           
3332: FE 06           CP      $06                 
3334: 20 05           JR      NZ,$123B            ; {}
3336: ED 7B 85 89     LD      SP,($8985)          
333A: C9              RET                         
333B: 3E 05           LD      A,$05               
333D: 90              SUB     B                   
333E: 28 1F           JR      Z,$1255             ; {}
3340: 4F              LD      C,A                 
3341: 06 00           LD      B,$00               
3343: 21 C1 89        LD      HL,$89C1            
3346: 11 C0 89        LD      DE,$89C0            
3349: 87              ADD     A,A                 
334A: 81              ADD     A,C                 
334B: ED B0           LDIR                        
334D: 21 A3 89        LD      HL,$89A3            
3350: 11 A0 89        LD      DE,$89A0            
3353: 4F              LD      C,A                 
3354: ED B0           LDIR                        
3356: 4F              LD      C,A                 
3357: 21 B3 89        LD      HL,$89B3            
335A: 11 B0 89        LD      DE,$89B0            
335D: ED B0           LDIR                        
335F: 4F              LD      C,A                 
3360: 21 A0 89        LD      HL,$89A0            
3363: 06 00           LD      B,$00               
3365: 09              ADD     HL,BC               
3366: EB              EX      DE,HL               
3367: 21 80 89        LD      HL,$8980            
336A: 0E 03           LD      C,$03               
336C: ED B0           LDIR                        
336E: 21 B0 89        LD      HL,$89B0            
3371: 4F              LD      C,A                 
3372: 09              ADD     HL,BC               
3373: 06 03           LD      B,$03               
3375: 36 37           LD      (HL),$37            
3377: 23              INC     HL                  
3378: 10 FB           DJNZ    $1231               ; {}
337A: 3A C5 89        LD      A,($89C5)           
337D: D6 05           SUB     $05                 
337F: ED 44           NEG                         
3381: 4F              LD      C,A                 
3382: 21 C0 89        LD      HL,$89C0            
3385: 09              ADD     HL,BC               
3386: 3A 88 89        LD      A,($8988)           
3389: 77              LD      (HL),A              
338A: 21 A8 85        LD      HL,$85A8            
338D: 3A 00 84        LD      A,($8400)           
3390: F6 F9           OR      $F9                 
3392: 3C              INC     A                   
3393: 20 01           JR      NZ,$1237            ; {}
3395: 23              INC     HL                  
3396: 22 C7 89        LD      ($89C7),HL          
3399: CD 21 3E        CALL    $3E21               ; {}
339C: 21 25 37        LD      HL,$3725            
339F: CD EB 36        CALL    $36EB               ; {}
33A2: CD EB 36        CALL    $36EB               ; {}
33A5: CD EB 36        CALL    $36EB               ; {}
33A8: 21 80 89        LD      HL,$8980            
33AB: 11 2F 83        LD      DE,$832F            
33AE: 01 00 03        LD      BC,$0300            
33B1: CD BE 36        CALL    $36BE               ; {}
33B4: 06 05           LD      B,$05               
33B6: CD E1 36        CALL    $36E1               ; {}
33B9: 10 FB           DJNZ    $1231               ; {}
33BB: 3A 88 89        LD      A,($8988)           
33BE: 0E 10           LD      C,$10               
33C0: CD 59 36        CALL    $3659               ; {}
33C3: 21 2F 81        LD      HL,$812F            
33C6: 22 C9 89        LD      ($89C9),HL          
33C9: AF              XOR     A                   
33CA: 32 C6 89        LD      ($89C6),A           
33CD: 21 28 F0        LD      HL,$F028            
33D0: 22 CD 89        LD      ($89CD),HL          
33D3: CD DF 35        CALL    $35DF               ; {}
33D6: CD E6 34        CALL    $34E6               ; {}
33D9: 3E FF           LD      A,$FF               
33DB: 32 94 9A        LD      ($9A94),A           
33DE: 06 02           LD      B,$02               
33E0: CD D5 34        CALL    $34D5               ; {}
33E3: 3A 23 84        LD      A,($8423)           
33E6: 4F              LD      C,A                 
33E7: CD E6 34        CALL    $34E6               ; {}
33EA: 3A 23 84        LD      A,($8423)           
33ED: B9              CP      C                   
33EE: 28 F7           JR      Z,$122D             ; {}
33F0: E6 0F           AND     $0F                 
33F2: CC 11 35        CALL    Z,$3511             ; {}
33F5: 2A C7 89        LD      HL,($89C7)          
33F8: CB 66           BIT     4,(HL)              
33FA: CC 7A 34        CALL    Z,$347A             ; {}
33FD: 2A C7 89        LD      HL,($89C7)          
3400: 7E              LD      A,(HL)              
3401: E6 0E           AND     $0E                 
3403: 21 84 89        LD      HL,$8984            
3406: BE              CP      (HL)                
3407: 77              LD      (HL),A              
3408: 28 1A           JR      Z,$1250             ; {}
340A: FE 02           CP      $02                 
340C: 28 0F           JR      Z,$1245             ; {}
340E: FE 0C           CP      $0C                 
3410: 28 0B           JR      Z,$1241             ; {}
3412: FE 06           CP      $06                 
3414: 20 CD           JR      NZ,$1203            ; {}
3416: 3E FD           LD      A,$FD               
3418: 32 CB 89        LD      ($89CB),A           
341B: 18 3A           JR      $1270               ; {}
341D: 3E FD           LD      A,$FD               
341F: 32 CC 89        LD      ($89CC),A           
3422: 18 0C           JR      $1242               ; {}
3424: FE 06           CP      $06                 
3426: 28 2F           JR      Z,$1265             ; {}
3428: FE 0C           CP      $0C                 
342A: 28 04           JR      Z,$123A             ; {}
342C: FE 02           CP      $02                 
342E: 20 B3           JR      NZ,$11E9            ; {}
3430: 21 CC 89        LD      HL,$89CC            
3433: 34              INC     (HL)                
3434: 20 AD           JR      NZ,$11E3            ; {}
3436: 36 F0           LD      (HL),$F0            
3438: 3E 28           LD      A,$28               
343A: 32 CD 89        LD      ($89CD),A           
343D: 2A C9 89        LD      HL,($89C9)          
3440: 34              INC     (HL)                
3441: 7E              LD      A,(HL)              
3442: E6 3F           AND     $3F                 
3444: FE 34           CP      $34                 
3446: 38 05           JR      C,$123B             ; {}
3448: FE 38           CP      $38                 
344A: 30 07           JR      NC,$123D            ; {}
344C: 34              INC     (HL)                
344D: CD DF 35        CALL    $35DF               ; {}
3450: C3 E3 33        JP      $33E3               ; {}
3453: 36 1A           LD      (HL),$1A            
3455: 18 F6           JR      $122C               ; {}
3457: 21 CB 89        LD      HL,$89CB            
345A: 34              INC     (HL)                
345B: 20 F3           JR      NZ,$1229            ; {}
345D: 36 F0           LD      (HL),$F0            
345F: 3E 28           LD      A,$28               
3461: 32 CD 89        LD      ($89CD),A           
3464: 2A C9 89        LD      HL,($89C9)          
3467: 35              DEC     (HL)                
3468: 7E              LD      A,(HL)              
3469: E6 3F           AND     $3F                 
346B: FE 19           CP      $19                 
346D: 28 07           JR      Z,$123D             ; {}
346F: FE 34           CP      $34                 
3471: 38 DA           JR      C,$1210             ; {}
3473: 35              DEC     (HL)                
3474: 18 D7           JR      $120D               ; {}
3476: 36 37           LD      (HL),$37            
3478: 18 D3           JR      $1209               ; {}
347A: 2A C9 89        LD      HL,($89C9)          
347D: CB BE           RES     7,(HL)              
347F: 4E              LD      C,(HL)              
3480: EB              EX      DE,HL               
3481: CD E1 36        CALL    $36E1               ; {}
3484: ED 53 C9 89     LD      ($89C9),DE          
3488: 3E 28           LD      A,$28               
348A: 32 CD 89        LD      ($89CD),A           
348D: 3A C6 89        LD      A,($89C6)           
3490: 5F              LD      E,A                 
3491: 3C              INC     A                   
3492: 32 C6 89        LD      ($89C6),A           
3495: 47              LD      B,A                 
3496: 16 00           LD      D,$00               
3498: 3A C5 89        LD      A,($89C5)           
349B: 21 27 35        LD      HL,$3527            
349E: CF              RST     0X08                
349F: 7E              LD      A,(HL)              
34A0: 23              INC     HL                  
34A1: 66              LD      H,(HL)              
34A2: 6F              LD      L,A                 
34A3: 19              ADD     HL,DE               
34A4: 71              LD      (HL),C              
34A5: 78              LD      A,B                 
34A6: FE 03           CP      $03                 
34A8: C2 DF 35        JP      NZ,$35DF            ; {}
34AB: ED 7B 85 89     LD      SP,($8985)          
34AF: CD DF 35        CALL    $35DF               ; {}
34B2: CD F4 34        CALL    $34F4               ; {}
34B5: 3E 01           LD      A,$01               
34B7: 32 94 9A        LD      ($9A94),A           
34BA: 06 04           LD      B,$04               
34BC: CD D5 34        CALL    $34D5               ; {}
34BF: 3A 94 9A        LD      A,($9A94)           
34C2: A7              AND     A                   
34C3: 20 FA           JR      NZ,$1230            ; {}
34C5: 3E 02           LD      A,$02               
34C7: 32 3D 9B        LD      ($9B3D),A           
34CA: 3A 3D 9B        LD      A,($9B3D)           
34CD: A7              AND     A                   
34CE: 20 FA           JR      NZ,$1230            ; {}
34D0: ED 7B 85 89     LD      SP,($8985)          
34D4: C9              RET                         
34D5: 3A 23 84        LD      A,($8423)           
34D8: E6 3F           AND     $3F                 
34DA: 20 F9           JR      NZ,$122F            ; {}
34DC: 3A 23 84        LD      A,($8423)           
34DF: E6 3F           AND     $3F                 
34E1: 28 F9           JR      Z,$122F             ; {}
34E3: 10 F0           DJNZ    $1226               ; {}
34E5: C9              RET                         
34E6: 3A A7 85        LD      A,($85A7)           
34E9: 5F              LD      E,A                 
34EA: 3A 87 89        LD      A,($8987)           
34ED: BB              CP      E                   
34EE: C8              RET     Z                   
34EF: CD 7A 34        CALL    $347A               ; {}
34F2: 18 FB           JR      $1231               ; {}
34F4: 3A A7 85        LD      A,($85A7)           
34F7: 5F              LD      E,A                 
34F8: 3A 87 89        LD      A,($8987)           
34FB: BB              CP      E                   
34FC: C8              RET     Z                   
34FD: 3A 94 9A        LD      A,($9A94)           
3500: A7              AND     A                   
3501: 28 C2           JR      Z,$11F8             ; {}
3503: 3E 01           LD      A,$01               
3505: 32 94 9A        LD      ($9A94),A           
3508: 3A 94 9A        LD      A,($9A94)           
350B: A7              AND     A                   
350C: 28 FA           JR      Z,$1230             ; {}
350E: 18 B5           JR      $11EB               ; {}
3510: C9              RET                         
3511: 2A C9 89        LD      HL,($89C9)          
3514: 7E              LD      A,(HL)              
3515: EE 80           XOR     $80                 
3517: 77              LD      (HL),A              
3518: 3A 23 84        LD      A,($8423)           
351B: E6 1F           AND     $1F                 
351D: C0              RET     NZ                  
351E: 21 CD 89        LD      HL,$89CD            
3521: 35              DEC     (HL)                
3522: 28 CB           JR      Z,$1201             ; {}
3524: 23              INC     HL                  
3525: 35              DEC     (HL)                
3526: 28 C7           JR      Z,$11FD             ; {}
3528: C9              RET                         
3529: BC              CP      H                   
352A: 89              ADC     A,C                 
352B: B9              CP      C                   
352C: 89              ADC     A,C                 
352D: B6              OR      (HL)                
352E: 89              ADC     A,C                 
352F: B3              OR      E                   
3530: 89              ADC     A,C                 
3531: B0              OR      B                   
3532: 89              ADC     A,C                 
3533: CD 21 3E        CALL    $3E21               ; {}
3536: 21 6F 37        LD      HL,$376F            
3539: CD EB 36        CALL    $36EB               ; {}
353C: CD EB 36        CALL    $36EB               ; {}
353F: CD EB 36        CALL    $36EB               ; {}
3542: CD EB 36        CALL    $36EB               ; {}
3545: 3E 01           LD      A,$01               
3547: 32 82 9A        LD      ($9A82),A           
354A: 3A 23 84        LD      A,($8423)           
354D: E6 1F           AND     $1F                 
354F: CC 6D 35        CALL    Z,$356D             ; {}
3552: E6 0F           AND     $0F                 
3554: CC C1 35        CALL    Z,$35C1             ; {}
3557: 3A 82 9A        LD      A,($9A82)           
355A: A7              AND     A                   
355B: 20 ED           JR      NZ,$1223            ; {}
355D: CD 6D 35        CALL    $356D               ; {}
3560: 3A 23 84        LD      A,($8423)           
3563: C6 3C           ADD     $3C                 
3565: 4F              LD      C,A                 
3566: 3A 23 84        LD      A,($8423)           
3569: B9              CP      C                   
356A: 20 FA           JR      NZ,$1230            ; {}
356C: C9              RET                         
356D: 21 80 89        LD      HL,$8980            
3570: 11 6D 83        LD      DE,$836D            
3573: 06 03           LD      B,$03               
3575: AF              XOR     A                   
3576: 32 83 89        LD      ($8983),A           
3579: 7E              LD      A,(HL)              
357A: 1F              RRA                         
357B: 1F              RRA                         
357C: 1F              RRA                         
357D: 1F              RRA                         
357E: CD 8B 35        CALL    $358B               ; {}
3581: 7E              LD      A,(HL)              
3582: CD 8B 35        CALL    $358B               ; {}
3585: 23              INC     HL                  
3586: 10 F1           DJNZ    $1227               ; {}
3588: 3E 01           LD      A,$01               
358A: C9              RET                         
358B: E6 0F           AND     $0F                 
358D: 20 0E           JR      NZ,$1244            ; {}
358F: 3A 83 89        LD      A,($8983)           
3592: A7              AND     A                   
3593: 3E 00           LD      A,$00               
3595: 20 06           JR      NZ,$123C            ; {}
3597: CD E1 36        CALL    $36E1               ; {}
359A: C3 E1 36        JP      $36E1               ; {}
359D: E5              PUSH    HL                  
359E: C5              PUSH    BC                  
359F: 21 C2 37        LD      HL,$37C2            
35A2: CF              RST     0X08                
35A3: 7E              LD      A,(HL)              
35A4: 23              INC     HL                  
35A5: 66              LD      H,(HL)              
35A6: 6F              LD      L,A                 
35A7: 01 FF 04        LD      BC,$04FF            
35AA: D5              PUSH    DE                  
35AB: ED A0           LDI                         
35AD: ED A0           LDI                         
35AF: ED A0           LDI                         
35B1: ED A0           LDI                         
35B3: D1              POP     DE                  
35B4: CD E1 36        CALL    $36E1               ; {}
35B7: 10 F1           DJNZ    $1227               ; {}
35B9: C1              POP     BC                  
35BA: E1              POP     HL                  
35BB: 3E 01           LD      A,$01               
35BD: 32 83 89        LD      ($8983),A           
35C0: C9              RET                         
35C1: 11 6D 83        LD      DE,$836D            
35C4: CD CD 35        CALL    $35CD               ; {}
35C7: CD CD 35        CALL    $35CD               ; {}
35CA: CD CD 35        CALL    $35CD               ; {}
35CD: D5              PUSH    DE                  
35CE: 06 18           LD      B,$18               
35D0: 3E 40           LD      A,$40               
35D2: 12              LD      (DE),A              
35D3: CD E1 36        CALL    $36E1               ; {}
35D6: 10 F8           DJNZ    $122E               ; {}
35D8: D1              POP     DE                  
35D9: 13              INC     DE                  
35DA: C9              RET                         
35DB: AF              XOR     A                   
35DC: 32 C5 89        LD      ($89C5),A           
35DF: 21 5B 37        LD      HL,$375B            
35E2: CD EB 36        CALL    $36EB               ; {}
35E5: 11 5D 83        LD      DE,$835D            
35E8: 06 05           LD      B,$05               
35EA: CD F0 35        CALL    $35F0               ; {}
35ED: 10 FB           DJNZ    $1231               ; {}
35EF: C9              RET                         
35F0: 0E 00           LD      C,$00               
35F2: 3A C5 89        LD      A,($89C5)           
35F5: B8              CP      B                   
35F6: 20 02           JR      NZ,$1238            ; {}
35F8: 0E 40           LD      C,$40               
35FA: 78              LD      A,B                 
35FB: 21 85 36        LD      HL,$3685            
35FE: CF              RST     0X08                
35FF: 7E              LD      A,(HL)              
3600: 23              INC     HL                  
3601: 66              LD      H,(HL)              
3602: 6F              LD      L,A                 
3603: D5              PUSH    DE                  
3604: C5              PUSH    BC                  
3605: 06 03           LD      B,$03               
3607: 7E              LD      A,(HL)              
3608: B1              OR      C                   
3609: 12              LD      (DE),A              
360A: 23              INC     HL                  
360B: CD E1 36        CALL    $36E1               ; {}
360E: 10 F7           DJNZ    $122D               ; {}
3610: CD E1 36        CALL    $36E1               ; {}
3613: CD E1 36        CALL    $36E1               ; {}
3616: CD 3D 36        CALL    $363D               ; {}
3619: 06 04           LD      B,$04               
361B: CD E1 36        CALL    $36E1               ; {}
361E: 10 FB           DJNZ    $1231               ; {}
3620: CD 5C 36        CALL    $365C               ; {}
3623: CD E1 36        CALL    $36E1               ; {}
3626: CD E1 36        CALL    $36E1               ; {}
3629: 7E              LD      A,(HL)              
362A: 23              INC     HL                  
362B: 66              LD      H,(HL)              
362C: 6F              LD      L,A                 
362D: 06 03           LD      B,$03               
362F: 7E              LD      A,(HL)              
3630: B1              OR      C                   
3631: 12              LD      (DE),A              
3632: CD E1 36        CALL    $36E1               ; {}
3635: 23              INC     HL                  
3636: 10 F7           DJNZ    $122D               ; {}
3638: C1              POP     BC                  
3639: D1              POP     DE                  
363A: 1B              DEC     DE                  
363B: 1B              DEC     DE                  
363C: C9              RET                         
363D: 7E              LD      A,(HL)              
363E: 23              INC     HL                  
363F: E5              PUSH    HL                  
3640: 66              LD      H,(HL)              
3641: 6F              LD      L,A                 
3642: C5              PUSH    BC                  
3643: D5              PUSH    DE                  
3644: 01 00 03        LD      BC,$0300            
3647: CD BE 36        CALL    $36BE               ; {}
364A: D1              POP     DE                  
364B: C1              POP     BC                  
364C: 06 06           LD      B,$06               
364E: 1A              LD      A,(DE)              
364F: B1              OR      C                   
3650: 12              LD      (DE),A              
3651: CD E1 36        CALL    $36E1               ; {}
3654: 10 F8           DJNZ    $122E               ; {}
3656: E1              POP     HL                  
3657: 23              INC     HL                  
3658: C9              RET                         
3659: E5              PUSH    HL                  
365A: 18 06           JR      $123C               ; {}
365C: 7E              LD      A,(HL)              
365D: 23              INC     HL                  
365E: E5              PUSH    HL                  
365F: 66              LD      H,(HL)              
3660: 6F              LD      L,A                 
3661: 7E              LD      A,(HL)              
3662: 06 00           LD      B,$00               
3664: D6 0A           SUB     $0A                 
3666: 38 03           JR      C,$1239             ; {}
3668: 04              INC     B                   
3669: 18 F9           JR      $122F               ; {}
366B: F5              PUSH    AF                  
366C: 78              LD      A,B                 
366D: CD 79 36        CALL    $3679               ; {}
3670: F1              POP     AF                  
3671: C6 0A           ADD     $0A                 
3673: CD 7F 36        CALL    $367F               ; {}
3676: E1              POP     HL                  
3677: 23              INC     HL                  
3678: C9              RET                         
3679: E6 0F           AND     $0F                 
367B: 20 02           JR      NZ,$1238            ; {}
367D: 3E 27           LD      A,$27               
367F: C6 10           ADD     $10                 
3681: B1              OR      C                   
3682: 12              LD      (DE),A              
3683: CD E1 36        CALL    $36E1               ; {}
3686: C9              RET                         
3687: 91              SUB     C                   
3688: 36 9A           LD      (HL),$9A            
368A: 36 A3           LD      (HL),$A3            
368C: 36 AC           LD      (HL),$AC            
368E: 36 B5           LD      (HL),$B5            
3690: 36 11           LD      (HL),$11            
3692: 2C              INC     L                   
3693: 2D              DEC     L                   
3694: AC              XOR     H                   
3695: 89              ADC     A,C                 
3696: C4 89 BC        CALL    NZ,$BC89            
3699: 89              ADC     A,C                 
369A: 12              LD      (DE),A              
369B: 27              DAA                         
369C: 1D              DEC     E                   
369D: A9              XOR     C                   
369E: 89              ADC     A,C                 
369F: C3 89 B9        JP      $B989               
36A2: 89              ADC     A,C                 
36A3: 13              INC     DE                  
36A4: 2B              DEC     HL                  
36A5: 1D              DEC     E                   
36A6: A6              AND     (HL)                
36A7: 89              ADC     A,C                 
36A8: C2 89 B6        JP      NZ,$B689            
36AB: 89              ADC     A,C                 
36AC: 14              INC     D                   
36AD: 2D              DEC     L                   
36AE: 21 A3 89        LD      HL,$89A3            
36B1: C1              POP     BC                  
36B2: 89              ADC     A,C                 
36B3: B3              OR      E                   
36B4: 89              ADC     A,C                 
36B5: 15              DEC     D                   
36B6: 2D              DEC     L                   
36B7: 21 A0 89        LD      HL,$89A0            
36BA: C0              RET     NZ                  
36BB: 89              ADC     A,C                 
36BC: B0              OR      B                   
36BD: 89              ADC     A,C                 
36BE: 7E              LD      A,(HL)              
36BF: CD C6 36        CALL    $36C6               ; {}
36C2: 23              INC     HL                  
36C3: 10 F9           DJNZ    $122F               ; {}
36C5: C9              RET                         
36C6: F5              PUSH    AF                  
36C7: 1F              RRA                         
36C8: 1F              RRA                         
36C9: 1F              RRA                         
36CA: 1F              RRA                         
36CB: CD D4 36        CALL    $36D4               ; {}
36CE: F1              POP     AF                  
36CF: 10 02           DJNZ    $1238               ; {}
36D1: 0E FF           LD      C,$FF               
36D3: 04              INC     B                   
36D4: E6 0F           AND     $0F                 
36D6: 28 02           JR      Z,$1238             ; {}
36D8: 0E FF           LD      C,$FF               
36DA: F6 10           OR      $10                 
36DC: A1              AND     C                   
36DD: CC E8 36        CALL    Z,$36E8             ; {}
36E0: 12              LD      (DE),A              
36E1: 7B              LD      A,E                 
36E2: D6 20           SUB     $20                 
36E4: 5F              LD      E,A                 
36E5: D0              RET     NC                  
36E6: 15              DEC     D                   
36E7: C9              RET                         
36E8: 3E 37           LD      A,$37               
36EA: C9              RET                         
36EB: 4E              LD      C,(HL)              
36EC: 23              INC     HL                  
36ED: 46              LD      B,(HL)              
36EE: 23              INC     HL                  
36EF: 5E              LD      E,(HL)              
36F0: 23              INC     HL                  
36F1: 56              LD      D,(HL)              
36F2: 23              INC     HL                  
36F3: 7E              LD      A,(HL)              
36F4: CD 04 37        CALL    $3704               ; {}
36F7: FE FF           CP      $FF                 
36F9: 28 05           JR      Z,$123B             ; {}
36FB: 81              ADD     A,C                 
36FC: 12              LD      (DE),A              
36FD: CD E1 36        CALL    $36E1               ; {}
3700: 23              INC     HL                  
3701: 10 F0           DJNZ    $1226               ; {}
3703: C9              RET                         
3704: D6 30           SUB     $30                 
3706: FE 0A           CP      $0A                 
3708: D8              RET     C                   
3709: D6 07           SUB     $07                 
370B: FE 23           CP      $23                 
370D: D8              RET     C                   
370E: C6 3E           ADD     $3E                 
3710: FE 27           CP      $27                 
3712: C8              RET     Z                   
3713: C6 FC           ADD     $FC                 
3715: FE 24           CP      $24                 
3717: C8              RET     Z                   
3718: C6 F4           ADD     $F4                 
371A: FE 25           CP      $25                 
371C: C8              RET     Z                   
371D: C6 08           ADD     $08                 
371F: FE 26           CP      $26                 
3721: C8              RET     Z                   
3722: 3E FF           LD      A,$FF               
3724: C9              RET                         
3725: 50              LD      D,B                 
3726: 15              DEC     D                   
3727: 2A 83 45        LD      HL,($4583)          
372A: 4E              LD      C,(HL)              
372B: 54              LD      D,H                 
372C: 45              LD      B,L                 
372D: 52              LD      D,D                 
372E: 20 59           JR      NZ,$128F            ; {}
3730: 4F              LD      C,A                 
3731: 55              LD      D,L                 
3732: 52              LD      D,D                 
3733: 20 49           JR      NZ,$127F            ; {}
3735: 4E              LD      C,(HL)              
3736: 49              LD      C,C                 
3737: 54              LD      D,H                 
3738: 49              LD      C,C                 
3739: 41              LD      B,C                 
373A: 4C              LD      C,H                 
373B: 53              LD      D,E                 
373C: 20 21           JR      NZ,$1257            ; {}
373E: 50              LD      D,B                 
373F: 12              LD      (DE),A              
3740: 0D              DEC     C                   
3741: 83              ADD     A,E                 
3742: 53              LD      D,E                 
3743: 43              LD      B,E                 
3744: 4F              LD      C,A                 
3745: 52              LD      D,D                 
3746: 45              LD      B,L                 
3747: 20 20           JR      NZ,$1256            ; {}
3749: 52              LD      D,D                 
374A: 4F              LD      C,A                 
374B: 55              LD      D,L                 
374C: 4E              LD      C,(HL)              
374D: 44              LD      B,H                 
374E: 20 20           JR      NZ,$1256            ; {}
3750: 4E              LD      C,(HL)              
3751: 41              LD      B,C                 
3752: 4D              LD      C,L                 
3753: 45              LD      B,L                 
3754: 10 03           DJNZ    $1239               ; {}
3756: 2F              CPL                         
3757: 81              ADD     A,C                 
3758: 41              LD      B,C                 
3759: 41              LD      B,C                 
375A: 41              LD      B,C                 
375B: 10 10           DJNZ    $1246               ; {}
375D: 93              SUB     E                   
375E: 82              ADD     A,D                 
375F: 53              LD      D,E                 
3760: 43              LD      B,E                 
3761: 4F              LD      C,A                 
3762: 52              LD      D,D                 
3763: 45              LD      B,L                 
3764: 20 52           JR      NZ,$1288            ; {}
3766: 4F              LD      C,A                 
3767: 55              LD      D,L                 
3768: 4E              LD      C,(HL)              
3769: 44              LD      B,H                 
376A: 20 4E           JR      NZ,$1284            ; {}
376C: 41              LD      B,C                 
376D: 4D              LD      C,L                 
376E: 45              LD      B,L                 
376F: 90              SUB     B                   
3770: 12              LD      (DE),A              
3771: 04              INC     B                   
3772: 83              ADD     A,E                 
3773: 43              LD      B,E                 
3774: 4F              LD      C,A                 
3775: 4E              LD      C,(HL)              
3776: 47              LD      B,A                 
3777: 52              LD      D,D                 
3778: 41              LD      B,C                 
3779: 54              LD      D,H                 
377A: 55              LD      D,L                 
377B: 4C              LD      C,H                 
377C: 41              LD      B,C                 
377D: 54              LD      D,H                 
377E: 49              LD      C,C                 
377F: 4F              LD      C,A                 
3780: 4E              LD      C,(HL)              
3781: 53              LD      D,E                 
3782: 20 21           JR      NZ,$1257            ; {}
3784: 21 50 15        LD      HL,$1550            
3787: 27              DAA                         
3788: 83              ADD     A,E                 
3789: 20 20           JR      NZ,$1256            ; {}
378B: 20 48           JR      NZ,$127E            ; {}
378D: 49              LD      C,C                 
378E: 47              LD      B,A                 
378F: 48              LD      C,B                 
3790: 45              LD      B,L                 
3791: 53              LD      D,E                 
3792: 54              LD      D,H                 
3793: 20 53           JR      NZ,$1289            ; {}
3795: 43              LD      B,E                 
3796: 4F              LD      C,A                 
3797: 52              LD      D,D                 
3798: 45              LD      B,L                 
3799: 20 20           JR      NZ,$1256            ; {}
379B: 20 20           JR      NZ,$1256            ; {}
379D: 20 10           JR      NZ,$1246            ; {}
379F: 17              RLA                         
37A0: 54              LD      D,H                 
37A1: 83              ADD     A,E                 
37A2: 47              LD      B,A                 
37A3: 4F              LD      C,A                 
37A4: 20 46           JR      NZ,$127C            ; {}
37A6: 4F              LD      C,A                 
37A7: 52              LD      D,D                 
37A8: 20 54           JR      NZ,$128A            ; {}
37AA: 48              LD      C,B                 
37AB: 45              LD      B,L                 
37AC: 20 57           JR      NZ,$128D            ; {}
37AE: 4F              LD      C,A                 
37AF: 52              LD      D,D                 
37B0: 4C              LD      C,H                 
37B1: 44              LD      B,H                 
37B2: 20 52           JR      NZ,$1288            ; {}
37B4: 45              LD      B,L                 
37B5: 43              LD      B,E                 
37B6: 4F              LD      C,A                 
37B7: 52              LD      D,D                 
37B8: 44              LD      B,H                 
37B9: 10 05           DJNZ    $123B               ; {}
37BB: 56              LD      D,(HL)              
37BC: 82              ADD     A,D                 
37BD: 4E              LD      C,(HL)              
37BE: 4F              LD      C,A                 
37BF: 57              LD      D,A                 
37C0: 20 21           JR      NZ,$1257            ; {}
37C2: D6 37           SUB     $37                 
37C4: E6 37           AND     $37                 
37C6: F6 37           OR      $37                 
37C8: 06 38           LD      B,$38               
37CA: 16 38           LD      D,$38               
37CC: 26 38           LD      H,$38               
37CE: 36 38           LD      (HL),$38            
37D0: 46              LD      B,(HL)              
37D1: 38 56           JR      C,$128C             ; {}
37D3: 38 66           JR      C,$129C             ; {}
37D5: 38 40           JR      C,$1276             ; {}
37D7: 48              LD      C,B                 
37D8: 4F              LD      C,A                 
37D9: 40              LD      B,B                 
37DA: 4B              LD      C,E                 
37DB: 46              LD      B,(HL)              
37DC: 42              LD      B,D                 
37DD: 4F              LD      C,A                 
37DE: 44              LD      B,H                 
37DF: 40              LD      B,B                 
37E0: 40              LD      B,B                 
37E1: 49              LD      C,C                 
37E2: 4D              LD      C,L                 
37E3: 41              LD      B,C                 
37E4: 45              LD      B,L                 
37E5: 40              LD      B,B                 
37E6: 40              LD      B,B                 
37E7: 40              LD      B,B                 
37E8: 40              LD      B,B                 
37E9: 40              LD      B,B                 
37EA: 4E              LD      C,(HL)              
37EB: 40              LD      B,B                 
37EC: 40              LD      B,B                 
37ED: 49              LD      C,C                 
37EE: 41              LD      B,C                 
37EF: 41              LD      B,C                 
37F0: 41              LD      B,C                 
37F1: 49              LD      C,C                 
37F2: 40              LD      B,B                 
37F3: 40              LD      B,B                 
37F4: 40              LD      B,B                 
37F5: 49              LD      C,C                 
37F6: 4E              LD      C,(HL)              
37F7: 40              LD      B,B                 
37F8: 4E              LD      C,(HL)              
37F9: 4F              LD      C,A                 
37FA: 45              LD      B,L                 
37FB: 4E              LD      C,(HL)              
37FC: 41              LD      B,C                 
37FD: 49              LD      C,C                 
37FE: 49              LD      C,C                 
37FF: 43              LD      B,E                 
3800: 49              LD      C,C                 
3801: 49              LD      C,C                 
3802: 42              LD      B,D                 
3803: 45              LD      B,L                 
3804: 40              LD      B,B                 
3805: 49              LD      C,C                 
3806: 40              LD      B,B                 
3807: 40              LD      B,B                 
3808: 4E              LD      C,(HL)              
3809: 40              LD      B,B                 
380A: 49              LD      C,C                 
380B: 4E              LD      C,(HL)              
380C: 4D              LD      C,L                 
380D: 49              LD      C,C                 
380E: 44              LD      B,H                 
380F: 41              LD      B,C                 
3810: 40              LD      B,B                 
3811: 49              LD      C,C                 
3812: 45              LD      B,L                 
3813: 4D              LD      C,L                 
3814: 41              LD      B,C                 
3815: 4C              LD      C,H                 
3816: 40              LD      B,B                 
3817: 4E              LD      C,(HL)              
3818: 4F              LD      C,A                 
3819: 40              LD      B,B                 
381A: 4E              LD      C,(HL)              
381B: 45              LD      B,L                 
381C: 49              LD      C,C                 
381D: 40              LD      B,B                 
381E: 41              LD      B,C                 
381F: 48              LD      C,B                 
3820: 44              LD      B,H                 
3821: 4F              LD      C,A                 
3822: 46              LD      B,(HL)              
3823: 46              LD      B,(HL)              
3824: 45              LD      B,L                 
3825: 4C              LD      C,H                 
3826: 48              LD      C,B                 
3827: 4F              LD      C,A                 
3828: 4E              LD      C,(HL)              
3829: 40              LD      B,B                 
382A: 45              LD      B,L                 
382B: 49              LD      C,C                 
382C: 4D              LD      C,L                 
382D: 49              LD      C,C                 
382E: 49              LD      C,C                 
382F: 49              LD      C,C                 
3830: 40              LD      B,B                 
3831: 49              LD      C,C                 
3832: 4C              LD      C,H                 
3833: 42              LD      B,D                 
3834: 41              LD      B,C                 
3835: 4C              LD      C,H                 
3836: 40              LD      B,B                 
3837: 48              LD      C,B                 
3838: 48              LD      C,B                 
3839: 40              LD      B,B                 
383A: 43              LD      B,E                 
383B: 42              LD      B,D                 
383C: 46              LD      B,(HL)              
383D: 49              LD      C,C                 
383E: 49              LD      C,C                 
383F: 47              LD      B,A                 
3840: 40              LD      B,B                 
3841: 49              LD      C,C                 
3842: 4C              LD      C,H                 
3843: 4D              LD      C,L                 
3844: 41              LD      B,C                 
3845: 4C              LD      C,H                 
3846: 48              LD      C,B                 
3847: 40              LD      B,B                 
3848: 40              LD      B,B                 
3849: 40              LD      B,B                 
384A: 45              LD      B,L                 
384B: 40              LD      B,B                 
384C: 48              LD      C,B                 
384D: 4F              LD      C,A                 
384E: 49              LD      C,C                 
384F: 43              LD      B,E                 
3850: 46              LD      B,(HL)              
3851: 4C              LD      C,H                 
3852: 41              LD      B,C                 
3853: 4C              LD      C,H                 
3854: 40              LD      B,B                 
3855: 40              LD      B,B                 
3856: 4E              LD      C,(HL)              
3857: 4F              LD      C,A                 
3858: 48              LD      C,B                 
3859: 40              LD      B,B                 
385A: 45              LD      B,L                 
385B: 41              LD      B,C                 
385C: 40              LD      B,B                 
385D: 49              LD      C,C                 
385E: 49              LD      C,C                 
385F: 47              LD      B,A                 
3860: 49              LD      C,C                 
3861: 49              LD      C,C                 
3862: 4D              LD      C,L                 
3863: 4C              LD      C,H                 
3864: 41              LD      B,C                 
3865: 4C              LD      C,H                 
3866: 4E              LD      C,(HL)              
3867: 4F              LD      C,A                 
3868: 40              LD      B,B                 
3869: 40              LD      B,B                 
386A: 45              LD      B,L                 
386B: 42              LD      B,D                 
386C: 40              LD      B,B                 
386D: 49              LD      C,C                 
386E: 49              LD      C,C                 
386F: 47              LD      B,A                 
3870: 4E              LD      C,(HL)              
3871: 49              LD      C,C                 
3872: 42              LD      B,D                 
3873: 41              LD      B,C                 
3874: 45              LD      B,L                 
3875: 40              LD      B,B                 
3876: F3              DI                          
3877: 3E 10           LD      A,$10               
3879: 32 00 71        LD      ($7100),A           
387C: AF              XOR     A                   
387D: 32 23 68        LD      ($6823),A           
3880: 32 02 A0        LD      ($A002),A           
3883: 32 20 68        LD      ($6820),A           
3886: 3D              DEC     A                   
3887: 32 00 70        LD      ($7000),A           
388A: 3E 04           LD      A,$04               
388C: 32 40 B8        LD      ($B840),A           
388F: 21 00 00        LD      HL,$0000            
3892: 06 10           LD      B,$10               
3894: D9              EXX                         
3895: 21 00 80        LD      HL,$8000            
3898: 01 00 04        LD      BC,$0400            
389B: 54              LD      D,H                 
389C: 5D              LD      E,L                 
389D: D9              EXX                         
389E: 54              LD      D,H                 
389F: 5D              LD      E,L                 
38A0: D9              EXX                         
38A1: D9              EXX                         
38A2: 7C              LD      A,H                 
38A3: AD              XOR     L                   
38A4: 2F              CPL                         
38A5: 87              ADD     A,A                 
38A6: 87              ADD     A,A                 
38A7: ED 6A           ADC     HL,HL               
38A9: 7D              LD      A,L                 
38AA: D9              EXX                         
38AB: 77              LD      (HL),A              
38AC: 23              INC     HL                  
38AD: 32 30 68        LD      ($6830),A           
38B0: 0D              DEC     C                   
38B1: 20 EE           JR      NZ,$1224            ; {}
38B3: 10 EC           DJNZ    $1222               ; {}
38B5: 06 04           LD      B,$04               
38B7: 62              LD      H,D                 
38B8: 6B              LD      L,E                 
38B9: D9              EXX                         
38BA: EB              EX      DE,HL               
38BB: D9              EXX                         
38BC: D9              EXX                         
38BD: 7D              LD      A,L                 
38BE: AC              XOR     H                   
38BF: 2F              CPL                         
38C0: 87              ADD     A,A                 
38C1: 87              ADD     A,A                 
38C2: ED 6A           ADC     HL,HL               
38C4: 7D              LD      A,L                 
38C5: D9              EXX                         
38C6: AE              XOR     (HL)                
38C7: C2 66 3D        JP      NZ,$3D66            ; {}
38CA: 23              INC     HL                  
38CB: 32 30 68        LD      ($6830),A           
38CE: 0D              DEC     C                   
38CF: 20 EB           JR      NZ,$1221            ; {}
38D1: 10 E9           DJNZ    $121F               ; {}
38D3: EB              EX      DE,HL               
38D4: D9              EXX                         
38D5: 10 BD           DJNZ    $11F3               ; {}
38D7: D9              EXX                         
38D8: 01 00 04        LD      BC,$0400            
38DB: 36 00           LD      (HL),$00            
38DD: 23              INC     HL                  
38DE: 0D              DEC     C                   
38DF: 20 FA           JR      NZ,$1230            ; {}
38E1: 10 F8           DJNZ    $122E               ; {}
38E3: 31 00 84        LD      SP,$8400            
38E6: 21 E0 89        LD      HL,$89E0            
38E9: 11 00 80        LD      DE,$8000            
38EC: 01 20 00        LD      BC,$0020            
38EF: ED B0           LDIR                        
38F1: 21 00 84        LD      HL,$8400            
38F4: CD D1 3D        CALL    $3DD1               ; {}
38F7: 21 00 88        LD      HL,$8800            
38FA: CD D1 3D        CALL    $3DD1               ; {}
38FD: 21 00 90        LD      HL,$9000            
3900: CD D1 3D        CALL    $3DD1               ; {}
3903: 21 00 98        LD      HL,$9800            
3906: CD D1 3D        CALL    $3DD1               ; {}
3909: 21 00 80        LD      HL,$8000            
390C: 11 E0 89        LD      DE,$89E0            
390F: 01 20 00        LD      BC,$0020            
3912: ED B0           LDIR                        
3914: 31 00 9A        LD      SP,$9A00            
3917: 32 30 68        LD      ($6830),A           
391A: 21 00 88        LD      HL,$8800            
391D: 22 02 89        LD      ($8902),HL          
3920: 22 00 89        LD      ($8900),HL          
3923: CD 29 3E        CALL    $3E29               ; {}
3926: 21 83 3E        LD      HL,$3E83            
3929: CD EB 36        CALL    $36EB               ; {}
392C: AF              XOR     A                   
392D: 32 00 8A        LD      ($8A00),A           
3930: 32 01 8A        LD      ($8A01),A           
3933: 3C              INC     A                   
3934: 32 9A 87        LD      ($879A),A           
3937: 32 22 68        LD      ($6822),A           
393A: 32 25 68        LD      ($6825),A           
393D: 32 26 68        LD      ($6826),A           
3940: 32 27 68        LD      ($6827),A           
3943: 32 23 68        LD      ($6823),A           
3946: 11 FC 3F        LD      DE,$3FFC            
3949: 21 00 00        LD      HL,$0000            
394C: 01 00 10        LD      BC,$1000            
394F: AF              XOR     A                   
3950: 86              ADD     A,(HL)              
3951: 32 30 68        LD      ($6830),A           
3954: 23              INC     HL                  
3955: 0D              DEC     C                   
3956: 20 F8           JR      NZ,$122E            ; {}
3958: 10 F6           DJNZ    $122C               ; {}
395A: EB              EX      DE,HL               
395B: BE              CP      (HL)                
395C: C2 53 3E        JP      NZ,$3E53            ; {}
395F: 06 10           LD      B,$10               
3961: EB              EX      DE,HL               
3962: 13              INC     DE                  
3963: 7C              LD      A,H                 
3964: FE 40           CP      $40                 
3966: 20 E7           JR      NZ,$121D            ; {}
3968: 32 30 68        LD      ($6830),A           
396B: 3A 00 8A        LD      A,($8A00)           
396E: A7              AND     A                   
396F: 28 FA           JR      Z,$1230             ; {}
3971: 3C              INC     A                   
3972: C2 58 3E        JP      NZ,$3E58            ; {}
3975: 32 30 68        LD      ($6830),A           
3978: 3A 01 8A        LD      A,($8A01)           
397B: A7              AND     A                   
397C: 28 FA           JR      Z,$1230             ; {}
397E: 3C              INC     A                   
397F: C2 58 3E        JP      NZ,$3E58            ; {}
3982: 21 8D 3E        LD      HL,$3E8D            
3985: CD EB 36        CALL    $36EB               ; {}
3988: AF              XOR     A                   
3989: 32 00 8A        LD      ($8A00),A           
398C: 32 01 8A        LD      ($8A01),A           
398F: 06 10           LD      B,$10               
3991: 32 30 68        LD      ($6830),A           
3994: 0D              DEC     C                   
3995: 20 FA           JR      NZ,$1230            ; {}
3997: 10 F8           DJNZ    $122E               ; {}
3999: 21 C1 3F        LD      HL,$3FC1            
399C: 11 00 70        LD      DE,$7000            
399F: 01 03 00        LD      BC,$0003            
39A2: D9              EXX                         
39A3: 3E A1           LD      A,$A1               
39A5: 32 00 71        LD      ($7100),A           
39A8: 3A 00 71        LD      A,($7100)           
39AB: FE 10           CP      $10                 
39AD: 20 F9           JR      NZ,$122F            ; {}
39AF: 21 C8 3F        LD      HL,$3FC8            
39B2: 11 18 8A        LD      DE,$8A18            
39B5: 01 09 00        LD      BC,$0009            
39B8: ED B0           LDIR                        
39BA: ED 56           IM      1                   
39BC: AF              XOR     A                   
39BD: 32 20 68        LD      ($6820),A           
39C0: 3C              INC     A                   
39C1: 32 20 68        LD      ($6820),A           
39C4: FB              EI                          
39C5: 3A 23 84        LD      A,($8423)           
39C8: C6 04           ADD     $04                 
39CA: 4F              LD      C,A                 
39CB: 3A 23 84        LD      A,($8423)           
39CE: B9              CP      C                   
39CF: 20 FA           JR      NZ,$1230            ; {}
39D1: 3A 23 84        LD      A,($8423)           
39D4: 4F              LD      C,A                 
39D5: 3A 23 84        LD      A,($8423)           
39D8: B9              CP      C                   
39D9: 28 FA           JR      Z,$1230             ; {}
39DB: CD B0 3A        CALL    $3AB0               ; {}
39DE: CD 7D 3A        CALL    $3A7D               ; {}
39E1: CD DF 3A        CALL    $3ADF               ; {}
39E4: CD 38 3B        CALL    $3B38               ; {}
39E7: CD AE 3B        CALL    $3BAE               ; {}
39EA: CD CC 3B        CALL    $3BCC               ; {}
39ED: CD DA 3B        CALL    $3BDA               ; {}
39F0: CD EA 3B        CALL    $3BEA               ; {}
39F3: CD 35 3C        CALL    $3C35               ; {}
39F6: CD A1 3C        CALL    $3CA1               ; {}
39F9: 3A A7 85        LD      A,($85A7)           
39FC: 87              ADD     A,A                 
39FD: 30 D2           JR      NC,$1208            ; {}
39FF: CD 73 3E        CALL    $3E73               ; {}
3A02: 3A 23 84        LD      A,($8423)           
3A05: C6 64           ADD     $64                 
3A07: 4F              LD      C,A                 
3A08: 3A 23 84        LD      A,($8423)           
3A0B: B9              CP      C                   
3A0C: 20 FA           JR      NZ,$1230            ; {}
3A0E: 3A A7 85        LD      A,($85A7)           
3A11: 87              ADD     A,A                 
3A12: 30 FA           JR      NC,$1230            ; {}
3A14: 3E 04           LD      A,$04               
3A16: 32 3D 9B        LD      ($9B3D),A           
3A19: 3A 3D 9B        LD      A,($9B3D)           
3A1C: A7              AND     A                   
3A1D: 20 FA           JR      NZ,$1230            ; {}
3A1F: 3E 01           LD      A,$01               
3A21: 32 3D 9B        LD      ($9B3D),A           
3A24: 3A 3D 9B        LD      A,($9B3D)           
3A27: A7              AND     A                   
3A28: 20 FA           JR      NZ,$1230            ; {}
3A2A: F3              DI                          
3A2B: 32 30 68        LD      ($6830),A           
3A2E: 3A 00 71        LD      A,($7100)           
3A31: FE 10           CP      $10                 
3A33: 20 F6           JR      NZ,$122C            ; {}
3A35: 01 00 08        LD      BC,$0800            
3A38: 32 30 68        LD      ($6830),A           
3A3B: 0D              DEC     C                   
3A3C: 20 FA           JR      NZ,$1230            ; {}
3A3E: 10 F8           DJNZ    $122E               ; {}
3A40: 21 18 8A        LD      HL,$8A18            
3A43: 11 00 70        LD      DE,$7000            
3A46: 01 09 00        LD      BC,$0009            
3A49: D9              EXX                         
3A4A: AF              XOR     A                   
3A4B: 32 00 70        LD      ($7000),A           
3A4E: 3E C1           LD      A,$C1               
3A50: 32 00 71        LD      ($7100),A           
3A53: 3A 00 71        LD      A,($7100)           
3A56: FE 10           CP      $10                 
3A58: 20 F9           JR      NZ,$122F            ; {}
3A5A: 21 00 70        LD      HL,$7000            
3A5D: 11 10 8A        LD      DE,$8A10            
3A60: 01 03 00        LD      BC,$0003            
3A63: D9              EXX                         
3A64: 3E B1           LD      A,$B1               
3A66: 32 00 71        LD      ($7100),A           
3A69: 3A 00 71        LD      A,($7100)           
3A6C: FE 10           CP      $10                 
3A6E: 20 F9           JR      NZ,$122F            ; {}
3A70: 3A 10 8A        LD      A,($8A10)           
3A73: A7              AND     A                   
3A74: 20 CA           JR      NZ,$1200            ; {}
3A76: FE A0           CP      $A0                 
3A78: 20 00           JR      NZ,$1236            ; {}
3A7A: C3 1C 01        JP      $011C               ; {}
3A7D: 21 CE 87        LD      HL,$87CE            
3A80: 11 8A 89        LD      DE,$898A            
3A83: 7E              LD      A,(HL)              
3A84: 17              RLA                         
3A85: E6 0E           AND     $0E                 
3A87: 12              LD      (DE),A              
3A88: 13              INC     DE                  
3A89: 7E              LD      A,(HL)              
3A8A: 1F              RRA                         
3A8B: 1F              RRA                         
3A8C: E6 0E           AND     $0E                 
3A8E: 12              LD      (DE),A              
3A8F: 7E              LD      A,(HL)              
3A90: 13              INC     DE                  
3A91: 07              RLCA                        
3A92: 07              RLCA                        
3A93: 3C              INC     A                   
3A94: E6 03           AND     $03                 
3A96: 12              LD      (DE),A              
3A97: 23              INC     HL                  
3A98: 13              INC     DE                  
3A99: 4E              LD      C,(HL)              
3A9A: CB 19           RR      C                   
3A9C: 8F              ADC     A,A                 
3A9D: CB 19           RR      C                   
3A9F: 8F              ADC     A,A                 
3AA0: E6 03           AND     $03                 
3AA2: 12              LD      (DE),A              
3AA3: 7E              LD      A,(HL)              
3AA4: 13              INC     DE                  
3AA5: E6 04           AND     $04                 
3AA7: 12              LD      (DE),A              
3AA8: 7E              LD      A,(HL)              
3AA9: 07              RLCA                        
3AAA: 07              RLCA                        
3AAB: E6 03           AND     $03                 
3AAD: 13              INC     DE                  
3AAE: 12              LD      (DE),A              
3AAF: C9              RET                         
3AB0: 21 D9 89        LD      HL,$89D9            
3AB3: 11 D8 89        LD      DE,$89D8            
3AB6: 01 07 00        LD      BC,$0007            
3AB9: ED B0           LDIR                        
3ABB: 3A A8 85        LD      A,($85A8)           
3ABE: 06 02           LD      B,$02               
3AC0: 5A              LD      E,D                 
3AC1: 2B              DEC     HL                  
3AC2: 77              LD      (HL),A              
3AC3: 2B              DEC     HL                  
3AC4: B6              OR      (HL)                
3AC5: 2B              DEC     HL                  
3AC6: 2F              CPL                         
3AC7: A6              AND     (HL)                
3AC8: 2B              DEC     HL                  
3AC9: A6              AND     (HL)                
3ACA: 77              LD      (HL),A              
3ACB: 57              LD      D,A                 
3ACC: 3A A7 85        LD      A,($85A7)           
3ACF: 10 EF           DJNZ    $1225               ; {}
3AD1: EB              EX      DE,HL               
3AD2: 29              ADD     HL,HL               
3AD3: 06 0F           LD      B,$0F               
3AD5: 29              ADD     HL,HL               
3AD6: 38 02           JR      C,$1238             ; {}
3AD8: 10 FB           DJNZ    $1231               ; {}
3ADA: 78              LD      A,B                 
3ADB: 32 88 89        LD      ($8988),A           
3ADE: C9              RET                         
3ADF: 3A 8F 89        LD      A,($898F)           
3AE2: 21 78 3F        LD      HL,$3F78            
3AE5: CF              RST     0X08                
3AE6: E5              PUSH    HL                  
3AE7: 21 AD 3E        LD      HL,$3EAD            
3AEA: CD EB 36        CALL    $36EB               ; {}
3AED: CD EB 36        CALL    $36EB               ; {}
3AF0: CD EB 36        CALL    $36EB               ; {}
3AF3: CD EB 36        CALL    $36EB               ; {}
3AF6: D1              POP     DE                  
3AF7: 21 48 83        LD      HL,$8348            
3AFA: 01 1A 8A        LD      BC,$8A1A            
3AFD: CD 0E 3B        CALL    $3B0E               ; {}
3B00: 3A 8A 89        LD      A,($898A)           
3B03: 21 80 3F        LD      HL,$3F80            
3B06: D7              RST     0X10                
3B07: EB              EX      DE,HL               
3B08: 21 4A 83        LD      HL,$834A            
3B0B: 01 1C 8A        LD      BC,$8A1C            
3B0E: 1A              LD      A,(DE)              
3B0F: 77              LD      (HL),A              
3B10: 02              LD      (BC),A              
3B11: 03              INC     BC                  
3B12: C5              PUSH    BC                  
3B13: D6 11           SUB     $11                 
3B15: 3E 2C           LD      A,$2C               
3B17: 20 02           JR      NZ,$1238            ; {}
3B19: 3E 37           LD      A,$37               
3B1B: 01 40 FF        LD      BC,$FF40            
3B1E: 09              ADD     HL,BC               
3B1F: 77              LD      (HL),A              
3B20: 3E 37           LD      A,$37               
3B22: 01 E0 FF        LD      BC,$FFE0            
3B25: 09              ADD     HL,BC               
3B26: 77              LD      (HL),A              
3B27: 13              INC     DE                  
3B28: 1A              LD      A,(DE)              
3B29: 09              ADD     HL,BC               
3B2A: 77              LD      (HL),A              
3B2B: C1              POP     BC                  
3B2C: 02              LD      (BC),A              
3B2D: D6 11           SUB     $11                 
3B2F: 3E 2C           LD      A,$2C               
3B31: 20 02           JR      NZ,$1238            ; {}
3B33: 3E 37           LD      A,$37               
3B35: 25              DEC     H                   
3B36: 77              LD      (HL),A              
3B37: C9              RET                         
3B38: 3A 8B 89        LD      A,($898B)           
3B3B: A7              AND     A                   
3B3C: 20 0F           JR      NZ,$1245            ; {}
3B3E: 21 FF FF        LD      HL,$FFFF            
3B41: 22 D0 89        LD      ($89D0),HL          
3B44: 21 5D 3F        LD      HL,$3F5D            
3B47: CD EB 36        CALL    $36EB               ; {}
3B4A: C3 9A 3B        JP      $3B9A               ; {}
3B4D: 21 8E 3F        LD      HL,$3F8E            
3B50: 4F              LD      C,A                 
3B51: 3A 8C 89        LD      A,($898C)           
3B54: A7              AND     A                   
3B55: 20 03           JR      NZ,$1239            ; {}
3B57: 21 9C 3F        LD      HL,$3F9C            
3B5A: 06 00           LD      B,$00               
3B5C: 09              ADD     HL,BC               
3B5D: E5              PUSH    HL                  
3B5E: 21 D5 3E        LD      HL,$3ED5            
3B61: CD EB 36        CALL    $36EB               ; {}
3B64: CD EB 36        CALL    $36EB               ; {}
3B67: E1              POP     HL                  
3B68: 7E              LD      A,(HL)              
3B69: 32 92 81        LD      ($8192),A           
3B6C: 32 D0 89        LD      ($89D0),A           
3B6F: 23              INC     HL                  
3B70: 7E              LD      A,(HL)              
3B71: 32 D1 89        LD      ($89D1),A           
3B74: FE FF           CP      $FF                 
3B76: 28 22           JR      Z,$1258             ; {}
3B78: F5              PUSH    AF                  
3B79: E6 1F           AND     $1F                 
3B7B: 32 94 81        LD      ($8194),A           
3B7E: 21 F2 3E        LD      HL,$3EF2            
3B81: CD EB 36        CALL    $36EB               ; {}
3B84: CD EB 36        CALL    $36EB               ; {}
3B87: F1              POP     AF                  
3B88: CB 7F           BIT     7,A                 
3B8A: 28 14           JR      Z,$124A             ; {}
3B8C: E6 1F           AND     $1F                 
3B8E: 32 96 81        LD      ($8196),A           
3B91: 21 0F 3F        LD      HL,$3F0F            
3B94: CD EB 36        CALL    $36EB               ; {}
3B97: C3 EB 36        JP      $36EB               ; {}
3B9A: 21 54 83        LD      HL,$8354            
3B9D: CD A3 3B        CALL    $3BA3               ; {}
3BA0: 21 56 83        LD      HL,$8356            
3BA3: 11 E0 FF        LD      DE,$FFE0            
3BA6: 06 18           LD      B,$18               
3BA8: 36 37           LD      (HL),$37            
3BAA: 19              ADD     HL,DE               
3BAB: 10 FB           DJNZ    $1231               ; {}
3BAD: C9              RET                         
3BAE: 3A 8C 89        LD      A,($898C)           
3BB1: A7              AND     A                   
3BB2: 20 02           JR      NZ,$1238            ; {}
3BB4: 3E 05           LD      A,$05               
3BB6: C6 10           ADD     $10                 
3BB8: 32 6C 82        LD      ($826C),A           
3BBB: D6 11           SUB     $11                 
3BBD: 3E 37           LD      A,$37               
3BBF: 20 02           JR      NZ,$1238            ; {}
3BC1: 3E 37           LD      A,$37               
3BC3: 32 4C 82        LD      ($824C),A           
3BC6: 21 2C 3F        LD      HL,$3F2C            
3BC9: C3 EB 36        JP      $36EB               ; {}
3BCC: 3A 8D 89        LD      A,($898D)           
3BCF: C6 1A           ADD     $1A                 
3BD1: 32 AE 82        LD      ($82AE),A           
3BD4: 21 36 3F        LD      HL,$3F36            
3BD7: C3 EB 36        JP      $36EB               ; {}
3BDA: 3A 8E 89        LD      A,($898E)           
3BDD: 21 3E 3F        LD      HL,$3F3E            
3BE0: A7              AND     A                   
3BE1: CA EB 36        JP      Z,$36EB             ; {}
3BE4: 21 49 3F        LD      HL,$3F49            
3BE7: C3 EB 36        JP      $36EB               ; {}
3BEA: 3A 89 89        LD      A,($8989)           
3BED: 0E 00           LD      C,$00               
3BEF: FE 0A           CP      $0A                 
3BF1: 38 05           JR      C,$123B             ; {}
3BF3: D6 0A           SUB     $0A                 
3BF5: 0C              INC     C                   
3BF6: 18 F7           JR      $122D               ; {}
3BF8: C6 10           ADD     $10                 
3BFA: 32 70 82        LD      ($8270),A           
3BFD: 79              LD      A,C                 
3BFE: C6 10           ADD     $10                 
3C00: 32 90 82        LD      ($8290),A           
3C03: 21 01 84        LD      HL,$8401            
3C06: CB EE           SET     5,(HL)              
3C08: 3A 88 89        LD      A,($8988)           
3C0B: A7              AND     A                   
3C0C: C4 15 3C        CALL    NZ,$3C15            ; {}
3C0F: 21 54 3F        LD      HL,$3F54            
3C12: C3 EB 36        JP      $36EB               ; {}
3C15: 3A 89 89        LD      A,($8989)           
3C18: 3C              INC     A                   
3C19: FE 15           CP      $15                 
3C1B: 38 01           JR      C,$1237             ; {}
3C1D: AF              XOR     A                   
3C1E: 32 89 89        LD      ($8989),A           
3C21: 21 80 9A        LD      HL,$9A80            
3C24: 06 2C           LD      B,$2C               
3C26: 36 00           LD      (HL),$00            
3C28: 23              INC     HL                  
3C29: 10 FB           DJNZ    $1231               ; {}
3C2B: 21 80 9A        LD      HL,$9A80            
3C2E: 4F              LD      C,A                 
3C2F: 06 00           LD      B,$00               
3C31: 09              ADD     HL,BC               
3C32: 36 01           LD      (HL),$01            
3C34: C9              RET                         
3C35: 2A 91 89        LD      HL,($8991)          
3C38: 7C              LD      A,H                 
3C39: B5              OR      L                   
3C3A: 28 05           JR      Z,$123B             ; {}
3C3C: 2B              DEC     HL                  
3C3D: 22 91 89        LD      ($8991),HL          
3C40: C9              RET                         
3C41: 3A 88 89        LD      A,($8988)           
3C44: FE 0F           CP      $0F                 
3C46: 28 0C           JR      Z,$1242             ; {}
3C48: 21 5A 83        LD      HL,$835A            
3C4B: C3 A3 3B        JP      $3BA3               ; {}
3C4E: 3E 03           LD      A,$03               
3C50: 32 3D 9B        LD      ($9B3D),A           
3C53: C9              RET                         
3C54: 3A A7 85        LD      A,($85A7)           
3C57: E6 01           AND     $01                 
3C59: 28 F3           JR      Z,$1229             ; {}
3C5B: 21 B0 04        LD      HL,$04B0            
3C5E: 22 91 89        LD      ($8991),HL          
3C61: 21 E0 89        LD      HL,$89E0            
3C64: 11 5A 83        LD      DE,$835A            
3C67: 01 02 01        LD      BC,$0102            
3C6A: CD 79 3C        CALL    $3C79               ; {}
3C6D: 06 03           LD      B,$03               
3C6F: CD 79 3C        CALL    $3C79               ; {}
3C72: 06 02           LD      B,$02               
3C74: CD 79 3C        CALL    $3C79               ; {}
3C77: 06 01           LD      B,$01               
3C79: 7E              LD      A,(HL)              
3C7A: CD 8E 3C        CALL    $3C8E               ; {}
3C7D: 23              INC     HL                  
3C7E: CD 85 3C        CALL    $3C85               ; {}
3C81: 23              INC     HL                  
3C82: 10 FA           DJNZ    $1230               ; {}
3C84: C9              RET                         
3C85: 7E              LD      A,(HL)              
3C86: 1F              RRA                         
3C87: 1F              RRA                         
3C88: 1F              RRA                         
3C89: 1F              RRA                         
3C8A: CD 8E 3C        CALL    $3C8E               ; {}
3C8D: 7E              LD      A,(HL)              
3C8E: E6 0F           AND     $0F                 
3C90: 2F              CPL                         
3C91: C6 1A           ADD     $1A                 
3C93: 12              LD      (DE),A              
3C94: CD E1 36        CALL    $36E1               ; {}
3C97: 0D              DEC     C                   
3C98: C0              RET     NZ                  
3C99: 0E 04           LD      C,$04               
3C9B: 3E 35           LD      A,$35               
3C9D: 12              LD      (DE),A              
3C9E: C3 E1 36        JP      $36E1               ; {}
3CA1: 3A A7 85        LD      A,($85A7)           
3CA4: E6 03           AND     $03                 
3CA6: 28 02           JR      Z,$1238             ; {}
3CA8: 3E 01           LD      A,$01               
3CAA: 3C              INC     A                   
3CAB: 32 07 A0        LD      ($A007),A           
3CAE: 3A A7 85        LD      A,($85A7)           
3CB1: E6 01           AND     $01                 
3CB3: 28 05           JR      Z,$123B             ; {}
3CB5: AF              XOR     A                   
3CB6: 32 90 89        LD      ($8990),A           
3CB9: C9              RET                         
3CBA: 3A 88 89        LD      A,($8988)           
3CBD: 3D              DEC     A                   
3CBE: FE 04           CP      $04                 
3CC0: D0              RET     NC                  
3CC1: 3C              INC     A                   
3CC2: 4F              LD      C,A                 
3CC3: 3A 90 89        LD      A,($8990)           
3CC6: 5F              LD      E,A                 
3CC7: 3C              INC     A                   
3CC8: 32 90 89        LD      ($8990),A           
3CCB: 16 00           LD      D,$00               
3CCD: 21 AC 3F        LD      HL,$3FAC            
3CD0: 19              ADD     HL,DE               
3CD1: 7E              LD      A,(HL)              
3CD2: 3C              INC     A                   
3CD3: 28 07           JR      Z,$123D             ; {}
3CD5: B9              CP      C                   
3CD6: C8              RET     Z                   
3CD7: AF              XOR     A                   
3CD8: 32 90 89        LD      ($8990),A           
3CDB: C9              RET                         
3CDC: CD 29 3E        CALL    $3E29               ; {}
3CDF: 11 12 3D        LD      DE,$3D12            
3CE2: 21 42 80        LD      HL,$8042            
3CE5: 06 1C           LD      B,$1C               
3CE7: CD F5 3C        CALL    $3CF5               ; {}
3CEA: 10 FB           DJNZ    $1231               ; {}
3CEC: 3A A7 85        LD      A,($85A7)           
3CEF: 87              ADD     A,A                 
3CF0: 30 FA           JR      NC,$1230            ; {}
3CF2: C3 FF 39        JP      $39FF               ; {}
3CF5: CD 03 3D        CALL    $3D03               ; {}
3CF8: CD 03 3D        CALL    $3D03               ; {}
3CFB: CD 03 3D        CALL    $3D03               ; {}
3CFE: 3E 05           LD      A,$05               
3D00: C3 10 00        JP      $0010               ; {}
3D03: 1A              LD      A,(DE)              
3D04: 0E 08           LD      C,$08               
3D06: 87              ADD     A,A                 
3D07: 30 02           JR      NC,$1238            ; {}
3D09: 36 18           LD      (HL),$18            
3D0B: 23              INC     HL                  
3D0C: 0D              DEC     C                   
3D0D: 20 F7           JR      NZ,$122D            ; {}
3D0F: 13              INC     DE                  
3D10: 23              INC     HL                  
3D11: C9              RET                         
3D12: 00              NOP                         
3D13: 3E 00           LD      A,$00               
3D15: 31 41 00        LD      SP,$0041            
3D18: 49              LD      C,C                 
3D19: 41              LD      B,C                 
3D1A: 00              NOP                         
3D1B: 45              LD      B,L                 
3D1C: 41              LD      B,C                 
3D1D: 00              NOP                         
3D1E: 23              INC     HL                  
3D1F: 3E 00           LD      A,$00               
3D21: 00              NOP                         
3D22: 00              NOP                         
3D23: 03              INC     BC                  
3D24: 36 22           LD      (HL),$22            
3D26: 03              INC     BC                  
3D27: 49              LD      C,C                 
3D28: 41              LD      B,C                 
3D29: 00              NOP                         
3D2A: 49              LD      C,C                 
3D2B: 41              LD      B,C                 
3D2C: 3E 36           LD      A,$36               
3D2E: 3E 41           LD      A,$41               
3D30: 00              NOP                         
3D31: 00              NOP                         
3D32: 41              LD      B,C                 
3D33: 3E 7F           LD      A,$7F               
3D35: 41              LD      B,C                 
3D36: 49              LD      C,C                 
3D37: 20 7F           JR      NZ,$12B5            ; {}
3D39: 49              LD      C,C                 
3D3A: 18 00           JR      $1236               ; {}
3D3C: 32 20 40        LD      ($4020),A           
3D3F: 00              NOP                         
3D40: 7F              LD      A,A                 
3D41: 40              LD      B,B                 
3D42: 01 00 7F        LD      BC,$7F00            
3D45: 7F              LD      A,A                 
3D46: 3F              CCF                         
3D47: 40              LD      B,B                 
3D48: 21 44 40        LD      HL,$4044            
3D4B: 00              NOP                         
3D4C: 44              LD      B,H                 
3D4D: 00              NOP                         
3D4E: 3C              INC     A                   
3D4F: 44              LD      B,H                 
3D50: 01 42 3F        LD      BC,$3F42            
3D53: 01 81 00        LD      BC,$0081            
3D56: 01 A5 7F        LD      BC,$7FA5            
3D59: 01 A5 04        LD      BC,$04A5            
3D5C: 7F              LD      A,A                 
3D5D: 99              SBC     C                   
3D5E: 08              EX      AF,AF'              
3D5F: 00              NOP                         
3D60: 42              LD      B,D                 
3D61: 10 00           DJNZ    $1236               ; {}
3D63: 3C              INC     A                   
3D64: 7F              LD      A,A                 
3D65: 00              NOP                         
3D66: E6 0F           AND     $0F                 
3D68: 1E 21           LD      E,$21               
3D6A: 28 02           JR      Z,$1238             ; {}
3D6C: 1E 25           LD      E,$25               
3D6E: 7C              LD      A,H                 
3D6F: 1F              RRA                         
3D70: 1F              RRA                         
3D71: E6 07           AND     $07                 
3D73: FE 03           CP      $03                 
3D75: 38 06           JR      C,$123C             ; {}
3D77: 3D              DEC     A                   
3D78: FE 03           CP      $03                 
3D7A: 28 01           JR      Z,$1237             ; {}
3D7C: 3D              DEC     A                   
3D7D: 21 00 80        LD      HL,$8000            
3D80: 01 00 04        LD      BC,$0400            
3D83: 36 37           LD      (HL),$37            
3D85: 32 30 68        LD      ($6830),A           
3D88: 23              INC     HL                  
3D89: 0D              DEC     C                   
3D8A: 20 F7           JR      NZ,$122D            ; {}
3D8C: 10 F5           DJNZ    $122B               ; {}
3D8E: 21 80 8B        LD      HL,$8B80            
3D91: 01 80 00        LD      BC,$0080            
3D94: 36 00           LD      (HL),$00            
3D96: 23              INC     HL                  
3D97: 10 FB           DJNZ    $1231               ; {}
3D99: 21 80 93        LD      HL,$9380            
3D9C: 01 80 00        LD      BC,$0080            
3D9F: 36 00           LD      (HL),$00            
3DA1: 23              INC     HL                  
3DA2: 10 FB           DJNZ    $1231               ; {}
3DA4: 21 80 9B        LD      HL,$9B80            
3DA7: 01 80 00        LD      BC,$0080            
3DAA: 36 00           LD      (HL),$00            
3DAC: 23              INC     HL                  
3DAD: 10 FB           DJNZ    $1231               ; {}
3DAF: C6 10           ADD     $10                 
3DB1: 32 C2 82        LD      ($82C2),A           
3DB4: 7B              LD      A,E                 
3DB5: 32 A2 82        LD      ($82A2),A           
3DB8: 3E 2B           LD      A,$2B               
3DBA: 32 42 83        LD      ($8342),A           
3DBD: 3E 1A           LD      A,$1A               
3DBF: 32 22 83        LD      ($8322),A           
3DC2: 3E 26           LD      A,$26               
3DC4: 32 02 83        LD      ($8302),A           
3DC7: 3E 01           LD      A,$01               
3DC9: 32 03 A0        LD      ($A003),A           
3DCC: 32 30 68        LD      ($6830),A           
3DCF: 18 FE           JR      $1234               ; {}
3DD1: D9              EXX                         
3DD2: 06 10           LD      B,$10               
3DD4: D9              EXX                         
3DD5: 01 00 04        LD      BC,$0400            
3DD8: 54              LD      D,H                 
3DD9: 5D              LD      E,L                 
3DDA: D9              EXX                         
3DDB: 54              LD      D,H                 
3DDC: 5D              LD      E,L                 
3DDD: D9              EXX                         
3DDE: D9              EXX                         
3DDF: 7C              LD      A,H                 
3DE0: AD              XOR     L                   
3DE1: 2F              CPL                         
3DE2: 87              ADD     A,A                 
3DE3: 87              ADD     A,A                 
3DE4: ED 6A           ADC     HL,HL               
3DE6: 7D              LD      A,L                 
3DE7: D9              EXX                         
3DE8: 77              LD      (HL),A              
3DE9: 23              INC     HL                  
3DEA: 32 30 68        LD      ($6830),A           
3DED: 0D              DEC     C                   
3DEE: 20 EE           JR      NZ,$1224            ; {}
3DF0: 10 EC           DJNZ    $1222               ; {}
3DF2: 06 04           LD      B,$04               
3DF4: 62              LD      H,D                 
3DF5: 6B              LD      L,E                 
3DF6: D9              EXX                         
3DF7: EB              EX      DE,HL               
3DF8: D9              EXX                         
3DF9: D9              EXX                         
3DFA: 7D              LD      A,L                 
3DFB: AC              XOR     H                   
3DFC: 2F              CPL                         
3DFD: 87              ADD     A,A                 
3DFE: 87              ADD     A,A                 
3DFF: ED 6A           ADC     HL,HL               
3E01: 7D              LD      A,L                 
3E02: D9              EXX                         
3E03: AE              XOR     (HL)                
3E04: C2 66 3D        JP      NZ,$3D66            ; {}
3E07: 23              INC     HL                  
3E08: 32 30 68        LD      ($6830),A           
3E0B: 0D              DEC     C                   
3E0C: 20 EB           JR      NZ,$1221            ; {}
3E0E: 10 E9           DJNZ    $121F               ; {}
3E10: EB              EX      DE,HL               
3E11: D9              EXX                         
3E12: 10 C0           DJNZ    $11F6               ; {}
3E14: D9              EXX                         
3E15: 01 00 04        LD      BC,$0400            
3E18: 36 00           LD      (HL),$00            
3E1A: 23              INC     HL                  
3E1B: 0D              DEC     C                   
3E1C: 20 FA           JR      NZ,$1230            ; {}
3E1E: 10 F8           DJNZ    $122E               ; {}
3E20: C9              RET                         
3E21: 21 40 80        LD      HL,$8040            
3E24: 01 C0 04        LD      BC,$04C0            
3E27: 18 06           JR      $123C               ; {}
3E29: 21 00 80        LD      HL,$8000            
3E2C: 01 00 04        LD      BC,$0400            
3E2F: 36 37           LD      (HL),$37            
3E31: 23              INC     HL                  
3E32: 0D              DEC     C                   
3E33: 20 FA           JR      NZ,$1230            ; {}
3E35: 10 F8           DJNZ    $122E               ; {}
3E37: 3E 01           LD      A,$01               
3E39: 32 03 A0        LD      ($A003),A           
3E3C: 21 80 8B        LD      HL,$8B80            
3E3F: CD 4B 3E        CALL    $3E4B               ; {}
3E42: 21 80 93        LD      HL,$9380            
3E45: CD 4B 3E        CALL    $3E4B               ; {}
3E48: 21 80 9B        LD      HL,$9B80            
3E4B: 06 80           LD      B,$80               
3E4D: AF              XOR     A                   
3E4E: 77              LD      (HL),A              
3E4F: 23              INC     HL                  
3E50: 10 FC           DJNZ    $1232               ; {}
3E52: C9              RET                         
3E53: 7A              LD      A,D                 
3E54: 1F              RRA                         
3E55: 1F              RRA                         
3E56: 1F              RRA                         
3E57: 1F              RRA                         
3E58: E6 0F           AND     $0F                 
3E5A: F6 10           OR      $10                 
3E5C: 32 C4 82        LD      ($82C4),A           
3E5F: 3E 2B           LD      A,$2B               
3E61: 32 44 83        LD      ($8344),A           
3E64: 3E 28           LD      A,$28               
3E66: 32 24 83        LD      ($8324),A           
3E69: 3E 26           LD      A,$26               
3E6B: 32 04 83        LD      ($8304),A           
3E6E: 32 30 68        LD      ($6830),A           
3E71: 18 FB           JR      $1231               ; {}
3E73: CD 29 3E        CALL    $3E29               ; {}
3E76: 21 00 A0        LD      HL,$A000            
3E79: 36 01           LD      (HL),$01            
3E7B: 06 03           LD      B,$03               
3E7D: 23              INC     HL                  
3E7E: 36 00           LD      (HL),$00            
3E80: 10 FB           DJNZ    $1231               ; {}
3E82: C9              RET                         
3E83: 10 06           DJNZ    $123C               ; {}
3E85: 42              LD      B,D                 
3E86: 83              ADD     A,E                 
3E87: 52              LD      D,D                 
3E88: 41              LD      B,C                 
3E89: 4D              LD      C,L                 
3E8A: 20 4F           JR      NZ,$1285            ; {}
3E8C: 4B              LD      C,E                 
3E8D: 10 06           DJNZ    $123C               ; {}
3E8F: 44              LD      B,H                 
3E90: 83              ADD     A,E                 
3E91: 52              LD      D,D                 
3E92: 4F              LD      C,A                 
3E93: 4D              LD      C,L                 
3E94: 20 4F           JR      NZ,$1285            ; {}
3E96: 4B              LD      C,E                 
3E97: 10 12           DJNZ    $1248               ; {}
3E99: 48              LD      C,B                 
3E9A: 83              ADD     A,E                 
3E9B: 46              LD      B,(HL)              
3E9C: 52              LD      D,D                 
3E9D: 45              LD      B,L                 
3E9E: 45              LD      B,L                 
3E9F: 20 50           JR      NZ,$1286            ; {}
3EA1: 4C              LD      C,H                 
3EA2: 41              LD      B,C                 
3EA3: 59              LD      E,C                 
3EA4: 20 20           JR      NZ,$1256            ; {}
3EA6: 20 20           JR      NZ,$1256            ; {}
3EA8: 20 20           JR      NZ,$1256            ; {}
3EAA: 20 20           JR      NZ,$1256            ; {}
3EAC: 20 10           JR      NZ,$1246            ; {}
3EAE: 05              DEC     B                   
3EAF: 28 83           JR      Z,$11B9             ; {}
3EB1: 20 43           JR      NZ,$1279            ; {}
3EB3: 4F              LD      C,A                 
3EB4: 49              LD      C,C                 
3EB5: 4E              LD      C,(HL)              
3EB6: 10 07           DJNZ    $123D               ; {}
3EB8: 28 82           JR      Z,$11B8             ; {}
3EBA: 20 43           JR      NZ,$1279            ; {}
3EBC: 52              LD      D,D                 
3EBD: 45              LD      B,L                 
3EBE: 44              LD      B,H                 
3EBF: 49              LD      C,C                 
3EC0: 54              LD      D,H                 
3EC1: 10 05           DJNZ    $123B               ; {}
3EC3: 2A 83 20        LD      HL,($2083)          ; {}
3EC6: 43              LD      B,E                 
3EC7: 4F              LD      C,A                 
3EC8: 49              LD      C,C                 
3EC9: 4E              LD      C,(HL)              
3ECA: 10 07           DJNZ    $123D               ; {}
3ECC: 2A 82 20        LD      HL,($2082)          ; {}
3ECF: 43              LD      B,E                 
3ED0: 52              LD      D,D                 
3ED1: 45              LD      B,L                 
3ED2: 44              LD      B,H                 
3ED3: 49              LD      C,C                 
3ED4: 54              LD      D,H                 
3ED5: 10 0D           DJNZ    $1243               ; {}
3ED7: 52              LD      D,D                 
3ED8: 83              ADD     A,E                 
3ED9: 31 53 54        LD      SP,$5453            
3EDC: 20 42           JR      NZ,$1278            ; {}
3EDE: 4F              LD      C,A                 
3EDF: 4E              LD      C,(HL)              
3EE0: 55              LD      D,L                 
3EE1: 53              LD      D,E                 
3EE2: 20 46           JR      NZ,$127C            ; {}
3EE4: 4F              LD      C,A                 
3EE5: 52              LD      D,D                 
3EE6: 10 08           DJNZ    $123E               ; {}
3EE8: 72              LD      (HL),D              
3EE9: 81              ADD     A,C                 
3EEA: 30 30           JR      NC,$1266            ; {}
3EEC: 30 30           JR      NC,$1266            ; {}
3EEE: 20 50           JR      NZ,$1286            ; {}
3EF0: 54              LD      D,H                 
3EF1: 53              LD      D,E                 
3EF2: 10 0D           DJNZ    $1243               ; {}
3EF4: 54              LD      D,H                 
3EF5: 83              ADD     A,E                 
3EF6: 32 4E 44        LD      ($444E),A           
3EF9: 20 42           JR      NZ,$1278            ; {}
3EFB: 4F              LD      C,A                 
3EFC: 4E              LD      C,(HL)              
3EFD: 55              LD      D,L                 
3EFE: 53              LD      D,E                 
3EFF: 20 46           JR      NZ,$127C            ; {}
3F01: 4F              LD      C,A                 
3F02: 52              LD      D,D                 
3F03: 10 08           DJNZ    $123E               ; {}
3F05: 74              LD      (HL),H              
3F06: 81              ADD     A,C                 
3F07: 30 30           JR      NC,$1266            ; {}
3F09: 30 30           JR      NC,$1266            ; {}
3F0B: 20 50           JR      NZ,$1286            ; {}
3F0D: 54              LD      D,H                 
3F0E: 53              LD      D,E                 
3F0F: 10 0D           DJNZ    $1243               ; {}
3F11: 56              LD      D,(HL)              
3F12: 83              ADD     A,E                 
3F13: 41              LD      B,C                 
3F14: 4E              LD      C,(HL)              
3F15: 44              LD      B,H                 
3F16: 20 46           JR      NZ,$127C            ; {}
3F18: 4F              LD      C,A                 
3F19: 52              LD      D,D                 
3F1A: 20 45           JR      NZ,$127B            ; {}
3F1C: 56              LD      D,(HL)              
3F1D: 45              LD      B,L                 
3F1E: 52              LD      D,D                 
3F1F: 59              LD      E,C                 
3F20: 10 08           DJNZ    $123E               ; {}
3F22: 76              HALT                        
3F23: 81              ADD     A,C                 
3F24: 30 30           JR      NC,$1266            ; {}
3F26: 30 30           JR      NC,$1266            ; {}
3F28: 20 50           JR      NZ,$1286            ; {}
3F2A: 54              LD      D,H                 
3F2B: 53              LD      D,E                 
3F2C: 10 06           DJNZ    $123C               ; {}
3F2E: 4C              LD      C,H                 
3F2F: 83              ADD     A,E                 
3F30: 44              LD      B,H                 
3F31: 49              LD      C,C                 
3F32: 47              LD      B,A                 
3F33: 44              LD      B,H                 
3F34: 55              LD      D,L                 
3F35: 47              LD      B,A                 
3F36: 10 04           DJNZ    $123A               ; {}
3F38: 4E              LD      C,(HL)              
3F39: 83              ADD     A,E                 
3F3A: 52              LD      D,D                 
3F3B: 41              LD      B,C                 
3F3C: 4E              LD      C,(HL)              
3F3D: 4B              LD      C,E                 
3F3E: 10 07           DJNZ    $123D               ; {}
3F40: 46              LD      B,(HL)              
3F41: 83              ADD     A,E                 
3F42: 54              LD      D,H                 
3F43: 41              LD      B,C                 
3F44: 42              LD      B,D                 
3F45: 4C              LD      C,H                 
3F46: 45              LD      B,L                 
3F47: 20 20           JR      NZ,$1256            ; {}
3F49: 10 07           DJNZ    $123D               ; {}
3F4B: 46              LD      B,(HL)              
3F4C: 83              ADD     A,E                 
3F4D: 55              LD      D,L                 
3F4E: 50              LD      D,B                 
3F4F: 52              LD      D,D                 
3F50: 49              LD      C,C                 
3F51: 47              LD      B,A                 
3F52: 48              LD      C,B                 
3F53: 54              LD      D,H                 
3F54: 10 05           DJNZ    $123B               ; {}
3F56: 50              LD      D,B                 
3F57: 83              ADD     A,E                 
3F58: 53              LD      D,E                 
3F59: 4F              LD      C,A                 
3F5A: 55              LD      D,L                 
3F5B: 4E              LD      C,(HL)              
3F5C: 44              LD      B,H                 
3F5D: 10 17           DJNZ    $124D               ; {}
3F5F: 52              LD      D,D                 
3F60: 83              ADD     A,E                 
3F61: 42              LD      B,D                 
3F62: 4F              LD      C,A                 
3F63: 4E              LD      C,(HL)              
3F64: 55              LD      D,L                 
3F65: 53              LD      D,E                 
3F66: 20 4E           JR      NZ,$1284            ; {}
3F68: 4F              LD      C,A                 
3F69: 54              LD      D,H                 
3F6A: 48              LD      C,B                 
3F6B: 49              LD      C,C                 
3F6C: 4E              LD      C,(HL)              
3F6D: 47              LD      B,A                 
3F6E: 20 20           JR      NZ,$1256            ; {}
3F70: 20 20           JR      NZ,$1256            ; {}
3F72: 20 20           JR      NZ,$1256            ; {}
3F74: 20 20           JR      NZ,$1256            ; {}
3F76: 20 20           JR      NZ,$1256            ; {}
3F78: 11 11 12        LD      DE,$1211            
3F7B: 11 11 12        LD      DE,$1211            
3F7E: 12              LD      (DE),A              
3F7F: 13              INC     DE                  
3F80: 11 17 11        LD      DE,$1117            
3F83: 11 11 13        LD      DE,$1311            
3F86: 12              LD      (DE),A              
3F87: 11 11 16        LD      DE,$1611            
3F8A: 12              LD      (DE),A              
3F8B: 13              INC     DE                  
3F8C: 11 12 13        LD      DE,$1312            
3F8F: 11 12 97        LD      DE,$9712            
3F92: 11 95 12        LD      DE,$1295            
3F95: 16 11           LD      D,$11               
3F97: 94              SUB     H                   
3F98: 11 14 12        LD      DE,$1214            
3F9B: 96              SUB     (HL)                
3F9C: 11 FF 12        LD      DE,$12FF            
3F9F: 16 13           LD      D,$13               
3FA1: 98              SBC     B                   
3FA2: 12              LD      (DE),A              
3FA3: FF              RST     0X38                
3FA4: 12              LD      (DE),A              
3FA5: 96              SUB     (HL)                
3FA6: 13              INC     DE                  
3FA7: 17              RLA                         
3FA8: 12              LD      (DE),A              
3FA9: 15              DEC     D                   
3FAA: 13              INC     DE                  
3FAB: FF              RST     0X38                
3FAC: 00              NOP                         
3FAD: 00              NOP                         
3FAE: 00              NOP                         
3FAF: 00              NOP                         
3FB0: 00              NOP                         
3FB1: 00              NOP                         
3FB2: 01 01 01        LD      BC,$0101            
3FB5: 02              LD      (BC),A              
3FB6: 02              LD      (BC),A              
3FB7: 02              LD      (BC),A              
3FB8: 02              LD      (BC),A              
3FB9: 03              INC     BC                  
3FBA: 03              INC     BC                  
3FBB: 03              INC     BC                  
3FBC: 03              INC     BC                  
3FBD: 03              INC     BC                  
3FBE: 03              INC     BC                  
3FBF: 03              INC     BC                  
3FC0: FF              RST     0X38                
3FC1: 05              DEC     B                   
3FC2: 05              DEC     B                   
3FC3: 05              DEC     B                   
3FC4: 05              DEC     B                   
3FC5: 05              DEC     B                   
3FC6: 05              DEC     B                   
3FC7: 05              DEC     B                   
3FC8: 00              NOP                         
3FC9: 01 01 01        LD      BC,$0101            
3FCC: 01 01 04        LD      BC,$0401            
3FCF: 02              LD      (BC),A              
3FD0: 02              LD      (BC),A              
3FD1: 02              LD      (BC),A              
3FD2: 02              LD      (BC),A              
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
3FFB: AE              XOR     (HL)                
3FFC: 4B              LD      C,E                 
3FFD: 88              ADC     A,B                 
3FFE: 10 AA           DJNZ    $11E0               ; {}
```

