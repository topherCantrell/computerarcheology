![Time Pilot Main Board](TimePilot.jpg)

# Time Pilot Main Board

>>> cpu Z80

>>> binary 0000:roms/TM1 + roms/TM2 + roms/TM3

>>> memoryTable hard 
[Hardware Info](Hardware.md)

>>> memoryTable ram 
[RAM Usage](RAMUse.md)


```code
; TM1+TM2+TM3 as Z80

; https://www.programcreek.com/java-api-examples/index.php?source_dir=arcadeflex036-master/emulator/src/drivers/timeplt.java

0000: C3 B1 07       JP      $07B1           
0003: FF             RST     0X38            
0004: FF             RST     0X38            
0005: FF             RST     0X38            
0006: 33             INC     SP              
0007: 4B             LD      C,E             
0008: 85             ADD     A,L             
0009: 6F             LD      L,A             
000A: 30 01          JR      NC,$0D          
000C: 24             INC     H               
000D: 7E             LD      A,(HL)          
000E: C9             RET                     
000F: 4F             LD      C,A             
0010: 87             ADD     A,A             
0011: DF             RST     0X18            
0012: 5E             LD      E,(HL)          
0013: 23             INC     HL              
0014: 56             LD      D,(HL)          
0015: 23             INC     HL              
0016: C9             RET                     
0017: 4E             LD      C,(HL)          
0018: 85             ADD     A,L             
0019: 6F             LD      L,A             
001A: D0             RET     NC              
001B: 24             INC     H               
001C: C9             RET                     
001D: FF             RST     0X38            
001E: FF             RST     0X38            
001F: 41             LD      B,C             
0020: 7B             LD      A,E             
0021: D6 20          SUB     $20             
0023: 5F             LD      E,A             
0024: D0             RET     NC              
0025: 15             DEC     D               
0026: C9             RET                     
0027: 4D             LD      C,L             
0028: 7B             LD      A,E             
0029: C6 20          ADD     $20             
002B: 5F             LD      E,A             
002C: D0             RET     NC              
002D: 14             INC     D               
002E: C9             RET                     
002F: 49             LD      C,C             
0030: E1             POP     HL              
0031: D7             RST     0X10            
0032: EB             EX      DE,HL           
0033: E9             JP      (HL)            
0034: FF             RST     0X38            
0035: FF             RST     0X38            
0036: FF             RST     0X38            
0037: FF             RST     0X38            
0038: E5             PUSH    HL              
0039: 26 AC          LD      H,$AC           
003B: 3A B2 A9       LD      A,($A9B2)       
003E: 6F             LD      L,A             
003F: CB 7E          BIT     7,(HL)          
0041: 28 0A          JR      Z,$4D           
0043: 72             LD      (HL),D          
0044: 2C             INC     L               
0045: 73             LD      (HL),E          
0046: 2C             INC     L               
0047: 7D             LD      A,L             
0048: E6 3F          AND     $3F             
004A: 32 B2 A9       LD      ($A9B2),A       
004D: E1             POP     HL              
004E: C9             RET                     
004F: 0F             RRCA                    
0050: A7             AND     A               
0051: 11 ED 77       LD      DE,$77ED        
0054: 68             LD      L,B             
0055: D7             RST     0X10            
0056: 34             INC     (HL)            
0057: F1             POP     AF              
0058: D7             RST     0X10            
0059: A5             AND     L               
005A: 3B             DEC     SP              
005B: 7C             LD      A,H             
005C: FD                                
005D: 3B             DEC     SP              
005E: 7D             LD      A,L             
005F: F1             POP     AF              
0060: DC A5 8C       CALL    C,$8CA5         
0063: 57             LD      D,A             
0064: 34             INC     (HL)            
0065: B9             CP      C               
0066: C3 D8 00       JP      $00D8           
0069: 32 00 C2       LD      ($C200),A       
006C: 21 11 B4       LD      HL,$B411        
006F: 06 30          LD      B,$30           
0071: 36 00          LD      (HL),$00        
0073: 23             INC     HL              
0074: 10 FB          DJNZ    $71             
0076: 32 00 C2       LD      ($C200),A       
0079: 21 10 B4       LD      HL,$B410        
007C: 06 30          LD      B,$30           
007E: 36 00          LD      (HL),$00        
0080: 23             INC     HL              
0081: 10 FB          DJNZ    $7E             
0083: 32 00 C2       LD      ($C200),A       
0086: 21 00 A8       LD      HL,$A800        
0089: 11 01 A8       LD      DE,$A801        
008C: 01 FF 07       LD      BC,$07FF        
008F: 36 00          LD      (HL),$00        
0091: ED B0          LDIR                    
0093: 32 00 C2       LD      ($C200),A       
0096: 06 00          LD      B,$00           
0098: 21 D8 00       LD      HL,$00D8        
009B: AF             XOR     A               
009C: 86             ADD     A,(HL)          
009D: 23             INC     HL              
009E: 10 FC          DJNZ    $9C             
00A0: D6 87          SUB     $87             
00A2: C4 D8 00       CALL    NZ,$00D8        
00A5: C3 66 58       JP      $5866           
00A8: 32 00 C3       LD      ($C300),A       
00AB: 32 00 C2       LD      ($C200),A       
00AE: C3 93 0B       JP      $0B93           
00B1: 21 20 A4       LD      HL,$A420        
00B4: 0E 0E          LD      C,$0E           
00B6: 11 20 00       LD      DE,$0020        
00B9: 19             ADD     HL,DE           
00BA: 06 10          LD      B,$10           
00BC: CD C7 00       CALL    $00C7           
00BF: 23             INC     HL              
00C0: 23             INC     HL              
00C1: 10 F9          DJNZ    $BC             
00C3: 0D             DEC     C               
00C4: 20 F0          JR      NZ,$B6          
00C6: C9             RET                     
00C7: E5             PUSH    HL              
00C8: 36 56          LD      (HL),$56        
00CA: 23             INC     HL              
00CB: 36 83          LD      (HL),$83        
00CD: 11 1F 00       LD      DE,$001F        
00D0: 19             ADD     HL,DE           
00D1: 36 C7          LD      (HL),$C7        
00D3: 23             INC     HL              
00D4: 36 EF          LD      (HL),$EF        
00D6: E1             POP     HL              
00D7: C9             RET                     
00D8: F5             PUSH    AF              
00D9: C5             PUSH    BC              
00DA: D5             PUSH    DE              
00DB: E5             PUSH    HL              
00DC: 08             EX      AF,AF'          
00DD: D9             EXX                     
00DE: F5             PUSH    AF              
00DF: C5             PUSH    BC              
00E0: D5             PUSH    DE              
00E1: E5             PUSH    HL              
00E2: DD E5          PUSH    IX              
00E4: FD E5          PUSH    IY              
00E6: CD 65 03       CALL    $0365           
00E9: CD 86 52       CALL    $5286           
00EC: AF             XOR     A               
00ED: 32 00 C3       LD      ($C300),A       
00F0: 32 00 C2       LD      ($C200),A       
00F3: 3C             INC     A               
00F4: 32 87 A9       LD      ($A987),A       
00F7: 3A 32 AD       LD      A,($AD32)       
00FA: A7             AND     A               
00FB: 28 09          JR      Z,$106          
00FD: 3A C2 A9       LD      A,($A9C2)       
0100: A7             AND     A               
0101: 20 03          JR      NZ,$106         
0103: 32 87 A9       LD      ($A987),A       
0106: 3A 87 A9       LD      A,($A987)       
0109: 32 02 C3       LD      ($C302),A       
010C: 3A 00 C2       LD      A,($C200)       
010F: 2F             CPL                     
0110: 32 AD A9       LD      ($A9AD),A       
0113: 3A 00 C3       LD      A,($C300)       
0116: 2F             CPL                     
0117: 32 AE A9       LD      ($A9AE),A       
011A: 3A 20 C3       LD      A,($C320)       
011D: 2F             CPL                     
011E: 32 AF A9       LD      ($A9AF),A       
0121: 3A 40 C3       LD      A,($C340)       
0124: 2F             CPL                     
0125: 32 B0 A9       LD      ($A9B0),A       
0128: 3A 60 C3       LD      A,($C360)       
012B: 2F             CPL                     
012C: 32 B1 A9       LD      ($A9B1),A       
012F: 21 80 A9       LD      HL,$A980        
0132: 34             INC     (HL)            
0133: 21 CE A9       LD      HL,$A9CE        
0136: 7E             LD      A,(HL)          
0137: 3C             INC     A               
0138: 27             DAA                     
0139: 77             LD      (HL),A          
013A: 21 17 A8       LD      HL,$A817        
013D: 7E             LD      A,(HL)          
013E: A7             AND     A               
013F: 28 01          JR      Z,$142          
0141: 35             DEC     (HL)            
0142: 21 12 A8       LD      HL,$A812        
0145: 7E             LD      A,(HL)          
0146: A7             AND     A               
0147: 28 01          JR      Z,$14A          
0149: 35             DEC     (HL)            
014A: 21 F4 A8       LD      HL,$A8F4        
014D: 7E             LD      A,(HL)          
014E: A7             AND     A               
014F: 28 01          JR      Z,$152          
0151: 35             DEC     (HL)            
0152: CD BE 48       CALL    $48BE           
0155: 21 74 01       LD      HL,$0174        
0158: E5             PUSH    HL              
0159: 3A AB A9       LD      A,($A9AB)       
015C: E6 03          AND     $03             
015E: F7             RST     0X30            
015F: C2 15 51       JP      NZ,$5115        
0162: 16 FE          LD      D,$FE           
0164: 17             RLA                     
0165: 1F             RRA                     
0166: 0F             RRCA                    
0167: 6F             LD      L,A             
0168: A6             AND     (HL)            
0169: 14             INC     D               
016A: 88             ADC     A,B             
016B: 57             LD      D,A             
016C: A5             AND     L               
016D: BF             CP      A               
016E: 34             INC     (HL)            
016F: D7             RST     0X10            
0170: F1             POP     AF              
0171: 96             SUB     (HL)            
0172: F1             POP     AF              
0173: B9             CP      C               
0174: CD D4 55       CALL    $55D4           
0177: FD E1          POP     IY              
0179: DD E1          POP     IX              
017B: E1             POP     HL              
017C: D1             POP     DE              
017D: C1             POP     BC              
017E: F1             POP     AF              
017F: D9             EXX                     
0180: 08             EX      AF,AF'          
0181: E1             POP     HL              
0182: D1             POP     DE              
0183: C1             POP     BC              
0184: 3A 00 16       LD      A,($1600)       
0187: 32 00 C3       LD      ($C300),A       
018A: F1             POP     AF              
018B: C9             RET                     
018C: 87             ADD     A,A             
018D: 30 01          JR      NC,$190         
018F: 24             INC     H               
0190: 85             ADD     A,L             
0191: 6F             LD      L,A             
0192: 30 01          JR      NC,$195         
0194: 24             INC     H               
0195: 5E             LD      E,(HL)          
0196: 23             INC     HL              
0197: 56             LD      D,(HL)          
0198: 23             INC     HL              
0199: C9             RET                     
019A: 21 00 A4       LD      HL,$A400        
019D: 22 89 A9       LD      ($A989),HL      
01A0: 3E 20          LD      A,$20           
01A2: 32 88 A9       LD      ($A988),A       
01A5: 06 F0          LD      B,$F0           
01A7: 21 A5 4B       LD      HL,$4BA5        
01AA: AF             XOR     A               
01AB: 86             ADD     A,(HL)          
01AC: 23             INC     HL              
01AD: 10 FC          DJNZ    $1AB            
01AF: D6 11          SUB     $11             
01B1: C4 67 01       CALL    NZ,$0167        
01B4: C9             RET                     
01B5: 21 04 A4       LD      HL,$A404        
01B8: 22 89 A9       LD      ($A989),HL      
01BB: 3A CD 0C       LD      A,($0CCD)       
01BE: 32 88 A9       LD      ($A988),A       
01C1: C9             RET                     
01C2: 2A 89 A9       LD      HL,($A989)      
01C5: 06 20          LD      B,$20           
01C7: 11 20 00       LD      DE,$0020        
01CA: 36 F1          LD      (HL),$F1        
01CC: CB 94          RES     2,H             
01CE: 36 10          LD      (HL),$10        
01D0: CB D4          SET     2,H             
01D2: 19             ADD     HL,DE           
01D3: 10 F5          DJNZ    $1CA            
01D5: 2A 89 A9       LD      HL,($A989)      
01D8: 23             INC     HL              
01D9: 22 89 A9       LD      ($A989),HL      
01DC: 21 88 A9       LD      HL,$A988        
01DF: 35             DEC     (HL)            
01E0: C9             RET                     
01E1: AF             XOR     A               
01E2: 32 E2 A9       LD      ($A9E2),A       
01E5: 2A 45 0D       LD      HL,($0D45)      
01E8: 22 E3 A9       LD      ($A9E3),HL      
01EB: 2A 0C 28       LD      HL,($280C)      
01EE: 22 E5 A9       LD      ($A9E5),HL      
01F1: 06 00          LD      B,$00           
01F3: 21 33 0E       LD      HL,$0E33        
01F6: AF             XOR     A               
01F7: 86             ADD     A,(HL)          
01F8: 23             INC     HL              
01F9: 10 FC          DJNZ    $1F7            
01FB: D6 FD          SUB     $FD             
01FD: C4 69 00       CALL    NZ,$0069        
0200: C9             RET                     
0201: CD 6F 02       CALL    $026F           
0204: 2A F5 32       LD      HL,($32F5)      
0207: ED 4B E3 A9    LD      BC,($A9E3)      
020B: A7             AND     A               
020C: ED 42          SBC     HL,BC           
020E: 29             ADD     HL,HL           
020F: 29             ADD     HL,HL           
0210: 29             ADD     HL,HL           
0211: 29             ADD     HL,HL           
0212: 3E 00          LD      A,$00           
0214: DE 00          SBC     $00             
0216: 6C             LD      L,H             
0217: 67             LD      H,A             
0218: 22 E7 A9       LD      ($A9E7),HL      
021B: 2A 45 0B       LD      HL,($0B45)      
021E: ED 4B E5 A9    LD      BC,($A9E5)      
0222: A7             AND     A               
0223: ED 42          SBC     HL,BC           
0225: 29             ADD     HL,HL           
0226: 29             ADD     HL,HL           
0227: 29             ADD     HL,HL           
0228: 29             ADD     HL,HL           
0229: 3E 00          LD      A,$00           
022B: DE 00          SBC     $00             
022D: 6C             LD      L,H             
022E: 67             LD      H,A             
022F: 22 E9 A9       LD      ($A9E9),HL      
0232: 2A E3 A9       LD      HL,($A9E3)      
0235: ED 4B E7 A9    LD      BC,($A9E7)      
0239: 09             ADD     HL,BC           
023A: 22 E3 A9       LD      ($A9E3),HL      
023D: 2A E5 A9       LD      HL,($A9E5)      
0240: ED 4B E9 A9    LD      BC,($A9E9)      
0244: 09             ADD     HL,BC           
0245: 22 E5 A9       LD      ($A9E5),HL      
0248: CD 6F 02       CALL    $026F           
024B: ED 5B B2 14    LD      DE,($14B2)      
024F: A7             AND     A               
0250: ED 52          SBC     HL,DE           
0252: C2 32 02       JP      NZ,$0232        
0255: 21 E2 A9       LD      HL,$A9E2        
0258: 34             INC     (HL)            
0259: 7E             LD      A,(HL)          
025A: 21 90 02       LD      HL,$0290        
025D: D7             RST     0X10            
025E: 21 E3 A9       LD      HL,$A9E3        
0261: 36 00          LD      (HL),$00        
0263: 23             INC     HL              
0264: 73             LD      (HL),E          
0265: 21 E5 A9       LD      HL,$A9E5        
0268: 36 00          LD      (HL),$00        
026A: 23             INC     HL              
026B: 72             LD      (HL),D          
026C: 7B             LD      A,E             
026D: A7             AND     A               
026E: C9             RET                     
026F: 3A E4 A9       LD      A,($A9E4)       
0272: 87             ADD     A,A             
0273: 87             ADD     A,A             
0274: 87             ADD     A,A             
0275: 6F             LD      L,A             
0276: 26 00          LD      H,$00           
0278: 29             ADD     HL,HL           
0279: 29             ADD     HL,HL           
027A: 3A E6 A9       LD      A,($A9E6)       
027D: 85             ADD     A,L             
027E: 6F             LD      L,A             
027F: 3E A4          LD      A,$A4           
0281: 84             ADD     A,H             
0282: 67             LD      H,A             
0283: 3A 0B AD       LD      A,($AD0B)       
0286: 77             LD      (HL),A          
0287: CB 94          RES     2,H             
0289: 3A 0C AD       LD      A,($AD0C)       
028C: 77             LD      (HL),A          
028D: CB D4          SET     2,H             
028F: C9             RET                     
0290: 10 04          DJNZ    $296            
0292: 11 04 12       LD      DE,$1204        
0295: 04             INC     B               
0296: 13             INC     DE              
0297: 04             INC     B               
0298: 14             INC     D               
0299: 04             INC     B               
029A: 15             DEC     D               
029B: 04             INC     B               
029C: 16 04          LD      D,$04           
029E: 17             RLA                     
029F: 04             INC     B               
02A0: 18 04          JR      $2A6            
02A2: 19             ADD     HL,DE           
02A3: 04             INC     B               
02A4: 1A             LD      A,(DE)          
02A5: 04             INC     B               
02A6: 1B             DEC     DE              
02A7: 04             INC     B               
02A8: 1C             INC     E               
02A9: 04             INC     B               
02AA: 1D             DEC     E               
02AB: 04             INC     B               
02AC: 1D             DEC     E               
02AD: 05             DEC     B               
02AE: 1D             DEC     E               
02AF: 06 1D          LD      B,$1D           
02B1: 07             RLCA                    
02B2: 1D             DEC     E               
02B3: 08             EX      AF,AF'          
02B4: 1D             DEC     E               
02B5: 09             ADD     HL,BC           
02B6: 1D             DEC     E               
02B7: 0A             LD      A,(BC)          
02B8: 1D             DEC     E               
02B9: 0B             DEC     BC              
02BA: 1D             DEC     E               
02BB: 0C             INC     C               
02BC: 1D             DEC     E               
02BD: 0D             DEC     C               
02BE: 1D             DEC     E               
02BF: 0E 1D          LD      C,$1D           
02C1: 0F             RRCA                    
02C2: 1D             DEC     E               
02C3: 10 1D          DJNZ    $2E2            
02C5: 11 1D 12       LD      DE,$121D        
02C8: 1D             DEC     E               
02C9: 13             INC     DE              
02CA: 1D             DEC     E               
02CB: 14             INC     D               
02CC: 1D             DEC     E               
02CD: 15             DEC     D               
02CE: 1D             DEC     E               
02CF: 16 1D          LD      D,$1D           
02D1: 17             RLA                     
02D2: 1D             DEC     E               
02D3: 18 1D          JR      $2F2            
02D5: 19             ADD     HL,DE           
02D6: 1D             DEC     E               
02D7: 1A             LD      A,(DE)          
02D8: 1D             DEC     E               
02D9: 1B             DEC     DE              
02DA: 1D             DEC     E               
02DB: 1C             INC     E               
02DC: 1D             DEC     E               
02DD: 1D             DEC     E               
02DE: 1D             DEC     E               
02DF: 1E 1C          LD      E,$1C           
02E1: 1E 1B          LD      E,$1B           
02E3: 1E 1A          LD      E,$1A           
02E5: 1E 19          LD      E,$19           
02E7: 1E 18          LD      E,$18           
02E9: 1E 17          LD      E,$17           
02EB: 1E 16          LD      E,$16           
02ED: 1E 15          LD      E,$15           
02EF: 1E 14          LD      E,$14           
02F1: 1E 13          LD      E,$13           
02F3: 1E 12          LD      E,$12           
02F5: 1E 11          LD      E,$11           
02F7: 1E 10          LD      E,$10           
02F9: 1E 0F          LD      E,$0F           
02FB: 1E 0E          LD      E,$0E           
02FD: 1E 0D          LD      E,$0D           
02FF: 1E 0C          LD      E,$0C           
0301: 1E 0B          LD      E,$0B           
0303: 1E 0A          LD      E,$0A           
0305: 1E 09          LD      E,$09           
0307: 1E 08          LD      E,$08           
0309: 1E 07          LD      E,$07           
030B: 1E 06          LD      E,$06           
030D: 1E 05          LD      E,$05           
030F: 1E 04          LD      E,$04           
0311: 1E 03          LD      E,$03           
0313: 1E 02          LD      E,$02           
0315: 1E 02          LD      E,$02           
0317: 1D             DEC     E               
0318: 02             LD      (BC),A          
0319: 1C             INC     E               
031A: 02             LD      (BC),A          
031B: 1B             DEC     DE              
031C: 02             LD      (BC),A          
031D: 1A             LD      A,(DE)          
031E: 02             LD      (BC),A          
031F: 19             ADD     HL,DE           
0320: 02             LD      (BC),A          
0321: 18 02          JR      $325            
0323: 17             RLA                     
0324: 02             LD      (BC),A          
0325: 16 02          LD      D,$02           
0327: 15             DEC     D               
0328: 02             LD      (BC),A          
0329: 14             INC     D               
032A: 02             LD      (BC),A          
032B: 13             INC     DE              
032C: 02             LD      (BC),A          
032D: 12             LD      (DE),A          
032E: 02             LD      (BC),A          
032F: 11 02 10       LD      DE,$1002        
0332: 02             LD      (BC),A          
0333: 0F             RRCA                    
0334: 02             LD      (BC),A          
0335: 0E 02          LD      C,$02           
0337: 0D             DEC     C               
0338: 02             LD      (BC),A          
0339: 0C             INC     C               
033A: 02             LD      (BC),A          
033B: 0B             DEC     BC              
033C: 02             LD      (BC),A          
033D: 0A             LD      A,(BC)          
033E: 02             LD      (BC),A          
033F: 09             ADD     HL,BC           
0340: 02             LD      (BC),A          
0341: 08             EX      AF,AF'          
0342: 02             LD      (BC),A          
0343: 07             RLCA                    
0344: 02             LD      (BC),A          
0345: 06 02          LD      B,$02           
0347: 05             DEC     B               
0348: 02             LD      (BC),A          
0349: 04             INC     B               
034A: 03             INC     BC              
034B: 04             INC     B               
034C: 04             INC     B               
034D: 04             INC     B               
034E: 05             DEC     B               
034F: 04             INC     B               
0350: 06 04          LD      B,$04           
0352: 07             RLCA                    
0353: 04             INC     B               
0354: 08             EX      AF,AF'          
0355: 04             INC     B               
0356: 09             ADD     HL,BC           
0357: 04             INC     B               
0358: 0A             LD      A,(BC)          
0359: 04             INC     B               
035A: 0B             DEC     BC              
035B: 04             INC     B               
035C: 0C             INC     C               
035D: 04             INC     B               
035E: 0D             DEC     C               
035F: 04             INC     B               
0360: 0E 04          LD      C,$04           
0362: 0F             RRCA                    
0363: 04             INC     B               
0364: 00             NOP                     
0365: 21 30 AA       LD      HL,$AA30        
0368: 11 10 B0       LD      DE,$B010        
036B: 3A 87 A9       LD      A,($A987)       
036E: A7             AND     A               
036F: CA 56 05       JP      Z,$0556         
0372: ED A0          LDI                     
0374: ED A0          LDI                     
0376: ED A0          LDI                     
0378: ED A0          LDI                     
037A: ED A0          LDI                     
037C: ED A0          LDI                     
037E: 21 10 AA       LD      HL,$AA10        
0381: ED A0          LDI                     
0383: ED A0          LDI                     
0385: ED A0          LDI                     
0387: ED A0          LDI                     
0389: ED A0          LDI                     
038B: ED A0          LDI                     
038D: ED A0          LDI                     
038F: ED A0          LDI                     
0391: ED A0          LDI                     
0393: ED A0          LDI                     
0395: ED A0          LDI                     
0397: ED A0          LDI                     
0399: ED A0          LDI                     
039B: ED A0          LDI                     
039D: ED A0          LDI                     
039F: ED A0          LDI                     
03A1: ED A0          LDI                     
03A3: ED A0          LDI                     
03A5: ED A0          LDI                     
03A7: ED A0          LDI                     
03A9: ED A0          LDI                     
03AB: ED A0          LDI                     
03AD: ED A0          LDI                     
03AF: ED A0          LDI                     
03B1: ED A0          LDI                     
03B3: ED A0          LDI                     
03B5: ED A0          LDI                     
03B7: ED A0          LDI                     
03B9: ED A0          LDI                     
03BB: ED A0          LDI                     
03BD: ED A0          LDI                     
03BF: ED A0          LDI                     
03C1: 21 36 AA       LD      HL,$AA36        
03C4: ED A0          LDI                     
03C6: ED A0          LDI                     
03C8: ED A0          LDI                     
03CA: ED A0          LDI                     
03CC: ED A0          LDI                     
03CE: ED A0          LDI                     
03D0: ED A0          LDI                     
03D2: ED A0          LDI                     
03D4: ED A0          LDI                     
03D6: ED A0          LDI                     
03D8: 21 60 AA       LD      HL,$AA60        
03DB: 11 10 B4       LD      DE,$B410        
03DE: ED A0          LDI                     
03E0: 7E             LD      A,(HL)          
03E1: C6 0E          ADD     $0E             
03E3: 2F             CPL                     
03E4: 12             LD      (DE),A          
03E5: 2C             INC     L               
03E6: 1C             INC     E               
03E7: ED A0          LDI                     
03E9: 7E             LD      A,(HL)          
03EA: C6 0E          ADD     $0E             
03EC: 2F             CPL                     
03ED: 12             LD      (DE),A          
03EE: 2C             INC     L               
03EF: 1C             INC     E               
03F0: ED A0          LDI                     
03F2: 7E             LD      A,(HL)          
03F3: C6 0E          ADD     $0E             
03F5: 2F             CPL                     
03F6: 12             LD      (DE),A          
03F7: 2C             INC     L               
03F8: 1C             INC     E               
03F9: 21 40 AA       LD      HL,$AA40        
03FC: ED A0          LDI                     
03FE: 7E             LD      A,(HL)          
03FF: C6 0E          ADD     $0E             
0401: 2F             CPL                     
0402: 12             LD      (DE),A          
0403: 2C             INC     L               
0404: 1C             INC     E               
0405: ED A0          LDI                     
0407: 7E             LD      A,(HL)          
0408: C6 0E          ADD     $0E             
040A: 2F             CPL                     
040B: 12             LD      (DE),A          
040C: 2C             INC     L               
040D: 1C             INC     E               
040E: ED A0          LDI                     
0410: 7E             LD      A,(HL)          
0411: C6 0E          ADD     $0E             
0413: 2F             CPL                     
0414: 12             LD      (DE),A          
0415: 2C             INC     L               
0416: 1C             INC     E               
0417: ED A0          LDI                     
0419: 7E             LD      A,(HL)          
041A: C6 0E          ADD     $0E             
041C: 2F             CPL                     
041D: 12             LD      (DE),A          
041E: 2C             INC     L               
041F: 1C             INC     E               
0420: ED A0          LDI                     
0422: 7E             LD      A,(HL)          
0423: C6 0E          ADD     $0E             
0425: 2F             CPL                     
0426: 12             LD      (DE),A          
0427: 2C             INC     L               
0428: 1C             INC     E               
0429: ED A0          LDI                     
042B: 7E             LD      A,(HL)          
042C: C6 0E          ADD     $0E             
042E: 2F             CPL                     
042F: 12             LD      (DE),A          
0430: 2C             INC     L               
0431: 1C             INC     E               
0432: ED A0          LDI                     
0434: 7E             LD      A,(HL)          
0435: C6 0E          ADD     $0E             
0437: 2F             CPL                     
0438: 12             LD      (DE),A          
0439: 2C             INC     L               
043A: 1C             INC     E               
043B: ED A0          LDI                     
043D: 7E             LD      A,(HL)          
043E: C6 0E          ADD     $0E             
0440: 2F             CPL                     
0441: 12             LD      (DE),A          
0442: 2C             INC     L               
0443: 1C             INC     E               
0444: ED A0          LDI                     
0446: 7E             LD      A,(HL)          
0447: C6 0E          ADD     $0E             
0449: 2F             CPL                     
044A: 12             LD      (DE),A          
044B: 2C             INC     L               
044C: 1C             INC     E               
044D: ED A0          LDI                     
044F: 7E             LD      A,(HL)          
0450: C6 0E          ADD     $0E             
0452: 2F             CPL                     
0453: 12             LD      (DE),A          
0454: 2C             INC     L               
0455: 1C             INC     E               
0456: ED A0          LDI                     
0458: 7E             LD      A,(HL)          
0459: C6 0E          ADD     $0E             
045B: 2F             CPL                     
045C: 12             LD      (DE),A          
045D: 2C             INC     L               
045E: 1C             INC     E               
045F: ED A0          LDI                     
0461: 7E             LD      A,(HL)          
0462: C6 0E          ADD     $0E             
0464: 2F             CPL                     
0465: 12             LD      (DE),A          
0466: 2C             INC     L               
0467: 1C             INC     E               
0468: ED A0          LDI                     
046A: 7E             LD      A,(HL)          
046B: C6 0E          ADD     $0E             
046D: 2F             CPL                     
046E: 12             LD      (DE),A          
046F: 2C             INC     L               
0470: 1C             INC     E               
0471: ED A0          LDI                     
0473: 7E             LD      A,(HL)          
0474: C6 0E          ADD     $0E             
0476: 2F             CPL                     
0477: 12             LD      (DE),A          
0478: 2C             INC     L               
0479: 1C             INC     E               
047A: ED A0          LDI                     
047C: 7E             LD      A,(HL)          
047D: C6 0E          ADD     $0E             
047F: 2F             CPL                     
0480: 12             LD      (DE),A          
0481: 2C             INC     L               
0482: 1C             INC     E               
0483: ED A0          LDI                     
0485: 7E             LD      A,(HL)          
0486: C6 0E          ADD     $0E             
0488: 2F             CPL                     
0489: 12             LD      (DE),A          
048A: 2C             INC     L               
048B: 1C             INC     E               
048C: 21 66 AA       LD      HL,$AA66        
048F: ED A0          LDI                     
0491: 7E             LD      A,(HL)          
0492: C6 0E          ADD     $0E             
0494: 2F             CPL                     
0495: 12             LD      (DE),A          
0496: 2C             INC     L               
0497: 1C             INC     E               
0498: ED A0          LDI                     
049A: 7E             LD      A,(HL)          
049B: C6 0E          ADD     $0E             
049D: 2F             CPL                     
049E: 12             LD      (DE),A          
049F: 2C             INC     L               
04A0: 1C             INC     E               
04A1: ED A0          LDI                     
04A3: 7E             LD      A,(HL)          
04A4: C6 0E          ADD     $0E             
04A6: 2F             CPL                     
04A7: 12             LD      (DE),A          
04A8: 2C             INC     L               
04A9: 1C             INC     E               
04AA: ED A0          LDI                     
04AC: 7E             LD      A,(HL)          
04AD: C6 0E          ADD     $0E             
04AF: 2F             CPL                     
04B0: 12             LD      (DE),A          
04B1: 2C             INC     L               
04B2: 1C             INC     E               
04B3: ED A0          LDI                     
04B5: 7E             LD      A,(HL)          
04B6: C6 0E          ADD     $0E             
04B8: 2F             CPL                     
04B9: 12             LD      (DE),A          
04BA: 2C             INC     L               
04BB: 1C             INC     E               
04BC: 3A AB A9       LD      A,($A9AB)       
04BF: FE 03          CP      $03             
04C1: C0             RET     NZ              
04C2: 3A AC A9       LD      A,($A9AC)       
04C5: 21 32 08       LD      HL,$0832        
04C8: BE             CP      (HL)            
04C9: D8             RET     C               
04CA: FE 08          CP      $08             
04CC: D0             RET     NC              
04CD: 3A 11 B4       LD      A,($B411)       
04D0: C6 80          ADD     $80             
04D2: 38 0A          JR      C,$4DE          
04D4: 32 11 B4       LD      ($B411),A       
04D7: 21 10 B0       LD      HL,$B010        
04DA: 7E             LD      A,(HL)          
04DB: C6 80          ADD     $80             
04DD: 77             LD      (HL),A          
04DE: 3A 13 B4       LD      A,($B413)       
04E1: C6 80          ADD     $80             
04E3: 38 0A          JR      C,$4EF          
04E5: 32 13 B4       LD      ($B413),A       
04E8: 21 12 B0       LD      HL,$B012        
04EB: 7E             LD      A,(HL)          
04EC: C6 80          ADD     $80             
04EE: 77             LD      (HL),A          
04EF: 3A 15 B4       LD      A,($B415)       
04F2: C6 80          ADD     $80             
04F4: 38 0A          JR      C,$500          
04F6: 32 15 B4       LD      ($B415),A       
04F9: 21 14 B0       LD      HL,$B014        
04FC: 7E             LD      A,(HL)          
04FD: C6 80          ADD     $80             
04FF: 77             LD      (HL),A          
0500: 3A 37 B4       LD      A,($B437)       
0503: C6 80          ADD     $80             
0505: 38 0A          JR      C,$511          
0507: 32 37 B4       LD      ($B437),A       
050A: 21 36 B0       LD      HL,$B036        
050D: 7E             LD      A,(HL)          
050E: C6 80          ADD     $80             
0510: 77             LD      (HL),A          
0511: 3A 39 B4       LD      A,($B439)       
0514: C6 80          ADD     $80             
0516: 38 0A          JR      C,$522          
0518: 32 39 B4       LD      ($B439),A       
051B: 21 38 B0       LD      HL,$B038        
051E: 7E             LD      A,(HL)          
051F: C6 80          ADD     $80             
0521: 77             LD      (HL),A          
0522: 3A 3B B4       LD      A,($B43B)       
0525: C6 80          ADD     $80             
0527: 38 0A          JR      C,$533          
0529: 32 3B B4       LD      ($B43B),A       
052C: 21 3A B0       LD      HL,$B03A        
052F: 7E             LD      A,(HL)          
0530: C6 80          ADD     $80             
0532: 77             LD      (HL),A          
0533: 3A 3D B4       LD      A,($B43D)       
0536: C6 80          ADD     $80             
0538: 38 0A          JR      C,$544          
053A: 32 3D B4       LD      ($B43D),A       
053D: 21 3C B0       LD      HL,$B03C        
0540: 7E             LD      A,(HL)          
0541: C6 80          ADD     $80             
0543: 77             LD      (HL),A          
0544: 3A 3F B4       LD      A,($B43F)       
0547: C6 80          ADD     $80             
0549: 38 0A          JR      C,$555          
054B: 32 3F B4       LD      ($B43F),A       
054E: 21 3E B0       LD      HL,$B03E        
0551: 7E             LD      A,(HL)          
0552: C6 80          ADD     $80             
0554: 77             LD      (HL),A          
0555: C9             RET                     
0556: 7E             LD      A,(HL)          
0557: C6 0F          ADD     $0F             
0559: 2F             CPL                     
055A: 12             LD      (DE),A          
055B: 2C             INC     L               
055C: 1C             INC     E               
055D: ED A0          LDI                     
055F: 7E             LD      A,(HL)          
0560: C6 0F          ADD     $0F             
0562: 2F             CPL                     
0563: 12             LD      (DE),A          
0564: 2C             INC     L               
0565: 1C             INC     E               
0566: ED A0          LDI                     
0568: 7E             LD      A,(HL)          
0569: C6 0F          ADD     $0F             
056B: 2F             CPL                     
056C: 12             LD      (DE),A          
056D: 2C             INC     L               
056E: 1C             INC     E               
056F: ED A0          LDI                     
0571: 21 10 AA       LD      HL,$AA10        
0574: 7E             LD      A,(HL)          
0575: C6 0F          ADD     $0F             
0577: 2F             CPL                     
0578: 12             LD      (DE),A          
0579: 2C             INC     L               
057A: 1C             INC     E               
057B: ED A0          LDI                     
057D: 7E             LD      A,(HL)          
057E: C6 0F          ADD     $0F             
0580: 2F             CPL                     
0581: 12             LD      (DE),A          
0582: 2C             INC     L               
0583: 1C             INC     E               
0584: ED A0          LDI                     
0586: 7E             LD      A,(HL)          
0587: C6 0F          ADD     $0F             
0589: 2F             CPL                     
058A: 12             LD      (DE),A          
058B: 2C             INC     L               
058C: 1C             INC     E               
058D: ED A0          LDI                     
058F: 7E             LD      A,(HL)          
0590: C6 0F          ADD     $0F             
0592: 2F             CPL                     
0593: 12             LD      (DE),A          
0594: 2C             INC     L               
0595: 1C             INC     E               
0596: ED A0          LDI                     
0598: 7E             LD      A,(HL)          
0599: C6 0F          ADD     $0F             
059B: 2F             CPL                     
059C: 12             LD      (DE),A          
059D: 2C             INC     L               
059E: 1C             INC     E               
059F: ED A0          LDI                     
05A1: 7E             LD      A,(HL)          
05A2: C6 0F          ADD     $0F             
05A4: 2F             CPL                     
05A5: 12             LD      (DE),A          
05A6: 2C             INC     L               
05A7: 1C             INC     E               
05A8: ED A0          LDI                     
05AA: 7E             LD      A,(HL)          
05AB: C6 0F          ADD     $0F             
05AD: 2F             CPL                     
05AE: 12             LD      (DE),A          
05AF: 2C             INC     L               
05B0: 1C             INC     E               
05B1: ED A0          LDI                     
05B3: 7E             LD      A,(HL)          
05B4: C6 0F          ADD     $0F             
05B6: 2F             CPL                     
05B7: 12             LD      (DE),A          
05B8: 2C             INC     L               
05B9: 1C             INC     E               
05BA: ED A0          LDI                     
05BC: 7E             LD      A,(HL)          
05BD: C6 0F          ADD     $0F             
05BF: 2F             CPL                     
05C0: 12             LD      (DE),A          
05C1: 2C             INC     L               
05C2: 1C             INC     E               
05C3: ED A0          LDI                     
05C5: 7E             LD      A,(HL)          
05C6: C6 0F          ADD     $0F             
05C8: 2F             CPL                     
05C9: 12             LD      (DE),A          
05CA: 2C             INC     L               
05CB: 1C             INC     E               
05CC: ED A0          LDI                     
05CE: 7E             LD      A,(HL)          
05CF: C6 0F          ADD     $0F             
05D1: 2F             CPL                     
05D2: 12             LD      (DE),A          
05D3: 2C             INC     L               
05D4: 1C             INC     E               
05D5: ED A0          LDI                     
05D7: 7E             LD      A,(HL)          
05D8: C6 0F          ADD     $0F             
05DA: 2F             CPL                     
05DB: 12             LD      (DE),A          
05DC: 2C             INC     L               
05DD: 1C             INC     E               
05DE: ED A0          LDI                     
05E0: 7E             LD      A,(HL)          
05E1: C6 0F          ADD     $0F             
05E3: 2F             CPL                     
05E4: 12             LD      (DE),A          
05E5: 2C             INC     L               
05E6: 1C             INC     E               
05E7: ED A0          LDI                     
05E9: 7E             LD      A,(HL)          
05EA: C6 0F          ADD     $0F             
05EC: 2F             CPL                     
05ED: 12             LD      (DE),A          
05EE: 2C             INC     L               
05EF: 1C             INC     E               
05F0: ED A0          LDI                     
05F2: 7E             LD      A,(HL)          
05F3: C6 0F          ADD     $0F             
05F5: 2F             CPL                     
05F6: 12             LD      (DE),A          
05F7: 2C             INC     L               
05F8: 1C             INC     E               
05F9: ED A0          LDI                     
05FB: 7E             LD      A,(HL)          
05FC: C6 0F          ADD     $0F             
05FE: 2F             CPL                     
05FF: 12             LD      (DE),A          
0600: 2C             INC     L               
0601: 1C             INC     E               
0602: ED A0          LDI                     
0604: 21 36 AA       LD      HL,$AA36        
0607: 7E             LD      A,(HL)          
0608: C6 0F          ADD     $0F             
060A: 2F             CPL                     
060B: 12             LD      (DE),A          
060C: 2C             INC     L               
060D: 1C             INC     E               
060E: ED A0          LDI                     
0610: 7E             LD      A,(HL)          
0611: C6 0F          ADD     $0F             
0613: 2F             CPL                     
0614: 12             LD      (DE),A          
0615: 2C             INC     L               
0616: 1C             INC     E               
0617: ED A0          LDI                     
0619: 7E             LD      A,(HL)          
061A: C6 0F          ADD     $0F             
061C: 2F             CPL                     
061D: 12             LD      (DE),A          
061E: 2C             INC     L               
061F: 1C             INC     E               
0620: ED A0          LDI                     
0622: 7E             LD      A,(HL)          
0623: C6 0F          ADD     $0F             
0625: 2F             CPL                     
0626: 12             LD      (DE),A          
0627: 2C             INC     L               
0628: 1C             INC     E               
0629: ED A0          LDI                     
062B: 7E             LD      A,(HL)          
062C: C6 0F          ADD     $0F             
062E: 2F             CPL                     
062F: 12             LD      (DE),A          
0630: 2C             INC     L               
0631: 1C             INC     E               
0632: ED A0          LDI                     
0634: 21 60 AA       LD      HL,$AA60        
0637: 11 10 B4       LD      DE,$B410        
063A: 7E             LD      A,(HL)          
063B: EE C0          XOR     $C0             
063D: 12             LD      (DE),A          
063E: 2C             INC     L               
063F: 1C             INC     E               
0640: 7E             LD      A,(HL)          
0641: 3C             INC     A               
0642: 12             LD      (DE),A          
0643: 2C             INC     L               
0644: 1C             INC     E               
0645: 7E             LD      A,(HL)          
0646: EE C0          XOR     $C0             
0648: 12             LD      (DE),A          
0649: 2C             INC     L               
064A: 1C             INC     E               
064B: 7E             LD      A,(HL)          
064C: 3C             INC     A               
064D: 12             LD      (DE),A          
064E: 2C             INC     L               
064F: 1C             INC     E               
0650: 7E             LD      A,(HL)          
0651: EE C0          XOR     $C0             
0653: 12             LD      (DE),A          
0654: 2C             INC     L               
0655: 1C             INC     E               
0656: 7E             LD      A,(HL)          
0657: 3C             INC     A               
0658: 12             LD      (DE),A          
0659: 2C             INC     L               
065A: 1C             INC     E               
065B: 21 40 AA       LD      HL,$AA40        
065E: 7E             LD      A,(HL)          
065F: EE C0          XOR     $C0             
0661: 12             LD      (DE),A          
0662: 2C             INC     L               
0663: 1C             INC     E               
0664: 7E             LD      A,(HL)          
0665: 3C             INC     A               
0666: 12             LD      (DE),A          
0667: 2C             INC     L               
0668: 1C             INC     E               
0669: 7E             LD      A,(HL)          
066A: EE C0          XOR     $C0             
066C: 12             LD      (DE),A          
066D: 2C             INC     L               
066E: 1C             INC     E               
066F: 7E             LD      A,(HL)          
0670: 3C             INC     A               
0671: 12             LD      (DE),A          
0672: 2C             INC     L               
0673: 1C             INC     E               
0674: 7E             LD      A,(HL)          
0675: EE C0          XOR     $C0             
0677: 12             LD      (DE),A          
0678: 2C             INC     L               
0679: 1C             INC     E               
067A: 7E             LD      A,(HL)          
067B: 3C             INC     A               
067C: 12             LD      (DE),A          
067D: 2C             INC     L               
067E: 1C             INC     E               
067F: 7E             LD      A,(HL)          
0680: EE C0          XOR     $C0             
0682: 12             LD      (DE),A          
0683: 2C             INC     L               
0684: 1C             INC     E               
0685: 7E             LD      A,(HL)          
0686: 3C             INC     A               
0687: 12             LD      (DE),A          
0688: 2C             INC     L               
0689: 1C             INC     E               
068A: 7E             LD      A,(HL)          
068B: EE C0          XOR     $C0             
068D: 12             LD      (DE),A          
068E: 2C             INC     L               
068F: 1C             INC     E               
0690: 7E             LD      A,(HL)          
0691: 3C             INC     A               
0692: 12             LD      (DE),A          
0693: 2C             INC     L               
0694: 1C             INC     E               
0695: 7E             LD      A,(HL)          
0696: EE C0          XOR     $C0             
0698: 12             LD      (DE),A          
0699: 2C             INC     L               
069A: 1C             INC     E               
069B: 7E             LD      A,(HL)          
069C: 3C             INC     A               
069D: 12             LD      (DE),A          
069E: 2C             INC     L               
069F: 1C             INC     E               
06A0: 7E             LD      A,(HL)          
06A1: EE C0          XOR     $C0             
06A3: 12             LD      (DE),A          
06A4: 2C             INC     L               
06A5: 1C             INC     E               
06A6: 7E             LD      A,(HL)          
06A7: 3C             INC     A               
06A8: 12             LD      (DE),A          
06A9: 2C             INC     L               
06AA: 1C             INC     E               
06AB: 7E             LD      A,(HL)          
06AC: EE C0          XOR     $C0             
06AE: 12             LD      (DE),A          
06AF: 2C             INC     L               
06B0: 1C             INC     E               
06B1: 7E             LD      A,(HL)          
06B2: 3C             INC     A               
06B3: 12             LD      (DE),A          
06B4: 2C             INC     L               
06B5: 1C             INC     E               
06B6: 7E             LD      A,(HL)          
06B7: EE C0          XOR     $C0             
06B9: 12             LD      (DE),A          
06BA: 2C             INC     L               
06BB: 1C             INC     E               
06BC: 7E             LD      A,(HL)          
06BD: 3C             INC     A               
06BE: 12             LD      (DE),A          
06BF: 2C             INC     L               
06C0: 1C             INC     E               
06C1: 7E             LD      A,(HL)          
06C2: EE C0          XOR     $C0             
06C4: 12             LD      (DE),A          
06C5: 2C             INC     L               
06C6: 1C             INC     E               
06C7: 7E             LD      A,(HL)          
06C8: 3C             INC     A               
06C9: 12             LD      (DE),A          
06CA: 2C             INC     L               
06CB: 1C             INC     E               
06CC: 7E             LD      A,(HL)          
06CD: EE C0          XOR     $C0             
06CF: 12             LD      (DE),A          
06D0: 2C             INC     L               
06D1: 1C             INC     E               
06D2: 7E             LD      A,(HL)          
06D3: 3C             INC     A               
06D4: 12             LD      (DE),A          
06D5: 2C             INC     L               
06D6: 1C             INC     E               
06D7: 7E             LD      A,(HL)          
06D8: EE C0          XOR     $C0             
06DA: 12             LD      (DE),A          
06DB: 2C             INC     L               
06DC: 1C             INC     E               
06DD: 7E             LD      A,(HL)          
06DE: 3C             INC     A               
06DF: 12             LD      (DE),A          
06E0: 2C             INC     L               
06E1: 1C             INC     E               
06E2: 7E             LD      A,(HL)          
06E3: EE C0          XOR     $C0             
06E5: 12             LD      (DE),A          
06E6: 2C             INC     L               
06E7: 1C             INC     E               
06E8: 7E             LD      A,(HL)          
06E9: 3C             INC     A               
06EA: 12             LD      (DE),A          
06EB: 2C             INC     L               
06EC: 1C             INC     E               
06ED: 7E             LD      A,(HL)          
06EE: EE C0          XOR     $C0             
06F0: 12             LD      (DE),A          
06F1: 2C             INC     L               
06F2: 1C             INC     E               
06F3: 7E             LD      A,(HL)          
06F4: 3C             INC     A               
06F5: 12             LD      (DE),A          
06F6: 2C             INC     L               
06F7: 1C             INC     E               
06F8: 7E             LD      A,(HL)          
06F9: EE C0          XOR     $C0             
06FB: 12             LD      (DE),A          
06FC: 2C             INC     L               
06FD: 1C             INC     E               
06FE: 7E             LD      A,(HL)          
06FF: 3C             INC     A               
0700: 12             LD      (DE),A          
0701: 2C             INC     L               
0702: 1C             INC     E               
0703: 7E             LD      A,(HL)          
0704: EE C0          XOR     $C0             
0706: 12             LD      (DE),A          
0707: 2C             INC     L               
0708: 1C             INC     E               
0709: 7E             LD      A,(HL)          
070A: 3C             INC     A               
070B: 12             LD      (DE),A          
070C: 2C             INC     L               
070D: 1C             INC     E               
070E: 21 66 AA       LD      HL,$AA66        
0711: 7E             LD      A,(HL)          
0712: EE C0          XOR     $C0             
0714: 12             LD      (DE),A          
0715: 2C             INC     L               
0716: 1C             INC     E               
0717: 7E             LD      A,(HL)          
0718: 3C             INC     A               
0719: 12             LD      (DE),A          
071A: 2C             INC     L               
071B: 1C             INC     E               
071C: 7E             LD      A,(HL)          
071D: EE C0          XOR     $C0             
071F: 12             LD      (DE),A          
0720: 2C             INC     L               
0721: 1C             INC     E               
0722: 7E             LD      A,(HL)          
0723: 3C             INC     A               
0724: 12             LD      (DE),A          
0725: 2C             INC     L               
0726: 1C             INC     E               
0727: 7E             LD      A,(HL)          
0728: EE C0          XOR     $C0             
072A: 12             LD      (DE),A          
072B: 2C             INC     L               
072C: 1C             INC     E               
072D: 7E             LD      A,(HL)          
072E: 3C             INC     A               
072F: 12             LD      (DE),A          
0730: 2C             INC     L               
0731: 1C             INC     E               
0732: 7E             LD      A,(HL)          
0733: EE C0          XOR     $C0             
0735: 12             LD      (DE),A          
0736: 2C             INC     L               
0737: 1C             INC     E               
0738: 7E             LD      A,(HL)          
0739: 3C             INC     A               
073A: 12             LD      (DE),A          
073B: 2C             INC     L               
073C: 1C             INC     E               
073D: 7E             LD      A,(HL)          
073E: EE C0          XOR     $C0             
0740: 12             LD      (DE),A          
0741: 2C             INC     L               
0742: 1C             INC     E               
0743: 7E             LD      A,(HL)          
0744: 3C             INC     A               
0745: 12             LD      (DE),A          
0746: 2C             INC     L               
0747: 1C             INC     E               
0748: C3 BC 04       JP      $04BC           
074B: 06 00          LD      B,$00           
074D: 21 A0 4A       LD      HL,$4AA0        
0750: AF             XOR     A               
0751: 86             ADD     A,(HL)          
0752: 23             INC     HL              
0753: 10 FC          DJNZ    $751            
0755: D6 B8          SUB     $B8             
0757: C2 FA 08       JP      NZ,$08FA        
075A: 3A 0C AD       LD      A,($AD0C)       
075D: FE 05          CP      $05             
075F: F5             PUSH    AF              
0760: 3E 05          LD      A,$05           
0762: 32 0C AD       LD      ($AD0C),A       
0765: 3E F1          LD      A,$F1           
0767: 32 0B AD       LD      ($AD0B),A       
076A: CD E1 01       CALL    $01E1           
076D: F1             POP     AF              
076E: CC 1A 0F       CALL    Z,$0F1A         
0771: C3 1A 0F       JP      $0F1A           
0774: 06 00          LD      B,$00           
0776: 21 99 4C       LD      HL,$4C99        
0779: 97             SUB     A               
077A: AE             XOR     (HL)            
077B: 23             INC     HL              
077C: 10 FC          DJNZ    $77A            
077E: C6 95          ADD     $95             
0780: C4 11 0F       CALL    NZ,$0F11        
0783: 3A 30 AD       LD      A,($AD30)       
0786: A7             AND     A               
0787: 28 17          JR      Z,$7A0          
0789: ED 5B 5B 12    LD      DE,($125B)      
078D: 3A 32 AD       LD      A,($AD32)       
0790: A7             AND     A               
0791: 28 01          JR      Z,$794          
0793: 1C             INC     E               
0794: FF             RST     0X38            
0795: 3A 0E AD       LD      A,($AD0E)       
0798: A7             AND     A               
0799: 28 05          JR      Z,$7A0          
079B: 16 07          LD      D,$07           
079D: FF             RST     0X38            
079E: 18 04          JR      $7A4            
07A0: 11 02 02       LD      DE,$0202        
07A3: FF             RST     0X38            
07A4: CD 09 08       CALL    $0809           
07A7: CD F0 19       CALL    $19F0           
07AA: C3 1A 0F       JP      $0F1A           
07AD: 47             LD      B,A             
07AE: C3 03 53       JP      $5303           

; Startup comes here
07B1: 3A 00 60       LD      A,($6000)       
07B4: FE 55          CP      $55             
07B6: CA 00 60       JP      Z,$6000         
07B9: 31 00 B0       LD      SP,$B000        
07BC: 32 00 C2       LD      ($C200),A       
07BF: 21 00 C3       LD      HL,$C300        
07C2: 06 08          LD      B,$08           
07C4: 36 00          LD      (HL),$00        
07C6: 23             INC     HL              
07C7: 10 FB          DJNZ    $7C4            
07C9: 3A 4B 2D       LD      A,($2D4B)       
07CC: 32 08 C3       LD      ($C308),A       
07CF: C3 69 00       JP      $0069           
07D2: 21 9F A7       LD      HL,$A79F        
07D5: 11 E0 FF       LD      DE,$FFE0        
07D8: 06 0E          LD      B,$0E           
07DA: 36 F1          LD      (HL),$F1        
07DC: CB 94          RES     2,H             
07DE: 36 16          LD      (HL),$16        
07E0: CB D4          SET     2,H             
07E2: 19             ADD     HL,DE           
07E3: 10 F5          DJNZ    $7DA            
07E5: C9             RET                     
07E6: CD 06 0B       CALL    $0B06           
07E9: CD 39 0B       CALL    $0B39           
07EC: 21 1C A6       LD      HL,$A61C        
07EF: 11 FE AB       LD      DE,$ABFE        
07F2: CD FC 1A       CALL    $1AFC           
07F5: 3A AE A9       LD      A,($A9AE)       
07F8: CB 5F          BIT     3,A             
07FA: C2 15 32       JP      NZ,$3215        
07FD: 3A 86 A9       LD      A,($A986)       
0800: 3D             DEC     A               
0801: C8             RET     Z               
0802: 11 19 01       LD      DE,$0119        
0805: FF             RST     0X38            
0806: C3 1A 0F       JP      $0F1A           
0809: 3A 04 AD       LD      A,($AD04)       
080C: 87             ADD     A,A             
080D: 47             LD      B,A             
080E: 87             ADD     A,A             
080F: 87             ADD     A,A             
0810: 80             ADD     A,B             
0811: 21 7C 08       LD      HL,$087C        
0814: DF             RST     0X18            
0815: 46             LD      B,(HL)          
0816: 23             INC     HL              
0817: 4E             LD      C,(HL)          
0818: 23             INC     HL              
0819: 3A 02 AD       LD      A,($AD02)       
081C: 5F             LD      E,A             
081D: E6 07          AND     $07             
081F: CF             RST     0X08            
0820: 08             EX      AF,AF'          
0821: 7B             LD      A,E             
0822: 21 9F A7       LD      HL,$A79F        
0825: 11 E0 FF       LD      DE,$FFE0        
0828: 0F             RRCA                    
0829: 0F             RRCA                    
082A: E6 1F          AND     $1F             
082C: 28 0A          JR      Z,$838          
082E: 70             LD      (HL),B          
082F: 19             ADD     HL,DE           
0830: 3D             DEC     A               
0831: 28 05          JR      Z,$838          
0833: 71             LD      (HL),C          
0834: 19             ADD     HL,DE           
0835: 3D             DEC     A               
0836: 20 F6          JR      NZ,$82E         
0838: 08             EX      AF,AF'          
0839: 77             LD      (HL),A          
083A: 19             ADD     HL,DE           
083B: 36 F1          LD      (HL),$F1        
083D: C9             RET                     
083E: CD 39 0B       CALL    $0B39           
0841: CD 06 0B       CALL    $0B06           
0844: 11 00 01       LD      DE,$0100        
0847: 06 02          LD      B,$02           
0849: FF             RST     0X38            
084A: 1C             INC     E               
084B: 10 FC          DJNZ    $849            
084D: 1C             INC     E               
084E: 06 05          LD      B,$05           
0850: FF             RST     0X38            
0851: 1C             INC     E               
0852: 10 FC          DJNZ    $850            
0854: 1E 14          LD      E,$14           
0856: FF             RST     0X38            
0857: 1C             INC     E               
0858: FF             RST     0X38            
0859: 21 6A 17       LD      HL,$176A        
085C: 06 18          LD      B,$18           
085E: AF             XOR     A               
085F: AE             XOR     (HL)            
0860: 2C             INC     L               
0861: 10 FC          DJNZ    $85F            
0863: D6 C9          SUB     $C9             
0865: C2 FA 08       JP      NZ,$08FA        
0868: C3 1A 0F       JP      $0F1A           
086B: BC             CP      H               
086C: A6             AND     (HL)            
086D: 10 30          DJNZ    $89F            
086F: F1             POP     AF              
0870: 7C             LD      A,H             
0871: 68             LD      L,B             
0872: 3B             DEC     SP              
0873: A5             AND     L               
0874: 38 FD          JR      C,$873          
0876: F1             POP     AF              
0877: 96             SUB     (HL)            
0878: 5D             LD      E,L             
0879: 17             RLA                     
087A: 9B             SBC     E               
087B: B9             CP      C               
087C: 4C             LD      C,H             
087D: 4F             LD      C,A             
087E: F1             POP     AF              
087F: 41             LD      B,C             
0880: 72             LD      (HL),D          
0881: A6             AND     (HL)            
0882: F1             POP     AF              
0883: 8D             ADC     A,L             
0884: E2 FB 37       JP      PO,$37FB        
0887: A7             AND     A               
0888: F1             POP     AF              
0889: AB             XOR     E               
088A: 31 07 F1       LD      SP,$F107        
088D: 5A             LD      E,D             
088E: 75             LD      (HL),L          
088F: 85             ADD     A,L             
0890: D9             EXX                     
0891: 1B             DEC     DE              
0892: F1             POP     AF              
0893: C1             POP     BC              
0894: E1             POP     HL              
0895: FA F1 B3       JP      M,$B3F1         
0898: A0             AND     B               
0899: 47             LD      B,A             
089A: 7B             LD      A,E             
089B: 78             LD      A,B             
089C: F1             POP     AF              
089D: 04             INC     B               
089E: 05             DEC     B               
089F: C2 F1 DE       JP      NZ,$DEF1        
08A2: F9             LD      SP,HL           
08A3: BB             CP      E               
08A4: 93             SUB     E               
08A5: AC             XOR     H               
08A6: F1             POP     AF              
08A7: 36 06          LD      (HL),$06        
08A9: 4B             LD      C,E             
08AA: F1             POP     AF              
08AB: EE D3          XOR     $D3             
08AD: D4 21 5E       CALL    NC,$5E21        
08B0: 33             INC     SP              
08B1: 06 1E          LD      B,$1E           
08B3: C9             RET                     
08B4: CD 01 02       CALL    $0201           
08B7: C0             RET     NZ              
08B8: 06 00          LD      B,$00           
08BA: 21 80 48       LD      HL,$4880        
08BD: 97             SUB     A               
08BE: AE             XOR     (HL)            
08BF: 23             INC     HL              
08C0: 10 FC          DJNZ    $8BE            
08C2: C6 D0          ADD     $D0             
08C4: C2 D9 00       JP      NZ,$00D9        
08C7: 11 13 01       LD      DE,$0113        
08CA: FF             RST     0X38            
08CB: 1E 00          LD      E,$00           
08CD: FF             RST     0X38            
08CE: 1E 14          LD      E,$14           
08D0: FF             RST     0X38            
08D1: 1C             INC     E               
08D2: FF             RST     0X38            
08D3: 1E 0C          LD      E,$0C           
08D5: FF             RST     0X38            
08D6: CD DC 4B       CALL    $4BDC           
08D9: 21 95 A9       LD      HL,$A995        
08DC: AF             XOR     A               
08DD: 06 05          LD      B,$05           
08DF: 77             LD      (HL),A          
08E0: 23             INC     HL              
08E1: 10 FC          DJNZ    $8DF            
08E3: 36 03          LD      (HL),$03        
08E5: ED 5B 93 A9    LD      DE,($A993)      
08E9: 3A 99 A9       LD      A,($A999)       
08EC: 21 C7 12       LD      HL,$12C7        
08EF: CF             RST     0X08            
08F0: 12             LD      (DE),A          
08F1: CB 92          RES     2,D             
08F3: 1A             LD      A,(DE)          
08F4: 32 90 A9       LD      ($A990),A       
08F7: C3 1A 0F       JP      $0F1A           
08FA: 4B             LD      C,E             
08FB: 01 4A 01       LD      BC,$014A        
08FE: 49             LD      C,C             
08FF: 01 48 01       LD      BC,$0148        
0902: 47             LD      B,A             
0903: 01 46 01       LD      BC,$0146        
0906: 45             LD      B,L             
0907: 01 40 01       LD      BC,$0140        
090A: 3E 01          LD      A,$01           
090C: 3C             INC     A               
090D: 01 3A 01       LD      BC,$013A        
0910: 38 01          JR      C,$913          
0912: 32 01 2F       LD      ($2F01),A       
0915: 01 2D 01       LD      BC,$012D        
0918: 27             DAA                     
0919: 01 24 01       LD      BC,$0124        
091C: 21 01 1E       LD      HL,$1E01        
091F: 01 18 01       LD      BC,$0118        
0922: 15             DEC     D               
0923: 01 12 01       LD      BC,$0112        
0926: 0C             INC     C               
0927: 01 09 01       LD      BC,$0109        
092A: 06 01          LD      B,$01           
092C: 00             NOP                     
092D: 01 FD 00       LD      BC,$00FD        
0930: FA 00 F7       JP      M,$F700         
0933: 00             NOP                     
0934: F1             POP     AF              
0935: 00             NOP                     
0936: EE 00          XOR     $00             
0938: EB             EX      DE,HL           
0939: 00             NOP                     
093A: E5             PUSH    HL              
093B: 00             NOP                     
093C: E2 00 DE       JP      PO,$DE00        
093F: 00             NOP                     
0940: D8             RET     C               
0941: 00             NOP                     
0942: D5             PUSH    DE              
0943: 00             NOP                     
0944: D1             POP     DE              
0945: 00             NOP                     
0946: CA 00 C6       JP      Z,$C600         
0949: 00             NOP                     
094A: C3 00 BC       JP      $BC00           
094D: 00             NOP                     
094E: B6             OR      (HL)            
094F: 00             NOP                     
0950: AE             XOR     (HL)            
0951: 00             NOP                     
0952: A9             XOR     C               
0953: 00             NOP                     
0954: 9F             SBC     A               
0955: 00             NOP                     
0956: 9C             SBC     H               
0957: 00             NOP                     
0958: 93             SUB     E               
0959: 00             NOP                     
095A: 8A             ADC     A,D             
095B: 00             NOP                     
095C: 84             ADD     A,H             
095D: 00             NOP                     
095E: 7B             LD      A,E             
095F: 00             NOP                     
0960: 71             LD      (HL),C          
0961: 00             NOP                     
0962: 6B             LD      L,E             
0963: 00             NOP                     
0964: 61             LD      H,C             
0965: 00             NOP                     
0966: 57             LD      D,A             
0967: 00             NOP                     
0968: 50             LD      D,B             
0969: 00             NOP                     
096A: 45             LD      B,L             
096B: 00             NOP                     
096C: 3B             DEC     SP              
096D: 00             NOP                     
096E: 34             INC     (HL)            
096F: 00             NOP                     
0970: 29             ADD     HL,HL           
0971: 00             NOP                     
0972: 1E 00          LD      E,$00           
0974: 13             INC     DE              
0975: 00             NOP                     
0976: 08             EX      AF,AF'          
0977: 00             NOP                     
0978: 00             NOP                     
0979: 00             NOP                     
097A: 00             NOP                     
097B: 00             NOP                     
097C: F8             RET     M               
097D: FF             RST     0X38            
097E: ED                                  
097F: FF             RST     0X38            
0980: 00             NOP                     
0981: 00             NOP                     
0982: D7             RST     0X10            
0983: FF             RST     0X38            
0984: CC FF C5       CALL    Z,$C5FF         
0987: FF             RST     0X38            
0988: BB             CP      E               
0989: FF             RST     0X38            
098A: B0             OR      B               
098B: FF             RST     0X38            
098C: A9             XOR     C               
098D: FF             RST     0X38            
098E: 9F             SBC     A               
098F: FF             RST     0X38            
0990: 95             SUB     L               
0991: FF             RST     0X38            
0992: 8F             ADC     A,A             
0993: FF             RST     0X38            
0994: 85             ADD     A,L             
0995: FF             RST     0X38            
0996: 7C             LD      A,H             
0997: FF             RST     0X38            
0998: 76             HALT                    
0999: FF             RST     0X38            
099A: 6D             LD      L,L             
099B: FF             RST     0X38            
099C: 64             LD      H,H             
099D: FF             RST     0X38            
099E: 61             LD      H,C             
099F: FF             RST     0X38            
09A0: 64             LD      H,H             
09A1: FF             RST     0X38            
09A2: 52             LD      D,D             
09A3: FF             RST     0X38            
09A4: 4A             LD      C,D             
09A5: FF             RST     0X38            
09A6: 44             LD      B,H             
09A7: FF             RST     0X38            
09A8: 3D             DEC     A               
09A9: FF             RST     0X38            
09AA: 3A FF 36       LD      A,($36FF)       
09AD: FF             RST     0X38            
09AE: 2F             CPL                     
09AF: FF             RST     0X38            
09B0: 2B             DEC     HL              
09B1: FF             RST     0X38            
09B2: 28 FF          JR      Z,$9B3          
09B4: 22 FF 1E       LD      ($1EFF),HL      
09B7: FF             RST     0X38            
09B8: 1B             DEC     DE              
09B9: FF             RST     0X38            
09BA: 15             DEC     D               
09BB: FF             RST     0X38            
09BC: 12             LD      (DE),A          
09BD: FF             RST     0X38            
09BE: 0F             RRCA                    
09BF: FF             RST     0X38            
09C0: 0F             RRCA                    
09C1: FF             RST     0X38            
09C2: 06 FF          LD      B,$FF           
09C4: 03             INC     BC              
09C5: FF             RST     0X38            
09C6: 00             NOP                     
09C7: FF             RST     0X38            
09C8: FA FE F7       JP      M,$F7FE         
09CB: FE F4          CP      $F4             
09CD: FE EE          CP      $EE             
09CF: FE EB          CP      $EB             
09D1: FE E8          CP      $E8             
09D3: FE E2          CP      $E2             
09D5: FE DF          CP      $DF             
09D7: FE DC          CP      $DC             
09D9: FE D9          CP      $D9             
09DB: FE D3          CP      $D3             
09DD: FE D1          CP      $D1             
09DF: FE CE          CP      $CE             
09E1: FE C8          CP      $C8             
09E3: FE C6          CP      $C6             
09E5: FE C4          CP      $C4             
09E7: FE C2          CP      $C2             
09E9: FE C0          CP      $C0             
09EB: FE BB          CP      $BB             
09ED: FE BA          CP      $BA             
09EF: FE B9          CP      $B9             
09F1: FE B8          CP      $B8             
09F3: FE B7          CP      $B7             
09F5: FE B6          CP      $B6             
09F7: FE B5          CP      $B5             
09F9: FE B5          CP      $B5             
09FB: FE B6          CP      $B6             
09FD: FE B7          CP      $B7             
09FF: FE B8          CP      $B8             
0A01: FE B9          CP      $B9             
0A03: FE BA          CP      $BA             
0A05: FE BB          CP      $BB             
0A07: FE C0          CP      $C0             
0A09: FE C2          CP      $C2             
0A0B: FE C4          CP      $C4             
0A0D: FE C6          CP      $C6             
0A0F: FE C8          CP      $C8             
0A11: FE CE          CP      $CE             
0A13: FE D1          CP      $D1             
0A15: FE D3          CP      $D3             
0A17: FE D9          CP      $D9             
0A19: FE DC          CP      $DC             
0A1B: FE DF          CP      $DF             
0A1D: FE E2          CP      $E2             
0A1F: FE E8          CP      $E8             
0A21: FE EB          CP      $EB             
0A23: FE EE          CP      $EE             
0A25: FE F4          CP      $F4             
0A27: FE F7          CP      $F7             
0A29: FE FA          CP      $FA             
0A2B: FE 00          CP      $00             
0A2D: FF             RST     0X38            
0A2E: 03             INC     BC              
0A2F: FF             RST     0X38            
0A30: 06 FF          LD      B,$FF           
0A32: 09             ADD     HL,BC           
0A33: FF             RST     0X38            
0A34: 0F             RRCA                    
0A35: FF             RST     0X38            
0A36: 12             LD      (DE),A          
0A37: FF             RST     0X38            
0A38: 15             DEC     D               
0A39: FF             RST     0X38            
0A3A: 1B             DEC     DE              
0A3B: FF             RST     0X38            
0A3C: 1E FF          LD      E,$FF           
0A3E: 22 FF 28       LD      ($28FF),HL      
0A41: FF             RST     0X38            
0A42: 2B             DEC     HL              
0A43: FF             RST     0X38            
0A44: 2F             CPL                     
0A45: FF             RST     0X38            
0A46: 36 FF          LD      (HL),$FF        
0A48: 3A FF 3D       LD      A,($3DFF)       
0A4B: FF             RST     0X38            
0A4C: 44             LD      B,H             
0A4D: FF             RST     0X38            
0A4E: 4A             LD      C,D             
0A4F: FF             RST     0X38            
0A50: 52             LD      D,D             
0A51: FF             RST     0X38            
0A52: 57             LD      D,A             
0A53: FF             RST     0X38            
0A54: 61             LD      H,C             
0A55: FF             RST     0X38            
0A56: 64             LD      H,H             
0A57: FF             RST     0X38            
0A58: 6D             LD      L,L             
0A59: FF             RST     0X38            
0A5A: 76             HALT                    
0A5B: FF             RST     0X38            
0A5C: 7C             LD      A,H             
0A5D: FF             RST     0X38            
0A5E: 85             ADD     A,L             
0A5F: FF             RST     0X38            
0A60: 8F             ADC     A,A             
0A61: FF             RST     0X38            
0A62: 95             SUB     L               
0A63: FF             RST     0X38            
0A64: 9F             SBC     A               
0A65: FF             RST     0X38            
0A66: A9             XOR     C               
0A67: FF             RST     0X38            
0A68: B0             OR      B               
0A69: FF             RST     0X38            
0A6A: BB             CP      E               
0A6B: FF             RST     0X38            
0A6C: C5             PUSH    BC              
0A6D: FF             RST     0X38            
0A6E: CC FF D7       CALL    Z,$D7FF         
0A71: FF             RST     0X38            
0A72: E2 FF ED       JP      PO,$EDFF        
0A75: FF             RST     0X38            
0A76: F8             RET     M               
0A77: FF             RST     0X38            
0A78: 00             NOP                     
0A79: 00             NOP                     
0A7A: 00             NOP                     
0A7B: 00             NOP                     
0A7C: 08             EX      AF,AF'          
0A7D: 00             NOP                     
0A7E: 13             INC     DE              
0A7F: 00             NOP                     
0A80: 1E 00          LD      E,$00           
0A82: 29             ADD     HL,HL           
0A83: 00             NOP                     
0A84: 34             INC     (HL)            
0A85: 00             NOP                     
0A86: 3B             DEC     SP              
0A87: 00             NOP                     
0A88: 45             LD      B,L             
0A89: 00             NOP                     
0A8A: 50             LD      D,B             
0A8B: 00             NOP                     
0A8C: 57             LD      D,A             
0A8D: 00             NOP                     
0A8E: 61             LD      H,C             
0A8F: 00             NOP                     
0A90: 6B             LD      L,E             
0A91: 00             NOP                     
0A92: 71             LD      (HL),C          
0A93: 00             NOP                     
0A94: 7B             LD      A,E             
0A95: 00             NOP                     
0A96: 84             ADD     A,H             
0A97: 00             NOP                     
0A98: 8A             ADC     A,D             
0A99: 00             NOP                     
0A9A: 93             SUB     E               
0A9B: 00             NOP                     
0A9C: 9C             SBC     H               
0A9D: 00             NOP                     
0A9E: 9F             SBC     A               
0A9F: 00             NOP                     
0AA0: 9F             SBC     A               
0AA1: 00             NOP                     
0AA2: AE             XOR     (HL)            
0AA3: 00             NOP                     
0AA4: B6             OR      (HL)            
0AA5: 00             NOP                     
0AA6: BC             CP      H               
0AA7: 00             NOP                     
0AA8: C3 00 C6       JP      $C600           
0AAB: 00             NOP                     
0AAC: CA 00 D1       JP      Z,$D100         
0AAF: 00             NOP                     
0AB0: D5             PUSH    DE              
0AB1: 00             NOP                     
0AB2: D8             RET     C               
0AB3: 00             NOP                     
0AB4: DE 00          SBC     $00             
0AB6: E2 00 E5       JP      PO,$E500        
0AB9: 00             NOP                     
0ABA: EB             EX      DE,HL           
0ABB: 00             NOP                     
0ABC: EE 00          XOR     $00             
0ABE: F1             POP     AF              
0ABF: 00             NOP                     
0AC0: EE 00          XOR     $00             
0AC2: FA 00 FD       JP      M,$FD00         
0AC5: 00             NOP                     
0AC6: 00             NOP                     
0AC7: 01 06 01       LD      BC,$0106        
0ACA: 09             ADD     HL,BC           
0ACB: 01 0C 01       LD      BC,$010C        
0ACE: 12             LD      (DE),A          
0ACF: 01 15 01       LD      BC,$0115        
0AD2: 18 01          JR      $AD5            
0AD4: 1E 01          LD      E,$01           
0AD6: 21 01 24       LD      HL,$2401        
0AD9: 01 27 01       LD      BC,$0127        
0ADC: 2D             DEC     L               
0ADD: 01 2F 01       LD      BC,$012F        
0AE0: 27             DAA                     
0AE1: 01 38 01       LD      BC,$0138        
0AE4: 3A 01 3C       LD      A,($3C01)       
0AE7: 01 3E 01       LD      BC,$013E        
0AEA: 40             LD      B,B             
0AEB: 01 45 01       LD      BC,$0145        
0AEE: 46             LD      B,(HL)          
0AEF: 01 47 01       LD      BC,$0147        
0AF2: 48             LD      C,B             
0AF3: 01 49 01       LD      BC,$0149        
0AF6: 4A             LD      C,D             
0AF7: 01 4B 01       LD      BC,$014B        
0AFA: 77             LD      (HL),A          
0AFB: A6             AND     (HL)            
0AFC: 13             INC     DE              
0AFD: ED                                  
0AFE: DC A5 7D       CALL    C,$7DA5         
0B01: 34             INC     (HL)            
0B02: F1             POP     AF              
0B03: F1             POP     AF              
0B04: F1             POP     AF              
0B05: B9             CP      C               
0B06: FD 21 10 AA    LD      IY,$AA10        
0B0A: 06 04          LD      B,$04           
0B0C: 0E 04          LD      C,$04           
0B0E: 16 A0          LD      D,$A0           
0B10: 1E D8          LD      E,$D8           
0B12: FD 72 31       LD      (IY+$31),D      
0B15: FD 73 00       LD      (IY+$00),E      
0B18: FD 71 01       LD      (IY+$01),C      
0B1B: FD 36 30 6C    LD      (IY+$30),$6C    
0B1F: FD 23          INC     IY              
0B21: FD 23          INC     IY              
0B23: 0C             INC     C               
0B24: 7A             LD      A,D             
0B25: D6 10          SUB     $10             
0B27: 57             LD      D,A             
0B28: 10 E8          DJNZ    $B12            
0B2A: C9             RET                     
0B2B: 21 41 AA       LD      HL,$AA41        
0B2E: 11 02 00       LD      DE,$0002        
0B31: 06 04          LD      B,$04           
0B33: AF             XOR     A               
0B34: 77             LD      (HL),A          
0B35: 19             ADD     HL,DE           
0B36: 10 FC          DJNZ    $B34            
0B38: C9             RET                     
0B39: 3A 80 A9       LD      A,($A980)       
0B3C: CB 47          BIT     0,A             
0B3E: 28 06          JR      Z,$B46          
0B40: 11 00 01       LD      DE,$0100        
0B43: C3 38 00       JP      $0038           
0B46: 11 1F 01       LD      DE,$011F        
0B49: C3 38 00       JP      $0038           
0B4C: AF             XOR     A               
0B4D: 86             ADD     A,(HL)          
0B4E: 23             INC     HL              
0B4F: 10 FC          DJNZ    $B4D            
0B51: B9             CP      C               
0B52: C8             RET     Z               
0B53: C9             RET                     
0B54: AF             XOR     A               
0B55: AE             XOR     (HL)            
0B56: 23             INC     HL              
0B57: 10 FC          DJNZ    $B55            
0B59: B9             CP      C               
0B5A: C8             RET     Z               
0B5B: C3 00 00       JP      $0000           
0B5E: AF             XOR     A               
0B5F: 86             ADD     A,(HL)          
0B60: 23             INC     HL              
0B61: 0D             DEC     C               
0B62: 28 02          JR      Z,$B66          
0B64: 18 F9          JR      $B5F            
0B66: CB 47          BIT     0,A             
0B68: C8             RET     Z               
0B69: C3 00 00       JP      $0000           
0B6C: 21 06 0B       LD      HL,$0B06        
0B6F: 06 24          LD      B,$24           
0B71: 0E 00          LD      C,$00           
0B73: 7E             LD      A,(HL)          
0B74: 91             SUB     C               
0B75: 23             INC     HL              
0B76: 10 FB          DJNZ    $B73            
0B78: EB             EX      DE,HL           
0B79: BE             CP      (HL)            
0B7A: C9             RET                     
0B7B: 0F             RRCA                    
0B7C: A7             AND     A               
0B7D: 13             INC     DE              
0B7E: 88             ADC     A,B             
0B7F: 0D             DEC     C               
0B80: ED                                  
0B81: C4 F1 ED       CALL    NZ,$EDF1        
0B84: DC A5 D7       CALL    C,$D7A5         
0B87: DC F1 8C       CALL    C,$8CF1         
0B8A: 0D             DEC     C               
0B8B: DC DC 68       CALL    C,$68DC         
0B8E: 3B             DEC     SP              
0B8F: B9             CP      C               
0B90: C3 93 0B       JP      $0B93           
0B93: 26 AC          LD      H,$AC           
0B95: 3A B3 A9       LD      A,($A9B3)       
0B98: 6F             LD      L,A             
0B99: 7E             LD      A,(HL)          
0B9A: 07             RLCA                    
0B9B: DA 90 0B       JP      C,$0B90         
0B9E: 4E             LD      C,(HL)          
0B9F: 36 FF          LD      (HL),$FF        
0BA1: 23             INC     HL              
0BA2: 46             LD      B,(HL)          
0BA3: 36 FF          LD      (HL),$FF        
0BA5: 23             INC     HL              
0BA6: 7D             LD      A,L             
0BA7: E6 3F          AND     $3F             
0BA9: 32 B3 A9       LD      ($A9B3),A       
0BAC: 79             LD      A,C             
0BAD: E6 0F          AND     $0F             
0BAF: 21 BC 0B       LD      HL,$0BBC        
0BB2: CD 8C 01       CALL    $018C           
0BB5: 78             LD      A,B             
0BB6: 21 90 0B       LD      HL,$0B90        
0BB9: E5             PUSH    HL              
0BBA: EB             EX      DE,HL           
0BBB: E9             JP      (HL)            
0BBC: DD                                  
0BBD: 0B             DEC     BC              
0BBE: F2 0B 0F       JP      P,$0F0B         
0BC1: 0C             INC     C               
0BC2: 39             ADD     HL,SP           
0BC3: 0C             INC     C               
0BC4: 90             SUB     B               
0BC5: 0C             INC     C               
0BC6: 72             LD      (HL),D          
0BC7: 4D             LD      C,L             
0BC8: D7             RST     0X10            
0BC9: 0D             DEC     C               
0BCA: AC             XOR     H               
0BCB: 0E DC          LD      C,$DC           
0BCD: 0B             DEC     BC              
0BCE: DC 0B 21       CALL    C,$210B         
0BD1: 34             INC     (HL)            
0BD2: 23             INC     HL              
0BD3: 0C             INC     C               
0BD4: DC 0B DC       CALL    C,$DC0B         
0BD7: 0B             DEC     BC              
0BD8: DC 0B DC       CALL    C,$DC0B         
0BDB: 0B             DEC     BC              
0BDC: C9             RET                     
0BDD: 21 50 0C       LD      HL,$0C50        
0BE0: CD 8C 01       CALL    $018C           
0BE3: EB             EX      DE,HL           
0BE4: 5E             LD      E,(HL)          
0BE5: 23             INC     HL              
0BE6: 56             LD      D,(HL)          
0BE7: 23             INC     HL              
0BE8: 23             INC     HL              
0BE9: 7E             LD      A,(HL)          
0BEA: FE B9          CP      $B9             
0BEC: C8             RET     Z               
0BED: 12             LD      (DE),A          
0BEE: 23             INC     HL              
0BEF: E7             RST     0X20            
0BF0: 18 F7          JR      $BE9            
0BF2: 21 50 0C       LD      HL,$0C50        
0BF5: CD 8C 01       CALL    $018C           
0BF8: EB             EX      DE,HL           
0BF9: 5E             LD      E,(HL)          
0BFA: 23             INC     HL              
0BFB: 56             LD      D,(HL)          
0BFC: 23             INC     HL              
0BFD: 4E             LD      C,(HL)          
0BFE: 23             INC     HL              
0BFF: 7E             LD      A,(HL)          
0C00: FE B9          CP      $B9             
0C02: C8             RET     Z               
0C03: 12             LD      (DE),A          
0C04: CB 92          RES     2,D             
0C06: 79             LD      A,C             
0C07: 12             LD      (DE),A          
0C08: CB D2          SET     2,D             
0C0A: 23             INC     HL              
0C0B: E7             RST     0X20            
0C0C: C3 FF 0B       JP      $0BFF           
0C0F: 21 50 0C       LD      HL,$0C50        
0C12: CD 8C 01       CALL    $018C           
0C15: EB             EX      DE,HL           
0C16: 5E             LD      E,(HL)          
0C17: 23             INC     HL              
0C18: 56             LD      D,(HL)          
0C19: 23             INC     HL              
0C1A: 23             INC     HL              
0C1B: 3A 0C AD       LD      A,($AD0C)       
0C1E: E6 0F          AND     $0F             
0C20: 4F             LD      C,A             
0C21: 18 DC          JR      $BFF            
0C23: 21 50 0C       LD      HL,$0C50        
0C26: CD 8C 01       CALL    $018C           
0C29: EB             EX      DE,HL           
0C2A: 5E             LD      E,(HL)          
0C2B: 23             INC     HL              
0C2C: 56             LD      D,(HL)          
0C2D: 23             INC     HL              
0C2E: 23             INC     HL              
0C2F: 3A 0C AD       LD      A,($AD0C)       
0C32: C6 0A          ADD     $0A             
0C34: E6 0F          AND     $0F             
0C36: 4F             LD      C,A             
0C37: 18 C6          JR      $BFF            
0C39: 21 50 0C       LD      HL,$0C50        
0C3C: CD 8C 01       CALL    $018C           
0C3F: EB             EX      DE,HL           
0C40: 5E             LD      E,(HL)          
0C41: 23             INC     HL              
0C42: 56             LD      D,(HL)          
0C43: 23             INC     HL              
0C44: 23             INC     HL              
0C45: 7E             LD      A,(HL)          
0C46: FE B9          CP      $B9             
0C48: C8             RET     Z               
0C49: 3E F1          LD      A,$F1           
0C4B: 12             LD      (DE),A          
0C4C: 23             INC     HL              
0C4D: E7             RST     0X20            
0C4E: 18 F5          JR      $C45            
0C50: 6B             LD      L,E             
0C51: 08             EX      AF,AF'          
0C52: 73             LD      (HL),E          
0C53: 16 7F          LD      D,$7F           
0C55: 30 1D          JR      NC,$C74         
0C57: 58             LD      E,B             
0C58: FA 49 D6       JP      M,$D649         
0C5B: 15             DEC     D               
0C5C: 4C             LD      C,H             
0C5D: 58             LD      E,B             
0C5E: 09             ADD     HL,BC           
0C5F: 25             DEC     H               
0C60: CA 15 67       JP      Z,$6715         
0C63: 01 42 4E       LD      BC,$4E42        
0C66: 10 18          DJNZ    $C80            
0C68: CE 48          ADC     $48             
0C6A: A4             AND     H               
0C6B: 1B             DEC     DE              
0C6C: FA 0A 31       JP      M,$310A         
0C6F: 24             INC     H               
0C70: 3B             DEC     SP              
0C71: 12             LD      (DE),A          
0C72: 9B             SBC     E               
0C73: 45             LD      B,L             
0C74: A4             AND     H               
0C75: 2C             INC     L               
0C76: 4F             LD      C,A             
0C77: 00             NOP                     
0C78: 9E             SBC     (HL)            
0C79: 31 6E 29       LD      SP,$296E        
0C7C: 7B             LD      A,E             
0C7D: 0B             DEC     BC              
0C7E: 5C             LD      E,H             
0C7F: 34             INC     (HL)            
0C80: D2 3E 48       JP      NC,$483E        
0C83: 33             INC     SP              
0C84: 49             LD      C,C             
0C85: 0F             RRCA                    
0C86: 14             INC     D               
0C87: 4C             LD      C,H             
0C88: 54             LD      D,H             
0C89: 59             LD      E,C             
0C8A: ED                                  
0C8B: 55             LD      D,L             
0C8C: D8             RET     C               
0C8D: 23             INC     HL              
0C8E: 00             NOP                     
0C8F: 49             LD      C,C             
0C90: 4F             LD      C,A             
0C91: 06 00          LD      B,$00           
0C93: 3A 30 AD       LD      A,($AD30)       
0C96: A7             AND     A               
0C97: CA E8 0C       JP      Z,$0CE8         
0C9A: 79             LD      A,C             
0C9B: A7             AND     A               
0C9C: CA E9 0C       JP      Z,$0CE9         
0C9F: 21 27 0D       LD      HL,$0D27        
0CA2: 09             ADD     HL,BC           
0CA3: 09             ADD     HL,BC           
0CA4: 09             ADD     HL,BC           
0CA5: 11 33 AD       LD      DE,$AD33        
0CA8: 3A 32 AD       LD      A,($AD32)       
0CAB: A7             AND     A               
0CAC: 28 03          JR      Z,$CB1          
0CAE: 11 36 AD       LD      DE,$AD36        
0CB1: 1A             LD      A,(DE)          
0CB2: 86             ADD     A,(HL)          
0CB3: 27             DAA                     
0CB4: 12             LD      (DE),A          
0CB5: 13             INC     DE              
0CB6: 23             INC     HL              
0CB7: 1A             LD      A,(DE)          
0CB8: 8E             ADC     A,(HL)          
0CB9: 27             DAA                     
0CBA: 12             LD      (DE),A          
0CBB: 13             INC     DE              
0CBC: 23             INC     HL              
0CBD: 1A             LD      A,(DE)          
0CBE: 8E             ADC     A,(HL)          
0CBF: 27             DAA                     
0CC0: 12             LD      (DE),A          
0CC1: 21 8D A9       LD      HL,$A98D        
0CC4: 01 03 00       LD      BC,$0003        
0CC7: 1A             LD      A,(DE)          
0CC8: BE             CP      (HL)            
0CC9: 38 0F          JR      C,$CDA          
0CCB: 20 07          JR      NZ,$CD4         
0CCD: 1B             DEC     DE              
0CCE: 2B             DEC     HL              
0CCF: 0D             DEC     C               
0CD0: 20 F5          JR      NZ,$CC7         
0CD2: 18 06          JR      $CDA            
0CD4: EB             EX      DE,HL           
0CD5: ED B8          LDDR                    
0CD7: CD 6B 0D       CALL    $0D6B           
0CDA: 3A 32 AD       LD      A,($AD32)       
0CDD: A7             AND     A               
0CDE: 20 05          JR      NZ,$CE5         
0CE0: CD 57 0D       CALL    $0D57           
0CE3: 18 03          JR      $CE8            
0CE5: CD 61 0D       CALL    $0D61           
0CE8: C9             RET                     
0CE9: 3A 31 AD       LD      A,($AD31)       
0CEC: A7             AND     A               
0CED: 20 1B          JR      NZ,$D0A         
0CEF: 3A 31 0B       LD      A,($0B31)       
0CF2: CD F2 0B       CALL    $0BF2           
0CF5: CD 57 0D       CALL    $0D57           
0CF8: 3A C6 15       LD      A,($15C6)       
0CFB: CD 39 0C       CALL    $0C39           
0CFE: 11 01 A5       LD      DE,$A501        
0D01: 06 06          LD      B,$06           
0D03: 3E F1          LD      A,$F1           
0D05: 12             LD      (DE),A          
0D06: E7             RST     0X20            
0D07: 10 FA          DJNZ    $D03            
0D09: C9             RET                     
0D0A: 3E 06          LD      A,$06           
0D0C: CD F2 0B       CALL    $0BF2           
0D0F: CD 57 0D       CALL    $0D57           
0D12: 3E 07          LD      A,$07           
0D14: CD F2 0B       CALL    $0BF2           
0D17: CD 61 0D       CALL    $0D61           
0D1A: C9             RET                     
0D1B: 3C             INC     A               
0D1C: A2             AND     D               
0D1D: C7             RST     0X00            
0D1E: AC             XOR     H               
0D1F: 7C             LD      A,H             
0D20: A2             AND     D               
0D21: 43             LD      B,E             
0D22: AB             XOR     E               
0D23: FC A1 BE       CALL    M,$BEA1         
0D26: AC             XOR     H               
0D27: 00             NOP                     
0D28: 00             NOP                     
0D29: 00             NOP                     
0D2A: 00             NOP                     
0D2B: 01 00 00       LD      BC,$0000        
0D2E: 02             LD      (BC),A          
0D2F: 00             NOP                     
0D30: 00             NOP                     
0D31: 03             INC     BC              
0D32: 00             NOP                     
0D33: 00             NOP                     
0D34: 04             INC     B               
0D35: 00             NOP                     
0D36: 00             NOP                     
0D37: 05             DEC     B               
0D38: 00             NOP                     
0D39: 00             NOP                     
0D3A: 06 00          LD      B,$00           
0D3C: 00             NOP                     
0D3D: 07             RLCA                    
0D3E: 00             NOP                     
0D3F: 00             NOP                     
0D40: 08             EX      AF,AF'          
0D41: 00             NOP                     
0D42: 00             NOP                     
0D43: 09             ADD     HL,BC           
0D44: 00             NOP                     
0D45: 00             NOP                     
0D46: 10 00          DJNZ    $D48            
0D48: 00             NOP                     
0D49: 15             DEC     D               
0D4A: 00             NOP                     
0D4B: 00             NOP                     
0D4C: 20 00          JR      NZ,$D4E         
0D4E: 00             NOP                     
0D4F: 30 00          JR      NC,$D51         
0D51: 00             NOP                     
0D52: 40             LD      B,B             
0D53: 00             NOP                     
0D54: 00             NOP                     
0D55: 50             LD      D,B             
0D56: 00             NOP                     
0D57: 11 81 A7       LD      DE,$A781        
0D5A: 21 35 AD       LD      HL,$AD35        
0D5D: 0E 10          LD      C,$10           
0D5F: 18 12          JR      $D73            
0D61: 11 01 A5       LD      DE,$A501        
0D64: 21 38 AD       LD      HL,$AD38        
0D67: 0E 10          LD      C,$10           
0D69: 18 08          JR      $D73            
0D6B: 11 41 A6       LD      DE,$A641        
0D6E: 21 8D A9       LD      HL,$A98D        
0D71: 0E 10          LD      C,$10           
0D73: 06 00          LD      B,$00           
0D75: CD A0 0D       CALL    $0DA0           
0D78: 2B             DEC     HL              
0D79: CD A0 0D       CALL    $0DA0           
0D7C: 2B             DEC     HL              
0D7D: CD 81 0D       CALL    $0D81           
0D80: C9             RET                     
0D81: 7E             LD      A,(HL)          
0D82: 0F             RRCA                    
0D83: 0F             RRCA                    
0D84: 0F             RRCA                    
0D85: 0F             RRCA                    
0D86: CD 90 0D       CALL    $0D90           
0D89: E7             RST     0X20            
0D8A: 7E             LD      A,(HL)          
0D8B: CD 90 0D       CALL    $0D90           
0D8E: E7             RST     0X20            
0D8F: C9             RET                     
0D90: E6 0F          AND     $0F             
0D92: E5             PUSH    HL              
0D93: 21 CC 0D       LD      HL,$0DCC        
0D96: CF             RST     0X08            
0D97: E1             POP     HL              
0D98: 12             LD      (DE),A          
0D99: CB 92          RES     2,D             
0D9B: 79             LD      A,C             
0D9C: 12             LD      (DE),A          
0D9D: CB D2          SET     2,D             
0D9F: C9             RET                     
0DA0: 7E             LD      A,(HL)          
0DA1: 0F             RRCA                    
0DA2: 0F             RRCA                    
0DA3: 0F             RRCA                    
0DA4: 0F             RRCA                    
0DA5: CD AF 0D       CALL    $0DAF           
0DA8: E7             RST     0X20            
0DA9: 7E             LD      A,(HL)          
0DAA: CD AF 0D       CALL    $0DAF           
0DAD: E7             RST     0X20            
0DAE: C9             RET                     
0DAF: E6 0F          AND     $0F             
0DB1: 28 03          JR      Z,$DB6          
0DB3: 04             INC     B               
0DB4: 18 08          JR      $DBE            
0DB6: 3A 46 32       LD      A,($3246)       
0DB9: 04             INC     B               
0DBA: 05             DEC     B               
0DBB: 28 01          JR      Z,$DBE          
0DBD: AF             XOR     A               
0DBE: E5             PUSH    HL              
0DBF: 21 CC 0D       LD      HL,$0DCC        
0DC2: CF             RST     0X08            
0DC3: E1             POP     HL              
0DC4: 12             LD      (DE),A          
0DC5: CB 92          RES     2,D             
0DC7: 79             LD      A,C             
0DC8: 12             LD      (DE),A          
0DC9: CB D2          SET     2,D             
0DCB: C9             RET                     
0DCC: 13             INC     DE              
0DCD: 96             SUB     (HL)            
0DCE: 9B             SBC     E               
0DCF: CD F3 7F       CALL    $7FF3           
0DD2: 65             LD      H,L             
0DD3: 02             LD      (BC),A          
0DD4: 17             RLA                     
0DD5: 5D             LD      E,L             
0DD6: F1             POP     AF              
0DD7: 11 63 A4       LD      DE,$A463        
0DDA: FE 64          CP      $64             
0DDC: 38 02          JR      C,$DE0          
0DDE: 3E 63          LD      A,$63           
0DE0: D9             EXX                     
0DE1: 06 00          LD      B,$00           
0DE3: D6 1E          SUB     $1E             
0DE5: 38 03          JR      C,$DEA          
0DE7: 04             INC     B               
0DE8: 18 F9          JR      $DE3            
0DEA: C6 1E          ADD     $1E             
0DEC: 0E 00          LD      C,$00           
0DEE: D6 0A          SUB     $0A             
0DF0: 38 03          JR      C,$DF5          
0DF2: 0C             INC     C               
0DF3: 18 F9          JR      $DEE            
0DF5: C6 0A          ADD     $0A             
0DF7: 16 00          LD      D,$00           
0DF9: D6 05          SUB     $05             
0DFB: 38 03          JR      C,$E00          
0DFD: 14             INC     D               
0DFE: 18 F9          JR      $DF9            
0E00: C6 05          ADD     $05             
0E02: 5F             LD      E,A             
0E03: D9             EXX                     
0E04: D9             EXX                     
0E05: 7B             LD      A,E             
0E06: D9             EXX                     
0E07: A7             AND     A               
0E08: 28 0C          JR      Z,$E16          
0E0A: 06 01          LD      B,$01           
0E0C: 0E 13          LD      C,$13           
0E0E: 08             EX      AF,AF'          
0E0F: CD 8D 0E       CALL    $0E8D           
0E12: 08             EX      AF,AF'          
0E13: 3D             DEC     A               
0E14: 20 F8          JR      NZ,$E0E         
0E16: D9             EXX                     
0E17: 7A             LD      A,D             
0E18: D9             EXX                     
0E19: A7             AND     A               
0E1A: 28 0C          JR      Z,$E28          
0E1C: 06 32          LD      B,$32           
0E1E: 0E 11          LD      C,$11           
0E20: 08             EX      AF,AF'          
0E21: CD 9C 0E       CALL    $0E9C           
0E24: 08             EX      AF,AF'          
0E25: 3D             DEC     A               
0E26: 20 F8          JR      NZ,$E20         
0E28: D9             EXX                     
0E29: 79             LD      A,C             
0E2A: D9             EXX                     
0E2B: A7             AND     A               
0E2C: 28 0C          JR      Z,$E3A          
0E2E: 06 CE          LD      B,$CE           
0E30: 0E 16          LD      C,$16           
0E32: 08             EX      AF,AF'          
0E33: CD 70 0E       CALL    $0E70           
0E36: 08             EX      AF,AF'          
0E37: 3D             DEC     A               
0E38: 20 F8          JR      NZ,$E32         
0E3A: D9             EXX                     
0E3B: 78             LD      A,B             
0E3C: D9             EXX                     
0E3D: A7             AND     A               
0E3E: 28 0C          JR      Z,$E4C          
0E40: 06 23          LD      B,$23           
0E42: 0E 11          LD      C,$11           
0E44: 08             EX      AF,AF'          
0E45: CD 70 0E       CALL    $0E70           
0E48: 08             EX      AF,AF'          
0E49: 3D             DEC     A               
0E4A: 20 F8          JR      NZ,$E44         
0E4C: 01 10 F1       LD      BC,$F110        
0E4F: 21 DD 59       LD      HL,$59DD        
0E52: 19             ADD     HL,DE           
0E53: 38 05          JR      C,$E5A          
0E55: CD 8D 0E       CALL    $0E8D           
0E58: 18 F5          JR      $E4F            
0E5A: AF             XOR     A               
0E5B: 2A A0 00       LD      HL,($00A0)      
0E5E: ED 5B A3 00    LD      DE,($00A3)      
0E62: ED 4B 9D 00    LD      BC,($009D)      
0E66: 19             ADD     HL,DE           
0E67: 09             ADD     HL,BC           
0E68: 85             ADD     A,L             
0E69: 84             ADD     A,H             
0E6A: D6 69          SUB     $69             
0E6C: C2 00 00       JP      NZ,$0000        
0E6F: C9             RET                     
0E70: 78             LD      A,B             
0E71: 3C             INC     A               
0E72: 12             LD      (DE),A          
0E73: 3D             DEC     A               
0E74: 1B             DEC     DE              
0E75: 12             LD      (DE),A          
0E76: EF             RST     0X28            
0E77: 78             LD      A,B             
0E78: C6 02          ADD     $02             
0E7A: 12             LD      (DE),A          
0E7B: 3C             INC     A               
0E7C: 13             INC     DE              
0E7D: 12             LD      (DE),A          
0E7E: 21 00 FC       LD      HL,$FC00        
0E81: 19             ADD     HL,DE           
0E82: EF             RST     0X28            
0E83: 71             LD      (HL),C          
0E84: 2B             DEC     HL              
0E85: 71             LD      (HL),C          
0E86: EB             EX      DE,HL           
0E87: E7             RST     0X20            
0E88: EB             EX      DE,HL           
0E89: 71             LD      (HL),C          
0E8A: 23             INC     HL              
0E8B: 71             LD      (HL),C          
0E8C: C9             RET                     
0E8D: EB             EX      DE,HL           
0E8E: 70             LD      (HL),B          
0E8F: 2B             DEC     HL              
0E90: 36 F1          LD      (HL),$F1        
0E92: CB 94          RES     2,H             
0E94: 71             LD      (HL),C          
0E95: 23             INC     HL              
0E96: 71             LD      (HL),C          
0E97: CB D4          SET     2,H             
0E99: EB             EX      DE,HL           
0E9A: EF             RST     0X28            
0E9B: C9             RET                     
0E9C: EB             EX      DE,HL           
0E9D: 04             INC     B               
0E9E: 70             LD      (HL),B          
0E9F: 05             DEC     B               
0EA0: 2B             DEC     HL              
0EA1: 70             LD      (HL),B          
0EA2: CB 94          RES     2,H             
0EA4: 71             LD      (HL),C          
0EA5: 23             INC     HL              
0EA6: 71             LD      (HL),C          
0EA7: CB D4          SET     2,H             
0EA9: EB             EX      DE,HL           
0EAA: EF             RST     0X28            
0EAB: C9             RET                     
0EAC: 3A 01 AD       LD      A,($AD01)       
0EAF: FE 64          CP      $64             
0EB1: D0             RET     NC              
0EB2: 3E 0E          LD      A,$0E           
0EB4: CD 0F 0C       CALL    $0C0F           
0EB7: EF             RST     0X28            
0EB8: EF             RST     0X28            
0EB9: 21 01 AD       LD      HL,$AD01        
0EBC: 06 01          LD      B,$01           
0EBE: 3A 0C AD       LD      A,($AD0C)       
0EC1: 4F             LD      C,A             
0EC2: C5             PUSH    BC              
0EC3: 0E 00          LD      C,$00           
0EC5: 7E             LD      A,(HL)          
0EC6: D6 0A          SUB     $0A             
0EC8: 38 03          JR      C,$ECD          
0ECA: 0C             INC     C               
0ECB: 18 F9          JR      $EC6            
0ECD: C6 0A          ADD     $0A             
0ECF: 08             EX      AF,AF'          
0ED0: 79             LD      A,C             
0ED1: C1             POP     BC              
0ED2: CD EB 0E       CALL    $0EEB           
0ED5: E7             RST     0X20            
0ED6: 08             EX      AF,AF'          
0ED7: CD EB 0E       CALL    $0EEB           
0EDA: E7             RST     0X20            
0EDB: 11 48 17       LD      DE,$1748        
0EDE: 01 8C 10       LD      BC,$108C        
0EE1: 1A             LD      A,(DE)          
0EE2: 81             ADD     A,C             
0EE3: 4F             LD      C,A             
0EE4: 13             INC     DE              
0EE5: 10 FA          DJNZ    $EE1            
0EE7: C2 09 25       JP      NZ,$2509        
0EEA: C9             RET                     
0EEB: E6 0F          AND     $0F             
0EED: 28 10          JR      Z,$EFF          
0EEF: 06 00          LD      B,$00           
0EF1: E5             PUSH    HL              
0EF2: 21 06 0F       LD      HL,$0F06        
0EF5: CF             RST     0X08            
0EF6: E1             POP     HL              
0EF7: 12             LD      (DE),A          
0EF8: CB 92          RES     2,D             
0EFA: 79             LD      A,C             
0EFB: 12             LD      (DE),A          
0EFC: CB D2          SET     2,D             
0EFE: C9             RET                     
0EFF: 78             LD      A,B             
0F00: A7             AND     A               
0F01: 28 EE          JR      Z,$EF1          
0F03: 05             DEC     B               
0F04: EF             RST     0X28            
0F05: C9             RET                     
0F06: E3             EX      (SP),HL         
0F07: 49             LD      C,C             
0F08: A8             XOR     B               
0F09: 64             LD      H,H             
0F0A: 27             DAA                     
0F0B: AE             XOR     (HL)            
0F0C: 42             LD      B,D             
0F0D: B0             OR      B               
0F0E: D5             PUSH    DE              
0F0F: 86             ADD     A,(HL)          
0F10: F1             POP     AF              
0F11: 21 AB A9       LD      HL,$A9AB        
0F14: 34             INC     (HL)            
0F15: AF             XOR     A               
0F16: 32 AC A9       LD      ($A9AC),A       
0F19: C9             RET                     
0F1A: 21 AC A9       LD      HL,$A9AC        
0F1D: 34             INC     (HL)            
0F1E: C9             RET                     
0F1F: 21 54 0F       LD      HL,$0F54        
0F22: E5             PUSH    HL              
0F23: 3A AC A9       LD      A,($A9AC)       
0F26: E6 0F          AND     $0F             
0F28: F7             RST     0X30            
0F29: B1             OR      C               
0F2A: 27             DAA                     
0F2B: 5E             LD      E,(HL)          
0F2C: 33             INC     SP              
0F2D: D7             RST     0X10            
0F2E: 5B             LD      E,E             
0F2F: 75             LD      (HL),L          
0F30: 4C             LD      C,H             
0F31: 74             LD      (HL),H          
0F32: 07             RLCA                    
0F33: AF             XOR     A               
0F34: 16 94          LD      D,$94           
0F36: 56             LD      D,(HL)          
0F37: 99             SBC     C               
0F38: 11 0B 33       LD      DE,$330B        
0F3B: B4             OR      H               
0F3C: 08             EX      AF,AF'          
0F3D: C3 18 E2       JP      $E218           
0F40: 12             LD      (DE),A          
0F41: FB             EI                      
0F42: 12             LD      (DE),A          
0F43: 0F             RRCA                    
0F44: 4A             LD      C,D             
0F45: 23             INC     HL              
0F46: 13             INC     DE              
0F47: B5             OR      L               
0F48: 15             DEC     D               
0F49: 73             LD      (HL),E          
0F4A: A6             AND     (HL)            
0F4B: 14             INC     D               
0F4C: 7E             LD      A,(HL)          
0F4D: 29             ADD     HL,HL           
0F4E: F8             RET     M               
0F4F: 96             SUB     (HL)            
0F50: 5D             LD      E,L             
0F51: 96             SUB     (HL)            
0F52: 13             INC     DE              
0F53: B9             CP      C               
0F54: 3A 30 AD       LD      A,($AD30)       
0F57: A7             AND     A               
0F58: C0             RET     NZ              
0F59: 3A 86 A9       LD      A,($A986)       
0F5C: A7             AND     A               
0F5D: 20 11          JR      NZ,$F70         
0F5F: 3A C0 A9       LD      A,($A9C0)       
0F62: A7             AND     A               
0F63: C8             RET     Z               
0F64: 3A AE A9       LD      A,($A9AE)       
0F67: E6 18          AND     $18             
0F69: C8             RET     Z               
0F6A: CD B6 15       CALL    $15B6           
0F6D: C3 90 16       JP      $1690           
0F70: AF             XOR     A               
0F71: 32 AC A9       LD      ($A9AC),A       
0F74: 3A 36 17       LD      A,($1736)       
0F77: 32 AB A9       LD      ($A9AB),A       
0F7A: C9             RET                     
0F7B: 87             ADD     A,A             
0F7C: 87             ADD     A,A             
0F7D: 21 6A 18       LD      HL,$186A        
0F80: 11 D3 A9       LD      DE,$A9D3        
0F83: DF             RST     0X18            
0F84: ED A0          LDI                     
0F86: ED A0          LDI                     
0F88: ED A0          LDI                     
0F8A: ED A0          LDI                     
0F8C: C9             RET                     
0F8D: F1             POP     AF              
0F8E: 01 F1 02       LD      BC,$02F1        
0F91: F1             POP     AF              
0F92: 03             INC     BC              
0F93: F1             POP     AF              
0F94: 04             INC     B               
0F95: F1             POP     AF              
0F96: 05             DEC     B               
0F97: 3A 11 B4       LD      A,($B411)       
0F9A: CB 7F          BIT     7,A             
0F9C: 28 19          JR      Z,$FB7          
0F9E: 4F             LD      C,A             
0F9F: 3A 00 C0       LD      A,($C000)       
0FA2: 81             ADD     A,C             
0FA3: 30 12          JR      NC,$FB7         
0FA5: 23             INC     HL              
0FA6: 23             INC     HL              
0FA7: 2B             DEC     HL              
0FA8: 2B             DEC     HL              
0FA9: 79             LD      A,C             
0FAA: E6 7F          AND     $7F             
0FAC: 32 11 B4       LD      ($B411),A       
0FAF: 3A 10 B0       LD      A,($B010)       
0FB2: C6 80          ADD     $80             
0FB4: 32 10 B0       LD      ($B010),A       
0FB7: 3A 13 B4       LD      A,($B413)       
0FBA: CB 7F          BIT     7,A             
0FBC: 28 19          JR      Z,$FD7          
0FBE: 4F             LD      C,A             
0FBF: 3A 00 C0       LD      A,($C000)       
0FC2: 81             ADD     A,C             
0FC3: 30 12          JR      NC,$FD7         
0FC5: 23             INC     HL              
0FC6: 23             INC     HL              
0FC7: 2B             DEC     HL              
0FC8: 2B             DEC     HL              
0FC9: 79             LD      A,C             
0FCA: E6 7F          AND     $7F             
0FCC: 32 13 B4       LD      ($B413),A       
0FCF: 3A 12 B0       LD      A,($B012)       
0FD2: C6 80          ADD     $80             
0FD4: 32 12 B0       LD      ($B012),A       
0FD7: 3A 15 B4       LD      A,($B415)       
0FDA: CB 7F          BIT     7,A             
0FDC: 28 19          JR      Z,$FF7          
0FDE: 4F             LD      C,A             
0FDF: 3A 00 C0       LD      A,($C000)       
0FE2: 81             ADD     A,C             
0FE3: 30 12          JR      NC,$FF7         
0FE5: 23             INC     HL              
0FE6: 23             INC     HL              
0FE7: 2B             DEC     HL              
0FE8: 2B             DEC     HL              
0FE9: 79             LD      A,C             
0FEA: E6 7F          AND     $7F             
0FEC: 32 15 B4       LD      ($B415),A       
0FEF: 3A 14 B0       LD      A,($B014)       
0FF2: C6 80          ADD     $80             
0FF4: 32 14 B0       LD      ($B014),A       
0FF7: 3A 37 B4       LD      A,($B437)       
0FFA: CB 7F          BIT     7,A             
0FFC: 28 19          JR      Z,$1017         
0FFE: 4F             LD      C,A             
0FFF: 3A 00 C0       LD      A,($C000)       
1002: 81             ADD     A,C             
1003: 30 12          JR      NC,$1017        
1005: 23             INC     HL              
1006: 23             INC     HL              
1007: 2B             DEC     HL              
1008: 2B             DEC     HL              
1009: 79             LD      A,C             
100A: E6 7F          AND     $7F             
100C: 32 37 B4       LD      ($B437),A       
100F: 3A 36 B0       LD      A,($B036)       
1012: C6 80          ADD     $80             
1014: 32 36 B0       LD      ($B036),A       
1017: 3A 39 B4       LD      A,($B439)       
101A: CB 7F          BIT     7,A             
101C: 28 19          JR      Z,$1037         
101E: 4F             LD      C,A             
101F: 3A 00 C0       LD      A,($C000)       
1022: 81             ADD     A,C             
1023: 30 12          JR      NC,$1037        
1025: 23             INC     HL              
1026: 23             INC     HL              
1027: 2B             DEC     HL              
1028: 2B             DEC     HL              
1029: 79             LD      A,C             
102A: E6 7F          AND     $7F             
102C: 32 39 B4       LD      ($B439),A       
102F: 3A 38 B0       LD      A,($B038)       
1032: C6 80          ADD     $80             
1034: 32 38 B0       LD      ($B038),A       
1037: 3A 3B B4       LD      A,($B43B)       
103A: CB 7F          BIT     7,A             
103C: 28 19          JR      Z,$1057         
103E: 4F             LD      C,A             
103F: 3A 00 C0       LD      A,($C000)       
1042: 81             ADD     A,C             
1043: 30 12          JR      NC,$1057        
1045: 23             INC     HL              
1046: 23             INC     HL              
1047: 2B             DEC     HL              
1048: 2B             DEC     HL              
1049: 79             LD      A,C             
104A: E6 7F          AND     $7F             
104C: 32 3B B4       LD      ($B43B),A       
104F: 3A 3A B0       LD      A,($B03A)       
1052: C6 80          ADD     $80             
1054: 32 3A B0       LD      ($B03A),A       
1057: 3A 3D B4       LD      A,($B43D)       
105A: CB 7F          BIT     7,A             
105C: 28 19          JR      Z,$1077         
105E: 4F             LD      C,A             
105F: 3A 00 C0       LD      A,($C000)       
1062: 81             ADD     A,C             
1063: 30 12          JR      NC,$1077        
1065: 23             INC     HL              
1066: 23             INC     HL              
1067: 2B             DEC     HL              
1068: 2B             DEC     HL              
1069: 79             LD      A,C             
106A: E6 7F          AND     $7F             
106C: 32 3D B4       LD      ($B43D),A       
106F: 3A 3C B0       LD      A,($B03C)       
1072: C6 80          ADD     $80             
1074: 32 3C B0       LD      ($B03C),A       
1077: 3A 3F B4       LD      A,($B43F)       
107A: CB 7F          BIT     7,A             
107C: 28 19          JR      Z,$1097         
107E: 4F             LD      C,A             
107F: 3A 00 C0       LD      A,($C000)       
1082: 81             ADD     A,C             
1083: 30 12          JR      NC,$1097        
1085: 23             INC     HL              
1086: 23             INC     HL              
1087: 2B             DEC     HL              
1088: 2B             DEC     HL              
1089: 79             LD      A,C             
108A: E6 7F          AND     $7F             
108C: 32 3F B4       LD      ($B43F),A       
108F: 3A 3E B0       LD      A,($B03E)       
1092: C6 80          ADD     $80             
1094: 32 3E B0       LD      ($B03E),A       
1097: C9             RET                     
1098: 3A 11 B4       LD      A,($B411)       
109B: CB 7F          BIT     7,A             
109D: 28 19          JR      Z,$10B8         
109F: 4F             LD      C,A             
10A0: 3A 00 C0       LD      A,($C000)       
10A3: 81             ADD     A,C             
10A4: 30 F2          JR      NC,$1098        
10A6: 23             INC     HL              
10A7: 23             INC     HL              
10A8: 2B             DEC     HL              
10A9: 2B             DEC     HL              
10AA: 79             LD      A,C             
10AB: E6 7F          AND     $7F             
10AD: 32 11 B4       LD      ($B411),A       
10B0: 3A 10 B0       LD      A,($B010)       
10B3: C6 80          ADD     $80             
10B5: 32 10 B0       LD      ($B010),A       
10B8: 3A 13 B4       LD      A,($B413)       
10BB: CB 7F          BIT     7,A             
10BD: 28 19          JR      Z,$10D8         
10BF: 4F             LD      C,A             
10C0: 3A 00 C0       LD      A,($C000)       
10C3: 81             ADD     A,C             
10C4: 30 F2          JR      NC,$10B8        
10C6: 23             INC     HL              
10C7: 23             INC     HL              
10C8: 2B             DEC     HL              
10C9: 2B             DEC     HL              
10CA: 79             LD      A,C             
10CB: E6 7F          AND     $7F             
10CD: 32 13 B4       LD      ($B413),A       
10D0: 3A 12 B0       LD      A,($B012)       
10D3: C6 80          ADD     $80             
10D5: 32 12 B0       LD      ($B012),A       
10D8: 3A 15 B4       LD      A,($B415)       
10DB: CB 7F          BIT     7,A             
10DD: 28 19          JR      Z,$10F8         
10DF: 4F             LD      C,A             
10E0: 3A 00 C0       LD      A,($C000)       
10E3: 81             ADD     A,C             
10E4: 30 F2          JR      NC,$10D8        
10E6: 23             INC     HL              
10E7: 23             INC     HL              
10E8: 2B             DEC     HL              
10E9: 2B             DEC     HL              
10EA: 79             LD      A,C             
10EB: E6 7F          AND     $7F             
10ED: 32 15 B4       LD      ($B415),A       
10F0: 3A 14 B0       LD      A,($B014)       
10F3: C6 80          ADD     $80             
10F5: 32 14 B0       LD      ($B014),A       
10F8: 3A 37 B4       LD      A,($B437)       
10FB: CB 7F          BIT     7,A             
10FD: 28 19          JR      Z,$1118         
10FF: 4F             LD      C,A             
1100: 3A 00 C0       LD      A,($C000)       
1103: 81             ADD     A,C             
1104: 30 F2          JR      NC,$10F8        
1106: 23             INC     HL              
1107: 23             INC     HL              
1108: 2B             DEC     HL              
1109: 2B             DEC     HL              
110A: 79             LD      A,C             
110B: E6 7F          AND     $7F             
110D: 32 37 B4       LD      ($B437),A       
1110: 3A 36 B0       LD      A,($B036)       
1113: C6 80          ADD     $80             
1115: 32 36 B0       LD      ($B036),A       
1118: 3A 39 B4       LD      A,($B439)       
111B: CB 7F          BIT     7,A             
111D: 28 19          JR      Z,$1138         
111F: 4F             LD      C,A             
1120: 3A 00 C0       LD      A,($C000)       
1123: 81             ADD     A,C             
1124: 30 F2          JR      NC,$1118        
1126: 23             INC     HL              
1127: 23             INC     HL              
1128: 2B             DEC     HL              
1129: 2B             DEC     HL              
112A: 79             LD      A,C             
112B: E6 7F          AND     $7F             
112D: 32 39 B4       LD      ($B439),A       
1130: 3A 38 B0       LD      A,($B038)       
1133: C6 80          ADD     $80             
1135: 32 38 B0       LD      ($B038),A       
1138: 3A 3B B4       LD      A,($B43B)       
113B: CB 7F          BIT     7,A             
113D: 28 19          JR      Z,$1158         
113F: 4F             LD      C,A             
1140: 3A 00 C0       LD      A,($C000)       
1143: 81             ADD     A,C             
1144: 30 F2          JR      NC,$1138        
1146: 23             INC     HL              
1147: 23             INC     HL              
1148: 2B             DEC     HL              
1149: 2B             DEC     HL              
114A: 79             LD      A,C             
114B: E6 7F          AND     $7F             
114D: 32 3B B4       LD      ($B43B),A       
1150: 3A 3A B0       LD      A,($B03A)       
1153: C6 80          ADD     $80             
1155: 32 3A B0       LD      ($B03A),A       
1158: 3A 3D B4       LD      A,($B43D)       
115B: CB 7F          BIT     7,A             
115D: 28 19          JR      Z,$1178         
115F: 4F             LD      C,A             
1160: 3A 00 C0       LD      A,($C000)       
1163: 81             ADD     A,C             
1164: 30 F2          JR      NC,$1158        
1166: 23             INC     HL              
1167: 23             INC     HL              
1168: 2B             DEC     HL              
1169: 2B             DEC     HL              
116A: 79             LD      A,C             
116B: E6 7F          AND     $7F             
116D: 32 3D B4       LD      ($B43D),A       
1170: 3A 3C B0       LD      A,($B03C)       
1173: C6 80          ADD     $80             
1175: 32 3C B0       LD      ($B03C),A       
1178: 3A 3F B4       LD      A,($B43F)       
117B: CB 7F          BIT     7,A             
117D: 28 19          JR      Z,$1198         
117F: 4F             LD      C,A             
1180: 3A 00 C0       LD      A,($C000)       
1183: 81             ADD     A,C             
1184: 30 F2          JR      NC,$1178        
1186: 23             INC     HL              
1187: 23             INC     HL              
1188: 2B             DEC     HL              
1189: 2B             DEC     HL              
118A: 79             LD      A,C             
118B: E6 7F          AND     $7F             
118D: 32 3F B4       LD      ($B43F),A       
1190: 3A 3E B0       LD      A,($B03E)       
1193: C6 80          ADD     $80             
1195: 32 3E B0       LD      ($B03E),A       
1198: C9             RET                     
1199: CD B4 31       CALL    $31B4           
119C: CD DF 1E       CALL    $1EDF           
119F: CD E3 23       CALL    $23E3           
11A2: CD AF 36       CALL    $36AF           
11A5: CD 97 0F       CALL    $0F97           
11A8: CD B3 47       CALL    $47B3           
11AB: CD B7 43       CALL    $43B7           
11AE: CD A1 28       CALL    $28A1           
11B1: CD 97 0F       CALL    $0F97           
11B4: CD BC 2C       CALL    $2CBC           
11B7: CD D6 40       CALL    $40D6           
11BA: CD 97 0F       CALL    $0F97           
11BD: CD 5F 3B       CALL    $3B5F           
11C0: CD DA 3D       CALL    $3DDA           
11C3: CD 36 3E       CALL    $3E36           
11C6: CD 97 0F       CALL    $0F97           
11C9: CD EA 3F       CALL    $3FEA           
11CC: CD 4F 4E       CALL    $4E4F           
11CF: CD B8 40       CALL    $40B8           
11D2: CD 97 0F       CALL    $0F97           
11D5: CD DE 4D       CALL    $4DDE           
11D8: CD 05 52       CALL    $5205           
11DB: CD 3A 4D       CALL    $4D3A           
11DE: CD 09 08       CALL    $0809           
11E1: CD 98 10       CALL    $1098           
11E4: 3A 00 A8       LD      A,($A800)       
11E7: 3C             INC     A               
11E8: CA 71 12       JP      Z,$1271         
11EB: 3D             DEC     A               
11EC: C0             RET     NZ              
11ED: CD B6 15       CALL    $15B6           
11F0: 3A C6 AC       LD      A,($ACC6)       
11F3: A7             AND     A               
11F4: C4 B8 2D       CALL    NZ,$2DB8        
11F7: CD 34 56       CALL    $5634           
11FA: 21 00 AD       LD      HL,$AD00        
11FD: 35             DEC     (HL)            
11FE: F5             PUSH    AF              
11FF: 3A 32 AD       LD      A,($AD32)       
1202: A7             AND     A               
1203: 11 10 AD       LD      DE,$AD10        
1206: 28 03          JR      Z,$120B         
1208: 11 20 AD       LD      DE,$AD20        
120B: 21 00 AD       LD      HL,$AD00        
120E: 01 10 00       LD      BC,$0010        
1211: ED B0          LDIR                    
1213: F1             POP     AF              
1214: 28 3D          JR      Z,$1253         
1216: 3A 32 AD       LD      A,($AD32)       
1219: A7             AND     A               
121A: 21 20 AD       LD      HL,$AD20        
121D: 28 03          JR      Z,$1222         
121F: 21 10 AD       LD      HL,$AD10        
1222: 7E             LD      A,(HL)          
1223: A7             AND     A               
1224: 28 09          JR      Z,$122F         
1226: 3A 32 AD       LD      A,($AD32)       
1229: 3C             INC     A               
122A: E6 01          AND     $01             
122C: 32 32 AD       LD      ($AD32),A       
122F: 3E 5A          LD      A,$5A           
1231: 32 EB A9       LD      ($A9EB),A       
1234: 3A 52 4B       LD      A,($4B52)       
1237: 32 AC A9       LD      ($A9AC),A       
123A: C9             RET                     
123B: 18 A7          JR      $11E4           
123D: 13             INC     DE              
123E: A5             AND     L               
123F: 3B             DEC     SP              
1240: 87             ADD     A,A             
1241: F1             POP     AF              
1242: 34             INC     (HL)            
1243: 0E 34          LD      C,$34           
1245: D7             RST     0X10            
1246: BF             CP      A               
1247: F1             POP     AF              
1248: 7F             LD      A,A             
1249: 13             INC     DE              
124A: 13             INC     DE              
124B: 13             INC     DE              
124C: 13             INC     DE              
124D: F1             POP     AF              
124E: 88             ADC     A,B             
124F: DC ED 11       CALL    C,$11ED         
1252: B9             CP      C               
1253: 3A 30 AD       LD      A,($AD30)       
1256: A7             AND     A               
1257: CA FB 12       JP      Z,$12FB         
125A: 11 09 02       LD      DE,$0209        
125D: 3A 32 AD       LD      A,($AD32)       
1260: A7             AND     A               
1261: 28 01          JR      Z,$1264         
1263: 1C             INC     E               
1264: FF             RST     0X38            
1265: 11 0B 0A       LD      DE,$0A0B        
1268: FF             RST     0X38            
1269: 3E B4          LD      A,$B4           
126B: 32 EB A9       LD      ($A9EB),A       
126E: C3 1A 0F       JP      $0F1A           
1271: 3A 02 AD       LD      A,($AD02)       
1274: A7             AND     A               
1275: C0             RET     NZ              
1276: 3A C6 AC       LD      A,($ACC6)       
1279: A7             AND     A               
127A: C8             RET     Z               
127B: 21 10 A8       LD      HL,$A810        
127E: 11 10 00       LD      DE,$0010        
1281: 06 0F          LD      B,$0F           
1283: 7E             LD      A,(HL)          
1284: A7             AND     A               
1285: C0             RET     NZ              
1286: 19             ADD     HL,DE           
1287: 10 FA          DJNZ    $1283           
1289: CD 34 56       CALL    $5634           
128C: 3A 30 AD       LD      A,($AD30)       
128F: A7             AND     A               
1290: 28 29          JR      Z,$12BB         
1292: 21 43 AA       LD      HL,$AA43        
1295: 06 17          LD      B,$17           
1297: AF             XOR     A               
1298: 77             LD      (HL),A          
1299: 2C             INC     L               
129A: 2C             INC     L               
129B: 10 FB          DJNZ    $1298           
129D: CD B8 2D       CALL    $2DB8           
12A0: 3A 32 AD       LD      A,($AD32)       
12A3: A7             AND     A               
12A4: 11 10 AD       LD      DE,$AD10        
12A7: 28 03          JR      Z,$12AC         
12A9: 11 20 AD       LD      DE,$AD20        
12AC: 21 00 AD       LD      HL,$AD00        
12AF: 01 10 00       LD      BC,$0010        
12B2: ED B0          LDIR                    
12B4: 3A 35 4A       LD      A,($4A35)       
12B7: 32 AC A9       LD      ($A9AC),A       
12BA: C9             RET                     
12BB: 3A D1 07       LD      A,($07D1)       
12BE: 32 C6 AC       LD      ($ACC6),A       
12C1: CD B6 15       CALL    $15B6           
12C4: C3 FB 12       JP      $12FB           
12C7: 74             LD      (HL),H          
12C8: B1             OR      C               
12C9: CC EC 5C       CALL    Z,$5CEC         
12CC: 16 39          LD      D,$39           
12CE: 50             LD      D,B             
12CF: 67             LD      H,A             
12D0: 21 7A C5       LD      HL,$C57A        
12D3: F7             RST     0X30            
12D4: BE             CP      (HL)            
12D5: 54             LD      D,H             
12D6: 80             ADD     A,B             
12D7: 2F             CPL                     
12D8: 5F             LD      E,A             
12D9: 9F             SBC     A               
12DA: 6D             LD      L,L             
12DB: 44             LD      B,H             
12DC: B8             CP      B               
12DD: E7             RST     0X20            
12DE: BD             CP      L               
12DF: 89             ADC     A,C             
12E0: 59             LD      E,C             
12E1: 1A             LD      A,(DE)          
12E2: 21 EB A9       LD      HL,$A9EB        
12E5: 35             DEC     (HL)            
12E6: C0             RET     NZ              
12E7: 3A 32 AD       LD      A,($AD32)       
12EA: A7             AND     A               
12EB: 21 20 AD       LD      HL,$AD20        
12EE: 28 03          JR      Z,$12F3         
12F0: 21 10 AD       LD      HL,$AD10        
12F3: 7E             LD      A,(HL)          
12F4: A7             AND     A               
12F5: C2 26 12       JP      NZ,$1226        
12F8: C3 1A 0F       JP      $0F1A           
12FB: AF             XOR     A               
12FC: 32 30 AD       LD      ($AD30),A       
12FF: 32 AC A9       LD      ($A9AC),A       
1302: 32 32 AD       LD      ($AD32),A       
1305: 3A D3 16       LD      A,($16D3)       
1308: 32 AB A9       LD      ($A9AB),A       
130B: 3A 01 49       LD      A,($4901)       
130E: 2A 02 49       LD      HL,($4902)      
1311: DF             RST     0X18            
1312: AC             XOR     H               
1313: D6 9B          SUB     $9B             
1315: 32 AC A9       LD      ($A9AC),A       
1318: C9             RET                     
1319: 11 E0 FF       LD      DE,$FFE0        
131C: 06 0D          LD      B,$0D           
131E: 77             LD      (HL),A          
131F: 19             ADD     HL,DE           
1320: 10 FC          DJNZ    $131E           
1322: C9             RET                     
1323: 3A 80 A9       LD      A,($A980)       
1326: E6 02          AND     $02             
1328: C0             RET     NZ              
1329: 3A F0 A9       LD      A,($A9F0)       
132C: A7             AND     A               
132D: 20 04          JR      NZ,$1333        
132F: CD 67 13       CALL    $1367           
1332: C9             RET                     
1333: 3D             DEC     A               
1334: 20 07          JR      NZ,$133D        
1336: CD 67 13       CALL    $1367           
1339: CD 2A 14       CALL    $142A           
133C: C9             RET                     
133D: 3D             DEC     A               
133E: 20 07          JR      NZ,$1347        
1340: CD 93 13       CALL    $1393           
1343: CD C5 14       CALL    $14C5           
1346: C9             RET                     
1347: 3D             DEC     A               
1348: 20 04          JR      NZ,$134E        
134A: CD C5 14       CALL    $14C5           
134D: C9             RET                     
134E: 3D             DEC     A               
134F: 20 04          JR      NZ,$1355        
1351: CD CC 13       CALL    $13CC           
1354: C9             RET                     
1355: 3E 5A          LD      A,$5A           
1357: 32 EB A9       LD      ($A9EB),A       
135A: CD B6 15       CALL    $15B6           
135D: CD 75 4C       CALL    $4C75           
1360: 3A 50 27       LD      A,($2750)       
1363: 32 AC A9       LD      ($A9AC),A       
1366: C9             RET                     
1367: 3A F1 A9       LD      A,($A9F1)       
136A: FE 08          CP      $08             
136C: 20 08          JR      NZ,$1376        
136E: 3E 01          LD      A,$01           
1370: 32 F0 A9       LD      ($A9F0),A       
1373: CD 11 58       CALL    $5811           
1376: 3A F1 A9       LD      A,($A9F1)       
1379: E6 01          AND     $01             
137B: 3E 3E          LD      A,$3E           
137D: 28 02          JR      Z,$1381         
137F: 3E 00          LD      A,$00           
1381: 47             LD      B,A             
1382: 3A 40 AA       LD      A,($AA40)       
1385: E6 C0          AND     $C0             
1387: 80             ADD     A,B             
1388: 32 40 AA       LD      ($AA40),A       
138B: 3A F1 A9       LD      A,($A9F1)       
138E: 3C             INC     A               
138F: 32 F1 A9       LD      ($A9F1),A       
1392: C9             RET                     
1393: 3A F3 A9       LD      A,($A9F3)       
1396: A7             AND     A               
1397: 20 09          JR      NZ,$13A2        
1399: 3E 03          LD      A,$03           
139B: 32 F0 A9       LD      ($A9F0),A       
139E: 3E 3F          LD      A,$3F           
13A0: 18 18          JR      $13BA           
13A2: E6 04          AND     $04             
13A4: 20 04          JR      NZ,$13AA        
13A6: 3E 3F          LD      A,$3F           
13A8: 18 10          JR      $13BA           
13AA: 3D             DEC     A               
13AB: 20 04          JR      NZ,$13B1        
13AD: 3E 36          LD      A,$36           
13AF: 18 09          JR      $13BA           
13B1: 3D             DEC     A               
13B2: 20 04          JR      NZ,$13B8        
13B4: 3E 3E          LD      A,$3E           
13B6: 18 02          JR      $13BA           
13B8: 3E 37          LD      A,$37           
13BA: 47             LD      B,A             
13BB: 3A 40 AA       LD      A,($AA40)       
13BE: E6 C0          AND     $C0             
13C0: 80             ADD     A,B             
13C1: 32 40 AA       LD      ($AA40),A       
13C4: 3A F3 A9       LD      A,($A9F3)       
13C7: 3D             DEC     A               
13C8: 32 F3 A9       LD      ($A9F3),A       
13CB: C9             RET                     
13CC: 3E 05          LD      A,$05           
13CE: 32 F0 A9       LD      ($A9F0),A       
13D1: 3A 32 AD       LD      A,($AD32)       
13D4: A7             AND     A               
13D5: 3A 1C AD       LD      A,($AD1C)       
13D8: 47             LD      B,A             
13D9: 28 04          JR      Z,$13DF         
13DB: 3A 2C AD       LD      A,($AD2C)       
13DE: 47             LD      B,A             
13DF: 3A 87 A9       LD      A,($A987)       
13E2: A7             AND     A               
13E3: 78             LD      A,B             
13E4: 28 22          JR      Z,$1408         
13E6: 21 44 A0       LD      HL,$A044        
13E9: 11 45 A0       LD      DE,$A045        
13EC: D9             EXX                     
13ED: 06 1C          LD      B,$1C           
13EF: D9             EXX                     
13F0: 01 1A 00       LD      BC,$001A        
13F3: 77             LD      (HL),A          
13F4: ED B0          LDIR                    
13F6: 11 06 00       LD      DE,$0006        
13F9: 19             ADD     HL,DE           
13FA: 54             LD      D,H             
13FB: 5D             LD      E,L             
13FC: 13             INC     DE              
13FD: D9             EXX                     
13FE: 10 EF          DJNZ    $13EF           
1400: 3A F6 A9       LD      A,($A9F6)       
1403: 3D             DEC     A               
1404: 32 F6 A9       LD      ($A9F6),A       
1407: C9             RET                     
1408: 21 BE A3       LD      HL,$A3BE        
140B: 11 BD A3       LD      DE,$A3BD        
140E: D9             EXX                     
140F: 06 1C          LD      B,$1C           
1411: D9             EXX                     
1412: 01 1A 00       LD      BC,$001A        
1415: 77             LD      (HL),A          
1416: ED B8          LDDR                    
1418: 11 FA FF       LD      DE,$FFFA        
141B: 19             ADD     HL,DE           
141C: 54             LD      D,H             
141D: 5D             LD      E,L             
141E: 1B             DEC     DE              
141F: D9             EXX                     
1420: 10 EF          DJNZ    $1411           
1422: 3A F6 A9       LD      A,($A9F6)       
1425: 3D             DEC     A               
1426: 32 F6 A9       LD      ($A9F6),A       
1429: C9             RET                     
142A: 3A F2 A9       LD      A,($A9F2)       
142D: CB 47          BIT     0,A             
142F: 28 6C          JR      Z,$149D         
1431: 2A F7 A9       LD      HL,($A9F7)      
1434: 7E             LD      A,(HL)          
1435: FE FF          CP      $FF             
1437: 20 12          JR      NZ,$144B        
1439: 3E 00          LD      A,$00           
143B: 32 F2 A9       LD      ($A9F2),A       
143E: 3E 02          LD      A,$02           
1440: 32 F0 A9       LD      ($A9F0),A       
1443: 2A F7 A9       LD      HL,($A9F7)      
1446: 2B             DEC     HL              
1447: 22 F7 A9       LD      ($A9F7),HL      
144A: C9             RET                     
144B: CD 63 15       CALL    $1563           
144E: 2A F7 A9       LD      HL,($A9F7)      
1451: 7E             LD      A,(HL)          
1452: E6 01          AND     $01             
1454: 23             INC     HL              
1455: 22 F7 A9       LD      ($A9F7),HL      
1458: 28 0F          JR      Z,$1469         
145A: 11 20 00       LD      DE,$0020        
145D: 21 F0 A5       LD      HL,$A5F0        
1460: 34             INC     (HL)            
1461: 19             ADD     HL,DE           
1462: 34             INC     (HL)            
1463: 21 F2 A5       LD      HL,$A5F2        
1466: 34             INC     (HL)            
1467: 19             ADD     HL,DE           
1468: 34             INC     (HL)            
1469: 2A F7 A9       LD      HL,($A9F7)      
146C: 7E             LD      A,(HL)          
146D: E6 01          AND     $01             
146F: 23             INC     HL              
1470: 22 F7 A9       LD      ($A9F7),HL      
1473: 28 09          JR      Z,$147E         
1475: 11 20 00       LD      DE,$0020        
1478: 21 F1 A5       LD      HL,$A5F1        
147B: 34             INC     (HL)            
147C: 19             ADD     HL,DE           
147D: 34             INC     (HL)            
147E: 0E 02          LD      C,$02           
1480: 11 D1 A5       LD      DE,$A5D1        
1483: CD 9D 4A       CALL    $4A9D           
1486: 2A F7 A9       LD      HL,($A9F7)      
1489: 11 F3 FF       LD      DE,$FFF3        
148C: 19             ADD     HL,DE           
148D: 22 F7 A9       LD      ($A9F7),HL      
1490: 0E 00          LD      C,$00           
1492: 11 31 A6       LD      DE,$A631        
1495: CD 9D 4A       CALL    $4A9D           
1498: CD 8C 15       CALL    $158C           
149B: 18 20          JR      $14BD           
149D: 3E F1          LD      A,$F1           
149F: 21 B1 A7       LD      HL,$A7B1        
14A2: CD 19 13       CALL    $1319           
14A5: 21 D1 A5       LD      HL,$A5D1        
14A8: CD 19 13       CALL    $1319           
14AB: 21 10 A6       LD      HL,$A610        
14AE: 77             LD      (HL),A          
14AF: 19             ADD     HL,DE           
14B0: 77             LD      (HL),A          
14B1: 21 11 A6       LD      HL,$A611        
14B4: 77             LD      (HL),A          
14B5: 19             ADD     HL,DE           
14B6: 77             LD      (HL),A          
14B7: 21 12 A6       LD      HL,$A612        
14BA: 77             LD      (HL),A          
14BB: 19             ADD     HL,DE           
14BC: 77             LD      (HL),A          
14BD: 3A F2 A9       LD      A,($A9F2)       
14C0: 3D             DEC     A               
14C1: 32 F2 A9       LD      ($A9F2),A       
14C4: C9             RET                     
14C5: 3A F4 A9       LD      A,($A9F4)       
14C8: CB 47          BIT     0,A             
14CA: 28 6F          JR      Z,$153B         
14CC: 2A F7 A9       LD      HL,($A9F7)      
14CF: 7E             LD      A,(HL)          
14D0: E6 FE          AND     $FE             
14D2: 28 15          JR      Z,$14E9         
14D4: 3E 00          LD      A,$00           
14D6: 32 F4 A9       LD      ($A9F4),A       
14D9: 3E 04          LD      A,$04           
14DB: 32 F0 A9       LD      ($A9F0),A       
14DE: CD E4 56       CALL    $56E4           
14E1: 2A F7 A9       LD      HL,($A9F7)      
14E4: 23             INC     HL              
14E5: 22 F7 A9       LD      ($A9F7),HL      
14E8: C9             RET                     
14E9: CD 63 15       CALL    $1563           
14EC: 0E 01          LD      C,$01           
14EE: 11 51 A4       LD      DE,$A451        
14F1: CD 9D 4A       CALL    $4A9D           
14F4: 2A F7 A9       LD      HL,($A9F7)      
14F7: 11 0D 00       LD      DE,$000D        
14FA: 19             ADD     HL,DE           
14FB: 22 F7 A9       LD      ($A9F7),HL      
14FE: 0E 03          LD      C,$03           
1500: 11 B1 A7       LD      DE,$A7B1        
1503: CD 9D 4A       CALL    $4A9D           
1506: 2A F7 A9       LD      HL,($A9F7)      
1509: 7E             LD      A,(HL)          
150A: E6 01          AND     $01             
150C: 2B             DEC     HL              
150D: 22 F7 A9       LD      ($A9F7),HL      
1510: 28 09          JR      Z,$151B         
1512: 11 20 00       LD      DE,$0020        
1515: 21 F1 A5       LD      HL,$A5F1        
1518: 35             DEC     (HL)            
1519: 19             ADD     HL,DE           
151A: 35             DEC     (HL)            
151B: 2A F7 A9       LD      HL,($A9F7)      
151E: 7E             LD      A,(HL)          
151F: E6 01          AND     $01             
1521: 2B             DEC     HL              
1522: 22 F7 A9       LD      ($A9F7),HL      
1525: 28 0F          JR      Z,$1536         
1527: 11 20 00       LD      DE,$0020        
152A: 21 F0 A5       LD      HL,$A5F0        
152D: 35             DEC     (HL)            
152E: 19             ADD     HL,DE           
152F: 35             DEC     (HL)            
1530: 21 F2 A5       LD      HL,$A5F2        
1533: 35             DEC     (HL)            
1534: 19             ADD     HL,DE           
1535: 35             DEC     (HL)            
1536: CD 8C 15       CALL    $158C           
1539: 18 20          JR      $155B           
153B: 3E F1          LD      A,$F1           
153D: 21 B1 A7       LD      HL,$A7B1        
1540: CD 19 13       CALL    $1319           
1543: 21 D1 A5       LD      HL,$A5D1        
1546: CD 19 13       CALL    $1319           
1549: 21 10 A6       LD      HL,$A610        
154C: 77             LD      (HL),A          
154D: 19             ADD     HL,DE           
154E: 77             LD      (HL),A          
154F: 21 11 A6       LD      HL,$A611        
1552: 77             LD      (HL),A          
1553: 19             ADD     HL,DE           
1554: 77             LD      (HL),A          
1555: 21 12 A6       LD      HL,$A612        
1558: 77             LD      (HL),A          
1559: 19             ADD     HL,DE           
155A: 77             LD      (HL),A          
155B: 3A F4 A9       LD      A,($A9F4)       
155E: 3D             DEC     A               
155F: 32 F4 A9       LD      ($A9F4),A       
1562: C9             RET                     
1563: 11 00 A4       LD      DE,$A400        
1566: 21 51 A4       LD      HL,$A451        
1569: 01 20 00       LD      BC,$0020        
156C: D9             EXX                     
156D: 06 1C          LD      B,$1C           
156F: D9             EXX                     
1570: 1A             LD      A,(DE)          
1571: 77             LD      (HL),A          
1572: 13             INC     DE              
1573: 09             ADD     HL,BC           
1574: D9             EXX                     
1575: 10 F8          DJNZ    $156F           
1577: D9             EXX                     
1578: 21 F0 A5       LD      HL,$A5F0        
157B: 1A             LD      A,(DE)          
157C: 77             LD      (HL),A          
157D: 09             ADD     HL,BC           
157E: 13             INC     DE              
157F: 1A             LD      A,(DE)          
1580: 77             LD      (HL),A          
1581: 13             INC     DE              
1582: 21 F2 A5       LD      HL,$A5F2        
1585: 1A             LD      A,(DE)          
1586: 77             LD      (HL),A          
1587: 09             ADD     HL,BC           
1588: 13             INC     DE              
1589: 1A             LD      A,(DE)          
158A: 77             LD      (HL),A          
158B: C9             RET                     
158C: 11 00 A4       LD      DE,$A400        
158F: 21 51 A4       LD      HL,$A451        
1592: 01 20 00       LD      BC,$0020        
1595: D9             EXX                     
1596: 06 1C          LD      B,$1C           
1598: D9             EXX                     
1599: 7E             LD      A,(HL)          
159A: 12             LD      (DE),A          
159B: 13             INC     DE              
159C: 09             ADD     HL,BC           
159D: D9             EXX                     
159E: 10 F8          DJNZ    $1598           
15A0: D9             EXX                     
15A1: 21 F0 A5       LD      HL,$A5F0        
15A4: 7E             LD      A,(HL)          
15A5: 12             LD      (DE),A          
15A6: 09             ADD     HL,BC           
15A7: 13             INC     DE              
15A8: 7E             LD      A,(HL)          
15A9: 12             LD      (DE),A          
15AA: 13             INC     DE              
15AB: 21 F2 A5       LD      HL,$A5F2        
15AE: 7E             LD      A,(HL)          
15AF: 12             LD      (DE),A          
15B0: 09             ADD     HL,BC           
15B1: 13             INC     DE              
15B2: 7E             LD      A,(HL)          
15B3: 12             LD      (DE),A          
15B4: C9             RET                     
15B5: C9             RET                     
15B6: 21 41 AA       LD      HL,$AA41        
15B9: 06 18          LD      B,$18           
15BB: AF             XOR     A               
15BC: 77             LD      (HL),A          
15BD: 2C             INC     L               
15BE: 2C             INC     L               
15BF: 10 FB          DJNZ    $15BC           
15C1: C9             RET                     
15C2: 3A AC A9       LD      A,($A9AC)       
15C5: E6 07          AND     $07             
15C7: F7             RST     0X30            
15C8: E2 15 5F       JP      PO,$5F15        
15CB: A5             AND     L               
15CC: 13             INC     DE              
15CD: 77             LD      (HL),A          
15CE: D7             RST     0X10            
15CF: 34             INC     (HL)            
15D0: 87             ADD     A,A             
15D1: FD DC B9 FE    CALL    C,$FEB9         
15D5: 15             DEC     D               
15D6: 60             LD      H,B             
15D7: A6             AND     (HL)            
15D8: 14             INC     D               
15D9: C4 FD 10       CALL    NZ,$10FD        
15DC: ED                                  
15DD: 77             LD      (HL),A          
15DE: 68             LD      L,B             
15DF: D7             RST     0X10            
15E0: 34             INC     (HL)            
15E1: B9             CP      C               
15E2: CD 9A 01       CALL    $019A           
15E5: 3A 49 17       LD      A,($1749)       
15E8: 32 AC A9       LD      ($A9AC),A       
15EB: 0E 00          LD      C,$00           
15ED: 21 48 56       LD      HL,$5648        
15F0: 3A AB A9       LD      A,($A9AB)       
15F3: 96             SUB     (HL)            
15F4: 23             INC     HL              
15F5: 0D             DEC     C               
15F6: 20 FB          JR      NZ,$15F3        
15F8: EE 4E          XOR     $4E             
15FA: 32 AB A9       LD      ($A9AB),A       
15FD: C9             RET                     
15FE: CD C2 01       CALL    $01C2           
1601: C0             RET     NZ              
1602: 11 05 01       LD      DE,$0105        
1605: FF             RST     0X38            
1606: 1C             INC     E               
1607: FF             RST     0X38            
1608: 1C             INC     E               
1609: FF             RST     0X38            
160A: 11 01 06       LD      DE,$0601        
160D: FF             RST     0X38            
160E: 3E 13          LD      A,$13           
1610: 32 01 A7       LD      ($A701),A       
1613: 32 E1 A6       LD      ($A6E1),A       
1616: 21 3F 16       LD      HL,$163F        
1619: 06 06          LD      B,$06           
161B: 5E             LD      E,(HL)          
161C: 23             INC     HL              
161D: 56             LD      D,(HL)          
161E: 23             INC     HL              
161F: 7E             LD      A,(HL)          
1620: 12             LD      (DE),A          
1621: 13             INC     DE              
1622: EB             EX      DE,HL           
1623: 36 05          LD      (HL),$05        
1625: EB             EX      DE,HL           
1626: 23             INC     HL              
1627: 10 F2          DJNZ    $161B           
1629: CD 6B 0D       CALL    $0D6B           
162C: 3E 01          LD      A,$01           
162E: 32 AB A9       LD      ($A9AB),A       
1631: 3C             INC     A               
1632: 32 AC A9       LD      ($A9AC),A       
1635: 3A C0 A9       LD      A,($A9C0)       
1638: A7             AND     A               
1639: C8             RET     Z               
163A: 11 0D 01       LD      DE,$010D        
163D: FF             RST     0X38            
163E: C9             RET                     
163F: FB             EI                      
1640: AD             XOR     L               
1641: FD 39          ADD     IY,SP           
1643: AD             XOR     L               
1644: 68             LD      L,B             
1645: 43             LD      B,E             
1646: AB             XOR     E               
1647: 7C             LD      A,H             
1648: FE AB          CP      $AB             
164A: A5             AND     L               
164B: BE             CP      (HL)            
164C: AC             XOR     H               
164D: 38 C7          JR      C,$1616         
164F: AC             XOR     H               
1650: 3B             DEC     SP              
1651: 21 7B 16       LD      HL,$167B        
1654: E5             PUSH    HL              
1655: 3A AC A9       LD      A,($A9AC)       
1658: F7             RST     0X30            
1659: 4B             LD      C,E             
165A: 07             RLCA                    
165B: 34             INC     (HL)            
165C: 17             RLA                     
165D: 3F             CCF                     
165E: 2D             DEC     L               
165F: 3E 08          LD      A,$08           
1661: 48             LD      C,B             
1662: 17             RLA                     
1663: 6A             LD      L,D             
1664: 17             RLA                     
1665: 8C             ADC     A,H             
1666: 17             RLA                     
1667: B9             CP      C               
1668: 17             RLA                     
1669: 52             LD      D,D             
166A: 32 E2 17       LD      ($17E2),A       
166D: 19             ADD     HL,DE           
166E: 4B             LD      C,E             
166F: FB             EI                      
1670: 17             RLA                     
1671: 30 27          JR      NC,$169A        
1673: 26 A6          LD      H,$A6           
1675: 13             INC     DE              
1676: 88             ADC     A,B             
1677: 57             LD      D,A             
1678: A5             AND     L               
1679: BF             CP      A               
167A: B9             CP      C               
167B: 3A 86 A9       LD      A,($A986)       
167E: A7             AND     A               
167F: C2 11 0F       JP      NZ,$0F11        
1682: 3A C0 A9       LD      A,($A9C0)       
1685: A7             AND     A               
1686: C8             RET     Z               
1687: 3A AE A9       LD      A,($A9AE)       
168A: E6 18          AND     $18             
168C: C8             RET     Z               
168D: CD B6 15       CALL    $15B6           
1690: 3A AE A9       LD      A,($A9AE)       
1693: CB 67          BIT     4,A             
1695: 20 05          JR      NZ,$169C        
1697: CB 5F          BIT     3,A             
1699: 20 7E          JR      NZ,$1719        
169B: C9             RET                     
169C: 3E FF          LD      A,$FF           
169E: 32 30 AD       LD      ($AD30),A       
16A1: 32 31 AD       LD      ($AD31),A       
16A4: 3A C1 A9       LD      A,($A9C1)       
16A7: 32 10 AD       LD      ($AD10),A       
16AA: 32 20 AD       LD      ($AD20),A       
16AD: 18 7B          JR      $172A           
16AF: 06 00          LD      B,$00           
16B1: 21 9F 4D       LD      HL,$4D9F        
16B4: 3A AB A9       LD      A,($A9AB)       
16B7: 96             SUB     (HL)            
16B8: 23             INC     HL              
16B9: 10 FC          DJNZ    $16B7           
16BB: EE A2          XOR     $A2             
16BD: 32 AB A9       LD      ($A9AB),A       
16C0: CD 97 0F       CALL    $0F97           
16C3: CD DF 1E       CALL    $1EDF           
16C6: CD 97 0F       CALL    $0F97           
16C9: CD BC 2C       CALL    $2CBC           
16CC: CD 98 10       CALL    $1098           
16CF: 3A 80 A9       LD      A,($A980)       
16D2: E6 01          AND     $01             
16D4: 28 1C          JR      Z,$16F2         
16D6: 21 EB A9       LD      HL,$A9EB        
16D9: 35             DEC     (HL)            
16DA: 20 16          JR      NZ,$16F2        
16DC: 11 09 03       LD      DE,$0309        
16DF: FF             RST     0X38            
16E0: 1E 0E          LD      E,$0E           
16E2: FF             RST     0X38            
16E3: 1E 1A          LD      E,$1A           
16E5: FF             RST     0X38            
16E6: AF             XOR     A               
16E7: 32 0E AD       LD      ($AD0E),A       
16EA: 3E 2A          LD      A,$2A           
16EC: 32 EB A9       LD      ($A9EB),A       
16EF: C3 1A 0F       JP      $0F1A           
16F2: 3A 0E AD       LD      A,($AD0E)       
16F5: A7             AND     A               
16F6: C8             RET     Z               
16F7: 3A 80 A9       LD      A,($A980)       
16FA: E6 0F          AND     $0F             
16FC: 28 09          JR      Z,$1707         
16FE: FE 05          CP      $05             
1700: 28 09          JR      Z,$170B         
1702: FE 0A          CP      $0A             
1704: 28 09          JR      Z,$170F         
1706: C9             RET                     
1707: 16 02          LD      D,$02           
1709: 18 06          JR      $1711           
170B: 16 0A          LD      D,$0A           
170D: 18 02          JR      $1711           
170F: 16 0B          LD      D,$0B           
1711: 3A 04 AD       LD      A,($AD04)       
1714: C6 1A          ADD     $1A             
1716: 5F             LD      E,A             
1717: FF             RST     0X38            
1718: C9             RET                     
1719: AF             XOR     A               
171A: 32 31 AD       LD      ($AD31),A       
171D: 32 20 AD       LD      ($AD20),A       
1720: 3D             DEC     A               
1721: 32 30 AD       LD      ($AD30),A       
1724: 3A C1 A9       LD      A,($A9C1)       
1727: 32 10 AD       LD      ($AD10),A       
172A: 3E 03          LD      A,$03           
172C: 32 AB A9       LD      ($A9AB),A       
172F: AF             XOR     A               
1730: 32 AC A9       LD      ($A9AC),A       
1733: C9             RET                     
1734: CD 01 02       CALL    $0201           
1737: C0             RET     NZ              
1738: 21 48 17       LD      HL,$1748        
173B: 06 22          LD      B,$22           
173D: AF             XOR     A               
173E: 96             SUB     (HL)            
173F: 23             INC     HL              
1740: 10 FC          DJNZ    $173E           
1742: 32 17 A8       LD      ($A817),A       
1745: C3 1A 0F       JP      $0F1A           
1748: CD 06 0B       CALL    $0B06           
174B: CD 39 0B       CALL    $0B39           
174E: 21 EB A9       LD      HL,$A9EB        
1751: 35             DEC     (HL)            
1752: C0             RET     NZ              
1753: 21 3C A6       LD      HL,$A63C        
1756: 11 C7 AC       LD      DE,$ACC7        
1759: 7E             LD      A,(HL)          
175A: 12             LD      (DE),A          
175B: 13             INC     DE              
175C: CB 94          RES     2,H             
175E: 7E             LD      A,(HL)          
175F: 12             LD      (DE),A          
1760: 11 03 03       LD      DE,$0303        
1763: FF             RST     0X38            
1764: 1C             INC     E               
1765: FF             RST     0X38            
1766: C3 1A 0F       JP      $0F1A           
1769: 31 CD DA       LD      SP,$DACD        
176C: 19             ADD     HL,DE           
176D: 3A 7C A6       LD      A,($A67C)       
1770: FE 7C          CP      $7C             
1772: C2 9B 45       JP      NZ,$459B        
1775: 11 13 01       LD      DE,$0113        
1778: FF             RST     0X38            
1779: CD DC 4B       CALL    $4BDC           
177C: 21 DC A5       LD      HL,$A5DC        
177F: 11 FB AD       LD      DE,$ADFB        
1782: 7E             LD      A,(HL)          
1783: 12             LD      (DE),A          
1784: 13             INC     DE              
1785: CB 94          RES     2,H             
1787: 7E             LD      A,(HL)          
1788: 12             LD      (DE),A          
1789: C3 1A 0F       JP      $0F1A           
178C: CD 06 0B       CALL    $0B06           
178F: CD 39 0B       CALL    $0B39           
1792: 21 EB A9       LD      HL,$A9EB        
1795: 35             DEC     (HL)            
1796: C0             RET     NZ              
1797: CD DA 19       CALL    $19DA           
179A: 3A B3 47       LD      A,($47B3)       
179D: C6 02          ADD     $02             
179F: 6F             LD      L,A             
17A0: C6 6A          ADD     $6A             
17A2: 67             LD      H,A             
17A3: 7E             LD      A,(HL)          
17A4: FE 3B          CP      $3B             
17A6: C2 CA 15       JP      NZ,$15CA        
17A9: 21 7C A6       LD      HL,$A67C        
17AC: 11 43 AB       LD      DE,$AB43        
17AF: 7E             LD      A,(HL)          
17B0: 12             LD      (DE),A          
17B1: 13             INC     DE              
17B2: CB 94          RES     2,H             
17B4: 7E             LD      A,(HL)          
17B5: 12             LD      (DE),A          
17B6: C3 1A 0F       JP      $0F1A           
17B9: 3A 0D 59       LD      A,($590D)       
17BC: 4F             LD      C,A             
17BD: 3A 40 4A       LD      A,($4A40)       
17C0: 21 06 0B       LD      HL,$0B06        
17C3: 06 33          LD      B,$33           
17C5: 86             ADD     A,(HL)          
17C6: 23             INC     HL              
17C7: 10 FC          DJNZ    $17C5           
17C9: FE EF          CP      $EF             
17CB: CA 1A 0F       JP      Z,$0F1A         
17CE: 3A 89 4C       LD      A,($4C89)       
17D1: 32 08 C3       LD      ($C308),A       
17D4: 21 5C A6       LD      HL,$A65C        
17D7: 11 39 AD       LD      DE,$AD39        
17DA: 7E             LD      A,(HL)          
17DB: 12             LD      (DE),A          
17DC: 13             INC     DE              
17DD: CB 94          RES     2,H             
17DF: 7E             LD      A,(HL)          
17E0: 12             LD      (DE),A          
17E1: C9             RET                     
17E2: 3E FF          LD      A,$FF           
17E4: 32 3F AA       LD      ($AA3F),A       
17E7: 11 B9 17       LD      DE,$17B9        
17EA: 0E 08          LD      C,$08           
17EC: CD D9 4B       CALL    $4BD9           
17EF: 3A C0 27       LD      A,($27C0)       
17F2: CD 1E 29       CALL    $291E           
17F5: 32 6F AA       LD      ($AA6F),A       
17F8: C3 1A 0F       JP      $0F1A           
17FB: C3 1A 0F       JP      $0F1A           
17FE: 21 1D 18       LD      HL,$181D        
1801: E5             PUSH    HL              
1802: 3A AC A9       LD      A,($A9AC)       
1805: F7             RST     0X30            
1806: 1E 18          LD      E,$18           
1808: DB 2C          IN      A,($2C)         
180A: 30 18          JR      NC,$1824        
180C: E6 07          AND     $07             
180E: 8A             ADC     A,D             
180F: 18 72          JR      $1883           
1811: A6             AND     (HL)            
1812: 14             INC     D               
1813: 7D             LD      A,L             
1814: A5             AND     L               
1815: 38 34          JR      C,$184B         
1817: F1             POP     AF              
1818: 68             LD      L,B             
1819: 0E 34          LD      C,$34           
181B: D7             RST     0X10            
181C: B9             CP      C               
181D: C9             RET                     
181E: CD B6 15       CALL    $15B6           
1821: 21 FC A5       LD      HL,$A5FC        
1824: 11 BE AC       LD      DE,$ACBE        
1827: CD FC 1A       CALL    $1AFC           
182A: CD B5 01       CALL    $01B5           
182D: C3 1A 0F       JP      $0F1A           
1830: CD 06 0B       CALL    $0B06           
1833: CD 39 0B       CALL    $0B39           
1836: 11 01 01       LD      DE,$0101        
1839: FF             RST     0X38            
183A: 1E 14          LD      E,$14           
183C: FF             RST     0X38            
183D: 1C             INC     E               
183E: FF             RST     0X38            
183F: 1E 0F          LD      E,$0F           
1841: 3A C3 A9       LD      A,($A9C3)       
1844: A7             AND     A               
1845: 28 02          JR      Z,$1849         
1847: 1C             INC     E               
1848: 1C             INC     E               
1849: FF             RST     0X38            
184A: 1C             INC     E               
184B: FF             RST     0X38            
184C: 1E 16          LD      E,$16           
184E: FF             RST     0X38            
184F: 1E 00          LD      E,$00           
1851: FF             RST     0X38            
1852: 3A 86 A9       LD      A,($A986)       
1855: FE 02          CP      $02             
1857: 30 07          JR      NC,$1860        
1859: 11 17 01       LD      DE,$0117        
185C: FF             RST     0X38            
185D: C3 1A 0F       JP      $0F1A           
1860: 11 19 01       LD      DE,$0119        
1863: FF             RST     0X38            
1864: CD 1A 0F       CALL    $0F1A           
1867: C3 1A 0F       JP      $0F1A           
186A: 00             NOP                     
186B: 02             LD      (BC),A          
186C: 06 0D          LD      B,$0D           
186E: 00             NOP                     
186F: 03             INC     BC              
1870: 07             RLCA                    
1871: 0C             INC     C               
1872: 00             NOP                     
1873: 04             INC     B               
1874: 08             EX      AF,AF'          
1875: 0B             DEC     BC              
1876: 02             LD      (BC),A          
1877: 06 0A          LD      B,$0A           
1879: 0A             LD      A,(BC)          
187A: 04             INC     B               
187B: 08             EX      AF,AF'          
187C: 0C             INC     C               
187D: 09             ADD     HL,BC           
187E: 07             RLCA                    
187F: 0A             LD      A,(BC)          
1880: 0D             DEC     C               
1881: 07             RLCA                    
1882: 0B             DEC     BC              
1883: 0D             DEC     C               
1884: 0E 05          LD      C,$05           
1886: 0F             RRCA                    
1887: 0F             RRCA                    
1888: 0F             RRCA                    
1889: 05             DEC     B               
188A: CD 06 0B       CALL    $0B06           
188D: CD 39 0B       CALL    $0B39           
1890: 3A AE A9       LD      A,($A9AE)       
1893: CB 67          BIT     4,A             
1895: C2 9E 18       JP      NZ,$189E        
1898: CB 5F          BIT     3,A             
189A: C2 15 32       JP      NZ,$3215        
189D: C9             RET                     
189E: CD 2B 0B       CALL    $0B2B           
18A1: 3E FF          LD      A,$FF           
18A3: 32 30 AD       LD      ($AD30),A       
18A6: 32 31 AD       LD      ($AD31),A       
18A9: 3A C1 A9       LD      A,($A9C1)       
18AC: 32 10 AD       LD      ($AD10),A       
18AF: 32 20 AD       LD      ($AD20),A       
18B2: CD 0E 46       CALL    $460E           
18B5: 21 86 A9       LD      HL,$A986        
18B8: 7E             LD      A,(HL)          
18B9: D6 02          SUB     $02             
18BB: 27             DAA                     
18BC: 77             LD      (HL),A          
18BD: CD FB 4A       CALL    $4AFB           
18C0: C3 2A 17       JP      $172A           
18C3: 3A 80 A9       LD      A,($A980)       
18C6: E6 01          AND     $01             
18C8: C2 84 19       JP      NZ,$1984        
18CB: CD D1 1E       CALL    $1ED1           
18CE: 21 95 A9       LD      HL,$A995        
18D1: 0F             RRCA                    
18D2: CB 16          RL      (HL)            
18D4: 23             INC     HL              
18D5: 0F             RRCA                    
18D6: CB 16          RL      (HL)            
18D8: 23             INC     HL              
18D9: 0F             RRCA                    
18DA: 0F             RRCA                    
18DB: 0F             RRCA                    
18DC: CB 16          RL      (HL)            
18DE: 23             INC     HL              
18DF: 0F             RRCA                    
18E0: CB 16          RL      (HL)            
18E2: 7E             LD      A,(HL)          
18E3: E6 07          AND     $07             
18E5: 3D             DEC     A               
18E6: 28 3B          JR      Z,$1923         
18E8: 2B             DEC     HL              
18E9: 7E             LD      A,(HL)          
18EA: E6 07          AND     $07             
18EC: 3D             DEC     A               
18ED: 28 34          JR      Z,$1923         
18EF: 2B             DEC     HL              
18F0: 7E             LD      A,(HL)          
18F1: FE FF          CP      $FF             
18F3: CC 80 19       CALL    Z,$1980         
18F6: E6 07          AND     $07             
18F8: 3D             DEC     A               
18F9: 28 1B          JR      Z,$1916         
18FB: 2B             DEC     HL              
18FC: 7E             LD      A,(HL)          
18FD: FE 7F          CP      $7F             
18FF: CC 80 19       CALL    Z,$1980         
1902: E6 07          AND     $07             
1904: 3D             DEC     A               
1905: 28 02          JR      Z,$1909         
1907: 18 5A          JR      $1963           
1909: 21 99 A9       LD      HL,$A999        
190C: 35             DEC     (HL)            
190D: 7E             LD      A,(HL)          
190E: FE 80          CP      $80             
1910: 38 3C          JR      C,$194E         
1912: 36 1A          LD      (HL),$1A        
1914: 18 38          JR      $194E           
1916: 21 99 A9       LD      HL,$A999        
1919: 34             INC     (HL)            
191A: 7E             LD      A,(HL)          
191B: FE 1B          CP      $1B             
191D: 38 2F          JR      C,$194E         
191F: 36 00          LD      (HL),$00        
1921: 18 2B          JR      $194E           
1923: 3A 99 A9       LD      A,($A999)       
1926: 21 C7 12       LD      HL,$12C7        
1929: CF             RST     0X08            
192A: 2A 91 A9       LD      HL,($A991)      
192D: ED 5B 93 A9    LD      DE,($A993)      
1931: 12             LD      (DE),A          
1932: 77             LD      (HL),A          
1933: 3A 90 A9       LD      A,($A990)       
1936: CB 92          RES     2,D             
1938: 12             LD      (DE),A          
1939: CB D2          SET     2,D             
193B: E7             RST     0X20            
193C: 23             INC     HL              
193D: 22 91 A9       LD      ($A991),HL      
1940: ED 53 93 A9    LD      ($A993),DE      
1944: 21 9A A9       LD      HL,$A99A        
1947: 35             DEC     (HL)            
1948: 28 2B          JR      Z,$1975         
194A: AF             XOR     A               
194B: 32 99 A9       LD      ($A999),A       
194E: ED 5B 93 A9    LD      DE,($A993)      
1952: 3A 99 A9       LD      A,($A999)       
1955: 21 C7 12       LD      HL,$12C7        
1958: CF             RST     0X08            
1959: 12             LD      (DE),A          
195A: CB 92          RES     2,D             
195C: 3E 10          LD      A,$10           
195E: 12             LD      (DE),A          
195F: AF             XOR     A               
1960: 32 9C A9       LD      ($A99C),A       
1963: 3A 80 A9       LD      A,($A980)       
1966: E6 07          AND     $07             
1968: 20 30          JR      NZ,$199A        
196A: 21 EB A9       LD      HL,$A9EB        
196D: 35             DEC     (HL)            
196E: 20 2A          JR      NZ,$199A        
1970: 2A 93 A9       LD      HL,($A993)      
1973: 36 F1          LD      (HL),$F1        
1975: 3E 3C          LD      A,$3C           
1977: 32 EB A9       LD      ($A9EB),A       
197A: CD 34 56       CALL    $5634           
197D: C3 1A 0F       JP      $0F1A           
1980: 36 00          LD      (HL),$00        
1982: AF             XOR     A               
1983: C9             RET                     
1984: 21 9C A9       LD      HL,$A99C        
1987: 34             INC     (HL)            
1988: 2A 93 A9       LD      HL,($A993)      
198B: CB 94          RES     2,H             
198D: 3A 9C A9       LD      A,($A99C)       
1990: CB 67          BIT     4,A             
1992: 28 04          JR      Z,$1998         
1994: 36 14          LD      (HL),$14        
1996: 18 02          JR      $199A           
1998: 36 10          LD      (HL),$10        
199A: 21 20 AD       LD      HL,$AD20        
199D: 3A 10 AD       LD      A,($AD10)       
19A0: B6             OR      (HL)            
19A1: C0             RET     NZ              
19A2: 3A C0 A9       LD      A,($A9C0)       
19A5: A7             AND     A               
19A6: 20 26          JR      NZ,$19CE        
19A8: 3A 86 A9       LD      A,($A986)       
19AB: FE 01          CP      $01             
19AD: D8             RET     C               
19AE: 28 10          JR      Z,$19C0         
19B0: 3A AE A9       LD      A,($A9AE)       
19B3: E6 18          AND     $18             
19B5: C8             RET     Z               
19B6: FE 08          CP      $08             
19B8: 28 0E          JR      Z,$19C8         
19BA: CD B6 15       CALL    $15B6           
19BD: C3 9E 18       JP      $189E           
19C0: 3A AE A9       LD      A,($A9AE)       
19C3: E6 18          AND     $18             
19C5: FE 08          CP      $08             
19C7: C0             RET     NZ              
19C8: CD B6 15       CALL    $15B6           
19CB: C3 15 32       JP      $3215           
19CE: 3A AE A9       LD      A,($A9AE)       
19D1: E6 18          AND     $18             
19D3: C8             RET     Z               
19D4: CD B6 15       CALL    $15B6           
19D7: C3 90 16       JP      $1690           
19DA: 21 BC A2       LD      HL,$A2BC        
19DD: 06 0D          LD      B,$0D           
19DF: 7E             LD      A,(HL)          
19E0: FE 10          CP      $10             
19E2: 28 05          JR      Z,$19E9         
19E4: FE 05          CP      $05             
19E6: C2 FA 49       JP      NZ,$49FA        
19E9: 11 E0 FF       LD      DE,$FFE0        
19EC: 19             ADD     HL,DE           
19ED: 10 F0          DJNZ    $19DF           
19EF: C9             RET                     
19F0: 21 00 00       LD      HL,$0000        
19F3: 22 08 A8       LD      ($A808),HL      
19F6: 22 0A A8       LD      ($A80A),HL      
19F9: 22 06 AD       LD      ($AD06),HL      
19FC: AF             XOR     A               
19FD: 32 0D AD       LD      ($AD0D),A       
1A00: 32 F7 A8       LD      ($A8F7),A       
1A03: 32 05 AD       LD      ($AD05),A       
1A06: 3A D6 A9       LD      A,($A9D6)       
1A09: 32 D7 A9       LD      ($A9D7),A       
1A0C: 3A 0A AD       LD      A,($AD0A)       
1A0F: 32 C0 AC       LD      ($ACC0),A       
1A12: AF             XOR     A               
1A13: 32 81 AA       LD      ($AA81),A       
1A16: 32 C6 AC       LD      ($ACC6),A       
1A19: 3E 80          LD      A,$80           
1A1B: 32 02 A8       LD      ($A802),A       
1A1E: AF             XOR     A               
1A1F: 32 01 A8       LD      ($A801),A       
1A22: 3E FF          LD      A,$FF           
1A24: 32 00 A8       LD      ($A800),A       
1A27: 3E 78          LD      A,$78           
1A29: 32 41 AA       LD      ($AA41),A       
1A2C: 3E 84          LD      A,$84           
1A2E: 32 10 AA       LD      ($AA10),A       
1A31: CD AF 20       CALL    $20AF           
1A34: CD 55 27       CALL    $2755           
1A37: DD 21 C0 A8    LD      IX,$A8C0        
1A3B: FD 21 28 AA    LD      IY,$AA28        
1A3F: CD 0D 3C       CALL    $3C0D           
1A42: 06 07          LD      B,$07           
1A44: DD 21 50 A8    LD      IX,$A850        
1A48: FD 21 1A AA    LD      IY,$AA1A        
1A4C: DD 21 E0 A8    LD      IX,$A8E0        
1A50: FD 21 2C AA    LD      IY,$AA2C        
1A54: CD FB 3D       CALL    $3DFB           
1A57: DD 21 F0 A8    LD      IX,$A8F0        
1A5B: FD 21 2E AA    LD      IY,$AA2E        
1A5F: CD AD 48       CALL    $48AD           
1A62: CD DE 2B       CALL    $2BDE           
1A65: 11 10 00       LD      DE,$0010        
1A68: DD 19          ADD     IX,DE           
1A6A: FD 23          INC     IY              
1A6C: FD 23          INC     IY              
1A6E: 10 F2          DJNZ    $1A62           
1A70: CD E4 1A       CALL    $1AE4           
1A73: FD 21 28 AA    LD      IY,$AA28        
1A77: FD 36 00 00    LD      (IY+$00),$00    
1A7B: FD 36 02 00    LD      (IY+$02),$00    
1A7F: FD 36 04 00    LD      (IY+$04),$00    
1A83: FD 36 06 00    LD      (IY+$06),$00    
1A87: FD 36 31 00    LD      (IY+$31),$00    
1A8B: FD 36 33 00    LD      (IY+$33),$00    
1A8F: FD 36 35 00    LD      (IY+$35),$00    
1A93: FD 36 37 00    LD      (IY+$37),$00    
1A97: CD A5 30       CALL    $30A5           
1A9A: 3A 04 AD       LD      A,($AD04)       
1A9D: 07             RLCA                    
1A9E: 07             RLCA                    
1A9F: 07             RLCA                    
1AA0: 07             RLCA                    
1AA1: E6 F0          AND     $F0             
1AA3: 47             LD      B,A             
1AA4: 3A C0 AC       LD      A,($ACC0)       
1AA7: 80             ADD     A,B             
1AA8: 21 04 1B       LD      HL,$1B04        
1AAB: D7             RST     0X10            
1AAC: 1A             LD      A,(DE)          
1AAD: 32 44 A8       LD      ($A844),A       
1AB0: 13             INC     DE              
1AB1: 1A             LD      A,(DE)          
1AB2: 32 37 A8       LD      ($A837),A       
1AB5: 13             INC     DE              
1AB6: 1A             LD      A,(DE)          
1AB7: 32 27 A8       LD      ($A827),A       
1ABA: 13             INC     DE              
1ABB: 1A             LD      A,(DE)          
1ABC: 32 17 A8       LD      ($A817),A       
1ABF: 32 14 A8       LD      ($A814),A       
1AC2: 13             INC     DE              
1AC3: 1A             LD      A,(DE)          
1AC4: 32 C1 AC       LD      ($ACC1),A       
1AC7: 13             INC     DE              
1AC8: 1A             LD      A,(DE)          
1AC9: 32 C4 AC       LD      ($ACC4),A       
1ACC: 13             INC     DE              
1ACD: 1A             LD      A,(DE)          
1ACE: 32 C6 A8       LD      ($A8C6),A       
1AD1: 13             INC     DE              
1AD2: 1A             LD      A,(DE)          
1AD3: 32 D6 A8       LD      ($A8D6),A       
1AD6: 13             INC     DE              
1AD7: 1A             LD      A,(DE)          
1AD8: 32 E6 A8       LD      ($A8E6),A       
1ADB: 13             INC     DE              
1ADC: 1A             LD      A,(DE)          
1ADD: 32 F4 A8       LD      ($A8F4),A       
1AE0: 32 F6 A8       LD      ($A8F6),A       
1AE3: C9             RET                     
1AE4: DD 21 10 A8    LD      IX,$A810        
1AE8: 3E 01          LD      A,$01           
1AEA: 06 17          LD      B,$17           
1AEC: 11 10 00       LD      DE,$0010        
1AEF: DD 36 00 00    LD      (IX+$00),$00    
1AF3: DD 77 0F       LD      (IX+$0F),A      
1AF6: 3C             INC     A               
1AF7: DD 19          ADD     IX,DE           
1AF9: 10 F4          DJNZ    $1AEF           
1AFB: C9             RET                     
1AFC: 7E             LD      A,(HL)          
1AFD: 12             LD      (DE),A          
1AFE: 13             INC     DE              
1AFF: CB 94          RES     2,H             
1B01: 7E             LD      A,(HL)          
1B02: 12             LD      (DE),A          
1B03: C9             RET                     
1B04: B1             OR      C               
1B05: 1B             DEC     DE              
1B06: BB             CP      E               
1B07: 1B             DEC     DE              
1B08: C5             PUSH    BC              
1B09: 1B             DEC     DE              
1B0A: CF             RST     0X08            
1B0B: 1B             DEC     DE              
1B0C: D9             EXX                     
1B0D: 1B             DEC     DE              
1B0E: E3             EX      (SP),HL         
1B0F: 1B             DEC     DE              
1B10: ED                                  
1B11: 1B             DEC     DE              
1B12: F7             RST     0X30            
1B13: 1B             DEC     DE              
1B14: 01 1C 0B       LD      BC,$0B1C        
1B17: 1C             INC     E               
1B18: 15             DEC     D               
1B19: 1C             INC     E               
1B1A: 1F             RRA                     
1B1B: 1C             INC     E               
1B1C: 29             ADD     HL,HL           
1B1D: 1C             INC     E               
1B1E: 33             INC     SP              
1B1F: 1C             INC     E               
1B20: 3D             DEC     A               
1B21: 1C             INC     E               
1B22: 47             LD      B,A             
1B23: 1C             INC     E               
1B24: 51             LD      D,C             
1B25: 1C             INC     E               
1B26: 5B             LD      E,E             
1B27: 1C             INC     E               
1B28: 65             LD      H,L             
1B29: 1C             INC     E               
1B2A: 6F             LD      L,A             
1B2B: 1C             INC     E               
1B2C: 79             LD      A,C             
1B2D: 1C             INC     E               
1B2E: 83             ADD     A,E             
1B2F: 1C             INC     E               
1B30: 8D             ADC     A,L             
1B31: 1C             INC     E               
1B32: 97             SUB     A               
1B33: 1C             INC     E               
1B34: A1             AND     C               
1B35: 1C             INC     E               
1B36: AB             XOR     E               
1B37: 1C             INC     E               
1B38: B5             OR      L               
1B39: 1C             INC     E               
1B3A: BF             CP      A               
1B3B: 1C             INC     E               
1B3C: C9             RET                     
1B3D: 1C             INC     E               
1B3E: D3 1C          OUT     ($1C),A         
1B40: DD                                  
1B41: 1C             INC     E               
1B42: E7             RST     0X20            
1B43: 1C             INC     E               
1B44: F1             POP     AF              
1B45: 1C             INC     E               
1B46: FB             EI                      
1B47: 1C             INC     E               
1B48: 05             DEC     B               
1B49: 1D             DEC     E               
1B4A: 0F             RRCA                    
1B4B: 1D             DEC     E               
1B4C: 19             ADD     HL,DE           
1B4D: 1D             DEC     E               
1B4E: 23             INC     HL              
1B4F: 1D             DEC     E               
1B50: 2D             DEC     L               
1B51: 1D             DEC     E               
1B52: 37             SCF                     
1B53: 1D             DEC     E               
1B54: 41             LD      B,C             
1B55: 1D             DEC     E               
1B56: 4B             LD      C,E             
1B57: 1D             DEC     E               
1B58: 55             LD      D,L             
1B59: 1D             DEC     E               
1B5A: 5F             LD      E,A             
1B5B: 1D             DEC     E               
1B5C: 69             LD      L,C             
1B5D: 1D             DEC     E               
1B5E: 73             LD      (HL),E          
1B5F: 1D             DEC     E               
1B60: 7D             LD      A,L             
1B61: 1D             DEC     E               
1B62: 87             ADD     A,A             
1B63: 1D             DEC     E               
1B64: 91             SUB     C               
1B65: 1D             DEC     E               
1B66: 9B             SBC     E               
1B67: 1D             DEC     E               
1B68: A5             AND     L               
1B69: 1D             DEC     E               
1B6A: AF             XOR     A               
1B6B: 1D             DEC     E               
1B6C: B9             CP      C               
1B6D: 1D             DEC     E               
1B6E: C3 1D CD       JP      $CD1D           
1B71: 1D             DEC     E               
1B72: D7             RST     0X10            
1B73: 1D             DEC     E               
1B74: E1             POP     HL              
1B75: 1D             DEC     E               
1B76: EB             EX      DE,HL           
1B77: 1D             DEC     E               
1B78: F5             PUSH    AF              
1B79: 1D             DEC     E               
1B7A: FF             RST     0X38            
1B7B: 1D             DEC     E               
1B7C: 09             ADD     HL,BC           
1B7D: 1E 13          LD      E,$13           
1B7F: 1E 1D          LD      E,$1D           
1B81: 1E 27          LD      E,$27           
1B83: 1E 31          LD      E,$31           
1B85: 1E 3B          LD      E,$3B           
1B87: 1E 45          LD      E,$45           
1B89: 1E 4F          LD      E,$4F           
1B8B: 1E 59          LD      E,$59           
1B8D: 1E 63          LD      E,$63           
1B8F: 1E 6D          LD      E,$6D           
1B91: 1E 77          LD      E,$77           
1B93: 1E 81          LD      E,$81           
1B95: 1E 8B          LD      E,$8B           
1B97: 1E 95          LD      E,$95           
1B99: 1E 9F          LD      E,$9F           
1B9B: 1E A9          LD      E,$A9           
1B9D: 1E B3          LD      E,$B3           
1B9F: 1E BD          LD      E,$BD           
1BA1: 1E C7          LD      E,$C7           
1BA3: 1E 5F          LD      E,$5F           
1BA5: A5             AND     L               
1BA6: 13             INC     DE              
1BA7: 00             NOP                     
1BA8: D7             RST     0X10            
1BA9: 34             INC     (HL)            
1BAA: 34             INC     (HL)            
1BAB: F1             POP     AF              
1BAC: 88             ADC     A,B             
1BAD: 57             LD      D,A             
1BAE: A5             AND     L               
1BAF: BF             CP      A               
1BB0: B9             CP      C               
1BB1: 00             NOP                     
1BB2: 20 50          JR      NZ,$1C04        
1BB4: 3C             INC     A               
1BB5: 04             INC     B               
1BB6: 50             LD      D,B             
1BB7: 00             NOP                     
1BB8: 50             LD      D,B             
1BB9: 18 5A          JR      $1C15           
1BBB: 01 20 4E       LD      BC,$4E20        
1BBE: 3C             INC     A               
1BBF: 04             INC     B               
1BC0: 50             LD      D,B             
1BC1: 00             NOP                     
1BC2: 4E             LD      C,(HL)          
1BC3: 18 54          JR      $1C19           
1BC5: 01 28 4C       LD      BC,$4C28        
1BC8: 32 05 60       LD      ($6005),A       
1BCB: 01 4C 1C       LD      BC,$1C4C        
1BCE: 4E             LD      C,(HL)          
1BCF: 02             LD      (BC),A          
1BD0: 28 48          JR      Z,$1C1A         
1BD2: 28 05          JR      Z,$1BD9         
1BD4: 60             LD      H,B             
1BD5: 01 48 1C       LD      BC,$1C48        
1BD8: 48             LD      C,B             
1BD9: 02             LD      (BC),A          
1BDA: 30 46          JR      NC,$1C22        
1BDC: 1E 06          LD      E,$06           
1BDE: 70             LD      (HL),B          
1BDF: 01 46 1C       LD      BC,$1C46        
1BE2: 42             LD      B,D             
1BE3: 03             INC     BC              
1BE4: 30 44          JR      NC,$1C2A        
1BE6: 1E 06          LD      E,$06           
1BE8: 70             LD      (HL),B          
1BE9: 02             LD      (BC),A          
1BEA: 44             LD      B,H             
1BEB: 20 3C          JR      NZ,$1C29        
1BED: 03             INC     BC              
1BEE: 38 42          JR      C,$1C32         
1BF0: 1E 06          LD      E,$06           
1BF2: 80             ADD     A,B             
1BF3: 02             LD      (BC),A          
1BF4: 42             LD      B,D             
1BF5: 20 36          JR      NZ,$1C2D        
1BF7: 03             INC     BC              
1BF8: 38 40          JR      C,$1C3A         
1BFA: 1E 06          LD      E,$06           
1BFC: 80             ADD     A,B             
1BFD: 02             LD      (BC),A          
1BFE: 40             LD      B,B             
1BFF: 20 30          JR      NZ,$1C31        
1C01: 04             INC     B               
1C02: 40             LD      B,B             
1C03: 3F             CCF                     
1C04: 1E 07          LD      E,$07           
1C06: 90             SUB     B               
1C07: 03             INC     BC              
1C08: 3F             CCF                     
1C09: 24             INC     H               
1C0A: 2A 04 40       LD      HL,($4004)      
1C0D: 3E 1E          LD      A,$1E           
1C0F: 07             RLCA                    
1C10: 90             SUB     B               
1C11: 03             INC     BC              
1C12: 3E 24          LD      A,$24           
1C14: 24             INC     H               
1C15: 04             INC     B               
1C16: 40             LD      B,B             
1C17: 3D             DEC     A               
1C18: 1E 07          LD      E,$07           
1C1A: A0             AND     B               
1C1B: 03             INC     BC              
1C1C: 3D             DEC     A               
1C1D: 24             INC     H               
1C1E: 1E 04          LD      E,$04           
1C20: 40             LD      B,B             
1C21: 3C             INC     A               
1C22: 1E 07          LD      E,$07           
1C24: B0             OR      B               
1C25: 03             INC     BC              
1C26: 3C             INC     A               
1C27: 28 1E          JR      Z,$1C47         
1C29: 04             INC     B               
1C2A: 48             LD      C,B             
1C2B: 3B             DEC     SP              
1C2C: 1E 07          LD      E,$07           
1C2E: C0             RET     NZ              
1C2F: 03             INC     BC              
1C30: 3B             DEC     SP              
1C31: 28 1E          JR      Z,$1C51         
1C33: 04             INC     B               
1C34: 48             LD      C,B             
1C35: 3A 1E 07       LD      A,($071E)       
1C38: D0             RET     NC              
1C39: 03             INC     BC              
1C3A: 3A 2C 1E       LD      A,($1E2C)       
1C3D: 04             INC     B               
1C3E: 48             LD      C,B             
1C3F: 39             ADD     HL,SP           
1C40: 1E 07          LD      E,$07           
1C42: E0             RET     PO              
1C43: 03             INC     BC              
1C44: 39             ADD     HL,SP           
1C45: 30 1E          JR      NC,$1C65        
1C47: 04             INC     B               
1C48: 48             LD      C,B             
1C49: 38 19          JR      C,$1C64         
1C4B: 07             RLCA                    
1C4C: F0             RET     P               
1C4D: 03             INC     BC              
1C4E: 38 30          JR      C,$1C80         
1C50: 19             ADD     HL,DE           
1C51: 01 28 48       LD      BC,$4828        
1C54: 32 05 50       LD      ($5005),A       
1C57: 01 5C 00       LD      BC,$005C        
1C5A: 1E 01          LD      E,$01           
1C5C: 28 48          JR      Z,$1CA6         
1C5E: 28 05          JR      Z,$1C65         
1C60: 50             LD      D,B             
1C61: 01 5A 00       LD      BC,$005A        
1C64: 1E 02          LD      E,$02           
1C66: 30 48          JR      NC,$1CB0        
1C68: 1E 05          LD      E,$05           
1C6A: 60             LD      H,B             
1C6B: 01 58 00       LD      BC,$0058        
1C6E: 1E 02          LD      E,$02           
1C70: 30 48          JR      NC,$1CBA        
1C72: 1E 06          LD      E,$06           
1C74: 60             LD      H,B             
1C75: 01 56 00       LD      BC,$0056        
1C78: 1E 02          LD      E,$02           
1C7A: 30 48          JR      NC,$1CC4        
1C7C: 1E 06          LD      E,$06           
1C7E: 70             LD      (HL),B          
1C7F: 02             LD      (BC),A          
1C80: 54             LD      D,H             
1C81: 00             NOP                     
1C82: 1E 03          LD      E,$03           
1C84: 38 40          JR      C,$1CC6         
1C86: 1E 06          LD      E,$06           
1C88: 70             LD      (HL),B          
1C89: 02             LD      (BC),A          
1C8A: 52             LD      D,D             
1C8B: 00             NOP                     
1C8C: 1E 03          LD      E,$03           
1C8E: 38 40          JR      C,$1CD0         
1C90: 1E 06          LD      E,$06           
1C92: 80             ADD     A,B             
1C93: 02             LD      (BC),A          
1C94: 50             LD      D,B             
1C95: 00             NOP                     
1C96: 1E 03          LD      E,$03           
1C98: 38 40          JR      C,$1CDA         
1C9A: 1E 06          LD      E,$06           
1C9C: 80             ADD     A,B             
1C9D: 02             LD      (BC),A          
1C9E: 4C             LD      C,H             
1C9F: 00             NOP                     
1CA0: 1E 04          LD      E,$04           
1CA2: 40             LD      B,B             
1CA3: 40             LD      B,B             
1CA4: 1E 07          LD      E,$07           
1CA6: 90             SUB     B               
1CA7: 02             LD      (BC),A          
1CA8: 4C             LD      C,H             
1CA9: 00             NOP                     
1CAA: 1E 04          LD      E,$04           
1CAC: 40             LD      B,B             
1CAD: 40             LD      B,B             
1CAE: 1E 07          LD      E,$07           
1CB0: 90             SUB     B               
1CB1: 02             LD      (BC),A          
1CB2: 48             LD      C,B             
1CB3: 00             NOP                     
1CB4: 1E 04          LD      E,$04           
1CB6: 48             LD      C,B             
1CB7: 38 1E          JR      C,$1CD7         
1CB9: 07             RLCA                    
1CBA: A0             AND     B               
1CBB: 02             LD      (BC),A          
1CBC: 48             LD      C,B             
1CBD: 00             NOP                     
1CBE: 1E 04          LD      E,$04           
1CC0: 48             LD      C,B             
1CC1: 38 1E          JR      C,$1CE1         
1CC3: 07             RLCA                    
1CC4: B0             OR      B               
1CC5: 02             LD      (BC),A          
1CC6: 48             LD      C,B             
1CC7: 00             NOP                     
1CC8: 1E 04          LD      E,$04           
1CCA: 48             LD      C,B             
1CCB: 38 1E          JR      C,$1CEB         
1CCD: 07             RLCA                    
1CCE: C0             RET     NZ              
1CCF: 02             LD      (BC),A          
1CD0: 48             LD      C,B             
1CD1: 00             NOP                     
1CD2: 1E 04          LD      E,$04           
1CD4: 48             LD      C,B             
1CD5: 38 1E          JR      C,$1CF5         
1CD7: 07             RLCA                    
1CD8: D0             RET     NC              
1CD9: 02             LD      (BC),A          
1CDA: 48             LD      C,B             
1CDB: 00             NOP                     
1CDC: 1E 04          LD      E,$04           
1CDE: 50             LD      D,B             
1CDF: 38 1E          JR      C,$1CFF         
1CE1: 07             RLCA                    
1CE2: E0             RET     PO              
1CE3: 02             LD      (BC),A          
1CE4: 48             LD      C,B             
1CE5: 00             NOP                     
1CE6: 1E 04          LD      E,$04           
1CE8: 58             LD      E,B             
1CE9: 30 19          JR      NC,$1D04        
1CEB: 07             RLCA                    
1CEC: F0             RET     P               
1CED: 02             LD      (BC),A          
1CEE: 48             LD      C,B             
1CEF: 00             NOP                     
1CF0: 19             ADD     HL,DE           
1CF1: 01 20 50       LD      BC,$5020        
1CF4: 32 03 50       LD      ($5003),A       
1CF7: 01 50 08       LD      BC,$0850        
1CFA: 1E 01          LD      E,$01           
1CFC: 20 50          JR      NZ,$1D4E        
1CFE: 28 04          JR      Z,$1D04         
1D00: 50             LD      D,B             
1D01: 01 50 08       LD      BC,$0850        
1D04: 1E 01          LD      E,$01           
1D06: 20 50          JR      NZ,$1D58        
1D08: 1E 04          LD      E,$04           
1D0A: 60             LD      H,B             
1D0B: 01 50 0C       LD      BC,$0C50        
1D0E: 1E 01          LD      E,$01           
1D10: 28 50          JR      Z,$1D62         
1D12: 1E 04          LD      E,$04           
1D14: 60             LD      H,B             
1D15: 02             LD      (BC),A          
1D16: 50             LD      D,B             
1D17: 0C             INC     C               
1D18: 1E 01          LD      E,$01           
1D1A: 28 48          JR      Z,$1D64         
1D1C: 1E 05          LD      E,$05           
1D1E: 70             LD      (HL),B          
1D1F: 02             LD      (BC),A          
1D20: 48             LD      C,B             
1D21: 10 1E          DJNZ    $1D41           
1D23: 01 28 48       LD      BC,$4828        
1D26: 1E 05          LD      E,$05           
1D28: 80             ADD     A,B             
1D29: 02             LD      (BC),A          
1D2A: 48             LD      C,B             
1D2B: 10 1E          DJNZ    $1D4B           
1D2D: 01 30 48       LD      BC,$4830        
1D30: 1E 05          LD      E,$05           
1D32: 90             SUB     B               
1D33: 03             INC     BC              
1D34: 48             LD      C,B             
1D35: 14             INC     D               
1D36: 1E 01          LD      E,$01           
1D38: 30 48          JR      NC,$1D82        
1D3A: 1E 06          LD      E,$06           
1D3C: A0             AND     B               
1D3D: 03             INC     BC              
1D3E: 48             LD      C,B             
1D3F: 14             INC     D               
1D40: 1E 02          LD      E,$02           
1D42: 30 40          JR      NC,$1D84        
1D44: 1E 06          LD      E,$06           
1D46: B0             OR      B               
1D47: 03             INC     BC              
1D48: 40             LD      B,B             
1D49: 18 1E          JR      $1D69           
1D4B: 02             LD      (BC),A          
1D4C: 38 40          JR      C,$1D8E         
1D4E: 1E 06          LD      E,$06           
1D50: C0             RET     NZ              
1D51: 03             INC     BC              
1D52: 40             LD      B,B             
1D53: 18 1E          JR      $1D73           
1D55: 02             LD      (BC),A          
1D56: 38 40          JR      C,$1D98         
1D58: 1E 06          LD      E,$06           
1D5A: D0             RET     NC              
1D5B: 03             INC     BC              
1D5C: 40             LD      B,B             
1D5D: 18 1E          JR      $1D7D           
1D5F: 02             LD      (BC),A          
1D60: 38 40          JR      C,$1DA2         
1D62: 1E 06          LD      E,$06           
1D64: D0             RET     NC              
1D65: 03             INC     BC              
1D66: 40             LD      B,B             
1D67: 18 1E          JR      $1D87           
1D69: 02             LD      (BC),A          
1D6A: 40             LD      B,B             
1D6B: 38 1E          JR      C,$1D8B         
1D6D: 06 E0          LD      B,$E0           
1D6F: 03             INC     BC              
1D70: 38 18          JR      C,$1D8A         
1D72: 1E 02          LD      E,$02           
1D74: 48             LD      C,B             
1D75: 38 1E          JR      C,$1D95         
1D77: 06 E0          LD      B,$E0           
1D79: 03             INC     BC              
1D7A: 38 18          JR      C,$1D94         
1D7C: 1E 02          LD      E,$02           
1D7E: 50             LD      D,B             
1D7F: 38 1E          JR      C,$1D9F         
1D81: 06 F0          LD      B,$F0           
1D83: 03             INC     BC              
1D84: 38 18          JR      C,$1D9E         
1D86: 1E 03          LD      E,$03           
1D88: 58             LD      E,B             
1D89: 30 19          JR      NC,$1DA4        
1D8B: 07             RLCA                    
1D8C: F0             RET     P               
1D8D: 03             INC     BC              
1D8E: 30 18          JR      NC,$1DA8        
1D90: 19             ADD     HL,DE           
1D91: 01 20 50       LD      BC,$5020        
1D94: 1E 04          LD      E,$04           
1D96: 60             LD      H,B             
1D97: 01 50 00       LD      BC,$0050        
1D9A: 1E 01          LD      E,$01           
1D9C: 20 50          JR      NZ,$1DEE        
1D9E: 1E 04          LD      E,$04           
1DA0: 70             LD      (HL),B          
1DA1: 01 50 00       LD      BC,$0050        
1DA4: 1E 01          LD      E,$01           
1DA6: 28 50          JR      Z,$1DF8         
1DA8: 1E 04          LD      E,$04           
1DAA: 80             ADD     A,B             
1DAB: 01 50 00       LD      BC,$0050        
1DAE: 1E 01          LD      E,$01           
1DB0: 28 50          JR      Z,$1E02         
1DB2: 1E 05          LD      E,$05           
1DB4: 90             SUB     B               
1DB5: 02             LD      (BC),A          
1DB6: 50             LD      D,B             
1DB7: 00             NOP                     
1DB8: 1E 01          LD      E,$01           
1DBA: 30 48          JR      NC,$1E04        
1DBC: 1E 05          LD      E,$05           
1DBE: A0             AND     B               
1DBF: 02             LD      (BC),A          
1DC0: 48             LD      C,B             
1DC1: 00             NOP                     
1DC2: 1E 01          LD      E,$01           
1DC4: 30 48          JR      NC,$1E0E        
1DC6: 1E 05          LD      E,$05           
1DC8: B0             OR      B               
1DC9: 02             LD      (BC),A          
1DCA: 48             LD      C,B             
1DCB: 00             NOP                     
1DCC: 1E 01          LD      E,$01           
1DCE: 38 48          JR      C,$1E18         
1DD0: 1E 05          LD      E,$05           
1DD2: C0             RET     NZ              
1DD3: 03             INC     BC              
1DD4: 48             LD      C,B             
1DD5: 00             NOP                     
1DD6: 1E 01          LD      E,$01           
1DD8: 38 48          JR      C,$1E22         
1DDA: 1E 06          LD      E,$06           
1DDC: D0             RET     NC              
1DDD: 03             INC     BC              
1DDE: 48             LD      C,B             
1DDF: 00             NOP                     
1DE0: 1E 01          LD      E,$01           
1DE2: 40             LD      B,B             
1DE3: 40             LD      B,B             
1DE4: 1E 06          LD      E,$06           
1DE6: E0             RET     PO              
1DE7: 03             INC     BC              
1DE8: 40             LD      B,B             
1DE9: 00             NOP                     
1DEA: 1E 01          LD      E,$01           
1DEC: 40             LD      B,B             
1DED: 40             LD      B,B             
1DEE: 1E 06          LD      E,$06           
1DF0: F0             RET     P               
1DF1: 03             INC     BC              
1DF2: 40             LD      B,B             
1DF3: 00             NOP                     
1DF4: 1E 01          LD      E,$01           
1DF6: 48             LD      C,B             
1DF7: 40             LD      B,B             
1DF8: 1E 06          LD      E,$06           
1DFA: F0             RET     P               
1DFB: 03             INC     BC              
1DFC: 40             LD      B,B             
1DFD: 00             NOP                     
1DFE: 1E 01          LD      E,$01           
1E00: 48             LD      C,B             
1E01: 40             LD      B,B             
1E02: 1E 06          LD      E,$06           
1E04: F0             RET     P               
1E05: 03             INC     BC              
1E06: 40             LD      B,B             
1E07: 00             NOP                     
1E08: 1E 01          LD      E,$01           
1E0A: 50             LD      D,B             
1E0B: 38 1E          JR      C,$1E2B         
1E0D: 06 F0          LD      B,$F0           
1E0F: 03             INC     BC              
1E10: 38 00          JR      C,$1E12         
1E12: 1E 01          LD      E,$01           
1E14: 50             LD      D,B             
1E15: 38 1E          JR      C,$1E35         
1E17: 06 F0          LD      B,$F0           
1E19: 03             INC     BC              
1E1A: 38 00          JR      C,$1E1C         
1E1C: 1E 01          LD      E,$01           
1E1E: 58             LD      E,B             
1E1F: 38 1E          JR      C,$1E3F         
1E21: 06 F0          LD      B,$F0           
1E23: 03             INC     BC              
1E24: 38 00          JR      C,$1E26         
1E26: 1E 01          LD      E,$01           
1E28: 58             LD      E,B             
1E29: 30 19          JR      NC,$1E44        
1E2B: 06 F0          LD      B,$F0           
1E2D: 03             INC     BC              
1E2E: 30 00          JR      NC,$1E30        
1E30: 19             ADD     HL,DE           
1E31: 01 20 50       LD      BC,$5020        
1E34: 5A             LD      E,D             
1E35: 03             INC     BC              
1E36: 00             NOP                     
1E37: 01 58 3C       LD      BC,$3C58        
1E3A: 64             LD      H,H             
1E3B: 01 20 50       LD      BC,$5020        
1E3E: 5A             LD      E,D             
1E3F: 03             INC     BC              
1E40: 10 01          DJNZ    $1E43           
1E42: 54             LD      D,H             
1E43: 46             LD      B,(HL)          
1E44: 5A             LD      E,D             
1E45: 01 28 50       LD      BC,$5028        
1E48: 50             LD      D,B             
1E49: 04             INC     B               
1E4A: 20 01          JR      NZ,$1E4D        
1E4C: 52             LD      D,D             
1E4D: 50             LD      D,B             
1E4E: 50             LD      D,B             
1E4F: 01 28 50       LD      BC,$5028        
1E52: 46             LD      B,(HL)          
1E53: 04             INC     B               
1E54: 30 02          JR      NC,$1E58        
1E56: 50             LD      D,B             
1E57: 5A             LD      E,D             
1E58: 46             LD      B,(HL)          
1E59: 01 30 48       LD      BC,$4830        
1E5C: 46             LD      B,(HL)          
1E5D: 04             INC     B               
1E5E: 40             LD      B,B             
1E5F: 02             LD      (BC),A          
1E60: 4E             LD      C,(HL)          
1E61: 64             LD      H,H             
1E62: 46             LD      B,(HL)          
1E63: 01 30 48       LD      BC,$4830        
1E66: 3C             INC     A               
1E67: 05             DEC     B               
1E68: 50             LD      D,B             
1E69: 02             LD      (BC),A          
1E6A: 4B             LD      C,E             
1E6B: 6E             LD      L,(HL)          
1E6C: 3C             INC     A               
1E6D: 01 38 48       LD      BC,$4838        
1E70: 3C             INC     A               
1E71: 05             DEC     B               
1E72: 60             LD      H,B             
1E73: 03             INC     BC              
1E74: 48             LD      C,B             
1E75: 78             LD      A,B             
1E76: 3C             INC     A               
1E77: 01 38 40       LD      BC,$4038        
1E7A: 32 05 70       LD      ($7005),A       
1E7D: 03             INC     BC              
1E7E: 46             LD      B,(HL)          
1E7F: 82             ADD     A,D             
1E80: 3C             INC     A               
1E81: 01 40 40       LD      BC,$4040        
1E84: 32 05 80       LD      ($8005),A       
1E87: 03             INC     BC              
1E88: 44             LD      B,H             
1E89: 8C             ADC     A,H             
1E8A: 32 01 40       LD      ($4001),A       
1E8D: 40             LD      B,B             
1E8E: 28 05          JR      Z,$1E95         
1E90: 90             SUB     B               
1E91: 03             INC     BC              
1E92: 44             LD      B,H             
1E93: 96             SUB     (HL)            
1E94: 32 01 48       LD      ($4801),A       
1E97: 40             LD      B,B             
1E98: 28 05          JR      Z,$1E9F         
1E9A: A0             AND     B               
1E9B: 03             INC     BC              
1E9C: 42             LD      B,D             
1E9D: A0             AND     B               
1E9E: 32 01 48       LD      ($4801),A       
1EA1: 3C             INC     A               
1EA2: 1E 05          LD      E,$05           
1EA4: B0             OR      B               
1EA5: 03             INC     BC              
1EA6: 42             LD      B,D             
1EA7: AA             XOR     D               
1EA8: 28 01          JR      Z,$1EAB         
1EAA: 50             LD      D,B             
1EAB: 3C             INC     A               
1EAC: 1E 05          LD      E,$05           
1EAE: C0             RET     NZ              
1EAF: 03             INC     BC              
1EB0: 40             LD      B,B             
1EB1: B4             OR      H               
1EB2: 28 01          JR      Z,$1EB5         
1EB4: 50             LD      D,B             
1EB5: 3C             INC     A               
1EB6: 1E 05          LD      E,$05           
1EB8: D0             RET     NC              
1EB9: 03             INC     BC              
1EBA: 3C             INC     A               
1EBB: BE             CP      (HL)            
1EBC: 28 01          JR      Z,$1EBF         
1EBE: 58             LD      E,B             
1EBF: 38 1E          JR      C,$1EDF         
1EC1: 05             DEC     B               
1EC2: E0             RET     PO              
1EC3: 03             INC     BC              
1EC4: 38 C8          JR      C,$1E8E         
1EC6: 1E 01          LD      E,$01           
1EC8: 58             LD      E,B             
1EC9: 30 19          JR      NC,$1EE4        
1ECB: 05             DEC     B               
1ECC: F0             RET     P               
1ECD: 03             INC     BC              
1ECE: 34             INC     (HL)            
1ECF: D2 19 3A       JP      NC,$3A19        
1ED2: 87             ADD     A,A             
1ED3: A9             XOR     C               
1ED4: A7             AND     A               
1ED5: 21 AF A9       LD      HL,$A9AF        
1ED8: 20 03          JR      NZ,$1EDD        
1EDA: 21 B0 A9       LD      HL,$A9B0        
1EDD: 7E             LD      A,(HL)          
1EDE: C9             RET                     
1EDF: DD 21 00 A8    LD      IX,$A800        
1EE3: FD 21 10 AA    LD      IY,$AA10        
1EE7: 3A 00 A8       LD      A,($A800)       
1EEA: A7             AND     A               
1EEB: C8             RET     Z               
1EEC: 3C             INC     A               
1EED: C2 10 20       JP      NZ,$2010        
1EF0: 3A 30 AD       LD      A,($AD30)       
1EF3: A7             AND     A               
1EF4: CA 4B 21       JP      Z,$214B         
1EF7: CD D1 1E       CALL    $1ED1           
1EFA: E6 0F          AND     $0F             
1EFC: 20 03          JR      NZ,$1F01        
1EFE: C3 42 1F       JP      $1F42           
1F01: 21 2E 1F       LD      HL,$1F2E        
1F04: CF             RST     0X08            
1F05: 47             LD      B,A             
1F06: 3A 02 A8       LD      A,($A802)       
1F09: 90             SUB     B               
1F0A: CA 42 1F       JP      Z,$1F42         
1F0D: 4F             LD      C,A             
1F0E: 3A 04 AD       LD      A,($AD04)       
1F11: E6 0F          AND     $0F             
1F13: FE 03          CP      $03             
1F15: 30 04          JR      NC,$1F1B        
1F17: 16 03          LD      D,$03           
1F19: 18 02          JR      $1F1D           
1F1B: 16 04          LD      D,$04           
1F1D: 79             LD      A,C             
1F1E: C6 01          ADD     $01             
1F20: FE 03          CP      $03             
1F22: DA 3E 1F       JP      C,$1F3E         
1F25: 79             LD      A,C             
1F26: FE 80          CP      $80             
1F28: D2 6F 1F       JP      NC,$1F6F        
1F2B: C3 68 1F       JP      $1F68           
1F2E: 00             NOP                     
1F2F: 00             NOP                     
1F30: 80             ADD     A,B             
1F31: 00             NOP                     
1F32: C0             RET     NZ              
1F33: E0             RET     PO              
1F34: A0             AND     B               
1F35: 00             NOP                     
1F36: 40             LD      B,B             
1F37: 20 60          JR      NZ,$1F99        
1F39: 00             NOP                     
1F3A: 00             NOP                     
1F3B: 00             NOP                     
1F3C: 00             NOP                     
1F3D: 00             NOP                     
1F3E: 78             LD      A,B             
1F3F: 32 02 A8       LD      ($A802),A       
1F42: 21 55 1F       LD      HL,$1F55        
1F45: E5             PUSH    HL              
1F46: 3A 04 AD       LD      A,($AD04)       
1F49: A7             AND     A               
1F4A: CA 4E 59       JP      Z,$594E         
1F4D: FE 03          CP      $03             
1F4F: DA 65 59       JP      C,$5965         
1F52: C3 6B 59       JP      $596B           
1F55: AF             XOR     A               
1F56: 67             LD      H,A             
1F57: 6F             LD      L,A             
1F58: ED 52          SBC     HL,DE           
1F5A: 22 08 A8       LD      ($A808),HL      
1F5D: AF             XOR     A               
1F5E: 67             LD      H,A             
1F5F: 6F             LD      L,A             
1F60: ED 42          SBC     HL,BC           
1F62: 22 0A A8       LD      ($A80A),HL      
1F65: C3 AF 20       JP      $20AF           
1F68: 92             SUB     D               
1F69: 80             ADD     A,B             
1F6A: 32 02 A8       LD      ($A802),A       
1F6D: 18 D3          JR      $1F42           
1F6F: 82             ADD     A,D             
1F70: 80             ADD     A,B             
1F71: 32 02 A8       LD      ($A802),A       
1F74: 18 CC          JR      $1F42           
1F76: F1             POP     AF              
1F77: F1             POP     AF              
1F78: F1             POP     AF              
1F79: F1             POP     AF              
1F7A: F1             POP     AF              
1F7B: F1             POP     AF              
1F7C: F1             POP     AF              
1F7D: DD                                  
1F7E: F1             POP     AF              
1F7F: F1             POP     AF              
1F80: F1             POP     AF              
1F81: F1             POP     AF              
1F82: F0             RET     P               
1F83: F1             POP     AF              
1F84: F1             POP     AF              
1F85: F1             POP     AF              
1F86: F1             POP     AF              
1F87: C3 F1 F1       JP      $F1F1           
1F8A: F1             POP     AF              
1F8B: F1             POP     AF              
1F8C: EA F1 F1       JP      PE,$F1F1        
1F8F: F1             POP     AF              
1F90: F1             POP     AF              
1F91: F1             POP     AF              
1F92: F1             POP     AF              
1F93: F1             POP     AF              
1F94: F1             POP     AF              
1F95: F1             POP     AF              
1F96: B7             OR      A               
1F97: F1             POP     AF              
1F98: F1             POP     AF              
1F99: F1             POP     AF              
1F9A: F1             POP     AF              
1F9B: 4D             LD      C,L             
1F9C: F1             POP     AF              
1F9D: F1             POP     AF              
1F9E: F1             POP     AF              
1F9F: E5             PUSH    HL              
1FA0: 2D             DEC     L               
1FA1: 6E             LD      L,(HL)          
1FA2: F1             POP     AF              
1FA3: F1             POP     AF              
1FA4: 5E             LD      E,(HL)          
1FA5: 61             LD      H,C             
1FA6: E6 F1          AND     $F1             
1FA8: F1             POP     AF              
1FA9: F1             POP     AF              
1FAA: B2             OR      D               
1FAB: F1             POP     AF              
1FAC: F1             POP     AF              
1FAD: F1             POP     AF              
1FAE: F1             POP     AF              
1FAF: 53             LD      D,E             
1FB0: F1             POP     AF              
1FB1: F1             POP     AF              
1FB2: F1             POP     AF              
1FB3: F1             POP     AF              
1FB4: 95             SUB     L               
1FB5: F1             POP     AF              
1FB6: F1             POP     AF              
1FB7: F1             POP     AF              
1FB8: 45             LD      B,L             
1FB9: CA F1 F1       JP      Z,$F1F1         
1FBC: F1             POP     AF              
1FBD: C6 2C          ADD     $2C             
1FBF: 97             SUB     A               
1FC0: F1             POP     AF              
1FC1: F1             POP     AF              
1FC2: 81             ADD     A,C             
1FC3: 69             LD      L,C             
1FC4: 1E F1          LD      E,$F1           
1FC6: F1             POP     AF              
1FC7: BC             CP      H               
1FC8: A1             AND     C               
1FC9: 60             LD      H,B             
1FCA: F1             POP     AF              
1FCB: F1             POP     AF              
1FCC: F4 EB F1       CALL    P,$F1EB         
1FCF: F1             POP     AF              
1FD0: F1             POP     AF              
1FD1: F1             POP     AF              
1FD2: 48             LD      C,B             
1FD3: F1             POP     AF              
1FD4: F1             POP     AF              
1FD5: F1             POP     AF              
1FD6: E0             RET     PO              
1FD7: 63             LD      H,E             
1FD8: 35             DEC     (HL)            
1FD9: F1             POP     AF              
1FDA: F1             POP     AF              
1FDB: AA             XOR     D               
1FDC: B4             OR      H               
1FDD: 8A             ADC     A,D             
1FDE: F1             POP     AF              
1FDF: F1             POP     AF              
1FE0: 51             LD      D,C             
1FE1: E9             JP      (HL)            
1FE2: F6 F1          OR      $F1             
1FE4: F1             POP     AF              
1FE5: 82             ADD     A,D             
1FE6: 92             SUB     D               
1FE7: 98             SBC     B               
1FE8: F1             POP     AF              
1FE9: F1             POP     AF              
1FEA: F1             POP     AF              
1FEB: 46             LD      B,(HL)          
1FEC: F1             POP     AF              
1FED: F1             POP     AF              
1FEE: F1             POP     AF              
1FEF: F1             POP     AF              
1FF0: F1             POP     AF              
1FF1: F1             POP     AF              
1FF2: F1             POP     AF              
1FF3: F1             POP     AF              
1FF4: F1             POP     AF              
1FF5: F1             POP     AF              
1FF6: F1             POP     AF              
1FF7: F1             POP     AF              
1FF8: F1             POP     AF              
1FF9: F1             POP     AF              
1FFA: F1             POP     AF              
1FFB: F1             POP     AF              
1FFC: F1             POP     AF              
1FFD: F1             POP     AF              
1FFE: F1             POP     AF              
1FFF: F1             POP     AF              
2000: F1             POP     AF              
2001: F1             POP     AF              
2002: F1             POP     AF              
2003: F1             POP     AF              
2004: F1             POP     AF              
2005: F1             POP     AF              
2006: F1             POP     AF              
2007: F1             POP     AF              
2008: F1             POP     AF              
2009: F1             POP     AF              
200A: F1             POP     AF              
200B: F1             POP     AF              
200C: 19             ADD     HL,DE           
200D: DF             RST     0X18            
200E: 78             LD      A,B             
200F: C9             RET                     
2010: DD 7E 00       LD      A,(IX+$00)      
2013: FE B4          CP      $B4             
2015: 38 29          JR      C,$2040         
2017: DD 36 00 B4    LD      (IX+$00),$B4    
201B: FD 36 01 FF    LD      (IY+$01),$FF    
201F: 3A 04 AD       LD      A,($AD04)       
2022: FE 02          CP      $02             
2024: D4 79 56       CALL    NC,$5679        
2027: CD D2 56       CALL    $56D2           
202A: 3A FE AB       LD      A,($ABFE)       
202D: FE A5          CP      $A5             
202F: C2 63 20       JP      NZ,$2063        
2032: 11 FF AB       LD      DE,$ABFF        
2035: 1A             LD      A,(DE)          
2036: FE 05          CP      $05             
2038: CA 40 20       JP      Z,$2040         
203B: FE 10          CP      $10             
203D: C2 63 20       JP      NZ,$2063        
2040: DD 35 00       DEC     (IX+$00)        
2043: DD 7E 00       LD      A,(IX+$00)      
2046: FE B3          CP      $B3             
2048: 28 1C          JR      Z,$2066         
204A: FE AB          CP      $AB             
204C: 28 1D          JR      Z,$206B         
204E: FE A3          CP      $A3             
2050: 28 1E          JR      Z,$2070         
2052: FE 9B          CP      $9B             
2054: 28 1F          JR      Z,$2075         
2056: FE 93          CP      $93             
2058: 28 20          JR      Z,$207A         
205A: FE 8B          CP      $8B             
205C: 28 21          JR      Z,$207F         
205E: FE 83          CP      $83             
2060: 28 22          JR      Z,$2084         
2062: C9             RET                     
2063: C3 2E 1F       JP      $1F2E           
2066: 11 76 1F       LD      DE,$1F76        
2069: 18 1E          JR      $2089           
206B: 11 94 1F       LD      DE,$1F94        
206E: 18 19          JR      $2089           
2070: 11 B2 1F       LD      DE,$1FB2        
2073: 18 14          JR      $2089           
2075: 11 D0 1F       LD      DE,$1FD0        
2078: 18 0F          JR      $2089           
207A: 11 D0 1F       LD      DE,$1FD0        
207D: 18 0A          JR      $2089           
207F: 11 B2 1F       LD      DE,$1FB2        
2082: 18 05          JR      $2089           
2084: 11 EE 1F       LD      DE,$1FEE        
2087: 18 00          JR      $2089           
2089: 21 AF A5       LD      HL,$A5AF        
208C: 06 C1          LD      B,$C1           
208E: 3A 04 AD       LD      A,($AD04)       
2091: 80             ADD     A,B             
2092: 4F             LD      C,A             
2093: D9             EXX                     
2094: 3A 7A 33       LD      A,($337A)       
2097: 47             LD      B,A             
2098: D9             EXX                     
2099: 3A 02 49       LD      A,($4902)       
209C: 47             LD      B,A             
209D: 1A             LD      A,(DE)          
209E: 77             LD      (HL),A          
209F: CB 94          RES     2,H             
20A1: 71             LD      (HL),C          
20A2: CB D4          SET     2,H             
20A4: 23             INC     HL              
20A5: 13             INC     DE              
20A6: 10 F5          DJNZ    $209D           
20A8: 3E 1B          LD      A,$1B           
20AA: DF             RST     0X18            
20AB: D9             EXX                     
20AC: 10 EA          DJNZ    $2098           
20AE: C9             RET                     
20AF: DD 21 00 A8    LD      IX,$A800        
20B3: 11 20 00       LD      DE,$0020        
20B6: 3A 02 A8       LD      A,($A802)       
20B9: C6 04          ADD     $04             
20BB: 0F             RRCA                    
20BC: 0F             RRCA                    
20BD: 0F             RRCA                    
20BE: E6 1F          AND     $1F             
20C0: 21 CE 20       LD      HL,$20CE        
20C3: DF             RST     0X18            
20C4: 7E             LD      A,(HL)          
20C5: 32 11 AA       LD      ($AA11),A       
20C8: 19             ADD     HL,DE           
20C9: 7E             LD      A,(HL)          
20CA: 32 40 AA       LD      ($AA40),A       
20CD: C9             RET                     
20CE: F0             RET     P               
20CF: F1             POP     AF              
20D0: F2 F3 F4       JP      P,$F4F3         
20D3: F5             PUSH    AF              
20D4: F6 F7          OR      $F7             
20D6: E8             RET     PE              
20D7: F7             RST     0X30            
20D8: F6 F5          OR      $F5             
20DA: F4 F3 F2       CALL    P,$F2F3         
20DD: F1             POP     AF              
20DE: F0             RET     P               
20DF: EF             RST     0X28            
20E0: EE ED          XOR     $ED             
20E2: EC EB EA       CALL    PE,$EAEB        
20E5: E9             JP      (HL)            
20E6: E8             RET     PE              
20E7: E9             JP      (HL)            
20E8: EA EB EC       JP      PE,$ECEB        
20EB: ED                                  
20EC: EE EF          XOR     $EF             
20EE: 40             LD      B,B             
20EF: 40             LD      B,B             
20F0: 40             LD      B,B             
20F1: 40             LD      B,B             
20F2: 40             LD      B,B             
20F3: 40             LD      B,B             
20F4: 40             LD      B,B             
20F5: 40             LD      B,B             
20F6: 80             ADD     A,B             
20F7: C0             RET     NZ              
20F8: C0             RET     NZ              
20F9: C0             RET     NZ              
20FA: C0             RET     NZ              
20FB: C0             RET     NZ              
20FC: C0             RET     NZ              
20FD: C0             RET     NZ              
20FE: C0             RET     NZ              
20FF: C0             RET     NZ              
2100: C0             RET     NZ              
2101: C0             RET     NZ              
2102: C0             RET     NZ              
2103: C0             RET     NZ              
2104: C0             RET     NZ              
2105: C0             RET     NZ              
2106: 40             LD      B,B             
2107: 40             LD      B,B             
2108: 40             LD      B,B             
2109: 40             LD      B,B             
210A: 40             LD      B,B             
210B: 40             LD      B,B             
210C: 40             LD      B,B             
210D: 40             LD      B,B             
210E: 21 F3 AD       LD      HL,$ADF3        
2111: EB             EX      DE,HL           
2112: 3A 14 AD       LD      A,($AD14)       
2115: A7             AND     A               
2116: 28 28          JR      Z,$2140         
2118: FE 03          CP      $03             
211A: 28 24          JR      Z,$2140         
211C: FE 01          CP      $01             
211E: 28 25          JR      Z,$2145         
2120: 21 FA 22       LD      HL,$22FA        
2123: 7E             LD      A,(HL)          
2124: 3C             INC     A               
2125: 32 F2 AD       LD      ($ADF2),A       
2128: EB             EX      DE,HL           
2129: 73             LD      (HL),E          
212A: 2C             INC     L               
212B: 72             LD      (HL),D          
212C: 21 FB AD       LD      HL,$ADFB        
212F: 7E             LD      A,(HL)          
2130: FE FD          CP      $FD             
2132: C2 3D 21       JP      NZ,$213D        
2135: 23             INC     HL              
2136: 7E             LD      A,(HL)          
2137: FE 10          CP      $10             
2139: C8             RET     Z               
213A: FE 05          CP      $05             
213C: C8             RET     Z               
213D: C3 51 22       JP      $2251           
2140: 21 8C 21       LD      HL,$218C        
2143: 18 DE          JR      $2123           
2145: 21 51 22       LD      HL,$2251        
2148: 18 D9          JR      $2123           
214A: C9             RET                     
214B: 21 F2 AD       LD      HL,$ADF2        
214E: 7E             LD      A,(HL)          
214F: 47             LD      B,A             
2150: E6 3F          AND     $3F             
2152: 28 07          JR      Z,$215B         
2154: 3D             DEC     A               
2155: 28 04          JR      Z,$215B         
2157: 05             DEC     B               
2158: 70             LD      (HL),B          
2159: 18 0F          JR      $216A           
215B: 23             INC     HL              
215C: 5E             LD      E,(HL)          
215D: 23             INC     HL              
215E: 56             LD      D,(HL)          
215F: 13             INC     DE              
2160: 72             LD      (HL),D          
2161: 2B             DEC     HL              
2162: 73             LD      (HL),E          
2163: EB             EX      DE,HL           
2164: 7E             LD      A,(HL)          
2165: 1B             DEC     DE              
2166: 3C             INC     A               
2167: 12             LD      (DE),A          
2168: 18 E1          JR      $214B           
216A: 78             LD      A,B             
216B: D9             EXX                     
216C: 07             RLCA                    
216D: 07             RLCA                    
216E: E6 03          AND     $03             
2170: CA 42 1F       JP      Z,$1F42         
2173: 3D             DEC     A               
2174: 28 0B          JR      Z,$2181         
2176: 3A 02 A8       LD      A,($A802)       
2179: C6 03          ADD     $03             
217B: 32 02 A8       LD      ($A802),A       
217E: C3 42 1F       JP      $1F42           
2181: 3A 02 A8       LD      A,($A802)       
2184: D6 03          SUB     $03             
2186: 32 02 A8       LD      ($A802),A       
2189: C3 42 1F       JP      $1F42           
218C: 3C             INC     A               
218D: 3C             INC     A               
218E: 3C             INC     A               
218F: 3C             INC     A               
2190: 0B             DEC     BC              
2191: 95             SUB     L               
2192: 03             INC     BC              
2193: 66             LD      H,(HL)          
2194: 95             SUB     L               
2195: 7C             LD      A,H             
2196: 59             LD      E,C             
2197: 8D             ADC     A,L             
2198: 4B             LD      C,E             
2199: 8E             ADC     A,(HL)          
219A: 4A             LD      C,D             
219B: 02             LD      (BC),A          
219C: 8B             ADC     A,E             
219D: 1A             LD      A,(DE)          
219E: 55             LD      D,L             
219F: 0E 8A          LD      C,$8A           
21A1: 7C             LD      A,H             
21A2: 4E             LD      C,(HL)          
21A3: 05             DEC     B               
21A4: 8A             ADC     A,D             
21A5: 0B             DEC     BC              
21A6: 86             ADD     A,(HL)          
21A7: 46             LD      B,(HL)          
21A8: 03             INC     BC              
21A9: 4A             LD      C,D             
21AA: 0D             DEC     C               
21AB: 7C             LD      A,H             
21AC: 5A             LD      E,D             
21AD: 36 AB          LD      (HL),$AB        
21AF: 08             EX      AF,AF'          
21B0: 55             LD      D,L             
21B1: 08             EX      AF,AF'          
21B2: 56             LD      D,(HL)          
21B3: 01 4A 05       LD      BC,$054A        
21B6: 56             LD      D,(HL)          
21B7: 03             INC     BC              
21B8: 7C             LD      A,H             
21B9: 4D             LD      C,L             
21BA: BC             CP      H               
21BB: 83             ADD     A,E             
21BC: 0A             LD      A,(BC)          
21BD: 4B             LD      C,E             
21BE: 07             RLCA                    
21BF: BC             CP      H               
21C0: 81             ADD     A,C             
21C1: 72             LD      (HL),D          
21C2: 02             LD      (BC),A          
21C3: 56             LD      D,(HL)          
21C4: 02             LD      (BC),A          
21C5: 6A             LD      L,D             
21C6: 01 95 3B       LD      BC,$3B95        
21C9: 88             ADC     A,B             
21CA: 53             LD      D,E             
21CB: 03             INC     BC              
21CC: BC             CP      H               
21CD: 95             SUB     L               
21CE: 46             LD      B,(HL)          
21CF: 0B             DEC     BC              
21D0: 95             SUB     L               
21D1: 04             INC     B               
21D2: A0             AND     B               
21D3: 0C             INC     C               
21D4: 4A             LD      C,D             
21D5: 02             LD      (BC),A          
21D6: 56             LD      D,(HL)          
21D7: 03             INC     BC              
21D8: 55             LD      D,L             
21D9: 01 95 03       LD      BC,$0395        
21DC: 4A             LD      C,D             
21DD: 04             INC     B               
21DE: 8A             ADC     A,D             
21DF: 02             LD      (BC),A          
21E0: 4A             LD      C,D             
21E1: 02             LD      (BC),A          
21E2: 8A             ADC     A,D             
21E3: 29             ADD     HL,HL           
21E4: 8B             ADC     A,E             
21E5: 06 4B          LD      B,$4B           
21E7: 16 4A          LD      D,$4A           
21E9: 01 95 0D       LD      BC,$0D95        
21EC: 88             ADC     A,B             
21ED: 53             LD      D,E             
21EE: 01 6A 0F       LD      BC,$0F6A        
21F1: 8A             ADC     A,D             
21F2: 08             EX      AF,AF'          
21F3: 8B             ADC     A,E             
21F4: 0D             DEC     C               
21F5: 4B             LD      C,E             
21F6: 08             EX      AF,AF'          
21F7: 8B             ADC     A,E             
21F8: 07             RLCA                    
21F9: 55             LD      D,L             
21FA: 02             LD      (BC),A          
21FB: 69             LD      L,C             
21FC: 89             ADC     A,C             
21FD: 03             INC     BC              
21FE: 4B             LD      C,E             
21FF: 01 7C 6F       LD      BC,$6F7C        
2202: 05             DEC     B               
2203: 8B             ADC     A,E             
2204: 4B             LD      C,E             
2205: 0D             DEC     C               
2206: 8B             ADC     A,E             
2207: 01 4E 83       LD      BC,$834E        
220A: 01 8B 0F       LD      BC,$0F8B        
220D: 55             LD      D,L             
220E: 05             DEC     B               
220F: A2             AND     D               
2210: 42             LD      B,D             
2211: 10 60          DJNZ    $2273           
2213: 26 4B          LD      H,$4B           
2215: 02             LD      (BC),A          
2216: 8B             ADC     A,E             
2217: 08             EX      AF,AF'          
2218: 4B             LD      C,E             
2219: 05             DEC     B               
221A: 8F             ADC     A,A             
221B: 4F             LD      C,A             
221C: 01 95 17       LD      BC,$1795        
221F: 4A             LD      C,D             
2220: 0E 8A          LD      C,$8A           
2222: 04             INC     B               
2223: A0             AND     B               
2224: 1B             DEC     DE              
2225: 8B             ADC     A,E             
2226: 11 4B 0A       LD      DE,$0A4B        
2229: 52             LD      D,D             
222A: 97             SUB     A               
222B: 4D             LD      C,L             
222C: 8F             ADC     A,A             
222D: 47             LD      B,A             
222E: 06 8B          LD      B,$8B           
2230: 02             LD      (BC),A          
2231: 55             LD      D,L             
2232: 03             INC     BC              
2233: 9D             SBC     L               
2234: 67             LD      H,A             
2235: 8A             ADC     A,D             
2236: 0A             LD      A,(BC)          
2237: 56             LD      D,(HL)          
2238: 05             DEC     B               
2239: 8B             ADC     A,E             
223A: 02             LD      (BC),A          
223B: 48             LD      C,B             
223C: 88             ADC     A,B             
223D: 03             INC     BC              
223E: 55             LD      D,L             
223F: 09             ADD     HL,BC           
2240: 60             LD      H,B             
2241: 03             INC     BC              
2242: 76             HALT                    
2243: 13             INC     DE              
2244: 8B             ADC     A,E             
2245: 24             INC     H               
2246: 4B             LD      C,E             
2247: 2F             CPL                     
2248: 8B             ADC     A,E             
2249: 05             DEC     B               
224A: 8B             ADC     A,E             
224B: 08             EX      AF,AF'          
224C: 8A             ADC     A,D             
224D: 15             DEC     D               
224E: 96             SUB     (HL)            
224F: 3C             INC     A               
2250: 3C             INC     A               
2251: 3C             INC     A               
2252: 3C             INC     A               
2253: 3C             INC     A               
2254: 3C             INC     A               
2255: 0A             LD      A,(BC)          
2256: 95             SUB     L               
2257: 60             LD      H,B             
2258: 04             INC     B               
2259: 9E             SBC     (HL)            
225A: 53             LD      D,E             
225B: 0D             DEC     C               
225C: 8B             ADC     A,E             
225D: 02             LD      (BC),A          
225E: 4B             LD      C,E             
225F: 0F             RRCA                    
2260: 93             SUB     E               
2261: 53             LD      D,E             
2262: 07             RLCA                    
2263: A9             XOR     C               
2264: 54             LD      D,H             
2265: 0A             LD      A,(BC)          
2266: 96             SUB     (HL)            
2267: 03             INC     BC              
2268: 60             LD      H,B             
2269: 0F             RRCA                    
226A: 8A             ADC     A,D             
226B: 23             INC     HL              
226C: 48             LD      C,B             
226D: B9             CP      C               
226E: 02             LD      (BC),A          
226F: 82             ADD     A,D             
2270: 59             LD      E,C             
2271: 9F             SBC     A               
2272: 59             LD      E,C             
2273: 01 8B 22       LD      BC,$228B        
2276: AB             XOR     E               
2277: 02             LD      (BC),A          
2278: 4B             LD      C,E             
2279: 02             LD      (BC),A          
227A: 8B             ADC     A,E             
227B: 07             RLCA                    
227C: 55             LD      D,L             
227D: AC             XOR     H               
227E: 42             LD      B,D             
227F: 01 50 90       LD      BC,$9050        
2282: 02             LD      (BC),A          
2283: 55             LD      D,L             
2284: 35             DEC     (HL)            
2285: 90             SUB     B               
2286: 50             LD      D,B             
2287: 04             INC     B               
2288: 92             SUB     D               
2289: 5B             LD      E,E             
228A: 89             ADC     A,C             
228B: 1F             RRA                     
228C: 48             LD      C,B             
228D: 88             ADC     A,B             
228E: 05             DEC     B               
228F: 8C             ADC     A,H             
2290: 42             LD      B,D             
2291: 05             DEC     B               
2292: 4A             LD      C,D             
2293: 3C             INC     A               
2294: 0C             INC     C               
2295: 46             LD      B,(HL)          
2296: 86             ADD     A,(HL)          
2297: 3C             INC     A               
2298: 04             INC     B               
2299: 93             SUB     E               
229A: 5E             LD      E,(HL)          
229B: 06 4B          LD      B,$4B           
229D: 09             ADD     HL,BC           
229E: 4A             LD      C,D             
229F: 0A             LD      A,(BC)          
22A0: 7C             LD      A,H             
22A1: 7C             LD      A,H             
22A2: 6F             LD      L,A             
22A3: BC             CP      H               
22A4: 01 8B 07       LD      BC,$078B        
22A7: 92             SUB     D               
22A8: 48             LD      C,B             
22A9: 07             RLCA                    
22AA: 88             ADC     A,B             
22AB: 7C             LD      A,H             
22AC: 7C             LD      A,H             
22AD: 45             LD      B,L             
22AE: 11 90 50       LD      DE,$5090        
22B1: 01 8B 07       LD      BC,$078B        
22B4: 4B             LD      C,E             
22B5: 0C             INC     C               
22B6: 8B             ADC     A,E             
22B7: 0A             LD      A,(BC)          
22B8: 76             HALT                    
22B9: AB             XOR     E               
22BA: 12             LD      (DE),A          
22BB: 87             ADD     A,A             
22BC: 47             LD      B,A             
22BD: 18 8B          JR      $224A           
22BF: 03             INC     BC              
22C0: 8A             ADC     A,D             
22C1: 02             LD      (BC),A          
22C2: 96             SUB     (HL)            
22C3: 08             EX      AF,AF'          
22C4: 4B             LD      C,E             
22C5: 02             LD      (BC),A          
22C6: 8B             ADC     A,E             
22C7: 07             RLCA                    
22C8: 95             SUB     L               
22C9: 3C             INC     A               
22CA: 3C             INC     A               
22CB: 17             RLA                     
22CC: 55             LD      D,L             
22CD: 3C             INC     A               
22CE: 05             DEC     B               
22CF: 56             LD      D,(HL)          
22D0: 20 7C          JR      NZ,$234E        
22D2: 44             LD      B,H             
22D3: 06 67          LD      B,$67           
22D5: BC             CP      H               
22D6: 4D             LD      C,L             
22D7: 8E             ADC     A,(HL)          
22D8: 0C             INC     C               
22D9: 56             LD      D,(HL)          
22DA: 02             LD      (BC),A          
22DB: 4A             LD      C,D             
22DC: 1A             LD      A,(DE)          
22DD: 4B             LD      C,E             
22DE: 39             ADD     HL,SP           
22DF: 55             LD      D,L             
22E0: 25             DEC     H               
22E1: 56             LD      D,(HL)          
22E2: 20 55          JR      NZ,$2339        
22E4: 0B             DEC     BC              
22E5: 4B             LD      C,E             
22E6: 03             INC     BC              
22E7: 60             LD      H,B             
22E8: 06 4A          LD      B,$4A           
22EA: 03             INC     BC              
22EB: 41             LD      B,C             
22EC: 01 BC 9F       LD      BC,$9FBC        
22EF: 50             LD      D,B             
22F0: 04             INC     B               
22F1: 96             SUB     (HL)            
22F2: 0F             RRCA                    
22F3: 4B             LD      C,E             
22F4: 07             RLCA                    
22F5: 8B             ADC     A,E             
22F6: 3C             INC     A               
22F7: 3C             INC     A               
22F8: 3C             INC     A               
22F9: 3C             INC     A               
22FA: 3C             INC     A               
22FB: 3C             INC     A               
22FC: 3C             INC     A               
22FD: 3C             INC     A               
22FE: 02             LD      (BC),A          
22FF: 90             SUB     B               
2300: 45             LD      B,L             
2301: 02             LD      (BC),A          
2302: 4B             LD      C,E             
2303: 02             LD      (BC),A          
2304: 48             LD      C,B             
2305: 88             ADC     A,B             
2306: 07             RLCA                    
2307: 8A             ADC     A,D             
2308: 55             LD      D,L             
2309: 01 4A 01       LD      BC,$014A        
230C: 58             LD      E,B             
230D: 82             ADD     A,D             
230E: 03             INC     BC              
230F: 8A             ADC     A,D             
2310: 5F             LD      E,A             
2311: 01 60 07       LD      BC,$0760        
2314: B2             OR      D               
2315: 52             LD      D,D             
2316: 03             INC     BC              
2317: 46             LD      B,(HL)          
2318: 86             ADD     A,(HL)          
2319: 1E 49          LD      E,$49           
231B: 89             ADC     A,C             
231C: 08             EX      AF,AF'          
231D: 4B             LD      C,E             
231E: 01 94 49       LD      BC,$4994        
2321: 05             DEC     B               
2322: 8A             ADC     A,D             
2323: 4A             LD      C,D             
2324: 3C             INC     A               
2325: 3C             INC     A               
2326: 0A             LD      A,(BC)          
2327: BC             CP      H               
2328: 84             ADD     A,H             
2329: 11 53 88       LD      DE,$8853        
232C: 01 4A 0B       LD      BC,$0B4A        
232F: 6B             LD      L,E             
2330: 06 4B          LD      B,$4B           
2332: 24             INC     H               
2333: 4A             LD      C,D             
2334: 11 56 08       LD      DE,$0856        
2337: 4A             LD      C,D             
2338: 0E 4B          LD      C,$4B           
233A: 07             RLCA                    
233B: 55             LD      D,L             
233C: 07             RLCA                    
233D: 4B             LD      C,E             
233E: 07             RLCA                    
233F: 7C             LD      A,H             
2340: 72             LD      (HL),D          
2341: 8E             ADC     A,(HL)          
2342: 01 AF 44       LD      BC,$44AF        
2345: 02             LD      (BC),A          
2346: 56             LD      D,(HL)          
2347: 8B             ADC     A,E             
2348: 04             INC     B               
2349: 5A             LD      E,D             
234A: 85             ADD     A,L             
234B: 02             LD      (BC),A          
234C: 8A             ADC     A,D             
234D: 02             LD      (BC),A          
234E: 90             SUB     B               
234F: 45             LD      B,L             
2350: 09             ADD     HL,BC           
2351: 8B             ADC     A,E             
2352: 01 48 89       LD      BC,$8948        
2355: 41             LD      B,C             
2356: 02             LD      (BC),A          
2357: 4B             LD      C,E             
2358: 05             DEC     B               
2359: B5             OR      L               
235A: 10 4D          DJNZ    $23A9           
235C: 83             ADD     A,E             
235D: 03             INC     BC              
235E: B5             OR      L               
235F: 4B             LD      C,E             
2360: 03             INC     BC              
2361: A0             AND     B               
2362: 07             RLCA                    
2363: 72             LD      (HL),D          
2364: 88             ADC     A,B             
2365: 08             EX      AF,AF'          
2366: 4B             LD      C,E             
2367: 01 50 85       LD      BC,$8550        
236A: 03             INC     BC              
236B: 8B             ADC     A,E             
236C: 02             LD      (BC),A          
236D: 55             LD      D,L             
236E: 05             DEC     B               
236F: 95             SUB     L               
2370: 06 60          LD      B,$60           
2372: 06 55          LD      B,$55           
2374: 01 4B 09       LD      BC,$094B        
2377: 48             LD      C,B             
2378: 8F             ADC     A,A             
2379: 47             LD      B,A             
237A: 03             INC     BC              
237B: 4B             LD      C,E             
237C: 01 96 07       LD      BC,$0796        
237F: 8A             ADC     A,D             
2380: 05             DEC     B               
2381: 6A             LD      L,D             
2382: 18 4B          JR      $23CF           
2384: 0A             LD      A,(BC)          
2385: 8B             ADC     A,E             
2386: 06 8A          LD      B,$8A           
2388: 02             LD      (BC),A          
2389: 44             LD      B,H             
238A: 84             ADD     A,H             
238B: 06 8B          LD      B,$8B           
238D: 08             EX      AF,AF'          
238E: 8B             ADC     A,E             
238F: 14             INC     D               
2390: BC             CP      H               
2391: 84             ADD     A,H             
2392: 03             INC     BC              
2393: 59             LD      E,C             
2394: 83             ADD     A,E             
2395: 02             LD      (BC),A          
2396: 8B             ADC     A,E             
2397: 03             INC     BC              
2398: 60             LD      H,B             
2399: 08             EX      AF,AF'          
239A: 8B             ADC     A,E             
239B: 05             DEC     B               
239C: 7C             LD      A,H             
239D: 5A             LD      E,D             
239E: 01 B6 0A       LD      BC,$0AB6        
23A1: 48             LD      C,B             
23A2: 95             SUB     L               
23A3: 4D             LD      C,L             
23A4: 01 8A 09       LD      BC,$098A        
23A7: 51             LD      D,C             
23A8: BC             CP      H               
23A9: 85             ADD     A,L             
23AA: 65             LD      H,L             
23AB: 2D             DEC     L               
23AC: 6B             LD      L,E             
23AD: 01 95 4D       LD      BC,$4D95        
23B0: 83             ADD     A,E             
23B1: 02             LD      (BC),A          
23B2: 8A             ADC     A,D             
23B3: 4A             LD      C,D             
23B4: 01 8B 02       LD      BC,$028B        
23B7: 72             LD      (HL),D          
23B8: 85             ADD     A,L             
23B9: 53             LD      D,E             
23BA: 01 95 02       LD      BC,$0295        
23BD: 8B             ADC     A,E             
23BE: 06 95          LD      B,$95           
23C0: 03             INC     BC              
23C1: 8B             ADC     A,E             
23C2: 01 8A 01       LD      BC,$018A        
23C5: 4A             LD      C,D             
23C6: 07             RLCA                    
23C7: 95             SUB     L               
23C8: 01 6B 03       LD      BC,$036B        
23CB: 97             SUB     A               
23CC: 41             LD      B,C             
23CD: 05             DEC     B               
23CE: 4B             LD      C,E             
23CF: 0B             DEC     BC              
23D0: 48             LD      C,B             
23D1: 88             ADC     A,B             
23D2: 05             DEC     B               
23D3: 60             LD      H,B             
23D4: 3C             INC     A               
23D5: 3C             INC     A               
23D6: 3C             INC     A               
23D7: 3C             INC     A               
23D8: 73             LD      (HL),E          
23D9: A6             AND     (HL)            
23DA: 14             INC     D               
23DB: 7E             LD      A,(HL)          
23DC: 29             ADD     HL,HL           
23DD: F8             RET     M               
23DE: 9B             SBC     E               
23DF: 13             INC     DE              
23E0: 13             INC     DE              
23E1: 96             SUB     (HL)            
23E2: B9             CP      C               
23E3: 3A 00 A8       LD      A,($A800)       
23E6: 3C             INC     A               
23E7: C2 96 24       JP      NZ,$2496        
23EA: 3A C6 AC       LD      A,($ACC6)       
23ED: A7             AND     A               
23EE: C2 96 24       JP      NZ,$2496        
23F1: CD D1 1E       CALL    $1ED1           
23F4: 07             RLCA                    
23F5: 07             RLCA                    
23F6: 07             RLCA                    
23F7: 07             RLCA                    
23F8: 21 8E A9       LD      HL,$A98E        
23FB: CB 16          RL      (HL)            
23FD: 7E             LD      A,(HL)          
23FE: E6 03          AND     $03             
2400: FE 01          CP      $01             
2402: 21 81 AA       LD      HL,$AA81        
2405: 20 02          JR      NZ,$2409        
2407: 36 03          LD      (HL),$03        
2409: 3A 30 AD       LD      A,($AD30)       
240C: A7             AND     A               
240D: 28 05          JR      Z,$2414         
240F: 7E             LD      A,(HL)          
2410: A7             AND     A               
2411: CA 96 24       JP      Z,$2496         
2414: 23             INC     HL              
2415: 7E             LD      A,(HL)          
2416: A7             AND     A               
2417: C2 96 24       JP      NZ,$2496        
241A: DD 21 80 AA    LD      IX,$AA80        
241E: 06 06          LD      B,$06           
2420: DD 7E 00       LD      A,(IX+$00)      
2423: A7             AND     A               
2424: 28 23          JR      Z,$2449         
2426: ED 5B 46 0D    LD      DE,($0D46)      
242A: DD 19          ADD     IX,DE           
242C: 10 F2          DJNZ    $2420           
242E: C3 96 24       JP      $2496           
2431: 16 A7          LD      D,$A7           
2433: 13             INC     DE              
2434: 96             SUB     (HL)            
2435: ED                                  
2436: DC F1 8C       CALL    C,$8CF1         
2439: 68             LD      L,B             
243A: 3B             DEC     SP              
243B: 0D             DEC     C               
243C: ED                                  
243D: F1             POP     AF              
243E: 96             SUB     (HL)            
243F: 13             INC     DE              
2440: 13             INC     DE              
2441: 13             INC     DE              
2442: 13             INC     DE              
2443: F1             POP     AF              
2444: 88             ADC     A,B             
2445: DC ED 11       CALL    C,$11ED         
2448: B9             CP      C               
2449: CD 7E 56       CALL    $567E           
244C: AF             XOR     A               
244D: 67             LD      H,A             
244E: 6F             LD      L,A             
244F: ED 4B 08 A8    LD      BC,($A808)      
2453: ED 42          SBC     HL,BC           
2455: 29             ADD     HL,HL           
2456: 29             ADD     HL,HL           
2457: DD 75 0A       LD      (IX+$0A),L      
245A: DD 74 0B       LD      (IX+$0B),H      
245D: AF             XOR     A               
245E: 67             LD      H,A             
245F: 6F             LD      L,A             
2460: ED 4B 0A A8    LD      BC,($A80A)      
2464: ED 42          SBC     HL,BC           
2466: 29             ADD     HL,HL           
2467: 29             ADD     HL,HL           
2468: DD 75 0C       LD      (IX+$0C),L      
246B: DD 74 0D       LD      (IX+$0D),H      
246E: 3A 02 A8       LD      A,($A802)       
2471: C6 04          ADD     $04             
2473: 0F             RRCA                    
2474: 0F             RRCA                    
2475: 0F             RRCA                    
2476: E6 1F          AND     $1F             
2478: 21 71 27       LD      HL,$2771        
247B: CD 8C 01       CALL    $018C           
247E: DD 35 00       DEC     (IX+$00)        
2481: DD 36 03 00    LD      (IX+$03),$00    
2485: DD 73 04       LD      (IX+$04),E      
2488: DD 36 05 00    LD      (IX+$05),$00    
248C: DD 72 06       LD      (IX+$06),D      
248F: 21 81 AA       LD      HL,$AA81        
2492: 35             DEC     (HL)            
2493: 23             INC     HL              
2494: 36 06          LD      (HL),$06        
2496: 3A 82 AA       LD      A,($AA82)       
2499: A7             AND     A               
249A: 28 04          JR      Z,$24A0         
249C: 3D             DEC     A               
249D: 32 82 AA       LD      ($AA82),A       
24A0: DD 21 80 AA    LD      IX,$AA80        
24A4: 06 06          LD      B,$06           
24A6: D9             EXX                     
24A7: DD 7E 00       LD      A,(IX+$00)      
24AA: A7             AND     A               
24AB: 28 46          JR      Z,$24F3         
24AD: 3C             INC     A               
24AE: 20 4C          JR      NZ,$24FC        
24B0: DD 6E 0A       LD      L,(IX+$0A)      
24B3: DD 66 0B       LD      H,(IX+$0B)      
24B6: ED 5B 08 A8    LD      DE,($A808)      
24BA: 19             ADD     HL,DE           
24BB: DD 56 04       LD      D,(IX+$04)      
24BE: DD 5E 03       LD      E,(IX+$03)      
24C1: 19             ADD     HL,DE           
24C2: 7C             LD      A,H             
24C3: C6 10          ADD     $10             
24C5: FE 10          CP      $10             
24C7: DA FC 24       JP      C,$24FC         
24CA: DD 74 04       LD      (IX+$04),H      
24CD: DD 75 03       LD      (IX+$03),L      
24D0: DD 6E 0C       LD      L,(IX+$0C)      
24D3: DD 66 0D       LD      H,(IX+$0D)      
24D6: ED 5B 0A A8    LD      DE,($A80A)      
24DA: 19             ADD     HL,DE           
24DB: DD 56 06       LD      D,(IX+$06)      
24DE: DD 5E 05       LD      E,(IX+$05)      
24E1: 19             ADD     HL,DE           
24E2: 7C             LD      A,H             
24E3: C6 08          ADD     $08             
24E5: FE 18          CP      $18             
24E7: DA FC 24       JP      C,$24FC         
24EA: DD 74 06       LD      (IX+$06),H      
24ED: DD 75 05       LD      (IX+$05),L      
24F0: CD 37 53       CALL    $5337           
24F3: 11 10 00       LD      DE,$0010        
24F6: DD 19          ADD     IX,DE           
24F8: D9             EXX                     
24F9: 10 AB          DJNZ    $24A6           
24FB: C9             RET                     
24FC: AF             XOR     A               
24FD: DD 77 00       LD      (IX+$00),A      
2500: DD 77 04       LD      (IX+$04),A      
2503: DD 77 06       LD      (IX+$06),A      
2506: C3 F3 24       JP      $24F3           
2509: E0             RET     PO              
250A: A4             AND     H               
250B: 14             INC     D               
250C: 9B             SBC     E               
250D: 10 0D          DJNZ    $251C           
250F: 88             ADC     A,B             
2510: B9             CP      C               
2511: 21 00 AC       LD      HL,$AC00        
2514: 06 40          LD      B,$40           
2516: 36 FF          LD      (HL),$FF        
2518: 23             INC     HL              
2519: 10 FB          DJNZ    $2516           
251B: CD 67 4B       CALL    $4B67           
251E: 32 00 C2       LD      ($C200),A       
2521: CD A5 4B       CALL    $4BA5           
2524: 32 00 C2       LD      ($C200),A       
2527: CD 6A 52       CALL    $526A           
252A: 32 00 C2       LD      ($C200),A       
252D: C3 AA 52       JP      $52AA           
2530: 19             ADD     HL,DE           
2531: 01 18 01       LD      BC,$0118        
2534: 17             RLA                     
2535: 01 16 01       LD      BC,$0116        
2538: 15             DEC     D               
2539: 01 14 01       LD      BC,$0114        
253C: 13             INC     DE              
253D: 01 10 01       LD      BC,$0110        
2540: 0E 01          LD      C,$01           
2542: 0C             INC     C               
2543: 01 0A 01       LD      BC,$010A        
2546: 08             EX      AF,AF'          
2547: 01 04 01       LD      BC,$0104        
254A: 01 01 FF       LD      BC,$FF01        
254D: 00             NOP                     
254E: FB             EI                      
254F: 00             NOP                     
2550: F8             RET     M               
2551: 00             NOP                     
2552: F5             PUSH    AF              
2553: 00             NOP                     
2554: F2 00 EE       JP      P,$EE00         
2557: 00             NOP                     
2558: EB             EX      DE,HL           
2559: 00             NOP                     
255A: E8             RET     PE              
255B: 00             NOP                     
255C: E4 00 E1       CALL    PO,$E100        
255F: 00             NOP                     
2560: DE 00          SBC     $00             
2562: DA 00 D7       JP      C,$D700         
2565: 00             NOP                     
2566: D4 00 D1       CALL    NC,$D100        
2569: 00             NOP                     
256A: CD 00 CA       CALL    $CA00           
256D: 00             NOP                     
256E: C7             RST     0X00            
256F: 00             NOP                     
2570: C3 00 C0       JP      $C000           
2573: 00             NOP                     
2574: BC             CP      H               
2575: 00             NOP                     
2576: B8             CP      B               
2577: 00             NOP                     
2578: B5             OR      L               
2579: 00             NOP                     
257A: B1             OR      C               
257B: 00             NOP                     
257C: AC             XOR     H               
257D: 00             NOP                     
257E: A8             XOR     B               
257F: 00             NOP                     
2580: A5             AND     L               
2581: 00             NOP                     
2582: A0             AND     B               
2583: 00             NOP                     
2584: 9A             SBC     D               
2585: 00             NOP                     
2586: 94             SUB     H               
2587: 00             NOP                     
2588: 8F             ADC     A,A             
2589: 00             NOP                     
258A: 87             ADD     A,A             
258B: 00             NOP                     
258C: 84             ADD     A,H             
258D: 00             NOP                     
258E: 7D             LD      A,L             
258F: 00             NOP                     
2590: 76             HALT                    
2591: 00             NOP                     
2592: 70             LD      (HL),B          
2593: 00             NOP                     
2594: 69             LD      L,C             
2595: 00             NOP                     
2596: 61             LD      H,C             
2597: 00             NOP                     
2598: 5B             LD      E,E             
2599: 00             NOP                     
259A: 53             LD      D,E             
259B: 00             NOP                     
259C: 4B             LD      C,E             
259D: 00             NOP                     
259E: 44             LD      B,H             
259F: 00             NOP                     
25A0: 3B             DEC     SP              
25A1: 00             NOP                     
25A2: 33             INC     SP              
25A3: 00             NOP                     
25A4: 2C             INC     L               
25A5: 00             NOP                     
25A6: 23             INC     HL              
25A7: 00             NOP                     
25A8: 1A             LD      A,(DE)          
25A9: 00             NOP                     
25AA: 11 00 08       LD      DE,$0800        
25AD: 00             NOP                     
25AE: 00             NOP                     
25AF: 00             NOP                     
25B0: 00             NOP                     
25B1: 00             NOP                     
25B2: F8             RET     M               
25B3: FF             RST     0X38            
25B4: EF             RST     0X28            
25B5: FF             RST     0X38            
25B6: 00             NOP                     
25B7: 00             NOP                     
25B8: DD                                  
25B9: FF             RST     0X38            
25BA: D4 FF CD       CALL    NC,$CDFF        
25BD: FF             RST     0X38            
25BE: C5             PUSH    BC              
25BF: FF             RST     0X38            
25C0: BC             CP      H               
25C1: FF             RST     0X38            
25C2: B5             OR      L               
25C3: FF             RST     0X38            
25C4: AD             XOR     L               
25C5: FF             RST     0X38            
25C6: A5             AND     L               
25C7: FF             RST     0X38            
25C8: 9F             SBC     A               
25C9: FF             RST     0X38            
25CA: 97             SUB     A               
25CB: FF             RST     0X38            
25CC: 90             SUB     B               
25CD: FF             RST     0X38            
25CE: 8A             ADC     A,D             
25CF: FF             RST     0X38            
25D0: 83             ADD     A,E             
25D1: FF             RST     0X38            
25D2: 7C             LD      A,H             
25D3: FF             RST     0X38            
25D4: 79             LD      A,C             
25D5: FF             RST     0X38            
25D6: 7C             LD      A,H             
25D7: FF             RST     0X38            
25D8: 6C             LD      L,H             
25D9: FF             RST     0X38            
25DA: 66             LD      H,(HL)          
25DB: FF             RST     0X38            
25DC: 60             LD      H,B             
25DD: FF             RST     0X38            
25DE: 5B             LD      E,E             
25DF: FF             RST     0X38            
25E0: 58             LD      E,B             
25E1: FF             RST     0X38            
25E2: 54             LD      D,H             
25E3: FF             RST     0X38            
25E4: 4F             LD      C,A             
25E5: FF             RST     0X38            
25E6: 4B             LD      C,E             
25E7: FF             RST     0X38            
25E8: 48             LD      C,B             
25E9: FF             RST     0X38            
25EA: 44             LD      B,H             
25EB: FF             RST     0X38            
25EC: 40             LD      B,B             
25ED: FF             RST     0X38            
25EE: 3D             DEC     A               
25EF: FF             RST     0X38            
25F0: 39             ADD     HL,SP           
25F1: FF             RST     0X38            
25F2: 36 FF          LD      (HL),$FF        
25F4: 33             INC     SP              
25F5: FF             RST     0X38            
25F6: 33             INC     SP              
25F7: FF             RST     0X38            
25F8: 2C             INC     L               
25F9: FF             RST     0X38            
25FA: 29             ADD     HL,HL           
25FB: FF             RST     0X38            
25FC: 26 FF          LD      H,$FF           
25FE: 22 FF 1F       LD      ($1FFF),HL      
2601: FF             RST     0X38            
2602: 1C             INC     E               
2603: FF             RST     0X38            
2604: 18 FF          JR      $2605           
2606: 15             DEC     D               
2607: FF             RST     0X38            
2608: 12             LD      (DE),A          
2609: FF             RST     0X38            
260A: 0E FF          LD      C,$FF           
260C: 0B             DEC     BC              
260D: FF             RST     0X38            
260E: 08             EX      AF,AF'          
260F: FF             RST     0X38            
2610: 05             DEC     B               
2611: FF             RST     0X38            
2612: 01 FF FF       LD      BC,$FFFF        
2615: FE FC          CP      $FC             
2617: FE F8          CP      $F8             
2619: FE F6          CP      $F6             
261B: FE F4          CP      $F4             
261D: FE F2          CP      $F2             
261F: FE F0          CP      $F0             
2621: FE ED          CP      $ED             
2623: FE EC          CP      $EC             
2625: FE EB          CP      $EB             
2627: FE EA          CP      $EA             
2629: FE E9          CP      $E9             
262B: FE E8          CP      $E8             
262D: FE E7          CP      $E7             
262F: FE E7          CP      $E7             
2631: FE E8          CP      $E8             
2633: FE E9          CP      $E9             
2635: FE EA          CP      $EA             
2637: FE EB          CP      $EB             
2639: FE EC          CP      $EC             
263B: FE ED          CP      $ED             
263D: FE F0          CP      $F0             
263F: FE F2          CP      $F2             
2641: FE F4          CP      $F4             
2643: FE F6          CP      $F6             
2645: FE F8          CP      $F8             
2647: FE FC          CP      $FC             
2649: FE FF          CP      $FF             
264B: FE 01          CP      $01             
264D: FF             RST     0X38            
264E: 05             DEC     B               
264F: FF             RST     0X38            
2650: 08             EX      AF,AF'          
2651: FF             RST     0X38            
2652: 0B             DEC     BC              
2653: FF             RST     0X38            
2654: 0E FF          LD      C,$FF           
2656: 12             LD      (DE),A          
2657: FF             RST     0X38            
2658: 15             DEC     D               
2659: FF             RST     0X38            
265A: 18 FF          JR      $265B           
265C: 1C             INC     E               
265D: FF             RST     0X38            
265E: 1F             RRA                     
265F: FF             RST     0X38            
2660: 22 FF 26       LD      ($26FF),HL      
2663: FF             RST     0X38            
2664: 29             ADD     HL,HL           
2665: FF             RST     0X38            
2666: 2C             INC     L               
2667: FF             RST     0X38            
2668: 2F             CPL                     
2669: FF             RST     0X38            
266A: 33             INC     SP              
266B: FF             RST     0X38            
266C: 36 FF          LD      (HL),$FF        
266E: 39             ADD     HL,SP           
266F: FF             RST     0X38            
2670: 3D             DEC     A               
2671: FF             RST     0X38            
2672: 40             LD      B,B             
2673: FF             RST     0X38            
2674: 44             LD      B,H             
2675: FF             RST     0X38            
2676: 48             LD      C,B             
2677: FF             RST     0X38            
2678: 4B             LD      C,E             
2679: FF             RST     0X38            
267A: 4F             LD      C,A             
267B: FF             RST     0X38            
267C: 54             LD      D,H             
267D: FF             RST     0X38            
267E: 58             LD      E,B             
267F: FF             RST     0X38            
2680: 5B             LD      E,E             
2681: FF             RST     0X38            
2682: 60             LD      H,B             
2683: FF             RST     0X38            
2684: 66             LD      H,(HL)          
2685: FF             RST     0X38            
2686: 6C             LD      L,H             
2687: FF             RST     0X38            
2688: 71             LD      (HL),C          
2689: FF             RST     0X38            
268A: 79             LD      A,C             
268B: FF             RST     0X38            
268C: 7C             LD      A,H             
268D: FF             RST     0X38            
268E: 83             ADD     A,E             
268F: FF             RST     0X38            
2690: 8A             ADC     A,D             
2691: FF             RST     0X38            
2692: 90             SUB     B               
2693: FF             RST     0X38            
2694: 97             SUB     A               
2695: FF             RST     0X38            
2696: 9F             SBC     A               
2697: FF             RST     0X38            
2698: A5             AND     L               
2699: FF             RST     0X38            
269A: AD             XOR     L               
269B: FF             RST     0X38            
269C: B5             OR      L               
269D: FF             RST     0X38            
269E: BC             CP      H               
269F: FF             RST     0X38            
26A0: C5             PUSH    BC              
26A1: FF             RST     0X38            
26A2: CD FF D4       CALL    $D4FF           
26A5: FF             RST     0X38            
26A6: DD                                  
26A7: FF             RST     0X38            
26A8: E6 FF          AND     $FF             
26AA: EF             RST     0X28            
26AB: FF             RST     0X38            
26AC: F8             RET     M               
26AD: FF             RST     0X38            
26AE: 00             NOP                     
26AF: 00             NOP                     
26B0: 00             NOP                     
26B1: 00             NOP                     
26B2: 08             EX      AF,AF'          
26B3: 00             NOP                     
26B4: 11 00 1A       LD      DE,$1A00        
26B7: 00             NOP                     
26B8: 23             INC     HL              
26B9: 00             NOP                     
26BA: 2C             INC     L               
26BB: 00             NOP                     
26BC: 33             INC     SP              
26BD: 00             NOP                     
26BE: 3B             DEC     SP              
26BF: 00             NOP                     
26C0: 44             LD      B,H             
26C1: 00             NOP                     
26C2: 4B             LD      C,E             
26C3: 00             NOP                     
26C4: 53             LD      D,E             
26C5: 00             NOP                     
26C6: 5B             LD      E,E             
26C7: 00             NOP                     
26C8: 61             LD      H,C             
26C9: 00             NOP                     
26CA: 69             LD      L,C             
26CB: 00             NOP                     
26CC: 70             LD      (HL),B          
26CD: 00             NOP                     
26CE: 76             HALT                    
26CF: 00             NOP                     
26D0: 7D             LD      A,L             
26D1: 00             NOP                     
26D2: 84             ADD     A,H             
26D3: 00             NOP                     
26D4: 87             ADD     A,A             
26D5: 00             NOP                     
26D6: 87             ADD     A,A             
26D7: 00             NOP                     
26D8: 94             SUB     H               
26D9: 00             NOP                     
26DA: 9A             SBC     D               
26DB: 00             NOP                     
26DC: A0             AND     B               
26DD: 00             NOP                     
26DE: A5             AND     L               
26DF: 00             NOP                     
26E0: A8             XOR     B               
26E1: 00             NOP                     
26E2: AC             XOR     H               
26E3: 00             NOP                     
26E4: B1             OR      C               
26E5: 00             NOP                     
26E6: B5             OR      L               
26E7: 00             NOP                     
26E8: B8             CP      B               
26E9: 00             NOP                     
26EA: BC             CP      H               
26EB: 00             NOP                     
26EC: C0             RET     NZ              
26ED: 00             NOP                     
26EE: C3 00 C7       JP      $C700           
26F1: 00             NOP                     
26F2: CA 00 CD       JP      Z,$CD00         
26F5: 00             NOP                     
26F6: CA 00 D4       JP      Z,$D400         
26F9: 00             NOP                     
26FA: D7             RST     0X10            
26FB: 00             NOP                     
26FC: DA 00 DE       JP      C,$DE00         
26FF: 00             NOP                     
2700: E1             POP     HL              
2701: 00             NOP                     
2702: E4 00 E8       CALL    PO,$E800        
2705: 00             NOP                     
2706: EB             EX      DE,HL           
2707: 00             NOP                     
2708: EE 00          XOR     $00             
270A: F2 00 F5       JP      P,$F500         
270D: 00             NOP                     
270E: F8             RET     M               
270F: 00             NOP                     
2710: FB             EI                      
2711: 00             NOP                     
2712: FF             RST     0X38            
2713: 00             NOP                     
2714: 01 01 FB       LD      BC,$FB01        
2717: 00             NOP                     
2718: 08             EX      AF,AF'          
2719: 01 0A 01       LD      BC,$010A        
271C: 0C             INC     C               
271D: 01 0E 01       LD      BC,$010E        
2720: 10 01          DJNZ    $2723           
2722: 13             INC     DE              
2723: 01 14 01       LD      BC,$0114        
2726: 15             DEC     D               
2727: 01 16 01       LD      BC,$0116        
272A: 17             RLA                     
272B: 01 18 01       LD      BC,$0118        
272E: 19             ADD     HL,DE           
272F: 01 3A 6F       LD      BC,$6F3A        
2732: AA             XOR     D               
2733: FE 76          CP      $76             
2735: C2 30 25       JP      NZ,$2530        
2738: CD 2B 0B       CALL    $0B2B           
273B: CD 0E 21       CALL    $210E           
273E: AF             XOR     A               
273F: 32 31 AD       LD      ($AD31),A       
2742: 32 20 AD       LD      ($AD20),A       
2745: 32 30 AD       LD      ($AD30),A       
2748: 32 AC A9       LD      ($A9AC),A       
274B: 3C             INC     A               
274C: 32 10 AD       LD      ($AD10),A       
274F: 3E 03          LD      A,$03           
2751: 32 AB A9       LD      ($A9AB),A       
2754: C9             RET                     
2755: DD 21 80 AA    LD      IX,$AA80        
2759: 21 6E 27       LD      HL,$276E        
275C: 3A 61 08       LD      A,($0861)       
275F: 5F             LD      E,A             
2760: 3A 01 5C       LD      A,($5C01)       
2763: 57             LD      D,A             
2764: 06 06          LD      B,$06           
2766: DD 77 00       LD      (IX+$00),A      
2769: DD 77 04       LD      (IX+$04),A      
276C: DD 19          ADD     IX,DE           
276E: 10 F6          DJNZ    $2766           
2770: C9             RET                     
2771: 7E             LD      A,(HL)          
2772: 84             ADD     A,H             
2773: 7E             LD      A,(HL)          
2774: 85             ADD     A,L             
2775: 7E             LD      A,(HL)          
2776: 86             ADD     A,(HL)          
2777: 7D             LD      A,L             
2778: 87             ADD     A,A             
2779: 7C             LD      A,H             
277A: 88             ADC     A,B             
277B: 7B             LD      A,E             
277C: 89             ADC     A,C             
277D: 7A             LD      A,D             
277E: 8A             ADC     A,D             
277F: 79             LD      A,C             
2780: 8A             ADC     A,D             
2781: 78             LD      A,B             
2782: 8A             ADC     A,D             
2783: 77             LD      (HL),A          
2784: 8A             ADC     A,D             
2785: 76             HALT                    
2786: 8A             ADC     A,D             
2787: 75             LD      (HL),L          
2788: 89             ADC     A,C             
2789: 74             LD      (HL),H          
278A: 88             ADC     A,B             
278B: 73             LD      (HL),E          
278C: 87             ADD     A,A             
278D: 72             LD      (HL),D          
278E: 86             ADD     A,(HL)          
278F: 72             LD      (HL),D          
2790: 85             ADD     A,L             
2791: 72             LD      (HL),D          
2792: 84             ADD     A,H             
2793: 72             LD      (HL),D          
2794: 83             ADD     A,E             
2795: 72             LD      (HL),D          
2796: 82             ADD     A,D             
2797: 73             LD      (HL),E          
2798: 81             ADD     A,C             
2799: 74             LD      (HL),H          
279A: 80             ADD     A,B             
279B: 75             LD      (HL),L          
279C: 7F             LD      A,A             
279D: 76             HALT                    
279E: 7E             LD      A,(HL)          
279F: 77             LD      (HL),A          
27A0: 7E             LD      A,(HL)          
27A1: 78             LD      A,B             
27A2: 7E             LD      A,(HL)          
27A3: 79             LD      A,C             
27A4: 7E             LD      A,(HL)          
27A5: 7A             LD      A,D             
27A6: 7E             LD      A,(HL)          
27A7: 7B             LD      A,E             
27A8: 7F             LD      A,A             
27A9: 7C             LD      A,H             
27AA: 80             ADD     A,B             
27AB: 7D             LD      A,L             
27AC: 81             ADD     A,C             
27AD: 7E             LD      A,(HL)          
27AE: 82             ADD     A,D             
27AF: 7E             LD      A,(HL)          
27B0: 83             ADD     A,E             
27B1: CD 34 58       CALL    $5834           
27B4: 3E 78          LD      A,$78           
27B6: 32 64 AC       LD      ($AC64),A       
27B9: 3E 84          LD      A,$84           
27BB: 32 65 AC       LD      ($AC65),A       
27BE: 21 00 00       LD      HL,$0000        
27C1: 22 16 AD       LD      ($AD16),HL      
27C4: 22 26 AD       LD      ($AD26),HL      
27C7: 3A CD A9       LD      A,($A9CD)       
27CA: 32 12 AD       LD      ($AD12),A       
27CD: 32 22 AD       LD      ($AD22),A       
27D0: AF             XOR     A               
27D1: 32 14 AD       LD      ($AD14),A       
27D4: 32 24 AD       LD      ($AD24),A       
27D7: 32 32 AD       LD      ($AD32),A       
27DA: 32 13 AD       LD      ($AD13),A       
27DD: 32 23 AD       LD      ($AD23),A       
27E0: 32 1D AD       LD      ($AD1D),A       
27E3: 32 2D AD       LD      ($AD2D),A       
27E6: 32 0C AD       LD      ($AD0C),A       
27E9: 3C             INC     A               
27EA: 32 11 AD       LD      ($AD11),A       
27ED: 32 21 AD       LD      ($AD21),A       
27F0: 32 1E AD       LD      ($AD1E),A       
27F3: 32 2E AD       LD      ($AD2E),A       
27F6: 3A 30 AD       LD      A,($AD30)       
27F9: A7             AND     A               
27FA: 28 39          JR      Z,$2835         
27FC: AF             XOR     A               
27FD: 67             LD      H,A             
27FE: 6F             LD      L,A             
27FF: 32 33 AD       LD      ($AD33),A       
2802: 22 34 AD       LD      ($AD34),HL      
2805: 32 36 AD       LD      ($AD36),A       
2808: 22 37 AD       LD      ($AD37),HL      
280B: 11 00 04       LD      DE,$0400        
280E: FF             RST     0X38            
280F: 3A C4 A9       LD      A,($A9C4)       
2812: CD 7B 0F       CALL    $0F7B           
2815: 06 00          LD      B,$00           
2817: 21 50 15       LD      HL,$1550        
281A: 97             SUB     A               
281B: AE             XOR     (HL)            
281C: 23             INC     HL              
281D: 10 FC          DJNZ    $281B           
281F: C6 01          ADD     $01             
2821: 32 08 C3       LD      ($C308),A       
2824: 3A D3 A9       LD      A,($A9D3)       
2827: 32 1A AD       LD      ($AD1A),A       
282A: 32 2A AD       LD      ($AD2A),A       
282D: 3E 96          LD      A,$96           
282F: 32 EB A9       LD      ($A9EB),A       
2832: C3 1A 0F       JP      $0F1A           
2835: 21 D0 A9       LD      HL,$A9D0        
2838: 7E             LD      A,(HL)          
2839: 3C             INC     A               
283A: FE 04          CP      $04             
283C: 38 02          JR      C,$2840         
283E: 3E 01          LD      A,$01           
2840: 77             LD      (HL),A          
2841: 32 14 AD       LD      ($AD14),A       
2844: 3C             INC     A               
2845: 32 11 AD       LD      ($AD11),A       
2848: AF             XOR     A               
2849: 32 80 A9       LD      ($A980),A       
284C: 32 CE A9       LD      ($A9CE),A       
284F: 32 CF A9       LD      ($A9CF),A       
2852: CD 67 4B       CALL    $4B67           
2855: 21 80 AA       LD      HL,$AA80        
2858: 11 81 AA       LD      DE,$AA81        
285B: 36 00          LD      (HL),$00        
285D: 01 5F 00       LD      BC,$005F        
2860: ED B0          LDIR                    
2862: 21 00 A8       LD      HL,$A800        
2865: 11 01 A8       LD      DE,$A801        
2868: 36 00          LD      (HL),$00        
286A: 01 7F 01       LD      BC,$017F        
286D: ED B0          LDIR                    
286F: 3E 02          LD      A,$02           
2871: CD 7B 0F       CALL    $0F7B           
2874: 3A D3 A9       LD      A,($A9D3)       
2877: 32 1A AD       LD      ($AD1A),A       
287A: 32 2A AD       LD      ($AD2A),A       
287D: 0E 00          LD      C,$00           
287F: 21 10 33       LD      HL,$3310        
2882: 3A AB A9       LD      A,($A9AB)       
2885: 96             SUB     (HL)            
2886: 23             INC     HL              
2887: 0D             DEC     C               
2888: 20 FB          JR      NZ,$2885        
288A: EE 90          XOR     $90             
288C: 32 AB A9       LD      ($A9AB),A       
288F: 21 74 AC       LD      HL,$AC74        
2892: 06 10          LD      B,$10           
2894: 36 80          LD      (HL),$80        
2896: 23             INC     HL              
2897: 10 FB          DJNZ    $2894           
2899: 3E 5A          LD      A,$5A           
289B: 32 EB A9       LD      ($A9EB),A       
289E: C3 1A 0F       JP      $0F1A           
28A1: CD B7 28       CALL    $28B7           
28A4: CD C2 28       CALL    $28C2           
28A7: CD CD 28       CALL    $28CD           
28AA: CD D8 28       CALL    $28D8           
28AD: CD E3 28       CALL    $28E3           
28B0: CD EE 28       CALL    $28EE           
28B3: CD FE 28       CALL    $28FE           
28B6: C9             RET                     
28B7: DD 21 50 A8    LD      IX,$A850        
28BB: FD 21 1A AA    LD      IY,$AA1A        
28BF: C3 0E 29       JP      $290E           
28C2: DD 21 60 A8    LD      IX,$A860        
28C6: FD 21 1C AA    LD      IY,$AA1C        
28CA: C3 0E 29       JP      $290E           
28CD: DD 21 70 A8    LD      IX,$A870        
28D1: FD 21 1E AA    LD      IY,$AA1E        
28D5: C3 0E 29       JP      $290E           
28D8: DD 21 80 A8    LD      IX,$A880        
28DC: FD 21 20 AA    LD      IY,$AA20        
28E0: C3 0E 29       JP      $290E           
28E3: DD 21 90 A8    LD      IX,$A890        
28E7: FD 21 22 AA    LD      IY,$AA22        
28EB: C3 0E 29       JP      $290E           
28EE: 3A 0D AD       LD      A,($AD0D)       
28F1: A7             AND     A               
28F2: C0             RET     NZ              
28F3: DD 21 A0 A8    LD      IX,$A8A0        
28F7: FD 21 24 AA    LD      IY,$AA24        
28FB: C3 0E 29       JP      $290E           
28FE: 3A 0D AD       LD      A,($AD0D)       
2901: A7             AND     A               
2902: C0             RET     NZ              
2903: DD 21 B0 A8    LD      IX,$A8B0        
2907: FD 21 26 AA    LD      IY,$AA26        
290B: C3 0E 29       JP      $290E           
290E: 3A 04 AD       LD      A,($AD04)       
2911: E6 07          AND     $07             
2913: F7             RST     0X30            
2914: 27             DAA                     
2915: 29             ADD     HL,HL           
2916: 4C             LD      C,H             
2917: 29             ADD     HL,HL           
2918: 84             ADD     A,H             
2919: 29             ADD     HL,HL           
291A: B0             OR      B               
291B: 29             ADD     HL,HL           
291C: D5             PUSH    DE              
291D: 29             ADD     HL,HL           
291E: 86             ADD     A,(HL)          
291F: EB             EX      DE,HL           
2920: 4E             LD      C,(HL)          
2921: EB             EX      DE,HL           
2922: 23             INC     HL              
2923: 13             INC     DE              
2924: 10 F8          DJNZ    $291E           
2926: C9             RET                     
2927: DD 7E 00       LD      A,(IX+$00)      
292A: A7             AND     A               
292B: C8             RET     Z               
292C: 3C             INC     A               
292D: 28 07          JR      Z,$2936         
292F: 3C             INC     A               
2930: CA 52 2B       JP      Z,$2B52         
2933: C3 93 2B       JP      $2B93           
2936: CD EF 2B       CALL    $2BEF           
2939: CD 40 58       CALL    $5840           
293C: CD 83 2B       CALL    $2B83           
293F: DA DE 2B       JP      C,$2BDE         
2942: CD D6 3E       CALL    $3ED6           
2945: CD 3C 2A       CALL    $2A3C           
2948: CD 43 42       CALL    $4243           
294B: C9             RET                     
294C: DD 7E 00       LD      A,(IX+$00)      
294F: A7             AND     A               
2950: C8             RET     Z               
2951: 3C             INC     A               
2952: 28 07          JR      Z,$295B         
2954: 3C             INC     A               
2955: CA 52 2B       JP      Z,$2B52         
2958: C3 93 2B       JP      $2B93           
295B: CD EF 2B       CALL    $2BEF           
295E: CD 54 58       CALL    $5854           
2961: CD 83 2B       CALL    $2B83           
2964: DA DE 2B       JP      C,$2BDE         
2967: CD D6 3E       CALL    $3ED6           
296A: CD 47 2A       CALL    $2A47           
296D: C9             RET                     
296E: 09             ADD     HL,BC           
296F: A7             AND     A               
2970: 32 82 6E       LD      ($6E82),A       
2973: 58             LD      E,B             
2974: B5             OR      L               
2975: 77             LD      (HL),A          
2976: E4 E8 EC       CALL    PO,$ECE8        
2979: 9D             SBC     L               
297A: CB 4F          BIT     1,A             
297C: 55             LD      D,L             
297D: FE A3          CP      $A3             
297F: 31 81 5B       LD      SP,$5B81        
2982: 9A             SBC     D               
2983: B9             CP      C               
2984: DD 7E 00       LD      A,(IX+$00)      
2987: A7             AND     A               
2988: C8             RET     Z               
2989: 3C             INC     A               
298A: 28 07          JR      Z,$2993         
298C: 3C             INC     A               
298D: CA 52 2B       JP      Z,$2B52         
2990: C3 93 2B       JP      $2B93           
2993: 3A 80 A9       LD      A,($A980)       
2996: E6 03          AND     $03             
2998: FE 03          CP      $03             
299A: DC EF 2B       CALL    C,$2BEF         
299D: CD 40 58       CALL    $5840           
29A0: CD 83 2B       CALL    $2B83           
29A3: DA DE 2B       JP      C,$2BDE         
29A6: CD D6 3E       CALL    $3ED6           
29A9: CD 97 2A       CALL    $2A97           
29AC: CD 43 42       CALL    $4243           
29AF: C9             RET                     
29B0: DD 7E 00       LD      A,(IX+$00)      
29B3: A7             AND     A               
29B4: C8             RET     Z               
29B5: 3C             INC     A               
29B6: 28 07          JR      Z,$29BF         
29B8: 3C             INC     A               
29B9: CA 52 2B       JP      Z,$2B52         
29BC: C3 93 2B       JP      $2B93           
29BF: CD EF 2B       CALL    $2BEF           
29C2: CD A4 58       CALL    $58A4           
29C5: CD 83 2B       CALL    $2B83           
29C8: DA DE 2B       JP      C,$2BDE         
29CB: CD D6 3E       CALL    $3ED6           
29CE: CD FC 2A       CALL    $2AFC           
29D1: CD 43 42       CALL    $4243           
29D4: C9             RET                     
29D5: DD 7E 00       LD      A,(IX+$00)      
29D8: A7             AND     A               
29D9: C8             RET     Z               
29DA: 3C             INC     A               
29DB: 28 07          JR      Z,$29E4         
29DD: 3C             INC     A               
29DE: CA 52 2B       JP      Z,$2B52         
29E1: C3 93 2B       JP      $2B93           
29E4: CD F7 29       CALL    $29F7           
29E7: CD 83 2B       CALL    $2B83           
29EA: DA DE 2B       JP      C,$2BDE         
29ED: CD 38 2B       CALL    $2B38           
29F0: CD D6 3E       CALL    $3ED6           
29F3: CD 43 42       CALL    $4243           
29F6: C9             RET                     
29F7: 3E 78          LD      A,$78           
29F9: FD 96 31       SUB     (IY+$31)        
29FC: C6 48          ADD     $48             
29FE: FE 90          CP      $90             
2A00: 38 1A          JR      C,$2A1C         
2A02: 3E 84          LD      A,$84           
2A04: FD 96 31       SUB     (IY+$31)        
2A07: C6 48          ADD     $48             
2A09: FE 90          CP      $90             
2A0B: 38 0F          JR      C,$2A1C         
2A0D: CD EF 2B       CALL    $2BEF           
2A10: 3A 80 A9       LD      A,($A980)       
2A13: 0F             RRCA                    
2A14: E6 01          AND     $01             
2A16: CA AA 58       JP      Z,$58AA         
2A19: C3 60 58       JP      $5860           
2A1C: AF             XOR     A               
2A1D: 32 04 AD       LD      ($AD04),A       
2A20: CD EF 2B       CALL    $2BEF           
2A23: 3E 04          LD      A,$04           
2A25: 32 04 AD       LD      ($AD04),A       
2A28: 18 E6          JR      $2A10           
2A2A: DD 7E 04       LD      A,(IX+$04)      
2A2D: 3D             DEC     A               
2A2E: CA 93 2B       JP      Z,$2B93         
2A31: DD 77 04       LD      (IX+$04),A      
2A34: DD 36 00 FF    LD      (IX+$00),$FF    
2A38: CD BA 2B       CALL    $2BBA           
2A3B: C9             RET                     
2A3C: CD 57 2A       CALL    $2A57           
2A3F: FD 71 30       LD      (IY+$30),C      
2A42: 78             LD      A,B             
2A43: FD 77 01       LD      (IY+$01),A      
2A46: C9             RET                     
2A47: CD 57 2A       CALL    $2A57           
2A4A: 79             LD      A,C             
2A4B: C6 35          ADD     $35             
2A4D: FD 77 30       LD      (IY+$30),A      
2A50: 78             LD      A,B             
2A51: C6 10          ADD     $10             
2A53: FD 77 01       LD      (IY+$01),A      
2A56: C9             RET                     
2A57: 11 10 00       LD      DE,$0010        
2A5A: DD 7E 02       LD      A,(IX+$02)      
2A5D: C6 08          ADD     $08             
2A5F: 0F             RRCA                    
2A60: 0F             RRCA                    
2A61: 0F             RRCA                    
2A62: 0F             RRCA                    
2A63: E6 0F          AND     $0F             
2A65: 21 77 2A       LD      HL,$2A77        
2A68: DF             RST     0X18            
2A69: 46             LD      B,(HL)          
2A6A: 19             ADD     HL,DE           
2A6B: 4E             LD      C,(HL)          
2A6C: 3A 80 A9       LD      A,($A980)       
2A6F: CB 4F          BIT     1,A             
2A71: C8             RET     Z               
2A72: 78             LD      A,B             
2A73: C6 08          ADD     $08             
2A75: 47             LD      B,A             
2A76: C9             RET                     
2A77: 0C             INC     C               
2A78: 0D             DEC     C               
2A79: 0E 0F          LD      C,$0F           
2A7B: 08             EX      AF,AF'          
2A7C: 0F             RRCA                    
2A7D: 0E 0D          LD      C,$0D           
2A7F: 0C             INC     C               
2A80: 0B             DEC     BC              
2A81: 0A             LD      A,(BC)          
2A82: 09             ADD     HL,BC           
2A83: 08             EX      AF,AF'          
2A84: 09             ADD     HL,BC           
2A85: 0A             LD      A,(BC)          
2A86: 0B             DEC     BC              
2A87: 41             LD      B,C             
2A88: 41             LD      B,C             
2A89: 41             LD      B,C             
2A8A: 41             LD      B,C             
2A8B: 81             ADD     A,C             
2A8C: C1             POP     BC              
2A8D: C1             POP     BC              
2A8E: C1             POP     BC              
2A8F: C1             POP     BC              
2A90: C1             POP     BC              
2A91: C1             POP     BC              
2A92: C1             POP     BC              
2A93: 41             LD      B,C             
2A94: 41             LD      B,C             
2A95: 41             LD      B,C             
2A96: 41             LD      B,C             
2A97: DD 7E 02       LD      A,(IX+$02)      
2A9A: C6 04          ADD     $04             
2A9C: E6 F8          AND     $F8             
2A9E: 0F             RRCA                    
2A9F: 0F             RRCA                    
2AA0: E6 3F          AND     $3F             
2AA2: 21 BC 2A       LD      HL,$2ABC        
2AA5: DF             RST     0X18            
2AA6: 46             LD      B,(HL)          
2AA7: 3A 80 A9       LD      A,($A980)       
2AAA: E6 02          AND     $02             
2AAC: 20 0A          JR      NZ,$2AB8        
2AAE: 80             ADD     A,B             
2AAF: FD 77 01       LD      (IY+$01),A      
2AB2: 23             INC     HL              
2AB3: 7E             LD      A,(HL)          
2AB4: FD 77 30       LD      (IY+$30),A      
2AB7: C9             RET                     
2AB8: 3E 08          LD      A,$08           
2ABA: 18 F2          JR      $2AAE           
2ABC: 80             ADD     A,B             
2ABD: DC 80 DC       CALL    C,$DC80         
2AC0: 80             ADD     A,B             
2AC1: DC 80 DC       CALL    C,$DC80         
2AC4: 81             ADD     A,C             
2AC5: DC 81 DC       CALL    C,$DC81         
2AC8: 82             ADD     A,D             
2AC9: DC 83 DC       CALL    C,$DC83         
2ACC: 84             ADD     A,H             
2ACD: 5C             LD      E,H             
2ACE: 84             ADD     A,H             
2ACF: 5C             LD      E,H             
2AD0: 83             ADD     A,E             
2AD1: 5C             LD      E,H             
2AD2: 82             ADD     A,D             
2AD3: 5C             LD      E,H             
2AD4: 81             ADD     A,C             
2AD5: 5C             LD      E,H             
2AD6: 81             ADD     A,C             
2AD7: 5C             LD      E,H             
2AD8: 80             ADD     A,B             
2AD9: 5C             LD      E,H             
2ADA: 80             ADD     A,B             
2ADB: 5C             LD      E,H             
2ADC: 80             ADD     A,B             
2ADD: 5C             LD      E,H             
2ADE: 80             ADD     A,B             
2ADF: 5C             LD      E,H             
2AE0: 80             ADD     A,B             
2AE1: 5C             LD      E,H             
2AE2: 80             ADD     A,B             
2AE3: 5C             LD      E,H             
2AE4: 81             ADD     A,C             
2AE5: 5C             LD      E,H             
2AE6: 81             ADD     A,C             
2AE7: 5C             LD      E,H             
2AE8: 82             ADD     A,D             
2AE9: 5C             LD      E,H             
2AEA: 83             ADD     A,E             
2AEB: 5C             LD      E,H             
2AEC: 84             ADD     A,H             
2AED: DC 84 DC       CALL    C,$DC84         
2AF0: 83             ADD     A,E             
2AF1: DC 82 DC       CALL    C,$DC82         
2AF4: 81             ADD     A,C             
2AF5: DC 81 DC       CALL    C,$DC81         
2AF8: 80             ADD     A,B             
2AF9: DC 80 DC       CALL    C,$DC80         
2AFC: 11 10 00       LD      DE,$0010        
2AFF: DD 7E 02       LD      A,(IX+$02)      
2B02: C6 08          ADD     $08             
2B04: 0F             RRCA                    
2B05: 0F             RRCA                    
2B06: 0F             RRCA                    
2B07: 0F             RRCA                    
2B08: E6 0F          AND     $0F             
2B0A: 21 18 2B       LD      HL,$2B18        
2B0D: DF             RST     0X18            
2B0E: 7E             LD      A,(HL)          
2B0F: FD 77 01       LD      (IY+$01),A      
2B12: 19             ADD     HL,DE           
2B13: 7E             LD      A,(HL)          
2B14: FD 77 30       LD      (IY+$30),A      
2B17: C9             RET                     
2B18: 2C             INC     L               
2B19: 2D             DEC     L               
2B1A: 2E 2F          LD      L,$2F           
2B1C: 28 2F          JR      Z,$2B4D         
2B1E: 2E 2D          LD      L,$2D           
2B20: 2C             INC     L               
2B21: 2B             DEC     HL              
2B22: 2A 29 28       LD      HL,($2829)      
2B25: 29             ADD     HL,HL           
2B26: 2A 2B 5B       LD      HL,($5B2B)      
2B29: 5B             LD      E,E             
2B2A: 5B             LD      E,E             
2B2B: 5B             LD      E,E             
2B2C: 9B             SBC     E               
2B2D: DB DB          IN      A,($DB)         
2B2F: DB DB          IN      A,($DB)         
2B31: DB DB          IN      A,($DB)         
2B33: DB 5B          IN      A,($5B)         
2B35: 5B             LD      E,E             
2B36: 5B             LD      E,E             
2B37: 5B             LD      E,E             
2B38: 3A 80 A9       LD      A,($A980)       
2B3B: 0F             RRCA                    
2B3C: 0F             RRCA                    
2B3D: E6 03          AND     $03             
2B3F: C6 D8          ADD     $D8             
2B41: 47             LD      B,A             
2B42: DD 7E 04       LD      A,(IX+$04)      
2B45: D6 01          SUB     $01             
2B47: 87             ADD     A,A             
2B48: 87             ADD     A,A             
2B49: 80             ADD     A,B             
2B4A: FD 77 01       LD      (IY+$01),A      
2B4D: FD 36 30 61    LD      (IY+$30),$61    
2B51: C9             RET                     
2B52: DD 35 0E       DEC     (IX+$0E)        
2B55: 28 01          JR      Z,$2B58         
2B57: C9             RET                     
2B58: DD 34 00       INC     (IX+$00)        
2B5B: DD 36 0E 80    LD      (IX+$0E),$80    
2B5F: C9             RET                     
2B60: FD 66 31       LD      H,(IY+$31)      
2B63: DD 6E 03       LD      L,(IX+$03)      
2B66: ED 5B 08 A8    LD      DE,($A808)      
2B6A: 19             ADD     HL,DE           
2B6B: FD 74 31       LD      (IY+$31),H      
2B6E: DD 75 03       LD      (IX+$03),L      
2B71: FD 66 00       LD      H,(IY+$00)      
2B74: DD 6E 05       LD      L,(IX+$05)      
2B77: ED 5B 0A A8    LD      DE,($A80A)      
2B7B: 19             ADD     HL,DE           
2B7C: FD 74 00       LD      (IY+$00),H      
2B7F: DD 75 05       LD      (IX+$05),L      
2B82: C9             RET                     
2B83: FD 7E 31       LD      A,(IY+$31)      
2B86: C6 09          ADD     $09             
2B88: FE 03          CP      $03             
2B8A: D8             RET     C               
2B8B: FD 7E 00       LD      A,(IY+$00)      
2B8E: D6 03          SUB     $03             
2B90: FE 03          CP      $03             
2B92: C9             RET                     
2B93: DD 7E 00       LD      A,(IX+$00)      
2B96: FE F0          CP      $F0             
2B98: CA AC 2B       JP      Z,$2BAC         
2B9B: FE 3C          CP      $3C             
2B9D: CC BA 2B       CALL    Z,$2BBA         
2BA0: D2 B4 2B       JP      NC,$2BB4        
2BA3: DD 35 00       DEC     (IX+$00)        
2BA6: 28 36          JR      Z,$2BDE         
2BA8: CD 22 2C       CALL    $2C22           
2BAB: C9             RET                     
2BAC: DD 36 00 3B    LD      (IX+$00),$3B    
2BB0: CD BA 2B       CALL    $2BBA           
2BB3: C9             RET                     
2BB4: DD 35 00       DEC     (IX+$00)        
2BB7: C3 40 58       JP      $5840           
2BBA: CD 83 56       CALL    $5683           
2BBD: 21 02 AD       LD      HL,$AD02        
2BC0: 7E             LD      A,(HL)          
2BC1: A7             AND     A               
2BC2: 28 01          JR      Z,$2BC5         
2BC4: 35             DEC     (HL)            
2BC5: DD 7E 0E       LD      A,(IX+$0E)      
2BC8: CB 7F          BIT     7,A             
2BCA: C8             RET     Z               
2BCB: 3A 12 A8       LD      A,($A812)       
2BCE: A7             AND     A               
2BCF: C8             RET     Z               
2BD0: 21 11 A8       LD      HL,$A811        
2BD3: 35             DEC     (HL)            
2BD4: C0             RET     NZ              
2BD5: DD 7E 0F       LD      A,(IX+$0F)      
2BD8: C6 80          ADD     $80             
2BDA: 32 21 A8       LD      ($A821),A       
2BDD: C9             RET                     
2BDE: AF             XOR     A               
2BDF: DD 77 00       LD      (IX+$00),A      
2BE2: DD 77 03       LD      (IX+$03),A      
2BE5: DD 77 05       LD      (IX+$05),A      
2BE8: FD 77 00       LD      (IY+$00),A      
2BEB: FD 77 31       LD      (IY+$31),A      
2BEE: C9             RET                     
2BEF: DD 7E 01       LD      A,(IX+$01)      
2BF2: DD 96 02       SUB     (IX+$02)        
2BF5: 4F             LD      C,A             
2BF6: C6 02          ADD     $02             
2BF8: FE 04          CP      $04             
2BFA: D8             RET     C               
2BFB: DD 46 02       LD      B,(IX+$02)      
2BFE: 79             LD      A,C             
2BFF: FE 80          CP      $80             
2C01: 30 0C          JR      NC,$2C0F        
2C03: 21 1D 2C       LD      HL,$2C1D        
2C06: 3A 04 AD       LD      A,($AD04)       
2C09: CF             RST     0X08            
2C0A: 80             ADD     A,B             
2C0B: DD 77 02       LD      (IX+$02),A      
2C0E: C9             RET                     
2C0F: 21 1D 2C       LD      HL,$2C1D        
2C12: 3A 04 AD       LD      A,($AD04)       
2C15: CF             RST     0X08            
2C16: 90             SUB     B               
2C17: ED 44          NEG                     
2C19: DD 77 02       LD      (IX+$02),A      
2C1C: C9             RET                     
2C1D: 01 01 02       LD      BC,$0201        
2C20: 02             LD      (BC),A          
2C21: 05             DEC     B               
2C22: 21 31 2C       LD      HL,$2C31        
2C25: E5             PUSH    HL              
2C26: DD 7E 00       LD      A,(IX+$00)      
2C29: FE 20          CP      $20             
2C2B: D2 B4 2B       JP      NC,$2BB4        
2C2E: C3 60 2B       JP      $2B60           
2C31: DD 7E 00       LD      A,(IX+$00)      
2C34: FE 2A          CP      $2A             
2C36: D2 71 2C       JP      NC,$2C71        
2C39: FE 0A          CP      $0A             
2C3B: 30 45          JR      NC,$2C82        
2C3D: 3A 21 A8       LD      A,($A821)       
2C40: CB 7F          BIT     7,A             
2C42: CA DE 2B       JP      Z,$2BDE         
2C45: 3A 21 A8       LD      A,($A821)       
2C48: CB BF          RES     7,A             
2C4A: DD BE 0F       CP      (IX+$0F)        
2C4D: C2 DE 2B       JP      NZ,$2BDE        
2C50: 3A 80 A9       LD      A,($A980)       
2C53: E6 07          AND     $07             
2C55: 28 03          JR      Z,$2C5A         
2C57: DD 34 00       INC     (IX+$00)        
2C5A: FD 36 01 FC    LD      (IY+$01),$FC    
2C5E: FD 36 30 6C    LD      (IY+$30),$6C    
2C62: DD 7E 00       LD      A,(IX+$00)      
2C65: FE 01          CP      $01             
2C67: C0             RET     NZ              
2C68: 11 0C 04       LD      DE,$040C        
2C6B: FF             RST     0X38            
2C6C: AF             XOR     A               
2C6D: 32 21 A8       LD      ($A821),A       
2C70: C9             RET                     
2C71: FD 7E 30       LD      A,(IY+$30)      
2C74: 4F             LD      C,A             
2C75: E6 C0          AND     $C0             
2C77: 47             LD      B,A             
2C78: 3A 80 A9       LD      A,($A980)       
2C7B: E6 0F          AND     $0F             
2C7D: 80             ADD     A,B             
2C7E: FD 77 30       LD      (IY+$30),A      
2C81: C9             RET                     
2C82: D6 0A          SUB     $0A             
2C84: 0F             RRCA                    
2C85: E6 0F          AND     $0F             
2C87: 47             LD      B,A             
2C88: 21 94 2C       LD      HL,$2C94        
2C8B: CF             RST     0X08            
2C8C: FD 77 01       LD      (IY+$01),A      
2C8F: FD 36 30 3C    LD      (IY+$30),$3C    
2C93: C9             RET                     
2C94: FF             RST     0X38            
2C95: FF             RST     0X38            
2C96: 7D             LD      A,L             
2C97: 7D             LD      A,L             
2C98: 7E             LD      A,(HL)          
2C99: 7E             LD      A,(HL)          
2C9A: 7D             LD      A,L             
2C9B: 7D             LD      A,L             
2C9C: 5B             LD      E,E             
2C9D: 5B             LD      E,E             
2C9E: 5A             LD      E,D             
2C9F: 5A             LD      E,D             
2CA0: 59             LD      E,C             
2CA1: 59             LD      E,C             
2CA2: 58             LD      E,B             
2CA3: 58             LD      E,B             
2CA4: 18 A7          JR      $2C4D           
2CA6: 13             INC     DE              
2CA7: A5             AND     L               
2CA8: 3B             DEC     SP              
2CA9: 87             ADD     A,A             
2CAA: F1             POP     AF              
2CAB: 34             INC     (HL)            
2CAC: 0E 34          LD      C,$34           
2CAE: D7             RST     0X10            
2CAF: BF             CP      A               
2CB0: F1             POP     AF              
2CB1: 65             LD      H,L             
2CB2: 13             INC     DE              
2CB3: 13             INC     DE              
2CB4: 13             INC     DE              
2CB5: 13             INC     DE              
2CB6: F1             POP     AF              
2CB7: 88             ADC     A,B             
2CB8: DC ED 11       CALL    C,$11ED         
2CBB: B9             CP      C               
2CBC: DD 21 00 A9    LD      IX,$A900        
2CC0: FD 21 30 AA    LD      IY,$AA30        
2CC4: 3A 04 AD       LD      A,($AD04)       
2CC7: A7             AND     A               
2CC8: 28 2B          JR      Z,$2CF5         
2CCA: FE 04          CP      $04             
2CCC: 28 34          JR      Z,$2D02         
2CCE: CD 21 2D       CALL    $2D21           
2CD1: CD 36 2D       CALL    $2D36           
2CD4: CD 36 2D       CALL    $2D36           
2CD7: CD 68 2D       CALL    $2D68           
2CDA: C9             RET                     
2CDB: CD C2 01       CALL    $01C2           
2CDE: C0             RET     NZ              
2CDF: 01 04 00       LD      BC,$0004        
2CE2: 21 80 49       LD      HL,$4980        
2CE5: 97             SUB     A               
2CE6: AE             XOR     (HL)            
2CE7: 23             INC     HL              
2CE8: 10 FC          DJNZ    $2CE6           
2CEA: 0D             DEC     C               
2CEB: 20 F9          JR      NZ,$2CE6        
2CED: C6 BD          ADD     $BD             
2CEF: C2 11 0F       JP      NZ,$0F11        
2CF2: C3 1A 0F       JP      $0F1A           
2CF5: CD 15 2D       CALL    $2D15           
2CF8: CD 36 2D       CALL    $2D36           
2CFB: CD 36 2D       CALL    $2D36           
2CFE: CD 68 2D       CALL    $2D68           
2D01: C9             RET                     
2D02: CD 2D 2D       CALL    $2D2D           
2D05: CD 2D 2D       CALL    $2D2D           
2D08: CD 62 2D       CALL    $2D62           
2D0B: CD 62 2D       CALL    $2D62           
2D0E: CD 68 2D       CALL    $2D68           
2D11: CD 68 2D       CALL    $2D68           
2D14: C9             RET                     
2D15: CD 6E 2D       CALL    $2D6E           
2D18: CD 58 30       CALL    $3058           
2D1B: CD 58 30       CALL    $3058           
2D1E: C3 9B 30       JP      $309B           
2D21: CD 6E 2D       CALL    $2D6E           
2D24: CD 58 30       CALL    $3058           
2D27: CD 8A 30       CALL    $308A           
2D2A: C3 9B 30       JP      $309B           
2D2D: CD 6E 2D       CALL    $2D6E           
2D30: CD 58 30       CALL    $3058           
2D33: C3 9B 30       JP      $309B           
2D36: CD 93 2D       CALL    $2D93           
2D39: CD 58 30       CALL    $3058           
2D3C: C3 9B 30       JP      $309B           
2D3F: 3A C0 A9       LD      A,($A9C0)       
2D42: A7             AND     A               
2D43: C2 1A 0F       JP      NZ,$0F1A        
2D46: CD FB 4A       CALL    $4AFB           
2D49: 11 08 01       LD      DE,$0108        
2D4C: FF             RST     0X38            
2D4D: 3A 17 A8       LD      A,($A817)       
2D50: A7             AND     A               
2D51: C2 3E 2E       JP      NZ,$2E3E        
2D54: CD 06 0B       CALL    $0B06           
2D57: CD 39 0B       CALL    $0B39           
2D5A: 21 6B 08       LD      HL,$086B        
2D5D: 06 14          LD      B,$14           
2D5F: C3 E8 43       JP      $43E8           
2D62: CD 93 2D       CALL    $2D93           
2D65: C3 9B 30       JP      $309B           
2D68: CD F4 2D       CALL    $2DF4           
2D6B: C3 9B 30       JP      $309B           
2D6E: FD 56 31       LD      D,(IY+$31)      
2D71: DD 5E 03       LD      E,(IX+$03)      
2D74: 2A 08 A8       LD      HL,($A808)      
2D77: CD 31 2E       CALL    $2E31           
2D7A: FD 74 31       LD      (IY+$31),H      
2D7D: DD 75 03       LD      (IX+$03),L      
2D80: FD 56 00       LD      D,(IY+$00)      
2D83: DD 5E 05       LD      E,(IX+$05)      
2D86: 2A 0A A8       LD      HL,($A80A)      
2D89: CD 31 2E       CALL    $2E31           
2D8C: FD 74 00       LD      (IY+$00),H      
2D8F: DD 75 05       LD      (IX+$05),L      
2D92: C9             RET                     
2D93: FD 56 31       LD      D,(IY+$31)      
2D96: DD 5E 03       LD      E,(IX+$03)      
2D99: 2A 08 A8       LD      HL,($A808)      
2D9C: CD 3E 30       CALL    $303E           
2D9F: FD 74 31       LD      (IY+$31),H      
2DA2: DD 75 03       LD      (IX+$03),L      
2DA5: FD 56 00       LD      D,(IY+$00)      
2DA8: DD 5E 05       LD      E,(IX+$05)      
2DAB: 2A 0A A8       LD      HL,($A80A)      
2DAE: CD 3E 30       CALL    $303E           
2DB1: FD 74 00       LD      (IY+$00),H      
2DB4: DD 75 05       LD      (IX+$05),L      
2DB7: C9             RET                     
2DB8: 21 01 AD       LD      HL,$AD01        
2DBB: 34             INC     (HL)            
2DBC: 21 04 AD       LD      HL,$AD04        
2DBF: 7E             LD      A,(HL)          
2DC0: 3C             INC     A               
2DC1: FE 05          CP      $05             
2DC3: 38 01          JR      C,$2DC6         
2DC5: AF             XOR     A               
2DC6: 77             LD      (HL),A          
2DC7: 3A 01 AD       LD      A,($AD01)       
2DCA: FE 06          CP      $06             
2DCC: 38 09          JR      C,$2DD7         
2DCE: FE 0B          CP      $0B             
2DD0: 38 0A          JR      C,$2DDC         
2DD2: 3A D5 A9       LD      A,($A9D5)       
2DD5: 18 08          JR      $2DDF           
2DD7: 3A D3 A9       LD      A,($A9D3)       
2DDA: 18 03          JR      $2DDF           
2DDC: 3A D4 A9       LD      A,($A9D4)       
2DDF: 32 0A AD       LD      ($AD0A),A       
2DE2: 3A CD A9       LD      A,($A9CD)       
2DE5: 32 02 AD       LD      ($AD02),A       
2DE8: AF             XOR     A               
2DE9: 32 0D AD       LD      ($AD0D),A       
2DEC: 32 C6 AC       LD      ($ACC6),A       
2DEF: 3D             DEC     A               
2DF0: 32 0E AD       LD      ($AD0E),A       
2DF3: C9             RET                     
2DF4: FD 56 31       LD      D,(IY+$31)      
2DF7: DD 5E 03       LD      E,(IX+$03)      
2DFA: 2A 08 A8       LD      HL,($A808)      
2DFD: CD 4D 30       CALL    $304D           
2E00: FD 74 31       LD      (IY+$31),H      
2E03: DD 75 03       LD      (IX+$03),L      
2E06: FD 56 00       LD      D,(IY+$00)      
2E09: DD 5E 05       LD      E,(IX+$05)      
2E0C: 2A 0A A8       LD      HL,($A80A)      
2E0F: CD 4D 30       CALL    $304D           
2E12: FD 74 00       LD      (IY+$00),H      
2E15: DD 75 05       LD      (IX+$05),L      
2E18: C9             RET                     
2E19: 32 C1 A9       LD      ($A9C1),A       
2E1C: 79             LD      A,C             
2E1D: 0F             RRCA                    
2E1E: 0F             RRCA                    
2E1F: 4F             LD      C,A             
2E20: E6 01          AND     $01             
2E22: 32 C2 A9       LD      ($A9C2),A       
2E25: 79             LD      A,C             
2E26: 0F             RRCA                    
2E27: 4F             LD      C,A             
2E28: E6 01          AND     $01             
2E2A: 32 C3 A9       LD      ($A9C3),A       
2E2D: 79             LD      A,C             
2E2E: C3 A8 49       JP      $49A8           
2E31: 44             LD      B,H             
2E32: 4D             LD      C,L             
2E33: CB 28          SRA     B               
2E35: CB 19          RR      C               
2E37: CB 28          SRA     B               
2E39: CB 19          RR      C               
2E3B: 09             ADD     HL,BC           
2E3C: 19             ADD     HL,DE           
2E3D: C9             RET                     
2E3E: 32 01 31       LD      ($3101),A       
2E41: 01 30 01       LD      BC,$0130        
2E44: 2F             CPL                     
2E45: 01 2E 01       LD      BC,$012E        
2E48: 2D             DEC     L               
2E49: 01 2C 01       LD      BC,$012C        
2E4C: 28 01          JR      Z,$2E4F         
2E4E: 26 01          LD      H,$01           
2E50: 24             INC     H               
2E51: 01 22 01       LD      BC,$0122        
2E54: 20 01          JR      NZ,$2E57        
2E56: 1B             DEC     DE              
2E57: 01 18 01       LD      BC,$0118        
2E5A: 16 01          LD      D,$01           
2E5C: 11 01 0E       LD      DE,$0E01        
2E5F: 01 0B 01       LD      BC,$010B        
2E62: 08             EX      AF,AF'          
2E63: 01 03 01       LD      BC,$0103        
2E66: 00             NOP                     
2E67: 01 FD 00       LD      BC,$00FD        
2E6A: F8             RET     M               
2E6B: 00             NOP                     
2E6C: F5             PUSH    AF              
2E6D: 00             NOP                     
2E6E: F2 00 ED       JP      P,$ED00         
2E71: 00             NOP                     
2E72: EA 00 E7       JP      PE,$E700        
2E75: 00             NOP                     
2E76: E4 00 DF       CALL    PO,$DF00        
2E79: 00             NOP                     
2E7A: DC 00 D9       CALL    C,$D900         
2E7D: 00             NOP                     
2E7E: D4 00 D1       CALL    NC,$D100        
2E81: 00             NOP                     
2E82: CD 00 C8       CALL    $C800           
2E85: 00             NOP                     
2E86: C5             PUSH    BC              
2E87: 00             NOP                     
2E88: C1             POP     BC              
2E89: 00             NOP                     
2E8A: BB             CP      E               
2E8B: 00             NOP                     
2E8C: B7             OR      A               
2E8D: 00             NOP                     
2E8E: B4             OR      H               
2E8F: 00             NOP                     
2E90: AE             XOR     (HL)            
2E91: 00             NOP                     
2E92: A8             XOR     B               
2E93: 00             NOP                     
2E94: A1             AND     C               
2E95: 00             NOP                     
2E96: 9C             SBC     H               
2E97: 00             NOP                     
2E98: 93             SUB     E               
2E99: 00             NOP                     
2E9A: 90             SUB     B               
2E9B: 00             NOP                     
2E9C: 88             ADC     A,B             
2E9D: 00             NOP                     
2E9E: 80             ADD     A,B             
2E9F: 00             NOP                     
2EA0: 7A             LD      A,D             
2EA1: 00             NOP                     
2EA2: 72             LD      (HL),D          
2EA3: 00             NOP                     
2EA4: 69             LD      L,C             
2EA5: 00             NOP                     
2EA6: 63             LD      H,E             
2EA7: 00             NOP                     
2EA8: 5A             LD      E,D             
2EA9: 00             NOP                     
2EAA: 51             LD      D,C             
2EAB: 00             NOP                     
2EAC: 4A             LD      C,D             
2EAD: 00             NOP                     
2EAE: 40             LD      B,B             
2EAF: 00             NOP                     
2EB0: 37             SCF                     
2EB1: 00             NOP                     
2EB2: 30 00          JR      NC,$2EB4        
2EB4: 26 00          LD      H,$00           
2EB6: 1C             INC     E               
2EB7: 00             NOP                     
2EB8: 12             LD      (DE),A          
2EB9: 00             NOP                     
2EBA: 08             EX      AF,AF'          
2EBB: 00             NOP                     
2EBC: 00             NOP                     
2EBD: 00             NOP                     
2EBE: 00             NOP                     
2EBF: 00             NOP                     
2EC0: F8             RET     M               
2EC1: FF             RST     0X38            
2EC2: EE FF          XOR     $FF             
2EC4: 00             NOP                     
2EC5: 00             NOP                     
2EC6: DA FF D0       JP      C,$D0FF         
2EC9: FF             RST     0X38            
2ECA: C9             RET                     
2ECB: FF             RST     0X38            
2ECC: C0             RET     NZ              
2ECD: FF             RST     0X38            
2ECE: B6             OR      (HL)            
2ECF: FF             RST     0X38            
2ED0: AF             XOR     A               
2ED1: FF             RST     0X38            
2ED2: A6             AND     (HL)            
2ED3: FF             RST     0X38            
2ED4: 9D             SBC     L               
2ED5: FF             RST     0X38            
2ED6: 97             SUB     A               
2ED7: FF             RST     0X38            
2ED8: 8E             ADC     A,(HL)          
2ED9: FF             RST     0X38            
2EDA: 86             ADD     A,(HL)          
2EDB: FF             RST     0X38            
2EDC: 80             ADD     A,B             
2EDD: FF             RST     0X38            
2EDE: 78             LD      A,B             
2EDF: FF             RST     0X38            
2EE0: 70             LD      (HL),B          
2EE1: FF             RST     0X38            
2EE2: 6D             LD      L,L             
2EE3: FF             RST     0X38            
2EE4: 70             LD      (HL),B          
2EE5: FF             RST     0X38            
2EE6: 5F             LD      E,A             
2EE7: FF             RST     0X38            
2EE8: 58             LD      E,B             
2EE9: FF             RST     0X38            
2EEA: 52             LD      D,D             
2EEB: FF             RST     0X38            
2EEC: 4C             LD      C,H             
2EED: FF             RST     0X38            
2EEE: 49             LD      C,C             
2EEF: FF             RST     0X38            
2EF0: 45             LD      B,L             
2EF1: FF             RST     0X38            
2EF2: 3F             CCF                     
2EF3: FF             RST     0X38            
2EF4: 3B             DEC     SP              
2EF5: FF             RST     0X38            
2EF6: 38 FF          JR      C,$2EF7         
2EF8: 33             INC     SP              
2EF9: FF             RST     0X38            
2EFA: 2F             CPL                     
2EFB: FF             RST     0X38            
2EFC: 2C             INC     L               
2EFD: FF             RST     0X38            
2EFE: 27             DAA                     
2EFF: FF             RST     0X38            
2F00: 24             INC     H               
2F01: FF             RST     0X38            
2F02: 21 FF 21       LD      HL,$21FF        
2F05: FF             RST     0X38            
2F06: 19             ADD     HL,DE           
2F07: FF             RST     0X38            
2F08: 16 FF          LD      D,$FF           
2F0A: 13             INC     DE              
2F0B: FF             RST     0X38            
2F0C: 0E FF          LD      C,$FF           
2F0E: 0B             DEC     BC              
2F0F: FF             RST     0X38            
2F10: 08             EX      AF,AF'          
2F11: FF             RST     0X38            
2F12: 03             INC     BC              
2F13: FF             RST     0X38            
2F14: 00             NOP                     
2F15: FF             RST     0X38            
2F16: FD                                  
2F17: FE F8          CP      $F8             
2F19: FE F5          CP      $F5             
2F1B: FE F2          CP      $F2             
2F1D: FE EF          CP      $EF             
2F1F: FE EA          CP      $EA             
2F21: FE E8          CP      $E8             
2F23: FE E5          CP      $E5             
2F25: FE E0          CP      $E0             
2F27: FE DE          CP      $DE             
2F29: FE DC          CP      $DC             
2F2B: FE DA          CP      $DA             
2F2D: FE D8          CP      $D8             
2F2F: FE D4          CP      $D4             
2F31: FE D3          CP      $D3             
2F33: FE D2          CP      $D2             
2F35: FE D1          CP      $D1             
2F37: FE D0          CP      $D0             
2F39: FE CF          CP      $CF             
2F3B: FE CE          CP      $CE             
2F3D: FE CE          CP      $CE             
2F3F: FE CF          CP      $CF             
2F41: FE D0          CP      $D0             
2F43: FE D1          CP      $D1             
2F45: FE D2          CP      $D2             
2F47: FE D3          CP      $D3             
2F49: FE D4          CP      $D4             
2F4B: FE D8          CP      $D8             
2F4D: FE DA          CP      $DA             
2F4F: FE DC          CP      $DC             
2F51: FE DE          CP      $DE             
2F53: FE E0          CP      $E0             
2F55: FE E5          CP      $E5             
2F57: FE E8          CP      $E8             
2F59: FE EA          CP      $EA             
2F5B: FE EF          CP      $EF             
2F5D: FE F2          CP      $F2             
2F5F: FE F5          CP      $F5             
2F61: FE F8          CP      $F8             
2F63: FE FD          CP      $FD             
2F65: FE 00          CP      $00             
2F67: FF             RST     0X38            
2F68: 03             INC     BC              
2F69: FF             RST     0X38            
2F6A: 08             EX      AF,AF'          
2F6B: FF             RST     0X38            
2F6C: 0B             DEC     BC              
2F6D: FF             RST     0X38            
2F6E: 0E FF          LD      C,$FF           
2F70: 13             INC     DE              
2F71: FF             RST     0X38            
2F72: 16 FF          LD      D,$FF           
2F74: 19             ADD     HL,DE           
2F75: FF             RST     0X38            
2F76: 1C             INC     E               
2F77: FF             RST     0X38            
2F78: 21 FF 24       LD      HL,$24FF        
2F7B: FF             RST     0X38            
2F7C: 27             DAA                     
2F7D: FF             RST     0X38            
2F7E: 2C             INC     L               
2F7F: FF             RST     0X38            
2F80: 2F             CPL                     
2F81: FF             RST     0X38            
2F82: 33             INC     SP              
2F83: FF             RST     0X38            
2F84: 38 FF          JR      C,$2F85         
2F86: 3B             DEC     SP              
2F87: FF             RST     0X38            
2F88: 3F             CCF                     
2F89: FF             RST     0X38            
2F8A: 45             LD      B,L             
2F8B: FF             RST     0X38            
2F8C: 49             LD      C,C             
2F8D: FF             RST     0X38            
2F8E: 4C             LD      C,H             
2F8F: FF             RST     0X38            
2F90: 52             LD      D,D             
2F91: FF             RST     0X38            
2F92: 58             LD      E,B             
2F93: FF             RST     0X38            
2F94: 5F             LD      E,A             
2F95: FF             RST     0X38            
2F96: 64             LD      H,H             
2F97: FF             RST     0X38            
2F98: 6D             LD      L,L             
2F99: FF             RST     0X38            
2F9A: 70             LD      (HL),B          
2F9B: FF             RST     0X38            
2F9C: 78             LD      A,B             
2F9D: FF             RST     0X38            
2F9E: 80             ADD     A,B             
2F9F: FF             RST     0X38            
2FA0: 86             ADD     A,(HL)          
2FA1: FF             RST     0X38            
2FA2: 8E             ADC     A,(HL)          
2FA3: FF             RST     0X38            
2FA4: 97             SUB     A               
2FA5: FF             RST     0X38            
2FA6: 9D             SBC     L               
2FA7: FF             RST     0X38            
2FA8: A6             AND     (HL)            
2FA9: FF             RST     0X38            
2FAA: AF             XOR     A               
2FAB: FF             RST     0X38            
2FAC: B6             OR      (HL)            
2FAD: FF             RST     0X38            
2FAE: C0             RET     NZ              
2FAF: FF             RST     0X38            
2FB0: C9             RET                     
2FB1: FF             RST     0X38            
2FB2: D0             RET     NC              
2FB3: FF             RST     0X38            
2FB4: DA FF E4       JP      C,$E4FF         
2FB7: FF             RST     0X38            
2FB8: EE FF          XOR     $FF             
2FBA: F8             RET     M               
2FBB: FF             RST     0X38            
2FBC: 00             NOP                     
2FBD: 00             NOP                     
2FBE: 00             NOP                     
2FBF: 00             NOP                     
2FC0: 08             EX      AF,AF'          
2FC1: 00             NOP                     
2FC2: 12             LD      (DE),A          
2FC3: 00             NOP                     
2FC4: 1C             INC     E               
2FC5: 00             NOP                     
2FC6: 26 00          LD      H,$00           
2FC8: 30 00          JR      NC,$2FCA        
2FCA: 37             SCF                     
2FCB: 00             NOP                     
2FCC: 40             LD      B,B             
2FCD: 00             NOP                     
2FCE: 4A             LD      C,D             
2FCF: 00             NOP                     
2FD0: 51             LD      D,C             
2FD1: 00             NOP                     
2FD2: 5A             LD      E,D             
2FD3: 00             NOP                     
2FD4: 63             LD      H,E             
2FD5: 00             NOP                     
2FD6: 69             LD      L,C             
2FD7: 00             NOP                     
2FD8: 72             LD      (HL),D          
2FD9: 00             NOP                     
2FDA: 7A             LD      A,D             
2FDB: 00             NOP                     
2FDC: 80             ADD     A,B             
2FDD: 00             NOP                     
2FDE: 88             ADC     A,B             
2FDF: 00             NOP                     
2FE0: 90             SUB     B               
2FE1: 00             NOP                     
2FE2: 93             SUB     E               
2FE3: 00             NOP                     
2FE4: 93             SUB     E               
2FE5: 00             NOP                     
2FE6: A1             AND     C               
2FE7: 00             NOP                     
2FE8: A8             XOR     B               
2FE9: 00             NOP                     
2FEA: AE             XOR     (HL)            
2FEB: 00             NOP                     
2FEC: B4             OR      H               
2FED: 00             NOP                     
2FEE: B7             OR      A               
2FEF: 00             NOP                     
2FF0: BB             CP      E               
2FF1: 00             NOP                     
2FF2: C1             POP     BC              
2FF3: 00             NOP                     
2FF4: C5             PUSH    BC              
2FF5: 00             NOP                     
2FF6: C8             RET     Z               
2FF7: 00             NOP                     
2FF8: CD 00 D1       CALL    $D100           
2FFB: 00             NOP                     
2FFC: D4 00 D9       CALL    NC,$D900        
2FFF: 00             NOP                     
3000: DC 00 DF       CALL    C,$DF00         
3003: 00             NOP                     
3004: DC 00 E7       CALL    C,$E700         
3007: 00             NOP                     
3008: EA 00 ED       JP      PE,$ED00        
300B: 00             NOP                     
300C: F2 00 F5       JP      P,$F500         
300F: 00             NOP                     
3010: F8             RET     M               
3011: 00             NOP                     
3012: FD                                  
3013: 00             NOP                     
3014: 00             NOP                     
3015: 01 03 01       LD      BC,$0103        
3018: 08             EX      AF,AF'          
3019: 01 0B 01       LD      BC,$010B        
301C: 0E 01          LD      C,$01           
301E: 11 01 16       LD      DE,$1601        
3021: 01 18 01       LD      BC,$0118        
3024: 11 01 20       LD      DE,$2001        
3027: 01 22 01       LD      BC,$0122        
302A: 24             INC     H               
302B: 01 26 01       LD      BC,$0126        
302E: 28 01          JR      Z,$3031         
3030: 2C             INC     L               
3031: 01 2D 01       LD      BC,$012D        
3034: 2E 01          LD      L,$01           
3036: 2F             CPL                     
3037: 01 30 01       LD      BC,$0130        
303A: 31 01 32       LD      SP,$3201        
303D: 01 44 4D       LD      BC,$4D44        
3040: CB 28          SRA     B               
3042: CB 19          RR      C               
3044: CB 28          SRA     B               
3046: CB 19          RR      C               
3048: A7             AND     A               
3049: ED 42          SBC     HL,BC           
304B: 19             ADD     HL,DE           
304C: C9             RET                     
304D: 44             LD      B,H             
304E: 4D             LD      C,L             
304F: CB 28          SRA     B               
3051: CB 19          RR      C               
3053: A7             AND     A               
3054: ED 42          SBC     HL,BC           
3056: 19             ADD     HL,DE           
3057: C9             RET                     
3058: FD 46 31       LD      B,(IY+$31)      
305B: FD 4E 00       LD      C,(IY+$00)      
305E: 3E 10          LD      A,$10           
3060: 80             ADD     A,B             
3061: FD 77 33       LD      (IY+$33),A      
3064: FD 71 02       LD      (IY+$02),C      
3067: C3 9B 30       JP      $309B           
306A: FD 46 31       LD      B,(IY+$31)      
306D: FD 4E 00       LD      C,(IY+$00)      
3070: 26 08          LD      H,$08           
3072: 2E 6E          LD      L,$6E           
3074: 7E             LD      A,(HL)          
3075: 81             ADD     A,C             
3076: FD 70 33       LD      (IY+$33),B      
3079: FD 77 02       LD      (IY+$02),A      
307C: C3 9B 30       JP      $309B           
307F: 73             LD      (HL),E          
3080: A6             AND     (HL)            
3081: 10 F1          DJNZ    $3074           
3083: D7             RST     0X10            
3084: 34             INC     (HL)            
3085: A5             AND     L               
3086: 87             ADD     A,A             
3087: BF             CP      A               
3088: F1             POP     AF              
3089: B9             CP      C               
308A: FD 46 31       LD      B,(IY+$31)      
308D: FD 4E 00       LD      C,(IY+$00)      
3090: 26 F0          LD      H,$F0           
3092: 2E 10          LD      L,$10           
3094: 09             ADD     HL,BC           
3095: FD 74 33       LD      (IY+$33),H      
3098: FD 75 02       LD      (IY+$02),L      
309B: 11 10 00       LD      DE,$0010        
309E: DD 19          ADD     IX,DE           
30A0: FD 23          INC     IY              
30A2: FD 23          INC     IY              
30A4: C9             RET                     
30A5: 21 6B 08       LD      HL,$086B        
30A8: 0E 22          LD      C,$22           
30AA: 06 10          LD      B,$10           
30AC: CD 4C 0B       CALL    $0B4C           
30AF: 3A 04 AD       LD      A,($AD04)       
30B2: 87             ADD     A,A             
30B3: 87             ADD     A,A             
30B4: 87             ADD     A,A             
30B5: 4F             LD      C,A             
30B6: 21 76 31       LD      HL,$3176        
30B9: DF             RST     0X18            
30BA: 11 31 AA       LD      DE,$AA31        
30BD: 06 08          LD      B,$08           
30BF: 7E             LD      A,(HL)          
30C0: 12             LD      (DE),A          
30C1: 23             INC     HL              
30C2: 13             INC     DE              
30C3: 13             INC     DE              
30C4: 10 F9          DJNZ    $30BF           
30C6: 3A 04 AD       LD      A,($AD04)       
30C9: FE 04          CP      $04             
30CB: 4F             LD      C,A             
30CC: CA 56 31       JP      Z,$3156         
30CF: 3E CC          LD      A,$CC           
30D1: 21 60 AA       LD      HL,$AA60        
30D4: 11 02 00       LD      DE,$0002        
30D7: 06 08          LD      B,$08           
30D9: 77             LD      (HL),A          
30DA: 19             ADD     HL,DE           
30DB: 10 FC          DJNZ    $30D9           
30DD: 79             LD      A,C             
30DE: FE 04          CP      $04             
30E0: DA 17 31       JP      C,$3117         
30E3: 21 C7 AC       LD      HL,$ACC7        
30E6: 7E             LD      A,(HL)          
30E7: FE 3B          CP      $3B             
30E9: C2 5B 31       JP      NZ,$315B        
30EC: 23             INC     HL              
30ED: 7E             LD      A,(HL)          
30EE: FE 05          CP      $05             
30F0: CA F8 30       JP      Z,$30F8         
30F3: FE 10          CP      $10             
30F5: C2 5B 31       JP      NZ,$315B        
30F8: 06 08          LD      B,$08           
30FA: FD 21 30 AA    LD      IY,$AA30        
30FE: 21 5E 31       LD      HL,$315E        
3101: 7E             LD      A,(HL)          
3102: FD 77 31       LD      (IY+$31),A      
3105: 23             INC     HL              
3106: 7E             LD      A,(HL)          
3107: FD 77 00       LD      (IY+$00),A      
310A: 23             INC     HL              
310B: FD 23          INC     IY              
310D: FD 23          INC     IY              
310F: 10 F0          DJNZ    $3101           
3111: C3 BC 2C       JP      $2CBC           
3114: C3 7F 30       JP      $307F           
3117: 21 39 AD       LD      HL,$AD39        
311A: 7E             LD      A,(HL)          
311B: FE 68          CP      $68             
311D: C2 14 31       JP      NZ,$3114        
3120: 23             INC     HL              
3121: 7E             LD      A,(HL)          
3122: FE 10          CP      $10             
3124: CA 2C 31       JP      Z,$312C         
3127: FE 05          CP      $05             
3129: C2 14 31       JP      NZ,$3114        
312C: 21 6E 31       LD      HL,$316E        
312F: 06 04          LD      B,$04           
3131: FD 21 30 AA    LD      IY,$AA30        
3135: 7E             LD      A,(HL)          
3136: FD 77 31       LD      (IY+$31),A      
3139: C6 10          ADD     $10             
313B: FD 77 33       LD      (IY+$33),A      
313E: 23             INC     HL              
313F: 7E             LD      A,(HL)          
3140: FD 77 00       LD      (IY+$00),A      
3143: FD 77 02       LD      (IY+$02),A      
3146: 23             INC     HL              
3147: 11 10 00       LD      DE,$0010        
314A: DD 19          ADD     IX,DE           
314C: 11 04 00       LD      DE,$0004        
314F: FD 19          ADD     IY,DE           
3151: 10 E2          DJNZ    $3135           
3153: C3 BC 2C       JP      $2CBC           
3156: 3E 28          LD      A,$28           
3158: C3 D1 30       JP      $30D1           
315B: C3 76 31       JP      $3176           
315E: 40             LD      B,B             
315F: 68             LD      L,B             
3160: 38 62          JR      C,$31C4         
3162: 60             LD      H,B             
3163: 70             LD      (HL),B          
3164: 68             LD      L,B             
3165: D8             RET     C               
3166: 88             ADC     A,B             
3167: 58             LD      E,B             
3168: 99             SBC     C               
3169: B0             OR      B               
316A: 37             SCF                     
316B: 43             LD      B,E             
316C: CF             RST     0X08            
316D: 78             LD      A,B             
316E: 20 D0          JR      NZ,$3140        
3170: 50             LD      D,B             
3171: 60             LD      H,B             
3172: A0             AND     B               
3173: A0             AND     B               
3174: D0             RET     NC              
3175: 60             LD      H,B             
3176: 60             LD      H,B             
3177: 68             LD      L,B             
3178: 61             LD      H,C             
3179: 60             LD      H,B             
317A: 61             LD      H,C             
317B: 62             LD      H,D             
317C: 63             LD      H,E             
317D: 5C             LD      E,H             
317E: 74             LD      (HL),H          
317F: 75             LD      (HL),L          
3180: 76             HALT                    
3181: 60             LD      H,B             
3182: 61             LD      H,C             
3183: 64             LD      H,H             
3184: 65             LD      H,L             
3185: 5D             LD      E,L             
3186: 77             LD      (HL),A          
3187: 78             LD      A,B             
3188: 79             LD      A,C             
3189: 66             LD      H,(HL)          
318A: 67             LD      H,A             
318B: 64             LD      H,H             
318C: 65             LD      H,L             
318D: 5E             LD      E,(HL)          
318E: 7A             LD      A,D             
318F: 7B             LD      A,E             
3190: 7C             LD      A,H             
3191: 60             LD      H,B             
3192: 61             LD      H,C             
3193: 62             LD      H,D             
3194: 63             LD      H,E             
3195: 5F             LD      E,A             
3196: 31 30 33       LD      SP,$3330        
3199: 32 85 86       LD      ($8685),A       
319C: 87             ADD     A,A             
319D: 85             ADD     A,L             
319E: 08             EX      AF,AF'          
319F: A7             AND     A               
31A0: 32 CA 7E       LD      ($7ECA),A       
31A3: C8             RET     Z               
31A4: FF             RST     0X38            
31A5: 5F             LD      E,A             
31A6: 93             SUB     E               
31A7: FB             EI                      
31A8: C4 AF D8       CALL    NZ,$D8AF        
31AB: 2A 6C E1       LD      HL,($E16C)      
31AE: 7A             LD      A,D             
31AF: 42             LD      B,D             
31B0: BD             CP      L               
31B1: B0             OR      B               
31B2: 5A             LD      E,D             
31B3: B9             CP      C               
31B4: 3A 05 AD       LD      A,($AD05)       
31B7: 4F             LD      C,A             
31B8: E6 F0          AND     $F0             
31BA: 28 0D          JR      Z,$31C9         
31BC: FE 30          CP      $30             
31BE: C2 6C 32       JP      NZ,$326C        
31C1: 3A 03 49       LD      A,($4903)       
31C4: FE 30          CP      $30             
31C6: C2 C9 31       JP      NZ,$31C9        
31C9: 79             LD      A,C             
31CA: E6 0F          AND     $0F             
31CC: FE 07          CP      $07             
31CE: D0             RET     NC              
31CF: DD 21 50 A8    LD      IX,$A850        
31D3: FD 21 1A AA    LD      IY,$AA1A        
31D7: 87             ADD     A,A             
31D8: 4F             LD      C,A             
31D9: 06 00          LD      B,$00           
31DB: FD 09          ADD     IY,BC           
31DD: 87             ADD     A,A             
31DE: 87             ADD     A,A             
31DF: 87             ADD     A,A             
31E0: 4F             LD      C,A             
31E1: DD 09          ADD     IX,BC           
31E3: DD 7E 00       LD      A,(IX+$00)      
31E6: 3C             INC     A               
31E7: C0             RET     NZ              
31E8: CD 3A 32       CALL    $323A           
31EB: DD 7E 08       LD      A,(IX+$08)      
31EE: FE 10          CP      $10             
31F0: C8             RET     Z               
31F1: FE 11          CP      $11             
31F3: 28 0C          JR      Z,$3201         
31F5: 87             ADD     A,A             
31F6: 21 65 AC       LD      HL,$AC65        
31F9: DF             RST     0X18            
31FA: CD B8 33       CALL    $33B8           
31FD: DD 77 01       LD      (IX+$01),A      
3200: C9             RET                     
3201: 21 65 AC       LD      HL,$AC65        
3204: CD B8 33       CALL    $33B8           
3207: C6 80          ADD     $80             
3209: DD 77 01       LD      (IX+$01),A      
320C: DD 36 08 10    LD      (IX+$08),$10    
3210: DD 36 09 00    LD      (IX+$09),$00    
3214: C9             RET                     
3215: CD 2B 0B       CALL    $0B2B           
3218: AF             XOR     A               
3219: 32 31 AD       LD      ($AD31),A       
321C: 32 20 AD       LD      ($AD20),A       
321F: 3D             DEC     A               
3220: 32 30 AD       LD      ($AD30),A       
3223: 3A C1 A9       LD      A,($A9C1)       
3226: 32 10 AD       LD      ($AD10),A       
3229: 21 86 A9       LD      HL,$A986        
322C: 7E             LD      A,(HL)          
322D: D6 01          SUB     $01             
322F: 27             DAA                     
3230: 77             LD      (HL),A          
3231: CD FB 4A       CALL    $4AFB           
3234: CD 30 4B       CALL    $4B30           
3237: C3 2A 17       JP      $172A           
323A: DD 7E 09       LD      A,(IX+$09)      
323D: A7             AND     A               
323E: C8             RET     Z               
323F: 3D             DEC     A               
3240: DD 77 09       LD      (IX+$09),A      
3243: 4F             LD      C,A             
3244: DD 7E 0A       LD      A,(IX+$0A)      
3247: 21 38 34       LD      HL,$3438        
324A: D7             RST     0X10            
324B: EB             EX      DE,HL           
324C: 79             LD      A,C             
324D: CF             RST     0X08            
324E: DD 77 08       LD      (IX+$08),A      
3251: C9             RET                     
3252: 01 00 03       LD      BC,$0300        
3255: 21 08 00       LD      HL,$0008        
3258: 1E 00          LD      E,$00           
325A: 7B             LD      A,E             
325B: AE             XOR     (HL)            
325C: 23             INC     HL              
325D: 0B             DEC     BC              
325E: 5F             LD      E,A             
325F: 79             LD      A,C             
3260: B0             OR      B               
3261: 20 F7          JR      NZ,$325A        
3263: 3E 52          LD      A,$52           
3265: 83             ADD     A,E             
3266: C2 11 0F       JP      NZ,$0F11        
3269: C3 1A 0F       JP      $0F1A           
326C: 79             LD      A,C             
326D: E6 0F          AND     $0F             
326F: FE 07          CP      $07             
3271: C0             RET     NZ              
3272: DD 21 64 AC    LD      IX,$AC64        
3276: 3A 02 A8       LD      A,($A802)       
3279: C6 40          ADD     $40             
327B: CD D1 59       CALL    $59D1           
327E: EB             EX      DE,HL           
327F: 29             ADD     HL,HL           
3280: 29             ADD     HL,HL           
3281: 29             ADD     HL,HL           
3282: 7C             LD      A,H             
3283: C6 78          ADD     $78             
3285: DD 77 10       LD      (IX+$10),A      
3288: 7C             LD      A,H             
3289: ED 44          NEG                     
328B: C6 78          ADD     $78             
328D: DD 77 14       LD      (IX+$14),A      
3290: 29             ADD     HL,HL           
3291: 7C             LD      A,H             
3292: C6 78          ADD     $78             
3294: DD 77 12       LD      (IX+$12),A      
3297: 7C             LD      A,H             
3298: ED 44          NEG                     
329A: C6 78          ADD     $78             
329C: DD 77 16       LD      (IX+$16),A      
329F: 60             LD      H,B             
32A0: 69             LD      L,C             
32A1: 29             ADD     HL,HL           
32A2: 29             ADD     HL,HL           
32A3: 29             ADD     HL,HL           
32A4: 7C             LD      A,H             
32A5: C6 84          ADD     $84             
32A7: DD 77 11       LD      (IX+$11),A      
32AA: 7C             LD      A,H             
32AB: ED 44          NEG                     
32AD: C6 84          ADD     $84             
32AF: DD 77 15       LD      (IX+$15),A      
32B2: 29             ADD     HL,HL           
32B3: 7C             LD      A,H             
32B4: C6 84          ADD     $84             
32B6: DD 77 13       LD      (IX+$13),A      
32B9: 7C             LD      A,H             
32BA: ED 44          NEG                     
32BC: C6 84          ADD     $84             
32BE: DD 77 17       LD      (IX+$17),A      
32C1: 3A 02 A8       LD      A,($A802)       
32C4: CD D1 59       CALL    $59D1           
32C7: EB             EX      DE,HL           
32C8: 29             ADD     HL,HL           
32C9: 29             ADD     HL,HL           
32CA: 29             ADD     HL,HL           
32CB: 7C             LD      A,H             
32CC: C6 78          ADD     $78             
32CE: DD 77 18       LD      (IX+$18),A      
32D1: 29             ADD     HL,HL           
32D2: 7C             LD      A,H             
32D3: C6 78          ADD     $78             
32D5: DD 77 1A       LD      (IX+$1A),A      
32D8: 60             LD      H,B             
32D9: 69             LD      L,C             
32DA: 29             ADD     HL,HL           
32DB: 29             ADD     HL,HL           
32DC: 29             ADD     HL,HL           
32DD: 7C             LD      A,H             
32DE: C6 84          ADD     $84             
32E0: DD 77 19       LD      (IX+$19),A      
32E3: 29             ADD     HL,HL           
32E4: 7C             LD      A,H             
32E5: C6 84          ADD     $84             
32E7: DD 77 1B       LD      (IX+$1B),A      
32EA: C9             RET                     
32EB: 32 00 C2       LD      ($C200),A       
32EE: 21 EB A9       LD      HL,$A9EB        
32F1: 36 0C          LD      (HL),$0C        
32F3: 01 00 00       LD      BC,$0000        
32F6: 10 FE          DJNZ    $32F6           
32F8: 32 00 C2       LD      ($C200),A       
32FB: 0D             DEC     C               
32FC: 20 F8          JR      NZ,$32F6        
32FE: 35             DEC     (HL)            
32FF: 20 F2          JR      NZ,$32F3        
3301: AF             XOR     A               
3302: CD F8 55       CALL    $55F8           
3305: 3A 87 4C       LD      A,($4C87)       
3308: C3 A8 00       JP      $00A8           
330B: 21 EB A9       LD      HL,$A9EB        
330E: 35             DEC     (HL)            
330F: C0             RET     NZ              
3310: CD C3 4C       CALL    $4CC3           
3313: D2 26 33       JP      NC,$3326        
3316: 11 09 03       LD      DE,$0309        
3319: FF             RST     0X38            
331A: 1E 0B          LD      E,$0B           
331C: FF             RST     0X38            
331D: 3A 43 08       LD      A,($0843)       
3320: 32 AC A9       LD      ($A9AC),A       
3323: C3 E7 12       JP      $12E7           
3326: CD 3A 58       CALL    $583A           
3329: 3E 00          LD      A,$00           
332B: 32 0C AD       LD      ($AD0C),A       
332E: 3E F1          LD      A,$F1           
3330: 32 0B AD       LD      ($AD0B),A       
3333: CD E1 01       CALL    $01E1           
3336: 06 00          LD      B,$00           
3338: 21 F1 01       LD      HL,$01F1        
333B: AF             XOR     A               
333C: 86             ADD     A,(HL)          
333D: 23             INC     HL              
333E: 10 FC          DJNZ    $333C           
3340: D6 19          SUB     $19             
3342: C4 11 0F       CALL    NZ,$0F11        
3345: C3 1A 0F       JP      $0F1A           
3348: 11 A7 13       LD      DE,$13A7        
334B: 68             LD      L,B             
334C: 3B             DEC     SP              
334D: 34             INC     (HL)            
334E: F1             POP     AF              
334F: 68             LD      L,B             
3350: D7             RST     0X10            
3351: F1             POP     AF              
3352: DC 0F 68       CALL    C,$680F         
3355: F1             POP     AF              
3356: 88             ADC     A,B             
3357: 57             LD      D,A             
3358: A5             AND     L               
3359: BF             CP      A               
335A: 34             INC     (HL)            
335B: D7             RST     0X10            
335C: ED B9          CPDR                    
335E: 3A AB A9       LD      A,($A9AB)       
3361: 21 8C 17       LD      HL,$178C        
3364: 06 1E          LD      B,$1E           
3366: 86             ADD     A,(HL)          
3367: 23             INC     HL              
3368: 10 FC          DJNZ    $3366           
336A: C6 2C          ADD     $2C             
336C: 32 AB A9       LD      ($A9AB),A       
336F: 3A 32 AD       LD      A,($AD32)       
3372: A7             AND     A               
3373: 11 1B AD       LD      DE,$AD1B        
3376: 3A 14 AD       LD      A,($AD14)       
3379: 28 06          JR      Z,$3381         
337B: 11 2B AD       LD      DE,$AD2B        
337E: 3A 24 AD       LD      A,($AD24)       
3381: 87             ADD     A,A             
3382: 21 8D 0F       LD      HL,$0F8D        
3385: CF             RST     0X08            
3386: 12             LD      (DE),A          
3387: 32 0B AD       LD      ($AD0B),A       
338A: 23             INC     HL              
338B: 13             INC     DE              
338C: 7E             LD      A,(HL)          
338D: 12             LD      (DE),A          
338E: 21 0C AD       LD      HL,$AD0C        
3391: BE             CP      (HL)            
3392: 77             LD      (HL),A          
3393: CC 1A 0F       CALL    Z,$0F1A         
3396: CD E1 01       CALL    $01E1           
3399: C3 1A 0F       JP      $0F1A           
339C: 3A 32 AD       LD      A,($AD32)       
339F: A7             AND     A               
33A0: 11 1B AD       LD      DE,$AD1B        
33A3: 3A 14 AD       LD      A,($AD14)       
33A6: 28 06          JR      Z,$33AE         
33A8: 11 2B AD       LD      DE,$AD2B        
33AB: 3A 24 AD       LD      A,($AD24)       
33AE: 87             ADD     A,A             
33AF: 21 8D 0F       LD      HL,$0F8D        
33B2: DF             RST     0X18            
33B3: ED A0          LDI                     
33B5: ED A0          LDI                     
33B7: C9             RET                     
33B8: 0E 00          LD      C,$00           
33BA: FD 46 31       LD      B,(IY+$31)      
33BD: 5E             LD      E,(HL)          
33BE: 2D             DEC     L               
33BF: 7E             LD      A,(HL)          
33C0: 90             SUB     B               
33C1: 30 04          JR      NC,$33C7        
33C3: ED 44          NEG                     
33C5: CB C1          SET     0,C             
33C7: 57             LD      D,A             
33C8: FD 46 00       LD      B,(IY+$00)      
33CB: 7B             LD      A,E             
33CC: 90             SUB     B               
33CD: 30 04          JR      NC,$33D3        
33CF: ED 44          NEG                     
33D1: CB C9          SET     1,C             
33D3: 5F             LD      E,A             
33D4: 08             EX      AF,AF'          
33D5: 7B             LD      A,E             
33D6: 08             EX      AF,AF'          
33D7: 92             SUB     D               
33D8: 28 35          JR      Z,$340F         
33DA: 30 02          JR      NC,$33DE        
33DC: CB D1          SET     2,C             
33DE: 2E 00          LD      L,$00           
33E0: CB 51          BIT     2,C             
33E2: 20 03          JR      NZ,$33E7        
33E4: 62             LD      H,D             
33E5: 18 02          JR      $33E9           
33E7: 63             LD      H,E             
33E8: 5A             LD      E,D             
33E9: 06 08          LD      B,$08           
33EB: AF             XOR     A               
33EC: ED 6A          ADC     HL,HL           
33EE: 7C             LD      A,H             
33EF: 38 03          JR      C,$33F4         
33F1: BB             CP      E               
33F2: 38 03          JR      C,$33F7         
33F4: 93             SUB     E               
33F5: 67             LD      H,A             
33F6: AF             XOR     A               
33F7: 3F             CCF                     
33F8: 10 F2          DJNZ    $33EC           
33FA: 45             LD      B,L             
33FB: 79             LD      A,C             
33FC: 21 15 34       LD      HL,$3415        
33FF: DF             RST     0X18            
3400: 78             LD      A,B             
3401: 0F             RRCA                    
3402: 0F             RRCA                    
3403: E6 1F          AND     $1F             
3405: CB 6E          BIT     5,(HL)          
3407: 28 04          JR      Z,$340D         
3409: 47             LD      B,A             
340A: 3E 1F          LD      A,$1F           
340C: 90             SUB     B               
340D: 86             ADD     A,(HL)          
340E: C9             RET                     
340F: 21 1D 34       LD      HL,$341D        
3412: 79             LD      A,C             
3413: CF             RST     0X08            
3414: C9             RET                     
3415: 20 40          JR      NZ,$3457        
3417: C0             RET     NZ              
3418: A0             AND     B               
3419: 00             NOP                     
341A: 60             LD      H,B             
341B: E0             RET     PO              
341C: 80             ADD     A,B             
341D: 20 60          JR      NZ,$347F        
341F: E0             RET     PO              
3420: A0             AND     B               
3421: 21 50 0C       LD      HL,$0C50        
3424: CD 8C 01       CALL    $018C           
3427: EB             EX      DE,HL           
3428: 5E             LD      E,(HL)          
3429: 23             INC     HL              
342A: 56             LD      D,(HL)          
342B: 23             INC     HL              
342C: 23             INC     HL              
342D: 3A 0C AD       LD      A,($AD0C)       
3430: C6 05          ADD     $05             
3432: E6 0F          AND     $0F             
3434: 4F             LD      C,A             
3435: C3 FF 0B       JP      $0BFF           
3438: 6F             LD      L,A             
3439: 34             INC     (HL)            
343A: 8F             ADC     A,A             
343B: 34             INC     (HL)            
343C: AF             XOR     A               
343D: 34             INC     (HL)            
343E: CF             RST     0X08            
343F: 34             INC     (HL)            
3440: EF             RST     0X28            
3441: 34             INC     (HL)            
3442: 0F             RRCA                    
3443: 35             DEC     (HL)            
3444: 2F             CPL                     
3445: 35             DEC     (HL)            
3446: 4F             LD      C,A             
3447: 35             DEC     (HL)            
3448: 6F             LD      L,A             
3449: 35             DEC     (HL)            
344A: 8F             ADC     A,A             
344B: 35             DEC     (HL)            
344C: AF             XOR     A               
344D: 35             DEC     (HL)            
344E: CF             RST     0X08            
344F: 35             DEC     (HL)            
3450: EF             RST     0X28            
3451: 35             DEC     (HL)            
3452: 0F             RRCA                    
3453: 36 2F          LD      (HL),$2F        
3455: 36 4F          LD      (HL),$4F        
3457: 36 6F          LD      (HL),$6F        
3459: 36 8F          LD      (HL),$8F        
345B: 36 11          LD      (HL),$11        
345D: A7             AND     A               
345E: 13             INC     DE              
345F: 68             LD      L,B             
3460: 3B             DEC     SP              
3461: 34             INC     (HL)            
3462: F1             POP     AF              
3463: 88             ADC     A,B             
3464: 57             LD      D,A             
3465: A5             AND     L               
3466: BF             CP      A               
3467: 34             INC     (HL)            
3468: D7             RST     0X10            
3469: F1             POP     AF              
346A: 68             LD      L,B             
346B: 3B             DEC     SP              
346C: 57             LD      D,A             
346D: BF             CP      A               
346E: B9             CP      C               
346F: 11 09 09       LD      DE,$0909        
3472: 09             ADD     HL,BC           
3473: 09             ADD     HL,BC           
3474: 09             ADD     HL,BC           
3475: 09             ADD     HL,BC           
3476: 09             ADD     HL,BC           
3477: 09             ADD     HL,BC           
3478: 09             ADD     HL,BC           
3479: 09             ADD     HL,BC           
347A: 09             ADD     HL,BC           
347B: 09             ADD     HL,BC           
347C: 09             ADD     HL,BC           
347D: 09             ADD     HL,BC           
347E: 09             ADD     HL,BC           
347F: 09             ADD     HL,BC           
3480: 09             ADD     HL,BC           
3481: 09             ADD     HL,BC           
3482: 09             ADD     HL,BC           
3483: 09             ADD     HL,BC           
3484: 09             ADD     HL,BC           
3485: 09             ADD     HL,BC           
3486: 09             ADD     HL,BC           
3487: 09             ADD     HL,BC           
3488: 09             ADD     HL,BC           
3489: 09             ADD     HL,BC           
348A: 09             ADD     HL,BC           
348B: 09             ADD     HL,BC           
348C: 09             ADD     HL,BC           
348D: 09             ADD     HL,BC           
348E: 09             ADD     HL,BC           
348F: 11 08 08       LD      DE,$0808        
3492: 08             EX      AF,AF'          
3493: 08             EX      AF,AF'          
3494: 08             EX      AF,AF'          
3495: 08             EX      AF,AF'          
3496: 08             EX      AF,AF'          
3497: 08             EX      AF,AF'          
3498: 08             EX      AF,AF'          
3499: 08             EX      AF,AF'          
349A: 08             EX      AF,AF'          
349B: 08             EX      AF,AF'          
349C: 08             EX      AF,AF'          
349D: 08             EX      AF,AF'          
349E: 08             EX      AF,AF'          
349F: 09             ADD     HL,BC           
34A0: 08             EX      AF,AF'          
34A1: 08             EX      AF,AF'          
34A2: 08             EX      AF,AF'          
34A3: 08             EX      AF,AF'          
34A4: 08             EX      AF,AF'          
34A5: 08             EX      AF,AF'          
34A6: 08             EX      AF,AF'          
34A7: 08             EX      AF,AF'          
34A8: 08             EX      AF,AF'          
34A9: 08             EX      AF,AF'          
34AA: 08             EX      AF,AF'          
34AB: 08             EX      AF,AF'          
34AC: 08             EX      AF,AF'          
34AD: 08             EX      AF,AF'          
34AE: 08             EX      AF,AF'          
34AF: 11 00 00       LD      DE,$0000        
34B2: 00             NOP                     
34B3: 00             NOP                     
34B4: 00             NOP                     
34B5: 00             NOP                     
34B6: 00             NOP                     
34B7: 00             NOP                     
34B8: 00             NOP                     
34B9: 00             NOP                     
34BA: 00             NOP                     
34BB: 00             NOP                     
34BC: 00             NOP                     
34BD: 00             NOP                     
34BE: 00             NOP                     
34BF: 00             NOP                     
34C0: 00             NOP                     
34C1: 00             NOP                     
34C2: 00             NOP                     
34C3: 00             NOP                     
34C4: 00             NOP                     
34C5: 00             NOP                     
34C6: 00             NOP                     
34C7: 00             NOP                     
34C8: 00             NOP                     
34C9: 00             NOP                     
34CA: 00             NOP                     
34CB: 00             NOP                     
34CC: 00             NOP                     
34CD: 00             NOP                     
34CE: 00             NOP                     
34CF: 11 0A 0A       LD      DE,$0A0A        
34D2: 0A             LD      A,(BC)          
34D3: 0A             LD      A,(BC)          
34D4: 0A             LD      A,(BC)          
34D5: 0A             LD      A,(BC)          
34D6: 0A             LD      A,(BC)          
34D7: 0A             LD      A,(BC)          
34D8: 0A             LD      A,(BC)          
34D9: 0A             LD      A,(BC)          
34DA: 0A             LD      A,(BC)          
34DB: 0A             LD      A,(BC)          
34DC: 0A             LD      A,(BC)          
34DD: 0A             LD      A,(BC)          
34DE: 0A             LD      A,(BC)          
34DF: 0A             LD      A,(BC)          
34E0: 0A             LD      A,(BC)          
34E1: 0A             LD      A,(BC)          
34E2: 0A             LD      A,(BC)          
34E3: 0A             LD      A,(BC)          
34E4: 0A             LD      A,(BC)          
34E5: 0A             LD      A,(BC)          
34E6: 0A             LD      A,(BC)          
34E7: 0A             LD      A,(BC)          
34E8: 0A             LD      A,(BC)          
34E9: 0A             LD      A,(BC)          
34EA: 0A             LD      A,(BC)          
34EB: 0A             LD      A,(BC)          
34EC: 0A             LD      A,(BC)          
34ED: 0A             LD      A,(BC)          
34EE: 0A             LD      A,(BC)          
34EF: 11 0B 0B       LD      DE,$0B0B        
34F2: 0B             DEC     BC              
34F3: 0B             DEC     BC              
34F4: 0B             DEC     BC              
34F5: 0B             DEC     BC              
34F6: 0B             DEC     BC              
34F7: 0B             DEC     BC              
34F8: 0B             DEC     BC              
34F9: 0B             DEC     BC              
34FA: 0B             DEC     BC              
34FB: 0B             DEC     BC              
34FC: 0B             DEC     BC              
34FD: 0B             DEC     BC              
34FE: 0B             DEC     BC              
34FF: 0B             DEC     BC              
3500: 0B             DEC     BC              
3501: 0B             DEC     BC              
3502: 0B             DEC     BC              
3503: 0B             DEC     BC              
3504: 0B             DEC     BC              
3505: 0B             DEC     BC              
3506: 0B             DEC     BC              
3507: 0B             DEC     BC              
3508: 0B             DEC     BC              
3509: 0B             DEC     BC              
350A: 0B             DEC     BC              
350B: 0B             DEC     BC              
350C: 0B             DEC     BC              
350D: 0B             DEC     BC              
350E: 0B             DEC     BC              
350F: 11 10 10       LD      DE,$1010        
3512: 10 10          DJNZ    $3524           
3514: 10 10          DJNZ    $3526           
3516: 10 10          DJNZ    $3528           
3518: 10 10          DJNZ    $352A           
351A: 10 10          DJNZ    $352C           
351C: 10 10          DJNZ    $352E           
351E: 10 10          DJNZ    $3530           
3520: 10 10          DJNZ    $3532           
3522: 10 10          DJNZ    $3534           
3524: 10 10          DJNZ    $3536           
3526: 10 10          DJNZ    $3538           
3528: 10 10          DJNZ    $353A           
352A: 10 10          DJNZ    $353C           
352C: 10 10          DJNZ    $353E           
352E: 10 11          DJNZ    $3541           
3530: 10 10          DJNZ    $3542           
3532: 10 10          DJNZ    $3544           
3534: 10 10          DJNZ    $3546           
3536: 10 10          DJNZ    $3548           
3538: 10 10          DJNZ    $354A           
353A: 10 10          DJNZ    $354C           
353C: 10 10          DJNZ    $354E           
353E: 10 10          DJNZ    $3550           
3540: 10 10          DJNZ    $3552           
3542: 10 10          DJNZ    $3554           
3544: 10 10          DJNZ    $3556           
3546: 10 10          DJNZ    $3558           
3548: 10 10          DJNZ    $355A           
354A: 10 10          DJNZ    $355C           
354C: 10 10          DJNZ    $355E           
354E: 0D             DEC     C               
354F: 11 10 10       LD      DE,$1010        
3552: 10 10          DJNZ    $3564           
3554: 10 10          DJNZ    $3566           
3556: 10 10          DJNZ    $3568           
3558: 10 10          DJNZ    $356A           
355A: 10 10          DJNZ    $356C           
355C: 10 10          DJNZ    $356E           
355E: 10 10          DJNZ    $3570           
3560: 10 10          DJNZ    $3572           
3562: 10 10          DJNZ    $3574           
3564: 10 10          DJNZ    $3576           
3566: 10 10          DJNZ    $3578           
3568: 10 10          DJNZ    $357A           
356A: 10 10          DJNZ    $357C           
356C: 10 0C          DJNZ    $357A           
356E: 0D             DEC     C               
356F: 11 10 10       LD      DE,$1010        
3572: 10 10          DJNZ    $3584           
3574: 10 10          DJNZ    $3586           
3576: 10 10          DJNZ    $3588           
3578: 10 10          DJNZ    $358A           
357A: 10 10          DJNZ    $358C           
357C: 10 10          DJNZ    $358E           
357E: 10 10          DJNZ    $3590           
3580: 10 10          DJNZ    $3592           
3582: 10 10          DJNZ    $3594           
3584: 10 10          DJNZ    $3596           
3586: 10 10          DJNZ    $3598           
3588: 10 10          DJNZ    $359A           
358A: 10 10          DJNZ    $359C           
358C: 0C             INC     C               
358D: 0D             DEC     C               
358E: 0D             DEC     C               
358F: 11 09 09       LD      DE,$0909        
3592: 09             ADD     HL,BC           
3593: 09             ADD     HL,BC           
3594: 09             ADD     HL,BC           
3595: 09             ADD     HL,BC           
3596: 09             ADD     HL,BC           
3597: 09             ADD     HL,BC           
3598: 09             ADD     HL,BC           
3599: 09             ADD     HL,BC           
359A: 09             ADD     HL,BC           
359B: 09             ADD     HL,BC           
359C: 09             ADD     HL,BC           
359D: 09             ADD     HL,BC           
359E: 09             ADD     HL,BC           
359F: 09             ADD     HL,BC           
35A0: 09             ADD     HL,BC           
35A1: 09             ADD     HL,BC           
35A2: 09             ADD     HL,BC           
35A3: 09             ADD     HL,BC           
35A4: 09             ADD     HL,BC           
35A5: 09             ADD     HL,BC           
35A6: 09             ADD     HL,BC           
35A7: 09             ADD     HL,BC           
35A8: 09             ADD     HL,BC           
35A9: 09             ADD     HL,BC           
35AA: 09             ADD     HL,BC           
35AB: 09             ADD     HL,BC           
35AC: 10 10          DJNZ    $35BE           
35AE: 10 11          DJNZ    $35C1           
35B0: 08             EX      AF,AF'          
35B1: 08             EX      AF,AF'          
35B2: 08             EX      AF,AF'          
35B3: 08             EX      AF,AF'          
35B4: 08             EX      AF,AF'          
35B5: 08             EX      AF,AF'          
35B6: 08             EX      AF,AF'          
35B7: 08             EX      AF,AF'          
35B8: 08             EX      AF,AF'          
35B9: 08             EX      AF,AF'          
35BA: 08             EX      AF,AF'          
35BB: 08             EX      AF,AF'          
35BC: 08             EX      AF,AF'          
35BD: 08             EX      AF,AF'          
35BE: 08             EX      AF,AF'          
35BF: 08             EX      AF,AF'          
35C0: 08             EX      AF,AF'          
35C1: 08             EX      AF,AF'          
35C2: 08             EX      AF,AF'          
35C3: 08             EX      AF,AF'          
35C4: 08             EX      AF,AF'          
35C5: 08             EX      AF,AF'          
35C6: 08             EX      AF,AF'          
35C7: 08             EX      AF,AF'          
35C8: 08             EX      AF,AF'          
35C9: 08             EX      AF,AF'          
35CA: 08             EX      AF,AF'          
35CB: 08             EX      AF,AF'          
35CC: 10 10          DJNZ    $35DE           
35CE: 10 11          DJNZ    $35E1           
35D0: 00             NOP                     
35D1: 00             NOP                     
35D2: 00             NOP                     
35D3: 00             NOP                     
35D4: 00             NOP                     
35D5: 00             NOP                     
35D6: 00             NOP                     
35D7: 00             NOP                     
35D8: 00             NOP                     
35D9: 00             NOP                     
35DA: 00             NOP                     
35DB: 00             NOP                     
35DC: 00             NOP                     
35DD: 00             NOP                     
35DE: 00             NOP                     
35DF: 00             NOP                     
35E0: 00             NOP                     
35E1: 00             NOP                     
35E2: 00             NOP                     
35E3: 00             NOP                     
35E4: 00             NOP                     
35E5: 00             NOP                     
35E6: 00             NOP                     
35E7: 00             NOP                     
35E8: 00             NOP                     
35E9: 00             NOP                     
35EA: 00             NOP                     
35EB: 00             NOP                     
35EC: 10 10          DJNZ    $35FE           
35EE: 10 11          DJNZ    $3601           
35F0: 0A             LD      A,(BC)          
35F1: 0A             LD      A,(BC)          
35F2: 0A             LD      A,(BC)          
35F3: 0A             LD      A,(BC)          
35F4: 0A             LD      A,(BC)          
35F5: 0A             LD      A,(BC)          
35F6: 0A             LD      A,(BC)          
35F7: 0A             LD      A,(BC)          
35F8: 0A             LD      A,(BC)          
35F9: 0A             LD      A,(BC)          
35FA: 0A             LD      A,(BC)          
35FB: 0A             LD      A,(BC)          
35FC: 0A             LD      A,(BC)          
35FD: 0A             LD      A,(BC)          
35FE: 0A             LD      A,(BC)          
35FF: 0A             LD      A,(BC)          
3600: 0A             LD      A,(BC)          
3601: 0A             LD      A,(BC)          
3602: 0A             LD      A,(BC)          
3603: 0A             LD      A,(BC)          
3604: 0A             LD      A,(BC)          
3605: 0A             LD      A,(BC)          
3606: 0A             LD      A,(BC)          
3607: 0A             LD      A,(BC)          
3608: 0A             LD      A,(BC)          
3609: 0A             LD      A,(BC)          
360A: 0A             LD      A,(BC)          
360B: 0A             LD      A,(BC)          
360C: 10 10          DJNZ    $361E           
360E: 10 11          DJNZ    $3621           
3610: 0B             DEC     BC              
3611: 0B             DEC     BC              
3612: 0B             DEC     BC              
3613: 0B             DEC     BC              
3614: 0B             DEC     BC              
3615: 0B             DEC     BC              
3616: 0B             DEC     BC              
3617: 0B             DEC     BC              
3618: 0B             DEC     BC              
3619: 0B             DEC     BC              
361A: 0B             DEC     BC              
361B: 0B             DEC     BC              
361C: 0B             DEC     BC              
361D: 0B             DEC     BC              
361E: 0B             DEC     BC              
361F: 0B             DEC     BC              
3620: 0B             DEC     BC              
3621: 0B             DEC     BC              
3622: 0B             DEC     BC              
3623: 0B             DEC     BC              
3624: 0B             DEC     BC              
3625: 0B             DEC     BC              
3626: 0B             DEC     BC              
3627: 0B             DEC     BC              
3628: 0B             DEC     BC              
3629: 0B             DEC     BC              
362A: 0B             DEC     BC              
362B: 0B             DEC     BC              
362C: 10 10          DJNZ    $363E           
362E: 10 11          DJNZ    $3641           
3630: 10 10          DJNZ    $3642           
3632: 10 10          DJNZ    $3644           
3634: 10 10          DJNZ    $3646           
3636: 10 10          DJNZ    $3648           
3638: 10 10          DJNZ    $364A           
363A: 10 10          DJNZ    $364C           
363C: 10 10          DJNZ    $364E           
363E: 10 10          DJNZ    $3650           
3640: 10 10          DJNZ    $3652           
3642: 10 10          DJNZ    $3654           
3644: 10 10          DJNZ    $3656           
3646: 10 10          DJNZ    $3658           
3648: 10 10          DJNZ    $365A           
364A: 10 10          DJNZ    $365C           
364C: 10 10          DJNZ    $365E           
364E: 10 11          DJNZ    $3661           
3650: 10 10          DJNZ    $3662           
3652: 10 10          DJNZ    $3664           
3654: 10 10          DJNZ    $3666           
3656: 10 10          DJNZ    $3668           
3658: 10 10          DJNZ    $366A           
365A: 10 10          DJNZ    $366C           
365C: 10 10          DJNZ    $366E           
365E: 10 10          DJNZ    $3670           
3660: 10 10          DJNZ    $3672           
3662: 10 10          DJNZ    $3674           
3664: 10 10          DJNZ    $3676           
3666: 10 10          DJNZ    $3678           
3668: 10 10          DJNZ    $367A           
366A: 10 0D          DJNZ    $3679           
366C: 10 10          DJNZ    $367E           
366E: 10 11          DJNZ    $3681           
3670: 10 10          DJNZ    $3682           
3672: 10 10          DJNZ    $3684           
3674: 10 10          DJNZ    $3686           
3676: 10 10          DJNZ    $3688           
3678: 10 10          DJNZ    $368A           
367A: 10 10          DJNZ    $368C           
367C: 10 10          DJNZ    $368E           
367E: 10 10          DJNZ    $3690           
3680: 10 10          DJNZ    $3692           
3682: 10 10          DJNZ    $3694           
3684: 10 10          DJNZ    $3696           
3686: 10 10          DJNZ    $3698           
3688: 10 10          DJNZ    $369A           
368A: 10 10          DJNZ    $369C           
368C: 10 10          DJNZ    $369E           
368E: 10 11          DJNZ    $36A1           
3690: 10 10          DJNZ    $36A2           
3692: 10 10          DJNZ    $36A4           
3694: 10 10          DJNZ    $36A6           
3696: 10 10          DJNZ    $36A8           
3698: 10 10          DJNZ    $36AA           
369A: 10 10          DJNZ    $36AC           
369C: 10 10          DJNZ    $36AE           
369E: 10 10          DJNZ    $36B0           
36A0: 10 10          DJNZ    $36B2           
36A2: 10 10          DJNZ    $36B4           
36A4: 10 10          DJNZ    $36B6           
36A6: 10 10          DJNZ    $36B8           
36A8: 10 10          DJNZ    $36BA           
36AA: 10 0D          DJNZ    $36B9           
36AC: 10 10          DJNZ    $36BE           
36AE: 10 3A          DJNZ    $36EA           
36B0: C6 AC          ADD     $AC             
36B2: A7             AND     A               
36B3: C0             RET     NZ              
36B4: 3A 04 AD       LD      A,($AD04)       
36B7: FE 04          CP      $04             
36B9: CA 6E 38       JP      Z,$386E         
36BC: 21 05 AD       LD      HL,$AD05        
36BF: 3A 06 AD       LD      A,($AD06)       
36C2: E6 0F          AND     $0F             
36C4: FE 07          CP      $07             
36C6: CA 55 38       JP      Z,$3855         
36C9: DA BD 37       JP      C,$37BD         
36CC: FE 09          CP      $09             
36CE: DA 9F 37       JP      C,$379F         
36D1: 7E             LD      A,(HL)          
36D2: A7             AND     A               
36D3: C0             RET     NZ              
36D4: CD 4B 4B       CALL    $4B4B           
36D7: 0F             RRCA                    
36D8: 3A 04 AD       LD      A,($AD04)       
36DB: 8F             ADC     A,A             
36DC: 21 C2 AC       LD      HL,$ACC2        
36DF: 36 FF          LD      (HL),$FF        
36E1: 23             INC     HL              
36E2: 77             LD      (HL),A          
36E3: 3A 02 A8       LD      A,($A802)       
36E6: C6 08          ADD     $08             
36E8: 0F             RRCA                    
36E9: 0F             RRCA                    
36EA: 0F             RRCA                    
36EB: 0F             RRCA                    
36EC: E6 0F          AND     $0F             
36EE: 21 D9 38       LD      HL,$38D9        
36F1: DF             RST     0X18            
36F2: 4E             LD      C,(HL)          
36F3: 3A C3 AC       LD      A,($ACC3)       
36F6: 87             ADD     A,A             
36F7: 87             ADD     A,A             
36F8: 87             ADD     A,A             
36F9: 87             ADD     A,A             
36FA: 21 7B 39       LD      HL,$397B        
36FD: DF             RST     0X18            
36FE: EB             EX      DE,HL           
36FF: 3A C1 AC       LD      A,($ACC1)       
3702: 47             LD      B,A             
3703: 3A 02 AD       LD      A,($AD02)       
3706: A7             AND     A               
3707: 20 02          JR      NZ,$370B        
3709: 06 05          LD      B,$05           
370B: AF             XOR     A               
370C: 32 11 A8       LD      ($A811),A       
370F: DD 21 50 A8    LD      IX,$A850        
3713: FD 21 1A AA    LD      IY,$AA1A        
3717: DD 7E 00       LD      A,(IX+$00)      
371A: A7             AND     A               
371B: C2 68 37       JP      NZ,$3768        
371E: 1A             LD      A,(DE)          
371F: 81             ADD     A,C             
3720: 87             ADD     A,A             
3721: 21 E9 38       LD      HL,$38E9        
3724: CF             RST     0X08            
3725: FD 77 31       LD      (IY+$31),A      
3728: 23             INC     HL              
3729: 7E             LD      A,(HL)          
372A: FD 77 00       LD      (IY+$00),A      
372D: 3A 02 A8       LD      A,($A802)       
3730: C6 80          ADD     $80             
3732: DD 77 01       LD      (IX+$01),A      
3735: DD 77 02       LD      (IX+$02),A      
3738: CD 2D 38       CALL    $382D           
373B: C6 09          ADD     $09             
373D: DD 77 0A       LD      (IX+$0A),A      
3740: 13             INC     DE              
3741: 1A             LD      A,(DE)          
3742: DD 77 0E       LD      (IX+$0E),A      
3745: 13             INC     DE              
3746: DD 36 03 00    LD      (IX+$03),$00    
374A: DD 36 05 00    LD      (IX+$05),$00    
374E: DD 36 09 20    LD      (IX+$09),$20    
3752: D9             EXX                     
3753: CD 3A 32       CALL    $323A           
3756: D9             EXX                     
3757: DD 36 00 FE    LD      (IX+$00),$FE    
375B: DD 7E 0E       LD      A,(IX+$0E)      
375E: A7             AND     A               
375F: 20 03          JR      NZ,$3764        
3761: DD 34 00       INC     (IX+$00)        
3764: 21 11 A8       LD      HL,$A811        
3767: 34             INC     (HL)            
3768: EB             EX      DE,HL           
3769: 11 10 00       LD      DE,$0010        
376C: DD 19          ADD     IX,DE           
376E: FD 23          INC     IY              
3770: FD 23          INC     IY              
3772: EB             EX      DE,HL           
3773: 10 A2          DJNZ    $3717           
3775: AF             XOR     A               
3776: 32 C2 AC       LD      ($ACC2),A       
3779: 3E E4          LD      A,$E4           
377B: 32 12 A8       LD      ($A812),A       
377E: 21 11 A8       LD      HL,$A811        
3781: 7E             LD      A,(HL)          
3782: FE 05          CP      $05             
3784: D2 17 58       JP      NC,$5817        
3787: 21 C1 AC       LD      HL,$ACC1        
378A: BE             CP      (HL)            
378B: 7E             LD      A,(HL)          
378C: 32 11 A8       LD      ($A811),A       
378F: D2 17 58       JP      NC,$5817        
3792: C9             RET                     
3793: 06 05          LD      B,$05           
3795: DD 21 90 A8    LD      IX,$A890        
3799: FD 21 22 AA    LD      IY,$AA22        
379D: 18 37          JR      $37D6           
379F: 7E             LD      A,(HL)          
37A0: A7             AND     A               
37A1: 28 03          JR      Z,$37A6         
37A3: FE 30          CP      $30             
37A5: C0             RET     NZ              
37A6: 21 50 A8       LD      HL,$A850        
37A9: 11 10 00       LD      DE,$0010        
37AC: 01 00 07       LD      BC,$0700        
37AF: 7E             LD      A,(HL)          
37B0: A7             AND     A               
37B1: 28 01          JR      Z,$37B4         
37B3: 0C             INC     C               
37B4: 19             ADD     HL,DE           
37B5: 10 F8          DJNZ    $37AF           
37B7: 79             LD      A,C             
37B8: FE 02          CP      $02             
37BA: D0             RET     NC              
37BB: 18 07          JR      $37C4           
37BD: 7E             LD      A,(HL)          
37BE: A7             AND     A               
37BF: 28 03          JR      Z,$37C4         
37C1: FE 30          CP      $30             
37C3: C0             RET     NZ              
37C4: 3A 02 AD       LD      A,($AD02)       
37C7: A7             AND     A               
37C8: 28 C9          JR      Z,$3793         
37CA: 3A C1 AC       LD      A,($ACC1)       
37CD: 47             LD      B,A             
37CE: DD 21 B0 A8    LD      IX,$A8B0        
37D2: FD 21 26 AA    LD      IY,$AA26        
37D6: DD 7E 00       LD      A,(IX+$00)      
37D9: A7             AND     A               
37DA: C2 47 38       JP      NZ,$3847        
37DD: DD 35 00       DEC     (IX+$00)        
37E0: 3A 02 A8       LD      A,($A802)       
37E3: 0F             RRCA                    
37E4: 0F             RRCA                    
37E5: E6 3F          AND     $3F             
37E7: 4F             LD      C,A             
37E8: CD 4B 4B       CALL    $4B4B           
37EB: E6 0F          AND     $0F             
37ED: D6 08          SUB     $08             
37EF: 81             ADD     A,C             
37F0: E6 3F          AND     $3F             
37F2: 21 FB 39       LD      HL,$39FB        
37F5: CF             RST     0X08            
37F6: 87             ADD     A,A             
37F7: 87             ADD     A,A             
37F8: 21 3B 3A       LD      HL,$3A3B        
37FB: CF             RST     0X08            
37FC: FD 77 31       LD      (IY+$31),A      
37FF: 23             INC     HL              
3800: 7E             LD      A,(HL)          
3801: FD 77 00       LD      (IY+$00),A      
3804: 3A 02 A8       LD      A,($A802)       
3807: C6 80          ADD     $80             
3809: DD 77 01       LD      (IX+$01),A      
380C: DD 77 02       LD      (IX+$02),A      
380F: CD 2D 38       CALL    $382D           
3812: DD 77 0A       LD      (IX+$0A),A      
3815: AF             XOR     A               
3816: 32 C5 AC       LD      ($ACC5),A       
3819: DD 36 03 00    LD      (IX+$03),$00    
381D: DD 36 05 00    LD      (IX+$05),$00    
3821: DD 36 09 20    LD      (IX+$09),$20    
3825: CD 3A 32       CALL    $323A           
3828: DD 36 0E 00    LD      (IX+$0E),$00    
382C: C9             RET                     
382D: CD 4B 4B       CALL    $4B4B           
3830: 21 C4 AC       LD      HL,$ACC4        
3833: BE             CP      (HL)            
3834: 30 0C          JR      NC,$3842        
3836: 21 CF A9       LD      HL,$A9CF        
3839: 7E             LD      A,(HL)          
383A: 3C             INC     A               
383B: FE 05          CP      $05             
383D: 38 01          JR      C,$3840         
383F: AF             XOR     A               
3840: 77             LD      (HL),A          
3841: C9             RET                     
3842: E6 03          AND     $03             
3844: C6 05          ADD     $05             
3846: C9             RET                     
3847: 11 F0 FF       LD      DE,$FFF0        
384A: DD 19          ADD     IX,DE           
384C: FD 2B          DEC     IY              
384E: FD 2B          DEC     IY              
3850: 05             DEC     B               
3851: C2 D6 37       JP      NZ,$37D6        
3854: C9             RET                     
3855: 7E             LD      A,(HL)          
3856: A7             AND     A               
3857: C0             RET     NZ              
3858: DD 21 50 A8    LD      IX,$A850        
385C: 11 10 00       LD      DE,$0010        
385F: 06 05          LD      B,$05           
3861: DD 36 08 11    LD      (IX+$08),$11    
3865: DD 36 09 00    LD      (IX+$09),$00    
3869: DD 19          ADD     IX,DE           
386B: 10 F4          DJNZ    $3861           
386D: C9             RET                     
386E: DD 21 50 A8    LD      IX,$A850        
3872: FD 21 1A AA    LD      IY,$AA1A        
3876: 3A C1 AC       LD      A,($ACC1)       
3879: 47             LD      B,A             
387A: 3A 0D AD       LD      A,($AD0D)       
387D: A7             AND     A               
387E: 28 02          JR      Z,$3882         
3880: 06 05          LD      B,$05           
3882: C5             PUSH    BC              
3883: DD 7E 00       LD      A,(IX+$00)      
3886: A7             AND     A               
3887: C2 C0 38       JP      NZ,$38C0        
388A: CD 4B 4B       CALL    $4B4B           
388D: E6 FC          AND     $FC             
388F: 21 3B 3A       LD      HL,$3A3B        
3892: CF             RST     0X08            
3893: FD 77 31       LD      (IY+$31),A      
3896: 23             INC     HL              
3897: 7E             LD      A,(HL)          
3898: FD 77 00       LD      (IY+$00),A      
389B: 23             INC     HL              
389C: 7E             LD      A,(HL)          
389D: DD 77 01       LD      (IX+$01),A      
38A0: DD 77 02       LD      (IX+$02),A      
38A3: 3A C1 AC       LD      A,($ACC1)       
38A6: 90             SUB     B               
38A7: 21 D2 38       LD      HL,$38D2        
38AA: CF             RST     0X08            
38AB: DD 77 0A       LD      (IX+$0A),A      
38AE: DD 36 09 20    LD      (IX+$09),$20    
38B2: CD 3A 32       CALL    $323A           
38B5: DD 36 04 01    LD      (IX+$04),$01    
38B9: DD 36 0E 00    LD      (IX+$0E),$00    
38BD: DD 35 00       DEC     (IX+$00)        
38C0: 11 10 00       LD      DE,$0010        
38C3: DD 19          ADD     IX,DE           
38C5: FD 23          INC     IY              
38C7: FD 23          INC     IY              
38C9: C1             POP     BC              
38CA: 10 B6          DJNZ    $3882           
38CC: 3E E4          LD      A,$E4           
38CE: 32 12 A8       LD      ($A812),A       
38D1: C9             RET                     
38D2: 0A             LD      A,(BC)          
38D3: 0B             DEC     BC              
38D4: 0D             DEC     C               
38D5: 0E 0F          LD      C,$0F           
38D7: 09             ADD     HL,BC           
38D8: 0C             INC     C               
38D9: 08             EX      AF,AF'          
38DA: 0C             INC     C               
38DB: 0F             RRCA                    
38DC: 13             INC     DE              
38DD: 16 1A          LD      D,$1A           
38DF: 1D             DEC     E               
38E0: 21 24 28       LD      HL,$2824        
38E3: 2B             DEC     HL              
38E4: 2F             CPL                     
38E5: 33             INC     SP              
38E6: 37             SCF                     
38E7: 3A 3D F0       LD      A,($F03D)       
38EA: 10 F0          DJNZ    $38DC           
38EC: 20 F0          JR      NZ,$38DE        
38EE: 30 F0          JR      NC,$38E0        
38F0: 40             LD      B,B             
38F1: F0             RET     P               
38F2: 50             LD      D,B             
38F3: F0             RET     P               
38F4: 60             LD      H,B             
38F5: F0             RET     P               
38F6: 70             LD      (HL),B          
38F7: F0             RET     P               
38F8: 80             ADD     A,B             
38F9: F0             RET     P               
38FA: 90             SUB     B               
38FB: F0             RET     P               
38FC: A0             AND     B               
38FD: F0             RET     P               
38FE: B0             OR      B               
38FF: F0             RET     P               
3900: C0             RET     NZ              
3901: F0             RET     P               
3902: D0             RET     NC              
3903: F0             RET     P               
3904: E0             RET     PO              
3905: F0             RET     P               
3906: F0             RET     P               
3907: E0             RET     PO              
3908: F8             RET     M               
3909: D0             RET     NC              
390A: F8             RET     M               
390B: C0             RET     NZ              
390C: F8             RET     M               
390D: B0             OR      B               
390E: F8             RET     M               
390F: A0             AND     B               
3910: F8             RET     M               
3911: 90             SUB     B               
3912: F8             RET     M               
3913: 80             ADD     A,B             
3914: F8             RET     M               
3915: 70             LD      (HL),B          
3916: F8             RET     M               
3917: 60             LD      H,B             
3918: F8             RET     M               
3919: 50             LD      D,B             
391A: F8             RET     M               
391B: 40             LD      B,B             
391C: F8             RET     M               
391D: 30 F8          JR      NC,$3917        
391F: 20 F8          JR      NZ,$3919        
3921: 10 F8          DJNZ    $391B           
3923: 00             NOP                     
3924: F0             RET     P               
3925: 00             NOP                     
3926: E0             RET     PO              
3927: 00             NOP                     
3928: D0             RET     NC              
3929: 00             NOP                     
392A: C0             RET     NZ              
392B: 00             NOP                     
392C: B0             OR      B               
392D: 00             NOP                     
392E: A0             AND     B               
392F: 00             NOP                     
3930: 90             SUB     B               
3931: 00             NOP                     
3932: 80             ADD     A,B             
3933: 00             NOP                     
3934: 70             LD      (HL),B          
3935: 00             NOP                     
3936: 60             LD      H,B             
3937: 00             NOP                     
3938: 50             LD      D,B             
3939: 00             NOP                     
393A: 40             LD      B,B             
393B: 00             NOP                     
393C: 30 00          JR      NC,$393E        
393E: 20 00          JR      NZ,$3940        
3940: 10 10          DJNZ    $3952           
3942: 10 20          DJNZ    $3964           
3944: 10 30          DJNZ    $3976           
3946: 10 40          DJNZ    $3988           
3948: 10 50          DJNZ    $399A           
394A: 10 60          DJNZ    $39AC           
394C: 10 70          DJNZ    $39BE           
394E: 10 80          DJNZ    $38D0           
3950: 10 90          DJNZ    $38E2           
3952: 10 A0          DJNZ    $38F4           
3954: 10 B0          DJNZ    $3906           
3956: 10 C0          DJNZ    $3918           
3958: 10 D0          DJNZ    $392A           
395A: 10 E0          DJNZ    $393C           
395C: 10 F0          DJNZ    $394E           
395E: 10 F0          DJNZ    $3950           
3960: 20 F0          JR      NZ,$3952        
3962: 30 F0          JR      NC,$3954        
3964: 40             LD      B,B             
3965: F0             RET     P               
3966: 50             LD      D,B             
3967: F0             RET     P               
3968: 60             LD      H,B             
3969: F0             RET     P               
396A: 70             LD      (HL),B          
396B: F0             RET     P               
396C: 80             ADD     A,B             
396D: F0             RET     P               
396E: 90             SUB     B               
396F: F0             RET     P               
3970: A0             AND     B               
3971: F0             RET     P               
3972: B0             OR      B               
3973: F0             RET     P               
3974: C0             RET     NZ              
3975: F0             RET     P               
3976: D0             RET     NC              
3977: F0             RET     P               
3978: E0             RET     PO              
3979: F0             RET     P               
397A: F0             RET     P               
397B: 00             NOP                     
397C: 01 01 11       LD      BC,$1101        
397F: FF             RST     0X38            
3980: 11 02 21       LD      DE,$2102        
3983: FE 21          CP      $21             
3985: 03             INC     BC              
3986: 31 FD 31       LD      SP,$31FD        
3989: 00             NOP                     
398A: 00             NOP                     
398B: 00             NOP                     
398C: 11 01 01       LD      DE,$0101        
398F: FF             RST     0X38            
3990: 01 02 11       LD      BC,$1102        
3993: FE 11          CP      $11             
3995: 03             INC     BC              
3996: 21 FD 21       LD      HL,$21FD        
3999: 00             NOP                     
399A: 00             NOP                     
399B: 00             NOP                     
399C: 01 02 11       LD      BC,$1102        
399F: FE 11          CP      $11             
39A1: 03             INC     BC              
39A2: 21 FD 21       LD      HL,$21FD        
39A5: 04             INC     B               
39A6: 31 FC 31       LD      SP,$31FC        
39A9: 00             NOP                     
39AA: 00             NOP                     
39AB: 00             NOP                     
39AC: 31 03 01       LD      SP,$0103        
39AF: FD                                  
39B0: 01 04 11       LD      BC,$1104        
39B3: FC 11 03       CALL    M,$0311         
39B6: 11 FD 11       LD      DE,$11FD        
39B9: 00             NOP                     
39BA: 00             NOP                     
39BB: 00             NOP                     
39BC: 01 03 01       LD      BC,$0103        
39BF: FD                                  
39C0: 01 04 11       LD      BC,$1104        
39C3: FC 11 05       CALL    M,$0511         
39C6: 21 FB 21       LD      HL,$21FB        
39C9: 00             NOP                     
39CA: 00             NOP                     
39CB: 00             NOP                     
39CC: 01 03 11       LD      BC,$1103        
39CF: FD                                  
39D0: 11 00 21       LD      DE,$2100        
39D3: 03             INC     BC              
39D4: 21 FD 21       LD      HL,$21FD        
39D7: 00             NOP                     
39D8: 31 00 00       LD      SP,$0000        
39DB: 03             INC     BC              
39DC: 01 FD 01       LD      BC,$01FD        
39DF: 03             INC     BC              
39E0: 11 FD 11       LD      DE,$11FD        
39E3: 05             DEC     B               
39E4: 11 FB 11       LD      DE,$11FB        
39E7: 00             NOP                     
39E8: 29             ADD     HL,HL           
39E9: 00             NOP                     
39EA: 00             NOP                     
39EB: 00             NOP                     
39EC: 01 03 11       LD      BC,$1103        
39EF: FD                                  
39F0: 11 05 21       LD      DE,$2105        
39F3: FB             EI                      
39F4: 21 03 31       LD      HL,$3103        
39F7: FD                                  
39F8: 31 00 00       LD      SP,$0000        
39FB: 08             EX      AF,AF'          
39FC: 09             ADD     HL,BC           
39FD: 0A             LD      A,(BC)          
39FE: 0B             DEC     BC              
39FF: 0C             INC     C               
3A00: 0D             DEC     C               
3A01: 0D             DEC     C               
3A02: 0E 0F          LD      C,$0F           
3A04: 10 11          DJNZ    $3A17           
3A06: 12             LD      (DE),A          
3A07: 13             INC     DE              
3A08: 14             INC     D               
3A09: 14             INC     D               
3A0A: 15             DEC     D               
3A0B: 16 17          LD      D,$17           
3A0D: 18 19          JR      $3A28           
3A0F: 1A             LD      A,(DE)          
3A10: 1B             DEC     DE              
3A11: 1B             DEC     DE              
3A12: 1C             INC     E               
3A13: 1D             DEC     E               
3A14: 1E 1F          LD      E,$1F           
3A16: 20 21          JR      NZ,$3A39        
3A18: 22 22 23       LD      ($2322),HL      
3A1B: 24             INC     H               
3A1C: 25             DEC     H               
3A1D: 26 27          LD      H,$27           
3A1F: 28 29          JR      Z,$3A4A         
3A21: 29             ADD     HL,HL           
3A22: 2A 2B 2C       LD      HL,($2C2B)      
3A25: 2D             DEC     L               
3A26: 2E 2F          LD      L,$2F           
3A28: 30 31          JR      NC,$3A5B        
3A2A: 32 33 34       LD      ($3433),A       
3A2D: 35             DEC     (HL)            
3A2E: 36 37          LD      (HL),$37        
3A30: 38 38          JR      C,$3A6A         
3A32: 39             ADD     HL,SP           
3A33: 00             NOP                     
3A34: 01 02 03       LD      BC,$0302        
3A37: 04             INC     B               
3A38: 05             DEC     B               
3A39: 06 07          LD      B,$07           
3A3B: F0             RET     P               
3A3C: 10 60          DJNZ    $3A9E           
3A3E: 00             NOP                     
3A3F: F0             RET     P               
3A40: 20 80          JR      NZ,$39C2        
3A42: 00             NOP                     
3A43: F0             RET     P               
3A44: 30 80          JR      NC,$39C6        
3A46: 00             NOP                     
3A47: F0             RET     P               
3A48: 40             LD      B,B             
3A49: 80             ADD     A,B             
3A4A: 00             NOP                     
3A4B: F0             RET     P               
3A4C: 50             LD      D,B             
3A4D: 80             ADD     A,B             
3A4E: 00             NOP                     
3A4F: F0             RET     P               
3A50: 60             LD      H,B             
3A51: 80             ADD     A,B             
3A52: 00             NOP                     
3A53: F0             RET     P               
3A54: 70             LD      (HL),B          
3A55: 80             ADD     A,B             
3A56: 00             NOP                     
3A57: F0             RET     P               
3A58: 80             ADD     A,B             
3A59: 80             ADD     A,B             
3A5A: 00             NOP                     
3A5B: F0             RET     P               
3A5C: 90             SUB     B               
3A5D: 80             ADD     A,B             
3A5E: 00             NOP                     
3A5F: F0             RET     P               
3A60: A0             AND     B               
3A61: 80             ADD     A,B             
3A62: 00             NOP                     
3A63: F0             RET     P               
3A64: B0             OR      B               
3A65: 80             ADD     A,B             
3A66: 00             NOP                     
3A67: F0             RET     P               
3A68: C0             RET     NZ              
3A69: 80             ADD     A,B             
3A6A: 00             NOP                     
3A6B: F0             RET     P               
3A6C: D0             RET     NC              
3A6D: 80             ADD     A,B             
3A6E: 00             NOP                     
3A6F: F0             RET     P               
3A70: E0             RET     PO              
3A71: 80             ADD     A,B             
3A72: 00             NOP                     
3A73: F0             RET     P               
3A74: F0             RET     P               
3A75: A0             AND     B               
3A76: 00             NOP                     
3A77: E0             RET     PO              
3A78: F8             RET     M               
3A79: C0             RET     NZ              
3A7A: 00             NOP                     
3A7B: D0             RET     NC              
3A7C: F8             RET     M               
3A7D: C0             RET     NZ              
3A7E: 00             NOP                     
3A7F: C0             RET     NZ              
3A80: F8             RET     M               
3A81: C0             RET     NZ              
3A82: 00             NOP                     
3A83: B0             OR      B               
3A84: F8             RET     M               
3A85: C0             RET     NZ              
3A86: 00             NOP                     
3A87: A0             AND     B               
3A88: F8             RET     M               
3A89: C0             RET     NZ              
3A8A: 00             NOP                     
3A8B: 90             SUB     B               
3A8C: F8             RET     M               
3A8D: C0             RET     NZ              
3A8E: 00             NOP                     
3A8F: 80             ADD     A,B             
3A90: F8             RET     M               
3A91: C0             RET     NZ              
3A92: 00             NOP                     
3A93: 70             LD      (HL),B          
3A94: F8             RET     M               
3A95: C0             RET     NZ              
3A96: 00             NOP                     
3A97: 60             LD      H,B             
3A98: F8             RET     M               
3A99: C0             RET     NZ              
3A9A: 00             NOP                     
3A9B: 50             LD      D,B             
3A9C: F8             RET     M               
3A9D: C0             RET     NZ              
3A9E: 00             NOP                     
3A9F: 40             LD      B,B             
3AA0: F8             RET     M               
3AA1: C0             RET     NZ              
3AA2: 00             NOP                     
3AA3: 30 F8          JR      NC,$3A9D        
3AA5: C0             RET     NZ              
3AA6: 00             NOP                     
3AA7: 20 F8          JR      NZ,$3AA1        
3AA9: C0             RET     NZ              
3AAA: 00             NOP                     
3AAB: 10 F8          DJNZ    $3AA5           
3AAD: C0             RET     NZ              
3AAE: 00             NOP                     
3AAF: 00             NOP                     
3AB0: F0             RET     P               
3AB1: E0             RET     PO              
3AB2: 00             NOP                     
3AB3: 00             NOP                     
3AB4: E0             RET     PO              
3AB5: 00             NOP                     
3AB6: 00             NOP                     
3AB7: 00             NOP                     
3AB8: D0             RET     NC              
3AB9: 00             NOP                     
3ABA: 00             NOP                     
3ABB: 00             NOP                     
3ABC: C0             RET     NZ              
3ABD: 00             NOP                     
3ABE: 00             NOP                     
3ABF: 00             NOP                     
3AC0: B0             OR      B               
3AC1: 00             NOP                     
3AC2: 00             NOP                     
3AC3: 00             NOP                     
3AC4: A0             AND     B               
3AC5: 00             NOP                     
3AC6: 00             NOP                     
3AC7: 00             NOP                     
3AC8: 90             SUB     B               
3AC9: 00             NOP                     
3ACA: 00             NOP                     
3ACB: 00             NOP                     
3ACC: 80             ADD     A,B             
3ACD: 00             NOP                     
3ACE: 00             NOP                     
3ACF: 00             NOP                     
3AD0: 70             LD      (HL),B          
3AD1: 00             NOP                     
3AD2: 00             NOP                     
3AD3: 00             NOP                     
3AD4: 60             LD      H,B             
3AD5: 00             NOP                     
3AD6: 00             NOP                     
3AD7: 00             NOP                     
3AD8: 50             LD      D,B             
3AD9: 00             NOP                     
3ADA: 00             NOP                     
3ADB: 00             NOP                     
3ADC: 40             LD      B,B             
3ADD: 00             NOP                     
3ADE: 00             NOP                     
3ADF: 00             NOP                     
3AE0: 30 00          JR      NC,$3AE2        
3AE2: 00             NOP                     
3AE3: 00             NOP                     
3AE4: 20 00          JR      NZ,$3AE6        
3AE6: 00             NOP                     
3AE7: 00             NOP                     
3AE8: 10 20          DJNZ    $3B0A           
3AEA: 00             NOP                     
3AEB: 10 10          DJNZ    $3AFD           
3AED: 40             LD      B,B             
3AEE: 00             NOP                     
3AEF: 20 10          JR      NZ,$3B01        
3AF1: 40             LD      B,B             
3AF2: 00             NOP                     
3AF3: 30 10          JR      NC,$3B05        
3AF5: 40             LD      B,B             
3AF6: 00             NOP                     
3AF7: 40             LD      B,B             
3AF8: 10 40          DJNZ    $3B3A           
3AFA: 00             NOP                     
3AFB: 50             LD      D,B             
3AFC: 10 40          DJNZ    $3B3E           
3AFE: 00             NOP                     
3AFF: 60             LD      H,B             
3B00: 10 40          DJNZ    $3B42           
3B02: 00             NOP                     
3B03: 70             LD      (HL),B          
3B04: 10 40          DJNZ    $3B46           
3B06: 00             NOP                     
3B07: 80             ADD     A,B             
3B08: 10 40          DJNZ    $3B4A           
3B0A: 00             NOP                     
3B0B: 90             SUB     B               
3B0C: 10 40          DJNZ    $3B4E           
3B0E: 00             NOP                     
3B0F: A0             AND     B               
3B10: 10 40          DJNZ    $3B52           
3B12: 00             NOP                     
3B13: B0             OR      B               
3B14: 10 40          DJNZ    $3B56           
3B16: 00             NOP                     
3B17: C0             RET     NZ              
3B18: 10 40          DJNZ    $3B5A           
3B1A: 00             NOP                     
3B1B: D0             RET     NC              
3B1C: 10 40          DJNZ    $3B5E           
3B1E: 00             NOP                     
3B1F: E0             RET     PO              
3B20: 10 40          DJNZ    $3B62           
3B22: 00             NOP                     
3B23: F0             RET     P               
3B24: 10 60          DJNZ    $3B86           
3B26: 00             NOP                     
3B27: F0             RET     P               
3B28: 20 80          JR      NZ,$3AAA        
3B2A: 00             NOP                     
3B2B: F0             RET     P               
3B2C: 30 80          JR      NC,$3AAE        
3B2E: 00             NOP                     
3B2F: F0             RET     P               
3B30: 40             LD      B,B             
3B31: 80             ADD     A,B             
3B32: 00             NOP                     
3B33: F0             RET     P               
3B34: 50             LD      D,B             
3B35: 80             ADD     A,B             
3B36: 00             NOP                     
3B37: F0             RET     P               
3B38: 60             LD      H,B             
3B39: 80             ADD     A,B             
3B3A: 00             NOP                     
3B3B: F0             RET     P               
3B3C: 70             LD      (HL),B          
3B3D: 80             ADD     A,B             
3B3E: 00             NOP                     
3B3F: F0             RET     P               
3B40: 80             ADD     A,B             
3B41: 80             ADD     A,B             
3B42: 00             NOP                     
3B43: F0             RET     P               
3B44: 90             SUB     B               
3B45: 80             ADD     A,B             
3B46: 00             NOP                     
3B47: F0             RET     P               
3B48: A0             AND     B               
3B49: 80             ADD     A,B             
3B4A: 00             NOP                     
3B4B: F0             RET     P               
3B4C: B0             OR      B               
3B4D: 80             ADD     A,B             
3B4E: 00             NOP                     
3B4F: F0             RET     P               
3B50: C0             RET     NZ              
3B51: 80             ADD     A,B             
3B52: 00             NOP                     
3B53: F0             RET     P               
3B54: D0             RET     NC              
3B55: 80             ADD     A,B             
3B56: 00             NOP                     
3B57: F0             RET     P               
3B58: E0             RET     PO              
3B59: 80             ADD     A,B             
3B5A: 00             NOP                     
3B5B: F0             RET     P               
3B5C: F0             RET     P               
3B5D: A0             AND     B               
3B5E: 00             NOP                     
3B5F: 3A 04 AD       LD      A,($AD04)       
3B62: 3D             DEC     A               
3B63: C0             RET     NZ              
3B64: DD 21 C0 A8    LD      IX,$A8C0        
3B68: FD 21 28 AA    LD      IY,$AA28        
3B6C: DD 7E 00       LD      A,(IX+$00)      
3B6F: A7             AND     A               
3B70: CA 25 3C       JP      Z,$3C25         
3B73: 3C             INC     A               
3B74: C2 94 3B       JP      NZ,$3B94        
3B77: CD 05 3E       CALL    $3E05           
3B7A: FD 7E 31       LD      A,(IY+$31)      
3B7D: C6 10          ADD     $10             
3B7F: FD 77 33       LD      (IY+$33),A      
3B82: FD 7E 00       LD      A,(IY+$00)      
3B85: FD 77 02       LD      (IY+$02),A      
3B88: CD C4 3C       CALL    $3CC4           
3B8B: DA 0D 3C       JP      C,$3C0D         
3B8E: CD E9 3C       CALL    $3CE9           
3B91: C3 25 3D       JP      $3D25           
3B94: 3D             DEC     A               
3B95: 4F             LD      C,A             
3B96: 21 DC A8       LD      HL,$A8DC        
3B99: 7E             LD      A,(HL)          
3B9A: A7             AND     A               
3B9B: CA A9 3B       JP      Z,$3BA9         
3B9E: 35             DEC     (HL)            
3B9F: DD 36 00 FF    LD      (IX+$00),$FF    
3BA3: CD 83 56       CALL    $5683           
3BA6: C3 77 3B       JP      $3B77           
3BA9: 79             LD      A,C             
3BAA: FE 61          CP      $61             
3BAC: 38 0F          JR      C,$3BBD         
3BAE: DD 36 00 61    LD      (IX+$00),$61    
3BB2: CD 83 56       CALL    $5683           
3BB5: FD 36 30 3D    LD      (IY+$30),$3D    
3BB9: FD 36 32 3D    LD      (IY+$32),$3D    
3BBD: DD 35 00       DEC     (IX+$00)        
3BC0: 28 4B          JR      Z,$3C0D         
3BC2: CD 60 2B       CALL    $2B60           
3BC5: FD 7E 31       LD      A,(IY+$31)      
3BC8: C6 10          ADD     $10             
3BCA: FD 77 33       LD      (IY+$33),A      
3BCD: FD 7E 00       LD      A,(IY+$00)      
3BD0: FD 77 02       LD      (IY+$02),A      
3BD3: DD 7E 00       LD      A,(IX+$00)      
3BD6: D6 40          SUB     $40             
3BD8: CA F1 3B       JP      Z,$3BF1         
3BDB: D8             RET     C               
3BDC: 4F             LD      C,A             
3BDD: E6 07          AND     $07             
3BDF: C0             RET     NZ              
3BE0: 79             LD      A,C             
3BE1: 0F             RRCA                    
3BE2: 0F             RRCA                    
3BE3: 0F             RRCA                    
3BE4: 3D             DEC     A               
3BE5: 21 09 3C       LD      HL,$3C09        
3BE8: CF             RST     0X08            
3BE9: FD 77 03       LD      (IY+$03),A      
3BEC: 3C             INC     A               
3BED: FD 77 01       LD      (IY+$01),A      
3BF0: C9             RET                     
3BF1: 11 0B 04       LD      DE,$040B        
3BF4: FF             RST     0X38            
3BF5: FD 36 03 FA    LD      (IY+$03),$FA    
3BF9: FD 36 01 FB    LD      (IY+$01),$FB    
3BFD: FD 36 30 6C    LD      (IY+$30),$6C    
3C01: FD 36 32 6C    LD      (IY+$32),$6C    
3C05: DD 35 00       DEC     (IX+$00)        
3C08: C9             RET                     
3C09: 96             SUB     (HL)            
3C0A: 94             SUB     H               
3C0B: 92             SUB     D               
3C0C: 90             SUB     B               
3C0D: AF             XOR     A               
3C0E: DD 77 00       LD      (IX+$00),A      
3C11: DD 77 10       LD      (IX+$10),A      
3C14: FD 77 00       LD      (IY+$00),A      
3C17: FD 77 31       LD      (IY+$31),A      
3C1A: 32 5B AA       LD      ($AA5B),A       
3C1D: 32 2A AA       LD      ($AA2A),A       
3C20: DD 36 0E 80    LD      (IX+$0E),$80    
3C24: C9             RET                     
3C25: 3A 80 A9       LD      A,($A980)       
3C28: E6 01          AND     $01             
3C2A: C0             RET     NZ              
3C2B: DD 35 0E       DEC     (IX+$0E)        
3C2E: CA 32 3C       JP      Z,$3C32         
3C31: C9             RET                     
3C32: 3A 0D AD       LD      A,($AD0D)       
3C35: A7             AND     A               
3C36: C0             RET     NZ              
3C37: 3A 02 A8       LD      A,($A802)       
3C3A: 47             LD      B,A             
3C3B: C6 08          ADD     $08             
3C3D: E6 7F          AND     $7F             
3C3F: FE 10          CP      $10             
3C41: 38 32          JR      C,$3C75         
3C43: 78             LD      A,B             
3C44: 0F             RRCA                    
3C45: 0F             RRCA                    
3C46: E6 3E          AND     $3E             
3C48: 21 84 3C       LD      HL,$3C84        
3C4B: CF             RST     0X08            
3C4C: FD 77 31       LD      (IY+$31),A      
3C4F: 23             INC     HL              
3C50: 7E             LD      A,(HL)          
3C51: FD 77 00       LD      (IY+$00),A      
3C54: 78             LD      A,B             
3C55: C6 C0          ADD     $C0             
3C57: E6 80          AND     $80             
3C59: DD 77 02       LD      (IX+$02),A      
3C5C: CD 42 59       CALL    $5942           
3C5F: DD 73 0A       LD      (IX+$0A),E      
3C62: DD 72 0B       LD      (IX+$0B),D      
3C65: DD 71 0C       LD      (IX+$0C),C      
3C68: DD 70 0D       LD      (IX+$0D),B      
3C6B: 3E 03          LD      A,$03           
3C6D: 32 DC A8       LD      ($A8DC),A       
3C70: DD 36 00 FF    LD      (IX+$00),$FF    
3C74: C9             RET                     
3C75: 3A 80 A9       LD      A,($A980)       
3C78: 4F             LD      C,A             
3C79: 3E 10          LD      A,$10           
3C7B: CB 59          BIT     3,C             
3C7D: 20 02          JR      NZ,$3C81        
3C7F: ED 44          NEG                     
3C81: 80             ADD     A,B             
3C82: 18 C0          JR      $3C44           
3C84: EC 80 EC       CALL    PE,$EC80        
3C87: 88             ADC     A,B             
3C88: EC 90 EC       CALL    PE,$EC90        
3C8B: A0             AND     B               
3C8C: EC B0 EC       CALL    PE,$ECB0        
3C8F: C0             RET     NZ              
3C90: EC D0 EC       CALL    PE,$ECD0        
3C93: E0             RET     PO              
3C94: F0             RET     P               
3C95: EC F0 EC       CALL    PE,$ECF0        
3C98: F0             RET     P               
3C99: E0             RET     PO              
3C9A: F0             RET     P               
3C9B: D0             RET     NC              
3C9C: F0             RET     P               
3C9D: C0             RET     NZ              
3C9E: F0             RET     P               
3C9F: B0             OR      B               
3CA0: F0             RET     P               
3CA1: A0             AND     B               
3CA2: F0             RET     P               
3CA3: 90             SUB     B               
3CA4: F0             RET     P               
3CA5: 80             ADD     A,B             
3CA6: F0             RET     P               
3CA7: 78             LD      A,B             
3CA8: F0             RET     P               
3CA9: 70             LD      (HL),B          
3CAA: F0             RET     P               
3CAB: 60             LD      H,B             
3CAC: F0             RET     P               
3CAD: 50             LD      D,B             
3CAE: F0             RET     P               
3CAF: 40             LD      B,B             
3CB0: F0             RET     P               
3CB1: 30 F0          JR      NC,$3CA3        
3CB3: 28 F0          JR      Z,$3CA5         
3CB5: 20 EC          JR      NZ,$3CA3        
3CB7: 20 EC          JR      NZ,$3CA5        
3CB9: 30 EC          JR      NC,$3CA7        
3CBB: 40             LD      B,B             
3CBC: EC 50 EC       CALL    PE,$EC50        
3CBF: 60             LD      H,B             
3CC0: EC 70 EC       CALL    PE,$EC70        
3CC3: 78             LD      A,B             
3CC4: DD 7E 02       LD      A,(IX+$02)      
3CC7: C6 40          ADD     $40             
3CC9: CB 7F          BIT     7,A             
3CCB: C2 D9 3C       JP      NZ,$3CD9        
3CCE: FD 7E 31       LD      A,(IY+$31)      
3CD1: C6 13          ADD     $13             
3CD3: FE 03          CP      $03             
3CD5: D8             RET     C               
3CD6: C3 E1 3C       JP      $3CE1           
3CD9: FD 7E 31       LD      A,(IY+$31)      
3CDC: C6 10          ADD     $10             
3CDE: FE 03          CP      $03             
3CE0: D8             RET     C               
3CE1: FD 7E 00       LD      A,(IY+$00)      
3CE4: C6 02          ADD     $02             
3CE6: FE 04          CP      $04             
3CE8: C9             RET                     
3CE9: 3A 80 A9       LD      A,($A980)       
3CEC: E6 02          AND     $02             
3CEE: 47             LD      B,A             
3CEF: 3A DC A8       LD      A,($A8DC)       
3CF2: 4F             LD      C,A             
3CF3: 3E 03          LD      A,$03           
3CF5: 91             SUB     C               
3CF6: 87             ADD     A,A             
3CF7: 87             ADD     A,A             
3CF8: C6 A0          ADD     $A0             
3CFA: 80             ADD     A,B             
3CFB: 4F             LD      C,A             
3CFC: DD 7E 02       LD      A,(IX+$02)      
3CFF: C6 40          ADD     $40             
3D01: FE 80          CP      $80             
3D03: 38 10          JR      C,$3D15         
3D05: FD 71 01       LD      (IY+$01),C      
3D08: 0C             INC     C               
3D09: FD 71 03       LD      (IY+$03),C      
3D0C: FD 36 30 ED    LD      (IY+$30),$ED    
3D10: FD 36 32 ED    LD      (IY+$32),$ED    
3D14: C9             RET                     
3D15: FD 71 03       LD      (IY+$03),C      
3D18: 0C             INC     C               
3D19: FD 71 01       LD      (IY+$01),C      
3D1C: FD 36 30 6D    LD      (IY+$30),$6D    
3D20: FD 36 32 6D    LD      (IY+$32),$6D    
3D24: C9             RET                     
3D25: DD 7E 00       LD      A,(IX+$00)      
3D28: 3C             INC     A               
3D29: C0             RET     NZ              
3D2A: 3A F4 A8       LD      A,($A8F4)       
3D2D: A7             AND     A               
3D2E: C0             RET     NZ              
3D2F: 3A C6 A8       LD      A,($A8C6)       
3D32: A7             AND     A               
3D33: C8             RET     Z               
3D34: FE 01          CP      $01             
3D36: CA 40 3D       JP      Z,$3D40         
3D39: 3A E0 A8       LD      A,($A8E0)       
3D3C: A7             AND     A               
3D3D: CA 45 3D       JP      Z,$3D45         
3D40: 3A 40 A8       LD      A,($A840)       
3D43: A7             AND     A               
3D44: C0             RET     NZ              
3D45: 06 02          LD      B,$02           
3D47: 3A D6 A8       LD      A,($A8D6)       
3D4A: 57             LD      D,A             
3D4B: 87             ADD     A,A             
3D4C: 5F             LD      E,A             
3D4D: 3E 84          LD      A,$84           
3D4F: FD 96 00       SUB     (IY+$00)        
3D52: 82             ADD     A,D             
3D53: BB             CP      E               
3D54: D2 6F 3D       JP      NC,$3D6F        
3D57: 3E 78          LD      A,$78           
3D59: FD 96 31       SUB     (IY+$31)        
3D5C: 82             ADD     A,D             
3D5D: BB             CP      E               
3D5E: D2 6F 3D       JP      NC,$3D6F        
3D61: D9             EXX                     
3D62: 11 10 00       LD      DE,$0010        
3D65: DD 19          ADD     IX,DE           
3D67: FD 23          INC     IY              
3D69: FD 23          INC     IY              
3D6B: D9             EXX                     
3D6C: 10 DF          DJNZ    $3D4D           
3D6E: C9             RET                     
3D6F: CD 5F 56       CALL    $565F           
3D72: 21 7F AC       LD      HL,$AC7F        
3D75: CD B8 33       CALL    $33B8           
3D78: 67             LD      H,A             
3D79: 3E 18          LD      A,$18           
3D7B: EB             EX      DE,HL           
3D7C: 21 D4 A8       LD      HL,$A8D4        
3D7F: 34             INC     (HL)            
3D80: 46             LD      B,(HL)          
3D81: CB 40          BIT     0,B             
3D83: 20 02          JR      NZ,$3D87        
3D85: ED 44          NEG                     
3D87: EB             EX      DE,HL           
3D88: 84             ADD     A,H             
3D89: 08             EX      AF,AF'          
3D8A: FD 46 31       LD      B,(IY+$31)      
3D8D: FD 4E 00       LD      C,(IY+$00)      
3D90: 3A C6 A8       LD      A,($A8C6)       
3D93: FE 01          CP      $01             
3D95: CA 9F 3D       JP      Z,$3D9F         
3D98: 3A E0 A8       LD      A,($A8E0)       
3D9B: A7             AND     A               
3D9C: CA CF 3D       JP      Z,$3DCF         
3D9F: DD 21 40 A8    LD      IX,$A840        
3DA3: FD 21 18 AA    LD      IY,$AA18        
3DA7: FD 70 31       LD      (IY+$31),B      
3DAA: FD 71 00       LD      (IY+$00),C      
3DAD: 08             EX      AF,AF'          
3DAE: CD C5 59       CALL    $59C5           
3DB1: DD 73 0A       LD      (IX+$0A),E      
3DB4: DD 72 0B       LD      (IX+$0B),D      
3DB7: DD 71 0C       LD      (IX+$0C),C      
3DBA: DD 70 0D       LD      (IX+$0D),B      
3DBD: FD 36 01 4D    LD      (IY+$01),$4D    
3DC1: FD 36 30 62    LD      (IY+$30),$62    
3DC5: DD 35 00       DEC     (IX+$00)        
3DC8: 3A F6 A8       LD      A,($A8F6)       
3DCB: 32 F4 A8       LD      ($A8F4),A       
3DCE: C9             RET                     
3DCF: DD 21 E0 A8    LD      IX,$A8E0        
3DD3: FD 21 2C AA    LD      IY,$AA2C        
3DD7: C3 A7 3D       JP      $3DA7           
3DDA: 3A 04 AD       LD      A,($AD04)       
3DDD: 3D             DEC     A               
3DDE: C0             RET     NZ              
3DDF: DD 21 E0 A8    LD      IX,$A8E0        
3DE3: FD 21 2C AA    LD      IY,$AA2C        
3DE7: CD EB 3D       CALL    $3DEB           
3DEA: C9             RET                     
3DEB: DD 7E 00       LD      A,(IX+$00)      
3DEE: A7             AND     A               
3DEF: C8             RET     Z               
3DF0: 3C             INC     A               
3DF1: C2 FB 3D       JP      NZ,$3DFB        
3DF4: CD 05 3E       CALL    $3E05           
3DF7: CD 83 2B       CALL    $2B83           
3DFA: D0             RET     NC              
3DFB: CD AB 40       CALL    $40AB           
3DFE: 3A F6 A8       LD      A,($A8F6)       
3E01: DD 77 0E       LD      (IX+$0E),A      
3E04: C9             RET                     
3E05: DD 66 0B       LD      H,(IX+$0B)      
3E08: DD 6E 0A       LD      L,(IX+$0A)      
3E0B: ED 5B 08 A8    LD      DE,($A808)      
3E0F: 19             ADD     HL,DE           
3E10: FD 56 31       LD      D,(IY+$31)      
3E13: DD 5E 03       LD      E,(IX+$03)      
3E16: 19             ADD     HL,DE           
3E17: FD 74 31       LD      (IY+$31),H      
3E1A: DD 75 03       LD      (IX+$03),L      
3E1D: DD 66 0D       LD      H,(IX+$0D)      
3E20: DD 6E 0C       LD      L,(IX+$0C)      
3E23: ED 5B 0A A8    LD      DE,($A80A)      
3E27: 19             ADD     HL,DE           
3E28: FD 56 00       LD      D,(IY+$00)      
3E2B: DD 5E 05       LD      E,(IX+$05)      
3E2E: 19             ADD     HL,DE           
3E2F: FD 74 00       LD      (IY+$00),H      
3E32: DD 75 05       LD      (IX+$05),L      
3E35: C9             RET                     
3E36: DD 21 10 A8    LD      IX,$A810        
3E3A: FD 21 12 AA    LD      IY,$AA12        
3E3E: CD 63 3E       CALL    $3E63           
3E41: DD 21 20 A8    LD      IX,$A820        
3E45: FD 21 14 AA    LD      IY,$AA14        
3E49: CD 63 3E       CALL    $3E63           
3E4C: DD 21 30 A8    LD      IX,$A830        
3E50: FD 21 16 AA    LD      IY,$AA16        
3E54: CD 63 3E       CALL    $3E63           
3E57: DD 21 40 A8    LD      IX,$A840        
3E5B: FD 21 18 AA    LD      IY,$AA18        
3E5F: CD 63 3E       CALL    $3E63           
3E62: C9             RET                     
3E63: DD 7E 00       LD      A,(IX+$00)      
3E66: A7             AND     A               
3E67: C8             RET     Z               
3E68: 3C             INC     A               
3E69: C2 8E 3E       JP      NZ,$3E8E        
3E6C: 3A 04 AD       LD      A,($AD04)       
3E6F: FE 04          CP      $04             
3E71: CC 7E 3E       CALL    Z,$3E7E         
3E74: CD 05 3E       CALL    $3E05           
3E77: CD 83 2B       CALL    $2B83           
3E7A: D0             RET     NC              
3E7B: C3 AB 40       JP      $40AB           
3E7E: 3A 80 A9       LD      A,($A980)       
3E81: 0F             RRCA                    
3E82: E6 07          AND     $07             
3E84: C6 40          ADD     $40             
3E86: FD 77 01       LD      (IY+$01),A      
3E89: FD 36 30 44    LD      (IY+$30),$44    
3E8D: C9             RET                     
3E8E: 3A 04 AD       LD      A,($AD04)       
3E91: FE 04          CP      $04             
3E93: 28 03          JR      Z,$3E98         
3E95: C3 AB 40       JP      $40AB           
3E98: DD 7E 00       LD      A,(IX+$00)      
3E9B: FE 01          CP      $01             
3E9D: CA AB 40       JP      Z,$40AB         
3EA0: DD 35 00       DEC     (IX+$00)        
3EA3: FE 3C          CP      $3C             
3EA5: D4 CB 3E       CALL    NC,$3ECB        
3EA8: CD 60 2B       CALL    $2B60           
3EAB: DD 7E 00       LD      A,(IX+$00)      
3EAE: FE 1C          CP      $1C             
3EB0: D8             RET     C               
3EB1: D6 1C          SUB     $1C             
3EB3: 0F             RRCA                    
3EB4: 0F             RRCA                    
3EB5: E6 07          AND     $07             
3EB7: 21 C3 3E       LD      HL,$3EC3        
3EBA: CF             RST     0X08            
3EBB: FD 77 01       LD      (IY+$01),A      
3EBE: FD 36 30 03    LD      (IY+$30),$03    
3EC2: C9             RET                     
3EC3: FF             RST     0X38            
3EC4: E6 E7          AND     $E7             
3EC6: E7             RST     0X20            
3EC7: E6 E6          AND     $E6             
3EC9: E5             PUSH    HL              
3ECA: E4 DD 36       CALL    PO,$36DD        
3ECD: 00             NOP                     
3ECE: 3B             DEC     SP              
3ECF: C3 83 56       JP      $5683           
3ED2: 92             SUB     D               
3ED3: A6             AND     (HL)            
3ED4: 14             INC     D               
3ED5: B9             CP      C               
3ED6: 3A 80 A9       LD      A,($A980)       
3ED9: E6 07          AND     $07             
3EDB: C6 05          ADD     $05             
3EDD: DD BE 0F       CP      (IX+$0F)        
3EE0: C0             RET     NZ              
3EE1: 3A 17 A8       LD      A,($A817)       
3EE4: A7             AND     A               
3EE5: C0             RET     NZ              
3EE6: 21 10 A8       LD      HL,$A810        
3EE9: 11 12 AA       LD      DE,$AA12        
3EEC: 3A 44 A8       LD      A,($A844)       
3EEF: A7             AND     A               
3EF0: C8             RET     Z               
3EF1: 47             LD      B,A             
3EF2: 7E             LD      A,(HL)          
3EF3: A7             AND     A               
3EF4: 28 09          JR      Z,$3EFF         
3EF6: 7D             LD      A,L             
3EF7: C6 10          ADD     $10             
3EF9: 6F             LD      L,A             
3EFA: 1C             INC     E               
3EFB: 1C             INC     E               
3EFC: 10 F4          DJNZ    $3EF2           
3EFE: C9             RET                     
3EFF: 22 91 A9       LD      ($A991),HL      
3F02: ED 53 93 A9    LD      ($A993),DE      
3F06: 3A 27 A8       LD      A,($A827)       
3F09: 47             LD      B,A             
3F0A: 87             ADD     A,A             
3F0B: 4F             LD      C,A             
3F0C: 3E 78          LD      A,$78           
3F0E: FD 96 31       SUB     (IY+$31)        
3F11: 80             ADD     A,B             
3F12: B9             CP      C               
3F13: 30 08          JR      NC,$3F1D        
3F15: 3E 84          LD      A,$84           
3F17: FD 96 00       SUB     (IY+$00)        
3F1A: 80             ADD     A,B             
3F1B: B9             CP      C               
3F1C: D8             RET     C               
3F1D: 3A 37 A8       LD      A,($A837)       
3F20: 47             LD      B,A             
3F21: 87             ADD     A,A             
3F22: 4F             LD      C,A             
3F23: 3A 02 A8       LD      A,($A802)       
3F26: DD 96 02       SUB     (IX+$02)        
3F29: 80             ADD     A,B             
3F2A: B9             CP      C               
3F2B: D0             RET     NC              
3F2C: 7A             LD      A,D             
3F2D: FE 02          CP      $02             
3F2F: CA 9E 3F       JP      Z,$3F9E         
3F32: 21 7F AC       LD      HL,$AC7F        
3F35: CD B8 33       CALL    $33B8           
3F38: 4F             LD      C,A             
3F39: DD 96 02       SUB     (IX+$02)        
3F3C: C6 10          ADD     $10             
3F3E: FE 20          CP      $20             
3F40: D0             RET     NC              
3F41: CD 93 3F       CALL    $3F93           
3F44: DD E5          PUSH    IX              
3F46: FD E5          PUSH    IY              
3F48: FD 56 31       LD      D,(IY+$31)      
3F4B: FD 5E 00       LD      E,(IY+$00)      
3F4E: DD 2A 91 A9    LD      IX,($A991)      
3F52: FD 2A 93 A9    LD      IY,($A993)      
3F56: FD 72 31       LD      (IY+$31),D      
3F59: FD 73 00       LD      (IY+$00),E      
3F5C: 3A 04 AD       LD      A,($AD04)       
3F5F: A7             AND     A               
3F60: 79             LD      A,C             
3F61: 20 05          JR      NZ,$3F68        
3F63: CD CB 59       CALL    $59CB           
3F66: 18 03          JR      $3F6B           
3F68: CD D1 59       CALL    $59D1           
3F6B: DD 73 0A       LD      (IX+$0A),E      
3F6E: DD 72 0B       LD      (IX+$0B),D      
3F71: DD 71 0C       LD      (IX+$0C),C      
3F74: DD 70 0D       LD      (IX+$0D),B      
3F77: FD 7E 31       LD      A,(IY+$31)      
3F7A: FD 7E 00       LD      A,(IY+$00)      
3F7D: FD 36 01 4D    LD      (IY+$01),$4D    
3F81: FD 36 30 62    LD      (IY+$30),$62    
3F85: 3A 14 A8       LD      A,($A814)       
3F88: 32 17 A8       LD      ($A817),A       
3F8B: DD 35 00       DEC     (IX+$00)        
3F8E: FD E1          POP     IY              
3F90: DD E1          POP     IX              
3F92: C9             RET                     
3F93: 3A 04 AD       LD      A,($AD04)       
3F96: FE 03          CP      $03             
3F98: DA 5F 56       JP      C,$565F         
3F9B: C3 69 56       JP      $5669           
3F9E: 3A E6 A8       LD      A,($A8E6)       
3FA1: 47             LD      B,A             
3FA2: 87             ADD     A,A             
3FA3: 4F             LD      C,A             
3FA4: 3E 84          LD      A,$84           
3FA6: FD 96 00       SUB     (IY+$00)        
3FA9: 80             ADD     A,B             
3FAA: B9             CP      C               
3FAB: D0             RET     NC              
3FAC: C3 32 3F       JP      $3F32           
3FAF: DD 7E 02       LD      A,(IX+$02)      
3FB2: C6 08          ADD     $08             
3FB4: 0F             RRCA                    
3FB5: 0F             RRCA                    
3FB6: 0F             RRCA                    
3FB7: 0F             RRCA                    
3FB8: E6 0F          AND     $0F             
3FBA: 21 CA 3F       LD      HL,$3FCA        
3FBD: CF             RST     0X08            
3FBE: FD 77 01       LD      (IY+$01),A      
3FC1: 11 10 00       LD      DE,$0010        
3FC4: 19             ADD     HL,DE           
3FC5: 7E             LD      A,(HL)          
3FC6: FD 77 30       LD      (IY+$30),A      
3FC9: C9             RET                     
3FCA: 48             LD      C,B             
3FCB: 49             LD      C,C             
3FCC: 4A             LD      C,D             
3FCD: 4B             LD      C,E             
3FCE: 4C             LD      C,H             
3FCF: 4B             LD      C,E             
3FD0: 4A             LD      C,D             
3FD1: 49             LD      C,C             
3FD2: 48             LD      C,B             
3FD3: 49             LD      C,C             
3FD4: 4A             LD      C,D             
3FD5: 4B             LD      C,E             
3FD6: 4C             LD      C,H             
3FD7: 4B             LD      C,E             
3FD8: 4A             LD      C,D             
3FD9: 49             LD      C,C             
3FDA: F4 B4 B4       CALL    P,$B4B4         
3FDD: B4             OR      H               
3FDE: B4             OR      H               
3FDF: 34             INC     (HL)            
3FE0: 34             INC     (HL)            
3FE1: 34             INC     (HL)            
3FE2: 34             INC     (HL)            
3FE3: 74             LD      (HL),H          
3FE4: 74             LD      (HL),H          
3FE5: 74             LD      (HL),H          
3FE6: 74             LD      (HL),H          
3FE7: F4 F4 F4       CALL    P,$F4F4         
3FEA: 3A 04 AD       LD      A,($AD04)       
3FED: A7             AND     A               
3FEE: C0             RET     NZ              
3FEF: DD 21 C0 A8    LD      IX,$A8C0        
3FF3: FD 21 28 AA    LD      IY,$AA28        
3FF7: 06 03          LD      B,$03           
3FF9: DD 7E 00       LD      A,(IX+$00)      
3FFC: A7             AND     A               
3FFD: CA 0B 40       JP      Z,$400B         
4000: 3C             INC     A               
4001: 20 05          JR      NZ,$4008        
4003: CD 17 40       CALL    $4017           
4006: 18 03          JR      $400B           
4008: CD 6C 40       CALL    $406C           
400B: 11 10 00       LD      DE,$0010        
400E: DD 19          ADD     IX,DE           
4010: FD 23          INC     IY              
4012: FD 23          INC     IY              
4014: 10 E3          DJNZ    $3FF9           
4016: C9             RET                     
4017: FD 56 31       LD      D,(IY+$31)      
401A: DD 5E 03       LD      E,(IX+$03)      
401D: DD 7E 01       LD      A,(IX+$01)      
4020: A7             AND     A               
4021: 28 05          JR      Z,$4028         
4023: 21 80 FE       LD      HL,$FE80        
4026: 18 03          JR      $402B           
4028: 21 80 01       LD      HL,$0180        
402B: 19             ADD     HL,DE           
402C: ED 5B 08 A8    LD      DE,($A808)      
4030: 19             ADD     HL,DE           
4031: FD 74 31       LD      (IY+$31),H      
4034: DD 75 03       LD      (IX+$03),L      
4037: DD 6E 07       LD      L,(IX+$07)      
403A: DD 66 08       LD      H,(IX+$08)      
403D: 11 09 00       LD      DE,$0009        
4040: 19             ADD     HL,DE           
4041: DD 75 07       LD      (IX+$07),L      
4044: DD 74 08       LD      (IX+$08),H      
4047: FD 56 00       LD      D,(IY+$00)      
404A: DD 5E 05       LD      E,(IX+$05)      
404D: 19             ADD     HL,DE           
404E: ED 5B 0A A8    LD      DE,($A80A)      
4052: 19             ADD     HL,DE           
4053: FD 74 00       LD      (IY+$00),H      
4056: DD 75 05       LD      (IX+$05),L      
4059: FD 7E 31       LD      A,(IY+$31)      
405C: C6 10          ADD     $10             
405E: FE 20          CP      $20             
4060: DA AB 40       JP      C,$40AB         
4063: FD 7E 00       LD      A,(IY+$00)      
4066: FE F8          CP      $F8             
4068: D2 AB 40       JP      NC,$40AB        
406B: C9             RET                     
406C: DD 7E 00       LD      A,(IX+$00)      
406F: FE 3C          CP      $3C             
4071: D4 9D 40       CALL    NC,$409D        
4074: DD 35 00       DEC     (IX+$00)        
4077: 28 32          JR      Z,$40AB         
4079: CD 60 2B       CALL    $2B60           
407C: DD 7E 00       LD      A,(IX+$00)      
407F: FE 1C          CP      $1C             
4081: D8             RET     C               
4082: D6 1C          SUB     $1C             
4084: 0F             RRCA                    
4085: 0F             RRCA                    
4086: E6 0F          AND     $0F             
4088: 21 94 40       LD      HL,$4094        
408B: CF             RST     0X08            
408C: FD 77 01       LD      (IY+$01),A      
408F: FD 36 30 0E    LD      (IY+$30),$0E    
4093: C9             RET                     
4094: FF             RST     0X38            
4095: 9A             SBC     D               
4096: 99             SBC     C               
4097: 98             SBC     B               
4098: 98             SBC     B               
4099: 99             SBC     C               
409A: 99             SBC     C               
409B: 9A             SBC     D               
409C: 9B             SBC     E               
409D: DD 36 00 3B    LD      (IX+$00),$3B    
40A1: 3A 04 AD       LD      A,($AD04)       
40A4: A7             AND     A               
40A5: CA 8E 56       JP      Z,$568E         
40A8: C3 8E 56       JP      $568E           
40AB: DD 36 00 00    LD      (IX+$00),$00    
40AF: FD 36 00 00    LD      (IY+$00),$00    
40B3: FD 36 31 00    LD      (IY+$31),$00    
40B7: C9             RET                     
40B8: 3A 04 AD       LD      A,($AD04)       
40BB: FE 02          CP      $02             
40BD: D8             RET     C               
40BE: 3A 80 A9       LD      A,($A980)       
40C1: E6 1F          AND     $1F             
40C3: C0             RET     NZ              
40C4: 3A C0 A8       LD      A,($A8C0)       
40C7: 3C             INC     A               
40C8: C8             RET     Z               
40C9: 3A D0 A8       LD      A,($A8D0)       
40CC: 3C             INC     A               
40CD: C8             RET     Z               
40CE: 3A E0 A8       LD      A,($A8E0)       
40D1: 3C             INC     A               
40D2: C8             RET     Z               
40D3: C3 79 56       JP      $5679           
40D6: 3A 04 AD       LD      A,($AD04)       
40D9: FE 02          CP      $02             
40DB: D8             RET     C               
40DC: DD 21 C0 A8    LD      IX,$A8C0        
40E0: FD 21 28 AA    LD      IY,$AA28        
40E4: 3A C6 A8       LD      A,($A8C6)       
40E7: A7             AND     A               
40E8: C8             RET     Z               
40E9: 47             LD      B,A             
40EA: DD 7E 00       LD      A,(IX+$00)      
40ED: A7             AND     A               
40EE: CA 0B 41       JP      Z,$410B         
40F1: 3C             INC     A               
40F2: 20 14          JR      NZ,$4108        
40F4: 3A 04 AD       LD      A,($AD04)       
40F7: FE 04          CP      $04             
40F9: CA 94 41       JP      Z,$4194         
40FC: DD 7E 0E       LD      A,(IX+$0E)      
40FF: A7             AND     A               
4100: C2 8B 41       JP      NZ,$418B        
4103: CD 17 41       CALL    $4117           
4106: 18 03          JR      $410B           
4108: CD 3C 41       CALL    $413C           
410B: 11 10 00       LD      DE,$0010        
410E: DD 19          ADD     IX,DE           
4110: FD 23          INC     IY              
4112: FD 23          INC     IY              
4114: 10 D4          DJNZ    $40EA           
4116: C9             RET                     
4117: C5             PUSH    BC              
4118: 3A 80 A9       LD      A,($A980)       
411B: E6 0F          AND     $0F             
411D: DD BE 0F       CP      (IX+$0F)        
4120: 20 09          JR      NZ,$412B        
4122: 21 7F AC       LD      HL,$AC7F        
4125: CD B8 33       CALL    $33B8           
4128: DD 77 01       LD      (IX+$01),A      
412B: CD 01 42       CALL    $4201           
412E: CD AA 58       CALL    $58AA           
4131: CD AF 3F       CALL    $3FAF           
4134: C1             POP     BC              
4135: CD 83 2B       CALL    $2B83           
4138: D0             RET     NC              
4139: C3 AB 40       JP      $40AB           
413C: DD 7E 00       LD      A,(IX+$00)      
413F: FE 3C          CP      $3C             
4141: D4 9D 40       CALL    NC,$409D        
4144: CD 60 2B       CALL    $2B60           
4147: DD 35 00       DEC     (IX+$00)        
414A: CA AB 40       JP      Z,$40AB         
414D: DD 7E 00       LD      A,(IX+$00)      
4150: FE 1C          CP      $1C             
4152: D8             RET     C               
4153: D6 1C          SUB     $1C             
4155: 0F             RRCA                    
4156: 0F             RRCA                    
4157: E6 07          AND     $07             
4159: 57             LD      D,A             
415A: 3A 04 AD       LD      A,($AD04)       
415D: FE 04          CP      $04             
415F: 30 15          JR      NC,$4176        
4161: 21 6E 41       LD      HL,$416E        
4164: 7A             LD      A,D             
4165: CF             RST     0X08            
4166: FD 77 01       LD      (IY+$01),A      
4169: FD 36 30 0D    LD      (IY+$30),$0D    
416D: C9             RET                     
416E: FF             RST     0X38            
416F: 9E             SBC     (HL)            
4170: 9F             SBC     A               
4171: 9F             SBC     A               
4172: 9E             SBC     (HL)            
4173: 9E             SBC     (HL)            
4174: 9D             SBC     L               
4175: 9C             SBC     H               
4176: 21 83 41       LD      HL,$4183        
4179: 7A             LD      A,D             
417A: CF             RST     0X08            
417B: FD 77 01       LD      (IY+$01),A      
417E: FD 36 30 02    LD      (IY+$30),$02    
4182: C9             RET                     
4183: FF             RST     0X38            
4184: E2 E3 E3       JP      PO,$E3E3        
4187: E2 E2 E1       JP      PO,$E1E2        
418A: E0             RET     PO              
418B: CD 6C 3E       CALL    $3E6C           
418E: DD 35 0E       DEC     (IX+$0E)        
4191: C3 0B 41       JP      $410B           
4194: DD 7E 04       LD      A,(IX+$04)      
4197: A7             AND     A               
4198: CA A4 41       JP      Z,$41A4         
419B: DD 35 04       DEC     (IX+$04)        
419E: CD B8 41       CALL    $41B8           
41A1: C3 0B 41       JP      $410B           
41A4: C5             PUSH    BC              
41A5: CD B6 58       CALL    $58B6           
41A8: CD F1 41       CALL    $41F1           
41AB: CD 83 2B       CALL    $2B83           
41AE: C1             POP     BC              
41AF: D2 0B 41       JP      NC,$410B        
41B2: CD AB 40       CALL    $40AB           
41B5: C3 0B 41       JP      $410B           
41B8: C5             PUSH    BC              
41B9: 3A 80 A9       LD      A,($A980)       
41BC: E6 0F          AND     $0F             
41BE: 20 1F          JR      NZ,$41DF        
41C0: 21 75 AC       LD      HL,$AC75        
41C3: DD CB 0F 46    BIT     0,(IX+$0F)      
41C7: 20 03          JR      NZ,$41CC        
41C9: 21 79 AC       LD      HL,$AC79        
41CC: CD B8 33       CALL    $33B8           
41CF: 47             LD      B,A             
41D0: 7A             LD      A,D             
41D1: FE 10          CP      $10             
41D3: 30 07          JR      NC,$41DC        
41D5: 08             EX      AF,AF'          
41D6: FE 10          CP      $10             
41D8: DC EC 41       CALL    C,$41EC         
41DB: 08             EX      AF,AF'          
41DC: DD 70 01       LD      (IX+$01),B      
41DF: CD 1F 42       CALL    $421F           
41E2: CD B6 58       CALL    $58B6           
41E5: CD F1 41       CALL    $41F1           
41E8: C1             POP     BC              
41E9: C3 83 2B       JP      $2B83           
41EC: DD 36 04 00    LD      (IX+$04),$00    
41F0: C9             RET                     
41F1: 3A 80 A9       LD      A,($A980)       
41F4: 0F             RRCA                    
41F5: E6 07          AND     $07             
41F7: C6 50          ADD     $50             
41F9: FD 77 01       LD      (IY+$01),A      
41FC: FD 36 30 0A    LD      (IY+$30),$0A    
4200: C9             RET                     
4201: DD 7E 01       LD      A,(IX+$01)      
4204: DD 96 02       SUB     (IX+$02)        
4207: C6 01          ADD     $01             
4209: FE 02          CP      $02             
420B: D8             RET     C               
420C: FE 80          CP      $80             
420E: DD 7E 02       LD      A,(IX+$02)      
4211: 30 06          JR      NC,$4219        
4213: C6 01          ADD     $01             
4215: DD 77 02       LD      (IX+$02),A      
4218: C9             RET                     
4219: D6 01          SUB     $01             
421B: DD 77 02       LD      (IX+$02),A      
421E: C9             RET                     
421F: 3A 80 A9       LD      A,($A980)       
4222: E6 03          AND     $03             
4224: C8             RET     Z               
4225: DD 7E 01       LD      A,(IX+$01)      
4228: DD 96 02       SUB     (IX+$02)        
422B: C6 01          ADD     $01             
422D: FE 02          CP      $02             
422F: D8             RET     C               
4230: FE 80          CP      $80             
4232: DD 7E 02       LD      A,(IX+$02)      
4235: 30 06          JR      NC,$423D        
4237: C6 02          ADD     $02             
4239: DD 77 02       LD      (IX+$02),A      
423C: C9             RET                     
423D: D6 02          SUB     $02             
423F: DD 77 02       LD      (IX+$02),A      
4242: C9             RET                     
4243: 3A 80 A9       LD      A,($A980)       
4246: E6 07          AND     $07             
4248: C6 05          ADD     $05             
424A: DD BE 0F       CP      (IX+$0F)        
424D: C0             RET     NZ              
424E: 21 F4 A8       LD      HL,$A8F4        
4251: 7E             LD      A,(HL)          
4252: A7             AND     A               
4253: 28 02          JR      Z,$4257         
4255: 35             DEC     (HL)            
4256: C9             RET                     
4257: 21 C0 A8       LD      HL,$A8C0        
425A: 11 28 AA       LD      DE,$AA28        
425D: 3A C6 A8       LD      A,($A8C6)       
4260: A7             AND     A               
4261: C8             RET     Z               
4262: 47             LD      B,A             
4263: 7E             LD      A,(HL)          
4264: A7             AND     A               
4265: CA 71 42       JP      Z,$4271         
4268: 7D             LD      A,L             
4269: C6 10          ADD     $10             
426B: 6F             LD      L,A             
426C: 13             INC     DE              
426D: 13             INC     DE              
426E: 10 F3          DJNZ    $4263           
4270: C9             RET                     
4271: 22 91 A9       LD      ($A991),HL      
4274: ED 53 93 A9    LD      ($A993),DE      
4278: 3A D6 A8       LD      A,($A8D6)       
427B: 57             LD      D,A             
427C: 87             ADD     A,A             
427D: 4F             LD      C,A             
427E: 3E 78          LD      A,$78           
4280: FD 96 31       SUB     (IY+$31)        
4283: 82             ADD     A,D             
4284: B9             CP      C               
4285: 30 08          JR      NC,$428F        
4287: 3E 84          LD      A,$84           
4289: FD 96 00       SUB     (IY+$00)        
428C: 82             ADD     A,D             
428D: B9             CP      C               
428E: D8             RET     C               
428F: DD 4E 02       LD      C,(IX+$02)      
4292: 3A 04 AD       LD      A,($AD04)       
4295: A7             AND     A               
4296: CA 9C 42       JP      Z,$429C         
4299: C3 B7 42       JP      $42B7           
429C: 3A E6 A8       LD      A,($A8E6)       
429F: 57             LD      D,A             
42A0: 87             ADD     A,A             
42A1: 4F             LD      C,A             
42A2: 3E 84          LD      A,$84           
42A4: FD 96 00       SUB     (IY+$00)        
42A7: 82             ADD     A,D             
42A8: B9             CP      C               
42A9: D0             RET     NC              
42AA: 3E 78          LD      A,$78           
42AC: FD 96 31       SUB     (IY+$31)        
42AF: 38 04          JR      C,$42B5         
42B1: 0E 00          LD      C,$00           
42B3: 18 02          JR      $42B7           
42B5: 0E 01          LD      C,$01           
42B7: FD 56 31       LD      D,(IY+$31)      
42BA: DD 5E 03       LD      E,(IX+$03)      
42BD: FD 66 00       LD      H,(IY+$00)      
42C0: DD 6E 05       LD      L,(IX+$05)      
42C3: D9             EXX                     
42C4: DD E5          PUSH    IX              
42C6: FD E5          PUSH    IY              
42C8: DD 2A 91 A9    LD      IX,($A991)      
42CC: FD 2A 93 A9    LD      IY,($A993)      
42D0: D9             EXX                     
42D1: DD 73 03       LD      (IX+$03),E      
42D4: FD 72 31       LD      (IY+$31),D      
42D7: DD 75 05       LD      (IX+$05),L      
42DA: FD 74 00       LD      (IY+$00),H      
42DD: DD 71 01       LD      (IX+$01),C      
42E0: 3A 04 AD       LD      A,($AD04)       
42E3: FE 04          CP      $04             
42E5: CA AE 43       JP      Z,$43AE         
42E8: A7             AND     A               
42E9: C2 13 43       JP      NZ,$4313        
42EC: FD 36 01 4F    LD      (IY+$01),$4F    
42F0: 79             LD      A,C             
42F1: 0F             RRCA                    
42F2: CB 2F          SRA     A               
42F4: E6 C0          AND     $C0             
42F6: C6 0B          ADD     $0B             
42F8: FD 77 30       LD      (IY+$30),A      
42FB: DD 36 07 00    LD      (IX+$07),$00    
42FF: DD 36 08 FF    LD      (IX+$08),$FF    
4303: DD 35 00       DEC     (IX+$00)        
4306: 3A F6 A8       LD      A,($A8F6)       
4309: 32 F4 A8       LD      ($A8F4),A       
430C: FD E1          POP     IY              
430E: DD E1          POP     IX              
4310: C3 64 56       JP      $5664           
4313: 3A 04 AD       LD      A,($AD04)       
4316: FE 03          CP      $03             
4318: CA 6F 43       JP      Z,$436F         
431B: D2 4C 43       JP      NC,$434C        
431E: 21 7F AC       LD      HL,$AC7F        
4321: CD B8 33       CALL    $33B8           
4324: DD 77 01       LD      (IX+$01),A      
4327: DD 7E 0F       LD      A,(IX+$0F)      
432A: 0F             RRCA                    
432B: E6 80          AND     $80             
432D: C6 40          ADD     $40             
432F: DD 86 01       ADD     A,(IX+$01)      
4332: DD 77 02       LD      (IX+$02),A      
4335: CD AF 3F       CALL    $3FAF           
4338: DD 35 00       DEC     (IX+$00)        
433B: 3A F6 A8       LD      A,($A8F6)       
433E: 32 F4 A8       LD      ($A8F4),A       
4341: DD 36 0E 00    LD      (IX+$0E),$00    
4345: FD E1          POP     IY              
4347: DD E1          POP     IX              
4349: C3 6E 56       JP      $566E           
434C: 21 7F AC       LD      HL,$AC7F        
434F: CD B8 33       CALL    $33B8           
4352: DD 77 01       LD      (IX+$01),A      
4355: DD 77 02       LD      (IX+$02),A      
4358: CD AF 3F       CALL    $3FAF           
435B: DD 35 00       DEC     (IX+$00)        
435E: 3A F6 A8       LD      A,($A8F6)       
4361: 32 F4 A8       LD      ($A8F4),A       
4364: DD 36 0E 00    LD      (IX+$0E),$00    
4368: FD E1          POP     IY              
436A: DD E1          POP     IX              
436C: C3 74 56       JP      $5674           
436F: C5             PUSH    BC              
4370: 79             LD      A,C             
4371: C6 40          ADD     $40             
4373: E6 80          AND     $80             
4375: 79             LD      A,C             
4376: 20 07          JR      NZ,$437F        
4378: C6 1A          ADD     $1A             
437A: DD 77 02       LD      (IX+$02),A      
437D: 18 05          JR      $4384           
437F: D6 1A          SUB     $1A             
4381: DD 77 02       LD      (IX+$02),A      
4384: CD 8E 59       CALL    $598E           
4387: DD 73 0A       LD      (IX+$0A),E      
438A: DD 72 0B       LD      (IX+$0B),D      
438D: DD 71 0C       LD      (IX+$0C),C      
4390: DD 70 0D       LD      (IX+$0D),B      
4393: C1             POP     BC              
4394: DD 71 02       LD      (IX+$02),C      
4397: CD AF 3F       CALL    $3FAF           
439A: DD 36 0E 20    LD      (IX+$0E),$20    
439E: DD 35 00       DEC     (IX+$00)        
43A1: 3A F6 A8       LD      A,($A8F6)       
43A4: 32 F4 A8       LD      ($A8F4),A       
43A7: FD E1          POP     IY              
43A9: DD E1          POP     IX              
43AB: C3 6E 56       JP      $566E           
43AE: 3A E6 A8       LD      A,($A8E6)       
43B1: DD 77 04       LD      (IX+$04),A      
43B4: C3 13 43       JP      $4313           
43B7: 3A C6 AC       LD      A,($ACC6)       
43BA: 3C             INC     A               
43BB: C8             RET     Z               
43BC: 3A 0D AD       LD      A,($AD0D)       
43BF: A7             AND     A               
43C0: 20 2E          JR      NZ,$43F0        
43C2: 3A 80 A9       LD      A,($A980)       
43C5: E6 07          AND     $07             
43C7: FE 05          CP      $05             
43C9: C0             RET     NZ              
43CA: DD 21 A0 A8    LD      IX,$A8A0        
43CE: FD 21 24 AA    LD      IY,$AA24        
43D2: 3A 02 AD       LD      A,($AD02)       
43D5: DD B6 00       OR      (IX+$00)        
43D8: DD B6 10       OR      (IX+$10)        
43DB: C0             RET     NZ              
43DC: 3E FF          LD      A,$FF           
43DE: 32 0D AD       LD      ($AD0D),A       
43E1: DD 36 04 07    LD      (IX+$04),$07    
43E5: C3 DB 46       JP      $46DB           
43E8: AF             XOR     A               
43E9: 86             ADD     A,(HL)          
43EA: 23             INC     HL              
43EB: 10 FC          DJNZ    $43E9           
43ED: C3 AD 07       JP      $07AD           
43F0: DD 21 A0 A8    LD      IX,$A8A0        
43F4: FD 21 24 AA    LD      IY,$AA24        
43F8: DD 7E 00       LD      A,(IX+$00)      
43FB: A7             AND     A               
43FC: CA 35 45       JP      Z,$4535         
43FF: 3C             INC     A               
4400: C2 40 45       JP      NZ,$4540        
4403: DD 66 0C       LD      H,(IX+$0C)      
4406: DD 6E 0D       LD      L,(IX+$0D)      
4409: ED 5B 08 A8    LD      DE,($A808)      
440D: 19             ADD     HL,DE           
440E: FD 56 31       LD      D,(IY+$31)      
4411: DD 5E 03       LD      E,(IX+$03)      
4414: 19             ADD     HL,DE           
4415: FD 74 31       LD      (IY+$31),H      
4418: DD 75 03       LD      (IX+$03),L      
441B: DD 66 1C       LD      H,(IX+$1C)      
441E: DD 6E 1D       LD      L,(IX+$1D)      
4421: ED 5B 0A A8    LD      DE,($A80A)      
4425: 19             ADD     HL,DE           
4426: FD 56 00       LD      D,(IY+$00)      
4429: DD 5E 05       LD      E,(IX+$05)      
442C: 19             ADD     HL,DE           
442D: FD 74 00       LD      (IY+$00),H      
4430: DD 75 05       LD      (IX+$05),L      
4433: FD 7E 31       LD      A,(IY+$31)      
4436: C6 10          ADD     $10             
4438: FD 77 33       LD      (IY+$33),A      
443B: FD 7E 00       LD      A,(IY+$00)      
443E: FD 77 02       LD      (IY+$02),A      
4441: CD 47 44       CALL    $4447           
4444: C3 F0 46       JP      $46F0           
4447: CD C4 3C       CALL    $3CC4           
444A: DA DB 46       JP      C,$46DB         
444D: 3A 04 AD       LD      A,($AD04)       
4450: 57             LD      D,A             
4451: FE 04          CP      $04             
4453: CA A2 44       JP      Z,$44A2         
4456: 7A             LD      A,D             
4457: 87             ADD     A,A             
4458: 87             ADD     A,A             
4459: 87             ADD     A,A             
445A: 87             ADD     A,A             
445B: 47             LD      B,A             
445C: 3A 80 A9       LD      A,($A980)       
445F: E6 02          AND     $02             
4461: 80             ADD     A,B             
4462: 47             LD      B,A             
4463: 3E 07          LD      A,$07           
4465: DD 96 04       SUB     (IX+$04)        
4468: 0F             RRCA                    
4469: E6 03          AND     $03             
446B: 5F             LD      E,A             
446C: 87             ADD     A,A             
446D: 87             ADD     A,A             
446E: 80             ADD     A,B             
446F: 21 F1 44       LD      HL,$44F1        
4472: DF             RST     0X18            
4473: 46             LD      B,(HL)          
4474: 23             INC     HL              
4475: 4E             LD      C,(HL)          
4476: 21 31 45       LD      HL,$4531        
4479: 7A             LD      A,D             
447A: DF             RST     0X18            
447B: 56             LD      D,(HL)          
447C: DD 7E 02       LD      A,(IX+$02)      
447F: C6 40          ADD     $40             
4481: FE 80          CP      $80             
4483: 38 10          JR      C,$4495         
4485: FD 70 01       LD      (IY+$01),B      
4488: FD 71 03       LD      (IY+$03),C      
448B: 7A             LD      A,D             
448C: C6 80          ADD     $80             
448E: FD 77 30       LD      (IY+$30),A      
4491: FD 77 32       LD      (IY+$32),A      
4494: C9             RET                     
4495: FD 71 01       LD      (IY+$01),C      
4498: FD 70 03       LD      (IY+$03),B      
449B: FD 72 30       LD      (IY+$30),D      
449E: FD 72 32       LD      (IY+$32),D      
44A1: C9             RET                     
44A2: DD 7E 04       LD      A,(IX+$04)      
44A5: 5F             LD      E,A             
44A6: FE 07          CP      $07             
44A8: CA BF 44       JP      Z,$44BF         
44AB: DD 34 06       INC     (IX+$06)        
44AE: DD 4E 06       LD      C,(IX+$06)      
44B1: CB 79          BIT     7,C             
44B3: 20 14          JR      NZ,$44C9        
44B5: 7B             LD      A,E             
44B6: C6 02          ADD     $02             
44B8: B9             CP      C               
44B9: 30 04          JR      NC,$44BF        
44BB: DD 36 06 80    LD      (IX+$06),$80    
44BF: FD 36 30 70    LD      (IY+$30),$70    
44C3: FD 36 32 70    LD      (IY+$32),$70    
44C7: 18 13          JR      $44DC           
44C9: 79             LD      A,C             
44CA: E6 7F          AND     $7F             
44CC: FE 03          CP      $03             
44CE: 38 04          JR      C,$44D4         
44D0: DD 36 06 00    LD      (IX+$06),$00    
44D4: FD 36 30 51    LD      (IY+$30),$51    
44D8: FD 36 32 51    LD      (IY+$32),$51    
44DC: 11 02 02       LD      DE,$0202        
44DF: 21 D5 D4       LD      HL,$D4D5        
44E2: 3A 80 A9       LD      A,($A980)       
44E5: CB 57          BIT     2,A             
44E7: 20 01          JR      NZ,$44EA        
44E9: 19             ADD     HL,DE           
44EA: FD 75 01       LD      (IY+$01),L      
44ED: FD 74 03       LD      (IY+$03),H      
44F0: C9             RET                     
44F1: 39             ADD     HL,SP           
44F2: 38 39          JR      C,$452D         
44F4: 38 3B          JR      C,$4531         
44F6: 3A 3D 3C       LD      A,($3C3D)       
44F9: 3B             DEC     SP              
44FA: 3A 3D 3C       LD      A,($3C3D)       
44FD: 3D             DEC     A               
44FE: 3C             INC     A               
44FF: 3F             CCF                     
4500: 3E B0          LD      A,$B0           
4502: B1             OR      C               
4503: B2             OR      D               
4504: B3             OR      E               
4505: B4             OR      H               
4506: B5             OR      L               
4507: B6             OR      (HL)            
4508: B7             OR      A               
4509: B8             CP      B               
450A: B9             CP      C               
450B: BA             CP      D               
450C: BB             CP      E               
450D: BC             CP      H               
450E: BD             CP      L               
450F: BE             CP      (HL)            
4510: BF             CP      A               
4511: C0             RET     NZ              
4512: C1             POP     BC              
4513: C2 C3 C4       JP      NZ,$C4C3        
4516: C5             PUSH    BC              
4517: C6 C7          ADD     $C7             
4519: C6 C7          ADD     $C7             
451B: C8             RET     Z               
451C: C9             RET                     
451D: C8             RET     Z               
451E: C9             RET                     
451F: CA CB CC       JP      Z,$CCCB         
4522: CD CC CD       CALL    $CDCC           
4525: CE CF          ADC     $CF             
4527: D0             RET     NC              
4528: D1             POP     DE              
4529: CE CF          ADC     $CF             
452B: D0             RET     NC              
452C: D1             POP     DE              
452D: D0             RET     NC              
452E: D1             POP     DE              
452F: D2 D3 E9       JP      NC,$E9D3        
4532: 58             LD      E,B             
4533: 6F             LD      L,A             
4534: 6E             LD      L,(HL)          
4535: DD 7E 0E       LD      A,(IX+$0E)      
4538: A7             AND     A               
4539: CA 63 46       JP      Z,$4663         
453C: DD 35 0E       DEC     (IX+$0E)        
453F: C9             RET                     
4540: 4F             LD      C,A             
4541: DD 7E 04       LD      A,(IX+$04)      
4544: A7             AND     A               
4545: 28 0D          JR      Z,$4554         
4547: DD 35 04       DEC     (IX+$04)        
454A: DD 36 00 FF    LD      (IX+$00),$FF    
454E: CD 83 56       CALL    $5683           
4551: C3 03 44       JP      $4403           
4554: 79             LD      A,C             
4555: FE F0          CP      $F0             
4557: C2 B3 45       JP      NZ,$45B3        
455A: AF             XOR     A               
455B: 32 DC A8       LD      ($A8DC),A       
455E: CD 34 56       CALL    $5634           
4561: CD D2 56       CALL    $56D2           
4564: 21 10 A8       LD      HL,$A810        
4567: 11 10 00       LD      DE,$0010        
456A: 06 0F          LD      B,$0F           
456C: 0E 14          LD      C,$14           
456E: 7E             LD      A,(HL)          
456F: 3C             INC     A               
4570: 20 22          JR      NZ,$4594        
4572: 71             LD      (HL),C          
4573: D9             EXX                     
4574: 11 02 04       LD      DE,$0402        
4577: FF             RST     0X38            
4578: D9             EXX                     
4579: 19             ADD     HL,DE           
457A: 79             LD      A,C             
457B: C6 0A          ADD     $0A             
457D: 4F             LD      C,A             
457E: 10 EE          DJNZ    $456E           
4580: 0E 3C          LD      C,$3C           
4582: 3E FE          LD      A,$FE           
4584: 32 C6 AC       LD      ($ACC6),A       
4587: DD 36 00 E4    LD      (IX+$00),$E4    
458B: FD 36 30 3D    LD      (IY+$30),$3D    
458F: FD 36 32 3D    LD      (IY+$32),$3D    
4593: C9             RET                     
4594: 3C             INC     A               
4595: 20 E2          JR      NZ,$4579        
4597: 36 00          LD      (HL),$00        
4599: 18 DE          JR      $4579           
459B: 16 A7          LD      D,$A7           
459D: 13             INC     DE              
459E: 96             SUB     (HL)            
459F: ED                                  
45A0: DC F1 8C       CALL    C,$8CF1         
45A3: 68             LD      L,B             
45A4: 3B             DEC     SP              
45A5: 0D             DEC     C               
45A6: ED                                  
45A7: F1             POP     AF              
45A8: 9B             SBC     E               
45A9: 13             INC     DE              
45AA: 13             INC     DE              
45AB: 13             INC     DE              
45AC: 13             INC     DE              
45AD: F1             POP     AF              
45AE: 88             ADC     A,B             
45AF: DC ED 11       CALL    C,$11ED         
45B2: B9             CP      C               
45B3: CD 60 2B       CALL    $2B60           
45B6: FD 7E 31       LD      A,(IY+$31)      
45B9: 47             LD      B,A             
45BA: C6 13          ADD     $13             
45BC: FE 03          CP      $03             
45BE: 38 15          JR      C,$45D5         
45C0: 78             LD      A,B             
45C1: C6 10          ADD     $10             
45C3: FD 77 33       LD      (IY+$33),A      
45C6: FD 7E 00       LD      A,(IY+$00)      
45C9: 47             LD      B,A             
45CA: C6 08          ADD     $08             
45CC: FE 28          CP      $28             
45CE: 38 05          JR      C,$45D5         
45D0: FD 70 02       LD      (IY+$02),B      
45D3: 18 08          JR      $45DD           
45D5: FD 36 01 FF    LD      (IY+$01),$FF    
45D9: FD 36 03 FF    LD      (IY+$03),$FF    
45DD: DD 7E 00       LD      A,(IX+$00)      
45E0: FE B4          CP      $B4             
45E2: 28 3F          JR      Z,$4623         
45E4: 38 13          JR      C,$45F9         
45E6: D6 B4          SUB     $B4             
45E8: 0F             RRCA                    
45E9: 0F             RRCA                    
45EA: 0F             RRCA                    
45EB: 3D             DEC     A               
45EC: E6 07          AND     $07             
45EE: 21 1B 46       LD      HL,$461B        
45F1: CF             RST     0X08            
45F2: FD 77 03       LD      (IY+$03),A      
45F5: 3C             INC     A               
45F6: FD 77 01       LD      (IY+$01),A      
45F9: DD 35 00       DEC     (IX+$00)        
45FC: CA 46 46       JP      Z,$4646         
45FF: DD 7E 00       LD      A,(IX+$00)      
4602: FE 5A          CP      $5A             
4604: C0             RET     NZ              
4605: FD 36 01 FF    LD      (IY+$01),$FF    
4609: FD 36 03 FF    LD      (IY+$03),$FF    
460D: C9             RET                     
460E: 21 7C A6       LD      HL,$A67C        
4611: 7E             LD      A,(HL)          
4612: 4F             LD      C,A             
4613: 3A 43 AB       LD      A,($AB43)       
4616: 91             SUB     C               
4617: C2 43 46       JP      NZ,$4643        
461A: C9             RET                     
461B: 94             SUB     H               
461C: 96             SUB     (HL)            
461D: 96             SUB     (HL)            
461E: 94             SUB     H               
461F: 92             SUB     D               
4620: 90             SUB     B               
4621: 90             SUB     B               
4622: 94             SUB     H               
4623: DD 35 00       DEC     (IX+$00)        
4626: FD 36 01 FE    LD      (IY+$01),$FE    
462A: FD 36 03 FD    LD      (IY+$03),$FD    
462E: FD 36 30 6C    LD      (IY+$30),$6C    
4632: FD 36 32 6C    LD      (IY+$32),$6C    
4636: 3A 00 A8       LD      A,($A800)       
4639: 3C             INC     A               
463A: CC 0B 58       CALL    Z,$580B         
463D: 11 0D 04       LD      DE,$040D        
4640: C3 38 00       JP      $0038           
4643: C3 1B 46       JP      $461B           
4646: 3E FF          LD      A,$FF           
4648: 32 C6 AC       LD      ($ACC6),A       
464B: DD 36 00 00    LD      (IX+$00),$00    
464F: 21 43 AB       LD      HL,$AB43        
4652: 7E             LD      A,(HL)          
4653: FE 7C          CP      $7C             
4655: C2 60 46       JP      NZ,$4660        
4658: 23             INC     HL              
4659: 7E             LD      A,(HL)          
465A: FE 10          CP      $10             
465C: C8             RET     Z               
465D: FE 05          CP      $05             
465F: C8             RET     Z               
4660: C3 9B 45       JP      $459B           
4663: 3A C6 AC       LD      A,($ACC6)       
4666: A7             AND     A               
4667: C0             RET     NZ              
4668: 3A 02 A8       LD      A,($A802)       
466B: 47             LD      B,A             
466C: 3A 80 A9       LD      A,($A980)       
466F: 4F             LD      C,A             
4670: 3E 10          LD      A,$10           
4672: CB 59          BIT     3,C             
4674: 20 02          JR      NZ,$4678        
4676: ED 44          NEG                     
4678: 80             ADD     A,B             
4679: 0F             RRCA                    
467A: 0F             RRCA                    
467B: E6 3E          AND     $3E             
467D: 21 84 3C       LD      HL,$3C84        
4680: CF             RST     0X08            
4681: FD 77 31       LD      (IY+$31),A      
4684: 23             INC     HL              
4685: 7E             LD      A,(HL)          
4686: FD 77 00       LD      (IY+$00),A      
4689: 78             LD      A,B             
468A: C6 C0          ADD     $C0             
468C: E6 80          AND     $80             
468E: DD 77 02       LD      (IX+$02),A      
4691: CD BA 46       CALL    $46BA           
4694: DD 7E 04       LD      A,(IX+$04)      
4697: FE 06          CP      $06             
4699: 30 04          JR      NC,$469F        
469B: DD 36 04 05    LD      (IX+$04),$05    
469F: DD 36 00 FF    LD      (IX+$00),$FF    
46A3: C3 F7 57       JP      $57F7           
46A6: 3A 80 A9       LD      A,($A980)       
46A9: 4F             LD      C,A             
46AA: E6 1C          AND     $1C             
46AC: CB 41          BIT     0,C             
46AE: 20 02          JR      NZ,$46B2        
46B0: ED 44          NEG                     
46B2: 80             ADD     A,B             
46B3: 0F             RRCA                    
46B4: 0F             RRCA                    
46B5: E6 3E          AND     $3E             
46B7: C3 7D 46       JP      $467D           
46BA: 21 CE 46       LD      HL,$46CE        
46BD: E5             PUSH    HL              
46BE: 3A 04 AD       LD      A,($AD04)       
46C1: E6 07          AND     $07             
46C3: F7             RST     0X30            
46C4: 42             LD      B,D             
46C5: 59             LD      E,C             
46C6: 4E             LD      C,(HL)          
46C7: 59             LD      E,C             
46C8: 4E             LD      C,(HL)          
46C9: 59             LD      E,C             
46CA: 65             LD      H,L             
46CB: 59             LD      E,C             
46CC: 6B             LD      L,E             
46CD: 59             LD      E,C             
46CE: DD 72 0C       LD      (IX+$0C),D      
46D1: DD 73 0D       LD      (IX+$0D),E      
46D4: DD 70 1C       LD      (IX+$1C),B      
46D7: DD 71 1D       LD      (IX+$1D),C      
46DA: C9             RET                     
46DB: AF             XOR     A               
46DC: DD 77 00       LD      (IX+$00),A      
46DF: FD 77 00       LD      (IY+$00),A      
46E2: FD 77 02       LD      (IY+$02),A      
46E5: FD 77 31       LD      (IY+$31),A      
46E8: FD 77 33       LD      (IY+$33),A      
46EB: DD 36 0E 5F    LD      (IX+$0E),$5F    
46EF: C9             RET                     
46F0: DD 7E 00       LD      A,(IX+$00)      
46F3: 3C             INC     A               
46F4: C0             RET     NZ              
46F5: 3A 17 A8       LD      A,($A817)       
46F8: A7             AND     A               
46F9: C0             RET     NZ              
46FA: 06 02          LD      B,$02           
46FC: 3A 27 A8       LD      A,($A827)       
46FF: 57             LD      D,A             
4700: 87             ADD     A,A             
4701: 5F             LD      E,A             
4702: FD 7E 00       LD      A,(IY+$00)      
4705: C6 08          ADD     $08             
4707: FE 28          CP      $28             
4709: 38 1B          JR      C,$4726         
470B: FD 7E 31       LD      A,(IY+$31)      
470E: C6 10          ADD     $10             
4710: FE 20          CP      $20             
4712: 38 12          JR      C,$4726         
4714: 3E 84          LD      A,$84           
4716: FD 96 00       SUB     (IY+$00)        
4719: 82             ADD     A,D             
471A: BB             CP      E               
471B: 30 17          JR      NC,$4734        
471D: 3E 78          LD      A,$78           
471F: FD 96 31       SUB     (IY+$31)        
4722: 82             ADD     A,D             
4723: BB             CP      E               
4724: 30 0E          JR      NC,$4734        
4726: D9             EXX                     
4727: 11 10 00       LD      DE,$0010        
472A: DD 19          ADD     IX,DE           
472C: FD 23          INC     IY              
472E: FD 23          INC     IY              
4730: D9             EXX                     
4731: 10 CF          DJNZ    $4702           
4733: C9             RET                     
4734: 21 30 A8       LD      HL,$A830        
4737: D9             EXX                     
4738: 21 16 AA       LD      HL,$AA16        
473B: 06 02          LD      B,$02           
473D: D9             EXX                     
473E: 7E             LD      A,(HL)          
473F: A7             AND     A               
4740: 28 0A          JR      Z,$474C         
4742: 11 10 00       LD      DE,$0010        
4745: 19             ADD     HL,DE           
4746: D9             EXX                     
4747: 23             INC     HL              
4748: 23             INC     HL              
4749: 10 F2          DJNZ    $473D           
474B: C9             RET                     
474C: 22 91 A9       LD      ($A991),HL      
474F: D9             EXX                     
4750: 22 93 A9       LD      ($A993),HL      
4753: CD 5F 56       CALL    $565F           
4756: 21 7F AC       LD      HL,$AC7F        
4759: CD B8 33       CALL    $33B8           
475C: 67             LD      H,A             
475D: EB             EX      DE,HL           
475E: 21 B4 A8       LD      HL,$A8B4        
4761: 34             INC     (HL)            
4762: 3E 18          LD      A,$18           
4764: CB 46          BIT     0,(HL)          
4766: 20 02          JR      NZ,$476A        
4768: ED 44          NEG                     
476A: EB             EX      DE,HL           
476B: 84             ADD     A,H             
476C: FD 46 31       LD      B,(IY+$31)      
476F: FD 4E 00       LD      C,(IY+$00)      
4772: DD 2A 91 A9    LD      IX,($A991)      
4776: FD 2A 93 A9    LD      IY,($A993)      
477A: DD 77 02       LD      (IX+$02),A      
477D: FD 70 31       LD      (IY+$31),B      
4780: FD 71 00       LD      (IY+$00),C      
4783: 21 95 47       LD      HL,$4795        
4786: E5             PUSH    HL              
4787: 3A 04 AD       LD      A,($AD04)       
478A: F7             RST     0X30            
478B: 8E             ADC     A,(HL)          
478C: 59             LD      E,C             
478D: 8E             ADC     A,(HL)          
478E: 59             LD      E,C             
478F: 94             SUB     H               
4790: 59             LD      E,C             
4791: 94             SUB     H               
4792: 59             LD      E,C             
4793: 94             SUB     H               
4794: 59             LD      E,C             
4795: DD 73 0A       LD      (IX+$0A),E      
4798: DD 72 0B       LD      (IX+$0B),D      
479B: DD 71 0C       LD      (IX+$0C),C      
479E: DD 70 0D       LD      (IX+$0D),B      
47A1: FD 36 01 4D    LD      (IY+$01),$4D    
47A5: FD 36 30 62    LD      (IY+$30),$62    
47A9: DD 35 00       DEC     (IX+$00)        
47AC: 3A 14 A8       LD      A,($A814)       
47AF: 32 17 A8       LD      ($A817),A       
47B2: C9             RET                     
47B3: 3A 04 AD       LD      A,($AD04)       
47B6: FE 04          CP      $04             
47B8: C8             RET     Z               
47B9: DD 21 F0 A8    LD      IX,$A8F0        
47BD: FD 21 2E AA    LD      IY,$AA2E        
47C1: DD 7E 00       LD      A,(IX+$00)      
47C4: A7             AND     A               
47C5: CA 53 48       JP      Z,$4853         
47C8: 3C             INC     A               
47C9: C2 F2 47       JP      NZ,$47F2        
47CC: CD 05 3E       CALL    $3E05           
47CF: CD 83 2B       CALL    $2B83           
47D2: DA AD 48       JP      C,$48AD         
47D5: 3A 80 A9       LD      A,($A980)       
47D8: 0F             RRCA                    
47D9: 0F             RRCA                    
47DA: 0F             RRCA                    
47DB: 0F             RRCA                    
47DC: E6 07          AND     $07             
47DE: 21 EA 47       LD      HL,$47EA        
47E1: CF             RST     0X08            
47E2: FD 77 01       LD      (IY+$01),A      
47E5: FD 36 30 75    LD      (IY+$30),$75    
47E9: C9             RET                     
47EA: 00             NOP                     
47EB: 01 02 03       LD      BC,$0302        
47EE: 03             INC     BC              
47EF: 02             LD      (BC),A          
47F0: 01 00 CD       LD      BC,$CD00        
47F3: 60             LD      H,B             
47F4: 2B             DEC     HL              
47F5: DD 7E 00       LD      A,(IX+$00)      
47F8: FE 10          CP      $10             
47FA: CA 31 48       JP      Z,$4831         
47FD: FE 3C          CP      $3C             
47FF: D2 09 48       JP      NC,$4809        
4802: DD 35 00       DEC     (IX+$00)        
4805: C0             RET     NZ              
4806: C3 AD 48       JP      $48AD           
4809: DD 36 00 3B    LD      (IX+$00),$3B    
480D: CD FF 57       CALL    $57FF           
4810: DD 7E 07       LD      A,(IX+$07)      
4813: FE 04          CP      $04             
4815: D2 24 48       JP      NC,$4824        
4818: 21 2D 48       LD      HL,$482D        
481B: CF             RST     0X08            
481C: FD 77 01       LD      (IY+$01),A      
481F: FD 36 30 6C    LD      (IY+$30),$6C    
4823: C9             RET                     
4824: FD 36 01 8F    LD      (IY+$01),$8F    
4828: FD 36 30 6C    LD      (IY+$30),$6C    
482C: C9             RET                     
482D: F9             LD      SP,HL           
482E: FC 8D 8E       CALL    M,$8E8D         
4831: DD 35 00       DEC     (IX+$00)        
4834: DD 7E 07       LD      A,(IX+$07)      
4837: DD 34 07       INC     (IX+$07)        
483A: FE 04          CP      $04             
483C: D2 49 48       JP      NC,$4849        
483F: 21 4F 48       LD      HL,$484F        
4842: DF             RST     0X18            
4843: 5E             LD      E,(HL)          
4844: 16 04          LD      D,$04           
4846: C3 38 00       JP      $0038           
4849: 11 0F 04       LD      DE,$040F        
484C: C3 38 00       JP      $0038           
484F: 0A             LD      A,(BC)          
4850: 0C             INC     C               
4851: 0D             DEC     C               
4852: 0E 3A          LD      C,$3A           
4854: 0D             DEC     C               
4855: AD             XOR     L               
4856: A7             AND     A               
4857: C0             RET     NZ              
4858: 3A 80 A9       LD      A,($A980)       
485B: E6 01          AND     $01             
485D: C8             RET     Z               
485E: DD 35 0E       DEC     (IX+$0E)        
4861: C0             RET     NZ              
4862: 3A 02 A8       LD      A,($A802)       
4865: C6 08          ADD     $08             
4867: 0F             RRCA                    
4868: 0F             RRCA                    
4869: 0F             RRCA                    
486A: E6 1E          AND     $1E             
486C: 21 8D 48       LD      HL,$488D        
486F: CF             RST     0X08            
4870: FD 77 31       LD      (IY+$31),A      
4873: 23             INC     HL              
4874: 7E             LD      A,(HL)          
4875: FD 77 00       LD      (IY+$00),A      
4878: DD 36 0A 00    LD      (IX+$0A),$00    
487C: DD 36 0B 00    LD      (IX+$0B),$00    
4880: DD 36 0C 40    LD      (IX+$0C),$40    
4884: DD 36 0D 00    LD      (IX+$0D),$00    
4888: DD 36 00 FF    LD      (IX+$00),$FF    
488C: C9             RET                     
488D: F0             RET     P               
488E: 40             LD      B,B             
488F: F0             RET     P               
4890: 80             ADD     A,B             
4891: F0             RET     P               
4892: F8             RET     M               
4893: 60             LD      H,B             
4894: F8             RET     M               
4895: 80             ADD     A,B             
4896: F8             RET     M               
4897: A0             AND     B               
4898: F8             RET     M               
4899: 10 F8          DJNZ    $4893           
489B: 00             NOP                     
489C: 80             ADD     A,B             
489D: 00             NOP                     
489E: 90             SUB     B               
489F: 10 10          DJNZ    $48B1           
48A1: 30 10          JR      NC,$48B3        
48A3: 60             LD      H,B             
48A4: 10 80          DJNZ    $4826           
48A6: 10 A0          DJNZ    $4848           
48A8: 10 C0          DJNZ    $486A           
48AA: 10 F0          DJNZ    $489C           
48AC: 28 DD          JR      Z,$488B         
48AE: 36 00          LD      (HL),$00        
48B0: 00             NOP                     
48B1: FD 36 00 00    LD      (IY+$00),$00    
48B5: FD 36 31 00    LD      (IY+$31),$00    
48B9: DD 36 0E F0    LD      (IX+$0E),$F0    
48BD: C9             RET                     
48BE: CD E7 48       CALL    $48E7           
48C1: CD 41 49       CALL    $4941           
48C4: CD 11 49       CALL    $4911           
48C7: CD 84 49       CALL    $4984           
48CA: CD D6 49       CALL    $49D6           
48CD: C9             RET                     
48CE: 2C             INC     L               
48CF: A7             AND     A               
48D0: 13             INC     DE              
48D1: FD                                  
48D2: 3B             DEC     SP              
48D3: 88             ADC     A,B             
48D4: 0D             DEC     C               
48D5: DC F1 BF       CALL    C,$BFF1         
48D8: 68             LD      L,B             
48D9: 0D             DEC     C               
48DA: D7             RST     0X10            
48DB: F1             POP     AF              
48DC: FD                                  
48DD: 3B             DEC     SP              
48DE: FD DC FD A5    CALL    C,$A5FD         
48E2: 57             LD      D,A             
48E3: ED                                  
48E4: F1             POP     AF              
48E5: 52             LD      D,D             
48E6: B9             CP      C               
48E7: 3A AE A9       LD      A,($A9AE)       
48EA: 0F             RRCA                    
48EB: 0F             RRCA                    
48EC: 0F             RRCA                    
48ED: 21 83 A9       LD      HL,$A983        
48F0: CB 16          RL      (HL)            
48F2: 7E             LD      A,(HL)          
48F3: E6 07          AND     $07             
48F5: FE 01          CP      $01             
48F7: C0             RET     NZ              
48F8: CD F1 57       CALL    $57F1           
48FB: 0E 01          LD      C,$01           
48FD: C3 6E 49       JP      $496E           
4900: BC             CP      H               
4901: A6             AND     (HL)            
4902: 05             DEC     B               
4903: 30 F1          JR      NC,$48F6        
4905: 7C             LD      A,H             
4906: 68             LD      L,B             
4907: 3B             DEC     SP              
4908: A5             AND     L               
4909: 38 FD          JR      C,$4908         
490B: F1             POP     AF              
490C: 96             SUB     (HL)            
490D: 5D             LD      E,L             
490E: 17             RLA                     
490F: 9B             SBC     E               
4910: B9             CP      C               
4911: 3A AE A9       LD      A,($A9AE)       
4914: 21 CA A9       LD      HL,$A9CA        
4917: 0F             RRCA                    
4918: 0F             RRCA                    
4919: CB 16          RL      (HL)            
491B: 7E             LD      A,(HL)          
491C: E6 07          AND     $07             
491E: FE 01          CP      $01             
4920: C0             RET     NZ              
4921: EB             EX      DE,HL           
4922: CD F1 57       CALL    $57F1           
4925: 21 82 A9       LD      HL,$A982        
4928: 34             INC     (HL)            
4929: EB             EX      DE,HL           
492A: 23             INC     HL              
492B: 7E             LD      A,(HL)          
492C: C6 10          ADD     $10             
492E: 77             LD      (HL),A          
492F: 47             LD      B,A             
4930: 23             INC     HL              
4931: 7E             LD      A,(HL)          
4932: 90             SUB     B               
4933: D0             RET     NC              
4934: 7E             LD      A,(HL)          
4935: 4F             LD      C,A             
4936: E6 F0          AND     $F0             
4938: C6 10          ADD     $10             
493A: 2B             DEC     HL              
493B: ED 44          NEG                     
493D: 86             ADD     A,(HL)          
493E: 77             LD      (HL),A          
493F: 18 2D          JR      $496E           
4941: 3A AE A9       LD      A,($A9AE)       
4944: 21 C7 A9       LD      HL,$A9C7        
4947: 0F             RRCA                    
4948: CB 16          RL      (HL)            
494A: 7E             LD      A,(HL)          
494B: E6 07          AND     $07             
494D: FE 01          CP      $01             
494F: C0             RET     NZ              
4950: EB             EX      DE,HL           
4951: CD F1 57       CALL    $57F1           
4954: 21 81 A9       LD      HL,$A981        
4957: 34             INC     (HL)            
4958: EB             EX      DE,HL           
4959: 23             INC     HL              
495A: 7E             LD      A,(HL)          
495B: C6 10          ADD     $10             
495D: 77             LD      (HL),A          
495E: 47             LD      B,A             
495F: 23             INC     HL              
4960: 7E             LD      A,(HL)          
4961: 90             SUB     B               
4962: D0             RET     NC              
4963: 7E             LD      A,(HL)          
4964: 4F             LD      C,A             
4965: E6 F0          AND     $F0             
4967: C6 10          ADD     $10             
4969: 2B             DEC     HL              
496A: ED 44          NEG                     
496C: 86             ADD     A,(HL)          
496D: 77             LD      (HL),A          
496E: 3A C0 A9       LD      A,($A9C0)       
4971: A7             AND     A               
4972: 20 10          JR      NZ,$4984        
4974: 79             LD      A,C             
4975: E6 0F          AND     $0F             
4977: 21 86 A9       LD      HL,$A986        
497A: 86             ADD     A,(HL)          
497B: 27             DAA                     
497C: 77             LD      (HL),A          
497D: 30 02          JR      NC,$4981        
497F: 36 99          LD      (HL),$99        
4981: CD FB 4A       CALL    $4AFB           
4984: 3A 81 A9       LD      A,($A981)       
4987: A7             AND     A               
4988: C8             RET     Z               
4989: 21 84 A9       LD      HL,$A984        
498C: 7E             LD      A,(HL)          
498D: A7             AND     A               
498E: 20 07          JR      NZ,$4997        
4990: 36 30          LD      (HL),$30        
4992: 3C             INC     A               
4993: 32 0A C3       LD      ($C30A),A       
4996: C9             RET                     
4997: 35             DEC     (HL)            
4998: 28 09          JR      Z,$49A3         
499A: 7E             LD      A,(HL)          
499B: FE 18          CP      $18             
499D: C0             RET     NZ              
499E: AF             XOR     A               
499F: 32 0A C3       LD      ($C30A),A       
49A2: C9             RET                     
49A3: 21 81 A9       LD      HL,$A981        
49A6: 35             DEC     (HL)            
49A7: C9             RET                     
49A8: 0F             RRCA                    
49A9: 4F             LD      C,A             
49AA: E6 07          AND     $07             
49AC: 32 C4 A9       LD      ($A9C4),A       
49AF: 79             LD      A,C             
49B0: 0F             RRCA                    
49B1: 0F             RRCA                    
49B2: 0F             RRCA                    
49B3: E6 01          AND     $01             
49B5: 32 C6 A9       LD      ($A9C6),A       
49B8: 32 00 C2       LD      ($C200),A       
49BB: 3A 3E 0C       LD      A,($0C3E)       
49BE: 32 02 C3       LD      ($C302),A       
49C1: CD B1 00       CALL    $00B1           
49C4: 06 00          LD      B,$00           
49C6: 21 DE 27       LD      HL,$27DE        
49C9: AF             XOR     A               
49CA: 86             ADD     A,(HL)          
49CB: 23             INC     HL              
49CC: 10 FC          DJNZ    $49CA           
49CE: D6 C5          SUB     $C5             
49D0: C4 D8 00       CALL    NZ,$00D8        
49D3: C3 EB 32       JP      $32EB           
49D6: 3A 82 A9       LD      A,($A982)       
49D9: A7             AND     A               
49DA: C8             RET     Z               
49DB: 21 85 A9       LD      HL,$A985        
49DE: 7E             LD      A,(HL)          
49DF: A7             AND     A               
49E0: 20 07          JR      NZ,$49E9        
49E2: 36 30          LD      (HL),$30        
49E4: 3C             INC     A               
49E5: 32 0C C3       LD      ($C30C),A       
49E8: C9             RET                     
49E9: 35             DEC     (HL)            
49EA: 28 09          JR      Z,$49F5         
49EC: 7E             LD      A,(HL)          
49ED: FE 18          CP      $18             
49EF: C0             RET     NZ              
49F0: AF             XOR     A               
49F1: 32 0C C3       LD      ($C30C),A       
49F4: C9             RET                     
49F5: 21 82 A9       LD      HL,$A982        
49F8: 35             DEC     (HL)            
49F9: C9             RET                     
49FA: EE A6          XOR     $A6             
49FC: 14             INC     D               
49FD: A5             AND     L               
49FE: 3B             DEC     SP              
49FF: 87             ADD     A,A             
4A00: F1             POP     AF              
4A01: DC D7 BF       CALL    C,$BFD7         
4A04: F1             POP     AF              
4A05: DC C4 FD       CALL    C,$FDC4         
4A08: ED                                  
4A09: F1             POP     AF              
4A0A: 7D             LD      A,L             
4A0B: A5             AND     L               
4A0C: 38 34          JR      C,$4A42         
4A0E: B9             CP      C               
4A0F: 3A 13 32       LD      A,($3213)       
4A12: 32 F0 A9       LD      ($A9F0),A       
4A15: 3E 00          LD      A,$00           
4A17: 32 F1 A9       LD      ($A9F1),A       
4A1A: 3E FF          LD      A,$FF           
4A1C: 32 F2 A9       LD      ($A9F2),A       
4A1F: 3E 04          LD      A,$04           
4A21: 32 F3 A9       LD      ($A9F3),A       
4A24: 3E FF          LD      A,$FF           
4A26: 32 F4 A9       LD      ($A9F4),A       
4A29: 3E 08          LD      A,$08           
4A2B: 32 F6 A9       LD      ($A9F6),A       
4A2E: 21 F1 56       LD      HL,$56F1        
4A31: 22 F7 A9       LD      ($A9F7),HL      
4A34: 06 0D          LD      B,$0D           
4A36: 21 00 A4       LD      HL,$A400        
4A39: 0E 14          LD      C,$14           
4A3B: 71             LD      (HL),C          
4A3C: 23             INC     HL              
4A3D: 10 FC          DJNZ    $4A3B           
4A3F: 3E 00          LD      A,$00           
4A41: 77             LD      (HL),A          
4A42: 23             INC     HL              
4A43: 77             LD      (HL),A          
4A44: 23             INC     HL              
4A45: 06 0D          LD      B,$0D           
4A47: 71             LD      (HL),C          
4A48: 23             INC     HL              
4A49: 10 FC          DJNZ    $4A47           
4A4B: 3E 0E          LD      A,$0E           
4A4D: 06 04          LD      B,$04           
4A4F: 77             LD      (HL),A          
4A50: 23             INC     HL              
4A51: 10 FC          DJNZ    $4A4F           
4A53: 21 B1 A7       LD      HL,$A7B1        
4A56: CB 94          RES     2,H             
4A58: 3A 0C AD       LD      A,($AD0C)       
4A5B: 4F             LD      C,A             
4A5C: 3E A0          LD      A,$A0           
4A5E: 81             ADD     A,C             
4A5F: CD 19 13       CALL    $1319           
4A62: 21 D1 A5       LD      HL,$A5D1        
4A65: CB 94          RES     2,H             
4A67: 3E 20          LD      A,$20           
4A69: 81             ADD     A,C             
4A6A: CD 19 13       CALL    $1319           
4A6D: 21 10 A6       LD      HL,$A610        
4A70: CB 94          RES     2,H             
4A72: 3E A0          LD      A,$A0           
4A74: 81             ADD     A,C             
4A75: 77             LD      (HL),A          
4A76: 19             ADD     HL,DE           
4A77: 3E 20          LD      A,$20           
4A79: 81             ADD     A,C             
4A7A: 77             LD      (HL),A          
4A7B: 21 12 A6       LD      HL,$A612        
4A7E: CB 94          RES     2,H             
4A80: 3E E0          LD      A,$E0           
4A82: 81             ADD     A,C             
4A83: 77             LD      (HL),A          
4A84: 19             ADD     HL,DE           
4A85: 3E 60          LD      A,$60           
4A87: 81             ADD     A,C             
4A88: 77             LD      (HL),A          
4A89: 21 11 A6       LD      HL,$A611        
4A8C: CB 94          RES     2,H             
4A8E: 3E A0          LD      A,$A0           
4A90: 81             ADD     A,C             
4A91: 77             LD      (HL),A          
4A92: 19             ADD     HL,DE           
4A93: 3E 20          LD      A,$20           
4A95: 81             ADD     A,C             
4A96: 77             LD      (HL),A          
4A97: CD 9C 33       CALL    $339C           
4A9A: C3 1A 0F       JP      $0F1A           
4A9D: 06 0D          LD      B,$0D           
4A9F: 2A F7 A9       LD      HL,($A9F7)      
4AA2: 7E             LD      A,(HL)          
4AA3: A7             AND     A               
4AA4: EB             EX      DE,HL           
4AA5: 28 09          JR      Z,$4AB0         
4AA7: 7E             LD      A,(HL)          
4AA8: 3C             INC     A               
4AA9: CB 41          BIT     0,C             
4AAB: 28 02          JR      Z,$4AAF         
4AAD: 3D             DEC     A               
4AAE: 3D             DEC     A               
4AAF: 77             LD      (HL),A          
4AB0: CB 49          BIT     1,C             
4AB2: 11 20 00       LD      DE,$0020        
4AB5: 28 03          JR      Z,$4ABA         
4AB7: 11 E0 FF       LD      DE,$FFE0        
4ABA: 19             ADD     HL,DE           
4ABB: EB             EX      DE,HL           
4ABC: 2A F7 A9       LD      HL,($A9F7)      
4ABF: 23             INC     HL              
4AC0: CB 41          BIT     0,C             
4AC2: 28 02          JR      Z,$4AC6         
4AC4: 2B             DEC     HL              
4AC5: 2B             DEC     HL              
4AC6: 22 F7 A9       LD      ($A9F7),HL      
4AC9: 10 D7          DJNZ    $4AA2           
4ACB: C9             RET                     
4ACC: 3A B1 A9       LD      A,($A9B1)       
4ACF: E6 0F          AND     $0F             
4AD1: FE 0F          CP      $0F             
4AD3: 20 05          JR      NZ,$4ADA        
4AD5: 21 C0 A9       LD      HL,$A9C0        
4AD8: 36 FF          LD      (HL),$FF        
4ADA: 21 95 4B       LD      HL,$4B95        
4ADD: CF             RST     0X08            
4ADE: 32 C9 A9       LD      ($A9C9),A       
4AE1: 3A B1 A9       LD      A,($A9B1)       
4AE4: 0F             RRCA                    
4AE5: 0F             RRCA                    
4AE6: 0F             RRCA                    
4AE7: 0F             RRCA                    
4AE8: E6 0F          AND     $0F             
4AEA: FE 0F          CP      $0F             
4AEC: 20 05          JR      NZ,$4AF3        
4AEE: 21 C0 A9       LD      HL,$A9C0        
4AF1: 36 FF          LD      (HL),$FF        
4AF3: 21 95 4B       LD      HL,$4B95        
4AF6: CF             RST     0X08            
4AF7: 32 CC A9       LD      ($A9CC),A       
4AFA: C9             RET                     
4AFB: 0E 10          LD      C,$10           
4AFD: 11 7F A4       LD      DE,$A47F        
4B00: 21 86 A9       LD      HL,$A986        
4B03: CD 81 0D       CALL    $0D81           
4B06: C9             RET                     
4B07: 2A 41 AB       LD      HL,($AB41)      
4B0A: 7D             LD      A,L             
4B0B: AC             XOR     H               
4B0C: 2F             CPL                     
4B0D: 87             ADD     A,A             
4B0E: 87             ADD     A,A             
4B0F: ED 6A          ADC     HL,HL           
4B11: 22 41 AB       LD      ($AB41),HL      
4B14: ED 5F          LD      A,R             
4B16: 85             ADD     A,L             
4B17: AC             XOR     H               
4B18: C9             RET                     
4B19: 11 CC 0B       LD      DE,$0BCC        
4B1C: 01 89 00       LD      BC,$0089        
4B1F: 3A 50 1A       LD      A,($1A50)       
4B22: 67             LD      H,A             
4B23: 1A             LD      A,(DE)          
4B24: 81             ADD     A,C             
4B25: 4F             LD      C,A             
4B26: 13             INC     DE              
4B27: 10 FA          DJNZ    $4B23           
4B29: 94             SUB     H               
4B2A: C4 11 0F       CALL    NZ,$0F11        
4B2D: C3 1A 0F       JP      $0F1A           
4B30: 21 1B 0D       LD      HL,$0D1B        
4B33: 06 03          LD      B,$03           
4B35: 5E             LD      E,(HL)          
4B36: 23             INC     HL              
4B37: 56             LD      D,(HL)          
4B38: 23             INC     HL              
4B39: 1A             LD      A,(DE)          
4B3A: 08             EX      AF,AF'          
4B3B: 3E 04          LD      A,$04           
4B3D: 82             ADD     A,D             
4B3E: 57             LD      D,A             
4B3F: 1A             LD      A,(DE)          
4B40: 5E             LD      E,(HL)          
4B41: 23             INC     HL              
4B42: 56             LD      D,(HL)          
4B43: 23             INC     HL              
4B44: 12             LD      (DE),A          
4B45: 1C             INC     E               
4B46: 08             EX      AF,AF'          
4B47: 12             LD      (DE),A          
4B48: 10 EB          DJNZ    $4B35           
4B4A: C9             RET                     
4B4B: D9             EXX                     
4B4C: 21 3F AB       LD      HL,$AB3F        
4B4F: 11 40 AB       LD      DE,$AB40        
4B52: 01 10 00       LD      BC,$0010        
4B55: ED B8          LDDR                    
4B57: 21 40 AB       LD      HL,$AB40        
4B5A: 3A 37 AB       LD      A,($AB37)       
4B5D: AE             XOR     (HL)            
4B5E: 32 30 AB       LD      ($AB30),A       
4B61: 21 80 A9       LD      HL,$A980        
4B64: 86             ADD     A,(HL)          
4B65: D9             EXX                     
4B66: C9             RET                     
4B67: 21 84 4B       LD      HL,$4B84        
4B6A: 11 30 AB       LD      DE,$AB30        
4B6D: 01 11 00       LD      BC,$0011        
4B70: ED B0          LDIR                    
4B72: DD 2A 6D 08    LD      IX,($086D)      
4B76: 2A 70 08       LD      HL,($0870)      
4B79: DD 7D          LD      A,IXL           
4B7B: DD 84          ADD     A,IXH           
4B7D: 85             ADD     A,L             
4B7E: C6 44          ADD     $44             
4B80: C2 00 60       JP      NZ,$6000        
4B83: C9             RET                     
4B84: FF             RST     0X38            
4B85: 05             DEC     B               
4B86: F6 80          OR      $80             
4B88: 32 17 9C       LD      ($9C17),A       
4B8B: C9             RET                     
4B8C: DD 21 74 98    LD      IX,$9874        
4B90: FD                                  
4B91: BF             CP      A               
4B92: 24             INC     H               
4B93: AE             XOR     (HL)            
4B94: 46             LD      B,(HL)          
4B95: 01 02 03       LD      BC,$0302        
4B98: 04             INC     B               
4B99: 05             DEC     B               
4B9A: 06 07          LD      B,$07           
4B9C: 11 13 15       LD      DE,$1513        
4B9F: 21 22 24       LD      HL,$2422        
4BA2: 31 33 01       LD      SP,$0133        
4BA5: 21 B1 4B       LD      HL,$4BB1        
4BA8: 11 08 AB       LD      DE,$AB08        
4BAB: 01 28 00       LD      BC,$0028        
4BAE: ED B0          LDIR                    
4BB0: C9             RET                     
4BB1: 00             NOP                     
4BB2: 00             NOP                     
4BB3: 00             NOP                     
4BB4: 01 7C 11       LD      BC,$117C        
4BB7: 68             LD      L,B             
4BB8: F1             POP     AF              
4BB9: 01 00 88       LD      BC,$8800        
4BBC: 00             NOP                     
4BBD: 3B             DEC     SP              
4BBE: 11 A5 F1       LD      DE,$F1A5        
4BC1: 02             LD      (BC),A          
4BC2: 60             LD      H,B             
4BC3: 84             ADD     A,H             
4BC4: 00             NOP                     
4BC5: 38 11          JR      C,$4BD8         
4BC7: FD                                  
4BC8: F1             POP     AF              
4BC9: 03             INC     BC              
4BCA: 20 65          JR      NZ,$4C31        
4BCC: 00             NOP                     
4BCD: 68             LD      L,B             
4BCE: 11 68 F1       LD      DE,$F168        
4BD1: 04             INC     B               
4BD2: 00             NOP                     
4BD3: 43             LD      B,E             
4BD4: 00             NOP                     
4BD5: BF             CP      A               
4BD6: 11 A5 F1       LD      DE,$F1A5        
4BD9: C3 AE 08       JP      $08AE           
4BDC: 21 08 AB       LD      HL,$AB08        
4BDF: 11 11 A7       LD      DE,$A711        
4BE2: 0E 14          LD      C,$14           
4BE4: CD 1F 4C       CALL    $4C1F           
4BE7: 21 10 AB       LD      HL,$AB10        
4BEA: 11 13 A7       LD      DE,$A713        
4BED: 0E 16          LD      C,$16           
4BEF: CD 1F 4C       CALL    $4C1F           
4BF2: 21 18 AB       LD      HL,$AB18        
4BF5: 11 15 A7       LD      DE,$A715        
4BF8: 0E 12          LD      C,$12           
4BFA: CD 1F 4C       CALL    $4C1F           
4BFD: 21 20 AB       LD      HL,$AB20        
4C00: 11 17 A7       LD      DE,$A717        
4C03: 0E 15          LD      C,$15           
4C05: CD 1F 4C       CALL    $4C1F           
4C08: 21 28 AB       LD      HL,$AB28        
4C0B: 11 19 A7       LD      DE,$A719        
4C0E: 0E 13          LD      C,$13           
4C10: CD 1F 4C       CALL    $4C1F           
4C13: C9             RET                     
4C14: 73             LD      (HL),E          
4C15: A6             AND     (HL)            
4C16: 14             INC     D               
4C17: 7E             LD      A,(HL)          
4C18: 29             ADD     HL,HL           
4C19: F8             RET     M               
4C1A: 96             SUB     (HL)            
4C1B: 5D             LD      E,L             
4C1C: F3             DI                      
4C1D: 13             INC     DE              
4C1E: B9             CP      C               
4C1F: E5             PUSH    HL              
4C20: 7E             LD      A,(HL)          
4C21: 87             ADD     A,A             
4C22: 86             ADD     A,(HL)          
4C23: 21 B4 4C       LD      HL,$4CB4        
4C26: CF             RST     0X08            
4C27: 12             LD      (DE),A          
4C28: CB 92          RES     2,D             
4C2A: 79             LD      A,C             
4C2B: 12             LD      (DE),A          
4C2C: CB D2          SET     2,D             
4C2E: 23             INC     HL              
4C2F: E7             RST     0X20            
4C30: 7E             LD      A,(HL)          
4C31: 12             LD      (DE),A          
4C32: CB 92          RES     2,D             
4C34: 79             LD      A,C             
4C35: 12             LD      (DE),A          
4C36: CB D2          SET     2,D             
4C38: 23             INC     HL              
4C39: E7             RST     0X20            
4C3A: 7E             LD      A,(HL)          
4C3B: 12             LD      (DE),A          
4C3C: CB 92          RES     2,D             
4C3E: 79             LD      A,C             
4C3F: 12             LD      (DE),A          
4C40: CB D2          SET     2,D             
4C42: 21 80 FF       LD      HL,$FF80        
4C45: 19             ADD     HL,DE           
4C46: EB             EX      DE,HL           
4C47: E1             POP     HL              
4C48: 23             INC     HL              
4C49: 23             INC     HL              
4C4A: 23             INC     HL              
4C4B: CD 73 0D       CALL    $0D73           
4C4E: E5             PUSH    HL              
4C4F: 21 A0 FF       LD      HL,$FFA0        
4C52: 19             ADD     HL,DE           
4C53: EB             EX      DE,HL           
4C54: E1             POP     HL              
4C55: 23             INC     HL              
4C56: 23             INC     HL              
4C57: 23             INC     HL              
4C58: 7E             LD      A,(HL)          
4C59: 12             LD      (DE),A          
4C5A: CB 92          RES     2,D             
4C5C: 79             LD      A,C             
4C5D: 12             LD      (DE),A          
4C5E: CB D2          SET     2,D             
4C60: 23             INC     HL              
4C61: E7             RST     0X20            
4C62: 7E             LD      A,(HL)          
4C63: 12             LD      (DE),A          
4C64: CB 92          RES     2,D             
4C66: 79             LD      A,C             
4C67: 12             LD      (DE),A          
4C68: CB D2          SET     2,D             
4C6A: 23             INC     HL              
4C6B: E7             RST     0X20            
4C6C: 7E             LD      A,(HL)          
4C6D: 12             LD      (DE),A          
4C6E: CB 92          RES     2,D             
4C70: 79             LD      A,C             
4C71: 12             LD      (DE),A          
4C72: CB D2          SET     2,D             
4C74: C9             RET                     
4C75: CD D2 07       CALL    $07D2           
4C78: 3A 32 AD       LD      A,($AD32)       
4C7B: A7             AND     A               
4C7C: 21 10 AD       LD      HL,$AD10        
4C7F: 28 03          JR      Z,$4C84         
4C81: 21 20 AD       LD      HL,$AD20        
4C84: 11 00 AD       LD      DE,$AD00        
4C87: 01 10 00       LD      BC,$0010        
4C8A: ED B0          LDIR                    
4C8C: 3A 30 AD       LD      A,($AD30)       
4C8F: A7             AND     A               
4C90: CA 1A 0F       JP      Z,$0F1A         
4C93: 3A 01 AD       LD      A,($AD01)       
4C96: 16 06          LD      D,$06           
4C98: 5F             LD      E,A             
4C99: FF             RST     0X38            
4C9A: 3A 00 AD       LD      A,($AD00)       
4C9D: 3D             DEC     A               
4C9E: 16 05          LD      D,$05           
4CA0: 5F             LD      E,A             
4CA1: FF             RST     0X38            
4CA2: 06 00          LD      B,$00           
4CA4: 21 50 5B       LD      HL,$5B50        
4CA7: 97             SUB     A               
4CA8: AE             XOR     (HL)            
4CA9: 23             INC     HL              
4CAA: 10 FC          DJNZ    $4CA8           
4CAC: C6 FF          ADD     $FF             
4CAE: 32 08 C3       LD      ($C308),A       
4CB1: C3 1A 0F       JP      $0F1A           
4CB4: 96             SUB     (HL)            
4CB5: ED                                  
4CB6: DC 9B 3B       CALL    C,$3B9B         
4CB9: 87             ADD     A,A             
4CBA: CD D7 87       CALL    $87D7           
4CBD: F3             DI                      
4CBE: DC C4 7F       CALL    C,$7FC4         
4CC1: DC C4 21       CALL    C,$21C4         
4CC4: 0B             DEC     BC              
4CC5: AB             XOR     E               
4CC6: 06 05          LD      B,$05           
4CC8: 3A 32 AD       LD      A,($AD32)       
4CCB: A7             AND     A               
4CCC: 11 35 AD       LD      DE,$AD35        
4CCF: 28 03          JR      Z,$4CD4         
4CD1: 11 38 AD       LD      DE,$AD38        
4CD4: E5             PUSH    HL              
4CD5: D5             PUSH    DE              
4CD6: CD 2B 4D       CALL    $4D2B           
4CD9: 30 09          JR      NC,$4CE4        
4CDB: D1             POP     DE              
4CDC: E1             POP     HL              
4CDD: 3E 08          LD      A,$08           
4CDF: CF             RST     0X08            
4CE0: 10 F2          DJNZ    $4CD4           
4CE2: 37             SCF                     
4CE3: C9             RET                     
4CE4: 05             DEC     B               
4CE5: 28 3F          JR      Z,$4D26         
4CE7: 21 27 AB       LD      HL,$AB27        
4CEA: 11 2F AB       LD      DE,$AB2F        
4CED: 78             LD      A,B             
4CEE: 87             ADD     A,A             
4CEF: 87             ADD     A,A             
4CF0: 87             ADD     A,A             
4CF1: 4F             LD      C,A             
4CF2: 06 00          LD      B,$00           
4CF4: ED B8          LDDR                    
4CF6: EB             EX      DE,HL           
4CF7: 2B             DEC     HL              
4CF8: 36 F1          LD      (HL),$F1        
4CFA: 2B             DEC     HL              
4CFB: 36 F1          LD      (HL),$F1        
4CFD: 2B             DEC     HL              
4CFE: 36 F1          LD      (HL),$F1        
4D00: 22 91 A9       LD      ($A991),HL      
4D03: 2B             DEC     HL              
4D04: D1             POP     DE              
4D05: 01 03 00       LD      BC,$0003        
4D08: EB             EX      DE,HL           
4D09: ED B8          LDDR                    
4D0B: 1A             LD      A,(DE)          
4D0C: E1             POP     HL              
4D0D: 21 31 A5       LD      HL,$A531        
4D10: 87             ADD     A,A             
4D11: CF             RST     0X08            
4D12: 22 93 A9       LD      ($A993),HL      
4D15: 21 08 AB       LD      HL,$AB08        
4D18: 11 08 00       LD      DE,$0008        
4D1B: 06 05          LD      B,$05           
4D1D: AF             XOR     A               
4D1E: 77             LD      (HL),A          
4D1F: 19             ADD     HL,DE           
4D20: 3C             INC     A               
4D21: 10 FB          DJNZ    $4D1E           
4D23: 37             SCF                     
4D24: 3F             CCF                     
4D25: C9             RET                     
4D26: 21 2F AB       LD      HL,$AB2F        
4D29: 18 CC          JR      $4CF7           
4D2B: 0E 03          LD      C,$03           
4D2D: 1A             LD      A,(DE)          
4D2E: BE             CP      (HL)            
4D2F: D8             RET     C               
4D30: 20 05          JR      NZ,$4D37        
4D32: 1B             DEC     DE              
4D33: 2B             DEC     HL              
4D34: 0D             DEC     C               
4D35: 20 F6          JR      NZ,$4D2D        
4D37: 37             SCF                     
4D38: 3F             CCF                     
4D39: C9             RET                     
4D3A: 21 05 AD       LD      HL,$AD05        
4D3D: CD 67 4D       CALL    $4D67           
4D40: D8             RET     C               
4D41: 2C             INC     L               
4D42: CD 67 4D       CALL    $4D67           
4D45: 38 04          JR      C,$4D4B         
4D47: 2C             INC     L               
4D48: CD 67 4D       CALL    $4D67           
4D4B: 21 D7 A9       LD      HL,$A9D7        
4D4E: 7E             LD      A,(HL)          
4D4F: A7             AND     A               
4D50: C8             RET     Z               
4D51: 35             DEC     (HL)            
4D52: C0             RET     NZ              
4D53: 3A D6 A9       LD      A,($A9D6)       
4D56: 77             LD      (HL),A          
4D57: 3A C0 AC       LD      A,($ACC0)       
4D5A: 3C             INC     A               
4D5B: FE 10          CP      $10             
4D5D: 38 02          JR      C,$4D61         
4D5F: 3E 0F          LD      A,$0F           
4D61: 32 C0 AC       LD      ($ACC0),A       
4D64: C3 9A 1A       JP      $1A9A           
4D67: 7E             LD      A,(HL)          
4D68: C6 01          ADD     $01             
4D6A: 27             DAA                     
4D6B: 77             LD      (HL),A          
4D6C: FE 60          CP      $60             
4D6E: D8             RET     C               
4D6F: 36 00          LD      (HL),$00        
4D71: C9             RET                     
4D72: 4F             LD      C,A             
4D73: 3A 30 AD       LD      A,($AD30)       
4D76: A7             AND     A               
4D77: C8             RET     Z               
4D78: 11 83 A7       LD      DE,$A783        
4D7B: 79             LD      A,C             
4D7C: FE 07          CP      $07             
4D7E: 38 02          JR      C,$4D82         
4D80: 3E 06          LD      A,$06           
4D82: A7             AND     A               
4D83: 28 0C          JR      Z,$4D91         
4D85: 06 09          LD      B,$09           
4D87: 0E 18          LD      C,$18           
4D89: 08             EX      AF,AF'          
4D8A: CD AF 4D       CALL    $4DAF           
4D8D: 08             EX      AF,AF'          
4D8E: 3D             DEC     A               
4D8F: 20 F8          JR      NZ,$4D89        
4D91: 01 10 F1       LD      BC,$F110        
4D94: 21 DD 59       LD      HL,$59DD        
4D97: 19             ADD     HL,DE           
4D98: 30 05          JR      NC,$4D9F        
4D9A: CD CF 4D       CALL    $4DCF           
4D9D: 18 F5          JR      $4D94           
4D9F: 06 00          LD      B,$00           
4DA1: 21 11 07       LD      HL,$0711        
4DA4: 97             SUB     A               
4DA5: AE             XOR     (HL)            
4DA6: 23             INC     HL              
4DA7: 10 FC          DJNZ    $4DA5           
4DA9: C6 19          ADD     $19             
4DAB: C2 B1 4B       JP      NZ,$4BB1        
4DAE: C9             RET                     
4DAF: 78             LD      A,B             
4DB0: C6 03          ADD     $03             
4DB2: 12             LD      (DE),A          
4DB3: 3D             DEC     A               
4DB4: 1B             DEC     DE              
4DB5: 12             LD      (DE),A          
4DB6: E7             RST     0X20            
4DB7: 78             LD      A,B             
4DB8: 12             LD      (DE),A          
4DB9: 3C             INC     A               
4DBA: 13             INC     DE              
4DBB: 12             LD      (DE),A          
4DBC: 21 00 FC       LD      HL,$FC00        
4DBF: 19             ADD     HL,DE           
4DC0: E7             RST     0X20            
4DC1: 71             LD      (HL),C          
4DC2: 2B             DEC     HL              
4DC3: 71             LD      (HL),C          
4DC4: 7D             LD      A,L             
4DC5: C6 20          ADD     $20             
4DC7: 6F             LD      L,A             
4DC8: 30 01          JR      NC,$4DCB        
4DCA: 24             INC     H               
4DCB: 71             LD      (HL),C          
4DCC: 23             INC     HL              
4DCD: 71             LD      (HL),C          
4DCE: C9             RET                     
4DCF: EB             EX      DE,HL           
4DD0: 70             LD      (HL),B          
4DD1: 2B             DEC     HL              
4DD2: 36 F1          LD      (HL),$F1        
4DD4: CB 94          RES     2,H             
4DD6: 71             LD      (HL),C          
4DD7: 23             INC     HL              
4DD8: 71             LD      (HL),C          
4DD9: CB D4          SET     2,H             
4DDB: EB             EX      DE,HL           
4DDC: E7             RST     0X20            
4DDD: C9             RET                     
4DDE: 3A 30 AD       LD      A,($AD30)       
4DE1: A7             AND     A               
4DE2: C8             RET     Z               
4DE3: 3A C3 A9       LD      A,($A9C3)       
4DE6: E6 01          AND     $01             
4DE8: 21 1B 4E       LD      HL,$4E1B        
4DEB: 28 03          JR      Z,$4DF0         
4DED: 21 30 4E       LD      HL,$4E30        
4DF0: 4E             LD      C,(HL)          
4DF1: 06 00          LD      B,$00           
4DF3: 23             INC     HL              
4DF4: 3A 32 AD       LD      A,($AD32)       
4DF7: A7             AND     A               
4DF8: 3A 35 AD       LD      A,($AD35)       
4DFB: 28 03          JR      Z,$4E00         
4DFD: 3A 38 AD       LD      A,($AD38)       
4E00: ED B1          CPIR                    
4E02: 21 03 AD       LD      HL,$AD03        
4E05: 20 11          JR      NZ,$4E18        
4E07: CB 46          BIT     0,(HL)          
4E09: C0             RET     NZ              
4E0A: CB C6          SET     0,(HL)          
4E0C: 21 00 AD       LD      HL,$AD00        
4E0F: 7E             LD      A,(HL)          
4E10: 34             INC     (HL)            
4E11: 16 05          LD      D,$05           
4E13: 5F             LD      E,A             
4E14: FF             RST     0X38            
4E15: C3 05 58       JP      $5805           
4E18: CB 86          RES     0,(HL)          
4E1A: C9             RET                     
4E1B: 14             INC     D               
4E1C: 01 06 11       LD      BC,$1106        
4E1F: 16 21          LD      D,$21           
4E21: 26 31          LD      H,$31           
4E23: 36 41          LD      (HL),$41        
4E25: 46             LD      B,(HL)          
4E26: 51             LD      D,C             
4E27: 56             LD      D,(HL)          
4E28: 61             LD      H,C             
4E29: 66             LD      H,(HL)          
4E2A: 71             LD      (HL),C          
4E2B: 76             HALT                    
4E2C: 81             ADD     A,C             
4E2D: 86             ADD     A,(HL)          
4E2E: 91             SUB     C               
4E2F: 96             SUB     (HL)            
4E30: 11 02 08       LD      DE,$0802        
4E33: 14             INC     D               
4E34: 20 26          JR      NZ,$4E5C        
4E36: 32 38 44       LD      ($4438),A       
4E39: 50             LD      D,B             
4E3A: 56             LD      D,(HL)          
4E3B: 62             LD      H,D             
4E3C: 68             LD      L,B             
4E3D: 74             LD      (HL),H          
4E3E: 80             ADD     A,B             
4E3F: 86             ADD     A,(HL)          
4E40: 92             SUB     D               
4E41: 98             SBC     B               
4E42: 6F             LD      L,A             
4E43: A6             AND     (HL)            
4E44: 14             INC     D               
4E45: 88             ADC     A,B             
4E46: 57             LD      D,A             
4E47: A5             AND     L               
4E48: BF             CP      A               
4E49: 34             INC     (HL)            
4E4A: D7             RST     0X10            
4E4B: F1             POP     AF              
4E4C: 9B             SBC     E               
4E4D: F1             POP     AF              
4E4E: B9             CP      C               
4E4F: 3A 04 AD       LD      A,($AD04)       
4E52: FE 04          CP      $04             
4E54: CA 2A 4F       JP      Z,$4F2A         
4E57: 3D             DEC     A               
4E58: CA BC 4E       JP      Z,$4EBC         
4E5B: 3A 80 A9       LD      A,($A980)       
4E5E: E6 01          AND     $01             
4E60: C2 35 4F       JP      NZ,$4F35        
4E63: CD 5D 4F       CALL    $4F5D           
4E66: 06 04          LD      B,$04           
4E68: 11 10 A8       LD      DE,$A810        
4E6B: FD 21 12 AA    LD      IY,$AA12        
4E6F: 2E 05          LD      L,$05           
4E71: 26 0B          LD      H,$0B           
4E73: CD 85 51       CALL    $5185           
4E76: 3A 0D AD       LD      A,($AD0D)       
4E79: A7             AND     A               
4E7A: 20 1B          JR      NZ,$4E97        
4E7C: 06 07          LD      B,$07           
4E7E: 2E 07          LD      L,$07           
4E80: 26 0F          LD      H,$0F           
4E82: CD 52 51       CALL    $5152           
4E85: 06 03          LD      B,$03           
4E87: 2E 06          LD      L,$06           
4E89: 26 0D          LD      H,$0D           
4E8B: CD 21 51       CALL    $5121           
4E8E: 06 01          LD      B,$01           
4E90: 2E 08          LD      L,$08           
4E92: 26 11          LD      H,$11           
4E94: C3 B3 51       JP      $51B3           
4E97: 06 05          LD      B,$05           
4E99: 2E 07          LD      L,$07           
4E9B: 26 0F          LD      H,$0F           
4E9D: CD 52 51       CALL    $5152           
4EA0: CD B1 50       CALL    $50B1           
4EA3: 06 03          LD      B,$03           
4EA5: 11 C0 A8       LD      DE,$A8C0        
4EA8: FD 21 28 AA    LD      IY,$AA28        
4EAC: 2E 06          LD      L,$06           
4EAE: 26 0D          LD      H,$0D           
4EB0: CD 21 51       CALL    $5121           
4EB3: 06 01          LD      B,$01           
4EB5: 2E 08          LD      L,$08           
4EB7: 26 11          LD      H,$11           
4EB9: C3 B3 51       JP      $51B3           
4EBC: 3A 80 A9       LD      A,($A980)       
4EBF: E6 01          AND     $01             
4EC1: C2 35 4F       JP      NZ,$4F35        
4EC4: CD 7E 4F       CALL    $4F7E           
4EC7: 06 04          LD      B,$04           
4EC9: 11 10 A8       LD      DE,$A810        
4ECC: FD 21 12 AA    LD      IY,$AA12        
4ED0: 2E 05          LD      L,$05           
4ED2: 26 0B          LD      H,$0B           
4ED4: CD 85 51       CALL    $5185           
4ED7: 3A 0D AD       LD      A,($AD0D)       
4EDA: A7             AND     A               
4EDB: 20 25          JR      NZ,$4F02        
4EDD: 06 07          LD      B,$07           
4EDF: 2E 07          LD      L,$07           
4EE1: 26 0F          LD      H,$0F           
4EE3: CD 52 51       CALL    $5152           
4EE6: CD 7E 50       CALL    $507E           
4EE9: 06 01          LD      B,$01           
4EEB: 11 E0 A8       LD      DE,$A8E0        
4EEE: FD 21 2C AA    LD      IY,$AA2C        
4EF2: 2E 05          LD      L,$05           
4EF4: 26 0B          LD      H,$0B           
4EF6: CD 85 51       CALL    $5185           
4EF9: 06 01          LD      B,$01           
4EFB: 2E 08          LD      L,$08           
4EFD: 26 11          LD      H,$11           
4EFF: C3 B3 51       JP      $51B3           
4F02: 06 05          LD      B,$05           
4F04: 2E 07          LD      L,$07           
4F06: 26 0F          LD      H,$0F           
4F08: CD 52 51       CALL    $5152           
4F0B: CD B1 50       CALL    $50B1           
4F0E: CD 7E 50       CALL    $507E           
4F11: 06 01          LD      B,$01           
4F13: 11 E0 A8       LD      DE,$A8E0        
4F16: FD 21 2C AA    LD      IY,$AA2C        
4F1A: 2E 05          LD      L,$05           
4F1C: 26 0B          LD      H,$0B           
4F1E: CD 85 51       CALL    $5185           
4F21: 06 01          LD      B,$01           
4F23: 2E 08          LD      L,$08           
4F25: 26 11          LD      H,$11           
4F27: C3 B3 51       JP      $51B3           
4F2A: 3A 80 A9       LD      A,($A980)       
4F2D: E6 01          AND     $01             
4F2F: CA 63 4E       JP      Z,$4E63         
4F32: C3 32 50       JP      $5032           
4F35: 3A 0D AD       LD      A,($AD0D)       
4F38: A7             AND     A               
4F39: C2 BF 4F       JP      NZ,$4FBF        
4F3C: 11 50 A8       LD      DE,$A850        
4F3F: FD 21 1A AA    LD      IY,$AA1A        
4F43: DD 21 80 AA    LD      IX,$AA80        
4F47: 08             EX      AF,AF'          
4F48: 3E 07          LD      A,$07           
4F4A: 47             LD      B,A             
4F4B: 08             EX      AF,AF'          
4F4C: 0E 06          LD      C,$06           
4F4E: ED 53 93 A9    LD      ($A993),DE      
4F52: FD 22 91 A9    LD      ($A991),IY      
4F56: 2E 07          LD      L,$07           
4F58: 26 0F          LD      H,$0F           
4F5A: C3 11 52       JP      $5211           
4F5D: 11 C0 A8       LD      DE,$A8C0        
4F60: FD 21 28 AA    LD      IY,$AA28        
4F64: DD 21 80 AA    LD      IX,$AA80        
4F68: 08             EX      AF,AF'          
4F69: 3E 03          LD      A,$03           
4F6B: 47             LD      B,A             
4F6C: 08             EX      AF,AF'          
4F6D: 0E 06          LD      C,$06           
4F6F: ED 53 93 A9    LD      ($A993),DE      
4F73: FD 22 91 A9    LD      ($A991),IY      
4F77: 2E 07          LD      L,$07           
4F79: 26 0F          LD      H,$0F           
4F7B: C3 11 52       JP      $5211           
4F7E: 2E 06          LD      L,$06           
4F80: 26 0D          LD      H,$0D           
4F82: 1E 17          LD      E,$17           
4F84: 16 1F          LD      D,$1F           
4F86: FD 21 80 AA    LD      IY,$AA80        
4F8A: 06 06          LD      B,$06           
4F8C: 3A C0 A8       LD      A,($A8C0)       
4F8F: 3C             INC     A               
4F90: C0             RET     NZ              
4F91: FD 7E 00       LD      A,(IY+$00)      
4F94: 3C             INC     A               
4F95: 20 1F          JR      NZ,$4FB6        
4F97: 3A 28 AA       LD      A,($AA28)       
4F9A: FD 96 06       SUB     (IY+$06)        
4F9D: 85             ADD     A,L             
4F9E: BC             CP      H               
4F9F: 30 15          JR      NC,$4FB6        
4FA1: 3A 59 AA       LD      A,($AA59)       
4FA4: FD 96 04       SUB     (IY+$04)        
4FA7: 83             ADD     A,E             
4FA8: BA             CP      D               
4FA9: 30 0B          JR      NC,$4FB6        
4FAB: 3E F0          LD      A,$F0           
4FAD: 32 C0 A8       LD      ($A8C0),A       
4FB0: FD 77 00       LD      (IY+$00),A      
4FB3: CD DE 51       CALL    $51DE           
4FB6: FD 7D          LD      A,IYL           
4FB8: C6 10          ADD     $10             
4FBA: FD 6F          LD      IXH,A           
4FBC: 10 D3          DJNZ    $4F91           
4FBE: C9             RET                     
4FBF: 11 50 A8       LD      DE,$A850        
4FC2: FD 21 1A AA    LD      IY,$AA1A        
4FC6: DD 21 80 AA    LD      IX,$AA80        
4FCA: 08             EX      AF,AF'          
4FCB: 3E 05          LD      A,$05           
4FCD: 47             LD      B,A             
4FCE: 08             EX      AF,AF'          
4FCF: 0E 06          LD      C,$06           
4FD1: ED 53 93 A9    LD      ($A993),DE      
4FD5: FD 22 91 A9    LD      ($A991),IY      
4FD9: 2E 07          LD      L,$07           
4FDB: 26 0F          LD      H,$0F           
4FDD: CD 11 52       CALL    $5211           
4FE0: 3A 04 AD       LD      A,($AD04)       
4FE3: A7             AND     A               
4FE4: 28 45          JR      Z,$502B         
4FE6: FE 04          CP      $04             
4FE8: 28 41          JR      Z,$502B         
4FEA: 2E 06          LD      L,$06           
4FEC: 26 0D          LD      H,$0D           
4FEE: 1E 17          LD      E,$17           
4FF0: 16 1F          LD      D,$1F           
4FF2: FD 21 80 AA    LD      IY,$AA80        
4FF6: 06 06          LD      B,$06           
4FF8: 3A A0 A8       LD      A,($A8A0)       
4FFB: 3C             INC     A               
4FFC: C0             RET     NZ              
4FFD: FD 7E 00       LD      A,(IY+$00)      
5000: 3C             INC     A               
5001: 20 1F          JR      NZ,$5022        
5003: 3A 24 AA       LD      A,($AA24)       
5006: FD 96 06       SUB     (IY+$06)        
5009: 85             ADD     A,L             
500A: BC             CP      H               
500B: 30 15          JR      NC,$5022        
500D: 3A 55 AA       LD      A,($AA55)       
5010: FD 96 04       SUB     (IY+$04)        
5013: 83             ADD     A,E             
5014: BA             CP      D               
5015: 30 0B          JR      NC,$5022        
5017: 3E F0          LD      A,$F0           
5019: 32 A0 A8       LD      ($A8A0),A       
501C: FD 77 00       LD      (IY+$00),A      
501F: CD DE 51       CALL    $51DE           
5022: FD 7D          LD      A,IYL           
5024: C6 10          ADD     $10             
5026: FD 6F          LD      IXH,A           
5028: 10 D3          DJNZ    $4FFD           
502A: C9             RET                     
502B: 2E 08          LD      L,$08           
502D: 26 11          LD      H,$11           
502F: C3 EE 4F       JP      $4FEE           
5032: 3A 0D AD       LD      A,($AD0D)       
5035: A7             AND     A               
5036: C2 5A 50       JP      NZ,$505A        
5039: 11 10 A8       LD      DE,$A810        
503C: FD 21 12 AA    LD      IY,$AA12        
5040: DD 21 80 AA    LD      IX,$AA80        
5044: 08             EX      AF,AF'          
5045: 3E 0B          LD      A,$0B           
5047: 47             LD      B,A             
5048: 08             EX      AF,AF'          
5049: 0E 06          LD      C,$06           
504B: ED 53 93 A9    LD      ($A993),DE      
504F: FD 22 91 A9    LD      ($A991),IY      
5053: 2E 07          LD      L,$07           
5055: 26 0F          LD      H,$0F           
5057: C3 11 52       JP      $5211           
505A: 11 10 A8       LD      DE,$A810        
505D: FD 21 12 AA    LD      IY,$AA12        
5061: DD 21 80 AA    LD      IX,$AA80        
5065: 08             EX      AF,AF'          
5066: 3E 09          LD      A,$09           
5068: 47             LD      B,A             
5069: 08             EX      AF,AF'          
506A: 0E 06          LD      C,$06           
506C: ED 53 93 A9    LD      ($A993),DE      
5070: FD 22 91 A9    LD      ($A991),IY      
5074: 2E 07          LD      L,$07           
5076: 26 0F          LD      H,$0F           
5078: CD 11 52       CALL    $5211           
507B: C3 E0 4F       JP      $4FE0           
507E: DD 21 10 AA    LD      IX,$AA10        
5082: 3A 00 A8       LD      A,($A800)       
5085: 3C             INC     A               
5086: C0             RET     NZ              
5087: 3A C0 A8       LD      A,($A8C0)       
508A: 3C             INC     A               
508B: C0             RET     NZ              
508C: 3A 28 AA       LD      A,($AA28)       
508F: DD 96 00       SUB     (IX+$00)        
5092: C6 06          ADD     $06             
5094: FE 0D          CP      $0D             
5096: D0             RET     NC              
5097: 3A 59 AA       LD      A,($AA59)       
509A: DD 96 31       SUB     (IX+$31)        
509D: C6 18          ADD     $18             
509F: FE 21          CP      $21             
50A1: D0             RET     NC              
50A2: 3E F0          LD      A,$F0           
50A4: 32 00 A8       LD      ($A800),A       
50A7: 32 C0 A8       LD      ($A8C0),A       
50AA: AF             XOR     A               
50AB: 32 DC A8       LD      ($A8DC),A       
50AE: C3 DE 51       JP      $51DE           
50B1: 3A 04 AD       LD      A,($AD04)       
50B4: A7             AND     A               
50B5: 28 37          JR      Z,$50EE         
50B7: FE 04          CP      $04             
50B9: 28 33          JR      Z,$50EE         
50BB: DD 21 10 AA    LD      IX,$AA10        
50BF: 3A 00 A8       LD      A,($A800)       
50C2: 3C             INC     A               
50C3: C0             RET     NZ              
50C4: 3A A0 A8       LD      A,($A8A0)       
50C7: 3C             INC     A               
50C8: C0             RET     NZ              
50C9: 3A 24 AA       LD      A,($AA24)       
50CC: DD 96 00       SUB     (IX+$00)        
50CF: C6 06          ADD     $06             
50D1: FE 0D          CP      $0D             
50D3: D0             RET     NC              
50D4: 3A 55 AA       LD      A,($AA55)       
50D7: DD 96 31       SUB     (IX+$31)        
50DA: C6 19          ADD     $19             
50DC: FE 23          CP      $23             
50DE: D0             RET     NC              
50DF: 3E F0          LD      A,$F0           
50E1: 32 00 A8       LD      ($A800),A       
50E4: 32 A0 A8       LD      ($A8A0),A       
50E7: AF             XOR     A               
50E8: 32 A4 A8       LD      ($A8A4),A       
50EB: C3 DE 51       JP      $51DE           
50EE: DD 21 10 AA    LD      IX,$AA10        
50F2: 3A 00 A8       LD      A,($A800)       
50F5: 3C             INC     A               
50F6: C0             RET     NZ              
50F7: 3A A0 A8       LD      A,($A8A0)       
50FA: 3C             INC     A               
50FB: C0             RET     NZ              
50FC: 3A 24 AA       LD      A,($AA24)       
50FF: DD 96 00       SUB     (IX+$00)        
5102: C6 08          ADD     $08             
5104: FE 11          CP      $11             
5106: D0             RET     NC              
5107: 3A 55 AA       LD      A,($AA55)       
510A: DD 96 31       SUB     (IX+$31)        
510D: C6 19          ADD     $19             
510F: FE 23          CP      $23             
5111: D0             RET     NC              
5112: 3E F0          LD      A,$F0           
5114: 32 00 A8       LD      ($A800),A       
5117: 32 A0 A8       LD      ($A8A0),A       
511A: AF             XOR     A               
511B: 32 A4 A8       LD      ($A8A4),A       
511E: C3 DE 51       JP      $51DE           
5121: 3A 00 A8       LD      A,($A800)       
5124: 3C             INC     A               
5125: C0             RET     NZ              
5126: 1A             LD      A,(DE)          
5127: 3C             INC     A               
5128: 20 1D          JR      NZ,$5147        
512A: 3A 10 AA       LD      A,($AA10)       
512D: FD 96 00       SUB     (IY+$00)        
5130: 85             ADD     A,L             
5131: BC             CP      H               
5132: 30 13          JR      NC,$5147        
5134: 3A 41 AA       LD      A,($AA41)       
5137: FD 96 31       SUB     (IY+$31)        
513A: 85             ADD     A,L             
513B: BC             CP      H               
513C: 30 09          JR      NC,$5147        
513E: 3E F0          LD      A,$F0           
5140: 32 00 A8       LD      ($A800),A       
5143: 12             LD      (DE),A          
5144: CD DE 51       CALL    $51DE           
5147: 7B             LD      A,E             
5148: C6 10          ADD     $10             
514A: 5F             LD      E,A             
514B: FD 23          INC     IY              
514D: FD 23          INC     IY              
514F: 10 D5          DJNZ    $5126           
5151: C9             RET                     
5152: 3A 00 A8       LD      A,($A800)       
5155: 3C             INC     A               
5156: C0             RET     NZ              
5157: 1A             LD      A,(DE)          
5158: 3C             INC     A               
5159: 20 1F          JR      NZ,$517A        
515B: 3A 10 AA       LD      A,($AA10)       
515E: FD 96 00       SUB     (IY+$00)        
5161: 85             ADD     A,L             
5162: BC             CP      H               
5163: 30 15          JR      NC,$517A        
5165: 3A 41 AA       LD      A,($AA41)       
5168: FD 96 31       SUB     (IY+$31)        
516B: C6 08          ADD     $08             
516D: FE 11          CP      $11             
516F: 30 09          JR      NC,$517A        
5171: 3E F0          LD      A,$F0           
5173: 32 00 A8       LD      ($A800),A       
5176: 12             LD      (DE),A          
5177: CD DE 51       CALL    $51DE           
517A: 7B             LD      A,E             
517B: C6 10          ADD     $10             
517D: 5F             LD      E,A             
517E: FD 23          INC     IY              
5180: FD 23          INC     IY              
5182: 10 D3          DJNZ    $5157           
5184: C9             RET                     
5185: 3A 00 A8       LD      A,($A800)       
5188: 3C             INC     A               
5189: C0             RET     NZ              
518A: 1A             LD      A,(DE)          
518B: 3C             INC     A               
518C: 20 1A          JR      NZ,$51A8        
518E: 3A 10 AA       LD      A,($AA10)       
5191: FD 96 00       SUB     (IY+$00)        
5194: 85             ADD     A,L             
5195: BC             CP      H               
5196: 30 10          JR      NC,$51A8        
5198: 3A 41 AA       LD      A,($AA41)       
519B: FD 96 31       SUB     (IY+$31)        
519E: 85             ADD     A,L             
519F: BC             CP      H               
51A0: 30 06          JR      NC,$51A8        
51A2: 3E F0          LD      A,$F0           
51A4: 32 00 A8       LD      ($A800),A       
51A7: 12             LD      (DE),A          
51A8: 7B             LD      A,E             
51A9: C6 10          ADD     $10             
51AB: 5F             LD      E,A             
51AC: FD 23          INC     IY              
51AE: FD 23          INC     IY              
51B0: 10 D8          DJNZ    $518A           
51B2: C9             RET                     
51B3: 3A 00 A8       LD      A,($A800)       
51B6: 3C             INC     A               
51B7: C0             RET     NZ              
51B8: 1A             LD      A,(DE)          
51B9: 3C             INC     A               
51BA: 20 17          JR      NZ,$51D3        
51BC: 3A 10 AA       LD      A,($AA10)       
51BF: FD 96 00       SUB     (IY+$00)        
51C2: 85             ADD     A,L             
51C3: BC             CP      H               
51C4: 30 0D          JR      NC,$51D3        
51C6: 3A 41 AA       LD      A,($AA41)       
51C9: FD 96 31       SUB     (IY+$31)        
51CC: 85             ADD     A,L             
51CD: BC             CP      H               
51CE: 30 03          JR      NC,$51D3        
51D0: 3E F0          LD      A,$F0           
51D2: 12             LD      (DE),A          
51D3: 7B             LD      A,E             
51D4: C6 10          ADD     $10             
51D6: 5F             LD      E,A             
51D7: FD 23          INC     IY              
51D9: FD 23          INC     IY              
51DB: 10 DB          DJNZ    $51B8           
51DD: C9             RET                     
51DE: D5             PUSH    DE              
51DF: 3A 9D A9       LD      A,($A99D)       
51E2: A7             AND     A               
51E3: 28 15          JR      Z,$51FA         
51E5: 3A 9E A9       LD      A,($A99E)       
51E8: 3C             INC     A               
51E9: 32 9E A9       LD      ($A99E),A       
51EC: E6 07          AND     $07             
51EE: 3C             INC     A               
51EF: 5F             LD      E,A             
51F0: 16 04          LD      D,$04           
51F2: FF             RST     0X38            
51F3: D1             POP     DE              
51F4: 3E 1E          LD      A,$1E           
51F6: 32 9D A9       LD      ($A99D),A       
51F9: C9             RET                     
51FA: 11 01 04       LD      DE,$0401        
51FD: FF             RST     0X38            
51FE: D1             POP     DE              
51FF: 3E 1E          LD      A,$1E           
5201: 32 9D A9       LD      ($A99D),A       
5204: C9             RET                     
5205: 21 9D A9       LD      HL,$A99D        
5208: 7E             LD      A,(HL)          
5209: A7             AND     A               
520A: 28 02          JR      Z,$520E         
520C: 35             DEC     (HL)            
520D: C9             RET                     
520E: 2C             INC     L               
520F: 77             LD      (HL),A          
5210: C9             RET                     
5211: DD 7E 00       LD      A,(IX+$00)      
5214: 3C             INC     A               
5215: 20 3D          JR      NZ,$5254        
5217: 1A             LD      A,(DE)          
5218: 3C             INC     A               
5219: 20 2F          JR      NZ,$524A        
521B: FD 7E 00       LD      A,(IY+$00)      
521E: C6 08          ADD     $08             
5220: FE 19          CP      $19             
5222: 38 26          JR      C,$524A         
5224: FD 7E 31       LD      A,(IY+$31)      
5227: C6 10          ADD     $10             
5229: FE 11          CP      $11             
522B: 38 1D          JR      C,$524A         
522D: DD 7E 06       LD      A,(IX+$06)      
5230: FD 96 00       SUB     (IY+$00)        
5233: 85             ADD     A,L             
5234: BC             CP      H               
5235: 30 13          JR      NC,$524A        
5237: DD 7E 04       LD      A,(IX+$04)      
523A: FD 96 31       SUB     (IY+$31)        
523D: 85             ADD     A,L             
523E: BC             CP      H               
523F: 30 09          JR      NC,$524A        
5241: 3E F0          LD      A,$F0           
5243: DD 77 00       LD      (IX+$00),A      
5246: 12             LD      (DE),A          
5247: CD DE 51       CALL    $51DE           
524A: 7B             LD      A,E             
524B: C6 10          ADD     $10             
524D: 5F             LD      E,A             
524E: FD 23          INC     IY              
5250: FD 23          INC     IY              
5252: 10 C3          DJNZ    $5217           
5254: FD 2A 91 A9    LD      IY,($A991)      
5258: ED 5B 93 A9    LD      DE,($A993)      
525C: 08             EX      AF,AF'          
525D: 47             LD      B,A             
525E: 08             EX      AF,AF'          
525F: DD 7D          LD      A,IXL           
5261: C6 10          ADD     $10             
5263: DD 6F          LD      IXL,A           
5265: 0D             DEC     C               
5266: C2 11 52       JP      NZ,$5211        
5269: C9             RET                     
526A: 21 84 AE       LD      HL,$AE84        
526D: 22 80 AE       LD      ($AE80),HL      
5270: 21 04 AE       LD      HL,$AE04        
5273: 22 00 AE       LD      ($AE00),HL      
5276: C9             RET                     
5277: 06 00          LD      B,$00           
5279: 21 DE 27       LD      HL,$27DE        
527C: AF             XOR     A               
527D: 86             ADD     A,(HL)          
527E: 23             INC     HL              
527F: 10 FC          DJNZ    $527D           
5281: D6 C5          SUB     $C5             
5283: C4 D4 53       CALL    NZ,$53D4        
5286: CD 0E 53       CALL    $530E           
5289: CD D2 52       CALL    $52D2           
528C: 3A 00 AE       LD      A,($AE00)       
528F: FE 04          CP      $04             
5291: 28 D7          JR      Z,$526A         
5293: 4F             LD      C,A             
5294: 06 00          LD      B,$00           
5296: 21 00 AE       LD      HL,$AE00        
5299: 11 80 AE       LD      DE,$AE80        
529C: ED B0          LDIR                    
529E: C6 80          ADD     $80             
52A0: 32 80 AE       LD      ($AE80),A       
52A3: 21 04 AE       LD      HL,$AE04        
52A6: 22 00 AE       LD      ($AE00),HL      
52A9: C9             RET                     
52AA: 3A C9 08       LD      A,($08C9)       
52AD: 32 8D A9       LD      ($A98D),A       
52B0: 3A 74 08       LD      A,($0874)       
52B3: 32 CD A9       LD      ($A9CD),A       
52B6: 3A 60 C3       LD      A,($C360)       
52B9: 2F             CPL                     
52BA: 32 B1 A9       LD      ($A9B1),A       
52BD: CD CC 4A       CALL    $4ACC           
52C0: 3A 00 C2       LD      A,($C200)       
52C3: 2F             CPL                     
52C4: 4F             LD      C,A             
52C5: E6 03          AND     $03             
52C7: C6 03          ADD     $03             
52C9: FE 06          CP      $06             
52CB: 20 02          JR      NZ,$52CF        
52CD: 3E FF          LD      A,$FF           
52CF: C3 19 2E       JP      $2E19           
52D2: 3A 0C AD       LD      A,($AD0C)       
52D5: E6 0F          AND     $0F             
52D7: 4F             LD      C,A             
52D8: 2A 00 AE       LD      HL,($AE00)      
52DB: 7D             LD      A,L             
52DC: D6 04          SUB     $04             
52DE: C8             RET     Z               
52DF: 0F             RRCA                    
52E0: 0F             RRCA                    
52E1: E6 1F          AND     $1F             
52E3: 47             LD      B,A             
52E4: 21 04 AE       LD      HL,$AE04        
52E7: 5E             LD      E,(HL)          
52E8: 2C             INC     L               
52E9: 56             LD      D,(HL)          
52EA: 2C             INC     L               
52EB: 1A             LD      A,(DE)          
52EC: E6 10          AND     $10             
52EE: 20 0E          JR      NZ,$52FE        
52F0: 7E             LD      A,(HL)          
52F1: CB D2          SET     2,D             
52F3: 12             LD      (DE),A          
52F4: CB 92          RES     2,D             
52F6: 2C             INC     L               
52F7: 7E             LD      A,(HL)          
52F8: 2C             INC     L               
52F9: 81             ADD     A,C             
52FA: 12             LD      (DE),A          
52FB: 10 EA          DJNZ    $52E7           
52FD: C9             RET                     
52FE: 2C             INC     L               
52FF: 2C             INC     L               
5300: 10 E5          DJNZ    $52E7           
5302: C9             RET                     
5303: CD 0C 20       CALL    $200C           
5306: FE 67          CP      $67             
5308: C2 8D 0F       JP      NZ,$0F8D        
530B: C3 1A 0F       JP      $0F1A           
530E: 2A 80 AE       LD      HL,($AE80)      
5311: 7D             LD      A,L             
5312: E6 7F          AND     $7F             
5314: D6 04          SUB     $04             
5316: C8             RET     Z               
5317: 0F             RRCA                    
5318: 0F             RRCA                    
5319: E6 1F          AND     $1F             
531B: 47             LD      B,A             
531C: 21 84 AE       LD      HL,$AE84        
531F: 5E             LD      E,(HL)          
5320: 2C             INC     L               
5321: 56             LD      D,(HL)          
5322: 2C             INC     L               
5323: 1A             LD      A,(DE)          
5324: E6 10          AND     $10             
5326: 20 0A          JR      NZ,$5332        
5328: 2C             INC     L               
5329: 2C             INC     L               
532A: CB D2          SET     2,D             
532C: 3E 20          LD      A,$20           
532E: 12             LD      (DE),A          
532F: 10 EE          DJNZ    $531F           
5331: C9             RET                     
5332: 2C             INC     L               
5333: 2C             INC     L               
5334: 10 E9          DJNZ    $531F           
5336: C9             RET                     
5337: DD 7E 04       LD      A,(IX+$04)      
533A: C6 07          ADD     $07             
533C: 47             LD      B,A             
533D: 16 28          LD      D,$28           
533F: 07             RLCA                    
5340: CB 12          RL      D               
5342: 07             RLCA                    
5343: CB 12          RL      D               
5345: E6 E0          AND     $E0             
5347: 5F             LD      E,A             
5348: DD 7E 06       LD      A,(IX+$06)      
534B: C6 07          ADD     $07             
534D: 4F             LD      C,A             
534E: 0F             RRCA                    
534F: 0F             RRCA                    
5350: 0F             RRCA                    
5351: E6 1F          AND     $1F             
5353: 83             ADD     A,E             
5354: 5F             LD      E,A             
5355: 79             LD      A,C             
5356: 07             RLCA                    
5357: 07             RLCA                    
5358: 07             RLCA                    
5359: E6 38          AND     $38             
535B: 4F             LD      C,A             
535C: 78             LD      A,B             
535D: 06 00          LD      B,$00           
535F: CB 57          BIT     2,A             
5361: 28 01          JR      Z,$5364         
5363: 04             INC     B               
5364: 0F             RRCA                    
5365: 0F             RRCA                    
5366: E6 C0          AND     $C0             
5368: 81             ADD     A,C             
5369: 4F             LD      C,A             
536A: 21 D4 53       LD      HL,$53D4        
536D: 09             ADD     HL,BC           
536E: 7E             LD      A,(HL)          
536F: 23             INC     HL              
5370: 46             LD      B,(HL)          
5371: 23             INC     HL              
5372: A7             AND     A               
5373: 28 10          JR      Z,$5385         
5375: E5             PUSH    HL              
5376: 2A 00 AE       LD      HL,($AE00)      
5379: 73             LD      (HL),E          
537A: 2C             INC     L               
537B: 72             LD      (HL),D          
537C: 2C             INC     L               
537D: 77             LD      (HL),A          
537E: 2C             INC     L               
537F: 70             LD      (HL),B          
5380: 2C             INC     L               
5381: 22 00 AE       LD      ($AE00),HL      
5384: E1             POP     HL              
5385: 13             INC     DE              
5386: 7E             LD      A,(HL)          
5387: 23             INC     HL              
5388: 46             LD      B,(HL)          
5389: 23             INC     HL              
538A: A7             AND     A               
538B: 28 10          JR      Z,$539D         
538D: E5             PUSH    HL              
538E: 2A 00 AE       LD      HL,($AE00)      
5391: 73             LD      (HL),E          
5392: 2C             INC     L               
5393: 72             LD      (HL),D          
5394: 2C             INC     L               
5395: 77             LD      (HL),A          
5396: 2C             INC     L               
5397: 70             LD      (HL),B          
5398: 2C             INC     L               
5399: 22 00 AE       LD      ($AE00),HL      
539C: E1             POP     HL              
539D: 7B             LD      A,E             
539E: C6 1F          ADD     $1F             
53A0: 5F             LD      E,A             
53A1: 30 01          JR      NC,$53A4        
53A3: 14             INC     D               
53A4: 7E             LD      A,(HL)          
53A5: 23             INC     HL              
53A6: 46             LD      B,(HL)          
53A7: 23             INC     HL              
53A8: A7             AND     A               
53A9: 28 10          JR      Z,$53BB         
53AB: E5             PUSH    HL              
53AC: 2A 00 AE       LD      HL,($AE00)      
53AF: 73             LD      (HL),E          
53B0: 2C             INC     L               
53B1: 72             LD      (HL),D          
53B2: 2C             INC     L               
53B3: 77             LD      (HL),A          
53B4: 2C             INC     L               
53B5: 70             LD      (HL),B          
53B6: 2C             INC     L               
53B7: 22 00 AE       LD      ($AE00),HL      
53BA: E1             POP     HL              
53BB: 13             INC     DE              
53BC: 7E             LD      A,(HL)          
53BD: 23             INC     HL              
53BE: 46             LD      B,(HL)          
53BF: 23             INC     HL              
53C0: A7             AND     A               
53C1: 28 10          JR      Z,$53D3         
53C3: E5             PUSH    HL              
53C4: 2A 00 AE       LD      HL,($AE00)      
53C7: 73             LD      (HL),E          
53C8: 2C             INC     L               
53C9: 72             LD      (HL),D          
53CA: 2C             INC     L               
53CB: 77             LD      (HL),A          
53CC: 2C             INC     L               
53CD: 70             LD      (HL),B          
53CE: 2C             INC     L               
53CF: 22 00 AE       LD      ($AE00),HL      
53D2: E1             POP     HL              
53D3: C9             RET                     
53D4: 24             INC     H               
53D5: 20 00          JR      NZ,$53D7        
53D7: 00             NOP                     
53D8: 00             NOP                     
53D9: 00             NOP                     
53DA: 00             NOP                     
53DB: 00             NOP                     
53DC: DD                                  
53DD: 20 00          JR      NZ,$53DF        
53DF: 00             NOP                     
53E0: 00             NOP                     
53E1: 00             NOP                     
53E2: 00             NOP                     
53E3: 00             NOP                     
53E4: 61             LD      H,C             
53E5: 20 00          JR      NZ,$53E7        
53E7: 00             NOP                     
53E8: 00             NOP                     
53E9: 00             NOP                     
53EA: 00             NOP                     
53EB: 00             NOP                     
53EC: 3C             INC     A               
53ED: 20 00          JR      NZ,$53EF        
53EF: 00             NOP                     
53F0: 00             NOP                     
53F1: 00             NOP                     
53F2: 00             NOP                     
53F3: 00             NOP                     
53F4: 61             LD      H,C             
53F5: 60             LD      H,B             
53F6: 00             NOP                     
53F7: 00             NOP                     
53F8: 00             NOP                     
53F9: 00             NOP                     
53FA: 00             NOP                     
53FB: 00             NOP                     
53FC: DD 60          LD      IXH,B           
53FE: 00             NOP                     
53FF: 00             NOP                     
5400: 00             NOP                     
5401: 00             NOP                     
5402: 00             NOP                     
5403: 00             NOP                     
5404: 24             INC     H               
5405: 60             LD      H,B             
5406: 00             NOP                     
5407: 00             NOP                     
5408: 00             NOP                     
5409: 00             NOP                     
540A: 00             NOP                     
540B: 00             NOP                     
540C: 39             ADD     HL,SP           
540D: 20 39          JR      NZ,$5448        
540F: 60             LD      H,B             
5410: 00             NOP                     
5411: 00             NOP                     
5412: 00             NOP                     
5413: 00             NOP                     
5414: 30 20          JR      NC,$5436        
5416: 00             NOP                     
5417: 00             NOP                     
5418: 00             NOP                     
5419: 00             NOP                     
541A: 00             NOP                     
541B: 00             NOP                     
541C: A1             AND     C               
541D: 20 00          JR      NZ,$541F        
541F: 00             NOP                     
5420: 00             NOP                     
5421: 00             NOP                     
5422: 00             NOP                     
5423: 00             NOP                     
5424: B7             OR      A               
5425: 20 00          JR      NZ,$5427        
5427: 00             NOP                     
5428: 00             NOP                     
5429: 00             NOP                     
542A: 00             NOP                     
542B: 00             NOP                     
542C: D0             RET     NC              
542D: 20 00          JR      NZ,$542F        
542F: 00             NOP                     
5430: 00             NOP                     
5431: 00             NOP                     
5432: 00             NOP                     
5433: 00             NOP                     
5434: B7             OR      A               
5435: 60             LD      H,B             
5436: 00             NOP                     
5437: 00             NOP                     
5438: 00             NOP                     
5439: 00             NOP                     
543A: 00             NOP                     
543B: 00             NOP                     
543C: A1             AND     C               
543D: 60             LD      H,B             
543E: 00             NOP                     
543F: 00             NOP                     
5440: 00             NOP                     
5441: 00             NOP                     
5442: 00             NOP                     
5443: 00             NOP                     
5444: 30 60          JR      NC,$54A6        
5446: 00             NOP                     
5447: 00             NOP                     
5448: 00             NOP                     
5449: 00             NOP                     
544A: 00             NOP                     
544B: 00             NOP                     
544C: 6D             LD      L,L             
544D: 20 6D          JR      NZ,$54BC        
544F: 60             LD      H,B             
5450: 00             NOP                     
5451: 00             NOP                     
5452: 00             NOP                     
5453: 00             NOP                     
5454: 40             LD      B,B             
5455: 20 00          JR      NZ,$5457        
5457: 00             NOP                     
5458: 00             NOP                     
5459: 00             NOP                     
545A: 00             NOP                     
545B: 00             NOP                     
545C: 34             INC     (HL)            
545D: 20 00          JR      NZ,$545F        
545F: 00             NOP                     
5460: 00             NOP                     
5461: 00             NOP                     
5462: 00             NOP                     
5463: 00             NOP                     
5464: 2B             DEC     HL              
5465: 20 00          JR      NZ,$5467        
5467: 00             NOP                     
5468: 00             NOP                     
5469: 00             NOP                     
546A: 00             NOP                     
546B: 00             NOP                     
546C: B1             OR      C               
546D: 20 00          JR      NZ,$546F        
546F: 00             NOP                     
5470: 00             NOP                     
5471: 00             NOP                     
5472: 00             NOP                     
5473: 00             NOP                     
5474: 2B             DEC     HL              
5475: 60             LD      H,B             
5476: 00             NOP                     
5477: 00             NOP                     
5478: 00             NOP                     
5479: 00             NOP                     
547A: 00             NOP                     
547B: 00             NOP                     
547C: 34             INC     (HL)            
547D: 60             LD      H,B             
547E: 00             NOP                     
547F: 00             NOP                     
5480: 00             NOP                     
5481: 00             NOP                     
5482: 00             NOP                     
5483: 00             NOP                     
5484: 40             LD      B,B             
5485: 60             LD      H,B             
5486: 00             NOP                     
5487: 00             NOP                     
5488: 00             NOP                     
5489: 00             NOP                     
548A: 00             NOP                     
548B: 00             NOP                     
548C: 8E             ADC     A,(HL)          
548D: 20 8E          JR      NZ,$541D        
548F: 60             LD      H,B             
5490: 00             NOP                     
5491: 00             NOP                     
5492: 00             NOP                     
5493: 00             NOP                     
5494: 74             LD      (HL),H          
5495: 20 00          JR      NZ,$5497        
5497: 00             NOP                     
5498: 00             NOP                     
5499: 00             NOP                     
549A: 00             NOP                     
549B: 00             NOP                     
549C: 54             LD      D,H             
549D: 20 00          JR      NZ,$549F        
549F: 00             NOP                     
54A0: 00             NOP                     
54A1: 00             NOP                     
54A2: 00             NOP                     
54A3: 00             NOP                     
54A4: 4C             LD      C,H             
54A5: 20 00          JR      NZ,$54A7        
54A7: 00             NOP                     
54A8: 00             NOP                     
54A9: 00             NOP                     
54AA: 00             NOP                     
54AB: 00             NOP                     
54AC: 2D             DEC     L               
54AD: 20 00          JR      NZ,$54AF        
54AF: 00             NOP                     
54B0: 00             NOP                     
54B1: 00             NOP                     
54B2: 00             NOP                     
54B3: 00             NOP                     
54B4: 4C             LD      C,H             
54B5: 60             LD      H,B             
54B6: 00             NOP                     
54B7: 00             NOP                     
54B8: 00             NOP                     
54B9: 00             NOP                     
54BA: 00             NOP                     
54BB: 00             NOP                     
54BC: 54             LD      D,H             
54BD: 60             LD      H,B             
54BE: 00             NOP                     
54BF: 00             NOP                     
54C0: 00             NOP                     
54C1: 00             NOP                     
54C2: 00             NOP                     
54C3: 00             NOP                     
54C4: 74             LD      (HL),H          
54C5: 60             LD      H,B             
54C6: 00             NOP                     
54C7: 00             NOP                     
54C8: 00             NOP                     
54C9: 00             NOP                     
54CA: 00             NOP                     
54CB: 00             NOP                     
54CC: D5             PUSH    DE              
54CD: 20 D5          JR      NZ,$54A4        
54CF: 60             LD      H,B             
54D0: 00             NOP                     
54D1: 00             NOP                     
54D2: 00             NOP                     
54D3: 00             NOP                     
54D4: 40             LD      B,B             
54D5: A0             AND     B               
54D6: 00             NOP                     
54D7: 00             NOP                     
54D8: 00             NOP                     
54D9: 00             NOP                     
54DA: 00             NOP                     
54DB: 00             NOP                     
54DC: 34             INC     (HL)            
54DD: A0             AND     B               
54DE: 00             NOP                     
54DF: 00             NOP                     
54E0: 00             NOP                     
54E1: 00             NOP                     
54E2: 00             NOP                     
54E3: 00             NOP                     
54E4: 2B             DEC     HL              
54E5: A0             AND     B               
54E6: 00             NOP                     
54E7: 00             NOP                     
54E8: 00             NOP                     
54E9: 00             NOP                     
54EA: 00             NOP                     
54EB: 00             NOP                     
54EC: B1             OR      C               
54ED: A0             AND     B               
54EE: 00             NOP                     
54EF: 00             NOP                     
54F0: 00             NOP                     
54F1: 00             NOP                     
54F2: 00             NOP                     
54F3: 00             NOP                     
54F4: 2B             DEC     HL              
54F5: E0             RET     PO              
54F6: 00             NOP                     
54F7: 00             NOP                     
54F8: 00             NOP                     
54F9: 00             NOP                     
54FA: 00             NOP                     
54FB: 00             NOP                     
54FC: 34             INC     (HL)            
54FD: E0             RET     PO              
54FE: 00             NOP                     
54FF: 00             NOP                     
5500: 00             NOP                     
5501: 00             NOP                     
5502: 00             NOP                     
5503: 00             NOP                     
5504: 40             LD      B,B             
5505: E0             RET     PO              
5506: 00             NOP                     
5507: 00             NOP                     
5508: 00             NOP                     
5509: 00             NOP                     
550A: 00             NOP                     
550B: 00             NOP                     
550C: 8E             ADC     A,(HL)          
550D: A0             AND     B               
550E: 8E             ADC     A,(HL)          
550F: E0             RET     PO              
5510: 00             NOP                     
5511: 00             NOP                     
5512: 00             NOP                     
5513: 00             NOP                     
5514: 30 A0          JR      NC,$54B6        
5516: 00             NOP                     
5517: 00             NOP                     
5518: 00             NOP                     
5519: 00             NOP                     
551A: 00             NOP                     
551B: 00             NOP                     
551C: A1             AND     C               
551D: A0             AND     B               
551E: 00             NOP                     
551F: 00             NOP                     
5520: 00             NOP                     
5521: 00             NOP                     
5522: 00             NOP                     
5523: 00             NOP                     
5524: B7             OR      A               
5525: A0             AND     B               
5526: 00             NOP                     
5527: 00             NOP                     
5528: 00             NOP                     
5529: 00             NOP                     
552A: 00             NOP                     
552B: 00             NOP                     
552C: D0             RET     NC              
552D: A0             AND     B               
552E: 00             NOP                     
552F: 00             NOP                     
5530: 00             NOP                     
5531: 00             NOP                     
5532: 00             NOP                     
5533: 00             NOP                     
5534: B7             OR      A               
5535: E0             RET     PO              
5536: 00             NOP                     
5537: 00             NOP                     
5538: 00             NOP                     
5539: 00             NOP                     
553A: 00             NOP                     
553B: 00             NOP                     
553C: A1             AND     C               
553D: E0             RET     PO              
553E: 00             NOP                     
553F: 00             NOP                     
5540: 00             NOP                     
5541: 00             NOP                     
5542: 00             NOP                     
5543: 00             NOP                     
5544: 30 E0          JR      NC,$5526        
5546: 00             NOP                     
5547: 00             NOP                     
5548: 00             NOP                     
5549: 00             NOP                     
554A: 00             NOP                     
554B: 00             NOP                     
554C: 6D             LD      L,L             
554D: A0             AND     B               
554E: 6D             LD      L,L             
554F: E0             RET     PO              
5550: 00             NOP                     
5551: 00             NOP                     
5552: 00             NOP                     
5553: 00             NOP                     
5554: 24             INC     H               
5555: A0             AND     B               
5556: 00             NOP                     
5557: 00             NOP                     
5558: 00             NOP                     
5559: 00             NOP                     
555A: 00             NOP                     
555B: 00             NOP                     
555C: DD                                  
555D: A0             AND     B               
555E: 00             NOP                     
555F: 00             NOP                     
5560: 00             NOP                     
5561: 00             NOP                     
5562: 00             NOP                     
5563: 00             NOP                     
5564: 61             LD      H,C             
5565: A0             AND     B               
5566: 00             NOP                     
5567: 00             NOP                     
5568: 00             NOP                     
5569: 00             NOP                     
556A: 00             NOP                     
556B: 00             NOP                     
556C: 3C             INC     A               
556D: A0             AND     B               
556E: 00             NOP                     
556F: 00             NOP                     
5570: 00             NOP                     
5571: 00             NOP                     
5572: 00             NOP                     
5573: 00             NOP                     
5574: 61             LD      H,C             
5575: E0             RET     PO              
5576: 00             NOP                     
5577: 00             NOP                     
5578: 00             NOP                     
5579: 00             NOP                     
557A: 00             NOP                     
557B: 00             NOP                     
557C: DD                                  
557D: E0             RET     PO              
557E: 00             NOP                     
557F: 00             NOP                     
5580: 00             NOP                     
5581: 00             NOP                     
5582: 00             NOP                     
5583: 00             NOP                     
5584: 24             INC     H               
5585: E0             RET     PO              
5586: 00             NOP                     
5587: 00             NOP                     
5588: 00             NOP                     
5589: 00             NOP                     
558A: 00             NOP                     
558B: 00             NOP                     
558C: 39             ADD     HL,SP           
558D: A0             AND     B               
558E: 39             ADD     HL,SP           
558F: E0             RET     PO              
5590: 00             NOP                     
5591: 00             NOP                     
5592: 00             NOP                     
5593: 00             NOP                     
5594: 3A 20 00       LD      A,($0020)       
5597: 00             NOP                     
5598: 3A A0 00       LD      A,($00A0)       
559B: 00             NOP                     
559C: 8F             ADC     A,A             
559D: 20 00          JR      NZ,$559F        
559F: 00             NOP                     
55A0: 8F             ADC     A,A             
55A1: A0             AND     B               
55A2: 00             NOP                     
55A3: 00             NOP                     
55A4: 70             LD      (HL),B          
55A5: 20 00          JR      NZ,$55A7        
55A7: 00             NOP                     
55A8: 70             LD      (HL),B          
55A9: A0             AND     B               
55AA: 00             NOP                     
55AB: 00             NOP                     
55AC: 66             LD      H,(HL)          
55AD: 20 00          JR      NZ,$55AF        
55AF: 00             NOP                     
55B0: 66             LD      H,(HL)          
55B1: A0             AND     B               
55B2: 00             NOP                     
55B3: 00             NOP                     
55B4: 70             LD      (HL),B          
55B5: 60             LD      H,B             
55B6: 00             NOP                     
55B7: 00             NOP                     
55B8: 70             LD      (HL),B          
55B9: E0             RET     PO              
55BA: 00             NOP                     
55BB: 00             NOP                     
55BC: 8F             ADC     A,A             
55BD: 60             LD      H,B             
55BE: 00             NOP                     
55BF: 00             NOP                     
55C0: 8F             ADC     A,A             
55C1: E0             RET     PO              
55C2: 00             NOP                     
55C3: 00             NOP                     
55C4: 3A 60 00       LD      A,($0060)       
55C7: 00             NOP                     
55C8: 3A E0 00       LD      A,($00E0)       
55CB: 00             NOP                     
55CC: C7             RST     0X00            
55CD: 20 C7          JR      NZ,$5596        
55CF: 60             LD      H,B             
55D0: C7             RST     0X00            
55D1: A0             AND     B               
55D2: C7             RST     0X00            
55D3: E0             RET     PO              
55D4: 21 43 AC       LD      HL,$AC43        
55D7: 7E             LD      A,(HL)          
55D8: A7             AND     A               
55D9: C8             RET     Z               
55DA: 35             DEC     (HL)            
55DB: F5             PUSH    AF              
55DC: 23             INC     HL              
55DD: 7E             LD      A,(HL)          
55DE: CD F8 55       CALL    $55F8           
55E1: F1             POP     AF              
55E2: C8             RET     Z               
55E3: 3D             DEC     A               
55E4: 06 00          LD      B,$00           
55E6: 4F             LD      C,A             
55E7: 5D             LD      E,L             
55E8: 54             LD      D,H             
55E9: 23             INC     HL              
55EA: ED B0          LDIR                    
55EC: C9             RET                     
55ED: 73             LD      (HL),E          
55EE: A6             AND     (HL)            
55EF: 14             INC     D               
55F0: 7E             LD      A,(HL)          
55F1: 29             ADD     HL,HL           
55F2: F8             RET     M               
55F3: 96             SUB     (HL)            
55F4: 5D             LD      E,L             
55F5: 17             RLA                     
55F6: 9B             SBC     E               
55F7: B9             CP      C               
55F8: 32 00 C0       LD      ($C000),A       
55FB: 3E 01          LD      A,$01           
55FD: 32 04 C3       LD      ($C304),A       
5600: 00             NOP                     
5601: 00             NOP                     
5602: 00             NOP                     
5603: 00             NOP                     
5604: 00             NOP                     
5605: 00             NOP                     
5606: 3E 00          LD      A,$00           
5608: 32 04 C3       LD      ($C304),A       
560B: C9             RET                     
560C: E5             PUSH    HL              
560D: F5             PUSH    AF              
560E: 3A 30 AD       LD      A,($AD30)       
5611: A7             AND     A               
5612: 20 16          JR      NZ,$562A        
5614: F1             POP     AF              
5615: E1             POP     HL              
5616: C9             RET                     
5617: E5             PUSH    HL              
5618: F5             PUSH    AF              
5619: 3A 30 AD       LD      A,($AD30)       
561C: A7             AND     A               
561D: 20 0B          JR      NZ,$562A        
561F: 3A C6 A9       LD      A,($A9C6)       
5622: A7             AND     A               
5623: 20 05          JR      NZ,$562A        
5625: F1             POP     AF              
5626: E1             POP     HL              
5627: C9             RET                     
5628: E5             PUSH    HL              
5629: F5             PUSH    AF              
562A: 21 43 AC       LD      HL,$AC43        
562D: 34             INC     (HL)            
562E: 7E             LD      A,(HL)          
562F: CF             RST     0X08            
5630: F1             POP     AF              
5631: 77             LD      (HL),A          
5632: E1             POP     HL              
5633: C9             RET                     
5634: 3A 7C 16       LD      A,($167C)       
5637: CD 28 56       CALL    $5628           
563A: 3A 9C 0A       LD      A,($0A9C)       
563D: CD 28 56       CALL    $5628           
5640: 3A 84 14       LD      A,($1484)       
5643: CD 28 56       CALL    $5628           
5646: 3A 78 0C       LD      A,($0C78)       
5649: CD 28 56       CALL    $5628           
564C: 3A D3 07       LD      A,($07D3)       
564F: CD 28 56       CALL    $5628           
5652: 3A B4 33       LD      A,($33B4)       
5655: CD 28 56       CALL    $5628           
5658: 3A 04 AD       LD      A,($AD04)       
565B: C6 8C          ADD     $8C             
565D: 18 C9          JR      $5628           
565F: 3A A2 07       LD      A,($07A2)       
5662: 18 A8          JR      $560C           
5664: 3A DE 16       LD      A,($16DE)       
5667: 18 A3          JR      $560C           
5669: 3A 9F 4C       LD      A,($4C9F)       
566C: 18 9E          JR      $560C           
566E: 3A D8 07       LD      A,($07D8)       
5671: CD 0C 56       CALL    $560C           
5674: 3A 6B 27       LD      A,($276B)       
5677: 18 93          JR      $560C           
5679: 3A FE 07       LD      A,($07FE)       
567C: 18 8E          JR      $560C           
567E: 3A 70 32       LD      A,($3270)       
5681: 18 94          JR      $5617           
5683: 3A A6 07       LD      A,($07A6)       
5686: CD 17 56       CALL    $5617           
5689: 3A DA 4C       LD      A,($4CDA)       
568C: 18 89          JR      $5617           
568E: 3A 87 2D       LD      A,($2D87)       
5691: C3 0C 56       JP      $560C           
5694: 0E 00          LD      C,$00           
5696: 21 31 08       LD      HL,$0831        
5699: 3A AB A9       LD      A,($A9AB)       
569C: 96             SUB     (HL)            
569D: 23             INC     HL              
569E: 0D             DEC     C               
569F: 20 FB          JR      NZ,$569C        
56A1: EE C2          XOR     $C2             
56A3: 32 AB A9       LD      ($A9AB),A       
56A6: CD 97 0F       CALL    $0F97           
56A9: CD DF 1E       CALL    $1EDF           
56AC: CD 97 0F       CALL    $0F97           
56AF: CD BC 2C       CALL    $2CBC           
56B2: CD E3 23       CALL    $23E3           
56B5: CD 98 10       CALL    $1098           
56B8: 21 EB A9       LD      HL,$A9EB        
56BB: 35             DEC     (HL)            
56BC: C0             RET     NZ              
56BD: 0E 00          LD      C,$00           
56BF: 21 A7 12       LD      HL,$12A7        
56C2: 3A AB A9       LD      A,($A9AB)       
56C5: 96             SUB     (HL)            
56C6: 23             INC     HL              
56C7: 0D             DEC     C               
56C8: 20 FB          JR      NZ,$56C5        
56CA: EE 59          XOR     $59             
56CC: 32 AB A9       LD      ($A9AB),A       
56CF: C3 1A 0F       JP      $0F1A           
56D2: 3A 5B 0C       LD      A,($0C5B)       
56D5: CD 0C 56       CALL    $560C           
56D8: 3A 55 08       LD      A,($0855)       
56DB: CD 0C 56       CALL    $560C           
56DE: 3A 75 16       LD      A,($1675)       
56E1: CD 0C 56       CALL    $560C           
56E4: 3A CB 27       LD      A,($27CB)       
56E7: CD 17 56       CALL    $5617           
56EA: 3A A0 33       LD      A,($33A0)       
56ED: C3 17 56       JP      $5617           
56F0: FF             RST     0X38            
56F1: 00             NOP                     
56F2: 01 00 00       LD      BC,$0000        
56F5: 00             NOP                     
56F6: 00             NOP                     
56F7: 00             NOP                     
56F8: 00             NOP                     
56F9: 00             NOP                     
56FA: 00             NOP                     
56FB: 00             NOP                     
56FC: 00             NOP                     
56FD: 00             NOP                     
56FE: 00             NOP                     
56FF: 00             NOP                     
5700: 00             NOP                     
5701: 01 00 00       LD      BC,$0000        
5704: 00             NOP                     
5705: 00             NOP                     
5706: 00             NOP                     
5707: 00             NOP                     
5708: 00             NOP                     
5709: 00             NOP                     
570A: 00             NOP                     
570B: 00             NOP                     
570C: 00             NOP                     
570D: 00             NOP                     
570E: 00             NOP                     
570F: 00             NOP                     
5710: 01 01 00       LD      BC,$0001        
5713: 00             NOP                     
5714: 00             NOP                     
5715: 00             NOP                     
5716: 00             NOP                     
5717: 00             NOP                     
5718: 00             NOP                     
5719: 00             NOP                     
571A: 00             NOP                     
571B: 00             NOP                     
571C: 00             NOP                     
571D: 00             NOP                     
571E: 00             NOP                     
571F: 00             NOP                     
5720: 00             NOP                     
5721: 01 00 00       LD      BC,$0000        
5724: 00             NOP                     
5725: 00             NOP                     
5726: 00             NOP                     
5727: 00             NOP                     
5728: 00             NOP                     
5729: 00             NOP                     
572A: 00             NOP                     
572B: 00             NOP                     
572C: 00             NOP                     
572D: 00             NOP                     
572E: 01 00 00       LD      BC,$0000        
5731: 01 01 00       LD      BC,$0001        
5734: 00             NOP                     
5735: 00             NOP                     
5736: 00             NOP                     
5737: 00             NOP                     
5738: 00             NOP                     
5739: 00             NOP                     
573A: 00             NOP                     
573B: 00             NOP                     
573C: 00             NOP                     
573D: 00             NOP                     
573E: 00             NOP                     
573F: 00             NOP                     
5740: 00             NOP                     
5741: 00             NOP                     
5742: 01 01 00       LD      BC,$0001        
5745: 00             NOP                     
5746: 00             NOP                     
5747: 00             NOP                     
5748: 00             NOP                     
5749: 00             NOP                     
574A: 00             NOP                     
574B: 00             NOP                     
574C: 01 00 00       LD      BC,$0000        
574F: 00             NOP                     
5750: 00             NOP                     
5751: 00             NOP                     
5752: 00             NOP                     
5753: 01 01 01       LD      BC,$0101        
5756: 00             NOP                     
5757: 00             NOP                     
5758: 00             NOP                     
5759: 00             NOP                     
575A: 00             NOP                     
575B: 00             NOP                     
575C: 00             NOP                     
575D: 00             NOP                     
575E: 00             NOP                     
575F: 00             NOP                     
5760: 00             NOP                     
5761: 00             NOP                     
5762: 00             NOP                     
5763: 00             NOP                     
5764: 00             NOP                     
5765: 01 01 01       LD      BC,$0101        
5768: 01 00 01       LD      BC,$0100        
576B: 00             NOP                     
576C: 00             NOP                     
576D: 00             NOP                     
576E: 00             NOP                     
576F: 00             NOP                     
5770: 00             NOP                     
5771: 00             NOP                     
5772: 00             NOP                     
5773: 00             NOP                     
5774: 00             NOP                     
5775: 00             NOP                     
5776: 00             NOP                     
5777: 00             NOP                     
5778: 00             NOP                     
5779: 01 01 00       LD      BC,$0001        
577C: 00             NOP                     
577D: 00             NOP                     
577E: 00             NOP                     
577F: 00             NOP                     
5780: 00             NOP                     
5781: 00             NOP                     
5782: 00             NOP                     
5783: 00             NOP                     
5784: 00             NOP                     
5785: 00             NOP                     
5786: 00             NOP                     
5787: 00             NOP                     
5788: 01 00 01       LD      BC,$0100        
578B: 00             NOP                     
578C: 00             NOP                     
578D: 00             NOP                     
578E: 00             NOP                     
578F: 00             NOP                     
5790: 00             NOP                     
5791: 00             NOP                     
5792: 00             NOP                     
5793: 00             NOP                     
5794: 00             NOP                     
5795: 00             NOP                     
5796: 00             NOP                     
5797: 01 00 00       LD      BC,$0000        
579A: 01 01 00       LD      BC,$0001        
579D: 00             NOP                     
579E: 00             NOP                     
579F: 00             NOP                     
57A0: 00             NOP                     
57A1: 00             NOP                     
57A2: 00             NOP                     
57A3: 00             NOP                     
57A4: 00             NOP                     
57A5: 00             NOP                     
57A6: 01 01 00       LD      BC,$0001        
57A9: 00             NOP                     
57AA: 00             NOP                     
57AB: 01 01 01       LD      BC,$0101        
57AE: 00             NOP                     
57AF: 00             NOP                     
57B0: 00             NOP                     
57B1: 00             NOP                     
57B2: 00             NOP                     
57B3: 00             NOP                     
57B4: 01 01 00       LD      BC,$0001        
57B7: 01 01 00       LD      BC,$0001        
57BA: 00             NOP                     
57BB: 00             NOP                     
57BC: 00             NOP                     
57BD: 01 01 00       LD      BC,$0001        
57C0: 00             NOP                     
57C1: 00             NOP                     
57C2: 00             NOP                     
57C3: 01 01 01       LD      BC,$0101        
57C6: 00             NOP                     
57C7: 00             NOP                     
57C8: 01 01 01       LD      BC,$0101        
57CB: 00             NOP                     
57CC: 00             NOP                     
57CD: 00             NOP                     
57CE: 00             NOP                     
57CF: 00             NOP                     
57D0: 00             NOP                     
57D1: 00             NOP                     
57D2: 01 01 00       LD      BC,$0001        
57D5: 01 01 00       LD      BC,$0001        
57D8: 00             NOP                     
57D9: 00             NOP                     
57DA: 00             NOP                     
57DB: 00             NOP                     
57DC: 00             NOP                     
57DD: 00             NOP                     
57DE: 00             NOP                     
57DF: 00             NOP                     
57E0: 00             NOP                     
57E1: 01 00 01       LD      BC,$0100        
57E4: 00             NOP                     
57E5: 00             NOP                     
57E6: 00             NOP                     
57E7: 00             NOP                     
57E8: 00             NOP                     
57E9: 00             NOP                     
57EA: 00             NOP                     
57EB: 00             NOP                     
57EC: 00             NOP                     
57ED: 00             NOP                     
57EE: 00             NOP                     
57EF: 00             NOP                     
57F0: FF             RST     0X38            
57F1: 3A 2E 32       LD      A,($322E)       
57F4: C3 28 56       JP      $5628           
57F7: 3A 04 AD       LD      A,($AD04)       
57FA: C6 0C          ADD     $0C             
57FC: C3 0C 56       JP      $560C           
57FF: 3A 9B 07       LD      A,($079B)       
5802: C3 0C 56       JP      $560C           
5805: 3A 4E 2D       LD      A,($2D4E)       
5808: C3 0C 56       JP      $560C           
580B: 3A EE 49       LD      A,($49EE)       
580E: C3 0C 56       JP      $560C           
5811: 3A A9 07       LD      A,($07A9)       
5814: C3 0C 56       JP      $560C           
5817: 3A 3A 27       LD      A,($273A)       
581A: C3 0C 56       JP      $560C           
581D: 0C             INC     C               
581E: A7             AND     A               
581F: 13             INC     DE              
5820: 88             ADC     A,B             
5821: 57             LD      D,A             
5822: 34             INC     (HL)            
5823: A5             AND     L               
5824: ED                                  
5825: 34             INC     (HL)            
5826: F1             POP     AF              
5827: 87             ADD     A,A             
5828: 34             INC     (HL)            
5829: 88             ADC     A,B             
582A: 68             LD      L,B             
582B: ED                                  
582C: FD DC F1 77    CALL    C,$77F1         
5830: 68             LD      L,B             
5831: FD                                  
5832: 3B             DEC     SP              
5833: B9             CP      C               
5834: 3A 67 17       LD      A,($1767)       
5837: C3 0C 56       JP      $560C           
583A: 3A FA 18       LD      A,($18FA)       
583D: C3 0C 56       JP      $560C           
5840: 21 D7 59       LD      HL,$59D7        
5843: C3 BC 58       JP      $58BC           
5846: 21 00 5C       LD      HL,$5C00        
5849: C3 BC 58       JP      $58BC           
584C: 60             LD      H,B             
584D: A7             AND     A               
584E: 14             INC     D               
584F: 96             SUB     (HL)            
5850: 10 0D          DJNZ    $585F           
5852: 88             ADC     A,B             
5853: B9             CP      C               
5854: 21 00 5E       LD      HL,$5E00        
5857: C3 BC 58       JP      $58BC           
585A: 21 30 25       LD      HL,$2530        
585D: C3 BC 58       JP      $58BC           
5860: 21 3E 2E       LD      HL,$2E3E        
5863: C3 BC 58       JP      $58BC           
5866: 2A 81 25       LD      HL,($2581)      
5869: 01 00 04       LD      BC,$0400        
586C: 16 10          LD      D,$10           
586E: 72             LD      (HL),D          
586F: 23             INC     HL              
5870: 0B             DEC     BC              
5871: 79             LD      A,C             
5872: B0             OR      B               
5873: 20 F9          JR      NZ,$586E        
5875: 32 00 C2       LD      ($C200),A       
5878: 2A 37 4A       LD      HL,($4A37)      
587B: 01 00 04       LD      BC,$0400        
587E: 16 F1          LD      D,$F1           
5880: 72             LD      (HL),D          
5881: 23             INC     HL              
5882: 0B             DEC     BC              
5883: 79             LD      A,C             
5884: B0             OR      B               
5885: 20 F9          JR      NZ,$5880        
5887: 21 00 00       LD      HL,$0000        
588A: 3A 00 00       LD      A,($0000)       
588D: 86             ADD     A,(HL)          
588E: 23             INC     HL              
588F: 08             EX      AF,AF'          
5890: 7C             LD      A,H             
5891: FE 60          CP      $60             
5893: 30 06          JR      NC,$589B        
5895: 08             EX      AF,AF'          
5896: 32 00 C2       LD      ($C200),A       
5899: 18 F2          JR      $588D           
589B: 08             EX      AF,AF'          
589C: D6 AF          SUB     $AF             
589E: C2 D7 59       JP      NZ,$59D7        
58A1: C3 11 25       JP      $2511           
58A4: 21 FA 08       LD      HL,$08FA        
58A7: C3 BC 58       JP      $58BC           
58AA: 21 D7 59       LD      HL,$59D7        
58AD: C3 FE 58       JP      $58FE           
58B0: 21 00 5C       LD      HL,$5C00        
58B3: C3 FE 58       JP      $58FE           
58B6: 21 00 5E       LD      HL,$5E00        
58B9: C3 FE 58       JP      $58FE           
58BC: DD 7E 02       LD      A,(IX+$02)      
58BF: 4F             LD      C,A             
58C0: 87             ADD     A,A             
58C1: 30 01          JR      NC,$58C4        
58C3: 24             INC     H               
58C4: 85             ADD     A,L             
58C5: 6F             LD      L,A             
58C6: 30 01          JR      NC,$58C9        
58C8: 24             INC     H               
58C9: 5E             LD      E,(HL)          
58CA: 23             INC     HL              
58CB: 56             LD      D,(HL)          
58CC: 79             LD      A,C             
58CD: C6 C0          ADD     $C0             
58CF: 01 80 01       LD      BC,$0180        
58D2: 30 03          JR      NC,$58D7        
58D4: 01 80 FF       LD      BC,$FF80        
58D7: 09             ADD     HL,BC           
58D8: 46             LD      B,(HL)          
58D9: 2B             DEC     HL              
58DA: 4E             LD      C,(HL)          
58DB: 2A 08 A8       LD      HL,($A808)      
58DE: 19             ADD     HL,DE           
58DF: DD 5E 03       LD      E,(IX+$03)      
58E2: FD 56 31       LD      D,(IY+$31)      
58E5: 19             ADD     HL,DE           
58E6: DD 75 03       LD      (IX+$03),L      
58E9: FD 74 31       LD      (IY+$31),H      
58EC: 2A 0A A8       LD      HL,($A80A)      
58EF: 09             ADD     HL,BC           
58F0: DD 5E 05       LD      E,(IX+$05)      
58F3: FD 56 00       LD      D,(IY+$00)      
58F6: 19             ADD     HL,DE           
58F7: DD 75 05       LD      (IX+$05),L      
58FA: FD 74 00       LD      (IY+$00),H      
58FD: C9             RET                     
58FE: DD 7E 02       LD      A,(IX+$02)      
5901: 4F             LD      C,A             
5902: 87             ADD     A,A             
5903: 30 01          JR      NC,$5906        
5905: 24             INC     H               
5906: 85             ADD     A,L             
5907: 6F             LD      L,A             
5908: 30 01          JR      NC,$590B        
590A: 24             INC     H               
590B: 5E             LD      E,(HL)          
590C: 23             INC     HL              
590D: 56             LD      D,(HL)          
590E: 79             LD      A,C             
590F: C6 C0          ADD     $C0             
5911: 01 80 01       LD      BC,$0180        
5914: 30 03          JR      NC,$5919        
5916: 01 80 FF       LD      BC,$FF80        
5919: 09             ADD     HL,BC           
591A: 46             LD      B,(HL)          
591B: 2B             DEC     HL              
591C: 4E             LD      C,(HL)          
591D: 2A 08 A8       LD      HL,($A808)      
5920: 19             ADD     HL,DE           
5921: 19             ADD     HL,DE           
5922: DD 5E 03       LD      E,(IX+$03)      
5925: FD 56 31       LD      D,(IY+$31)      
5928: 19             ADD     HL,DE           
5929: DD 75 03       LD      (IX+$03),L      
592C: FD 74 31       LD      (IY+$31),H      
592F: 2A 0A A8       LD      HL,($A80A)      
5932: 09             ADD     HL,BC           
5933: 09             ADD     HL,BC           
5934: DD 5E 05       LD      E,(IX+$05)      
5937: FD 56 00       LD      D,(IY+$00)      
593A: 19             ADD     HL,DE           
593B: DD 75 05       LD      (IX+$05),L      
593E: FD 74 00       LD      (IY+$00),H      
5941: C9             RET                     
5942: 21 D7 59       LD      HL,$59D7        
5945: C3 6E 59       JP      $596E           
5948: 21 00 5C       LD      HL,$5C00        
594B: C3 6E 59       JP      $596E           
594E: 21 00 5E       LD      HL,$5E00        
5951: C3 6E 59       JP      $596E           
5954: 73             LD      (HL),E          
5955: A6             AND     (HL)            
5956: 14             INC     D               
5957: 7E             LD      A,(HL)          
5958: 29             ADD     HL,HL           
5959: F8             RET     M               
595A: 96             SUB     (HL)            
595B: 5D             LD      E,L             
595C: 02             LD      (BC),A          
595D: 13             INC     DE              
595E: B9             CP      C               
595F: 21 30 25       LD      HL,$2530        
5962: C3 6E 59       JP      $596E           
5965: 21 3E 2E       LD      HL,$2E3E        
5968: C3 6E 59       JP      $596E           
596B: 21 FA 08       LD      HL,$08FA        
596E: DD 7E 02       LD      A,(IX+$02)      
5971: 4F             LD      C,A             
5972: 87             ADD     A,A             
5973: 30 01          JR      NC,$5976        
5975: 24             INC     H               
5976: 85             ADD     A,L             
5977: 6F             LD      L,A             
5978: 30 01          JR      NC,$597B        
597A: 24             INC     H               
597B: 5E             LD      E,(HL)          
597C: 23             INC     HL              
597D: 56             LD      D,(HL)          
597E: 79             LD      A,C             
597F: C6 C0          ADD     $C0             
5981: 01 80 01       LD      BC,$0180        
5984: 30 03          JR      NC,$5989        
5986: 01 80 FF       LD      BC,$FF80        
5989: 09             ADD     HL,BC           
598A: 46             LD      B,(HL)          
598B: 2B             DEC     HL              
598C: 4E             LD      C,(HL)          
598D: C9             RET                     
598E: 21 D7 59       LD      HL,$59D7        
5991: C3 9D 59       JP      $599D           
5994: 21 00 5C       LD      HL,$5C00        
5997: C3 9D 59       JP      $599D           
599A: 21 00 5E       LD      HL,$5E00        
599D: DD 7E 02       LD      A,(IX+$02)      
59A0: 4F             LD      C,A             
59A1: 87             ADD     A,A             
59A2: 30 01          JR      NC,$59A5        
59A4: 24             INC     H               
59A5: 85             ADD     A,L             
59A6: 6F             LD      L,A             
59A7: 30 01          JR      NC,$59AA        
59A9: 24             INC     H               
59AA: 5E             LD      E,(HL)          
59AB: 23             INC     HL              
59AC: 56             LD      D,(HL)          
59AD: CB 23          SLA     E               
59AF: CB 12          RL      D               
59B1: 79             LD      A,C             
59B2: C6 C0          ADD     $C0             
59B4: 01 80 01       LD      BC,$0180        
59B7: 30 03          JR      NC,$59BC        
59B9: 01 80 FF       LD      BC,$FF80        
59BC: 09             ADD     HL,BC           
59BD: 46             LD      B,(HL)          
59BE: 2B             DEC     HL              
59BF: 4E             LD      C,(HL)          
59C0: CB 21          SLA     C               
59C2: CB 10          RL      B               
59C4: C9             RET                     
59C5: 21 D7 59       LD      HL,$59D7        
59C8: C3 A0 59       JP      $59A0           
59CB: 21 00 5C       LD      HL,$5C00        
59CE: C3 A0 59       JP      $59A0           
59D1: 21 00 5E       LD      HL,$5E00        
59D4: C3 A0 59       JP      $59A0           
59D7: CE 00          ADC     $00             
59D9: CD 00 CC       CALL    $CC00           
59DC: 00             NOP                     
59DD: CB 00          RLC     B               
59DF: CA 00 C9       JP      Z,$C900         
59E2: 00             NOP                     
59E3: C8             RET     Z               
59E4: 00             NOP                     
59E5: C8             RET     Z               
59E6: 00             NOP                     
59E7: C6 00          ADD     $00             
59E9: C4 00 C2       CALL    NZ,$C200        
59EC: 00             NOP                     
59ED: C0             RET     NZ              
59EE: 00             NOP                     
59EF: BF             CP      A               
59F0: 00             NOP                     
59F1: BC             CP      H               
59F2: 00             NOP                     
59F3: BA             CP      D               
59F4: 00             NOP                     
59F5: B9             CP      C               
59F6: 00             NOP                     
59F7: B6             OR      (HL)            
59F8: 00             NOP                     
59F9: B3             OR      E               
59FA: 00             NOP                     
59FB: B0             OR      B               
59FC: 00             NOP                     
59FD: AF             XOR     A               
59FE: 00             NOP                     
59FF: AC             XOR     H               
5A00: 00             NOP                     
5A01: A9             XOR     C               
5A02: 00             NOP                     
5A03: A8             XOR     B               
5A04: 00             NOP                     
5A05: A5             AND     L               
5A06: 00             NOP                     
5A07: A2             AND     D               
5A08: 00             NOP                     
5A09: A1             AND     C               
5A0A: 00             NOP                     
5A0B: 9E             SBC     (HL)            
5A0C: 00             NOP                     
5A0D: 9B             SBC     E               
5A0E: 00             NOP                     
5A0F: 98             SBC     B               
5A10: 00             NOP                     
5A11: 97             SUB     A               
5A12: 00             NOP                     
5A13: 94             SUB     H               
5A14: 00             NOP                     
5A15: 91             SUB     C               
5A16: 00             NOP                     
5A17: 90             SUB     B               
5A18: 00             NOP                     
5A19: 8D             ADC     A,L             
5A1A: 00             NOP                     
5A1B: 89             ADC     A,C             
5A1C: 00             NOP                     
5A1D: 88             ADC     A,B             
5A1E: 00             NOP                     
5A1F: 85             ADD     A,L             
5A20: 00             NOP                     
5A21: 81             ADD     A,C             
5A22: 00             NOP                     
5A23: 7F             LD      A,A             
5A24: 00             NOP                     
5A25: 7B             LD      A,E             
5A26: 00             NOP                     
5A27: 78             LD      A,B             
5A28: 00             NOP                     
5A29: 76             HALT                    
5A2A: 00             NOP                     
5A2B: 70             LD      (HL),B          
5A2C: 00             NOP                     
5A2D: 6D             LD      L,L             
5A2E: 00             NOP                     
5A2F: 68             LD      L,B             
5A30: 00             NOP                     
5A31: 63             LD      H,E             
5A32: 00             NOP                     
5A33: 60             LD      H,B             
5A34: 00             NOP                     
5A35: 5C             LD      E,H             
5A36: 00             NOP                     
5A37: 58             LD      E,B             
5A38: 00             NOP                     
5A39: 52             LD      D,D             
5A3A: 00             NOP                     
5A3B: 4E             LD      C,(HL)          
5A3C: 00             NOP                     
5A3D: 49             LD      C,C             
5A3E: 00             NOP                     
5A3F: 43             LD      B,E             
5A40: 00             NOP                     
5A41: 3E 00          LD      A,$00           
5A43: 39             ADD     HL,SP           
5A44: 00             NOP                     
5A45: 32 00 2C       LD      ($2C00),A       
5A48: 00             NOP                     
5A49: 27             DAA                     
5A4A: 00             NOP                     
5A4B: 20 00          JR      NZ,$5A4D        
5A4D: 1A             LD      A,(DE)          
5A4E: 00             NOP                     
5A4F: 14             INC     D               
5A50: 00             NOP                     
5A51: 0E 00          LD      C,$00           
5A53: 08             EX      AF,AF'          
5A54: 00             NOP                     
5A55: 00             NOP                     
5A56: 00             NOP                     
5A57: 00             NOP                     
5A58: 00             NOP                     
5A59: F8             RET     M               
5A5A: FF             RST     0X38            
5A5B: F2 FF 00       JP      P,$00FF         
5A5E: 00             NOP                     
5A5F: E6 FF          AND     $FF             
5A61: E0             RET     PO              
5A62: FF             RST     0X38            
5A63: D9             EXX                     
5A64: FF             RST     0X38            
5A65: D4 FF CE       CALL    NC,$CEFF        
5A68: FF             RST     0X38            
5A69: C7             RST     0X00            
5A6A: FF             RST     0X38            
5A6B: C2 FF BD       JP      NZ,$BDFF        
5A6E: FF             RST     0X38            
5A6F: B7             OR      A               
5A70: FF             RST     0X38            
5A71: B2             OR      D               
5A72: FF             RST     0X38            
5A73: AE             XOR     (HL)            
5A74: FF             RST     0X38            
5A75: A8             XOR     B               
5A76: FF             RST     0X38            
5A77: A4             AND     H               
5A78: FF             RST     0X38            
5A79: A0             AND     B               
5A7A: FF             RST     0X38            
5A7B: 9D             SBC     L               
5A7C: FF             RST     0X38            
5A7D: A0             AND     B               
5A7E: FF             RST     0X38            
5A7F: 93             SUB     E               
5A80: FF             RST     0X38            
5A81: 90             SUB     B               
5A82: FF             RST     0X38            
5A83: 8A             ADC     A,D             
5A84: FF             RST     0X38            
5A85: 88             ADC     A,B             
5A86: FF             RST     0X38            
5A87: 85             ADD     A,L             
5A88: FF             RST     0X38            
5A89: 81             ADD     A,C             
5A8A: FF             RST     0X38            
5A8B: 7F             LD      A,A             
5A8C: FF             RST     0X38            
5A8D: 7B             LD      A,E             
5A8E: FF             RST     0X38            
5A8F: 78             LD      A,B             
5A90: FF             RST     0X38            
5A91: 77             LD      (HL),A          
5A92: FF             RST     0X38            
5A93: 73             LD      (HL),E          
5A94: FF             RST     0X38            
5A95: 70             LD      (HL),B          
5A96: FF             RST     0X38            
5A97: 6F             LD      L,A             
5A98: FF             RST     0X38            
5A99: 6C             LD      L,H             
5A9A: FF             RST     0X38            
5A9B: 69             LD      L,C             
5A9C: FF             RST     0X38            
5A9D: 69             LD      L,C             
5A9E: FF             RST     0X38            
5A9F: 65             LD      H,L             
5AA0: FF             RST     0X38            
5AA1: 62             LD      H,D             
5AA2: FF             RST     0X38            
5AA3: 5F             LD      E,A             
5AA4: FF             RST     0X38            
5AA5: 5E             LD      E,(HL)          
5AA6: FF             RST     0X38            
5AA7: 5B             LD      E,E             
5AA8: FF             RST     0X38            
5AA9: 58             LD      E,B             
5AAA: FF             RST     0X38            
5AAB: 57             LD      D,A             
5AAC: FF             RST     0X38            
5AAD: 54             LD      D,H             
5AAE: FF             RST     0X38            
5AAF: 51             LD      D,C             
5AB0: FF             RST     0X38            
5AB1: 50             LD      D,B             
5AB2: FF             RST     0X38            
5AB3: 4D             LD      C,L             
5AB4: FF             RST     0X38            
5AB5: 4A             LD      C,D             
5AB6: FF             RST     0X38            
5AB7: 47             LD      B,A             
5AB8: FF             RST     0X38            
5AB9: 46             LD      B,(HL)          
5ABA: FF             RST     0X38            
5ABB: 44             LD      B,H             
5ABC: FF             RST     0X38            
5ABD: 41             LD      B,C             
5ABE: FF             RST     0X38            
5ABF: 40             LD      B,B             
5AC0: FF             RST     0X38            
5AC1: 3E FF          LD      A,$FF           
5AC3: 3C             INC     A               
5AC4: FF             RST     0X38            
5AC5: 3A FF 38       LD      A,($38FF)       
5AC8: FF             RST     0X38            
5AC9: 38 FF          JR      C,$5ACA         
5ACB: 37             SCF                     
5ACC: FF             RST     0X38            
5ACD: 36 FF          LD      (HL),$FF        
5ACF: 35             DEC     (HL)            
5AD0: FF             RST     0X38            
5AD1: 34             INC     (HL)            
5AD2: FF             RST     0X38            
5AD3: 33             INC     SP              
5AD4: FF             RST     0X38            
5AD5: 32 FF 32       LD      ($32FF),A       
5AD8: FF             RST     0X38            
5AD9: 33             INC     SP              
5ADA: FF             RST     0X38            
5ADB: 34             INC     (HL)            
5ADC: FF             RST     0X38            
5ADD: 35             DEC     (HL)            
5ADE: FF             RST     0X38            
5ADF: 36 FF          LD      (HL),$FF        
5AE1: 37             SCF                     
5AE2: FF             RST     0X38            
5AE3: 38 FF          JR      C,$5AE4         
5AE5: 38 FF          JR      C,$5AE6         
5AE7: 3A FF 3C       LD      A,($3CFF)       
5AEA: FF             RST     0X38            
5AEB: 3E FF          LD      A,$FF           
5AED: 40             LD      B,B             
5AEE: FF             RST     0X38            
5AEF: 41             LD      B,C             
5AF0: FF             RST     0X38            
5AF1: 44             LD      B,H             
5AF2: FF             RST     0X38            
5AF3: 46             LD      B,(HL)          
5AF4: FF             RST     0X38            
5AF5: 47             LD      B,A             
5AF6: FF             RST     0X38            
5AF7: 4A             LD      C,D             
5AF8: FF             RST     0X38            
5AF9: 4D             LD      C,L             
5AFA: FF             RST     0X38            
5AFB: 50             LD      D,B             
5AFC: FF             RST     0X38            
5AFD: 51             LD      D,C             
5AFE: FF             RST     0X38            
5AFF: 54             LD      D,H             
5B00: FF             RST     0X38            
5B01: 57             LD      D,A             
5B02: FF             RST     0X38            
5B03: 58             LD      E,B             
5B04: FF             RST     0X38            
5B05: 5B             LD      E,E             
5B06: FF             RST     0X38            
5B07: 5E             LD      E,(HL)          
5B08: FF             RST     0X38            
5B09: 5F             LD      E,A             
5B0A: FF             RST     0X38            
5B0B: 62             LD      H,D             
5B0C: FF             RST     0X38            
5B0D: 65             LD      H,L             
5B0E: FF             RST     0X38            
5B0F: 68             LD      L,B             
5B10: FF             RST     0X38            
5B11: 69             LD      L,C             
5B12: FF             RST     0X38            
5B13: 6C             LD      L,H             
5B14: FF             RST     0X38            
5B15: 6F             LD      L,A             
5B16: FF             RST     0X38            
5B17: 70             LD      (HL),B          
5B18: FF             RST     0X38            
5B19: 73             LD      (HL),E          
5B1A: FF             RST     0X38            
5B1B: 77             LD      (HL),A          
5B1C: FF             RST     0X38            
5B1D: 78             LD      A,B             
5B1E: FF             RST     0X38            
5B1F: 7B             LD      A,E             
5B20: FF             RST     0X38            
5B21: 7F             LD      A,A             
5B22: FF             RST     0X38            
5B23: 81             ADD     A,C             
5B24: FF             RST     0X38            
5B25: 85             ADD     A,L             
5B26: FF             RST     0X38            
5B27: 88             ADC     A,B             
5B28: FF             RST     0X38            
5B29: 8A             ADC     A,D             
5B2A: FF             RST     0X38            
5B2B: 90             SUB     B               
5B2C: FF             RST     0X38            
5B2D: 93             SUB     E               
5B2E: FF             RST     0X38            
5B2F: 98             SBC     B               
5B30: FF             RST     0X38            
5B31: 9D             SBC     L               
5B32: FF             RST     0X38            
5B33: A0             AND     B               
5B34: FF             RST     0X38            
5B35: A4             AND     H               
5B36: FF             RST     0X38            
5B37: A8             XOR     B               
5B38: FF             RST     0X38            
5B39: AE             XOR     (HL)            
5B3A: FF             RST     0X38            
5B3B: B2             OR      D               
5B3C: FF             RST     0X38            
5B3D: B7             OR      A               
5B3E: FF             RST     0X38            
5B3F: BD             CP      L               
5B40: FF             RST     0X38            
5B41: C2 FF C7       JP      NZ,$C7FF        
5B44: FF             RST     0X38            
5B45: CE FF          ADC     $FF             
5B47: D4 FF D9       CALL    NC,$D9FF        
5B4A: FF             RST     0X38            
5B4B: E0             RET     PO              
5B4C: FF             RST     0X38            
5B4D: E6 FF          AND     $FF             
5B4F: EC FF F2       CALL    PE,$F2FF        
5B52: FF             RST     0X38            
5B53: F8             RET     M               
5B54: FF             RST     0X38            
5B55: 00             NOP                     
5B56: 00             NOP                     
5B57: 00             NOP                     
5B58: 00             NOP                     
5B59: 08             EX      AF,AF'          
5B5A: 00             NOP                     
5B5B: 0E 00          LD      C,$00           
5B5D: 14             INC     D               
5B5E: 00             NOP                     
5B5F: 1A             LD      A,(DE)          
5B60: 00             NOP                     
5B61: 20 00          JR      NZ,$5B63        
5B63: 27             DAA                     
5B64: 00             NOP                     
5B65: 2C             INC     L               
5B66: 00             NOP                     
5B67: 32 00 39       LD      ($3900),A       
5B6A: 00             NOP                     
5B6B: 3E 00          LD      A,$00           
5B6D: 43             LD      B,E             
5B6E: 00             NOP                     
5B6F: 49             LD      C,C             
5B70: 00             NOP                     
5B71: 4E             LD      C,(HL)          
5B72: 00             NOP                     
5B73: 52             LD      D,D             
5B74: 00             NOP                     
5B75: 58             LD      E,B             
5B76: 00             NOP                     
5B77: 5C             LD      E,H             
5B78: 00             NOP                     
5B79: 60             LD      H,B             
5B7A: 00             NOP                     
5B7B: 63             LD      H,E             
5B7C: 00             NOP                     
5B7D: 63             LD      H,E             
5B7E: 00             NOP                     
5B7F: 6D             LD      L,L             
5B80: 00             NOP                     
5B81: 70             LD      (HL),B          
5B82: 00             NOP                     
5B83: 76             HALT                    
5B84: 00             NOP                     
5B85: 78             LD      A,B             
5B86: 00             NOP                     
5B87: 7B             LD      A,E             
5B88: 00             NOP                     
5B89: 7F             LD      A,A             
5B8A: 00             NOP                     
5B8B: 81             ADD     A,C             
5B8C: 00             NOP                     
5B8D: 85             ADD     A,L             
5B8E: 00             NOP                     
5B8F: 88             ADC     A,B             
5B90: 00             NOP                     
5B91: 89             ADC     A,C             
5B92: 00             NOP                     
5B93: 8D             ADC     A,L             
5B94: 00             NOP                     
5B95: 90             SUB     B               
5B96: 00             NOP                     
5B97: 91             SUB     C               
5B98: 00             NOP                     
5B99: 94             SUB     H               
5B9A: 00             NOP                     
5B9B: 97             SUB     A               
5B9C: 00             NOP                     
5B9D: 94             SUB     H               
5B9E: 00             NOP                     
5B9F: 9B             SBC     E               
5BA0: 00             NOP                     
5BA1: 9E             SBC     (HL)            
5BA2: 00             NOP                     
5BA3: A1             AND     C               
5BA4: 00             NOP                     
5BA5: A2             AND     D               
5BA6: 00             NOP                     
5BA7: A5             AND     L               
5BA8: 00             NOP                     
5BA9: A8             XOR     B               
5BAA: 00             NOP                     
5BAB: A9             XOR     C               
5BAC: 00             NOP                     
5BAD: AC             XOR     H               
5BAE: 00             NOP                     
5BAF: AF             XOR     A               
5BB0: 00             NOP                     
5BB1: B0             OR      B               
5BB2: 00             NOP                     
5BB3: B3             OR      E               
5BB4: 00             NOP                     
5BB5: B6             OR      (HL)            
5BB6: 00             NOP                     
5BB7: B9             CP      C               
5BB8: 00             NOP                     
5BB9: BA             CP      D               
5BBA: 00             NOP                     
5BBB: BC             CP      H               
5BBC: 00             NOP                     
5BBD: B9             CP      C               
5BBE: 00             NOP                     
5BBF: C0             RET     NZ              
5BC0: 00             NOP                     
5BC1: C2 00 C4       JP      NZ,$C400        
5BC4: 00             NOP                     
5BC5: C6 00          ADD     $00             
5BC7: C8             RET     Z               
5BC8: 00             NOP                     
5BC9: C8             RET     Z               
5BCA: 00             NOP                     
5BCB: C9             RET                     
5BCC: 00             NOP                     
5BCD: CA 00 CB       JP      Z,$CB00         
5BD0: 00             NOP                     
5BD1: CC 00 CD       CALL    Z,$CD00         
5BD4: 00             NOP                     
5BD5: CE 00          ADC     $00             
5BD7: CD D2 07       CALL    $07D2           
5BDA: CD 01 02       CALL    $0201           
5BDD: C0             RET     NZ              
5BDE: 21 DD 0B       LD      HL,$0BDD        
5BE1: 97             SUB     A               
5BE2: 47             LD      B,A             
5BE3: AE             XOR     (HL)            
5BE4: 23             INC     HL              
5BE5: 10 FC          DJNZ    $5BE3           
5BE7: C6 E4          ADD     $E4             
5BE9: C4 11 0F       CALL    NZ,$0F11        
5BEC: 3A AB A9       LD      A,($A9AB)       
5BEF: 21 34 17       LD      HL,$1734        
5BF2: 06 14          LD      B,$14           
5BF4: 86             ADD     A,(HL)          
5BF5: 23             INC     HL              
5BF6: 10 FC          DJNZ    $5BF4           
5BF8: C6 77          ADD     $77             
5BFA: 32 AB A9       LD      ($A9AB),A       
5BFD: C3 1A 0F       JP      $0F1A           
5C00: E7             RST     0X20            
5C01: 00             NOP                     
5C02: E6 00          AND     $00             
5C04: E5             PUSH    HL              
5C05: 00             NOP                     
5C06: E4 00 E3       CALL    PO,$E300        
5C09: 00             NOP                     
5C0A: E2 00 E1       JP      PO,$E100        
5C0D: 00             NOP                     
5C0E: E0             RET     PO              
5C0F: 00             NOP                     
5C10: DE 00          SBC     $00             
5C12: DC 00 DA       CALL    C,$DA00         
5C15: 00             NOP                     
5C16: D8             RET     C               
5C17: 00             NOP                     
5C18: D6 00          SUB     $00             
5C1A: D3 00          OUT     ($00),A         
5C1C: D1             POP     DE              
5C1D: 00             NOP                     
5C1E: CF             RST     0X08            
5C1F: 00             NOP                     
5C20: CC 00 C9       CALL    Z,$C900         
5C23: 00             NOP                     
5C24: C6 00          ADD     $00             
5C26: C4 00 C1       CALL    NZ,$C100        
5C29: 00             NOP                     
5C2A: BE             CP      (HL)            
5C2B: 00             NOP                     
5C2C: BC             CP      H               
5C2D: 00             NOP                     
5C2E: B9             CP      C               
5C2F: 00             NOP                     
5C30: B6             OR      (HL)            
5C31: 00             NOP                     
5C32: B4             OR      H               
5C33: 00             NOP                     
5C34: B1             OR      C               
5C35: 00             NOP                     
5C36: AE             XOR     (HL)            
5C37: 00             NOP                     
5C38: AB             XOR     E               
5C39: 00             NOP                     
5C3A: A9             XOR     C               
5C3B: 00             NOP                     
5C3C: A6             AND     (HL)            
5C3D: 00             NOP                     
5C3E: A3             AND     E               
5C3F: 00             NOP                     
5C40: A1             AND     C               
5C41: 00             NOP                     
5C42: 9E             SBC     (HL)            
5C43: 00             NOP                     
5C44: 9A             SBC     D               
5C45: 00             NOP                     
5C46: 98             SBC     B               
5C47: 00             NOP                     
5C48: 95             SUB     L               
5C49: 00             NOP                     
5C4A: 91             SUB     C               
5C4B: 00             NOP                     
5C4C: 8E             ADC     A,(HL)          
5C4D: 00             NOP                     
5C4E: 8A             ADC     A,D             
5C4F: 00             NOP                     
5C50: 87             ADD     A,A             
5C51: 00             NOP                     
5C52: 84             ADD     A,H             
5C53: 00             NOP                     
5C54: 7E             LD      A,(HL)          
5C55: 00             NOP                     
5C56: 7A             LD      A,D             
5C57: 00             NOP                     
5C58: 75             LD      (HL),L          
5C59: 00             NOP                     
5C5A: 6F             LD      L,A             
5C5B: 00             NOP                     
5C5C: 6C             LD      L,H             
5C5D: 00             NOP                     
5C5E: 67             LD      H,A             
5C5F: 00             NOP                     
5C60: 62             LD      H,D             
5C61: 00             NOP                     
5C62: 5C             LD      E,H             
5C63: 00             NOP                     
5C64: 57             LD      D,A             
5C65: 00             NOP                     
5C66: 51             LD      D,C             
5C67: 00             NOP                     
5C68: 4B             LD      C,E             
5C69: 00             NOP                     
5C6A: 45             LD      B,L             
5C6B: 00             NOP                     
5C6C: 3F             CCF                     
5C6D: 00             NOP                     
5C6E: 38 00          JR      C,$5C70         
5C70: 31 00 2B       LD      SP,$2B00        
5C73: 00             NOP                     
5C74: 24             INC     H               
5C75: 00             NOP                     
5C76: 1D             DEC     E               
5C77: 00             NOP                     
5C78: 16 00          LD      D,$00           
5C7A: 0F             RRCA                    
5C7B: 00             NOP                     
5C7C: 08             EX      AF,AF'          
5C7D: 00             NOP                     
5C7E: 00             NOP                     
5C7F: 00             NOP                     
5C80: 00             NOP                     
5C81: 00             NOP                     
5C82: F8             RET     M               
5C83: FF             RST     0X38            
5C84: F1             POP     AF              
5C85: FF             RST     0X38            
5C86: 00             NOP                     
5C87: 00             NOP                     
5C88: E3             EX      (SP),HL         
5C89: FF             RST     0X38            
5C8A: DC FF D5       CALL    C,$D5FF         
5C8D: FF             RST     0X38            
5C8E: CF             RST     0X08            
5C8F: FF             RST     0X38            
5C90: C8             RET     Z               
5C91: FF             RST     0X38            
5C92: C1             POP     BC              
5C93: FF             RST     0X38            
5C94: BB             CP      E               
5C95: FF             RST     0X38            
5C96: B5             OR      L               
5C97: FF             RST     0X38            
5C98: AF             XOR     A               
5C99: FF             RST     0X38            
5C9A: A9             XOR     C               
5C9B: FF             RST     0X38            
5C9C: A4             AND     H               
5C9D: FF             RST     0X38            
5C9E: 9E             SBC     (HL)            
5C9F: FF             RST     0X38            
5CA0: 99             SBC     C               
5CA1: FF             RST     0X38            
5CA2: 94             SUB     H               
5CA3: FF             RST     0X38            
5CA4: 91             SUB     C               
5CA5: FF             RST     0X38            
5CA6: 94             SUB     H               
5CA7: FF             RST     0X38            
5CA8: 86             ADD     A,(HL)          
5CA9: FF             RST     0X38            
5CAA: 82             ADD     A,D             
5CAB: FF             RST     0X38            
5CAC: 7C             LD      A,H             
5CAD: FF             RST     0X38            
5CAE: 79             LD      A,C             
5CAF: FF             RST     0X38            
5CB0: 76             HALT                    
5CB1: FF             RST     0X38            
5CB2: 72             LD      (HL),D          
5CB3: FF             RST     0X38            
5CB4: 6F             LD      L,A             
5CB5: FF             RST     0X38            
5CB6: 6B             LD      L,E             
5CB7: FF             RST     0X38            
5CB8: 68             LD      L,B             
5CB9: FF             RST     0X38            
5CBA: 66             LD      H,(HL)          
5CBB: FF             RST     0X38            
5CBC: 62             LD      H,D             
5CBD: FF             RST     0X38            
5CBE: 5F             LD      E,A             
5CBF: FF             RST     0X38            
5CC0: 5D             LD      E,L             
5CC1: FF             RST     0X38            
5CC2: 5A             LD      E,D             
5CC3: FF             RST     0X38            
5CC4: 57             LD      D,A             
5CC5: FF             RST     0X38            
5CC6: 57             LD      D,A             
5CC7: FF             RST     0X38            
5CC8: 52             LD      D,D             
5CC9: FF             RST     0X38            
5CCA: 4F             LD      C,A             
5CCB: FF             RST     0X38            
5CCC: 4C             LD      C,H             
5CCD: FF             RST     0X38            
5CCE: 4A             LD      C,D             
5CCF: FF             RST     0X38            
5CD0: 47             LD      B,A             
5CD1: FF             RST     0X38            
5CD2: 44             LD      B,H             
5CD3: FF             RST     0X38            
5CD4: 42             LD      B,D             
5CD5: FF             RST     0X38            
5CD6: 3F             CCF                     
5CD7: FF             RST     0X38            
5CD8: 3C             INC     A               
5CD9: FF             RST     0X38            
5CDA: 3A FF 37       LD      A,($37FF)       
5CDD: FF             RST     0X38            
5CDE: 34             INC     (HL)            
5CDF: FF             RST     0X38            
5CE0: 31 FF 2F       LD      SP,$2FFF        
5CE3: FF             RST     0X38            
5CE4: 2D             DEC     L               
5CE5: FF             RST     0X38            
5CE6: 2A FF 28       LD      HL,($28FF)      
5CE9: FF             RST     0X38            
5CEA: 26 FF          LD      H,$FF           
5CEC: 24             INC     H               
5CED: FF             RST     0X38            
5CEE: 22 FF 20       LD      ($20FF),HL      
5CF1: FF             RST     0X38            
5CF2: 1F             RRA                     
5CF3: FF             RST     0X38            
5CF4: 1E FF          LD      E,$FF           
5CF6: 1D             DEC     E               
5CF7: FF             RST     0X38            
5CF8: 1C             INC     E               
5CF9: FF             RST     0X38            
5CFA: 1B             DEC     DE              
5CFB: FF             RST     0X38            
5CFC: 1A             LD      A,(DE)          
5CFD: FF             RST     0X38            
5CFE: 19             ADD     HL,DE           
5CFF: FF             RST     0X38            
5D00: 19             ADD     HL,DE           
5D01: FF             RST     0X38            
5D02: 1A             LD      A,(DE)          
5D03: FF             RST     0X38            
5D04: 1B             DEC     DE              
5D05: FF             RST     0X38            
5D06: 1C             INC     E               
5D07: FF             RST     0X38            
5D08: 1D             DEC     E               
5D09: FF             RST     0X38            
5D0A: 1E FF          LD      E,$FF           
5D0C: 1F             RRA                     
5D0D: FF             RST     0X38            
5D0E: 20 FF          JR      NZ,$5D0F        
5D10: 22 FF 24       LD      ($24FF),HL      
5D13: FF             RST     0X38            
5D14: 26 FF          LD      H,$FF           
5D16: 28 FF          JR      Z,$5D17         
5D18: 2A FF 2D       LD      HL,($2DFF)      
5D1B: FF             RST     0X38            
5D1C: 2F             CPL                     
5D1D: FF             RST     0X38            
5D1E: 31 FF 34       LD      SP,$34FF        
5D21: FF             RST     0X38            
5D22: 37             SCF                     
5D23: FF             RST     0X38            
5D24: 3A FF 3C       LD      A,($3CFF)       
5D27: FF             RST     0X38            
5D28: 3F             CCF                     
5D29: FF             RST     0X38            
5D2A: 42             LD      B,D             
5D2B: FF             RST     0X38            
5D2C: 44             LD      B,H             
5D2D: FF             RST     0X38            
5D2E: 47             LD      B,A             
5D2F: FF             RST     0X38            
5D30: 4A             LD      C,D             
5D31: FF             RST     0X38            
5D32: 4C             LD      C,H             
5D33: FF             RST     0X38            
5D34: 4F             LD      C,A             
5D35: FF             RST     0X38            
5D36: 52             LD      D,D             
5D37: FF             RST     0X38            
5D38: 55             LD      D,L             
5D39: FF             RST     0X38            
5D3A: 57             LD      D,A             
5D3B: FF             RST     0X38            
5D3C: 5A             LD      E,D             
5D3D: FF             RST     0X38            
5D3E: 5D             LD      E,L             
5D3F: FF             RST     0X38            
5D40: 5F             LD      E,A             
5D41: FF             RST     0X38            
5D42: 62             LD      H,D             
5D43: FF             RST     0X38            
5D44: 66             LD      H,(HL)          
5D45: FF             RST     0X38            
5D46: 68             LD      L,B             
5D47: FF             RST     0X38            
5D48: 6B             LD      L,E             
5D49: FF             RST     0X38            
5D4A: 6F             LD      L,A             
5D4B: FF             RST     0X38            
5D4C: 72             LD      (HL),D          
5D4D: FF             RST     0X38            
5D4E: 76             HALT                    
5D4F: FF             RST     0X38            
5D50: 79             LD      A,C             
5D51: FF             RST     0X38            
5D52: 7C             LD      A,H             
5D53: FF             RST     0X38            
5D54: 82             ADD     A,D             
5D55: FF             RST     0X38            
5D56: 86             ADD     A,(HL)          
5D57: FF             RST     0X38            
5D58: 8B             ADC     A,E             
5D59: FF             RST     0X38            
5D5A: 91             SUB     C               
5D5B: FF             RST     0X38            
5D5C: 94             SUB     H               
5D5D: FF             RST     0X38            
5D5E: 99             SBC     C               
5D5F: FF             RST     0X38            
5D60: 9E             SBC     (HL)            
5D61: FF             RST     0X38            
5D62: A4             AND     H               
5D63: FF             RST     0X38            
5D64: A9             XOR     C               
5D65: FF             RST     0X38            
5D66: AF             XOR     A               
5D67: FF             RST     0X38            
5D68: B5             OR      L               
5D69: FF             RST     0X38            
5D6A: BB             CP      E               
5D6B: FF             RST     0X38            
5D6C: C1             POP     BC              
5D6D: FF             RST     0X38            
5D6E: C8             RET     Z               
5D6F: FF             RST     0X38            
5D70: CF             RST     0X08            
5D71: FF             RST     0X38            
5D72: D5             PUSH    DE              
5D73: FF             RST     0X38            
5D74: DC FF E3       CALL    C,$E3FF         
5D77: FF             RST     0X38            
5D78: EA FF F1       JP      PE,$F1FF        
5D7B: FF             RST     0X38            
5D7C: F8             RET     M               
5D7D: FF             RST     0X38            
5D7E: 00             NOP                     
5D7F: 00             NOP                     
5D80: 00             NOP                     
5D81: 00             NOP                     
5D82: 08             EX      AF,AF'          
5D83: 00             NOP                     
5D84: 0F             RRCA                    
5D85: 00             NOP                     
5D86: 16 00          LD      D,$00           
5D88: 1D             DEC     E               
5D89: 00             NOP                     
5D8A: 24             INC     H               
5D8B: 00             NOP                     
5D8C: 2B             DEC     HL              
5D8D: 00             NOP                     
5D8E: 31 00 38       LD      SP,$3800        
5D91: 00             NOP                     
5D92: 3F             CCF                     
5D93: 00             NOP                     
5D94: 45             LD      B,L             
5D95: 00             NOP                     
5D96: 4B             LD      C,E             
5D97: 00             NOP                     
5D98: 51             LD      D,C             
5D99: 00             NOP                     
5D9A: 57             LD      D,A             
5D9B: 00             NOP                     
5D9C: 5C             LD      E,H             
5D9D: 00             NOP                     
5D9E: 62             LD      H,D             
5D9F: 00             NOP                     
5DA0: 67             LD      H,A             
5DA1: 00             NOP                     
5DA2: 6C             LD      L,H             
5DA3: 00             NOP                     
5DA4: 6F             LD      L,A             
5DA5: 00             NOP                     
5DA6: 6F             LD      L,A             
5DA7: 00             NOP                     
5DA8: 7A             LD      A,D             
5DA9: 00             NOP                     
5DAA: 7E             LD      A,(HL)          
5DAB: 00             NOP                     
5DAC: 84             ADD     A,H             
5DAD: 00             NOP                     
5DAE: 87             ADD     A,A             
5DAF: 00             NOP                     
5DB0: 8A             ADC     A,D             
5DB1: 00             NOP                     
5DB2: 8E             ADC     A,(HL)          
5DB3: 00             NOP                     
5DB4: 91             SUB     C               
5DB5: 00             NOP                     
5DB6: 95             SUB     L               
5DB7: 00             NOP                     
5DB8: 98             SBC     B               
5DB9: 00             NOP                     
5DBA: 9A             SBC     D               
5DBB: 00             NOP                     
5DBC: 9E             SBC     (HL)            
5DBD: 00             NOP                     
5DBE: A1             AND     C               
5DBF: 00             NOP                     
5DC0: A3             AND     E               
5DC1: 00             NOP                     
5DC2: A6             AND     (HL)            
5DC3: 00             NOP                     
5DC4: A9             XOR     C               
5DC5: 00             NOP                     
5DC6: A6             AND     (HL)            
5DC7: 00             NOP                     
5DC8: AE             XOR     (HL)            
5DC9: 00             NOP                     
5DCA: B1             OR      C               
5DCB: 00             NOP                     
5DCC: B4             OR      H               
5DCD: 00             NOP                     
5DCE: B6             OR      (HL)            
5DCF: 00             NOP                     
5DD0: B9             CP      C               
5DD1: 00             NOP                     
5DD2: BC             CP      H               
5DD3: 00             NOP                     
5DD4: BE             CP      (HL)            
5DD5: 00             NOP                     
5DD6: C1             POP     BC              
5DD7: 00             NOP                     
5DD8: C4 00 C6       CALL    NZ,$C600        
5DDB: 00             NOP                     
5DDC: C9             RET                     
5DDD: 00             NOP                     
5DDE: CC 00 CF       CALL    Z,$CF00         
5DE1: 00             NOP                     
5DE2: D1             POP     DE              
5DE3: 00             NOP                     
5DE4: D3 00          OUT     ($00),A         
5DE6: CF             RST     0X08            
5DE7: 00             NOP                     
5DE8: D8             RET     C               
5DE9: 00             NOP                     
5DEA: DA 00 DC       JP      C,$DC00         
5DED: 00             NOP                     
5DEE: DE 00          SBC     $00             
5DF0: E0             RET     PO              
5DF1: 00             NOP                     
5DF2: E1             POP     HL              
5DF3: 00             NOP                     
5DF4: E2 00 E3       JP      PO,$E300        
5DF7: 00             NOP                     
5DF8: E4 00 E5       CALL    PO,$E500        
5DFB: 00             NOP                     
5DFC: E6 00          AND     $00             
5DFE: E7             RST     0X20            
5DFF: 00             NOP                     
5E00: 00             NOP                     
5E01: 01 FF 00       LD      BC,$00FF        
5E04: FE 00          CP      $00             
5E06: FD                                  
5E07: 00             NOP                     
5E08: FC 00 FB       CALL    M,$FB00         
5E0B: 00             NOP                     
5E0C: FA 00 F8       JP      M,$F800         
5E0F: 00             NOP                     
5E10: F6 00          OR      $00             
5E12: F4 00 F2       CALL    P,$F200         
5E15: 00             NOP                     
5E16: F0             RET     P               
5E17: 00             NOP                     
5E18: ED                                  
5E19: 00             NOP                     
5E1A: EA 00 E8       JP      PE,$E800        
5E1D: 00             NOP                     
5E1E: E5             PUSH    HL              
5E1F: 00             NOP                     
5E20: E2 00 DF       JP      PO,$DF00        
5E23: 00             NOP                     
5E24: DC 00 D9       CALL    C,$D900         
5E27: 00             NOP                     
5E28: D6 00          SUB     $00             
5E2A: D3 00          OUT     ($00),A         
5E2C: D0             RET     NC              
5E2D: 00             NOP                     
5E2E: CD 00 CA       CALL    $CA00           
5E31: 00             NOP                     
5E32: C7             RST     0X00            
5E33: 00             NOP                     
5E34: C4 00 C1       CALL    NZ,$C100        
5E37: 00             NOP                     
5E38: BE             CP      (HL)            
5E39: 00             NOP                     
5E3A: BB             CP      E               
5E3B: 00             NOP                     
5E3C: B8             CP      B               
5E3D: 00             NOP                     
5E3E: B5             OR      L               
5E3F: 00             NOP                     
5E40: B2             OR      D               
5E41: 00             NOP                     
5E42: AF             XOR     A               
5E43: 00             NOP                     
5E44: AB             XOR     E               
5E45: 00             NOP                     
5E46: A8             XOR     B               
5E47: 00             NOP                     
5E48: A5             AND     L               
5E49: 00             NOP                     
5E4A: A1             AND     C               
5E4B: 00             NOP                     
5E4C: 9D             SBC     L               
5E4D: 00             NOP                     
5E4E: 99             SBC     C               
5E4F: 00             NOP                     
5E50: 96             SUB     (HL)            
5E51: 00             NOP                     
5E52: 92             SUB     D               
5E53: 00             NOP                     
5E54: 8C             ADC     A,H             
5E55: 00             NOP                     
5E56: 87             ADD     A,A             
5E57: 00             NOP                     
5E58: 82             ADD     A,D             
5E59: 00             NOP                     
5E5A: 7B             LD      A,E             
5E5B: 00             NOP                     
5E5C: 78             LD      A,B             
5E5D: 00             NOP                     
5E5E: 72             LD      (HL),D          
5E5F: 00             NOP                     
5E60: 6C             LD      L,H             
5E61: 00             NOP                     
5E62: 66             LD      H,(HL)          
5E63: 00             NOP                     
5E64: 60             LD      H,B             
5E65: 00             NOP                     
5E66: 59             LD      E,C             
5E67: 00             NOP                     
5E68: 53             LD      D,E             
5E69: 00             NOP                     
5E6A: 4C             LD      C,H             
5E6B: 00             NOP                     
5E6C: 45             LD      B,L             
5E6D: 00             NOP                     
5E6E: 3E 00          LD      A,$00           
5E70: 36 00          LD      (HL),$00        
5E72: 2F             CPL                     
5E73: 00             NOP                     
5E74: 28 00          JR      Z,$5E76         
5E76: 20 00          JR      NZ,$5E78        
5E78: 18 00          JR      $5E7A           
5E7A: 10 00          DJNZ    $5E7C           
5E7C: 08             EX      AF,AF'          
5E7D: 00             NOP                     
5E7E: 00             NOP                     
5E7F: 00             NOP                     
5E80: 00             NOP                     
5E81: 00             NOP                     
5E82: F8             RET     M               
5E83: FF             RST     0X38            
5E84: F0             RET     P               
5E85: FF             RST     0X38            
5E86: 00             NOP                     
5E87: 00             NOP                     
5E88: E0             RET     PO              
5E89: FF             RST     0X38            
5E8A: D8             RET     C               
5E8B: FF             RST     0X38            
5E8C: D1             POP     DE              
5E8D: FF             RST     0X38            
5E8E: CA FF C2       JP      Z,$C2FF         
5E91: FF             RST     0X38            
5E92: BB             CP      E               
5E93: FF             RST     0X38            
5E94: B4             OR      H               
5E95: FF             RST     0X38            
5E96: AD             XOR     L               
5E97: FF             RST     0X38            
5E98: A7             AND     A               
5E99: FF             RST     0X38            
5E9A: A0             AND     B               
5E9B: FF             RST     0X38            
5E9C: 9A             SBC     D               
5E9D: FF             RST     0X38            
5E9E: 94             SUB     H               
5E9F: FF             RST     0X38            
5EA0: 8E             ADC     A,(HL)          
5EA1: FF             RST     0X38            
5EA2: 88             ADC     A,B             
5EA3: FF             RST     0X38            
5EA4: 85             ADD     A,L             
5EA5: FF             RST     0X38            
5EA6: 88             ADC     A,B             
5EA7: FF             RST     0X38            
5EA8: 79             LD      A,C             
5EA9: FF             RST     0X38            
5EAA: 74             LD      (HL),H          
5EAB: FF             RST     0X38            
5EAC: 6E             LD      L,(HL)          
5EAD: FF             RST     0X38            
5EAE: 6A             LD      L,D             
5EAF: FF             RST     0X38            
5EB0: 67             LD      H,A             
5EB1: FF             RST     0X38            
5EB2: 63             LD      H,E             
5EB3: FF             RST     0X38            
5EB4: 5F             LD      E,A             
5EB5: FF             RST     0X38            
5EB6: 5B             LD      E,E             
5EB7: FF             RST     0X38            
5EB8: 58             LD      E,B             
5EB9: FF             RST     0X38            
5EBA: 55             LD      D,L             
5EBB: FF             RST     0X38            
5EBC: 51             LD      D,C             
5EBD: FF             RST     0X38            
5EBE: 4E             LD      C,(HL)          
5EBF: FF             RST     0X38            
5EC0: 4B             LD      C,E             
5EC1: FF             RST     0X38            
5EC2: 48             LD      C,B             
5EC3: FF             RST     0X38            
5EC4: 45             LD      B,L             
5EC5: FF             RST     0X38            
5EC6: 45             LD      B,L             
5EC7: FF             RST     0X38            
5EC8: 3F             CCF                     
5EC9: FF             RST     0X38            
5ECA: 3C             INC     A               
5ECB: FF             RST     0X38            
5ECC: 39             ADD     HL,SP           
5ECD: FF             RST     0X38            
5ECE: 36 FF          LD      (HL),$FF        
5ED0: 33             INC     SP              
5ED1: FF             RST     0X38            
5ED2: 30 FF          JR      NC,$5ED3        
5ED4: 2D             DEC     L               
5ED5: FF             RST     0X38            
5ED6: 2A FF 27       LD      HL,($27FF)      
5ED9: FF             RST     0X38            
5EDA: 24             INC     H               
5EDB: FF             RST     0X38            
5EDC: 21 FF 1E       LD      HL,$1EFF        
5EDF: FF             RST     0X38            
5EE0: 1B             DEC     DE              
5EE1: FF             RST     0X38            
5EE2: 18 FF          JR      $5EE3           
5EE4: 16 FF          LD      D,$FF           
5EE6: 13             INC     DE              
5EE7: FF             RST     0X38            
5EE8: 10 FF          DJNZ    $5EE9           
5EEA: 0E FF          LD      C,$FF           
5EEC: 0C             INC     C               
5EED: FF             RST     0X38            
5EEE: 0A             LD      A,(BC)          
5EEF: FF             RST     0X38            
5EF0: 08             EX      AF,AF'          
5EF1: FF             RST     0X38            
5EF2: 06 FF          LD      B,$FF           
5EF4: 05             DEC     B               
5EF5: FF             RST     0X38            
5EF6: 04             INC     B               
5EF7: FF             RST     0X38            
5EF8: 03             INC     BC              
5EF9: FF             RST     0X38            
5EFA: 02             LD      (BC),A          
5EFB: FF             RST     0X38            
5EFC: 01 FF 00       LD      BC,$00FF        
5EFF: FF             RST     0X38            
5F00: 00             NOP                     
5F01: FF             RST     0X38            
5F02: 01 FF 02       LD      BC,$02FF        
5F05: FF             RST     0X38            
5F06: 03             INC     BC              
5F07: FF             RST     0X38            
5F08: 04             INC     B               
5F09: FF             RST     0X38            
5F0A: 05             DEC     B               
5F0B: FF             RST     0X38            
5F0C: 06 FF          LD      B,$FF           
5F0E: 08             EX      AF,AF'          
5F0F: FF             RST     0X38            
5F10: 0A             LD      A,(BC)          
5F11: FF             RST     0X38            
5F12: 0C             INC     C               
5F13: FF             RST     0X38            
5F14: 0E FF          LD      C,$FF           
5F16: 10 FF          DJNZ    $5F17           
5F18: 13             INC     DE              
5F19: FF             RST     0X38            
5F1A: 16 FF          LD      D,$FF           
5F1C: 18 FF          JR      $5F1D           
5F1E: 1B             DEC     DE              
5F1F: FF             RST     0X38            
5F20: 1E FF          LD      E,$FF           
5F22: 21 FF 24       LD      HL,$24FF        
5F25: FF             RST     0X38            
5F26: 27             DAA                     
5F27: FF             RST     0X38            
5F28: 2A FF 2D       LD      HL,($2DFF)      
5F2B: FF             RST     0X38            
5F2C: 30 FF          JR      NC,$5F2D        
5F2E: 33             INC     SP              
5F2F: FF             RST     0X38            
5F30: 36 FF          LD      (HL),$FF        
5F32: 39             ADD     HL,SP           
5F33: FF             RST     0X38            
5F34: 3C             INC     A               
5F35: FF             RST     0X38            
5F36: 3F             CCF                     
5F37: FF             RST     0X38            
5F38: 42             LD      B,D             
5F39: FF             RST     0X38            
5F3A: 45             LD      B,L             
5F3B: FF             RST     0X38            
5F3C: 48             LD      C,B             
5F3D: FF             RST     0X38            
5F3E: 4B             LD      C,E             
5F3F: FF             RST     0X38            
5F40: 4E             LD      C,(HL)          
5F41: FF             RST     0X38            
5F42: 51             LD      D,C             
5F43: FF             RST     0X38            
5F44: 55             LD      D,L             
5F45: FF             RST     0X38            
5F46: 58             LD      E,B             
5F47: FF             RST     0X38            
5F48: 5B             LD      E,E             
5F49: FF             RST     0X38            
5F4A: 5F             LD      E,A             
5F4B: FF             RST     0X38            
5F4C: 63             LD      H,E             
5F4D: FF             RST     0X38            
5F4E: 67             LD      H,A             
5F4F: FF             RST     0X38            
5F50: 6A             LD      L,D             
5F51: FF             RST     0X38            
5F52: 6E             LD      L,(HL)          
5F53: FF             RST     0X38            
5F54: 74             LD      (HL),H          
5F55: FF             RST     0X38            
5F56: 79             LD      A,C             
5F57: FF             RST     0X38            
5F58: 7E             LD      A,(HL)          
5F59: FF             RST     0X38            
5F5A: 85             ADD     A,L             
5F5B: FF             RST     0X38            
5F5C: 88             ADC     A,B             
5F5D: FF             RST     0X38            
5F5E: 8E             ADC     A,(HL)          
5F5F: FF             RST     0X38            
5F60: 94             SUB     H               
5F61: FF             RST     0X38            
5F62: 9A             SBC     D               
5F63: FF             RST     0X38            
5F64: A0             AND     B               
5F65: FF             RST     0X38            
5F66: A7             AND     A               
5F67: FF             RST     0X38            
5F68: AD             XOR     L               
5F69: FF             RST     0X38            
5F6A: B4             OR      H               
5F6B: FF             RST     0X38            
5F6C: BB             CP      E               
5F6D: FF             RST     0X38            
5F6E: C2 FF CA       JP      NZ,$CAFF        
5F71: FF             RST     0X38            
5F72: D1             POP     DE              
5F73: FF             RST     0X38            
5F74: D8             RET     C               
5F75: FF             RST     0X38            
5F76: E0             RET     PO              
5F77: FF             RST     0X38            
5F78: E8             RET     PE              
5F79: FF             RST     0X38            
5F7A: F0             RET     P               
5F7B: FF             RST     0X38            
5F7C: F8             RET     M               
5F7D: FF             RST     0X38            
5F7E: 00             NOP                     
5F7F: 00             NOP                     
5F80: 00             NOP                     
5F81: 00             NOP                     
5F82: 08             EX      AF,AF'          
5F83: 00             NOP                     
5F84: 10 00          DJNZ    $5F86           
5F86: 18 00          JR      $5F88           
5F88: 20 00          JR      NZ,$5F8A        
5F8A: 28 00          JR      Z,$5F8C         
5F8C: 2F             CPL                     
5F8D: 00             NOP                     
5F8E: 36 00          LD      (HL),$00        
5F90: 3E 00          LD      A,$00           
5F92: 45             LD      B,L             
5F93: 00             NOP                     
5F94: 4C             LD      C,H             
5F95: 00             NOP                     
5F96: 53             LD      D,E             
5F97: 00             NOP                     
5F98: 59             LD      E,C             
5F99: 00             NOP                     
5F9A: 60             LD      H,B             
5F9B: 00             NOP                     
5F9C: 66             LD      H,(HL)          
5F9D: 00             NOP                     
5F9E: 6C             LD      L,H             
5F9F: 00             NOP                     
5FA0: 72             LD      (HL),D          
5FA1: 00             NOP                     
5FA2: 78             LD      A,B             
5FA3: 00             NOP                     
5FA4: 7B             LD      A,E             
5FA5: 00             NOP                     
5FA6: 7B             LD      A,E             
5FA7: 00             NOP                     
5FA8: 87             ADD     A,A             
5FA9: 00             NOP                     
5FAA: 8C             ADC     A,H             
5FAB: 00             NOP                     
5FAC: 92             SUB     D               
5FAD: 00             NOP                     
5FAE: 96             SUB     (HL)            
5FAF: 00             NOP                     
5FB0: 99             SBC     C               
5FB1: 00             NOP                     
5FB2: 9D             SBC     L               
5FB3: 00             NOP                     
5FB4: A1             AND     C               
5FB5: 00             NOP                     
5FB6: A5             AND     L               
5FB7: 00             NOP                     
5FB8: A8             XOR     B               
5FB9: 00             NOP                     
5FBA: AB             XOR     E               
5FBB: 00             NOP                     
5FBC: AF             XOR     A               
5FBD: 00             NOP                     
5FBE: B2             OR      D               
5FBF: 00             NOP                     
5FC0: B5             OR      L               
5FC1: 00             NOP                     
5FC2: B8             CP      B               
5FC3: 00             NOP                     
5FC4: BB             CP      E               
5FC5: 00             NOP                     
5FC6: B8             CP      B               
5FC7: 00             NOP                     
5FC8: C1             POP     BC              
5FC9: 00             NOP                     
5FCA: C4 00 C7       CALL    NZ,$C700        
5FCD: 00             NOP                     
5FCE: CA 00 CD       JP      Z,$CD00         
5FD1: 00             NOP                     
5FD2: D0             RET     NC              
5FD3: 00             NOP                     
5FD4: D3 00          OUT     ($00),A         
5FD6: D6 00          SUB     $00             
5FD8: D9             EXX                     
5FD9: 00             NOP                     
5FDA: DC 00 DF       CALL    C,$DF00         
5FDD: 00             NOP                     
5FDE: E2 00 E5       JP      PO,$E500        
5FE1: 00             NOP                     
5FE2: E8             RET     PE              
5FE3: 00             NOP                     
5FE4: EA 00 E5       JP      PE,$E500        
5FE7: 00             NOP                     
5FE8: F0             RET     P               
5FE9: 00             NOP                     
5FEA: F2 00 F4       JP      P,$F400         
5FED: 00             NOP                     
5FEE: F6 00          OR      $00             
5FF0: F8             RET     M               
5FF1: 00             NOP                     
5FF2: FA 00 FB       JP      M,$FB00         
5FF5: 00             NOP                     
5FF6: FC 00 FD       CALL    M,$FD00         
5FF9: 00             NOP                     
5FFA: FE 00          CP      $00             
5FFC: FF             RST     0X38            
5FFD: 00             NOP                     
5FFE: 00             NOP                     
5FFF: 01      
```
