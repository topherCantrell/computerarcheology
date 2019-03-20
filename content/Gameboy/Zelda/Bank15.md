![Bank 15](GBZelda.jpg)

# Bank 15

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: CD AF 3D   CALL    $3DAF           
4003: 21 30 C3   LD      HL,$C330        
4006: 09         ADD     HL,BC           
4007: 70         LD      (HL),B          
4008: 21 60 C2   LD      HL,$C260        
400B: 09         ADD     HL,BC           
400C: 70         LD      (HL),B          
400D: 21 70 C2   LD      HL,$C270        
4010: 09         ADD     HL,BC           
4011: 70         LD      (HL),B          
4012: 21 20 C3   LD      HL,$C320        
4015: 09         ADD     HL,BC           
4016: 70         LD      (HL),B          
4017: 21 90 C2   LD      HL,$C290        
401A: 09         ADD     HL,BC           
401B: 70         LD      (HL),B          
401C: 21 A0 C2   LD      HL,$C2A0        
401F: 09         ADD     HL,BC           
4020: 70         LD      (HL),B          
4021: 21 B0 C2   LD      HL,$C2B0        
4024: 09         ADD     HL,BC           
4025: 70         LD      (HL),B          
4026: 21 C0 C2   LD      HL,$C2C0        
4029: 09         ADD     HL,BC           
402A: 70         LD      (HL),B          
402B: 21 D0 C2   LD      HL,$C2D0        
402E: 09         ADD     HL,BC           
402F: 70         LD      (HL),B          
4030: 21 40 C4   LD      HL,$C440        
4033: 09         ADD     HL,BC           
4034: 70         LD      (HL),B          
4035: 21 90 C3   LD      HL,$C390        
4038: 09         ADD     HL,BC           
4039: 70         LD      (HL),B          
403A: 21 E0 C2   LD      HL,$C2E0        
403D: 09         ADD     HL,BC           
403E: 70         LD      (HL),B          
403F: 21 F0 C2   LD      HL,$C2F0        
4042: 09         ADD     HL,BC           
4043: 70         LD      (HL),B          
4044: 21 00 C3   LD      HL,$C300        
4047: 09         ADD     HL,BC           
4048: 70         LD      (HL),B          
4049: 21 10 C3   LD      HL,$C310        
404C: 09         ADD     HL,BC           
404D: 70         LD      (HL),B          
404E: 21 80 C3   LD      HL,$C380        
4051: 09         ADD     HL,BC           
4052: 70         LD      (HL),B          
4053: AF         XOR     A               
4054: CD 87 3B   CALL    $3B87           
4057: 21 D0 C3   LD      HL,$C3D0        
405A: 09         ADD     HL,BC           
405B: 70         LD      (HL),B          
405C: 21 60 C3   LD      HL,$C360        
405F: 09         ADD     HL,BC           
4060: 70         LD      (HL),B          
4061: 21 10 C4   LD      HL,$C410        
4064: 09         ADD     HL,BC           
4065: 70         LD      (HL),B          
4066: 21 20 C2   LD      HL,$C220        
4069: 09         ADD     HL,BC           
406A: 70         LD      (HL),B          
406B: 21 30 C2   LD      HL,$C230        
406E: 09         ADD     HL,BC           
406F: 70         LD      (HL),B          
4070: 21 70 C4   LD      HL,$C470        
4073: 09         ADD     HL,BC           
4074: 70         LD      (HL),B          
4075: 21 50 C4   LD      HL,$C450        
4078: 09         ADD     HL,BC           
4079: 70         LD      (HL),B          
407A: 21 80 C4   LD      HL,$C480        
407D: 09         ADD     HL,BC           
407E: 70         LD      (HL),B          
407F: 21 90 C4   LD      HL,$C490        
4082: 09         ADD     HL,BC           
4083: 70         LD      (HL),B          
4084: 21 20 C4   LD      HL,$C420        
4087: 09         ADD     HL,BC           
4088: 70         LD      (HL),B          
4089: 21 E0 C4   LD      HL,$C4E0        
408C: 09         ADD     HL,BC           
408D: 70         LD      (HL),B          
408E: 21 F0 C4   LD      HL,$C4F0        
4091: 09         ADD     HL,BC           
4092: 70         LD      (HL),B          
4093: 21 D0 C5   LD      HL,$C5D0        
4096: 09         ADD     HL,BC           
4097: 36 FF      LD      (HL),$FF        
4099: C9         RET                     
409A: F0 F8      LD      A,($F8)         
409C: E6 20      AND     $20             
409E: C2 35 7C   JP      NZ,$7C35        
40A1: CD 20 7B   CALL    $7B20           
40A4: F0 F0      LD      A,($F0)         
40A6: C7         RST     0X00            
40A7: AD         XOR     L               
40A8: 40         LD      B,B             
40A9: BC         CP      H               
40AA: 40         LD      B,B             
40AB: D2 40 FA   JP      NC,$FA40        
40AE: CB C1      SET     1,E             
40B0: A7         AND     A               
40B1: 28 08      JR      Z,$40BB         
40B3: CD 8D 3B   CALL    $3B8D           
40B6: CD 91 08   CALL    $0891           
40B9: 36 20      LD      (HL),$20        
40BB: C9         RET                     
40BC: 3E 02      LD      A,$02           
40BE: E0 A1      LDFF00  ($A1),A         
40C0: EA 67 C1   LD      ($C167),A       
40C3: CD 91 08   CALL    $0891           
40C6: 20 09      JR      NZ,$40D1        
40C8: 36 30      LD      (HL),$30        
40CA: 3E 11      LD      A,$11           
40CC: E0 F4      LDFF00  ($F4),A         
40CE: CD 8D 3B   CALL    $3B8D           
40D1: C9         RET                     
40D2: 3E 02      LD      A,$02           
40D4: E0 A1      LDFF00  ($A1),A         
40D6: CD 91 08   CALL    $0891           
40D9: 20 11      JR      NZ,$40EC        
40DB: EA 67 C1   LD      ($C167),A       
40DE: EA 55 C1   LD      ($C155),A       
40E1: 3E 39      LD      A,$39           
40E3: CD 97 21   CALL    $2197           
40E6: CD E4 7C   CALL    $7CE4           
40E9: C3 35 7C   JP      $7C35           
40EC: 1E 01      LD      E,$01           
40EE: E6 04      AND     $04             
40F0: 28 02      JR      Z,$40F4         
40F2: 1E FF      LD      E,$FF           
40F4: 7B         LD      A,E             
40F5: EA 55 C1   LD      ($C155),A       
40F8: C9         RET                     
40F9: F8 10      LDHL    SP,$10          
40FB: FA 10 11   LD      A,($1110)       
40FE: F9         LD      SP,HL           
40FF: 40         LD      B,B             
4100: CD 3B 3C   CALL    $3C3B           
4103: CD 20 7B   CALL    $7B20           
4106: AF         XOR     A               
4107: E0 E8      LDFF00  ($E8),A         
4109: F0 F0      LD      A,($F0)         
410B: C7         RST     0X00            
410C: 10 41      STOP    $41             
410E: 24         INC     H               
410F: 41         LD      B,C             
4110: 21 10 C2   LD      HL,$C210        
4113: 09         ADD     HL,BC           
4114: 7E         LD      A,(HL)          
4115: 21 C0 C2   LD      HL,$C2C0        
4118: 09         ADD     HL,BC           
4119: 77         LD      (HL),A          
411A: C6 10      ADD     $10             
411C: 21 B0 C2   LD      HL,$C2B0        
411F: 09         ADD     HL,BC           
4120: 77         LD      (HL),A          
4121: C3 8D 3B   JP      $3B8D           
4124: F0 BA      LD      A,($BA)         
4126: FE 02      CP      $02             
4128: 28 42      JR      Z,$416C         
412A: A7         AND     A               
412B: 28 1D      JR      Z,$414A         
412D: 21 D0 C3   LD      HL,$C3D0        
4130: 09         ADD     HL,BC           
4131: 34         INC     (HL)            
4132: 7E         LD      A,(HL)          
4133: FE 0A      CP      $0A             
4135: 38 12      JR      C,$4149         
4137: 70         LD      (HL),B          
4138: 3E 11      LD      A,$11           
413A: E0 F4      LDFF00  ($F4),A         
413C: 21 C0 C2   LD      HL,$C2C0        
413F: 09         ADD     HL,BC           
4140: 7E         LD      A,(HL)          
4141: 21 10 C2   LD      HL,$C210        
4144: 09         ADD     HL,BC           
4145: BE         CP      (HL)            
4146: 28 01      JR      Z,$4149         
4148: 35         DEC     (HL)            
4149: C9         RET                     
414A: 21 B0 C2   LD      HL,$C2B0        
414D: 09         ADD     HL,BC           
414E: 7E         LD      A,(HL)          
414F: 21 10 C2   LD      HL,$C210        
4152: 09         ADD     HL,BC           
4153: BE         CP      (HL)            
4154: 28 12      JR      Z,$4168         
4156: 21 D0 C3   LD      HL,$C3D0        
4159: 09         ADD     HL,BC           
415A: 7E         LD      A,(HL)          
415B: 34         INC     (HL)            
415C: FE 0D      CP      $0D             
415E: 38 0C      JR      C,$416C         
4160: 70         LD      (HL),B          
4161: 21 10 C2   LD      HL,$C210        
4164: 09         ADD     HL,BC           
4165: 34         INC     (HL)            
4166: 18 04      JR      $416C           
4168: 21 E8 FF   LD      HL,$FFE8        
416B: 34         INC     (HL)            
416C: CD BA 3D   CALL    $3DBA           
416F: CD DF 7B   CALL    $7BDF           
4172: C6 0C      ADD     $0C             
4174: FE 18      CP      $18             
4176: 30 4E      JR      NC,$41C6        
4178: CD EF 7B   CALL    $7BEF           
417B: C6 10      ADD     $10             
417D: FE 1C      CP      $1C             
417F: 30 45      JR      NC,$41C6        
4181: CD 42 09   CALL    $0942           
4184: CD 95 14   CALL    $1495           
4187: CD 0E 7C   CALL    $7C0E           
418A: 7B         LD      A,E             
418B: FE 00      CP      $00             
418D: 20 07      JR      NZ,$4196        
418F: F0 EE      LD      A,($EE)         
4191: C6 0C      ADD     $0C             
4193: E0 98      LDFF00  ($98),A         
4195: C9         RET                     
4196: FE 01      CP      $01             
4198: 20 07      JR      NZ,$41A1        
419A: F0 EE      LD      A,($EE)         
419C: C6 F4      ADD     $F4             
419E: E0 98      LDFF00  ($98),A         
41A0: C9         RET                     
41A1: FE 02      CP      $02             
41A3: 20 11      JR      NZ,$41B6        
41A5: F0 EB      LD      A,($EB)         
41A7: FE 47      CP      $47             
41A9: 20 04      JR      NZ,$41AF        
41AB: F0 E8      LD      A,($E8)         
41AD: A7         AND     A               
41AE: C0         RET     NZ              
41AF: F0 EC      LD      A,($EC)         
41B1: C6 F0      ADD     $F0             
41B3: E0 99      LDFF00  ($99),A         
41B5: C9         RET                     
41B6: F0 EB      LD      A,($EB)         
41B8: FE 46      CP      $46             
41BA: 20 04      JR      NZ,$41C0        
41BC: F0 E8      LD      A,($E8)         
41BE: A7         AND     A               
41BF: C0         RET     NZ              
41C0: F0 EC      LD      A,($EC)         
41C2: C6 0C      ADD     $0C             
41C4: E0 99      LDFF00  ($99),A         
41C6: C9         RET                     
41C7: 11 F9 40   LD      DE,$40F9        
41CA: CD 3B 3C   CALL    $3C3B           
41CD: CD 20 7B   CALL    $7B20           
41D0: AF         XOR     A               
41D1: E0 E8      LDFF00  ($E8),A         
41D3: F0 F0      LD      A,($F0)         
41D5: C7         RST     0X00            
41D6: DA 41 EE   JP      C,$EE41         
41D9: 41         LD      B,C             
41DA: 21 10 C2   LD      HL,$C210        
41DD: 09         ADD     HL,BC           
41DE: 7E         LD      A,(HL)          
41DF: 21 C0 C2   LD      HL,$C2C0        
41E2: 09         ADD     HL,BC           
41E3: 77         LD      (HL),A          
41E4: D6 10      SUB     $10             
41E6: 21 B0 C2   LD      HL,$C2B0        
41E9: 09         ADD     HL,BC           
41EA: 77         LD      (HL),A          
41EB: C3 8D 3B   JP      $3B8D           
41EE: F0 BA      LD      A,($BA)         
41F0: FE 02      CP      $02             
41F2: 28 42      JR      Z,$4236         
41F4: A7         AND     A               
41F5: 28 1D      JR      Z,$4214         
41F7: 21 D0 C3   LD      HL,$C3D0        
41FA: 09         ADD     HL,BC           
41FB: 34         INC     (HL)            
41FC: 7E         LD      A,(HL)          
41FD: FE 0A      CP      $0A             
41FF: 38 12      JR      C,$4213         
4201: 70         LD      (HL),B          
4202: 3E 11      LD      A,$11           
4204: E0 F4      LDFF00  ($F4),A         
4206: 21 C0 C2   LD      HL,$C2C0        
4209: 09         ADD     HL,BC           
420A: 7E         LD      A,(HL)          
420B: 21 10 C2   LD      HL,$C210        
420E: 09         ADD     HL,BC           
420F: BE         CP      (HL)            
4210: 28 01      JR      Z,$4213         
4212: 34         INC     (HL)            
4213: C9         RET                     
4214: 21 B0 C2   LD      HL,$C2B0        
4217: 09         ADD     HL,BC           
4218: 7E         LD      A,(HL)          
4219: 21 10 C2   LD      HL,$C210        
421C: 09         ADD     HL,BC           
421D: BE         CP      (HL)            
421E: 28 12      JR      Z,$4232         
4220: 21 D0 C3   LD      HL,$C3D0        
4223: 09         ADD     HL,BC           
4224: 7E         LD      A,(HL)          
4225: 34         INC     (HL)            
4226: FE 0D      CP      $0D             
4228: 38 0C      JR      C,$4236         
422A: 70         LD      (HL),B          
422B: 21 10 C2   LD      HL,$C210        
422E: 09         ADD     HL,BC           
422F: 35         DEC     (HL)            
4230: 18 04      JR      $4236           
4232: 21 E8 FF   LD      HL,$FFE8        
4235: 34         INC     (HL)            
4236: CD 6C 41   CALL    $416C           
4239: C9         RET                     
423A: 11 F9 40   LD      DE,$40F9        
423D: CD 3B 3C   CALL    $3C3B           
4240: CD 20 7B   CALL    $7B20           
4243: AF         XOR     A               
4244: E0 E8      LDFF00  ($E8),A         
4246: F0 F0      LD      A,($F0)         
4248: C7         RST     0X00            
4249: 4D         LD      C,L             
424A: 42         LD      B,D             
424B: 61         LD      H,C             
424C: 42         LD      B,D             
424D: 21 00 C2   LD      HL,$C200        
4250: 09         ADD     HL,BC           
4251: 7E         LD      A,(HL)          
4252: 21 C0 C2   LD      HL,$C2C0        
4255: 09         ADD     HL,BC           
4256: 77         LD      (HL),A          
4257: C6 10      ADD     $10             
4259: 21 B0 C2   LD      HL,$C2B0        
425C: 09         ADD     HL,BC           
425D: 77         LD      (HL),A          
425E: C3 8D 3B   JP      $3B8D           
4261: F0 BA      LD      A,($BA)         
4263: FE 02      CP      $02             
4265: 28 42      JR      Z,$42A9         
4267: A7         AND     A               
4268: 28 1D      JR      Z,$4287         
426A: 21 D0 C3   LD      HL,$C3D0        
426D: 09         ADD     HL,BC           
426E: 34         INC     (HL)            
426F: 7E         LD      A,(HL)          
4270: FE 0A      CP      $0A             
4272: 38 12      JR      C,$4286         
4274: 70         LD      (HL),B          
4275: 3E 11      LD      A,$11           
4277: E0 F4      LDFF00  ($F4),A         
4279: 21 C0 C2   LD      HL,$C2C0        
427C: 09         ADD     HL,BC           
427D: 7E         LD      A,(HL)          
427E: 21 00 C2   LD      HL,$C200        
4281: 09         ADD     HL,BC           
4282: BE         CP      (HL)            
4283: 28 01      JR      Z,$4286         
4285: 35         DEC     (HL)            
4286: C9         RET                     
4287: 21 B0 C2   LD      HL,$C2B0        
428A: 09         ADD     HL,BC           
428B: 7E         LD      A,(HL)          
428C: 21 00 C2   LD      HL,$C200        
428F: 09         ADD     HL,BC           
4290: BE         CP      (HL)            
4291: 28 12      JR      Z,$42A5         
4293: 21 D0 C3   LD      HL,$C3D0        
4296: 09         ADD     HL,BC           
4297: 7E         LD      A,(HL)          
4298: 34         INC     (HL)            
4299: FE 0D      CP      $0D             
429B: 38 0C      JR      C,$42A9         
429D: 70         LD      (HL),B          
429E: 21 00 C2   LD      HL,$C200        
42A1: 09         ADD     HL,BC           
42A2: 34         INC     (HL)            
42A3: 18 04      JR      $42A9           
42A5: 21 E8 FF   LD      HL,$FFE8        
42A8: 34         INC     (HL)            
42A9: CD 6C 41   CALL    $416C           
42AC: C9         RET                     
42AD: 11 F9 40   LD      DE,$40F9        
42B0: CD 3B 3C   CALL    $3C3B           
42B3: CD 20 7B   CALL    $7B20           
42B6: AF         XOR     A               
42B7: E0 E8      LDFF00  ($E8),A         
42B9: F0 F0      LD      A,($F0)         
42BB: C7         RST     0X00            
42BC: C0         RET     NZ              
42BD: 42         LD      B,D             
42BE: D4 42 21   CALL    NC,$2142        
42C1: 00         NOP                     
42C2: C2 09 7E   JP      NZ,$7E09        
42C5: 21 C0 C2   LD      HL,$C2C0        
42C8: 09         ADD     HL,BC           
42C9: 77         LD      (HL),A          
42CA: D6 10      SUB     $10             
42CC: 21 B0 C2   LD      HL,$C2B0        
42CF: 09         ADD     HL,BC           
42D0: 77         LD      (HL),A          
42D1: C3 8D 3B   JP      $3B8D           
42D4: F0 BA      LD      A,($BA)         
42D6: FE 02      CP      $02             
42D8: 28 42      JR      Z,$431C         
42DA: A7         AND     A               
42DB: 28 1D      JR      Z,$42FA         
42DD: 21 D0 C3   LD      HL,$C3D0        
42E0: 09         ADD     HL,BC           
42E1: 34         INC     (HL)            
42E2: 7E         LD      A,(HL)          
42E3: FE 0A      CP      $0A             
42E5: 38 12      JR      C,$42F9         
42E7: 70         LD      (HL),B          
42E8: 3E 11      LD      A,$11           
42EA: E0 F4      LDFF00  ($F4),A         
42EC: 21 C0 C2   LD      HL,$C2C0        
42EF: 09         ADD     HL,BC           
42F0: 7E         LD      A,(HL)          
42F1: 21 00 C2   LD      HL,$C200        
42F4: 09         ADD     HL,BC           
42F5: BE         CP      (HL)            
42F6: 28 01      JR      Z,$42F9         
42F8: 34         INC     (HL)            
42F9: C9         RET                     
42FA: 21 B0 C2   LD      HL,$C2B0        
42FD: 09         ADD     HL,BC           
42FE: 7E         LD      A,(HL)          
42FF: 21 00 C2   LD      HL,$C200        
4302: 09         ADD     HL,BC           
4303: BE         CP      (HL)            
4304: 28 12      JR      Z,$4318         
4306: 21 D0 C3   LD      HL,$C3D0        
4309: 09         ADD     HL,BC           
430A: 7E         LD      A,(HL)          
430B: 34         INC     (HL)            
430C: FE 0D      CP      $0D             
430E: 38 0C      JR      C,$431C         
4310: 70         LD      (HL),B          
4311: 21 00 C2   LD      HL,$C200        
4314: 09         ADD     HL,BC           
4315: 35         DEC     (HL)            
4316: 18 04      JR      $431C           
4318: 21 E8 FF   LD      HL,$FFE8        
431B: 34         INC     (HL)            
431C: CD 6C 41   CALL    $416C           
431F: C9         RET                     
4320: 58         LD      E,B             
4321: 00         NOP                     
4322: 58         LD      E,B             
4323: 20 21      JR      NZ,$4346        
4325: 60         LD      H,B             
4326: C3 09 36   JP      $3609           
4329: FF         RST     0X38            
432A: CD 91 08   CALL    $0891           
432D: 17         RLA                     
432E: E6 10      AND     $10             
4330: E0 ED      LDFF00  ($ED),A         
4332: 11 20 43   LD      DE,$4320        
4335: CD 3B 3C   CALL    $3C3B           
4338: CD 20 7B   CALL    $7B20           
433B: CD E2 08   CALL    $08E2           
433E: CD EB 3B   CALL    $3BEB           
4341: CD 85 7A   CALL    $7A85           
4344: CD 9E 3B   CALL    $3B9E           
4347: 21 20 C4   LD      HL,$C420        
434A: 09         ADD     HL,BC           
434B: 7E         LD      A,(HL)          
434C: A7         AND     A               
434D: 28 15      JR      Z,$4364         
434F: 70         LD      (HL),B          
4350: FA F8 D6   LD      A,($D6F8)       
4353: A7         AND     A               
4354: 20 0E      JR      NZ,$4364        
4356: 3E 01      LD      A,$01           
4358: EA F8 D6   LD      ($D6F8),A       
435B: CD 91 08   CALL    $0891           
435E: 36 18      LD      (HL),$18        
4360: 3E 0E      LD      A,$0E           
4362: E0 F3      LDFF00  ($F3),A         
4364: C9         RET                     
4365: F0 F0      LD      A,($F0)         
4367: A7         AND     A               
4368: C2 CA 43   JP      NZ,$43CA        
436B: CD 20 7B   CALL    $7B20           
436E: CD 91 08   CALL    $0891           
4371: 20 3A      JR      NZ,$43AD        
4373: CD ED 27   CALL    $27ED           
4376: E6 3F      AND     $3F             
4378: C6 30      ADD     $30             
437A: 77         LD      (HL),A          
437B: F0 99      LD      A,($99)         
437D: FE 18      CP      $18             
437F: D8         RET     C               
4380: 3E 45      LD      A,$45           
4382: CD 01 3C   CALL    $3C01           
4385: D8         RET     C               
4386: CD ED 27   CALL    $27ED           
4389: 17         RLA                     
438A: 17         RLA                     
438B: 17         RLA                     
438C: 17         RLA                     
438D: E6 70      AND     $70             
438F: C6 18      ADD     $18             
4391: 21 00 C2   LD      HL,$C200        
4394: 19         ADD     HL,DE           
4395: 77         LD      (HL),A          
4396: 21 10 C2   LD      HL,$C210        
4399: 19         ADD     HL,DE           
439A: 36 10      LD      (HL),$10        
439C: 21 40 C3   LD      HL,$C340        
439F: 19         ADD     HL,DE           
43A0: 36 12      LD      (HL),$12        
43A2: 21 50 C3   LD      HL,$C350        
43A5: 19         ADD     HL,DE           
43A6: CB FE      SET     1,E             
43A8: 21 90 C2   LD      HL,$C290        
43AB: 19         ADD     HL,DE           
43AC: 34         INC     (HL)            
43AD: C9         RET                     
43AE: 5C         LD      E,H             
43AF: 00         NOP                     
43B0: 5E         LD      E,(HL)          
43B1: 00         NOP                     
43B2: 5E         LD      E,(HL)          
43B3: 20 5C      JR      NZ,$4411        
43B5: 20 5E      JR      NZ,$4415        
43B7: 60         LD      H,B             
43B8: 5C         LD      E,H             
43B9: 60         LD      H,B             
43BA: 5C         LD      E,H             
43BB: 40         LD      B,B             
43BC: 5E         LD      E,(HL)          
43BD: 40         LD      B,B             
43BE: 0C         INC     C               
43BF: F4                              
43C0: 05         DEC     B               
43C1: FB         EI                      
43C2: 08 0A 06   LD      ($060A),SP      
43C5: 0C         INC     C               
43C6: 18 20      JR      $43E8           
43C8: 1C         INC     E               
43C9: 28 11      JR      Z,$43DC         
43CB: AE         XOR     (HL)            
43CC: 43         LD      B,E             
43CD: CD 3B 3C   CALL    $3C3B           
43D0: CD 20 7B   CALL    $7B20           
43D3: CD E2 08   CALL    $08E2           
43D6: CD B4 3B   CALL    $3BB4           
43D9: F0 E7      LD      A,($E7)         
43DB: 1F         RRA                     
43DC: 1F         RRA                     
43DD: 1F         RRA                     
43DE: E6 03      AND     $03             
43E0: CD 87 3B   CALL    $3B87           
43E3: CD 8C 7B   CALL    $7B8C           
43E6: CD C5 7B   CALL    $7BC5           
43E9: 21 20 C3   LD      HL,$C320        
43EC: 09         ADD     HL,BC           
43ED: 35         DEC     (HL)            
43EE: 35         DEC     (HL)            
43EF: 21 10 C3   LD      HL,$C310        
43F2: 09         ADD     HL,BC           
43F3: 7E         LD      A,(HL)          
43F4: E6 80      AND     $80             
43F6: 28 38      JR      Z,$4430         
43F8: 70         LD      (HL),B          
43F9: CD ED 27   CALL    $27ED           
43FC: E6 03      AND     $03             
43FE: 5F         LD      E,A             
43FF: 50         LD      D,B             
4400: 21 BE 43   LD      HL,$43BE        
4403: 19         ADD     HL,DE           
4404: 7E         LD      A,(HL)          
4405: 21 40 C2   LD      HL,$C240        
4408: 09         ADD     HL,BC           
4409: 77         LD      (HL),A          
440A: CD ED 27   CALL    $27ED           
440D: E6 03      AND     $03             
440F: 5F         LD      E,A             
4410: 50         LD      D,B             
4411: 21 C2 43   LD      HL,$43C2        
4414: 19         ADD     HL,DE           
4415: 7E         LD      A,(HL)          
4416: 21 50 C2   LD      HL,$C250        
4419: 09         ADD     HL,BC           
441A: 77         LD      (HL),A          
441B: CD ED 27   CALL    $27ED           
441E: E6 03      AND     $03             
4420: 5F         LD      E,A             
4421: 50         LD      D,B             
4422: 21 C6 43   LD      HL,$43C6        
4425: 19         ADD     HL,DE           
4426: 7E         LD      A,(HL)          
4427: 21 20 C3   LD      HL,$C320        
442A: 09         ADD     HL,BC           
442B: 77         LD      (HL),A          
442C: 3E 20      LD      A,$20           
442E: E0 F2      LDFF00  ($F2),A         
4430: F0 EE      LD      A,($EE)         
4432: FE A8      CP      $A8             
4434: D2 35 7C   JP      NC,$7C35        
4437: F0 EC      LD      A,($EC)         
4439: FE 84      CP      $84             
443B: D2 35 7C   JP      NC,$7C35        
443E: C9         RET                     
443F: CD 20 7B   CALL    $7B20           
4442: 1E 0F      LD      E,$0F           
4444: 50         LD      D,B             
4445: 21 80 C2   LD      HL,$C280        
4448: 19         ADD     HL,DE           
4449: 7E         LD      A,(HL)          
444A: FE 05      CP      $05             
444C: 20 3F      JR      NZ,$448D        
444E: 21 A0 C3   LD      HL,$C3A0        
4451: 19         ADD     HL,DE           
4452: 7E         LD      A,(HL)          
4453: FE 08      CP      $08             
4455: 20 36      JR      NZ,$448D        
4457: 21 E0 C2   LD      HL,$C2E0        
445A: 19         ADD     HL,DE           
445B: 7E         LD      A,(HL)          
445C: FE 08      CP      $08             
445E: 20 2D      JR      NZ,$448D        
4460: 21 00 C2   LD      HL,$C200        
4463: 19         ADD     HL,DE           
4464: F0 EE      LD      A,($EE)         
4466: 96         SUB     (HL)            
4467: C6 08      ADD     $08             
4469: FE 10      CP      $10             
446B: 30 20      JR      NC,$448D        
446D: 21 10 C2   LD      HL,$C210        
4470: 19         ADD     HL,DE           
4471: F0 EC      LD      A,($EC)         
4473: 96         SUB     (HL)            
4474: C6 08      ADD     $08             
4476: FE 10      CP      $10             
4478: 30 13      JR      NC,$448D        
447A: F0 F6      LD      A,($F6)         
447C: FE DF      CP      $DF             
447E: 3E 92      LD      A,$92           
4480: 28 07      JR      Z,$4489         
4482: FA 79 DB   LD      A,($DB79)       
4485: A7         AND     A               
4486: C0         RET     NZ              
4487: 3E 43      LD      A,$43           
4489: CD 97 21   CALL    $2197           
448C: C9         RET                     
448D: 1D         DEC     E               
448E: 7B         LD      A,E             
448F: FE FF      CP      $FF             
4491: 20 B2      JR      NZ,$4445        
4493: C9         RET                     
4494: CD 20 7B   CALL    $7B20           
4497: CD D3 7A   CALL    $7AD3           
449A: D0         RET     NC              
449B: 3E 12      LD      A,$12           
449D: CD 97 21   CALL    $2197           
44A0: C9         RET                     
44A1: FF         RST     0X38            
44A2: 00         NOP                     
44A3: FF         RST     0X38            
44A4: 00         NOP                     
44A5: 54         LD      D,H             
44A6: 00         NOP                     
44A7: 56         LD      D,(HL)          
44A8: 00         NOP                     
44A9: 58         LD      E,B             
44AA: 00         NOP                     
44AB: 5A         LD      E,D             
44AC: 00         NOP                     
44AD: 56         LD      D,(HL)          
44AE: 20 54      JR      NZ,$4504        
44B0: 20 5A      JR      NZ,$450C        
44B2: 20 58      JR      NZ,$450C        
44B4: 20 5C      JR      NZ,$4512        
44B6: 00         NOP                     
44B7: 5C         LD      E,H             
44B8: 20 5E      JR      NZ,$4518        
44BA: 00         NOP                     
44BB: 5E         LD      E,(HL)          
44BC: 00         NOP                     
44BD: F0 F1      LD      A,($F1)         
44BF: FE FF      CP      $FF             
44C1: 28 16      JR      Z,$44D9         
44C3: FE 05      CP      $05             
44C5: 38 0C      JR      C,$44D3         
44C7: D6 05      SUB     $05             
44C9: E0 F1      LDFF00  ($F1),A         
44CB: 11 B5 44   LD      DE,$44B5        
44CE: CD D0 3C   CALL    $3CD0           
44D1: 18 06      JR      $44D9           
44D3: 11 A1 44   LD      DE,$44A1        
44D6: CD 3B 3C   CALL    $3C3B           
44D9: CD 20 7B   CALL    $7B20           
44DC: CD 42 7B   CALL    $7B42           
44DF: CD 8C 7B   CALL    $7B8C           
44E2: CD 9E 3B   CALL    $3B9E           
44E5: F0 F0      LD      A,($F0)         
44E7: C7         RST     0X00            
44E8: EE 44      XOR     $44             
44EA: 02         LD      (BC),A          
44EB: 45         LD      B,L             
44EC: 57         LD      D,A             
44ED: 45         LD      B,L             
44EE: 21 40 C2   LD      HL,$C240        
44F1: 09         ADD     HL,BC           
44F2: 36 08      LD      (HL),$08        
44F4: CD 91 08   CALL    $0891           
44F7: CD ED 27   CALL    $27ED           
44FA: E6 7F      AND     $7F             
44FC: C6 40      ADD     $40             
44FE: 77         LD      (HL),A          
44FF: C3 8D 3B   JP      $3B8D           
4502: CD BF 3B   CALL    $3BBF           
4505: CD 91 08   CALL    $0891           
4508: 20 29      JR      NZ,$4533        
450A: 21 40 C3   LD      HL,$C340        
450D: 09         ADD     HL,BC           
450E: 36 12      LD      (HL),$12        
4510: 21 20 C3   LD      HL,$C320        
4513: 09         ADD     HL,BC           
4514: 36 18      LD      (HL),$18        
4516: CD 8D 3B   CALL    $3B8D           
4519: 21 40 C2   LD      HL,$C240        
451C: 09         ADD     HL,BC           
451D: CB 26      SET     1,E             
451F: 3E 0E      LD      A,$0E           
4521: E0 F2      LDFF00  ($F2),A         
4523: F0 EE      LD      A,($EE)         
4525: E0 D7      LDFF00  ($D7),A         
4527: F0 EC      LD      A,($EC)         
4529: C6 00      ADD     $00             
452B: E0 D8      LDFF00  ($D8),A         
452D: 3E 01      LD      A,$01           
452F: CD 53 09   CALL    $0953           
4532: C9         RET                     
4533: 21 A0 C2   LD      HL,$C2A0        
4536: 09         ADD     HL,BC           
4537: 7E         LD      A,(HL)          
4538: E6 03      AND     $03             
453A: 28 08      JR      Z,$4544         
453C: 21 40 C2   LD      HL,$C240        
453F: 09         ADD     HL,BC           
4540: 7E         LD      A,(HL)          
4541: 2F         CPL                     
4542: 3C         INC     A               
4543: 77         LD      (HL),A          
4544: 21 40 C2   LD      HL,$C240        
4547: 09         ADD     HL,BC           
4548: 1E 06      LD      E,$06           
454A: 7E         LD      A,(HL)          
454B: E6 80      AND     $80             
454D: 28 02      JR      Z,$4551         
454F: 1E 05      LD      E,$05           
4551: 7B         LD      A,E             
4552: CD 87 3B   CALL    $3B87           
4555: C9         RET                     
4556: C9         RET                     
4557: CD B4 3B   CALL    $3BB4           
455A: CD C5 7B   CALL    $7BC5           
455D: 21 20 C3   LD      HL,$C320        
4560: 09         ADD     HL,BC           
4561: 35         DEC     (HL)            
4562: 21 10 C3   LD      HL,$C310        
4565: 09         ADD     HL,BC           
4566: 7E         LD      A,(HL)          
4567: E6 80      AND     $80             
4569: 28 21      JR      Z,$458C         
456B: 70         LD      (HL),B          
456C: CD 1F 45   CALL    $451F           
456F: CD 91 08   CALL    $0891           
4572: CD ED 27   CALL    $27ED           
4575: E6 7F      AND     $7F             
4577: C6 50      ADD     $50             
4579: 77         LD      (HL),A          
457A: 21 40 C2   LD      HL,$C240        
457D: 09         ADD     HL,BC           
457E: CB 2E      SET     1,E             
4580: 21 40 C3   LD      HL,$C340        
4583: 09         ADD     HL,BC           
4584: 36 52      LD      (HL),$52        
4586: CD 8D 3B   CALL    $3B8D           
4589: 36 01      LD      (HL),$01        
458B: C9         RET                     
458C: 1E 01      LD      E,$01           
458E: 21 40 C2   LD      HL,$C240        
4591: 09         ADD     HL,BC           
4592: 7E         LD      A,(HL)          
4593: E6 80      AND     $80             
4595: 20 02      JR      NZ,$4599        
4597: 1E 03      LD      E,$03           
4599: 21 20 C3   LD      HL,$C320        
459C: 09         ADD     HL,BC           
459D: 7E         LD      A,(HL)          
459E: E6 80      AND     $80             
45A0: 28 01      JR      Z,$45A3         
45A2: 1C         INC     E               
45A3: 7B         LD      A,E             
45A4: CD 87 3B   CALL    $3B87           
45A7: C9         RET                     
45A8: 00         NOP                     
45A9: 00         NOP                     
45AA: 46         LD      B,(HL)          
45AB: 00         NOP                     
45AC: 00         NOP                     
45AD: 08 7E 00   LD      ($007E),SP      
45B0: F0 00      LD      A,($00)         
45B2: 46         LD      B,(HL)          
45B3: 00         NOP                     
45B4: F0 08      LD      A,($08)         
45B6: 7E         LD      A,(HL)          
45B7: 00         NOP                     
45B8: E0 00      LDFF00  ($00),A         
45BA: 46         LD      B,(HL)          
45BB: 00         NOP                     
45BC: E0 08      LDFF00  ($08),A         
45BE: 7E         LD      A,(HL)          
45BF: 00         NOP                     
45C0: D0         RET     NC              
45C1: 00         NOP                     
45C2: 46         LD      B,(HL)          
45C3: 00         NOP                     
45C4: D0         RET     NC              
45C5: 08 7E 00   LD      ($007E),SP      
45C8: C0         RET     NZ              
45C9: 00         NOP                     
45CA: 46         LD      B,(HL)          
45CB: 00         NOP                     
45CC: C0         RET     NZ              
45CD: 08 7E 00   LD      ($007E),SP      
45D0: 21 D0 C3   LD      HL,$C3D0        
45D3: 09         ADD     HL,BC           
45D4: 7E         LD      A,(HL)          
45D5: C6 01      ADD     $01             
45D7: CB 27      SET     1,E             
45D9: 4F         LD      C,A             
45DA: 21 A8 45   LD      HL,$45A8        
45DD: CD 26 3D   CALL    $3D26           
45E0: 3E 0A      LD      A,$0A           
45E2: CD D0 3D   CALL    $3DD0           
45E5: CD 20 7B   CALL    $7B20           
45E8: FA 95 DB   LD      A,($DB95)       
45EB: FE 01      CP      $01             
45ED: C8         RET     Z               
45EE: F0 F0      LD      A,($F0)         
45F0: C7         RST     0X00            
45F1: FB         EI                      
45F2: 45         LD      B,L             
45F3: 03         INC     BC              
45F4: 46         LD      B,(HL)          
45F5: 2C         INC     L               
45F6: 46         LD      B,(HL)          
45F7: 45         LD      B,L             
45F8: 46         LD      B,(HL)          
45F9: 68         LD      L,B             
45FA: 46         LD      B,(HL)          
45FB: CD 91 08   CALL    $0891           
45FE: 36 C0      LD      (HL),$C0        
4600: C3 8D 3B   JP      $3B8D           
4603: CD 91 08   CALL    $0891           
4606: FE 40      CP      $40             
4608: 20 06      JR      NZ,$4610        
460A: 35         DEC     (HL)            
460B: 3E D7      LD      A,$D7           
460D: C3 97 21   JP      $2197           
4610: A7         AND     A               
4611: C0         RET     NZ              
4612: 3E 50      LD      A,$50           
4614: 3D         DEC     A               
4615: E0 D7      LDFF00  ($D7),A         
4617: 3E 30      LD      A,$30           
4619: E0 D8      LDFF00  ($D8),A         
461B: 3E 02      LD      A,$02           
461D: CD 53 09   CALL    $0953           
4620: 3E 2F      LD      A,$2F           
4622: E0 F2      LDFF00  ($F2),A         
4624: 3E 00      LD      A,$00           
4626: CD 87 3B   CALL    $3B87           
4629: C3 8D 3B   JP      $3B8D           
462C: F0 98      LD      A,($98)         
462E: D6 50      SUB     $50             
4630: C6 08      ADD     $08             
4632: FE 10      CP      $10             
4634: 30 0B      JR      NC,$4641        
4636: F0 99      LD      A,($99)         
4638: D6 30      SUB     $30             
463A: C6 08      ADD     $08             
463C: FE 10      CP      $10             
463E: 30 01      JR      NC,$4641        
4640: C9         RET                     
4641: CD 8D 3B   CALL    $3B8D           
4644: C9         RET                     
4645: F0 98      LD      A,($98)         
4647: D6 50      SUB     $50             
4649: C6 08      ADD     $08             
464B: FE 10      CP      $10             
464D: 30 18      JR      NC,$4667        
464F: F0 99      LD      A,($99)         
4651: D6 30      SUB     $30             
4653: C6 08      ADD     $08             
4655: FE 10      CP      $10             
4657: 30 0E      JR      NC,$4667        
4659: FA 46 C1   LD      A,($C146)       
465C: A7         AND     A               
465D: C0         RET     NZ              
465E: CD 8D 3B   CALL    $3B8D           
4661: 21 B0 C2   LD      HL,$C2B0        
4664: 09         ADD     HL,BC           
4665: 36 30      LD      (HL),$30        
4667: C9         RET                     
4668: 3E 02      LD      A,$02           
466A: E0 A1      LDFF00  ($A1),A         
466C: EA 67 C1   LD      ($C167),A       
466F: 21 B0 C2   LD      HL,$C2B0        
4672: 09         ADD     HL,BC           
4673: 7E         LD      A,(HL)          
4674: E0 99      LDFF00  ($99),A         
4676: 3E 50      LD      A,$50           
4678: E0 98      LDFF00  ($98),A         
467A: F0 E7      LD      A,($E7)         
467C: E6 07      AND     $07             
467E: 20 0A      JR      NZ,$468A        
4680: 21 D0 C3   LD      HL,$C3D0        
4683: 09         ADD     HL,BC           
4684: 7E         LD      A,(HL)          
4685: FE 04      CP      $04             
4687: 28 01      JR      Z,$468A         
4689: 34         INC     (HL)            
468A: F0 E7      LD      A,($E7)         
468C: E6 03      AND     $03             
468E: 20 14      JR      NZ,$46A4        
4690: 21 B0 C2   LD      HL,$C2B0        
4693: 09         ADD     HL,BC           
4694: 35         DEC     (HL)            
4695: 7E         LD      A,(HL)          
4696: FE 12      CP      $12             
4698: 30 0A      JR      NC,$46A4        
469A: AF         XOR     A               
469B: EA 96 DB   LD      ($DB96),A       
469E: 3E 01      LD      A,$01           
46A0: EA 95 DB   LD      ($DB95),A       
46A3: C9         RET                     
46A4: 3E 02      LD      A,$02           
46A6: E0 9E      LDFF00  ($9E),A         
46A8: F0 E7      LD      A,($E7)         
46AA: E6 08      AND     $08             
46AC: EA 20 C1   LD      ($C120),A       
46AF: C5         PUSH    BC              
46B0: CD 7C 08   CALL    $087C           
46B3: C1         POP     BC              
46B4: CD 3B 09   CALL    $093B           
46B7: EA 37 C1   LD      ($C137),A       
46BA: EA 6A C1   LD      ($C16A),A       
46BD: C9         RET                     
46BE: FA 56 DB   LD      A,($DB56)       
46C1: FE 80      CP      $80             
46C3: C2 35 7C   JP      NZ,$7C35        
46C6: 21 80 C3   LD      HL,$C380        
46C9: 09         ADD     HL,BC           
46CA: 7E         LD      A,(HL)          
46CB: A7         AND     A               
46CC: 20 0A      JR      NZ,$46D8        
46CE: F0 F1      LD      A,($F1)         
46D0: FE 0C      CP      $0C             
46D2: 30 04      JR      NC,$46D8        
46D4: C6 06      ADD     $06             
46D6: E0 F1      LDFF00  ($F1),A         
46D8: CD DB 4A   CALL    $4ADB           
46DB: F0 EA      LD      A,($EA)         
46DD: FE 01      CP      $01             
46DF: 20 08      JR      NZ,$46E9        
46E1: 3E 0C      LD      A,$0C           
46E3: CD C6 48   CALL    $48C6           
46E6: C3 3B 7C   JP      $7C3B           
46E9: CD 0E 38   CALL    $380E           
46EC: CD 20 7B   CALL    $7B20           
46EF: CD 42 7B   CALL    $7B42           
46F2: CD B4 3B   CALL    $3BB4           
46F5: 21 30 C4   LD      HL,$C430        
46F8: 09         ADD     HL,BC           
46F9: CB F6      SET     1,E             
46FB: 21 40 C3   LD      HL,$C340        
46FE: 09         ADD     HL,BC           
46FF: CB BE      SET     1,E             
4701: CD 8C 7B   CALL    $7B8C           
4704: CD 9E 3B   CALL    $3B9E           
4707: CD C5 7B   CALL    $7BC5           
470A: 21 20 C3   LD      HL,$C320        
470D: 09         ADD     HL,BC           
470E: 35         DEC     (HL)            
470F: 35         DEC     (HL)            
4710: 35         DEC     (HL)            
4711: 21 10 C3   LD      HL,$C310        
4714: 09         ADD     HL,BC           
4715: 7E         LD      A,(HL)          
4716: E6 80      AND     $80             
4718: E0 E8      LDFF00  ($E8),A         
471A: 28 06      JR      Z,$4722         
471C: 70         LD      (HL),B          
471D: 21 20 C3   LD      HL,$C320        
4720: 09         ADD     HL,BC           
4721: 70         LD      (HL),B          
4722: 21 90 C2   LD      HL,$C290        
4725: 09         ADD     HL,BC           
4726: 7E         LD      A,(HL)          
4727: C7         RST     0X00            
4728: 3C         INC     A               
4729: 47         LD      B,A             
472A: 58         LD      E,B             
472B: 47         LD      B,A             
472C: 8B         ADC     A,E             
472D: 47         LD      B,A             
472E: 4C         LD      C,H             
472F: 48         LD      C,B             
4730: 82         ADD     A,D             
4731: 48         LD      C,B             
4732: DF         RST     0X18            
4733: 48         LD      C,B             
4734: 5C         LD      E,H             
4735: 49         LD      C,C             
4736: 88         ADC     A,B             
4737: 49         LD      C,C             
4738: AD         XOR     L               
4739: 49         LD      C,C             
473A: D3                              
473B: 49         LD      C,C             
473C: CD 91 08   CALL    $0891           
473F: 36 20      LD      (HL),$20        
4741: AF         XOR     A               
4742: EA 28 D2   LD      ($D228),A       
4745: CD 87 3B   CALL    $3B87           
4748: CD 8D 3B   CALL    $3B8D           
474B: CD DF 7B   CALL    $7BDF           
474E: 7B         LD      A,E             
474F: EA 27 D2   LD      ($D227),A       
4752: 21 80 C3   LD      HL,$C380        
4755: 09         ADD     HL,BC           
4756: 77         LD      (HL),A          
4757: C9         RET                     
4758: CD 91 08   CALL    $0891           
475B: 20 23      JR      NZ,$4780        
475D: 3E 91      LD      A,$91           
475F: CD 85 21   CALL    $2185           
4762: 21 9F C1   LD      HL,$C19F        
4765: CB BE      SET     1,E             
4767: CD 8D 3B   CALL    $3B8D           
476A: CD 87 08   CALL    $0887           
476D: 36 30      LD      (HL),$30        
476F: 21 30 C4   LD      HL,$C430        
4772: 09         ADD     HL,BC           
4773: 36 84      LD      (HL),$84        
4775: 3E 01      LD      A,$01           
4777: EA 28 D2   LD      ($D228),A       
477A: 3E 01      LD      A,$01           
477C: CD 87 3B   CALL    $3B87           
477F: C9         RET                     
4780: C9         RET                     
4781: 08 F8 FC   LD      ($FCF8),SP      
4784: FC                              
4785: 20 E0      JR      NZ,$4767        
4787: 00         NOP                     
4788: 00         NOP                     
4789: D0         RET     NC              
478A: 30 CD      JR      NC,$4759        
478C: 8C         ADC     A,H             
478D: 08 28 5F   LD      ($5F28),SP      
4790: FE 0C      CP      $0C             
4792: 20 48      JR      NZ,$47DC        
4794: 3E 0C      LD      A,$0C           
4796: CD 01 3C   CALL    $3C01           
4799: 38 41      JR      C,$47DC         
479B: 3E 0A      LD      A,$0A           
479D: E0 F4      LDFF00  ($F4),A         
479F: C5         PUSH    BC              
47A0: F0 D9      LD      A,($D9)         
47A2: 4F         LD      C,A             
47A3: 21 81 47   LD      HL,$4781        
47A6: 09         ADD     HL,BC           
47A7: F0 D7      LD      A,($D7)         
47A9: 86         ADD     A,(HL)          
47AA: 21 00 C2   LD      HL,$C200        
47AD: 19         ADD     HL,DE           
47AE: 77         LD      (HL),A          
47AF: 21 83 47   LD      HL,$4783        
47B2: 09         ADD     HL,BC           
47B3: F0 D8      LD      A,($D8)         
47B5: 86         ADD     A,(HL)          
47B6: 21 10 C2   LD      HL,$C210        
47B9: 19         ADD     HL,DE           
47BA: 77         LD      (HL),A          
47BB: 21 85 47   LD      HL,$4785        
47BE: 09         ADD     HL,BC           
47BF: 7E         LD      A,(HL)          
47C0: 21 40 C2   LD      HL,$C240        
47C3: 19         ADD     HL,DE           
47C4: 77         LD      (HL),A          
47C5: 21 87 47   LD      HL,$4787        
47C8: 09         ADD     HL,BC           
47C9: 7E         LD      A,(HL)          
47CA: 21 50 C2   LD      HL,$C250        
47CD: 19         ADD     HL,DE           
47CE: 77         LD      (HL),A          
47CF: F0 D9      LD      A,($D9)         
47D1: 21 B0 C3   LD      HL,$C3B0        
47D4: 19         ADD     HL,DE           
47D5: 77         LD      (HL),A          
47D6: 21 80 C3   LD      HL,$C380        
47D9: 19         ADD     HL,DE           
47DA: 77         LD      (HL),A          
47DB: C1         POP     BC              
47DC: CD 8C 08   CALL    $088C           
47DF: 1E 00      LD      E,$00           
47E1: FE 0C      CP      $0C             
47E3: 38 02      JR      C,$47E7         
47E5: 1E 02      LD      E,$02           
47E7: 7B         LD      A,E             
47E8: CD 87 3B   CALL    $3B87           
47EB: CD AF 3D   CALL    $3DAF           
47EE: C9         RET                     
47EF: CD 87 08   CALL    $0887           
47F2: 20 0C      JR      NZ,$4800        
47F4: CD 91 08   CALL    $0891           
47F7: 36 30      LD      (HL),$30        
47F9: CD AF 3D   CALL    $3DAF           
47FC: CD 8D 3B   CALL    $3B8D           
47FF: C9         RET                     
4800: F0 E8      LD      A,($E8)         
4802: A7         AND     A               
4803: 28 1E      JR      Z,$4823         
4805: F0 98      LD      A,($98)         
4807: F5         PUSH    AF              
4808: CD DF 7B   CALL    $7BDF           
480B: 50         LD      D,B             
480C: 21 89 47   LD      HL,$4789        
480F: 19         ADD     HL,DE           
4810: F0 98      LD      A,($98)         
4812: 86         ADD     A,(HL)          
4813: E0 98      LDFF00  ($98),A         
4815: 3E 0C      LD      A,$0C           
4817: CD 25 3C   CALL    $3C25           
481A: F1         POP     AF              
481B: E0 98      LDFF00  ($98),A         
481D: 21 20 C3   LD      HL,$C320        
4820: 09         ADD     HL,BC           
4821: 36 10      LD      (HL),$10        
4823: F0 E7      LD      A,($E7)         
4825: 1F         RRA                     
4826: 1F         RRA                     
4827: 1F         RRA                     
4828: 1F         RRA                     
4829: E6 01      AND     $01             
482B: CD 87 3B   CALL    $3B87           
482E: EA 28 D2   LD      ($D228),A       
4831: CD 4B 47   CALL    $474B           
4834: 21 00 C3   LD      HL,$C300        
4837: 09         ADD     HL,BC           
4838: 7E         LD      A,(HL)          
4839: A7         AND     A               
483A: 20 0D      JR      NZ,$4849        
483C: CD ED 27   CALL    $27ED           
483F: E6 3F      AND     $3F             
4841: C6 30      ADD     $30             
4843: 77         LD      (HL),A          
4844: CD 8C 08   CALL    $088C           
4847: 36 18      LD      (HL),$18        
4849: C9         RET                     
484A: 28 D8      JR      Z,$4824         
484C: CD 91 08   CALL    $0891           
484F: 20 19      JR      NZ,$486A        
4851: 36 22      LD      (HL),$22        
4853: CD AF 3D   CALL    $3DAF           
4856: 21 80 C3   LD      HL,$C380        
4859: 09         ADD     HL,BC           
485A: 5E         LD      E,(HL)          
485B: 50         LD      D,B             
485C: 21 4A 48   LD      HL,$484A        
485F: 19         ADD     HL,DE           
4860: 7E         LD      A,(HL)          
4861: 21 40 C2   LD      HL,$C240        
4864: 09         ADD     HL,BC           
4865: 77         LD      (HL),A          
4866: CD 8D 3B   CALL    $3B8D           
4869: C9         RET                     
486A: E6 07      AND     $07             
486C: 20 04      JR      NZ,$4872        
486E: 3E 09      LD      A,$09           
4870: E0 F2      LDFF00  ($F2),A         
4872: CD AF 3D   CALL    $3DAF           
4875: F0 E7      LD      A,($E7)         
4877: 1F         RRA                     
4878: 1F         RRA                     
4879: 1F         RRA                     
487A: E6 01      AND     $01             
487C: C6 02      ADD     $02             
487E: CD 87 3B   CALL    $3B87           
4881: C9         RET                     
4882: CD 91 08   CALL    $0891           
4885: 20 07      JR      NZ,$488E        
4887: CD 8D 3B   CALL    $3B8D           
488A: CD 8D 3B   CALL    $3B8D           
488D: C9         RET                     
488E: 21 A0 C2   LD      HL,$C2A0        
4891: 09         ADD     HL,BC           
4892: 7E         LD      A,(HL)          
4893: E6 03      AND     $03             
4895: 28 27      JR      Z,$48BE         
4897: AF         XOR     A               
4898: EA 58 C1   LD      ($C158),A       
489B: 3E 20      LD      A,$20           
489D: EA 57 C1   LD      ($C157),A       
48A0: 3E 0B      LD      A,$0B           
48A2: E0 F2      LDFF00  ($F2),A         
48A4: 21 40 C2   LD      HL,$C240        
48A7: 09         ADD     HL,BC           
48A8: CB 2E      SET     1,E             
48AA: CB 2E      SET     1,E             
48AC: 7E         LD      A,(HL)          
48AD: 2F         CPL                     
48AE: 3C         INC     A               
48AF: 77         LD      (HL),A          
48B0: 21 20 C3   LD      HL,$C320        
48B3: 09         ADD     HL,BC           
48B4: 36 28      LD      (HL),$28        
48B6: CD 8D 3B   CALL    $3B8D           
48B9: CD 91 08   CALL    $0891           
48BC: 36 60      LD      (HL),$60        
48BE: F0 E7      LD      A,($E7)         
48C0: 1F         RRA                     
48C1: 1F         RRA                     
48C2: E6 01      AND     $01             
48C4: C6 04      ADD     $04             
48C6: CD 87 3B   CALL    $3B87           
48C9: 3E FF      LD      A,$FF           
48CB: EA 28 D2   LD      ($D228),A       
48CE: C9         RET                     
48CF: 00         NOP                     
48D0: FE FD      CP      $FD             
48D2: FE 00      CP      $00             
48D4: 02         LD      (BC),A          
48D5: 03         INC     BC              
48D6: 02         LD      (BC),A          
48D7: 00         NOP                     
48D8: 04         INC     B               
48D9: 08 0C 10   LD      ($100C),SP      
48DC: 0C         INC     C               
48DD: 08 04 21   LD      ($2104),SP      
48E0: 30 C4      JR      NC,$48A6        
48E2: 09         ADD     HL,BC           
48E3: CB B6      SET     1,E             
48E5: 21 40 C3   LD      HL,$C340        
48E8: 09         ADD     HL,BC           
48E9: CB FE      SET     1,E             
48EB: CD 91 08   CALL    $0891           
48EE: 20 10      JR      NZ,$4900        
48F0: 36 40      LD      (HL),$40        
48F2: CD 8D 3B   CALL    $3B8D           
48F5: CD 8D 3B   CALL    $3B8D           
48F8: 3E 00      LD      A,$00           
48FA: EA 28 D2   LD      ($D228),A       
48FD: C3 87 3B   JP      $3B87           
4900: F0 E8      LD      A,($E8)         
4902: A7         AND     A               
4903: 28 03      JR      Z,$4908         
4905: CD AF 3D   CALL    $3DAF           
4908: F0 E7      LD      A,($E7)         
490A: 1F         RRA                     
490B: 1F         RRA                     
490C: 1F         RRA                     
490D: E6 01      AND     $01             
490F: C6 0C      ADD     $0C             
4911: CD 87 3B   CALL    $3B87           
4914: FA C0 C3   LD      A,($C3C0)       
4917: 5F         LD      E,A             
4918: 50         LD      D,B             
4919: 21 30 C0   LD      HL,$C030        
491C: 19         ADD     HL,DE           
491D: F0 E7      LD      A,($E7)         
491F: 1F         RRA                     
4920: 1F         RRA                     
4921: 1F         RRA                     
4922: E6 07      AND     $07             
4924: CD 2C 49   CALL    $492C           
4927: 3E 02      LD      A,$02           
4929: C3 D0 3D   JP      $3DD0           
492C: CD 38 49   CALL    $4938           
492F: F0 E7      LD      A,($E7)         
4931: 1F         RRA                     
4932: 1F         RRA                     
4933: 1F         RRA                     
4934: C6 04      ADD     $04             
4936: E6 07      AND     $07             
4938: C5         PUSH    BC              
4939: E5         PUSH    HL              
493A: 5F         LD      E,A             
493B: 16 00      LD      D,$00           
493D: 21 CF 48   LD      HL,$48CF        
4940: 19         ADD     HL,DE           
4941: 46         LD      B,(HL)          
4942: 21 D7 48   LD      HL,$48D7        
4945: 19         ADD     HL,DE           
4946: 4E         LD      C,(HL)          
4947: E1         POP     HL              
4948: F0 EC      LD      A,($EC)         
494A: 80         ADD     A,B             
494B: C6 F6      ADD     $F6             
494D: 22         LD      (HLI),A         
494E: F0 EE      LD      A,($EE)         
4950: 81         ADD     A,C             
4951: C6 FC      ADD     $FC             
4953: 22         LD      (HLI),A         
4954: 36 24      LD      (HL),$24        
4956: 23         INC     HL              
4957: 36 00      LD      (HL),$00        
4959: 23         INC     HL              
495A: C1         POP     BC              
495B: C9         RET                     
495C: 21 40 C2   LD      HL,$C240        
495F: 09         ADD     HL,BC           
4960: 7E         LD      A,(HL)          
4961: E6 FE      AND     $FE             
4963: 20 0B      JR      NZ,$4970        
4965: CD AF 3D   CALL    $3DAF           
4968: CD 91 08   CALL    $0891           
496B: 36 40      LD      (HL),$40        
496D: C3 8D 3B   JP      $3B8D           
4970: 21 40 C2   LD      HL,$C240        
4973: 09         ADD     HL,BC           
4974: 7E         LD      A,(HL)          
4975: E6 80      AND     $80             
4977: 28 04      JR      Z,$497D         
4979: 34         INC     (HL)            
497A: 34         INC     (HL)            
497B: 34         INC     (HL)            
497C: 34         INC     (HL)            
497D: 35         DEC     (HL)            
497E: 35         DEC     (HL)            
497F: 3E 00      LD      A,$00           
4981: EA 28 D2   LD      ($D228),A       
4984: CD 87 3B   CALL    $3B87           
4987: C9         RET                     
4988: CD AF 3D   CALL    $3DAF           
498B: CD 91 08   CALL    $0891           
498E: 20 11      JR      NZ,$49A1        
4990: CD 87 08   CALL    $0887           
4993: CD ED 27   CALL    $27ED           
4996: E6 1F      AND     $1F             
4998: C6 20      ADD     $20             
499A: 77         LD      (HL),A          
499B: CD 8D 3B   CALL    $3B8D           
499E: 36 02      LD      (HL),$02        
49A0: C9         RET                     
49A1: F0 E7      LD      A,($E7)         
49A3: 1F         RRA                     
49A4: 1F         RRA                     
49A5: 1F         RRA                     
49A6: 1F         RRA                     
49A7: E6 01      AND     $01             
49A9: EA 27 D2   LD      ($D227),A       
49AC: C9         RET                     
49AD: CD 8D 3B   CALL    $3B8D           
49B0: CD 91 08   CALL    $0891           
49B3: 36 60      LD      (HL),$60        
49B5: 21 40 C2   LD      HL,$C240        
49B8: 09         ADD     HL,BC           
49B9: 7E         LD      A,(HL)          
49BA: E0 9A      LDFF00  ($9A),A         
49BC: 3E 28      LD      A,$28           
49BE: EA 3E C1   LD      ($C13E),A       
49C1: 3E 40      LD      A,$40           
49C3: EA C7 DB   LD      ($DBC7),A       
49C6: FA 94 DB   LD      A,($DB94)       
49C9: C6 08      ADD     $08             
49CB: EA 94 DB   LD      ($DB94),A       
49CE: 3E 0B      LD      A,$0B           
49D0: E0 F2      LDFF00  ($F2),A         
49D2: C9         RET                     
49D3: CD AF 3D   CALL    $3DAF           
49D6: CD 91 08   CALL    $0891           
49D9: 20 03      JR      NZ,$49DE        
49DB: C3 90 49   JP      $4990           
49DE: FE 40      CP      $40             
49E0: 3E 00      LD      A,$00           
49E2: 30 09      JR      NC,$49ED        
49E4: F0 E7      LD      A,($E7)         
49E6: 1F         RRA                     
49E7: 1F         RRA                     
49E8: 1F         RRA                     
49E9: 1F         RRA                     
49EA: 1F         RRA                     
49EB: E6 01      AND     $01             
49ED: CD 87 3B   CALL    $3B87           
49F0: EA 28 D2   LD      ($D228),A       
49F3: CD 4B 47   CALL    $474B           
49F6: C9         RET                     
49F7: F8 FC      LDHL    SP,$FC          
49F9: 54         LD      D,H             
49FA: 20 F8      JR      NZ,$49F4        
49FC: 04         INC     B               
49FD: 52         LD      D,D             
49FE: 20 F8      JR      NZ,$49F8        
4A00: 0C         INC     C               
4A01: 50         LD      D,B             
4A02: 20 F7      JR      NZ,$49FB        
4A04: FC                              
4A05: 54         LD      D,H             
4A06: 20 F7      JR      NZ,$49FF        
4A08: 04         INC     B               
4A09: 52         LD      D,D             
4A0A: 20 F7      JR      NZ,$4A03        
4A0C: 0C         INC     C               
4A0D: 50         LD      D,B             
4A0E: 20 F8      JR      NZ,$4A08        
4A10: FC                              
4A11: 50         LD      D,B             
4A12: 00         NOP                     
4A13: F8 04      LDHL    SP,$04          
4A15: 52         LD      D,D             
4A16: 00         NOP                     
4A17: F8 0C      LDHL    SP,$0C          
4A19: 54         LD      D,H             
4A1A: 00         NOP                     
4A1B: F7         RST     0X30            
4A1C: FC                              
4A1D: 50         LD      D,B             
4A1E: 00         NOP                     
4A1F: F7         RST     0X30            
4A20: 04         INC     B               
4A21: 52         LD      D,D             
4A22: 00         NOP                     
4A23: F7         RST     0X30            
4A24: 0C         INC     C               
4A25: 54         LD      D,H             
4A26: 00         NOP                     
4A27: 00         NOP                     
4A28: FC                              
4A29: 56         LD      D,(HL)          
4A2A: 00         NOP                     
4A2B: 00         NOP                     
4A2C: 04         INC     B               
4A2D: 58         LD      E,B             
4A2E: 00         NOP                     
4A2F: 00         NOP                     
4A30: 0C         INC     C               
4A31: 5A         LD      E,D             
4A32: 00         NOP                     
4A33: 00         NOP                     
4A34: FC                              
4A35: 5C         LD      E,H             
4A36: 00         NOP                     
4A37: 00         NOP                     
4A38: 04         INC     B               
4A39: 58         LD      E,B             
4A3A: 00         NOP                     
4A3B: 00         NOP                     
4A3C: 0C         INC     C               
4A3D: 5E         LD      E,(HL)          
4A3E: 00         NOP                     
4A3F: 00         NOP                     
4A40: FC                              
4A41: 5C         LD      E,H             
4A42: 00         NOP                     
4A43: 00         NOP                     
4A44: 04         INC     B               
4A45: 58         LD      E,B             
4A46: 00         NOP                     
4A47: 00         NOP                     
4A48: 0C         INC     C               
4A49: 5A         LD      E,D             
4A4A: 00         NOP                     
4A4B: 00         NOP                     
4A4C: FC                              
4A4D: 56         LD      D,(HL)          
4A4E: 00         NOP                     
4A4F: 00         NOP                     
4A50: 04         INC     B               
4A51: 58         LD      E,B             
4A52: 00         NOP                     
4A53: 00         NOP                     
4A54: 0C         INC     C               
4A55: 5E         LD      E,(HL)          
4A56: 00         NOP                     
4A57: 00         NOP                     
4A58: FC                              
4A59: 70         LD      (HL),B          
4A5A: 00         NOP                     
4A5B: 00         NOP                     
4A5C: 04         INC     B               
4A5D: 72         LD      (HL),D          
4A5E: 00         NOP                     
4A5F: 00         NOP                     
4A60: 0C         INC     C               
4A61: 74         LD      (HL),H          
4A62: 00         NOP                     
4A63: 01 FC 70   LD      BC,$70FC        
4A66: 00         NOP                     
4A67: 00         NOP                     
4A68: 04         INC     B               
4A69: 76         HALT                    
4A6A: 00         NOP                     
4A6B: 00         NOP                     
4A6C: 0C         INC     C               
4A6D: 78         LD      A,B             
4A6E: 00         NOP                     
4A6F: 00         NOP                     
4A70: FC                              
4A71: 5A         LD      E,D             
4A72: 20 00      JR      NZ,$4A74        
4A74: 04         INC     B               
4A75: 58         LD      E,B             
4A76: 20 00      JR      NZ,$4A78        
4A78: 0C         INC     C               
4A79: 56         LD      D,(HL)          
4A7A: 20 00      JR      NZ,$4A7C        
4A7C: FC                              
4A7D: 5E         LD      E,(HL)          
4A7E: 20 00      JR      NZ,$4A80        
4A80: 04         INC     B               
4A81: 58         LD      E,B             
4A82: 20 00      JR      NZ,$4A84        
4A84: 0C         INC     C               
4A85: 5C         LD      E,H             
4A86: 20 00      JR      NZ,$4A88        
4A88: FC                              
4A89: 5A         LD      E,D             
4A8A: 20 00      JR      NZ,$4A8C        
4A8C: 04         INC     B               
4A8D: 58         LD      E,B             
4A8E: 20 00      JR      NZ,$4A90        
4A90: 0C         INC     C               
4A91: 5C         LD      E,H             
4A92: 20 00      JR      NZ,$4A94        
4A94: FC                              
4A95: 5E         LD      E,(HL)          
4A96: 20 00      JR      NZ,$4A98        
4A98: 04         INC     B               
4A99: 58         LD      E,B             
4A9A: 20 00      JR      NZ,$4A9C        
4A9C: 0C         INC     C               
4A9D: 56         LD      D,(HL)          
4A9E: 20 00      JR      NZ,$4AA0        
4AA0: FC                              
4AA1: 74         LD      (HL),H          
4AA2: 20 00      JR      NZ,$4AA4        
4AA4: 04         INC     B               
4AA5: 72         LD      (HL),D          
4AA6: 20 00      JR      NZ,$4AA8        
4AA8: 0C         INC     C               
4AA9: 70         LD      (HL),B          
4AAA: 20 00      JR      NZ,$4AAC        
4AAC: FC                              
4AAD: 78         LD      A,B             
4AAE: 20 00      JR      NZ,$4AB0        
4AB0: 04         INC     B               
4AB1: 76         HALT                    
4AB2: 20 01      JR      NZ,$4AB5        
4AB4: 0C         INC     C               
4AB5: 70         LD      (HL),B          
4AB6: 20 00      JR      NZ,$4AB8        
4AB8: FC                              
4AB9: 7A         LD      A,D             
4ABA: 00         NOP                     
4ABB: 00         NOP                     
4ABC: 04         INC     B               
4ABD: 7C         LD      A,H             
4ABE: 00         NOP                     
4ABF: 00         NOP                     
4AC0: 0C         INC     C               
4AC1: 7E         LD      A,(HL)          
4AC2: 00         NOP                     
4AC3: 00         NOP                     
4AC4: FC                              
4AC5: 7E         LD      A,(HL)          
4AC6: 20 00      JR      NZ,$4AC8        
4AC8: 04         INC     B               
4AC9: 7C         LD      A,H             
4ACA: 20 00      JR      NZ,$4ACC        
4ACC: 0C         INC     C               
4ACD: 7A         LD      A,D             
4ACE: 20 0C      JR      NZ,$4ADC        
4AD0: FF         RST     0X38            
4AD1: 26 00      LD      H,$00           
4AD3: 0C         INC     C               
4AD4: 04         INC     B               
4AD5: 26 00      LD      H,$00           
4AD7: 0C         INC     C               
4AD8: 09         ADD     HL,BC           
4AD9: 26 00      LD      H,$00           
4ADB: FA 27 D2   LD      A,($D227)       
4ADE: CB 27      SET     1,E             
4AE0: 5F         LD      E,A             
4AE1: FA 28 D2   LD      A,($D228)       
4AE4: FE FF      CP      $FF             
4AE6: 28 15      JR      Z,$4AFD         
4AE8: 83         ADD     A,E             
4AE9: 17         RLA                     
4AEA: 17         RLA                     
4AEB: E6 FC      AND     $FC             
4AED: 5F         LD      E,A             
4AEE: 17         RLA                     
4AEF: E6 F8      AND     $F8             
4AF1: 83         ADD     A,E             
4AF2: 5F         LD      E,A             
4AF3: 50         LD      D,B             
4AF4: 21 F7 49   LD      HL,$49F7        
4AF7: 19         ADD     HL,DE           
4AF8: 0E 03      LD      C,$03           
4AFA: CD 26 3D   CALL    $3D26           
4AFD: F0 F1      LD      A,($F1)         
4AFF: 17         RLA                     
4B00: 17         RLA                     
4B01: E6 FC      AND     $FC             
4B03: 5F         LD      E,A             
4B04: 17         RLA                     
4B05: E6 F8      AND     $F8             
4B07: 83         ADD     A,E             
4B08: 5F         LD      E,A             
4B09: 50         LD      D,B             
4B0A: 21 27 4A   LD      HL,$4A27        
4B0D: 19         ADD     HL,DE           
4B0E: 0E 03      LD      C,$03           
4B10: CD 26 3D   CALL    $3D26           
4B13: 21 10 C3   LD      HL,$C310        
4B16: 09         ADD     HL,BC           
4B17: 7E         LD      A,(HL)          
4B18: A7         AND     A               
4B19: 28 0F      JR      Z,$4B2A         
4B1B: F0 EF      LD      A,($EF)         
4B1D: E0 EC      LDFF00  ($EC),A         
4B1F: 21 CF 4A   LD      HL,$4ACF        
4B22: 0E 03      LD      C,$03           
4B24: CD 26 3D   CALL    $3D26           
4B27: CD BA 3D   CALL    $3DBA           
4B2A: C9         RET                     
4B2B: E8 FE      ADD     SP,$FE          
4B2D: 74         LD      (HL),H          
4B2E: 00         NOP                     
4B2F: E8 06      ADD     SP,$06          
4B31: 74         LD      (HL),H          
4B32: 20 F4      JR      NZ,$4B28        
4B34: 01 76 00   LD      BC,$0076        
4B37: F4                              
4B38: 09         ADD     HL,BC           
4B39: 76         HALT                    
4B3A: 20 00      JR      NZ,$4B3C        
4B3C: 00         NOP                     
4B3D: 76         HALT                    
4B3E: 00         NOP                     
4B3F: 00         NOP                     
4B40: 08 76 20   LD      ($2076),SP      
4B43: E8 00      ADD     SP,$00          
4B45: 74         LD      (HL),H          
4B46: 00         NOP                     
4B47: E8 08      ADD     SP,$08          
4B49: 74         LD      (HL),H          
4B4A: 20 F4      JR      NZ,$4B40        
4B4C: 00         NOP                     
4B4D: 76         HALT                    
4B4E: 00         NOP                     
4B4F: F4                              
4B50: 08 76 20   LD      ($2076),SP      
4B53: 00         NOP                     
4B54: 00         NOP                     
4B55: 76         HALT                    
4B56: 00         NOP                     
4B57: 00         NOP                     
4B58: 08 76 20   LD      ($2076),SP      
4B5B: E8 02      ADD     SP,$02          
4B5D: 74         LD      (HL),H          
4B5E: 00         NOP                     
4B5F: E8 0A      ADD     SP,$0A          
4B61: 74         LD      (HL),H          
4B62: 20 F4      JR      NZ,$4B58        
4B64: FF         RST     0X38            
4B65: 76         HALT                    
4B66: 00         NOP                     
4B67: F4                              
4B68: 07         RLCA                    
4B69: 76         HALT                    
4B6A: 20 00      JR      NZ,$4B6C        
4B6C: 00         NOP                     
4B6D: 76         HALT                    
4B6E: 00         NOP                     
4B6F: 00         NOP                     
4B70: 08 76 20   LD      ($2076),SP      
4B73: E8 00      ADD     SP,$00          
4B75: 74         LD      (HL),H          
4B76: 00         NOP                     
4B77: E8 08      ADD     SP,$08          
4B79: 74         LD      (HL),H          
4B7A: 20 F4      JR      NZ,$4B70        
4B7C: 00         NOP                     
4B7D: 76         HALT                    
4B7E: 00         NOP                     
4B7F: F4                              
4B80: 08 76 20   LD      ($2076),SP      
4B83: 00         NOP                     
4B84: 00         NOP                     
4B85: 76         HALT                    
4B86: 00         NOP                     
4B87: 00         NOP                     
4B88: 08 76 20   LD      ($2076),SP      
4B8B: F4                              
4B8C: FF         RST     0X38            
4B8D: 74         LD      (HL),H          
4B8E: 00         NOP                     
4B8F: F4                              
4B90: 07         RLCA                    
4B91: 74         LD      (HL),H          
4B92: 20 00      JR      NZ,$4B94        
4B94: 00         NOP                     
4B95: 76         HALT                    
4B96: 00         NOP                     
4B97: 00         NOP                     
4B98: 08 76 20   LD      ($2076),SP      
4B9B: F4                              
4B9C: 00         NOP                     
4B9D: 74         LD      (HL),H          
4B9E: 00         NOP                     
4B9F: F4                              
4BA0: 08 74 20   LD      ($2074),SP      
4BA3: 00         NOP                     
4BA4: 00         NOP                     
4BA5: 76         HALT                    
4BA6: 00         NOP                     
4BA7: 00         NOP                     
4BA8: 08 76 20   LD      ($2076),SP      
4BAB: F4                              
4BAC: 01 74 00   LD      BC,$0074        
4BAF: F4                              
4BB0: 09         ADD     HL,BC           
4BB1: 74         LD      (HL),H          
4BB2: 20 00      JR      NZ,$4BB4        
4BB4: 00         NOP                     
4BB5: 76         HALT                    
4BB6: 00         NOP                     
4BB7: 00         NOP                     
4BB8: 08 76 20   LD      ($2076),SP      
4BBB: F4                              
4BBC: 00         NOP                     
4BBD: 74         LD      (HL),H          
4BBE: 00         NOP                     
4BBF: F4                              
4BC0: 08 74 20   LD      ($2074),SP      
4BC3: 00         NOP                     
4BC4: 00         NOP                     
4BC5: 76         HALT                    
4BC6: 00         NOP                     
4BC7: 00         NOP                     
4BC8: 08 76 20   LD      ($2076),SP      
4BCB: 00         NOP                     
4BCC: FF         RST     0X38            
4BCD: 74         LD      (HL),H          
4BCE: 00         NOP                     
4BCF: 00         NOP                     
4BD0: 07         RLCA                    
4BD1: 74         LD      (HL),H          
4BD2: 20 00      JR      NZ,$4BD4        
4BD4: 00         NOP                     
4BD5: 74         LD      (HL),H          
4BD6: 00         NOP                     
4BD7: 00         NOP                     
4BD8: 08 74 20   LD      ($2074),SP      
4BDB: 00         NOP                     
4BDC: 01 74 00   LD      BC,$0074        
4BDF: 00         NOP                     
4BE0: 09         ADD     HL,BC           
4BE1: 74         LD      (HL),H          
4BE2: 20 00      JR      NZ,$4BE4        
4BE4: 00         NOP                     
4BE5: 74         LD      (HL),H          
4BE6: 00         NOP                     
4BE7: 00         NOP                     
4BE8: 08 74 20   LD      ($2074),SP      
4BEB: FA FC 00   LD      A,($00FC)       
4BEE: 04         INC     B               
4BEF: 06 04      LD      B,$04           
4BF1: 00         NOP                     
4BF2: FC                              
4BF3: FA FC 21   LD      A,($21FC)       
4BF6: B0         OR      B               
4BF7: C2 09 7E   JP      NZ,$7E09        
4BFA: A7         AND     A               
4BFB: C2 EE 4C   JP      NZ,$4CEE        
4BFE: CD 9A 4C   CALL    $4C9A           
4C01: CD 20 7B   CALL    $7B20           
4C04: 21 D0 C3   LD      HL,$C3D0        
4C07: 09         ADD     HL,BC           
4C08: 7E         LD      A,(HL)          
4C09: FE 02      CP      $02             
4C0B: 30 50      JR      NC,$4C5D        
4C0D: 21 60 C3   LD      HL,$C360        
4C10: 09         ADD     HL,BC           
4C11: 36 02      LD      (HL),$02        
4C13: 21 20 C4   LD      HL,$C420        
4C16: 09         ADD     HL,BC           
4C17: 7E         LD      A,(HL)          
4C18: FE 14      CP      $14             
4C1A: 20 41      JR      NZ,$4C5D        
4C1C: 35         DEC     (HL)            
4C1D: 21 D0 C3   LD      HL,$C3D0        
4C20: 09         ADD     HL,BC           
4C21: 34         INC     (HL)            
4C22: 3E E3      LD      A,$E3           
4C24: CD 01 3C   CALL    $3C01           
4C27: 38 34      JR      C,$4C5D         
4C29: F0 D7      LD      A,($D7)         
4C2B: 21 00 C2   LD      HL,$C200        
4C2E: 19         ADD     HL,DE           
4C2F: 77         LD      (HL),A          
4C30: F0 D8      LD      A,($D8)         
4C32: 21 10 C2   LD      HL,$C210        
4C35: 19         ADD     HL,DE           
4C36: 77         LD      (HL),A          
4C37: 21 B0 C2   LD      HL,$C2B0        
4C3A: 19         ADD     HL,DE           
4C3B: 34         INC     (HL)            
4C3C: C5         PUSH    BC              
4C3D: D5         PUSH    DE              
4C3E: C1         POP     BC              
4C3F: 3E 20      LD      A,$20           
4C41: CD 30 3C   CALL    $3C30           
4C44: F0 D8      LD      A,($D8)         
4C46: 2F         CPL                     
4C47: 3C         INC     A               
4C48: 21 40 C2   LD      HL,$C240        
4C4B: 09         ADD     HL,BC           
4C4C: 77         LD      (HL),A          
4C4D: F0 D7      LD      A,($D7)         
4C4F: 2F         CPL                     
4C50: 3C         INC     A               
4C51: 21 50 C2   LD      HL,$C250        
4C54: 09         ADD     HL,BC           
4C55: 77         LD      (HL),A          
4C56: 21 E0 C2   LD      HL,$C2E0        
4C59: 09         ADD     HL,BC           
4C5A: 36 18      LD      (HL),$18        
4C5C: C1         POP     BC              
4C5D: CD E2 08   CALL    $08E2           
4C60: CD B4 3B   CALL    $3BB4           
4C63: F0 E7      LD      A,($E7)         
4C65: 1F         RRA                     
4C66: 1F         RRA                     
4C67: 1F         RRA                     
4C68: 00         NOP                     
4C69: E6 03      AND     $03             
4C6B: CD 87 3B   CALL    $3B87           
4C6E: CD 91 08   CALL    $0891           
4C71: 20 20      JR      NZ,$4C93        
4C73: CD ED 27   CALL    $27ED           
4C76: E6 3F      AND     $3F             
4C78: C6 30      ADD     $30             
4C7A: 77         LD      (HL),A          
4C7B: E6 07      AND     $07             
4C7D: 5F         LD      E,A             
4C7E: 50         LD      D,B             
4C7F: 21 ED 4B   LD      HL,$4BED        
4C82: 19         ADD     HL,DE           
4C83: 7E         LD      A,(HL)          
4C84: 21 40 C2   LD      HL,$C240        
4C87: 09         ADD     HL,BC           
4C88: 77         LD      (HL),A          
4C89: 21 EB 4B   LD      HL,$4BEB        
4C8C: 19         ADD     HL,DE           
4C8D: 7E         LD      A,(HL)          
4C8E: 21 50 C2   LD      HL,$C250        
4C91: 09         ADD     HL,BC           
4C92: 77         LD      (HL),A          
4C93: CD 8C 7B   CALL    $7B8C           
4C96: CD 9E 3B   CALL    $3B9E           
4C99: C9         RET                     
4C9A: 50         LD      D,B             
4C9B: 21 D0 C3   LD      HL,$C3D0        
4C9E: 09         ADD     HL,BC           
4C9F: 7E         LD      A,(HL)          
4CA0: A7         AND     A               
4CA1: 20 1B      JR      NZ,$4CBE        
4CA3: F0 F1      LD      A,($F1)         
4CA5: 17         RLA                     
4CA6: 17         RLA                     
4CA7: 17         RLA                     
4CA8: E6 F8      AND     $F8             
4CAA: 5F         LD      E,A             
4CAB: 17         RLA                     
4CAC: E6 F0      AND     $F0             
4CAE: 83         ADD     A,E             
4CAF: 5F         LD      E,A             
4CB0: 21 2B 4B   LD      HL,$4B2B        
4CB3: 19         ADD     HL,DE           
4CB4: 0E 06      LD      C,$06           
4CB6: CD 26 3D   CALL    $3D26           
4CB9: 3E 04      LD      A,$04           
4CBB: C3 D0 3D   JP      $3DD0           
4CBE: FE 02      CP      $02             
4CC0: 28 17      JR      Z,$4CD9         
4CC2: F0 F1      LD      A,($F1)         
4CC4: 17         RLA                     
4CC5: 17         RLA                     
4CC6: 17         RLA                     
4CC7: 17         RLA                     
4CC8: E6 F0      AND     $F0             
4CCA: 5F         LD      E,A             
4CCB: 21 8B 4B   LD      HL,$4B8B        
4CCE: 19         ADD     HL,DE           
4CCF: 0E 04      LD      C,$04           
4CD1: CD 26 3D   CALL    $3D26           
4CD4: 3E 02      LD      A,$02           
4CD6: C3 D0 3D   JP      $3DD0           
4CD9: F0 F1      LD      A,($F1)         
4CDB: 17         RLA                     
4CDC: 17         RLA                     
4CDD: 17         RLA                     
4CDE: E6 F8      AND     $F8             
4CE0: 5F         LD      E,A             
4CE1: 21 CB 4B   LD      HL,$4BCB        
4CE4: 19         ADD     HL,DE           
4CE5: 0E 02      LD      C,$02           
4CE7: C3 26 3D   JP      $3D26           
4CEA: 76         HALT                    
4CEB: 00         NOP                     
4CEC: 76         HALT                    
4CED: 20 11      JR      NZ,$4D00        
4CEF: EA 4C CD   LD      ($CD4C),A       
4CF2: 3B         DEC     SP              
4CF3: 3C         INC     A               
4CF4: CD 20 7B   CALL    $7B20           
4CF7: CD 42 7B   CALL    $7B42           
4CFA: CD 91 08   CALL    $0891           
4CFD: 20 03      JR      NZ,$4D02        
4CFF: CD B4 3B   CALL    $3BB4           
4D02: CD 8C 7B   CALL    $7B8C           
4D05: CD 9E 3B   CALL    $3B9E           
4D08: 21 A0 C2   LD      HL,$C2A0        
4D0B: 09         ADD     HL,BC           
4D0C: 7E         LD      A,(HL)          
4D0D: E6 03      AND     $03             
4D0F: 28 07      JR      Z,$4D18         
4D11: 21 40 C2   LD      HL,$C240        
4D14: CD 24 4D   CALL    $4D24           
4D17: D8         RET     C               
4D18: 21 A0 C2   LD      HL,$C2A0        
4D1B: 09         ADD     HL,BC           
4D1C: 7E         LD      A,(HL)          
4D1D: E6 0C      AND     $0C             
4D1F: 28 2D      JR      Z,$4D4E         
4D21: 21 50 C2   LD      HL,$C250        
4D24: 09         ADD     HL,BC           
4D25: 7E         LD      A,(HL)          
4D26: 2F         CPL                     
4D27: 3C         INC     A               
4D28: 77         LD      (HL),A          
4D29: 3E 09      LD      A,$09           
4D2B: E0 F2      LDFF00  ($F2),A         
4D2D: 21 D0 C3   LD      HL,$C3D0        
4D30: 09         ADD     HL,BC           
4D31: 7E         LD      A,(HL)          
4D32: 3C         INC     A               
4D33: 77         LD      (HL),A          
4D34: FE 03      CP      $03             
4D36: 38 16      JR      C,$4D4E         
4D38: F0 EE      LD      A,($EE)         
4D3A: E0 D7      LDFF00  ($D7),A         
4D3C: F0 EC      LD      A,($EC)         
4D3E: E0 D8      LDFF00  ($D8),A         
4D40: 3E 02      LD      A,$02           
4D42: CD 53 09   CALL    $0953           
4D45: 3E 2F      LD      A,$2F           
4D47: E0 F2      LDFF00  ($F2),A         
4D49: CD 35 7C   CALL    $7C35           
4D4C: 37         SCF                     
4D4D: C9         RET                     
4D4E: A7         AND     A               
4D4F: C9         RET                     
4D50: 70         LD      (HL),B          
4D51: 00         NOP                     
4D52: 70         LD      (HL),B          
4D53: 20 72      JR      NZ,$4DC7        
4D55: 00         NOP                     
4D56: 72         LD      (HL),D          
4D57: 20 21      JR      NZ,$4D7A        
4D59: B0         OR      B               
4D5A: C2 09 7E   JP      NZ,$7E09        
4D5D: A7         AND     A               
4D5E: C2 CA 4D   JP      NZ,$4DCA        
4D61: 11 50 4D   LD      DE,$4D50        
4D64: CD 3B 3C   CALL    $3C3B           
4D67: CD 8C 08   CALL    $088C           
4D6A: 1E 00      LD      E,$00           
4D6C: A7         AND     A               
4D6D: 28 01      JR      Z,$4D70         
4D6F: 1C         INC     E               
4D70: 7B         LD      A,E             
4D71: CD 87 3B   CALL    $3B87           
4D74: CD 20 7B   CALL    $7B20           
4D77: 21 D0 C3   LD      HL,$C3D0        
4D7A: 09         ADD     HL,BC           
4D7B: 34         INC     (HL)            
4D7C: 7E         LD      A,(HL)          
4D7D: E6 0F      AND     $0F             
4D7F: 20 30      JR      NZ,$4DB1        
4D81: CD 8C 08   CALL    $088C           
4D84: 36 08      LD      (HL),$08        
4D86: 3E E2      LD      A,$E2           
4D88: CD 01 3C   CALL    $3C01           
4D8B: D8         RET     C               
4D8C: 3E 12      LD      A,$12           
4D8E: E0 F4      LDFF00  ($F4),A         
4D90: F0 D7      LD      A,($D7)         
4D92: 21 00 C2   LD      HL,$C200        
4D95: 19         ADD     HL,DE           
4D96: 77         LD      (HL),A          
4D97: F0 D8      LD      A,($D8)         
4D99: 21 10 C2   LD      HL,$C210        
4D9C: 19         ADD     HL,DE           
4D9D: C6 04      ADD     $04             
4D9F: 77         LD      (HL),A          
4DA0: 21 B0 C2   LD      HL,$C2B0        
4DA3: 19         ADD     HL,DE           
4DA4: 34         INC     (HL)            
4DA5: 21 50 C2   LD      HL,$C250        
4DA8: 19         ADD     HL,DE           
4DA9: 36 10      LD      (HL),$10        
4DAB: 21 E0 C2   LD      HL,$C2E0        
4DAE: 19         ADD     HL,DE           
4DAF: 36 30      LD      (HL),$30        
4DB1: C9         RET                     
4DB2: 78         LD      A,B             
4DB3: 00         NOP                     
4DB4: 78         LD      A,B             
4DB5: 20 76      JR      NZ,$4E2D        
4DB7: 00         NOP                     
4DB8: 76         HALT                    
4DB9: 20 74      JR      NZ,$4E2F        
4DBB: 00         NOP                     
4DBC: 74         LD      (HL),H          
4DBD: 20 7A      JR      NZ,$4E39        
4DBF: 00         NOP                     
4DC0: 7C         LD      A,H             
4DC1: 00         NOP                     
4DC2: 7C         LD      A,H             
4DC3: 20 7A      JR      NZ,$4E3F        
4DC5: 20 FC      JR      NZ,$4DC3        
4DC7: 04         INC     B               
4DC8: F4                              
4DC9: 0C         INC     C               
4DCA: FE 02      CP      $02             
4DCC: CA 77 4E   JP      Z,$4E77         
4DCF: F0 E7      LD      A,($E7)         
4DD1: 17         RLA                     
4DD2: 17         RLA                     
4DD3: E6 10      AND     $10             
4DD5: E0 ED      LDFF00  ($ED),A         
4DD7: 11 B2 4D   LD      DE,$4DB2        
4DDA: CD 3B 3C   CALL    $3C3B           
4DDD: CD 20 7B   CALL    $7B20           
4DE0: CD E2 08   CALL    $08E2           
4DE3: CD EB 3B   CALL    $3BEB           
4DE6: FA C7 DB   LD      A,($DBC7)       
4DE9: F5         PUSH    AF              
4DEA: CD D5 3B   CALL    $3BD5           
4DED: F1         POP     AF              
4DEE: 5F         LD      E,A             
4DEF: FA C7 DB   LD      A,($DBC7)       
4DF2: BB         CP      E               
4DF3: 28 12      JR      Z,$4E07         
4DF5: FE 20      CP      $20             
4DF7: 38 0E      JR      C,$4E07         
4DF9: 3E 1F      LD      A,$1F           
4DFB: EA C7 DB   LD      ($DBC7),A       
4DFE: 3E 30      LD      A,$30           
4E00: CD 30 3C   CALL    $3C30           
4E03: F0 D7      LD      A,($D7)         
4E05: E0 9B      LDFF00  ($9B),A         
4E07: CD 8F 7B   CALL    $7B8F           
4E0A: F0 F0      LD      A,($F0)         
4E0C: A7         AND     A               
4E0D: 28 4F      JR      Z,$4E5E         
4E0F: AF         XOR     A               
4E10: E0 E8      LDFF00  ($E8),A         
4E12: 3E E2      LD      A,$E2           
4E14: CD 01 3C   CALL    $3C01           
4E17: 38 42      JR      C,$4E5B         
4E19: 21 B0 C2   LD      HL,$C2B0        
4E1C: 19         ADD     HL,DE           
4E1D: 36 02      LD      (HL),$02        
4E1F: C5         PUSH    BC              
4E20: F0 E8      LD      A,($E8)         
4E22: 4F         LD      C,A             
4E23: 21 B0 C3   LD      HL,$C3B0        
4E26: 19         ADD     HL,DE           
4E27: 77         LD      (HL),A          
4E28: 21 C6 4D   LD      HL,$4DC6        
4E2B: 09         ADD     HL,BC           
4E2C: F0 D7      LD      A,($D7)         
4E2E: 86         ADD     A,(HL)          
4E2F: 21 00 C2   LD      HL,$C200        
4E32: 19         ADD     HL,DE           
4E33: 77         LD      (HL),A          
4E34: 21 C8 4D   LD      HL,$4DC8        
4E37: 09         ADD     HL,BC           
4E38: 7E         LD      A,(HL)          
4E39: 21 40 C2   LD      HL,$C240        
4E3C: 19         ADD     HL,DE           
4E3D: 77         LD      (HL),A          
4E3E: F0 D8      LD      A,($D8)         
4E40: C6 00      ADD     $00             
4E42: 21 10 C2   LD      HL,$C210        
4E45: 19         ADD     HL,DE           
4E46: 77         LD      (HL),A          
4E47: 21 50 C2   LD      HL,$C250        
4E4A: 19         ADD     HL,DE           
4E4B: 36 0C      LD      (HL),$0C        
4E4D: 21 E0 C2   LD      HL,$C2E0        
4E50: 19         ADD     HL,DE           
4E51: 36 20      LD      (HL),$20        
4E53: C1         POP     BC              
4E54: F0 E8      LD      A,($E8)         
4E56: 3C         INC     A               
4E57: FE 02      CP      $02             
4E59: 38 B5      JR      C,$4E10         
4E5B: C3 35 7C   JP      $7C35           
4E5E: CD 91 08   CALL    $0891           
4E61: CA 35 7C   JP      Z,$7C35         
4E64: 21 B0 C3   LD      HL,$C3B0        
4E67: 09         ADD     HL,BC           
4E68: FE 10      CP      $10             
4E6A: 28 04      JR      Z,$4E70         
4E6C: FE 20      CP      $20             
4E6E: 20 06      JR      NZ,$4E76        
4E70: 7E         LD      A,(HL)          
4E71: FE 02      CP      $02             
4E73: 28 01      JR      Z,$4E76         
4E75: 34         INC     (HL)            
4E76: C9         RET                     
4E77: F0 E7      LD      A,($E7)         
4E79: 17         RLA                     
4E7A: 17         RLA                     
4E7B: E6 10      AND     $10             
4E7D: E0 ED      LDFF00  ($ED),A         
4E7F: 11 BE 4D   LD      DE,$4DBE        
4E82: CD 3B 3C   CALL    $3C3B           
4E85: CD 20 7B   CALL    $7B20           
4E88: CD 8C 7B   CALL    $7B8C           
4E8B: CD 91 08   CALL    $0891           
4E8E: CA 35 7C   JP      Z,$7C35         
4E91: C9         RET                     
4E92: 4A         LD      C,D             
4E93: 00         NOP                     
4E94: 4C         LD      C,H             
4E95: 00         NOP                     
4E96: 4C         LD      C,H             
4E97: 20 4A      JR      NZ,$4EE3        
4E99: 20 4E      JR      NZ,$4EE9        
4E9B: 00         NOP                     
4E9C: 4E         LD      C,(HL)          
4E9D: 20 00      JR      NZ,$4E9F        
4E9F: 06 FA      LD      B,$FA           
4EA1: FA 06 48   LD      A,($4806)       
4EA4: 00         NOP                     
4EA5: 48         LD      C,B             
4EA6: 60         LD      H,B             
4EA7: 48         LD      C,B             
4EA8: 40         LD      B,B             
4EA9: 48         LD      C,B             
4EAA: 20 21      JR      NZ,$4ECD        
4EAC: B0         OR      B               
4EAD: C2 09 7E   JP      NZ,$7E09        
4EB0: A7         AND     A               
4EB1: 28 50      JR      Z,$4F03         
4EB3: 11 A3 4E   LD      DE,$4EA3        
4EB6: CD 3B 3C   CALL    $3C3B           
4EB9: CD 20 7B   CALL    $7B20           
4EBC: F0 E7      LD      A,($E7)         
4EBE: 1F         RRA                     
4EBF: 1F         RRA                     
4EC0: 1F         RRA                     
4EC1: E6 01      AND     $01             
4EC3: CD 87 3B   CALL    $3B87           
4EC6: CD 8C 7B   CALL    $7B8C           
4EC9: CD 9E 3B   CALL    $3B9E           
4ECC: 21 A0 C2   LD      HL,$C2A0        
4ECF: 09         ADD     HL,BC           
4ED0: 7E         LD      A,(HL)          
4ED1: A7         AND     A               
4ED2: C2 E0 4E   JP      NZ,$4EE0        
4ED5: CD B4 3B   CALL    $3BB4           
4ED8: 21 10 C4   LD      HL,$C410        
4EDB: 09         ADD     HL,BC           
4EDC: 7E         LD      A,(HL)          
4EDD: A7         AND     A               
4EDE: 28 14      JR      Z,$4EF4         
4EE0: F0 EE      LD      A,($EE)         
4EE2: E0 D7      LDFF00  ($D7),A         
4EE4: F0 EC      LD      A,($EC)         
4EE6: E0 D8      LDFF00  ($D8),A         
4EE8: 3E 07      LD      A,$07           
4EEA: E0 F2      LDFF00  ($F2),A         
4EEC: 3E 05      LD      A,$05           
4EEE: CD 53 09   CALL    $0953           
4EF1: C3 35 7C   JP      $7C35           
4EF4: F0 EE      LD      A,($EE)         
4EF6: FE A8      CP      $A8             
4EF8: D2 35 7C   JP      NC,$7C35        
4EFB: F0 EC      LD      A,($EC)         
4EFD: FE 84      CP      $84             
4EFF: D2 35 7C   JP      NC,$7C35        
4F02: C9         RET                     
4F03: 11 92 4E   LD      DE,$4E92        
4F06: CD 3B 3C   CALL    $3C3B           
4F09: CD 20 7B   CALL    $7B20           
4F0C: CD 42 7B   CALL    $7B42           
4F0F: CD 91 08   CALL    $0891           
4F12: 20 03      JR      NZ,$4F17        
4F14: CD B4 3B   CALL    $3BB4           
4F17: CD 8C 08   CALL    $088C           
4F1A: FE 01      CP      $01             
4F1C: 20 47      JR      NZ,$4F65        
4F1E: F0 F7      LD      A,($F7)         
4F20: FE 03      CP      $03             
4F22: D8         RET     C               
4F23: 3E 1E      LD      A,$1E           
4F25: CD 01 3C   CALL    $3C01           
4F28: D8         RET     C               
4F29: 3E 0A      LD      A,$0A           
4F2B: E0 F4      LDFF00  ($F4),A         
4F2D: 21 10 C4   LD      HL,$C410        
4F30: 19         ADD     HL,DE           
4F31: 70         LD      (HL),B          
4F32: 21 40 C3   LD      HL,$C340        
4F35: 19         ADD     HL,DE           
4F36: CB F6      SET     1,E             
4F38: CB E6      SET     1,E             
4F3A: 21 30 C4   LD      HL,$C430        
4F3D: 19         ADD     HL,DE           
4F3E: CB CE      SET     1,E             
4F40: CB E6      SET     1,E             
4F42: F0 D7      LD      A,($D7)         
4F44: 21 00 C2   LD      HL,$C200        
4F47: 19         ADD     HL,DE           
4F48: 77         LD      (HL),A          
4F49: F0 D8      LD      A,($D8)         
4F4B: 21 10 C2   LD      HL,$C210        
4F4E: 19         ADD     HL,DE           
4F4F: 77         LD      (HL),A          
4F50: F0 DA      LD      A,($DA)         
4F52: 21 10 C3   LD      HL,$C310        
4F55: 19         ADD     HL,DE           
4F56: 77         LD      (HL),A          
4F57: 21 B0 C2   LD      HL,$C2B0        
4F5A: 19         ADD     HL,DE           
4F5B: 34         INC     (HL)            
4F5C: C5         PUSH    BC              
4F5D: D5         PUSH    DE              
4F5E: C1         POP     BC              
4F5F: 3E 18      LD      A,$18           
4F61: CD 25 3C   CALL    $3C25           
4F64: C1         POP     BC              
4F65: 21 D0 C3   LD      HL,$C3D0        
4F68: 09         ADD     HL,BC           
4F69: 7E         LD      A,(HL)          
4F6A: C7         RST     0X00            
4F6B: 6F         LD      L,A             
4F6C: 4F         LD      C,A             
4F6D: 30 50      JR      NC,$4FBF        
4F6F: CD 8C 7B   CALL    $7B8C           
4F72: CD 9E 3B   CALL    $3B9E           
4F75: F0 CC      LD      A,($CC)         
4F77: E6 30      AND     $30             
4F79: 28 48      JR      Z,$4FC3         
4F7B: CD DF 7B   CALL    $7BDF           
4F7E: C6 24      ADD     $24             
4F80: FE 48      CP      $48             
4F82: 30 3F      JR      NC,$4FC3        
4F84: CD EF 7B   CALL    $7BEF           
4F87: C6 24      ADD     $24             
4F89: FE 48      CP      $48             
4F8B: 30 36      JR      NC,$4FC3        
4F8D: CD 91 08   CALL    $0891           
4F90: 36 08      LD      (HL),$08        
4F92: CD 8C 08   CALL    $088C           
4F95: 70         LD      (HL),B          
4F96: 21 D0 C3   LD      HL,$C3D0        
4F99: 09         ADD     HL,BC           
4F9A: 34         INC     (HL)            
4F9B: 21 20 C3   LD      HL,$C320        
4F9E: 09         ADD     HL,BC           
4F9F: 36 15      LD      (HL),$15        
4FA1: 3E 24      LD      A,$24           
4FA3: E0 F2      LDFF00  ($F2),A         
4FA5: 3E 12      LD      A,$12           
4FA7: CD 30 3C   CALL    $3C30           
4FAA: F0 D7      LD      A,($D7)         
4FAC: 2F         CPL                     
4FAD: 3C         INC     A               
4FAE: 21 50 C2   LD      HL,$C250        
4FB1: 09         ADD     HL,BC           
4FB2: 77         LD      (HL),A          
4FB3: F0 D8      LD      A,($D8)         
4FB5: 2F         CPL                     
4FB6: 3C         INC     A               
4FB7: 21 40 C2   LD      HL,$C240        
4FBA: 09         ADD     HL,BC           
4FBB: 77         LD      (HL),A          
4FBC: 21 B0 C3   LD      HL,$C3B0        
4FBF: 09         ADD     HL,BC           
4FC0: 36 02      LD      (HL),$02        
4FC2: C9         RET                     
4FC3: 21 A0 C2   LD      HL,$C2A0        
4FC6: 09         ADD     HL,BC           
4FC7: 7E         LD      A,(HL)          
4FC8: E6 03      AND     $03             
4FCA: 20 0F      JR      NZ,$4FDB        
4FCC: 7E         LD      A,(HL)          
4FCD: E6 0C      AND     $0C             
4FCF: 28 12      JR      Z,$4FE3         
4FD1: 21 50 C2   LD      HL,$C250        
4FD4: 09         ADD     HL,BC           
4FD5: 7E         LD      A,(HL)          
4FD6: EE F0      XOR     $F0             
4FD8: 77         LD      (HL),A          
4FD9: 18 08      JR      $4FE3           
4FDB: 21 40 C2   LD      HL,$C240        
4FDE: 09         ADD     HL,BC           
4FDF: 7E         LD      A,(HL)          
4FE0: EE F0      XOR     $F0             
4FE2: 77         LD      (HL),A          
4FE3: 21 90 C2   LD      HL,$C290        
4FE6: 09         ADD     HL,BC           
4FE7: 7E         LD      A,(HL)          
4FE8: A7         AND     A               
4FE9: 20 07      JR      NZ,$4FF2        
4FEB: CD ED 27   CALL    $27ED           
4FEE: E6 2F      AND     $2F             
4FF0: 20 2D      JR      NZ,$501F        
4FF2: AF         XOR     A               
4FF3: 21 50 C2   LD      HL,$C250        
4FF6: 09         ADD     HL,BC           
4FF7: 77         LD      (HL),A          
4FF8: CD ED 27   CALL    $27ED           
4FFB: E6 03      AND     $03             
4FFD: 5F         LD      E,A             
4FFE: 50         LD      D,B             
4FFF: 21 9E 4E   LD      HL,$4E9E        
5002: 19         ADD     HL,DE           
5003: 7E         LD      A,(HL)          
5004: 21 40 C2   LD      HL,$C240        
5007: 09         ADD     HL,BC           
5008: 77         LD      (HL),A          
5009: A7         AND     A               
500A: 20 13      JR      NZ,$501F        
500C: CD ED 27   CALL    $27ED           
500F: E6 01      AND     $01             
5011: C6 03      ADD     $03             
5013: 5F         LD      E,A             
5014: 50         LD      D,B             
5015: 21 9E 4E   LD      HL,$4E9E        
5018: 19         ADD     HL,DE           
5019: 7E         LD      A,(HL)          
501A: 21 50 C2   LD      HL,$C250        
501D: 09         ADD     HL,BC           
501E: 77         LD      (HL),A          
501F: 21 90 C2   LD      HL,$C290        
5022: 09         ADD     HL,BC           
5023: AF         XOR     A               
5024: 77         LD      (HL),A          
5025: F0 E7      LD      A,($E7)         
5027: 1F         RRA                     
5028: 1F         RRA                     
5029: 1F         RRA                     
502A: E6 01      AND     $01             
502C: CD 87 3B   CALL    $3B87           
502F: C9         RET                     
5030: CD 8C 7B   CALL    $7B8C           
5033: 21 10 C4   LD      HL,$C410        
5036: 09         ADD     HL,BC           
5037: 7E         LD      A,(HL)          
5038: E5         PUSH    HL              
5039: 36 01      LD      (HL),$01        
503B: CD 9E 3B   CALL    $3B9E           
503E: E1         POP     HL              
503F: 70         LD      (HL),B          
5040: CD C5 7B   CALL    $7BC5           
5043: 21 20 C3   LD      HL,$C320        
5046: 09         ADD     HL,BC           
5047: 35         DEC     (HL)            
5048: 21 10 C3   LD      HL,$C310        
504B: 09         ADD     HL,BC           
504C: 7E         LD      A,(HL)          
504D: E6 80      AND     $80             
504F: 28 1C      JR      Z,$506D         
5051: 70         LD      (HL),B          
5052: 21 20 C3   LD      HL,$C320        
5055: 09         ADD     HL,BC           
5056: 70         LD      (HL),B          
5057: 21 50 C2   LD      HL,$C250        
505A: 09         ADD     HL,BC           
505B: 36 08      LD      (HL),$08        
505D: 21 40 C2   LD      HL,$C240        
5060: 09         ADD     HL,BC           
5061: 36 08      LD      (HL),$08        
5063: 21 D0 C3   LD      HL,$C3D0        
5066: 09         ADD     HL,BC           
5067: 70         LD      (HL),B          
5068: CD 8C 08   CALL    $088C           
506B: 36 10      LD      (HL),$10        
506D: C9         RET                     
506E: EA EB EA   LD      ($EAEB),A       
5071: EB                              
5072: EC                              
5073: ED                              
5074: EE EF      XOR     $EF             
5076: F0 F1      LD      A,($F1)         
5078: F2                              
5079: F3         DI                      
507A: FA 19 D2   LD      A,($D219)       
507D: 17         RLA                     
507E: E6 FE      AND     $FE             
5080: 5F         LD      E,A             
5081: 50         LD      D,B             
5082: 21 6E 50   LD      HL,$506E        
5085: 19         ADD     HL,DE           
5086: 2A         LD      A,(HLI)         
5087: EA 95 C1   LD      ($C195),A       
508A: 7E         LD      A,(HL)          
508B: EA 96 C1   LD      ($C196),A       
508E: 3E 01      LD      A,$01           
5090: E0 91      LDFF00  ($91),A         
5092: EA 0E C1   LD      ($C10E),A       
5095: C9         RET                     
5096: FA 24 C1   LD      A,($C124)       
5099: A7         AND     A               
509A: 20 0D      JR      NZ,$50A9        
509C: FA 16 C1   LD      A,($C116)       
509F: A7         AND     A               
50A0: 20 07      JR      NZ,$50A9        
50A2: 3C         INC     A               
50A3: EA 16 C1   LD      ($C116),A       
50A6: CD 7A 50   CALL    $507A           
50A9: 21 90 C3   LD      HL,$C390        
50AC: 09         ADD     HL,BC           
50AD: 7E         LD      A,(HL)          
50AE: FE 02      CP      $02             
50B0: CA D0 45   JP      Z,$45D0         
50B3: A7         AND     A               
50B4: C2 D0 54   JP      NZ,$54D0        
50B7: FA 19 D2   LD      A,($D219)       
50BA: C7         RST     0X00            
50BB: C7         RST     0X00            
50BC: 50         LD      D,B             
50BD: FE 51      CP      $51             
50BF: 41         LD      B,C             
50C0: 57         LD      D,A             
50C1: E4                              
50C2: 5F         LD      E,A             
50C3: D8         RET     C               
50C4: 63         LD      H,E             
50C5: 4A         LD      C,D             
50C6: 6E         LD      L,(HL)          
50C7: F0 F0      LD      A,($F0)         
50C9: C7         RST     0X00            
50CA: D8         RET     C               
50CB: 50         LD      D,B             
50CC: 35         DEC     (HL)            
50CD: 51         LD      D,C             
50CE: 50         LD      D,B             
50CF: 51         LD      D,C             
50D0: 6C         LD      L,H             
50D1: 51         LD      D,C             
50D2: 89         ADC     A,C             
50D3: 51         LD      D,C             
50D4: AD         XOR     L               
50D5: 51         LD      D,C             
50D6: D3                              
50D7: 51         LD      D,C             
50D8: FA 46 C1   LD      A,($C146)       
50DB: A7         AND     A               
50DC: 20 56      JR      NZ,$5134        
50DE: 3E 5D      LD      A,$5D           
50E0: EA 68 D3   LD      ($D368),A       
50E3: 21 74 DA   LD      HL,$DA74        
50E6: CB F6      SET     1,E             
50E8: 3E F5      LD      A,$F5           
50EA: CD 97 21   CALL    $2197           
50ED: CD 91 08   CALL    $0891           
50F0: 36 50      LD      (HL),$50        
50F2: F0 98      LD      A,($98)         
50F4: 21 00 C2   LD      HL,$C200        
50F7: 09         ADD     HL,BC           
50F8: 77         LD      (HL),A          
50F9: 1E 80      LD      E,$80           
50FB: 21 00 D0   LD      HL,$D000        
50FE: 22         LD      (HLI),A         
50FF: 1D         DEC     E               
5100: 20 FC      JR      NZ,$50FE        
5102: F0 99      LD      A,($99)         
5104: 21 10 C2   LD      HL,$C210        
5107: 09         ADD     HL,BC           
5108: 77         LD      (HL),A          
5109: 1E 80      LD      E,$80           
510B: 21 00 D1   LD      HL,$D100        
510E: 22         LD      (HLI),A         
510F: 1D         DEC     E               
5110: 20 FC      JR      NZ,$510E        
5112: AF         XOR     A               
5113: EA 1A D2   LD      ($D21A),A       
5116: EA 1B D2   LD      ($D21B),A       
5119: EA 1C D2   LD      ($D21C),A       
511C: EA 1D D2   LD      ($D21D),A       
511F: EA 1E D2   LD      ($D21E),A       
5122: EA 1F D2   LD      ($D21F),A       
5125: EA 20 D2   LD      ($D220),A       
5128: EA 21 D2   LD      ($D221),A       
512B: EA 22 D2   LD      ($D222),A       
512E: EA 23 D2   LD      ($D223),A       
5131: CD 8D 3B   CALL    $3B8D           
5134: C9         RET                     
5135: CD 2D 56   CALL    $562D           
5138: CD 91 08   CALL    $0891           
513B: 20 08      JR      NZ,$5145        
513D: CD 8D 3B   CALL    $3B8D           
5140: 3E 35      LD      A,$35           
5142: E0 F2      LDFF00  ($F2),A         
5144: C9         RET                     
5145: FE 30      CP      $30             
5147: 20 06      JR      NZ,$514F        
5149: 35         DEC     (HL)            
514A: 3E 23      LD      A,$23           
514C: EA 68 D3   LD      ($D368),A       
514F: C9         RET                     
5150: CD 2D 56   CALL    $562D           
5153: CD 20 7B   CALL    $7B20           
5156: 21 50 C2   LD      HL,$C250        
5159: 09         ADD     HL,BC           
515A: 35         DEC     (HL)            
515B: 7E         LD      A,(HL)          
515C: FE E8      CP      $E8             
515E: 20 08      JR      NZ,$5168        
5160: CD 91 08   CALL    $0891           
5163: 36 08      LD      (HL),$08        
5165: CD 8D 3B   CALL    $3B8D           
5168: CD 8F 7B   CALL    $7B8F           
516B: C9         RET                     
516C: CD 2D 56   CALL    $562D           
516F: CD 20 7B   CALL    $7B20           
5172: CD 8F 7B   CALL    $7B8F           
5175: CD 91 08   CALL    $0891           
5178: C0         RET     NZ              
5179: 21 50 C2   LD      HL,$C250        
517C: 09         ADD     HL,BC           
517D: 34         INC     (HL)            
517E: 20 08      JR      NZ,$5188        
5180: CD 91 08   CALL    $0891           
5183: 36 80      LD      (HL),$80        
5185: CD 8D 3B   CALL    $3B8D           
5188: C9         RET                     
5189: CD 2D 56   CALL    $562D           
518C: CD 91 08   CALL    $0891           
518F: 28 0E      JR      Z,$519F         
5191: E6 07      AND     $07             
5193: 20 0A      JR      NZ,$519F        
5195: 21 B0 C3   LD      HL,$C3B0        
5198: 09         ADD     HL,BC           
5199: 7E         LD      A,(HL)          
519A: FE 05      CP      $05             
519C: 28 02      JR      Z,$51A0         
519E: 34         INC     (HL)            
519F: C9         RET                     
51A0: CD 91 08   CALL    $0891           
51A3: 36 C0      LD      (HL),$C0        
51A5: CD 8D 3B   CALL    $3B8D           
51A8: C9         RET                     
51A9: 06 05      LD      B,$05           
51AB: 07         RLCA                    
51AC: 05         DEC     B               
51AD: CD 9B 56   CALL    $569B           
51B0: F0 E7      LD      A,($E7)         
51B2: 1F         RRA                     
51B3: 1F         RRA                     
51B4: 1F         RRA                     
51B5: 1F         RRA                     
51B6: E6 03      AND     $03             
51B8: 5F         LD      E,A             
51B9: 50         LD      D,B             
51BA: 21 A9 51   LD      HL,$51A9        
51BD: 19         ADD     HL,DE           
51BE: 7E         LD      A,(HL)          
51BF: CD 87 3B   CALL    $3B87           
51C2: CD 91 08   CALL    $0891           
51C5: 20 05      JR      NZ,$51CC        
51C7: 36 2F      LD      (HL),$2F        
51C9: CD 8D 3B   CALL    $3B8D           
51CC: C9         RET                     
51CD: 08 00 01   LD      ($0100),SP      
51D0: 02         LD      (BC),A          
51D1: 03         INC     BC              
51D2: 04         INC     B               
51D3: CD 9B 56   CALL    $569B           
51D6: CD 91 08   CALL    $0891           
51D9: 20 13      JR      NZ,$51EE        
51DB: 21 19 D2   LD      HL,$D219        
51DE: 34         INC     (HL)            
51DF: AF         XOR     A               
51E0: CD 87 3B   CALL    $3B87           
51E3: CD 8D 3B   CALL    $3B8D           
51E6: 70         LD      (HL),B          
51E7: 21 40 C3   LD      HL,$C340        
51EA: 09         ADD     HL,BC           
51EB: CB BE      SET     1,E             
51ED: C9         RET                     
51EE: 1F         RRA                     
51EF: 1F         RRA                     
51F0: 1F         RRA                     
51F1: E6 0F      AND     $0F             
51F3: 5F         LD      E,A             
51F4: 50         LD      D,B             
51F5: 21 CD 51   LD      HL,$51CD        
51F8: 19         ADD     HL,DE           
51F9: 7E         LD      A,(HL)          
51FA: CD 87 3B   CALL    $3B87           
51FD: C9         RET                     
51FE: CD 28 57   CALL    $5728           
5201: CD 20 7B   CALL    $7B20           
5204: CD E2 08   CALL    $08E2           
5207: F0 F0      LD      A,($F0)         
5209: C7         RST     0X00            
520A: 1E 52      LD      E,$52           
520C: 2B         DEC     HL              
520D: 52         LD      D,D             
520E: 4F         LD      C,A             
520F: 52         LD      D,D             
5210: AE         XOR     (HL)            
5211: 52         LD      D,D             
5212: CF         RST     0X08            
5213: 52         LD      D,D             
5214: DD                              
5215: 52         LD      D,D             
5216: 9A         SBC     D               
5217: 53         LD      D,E             
5218: 0B         DEC     BC              
5219: 54         LD      D,H             
521A: 40         LD      B,B             
521B: 53         LD      D,E             
521C: 5A         LD      E,D             
521D: 53         LD      D,E             
521E: CD 91 08   CALL    $0891           
5221: 36 80      LD      (HL),$80        
5223: 21 D0 C3   LD      HL,$C3D0        
5226: 09         ADD     HL,BC           
5227: 70         LD      (HL),B          
5228: C3 8D 3B   JP      $3B8D           
522B: CD 91 08   CALL    $0891           
522E: 20 1E      JR      NZ,$524E        
5230: F0 E7      LD      A,($E7)         
5232: E6 07      AND     $07             
5234: 20 18      JR      NZ,$524E        
5236: 21 B0 C3   LD      HL,$C3B0        
5239: 09         ADD     HL,BC           
523A: 34         INC     (HL)            
523B: 7E         LD      A,(HL)          
523C: FE 03      CP      $03             
523E: 20 0E      JR      NZ,$524E        
5240: 21 20 C3   LD      HL,$C320        
5243: 09         ADD     HL,BC           
5244: 36 28      LD      (HL),$28        
5246: 3E 08      LD      A,$08           
5248: CD 25 3C   CALL    $3C25           
524B: CD 8D 3B   CALL    $3B8D           
524E: C9         RET                     
524F: CD 5F 54   CALL    $545F           
5252: CD B4 3B   CALL    $3BB4           
5255: CD 8C 7B   CALL    $7B8C           
5258: CD 9E 3B   CALL    $3B9E           
525B: CD C5 7B   CALL    $7BC5           
525E: 21 20 C3   LD      HL,$C320        
5261: 09         ADD     HL,BC           
5262: 35         DEC     (HL)            
5263: 35         DEC     (HL)            
5264: 21 10 C3   LD      HL,$C310        
5267: 09         ADD     HL,BC           
5268: 7E         LD      A,(HL)          
5269: E6 80      AND     $80             
526B: 28 30      JR      Z,$529D         
526D: 70         LD      (HL),B          
526E: 21 20 C3   LD      HL,$C320        
5271: 09         ADD     HL,BC           
5272: 70         LD      (HL),B          
5273: 21 D0 C3   LD      HL,$C3D0        
5276: 09         ADD     HL,BC           
5277: 7E         LD      A,(HL)          
5278: 3C         INC     A               
5279: 77         LD      (HL),A          
527A: E6 01      AND     $01             
527C: 20 13      JR      NZ,$5291        
527E: CD ED 27   CALL    $27ED           
5281: E6 01      AND     $01             
5283: 20 0C      JR      NZ,$5291        
5285: CD 91 08   CALL    $0891           
5288: 36 1F      LD      (HL),$1F        
528A: CD 8D 3B   CALL    $3B8D           
528D: 36 08      LD      (HL),$08        
528F: 18 0C      JR      $529D           
5291: 3E 20      LD      A,$20           
5293: E0 F2      LDFF00  ($F2),A         
5295: CD 91 08   CALL    $0891           
5298: 36 30      LD      (HL),$30        
529A: CD 8D 3B   CALL    $3B8D           
529D: 1E 03      LD      E,$03           
529F: 21 10 C3   LD      HL,$C310        
52A2: 09         ADD     HL,BC           
52A3: 7E         LD      A,(HL)          
52A4: FE 0C      CP      $0C             
52A6: 38 01      JR      C,$52A9         
52A8: 1C         INC     E               
52A9: 7B         LD      A,E             
52AA: CD 87 3B   CALL    $3B87           
52AD: C9         RET                     
52AE: 3E 05      LD      A,$05           
52B0: CD 87 3B   CALL    $3B87           
52B3: CD 91 08   CALL    $0891           
52B6: 20 10      JR      NZ,$52C8        
52B8: 3E 0C      LD      A,$0C           
52BA: CD 25 3C   CALL    $3C25           
52BD: 21 20 C3   LD      HL,$C320        
52C0: 09         ADD     HL,BC           
52C1: 36 20      LD      (HL),$20        
52C3: CD 8D 3B   CALL    $3B8D           
52C6: 35         DEC     (HL)            
52C7: 35         DEC     (HL)            
52C8: CD 5F 54   CALL    $545F           
52CB: CD B4 3B   CALL    $3BB4           
52CE: C9         RET                     
52CF: CD 91 08   CALL    $0891           
52D2: 20 03      JR      NZ,$52D7        
52D4: C3 5F 53   JP      $535F           
52D7: C9         RET                     
52D8: 3E 23      LD      A,$23           
52DA: E0 F3      LDFF00  ($F3),A         
52DC: C9         RET                     
52DD: CD 91 08   CALL    $0891           
52E0: 20 44      JR      NZ,$5326        
52E2: FA 19 D2   LD      A,($D219)       
52E5: 3C         INC     A               
52E6: EA 19 D2   LD      ($D219),A       
52E9: CD 7A 50   CALL    $507A           
52EC: AF         XOR     A               
52ED: EA 21 D2   LD      ($D221),A       
52F0: EA 22 D2   LD      ($D222),A       
52F3: EA 23 D2   LD      ($D223),A       
52F6: EA 20 D2   LD      ($D220),A       
52F9: 21 10 C3   LD      HL,$C310        
52FC: 09         ADD     HL,BC           
52FD: 70         LD      (HL),B          
52FE: 21 40 C3   LD      HL,$C340        
5301: 09         ADD     HL,BC           
5302: 36 C0      LD      (HL),$C0        
5304: 3E 02      LD      A,$02           
5306: EA 97 C1   LD      ($C197),A       
5309: 3C         INC     A               
530A: EA 0D C1   LD      ($C10D),A       
530D: 3E FF      LD      A,$FF           
530F: CD 87 3B   CALL    $3B87           
5312: CD 91 08   CALL    $0891           
5315: 36 40      LD      (HL),$40        
5317: 21 B0 C2   LD      HL,$C2B0        
531A: 09         ADD     HL,BC           
531B: 70         LD      (HL),B          
531C: CD 8D 3B   CALL    $3B8D           
531F: 70         LD      (HL),B          
5320: 3E 01      LD      A,$01           
5322: EA 1A D2   LD      ($D21A),A       
5325: C9         RET                     
5326: FE 18      CP      $18             
5328: 30 11      JR      NC,$533B        
532A: FE 17      CP      $17             
532C: 20 05      JR      NZ,$5333        
532E: 21 F2 FF   LD      HL,$FFF2        
5331: 36 35      LD      (HL),$35        
5333: 1F         RRA                     
5334: 1F         RRA                     
5335: 1F         RRA                     
5336: E6 03      AND     $03             
5338: CD 87 3B   CALL    $3B87           
533B: C9         RET                     
533C: FF         RST     0X38            
533D: 00         NOP                     
533E: 01 02 CD   LD      BC,$CD02        
5341: 91         SUB     C               
5342: 08 20 05   LD      ($0520),SP      
5345: 36 80      LD      (HL),$80        
5347: C3 8D 3B   JP      $3B8D           
534A: 1F         RRA                     
534B: 1F         RRA                     
534C: 1F         RRA                     
534D: E6 03      AND     $03             
534F: 5F         LD      E,A             
5350: 50         LD      D,B             
5351: 21 3C 53   LD      HL,$533C        
5354: 19         ADD     HL,DE           
5355: 7E         LD      A,(HL)          
5356: CD 87 3B   CALL    $3B87           
5359: C9         RET                     
535A: CD 91 08   CALL    $0891           
535D: 20 20      JR      NZ,$537F        
535F: CD ED 27   CALL    $27ED           
5362: E6 07      AND     $07             
5364: 5F         LD      E,A             
5365: 50         LD      D,B             
5366: 21 13 59   LD      HL,$5913        
5369: 19         ADD     HL,DE           
536A: 7E         LD      A,(HL)          
536B: 21 00 C2   LD      HL,$C200        
536E: 09         ADD     HL,BC           
536F: 77         LD      (HL),A          
5370: 21 1B 59   LD      HL,$591B        
5373: 19         ADD     HL,DE           
5374: 7E         LD      A,(HL)          
5375: 21 10 C2   LD      HL,$C210        
5378: 09         ADD     HL,BC           
5379: 77         LD      (HL),A          
537A: CD 8D 3B   CALL    $3B8D           
537D: 36 01      LD      (HL),$01        
537F: C9         RET                     
5380: 00         NOP                     
5381: 00         NOP                     
5382: 00         NOP                     
5383: 00         NOP                     
5384: 00         NOP                     
5385: 00         NOP                     
5386: 00         NOP                     
5387: 00         NOP                     
5388: 00         NOP                     
5389: 00         NOP                     
538A: 00         NOP                     
538B: 00         NOP                     
538C: 00         NOP                     
538D: 00         NOP                     
538E: 00         NOP                     
538F: 00         NOP                     
5390: 00         NOP                     
5391: 18 20      JR      $53B3           
5393: 18 00      JR      $5395           
5395: E8 E0      ADD     SP,$E0          
5397: E8 00      ADD     SP,$00          
5399: 18 3E      JR      $53D9           
539B: FF         RST     0X38            
539C: CD 87 3B   CALL    $3B87           
539F: CD 91 08   CALL    $0891           
53A2: 36 80      LD      (HL),$80        
53A4: CD 8D 3B   CALL    $3B8D           
53A7: 36 04      LD      (HL),$04        
53A9: 3E 21      LD      A,$21           
53AB: E0 F3      LDFF00  ($F3),A         
53AD: AF         XOR     A               
53AE: E0 E8      LDFF00  ($E8),A         
53B0: 3E E6      LD      A,$E6           
53B2: CD 01 3C   CALL    $3C01           
53B5: D8         RET     C               
53B6: C5         PUSH    BC              
53B7: F0 E8      LD      A,($E8)         
53B9: 4F         LD      C,A             
53BA: F0 D7      LD      A,($D7)         
53BC: 21 80 53   LD      HL,$5380        
53BF: 09         ADD     HL,BC           
53C0: 86         ADD     A,(HL)          
53C1: 21 00 C2   LD      HL,$C200        
53C4: 19         ADD     HL,DE           
53C5: 77         LD      (HL),A          
53C6: F0 D8      LD      A,($D8)         
53C8: 21 88 53   LD      HL,$5388        
53CB: 09         ADD     HL,BC           
53CC: 86         ADD     A,(HL)          
53CD: 21 10 C2   LD      HL,$C210        
53D0: 19         ADD     HL,DE           
53D1: 77         LD      (HL),A          
53D2: F0 DA      LD      A,($DA)         
53D4: 21 10 C3   LD      HL,$C310        
53D7: 19         ADD     HL,DE           
53D8: 77         LD      (HL),A          
53D9: 21 92 53   LD      HL,$5392        
53DC: 09         ADD     HL,BC           
53DD: 7E         LD      A,(HL)          
53DE: 21 40 C2   LD      HL,$C240        
53E1: 19         ADD     HL,DE           
53E2: 77         LD      (HL),A          
53E3: 21 90 53   LD      HL,$5390        
53E6: 09         ADD     HL,BC           
53E7: 7E         LD      A,(HL)          
53E8: 21 50 C2   LD      HL,$C250        
53EB: 19         ADD     HL,DE           
53EC: 77         LD      (HL),A          
53ED: 21 E0 C2   LD      HL,$C2E0        
53F0: 19         ADD     HL,DE           
53F1: 36 2F      LD      (HL),$2F        
53F3: 21 40 C3   LD      HL,$C340        
53F6: 19         ADD     HL,DE           
53F7: 36 C2      LD      (HL),$C2        
53F9: 21 90 C3   LD      HL,$C390        
53FC: 19         ADD     HL,DE           
53FD: 34         INC     (HL)            
53FE: C1         POP     BC              
53FF: F0 E8      LD      A,($E8)         
5401: 3C         INC     A               
5402: FE 08      CP      $08             
5404: 20 A8      JR      NZ,$53AE        
5406: C9         RET                     
5407: 05         DEC     B               
5408: 03         INC     BC              
5409: 04         INC     B               
540A: 03         INC     BC              
540B: CD C5 7B   CALL    $7BC5           
540E: 21 20 C3   LD      HL,$C320        
5411: 09         ADD     HL,BC           
5412: 35         DEC     (HL)            
5413: 35         DEC     (HL)            
5414: 21 10 C3   LD      HL,$C310        
5417: 09         ADD     HL,BC           
5418: 7E         LD      A,(HL)          
5419: E6 80      AND     $80             
541B: 28 06      JR      Z,$5423         
541D: 70         LD      (HL),B          
541E: 21 20 C3   LD      HL,$C320        
5421: 09         ADD     HL,BC           
5422: 70         LD      (HL),B          
5423: CD 91 08   CALL    $0891           
5426: 28 10      JR      Z,$5438         
5428: 1F         RRA                     
5429: 00         NOP                     
542A: 00         NOP                     
542B: 00         NOP                     
542C: E6 03      AND     $03             
542E: 5F         LD      E,A             
542F: 50         LD      D,B             
5430: 21 07 54   LD      HL,$5407        
5433: 19         ADD     HL,DE           
5434: 7E         LD      A,(HL)          
5435: C3 87 3B   JP      $3B87           
5438: FA 20 D2   LD      A,($D220)       
543B: 3C         INC     A               
543C: EA 20 D2   LD      ($D220),A       
543F: FE 03      CP      $03             
5441: 30 06      JR      NC,$5449        
5443: CD 8D 3B   CALL    $3B8D           
5446: 36 02      LD      (HL),$02        
5448: C9         RET                     
5449: 3E 06      LD      A,$06           
544B: CD 87 3B   CALL    $3B87           
544E: CD 91 08   CALL    $0891           
5451: 36 80      LD      (HL),$80        
5453: CD 8D 3B   CALL    $3B8D           
5456: 36 05      LD      (HL),$05        
5458: 3E 37      LD      A,$37           
545A: E0 F4      LDFF00  ($F4),A         
545C: C3 AD 53   JP      $53AD           
545F: 1E 0F      LD      E,$0F           
5461: 50         LD      D,B             
5462: 21 80 C2   LD      HL,$C280        
5465: 19         ADD     HL,DE           
5466: 7E         LD      A,(HL)          
5467: FE 05      CP      $05             
5469: 20 46      JR      NZ,$54B1        
546B: 21 A0 C3   LD      HL,$C3A0        
546E: 19         ADD     HL,DE           
546F: 7E         LD      A,(HL)          
5470: FE 08      CP      $08             
5472: 20 3D      JR      NZ,$54B1        
5474: 21 E0 C2   LD      HL,$C2E0        
5477: 19         ADD     HL,DE           
5478: 7E         LD      A,(HL)          
5479: FE 08      CP      $08             
547B: 20 34      JR      NZ,$54B1        
547D: 21 00 C2   LD      HL,$C200        
5480: 19         ADD     HL,DE           
5481: F0 EE      LD      A,($EE)         
5483: 96         SUB     (HL)            
5484: C6 0C      ADD     $0C             
5486: FE 18      CP      $18             
5488: 30 27      JR      NC,$54B1        
548A: 21 10 C2   LD      HL,$C210        
548D: 19         ADD     HL,DE           
548E: F0 EC      LD      A,($EC)         
5490: 96         SUB     (HL)            
5491: C6 0C      ADD     $0C             
5493: FE 18      CP      $18             
5495: 30 1A      JR      NC,$54B1        
5497: 21 20 C4   LD      HL,$C420        
549A: 09         ADD     HL,BC           
549B: 36 14      LD      (HL),$14        
549D: 3E 07      LD      A,$07           
549F: E0 F3      LDFF00  ($F3),A         
54A1: 3E 37      LD      A,$37           
54A3: E0 F2      LDFF00  ($F2),A         
54A5: CD 8D 3B   CALL    $3B8D           
54A8: 36 07      LD      (HL),$07        
54AA: CD 91 08   CALL    $0891           
54AD: 36 80      LD      (HL),$80        
54AF: F1         POP     AF              
54B0: C9         RET                     
54B1: 1D         DEC     E               
54B2: 7B         LD      A,E             
54B3: FE FF      CP      $FF             
54B5: 20 AB      JR      NZ,$5462        
54B7: C9         RET                     
54B8: 4E         LD      C,(HL)          
54B9: 00         NOP                     
54BA: 4E         LD      C,(HL)          
54BB: 20 4C      JR      NZ,$5509        
54BD: 00         NOP                     
54BE: 4C         LD      C,H             
54BF: 20 4A      JR      NZ,$550B        
54C1: 00         NOP                     
54C2: 4A         LD      C,D             
54C3: 20 02      JR      NZ,$54C7        
54C5: 02         LD      (BC),A          
54C6: 02         LD      (BC),A          
54C7: 01 01 00   LD      BC,$0001        
54CA: 0F         RRCA                    
54CB: 07         RLCA                    
54CC: 03         INC     BC              
54CD: 01 00 00   LD      BC,$0000        
54D0: 11 B8 54   LD      DE,$54B8        
54D3: CD 3B 3C   CALL    $3C3B           
54D6: CD 20 7B   CALL    $7B20           
54D9: CD 91 08   CALL    $0891           
54DC: CA 35 7C   JP      Z,$7C35         
54DF: 1F         RRA                     
54E0: 1F         RRA                     
54E1: 1F         RRA                     
54E2: E6 07      AND     $07             
54E4: 5F         LD      E,A             
54E5: 50         LD      D,B             
54E6: 21 C4 54   LD      HL,$54C4        
54E9: 19         ADD     HL,DE           
54EA: D5         PUSH    DE              
54EB: 7E         LD      A,(HL)          
54EC: CD 87 3B   CALL    $3B87           
54EF: D1         POP     DE              
54F0: 21 CA 54   LD      HL,$54CA        
54F3: 19         ADD     HL,DE           
54F4: F0 E7      LD      A,($E7)         
54F6: A6         AND     (HL)            
54F7: 20 03      JR      NZ,$54FC        
54F9: CD 8C 7B   CALL    $7B8C           
54FC: C9         RET                     
54FD: 00         NOP                     
54FE: 00         NOP                     
54FF: 4C         LD      C,H             
5500: 00         NOP                     
5501: 00         NOP                     
5502: 08 4C 20   LD      ($204C),SP      
5505: 00         NOP                     
5506: 08 FF 20   LD      ($20FF),SP      
5509: 00         NOP                     
550A: 10 FF      STOP    $FF             
550C: 20 00      JR      NZ,$550E        
550E: F8 FF      LDHL    SP,$FF          
5510: 40         LD      B,B             
5511: 00         NOP                     
5512: 00         NOP                     
5513: FF         RST     0X38            
5514: 40         LD      B,B             
5515: 00         NOP                     
5516: 08 FF 60   LD      ($60FF),SP      
5519: 00         NOP                     
551A: 10 FF      STOP    $FF             
551C: 60         LD      H,B             
551D: 00         NOP                     
551E: 00         NOP                     
551F: 4E         LD      C,(HL)          
5520: 00         NOP                     
5521: 00         NOP                     
5522: 08 4E 20   LD      ($204E),SP      
5525: 00         NOP                     
5526: 08 FF 20   LD      ($20FF),SP      
5529: 00         NOP                     
552A: 10 FF      STOP    $FF             
552C: 20 00      JR      NZ,$552E        
552E: F8 FF      LDHL    SP,$FF          
5530: 40         LD      B,B             
5531: 00         NOP                     
5532: 00         NOP                     
5533: FF         RST     0X38            
5534: 40         LD      B,B             
5535: 00         NOP                     
5536: 08 FF 60   LD      ($60FF),SP      
5539: 00         NOP                     
553A: 10 FF      STOP    $FF             
553C: 60         LD      H,B             
553D: F8 F8      LDHL    SP,$F8          
553F: 7A         LD      A,D             
5540: 00         NOP                     
5541: F8 00      LDHL    SP,$00          
5543: 7C         LD      A,H             
5544: 00         NOP                     
5545: F8 08      LDHL    SP,$08          
5547: 7C         LD      A,H             
5548: 20 F8      JR      NZ,$5542        
554A: 10 7A      STOP    $7A             
554C: 20 08      JR      NZ,$5556        
554E: F8 7A      LDHL    SP,$7A          
5550: 40         LD      B,B             
5551: 08 00 7C   LD      ($7C00),SP      
5554: 40         LD      B,B             
5555: 08 08 7C   LD      ($7C08),SP      
5558: 60         LD      H,B             
5559: 08 10 7A   LD      ($7A10),SP      
555C: 60         LD      H,B             
555D: F8 F8      LDHL    SP,$F8          
555F: 76         HALT                    
5560: 00         NOP                     
5561: F8 00      LDHL    SP,$00          
5563: 78         LD      A,B             
5564: 00         NOP                     
5565: F8 08      LDHL    SP,$08          
5567: 78         LD      A,B             
5568: 20 F8      JR      NZ,$5562        
556A: 10 76      STOP    $76             
556C: 20 08      JR      NZ,$5576        
556E: F8 76      LDHL    SP,$76          
5570: 40         LD      B,B             
5571: 08 00 78   LD      ($7800),SP      
5574: 40         LD      B,B             
5575: 08 08 78   LD      ($7808),SP      
5578: 60         LD      H,B             
5579: 08 10 76   LD      ($7610),SP      
557C: 60         LD      H,B             
557D: F8 F8      LDHL    SP,$F8          
557F: 72         LD      (HL),D          
5580: 00         NOP                     
5581: F8 00      LDHL    SP,$00          
5583: 74         LD      (HL),H          
5584: 00         NOP                     
5585: F8 08      LDHL    SP,$08          
5587: 74         LD      (HL),H          
5588: 20 F8      JR      NZ,$5582        
558A: 10 72      STOP    $72             
558C: 20 08      JR      NZ,$5596        
558E: F8 72      LDHL    SP,$72          
5590: 40         LD      B,B             
5591: 08 00 74   LD      ($7400),SP      
5594: 40         LD      B,B             
5595: 08 08 74   LD      ($7408),SP      
5598: 60         LD      H,B             
5599: 08 10 72   LD      ($7210),SP      
559C: 60         LD      H,B             
559D: F8 F8      LDHL    SP,$F8          
559F: 66         LD      H,(HL)          
55A0: 00         NOP                     
55A1: F8 00      LDHL    SP,$00          
55A3: 68         LD      L,B             
55A4: 00         NOP                     
55A5: F8 08      LDHL    SP,$08          
55A7: 68         LD      L,B             
55A8: 20 F8      JR      NZ,$55A2        
55AA: 10 66      STOP    $66             
55AC: 20 08      JR      NZ,$55B6        
55AE: F8 66      LDHL    SP,$66          
55B0: 40         LD      B,B             
55B1: 08 00 6A   LD      ($6A00),SP      
55B4: 00         NOP                     
55B5: 08 08 6A   LD      ($6A08),SP      
55B8: 20 08      JR      NZ,$55C2        
55BA: 10 66      STOP    $66             
55BC: 60         LD      H,B             
55BD: F8 F8      LDHL    SP,$F8          
55BF: 60         LD      H,B             
55C0: 00         NOP                     
55C1: F8 00      LDHL    SP,$00          
55C3: 62         LD      H,D             
55C4: 00         NOP                     
55C5: F8 08      LDHL    SP,$08          
55C7: 62         LD      H,D             
55C8: 20 F8      JR      NZ,$55C2        
55CA: 10 60      STOP    $60             
55CC: 20 08      JR      NZ,$55D6        
55CE: F8 60      LDHL    SP,$60          
55D0: 40         LD      B,B             
55D1: 08 00 64   LD      ($6400),SP      
55D4: 00         NOP                     
55D5: 08 08 64   LD      ($6408),SP      
55D8: 20 08      JR      NZ,$55E2        
55DA: 10 60      STOP    $60             
55DC: 60         LD      H,B             
55DD: F8 F8      LDHL    SP,$F8          
55DF: 6C         LD      L,H             
55E0: 00         NOP                     
55E1: F8 00      LDHL    SP,$00          
55E3: 6E         LD      L,(HL)          
55E4: 00         NOP                     
55E5: F8 08      LDHL    SP,$08          
55E7: 6E         LD      L,(HL)          
55E8: 20 F8      JR      NZ,$55E2        
55EA: 10 6C      STOP    $6C             
55EC: 20 08      JR      NZ,$55F6        
55EE: F8 6C      LDHL    SP,$6C          
55F0: 40         LD      B,B             
55F1: 08 00 70   LD      ($7000),SP      
55F4: 00         NOP                     
55F5: 08 08 70   LD      ($7008),SP      
55F8: 20 08      JR      NZ,$5602        
55FA: 10 6C      STOP    $6C             
55FC: 60         LD      H,B             
55FD: 00         NOP                     
55FE: 00         NOP                     
55FF: 4A         LD      C,D             
5600: 00         NOP                     
5601: 00         NOP                     
5602: 08 4A 20   LD      ($204A),SP      
5605: 00         NOP                     
5606: 08 FF 20   LD      ($20FF),SP      
5609: 00         NOP                     
560A: 10 FF      STOP    $FF             
560C: 20 00      JR      NZ,$560E        
560E: F8 FF      LDHL    SP,$FF          
5610: 40         LD      B,B             
5611: 00         NOP                     
5612: 00         NOP                     
5613: FF         RST     0X38            
5614: 40         LD      B,B             
5615: 00         NOP                     
5616: 08 FF 60   LD      ($60FF),SP      
5619: 00         NOP                     
561A: 10 FF      STOP    $FF             
561C: 60         LD      H,B             
561D: 4C         LD      C,H             
561E: 00         NOP                     
561F: 4C         LD      C,H             
5620: 20 48      JR      NZ,$566A        
5622: 00         NOP                     
5623: 48         LD      C,B             
5624: 20 28      JR      NZ,$564E        
5626: 23         INC     HL              
5627: 1E 19      LD      E,$19           
5629: 14         INC     D               
562A: 0F         RRCA                    
562B: 0A         LD      A,(BC)          
562C: 05         DEC     B               
562D: 21 D0 C3   LD      HL,$C3D0        
5630: 09         ADD     HL,BC           
5631: 7E         LD      A,(HL)          
5632: E0 E9      LDFF00  ($E9),A         
5634: AF         XOR     A               
5635: E0 E8      LDFF00  ($E8),A         
5637: 5F         LD      E,A             
5638: 50         LD      D,B             
5639: 21 25 56   LD      HL,$5625        
563C: 19         ADD     HL,DE           
563D: F0 E9      LD      A,($E9)         
563F: 96         SUB     (HL)            
5640: E6 7F      AND     $7F             
5642: 5F         LD      E,A             
5643: 50         LD      D,B             
5644: 21 00 D0   LD      HL,$D000        
5647: 19         ADD     HL,DE           
5648: 7E         LD      A,(HL)          
5649: E0 EE      LDFF00  ($EE),A         
564B: 21 00 D1   LD      HL,$D100        
564E: 19         ADD     HL,DE           
564F: 7E         LD      A,(HL)          
5650: E0 EC      LDFF00  ($EC),A         
5652: 11 21 56   LD      DE,$5621        
5655: F0 E8      LD      A,($E8)         
5657: FE 00      CP      $00             
5659: 28 0C      JR      Z,$5667         
565B: 21 10 C2   LD      HL,$C210        
565E: 09         ADD     HL,BC           
565F: F0 EC      LD      A,($EC)         
5661: BE         CP      (HL)            
5662: 28 0E      JR      Z,$5672         
5664: 11 1D 56   LD      DE,$561D        
5667: AF         XOR     A               
5668: E0 F1      LDFF00  ($F1),A         
566A: CD 3B 3C   CALL    $3C3B           
566D: 3E 02      LD      A,$02           
566F: CD D0 3D   CALL    $3DD0           
5672: F0 E8      LD      A,($E8)         
5674: 3C         INC     A               
5675: FE 08      CP      $08             
5677: 20 BC      JR      NZ,$5635        
5679: CD BA 3D   CALL    $3DBA           
567C: CD 9B 56   CALL    $569B           
567F: CD 20 7B   CALL    $7B20           
5682: 21 D0 C3   LD      HL,$C3D0        
5685: 09         ADD     HL,BC           
5686: 7E         LD      A,(HL)          
5687: 34         INC     (HL)            
5688: E6 7F      AND     $7F             
568A: 5F         LD      E,A             
568B: 50         LD      D,B             
568C: F0 EC      LD      A,($EC)         
568E: 21 00 D1   LD      HL,$D100        
5691: 19         ADD     HL,DE           
5692: 77         LD      (HL),A          
5693: F0 EE      LD      A,($EE)         
5695: 21 00 D0   LD      HL,$D000        
5698: 19         ADD     HL,DE           
5699: 77         LD      (HL),A          
569A: C9         RET                     
569B: 21 B0 C3   LD      HL,$C3B0        
569E: 09         ADD     HL,BC           
569F: 7E         LD      A,(HL)          
56A0: 17         RLA                     
56A1: 17         RLA                     
56A2: 17         RLA                     
56A3: 17         RLA                     
56A4: 17         RLA                     
56A5: E6 E0      AND     $E0             
56A7: 5F         LD      E,A             
56A8: 50         LD      D,B             
56A9: 21 FD 54   LD      HL,$54FD        
56AC: 19         ADD     HL,DE           
56AD: 0E 08      LD      C,$08           
56AF: CD 26 3D   CALL    $3D26           
56B2: 3E 08      LD      A,$08           
56B4: CD D0 3D   CALL    $3DD0           
56B7: C9         RET                     
56B8: 00         NOP                     
56B9: 00         NOP                     
56BA: 4A         LD      C,D             
56BB: 00         NOP                     
56BC: 00         NOP                     
56BD: 08 4A 20   LD      ($204A),SP      
56C0: 00         NOP                     
56C1: 00         NOP                     
56C2: FF         RST     0X38            
56C3: 00         NOP                     
56C4: 00         NOP                     
56C5: 00         NOP                     
56C6: FF         RST     0X38            
56C7: 00         NOP                     
56C8: 00         NOP                     
56C9: 00         NOP                     
56CA: 4C         LD      C,H             
56CB: 00         NOP                     
56CC: 00         NOP                     
56CD: 08 4C 20   LD      ($204C),SP      
56D0: 00         NOP                     
56D1: 00         NOP                     
56D2: FF         RST     0X38            
56D3: 00         NOP                     
56D4: 00         NOP                     
56D5: 00         NOP                     
56D6: FF         RST     0X38            
56D7: 00         NOP                     
56D8: 00         NOP                     
56D9: 00         NOP                     
56DA: 4E         LD      C,(HL)          
56DB: 00         NOP                     
56DC: 00         NOP                     
56DD: 08 4E 20   LD      ($204E),SP      
56E0: 00         NOP                     
56E1: 00         NOP                     
56E2: FF         RST     0X38            
56E3: 00         NOP                     
56E4: 00         NOP                     
56E5: 00         NOP                     
56E6: FF         RST     0X38            
56E7: 20 F0      JR      NZ,$56D9        
56E9: 00         NOP                     
56EA: 5C         LD      E,H             
56EB: 00         NOP                     
56EC: F0 08      LD      A,($08)         
56EE: 5C         LD      E,H             
56EF: 20 00      JR      NZ,$56F1        
56F1: 00         NOP                     
56F2: 5E         LD      E,(HL)          
56F3: 00         NOP                     
56F4: 00         NOP                     
56F5: 08 5E 20   LD      ($205E),SP      
56F8: F0 00      LD      A,($00)         
56FA: 44         LD      B,H             
56FB: 00         NOP                     
56FC: F0 08      LD      A,($08)         
56FE: 44         LD      B,H             
56FF: 20 00      JR      NZ,$5701        
5701: 00         NOP                     
5702: 44         LD      B,H             
5703: 40         LD      B,B             
5704: 00         NOP                     
5705: 08 44 60   LD      ($6044),SP      
5708: 00         NOP                     
5709: FC                              
570A: 40         LD      B,B             
570B: 00         NOP                     
570C: 00         NOP                     
570D: 04         INC     B               
570E: 42         LD      B,D             
570F: 00         NOP                     
5710: 00         NOP                     
5711: 0C         INC     C               
5712: 40         LD      B,B             
5713: 20 00      JR      NZ,$5715        
5715: 00         NOP                     
5716: FF         RST     0X38            
5717: 00         NOP                     
5718: 00         NOP                     
5719: 00         NOP                     
571A: 48         LD      C,B             
571B: 00         NOP                     
571C: 00         NOP                     
571D: 08 48 20   LD      ($2048),SP      
5720: 00         NOP                     
5721: 00         NOP                     
5722: FF         RST     0X38            
5723: 00         NOP                     
5724: 00         NOP                     
5725: 00         NOP                     
5726: FF         RST     0X38            
5727: 20 F0      JR      NZ,$5719        
5729: F1         POP     AF              
572A: 17         RLA                     
572B: 17         RLA                     
572C: 17         RLA                     
572D: 17         RLA                     
572E: E6 F0      AND     $F0             
5730: 5F         LD      E,A             
5731: 50         LD      D,B             
5732: 21 B8 56   LD      HL,$56B8        
5735: 19         ADD     HL,DE           
5736: 0E 04      LD      C,$04           
5738: CD 26 3D   CALL    $3D26           
573B: 3E 04      LD      A,$04           
573D: CD D0 3D   CALL    $3DD0           
5740: C9         RET                     
5741: 21 40 C4   LD      HL,$C440        
5744: 09         ADD     HL,BC           
5745: 7E         LD      A,(HL)          
5746: FE 02      CP      $02             
5748: CA E0 5D   JP      Z,$5DE0         
574B: A7         AND     A               
574C: C2 F8 5D   JP      NZ,$5DF8        
574F: 79         LD      A,C             
5750: EA 01 D2   LD      ($D201),A       
5753: FA 1A D2   LD      A,($D21A)       
5756: A7         AND     A               
5757: 20 03      JR      NZ,$575C        
5759: CD 6E 5A   CALL    $5A6E           
575C: CD 20 7B   CALL    $7B20           
575F: CD 42 7B   CALL    $7B42           
5762: F0 F0      LD      A,($F0)         
5764: C7         RST     0X00            
5765: 79         LD      A,C             
5766: 57         LD      D,A             
5767: CE 57      ADC     $57             
5769: 0B         DEC     BC              
576A: 58         LD      E,B             
576B: 55         LD      D,L             
576C: 58         LD      E,B             
576D: EE 58      XOR     $58             
576F: 28 59      JR      Z,$57CA         
5771: 65         LD      H,L             
5772: 59         LD      E,C             
5773: BC         CP      H               
5774: 59         LD      E,C             
5775: 0A         LD      A,(BC)          
5776: 5A         LD      E,D             
5777: 25         DEC     H               
5778: 5A         LD      E,D             
5779: AF         XOR     A               
577A: CD 87 3B   CALL    $3B87           
577D: CD 28 57   CALL    $5728           
5780: F0 98      LD      A,($98)         
5782: F5         PUSH    AF              
5783: F0 99      LD      A,($99)         
5785: F5         PUSH    AF              
5786: 3E 50      LD      A,$50           
5788: E0 98      LDFF00  ($98),A         
578A: 3E 30      LD      A,$30           
578C: E0 99      LDFF00  ($99),A         
578E: 3E 10      LD      A,$10           
5790: CD 25 3C   CALL    $3C25           
5793: 21 99 FF   LD      HL,$FF99        
5796: F0 EC      LD      A,($EC)         
5798: 96         SUB     (HL)            
5799: C6 03      ADD     $03             
579B: FE 06      CP      $06             
579D: 30 16      JR      NC,$57B5        
579F: 21 98 FF   LD      HL,$FF98        
57A2: F0 EE      LD      A,($EE)         
57A4: 96         SUB     (HL)            
57A5: C6 03      ADD     $03             
57A7: FE 06      CP      $06             
57A9: 30 0A      JR      NC,$57B5        
57AB: CD 91 08   CALL    $0891           
57AE: 36 50      LD      (HL),$50        
57B0: CD 8D 3B   CALL    $3B8D           
57B3: 36 01      LD      (HL),$01        
57B5: F1         POP     AF              
57B6: E0 99      LDFF00  ($99),A         
57B8: F1         POP     AF              
57B9: E0 98      LDFF00  ($98),A         
57BB: CD 8C 7B   CALL    $7B8C           
57BE: C9         RET                     
57BF: 04         INC     B               
57C0: 03         INC     BC              
57C1: 02         LD      (BC),A          
57C2: 01 00 00   LD      BC,$0000        
57C5: 00         NOP                     
57C6: 00         NOP                     
57C7: 00         NOP                     
57C8: 00         NOP                     
57C9: 00         NOP                     
57CA: 00         NOP                     
57CB: 00         NOP                     
57CC: 00         NOP                     
57CD: 00         NOP                     
57CE: CD 91 08   CALL    $0891           
57D1: 28 11      JR      Z,$57E4         
57D3: 1F         RRA                     
57D4: 1F         RRA                     
57D5: 1F         RRA                     
57D6: E6 0F      AND     $0F             
57D8: 5F         LD      E,A             
57D9: 50         LD      D,B             
57DA: 21 BF 57   LD      HL,$57BF        
57DD: 19         ADD     HL,DE           
57DE: 7E         LD      A,(HL)          
57DF: E0 F1      LDFF00  ($F1),A         
57E1: C3 28 57   JP      $5728           
57E4: AF         XOR     A               
57E5: EA 1A D2   LD      ($D21A),A       
57E8: CD 19 58   CALL    $5819           
57EB: 21 10 C2   LD      HL,$C210        
57EE: 09         ADD     HL,BC           
57EF: 7E         LD      A,(HL)          
57F0: D6 08      SUB     $08             
57F2: 77         LD      (HL),A          
57F3: CD 91 08   CALL    $0891           
57F6: 36 40      LD      (HL),$40        
57F8: CD 8D 3B   CALL    $3B8D           
57FB: 21 D0 C2   LD      HL,$C2D0        
57FE: 09         ADD     HL,BC           
57FF: 7E         LD      A,(HL)          
5800: A7         AND     A               
5801: C0         RET     NZ              
5802: 34         INC     (HL)            
5803: CD D8 52   CALL    $52D8           
5806: C9         RET                     
5807: 0F         RRCA                    
5808: 0A         LD      A,(BC)          
5809: 05         DEC     B               
580A: 00         NOP                     
580B: CD 91 08   CALL    $0891           
580E: 20 09      JR      NZ,$5819        
5810: 3E 22      LD      A,$22           
5812: E0 F3      LDFF00  ($F3),A         
5814: 36 C0      LD      (HL),$C0        
5816: C3 8D 3B   JP      $3B8D           
5819: CD 0E 7C   CALL    $7C0E           
581C: 7B         LD      A,E             
581D: EA 1E D2   LD      ($D21E),A       
5820: 50         LD      D,B             
5821: 21 07 58   LD      HL,$5807        
5824: 19         ADD     HL,DE           
5825: 7E         LD      A,(HL)          
5826: 21 80 C3   LD      HL,$C380        
5829: 09         ADD     HL,BC           
582A: 77         LD      (HL),A          
582B: 21 80 C3   LD      HL,$C380        
582E: 09         ADD     HL,BC           
582F: 7E         LD      A,(HL)          
5830: 21 B0 C2   LD      HL,$C2B0        
5833: 09         ADD     HL,BC           
5834: 86         ADD     A,(HL)          
5835: CD 87 3B   CALL    $3B87           
5838: C9         RET                     
5839: 00         NOP                     
583A: 01 02 03   LD      BC,$0302        
583D: 03         INC     BC              
583E: 03         INC     BC              
583F: 03         INC     BC              
5840: 03         INC     BC              
5841: 02         LD      (BC),A          
5842: 02         LD      (BC),A          
5843: 02         LD      (BC),A          
5844: 02         LD      (BC),A          
5845: 01 01 01   LD      BC,$0101        
5848: 01 00 00   LD      BC,$0000        
584B: 00         NOP                     
584C: 00         NOP                     
584D: 18 E8      JR      $5837           
584F: 00         NOP                     
5850: 00         NOP                     
5851: 00         NOP                     
5852: 00         NOP                     
5853: F0 00      LD      A,($00)         
5855: CD 91 08   CALL    $0891           
5858: 20 67      JR      NZ,$58C1        
585A: EA 1D D2   LD      ($D21D),A       
585D: 36 50      LD      (HL),$50        
585F: 3E E6      LD      A,$E6           
5861: CD 01 3C   CALL    $3C01           
5864: 21 40 C4   LD      HL,$C440        
5867: 19         ADD     HL,DE           
5868: 34         INC     (HL)            
5869: C5         PUSH    BC              
586A: FA 1E D2   LD      A,($D21E)       
586D: 4F         LD      C,A             
586E: 21 4D 58   LD      HL,$584D        
5871: 09         ADD     HL,BC           
5872: F0 D7      LD      A,($D7)         
5874: 86         ADD     A,(HL)          
5875: 21 00 C2   LD      HL,$C200        
5878: 19         ADD     HL,DE           
5879: 77         LD      (HL),A          
587A: 21 51 58   LD      HL,$5851        
587D: 09         ADD     HL,BC           
587E: F0 D8      LD      A,($D8)         
5880: 86         ADD     A,(HL)          
5881: 21 10 C2   LD      HL,$C210        
5884: 19         ADD     HL,DE           
5885: 77         LD      (HL),A          
5886: 21 40 C3   LD      HL,$C340        
5889: 19         ADD     HL,DE           
588A: 36 42      LD      (HL),$42        
588C: 21 50 C3   LD      HL,$C350        
588F: 19         ADD     HL,DE           
5890: 72         LD      (HL),D          
5891: 3E 38      LD      A,$38           
5893: E0 F4      LDFF00  ($F4),A         
5895: FA 20 D2   LD      A,($D220)       
5898: FE 02      CP      $02             
589A: 38 1A      JR      C,$58B6         
589C: F0 98      LD      A,($98)         
589E: 21 E7 FF   LD      HL,$FFE7        
58A1: 86         ADD     A,(HL)          
58A2: E6 01      AND     $01             
58A4: 20 10      JR      NZ,$58B6        
58A6: 21 90 C2   LD      HL,$C290        
58A9: 19         ADD     HL,DE           
58AA: 36 03      LD      (HL),$03        
58AC: 21 E0 C2   LD      HL,$C2E0        
58AF: 19         ADD     HL,DE           
58B0: 36 1C      LD      (HL),$1C        
58B2: 3E 39      LD      A,$39           
58B4: E0 F4      LDFF00  ($F4),A         
58B6: D5         PUSH    DE              
58B7: C1         POP     BC              
58B8: 3E 18      LD      A,$18           
58BA: CD 25 3C   CALL    $3C25           
58BD: C1         POP     BC              
58BE: C3 8D 3B   JP      $3B8D           
58C1: 1F         RRA                     
58C2: 1F         RRA                     
58C3: 1F         RRA                     
58C4: E6 03      AND     $03             
58C6: 21 B0 C2   LD      HL,$C2B0        
58C9: 09         ADD     HL,BC           
58CA: 77         LD      (HL),A          
58CB: CD 91 08   CALL    $0891           
58CE: 1F         RRA                     
58CF: 1F         RRA                     
58D0: 1F         RRA                     
58D1: 1F         RRA                     
58D2: E6 0F      AND     $0F             
58D4: 5F         LD      E,A             
58D5: 50         LD      D,B             
58D6: 21 3D 58   LD      HL,$583D        
58D9: 19         ADD     HL,DE           
58DA: 7E         LD      A,(HL)          
58DB: EA 1D D2   LD      ($D21D),A       
58DE: CD 91 08   CALL    $0891           
58E1: FE 40      CP      $40             
58E3: DA 2B 58   JP      C,$582B         
58E6: E6 1F      AND     $1F             
58E8: CA 19 58   JP      Z,$5819         
58EB: C3 2B 58   JP      $582B           
58EE: CD 91 08   CALL    $0891           
58F1: 20 16      JR      NZ,$5909        
58F3: 36 27      LD      (HL),$27        
58F5: 3E 35      LD      A,$35           
58F7: E0 F2      LDFF00  ($F2),A         
58F9: 21 10 C2   LD      HL,$C210        
58FC: 09         ADD     HL,BC           
58FD: 7E         LD      A,(HL)          
58FE: C6 08      ADD     $08             
5900: 77         LD      (HL),A          
5901: 3E 01      LD      A,$01           
5903: EA 1A D2   LD      ($D21A),A       
5906: C3 8D 3B   JP      $3B8D           
5909: 21 B0 C2   LD      HL,$C2B0        
590C: 09         ADD     HL,BC           
590D: 36 04      LD      (HL),$04        
590F: CD 2B 58   CALL    $582B           
5912: C9         RET                     
5913: 50         LD      D,B             
5914: 28 78      JR      Z,$598E         
5916: 18 88      JR      $58A0           
5918: 38 68      JR      C,$5982         
591A: 50         LD      D,B             
591B: 30 30      JR      NC,$594D        
591D: 30 50      JR      NC,$596F        
591F: 50         LD      D,B             
5920: 70         LD      (HL),B          
5921: 70         LD      (HL),B          
5922: 74         LD      (HL),H          
5923: 00         NOP                     
5924: 01 02 03   LD      BC,$0302        
5927: 04         INC     B               
5928: CD 91 08   CALL    $0891           
592B: 20 1F      JR      NZ,$594C        
592D: CD ED 27   CALL    $27ED           
5930: E6 07      AND     $07             
5932: 5F         LD      E,A             
5933: 50         LD      D,B             
5934: 21 13 59   LD      HL,$5913        
5937: 19         ADD     HL,DE           
5938: 7E         LD      A,(HL)          
5939: EA 1B D2   LD      ($D21B),A       
593C: 21 1B 59   LD      HL,$591B        
593F: 19         ADD     HL,DE           
5940: 7E         LD      A,(HL)          
5941: EA 1C D2   LD      ($D21C),A       
5944: CD 91 08   CALL    $0891           
5947: 36 1F      LD      (HL),$1F        
5949: C3 8D 3B   JP      $3B8D           
594C: 1F         RRA                     
594D: 1F         RRA                     
594E: 1F         RRA                     
594F: E6 0F      AND     $0F             
5951: 5F         LD      E,A             
5952: 50         LD      D,B             
5953: 21 23 59   LD      HL,$5923        
5956: 19         ADD     HL,DE           
5957: 7E         LD      A,(HL)          
5958: E0 F1      LDFF00  ($F1),A         
595A: C3 28 57   JP      $5728           
595D: 18 14      JR      $5973           
595F: 10 0C      STOP    $0C             
5961: 08 05 02   LD      ($0205),SP      
5964: 01 AF E0   LD      BC,$E0AF        
5967: F1         POP     AF              
5968: CD 28 57   CALL    $5728           
596B: F0 99      LD      A,($99)         
596D: F5         PUSH    AF              
596E: F0 98      LD      A,($98)         
5970: F5         PUSH    AF              
5971: FA 1B D2   LD      A,($D21B)       
5974: E0 98      LDFF00  ($98),A         
5976: FA 1C D2   LD      A,($D21C)       
5979: E0 99      LDFF00  ($99),A         
597B: CD 91 08   CALL    $0891           
597E: 1F         RRA                     
597F: 1F         RRA                     
5980: E6 07      AND     $07             
5982: 5F         LD      E,A             
5983: 50         LD      D,B             
5984: 21 5D 59   LD      HL,$595D        
5987: 19         ADD     HL,DE           
5988: 7E         LD      A,(HL)          
5989: CD 25 3C   CALL    $3C25           
598C: 21 99 FF   LD      HL,$FF99        
598F: F0 EC      LD      A,($EC)         
5991: 96         SUB     (HL)            
5992: C6 03      ADD     $03             
5994: FE 06      CP      $06             
5996: 30 16      JR      NC,$59AE        
5998: 21 98 FF   LD      HL,$FF98        
599B: F0 EE      LD      A,($EE)         
599D: 96         SUB     (HL)            
599E: C6 03      ADD     $03             
59A0: FE 06      CP      $06             
59A2: 30 0A      JR      NC,$59AE        
59A4: CD 91 08   CALL    $0891           
59A7: 36 50      LD      (HL),$50        
59A9: CD 8D 3B   CALL    $3B8D           
59AC: 36 01      LD      (HL),$01        
59AE: F1         POP     AF              
59AF: E0 98      LDFF00  ($98),A         
59B1: F1         POP     AF              
59B2: E0 99      LDFF00  ($99),A         
59B4: CD 8C 7B   CALL    $7B8C           
59B7: C9         RET                     
59B8: 00         NOP                     
59B9: 0A         LD      A,(BC)          
59BA: 0F         RRCA                    
59BB: 05         DEC     B               
59BC: CD 91 08   CALL    $0891           
59BF: 20 16      JR      NZ,$59D7        
59C1: CD 58 54   CALL    $5458           
59C4: 3E 01      LD      A,$01           
59C6: EA 1A D2   LD      ($D21A),A       
59C9: 3E 06      LD      A,$06           
59CB: CD 87 3B   CALL    $3B87           
59CE: CD 91 08   CALL    $0891           
59D1: 36 50      LD      (HL),$50        
59D3: CD 8D 3B   CALL    $3B8D           
59D6: C9         RET                     
59D7: FA 21 D2   LD      A,($D221)       
59DA: FE 80      CP      $80             
59DC: 30 04      JR      NC,$59E2        
59DE: 3C         INC     A               
59DF: EA 21 D2   LD      ($D221),A       
59E2: FA 21 D2   LD      A,($D221)       
59E5: 21 22 D2   LD      HL,$D222        
59E8: 86         ADD     A,(HL)          
59E9: 77         LD      (HL),A          
59EA: 30 04      JR      NC,$59F0        
59EC: 21 23 D2   LD      HL,$D223        
59EF: 34         INC     (HL)            
59F0: FA 23 D2   LD      A,($D223)       
59F3: E6 03      AND     $03             
59F5: 5F         LD      E,A             
59F6: 50         LD      D,B             
59F7: 21 B8 59   LD      HL,$59B8        
59FA: 19         ADD     HL,DE           
59FB: 7E         LD      A,(HL)          
59FC: 21 80 C3   LD      HL,$C380        
59FF: 09         ADD     HL,BC           
5A00: 77         LD      (HL),A          
5A01: 21 B0 C2   LD      HL,$C2B0        
5A04: 09         ADD     HL,BC           
5A05: 70         LD      (HL),B          
5A06: CD 2B 58   CALL    $582B           
5A09: C9         RET                     
5A0A: CD 91 08   CALL    $0891           
5A0D: 20 06      JR      NZ,$5A15        
5A0F: CD 40 51   CALL    $5140           
5A12: C3 8D 3B   JP      $3B8D           
5A15: FE 18      CP      $18             
5A17: 30 08      JR      NC,$5A21        
5A19: 1F         RRA                     
5A1A: 1F         RRA                     
5A1B: 1F         RRA                     
5A1C: E6 03      AND     $03             
5A1E: CD 87 3B   CALL    $3B87           
5A21: CD 28 57   CALL    $5728           
5A24: C9         RET                     
5A25: CD 28 57   CALL    $5728           
5A28: F0 98      LD      A,($98)         
5A2A: F5         PUSH    AF              
5A2B: F0 99      LD      A,($99)         
5A2D: F5         PUSH    AF              
5A2E: 3E 50      LD      A,$50           
5A30: E0 98      LDFF00  ($98),A         
5A32: 3E 30      LD      A,$30           
5A34: E0 99      LDFF00  ($99),A         
5A36: 3E 10      LD      A,$10           
5A38: CD 25 3C   CALL    $3C25           
5A3B: 21 99 FF   LD      HL,$FF99        
5A3E: F0 EC      LD      A,($EC)         
5A40: 96         SUB     (HL)            
5A41: C6 03      ADD     $03             
5A43: FE 06      CP      $06             
5A45: 30 1D      JR      NC,$5A64        
5A47: 21 98 FF   LD      HL,$FF98        
5A4A: F0 EE      LD      A,($EE)         
5A4C: 96         SUB     (HL)            
5A4D: C6 03      ADD     $03             
5A4F: FE 06      CP      $06             
5A51: 30 11      JR      NC,$5A64        
5A53: CD E2 52   CALL    $52E2           
5A56: CD 91 08   CALL    $0891           
5A59: 36 31      LD      (HL),$31        
5A5B: 21 60 C3   LD      HL,$C360        
5A5E: 09         ADD     HL,BC           
5A5F: 36 FF      LD      (HL),$FF        
5A61: CD A7 5F   CALL    $5FA7           
5A64: F1         POP     AF              
5A65: E0 99      LDFF00  ($99),A         
5A67: F1         POP     AF              
5A68: E0 98      LDFF00  ($98),A         
5A6A: CD 8C 7B   CALL    $7B8C           
5A6D: C9         RET                     
5A6E: CD 97 5D   CALL    $5D97           
5A71: CD 34 5B   CALL    $5B34           
5A74: CD 13 5B   CALL    $5B13           
5A77: CD 51 5D   CALL    $5D51           
5A7A: C9         RET                     
5A7B: 6A         LD      L,D             
5A7C: 00         NOP                     
5A7D: 6C         LD      L,H             
5A7E: 00         NOP                     
5A7F: 6C         LD      L,H             
5A80: 20 6A      JR      NZ,$5AEC        
5A82: 20 6A      JR      NZ,$5AEE        
5A84: 00         NOP                     
5A85: FF         RST     0X38            
5A86: FF         RST     0X38            
5A87: 6A         LD      L,D             
5A88: 20 FF      JR      NZ,$5A89        
5A8A: FF         RST     0X38            
5A8B: 00         NOP                     
5A8C: 00         NOP                     
5A8D: 6A         LD      L,D             
5A8E: 00         NOP                     
5A8F: 08 08 7A   LD      ($7A08),SP      
5A92: 00         NOP                     
5A93: 08 00 7A   LD      ($7A00),SP      
5A96: 20 00      JR      NZ,$5A98        
5A98: 08 6A 20   LD      ($206A),SP      
5A9B: 00         NOP                     
5A9C: 00         NOP                     
5A9D: 00         NOP                     
5A9E: 00         NOP                     
5A9F: 02         LD      (BC),A          
5AA0: 00         NOP                     
5AA1: 00         NOP                     
5AA2: 00         NOP                     
5AA3: 00         NOP                     
5AA4: 02         LD      (BC),A          
5AA5: 04         INC     B               
5AA6: 04         INC     B               
5AA7: 04         INC     B               
5AA8: 04         INC     B               
5AA9: 04         INC     B               
5AAA: 05         DEC     B               
5AAB: 05         DEC     B               
5AAC: 05         DEC     B               
5AAD: 05         DEC     B               
5AAE: 05         DEC     B               
5AAF: F0 F3      LD      A,($F3)         
5AB1: F3         DI                      
5AB2: F0 F5      LD      A,($F5)         
5AB4: F0 F3      LD      A,($F3)         
5AB6: F3         DI                      
5AB7: F0 F5      LD      A,($F5)         
5AB9: F1         POP     AF              
5ABA: F0 F1      LD      A,($F1)         
5ABC: F2                              
5ABD: F0 0F      LD      A,($0F)         
5ABF: 10 0F      STOP    $0F             
5AC1: 0E 10      LD      C,$10           
5AC3: ED                              
5AC4: ED                              
5AC5: F1         POP     AF              
5AC6: F1         POP     AF              
5AC7: FD                              
5AC8: ED                              
5AC9: ED                              
5ACA: F1         POP     AF              
5ACB: F1         POP     AF              
5ACC: FD                              
5ACD: F4                              
5ACE: F6 F7      OR      $F7             
5AD0: F6 F8      OR      $F8             
5AD2: F4                              
5AD3: F6 F7      OR      $F7             
5AD5: F6 F8      OR      $F8             
5AD7: 01 01 01   LD      BC,$0101        
5ADA: 01 03 01   LD      BC,$0103        
5ADD: 01 01 01   LD      BC,$0101        
5AE0: 03         INC     BC              
5AE1: 02         LD      (BC),A          
5AE2: 02         LD      (BC),A          
5AE3: 02         LD      (BC),A          
5AE4: 02         LD      (BC),A          
5AE5: 02         LD      (BC),A          
5AE6: 03         INC     BC              
5AE7: 03         INC     BC              
5AE8: 03         INC     BC              
5AE9: 03         INC     BC              
5AEA: 03         INC     BC              
5AEB: 10 0D      STOP    $0D             
5AED: 0D         DEC     C               
5AEE: 10 13      STOP    $13             
5AF0: 10 0D      STOP    $0D             
5AF2: 0D         DEC     C               
5AF3: 10 13      STOP    $13             
5AF5: F5         PUSH    AF              
5AF6: F6 F5      OR      $F5             
5AF8: F4                              
5AF9: F3         DI                      
5AFA: 13         INC     DE              
5AFB: 12         LD      (DE),A          
5AFC: 13         INC     DE              
5AFD: 14         INC     D               
5AFE: 15         DEC     D               
5AFF: ED                              
5B00: ED                              
5B01: F1         POP     AF              
5B02: F1         POP     AF              
5B03: FD                              
5B04: ED                              
5B05: ED                              
5B06: F1         POP     AF              
5B07: F1         POP     AF              
5B08: FD                              
5B09: EB                              
5B0A: EC                              
5B0B: ED                              
5B0C: EC                              
5B0D: F2                              
5B0E: EB                              
5B0F: EC                              
5B10: ED                              
5B11: EC                              
5B12: F2                              
5B13: 21 B0 C3   LD      HL,$C3B0        
5B16: 09         ADD     HL,BC           
5B17: 7E         LD      A,(HL)          
5B18: 5F         LD      E,A             
5B19: 50         LD      D,B             
5B1A: 21 EB 5A   LD      HL,$5AEB        
5B1D: 19         ADD     HL,DE           
5B1E: F0 EE      LD      A,($EE)         
5B20: 86         ADD     A,(HL)          
5B21: E0 EE      LDFF00  ($EE),A         
5B23: 21 FF 5A   LD      HL,$5AFF        
5B26: 19         ADD     HL,DE           
5B27: F0 EC      LD      A,($EC)         
5B29: C6 08      ADD     $08             
5B2B: 86         ADD     A,(HL)          
5B2C: E0 EC      LDFF00  ($EC),A         
5B2E: 21 D7 5A   LD      HL,$5AD7        
5B31: 19         ADD     HL,DE           
5B32: 18 1F      JR      $5B53           
5B34: 21 B0 C3   LD      HL,$C3B0        
5B37: 09         ADD     HL,BC           
5B38: 7E         LD      A,(HL)          
5B39: 5F         LD      E,A             
5B3A: 50         LD      D,B             
5B3B: 21 AF 5A   LD      HL,$5AAF        
5B3E: 19         ADD     HL,DE           
5B3F: F0 EE      LD      A,($EE)         
5B41: 86         ADD     A,(HL)          
5B42: E0 EE      LDFF00  ($EE),A         
5B44: 21 C3 5A   LD      HL,$5AC3        
5B47: 19         ADD     HL,DE           
5B48: F0 EC      LD      A,($EC)         
5B4A: C6 08      ADD     $08             
5B4C: 86         ADD     A,(HL)          
5B4D: E0 EC      LDFF00  ($EC),A         
5B4F: 21 9B 5A   LD      HL,$5A9B        
5B52: 19         ADD     HL,DE           
5B53: 7E         LD      A,(HL)          
5B54: FE 04      CP      $04             
5B56: 30 0A      JR      NC,$5B62        
5B58: E0 F1      LDFF00  ($F1),A         
5B5A: 11 7B 5A   LD      DE,$5A7B        
5B5D: CD 3B 3C   CALL    $3C3B           
5B60: 18 12      JR      $5B74           
5B62: D6 04      SUB     $04             
5B64: 17         RLA                     
5B65: 17         RLA                     
5B66: 17         RLA                     
5B67: E6 F8      AND     $F8             
5B69: 5F         LD      E,A             
5B6A: 50         LD      D,B             
5B6B: 21 8B 5A   LD      HL,$5A8B        
5B6E: 19         ADD     HL,DE           
5B6F: 0E 02      LD      C,$02           
5B71: CD 26 3D   CALL    $3D26           
5B74: 3E 02      LD      A,$02           
5B76: CD D0 3D   CALL    $3DD0           
5B79: CD BA 3D   CALL    $3DBA           
5B7C: C9         RET                     
5B7D: F8 F8      LDHL    SP,$F8          
5B7F: 60         LD      H,B             
5B80: 00         NOP                     
5B81: F8 00      LDHL    SP,$00          
5B83: 62         LD      H,D             
5B84: 00         NOP                     
5B85: F8 08      LDHL    SP,$08          
5B87: 62         LD      H,D             
5B88: 20 F8      JR      NZ,$5B82        
5B8A: 10 60      STOP    $60             
5B8C: 20 05      JR      NZ,$5B93        
5B8E: F8 6E      LDHL    SP,$6E          
5B90: 00         NOP                     
5B91: 08 00 64   LD      ($6400),SP      
5B94: 00         NOP                     
5B95: 08 08 64   LD      ($6408),SP      
5B98: 20 05      JR      NZ,$5B9F        
5B9A: 10 6E      STOP    $6E             
5B9C: 20 F8      JR      NZ,$5B96        
5B9E: F8 60      LDHL    SP,$60          
5BA0: 00         NOP                     
5BA1: F8 00      LDHL    SP,$00          
5BA3: 62         LD      H,D             
5BA4: 00         NOP                     
5BA5: F8 08      LDHL    SP,$08          
5BA7: 62         LD      H,D             
5BA8: 20 F8      JR      NZ,$5BA2        
5BAA: 10 60      STOP    $60             
5BAC: 20 05      JR      NZ,$5BB3        
5BAE: F9         LD      SP,HL           
5BAF: 6E         LD      L,(HL)          
5BB0: 00         NOP                     
5BB1: 08 00 64   LD      ($6400),SP      
5BB4: 00         NOP                     
5BB5: 08 08 64   LD      ($6408),SP      
5BB8: 20 05      JR      NZ,$5BBF        
5BBA: 0F         RRCA                    
5BBB: 6E         LD      L,(HL)          
5BBC: 20 F8      JR      NZ,$5BB6        
5BBE: F8 60      LDHL    SP,$60          
5BC0: 00         NOP                     
5BC1: F8 00      LDHL    SP,$00          
5BC3: 62         LD      H,D             
5BC4: 00         NOP                     
5BC5: F8 08      LDHL    SP,$08          
5BC7: 62         LD      H,D             
5BC8: 20 F8      JR      NZ,$5BC2        
5BCA: 10 60      STOP    $60             
5BCC: 20 06      JR      NZ,$5BD4        
5BCE: F9         LD      SP,HL           
5BCF: 6E         LD      L,(HL)          
5BD0: 00         NOP                     
5BD1: 08 00 64   LD      ($6400),SP      
5BD4: 00         NOP                     
5BD5: 08 08 64   LD      ($6408),SP      
5BD8: 20 06      JR      NZ,$5BE0        
5BDA: 0F         RRCA                    
5BDB: 6E         LD      L,(HL)          
5BDC: 20 F8      JR      NZ,$5BD6        
5BDE: F8 60      LDHL    SP,$60          
5BE0: 00         NOP                     
5BE1: F8 00      LDHL    SP,$00          
5BE3: 62         LD      H,D             
5BE4: 00         NOP                     
5BE5: F8 08      LDHL    SP,$08          
5BE7: 62         LD      H,D             
5BE8: 20 F8      JR      NZ,$5BE2        
5BEA: 10 60      STOP    $60             
5BEC: 20 06      JR      NZ,$5BF4        
5BEE: F8 6E      LDHL    SP,$6E          
5BF0: 00         NOP                     
5BF1: 08 00 64   LD      ($6400),SP      
5BF4: 00         NOP                     
5BF5: 08 08 64   LD      ($6408),SP      
5BF8: 20 06      JR      NZ,$5C00        
5BFA: 10 6E      STOP    $6E             
5BFC: 20 FA      JR      NZ,$5BF8        
5BFE: F8 60      LDHL    SP,$60          
5C00: 00         NOP                     
5C01: FA 00 62   LD      A,($6200)       
5C04: 00         NOP                     
5C05: FA 08 62   LD      A,($6208)       
5C08: 20 FA      JR      NZ,$5C04        
5C0A: 10 60      STOP    $60             
5C0C: 20 08      JR      NZ,$5C16        
5C0E: F8 6E      LDHL    SP,$6E          
5C10: 00         NOP                     
5C11: 08 00 64   LD      ($6400),SP      
5C14: 00         NOP                     
5C15: 08 08 64   LD      ($6408),SP      
5C18: 20 08      JR      NZ,$5C22        
5C1A: 10 6E      STOP    $6E             
5C1C: 20 FA      JR      NZ,$5C18        
5C1E: F8 60      LDHL    SP,$60          
5C20: 00         NOP                     
5C21: FA 00 66   LD      A,($6600)       
5C24: 00         NOP                     
5C25: FA 08 66   LD      A,($6608)       
5C28: 20 FA      JR      NZ,$5C24        
5C2A: 10 60      STOP    $60             
5C2C: 20 05      JR      NZ,$5C33        
5C2E: F8 6E      LDHL    SP,$6E          
5C30: 00         NOP                     
5C31: 08 00 68   LD      ($6800),SP      
5C34: 00         NOP                     
5C35: 08 08 68   LD      ($6808),SP      
5C38: 20 05      JR      NZ,$5C3F        
5C3A: 10 6E      STOP    $6E             
5C3C: 20 FA      JR      NZ,$5C38        
5C3E: F8 60      LDHL    SP,$60          
5C40: 00         NOP                     
5C41: FA 00 66   LD      A,($6600)       
5C44: 00         NOP                     
5C45: FA 08 66   LD      A,($6608)       
5C48: 20 FA      JR      NZ,$5C44        
5C4A: 10 60      STOP    $60             
5C4C: 20 05      JR      NZ,$5C53        
5C4E: F9         LD      SP,HL           
5C4F: 6E         LD      L,(HL)          
5C50: 00         NOP                     
5C51: 08 00 68   LD      ($6800),SP      
5C54: 00         NOP                     
5C55: 08 08 68   LD      ($6808),SP      
5C58: 20 05      JR      NZ,$5C5F        
5C5A: 0F         RRCA                    
5C5B: 6E         LD      L,(HL)          
5C5C: 20 FA      JR      NZ,$5C58        
5C5E: F8 60      LDHL    SP,$60          
5C60: 00         NOP                     
5C61: FA 00 66   LD      A,($6600)       
5C64: 00         NOP                     
5C65: FA 08 66   LD      A,($6608)       
5C68: 20 FA      JR      NZ,$5C64        
5C6A: 10 60      STOP    $60             
5C6C: 20 06      JR      NZ,$5C74        
5C6E: F9         LD      SP,HL           
5C6F: 6E         LD      L,(HL)          
5C70: 00         NOP                     
5C71: 08 00 68   LD      ($6800),SP      
5C74: 00         NOP                     
5C75: 08 08 68   LD      ($6808),SP      
5C78: 20 06      JR      NZ,$5C80        
5C7A: 0F         RRCA                    
5C7B: 6E         LD      L,(HL)          
5C7C: 20 FA      JR      NZ,$5C78        
5C7E: F8 60      LDHL    SP,$60          
5C80: 00         NOP                     
5C81: FA 00 66   LD      A,($6600)       
5C84: 00         NOP                     
5C85: FA 08 66   LD      A,($6608)       
5C88: 20 FA      JR      NZ,$5C84        
5C8A: 10 60      STOP    $60             
5C8C: 20 06      JR      NZ,$5C94        
5C8E: F8 6E      LDHL    SP,$6E          
5C90: 00         NOP                     
5C91: 08 00 68   LD      ($6800),SP      
5C94: 00         NOP                     
5C95: 08 08 68   LD      ($6808),SP      
5C98: 20 06      JR      NZ,$5CA0        
5C9A: 10 6E      STOP    $6E             
5C9C: 20 F8      JR      NZ,$5C96        
5C9E: F8 60      LDHL    SP,$60          
5CA0: 00         NOP                     
5CA1: F8 00      LDHL    SP,$00          
5CA3: 66         LD      H,(HL)          
5CA4: 00         NOP                     
5CA5: F8 08      LDHL    SP,$08          
5CA7: 66         LD      H,(HL)          
5CA8: 20 F8      JR      NZ,$5CA2        
5CAA: 10 60      STOP    $60             
5CAC: 20 04      JR      NZ,$5CB2        
5CAE: F8 6E      LDHL    SP,$6E          
5CB0: 00         NOP                     
5CB1: 08 00 68   LD      ($6800),SP      
5CB4: 00         NOP                     
5CB5: 08 08 68   LD      ($6808),SP      
5CB8: 20 04      JR      NZ,$5CBE        
5CBA: 10 6E      STOP    $6E             
5CBC: 20 F8      JR      NZ,$5CB6        
5CBE: FC                              
5CBF: 72         LD      (HL),D          
5CC0: 00         NOP                     
5CC1: F8 04      LDHL    SP,$04          
5CC3: 74         LD      (HL),H          
5CC4: 00         NOP                     
5CC5: 08 00 76   LD      ($7600),SP      
5CC8: 00         NOP                     
5CC9: 08 08 78   LD      ($7808),SP      
5CCC: 00         NOP                     
5CCD: FF         RST     0X38            
5CCE: FF         RST     0X38            
5CCF: FF         RST     0X38            
5CD0: FF         RST     0X38            
5CD1: FF         RST     0X38            
5CD2: FF         RST     0X38            
5CD3: FF         RST     0X38            
5CD4: FF         RST     0X38            
5CD5: FF         RST     0X38            
5CD6: FF         RST     0X38            
5CD7: FF         RST     0X38            
5CD8: FF         RST     0X38            
5CD9: FF         RST     0X38            
5CDA: FF         RST     0X38            
5CDB: FF         RST     0X38            
5CDC: FF         RST     0X38            
5CDD: FA FB 72   LD      A,($72FB)       
5CE0: 00         NOP                     
5CE1: FA 03 74   LD      A,($7403)       
5CE4: 00         NOP                     
5CE5: 08 00 76   LD      ($7600),SP      
5CE8: 00         NOP                     
5CE9: 08 08 78   LD      ($7808),SP      
5CEC: 00         NOP                     
5CED: FF         RST     0X38            
5CEE: FF         RST     0X38            
5CEF: FF         RST     0X38            
5CF0: FF         RST     0X38            
5CF1: FF         RST     0X38            
5CF2: FF         RST     0X38            
5CF3: FF         RST     0X38            
5CF4: FF         RST     0X38            
5CF5: FF         RST     0X38            
5CF6: FF         RST     0X38            
5CF7: FF         RST     0X38            
5CF8: FF         RST     0X38            
5CF9: FF         RST     0X38            
5CFA: FF         RST     0X38            
5CFB: FF         RST     0X38            
5CFC: FF         RST     0X38            
5CFD: F8 04      LDHL    SP,$04          
5CFF: 74         LD      (HL),H          
5D00: 20 F8      JR      NZ,$5CFA        
5D02: 0C         INC     C               
5D03: 72         LD      (HL),D          
5D04: 20 08      JR      NZ,$5D0E        
5D06: 00         NOP                     
5D07: 78         LD      A,B             
5D08: 20 08      JR      NZ,$5D12        
5D0A: 08 76 20   LD      ($2076),SP      
5D0D: FF         RST     0X38            
5D0E: FF         RST     0X38            
5D0F: FF         RST     0X38            
5D10: FF         RST     0X38            
5D11: FF         RST     0X38            
5D12: FF         RST     0X38            
5D13: FF         RST     0X38            
5D14: FF         RST     0X38            
5D15: FF         RST     0X38            
5D16: FF         RST     0X38            
5D17: FF         RST     0X38            
5D18: FF         RST     0X38            
5D19: FF         RST     0X38            
5D1A: FF         RST     0X38            
5D1B: FF         RST     0X38            
5D1C: FF         RST     0X38            
5D1D: FA 05 74   LD      A,($7405)       
5D20: 20 FA      JR      NZ,$5D1C        
5D22: 0D         DEC     C               
5D23: 72         LD      (HL),D          
5D24: 20 08      JR      NZ,$5D2E        
5D26: 00         NOP                     
5D27: 78         LD      A,B             
5D28: 20 08      JR      NZ,$5D32        
5D2A: 08 76 20   LD      ($2076),SP      
5D2D: FF         RST     0X38            
5D2E: FF         RST     0X38            
5D2F: FF         RST     0X38            
5D30: FF         RST     0X38            
5D31: FF         RST     0X38            
5D32: FF         RST     0X38            
5D33: FF         RST     0X38            
5D34: FF         RST     0X38            
5D35: FF         RST     0X38            
5D36: FF         RST     0X38            
5D37: FF         RST     0X38            
5D38: FF         RST     0X38            
5D39: FF         RST     0X38            
5D3A: FF         RST     0X38            
5D3B: FF         RST     0X38            
5D3C: FF         RST     0X38            
5D3D: 00         NOP                     
5D3E: 01 02 03   LD      BC,$0302        
5D41: 04         INC     B               
5D42: 05         DEC     B               
5D43: 06 07      LD      B,$07           
5D45: 08 09 0A   LD      ($0A09),SP      
5D48: 0A         LD      A,(BC)          
5D49: 0A         LD      A,(BC)          
5D4A: 0A         LD      A,(BC)          
5D4B: 0B         DEC     BC              
5D4C: 0C         INC     C               
5D4D: 0C         INC     C               
5D4E: 0C         INC     C               
5D4F: 0C         INC     C               
5D50: 0D         DEC     C               
5D51: 21 B0 C3   LD      HL,$C3B0        
5D54: 09         ADD     HL,BC           
5D55: 7E         LD      A,(HL)          
5D56: 5F         LD      E,A             
5D57: 50         LD      D,B             
5D58: 21 3D 5D   LD      HL,$5D3D        
5D5B: 19         ADD     HL,DE           
5D5C: 7E         LD      A,(HL)          
5D5D: 16 00      LD      D,$00           
5D5F: 5F         LD      E,A             
5D60: CB 23      SET     1,E             
5D62: CB 12      SET     1,E             
5D64: CB 23      SET     1,E             
5D66: CB 12      SET     1,E             
5D68: CB 23      SET     1,E             
5D6A: CB 12      SET     1,E             
5D6C: CB 23      SET     1,E             
5D6E: CB 12      SET     1,E             
5D70: CB 23      SET     1,E             
5D72: CB 12      SET     1,E             
5D74: 21 7D 5B   LD      HL,$5B7D        
5D77: 19         ADD     HL,DE           
5D78: 0E 08      LD      C,$08           
5D7A: CD 26 3D   CALL    $3D26           
5D7D: 3E 08      LD      A,$08           
5D7F: CD D0 3D   CALL    $3DD0           
5D82: C9         RET                     
5D83: 1E 00      LD      E,$00           
5D85: 1E 60      LD      E,$60           
5D87: 7C         LD      A,H             
5D88: 00         NOP                     
5D89: 7C         LD      A,H             
5D8A: 20 7E      JR      NZ,$5E0A        
5D8C: 00         NOP                     
5D8D: 7E         LD      A,(HL)          
5D8E: 20 14      JR      NZ,$5DA4        
5D90: EC                              
5D91: 00         NOP                     
5D92: 00         NOP                     
5D93: 00         NOP                     
5D94: 00         NOP                     
5D95: F0 04      LD      A,($04)         
5D97: F0 ED      LD      A,($ED)         
5D99: F5         PUSH    AF              
5D9A: CD A1 5D   CALL    $5DA1           
5D9D: F1         POP     AF              
5D9E: E0 ED      LDFF00  ($ED),A         
5DA0: C9         RET                     
5DA1: FA 1D D2   LD      A,($D21D)       
5DA4: A7         AND     A               
5DA5: C8         RET     Z               
5DA6: 3D         DEC     A               
5DA7: E0 F1      LDFF00  ($F1),A         
5DA9: F0 E7      LD      A,($E7)         
5DAB: 17         RLA                     
5DAC: 17         RLA                     
5DAD: 17         RLA                     
5DAE: E6 50      AND     $50             
5DB0: E0 ED      LDFF00  ($ED),A         
5DB2: FA 1E D2   LD      A,($D21E)       
5DB5: 5F         LD      E,A             
5DB6: 50         LD      D,B             
5DB7: 21 8F 5D   LD      HL,$5D8F        
5DBA: 19         ADD     HL,DE           
5DBB: F0 EE      LD      A,($EE)         
5DBD: 86         ADD     A,(HL)          
5DBE: E0 EE      LDFF00  ($EE),A         
5DC0: 21 93 5D   LD      HL,$5D93        
5DC3: 19         ADD     HL,DE           
5DC4: F0 EC      LD      A,($EC)         
5DC6: 86         ADD     A,(HL)          
5DC7: E0 EC      LDFF00  ($EC),A         
5DC9: 11 83 5D   LD      DE,$5D83        
5DCC: CD 3B 3C   CALL    $3C3B           
5DCF: 3E 02      LD      A,$02           
5DD1: CD D0 3D   CALL    $3DD0           
5DD4: CD BA 3D   CALL    $3DBA           
5DD7: C9         RET                     
5DD8: 46         LD      B,(HL)          
5DD9: 00         NOP                     
5DDA: 46         LD      B,(HL)          
5DDB: 60         LD      H,B             
5DDC: 70         LD      (HL),B          
5DDD: 00         NOP                     
5DDE: FF         RST     0X38            
5DDF: FF         RST     0X38            
5DE0: 11 D8 5D   LD      DE,$5DD8        
5DE3: C9         RET                     
5DE4: 7E         LD      A,(HL)          
5DE5: 00         NOP                     
5DE6: 7E         LD      A,(HL)          
5DE7: 20 7C      JR      NZ,$5E65        
5DE9: 00         NOP                     
5DEA: 7C         LD      A,H             
5DEB: 20 1E      JR      NZ,$5E0B        
5DED: 00         NOP                     
5DEE: 1E 60      LD      E,$60           
5DF0: 58         LD      E,B             
5DF1: 00         NOP                     
5DF2: 58         LD      E,B             
5DF3: 20 5A      JR      NZ,$5E4F        
5DF5: 00         NOP                     
5DF6: 5A         LD      E,D             
5DF7: 20 F0      JR      NZ,$5DE9        
5DF9: E7         RST     0X20            
5DFA: 17         RLA                     
5DFB: 17         RLA                     
5DFC: 17         RLA                     
5DFD: E6 50      AND     $50             
5DFF: E0 ED      LDFF00  ($ED),A         
5E01: 11 E4 5D   LD      DE,$5DE4        
5E04: CD 3B 3C   CALL    $3C3B           
5E07: CD 20 7B   CALL    $7B20           
5E0A: CD E2 08   CALL    $08E2           
5E0D: F0 F0      LD      A,($F0)         
5E0F: FE 04      CP      $04             
5E11: 20 1D      JR      NZ,$5E30        
5E13: CD 8C 08   CALL    $088C           
5E16: CA 35 7C   JP      Z,$7C35         
5E19: A9         XOR     C               
5E1A: CB 47      SET     1,E             
5E1C: 1E FF      LD      E,$FF           
5E1E: 28 0B      JR      Z,$5E2B         
5E20: CD 8C 08   CALL    $088C           
5E23: 1E 01      LD      E,$01           
5E25: FE 08      CP      $08             
5E27: 30 02      JR      NC,$5E2B        
5E29: 1E 02      LD      E,$02           
5E2B: 7B         LD      A,E             
5E2C: CD 87 3B   CALL    $3B87           
5E2F: C9         RET                     
5E30: CD 8C 7B   CALL    $7B8C           
5E33: CD 9E 3B   CALL    $3B9E           
5E36: F0 F0      LD      A,($F0)         
5E38: C7         RST     0X00            
5E39: 41         LD      B,C             
5E3A: 5E         LD      E,(HL)          
5E3B: 91         SUB     C               
5E3C: 5E         LD      E,(HL)          
5E3D: B9         CP      C               
5E3E: 5E         LD      E,(HL)          
5E3F: 2F         CPL                     
5E40: 5F         LD      E,A             
5E41: CD B4 3B   CALL    $3BB4           
5E44: 21 D0 C3   LD      HL,$C3D0        
5E47: 09         ADD     HL,BC           
5E48: 7E         LD      A,(HL)          
5E49: 3C         INC     A               
5E4A: 77         LD      (HL),A          
5E4B: E6 03      AND     $03             
5E4D: 20 36      JR      NZ,$5E85        
5E4F: 3E E6      LD      A,$E6           
5E51: CD 01 3C   CALL    $3C01           
5E54: D8         RET     C               
5E55: 21 40 C3   LD      HL,$C340        
5E58: 19         ADD     HL,DE           
5E59: 36 C2      LD      (HL),$C2        
5E5B: 21 50 C3   LD      HL,$C350        
5E5E: 19         ADD     HL,DE           
5E5F: 72         LD      (HL),D          
5E60: 21 40 C4   LD      HL,$C440        
5E63: 19         ADD     HL,DE           
5E64: 34         INC     (HL)            
5E65: F0 D7      LD      A,($D7)         
5E67: 21 00 C2   LD      HL,$C200        
5E6A: 19         ADD     HL,DE           
5E6B: 77         LD      (HL),A          
5E6C: F0 D8      LD      A,($D8)         
5E6E: 21 10 C2   LD      HL,$C210        
5E71: 19         ADD     HL,DE           
5E72: 77         LD      (HL),A          
5E73: 21 F0 C2   LD      HL,$C2F0        
5E76: 19         ADD     HL,DE           
5E77: 36 0F      LD      (HL),$0F        
5E79: 21 B0 C3   LD      HL,$C3B0        
5E7C: 19         ADD     HL,DE           
5E7D: 36 01      LD      (HL),$01        
5E7F: 21 90 C2   LD      HL,$C290        
5E82: 19         ADD     HL,DE           
5E83: 36 04      LD      (HL),$04        
5E85: 21 A0 C2   LD      HL,$C2A0        
5E88: 09         ADD     HL,BC           
5E89: 7E         LD      A,(HL)          
5E8A: A7         AND     A               
5E8B: 28 03      JR      Z,$5E90         
5E8D: C3 35 7C   JP      $7C35           
5E90: C9         RET                     
5E91: 3E 08      LD      A,$08           
5E93: E0 F4      LDFF00  ($F4),A         
5E95: 3E 18      LD      A,$18           
5E97: CD 30 3C   CALL    $3C30           
5E9A: F0 D7      LD      A,($D7)         
5E9C: E0 9B      LDFF00  ($9B),A         
5E9E: 2F         CPL                     
5E9F: 3C         INC     A               
5EA0: 21 50 C2   LD      HL,$C250        
5EA3: 09         ADD     HL,BC           
5EA4: 77         LD      (HL),A          
5EA5: F0 D8      LD      A,($D8)         
5EA7: E0 9A      LDFF00  ($9A),A         
5EA9: 2F         CPL                     
5EAA: 3C         INC     A               
5EAB: 21 40 C2   LD      HL,$C240        
5EAE: 09         ADD     HL,BC           
5EAF: 77         LD      (HL),A          
5EB0: 3E 10      LD      A,$10           
5EB2: EA 3E C1   LD      ($C13E),A       
5EB5: CD 8D 3B   CALL    $3B8D           
5EB8: C9         RET                     
5EB9: CD 44 5E   CALL    $5E44           
5EBC: FA 1A D2   LD      A,($D21A)       
5EBF: A7         AND     A               
5EC0: C0         RET     NZ              
5EC1: FA 01 D2   LD      A,($D201)       
5EC4: 5F         LD      E,A             
5EC5: 50         LD      D,B             
5EC6: 21 00 C2   LD      HL,$C200        
5EC9: 19         ADD     HL,DE           
5ECA: F0 EE      LD      A,($EE)         
5ECC: 96         SUB     (HL)            
5ECD: C6 10      ADD     $10             
5ECF: FE 20      CP      $20             
5ED1: 30 53      JR      NC,$5F26        
5ED3: 21 10 C2   LD      HL,$C210        
5ED6: 19         ADD     HL,DE           
5ED7: F0 EC      LD      A,($EC)         
5ED9: 96         SUB     (HL)            
5EDA: C6 0C      ADD     $0C             
5EDC: FE 18      CP      $18             
5EDE: 30 46      JR      NC,$5F26        
5EE0: 21 40 C2   LD      HL,$C240        
5EE3: 09         ADD     HL,BC           
5EE4: 7E         LD      A,(HL)          
5EE5: CB 27      SET     1,E             
5EE7: 21 F0 C3   LD      HL,$C3F0        
5EEA: 19         ADD     HL,DE           
5EEB: 77         LD      (HL),A          
5EEC: 21 50 C2   LD      HL,$C250        
5EEF: 09         ADD     HL,BC           
5EF0: 7E         LD      A,(HL)          
5EF1: CB 27      SET     1,E             
5EF3: 21 00 C4   LD      HL,$C400        
5EF6: 19         ADD     HL,DE           
5EF7: 77         LD      (HL),A          
5EF8: 21 10 C4   LD      HL,$C410        
5EFB: 19         ADD     HL,DE           
5EFC: 36 12      LD      (HL),$12        
5EFE: CD 35 7C   CALL    $7C35           
5F01: FA 20 D2   LD      A,($D220)       
5F04: 3C         INC     A               
5F05: EA 20 D2   LD      ($D220),A       
5F08: FE 04      CP      $04             
5F0A: 38 10      JR      C,$5F1C         
5F0C: 21 90 C2   LD      HL,$C290        
5F0F: 19         ADD     HL,DE           
5F10: 36 07      LD      (HL),$07        
5F12: 21 E0 C2   LD      HL,$C2E0        
5F15: 19         ADD     HL,DE           
5F16: 36 C0      LD      (HL),$C0        
5F18: 3E 36      LD      A,$36           
5F1A: E0 F2      LDFF00  ($F2),A         
5F1C: 21 20 C4   LD      HL,$C420        
5F1F: 19         ADD     HL,DE           
5F20: 36 14      LD      (HL),$14        
5F22: 3E 07      LD      A,$07           
5F24: E0 F3      LDFF00  ($F3),A         
5F26: C9         RET                     
5F27: 20 20      JR      NZ,$5F49        
5F29: E0 E0      LDFF00  ($E0),A         
5F2B: 20 E0      JR      NZ,$5F0D        
5F2D: 20 E0      JR      NZ,$5F0F        
5F2F: CD BF 3B   CALL    $3BBF           
5F32: F0 E7      LD      A,($E7)         
5F34: 1F         RRA                     
5F35: 1F         RRA                     
5F36: 1F         RRA                     
5F37: E6 01      AND     $01             
5F39: C6 03      ADD     $03             
5F3B: CD 87 3B   CALL    $3B87           
5F3E: CD 91 08   CALL    $0891           
5F41: 28 09      JR      Z,$5F4C         
5F43: E6 01      AND     $01             
5F45: 20 05      JR      NZ,$5F4C        
5F47: 3E 18      LD      A,$18           
5F49: CD 25 3C   CALL    $3C25           
5F4C: 21 A0 C2   LD      HL,$C2A0        
5F4F: 09         ADD     HL,BC           
5F50: 7E         LD      A,(HL)          
5F51: A7         AND     A               
5F52: 28 52      JR      Z,$5FA6         
5F54: 3E 36      LD      A,$36           
5F56: E0 F4      LDFF00  ($F4),A         
5F58: AF         XOR     A               
5F59: E0 E8      LDFF00  ($E8),A         
5F5B: 3E 7D      LD      A,$7D           
5F5D: CD 01 3C   CALL    $3C01           
5F60: 38 41      JR      C,$5FA3         
5F62: F0 D7      LD      A,($D7)         
5F64: 21 00 C2   LD      HL,$C200        
5F67: 19         ADD     HL,DE           
5F68: 77         LD      (HL),A          
5F69: F0 D8      LD      A,($D8)         
5F6B: 21 10 C2   LD      HL,$C210        
5F6E: 19         ADD     HL,DE           
5F6F: 77         LD      (HL),A          
5F70: 21 B0 C2   LD      HL,$C2B0        
5F73: 19         ADD     HL,DE           
5F74: 34         INC     (HL)            
5F75: C5         PUSH    BC              
5F76: F0 D7      LD      A,($D7)         
5F78: 21 00 C2   LD      HL,$C200        
5F7B: 19         ADD     HL,DE           
5F7C: 77         LD      (HL),A          
5F7D: F0 D8      LD      A,($D8)         
5F7F: 21 10 C2   LD      HL,$C210        
5F82: 19         ADD     HL,DE           
5F83: 77         LD      (HL),A          
5F84: F0 E8      LD      A,($E8)         
5F86: 4F         LD      C,A             
5F87: 21 27 5F   LD      HL,$5F27        
5F8A: 09         ADD     HL,BC           
5F8B: 7E         LD      A,(HL)          
5F8C: 21 40 C2   LD      HL,$C240        
5F8F: 19         ADD     HL,DE           
5F90: 77         LD      (HL),A          
5F91: 21 2B 5F   LD      HL,$5F2B        
5F94: 09         ADD     HL,BC           
5F95: 7E         LD      A,(HL)          
5F96: 21 50 C2   LD      HL,$C250        
5F99: 19         ADD     HL,DE           
5F9A: 77         LD      (HL),A          
5F9B: C1         POP     BC              
5F9C: F0 E8      LD      A,($E8)         
5F9E: 3C         INC     A               
5F9F: FE 04      CP      $04             
5FA1: 20 B6      JR      NZ,$5F59        
5FA3: C3 35 7C   JP      $7C35           
5FA6: C9         RET                     
5FA7: 1E 80      LD      E,$80           
5FA9: 21 00 D1   LD      HL,$D100        
5FAC: AF         XOR     A               
5FAD: 22         LD      (HLI),A         
5FAE: 1D         DEC     E               
5FAF: 20 FB      JR      NZ,$5FAC        
5FB1: C9         RET                     
5FB2: 03         INC     BC              
5FB3: 03         INC     BC              
5FB4: 05         DEC     B               
5FB5: 05         DEC     B               
5FB6: 00         NOP                     
5FB7: 00         NOP                     
5FB8: 04         INC     B               
5FB9: 04         INC     B               
5FBA: 02         LD      (BC),A          
5FBB: 02         LD      (BC),A          
5FBC: 06 06      LD      B,$06           
5FBE: 01 01 07   LD      BC,$0701        
5FC1: 07         RLCA                    
5FC2: 00         NOP                     
5FC3: 06 0C      LD      B,$0C           
5FC5: 0E 10      LD      C,$10           
5FC7: 0E 0C      LD      C,$0C           
5FC9: 06 00      LD      B,$00           
5FCB: FA F4 F2   LD      A,($F2F4)       
5FCE: F0 F2      LD      A,($F2)         
5FD0: F4                              
5FD1: FA 00 06   LD      A,($0600)       
5FD4: 0C         INC     C               
5FD5: 0E 06      LD      C,$06           
5FD7: 07         RLCA                    
5FD8: 00         NOP                     
5FD9: 01 02 03   LD      BC,$0302        
5FDC: 04         INC     B               
5FDD: 05         DEC     B               
5FDE: CD 20 7B   CALL    $7B20           
5FE1: C3 B4 3B   JP      $3BB4           
5FE4: F0 F0      LD      A,($F0)         
5FE6: C7         RST     0X00            
5FE7: 57         LD      D,A             
5FE8: 60         LD      H,B             
5FE9: E3                              
5FEA: 60         LD      H,B             
5FEB: D0         RET     NC              
5FEC: 60         LD      H,B             
5FED: 9A         SBC     D               
5FEE: 60         LD      H,B             
5FEF: 00         NOP                     
5FF0: 00         NOP                     
5FF1: 4A         LD      C,D             
5FF2: 00         NOP                     
5FF3: 00         NOP                     
5FF4: 08 4A 20   LD      ($204A),SP      
5FF7: FF         RST     0X38            
5FF8: FF         RST     0X38            
5FF9: FF         RST     0X38            
5FFA: FF         RST     0X38            
5FFB: FF         RST     0X38            
5FFC: FF         RST     0X38            
5FFD: FF         RST     0X38            
5FFE: FF         RST     0X38            
5FFF: FF         RST     0X38            
6000: FF         RST     0X38            
6001: FF         RST     0X38            
6002: FF         RST     0X38            
6003: FF         RST     0X38            
6004: FF         RST     0X38            
6005: FF         RST     0X38            
6006: FF         RST     0X38            
6007: 00         NOP                     
6008: 00         NOP                     
6009: 4C         LD      C,H             
600A: 00         NOP                     
600B: 00         NOP                     
600C: 08 4C 20   LD      ($204C),SP      
600F: FF         RST     0X38            
6010: FF         RST     0X38            
6011: FF         RST     0X38            
6012: FF         RST     0X38            
6013: FF         RST     0X38            
6014: FF         RST     0X38            
6015: FF         RST     0X38            
6016: FF         RST     0X38            
6017: FF         RST     0X38            
6018: FF         RST     0X38            
6019: FF         RST     0X38            
601A: FF         RST     0X38            
601B: FF         RST     0X38            
601C: FF         RST     0X38            
601D: FF         RST     0X38            
601E: FF         RST     0X38            
601F: 00         NOP                     
6020: 00         NOP                     
6021: 4E         LD      C,(HL)          
6022: 00         NOP                     
6023: 00         NOP                     
6024: 08 4E 20   LD      ($204E),SP      
6027: FF         RST     0X38            
6028: FF         RST     0X38            
6029: FF         RST     0X38            
602A: FF         RST     0X38            
602B: FF         RST     0X38            
602C: FF         RST     0X38            
602D: FF         RST     0X38            
602E: FF         RST     0X38            
602F: FF         RST     0X38            
6030: FF         RST     0X38            
6031: FF         RST     0X38            
6032: FF         RST     0X38            
6033: FF         RST     0X38            
6034: FF         RST     0X38            
6035: FF         RST     0X38            
6036: FF         RST     0X38            
6037: 00         NOP                     
6038: F8 78      LDHL    SP,$78          
603A: 00         NOP                     
603B: F8 00      LDHL    SP,$00          
603D: 7A         LD      A,D             
603E: 00         NOP                     
603F: F8 08      LDHL    SP,$08          
6041: 7A         LD      A,D             
6042: 20 00      JR      NZ,$6044        
6044: 10 78      STOP    $78             
6046: 20 08      JR      NZ,$6050        
6048: 00         NOP                     
6049: 7C         LD      A,H             
604A: 00         NOP                     
604B: 08 08 7C   LD      ($7C08),SP      
604E: 20 03      JR      NZ,$6053        
6050: 03         INC     BC              
6051: 02         LD      (BC),A          
6052: 01 00 00   LD      BC,$0000        
6055: 00         NOP                     
6056: 00         NOP                     
6057: AF         XOR     A               
6058: E0 F1      LDFF00  ($F1),A         
605A: CD 91 08   CALL    $0891           
605D: 20 03      JR      NZ,$6062        
605F: C3 8D 3B   JP      $3B8D           
6062: FE 20      CP      $20             
6064: 20 06      JR      NZ,$606C        
6066: 35         DEC     (HL)            
6067: CD D8 52   CALL    $52D8           
606A: 3E 20      LD      A,$20           
606C: 1F         RRA                     
606D: 1F         RRA                     
606E: 1F         RRA                     
606F: E6 07      AND     $07             
6071: 5F         LD      E,A             
6072: 50         LD      D,B             
6073: 21 4F 60   LD      HL,$604F        
6076: 19         ADD     HL,DE           
6077: 7E         LD      A,(HL)          
6078: 17         RLA                     
6079: 17         RLA                     
607A: 17         RLA                     
607B: E6 F8      AND     $F8             
607D: 5F         LD      E,A             
607E: 17         RLA                     
607F: E6 F0      AND     $F0             
6081: 83         ADD     A,E             
6082: 5F         LD      E,A             
6083: 21 EF 5F   LD      HL,$5FEF        
6086: 19         ADD     HL,DE           
6087: 0E 06      LD      C,$06           
6089: CD 26 3D   CALL    $3D26           
608C: 3E 06      LD      A,$06           
608E: CD D0 3D   CALL    $3DD0           
6091: C9         RET                     
6092: 00         NOP                     
6093: 00         NOP                     
6094: 01 01 02   LD      BC,$0201        
6097: 02         LD      (BC),A          
6098: 03         INC     BC              
6099: 03         INC     BC              
609A: AF         XOR     A               
609B: E0 F1      LDFF00  ($F1),A         
609D: CD 91 08   CALL    $0891           
60A0: 20 22      JR      NZ,$60C4        
60A2: CD E2 52   CALL    $52E2           
60A5: CD 40 51   CALL    $5140           
60A8: 21 60 C3   LD      HL,$C360        
60AB: 09         ADD     HL,BC           
60AC: 36 FF      LD      (HL),$FF        
60AE: 21 40 C3   LD      HL,$C340        
60B1: 09         ADD     HL,BC           
60B2: 36 40      LD      (HL),$40        
60B4: 21 50 C3   LD      HL,$C350        
60B7: 09         ADD     HL,BC           
60B8: 36 0A      LD      (HL),$0A        
60BA: 21 30 C4   LD      HL,$C430        
60BD: 09         ADD     HL,BC           
60BE: 36 90      LD      (HL),$90        
60C0: CD 65 3B   CALL    $3B65           
60C3: C9         RET                     
60C4: 1F         RRA                     
60C5: 1F         RRA                     
60C6: 1F         RRA                     
60C7: E6 07      AND     $07             
60C9: 5F         LD      E,A             
60CA: 50         LD      D,B             
60CB: 21 92 60   LD      HL,$6092        
60CE: 18 A6      JR      $6076           
60D0: 21 80 C4   LD      HL,$C480        
60D3: 09         ADD     HL,BC           
60D4: 7E         LD      A,(HL)          
60D5: A7         AND     A               
60D6: 20 0B      JR      NZ,$60E3        
60D8: CD 91 08   CALL    $0891           
60DB: 36 1F      LD      (HL),$1F        
60DD: CD 58 54   CALL    $5458           
60E0: C3 8D 3B   JP      $3B8D           
60E3: CD DE 5F   CALL    $5FDE           
60E6: CD 55 62   CALL    $6255           
60E9: CD E2 08   CALL    $08E2           
60EC: CD BA 3D   CALL    $3DBA           
60EF: CD 20 7B   CALL    $7B20           
60F2: AF         XOR     A               
60F3: EA D6 D3   LD      ($D3D6),A       
60F6: 1E 0C      LD      E,$0C           
60F8: 21 00 C3   LD      HL,$C300        
60FB: 09         ADD     HL,BC           
60FC: 7E         LD      A,(HL)          
60FD: A7         AND     A               
60FE: 28 0A      JR      Z,$610A         
6100: CD 18 61   CALL    $6118           
6103: 3E 01      LD      A,$01           
6105: EA D6 D3   LD      ($D3D6),A       
6108: 1E 0C      LD      E,$0C           
610A: 21 02 D2   LD      HL,$D202        
610D: 7E         LD      A,(HL)          
610E: 3C         INC     A               
610F: 77         LD      (HL),A          
6110: BB         CP      E               
6111: 38 05      JR      C,$6118         
6113: 70         LD      (HL),B          
6114: 3E 38      LD      A,$38           
6116: E0 F2      LDFF00  ($F2),A         
6118: 21 D0 C3   LD      HL,$C3D0        
611B: 09         ADD     HL,BC           
611C: 7E         LD      A,(HL)          
611D: 3C         INC     A               
611E: E6 7F      AND     $7F             
6120: 77         LD      (HL),A          
6121: 5F         LD      E,A             
6122: 50         LD      D,B             
6123: 21 00 D0   LD      HL,$D000        
6126: 19         ADD     HL,DE           
6127: F0 EE      LD      A,($EE)         
6129: 77         LD      (HL),A          
612A: 21 00 D1   LD      HL,$D100        
612D: 19         ADD     HL,DE           
612E: F0 EC      LD      A,($EC)         
6130: 77         LD      (HL),A          
6131: CD 41 63   CALL    $6341           
6134: 21 B0 C2   LD      HL,$C2B0        
6137: 09         ADD     HL,BC           
6138: 5E         LD      E,(HL)          
6139: CB 3B      SET     1,E             
613B: 50         LD      D,B             
613C: 21 D6 5F   LD      HL,$5FD6        
613F: 19         ADD     HL,DE           
6140: 7E         LD      A,(HL)          
6141: CD 87 3B   CALL    $3B87           
6144: C9         RET                     
6145: F8 F8      LDHL    SP,$F8          
6147: 60         LD      H,B             
6148: 00         NOP                     
6149: F8 00      LDHL    SP,$00          
614B: 62         LD      H,D             
614C: 00         NOP                     
614D: F8 08      LDHL    SP,$08          
614F: 62         LD      H,D             
6150: 20 F8      JR      NZ,$614A        
6152: 10 60      STOP    $60             
6154: 20 08      JR      NZ,$615E        
6156: F8 64      LDHL    SP,$64          
6158: 00         NOP                     
6159: 08 00 66   LD      ($6600),SP      
615C: 00         NOP                     
615D: 08 08 66   LD      ($6608),SP      
6160: 20 08      JR      NZ,$616A        
6162: 10 64      STOP    $64             
6164: 20 F8      JR      NZ,$615E        
6166: F8 60      LDHL    SP,$60          
6168: 00         NOP                     
6169: F8 00      LDHL    SP,$00          
616B: 62         LD      H,D             
616C: 00         NOP                     
616D: F8 08      LDHL    SP,$08          
616F: 62         LD      H,D             
6170: 20 F8      JR      NZ,$616A        
6172: 10 60      STOP    $60             
6174: 20 08      JR      NZ,$617E        
6176: F8 6C      LDHL    SP,$6C          
6178: 00         NOP                     
6179: 08 00 6E   LD      ($6E00),SP      
617C: 00         NOP                     
617D: 08 08 62   LD      ($6208),SP      
6180: 60         LD      H,B             
6181: 08 10 60   LD      ($6010),SP      
6184: 60         LD      H,B             
6185: F8 F8      LDHL    SP,$F8          
6187: 68         LD      L,B             
6188: 00         NOP                     
6189: F8 00      LDHL    SP,$00          
618B: 6A         LD      L,D             
618C: 00         NOP                     
618D: F8 08      LDHL    SP,$08          
618F: 62         LD      H,D             
6190: 20 F8      JR      NZ,$618A        
6192: 10 60      STOP    $60             
6194: 20 08      JR      NZ,$619E        
6196: F8 68      LDHL    SP,$68          
6198: 40         LD      B,B             
6199: 08 00 6A   LD      ($6A00),SP      
619C: 40         LD      B,B             
619D: 08 08 62   LD      ($6208),SP      
61A0: 60         LD      H,B             
61A1: 08 10 60   LD      ($6010),SP      
61A4: 60         LD      H,B             
61A5: F8 F8      LDHL    SP,$F8          
61A7: 6C         LD      L,H             
61A8: 40         LD      B,B             
61A9: F8 00      LDHL    SP,$00          
61AB: 6E         LD      L,(HL)          
61AC: 40         LD      B,B             
61AD: F8 08      LDHL    SP,$08          
61AF: 62         LD      H,D             
61B0: 20 F8      JR      NZ,$61AA        
61B2: 10 60      STOP    $60             
61B4: 20 08      JR      NZ,$61BE        
61B6: F8 60      LDHL    SP,$60          
61B8: 40         LD      B,B             
61B9: 08 00 62   LD      ($6200),SP      
61BC: 40         LD      B,B             
61BD: 08 08 62   LD      ($6208),SP      
61C0: 60         LD      H,B             
61C1: 08 10 60   LD      ($6010),SP      
61C4: 60         LD      H,B             
61C5: F8 F8      LDHL    SP,$F8          
61C7: 64         LD      H,H             
61C8: 40         LD      B,B             
61C9: F8 00      LDHL    SP,$00          
61CB: 66         LD      H,(HL)          
61CC: 40         LD      B,B             
61CD: F8 08      LDHL    SP,$08          
61CF: 66         LD      H,(HL)          
61D0: 60         LD      H,B             
61D1: F8 10      LDHL    SP,$10          
61D3: 64         LD      H,H             
61D4: 60         LD      H,B             
61D5: 08 F8 60   LD      ($60F8),SP      
61D8: 40         LD      B,B             
61D9: 08 00 62   LD      ($6200),SP      
61DC: 40         LD      B,B             
61DD: 08 08 62   LD      ($6208),SP      
61E0: 60         LD      H,B             
61E1: 08 10 60   LD      ($6010),SP      
61E4: 60         LD      H,B             
61E5: F8 F8      LDHL    SP,$F8          
61E7: 60         LD      H,B             
61E8: 00         NOP                     
61E9: F8 00      LDHL    SP,$00          
61EB: 62         LD      H,D             
61EC: 00         NOP                     
61ED: F8 08      LDHL    SP,$08          
61EF: 6E         LD      L,(HL)          
61F0: 60         LD      H,B             
61F1: F8 10      LDHL    SP,$10          
61F3: 6C         LD      L,H             
61F4: 60         LD      H,B             
61F5: 08 F8 60   LD      ($60F8),SP      
61F8: 40         LD      B,B             
61F9: 08 00 62   LD      ($6200),SP      
61FC: 40         LD      B,B             
61FD: 08 08 62   LD      ($6208),SP      
6200: 60         LD      H,B             
6201: 08 10 60   LD      ($6010),SP      
6204: 60         LD      H,B             
6205: F8 F8      LDHL    SP,$F8          
6207: 60         LD      H,B             
6208: 00         NOP                     
6209: F8 00      LDHL    SP,$00          
620B: 62         LD      H,D             
620C: 00         NOP                     
620D: F8 08      LDHL    SP,$08          
620F: 6A         LD      L,D             
6210: 20 F8      JR      NZ,$620A        
6212: 10 68      STOP    $68             
6214: 20 08      JR      NZ,$621E        
6216: F8 60      LDHL    SP,$60          
6218: 40         LD      B,B             
6219: 08 00 62   LD      ($6200),SP      
621C: 40         LD      B,B             
621D: 08 08 6A   LD      ($6A08),SP      
6220: 60         LD      H,B             
6221: 08 10 68   LD      ($6810),SP      
6224: 60         LD      H,B             
6225: F8 F8      LDHL    SP,$F8          
6227: 60         LD      H,B             
6228: 00         NOP                     
6229: F8 00      LDHL    SP,$00          
622B: 62         LD      H,D             
622C: 00         NOP                     
622D: F8 08      LDHL    SP,$08          
622F: 62         LD      H,D             
6230: 20 F8      JR      NZ,$622A        
6232: 10 60      STOP    $60             
6234: 20 08      JR      NZ,$623E        
6236: F8 60      LDHL    SP,$60          
6238: 40         LD      B,B             
6239: 08 00 62   LD      ($6200),SP      
623C: 40         LD      B,B             
623D: 08 08 6E   LD      ($6E08),SP      
6240: 20 08      JR      NZ,$624A        
6242: 10 6C      STOP    $6C             
6244: 20 70      JR      NZ,$62B6        
6246: 00         NOP                     
6247: 70         LD      (HL),B          
6248: 20 72      JR      NZ,$62BC        
624A: 00         NOP                     
624B: 72         LD      (HL),D          
624C: 20 74      JR      NZ,$62C2        
624E: 00         NOP                     
624F: 74         LD      (HL),H          
6250: 20 76      JR      NZ,$62C8        
6252: 00         NOP                     
6253: 76         HALT                    
6254: 20 21      JR      NZ,$6277        
6256: 40         LD      B,B             
6257: C3 09 36   JP      $3609           
625A: 48         LD      C,B             
625B: 21 B0 C3   LD      HL,$C3B0        
625E: 09         ADD     HL,BC           
625F: 7E         LD      A,(HL)          
6260: 17         RLA                     
6261: 17         RLA                     
6262: 17         RLA                     
6263: 17         RLA                     
6264: 17         RLA                     
6265: E6 E0      AND     $E0             
6267: 5F         LD      E,A             
6268: 50         LD      D,B             
6269: 21 45 61   LD      HL,$6145        
626C: 19         ADD     HL,DE           
626D: 0E 08      LD      C,$08           
626F: CD 26 3D   CALL    $3D26           
6272: 21 40 C3   LD      HL,$C340        
6275: 09         ADD     HL,BC           
6276: 36 42      LD      (HL),$42        
6278: 21 D0 C3   LD      HL,$C3D0        
627B: 09         ADD     HL,BC           
627C: 7E         LD      A,(HL)          
627D: E0 D7      LDFF00  ($D7),A         
627F: F0 D7      LD      A,($D7)         
6281: D6 0C      SUB     $0C             
6283: E6 7F      AND     $7F             
6285: 5F         LD      E,A             
6286: 50         LD      D,B             
6287: 21 00 D0   LD      HL,$D000        
628A: 19         ADD     HL,DE           
628B: 7E         LD      A,(HL)          
628C: E0 EE      LDFF00  ($EE),A         
628E: 21 00 D1   LD      HL,$D100        
6291: 19         ADD     HL,DE           
6292: 7E         LD      A,(HL)          
6293: E0 EC      LDFF00  ($EC),A         
6295: 3E 00      LD      A,$00           
6297: E0 F1      LDFF00  ($F1),A         
6299: 11 45 62   LD      DE,$6245        
629C: CD 3B 3C   CALL    $3C3B           
629F: F0 D7      LD      A,($D7)         
62A1: D6 18      SUB     $18             
62A3: E6 7F      AND     $7F             
62A5: 5F         LD      E,A             
62A6: 50         LD      D,B             
62A7: 21 00 D0   LD      HL,$D000        
62AA: 19         ADD     HL,DE           
62AB: 7E         LD      A,(HL)          
62AC: E0 EE      LDFF00  ($EE),A         
62AE: 21 00 D1   LD      HL,$D100        
62B1: 19         ADD     HL,DE           
62B2: 7E         LD      A,(HL)          
62B3: E0 EC      LDFF00  ($EC),A         
62B5: 3E 00      LD      A,$00           
62B7: E0 F1      LDFF00  ($F1),A         
62B9: 11 45 62   LD      DE,$6245        
62BC: CD 3B 3C   CALL    $3C3B           
62BF: F0 D7      LD      A,($D7)         
62C1: D6 24      SUB     $24             
62C3: E6 7F      AND     $7F             
62C5: 5F         LD      E,A             
62C6: 50         LD      D,B             
62C7: 21 00 D0   LD      HL,$D000        
62CA: 19         ADD     HL,DE           
62CB: 7E         LD      A,(HL)          
62CC: E0 EE      LDFF00  ($EE),A         
62CE: 21 00 D1   LD      HL,$D100        
62D1: 19         ADD     HL,DE           
62D2: 7E         LD      A,(HL)          
62D3: E0 EC      LDFF00  ($EC),A         
62D5: 3E 01      LD      A,$01           
62D7: E0 F1      LDFF00  ($F1),A         
62D9: 11 45 62   LD      DE,$6245        
62DC: CD 3B 3C   CALL    $3C3B           
62DF: F0 D7      LD      A,($D7)         
62E1: D6 2E      SUB     $2E             
62E3: E6 7F      AND     $7F             
62E5: 5F         LD      E,A             
62E6: 50         LD      D,B             
62E7: 21 00 D0   LD      HL,$D000        
62EA: 19         ADD     HL,DE           
62EB: 7E         LD      A,(HL)          
62EC: E0 EE      LDFF00  ($EE),A         
62EE: 21 00 D1   LD      HL,$D100        
62F1: 19         ADD     HL,DE           
62F2: 7E         LD      A,(HL)          
62F3: E0 EC      LDFF00  ($EC),A         
62F5: F0 E7      LD      A,($E7)         
62F7: 1F         RRA                     
62F8: 1F         RRA                     
62F9: 1F         RRA                     
62FA: E6 01      AND     $01             
62FC: C6 02      ADD     $02             
62FE: E0 F1      LDFF00  ($F1),A         
6300: F0 E7      LD      A,($E7)         
6302: 17         RLA                     
6303: 17         RLA                     
6304: E6 10      AND     $10             
6306: 21 ED FF   LD      HL,$FFED        
6309: AE         XOR     (HL)            
630A: 77         LD      (HL),A          
630B: 11 45 62   LD      DE,$6245        
630E: CD 3B 3C   CALL    $3C3B           
6311: F0 F0      LD      A,($F0)         
6313: FE 02      CP      $02             
6315: 30 29      JR      NC,$6340        
6317: 21 20 C4   LD      HL,$C420        
631A: 09         ADD     HL,BC           
631B: 7E         LD      A,(HL)          
631C: A7         AND     A               
631D: 20 21      JR      NZ,$6340        
631F: 21 30 C4   LD      HL,$C430        
6322: 09         ADD     HL,BC           
6323: 36 90      LD      (HL),$90        
6325: CD EB 3B   CALL    $3BEB           
6328: 21 30 C4   LD      HL,$C430        
632B: 09         ADD     HL,BC           
632C: 36 D0      LD      (HL),$D0        
632E: 21 60 C3   LD      HL,$C360        
6331: 09         ADD     HL,BC           
6332: 7E         LD      A,(HL)          
6333: FE F0      CP      $F0             
6335: 30 09      JR      NC,$6340        
6337: CD 8D 3B   CALL    $3B8D           
633A: 21 80 C4   LD      HL,$C480        
633D: 09         ADD     HL,BC           
633E: 36 50      LD      (HL),$50        
6340: C9         RET                     
6341: F0 F0      LD      A,($F0)         
6343: FE 02      CP      $02             
6345: 30 0B      JR      NC,$6352        
6347: 21 20 C4   LD      HL,$C420        
634A: 09         ADD     HL,BC           
634B: 7E         LD      A,(HL)          
634C: A7         AND     A               
634D: 20 03      JR      NZ,$6352        
634F: CD 8C 7B   CALL    $7B8C           
6352: CD 9E 3B   CALL    $3B9E           
6355: 21 A0 C2   LD      HL,$C2A0        
6358: 09         ADD     HL,BC           
6359: 7E         LD      A,(HL)          
635A: A7         AND     A               
635B: 28 2C      JR      Z,$6389         
635D: 1E 08      LD      E,$08           
635F: CB 47      SET     1,E             
6361: 20 0E      JR      NZ,$6371        
6363: 1E 00      LD      E,$00           
6365: CB 4F      SET     1,E             
6367: 20 08      JR      NZ,$6371        
6369: 1E 04      LD      E,$04           
636B: CB 57      SET     1,E             
636D: 20 02      JR      NZ,$6371        
636F: 1E 0C      LD      E,$0C           
6371: 21 B0 C2   LD      HL,$C2B0        
6374: 09         ADD     HL,BC           
6375: 73         LD      (HL),E          
6376: CD ED 27   CALL    $27ED           
6379: 1F         RRA                     
637A: 38 08      JR      C,$6384         
637C: 21 C0 C2   LD      HL,$C2C0        
637F: 09         ADD     HL,BC           
6380: 7E         LD      A,(HL)          
6381: 2F         CPL                     
6382: 3C         INC     A               
6383: 77         LD      (HL),A          
6384: CD 91 08   CALL    $0891           
6387: 36 10      LD      (HL),$10        
6389: CD 8C 08   CALL    $088C           
638C: 20 31      JR      NZ,$63BF        
638E: 36 06      LD      (HL),$06        
6390: 21 C0 C2   LD      HL,$C2C0        
6393: 09         ADD     HL,BC           
6394: 7E         LD      A,(HL)          
6395: 21 B0 C2   LD      HL,$C2B0        
6398: 09         ADD     HL,BC           
6399: 86         ADD     A,(HL)          
639A: E6 0F      AND     $0F             
639C: 77         LD      (HL),A          
639D: 21 B0 C2   LD      HL,$C2B0        
63A0: 09         ADD     HL,BC           
63A1: 5E         LD      E,(HL)          
63A2: 50         LD      D,B             
63A3: 21 B2 5F   LD      HL,$5FB2        
63A6: 19         ADD     HL,DE           
63A7: 7E         LD      A,(HL)          
63A8: CD 87 3B   CALL    $3B87           
63AB: 21 C2 5F   LD      HL,$5FC2        
63AE: 19         ADD     HL,DE           
63AF: 7E         LD      A,(HL)          
63B0: 21 50 C2   LD      HL,$C250        
63B3: 09         ADD     HL,BC           
63B4: 77         LD      (HL),A          
63B5: 21 C6 5F   LD      HL,$5FC6        
63B8: 19         ADD     HL,DE           
63B9: 7E         LD      A,(HL)          
63BA: 21 40 C2   LD      HL,$C240        
63BD: 09         ADD     HL,BC           
63BE: 77         LD      (HL),A          
63BF: CD 91 08   CALL    $0891           
63C2: 20 13      JR      NZ,$63D7        
63C4: CD ED 27   CALL    $27ED           
63C7: E6 1F      AND     $1F             
63C9: C6 10      ADD     $10             
63CB: 77         LD      (HL),A          
63CC: CD ED 27   CALL    $27ED           
63CF: E6 02      AND     $02             
63D1: 3D         DEC     A               
63D2: 21 C0 C2   LD      HL,$C2C0        
63D5: 09         ADD     HL,BC           
63D6: 77         LD      (HL),A          
63D7: C9         RET                     
63D8: 21 B0 C2   LD      HL,$C2B0        
63DB: 09         ADD     HL,BC           
63DC: 7E         LD      A,(HL)          
63DD: FE 03      CP      $03             
63DF: CA 5D 6D   JP      Z,$6D5D         
63E2: FE 02      CP      $02             
63E4: CA 8C 6D   JP      Z,$6D8C         
63E7: A7         AND     A               
63E8: C2 7E 6C   JP      NZ,$6C7E        
63EB: F0 F0      LD      A,($F0)         
63ED: FE 02      CP      $02             
63EF: 38 44      JR      C,$6435         
63F1: FE 0B      CP      $0B             
63F3: 28 04      JR      Z,$63F9         
63F5: FE 0C      CP      $0C             
63F7: 20 09      JR      NZ,$6402        
63F9: 3E 06      LD      A,$06           
63FB: E0 F1      LDFF00  ($F1),A         
63FD: CD 28 57   CALL    $5728           
6400: 18 03      JR      $6405           
6402: CD 43 69   CALL    $6943           
6405: CD 20 7B   CALL    $7B20           
6408: CD E2 08   CALL    $08E2           
640B: F0 F0      LD      A,($F0)         
640D: FE 09      CP      $09             
640F: 30 24      JR      NC,$6435        
6411: CD B4 3B   CALL    $3BB4           
6414: 21 60 C3   LD      HL,$C360        
6417: 09         ADD     HL,BC           
6418: 7E         LD      A,(HL)          
6419: FE E8      CP      $E8             
641B: 30 18      JR      NC,$6435        
641D: CD 8D 3B   CALL    $3B8D           
6420: 36 09      LD      (HL),$09        
6422: 3E 09      LD      A,$09           
6424: E0 F0      LDFF00  ($F0),A         
6426: 3E 10      LD      A,$10           
6428: E0 F3      LDFF00  ($F3),A         
642A: CD 91 08   CALL    $0891           
642D: 36 80      LD      (HL),$80        
642F: 21 20 C4   LD      HL,$C420        
6432: 09         ADD     HL,BC           
6433: 36 80      LD      (HL),$80        
6435: F0 F0      LD      A,($F0)         
6437: C7         RST     0X00            
6438: CC 64 1F   CALL    Z,$1F64         
643B: 65         LD      H,L             
643C: 65         LD      H,L             
643D: 65         LD      H,L             
643E: B8         CP      B               
643F: 65         LD      H,L             
6440: 2A         LD      A,(HLI)         
6441: 66         LD      H,(HL)          
6442: DE 66      SBC     $66             
6444: 66         LD      H,(HL)          
6445: 67         LD      H,A             
6446: A3         AND     E               
6447: 67         LD      H,A             
6448: F7         RST     0X30            
6449: 67         LD      H,A             
644A: F8 67      LDHL    SP,$67          
644C: 0F         RRCA                    
644D: 68         LD      L,B             
644E: 28 68      JR      Z,$64B8         
6450: AD         XOR     L               
6451: 68         LD      L,B             
6452: FF         RST     0X38            
6453: 68         LD      L,B             
6454: 00         NOP                     
6455: 00         NOP                     
6456: 4A         LD      C,D             
6457: 00         NOP                     
6458: 00         NOP                     
6459: 08 4A 20   LD      ($204A),SP      
645C: FF         RST     0X38            
645D: FF         RST     0X38            
645E: FF         RST     0X38            
645F: FF         RST     0X38            
6460: FF         RST     0X38            
6461: FF         RST     0X38            
6462: FF         RST     0X38            
6463: FF         RST     0X38            
6464: FF         RST     0X38            
6465: FF         RST     0X38            
6466: FF         RST     0X38            
6467: FF         RST     0X38            
6468: FF         RST     0X38            
6469: FF         RST     0X38            
646A: FF         RST     0X38            
646B: FF         RST     0X38            
646C: 00         NOP                     
646D: 00         NOP                     
646E: 4C         LD      C,H             
646F: 00         NOP                     
6470: 00         NOP                     
6471: 08 4C 20   LD      ($204C),SP      
6474: FF         RST     0X38            
6475: FF         RST     0X38            
6476: FF         RST     0X38            
6477: FF         RST     0X38            
6478: FF         RST     0X38            
6479: FF         RST     0X38            
647A: FF         RST     0X38            
647B: FF         RST     0X38            
647C: FF         RST     0X38            
647D: FF         RST     0X38            
647E: FF         RST     0X38            
647F: FF         RST     0X38            
6480: FF         RST     0X38            
6481: FF         RST     0X38            
6482: FF         RST     0X38            
6483: FF         RST     0X38            
6484: 00         NOP                     
6485: 00         NOP                     
6486: 4E         LD      C,(HL)          
6487: 00         NOP                     
6488: 00         NOP                     
6489: 08 4E 20   LD      ($204E),SP      
648C: FF         RST     0X38            
648D: FF         RST     0X38            
648E: FF         RST     0X38            
648F: FF         RST     0X38            
6490: FF         RST     0X38            
6491: FF         RST     0X38            
6492: FF         RST     0X38            
6493: FF         RST     0X38            
6494: FF         RST     0X38            
6495: FF         RST     0X38            
6496: FF         RST     0X38            
6497: FF         RST     0X38            
6498: FF         RST     0X38            
6499: FF         RST     0X38            
649A: FF         RST     0X38            
649B: FF         RST     0X38            
649C: F0 00      LD      A,($00)         
649E: 5C         LD      E,H             
649F: 00         NOP                     
64A0: F0 08      LD      A,($08)         
64A2: 5C         LD      E,H             
64A3: 20 00      JR      NZ,$64A5        
64A5: 00         NOP                     
64A6: 5E         LD      E,(HL)          
64A7: 00         NOP                     
64A8: 00         NOP                     
64A9: 08 5E 20   LD      ($205E),SP      
64AC: FF         RST     0X38            
64AD: FF         RST     0X38            
64AE: FF         RST     0X38            
64AF: FF         RST     0X38            
64B0: FF         RST     0X38            
64B1: FF         RST     0X38            
64B2: FF         RST     0X38            
64B3: FF         RST     0X38            
64B4: 00         NOP                     
64B5: FC                              
64B6: 6A         LD      L,D             
64B7: 00         NOP                     
64B8: 00         NOP                     
64B9: 04         INC     B               
64BA: 6C         LD      L,H             
64BB: 20 00      JR      NZ,$64BD        
64BD: 0C         INC     C               
64BE: 6A         LD      L,D             
64BF: 20 F3      JR      NZ,$64B4        
64C1: FC                              
64C2: 50         LD      D,B             
64C3: 00         NOP                     
64C4: F3         DI                      
64C5: 04         INC     B               
64C6: 52         LD      D,D             
64C7: 00         NOP                     
64C8: F3         DI                      
64C9: 0C         INC     C               
64CA: 6E         LD      L,(HL)          
64CB: 00         NOP                     
64CC: AF         XOR     A               
64CD: E0 F1      LDFF00  ($F1),A         
64CF: CD 87 3B   CALL    $3B87           
64D2: CD 28 57   CALL    $5728           
64D5: F0 98      LD      A,($98)         
64D7: F5         PUSH    AF              
64D8: F0 99      LD      A,($99)         
64DA: F5         PUSH    AF              
64DB: 3E 50      LD      A,$50           
64DD: E0 98      LDFF00  ($98),A         
64DF: 3E 30      LD      A,$30           
64E1: E0 99      LDFF00  ($99),A         
64E3: 3E 10      LD      A,$10           
64E5: CD 25 3C   CALL    $3C25           
64E8: 21 99 FF   LD      HL,$FF99        
64EB: F0 EC      LD      A,($EC)         
64ED: 96         SUB     (HL)            
64EE: C6 03      ADD     $03             
64F0: FE 06      CP      $06             
64F2: 30 14      JR      NC,$6508        
64F4: 21 98 FF   LD      HL,$FF98        
64F7: F0 EE      LD      A,($EE)         
64F9: 96         SUB     (HL)            
64FA: C6 03      ADD     $03             
64FC: FE 06      CP      $06             
64FE: 30 08      JR      NC,$6508        
6500: CD 91 08   CALL    $0891           
6503: 36 60      LD      (HL),$60        
6505: CD 8D 3B   CALL    $3B8D           
6508: F1         POP     AF              
6509: E0 99      LDFF00  ($99),A         
650B: F1         POP     AF              
650C: E0 98      LDFF00  ($98),A         
650E: CD 8C 7B   CALL    $7B8C           
6511: C9         RET                     
6512: 04         INC     B               
6513: 03         INC     BC              
6514: 02         LD      (BC),A          
6515: 01 00 00   LD      BC,$0000        
6518: 00         NOP                     
6519: 00         NOP                     
651A: 00         NOP                     
651B: 00         NOP                     
651C: 00         NOP                     
651D: 00         NOP                     
651E: 00         NOP                     
651F: CD 91 08   CALL    $0891           
6522: 20 1B      JR      NZ,$653F        
6524: EA 24 D2   LD      ($D224),A       
6527: 21 10 C2   LD      HL,$C210        
652A: 09         ADD     HL,BC           
652B: 7E         LD      A,(HL)          
652C: D6 08      SUB     $08             
652E: 77         LD      (HL),A          
652F: CD 91 08   CALL    $0891           
6532: 36 08      LD      (HL),$08        
6534: 3E 04      LD      A,$04           
6536: CD 87 3B   CALL    $3B87           
6539: CD D8 52   CALL    $52D8           
653C: C3 8D 3B   JP      $3B8D           
653F: 1F         RRA                     
6540: 1F         RRA                     
6541: 1F         RRA                     
6542: E6 0F      AND     $0F             
6544: 5F         LD      E,A             
6545: 50         LD      D,B             
6546: 21 12 65   LD      HL,$6512        
6549: 19         ADD     HL,DE           
654A: 7E         LD      A,(HL)          
654B: 17         RLA                     
654C: 17         RLA                     
654D: 17         RLA                     
654E: E6 F8      AND     $F8             
6550: 5F         LD      E,A             
6551: 17         RLA                     
6552: E6 F0      AND     $F0             
6554: 83         ADD     A,E             
6555: 5F         LD      E,A             
6556: 21 54 64   LD      HL,$6454        
6559: 19         ADD     HL,DE           
655A: 0E 06      LD      C,$06           
655C: CD 26 3D   CALL    $3D26           
655F: 3E 06      LD      A,$06           
6561: CD D0 3D   CALL    $3DD0           
6564: C9         RET                     
6565: CD 91 08   CALL    $0891           
6568: 20 0D      JR      NZ,$6577        
656A: 36 7F      LD      (HL),$7F        
656C: C3 8D 3B   JP      $3B8D           
656F: CD DF 7B   CALL    $7BDF           
6572: 7B         LD      A,E             
6573: EA 1E D2   LD      ($D21E),A       
6576: C9         RET                     
6577: C9         RET                     
6578: 04         INC     B               
6579: 04         INC     B               
657A: 04         INC     B               
657B: 04         INC     B               
657C: 04         INC     B               
657D: 04         INC     B               
657E: 04         INC     B               
657F: 04         INC     B               
6580: 04         INC     B               
6581: 04         INC     B               
6582: 04         INC     B               
6583: 04         INC     B               
6584: 04         INC     B               
6585: 04         INC     B               
6586: 04         INC     B               
6587: 04         INC     B               
6588: 00         NOP                     
6589: 00         NOP                     
658A: 00         NOP                     
658B: 00         NOP                     
658C: 00         NOP                     
658D: 00         NOP                     
658E: 00         NOP                     
658F: 00         NOP                     
6590: 00         NOP                     
6591: 00         NOP                     
6592: 00         NOP                     
6593: 00         NOP                     
6594: 00         NOP                     
6595: 00         NOP                     
6596: 00         NOP                     
6597: 00         NOP                     
6598: 05         DEC     B               
6599: 05         DEC     B               
659A: 05         DEC     B               
659B: 05         DEC     B               
659C: 05         DEC     B               
659D: 05         DEC     B               
659E: 05         DEC     B               
659F: 05         DEC     B               
65A0: 05         DEC     B               
65A1: 05         DEC     B               
65A2: 05         DEC     B               
65A3: 05         DEC     B               
65A4: 05         DEC     B               
65A5: 05         DEC     B               
65A6: 05         DEC     B               
65A7: 05         DEC     B               
65A8: 02         LD      (BC),A          
65A9: 07         RLCA                    
65AA: 08 00 00   LD      ($0000),SP      
65AD: 00         NOP                     
65AE: 00         NOP                     
65AF: 00         NOP                     
65B0: 00         NOP                     
65B1: 00         NOP                     
65B2: 00         NOP                     
65B3: 00         NOP                     
65B4: 00         NOP                     
65B5: 00         NOP                     
65B6: 00         NOP                     
65B7: 00         NOP                     
65B8: 3E 00      LD      A,$00           
65BA: EA 1E D2   LD      ($D21E),A       
65BD: CD 91 08   CALL    $0891           
65C0: 20 0B      JR      NZ,$65CD        
65C2: CD 87 08   CALL    $0887           
65C5: 36 4C      LD      (HL),$4C        
65C7: CD 6F 65   CALL    $656F           
65CA: C3 8D 3B   JP      $3B8D           
65CD: FE 40      CP      $40             
65CF: 20 05      JR      NZ,$65D6        
65D1: 21 F4 FF   LD      HL,$FFF4        
65D4: 36 19      LD      (HL),$19        
65D6: FE 58      CP      $58             
65D8: 20 05      JR      NZ,$65DF        
65DA: 21 F2 FF   LD      HL,$FFF2        
65DD: 36 39      LD      (HL),$39        
65DF: 1F         RRA                     
65E0: 1F         RRA                     
65E1: E6 3F      AND     $3F             
65E3: 5F         LD      E,A             
65E4: 50         LD      D,B             
65E5: 21 98 65   LD      HL,$6598        
65E8: 19         ADD     HL,DE           
65E9: 7E         LD      A,(HL)          
65EA: EA 24 D2   LD      ($D224),A       
65ED: 21 78 65   LD      HL,$6578        
65F0: 19         ADD     HL,DE           
65F1: 7E         LD      A,(HL)          
65F2: CD 87 3B   CALL    $3B87           
65F5: FA 24 D2   LD      A,($D224)       
65F8: FE 05      CP      $05             
65FA: 28 0B      JR      Z,$6607         
65FC: 3E F3      LD      A,$F3           
65FE: EA 25 D2   LD      ($D225),A       
6601: 3E F0      LD      A,$F0           
6603: EA 26 D2   LD      ($D226),A       
6606: C9         RET                     
6607: 3E F8      LD      A,$F8           
6609: EA 25 D2   LD      ($D225),A       
660C: 3E FE      LD      A,$FE           
660E: EA 26 D2   LD      ($D226),A       
6611: C9         RET                     
6612: 03         INC     BC              
6613: 02         LD      (BC),A          
6614: 01 00 00   LD      BC,$0000        
6617: 01 02 03   LD      BC,$0302        
661A: E8 00      ADD     SP,$00          
661C: 18 18      JR      $6636           
661E: 00         NOP                     
661F: E8 E8      ADD     SP,$E8          
6621: 00         NOP                     
6622: 10 18      STOP    $18             
6624: 10 F0      STOP    $F0             
6626: E8 F0      ADD     SP,$F0          
6628: 10 18      STOP    $18             
662A: CD 87 08   CALL    $0887           
662D: 20 0B      JR      NZ,$663A        
662F: EA 21 D2   LD      ($D221),A       
6632: CD 91 08   CALL    $0891           
6635: 36 30      LD      (HL),$30        
6637: C3 8D 3B   JP      $3B8D           
663A: FA 1E D2   LD      A,($D21E)       
663D: A7         AND     A               
663E: 3E F5      LD      A,$F5           
6640: 28 02      JR      Z,$6644         
6642: 3E 0B      LD      A,$0B           
6644: EA 25 D2   LD      ($D225),A       
6647: 3E EE      LD      A,$EE           
6649: EA 26 D2   LD      ($D226),A       
664C: F0 E7      LD      A,($E7)         
664E: 1F         RRA                     
664F: 1F         RRA                     
6650: 1F         RRA                     
6651: 00         NOP                     
6652: E6 01      AND     $01             
6654: CD 87 3B   CALL    $3B87           
6657: FA 1E D2   LD      A,($D21E)       
665A: A7         AND     A               
665B: 21 12 66   LD      HL,$6612        
665E: 28 03      JR      Z,$6663         
6660: 21 16 66   LD      HL,$6616        
6663: F0 E7      LD      A,($E7)         
6665: 1F         RRA                     
6666: 1F         RRA                     
6667: 1F         RRA                     
6668: 00         NOP                     
6669: 00         NOP                     
666A: E6 03      AND     $03             
666C: 5F         LD      E,A             
666D: 50         LD      D,B             
666E: 19         ADD     HL,DE           
666F: 7E         LD      A,(HL)          
6670: 3C         INC     A               
6671: EA 24 D2   LD      ($D224),A       
6674: F0 E7      LD      A,($E7)         
6676: E6 1F      AND     $1F             
6678: 20 5F      JR      NZ,$66D9        
667A: FA 21 D2   LD      A,($D221)       
667D: FE 06      CP      $06             
667F: 30 58      JR      NC,$66D9        
6681: 3E E6      LD      A,$E6           
6683: CD 01 3C   CALL    $3C01           
6686: D8         RET     C               
6687: 21 E0 C2   LD      HL,$C2E0        
668A: 19         ADD     HL,DE           
668B: 36 30      LD      (HL),$30        
668D: 21 B0 C2   LD      HL,$C2B0        
6690: 19         ADD     HL,DE           
6691: 36 02      LD      (HL),$02        
6693: C5         PUSH    BC              
6694: 21 40 C3   LD      HL,$C340        
6697: 19         ADD     HL,DE           
6698: 36 42      LD      (HL),$42        
669A: 21 50 C3   LD      HL,$C350        
669D: 19         ADD     HL,DE           
669E: 36 00      LD      (HL),$00        
66A0: D5         PUSH    DE              
66A1: D5         PUSH    DE              
66A2: C1         POP     BC              
66A3: CD 65 3B   CALL    $3B65           
66A6: D1         POP     DE              
66A7: FA 1E D2   LD      A,($D21E)       
66AA: A7         AND     A               
66AB: FA 21 D2   LD      A,($D221)       
66AE: 20 02      JR      NZ,$66B2        
66B0: EE 07      XOR     $07             
66B2: 4F         LD      C,A             
66B3: 21 22 66   LD      HL,$6622        
66B6: 09         ADD     HL,BC           
66B7: FA 25 D2   LD      A,($D225)       
66BA: 86         ADD     A,(HL)          
66BB: 21 D7 FF   LD      HL,$FFD7        
66BE: 86         ADD     A,(HL)          
66BF: 21 00 C2   LD      HL,$C200        
66C2: 19         ADD     HL,DE           
66C3: 77         LD      (HL),A          
66C4: 21 1A 66   LD      HL,$661A        
66C7: 09         ADD     HL,BC           
66C8: 7E         LD      A,(HL)          
66C9: D6 0C      SUB     $0C             
66CB: 21 D8 FF   LD      HL,$FFD8        
66CE: 86         ADD     A,(HL)          
66CF: 21 10 C2   LD      HL,$C210        
66D2: 19         ADD     HL,DE           
66D3: 77         LD      (HL),A          
66D4: 21 21 D2   LD      HL,$D221        
66D7: 34         INC     (HL)            
66D8: C1         POP     BC              
66D9: C9         RET                     
66DA: 0B         DEC     BC              
66DB: 0A         LD      A,(BC)          
66DC: 02         LD      (BC),A          
66DD: 0A         LD      A,(BC)          
66DE: FA 1E D2   LD      A,($D21E)       
66E1: A7         AND     A               
66E2: 3E FD      LD      A,$FD           
66E4: 28 02      JR      Z,$66E8         
66E6: 3E 03      LD      A,$03           
66E8: EA 25 D2   LD      ($D225),A       
66EB: 3E EC      LD      A,$EC           
66ED: EA 26 D2   LD      ($D226),A       
66F0: F0 E7      LD      A,($E7)         
66F2: 1F         RRA                     
66F3: 1F         RRA                     
66F4: 1F         RRA                     
66F5: 00         NOP                     
66F6: 00         NOP                     
66F7: E6 03      AND     $03             
66F9: 5F         LD      E,A             
66FA: 50         LD      D,B             
66FB: 21 DA 66   LD      HL,$66DA        
66FE: 19         ADD     HL,DE           
66FF: 7E         LD      A,(HL)          
6700: 3C         INC     A               
6701: EA 24 D2   LD      ($D224),A       
6704: CD 91 08   CALL    $0891           
6707: 20 57      JR      NZ,$6760        
6709: 36 40      LD      (HL),$40        
670B: AF         XOR     A               
670C: EA 24 D2   LD      ($D224),A       
670F: CD 8D 3B   CALL    $3B8D           
6712: 3E E6      LD      A,$E6           
6714: CD 01 3C   CALL    $3C01           
6717: 38 47      JR      C,$6760         
6719: 21 B0 C2   LD      HL,$C2B0        
671C: 19         ADD     HL,DE           
671D: 34         INC     (HL)            
671E: F0 D8      LD      A,($D8)         
6720: D6 10      SUB     $10             
6722: 21 10 C2   LD      HL,$C210        
6725: 19         ADD     HL,DE           
6726: 77         LD      (HL),A          
6727: FA 1E D2   LD      A,($D21E)       
672A: 21 80 C3   LD      HL,$C380        
672D: 19         ADD     HL,DE           
672E: 77         LD      (HL),A          
672F: A7         AND     A               
6730: 3E 08      LD      A,$08           
6732: 20 02      JR      NZ,$6736        
6734: 3E F8      LD      A,$F8           
6736: 21 D7 FF   LD      HL,$FFD7        
6739: 86         ADD     A,(HL)          
673A: 21 00 C2   LD      HL,$C200        
673D: 19         ADD     HL,DE           
673E: 77         LD      (HL),A          
673F: 21 40 C3   LD      HL,$C340        
6742: 19         ADD     HL,DE           
6743: 36 40      LD      (HL),$40        
6745: 21 50 C3   LD      HL,$C350        
6748: 19         ADD     HL,DE           
6749: 36 08      LD      (HL),$08        
674B: C5         PUSH    BC              
674C: D5         PUSH    DE              
674D: C1         POP     BC              
674E: CD 65 3B   CALL    $3B65           
6751: 3E 18      LD      A,$18           
6753: CD 25 3C   CALL    $3C25           
6756: CD 91 08   CALL    $0891           
6759: 36 30      LD      (HL),$30        
675B: 3E 27      LD      A,$27           
675D: E0 F4      LDFF00  ($F4),A         
675F: C1         POP     BC              
6760: 3E 02      LD      A,$02           
6762: CD 87 3B   CALL    $3B87           
6765: C9         RET                     
6766: CD 91 08   CALL    $0891           
6769: 20 12      JR      NZ,$677D        
676B: 36 1F      LD      (HL),$1F        
676D: CD ED 27   CALL    $27ED           
6770: E6 07      AND     $07             
6772: 21 C0 C2   LD      HL,$C2C0        
6775: 09         ADD     HL,BC           
6776: 77         LD      (HL),A          
6777: CD 40 51   CALL    $5140           
677A: CD 8D 3B   CALL    $3B8D           
677D: 3E 03      LD      A,$03           
677F: CD 87 3B   CALL    $3B87           
6782: C9         RET                     
6783: 28 50      JR      Z,$67D5         
6785: 78         LD      A,B             
6786: 28 78      JR      Z,$6800         
6788: 28 50      JR      Z,$67DA         
678A: 78         LD      A,B             
678B: 20 28      JR      NZ,$67B5        
678D: 20 30      JR      NZ,$67BF        
678F: 30 50      JR      NC,$67E1        
6791: 50         LD      D,B             
6792: 50         LD      D,B             
6793: 20 1E      JR      NZ,$67B3        
6795: 1C         INC     E               
6796: 1A         LD      A,(DE)          
6797: 18 16      JR      $67AF           
6799: 14         INC     D               
679A: 12         LD      (DE),A          
679B: 10 0E      STOP    $0E             
679D: 0C         INC     C               
679E: 0A         LD      A,(BC)          
679F: 08 06 04   LD      ($0406),SP      
67A2: 02         LD      (BC),A          
67A3: 3E 04      LD      A,$04           
67A5: CD 87 3B   CALL    $3B87           
67A8: F0 98      LD      A,($98)         
67AA: F5         PUSH    AF              
67AB: F0 99      LD      A,($99)         
67AD: F5         PUSH    AF              
67AE: 21 C0 C2   LD      HL,$C2C0        
67B1: 09         ADD     HL,BC           
67B2: 5E         LD      E,(HL)          
67B3: 50         LD      D,B             
67B4: 21 83 67   LD      HL,$6783        
67B7: 19         ADD     HL,DE           
67B8: 7E         LD      A,(HL)          
67B9: E0 98      LDFF00  ($98),A         
67BB: 21 8B 67   LD      HL,$678B        
67BE: 19         ADD     HL,DE           
67BF: 7E         LD      A,(HL)          
67C0: E0 99      LDFF00  ($99),A         
67C2: CD 91 08   CALL    $0891           
67C5: 1F         RRA                     
67C6: E6 0F      AND     $0F             
67C8: 5F         LD      E,A             
67C9: 50         LD      D,B             
67CA: 21 93 67   LD      HL,$6793        
67CD: 19         ADD     HL,DE           
67CE: 7E         LD      A,(HL)          
67CF: CD 25 3C   CALL    $3C25           
67D2: 21 EE FF   LD      HL,$FFEE        
67D5: F0 98      LD      A,($98)         
67D7: 96         SUB     (HL)            
67D8: C6 03      ADD     $03             
67DA: FE 06      CP      $06             
67DC: 30 0F      JR      NC,$67ED        
67DE: 21 EC FF   LD      HL,$FFEC        
67E1: F0 99      LD      A,($99)         
67E3: 96         SUB     (HL)            
67E4: C6 03      ADD     $03             
67E6: FE 06      CP      $06             
67E8: 30 03      JR      NC,$67ED        
67EA: CD 8D 3B   CALL    $3B8D           
67ED: F1         POP     AF              
67EE: E0 99      LDFF00  ($99),A         
67F0: F1         POP     AF              
67F1: E0 98      LDFF00  ($98),A         
67F3: CD 8C 7B   CALL    $7B8C           
67F6: C9         RET                     
67F7: C9         RET                     
67F8: CD 91 08   CALL    $0891           
67FB: 20 11      JR      NZ,$680E        
67FD: 36 40      LD      (HL),$40        
67FF: CD 58 54   CALL    $5458           
6802: CD 8D 3B   CALL    $3B8D           
6805: 3E 00      LD      A,$00           
6807: CD 87 3B   CALL    $3B87           
680A: AF         XOR     A               
680B: EA 24 D2   LD      ($D224),A       
680E: C9         RET                     
680F: 3E 06      LD      A,$06           
6811: E0 F1      LDFF00  ($F1),A         
6813: CD 28 57   CALL    $5728           
6816: CD 91 08   CALL    $0891           
6819: 20 0C      JR      NZ,$6827        
681B: 21 40 C3   LD      HL,$C340        
681E: 09         ADD     HL,BC           
681F: CB B6      SET     1,E             
6821: CD 8D 3B   CALL    $3B8D           
6824: CD AF 3D   CALL    $3DAF           
6827: C9         RET                     
6828: CD B4 3B   CALL    $3BB4           
682B: CD 8C 7B   CALL    $7B8C           
682E: CD 9E 3B   CALL    $3B9E           
6831: F0 E7      LD      A,($E7)         
6833: E6 01      AND     $01             
6835: 20 1F      JR      NZ,$6856        
6837: 3E 18      LD      A,$18           
6839: CD 30 3C   CALL    $3C30           
683C: F0 D7      LD      A,($D7)         
683E: 21 50 C2   LD      HL,$C250        
6841: 96         SUB     (HL)            
6842: CB 7F      SET     1,E             
6844: 28 02      JR      Z,$6848         
6846: 35         DEC     (HL)            
6847: 35         DEC     (HL)            
6848: 34         INC     (HL)            
6849: F0 D8      LD      A,($D8)         
684B: 21 40 C2   LD      HL,$C240        
684E: 96         SUB     (HL)            
684F: CB 7F      SET     1,E             
6851: 28 02      JR      Z,$6855         
6853: 35         DEC     (HL)            
6854: 35         DEC     (HL)            
6855: 34         INC     (HL)            
6856: 21 20 C4   LD      HL,$C420        
6859: 09         ADD     HL,BC           
685A: 7E         LD      A,(HL)          
685B: A7         AND     A               
685C: 28 18      JR      Z,$6876         
685E: 21 40 C3   LD      HL,$C340        
6861: 09         ADD     HL,BC           
6862: CB F6      SET     1,E             
6864: CD 91 08   CALL    $0891           
6867: 36 80      LD      (HL),$80        
6869: CD D2 27   CALL    $27D2           
686C: 3E 10      LD      A,$10           
686E: E0 F3      LDFF00  ($F3),A         
6870: CD AD 53   CALL    $53AD           
6873: C3 8D 3B   JP      $3B8D           
6876: 21 D0 C3   LD      HL,$C3D0        
6879: 09         ADD     HL,BC           
687A: 7E         LD      A,(HL)          
687B: 3C         INC     A               
687C: 77         LD      (HL),A          
687D: E6 07      AND     $07             
687F: C0         RET     NZ              
6880: 3E E6      LD      A,$E6           
6882: CD 01 3C   CALL    $3C01           
6885: D8         RET     C               
6886: F0 D7      LD      A,($D7)         
6888: 21 00 C2   LD      HL,$C200        
688B: 19         ADD     HL,DE           
688C: 77         LD      (HL),A          
688D: F0 D8      LD      A,($D8)         
688F: 21 10 C2   LD      HL,$C210        
6892: 19         ADD     HL,DE           
6893: 77         LD      (HL),A          
6894: 21 B0 C2   LD      HL,$C2B0        
6897: 19         ADD     HL,DE           
6898: 36 03      LD      (HL),$03        
689A: 21 E0 C2   LD      HL,$C2E0        
689D: 19         ADD     HL,DE           
689E: 36 1F      LD      (HL),$1F        
68A0: 21 40 C3   LD      HL,$C340        
68A3: 19         ADD     HL,DE           
68A4: 36 C2      LD      (HL),$C2        
68A6: 21 B0 C3   LD      HL,$C3B0        
68A9: 19         ADD     HL,DE           
68AA: 36 01      LD      (HL),$01        
68AC: C9         RET                     
68AD: CD 91 08   CALL    $0891           
68B0: FE 01      CP      $01             
68B2: 20 04      JR      NZ,$68B8        
68B4: 35         DEC     (HL)            
68B5: C3 40 51   JP      $5140           
68B8: A7         AND     A               
68B9: C0         RET     NZ              
68BA: F0 98      LD      A,($98)         
68BC: F5         PUSH    AF              
68BD: F0 99      LD      A,($99)         
68BF: F5         PUSH    AF              
68C0: 3E 50      LD      A,$50           
68C2: E0 98      LDFF00  ($98),A         
68C4: 3E 30      LD      A,$30           
68C6: E0 99      LDFF00  ($99),A         
68C8: 3E 0C      LD      A,$0C           
68CA: CD 25 3C   CALL    $3C25           
68CD: 21 99 FF   LD      HL,$FF99        
68D0: F0 EC      LD      A,($EC)         
68D2: 96         SUB     (HL)            
68D3: C6 03      ADD     $03             
68D5: FE 06      CP      $06             
68D7: 30 14      JR      NC,$68ED        
68D9: 21 98 FF   LD      HL,$FF98        
68DC: F0 EE      LD      A,($EE)         
68DE: 96         SUB     (HL)            
68DF: C6 03      ADD     $03             
68E1: FE 06      CP      $06             
68E3: 30 08      JR      NC,$68ED        
68E5: CD 91 08   CALL    $0891           
68E8: 36 5F      LD      (HL),$5F        
68EA: CD 8D 3B   CALL    $3B8D           
68ED: F1         POP     AF              
68EE: E0 99      LDFF00  ($99),A         
68F0: F1         POP     AF              
68F1: E0 98      LDFF00  ($98),A         
68F3: CD 8C 7B   CALL    $7B8C           
68F6: C9         RET                     
68F7: 00         NOP                     
68F8: 00         NOP                     
68F9: 00         NOP                     
68FA: 01 01 01   LD      BC,$0101        
68FD: 02         LD      (BC),A          
68FE: 02         LD      (BC),A          
68FF: CD 91 08   CALL    $0891           
6902: 20 28      JR      NZ,$692C        
6904: CD AF 3D   CALL    $3DAF           
6907: CD E2 52   CALL    $52E2           
690A: 21 60 C3   LD      HL,$C360        
690D: 09         ADD     HL,BC           
690E: 36 FF      LD      (HL),$FF        
6910: 21 40 C3   LD      HL,$C340        
6913: 09         ADD     HL,BC           
6914: 36 00      LD      (HL),$00        
6916: 21 30 C4   LD      HL,$C430        
6919: 09         ADD     HL,BC           
691A: 36 C0      LD      (HL),$C0        
691C: CD 87 08   CALL    $0887           
691F: 36 90      LD      (HL),$90        
6921: AF         XOR     A               
6922: EA 23 D2   LD      ($D223),A       
6925: 21 00 C3   LD      HL,$C300        
6928: 09         ADD     HL,BC           
6929: 36 3F      LD      (HL),$3F        
692B: C9         RET                     
692C: FE 20      CP      $20             
692E: 38 02      JR      C,$6932         
6930: 3E 1F      LD      A,$1F           
6932: 1F         RRA                     
6933: 1F         RRA                     
6934: E6 07      AND     $07             
6936: 5F         LD      E,A             
6937: 50         LD      D,B             
6938: 21 F7 68   LD      HL,$68F7        
693B: 19         ADD     HL,DE           
693C: 7E         LD      A,(HL)          
693D: E0 F1      LDFF00  ($F1),A         
693F: CD 28 57   CALL    $5728           
6942: C9         RET                     
6943: F0 F0      LD      A,($F0)         
6945: FE 0A      CP      $0A             
6947: D0         RET     NC              
6948: F0 F1      LD      A,($F1)         
694A: 3C         INC     A               
694B: C8         RET     Z               
694C: FA 1E D2   LD      A,($D21E)       
694F: A7         AND     A               
6950: F0 F1      LD      A,($F1)         
6952: 28 02      JR      Z,$6956         
6954: C6 05      ADD     $05             
6956: E0 F1      LDFF00  ($F1),A         
6958: CD EC 69   CALL    $69EC           
695B: CD 84 6A   CALL    $6A84           
695E: CD 2C 6C   CALL    $6C2C           
6961: C9         RET                     
6962: F8 FC      LDHL    SP,$FC          
6964: 50         LD      D,B             
6965: 00         NOP                     
6966: F8 04      LDHL    SP,$04          
6968: 52         LD      D,D             
6969: 00         NOP                     
696A: F8 0C      LDHL    SP,$0C          
696C: 6E         LD      L,(HL)          
696D: 00         NOP                     
696E: 08 F8 6A   LD      ($6AF8),SP      
6971: 00         NOP                     
6972: 08 00 6C   LD      ($6C00),SP      
6975: 00         NOP                     
6976: 08 08 6C   LD      ($6C08),SP      
6979: 20 08      JR      NZ,$6983        
697B: 10 6A      STOP    $6A             
697D: 20 FF      JR      NZ,$697E        
697F: FF         RST     0X38            
6980: FF         RST     0X38            
6981: FF         RST     0X38            
6982: FB         EI                      
6983: FE 50      CP      $50             
6985: 00         NOP                     
6986: FB         EI                      
6987: 06 52      LD      B,$52           
6989: 00         NOP                     
698A: FB         EI                      
698B: 0E 6E      LD      C,$6E           
698D: 00         NOP                     
698E: 08 F8 6A   LD      ($6AF8),SP      
6991: 00         NOP                     
6992: 08 00 6C   LD      ($6C00),SP      
6995: 00         NOP                     
6996: 08 08 6C   LD      ($6C08),SP      
6999: 20 08      JR      NZ,$69A3        
699B: 10 6A      STOP    $6A             
699D: 20 FF      JR      NZ,$699E        
699F: FF         RST     0X38            
69A0: FF         RST     0X38            
69A1: FF         RST     0X38            
69A2: F8 FC      LDHL    SP,$FC          
69A4: 6E         LD      L,(HL)          
69A5: 20 F8      JR      NZ,$699F        
69A7: 04         INC     B               
69A8: 52         LD      D,D             
69A9: 20 F8      JR      NZ,$69A3        
69AB: 0C         INC     C               
69AC: 50         LD      D,B             
69AD: 20 08      JR      NZ,$69B7        
69AF: F8 6A      LDHL    SP,$6A          
69B1: 00         NOP                     
69B2: 08 00 6C   LD      ($6C00),SP      
69B5: 00         NOP                     
69B6: 08 08 6C   LD      ($6C08),SP      
69B9: 20 08      JR      NZ,$69C3        
69BB: 10 6A      STOP    $6A             
69BD: 20 FF      JR      NZ,$69BE        
69BF: FF         RST     0X38            
69C0: FF         RST     0X38            
69C1: FF         RST     0X38            
69C2: FB         EI                      
69C3: FA 6E 20   LD      A,($206E)       
69C6: FB         EI                      
69C7: 02         LD      (BC),A          
69C8: 52         LD      D,D             
69C9: 20 FB      JR      NZ,$69C6        
69CB: 0A         LD      A,(BC)          
69CC: 50         LD      D,B             
69CD: 20 08      JR      NZ,$69D7        
69CF: F8 6A      LDHL    SP,$6A          
69D1: 00         NOP                     
69D2: 08 00 6C   LD      ($6C00),SP      
69D5: 00         NOP                     
69D6: 08 08 6C   LD      ($6C08),SP      
69D9: 20 08      JR      NZ,$69E3        
69DB: 10 6A      STOP    $6A             
69DD: 20 FF      JR      NZ,$69DE        
69DF: FF         RST     0X38            
69E0: FF         RST     0X38            
69E1: FF         RST     0X38            
69E2: 00         NOP                     
69E3: 00         NOP                     
69E4: 02         LD      (BC),A          
69E5: 01 00 02   LD      BC,$0200        
69E8: 02         LD      (BC),A          
69E9: 00         NOP                     
69EA: 03         INC     BC              
69EB: 02         LD      (BC),A          
69EC: F0 F1      LD      A,($F1)         
69EE: 5F         LD      E,A             
69EF: 50         LD      D,B             
69F0: 21 E2 69   LD      HL,$69E2        
69F3: 19         ADD     HL,DE           
69F4: 7E         LD      A,(HL)          
69F5: 17         RLA                     
69F6: 17         RLA                     
69F7: 17         RLA                     
69F8: 17         RLA                     
69F9: 17         RLA                     
69FA: E6 70      AND     $70             
69FC: 5F         LD      E,A             
69FD: 21 62 69   LD      HL,$6962        
6A00: 19         ADD     HL,DE           
6A01: 0E 07      LD      C,$07           
6A03: CD 26 3D   CALL    $3D26           
6A06: 3E 07      LD      A,$07           
6A08: CD D0 3D   CALL    $3DD0           
6A0B: C9         RET                     
6A0C: F4                              
6A0D: F8 64      LDHL    SP,$64          
6A0F: 00         NOP                     
6A10: FE 11      CP      $11             
6A12: 60         LD      H,B             
6A13: 00         NOP                     
6A14: FE 19      CP      $19             
6A16: 62         LD      H,D             
6A17: 00         NOP                     
6A18: F4                              
6A19: F9         LD      SP,HL           
6A1A: 64         LD      H,H             
6A1B: 00         NOP                     
6A1C: FE 11      CP      $11             
6A1E: 60         LD      H,B             
6A1F: 00         NOP                     
6A20: FE 19      CP      $19             
6A22: 62         LD      H,D             
6A23: 00         NOP                     
6A24: F0 00      LD      A,($00)         
6A26: 64         LD      H,H             
6A27: 20 FF      JR      NZ,$6A28        
6A29: FF         RST     0X38            
6A2A: FF         RST     0X38            
6A2B: FF         RST     0X38            
6A2C: FF         RST     0X38            
6A2D: FF         RST     0X38            
6A2E: FF         RST     0X38            
6A2F: FF         RST     0X38            
6A30: FF         RST     0X38            
6A31: FF         RST     0X38            
6A32: FF         RST     0X38            
6A33: FF         RST     0X38            
6A34: FB         EI                      
6A35: 10 60      STOP    $60             
6A37: 00         NOP                     
6A38: FB         EI                      
6A39: 18 62      JR      $6A9D           
6A3B: 00         NOP                     
6A3C: 00         NOP                     
6A3D: F8 66      LDHL    SP,$66          
6A3F: 00         NOP                     
6A40: FE 10      CP      $10             
6A42: 66         LD      H,(HL)          
6A43: 20 FF      JR      NZ,$6A44        
6A45: FF         RST     0X38            
6A46: FF         RST     0X38            
6A47: FF         RST     0X38            
6A48: F4                              
6A49: 10 64      STOP    $64             
6A4B: 20 FE      JR      NZ,$6A4B        
6A4D: EF         RST     0X28            
6A4E: 62         LD      H,D             
6A4F: 20 FE      JR      NZ,$6A4F        
6A51: F7         RST     0X30            
6A52: 60         LD      H,B             
6A53: 20 F4      JR      NZ,$6A49        
6A55: 0F         RRCA                    
6A56: 64         LD      H,H             
6A57: 20 FE      JR      NZ,$6A57        
6A59: EF         RST     0X28            
6A5A: 62         LD      H,D             
6A5B: 20 FE      JR      NZ,$6A5B        
6A5D: F7         RST     0X30            
6A5E: 60         LD      H,B             
6A5F: 20 F0      JR      NZ,$6A51        
6A61: 08 64 00   LD      ($0064),SP      
6A64: FF         RST     0X38            
6A65: FF         RST     0X38            
6A66: FF         RST     0X38            
6A67: FF         RST     0X38            
6A68: FF         RST     0X38            
6A69: FF         RST     0X38            
6A6A: FF         RST     0X38            
6A6B: FF         RST     0X38            
6A6C: FF         RST     0X38            
6A6D: FF         RST     0X38            
6A6E: FF         RST     0X38            
6A6F: FF         RST     0X38            
6A70: FB         EI                      
6A71: F0 62      LD      A,($62)         
6A73: 20 FB      JR      NZ,$6A70        
6A75: F8 60      LDHL    SP,$60          
6A77: 20 FE      JR      NZ,$6A77        
6A79: F8 66      LDHL    SP,$66          
6A7B: 00         NOP                     
6A7C: 00         NOP                     
6A7D: 10 66      STOP    $66             
6A7F: 20 FF      JR      NZ,$6A80        
6A81: FF         RST     0X38            
6A82: FF         RST     0X38            
6A83: FF         RST     0X38            
6A84: F0 F1      LD      A,($F1)         
6A86: 17         RLA                     
6A87: 17         RLA                     
6A88: E6 FC      AND     $FC             
6A8A: 5F         LD      E,A             
6A8B: 17         RLA                     
6A8C: E6 F8      AND     $F8             
6A8E: 83         ADD     A,E             
6A8F: 5F         LD      E,A             
6A90: 50         LD      D,B             
6A91: 21 0C 6A   LD      HL,$6A0C        
6A94: 19         ADD     HL,DE           
6A95: 0E 03      LD      C,$03           
6A97: CD 26 3D   CALL    $3D26           
6A9A: 3E 03      LD      A,$03           
6A9C: CD D0 3D   CALL    $3DD0           
6A9F: C9         RET                     
6AA0: EC                              
6AA1: 00         NOP                     
6AA2: 70         LD      (HL),B          
6AA3: 00         NOP                     
6AA4: EC                              
6AA5: 08 70 20   LD      ($2070),SP      
6AA8: F4                              
6AA9: 00         NOP                     
6AAA: 7C         LD      A,H             
6AAB: 00         NOP                     
6AAC: F4                              
6AAD: 08 7C 20   LD      ($207C),SP      
6AB0: 08 00 7C   LD      ($7C00),SP      
6AB3: 40         LD      B,B             
6AB4: 08 08 7C   LD      ($7C08),SP      
6AB7: 60         LD      H,B             
6AB8: 14         INC     D               
6AB9: 00         NOP                     
6ABA: 70         LD      (HL),B          
6ABB: 40         LD      B,B             
6ABC: 14         INC     D               
6ABD: 08 70 60   LD      ($6070),SP      
6AC0: 00         NOP                     
6AC1: 00         NOP                     
6AC2: 7E         LD      A,(HL)          
6AC3: 40         LD      B,B             
6AC4: 00         NOP                     
6AC5: 08 7E 20   LD      ($207E),SP      
6AC8: F3         DI                      
6AC9: 0D         DEC     C               
6ACA: 78         LD      A,B             
6ACB: 20 F3      JR      NZ,$6AC0        
6ACD: 15         DEC     D               
6ACE: 76         HALT                    
6ACF: 20 0D      JR      NZ,$6ADE        
6AD1: F3         DI                      
6AD2: 76         HALT                    
6AD3: 40         LD      B,B             
6AD4: 0D         DEC     C               
6AD5: FB         EI                      
6AD6: 78         LD      A,B             
6AD7: 40         LD      B,B             
6AD8: FF         RST     0X38            
6AD9: FF         RST     0X38            
6ADA: FF         RST     0X38            
6ADB: FF         RST     0X38            
6ADC: FF         RST     0X38            
6ADD: FF         RST     0X38            
6ADE: FF         RST     0X38            
6ADF: FF         RST     0X38            
6AE0: 00         NOP                     
6AE1: EC                              
6AE2: 72         LD      (HL),D          
6AE3: 00         NOP                     
6AE4: 00         NOP                     
6AE5: F4                              
6AE6: 74         LD      (HL),H          
6AE7: 00         NOP                     
6AE8: 00         NOP                     
6AE9: FC                              
6AEA: 7A         LD      A,D             
6AEB: 00         NOP                     
6AEC: 00         NOP                     
6AED: 0C         INC     C               
6AEE: 7A         LD      A,D             
6AEF: 00         NOP                     
6AF0: 00         NOP                     
6AF1: 14         INC     D               
6AF2: 74         LD      (HL),H          
6AF3: 20 00      JR      NZ,$6AF5        
6AF5: 1C         INC     E               
6AF6: 72         LD      (HL),D          
6AF7: 20 00      JR      NZ,$6AF9        
6AF9: 00         NOP                     
6AFA: FF         RST     0X38            
6AFB: FF         RST     0X38            
6AFC: 00         NOP                     
6AFD: 00         NOP                     
6AFE: FF         RST     0X38            
6AFF: FF         RST     0X38            
6B00: 00         NOP                     
6B01: 00         NOP                     
6B02: 7E         LD      A,(HL)          
6B03: 00         NOP                     
6B04: 00         NOP                     
6B05: 08 7E 60   LD      ($607E),SP      
6B08: F3         DI                      
6B09: F3         DI                      
6B0A: 76         HALT                    
6B0B: 00         NOP                     
6B0C: F3         DI                      
6B0D: FB         EI                      
6B0E: 78         LD      A,B             
6B0F: 00         NOP                     
6B10: 0D         DEC     C               
6B11: 0D         DEC     C               
6B12: 78         LD      A,B             
6B13: 60         LD      H,B             
6B14: 0D         DEC     C               
6B15: 15         DEC     D               
6B16: 76         HALT                    
6B17: 60         LD      H,B             
6B18: FF         RST     0X38            
6B19: FF         RST     0X38            
6B1A: FF         RST     0X38            
6B1B: FF         RST     0X38            
6B1C: FF         RST     0X38            
6B1D: FF         RST     0X38            
6B1E: FF         RST     0X38            
6B1F: FF         RST     0X38            
6B20: F1         POP     AF              
6B21: 0F         RRCA                    
6B22: 78         LD      A,B             
6B23: 20 F1      JR      NZ,$6B16        
6B25: 17         RLA                     
6B26: 76         HALT                    
6B27: 20 0D      JR      NZ,$6B36        
6B29: F3         DI                      
6B2A: 76         HALT                    
6B2B: 40         LD      B,B             
6B2C: 0D         DEC     C               
6B2D: FB         EI                      
6B2E: 78         LD      A,B             
6B2F: 40         LD      B,B             
6B30: 00         NOP                     
6B31: 00         NOP                     
6B32: FF         RST     0X38            
6B33: FF         RST     0X38            
6B34: 00         NOP                     
6B35: 08 FF FF   LD      ($FFFF),SP      
6B38: FF         RST     0X38            
6B39: FF         RST     0X38            
6B3A: FF         RST     0X38            
6B3B: FF         RST     0X38            
6B3C: FF         RST     0X38            
6B3D: FF         RST     0X38            
6B3E: FF         RST     0X38            
6B3F: FF         RST     0X38            
6B40: F1         POP     AF              
6B41: F1         POP     AF              
6B42: 76         HALT                    
6B43: 00         NOP                     
6B44: F1         POP     AF              
6B45: F9         LD      SP,HL           
6B46: 78         LD      A,B             
6B47: 00         NOP                     
6B48: 0D         DEC     C               
6B49: 0D         DEC     C               
6B4A: 78         LD      A,B             
6B4B: 60         LD      H,B             
6B4C: 0D         DEC     C               
6B4D: 15         DEC     D               
6B4E: 76         HALT                    
6B4F: 60         LD      H,B             
6B50: 00         NOP                     
6B51: 00         NOP                     
6B52: FF         RST     0X38            
6B53: FF         RST     0X38            
6B54: 00         NOP                     
6B55: 08 FF FF   LD      ($FFFF),SP      
6B58: FF         RST     0X38            
6B59: FF         RST     0X38            
6B5A: FF         RST     0X38            
6B5B: FF         RST     0X38            
6B5C: FF         RST     0X38            
6B5D: FF         RST     0X38            
6B5E: FF         RST     0X38            
6B5F: FF         RST     0X38            
6B60: F8 08      LDHL    SP,$08          
6B62: 78         LD      A,B             
6B63: 20 F8      JR      NZ,$6B5D        
6B65: 10 76      STOP    $76             
6B67: 20 08      JR      NZ,$6B71        
6B69: F8 76      LDHL    SP,$76          
6B6B: 40         LD      B,B             
6B6C: 08 00 78   LD      ($7800),SP      
6B6F: 40         LD      B,B             
6B70: 00         NOP                     
6B71: 00         NOP                     
6B72: FF         RST     0X38            
6B73: 40         LD      B,B             
6B74: 00         NOP                     
6B75: 08 FF 20   LD      ($20FF),SP      
6B78: FF         RST     0X38            
6B79: FF         RST     0X38            
6B7A: FF         RST     0X38            
6B7B: FF         RST     0X38            
6B7C: FF         RST     0X38            
6B7D: FF         RST     0X38            
6B7E: FF         RST     0X38            
6B7F: FF         RST     0X38            
6B80: FC                              
6B81: 04         INC     B               
6B82: 78         LD      A,B             
6B83: 20 FC      JR      NZ,$6B81        
6B85: 0C         INC     C               
6B86: 76         HALT                    
6B87: 20 04      JR      NZ,$6B8D        
6B89: FC                              
6B8A: 76         HALT                    
6B8B: 40         LD      B,B             
6B8C: 04         INC     B               
6B8D: 04         INC     B               
6B8E: 78         LD      A,B             
6B8F: 40         LD      B,B             
6B90: 00         NOP                     
6B91: 00         NOP                     
6B92: FF         RST     0X38            
6B93: 40         LD      B,B             
6B94: 00         NOP                     
6B95: 08 FF 20   LD      ($20FF),SP      
6B98: FF         RST     0X38            
6B99: FF         RST     0X38            
6B9A: FF         RST     0X38            
6B9B: FF         RST     0X38            
6B9C: FF         RST     0X38            
6B9D: FF         RST     0X38            
6B9E: FF         RST     0X38            
6B9F: FF         RST     0X38            
6BA0: F8 F8      LDHL    SP,$F8          
6BA2: 76         HALT                    
6BA3: 00         NOP                     
6BA4: F8 00      LDHL    SP,$00          
6BA6: 78         LD      A,B             
6BA7: 00         NOP                     
6BA8: 08 08 78   LD      ($7808),SP      
6BAB: 60         LD      H,B             
6BAC: 08 10 76   LD      ($7610),SP      
6BAF: 60         LD      H,B             
6BB0: 00         NOP                     
6BB1: 00         NOP                     
6BB2: FF         RST     0X38            
6BB3: 00         NOP                     
6BB4: 00         NOP                     
6BB5: 08 FF 60   LD      ($60FF),SP      
6BB8: FF         RST     0X38            
6BB9: FF         RST     0X38            
6BBA: FF         RST     0X38            
6BBB: FF         RST     0X38            
6BBC: FF         RST     0X38            
6BBD: FF         RST     0X38            
6BBE: FF         RST     0X38            
6BBF: FF         RST     0X38            
6BC0: FC                              
6BC1: FC                              
6BC2: 76         HALT                    
6BC3: 00         NOP                     
6BC4: FC                              
6BC5: 04         INC     B               
6BC6: 78         LD      A,B             
6BC7: 00         NOP                     
6BC8: 04         INC     B               
6BC9: 04         INC     B               
6BCA: 78         LD      A,B             
6BCB: 60         LD      H,B             
6BCC: 04         INC     B               
6BCD: 0C         INC     C               
6BCE: 76         HALT                    
6BCF: 60         LD      H,B             
6BD0: 00         NOP                     
6BD1: 00         NOP                     
6BD2: FF         RST     0X38            
6BD3: 00         NOP                     
6BD4: 00         NOP                     
6BD5: 08 FF 60   LD      ($60FF),SP      
6BD8: FF         RST     0X38            
6BD9: FF         RST     0X38            
6BDA: FF         RST     0X38            
6BDB: FF         RST     0X38            
6BDC: FF         RST     0X38            
6BDD: FF         RST     0X38            
6BDE: FF         RST     0X38            
6BDF: FF         RST     0X38            
6BE0: 00         NOP                     
6BE1: F8 72      LDHL    SP,$72          
6BE3: 00         NOP                     
6BE4: 00         NOP                     
6BE5: 00         NOP                     
6BE6: 74         LD      (HL),H          
6BE7: 00         NOP                     
6BE8: 00         NOP                     
6BE9: 08 74 20   LD      ($2074),SP      
6BEC: 00         NOP                     
6BED: 10 72      STOP    $72             
6BEF: 20 00      JR      NZ,$6BF1        
6BF1: 08 FF FF   LD      ($FFFF),SP      
6BF4: 00         NOP                     
6BF5: 10 FF      STOP    $FF             
6BF7: FF         RST     0X38            
6BF8: 00         NOP                     
6BF9: 00         NOP                     
6BFA: FF         RST     0X38            
6BFB: FF         RST     0X38            
6BFC: 00         NOP                     
6BFD: 00         NOP                     
6BFE: FF         RST     0X38            
6BFF: FF         RST     0X38            
6C00: 00         NOP                     
6C01: FB         EI                      
6C02: 72         LD      (HL),D          
6C03: 00         NOP                     
6C04: 00         NOP                     
6C05: 03         INC     BC              
6C06: 74         LD      (HL),H          
6C07: 00         NOP                     
6C08: 00         NOP                     
6C09: 05         DEC     B               
6C0A: 74         LD      (HL),H          
6C0B: 20 00      JR      NZ,$6C0D        
6C0D: 0D         DEC     C               
6C0E: 72         LD      (HL),D          
6C0F: 20 00      JR      NZ,$6C11        
6C11: FC                              
6C12: FF         RST     0X38            
6C13: FF         RST     0X38            
6C14: 00         NOP                     
6C15: 0C         INC     C               
6C16: FF         RST     0X38            
6C17: FF         RST     0X38            
6C18: 00         NOP                     
6C19: 00         NOP                     
6C1A: FF         RST     0X38            
6C1B: FF         RST     0X38            
6C1C: 00         NOP                     
6C1D: 00         NOP                     
6C1E: FF         RST     0X38            
6C1F: FF         RST     0X38            
6C20: 08 06 06   LD      ($0606),SP      
6C23: 06 04      LD      B,$04           
6C25: 04         INC     B               
6C26: 04         INC     B               
6C27: 04         INC     B               
6C28: 04         INC     B               
6C29: 04         INC     B               
6C2A: 04         INC     B               
6C2B: 04         INC     B               
6C2C: FA 24 D2   LD      A,($D224)       
6C2F: A7         AND     A               
6C30: C8         RET     Z               
6C31: FA 25 D2   LD      A,($D225)       
6C34: 21 EE FF   LD      HL,$FFEE        
6C37: 86         ADD     A,(HL)          
6C38: 77         LD      (HL),A          
6C39: FA 26 D2   LD      A,($D226)       
6C3C: 21 EC FF   LD      HL,$FFEC        
6C3F: 86         ADD     A,(HL)          
6C40: 77         LD      (HL),A          
6C41: FA 24 D2   LD      A,($D224)       
6C44: 3D         DEC     A               
6C45: 5F         LD      E,A             
6C46: 50         LD      D,B             
6C47: 21 20 6C   LD      HL,$6C20        
6C4A: 19         ADD     HL,DE           
6C4B: 4E         LD      C,(HL)          
6C4C: 50         LD      D,B             
6C4D: CB 23      SET     1,E             
6C4F: CB 12      SET     1,E             
6C51: CB 23      SET     1,E             
6C53: CB 12      SET     1,E             
6C55: CB 23      SET     1,E             
6C57: CB 12      SET     1,E             
6C59: CB 23      SET     1,E             
6C5B: CB 12      SET     1,E             
6C5D: CB 23      SET     1,E             
6C5F: CB 12      SET     1,E             
6C61: 7B         LD      A,E             
6C62: E6 E0      AND     $E0             
6C64: 5F         LD      E,A             
6C65: 21 A0 6A   LD      HL,$6AA0        
6C68: 19         ADD     HL,DE           
6C69: C5         PUSH    BC              
6C6A: CD 26 3D   CALL    $3D26           
6C6D: D1         POP     DE              
6C6E: 7B         LD      A,E             
6C6F: CD D0 3D   CALL    $3DD0           
6C72: CD BA 3D   CALL    $3DBA           
6C75: C9         RET                     
6C76: 03         INC     BC              
6C77: 02         LD      (BC),A          
6C78: 01 00 00   LD      BC,$0000        
6C7B: 01 02 03   LD      BC,$0302        
6C7E: FA 01 D2   LD      A,($D201)       
6C81: 5F         LD      E,A             
6C82: 50         LD      D,B             
6C83: 21 90 C2   LD      HL,$C290        
6C86: 19         ADD     HL,DE           
6C87: 7E         LD      A,(HL)          
6C88: FE 09      CP      $09             
6C8A: D2 35 7C   JP      NC,$7C35        
6C8D: 21 D0 C3   LD      HL,$C3D0        
6C90: 09         ADD     HL,BC           
6C91: 7E         LD      A,(HL)          
6C92: 1F         RRA                     
6C93: 1F         RRA                     
6C94: 1F         RRA                     
6C95: E6 03      AND     $03             
6C97: 5F         LD      E,A             
6C98: 50         LD      D,B             
6C99: 21 80 C3   LD      HL,$C380        
6C9C: 09         ADD     HL,BC           
6C9D: 7E         LD      A,(HL)          
6C9E: A7         AND     A               
6C9F: 21 76 6C   LD      HL,$6C76        
6CA2: 28 03      JR      Z,$6CA7         
6CA4: 21 7A 6C   LD      HL,$6C7A        
6CA7: 19         ADD     HL,DE           
6CA8: 7E         LD      A,(HL)          
6CA9: 3C         INC     A               
6CAA: EA 24 D2   LD      ($D224),A       
6CAD: AF         XOR     A               
6CAE: EA 25 D2   LD      ($D225),A       
6CB1: EA 26 D2   LD      ($D226),A       
6CB4: CD 2C 6C   CALL    $6C2C           
6CB7: AF         XOR     A               
6CB8: EA 24 D2   LD      ($D224),A       
6CBB: CD 20 7B   CALL    $7B20           
6CBE: F0 E7      LD      A,($E7)         
6CC0: E6 0F      AND     $0F             
6CC2: 20 04      JR      NZ,$6CC8        
6CC4: 3E 3A      LD      A,$3A           
6CC6: E0 F4      LDFF00  ($F4),A         
6CC8: 21 D0 C3   LD      HL,$C3D0        
6CCB: 09         ADD     HL,BC           
6CCC: 34         INC     (HL)            
6CCD: CD 8C 7B   CALL    $7B8C           
6CD0: CD BF 3B   CALL    $3BBF           
6CD3: CD 91 08   CALL    $0891           
6CD6: 28 01      JR      Z,$6CD9         
6CD8: C9         RET                     
6CD9: F0 98      LD      A,($98)         
6CDB: F5         PUSH    AF              
6CDC: F0 99      LD      A,($99)         
6CDE: F5         PUSH    AF              
6CDF: FA 01 D2   LD      A,($D201)       
6CE2: 5F         LD      E,A             
6CE3: 50         LD      D,B             
6CE4: 21 00 C2   LD      HL,$C200        
6CE7: 19         ADD     HL,DE           
6CE8: 7E         LD      A,(HL)          
6CE9: E0 98      LDFF00  ($98),A         
6CEB: 21 10 C2   LD      HL,$C210        
6CEE: 19         ADD     HL,DE           
6CEF: 7E         LD      A,(HL)          
6CF0: D6 0C      SUB     $0C             
6CF2: E0 99      LDFF00  ($99),A         
6CF4: 3E 10      LD      A,$10           
6CF6: CD 30 3C   CALL    $3C30           
6CF9: 21 50 C2   LD      HL,$C250        
6CFC: 09         ADD     HL,BC           
6CFD: F0 D7      LD      A,($D7)         
6CFF: 96         SUB     (HL)            
6D00: E6 80      AND     $80             
6D02: 20 02      JR      NZ,$6D06        
6D04: 34         INC     (HL)            
6D05: 34         INC     (HL)            
6D06: 35         DEC     (HL)            
6D07: 21 40 C2   LD      HL,$C240        
6D0A: 09         ADD     HL,BC           
6D0B: F0 D8      LD      A,($D8)         
6D0D: 96         SUB     (HL)            
6D0E: E6 80      AND     $80             
6D10: 20 02      JR      NZ,$6D14        
6D12: 34         INC     (HL)            
6D13: 34         INC     (HL)            
6D14: 35         DEC     (HL)            
6D15: 21 99 FF   LD      HL,$FF99        
6D18: F0 EC      LD      A,($EC)         
6D1A: 96         SUB     (HL)            
6D1B: C6 03      ADD     $03             
6D1D: FE 06      CP      $06             
6D1F: 30 25      JR      NC,$6D46        
6D21: 21 98 FF   LD      HL,$FF98        
6D24: F0 EE      LD      A,($EE)         
6D26: 96         SUB     (HL)            
6D27: C6 03      ADD     $03             
6D29: FE 06      CP      $06             
6D2B: 30 19      JR      NC,$6D46        
6D2D: FA 01 D2   LD      A,($D201)       
6D30: 5F         LD      E,A             
6D31: 50         LD      D,B             
6D32: 21 90 C2   LD      HL,$C290        
6D35: 19         ADD     HL,DE           
6D36: 7E         LD      A,(HL)          
6D37: FE 08      CP      $08             
6D39: 20 0B      JR      NZ,$6D46        
6D3B: 36 03      LD      (HL),$03        
6D3D: 21 E0 C2   LD      HL,$C2E0        
6D40: 19         ADD     HL,DE           
6D41: 36 4C      LD      (HL),$4C        
6D43: CD 35 7C   CALL    $7C35           
6D46: F1         POP     AF              
6D47: E0 99      LDFF00  ($99),A         
6D49: F1         POP     AF              
6D4A: E0 98      LDFF00  ($98),A         
6D4C: C9         RET                     
6D4D: 4A         LD      C,D             
6D4E: 00         NOP                     
6D4F: 4A         LD      C,D             
6D50: 20 4C      JR      NZ,$6D9E        
6D52: 00         NOP                     
6D53: 4C         LD      C,H             
6D54: 20 4E      JR      NZ,$6DA4        
6D56: 00         NOP                     
6D57: 4E         LD      C,(HL)          
6D58: 20 00      JR      NZ,$6D5A        
6D5A: 00         NOP                     
6D5B: 01 01 11   LD      BC,$1101        
6D5E: 4D         LD      C,L             
6D5F: 6D         LD      L,L             
6D60: CD 3B 3C   CALL    $3C3B           
6D63: CD 20 7B   CALL    $7B20           
6D66: CD 91 08   CALL    $0891           
6D69: CA 35 7C   JP      Z,$7C35         
6D6C: 1F         RRA                     
6D6D: 1F         RRA                     
6D6E: 1F         RRA                     
6D6F: E6 03      AND     $03             
6D71: 5F         LD      E,A             
6D72: 50         LD      D,B             
6D73: 21 59 6D   LD      HL,$6D59        
6D76: 19         ADD     HL,DE           
6D77: 7E         LD      A,(HL)          
6D78: CD 87 3B   CALL    $3B87           
6D7B: C9         RET                     
6D7C: 1E 00      LD      E,$00           
6D7E: 1E 60      LD      E,$60           
6D80: 34         INC     (HL)            
6D81: 00         NOP                     
6D82: 34         INC     (HL)            
6D83: 20 54      JR      NZ,$6DD9        
6D85: 00         NOP                     
6D86: 54         LD      D,H             
6D87: 20 56      JR      NZ,$6DDF        
6D89: 00         NOP                     
6D8A: 56         LD      D,(HL)          
6D8B: 20 F0      JR      NZ,$6D7D        
6D8D: E7         RST     0X20            
6D8E: 17         RLA                     
6D8F: 17         RLA                     
6D90: E6 10      AND     $10             
6D92: E0 ED      LDFF00  ($ED),A         
6D94: 11 7C 6D   LD      DE,$6D7C        
6D97: CD 3B 3C   CALL    $3C3B           
6D9A: CD 20 7B   CALL    $7B20           
6D9D: F0 F0      LD      A,($F0)         
6D9F: C7         RST     0X00            
6DA0: A4         AND     H               
6DA1: 6D         LD      L,L             
6DA2: BB         CP      E               
6DA3: 6D         LD      L,L             
6DA4: CD 91 08   CALL    $0891           
6DA7: 20 05      JR      NZ,$6DAE        
6DA9: 36 20      LD      (HL),$20        
6DAB: C3 8D 3B   JP      $3B8D           
6DAE: 1E 00      LD      E,$00           
6DB0: FE 18      CP      $18             
6DB2: 30 02      JR      NC,$6DB6        
6DB4: 1E 01      LD      E,$01           
6DB6: 7B         LD      A,E             
6DB7: CD 87 3B   CALL    $3B87           
6DBA: C9         RET                     
6DBB: F0 E7      LD      A,($E7)         
6DBD: 1F         RRA                     
6DBE: 1F         RRA                     
6DBF: 1F         RRA                     
6DC0: E6 01      AND     $01             
6DC2: C6 02      ADD     $02             
6DC4: CD 87 3B   CALL    $3B87           
6DC7: CD 91 08   CALL    $0891           
6DCA: FE 01      CP      $01             
6DCC: 20 09      JR      NZ,$6DD7        
6DCE: 3E 28      LD      A,$28           
6DD0: E0 F4      LDFF00  ($F4),A         
6DD2: 3E 30      LD      A,$30           
6DD4: CD 25 3C   CALL    $3C25           
6DD7: F0 E7      LD      A,($E7)         
6DD9: A9         XOR     C               
6DDA: 1F         RRA                     
6DDB: 30 06      JR      NC,$6DE3        
6DDD: CD 8C 7B   CALL    $7B8C           
6DE0: CD BF 3B   CALL    $3BBF           
6DE3: F0 EE      LD      A,($EE)         
6DE5: FE A8      CP      $A8             
6DE7: D2 35 7C   JP      NC,$7C35        
6DEA: F0 EC      LD      A,($EC)         
6DEC: FE 88      CP      $88             
6DEE: D2 35 7C   JP      NC,$7C35        
6DF1: C9         RET                     
6DF2: 01 02 03   LD      BC,$0302        
6DF5: 03         INC     BC              
6DF6: 03         INC     BC              
6DF7: 03         INC     BC              
6DF8: 02         LD      (BC),A          
6DF9: 01 20 23   LD      BC,$2320        
6DFC: 26 29      LD      H,$29           
6DFE: 2C         INC     L               
6DFF: 2F         CPL                     
6E00: 32         LD      (HLD),A         
6E01: 35         DEC     (HL)            
6E02: 38 38      JR      C,$6E3C         
6E04: 38 38      JR      C,$6E3E         
6E06: 38 38      JR      C,$6E40         
6E08: 38 38      JR      C,$6E42         
6E0A: 38 38      JR      C,$6E44         
6E0C: 38 38      JR      C,$6E46         
6E0E: 38 38      JR      C,$6E48         
6E10: 38 38      JR      C,$6E4A         
6E12: 20 23      JR      NZ,$6E37        
6E14: 26 29      LD      H,$29           
6E16: 2C         INC     L               
6E17: 2F         CPL                     
6E18: 32         LD      (HLD),A         
6E19: 34         INC     (HL)            
6E1A: 34         INC     (HL)            
6E1B: 34         INC     (HL)            
6E1C: 34         INC     (HL)            
6E1D: 34         INC     (HL)            
6E1E: 34         INC     (HL)            
6E1F: 34         INC     (HL)            
6E20: 34         INC     (HL)            
6E21: 34         INC     (HL)            
6E22: 34         INC     (HL)            
6E23: 34         INC     (HL)            
6E24: 34         INC     (HL)            
6E25: 34         INC     (HL)            
6E26: 34         INC     (HL)            
6E27: 34         INC     (HL)            
6E28: 34         INC     (HL)            
6E29: 34         INC     (HL)            
6E2A: 28 27      JR      Z,$6E53         
6E2C: 26 25      LD      H,$25           
6E2E: 24         INC     H               
6E2F: 23         INC     HL              
6E30: 22         LD      (HLI),A         
6E31: 21 20 1F   LD      HL,$1F20        
6E34: 1E 1D      LD      E,$1D           
6E36: 1C         INC     E               
6E37: 1B         DEC     DE              
6E38: 1A         LD      A,(DE)          
6E39: 19         ADD     HL,DE           
6E3A: 18 18      JR      $6E54           
6E3C: 18 18      JR      $6E56           
6E3E: 18 18      JR      $6E58           
6E40: 18 18      JR      $6E5A           
6E42: 03         INC     BC              
6E43: 02         LD      (BC),A          
6E44: 01 00 00   LD      BC,$0000        
6E47: 00         NOP                     
6E48: 00         NOP                     
6E49: 00         NOP                     
6E4A: 21 00 C3   LD      HL,$C300        
6E4D: 09         ADD     HL,BC           
6E4E: 7E         LD      A,(HL)          
6E4F: A7         AND     A               
6E50: 28 1C      JR      Z,$6E6E         
6E52: FE 10      CP      $10             
6E54: 20 06      JR      NZ,$6E5C        
6E56: 35         DEC     (HL)            
6E57: CD D8 52   CALL    $52D8           
6E5A: 3E 10      LD      A,$10           
6E5C: 1F         RRA                     
6E5D: 1F         RRA                     
6E5E: 1F         RRA                     
6E5F: E6 07      AND     $07             
6E61: 5F         LD      E,A             
6E62: 50         LD      D,B             
6E63: 21 42 6E   LD      HL,$6E42        
6E66: 19         ADD     HL,DE           
6E67: 7E         LD      A,(HL)          
6E68: E0 F1      LDFF00  ($F1),A         
6E6A: CD 28 57   CALL    $5728           
6E6D: C9         RET                     
6E6E: CD 70 70   CALL    $7070           
6E71: CD 20 7B   CALL    $7B20           
6E74: F0 F0      LD      A,($F0)         
6E76: C7         RST     0X00            
6E77: 7D         LD      A,L             
6E78: 6E         LD      L,(HL)          
6E79: B9         CP      C               
6E7A: 6F         LD      L,A             
6E7B: D6 6F      SUB     $6F             
6E7D: 21 60 C3   LD      HL,$C360        
6E80: 09         ADD     HL,BC           
6E81: 7E         LD      A,(HL)          
6E82: FE F0      CP      $F0             
6E84: 30 2D      JR      NC,$6EB3        
6E86: 3E 03      LD      A,$03           
6E88: EA A7 C5   LD      ($C5A7),A       
6E8B: 3E F6      LD      A,$F6           
6E8D: CD 97 21   CALL    $2197           
6E90: 3E 5E      LD      A,$5E           
6E92: EA 68 D3   LD      ($D368),A       
6E95: CD 91 08   CALL    $0891           
6E98: 36 80      LD      (HL),$80        
6E9A: 21 20 C4   LD      HL,$C420        
6E9D: 09         ADD     HL,BC           
6E9E: 36 80      LD      (HL),$80        
6EA0: 21 50 C3   LD      HL,$C350        
6EA3: 09         ADD     HL,BC           
6EA4: CB BE      SET     1,E             
6EA6: 21 40 C3   LD      HL,$C340        
6EA9: 09         ADD     HL,BC           
6EAA: CB F6      SET     1,E             
6EAC: CD D2 27   CALL    $27D2           
6EAF: CD 8D 3B   CALL    $3B8D           
6EB2: C9         RET                     
6EB3: F0 E7      LD      A,($E7)         
6EB5: E6 0F      AND     $0F             
6EB7: 20 14      JR      NZ,$6ECD        
6EB9: FA 23 D2   LD      A,($D223)       
6EBC: FE 04      CP      $04             
6EBE: 30 0D      JR      NC,$6ECD        
6EC0: 3C         INC     A               
6EC1: EA 23 D2   LD      ($D223),A       
6EC4: FE 01      CP      $01             
6EC6: 20 05      JR      NZ,$6ECD        
6EC8: 21 68 D3   LD      HL,$D368        
6ECB: 36 50      LD      (HL),$50        
6ECD: CD E2 08   CALL    $08E2           
6ED0: 21 60 C3   LD      HL,$C360        
6ED3: 09         ADD     HL,BC           
6ED4: 7E         LD      A,(HL)          
6ED5: 2F         CPL                     
6ED6: FE 17      CP      $17             
6ED8: 38 02      JR      C,$6EDC         
6EDA: 3E 17      LD      A,$17           
6EDC: 5F         LD      E,A             
6EDD: 50         LD      D,B             
6EDE: 21 FA 6D   LD      HL,$6DFA        
6EE1: 19         ADD     HL,DE           
6EE2: 7E         LD      A,(HL)          
6EE3: 21 B0 C2   LD      HL,$C2B0        
6EE6: 09         ADD     HL,BC           
6EE7: 77         LD      (HL),A          
6EE8: 21 12 6E   LD      HL,$6E12        
6EEB: 19         ADD     HL,DE           
6EEC: 7E         LD      A,(HL)          
6EED: 21 C0 C2   LD      HL,$C2C0        
6EF0: 09         ADD     HL,BC           
6EF1: 77         LD      (HL),A          
6EF2: 21 2A 6E   LD      HL,$6E2A        
6EF5: 19         ADD     HL,DE           
6EF6: FA 10 D2   LD      A,($D210)       
6EF9: 3C         INC     A               
6EFA: BE         CP      (HL)            
6EFB: 38 05      JR      C,$6F02         
6EFD: 3E 3D      LD      A,$3D           
6EFF: E0 F2      LDFF00  ($F2),A         
6F01: AF         XOR     A               
6F02: EA 10 D2   LD      ($D210),A       
6F05: 3E 00      LD      A,$00           
6F07: CD 87 3B   CALL    $3B87           
6F0A: CD 87 08   CALL    $0887           
6F0D: 20 14      JR      NZ,$6F23        
6F0F: CD ED 27   CALL    $27ED           
6F12: E6 0F      AND     $0F             
6F14: C6 20      ADD     $20             
6F16: 77         LD      (HL),A          
6F17: CD ED 27   CALL    $27ED           
6F1A: E6 01      AND     $01             
6F1C: 20 05      JR      NZ,$6F23        
6F1E: CD 8C 08   CALL    $088C           
6F21: 36 7F      LD      (HL),$7F        
6F23: 21 50 C3   LD      HL,$C350        
6F26: 09         ADD     HL,BC           
6F27: CB FE      SET     1,E             
6F29: CD 8C 08   CALL    $088C           
6F2C: 28 1A      JR      Z,$6F48         
6F2E: 1F         RRA                     
6F2F: 1F         RRA                     
6F30: 1F         RRA                     
6F31: 1F         RRA                     
6F32: E6 07      AND     $07             
6F34: 5F         LD      E,A             
6F35: 50         LD      D,B             
6F36: 21 F2 6D   LD      HL,$6DF2        
6F39: 19         ADD     HL,DE           
6F3A: 7E         LD      A,(HL)          
6F3B: CD 87 3B   CALL    $3B87           
6F3E: FE 03      CP      $03             
6F40: 20 06      JR      NZ,$6F48        
6F42: 21 50 C3   LD      HL,$C350        
6F45: 09         ADD     HL,BC           
6F46: CB BE      SET     1,E             
6F48: CD B4 3B   CALL    $3BB4           
6F4B: 1E 0F      LD      E,$0F           
6F4D: 21 60 C3   LD      HL,$C360        
6F50: 09         ADD     HL,BC           
6F51: 7E         LD      A,(HL)          
6F52: FE F8      CP      $F8             
6F54: 30 02      JR      NC,$6F58        
6F56: 1E 07      LD      E,$07           
6F58: F0 E7      LD      A,($E7)         
6F5A: A3         AND     E               
6F5B: 20 2B      JR      NZ,$6F88        
6F5D: F0 99      LD      A,($99)         
6F5F: F5         PUSH    AF              
6F60: D6 20      SUB     $20             
6F62: E0 99      LDFF00  ($99),A         
6F64: 3E 08      LD      A,$08           
6F66: CD 30 3C   CALL    $3C30           
6F69: F0 D7      LD      A,($D7)         
6F6B: 21 50 C2   LD      HL,$C250        
6F6E: 09         ADD     HL,BC           
6F6F: 96         SUB     (HL)            
6F70: E6 80      AND     $80             
6F72: 20 02      JR      NZ,$6F76        
6F74: 34         INC     (HL)            
6F75: 34         INC     (HL)            
6F76: 35         DEC     (HL)            
6F77: F0 D8      LD      A,($D8)         
6F79: 21 40 C2   LD      HL,$C240        
6F7C: 09         ADD     HL,BC           
6F7D: 96         SUB     (HL)            
6F7E: E6 80      AND     $80             
6F80: 20 02      JR      NZ,$6F84        
6F82: 34         INC     (HL)            
6F83: 34         INC     (HL)            
6F84: 35         DEC     (HL)            
6F85: F1         POP     AF              
6F86: E0 99      LDFF00  ($99),A         
6F88: CD 8C 7B   CALL    $7B8C           
6F8B: CD 9E 3B   CALL    $3B9E           
6F8E: 21 B0 C2   LD      HL,$C2B0        
6F91: 09         ADD     HL,BC           
6F92: 5E         LD      E,(HL)          
6F93: 21 D0 C3   LD      HL,$C3D0        
6F96: 09         ADD     HL,BC           
6F97: 7E         LD      A,(HL)          
6F98: 83         ADD     A,E             
6F99: 77         LD      (HL),A          
6F9A: 30 07      JR      NC,$6FA3        
6F9C: FA 21 D2   LD      A,($D221)       
6F9F: 3C         INC     A               
6FA0: EA 21 D2   LD      ($D221),A       
6FA3: 21 C0 C2   LD      HL,$C2C0        
6FA6: 09         ADD     HL,BC           
6FA7: 5E         LD      E,(HL)          
6FA8: 21 D0 C2   LD      HL,$C2D0        
6FAB: 09         ADD     HL,BC           
6FAC: 7E         LD      A,(HL)          
6FAD: 83         ADD     A,E             
6FAE: 77         LD      (HL),A          
6FAF: 30 07      JR      NC,$6FB8        
6FB1: FA 22 D2   LD      A,($D222)       
6FB4: 3D         DEC     A               
6FB5: EA 22 D2   LD      ($D222),A       
6FB8: C9         RET                     
6FB9: CD 91 08   CALL    $0891           
6FBC: FE 02      CP      $02             
6FBE: 20 05      JR      NZ,$6FC5        
6FC0: 21 68 D3   LD      HL,$D368        
6FC3: 36 5F      LD      (HL),$5F        
6FC5: A7         AND     A               
6FC6: 20 0D      JR      NZ,$6FD5        
6FC8: 36 80      LD      (HL),$80        
6FCA: 3E 3D      LD      A,$3D           
6FCC: E0 F4      LDFF00  ($F4),A         
6FCE: 3E 10      LD      A,$10           
6FD0: E0 F3      LDFF00  ($F3),A         
6FD2: CD 8D 3B   CALL    $3B8D           
6FD5: C9         RET                     
6FD6: CD 91 08   CALL    $0891           
6FD9: E6 0F      AND     $0F             
6FDB: 20 32      JR      NZ,$700F        
6FDD: FA 23 D2   LD      A,($D223)       
6FE0: FE 00      CP      $00             
6FE2: 20 27      JR      NZ,$700B        
6FE4: CD D7 08   CALL    $08D7           
6FE7: CD AD 53   CALL    $53AD           
6FEA: CD 35 7C   CALL    $7C35           
6FED: 3E E6      LD      A,$E6           
6FEF: CD 01 3C   CALL    $3C01           
6FF2: 21 90 C3   LD      HL,$C390        
6FF5: 19         ADD     HL,DE           
6FF6: 36 02      LD      (HL),$02        
6FF8: 21 10 C2   LD      HL,$C210        
6FFB: 19         ADD     HL,DE           
6FFC: 36 30      LD      (HL),$30        
6FFE: 21 00 C2   LD      HL,$C200        
7001: 19         ADD     HL,DE           
7002: 36 50      LD      (HL),$50        
7004: 21 B0 C3   LD      HL,$C3B0        
7007: 19         ADD     HL,DE           
7008: 36 FF      LD      (HL),$FF        
700A: C9         RET                     
700B: 3D         DEC     A               
700C: EA 23 D2   LD      ($D223),A       
700F: C9         RET                     
7010: F0 FC      LD      A,($FC)         
7012: 60         LD      H,B             
7013: 00         NOP                     
7014: F0 04      LD      A,($04)         
7016: 62         LD      H,D             
7017: 00         NOP                     
7018: F0 0C      LD      A,($0C)         
701A: 60         LD      H,B             
701B: 20 F0      JR      NZ,$700D        
701D: FC                              
701E: 64         LD      H,H             
701F: 00         NOP                     
7020: F0 04      LD      A,($04)         
7022: 66         LD      H,(HL)          
7023: 00         NOP                     
7024: F0 0C      LD      A,($0C)         
7026: 64         LD      H,H             
7027: 20 F0      JR      NZ,$7019        
7029: FC                              
702A: 68         LD      L,B             
702B: 00         NOP                     
702C: F0 04      LD      A,($04)         
702E: 6A         LD      L,D             
702F: 00         NOP                     
7030: F0 0C      LD      A,($0C)         
7032: 68         LD      L,B             
7033: 20 F0      JR      NZ,$7025        
7035: FC                              
7036: 64         LD      H,H             
7037: 00         NOP                     
7038: F0 04      LD      A,($04)         
703A: 66         LD      H,(HL)          
703B: 00         NOP                     
703C: F0 0C      LD      A,($0C)         
703E: 64         LD      H,H             
703F: 20 00      JR      NZ,$7041        
7041: FC                              
7042: 6C         LD      L,H             
7043: 00         NOP                     
7044: 00         NOP                     
7045: 04         INC     B               
7046: 6E         LD      L,(HL)          
7047: 00         NOP                     
7048: 00         NOP                     
7049: 0C         INC     C               
704A: 6C         LD      L,H             
704B: 20 00      JR      NZ,$704D        
704D: FC                              
704E: 70         LD      (HL),B          
704F: 00         NOP                     
7050: 00         NOP                     
7051: 04         INC     B               
7052: 72         LD      (HL),D          
7053: 00         NOP                     
7054: 00         NOP                     
7055: 0C         INC     C               
7056: 70         LD      (HL),B          
7057: 20 00      JR      NZ,$7059        
7059: FC                              
705A: 74         LD      (HL),H          
705B: 00         NOP                     
705C: 00         NOP                     
705D: 04         INC     B               
705E: 76         HALT                    
705F: 00         NOP                     
7060: 00         NOP                     
7061: 0C         INC     C               
7062: 74         LD      (HL),H          
7063: 20 00      JR      NZ,$7065        
7065: FC                              
7066: 78         LD      A,B             
7067: 00         NOP                     
7068: 00         NOP                     
7069: 04         INC     B               
706A: 7A         LD      A,D             
706B: 00         NOP                     
706C: 00         NOP                     
706D: 0C         INC     C               
706E: 78         LD      A,B             
706F: 20 F0      JR      NZ,$7061        
7071: E7         RST     0X20            
7072: 1F         RRA                     
7073: 1F         RRA                     
7074: 1F         RRA                     
7075: E6 03      AND     $03             
7077: 17         RLA                     
7078: 17         RLA                     
7079: E6 FC      AND     $FC             
707B: 5F         LD      E,A             
707C: 17         RLA                     
707D: E6 F8      AND     $F8             
707F: 83         ADD     A,E             
7080: 5F         LD      E,A             
7081: 50         LD      D,B             
7082: 21 10 70   LD      HL,$7010        
7085: 19         ADD     HL,DE           
7086: 0E 03      LD      C,$03           
7088: CD 26 3D   CALL    $3D26           
708B: 3E 03      LD      A,$03           
708D: CD D0 3D   CALL    $3DD0           
7090: F0 F1      LD      A,($F1)         
7092: 17         RLA                     
7093: 17         RLA                     
7094: E6 FC      AND     $FC             
7096: 5F         LD      E,A             
7097: 17         RLA                     
7098: E6 F8      AND     $F8             
709A: 83         ADD     A,E             
709B: 5F         LD      E,A             
709C: 50         LD      D,B             
709D: 21 40 70   LD      HL,$7040        
70A0: 19         ADD     HL,DE           
70A1: 0E 03      LD      C,$03           
70A3: CD 26 3D   CALL    $3D26           
70A6: 3E 03      LD      A,$03           
70A8: CD D0 3D   CALL    $3DD0           
70AB: 21 10 C2   LD      HL,$C210        
70AE: 09         ADD     HL,BC           
70AF: 7E         LD      A,(HL)          
70B0: F5         PUSH    AF              
70B1: E5         PUSH    HL              
70B2: D6 08      SUB     $08             
70B4: 77         LD      (HL),A          
70B5: CD BA 3D   CALL    $3DBA           
70B8: CD 96 71   CALL    $7196           
70BB: E1         POP     HL              
70BC: F1         POP     AF              
70BD: 77         LD      (HL),A          
70BE: CD BA 3D   CALL    $3DBA           
70C1: C9         RET                     
70C2: D0         RET     NC              
70C3: D1         POP     DE              
70C4: D4 D9 DF   CALL    NC,$DFD9        
70C7: E6 EE      AND     $EE             
70C9: F7         RST     0X30            
70CA: 00         NOP                     
70CB: 09         ADD     HL,BC           
70CC: 12         LD      (DE),A          
70CD: 1A         LD      A,(DE)          
70CE: 21 27 2C   LD      HL,$2C27        
70D1: 2F         CPL                     
70D2: 30 2F      JR      NC,$7103        
70D4: 2C         INC     L               
70D5: 27         DAA                     
70D6: 21 1A 12   LD      HL,$121A        
70D9: 09         ADD     HL,BC           
70DA: 00         NOP                     
70DB: F7         RST     0X30            
70DC: EE E6      XOR     $E6             
70DE: DF         RST     0X18            
70DF: D9         RETI                    
70E0: D4 D1 D0   CALL    NC,$D0D1        
70E3: D1         POP     DE              
70E4: D4 D9 DF   CALL    NC,$DFD9        
70E7: E6 EE      AND     $EE             
70E9: F7         RST     0X30            
70EA: DA DB DD   JP      C,$DDDB         
70ED: E1         POP     HL              
70EE: E6 EB      AND     $EB             
70F0: F2                              
70F1: F9         LD      SP,HL           
70F2: 00         NOP                     
70F3: 07         RLCA                    
70F4: 0E 15      LD      C,$15           
70F6: 1A         LD      A,(DE)          
70F7: 1F         RRA                     
70F8: 23         INC     HL              
70F9: 25         DEC     H               
70FA: 26 25      LD      H,$25           
70FC: 23         INC     HL              
70FD: 1F         RRA                     
70FE: 1A         LD      A,(DE)          
70FF: 15         DEC     D               
7100: 0E 07      LD      C,$07           
7102: 00         NOP                     
7103: F9         LD      SP,HL           
7104: F2                              
7105: EB                              
7106: E6 E1      AND     $E1             
7108: DD                              
7109: DB                              
710A: DA DB DD   JP      C,$DDDB         
710D: E1         POP     HL              
710E: E6 EB      AND     $EB             
7110: F2                              
7111: F9         LD      SP,HL           
7112: E4                              
7113: E5         PUSH    HL              
7114: E7         RST     0X20            
7115: E9         JP      (HL)            
7116: ED                              
7117: F1         POP     AF              
7118: F6 FB      OR      $FB             
711A: 00         NOP                     
711B: 05         DEC     B               
711C: 0A         LD      A,(BC)          
711D: 0F         RRCA                    
711E: 13         INC     DE              
711F: 17         RLA                     
7120: 19         ADD     HL,DE           
7121: 1B         DEC     DE              
7122: 1C         INC     E               
7123: 1B         DEC     DE              
7124: 19         ADD     HL,DE           
7125: 17         RLA                     
7126: 13         INC     DE              
7127: 0F         RRCA                    
7128: 0A         LD      A,(BC)          
7129: 05         DEC     B               
712A: 00         NOP                     
712B: FB         EI                      
712C: F6 F1      OR      $F1             
712E: ED                              
712F: E9         JP      (HL)            
7130: E7         RST     0X20            
7131: E5         PUSH    HL              
7132: E4                              
7133: E5         PUSH    HL              
7134: E7         RST     0X20            
7135: E9         JP      (HL)            
7136: ED                              
7137: F1         POP     AF              
7138: F6 FB      OR      $FB             
713A: EE EF      XOR     $EF             
713C: F0 F2      LD      A,($F2)         
713E: F4                              
713F: F6 FA      OR      $FA             
7141: FD                              
7142: 00         NOP                     
7143: 03         INC     BC              
7144: 06 0A      LD      B,$0A           
7146: 0C         INC     C               
7147: 0E 10      LD      C,$10           
7149: 11 12 11   LD      DE,$1112        
714C: 10 0E      STOP    $0E             
714E: 0C         INC     C               
714F: 0A         LD      A,(BC)          
7150: 06 03      LD      B,$03           
7152: 00         NOP                     
7153: FD                              
7154: FA F6 F4   LD      A,($F4F6)       
7157: F2                              
7158: F0 EF      LD      A,($EF)         
715A: EE EF      XOR     $EF             
715C: F0 F2      LD      A,($F2)         
715E: F4                              
715F: F6 FA      OR      $FA             
7161: FD                              
7162: F8 F9      LDHL    SP,$F9          
7164: FA FB FB   LD      A,($FBFB)       
7167: FC                              
7168: FD                              
7169: FF         RST     0X38            
716A: 00         NOP                     
716B: 01 03 04   LD      BC,$0403        
716E: 05         DEC     B               
716F: 05         DEC     B               
7170: 06 07      LD      B,$07           
7172: 08 07 06   LD      ($0607),SP      
7175: 05         DEC     B               
7176: 05         DEC     B               
7177: 04         INC     B               
7178: 03         INC     BC              
7179: 01 00 FF   LD      BC,$FF00        
717C: FD                              
717D: FC                              
717E: FB         EI                      
717F: FB         EI                      
7180: FA F9 F8   LD      A,($F8F9)       
7183: F9         LD      SP,HL           
7184: FA FB FB   LD      A,($FBFB)       
7187: FC                              
7188: FD                              
7189: FF         RST     0X38            
718A: 4E         LD      C,(HL)          
718B: 00         NOP                     
718C: 4E         LD      C,(HL)          
718D: 20 4C      JR      NZ,$71DB        
718F: 00         NOP                     
7190: 4C         LD      C,H             
7191: 20 7C      JR      NZ,$720F        
7193: 00         NOP                     
7194: 7C         LD      A,H             
7195: 20 FA      JR      NZ,$7191        
7197: 23         INC     HL              
7198: D2 FE 04   JP      NC,$04FE        
719B: 38 1E      JR      C,$71BB         
719D: FA 21 D2   LD      A,($D221)       
71A0: E6 1F      AND     $1F             
71A2: 5F         LD      E,A             
71A3: 50         LD      D,B             
71A4: 21 CA 70   LD      HL,$70CA        
71A7: 19         ADD     HL,DE           
71A8: F0 EE      LD      A,($EE)         
71AA: 86         ADD     A,(HL)          
71AB: E0 EE      LDFF00  ($EE),A         
71AD: 21 C2 70   LD      HL,$70C2        
71B0: 19         ADD     HL,DE           
71B1: F0 EC      LD      A,($EC)         
71B3: 86         ADD     A,(HL)          
71B4: E0 EC      LDFF00  ($EC),A         
71B6: 3E 02      LD      A,$02           
71B8: CD ED 72   CALL    $72ED           
71BB: FA 23 D2   LD      A,($D223)       
71BE: FE 03      CP      $03             
71C0: 38 1E      JR      C,$71E0         
71C2: FA 21 D2   LD      A,($D221)       
71C5: E6 1F      AND     $1F             
71C7: 5F         LD      E,A             
71C8: 50         LD      D,B             
71C9: 21 F2 70   LD      HL,$70F2        
71CC: 19         ADD     HL,DE           
71CD: F0 EE      LD      A,($EE)         
71CF: 86         ADD     A,(HL)          
71D0: E0 EE      LDFF00  ($EE),A         
71D2: 21 EA 70   LD      HL,$70EA        
71D5: 19         ADD     HL,DE           
71D6: F0 EC      LD      A,($EC)         
71D8: 86         ADD     A,(HL)          
71D9: E0 EC      LDFF00  ($EC),A         
71DB: 3E 01      LD      A,$01           
71DD: CD ED 72   CALL    $72ED           
71E0: FA 23 D2   LD      A,($D223)       
71E3: FE 02      CP      $02             
71E5: 38 1E      JR      C,$7205         
71E7: FA 21 D2   LD      A,($D221)       
71EA: E6 1F      AND     $1F             
71EC: 5F         LD      E,A             
71ED: 50         LD      D,B             
71EE: 21 1A 71   LD      HL,$711A        
71F1: 19         ADD     HL,DE           
71F2: F0 EE      LD      A,($EE)         
71F4: 86         ADD     A,(HL)          
71F5: E0 EE      LDFF00  ($EE),A         
71F7: 21 12 71   LD      HL,$7112        
71FA: 19         ADD     HL,DE           
71FB: F0 EC      LD      A,($EC)         
71FD: 86         ADD     A,(HL)          
71FE: E0 EC      LDFF00  ($EC),A         
7200: 3E 01      LD      A,$01           
7202: CD ED 72   CALL    $72ED           
7205: FA 23 D2   LD      A,($D223)       
7208: FE 01      CP      $01             
720A: 38 35      JR      C,$7241         
720C: FA 21 D2   LD      A,($D221)       
720F: E6 0F      AND     $0F             
7211: FE 07      CP      $07             
7213: 28 08      JR      Z,$721D         
7215: FE 08      CP      $08             
7217: 28 04      JR      Z,$721D         
7219: FE 09      CP      $09             
721B: 20 06      JR      NZ,$7223        
721D: F0 E7      LD      A,($E7)         
721F: E6 01      AND     $01             
7221: 20 1E      JR      NZ,$7241        
7223: FA 21 D2   LD      A,($D221)       
7226: E6 1F      AND     $1F             
7228: 5F         LD      E,A             
7229: 50         LD      D,B             
722A: 21 42 71   LD      HL,$7142        
722D: 19         ADD     HL,DE           
722E: F0 EE      LD      A,($EE)         
7230: 86         ADD     A,(HL)          
7231: E0 EE      LDFF00  ($EE),A         
7233: 21 3A 71   LD      HL,$713A        
7236: 19         ADD     HL,DE           
7237: F0 EC      LD      A,($EC)         
7239: 86         ADD     A,(HL)          
723A: E0 EC      LDFF00  ($EC),A         
723C: 3E 00      LD      A,$00           
723E: CD ED 72   CALL    $72ED           
7241: FA 23 D2   LD      A,($D223)       
7244: FE 04      CP      $04             
7246: 38 1E      JR      C,$7266         
7248: FA 22 D2   LD      A,($D222)       
724B: E6 1F      AND     $1F             
724D: 5F         LD      E,A             
724E: 50         LD      D,B             
724F: 21 CA 70   LD      HL,$70CA        
7252: 19         ADD     HL,DE           
7253: F0 EE      LD      A,($EE)         
7255: 86         ADD     A,(HL)          
7256: E0 EE      LDFF00  ($EE),A         
7258: 21 C2 70   LD      HL,$70C2        
725B: 19         ADD     HL,DE           
725C: F0 EC      LD      A,($EC)         
725E: 86         ADD     A,(HL)          
725F: E0 EC      LDFF00  ($EC),A         
7261: 3E 02      LD      A,$02           
7263: CD ED 72   CALL    $72ED           
7266: FA 23 D2   LD      A,($D223)       
7269: FE 03      CP      $03             
726B: 38 1E      JR      C,$728B         
726D: FA 22 D2   LD      A,($D222)       
7270: E6 1F      AND     $1F             
7272: 5F         LD      E,A             
7273: 50         LD      D,B             
7274: 21 F2 70   LD      HL,$70F2        
7277: 19         ADD     HL,DE           
7278: F0 EE      LD      A,($EE)         
727A: 86         ADD     A,(HL)          
727B: E0 EE      LDFF00  ($EE),A         
727D: 21 EA 70   LD      HL,$70EA        
7280: 19         ADD     HL,DE           
7281: F0 EC      LD      A,($EC)         
7283: 86         ADD     A,(HL)          
7284: E0 EC      LDFF00  ($EC),A         
7286: 3E 01      LD      A,$01           
7288: CD ED 72   CALL    $72ED           
728B: FA 23 D2   LD      A,($D223)       
728E: FE 02      CP      $02             
7290: 38 1E      JR      C,$72B0         
7292: FA 22 D2   LD      A,($D222)       
7295: E6 1F      AND     $1F             
7297: 5F         LD      E,A             
7298: 50         LD      D,B             
7299: 21 1A 71   LD      HL,$711A        
729C: 19         ADD     HL,DE           
729D: F0 EE      LD      A,($EE)         
729F: 86         ADD     A,(HL)          
72A0: E0 EE      LDFF00  ($EE),A         
72A2: 21 12 71   LD      HL,$7112        
72A5: 19         ADD     HL,DE           
72A6: F0 EC      LD      A,($EC)         
72A8: 86         ADD     A,(HL)          
72A9: E0 EC      LDFF00  ($EC),A         
72AB: 3E 01      LD      A,$01           
72AD: CD ED 72   CALL    $72ED           
72B0: FA 23 D2   LD      A,($D223)       
72B3: FE 01      CP      $01             
72B5: 38 35      JR      C,$72EC         
72B7: FA 22 D2   LD      A,($D222)       
72BA: E6 0F      AND     $0F             
72BC: FE 07      CP      $07             
72BE: 28 08      JR      Z,$72C8         
72C0: FE 08      CP      $08             
72C2: 28 04      JR      Z,$72C8         
72C4: FE 09      CP      $09             
72C6: 20 06      JR      NZ,$72CE        
72C8: F0 E7      LD      A,($E7)         
72CA: E6 01      AND     $01             
72CC: 28 1E      JR      Z,$72EC         
72CE: FA 22 D2   LD      A,($D222)       
72D1: E6 1F      AND     $1F             
72D3: 5F         LD      E,A             
72D4: 50         LD      D,B             
72D5: 21 42 71   LD      HL,$7142        
72D8: 19         ADD     HL,DE           
72D9: F0 EE      LD      A,($EE)         
72DB: 86         ADD     A,(HL)          
72DC: E0 EE      LDFF00  ($EE),A         
72DE: 21 3A 71   LD      HL,$713A        
72E1: 19         ADD     HL,DE           
72E2: F0 EC      LD      A,($EC)         
72E4: 86         ADD     A,(HL)          
72E5: E0 EC      LDFF00  ($EC),A         
72E7: 3E 00      LD      A,$00           
72E9: CD ED 72   CALL    $72ED           
72EC: C9         RET                     
72ED: E0 F1      LDFF00  ($F1),A         
72EF: 11 8A 71   LD      DE,$718A        
72F2: CD 3B 3C   CALL    $3C3B           
72F5: 3E 02      LD      A,$02           
72F7: CD D0 3D   CALL    $3DD0           
72FA: 21 98 FF   LD      HL,$FF98        
72FD: F0 EE      LD      A,($EE)         
72FF: 96         SUB     (HL)            
7300: C6 08      ADD     $08             
7302: FE 10      CP      $10             
7304: 30 35      JR      NC,$733B        
7306: 21 99 FF   LD      HL,$FF99        
7309: F0 EC      LD      A,($EC)         
730B: 96         SUB     (HL)            
730C: C6 08      ADD     $08             
730E: FE 10      CP      $10             
7310: 30 29      JR      NC,$733B        
7312: 21 46 C1   LD      HL,$C146        
7315: FA C7 DB   LD      A,($DBC7)       
7318: B6         OR      (HL)            
7319: 20 20      JR      NZ,$733B        
731B: 3E 08      LD      A,$08           
731D: EA 94 DB   LD      ($DB94),A       
7320: 3E 20      LD      A,$20           
7322: CD 30 3C   CALL    $3C30           
7325: F0 D7      LD      A,($D7)         
7327: E0 9B      LDFF00  ($9B),A         
7329: F0 D8      LD      A,($D8)         
732B: E0 9A      LDFF00  ($9A),A         
732D: 3E 10      LD      A,$10           
732F: EA 3E C1   LD      ($C13E),A       
7332: 3E 30      LD      A,$30           
7334: EA C7 DB   LD      ($DBC7),A       
7337: 3E 03      LD      A,$03           
7339: E0 F3      LDFF00  ($F3),A         
733B: C3 BA 3D   JP      $3DBA           
733E: 58         LD      E,B             
733F: 00         NOP                     
7340: 58         LD      E,B             
7341: 20 5A      JR      NZ,$739D        
7343: 00         NOP                     
7344: 5A         LD      E,D             
7345: 20 10      JR      NZ,$7357        
7347: F0 00      LD      A,($00)         
7349: 00         NOP                     
734A: 00         NOP                     
734B: 00         NOP                     
734C: FB         EI                      
734D: 05         DEC     B               
734E: 11 3E 73   LD      DE,$733E        
7351: CD 3B 3C   CALL    $3C3B           
7354: CD 20 7B   CALL    $7B20           
7357: CD 42 7B   CALL    $7B42           
735A: CD 8C 7B   CALL    $7B8C           
735D: CD 9E 3B   CALL    $3B9E           
7360: CD B4 3B   CALL    $3BB4           
7363: F0 E7      LD      A,($E7)         
7365: 1F         RRA                     
7366: 1F         RRA                     
7367: 1F         RRA                     
7368: E6 01      AND     $01             
736A: CD 87 3B   CALL    $3B87           
736D: 21 A0 C2   LD      HL,$C2A0        
7370: 09         ADD     HL,BC           
7371: 7E         LD      A,(HL)          
7372: A7         AND     A               
7373: 20 05      JR      NZ,$737A        
7375: CD 91 08   CALL    $0891           
7378: 20 26      JR      NZ,$73A0        
737A: CD 91 08   CALL    $0891           
737D: CD ED 27   CALL    $27ED           
7380: E6 7F      AND     $7F             
7382: C6 30      ADD     $30             
7384: 77         LD      (HL),A          
7385: CD ED 27   CALL    $27ED           
7388: E6 03      AND     $03             
738A: 5F         LD      E,A             
738B: 50         LD      D,B             
738C: 21 46 73   LD      HL,$7346        
738F: 19         ADD     HL,DE           
7390: 7E         LD      A,(HL)          
7391: 21 40 C2   LD      HL,$C240        
7394: 09         ADD     HL,BC           
7395: 77         LD      (HL),A          
7396: 21 4A 73   LD      HL,$734A        
7399: 19         ADD     HL,DE           
739A: 7E         LD      A,(HL)          
739B: 21 50 C2   LD      HL,$C250        
739E: 09         ADD     HL,BC           
739F: 77         LD      (HL),A          
73A0: C9         RET                     
73A1: 5C         LD      E,H             
73A2: 00         NOP                     
73A3: 5E         LD      E,(HL)          
73A4: 00         NOP                     
73A5: 5E         LD      E,(HL)          
73A6: 20 5C      JR      NZ,$7404        
73A8: 20 5E      JR      NZ,$7408        
73AA: 60         LD      H,B             
73AB: 5C         LD      E,H             
73AC: 60         LD      H,B             
73AD: 5C         LD      E,H             
73AE: 40         LD      B,B             
73AF: 5E         LD      E,(HL)          
73B0: 40         LD      B,B             
73B1: 2C         INC     L               
73B2: 00         NOP                     
73B3: 2E 00      LD      L,$00           
73B5: 2E 20      LD      L,$20           
73B7: 2C         INC     L               
73B8: 20 2E      JR      NZ,$73E8        
73BA: 60         LD      H,B             
73BB: 2C         INC     L               
73BC: 60         LD      H,B             
73BD: 2C         INC     L               
73BE: 40         LD      B,B             
73BF: 2E 40      LD      L,$40           
73C1: FD                              
73C2: 03         INC     BC              
73C3: 00         NOP                     
73C4: 00         NOP                     
73C5: 00         NOP                     
73C6: 00         NOP                     
73C7: 03         INC     BC              
73C8: FD                              
73C9: 11 A1 73   LD      DE,$73A1        
73CC: FA 95 DB   LD      A,($DB95)       
73CF: FE 01      CP      $01             
73D1: 20 03      JR      NZ,$73D6        
73D3: 11 B1 73   LD      DE,$73B1        
73D6: CD 3B 3C   CALL    $3C3B           
73D9: CD 20 7B   CALL    $7B20           
73DC: CD 42 7B   CALL    $7B42           
73DF: F0 E7      LD      A,($E7)         
73E1: 1F         RRA                     
73E2: 1F         RRA                     
73E3: 1F         RRA                     
73E4: 1F         RRA                     
73E5: E6 03      AND     $03             
73E7: CD 87 3B   CALL    $3B87           
73EA: CD 0E 7C   CALL    $7C0E           
73ED: 21 80 C3   LD      HL,$C380        
73F0: 09         ADD     HL,BC           
73F1: 73         LD      (HL),E          
73F2: 21 40 C3   LD      HL,$C340        
73F5: 09         ADD     HL,BC           
73F6: CB BE      SET     1,E             
73F8: FA 5B C1   LD      A,($C15B)       
73FB: A7         AND     A               
73FC: 28 09      JR      Z,$7407         
73FE: F0 9E      LD      A,($9E)         
7400: EE 01      XOR     $01             
7402: BB         CP      E               
7403: 20 02      JR      NZ,$7407        
7405: CB FE      SET     1,E             
7407: CD D5 3B   CALL    $3BD5           
740A: 30 3A      JR      NC,$7446        
740C: CD 4A 09   CALL    $094A           
740F: 21 40 C3   LD      HL,$C340        
7412: 09         ADD     HL,BC           
7413: 7E         LD      A,(HL)          
7414: E6 80      AND     $80             
7416: C8         RET     Z               
7417: 21 80 C3   LD      HL,$C380        
741A: 09         ADD     HL,BC           
741B: 5E         LD      E,(HL)          
741C: 50         LD      D,B             
741D: 21 C1 73   LD      HL,$73C1        
7420: 19         ADD     HL,DE           
7421: 7E         LD      A,(HL)          
7422: 21 40 C2   LD      HL,$C240        
7425: 09         ADD     HL,BC           
7426: 77         LD      (HL),A          
7427: 21 C5 73   LD      HL,$73C5        
742A: 19         ADD     HL,DE           
742B: 7E         LD      A,(HL)          
742C: 21 50 C2   LD      HL,$C250        
742F: 09         ADD     HL,BC           
7430: 77         LD      (HL),A          
7431: 3E 3E      LD      A,$3E           
7433: E0 F2      LDFF00  ($F2),A         
7435: CD 8C 7B   CALL    $7B8C           
7438: 21 10 C4   LD      HL,$C410        
743B: 09         ADD     HL,BC           
743C: 36 03      LD      (HL),$03        
743E: CD 9E 3B   CALL    $3B9E           
7441: 21 10 C4   LD      HL,$C410        
7444: 09         ADD     HL,BC           
7445: 70         LD      (HL),B          
7446: FA 6A C1   LD      A,($C16A)       
7449: A7         AND     A               
744A: 20 06      JR      NZ,$7452        
744C: FA 5B C1   LD      A,($C15B)       
744F: A7         AND     A               
7450: 20 03      JR      NZ,$7455        
7452: CD EB 3B   CALL    $3BEB           
7455: C9         RET                     
7456: 30 D0      JR      NC,$7428        
7458: CD 20 7B   CALL    $7B20           
745B: 21 80 C3   LD      HL,$C380        
745E: 09         ADD     HL,BC           
745F: 5E         LD      E,(HL)          
7460: 50         LD      D,B             
7461: 21 56 74   LD      HL,$7456        
7464: 19         ADD     HL,DE           
7465: 7E         LD      A,(HL)          
7466: 21 50 C2   LD      HL,$C250        
7469: 09         ADD     HL,BC           
746A: 77         LD      (HL),A          
746B: CD 8F 7B   CALL    $7B8F           
746E: CD 9E 3B   CALL    $3B9E           
7471: F0 AF      LD      A,($AF)         
7473: FE 9D      CP      $9D             
7475: 28 13      JR      Z,$748A         
7477: 5F         LD      E,A             
7478: 16 01      LD      D,$01           
747A: CD DB 29   CALL    $29DB           
747D: A7         AND     A               
747E: 20 0A      JR      NZ,$748A        
7480: CD 35 7C   CALL    $7C35           
7483: 21 80 C2   LD      HL,$C280        
7486: 09         ADD     HL,BC           
7487: 7E         LD      A,(HL)          
7488: E0 EA      LDFF00  ($EA),A         
748A: F0 EE      LD      A,($EE)         
748C: D6 08      SUB     $08             
748E: E0 CE      LDFF00  ($CE),A         
7490: CB 37      SET     1,E             
7492: E6 0F      AND     $0F             
7494: 5F         LD      E,A             
7495: F0 EC      LD      A,($EC)         
7497: C6 04      ADD     $04             
7499: D6 10      SUB     $10             
749B: E0 CD      LDFF00  ($CD),A         
749D: E6 F0      AND     $F0             
749F: B3         OR      E               
74A0: 5F         LD      E,A             
74A1: 16 00      LD      D,$00           
74A3: 21 11 D7   LD      HL,$D711        
74A6: 19         ADD     HL,DE           
74A7: 36 9D      LD      (HL),$9D        
74A9: CD 39 28   CALL    $2839           
74AC: 21 01 D6   LD      HL,$D601        
74AF: FA 00 D6   LD      A,($D600)       
74B2: 5F         LD      E,A             
74B3: C6 0A      ADD     $0A             
74B5: EA 00 D6   LD      ($D600),A       
74B8: 16 00      LD      D,$00           
74BA: 19         ADD     HL,DE           
74BB: F0 CF      LD      A,($CF)         
74BD: 22         LD      (HLI),A         
74BE: F0 D0      LD      A,($D0)         
74C0: 22         LD      (HLI),A         
74C1: 3E 81      LD      A,$81           
74C3: 22         LD      (HLI),A         
74C4: E5         PUSH    HL              
74C5: 21 80 C3   LD      HL,$C380        
74C8: 09         ADD     HL,BC           
74C9: 7E         LD      A,(HL)          
74CA: E1         POP     HL              
74CB: A7         AND     A               
74CC: 20 27      JR      NZ,$74F5        
74CE: 3E 04      LD      A,$04           
74D0: 22         LD      (HLI),A         
74D1: F0 EA      LD      A,($EA)         
74D3: A7         AND     A               
74D4: 3E 08      LD      A,$08           
74D6: 20 02      JR      NZ,$74DA        
74D8: 3E 04      LD      A,$04           
74DA: 22         LD      (HLI),A         
74DB: F0 CF      LD      A,($CF)         
74DD: 22         LD      (HLI),A         
74DE: F0 D0      LD      A,($D0)         
74E0: 3C         INC     A               
74E1: 22         LD      (HLI),A         
74E2: 3E 81      LD      A,$81           
74E4: 22         LD      (HLI),A         
74E5: 3E 05      LD      A,$05           
74E7: 22         LD      (HLI),A         
74E8: F0 EA      LD      A,($EA)         
74EA: A7         AND     A               
74EB: 3E 09      LD      A,$09           
74ED: 20 02      JR      NZ,$74F1        
74EF: 3E 05      LD      A,$05           
74F1: 22         LD      (HLI),A         
74F2: 36 00      LD      (HL),$00        
74F4: C9         RET                     
74F5: F0 EA      LD      A,($EA)         
74F7: A7         AND     A               
74F8: 3E 0A      LD      A,$0A           
74FA: 20 02      JR      NZ,$74FE        
74FC: 3E 04      LD      A,$04           
74FE: 22         LD      (HLI),A         
74FF: 3E 04      LD      A,$04           
7501: 22         LD      (HLI),A         
7502: F0 CF      LD      A,($CF)         
7504: 22         LD      (HLI),A         
7505: F0 D0      LD      A,($D0)         
7507: 3C         INC     A               
7508: 22         LD      (HLI),A         
7509: 3E 81      LD      A,$81           
750B: 22         LD      (HLI),A         
750C: F0 EA      LD      A,($EA)         
750E: A7         AND     A               
750F: 3E 0B      LD      A,$0B           
7511: 20 02      JR      NZ,$7515        
7513: 3E 05      LD      A,$05           
7515: 22         LD      (HLI),A         
7516: 3E 05      LD      A,$05           
7518: 22         LD      (HLI),A         
7519: 36 00      LD      (HL),$00        
751B: C9         RET                     
751C: 21 D0 C2   LD      HL,$C2D0        
751F: 09         ADD     HL,BC           
7520: 7E         LD      A,(HL)          
7521: A7         AND     A               
7522: C2 8E 75   JP      NZ,$758E        
7525: CD 20 7B   CALL    $7B20           
7528: CD DF 7B   CALL    $7BDF           
752B: C6 20      ADD     $20             
752D: FE 40      CP      $40             
752F: 30 4C      JR      NC,$757D        
7531: CD EF 7B   CALL    $7BEF           
7534: C6 20      ADD     $20             
7536: FE 40      CP      $40             
7538: 30 43      JR      NC,$757D        
753A: 21 D0 C3   LD      HL,$C3D0        
753D: 09         ADD     HL,BC           
753E: 7E         LD      A,(HL)          
753F: 3C         INC     A               
7540: 77         LD      (HL),A          
7541: E6 3F      AND     $3F             
7543: 20 38      JR      NZ,$757D        
7545: 3E B2      LD      A,$B2           
7547: 1E 04      LD      E,$04           
7549: CD 13 3C   CALL    $3C13           
754C: 38 2F      JR      C,$757D         
754E: F0 D7      LD      A,($D7)         
7550: 21 00 C2   LD      HL,$C200        
7553: 19         ADD     HL,DE           
7554: 77         LD      (HL),A          
7555: F0 D8      LD      A,($D8)         
7557: 21 10 C2   LD      HL,$C210        
755A: 19         ADD     HL,DE           
755B: 77         LD      (HL),A          
755C: 21 40 C3   LD      HL,$C340        
755F: 19         ADD     HL,DE           
7560: 36 12      LD      (HL),$12        
7562: 21 D0 C2   LD      HL,$C2D0        
7565: 19         ADD     HL,DE           
7566: 36 01      LD      (HL),$01        
7568: 21 E0 C2   LD      HL,$C2E0        
756B: 19         ADD     HL,DE           
756C: 36 18      LD      (HL),$18        
756E: 21 F0 C2   LD      HL,$C2F0        
7571: 19         ADD     HL,DE           
7572: 36 20      LD      (HL),$20        
7574: C5         PUSH    BC              
7575: D5         PUSH    DE              
7576: C1         POP     BC              
7577: 3E 08      LD      A,$08           
7579: CD 25 3C   CALL    $3C25           
757C: C1         POP     BC              
757D: C9         RET                     
757E: 08 F8 00   LD      ($00F8),SP      
7581: 00         NOP                     
7582: 00         NOP                     
7583: 00         NOP                     
7584: F8 08      LDHL    SP,$08          
7586: 70         LD      (HL),B          
7587: 00         NOP                     
7588: 72         LD      (HL),D          
7589: 00         NOP                     
758A: 72         LD      (HL),D          
758B: 20 70      JR      NZ,$75FD        
758D: 20 11      JR      NZ,$75A0        
758F: 86         ADD     A,(HL)          
7590: 75         LD      (HL),L          
7591: CD 3B 3C   CALL    $3C3B           
7594: CD 20 7B   CALL    $7B20           
7597: CD 42 7B   CALL    $7B42           
759A: F0 E7      LD      A,($E7)         
759C: 1F         RRA                     
759D: 1F         RRA                     
759E: 1F         RRA                     
759F: E6 01      AND     $01             
75A1: CD 87 3B   CALL    $3B87           
75A4: CD 8C 7B   CALL    $7B8C           
75A7: CD 8C 08   CALL    $088C           
75AA: 20 03      JR      NZ,$75AF        
75AC: CD 9E 3B   CALL    $3B9E           
75AF: CD B4 3B   CALL    $3BB4           
75B2: CD 91 08   CALL    $0891           
75B5: 20 23      JR      NZ,$75DA        
75B7: CD ED 27   CALL    $27ED           
75BA: E6 1F      AND     $1F             
75BC: C6 20      ADD     $20             
75BE: 77         LD      (HL),A          
75BF: CD ED 27   CALL    $27ED           
75C2: E6 03      AND     $03             
75C4: 5F         LD      E,A             
75C5: 50         LD      D,B             
75C6: 21 7E 75   LD      HL,$757E        
75C9: 19         ADD     HL,DE           
75CA: 7E         LD      A,(HL)          
75CB: 21 40 C2   LD      HL,$C240        
75CE: 09         ADD     HL,BC           
75CF: 77         LD      (HL),A          
75D0: 21 82 75   LD      HL,$7582        
75D3: 19         ADD     HL,DE           
75D4: 7E         LD      A,(HL)          
75D5: 21 50 C2   LD      HL,$C250        
75D8: 09         ADD     HL,BC           
75D9: 77         LD      (HL),A          
75DA: C9         RET                     
75DB: 3E 00      LD      A,$00           
75DD: F8 08      LDHL    SP,$08          
75DF: 00         NOP                     
75E0: 00         NOP                     
75E1: 00         NOP                     
75E2: 00         NOP                     
75E3: 08 F8 CD   LD      ($CDF8),SP      
75E6: 20 7B      JR      NZ,$7663        
75E8: F0 F0      LD      A,($F0)         
75EA: A7         AND     A               
75EB: 20 03      JR      NZ,$75F0        
75ED: CD CA 3B   CALL    $3BCA           
75F0: CD 8C 7B   CALL    $7B8C           
75F3: CD A9 3B   CALL    $3BA9           
75F6: 21 A0 C2   LD      HL,$C2A0        
75F9: 09         ADD     HL,BC           
75FA: 7E         LD      A,(HL)          
75FB: A7         AND     A               
75FC: 28 4A      JR      Z,$7648         
75FE: E5         PUSH    HL              
75FF: F0 EE      LD      A,($EE)         
7601: E0 D7      LDFF00  ($D7),A         
7603: F0 EF      LD      A,($EF)         
7605: E0 D8      LDFF00  ($D8),A         
7607: 3E 05      LD      A,$05           
7609: CD 53 09   CALL    $0953           
760C: E1         POP     HL              
760D: 7E         LD      A,(HL)          
760E: FE 02      CP      $02             
7610: C2 35 7C   JP      NZ,$7C35        
7613: 36 00      LD      (HL),$00        
7615: 21 90 C2   LD      HL,$C290        
7618: 09         ADD     HL,BC           
7619: 77         LD      (HL),A          
761A: F0 9E      LD      A,($9E)         
761C: E6 02      AND     $02             
761E: 20 05      JR      NZ,$7625        
7620: 21 40 C2   LD      HL,$C240        
7623: 18 03      JR      $7628           
7625: 21 50 C2   LD      HL,$C250        
7628: 09         ADD     HL,BC           
7629: 7E         LD      A,(HL)          
762A: 2F         CPL                     
762B: 3C         INC     A               
762C: 77         LD      (HL),A          
762D: CD 3B 09   CALL    $093B           
7630: 3E 10      LD      A,$10           
7632: EA 3E C1   LD      ($C13E),A       
7635: F0 9E      LD      A,($9E)         
7637: 5F         LD      E,A             
7638: 50         LD      D,B             
7639: 21 DD 75   LD      HL,$75DD        
763C: 19         ADD     HL,DE           
763D: 7E         LD      A,(HL)          
763E: E0 9A      LDFF00  ($9A),A         
7640: 21 E1 75   LD      HL,$75E1        
7643: 19         ADD     HL,DE           
7644: 7E         LD      A,(HL)          
7645: E0 9B      LDFF00  ($9B),A         
7647: C9         RET                     
7648: F0 EE      LD      A,($EE)         
764A: C6 04      ADD     $04             
764C: E0 D7      LDFF00  ($D7),A         
764E: F0 EF      LD      A,($EF)         
7650: E0 D8      LDFF00  ($D8),A         
7652: 3E 06      LD      A,$06           
7654: CD 53 09   CALL    $0953           
7657: 36 10      LD      (HL),$10        
7659: C9         RET                     
765A: 00         NOP                     
765B: 00         NOP                     
765C: 74         LD      (HL),H          
765D: 00         NOP                     
765E: 00         NOP                     
765F: 08 74 20   LD      ($2074),SP      
7662: 00         NOP                     
7663: 00         NOP                     
7664: FF         RST     0X38            
7665: 00         NOP                     
7666: F0 08      LD      A,($08)         
7668: 7A         LD      A,D             
7669: 00         NOP                     
766A: 00         NOP                     
766B: 00         NOP                     
766C: 76         HALT                    
766D: 00         NOP                     
766E: 00         NOP                     
766F: 08 78 00   LD      ($0078),SP      
7672: F0 00      LD      A,($00)         
7674: 7A         LD      A,D             
7675: 20 00      JR      NZ,$7677        
7677: 00         NOP                     
7678: 78         LD      A,B             
7679: 20 00      JR      NZ,$767B        
767B: 08 76 20   LD      ($2076),SP      
767E: 00         NOP                     
767F: 00         NOP                     
7680: 74         LD      (HL),H          
7681: 40         LD      B,B             
7682: 00         NOP                     
7683: 08 74 60   LD      ($6074),SP      
7686: 00         NOP                     
7687: 00         NOP                     
7688: FF         RST     0X38            
7689: 00         NOP                     
768A: 21 B0 C2   LD      HL,$C2B0        
768D: 09         ADD     HL,BC           
768E: 7E         LD      A,(HL)          
768F: A7         AND     A               
7690: C2 34 78   JP      NZ,$7834        
7693: 21 5A 76   LD      HL,$765A        
7696: F0 F1      LD      A,($F1)         
7698: 17         RLA                     
7699: 17         RLA                     
769A: E6 FC      AND     $FC             
769C: 5F         LD      E,A             
769D: 17         RLA                     
769E: 83         ADD     A,E             
769F: 5F         LD      E,A             
76A0: 50         LD      D,B             
76A1: 19         ADD     HL,DE           
76A2: 0E 03      LD      C,$03           
76A4: CD 26 3D   CALL    $3D26           
76A7: CD 19 3D   CALL    $3D19           
76AA: F0 F0      LD      A,($F0)         
76AC: FE 02      CP      $02             
76AE: 30 4E      JR      NC,$76FE        
76B0: FA 57 C1   LD      A,($C157)       
76B3: A7         AND     A               
76B4: 28 48      JR      Z,$76FE         
76B6: FA 78 C1   LD      A,($C178)       
76B9: A7         AND     A               
76BA: 28 42      JR      Z,$76FE         
76BC: F0 EE      LD      A,($EE)         
76BE: C6 08      ADD     $08             
76C0: 21 79 C1   LD      HL,$C179        
76C3: 96         SUB     (HL)            
76C4: C6 10      ADD     $10             
76C6: FE 20      CP      $20             
76C8: 30 34      JR      NC,$76FE        
76CA: F0 EF      LD      A,($EF)         
76CC: C6 08      ADD     $08             
76CE: 21 7A C1   LD      HL,$C17A        
76D1: 96         SUB     (HL)            
76D2: C6 10      ADD     $10             
76D4: FE 20      CP      $20             
76D6: 30 26      JR      NC,$76FE        
76D8: 21 10 C2   LD      HL,$C210        
76DB: 09         ADD     HL,BC           
76DC: 7E         LD      A,(HL)          
76DD: C6 18      ADD     $18             
76DF: 77         LD      (HL),A          
76E0: 21 10 C3   LD      HL,$C310        
76E3: 09         ADD     HL,BC           
76E4: 36 18      LD      (HL),$18        
76E6: CD 8D 3B   CALL    $3B8D           
76E9: 36 02      LD      (HL),$02        
76EB: 21 20 C3   LD      HL,$C320        
76EE: 09         ADD     HL,BC           
76EF: 36 15      LD      (HL),$15        
76F1: 21 50 C2   LD      HL,$C250        
76F4: 09         ADD     HL,BC           
76F5: 36 0C      LD      (HL),$0C        
76F7: 21 40 C2   LD      HL,$C240        
76FA: 09         ADD     HL,BC           
76FB: 36 FA      LD      (HL),$FA        
76FD: C9         RET                     
76FE: F0 F0      LD      A,($F0)         
7700: C7         RST     0X00            
7701: 09         ADD     HL,BC           
7702: 77         LD      (HL),A          
7703: 19         ADD     HL,DE           
7704: 77         LD      (HL),A          
7705: A2         AND     D               
7706: 77         LD      (HL),A          
7707: CE 77      ADC     $77             
7709: 21 00 C2   LD      HL,$C200        
770C: 09         ADD     HL,BC           
770D: 7E         LD      A,(HL)          
770E: C6 08      ADD     $08             
7710: 77         LD      (HL),A          
7711: CD 91 08   CALL    $0891           
7714: 36 80      LD      (HL),$80        
7716: C3 8D 3B   JP      $3B8D           
7719: CD 20 7B   CALL    $7B20           
771C: CD 91 08   CALL    $0891           
771F: C0         RET     NZ              
7720: 36 50      LD      (HL),$50        
7722: 21 B0 C3   LD      HL,$C3B0        
7725: 09         ADD     HL,BC           
7726: 7E         LD      A,(HL)          
7727: 3C         INC     A               
7728: FE 03      CP      $03             
772A: 20 01      JR      NZ,$772D        
772C: AF         XOR     A               
772D: 77         LD      (HL),A          
772E: E0 F1      LDFF00  ($F1),A         
7730: FE 00      CP      $00             
7732: 28 6D      JR      Z,$77A1         
7734: CD 91 08   CALL    $0891           
7737: 36 28      LD      (HL),$28        
7739: 21 D0 C3   LD      HL,$C3D0        
773C: 09         ADD     HL,BC           
773D: 34         INC     (HL)            
773E: 7E         LD      A,(HL)          
773F: E6 0F      AND     $0F             
7741: 20 04      JR      NZ,$7747        
7743: 3E 02      LD      A,$02           
7745: 18 02      JR      $7749           
7747: 3E E0      LD      A,$E0           
7749: CD 01 3C   CALL    $3C01           
774C: D8         RET     C               
774D: F0 D7      LD      A,($D7)         
774F: 21 00 C2   LD      HL,$C200        
7752: 19         ADD     HL,DE           
7753: 77         LD      (HL),A          
7754: F0 D8      LD      A,($D8)         
7756: 21 10 C2   LD      HL,$C210        
7759: 19         ADD     HL,DE           
775A: D6 0C      SUB     $0C             
775C: C6 18      ADD     $18             
775E: 77         LD      (HL),A          
775F: 21 10 C3   LD      HL,$C310        
7762: 19         ADD     HL,DE           
7763: 36 18      LD      (HL),$18        
7765: 21 B0 C2   LD      HL,$C2B0        
7768: 19         ADD     HL,DE           
7769: 34         INC     (HL)            
776A: 21 20 C3   LD      HL,$C320        
776D: 19         ADD     HL,DE           
776E: 36 20      LD      (HL),$20        
7770: F0 F1      LD      A,($F1)         
7772: FE 01      CP      $01             
7774: 3E F8      LD      A,$F8           
7776: 28 02      JR      Z,$777A         
7778: 3E 08      LD      A,$08           
777A: 21 40 C2   LD      HL,$C240        
777D: 19         ADD     HL,DE           
777E: 77         LD      (HL),A          
777F: 21 50 C2   LD      HL,$C250        
7782: 19         ADD     HL,DE           
7783: 36 0C      LD      (HL),$0C        
7785: 21 40 C3   LD      HL,$C340        
7788: 19         ADD     HL,DE           
7789: 36 12      LD      (HL),$12        
778B: 21 30 C4   LD      HL,$C430        
778E: 19         ADD     HL,DE           
778F: CB C6      SET     1,E             
7791: 3E 08      LD      A,$08           
7793: E0 F2      LDFF00  ($F2),A         
7795: 21 E0 C2   LD      HL,$C2E0        
7798: 19         ADD     HL,DE           
7799: 36 60      LD      (HL),$60        
779B: 21 40 C4   LD      HL,$C440        
779E: 19         ADD     HL,DE           
779F: 36 01      LD      (HL),$01        
77A1: C9         RET                     
77A2: 3E 03      LD      A,$03           
77A4: CD 87 3B   CALL    $3B87           
77A7: CD 8C 7B   CALL    $7B8C           
77AA: CD C5 7B   CALL    $7BC5           
77AD: 21 20 C3   LD      HL,$C320        
77B0: 09         ADD     HL,BC           
77B1: 35         DEC     (HL)            
77B2: 35         DEC     (HL)            
77B3: 21 10 C3   LD      HL,$C310        
77B6: 09         ADD     HL,BC           
77B7: 7E         LD      A,(HL)          
77B8: E6 80      AND     $80             
77BA: 28 11      JR      Z,$77CD         
77BC: 70         LD      (HL),B          
77BD: 21 20 C3   LD      HL,$C320        
77C0: 09         ADD     HL,BC           
77C1: 36 20      LD      (HL),$20        
77C3: CD AF 3D   CALL    $3DAF           
77C6: CD 8D 3B   CALL    $3B8D           
77C9: 3E 14      LD      A,$14           
77CB: E0 F3      LDFF00  ($F3),A         
77CD: C9         RET                     
77CE: 3E 00      LD      A,$00           
77D0: CD 87 3B   CALL    $3B87           
77D3: CD 8C 7B   CALL    $7B8C           
77D6: CD C5 7B   CALL    $7BC5           
77D9: 21 20 C3   LD      HL,$C320        
77DC: 09         ADD     HL,BC           
77DD: 35         DEC     (HL)            
77DE: 35         DEC     (HL)            
77DF: 21 10 C3   LD      HL,$C310        
77E2: 09         ADD     HL,BC           
77E3: 7E         LD      A,(HL)          
77E4: E6 80      AND     $80             
77E6: 28 25      JR      Z,$780D         
77E8: 36 01      LD      (HL),$01        
77EA: CD ED 27   CALL    $27ED           
77ED: E6 0F      AND     $0F             
77EF: C6 08      ADD     $08             
77F1: 21 20 C3   LD      HL,$C320        
77F4: 09         ADD     HL,BC           
77F5: 77         LD      (HL),A          
77F6: 3E 10      LD      A,$10           
77F8: CD 30 3C   CALL    $3C30           
77FB: F0 D7      LD      A,($D7)         
77FD: 2F         CPL                     
77FE: 3C         INC     A               
77FF: 21 50 C2   LD      HL,$C250        
7802: 09         ADD     HL,BC           
7803: 77         LD      (HL),A          
7804: F0 D8      LD      A,($D8)         
7806: 2F         CPL                     
7807: 3C         INC     A               
7808: 21 40 C2   LD      HL,$C240        
780B: 09         ADD     HL,BC           
780C: 77         LD      (HL),A          
780D: F0 EE      LD      A,($EE)         
780F: FE A8      CP      $A8             
7811: D2 35 7C   JP      NC,$7C35        
7814: F0 EC      LD      A,($EC)         
7816: FE 80      CP      $80             
7818: D2 35 7C   JP      NC,$7C35        
781B: F0 E7      LD      A,($E7)         
781D: E6 0F      AND     $0F             
781F: 28 A8      JR      Z,$77C9         
7821: C9         RET                     
7822: 7C         LD      A,H             
7823: 00         NOP                     
7824: 7E         LD      A,(HL)          
7825: 00         NOP                     
7826: 7E         LD      A,(HL)          
7827: 20 7C      JR      NZ,$78A5        
7829: 20 00      JR      NZ,$782B        
782B: 0C         INC     C               
782C: 10 0C      STOP    $0C             
782E: 00         NOP                     
782F: F4                              
7830: F0 F4      LD      A,($F4)         
7832: 00         NOP                     
7833: 0C         INC     C               
7834: 11 22 78   LD      DE,$7822        
7837: CD 3B 3C   CALL    $3C3B           
783A: CD 20 7B   CALL    $7B20           
783D: CD 42 7B   CALL    $7B42           
7840: F0 E7      LD      A,($E7)         
7842: 1F         RRA                     
7843: 1F         RRA                     
7844: 1F         RRA                     
7845: 1F         RRA                     
7846: E6 01      AND     $01             
7848: CD 87 3B   CALL    $3B87           
784B: CD B4 3B   CALL    $3BB4           
784E: CD 8C 7B   CALL    $7B8C           
7851: CD C5 7B   CALL    $7BC5           
7854: 21 20 C3   LD      HL,$C320        
7857: 09         ADD     HL,BC           
7858: 35         DEC     (HL)            
7859: 35         DEC     (HL)            
785A: 21 10 C3   LD      HL,$C310        
785D: 09         ADD     HL,BC           
785E: 7E         LD      A,(HL)          
785F: E6 80      AND     $80             
7861: 28 38      JR      Z,$789B         
7863: 70         LD      (HL),B          
7864: CD ED 27   CALL    $27ED           
7867: E6 0F      AND     $0F             
7869: C6 10      ADD     $10             
786B: 21 20 C3   LD      HL,$C320        
786E: 09         ADD     HL,BC           
786F: 77         LD      (HL),A          
7870: CD ED 27   CALL    $27ED           
7873: E6 07      AND     $07             
7875: 5F         LD      E,A             
7876: 50         LD      D,B             
7877: 21 2C 78   LD      HL,$782C        
787A: 19         ADD     HL,DE           
787B: 7E         LD      A,(HL)          
787C: 21 40 C2   LD      HL,$C240        
787F: 09         ADD     HL,BC           
7880: 77         LD      (HL),A          
7881: 21 2A 78   LD      HL,$782A        
7884: 19         ADD     HL,DE           
7885: 7E         LD      A,(HL)          
7886: 21 50 C2   LD      HL,$C250        
7889: 09         ADD     HL,BC           
788A: 77         LD      (HL),A          
788B: 21 D0 C3   LD      HL,$C3D0        
788E: 09         ADD     HL,BC           
788F: 7E         LD      A,(HL)          
7890: 34         INC     (HL)            
7891: 7E         LD      A,(HL)          
7892: FE 04      CP      $04             
7894: CA 35 7C   JP      Z,$7C35         
7897: 3E 09      LD      A,$09           
7899: E0 F2      LDFF00  ($F2),A         
789B: C9         RET                     
789C: 50         LD      D,B             
789D: 00         NOP                     
789E: 52         LD      D,D             
789F: 00         NOP                     
78A0: 54         LD      D,H             
78A1: 00         NOP                     
78A2: 56         LD      D,(HL)          
78A3: 00         NOP                     
78A4: 52         LD      D,D             
78A5: 20 50      JR      NZ,$78F7        
78A7: 20 56      JR      NZ,$78FF        
78A9: 20 54      JR      NZ,$78FF        
78AB: 20 21      JR      NZ,$78CE        
78AD: 80         ADD     A,B             
78AE: C3 09 7E   JP      $7E09           
78B1: A7         AND     A               
78B2: 20 06      JR      NZ,$78BA        
78B4: F0 F1      LD      A,($F1)         
78B6: C6 02      ADD     $02             
78B8: E0 F1      LDFF00  ($F1),A         
78BA: 11 9C 78   LD      DE,$789C        
78BD: CD 3B 3C   CALL    $3C3B           
78C0: CD 20 7B   CALL    $7B20           
78C3: CD C5 7B   CALL    $7BC5           
78C6: 21 20 C3   LD      HL,$C320        
78C9: 09         ADD     HL,BC           
78CA: 35         DEC     (HL)            
78CB: 35         DEC     (HL)            
78CC: 21 10 C3   LD      HL,$C310        
78CF: 09         ADD     HL,BC           
78D0: 7E         LD      A,(HL)          
78D1: E6 80      AND     $80             
78D3: E0 E8      LDFF00  ($E8),A         
78D5: 28 07      JR      Z,$78DE         
78D7: AF         XOR     A               
78D8: 77         LD      (HL),A          
78D9: 21 20 C3   LD      HL,$C320        
78DC: 09         ADD     HL,BC           
78DD: 77         LD      (HL),A          
78DE: F0 F0      LD      A,($F0)         
78E0: C7         RST     0X00            
78E1: ED                              
78E2: 78         LD      A,B             
78E3: 3D         DEC     A               
78E4: 79         LD      A,C             
78E5: 02         LD      (BC),A          
78E6: 08 0C 08   LD      ($080C),SP      
78E9: FE F8      CP      $F8             
78EB: F4                              
78EC: F8 CD      LDHL    SP,$CD          
78EE: 91         SUB     C               
78EF: 08 20 37   LD      ($3720),SP      
78F2: CD ED 27   CALL    $27ED           
78F5: E6 07      AND     $07             
78F7: 5F         LD      E,A             
78F8: 50         LD      D,B             
78F9: 21 E5 78   LD      HL,$78E5        
78FC: 19         ADD     HL,DE           
78FD: 7E         LD      A,(HL)          
78FE: 21 40 C2   LD      HL,$C240        
7901: 09         ADD     HL,BC           
7902: 77         LD      (HL),A          
7903: 7B         LD      A,E             
7904: E6 04      AND     $04             
7906: 21 80 C3   LD      HL,$C380        
7909: 09         ADD     HL,BC           
790A: 77         LD      (HL),A          
790B: CD ED 27   CALL    $27ED           
790E: E6 07      AND     $07             
7910: 5F         LD      E,A             
7911: 21 E5 78   LD      HL,$78E5        
7914: 19         ADD     HL,DE           
7915: 7E         LD      A,(HL)          
7916: 21 50 C2   LD      HL,$C250        
7919: 09         ADD     HL,BC           
791A: 77         LD      (HL),A          
791B: CD 91 08   CALL    $0891           
791E: CD ED 27   CALL    $27ED           
7921: E6 1F      AND     $1F             
7923: C6 30      ADD     $30             
7925: 77         LD      (HL),A          
7926: C3 8D 3B   JP      $3B8D           
7929: 3E 01      LD      A,$01           
792B: CD 87 3B   CALL    $3B87           
792E: F0 E7      LD      A,($E7)         
7930: E6 1F      AND     $1F             
7932: 20 08      JR      NZ,$793C        
7934: 21 80 C3   LD      HL,$C380        
7937: 09         ADD     HL,BC           
7938: 7E         LD      A,(HL)          
7939: EE 04      XOR     $04             
793B: 77         LD      (HL),A          
793C: C9         RET                     
793D: CD 8C 7B   CALL    $7B8C           
7940: CD 9E 3B   CALL    $3B9E           
7943: F0 E8      LD      A,($E8)         
7945: A7         AND     A               
7946: 28 17      JR      Z,$795F         
7948: CD 91 08   CALL    $0891           
794B: 20 07      JR      NZ,$7954        
794D: 36 48      LD      (HL),$48        
794F: CD 8D 3B   CALL    $3B8D           
7952: 70         LD      (HL),B          
7953: C9         RET                     
7954: 21 20 C3   LD      HL,$C320        
7957: 09         ADD     HL,BC           
7958: 36 08      LD      (HL),$08        
795A: 21 10 C3   LD      HL,$C310        
795D: 09         ADD     HL,BC           
795E: 34         INC     (HL)            
795F: 3E 00      LD      A,$00           
7961: CD 87 3B   CALL    $3B87           
7964: C9         RET                     
7965: 00         NOP                     
7966: 08 10 18   LD      ($1810),SP      
7969: 20 28      JR      NZ,$7993        
796B: 30 38      JR      NC,$79A5        
796D: 21 40 C3   LD      HL,$C340        
7970: 09         ADD     HL,BC           
7971: 7E         LD      A,(HL)          
7972: E6 0F      AND     $0F             
7974: CB 27      SET     1,E             
7976: CB 27      SET     1,E             
7978: 5F         LD      E,A             
7979: FA C0 C3   LD      A,($C3C0)       
797C: 83         ADD     A,E             
797D: FE 60      CP      $60             
797F: 38 02      JR      C,$7983         
7981: D6 60      SUB     $60             
7983: EA C0 C3   LD      ($C3C0),A       
7986: FA C1 C3   LD      A,($C3C1)       
7989: 83         ADD     A,E             
798A: EA C1 C3   LD      ($C3C1),A       
798D: FE 60      CP      $60             
798F: 38 13      JR      C,$79A4         
7991: F0 E7      LD      A,($E7)         
7993: 21 23 C1   LD      HL,$C123        
7996: 86         ADD     A,(HL)          
7997: E6 07      AND     $07             
7999: 5F         LD      E,A             
799A: 16 00      LD      D,$00           
799C: 21 65 79   LD      HL,$7965        
799F: 19         ADD     HL,DE           
79A0: 7E         LD      A,(HL)          
79A1: EA C0 C3   LD      ($C3C0),A       
79A4: C9         RET                     
79A5: F0 EA      LD      A,($EA)         
79A7: FE 07      CP      $07             
79A9: 28 49      JR      Z,$79F4         
79AB: 21 70 C4   LD      HL,$C470        
79AE: 09         ADD     HL,BC           
79AF: 7E         LD      A,(HL)          
79B0: FE 02      CP      $02             
79B2: CA F5 79   JP      Z,$79F5         
79B5: FE 03      CP      $03             
79B7: CA 3E 7A   JP      Z,$7A3E         
79BA: 21 10 C3   LD      HL,$C310        
79BD: 09         ADD     HL,BC           
79BE: 7E         LD      A,(HL)          
79BF: A7         AND     A               
79C0: 28 32      JR      Z,$79F4         
79C2: F0 F9      LD      A,($F9)         
79C4: A7         AND     A               
79C5: 20 2D      JR      NZ,$79F4        
79C7: 21 40 C3   LD      HL,$C340        
79CA: 09         ADD     HL,BC           
79CB: 7E         LD      A,(HL)          
79CC: E6 10      AND     $10             
79CE: 28 24      JR      Z,$79F4         
79D0: F0 E7      LD      A,($E7)         
79D2: A9         XOR     C               
79D3: E6 01      AND     $01             
79D5: 20 1D      JR      NZ,$79F4        
79D7: FA C0 C3   LD      A,($C3C0)       
79DA: 6F         LD      L,A             
79DB: 26 00      LD      H,$00           
79DD: 11 30 C0   LD      DE,$C030        
79E0: 19         ADD     HL,DE           
79E1: F0 EF      LD      A,($EF)         
79E3: C6 0A      ADD     $0A             
79E5: 22         LD      (HLI),A         
79E6: F0 EE      LD      A,($EE)         
79E8: C6 04      ADD     $04             
79EA: 22         LD      (HLI),A         
79EB: 3E 26      LD      A,$26           
79ED: 22         LD      (HLI),A         
79EE: 70         LD      (HL),B          
79EF: 3E 01      LD      A,$01           
79F1: CD 74 79   CALL    $7974           
79F4: C9         RET                     
79F5: F0 EB      LD      A,($EB)         
79F7: FE 02      CP      $02             
79F9: 20 0B      JR      NZ,$7A06        
79FB: 21 EC FF   LD      HL,$FFEC        
79FE: 35         DEC     (HL)            
79FF: 35         DEC     (HL)            
7A00: CD 06 7A   CALL    $7A06           
7A03: C3 BA 3D   JP      $3DBA           
7A06: FA C0 C3   LD      A,($C3C0)       
7A09: 6F         LD      L,A             
7A0A: 26 00      LD      H,$00           
7A0C: 11 30 C0   LD      DE,$C030        
7A0F: 19         ADD     HL,DE           
7A10: 1E 00      LD      E,$00           
7A12: F0 E7      LD      A,($E7)         
7A14: E6 04      AND     $04             
7A16: 28 02      JR      Z,$7A1A         
7A18: 1E 10      LD      E,$10           
7A1A: F0 EC      LD      A,($EC)         
7A1C: C6 0B      ADD     $0B             
7A1E: 22         LD      (HLI),A         
7A1F: F0 EE      LD      A,($EE)         
7A21: 22         LD      (HLI),A         
7A22: 3E 1C      LD      A,$1C           
7A24: 22         LD      (HLI),A         
7A25: 7B         LD      A,E             
7A26: 22         LD      (HLI),A         
7A27: F0 EC      LD      A,($EC)         
7A29: C6 0B      ADD     $0B             
7A2B: 22         LD      (HLI),A         
7A2C: F0 EE      LD      A,($EE)         
7A2E: C6 08      ADD     $08             
7A30: 22         LD      (HLI),A         
7A31: 3E 1C      LD      A,$1C           
7A33: 22         LD      (HLI),A         
7A34: 7B         LD      A,E             
7A35: F6 20      OR      $20             
7A37: 22         LD      (HLI),A         
7A38: 3E 02      LD      A,$02           
7A3A: CD 74 79   CALL    $7974           
7A3D: C9         RET                     
7A3E: C5         PUSH    BC              
7A3F: 21 D0 C3   LD      HL,$C3D0        
7A42: 09         ADD     HL,BC           
7A43: 5E         LD      E,(HL)          
7A44: 21 40 C2   LD      HL,$C240        
7A47: 09         ADD     HL,BC           
7A48: 7E         LD      A,(HL)          
7A49: 21 50 C2   LD      HL,$C250        
7A4C: 09         ADD     HL,BC           
7A4D: 48         LD      C,B             
7A4E: B6         OR      (HL)            
7A4F: 28 06      JR      Z,$7A57         
7A51: 7B         LD      A,E             
7A52: 17         RLA                     
7A53: 17         RLA                     
7A54: E6 20      AND     $20             
7A56: 4F         LD      C,A             
7A57: FA C0 C3   LD      A,($C3C0)       
7A5A: 6F         LD      L,A             
7A5B: 26 00      LD      H,$00           
7A5D: 11 30 C0   LD      DE,$C030        
7A60: 19         ADD     HL,DE           
7A61: F0 EC      LD      A,($EC)         
7A63: C6 08      ADD     $08             
7A65: 22         LD      (HLI),A         
7A66: F0 EE      LD      A,($EE)         
7A68: 3D         DEC     A               
7A69: 22         LD      (HLI),A         
7A6A: 3E 1A      LD      A,$1A           
7A6C: 22         LD      (HLI),A         
7A6D: 79         LD      A,C             
7A6E: 22         LD      (HLI),A         
7A6F: F0 EC      LD      A,($EC)         
7A71: C6 08      ADD     $08             
7A73: 22         LD      (HLI),A         
7A74: F0 EE      LD      A,($EE)         
7A76: C6 07      ADD     $07             
7A78: 22         LD      (HLI),A         
7A79: 3E 1A      LD      A,$1A           
7A7B: 22         LD      (HLI),A         
7A7C: 79         LD      A,C             
7A7D: 77         LD      (HL),A          
7A7E: C1         POP     BC              
7A7F: 3E 02      LD      A,$02           
7A81: CD 74 79   CALL    $7974           
7A84: C9         RET                     
7A85: CD D5 3B   CALL    $3BD5           
7A88: 30 27      JR      NC,$7AB1        
7A8A: CD 4A 09   CALL    $094A           
7A8D: FA A6 C1   LD      A,($C1A6)       
7A90: A7         AND     A               
7A91: 28 11      JR      Z,$7AA4         
7A93: 5F         LD      E,A             
7A94: 50         LD      D,B             
7A95: 21 9F C3   LD      HL,$C39F        
7A98: 19         ADD     HL,DE           
7A99: 7E         LD      A,(HL)          
7A9A: FE 03      CP      $03             
7A9C: 20 06      JR      NZ,$7AA4        
7A9E: 21 8F C2   LD      HL,$C28F        
7AA1: 19         ADD     HL,DE           
7AA2: 36 00      LD      (HL),$00        
7AA4: FA 4A C1   LD      A,($C14A)       
7AA7: 5F         LD      E,A             
7AA8: CD 42 09   CALL    $0942           
7AAB: CD 95 14   CALL    $1495           
7AAE: 7B         LD      A,E             
7AAF: 37         SCF                     
7AB0: C9         RET                     
7AB1: A7         AND     A               
7AB2: C9         RET                     
7AB3: 06 04      LD      B,$04           
7AB5: 02         LD      (BC),A          
7AB6: 00         NOP                     
7AB7: 21 80 C3   LD      HL,$C380        
7ABA: 09         ADD     HL,BC           
7ABB: 5E         LD      E,(HL)          
7ABC: 50         LD      D,B             
7ABD: 21 B3 7A   LD      HL,$7AB3        
7AC0: 19         ADD     HL,DE           
7AC1: E5         PUSH    HL              
7AC2: 21 D0 C3   LD      HL,$C3D0        
7AC5: 09         ADD     HL,BC           
7AC6: 34         INC     (HL)            
7AC7: 7E         LD      A,(HL)          
7AC8: 1F         RRA                     
7AC9: 1F         RRA                     
7ACA: 1F         RRA                     
7ACB: 1F         RRA                     
7ACC: E1         POP     HL              
7ACD: E6 01      AND     $01             
7ACF: B6         OR      (HL)            
7AD0: C3 87 3B   JP      $3B87           
7AD3: 58         LD      E,B             
7AD4: F0 99      LD      A,($99)         
7AD6: 21 EF FF   LD      HL,$FFEF        
7AD9: 96         SUB     (HL)            
7ADA: C6 14      ADD     $14             
7ADC: FE 28      CP      $28             
7ADE: 30 3E      JR      NC,$7B1E        
7AE0: F0 98      LD      A,($98)         
7AE2: 21 EE FF   LD      HL,$FFEE        
7AE5: 96         SUB     (HL)            
7AE6: C6 10      ADD     $10             
7AE8: FE 20      CP      $20             
7AEA: 30 32      JR      NC,$7B1E        
7AEC: 1C         INC     E               
7AED: D5         PUSH    DE              
7AEE: CD 0E 7C   CALL    $7C0E           
7AF1: F0 9E      LD      A,($9E)         
7AF3: EE 01      XOR     $01             
7AF5: BB         CP      E               
7AF6: D1         POP     DE              
7AF7: 20 25      JR      NZ,$7B1E        
7AF9: 21 AD C1   LD      HL,$C1AD        
7AFC: 36 01      LD      (HL),$01        
7AFE: FA 9F C1   LD      A,($C19F)       
7B01: 21 4F C1   LD      HL,$C14F        
7B04: B6         OR      (HL)            
7B05: 21 46 C1   LD      HL,$C146        
7B08: B6         OR      (HL)            
7B09: 21 34 C1   LD      HL,$C134        
7B0C: B6         OR      (HL)            
7B0D: 20 0F      JR      NZ,$7B1E        
7B0F: FA 9A DB   LD      A,($DB9A)       
7B12: FE 80      CP      $80             
7B14: 20 08      JR      NZ,$7B1E        
7B16: F0 CC      LD      A,($CC)         
7B18: E6 10      AND     $10             
7B1A: 28 02      JR      Z,$7B1E         
7B1C: 37         SCF                     
7B1D: C9         RET                     
7B1E: A7         AND     A               
7B1F: C9         RET                     
7B20: F0 EA      LD      A,($EA)         
7B22: FE 05      CP      $05             
7B24: 20 1A      JR      NZ,$7B40        
7B26: FA 95 DB   LD      A,($DB95)       
7B29: FE 07      CP      $07             
7B2B: 28 13      JR      Z,$7B40         
7B2D: 21 A8 C1   LD      HL,$C1A8        
7B30: FA 9F C1   LD      A,($C19F)       
7B33: B6         OR      (HL)            
7B34: 21 4F C1   LD      HL,$C14F        
7B37: B6         OR      (HL)            
7B38: 20 06      JR      NZ,$7B40        
7B3A: FA 24 C1   LD      A,($C124)       
7B3D: A7         AND     A               
7B3E: 28 01      JR      Z,$7B41         
7B40: F1         POP     AF              
7B41: C9         RET                     
7B42: 21 10 C4   LD      HL,$C410        
7B45: 09         ADD     HL,BC           
7B46: 7E         LD      A,(HL)          
7B47: A7         AND     A               
7B48: 28 41      JR      Z,$7B8B         
7B4A: 3D         DEC     A               
7B4B: 77         LD      (HL),A          
7B4C: CD B8 3E   CALL    $3EB8           
7B4F: 21 40 C2   LD      HL,$C240        
7B52: 09         ADD     HL,BC           
7B53: 7E         LD      A,(HL)          
7B54: F5         PUSH    AF              
7B55: 21 50 C2   LD      HL,$C250        
7B58: 09         ADD     HL,BC           
7B59: 7E         LD      A,(HL)          
7B5A: F5         PUSH    AF              
7B5B: 21 F0 C3   LD      HL,$C3F0        
7B5E: 09         ADD     HL,BC           
7B5F: 7E         LD      A,(HL)          
7B60: 21 40 C2   LD      HL,$C240        
7B63: 09         ADD     HL,BC           
7B64: 77         LD      (HL),A          
7B65: 21 00 C4   LD      HL,$C400        
7B68: 09         ADD     HL,BC           
7B69: 7E         LD      A,(HL)          
7B6A: 21 50 C2   LD      HL,$C250        
7B6D: 09         ADD     HL,BC           
7B6E: 77         LD      (HL),A          
7B6F: CD 8C 7B   CALL    $7B8C           
7B72: 21 30 C4   LD      HL,$C430        
7B75: 09         ADD     HL,BC           
7B76: 7E         LD      A,(HL)          
7B77: E6 20      AND     $20             
7B79: 20 03      JR      NZ,$7B7E        
7B7B: CD 9E 3B   CALL    $3B9E           
7B7E: 21 50 C2   LD      HL,$C250        
7B81: 09         ADD     HL,BC           
7B82: F1         POP     AF              
7B83: 77         LD      (HL),A          
7B84: 21 40 C2   LD      HL,$C240        
7B87: 09         ADD     HL,BC           
7B88: F1         POP     AF              
7B89: 77         LD      (HL),A          
7B8A: F1         POP     AF              
7B8B: C9         RET                     
7B8C: CD 99 7B   CALL    $7B99           
7B8F: C5         PUSH    BC              
7B90: 79         LD      A,C             
7B91: C6 10      ADD     $10             
7B93: 4F         LD      C,A             
7B94: CD 99 7B   CALL    $7B99           
7B97: C1         POP     BC              
7B98: C9         RET                     
7B99: 21 40 C2   LD      HL,$C240        
7B9C: 09         ADD     HL,BC           
7B9D: 7E         LD      A,(HL)          
7B9E: A7         AND     A               
7B9F: 28 23      JR      Z,$7BC4         
7BA1: F5         PUSH    AF              
7BA2: CB 37      SET     1,E             
7BA4: E6 F0      AND     $F0             
7BA6: 21 60 C2   LD      HL,$C260        
7BA9: 09         ADD     HL,BC           
7BAA: 86         ADD     A,(HL)          
7BAB: 77         LD      (HL),A          
7BAC: CB 12      SET     1,E             
7BAE: 21 00 C2   LD      HL,$C200        
7BB1: 09         ADD     HL,BC           
7BB2: F1         POP     AF              
7BB3: 1E 00      LD      E,$00           
7BB5: CB 7F      SET     1,E             
7BB7: 28 02      JR      Z,$7BBB         
7BB9: 1E F0      LD      E,$F0           
7BBB: CB 37      SET     1,E             
7BBD: E6 0F      AND     $0F             
7BBF: B3         OR      E               
7BC0: CB 1A      SET     1,E             
7BC2: 8E         ADC     A,(HL)          
7BC3: 77         LD      (HL),A          
7BC4: C9         RET                     
7BC5: 21 20 C3   LD      HL,$C320        
7BC8: 09         ADD     HL,BC           
7BC9: 7E         LD      A,(HL)          
7BCA: A7         AND     A               
7BCB: 28 F7      JR      Z,$7BC4         
7BCD: F5         PUSH    AF              
7BCE: CB 37      SET     1,E             
7BD0: E6 F0      AND     $F0             
7BD2: 21 30 C3   LD      HL,$C330        
7BD5: 09         ADD     HL,BC           
7BD6: 86         ADD     A,(HL)          
7BD7: 77         LD      (HL),A          
7BD8: CB 12      SET     1,E             
7BDA: 21 10 C3   LD      HL,$C310        
7BDD: 18 D2      JR      $7BB1           
7BDF: 1E 00      LD      E,$00           
7BE1: F0 98      LD      A,($98)         
7BE3: 21 00 C2   LD      HL,$C200        
7BE6: 09         ADD     HL,BC           
7BE7: 96         SUB     (HL)            
7BE8: CB 7F      SET     1,E             
7BEA: 28 01      JR      Z,$7BED         
7BEC: 1C         INC     E               
7BED: 57         LD      D,A             
7BEE: C9         RET                     
7BEF: 1E 02      LD      E,$02           
7BF1: F0 99      LD      A,($99)         
7BF3: 21 10 C2   LD      HL,$C210        
7BF6: 09         ADD     HL,BC           
7BF7: 96         SUB     (HL)            
7BF8: CB 7F      SET     1,E             
7BFA: 20 01      JR      NZ,$7BFD        
7BFC: 1C         INC     E               
7BFD: 57         LD      D,A             
7BFE: C9         RET                     
7BFF: 1E 02      LD      E,$02           
7C01: F0 99      LD      A,($99)         
7C03: 21 EC FF   LD      HL,$FFEC        
7C06: 96         SUB     (HL)            
7C07: CB 7F      SET     1,E             
7C09: 20 01      JR      NZ,$7C0C        
7C0B: 1C         INC     E               
7C0C: 57         LD      D,A             
7C0D: C9         RET                     
7C0E: CD DF 7B   CALL    $7BDF           
7C11: 7B         LD      A,E             
7C12: E0 D7      LDFF00  ($D7),A         
7C14: 7A         LD      A,D             
7C15: CB 7F      SET     1,E             
7C17: 28 02      JR      Z,$7C1B         
7C19: 2F         CPL                     
7C1A: 3C         INC     A               
7C1B: F5         PUSH    AF              
7C1C: CD EF 7B   CALL    $7BEF           
7C1F: 7B         LD      A,E             
7C20: E0 D8      LDFF00  ($D8),A         
7C22: 7A         LD      A,D             
7C23: CB 7F      SET     1,E             
7C25: 28 02      JR      Z,$7C29         
7C27: 2F         CPL                     
7C28: 3C         INC     A               
7C29: D1         POP     DE              
7C2A: BA         CP      D               
7C2B: 30 04      JR      NC,$7C31        
7C2D: F0 D7      LD      A,($D7)         
7C2F: 18 02      JR      $7C33           
7C31: F0 D8      LD      A,($D8)         
7C33: 5F         LD      E,A             
7C34: C9         RET                     
7C35: 21 80 C2   LD      HL,$C280        
7C38: 09         ADD     HL,BC           
7C39: 70         LD      (HL),B          
7C3A: C9         RET                     
7C3B: 21 C0 C2   LD      HL,$C2C0        
7C3E: 09         ADD     HL,BC           
7C3F: 7E         LD      A,(HL)          
7C40: C7         RST     0X00            
7C41: 47         LD      B,A             
7C42: 7C         LD      A,H             
7C43: 58         LD      E,B             
7C44: 7C         LD      A,H             
7C45: 69         LD      L,C             
7C46: 7C         LD      A,H             
7C47: CD 91 08   CALL    $0891           
7C4A: 36 A0      LD      (HL),$A0        
7C4C: 21 20 C4   LD      HL,$C420        
7C4F: 09         ADD     HL,BC           
7C50: 36 FF      LD      (HL),$FF        
7C52: 21 C0 C2   LD      HL,$C2C0        
7C55: 09         ADD     HL,BC           
7C56: 34         INC     (HL)            
7C57: C9         RET                     
7C58: CD 91 08   CALL    $0891           
7C5B: 20 0B      JR      NZ,$7C68        
7C5D: 36 C0      LD      (HL),$C0        
7C5F: 21 20 C4   LD      HL,$C420        
7C62: 09         ADD     HL,BC           
7C63: 36 FF      LD      (HL),$FF        
7C65: CD 52 7C   CALL    $7C52           
7C68: C9         RET                     
7C69: CD 91 08   CALL    $0891           
7C6C: 20 06      JR      NZ,$7C74        
7C6E: CD D7 08   CALL    $08D7           
7C71: C3 7A 3F   JP      $3F7A           
7C74: CD 78 7C   CALL    $7C78           
7C77: C9         RET                     
7C78: E6 07      AND     $07             
7C7A: 20 1D      JR      NZ,$7C99        
7C7C: CD ED 27   CALL    $27ED           
7C7F: E6 1F      AND     $1F             
7C81: D6 10      SUB     $10             
7C83: 5F         LD      E,A             
7C84: 21 EE FF   LD      HL,$FFEE        
7C87: 86         ADD     A,(HL)          
7C88: 77         LD      (HL),A          
7C89: CD ED 27   CALL    $27ED           
7C8C: E6 1F      AND     $1F             
7C8E: D6 14      SUB     $14             
7C90: 5F         LD      E,A             
7C91: 21 EC FF   LD      HL,$FFEC        
7C94: 86         ADD     A,(HL)          
7C95: 77         LD      (HL),A          
7C96: CD 9A 7C   CALL    $7C9A           
7C99: C9         RET                     
7C9A: CD 26 7B   CALL    $7B26           
7C9D: F0 EE      LD      A,($EE)         
7C9F: E0 D7      LDFF00  ($D7),A         
7CA1: F0 EC      LD      A,($EC)         
7CA3: E0 D8      LDFF00  ($D8),A         
7CA5: 3E 02      LD      A,$02           
7CA7: CD 53 09   CALL    $0953           
7CAA: 3E 13      LD      A,$13           
7CAC: E0 F4      LDFF00  ($F4),A         
7CAE: C9         RET                     
7CAF: 3E 36      LD      A,$36           
7CB1: CD 01 3C   CALL    $3C01           
7CB4: F0 D7      LD      A,($D7)         
7CB6: 21 00 C2   LD      HL,$C200        
7CB9: 19         ADD     HL,DE           
7CBA: 77         LD      (HL),A          
7CBB: F0 D8      LD      A,($D8)         
7CBD: 21 10 C2   LD      HL,$C210        
7CC0: 19         ADD     HL,DE           
7CC1: 77         LD      (HL),A          
7CC2: F0 F9      LD      A,($F9)         
7CC4: A7         AND     A               
7CC5: 28 08      JR      Z,$7CCF         
7CC7: 21 50 C2   LD      HL,$C250        
7CCA: 09         ADD     HL,BC           
7CCB: 36 F0      LD      (HL),$F0        
7CCD: 18 0C      JR      $7CDB           
7CCF: 21 20 C3   LD      HL,$C320        
7CD2: 19         ADD     HL,DE           
7CD3: 36 10      LD      (HL),$10        
7CD5: 21 10 C3   LD      HL,$C310        
7CD8: 19         ADD     HL,DE           
7CD9: 36 08      LD      (HL),$08        
7CDB: CD 35 7C   CALL    $7C35           
7CDE: 21 F4 FF   LD      HL,$FFF4        
7CE1: 36 1A      LD      (HL),$1A        
7CE3: C9         RET                     
7CE4: 21 00 D8   LD      HL,$D800        
7CE7: F0 F6      LD      A,($F6)         
7CE9: 5F         LD      E,A             
7CEA: FA A5 DB   LD      A,($DBA5)       
7CED: 57         LD      D,A             
7CEE: F0 F7      LD      A,($F7)         
7CF0: FE 1A      CP      $1A             
7CF2: 30 05      JR      NC,$7CF9        
7CF4: FE 06      CP      $06             
7CF6: 38 01      JR      C,$7CF9         
7CF8: 14         INC     D               
7CF9: 19         ADD     HL,DE           
7CFA: 7E         LD      A,(HL)          
7CFB: F6 20      OR      $20             
7CFD: 77         LD      (HL),A          
7CFE: E0 F8      LDFF00  ($F8),A         
7D00: C9         RET                     
7D01: FF         RST     0X38            
7D02: FF         RST     0X38            
7D03: FF         RST     0X38            
7D04: FF         RST     0X38            
7D05: FF         RST     0X38            
7D06: FF         RST     0X38            
7D07: FF         RST     0X38            
7D08: FF         RST     0X38            
7D09: FF         RST     0X38            
7D0A: FF         RST     0X38            
7D0B: FF         RST     0X38            
7D0C: FF         RST     0X38            
7D0D: FF         RST     0X38            
7D0E: FF         RST     0X38            
7D0F: FF         RST     0X38            
7D10: FF         RST     0X38            
7D11: FF         RST     0X38            
7D12: FF         RST     0X38            
7D13: FF         RST     0X38            
7D14: FF         RST     0X38            
7D15: FF         RST     0X38            
7D16: FF         RST     0X38            
7D17: FF         RST     0X38            
7D18: FF         RST     0X38            
7D19: FF         RST     0X38            
7D1A: FF         RST     0X38            
7D1B: FF         RST     0X38            
7D1C: FF         RST     0X38            
7D1D: FF         RST     0X38            
7D1E: FF         RST     0X38            
7D1F: FF         RST     0X38            
7D20: FF         RST     0X38            
7D21: FF         RST     0X38            
7D22: FF         RST     0X38            
7D23: FF         RST     0X38            
7D24: FF         RST     0X38            
7D25: FF         RST     0X38            
7D26: FF         RST     0X38            
7D27: FF         RST     0X38            
7D28: FF         RST     0X38            
7D29: FF         RST     0X38            
7D2A: FF         RST     0X38            
7D2B: FF         RST     0X38            
7D2C: FF         RST     0X38            
7D2D: FF         RST     0X38            
7D2E: FF         RST     0X38            
7D2F: FF         RST     0X38            
7D30: FF         RST     0X38            
7D31: FF         RST     0X38            
7D32: FF         RST     0X38            
7D33: FF         RST     0X38            
7D34: FF         RST     0X38            
7D35: FF         RST     0X38            
7D36: FF         RST     0X38            
7D37: FF         RST     0X38            
7D38: FF         RST     0X38            
7D39: FF         RST     0X38            
7D3A: FF         RST     0X38            
7D3B: FF         RST     0X38            
7D3C: FF         RST     0X38            
7D3D: FF         RST     0X38            
7D3E: FF         RST     0X38            
7D3F: FF         RST     0X38            
7D40: FF         RST     0X38            
7D41: FF         RST     0X38            
7D42: FF         RST     0X38            
7D43: FF         RST     0X38            
7D44: FF         RST     0X38            
7D45: FF         RST     0X38            
7D46: FF         RST     0X38            
7D47: FF         RST     0X38            
7D48: FF         RST     0X38            
7D49: FF         RST     0X38            
7D4A: FF         RST     0X38            
7D4B: FF         RST     0X38            
7D4C: FF         RST     0X38            
7D4D: FF         RST     0X38            
7D4E: FF         RST     0X38            
7D4F: FF         RST     0X38            
7D50: FF         RST     0X38            
7D51: FF         RST     0X38            
7D52: FF         RST     0X38            
7D53: FF         RST     0X38            
7D54: FF         RST     0X38            
7D55: FF         RST     0X38            
7D56: FF         RST     0X38            
7D57: FF         RST     0X38            
7D58: FF         RST     0X38            
7D59: FF         RST     0X38            
7D5A: FF         RST     0X38            
7D5B: FF         RST     0X38            
7D5C: FF         RST     0X38            
7D5D: FF         RST     0X38            
7D5E: FF         RST     0X38            
7D5F: FF         RST     0X38            
7D60: FF         RST     0X38            
7D61: FF         RST     0X38            
7D62: FF         RST     0X38            
7D63: FF         RST     0X38            
7D64: FF         RST     0X38            
7D65: FF         RST     0X38            
7D66: FF         RST     0X38            
7D67: FF         RST     0X38            
7D68: FF         RST     0X38            
7D69: FF         RST     0X38            
7D6A: FF         RST     0X38            
7D6B: FF         RST     0X38            
7D6C: FF         RST     0X38            
7D6D: FF         RST     0X38            
7D6E: FF         RST     0X38            
7D6F: FF         RST     0X38            
7D70: FF         RST     0X38            
7D71: FF         RST     0X38            
7D72: FF         RST     0X38            
7D73: FF         RST     0X38            
7D74: FF         RST     0X38            
7D75: FF         RST     0X38            
7D76: FF         RST     0X38            
7D77: FF         RST     0X38            
7D78: FF         RST     0X38            
7D79: FF         RST     0X38            
7D7A: FF         RST     0X38            
7D7B: FF         RST     0X38            
7D7C: FF         RST     0X38            
7D7D: FF         RST     0X38            
7D7E: FF         RST     0X38            
7D7F: FF         RST     0X38            
7D80: FF         RST     0X38            
7D81: FF         RST     0X38            
7D82: FF         RST     0X38            
7D83: FF         RST     0X38            
7D84: FF         RST     0X38            
7D85: FF         RST     0X38            
7D86: FF         RST     0X38            
7D87: FF         RST     0X38            
7D88: FF         RST     0X38            
7D89: FF         RST     0X38            
7D8A: FF         RST     0X38            
7D8B: FF         RST     0X38            
7D8C: FF         RST     0X38            
7D8D: FF         RST     0X38            
7D8E: FF         RST     0X38            
7D8F: FF         RST     0X38            
7D90: FF         RST     0X38            
7D91: FF         RST     0X38            
7D92: FF         RST     0X38            
7D93: FF         RST     0X38            
7D94: FF         RST     0X38            
7D95: FF         RST     0X38            
7D96: FF         RST     0X38            
7D97: FF         RST     0X38            
7D98: FF         RST     0X38            
7D99: FF         RST     0X38            
7D9A: FF         RST     0X38            
7D9B: FF         RST     0X38            
7D9C: FF         RST     0X38            
7D9D: FF         RST     0X38            
7D9E: FF         RST     0X38            
7D9F: FF         RST     0X38            
7DA0: FF         RST     0X38            
7DA1: FF         RST     0X38            
7DA2: FF         RST     0X38            
7DA3: FF         RST     0X38            
7DA4: FF         RST     0X38            
7DA5: FF         RST     0X38            
7DA6: FF         RST     0X38            
7DA7: FF         RST     0X38            
7DA8: FF         RST     0X38            
7DA9: FF         RST     0X38            
7DAA: FF         RST     0X38            
7DAB: FF         RST     0X38            
7DAC: FF         RST     0X38            
7DAD: FF         RST     0X38            
7DAE: FF         RST     0X38            
7DAF: FF         RST     0X38            
7DB0: FF         RST     0X38            
7DB1: FF         RST     0X38            
7DB2: FF         RST     0X38            
7DB3: FF         RST     0X38            
7DB4: FF         RST     0X38            
7DB5: FF         RST     0X38            
7DB6: FF         RST     0X38            
7DB7: FF         RST     0X38            
7DB8: FF         RST     0X38            
7DB9: FF         RST     0X38            
7DBA: FF         RST     0X38            
7DBB: FF         RST     0X38            
7DBC: FF         RST     0X38            
7DBD: FF         RST     0X38            
7DBE: FF         RST     0X38            
7DBF: FF         RST     0X38            
7DC0: FF         RST     0X38            
7DC1: FF         RST     0X38            
7DC2: FF         RST     0X38            
7DC3: FF         RST     0X38            
7DC4: FF         RST     0X38            
7DC5: FF         RST     0X38            
7DC6: FF         RST     0X38            
7DC7: FF         RST     0X38            
7DC8: FF         RST     0X38            
7DC9: FF         RST     0X38            
7DCA: FF         RST     0X38            
7DCB: FF         RST     0X38            
7DCC: FF         RST     0X38            
7DCD: FF         RST     0X38            
7DCE: FF         RST     0X38            
7DCF: FF         RST     0X38            
7DD0: FF         RST     0X38            
7DD1: FF         RST     0X38            
7DD2: FF         RST     0X38            
7DD3: FF         RST     0X38            
7DD4: FF         RST     0X38            
7DD5: FF         RST     0X38            
7DD6: FF         RST     0X38            
7DD7: FF         RST     0X38            
7DD8: FF         RST     0X38            
7DD9: FF         RST     0X38            
7DDA: FF         RST     0X38            
7DDB: FF         RST     0X38            
7DDC: FF         RST     0X38            
7DDD: FF         RST     0X38            
7DDE: FF         RST     0X38            
7DDF: FF         RST     0X38            
7DE0: FF         RST     0X38            
7DE1: FF         RST     0X38            
7DE2: FF         RST     0X38            
7DE3: FF         RST     0X38            
7DE4: FF         RST     0X38            
7DE5: FF         RST     0X38            
7DE6: FF         RST     0X38            
7DE7: FF         RST     0X38            
7DE8: FF         RST     0X38            
7DE9: FF         RST     0X38            
7DEA: FF         RST     0X38            
7DEB: FF         RST     0X38            
7DEC: FF         RST     0X38            
7DED: FF         RST     0X38            
7DEE: FF         RST     0X38            
7DEF: FF         RST     0X38            
7DF0: FF         RST     0X38            
7DF1: FF         RST     0X38            
7DF2: FF         RST     0X38            
7DF3: FF         RST     0X38            
7DF4: FF         RST     0X38            
7DF5: FF         RST     0X38            
7DF6: FF         RST     0X38            
7DF7: FF         RST     0X38            
7DF8: FF         RST     0X38            
7DF9: FF         RST     0X38            
7DFA: FF         RST     0X38            
7DFB: FF         RST     0X38            
7DFC: FF         RST     0X38            
7DFD: FF         RST     0X38            
7DFE: FF         RST     0X38            
7DFF: FF         RST     0X38            
7E00: FF         RST     0X38            
7E01: FF         RST     0X38            
7E02: FF         RST     0X38            
7E03: FF         RST     0X38            
7E04: FF         RST     0X38            
7E05: FF         RST     0X38            
7E06: FF         RST     0X38            
7E07: FF         RST     0X38            
7E08: FF         RST     0X38            
7E09: FF         RST     0X38            
7E0A: FF         RST     0X38            
7E0B: FF         RST     0X38            
7E0C: FF         RST     0X38            
7E0D: FF         RST     0X38            
7E0E: FF         RST     0X38            
7E0F: FF         RST     0X38            
7E10: FF         RST     0X38            
7E11: FF         RST     0X38            
7E12: FF         RST     0X38            
7E13: FF         RST     0X38            
7E14: FF         RST     0X38            
7E15: FF         RST     0X38            
7E16: FF         RST     0X38            
7E17: FF         RST     0X38            
7E18: FF         RST     0X38            
7E19: FF         RST     0X38            
7E1A: FF         RST     0X38            
7E1B: FF         RST     0X38            
7E1C: FF         RST     0X38            
7E1D: FF         RST     0X38            
7E1E: FF         RST     0X38            
7E1F: FF         RST     0X38            
7E20: FF         RST     0X38            
7E21: FF         RST     0X38            
7E22: FF         RST     0X38            
7E23: FF         RST     0X38            
7E24: FF         RST     0X38            
7E25: FF         RST     0X38            
7E26: FF         RST     0X38            
7E27: FF         RST     0X38            
7E28: FF         RST     0X38            
7E29: FF         RST     0X38            
7E2A: FF         RST     0X38            
7E2B: FF         RST     0X38            
7E2C: FF         RST     0X38            
7E2D: FF         RST     0X38            
7E2E: FF         RST     0X38            
7E2F: FF         RST     0X38            
7E30: FF         RST     0X38            
7E31: FF         RST     0X38            
7E32: FF         RST     0X38            
7E33: FF         RST     0X38            
7E34: FF         RST     0X38            
7E35: FF         RST     0X38            
7E36: FF         RST     0X38            
7E37: FF         RST     0X38            
7E38: FF         RST     0X38            
7E39: FF         RST     0X38            
7E3A: FF         RST     0X38            
7E3B: FF         RST     0X38            
7E3C: FF         RST     0X38            
7E3D: FF         RST     0X38            
7E3E: FF         RST     0X38            
7E3F: FF         RST     0X38            
7E40: FF         RST     0X38            
7E41: FF         RST     0X38            
7E42: FF         RST     0X38            
7E43: FF         RST     0X38            
7E44: FF         RST     0X38            
7E45: FF         RST     0X38            
7E46: FF         RST     0X38            
7E47: FF         RST     0X38            
7E48: FF         RST     0X38            
7E49: FF         RST     0X38            
7E4A: FF         RST     0X38            
7E4B: FF         RST     0X38            
7E4C: FF         RST     0X38            
7E4D: FF         RST     0X38            
7E4E: FF         RST     0X38            
7E4F: FF         RST     0X38            
7E50: FF         RST     0X38            
7E51: FF         RST     0X38            
7E52: FF         RST     0X38            
7E53: FF         RST     0X38            
7E54: FF         RST     0X38            
7E55: FF         RST     0X38            
7E56: FF         RST     0X38            
7E57: FF         RST     0X38            
7E58: FF         RST     0X38            
7E59: FF         RST     0X38            
7E5A: FF         RST     0X38            
7E5B: FF         RST     0X38            
7E5C: FF         RST     0X38            
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