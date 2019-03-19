![Bank 07](GBZelda.jpg)

# Bank 07

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```
4000: 3E 04      LD      A,$04           
4002: E0 F4      LDFF00  ($F4),A         
4004: C9         RET                     
4005: 7C         LD      A,H             
4006: 00         NOP                     
4007: 7E         LD      A,(HL)          
4008: 00         NOP                     
4009: 7E         LD      A,(HL)          
400A: 20 7C      JR      NZ,$4088        
400C: 20 F4      JR      NZ,$4002        
400E: 10 F6      STOP    $F6             
4010: 10 F0      STOP    $F0             
4012: 10 F2      STOP    $F2             
4014: 10 21      STOP    $21             
4016: B0         OR      B               
4017: C2 09 7E   JP      NZ,$7E09        
401A: FE 02      CP      $02             
401C: CA DD 41   JP      Z,$41DD         
401F: A7         AND     A               
4020: 20 24      JR      NZ,$4046        
4022: 34         INC     (HL)            
4023: F0 EE      LD      A,($EE)         
4025: 17         RLA                     
4026: 17         RLA                     
4027: E6 40      AND     $40             
4029: F5         PUSH    AF              
402A: 21 30 C4   LD      HL,$C430        
402D: 09         ADD     HL,BC           
402E: B6         OR      (HL)            
402F: 77         LD      (HL),A          
4030: F1         POP     AF              
4031: CB 27      SET     1,E             
4033: 21 50 C3   LD      HL,$C350        
4036: 09         ADD     HL,BC           
4037: B6         OR      (HL)            
4038: 77         LD      (HL),A          
4039: F0 EE      LD      A,($EE)         
403B: 1F         RRA                     
403C: 1F         RRA                     
403D: 1F         RRA                     
403E: 1F         RRA                     
403F: E6 01      AND     $01             
4041: 21 40 C4   LD      HL,$C440        
4044: 09         ADD     HL,BC           
4045: 77         LD      (HL),A          
4046: 21 C0 C2   LD      HL,$C2C0        
4049: 09         ADD     HL,BC           
404A: F0 EC      LD      A,($EC)         
404C: 96         SUB     (HL)            
404D: E0 EC      LDFF00  ($EC),A         
404F: 21 40 C4   LD      HL,$C440        
4052: 09         ADD     HL,BC           
4053: 7E         LD      A,(HL)          
4054: E0 F1      LDFF00  ($F1),A         
4056: 11 0D 40   LD      DE,$400D        
4059: CD 3B 3C   CALL    $3C3B           
405C: CD BA 3D   CALL    $3DBA           
405F: 21 C0 C2   LD      HL,$C2C0        
4062: 09         ADD     HL,BC           
4063: 7E         LD      A,(HL)          
4064: A7         AND     A               
4065: 28 0D      JR      Z,$4074         
4067: 21 B0 C3   LD      HL,$C3B0        
406A: 09         ADD     HL,BC           
406B: 7E         LD      A,(HL)          
406C: E0 F1      LDFF00  ($F1),A         
406E: 11 05 40   LD      DE,$4005        
4071: CD 3B 3C   CALL    $3C3B           
4074: CD 76 7C   CALL    $7C76           
4077: 21 60 C3   LD      HL,$C360        
407A: 09         ADD     HL,BC           
407B: 36 04      LD      (HL),$04        
407D: 21 20 C4   LD      HL,$C420        
4080: 09         ADD     HL,BC           
4081: 7E         LD      A,(HL)          
4082: A7         AND     A               
4083: 28 27      JR      Z,$40AC         
4085: 70         LD      (HL),B          
4086: 21 40 C4   LD      HL,$C440        
4089: 09         ADD     HL,BC           
408A: 7E         LD      A,(HL)          
408B: EE 01      XOR     $01             
408D: CD 87 3B   CALL    $3B87           
4090: 21 A0 C3   LD      HL,$C3A0        
4093: 09         ADD     HL,BC           
4094: 36 05      LD      (HL),$05        
4096: 21 F4 FF   LD      HL,$FFF4        
4099: 36 05      LD      (HL),$05        
409B: CD 8C 08   CALL    $088C           
409E: 36 1F      LD      (HL),$1F        
40A0: 21 40 C3   LD      HL,$C340        
40A3: 09         ADD     HL,BC           
40A4: 7E         LD      A,(HL)          
40A5: C6 02      ADD     $02             
40A7: 77         LD      (HL),A          
40A8: CD 84 41   CALL    $4184           
40AB: C9         RET                     
40AC: CD E2 08   CALL    $08E2           
40AF: CD B4 3B   CALL    $3BB4           
40B2: F0 F0      LD      A,($F0)         
40B4: C7         RST     0X00            
40B5: C1         POP     BC              
40B6: 40         LD      B,B             
40B7: A5         AND     L               
40B8: 41         LD      B,C             
40B9: 10 F0      STOP    $F0             
40BB: 00         NOP                     
40BC: 00         NOP                     
40BD: 00         NOP                     
40BE: 00         NOP                     
40BF: F0 10      LD      A,($10)         
40C1: 21 C0 C2   LD      HL,$C2C0        
40C4: 09         ADD     HL,BC           
40C5: 70         LD      (HL),B          
40C6: CD 91 08   CALL    $0891           
40C9: 20 49      JR      NZ,$4114        
40CB: CD 45 7D   CALL    $7D45           
40CE: C6 08      ADD     $08             
40D0: FE 10      CP      $10             
40D2: 38 10      JR      C,$40E4         
40D4: D5         PUSH    DE              
40D5: CD 35 7D   CALL    $7D35           
40D8: C6 08      ADD     $08             
40DA: D1         POP     DE              
40DB: FE 10      CP      $10             
40DD: 30 35      JR      NC,$4114        
40DF: 7B         LD      A,E             
40E0: FE 02      CP      $02             
40E2: 28 30      JR      Z,$4114         
40E4: CD 8D 3B   CALL    $3B8D           
40E7: CD 55 7D   CALL    $7D55           
40EA: 50         LD      D,B             
40EB: 21 B9 40   LD      HL,$40B9        
40EE: 19         ADD     HL,DE           
40EF: 7E         LD      A,(HL)          
40F0: 21 40 C2   LD      HL,$C240        
40F3: 09         ADD     HL,BC           
40F4: 77         LD      (HL),A          
40F5: 21 BD 40   LD      HL,$40BD        
40F8: 19         ADD     HL,DE           
40F9: 7E         LD      A,(HL)          
40FA: 21 50 C2   LD      HL,$C250        
40FD: 09         ADD     HL,BC           
40FE: 77         LD      (HL),A          
40FF: 21 40 C3   LD      HL,$C340        
4102: 09         ADD     HL,BC           
4103: CB BE      SET     1,E             
4105: 21 50 C3   LD      HL,$C350        
4108: 09         ADD     HL,BC           
4109: CB 96      SET     1,E             
410B: CD 65 3B   CALL    $3B65           
410E: CD 91 08   CALL    $0891           
4111: 36 30      LD      (HL),$30        
4113: C9         RET                     
4114: 21 40 C3   LD      HL,$C340        
4117: 09         ADD     HL,BC           
4118: CB FE      SET     1,E             
411A: 21 50 C3   LD      HL,$C350        
411D: 09         ADD     HL,BC           
411E: CB D6      SET     1,E             
4120: CD 65 3B   CALL    $3B65           
4123: CD D5 3B   CALL    $3BD5           
4126: D0         RET     NC              
4127: FA 9B C1   LD      A,($C19B)       
412A: A7         AND     A               
412B: C0         RET     NZ              
412C: FA 00 DB   LD      A,($DB00)       
412F: FE 03      CP      $03             
4131: 20 07      JR      NZ,$413A        
4133: F0 CC      LD      A,($CC)         
4135: E6 20      AND     $20             
4137: 20 0D      JR      NZ,$4146        
4139: C9         RET                     
413A: FA 01 DB   LD      A,($DB01)       
413D: FE 03      CP      $03             
413F: C0         RET     NZ              
4140: F0 CC      LD      A,($CC)         
4142: E6 10      AND     $10             
4144: 28 5E      JR      Z,$41A4         
4146: FA CF C3   LD      A,($C3CF)       
4149: A7         AND     A               
414A: C0         RET     NZ              
414B: 3C         INC     A               
414C: EA CF C3   LD      ($C3CF),A       
414F: CD 8D 3B   CALL    $3B8D           
4152: 36 02      LD      (HL),$02        
4154: 21 80 C2   LD      HL,$C280        
4157: 09         ADD     HL,BC           
4158: 36 07      LD      (HL),$07        
415A: 21 90 C3   LD      HL,$C390        
415D: 09         ADD     HL,BC           
415E: 36 01      LD      (HL),$01        
4160: 21 90 C4   LD      HL,$C490        
4163: 09         ADD     HL,BC           
4164: 70         LD      (HL),B          
4165: F0 9E      LD      A,($9E)         
4167: EA 5D C1   LD      ($C15D),A       
416A: CD 91 08   CALL    $0891           
416D: 36 02      LD      (HL),$02        
416F: 21 F3 FF   LD      HL,$FFF3        
4172: 36 02      LD      (HL),$02        
4174: 21 A0 C3   LD      HL,$C3A0        
4177: 09         ADD     HL,BC           
4178: 36 05      LD      (HL),$05        
417A: 21 40 C4   LD      HL,$C440        
417D: 09         ADD     HL,BC           
417E: 7E         LD      A,(HL)          
417F: EE 01      XOR     $01             
4181: CD 87 3B   CALL    $3B87           
4184: 3E BB      LD      A,$BB           
4186: CD 01 3C   CALL    $3C01           
4189: D8         RET     C               
418A: F0 D7      LD      A,($D7)         
418C: 21 00 C2   LD      HL,$C200        
418F: 19         ADD     HL,DE           
4190: 77         LD      (HL),A          
4191: F0 D8      LD      A,($D8)         
4193: 21 10 C2   LD      HL,$C210        
4196: 19         ADD     HL,DE           
4197: 77         LD      (HL),A          
4198: 21 B0 C2   LD      HL,$C2B0        
419B: 19         ADD     HL,DE           
419C: 36 02      LD      (HL),$02        
419E: 21 E0 C2   LD      HL,$C2E0        
41A1: 19         ADD     HL,DE           
41A2: 36 40      LD      (HL),$40        
41A4: C9         RET                     
41A5: CD 91 08   CALL    $0891           
41A8: 20 0A      JR      NZ,$41B4        
41AA: CD 91 08   CALL    $0891           
41AD: 36 20      LD      (HL),$20        
41AF: CD 8D 3B   CALL    $3B8D           
41B2: 70         LD      (HL),B          
41B3: C9         RET                     
41B4: CD E2 7C   CALL    $7CE2           
41B7: CD 9E 3B   CALL    $3B9E           
41BA: 21 A0 C2   LD      HL,$C2A0        
41BD: 09         ADD     HL,BC           
41BE: 7E         LD      A,(HL)          
41BF: A7         AND     A               
41C0: 20 E8      JR      NZ,$41AA        
41C2: 21 C0 C2   LD      HL,$C2C0        
41C5: 09         ADD     HL,BC           
41C6: 36 04      LD      (HL),$04        
41C8: F0 E7      LD      A,($E7)         
41CA: 1F         RRA                     
41CB: 1F         RRA                     
41CC: 1F         RRA                     
41CD: E6 01      AND     $01             
41CF: CD 87 3B   CALL    $3B87           
41D2: C9         RET                     
41D3: F0 F4      LD      A,($F4)         
41D5: 00         NOP                     
41D6: 0C         INC     C               
41D7: 10 0C      STOP    $0C             
41D9: 00         NOP                     
41DA: F4         ???                     
41DB: F0 F4      LD      A,($F4)         
41DD: 11 05 40   LD      DE,$4005        
41E0: CD 3B 3C   CALL    $3C3B           
41E3: CD 76 7C   CALL    $7C76           
41E6: CD 98 7C   CALL    $7C98           
41E9: F0 E7      LD      A,($E7)         
41EB: 1F         RRA                     
41EC: 1F         RRA                     
41ED: 1F         RRA                     
41EE: E6 01      AND     $01             
41F0: CD 87 3B   CALL    $3B87           
41F3: CD E2 7C   CALL    $7CE2           
41F6: CD 9E 3B   CALL    $3B9E           
41F9: CD B4 3B   CALL    $3BB4           
41FC: CD 91 08   CALL    $0891           
41FF: 20 20      JR      NZ,$4221        
4201: CD ED 27   CALL    $27ED           
4204: E6 1F      AND     $1F             
4206: C6 20      ADD     $20             
4208: 77         LD      (HL),A          
4209: E6 07      AND     $07             
420B: 5F         LD      E,A             
420C: 50         LD      D,B             
420D: 21 D5 41   LD      HL,$41D5        
4210: 19         ADD     HL,DE           
4211: 7E         LD      A,(HL)          
4212: 21 40 C2   LD      HL,$C240        
4215: 09         ADD     HL,BC           
4216: 77         LD      (HL),A          
4217: 21 D3 41   LD      HL,$41D3        
421A: 19         ADD     HL,DE           
421B: 7E         LD      A,(HL)          
421C: 21 50 C2   LD      HL,$C250        
421F: 09         ADD     HL,BC           
4220: 77         LD      (HL),A          
4221: C9         RET                     
4222: 00         NOP                     
4223: F0 78      LD      A,($78)         
4225: 00         NOP                     
4226: 00         NOP                     
4227: F8 7A      LDHL    SP,$7A          
4229: 00         NOP                     
422A: 00         NOP                     
422B: 00         NOP                     
422C: 70         LD      (HL),B          
422D: 00         NOP                     
422E: 00         NOP                     
422F: 08 72 00   LD      ($0072),SP      
4232: 00         NOP                     
4233: F0 7C      LD      A,($7C)         
4235: 00         NOP                     
4236: 00         NOP                     
4237: F8 7E      LDHL    SP,$7E          
4239: 00         NOP                     
423A: 00         NOP                     
423B: 00         NOP                     
423C: 70         LD      (HL),B          
423D: 00         NOP                     
423E: 00         NOP                     
423F: 08 72 00   LD      ($0072),SP      
4242: 00         NOP                     
4243: F0 78      LD      A,($78)         
4245: 00         NOP                     
4246: 00         NOP                     
4247: F8 7A      LDHL    SP,$7A          
4249: 00         NOP                     
424A: 00         NOP                     
424B: 00         NOP                     
424C: 74         LD      (HL),H          
424D: 00         NOP                     
424E: 00         NOP                     
424F: 08 76 00   LD      ($0076),SP      
4252: FC         ???                     
4253: F0 64      LD      A,($64)         
4255: 00         NOP                     
4256: FC         ???                     
4257: F8 66      LDHL    SP,$66          
4259: 00         NOP                     
425A: 00         NOP                     
425B: 00         NOP                     
425C: 60         LD      H,B             
425D: 00         NOP                     
425E: 00         NOP                     
425F: 08 62 00   LD      ($0062),SP      
4262: FC         ???                     
4263: F0 64      LD      A,($64)         
4265: 00         NOP                     
4266: FC         ???                     
4267: F8 66      LDHL    SP,$66          
4269: 00         NOP                     
426A: 00         NOP                     
426B: 00         NOP                     
426C: 74         LD      (HL),H          
426D: 00         NOP                     
426E: 00         NOP                     
426F: 08 76 00   LD      ($0076),SP      
4272: 21 B0 C2   LD      HL,$C2B0        
4275: 09         ADD     HL,BC           
4276: 7E         LD      A,(HL)          
4277: FE 02      CP      $02             
4279: CA 17 44   JP      Z,$4417         
427C: A7         AND     A               
427D: 20 33      JR      NZ,$42B2        
427F: 34         INC     (HL)            
4280: 21 10 C2   LD      HL,$C210        
4283: 09         ADD     HL,BC           
4284: 7E         LD      A,(HL)          
4285: C6 08      ADD     $08             
4287: 77         LD      (HL),A          
4288: 3E B8      LD      A,$B8           
428A: CD 01 3C   CALL    $3C01           
428D: F0 D7      LD      A,($D7)         
428F: 21 00 C2   LD      HL,$C200        
4292: 19         ADD     HL,DE           
4293: C6 06      ADD     $06             
4295: 77         LD      (HL),A          
4296: F0 D8      LD      A,($D8)         
4298: 21 10 C2   LD      HL,$C210        
429B: 19         ADD     HL,DE           
429C: C6 10      ADD     $10             
429E: 77         LD      (HL),A          
429F: 21 B0 C2   LD      HL,$C2B0        
42A2: 19         ADD     HL,DE           
42A3: 36 02      LD      (HL),$02        
42A5: 21 50 C3   LD      HL,$C350        
42A8: 19         ADD     HL,DE           
42A9: 36 AC      LD      (HL),$AC        
42AB: C5         PUSH    BC              
42AC: D5         PUSH    DE              
42AD: C1         POP     BC              
42AE: CD 65 3B   CALL    $3B65           
42B1: C1         POP     BC              
42B2: FA 9F C1   LD      A,($C19F)       
42B5: A7         AND     A               
42B6: 28 0C      JR      Z,$42C4         
42B8: F0 F1      LD      A,($F1)         
42BA: FE 03      CP      $03             
42BC: 3E 02      LD      A,$02           
42BE: 20 02      JR      NZ,$42C2        
42C0: 3E 04      LD      A,$04           
42C2: E0 F1      LDFF00  ($F1),A         
42C4: CD B3 43   CALL    $43B3           
42C7: CD 76 7C   CALL    $7C76           
42CA: F0 F0      LD      A,($F0)         
42CC: C7         RST     0X00            
42CD: D7         RST     0X10            
42CE: 42         LD      B,D             
42CF: 05         DEC     B               
42D0: 43         LD      B,E             
42D1: 27         DAA                     
42D2: 43         LD      B,E             
42D3: 55         LD      D,L             
42D4: 43         LD      B,E             
42D5: AA         XOR     D               
42D6: 43         LD      B,E             
42D7: CD 23 7C   CALL    $7C23           
42DA: 30 1D      JR      NC,$42F9        
42DC: FA 0E DB   LD      A,($DB0E)       
42DF: FE 0B      CP      $0B             
42E1: 20 08      JR      NZ,$42EB        
42E3: 3E E8      LD      A,$E8           
42E5: CD 85 21   CALL    $2185           
42E8: C3 8D 3B   JP      $3B8D           
42EB: FE 0C      CP      $0C             
42ED: 30 05      JR      NC,$42F4        
42EF: 3E E7      LD      A,$E7           
42F1: C3 85 21   JP      $2185           
42F4: 3E ED      LD      A,$ED           
42F6: C3 85 21   JP      $2185           
42F9: F0 E7      LD      A,($E7)         
42FB: E6 30      AND     $30             
42FD: 58         LD      E,B             
42FE: 28 01      JR      Z,$4301         
4300: 1C         INC     E               
4301: 7B         LD      A,E             
4302: C3 87 3B   JP      $3B87           
4305: CD 8D 3B   CALL    $3B8D           
4308: FA 77 C1   LD      A,($C177)       
430B: A7         AND     A               
430C: 20 12      JR      NZ,$4320        
430E: 3E 01      LD      A,$01           
4310: EA 7F DB   LD      ($DB7F),A       
4313: EA 67 C1   LD      ($C167),A       
4316: CD 91 08   CALL    $0891           
4319: 36 D0      LD      (HL),$D0        
431B: 3E E9      LD      A,$E9           
431D: C3 85 21   JP      $2185           
4320: 70         LD      (HL),B          
4321: 3E EA      LD      A,$EA           
4323: CD 85 21   CALL    $2185           
4326: C9         RET                     
4327: 3E 02      LD      A,$02           
4329: E0 A1      LDFF00  ($A1),A         
432B: 3E 01      LD      A,$01           
432D: EA 0B C1   LD      ($C10B),A       
4330: CD 91 08   CALL    $0891           
4333: 20 0A      JR      NZ,$433F        
4335: 36 20      LD      (HL),$20        
4337: 3E EB      LD      A,$EB           
4339: CD 85 21   CALL    $2185           
433C: CD 8D 3B   CALL    $3B8D           
433F: 1E 03      LD      E,$03           
4341: FE 30      CP      $30             
4343: 38 0C      JR      C,$4351         
4345: FE 80      CP      $80             
4347: 30 B0      JR      NC,$42F9        
4349: F0 E7      LD      A,($E7)         
434B: E6 18      AND     $18             
434D: 58         LD      E,B             
434E: 28 01      JR      Z,$4351         
4350: 1C         INC     E               
4351: 7B         LD      A,E             
4352: C3 87 3B   JP      $3B87           
4355: 3E 02      LD      A,$02           
4357: E0 A1      LDFF00  ($A1),A         
4359: CD 91 08   CALL    $0891           
435C: 20 46      JR      NZ,$43A4        
435E: EA 0B C1   LD      ($C10B),A       
4361: CD 8D 3B   CALL    $3B8D           
4364: 3E 54      LD      A,$54           
4366: CD 01 3C   CALL    $3C01           
4369: F0 D7      LD      A,($D7)         
436B: D6 20      SUB     $20             
436D: 21 00 C2   LD      HL,$C200        
4370: 19         ADD     HL,DE           
4371: 77         LD      (HL),A          
4372: E0 EE      LDFF00  ($EE),A         
4374: F0 D8      LD      A,($D8)         
4376: C6 08      ADD     $08             
4378: 21 10 C2   LD      HL,$C210        
437B: 19         ADD     HL,DE           
437C: 77         LD      (HL),A          
437D: E0 EC      LDFF00  ($EC),A         
437F: 21 20 C3   LD      HL,$C320        
4382: 19         ADD     HL,DE           
4383: 36 20      LD      (HL),$20        
4385: 21 40 C4   LD      HL,$C440        
4388: 19         ADD     HL,DE           
4389: 36 01      LD      (HL),$01        
438B: C5         PUSH    BC              
438C: D5         PUSH    DE              
438D: C1         POP     BC              
438E: 3E 0A      LD      A,$0A           
4390: CD 25 3C   CALL    $3C25           
4393: C1         POP     BC              
4394: CD 00 47   CALL    $4700           
4397: 3E 08      LD      A,$08           
4399: E0 F2      LDFF00  ($F2),A         
439B: 3E 0C      LD      A,$0C           
439D: EA 0E DB   LD      ($DB0E),A       
43A0: 3E 0D      LD      A,$0D           
43A2: E0 A5      LDFF00  ($A5),A         
43A4: 3E 03      LD      A,$03           
43A6: CD 87 3B   CALL    $3B87           
43A9: C9         RET                     
43AA: 3E 02      LD      A,$02           
43AC: E0 A1      LDFF00  ($A1),A         
43AE: CD 8D 3B   CALL    $3B8D           
43B1: 70         LD      (HL),B          
43B2: C9         RET                     
43B3: F0 F1      LD      A,($F1)         
43B5: 17         RLA                     
43B6: 17         RLA                     
43B7: 17         RLA                     
43B8: 17         RLA                     
43B9: E6 F0      AND     $F0             
43BB: 5F         LD      E,A             
43BC: 50         LD      D,B             
43BD: 21 22 42   LD      HL,$4222        
43C0: 19         ADD     HL,DE           
43C1: 0E 04      LD      C,$04           
43C3: CD 26 3D   CALL    $3D26           
43C6: C9         RET                     
43C7: FE FE      CP      $FE             
43C9: FE FE      CP      $FE             
43CB: FF         RST     0X38            
43CC: FF         RST     0X38            
43CD: FF         RST     0X38            
43CE: FF         RST     0X38            
43CF: FF         RST     0X38            
43D0: 00         NOP                     
43D1: 00         NOP                     
43D2: 01 01 01   LD      BC,$0101        
43D5: 01 01 02   LD      BC,$0201        
43D8: 02         LD      (BC),A          
43D9: 02         LD      (BC),A          
43DA: 02         LD      (BC),A          
43DB: 02         LD      (BC),A          
43DC: 02         LD      (BC),A          
43DD: 02         LD      (BC),A          
43DE: 02         LD      (BC),A          
43DF: 02         LD      (BC),A          
43E0: 02         LD      (BC),A          
43E1: 02         LD      (BC),A          
43E2: 02         LD      (BC),A          
43E3: 02         LD      (BC),A          
43E4: 02         LD      (BC),A          
43E5: 02         LD      (BC),A          
43E6: 02         LD      (BC),A          
43E7: 02         LD      (BC),A          
43E8: 02         LD      (BC),A          
43E9: 01 00 00   LD      BC,$0000        
43EC: FF         RST     0X38            
43ED: FE FE      CP      $FE             
43EF: 01 01 01   LD      BC,$0101        
43F2: 00         NOP                     
43F3: 00         NOP                     
43F4: FF         RST     0X38            
43F5: FF         RST     0X38            
43F6: FF         RST     0X38            
43F7: 00         NOP                     
43F8: 00         NOP                     
43F9: 00         NOP                     
43FA: 00         NOP                     
43FB: 00         NOP                     
43FC: 00         NOP                     
43FD: 00         NOP                     
43FE: 00         NOP                     
43FF: FF         RST     0X38            
4400: FF         RST     0X38            
4401: FF         RST     0X38            
4402: 00         NOP                     
4403: 00         NOP                     
4404: 01 01 01   LD      BC,$0101        
4407: FE FE      CP      $FE             
4409: FF         RST     0X38            
440A: 00         NOP                     
440B: 00         NOP                     
440C: 01 02 02   LD      BC,$0202        
440F: 00         NOP                     
4410: 00         NOP                     
4411: 01 02 02   LD      BC,$0202        
4414: 02         LD      (BC),A          
4415: 01 00 21   LD      BC,$2100        
4418: D0         RET     NC              
4419: C3 09 7E   JP      $7E09           
441C: 1F         RRA                     
441D: 1F         RRA                     
441E: 1F         RRA                     
441F: E6 07      AND     $07             
4421: 5F         LD      E,A             
4422: 50         LD      D,B             
4423: 21 0F 44   LD      HL,$440F        
4426: 19         ADD     HL,DE           
4427: F0 EC      LD      A,($EC)         
4429: 86         ADD     A,(HL)          
442A: E0 EC      LDFF00  ($EC),A         
442C: D6 10      SUB     $10             
442E: EA 10 C2   LD      ($C210),A       
4431: CD 92 44   CALL    $4492           
4434: CD D5 3B   CALL    $3BD5           
4437: 30 1E      JR      NC,$4457        
4439: F0 9B      LD      A,($9B)         
443B: E6 80      AND     $80             
443D: 20 18      JR      NZ,$4457        
443F: CD 45 7D   CALL    $7D45           
4442: C6 08      ADD     $08             
4444: CB 7F      SET     1,E             
4446: 28 0F      JR      Z,$4457         
4448: F0 EC      LD      A,($EC)         
444A: D6 0F      SUB     $0F             
444C: E0 99      LDFF00  ($99),A         
444E: 3E 02      LD      A,$02           
4450: E0 9B      LDFF00  ($9B),A         
4452: 3E 01      LD      A,$01           
4454: EA 47 C1   LD      ($C147),A       
4457: CD 76 7C   CALL    $7C76           
445A: 21 D0 C3   LD      HL,$C3D0        
445D: 09         ADD     HL,BC           
445E: 34         INC     (HL)            
445F: 7E         LD      A,(HL)          
4460: E6 07      AND     $07             
4462: 20 19      JR      NZ,$447D        
4464: 1E 48      LD      E,$48           
4466: FA 47 C1   LD      A,($C147)       
4469: A7         AND     A               
446A: 28 02      JR      Z,$446E         
446C: 1E 4B      LD      E,$4B           
446E: 21 10 C2   LD      HL,$C210        
4471: 09         ADD     HL,BC           
4472: 7E         LD      A,(HL)          
4473: 93         SUB     E               
4474: 28 07      JR      Z,$447D         
4476: E6 80      AND     $80             
4478: 28 02      JR      Z,$447C         
447A: 34         INC     (HL)            
447B: 34         INC     (HL)            
447C: 35         DEC     (HL)            
447D: C9         RET                     
447E: 00         NOP                     
447F: F8 68      LDHL    SP,$68          
4481: 00         NOP                     
4482: 00         NOP                     
4483: 00         NOP                     
4484: 6A         LD      L,D             
4485: 00         NOP                     
4486: 00         NOP                     
4487: 08 6A 00   LD      ($006A),SP      
448A: 00         NOP                     
448B: 10 6A      STOP    $6A             
448D: 00         NOP                     
448E: 00         NOP                     
448F: 18 6C      JR      $44FD           
4491: 00         NOP                     
4492: 21 7E 44   LD      HL,$447E        
4495: 0E 05      LD      C,$05           
4497: CD 26 3D   CALL    $3D26           
449A: C9         RET                     
449B: 72         LD      (HL),D          
449C: 20 70      JR      NZ,$450E        
449E: 20 70      JR      NZ,$4510        
44A0: 00         NOP                     
44A1: 72         LD      (HL),D          
44A2: 00         NOP                     
44A3: 76         HALT                    
44A4: 00         NOP                     
44A5: 78         LD      A,B             
44A6: 00         NOP                     
44A7: 78         LD      A,B             
44A8: 20 76      JR      NZ,$4520        
44AA: 20 74      JR      NZ,$4520        
44AC: 00         NOP                     
44AD: 74         LD      (HL),H          
44AE: 20 74      JR      NZ,$4524        
44B0: 10 74      STOP    $74             
44B2: 30 00      JR      NC,$44B4        
44B4: FC         ???                     
44B5: 7A         LD      A,D             
44B6: 00         NOP                     
44B7: 00         NOP                     
44B8: 04         INC     B               
44B9: 7C         LD      A,H             
44BA: 00         NOP                     
44BB: 00         NOP                     
44BC: 0C         INC     C               
44BD: 7E         LD      A,(HL)          
44BE: 00         NOP                     
44BF: 00         NOP                     
44C0: FC         ???                     
44C1: 7E         LD      A,(HL)          
44C2: 20 00      JR      NZ,$44C4        
44C4: 04         INC     B               
44C5: 7C         LD      A,H             
44C6: 20 00      JR      NZ,$44C8        
44C8: 0C         INC     C               
44C9: 7A         LD      A,D             
44CA: 20 00      JR      NZ,$44CC        
44CC: 00         NOP                     
44CD: 01 02 02   LD      BC,$0202        
44D0: 02         LD      (BC),A          
44D1: 01 00 21   LD      BC,$2100        
44D4: D0         RET     NC              
44D5: C2 09 7E   JP      NZ,$7E09        
44D8: A7         AND     A               
44D9: C2 12 47   JP      NZ,$4712        
44DC: F0 F0      LD      A,($F0)         
44DE: FE 02      CP      $02             
44E0: 30 1A      JR      NC,$44FC        
44E2: F0 F8      LD      A,($F8)         
44E4: E6 20      AND     $20             
44E6: 28 02      JR      Z,$44EA         
44E8: 34         INC     (HL)            
44E9: C9         RET                     
44EA: F0 E7      LD      A,($E7)         
44EC: 1F         RRA                     
44ED: 1F         RRA                     
44EE: 1F         RRA                     
44EF: E6 07      AND     $07             
44F1: 5F         LD      E,A             
44F2: 50         LD      D,B             
44F3: 21 CB 44   LD      HL,$44CB        
44F6: 19         ADD     HL,DE           
44F7: F0 EC      LD      A,($EC)         
44F9: 86         ADD     A,(HL)          
44FA: E0 EC      LDFF00  ($EC),A         
44FC: F0 F1      LD      A,($F1)         
44FE: FE 04      CP      $04             
4500: 38 18      JR      C,$451A         
4502: D6 04      SUB     $04             
4504: 17         RLA                     
4505: 17         RLA                     
4506: E6 FC      AND     $FC             
4508: 5F         LD      E,A             
4509: 17         RLA                     
450A: E6 F8      AND     $F8             
450C: 83         ADD     A,E             
450D: 5F         LD      E,A             
450E: 50         LD      D,B             
450F: 21 B3 44   LD      HL,$44B3        
4512: 19         ADD     HL,DE           
4513: 0E 03      LD      C,$03           
4515: CD 26 3D   CALL    $3D26           
4518: 18 09      JR      $4523           
451A: 11 9B 44   LD      DE,$449B        
451D: CD 3B 3C   CALL    $3C3B           
4520: CD BA 3D   CALL    $3DBA           
4523: F0 F0      LD      A,($F0)         
4525: FE 05      CP      $05             
4527: 28 04      JR      Z,$452D         
4529: FE 03      CP      $03             
452B: 30 12      JR      NC,$453F        
452D: F0 EC      LD      A,($EC)         
452F: C6 0B      ADD     $0B             
4531: E0 EC      LDFF00  ($EC),A         
4533: AF         XOR     A               
4534: E0 F1      LDFF00  ($F1),A         
4536: 11 AB 44   LD      DE,$44AB        
4539: CD 3B 3C   CALL    $3C3B           
453C: CD BA 3D   CALL    $3DBA           
453F: CD 76 7C   CALL    $7C76           
4542: F0 F0      LD      A,($F0)         
4544: C7         RST     0X00            
4545: 5B         LD      E,E             
4546: 45         LD      B,L             
4547: 64         LD      H,H             
4548: 45         LD      B,L             
4549: B0         OR      B               
454A: 45         LD      B,L             
454B: B3         OR      E               
454C: 45         LD      B,L             
454D: DE 45      SBC     $45             
454F: FC         ???                     
4550: 45         LD      B,L             
4551: 11 46 6F   LD      DE,$6F46        
4554: 46         LD      B,(HL)          
4555: 98         SBC     B               
4556: 46         LD      B,(HL)          
4557: BA         CP      D               
4558: 46         LD      B,(HL)          
4559: D5         PUSH    DE              
455A: 46         LD      B,(HL)          
455B: 21 B0 C2   LD      HL,$C2B0        
455E: 09         ADD     HL,BC           
455F: 36 30      LD      (HL),$30        
4561: C3 8D 3B   JP      $3B8D           
4564: CD 35 7D   CALL    $7D35           
4567: 7B         LD      A,E             
4568: CD 87 3B   CALL    $3B87           
456B: CD D0 7B   CALL    $7BD0           
456E: CD 35 7D   CALL    $7D35           
4571: C6 12      ADD     $12             
4573: FE 24      CP      $24             
4575: 30 1C      JR      NC,$4593        
4577: CD 45 7D   CALL    $7D45           
457A: C6 12      ADD     $12             
457C: FE 24      CP      $24             
457E: 30 13      JR      NC,$4593        
4580: F0 9C      LD      A,($9C)         
4582: A7         AND     A               
4583: 28 0E      JR      Z,$4593         
4585: CD 8D 3B   CALL    $3B8D           
4588: CD 91 08   CALL    $0891           
458B: 36 14      LD      (HL),$14        
458D: 3E F1      LD      A,$F1           
458F: CD 85 21   CALL    $2185           
4592: C9         RET                     
4593: CD 23 7C   CALL    $7C23           
4596: 30 17      JR      NC,$45AF        
4598: FA 0E DB   LD      A,($DB0E)       
459B: FE 0C      CP      $0C             
459D: 20 0B      JR      NZ,$45AA        
459F: 3E F2      LD      A,$F2           
45A1: CD 85 21   CALL    $2185           
45A4: CD 8D 3B   CALL    $3B8D           
45A7: 36 05      LD      (HL),$05        
45A9: C9         RET                     
45AA: 3E F0      LD      A,$F0           
45AC: CD 85 21   CALL    $2185           
45AF: C9         RET                     
45B0: C3 8D 3B   JP      $3B8D           
45B3: FA 9F C1   LD      A,($C19F)       
45B6: A7         AND     A               
45B7: 20 24      JR      NZ,$45DD        
45B9: CD 91 08   CALL    $0891           
45BC: 20 0E      JR      NZ,$45CC        
45BE: 36 40      LD      (HL),$40        
45C0: CD 00 47   CALL    $4700           
45C3: CD 8D 3B   CALL    $3B8D           
45C6: 3E FF      LD      A,$FF           
45C8: CD 87 3B   CALL    $3B87           
45CB: C9         RET                     
45CC: 1E FF      LD      E,$FF           
45CE: FE 10      CP      $10             
45D0: 30 07      JR      NC,$45D9        
45D2: 1E 02      LD      E,$02           
45D4: FE 08      CP      $08             
45D6: 38 01      JR      C,$45D9         
45D8: 1C         INC     E               
45D9: 7B         LD      A,E             
45DA: CD 87 3B   CALL    $3B87           
45DD: C9         RET                     
45DE: CD 91 08   CALL    $0891           
45E1: 20 18      JR      NZ,$45FB        
45E3: 21 B0 C2   LD      HL,$C2B0        
45E6: 09         ADD     HL,BC           
45E7: 7E         LD      A,(HL)          
45E8: 2F         CPL                     
45E9: 3C         INC     A               
45EA: 77         LD      (HL),A          
45EB: 21 00 C2   LD      HL,$C200        
45EE: 09         ADD     HL,BC           
45EF: 86         ADD     A,(HL)          
45F0: 77         LD      (HL),A          
45F1: E0 EE      LDFF00  ($EE),A         
45F3: CD 8D 3B   CALL    $3B8D           
45F6: 36 01      LD      (HL),$01        
45F8: CD 00 47   CALL    $4700           
45FB: C9         RET                     
45FC: CD 8D 3B   CALL    $3B8D           
45FF: FA 77 C1   LD      A,($C177)       
4602: A7         AND     A               
4603: 20 06      JR      NZ,$460B        
4605: CD 91 08   CALL    $0891           
4608: 36 C0      LD      (HL),$C0        
460A: C9         RET                     
460B: 70         LD      (HL),B          
460C: 3E F4      LD      A,$F4           
460E: C3 85 21   JP      $2185           
4611: FA 9F C1   LD      A,($C19F)       
4614: A7         AND     A               
4615: 20 57      JR      NZ,$466E        
4617: CD 91 08   CALL    $0891           
461A: 28 40      JR      Z,$465C         
461C: FE 70      CP      $70             
461E: 20 08      JR      NZ,$4628        
4620: 35         DEC     (HL)            
4621: F5         PUSH    AF              
4622: 3E F3      LD      A,$F3           
4624: CD 85 21   CALL    $2185           
4627: F1         POP     AF              
4628: FE 90      CP      $90             
462A: 20 16      JR      NZ,$4642        
462C: F0 99      LD      A,($99)         
462E: D6 03      SUB     $03             
4630: E0 D8      LDFF00  ($D8),A         
4632: F0 98      LD      A,($98)         
4634: E0 D7      LDFF00  ($D7),A         
4636: 3E 0E      LD      A,$0E           
4638: E0 F2      LDFF00  ($F2),A         
463A: 3E 01      LD      A,$01           
463C: CD 53 09   CALL    $0953           
463F: CD 91 08   CALL    $0891           
4642: 1E 00      LD      E,$00           
4644: FE 20      CP      $20             
4646: 38 06      JR      C,$464E         
4648: FE 90      CP      $90             
464A: 30 02      JR      NC,$464E        
464C: 1E 01      LD      E,$01           
464E: 7B         LD      A,E             
464F: E0 9C      LDFF00  ($9C),A         
4651: 21 A1 FF   LD      HL,$FFA1        
4654: 36 02      LD      (HL),$02        
4656: 3E 04      LD      A,$04           
4658: EA 3B C1   LD      ($C13B),A       
465B: C9         RET                     
465C: 3E 0D      LD      A,$0D           
465E: EA 0E DB   LD      ($DB0E),A       
4661: E0 A5      LDFF00  ($A5),A         
4663: CD 98 08   CALL    $0898           
4666: CD 8D 3B   CALL    $3B8D           
4669: CD 91 08   CALL    $0891           
466C: 36 30      LD      (HL),$30        
466E: C9         RET                     
466F: CD 91 08   CALL    $0891           
4672: 20 23      JR      NZ,$4697        
4674: CD 8D 3B   CALL    $3B8D           
4677: F0 F1      LD      A,($F1)         
4679: C6 04      ADD     $04             
467B: CD 87 3B   CALL    $3B87           
467E: 1E 08      LD      E,$08           
4680: FE 04      CP      $04             
4682: 20 02      JR      NZ,$4686        
4684: 1E F8      LD      E,$F8           
4686: 21 40 C2   LD      HL,$C240        
4689: 09         ADD     HL,BC           
468A: 73         LD      (HL),E          
468B: 21 20 C3   LD      HL,$C320        
468E: 09         ADD     HL,BC           
468F: 36 20      LD      (HL),$20        
4691: CD 00 47   CALL    $4700           
4694: CD 44 72   CALL    $7244           
4697: C9         RET                     
4698: CD E2 7C   CALL    $7CE2           
469B: CD 1B 7D   CALL    $7D1B           
469E: 21 20 C3   LD      HL,$C320        
46A1: 09         ADD     HL,BC           
46A2: 35         DEC     (HL)            
46A3: 35         DEC     (HL)            
46A4: 21 10 C3   LD      HL,$C310        
46A7: 09         ADD     HL,BC           
46A8: 7E         LD      A,(HL)          
46A9: E6 80      AND     $80             
46AB: 28 0C      JR      Z,$46B9         
46AD: 70         LD      (HL),B          
46AE: CD 8D 3B   CALL    $3B8D           
46B1: CD 00 47   CALL    $4700           
46B4: CD 91 08   CALL    $0891           
46B7: 36 10      LD      (HL),$10        
46B9: C9         RET                     
46BA: CD 91 08   CALL    $0891           
46BD: 20 0A      JR      NZ,$46C9        
46BF: 36 20      LD      (HL),$20        
46C1: 3E FF      LD      A,$FF           
46C3: CD 87 3B   CALL    $3B87           
46C6: C3 8D 3B   JP      $3B8D           
46C9: 1E 02      LD      E,$02           
46CB: FE 08      CP      $08             
46CD: 30 01      JR      NC,$46D0        
46CF: 1C         INC     E               
46D0: 7B         LD      A,E             
46D1: CD 87 3B   CALL    $3B87           
46D4: C9         RET                     
46D5: CD 91 08   CALL    $0891           
46D8: C0         RET     NZ              
46D9: 21 90 C3   LD      HL,$C390        
46DC: 09         ADD     HL,BC           
46DD: 7E         LD      A,(HL)          
46DE: FE 03      CP      $03             
46E0: CA 7C 7D   JP      Z,$7D7C         
46E3: 34         INC     (HL)            
46E4: CD ED 27   CALL    $27ED           
46E7: E6 01      AND     $01             
46E9: CD 87 3B   CALL    $3B87           
46EC: 1E 10      LD      E,$10           
46EE: A7         AND     A               
46EF: 28 02      JR      Z,$46F3         
46F1: 1E F0      LD      E,$F0           
46F3: 21 10 C2   LD      HL,$C210        
46F6: 09         ADD     HL,BC           
46F7: 7E         LD      A,(HL)          
46F8: 83         ADD     A,E             
46F9: 77         LD      (HL),A          
46FA: CD 8D 3B   CALL    $3B8D           
46FD: 36 07      LD      (HL),$07        
46FF: C9         RET                     
4700: F0 EC      LD      A,($EC)         
4702: E0 D8      LDFF00  ($D8),A         
4704: F0 EE      LD      A,($EE)         
4706: E0 D7      LDFF00  ($D7),A         
4708: 3E 01      LD      A,$01           
470A: CD 53 09   CALL    $0953           
470D: 3E 0E      LD      A,$0E           
470F: E0 F2      LDFF00  ($F2),A         
4711: C9         RET                     
4712: F0 F0      LD      A,($F0)         
4714: C7         RST     0X00            
4715: 1D         DEC     E               
4716: 47         LD      B,A             
4717: 36 47      LD      (HL),$47        
4719: 4B         LD      C,E             
471A: 47         LD      B,A             
471B: 75         LD      (HL),L          
471C: 47         LD      B,A             
471D: CD 76 7C   CALL    $7C76           
4720: 21 00 C2   LD      HL,$C200        
4723: 09         ADD     HL,BC           
4724: 36 58      LD      (HL),$58        
4726: 21 10 C2   LD      HL,$C210        
4729: 09         ADD     HL,BC           
472A: 36 80      LD      (HL),$80        
472C: FA 30 C1   LD      A,($C130)       
472F: A7         AND     A               
4730: 28 03      JR      Z,$4735         
4732: CD 8D 3B   CALL    $3B8D           
4735: C9         RET                     
4736: CD 76 7C   CALL    $7C76           
4739: 21 20 C3   LD      HL,$C320        
473C: 09         ADD     HL,BC           
473D: 36 20      LD      (HL),$20        
473F: 21 50 C2   LD      HL,$C250        
4742: 09         ADD     HL,BC           
4743: 36 FC      LD      (HL),$FC        
4745: CD 00 47   CALL    $4700           
4748: C3 8D 3B   JP      $3B8D           
474B: CD CE 47   CALL    $47CE           
474E: CD 76 7C   CALL    $7C76           
4751: CD E2 7C   CALL    $7CE2           
4754: CD 1B 7D   CALL    $7D1B           
4757: 21 20 C3   LD      HL,$C320        
475A: 09         ADD     HL,BC           
475B: 35         DEC     (HL)            
475C: 21 10 C3   LD      HL,$C310        
475F: 09         ADD     HL,BC           
4760: 7E         LD      A,(HL)          
4761: E6 80      AND     $80             
4763: 28 04      JR      Z,$4769         
4765: 70         LD      (HL),B          
4766: CD 8D 3B   CALL    $3B8D           
4769: F0 E7      LD      A,($E7)         
476B: 1F         RRA                     
476C: 1F         RRA                     
476D: 1F         RRA                     
476E: 1F         RRA                     
476F: E6 01      AND     $01             
4771: CD 87 3B   CALL    $3B87           
4774: C9         RET                     
4775: CD 35 7D   CALL    $7D35           
4778: 7B         LD      A,E             
4779: C6 02      ADD     $02             
477B: E0 F1      LDFF00  ($F1),A         
477D: CD CE 47   CALL    $47CE           
4780: CD 76 7C   CALL    $7C76           
4783: CD 23 7C   CALL    $7C23           
4786: 30 05      JR      NC,$478D        
4788: 3E F6      LD      A,$F6           
478A: CD 85 21   CALL    $2185           
478D: C9         RET                     
478E: F0 00      LD      A,($00)         
4790: 70         LD      (HL),B          
4791: 00         NOP                     
4792: F0 08      LD      A,($08)         
4794: 72         LD      (HL),D          
4795: 00         NOP                     
4796: 00         NOP                     
4797: 00         NOP                     
4798: 74         LD      (HL),H          
4799: 00         NOP                     
479A: 00         NOP                     
479B: 08 76 00   LD      ($0076),SP      
479E: F0 00      LD      A,($00)         
47A0: 72         LD      (HL),D          
47A1: 20 F0      JR      NZ,$4793        
47A3: 08 70 20   LD      ($2070),SP      
47A6: 00         NOP                     
47A7: 00         NOP                     
47A8: 76         HALT                    
47A9: 20 00      JR      NZ,$47AB        
47AB: 08 74 20   LD      ($2074),SP      
47AE: F0 FF      LD      A,($FF)         
47B0: 72         LD      (HL),D          
47B1: 20 F0      JR      NZ,$47A3        
47B3: 07         RLCA                    
47B4: 70         LD      (HL),B          
47B5: 20 00      JR      NZ,$47B7        
47B7: 00         NOP                     
47B8: 7A         LD      A,D             
47B9: 20 00      JR      NZ,$47BB        
47BB: 08 78 20   LD      ($2078),SP      
47BE: F0 01      LD      A,($01)         
47C0: 70         LD      (HL),B          
47C1: 00         NOP                     
47C2: F0 09      LD      A,($09)         
47C4: 72         LD      (HL),D          
47C5: 00         NOP                     
47C6: 00         NOP                     
47C7: 00         NOP                     
47C8: 78         LD      A,B             
47C9: 00         NOP                     
47CA: 00         NOP                     
47CB: 08 7A 00   LD      ($007A),SP      
47CE: F0 F1      LD      A,($F1)         
47D0: 17         RLA                     
47D1: 17         RLA                     
47D2: 17         RLA                     
47D3: 17         RLA                     
47D4: E6 F0      AND     $F0             
47D6: 5F         LD      E,A             
47D7: 50         LD      D,B             
47D8: 21 8E 47   LD      HL,$478E        
47DB: 19         ADD     HL,DE           
47DC: 0E 04      LD      C,$04           
47DE: C3 26 3D   JP      $3D26           
47E1: 6E         LD      L,(HL)          
47E2: 20 6C      JR      NZ,$4850        
47E4: 20 6C      JR      NZ,$4852        
47E6: 00         NOP                     
47E7: 6E         LD      L,(HL)          
47E8: 00         NOP                     
47E9: 70         LD      (HL),B          
47EA: 00         NOP                     
47EB: 72         LD      (HL),D          
47EC: 00         NOP                     
47ED: 74         LD      (HL),H          
47EE: 00         NOP                     
47EF: 76         HALT                    
47F0: 00         NOP                     
47F1: 78         LD      A,B             
47F2: 00         NOP                     
47F3: 7A         LD      A,D             
47F4: 00         NOP                     
47F5: 7C         LD      A,H             
47F6: 00         NOP                     
47F7: 76         HALT                    
47F8: 00         NOP                     
47F9: 72         LD      (HL),D          
47FA: 20 70      JR      NZ,$486C        
47FC: 20 76      JR      NZ,$4874        
47FE: 20 74      JR      NZ,$4874        
4800: 20 7A      JR      NZ,$487C        
4802: 20 78      JR      NZ,$487C        
4804: 20 76      JR      NZ,$487C        
4806: 20 7C      JR      NZ,$4884        
4808: 20 7E      JR      NZ,$4888        
480A: 00         NOP                     
480B: 7E         LD      A,(HL)          
480C: 20 FA      JR      NZ,$4808        
480E: A5         AND     L               
480F: DB         ???                     
4810: A7         AND     A               
4811: 28 4A      JR      Z,$485D         
4813: FA 0E DB   LD      A,($DB0E)       
4816: FE 08      CP      $08             
4818: 30 08      JR      NC,$4822        
481A: FA 66 DB   LD      A,($DB66)       
481D: E6 02      AND     $02             
481F: C2 7C 7D   JP      NZ,$7D7C        
4822: 11 F9 47   LD      DE,$47F9        
4825: FA 0E DB   LD      A,($DB0E)       
4828: FE 08      CP      $08             
482A: 30 09      JR      NC,$4835        
482C: CD 35 7D   CALL    $7D35           
482F: 7B         LD      A,E             
4830: E0 F1      LDFF00  ($F1),A         
4832: 11 E1 47   LD      DE,$47E1        
4835: CD 3B 3C   CALL    $3C3B           
4838: F0 E7      LD      A,($E7)         
483A: 1F         RRA                     
483B: 1F         RRA                     
483C: 1F         RRA                     
483D: 1F         RRA                     
483E: E6 01      AND     $01             
4840: CD 87 3B   CALL    $3B87           
4843: CD D0 7B   CALL    $7BD0           
4846: CD 23 7C   CALL    $7C23           
4849: 30 11      JR      NC,$485C        
484B: FA 0E DB   LD      A,($DB0E)       
484E: FE 08      CP      $08             
4850: 30 05      JR      NC,$4857        
4852: 3E 27      LD      A,$27           
4854: C3 97 21   JP      $2197           
4857: 3E 76      LD      A,$76           
4859: CD 85 21   CALL    $2185           
485C: C9         RET                     
485D: F0 F8      LD      A,($F8)         
485F: E6 20      AND     $20             
4861: C2 7C 7D   JP      NZ,$7D7C        
4864: 11 E9 47   LD      DE,$47E9        
4867: 21 80 C3   LD      HL,$C380        
486A: 09         ADD     HL,BC           
486B: 7E         LD      A,(HL)          
486C: A7         AND     A               
486D: 20 03      JR      NZ,$4872        
486F: 11 F9 47   LD      DE,$47F9        
4872: CD 3B 3C   CALL    $3C3B           
4875: FA 0E DB   LD      A,($DB0E)       
4878: FE 08      CP      $08             
487A: 30 18      JR      NC,$4894        
487C: F0 EE      LD      A,($EE)         
487E: C6 10      ADD     $10             
4880: E0 EE      LDFF00  ($EE),A         
4882: F0 EC      LD      A,($EC)         
4884: D6 10      SUB     $10             
4886: E0 EC      LDFF00  ($EC),A         
4888: AF         XOR     A               
4889: E0 F1      LDFF00  ($F1),A         
488B: 11 09 48   LD      DE,$4809        
488E: CD 3B 3C   CALL    $3C3B           
4891: CD BA 3D   CALL    $3DBA           
4894: CD 76 7C   CALL    $7C76           
4897: CD D0 7B   CALL    $7BD0           
489A: F0 F0      LD      A,($F0)         
489C: C7         RST     0X00            
489D: A7         AND     A               
489E: 48         LD      C,B             
489F: E4         ???                     
48A0: 48         LD      C,B             
48A1: 09         ADD     HL,BC           
48A2: 49         LD      C,C             
48A3: 3E 49      LD      A,$49           
48A5: 4B         LD      C,E             
48A6: 49         LD      C,C             
48A7: CD 35 7D   CALL    $7D35           
48AA: 21 80 C3   LD      HL,$C380        
48AD: 09         ADD     HL,BC           
48AE: 73         LD      (HL),E          
48AF: C6 24      ADD     $24             
48B1: FE 48      CP      $48             
48B3: 30 24      JR      NC,$48D9        
48B5: CD 45 7D   CALL    $7D45           
48B8: C6 24      ADD     $24             
48BA: FE 48      CP      $48             
48BC: 30 1B      JR      NC,$48D9        
48BE: CD 23 7C   CALL    $7C23           
48C1: 30 11      JR      NC,$48D4        
48C3: FA 0E DB   LD      A,($DB0E)       
48C6: FE 07      CP      $07             
48C8: 3E 70      LD      A,$70           
48CA: 28 02      JR      Z,$48CE         
48CC: 3E 77      LD      A,$77           
48CE: CD 85 21   CALL    $2185           
48D1: CD 8D 3B   CALL    $3B8D           
48D4: AF         XOR     A               
48D5: CD 87 3B   CALL    $3B87           
48D8: C9         RET                     
48D9: F0 E7      LD      A,($E7)         
48DB: 1F         RRA                     
48DC: 1F         RRA                     
48DD: 1F         RRA                     
48DE: E6 01      AND     $01             
48E0: CD 87 3B   CALL    $3B87           
48E3: C9         RET                     
48E4: FA 77 C1   LD      A,($C177)       
48E7: A7         AND     A               
48E8: 20 15      JR      NZ,$48FF        
48EA: FA 0E DB   LD      A,($DB0E)       
48ED: FE 07      CP      $07             
48EF: 20 0E      JR      NZ,$48FF        
48F1: 3E 72      LD      A,$72           
48F3: CD 85 21   CALL    $2185           
48F6: CD 8D 3B   CALL    $3B8D           
48F9: CD 91 08   CALL    $0891           
48FC: 36 C0      LD      (HL),$C0        
48FE: C9         RET                     
48FF: 3E 71      LD      A,$71           
4901: CD 85 21   CALL    $2185           
4904: CD 8D 3B   CALL    $3B8D           
4907: 70         LD      (HL),B          
4908: C9         RET                     
4909: FA 9F C1   LD      A,($C19F)       
490C: A7         AND     A               
490D: 20 22      JR      NZ,$4931        
490F: CD 91 08   CALL    $0891           
4912: 20 14      JR      NZ,$4928        
4914: EA 0B C1   LD      ($C10B),A       
4917: 3E 73      LD      A,$73           
4919: CD 85 21   CALL    $2185           
491C: 3E 08      LD      A,$08           
491E: EA 0E DB   LD      ($DB0E),A       
4921: 3E 0D      LD      A,$0D           
4923: E0 A5      LDFF00  ($A5),A         
4925: C3 8D 3B   JP      $3B8D           
4928: 3E 02      LD      A,$02           
492A: E0 A1      LDFF00  ($A1),A         
492C: 3E 01      LD      A,$01           
492E: EA 0B C1   LD      ($C10B),A       
4931: F0 E7      LD      A,($E7)         
4933: 1F         RRA                     
4934: 1F         RRA                     
4935: 1F         RRA                     
4936: E6 01      AND     $01             
4938: C6 02      ADD     $02             
493A: CD 87 3B   CALL    $3B87           
493D: C9         RET                     
493E: FA 9F C1   LD      A,($C19F)       
4941: A7         AND     A               
4942: 20 06      JR      NZ,$494A        
4944: CD 98 08   CALL    $0898           
4947: CD 8D 3B   CALL    $3B8D           
494A: C9         RET                     
494B: CD 31 49   CALL    $4931           
494E: CD 23 7C   CALL    $7C23           
4951: 30 05      JR      NC,$4958        
4953: 3E 75      LD      A,$75           
4955: CD 85 21   CALL    $2185           
4958: C9         RET                     
4959: FA 00 70   LD      A,($7000)       
495C: 00         NOP                     
495D: FA 08 72   LD      A,($7208)       
4960: 00         NOP                     
4961: FA 10 74   LD      A,($7410)       
4964: 00         NOP                     
4965: FA 18 70   LD      A,($7018)       
4968: 20 0A      JR      NZ,$4974        
496A: 00         NOP                     
496B: 76         HALT                    
496C: 00         NOP                     
496D: 0A         LD      A,(BC)          
496E: 08 78 00   LD      ($0078),SP      
4971: 0A         LD      A,(BC)          
4972: 10 78      STOP    $78             
4974: 20 0A      JR      NZ,$4980        
4976: 18 76      JR      $49EE           
4978: 20 FA      JR      NZ,$4974        
497A: 00         NOP                     
497B: 70         LD      (HL),B          
497C: 00         NOP                     
497D: FA 08 74   LD      A,($7408)       
4980: 20 FA      JR      NZ,$497C        
4982: 10 72      STOP    $72             
4984: 20 FA      JR      NZ,$4980        
4986: 18 70      JR      $49F8           
4988: 20 0A      JR      NZ,$4994        
498A: 00         NOP                     
498B: 76         HALT                    
498C: 00         NOP                     
498D: 0A         LD      A,(BC)          
498E: 08 78 00   LD      ($0078),SP      
4991: 0A         LD      A,(BC)          
4992: 10 78      STOP    $78             
4994: 20 0A      JR      NZ,$49A0        
4996: 18 76      JR      $4A0E           
4998: 20 7E      JR      NZ,$4A18        
499A: 00         NOP                     
499B: 7A         LD      A,D             
499C: 00         NOP                     
499D: 7C         LD      A,H             
499E: 00         NOP                     
499F: 7C         LD      A,H             
49A0: 20 7A      JR      NZ,$4A1C        
49A2: 20 AF      JR      NZ,$4953        
49A4: E0 F1      LDFF00  ($F1),A         
49A6: 3E 4A      LD      A,$4A           
49A8: E0 EC      LDFF00  ($EC),A         
49AA: 11 9B 49   LD      DE,$499B        
49AD: CD 3B 3C   CALL    $3C3B           
49B0: 3E 68      LD      A,$68           
49B2: E0 EE      LDFF00  ($EE),A         
49B4: 11 9F 49   LD      DE,$499F        
49B7: CD 3B 3C   CALL    $3C3B           
49BA: FA 0E DB   LD      A,($DB0E)       
49BD: FE 06      CP      $06             
49BF: 20 0E      JR      NZ,$49CF        
49C1: 3E 74      LD      A,$74           
49C3: E0 EE      LDFF00  ($EE),A         
49C5: 3E 38      LD      A,$38           
49C7: E0 EC      LDFF00  ($EC),A         
49C9: 11 99 49   LD      DE,$4999        
49CC: CD D0 3C   CALL    $3CD0           
49CF: CD BA 3D   CALL    $3DBA           
49D2: 21 B0 C3   LD      HL,$C3B0        
49D5: 09         ADD     HL,BC           
49D6: 7E         LD      A,(HL)          
49D7: 21 59 49   LD      HL,$4959        
49DA: A7         AND     A               
49DB: 28 03      JR      Z,$49E0         
49DD: 21 79 49   LD      HL,$4979        
49E0: 0E 08      LD      C,$08           
49E2: CD 26 3D   CALL    $3D26           
49E5: 3E 06      LD      A,$06           
49E7: CD D0 3D   CALL    $3DD0           
49EA: AF         XOR     A               
49EB: CD 87 3B   CALL    $3B87           
49EE: CD 76 7C   CALL    $7C76           
49F1: F0 E7      LD      A,($E7)         
49F3: E6 20      AND     $20             
49F5: CD 87 3B   CALL    $3B87           
49F8: CD D0 7B   CALL    $7BD0           
49FB: F0 F0      LD      A,($F0)         
49FD: C7         RST     0X00            
49FE: 04         INC     B               
49FF: 4A         LD      C,D             
4A00: 39         ADD     HL,SP           
4A01: 4A         LD      C,D             
4A02: 61         LD      H,C             
4A03: 4A         LD      C,D             
4A04: CD 16 7C   CALL    $7C16           
4A07: 30 2F      JR      NC,$4A38        
4A09: 1E D3      LD      E,$D3           
4A0B: FA FD D8   LD      A,($D8FD)       
4A0E: E6 30      AND     $30             
4A10: 20 22      JR      NZ,$4A34        
4A12: FA 0E DB   LD      A,($DB0E)       
4A15: FE 06      CP      $06             
4A17: 20 08      JR      NZ,$4A21        
4A19: 3E CF      LD      A,$CF           
4A1B: CD 74 4A   CALL    $4A74           
4A1E: C3 8D 3B   JP      $3B8D           
4A21: 1E D4      LD      E,$D4           
4A23: FA 73 DB   LD      A,($DB73)       
4A26: A7         AND     A               
4A27: 20 0B      JR      NZ,$4A34        
4A29: 1E CE      LD      E,$CE           
4A2B: FA 0E DB   LD      A,($DB0E)       
4A2E: FE 07      CP      $07             
4A30: 20 02      JR      NZ,$4A34        
4A32: 1E D2      LD      E,$D2           
4A34: 7B         LD      A,E             
4A35: CD 74 4A   CALL    $4A74           
4A38: C9         RET                     
4A39: FA 9F C1   LD      A,($C19F)       
4A3C: A7         AND     A               
4A3D: 20 21      JR      NZ,$4A60        
4A3F: CD 8D 3B   CALL    $3B8D           
4A42: FA 77 C1   LD      A,($C177)       
4A45: A7         AND     A               
4A46: 28 07      JR      Z,$4A4F         
4A48: 70         LD      (HL),B          
4A49: 3E D1      LD      A,$D1           
4A4B: CD 74 4A   CALL    $4A74           
4A4E: C9         RET                     
4A4F: 3E 07      LD      A,$07           
4A51: EA 0E DB   LD      ($DB0E),A       
4A54: 3E 0D      LD      A,$0D           
4A56: E0 A5      LDFF00  ($A5),A         
4A58: CD 98 08   CALL    $0898           
4A5B: CD 91 08   CALL    $0891           
4A5E: 36 70      LD      (HL),$70        
4A60: C9         RET                     
4A61: CD 91 08   CALL    $0891           
4A64: 20 0D      JR      NZ,$4A73        
4A66: FA 9F C1   LD      A,($C19F)       
4A69: A7         AND     A               
4A6A: 20 07      JR      NZ,$4A73        
4A6C: CD 32 4A   CALL    $4A32           
4A6F: CD 8D 3B   CALL    $3B8D           
4A72: 70         LD      (HL),B          
4A73: C9         RET                     
4A74: 5F         LD      E,A             
4A75: F0 99      LD      A,($99)         
4A77: F5         PUSH    AF              
4A78: 3E 10      LD      A,$10           
4A7A: E0 99      LDFF00  ($99),A         
4A7C: 7B         LD      A,E             
4A7D: CD 85 21   CALL    $2185           
4A80: F1         POP     AF              
4A81: E0 99      LDFF00  ($99),A         
4A83: C9         RET                     
4A84: 70         LD      (HL),B          
4A85: 00         NOP                     
4A86: 70         LD      (HL),B          
4A87: 20 F0      JR      NZ,$4A79        
4A89: F8 E6      LDHL    SP,$E6          
4A8B: 20 C2      JR      NZ,$4A4F        
4A8D: 7C         LD      A,H             
4A8E: 7D         LD      A,L             
4A8F: 21 40 C4   LD      HL,$C440        
4A92: 09         ADD     HL,BC           
4A93: 7E         LD      A,(HL)          
4A94: A7         AND     A               
4A95: C2 79 4B   JP      NZ,$4B79        
4A98: 79         LD      A,C             
4A99: EA 01 D2   LD      ($D201),A       
4A9C: CD 91 08   CALL    $0891           
4A9F: E6 20      AND     $20             
4AA1: 28 04      JR      Z,$4AA7         
4AA3: 21 EE FF   LD      HL,$FFEE        
4AA6: 35         DEC     (HL)            
4AA7: 11 84 4A   LD      DE,$4A84        
4AAA: CD 3B 3C   CALL    $3C3B           
4AAD: CD 76 7C   CALL    $7C76           
4AB0: F0 F0      LD      A,($F0)         
4AB2: C7         RST     0X00            
4AB3: BD         CP      L               
4AB4: 4A         LD      C,D             
4AB5: 10 4B      STOP    $4B             
4AB7: 18 4B      JR      $4B04           
4AB9: 3E 4B      LD      A,$4B           
4ABB: 3F         CCF                     
4ABC: 4B         LD      C,E             
4ABD: FA 7F DB   LD      A,($DB7F)       
4AC0: FE 02      CP      $02             
4AC2: 20 14      JR      NZ,$4AD8        
4AC4: 21 10 C2   LD      HL,$C210        
4AC7: 09         ADD     HL,BC           
4AC8: 7E         LD      A,(HL)          
4AC9: C6 10      ADD     $10             
4ACB: 77         LD      (HL),A          
4ACC: 21 10 C3   LD      HL,$C310        
4ACF: 09         ADD     HL,BC           
4AD0: 36 10      LD      (HL),$10        
4AD2: CD 8D 3B   CALL    $3B8D           
4AD5: 36 04      LD      (HL),$04        
4AD7: C9         RET                     
4AD8: AF         XOR     A               
4AD9: EA 02 D2   LD      ($D202),A       
4ADC: CD 8D 3B   CALL    $3B8D           
4ADF: 3E B3      LD      A,$B3           
4AE1: CD 01 3C   CALL    $3C01           
4AE4: 38 28      JR      C,$4B0E         
4AE6: F0 D7      LD      A,($D7)         
4AE8: 21 00 C2   LD      HL,$C200        
4AEB: 19         ADD     HL,DE           
4AEC: 77         LD      (HL),A          
4AED: F0 D8      LD      A,($D8)         
4AEF: 21 10 C2   LD      HL,$C210        
4AF2: 19         ADD     HL,DE           
4AF3: 77         LD      (HL),A          
4AF4: 21 40 C4   LD      HL,$C440        
4AF7: 19         ADD     HL,DE           
4AF8: 36 01      LD      (HL),$01        
4AFA: 21 40 C2   LD      HL,$C240        
4AFD: 19         ADD     HL,DE           
4AFE: 36 0E      LD      (HL),$0E        
4B00: 21 40 C3   LD      HL,$C340        
4B03: 19         ADD     HL,DE           
4B04: 36 C1      LD      (HL),$C1        
4B06: 21 50 C3   LD      HL,$C350        
4B09: 19         ADD     HL,DE           
4B0A: 36 00      LD      (HL),$00        
4B0C: A7         AND     A               
4B0D: C9         RET                     
4B0E: 37         SCF                     
4B0F: C9         RET                     
4B10: FA 02 D2   LD      A,($D202)       
4B13: A7         AND     A               
4B14: C2 8D 3B   JP      NZ,$3B8D        
4B17: C9         RET                     
4B18: 21 D0 C3   LD      HL,$C3D0        
4B1B: 09         ADD     HL,BC           
4B1C: 7E         LD      A,(HL)          
4B1D: FE 05      CP      $05             
4B1F: CA 8D 3B   JP      Z,$3B8D         
4B22: F0 E7      LD      A,($E7)         
4B24: E6 07      AND     $07             
4B26: 20 15      JR      NZ,$4B3D        
4B28: CD DF 4A   CALL    $4ADF           
4B2B: 38 10      JR      C,$4B3D         
4B2D: 21 D0 C3   LD      HL,$C3D0        
4B30: 09         ADD     HL,BC           
4B31: 34         INC     (HL)            
4B32: 7E         LD      A,(HL)          
4B33: 21 D0 C3   LD      HL,$C3D0        
4B36: 19         ADD     HL,DE           
4B37: 77         LD      (HL),A          
4B38: 21 40 C2   LD      HL,$C240        
4B3B: 19         ADD     HL,DE           
4B3C: 70         LD      (HL),B          
4B3D: C9         RET                     
4B3E: C9         RET                     
4B3F: CD 91 08   CALL    $0891           
4B42: 20 30      JR      NZ,$4B74        
4B44: CD 1B 7D   CALL    $7D1B           
4B47: 21 20 C3   LD      HL,$C320        
4B4A: 09         ADD     HL,BC           
4B4B: 35         DEC     (HL)            
4B4C: 35         DEC     (HL)            
4B4D: 21 10 C3   LD      HL,$C310        
4B50: 09         ADD     HL,BC           
4B51: 7E         LD      A,(HL)          
4B52: E6 80      AND     $80             
4B54: 28 1E      JR      Z,$4B74         
4B56: 70         LD      (HL),B          
4B57: 21 20 C3   LD      HL,$C320        
4B5A: 09         ADD     HL,BC           
4B5B: 70         LD      (HL),B          
4B5C: CD D5 3B   CALL    $3BD5           
4B5F: 30 13      JR      NC,$4B74        
4B61: AF         XOR     A               
4B62: EA 7F DB   LD      ($DB7F),A       
4B65: 3E 06      LD      A,$06           
4B67: EA 0E DB   LD      ($DB0E),A       
4B6A: 3E 0D      LD      A,$0D           
4B6C: E0 A5      LDFF00  ($A5),A         
4B6E: CD 98 08   CALL    $0898           
4B71: CD 7C 7D   CALL    $7D7C           
4B74: C9         RET                     
4B75: 72         LD      (HL),D          
4B76: 00         NOP                     
4B77: 72         LD      (HL),D          
4B78: 40         LD      B,B             
4B79: 11 75 4B   LD      DE,$4B75        
4B7C: CD D0 3C   CALL    $3CD0           
4B7F: F0 E7      LD      A,($E7)         
4B81: 1F         RRA                     
4B82: 1F         RRA                     
4B83: E6 01      AND     $01             
4B85: CD 87 3B   CALL    $3B87           
4B88: CD 76 7C   CALL    $7C76           
4B8B: F0 F0      LD      A,($F0)         
4B8D: C7         RST     0X00            
4B8E: 9A         SBC     D               
4B8F: 4B         LD      C,E             
4B90: 1B         DEC     DE              
4B91: 4C         LD      C,H             
4B92: 83         ADD     A,E             
4B93: 4C         LD      C,H             
4B94: 01 FF 10   LD      BC,$10FF        
4B97: F0 0B      LD      A,($0B)         
4B99: F5         PUSH    AF              
4B9A: F0 E7      LD      A,($E7)         
4B9C: E6 01      AND     $01             
4B9E: 20 40      JR      NZ,$4BE0        
4BA0: 21 B0 C2   LD      HL,$C2B0        
4BA3: 09         ADD     HL,BC           
4BA4: 5E         LD      E,(HL)          
4BA5: 50         LD      D,B             
4BA6: 21 94 4B   LD      HL,$4B94        
4BA9: 19         ADD     HL,DE           
4BAA: 7E         LD      A,(HL)          
4BAB: 21 40 C2   LD      HL,$C240        
4BAE: 09         ADD     HL,BC           
4BAF: 86         ADD     A,(HL)          
4BB0: 77         LD      (HL),A          
4BB1: 21 96 4B   LD      HL,$4B96        
4BB4: 19         ADD     HL,DE           
4BB5: BE         CP      (HL)            
4BB6: 20 08      JR      NZ,$4BC0        
4BB8: 21 B0 C2   LD      HL,$C2B0        
4BBB: 09         ADD     HL,BC           
4BBC: 7E         LD      A,(HL)          
4BBD: EE 01      XOR     $01             
4BBF: 77         LD      (HL),A          
4BC0: 21 C0 C2   LD      HL,$C2C0        
4BC3: 09         ADD     HL,BC           
4BC4: 5E         LD      E,(HL)          
4BC5: 50         LD      D,B             
4BC6: 21 94 4B   LD      HL,$4B94        
4BC9: 19         ADD     HL,DE           
4BCA: 7E         LD      A,(HL)          
4BCB: 21 50 C2   LD      HL,$C250        
4BCE: 09         ADD     HL,BC           
4BCF: 86         ADD     A,(HL)          
4BD0: 77         LD      (HL),A          
4BD1: 21 98 4B   LD      HL,$4B98        
4BD4: 19         ADD     HL,DE           
4BD5: BE         CP      (HL)            
4BD6: 20 08      JR      NZ,$4BE0        
4BD8: 21 C0 C2   LD      HL,$C2C0        
4BDB: 09         ADD     HL,BC           
4BDC: 7E         LD      A,(HL)          
4BDD: EE 01      XOR     $01             
4BDF: 77         LD      (HL),A          
4BE0: CD E2 7C   CALL    $7CE2           
4BE3: FA 02 D2   LD      A,($D202)       
4BE6: A7         AND     A               
4BE7: C2 8D 3B   JP      NZ,$3B8D        
4BEA: C9         RET                     
4BEB: F0 E8      LD      A,($E8)         
4BED: E8 E0      ADD     SP,$E0          
4BEF: E0 D8      LDFF00  ($D8),A         
4BF1: 10 18      STOP    $18             
4BF3: 18 20      JR      $4C15           
4BF5: 20 28      JR      NZ,$4C1F        
4BF7: 00         NOP                     
4BF8: F8 08      LDHL    SP,$08          
4BFA: F8 08      LDHL    SP,$08          
4BFC: 00         NOP                     
4BFD: 00         NOP                     
4BFE: 08 F8 08   LD      ($08F8),SP      
4C01: F8 00      LDHL    SP,$00          
4C03: 00         NOP                     
4C04: F8 08      LDHL    SP,$08          
4C06: F8 08      LDHL    SP,$08          
4C08: 00         NOP                     
4C09: 00         NOP                     
4C0A: 08 F8 08   LD      ($08F8),SP      
4C0D: F8 00      LDHL    SP,$00          
4C0F: 10 18      STOP    $18             
4C11: 18 20      JR      $4C33           
4C13: 20 28      JR      NZ,$4C3D        
4C15: F0 E8      LD      A,($E8)         
4C17: E8 E0      ADD     SP,$E0          
4C19: E0 D8      LDFF00  ($D8),A         
4C1B: 3E 22      LD      A,$22           
4C1D: E0 F2      LDFF00  ($F2),A         
4C1F: FA 04 D2   LD      A,($D204)       
4C22: 5F         LD      E,A             
4C23: 50         LD      D,B             
4C24: 21 80 C2   LD      HL,$C280        
4C27: 19         ADD     HL,DE           
4C28: 7E         LD      A,(HL)          
4C29: A7         AND     A               
4C2A: CA 7C 7D   JP      Z,$7D7C         
4C2D: F0 E7      LD      A,($E7)         
4C2F: E6 07      AND     $07             
4C31: 21 D0 C3   LD      HL,$C3D0        
4C34: 09         ADD     HL,BC           
4C35: BE         CP      (HL)            
4C36: 20 47      JR      NZ,$4C7F        
4C38: FA 04 D2   LD      A,($D204)       
4C3B: 5F         LD      E,A             
4C3C: 50         LD      D,B             
4C3D: 21 80 C3   LD      HL,$C380        
4C40: 19         ADD     HL,DE           
4C41: 7E         LD      A,(HL)          
4C42: 5F         LD      E,A             
4C43: 21 D0 C3   LD      HL,$C3D0        
4C46: 09         ADD     HL,BC           
4C47: 17         RLA                     
4C48: 17         RLA                     
4C49: E6 FC      AND     $FC             
4C4B: 83         ADD     A,E             
4C4C: 83         ADD     A,E             
4C4D: 86         ADD     A,(HL)          
4C4E: 5F         LD      E,A             
4C4F: 50         LD      D,B             
4C50: F0 98      LD      A,($98)         
4C52: F5         PUSH    AF              
4C53: F0 99      LD      A,($99)         
4C55: F5         PUSH    AF              
4C56: C5         PUSH    BC              
4C57: FA 04 D2   LD      A,($D204)       
4C5A: 4F         LD      C,A             
4C5B: 21 EB 4B   LD      HL,$4BEB        
4C5E: 19         ADD     HL,DE           
4C5F: 7E         LD      A,(HL)          
4C60: 21 00 C2   LD      HL,$C200        
4C63: 09         ADD     HL,BC           
4C64: 86         ADD     A,(HL)          
4C65: E0 98      LDFF00  ($98),A         
4C67: 21 03 4C   LD      HL,$4C03        
4C6A: 19         ADD     HL,DE           
4C6B: 7E         LD      A,(HL)          
4C6C: 21 10 C2   LD      HL,$C210        
4C6F: 09         ADD     HL,BC           
4C70: 86         ADD     A,(HL)          
4C71: E0 99      LDFF00  ($99),A         
4C73: C1         POP     BC              
4C74: 3E 24      LD      A,$24           
4C76: CD 25 3C   CALL    $3C25           
4C79: F1         POP     AF              
4C7A: E0 99      LDFF00  ($99),A         
4C7C: F1         POP     AF              
4C7D: E0 98      LDFF00  ($98),A         
4C7F: CD E2 7C   CALL    $7CE2           
4C82: C9         RET                     
4C83: C9         RET                     
4C84: 5A         LD      E,D             
4C85: 20 58      JR      NZ,$4CDF        
4C87: 20 5E      JR      NZ,$4CE7        
4C89: 20 5C      JR      NZ,$4CE7        
4C8B: 20 58      JR      NZ,$4CE5        
4C8D: 00         NOP                     
4C8E: 5A         LD      E,D             
4C8F: 00         NOP                     
4C90: 5C         LD      E,H             
4C91: 00         NOP                     
4C92: 5E         LD      E,(HL)          
4C93: 00         NOP                     
4C94: 54         LD      D,H             
4C95: 00         NOP                     
4C96: 56         LD      D,(HL)          
4C97: 00         NOP                     
4C98: 56         LD      D,(HL)          
4C99: 20 54      JR      NZ,$4CEF        
4C9B: 20 50      JR      NZ,$4CED        
4C9D: 00         NOP                     
4C9E: 52         LD      D,D             
4C9F: 00         NOP                     
4CA0: 52         LD      D,D             
4CA1: 20 50      JR      NZ,$4CF3        
4CA3: 20 74      JR      NZ,$4D19        
4CA5: 00         NOP                     
4CA6: 76         HALT                    
4CA7: 00         NOP                     
4CA8: 79         LD      A,C             
4CA9: EA 04 D2   LD      ($D204),A       
4CAC: F0 F8      LD      A,($F8)         
4CAE: E6 40      AND     $40             
4CB0: C2 7C 7D   JP      NZ,$7D7C        
4CB3: FA 67 DB   LD      A,($DB67)       
4CB6: E6 02      AND     $02             
4CB8: CA 7C 7D   JP      Z,$7D7C         
4CBB: 11 84 4C   LD      DE,$4C84        
4CBE: CD 3B 3C   CALL    $3C3B           
4CC1: CD 76 7C   CALL    $7C76           
4CC4: CD 1B 7D   CALL    $7D1B           
4CC7: 21 20 C3   LD      HL,$C320        
4CCA: 09         ADD     HL,BC           
4CCB: 35         DEC     (HL)            
4CCC: 35         DEC     (HL)            
4CCD: 21 10 C3   LD      HL,$C310        
4CD0: 09         ADD     HL,BC           
4CD1: 7E         LD      A,(HL)          
4CD2: E6 80      AND     $80             
4CD4: 28 06      JR      Z,$4CDC         
4CD6: 70         LD      (HL),B          
4CD7: 21 20 C3   LD      HL,$C320        
4CDA: 09         ADD     HL,BC           
4CDB: 70         LD      (HL),B          
4CDC: F0 F0      LD      A,($F0)         
4CDE: C7         RST     0X00            
4CDF: ED         ???                     
4CE0: 4C         LD      C,H             
4CE1: 0F         RRCA                    
4CE2: 4D         LD      C,L             
4CE3: 46         LD      B,(HL)          
4CE4: 4D         LD      C,L             
4CE5: BA         CP      D               
4CE6: 4D         LD      C,L             
4CE7: 43         LD      B,E             
4CE8: 4E         LD      C,(HL)          
4CE9: AA         XOR     D               
4CEA: 4E         LD      C,(HL)          
4CEB: DA 4E 3E   JP      C,$3E4E         
4CEE: 02         LD      (BC),A          
4CEF: CD 87 3B   CALL    $3B87           
4CF2: 21 00 C2   LD      HL,$C200        
4CF5: 09         ADD     HL,BC           
4CF6: 36 60      LD      (HL),$60        
4CF8: 21 10 C2   LD      HL,$C210        
4CFB: 09         ADD     HL,BC           
4CFC: 36 58      LD      (HL),$58        
4CFE: CD D0 7B   CALL    $7BD0           
4D01: CD 23 7C   CALL    $7C23           
4D04: 30 08      JR      NC,$4D0E        
4D06: 3E C0      LD      A,$C0           
4D08: CD 85 21   CALL    $2185           
4D0B: CD 8D 3B   CALL    $3B8D           
4D0E: C9         RET                     
4D0F: CD D0 7B   CALL    $7BD0           
4D12: FA 9F C1   LD      A,($C19F)       
4D15: A7         AND     A               
4D16: 20 25      JR      NZ,$4D3D        
4D18: FA 77 C1   LD      A,($C177)       
4D1B: A7         AND     A               
4D1C: 20 16      JR      NZ,$4D34        
4D1E: 3E 02      LD      A,$02           
4D20: EA 7F DB   LD      ($DB7F),A       
4D23: 21 87 D8   LD      HL,$D887        
4D26: CB F6      SET     1,E             
4D28: CD 91 08   CALL    $0891           
4D2B: 36 A0      LD      (HL),$A0        
4D2D: 3E 01      LD      A,$01           
4D2F: E0 F2      LDFF00  ($F2),A         
4D31: C3 8D 3B   JP      $3B8D           
4D34: 3E C2      LD      A,$C2           
4D36: CD 85 21   CALL    $2185           
4D39: CD 8D 3B   CALL    $3B8D           
4D3C: 70         LD      (HL),B          
4D3D: C9         RET                     
4D3E: 78         LD      A,B             
4D3F: 00         NOP                     
4D40: FF         RST     0X38            
4D41: 00         NOP                     
4D42: 7A         LD      A,D             
4D43: 00         NOP                     
4D44: 7C         LD      A,H             
4D45: 00         NOP                     
4D46: 3E 01      LD      A,$01           
4D48: E0 A1      LDFF00  ($A1),A         
4D4A: EA 67 C1   LD      ($C167),A       
4D4D: CD 91 08   CALL    $0891           
4D50: FE 30      CP      $30             
4D52: 38 18      JR      C,$4D6C         
4D54: AF         XOR     A               
4D55: E0 F1      LDFF00  ($F1),A         
4D57: F0 EC      LD      A,($EC)         
4D59: D6 10      SUB     $10             
4D5B: E0 EC      LDFF00  ($EC),A         
4D5D: 11 3E 4D   LD      DE,$4D3E        
4D60: CD 3B 3C   CALL    $3C3B           
4D63: CD BA 3D   CALL    $3DBA           
4D66: 3E 08      LD      A,$08           
4D68: CD 87 3B   CALL    $3B87           
4D6B: C9         RET                     
4D6C: FE 18      CP      $18             
4D6E: 30 28      JR      NC,$4D98        
4D70: 3E 02      LD      A,$02           
4D72: E0 9E      LDFF00  ($9E),A         
4D74: 21 40 C2   LD      HL,$C240        
4D77: 09         ADD     HL,BC           
4D78: 36 FE      LD      (HL),$FE        
4D7A: 21 50 C2   LD      HL,$C250        
4D7D: 09         ADD     HL,BC           
4D7E: 36 F4      LD      (HL),$F4        
4D80: CD E2 7C   CALL    $7CE2           
4D83: CD 91 08   CALL    $0891           
4D86: 20 10      JR      NZ,$4D98        
4D88: 3E 34      LD      A,$34           
4D8A: EA 68 D3   LD      ($D368),A       
4D8D: E0 B0      LDFF00  ($B0),A         
4D8F: CD 91 08   CALL    $0891           
4D92: 36 C0      LD      (HL),$C0        
4D94: CD 8D 3B   CALL    $3B8D           
4D97: C9         RET                     
4D98: 3E 01      LD      A,$01           
4D9A: E0 F1      LDFF00  ($F1),A         
4D9C: F0 EE      LD      A,($EE)         
4D9E: D6 0C      SUB     $0C             
4DA0: E0 EE      LDFF00  ($EE),A         
4DA2: 11 3E 4D   LD      DE,$4D3E        
4DA5: CD 3B 3C   CALL    $3C3B           
4DA8: CD BA 3D   CALL    $3DBA           
4DAB: CD 91 08   CALL    $0891           
4DAE: 1F         RRA                     
4DAF: 1F         RRA                     
4DB0: 1F         RRA                     
4DB1: 1F         RRA                     
4DB2: E6 01      AND     $01             
4DB4: C6 02      ADD     $02             
4DB6: CD 87 3B   CALL    $3B87           
4DB9: C9         RET                     
4DBA: 3E 01      LD      A,$01           
4DBC: E0 A1      LDFF00  ($A1),A         
4DBE: CD 91 08   CALL    $0891           
4DC1: 20 05      JR      NZ,$4DC8        
4DC3: 36 0C      LD      (HL),$0C        
4DC5: CD 8D 3B   CALL    $3B8D           
4DC8: CD 91 08   CALL    $0891           
4DCB: FE 20      CP      $20             
4DCD: 20 0A      JR      NZ,$4DD9        
4DCF: 21 20 C3   LD      HL,$C320        
4DD2: 09         ADD     HL,BC           
4DD3: 36 18      LD      (HL),$18        
4DD5: CD 44 72   CALL    $7244           
4DD8: AF         XOR     A               
4DD9: FE 60      CP      $60             
4DDB: 20 04      JR      NZ,$4DE1        
4DDD: 21 02 D2   LD      HL,$D202        
4DE0: 34         INC     (HL)            
4DE1: FE A0      CP      $A0             
4DE3: 20 0B      JR      NZ,$4DF0        
4DE5: FA 01 D2   LD      A,($D201)       
4DE8: 5F         LD      E,A             
4DE9: 50         LD      D,B             
4DEA: 21 E0 C2   LD      HL,$C2E0        
4DED: 19         ADD     HL,DE           
4DEE: 36 A0      LD      (HL),$A0        
4DF0: E6 20      AND     $20             
4DF2: 28 12      JR      Z,$4E06         
4DF4: 3E 01      LD      A,$01           
4DF6: E0 F1      LDFF00  ($F1),A         
4DF8: F0 EE      LD      A,($EE)         
4DFA: D6 0E      SUB     $0E             
4DFC: E0 EE      LDFF00  ($EE),A         
4DFE: F0 EC      LD      A,($EC)         
4E00: D6 08      SUB     $08             
4E02: E0 EC      LDFF00  ($EC),A         
4E04: 18 09      JR      $4E0F           
4E06: AF         XOR     A               
4E07: E0 F1      LDFF00  ($F1),A         
4E09: F0 EC      LD      A,($EC)         
4E0B: D6 10      SUB     $10             
4E0D: E0 EC      LDFF00  ($EC),A         
4E0F: 11 3E 4D   LD      DE,$4D3E        
4E12: CD 3B 3C   CALL    $3C3B           
4E15: CD BA 3D   CALL    $3DBA           
4E18: CD 91 08   CALL    $0891           
4E1B: 1E 02      LD      E,$02           
4E1D: E6 20      AND     $20             
4E1F: 28 01      JR      Z,$4E22         
4E21: 1C         INC     E               
4E22: 7B         LD      A,E             
4E23: CD 87 3B   CALL    $3B87           
4E26: C9         RET                     
4E27: 20 00      JR      NZ,$4E29        
4E29: E0 00      LDFF00  ($00),A         
4E2B: 00         NOP                     
4E2C: E0 00      LDFF00  ($00),A         
4E2E: 20 00      JR      NZ,$4E30        
4E30: 02         LD      (BC),A          
4E31: 01 03 16   LD      BC,$1603        
4E34: 28 28      JR      Z,$4E5E         
4E36: 28 28      JR      Z,$4E60         
4E38: 28 28      JR      Z,$4E62         
4E3A: 28 28      JR      Z,$4E64         
4E3C: 28 28      JR      Z,$4E66         
4E3E: 28 00      JR      Z,$4E40         
4E40: 02         LD      (BC),A          
4E41: 04         INC     B               
4E42: 06 3E      LD      B,$3E           
4E44: 01 E0 A1   LD      BC,$A1E0        
4E47: CD 91 08   CALL    $0891           
4E4A: 20 17      JR      NZ,$4E63        
4E4C: 21 D0 C3   LD      HL,$C3D0        
4E4F: 09         ADD     HL,BC           
4E50: 7E         LD      A,(HL)          
4E51: 3C         INC     A               
4E52: 77         LD      (HL),A          
4E53: FE 0B      CP      $0B             
4E55: CA 8D 3B   JP      Z,$3B8D         
4E58: 5F         LD      E,A             
4E59: 50         LD      D,B             
4E5A: 21 32 4E   LD      HL,$4E32        
4E5D: 19         ADD     HL,DE           
4E5E: 5E         LD      E,(HL)          
4E5F: CD 91 08   CALL    $0891           
4E62: 73         LD      (HL),E          
4E63: 21 D0 C3   LD      HL,$C3D0        
4E66: 09         ADD     HL,BC           
4E67: 7E         LD      A,(HL)          
4E68: E6 03      AND     $03             
4E6A: 5F         LD      E,A             
4E6B: 50         LD      D,B             
4E6C: 21 27 4E   LD      HL,$4E27        
4E6F: 19         ADD     HL,DE           
4E70: 7E         LD      A,(HL)          
4E71: 21 40 C2   LD      HL,$C240        
4E74: 09         ADD     HL,BC           
4E75: 77         LD      (HL),A          
4E76: 21 2B 4E   LD      HL,$4E2B        
4E79: 19         ADD     HL,DE           
4E7A: 7E         LD      A,(HL)          
4E7B: 21 50 C2   LD      HL,$C250        
4E7E: 09         ADD     HL,BC           
4E7F: 77         LD      (HL),A          
4E80: 21 2F 4E   LD      HL,$4E2F        
4E83: 19         ADD     HL,DE           
4E84: 7E         LD      A,(HL)          
4E85: 21 80 C3   LD      HL,$C380        
4E88: 09         ADD     HL,BC           
4E89: 77         LD      (HL),A          
4E8A: CD 55 7D   CALL    $7D55           
4E8D: 7B         LD      A,E             
4E8E: EE 01      XOR     $01             
4E90: E0 9E      LDFF00  ($9E),A         
4E92: CD E2 7C   CALL    $7CE2           
4E95: 21 80 C3   LD      HL,$C380        
4E98: 09         ADD     HL,BC           
4E99: 5E         LD      E,(HL)          
4E9A: 50         LD      D,B             
4E9B: 21 3F 4E   LD      HL,$4E3F        
4E9E: 19         ADD     HL,DE           
4E9F: F0 E7      LD      A,($E7)         
4EA1: 1F         RRA                     
4EA2: 1F         RRA                     
4EA3: 1F         RRA                     
4EA4: E6 01      AND     $01             
4EA6: B6         OR      (HL)            
4EA7: C3 87 3B   JP      $3B87           
4EAA: 3E 01      LD      A,$01           
4EAC: E0 A1      LDFF00  ($A1),A         
4EAE: 21 80 C3   LD      HL,$C380        
4EB1: 09         ADD     HL,BC           
4EB2: 3E 01      LD      A,$01           
4EB4: 77         LD      (HL),A          
4EB5: 21 40 C2   LD      HL,$C240        
4EB8: 09         ADD     HL,BC           
4EB9: 36 E4      LD      (HL),$E4        
4EBB: 21 50 C2   LD      HL,$C250        
4EBE: 09         ADD     HL,BC           
4EBF: 36 08      LD      (HL),$08        
4EC1: CD E2 7C   CALL    $7CE2           
4EC4: F0 EE      LD      A,($EE)         
4EC6: FE C0      CP      $C0             
4EC8: 38 0C      JR      C,$4ED6         
4ECA: FE C4      CP      $C4             
4ECC: D2 D6 4E   JP      NC,$4ED6        
4ECF: AF         XOR     A               
4ED0: EA 67 C1   LD      ($C167),A       
4ED3: CD 8D 3B   CALL    $3B8D           
4ED6: 3E 01      LD      A,$01           
4ED8: 18 B6      JR      $4E90           
4EDA: FA 01 D2   LD      A,($D201)       
4EDD: 5F         LD      E,A             
4EDE: 50         LD      D,B             
4EDF: 21 90 C2   LD      HL,$C290        
4EE2: 19         ADD     HL,DE           
4EE3: 34         INC     (HL)            
4EE4: 21 E0 C2   LD      HL,$C2E0        
4EE7: 19         ADD     HL,DE           
4EE8: 36 50      LD      (HL),$50        
4EEA: 21 10 C2   LD      HL,$C210        
4EED: 19         ADD     HL,DE           
4EEE: 7E         LD      A,(HL)          
4EEF: C6 10      ADD     $10             
4EF1: 77         LD      (HL),A          
4EF2: 21 10 C3   LD      HL,$C310        
4EF5: 19         ADD     HL,DE           
4EF6: 36 10      LD      (HL),$10        
4EF8: C3 7C 7D   JP      $7D7C           
4EFB: 40         LD      B,B             
4EFC: 00         NOP                     
4EFD: 40         LD      B,B             
4EFE: 20 42      JR      NZ,$4F42        
4F00: 00         NOP                     
4F01: 42         LD      B,D             
4F02: 20 11      JR      NZ,$4F15        
4F04: FB         EI                      
4F05: 4E         LD      C,(HL)          
4F06: CD 3B 3C   CALL    $3C3B           
4F09: CD 76 7C   CALL    $7C76           
4F0C: F0 E7      LD      A,($E7)         
4F0E: 1F         RRA                     
4F0F: 1F         RRA                     
4F10: 1F         RRA                     
4F11: 1F         RRA                     
4F12: E6 01      AND     $01             
4F14: CD 87 3B   CALL    $3B87           
4F17: F0 F0      LD      A,($F0)         
4F19: C7         RST     0X00            
4F1A: 26 4F      LD      H,$4F           
4F1C: 74         LD      (HL),H          
4F1D: 4F         LD      C,A             
4F1E: 08 F8 00   LD      ($00F8),SP      
4F21: 00         NOP                     
4F22: 00         NOP                     
4F23: 00         NOP                     
4F24: F8 08      LDHL    SP,$08          
4F26: CD D0 7B   CALL    $7BD0           
4F29: 30 3B      JR      NC,$4F66        
4F2B: F0 CB      LD      A,($CB)         
4F2D: E6 0F      AND     $0F             
4F2F: 28 35      JR      Z,$4F66         
4F31: 3E 01      LD      A,$01           
4F33: EA 44 C1   LD      ($C144),A       
4F36: 21 D0 C3   LD      HL,$C3D0        
4F39: 09         ADD     HL,BC           
4F3A: 7E         LD      A,(HL)          
4F3B: 3C         INC     A               
4F3C: 77         LD      (HL),A          
4F3D: FE 10      CP      $10             
4F3F: 20 2A      JR      NZ,$4F6B        
4F41: CD 8D 3B   CALL    $3B8D           
4F44: CD 55 7D   CALL    $7D55           
4F47: 21 80 C3   LD      HL,$C380        
4F4A: 09         ADD     HL,BC           
4F4B: 7B         LD      A,E             
4F4C: EE 01      XOR     $01             
4F4E: 5F         LD      E,A             
4F4F: 73         LD      (HL),E          
4F50: 50         LD      D,B             
4F51: 21 1E 4F   LD      HL,$4F1E        
4F54: 19         ADD     HL,DE           
4F55: 7E         LD      A,(HL)          
4F56: 21 40 C2   LD      HL,$C240        
4F59: 09         ADD     HL,BC           
4F5A: 77         LD      (HL),A          
4F5B: 21 22 4F   LD      HL,$4F22        
4F5E: 19         ADD     HL,DE           
4F5F: 7E         LD      A,(HL)          
4F60: 21 50 C2   LD      HL,$C250        
4F63: 09         ADD     HL,BC           
4F64: 77         LD      (HL),A          
4F65: C9         RET                     
4F66: 21 D0 C3   LD      HL,$C3D0        
4F69: 09         ADD     HL,BC           
4F6A: 70         LD      (HL),B          
4F6B: C9         RET                     
4F6C: 10 F0      STOP    $F0             
4F6E: 00         NOP                     
4F6F: 00         NOP                     
4F70: 00         NOP                     
4F71: 00         NOP                     
4F72: F0 10      LD      A,($10)         
4F74: 3E 01      LD      A,$01           
4F76: E0 A1      LDFF00  ($A1),A         
4F78: 3E 3E      LD      A,$3E           
4F7A: E0 F2      LDFF00  ($F2),A         
4F7C: F0 CC      LD      A,($CC)         
4F7E: E6 0F      AND     $0F             
4F80: 57         LD      D,A             
4F81: 28 1F      JR      Z,$4FA2         
4F83: E6 03      AND     $03             
4F85: 28 09      JR      Z,$4F90         
4F87: 1E 00      LD      E,$00           
4F89: E6 01      AND     $01             
4F8B: 20 01      JR      NZ,$4F8E        
4F8D: 1C         INC     E               
4F8E: 18 07      JR      $4F97           
4F90: 1E 02      LD      E,$02           
4F92: CB 52      SET     1,E             
4F94: 20 01      JR      NZ,$4F97        
4F96: 1C         INC     E               
4F97: 21 80 C3   LD      HL,$C380        
4F9A: 09         ADD     HL,BC           
4F9B: 7E         LD      A,(HL)          
4F9C: AB         XOR     E               
4F9D: FE 01      CP      $01             
4F9F: 28 01      JR      Z,$4FA2         
4FA1: 73         LD      (HL),E          
4FA2: CD E2 7C   CALL    $7CE2           
4FA5: 21 00 C2   LD      HL,$C200        
4FA8: 09         ADD     HL,BC           
4FA9: 7E         LD      A,(HL)          
4FAA: D6 08      SUB     $08             
4FAC: 21 10 C2   LD      HL,$C210        
4FAF: 09         ADD     HL,BC           
4FB0: B6         OR      (HL)            
4FB1: E6 0F      AND     $0F             
4FB3: C2 86 50   JP      NZ,$5086        
4FB6: 7E         LD      A,(HL)          
4FB7: D6 10      SUB     $10             
4FB9: E0 CD      LDFF00  ($CD),A         
4FBB: 21 00 C2   LD      HL,$C200        
4FBE: 09         ADD     HL,BC           
4FBF: 7E         LD      A,(HL)          
4FC0: D6 08      SUB     $08             
4FC2: E0 CE      LDFF00  ($CE),A         
4FC4: CB 37      SET     1,E             
4FC6: E6 0F      AND     $0F             
4FC8: 5F         LD      E,A             
4FC9: F0 CD      LD      A,($CD)         
4FCB: E6 F0      AND     $F0             
4FCD: B3         OR      E               
4FCE: 5F         LD      E,A             
4FCF: 50         LD      D,B             
4FD0: 21 11 D7   LD      HL,$D711        
4FD3: 19         ADD     HL,DE           
4FD4: 36 0D      LD      (HL),$0D        
4FD6: CD 39 28   CALL    $2839           
4FD9: 21 01 D6   LD      HL,$D601        
4FDC: FA 00 D6   LD      A,($D600)       
4FDF: 5F         LD      E,A             
4FE0: C6 0A      ADD     $0A             
4FE2: EA 00 D6   LD      ($D600),A       
4FE5: 16 00      LD      D,$00           
4FE7: 19         ADD     HL,DE           
4FE8: F0 CF      LD      A,($CF)         
4FEA: 22         LD      (HLI),A         
4FEB: F0 D0      LD      A,($D0)         
4FED: 22         LD      (HLI),A         
4FEE: 3E 81      LD      A,$81           
4FF0: 22         LD      (HLI),A         
4FF1: 3E 10      LD      A,$10           
4FF3: 22         LD      (HLI),A         
4FF4: 3E 12      LD      A,$12           
4FF6: 22         LD      (HLI),A         
4FF7: F0 CF      LD      A,($CF)         
4FF9: 22         LD      (HLI),A         
4FFA: F0 D0      LD      A,($D0)         
4FFC: 3C         INC     A               
4FFD: 22         LD      (HLI),A         
4FFE: 3E 81      LD      A,$81           
5000: 22         LD      (HLI),A         
5001: 3E 11      LD      A,$11           
5003: 22         LD      (HLI),A         
5004: 3E 13      LD      A,$13           
5006: 22         LD      (HLI),A         
5007: 70         LD      (HL),B          
5008: 21 80 C3   LD      HL,$C380        
500B: 09         ADD     HL,BC           
500C: 5E         LD      E,(HL)          
500D: CD 50 4F   CALL    $4F50           
5010: 21 80 C3   LD      HL,$C380        
5013: 09         ADD     HL,BC           
5014: 5E         LD      E,(HL)          
5015: 50         LD      D,B             
5016: 21 6C 4F   LD      HL,$4F6C        
5019: 19         ADD     HL,DE           
501A: F0 CE      LD      A,($CE)         
501C: 86         ADD     A,(HL)          
501D: CB 37      SET     1,E             
501F: E6 0F      AND     $0F             
5021: F5         PUSH    AF              
5022: 21 70 4F   LD      HL,$4F70        
5025: 19         ADD     HL,DE           
5026: F1         POP     AF              
5027: 5F         LD      E,A             
5028: F0 CD      LD      A,($CD)         
502A: 86         ADD     A,(HL)          
502B: E6 F0      AND     $F0             
502D: B3         OR      E               
502E: 5F         LD      E,A             
502F: 50         LD      D,B             
5030: 21 11 D7   LD      HL,$D711        
5033: 19         ADD     HL,DE           
5034: 5E         LD      E,(HL)          
5035: 16 01      LD      D,$01           
5037: CD DB 29   CALL    $29DB           
503A: FE 0B      CP      $0B             
503C: 28 48      JR      Z,$5086         
503E: FE 50      CP      $50             
5040: 28 44      JR      Z,$5086         
5042: FE 51      CP      $51             
5044: 28 40      JR      Z,$5086         
5046: F0 EE      LD      A,($EE)         
5048: E0 D7      LDFF00  ($D7),A         
504A: F0 EC      LD      A,($EC)         
504C: E0 D8      LDFF00  ($D8),A         
504E: 3E 2F      LD      A,$2F           
5050: E0 F2      LDFF00  ($F2),A         
5052: 3E 02      LD      A,$02           
5054: CD 53 09   CALL    $0953           
5057: 21 20 C5   LD      HL,$C520        
505A: 19         ADD     HL,DE           
505B: 36 0F      LD      (HL),$0F        
505D: CD 7C 7D   CALL    $7D7C           
5060: FA 8E C1   LD      A,($C18E)       
5063: E6 0F      AND     $0F             
5065: FE 0E      CP      $0E             
5067: 20 1D      JR      NZ,$5086        
5069: C5         PUSH    BC              
506A: 48         LD      C,B             
506B: 21 00 D7   LD      HL,$D700        
506E: 2A         LD      A,(HLI)         
506F: E5         PUSH    HL              
5070: 5F         LD      E,A             
5071: 16 01      LD      D,$01           
5073: CD DB 29   CALL    $29DB           
5076: E1         POP     HL              
5077: FE 50      CP      $50             
5079: 28 0A      JR      Z,$5085         
507B: FE 51      CP      $51             
507D: 28 06      JR      Z,$5085         
507F: 0D         DEC     C               
5080: 20 EC      JR      NZ,$506E        
5082: CD EC 08   CALL    $08EC           
5085: C1         POP     BC              
5086: C9         RET                     
5087: 00         NOP                     
5088: 00         NOP                     
5089: 01 01 01   LD      BC,$0101        
508C: 02         LD      (BC),A          
508D: 02         LD      (BC),A          
508E: 02         LD      (BC),A          
508F: 00         NOP                     
5090: 00         NOP                     
5091: 0F         RRCA                    
5092: 0F         RRCA                    
5093: 0F         RRCA                    
5094: 0E 0E      LD      C,$0E           
5096: 0E 08      LD      C,$08           
5098: 08 07 07   LD      ($0707),SP      
509B: 07         RLCA                    
509C: 06 06      LD      B,$06           
509E: 06 08      LD      B,$08           
50A0: 08 09 09   LD      ($0909),SP      
50A3: 09         ADD     HL,BC           
50A4: 0A         LD      A,(BC)          
50A5: 0A         LD      A,(BC)          
50A6: 0A         LD      A,(BC)          
50A7: 04         INC     B               
50A8: 04         INC     B               
50A9: 03         INC     BC              
50AA: 03         INC     BC              
50AB: 03         INC     BC              
50AC: 02         LD      (BC),A          
50AD: 02         LD      (BC),A          
50AE: 02         LD      (BC),A          
50AF: 0C         INC     C               
50B0: 0C         INC     C               
50B1: 0D         DEC     C               
50B2: 0D         DEC     C               
50B3: 0D         DEC     C               
50B4: 0E 0E      LD      C,$0E           
50B6: 0E 04      LD      C,$04           
50B8: 04         INC     B               
50B9: 05         DEC     B               
50BA: 05         DEC     B               
50BB: 05         DEC     B               
50BC: 06 06      LD      B,$06           
50BE: 06 0C      LD      B,$0C           
50C0: 0C         INC     C               
50C1: 0B         DEC     BC              
50C2: 0B         DEC     BC              
50C3: 0B         DEC     BC              
50C4: 0A         LD      A,(BC)          
50C5: 0A         LD      A,(BC)          
50C6: 0A         LD      A,(BC)          
50C7: F0 D7      LD      A,($D7)         
50C9: 07         RLCA                    
50CA: E6 01      AND     $01             
50CC: 5F         LD      E,A             
50CD: F0 D8      LD      A,($D8)         
50CF: 07         RLCA                    
50D0: 17         RLA                     
50D1: E6 02      AND     $02             
50D3: B3         OR      E               
50D4: 17         RLA                     
50D5: 17         RLA                     
50D6: 17         RLA                     
50D7: E6 18      AND     $18             
50D9: 67         LD      H,A             
50DA: F0 D8      LD      A,($D8)         
50DC: CB 7F      SET     1,E             
50DE: 28 02      JR      Z,$50E2         
50E0: 2F         CPL                     
50E1: 3C         INC     A               
50E2: 57         LD      D,A             
50E3: F0 D7      LD      A,($D7)         
50E5: CB 7F      SET     1,E             
50E7: 28 02      JR      Z,$50EB         
50E9: 2F         CPL                     
50EA: 3C         INC     A               
50EB: BA         CP      D               
50EC: 30 0D      JR      NC,$50FB        
50EE: CB 2F      SET     1,E             
50F0: CB 2F      SET     1,E             
50F2: 84         ADD     A,H             
50F3: 5F         LD      E,A             
50F4: 50         LD      D,B             
50F5: 21 87 50   LD      HL,$5087        
50F8: 19         ADD     HL,DE           
50F9: 7E         LD      A,(HL)          
50FA: C9         RET                     
50FB: 7A         LD      A,D             
50FC: CB 2F      SET     1,E             
50FE: CB 2F      SET     1,E             
5100: 84         ADD     A,H             
5101: 5F         LD      E,A             
5102: 50         LD      D,B             
5103: 21 A7 50   LD      HL,$50A7        
5106: 19         ADD     HL,DE           
5107: 7E         LD      A,(HL)          
5108: C9         RET                     
5109: 21 70 C4   LD      HL,$C470        
510C: 09         ADD     HL,BC           
510D: 70         LD      (HL),B          
510E: 21 F0 C3   LD      HL,$C3F0        
5111: 09         ADD     HL,BC           
5112: 70         LD      (HL),B          
5113: 21 00 C4   LD      HL,$C400        
5116: 09         ADD     HL,BC           
5117: 70         LD      (HL),B          
5118: CD 40 52   CALL    $5240           
511B: CD 76 7C   CALL    $7C76           
511E: CD E2 08   CALL    $08E2           
5121: F0 F0      LD      A,($F0)         
5123: C7         RST     0X00            
5124: 30 51      JR      NC,$5177        
5126: 42         LD      B,D             
5127: 51         LD      D,C             
5128: 6C         LD      L,H             
5129: 51         LD      D,C             
512A: A7         AND     A               
512B: 51         LD      D,C             
512C: B8         CP      B               
512D: 51         LD      D,C             
512E: C4 51 F0   CALL    NZ,$F051        
5131: EE 21      XOR     $21             
5133: B0         OR      B               
5134: C2 09 77   JP      NZ,$7709        
5137: F0 EF      LD      A,($EF)         
5139: 21 C0 C2   LD      HL,$C2C0        
513C: 09         ADD     HL,BC           
513D: 77         LD      (HL),A          
513E: CD 8D 3B   CALL    $3B8D           
5141: C9         RET                     
5142: CD 91 08   CALL    $0891           
5145: 20 20      JR      NZ,$5167        
5147: 21 40 C3   LD      HL,$C340        
514A: 09         ADD     HL,BC           
514B: CB F6      SET     1,E             
514D: CD 35 7D   CALL    $7D35           
5150: C6 20      ADD     $20             
5152: FE 40      CP      $40             
5154: 30 11      JR      NC,$5167        
5156: CD 45 7D   CALL    $7D45           
5159: C6 20      ADD     $20             
515B: FE 40      CP      $40             
515D: 30 08      JR      NC,$5167        
515F: CD 91 08   CALL    $0891           
5162: 36 30      LD      (HL),$30        
5164: CD 8D 3B   CALL    $3B8D           
5167: AF         XOR     A               
5168: CD 87 3B   CALL    $3B87           
516B: C9         RET                     
516C: CD 91 08   CALL    $0891           
516F: 20 16      JR      NZ,$5187        
5171: 21 D0 C2   LD      HL,$C2D0        
5174: 09         ADD     HL,BC           
5175: 7E         LD      A,(HL)          
5176: CD 87 3B   CALL    $3B87           
5179: CD 91 08   CALL    $0891           
517C: 36 18      LD      (HL),$18        
517E: 21 40 C3   LD      HL,$C340        
5181: 09         ADD     HL,BC           
5182: CB B6      SET     1,E             
5184: C3 8D 3B   JP      $3B8D           
5187: FE 10      CP      $10             
5189: 20 16      JR      NZ,$51A1        
518B: 3E 1F      LD      A,$1F           
518D: CD 25 3C   CALL    $3C25           
5190: CD C7 50   CALL    $50C7           
5193: CB 2F      SET     1,E             
5195: C6 02      ADD     $02             
5197: 21 D0 C2   LD      HL,$C2D0        
519A: 09         ADD     HL,BC           
519B: 77         LD      (HL),A          
519C: 3E 18      LD      A,$18           
519E: CD 25 3C   CALL    $3C25           
51A1: 3E 01      LD      A,$01           
51A3: CD 87 3B   CALL    $3B87           
51A6: C9         RET                     
51A7: CD E2 7C   CALL    $7CE2           
51AA: CD 91 08   CALL    $0891           
51AD: 20 05      JR      NZ,$51B4        
51AF: 36 20      LD      (HL),$20        
51B1: CD 8D 3B   CALL    $3B8D           
51B4: CD B4 3B   CALL    $3BB4           
51B7: C9         RET                     
51B8: CD 91 08   CALL    $0891           
51BB: 20 03      JR      NZ,$51C0        
51BD: CD 8D 3B   CALL    $3B8D           
51C0: CD B4 3B   CALL    $3BB4           
51C3: C9         RET                     
51C4: F0 98      LD      A,($98)         
51C6: F5         PUSH    AF              
51C7: F0 99      LD      A,($99)         
51C9: F5         PUSH    AF              
51CA: 21 B0 C2   LD      HL,$C2B0        
51CD: 09         ADD     HL,BC           
51CE: 7E         LD      A,(HL)          
51CF: E0 98      LDFF00  ($98),A         
51D1: 21 C0 C2   LD      HL,$C2C0        
51D4: 09         ADD     HL,BC           
51D5: 7E         LD      A,(HL)          
51D6: E0 99      LDFF00  ($99),A         
51D8: 3E 10      LD      A,$10           
51DA: CD 25 3C   CALL    $3C25           
51DD: CD 35 7D   CALL    $7D35           
51E0: C6 02      ADD     $02             
51E2: FE 04      CP      $04             
51E4: 30 25      JR      NC,$520B        
51E6: CD 45 7D   CALL    $7D45           
51E9: C6 02      ADD     $02             
51EB: FE 04      CP      $04             
51ED: 30 1C      JR      NC,$520B        
51EF: 21 00 C2   LD      HL,$C200        
51F2: 09         ADD     HL,BC           
51F3: F0 98      LD      A,($98)         
51F5: 77         LD      (HL),A          
51F6: 21 10 C2   LD      HL,$C210        
51F9: 09         ADD     HL,BC           
51FA: F0 99      LD      A,($99)         
51FC: 77         LD      (HL),A          
51FD: AF         XOR     A               
51FE: CD 87 3B   CALL    $3B87           
5201: CD 8D 3B   CALL    $3B8D           
5204: 36 01      LD      (HL),$01        
5206: CD 91 08   CALL    $0891           
5209: 36 20      LD      (HL),$20        
520B: F1         POP     AF              
520C: E0 99      LDFF00  ($99),A         
520E: F1         POP     AF              
520F: E0 98      LDFF00  ($98),A         
5211: CD E2 7C   CALL    $7CE2           
5214: CD B4 3B   CALL    $3BB4           
5217: C9         RET                     
5218: FF         RST     0X38            
5219: 00         NOP                     
521A: FF         RST     0X38            
521B: 20 6C      JR      NZ,$5289        
521D: 00         NOP                     
521E: 6C         LD      L,H             
521F: 20 64      JR      NZ,$5285        
5221: 20 62      JR      NZ,$5285        
5223: 20 68      JR      NZ,$528D        
5225: 20 66      JR      NZ,$528D        
5227: 20 60      JR      NZ,$5289        
5229: 00         NOP                     
522A: 60         LD      H,B             
522B: 20 66      JR      NZ,$5293        
522D: 00         NOP                     
522E: 68         LD      L,B             
522F: 00         NOP                     
5230: 62         LD      H,D             
5231: 00         NOP                     
5232: 64         LD      H,H             
5233: 00         NOP                     
5234: 66         LD      H,(HL)          
5235: 40         LD      B,B             
5236: 68         LD      L,B             
5237: 40         LD      B,B             
5238: 60         LD      H,B             
5239: 40         LD      B,B             
523A: 60         LD      H,B             
523B: 60         LD      H,B             
523C: 68         LD      L,B             
523D: 60         LD      H,B             
523E: 66         LD      H,(HL)          
523F: 60         LD      H,B             
5240: 11 18 52   LD      DE,$5218        
5243: CD 3B 3C   CALL    $3C3B           
5246: F0 F0      LD      A,($F0)         
5248: FE 03      CP      $03             
524A: D8         RET     C               
524B: F0 EE      LD      A,($EE)         
524D: 21 B0 C2   LD      HL,$C2B0        
5250: 09         ADD     HL,BC           
5251: 96         SUB     (HL)            
5252: CB 2F      SET     1,E             
5254: CB 2F      SET     1,E             
5256: E0 D7      LDFF00  ($D7),A         
5258: E0 D9      LDFF00  ($D9),A         
525A: F0 EC      LD      A,($EC)         
525C: 21 C0 C2   LD      HL,$C2C0        
525F: 09         ADD     HL,BC           
5260: 96         SUB     (HL)            
5261: CB 2F      SET     1,E             
5263: CB 2F      SET     1,E             
5265: E0 D8      LDFF00  ($D8),A         
5267: E0 DA      LDFF00  ($DA),A         
5269: FA C0 C3   LD      A,($C3C0)       
526C: 5F         LD      E,A             
526D: 16 00      LD      D,$00           
526F: 21 30 C0   LD      HL,$C030        
5272: 19         ADD     HL,DE           
5273: E5         PUSH    HL              
5274: D1         POP     DE              
5275: 3E 03      LD      A,$03           
5277: E0 DB      LDFF00  ($DB),A         
5279: 21 C0 C2   LD      HL,$C2C0        
527C: 09         ADD     HL,BC           
527D: F0 D8      LD      A,($D8)         
527F: 86         ADD     A,(HL)          
5280: 12         LD      (DE),A          
5281: 13         INC     DE              
5282: 21 B0 C2   LD      HL,$C2B0        
5285: 09         ADD     HL,BC           
5286: F0 D7      LD      A,($D7)         
5288: 86         ADD     A,(HL)          
5289: C6 04      ADD     $04             
528B: 12         LD      (DE),A          
528C: 13         INC     DE              
528D: 3E 6A      LD      A,$6A           
528F: 12         LD      (DE),A          
5290: 13         INC     DE              
5291: 3E 00      LD      A,$00           
5293: 12         LD      (DE),A          
5294: 13         INC     DE              
5295: F0 D7      LD      A,($D7)         
5297: 21 D9 FF   LD      HL,$FFD9        
529A: 86         ADD     A,(HL)          
529B: E0 D7      LDFF00  ($D7),A         
529D: F0 D8      LD      A,($D8)         
529F: 21 DA FF   LD      HL,$FFDA        
52A2: 86         ADD     A,(HL)          
52A3: E0 D8      LDFF00  ($D8),A         
52A5: F0 DB      LD      A,($DB)         
52A7: 3D         DEC     A               
52A8: 20 CD      JR      NZ,$5277        
52AA: 3E 03      LD      A,$03           
52AC: CD D0 3D   CALL    $3DD0           
52AF: C9         RET                     
52B0: 44         LD      B,H             
52B1: 29         ADD     HL,HL           
52B2: 82         ADD     A,D             
52B3: CB 64      SET     1,E             
52B5: C1         POP     BC              
52B6: D0         RET     NC              
52B7: 74         LD      (HL),H          
52B8: 6A         LD      L,D             
52B9: 36 5E      LD      (HL),$5E        
52BB: EC         ???                     
52BC: F5         PUSH    AF              
52BD: 9D         SBC     L               
52BE: 9A         SBC     D               
52BF: 10 9C      STOP    $9C             
52C1: 10 74      STOP    $74             
52C3: 00         NOP                     
52C4: 76         HALT                    
52C5: 00         NOP                     
52C6: FA A5 DB   LD      A,($DBA5)       
52C9: A7         AND     A               
52CA: 20 18      JR      NZ,$52E4        
52CC: F0 F6      LD      A,($F6)         
52CE: FE 6B      CP      $6B             
52D0: 28 0C      JR      Z,$52DE         
52D2: FE 7A      CP      $7A             
52D4: 28 08      JR      Z,$52DE         
52D6: FE 8B      CP      $8B             
52D8: 28 04      JR      Z,$52DE         
52DA: FE 7B      CP      $7B             
52DC: 20 06      JR      NZ,$52E4        
52DE: FA 7B D8   LD      A,($D87B)       
52E1: E6 10      AND     $10             
52E3: C8         RET     Z               
52E4: F0 F8      LD      A,($F8)         
52E6: E6 20      AND     $20             
52E8: C2 7C 7D   JP      NZ,$7D7C        
52EB: 11 C2 52   LD      DE,$52C2        
52EE: FA 0E DB   LD      A,($DB0E)       
52F1: FE 04      CP      $04             
52F3: 28 0E      JR      Z,$5303         
52F5: F0 F9      LD      A,($F9)         
52F7: A7         AND     A               
52F8: 28 06      JR      Z,$5300         
52FA: F0 EC      LD      A,($EC)         
52FC: C6 02      ADD     $02             
52FE: E0 EC      LDFF00  ($EC),A         
5300: 11 BE 52   LD      DE,$52BE        
5303: CD 3B 3C   CALL    $3C3B           
5306: CD 91 08   CALL    $0891           
5309: 20 1E      JR      NZ,$5329        
530B: CD D5 3B   CALL    $3BD5           
530E: 30 18      JR      NC,$5328        
5310: 3E 10      LD      A,$10           
5312: EA 68 D3   LD      ($D368),A       
5315: EA 67 C1   LD      ($C167),A       
5318: F0 BF      LD      A,($BF)         
531A: E0 B0      LDFF00  ($B0),A         
531C: CD 91 08   CALL    $0891           
531F: 3E 68      LD      A,$68           
5321: 77         LD      (HL),A          
5322: EA 11 C1   LD      ($C111),A       
5325: C3 3B 09   JP      $093B           
5328: C9         RET                     
5329: FE 10      CP      $10             
532B: 20 1C      JR      NZ,$5349        
532D: 35         DEC     (HL)            
532E: FA 0E DB   LD      A,($DB0E)       
5331: 5F         LD      E,A             
5332: 50         LD      D,B             
5333: 21 AF 52   LD      HL,$52AF        
5336: 19         ADD     HL,DE           
5337: 7E         LD      A,(HL)          
5338: FE 9D      CP      $9D             
533A: 28 04      JR      Z,$5340         
533C: FE 44      CP      $44             
533E: 20 05      JR      NZ,$5345        
5340: CD 97 21   CALL    $2197           
5343: 18 03      JR      $5348           
5345: CD 85 21   CALL    $2185           
5348: AF         XOR     A               
5349: 3D         DEC     A               
534A: 20 10      JR      NZ,$535C        
534C: AF         XOR     A               
534D: EA 7F DB   LD      ($DB7F),A       
5350: EA 67 C1   LD      ($C167),A       
5353: CD 9C 53   CALL    $539C           
5356: F6 20      OR      $20             
5358: 77         LD      (HL),A          
5359: C3 7C 7D   JP      $7D7C           
535C: F0 98      LD      A,($98)         
535E: 21 00 C2   LD      HL,$C200        
5361: 09         ADD     HL,BC           
5362: 77         LD      (HL),A          
5363: F0 F6      LD      A,($F6)         
5365: FE C9      CP      $C9             
5367: 20 05      JR      NZ,$536E        
5369: 3E 04      LD      A,$04           
536B: EA 3B C1   LD      ($C13B),A       
536E: 21 3B C1   LD      HL,$C13B        
5371: F0 99      LD      A,($99)         
5373: 86         ADD     A,(HL)          
5374: 21 10 C2   LD      HL,$C210        
5377: 09         ADD     HL,BC           
5378: D6 10      SUB     $10             
537A: 77         LD      (HL),A          
537B: F0 A2      LD      A,($A2)         
537D: 21 10 C3   LD      HL,$C310        
5380: 09         ADD     HL,BC           
5381: 77         LD      (HL),A          
5382: 3E 6C      LD      A,$6C           
5384: E0 9D      LDFF00  ($9D),A         
5386: 3E 02      LD      A,$02           
5388: E0 A1      LDFF00  ($A1),A         
538A: 3E 03      LD      A,$03           
538C: E0 9E      LDFF00  ($9E),A         
538E: AF         XOR     A               
538F: EA 37 C1   LD      ($C137),A       
5392: EA 6A C1   LD      ($C16A),A       
5395: EA 22 C1   LD      ($C122),A       
5398: EA 21 C1   LD      ($C121),A       
539B: C9         RET                     
539C: 21 00 D8   LD      HL,$D800        
539F: F0 F6      LD      A,($F6)         
53A1: 5F         LD      E,A             
53A2: FA A5 DB   LD      A,($DBA5)       
53A5: 57         LD      D,A             
53A6: F0 F7      LD      A,($F7)         
53A8: FE 1A      CP      $1A             
53AA: 30 05      JR      NC,$53B1        
53AC: FE 06      CP      $06             
53AE: 38 01      JR      C,$53B1         
53B0: 14         INC     D               
53B1: 19         ADD     HL,DE           
53B2: 7E         LD      A,(HL)          
53B3: C9         RET                     
53B4: 08 F8 00   LD      ($00F8),SP      
53B7: 00         NOP                     
53B8: 00         NOP                     
53B9: 00         NOP                     
53BA: F8 08      LDHL    SP,$08          
53BC: 50         LD      D,B             
53BD: 00         NOP                     
53BE: 50         LD      D,B             
53BF: 20 52      JR      NZ,$5413        
53C1: 00         NOP                     
53C2: 52         LD      D,D             
53C3: 20 50      JR      NZ,$5415        
53C5: 40         LD      B,B             
53C6: 50         LD      D,B             
53C7: 60         LD      H,B             
53C8: 52         LD      D,D             
53C9: 40         LD      B,B             
53CA: 52         LD      D,D             
53CB: 60         LD      H,B             
53CC: 54         LD      D,H             
53CD: 00         NOP                     
53CE: 56         LD      D,(HL)          
53CF: 00         NOP                     
53D0: 58         LD      E,B             
53D1: 00         NOP                     
53D2: 5A         LD      E,D             
53D3: 00         NOP                     
53D4: 56         LD      D,(HL)          
53D5: 20 54      JR      NZ,$542B        
53D7: 20 5A      JR      NZ,$5433        
53D9: 20 58      JR      NZ,$5433        
53DB: 20 11      JR      NZ,$53EE        
53DD: BC         CP      H               
53DE: 53         LD      D,E             
53DF: CD 3B 3C   CALL    $3C3B           
53E2: CD 97 55   CALL    $5597           
53E5: CD 76 7C   CALL    $7C76           
53E8: 21 10 C4   LD      HL,$C410        
53EB: 09         ADD     HL,BC           
53EC: 7E         LD      A,(HL)          
53ED: A7         AND     A               
53EE: 28 0E      JR      Z,$53FE         
53F0: 21 90 C2   LD      HL,$C290        
53F3: 09         ADD     HL,BC           
53F4: 3E 01      LD      A,$01           
53F6: 77         LD      (HL),A          
53F7: E0 F0      LDFF00  ($F0),A         
53F9: CD 91 08   CALL    $0891           
53FC: 36 40      LD      (HL),$40        
53FE: CD 98 7C   CALL    $7C98           
5401: CD E2 7C   CALL    $7CE2           
5404: CD 1B 7D   CALL    $7D1B           
5407: 21 20 C3   LD      HL,$C320        
540A: 09         ADD     HL,BC           
540B: 35         DEC     (HL)            
540C: 21 10 C3   LD      HL,$C310        
540F: 09         ADD     HL,BC           
5410: 7E         LD      A,(HL)          
5411: E6 80      AND     $80             
5413: E0 E8      LDFF00  ($E8),A         
5415: 28 0B      JR      Z,$5422         
5417: 70         LD      (HL),B          
5418: 21 20 C3   LD      HL,$C320        
541B: 09         ADD     HL,BC           
541C: 70         LD      (HL),B          
541D: 21 C0 C2   LD      HL,$C2C0        
5420: 09         ADD     HL,BC           
5421: 70         LD      (HL),B          
5422: CD 9E 3B   CALL    $3B9E           
5425: F0 F0      LD      A,($F0)         
5427: FE 02      CP      $02             
5429: CA 0C 55   JP      Z,$550C         
542C: A7         AND     A               
542D: 28 60      JR      Z,$548F         
542F: CD 91 08   CALL    $0891           
5432: 28 18      JR      Z,$544C         
5434: FE 0A      CP      $0A             
5436: 20 0E      JR      NZ,$5446        
5438: CD 55 7D   CALL    $7D55           
543B: 21 80 C3   LD      HL,$C380        
543E: 09         ADD     HL,BC           
543F: 7B         LD      A,E             
5440: BE         CP      (HL)            
5441: 20 03      JR      NZ,$5446        
5443: CD 42 55   CALL    $5542           
5446: CD AF 3D   CALL    $3DAF           
5449: C3 B1 54   JP      $54B1           
544C: CD ED 27   CALL    $27ED           
544F: E6 1F      AND     $1F             
5451: F6 20      OR      $20             
5453: 77         LD      (HL),A          
5454: 21 90 C2   LD      HL,$C290        
5457: 09         ADD     HL,BC           
5458: 36 00      LD      (HL),$00        
545A: 21 B0 C2   LD      HL,$C2B0        
545D: 09         ADD     HL,BC           
545E: 7E         LD      A,(HL)          
545F: 3C         INC     A               
5460: E6 03      AND     $03             
5462: 77         LD      (HL),A          
5463: FE 00      CP      $00             
5465: 20 05      JR      NZ,$546C        
5467: CD 55 7D   CALL    $7D55           
546A: 18 03      JR      $546F           
546C: CD ED 27   CALL    $27ED           
546F: E6 03      AND     $03             
5471: 21 80 C3   LD      HL,$C380        
5474: 09         ADD     HL,BC           
5475: 77         LD      (HL),A          
5476: 5F         LD      E,A             
5477: 50         LD      D,B             
5478: 21 B4 53   LD      HL,$53B4        
547B: 19         ADD     HL,DE           
547C: 7E         LD      A,(HL)          
547D: 21 40 C2   LD      HL,$C240        
5480: 09         ADD     HL,BC           
5481: 77         LD      (HL),A          
5482: 21 B8 53   LD      HL,$53B8        
5485: 19         ADD     HL,DE           
5486: 7E         LD      A,(HL)          
5487: 21 50 C2   LD      HL,$C250        
548A: 09         ADD     HL,BC           
548B: 77         LD      (HL),A          
548C: C3 B1 54   JP      $54B1           
548F: 21 A0 C2   LD      HL,$C2A0        
5492: 09         ADD     HL,BC           
5493: 7E         LD      A,(HL)          
5494: E6 0F      AND     $0F             
5496: 20 05      JR      NZ,$549D        
5498: CD 91 08   CALL    $0891           
549B: 20 11      JR      NZ,$54AE        
549D: CD ED 27   CALL    $27ED           
54A0: E6 0F      AND     $0F             
54A2: F6 10      OR      $10             
54A4: 77         LD      (HL),A          
54A5: 21 90 C2   LD      HL,$C290        
54A8: 09         ADD     HL,BC           
54A9: 36 01      LD      (HL),$01        
54AB: CD AF 3D   CALL    $3DAF           
54AE: CD FA 7B   CALL    $7BFA           
54B1: 21 00 C3   LD      HL,$C300        
54B4: 09         ADD     HL,BC           
54B5: 7E         LD      A,(HL)          
54B6: A7         AND     A               
54B7: 20 4F      JR      NZ,$5508        
54B9: CD 35 7D   CALL    $7D35           
54BC: C6 20      ADD     $20             
54BE: FE 40      CP      $40             
54C0: 30 46      JR      NC,$5508        
54C2: CD 45 7D   CALL    $7D45           
54C5: C6 20      ADD     $20             
54C7: FE 40      CP      $40             
54C9: 30 3D      JR      NC,$5508        
54CB: FA 00 DB   LD      A,($DB00)       
54CE: FE 01      CP      $01             
54D0: 20 08      JR      NZ,$54DA        
54D2: F0 CC      LD      A,($CC)         
54D4: E6 20      AND     $20             
54D6: 20 0F      JR      NZ,$54E7        
54D8: 18 2E      JR      $5508           
54DA: FA 01 DB   LD      A,($DB01)       
54DD: FE 01      CP      $01             
54DF: 20 27      JR      NZ,$5508        
54E1: F0 CC      LD      A,($CC)         
54E3: E6 10      AND     $10             
54E5: 28 21      JR      Z,$5508         
54E7: CD 55 7D   CALL    $7D55           
54EA: 21 80 C3   LD      HL,$C380        
54ED: 09         ADD     HL,BC           
54EE: 7E         LD      A,(HL)          
54EF: EE 01      XOR     $01             
54F1: BB         CP      E               
54F2: 28 14      JR      Z,$5508         
54F4: 21 20 C3   LD      HL,$C320        
54F7: 09         ADD     HL,BC           
54F8: 36 18      LD      (HL),$18        
54FA: 3E 10      LD      A,$10           
54FC: CD 25 3C   CALL    $3C25           
54FF: CD 8D 3B   CALL    $3B8D           
5502: 36 02      LD      (HL),$02        
5504: CD 44 72   CALL    $7244           
5507: C9         RET                     
5508: CD B4 3B   CALL    $3BB4           
550B: C9         RET                     
550C: F0 E7      LD      A,($E7)         
550E: 1F         RRA                     
550F: 1F         RRA                     
5510: E6 01      AND     $01             
5512: 21 C0 C2   LD      HL,$C2C0        
5515: 09         ADD     HL,BC           
5516: 77         LD      (HL),A          
5517: CD 55 7D   CALL    $7D55           
551A: 21 80 C3   LD      HL,$C380        
551D: 09         ADD     HL,BC           
551E: 73         LD      (HL),E          
551F: CD FA 7B   CALL    $7BFA           
5522: F0 E8      LD      A,($E8)         
5524: A7         AND     A               
5525: 28 0A      JR      Z,$5531         
5527: CD 8D 3B   CALL    $3B8D           
552A: 36 01      LD      (HL),$01        
552C: CD 91 08   CALL    $0891           
552F: 36 20      LD      (HL),$20        
5531: C9         RET                     
5532: 08 F8 00   LD      ($00F8),SP      
5535: 00         NOP                     
5536: 00         NOP                     
5537: 00         NOP                     
5538: F8 08      LDHL    SP,$08          
553A: 20 E0      JR      NZ,$551C        
553C: 00         NOP                     
553D: 00         NOP                     
553E: 00         NOP                     
553F: 00         NOP                     
5540: E0 20      LDFF00  ($20),A         
5542: 3E 0A      LD      A,$0A           
5544: CD 01 3C   CALL    $3C01           
5547: 38 3D      JR      C,$5586         
5549: C5         PUSH    BC              
554A: 21 B0 C3   LD      HL,$C3B0        
554D: 19         ADD     HL,DE           
554E: 36 01      LD      (HL),$01        
5550: F0 D9      LD      A,($D9)         
5552: 21 80 C3   LD      HL,$C380        
5555: 19         ADD     HL,DE           
5556: 77         LD      (HL),A          
5557: 4F         LD      C,A             
5558: 21 32 55   LD      HL,$5532        
555B: 09         ADD     HL,BC           
555C: F0 D7      LD      A,($D7)         
555E: 86         ADD     A,(HL)          
555F: 21 00 C2   LD      HL,$C200        
5562: 19         ADD     HL,DE           
5563: 77         LD      (HL),A          
5564: 21 36 55   LD      HL,$5536        
5567: 09         ADD     HL,BC           
5568: F0 D8      LD      A,($D8)         
556A: 86         ADD     A,(HL)          
556B: 21 10 C2   LD      HL,$C210        
556E: 19         ADD     HL,DE           
556F: 77         LD      (HL),A          
5570: 21 3A 55   LD      HL,$553A        
5573: 09         ADD     HL,BC           
5574: 7E         LD      A,(HL)          
5575: 21 40 C2   LD      HL,$C240        
5578: 19         ADD     HL,DE           
5579: 77         LD      (HL),A          
557A: 21 3E 55   LD      HL,$553E        
557D: 09         ADD     HL,BC           
557E: 7E         LD      A,(HL)          
557F: 21 50 C2   LD      HL,$C250        
5582: 19         ADD     HL,DE           
5583: 77         LD      (HL),A          
5584: C1         POP     BC              
5585: A7         AND     A               
5586: C9         RET                     
5587: 00         NOP                     
5588: FC         ???                     
5589: 22         LD      (HLI),A         
558A: 40         LD      B,B             
558B: 00         NOP                     
558C: 0C         INC     C               
558D: 22         LD      (HLI),A         
558E: 60         LD      H,B             
558F: 00         NOP                     
5590: FC         ???                     
5591: 22         LD      (HLI),A         
5592: 00         NOP                     
5593: 00         NOP                     
5594: 0C         INC     C               
5595: 22         LD      (HLI),A         
5596: 20 21      JR      NZ,$55B9        
5598: C0         RET     NZ              
5599: C2 09 7E   JP      NZ,$7E09        
559C: 17         RLA                     
559D: 17         RLA                     
559E: 17         RLA                     
559F: E6 F8      AND     $F8             
55A1: 5F         LD      E,A             
55A2: 50         LD      D,B             
55A3: 21 87 55   LD      HL,$5587        
55A6: 19         ADD     HL,DE           
55A7: 0E 02      LD      C,$02           
55A9: CD 26 3D   CALL    $3D26           
55AC: C9         RET                     
55AD: 78         LD      A,B             
55AE: 00         NOP                     
55AF: 72         LD      (HL),D          
55B0: 00         NOP                     
55B1: 7A         LD      A,D             
55B2: 00         NOP                     
55B3: 72         LD      (HL),D          
55B4: 00         NOP                     
55B5: 70         LD      (HL),B          
55B6: 00         NOP                     
55B7: 72         LD      (HL),D          
55B8: 00         NOP                     
55B9: 7C         LD      A,H             
55BA: 00         NOP                     
55BB: 7E         LD      A,(HL)          
55BC: 00         NOP                     
55BD: 74         LD      (HL),H          
55BE: 00         NOP                     
55BF: 76         HALT                    
55C0: 00         NOP                     
55C1: 72         LD      (HL),D          
55C2: 20 78      JR      NZ,$563C        
55C4: 20 72      JR      NZ,$5638        
55C6: 20 7A      JR      NZ,$5642        
55C8: 20 72      JR      NZ,$563C        
55CA: 20 70      JR      NZ,$563C        
55CC: 20 7E      JR      NZ,$564C        
55CE: 20 7C      JR      NZ,$564C        
55D0: 20 76      JR      NZ,$5648        
55D2: 20 74      JR      NZ,$5648        
55D4: 20 F0      JR      NZ,$55C6        
55D6: F8 E6      LDHL    SP,$E6          
55D8: 10 C2      STOP    $C2             
55DA: 7C         LD      A,H             
55DB: 7D         LD      A,L             
55DC: 11 AD 55   LD      DE,$55AD        
55DF: 21 80 C3   LD      HL,$C380        
55E2: 09         ADD     HL,BC           
55E3: 7E         LD      A,(HL)          
55E4: A7         AND     A               
55E5: 20 03      JR      NZ,$55EA        
55E7: 11 C1 55   LD      DE,$55C1        
55EA: CD 3B 3C   CALL    $3C3B           
55ED: 21 80 C4   LD      HL,$C480        
55F0: 09         ADD     HL,BC           
55F1: 7E         LD      A,(HL)          
55F2: A7         AND     A               
55F3: 28 12      JR      Z,$5607         
55F5: AF         XOR     A               
55F6: E0 F1      LDFF00  ($F1),A         
55F8: F0 EC      LD      A,($EC)         
55FA: D6 0E      SUB     $0E             
55FC: E0 EC      LDFF00  ($EC),A         
55FE: 11 E3 56   LD      DE,$56E3        
5601: CD 3B 3C   CALL    $3C3B           
5604: CD BA 3D   CALL    $3DBA           
5607: CD 76 7C   CALL    $7C76           
560A: CD 1B 7D   CALL    $7D1B           
560D: 21 20 C3   LD      HL,$C320        
5610: 09         ADD     HL,BC           
5611: 35         DEC     (HL)            
5612: 35         DEC     (HL)            
5613: 21 10 C3   LD      HL,$C310        
5616: 09         ADD     HL,BC           
5617: 7E         LD      A,(HL)          
5618: E6 80      AND     $80             
561A: E0 E8      LDFF00  ($E8),A         
561C: 28 06      JR      Z,$5624         
561E: 70         LD      (HL),B          
561F: 21 20 C3   LD      HL,$C320        
5622: 09         ADD     HL,BC           
5623: 70         LD      (HL),B          
5624: F0 F0      LD      A,($F0)         
5626: C7         RST     0X00            
5627: 3B         DEC     SP              
5628: 56         LD      D,(HL)          
5629: AE         XOR     (HL)            
562A: 56         LD      D,(HL)          
562B: CA 56 E7   JP      Z,$E756         
562E: 56         LD      D,(HL)          
562F: 2D         DEC     L               
5630: 57         LD      D,A             
5631: 26 58      LD      H,$58           
5633: A3         AND     E               
5634: 58         LD      E,B             
5635: E8 58      ADD     SP,$58          
5637: 5B         LD      E,E             
5638: 59         LD      E,C             
5639: 73         LD      (HL),E          
563A: 59         LD      E,C             
563B: FA 56 DB   LD      A,($DB56)       
563E: FE 01      CP      $01             
5640: 20 2F      JR      NZ,$5671        
5642: 21 20 C4   LD      HL,$C420        
5645: 09         ADD     HL,BC           
5646: 7E         LD      A,(HL)          
5647: A7         AND     A               
5648: 20 12      JR      NZ,$565C        
564A: CD 35 7D   CALL    $7D35           
564D: C6 18      ADD     $18             
564F: FE 30      CP      $30             
5651: 30 1D      JR      NC,$5670        
5653: CD 45 7D   CALL    $7D45           
5656: C6 18      ADD     $18             
5658: FE 30      CP      $30             
565A: 30 14      JR      NC,$5670        
565C: CD 91 08   CALL    $0891           
565F: 36 10      LD      (HL),$10        
5661: CD 8D 3B   CALL    $3B8D           
5664: 36 05      LD      (HL),$05        
5666: 3E 60      LD      A,$60           
5668: CD 85 21   CALL    $2185           
566B: 3E 14      LD      A,$14           
566D: EA AB C5   LD      ($C5AB),A       
5670: C9         RET                     
5671: CD D0 7B   CALL    $7BD0           
5674: CD 23 7C   CALL    $7C23           
5677: 30 15      JR      NC,$568E        
5679: FA 0E DB   LD      A,($DB0E)       
567C: FE 04      CP      $04             
567E: 20 09      JR      NZ,$5689        
5680: 3E 65      LD      A,$65           
5682: CD 68 56   CALL    $5668           
5685: CD 8D 3B   CALL    $3B8D           
5688: C9         RET                     
5689: 3E 61      LD      A,$61           
568B: CD 68 56   CALL    $5668           
568E: F0 E7      LD      A,($E7)         
5690: 1F         RRA                     
5691: 1F         RRA                     
5692: 1F         RRA                     
5693: E6 01      AND     $01             
5695: CD 87 3B   CALL    $3B87           
5698: F0 E7      LD      A,($E7)         
569A: E6 1F      AND     $1F             
569C: 20 0F      JR      NZ,$56AD        
569E: CD ED 27   CALL    $27ED           
56A1: E6 01      AND     $01             
56A3: 20 08      JR      NZ,$56AD        
56A5: 21 80 C3   LD      HL,$C380        
56A8: 09         ADD     HL,BC           
56A9: 7E         LD      A,(HL)          
56AA: EE 01      XOR     $01             
56AC: 77         LD      (HL),A          
56AD: C9         RET                     
56AE: FA 9F C1   LD      A,($C19F)       
56B1: A7         AND     A               
56B2: 20 15      JR      NZ,$56C9        
56B4: CD 8D 3B   CALL    $3B8D           
56B7: FA 77 C1   LD      A,($C177)       
56BA: A7         AND     A               
56BB: 20 06      JR      NZ,$56C3        
56BD: CD 91 08   CALL    $0891           
56C0: 36 10      LD      (HL),$10        
56C2: C9         RET                     
56C3: 70         LD      (HL),B          
56C4: 3E 61      LD      A,$61           
56C6: CD 68 56   CALL    $5668           
56C9: C9         RET                     
56CA: CD 91 08   CALL    $0891           
56CD: 20 0F      JR      NZ,$56DE        
56CF: 36 80      LD      (HL),$80        
56D1: 21 80 C4   LD      HL,$C480        
56D4: 09         ADD     HL,BC           
56D5: 36 80      LD      (HL),$80        
56D7: 3E 01      LD      A,$01           
56D9: E0 F2      LDFF00  ($F2),A         
56DB: CD 8D 3B   CALL    $3B8D           
56DE: 3E 02      LD      A,$02           
56E0: E0 A1      LDFF00  ($A1),A         
56E2: C9         RET                     
56E3: 9A         SBC     D               
56E4: 10 9C      STOP    $9C             
56E6: 10 3E      STOP    $3E             
56E8: 03         INC     BC              
56E9: CD 87 3B   CALL    $3B87           
56EC: CD 91 08   CALL    $0891           
56EF: 20 0F      JR      NZ,$5700        
56F1: 3E 36      LD      A,$36           
56F3: EA 68 D3   LD      ($D368),A       
56F6: E0 B0      LDFF00  ($B0),A         
56F8: CD 87 08   CALL    $0887           
56FB: 36 80      LD      (HL),$80        
56FD: C3 8D 3B   JP      $3B8D           
5700: FE 10      CP      $10             
5702: 20 05      JR      NZ,$5709        
5704: 3E 62      LD      A,$62           
5706: CD 68 56   CALL    $5668           
5709: 3E 02      LD      A,$02           
570B: E0 A1      LDFF00  ($A1),A         
570D: C9         RET                     
570E: 48         LD      C,B             
570F: 48         LD      C,B             
5710: 48         LD      C,B             
5711: 48         LD      C,B             
5712: 48         LD      C,B             
5713: 48         LD      C,B             
5714: 48         LD      C,B             
5715: 18 20      JR      $5737           
5717: 28 30      JR      Z,$5749         
5719: 38 40      JR      C,$575B         
571B: 48         LD      C,B             
571C: 00         NOP                     
571D: 78         LD      A,B             
571E: 28 58      JR      Z,$5778         
5720: 40         LD      B,B             
5721: 30 60      JR      NC,$5783        
5723: 00         NOP                     
5724: 00         NOP                     
5725: 80         ADD     A,B             
5726: 80         ADD     A,B             
5727: 00         NOP                     
5728: 80         ADD     A,B             
5729: 00         NOP                     
572A: 10 30      STOP    $30             
572C: 20 3E      JR      NZ,$576C        
572E: 02         LD      (BC),A          
572F: E0 A1      LDFF00  ($A1),A         
5731: CD 8E 56   CALL    $568E           
5734: CD 87 08   CALL    $0887           
5737: 20 25      JR      NZ,$575E        
5739: 3E 02      LD      A,$02           
573B: E0 F2      LDFF00  ($F2),A         
573D: FA 7B D8   LD      A,($D87B)       
5740: F6 10      OR      $10             
5742: EA 7B D8   LD      ($D87B),A       
5745: 3E 01      LD      A,$01           
5747: EA 7F DB   LD      ($DB7F),A       
574A: 3E 63      LD      A,$63           
574C: EA 68 C1   LD      ($C168),A       
574F: CD 68 56   CALL    $5668           
5752: CD 8D 3B   CALL    $3B8D           
5755: 36 05      LD      (HL),$05        
5757: 21 D0 C3   LD      HL,$C3D0        
575A: 09         ADD     HL,BC           
575B: 36 06      LD      (HL),$06        
575D: C9         RET                     
575E: FE 01      CP      $01             
5760: 20 09      JR      NZ,$576B        
5762: 3E 05      LD      A,$05           
5764: EA 0E DB   LD      ($DB0E),A       
5767: 3E 0D      LD      A,$0D           
5769: E0 A5      LDFF00  ($A5),A         
576B: F0 E7      LD      A,($E7)         
576D: E6 1F      AND     $1F             
576F: 20 4F      JR      NZ,$57C0        
5771: 21 D0 C2   LD      HL,$C2D0        
5774: 09         ADD     HL,BC           
5775: 7E         LD      A,(HL)          
5776: FE 07      CP      $07             
5778: 28 46      JR      Z,$57C0         
577A: 3E AD      LD      A,$AD           
577C: CD 01 3C   CALL    $3C01           
577F: 38 3F      JR      C,$57C0         
5781: C5         PUSH    BC              
5782: CD 44 72   CALL    $7244           
5785: 21 D0 C2   LD      HL,$C2D0        
5788: 09         ADD     HL,BC           
5789: 4E         LD      C,(HL)          
578A: 34         INC     (HL)            
578B: 21 0E 57   LD      HL,$570E        
578E: 09         ADD     HL,BC           
578F: 7E         LD      A,(HL)          
5790: 21 B0 C2   LD      HL,$C2B0        
5793: 19         ADD     HL,DE           
5794: 77         LD      (HL),A          
5795: 21 15 57   LD      HL,$5715        
5798: 09         ADD     HL,BC           
5799: 7E         LD      A,(HL)          
579A: 21 C0 C2   LD      HL,$C2C0        
579D: 19         ADD     HL,DE           
579E: 77         LD      (HL),A          
579F: 21 1C 57   LD      HL,$571C        
57A2: 09         ADD     HL,BC           
57A3: 7E         LD      A,(HL)          
57A4: 21 00 C2   LD      HL,$C200        
57A7: 19         ADD     HL,DE           
57A8: 77         LD      (HL),A          
57A9: 21 23 57   LD      HL,$5723        
57AC: 09         ADD     HL,BC           
57AD: 7E         LD      A,(HL)          
57AE: 21 10 C2   LD      HL,$C210        
57B1: 19         ADD     HL,DE           
57B2: 77         LD      (HL),A          
57B3: 21 90 C2   LD      HL,$C290        
57B6: 19         ADD     HL,DE           
57B7: 36 07      LD      (HL),$07        
57B9: 21 00 C3   LD      HL,$C300        
57BC: 19         ADD     HL,DE           
57BD: 36 80      LD      (HL),$80        
57BF: C1         POP     BC              
57C0: CD 87 08   CALL    $0887           
57C3: FE 40      CP      $40             
57C5: 30 5E      JR      NC,$5825        
57C7: F0 E7      LD      A,($E7)         
57C9: E6 3F      AND     $3F             
57CB: 20 58      JR      NZ,$5825        
57CD: 21 40 C4   LD      HL,$C440        
57D0: 09         ADD     HL,BC           
57D1: 7E         LD      A,(HL)          
57D2: FE 03      CP      $03             
57D4: 30 4F      JR      NC,$5825        
57D6: 5F         LD      E,A             
57D7: 50         LD      D,B             
57D8: 34         INC     (HL)            
57D9: 21 2A 57   LD      HL,$572A        
57DC: 19         ADD     HL,DE           
57DD: 7E         LD      A,(HL)          
57DE: E0 CD      LDFF00  ($CD),A         
57E0: 3E 40      LD      A,$40           
57E2: E0 CE      LDFF00  ($CE),A         
57E4: CD 39 28   CALL    $2839           
57E7: 21 01 D6   LD      HL,$D601        
57EA: FA 00 D6   LD      A,($D600)       
57ED: 5F         LD      E,A             
57EE: C6 0A      ADD     $0A             
57F0: EA 00 D6   LD      ($D600),A       
57F3: 16 00      LD      D,$00           
57F5: 19         ADD     HL,DE           
57F6: F0 CF      LD      A,($CF)         
57F8: 22         LD      (HLI),A         
57F9: F0 D0      LD      A,($D0)         
57FB: 22         LD      (HLI),A         
57FC: 3E 81      LD      A,$81           
57FE: 22         LD      (HLI),A         
57FF: 3E 0C      LD      A,$0C           
5801: 22         LD      (HLI),A         
5802: 3E 1C      LD      A,$1C           
5804: 22         LD      (HLI),A         
5805: F0 CF      LD      A,($CF)         
5807: 22         LD      (HLI),A         
5808: F0 D0      LD      A,($D0)         
580A: 3C         INC     A               
580B: 22         LD      (HLI),A         
580C: 3E 81      LD      A,$81           
580E: 22         LD      (HLI),A         
580F: 3E 0D      LD      A,$0D           
5811: 22         LD      (HLI),A         
5812: 3E 1D      LD      A,$1D           
5814: 22         LD      (HLI),A         
5815: 70         LD      (HL),B          
5816: 21 25 D7   LD      HL,$D725        
5819: 36 DB      LD      (HL),$DB        
581B: 21 35 D7   LD      HL,$D735        
581E: 36 DB      LD      (HL),$DB        
5820: 21 45 D7   LD      HL,$D745        
5823: 36 DB      LD      (HL),$DB        
5825: C9         RET                     
5826: CD 91 08   CALL    $0891           
5829: 20 6A      JR      NZ,$5895        
582B: CD 8D 3B   CALL    $3B8D           
582E: 21 D0 C3   LD      HL,$C3D0        
5831: 09         ADD     HL,BC           
5832: 7E         LD      A,(HL)          
5833: FE 05      CP      $05             
5835: 38 23      JR      C,$585A         
5837: CD ED 27   CALL    $27ED           
583A: E6 0F      AND     $0F             
583C: C6 10      ADD     $10             
583E: 21 20 C3   LD      HL,$C320        
5841: 09         ADD     HL,BC           
5842: 77         LD      (HL),A          
5843: 1E 10      LD      E,$10           
5845: E6 01      AND     $01             
5847: 28 02      JR      Z,$584B         
5849: 1E F0      LD      E,$F0           
584B: 21 40 C2   LD      HL,$C240        
584E: 09         ADD     HL,BC           
584F: 73         LD      (HL),E          
5850: 21 50 C2   LD      HL,$C250        
5853: 09         ADD     HL,BC           
5854: 36 F0      LD      (HL),$F0        
5856: CD 84 58   CALL    $5884           
5859: C9         RET                     
585A: 21 20 C3   LD      HL,$C320        
585D: 09         ADD     HL,BC           
585E: 36 18      LD      (HL),$18        
5860: F0 98      LD      A,($98)         
5862: F5         PUSH    AF              
5863: F0 99      LD      A,($99)         
5865: F5         PUSH    AF              
5866: FA 54 D1   LD      A,($D154)       
5869: 5F         LD      E,A             
586A: 50         LD      D,B             
586B: 21 00 C2   LD      HL,$C200        
586E: 19         ADD     HL,DE           
586F: 7E         LD      A,(HL)          
5870: E0 98      LDFF00  ($98),A         
5872: 21 10 C2   LD      HL,$C210        
5875: 19         ADD     HL,DE           
5876: 7E         LD      A,(HL)          
5877: E0 99      LDFF00  ($99),A         
5879: 3E 14      LD      A,$14           
587B: CD 25 3C   CALL    $3C25           
587E: F1         POP     AF              
587F: E0 99      LDFF00  ($99),A         
5881: F1         POP     AF              
5882: E0 98      LDFF00  ($98),A         
5884: 21 40 C2   LD      HL,$C240        
5887: 09         ADD     HL,BC           
5888: 7E         LD      A,(HL)          
5889: 1E 00      LD      E,$00           
588B: E6 80      AND     $80             
588D: 28 01      JR      Z,$5890         
588F: 1C         INC     E               
5890: 21 80 C3   LD      HL,$C380        
5893: 09         ADD     HL,BC           
5894: 73         LD      (HL),E          
5895: CD 8E 56   CALL    $568E           
5898: CD 8C 08   CALL    $088C           
589B: 28 05      JR      Z,$58A2         
589D: 3E 04      LD      A,$04           
589F: CD 87 3B   CALL    $3B87           
58A2: C9         RET                     
58A3: CD E2 7C   CALL    $7CE2           
58A6: F0 EF      LD      A,($EF)         
58A8: FE 08      CP      $08             
58AA: DA 7C 7D   JP      C,$7D7C         
58AD: 21 D0 C3   LD      HL,$C3D0        
58B0: 09         ADD     HL,BC           
58B1: 7E         LD      A,(HL)          
58B2: FE 05      CP      $05             
58B4: 30 03      JR      NC,$58B9        
58B6: CD 9E 3B   CALL    $3B9E           
58B9: F0 E8      LD      A,($E8)         
58BB: A7         AND     A               
58BC: 28 24      JR      Z,$58E2         
58BE: CD 8D 3B   CALL    $3B8D           
58C1: 36 05      LD      (HL),$05        
58C3: 21 D0 C3   LD      HL,$C3D0        
58C6: 09         ADD     HL,BC           
58C7: 7E         LD      A,(HL)          
58C8: FE 05      CP      $05             
58CA: 38 0B      JR      C,$58D7         
58CC: CD 91 08   CALL    $0891           
58CF: 36 10      LD      (HL),$10        
58D1: CD 8C 08   CALL    $088C           
58D4: 36 10      LD      (HL),$10        
58D6: C9         RET                     
58D7: CD 91 08   CALL    $0891           
58DA: CD ED 27   CALL    $27ED           
58DD: E6 3F      AND     $3F             
58DF: C6 30      ADD     $30             
58E1: 77         LD      (HL),A          
58E2: 3E 03      LD      A,$03           
58E4: CD 87 3B   CALL    $3B87           
58E7: C9         RET                     
58E8: CD 91 08   CALL    $0891           
58EB: 20 5D      JR      NZ,$594A        
58ED: F0 98      LD      A,($98)         
58EF: F5         PUSH    AF              
58F0: F0 99      LD      A,($99)         
58F2: F5         PUSH    AF              
58F3: 21 B0 C2   LD      HL,$C2B0        
58F6: 09         ADD     HL,BC           
58F7: 7E         LD      A,(HL)          
58F8: E0 98      LDFF00  ($98),A         
58FA: 21 C0 C2   LD      HL,$C2C0        
58FD: 09         ADD     HL,BC           
58FE: 7E         LD      A,(HL)          
58FF: E0 99      LDFF00  ($99),A         
5901: 21 00 C3   LD      HL,$C300        
5904: 09         ADD     HL,BC           
5905: FA 68 C1   LD      A,($C168)       
5908: B6         OR      (HL)            
5909: 3E 10      LD      A,$10           
590B: 1E 10      LD      E,$10           
590D: 20 04      JR      NZ,$5913        
590F: 3E 08      LD      A,$08           
5911: 1E 08      LD      E,$08           
5913: D5         PUSH    DE              
5914: CD 25 3C   CALL    $3C25           
5917: D1         POP     DE              
5918: 21 20 C3   LD      HL,$C320        
591B: 09         ADD     HL,BC           
591C: 73         LD      (HL),E          
591D: FA 68 C1   LD      A,($C168)       
5920: A7         AND     A               
5921: 28 1B      JR      Z,$593E         
5923: F0 D7      LD      A,($D7)         
5925: 21 50 C2   LD      HL,$C250        
5928: 09         ADD     HL,BC           
5929: 2F         CPL                     
592A: 3C         INC     A               
592B: 77         LD      (HL),A          
592C: F0 D8      LD      A,($D8)         
592E: 21 40 C2   LD      HL,$C240        
5931: 09         ADD     HL,BC           
5932: 2F         CPL                     
5933: 3C         INC     A               
5934: 77         LD      (HL),A          
5935: F0 EF      LD      A,($EF)         
5937: FE 90      CP      $90             
5939: 38 03      JR      C,$593E         
593B: CD 7C 7D   CALL    $7D7C           
593E: F1         POP     AF              
593F: E0 99      LDFF00  ($99),A         
5941: F1         POP     AF              
5942: E0 98      LDFF00  ($98),A         
5944: CD 8D 3B   CALL    $3B8D           
5947: CD 84 58   CALL    $5884           
594A: 21 50 C2   LD      HL,$C250        
594D: 09         ADD     HL,BC           
594E: 7E         LD      A,(HL)          
594F: E6 80      AND     $80             
5951: 3E 02      LD      A,$02           
5953: 28 02      JR      Z,$5957         
5955: 3E 04      LD      A,$04           
5957: CD 87 3B   CALL    $3B87           
595A: C9         RET                     
595B: F0 E8      LD      A,($E8)         
595D: A7         AND     A               
595E: 28 0A      JR      Z,$596A         
5960: CD 91 08   CALL    $0891           
5963: 36 08      LD      (HL),$08        
5965: CD 8D 3B   CALL    $3B8D           
5968: 35         DEC     (HL)            
5969: 35         DEC     (HL)            
596A: 3E 03      LD      A,$03           
596C: CD 87 3B   CALL    $3B87           
596F: CD E2 7C   CALL    $7CE2           
5972: C9         RET                     
5973: C9         RET                     
5974: 6A         LD      L,D             
5975: 00         NOP                     
5976: 6A         LD      L,D             
5977: 20 68      JR      NZ,$59E1        
5979: 00         NOP                     
597A: 68         LD      L,B             
597B: 20 11      JR      NZ,$598E        
597D: 74         LD      (HL),H          
597E: 59         LD      E,C             
597F: CD 3B 3C   CALL    $3C3B           
5982: CD 76 7C   CALL    $7C76           
5985: CD 98 7C   CALL    $7C98           
5988: CD B4 3B   CALL    $3BB4           
598B: CD E2 7C   CALL    $7CE2           
598E: CD 9E 3B   CALL    $3B9E           
5991: 21 70 C4   LD      HL,$C470        
5994: 09         ADD     HL,BC           
5995: 7E         LD      A,(HL)          
5996: A7         AND     A               
5997: 20 14      JR      NZ,$59AD        
5999: 21 80 C4   LD      HL,$C480        
599C: 09         ADD     HL,BC           
599D: 36 10      LD      (HL),$10        
599F: F0 EE      LD      A,($EE)         
59A1: 21 00 C2   LD      HL,$C200        
59A4: 09         ADD     HL,BC           
59A5: 77         LD      (HL),A          
59A6: F0 EF      LD      A,($EF)         
59A8: 21 10 C2   LD      HL,$C210        
59AB: 09         ADD     HL,BC           
59AC: 77         LD      (HL),A          
59AD: AF         XOR     A               
59AE: CD 87 3B   CALL    $3B87           
59B1: F0 F0      LD      A,($F0)         
59B3: C7         RST     0X00            
59B4: B8         CP      B               
59B5: 59         LD      E,C             
59B6: FD         ???                     
59B7: 59         LD      E,C             
59B8: CD 91 08   CALL    $0891           
59BB: 20 1E      JR      NZ,$59DB        
59BD: CD 45 7D   CALL    $7D45           
59C0: 7B         LD      A,E             
59C1: FE 03      CP      $03             
59C3: 28 16      JR      Z,$59DB         
59C5: CD AF 3D   CALL    $3DAF           
59C8: CD 91 08   CALL    $0891           
59CB: 36 25      LD      (HL),$25        
59CD: CD 35 7D   CALL    $7D35           
59D0: 21 80 C3   LD      HL,$C380        
59D3: 09         ADD     HL,BC           
59D4: 73         LD      (HL),E          
59D5: CD 8D 3B   CALL    $3B8D           
59D8: 36 01      LD      (HL),$01        
59DA: C9         RET                     
59DB: 21 50 C2   LD      HL,$C250        
59DE: 09         ADD     HL,BC           
59DF: 7E         LD      A,(HL)          
59E0: D6 04      SUB     $04             
59E2: 28 07      JR      Z,$59EB         
59E4: E6 80      AND     $80             
59E6: 28 02      JR      Z,$59EA         
59E8: 34         INC     (HL)            
59E9: 34         INC     (HL)            
59EA: 35         DEC     (HL)            
59EB: 21 40 C2   LD      HL,$C240        
59EE: 09         ADD     HL,BC           
59EF: 7E         LD      A,(HL)          
59F0: A7         AND     A               
59F1: 28 07      JR      Z,$59FA         
59F3: E6 80      AND     $80             
59F5: 28 02      JR      Z,$59F9         
59F7: 34         INC     (HL)            
59F8: 34         INC     (HL)            
59F9: 35         DEC     (HL)            
59FA: C9         RET                     
59FB: 01 FF CD   LD      BC,$CDFF        
59FE: 91         SUB     C               
59FF: 08 20 07   LD      ($0720),SP      
5A02: 36 40      LD      (HL),$40        
5A04: CD 8D 3B   CALL    $3B8D           
5A07: 70         LD      (HL),B          
5A08: C9         RET                     
5A09: F0 E7      LD      A,($E7)         
5A0B: E6 01      AND     $01             
5A0D: 20 16      JR      NZ,$5A25        
5A0F: 21 50 C2   LD      HL,$C250        
5A12: 09         ADD     HL,BC           
5A13: 35         DEC     (HL)            
5A14: 21 80 C3   LD      HL,$C380        
5A17: 09         ADD     HL,BC           
5A18: 5E         LD      E,(HL)          
5A19: 50         LD      D,B             
5A1A: 21 FB 59   LD      HL,$59FB        
5A1D: 19         ADD     HL,DE           
5A1E: 7E         LD      A,(HL)          
5A1F: 21 40 C2   LD      HL,$C240        
5A22: 09         ADD     HL,BC           
5A23: 86         ADD     A,(HL)          
5A24: 77         LD      (HL),A          
5A25: 3E 01      LD      A,$01           
5A27: CD 87 3B   CALL    $3B87           
5A2A: C9         RET                     
5A2B: F0 F1      LD      A,($F1)         
5A2D: 3C         INC     A               
5A2E: 28 4A      JR      Z,$5A7A         
5A30: E5         PUSH    HL              
5A31: FA C0 C3   LD      A,($C3C0)       
5A34: 5F         LD      E,A             
5A35: 16 00      LD      D,$00           
5A37: 21 30 C0   LD      HL,$C030        
5A3A: 19         ADD     HL,DE           
5A3B: E5         PUSH    HL              
5A3C: D1         POP     DE              
5A3D: E1         POP     HL              
5A3E: F0 EC      LD      A,($EC)         
5A40: 86         ADD     A,(HL)          
5A41: FE 7E      CP      $7E             
5A43: 38 01      JR      C,$5A46         
5A45: AF         XOR     A               
5A46: 12         LD      (DE),A          
5A47: 23         INC     HL              
5A48: 13         INC     DE              
5A49: C5         PUSH    BC              
5A4A: FA 55 C1   LD      A,($C155)       
5A4D: 4F         LD      C,A             
5A4E: F0 EE      LD      A,($EE)         
5A50: 86         ADD     A,(HL)          
5A51: 91         SUB     C               
5A52: 12         LD      (DE),A          
5A53: 23         INC     HL              
5A54: 13         INC     DE              
5A55: F0 F5      LD      A,($F5)         
5A57: 4F         LD      C,A             
5A58: 2A         LD      A,(HLI)         
5A59: F5         PUSH    AF              
5A5A: 81         ADD     A,C             
5A5B: 12         LD      (DE),A          
5A5C: F1         POP     AF              
5A5D: FE FF      CP      $FF             
5A5F: 20 04      JR      NZ,$5A65        
5A61: 1B         DEC     DE              
5A62: AF         XOR     A               
5A63: 12         LD      (DE),A          
5A64: 13         INC     DE              
5A65: C1         POP     BC              
5A66: 13         INC     DE              
5A67: F0 ED      LD      A,($ED)         
5A69: AE         XOR     (HL)            
5A6A: 23         INC     HL              
5A6B: 12         LD      (DE),A          
5A6C: 13         INC     DE              
5A6D: 0D         DEC     C               
5A6E: 20 CE      JR      NZ,$5A3E        
5A70: FA 23 C1   LD      A,($C123)       
5A73: 4F         LD      C,A             
5A74: 3E 0A      LD      A,$0A           
5A76: CD D0 3D   CALL    $3DD0           
5A79: C9         RET                     
5A7A: FA 23 C1   LD      A,($C123)       
5A7D: 4F         LD      C,A             
5A7E: C9         RET                     
5A7F: 00         NOP                     
5A80: 00         NOP                     
5A81: 4C         LD      C,H             
5A82: 00         NOP                     
5A83: 00         NOP                     
5A84: 08 4C 20   LD      ($204C),SP      
5A87: F0 00      LD      A,($00)         
5A89: 4A         LD      C,D             
5A8A: 00         NOP                     
5A8B: F0 08      LD      A,($08)         
5A8D: 4A         LD      C,D             
5A8E: 20 E0      JR      NZ,$5A70        
5A90: 00         NOP                     
5A91: 4A         LD      C,D             
5A92: 00         NOP                     
5A93: E0 08      LDFF00  ($08),A         
5A95: 4A         LD      C,D             
5A96: 20 D0      JR      NZ,$5A68        
5A98: 00         NOP                     
5A99: 4A         LD      C,D             
5A9A: 00         NOP                     
5A9B: D0         RET     NC              
5A9C: 08 4A 20   LD      ($204A),SP      
5A9F: C0         RET     NZ              
5AA0: 00         NOP                     
5AA1: 48         LD      C,B             
5AA2: 00         NOP                     
5AA3: C0         RET     NZ              
5AA4: 08 48 20   LD      ($2048),SP      
5AA7: 00         NOP                     
5AA8: 00         NOP                     
5AA9: 4A         LD      C,D             
5AAA: 00         NOP                     
5AAB: 00         NOP                     
5AAC: 08 4A 20   LD      ($204A),SP      
5AAF: F0 00      LD      A,($00)         
5AB1: 4A         LD      C,D             
5AB2: 00         NOP                     
5AB3: F0 08      LD      A,($08)         
5AB5: 4A         LD      C,D             
5AB6: 20 E0      JR      NZ,$5A98        
5AB8: 00         NOP                     
5AB9: 4A         LD      C,D             
5ABA: 00         NOP                     
5ABB: E0 08      LDFF00  ($08),A         
5ABD: 4A         LD      C,D             
5ABE: 20 D0      JR      NZ,$5A90        
5AC0: 00         NOP                     
5AC1: 48         LD      C,B             
5AC2: 00         NOP                     
5AC3: D0         RET     NC              
5AC4: 08 48 20   LD      ($2048),SP      
5AC7: C0         RET     NZ              
5AC8: 00         NOP                     
5AC9: FF         RST     0X38            
5ACA: 00         NOP                     
5ACB: C0         RET     NZ              
5ACC: 08 FF 20   LD      ($20FF),SP      
5ACF: 00         NOP                     
5AD0: 00         NOP                     
5AD1: 4A         LD      C,D             
5AD2: 00         NOP                     
5AD3: 00         NOP                     
5AD4: 08 4A 20   LD      ($204A),SP      
5AD7: F0 00      LD      A,($00)         
5AD9: 4A         LD      C,D             
5ADA: 00         NOP                     
5ADB: F0 08      LD      A,($08)         
5ADD: 4A         LD      C,D             
5ADE: 20 E0      JR      NZ,$5AC0        
5AE0: 00         NOP                     
5AE1: 48         LD      C,B             
5AE2: 00         NOP                     
5AE3: E0 08      LDFF00  ($08),A         
5AE5: 48         LD      C,B             
5AE6: 20 D0      JR      NZ,$5AB8        
5AE8: 00         NOP                     
5AE9: FF         RST     0X38            
5AEA: 00         NOP                     
5AEB: D0         RET     NC              
5AEC: 08 FF 20   LD      ($20FF),SP      
5AEF: C0         RET     NZ              
5AF0: 00         NOP                     
5AF1: FF         RST     0X38            
5AF2: 00         NOP                     
5AF3: C0         RET     NZ              
5AF4: 08 FF 20   LD      ($20FF),SP      
5AF7: 00         NOP                     
5AF8: 00         NOP                     
5AF9: 4A         LD      C,D             
5AFA: 00         NOP                     
5AFB: 00         NOP                     
5AFC: 08 4A 20   LD      ($204A),SP      
5AFF: F0 00      LD      A,($00)         
5B01: 48         LD      C,B             
5B02: 00         NOP                     
5B03: F0 08      LD      A,($08)         
5B05: 48         LD      C,B             
5B06: 20 E0      JR      NZ,$5AE8        
5B08: 00         NOP                     
5B09: FF         RST     0X38            
5B0A: 00         NOP                     
5B0B: E0 08      LDFF00  ($08),A         
5B0D: FF         RST     0X38            
5B0E: 20 D0      JR      NZ,$5AE0        
5B10: 00         NOP                     
5B11: FF         RST     0X38            
5B12: 00         NOP                     
5B13: D0         RET     NC              
5B14: 08 FF 20   LD      ($20FF),SP      
5B17: C0         RET     NZ              
5B18: 00         NOP                     
5B19: FF         RST     0X38            
5B1A: 00         NOP                     
5B1B: C0         RET     NZ              
5B1C: 08 FF 20   LD      ($20FF),SP      
5B1F: 00         NOP                     
5B20: 00         NOP                     
5B21: 48         LD      C,B             
5B22: 00         NOP                     
5B23: 00         NOP                     
5B24: 08 48 20   LD      ($2048),SP      
5B27: F0 00      LD      A,($00)         
5B29: FF         RST     0X38            
5B2A: 00         NOP                     
5B2B: F0 08      LD      A,($08)         
5B2D: FF         RST     0X38            
5B2E: 20 E0      JR      NZ,$5B10        
5B30: 00         NOP                     
5B31: FF         RST     0X38            
5B32: 00         NOP                     
5B33: E0 08      LDFF00  ($08),A         
5B35: FF         RST     0X38            
5B36: 20 D0      JR      NZ,$5B08        
5B38: 00         NOP                     
5B39: FF         RST     0X38            
5B3A: 00         NOP                     
5B3B: D0         RET     NC              
5B3C: 08 FF 20   LD      ($20FF),SP      
5B3F: C0         RET     NZ              
5B40: 00         NOP                     
5B41: FF         RST     0X38            
5B42: 00         NOP                     
5B43: C0         RET     NZ              
5B44: 08 FF 20   LD      ($20FF),SP      
5B47: 21 B0 C2   LD      HL,$C2B0        
5B4A: 09         ADD     HL,BC           
5B4B: 7E         LD      A,(HL)          
5B4C: FE 02      CP      $02             
5B4E: CA 28 5D   JP      Z,$5D28         
5B51: A7         AND     A               
5B52: C2 C8 5C   JP      NZ,$5CC8        
5B55: F0 F8      LD      A,($F8)         
5B57: E6 20      AND     $20             
5B59: C2 7C 7D   JP      NZ,$7D7C        
5B5C: FA 24 C1   LD      A,($C124)       
5B5F: A7         AND     A               
5B60: 20 0A      JR      NZ,$5B6C        
5B62: 21 E0 C3   LD      HL,$C3E0        
5B65: 09         ADD     HL,BC           
5B66: F0 F6      LD      A,($F6)         
5B68: BE         CP      (HL)            
5B69: C2 7C 7D   JP      NZ,$7D7C        
5B6C: F0 F1      LD      A,($F1)         
5B6E: FE 05      CP      $05             
5B70: 30 17      JR      NC,$5B89        
5B72: 17         RLA                     
5B73: 17         RLA                     
5B74: E6 FC      AND     $FC             
5B76: CB 27      SET     1,E             
5B78: 5F         LD      E,A             
5B79: CB 27      SET     1,E             
5B7B: CB 27      SET     1,E             
5B7D: 83         ADD     A,E             
5B7E: 5F         LD      E,A             
5B7F: 50         LD      D,B             
5B80: 21 7F 5A   LD      HL,$5A7F        
5B83: 19         ADD     HL,DE           
5B84: 0E 0A      LD      C,$0A           
5B86: CD 2B 5A   CALL    $5A2B           
5B89: CD E2 08   CALL    $08E2           
5B8C: CD EB 3B   CALL    $3BEB           
5B8F: CD D0 7B   CALL    $7BD0           
5B92: F0 F0      LD      A,($F0)         
5B94: C7         RST     0X00            
5B95: A1         AND     C               
5B96: 5B         LD      E,E             
5B97: A2         AND     D               
5B98: 5B         LD      E,E             
5B99: BA         CP      D               
5B9A: 5B         LD      E,E             
5B9B: 3D         DEC     A               
5B9C: 5C         LD      E,H             
5B9D: 6B         LD      L,E             
5B9E: 5C         LD      E,H             
5B9F: 8C         ADC     A,H             
5BA0: 5C         LD      E,H             
5BA1: C9         RET                     
5BA2: CD 63 5C   CALL    $5C63           
5BA5: CD 91 08   CALL    $0891           
5BA8: 20 03      JR      NZ,$5BAD        
5BAA: C3 8D 3B   JP      $3B8D           
5BAD: 1E 00      LD      E,$00           
5BAF: E6 04      AND     $04             
5BB1: 28 02      JR      Z,$5BB5         
5BB3: 1E 02      LD      E,$02           
5BB5: 7B         LD      A,E             
5BB6: EA 55 C1   LD      ($C155),A       
5BB9: C9         RET                     
5BBA: CD 63 5C   CALL    $5C63           
5BBD: F0 E7      LD      A,($E7)         
5BBF: CD AD 5B   CALL    $5BAD           
5BC2: F0 E7      LD      A,($E7)         
5BC4: E6 1F      AND     $1F             
5BC6: 20 16      JR      NZ,$5BDE        
5BC8: 21 B0 C3   LD      HL,$C3B0        
5BCB: 09         ADD     HL,BC           
5BCC: 7E         LD      A,(HL)          
5BCD: 3C         INC     A               
5BCE: 77         LD      (HL),A          
5BCF: FE 05      CP      $05             
5BD1: CA 1E 5C   JP      Z,$5C1E         
5BD4: CD ED 27   CALL    $27ED           
5BD7: E6 03      AND     $03             
5BD9: 28 03      JR      Z,$5BDE         
5BDB: CD DE 5C   CALL    $5CDE           
5BDE: F0 E7      LD      A,($E7)         
5BE0: E6 03      AND     $03             
5BE2: 20 39      JR      NZ,$5C1D        
5BE4: 3E A7      LD      A,$A7           
5BE6: CD 01 3C   CALL    $3C01           
5BE9: 38 32      JR      C,$5C1D         
5BEB: CD ED 27   CALL    $27ED           
5BEE: E6 07      AND     $07             
5BF0: D6 04      SUB     $04             
5BF2: 21 D8 FF   LD      HL,$FFD8        
5BF5: 86         ADD     A,(HL)          
5BF6: 21 10 C2   LD      HL,$C210        
5BF9: 19         ADD     HL,DE           
5BFA: 77         LD      (HL),A          
5BFB: CD ED 27   CALL    $27ED           
5BFE: E6 1F      AND     $1F             
5C00: D6 10      SUB     $10             
5C02: 21 D7 FF   LD      HL,$FFD7        
5C05: 86         ADD     A,(HL)          
5C06: 21 00 C2   LD      HL,$C200        
5C09: 19         ADD     HL,DE           
5C0A: 77         LD      (HL),A          
5C0B: 21 40 C3   LD      HL,$C340        
5C0E: 19         ADD     HL,DE           
5C0F: 36 C2      LD      (HL),$C2        
5C11: 21 E0 C2   LD      HL,$C2E0        
5C14: 19         ADD     HL,DE           
5C15: 36 10      LD      (HL),$10        
5C17: 21 B0 C2   LD      HL,$C2B0        
5C1A: 19         ADD     HL,DE           
5C1B: 36 01      LD      (HL),$01        
5C1D: C9         RET                     
5C1E: 3E 00      LD      A,$00           
5C20: EA 55 C1   LD      ($C155),A       
5C23: FA 72 DB   LD      A,($DB72)       
5C26: 3C         INC     A               
5C27: EA 72 DB   LD      ($DB72),A       
5C2A: FE 04      CP      $04             
5C2C: 38 09      JR      C,$5C37         
5C2E: CD 91 08   CALL    $0891           
5C31: 36 20      LD      (HL),$20        
5C33: CD 8D 3B   CALL    $3B8D           
5C36: C9         RET                     
5C37: CD 97 6D   CALL    $6D97           
5C3A: C3 7C 7D   JP      $7D7C           
5C3D: CD 91 08   CALL    $0891           
5C40: 20 15      JR      NZ,$5C57        
5C42: 36 20      LD      (HL),$20        
5C44: 3E 08      LD      A,$08           
5C46: EA 95 DB   LD      ($DB95),A       
5C49: AF         XOR     A               
5C4A: EA 6B C1   LD      ($C16B),A       
5C4D: EA 6C C1   LD      ($C16C),A       
5C50: EA 96 DB   LD      ($DB96),A       
5C53: CD 8D 3B   CALL    $3B8D           
5C56: C9         RET                     
5C57: 1E 00      LD      E,$00           
5C59: E6 04      AND     $04             
5C5B: 28 02      JR      Z,$5C5F         
5C5D: 1E 02      LD      E,$02           
5C5F: 7B         LD      A,E             
5C60: EA 55 C1   LD      ($C155),A       
5C63: 3E 02      LD      A,$02           
5C65: E0 A1      LDFF00  ($A1),A         
5C67: EA 11 C1   LD      ($C111),A       
5C6A: C9         RET                     
5C6B: AF         XOR     A               
5C6C: EA 55 C1   LD      ($C155),A       
5C6F: CD 91 08   CALL    $0891           
5C72: 20 0C      JR      NZ,$5C80        
5C74: CD 97 6D   CALL    $6D97           
5C77: 21 6B DB   LD      HL,$DB6B        
5C7A: CB D6      SET     1,E             
5C7C: CD 7C 7D   CALL    $7D7C           
5C7F: C9         RET                     
5C80: CD 63 5C   CALL    $5C63           
5C83: C9         RET                     
5C84: 00         NOP                     
5C85: 02         LD      (BC),A          
5C86: 04         INC     B               
5C87: 06 06      LD      B,$06           
5C89: 04         INC     B               
5C8A: 02         LD      (BC),A          
5C8B: 00         NOP                     
5C8C: AF         XOR     A               
5C8D: EA 56 C1   LD      ($C156),A       
5C90: CD 91 08   CALL    $0891           
5C93: 20 03      JR      NZ,$5C98        
5C95: C3 7C 7D   JP      $7D7C           
5C98: F5         PUSH    AF              
5C99: E6 07      AND     $07             
5C9B: 5F         LD      E,A             
5C9C: 50         LD      D,B             
5C9D: 21 84 5C   LD      HL,$5C84        
5CA0: 19         ADD     HL,DE           
5CA1: 7E         LD      A,(HL)          
5CA2: EA 56 C1   LD      ($C156),A       
5CA5: F1         POP     AF              
5CA6: FE 20      CP      $20             
5CA8: 30 08      JR      NC,$5CB2        
5CAA: E6 03      AND     $03             
5CAC: 20 04      JR      NZ,$5CB2        
5CAE: CD DE 5C   CALL    $5CDE           
5CB1: AF         XOR     A               
5CB2: FE 40      CP      $40             
5CB4: 38 09      JR      C,$5CBF         
5CB6: E6 07      AND     $07             
5CB8: 20 05      JR      NZ,$5CBF        
5CBA: 21 F4 FF   LD      HL,$FFF4        
5CBD: 36 0C      LD      (HL),$0C        
5CBF: C9         RET                     
5CC0: 30 00      JR      NC,$5CC2        
5CC2: 30 20      JR      NC,$5CE4        
5CC4: 32         LD      (HLD),A         
5CC5: 00         NOP                     
5CC6: 32         LD      (HLD),A         
5CC7: 20 11      JR      NZ,$5CDA        
5CC9: C0         RET     NZ              
5CCA: 5C         LD      E,H             
5CCB: CD 3B 3C   CALL    $3C3B           
5CCE: CD 91 08   CALL    $0891           
5CD1: CA 7C 7D   JP      Z,$7D7C         
5CD4: FE 04      CP      $04             
5CD6: 20 05      JR      NZ,$5CDD        
5CD8: 3E 01      LD      A,$01           
5CDA: CD 87 3B   CALL    $3B87           
5CDD: C9         RET                     
5CDE: 3E A7      LD      A,$A7           
5CE0: CD 01 3C   CALL    $3C01           
5CE3: 38 32      JR      C,$5D17         
5CE5: 21 B0 C2   LD      HL,$C2B0        
5CE8: 19         ADD     HL,DE           
5CE9: 36 02      LD      (HL),$02        
5CEB: 21 40 C3   LD      HL,$C340        
5CEE: 19         ADD     HL,DE           
5CEF: 36 D1      LD      (HL),$D1        
5CF1: 21 10 C3   LD      HL,$C310        
5CF4: 19         ADD     HL,DE           
5CF5: 36 70      LD      (HL),$70        
5CF7: CD ED 27   CALL    $27ED           
5CFA: E6 3F      AND     $3F             
5CFC: D6 20      SUB     $20             
5CFE: 21 D7 FF   LD      HL,$FFD7        
5D01: 86         ADD     A,(HL)          
5D02: 21 00 C2   LD      HL,$C200        
5D05: 19         ADD     HL,DE           
5D06: 77         LD      (HL),A          
5D07: CD ED 27   CALL    $27ED           
5D0A: E6 3F      AND     $3F             
5D0C: D6 20      SUB     $20             
5D0E: 21 D8 FF   LD      HL,$FFD8        
5D11: 86         ADD     A,(HL)          
5D12: 21 10 C2   LD      HL,$C210        
5D15: 19         ADD     HL,DE           
5D16: 77         LD      (HL),A          
5D17: C9         RET                     
5D18: 16 00      LD      D,$00           
5D1A: 16 20      LD      D,$20           
5D1C: 18 10      JR      $5D2E           
5D1E: 0C         INC     C               
5D1F: 08 0C F4   LD      ($F40C),SP      
5D22: 0C         INC     C               
5D23: F4         ???                     
5D24: F4         ???                     
5D25: F4         ???                     
5D26: 0C         INC     C               
5D27: 0C         INC     C               
5D28: F0 EC      LD      A,($EC)         
5D2A: C6 08      ADD     $08             
5D2C: E0 EC      LDFF00  ($EC),A         
5D2E: 11 18 5D   LD      DE,$5D18        
5D31: CD D0 3C   CALL    $3CD0           
5D34: CD E2 7C   CALL    $7CE2           
5D37: CD 1B 7D   CALL    $7D1B           
5D3A: 21 20 C3   LD      HL,$C320        
5D3D: 09         ADD     HL,BC           
5D3E: 35         DEC     (HL)            
5D3F: 35         DEC     (HL)            
5D40: 21 10 C3   LD      HL,$C310        
5D43: 09         ADD     HL,BC           
5D44: 7E         LD      A,(HL)          
5D45: E6 80      AND     $80             
5D47: 28 39      JR      Z,$5D82         
5D49: 70         LD      (HL),B          
5D4A: 21 90 C2   LD      HL,$C290        
5D4D: 09         ADD     HL,BC           
5D4E: 7E         LD      A,(HL)          
5D4F: 34         INC     (HL)            
5D50: FE 04      CP      $04             
5D52: CA 7C 7D   JP      Z,$7D7C         
5D55: 5F         LD      E,A             
5D56: 50         LD      D,B             
5D57: 21 1C 5D   LD      HL,$5D1C        
5D5A: 19         ADD     HL,DE           
5D5B: 7E         LD      A,(HL)          
5D5C: 21 20 C3   LD      HL,$C320        
5D5F: 09         ADD     HL,BC           
5D60: 77         LD      (HL),A          
5D61: CD ED 27   CALL    $27ED           
5D64: E6 03      AND     $03             
5D66: 5F         LD      E,A             
5D67: 50         LD      D,B             
5D68: 21 20 5D   LD      HL,$5D20        
5D6B: 19         ADD     HL,DE           
5D6C: 7E         LD      A,(HL)          
5D6D: 21 40 C2   LD      HL,$C240        
5D70: 09         ADD     HL,BC           
5D71: 77         LD      (HL),A          
5D72: 21 24 5D   LD      HL,$5D24        
5D75: 19         ADD     HL,DE           
5D76: 7E         LD      A,(HL)          
5D77: 21 50 C2   LD      HL,$C250        
5D7A: 09         ADD     HL,BC           
5D7B: 77         LD      (HL),A          
5D7C: 7B         LD      A,E             
5D7D: E6 01      AND     $01             
5D7F: CD 87 3B   CALL    $3B87           
5D82: C9         RET                     
5D83: 4E         LD      C,(HL)          
5D84: 00         NOP                     
5D85: 4E         LD      C,(HL)          
5D86: 20 F0      JR      NZ,$5D78        
5D88: EA FE 07   LD      ($07FE),A       
5D8B: 20 1D      JR      NZ,$5DAA        
5D8D: FA 1C C1   LD      A,($C11C)       
5D90: FE 05      CP      $05             
5D92: 20 05      JR      NZ,$5D99        
5D94: 3E 10      LD      A,$10           
5D96: EA AE C5   LD      ($C5AE),A       
5D99: F0 F6      LD      A,($F6)         
5D9B: 21 E0 C3   LD      HL,$C3E0        
5D9E: 09         ADD     HL,BC           
5D9F: 77         LD      (HL),A          
5DA0: 21 20 C2   LD      HL,$C220        
5DA3: 09         ADD     HL,BC           
5DA4: 70         LD      (HL),B          
5DA5: 21 30 C2   LD      HL,$C230        
5DA8: 09         ADD     HL,BC           
5DA9: 70         LD      (HL),B          
5DAA: 11 83 5D   LD      DE,$5D83        
5DAD: CD 3B 3C   CALL    $3C3B           
5DB0: FA 24 C1   LD      A,($C124)       
5DB3: A7         AND     A               
5DB4: C0         RET     NZ              
5DB5: F0 F6      LD      A,($F6)         
5DB7: EA 6F DB   LD      ($DB6F),A       
5DBA: F0 EE      LD      A,($EE)         
5DBC: EA 70 DB   LD      ($DB70),A       
5DBF: F0 EF      LD      A,($EF)         
5DC1: EA 71 DB   LD      ($DB71),A       
5DC4: FA 9F C1   LD      A,($C19F)       
5DC7: A7         AND     A               
5DC8: C0         RET     NZ              
5DC9: F0 EA      LD      A,($EA)         
5DCB: FE 02      CP      $02             
5DCD: C8         RET     Z               
5DCE: CD E2 08   CALL    $08E2           
5DD1: CD EB 3B   CALL    $3BEB           
5DD4: CD E2 7C   CALL    $7CE2           
5DD7: CD 1B 7D   CALL    $7D1B           
5DDA: 21 20 C3   LD      HL,$C320        
5DDD: 09         ADD     HL,BC           
5DDE: 35         DEC     (HL)            
5DDF: 35         DEC     (HL)            
5DE0: 21 10 C3   LD      HL,$C310        
5DE3: 09         ADD     HL,BC           
5DE4: 7E         LD      A,(HL)          
5DE5: E0 E9      LDFF00  ($E9),A         
5DE7: E6 80      AND     $80             
5DE9: E0 E8      LDFF00  ($E8),A         
5DEB: 28 23      JR      Z,$5E10         
5DED: 70         LD      (HL),B          
5DEE: 21 20 C3   LD      HL,$C320        
5DF1: 09         ADD     HL,BC           
5DF2: 7E         LD      A,(HL)          
5DF3: CB 2F      SET     1,E             
5DF5: 2F         CPL                     
5DF6: FE 07      CP      $07             
5DF8: 38 08      JR      C,$5E02         
5DFA: F5         PUSH    AF              
5DFB: 3E 17      LD      A,$17           
5DFD: E0 F4      LDFF00  ($F4),A         
5DFF: F1         POP     AF              
5E00: 18 01      JR      $5E03           
5E02: AF         XOR     A               
5E03: 77         LD      (HL),A          
5E04: 21 40 C2   LD      HL,$C240        
5E07: 09         ADD     HL,BC           
5E08: CB 2E      SET     1,E             
5E0A: 21 50 C2   LD      HL,$C250        
5E0D: 09         ADD     HL,BC           
5E0E: CB 2E      SET     1,E             
5E10: 21 10 C4   LD      HL,$C410        
5E13: 09         ADD     HL,BC           
5E14: 36 03      LD      (HL),$03        
5E16: 1E 03      LD      E,$03           
5E18: 7B         LD      A,E             
5E19: E0 ED      LDFF00  ($ED),A         
5E1B: 21 10 C2   LD      HL,$C210        
5E1E: 09         ADD     HL,BC           
5E1F: 7E         LD      A,(HL)          
5E20: 83         ADD     A,E             
5E21: 77         LD      (HL),A          
5E22: F0 EF      LD      A,($EF)         
5E24: 83         ADD     A,E             
5E25: E0 EF      LDFF00  ($EF),A         
5E27: CD 9E 3B   CALL    $3B9E           
5E2A: F0 ED      LD      A,($ED)         
5E2C: 5F         LD      E,A             
5E2D: 21 10 C2   LD      HL,$C210        
5E30: 09         ADD     HL,BC           
5E31: 7E         LD      A,(HL)          
5E32: 93         SUB     E               
5E33: 77         LD      (HL),A          
5E34: F0 EF      LD      A,($EF)         
5E36: 93         SUB     E               
5E37: E0 EF      LDFF00  ($EF),A         
5E39: F0 F0      LD      A,($F0)         
5E3B: C7         RST     0X00            
5E3C: 42         LD      B,D             
5E3D: 5E         LD      E,(HL)          
5E3E: B5         OR      L               
5E3F: 5E         LD      E,(HL)          
5E40: B6         OR      (HL)            
5E41: 5E         LD      E,(HL)          
5E42: F0 E9      LD      A,($E9)         
5E44: 3D         DEC     A               
5E45: E6 80      AND     $80             
5E47: 28 15      JR      Z,$5E5E         
5E49: 21 50 C2   LD      HL,$C250        
5E4C: CD 52 5E   CALL    $5E52           
5E4F: 21 40 C2   LD      HL,$C240        
5E52: 09         ADD     HL,BC           
5E53: 7E         LD      A,(HL)          
5E54: A7         AND     A               
5E55: 28 07      JR      Z,$5E5E         
5E57: E6 80      AND     $80             
5E59: 28 02      JR      Z,$5E5D         
5E5B: 34         INC     (HL)            
5E5C: 34         INC     (HL)            
5E5D: 35         DEC     (HL)            
5E5E: CD D5 3B   CALL    $3BD5           
5E61: 30 51      JR      NC,$5EB4        
5E63: FA 9B C1   LD      A,($C19B)       
5E66: A7         AND     A               
5E67: 20 4B      JR      NZ,$5EB4        
5E69: FA 00 DB   LD      A,($DB00)       
5E6C: FE 03      CP      $03             
5E6E: 20 08      JR      NZ,$5E78        
5E70: F0 CC      LD      A,($CC)         
5E72: E6 20      AND     $20             
5E74: 20 0F      JR      NZ,$5E85        
5E76: 18 3C      JR      $5EB4           
5E78: FA 01 DB   LD      A,($DB01)       
5E7B: FE 03      CP      $03             
5E7D: 20 35      JR      NZ,$5EB4        
5E7F: F0 CC      LD      A,($CC)         
5E81: E6 10      AND     $10             
5E83: 28 2F      JR      Z,$5EB4         
5E85: FA CF C3   LD      A,($C3CF)       
5E88: A7         AND     A               
5E89: 20 29      JR      NZ,$5EB4        
5E8B: 3C         INC     A               
5E8C: EA CF C3   LD      ($C3CF),A       
5E8F: F0 EA      LD      A,($EA)         
5E91: FE 07      CP      $07             
5E93: 28 1F      JR      Z,$5EB4         
5E95: CD 8D 3B   CALL    $3B8D           
5E98: 36 02      LD      (HL),$02        
5E9A: 21 80 C2   LD      HL,$C280        
5E9D: 09         ADD     HL,BC           
5E9E: 36 07      LD      (HL),$07        
5EA0: 21 90 C4   LD      HL,$C490        
5EA3: 09         ADD     HL,BC           
5EA4: 70         LD      (HL),B          
5EA5: F0 9E      LD      A,($9E)         
5EA7: EA 5D C1   LD      ($C15D),A       
5EAA: CD 91 08   CALL    $0891           
5EAD: 36 02      LD      (HL),$02        
5EAF: 21 F3 FF   LD      HL,$FFF3        
5EB2: 36 02      LD      (HL),$02        
5EB4: C9         RET                     
5EB5: C9         RET                     
5EB6: F0 E8      LD      A,($E8)         
5EB8: A7         AND     A               
5EB9: 20 20      JR      NZ,$5EDB        
5EBB: 21 A0 C2   LD      HL,$C2A0        
5EBE: 09         ADD     HL,BC           
5EBF: 7E         LD      A,(HL)          
5EC0: A7         AND     A               
5EC1: 28 23      JR      Z,$5EE6         
5EC3: 3E 07      LD      A,$07           
5EC5: E0 F2      LDFF00  ($F2),A         
5EC7: 21 40 C2   LD      HL,$C240        
5ECA: 09         ADD     HL,BC           
5ECB: 7E         LD      A,(HL)          
5ECC: 2F         CPL                     
5ECD: 3C         INC     A               
5ECE: CB 2F      SET     1,E             
5ED0: 77         LD      (HL),A          
5ED1: 21 50 C2   LD      HL,$C250        
5ED4: 09         ADD     HL,BC           
5ED5: 7E         LD      A,(HL)          
5ED6: 2F         CPL                     
5ED7: 3C         INC     A               
5ED8: CB 2F      SET     1,E             
5EDA: 77         LD      (HL),A          
5EDB: 21 D0 C5   LD      HL,$C5D0        
5EDE: 09         ADD     HL,BC           
5EDF: 36 FF      LD      (HL),$FF        
5EE1: CD 8D 3B   CALL    $3B8D           
5EE4: 70         LD      (HL),B          
5EE5: C9         RET                     
5EE6: CD 76 7C   CALL    $7C76           
5EE9: 3E 0B      LD      A,$0B           
5EEB: EA 9E C1   LD      ($C19E),A       
5EEE: CD F6 3B   CALL    $3BF6           
5EF1: 1E 0F      LD      E,$0F           
5EF3: 50         LD      D,B             
5EF4: 21 80 C2   LD      HL,$C280        
5EF7: 19         ADD     HL,DE           
5EF8: 7E         LD      A,(HL)          
5EF9: A7         AND     A               
5EFA: 28 0E      JR      Z,$5F0A         
5EFC: 21 A0 C3   LD      HL,$C3A0        
5EFF: 19         ADD     HL,DE           
5F00: 7E         LD      A,(HL)          
5F01: FE A7      CP      $A7             
5F03: 20 05      JR      NZ,$5F0A        
5F05: D5         PUSH    DE              
5F06: CD 11 5F   CALL    $5F11           
5F09: D1         POP     DE              
5F0A: 1D         DEC     E               
5F0B: 7B         LD      A,E             
5F0C: FE FF      CP      $FF             
5F0E: 20 E4      JR      NZ,$5EF4        
5F10: C9         RET                     
5F11: CD 91 08   CALL    $0891           
5F14: 20 39      JR      NZ,$5F4F        
5F16: 21 00 C2   LD      HL,$C200        
5F19: 19         ADD     HL,DE           
5F1A: F0 EE      LD      A,($EE)         
5F1C: 96         SUB     (HL)            
5F1D: C6 10      ADD     $10             
5F1F: FE 20      CP      $20             
5F21: 30 2C      JR      NC,$5F4F        
5F23: 21 10 C2   LD      HL,$C210        
5F26: 19         ADD     HL,DE           
5F27: F0 EC      LD      A,($EC)         
5F29: 96         SUB     (HL)            
5F2A: C6 18      ADD     $18             
5F2C: FE 28      CP      $28             
5F2E: 30 1F      JR      NC,$5F4F        
5F30: CD C3 5E   CALL    $5EC3           
5F33: 3E 25      LD      A,$25           
5F35: E0 F4      LDFF00  ($F4),A         
5F37: 3E 0B      LD      A,$0B           
5F39: E0 F2      LDFF00  ($F2),A         
5F3B: CD 91 08   CALL    $0891           
5F3E: 36 10      LD      (HL),$10        
5F40: 21 90 C2   LD      HL,$C290        
5F43: 19         ADD     HL,DE           
5F44: 7E         LD      A,(HL)          
5F45: A7         AND     A               
5F46: 20 07      JR      NZ,$5F4F        
5F48: 34         INC     (HL)            
5F49: 21 E0 C2   LD      HL,$C2E0        
5F4C: 19         ADD     HL,DE           
5F4D: 36 50      LD      (HL),$50        
5F4F: C9         RET                     
5F50: 50         LD      D,B             
5F51: 00         NOP                     
5F52: 50         LD      D,B             
5F53: 20 11      JR      NZ,$5F66        
5F55: 50         LD      D,B             
5F56: 5F         LD      E,A             
5F57: CD 3B 3C   CALL    $3C3B           
5F5A: CD 76 7C   CALL    $7C76           
5F5D: CD 03 61   CALL    $6103           
5F60: 21 D0 C2   LD      HL,$C2D0        
5F63: 09         ADD     HL,BC           
5F64: 7E         LD      A,(HL)          
5F65: 5F         LD      E,A             
5F66: A7         AND     A               
5F67: 20 13      JR      NZ,$5F7C        
5F69: 21 C0 C2   LD      HL,$C2C0        
5F6C: 09         ADD     HL,BC           
5F6D: 7E         LD      A,(HL)          
5F6E: A7         AND     A               
5F6F: 28 5C      JR      Z,$5FCD         
5F71: CD 81 60   CALL    $6081           
5F74: 21 D0 C2   LD      HL,$C2D0        
5F77: 19         ADD     HL,DE           
5F78: 36 F0      LD      (HL),$F0        
5F7A: 1E 10      LD      E,$10           
5F7C: F0 E7      LD      A,($E7)         
5F7E: E6 01      AND     $01             
5F80: 20 0F      JR      NZ,$5F91        
5F82: 21 50 C2   LD      HL,$C250        
5F85: 09         ADD     HL,BC           
5F86: 7E         LD      A,(HL)          
5F87: 93         SUB     E               
5F88: 28 07      JR      Z,$5F91         
5F8A: E6 80      AND     $80             
5F8C: 28 02      JR      Z,$5F90         
5F8E: 34         INC     (HL)            
5F8F: 34         INC     (HL)            
5F90: 35         DEC     (HL)            
5F91: 21 50 C3   LD      HL,$C350        
5F94: 09         ADD     HL,BC           
5F95: 36 02      LD      (HL),$02        
5F97: 21 50 C2   LD      HL,$C250        
5F9A: 09         ADD     HL,BC           
5F9B: 7E         LD      A,(HL)          
5F9C: E5         PUSH    HL              
5F9D: F5         PUSH    AF              
5F9E: 73         LD      (HL),E          
5F9F: 21 10 C2   LD      HL,$C210        
5FA2: 09         ADD     HL,BC           
5FA3: 7E         LD      A,(HL)          
5FA4: E5         PUSH    HL              
5FA5: F5         PUSH    AF              
5FA6: CD 9E 3B   CALL    $3B9E           
5FA9: F1         POP     AF              
5FAA: E1         POP     HL              
5FAB: 77         LD      (HL),A          
5FAC: F1         POP     AF              
5FAD: E1         POP     HL              
5FAE: 77         LD      (HL),A          
5FAF: 21 50 C3   LD      HL,$C350        
5FB2: 09         ADD     HL,BC           
5FB3: 36 30      LD      (HL),$30        
5FB5: 21 A0 C2   LD      HL,$C2A0        
5FB8: 09         ADD     HL,BC           
5FB9: 7E         LD      A,(HL)          
5FBA: A7         AND     A               
5FBB: 28 0E      JR      Z,$5FCB         
5FBD: 21 50 C2   LD      HL,$C250        
5FC0: 09         ADD     HL,BC           
5FC1: 70         LD      (HL),B          
5FC2: CD 81 60   CALL    $6081           
5FC5: 21 50 C2   LD      HL,$C250        
5FC8: 19         ADD     HL,DE           
5FC9: 36 00      LD      (HL),$00        
5FCB: 18 18      JR      $5FE5           
5FCD: 21 50 C2   LD      HL,$C250        
5FD0: 09         ADD     HL,BC           
5FD1: 7E         LD      A,(HL)          
5FD2: A7         AND     A               
5FD3: 28 07      JR      Z,$5FDC         
5FD5: E6 80      AND     $80             
5FD7: 28 02      JR      Z,$5FDB         
5FD9: 34         INC     (HL)            
5FDA: 34         INC     (HL)            
5FDB: 35         DEC     (HL)            
5FDC: CD 81 60   CALL    $6081           
5FDF: 21 D0 C2   LD      HL,$C2D0        
5FE2: 19         ADD     HL,DE           
5FE3: 36 00      LD      (HL),$00        
5FE5: F0 EF      LD      A,($EF)         
5FE7: E6 0F      AND     $0F             
5FE9: FE 00      CP      $00             
5FEB: 20 5A      JR      NZ,$6047        
5FED: F0 EF      LD      A,($EF)         
5FEF: D6 10      SUB     $10             
5FF1: E0 CD      LDFF00  ($CD),A         
5FF3: E6 F0      AND     $F0             
5FF5: 5F         LD      E,A             
5FF6: F0 EE      LD      A,($EE)         
5FF8: D6 08      SUB     $08             
5FFA: E0 CE      LDFF00  ($CE),A         
5FFC: CB 37      SET     1,E             
5FFE: E6 0F      AND     $0F             
6000: B3         OR      E               
6001: 5F         LD      E,A             
6002: 50         LD      D,B             
6003: 21 50 C2   LD      HL,$C250        
6006: 09         ADD     HL,BC           
6007: 7E         LD      A,(HL)          
6008: A7         AND     A               
6009: 28 3C      JR      Z,$6047         
600B: E6 80      AND     $80             
600D: 20 39      JR      NZ,$6048        
600F: 21 11 D7   LD      HL,$D711        
6012: 19         ADD     HL,DE           
6013: 36 4D      LD      (HL),$4D        
6015: CD 39 28   CALL    $2839           
6018: 21 01 D6   LD      HL,$D601        
601B: FA 00 D6   LD      A,($D600)       
601E: 5F         LD      E,A             
601F: C6 0A      ADD     $0A             
6021: EA 00 D6   LD      ($D600),A       
6024: 16 00      LD      D,$00           
6026: 19         ADD     HL,DE           
6027: F0 CF      LD      A,($CF)         
6029: 22         LD      (HLI),A         
602A: F0 D0      LD      A,($D0)         
602C: 22         LD      (HLI),A         
602D: 3E 81      LD      A,$81           
602F: 22         LD      (HLI),A         
6030: 3E 44      LD      A,$44           
6032: 22         LD      (HLI),A         
6033: 3E 54      LD      A,$54           
6035: 22         LD      (HLI),A         
6036: F0 CF      LD      A,($CF)         
6038: 22         LD      (HLI),A         
6039: F0 D0      LD      A,($D0)         
603B: 3C         INC     A               
603C: 22         LD      (HLI),A         
603D: 3E 81      LD      A,$81           
603F: 22         LD      (HLI),A         
6040: 3E 45      LD      A,$45           
6042: 22         LD      (HLI),A         
6043: 3E 55      LD      A,$55           
6045: 22         LD      (HLI),A         
6046: 70         LD      (HL),B          
6047: C9         RET                     
6048: 21 11 D7   LD      HL,$D711        
604B: 19         ADD     HL,DE           
604C: 36 04      LD      (HL),$04        
604E: CD 39 28   CALL    $2839           
6051: 21 01 D6   LD      HL,$D601        
6054: FA 00 D6   LD      A,($D600)       
6057: 5F         LD      E,A             
6058: C6 0A      ADD     $0A             
605A: EA 00 D6   LD      ($D600),A       
605D: 16 00      LD      D,$00           
605F: 19         ADD     HL,DE           
6060: F0 CF      LD      A,($CF)         
6062: 22         LD      (HLI),A         
6063: F0 D0      LD      A,($D0)         
6065: 22         LD      (HLI),A         
6066: 3E 81      LD      A,$81           
6068: 22         LD      (HLI),A         
6069: 3E 7E      LD      A,$7E           
606B: 22         LD      (HLI),A         
606C: 3E 7E      LD      A,$7E           
606E: 22         LD      (HLI),A         
606F: F0 CF      LD      A,($CF)         
6071: 22         LD      (HLI),A         
6072: F0 D0      LD      A,($D0)         
6074: 3C         INC     A               
6075: 22         LD      (HLI),A         
6076: 3E 81      LD      A,$81           
6078: 22         LD      (HLI),A         
6079: 3E 7E      LD      A,$7E           
607B: 22         LD      (HLI),A         
607C: 3E 7E      LD      A,$7E           
607E: 22         LD      (HLI),A         
607F: 70         LD      (HL),B          
6080: C9         RET                     
6081: 21 60 C4   LD      HL,$C460        
6084: 09         ADD     HL,BC           
6085: 7E         LD      A,(HL)          
6086: EE 01      XOR     $01             
6088: E0 D7      LDFF00  ($D7),A         
608A: 58         LD      E,B             
608B: 50         LD      D,B             
608C: 21 80 C2   LD      HL,$C280        
608F: 19         ADD     HL,DE           
6090: 7E         LD      A,(HL)          
6091: A7         AND     A               
6092: 28 12      JR      Z,$60A6         
6094: 21 A0 C3   LD      HL,$C3A0        
6097: 19         ADD     HL,DE           
6098: 7E         LD      A,(HL)          
6099: FE A6      CP      $A6             
609B: 20 09      JR      NZ,$60A6        
609D: 21 60 C4   LD      HL,$C460        
60A0: 19         ADD     HL,DE           
60A1: F0 D7      LD      A,($D7)         
60A3: BE         CP      (HL)            
60A4: 28 06      JR      Z,$60AC         
60A6: 1C         INC     E               
60A7: 7B         LD      A,E             
60A8: FE 10      CP      $10             
60AA: 20 E0      JR      NZ,$608C        
60AC: C9         RET                     
60AD: 00         NOP                     
60AE: 00         NOP                     
60AF: 50         LD      D,B             
60B0: 00         NOP                     
60B1: 00         NOP                     
60B2: 08 52 00   LD      ($0052),SP      
60B5: 00         NOP                     
60B6: 10 52      STOP    $52             
60B8: 20 00      JR      NZ,$60BA        
60BA: 18 50      JR      $610C           
60BC: 20 21      JR      NZ,$60DF        
60BE: AD         XOR     L               
60BF: 60         LD      H,B             
60C0: 0E 04      LD      C,$04           
60C2: CD 26 3D   CALL    $3D26           
60C5: CD 76 7C   CALL    $7C76           
60C8: CD 91 08   CALL    $0891           
60CB: 5F         LD      E,A             
60CC: 21 D0 C3   LD      HL,$C3D0        
60CF: 09         ADD     HL,BC           
60D0: 34         INC     (HL)            
60D1: 7E         LD      A,(HL)          
60D2: E6 03      AND     $03             
60D4: B3         OR      E               
60D5: 20 2C      JR      NZ,$6103        
60D7: F0 EB      LD      A,($EB)         
60D9: FE A4      CP      $A4             
60DB: CA 60 61   JP      Z,$6160         
60DE: 21 B0 C2   LD      HL,$C2B0        
60E1: 09         ADD     HL,BC           
60E2: 5E         LD      E,(HL)          
60E3: 50         LD      D,B             
60E4: 21 5C 61   LD      HL,$615C        
60E7: 19         ADD     HL,DE           
60E8: 7E         LD      A,(HL)          
60E9: 21 40 C2   LD      HL,$C240        
60EC: 09         ADD     HL,BC           
60ED: 86         ADD     A,(HL)          
60EE: 77         LD      (HL),A          
60EF: 21 5E 61   LD      HL,$615E        
60F2: 19         ADD     HL,DE           
60F3: BE         CP      (HL)            
60F4: 20 0D      JR      NZ,$6103        
60F6: 21 B0 C2   LD      HL,$C2B0        
60F9: 09         ADD     HL,BC           
60FA: 7E         LD      A,(HL)          
60FB: EE 01      XOR     $01             
60FD: 77         LD      (HL),A          
60FE: CD 91 08   CALL    $0891           
6101: 36 6A      LD      (HL),$6A        
6103: 21 C0 C2   LD      HL,$C2C0        
6106: 09         ADD     HL,BC           
6107: 70         LD      (HL),B          
6108: F0 EE      LD      A,($EE)         
610A: F5         PUSH    AF              
610B: CD E2 7C   CALL    $7CE2           
610E: F1         POP     AF              
610F: 5F         LD      E,A             
6110: 21 00 C2   LD      HL,$C200        
6113: 09         ADD     HL,BC           
6114: 7E         LD      A,(HL)          
6115: 93         SUB     E               
6116: E0 E8      LDFF00  ($E8),A         
6118: CD 9E 3B   CALL    $3B9E           
611B: CD D5 3B   CALL    $3BD5           
611E: 30 3B      JR      NC,$615B        
6120: F0 9B      LD      A,($9B)         
6122: E6 80      AND     $80             
6124: 20 35      JR      NZ,$615B        
6126: CD 45 7D   CALL    $7D45           
6129: C6 08      ADD     $08             
612B: CB 7F      SET     1,E             
612D: 28 2C      JR      Z,$615B         
612F: 21 10 C2   LD      HL,$C210        
6132: 09         ADD     HL,BC           
6133: 7E         LD      A,(HL)          
6134: D6 10      SUB     $10             
6136: E0 99      LDFF00  ($99),A         
6138: F0 9A      LD      A,($9A)         
613A: F5         PUSH    AF              
613B: F0 E8      LD      A,($E8)         
613D: E0 9A      LDFF00  ($9A),A         
613F: 21 98 FF   LD      HL,$FF98        
6142: 86         ADD     A,(HL)          
6143: 77         LD      (HL),A          
6144: C5         PUSH    BC              
6145: CD 49 3E   CALL    $3E49           
6148: C1         POP     BC              
6149: F1         POP     AF              
614A: E0 9A      LDFF00  ($9A),A         
614C: 3E 02      LD      A,$02           
614E: E0 9B      LDFF00  ($9B),A         
6150: 3E 01      LD      A,$01           
6152: EA 47 C1   LD      ($C147),A       
6155: 21 C0 C2   LD      HL,$C2C0        
6158: 09         ADD     HL,BC           
6159: 36 10      LD      (HL),$10        
615B: C9         RET                     
615C: 01 FF 06   LD      BC,$06FF        
615F: FA 21 B0   LD      A,($B021)       
6162: C2 09 5E   JP      NZ,$5E09        
6165: 50         LD      D,B             
6166: 21 5C 61   LD      HL,$615C        
6169: 19         ADD     HL,DE           
616A: 7E         LD      A,(HL)          
616B: 21 50 C2   LD      HL,$C250        
616E: 09         ADD     HL,BC           
616F: 86         ADD     A,(HL)          
6170: 77         LD      (HL),A          
6171: 21 5E 61   LD      HL,$615E        
6174: 19         ADD     HL,DE           
6175: BE         CP      (HL)            
6176: 20 0D      JR      NZ,$6185        
6178: 21 B0 C2   LD      HL,$C2B0        
617B: 09         ADD     HL,BC           
617C: 7E         LD      A,(HL)          
617D: EE 01      XOR     $01             
617F: 77         LD      (HL),A          
6180: CD 91 08   CALL    $0891           
6183: 36 6A      LD      (HL),$6A        
6185: C3 03 61   JP      $6103           
6188: 00         NOP                     
6189: 00         NOP                     
618A: 50         LD      D,B             
618B: 00         NOP                     
618C: 00         NOP                     
618D: 08 52 00   LD      ($0052),SP      
6190: 00         NOP                     
6191: 10 52      STOP    $52             
6193: 20 00      JR      NZ,$6195        
6195: 18 50      JR      $61E7           
6197: 20 CD      JR      NZ,$6166        
6199: 8C         ADC     A,H             
619A: 08 28 04   LD      ($0428),SP      
619D: 3E 04      LD      A,$04           
619F: E0 F5      LDFF00  ($F5),A         
61A1: 21 88 61   LD      HL,$6188        
61A4: 0E 04      LD      C,$04           
61A6: CD 26 3D   CALL    $3D26           
61A9: CD 76 7C   CALL    $7C76           
61AC: CD 03 61   CALL    $6103           
61AF: 21 C0 C2   LD      HL,$C2C0        
61B2: 09         ADD     HL,BC           
61B3: 7E         LD      A,(HL)          
61B4: A7         AND     A               
61B5: 28 39      JR      Z,$61F0         
61B7: 1E 04      LD      E,$04           
61B9: F0 F6      LD      A,($F6)         
61BB: FE 3B      CP      $3B             
61BD: 28 0D      JR      Z,$61CC         
61BF: CD 8C 08   CALL    $088C           
61C2: 36 08      LD      (HL),$08        
61C4: FA CF C3   LD      A,($C3CF)       
61C7: A7         AND     A               
61C8: 28 26      JR      Z,$61F0         
61CA: 1E 04      LD      E,$04           
61CC: 21 40 C4   LD      HL,$C440        
61CF: 09         ADD     HL,BC           
61D0: 7E         LD      A,(HL)          
61D1: FE 04      CP      $04             
61D3: 28 09      JR      Z,$61DE         
61D5: 34         INC     (HL)            
61D6: FE 03      CP      $03             
61D8: 20 04      JR      NZ,$61DE        
61DA: 3E 11      LD      A,$11           
61DC: E0 F4      LDFF00  ($F4),A         
61DE: F0 E7      LD      A,($E7)         
61E0: E6 03      AND     $03             
61E2: 20 0B      JR      NZ,$61EF        
61E4: 21 50 C2   LD      HL,$C250        
61E7: 09         ADD     HL,BC           
61E8: 7E         LD      A,(HL)          
61E9: 93         SUB     E               
61EA: E6 80      AND     $80             
61EC: 28 01      JR      Z,$61EF         
61EE: 34         INC     (HL)            
61EF: C9         RET                     
61F0: 21 50 C2   LD      HL,$C250        
61F3: 09         ADD     HL,BC           
61F4: 70         LD      (HL),B          
61F5: 21 40 C4   LD      HL,$C440        
61F8: 09         ADD     HL,BC           
61F9: 70         LD      (HL),B          
61FA: C9         RET                     
61FB: 21 F0 C3   LD      HL,$C3F0        
61FE: 09         ADD     HL,BC           
61FF: 70         LD      (HL),B          
6200: 21 00 C4   LD      HL,$C400        
6203: 09         ADD     HL,BC           
6204: 70         LD      (HL),B          
6205: CD 31 63   CALL    $6331           
6208: CD 76 7C   CALL    $7C76           
620B: 21 C0 C2   LD      HL,$C2C0        
620E: 09         ADD     HL,BC           
620F: 7E         LD      A,(HL)          
6210: A7         AND     A               
6211: 20 08      JR      NZ,$621B        
6213: 34         INC     (HL)            
6214: F0 EF      LD      A,($EF)         
6216: 21 B0 C2   LD      HL,$C2B0        
6219: 09         ADD     HL,BC           
621A: 77         LD      (HL),A          
621B: CD 98 7C   CALL    $7C98           
621E: F0 F0      LD      A,($F0)         
6220: C7         RST     0X00            
6221: 29         ADD     HL,HL           
6222: 62         LD      H,D             
6223: 4D         LD      C,L             
6224: 62         LD      H,D             
6225: 7A         LD      A,D             
6226: 62         LD      H,D             
6227: A3         AND     E               
6228: 62         LD      H,D             
6229: CD 91 08   CALL    $0891           
622C: 20 0E      JR      NZ,$623C        
622E: 36 40      LD      (HL),$40        
6230: CD 35 7D   CALL    $7D35           
6233: C6 10      ADD     $10             
6235: FE 20      CP      $20             
6237: 38 03      JR      C,$623C         
6239: CD 8D 3B   CALL    $3B8D           
623C: C9         RET                     
623D: 04         INC     B               
623E: 04         INC     B               
623F: 03         INC     BC              
6240: 02         LD      (BC),A          
6241: 01 00 00   LD      BC,$0000        
6244: 00         NOP                     
6245: E0 E0      LDFF00  ($E0),A         
6247: E8 F0      ADD     SP,$F0          
6249: 00         NOP                     
624A: 00         NOP                     
624B: 00         NOP                     
624C: 00         NOP                     
624D: CD B4 3B   CALL    $3BB4           
6250: CD 91 08   CALL    $0891           
6253: 20 06      JR      NZ,$625B        
6255: 36 80      LD      (HL),$80        
6257: CD 8D 3B   CALL    $3B8D           
625A: C9         RET                     
625B: 1F         RRA                     
625C: 1F         RRA                     
625D: 1F         RRA                     
625E: E6 07      AND     $07             
6260: 5F         LD      E,A             
6261: 50         LD      D,B             
6262: 21 3D 62   LD      HL,$623D        
6265: 19         ADD     HL,DE           
6266: 7E         LD      A,(HL)          
6267: CD 87 3B   CALL    $3B87           
626A: 21 45 62   LD      HL,$6245        
626D: 19         ADD     HL,DE           
626E: 7E         LD      A,(HL)          
626F: 21 B0 C2   LD      HL,$C2B0        
6272: 09         ADD     HL,BC           
6273: 86         ADD     A,(HL)          
6274: 21 10 C2   LD      HL,$C210        
6277: 09         ADD     HL,BC           
6278: 77         LD      (HL),A          
6279: C9         RET                     
627A: CD B4 3B   CALL    $3BB4           
627D: CD 91 08   CALL    $0891           
6280: 20 05      JR      NZ,$6287        
6282: 36 40      LD      (HL),$40        
6284: CD 8D 3B   CALL    $3B8D           
6287: 1E 04      LD      E,$04           
6289: E6 10      AND     $10             
628B: 20 01      JR      NZ,$628E        
628D: 1C         INC     E               
628E: 7B         LD      A,E             
628F: CD 87 3B   CALL    $3B87           
6292: C9         RET                     
6293: 00         NOP                     
6294: 00         NOP                     
6295: 00         NOP                     
6296: 00         NOP                     
6297: 01 02 03   LD      BC,$0302        
629A: 05         DEC     B               
629B: 00         NOP                     
629C: 00         NOP                     
629D: 00         NOP                     
629E: 00         NOP                     
629F: 00         NOP                     
62A0: F0 E8      LD      A,($E8)         
62A2: E0 CD      LDFF00  ($CD),A         
62A4: B4         OR      H               
62A5: 3B         DEC     SP              
62A6: CD 91 08   CALL    $0891           
62A9: 20 07      JR      NZ,$62B2        
62AB: 36 40      LD      (HL),$40        
62AD: CD 8D 3B   CALL    $3B8D           
62B0: 70         LD      (HL),B          
62B1: C9         RET                     
62B2: 1F         RRA                     
62B3: 1F         RRA                     
62B4: 1F         RRA                     
62B5: E6 07      AND     $07             
62B7: 5F         LD      E,A             
62B8: 50         LD      D,B             
62B9: 21 93 62   LD      HL,$6293        
62BC: 19         ADD     HL,DE           
62BD: 7E         LD      A,(HL)          
62BE: CD 87 3B   CALL    $3B87           
62C1: 21 9B 62   LD      HL,$629B        
62C4: 19         ADD     HL,DE           
62C5: 7E         LD      A,(HL)          
62C6: 21 B0 C2   LD      HL,$C2B0        
62C9: 09         ADD     HL,BC           
62CA: 86         ADD     A,(HL)          
62CB: 21 10 C2   LD      HL,$C210        
62CE: 09         ADD     HL,BC           
62CF: 77         LD      (HL),A          
62D0: C9         RET                     
62D1: FF         RST     0X38            
62D2: FF         RST     0X38            
62D3: FF         RST     0X38            
62D4: FF         RST     0X38            
62D5: FF         RST     0X38            
62D6: FF         RST     0X38            
62D7: FF         RST     0X38            
62D8: FF         RST     0X38            
62D9: FF         RST     0X38            
62DA: FF         RST     0X38            
62DB: FF         RST     0X38            
62DC: FF         RST     0X38            
62DD: FF         RST     0X38            
62DE: FF         RST     0X38            
62DF: FF         RST     0X38            
62E0: FF         RST     0X38            
62E1: F0 00      LD      A,($00)         
62E3: 74         LD      (HL),H          
62E4: 00         NOP                     
62E5: F0 08      LD      A,($08)         
62E7: 74         LD      (HL),H          
62E8: 20 FF      JR      NZ,$62E9        
62EA: FF         RST     0X38            
62EB: FF         RST     0X38            
62EC: FF         RST     0X38            
62ED: FF         RST     0X38            
62EE: FF         RST     0X38            
62EF: FF         RST     0X38            
62F0: FF         RST     0X38            
62F1: 00         NOP                     
62F2: 00         NOP                     
62F3: 70         LD      (HL),B          
62F4: 00         NOP                     
62F5: 00         NOP                     
62F6: 08 70 20   LD      ($2070),SP      
62F9: FF         RST     0X38            
62FA: FF         RST     0X38            
62FB: FF         RST     0X38            
62FC: FF         RST     0X38            
62FD: FF         RST     0X38            
62FE: FF         RST     0X38            
62FF: FF         RST     0X38            
6300: FF         RST     0X38            
6301: F8 00      LDHL    SP,$00          
6303: 74         LD      (HL),H          
6304: 00         NOP                     
6305: F8 08      LDHL    SP,$08          
6307: 74         LD      (HL),H          
6308: 20 08      JR      NZ,$6312        
630A: 00         NOP                     
630B: 76         HALT                    
630C: 00         NOP                     
630D: 08 08 76   LD      ($7608),SP      
6310: 20 00      JR      NZ,$6312        
6312: 00         NOP                     
6313: 70         LD      (HL),B          
6314: 00         NOP                     
6315: 00         NOP                     
6316: 08 70 20   LD      ($2070),SP      
6319: 10 00      STOP    $00             
631B: 72         LD      (HL),D          
631C: 00         NOP                     
631D: 10 08      STOP    $08             
631F: 72         LD      (HL),D          
6320: 20 00      JR      NZ,$6322        
6322: 00         NOP                     
6323: 78         LD      A,B             
6324: 00         NOP                     
6325: 00         NOP                     
6326: 08 78 20   LD      ($2078),SP      
6329: 10 00      STOP    $00             
632B: 72         LD      (HL),D          
632C: 00         NOP                     
632D: 10 08      STOP    $08             
632F: 72         LD      (HL),D          
6330: 20 F0      JR      NZ,$6322        
6332: F1         POP     AF              
6333: 17         RLA                     
6334: 17         RLA                     
6335: 17         RLA                     
6336: 17         RLA                     
6337: E6 F0      AND     $F0             
6339: 5F         LD      E,A             
633A: 50         LD      D,B             
633B: 21 D1 62   LD      HL,$62D1        
633E: 19         ADD     HL,DE           
633F: 0E 04      LD      C,$04           
6341: CD 26 3D   CALL    $3D26           
6344: C9         RET                     
6345: 98         SBC     B               
6346: 00         NOP                     
6347: 53         LD      D,E             
6348: 7F         LD      A,A             
6349: 98         SBC     B               
634A: 20 53      JR      NZ,$639F        
634C: 7F         LD      A,A             
634D: 98         SBC     B               
634E: 40         LD      B,B             
634F: 53         LD      D,E             
6350: 7F         LD      A,A             
6351: 98         SBC     B               
6352: 60         LD      H,B             
6353: 53         LD      D,E             
6354: 7F         LD      A,A             
6355: 98         SBC     B               
6356: 80         ADD     A,B             
6357: 53         LD      D,E             
6358: 7F         LD      A,A             
6359: 98         SBC     B               
635A: A0         AND     B               
635B: 53         LD      D,E             
635C: 7F         LD      A,A             
635D: 98         SBC     B               
635E: C0         RET     NZ              
635F: 53         LD      D,E             
6360: 7F         LD      A,A             
6361: 98         SBC     B               
6362: E0 53      LDFF00  ($53),A         
6364: 7F         LD      A,A             
6365: 99         SBC     C               
6366: 00         NOP                     
6367: 53         LD      D,E             
6368: 7F         LD      A,A             
6369: 99         SBC     C               
636A: 20 53      JR      NZ,$63BF        
636C: 7F         LD      A,A             
636D: 99         SBC     C               
636E: 40         LD      B,B             
636F: 53         LD      D,E             
6370: 7F         LD      A,A             
6371: 99         SBC     C               
6372: 60         LD      H,B             
6373: 53         LD      D,E             
6374: 7F         LD      A,A             
6375: 99         SBC     C               
6376: 80         ADD     A,B             
6377: 53         LD      D,E             
6378: 7F         LD      A,A             
6379: 99         SBC     C               
637A: A0         AND     B               
637B: 53         LD      D,E             
637C: 7F         LD      A,A             
637D: 99         SBC     C               
637E: C0         RET     NZ              
637F: 53         LD      D,E             
6380: 7F         LD      A,A             
6381: 99         SBC     C               
6382: E0 53      LDFF00  ($53),A         
6384: 7F         LD      A,A             
6385: 9A         SBC     D               
6386: 00         NOP                     
6387: 53         LD      D,E             
6388: 7F         LD      A,A             
6389: 9A         SBC     D               
638A: 20 53      JR      NZ,$63DF        
638C: 7F         LD      A,A             
638D: AF         XOR     A               
638E: E0 96      LDFF00  ($96),A         
6390: E0 97      LDFF00  ($97),A         
6392: EA 2F C1   LD      ($C12F),A       
6395: EA 2E C1   LD      ($C12E),A       
6398: 21 FD D6   LD      HL,$D6FD        
639B: CB AE      SET     1,E             
639D: 21 D0 C3   LD      HL,$C3D0        
63A0: 09         ADD     HL,BC           
63A1: 7E         LD      A,(HL)          
63A2: FE 09      CP      $09             
63A4: 28 2C      JR      Z,$63D2         
63A6: FA 00 D6   LD      A,($D600)       
63A9: 5F         LD      E,A             
63AA: C6 08      ADD     $08             
63AC: EA 00 D6   LD      ($D600),A       
63AF: 50         LD      D,B             
63B0: C5         PUSH    BC              
63B1: 21 D0 C3   LD      HL,$C3D0        
63B4: 09         ADD     HL,BC           
63B5: 4E         LD      C,(HL)          
63B6: 34         INC     (HL)            
63B7: CB 21      SET     1,E             
63B9: CB 21      SET     1,E             
63BB: CB 21      SET     1,E             
63BD: 21 45 63   LD      HL,$6345        
63C0: 09         ADD     HL,BC           
63C1: E5         PUSH    HL              
63C2: C1         POP     BC              
63C3: 21 01 D6   LD      HL,$D601        
63C6: 19         ADD     HL,DE           
63C7: 1E 08      LD      E,$08           
63C9: 0A         LD      A,(BC)          
63CA: 03         INC     BC              
63CB: 22         LD      (HLI),A         
63CC: 1D         DEC     E               
63CD: 20 FA      JR      NZ,$63C9        
63CF: 70         LD      (HL),B          
63D0: C1         POP     BC              
63D1: C9         RET                     
63D2: CD 91 08   CALL    $0891           
63D5: C0         RET     NZ              
63D6: F0 F7      LD      A,($F7)         
63D8: C6 50      ADD     $50             
63DA: CD 85 21   CALL    $2185           
63DD: 3E E4      LD      A,$E4           
63DF: EA 97 DB   LD      ($DB97),A       
63E2: C3 7C 7D   JP      $7D7C           
63E5: 4A         LD      C,D             
63E6: 00         NOP                     
63E7: 4C         LD      C,H             
63E8: 00         NOP                     
63E9: 4C         LD      C,H             
63EA: 20 4A      JR      NZ,$6436        
63EC: 20 4E      JR      NZ,$643C        
63EE: 00         NOP                     
63EF: 4E         LD      C,(HL)          
63F0: 20 21      JR      NZ,$6413        
63F2: B0         OR      B               
63F3: C2 09 7E   JP      NZ,$7E09        
63F6: A7         AND     A               
63F7: C2 8D 63   JP      NZ,$638D        
63FA: 11 E5 63   LD      DE,$63E5        
63FD: CD 3B 3C   CALL    $3C3B           
6400: CD 76 7C   CALL    $7C76           
6403: CD 98 7C   CALL    $7C98           
6406: F0 F9      LD      A,($F9)         
6408: A7         AND     A               
6409: C2 AD 64   JP      NZ,$64AD        
640C: F0 F0      LD      A,($F0)         
640E: C7         RST     0X00            
640F: 1D         DEC     E               
6410: 64         LD      H,H             
6411: 61         LD      H,C             
6412: 64         LD      H,H             
6413: 84         ADD     A,H             
6414: 64         LD      H,H             
6415: 08 F8 00   LD      ($00F8),SP      
6418: 00         NOP                     
6419: 00         NOP                     
641A: 00         NOP                     
641B: F8 08      LDHL    SP,$08          
641D: CD EB 3B   CALL    $3BEB           
6420: CD 0E 65   CALL    $650E           
6423: CD 91 08   CALL    $0891           
6426: 20 37      JR      NZ,$645F        
6428: CD ED 27   CALL    $27ED           
642B: E6 3F      AND     $3F             
642D: C6 30      ADD     $30             
642F: 77         LD      (HL),A          
6430: 21 D0 C3   LD      HL,$C3D0        
6433: 09         ADD     HL,BC           
6434: 7E         LD      A,(HL)          
6435: 3C         INC     A               
6436: 77         LD      (HL),A          
6437: FE 04      CP      $04             
6439: 20 06      JR      NZ,$6441        
643B: 70         LD      (HL),B          
643C: CD 55 7D   CALL    $7D55           
643F: 18 06      JR      $6447           
6441: CD ED 27   CALL    $27ED           
6444: E6 03      AND     $03             
6446: 5F         LD      E,A             
6447: 50         LD      D,B             
6448: 21 15 64   LD      HL,$6415        
644B: 19         ADD     HL,DE           
644C: 7E         LD      A,(HL)          
644D: 21 40 C2   LD      HL,$C240        
6450: 09         ADD     HL,BC           
6451: 77         LD      (HL),A          
6452: 21 19 64   LD      HL,$6419        
6455: 19         ADD     HL,DE           
6456: 7E         LD      A,(HL)          
6457: 21 50 C2   LD      HL,$C250        
645A: 09         ADD     HL,BC           
645B: 77         LD      (HL),A          
645C: CD 8D 3B   CALL    $3B8D           
645F: 18 17      JR      $6478           
6461: CD EB 3B   CALL    $3BEB           
6464: CD 0E 65   CALL    $650E           
6467: CD 91 08   CALL    $0891           
646A: 20 06      JR      NZ,$6472        
646C: 36 20      LD      (HL),$20        
646E: CD 8D 3B   CALL    $3B8D           
6471: 70         LD      (HL),B          
6472: CD E2 7C   CALL    $7CE2           
6475: CD 9E 3B   CALL    $3B9E           
6478: F0 E7      LD      A,($E7)         
647A: 1F         RRA                     
647B: 1F         RRA                     
647C: 1F         RRA                     
647D: 1F         RRA                     
647E: E6 01      AND     $01             
6480: CD 87 3B   CALL    $3B87           
6483: C9         RET                     
6484: 21 40 C3   LD      HL,$C340        
6487: 09         ADD     HL,BC           
6488: 36 C2      LD      (HL),$C2        
648A: CD 91 08   CALL    $0891           
648D: 20 18      JR      NZ,$64A7        
648F: 21 E0 C4   LD      HL,$C4E0        
6492: 09         ADD     HL,BC           
6493: 36 2D      LD      (HL),$2D        
6495: 21 80 C4   LD      HL,$C480        
6498: 09         ADD     HL,BC           
6499: 36 0C      LD      (HL),$0C        
649B: 21 80 C2   LD      HL,$C280        
649E: 09         ADD     HL,BC           
649F: 36 01      LD      (HL),$01        
64A1: 21 40 C3   LD      HL,$C340        
64A4: 09         ADD     HL,BC           
64A5: 36 04      LD      (HL),$04        
64A7: 3E 02      LD      A,$02           
64A9: CD 87 3B   CALL    $3B87           
64AC: C9         RET                     
64AD: F0 F0      LD      A,($F0)         
64AF: FE 02      CP      $02             
64B1: 28 D1      JR      Z,$6484         
64B3: CD EB 3B   CALL    $3BEB           
64B6: CD 1A 65   CALL    $651A           
64B9: F0 F0      LD      A,($F0)         
64BB: C7         RST     0X00            
64BC: C0         RET     NZ              
64BD: 64         LD      H,H             
64BE: D2 64 CD   JP      NC,$CD64        
64C1: 35         DEC     (HL)            
64C2: 7D         LD      A,L             
64C3: 3E 08      LD      A,$08           
64C5: 1D         DEC     E               
64C6: 20 02      JR      NZ,$64CA        
64C8: 3E F8      LD      A,$F8           
64CA: 21 40 C2   LD      HL,$C240        
64CD: 09         ADD     HL,BC           
64CE: 77         LD      (HL),A          
64CF: C3 8D 3B   JP      $3B8D           
64D2: CD E2 7C   CALL    $7CE2           
64D5: 21 50 C2   LD      HL,$C250        
64D8: 09         ADD     HL,BC           
64D9: 34         INC     (HL)            
64DA: 34         INC     (HL)            
64DB: CD 9E 3B   CALL    $3B9E           
64DE: 21 A0 C2   LD      HL,$C2A0        
64E1: 09         ADD     HL,BC           
64E2: 7E         LD      A,(HL)          
64E3: E6 03      AND     $03             
64E5: 28 08      JR      Z,$64EF         
64E7: 21 40 C2   LD      HL,$C240        
64EA: 09         ADD     HL,BC           
64EB: 7E         LD      A,(HL)          
64EC: 2F         CPL                     
64ED: 3C         INC     A               
64EE: 77         LD      (HL),A          
64EF: 21 A0 C2   LD      HL,$C2A0        
64F2: 09         ADD     HL,BC           
64F3: 7E         LD      A,(HL)          
64F4: E6 08      AND     $08             
64F6: 28 12      JR      Z,$650A         
64F8: 21 10 C2   LD      HL,$C210        
64FB: 09         ADD     HL,BC           
64FC: 7E         LD      A,(HL)          
64FD: E6 F0      AND     $F0             
64FF: C6 03      ADD     $03             
6501: 77         LD      (HL),A          
6502: 21 50 C2   LD      HL,$C250        
6505: 09         ADD     HL,BC           
6506: 70         LD      (HL),B          
6507: C3 78 64   JP      $6478           
650A: AF         XOR     A               
650B: C3 87 3B   JP      $3B87           
650E: F0 A2      LD      A,($A2)         
6510: A7         AND     A               
6511: CA D5 3B   JP      Z,$3BD5         
6514: FE 08      CP      $08             
6516: DA D5 3B   JP      C,$3BD5         
6519: C9         RET                     
651A: C3 D5 3B   JP      $3BD5           
651D: 40         LD      B,B             
651E: 00         NOP                     
651F: 40         LD      B,B             
6520: 20 42      JR      NZ,$6564        
6522: 00         NOP                     
6523: 42         LD      B,D             
6524: 20 11      JR      NZ,$6537        
6526: 1D         DEC     E               
6527: 65         LD      H,L             
6528: CD 3B 3C   CALL    $3C3B           
652B: CD 76 7C   CALL    $7C76           
652E: CD 98 7C   CALL    $7C98           
6531: CD B4 3B   CALL    $3BB4           
6534: CD E2 7C   CALL    $7CE2           
6537: CD 1B 7D   CALL    $7D1B           
653A: CD 9E 3B   CALL    $3B9E           
653D: 21 50 C3   LD      HL,$C350        
6540: 09         ADD     HL,BC           
6541: CB FE      SET     1,E             
6543: 21 30 C4   LD      HL,$C430        
6546: 09         ADD     HL,BC           
6547: CB F6      SET     1,E             
6549: F0 F0      LD      A,($F0)         
654B: C7         RST     0X00            
654C: 52         LD      D,D             
654D: 65         LD      H,L             
654E: AD         XOR     L               
654F: 65         LD      H,L             
6550: F5         PUSH    AF              
6551: 65         LD      H,L             
6552: 21 10 C3   LD      HL,$C310        
6555: 09         ADD     HL,BC           
6556: 7E         LD      A,(HL)          
6557: A7         AND     A               
6558: 28 09      JR      Z,$6563         
655A: F0 E7      LD      A,($E7)         
655C: E6 07      AND     $07             
655E: 20 0F      JR      NZ,$656F        
6560: 35         DEC     (HL)            
6561: 18 0C      JR      $656F           
6563: 21 50 C3   LD      HL,$C350        
6566: 09         ADD     HL,BC           
6567: CB BE      SET     1,E             
6569: 21 30 C4   LD      HL,$C430        
656C: 09         ADD     HL,BC           
656D: CB B6      SET     1,E             
656F: F0 E7      LD      A,($E7)         
6571: E6 07      AND     $07             
6573: 20 1E      JR      NZ,$6593        
6575: 21 40 C2   LD      HL,$C240        
6578: 09         ADD     HL,BC           
6579: 7E         LD      A,(HL)          
657A: A7         AND     A               
657B: 28 07      JR      Z,$6584         
657D: E6 80      AND     $80             
657F: 28 02      JR      Z,$6583         
6581: 34         INC     (HL)            
6582: 34         INC     (HL)            
6583: 35         DEC     (HL)            
6584: 21 50 C2   LD      HL,$C250        
6587: 09         ADD     HL,BC           
6588: 7E         LD      A,(HL)          
6589: A7         AND     A               
658A: 28 07      JR      Z,$6593         
658C: E6 80      AND     $80             
658E: 28 02      JR      Z,$6592         
6590: 34         INC     (HL)            
6591: 34         INC     (HL)            
6592: 35         DEC     (HL)            
6593: CD 87 08   CALL    $0887           
6596: 20 03      JR      NZ,$659B        
6598: CD 8D 3B   CALL    $3B8D           
659B: 21 B0 C2   LD      HL,$C2B0        
659E: 09         ADD     HL,BC           
659F: 7E         LD      A,(HL)          
65A0: A7         AND     A               
65A1: 28 07      JR      Z,$65AA         
65A3: F0 E7      LD      A,($E7)         
65A5: E6 1F      AND     $1F             
65A7: 20 01      JR      NZ,$65AA        
65A9: 35         DEC     (HL)            
65AA: C3 CB 65   JP      $65CB           
65AD: 21 B0 C2   LD      HL,$C2B0        
65B0: 09         ADD     HL,BC           
65B1: 7E         LD      A,(HL)          
65B2: FE 08      CP      $08             
65B4: 38 0E      JR      C,$65C4         
65B6: CD 87 08   CALL    $0887           
65B9: CD ED 27   CALL    $27ED           
65BC: E6 1F      AND     $1F             
65BE: C6 80      ADD     $80             
65C0: 77         LD      (HL),A          
65C1: C3 8D 3B   JP      $3B8D           
65C4: F0 E7      LD      A,($E7)         
65C6: E6 0F      AND     $0F             
65C8: 20 01      JR      NZ,$65CB        
65CA: 34         INC     (HL)            
65CB: 21 B0 C2   LD      HL,$C2B0        
65CE: 09         ADD     HL,BC           
65CF: 7E         LD      A,(HL)          
65D0: 21 D0 C3   LD      HL,$C3D0        
65D3: 09         ADD     HL,BC           
65D4: 86         ADD     A,(HL)          
65D5: 77         LD      (HL),A          
65D6: 1F         RRA                     
65D7: 1F         RRA                     
65D8: 1F         RRA                     
65D9: 1F         RRA                     
65DA: 1F         RRA                     
65DB: E6 01      AND     $01             
65DD: CD 87 3B   CALL    $3B87           
65E0: C9         RET                     
65E1: 00         NOP                     
65E2: 05         DEC     B               
65E3: 0A         LD      A,(BC)          
65E4: 0D         DEC     C               
65E5: 0E 0D      LD      C,$0D           
65E7: 0A         LD      A,(BC)          
65E8: 05         DEC     B               
65E9: 00         NOP                     
65EA: FB         EI                      
65EB: F6 F3      OR      $F3             
65ED: F2         ???                     
65EE: F3         DI                      
65EF: F6 FB      OR      $FB             
65F1: 00         NOP                     
65F2: 05         DEC     B               
65F3: 0A         LD      A,(BC)          
65F4: 0D         DEC     C               
65F5: CD CB 65   CALL    $65CB           
65F8: 21 10 C3   LD      HL,$C310        
65FB: 09         ADD     HL,BC           
65FC: 7E         LD      A,(HL)          
65FD: FE 10      CP      $10             
65FF: 28 08      JR      Z,$6609         
6601: F0 E7      LD      A,($E7)         
6603: E6 07      AND     $07             
6605: 20 01      JR      NZ,$6608        
6607: 34         INC     (HL)            
6608: C9         RET                     
6609: CD 87 08   CALL    $0887           
660C: 20 06      JR      NZ,$6614        
660E: 36 60      LD      (HL),$60        
6610: CD 8D 3B   CALL    $3B8D           
6613: 70         LD      (HL),B          
6614: 21 D0 C2   LD      HL,$C2D0        
6617: 09         ADD     HL,BC           
6618: 34         INC     (HL)            
6619: 7E         LD      A,(HL)          
661A: FE 18      CP      $18             
661C: 38 3E      JR      C,$665C         
661E: 70         LD      (HL),B          
661F: 21 C0 C2   LD      HL,$C2C0        
6622: 09         ADD     HL,BC           
6623: 7E         LD      A,(HL)          
6624: 21 40 C4   LD      HL,$C440        
6627: 09         ADD     HL,BC           
6628: 86         ADD     A,(HL)          
6629: E6 0F      AND     $0F             
662B: 77         LD      (HL),A          
662C: 21 40 C4   LD      HL,$C440        
662F: 09         ADD     HL,BC           
6630: 5E         LD      E,(HL)          
6631: 50         LD      D,B             
6632: 21 E1 65   LD      HL,$65E1        
6635: 19         ADD     HL,DE           
6636: 7E         LD      A,(HL)          
6637: CB 2F      SET     1,E             
6639: 21 50 C2   LD      HL,$C250        
663C: 09         ADD     HL,BC           
663D: 77         LD      (HL),A          
663E: 21 E5 65   LD      HL,$65E5        
6641: 19         ADD     HL,DE           
6642: 7E         LD      A,(HL)          
6643: CB 2F      SET     1,E             
6645: 21 40 C2   LD      HL,$C240        
6648: 09         ADD     HL,BC           
6649: 77         LD      (HL),A          
664A: CD ED 27   CALL    $27ED           
664D: E6 07      AND     $07             
664F: 20 0B      JR      NZ,$665C        
6651: CD ED 27   CALL    $27ED           
6654: E6 02      AND     $02             
6656: 3D         DEC     A               
6657: 21 C0 C2   LD      HL,$C2C0        
665A: 09         ADD     HL,BC           
665B: 77         LD      (HL),A          
665C: C9         RET                     
665D: 44         LD      B,H             
665E: 00         NOP                     
665F: 46         LD      B,(HL)          
6660: 00         NOP                     
6661: 44         LD      B,H             
6662: 00         NOP                     
6663: 48         LD      C,B             
6664: 00         NOP                     
6665: 46         LD      B,(HL)          
6666: 20 44      JR      NZ,$66AC        
6668: 20 48      JR      NZ,$66B2        
666A: 20 44      JR      NZ,$66B0        
666C: 20 21      JR      NZ,$668F        
666E: 80         ADD     A,B             
666F: C3 09 F0   JP      $F009           
6672: F1         POP     AF              
6673: 86         ADD     A,(HL)          
6674: E0 F1      LDFF00  ($F1),A         
6676: 11 5D 66   LD      DE,$665D        
6679: CD 3B 3C   CALL    $3C3B           
667C: CD 76 7C   CALL    $7C76           
667F: CD 98 7C   CALL    $7C98           
6682: CD B4 3B   CALL    $3BB4           
6685: CD E2 7C   CALL    $7CE2           
6688: CD 9E 3B   CALL    $3B9E           
668B: 21 A0 C2   LD      HL,$C2A0        
668E: 09         ADD     HL,BC           
668F: 7E         LD      A,(HL)          
6690: A7         AND     A               
6691: 28 0E      JR      Z,$66A1         
6693: CD 8D 3B   CALL    $3B8D           
6696: 70         LD      (HL),B          
6697: CD 91 08   CALL    $0891           
669A: 36 08      LD      (HL),$08        
669C: CD 8C 08   CALL    $088C           
669F: 36 20      LD      (HL),$20        
66A1: F0 F0      LD      A,($F0)         
66A3: C7         RST     0X00            
66A4: B6         OR      (HL)            
66A5: 66         LD      H,(HL)          
66A6: F8 66      LDHL    SP,$66          
66A8: 4B         LD      C,E             
66A9: 67         LD      H,A             
66AA: 08 F8 00   LD      ($00F8),SP      
66AD: 00         NOP                     
66AE: 00         NOP                     
66AF: 00         NOP                     
66B0: F8 08      LDHL    SP,$08          
66B2: 02         LD      (BC),A          
66B3: 00         NOP                     
66B4: FF         RST     0X38            
66B5: FF         RST     0X38            
66B6: CD 91 08   CALL    $0891           
66B9: 20 35      JR      NZ,$66F0        
66BB: CD 8D 3B   CALL    $3B8D           
66BE: CD 91 08   CALL    $0891           
66C1: CD ED 27   CALL    $27ED           
66C4: E6 1F      AND     $1F             
66C6: C6 30      ADD     $30             
66C8: 77         LD      (HL),A          
66C9: E6 03      AND     $03             
66CB: 5F         LD      E,A             
66CC: 50         LD      D,B             
66CD: 21 AA 66   LD      HL,$66AA        
66D0: 19         ADD     HL,DE           
66D1: 7E         LD      A,(HL)          
66D2: 21 40 C2   LD      HL,$C240        
66D5: 09         ADD     HL,BC           
66D6: 77         LD      (HL),A          
66D7: 21 AE 66   LD      HL,$66AE        
66DA: 19         ADD     HL,DE           
66DB: 7E         LD      A,(HL)          
66DC: 21 50 C2   LD      HL,$C250        
66DF: 09         ADD     HL,BC           
66E0: 77         LD      (HL),A          
66E1: 21 B2 66   LD      HL,$66B2        
66E4: 19         ADD     HL,DE           
66E5: 7E         LD      A,(HL)          
66E6: FE FF      CP      $FF             
66E8: 28 05      JR      Z,$66EF         
66EA: 21 80 C3   LD      HL,$C380        
66ED: 09         ADD     HL,BC           
66EE: 77         LD      (HL),A          
66EF: C9         RET                     
66F0: CD AF 3D   CALL    $3DAF           
66F3: CD 11 67   CALL    $6711           
66F6: 18 0E      JR      $6706           
66F8: CD 91 08   CALL    $0891           
66FB: 20 06      JR      NZ,$6703        
66FD: 36 18      LD      (HL),$18        
66FF: CD 8D 3B   CALL    $3B8D           
6702: 70         LD      (HL),B          
6703: CD 11 67   CALL    $6711           
6706: F0 E7      LD      A,($E7)         
6708: 1F         RRA                     
6709: 1F         RRA                     
670A: 1F         RRA                     
670B: E6 01      AND     $01             
670D: CD 87 3B   CALL    $3B87           
6710: C9         RET                     
6711: CD 8C 08   CALL    $088C           
6714: 20 25      JR      NZ,$673B        
6716: CD 35 7D   CALL    $7D35           
6719: C6 08      ADD     $08             
671B: FE 10      CP      $10             
671D: 30 1D      JR      NC,$673C        
671F: CD 45 7D   CALL    $7D45           
6722: CD CC 66   CALL    $66CC           
6725: 21 40 C2   LD      HL,$C240        
6728: 09         ADD     HL,BC           
6729: CB 26      SET     1,E             
672B: 21 50 C2   LD      HL,$C250        
672E: 09         ADD     HL,BC           
672F: CB 26      SET     1,E             
6731: CD 8D 3B   CALL    $3B8D           
6734: 36 02      LD      (HL),$02        
6736: CD 91 08   CALL    $0891           
6739: 36 30      LD      (HL),$30        
673B: C9         RET                     
673C: CD 45 7D   CALL    $7D45           
673F: C6 08      ADD     $08             
6741: FE 10      CP      $10             
6743: 30 05      JR      NC,$674A        
6745: CD 35 7D   CALL    $7D35           
6748: 18 D8      JR      $6722           
674A: C9         RET                     
674B: CD 91 08   CALL    $0891           
674E: 20 0B      JR      NZ,$675B        
6750: 36 20      LD      (HL),$20        
6752: CD 8D 3B   CALL    $3B8D           
6755: 70         LD      (HL),B          
6756: CD 8C 08   CALL    $088C           
6759: 36 40      LD      (HL),$40        
675B: F0 E7      LD      A,($E7)         
675D: 1F         RRA                     
675E: 1F         RRA                     
675F: E6 01      AND     $01             
6761: CD 87 3B   CALL    $3B87           
6764: C9         RET                     
6765: 55         LD      D,L             
6766: 56         LD      D,(HL)          
6767: 0A         LD      A,(BC)          
6768: 0B         DEC     BC              
6769: 0C         INC     C               
676A: 0D         DEC     C               
676B: 0E 0F      LD      C,$0F           
676D: 55         LD      D,L             
676E: 56         LD      D,(HL)          
676F: 55         LD      D,L             
6770: 56         LD      D,(HL)          
6771: 1A         LD      A,(DE)          
6772: 1B         DEC     DE              
6773: 1C         INC     E               
6774: 1D         DEC     E               
6775: 1E 1F      LD      E,$1F           
6777: 55         LD      D,L             
6778: 56         LD      D,(HL)          
6779: 55         LD      D,L             
677A: 56         LD      D,(HL)          
677B: 04         INC     B               
677C: 05         DEC     B               
677D: 64         LD      H,H             
677E: 65         LD      H,L             
677F: 06 07      LD      B,$07           
6781: 55         LD      D,L             
6782: 56         LD      D,(HL)          
6783: 55         LD      D,L             
6784: 56         LD      D,(HL)          
6785: 14         INC     D               
6786: 15         DEC     D               
6787: 66         LD      H,(HL)          
6788: 67         LD      H,A             
6789: 16 17      LD      D,$17           
678B: 55         LD      D,L             
678C: 56         LD      D,(HL)          
678D: 76         HALT                    
678E: 76         HALT                    
678F: 72         LD      (HL),D          
6790: 73         LD      (HL),E          
6791: 76         HALT                    
6792: 76         HALT                    
6793: 72         LD      (HL),D          
6794: 73         LD      (HL),E          
6795: 68         LD      L,B             
6796: 69         LD      L,C             
6797: 76         HALT                    
6798: 76         HALT                    
6799: 73         LD      (HL),E          
679A: 72         LD      (HL),D          
679B: 76         HALT                    
679C: 76         HALT                    
679D: 73         LD      (HL),E          
679E: 72         LD      (HL),D          
679F: 77         LD      (HL),A          
67A0: 4B         LD      C,E             
67A1: 6C         LD      L,H             
67A2: 6C         LD      L,H             
67A3: 6C         LD      L,H             
67A4: 6C         LD      L,H             
67A5: 76         HALT                    
67A6: 76         HALT                    
67A7: 76         HALT                    
67A8: 76         HALT                    
67A9: 72         LD      (HL),D          
67AA: 73         LD      (HL),E          
67AB: 6C         LD      L,H             
67AC: 6C         LD      L,H             
67AD: 6C         LD      L,H             
67AE: 6C         LD      L,H             
67AF: 76         HALT                    
67B0: 76         HALT                    
67B1: 76         HALT                    
67B2: 76         HALT                    
67B3: 73         LD      (HL),E          
67B4: 72         LD      (HL),D          
67B5: 6D         LD      L,L             
67B6: 6D         LD      L,L             
67B7: 6C         LD      L,H             
67B8: 6C         LD      L,H             
67B9: 6C         LD      L,H             
67BA: 6C         LD      L,H             
67BB: 6C         LD      L,H             
67BC: 6C         LD      L,H             
67BD: 6C         LD      L,H             
67BE: 6C         LD      L,H             
67BF: 6D         LD      L,L             
67C0: 6D         LD      L,L             
67C1: 6C         LD      L,H             
67C2: 6C         LD      L,H             
67C3: 6C         LD      L,H             
67C4: 6C         LD      L,H             
67C5: 6C         LD      L,H             
67C6: 6C         LD      L,H             
67C7: 6C         LD      L,H             
67C8: 6C         LD      L,H             
67C9: 55         LD      D,L             
67CA: 56         LD      D,(HL)          
67CB: 6E         LD      L,(HL)          
67CC: 6E         LD      L,(HL)          
67CD: 6E         LD      L,(HL)          
67CE: 6E         LD      L,(HL)          
67CF: 6E         LD      L,(HL)          
67D0: 6E         LD      L,(HL)          
67D1: 55         LD      D,L             
67D2: 56         LD      D,(HL)          
67D3: 55         LD      D,L             
67D4: 56         LD      D,(HL)          
67D5: 6E         LD      L,(HL)          
67D6: 6E         LD      L,(HL)          
67D7: 6E         LD      L,(HL)          
67D8: 6E         LD      L,(HL)          
67D9: 6E         LD      L,(HL)          
67DA: 6E         LD      L,(HL)          
67DB: 55         LD      D,L             
67DC: 56         LD      D,(HL)          
67DD: 55         LD      D,L             
67DE: 56         LD      D,(HL)          
67DF: 6E         LD      L,(HL)          
67E0: 6E         LD      L,(HL)          
67E1: 6E         LD      L,(HL)          
67E2: 6E         LD      L,(HL)          
67E3: 6E         LD      L,(HL)          
67E4: 6E         LD      L,(HL)          
67E5: 55         LD      D,L             
67E6: 56         LD      D,(HL)          
67E7: 55         LD      D,L             
67E8: 56         LD      D,(HL)          
67E9: 6E         LD      L,(HL)          
67EA: 6E         LD      L,(HL)          
67EB: 6E         LD      L,(HL)          
67EC: 6E         LD      L,(HL)          
67ED: 6E         LD      L,(HL)          
67EE: 6E         LD      L,(HL)          
67EF: 55         LD      D,L             
67F0: 56         LD      D,(HL)          
67F1: 6D         LD      L,L             
67F2: 6D         LD      L,L             
67F3: 6D         LD      L,L             
67F4: 6D         LD      L,L             
67F5: 6D         LD      L,L             
67F6: 6D         LD      L,L             
67F7: 6D         LD      L,L             
67F8: 6D         LD      L,L             
67F9: 6D         LD      L,L             
67FA: 6D         LD      L,L             
67FB: 6D         LD      L,L             
67FC: 6D         LD      L,L             
67FD: 6D         LD      L,L             
67FE: 6D         LD      L,L             
67FF: 6D         LD      L,L             
6800: 6D         LD      L,L             
6801: 6D         LD      L,L             
6802: 6D         LD      L,L             
6803: 6D         LD      L,L             
6804: 6D         LD      L,L             
6805: 6D         LD      L,L             
6806: 6D         LD      L,L             
6807: 6D         LD      L,L             
6808: 6D         LD      L,L             
6809: 6D         LD      L,L             
680A: 6D         LD      L,L             
680B: 6D         LD      L,L             
680C: 6D         LD      L,L             
680D: 6D         LD      L,L             
680E: 6D         LD      L,L             
680F: 6D         LD      L,L             
6810: 6D         LD      L,L             
6811: 6D         LD      L,L             
6812: 6D         LD      L,L             
6813: 6D         LD      L,L             
6814: 6D         LD      L,L             
6815: 6D         LD      L,L             
6816: 6D         LD      L,L             
6817: 6D         LD      L,L             
6818: 6D         LD      L,L             
6819: 6D         LD      L,L             
681A: 6D         LD      L,L             
681B: 6D         LD      L,L             
681C: 6D         LD      L,L             
681D: 6D         LD      L,L             
681E: 6D         LD      L,L             
681F: 6D         LD      L,L             
6820: 6D         LD      L,L             
6821: 6D         LD      L,L             
6822: 6D         LD      L,L             
6823: 6D         LD      L,L             
6824: 6D         LD      L,L             
6825: 6D         LD      L,L             
6826: 6D         LD      L,L             
6827: 6D         LD      L,L             
6828: 6D         LD      L,L             
6829: 6D         LD      L,L             
682A: 6D         LD      L,L             
682B: 6D         LD      L,L             
682C: 6D         LD      L,L             
682D: 3A         LD      A,(HLD)         
682E: D5         PUSH    DE              
682F: D6 D7      SUB     $D7             
6831: 3A         LD      A,(HLD)         
6832: 3A         LD      A,(HLD)         
6833: CD E1 CE   CALL    $CEE1           
6836: 3A         LD      A,(HLD)         
6837: 03         INC     BC              
6838: 09         ADD     HL,BC           
6839: 03         INC     BC              
683A: 09         ADD     HL,BC           
683B: C6 1B      ADD     $1B             
683D: 1B         DEC     DE              
683E: 03         INC     BC              
683F: 03         INC     BC              
6840: 09         ADD     HL,BC           
6841: 0E 1B      LD      C,$1B           
6843: 1B         DEC     DE              
6844: 1B         DEC     DE              
6845: 1B         DEC     DE              
6846: 02         LD      (BC),A          
6847: 12         LD      (DE),A          
6848: 22         LD      (HLI),A         
6849: 32         LD      (HLD),A         
684A: 42         LD      B,D             
684B: 00         NOP                     
684C: 08 10 18   LD      ($1810),SP      
684F: 20 28      JR      NZ,$6879        
6851: 30 38      JR      NC,$688B        
6853: 40         LD      B,B             
6854: 48         LD      C,B             
6855: CD 76 7C   CALL    $7C76           
6858: 3E 02      LD      A,$02           
685A: E0 A1      LDFF00  ($A1),A         
685C: EA 67 C1   LD      ($C167),A       
685F: F0 F0      LD      A,($F0)         
6861: C7         RST     0X00            
6862: 6A         LD      L,D             
6863: 68         LD      L,B             
6864: 75         LD      (HL),L          
6865: 68         LD      L,B             
6866: 81         ADD     A,C             
6867: 68         LD      L,B             
6868: 8D         ADC     A,L             
6869: 68         LD      L,B             
686A: CD 00 40   CALL    $4000           
686D: CD 91 08   CALL    $0891           
6870: 36 28      LD      (HL),$28        
6872: C3 8D 3B   JP      $3B8D           
6875: CD 91 08   CALL    $0891           
6878: C0         RET     NZ              
6879: 3E 4C      LD      A,$4C           
687B: EA 68 D3   LD      ($D368),A       
687E: C3 8D 3B   JP      $3B8D           
6881: 3E 1D      LD      A,$1D           
6883: E0 F4      LDFF00  ($F4),A         
6885: CD 91 08   CALL    $0891           
6888: 36 80      LD      (HL),$80        
688A: C3 8D 3B   JP      $3B8D           
688D: F0 E7      LD      A,($E7)         
688F: 1E 00      LD      E,$00           
6891: E6 08      AND     $08             
6893: 28 02      JR      Z,$6897         
6895: 1E 02      LD      E,$02           
6897: 7B         LD      A,E             
6898: EA 55 C1   LD      ($C155),A       
689B: CD 91 08   CALL    $0891           
689E: C0         RET     NZ              
689F: 21 B0 C2   LD      HL,$C2B0        
68A2: 09         ADD     HL,BC           
68A3: 7E         LD      A,(HL)          
68A4: 5F         LD      E,A             
68A5: 3C         INC     A               
68A6: 77         LD      (HL),A          
68A7: E0 E8      LDFF00  ($E8),A         
68A9: 7B         LD      A,E             
68AA: E6 1F      AND     $1F             
68AC: C2 BB 68   JP      NZ,$68BB        
68AF: 21 D0 C3   LD      HL,$C3D0        
68B2: 09         ADD     HL,BC           
68B3: 7E         LD      A,(HL)          
68B4: FE 0A      CP      $0A             
68B6: CA 40 69   JP      Z,$6940         
68B9: 3C         INC     A               
68BA: 77         LD      (HL),A          
68BB: 21 D0 C3   LD      HL,$C3D0        
68BE: 09         ADD     HL,BC           
68BF: E5         PUSH    HL              
68C0: 7E         LD      A,(HL)          
68C1: 5F         LD      E,A             
68C2: 50         LD      D,B             
68C3: 21 4A 68   LD      HL,$684A        
68C6: 19         ADD     HL,DE           
68C7: 7E         LD      A,(HL)          
68C8: E0 CD      LDFF00  ($CD),A         
68CA: 3E 20      LD      A,$20           
68CC: E0 CE      LDFF00  ($CE),A         
68CE: CD 39 28   CALL    $2839           
68D1: E1         POP     HL              
68D2: 7E         LD      A,(HL)          
68D3: 3D         DEC     A               
68D4: 5F         LD      E,A             
68D5: CB 27      SET     1,E             
68D7: CB 27      SET     1,E             
68D9: CB 27      SET     1,E             
68DB: 83         ADD     A,E             
68DC: 83         ADD     A,E             
68DD: 5F         LD      E,A             
68DE: 50         LD      D,B             
68DF: 21 65 67   LD      HL,$6765        
68E2: F0 E8      LD      A,($E8)         
68E4: E6 01      AND     $01             
68E6: 28 03      JR      Z,$68EB         
68E8: 21 C9 67   LD      HL,$67C9        
68EB: 19         ADD     HL,DE           
68EC: E5         PUSH    HL              
68ED: FA 00 D6   LD      A,($D600)       
68F0: 5F         LD      E,A             
68F1: 50         LD      D,B             
68F2: C6 0D      ADD     $0D             
68F4: EA 00 D6   LD      ($D600),A       
68F7: 21 01 D6   LD      HL,$D601        
68FA: 19         ADD     HL,DE           
68FB: F0 CF      LD      A,($CF)         
68FD: 22         LD      (HLI),A         
68FE: F0 D0      LD      A,($D0)         
6900: 22         LD      (HLI),A         
6901: 3E 09      LD      A,$09           
6903: 22         LD      (HLI),A         
6904: D1         POP     DE              
6905: C5         PUSH    BC              
6906: 0E 0A      LD      C,$0A           
6908: 1A         LD      A,(DE)          
6909: 13         INC     DE              
690A: 22         LD      (HLI),A         
690B: 0D         DEC     C               
690C: 20 FA      JR      NZ,$6908        
690E: 70         LD      (HL),B          
690F: C1         POP     BC              
6910: C5         PUSH    BC              
6911: 21 D0 C3   LD      HL,$C3D0        
6914: 09         ADD     HL,BC           
6915: 7E         LD      A,(HL)          
6916: 3D         DEC     A               
6917: 1F         RRA                     
6918: E6 07      AND     $07             
691A: F5         PUSH    AF              
691B: 5F         LD      E,A             
691C: 50         LD      D,B             
691D: 21 46 68   LD      HL,$6846        
6920: 19         ADD     HL,DE           
6921: 5E         LD      E,(HL)          
6922: 21 11 D7   LD      HL,$D711        
6925: 19         ADD     HL,DE           
6926: E5         PUSH    HL              
6927: C1         POP     BC              
6928: F1         POP     AF              
6929: 5F         LD      E,A             
692A: CB 27      SET     1,E             
692C: CB 27      SET     1,E             
692E: 83         ADD     A,E             
692F: 5F         LD      E,A             
6930: 16 00      LD      D,$00           
6932: 21 2D 68   LD      HL,$682D        
6935: 19         ADD     HL,DE           
6936: 1E 05      LD      E,$05           
6938: 2A         LD      A,(HLI)         
6939: 02         LD      (BC),A          
693A: 03         INC     BC              
693B: 1D         DEC     E               
693C: 20 FA      JR      NZ,$6938        
693E: C1         POP     BC              
693F: C9         RET                     
6940: AF         XOR     A               
6941: EA 55 C1   LD      ($C155),A       
6944: EA 67 C1   LD      ($C167),A       
6947: CD BD 27   CALL    $27BD           
694A: C3 7C 7D   JP      $7D7C           
694D: 21 40 C4   LD      HL,$C440        
6950: 09         ADD     HL,BC           
6951: 7E         LD      A,(HL)          
6952: FE FF      CP      $FF             
6954: CA 55 68   JP      Z,$6855         
6957: A7         AND     A               
6958: 20 04      JR      NZ,$695E        
695A: 34         INC     (HL)            
695B: CD E1 6D   CALL    $6DE1           
695E: CD C2 6E   CALL    $6EC2           
6961: F0 EA      LD      A,($EA)         
6963: FE 05      CP      $05             
6965: C2 82 7D   JP      NZ,$7D82        
6968: CD 76 7C   CALL    $7C76           
696B: CD 0E 38   CALL    $380E           
696E: CD 12 3F   CALL    $3F12           
6971: 21 20 C4   LD      HL,$C420        
6974: 09         ADD     HL,BC           
6975: 7E         LD      A,(HL)          
6976: FE 16      CP      $16             
6978: 20 1B      JR      NZ,$6995        
697A: F0 F0      LD      A,($F0)         
697C: FE 09      CP      $09             
697E: 30 10      JR      NC,$6990        
6980: 70         LD      (HL),B          
6981: 21 20 C3   LD      HL,$C320        
6984: 09         ADD     HL,BC           
6985: 70         LD      (HL),B          
6986: CD 8D 3B   CALL    $3B8D           
6989: 3E 09      LD      A,$09           
698B: 77         LD      (HL),A          
698C: E0 F0      LDFF00  ($F0),A         
698E: 18 05      JR      $6995           
6990: 21 D0 C3   LD      HL,$C3D0        
6993: 09         ADD     HL,BC           
6994: 34         INC     (HL)            
6995: CD 98 7C   CALL    $7C98           
6998: CD 1B 7D   CALL    $7D1B           
699B: 21 20 C3   LD      HL,$C320        
699E: 09         ADD     HL,BC           
699F: 35         DEC     (HL)            
69A0: 35         DEC     (HL)            
69A1: 21 10 C3   LD      HL,$C310        
69A4: 09         ADD     HL,BC           
69A5: 7E         LD      A,(HL)          
69A6: E6 80      AND     $80             
69A8: E0 E8      LDFF00  ($E8),A         
69AA: 28 06      JR      Z,$69B2         
69AC: 70         LD      (HL),B          
69AD: 21 20 C3   LD      HL,$C320        
69B0: 09         ADD     HL,BC           
69B1: 70         LD      (HL),B          
69B2: F0 F0      LD      A,($F0)         
69B4: FE 09      CP      $09             
69B6: 30 14      JR      NC,$69CC        
69B8: CD E0 3B   CALL    $3BE0           
69BB: 21 10 C4   LD      HL,$C410        
69BE: 09         ADD     HL,BC           
69BF: FA 3E C1   LD      A,($C13E)       
69C2: B6         OR      (HL)            
69C3: A7         AND     A               
69C4: 20 06      JR      NZ,$69CC        
69C6: CD D5 3B   CALL    $3BD5           
69C9: CD EB 3B   CALL    $3BEB           
69CC: F0 F0      LD      A,($F0)         
69CE: C7         RST     0X00            
69CF: EB         ???                     
69D0: 69         LD      L,C             
69D1: 01 6A 22   LD      BC,$226A        
69D4: 6A         LD      L,D             
69D5: 74         LD      (HL),H          
69D6: 6A         LD      L,D             
69D7: D4 6A 03   CALL    NC,$036A        
69DA: 6B         LD      L,E             
69DB: 49         LD      C,C             
69DC: 6B         LD      L,E             
69DD: 28 6C      JR      Z,$6A4B         
69DF: 70         LD      (HL),B          
69E0: 6C         LD      L,H             
69E1: 93         SUB     E               
69E2: 6C         LD      L,H             
69E3: B4         OR      H               
69E4: 6C         LD      L,H             
69E5: EF         RST     0X28            
69E6: 6C         LD      L,H             
69E7: 0D         DEC     C               
69E8: 6D         LD      L,L             
69E9: 6F         LD      L,A             
69EA: 6D         LD      L,L             
69EB: 21 20 C3   LD      HL,$C320        
69EE: 09         ADD     HL,BC           
69EF: 70         LD      (HL),B          
69F0: CD 91 08   CALL    $0891           
69F3: 20 0B      JR      NZ,$6A00        
69F5: 36 30      LD      (HL),$30        
69F7: CD 8D 3B   CALL    $3B8D           
69FA: 21 10 C3   LD      HL,$C310        
69FD: 09         ADD     HL,BC           
69FE: 36 6F      LD      (HL),$6F        
6A00: C9         RET                     
6A01: CD 91 08   CALL    $0891           
6A04: 28 0E      JR      Z,$6A14         
6A06: FE 01      CP      $01             
6A08: 20 04      JR      NZ,$6A0E        
6A0A: 3E 08      LD      A,$08           
6A0C: E0 F2      LDFF00  ($F2),A         
6A0E: 21 20 C3   LD      HL,$C320        
6A11: 09         ADD     HL,BC           
6A12: 70         LD      (HL),B          
6A13: C9         RET                     
6A14: F0 E8      LD      A,($E8)         
6A16: A7         AND     A               
6A17: 28 08      JR      Z,$6A21         
6A19: CD 91 08   CALL    $0891           
6A1C: 36 40      LD      (HL),$40        
6A1E: CD 8D 3B   CALL    $3B8D           
6A21: C9         RET                     
6A22: CD 91 08   CALL    $0891           
6A25: FE 01      CP      $01             
6A27: 20 16      JR      NZ,$6A3F        
6A29: 1E 12      LD      E,$12           
6A2B: F0 F6      LD      A,($F6)         
6A2D: FE 92      CP      $92             
6A2F: 28 0A      JR      Z,$6A3B         
6A31: FE 84      CP      $84             
6A33: 28 06      JR      Z,$6A3B         
6A35: FE 80      CP      $80             
6A37: 20 06      JR      NZ,$6A3F        
6A39: 1E 14      LD      E,$14           
6A3B: 7B         LD      A,E             
6A3C: CD 85 21   CALL    $2185           
6A3F: CD 91 08   CALL    $0891           
6A42: 20 0D      JR      NZ,$6A51        
6A44: 36 A0      LD      (HL),$A0        
6A46: F0 F6      LD      A,($F6)         
6A48: FE 95      CP      $95             
6A4A: 28 02      JR      Z,$6A4E         
6A4C: 36 20      LD      (HL),$20        
6A4E: C3 8D 3B   JP      $3B8D           
6A51: 21 0E D2   LD      HL,$D20E        
6A54: 36 F0      LD      (HL),$F0        
6A56: 21 0B D2   LD      HL,$D20B        
6A59: 36 F8      LD      (HL),$F8        
6A5B: 21 0D D2   LD      HL,$D20D        
6A5E: 36 F0      LD      (HL),$F0        
6A60: FE 20      CP      $20             
6A62: 38 0F      JR      C,$6A73         
6A64: 21 0E D2   LD      HL,$D20E        
6A67: 36 F2      LD      (HL),$F2        
6A69: 21 0B D2   LD      HL,$D20B        
6A6C: 36 FA      LD      (HL),$FA        
6A6E: 21 0D D2   LD      HL,$D20D        
6A71: 36 F2      LD      (HL),$F2        
6A73: C9         RET                     
6A74: CD 91 08   CALL    $0891           
6A77: 20 05      JR      NZ,$6A7E        
6A79: 36 20      LD      (HL),$20        
6A7B: C3 8D 3B   JP      $3B8D           
6A7E: E6 3F      AND     $3F             
6A80: 20 00      JR      NZ,$6A82        
6A82: CD 91 08   CALL    $0891           
6A85: E6 40      AND     $40             
6A87: 28 26      JR      Z,$6AAF         
6A89: CD 01 6E   CALL    $6E01           
6A8C: 21 08 D2   LD      HL,$D208        
6A8F: 36 01      LD      (HL),$01        
6A91: 21 09 D2   LD      HL,$D209        
6A94: 70         LD      (HL),B          
6A95: 21 0A D2   LD      HL,$D20A        
6A98: 36 F0      LD      (HL),$F0        
6A9A: 21 0B D2   LD      HL,$D20B        
6A9D: 36 F8      LD      (HL),$F8        
6A9F: 21 0D D2   LD      HL,$D20D        
6AA2: 36 F3      LD      (HL),$F3        
6AA4: 21 0C D2   LD      HL,$D20C        
6AA7: 36 10      LD      (HL),$10        
6AA9: 21 07 D2   LD      HL,$D207        
6AAC: 36 00      LD      (HL),$00        
6AAE: C9         RET                     
6AAF: CD 01 6E   CALL    $6E01           
6AB2: 21 08 D2   LD      HL,$D208        
6AB5: 70         LD      (HL),B          
6AB6: 21 09 D2   LD      HL,$D209        
6AB9: 70         LD      (HL),B          
6ABA: 21 0A D2   LD      HL,$D20A        
6ABD: 36 F8      LD      (HL),$F8        
6ABF: 21 0B D2   LD      HL,$D20B        
6AC2: 36 F8      LD      (HL),$F8        
6AC4: 21 0D D2   LD      HL,$D20D        
6AC7: 36 F0      LD      (HL),$F0        
6AC9: 21 0C D2   LD      HL,$D20C        
6ACC: 36 10      LD      (HL),$10        
6ACE: 21 07 D2   LD      HL,$D207        
6AD1: 36 00      LD      (HL),$00        
6AD3: C9         RET                     
6AD4: CD B1 6D   CALL    $6DB1           
6AD7: CD 91 08   CALL    $0891           
6ADA: 20 26      JR      NZ,$6B02        
6ADC: CD ED 27   CALL    $27ED           
6ADF: E6 1F      AND     $1F             
6AE1: C6 30      ADD     $30             
6AE3: 77         LD      (HL),A          
6AE4: 3E 08      LD      A,$08           
6AE6: CD 25 3C   CALL    $3C25           
6AE9: CD 8D 3B   CALL    $3B8D           
6AEC: CD 35 7D   CALL    $7D35           
6AEF: 21 80 C3   LD      HL,$C380        
6AF2: 09         ADD     HL,BC           
6AF3: 73         LD      (HL),E          
6AF4: CD 89 6A   CALL    $6A89           
6AF7: 21 80 C3   LD      HL,$C380        
6AFA: 09         ADD     HL,BC           
6AFB: 7E         LD      A,(HL)          
6AFC: A7         AND     A               
6AFD: 20 03      JR      NZ,$6B02        
6AFF: CD AF 6A   CALL    $6AAF           
6B02: C9         RET                     
6B03: CD B1 6D   CALL    $6DB1           
6B06: CD 35 7D   CALL    $7D35           
6B09: C6 20      ADD     $20             
6B0B: FE 40      CP      $40             
6B0D: 30 14      JR      NC,$6B23        
6B0F: CD 45 7D   CALL    $7D45           
6B12: C6 1C      ADD     $1C             
6B14: FE 38      CP      $38             
6B16: 30 0B      JR      NC,$6B23        
6B18: CD 8D 3B   CALL    $3B8D           
6B1B: 36 06      LD      (HL),$06        
6B1D: CD 91 08   CALL    $0891           
6B20: 36 30      LD      (HL),$30        
6B22: C9         RET                     
6B23: CD 91 08   CALL    $0891           
6B26: 20 0E      JR      NZ,$6B36        
6B28: CD ED 27   CALL    $27ED           
6B2B: E6 0F      AND     $0F             
6B2D: C6 10      ADD     $10             
6B2F: 77         LD      (HL),A          
6B30: CD 8D 3B   CALL    $3B8D           
6B33: 36 04      LD      (HL),$04        
6B35: C9         RET                     
6B36: E6 0F      AND     $0F             
6B38: 20 08      JR      NZ,$6B42        
6B3A: FA 09 D2   LD      A,($D209)       
6B3D: EE 01      XOR     $01             
6B3F: EA 09 D2   LD      ($D209),A       
6B42: CD E2 7C   CALL    $7CE2           
6B45: CD 9E 3B   CALL    $3B9E           
6B48: C9         RET                     
6B49: CD 91 08   CALL    $0891           
6B4C: 20 17      JR      NZ,$6B65        
6B4E: CD 91 08   CALL    $0891           
6B51: 36 20      LD      (HL),$20        
6B53: CD 8D 3B   CALL    $3B8D           
6B56: 36 04      LD      (HL),$04        
6B58: 21 50 C3   LD      HL,$C350        
6B5B: 09         ADD     HL,BC           
6B5C: CB FE      SET     1,E             
6B5E: 21 30 C4   LD      HL,$C430        
6B61: 09         ADD     HL,BC           
6B62: CB B6      SET     1,E             
6B64: C9         RET                     
6B65: 21 80 C3   LD      HL,$C380        
6B68: 09         ADD     HL,BC           
6B69: 7E         LD      A,(HL)          
6B6A: A7         AND     A               
6B6B: 20 5B      JR      NZ,$6BC8        
6B6D: CD 91 08   CALL    $0891           
6B70: FE 18      CP      $18             
6B72: 38 13      JR      C,$6B87         
6B74: CD AF 6A   CALL    $6AAF           
6B77: 3E 08      LD      A,$08           
6B79: EA 0C D2   LD      ($D20C),A       
6B7C: 3E E0      LD      A,$E0           
6B7E: EA 0D D2   LD      ($D20D),A       
6B81: 3E 01      LD      A,$01           
6B83: EA 07 D2   LD      ($D207),A       
6B86: C9         RET                     
6B87: FE 10      CP      $10             
6B89: 38 23      JR      C,$6BAE         
6B8B: FE 17      CP      $17             
6B8D: 20 0A      JR      NZ,$6B99        
6B8F: 3E 27      LD      A,$27           
6B91: E0 F4      LDFF00  ($F4),A         
6B93: 21 00 C3   LD      HL,$C300        
6B96: 09         ADD     HL,BC           
6B97: 36 10      LD      (HL),$10        
6B99: 3E FF      LD      A,$FF           
6B9B: EA 07 D2   LD      ($D207),A       
6B9E: 3E F0      LD      A,$F0           
6BA0: EA 0A D2   LD      ($D20A),A       
6BA3: 3E F4      LD      A,$F4           
6BA5: EA 0B D2   LD      ($D20B),A       
6BA8: 3E 01      LD      A,$01           
6BAA: EA 08 D2   LD      ($D208),A       
6BAD: C9         RET                     
6BAE: 3E 03      LD      A,$03           
6BB0: EA 07 D2   LD      ($D207),A       
6BB3: 3E F8      LD      A,$F8           
6BB5: EA 0C D2   LD      ($D20C),A       
6BB8: 3E 08      LD      A,$08           
6BBA: EA 0D D2   LD      ($D20D),A       
6BBD: 3E F0      LD      A,$F0           
6BBF: EA 0A D2   LD      ($D20A),A       
6BC2: 3E F0      LD      A,$F0           
6BC4: EA 0B D2   LD      ($D20B),A       
6BC7: C9         RET                     
6BC8: CD 91 08   CALL    $0891           
6BCB: FE 18      CP      $18             
6BCD: 38 18      JR      C,$6BE7         
6BCF: CD 89 6A   CALL    $6A89           
6BD2: 3E 01      LD      A,$01           
6BD4: EA 09 D2   LD      ($D209),A       
6BD7: 3E F8      LD      A,$F8           
6BD9: EA 0C D2   LD      ($D20C),A       
6BDC: 3E E8      LD      A,$E8           
6BDE: EA 0D D2   LD      ($D20D),A       
6BE1: 3E 00      LD      A,$00           
6BE3: EA 07 D2   LD      ($D207),A       
6BE6: C9         RET                     
6BE7: FE 10      CP      $10             
6BE9: 38 23      JR      C,$6C0E         
6BEB: FE 17      CP      $17             
6BED: 20 0A      JR      NZ,$6BF9        
6BEF: 3E 27      LD      A,$27           
6BF1: E0 F4      LDFF00  ($F4),A         
6BF3: 21 00 C3   LD      HL,$C300        
6BF6: 09         ADD     HL,BC           
6BF7: 36 10      LD      (HL),$10        
6BF9: 3E FF      LD      A,$FF           
6BFB: EA 07 D2   LD      ($D207),A       
6BFE: 3E F0      LD      A,$F0           
6C00: EA 0A D2   LD      ($D20A),A       
6C03: 3E F0      LD      A,$F0           
6C05: EA 0B D2   LD      ($D20B),A       
6C08: 3E 00      LD      A,$00           
6C0A: EA 08 D2   LD      ($D208),A       
6C0D: C9         RET                     
6C0E: 3E 02      LD      A,$02           
6C10: EA 07 D2   LD      ($D207),A       
6C13: 3E 10      LD      A,$10           
6C15: EA 0C D2   LD      ($D20C),A       
6C18: 3E 08      LD      A,$08           
6C1A: EA 0D D2   LD      ($D20D),A       
6C1D: 3E F0      LD      A,$F0           
6C1F: EA 0A D2   LD      ($D20A),A       
6C22: 3E EC      LD      A,$EC           
6C24: EA 0B D2   LD      ($D20B),A       
6C27: C9         RET                     
6C28: CD F4 6A   CALL    $6AF4           
6C2B: CD 91 08   CALL    $0891           
6C2E: 20 27      JR      NZ,$6C57        
6C30: CD 8D 3B   CALL    $3B8D           
6C33: CD 44 72   CALL    $7244           
6C36: 21 B0 C2   LD      HL,$C2B0        
6C39: 09         ADD     HL,BC           
6C3A: 7E         LD      A,(HL)          
6C3B: 21 20 C3   LD      HL,$C320        
6C3E: 09         ADD     HL,BC           
6C3F: 36 30      LD      (HL),$30        
6C41: A7         AND     A               
6C42: 20 07      JR      NZ,$6C4B        
6C44: 36 28      LD      (HL),$28        
6C46: 3E 18      LD      A,$18           
6C48: C3 25 3C   JP      $3C25           
6C4B: 3E 08      LD      A,$08           
6C4D: CD 25 3C   CALL    $3C25           
6C50: 21 50 C2   LD      HL,$C250        
6C53: 09         ADD     HL,BC           
6C54: 36 F0      LD      (HL),$F0        
6C56: C9         RET                     
6C57: FA 0E D2   LD      A,($D20E)       
6C5A: C6 02      ADD     $02             
6C5C: EA 0E D2   LD      ($D20E),A       
6C5F: FA 0B D2   LD      A,($D20B)       
6C62: C6 02      ADD     $02             
6C64: EA 0B D2   LD      ($D20B),A       
6C67: FA 0D D2   LD      A,($D20D)       
6C6A: C6 02      ADD     $02             
6C6C: EA 0D D2   LD      ($D20D),A       
6C6F: C9         RET                     
6C70: CD 91 08   CALL    $0891           
6C73: 28 0D      JR      Z,$6C82         
6C75: 3D         DEC     A               
6C76: 20 03      JR      NZ,$6C7B        
6C78: CD 4E 6B   CALL    $6B4E           
6C7B: CD F4 6A   CALL    $6AF4           
6C7E: CD 57 6C   CALL    $6C57           
6C81: C9         RET                     
6C82: CD 42 6B   CALL    $6B42           
6C85: F0 E8      LD      A,($E8)         
6C87: A7         AND     A               
6C88: 28 08      JR      Z,$6C92         
6C8A: CD 91 08   CALL    $0891           
6C8D: 36 10      LD      (HL),$10        
6C8F: CD 21 6A   CALL    $6A21           
6C92: C9         RET                     
6C93: F0 E8      LD      A,($E8)         
6C95: A7         AND     A               
6C96: 28 18      JR      Z,$6CB0         
6C98: CD 8D 3B   CALL    $3B8D           
6C9B: CD 91 08   CALL    $0891           
6C9E: 36 20      LD      (HL),$20        
6CA0: 21 50 C3   LD      HL,$C350        
6CA3: 09         ADD     HL,BC           
6CA4: CB BE      SET     1,E             
6CA6: 21 30 C4   LD      HL,$C430        
6CA9: 09         ADD     HL,BC           
6CAA: CB F6      SET     1,E             
6CAC: 3E 28      LD      A,$28           
6CAE: E0 F2      LDFF00  ($F2),A         
6CB0: CD 42 6B   CALL    $6B42           
6CB3: C9         RET                     
6CB4: CD 91 08   CALL    $0891           
6CB7: 20 06      JR      NZ,$6CBF        
6CB9: 36 C0      LD      (HL),$C0        
6CBB: CD 8D 3B   CALL    $3B8D           
6CBE: C9         RET                     
6CBF: 21 0B D2   LD      HL,$D20B        
6CC2: 7E         LD      A,(HL)          
6CC3: D6 03      SUB     $03             
6CC5: 28 07      JR      Z,$6CCE         
6CC7: CB 7F      SET     1,E             
6CC9: 28 02      JR      Z,$6CCD         
6CCB: 34         INC     (HL)            
6CCC: 34         INC     (HL)            
6CCD: 35         DEC     (HL)            
6CCE: 21 0D D2   LD      HL,$D20D        
6CD1: 7E         LD      A,(HL)          
6CD2: D6 03      SUB     $03             
6CD4: 28 07      JR      Z,$6CDD         
6CD6: CB 7F      SET     1,E             
6CD8: 28 02      JR      Z,$6CDC         
6CDA: 34         INC     (HL)            
6CDB: 34         INC     (HL)            
6CDC: 35         DEC     (HL)            
6CDD: CD 91 08   CALL    $0891           
6CE0: FE 14      CP      $14             
6CE2: 30 0A      JR      NC,$6CEE        
6CE4: FA 0E D2   LD      A,($D20E)       
6CE7: A7         AND     A               
6CE8: 28 04      JR      Z,$6CEE         
6CEA: 3C         INC     A               
6CEB: EA 0E D2   LD      ($D20E),A       
6CEE: C9         RET                     
6CEF: CD 91 08   CALL    $0891           
6CF2: 20 06      JR      NZ,$6CFA        
6CF4: 36 30      LD      (HL),$30        
6CF6: CD 8D 3B   CALL    $3B8D           
6CF9: C9         RET                     
6CFA: FE 30      CP      $30             
6CFC: 30 0E      JR      NC,$6D0C        
6CFE: E6 03      AND     $03             
6D00: 20 0A      JR      NZ,$6D0C        
6D02: FA 0E D2   LD      A,($D20E)       
6D05: C6 02      ADD     $02             
6D07: 2F         CPL                     
6D08: 3C         INC     A               
6D09: EA 0E D2   LD      ($D20E),A       
6D0C: C9         RET                     
6D0D: FA 0E D2   LD      A,($D20E)       
6D10: FE F0      CP      $F0             
6D12: 28 04      JR      Z,$6D18         
6D14: 3D         DEC     A               
6D15: EA 0E D2   LD      ($D20E),A       
6D18: CD 91 08   CALL    $0891           
6D1B: 20 2F      JR      NZ,$6D4C        
6D1D: 1E FF      LD      E,$FF           
6D1F: F0 F6      LD      A,($F6)         
6D21: FE 80      CP      $80             
6D23: 28 08      JR      Z,$6D2D         
6D25: 1E 03      LD      E,$03           
6D27: FE 95      CP      $95             
6D29: 28 02      JR      Z,$6D2D         
6D2B: 1E 02      LD      E,$02           
6D2D: 21 D0 C3   LD      HL,$C3D0        
6D30: 09         ADD     HL,BC           
6D31: 7E         LD      A,(HL)          
6D32: BB         CP      E               
6D33: 38 14      JR      C,$6D49         
6D35: 21 50 C3   LD      HL,$C350        
6D38: 09         ADD     HL,BC           
6D39: CB FE      SET     1,E             
6D3B: CD 8D 3B   CALL    $3B8D           
6D3E: 3E 13      LD      A,$13           
6D40: CD 85 21   CALL    $2185           
6D43: CD 91 08   CALL    $0891           
6D46: 36 04      LD      (HL),$04        
6D48: C9         RET                     
6D49: C3 4E 6B   JP      $6B4E           
6D4C: FE 24      CP      $24             
6D4E: 30 1E      JR      NC,$6D6E        
6D50: 21 0B D2   LD      HL,$D20B        
6D53: 7E         LD      A,(HL)          
6D54: D6 F8      SUB     $F8             
6D56: 28 07      JR      Z,$6D5F         
6D58: CB 7F      SET     1,E             
6D5A: 28 02      JR      Z,$6D5E         
6D5C: 34         INC     (HL)            
6D5D: 34         INC     (HL)            
6D5E: 35         DEC     (HL)            
6D5F: 21 0D D2   LD      HL,$D20D        
6D62: 7E         LD      A,(HL)          
6D63: D6 F0      SUB     $F0             
6D65: 28 07      JR      Z,$6D6E         
6D67: CB 7F      SET     1,E             
6D69: 28 02      JR      Z,$6D6D         
6D6B: 34         INC     (HL)            
6D6C: 34         INC     (HL)            
6D6D: 35         DEC     (HL)            
6D6E: C9         RET                     
6D6F: CD F4 6A   CALL    $6AF4           
6D72: CD 91 08   CALL    $0891           
6D75: 28 0B      JR      Z,$6D82         
6D77: 3D         DEC     A               
6D78: 20 04      JR      NZ,$6D7E        
6D7A: 3E 3F      LD      A,$3F           
6D7C: E0 F4      LDFF00  ($F4),A         
6D7E: CD 57 6C   CALL    $6C57           
6D81: C9         RET                     
6D82: 21 20 C3   LD      HL,$C320        
6D85: 09         ADD     HL,BC           
6D86: 36 30      LD      (HL),$30        
6D88: 21 10 C3   LD      HL,$C310        
6D8B: 09         ADD     HL,BC           
6D8C: 7E         LD      A,(HL)          
6D8D: FE 78      CP      $78             
6D8F: 38 1F      JR      C,$6DB0         
6D91: CD BD 27   CALL    $27BD           
6D94: CD 7C 7D   CALL    $7D7C           
6D97: 21 00 D9   LD      HL,$D900        
6D9A: F0 F6      LD      A,($F6)         
6D9C: 5F         LD      E,A             
6D9D: 50         LD      D,B             
6D9E: F0 F7      LD      A,($F7)         
6DA0: FE 1A      CP      $1A             
6DA2: 30 05      JR      NC,$6DA9        
6DA4: FE 06      CP      $06             
6DA6: 38 01      JR      C,$6DA9         
6DA8: 14         INC     D               
6DA9: 19         ADD     HL,DE           
6DAA: 7E         LD      A,(HL)          
6DAB: F6 20      OR      $20             
6DAD: 77         LD      (HL),A          
6DAE: E0 F8      LDFF00  ($F8),A         
6DB0: C9         RET                     
6DB1: 21 B0 C2   LD      HL,$C2B0        
6DB4: 09         ADD     HL,BC           
6DB5: 70         LD      (HL),B          
6DB6: CD 35 7D   CALL    $7D35           
6DB9: C6 30      ADD     $30             
6DBB: FE 60      CP      $60             
6DBD: 30 14      JR      NC,$6DD3        
6DBF: CD 45 7D   CALL    $7D45           
6DC2: C6 30      ADD     $30             
6DC4: FE 60      CP      $60             
6DC6: 30 0B      JR      NC,$6DD3        
6DC8: 7B         LD      A,E             
6DC9: FE 02      CP      $02             
6DCB: 20 13      JR      NZ,$6DE0        
6DCD: 21 B0 C2   LD      HL,$C2B0        
6DD0: 09         ADD     HL,BC           
6DD1: 36 01      LD      (HL),$01        
6DD3: CD 8D 3B   CALL    $3B8D           
6DD6: 36 07      LD      (HL),$07        
6DD8: CD 91 08   CALL    $0891           
6DDB: 36 20      LD      (HL),$20        
6DDD: CD EC 6A   CALL    $6AEC           
6DE0: C9         RET                     
6DE1: 21 10 C3   LD      HL,$C310        
6DE4: 09         ADD     HL,BC           
6DE5: 36 7F      LD      (HL),$7F        
6DE7: CD 91 08   CALL    $0891           
6DEA: 36 80      LD      (HL),$80        
6DEC: F0 B0      LD      A,($B0)         
6DEE: 21 90 C3   LD      HL,$C390        
6DF1: 09         ADD     HL,BC           
6DF2: 77         LD      (HL),A          
6DF3: 21 60 C3   LD      HL,$C360        
6DF6: 09         ADD     HL,BC           
6DF7: 36 FF      LD      (HL),$FF        
6DF9: F0 F6      LD      A,($F6)         
6DFB: FE 80      CP      $80             
6DFD: 20 02      JR      NZ,$6E01        
6DFF: 36 C0      LD      (HL),$C0        
6E01: 3E F8      LD      A,$F8           
6E03: EA 0A D2   LD      ($D20A),A       
6E06: 3E F8      LD      A,$F8           
6E08: EA 0B D2   LD      ($D20B),A       
6E0B: 3E F0      LD      A,$F0           
6E0D: EA 0E D2   LD      ($D20E),A       
6E10: 3E 00      LD      A,$00           
6E12: EA 07 D2   LD      ($D207),A       
6E15: EA 08 D2   LD      ($D208),A       
6E18: EA 09 D2   LD      ($D209),A       
6E1B: 3E 10      LD      A,$10           
6E1D: EA 0C D2   LD      ($D20C),A       
6E20: 3E F0      LD      A,$F0           
6E22: EA 0D D2   LD      ($D20D),A       
6E25: C9         RET                     
6E26: 70         LD      (HL),B          
6E27: 00         NOP                     
6E28: 70         LD      (HL),B          
6E29: 20 00      JR      NZ,$6E2B        
6E2B: F8 60      LDHL    SP,$60          
6E2D: 00         NOP                     
6E2E: 00         NOP                     
6E2F: 00         NOP                     
6E30: 62         LD      H,D             
6E31: 00         NOP                     
6E32: 00         NOP                     
6E33: 08 64 00   LD      ($0064),SP      
6E36: 00         NOP                     
6E37: 10 66      STOP    $66             
6E39: 00         NOP                     
6E3A: 00         NOP                     
6E3B: F8 66      LDHL    SP,$66          
6E3D: 20 00      JR      NZ,$6E3F        
6E3F: 00         NOP                     
6E40: 64         LD      H,H             
6E41: 20 00      JR      NZ,$6E43        
6E43: 08 62 20   LD      ($2062),SP      
6E46: 00         NOP                     
6E47: 10 60      STOP    $60             
6E49: 20 00      JR      NZ,$6E4B        
6E4B: F8 68      LDHL    SP,$68          
6E4D: 00         NOP                     
6E4E: 00         NOP                     
6E4F: 00         NOP                     
6E50: 6A         LD      L,D             
6E51: 00         NOP                     
6E52: 00         NOP                     
6E53: 08 6C 00   LD      ($006C),SP      
6E56: 00         NOP                     
6E57: 10 6E      STOP    $6E             
6E59: 00         NOP                     
6E5A: 00         NOP                     
6E5B: F8 6E      LDHL    SP,$6E          
6E5D: 20 00      JR      NZ,$6E5F        
6E5F: 00         NOP                     
6E60: 6C         LD      L,H             
6E61: 20 00      JR      NZ,$6E63        
6E63: 08 6A 20   LD      ($206A),SP      
6E66: 00         NOP                     
6E67: 10 68      STOP    $68             
6E69: 20 00      JR      NZ,$6E6B        
6E6B: 00         NOP                     
6E6C: 72         LD      (HL),D          
6E6D: 00         NOP                     
6E6E: F8 08      LDHL    SP,$08          
6E70: 74         LD      (HL),H          
6E71: 00         NOP                     
6E72: F8 00      LDHL    SP,$00          
6E74: 74         LD      (HL),H          
6E75: 20 00      JR      NZ,$6E77        
6E77: 08 72 20   LD      ($2072),SP      
6E7A: 00         NOP                     
6E7B: 00         NOP                     
6E7C: 72         LD      (HL),D          
6E7D: 40         LD      B,B             
6E7E: 08 08 74   LD      ($7408),SP      
6E81: 40         LD      B,B             
6E82: 08 00 74   LD      ($7400),SP      
6E85: 60         LD      H,B             
6E86: 00         NOP                     
6E87: 08 72 60   LD      ($6072),SP      
6E8A: 10 00      STOP    $00             
6E8C: 76         HALT                    
6E8D: 00         NOP                     
6E8E: 10 08      STOP    $08             
6E90: 78         LD      A,B             
6E91: 00         NOP                     
6E92: 10 10      STOP    $10             
6E94: 7A         LD      A,D             
6E95: 00         NOP                     
6E96: 08 18 7C   LD      ($7C18),SP      
6E99: 00         NOP                     
6E9A: F8 18      LDHL    SP,$18          
6E9C: 7E         LD      A,(HL)          
6E9D: 00         NOP                     
6E9E: 10 08      STOP    $08             
6EA0: 76         HALT                    
6EA1: 20 10      JR      NZ,$6EB3        
6EA3: 00         NOP                     
6EA4: 78         LD      A,B             
6EA5: 20 10      JR      NZ,$6EB7        
6EA7: F8 7A      LDHL    SP,$7A          
6EA9: 20 08      JR      NZ,$6EB3        
6EAB: F0 7C      LD      A,($7C)         
6EAD: 20 F8      JR      NZ,$6EA7        
6EAF: F0 7E      LD      A,($7E)         
6EB1: 20 0C      JR      NZ,$6EBF        
6EB3: FB         EI                      
6EB4: 26 00      LD      H,$00           
6EB6: 0C         INC     C               
6EB7: 01 26 00   LD      BC,$0026        
6EBA: 0C         INC     C               
6EBB: 07         RLCA                    
6EBC: 26 00      LD      H,$00           
6EBE: 0C         INC     C               
6EBF: 0D         DEC     C               
6EC0: 26 00      LD      H,$00           
6EC2: 21 10 C3   LD      HL,$C310        
6EC5: 09         ADD     HL,BC           
6EC6: 7E         LD      A,(HL)          
6EC7: FE 70      CP      $70             
6EC9: 30 5C      JR      NC,$6F27        
6ECB: CD F8 6E   CALL    $6EF8           
6ECE: CD 28 6F   CALL    $6F28           
6ED1: CD 4F 6F   CALL    $6F4F           
6ED4: CD 84 6F   CALL    $6F84           
6ED7: CD A5 6F   CALL    $6FA5           
6EDA: 21 10 C3   LD      HL,$C310        
6EDD: 09         ADD     HL,BC           
6EDE: 7E         LD      A,(HL)          
6EDF: A7         AND     A               
6EE0: 28 13      JR      Z,$6EF5         
6EE2: F0 EF      LD      A,($EF)         
6EE4: D6 02      SUB     $02             
6EE6: E0 EC      LDFF00  ($EC),A         
6EE8: 21 B2 6E   LD      HL,$6EB2        
6EEB: 0E 04      LD      C,$04           
6EED: CD 26 3D   CALL    $3D26           
6EF0: 3E 04      LD      A,$04           
6EF2: CD D0 3D   CALL    $3DD0           
6EF5: C3 BA 3D   JP      $3DBA           
6EF8: FA 0C D2   LD      A,($D20C)       
6EFB: 21 EE FF   LD      HL,$FFEE        
6EFE: 86         ADD     A,(HL)          
6EFF: 77         LD      (HL),A          
6F00: FA 0D D2   LD      A,($D20D)       
6F03: 21 EC FF   LD      HL,$FFEC        
6F06: 86         ADD     A,(HL)          
6F07: 77         LD      (HL),A          
6F08: FA 07 D2   LD      A,($D207)       
6F0B: FE FF      CP      $FF             
6F0D: 28 15      JR      Z,$6F24         
6F0F: 17         RLA                     
6F10: 17         RLA                     
6F11: 17         RLA                     
6F12: E6 F8      AND     $F8             
6F14: 5F         LD      E,A             
6F15: 50         LD      D,B             
6F16: 21 6A 6E   LD      HL,$6E6A        
6F19: 19         ADD     HL,DE           
6F1A: 0E 02      LD      C,$02           
6F1C: CD 26 3D   CALL    $3D26           
6F1F: 3E 02      LD      A,$02           
6F21: C3 48 6F   JP      $6F48           
6F24: CD BA 3D   CALL    $3DBA           
6F27: C9         RET                     
6F28: 21 00 C3   LD      HL,$C300        
6F2B: 09         ADD     HL,BC           
6F2C: 7E         LD      A,(HL)          
6F2D: A7         AND     A               
6F2E: 28 1E      JR      Z,$6F4E         
6F30: CD CC 6F   CALL    $6FCC           
6F33: 21 80 C3   LD      HL,$C380        
6F36: 09         ADD     HL,BC           
6F37: 7E         LD      A,(HL)          
6F38: 21 8A 6E   LD      HL,$6E8A        
6F3B: A7         AND     A               
6F3C: 28 03      JR      Z,$6F41         
6F3E: 21 9E 6E   LD      HL,$6E9E        
6F41: 0E 05      LD      C,$05           
6F43: CD 26 3D   CALL    $3D26           
6F46: 3E 05      LD      A,$05           
6F48: CD D0 3D   CALL    $3DD0           
6F4B: CD BA 3D   CALL    $3DBA           
6F4E: C9         RET                     
6F4F: FA 0A D2   LD      A,($D20A)       
6F52: 21 EE FF   LD      HL,$FFEE        
6F55: 86         ADD     A,(HL)          
6F56: 77         LD      (HL),A          
6F57: FA 0A D2   LD      A,($D20A)       
6F5A: C6 0C      ADD     $0C             
6F5C: EA C0 D5   LD      ($D5C0),A       
6F5F: FA 0B D2   LD      A,($D20B)       
6F62: 21 EC FF   LD      HL,$FFEC        
6F65: 86         ADD     A,(HL)          
6F66: 77         LD      (HL),A          
6F67: FA 0B D2   LD      A,($D20B)       
6F6A: C6 08      ADD     $08             
6F6C: EA C2 D5   LD      ($D5C2),A       
6F6F: 3E 08      LD      A,$08           
6F71: EA C1 D5   LD      ($D5C1),A       
6F74: 3E 06      LD      A,$06           
6F76: EA C3 D5   LD      ($D5C3),A       
6F79: 11 26 6E   LD      DE,$6E26        
6F7C: CD 3B 3C   CALL    $3C3B           
6F7F: 3E 02      LD      A,$02           
6F81: C3 48 6F   JP      $6F48           
6F84: FA 0E D2   LD      A,($D20E)       
6F87: 21 EC FF   LD      HL,$FFEC        
6F8A: 86         ADD     A,(HL)          
6F8B: 77         LD      (HL),A          
6F8C: FA 08 D2   LD      A,($D208)       
6F8F: 17         RLA                     
6F90: 17         RLA                     
6F91: 17         RLA                     
6F92: 17         RLA                     
6F93: E6 F0      AND     $F0             
6F95: 5F         LD      E,A             
6F96: 50         LD      D,B             
6F97: 21 2A 6E   LD      HL,$6E2A        
6F9A: 19         ADD     HL,DE           
6F9B: 0E 04      LD      C,$04           
6F9D: CD 26 3D   CALL    $3D26           
6FA0: 3E 04      LD      A,$04           
6FA2: C3 48 6F   JP      $6F48           
6FA5: FA 0E D2   LD      A,($D20E)       
6FA8: FE 00      CP      $00             
6FAA: C8         RET     Z               
6FAB: FA 0F D2   LD      A,($D20F)       
6FAE: 21 EC FF   LD      HL,$FFEC        
6FB1: 86         ADD     A,(HL)          
6FB2: 77         LD      (HL),A          
6FB3: FA 09 D2   LD      A,($D209)       
6FB6: 17         RLA                     
6FB7: 17         RLA                     
6FB8: 17         RLA                     
6FB9: 17         RLA                     
6FBA: E6 F0      AND     $F0             
6FBC: 5F         LD      E,A             
6FBD: 50         LD      D,B             
6FBE: 21 4A 6E   LD      HL,$6E4A        
6FC1: 19         ADD     HL,DE           
6FC2: 0E 04      LD      C,$04           
6FC4: CD 26 3D   CALL    $3D26           
6FC7: 3E 04      LD      A,$04           
6FC9: C3 48 6F   JP      $6F48           
6FCC: 21 46 C1   LD      HL,$C146        
6FCF: FA C7 DB   LD      A,($DBC7)       
6FD2: B6         OR      (HL)            
6FD3: 20 51      JR      NZ,$7026        
6FD5: F0 EC      LD      A,($EC)         
6FD7: C6 18      ADD     $18             
6FD9: 5F         LD      E,A             
6FDA: F0 99      LD      A,($99)         
6FDC: 21 A2 FF   LD      HL,$FFA2        
6FDF: 96         SUB     (HL)            
6FE0: C6 08      ADD     $08             
6FE2: 93         SUB     E               
6FE3: C6 0C      ADD     $0C             
6FE5: FE 18      CP      $18             
6FE7: 30 3D      JR      NC,$7026        
6FE9: 21 80 C3   LD      HL,$C380        
6FEC: 09         ADD     HL,BC           
6FED: 1E 08      LD      E,$08           
6FEF: 7E         LD      A,(HL)          
6FF0: A7         AND     A               
6FF1: 28 02      JR      Z,$6FF5         
6FF3: 1E F8      LD      E,$F8           
6FF5: F0 EE      LD      A,($EE)         
6FF7: 83         ADD     A,E             
6FF8: 21 98 FF   LD      HL,$FF98        
6FFB: 96         SUB     (HL)            
6FFC: C6 1A      ADD     $1A             
6FFE: FE 34      CP      $34             
7000: 30 24      JR      NC,$7026        
7002: 3E 28      LD      A,$28           
7004: CD 30 3C   CALL    $3C30           
7007: F0 D7      LD      A,($D7)         
7009: E0 9B      LDFF00  ($9B),A         
700B: F0 D8      LD      A,($D8)         
700D: E0 9A      LDFF00  ($9A),A         
700F: 3E 02      LD      A,$02           
7011: EA 46 C1   LD      ($C146),A       
7014: 3E 13      LD      A,$13           
7016: E0 A3      LDFF00  ($A3),A         
7018: 3E 08      LD      A,$08           
701A: EA 94 DB   LD      ($DB94),A       
701D: 3E 20      LD      A,$20           
701F: EA C7 DB   LD      ($DBC7),A       
7022: 3E 03      LD      A,$03           
7024: E0 F3      LDFF00  ($F3),A         
7026: C9         RET                     
7027: 12         LD      (DE),A          
7028: 14         INC     D               
7029: 16 18      LD      D,$18           
702B: 19         ADD     HL,DE           
702C: 1A         LD      A,(DE)          
702D: 1A         LD      A,(DE)          
702E: 1A         LD      A,(DE)          
702F: 1A         LD      A,(DE)          
7030: 1A         LD      A,(DE)          
7031: CD 76 7C   CALL    $7C76           
7034: CD 35 7D   CALL    $7D35           
7037: C6 20      ADD     $20             
7039: FE 40      CP      $40             
703B: 30 09      JR      NC,$7046        
703D: CD 45 7D   CALL    $7D45           
7040: C6 20      ADD     $20             
7042: FE 40      CP      $40             
7044: 38 66      JR      C,$70AC         
7046: 21 B0 C3   LD      HL,$C3B0        
7049: 09         ADD     HL,BC           
704A: 7E         LD      A,(HL)          
704B: 3C         INC     A               
704C: 77         LD      (HL),A          
704D: E6 7F      AND     $7F             
704F: C0         RET     NZ              
7050: 1E 0F      LD      E,$0F           
7052: 50         LD      D,B             
7053: 21 A0 C3   LD      HL,$C3A0        
7056: 19         ADD     HL,DE           
7057: 7E         LD      A,(HL)          
7058: FE 82      CP      $82             
705A: 28 1A      JR      Z,$7076         
705C: FE 9E      CP      $9E             
705E: 28 16      JR      Z,$7076         
7060: FE 7D      CP      $7D             
7062: 28 12      JR      Z,$7076         
7064: 21 40 C3   LD      HL,$C340        
7067: 19         ADD     HL,DE           
7068: 7E         LD      A,(HL)          
7069: E6 80      AND     $80             
706B: 20 09      JR      NZ,$7076        
706D: 21 80 C2   LD      HL,$C280        
7070: 19         ADD     HL,DE           
7071: 7E         LD      A,(HL)          
7072: FE 05      CP      $05             
7074: 28 07      JR      Z,$707D         
7076: 1D         DEC     E               
7077: 7B         LD      A,E             
7078: FE FF      CP      $FF             
707A: 20 D7      JR      NZ,$7053        
707C: C9         RET                     
707D: FA 8F C1   LD      A,($C18F)       
7080: A7         AND     A               
7081: C0         RET     NZ              
7082: 3E 7D      LD      A,$7D           
7084: CD 01 3C   CALL    $3C01           
7087: 38 23      JR      C,$70AC         
7089: F0 D7      LD      A,($D7)         
708B: 21 00 C2   LD      HL,$C200        
708E: 19         ADD     HL,DE           
708F: 77         LD      (HL),A          
7090: F0 D8      LD      A,($D8)         
7092: 21 10 C2   LD      HL,$C210        
7095: 19         ADD     HL,DE           
7096: 77         LD      (HL),A          
7097: C5         PUSH    BC              
7098: D5         PUSH    DE              
7099: C1         POP     BC              
709A: F0 F7      LD      A,($F7)         
709C: 5F         LD      E,A             
709D: 3E 14      LD      A,$14           
709F: FE 0A      CP      $0A             
70A1: 30 05      JR      NC,$70A8        
70A3: 21 27 70   LD      HL,$7027        
70A6: 19         ADD     HL,DE           
70A7: 7E         LD      A,(HL)          
70A8: CD 25 3C   CALL    $3C25           
70AB: C1         POP     BC              
70AC: C9         RET                     
70AD: 21 60 C4   LD      HL,$C460        
70B0: 09         ADD     HL,BC           
70B1: 7E         LD      A,(HL)          
70B2: FE 00      CP      $00             
70B4: 20 13      JR      NZ,$70C9        
70B6: F0 F8      LD      A,($F8)         
70B8: E6 10      AND     $10             
70BA: C2 7C 7D   JP      NZ,$7D7C        
70BD: 21 60 C4   LD      HL,$C460        
70C0: 09         ADD     HL,BC           
70C1: 36 FF      LD      (HL),$FF        
70C3: 21 E0 C4   LD      HL,$C4E0        
70C6: 09         ADD     HL,BC           
70C7: 36 3C      LD      (HL),$3C        
70C9: CD 76 7C   CALL    $7C76           
70CC: 21 B0 C3   LD      HL,$C3B0        
70CF: 09         ADD     HL,BC           
70D0: 70         LD      (HL),B          
70D1: 21 10 C4   LD      HL,$C410        
70D4: 09         ADD     HL,BC           
70D5: 7E         LD      A,(HL)          
70D6: A7         AND     A               
70D7: 28 70      JR      Z,$7149         
70D9: 3E 14      LD      A,$14           
70DB: CD 01 3C   CALL    $3C01           
70DE: 38 69      JR      C,$7149         
70E0: 21 E0 C4   LD      HL,$C4E0        
70E3: 09         ADD     HL,BC           
70E4: 7E         LD      A,(HL)          
70E5: 21 E0 C4   LD      HL,$C4E0        
70E8: 19         ADD     HL,DE           
70E9: 77         LD      (HL),A          
70EA: F0 D7      LD      A,($D7)         
70EC: 21 00 C2   LD      HL,$C200        
70EF: 19         ADD     HL,DE           
70F0: 77         LD      (HL),A          
70F1: F0 D8      LD      A,($D8)         
70F3: 21 10 C2   LD      HL,$C210        
70F6: 19         ADD     HL,DE           
70F7: C6 08      ADD     $08             
70F9: 77         LD      (HL),A          
70FA: CD 64 3E   CALL    $3E64           
70FD: F0 EE      LD      A,($EE)         
70FF: D6 08      SUB     $08             
7101: E0 CE      LDFF00  ($CE),A         
7103: F0 EF      LD      A,($EF)         
7105: D6 10      SUB     $10             
7107: E0 CD      LDFF00  ($CD),A         
7109: F0 CE      LD      A,($CE)         
710B: CB 37      SET     1,E             
710D: E6 0F      AND     $0F             
710F: 5F         LD      E,A             
7110: F0 CD      LD      A,($CD)         
7112: E6 F0      AND     $F0             
7114: B3         OR      E               
7115: 5F         LD      E,A             
7116: 50         LD      D,B             
7117: 21 11 D7   LD      HL,$D711        
711A: 19         ADD     HL,DE           
711B: 36 91      LD      (HL),$91        
711D: CD 39 28   CALL    $2839           
7120: FA 00 D6   LD      A,($D600)       
7123: 5F         LD      E,A             
7124: 16 00      LD      D,$00           
7126: 21 01 D6   LD      HL,$D601        
7129: 19         ADD     HL,DE           
712A: C6 0A      ADD     $0A             
712C: EA 00 D6   LD      ($D600),A       
712F: 1E 08      LD      E,$08           
7131: CD 36 71   CALL    $7136           
7134: 1E 09      LD      E,$09           
7136: F0 CF      LD      A,($CF)         
7138: 22         LD      (HLI),A         
7139: F0 D0      LD      A,($D0)         
713B: 22         LD      (HLI),A         
713C: 3C         INC     A               
713D: E0 D0      LDFF00  ($D0),A         
713F: 3E 81      LD      A,$81           
7141: 22         LD      (HLI),A         
7142: 7B         LD      A,E             
7143: 22         LD      (HLI),A         
7144: 3C         INC     A               
7145: 3C         INC     A               
7146: 22         LD      (HLI),A         
7147: AF         XOR     A               
7148: 77         LD      (HL),A          
7149: C9         RET                     
714A: 74         LD      (HL),H          
714B: 00         NOP                     
714C: 74         LD      (HL),H          
714D: 20 76      JR      NZ,$71C5        
714F: 00         NOP                     
7150: 78         LD      A,B             
7151: 00         NOP                     
7152: 7A         LD      A,D             
7153: 00         NOP                     
7154: 7A         LD      A,D             
7155: 20 78      JR      NZ,$71CF        
7157: 20 76      JR      NZ,$71CF        
7159: 20 7C      JR      NZ,$71D7        
715B: 00         NOP                     
715C: 7C         LD      A,H             
715D: 00         NOP                     
715E: 11 4A 71   LD      DE,$714A        
7161: CD 3B 3C   CALL    $3C3B           
7164: CD 76 7C   CALL    $7C76           
7167: CD 98 7C   CALL    $7C98           
716A: CD B4 3B   CALL    $3BB4           
716D: CD E2 7C   CALL    $7CE2           
7170: CD 9E 3B   CALL    $3B9E           
7173: 21 A0 C2   LD      HL,$C2A0        
7176: 09         ADD     HL,BC           
7177: 7E         LD      A,(HL)          
7178: E6 03      AND     $03             
717A: 20 07      JR      NZ,$7183        
717C: 7E         LD      A,(HL)          
717D: E6 0C      AND     $0C             
717F: 20 0C      JR      NZ,$718D        
7181: 18 12      JR      $7195           
7183: 21 40 C2   LD      HL,$C240        
7186: 09         ADD     HL,BC           
7187: 7E         LD      A,(HL)          
7188: 2F         CPL                     
7189: 3C         INC     A               
718A: 77         LD      (HL),A          
718B: 18 08      JR      $7195           
718D: 21 50 C2   LD      HL,$C250        
7190: 09         ADD     HL,BC           
7191: 7E         LD      A,(HL)          
7192: 2F         CPL                     
7193: 3C         INC     A               
7194: 77         LD      (HL),A          
7195: F0 E7      LD      A,($E7)         
7197: 1F         RRA                     
7198: 1F         RRA                     
7199: 1F         RRA                     
719A: E6 03      AND     $03             
719C: CD 87 3B   CALL    $3B87           
719F: C9         RET                     
71A0: FF         RST     0X38            
71A1: FF         RST     0X38            
71A2: FF         RST     0X38            
71A3: FF         RST     0X38            
71A4: FF         RST     0X38            
71A5: FF         RST     0X38            
71A6: FF         RST     0X38            
71A7: FF         RST     0X38            
71A8: 54         LD      D,H             
71A9: 00         NOP                     
71AA: 54         LD      D,H             
71AB: 20 52      JR      NZ,$71FF        
71AD: 00         NOP                     
71AE: 52         LD      D,D             
71AF: 20 56      JR      NZ,$7207        
71B1: 00         NOP                     
71B2: 56         LD      D,(HL)          
71B3: 00         NOP                     
71B4: F0 F1      LD      A,($F1)         
71B6: FE 01      CP      $01             
71B8: 20 08      JR      NZ,$71C2        
71BA: 11 B0 71   LD      DE,$71B0        
71BD: CD D0 3C   CALL    $3CD0           
71C0: 18 06      JR      $71C8           
71C2: 11 A0 71   LD      DE,$71A0        
71C5: CD 3B 3C   CALL    $3C3B           
71C8: CD 76 7C   CALL    $7C76           
71CB: CD 98 7C   CALL    $7C98           
71CE: CD 1B 7D   CALL    $7D1B           
71D1: 21 20 C3   LD      HL,$C320        
71D4: 09         ADD     HL,BC           
71D5: 35         DEC     (HL)            
71D6: 35         DEC     (HL)            
71D7: 21 10 C3   LD      HL,$C310        
71DA: 09         ADD     HL,BC           
71DB: 7E         LD      A,(HL)          
71DC: E6 80      AND     $80             
71DE: E0 E8      LDFF00  ($E8),A         
71E0: 28 06      JR      Z,$71E8         
71E2: 70         LD      (HL),B          
71E3: 21 20 C3   LD      HL,$C320        
71E6: 09         ADD     HL,BC           
71E7: 70         LD      (HL),B          
71E8: F0 F0      LD      A,($F0)         
71EA: C7         RST     0X00            
71EB: F9         LD      SP,HL           
71EC: 71         LD      (HL),C          
71ED: 25         DEC     H               
71EE: 72         LD      (HL),D          
71EF: 56         LD      D,(HL)          
71F0: 72         LD      (HL),D          
71F1: 64         LD      H,H             
71F2: 72         LD      (HL),D          
71F3: 86         ADD     A,(HL)          
71F4: 72         LD      (HL),D          
71F5: AB         XOR     E               
71F6: 72         LD      (HL),D          
71F7: E3         ???                     
71F8: 72         LD      (HL),D          
71F9: CD 91 08   CALL    $0891           
71FC: 20 26      JR      NZ,$7224        
71FE: CD 35 7D   CALL    $7D35           
7201: C6 20      ADD     $20             
7203: FE 40      CP      $40             
7205: 30 1D      JR      NC,$7224        
7207: CD 45 7D   CALL    $7D45           
720A: C6 20      ADD     $20             
720C: FE 40      CP      $40             
720E: 30 14      JR      NC,$7224        
7210: CD 8D 3B   CALL    $3B8D           
7213: CD 91 08   CALL    $0891           
7216: 36 20      LD      (HL),$20        
7218: CD ED 27   CALL    $27ED           
721B: E6 03      AND     $03             
721D: C6 03      ADD     $03             
721F: 21 B0 C2   LD      HL,$C2B0        
7222: 09         ADD     HL,BC           
7223: 77         LD      (HL),A          
7224: C9         RET                     
7225: CD 91 08   CALL    $0891           
7228: 20 1F      JR      NZ,$7249        
722A: 21 10 C3   LD      HL,$C310        
722D: 09         ADD     HL,BC           
722E: 36 08      LD      (HL),$08        
7230: 21 20 C3   LD      HL,$C320        
7233: 09         ADD     HL,BC           
7234: 36 08      LD      (HL),$08        
7236: 21 40 C3   LD      HL,$C340        
7239: 09         ADD     HL,BC           
723A: 36 12      LD      (HL),$12        
723C: 3E 03      LD      A,$03           
723E: CD 87 3B   CALL    $3B87           
7241: CD 8D 3B   CALL    $3B8D           
7244: 3E 24      LD      A,$24           
7246: E0 F2      LDFF00  ($F2),A         
7248: C9         RET                     
7249: 1E 01      LD      E,$01           
724B: FE 10      CP      $10             
724D: 30 02      JR      NC,$7251        
724F: 1E 02      LD      E,$02           
7251: 7B         LD      A,E             
7252: CD 87 3B   CALL    $3B87           
7255: C9         RET                     
7256: F0 E8      LD      A,($E8)         
7258: A7         AND     A               
7259: 28 08      JR      Z,$7263         
725B: CD 91 08   CALL    $0891           
725E: 36 20      LD      (HL),$20        
7260: CD 8D 3B   CALL    $3B8D           
7263: C9         RET                     
7264: CD EB 3B   CALL    $3BEB           
7267: CD 91 08   CALL    $0891           
726A: 20 09      JR      NZ,$7275        
726C: 36 10      LD      (HL),$10        
726E: CD AF 3D   CALL    $3DAF           
7271: CD 8D 3B   CALL    $3B8D           
7274: C9         RET                     
7275: 1E 08      LD      E,$08           
7277: E6 04      AND     $04             
7279: 28 02      JR      Z,$727D         
727B: 1E F8      LD      E,$F8           
727D: 21 40 C2   LD      HL,$C240        
7280: 09         ADD     HL,BC           
7281: 73         LD      (HL),E          
7282: CD EF 7C   CALL    $7CEF           
7285: C9         RET                     
7286: CD B4 3B   CALL    $3BB4           
7289: CD E2 7C   CALL    $7CE2           
728C: CD 05 73   CALL    $7305           
728F: CD 91 08   CALL    $0891           
7292: 20 11      JR      NZ,$72A5        
7294: 3E 0C      LD      A,$0C           
7296: CD 25 3C   CALL    $3C25           
7299: 21 20 C3   LD      HL,$C320        
729C: 09         ADD     HL,BC           
729D: 36 18      LD      (HL),$18        
729F: CD 44 72   CALL    $7244           
72A2: CD 8D 3B   CALL    $3B8D           
72A5: 3E 03      LD      A,$03           
72A7: CD 87 3B   CALL    $3B87           
72AA: C9         RET                     
72AB: CD B4 3B   CALL    $3BB4           
72AE: CD E2 7C   CALL    $7CE2           
72B1: CD 05 73   CALL    $7305           
72B4: F0 E8      LD      A,($E8)         
72B6: A7         AND     A               
72B7: 28 24      JR      Z,$72DD         
72B9: CD AF 3D   CALL    $3DAF           
72BC: CD 8D 3B   CALL    $3B8D           
72BF: 36 04      LD      (HL),$04        
72C1: CD 91 08   CALL    $0891           
72C4: 36 20      LD      (HL),$20        
72C6: 21 B0 C2   LD      HL,$C2B0        
72C9: 09         ADD     HL,BC           
72CA: 35         DEC     (HL)            
72CB: 20 10      JR      NZ,$72DD        
72CD: CD 8D 3B   CALL    $3B8D           
72D0: 36 06      LD      (HL),$06        
72D2: CD 91 08   CALL    $0891           
72D5: 36 30      LD      (HL),$30        
72D7: 21 40 C3   LD      HL,$C340        
72DA: 09         ADD     HL,BC           
72DB: 36 D2      LD      (HL),$D2        
72DD: 3E 02      LD      A,$02           
72DF: CD 87 3B   CALL    $3B87           
72E2: C9         RET                     
72E3: CD 91 08   CALL    $0891           
72E6: 20 0B      JR      NZ,$72F3        
72E8: 36 50      LD      (HL),$50        
72EA: CD 8D 3B   CALL    $3B8D           
72ED: 70         LD      (HL),B          
72EE: AF         XOR     A               
72EF: CD 87 3B   CALL    $3B87           
72F2: C9         RET                     
72F3: 1E 03      LD      E,$03           
72F5: FE 20      CP      $20             
72F7: 30 07      JR      NC,$7300        
72F9: 1E 01      LD      E,$01           
72FB: FE 10      CP      $10             
72FD: 38 01      JR      C,$7300         
72FF: 1C         INC     E               
7300: 7B         LD      A,E             
7301: CD 87 3B   CALL    $3B87           
7304: C9         RET                     
7305: 21 10 C4   LD      HL,$C410        
7308: 09         ADD     HL,BC           
7309: 36 03      LD      (HL),$03        
730B: CD 9E 3B   CALL    $3B9E           
730E: 21 10 C4   LD      HL,$C410        
7311: 09         ADD     HL,BC           
7312: 70         LD      (HL),B          
7313: C9         RET                     
7314: CD 76 7C   CALL    $7C76           
7317: F0 F0      LD      A,($F0)         
7319: C7         RST     0X00            
731A: 1E 73      LD      E,$73           
731C: B7         OR      A               
731D: 73         LD      (HL),E          
731E: F0 EE      LD      A,($EE)         
7320: E6 70      AND     $70             
7322: EA 01 D2   LD      ($D201),A       
7325: CD 91 08   CALL    $0891           
7328: 36 80      LD      (HL),$80        
732A: CD 8D 3B   CALL    $3B8D           
732D: C9         RET                     
732E: 23         INC     HL              
732F: 56         LD      D,(HL)          
7330: 26 53      LD      H,$53           
7332: 32         LD      (HLD),A         
7333: 47         LD      B,A             
7334: 42         LD      B,D             
7335: 37         SCF                     
7336: 33         INC     SP              
7337: 46         LD      B,(HL)          
7338: 43         LD      B,E             
7339: 36 24      LD      (HL),$24        
733B: 55         LD      D,L             
733C: 25         DEC     H               
733D: 54         LD      D,H             
733E: 21 28 53   LD      HL,$5328        
7341: 56         LD      D,(HL)          
7342: 34         INC     (HL)            
7343: 45         LD      B,L             
7344: 35         DEC     (HL)            
7345: 44         LD      B,H             
7346: 31 48 38   LD      SP,$3848        
7349: 41         LD      B,C             
734A: 14         INC     D               
734B: 66         LD      H,(HL)          
734C: 15         DEC     D               
734D: 63         LD      H,E             
734E: 31 45 38   LD      SP,$3845        
7351: 44         LD      B,H             
7352: 13         INC     DE              
7353: 56         LD      D,(HL)          
7354: 16 53      LD      D,$53           
7356: 27         DAA                     
7357: 42         LD      B,D             
7358: 47         LD      B,A             
7359: 22         LD      (HLI),A         
735A: 65         LD      H,L             
735B: 33         INC     SP              
735C: 64         LD      H,H             
735D: 36 23      LD      (HL),$23        
735F: 56         LD      D,(HL)          
7360: 26 53      LD      H,$53           
7362: 32         LD      (HLD),A         
7363: 47         LD      B,A             
7364: 42         LD      B,D             
7365: 37         SCF                     
7366: 33         INC     SP              
7367: 46         LD      B,(HL)          
7368: 43         LD      B,E             
7369: 36 24      LD      (HL),$24        
736B: 55         LD      D,L             
736C: 25         DEC     H               
736D: 54         LD      D,H             
736E: 23         INC     HL              
736F: 56         LD      D,(HL)          
7370: 26 53      LD      H,$53           
7372: 32         LD      (HLD),A         
7373: 47         LD      B,A             
7374: 42         LD      B,D             
7375: 37         SCF                     
7376: 33         INC     SP              
7377: 46         LD      B,(HL)          
7378: 43         LD      B,E             
7379: 36 24      LD      (HL),$24        
737B: 55         LD      D,L             
737C: 25         DEC     H               
737D: 54         LD      D,H             
737E: 23         INC     HL              
737F: 56         LD      D,(HL)          
7380: 26 53      LD      H,$53           
7382: 32         LD      (HLD),A         
7383: 47         LD      B,A             
7384: 42         LD      B,D             
7385: 37         SCF                     
7386: 33         INC     SP              
7387: 46         LD      B,(HL)          
7388: 43         LD      B,E             
7389: 36 24      LD      (HL),$24        
738B: 55         LD      D,L             
738C: 25         DEC     H               
738D: 54         LD      D,H             
738E: 23         INC     HL              
738F: 56         LD      D,(HL)          
7390: 26 53      LD      H,$53           
7392: 32         LD      (HLD),A         
7393: 47         LD      B,A             
7394: 42         LD      B,D             
7395: 37         SCF                     
7396: 33         INC     SP              
7397: 46         LD      B,(HL)          
7398: 43         LD      B,E             
7399: 36 24      LD      (HL),$24        
739B: 55         LD      D,L             
739C: 25         DEC     H               
739D: 54         LD      D,H             
739E: 23         INC     HL              
739F: 56         LD      D,(HL)          
73A0: 26 53      LD      H,$53           
73A2: 32         LD      (HLD),A         
73A3: 47         LD      B,A             
73A4: 42         LD      B,D             
73A5: 37         SCF                     
73A6: 33         INC     SP              
73A7: 46         LD      B,(HL)          
73A8: 43         LD      B,E             
73A9: 36 24      LD      (HL),$24        
73AB: 55         LD      D,L             
73AC: 25         DEC     H               
73AD: 54         LD      D,H             
73AE: 30 30      JR      NC,$73E0        
73B0: 30 30      JR      NC,$73E2        
73B2: 30 30      JR      NC,$73E4        
73B4: 30 28      JR      NC,$73DE        
73B6: 28 21      JR      Z,$73D9         
73B8: D0         RET     NC              
73B9: C3 09 7E   JP      $7E09           
73BC: FE 10      CP      $10             
73BE: CA 7C 7D   JP      Z,$7D7C         
73C1: CD 91 08   CALL    $0891           
73C4: 20 75      JR      NZ,$743B        
73C6: E5         PUSH    HL              
73C7: F0 F7      LD      A,($F7)         
73C9: 5F         LD      E,A             
73CA: 50         LD      D,B             
73CB: 21 AE 73   LD      HL,$73AE        
73CE: 19         ADD     HL,DE           
73CF: 7E         LD      A,(HL)          
73D0: E1         POP     HL              
73D1: 77         LD      (HL),A          
73D2: 3E 5A      LD      A,$5A           
73D4: CD 01 3C   CALL    $3C01           
73D7: 38 62      JR      C,$743B         
73D9: 21 B0 C2   LD      HL,$C2B0        
73DC: 19         ADD     HL,DE           
73DD: 36 02      LD      (HL),$02        
73DF: C5         PUSH    BC              
73E0: FA 01 D2   LD      A,($D201)       
73E3: 21 D0 C3   LD      HL,$C3D0        
73E6: 09         ADD     HL,BC           
73E7: 86         ADD     A,(HL)          
73E8: 34         INC     (HL)            
73E9: 4F         LD      C,A             
73EA: 21 40 C4   LD      HL,$C440        
73ED: 19         ADD     HL,DE           
73EE: F0 EF      LD      A,($EF)         
73F0: D6 10      SUB     $10             
73F2: E6 F0      AND     $F0             
73F4: 28 01      JR      Z,$73F7         
73F6: 77         LD      (HL),A          
73F7: 79         LD      A,C             
73F8: FE 0F      CP      $0F             
73FA: 20 0B      JR      NZ,$7407        
73FC: FA 8E C1   LD      A,($C18E)       
73FF: E6 1F      AND     $1F             
7401: FE 03      CP      $03             
7403: 20 02      JR      NZ,$7407        
7405: 36 01      LD      (HL),$01        
7407: 21 2E 73   LD      HL,$732E        
740A: 09         ADD     HL,BC           
740B: 7E         LD      A,(HL)          
740C: F5         PUSH    AF              
740D: CB 37      SET     1,E             
740F: E6 F0      AND     $F0             
7411: F6 08      OR      $08             
7413: 21 00 C2   LD      HL,$C200        
7416: 19         ADD     HL,DE           
7417: 77         LD      (HL),A          
7418: F1         POP     AF              
7419: E6 F0      AND     $F0             
741B: C6 10      ADD     $10             
741D: 21 10 C2   LD      HL,$C210        
7420: 19         ADD     HL,DE           
7421: 77         LD      (HL),A          
7422: 21 40 C3   LD      HL,$C340        
7425: 19         ADD     HL,DE           
7426: 36 12      LD      (HL),$12        
7428: 21 50 C3   LD      HL,$C350        
742B: 19         ADD     HL,DE           
742C: 36 00      LD      (HL),$00        
742E: 21 30 C4   LD      HL,$C430        
7431: 19         ADD     HL,DE           
7432: 36 00      LD      (HL),$00        
7434: 21 D0 C4   LD      HL,$C4D0        
7437: 19         ADD     HL,DE           
7438: 36 00      LD      (HL),$00        
743A: C1         POP     BC              
743B: C9         RET                     
743C: 70         LD      (HL),B          
743D: 00         NOP                     
743E: 70         LD      (HL),B          
743F: 20 72      JR      NZ,$74B3        
7441: 00         NOP                     
7442: 72         LD      (HL),D          
7443: 20 11      JR      NZ,$7456        
7445: 3C         INC     A               
7446: 74         LD      (HL),H          
7447: CD 3B 3C   CALL    $3C3B           
744A: CD 76 7C   CALL    $7C76           
744D: CD 98 7C   CALL    $7C98           
7450: F0 E7      LD      A,($E7)         
7452: 1F         RRA                     
7453: 1F         RRA                     
7454: 1F         RRA                     
7455: 1F         RRA                     
7456: E6 01      AND     $01             
7458: CD 87 3B   CALL    $3B87           
745B: CD E2 7C   CALL    $7CE2           
745E: CD 9E 3B   CALL    $3B9E           
7461: 21 A0 C2   LD      HL,$C2A0        
7464: 09         ADD     HL,BC           
7465: 7E         LD      A,(HL)          
7466: E6 0F      AND     $0F             
7468: 28 0F      JR      Z,$7479         
746A: CD 91 08   CALL    $0891           
746D: 36 10      LD      (HL),$10        
746F: CD AF 3D   CALL    $3DAF           
7472: CD 8D 3B   CALL    $3B8D           
7475: AF         XOR     A               
7476: 77         LD      (HL),A          
7477: E0 F0      LDFF00  ($F0),A         
7479: CD B4 3B   CALL    $3BB4           
747C: F0 F0      LD      A,($F0)         
747E: C7         RST     0X00            
747F: 85         ADD     A,L             
7480: 74         LD      (HL),H          
7481: A6         AND     (HL)            
7482: 74         LD      (HL),H          
7483: C7         RST     0X00            
7484: 74         LD      (HL),H          
7485: CD 91 08   CALL    $0891           
7488: 20 1B      JR      NZ,$74A5        
748A: 36 20      LD      (HL),$20        
748C: CD 8D 3B   CALL    $3B8D           
748F: CD ED 27   CALL    $27ED           
7492: E6 02      AND     $02             
7494: 3D         DEC     A               
7495: 21 B0 C2   LD      HL,$C2B0        
7498: 09         ADD     HL,BC           
7499: 77         LD      (HL),A          
749A: CD ED 27   CALL    $27ED           
749D: E6 02      AND     $02             
749F: 3D         DEC     A               
74A0: 21 C0 C2   LD      HL,$C2C0        
74A3: 09         ADD     HL,BC           
74A4: 77         LD      (HL),A          
74A5: C9         RET                     
74A6: CD 91 08   CALL    $0891           
74A9: CA 8D 3B   JP      Z,$3B8D         
74AC: E6 01      AND     $01             
74AE: 20 16      JR      NZ,$74C6        
74B0: 21 B0 C2   LD      HL,$C2B0        
74B3: 09         ADD     HL,BC           
74B4: 7E         LD      A,(HL)          
74B5: 21 40 C2   LD      HL,$C240        
74B8: 09         ADD     HL,BC           
74B9: 86         ADD     A,(HL)          
74BA: 77         LD      (HL),A          
74BB: 21 C0 C2   LD      HL,$C2C0        
74BE: 09         ADD     HL,BC           
74BF: 7E         LD      A,(HL)          
74C0: 21 50 C2   LD      HL,$C250        
74C3: 09         ADD     HL,BC           
74C4: 86         ADD     A,(HL)          
74C5: 77         LD      (HL),A          
74C6: C9         RET                     
74C7: F0 E7      LD      A,($E7)         
74C9: E6 01      AND     $01             
74CB: 20 21      JR      NZ,$74EE        
74CD: 21 40 C2   LD      HL,$C240        
74D0: 09         ADD     HL,BC           
74D1: 7E         LD      A,(HL)          
74D2: A7         AND     A               
74D3: 20 0A      JR      NZ,$74DF        
74D5: CD 8D 3B   CALL    $3B8D           
74D8: 70         LD      (HL),B          
74D9: CD 91 08   CALL    $0891           
74DC: 36 10      LD      (HL),$10        
74DE: C9         RET                     
74DF: CD E7 74   CALL    $74E7           
74E2: 21 50 C2   LD      HL,$C250        
74E5: 09         ADD     HL,BC           
74E6: 7E         LD      A,(HL)          
74E7: CB 7F      SET     1,E             
74E9: 28 02      JR      Z,$74ED         
74EB: 34         INC     (HL)            
74EC: 34         INC     (HL)            
74ED: 35         DEC     (HL)            
74EE: C9         RET                     
74EF: 60         LD      H,B             
74F0: 00         NOP                     
74F1: 62         LD      H,D             
74F2: 00         NOP                     
74F3: 64         LD      H,H             
74F4: 00         NOP                     
74F5: 66         LD      H,(HL)          
74F6: 00         NOP                     
74F7: 62         LD      H,D             
74F8: 60         LD      H,B             
74F9: 60         LD      H,B             
74FA: 60         LD      H,B             
74FB: 66         LD      H,(HL)          
74FC: 60         LD      H,B             
74FD: 64         LD      H,H             
74FE: 60         LD      H,B             
74FF: 66         LD      H,(HL)          
7500: 20 64      JR      NZ,$7566        
7502: 20 21      JR      NZ,$7525        
7504: 60         LD      H,B             
7505: C4 09 7E   CALL    NZ,$7E09        
7508: A7         AND     A               
7509: 28 04      JR      Z,$750F         
750B: 79         LD      A,C             
750C: EA 01 D2   LD      ($D201),A       
750F: 11 EF 74   LD      DE,$74EF        
7512: CD 3B 3C   CALL    $3C3B           
7515: CD 76 7C   CALL    $7C76           
7518: CD E2 7C   CALL    $7CE2           
751B: CD 1B 7D   CALL    $7D1B           
751E: CD 9E 3B   CALL    $3B9E           
7521: 21 20 C3   LD      HL,$C320        
7524: 09         ADD     HL,BC           
7525: 35         DEC     (HL)            
7526: 35         DEC     (HL)            
7527: 21 10 C3   LD      HL,$C310        
752A: 09         ADD     HL,BC           
752B: 7E         LD      A,(HL)          
752C: E0 E8      LDFF00  ($E8),A         
752E: 3D         DEC     A               
752F: E6 80      AND     $80             
7531: 28 11      JR      Z,$7544         
7533: 70         LD      (HL),B          
7534: 21 20 C3   LD      HL,$C320        
7537: 09         ADD     HL,BC           
7538: 7E         LD      A,(HL)          
7539: E0 E9      LDFF00  ($E9),A         
753B: CB 2F      SET     1,E             
753D: 2F         CPL                     
753E: FE 07      CP      $07             
7540: 30 01      JR      NC,$7543        
7542: AF         XOR     A               
7543: 77         LD      (HL),A          
7544: F0 F0      LD      A,($F0)         
7546: C7         RST     0X00            
7547: 51         LD      D,C             
7548: 75         LD      (HL),L          
7549: 51         LD      D,C             
754A: 75         LD      (HL),L          
754B: 69         LD      L,C             
754C: 75         LD      (HL),L          
754D: 02         LD      (BC),A          
754E: 76         HALT                    
754F: 3B         DEC     SP              
7550: 76         HALT                    
7551: CD 4B 76   CALL    $764B           
7554: C9         RET                     
7555: 00         NOP                     
7556: 0C         INC     C               
7557: 10 0C      STOP    $0C             
7559: 00         NOP                     
755A: F4         ???                     
755B: F0 F4      LD      A,($F4)         
755D: F0 F4      LD      A,($F4)         
755F: 00         NOP                     
7560: 0C         INC     C               
7561: 10 0C      STOP    $0C             
7563: 00         NOP                     
7564: F4         ???                     
7565: 00         NOP                     
7566: 01 04 00   LD      BC,$0004        
7569: CD 91 08   CALL    $0891           
756C: 20 16      JR      NZ,$7584        
756E: CD AF 3D   CALL    $3DAF           
7571: CD 8D 3B   CALL    $3B8D           
7574: CD ED 27   CALL    $27ED           
7577: E6 03      AND     $03             
7579: 5F         LD      E,A             
757A: 50         LD      D,B             
757B: 21 65 75   LD      HL,$7565        
757E: 19         ADD     HL,DE           
757F: 7E         LD      A,(HL)          
7580: CD 87 3B   CALL    $3B87           
7583: C9         RET                     
7584: E6 07      AND     $07             
7586: 20 09      JR      NZ,$7591        
7588: 21 B0 C3   LD      HL,$C3B0        
758B: 09         ADD     HL,BC           
758C: 7E         LD      A,(HL)          
758D: 3C         INC     A               
758E: E6 03      AND     $03             
7590: 77         LD      (HL),A          
7591: F0 E8      LD      A,($E8)         
7593: 3D         DEC     A               
7594: E6 80      AND     $80             
7596: 28 3E      JR      Z,$75D6         
7598: CD FB 75   CALL    $75FB           
759B: F0 E9      LD      A,($E9)         
759D: D6 FC      SUB     $FC             
759F: E6 80      AND     $80             
75A1: 20 06      JR      NZ,$75A9        
75A3: F0 E7      LD      A,($E7)         
75A5: E6 07      AND     $07             
75A7: 20 2D      JR      NZ,$75D6        
75A9: CD ED 27   CALL    $27ED           
75AC: E6 01      AND     $01             
75AE: 1E 01      LD      E,$01           
75B0: 28 02      JR      Z,$75B4         
75B2: 1E FF      LD      E,$FF           
75B4: 21 80 C3   LD      HL,$C380        
75B7: 09         ADD     HL,BC           
75B8: 7E         LD      A,(HL)          
75B9: 83         ADD     A,E             
75BA: E6 07      AND     $07             
75BC: 77         LD      (HL),A          
75BD: 5F         LD      E,A             
75BE: 50         LD      D,B             
75BF: 21 55 75   LD      HL,$7555        
75C2: 19         ADD     HL,DE           
75C3: 7E         LD      A,(HL)          
75C4: 21 40 C2   LD      HL,$C240        
75C7: 09         ADD     HL,BC           
75C8: 77         LD      (HL),A          
75C9: 21 5D 75   LD      HL,$755D        
75CC: 19         ADD     HL,DE           
75CD: 7E         LD      A,(HL)          
75CE: 21 50 C2   LD      HL,$C250        
75D1: 09         ADD     HL,BC           
75D2: 77         LD      (HL),A          
75D3: CD FB 75   CALL    $75FB           
75D6: 21 A0 C2   LD      HL,$C2A0        
75D9: 09         ADD     HL,BC           
75DA: 7E         LD      A,(HL)          
75DB: A7         AND     A               
75DC: 28 23      JR      Z,$7601         
75DE: 21 80 C3   LD      HL,$C380        
75E1: 09         ADD     HL,BC           
75E2: 7E         LD      A,(HL)          
75E3: EE 04      XOR     $04             
75E5: 77         LD      (HL),A          
75E6: CD 91 08   CALL    $0891           
75E9: CB 3E      SET     1,E             
75EB: 21 40 C2   LD      HL,$C240        
75EE: CD F4 75   CALL    $75F4           
75F1: 21 50 C2   LD      HL,$C250        
75F4: 09         ADD     HL,BC           
75F5: 7E         LD      A,(HL)          
75F6: 2F         CPL                     
75F7: CB 2F      SET     1,E             
75F9: 3C         INC     A               
75FA: 77         LD      (HL),A          
75FB: 21 D0 C5   LD      HL,$C5D0        
75FE: 09         ADD     HL,BC           
75FF: 36 FF      LD      (HL),$FF        
7601: C9         RET                     
7602: 21 60 C4   LD      HL,$C460        
7605: 09         ADD     HL,BC           
7606: 7E         LD      A,(HL)          
7607: A7         AND     A               
7608: 20 30      JR      NZ,$763A        
760A: FA 01 D2   LD      A,($D201)       
760D: 5F         LD      E,A             
760E: 50         LD      D,B             
760F: 21 90 C2   LD      HL,$C290        
7612: 19         ADD     HL,DE           
7613: 7E         LD      A,(HL)          
7614: FE 03      CP      $03             
7616: 20 22      JR      NZ,$763A        
7618: 34         INC     (HL)            
7619: CD 8D 3B   CALL    $3B8D           
761C: F0 F1      LD      A,($F1)         
761E: FE 00      CP      $00             
7620: 20 0A      JR      NZ,$762C        
7622: 21 B0 C3   LD      HL,$C3B0        
7625: 19         ADD     HL,DE           
7626: 7E         LD      A,(HL)          
7627: FE 00      CP      $00             
7629: CA EC 08   JP      Z,$08EC         
762C: 21 E0 C2   LD      HL,$C2E0        
762F: 19         ADD     HL,DE           
7630: 36 40      LD      (HL),$40        
7632: CD 91 08   CALL    $0891           
7635: 36 40      LD      (HL),$40        
7637: C3 AC 08   JP      $08AC           
763A: C9         RET                     
763B: CD 91 08   CALL    $0891           
763E: FE 01      CP      $01             
7640: 20 05      JR      NZ,$7647        
7642: 3E 01      LD      A,$01           
7644: CD 87 3B   CALL    $3B87           
7647: CD 4B 76   CALL    $764B           
764A: C9         RET                     
764B: CD D5 3B   CALL    $3BD5           
764E: 30 4B      JR      NC,$769B        
7650: FA 9B C1   LD      A,($C19B)       
7653: A7         AND     A               
7654: 20 45      JR      NZ,$769B        
7656: FA 00 DB   LD      A,($DB00)       
7659: FE 03      CP      $03             
765B: 20 08      JR      NZ,$7665        
765D: F0 CC      LD      A,($CC)         
765F: E6 20      AND     $20             
7661: 20 0F      JR      NZ,$7672        
7663: 18 36      JR      $769B           
7665: FA 01 DB   LD      A,($DB01)       
7668: FE 03      CP      $03             
766A: 20 2F      JR      NZ,$769B        
766C: F0 CC      LD      A,($CC)         
766E: E6 10      AND     $10             
7670: 28 29      JR      Z,$769B         
7672: FA CF C3   LD      A,($C3CF)       
7675: A7         AND     A               
7676: 20 23      JR      NZ,$769B        
7678: 3C         INC     A               
7679: EA CF C3   LD      ($C3CF),A       
767C: CD 8D 3B   CALL    $3B8D           
767F: 36 02      LD      (HL),$02        
7681: 21 80 C2   LD      HL,$C280        
7684: 09         ADD     HL,BC           
7685: 36 07      LD      (HL),$07        
7687: 21 90 C4   LD      HL,$C490        
768A: 09         ADD     HL,BC           
768B: 70         LD      (HL),B          
768C: F0 9E      LD      A,($9E)         
768E: EA 5D C1   LD      ($C15D),A       
7691: CD 91 08   CALL    $0891           
7694: 36 02      LD      (HL),$02        
7696: 21 F3 FF   LD      HL,$FFF3        
7699: 36 02      LD      (HL),$02        
769B: C9         RET                     
769C: 70         LD      (HL),B          
769D: 00         NOP                     
769E: 70         LD      (HL),B          
769F: 20 72      JR      NZ,$7713        
76A1: 00         NOP                     
76A2: 72         LD      (HL),D          
76A3: 20 74      JR      NZ,$7719        
76A5: 00         NOP                     
76A6: 74         LD      (HL),H          
76A7: 20 76      JR      NZ,$771F        
76A9: 00         NOP                     
76AA: 76         HALT                    
76AB: 20 60      JR      NZ,$770D        
76AD: 00         NOP                     
76AE: 60         LD      H,B             
76AF: 20 62      JR      NZ,$7713        
76B1: 00         NOP                     
76B2: 62         LD      H,D             
76B3: 20 64      JR      NZ,$7719        
76B5: 00         NOP                     
76B6: 64         LD      H,H             
76B7: 20 66      JR      NZ,$771F        
76B9: 00         NOP                     
76BA: 66         LD      H,(HL)          
76BB: 20 11      JR      NZ,$76CE        
76BD: 9C         SBC     H               
76BE: 76         HALT                    
76BF: F0 F7      LD      A,($F7)         
76C1: FE 03      CP      $03             
76C3: 20 03      JR      NZ,$76C8        
76C5: 11 AC 76   LD      DE,$76AC        
76C8: CD 3B 3C   CALL    $3C3B           
76CB: CD 76 7C   CALL    $7C76           
76CE: 21 10 C4   LD      HL,$C410        
76D1: 09         ADD     HL,BC           
76D2: 7E         LD      A,(HL)          
76D3: A7         AND     A               
76D4: 28 03      JR      Z,$76D9         
76D6: CD AF 3D   CALL    $3DAF           
76D9: CD 98 7C   CALL    $7C98           
76DC: CD B4 3B   CALL    $3BB4           
76DF: CD E2 7C   CALL    $7CE2           
76E2: CD 1B 7D   CALL    $7D1B           
76E5: CD 9E 3B   CALL    $3B9E           
76E8: 21 20 C3   LD      HL,$C320        
76EB: 09         ADD     HL,BC           
76EC: 35         DEC     (HL)            
76ED: 35         DEC     (HL)            
76EE: 21 10 C3   LD      HL,$C310        
76F1: 09         ADD     HL,BC           
76F2: 7E         LD      A,(HL)          
76F3: CB 7F      SET     1,E             
76F5: 20 03      JR      NZ,$76FA        
76F7: A7         AND     A               
76F8: 20 2D      JR      NZ,$7727        
76FA: 70         LD      (HL),B          
76FB: F0 F0      LD      A,($F0)         
76FD: FE 03      CP      $03             
76FF: 20 21      JR      NZ,$7722        
7701: 21 40 C2   LD      HL,$C240        
7704: 09         ADD     HL,BC           
7705: CB 2E      SET     1,E             
7707: 21 50 C2   LD      HL,$C250        
770A: 09         ADD     HL,BC           
770B: CB 2E      SET     1,E             
770D: 21 20 C3   LD      HL,$C320        
7710: 09         ADD     HL,BC           
7711: 7E         LD      A,(HL)          
7712: CB 2F      SET     1,E             
7714: 2F         CPL                     
7715: 77         LD      (HL),A          
7716: FE 07      CP      $07             
7718: 30 06      JR      NC,$7720        
771A: 70         LD      (HL),B          
771B: CD AF 3D   CALL    $3DAF           
771E: 18 07      JR      $7727           
7720: 18 05      JR      $7727           
7722: 21 20 C3   LD      HL,$C320        
7725: 09         ADD     HL,BC           
7726: 70         LD      (HL),B          
7727: F0 F0      LD      A,($F0)         
7729: FE 04      CP      $04             
772B: 38 01      JR      C,$772E         
772D: C9         RET                     
772E: C7         RST     0X00            
772F: 3F         CCF                     
7730: 77         LD      (HL),A          
7731: 7B         LD      A,E             
7732: 77         LD      (HL),A          
7733: C0         RET     NZ              
7734: 77         LD      (HL),A          
7735: 09         ADD     HL,BC           
7736: 78         LD      A,B             
7737: 06 FA      LD      B,$FA           
7739: 00         NOP                     
773A: 00         NOP                     
773B: 00         NOP                     
773C: 00         NOP                     
773D: FA 06 CD   LD      A,($CD06)       
7740: AF         XOR     A               
7741: 3D         DEC     A               
7742: CD 91 08   CALL    $0891           
7745: 20 32      JR      NZ,$7779        
7747: CD ED 27   CALL    $27ED           
774A: E6 1F      AND     $1F             
774C: C6 30      ADD     $30             
774E: 77         LD      (HL),A          
774F: CD 8D 3B   CALL    $3B8D           
7752: CD ED 27   CALL    $27ED           
7755: E6 06      AND     $06             
7757: 20 05      JR      NZ,$775E        
7759: CD 55 7D   CALL    $7D55           
775C: 18 06      JR      $7764           
775E: CD ED 27   CALL    $27ED           
7761: E6 03      AND     $03             
7763: 5F         LD      E,A             
7764: 50         LD      D,B             
7765: 21 37 77   LD      HL,$7737        
7768: 19         ADD     HL,DE           
7769: 7E         LD      A,(HL)          
776A: 21 40 C2   LD      HL,$C240        
776D: 09         ADD     HL,BC           
776E: 77         LD      (HL),A          
776F: 21 3B 77   LD      HL,$773B        
7772: 19         ADD     HL,DE           
7773: 7E         LD      A,(HL)          
7774: 21 50 C2   LD      HL,$C250        
7777: 09         ADD     HL,BC           
7778: 77         LD      (HL),A          
7779: 18 0E      JR      $7789           
777B: CD 91 08   CALL    $0891           
777E: 20 06      JR      NZ,$7786        
7780: 36 18      LD      (HL),$18        
7782: CD 8D 3B   CALL    $3B8D           
7785: 70         LD      (HL),B          
7786: CD FD 77   CALL    $77FD           
7789: 21 50 C3   LD      HL,$C350        
778C: 09         ADD     HL,BC           
778D: 36 80      LD      (HL),$80        
778F: 21 30 C4   LD      HL,$C430        
7792: 09         ADD     HL,BC           
7793: 36 48      LD      (HL),$48        
7795: CD 35 7D   CALL    $7D35           
7798: C6 06      ADD     $06             
779A: FE 0A      CP      $0A             
779C: 38 09      JR      C,$77A7         
779E: CD 45 7D   CALL    $7D45           
77A1: C6 06      ADD     $06             
77A3: FE 0A      CP      $0A             
77A5: 30 10      JR      NC,$77B7        
77A7: CD 55 7D   CALL    $7D55           
77AA: 21 80 C3   LD      HL,$C380        
77AD: 09         ADD     HL,BC           
77AE: 73         LD      (HL),E          
77AF: CD 8D 3B   CALL    $3B8D           
77B2: CD 91 08   CALL    $0891           
77B5: 36 FF      LD      (HL),$FF        
77B7: C9         RET                     
77B8: 18 E8      JR      $77A2           
77BA: 00         NOP                     
77BB: 00         NOP                     
77BC: 00         NOP                     
77BD: 00         NOP                     
77BE: E8 18      ADD     SP,$18          
77C0: CD 91 08   CALL    $0891           
77C3: 28 34      JR      Z,$77F9         
77C5: 21 80 C3   LD      HL,$C380        
77C8: 09         ADD     HL,BC           
77C9: 5E         LD      E,(HL)          
77CA: 50         LD      D,B             
77CB: 21 B8 77   LD      HL,$77B8        
77CE: 19         ADD     HL,DE           
77CF: 7E         LD      A,(HL)          
77D0: 21 40 C2   LD      HL,$C240        
77D3: 09         ADD     HL,BC           
77D4: 96         SUB     (HL)            
77D5: 28 07      JR      Z,$77DE         
77D7: E6 80      AND     $80             
77D9: 20 02      JR      NZ,$77DD        
77DB: 34         INC     (HL)            
77DC: 34         INC     (HL)            
77DD: 35         DEC     (HL)            
77DE: 21 BC 77   LD      HL,$77BC        
77E1: 19         ADD     HL,DE           
77E2: 7E         LD      A,(HL)          
77E3: 21 50 C2   LD      HL,$C250        
77E6: 09         ADD     HL,BC           
77E7: 96         SUB     (HL)            
77E8: 28 07      JR      Z,$77F1         
77EA: E6 80      AND     $80             
77EC: 20 02      JR      NZ,$77F0        
77EE: 34         INC     (HL)            
77EF: 34         INC     (HL)            
77F0: 35         DEC     (HL)            
77F1: 21 A0 C2   LD      HL,$C2A0        
77F4: 09         ADD     HL,BC           
77F5: 7E         LD      A,(HL)          
77F6: A7         AND     A               
77F7: 28 04      JR      Z,$77FD         
77F9: CD 8D 3B   CALL    $3B8D           
77FC: 70         LD      (HL),B          
77FD: F0 E7      LD      A,($E7)         
77FF: 1F         RRA                     
7800: 1F         RRA                     
7801: 1F         RRA                     
7802: 1F         RRA                     
7803: E6 01      AND     $01             
7805: CD 87 3B   CALL    $3B87           
7808: C9         RET                     
7809: 21 30 C4   LD      HL,$C430        
780C: 09         ADD     HL,BC           
780D: 36 08      LD      (HL),$08        
780F: 21 50 C3   LD      HL,$C350        
7812: 09         ADD     HL,BC           
7813: 36 00      LD      (HL),$00        
7815: F0 E7      LD      A,($E7)         
7817: 1F         RRA                     
7818: 1F         RRA                     
7819: 1F         RRA                     
781A: 1F         RRA                     
781B: E6 01      AND     $01             
781D: 3C         INC     A               
781E: 3C         INC     A               
781F: CD 87 3B   CALL    $3B87           
7822: CD 91 08   CALL    $0891           
7825: 20 10      JR      NZ,$7837        
7827: CD 8D 3B   CALL    $3B8D           
782A: 70         LD      (HL),B          
782B: 21 20 C3   LD      HL,$C320        
782E: 09         ADD     HL,BC           
782F: 36 18      LD      (HL),$18        
7831: 21 40 C2   LD      HL,$C240        
7834: 09         ADD     HL,BC           
7835: 70         LD      (HL),B          
7836: C9         RET                     
7837: FE 60      CP      $60             
7839: 30 0D      JR      NC,$7848        
783B: E6 04      AND     $04             
783D: 3E 08      LD      A,$08           
783F: 20 02      JR      NZ,$7843        
7841: 3E F8      LD      A,$F8           
7843: 21 40 C2   LD      HL,$C240        
7846: 09         ADD     HL,BC           
7847: 77         LD      (HL),A          
7848: 21 10 C4   LD      HL,$C410        
784B: 09         ADD     HL,BC           
784C: 7E         LD      A,(HL)          
784D: F5         PUSH    AF              
784E: 36 01      LD      (HL),$01        
7850: CD 9E 3B   CALL    $3B9E           
7853: F1         POP     AF              
7854: 21 10 C4   LD      HL,$C410        
7857: 09         ADD     HL,BC           
7858: 77         LD      (HL),A          
7859: C9         RET                     
785A: 06 04      LD      B,$04           
785C: 02         LD      (BC),A          
785D: 00         NOP                     
785E: F0 F7      LD      A,($F7)         
7860: FE 15      CP      $15             
7862: 20 08      JR      NZ,$786C        
7864: FA 56 DB   LD      A,($DB56)       
7867: FE 80      CP      $80             
7869: C2 7C 7D   JP      NZ,$7D7C        
786C: CD D5 79   CALL    $79D5           
786F: CD 76 7C   CALL    $7C76           
7872: F0 F7      LD      A,($F7)         
7874: FE 15      CP      $15             
7876: 28 08      JR      Z,$7880         
7878: 21 10 C4   LD      HL,$C410        
787B: 09         ADD     HL,BC           
787C: 7E         LD      A,(HL)          
787D: A7         AND     A               
787E: 28 03      JR      Z,$7883         
7880: CD 75 79   CALL    $7975           
7883: CD 98 7C   CALL    $7C98           
7886: CD E0 3B   CALL    $3BE0           
7889: CD B4 3B   CALL    $3BB4           
788C: F0 F0      LD      A,($F0)         
788E: C7         RST     0X00            
788F: 9D         SBC     L               
7890: 78         LD      A,B             
7891: D2 78 F5   JP      NC,$F578        
7894: 78         LD      A,B             
7895: 06 FA      LD      B,$FA           
7897: 00         NOP                     
7898: 00         NOP                     
7899: 00         NOP                     
789A: 00         NOP                     
789B: FA 06 CD   LD      A,($CD06)       
789E: 9E         SBC     (HL)            
789F: 3B         DEC     SP              
78A0: 21 D0 C3   LD      HL,$C3D0        
78A3: 09         ADD     HL,BC           
78A4: 36 00      LD      (HL),$00        
78A6: CD 4D 79   CALL    $794D           
78A9: CD 91 08   CALL    $0891           
78AC: 20 23      JR      NZ,$78D1        
78AE: 36 80      LD      (HL),$80        
78B0: CD 8D 3B   CALL    $3B8D           
78B3: 21 80 C3   LD      HL,$C380        
78B6: 09         ADD     HL,BC           
78B7: 7E         LD      A,(HL)          
78B8: EE 01      XOR     $01             
78BA: 77         LD      (HL),A          
78BB: 5F         LD      E,A             
78BC: 50         LD      D,B             
78BD: 21 95 78   LD      HL,$7895        
78C0: 19         ADD     HL,DE           
78C1: 7E         LD      A,(HL)          
78C2: 21 40 C2   LD      HL,$C240        
78C5: 09         ADD     HL,BC           
78C6: 77         LD      (HL),A          
78C7: 21 99 78   LD      HL,$7899        
78CA: 19         ADD     HL,DE           
78CB: 7E         LD      A,(HL)          
78CC: 21 50 C2   LD      HL,$C250        
78CF: 09         ADD     HL,BC           
78D0: 77         LD      (HL),A          
78D1: C9         RET                     
78D2: CD 4D 79   CALL    $794D           
78D5: 21 A0 C2   LD      HL,$C2A0        
78D8: 09         ADD     HL,BC           
78D9: 7E         LD      A,(HL)          
78DA: A7         AND     A               
78DB: 28 03      JR      Z,$78E0         
78DD: CD B3 78   CALL    $78B3           
78E0: CD E2 7C   CALL    $7CE2           
78E3: CD 9E 3B   CALL    $3B9E           
78E6: CD FA 7B   CALL    $7BFA           
78E9: CD 91 08   CALL    $0891           
78EC: 20 06      JR      NZ,$78F4        
78EE: 36 30      LD      (HL),$30        
78F0: CD 8D 3B   CALL    $3B8D           
78F3: 70         LD      (HL),B          
78F4: C9         RET                     
78F5: CD 8C 08   CALL    $088C           
78F8: 28 1D      JR      Z,$7917         
78FA: FA 6B C1   LD      A,($C16B)       
78FD: FE 04      CP      $04             
78FF: 20 16      JR      NZ,$7917        
7901: F0 F7      LD      A,($F7)         
7903: FE 15      CP      $15             
7905: 20 10      JR      NZ,$7917        
7907: 21 D0 C2   LD      HL,$C2D0        
790A: 09         ADD     HL,BC           
790B: 7E         LD      A,(HL)          
790C: A7         AND     A               
790D: 20 2E      JR      NZ,$793D        
790F: 34         INC     (HL)            
7910: 3E 90      LD      A,$90           
7912: CD 85 21   CALL    $2185           
7915: 18 26      JR      $793D           
7917: 7E         LD      A,(HL)          
7918: A7         AND     A               
7919: 20 22      JR      NZ,$793D        
791B: CD 91 08   CALL    $0891           
791E: 20 05      JR      NZ,$7925        
7920: 36 18      LD      (HL),$18        
7922: CD F0 78   CALL    $78F0           
7925: CD FA 7B   CALL    $7BFA           
7928: CD FA 7B   CALL    $7BFA           
792B: CD E2 7C   CALL    $7CE2           
792E: CD 9E 3B   CALL    $3B9E           
7931: F0 E7      LD      A,($E7)         
7933: A9         XOR     C               
7934: E6 0F      AND     $0F             
7936: 20 10      JR      NZ,$7948        
7938: 3E 0A      LD      A,$0A           
793A: CD 25 3C   CALL    $3C25           
793D: CD 55 7D   CALL    $7D55           
7940: 21 80 C3   LD      HL,$C380        
7943: 09         ADD     HL,BC           
7944: 77         LD      (HL),A          
7945: CD FA 7B   CALL    $7BFA           
7948: C9         RET                     
7949: 01 00 03   LD      BC,$0300        
794C: 02         LD      (BC),A          
794D: FA 02 C5   LD      A,($C502)       
7950: A7         AND     A               
7951: 20 22      JR      NZ,$7975        
7953: CD 35 7D   CALL    $7D35           
7956: C6 30      ADD     $30             
7958: FE 60      CP      $60             
795A: 30 30      JR      NC,$798C        
795C: CD 45 7D   CALL    $7D45           
795F: C6 30      ADD     $30             
7961: FE 60      CP      $60             
7963: 30 27      JR      NC,$798C        
7965: CD 55 7D   CALL    $7D55           
7968: 50         LD      D,B             
7969: 21 49 79   LD      HL,$7949        
796C: 19         ADD     HL,DE           
796D: 7E         LD      A,(HL)          
796E: 21 80 C3   LD      HL,$C380        
7971: 09         ADD     HL,BC           
7972: BE         CP      (HL)            
7973: 28 17      JR      Z,$798C         
7975: 21 90 C2   LD      HL,$C290        
7978: 09         ADD     HL,BC           
7979: 7E         LD      A,(HL)          
797A: FE 02      CP      $02             
797C: 28 07      JR      Z,$7985         
797E: E5         PUSH    HL              
797F: CD 8C 08   CALL    $088C           
7982: 36 10      LD      (HL),$10        
7984: E1         POP     HL              
7985: 36 02      LD      (HL),$02        
7987: CD 91 08   CALL    $0891           
798A: 36 80      LD      (HL),$80        
798C: C9         RET                     
798D: 00         NOP                     
798E: 00         NOP                     
798F: F9         LD      SP,HL           
7990: F9         LD      SP,HL           
7991: F8 F2      LDHL    SP,$F2          
7993: 08 0E 08   LD      ($080E),SP      
7996: 0E F8      LD      C,$F8           
7998: F2         ???                     
7999: 00         NOP                     
799A: 00         NOP                     
799B: 00         NOP                     
799C: 00         NOP                     
799D: 02         LD      (BC),A          
799E: 02         LD      (BC),A          
799F: 06 06      LD      B,$06           
79A1: 04         INC     B               
79A2: 04         INC     B               
79A3: 00         NOP                     
79A4: 00         NOP                     
79A5: 0C         INC     C               
79A6: 0C         INC     C               
79A7: 04         INC     B               
79A8: 04         INC     B               
79A9: FC         ???                     
79AA: FC         ???                     
79AB: 14         INC     D               
79AC: 14         INC     D               
79AD: 14         INC     D               
79AE: 14         INC     D               
79AF: FC         ???                     
79B0: FC         ???                     
79B1: 0C         INC     C               
79B2: 0C         INC     C               
79B3: 0C         INC     C               
79B4: 0C         INC     C               
79B5: 60         LD      H,B             
79B6: 00         NOP                     
79B7: 62         LD      H,D             
79B8: 00         NOP                     
79B9: 62         LD      H,D             
79BA: 20 60      JR      NZ,$7A1C        
79BC: 20 64      JR      NZ,$7A22        
79BE: 00         NOP                     
79BF: 66         LD      H,(HL)          
79C0: 00         NOP                     
79C1: 66         LD      H,(HL)          
79C2: 20 64      JR      NZ,$7A28        
79C4: 20 68      JR      NZ,$7A2E        
79C6: 00         NOP                     
79C7: 6A         LD      L,D             
79C8: 00         NOP                     
79C9: 6C         LD      L,H             
79CA: 00         NOP                     
79CB: 6E         LD      L,(HL)          
79CC: 00         NOP                     
79CD: 6A         LD      L,D             
79CE: 20 68      JR      NZ,$7A38        
79D0: 20 6E      JR      NZ,$7A40        
79D2: 20 6C      JR      NZ,$7A40        
79D4: 20 CD      JR      NZ,$79A3        
79D6: 87         ADD     A,A             
79D7: 3D         DEC     A               
79D8: F0 F1      LD      A,($F1)         
79DA: FE 02      CP      $02             
79DC: 30 03      JR      NC,$79E1        
79DE: CD 39 7A   CALL    $7A39           
79E1: C5         PUSH    BC              
79E2: F0 EC      LD      A,($EC)         
79E4: E0 D7      LDFF00  ($D7),A         
79E6: F0 EE      LD      A,($EE)         
79E8: E0 D8      LDFF00  ($D8),A         
79EA: F0 F1      LD      A,($F1)         
79EC: 5F         LD      E,A             
79ED: 50         LD      D,B             
79EE: 21 A5 79   LD      HL,$79A5        
79F1: 19         ADD     HL,DE           
79F2: 7E         LD      A,(HL)          
79F3: EA C0 D5   LD      ($D5C0),A       
79F6: 21 AD 79   LD      HL,$79AD        
79F9: 19         ADD     HL,DE           
79FA: 7E         LD      A,(HL)          
79FB: EA C2 D5   LD      ($D5C2),A       
79FE: 3E 02      LD      A,$02           
7A00: EA C1 D5   LD      ($D5C1),A       
7A03: EA C3 D5   LD      ($D5C3),A       
7A06: 21 9D 79   LD      HL,$799D        
7A09: 19         ADD     HL,DE           
7A0A: 7E         LD      A,(HL)          
7A0B: E0 D9      LDFF00  ($D9),A         
7A0D: 21 95 79   LD      HL,$7995        
7A10: 19         ADD     HL,DE           
7A11: 7E         LD      A,(HL)          
7A12: 21 8D 79   LD      HL,$798D        
7A15: 19         ADD     HL,DE           
7A16: 6E         LD      L,(HL)          
7A17: 67         LD      H,A             
7A18: E5         PUSH    HL              
7A19: FA C0 C3   LD      A,($C3C0)       
7A1C: 5F         LD      E,A             
7A1D: 16 00      LD      D,$00           
7A1F: 21 30 C0   LD      HL,$C030        
7A22: 19         ADD     HL,DE           
7A23: E5         PUSH    HL              
7A24: C1         POP     BC              
7A25: AF         XOR     A               
7A26: E0 DA      LDFF00  ($DA),A         
7A28: E1         POP     HL              
7A29: CD 40 15   CALL    $1540           
7A2C: C1         POP     BC              
7A2D: 3E 02      LD      A,$02           
7A2F: CD D0 3D   CALL    $3DD0           
7A32: 11 B5 79   LD      DE,$79B5        
7A35: CD 3B 3C   CALL    $3C3B           
7A38: C9         RET                     
7A39: EE 01      XOR     $01             
7A3B: F5         PUSH    AF              
7A3C: FA C0 C3   LD      A,($C3C0)       
7A3F: 6F         LD      L,A             
7A40: 26 00      LD      H,$00           
7A42: 11 30 C0   LD      DE,$C030        
7A45: 19         ADD     HL,DE           
7A46: D1         POP     DE              
7A47: F0 EC      LD      A,($EC)         
7A49: 82         ADD     A,D             
7A4A: C6 04      ADD     $04             
7A4C: 22         LD      (HLI),A         
7A4D: F0 EE      LD      A,($EE)         
7A4F: C6 FE      ADD     $FE             
7A51: 22         LD      (HLI),A         
7A52: 3E 86      LD      A,$86           
7A54: 22         LD      (HLI),A         
7A55: 36 10      LD      (HL),$10        
7A57: 3E 01      LD      A,$01           
7A59: CD D0 3D   CALL    $3DD0           
7A5C: C9         RET                     
7A5D: 82         ADD     A,D             
7A5E: 10 86      STOP    $86             
7A60: 10 88      STOP    $88             
7A62: 10 8A      STOP    $8A             
7A64: 10 8C      STOP    $8C             
7A66: 10 98      STOP    $98             
7A68: 10 90      STOP    $90             
7A6A: 10 92      STOP    $92             
7A6C: 10 96      STOP    $96             
7A6E: 10 8E      STOP    $8E             
7A70: 10 80      STOP    $80             
7A72: 10 84      STOP    $84             
7A74: 10 94      STOP    $94             
7A76: 10 9A      STOP    $9A             
7A78: 10 AE      STOP    $AE             
7A7A: 10 9C      STOP    $9C             
7A7C: 10 A0      STOP    $A0             
7A7E: 10 C0      STOP    $C0             
7A80: 10 C2      STOP    $C2             
7A82: 10 C4      STOP    $C4             
7A84: 10 C6      STOP    $C6             
7A86: 10 CA      STOP    $CA             
7A88: 10 C0      STOP    $C0             
7A8A: 10 C2      STOP    $C2             
7A8C: 10 C4      STOP    $C4             
7A8E: 10 C6      STOP    $C6             
7A90: 10 CA      STOP    $CA             
7A92: 10 A6      STOP    $A6             
7A94: 10 A6      STOP    $A6             
7A96: 10 A6      STOP    $A6             
7A98: 10 A6      STOP    $A6             
7A9A: 10 A6      STOP    $A6             
7A9C: 10 9E      STOP    $9E             
7A9E: 10 90      STOP    $90             
7AA0: 91         SUB     C               
7AA1: 92         SUB     D               
7AA2: 93         SUB     E               
7AA3: 94         SUB     H               
7AA4: 95         SUB     L               
7AA5: 96         SUB     (HL)            
7AA6: 97         SUB     A               
7AA7: 98         SBC     B               
7AA8: 99         SBC     C               
7AA9: 9A         SBC     D               
7AAA: 9B         SBC     E               
7AAB: 9C         SBC     H               
7AAC: 9D         SBC     L               
7AAD: 9E         SBC     (HL)            
7AAE: 9F         SBC     A               
7AAF: A0         AND     B               
7AB0: A1         AND     C               
7AB1: A2         AND     D               
7AB2: A3         AND     E               
7AB3: A4         AND     H               
7AB4: A5         AND     L               
7AB5: A6         AND     (HL)            
7AB6: A7         AND     A               
7AB7: A8         XOR     B               
7AB8: A9         XOR     C               
7AB9: AA         XOR     D               
7ABA: AC         XOR     H               
7ABB: AB         XOR     E               
7ABC: AD         XOR     L               
7ABD: AE         XOR     (HL)            
7ABE: AE         XOR     (HL)            
7ABF: EF         RST     0X28            
7AC0: 06 10      LD      B,$10           
7AC2: 10 10      STOP    $10             
7AC4: 10 10      STOP    $10             
7AC6: 10 10      STOP    $10             
7AC8: 10 10      STOP    $10             
7ACA: 01 01 10   LD      BC,$1001        
7ACD: 10 10      STOP    $10             
7ACF: 10 10      STOP    $10             
7AD1: 01 10 10   LD      BC,$1010        
7AD4: 10 10      STOP    $10             
7AD6: 10 01      STOP    $01             
7AD8: 01 01 01   LD      BC,$0101        
7ADB: 01 01 01   LD      BC,$0101        
7ADE: 01 01 01   LD      BC,$0101        
7AE1: 01 00 3E   LD      BC,$3E00        
7AE4: 02         LD      (BC),A          
7AE5: E0 A1      LDFF00  ($A1),A         
7AE7: AF         XOR     A               
7AE8: EA 37 C1   LD      ($C137),A       
7AEB: EA 6A C1   LD      ($C16A),A       
7AEE: F0 F1      LD      A,($F1)         
7AF0: FE 22      CP      $22             
7AF2: 20 3B      JR      NZ,$7B2F        
7AF4: 3E 1B      LD      A,$1B           
7AF6: CD 01 3C   CALL    $3C01           
7AF9: DA 7C 7D   JP      C,$7D7C         
7AFC: F0 D7      LD      A,($D7)         
7AFE: 21 00 C2   LD      HL,$C200        
7B01: 19         ADD     HL,DE           
7B02: 77         LD      (HL),A          
7B03: F0 D8      LD      A,($D8)         
7B05: 21 10 C2   LD      HL,$C210        
7B08: 19         ADD     HL,DE           
7B09: 77         LD      (HL),A          
7B0A: 21 20 C3   LD      HL,$C320        
7B0D: 19         ADD     HL,DE           
7B0E: 36 18      LD      (HL),$18        
7B10: 21 10 C3   LD      HL,$C310        
7B13: 19         ADD     HL,DE           
7B14: 36 06      LD      (HL),$06        
7B16: 21 F0 C2   LD      HL,$C2F0        
7B19: 19         ADD     HL,DE           
7B1A: 36 50      LD      (HL),$50        
7B1C: 21 40 C2   LD      HL,$C240        
7B1F: 19         ADD     HL,DE           
7B20: 36 08      LD      (HL),$08        
7B22: 21 90 C2   LD      HL,$C290        
7B25: 19         ADD     HL,DE           
7B26: 36 03      LD      (HL),$03        
7B28: 3E 1D      LD      A,$1D           
7B2A: E0 F2      LDFF00  ($F2),A         
7B2C: C3 7C 7D   JP      $7D7C           
7B2F: FE 21      CP      $21             
7B31: 28 06      JR      Z,$7B39         
7B33: 11 5D 7A   LD      DE,$7A5D        
7B36: CD D0 3C   CALL    $3CD0           
7B39: FA 9F C1   LD      A,($C19F)       
7B3C: A7         AND     A               
7B3D: C2 CF 7B   JP      NZ,$7BCF        
7B40: CD E2 7C   CALL    $7CE2           
7B43: 21 D0 C3   LD      HL,$C3D0        
7B46: 09         ADD     HL,BC           
7B47: 7E         LD      A,(HL)          
7B48: 3C         INC     A               
7B49: 77         LD      (HL),A          
7B4A: FE 10      CP      $10             
7B4C: 20 06      JR      NZ,$7B54        
7B4E: 21 50 C2   LD      HL,$C250        
7B51: 09         ADD     HL,BC           
7B52: 36 00      LD      (HL),$00        
7B54: FE 08      CP      $08             
7B56: 20 19      JR      NZ,$7B71        
7B58: F0 F1      LD      A,($F1)         
7B5A: 5F         LD      E,A             
7B5B: 50         LD      D,B             
7B5C: 21 C1 7A   LD      HL,$7AC1        
7B5F: 19         ADD     HL,DE           
7B60: 7E         LD      A,(HL)          
7B61: A7         AND     A               
7B62: 28 0D      JR      Z,$7B71         
7B64: FE 01      CP      $01             
7B66: 20 06      JR      NZ,$7B6E        
7B68: 3E 01      LD      A,$01           
7B6A: E0 F2      LDFF00  ($F2),A         
7B6C: 18 03      JR      $7B71           
7B6E: EA 68 D3   LD      ($D368),A       
7B71: 21 D0 C3   LD      HL,$C3D0        
7B74: 09         ADD     HL,BC           
7B75: 7E         LD      A,(HL)          
7B76: FE 26      CP      $26             
7B78: 20 4E      JR      NZ,$7BC8        
7B7A: F0 F1      LD      A,($F1)         
7B7C: 5F         LD      E,A             
7B7D: 50         LD      D,B             
7B7E: FE 21      CP      $21             
7B80: 20 0D      JR      NZ,$7B8F        
7B82: F0 F6      LD      A,($F6)         
7B84: FE 96      CP      $96             
7B86: 20 07      JR      NZ,$7B8F        
7B88: 3E 11      LD      A,$11           
7B8A: CD 85 21   CALL    $2185           
7B8D: 18 38      JR      $7BC7           
7B8F: 7B         LD      A,E             
7B90: FE 01      CP      $01             
7B92: 20 0B      JR      NZ,$7B9F        
7B94: FA 44 DB   LD      A,($DB44)       
7B97: FE 02      CP      $02             
7B99: 20 04      JR      NZ,$7B9F        
7B9B: 3E ED      LD      A,$ED           
7B9D: 18 25      JR      $7BC4           
7B9F: 7B         LD      A,E             
7BA0: FE 0B      CP      $0B             
7BA2: 20 0B      JR      NZ,$7BAF        
7BA4: FA 4E DB   LD      A,($DB4E)       
7BA7: FE 02      CP      $02             
7BA9: 20 04      JR      NZ,$7BAF        
7BAB: 3E 9F      LD      A,$9F           
7BAD: 18 15      JR      $7BC4           
7BAF: 7B         LD      A,E             
7BB0: FE 00      CP      $00             
7BB2: 20 0B      JR      NZ,$7BBF        
7BB4: FA 43 DB   LD      A,($DB43)       
7BB7: FE 02      CP      $02             
7BB9: 20 04      JR      NZ,$7BBF        
7BBB: 3E EE      LD      A,$EE           
7BBD: 18 05      JR      $7BC4           
7BBF: 21 9F 7A   LD      HL,$7A9F        
7BC2: 19         ADD     HL,DE           
7BC3: 7E         LD      A,(HL)          
7BC4: CD 97 21   CALL    $2197           
7BC7: AF         XOR     A               
7BC8: FE 28      CP      $28             
7BCA: 20 03      JR      NZ,$7BCF        
7BCC: CD 7C 7D   CALL    $7D7C           
7BCF: C9         RET                     
7BD0: CD D5 3B   CALL    $3BD5           
7BD3: 30 1F      JR      NC,$7BF4        
7BD5: CD 4A 09   CALL    $094A           
7BD8: CD 42 09   CALL    $0942           
7BDB: FA A6 C1   LD      A,($C1A6)       
7BDE: A7         AND     A               
7BDF: 28 11      JR      Z,$7BF2         
7BE1: 5F         LD      E,A             
7BE2: 50         LD      D,B             
7BE3: 21 9F C3   LD      HL,$C39F        
7BE6: 19         ADD     HL,DE           
7BE7: 7E         LD      A,(HL)          
7BE8: FE 03      CP      $03             
7BEA: 20 06      JR      NZ,$7BF2        
7BEC: 21 8F C2   LD      HL,$C28F        
7BEF: 19         ADD     HL,DE           
7BF0: 36 00      LD      (HL),$00        
7BF2: 37         SCF                     
7BF3: C9         RET                     
7BF4: A7         AND     A               
7BF5: C9         RET                     
7BF6: 06 04      LD      B,$04           
7BF8: 02         LD      (BC),A          
7BF9: 00         NOP                     
7BFA: 21 80 C3   LD      HL,$C380        
7BFD: 09         ADD     HL,BC           
7BFE: 5E         LD      E,(HL)          
7BFF: 50         LD      D,B             
7C00: 21 F6 7B   LD      HL,$7BF6        
7C03: 19         ADD     HL,DE           
7C04: E5         PUSH    HL              
7C05: 21 D0 C3   LD      HL,$C3D0        
7C08: 09         ADD     HL,BC           
7C09: 34         INC     (HL)            
7C0A: 7E         LD      A,(HL)          
7C0B: 1F         RRA                     
7C0C: 1F         RRA                     
7C0D: 1F         RRA                     
7C0E: 1F         RRA                     
7C0F: E1         POP     HL              
7C10: E6 01      AND     $01             
7C12: B6         OR      (HL)            
7C13: C3 87 3B   JP      $3B87           
7C16: 58         LD      E,B             
7C17: F0 99      LD      A,($99)         
7C19: 21 EF FF   LD      HL,$FFEF        
7C1C: 96         SUB     (HL)            
7C1D: C6 14      ADD     $14             
7C1F: FE 38      CP      $38             
7C21: 18 0B      JR      $7C2E           
7C23: 58         LD      E,B             
7C24: F0 99      LD      A,($99)         
7C26: 21 EF FF   LD      HL,$FFEF        
7C29: 96         SUB     (HL)            
7C2A: C6 14      ADD     $14             
7C2C: FE 28      CP      $28             
7C2E: 30 44      JR      NC,$7C74        
7C30: F0 98      LD      A,($98)         
7C32: 21 EE FF   LD      HL,$FFEE        
7C35: 96         SUB     (HL)            
7C36: C6 10      ADD     $10             
7C38: FE 20      CP      $20             
7C3A: 30 38      JR      NC,$7C74        
7C3C: 1C         INC     E               
7C3D: F0 EB      LD      A,($EB)         
7C3F: FE B5      CP      $B5             
7C41: 28 0C      JR      Z,$7C4F         
7C43: D5         PUSH    DE              
7C44: CD 55 7D   CALL    $7D55           
7C47: F0 9E      LD      A,($9E)         
7C49: EE 01      XOR     $01             
7C4B: BB         CP      E               
7C4C: D1         POP     DE              
7C4D: 20 25      JR      NZ,$7C74        
7C4F: 21 AD C1   LD      HL,$C1AD        
7C52: 36 01      LD      (HL),$01        
7C54: FA 9F C1   LD      A,($C19F)       
7C57: 21 4F C1   LD      HL,$C14F        
7C5A: B6         OR      (HL)            
7C5B: 21 46 C1   LD      HL,$C146        
7C5E: B6         OR      (HL)            
7C5F: 21 34 C1   LD      HL,$C134        
7C62: B6         OR      (HL)            
7C63: 20 0F      JR      NZ,$7C74        
7C65: FA 9A DB   LD      A,($DB9A)       
7C68: FE 80      CP      $80             
7C6A: 20 08      JR      NZ,$7C74        
7C6C: F0 CC      LD      A,($CC)         
7C6E: E6 10      AND     $10             
7C70: 28 02      JR      Z,$7C74         
7C72: 37         SCF                     
7C73: C9         RET                     
7C74: A7         AND     A               
7C75: C9         RET                     
7C76: F0 EA      LD      A,($EA)         
7C78: FE 05      CP      $05             
7C7A: 20 1A      JR      NZ,$7C96        
7C7C: FA 95 DB   LD      A,($DB95)       
7C7F: FE 07      CP      $07             
7C81: 28 13      JR      Z,$7C96         
7C83: FA 9F C1   LD      A,($C19F)       
7C86: 21 A8 C1   LD      HL,$C1A8        
7C89: B6         OR      (HL)            
7C8A: 21 4F C1   LD      HL,$C14F        
7C8D: B6         OR      (HL)            
7C8E: 20 06      JR      NZ,$7C96        
7C90: FA 24 C1   LD      A,($C124)       
7C93: A7         AND     A               
7C94: 28 01      JR      Z,$7C97         
7C96: F1         POP     AF              
7C97: C9         RET                     
7C98: 21 10 C4   LD      HL,$C410        
7C9B: 09         ADD     HL,BC           
7C9C: 7E         LD      A,(HL)          
7C9D: A7         AND     A               
7C9E: 28 41      JR      Z,$7CE1         
7CA0: 3D         DEC     A               
7CA1: 77         LD      (HL),A          
7CA2: CD B8 3E   CALL    $3EB8           
7CA5: 21 40 C2   LD      HL,$C240        
7CA8: 09         ADD     HL,BC           
7CA9: 7E         LD      A,(HL)          
7CAA: F5         PUSH    AF              
7CAB: 21 50 C2   LD      HL,$C250        
7CAE: 09         ADD     HL,BC           
7CAF: 7E         LD      A,(HL)          
7CB0: F5         PUSH    AF              
7CB1: 21 F0 C3   LD      HL,$C3F0        
7CB4: 09         ADD     HL,BC           
7CB5: 7E         LD      A,(HL)          
7CB6: 21 40 C2   LD      HL,$C240        
7CB9: 09         ADD     HL,BC           
7CBA: 77         LD      (HL),A          
7CBB: 21 00 C4   LD      HL,$C400        
7CBE: 09         ADD     HL,BC           
7CBF: 7E         LD      A,(HL)          
7CC0: 21 50 C2   LD      HL,$C250        
7CC3: 09         ADD     HL,BC           
7CC4: 77         LD      (HL),A          
7CC5: CD E2 7C   CALL    $7CE2           
7CC8: 21 30 C4   LD      HL,$C430        
7CCB: 09         ADD     HL,BC           
7CCC: 7E         LD      A,(HL)          
7CCD: E6 20      AND     $20             
7CCF: 20 03      JR      NZ,$7CD4        
7CD1: CD 9E 3B   CALL    $3B9E           
7CD4: 21 50 C2   LD      HL,$C250        
7CD7: 09         ADD     HL,BC           
7CD8: F1         POP     AF              
7CD9: 77         LD      (HL),A          
7CDA: 21 40 C2   LD      HL,$C240        
7CDD: 09         ADD     HL,BC           
7CDE: F1         POP     AF              
7CDF: 77         LD      (HL),A          
7CE0: F1         POP     AF              
7CE1: C9         RET                     
7CE2: CD EF 7C   CALL    $7CEF           
7CE5: C5         PUSH    BC              
7CE6: 79         LD      A,C             
7CE7: C6 10      ADD     $10             
7CE9: 4F         LD      C,A             
7CEA: CD EF 7C   CALL    $7CEF           
7CED: C1         POP     BC              
7CEE: C9         RET                     
7CEF: 21 40 C2   LD      HL,$C240        
7CF2: 09         ADD     HL,BC           
7CF3: 7E         LD      A,(HL)          
7CF4: A7         AND     A               
7CF5: 28 23      JR      Z,$7D1A         
7CF7: F5         PUSH    AF              
7CF8: CB 37      SET     1,E             
7CFA: E6 F0      AND     $F0             
7CFC: 21 60 C2   LD      HL,$C260        
7CFF: 09         ADD     HL,BC           
7D00: 86         ADD     A,(HL)          
7D01: 77         LD      (HL),A          
7D02: CB 12      SET     1,E             
7D04: 21 00 C2   LD      HL,$C200        
7D07: 09         ADD     HL,BC           
7D08: F1         POP     AF              
7D09: 1E 00      LD      E,$00           
7D0B: CB 7F      SET     1,E             
7D0D: 28 02      JR      Z,$7D11         
7D0F: 1E F0      LD      E,$F0           
7D11: CB 37      SET     1,E             
7D13: E6 0F      AND     $0F             
7D15: B3         OR      E               
7D16: CB 1A      SET     1,E             
7D18: 8E         ADC     A,(HL)          
7D19: 77         LD      (HL),A          
7D1A: C9         RET                     
7D1B: 21 20 C3   LD      HL,$C320        
7D1E: 09         ADD     HL,BC           
7D1F: 7E         LD      A,(HL)          
7D20: A7         AND     A               
7D21: 28 F7      JR      Z,$7D1A         
7D23: F5         PUSH    AF              
7D24: CB 37      SET     1,E             
7D26: E6 F0      AND     $F0             
7D28: 21 30 C3   LD      HL,$C330        
7D2B: 09         ADD     HL,BC           
7D2C: 86         ADD     A,(HL)          
7D2D: 77         LD      (HL),A          
7D2E: CB 12      SET     1,E             
7D30: 21 10 C3   LD      HL,$C310        
7D33: 18 D2      JR      $7D07           
7D35: 1E 00      LD      E,$00           
7D37: F0 98      LD      A,($98)         
7D39: 21 00 C2   LD      HL,$C200        
7D3C: 09         ADD     HL,BC           
7D3D: 96         SUB     (HL)            
7D3E: CB 7F      SET     1,E             
7D40: 28 01      JR      Z,$7D43         
7D42: 1C         INC     E               
7D43: 57         LD      D,A             
7D44: C9         RET                     
7D45: 1E 02      LD      E,$02           
7D47: F0 99      LD      A,($99)         
7D49: 21 10 C2   LD      HL,$C210        
7D4C: 09         ADD     HL,BC           
7D4D: 96         SUB     (HL)            
7D4E: CB 7F      SET     1,E             
7D50: 20 01      JR      NZ,$7D53        
7D52: 1C         INC     E               
7D53: 57         LD      D,A             
7D54: C9         RET                     
7D55: CD 35 7D   CALL    $7D35           
7D58: 7B         LD      A,E             
7D59: E0 D7      LDFF00  ($D7),A         
7D5B: 7A         LD      A,D             
7D5C: CB 7F      SET     1,E             
7D5E: 28 02      JR      Z,$7D62         
7D60: 2F         CPL                     
7D61: 3C         INC     A               
7D62: F5         PUSH    AF              
7D63: CD 45 7D   CALL    $7D45           
7D66: 7B         LD      A,E             
7D67: E0 D8      LDFF00  ($D8),A         
7D69: 7A         LD      A,D             
7D6A: CB 7F      SET     1,E             
7D6C: 28 02      JR      Z,$7D70         
7D6E: 2F         CPL                     
7D6F: 3C         INC     A               
7D70: D1         POP     DE              
7D71: BA         CP      D               
7D72: 30 04      JR      NC,$7D78        
7D74: F0 D7      LD      A,($D7)         
7D76: 18 02      JR      $7D7A           
7D78: F0 D8      LD      A,($D8)         
7D7A: 5F         LD      E,A             
7D7B: C9         RET                     
7D7C: 21 80 C2   LD      HL,$C280        
7D7F: 09         ADD     HL,BC           
7D80: 70         LD      (HL),B          
7D81: C9         RET                     
7D82: 21 C0 C2   LD      HL,$C2C0        
7D85: 09         ADD     HL,BC           
7D86: 7E         LD      A,(HL)          
7D87: C7         RST     0X00            
7D88: 8E         ADC     A,(HL)          
7D89: 7D         LD      A,L             
7D8A: 9F         SBC     A               
7D8B: 7D         LD      A,L             
7D8C: B0         OR      B               
7D8D: 7D         LD      A,L             
7D8E: CD 91 08   CALL    $0891           
7D91: 36 A0      LD      (HL),$A0        
7D93: 21 20 C4   LD      HL,$C420        
7D96: 09         ADD     HL,BC           
7D97: 36 FF      LD      (HL),$FF        
7D99: 21 C0 C2   LD      HL,$C2C0        
7D9C: 09         ADD     HL,BC           
7D9D: 34         INC     (HL)            
7D9E: C9         RET                     
7D9F: CD 91 08   CALL    $0891           
7DA2: 20 0B      JR      NZ,$7DAF        
7DA4: 36 C0      LD      (HL),$C0        
7DA6: 21 20 C4   LD      HL,$C420        
7DA9: 09         ADD     HL,BC           
7DAA: 36 FF      LD      (HL),$FF        
7DAC: CD 99 7D   CALL    $7D99           
7DAF: C9         RET                     
7DB0: CD 91 08   CALL    $0891           
7DB3: 20 38      JR      NZ,$7DED        
7DB5: F0 EB      LD      A,($EB)         
7DB7: FE 5F      CP      $5F             
7DB9: 20 29      JR      NZ,$7DE4        
7DBB: 3E 30      LD      A,$30           
7DBD: CD 01 3C   CALL    $3C01           
7DC0: F0 D7      LD      A,($D7)         
7DC2: 21 00 C2   LD      HL,$C200        
7DC5: 19         ADD     HL,DE           
7DC6: 77         LD      (HL),A          
7DC7: F0 D8      LD      A,($D8)         
7DC9: 21 10 C2   LD      HL,$C210        
7DCC: 19         ADD     HL,DE           
7DCD: 77         LD      (HL),A          
7DCE: 21 20 C3   LD      HL,$C320        
7DD1: 19         ADD     HL,DE           
7DD2: 36 18      LD      (HL),$18        
7DD4: 21 F0 C2   LD      HL,$C2F0        
7DD7: 19         ADD     HL,DE           
7DD8: 36 20      LD      (HL),$20        
7DDA: 21 90 C3   LD      HL,$C390        
7DDD: 09         ADD     HL,BC           
7DDE: 7E         LD      A,(HL)          
7DDF: E0 B0      LDFF00  ($B0),A         
7DE1: C3 54 7E   JP      $7E54           
7DE4: CD D7 08   CALL    $08D7           
7DE7: CD BD 27   CALL    $27BD           
7DEA: C3 7A 3F   JP      $3F7A           
7DED: CD F1 7D   CALL    $7DF1           
7DF0: C9         RET                     
7DF1: E6 07      AND     $07             
7DF3: 20 1D      JR      NZ,$7E12        
7DF5: CD ED 27   CALL    $27ED           
7DF8: E6 1F      AND     $1F             
7DFA: D6 10      SUB     $10             
7DFC: 5F         LD      E,A             
7DFD: 21 EE FF   LD      HL,$FFEE        
7E00: 86         ADD     A,(HL)          
7E01: 77         LD      (HL),A          
7E02: CD ED 27   CALL    $27ED           
7E05: E6 1F      AND     $1F             
7E07: D6 14      SUB     $14             
7E09: 5F         LD      E,A             
7E0A: 21 EC FF   LD      HL,$FFEC        
7E0D: 86         ADD     A,(HL)          
7E0E: 77         LD      (HL),A          
7E0F: CD 13 7E   CALL    $7E13           
7E12: C9         RET                     
7E13: CD 7C 7C   CALL    $7C7C           
7E16: F0 EE      LD      A,($EE)         
7E18: E0 D7      LDFF00  ($D7),A         
7E1A: F0 EC      LD      A,($EC)         
7E1C: E0 D8      LDFF00  ($D8),A         
7E1E: 3E 02      LD      A,$02           
7E20: CD 53 09   CALL    $0953           
7E23: 3E 13      LD      A,$13           
7E25: E0 F4      LDFF00  ($F4),A         
7E27: C9         RET                     
7E28: 3E 36      LD      A,$36           
7E2A: CD 01 3C   CALL    $3C01           
7E2D: F0 D7      LD      A,($D7)         
7E2F: 21 00 C2   LD      HL,$C200        
7E32: 19         ADD     HL,DE           
7E33: 77         LD      (HL),A          
7E34: F0 D8      LD      A,($D8)         
7E36: 21 10 C2   LD      HL,$C210        
7E39: 19         ADD     HL,DE           
7E3A: 77         LD      (HL),A          
7E3B: F0 F9      LD      A,($F9)         
7E3D: A7         AND     A               
7E3E: 28 08      JR      Z,$7E48         
7E40: 21 50 C2   LD      HL,$C250        
7E43: 09         ADD     HL,BC           
7E44: 36 F0      LD      (HL),$F0        
7E46: 18 0C      JR      $7E54           
7E48: 21 20 C3   LD      HL,$C320        
7E4B: 19         ADD     HL,DE           
7E4C: 36 10      LD      (HL),$10        
7E4E: 21 10 C3   LD      HL,$C310        
7E51: 19         ADD     HL,DE           
7E52: 36 08      LD      (HL),$08        
7E54: CD 7C 7D   CALL    $7D7C           
7E57: 21 F4 FF   LD      HL,$FFF4        
7E5A: 36 1A      LD      (HL),$1A        
7E5C: C9         RET                     
7E5D: FF         RST     0X38            
7E5E: FF         RST     0X38            
7E5F: FF         RST     0X38            
7E60: FF         RST     0X38            
7E61: FF         RST     0X38            
7E62: FF         RST     0X38            
7E63: FF         RST     0X38            
7E64: FF         RST     0X38            
7E65: FF         RST     0X38            
7E66: FF         RST     0X38            
7E67: FF         RST     0X38            
7E68: FF         RST     0X38            
7E69: FF         RST     0X38            
7E6A: FF         RST     0X38            
7E6B: FF         RST     0X38            
7E6C: FF         RST     0X38            
7E6D: FF         RST     0X38            
7E6E: FF         RST     0X38            
7E6F: FF         RST     0X38            
7E70: FF         RST     0X38            
7E71: FF         RST     0X38            
7E72: FF         RST     0X38            
7E73: FF         RST     0X38            
7E74: FF         RST     0X38            
7E75: FF         RST     0X38            
7E76: FF         RST     0X38            
7E77: FF         RST     0X38            
7E78: FF         RST     0X38            
7E79: FF         RST     0X38            
7E7A: FF         RST     0X38            
7E7B: FF         RST     0X38            
7E7C: FF         RST     0X38            
7E7D: FF         RST     0X38            
7E7E: FF         RST     0X38            
7E7F: FF         RST     0X38            
7E80: FF         RST     0X38            
7E81: FF         RST     0X38            
7E82: FF         RST     0X38            
7E83: FF         RST     0X38            
7E84: FF         RST     0X38            
7E85: FF         RST     0X38            
7E86: FF         RST     0X38            
7E87: FF         RST     0X38            
7E88: FF         RST     0X38            
7E89: FF         RST     0X38            
7E8A: FF         RST     0X38            
7E8B: FF         RST     0X38            
7E8C: FF         RST     0X38            
7E8D: FF         RST     0X38            
7E8E: FF         RST     0X38            
7E8F: FF         RST     0X38            
7E90: FF         RST     0X38            
7E91: FF         RST     0X38            
7E92: FF         RST     0X38            
7E93: FF         RST     0X38            
7E94: FF         RST     0X38            
7E95: FF         RST     0X38            
7E96: FF         RST     0X38            
7E97: FF         RST     0X38            
7E98: FF         RST     0X38            
7E99: FF         RST     0X38            
7E9A: FF         RST     0X38            
7E9B: FF         RST     0X38            
7E9C: FF         RST     0X38            
7E9D: FF         RST     0X38            
7E9E: FF         RST     0X38            
7E9F: FF         RST     0X38            
7EA0: FF         RST     0X38            
7EA1: FF         RST     0X38            
7EA2: FF         RST     0X38            
7EA3: FF         RST     0X38            
7EA4: FF         RST     0X38            
7EA5: FF         RST     0X38            
7EA6: FF         RST     0X38            
7EA7: FF         RST     0X38            
7EA8: FF         RST     0X38            
7EA9: FF         RST     0X38            
7EAA: FF         RST     0X38            
7EAB: FF         RST     0X38            
7EAC: FF         RST     0X38            
7EAD: FF         RST     0X38            
7EAE: FF         RST     0X38            
7EAF: FF         RST     0X38            
7EB0: FF         RST     0X38            
7EB1: FF         RST     0X38            
7EB2: FF         RST     0X38            
7EB3: FF         RST     0X38            
7EB4: FF         RST     0X38            
7EB5: FF         RST     0X38            
7EB6: FF         RST     0X38            
7EB7: FF         RST     0X38            
7EB8: FF         RST     0X38            
7EB9: FF         RST     0X38            
7EBA: FF         RST     0X38            
7EBB: FF         RST     0X38            
7EBC: FF         RST     0X38            
7EBD: FF         RST     0X38            
7EBE: FF         RST     0X38            
7EBF: FF         RST     0X38            
7EC0: FF         RST     0X38            
7EC1: FF         RST     0X38            
7EC2: FF         RST     0X38            
7EC3: FF         RST     0X38            
7EC4: FF         RST     0X38            
7EC5: FF         RST     0X38            
7EC6: FF         RST     0X38            
7EC7: FF         RST     0X38            
7EC8: FF         RST     0X38            
7EC9: FF         RST     0X38            
7ECA: FF         RST     0X38            
7ECB: FF         RST     0X38            
7ECC: FF         RST     0X38            
7ECD: FF         RST     0X38            
7ECE: FF         RST     0X38            
7ECF: FF         RST     0X38            
7ED0: FF         RST     0X38            
7ED1: FF         RST     0X38            
7ED2: FF         RST     0X38            
7ED3: FF         RST     0X38            
7ED4: FF         RST     0X38            
7ED5: FF         RST     0X38            
7ED6: FF         RST     0X38            
7ED7: FF         RST     0X38            
7ED8: FF         RST     0X38            
7ED9: FF         RST     0X38            
7EDA: FF         RST     0X38            
7EDB: FF         RST     0X38            
7EDC: FF         RST     0X38            
7EDD: FF         RST     0X38            
7EDE: FF         RST     0X38            
7EDF: FF         RST     0X38            
7EE0: FF         RST     0X38            
7EE1: FF         RST     0X38            
7EE2: FF         RST     0X38            
7EE3: FF         RST     0X38            
7EE4: FF         RST     0X38            
7EE5: FF         RST     0X38            
7EE6: FF         RST     0X38            
7EE7: FF         RST     0X38            
7EE8: FF         RST     0X38            
7EE9: FF         RST     0X38            
7EEA: FF         RST     0X38            
7EEB: FF         RST     0X38            
7EEC: FF         RST     0X38            
7EED: FF         RST     0X38            
7EEE: FF         RST     0X38            
7EEF: FF         RST     0X38            
7EF0: FF         RST     0X38            
7EF1: FF         RST     0X38            
7EF2: FF         RST     0X38            
7EF3: FF         RST     0X38            
7EF4: FF         RST     0X38            
7EF5: FF         RST     0X38            
7EF6: FF         RST     0X38            
7EF7: FF         RST     0X38            
7EF8: FF         RST     0X38            
7EF9: FF         RST     0X38            
7EFA: FF         RST     0X38            
7EFB: FF         RST     0X38            
7EFC: FF         RST     0X38            
7EFD: FF         RST     0X38            
7EFE: FF         RST     0X38            
7EFF: FF         RST     0X38            
7F00: FF         RST     0X38            
7F01: FF         RST     0X38            
7F02: FF         RST     0X38            
7F03: FF         RST     0X38            
7F04: FF         RST     0X38            
7F05: FF         RST     0X38            
7F06: FF         RST     0X38            
7F07: FF         RST     0X38            
7F08: FF         RST     0X38            
7F09: FF         RST     0X38            
7F0A: FF         RST     0X38            
7F0B: FF         RST     0X38            
7F0C: FF         RST     0X38            
7F0D: FF         RST     0X38            
7F0E: FF         RST     0X38            
7F0F: FF         RST     0X38            
7F10: FF         RST     0X38            
7F11: FF         RST     0X38            
7F12: FF         RST     0X38            
7F13: FF         RST     0X38            
7F14: FF         RST     0X38            
7F15: FF         RST     0X38            
7F16: FF         RST     0X38            
7F17: FF         RST     0X38            
7F18: FF         RST     0X38            
7F19: FF         RST     0X38            
7F1A: FF         RST     0X38            
7F1B: FF         RST     0X38            
7F1C: FF         RST     0X38            
7F1D: FF         RST     0X38            
7F1E: FF         RST     0X38            
7F1F: FF         RST     0X38            
7F20: FF         RST     0X38            
7F21: FF         RST     0X38            
7F22: FF         RST     0X38            
7F23: FF         RST     0X38            
7F24: FF         RST     0X38            
7F25: FF         RST     0X38            
7F26: FF         RST     0X38            
7F27: FF         RST     0X38            
7F28: FF         RST     0X38            
7F29: FF         RST     0X38            
7F2A: FF         RST     0X38            
7F2B: FF         RST     0X38            
7F2C: FF         RST     0X38            
7F2D: FF         RST     0X38            
7F2E: FF         RST     0X38            
7F2F: FF         RST     0X38            
7F30: FF         RST     0X38            
7F31: FF         RST     0X38            
7F32: FF         RST     0X38            
7F33: FF         RST     0X38            
7F34: FF         RST     0X38            
7F35: FF         RST     0X38            
7F36: FF         RST     0X38            
7F37: FF         RST     0X38            
7F38: FF         RST     0X38            
7F39: FF         RST     0X38            
7F3A: FF         RST     0X38            
7F3B: FF         RST     0X38            
7F3C: FF         RST     0X38            
7F3D: FF         RST     0X38            
7F3E: FF         RST     0X38            
7F3F: FF         RST     0X38            
7F40: FF         RST     0X38            
7F41: FF         RST     0X38            
7F42: FF         RST     0X38            
7F43: FF         RST     0X38            
7F44: FF         RST     0X38            
7F45: FF         RST     0X38            
7F46: FF         RST     0X38            
7F47: FF         RST     0X38            
7F48: FF         RST     0X38            
7F49: FF         RST     0X38            
7F4A: FF         RST     0X38            
7F4B: FF         RST     0X38            
7F4C: FF         RST     0X38            
7F4D: FF         RST     0X38            
7F4E: FF         RST     0X38            
7F4F: FF         RST     0X38            
7F50: FF         RST     0X38            
7F51: FF         RST     0X38            
7F52: FF         RST     0X38            
7F53: FF         RST     0X38            
7F54: FF         RST     0X38            
7F55: FF         RST     0X38            
7F56: FF         RST     0X38            
7F57: FF         RST     0X38            
7F58: FF         RST     0X38            
7F59: FF         RST     0X38            
7F5A: FF         RST     0X38            
7F5B: FF         RST     0X38            
7F5C: FF         RST     0X38            
7F5D: FF         RST     0X38            
7F5E: FF         RST     0X38            
7F5F: FF         RST     0X38            
7F60: FF         RST     0X38            
7F61: FF         RST     0X38            
7F62: FF         RST     0X38            
7F63: FF         RST     0X38            
7F64: FF         RST     0X38            
7F65: FF         RST     0X38            
7F66: FF         RST     0X38            
7F67: FF         RST     0X38            
7F68: FF         RST     0X38            
7F69: FF         RST     0X38            
7F6A: FF         RST     0X38            
7F6B: FF         RST     0X38            
7F6C: FF         RST     0X38            
7F6D: FF         RST     0X38            
7F6E: FF         RST     0X38            
7F6F: FF         RST     0X38            
7F70: FF         RST     0X38            
7F71: FF         RST     0X38            
7F72: FF         RST     0X38            
7F73: FF         RST     0X38            
7F74: FF         RST     0X38            
7F75: FF         RST     0X38            
7F76: FF         RST     0X38            
7F77: FF         RST     0X38            
7F78: FF         RST     0X38            
7F79: FF         RST     0X38            
7F7A: FF         RST     0X38            
7F7B: FF         RST     0X38            
7F7C: FF         RST     0X38            
7F7D: FF         RST     0X38            
7F7E: FF         RST     0X38            
7F7F: FF         RST     0X38            
7F80: FF         RST     0X38            
7F81: FF         RST     0X38            
7F82: FF         RST     0X38            
7F83: FF         RST     0X38            
7F84: FF         RST     0X38            
7F85: FF         RST     0X38            
7F86: FF         RST     0X38            
7F87: FF         RST     0X38            
7F88: FF         RST     0X38            
7F89: FF         RST     0X38            
7F8A: FF         RST     0X38            
7F8B: FF         RST     0X38            
7F8C: FF         RST     0X38            
7F8D: FF         RST     0X38            
7F8E: FF         RST     0X38            
7F8F: FF         RST     0X38            
7F90: FF         RST     0X38            
7F91: FF         RST     0X38            
7F92: FF         RST     0X38            
7F93: FF         RST     0X38            
7F94: FF         RST     0X38            
7F95: FF         RST     0X38            
7F96: FF         RST     0X38            
7F97: FF         RST     0X38            
7F98: FF         RST     0X38            
7F99: FF         RST     0X38            
7F9A: FF         RST     0X38            
7F9B: FF         RST     0X38            
7F9C: FF         RST     0X38            
7F9D: FF         RST     0X38            
7F9E: FF         RST     0X38            
7F9F: FF         RST     0X38            
7FA0: FF         RST     0X38            
7FA1: FF         RST     0X38            
7FA2: FF         RST     0X38            
7FA3: FF         RST     0X38            
7FA4: FF         RST     0X38            
7FA5: FF         RST     0X38            
7FA6: FF         RST     0X38            
7FA7: FF         RST     0X38            
7FA8: FF         RST     0X38            
7FA9: FF         RST     0X38            
7FAA: FF         RST     0X38            
7FAB: FF         RST     0X38            
7FAC: FF         RST     0X38            
7FAD: FF         RST     0X38            
7FAE: FF         RST     0X38            
7FAF: FF         RST     0X38            
7FB0: FF         RST     0X38            
7FB1: FF         RST     0X38            
7FB2: FF         RST     0X38            
7FB3: FF         RST     0X38            
7FB4: FF         RST     0X38            
7FB5: FF         RST     0X38            
7FB6: FF         RST     0X38            
7FB7: FF         RST     0X38            
7FB8: FF         RST     0X38            
7FB9: FF         RST     0X38            
7FBA: FF         RST     0X38            
7FBB: FF         RST     0X38            
7FBC: FF         RST     0X38            
7FBD: FF         RST     0X38            
7FBE: FF         RST     0X38            
7FBF: FF         RST     0X38            
7FC0: FF         RST     0X38            
7FC1: FF         RST     0X38            
7FC2: FF         RST     0X38            
7FC3: FF         RST     0X38            
7FC4: FF         RST     0X38            
7FC5: FF         RST     0X38            
7FC6: FF         RST     0X38            
7FC7: FF         RST     0X38            
7FC8: FF         RST     0X38            
7FC9: FF         RST     0X38            
7FCA: FF         RST     0X38            
7FCB: FF         RST     0X38            
7FCC: FF         RST     0X38            
7FCD: FF         RST     0X38            
7FCE: FF         RST     0X38            
7FCF: FF         RST     0X38            
7FD0: FF         RST     0X38            
7FD1: FF         RST     0X38            
7FD2: FF         RST     0X38            
7FD3: FF         RST     0X38            
7FD4: FF         RST     0X38            
7FD5: FF         RST     0X38            
7FD6: FF         RST     0X38            
7FD7: FF         RST     0X38            
7FD8: FF         RST     0X38            
7FD9: FF         RST     0X38            
7FDA: FF         RST     0X38            
7FDB: FF         RST     0X38            
7FDC: FF         RST     0X38            
7FDD: FF         RST     0X38            
7FDE: FF         RST     0X38            
7FDF: FF         RST     0X38            
7FE0: FF         RST     0X38            
7FE1: FF         RST     0X38            
7FE2: FF         RST     0X38            
7FE3: FF         RST     0X38            
7FE4: FF         RST     0X38            
7FE5: FF         RST     0X38            
7FE6: FF         RST     0X38            
7FE7: FF         RST     0X38            
7FE8: FF         RST     0X38            
7FE9: FF         RST     0X38            
7FEA: FF         RST     0X38            
7FEB: FF         RST     0X38            
7FEC: FF         RST     0X38            
7FED: FF         RST     0X38            
7FEE: FF         RST     0X38            
7FEF: FF         RST     0X38            
7FF0: FF         RST     0X38            
7FF1: FF         RST     0X38            
7FF2: FF         RST     0X38            
7FF3: FF         RST     0X38            
7FF4: FF         RST     0X38            
7FF5: FF         RST     0X38            
7FF6: FF         RST     0X38            
7FF7: FF         RST     0X38            
7FF8: FF         RST     0X38            
7FF9: FF         RST     0X38            
7FFA: FF         RST     0X38            
7FFB: FF         RST     0X38            
7FFC: FF         RST     0X38            
7FFD: FF         RST     0X38            
7FFE: FF         RST     0X38            
7FFF: FF         RST     0X38            
```