![Bank 09](GBZelda.jpg)

# Bank 09

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```code
4000: 00         NOP                     
4001: 42         LD      B,D             
4002: 64         LD      H,H             
4003: 42         LD      B,D             
4004: B5         OR      L               
4005: 42         LD      B,D             
4006: 16 43      LD      D,$43           
4008: 8B         ADC     A,E             
4009: 43         LD      B,E             
400A: D8         RET     C               
400B: 43         LD      B,E             
400C: 1F         RRA                     
400D: 44         LD      B,H             
400E: 0F         RRCA                    
400F: 45         LD      B,L             
4010: 6C         LD      L,H             
4011: 45         LD      B,L             
4012: B8         CP      B               
4013: 45         LD      B,L             
4014: 10 46      STOP    $46             
4016: 61         LD      H,C             
4017: 46         LD      B,(HL)          
4018: AB         XOR     E               
4019: 46         LD      B,(HL)          
401A: 24         INC     H               
401B: 47         LD      B,A             
401C: 8F         ADC     A,A             
401D: 47         LD      B,A             
401E: 54         LD      D,H             
401F: 48         LD      C,B             
4020: A0         AND     B               
4021: 48         LD      C,B             
4022: EF         RST     0X28            
4023: 48         LD      C,B             
4024: 46         LD      B,(HL)          
4025: 49         LD      C,C             
4026: 68         LD      L,B             
4027: 49         LD      C,C             
4028: 9F         SBC     A               
4029: 49         LD      C,C             
402A: DB                              
402B: 49         LD      C,C             
402C: 1E 4A      LD      E,$4A           
402E: 69         LD      L,C             
402F: 4A         LD      C,D             
4030: D6 4A      SUB     $4A             
4032: 27         DAA                     
4033: 4B         LD      C,E             
4034: 6C         LD      L,H             
4035: 4B         LD      C,E             
4036: B7         OR      A               
4037: 4B         LD      C,E             
4038: 74         LD      (HL),H          
4039: 4C         LD      C,H             
403A: C2 4C 1B   JP      NZ,$1B4C        
403D: 4D         LD      C,L             
403E: 84         ADD     A,H             
403F: 4D         LD      C,L             
4040: EC                              
4041: 4D         LD      C,L             
4042: 23         INC     HL              
4043: 4E         LD      C,(HL)          
4044: 62         LD      H,D             
4045: 4E         LD      C,(HL)          
4046: 97         SUB     A               
4047: 4E         LD      C,(HL)          
4048: C0         RET     NZ              
4049: 4E         LD      C,(HL)          
404A: 0F         RRCA                    
404B: 4F         LD      C,A             
404C: 41         LD      B,C             
404D: 4F         LD      C,A             
404E: 73         LD      (HL),E          
404F: 4F         LD      C,A             
4050: AD         XOR     L               
4051: 4F         LD      C,A             
4052: E9         JP      (HL)            
4053: 4F         LD      C,A             
4054: 23         INC     HL              
4055: 50         LD      D,B             
4056: 60         LD      H,B             
4057: 50         LD      D,B             
4058: 0B         DEC     BC              
4059: 51         LD      D,C             
405A: 47         LD      B,A             
405B: 51         LD      D,C             
405C: 84         ADD     A,H             
405D: 51         LD      D,C             
405E: BA         CP      D               
405F: 51         LD      D,C             
4060: F6 51      OR      $51             
4062: 32         LD      (HLD),A         
4063: 52         LD      D,D             
4064: 6B         LD      L,E             
4065: 52         LD      D,D             
4066: CE 52      ADC     $52             
4068: F5         PUSH    AF              
4069: 52         LD      D,D             
406A: 50         LD      D,B             
406B: 53         LD      D,E             
406C: 94         SUB     H               
406D: 53         LD      D,E             
406E: CE 53      ADC     $53             
4070: F6 53      OR      $53             
4072: 4C         LD      C,H             
4073: 54         LD      D,H             
4074: 7C         LD      A,H             
4075: 54         LD      D,H             
4076: B8         CP      B               
4077: 54         LD      D,H             
4078: 15         DEC     D               
4079: 55         LD      D,L             
407A: 6C         LD      L,H             
407B: 55         LD      D,L             
407C: A9         XOR     C               
407D: 55         LD      D,L             
407E: DC 55 1F   CALL    C,$1F55         
4081: 56         LD      D,(HL)          
4082: 6A         LD      L,D             
4083: 56         LD      D,(HL)          
4084: BC         CP      H               
4085: 56         LD      D,(HL)          
4086: 2C         INC     L               
4087: 57         LD      D,A             
4088: 70         LD      (HL),B          
4089: 57         LD      D,A             
408A: B7         OR      A               
408B: 57         LD      D,A             
408C: FD                              
408D: 57         LD      D,A             
408E: 3B         DEC     SP              
408F: 58         LD      E,B             
4090: 74         LD      (HL),H          
4091: 58         LD      E,B             
4092: C3 58 E4   JP      $E458           
4095: 58         LD      E,B             
4096: 22         LD      (HLI),A         
4097: 59         LD      E,C             
4098: 48         LD      C,B             
4099: 59         LD      E,C             
409A: 96         SUB     (HL)            
409B: 59         LD      E,C             
409C: E7         RST     0X20            
409D: 59         LD      E,C             
409E: 0C         INC     C               
409F: 5A         LD      E,D             
40A0: 3D         DEC     A               
40A1: 5A         LD      E,D             
40A2: 8D         ADC     A,L             
40A3: 5A         LD      E,D             
40A4: E0 5A      LDFF00  ($5A),A         
40A6: 33         INC     SP              
40A7: 5B         LD      E,E             
40A8: 80         ADD     A,B             
40A9: 5B         LD      E,E             
40AA: BC         CP      H               
40AB: 5B         LD      E,E             
40AC: F3         DI                      
40AD: 5B         LD      E,E             
40AE: 2F         CPL                     
40AF: 5C         LD      E,H             
40B0: 71         LD      (HL),C          
40B1: 5C         LD      E,H             
40B2: A7         AND     A               
40B3: 5C         LD      E,H             
40B4: E5         PUSH    HL              
40B5: 5C         LD      E,H             
40B6: 0F         RRCA                    
40B7: 5D         LD      E,L             
40B8: 43         LD      B,E             
40B9: 5D         LD      E,L             
40BA: 89         ADC     A,C             
40BB: 5D         LD      E,L             
40BC: D1         POP     DE              
40BD: 5D         LD      E,L             
40BE: 20 5E      JR      NZ,$411E        
40C0: 62         LD      H,D             
40C1: 5E         LD      E,(HL)          
40C2: A5         AND     L               
40C3: 5E         LD      E,(HL)          
40C4: F1         POP     AF              
40C5: 5E         LD      E,(HL)          
40C6: 8D         ADC     A,L             
40C7: 5A         LD      E,D             
40C8: 4A         LD      C,D             
40C9: 5F         LD      E,A             
40CA: 86         ADD     A,(HL)          
40CB: 5F         LD      E,A             
40CC: C4 5F 0D   CALL    NZ,$0D5F        
40CF: 60         LD      H,B             
40D0: 58         LD      E,B             
40D1: 60         LD      H,B             
40D2: 7F         LD      A,A             
40D3: 60         LD      H,B             
40D4: C9         RET                     
40D5: 60         LD      H,B             
40D6: FD                              
40D7: 60         LD      H,B             
40D8: 36 61      LD      (HL),$61        
40DA: 85         ADD     A,L             
40DB: 61         LD      H,C             
40DC: C5         PUSH    BC              
40DD: 61         LD      H,C             
40DE: 06 62      LD      B,$62           
40E0: 41         LD      B,C             
40E1: 62         LD      H,D             
40E2: 87         ADD     A,A             
40E3: 62         LD      H,D             
40E4: C0         RET     NZ              
40E5: 62         LD      H,D             
40E6: 0A         LD      A,(BC)          
40E7: 63         LD      H,E             
40E8: 5D         LD      E,L             
40E9: 63         LD      H,E             
40EA: 94         SUB     H               
40EB: 63         LD      H,E             
40EC: DB                              
40ED: 63         LD      H,E             
40EE: 30 64      JR      NC,$4154        
40F0: 7F         LD      A,A             
40F1: 64         LD      H,H             
40F2: B1         OR      C               
40F3: 64         LD      H,H             
40F4: 43         LD      B,E             
40F5: 65         LD      H,L             
40F6: 64         LD      H,H             
40F7: 65         LD      H,L             
40F8: A8         XOR     B               
40F9: 65         LD      H,L             
40FA: CC 65 F5   CALL    Z,$F565         
40FD: 65         LD      H,L             
40FE: 1E 66      LD      E,$66           
4100: 00         NOP                     
4101: 40         LD      B,B             
4102: 39         ADD     HL,SP           
4103: 40         LD      B,B             
4104: 82         ADD     A,D             
4105: 40         LD      B,B             
4106: BC         CP      H               
4107: 40         LD      B,B             
4108: F7         RST     0X30            
4109: 40         LD      B,B             
410A: 2F         CPL                     
410B: 41         LD      B,C             
410C: 83         ADD     A,E             
410D: 41         LD      B,C             
410E: E2         LDFF00  (C),A           
410F: 41         LD      B,C             
4110: 30 42      JR      NC,$4154        
4112: 5D         LD      E,L             
4113: 42         LD      B,D             
4114: 93         SUB     E               
4115: 42         LD      B,D             
4116: C0         RET     NZ              
4117: 42         LD      B,D             
4118: FD                              
4119: 42         LD      B,D             
411A: C1         POP     BC              
411B: 43         LD      B,E             
411C: 02         LD      (BC),A          
411D: 44         LD      B,H             
411E: 42         LD      B,D             
411F: 44         LD      B,H             
4120: 9B         SBC     E               
4121: 44         LD      B,H             
4122: C4 44 E3   CALL    NZ,$E344        
4125: 44         LD      B,H             
4126: 1E 45      LD      E,$45           
4128: 51         LD      D,C             
4129: 45         LD      B,L             
412A: 8D         ADC     A,L             
412B: 45         LD      B,L             
412C: D9         RETI                    
412D: 45         LD      B,L             
412E: 03         INC     BC              
412F: 46         LD      B,(HL)          
4130: 3D         DEC     A               
4131: 46         LD      B,(HL)          
4132: 80         ADD     A,B             
4133: 46         LD      B,(HL)          
4134: BD         CP      L               
4135: 46         LD      B,(HL)          
4136: E6 46      AND     $46             
4138: 32         LD      (HLD),A         
4139: 47         LD      B,A             
413A: 74         LD      (HL),H          
413B: 47         LD      B,A             
413C: AF         XOR     A               
413D: 47         LD      B,A             
413E: E7         RST     0X20            
413F: 47         LD      B,A             
4140: 22         LD      (HLI),A         
4141: 48         LD      C,B             
4142: 6E         LD      L,(HL)          
4143: 48         LD      C,B             
4144: B3         OR      E               
4145: 48         LD      C,B             
4146: E6 48      AND     $48             
4148: FE 48      CP      $48             
414A: 41         LD      B,C             
414B: 49         LD      C,C             
414C: 7B         LD      A,E             
414D: 49         LD      C,C             
414E: B8         CP      B               
414F: 49         LD      C,C             
4150: EC                              
4151: 49         LD      C,C             
4152: 21 4A 4E   LD      HL,$4E4A        
4155: 4A         LD      C,D             
4156: 6D         LD      L,L             
4157: 4A         LD      C,D             
4158: B6         OR      (HL)            
4159: 4A         LD      C,D             
415A: 03         INC     BC              
415B: 4B         LD      C,E             
415C: 25         DEC     H               
415D: 4B         LD      C,E             
415E: 53         LD      D,E             
415F: 4B         LD      C,E             
4160: A2         AND     D               
4161: 4B         LD      C,E             
4162: D0         RET     NC              
4163: 4B         LD      C,E             
4164: FB         EI                      
4165: 4B         LD      C,E             
4166: 2C         INC     L               
4167: 4C         LD      C,H             
4168: 69         LD      L,C             
4169: 4C         LD      C,H             
416A: 9F         SBC     A               
416B: 4C         LD      C,H             
416C: 00         NOP                     
416D: 4D         LD      C,L             
416E: 4A         LD      C,D             
416F: 4D         LD      C,L             
4170: 8B         ADC     A,E             
4171: 4D         LD      C,L             
4172: D5         PUSH    DE              
4173: 4D         LD      C,L             
4174: 08 4E 4D   LD      ($4D4E),SP      
4177: 4E         LD      C,(HL)          
4178: 8D         ADC     A,L             
4179: 4E         LD      C,(HL)          
417A: CD 4E EE   CALL    $EE4E           
417D: 4E         LD      C,(HL)          
417E: 16 4F      LD      D,$4F           
4180: 52         LD      D,D             
4181: 4F         LD      C,A             
4182: A7         AND     A               
4183: 4F         LD      C,A             
4184: CC 4F E7   CALL    Z,$E74F         
4187: 4F         LD      C,A             
4188: 0E 50      LD      C,$50           
418A: 6D         LD      L,L             
418B: 50         LD      D,B             
418C: DC 50 2A   CALL    C,$2A50         
418F: 51         LD      D,C             
4190: 5B         LD      E,E             
4191: 51         LD      D,C             
4192: BC         CP      H               
4193: 51         LD      D,C             
4194: E6 51      AND     $51             
4196: F4                              
4197: 51         LD      D,C             
4198: 31 52 6F   LD      SP,$6F52        
419B: 52         LD      D,D             
419C: A6         AND     (HL)            
419D: 52         LD      D,D             
419E: F8 52      LDHL    SP,$52          
41A0: 35         DEC     (HL)            
41A1: 53         LD      D,E             
41A2: 6D         LD      L,L             
41A3: 53         LD      D,E             
41A4: A6         AND     (HL)            
41A5: 53         LD      D,E             
41A6: C3 53 04   JP      $0453           
41A9: 54         LD      D,H             
41AA: 73         LD      (HL),E          
41AB: 54         LD      D,H             
41AC: CE 54      ADC     $54             
41AE: 11 55 55   LD      DE,$5555        
41B1: 55         LD      D,L             
41B2: 88         ADC     A,B             
41B3: 55         LD      D,L             
41B4: AF         XOR     A               
41B5: 55         LD      D,L             
41B6: F0 55      LD      A,($55)         
41B8: 31 56 65   LD      SP,$6556        
41BB: 56         LD      D,(HL)          
41BC: B2         OR      D               
41BD: 56         LD      D,(HL)          
41BE: F9         LD      SP,HL           
41BF: 56         LD      D,(HL)          
41C0: 2B         DEC     HL              
41C1: 57         LD      D,A             
41C2: 4E         LD      C,(HL)          
41C3: 57         LD      D,A             
41C4: 85         ADD     A,L             
41C5: 57         LD      D,A             
41C6: AE         XOR     (HL)            
41C7: 57         LD      D,A             
41C8: DA 57 04   JP      C,$0457         
41CB: 58         LD      E,B             
41CC: 3C         INC     A               
41CD: 58         LD      E,B             
41CE: 78         LD      A,B             
41CF: 58         LD      E,B             
41D0: A8         XOR     B               
41D1: 58         LD      E,B             
41D2: E4                              
41D3: 58         LD      E,B             
41D4: 3D         DEC     A               
41D5: 59         LD      E,C             
41D6: 96         SUB     (HL)            
41D7: 59         LD      E,C             
41D8: BE         CP      (HL)            
41D9: 59         LD      E,C             
41DA: 06 5A      LD      B,$5A           
41DC: 5B         LD      E,E             
41DD: 5A         LD      E,D             
41DE: 93         SUB     E               
41DF: 5A         LD      E,D             
41E0: AF         XOR     A               
41E1: 5A         LD      E,D             
41E2: EC                              
41E3: 5A         LD      E,D             
41E4: 1D         DEC     E               
41E5: 5B         LD      E,E             
41E6: 5E         LD      E,(HL)          
41E7: 5B         LD      E,E             
41E8: 81         ADD     A,C             
41E9: 5B         LD      E,E             
41EA: AB         XOR     E               
41EB: 5B         LD      E,E             
41EC: DF         RST     0X18            
41ED: 5B         LD      E,E             
41EE: 32         LD      (HLD),A         
41EF: 5C         LD      E,H             
41F0: 61         LD      H,C             
41F1: 5C         LD      E,H             
41F2: BB         CP      E               
41F3: 5C         LD      E,H             
41F4: 00         NOP                     
41F5: 5D         LD      E,L             
41F6: 4F         LD      C,A             
41F7: 5D         LD      E,L             
41F8: 7F         LD      A,A             
41F9: 5D         LD      E,L             
41FA: C8         RET     Z               
41FB: 5D         LD      E,L             
41FC: 02         LD      (BC),A          
41FD: 5E         LD      E,(HL)          
41FE: 30 5E      JR      NC,$425E        
4200: 0B         DEC     BC              
4201: E5         PUSH    HL              
4202: 8A         ADC     A,D             
4203: 00         NOP                     
4204: 00         NOP                     
4205: 8A         ADC     A,D             
4206: 10 00      STOP    $00             
4208: 8A         ADC     A,D             
4209: 20 EF      JR      NZ,$41FA        
420B: 10 7C      STOP    $7C             
420D: 11 7D 19   LD      DE,$197D        
4210: 7C         LD      A,H             
4211: 13         INC     DE              
4212: 80         ADD     A,B             
4213: 84         ADD     A,H             
4214: 14         INC     D               
4215: 4D         LD      C,L             
4216: 17         RLA                     
4217: 81         ADD     A,C             
4218: 23         INC     HL              
4219: 37         SCF                     
421A: 83         ADD     A,E             
421B: 24         INC     H               
421C: 0A         LD      A,(BC)          
421D: 27         DAA                     
421E: 38 32      JR      C,$4252         
4220: 1D         DEC     E               
4221: 33         INC     SP              
4222: 2E 34      LD      L,$34           
4224: 48         LD      C,B             
4225: 36 49      LD      (HL),$49        
4227: 37         SCF                     
4228: 4E         LD      C,(HL)          
4229: 38 5D      JR      C,$4288         
422B: 41         LD      B,C             
422C: 1D         DEC     E               
422D: 42         LD      B,D             
422E: 37         SCF                     
422F: 43         LD      B,E             
4230: 39         ADD     HL,SP           
4231: 44         LD      B,H             
4232: E1         POP     HL              
4233: E1         POP     HL              
4234: 07         RLCA                    
4235: 3A         LD      A,(HLD)         
4236: 58         LD      E,B             
4237: 10 82      STOP    $82             
4239: 45         LD      B,L             
423A: 3A         LD      A,(HLD)         
423B: C2 35 E0   JP      NZ,$E035        
423E: 47         LD      B,A             
423F: 3B         DEC     SP              
4240: 48         LD      C,B             
4241: 38 50      JR      C,$4293         
4243: 1D         DEC     E               
4244: C3 51 37   JP      $3751           
4247: C2 52 37   JP      NZ,$3752        
424A: 85         ADD     A,L             
424B: 53         LD      D,E             
424C: 09         ADD     HL,BC           
424D: 82         ADD     A,D             
424E: 58         LD      E,B             
424F: 7A         LD      A,D             
4250: C2 60 37   JP      NZ,$3760        
4253: 85         ADD     A,L             
4254: 63         LD      H,E             
4255: 09         ADD     HL,BC           
4256: 68         LD      L,B             
4257: 38 72      JR      C,$42CB         
4259: 2E 85      LD      L,$85           
425B: 73         LD      (HL),E          
425C: 2F         CPL                     
425D: 78         LD      A,B             
425E: 4E         LD      C,(HL)          
425F: 69         LD      L,C             
4260: 50         LD      D,B             
4261: 79         LD      A,C             
4262: 09         ADD     HL,BC           
4263: FE 0B      CP      $0B             
4265: E5         PUSH    HL              
4266: 8A         ADC     A,D             
4267: 00         NOP                     
4268: 00         NOP                     
4269: 8A         ADC     A,D             
426A: 10 00      STOP    $00             
426C: 8A         ADC     A,D             
426D: 20 EF      JR      NZ,$425E        
426F: 00         NOP                     
4270: 7C         LD      A,H             
4271: 01 7D 03   LD      BC,$037D        
4274: 7C         LD      A,H             
4275: 04         INC     B               
4276: 7D         LD      A,L             
4277: 10 1C      STOP    $1C             
4279: 82         ADD     A,D             
427A: 10 1C      STOP    $1C             
427C: 12         LD      (DE),A          
427D: 7E         LD      A,(HL)          
427E: 82         ADD     A,D             
427F: 13         INC     DE              
4280: 1C         INC     E               
4281: 15         DEC     D               
4282: 7E         LD      A,(HL)          
4283: 16 7D      LD      D,$7D           
4285: 35         DEC     (HL)            
4286: 1D         DEC     E               
4287: 36 50      LD      (HL),$50        
4289: 37         SCF                     
428A: 5D         LD      E,L             
428B: 43         LD      B,E             
428C: 1D         DEC     E               
428D: 86         ADD     A,(HL)          
428E: 44         LD      B,H             
428F: 50         LD      D,B             
4290: 45         LD      B,L             
4291: 37         SCF                     
4292: 46         LD      B,(HL)          
4293: E8 47      ADD     SP,$47          
4295: 38 84      JR      C,$421B         
4297: 50         LD      D,B             
4298: 7A         LD      A,D             
4299: 54         LD      D,H             
429A: 0A         LD      A,(BC)          
429B: 55         LD      D,L             
429C: 33         INC     SP              
429D: 56         LD      D,(HL)          
429E: E0 57      LDFF00  ($57),A         
42A0: 34         INC     (HL)            
42A1: 82         ADD     A,D             
42A2: 58         LD      E,B             
42A3: 03         INC     BC              
42A4: 83         ADD     A,E             
42A5: 60         LD      H,B             
42A6: 50         LD      D,B             
42A7: 63         LD      H,E             
42A8: 37         SCF                     
42A9: 86         ADD     A,(HL)          
42AA: 64         LD      H,H             
42AB: 0A         LD      A,(BC)          
42AC: 83         ADD     A,E             
42AD: 70         LD      (HL),B          
42AE: 09         ADD     HL,BC           
42AF: 73         LD      (HL),E          
42B0: 2E 86      LD      L,$86           
42B2: 74         LD      (HL),H          
42B3: 2F         CPL                     
42B4: FE 0B      CP      $0B             
42B6: E5         PUSH    HL              
42B7: 8A         ADC     A,D             
42B8: 00         NOP                     
42B9: 00         NOP                     
42BA: 8A         ADC     A,D             
42BB: 10 00      STOP    $00             
42BD: 8A         ADC     A,D             
42BE: 20 EF      JR      NZ,$42AF        
42C0: 06 7C      LD      B,$7C           
42C2: 07         RLCA                    
42C3: 7D         LD      A,L             
42C4: 15         DEC     D               
42C5: 7C         LD      A,H             
42C6: 82         ADD     A,D             
42C7: 16 1C      LD      D,$1C           
42C9: 18 7E      JR      $4349           
42CB: 19         ADD     HL,DE           
42CC: 7D         LD      A,L             
42CD: 12         LD      (DE),A          
42CE: 80         ADD     A,B             
42CF: 13         INC     DE              
42D0: 4D         LD      C,L             
42D1: 14         INC     D               
42D2: 81         ADD     A,C             
42D3: 22         LD      (HLI),A         
42D4: 37         SCF                     
42D5: 23         INC     HL              
42D6: 03         INC     BC              
42D7: 24         INC     H               
42D8: 38 31      JR      C,$430B         
42DA: 1D         DEC     E               
42DB: 32         LD      (HLD),A         
42DC: 2E 33      LD      L,$33           
42DE: 2F         CPL                     
42DF: 34         INC     (HL)            
42E0: 4E         LD      C,(HL)          
42E1: 35         DEC     (HL)            
42E2: 5D         LD      E,L             
42E3: 39         ADD     HL,SP           
42E4: 1D         DEC     E               
42E5: 40         LD      B,B             
42E6: 50         LD      D,B             
42E7: 41         LD      B,C             
42E8: 4B         LD      C,E             
42E9: 42         LD      B,D             
42EA: 39         ADD     HL,SP           
42EB: 43         LD      B,E             
42EC: E1         POP     HL              
42ED: E1         POP     HL              
42EE: 07         RLCA                    
42EF: 3D         DEC     A               
42F0: 58         LD      E,B             
42F1: 10 44      STOP    $44             
42F3: 3B         DEC     SP              
42F4: C3 45 38   JP      $3845           
42F7: 49         LD      C,C             
42F8: 37         SCF                     
42F9: 85         ADD     A,L             
42FA: 50         LD      D,B             
42FB: 03         INC     BC              
42FC: 83         ADD     A,E             
42FD: 56         LD      D,(HL)          
42FE: 50         LD      D,B             
42FF: 59         LD      E,C             
4300: 4B         LD      C,E             
4301: 85         ADD     A,L             
4302: 60         LD      H,B             
4303: 03         INC     BC              
4304: 85         ADD     A,L             
4305: 70         LD      (HL),B          
4306: 2F         CPL                     
4307: 75         LD      (HL),L          
4308: 4E         LD      C,(HL)          
4309: 84         ADD     A,H             
430A: 66         LD      H,(HL)          
430B: 03         INC     BC              
430C: 84         ADD     A,H             
430D: 76         HALT                    
430E: 03         INC     BC              
430F: 79         LD      A,C             
4310: 3D         DEC     A               
4311: 42         LD      B,D             
4312: CD 44 D7   CALL    $D744           
4315: FE 0B      CP      $0B             
4317: 03         INC     BC              
4318: 00         NOP                     
4319: 80         ADD     A,B             
431A: 82         ADD     A,D             
431B: 01 4D 03   LD      BC,$034D        
431E: 81         ADD     A,C             
431F: 04         INC     B               
4320: 00         NOP                     
4321: 05         DEC     B               
4322: 80         ADD     A,B             
4323: 82         ADD     A,D             
4324: 06 4D      LD      B,$4D           
4326: 08 81 09   LD      ($0981),SP      
4329: 00         NOP                     
432A: C3 10 37   JP      $3710           
432D: 87         ADD     A,A             
432E: 11 03 87   LD      DE,$8703        
4331: 21 03 87   LD      HL,$8703        
4334: 31 03 13   LD      SP,$1303        
4337: 4C         LD      C,H             
4338: 14         INC     D               
4339: 4D         LD      C,L             
433A: 15         DEC     D               
433B: 4B         LD      C,E             
433C: C3 18 38   JP      $3818           
433F: 40         LD      B,B             
4340: 2E 82      LD      L,$82           
4342: 41         LD      B,C             
4343: 2F         CPL                     
4344: 43         LD      B,E             
4345: 4E         LD      C,(HL)          
4346: 33         INC     SP              
4347: 3D         DEC     A               
4348: 34         INC     (HL)            
4349: 2F         CPL                     
434A: 35         DEC     (HL)            
434B: 3C         INC     A               
434C: 44         LD      B,H             
434D: 3A         LD      A,(HLD)         
434E: 45         LD      B,L             
434F: 2E 82      LD      L,$82           
4351: 46         LD      B,(HL)          
4352: 2F         CPL                     
4353: 48         LD      C,B             
4354: 4E         LD      C,(HL)          
4355: 50         LD      D,B             
4356: 39         ADD     HL,SP           
4357: 82         ADD     A,D             
4358: 51         LD      D,C             
4359: 3A         LD      A,(HLD)         
435A: 53         LD      D,E             
435B: 3B         DEC     SP              
435C: 55         LD      D,L             
435D: 39         ADD     HL,SP           
435E: 82         ADD     A,D             
435F: 56         LD      D,(HL)          
4360: 3A         LD      A,(HLD)         
4361: 58         LD      E,B             
4362: 3B         DEC     SP              
4363: 39         ADD     HL,SP           
4364: 5D         LD      E,L             
4365: C4 49 38   CALL    NZ,$3849        
4368: 69         LD      L,C             
4369: 7A         LD      A,D             
436A: 78         LD      A,B             
436B: 09         ADD     HL,BC           
436C: 19         ADD     HL,DE           
436D: 00         NOP                     
436E: 29         ADD     HL,HL           
436F: EF         RST     0X28            
4370: 66         LD      H,(HL)          
4371: C8         RET     Z               
4372: 8A         ADC     A,D             
4373: 70         LD      (HL),B          
4374: 2F         CPL                     
4375: 72         LD      (HL),D          
4376: 48         LD      C,B             
4377: 73         LD      (HL),E          
4378: 4A         LD      C,D             
4379: 74         LD      (HL),H          
437A: 49         LD      C,C             
437B: 76         HALT                    
437C: 48         LD      C,B             
437D: 77         LD      (HL),A          
437E: 4A         LD      C,D             
437F: 78         LD      A,B             
4380: 49         LD      C,C             
4381: 79         LD      A,C             
4382: 4E         LD      C,(HL)          
4383: 44         LD      B,H             
4384: E1         POP     HL              
4385: E1         POP     HL              
4386: 1F         RRA                     
4387: EE 18      XOR     $18             
4389: 40         LD      B,B             
438A: FE 0B      CP      $0B             
438C: E5         PUSH    HL              
438D: 8A         ADC     A,D             
438E: 00         NOP                     
438F: 00         NOP                     
4390: 8A         ADC     A,D             
4391: 10 00      STOP    $00             
4393: 8A         ADC     A,D             
4394: 20 EF      JR      NZ,$4385        
4396: 06 7C      LD      B,$7C           
4398: 07         RLCA                    
4399: 7D         LD      A,L             
439A: 10 7C      STOP    $7C             
439C: 11 7D 13   LD      DE,$137D        
439F: 7C         LD      A,H             
43A0: 14         INC     D               
43A1: 7D         LD      A,L             
43A2: 15         DEC     D               
43A3: 7C         LD      A,H             
43A4: 82         ADD     A,D             
43A5: 16 1C      LD      D,$1C           
43A7: 18 7E      JR      $4427           
43A9: 19         ADD     HL,DE           
43AA: 7D         LD      A,L             
43AB: 32         LD      (HLD),A         
43AC: 1D         DEC     E               
43AD: 87         ADD     A,A             
43AE: 33         INC     SP              
43AF: 50         LD      D,B             
43B0: C2 42 37   JP      NZ,$3742        
43B3: 87         ADD     A,A             
43B4: 43         LD      B,E             
43B5: 03         INC     BC              
43B6: 87         ADD     A,A             
43B7: 53         LD      D,E             
43B8: 03         INC     BC              
43B9: 87         ADD     A,A             
43BA: 63         LD      H,E             
43BB: 03         INC     BC              
43BC: 45         LD      B,L             
43BD: A0         AND     B               
43BE: 70         LD      (HL),B          
43BF: 1D         DEC     E               
43C0: 71         LD      (HL),C          
43C1: 50         LD      D,B             
43C2: 72         LD      (HL),D          
43C3: 2E 87      LD      L,$87           
43C5: 73         LD      (HL),E          
43C6: 2F         CPL                     
43C7: 76         HALT                    
43C8: 48         LD      C,B             
43C9: 77         LD      (HL),A          
43CA: 4A         LD      C,D             
43CB: 78         LD      A,B             
43CC: 49         LD      C,C             
43CD: 83         ADD     A,E             
43CE: 60         LD      H,B             
43CF: 7A         LD      A,D             
43D0: 66         LD      H,(HL)          
43D1: 20 E1      JR      NZ,$43B4        
43D3: 1F         RRA                     
43D4: E2         LDFF00  (C),A           
43D5: 88         ADC     A,B             
43D6: 50         LD      D,B             
43D7: FE 0B      CP      $0B             
43D9: 03         INC     BC              
43DA: 8A         ADC     A,D             
43DB: 00         NOP                     
43DC: 00         NOP                     
43DD: 8A         ADC     A,D             
43DE: 10 00      STOP    $00             
43E0: 8A         ADC     A,D             
43E1: 20 EF      JR      NZ,$43D2        
43E3: 13         INC     DE              
43E4: 7C         LD      A,H             
43E5: 04         INC     B               
43E6: 7C         LD      A,H             
43E7: 05         DEC     B               
43E8: 7D         LD      A,L             
43E9: 16 7E      LD      D,$7E           
43EB: 17         RLA                     
43EC: 7D         LD      A,L             
43ED: 82         ADD     A,D             
43EE: 14         INC     D               
43EF: 1C         INC     E               
43F0: 87         ADD     A,A             
43F1: 30 50      JR      NC,$4443        
43F3: 37         SCF                     
43F4: 5D         LD      E,L             
43F5: 82         ADD     A,D             
43F6: 38 E5      JR      C,$43DD         
43F8: 41         LD      B,C             
43F9: 09         ADD     HL,BC           
43FA: C3 47 38   JP      $3847           
43FD: C4 48 E5   CALL    NZ,$E548        
4400: C4 49 E5   CALL    NZ,$E549        
4403: 63         LD      H,E             
4404: 09         ADD     HL,BC           
4405: 87         ADD     A,A             
4406: 70         LD      (HL),B          
4407: 2F         CPL                     
4408: 73         LD      (HL),E          
4409: 48         LD      C,B             
440A: 74         LD      (HL),H          
440B: E0 75      LDFF00  ($75),A         
440D: 49         LD      C,C             
440E: 77         LD      (HL),A          
440F: 4E         LD      C,(HL)          
4410: 78         LD      A,B             
4411: 50         LD      D,B             
4412: 79         LD      A,C             
4413: 5D         LD      E,L             
4414: 43         LD      B,E             
4415: 20 46      JR      NZ,$445D        
4417: 20 51      JR      NZ,$446A        
4419: 20 54      JR      NZ,$446F        
441B: 20 65      JR      NZ,$4482        
441D: 20 FE      JR      NZ,$441D        
441F: 0B         DEC     BC              
4420: E5         PUSH    HL              
4421: 35         DEC     (HL)            
4422: E1         POP     HL              
4423: 8A         ADC     A,D             
4424: 00         NOP                     
4425: 00         NOP                     
4426: 8A         ADC     A,D             
4427: 10 00      STOP    $00             
4429: 8A         ADC     A,D             
442A: 20 EF      JR      NZ,$441B        
442C: 04         INC     B               
442D: 05         DEC     B               
442E: 05         DEC     B               
442F: 06 06      LD      B,$06           
4431: 07         RLCA                    
4432: 14         INC     D               
4433: 63         LD      H,E             
4434: 15         DEC     D               
4435: 64         LD      H,H             
4436: 16 65      LD      D,$65           
4438: 24         INC     H               
4439: 71         LD      (HL),C          
443A: 25         DEC     H               
443B: 1C         INC     E               
443C: 26 7F      LD      H,$7F           
443E: 34         INC     (HL)            
443F: A9         XOR     C               
4440: 35         DEC     (HL)            
4441: AA         XOR     D               
4442: 36 BF      LD      (HL),$BF        
4444: 10 7C      STOP    $7C             
4446: 11 7D 18   LD      DE,$187D        
4449: 7C         LD      A,H             
444A: 19         ADD     HL,DE           
444B: 7D         LD      A,L             
444C: 13         INC     DE              
444D: 80         ADD     A,B             
444E: 17         RLA                     
444F: 81         ADD     A,C             
4450: C2 23 37   JP      NZ,$3723        
4453: C2 27 38   JP      NZ,$3827        
4456: 32         LD      (HLD),A         
4457: 1D         DEC     E               
4458: 38 5D      JR      C,$44B7         
445A: C2 42 37   JP      NZ,$3742        
445D: C2 48 38   JP      NZ,$3848        
4460: 43         LD      B,E             
4461: 2E 44      LD      L,$44           
4463: 48         LD      C,B             
4464: 46         LD      B,(HL)          
4465: 49         LD      C,C             
4466: 47         LD      B,A             
4467: 4E         LD      C,(HL)          
4468: C2 48 38   JP      NZ,$3848        
446B: 53         LD      D,E             
446C: 3E 83      LD      A,$83           
446E: 54         LD      D,H             
446F: 3A         LD      A,(HLD)         
4470: 57         LD      D,A             
4471: 3F         CCF                     
4472: 61         LD      H,C             
4473: 1D         DEC     E               
4474: 62         LD      H,D             
4475: 2E 63      LD      L,$63           
4477: 2F         CPL                     
4478: 64         LD      H,H             
4479: 48         LD      C,B             
447A: 66         LD      H,(HL)          
447B: 49         LD      C,C             
447C: 67         LD      H,A             
447D: 2F         CPL                     
447E: 68         LD      L,B             
447F: 4E         LD      C,(HL)          
4480: 69         LD      L,C             
4481: 5D         LD      E,L             
4482: 71         LD      (HL),C          
4483: 37         SCF                     
4484: 72         LD      (HL),D          
4485: 3E 85      LD      A,$85           
4487: 73         LD      (HL),E          
4488: 3A         LD      A,(HLD)         
4489: 78         LD      A,B             
448A: 3B         DEC     SP              
448B: 79         LD      A,C             
448C: 38 C4      JR      C,$4452         
448E: 45         LD      B,L             
448F: E0 E1      LDFF00  ($E1),A         
4491: 08 70 50   LD      ($5070),SP      
4494: 7C         LD      A,H             
4495: FE 0B      CP      $0B             
4497: E5         PUSH    HL              
4498: 8A         ADC     A,D             
4499: 00         NOP                     
449A: 00         NOP                     
449B: 8A         ADC     A,D             
449C: 10 00      STOP    $00             
449E: 8A         ADC     A,D             
449F: 20 EF      JR      NZ,$4490        
44A1: 04         INC     B               
44A2: 05         DEC     B               
44A3: 05         DEC     B               
44A4: 06 06      LD      B,$06           
44A6: 07         RLCA                    
44A7: 14         INC     D               
44A8: 63         LD      H,E             
44A9: 15         DEC     D               
44AA: 64         LD      H,H             
44AB: 16 65      LD      D,$65           
44AD: 24         INC     H               
44AE: 71         LD      (HL),C          
44AF: 25         DEC     H               
44B0: 1C         INC     E               
44B1: 26 7F      LD      H,$7F           
44B3: 34         INC     (HL)            
44B4: A9         XOR     C               
44B5: 35         DEC     (HL)            
44B6: AA         XOR     D               
44B7: 36 BF      LD      (HL),$BF        
44B9: 10 7C      STOP    $7C             
44BB: 11 7D 18   LD      DE,$187D        
44BE: 7C         LD      A,H             
44BF: 19         ADD     HL,DE           
44C0: 7D         LD      A,L             
44C1: 13         INC     DE              
44C2: 80         ADD     A,B             
44C3: 17         RLA                     
44C4: 81         ADD     A,C             
44C5: C2 23 37   JP      NZ,$3723        
44C8: C2 27 38   JP      NZ,$3827        
44CB: 32         LD      (HLD),A         
44CC: 1D         DEC     E               
44CD: 38 5D      JR      C,$452C         
44CF: C2 42 37   JP      NZ,$3742        
44D2: C2 48 38   JP      NZ,$3848        
44D5: 43         LD      B,E             
44D6: 2E 44      LD      L,$44           
44D8: 48         LD      C,B             
44D9: 46         LD      B,(HL)          
44DA: 49         LD      C,C             
44DB: 47         LD      B,A             
44DC: 4E         LD      C,(HL)          
44DD: C2 48 38   JP      NZ,$3848        
44E0: 53         LD      D,E             
44E1: 3E 83      LD      A,$83           
44E3: 54         LD      D,H             
44E4: 3A         LD      A,(HLD)         
44E5: 57         LD      D,A             
44E6: 3F         CCF                     
44E7: 61         LD      H,C             
44E8: 1D         DEC     E               
44E9: 62         LD      H,D             
44EA: 2E 63      LD      L,$63           
44EC: 2F         CPL                     
44ED: 64         LD      H,H             
44EE: 48         LD      C,B             
44EF: 66         LD      H,(HL)          
44F0: 49         LD      C,C             
44F1: 67         LD      H,A             
44F2: 2F         CPL                     
44F3: 68         LD      L,B             
44F4: 4E         LD      C,(HL)          
44F5: 69         LD      L,C             
44F6: 5D         LD      E,L             
44F7: 71         LD      (HL),C          
44F8: 37         SCF                     
44F9: 72         LD      (HL),D          
44FA: 3E 85      LD      A,$85           
44FC: 73         LD      (HL),E          
44FD: 3A         LD      A,(HLD)         
44FE: 78         LD      A,B             
44FF: 3B         DEC     SP              
4500: 79         LD      A,C             
4501: 38 C4      JR      C,$44C7         
4503: 45         LD      B,L             
4504: E0 25      LDFF00  ($25),A         
4506: C1         POP     BC              
4507: 35         DEC     (HL)            
4508: CB E1      SET     1,E             
450A: 08 70 50   LD      ($5070),SP      
450D: 7C         LD      A,H             
450E: FE 0B      CP      $0B             
4510: E5         PUSH    HL              
4511: 8A         ADC     A,D             
4512: 00         NOP                     
4513: 00         NOP                     
4514: 8A         ADC     A,D             
4515: 10 00      STOP    $00             
4517: 85         ADD     A,L             
4518: 20 EF      JR      NZ,$4509        
451A: 10 7C      STOP    $7C             
451C: 11 7D 13   LD      DE,$137D        
451F: 80         ADD     A,B             
4520: 85         ADD     A,L             
4521: 14         INC     D               
4522: 4D         LD      C,L             
4523: 19         ADD     HL,DE           
4524: 81         ADD     A,C             
4525: 23         INC     HL              
4526: 37         SCF                     
4527: 85         ADD     A,L             
4528: 24         INC     H               
4529: 03         INC     BC              
452A: 25         DEC     H               
452B: 09         ADD     HL,BC           
452C: 29         ADD     HL,HL           
452D: 38 32      JR      C,$4561         
452F: 1D         DEC     E               
4530: 33         INC     SP              
4531: 4B         LD      C,E             
4532: 85         ADD     A,L             
4533: 34         INC     (HL)            
4534: 03         INC     BC              
4535: 39         ADD     HL,SP           
4536: 7A         LD      A,D             
4537: C3 42 37   JP      $3742           
453A: 43         LD      B,E             
453B: D3                              
453C: E1         POP     HL              
453D: 0A         LD      A,(BC)          
453E: EE 78      XOR     $78             
4540: 30 C3      JR      NC,$4505        
4542: 44         LD      B,H             
4543: 03         INC     BC              
4544: 45         LD      B,L             
4545: 3D         DEC     A               
4546: 46         LD      B,(HL)          
4547: 48         LD      C,B             
4548: 47         LD      B,A             
4549: 4A         LD      C,D             
454A: 48         LD      C,B             
454B: 49         LD      C,C             
454C: 49         LD      C,C             
454D: 4E         LD      C,(HL)          
454E: 53         LD      D,E             
454F: 03         INC     BC              
4550: C2 55 38   JP      NZ,$3855        
4553: 83         ADD     A,E             
4554: 56         LD      D,(HL)          
4555: 3A         LD      A,(HLD)         
4556: 59         LD      E,C             
4557: 3B         DEC     SP              
4558: 63         LD      H,E             
4559: 09         ADD     HL,BC           
455A: 84         ADD     A,H             
455B: 66         LD      H,(HL)          
455C: 03         INC     BC              
455D: 72         LD      (HL),D          
455E: 2E 82      LD      L,$82           
4560: 73         LD      (HL),E          
4561: 2F         CPL                     
4562: 75         LD      (HL),L          
4563: 4E         LD      C,(HL)          
4564: 76         HALT                    
4565: E0 77      LDFF00  ($77),A         
4567: 3C         INC     A               
4568: 82         ADD     A,D             
4569: 78         LD      A,B             
456A: 03         INC     BC              
456B: FE 0B      CP      $0B             
456D: E5         PUSH    HL              
456E: 8A         ADC     A,D             
456F: 00         NOP                     
4570: 00         NOP                     
4571: 8A         ADC     A,D             
4572: 10 00      STOP    $00             
4574: 8A         ADC     A,D             
4575: 20 EF      JR      NZ,$4566        
4577: 12         LD      (DE),A          
4578: 7C         LD      A,H             
4579: 13         INC     DE              
457A: 7D         LD      A,L             
457B: 18 7C      JR      $45F9           
457D: 19         ADD     HL,DE           
457E: 7D         LD      A,L             
457F: 20 C8      JR      NZ,$4549        
4581: 82         ADD     A,D             
4582: 21 7A 24   LD      HL,$247A        
4585: 7A         LD      A,D             
4586: 82         ADD     A,D             
4587: 28 7A      JR      Z,$4603         
4589: 83         ADD     A,E             
458A: 30 7A      JR      NC,$4606        
458C: 86         ADD     A,(HL)          
458D: 33         INC     SP              
458E: 7B         LD      A,E             
458F: 34         INC     (HL)            
4590: 7A         LD      A,D             
4591: 82         ADD     A,D             
4592: 38 7A      JR      C,$460E         
4594: 29         ADD     HL,HL           
4595: C8         RET     Z               
4596: 82         ADD     A,D             
4597: 50         LD      D,B             
4598: 50         LD      D,B             
4599: 52         LD      D,D             
459A: 5D         LD      E,L             
459B: 82         ADD     A,D             
459C: 60         LD      H,B             
459D: 03         INC     BC              
459E: C2 62 38   JP      NZ,$3862        
45A1: 82         ADD     A,D             
45A2: 70         LD      (HL),B          
45A3: 03         INC     BC              
45A4: 71         LD      (HL),C          
45A5: 09         ADD     HL,BC           
45A6: 54         LD      D,H             
45A7: 1D         DEC     E               
45A8: 85         ADD     A,L             
45A9: 55         LD      D,L             
45AA: 50         LD      D,B             
45AB: 64         LD      H,H             
45AC: 37         SCF                     
45AD: 85         ADD     A,L             
45AE: 65         LD      H,L             
45AF: 03         INC     BC              
45B0: 73         LD      (HL),E          
45B1: 1D         DEC     E               
45B2: 74         LD      (HL),H          
45B3: 2E 85      LD      L,$85           
45B5: 75         LD      (HL),L          
45B6: 2F         CPL                     
45B7: FE 0B      CP      $0B             
45B9: 03         INC     BC              
45BA: 8A         ADC     A,D             
45BB: 00         NOP                     
45BC: 00         NOP                     
45BD: 8A         ADC     A,D             
45BE: 10 00      STOP    $00             
45C0: 8A         ADC     A,D             
45C1: 20 EF      JR      NZ,$45B2        
45C3: 83         ADD     A,E             
45C4: 20 78      JR      NZ,$463E        
45C6: 83         ADD     A,E             
45C7: 30 79      JR      NC,$4642        
45C9: 84         ADD     A,H             
45CA: 33         INC     SP              
45CB: 7B         LD      A,E             
45CC: 84         ADD     A,H             
45CD: 40         LD      B,B             
45CE: E5         PUSH    HL              
45CF: 44         LD      B,H             
45D0: 1D         DEC     E               
45D1: 85         ADD     A,L             
45D2: 45         LD      B,L             
45D3: 50         LD      D,B             
45D4: 84         ADD     A,H             
45D5: 50         LD      D,B             
45D6: 50         LD      D,B             
45D7: 54         LD      D,H             
45D8: 4B         LD      C,E             
45D9: 84         ADD     A,H             
45DA: 70         LD      (HL),B          
45DB: 2F         CPL                     
45DC: 73         LD      (HL),E          
45DD: 3C         INC     A               
45DE: 66         LD      H,(HL)          
45DF: 09         ADD     HL,BC           
45E0: 02         LD      (BC),A          
45E1: 7C         LD      A,H             
45E2: 03         INC     BC              
45E3: 7D         LD      A,L             
45E4: 11 7C 82   LD      DE,$827C        
45E7: 12         LD      (DE),A          
45E8: 1C         INC     E               
45E9: 14         INC     D               
45EA: 7E         LD      A,(HL)          
45EB: 15         DEC     D               
45EC: 7D         LD      A,L             
45ED: 18 80      JR      $456F           
45EF: 19         ADD     HL,DE           
45F0: 4D         LD      C,L             
45F1: 82         ADD     A,D             
45F2: 27         DAA                     
45F3: 78         LD      A,B             
45F4: 82         ADD     A,D             
45F5: 37         SCF                     
45F6: 79         LD      A,C             
45F7: C2 29 03   JP      NZ,$0329        
45FA: 48         LD      C,B             
45FB: 2E 49      LD      L,$49           
45FD: 2F         CPL                     
45FE: 58         LD      E,B             
45FF: 3E C2      LD      A,$C2           
4601: 59         LD      E,C             
4602: 3A         LD      A,(HLD)         
4603: 68         LD      L,B             
4604: 39         ADD     HL,SP           
4605: 70         LD      (HL),B          
4606: 48         LD      C,B             
4607: 71         LD      (HL),C          
4608: 4A         LD      C,D             
4609: 72         LD      (HL),D          
460A: 49         LD      C,C             
460B: 20 C8      JR      NZ,$45D5        
460D: 38 C8      JR      C,$45D7         
460F: FE 0B      CP      $0B             
4611: 03         INC     BC              
4612: 8A         ADC     A,D             
4613: 00         NOP                     
4614: 4D         LD      C,L             
4615: 8A         ADC     A,D             
4616: 40         LD      B,B             
4617: 2F         CPL                     
4618: 43         LD      B,E             
4619: 48         LD      C,B             
461A: 44         LD      B,H             
461B: 4A         LD      C,D             
461C: 45         LD      B,L             
461D: 49         LD      C,C             
461E: 46         LD      B,(HL)          
461F: 3C         INC     A               
4620: 47         LD      B,A             
4621: 03         INC     BC              
4622: 48         LD      C,B             
4623: 3D         DEC     A               
4624: 8A         ADC     A,D             
4625: 50         LD      D,B             
4626: 3A         LD      A,(HLD)         
4627: 82         ADD     A,D             
4628: 60         LD      H,B             
4629: 3A         LD      A,(HLD)         
462A: 8A         ADC     A,D             
462B: 70         LD      (HL),B          
462C: 03         INC     BC              
462D: C2 62 37   JP      NZ,$3762        
4630: 56         LD      D,(HL)          
4631: 2E 57      LD      L,$57           
4633: 2F         CPL                     
4634: 58         LD      E,B             
4635: 4E         LD      C,(HL)          
4636: 61         LD      H,C             
4637: E1         POP     HL              
4638: E1         POP     HL              
4639: 0A         LD      A,(BC)          
463A: 8B         ADC     A,E             
463B: 50         LD      D,B             
463C: 7C         LD      A,H             
463D: 66         LD      H,(HL)          
463E: 39         ADD     HL,SP           
463F: 67         LD      H,A             
4640: E1         POP     HL              
4641: E1         POP     HL              
4642: 0A         LD      A,(BC)          
4643: 7E         LD      A,(HL)          
4644: 60         LD      H,B             
4645: 7C         LD      A,H             
4646: 68         LD      L,B             
4647: 3B         DEC     SP              
4648: 03         INC     BC              
4649: FD                              
464A: E1         POP     HL              
464B: 10 9F      STOP    $9F             
464D: 50         LD      D,B             
464E: 7C         LD      A,H             
464F: 12         LD      (DE),A          
4650: 09         ADD     HL,BC           
4651: 16 09      LD      D,$09           
4653: 23         INC     HL              
4654: 09         ADD     HL,BC           
4655: 38 09      JR      C,$4660         
4657: C2 44 E0   JP      NZ,$E044        
465A: 62         LD      H,D             
465B: DE 00      SBC     $00             
465D: 80         ADD     A,B             
465E: 10 4B      STOP    $4B             
4660: FE 0B      CP      $0B             
4662: 03         INC     BC              
4663: 83         ADD     A,E             
4664: 00         NOP                     
4665: 4D         LD      C,L             
4666: 03         INC     BC              
4667: 81         ADD     A,C             
4668: 13         INC     DE              
4669: 4C         LD      C,H             
466A: 14         INC     D               
466B: 4D         LD      C,L             
466C: 15         DEC     D               
466D: 81         ADD     A,C             
466E: 85         ADD     A,L             
466F: 40         LD      B,B             
4670: 2F         CPL                     
4671: 45         LD      B,L             
4672: 4E         LD      C,(HL)          
4673: 85         ADD     A,L             
4674: 35         DEC     (HL)            
4675: 7A         LD      A,D             
4676: 37         SCF                     
4677: 7B         LD      A,E             
4678: 85         ADD     A,L             
4679: 50         LD      D,B             
467A: 3A         LD      A,(HLD)         
467B: 87         ADD     A,A             
467C: 70         LD      (HL),B          
467D: 03         INC     BC              
467E: 55         LD      D,L             
467F: 3F         CCF                     
4680: 46         LD      B,(HL)          
4681: 50         LD      D,B             
4682: 47         LD      B,A             
4683: 5D         LD      E,L             
4684: 82         ADD     A,D             
4685: 48         LD      C,B             
4686: E5         PUSH    HL              
4687: 82         ADD     A,D             
4688: 74         LD      (HL),H          
4689: 09         ADD     HL,BC           
468A: 66         LD      H,(HL)          
468B: 09         ADD     HL,BC           
468C: 83         ADD     A,E             
468D: 57         LD      D,A             
468E: 78         LD      A,B             
468F: 83         ADD     A,E             
4690: 67         LD      H,A             
4691: 79         LD      A,C             
4692: 86         ADD     A,(HL)          
4693: 04         INC     B               
4694: 00         NOP                     
4695: 84         ADD     A,H             
4696: 16 00      LD      D,$00           
4698: 16 7C      LD      D,$7C           
469A: 17         RLA                     
469B: 7D         LD      A,L             
469C: 84         ADD     A,H             
469D: 26 EF      LD      H,$EF           
469F: 77         LD      (HL),A          
46A0: 38 82      JR      C,$4624         
46A2: 78         LD      A,B             
46A3: E5         PUSH    HL              
46A4: 56         LD      D,(HL)          
46A5: 03         INC     BC              
46A6: 25         DEC     H               
46A7: 38 55      JR      C,$46FE         
46A9: 3B         DEC     SP              
46AA: FE 0B      CP      $0B             
46AC: E5         PUSH    HL              
46AD: 8A         ADC     A,D             
46AE: 00         NOP                     
46AF: 00         NOP                     
46B0: 10 00      STOP    $00             
46B2: 11 7C 12   LD      DE,$127C        
46B5: 7D         LD      A,L             
46B6: 13         INC     DE              
46B7: 00         NOP                     
46B8: 14         INC     D               
46B9: 7C         LD      A,H             
46BA: 15         DEC     D               
46BB: 7D         LD      A,L             
46BC: 16 80      LD      D,$80           
46BE: 82         ADD     A,D             
46BF: 17         RLA                     
46C0: 4D         LD      C,L             
46C1: 19         ADD     HL,DE           
46C2: 81         ADD     A,C             
46C3: 20 EF      JR      NZ,$46B4        
46C5: 82         ADD     A,D             
46C6: 21 78 84   LD      HL,$8478        
46C9: 23         INC     HL              
46CA: 7A         LD      A,D             
46CB: 82         ADD     A,D             
46CC: 27         DAA                     
46CD: 20 C2      JR      NZ,$4691        
46CF: 29         ADD     HL,HL           
46D0: 38 30      JR      C,$4702         
46D2: 7A         LD      A,D             
46D3: 82         ADD     A,D             
46D4: 31 79 35   LD      SP,$3579        
46D7: 1D         DEC     E               
46D8: 36 4B      LD      (HL),$4B        
46DA: 37         SCF                     
46DB: 03         INC     BC              
46DC: 38 03      JR      C,$46E1         
46DE: 41         LD      B,C             
46DF: 1D         DEC     E               
46E0: 82         ADD     A,D             
46E1: 42         LD      B,D             
46E2: 50         LD      D,B             
46E3: 44         LD      B,H             
46E4: 5D         LD      E,L             
46E5: C2 45 37   JP      NZ,$3745        
46E8: 82         ADD     A,D             
46E9: 46         LD      B,(HL)          
46EA: 03         INC     BC              
46EB: 48         LD      C,B             
46EC: 3D         DEC     A               
46ED: 49         LD      C,C             
46EE: 4E         LD      C,(HL)          
46EF: 82         ADD     A,D             
46F0: 50         LD      D,B             
46F1: 78         LD      A,B             
46F2: 82         ADD     A,D             
46F3: 52         LD      D,D             
46F4: 03         INC     BC              
46F5: C2 54 38   JP      NZ,$3854        
46F8: 82         ADD     A,D             
46F9: 56         LD      D,(HL)          
46FA: 03         INC     BC              
46FB: 82         ADD     A,D             
46FC: 48         LD      C,B             
46FD: 7A         LD      A,D             
46FE: 58         LD      E,B             
46FF: 38 59      JR      C,$475A         
4701: 3F         CCF                     
4702: 82         ADD     A,D             
4703: 60         LD      H,B             
4704: 79         LD      A,C             
4705: 82         ADD     A,D             
4706: 62         LD      H,D             
4707: 03         INC     BC              
4708: 65         LD      H,L             
4709: 2E 82      LD      L,$82           
470B: 66         LD      H,(HL)          
470C: 2F         CPL                     
470D: 68         LD      L,B             
470E: 4E         LD      C,(HL)          
470F: 69         LD      L,C             
4710: 3F         CCF                     
4711: 71         LD      (HL),C          
4712: 2E 82      LD      L,$82           
4714: 72         LD      (HL),D          
4715: 2F         CPL                     
4716: 74         LD      (HL),H          
4717: 4E         LD      C,(HL)          
4718: 75         LD      (HL),L          
4719: 3E 76      LD      A,$76           
471B: E1         POP     HL              
471C: 77         LD      (HL),A          
471D: 3A         LD      A,(HLD)         
471E: 82         ADD     A,D             
471F: 78         LD      A,B             
4720: 3F         CCF                     
4721: 73         LD      (HL),E          
4722: E0 FE      LDFF00  ($FE),A         
4724: 0B         DEC     BC              
4725: E5         PUSH    HL              
4726: 8A         ADC     A,D             
4727: 00         NOP                     
4728: 00         NOP                     
4729: 8A         ADC     A,D             
472A: 10 00      STOP    $00             
472C: 16 7C      LD      D,$7C           
472E: 82         ADD     A,D             
472F: 17         RLA                     
4730: 1C         INC     E               
4731: 19         ADD     HL,DE           
4732: 7D         LD      A,L             
4733: 07         RLCA                    
4734: 7C         LD      A,H             
4735: 08 7D 8A   LD      ($8A7D),SP      
4738: 20 EF      JR      NZ,$4729        
473A: 10 80      STOP    $80             
473C: 83         ADD     A,E             
473D: 11 4D 14   LD      DE,$144D        
4740: 81         ADD     A,C             
4741: 82         ADD     A,D             
4742: 36 50      LD      (HL),$50        
4744: 38 5D      JR      C,$47A3         
4746: 30 3E      JR      NC,$4786        
4748: 83         ADD     A,E             
4749: 31 3A 34   LD      SP,$343A        
474C: 3F         CCF                     
474D: 20 2E      JR      NZ,$477D        
474F: 83         ADD     A,E             
4750: 21 2F 24   LD      HL,$242F        
4753: 4E         LD      C,(HL)          
4754: 35         DEC     (HL)            
4755: 1D         DEC     E               
4756: 82         ADD     A,D             
4757: 46         LD      B,(HL)          
4758: 03         INC     BC              
4759: C2 48 38   JP      NZ,$3848        
475C: 86         ADD     A,(HL)          
475D: 40         LD      B,B             
475E: 7A         LD      A,D             
475F: 82         ADD     A,D             
4760: 56         LD      D,(HL)          
4761: 03         INC     BC              
4762: 50         LD      D,B             
4763: 3E 83      LD      A,$83           
4765: 51         LD      D,C             
4766: 3A         LD      A,(HLD)         
4767: 54         LD      D,H             
4768: 3F         CCF                     
4769: 55         LD      D,L             
476A: 37         SCF                     
476B: 60         LD      H,B             
476C: 3E 83      LD      A,$83           
476E: 61         LD      H,C             
476F: 3A         LD      A,(HLD)         
4770: 64         LD      H,H             
4771: 3F         CCF                     
4772: 65         LD      H,L             
4773: 2E 82      LD      L,$82           
4775: 66         LD      H,(HL)          
4776: 2F         CPL                     
4777: 68         LD      L,B             
4778: 4E         LD      C,(HL)          
4779: 70         LD      (HL),B          
477A: 37         SCF                     
477B: 83         ADD     A,E             
477C: 71         LD      (HL),C          
477D: 03         INC     BC              
477E: 74         LD      (HL),H          
477F: 38 75      JR      C,$47F6         
4781: 3E 82      LD      A,$82           
4783: 76         HALT                    
4784: 3A         LD      A,(HLD)         
4785: 78         LD      A,B             
4786: 3F         CCF                     
4787: 61         LD      H,C             
4788: E1         POP     HL              
4789: E1         POP     HL              
478A: 0A         LD      A,(BC)          
478B: F2                              
478C: 50         LD      D,B             
478D: 7C         LD      A,H             
478E: FE 0B      CP      $0B             
4790: 03         INC     BC              
4791: 25         DEC     H               
4792: E1         POP     HL              
4793: 8A         ADC     A,D             
4794: 00         NOP                     
4795: 00         NOP                     
4796: 8A         ADC     A,D             
4797: 10 00      STOP    $00             
4799: 10 7C      STOP    $7C             
479B: 11 7E 12   LD      DE,$127E        
479E: 7D         LD      A,L             
479F: 18 7C      JR      $481D           
47A1: 19         ADD     HL,DE           
47A2: 7D         LD      A,L             
47A3: 8A         ADC     A,D             
47A4: 20 EF      JR      NZ,$4795        
47A6: 30 1D      JR      NC,$47C5        
47A8: 89         ADC     A,C             
47A9: 31 50 C2   LD      SP,$C250        
47AC: 40         LD      B,B             
47AD: 37         SCF                     
47AE: 60         LD      H,B             
47AF: 2E 61      LD      L,$61           
47B1: 3C         INC     A               
47B2: 70         LD      (HL),B          
47B3: 3E 71      LD      A,$71           
47B5: 2E 82      LD      L,$82           
47B7: 72         LD      (HL),D          
47B8: 2F         CPL                     
47B9: 74         LD      (HL),H          
47BA: 48         LD      C,B             
47BB: 75         LD      (HL),L          
47BC: 4A         LD      C,D             
47BD: 76         HALT                    
47BE: 49         LD      C,C             
47BF: 77         LD      (HL),A          
47C0: 48         LD      C,B             
47C1: 78         LD      A,B             
47C2: 4A         LD      C,D             
47C3: 79         LD      A,C             
47C4: 49         LD      C,C             
47C5: 41         LD      B,C             
47C6: 54         LD      D,H             
47C7: 42         LD      B,D             
47C8: 20 51      JR      NZ,$481B        
47CA: 20 56      JR      NZ,$4822        
47CC: 09         ADD     HL,BC           
47CD: 59         LD      E,C             
47CE: 09         ADD     HL,BC           
47CF: 63         LD      H,E             
47D0: 09         ADD     HL,BC           
47D1: C4 03 72   CALL    NZ,$7203        
47D4: 43         LD      B,E             
47D5: B6         OR      (HL)            
47D6: C5         PUSH    BC              
47D7: 04         INC     B               
47D8: 74         LD      (HL),H          
47D9: C5         PUSH    BC              
47DA: 05         DEC     B               
47DB: 74         LD      (HL),H          
47DC: C5         PUSH    BC              
47DD: 06 74      LD      B,$74           
47DF: C4 07 73   CALL    NZ,$7307        
47E2: 47         LD      B,A             
47E3: B7         OR      A               
47E4: 14         INC     D               
47E5: 75         LD      (HL),L          
47E6: 15         DEC     D               
47E7: D6 16      SUB     $16             
47E9: 76         HALT                    
47EA: E1         POP     HL              
47EB: 06 0E      LD      B,$0E           
47ED: 50         LD      D,B             
47EE: 7C         LD      A,H             
47EF: FE 0B      CP      $0B             
47F1: 03         INC     BC              
47F2: 8A         ADC     A,D             
47F3: 00         NOP                     
47F4: 00         NOP                     
47F5: 8A         ADC     A,D             
47F6: 10 00      STOP    $00             
47F8: 10 7C      STOP    $7C             
47FA: 11 7E 12   LD      DE,$127E        
47FD: 7D         LD      A,L             
47FE: 18 7C      JR      $487C           
4800: 19         ADD     HL,DE           
4801: 7D         LD      A,L             
4802: 8A         ADC     A,D             
4803: 20 EF      JR      NZ,$47F4        
4805: 30 1D      JR      NC,$4824        
4807: 89         ADC     A,C             
4808: 31 50 C2   LD      SP,$C250        
480B: 40         LD      B,B             
480C: 37         SCF                     
480D: 60         LD      H,B             
480E: 2E 61      LD      L,$61           
4810: 3C         INC     A               
4811: 70         LD      (HL),B          
4812: 3E 71      LD      A,$71           
4814: 2E 82      LD      L,$82           
4816: 72         LD      (HL),D          
4817: 2F         CPL                     
4818: 74         LD      (HL),H          
4819: 48         LD      C,B             
481A: 75         LD      (HL),L          
481B: 4A         LD      C,D             
481C: 76         HALT                    
481D: 49         LD      C,C             
481E: 77         LD      (HL),A          
481F: 48         LD      C,B             
4820: 78         LD      A,B             
4821: 4A         LD      C,D             
4822: 79         LD      A,C             
4823: 49         LD      C,C             
4824: 41         LD      B,C             
4825: 54         LD      D,H             
4826: 42         LD      B,D             
4827: 20 51      JR      NZ,$487A        
4829: 20 56      JR      NZ,$4881        
482B: 09         ADD     HL,BC           
482C: 59         LD      E,C             
482D: 09         ADD     HL,BC           
482E: 63         LD      H,E             
482F: 09         ADD     HL,BC           
4830: C4 03 72   CALL    NZ,$7203        
4833: 43         LD      B,E             
4834: B6         OR      (HL)            
4835: C5         PUSH    BC              
4836: 04         INC     B               
4837: 74         LD      (HL),H          
4838: C5         PUSH    BC              
4839: 05         DEC     B               
483A: 74         LD      (HL),H          
483B: C5         PUSH    BC              
483C: 06 74      LD      B,$74           
483E: C4 07 73   CALL    NZ,$7307        
4841: 47         LD      B,A             
4842: B7         OR      A               
4843: 14         INC     D               
4844: 75         LD      (HL),L          
4845: 15         DEC     D               
4846: D6 16      SUB     $16             
4848: 76         HALT                    
4849: C2 35 77   JP      NZ,$7735        
484C: 25         DEC     H               
484D: E1         POP     HL              
484E: E1         POP     HL              
484F: 06 0E      LD      B,$0E           
4851: 50         LD      D,B             
4852: 7C         LD      A,H             
4853: FE 0B      CP      $0B             
4855: E5         PUSH    HL              
4856: 8A         ADC     A,D             
4857: 00         NOP                     
4858: 00         NOP                     
4859: 8A         ADC     A,D             
485A: 10 00      STOP    $00             
485C: 06 7C      LD      B,$7C           
485E: 07         RLCA                    
485F: 7D         LD      A,L             
4860: 10 7C      STOP    $7C             
4862: 11 7D 15   LD      DE,$157D        
4865: 7E         LD      A,(HL)          
4866: 82         ADD     A,D             
4867: 16 1C      LD      D,$1C           
4869: 14         INC     D               
486A: 7C         LD      A,H             
486B: 18 7D      JR      $48EA           
486D: 8A         ADC     A,D             
486E: 20 EF      JR      NZ,$485F        
4870: 88         ADC     A,B             
4871: 30 50      JR      NC,$48C3        
4873: 38 5D      JR      C,$48D2         
4875: 88         ADC     A,B             
4876: 40         LD      B,B             
4877: 03         INC     BC              
4878: C2 48 38   JP      NZ,$3848        
487B: 41         LD      B,C             
487C: 09         ADD     HL,BC           
487D: 47         LD      B,A             
487E: 09         ADD     HL,BC           
487F: 33         INC     SP              
4880: FD                              
4881: E1         POP     HL              
4882: 0A         LD      A,(BC)          
4883: 8E         ADC     A,(HL)          
4884: 70         LD      (HL),B          
4885: 7C         LD      A,H             
4886: 43         LD      B,E             
4887: B6         OR      (HL)            
4888: 45         LD      B,L             
4889: B7         OR      A               
488A: 88         ADC     A,B             
488B: 50         LD      D,B             
488C: 03         INC     BC              
488D: 86         ADD     A,(HL)          
488E: 60         LD      H,B             
488F: 03         INC     BC              
4890: 66         LD      H,(HL)          
4891: 3D         DEC     A               
4892: 67         LD      H,A             
4893: 2F         CPL                     
4894: 68         LD      L,B             
4895: 4E         LD      C,(HL)          
4896: 86         ADD     A,(HL)          
4897: 70         LD      (HL),B          
4898: 2F         CPL                     
4899: 76         HALT                    
489A: 4E         LD      C,(HL)          
489B: 77         LD      (HL),A          
489C: 3A         LD      A,(HLD)         
489D: 78         LD      A,B             
489E: 3F         CCF                     
489F: FE 0B      CP      $0B             
48A1: 09         ADD     HL,BC           
48A2: C7         RST     0X00            
48A3: 00         NOP                     
48A4: 37         SCF                     
48A5: 70         LD      (HL),B          
48A6: 2E 85      LD      L,$85           
48A8: 71         LD      (HL),C          
48A9: 2F         CPL                     
48AA: 76         HALT                    
48AB: 3C         INC     A               
48AC: C7         RST     0X00            
48AD: 01 37 61   LD      BC,$6137        
48B0: 33         INC     SP              
48B1: 88         ADC     A,B             
48B2: 62         LD      H,D             
48B3: 2F         CPL                     
48B4: 02         LD      (BC),A          
48B5: 39         ADD     HL,SP           
48B6: 85         ADD     A,L             
48B7: 03         INC     BC              
48B8: 3A         LD      A,(HLD)         
48B9: 05         DEC     B               
48BA: E1         POP     HL              
48BB: E1         POP     HL              
48BC: 07         RLCA                    
48BD: 5D         LD      E,L             
48BE: 50         LD      D,B             
48BF: 7C         LD      A,H             
48C0: 08 3B 03   LD      ($033B),SP      
48C3: B6         OR      (HL)            
48C4: 07         RLCA                    
48C5: B6         OR      (HL)            
48C6: 13         INC     DE              
48C7: B7         OR      A               
48C8: 17         RLA                     
48C9: B7         OR      A               
48CA: 22         LD      (HLI),A         
48CB: C8         RET     Z               
48CC: 28 C8      JR      Z,$4896         
48CE: 83         ADD     A,E             
48CF: 77         LD      (HL),A          
48D0: 0A         LD      A,(BC)          
48D1: 09         ADD     HL,BC           
48D2: C8         RET     Z               
48D3: 83         ADD     A,E             
48D4: 77         LD      (HL),A          
48D5: 04         INC     B               
48D6: 82         ADD     A,D             
48D7: 77         LD      (HL),A          
48D8: F5         PUSH    AF              
48D9: 49         LD      C,C             
48DA: 3D         DEC     A               
48DB: 59         LD      E,C             
48DC: 38 69      JR      C,$4947         
48DE: 34         INC     (HL)            
48DF: 83         ADD     A,E             
48E0: 32         LD      (HLD),A         
48E1: 03         INC     BC              
48E2: 43         LD      B,E             
48E3: 03         INC     BC              
48E4: 52         LD      D,D             
48E5: 03         INC     BC              
48E6: 83         ADD     A,E             
48E7: 36 03      LD      (HL),$03        
48E9: 47         LD      B,A             
48EA: 03         INC     BC              
48EB: 83         ADD     A,E             
48EC: 56         LD      D,(HL)          
48ED: 03         INC     BC              
48EE: FE 0B      CP      $0B             
48F0: 03         INC     BC              
48F1: 03         INC     BC              
48F2: 39         ADD     HL,SP           
48F3: 86         ADD     A,(HL)          
48F4: 04         INC     B               
48F5: 3A         LD      A,(HLD)         
48F6: C4 10 09   CALL    NZ,$0910        
48F9: 15         DEC     D               
48FA: F5         PUSH    AF              
48FB: 16 F5      LD      D,$F5           
48FD: 16 45      LD      D,$45           
48FF: C2 21 09   JP      NZ,$0921        
4902: C2 23 09   JP      NZ,$0923        
4905: 26 E1      LD      H,$E1           
4907: E1         POP     HL              
4908: 10 99      STOP    $99             
490A: 50         LD      D,B             
490B: 7C         LD      A,H             
490C: 82         ADD     A,D             
490D: 40         LD      B,B             
490E: 2F         CPL                     
490F: 42         LD      B,D             
4910: 3C         INC     A               
4911: 46         LD      B,(HL)          
4912: 3D         DEC     A               
4913: 83         ADD     A,E             
4914: 47         LD      B,A             
4915: 2F         CPL                     
4916: C2 50 C8   JP      NZ,$C850        
4919: 51         LD      D,C             
491A: 0A         LD      A,(BC)          
491B: 52         LD      D,D             
491C: 2E 53      LD      L,$53           
491E: 48         LD      C,B             
491F: 54         LD      D,H             
4920: 4A         LD      C,D             
4921: 55         LD      D,L             
4922: 49         LD      C,C             
4923: 56         LD      D,(HL)          
4924: 4E         LD      C,(HL)          
4925: 83         ADD     A,E             
4926: 57         LD      D,A             
4927: 3A         LD      A,(HLD)         
4928: 62         LD      H,D             
4929: 39         ADD     HL,SP           
492A: 84         ADD     A,H             
492B: 63         LD      H,E             
492C: 3A         LD      A,(HLD)         
492D: 66         LD      H,(HL)          
492E: 3B         DEC     SP              
492F: 7F         LD      A,A             
4930: F5         PUSH    AF              
4931: 84         ADD     A,H             
4932: 71         LD      (HL),C          
4933: 0A         LD      A,(BC)          
4934: 72         LD      (HL),D          
4935: 09         ADD     HL,BC           
4936: 75         LD      (HL),L          
4937: 3D         DEC     A               
4938: 76         HALT                    
4939: 48         LD      C,B             
493A: 77         LD      (HL),A          
493B: 4A         LD      C,D             
493C: 78         LD      A,B             
493D: 49         LD      C,C             
493E: 79         LD      A,C             
493F: 3C         INC     A               
4940: 51         LD      D,C             
4941: 6F         LD      L,A             
4942: 83         ADD     A,E             
4943: 00         NOP                     
4944: C8         RET     Z               
4945: FE 0B      CP      $0B             
4947: 03         INC     BC              
4948: 85         ADD     A,L             
4949: 00         NOP                     
494A: 3A         LD      A,(HLD)         
494B: 05         DEC     B               
494C: 3B         DEC     SP              
494D: 8A         ADC     A,D             
494E: 40         LD      B,B             
494F: 2F         CPL                     
4950: 8A         ADC     A,D             
4951: 50         LD      D,B             
4952: 3A         LD      A,(HLD)         
4953: 8A         ADC     A,D             
4954: 70         LD      (HL),B          
4955: 2F         CPL                     
4956: 14         INC     D               
4957: 09         ADD     HL,BC           
4958: 31 09 70   LD      SP,$7009        
495B: 3D         DEC     A               
495C: C4 09 38   CALL    NZ,$3809        
495F: 48         LD      C,B             
4960: 2F         CPL                     
4961: 49         LD      C,C             
4962: 4E         LD      C,(HL)          
4963: 58         LD      E,B             
4964: 3A         LD      A,(HLD)         
4965: 59         LD      E,C             
4966: 3B         DEC     SP              
4967: FE 0B      CP      $0B             
4969: 03         INC     BC              
496A: 8A         ADC     A,D             
496B: 00         NOP                     
496C: 3A         LD      A,(HLD)         
496D: 09         ADD     HL,BC           
496E: 3B         DEC     SP              
496F: 12         LD      (DE),A          
4970: 09         ADD     HL,BC           
4971: 68         LD      L,B             
4972: 09         ADD     HL,BC           
4973: 8A         ADC     A,D             
4974: 70         LD      (HL),B          
4975: 2F         CPL                     
4976: 10 C8      STOP    $C8             
4978: C2 12 C8   JP      NZ,$C812        
497B: C3 16 C8   JP      $C816           
497E: 18 C8      JR      $4948           
4980: 24         INC     H               
4981: C8         RET     Z               
4982: C2 29 C8   JP      NZ,$C829        
4985: 31 C8 C2   LD      SP,$C2C8        
4988: 40         LD      B,B             
4989: C8         RET     Z               
498A: 43         LD      B,E             
498B: C8         RET     Z               
498C: 45         LD      B,L             
498D: C8         RET     Z               
498E: 48         LD      C,B             
498F: C8         RET     Z               
4990: C2 59 C8   JP      NZ,$C859        
4993: 64         LD      H,H             
4994: C8         RET     Z               
4995: 67         LD      H,A             
4996: C8         RET     Z               
4997: 05         DEC     B               
4998: BA         CP      D               
4999: E1         POP     HL              
499A: 1F         RRA                     
499B: FE 70      CP      $70             
499D: 7C         LD      A,H             
499E: FE 0B      CP      $0B             
49A0: 03         INC     BC              
49A1: C2 00 37   JP      NZ,$3700        
49A4: 02         LD      (BC),A          
49A5: 3E 87      LD      A,$87           
49A7: 03         INC     BC              
49A8: 3A         LD      A,(HLD)         
49A9: 12         LD      (DE),A          
49AA: 39         ADD     HL,SP           
49AB: 87         ADD     A,A             
49AC: 13         INC     DE              
49AD: 3A         LD      A,(HLD)         
49AE: 20 2E      JR      NZ,$49DE        
49B0: 21 3C 30   LD      HL,$303C        
49B3: 39         ADD     HL,SP           
49B4: 31 2E 88   LD      SP,$882E        
49B7: 32         LD      (HLD),A         
49B8: 2F         CPL                     
49B9: 33         INC     SP              
49BA: 48         LD      C,B             
49BB: 35         DEC     (HL)            
49BC: 49         LD      C,C             
49BD: 40         LD      B,B             
49BE: 09         ADD     HL,BC           
49BF: 41         LD      B,C             
49C0: 39         ADD     HL,SP           
49C1: 88         ADC     A,B             
49C2: 42         LD      B,D             
49C3: 3A         LD      A,(HLD)         
49C4: C2 34 E0   JP      NZ,$E034        
49C7: 50         LD      D,B             
49C8: C8         RET     Z               
49C9: 61         LD      H,C             
49CA: C8         RET     Z               
49CB: 65         LD      H,L             
49CC: 09         ADD     HL,BC           
49CD: 66         LD      H,(HL)          
49CE: 3D         DEC     A               
49CF: 83         ADD     A,E             
49D0: 67         LD      H,A             
49D1: 2F         CPL                     
49D2: 87         ADD     A,A             
49D3: 70         LD      (HL),B          
49D4: 2F         CPL                     
49D5: 76         HALT                    
49D6: 4E         LD      C,(HL)          
49D7: 83         ADD     A,E             
49D8: 77         LD      (HL),A          
49D9: 3A         LD      A,(HLD)         
49DA: FE 0B      CP      $0B             
49DC: 03         INC     BC              
49DD: 87         ADD     A,A             
49DE: 00         NOP                     
49DF: 3A         LD      A,(HLD)         
49E0: 07         RLCA                    
49E1: 3F         CCF                     
49E2: C2 09 38   JP      NZ,$3809        
49E5: 87         ADD     A,A             
49E6: 10 3A      STOP    $3A             
49E8: 17         RLA                     
49E9: 3B         DEC     SP              
49EA: 18 09      JR      $49F5           
49EC: C2 04 E0   JP      NZ,$E004        
49EF: 21 09 26   LD      HL,$2609        
49F2: 3D         DEC     A               
49F3: 82         ADD     A,D             
49F4: 27         DAA                     
49F5: 2F         CPL                     
49F6: 29         ADD     HL,HL           
49F7: 4E         LD      C,(HL)          
49F8: 86         ADD     A,(HL)          
49F9: 30 2F      JR      NC,$4A2A        
49FB: 36 4E      LD      (HL),$4E        
49FD: 82         ADD     A,D             
49FE: 37         SCF                     
49FF: 3A         LD      A,(HLD)         
4A00: 39         ADD     HL,SP           
4A01: 3B         DEC     SP              
4A02: 86         ADD     A,(HL)          
4A03: 40         LD      B,B             
4A04: 3A         LD      A,(HLD)         
4A05: 46         LD      B,(HL)          
4A06: 3B         DEC     SP              
4A07: 38 E1      JR      C,$49EA         
4A09: E1         POP     HL              
4A0A: 0A         LD      A,(BC)          
4A0B: EA 50 7C   LD      ($7C50),A       
4A0E: C2 49 C8   JP      NZ,$C849        
4A11: 58         LD      E,B             
4A12: 09         ADD     HL,BC           
4A13: 8A         ADC     A,D             
4A14: 60         LD      H,B             
4A15: 2F         CPL                     
4A16: 8A         ADC     A,D             
4A17: 70         LD      (HL),B          
4A18: 3A         LD      A,(HLD)         
4A19: 69         LD      L,C             
4A1A: 3C         INC     A               
4A1B: 79         LD      A,C             
4A1C: 2E FE      LD      L,$FE           
4A1E: 0B         DEC     BC              
4A1F: 03         INC     BC              
4A20: 00         NOP                     
4A21: 1D         DEC     E               
4A22: 01 2E 82   LD      BC,$822E        
4A25: 02         LD      (BC),A          
4A26: 2F         CPL                     
4A27: 04         INC     B               
4A28: 48         LD      C,B             
4A29: 06 49      LD      B,$49           
4A2B: 82         ADD     A,D             
4A2C: 07         RLCA                    
4A2D: 2F         CPL                     
4A2E: 09         ADD     HL,BC           
4A2F: 4E         LD      C,(HL)          
4A30: C2 10 37   JP      NZ,$3710        
4A33: C2 11 3E   JP      NZ,$3E11        
4A36: 87         ADD     A,A             
4A37: 12         LD      (DE),A          
4A38: 3A         LD      A,(HLD)         
4A39: 87         ADD     A,A             
4A3A: 22         LD      (HLI),A         
4A3B: 3A         LD      A,(HLD)         
4A3C: C2 19 3F   JP      NZ,$3F19        
4A3F: 30 2E      JR      NC,$4A6F        
4A41: 83         ADD     A,E             
4A42: 31 2F 34   LD      SP,$342F        
4A45: 48         LD      C,B             
4A46: 36 49      LD      (HL),$49        
4A48: 83         ADD     A,E             
4A49: 37         SCF                     
4A4A: 2F         CPL                     
4A4B: 40         LD      B,B             
4A4C: 39         ADD     HL,SP           
4A4D: 89         ADC     A,C             
4A4E: 41         LD      B,C             
4A4F: 3A         LD      A,(HLD)         
4A50: C5         PUSH    BC              
4A51: 05         DEC     B               
4A52: E0 C2      LDFF00  ($C2),A         
4A54: 50         LD      D,B             
4A55: C8         RET     Z               
4A56: 54         LD      D,H             
4A57: D4 57 09   CALL    NC,$0957        
4A5A: C2 59 C8   JP      NZ,$C859        
4A5D: 61         LD      H,C             
4A5E: 09         ADD     HL,BC           
4A5F: 8A         ADC     A,D             
4A60: 70         LD      (HL),B          
4A61: 2F         CPL                     
4A62: 74         LD      (HL),H          
4A63: 48         LD      C,B             
4A64: 75         LD      (HL),L          
4A65: E0 76      LDFF00  ($76),A         
4A67: 49         LD      C,C             
4A68: FE 0B      CP      $0B             
4A6A: 03         INC     BC              
4A6B: 00         NOP                     
4A6C: 5D         LD      E,L             
4A6D: 01 1D C2   LD      BC,$C21D        
4A70: 02         LD      (BC),A          
4A71: 3E C2      LD      A,$C2           
4A73: 03         INC     BC              
4A74: 3A         LD      A,(HLD)         
4A75: C3 04 3A   JP      $3A04           
4A78: C2 05 3F   JP      NZ,$3F05        
4A7B: C2 06 E0   JP      NZ,$E006        
4A7E: C2 07 37   JP      NZ,$3707        
4A81: 09         ADD     HL,BC           
4A82: 09         ADD     HL,BC           
4A83: C2 10 38   JP      NZ,$3810        
4A86: C4 11 37   CALL    NZ,$3711        
4A89: 22         LD      (HLI),A         
4A8A: 39         ADD     HL,SP           
4A8B: 25         DEC     H               
4A8C: 3B         DEC     SP              
4A8D: 35         DEC     (HL)            
4A8E: 09         ADD     HL,BC           
4A8F: 27         DAA                     
4A90: 2E 82      LD      L,$82           
4A92: 28 2F      JR      Z,$4AC3         
4A94: 30 4E      JR      NC,$4AE4        
4A96: 32         LD      (HLD),A         
4A97: 20 34      JR      NZ,$4ACD        
4A99: 20 43      JR      NZ,$4ADE        
4A9B: 20 37      JR      NZ,$4AD4        
4A9D: 39         ADD     HL,SP           
4A9E: 38 3A      JR      C,$4ADA         
4AA0: C2 39 38   JP      NZ,$3839        
4AA3: 39         ADD     HL,SP           
4AA4: 3A         LD      A,(HLD)         
4AA5: 40         LD      B,B             
4AA6: 3B         DEC     SP              
4AA7: 51         LD      D,C             
4AA8: 33         INC     SP              
4AA9: 82         ADD     A,D             
4AAA: 52         LD      D,D             
4AAB: 2F         CPL                     
4AAC: 54         LD      D,H             
4AAD: 48         LD      C,B             
4AAE: 56         LD      D,(HL)          
4AAF: 49         LD      C,C             
4AB0: 82         ADD     A,D             
4AB1: 57         LD      D,A             
4AB2: 2F         CPL                     
4AB3: 59         LD      E,C             
4AB4: 4E         LD      C,(HL)          
4AB5: 86         ADD     A,(HL)          
4AB6: 63         LD      H,E             
4AB7: 3A         LD      A,(HLD)         
4AB8: 86         ADD     A,(HL)          
4AB9: 73         LD      (HL),E          
4ABA: 3A         LD      A,(HLD)         
4ABB: C2 69 3F   JP      NZ,$3F69        
4ABE: C3 55 E0   JP      $E055           
4AC1: 42         LD      B,D             
4AC2: 09         ADD     HL,BC           
4AC3: 23         INC     HL              
4AC4: E1         POP     HL              
4AC5: E1         POP     HL              
4AC6: 0A         LD      A,(BC)          
4AC7: B6         OR      (HL)            
4AC8: 50         LD      D,B             
4AC9: 7C         LD      A,H             
4ACA: 62         LD      H,D             
4ACB: 38 82      JR      C,$4A4F         
4ACD: 70         LD      (HL),B          
4ACE: 2F         CPL                     
4ACF: 72         LD      (HL),D          
4AD0: 4E         LD      C,(HL)          
4AD1: 49         LD      C,C             
4AD2: DD                              
4AD3: 62         LD      H,D             
4AD4: DD                              
4AD5: FE 0B      CP      $0B             
4AD7: 03         INC     BC              
4AD8: C2 02 38   JP      NZ,$3802        
4ADB: 82         ADD     A,D             
4ADC: 20 2F      JR      NZ,$4B0D        
4ADE: 22         LD      (HLI),A         
4ADF: 4E         LD      C,(HL)          
4AE0: C4 30 3A   CALL    NZ,$3A30        
4AE3: C4 31 3A   CALL    NZ,$3A31        
4AE6: C4 03 37   CALL    NZ,$3703        
4AE9: 43         LD      B,E             
4AEA: 33         INC     SP              
4AEB: 86         ADD     A,(HL)          
4AEC: 44         LD      B,H             
4AED: 2F         CPL                     
4AEE: 04         INC     B               
4AEF: 39         ADD     HL,SP           
4AF0: 85         ADD     A,L             
4AF1: 05         DEC     B               
4AF2: 3A         LD      A,(HLD)         
4AF3: 14         INC     D               
4AF4: A0         AND     B               
4AF5: C3 17 C8   JP      $C817           
4AF8: 18 09      JR      $4B03           
4AFA: 26 09      LD      H,$09           
4AFC: 32         LD      (HLD),A         
4AFD: 37         SCF                     
4AFE: C2 42 37   JP      NZ,$3742        
4B01: 62         LD      H,D             
4B02: 2E 85      LD      L,$85           
4B04: 63         LD      H,E             
4B05: 2F         CPL                     
4B06: 85         ADD     A,L             
4B07: 73         LD      (HL),E          
4B08: 3A         LD      A,(HLD)         
4B09: 87         ADD     A,A             
4B0A: 53         LD      D,E             
4B0B: 1B         DEC     DE              
4B0C: 68         LD      L,B             
4B0D: 3C         INC     A               
4B0E: 78         LD      A,B             
4B0F: 2E 79      LD      L,$79           
4B11: 2F         CPL                     
4B12: 69         LD      L,C             
4B13: 1B         DEC     DE              
4B14: 72         LD      (HL),D          
4B15: 3E 06      LD      A,$06           
4B17: E1         POP     HL              
4B18: E1         POP     HL              
4B19: 0A         LD      A,(BC)          
4B1A: BB         CP      E               
4B1B: 50         LD      D,B             
4B1C: 7C         LD      A,H             
4B1D: 08 E1 E1   LD      ($E1E1),SP      
4B20: 0A         LD      A,(BC)          
4B21: BC         CP      H               
4B22: 30 7C      JR      NC,$4BA0        
4B24: 70         LD      (HL),B          
4B25: F5         PUSH    AF              
4B26: FE 0B      CP      $0B             
4B28: 03         INC     BC              
4B29: 83         ADD     A,E             
4B2A: 00         NOP                     
4B2B: 3A         LD      A,(HLD)         
4B2C: C3 03 37   JP      $3703           
4B2F: 08 09 22   LD      ($2209),SP      
4B32: 09         ADD     HL,BC           
4B33: 25         DEC     H               
4B34: 09         ADD     HL,BC           
4B35: 27         DAA                     
4B36: 3D         DEC     A               
4B37: 82         ADD     A,D             
4B38: 28 2F      JR      Z,$4B69         
4B3A: 33         INC     SP              
4B3B: 2E 83      LD      L,$83           
4B3D: 34         INC     (HL)            
4B3E: 2F         CPL                     
4B3F: 37         SCF                     
4B40: 4E         LD      C,(HL)          
4B41: 38 E1      JR      C,$4B24         
4B43: E1         POP     HL              
4B44: 0A         LD      A,(BC)          
4B45: 89         ADC     A,C             
4B46: 40         LD      B,B             
4B47: 7C         LD      A,H             
4B48: 39         ADD     HL,SP           
4B49: 3A         LD      A,(HLD)         
4B4A: 40         LD      B,B             
4B4B: 2F         CPL                     
4B4C: 41         LD      B,C             
4B4D: 48         LD      C,B             
4B4E: 42         LD      B,D             
4B4F: E0 43      LDFF00  ($43),A         
4B51: 39         ADD     HL,SP           
4B52: 83         ADD     A,E             
4B53: 44         LD      B,H             
4B54: 3A         LD      A,(HLD)         
4B55: 47         LD      B,A             
4B56: 3B         DEC     SP              
4B57: 82         ADD     A,D             
4B58: 48         LD      C,B             
4B59: 1B         DEC     DE              
4B5A: 8A         ADC     A,D             
4B5B: 50         LD      D,B             
4B5C: 1B         DEC     DE              
4B5D: 60         LD      H,B             
4B5E: 1B         DEC     DE              
4B5F: 61         LD      H,C             
4B60: 3D         DEC     A               
4B61: 88         ADC     A,B             
4B62: 62         LD      H,D             
4B63: 2F         CPL                     
4B64: 70         LD      (HL),B          
4B65: 2F         CPL                     
4B66: 71         LD      (HL),C          
4B67: 4E         LD      C,(HL)          
4B68: 88         ADC     A,B             
4B69: 72         LD      (HL),D          
4B6A: 3A         LD      A,(HLD)         
4B6B: FE 0B      CP      $0B             
4B6D: 1B         DEC     DE              
4B6E: 8A         ADC     A,D             
4B6F: 00         NOP                     
4B70: 03         INC     BC              
4B71: 8A         ADC     A,D             
4B72: 10 03      STOP    $03             
4B74: C2 02 37   JP      NZ,$3702        
4B77: 14         INC     D               
4B78: 3D         DEC     A               
4B79: 83         ADD     A,E             
4B7A: 15         DEC     D               
4B7B: 2F         CPL                     
4B7C: 18 3C      JR      $4BBA           
4B7E: 82         ADD     A,D             
4B7F: 20 2F      JR      NZ,$4BB0        
4B81: 22         LD      (HLI),A         
4B82: 2E 23      LD      L,$23           
4B84: 2F         CPL                     
4B85: 24         INC     H               
4B86: 4E         LD      C,(HL)          
4B87: 83         ADD     A,E             
4B88: 25         DEC     H               
4B89: E1         POP     HL              
4B8A: 28 2E      JR      Z,$4BBA         
4B8C: 29         ADD     HL,HL           
4B8D: 2F         CPL                     
4B8E: 82         ADD     A,D             
4B8F: 30 3A      JR      NC,$4BCB        
4B91: 32         LD      (HLD),A         
4B92: 3E C2      LD      A,$C2           
4B94: 33         INC     SP              
4B95: 3A         LD      A,(HLD)         
4B96: 34         INC     (HL)            
4B97: 3F         CCF                     
4B98: 83         ADD     A,E             
4B99: 35         DEC     (HL)            
4B9A: E9         JP      (HL)            
4B9B: 38 3E      JR      C,$4BDB         
4B9D: C2 39 3A   JP      NZ,$3A39        
4BA0: 42         LD      B,D             
4BA1: 39         ADD     HL,SP           
4BA2: 44         LD      B,H             
4BA3: 3B         DEC     SP              
4BA4: 83         ADD     A,E             
4BA5: 45         LD      B,L             
4BA6: E9         JP      (HL)            
4BA7: 48         LD      C,B             
4BA8: 39         ADD     HL,SP           
4BA9: 83         ADD     A,E             
4BAA: 60         LD      H,B             
4BAB: 2F         CPL                     
4BAC: 63         LD      H,E             
4BAD: 3C         INC     A               
4BAE: 83         ADD     A,E             
4BAF: 70         LD      (HL),B          
4BB0: 3A         LD      A,(HLD)         
4BB1: 73         LD      (HL),E          
4BB2: 2E 86      LD      L,$86           
4BB4: 74         LD      (HL),H          
4BB5: 2F         CPL                     
4BB6: FE 0B      CP      $0B             
4BB8: 1B         DEC     DE              
4BB9: 87         ADD     A,A             
4BBA: 00         NOP                     
4BBB: 03         INC     BC              
4BBC: 87         ADD     A,A             
4BBD: 10 03      STOP    $03             
4BBF: 20 2F      JR      NZ,$4BF0        
4BC1: 21 4E 11   LD      HL,$114E        
4BC4: 3D         DEC     A               
4BC5: 12         LD      (DE),A          
4BC6: 2F         CPL                     
4BC7: 13         INC     DE              
4BC8: 3C         INC     A               
4BC9: 23         INC     HL              
4BCA: 2E 83      LD      L,$83           
4BCC: 24         INC     H               
4BCD: 2F         CPL                     
4BCE: 27         DAA                     
4BCF: 4E         LD      C,(HL)          
4BD0: C2 07 38   JP      NZ,$3807        
4BD3: 82         ADD     A,D             
4BD4: 08 50 22   LD      ($2250),SP      
4BD7: E1         POP     HL              
4BD8: C2 30 3A   JP      NZ,$3A30        
4BDB: 31 3F C2   LD      SP,$C23F        
4BDE: 32         LD      (HLD),A         
4BDF: E9         JP      (HL)            
4BE0: 33         INC     SP              
4BE1: 3E 83      LD      A,$83           
4BE3: 34         INC     (HL)            
4BE4: 3A         LD      A,(HLD)         
4BE5: 36 E1      LD      (HL),$E1        
4BE7: 37         SCF                     
4BE8: 3F         CCF                     
4BE9: 41         LD      B,C             
4BEA: 3B         DEC     SP              
4BEB: 43         LD      B,E             
4BEC: 39         ADD     HL,SP           
4BED: 83         ADD     A,E             
4BEE: 44         LD      B,H             
4BEF: 3A         LD      A,(HLD)         
4BF0: 46         LD      B,(HL)          
4BF1: E9         JP      (HL)            
4BF2: 47         LD      B,A             
4BF3: 3B         DEC     SP              
4BF4: 87         ADD     A,A             
4BF5: 51         LD      D,C             
4BF6: 0E 68      LD      C,$68           
4BF8: 0E 8A      LD      C,$8A           
4BFA: 70         LD      (HL),B          
4BFB: 2F         CPL                     
4BFC: 61         LD      H,C             
4BFD: 3D         DEC     A               
4BFE: 62         LD      H,D             
4BFF: 48         LD      C,B             
4C00: 83         ADD     A,E             
4C01: 63         LD      H,E             
4C02: E9         JP      (HL)            
4C03: 66         LD      H,(HL)          
4C04: 49         LD      C,C             
4C05: 67         LD      H,A             
4C06: 3C         INC     A               
4C07: 71         LD      (HL),C          
4C08: 4E         LD      C,(HL)          
4C09: 72         LD      (HL),D          
4C0A: 3A         LD      A,(HLD)         
4C0B: 83         ADD     A,E             
4C0C: 73         LD      (HL),E          
4C0D: E9         JP      (HL)            
4C0E: 76         HALT                    
4C0F: 3A         LD      A,(HLD)         
4C10: 77         LD      (HL),A          
4C11: 2E FE      LD      L,$FE           
4C13: 0B         DEC     BC              
4C14: 03         INC     BC              
4C15: 82         ADD     A,D             
4C16: 18 1B      JR      $4C33           
4C18: 29         ADD     HL,HL           
4C19: 1B         DEC     DE              
4C1A: 59         LD      E,C             
4C1B: 1B         DEC     DE              
4C1C: C2 50 1B   JP      NZ,$1B50        
4C1F: 87         ADD     A,A             
4C20: 00         NOP                     
4C21: 03         INC     BC              
4C22: 87         ADD     A,A             
4C23: 10 03      STOP    $03             
4C25: 20 2F      JR      NZ,$4C56        
4C27: 21 4E 11   LD      HL,$114E        
4C2A: 3D         DEC     A               
4C2B: 12         LD      (DE),A          
4C2C: 2F         CPL                     
4C2D: 13         INC     DE              
4C2E: 3C         INC     A               
4C2F: 23         INC     HL              
4C30: 2E 83      LD      L,$83           
4C32: 24         INC     H               
4C33: 2F         CPL                     
4C34: 27         DAA                     
4C35: 4E         LD      C,(HL)          
4C36: C2 07 38   JP      NZ,$3807        
4C39: 82         ADD     A,D             
4C3A: 08 50 22   LD      ($2250),SP      
4C3D: E1         POP     HL              
4C3E: C2 30 3A   JP      NZ,$3A30        
4C41: 31 3F 32   LD      SP,$323F        
4C44: 3A         LD      A,(HLD)         
4C45: 33         INC     SP              
4C46: 3E 83      LD      A,$83           
4C48: 34         INC     (HL)            
4C49: 3A         LD      A,(HLD)         
4C4A: 36 E1      LD      (HL),$E1        
4C4C: 37         SCF                     
4C4D: 3F         CCF                     
4C4E: 41         LD      B,C             
4C4F: 3B         DEC     SP              
4C50: 43         LD      B,E             
4C51: 39         ADD     HL,SP           
4C52: 83         ADD     A,E             
4C53: 44         LD      B,H             
4C54: 3A         LD      A,(HLD)         
4C55: 47         LD      B,A             
4C56: 3B         DEC     SP              
4C57: 8A         ADC     A,D             
4C58: 70         LD      (HL),B          
4C59: 2F         CPL                     
4C5A: 61         LD      H,C             
4C5B: 3D         DEC     A               
4C5C: 62         LD      H,D             
4C5D: 48         LD      C,B             
4C5E: 66         LD      H,(HL)          
4C5F: 49         LD      C,C             
4C60: 67         LD      H,A             
4C61: 3C         INC     A               
4C62: 71         LD      (HL),C          
4C63: 4E         LD      C,(HL)          
4C64: 83         ADD     A,E             
4C65: 63         LD      H,E             
4C66: 4A         LD      C,D             
4C67: 85         ADD     A,L             
4C68: 72         LD      (HL),D          
4C69: 3A         LD      A,(HLD)         
4C6A: 77         LD      (HL),A          
4C6B: 2E 52      LD      L,$52           
4C6D: 09         ADD     HL,BC           
4C6E: 82         ADD     A,D             
4C6F: 55         LD      D,L             
4C70: 09         ADD     HL,BC           
4C71: 68         LD      L,B             
4C72: 09         ADD     HL,BC           
4C73: FE 0B      CP      $0B             
4C75: 0E 00      LD      C,$00           
4C77: 50         LD      D,B             
4C78: C4 01 3E   CALL    NZ,$3E01        
4C7B: C5         PUSH    BC              
4C7C: 02         LD      (BC),A          
4C7D: 3A         LD      A,(HLD)         
4C7E: 03         INC     BC              
4C7F: E1         POP     HL              
4C80: C4 04 3F   CALL    NZ,$3F04        
4C83: C3 05 3E   JP      $3E05           
4C86: C4 06 E9   CALL    NZ,$E906        
4C89: C4 07 3A   CALL    NZ,$3A07        
4C8C: C3 08 3F   JP      $3F08           
4C8F: C2 09 3F   JP      NZ,$3F09        
4C92: C4 13 E9   CALL    NZ,$E913        
4C95: 41         LD      B,C             
4C96: 39         ADD     HL,SP           
4C97: 44         LD      B,H             
4C98: 3B         DEC     SP              
4C99: 35         DEC     (HL)            
4C9A: 39         ADD     HL,SP           
4C9B: 38 3B      JR      C,$4CD8         
4C9D: 8A         ADC     A,D             
4C9E: 60         LD      H,B             
4C9F: 2F         CPL                     
4CA0: 8A         ADC     A,D             
4CA1: 70         LD      (HL),B          
4CA2: 3A         LD      A,(HLD)         
4CA3: 29         ADD     HL,HL           
4CA4: 3B         DEC     SP              
4CA5: 61         LD      H,C             
4CA6: 3D         DEC     A               
4CA7: 70         LD      (HL),B          
4CA8: 2F         CPL                     
4CA9: 71         LD      (HL),C          
4CAA: 4E         LD      C,(HL)          
4CAB: C6 10      ADD     $10             
4CAD: 1B         DEC     DE              
4CAE: 51         LD      D,C             
4CAF: 1B         DEC     DE              
4CB0: 48         LD      C,B             
4CB1: 1B         DEC     DE              
4CB2: C3 39 1B   JP      $1B39           
4CB5: C2 63 E9   JP      NZ,$E963        
4CB8: C2 65 E9   JP      NZ,$E965        
4CBB: C2 67 E9   JP      NZ,$E967        
4CBE: C5         PUSH    BC              
4CBF: 03         INC     BC              
4CC0: E0 FE      LDFF00  ($FE),A         
4CC2: 0B         DEC     BC              
4CC3: 03         INC     BC              
4CC4: 00         NOP                     
4CC5: 37         SCF                     
4CC6: 83         ADD     A,E             
4CC7: 01 03 04   LD      BC,$0403        
4CCA: 32         LD      (HLD),A         
4CCB: 05         DEC     B               
4CCC: 2C         INC     L               
4CCD: 06 2D      LD      B,$2D           
4CCF: C4 07 3A   CALL    NZ,$3A07        
4CD2: C4 08 3F   CALL    NZ,$3F08        
4CD5: C2 09 E5   JP      NZ,$E509        
4CD8: 10 2E      STOP    $2E             
4CDA: 11 2F 12   LD      DE,$122F        
4CDD: 3C         INC     A               
4CDE: 15         DEC     D               
4CDF: A0         AND     B               
4CE0: C2 16 38   JP      NZ,$3816        
4CE3: 20 39      JR      NZ,$4D1E        
4CE5: 21 E1 E1   LD      HL,$E1E1        
4CE8: 0A         LD      A,(BC)          
4CE9: F9         LD      SP,HL           
4CEA: 20 7C      JR      NZ,$4D68        
4CEC: 22         LD      (HLI),A         
4CED: 37         SCF                     
4CEE: 29         ADD     HL,HL           
4CEF: 50         LD      D,B             
4CF0: C3 30 1B   JP      $1B30           
4CF3: C3 31 1B   JP      $1B31           
4CF6: 32         LD      (HLD),A         
4CF7: 2E 83      LD      L,$83           
4CF9: 33         INC     SP              
4CFA: 2F         CPL                     
4CFB: 36 4E      LD      (HL),$4E        
4CFD: 42         LD      B,D             
4CFE: 3E 83      LD      A,$83           
4D00: 43         LD      B,E             
4D01: 3A         LD      A,(HLD)         
4D02: 83         ADD     A,E             
4D03: 53         LD      D,E             
4D04: 3A         LD      A,(HLD)         
4D05: 46         LD      B,(HL)          
4D06: 3F         CCF                     
4D07: 47         LD      B,A             
4D08: E1         POP     HL              
4D09: E1         POP     HL              
4D0A: 0A         LD      A,(BC)          
4D0B: FA 70 7C   LD      A,($7C70)       
4D0E: 48         LD      C,B             
4D0F: 3B         DEC     SP              
4D10: 52         LD      D,D             
4D11: 39         ADD     HL,SP           
4D12: 56         LD      D,(HL)          
4D13: 3B         DEC     SP              
4D14: 8A         ADC     A,D             
4D15: 60         LD      H,B             
4D16: 2F         CPL                     
4D17: 8A         ADC     A,D             
4D18: 70         LD      (HL),B          
4D19: 3A         LD      A,(HLD)         
4D1A: FE 0B      CP      $0B             
4D1C: 03         INC     BC              
4D1D: C2 00 3E   JP      NZ,$3E00        
4D20: 20 39      JR      NZ,$4D5B        
4D22: C3 01 3E   JP      $3E01           
4D25: 31 39 88   LD      SP,$8839        
4D28: 02         LD      (BC),A          
4D29: 3A         LD      A,(HLD)         
4D2A: 12         LD      (DE),A          
4D2B: 37         SCF                     
4D2C: 22         LD      (HLI),A         
4D2D: 2E 32      LD      L,$32           
4D2F: 3E 42      LD      A,$42           
4D31: 39         ADD     HL,SP           
4D32: 03         INC     BC              
4D33: E1         POP     HL              
4D34: E1         POP     HL              
4D35: 0A         LD      A,(BC)          
4D36: 80         ADD     A,B             
4D37: 20 7C      JR      NZ,$4DB5        
4D39: 13         INC     DE              
4D3A: 03         INC     BC              
4D3B: C3 23 E0   JP      $E023           
4D3E: 14         INC     D               
4D3F: 38 24      JR      C,$4D65         
4D41: 4E         LD      C,(HL)          
4D42: 34         INC     (HL)            
4D43: 3F         CCF                     
4D44: 44         LD      B,H             
4D45: 3B         DEC     SP              
4D46: 16 37      LD      D,$37           
4D48: 26 2E      LD      H,$2E           
4D4A: 36 3E      LD      (HL),$3E        
4D4C: 46         LD      B,(HL)          
4D4D: 39         ADD     HL,SP           
4D4E: 83         ADD     A,E             
4D4F: 27         DAA                     
4D50: 2F         CPL                     
4D51: 83         ADD     A,E             
4D52: 17         RLA                     
4D53: 03         INC     BC              
4D54: 07         RLCA                    
4D55: E1         POP     HL              
4D56: E1         POP     HL              
4D57: 0A         LD      A,(BC)          
4D58: 83         ADD     A,E             
4D59: 80         ADD     A,B             
4D5A: 7C         LD      A,H             
4D5B: 37         SCF                     
4D5C: 37         SCF                     
4D5D: 47         LD      B,A             
4D5E: 2E 57      LD      L,$57           
4D60: 39         ADD     HL,SP           
4D61: 82         ADD     A,D             
4D62: 48         LD      C,B             
4D63: 2F         CPL                     
4D64: 82         ADD     A,D             
4D65: 58         LD      E,B             
4D66: 3A         LD      A,(HLD)         
4D67: 39         ADD     HL,SP           
4D68: 03         INC     BC              
4D69: 8A         ADC     A,D             
4D6A: 60         LD      H,B             
4D6B: 2F         CPL                     
4D6C: 8A         ADC     A,D             
4D6D: 70         LD      (HL),B          
4D6E: 3A         LD      A,(HLD)         
4D6F: C3 15 3A   JP      $3A15           
4D72: 45         LD      B,L             
4D73: E1         POP     HL              
4D74: E1         POP     HL              
4D75: 1F         RRA                     
4D76: F2                              
4D77: 48         LD      C,B             
4D78: 40         LD      B,B             
4D79: 45         LD      B,L             
4D7A: E8 16      ADD     SP,$16          
4D7C: DE 37      SBC     $37             
4D7E: DE 12      SBC     $12             
4D80: DE 14      SBC     $14             
4D82: DD                              
4D83: FE 0B      CP      $0B             
4D85: 03         INC     BC              
4D86: C8         RET     Z               
4D87: 09         ADD     HL,BC           
4D88: E5         PUSH    HL              
4D89: 86         ADD     A,(HL)          
4D8A: 00         NOP                     
4D8B: 3A         LD      A,(HLD)         
4D8C: 02         LD      (BC),A          
4D8D: E1         POP     HL              
4D8E: E1         POP     HL              
4D8F: 0A         LD      A,(BC)          
4D90: 82         ADD     A,D             
4D91: 70         LD      (HL),B          
4D92: 7C         LD      A,H             
4D93: C3 06 3F   JP      $3F06           
4D96: 07         RLCA                    
4D97: E1         POP     HL              
4D98: E1         POP     HL              
4D99: 0A         LD      A,(BC)          
4D9A: 8C         ADC     A,H             
4D9B: 60         LD      H,B             
4D9C: 7C         LD      A,H             
4D9D: 08 3F 84   LD      ($843F),SP      
4DA0: 10 03      STOP    $03             
4DA2: 11 09 14   LD      DE,$1409        
4DA5: 38 C2      JR      C,$4D69         
4DA7: 15         DEC     D               
4DA8: 3A         LD      A,(HLD)         
4DA9: C5         PUSH    BC              
4DAA: 18 38      JR      $4DE4           
4DAC: 84         ADD     A,H             
4DAD: 20 2F      JR      NZ,$4DDE        
4DAF: 20 48      JR      NZ,$4DF9        
4DB1: 21 E0 22   LD      HL,$22E0        
4DB4: 49         LD      C,C             
4DB5: 24         INC     H               
4DB6: 4E         LD      C,(HL)          
4DB7: 82         ADD     A,D             
4DB8: 30 03      JR      NC,$4DBD        
4DBA: 32         LD      (HLD),A         
4DBB: 38 C2      JR      C,$4D7F         
4DBD: 33         INC     SP              
4DBE: 3A         LD      A,(HLD)         
4DBF: 34         INC     (HL)            
4DC0: 3F         CCF                     
4DC1: 35         DEC     (HL)            
4DC2: E1         POP     HL              
4DC3: E1         POP     HL              
4DC4: 0A         LD      A,(BC)          
4DC5: 87         ADD     A,A             
4DC6: 60         LD      H,B             
4DC7: 7C         LD      A,H             
4DC8: 36 3B      LD      (HL),$3B        
4DCA: 82         ADD     A,D             
4DCB: 40         LD      B,B             
4DCC: 2F         CPL                     
4DCD: 42         LD      B,D             
4DCE: 4E         LD      C,(HL)          
4DCF: 43         LD      B,E             
4DD0: BA         CP      D               
4DD1: E1         POP     HL              
4DD2: 1F         RRA                     
4DD3: FB         EI                      
4DD4: 50         LD      D,B             
4DD5: 7C         LD      A,H             
4DD6: 44         LD      B,H             
4DD7: 3B         DEC     SP              
4DD8: 82         ADD     A,D             
4DD9: 50         LD      D,B             
4DDA: 3A         LD      A,(HLD)         
4DDB: 52         LD      D,D             
4DDC: 3B         DEC     SP              
4DDD: 88         ADC     A,B             
4DDE: 60         LD      H,B             
4DDF: 2F         CPL                     
4DE0: 68         LD      L,B             
4DE1: 4E         LD      C,(HL)          
4DE2: 88         ADC     A,B             
4DE3: 70         LD      (HL),B          
4DE4: 3A         LD      A,(HLD)         
4DE5: 78         LD      A,B             
4DE6: 3F         CCF                     
4DE7: 14         INC     D               
4DE8: DD                              
4DE9: 32         LD      (HLD),A         
4DEA: DD                              
4DEB: FE 03      CP      $03             
4DED: 04         INC     B               
4DEE: C3 00 37   JP      $3700           
4DF1: 86         ADD     A,(HL)          
4DF2: 01 3A 06   LD      BC,$063A        
4DF5: 37         SCF                     
4DF6: 82         ADD     A,D             
4DF7: F7         RST     0X30            
4DF8: F5         PUSH    AF              
4DF9: 86         ADD     A,(HL)          
4DFA: 11 3A 16   LD      DE,$163A        
4DFD: 2E 83      LD      L,$83           
4DFF: 17         RLA                     
4E00: 2F         CPL                     
4E01: 26 39      LD      H,$39           
4E03: 83         ADD     A,E             
4E04: 27         DAA                     
4E05: 3A         LD      A,(HLD)         
4E06: 28 E1      JR      Z,$4DE9         
4E08: E1         POP     HL              
4E09: 11 AE 50   LD      DE,$50AE        
4E0C: 7C         LD      A,H             
4E0D: 30 2E      JR      NC,$4E3D        
4E0F: 31 3C 40   LD      SP,$403C        
4E12: 39         ADD     HL,SP           
4E13: C4 41 37   CALL    NZ,$3741        
4E16: 49         LD      C,C             
4E17: 2B         DEC     HL              
4E18: C3 50 0E   JP      $0E50           
4E1B: 54         LD      D,H             
4E1C: 20 57      JR      NZ,$4E75        
4E1E: 20 C3      JR      NZ,$4DE3        
4E20: 59         LD      E,C             
4E21: 37         SCF                     
4E22: FE 03      CP      $03             
4E24: 04         INC     B               
4E25: FF         RST     0X38            
4E26: F5         PUSH    AF              
4E27: 86         ADD     A,(HL)          
4E28: 01 0A 05   LD      BC,$050A        
4E2B: 38 83      JR      C,$4DB0         
4E2D: 06 3A      LD      B,$3A           
4E2F: 83         ADD     A,E             
4E30: 16 3A      LD      D,$3A           
4E32: C8         RET     Z               
4E33: 09         ADD     HL,BC           
4E34: 37         SCF                     
4E35: 85         ADD     A,L             
4E36: 10 2F      STOP    $2F             
4E38: 12         LD      (DE),A          
4E39: 48         LD      C,B             
4E3A: 14         INC     D               
4E3B: 49         LD      C,C             
4E3C: 15         DEC     D               
4E3D: 4E         LD      C,(HL)          
4E3E: 86         ADD     A,(HL)          
4E3F: 20 3A      JR      NZ,$4E7B        
4E41: 21 E1 E1   LD      HL,$E1E1        
4E44: 11 AF 50   LD      DE,$50AF        
4E47: 7C         LD      A,H             
4E48: 25         DEC     H               
4E49: 3B         DEC     SP              
4E4A: 82         ADD     A,D             
4E4B: 34         INC     (HL)            
4E4C: 5C         LD      E,H             
4E4D: 40         LD      B,B             
4E4E: 2D         DEC     L               
4E4F: C4 48 0A   CALL    NZ,$0A48        
4E52: C3 50 38   JP      $3850           
4E55: 52         LD      D,D             
4E56: 5C         LD      E,H             
4E57: 56         LD      D,(HL)          
4E58: 0A         LD      A,(BC)          
4E59: 57         LD      D,A             
4E5A: 5C         LD      E,H             
4E5B: 83         ADD     A,E             
4E5C: 65         LD      H,L             
4E5D: 0A         LD      A,(BC)          
4E5E: C2 13 E0   JP      NZ,$E013        
4E61: FE 03      CP      $03             
4E63: 1B         DEC     DE              
4E64: 8A         ADC     A,D             
4E65: 00         NOP                     
4E66: 3A         LD      A,(HLD)         
4E67: 8A         ADC     A,D             
4E68: 10 3A      STOP    $3A             
4E6A: C6 21      ADD     $21             
4E6C: 04         INC     B               
4E6D: 83         ADD     A,E             
4E6E: 20 04      JR      NZ,$4E74        
4E70: C5         PUSH    BC              
4E71: 30 04      JR      NC,$4E77        
4E73: 23         INC     HL              
4E74: 11 32 13   LD      DE,$1332        
4E77: 33         INC     SP              
4E78: 17         RLA                     
4E79: C4 42 11   CALL    NZ,$1142        
4E7C: C3 24 30   JP      $3024           
4E7F: C2 43 30   JP      NZ,$3043        
4E82: 26 30      LD      H,$30           
4E84: C3 25 51   JP      $5125           
4E87: 29         ADD     HL,HL           
4E88: 51         LD      D,C             
4E89: 82         ADD     A,D             
4E8A: 57         LD      D,A             
4E8B: 51         LD      D,C             
4E8C: 49         LD      C,C             
4E8D: 51         LD      D,C             
4E8E: 75         LD      (HL),L          
4E8F: 51         LD      D,C             
4E90: 82         ADD     A,D             
4E91: 78         LD      A,B             
4E92: 51         LD      D,C             
4E93: C8         RET     Z               
4E94: 00         NOP                     
4E95: 38 FE      JR      C,$4E95         
4E97: 03         INC     BC              
4E98: 1B         DEC     DE              
4E99: 8A         ADC     A,D             
4E9A: 00         NOP                     
4E9B: 3A         LD      A,(HLD)         
4E9C: 8A         ADC     A,D             
4E9D: 10 3A      STOP    $3A             
4E9F: 20 51      JR      NZ,$4EF2        
4EA1: 82         ADD     A,D             
4EA2: 21 30 27   LD      HL,$2730        
4EA5: 51         LD      D,C             
4EA6: 31 30 34   LD      SP,$3430        
4EA9: 51         LD      D,C             
4EAA: 39         ADD     HL,SP           
4EAB: 51         LD      D,C             
4EAC: 83         ADD     A,E             
4EAD: 40         LD      B,B             
4EAE: 51         LD      D,C             
4EAF: 82         ADD     A,D             
4EB0: 48         LD      C,B             
4EB1: 51         LD      D,C             
4EB2: 53         LD      D,E             
4EB3: 51         LD      D,C             
4EB4: C3 59 51   JP      $5159           
4EB7: 66         LD      H,(HL)          
4EB8: 51         LD      D,C             
4EB9: 70         LD      (HL),B          
4EBA: 51         LD      D,C             
4EBB: 74         LD      (HL),H          
4EBC: 51         LD      D,C             
4EBD: 76         HALT                    
4EBE: 51         LD      D,C             
4EBF: FE 03      CP      $03             
4EC1: 1B         DEC     DE              
4EC2: 8A         ADC     A,D             
4EC3: 00         NOP                     
4EC4: 3A         LD      A,(HLD)         
4EC5: 86         ADD     A,(HL)          
4EC6: 10 3A      STOP    $3A             
4EC8: 06 3F      LD      B,$3F           
4ECA: 16 3B      LD      D,$3B           
4ECC: 13         INC     DE              
4ECD: E1         POP     HL              
4ECE: 25         DEC     H               
4ECF: 12         LD      (DE),A          
4ED0: 35         DEC     (HL)            
4ED1: 18 36      JR      $4F09           
4ED3: 14         INC     D               
4ED4: C4 46 12   CALL    NZ,$1246        
4ED7: C7         RST     0X00            
4ED8: 17         RLA                     
4ED9: 04         INC     B               
4EDA: C7         RST     0X00            
4EDB: 18 04      JR      $4EE1           
4EDD: C7         RST     0X00            
4EDE: 19         ADD     HL,DE           
4EDF: 04         INC     B               
4EE0: C3 37 F5   JP      $F537           
4EE3: 29         ADD     HL,HL           
4EE4: F5         PUSH    AF              
4EE5: 79         LD      A,C             
4EE6: F5         PUSH    AF              
4EE7: C5         PUSH    BC              
4EE8: 30 51      JR      NC,$4F3B        
4EEA: 82         ADD     A,D             
4EEB: 71         LD      (HL),C          
4EEC: 51         LD      D,C             
4EED: 75         LD      (HL),L          
4EEE: 51         LD      D,C             
4EEF: 82         ADD     A,D             
4EF0: 57         LD      D,A             
4EF1: 04         INC     B               
4EF2: 82         ADD     A,D             
4EF3: 67         LD      H,A             
4EF4: 04         INC     B               
4EF5: 82         ADD     A,D             
4EF6: 26 20      LD      H,$20           
4EF8: C2 57 20   JP      NZ,$2057        
4EFB: 02         LD      (BC),A          
4EFC: B6         OR      (HL)            
4EFD: 03         INC     BC              
4EFE: D7         RST     0X10            
4EFF: 04         INC     B               
4F00: B6         OR      (HL)            
4F01: 11 B6 12   LD      DE,$12B6        
4F04: B7         OR      A               
4F05: 14         INC     D               
4F06: B7         OR      A               
4F07: 15         DEC     D               
4F08: B6         OR      (HL)            
4F09: E1         POP     HL              
4F0A: 01 36 50   LD      BC,$5036        
4F0D: 7C         LD      A,H             
4F0E: FE 03      CP      $03             
4F10: 04         INC     B               
4F11: 8A         ADC     A,D             
4F12: 00         NOP                     
4F13: 3A         LD      A,(HLD)         
4F14: 82         ADD     A,D             
4F15: 2F         CPL                     
4F16: F5         PUSH    AF              
4F17: C2 23 20   JP      NZ,$2023        
4F1A: 35         DEC     (HL)            
4F1B: 20 24      JR      NZ,$4F41        
4F1D: 36 25      LD      (HL),$25        
4F1F: 2F         CPL                     
4F20: 26 3C      LD      H,$3C           
4F22: 36 37      LD      (HL),$37        
4F24: 46         LD      B,(HL)          
4F25: 2E 47      LD      L,$47           
4F27: 48         LD      C,B             
4F28: 48         LD      C,B             
4F29: 4A         LD      C,D             
4F2A: 49         LD      C,C             
4F2B: 49         LD      C,C             
4F2C: 56         LD      D,(HL)          
4F2D: 39         ADD     HL,SP           
4F2E: 83         ADD     A,E             
4F2F: 57         LD      D,A             
4F30: 3A         LD      A,(HLD)         
4F31: 7F         LD      A,A             
4F32: F5         PUSH    AF              
4F33: 51         LD      D,C             
4F34: 36 C2      LD      (HL),$C2        
4F36: 62         LD      H,D             
4F37: 37         SCF                     
4F38: 52         LD      D,D             
4F39: 3C         INC     A               
4F3A: 34         INC     (HL)            
4F3B: D4 09 3E   CALL    NC,$3E09        
4F3E: 19         ADD     HL,DE           
4F3F: 39         ADD     HL,SP           
4F40: FE 03      CP      $03             
4F42: 04         INC     B               
4F43: 82         ADD     A,D             
4F44: 40         LD      B,B             
4F45: 2F         CPL                     
4F46: 82         ADD     A,D             
4F47: 50         LD      D,B             
4F48: 3A         LD      A,(HLD)         
4F49: 87         ADD     A,A             
4F4A: 33         INC     SP              
4F4B: 2F         CPL                     
4F4C: 87         ADD     A,A             
4F4D: 43         LD      B,E             
4F4E: 3A         LD      A,(HLD)         
4F4F: 32         LD      (HLD),A         
4F50: 3D         DEC     A               
4F51: 42         LD      B,D             
4F52: 4E         LD      C,(HL)          
4F53: 52         LD      D,D             
4F54: 3B         DEC     SP              
4F55: 34         INC     (HL)            
4F56: 48         LD      C,B             
4F57: 35         DEC     (HL)            
4F58: 4A         LD      C,D             
4F59: 36 49      LD      (HL),$49        
4F5B: 02         LD      (BC),A          
4F5C: 09         ADD     HL,BC           
4F5D: 17         RLA                     
4F5E: 09         ADD     HL,BC           
4F5F: 75         LD      (HL),L          
4F60: 3D         DEC     A               
4F61: 66         LD      H,(HL)          
4F62: 3D         DEC     A               
4F63: 67         LD      H,A             
4F64: 35         DEC     (HL)            
4F65: 76         HALT                    
4F66: 4E         LD      C,(HL)          
4F67: 27         DAA                     
4F68: 09         ADD     HL,BC           
4F69: 8A         ADC     A,D             
4F6A: 00         NOP                     
4F6B: 3A         LD      A,(HLD)         
4F6C: 8A         ADC     A,D             
4F6D: 10 3A      STOP    $3A             
4F6F: C2 05 E0   JP      NZ,$E005        
4F72: FE 0B      CP      $0B             
4F74: 04         INC     B               
4F75: 86         ADD     A,(HL)          
4F76: 30 2F      JR      NC,$4FA7        
4F78: 32         LD      (HLD),A         
4F79: 48         LD      C,B             
4F7A: 33         INC     SP              
4F7B: 4A         LD      C,D             
4F7C: 34         INC     (HL)            
4F7D: 49         LD      C,C             
4F7E: 86         ADD     A,(HL)          
4F7F: 40         LD      B,B             
4F80: 3A         LD      A,(HLD)         
4F81: C4 46 37   CALL    NZ,$3746        
4F84: 82         ADD     A,D             
4F85: 52         LD      D,D             
4F86: 0A         LD      A,(BC)          
4F87: 54         LD      D,H             
4F88: 5C         LD      E,H             
4F89: 55         LD      D,L             
4F8A: 5C         LD      E,H             
4F8B: 65         LD      H,L             
4F8C: 5C         LD      E,H             
4F8D: 17         RLA                     
4F8E: 09         ADD     HL,BC           
4F8F: 24         INC     H               
4F90: 09         ADD     HL,BC           
4F91: 38 09      JR      C,$4F9C         
4F93: 77         LD      (HL),A          
4F94: 09         ADD     HL,BC           
4F95: 01 39 89   LD      BC,$8939        
4F98: 00         NOP                     
4F99: 3A         LD      A,(HLD)         
4F9A: 09         ADD     HL,BC           
4F9B: 3B         DEC     SP              
4F9C: 05         DEC     B               
4F9D: E0 02      LDFF00  ($02),A         
4F9F: 3F         CCF                     
4FA0: 82         ADD     A,D             
4FA1: 10 3A      STOP    $3A             
4FA3: 12         LD      (DE),A          
4FA4: 3B         DEC     SP              
4FA5: 36 3C      LD      (HL),$3C        
4FA7: 29         ADD     HL,HL           
4FA8: 2B         DEC     HL              
4FA9: C5         PUSH    BC              
4FAA: 39         ADD     HL,SP           
4FAB: 37         SCF                     
4FAC: FE 0B      CP      $0B             
4FAE: 04         INC     B               
4FAF: 86         ADD     A,(HL)          
4FB0: 03         INC     BC              
4FB1: 3A         LD      A,(HLD)         
4FB2: 02         LD      (BC),A          
4FB3: 39         ADD     HL,SP           
4FB4: 84         ADD     A,H             
4FB5: 15         DEC     D               
4FB6: 3A         LD      A,(HLD)         
4FB7: 84         ADD     A,H             
4FB8: 25         DEC     H               
4FB9: 0E 85      LD      C,$85           
4FBB: 35         DEC     (HL)            
4FBC: 0E C3      LD      C,$C3           
4FBE: 14         INC     D               
4FBF: 38 44      JR      C,$5005         
4FC1: 32         LD      (HLD),A         
4FC2: 85         ADD     A,L             
4FC3: 45         LD      B,L             
4FC4: 2C         INC     L               
4FC5: 64         LD      H,H             
4FC6: 3D         DEC     A               
4FC7: 83         ADD     A,E             
4FC8: 65         LD      H,L             
4FC9: 2F         CPL                     
4FCA: 68         LD      L,B             
4FCB: 3C         INC     A               
4FCC: 74         LD      (HL),H          
4FCD: 38 83      JR      C,$4F52         
4FCF: 75         LD      (HL),L          
4FD0: 3A         LD      A,(HLD)         
4FD1: 78         LD      A,B             
4FD2: 2E 79      LD      L,$79           
4FD4: 2F         CPL                     
4FD5: C3 09 3A   JP      $3A09           
4FD8: C2 08 3E   JP      NZ,$3E08        
4FDB: 28 39      JR      Z,$5016         
4FDD: 55         LD      D,L             
4FDE: 20 F0      JR      NZ,$4FD0        
4FE0: F5         PUSH    AF              
4FE1: 20 2D      JR      NZ,$5010        
4FE3: C5         PUSH    BC              
4FE4: 30 38      JR      NC,$501E        
4FE6: 14         INC     D               
4FE7: DD                              
4FE8: FE 0B      CP      $0B             
4FEA: 04         INC     B               
4FEB: C3 00 3A   JP      $3A00           
4FEE: C2 01 3F   JP      NZ,$3F01        
4FF1: 21 3B 88   LD      HL,$883B        
4FF4: 02         LD      (BC),A          
4FF5: 3A         LD      A,(HLD)         
4FF6: 88         ADC     A,B             
4FF7: 12         LD      (DE),A          
4FF8: 3A         LD      A,(HLD)         
4FF9: 88         ADC     A,B             
4FFA: 22         LD      (HLI),A         
4FFB: 0E 8A      LD      C,$8A           
4FFD: 30 0E      JR      NC,$500D        
4FFF: 43         LD      B,E             
5000: 0E 82      LD      C,$82           
5002: 40         LD      B,B             
5003: 2C         INC     L               
5004: 42         LD      B,D             
5005: 2D         DEC     L               
5006: C2 52 38   JP      NZ,$3852        
5009: 70         LD      (HL),B          
500A: 48         LD      C,B             
500B: 71         LD      (HL),C          
500C: E0 72      LDFF00  ($72),A         
500E: 4E         LD      C,(HL)          
500F: 53         LD      D,E             
5010: 2C         INC     L               
5011: 54         LD      D,H             
5012: 31 44 2B   LD      SP,$2B44        
5015: 85         ADD     A,L             
5016: 45         LD      B,L             
5017: 2C         INC     L               
5018: 73         LD      (HL),E          
5019: 0A         LD      A,(BC)          
501A: 74         LD      (HL),H          
501B: 2B         DEC     HL              
501C: 75         LD      (HL),L          
501D: 2C         INC     L               
501E: 76         HALT                    
501F: 2D         DEC     L               
5020: 79         LD      A,C             
5021: 2B         DEC     HL              
5022: FE 0B      CP      $0B             
5024: 0E 8A      LD      C,$8A           
5026: 00         NOP                     
5027: 3A         LD      A,(HLD)         
5028: 8A         ADC     A,D             
5029: 10 3A      STOP    $3A             
502B: 86         ADD     A,(HL)          
502C: 24         INC     H               
502D: 3A         LD      A,(HLD)         
502E: C2 03 3E   JP      NZ,$3E03        
5031: 23         INC     HL              
5032: 39         ADD     HL,SP           
5033: 40         LD      B,B             
5034: 2C         INC     L               
5035: 41         LD      B,C             
5036: 2D         DEC     L               
5037: 51         LD      D,C             
5038: 32         LD      (HLD),A         
5039: 88         ADC     A,B             
503A: 52         LD      D,D             
503B: 2C         INC     L               
503C: 50         LD      D,B             
503D: 04         INC     B               
503E: 8A         ADC     A,D             
503F: 60         LD      H,B             
5040: 04         INC     B               
5041: 8A         ADC     A,D             
5042: 70         LD      (HL),B          
5043: 04         INC     B               
5044: 14         INC     D               
5045: B6         OR      (HL)            
5046: 15         DEC     D               
5047: B7         OR      A               
5048: 17         RLA                     
5049: B6         OR      (HL)            
504A: 18 B7      JR      $5003           
504C: 26 E1      LD      H,$E1           
504E: E2         LDFF00  (C),A           
504F: 0A         LD      A,(BC)          
5050: FD                              
5051: 0B         DEC     BC              
5052: 30 70      JR      NC,$50C4        
5054: 2C         INC     L               
5055: 71         LD      (HL),C          
5056: 2D         DEC     L               
5057: 74         LD      (HL),H          
5058: 2B         DEC     HL              
5059: 75         LD      (HL),L          
505A: 2C         INC     L               
505B: 76         HALT                    
505C: 2D         DEC     L               
505D: 79         LD      A,C             
505E: 2B         DEC     HL              
505F: FE 0B      CP      $0B             
5061: 0E 14      LD      C,$14           
5063: E1         POP     HL              
5064: E1         POP     HL              
5065: 03         INC     BC              
5066: 7A         LD      A,D             
5067: 50         LD      D,B             
5068: 7C         LD      A,H             
5069: 26 C6      LD      H,$C6           
506B: E1         POP     HL              
506C: 1F         RRA                     
506D: E9         JP      (HL)            
506E: 28 20      JR      Z,$5090         
5070: 8A         ADC     A,D             
5071: 00         NOP                     
5072: 3A         LD      A,(HLD)         
5073: 8A         ADC     A,D             
5074: 10 3A      STOP    $3A             
5076: 8A         ADC     A,D             
5077: 20 3A      JR      NZ,$50B3        
5079: C2 01 3F   JP      NZ,$3F01        
507C: C2 07 3E   JP      NZ,$3E07        
507F: 21 3B 27   LD      HL,$273B        
5082: 39         ADD     HL,SP           
5083: 8A         ADC     A,D             
5084: 50         LD      D,B             
5085: 2C         INC     L               
5086: 8A         ADC     A,D             
5087: 60         LD      H,B             
5088: 04         INC     B               
5089: 8A         ADC     A,D             
508A: 70         LD      (HL),B          
508B: 04         INC     B               
508C: 54         LD      D,H             
508D: 54         LD      D,H             
508E: 83         ADD     A,E             
508F: 03         INC     BC              
5090: E9         JP      (HL)            
5091: 83         ADD     A,E             
5092: 13         INC     DE              
5093: E9         JP      (HL)            
5094: 85         ADD     A,L             
5095: 22         LD      (HLI),A         
5096: 0E 70      LD      C,$70           
5098: 2C         INC     L               
5099: 71         LD      (HL),C          
509A: 2D         DEC     L               
509B: 72         LD      (HL),D          
509C: 2B         DEC     HL              
509D: 73         LD      (HL),E          
509E: 2C         INC     L               
509F: 74         LD      (HL),H          
50A0: 2D         DEC     L               
50A1: 75         LD      (HL),L          
50A2: 2B         DEC     HL              
50A3: 76         HALT                    
50A4: 2C         INC     L               
50A5: 77         LD      (HL),A          
50A6: 2D         DEC     L               
50A7: 78         LD      A,B             
50A8: 2B         DEC     HL              
50A9: 79         LD      A,C             
50AA: 2C         INC     L               
50AB: FE 0B      CP      $0B             
50AD: 0E 8A      LD      C,$8A           
50AF: 00         NOP                     
50B0: 3A         LD      A,(HLD)         
50B1: 8A         ADC     A,D             
50B2: 10 3A      STOP    $3A             
50B4: 8A         ADC     A,D             
50B5: 20 3A      JR      NZ,$50F1        
50B7: C2 01 3F   JP      NZ,$3F01        
50BA: C2 07 3E   JP      NZ,$3E07        
50BD: 21 3B 27   LD      HL,$273B        
50C0: 39         ADD     HL,SP           
50C1: 8A         ADC     A,D             
50C2: 50         LD      D,B             
50C3: 2C         INC     L               
50C4: 8A         ADC     A,D             
50C5: 60         LD      H,B             
50C6: 04         INC     B               
50C7: 8A         ADC     A,D             
50C8: 70         LD      (HL),B          
50C9: 04         INC     B               
50CA: 54         LD      D,H             
50CB: 54         LD      D,H             
50CC: 03         INC     BC              
50CD: D5         PUSH    DE              
50CE: 04         INC     B               
50CF: D6 05      SUB     $05             
50D1: D7         RST     0X10            
50D2: 85         ADD     A,L             
50D3: 22         LD      (HLI),A         
50D4: 03         INC     BC              
50D5: 83         ADD     A,E             
50D6: 34         INC     (HL)            
50D7: 03         INC     BC              
50D8: 23         INC     HL              
50D9: 09         ADD     HL,BC           
50DA: 25         DEC     H               
50DB: 09         ADD     HL,BC           
50DC: 36 09      LD      (HL),$09        
50DE: 82         ADD     A,D             
50DF: 32         LD      (HLD),A         
50E0: 1B         DEC     DE              
50E1: 84         ADD     A,H             
50E2: 43         LD      B,E             
50E3: 1B         DEC     DE              
50E4: 13         INC     DE              
50E5: CD 14 E1   CALL    $E114           
50E8: 15         DEC     D               
50E9: CE E1      ADC     $E1             
50EB: 03         INC     BC              
50EC: 7A         LD      A,D             
50ED: 50         LD      D,B             
50EE: 7C         LD      A,H             
50EF: 70         LD      (HL),B          
50F0: 2C         INC     L               
50F1: 71         LD      (HL),C          
50F2: 2D         DEC     L               
50F3: 72         LD      (HL),D          
50F4: 2B         DEC     HL              
50F5: 73         LD      (HL),E          
50F6: 2C         INC     L               
50F7: 74         LD      (HL),H          
50F8: 2D         DEC     L               
50F9: 75         LD      (HL),L          
50FA: 2B         DEC     HL              
50FB: 76         HALT                    
50FC: 2C         INC     L               
50FD: 77         LD      (HL),A          
50FE: 2D         DEC     L               
50FF: 78         LD      A,B             
5100: 2B         DEC     HL              
5101: 79         LD      A,C             
5102: 2C         INC     L               
5103: 26 C6      LD      H,$C6           
5105: E1         POP     HL              
5106: 1F         RRA                     
5107: E9         JP      (HL)            
5108: 28 20      JR      Z,$512A         
510A: FE 0B      CP      $0B             
510C: 04         INC     B               
510D: 8A         ADC     A,D             
510E: 00         NOP                     
510F: 3A         LD      A,(HLD)         
5110: 8A         ADC     A,D             
5111: 10 3A      STOP    $3A             
5113: C2 01 3F   JP      NZ,$3F01        
5116: 21 3B 88   LD      HL,$883B        
5119: 22         LD      (HLI),A         
511A: 0E 8A      LD      C,$8A           
511C: 30 0E      JR      NC,$512C        
511E: 83         ADD     A,E             
511F: 40         LD      B,B             
5120: 0E 43      LD      C,$43           
5122: 2B         DEC     HL              
5123: 86         ADD     A,(HL)          
5124: 44         LD      B,H             
5125: 2C         INC     L               
5126: 83         ADD     A,E             
5127: 50         LD      D,B             
5128: 2C         INC     L               
5129: 53         LD      D,E             
512A: 31 20 3A   LD      SP,$3A20        
512D: 35         DEC     (HL)            
512E: FC                              
512F: 39         ADD     HL,SP           
5130: FC                              
5131: 56         LD      D,(HL)          
5132: E0 70      LDFF00  ($70),A         
5134: 2D         DEC     L               
5135: 71         LD      (HL),C          
5136: FC                              
5137: 75         LD      (HL),L          
5138: FC                              
5139: 79         LD      A,C             
513A: 2B         DEC     HL              
513B: C2 03 E9   JP      NZ,$E903        
513E: C2 05 E9   JP      NZ,$E905        
5141: C2 07 E9   JP      NZ,$E907        
5144: 69         LD      L,C             
5145: 0A         LD      A,(BC)          
5146: FE 0B      CP      $0B             
5148: 04         INC     B               
5149: 8A         ADC     A,D             
514A: 00         NOP                     
514B: 3A         LD      A,(HLD)         
514C: 8A         ADC     A,D             
514D: 10 3A      STOP    $3A             
514F: 8A         ADC     A,D             
5150: 20 0E      JR      NZ,$5160        
5152: 8A         ADC     A,D             
5153: 30 0E      JR      NC,$5163        
5155: 8A         ADC     A,D             
5156: 40         LD      B,B             
5157: 2C         INC     L               
5158: 30 2C      JR      NC,$5186        
515A: 31 2D 40   LD      SP,$402D        
515D: E8 41      ADD     SP,$41          
515F: 38 50      JR      C,$51B1         
5161: 2F         CPL                     
5162: 51         LD      D,C             
5163: 34         INC     (HL)            
5164: 34         INC     (HL)            
5165: FC                              
5166: 82         ADD     A,D             
5167: 60         LD      H,B             
5168: 0A         LD      A,(BC)          
5169: 83         ADD     A,E             
516A: 64         LD      H,H             
516B: 0A         LD      A,(BC)          
516C: 70         LD      (HL),B          
516D: 2C         INC     L               
516E: 71         LD      (HL),C          
516F: 2D         DEC     L               
5170: 74         LD      (HL),H          
5171: FC                              
5172: 45         LD      B,L             
5173: C6 55      ADD     $55             
5175: E0 E1      LDFF00  ($E1),A         
5177: 1F         RRA                     
5178: EA 88 70   LD      ($7088),A       
517B: 38 2B      JR      C,$51A8         
517D: 39         ADD     HL,SP           
517E: 2C         INC     L               
517F: 48         LD      C,B             
5180: 31 49 04   LD      SP,$0449        
5183: FE 03      CP      $03             
5185: 04         INC     B               
5186: 8A         ADC     A,D             
5187: 00         NOP                     
5188: 3A         LD      A,(HLD)         
5189: 8A         ADC     A,D             
518A: 10 3A      STOP    $3A             
518C: 8A         ADC     A,D             
518D: 20 0E      JR      NZ,$519D        
518F: 8A         ADC     A,D             
5190: 30 2C      JR      NC,$51BE        
5192: C5         PUSH    BC              
5193: 34         INC     (HL)            
5194: 0E C5      LD      C,$C5           
5196: 35         DEC     (HL)            
5197: 0E 33      LD      C,$33           
5199: 2D         DEC     L               
519A: 36 2B      LD      (HL),$2B        
519C: 43         LD      B,E             
519D: F2                              
519E: 46         LD      B,(HL)          
519F: EA 51 6E   LD      ($6E51),A       
51A2: C2 53 F3   JP      NZ,$F353        
51A5: C2 56 F0   JP      NZ,$F056        
51A8: 68         LD      L,B             
51A9: 6E         LD      L,(HL)          
51AA: 69         LD      L,C             
51AB: F5         PUSH    AF              
51AC: 73         LD      (HL),E          
51AD: F4                              
51AE: 76         HALT                    
51AF: F1         POP     AF              
51B0: 75         LD      (HL),L          
51B1: CA 15 E1   JP      Z,$E115         
51B4: E1         POP     HL              
51B5: 1F         RRA                     
51B6: F2                              
51B7: 48         LD      C,B             
51B8: 7C         LD      A,H             
51B9: FE 03      CP      $03             
51BB: 04         INC     B               
51BC: 88         ADC     A,B             
51BD: 00         NOP                     
51BE: 3A         LD      A,(HLD)         
51BF: 08 3F 09   LD      ($093F),SP      
51C2: 2D         DEC     L               
51C3: 88         ADC     A,B             
51C4: 10 3A      STOP    $3A             
51C6: C7         RST     0X00            
51C7: 18 0E      JR      $51D7           
51C9: C7         RST     0X00            
51CA: 19         ADD     HL,DE           
51CB: 38 88      JR      C,$5155         
51CD: 20 0E      JR      NZ,$51DD        
51CF: C2 36 0E   JP      NZ,$0E36        
51D2: C5         PUSH    BC              
51D3: 37         SCF                     
51D4: 0E 85      LD      C,$85           
51D6: 30 2C      JR      NC,$5204        
51D8: 35         DEC     (HL)            
51D9: 2D         DEC     L               
51DA: 45         LD      B,L             
51DB: 38 55      JR      C,$5232         
51DD: 32         LD      (HLD),A         
51DE: 56         LD      D,(HL)          
51DF: 2D         DEC     L               
51E0: C2 66 38   JP      NZ,$3866        
51E3: 6F         LD      L,A             
51E4: F5         PUSH    AF              
51E5: 82         ADD     A,D             
51E6: 70         LD      (HL),B          
51E7: F5         PUSH    AF              
51E8: 18 3B      JR      $5225           
51EA: 57         LD      D,A             
51EB: CA 68 CA   JP      Z,$CA68         
51EE: 61         LD      H,C             
51EF: C6 E1      ADD     $E1             
51F1: 1F         RRA                     
51F2: E7         RST     0X20            
51F3: 48         LD      C,B             
51F4: 10 FE      STOP    $FE             
51F6: 03         INC     BC              
51F7: 04         INC     B               
51F8: C2 00 0E   JP      NZ,$0E00        
51FB: C2 01 37   JP      NZ,$3701        
51FE: C5         PUSH    BC              
51FF: 30 37      JR      NC,$5238        
5201: 83         ADD     A,E             
5202: 46         LD      B,(HL)          
5203: E8 82      ADD     SP,$82          
5205: 55         LD      D,L             
5206: E8 C2      ADD     SP,$C2          
5208: 51         LD      D,C             
5209: F5         PUSH    AF              
520A: 62         LD      H,D             
520B: F5         PUSH    AF              
520C: 68         LD      L,B             
520D: F5         PUSH    AF              
520E: 79         LD      A,C             
520F: F5         PUSH    AF              
5210: 34         INC     (HL)            
5211: E8 54      ADD     SP,$54          
5213: D4 21 31   CALL    NC,$3121        
5216: 20 2B      JR      NZ,$5243        
5218: 12         LD      (DE),A          
5219: 44         LD      B,H             
521A: 25         DEC     H               
521B: 44         LD      B,H             
521C: 41         LD      B,C             
521D: 44         LD      B,H             
521E: C4 09 37   CALL    NZ,$3709        
5221: 39         ADD     HL,SP           
5222: 2E 49      LD      L,$49           
5224: 39         ADD     HL,SP           
5225: 25         DEC     H               
5226: 0A         LD      A,(BC)          
5227: 83         ADD     A,E             
5228: 36 0A      LD      (HL),$0A        
522A: 16 FD      LD      D,$FD           
522C: E1         POP     HL              
522D: 10 A8      STOP    $A8             
522F: 50         LD      D,B             
5230: 7C         LD      A,H             
5231: FE 03      CP      $03             
5233: 04         INC     B               
5234: 60         LD      H,B             
5235: F5         PUSH    AF              
5236: 68         LD      L,B             
5237: F5         PUSH    AF              
5238: 86         ADD     A,(HL)          
5239: 7F         LD      A,A             
523A: F5         PUSH    AF              
523B: C2 49 0A   JP      NZ,$0A49        
523E: 86         ADD     A,(HL)          
523F: 43         LD      B,E             
5240: 0A         LD      A,(BC)          
5241: 82         ADD     A,D             
5242: 55         LD      D,L             
5243: 0A         LD      A,(BC)          
5244: 08 0A 22   LD      ($220A),SP      
5247: 44         LD      B,H             
5248: C4 00 38   CALL    NZ,$3800        
524B: 30 4E      JR      NC,$529B        
524D: 40         LD      B,B             
524E: 3B         DEC     SP              
524F: C2 09 37   JP      NZ,$3709        
5252: 29         ADD     HL,HL           
5253: 2E 39      LD      L,$39           
5255: 39         ADD     HL,SP           
5256: 23         INC     HL              
5257: F5         PUSH    AF              
5258: 27         DAA                     
5259: F5         PUSH    AF              
525A: 82         ADD     A,D             
525B: 31 E8 35   LD      SP,$35E8        
525E: F5         PUSH    AF              
525F: 36 F5      LD      (HL),$F5        
5261: 36 45      LD      (HL),$45        
5263: 46         LD      B,(HL)          
5264: E1         POP     HL              
5265: E1         POP     HL              
5266: 10 9B      STOP    $9B             
5268: 50         LD      D,B             
5269: 7C         LD      A,H             
526A: FE 03      CP      $03             
526C: 04         INC     B               
526D: C3 02 11   JP      $1102           
5270: 32         LD      (HLD),A         
5271: 15         DEC     D               
5272: 33         INC     SP              
5273: 10 34      STOP    $34             
5275: 19         ADD     HL,DE           
5276: C2 44 11   JP      NZ,$1144        
5279: 87         ADD     A,A             
527A: 03         INC     BC              
527B: 1B         DEC     DE              
527C: 87         ADD     A,A             
527D: 13         INC     DE              
527E: 1B         DEC     DE              
527F: 87         ADD     A,A             
5280: 23         INC     HL              
5281: 1B         DEC     DE              
5282: 85         ADD     A,L             
5283: 35         DEC     (HL)            
5284: 1B         DEC     DE              
5285: 85         ADD     A,L             
5286: 45         LD      B,L             
5287: 1B         DEC     DE              
5288: 85         ADD     A,L             
5289: 55         LD      D,L             
528A: 1B         DEC     DE              
528B: 82         ADD     A,D             
528C: 68         LD      L,B             
528D: 1B         DEC     DE              
528E: 54         LD      D,H             
528F: 15         DEC     D               
5290: 55         LD      D,L             
5291: 10 56      STOP    $56             
5293: 19         ADD     HL,DE           
5294: 67         LD      H,A             
5295: 1B         DEC     DE              
5296: 83         ADD     A,E             
5297: 77         LD      (HL),A          
5298: 1B         DEC     DE              
5299: 84         ADD     A,H             
529A: 60         LD      H,B             
529B: F5         PUSH    AF              
529C: 86         ADD     A,(HL)          
529D: 7F         LD      A,A             
529E: F5         PUSH    AF              
529F: C2 13 30   JP      NZ,$3013        
52A2: C2 05 51   JP      NZ,$5105        
52A5: 19         ADD     HL,DE           
52A6: 51         LD      D,C             
52A7: 24         INC     H               
52A8: 30 26      JR      NC,$52D0        
52AA: 51         LD      D,C             
52AB: 82         ADD     A,D             
52AC: 45         LD      B,L             
52AD: 30 82      JR      NC,$5231        
52AF: 48         LD      C,B             
52B0: 51         LD      D,C             
52B1: 57         LD      D,A             
52B2: 30 C2      JR      NC,$5276        
52B4: 58         LD      E,B             
52B5: 51         LD      D,C             
52B6: 82         ADD     A,D             
52B7: 08 51 11   LD      ($1151),SP      
52BA: 44         LD      B,H             
52BB: 33         INC     SP              
52BC: D4 C2 00   CALL    NC,$00C2        
52BF: 38 20      JR      C,$52E1         
52C1: 4E         LD      C,(HL)          
52C2: 30 3B      JR      NC,$52FF        
52C4: C2 40 0A   JP      NZ,$0A40        
52C7: 51         LD      D,C             
52C8: 0A         LD      A,(BC)          
52C9: 53         LD      D,E             
52CA: 44         LD      B,H             
52CB: 37         SCF                     
52CC: 51         LD      D,C             
52CD: FE 03      CP      $03             
52CF: 1B         DEC     DE              
52D0: 84         ADD     A,H             
52D1: 70         LD      (HL),B          
52D2: 1B         DEC     DE              
52D3: 86         ADD     A,(HL)          
52D4: 7F         LD      A,A             
52D5: F5         PUSH    AF              
52D6: C2 00 51   JP      NZ,$5100        
52D9: C3 04 51   JP      $5104           
52DC: C4 06 51   CALL    NZ,$5106        
52DF: C2 09 51   JP      NZ,$5109        
52E2: 33         INC     SP              
52E3: 51         LD      D,C             
52E4: 83         ADD     A,E             
52E5: 40         LD      B,B             
52E6: 51         LD      D,C             
52E7: 83         ADD     A,E             
52E8: 47         LD      B,A             
52E9: 51         LD      D,C             
52EA: 53         LD      D,E             
52EB: 51         LD      D,C             
52EC: 82         ADD     A,D             
52ED: 61         LD      H,C             
52EE: 30 65      JR      NC,$5355        
52F0: 51         LD      D,C             
52F1: 82         ADD     A,D             
52F2: 67         LD      H,A             
52F3: 30 FE      JR      NC,$52F3        
52F5: 03         INC     BC              
52F6: 04         INC     B               
52F7: 86         ADD     A,(HL)          
52F8: 00         NOP                     
52F9: 1B         DEC     DE              
52FA: 86         ADD     A,(HL)          
52FB: 10 1B      STOP    $1B             
52FD: 84         ADD     A,H             
52FE: 20 1B      JR      NZ,$531B        
5300: 83         ADD     A,E             
5301: 30 1B      JR      NC,$531E        
5303: 83         ADD     A,E             
5304: 40         LD      B,B             
5305: 1B         DEC     DE              
5306: 83         ADD     A,E             
5307: 50         LD      D,B             
5308: 1B         DEC     DE              
5309: 83         ADD     A,E             
530A: 60         LD      H,B             
530B: 1B         DEC     DE              
530C: 83         ADD     A,E             
530D: 70         LD      (HL),B          
530E: 1B         DEC     DE              
530F: 83         ADD     A,E             
5310: 00         NOP                     
5311: 51         LD      D,C             
5312: 05         DEC     B               
5313: 51         LD      D,C             
5314: C2 06 12   JP      NZ,$1206        
5317: 82         ADD     A,D             
5318: F7         RST     0X30            
5319: F5         PUSH    AF              
531A: 10 51      STOP    $51             
531C: C2 12 51   JP      NZ,$5112        
531F: 15         DEC     D               
5320: 30 19      JR      NC,$533B        
5322: F5         PUSH    AF              
5323: 24         INC     H               
5324: 1A         LD      A,(DE)          
5325: 25         DEC     H               
5326: 10 26      STOP    $26             
5328: 16 27      LD      D,$27           
532A: F5         PUSH    AF              
532B: 31 51 33   LD      SP,$3351        
532E: 1A         LD      A,(DE)          
532F: 34         INC     (HL)            
5330: 16 35      LD      D,$35           
5332: F5         PUSH    AF              
5333: 82         ADD     A,D             
5334: 40         LD      B,B             
5335: 51         LD      D,C             
5336: C2 43 12   JP      NZ,$1243        
5339: C2 44 20   JP      NZ,$2044        
533C: 52         LD      D,D             
533D: 30 59      JR      NC,$5398        
533F: F5         PUSH    AF              
5340: 61         LD      H,C             
5341: 30 62      JR      NC,$53A5        
5343: F5         PUSH    AF              
5344: 82         ADD     A,D             
5345: 66         LD      H,(HL)          
5346: F5         PUSH    AF              
5347: 82         ADD     A,D             
5348: 7F         LD      A,A             
5349: F5         PUSH    AF              
534A: 82         ADD     A,D             
534B: 77         LD      (HL),A          
534C: F5         PUSH    AF              
534D: 11 A0 FE   LD      DE,$FEA0        
5350: 03         INC     BC              
5351: 04         INC     B               
5352: 60         LD      H,B             
5353: F5         PUSH    AF              
5354: C5         PUSH    BC              
5355: FF         RST     0X38            
5356: F5         PUSH    AF              
5357: 68         LD      L,B             
5358: F5         PUSH    AF              
5359: 85         ADD     A,L             
535A: 71         LD      (HL),C          
535B: F5         PUSH    AF              
535C: C3 02 37   JP      $3702           
535F: 32         LD      (HLD),A         
5360: 2E 87      LD      L,$87           
5362: 33         INC     SP              
5363: 2F         CPL                     
5364: 36 48      LD      (HL),$48        
5366: 82         ADD     A,D             
5367: 37         SCF                     
5368: 4A         LD      C,D             
5369: 39         ADD     HL,SP           
536A: 49         LD      C,C             
536B: 42         LD      B,D             
536C: 39         ADD     HL,SP           
536D: 87         ADD     A,A             
536E: 43         LD      B,E             
536F: 3A         LD      A,(HLD)         
5370: 45         LD      B,L             
5371: B6         OR      (HL)            
5372: 46         LD      B,(HL)          
5373: E1         POP     HL              
5374: 47         LD      B,A             
5375: B6         OR      (HL)            
5376: E1         POP     HL              
5377: 15         DEC     D               
5378: F0 50      LD      A,($50)         
537A: 7C         LD      A,H             
537B: C2 30 04   JP      NZ,$0430        
537E: 83         ADD     A,E             
537F: 03         INC     BC              
5380: 0F         RRCA                    
5381: 06 14      LD      B,$14           
5383: 82         ADD     A,D             
5384: 13         INC     DE              
5385: 1B         DEC     DE              
5386: 15         DEC     D               
5387: 30 16      JR      NC,$539F        
5389: 12         LD      (DE),A          
538A: 82         ADD     A,D             
538B: 23         INC     HL              
538C: 1B         DEC     DE              
538D: 25         DEC     H               
538E: 1A         LD      A,(DE)          
538F: 26 16      LD      H,$16           
5391: 53         LD      D,E             
5392: 6F         LD      L,A             
5393: FE 03      CP      $03             
5395: 04         INC     B               
5396: 30 2F      JR      NC,$53C7        
5398: 40         LD      B,B             
5399: 3A         LD      A,(HLD)         
539A: 83         ADD     A,E             
539B: 22         LD      (HLI),A         
539C: 3A         LD      A,(HLD)         
539D: 11 3D 12   LD      DE,$123D        
53A0: 48         LD      C,B             
53A1: 13         INC     DE              
53A2: 4A         LD      C,D             
53A3: 14         INC     D               
53A4: 49         LD      C,C             
53A5: 15         DEC     D               
53A6: 4E         LD      C,(HL)          
53A7: 05         DEC     B               
53A8: 38 25      JR      C,$53CF         
53AA: 3B         DEC     SP              
53AB: 06 3B      LD      B,$3B           
53AD: 82         ADD     A,D             
53AE: 32         LD      (HLD),A         
53AF: 0A         LD      A,(BC)          
53B0: 42         LD      B,D             
53B1: 0A         LD      A,(BC)          
53B2: 16 0A      LD      D,$0A           
53B4: 46         LD      B,(HL)          
53B5: E8 64      ADD     SP,$64          
53B7: E8 C2      ADD     SP,$C2          
53B9: 59         LD      E,C             
53BA: F5         PUSH    AF              
53BB: 68         LD      L,B             
53BC: F5         PUSH    AF              
53BD: 77         LD      (HL),A          
53BE: F5         PUSH    AF              
53BF: 31 4E 41   LD      SP,$414E        
53C2: 3B         DEC     SP              
53C3: 60         LD      H,B             
53C4: F5         PUSH    AF              
53C5: 7F         LD      A,A             
53C6: F5         PUSH    AF              
53C7: 24         INC     H               
53C8: 3A         LD      A,(HLD)         
53C9: 21 38 43   LD      HL,$4338        
53CC: D4 FE 0B   CALL    NC,$0BFE        
53CF: 04         INC     B               
53D0: 86         ADD     A,(HL)          
53D1: 7F         LD      A,A             
53D2: F5         PUSH    AF              
53D3: 5F         LD      E,A             
53D4: F5         PUSH    AF              
53D5: C2 06 37   JP      NZ,$3706        
53D8: C2 37 37   JP      NZ,$3737        
53DB: 26 2E      LD      H,$2E           
53DD: 36 39      LD      (HL),$39        
53DF: 27         DAA                     
53E0: 3C         INC     A               
53E1: 57         LD      D,A             
53E2: 2E 67      LD      L,$67           
53E4: 39         ADD     HL,SP           
53E5: 82         ADD     A,D             
53E6: 58         LD      E,B             
53E7: 2F         CPL                     
53E8: 82         ADD     A,D             
53E9: 68         LD      L,B             
53EA: 3A         LD      A,(HLD)         
53EB: 09         ADD     HL,BC           
53EC: 09         ADD     HL,BC           
53ED: 28 09      JR      Z,$53F8         
53EF: 09         ADD     HL,BC           
53F0: 37         SCF                     
53F1: 19         ADD     HL,DE           
53F2: 2E 29      LD      L,$29           
53F4: 39         ADD     HL,SP           
53F5: FE 0B      CP      $0B             
53F7: 04         INC     B               
53F8: C2 04 38   JP      NZ,$3804        
53FB: 83         ADD     A,E             
53FC: 05         DEC     B               
53FD: 3A         LD      A,(HLD)         
53FE: 08 3E C2   LD      ($C23E),SP      
5401: 09         ADD     HL,BC           
5402: 3A         LD      A,(HLD)         
5403: 15         DEC     D               
5404: 3A         LD      A,(HLD)         
5405: 18 39      JR      $5440           
5407: 23         INC     HL              
5408: 3D         DEC     A               
5409: 24         INC     H               
540A: 4E         LD      C,(HL)          
540B: C2 33 38   JP      NZ,$3833        
540E: 53         LD      D,E             
540F: 4E         LD      C,(HL)          
5410: 83         ADD     A,E             
5411: 50         LD      D,B             
5412: 2F         CPL                     
5413: 83         ADD     A,E             
5414: 60         LD      H,B             
5415: 3A         LD      A,(HLD)         
5416: 34         INC     (HL)            
5417: 3F         CCF                     
5418: 44         LD      B,H             
5419: 3B         DEC     SP              
541A: 63         LD      H,E             
541B: 3F         CCF                     
541C: 73         LD      (HL),E          
541D: 3F         CCF                     
541E: 7F         LD      A,A             
541F: F5         PUSH    AF              
5420: 72         LD      (HL),D          
5421: 38 C3      JR      C,$53E6         
5423: 16 37      LD      D,$37           
5425: 46         LD      B,(HL)          
5426: 33         INC     SP              
5427: 47         LD      B,A             
5428: 3C         INC     A               
5429: 57         LD      D,A             
542A: 33         INC     SP              
542B: 82         ADD     A,D             
542C: 58         LD      E,B             
542D: 2F         CPL                     
542E: 82         ADD     A,D             
542F: 28 0A      JR      Z,$543B         
5431: C3 25 0E   JP      $0E25           
5434: 83         ADD     A,E             
5435: 54         LD      D,H             
5436: 0E 86      LD      C,$86           
5438: 64         LD      H,H             
5439: 0E 74      LD      C,$74           
543B: 0E 75      LD      C,$75           
543D: 2B         DEC     HL              
543E: 84         ADD     A,H             
543F: 76         HALT                    
5440: 2C         INC     L               
5441: 00         NOP                     
5442: 38 10      JR      C,$5454         
5444: 4E         LD      C,(HL)          
5445: 20 3B      JR      NZ,$5482        
5447: 16 DE      LD      D,$DE           
5449: 72         LD      (HL),D          
544A: DD                              
544B: FE 0B      CP      $0B             
544D: 04         INC     B               
544E: 82         ADD     A,D             
544F: 00         NOP                     
5450: 3A         LD      A,(HLD)         
5451: 82         ADD     A,D             
5452: 10 3A      STOP    $3A             
5454: C2 01 E0   JP      NZ,$E001        
5457: 02         LD      (BC),A          
5458: 3F         CCF                     
5459: 12         LD      (DE),A          
545A: 3B         DEC     SP              
545B: 84         ADD     A,H             
545C: 20 0A      JR      NZ,$5468        
545E: 03         INC     BC              
545F: 0A         LD      A,(BC)          
5460: 16 F5      LD      D,$F5           
5462: 8A         ADC     A,D             
5463: 50         LD      D,B             
5464: 2F         CPL                     
5465: 8A         ADC     A,D             
5466: 60         LD      H,B             
5467: 0E 8A      LD      C,$8A           
5469: 70         LD      (HL),B          
546A: 2C         INC     L               
546B: 04         INC     B               
546C: 33         INC     SP              
546D: 05         DEC     B               
546E: 2F         CPL                     
546F: 06 34      LD      B,$34           
5471: 82         ADD     A,D             
5472: 07         RLCA                    
5473: 0A         LD      A,(BC)          
5474: 09         ADD     HL,BC           
5475: 33         INC     SP              
5476: 82         ADD     A,D             
5477: 14         INC     D               
5478: 0A         LD      A,(BC)          
5479: 19         ADD     HL,DE           
547A: 0A         LD      A,(BC)          
547B: FE 0B      CP      $0B             
547D: 04         INC     B               
547E: 35         DEC     (HL)            
547F: 3D         DEC     A               
5480: 84         ADD     A,H             
5481: 36 2F      LD      (HL),$2F        
5483: 45         LD      B,L             
5484: 38 84      JR      C,$540A         
5486: 46         LD      B,(HL)          
5487: 0E 85      LD      C,$85           
5489: 50         LD      D,B             
548A: 2F         CPL                     
548B: 55         LD      D,L             
548C: 34         INC     (HL)            
548D: 82         ADD     A,D             
548E: 56         LD      D,(HL)          
548F: 0E 58      LD      C,$58           
5491: 2B         DEC     HL              
5492: 59         LD      E,C             
5493: 2C         INC     L               
5494: 88         ADC     A,B             
5495: 60         LD      H,B             
5496: 0E 68      LD      C,$68           
5498: 37         SCF                     
5499: 69         LD      L,C             
549A: F5         PUSH    AF              
549B: 88         ADC     A,B             
549C: 70         LD      (HL),B          
549D: 2C         INC     L               
549E: 78         LD      A,B             
549F: 31 8A 00   LD      SP,$008A        
54A2: 0A         LD      A,(BC)          
54A3: 82         ADD     A,D             
54A4: 10 0A      STOP    $0A             
54A6: 83         ADD     A,E             
54A7: 14         INC     D               
54A8: 0A         LD      A,(BC)          
54A9: 19         ADD     HL,DE           
54AA: 0A         LD      A,(BC)          
54AB: 00         NOP                     
54AC: 2F         CPL                     
54AD: 01 34 04   LD      BC,$0434        
54B0: 33         INC     SP              
54B1: 05         DEC     B               
54B2: 2F         CPL                     
54B3: 06 34      LD      B,$34           
54B5: 09         ADD     HL,BC           
54B6: 33         INC     SP              
54B7: FE 0B      CP      $0B             
54B9: 04         INC     B               
54BA: 86         ADD     A,(HL)          
54BB: 30 2F      JR      NC,$54EC        
54BD: 36 3C      LD      (HL),$3C        
54BF: 46         LD      B,(HL)          
54C0: 33         INC     SP              
54C1: 47         LD      B,A             
54C2: 2F         CPL                     
54C3: 48         LD      C,B             
54C4: 3C         INC     A               
54C5: C2 58 37   JP      NZ,$3758        
54C8: 68         LD      L,B             
54C9: 2E 69      LD      L,$69           
54CB: 3C         INC     A               
54CC: 79         LD      A,C             
54CD: 37         SCF                     
54CE: 78         LD      A,B             
54CF: 3E 86      LD      A,$86           
54D1: 40         LD      B,B             
54D2: 0E 88      LD      C,$88           
54D4: 50         LD      D,B             
54D5: 0E 84      LD      C,$84           
54D7: 64         LD      H,H             
54D8: 0E 77      LD      C,$77           
54DA: 0E 83      LD      C,$83           
54DC: 50         LD      D,B             
54DD: 2C         INC     L               
54DE: 51         LD      D,C             
54DF: E0 53      LDFF00  ($53),A         
54E1: 2D         DEC     L               
54E2: 6F         LD      L,A             
54E3: F5         PUSH    AF              
54E4: 63         LD      H,E             
54E5: 38 73      JR      C,$555A         
54E7: 32         LD      (HLD),A         
54E8: 82         ADD     A,D             
54E9: 74         LD      (HL),H          
54EA: 2C         INC     L               
54EB: 76         HALT                    
54EC: 2D         DEC     L               
54ED: 33         INC     SP              
54EE: 48         LD      C,B             
54EF: 34         INC     (HL)            
54F0: E0 35      LDFF00  ($35),A         
54F2: 49         LD      C,C             
54F3: 00         NOP                     
54F4: 2F         CPL                     
54F5: 01 34 02   LD      BC,$0234        
54F8: 33         INC     SP              
54F9: 03         INC     BC              
54FA: 2F         CPL                     
54FB: 04         INC     B               
54FC: 34         INC     (HL)            
54FD: 05         DEC     B               
54FE: 33         INC     SP              
54FF: 06 2F      LD      B,$2F           
5501: 07         RLCA                    
5502: 34         INC     (HL)            
5503: 08 37 09   LD      ($0937),SP      
5506: E8 88      ADD     SP,$88          
5508: 10 0A      STOP    $0A             
550A: 18 33      JR      $553F           
550C: 19         ADD     HL,DE           
550D: 2F         CPL                     
550E: 85         ADD     A,L             
550F: 25         DEC     H               
5510: 0A         LD      A,(BC)          
5511: 82         ADD     A,D             
5512: 37         SCF                     
5513: 0A         LD      A,(BC)          
5514: FE 0A      CP      $0A             
5516: 04         INC     B               
5517: 00         NOP                     
5518: 38 10      JR      C,$552A         
551A: 34         INC     (HL)            
551B: 01 37 02   LD      BC,$0237        
551E: E8 03      ADD     SP,$03          
5520: 38 11      JR      C,$5533         
5522: 33         INC     SP              
5523: 12         LD      (DE),A          
5524: 2F         CPL                     
5525: 13         INC     DE              
5526: 34         INC     (HL)            
5527: 05         DEC     B               
5528: 37         SCF                     
5529: 06 E8      LD      B,$E8           
552B: 07         RLCA                    
552C: 38 15      JR      C,$5543         
552E: 33         INC     SP              
552F: 16 2F      LD      D,$2F           
5531: 17         RLA                     
5532: 34         INC     (HL)            
5533: 09         ADD     HL,BC           
5534: 37         SCF                     
5535: 19         ADD     HL,DE           
5536: 33         INC     SP              
5537: 41         LD      B,C             
5538: 3D         DEC     A               
5539: 88         ADC     A,B             
553A: 42         LD      B,D             
553B: 2F         CPL                     
553C: 51         LD      D,C             
553D: 38 61      JR      C,$55A0         
553F: 4E         LD      C,(HL)          
5540: 60         LD      H,B             
5541: 3D         DEC     A               
5542: 70         LD      (HL),B          
5543: 38 71      JR      C,$55B6         
5545: 3F         CCF                     
5546: 52         LD      D,D             
5547: 0E 87      LD      C,$87           
5549: 53         LD      D,E             
554A: 0E 83      LD      C,$83           
554C: 67         LD      H,A             
554D: 0E 83      LD      C,$83           
554F: 62         LD      H,D             
5550: E9         JP      (HL)            
5551: 83         ADD     A,E             
5552: 72         LD      (HL),D          
5553: E9         JP      (HL)            
5554: 65         LD      H,L             
5555: 49         LD      C,C             
5556: 66         LD      H,(HL)          
5557: 3C         INC     A               
5558: 75         LD      (HL),L          
5559: 3A         LD      A,(HLD)         
555A: 76         HALT                    
555B: 2E 83      LD      L,$83           
555D: 77         LD      (HL),A          
555E: 2F         CPL                     
555F: 84         ADD     A,H             
5560: 20 0A      JR      NZ,$556C        
5562: 14         INC     D               
5563: 0A         LD      A,(BC)          
5564: 83         ADD     A,E             
5565: 25         DEC     H               
5566: 0A         LD      A,(BC)          
5567: 18 0A      JR      $5573           
5569: 29         ADD     HL,HL           
556A: 0A         LD      A,(BC)          
556B: FE 0A      CP      $0A             
556D: 04         INC     B               
556E: 00         NOP                     
556F: E8 01      ADD     SP,$01          
5571: 38 10      JR      C,$5583         
5573: 2F         CPL                     
5574: 11 34 04   LD      DE,$0434        
5577: 37         SCF                     
5578: 05         DEC     B               
5579: E8 06      ADD     SP,$06          
557B: 38 14      JR      C,$5591         
557D: 33         INC     SP              
557E: 15         DEC     D               
557F: 2F         CPL                     
5580: 16 34      LD      D,$34           
5582: 8A         ADC     A,D             
5583: 40         LD      B,B             
5584: 2F         CPL                     
5585: 8A         ADC     A,D             
5586: 50         LD      D,B             
5587: 0E 60      LD      C,$60           
5589: 0E 70      LD      C,$70           
558B: 2F         CPL                     
558C: 71         LD      (HL),C          
558D: 4E         LD      C,(HL)          
558E: 61         LD      H,C             
558F: 3D         DEC     A               
5590: 62         LD      H,D             
5591: 48         LD      C,B             
5592: 72         LD      (HL),D          
5593: 3A         LD      A,(HLD)         
5594: 82         ADD     A,D             
5595: 63         LD      H,E             
5596: E9         JP      (HL)            
5597: 82         ADD     A,D             
5598: 73         LD      (HL),E          
5599: E9         JP      (HL)            
559A: 65         LD      H,L             
559B: 49         LD      C,C             
559C: 84         ADD     A,H             
559D: 66         LD      H,(HL)          
559E: 2F         CPL                     
559F: 85         ADD     A,L             
55A0: 75         LD      (HL),L          
55A1: 3A         LD      A,(HLD)         
55A2: 82         ADD     A,D             
55A3: 20 0A      JR      NZ,$55AF        
55A5: 83         ADD     A,E             
55A6: 24         INC     H               
55A7: 0A         LD      A,(BC)          
55A8: FE 0B      CP      $0B             
55AA: 04         INC     B               
55AB: C2 03 38   JP      NZ,$3803        
55AE: C4 04 0E   CALL    NZ,$0E04        
55B1: 05         DEC     B               
55B2: 2B         DEC     HL              
55B3: 06 31      LD      B,$31           
55B5: C2 09 F5   JP      NZ,$F509        
55B8: C3 15 37   JP      $3715           
55BB: 21 3D 22   LD      HL,$223D        
55BE: E0 23      LDFF00  ($23),A         
55C0: 34         INC     (HL)            
55C1: 31 38 83   LD      SP,$8338        
55C4: 32         LD      (HLD),A         
55C5: 0E 40      LD      C,$40           
55C7: 2F         CPL                     
55C8: 41         LD      B,C             
55C9: 34         INC     (HL)            
55CA: 83         ADD     A,E             
55CB: 42         LD      B,D             
55CC: CA 45 33   JP      Z,$3345         
55CF: 84         ADD     A,H             
55D0: 46         LD      B,(HL)          
55D1: 2F         CPL                     
55D2: 8A         ADC     A,D             
55D3: 50         LD      D,B             
55D4: 0E 8A      LD      C,$8A           
55D6: 60         LD      H,B             
55D7: 2F         CPL                     
55D8: 8A         ADC     A,D             
55D9: 70         LD      (HL),B          
55DA: 3A         LD      A,(HLD)         
55DB: FE 03      CP      $03             
55DD: 04         INC     B               
55DE: C2 0F F5   JP      NZ,$F50F        
55E1: 01 FD 82   LD      BC,$82FD        
55E4: 21 0A 14   LD      HL,$140A        
55E7: 0A         LD      A,(BC)          
55E8: C2 06 38   JP      NZ,$3806        
55EB: 25         DEC     H               
55EC: 3D         DEC     A               
55ED: 26 34      LD      H,$34           
55EF: 35         DEC     (HL)            
55F0: 38 45      JR      C,$5637         
55F2: 34         INC     (HL)            
55F3: 84         ADD     A,H             
55F4: 40         LD      B,B             
55F5: 2F         CPL                     
55F6: 44         LD      B,H             
55F7: E0 89      LDFF00  ($89),A         
55F9: 60         LD      H,B             
55FA: 2F         CPL                     
55FB: 89         ADC     A,C             
55FC: 70         LD      (HL),B          
55FD: 3A         LD      A,(HLD)         
55FE: C8         RET     Z               
55FF: 09         ADD     HL,BC           
5600: 38 C6      JR      C,$55C8         
5602: 07         RLCA                    
5603: 0E C3      LD      C,$C3           
5605: 36 0E      LD      (HL),$0E        
5607: 86         ADD     A,(HL)          
5608: 50         LD      D,B             
5609: 0E C6      LD      C,$C6           
560B: 08 0E 23   LD      ($230E),SP      
560E: D4 69 4E   CALL    NC,$4E69        
5611: 79         LD      A,C             
5612: 3F         CCF                     
5613: E1         POP     HL              
5614: 10 B0      STOP    $B0             
5616: 50         LD      D,B             
5617: 7C         LD      A,H             
5618: 01 B6 02   LD      BC,$02B6        
561B: B7         OR      A               
561C: 03         INC     BC              
561D: 66         LD      H,(HL)          
561E: FE 03      CP      $03             
5620: 04         INC     B               
5621: C8         RET     Z               
5622: 00         NOP                     
5623: 37         SCF                     
5624: C4 01 90   CALL    NZ,$9001        
5627: C4 02 90   CALL    NZ,$9002        
562A: 41         LD      B,C             
562B: 88         ADC     A,B             
562C: C3 51 87   JP      $8751           
562F: 03         INC     BC              
5630: 8E         ADC     A,(HL)          
5631: C2 13 87   JP      NZ,$8713        
5634: 33         INC     SP              
5635: 8A         ADC     A,D             
5636: 86         ADD     A,(HL)          
5637: 34         INC     (HL)            
5638: 85         ADD     A,L             
5639: 88         ADC     A,B             
563A: 42         LD      B,D             
563B: 84         ADD     A,H             
563C: C2 F1 F5   JP      NZ,$F5F1        
563F: 14         INC     D               
5640: 08 27 08   LD      ($0827),SP      
5643: 52         LD      D,D             
5644: 08 83 53   LD      ($5383),SP      
5647: 5C         LD      E,H             
5648: 75         LD      (HL),L          
5649: 0A         LD      A,(BC)          
564A: 76         HALT                    
564B: 8F         ADC     A,A             
564C: 83         ADD     A,E             
564D: 77         LD      (HL),A          
564E: 85         ADD     A,L             
564F: 08 8F 09   LD      ($098F),SP      
5652: 90         SUB     B               
5653: 18 8D      JR      $55E2           
5655: 19         ADD     HL,DE           
5656: 84         ADD     A,H             
5657: F9         LD      SP,HL           
5658: F5         PUSH    AF              
5659: 35         DEC     (HL)            
565A: 8E         ADC     A,(HL)          
565B: 36 04      LD      (HL),$04        
565D: 37         SCF                     
565E: 8F         ADC     A,A             
565F: 45         LD      B,L             
5660: 8C         ADC     A,H             
5661: 46         LD      B,(HL)          
5662: E8 47      ADD     SP,$47          
5664: 8D         ADC     A,L             
5665: 28 44      JR      Z,$56AB         
5667: 72         LD      (HL),D          
5668: 44         LD      B,H             
5669: FE 03      CP      $03             
566B: 04         INC     B               
566C: 8A         ADC     A,D             
566D: 00         NOP                     
566E: 90         SUB     B               
566F: 86         ADD     A,(HL)          
5670: FF         RST     0X38            
5671: F5         PUSH    AF              
5672: 8A         ADC     A,D             
5673: 10 84      STOP    $84             
5675: 16 89      LD      D,$89           
5677: 17         RLA                     
5678: 88         ADC     A,B             
5679: 26 86      LD      H,$86           
567B: 27         DAA                     
567C: 87         ADD     A,A             
567D: 36 8D      LD      (HL),$8D        
567F: 37         SCF                     
5680: 8C         ADC     A,H             
5681: C2 47 E8   JP      NZ,$E847        
5684: 82         ADD     A,D             
5685: 30 85      JR      NC,$560C        
5687: 32         LD      (HLD),A         
5688: 8E         ADC     A,(HL)          
5689: 40         LD      B,B             
568A: 84         ADD     A,H             
568B: 41         LD      B,C             
568C: 89         ADC     A,C             
568D: C4 42 87   CALL    NZ,$8742        
5690: C2 51 86   JP      NZ,$8651        
5693: 70         LD      (HL),B          
5694: 85         ADD     A,L             
5695: 71         LD      (HL),C          
5696: 8B         ADC     A,E             
5697: 58         LD      E,B             
5698: 8F         ADC     A,A             
5699: 59         LD      E,C             
569A: 85         ADD     A,L             
569B: 67         LD      H,A             
569C: 8F         ADC     A,A             
569D: 77         LD      (HL),A          
569E: 86         ADD     A,(HL)          
569F: 82         ADD     A,D             
56A0: 68         LD      L,B             
56A1: 90         SUB     B               
56A2: 82         ADD     A,D             
56A3: 78         LD      A,B             
56A4: 90         SUB     B               
56A5: 68         LD      L,B             
56A6: F5         PUSH    AF              
56A7: 79         LD      A,C             
56A8: F5         PUSH    AF              
56A9: 83         ADD     A,E             
56AA: 33         INC     SP              
56AB: 5C         LD      E,H             
56AC: 44         LD      B,H             
56AD: 5C         LD      E,H             
56AE: 34         INC     (HL)            
56AF: A0         AND     B               
56B0: 28 08      JR      Z,$56BA         
56B2: C2 66 0A   JP      NZ,$0A66        
56B5: 65         LD      H,L             
56B6: 08 38 44   LD      ($4438),SP      
56B9: 73         LD      (HL),E          
56BA: 44         LD      B,H             
56BB: FE 03      CP      $03             
56BD: 04         INC     B               
56BE: 8A         ADC     A,D             
56BF: 00         NOP                     
56C0: 90         SUB     B               
56C1: 86         ADD     A,(HL)          
56C2: FF         RST     0X38            
56C3: F5         PUSH    AF              
56C4: 8A         ADC     A,D             
56C5: 10 84      STOP    $84             
56C7: 11 89 21   LD      DE,$2189        
56CA: 86         ADD     A,(HL)          
56CB: 31 8D 32   LD      SP,$328D        
56CE: 8C         ADC     A,H             
56CF: 22         LD      (HLI),A         
56D0: 87         ADD     A,A             
56D1: 12         LD      (DE),A          
56D2: 88         ADC     A,B             
56D3: 13         INC     DE              
56D4: 92         SUB     D               
56D5: 14         INC     D               
56D6: 89         ADC     A,C             
56D7: 24         INC     H               
56D8: 86         ADD     A,(HL)          
56D9: 34         INC     (HL)            
56DA: 8D         ADC     A,L             
56DB: 35         DEC     (HL)            
56DC: 84         ADD     A,H             
56DD: 23         INC     HL              
56DE: E4                              
56DF: 36 8C      LD      (HL),$8C        
56E1: 26 87      LD      H,$87           
56E3: 16 88      LD      D,$88           
56E5: 50         LD      D,B             
56E6: 8E         ADC     A,(HL)          
56E7: 60         LD      H,B             
56E8: 8A         ADC     A,D             
56E9: 61         LD      H,C             
56EA: 8E         ADC     A,(HL)          
56EB: 70         LD      (HL),B          
56EC: 90         SUB     B               
56ED: 71         LD      (HL),C          
56EE: 87         ADD     A,A             
56EF: 48         LD      C,B             
56F0: 8F         ADC     A,A             
56F1: 49         LD      C,C             
56F2: 85         ADD     A,L             
56F3: 58         LD      E,B             
56F4: 86         ADD     A,(HL)          
56F5: 68         LD      L,B             
56F6: 8B         ADC     A,E             
56F7: 66         LD      H,(HL)          
56F8: 8F         ADC     A,A             
56F9: 67         LD      H,A             
56FA: 85         ADD     A,L             
56FB: 76         HALT                    
56FC: 86         ADD     A,(HL)          
56FD: 83         ADD     A,E             
56FE: 77         LD      (HL),A          
56FF: 90         SUB     B               
5700: C2 59 90   JP      NZ,$9059        
5703: C2 20 0A   JP      NZ,$0A20        
5706: 41         LD      B,C             
5707: 0A         LD      A,(BC)          
5708: 42         LD      B,D             
5709: 20 44      JR      NZ,$574F        
570B: 20 53      JR      NZ,$5760        
570D: 20 C2      JR      NZ,$56D1        
570F: 47         LD      B,A             
5710: 0A         LD      A,(BC)          
5711: C2 65 0A   JP      NZ,$0A65        
5714: 51         LD      D,C             
5715: 08 C2 15   LD      ($15C2),SP      
5718: 90         SUB     B               
5719: 59         LD      E,C             
571A: F5         PUSH    AF              
571B: 82         ADD     A,D             
571C: 77         LD      (HL),A          
571D: F5         PUSH    AF              
571E: 7F         LD      A,A             
571F: F5         PUSH    AF              
5720: 33         INC     SP              
5721: E3                              
5722: E1         POP     HL              
5723: 11 B3 50   LD      DE,$50B3        
5726: 7C         LD      A,H             
5727: 56         LD      D,(HL)          
5728: 44         LD      B,H             
5729: 64         LD      H,H             
572A: 44         LD      B,H             
572B: FE 03      CP      $03             
572D: 04         INC     B               
572E: 8A         ADC     A,D             
572F: 00         NOP                     
5730: 90         SUB     B               
5731: 85         ADD     A,L             
5732: FF         RST     0X38            
5733: F5         PUSH    AF              
5734: 8A         ADC     A,D             
5735: 10 84      STOP    $84             
5737: 28 8C      JR      Z,$56C5         
5739: 40         LD      B,B             
573A: 85         ADD     A,L             
573B: 41         LD      B,C             
573C: 8E         ADC     A,(HL)          
573D: 51         LD      D,C             
573E: 87         ADD     A,A             
573F: 61         LD      H,C             
5740: 8A         ADC     A,D             
5741: 86         ADD     A,(HL)          
5742: 62         LD      H,D             
5743: 85         ADD     A,L             
5744: 88         ADC     A,B             
5745: 70         LD      (HL),B          
5746: 90         SUB     B               
5747: 86         ADD     A,(HL)          
5748: 7F         LD      A,A             
5749: F5         PUSH    AF              
574A: 67         LD      H,A             
574B: 8E         ADC     A,(HL)          
574C: C2 50 90   JP      NZ,$9050        
574F: 5F         LD      E,A             
5750: F5         PUSH    AF              
5751: 86         ADD     A,(HL)          
5752: 52         LD      D,D             
5753: 0A         LD      A,(BC)          
5754: 68         LD      L,B             
5755: 0A         LD      A,(BC)          
5756: 32         LD      (HLD),A         
5757: 08 48 08   LD      ($0848),SP      
575A: 69         LD      L,C             
575B: 08 17 89   LD      ($8917),SP      
575E: 27         DAA                     
575F: 8D         ADC     A,L             
5760: 82         ADD     A,D             
5761: 18 90      JR      $56F3           
5763: 82         ADD     A,D             
5764: 28 90      JR      Z,$56F6         
5766: C2 08 F5   JP      NZ,$F508        
5769: 19         ADD     HL,DE           
576A: F5         PUSH    AF              
576B: 33         INC     SP              
576C: 44         LD      B,H             
576D: 46         LD      B,(HL)          
576E: 44         LD      B,H             
576F: FE 03      CP      $03             
5771: 04         INC     B               
5772: 82         ADD     A,D             
5773: FF         RST     0X38            
5774: F5         PUSH    AF              
5775: 82         ADD     A,D             
5776: F7         RST     0X30            
5777: F5         PUSH    AF              
5778: 85         ADD     A,L             
5779: 00         NOP                     
577A: F5         PUSH    AF              
577B: 82         ADD     A,D             
577C: 04         INC     B               
577D: 04         INC     B               
577E: 82         ADD     A,D             
577F: 14         INC     D               
5780: 04         INC     B               
5781: 82         ADD     A,D             
5782: 1F         RRA                     
5783: F5         PUSH    AF              
5784: 7F         LD      A,A             
5785: F5         PUSH    AF              
5786: C2 59 F5   JP      NZ,$F559        
5789: 83         ADD     A,E             
578A: 23         INC     HL              
578B: E8 83      ADD     SP,$83          
578D: 63         LD      H,E             
578E: E8 C3      ADD     SP,$C3          
5790: 32         LD      (HLD),A         
5791: E8 C3      ADD     SP,$C3          
5793: 36 E8      LD      (HL),$E8        
5795: 83         ADD     A,E             
5796: 33         INC     SP              
5797: 0A         LD      A,(BC)          
5798: 83         ADD     A,E             
5799: 43         LD      B,E             
579A: 0A         LD      A,(BC)          
579B: 83         ADD     A,E             
579C: 53         LD      D,E             
579D: 0A         LD      A,(BC)          
579E: 82         ADD     A,D             
579F: 50         LD      D,B             
57A0: 0B         DEC     BC              
57A1: 82         ADD     A,D             
57A2: 61         LD      H,C             
57A3: 0B         DEC     BC              
57A4: 72         LD      (HL),D          
57A5: 0B         DEC     BC              
57A6: 33         INC     SP              
57A7: E8 35      ADD     SP,$35          
57A9: E8 53      ADD     SP,$53          
57AB: E8 55      ADD     SP,$55          
57AD: E8 37      ADD     SP,$37          
57AF: 44         LD      B,H             
57B0: 58         LD      E,B             
57B1: 44         LD      B,H             
57B2: 20 F5      JR      NZ,$57A9        
57B4: 26 20      LD      H,$20           
57B6: FE 03      CP      $03             
57B8: 04         INC     B               
57B9: 86         ADD     A,(HL)          
57BA: FF         RST     0X38            
57BB: F5         PUSH    AF              
57BC: 85         ADD     A,L             
57BD: 00         NOP                     
57BE: F5         PUSH    AF              
57BF: C2 5F F5   JP      NZ,$F55F        
57C2: 13         INC     DE              
57C3: F5         PUSH    AF              
57C4: 33         INC     SP              
57C5: 20 42      JR      NZ,$5809        
57C7: 3D         DEC     A               
57C8: 82         ADD     A,D             
57C9: 43         LD      B,E             
57CA: 2F         CPL                     
57CB: 44         LD      B,H             
57CC: E0 45      LDFF00  ($45),A         
57CE: 3C         INC     A               
57CF: 84         ADD     A,H             
57D0: 46         LD      B,(HL)          
57D1: 0A         LD      A,(BC)          
57D2: 51         LD      D,C             
57D3: 20 52      JR      NZ,$5827        
57D5: 38 82      JR      C,$5759         
57D7: 53         LD      D,E             
57D8: 1B         DEC     DE              
57D9: 55         LD      D,L             
57DA: 37         SCF                     
57DB: 83         ADD     A,E             
57DC: 56         LD      D,(HL)          
57DD: 0A         LD      A,(BC)          
57DE: 61         LD      H,C             
57DF: 0A         LD      A,(BC)          
57E0: 62         LD      H,D             
57E1: 32         LD      (HLD),A         
57E2: 82         ADD     A,D             
57E3: 63         LD      H,E             
57E4: 2C         INC     L               
57E5: 65         LD      H,L             
57E6: 31 66 0A   LD      SP,$0A66        
57E9: 83         ADD     A,E             
57EA: 73         LD      (HL),E          
57EB: 0A         LD      A,(BC)          
57EC: 20 44      JR      NZ,$5832        
57EE: 78         LD      A,B             
57EF: 44         LD      B,H             
57F0: 22         LD      (HLI),A         
57F1: D4 27 FD   CALL    NC,$FD27        
57F4: E1         POP     HL              
57F5: 0E AD      LD      C,$AD           
57F7: 50         LD      D,B             
57F8: 7C         LD      A,H             
57F9: C2 59 F5   JP      NZ,$F559        
57FC: FE 03      CP      $03             
57FE: 04         INC     B               
57FF: FF         RST     0X38            
5800: F5         PUSH    AF              
5801: 59         LD      E,C             
5802: 0A         LD      A,(BC)          
5803: C2 00 F5   JP      NZ,$F500        
5806: 82         ADD     A,D             
5807: F7         RST     0X30            
5808: F5         PUSH    AF              
5809: 14         INC     D               
580A: FB         EI                      
580B: 18 FB      JR      $5808           
580D: 36 FB      LD      (HL),$FB        
580F: 49         LD      C,C             
5810: FB         EI                      
5811: 53         LD      D,E             
5812: FB         EI                      
5813: 75         LD      (HL),L          
5814: FB         EI                      
5815: 79         LD      A,C             
5816: FB         EI                      
5817: C3 12 0A   JP      $0A12           
581A: 23         INC     HL              
581B: 0A         LD      A,(BC)          
581C: 83         ADD     A,E             
581D: 33         INC     SP              
581E: 09         ADD     HL,BC           
581F: 82         ADD     A,D             
5820: 42         LD      B,D             
5821: 09         ADD     HL,BC           
5822: C2 40 0A   JP      NZ,$0A40        
5825: 51         LD      D,C             
5826: 09         ADD     HL,BC           
5827: 82         ADD     A,D             
5828: 67         LD      H,A             
5829: 09         ADD     HL,BC           
582A: 82         ADD     A,D             
582B: 38 03      JR      C,$5830         
582D: 48         LD      C,B             
582E: 03         INC     BC              
582F: 82         ADD     A,D             
5830: 56         LD      D,(HL)          
5831: 03         INC     BC              
5832: 82         ADD     A,D             
5833: 71         LD      (HL),C          
5834: 03         INC     BC              
5835: C2 5F F5   JP      NZ,$F55F        
5838: 41         LD      B,C             
5839: 20 FE      JR      NZ,$5839        
583B: 03         INC     BC              
583C: 04         INC     B               
583D: 50         LD      D,B             
583E: 0A         LD      A,(BC)          
583F: 86         ADD     A,(HL)          
5840: FF         RST     0X38            
5841: F5         PUSH    AF              
5842: C4 08 F5   CALL    NZ,$F508        
5845: 10 FB      STOP    $FB             
5847: 25         DEC     H               
5848: FB         EI                      
5849: 3F         CCF                     
584A: FB         EI                      
584B: 52         LD      D,D             
584C: FB         EI                      
584D: 70         LD      (HL),B          
584E: B7         OR      A               
584F: 22         LD      (HLI),A         
5850: E8 15      ADD     SP,$15          
5852: 09         ADD     HL,BC           
5853: 23         INC     HL              
5854: 09         ADD     HL,BC           
5855: 84         ADD     A,H             
5856: 30 03      JR      NC,$585B        
5858: 82         ADD     A,D             
5859: 44         LD      B,H             
585A: 09         ADD     HL,BC           
585B: 47         LD      B,A             
585C: 03         INC     BC              
585D: 55         LD      D,L             
585E: E8 67      ADD     SP,$67          
5860: 09         ADD     HL,BC           
5861: 82         ADD     A,D             
5862: 56         LD      D,(HL)          
5863: 03         INC     BC              
5864: 82         ADD     A,D             
5865: 64         LD      H,H             
5866: 03         INC     BC              
5867: 82         ADD     A,D             
5868: 72         LD      (HL),D          
5869: 03         INC     BC              
586A: 82         ADD     A,D             
586B: 74         LD      (HL),H          
586C: 09         ADD     HL,BC           
586D: 77         LD      (HL),A          
586E: 03         INC     BC              
586F: 06 F5      LD      B,$F5           
5871: 17         RLA                     
5872: F5         PUSH    AF              
5873: FE 03      CP      $03             
5875: 04         INC     B               
5876: FF         RST     0X38            
5877: F5         PUSH    AF              
5878: 10 3D      STOP    $3D             
587A: 11 2F 12   LD      DE,$122F        
587D: 4E         LD      C,(HL)          
587E: 02         LD      (BC),A          
587F: 38 03      JR      C,$5884         
5881: 3B         DEC     SP              
5882: 21 3A 22   LD      HL,$223A        
5885: 3B         DEC     SP              
5886: C6 20      ADD     $20             
5888: 38 C5      JR      C,$584F         
588A: 31 0E 83   LD      SP,$830E        
588D: 32         LD      (HLD),A         
588E: 0E C3      LD      C,$C3           
5890: 13         INC     DE              
5891: 0E C4      LD      C,$C4           
5893: 04         INC     B               
5894: 0E 05      LD      C,$05           
5896: 9B         SBC     E               
5897: 84         ADD     A,H             
5898: 06 99      LD      B,$99           
589A: 84         ADD     A,H             
589B: 16 96      LD      D,$96           
589D: 84         ADD     A,H             
589E: 26 93      LD      H,$93           
58A0: C3 15 9A   JP      $9A15           
58A3: 45         LD      B,L             
58A4: 9E         SBC     (HL)            
58A5: 82         ADD     A,D             
58A6: 43         LD      B,E             
58A7: 99         SBC     C               
58A8: 42         LD      B,D             
58A9: 9B         SBC     E               
58AA: C3 52 9A   JP      $9A52           
58AD: 82         ADD     A,D             
58AE: 53         LD      D,E             
58AF: 96         SUB     (HL)            
58B0: 55         LD      D,L             
58B1: 98         SBC     B               
58B2: 82         ADD     A,D             
58B3: 63         LD      H,E             
58B4: 93         SUB     E               
58B5: 65         LD      H,L             
58B6: 95         SUB     L               
58B7: 59         LD      E,C             
58B8: 9B         SBC     E               
58B9: 68         LD      L,B             
58BA: 9B         SBC     E               
58BB: 78         LD      A,B             
58BC: 9A         SBC     D               
58BD: C2 69 9A   JP      NZ,$9A69        
58C0: 73         LD      (HL),E          
58C1: F5         PUSH    AF              
58C2: FE 03      CP      $03             
58C4: 04         INC     B               
58C5: 8A         ADC     A,D             
58C6: 00         NOP                     
58C7: 99         SBC     C               
58C8: 8A         ADC     A,D             
58C9: 10 96      STOP    $96             
58CB: 8A         ADC     A,D             
58CC: 20 93      JR      NZ,$5861        
58CE: 82         ADD     A,D             
58CF: 42         LD      B,D             
58D0: F5         PUSH    AF              
58D1: 39         ADD     HL,SP           
58D2: 44         LD      B,H             
58D3: 8A         ADC     A,D             
58D4: 50         LD      D,B             
58D5: 99         SBC     C               
58D6: 8A         ADC     A,D             
58D7: 60         LD      H,B             
58D8: 0C         INC     C               
58D9: 8A         ADC     A,D             
58DA: 70         LD      (HL),B          
58DB: 0C         INC     C               
58DC: 46         LD      B,(HL)          
58DD: C6 E2      ADD     $E2             
58DF: 1F         RRA                     
58E0: EB                              
58E1: 18 30      JR      $5913           
58E3: FE 03      CP      $03             
58E5: 04         INC     B               
58E6: 86         ADD     A,(HL)          
58E7: 00         NOP                     
58E8: 99         SBC     C               
58E9: 06 9C      LD      B,$9C           
58EB: 82         ADD     A,D             
58EC: 07         RLCA                    
58ED: F5         PUSH    AF              
58EE: 86         ADD     A,(HL)          
58EF: 10 96      STOP    $96             
58F1: C3 16 9A   JP      $9A16           
58F4: 86         ADD     A,(HL)          
58F5: 20 93      JR      NZ,$588A        
58F7: 83         ADD     A,E             
58F8: 27         DAA                     
58F9: 44         LD      B,H             
58FA: 83         ADD     A,E             
58FB: 37         SCF                     
58FC: 44         LD      B,H             
58FD: 28 D3      JR      Z,$58D2         
58FF: 46         LD      B,(HL)          
5900: 9D         SBC     L               
5901: 82         ADD     A,D             
5902: 47         LD      B,A             
5903: 99         SBC     C               
5904: 49         LD      C,C             
5905: 9C         SBC     H               
5906: 50         LD      D,B             
5907: 9C         SBC     H               
5908: 56         LD      D,(HL)          
5909: 97         SUB     A               
590A: 82         ADD     A,D             
590B: 57         LD      D,A             
590C: 96         SUB     (HL)            
590D: C3 59 9A   JP      $9A59           
5910: C2 60 9A   JP      NZ,$9A60        
5913: 61         LD      H,C             
5914: 9C         SBC     H               
5915: 71         LD      (HL),C          
5916: 9A         SBC     D               
5917: 66         LD      H,(HL)          
5918: 94         SUB     H               
5919: 82         ADD     A,D             
591A: 67         LD      H,A             
591B: 93         SUB     E               
591C: E2         LDFF00  (C),A           
591D: 1F         RRA                     
591E: EC                              
591F: 68         LD      L,B             
5920: 30 FE      JR      NC,$5920        
5922: 03         INC     BC              
5923: 04         INC     B               
5924: 0F         RRCA                    
5925: F5         PUSH    AF              
5926: C2 06 0E   JP      NZ,$0E06        
5929: C8         RET     Z               
592A: 07         RLCA                    
592B: 0E 08      LD      C,$08           
592D: 39         ADD     HL,SP           
592E: C7         RST     0X00            
592F: 18 0E      JR      $593F           
5931: C8         RET     Z               
5932: 09         ADD     HL,BC           
5933: 37         SCF                     
5934: C2 40 F5   JP      NZ,$F540        
5937: 03         INC     BC              
5938: F5         PUSH    AF              
5939: 04         INC     B               
593A: F5         PUSH    AF              
593B: 14         INC     D               
593C: E1         POP     HL              
593D: 04         INC     B               
593E: 45         LD      B,L             
593F: E1         POP     HL              
5940: 10 CC      STOP    $CC             
5942: 50         LD      D,B             
5943: 7C         LD      A,H             
5944: C8         RET     Z               
5945: 06 38      LD      B,$38           
5947: FE 0A      CP      $0A             
5949: EB                              
594A: C8         RET     Z               
594B: 00         NOP                     
594C: 38 01      JR      C,$594F         
594E: 3F         CCF                     
594F: 11 3B 83   LD      DE,$833B        
5952: 02         LD      (BC),A          
5953: E9         JP      (HL)            
5954: 83         ADD     A,E             
5955: 12         LD      (DE),A          
5956: E9         JP      (HL)            
5957: C2 05 3A   JP      NZ,$3A05        
595A: C2 06 3E   JP      NZ,$3E06        
595D: 26 39      LD      H,$39           
595F: 83         ADD     A,E             
5960: 07         RLCA                    
5961: 3A         LD      A,(HLD)         
5962: 83         ADD     A,E             
5963: 17         RLA                     
5964: 3A         LD      A,(HLD)         
5965: 83         ADD     A,E             
5966: 27         DAA                     
5967: 3A         LD      A,(HLD)         
5968: C4 21 ED   CALL    NZ,$ED21        
596B: 52         LD      D,D             
596C: ED                              
596D: 82         ADD     A,D             
596E: 24         INC     H               
596F: ED                              
5970: 46         LD      B,(HL)          
5971: ED                              
5972: 47         LD      B,A             
5973: C8         RET     Z               
5974: 82         ADD     A,D             
5975: 61         LD      H,C             
5976: E9         JP      (HL)            
5977: 82         ADD     A,D             
5978: 71         LD      (HL),C          
5979: E9         JP      (HL)            
597A: 82         ADD     A,D             
597B: 67         LD      H,A             
597C: E9         JP      (HL)            
597D: 82         ADD     A,D             
597E: 77         LD      (HL),A          
597F: E9         JP      (HL)            
5980: 63         LD      H,E             
5981: 2B         DEC     HL              
5982: 69         LD      L,C             
5983: 2B         DEC     HL              
5984: 73         LD      (HL),E          
5985: 2E 79      LD      L,$79           
5987: 2E 82      LD      L,$82           
5989: 64         LD      H,H             
598A: 2C         INC     L               
598B: 66         LD      H,(HL)          
598C: 2D         DEC     L               
598D: 82         ADD     A,D             
598E: 74         LD      (HL),H          
598F: 2F         CPL                     
5990: 76         HALT                    
5991: 4E         LD      C,(HL)          
5992: C2 22 ED   JP      NZ,$ED22        
5995: FE 0A      CP      $0A             
5997: EB                              
5998: C3 00 3A   JP      $3A00           
599B: C2 01 3F   JP      NZ,$3F01        
599E: 02         LD      (BC),A          
599F: 3B         DEC     SP              
59A0: C2 02 3A   JP      NZ,$3A02        
59A3: 85         ADD     A,L             
59A4: 05         DEC     B               
59A5: 3A         LD      A,(HLD)         
59A6: 85         ADD     A,L             
59A7: 15         DEC     D               
59A8: 3A         LD      A,(HLD)         
59A9: 82         ADD     A,D             
59AA: 03         INC     BC              
59AB: E9         JP      (HL)            
59AC: 82         ADD     A,D             
59AD: 13         INC     DE              
59AE: E9         JP      (HL)            
59AF: 31 ED 32   LD      SP,$32ED        
59B2: C8         RET     Z               
59B3: C2 25 ED   JP      NZ,$ED25        
59B6: 46         LD      B,(HL)          
59B7: ED                              
59B8: 58         LD      E,B             
59B9: ED                              
59BA: 17         RLA                     
59BB: 21 18 4F   LD      HL,$4F18        
59BE: 26 B6      LD      H,$B6           
59C0: 27         DAA                     
59C1: 4F         LD      C,A             
59C2: 28 21      JR      Z,$59E5         
59C4: 29         ADD     HL,HL           
59C5: B7         OR      A               
59C6: 36 CD      LD      (HL),$CD        
59C8: 37         SCF                     
59C9: 21 38 4F   LD      HL,$4F38        
59CC: 39         ADD     HL,SP           
59CD: CE 47      ADC     $47             
59CF: CD 48 CE   CALL    $CE48           
59D2: 60         LD      H,B             
59D3: 2C         INC     L               
59D4: 61         LD      H,C             
59D5: 2D         DEC     L               
59D6: 70         LD      (HL),B          
59D7: 2F         CPL                     
59D8: 71         LD      (HL),C          
59D9: 4E         LD      C,(HL)          
59DA: 21 3B 62   LD      HL,$623B        
59DD: FB         EI                      
59DE: 64         LD      H,H             
59DF: FB         EI                      
59E0: 66         LD      H,(HL)          
59E1: FB         EI                      
59E2: 78         LD      A,B             
59E3: B6         OR      (HL)            
59E4: 79         LD      A,C             
59E5: B7         OR      A               
59E6: FE 09      CP      $09             
59E8: EB                              
59E9: 8A         ADC     A,D             
59EA: 00         NOP                     
59EB: 3A         LD      A,(HLD)         
59EC: 8A         ADC     A,D             
59ED: 10 3A      STOP    $3A             
59EF: 20 FB      JR      NZ,$59EC        
59F1: C4 24 ED   CALL    NZ,$ED24        
59F4: 45         LD      B,L             
59F5: FB         EI                      
59F6: 47         LD      B,A             
59F7: FB         EI                      
59F8: 49         LD      C,C             
59F9: B6         OR      (HL)            
59FA: 59         LD      E,C             
59FB: CD 70 FB   CALL    $FB70           
59FE: 72         LD      (HL),D          
59FF: FB         EI                      
5A00: 74         LD      (HL),H          
5A01: C8         RET     Z               
5A02: 75         LD      (HL),L          
5A03: FB         EI                      
5A04: 77         LD      (HL),A          
5A05: FB         EI                      
5A06: 79         LD      A,C             
5A07: B6         OR      (HL)            
5A08: C2 24 EB   JP      NZ,$EB24        
5A0B: FE 09      CP      $09             
5A0D: ED                              
5A0E: 89         ADC     A,C             
5A0F: 00         NOP                     
5A10: 3A         LD      A,(HLD)         
5A11: 89         ADC     A,C             
5A12: 10 3A      STOP    $3A             
5A14: C2 09 3F   JP      NZ,$3F09        
5A17: C6 29      ADD     $29             
5A19: 38 87      JR      C,$59A2         
5A1B: 20 EB      JR      NZ,$5A08        
5A1D: 85         ADD     A,L             
5A1E: 30 EB      JR      NC,$5A0B        
5A20: 37         SCF                     
5A21: EB                              
5A22: 82         ADD     A,D             
5A23: 45         LD      B,L             
5A24: EE 82      XOR     $82             
5A26: 57         LD      D,A             
5A27: EE 36      XOR     $36             
5A29: C8         RET     Z               
5A2A: 47         LD      B,A             
5A2B: C8         RET     Z               
5A2C: 55         LD      D,L             
5A2D: C8         RET     Z               
5A2E: 66         LD      H,(HL)          
5A2F: C8         RET     Z               
5A30: 56         LD      D,(HL)          
5A31: EC                              
5A32: 40         LD      B,B             
5A33: B7         OR      A               
5A34: 50         LD      D,B             
5A35: CE 70      ADC     $70             
5A37: B7         OR      A               
5A38: 41         LD      B,C             
5A39: FB         EI                      
5A3A: 60         LD      H,B             
5A3B: EB                              
5A3C: FE 03      CP      $03             
5A3E: 04         INC     B               
5A3F: C8         RET     Z               
5A40: 00         NOP                     
5A41: 37         SCF                     
5A42: C5         PUSH    BC              
5A43: 01 87 C3   LD      BC,$C387        
5A46: 05         DEC     B               
5A47: 0A         LD      A,(BC)          
5A48: C2 06 86   JP      NZ,$8606        
5A4B: 07         RLCA                    
5A4C: 88         ADC     A,B             
5A4D: 08 92 09   LD      ($0992),SP      
5A50: 89         ADC     A,C             
5A51: 17         RLA                     
5A52: 87         ADD     A,A             
5A53: 18 E4      JR      $5A39           
5A55: C6 19      ADD     $19             
5A57: 86         ADD     A,(HL)          
5A58: C3 23 5C   JP      $5C23           
5A5B: 26 8D      LD      H,$8D           
5A5D: 27         DAA                     
5A5E: 8C         ADC     A,H             
5A5F: 83         ADD     A,E             
5A60: 36 0A      LD      (HL),$0A        
5A62: 51         LD      D,C             
5A63: 8A         ADC     A,D             
5A64: 52         LD      D,D             
5A65: 85         ADD     A,L             
5A66: 53         LD      D,E             
5A67: 8E         ADC     A,(HL)          
5A68: 82         ADD     A,D             
5A69: 61         LD      H,C             
5A6A: 90         SUB     B               
5A6B: 63         LD      H,E             
5A6C: 87         ADD     A,A             
5A6D: 82         ADD     A,D             
5A6E: 71         LD      (HL),C          
5A6F: 90         SUB     B               
5A70: 73         LD      (HL),E          
5A71: 8A         ADC     A,D             
5A72: 85         ADD     A,L             
5A73: 74         LD      (HL),H          
5A74: 85         ADD     A,L             
5A75: 79         LD      A,C             
5A76: 8B         ADC     A,E             
5A77: 61         LD      H,C             
5A78: F5         PUSH    AF              
5A79: 12         LD      (DE),A          
5A7A: 08 42 08   LD      ($0842),SP      
5A7D: 64         LD      H,H             
5A7E: 08 34 44   LD      ($4434),SP      
5A81: 45         LD      B,L             
5A82: 44         LD      B,H             
5A83: 58         LD      E,B             
5A84: 44         LD      B,H             
5A85: 28 E3      JR      Z,$5A6A         
5A87: E1         POP     HL              
5A88: 0A         LD      A,(BC)          
5A89: AB         XOR     E               
5A8A: 50         LD      D,B             
5A8B: 7C         LD      A,H             
5A8C: FE 03      CP      $03             
5A8E: 04         INC     B               
5A8F: 00         NOP                     
5A90: 90         SUB     B               
5A91: 01 88 02   LD      BC,$0288        
5A94: 8C         ADC     A,H             
5A95: C2 06 0A   JP      NZ,$0A06        
5A98: 07         RLCA                    
5A99: 86         ADD     A,(HL)          
5A9A: 08 90 C8   LD      ($C890),SP      
5A9D: 09         ADD     HL,BC           
5A9E: 90         SUB     B               
5A9F: C5         PUSH    BC              
5AA0: F9         LD      SP,HL           
5AA1: F5         PUSH    AF              
5AA2: 10 88      STOP    $88             
5AA4: 11 8C 17   LD      DE,$178C        
5AA7: 8D         ADC     A,L             
5AA8: 18 89      JR      $5A33           
5AAA: C5         PUSH    BC              
5AAB: 20 87      JR      NZ,$5A34        
5AAD: 21 08 82   LD      HL,$8208        
5AB0: 23         INC     HL              
5AB1: 5C         LD      E,H             
5AB2: 27         DAA                     
5AB3: 44         LD      B,H             
5AB4: C4 28 86   CALL    NZ,$8628        
5AB7: C2 32 5C   JP      NZ,$5C32        
5ABA: 33         INC     SP              
5ABB: F5         PUSH    AF              
5ABC: C2 35 5C   JP      NZ,$5C35        
5ABF: 36 44      LD      (HL),$44        
5AC1: C3 37 0A   JP      $0A37           
5AC4: 82         ADD     A,D             
5AC5: 53         LD      D,E             
5AC6: 5C         LD      E,H             
5AC7: C2 56 0A   JP      NZ,$0A56        
5ACA: 63         LD      H,E             
5ACB: 44         LD      B,H             
5ACC: 64         LD      H,H             
5ACD: 08 67 8F   LD      ($8F67),SP      
5AD0: 68         LD      L,B             
5AD1: 8B         ADC     A,E             
5AD2: 70         LD      (HL),B          
5AD3: 8A         ADC     A,D             
5AD4: 71         LD      (HL),C          
5AD5: 85         ADD     A,L             
5AD6: 72         LD      (HL),D          
5AD7: 8E         ADC     A,(HL)          
5AD8: 82         ADD     A,D             
5AD9: 75         LD      (HL),L          
5ADA: 0A         LD      A,(BC)          
5ADB: 77         LD      (HL),A          
5ADC: 86         ADD     A,(HL)          
5ADD: 78         LD      A,B             
5ADE: 90         SUB     B               
5ADF: FE 03      CP      $03             
5AE1: 04         INC     B               
5AE2: 83         ADD     A,E             
5AE3: 07         RLCA                    
5AE4: 90         SUB     B               
5AE5: C8         RET     Z               
5AE6: 00         NOP                     
5AE7: 90         SUB     B               
5AE8: C8         RET     Z               
5AE9: 01 87 06   LD      BC,$0687        
5AEC: 86         ADD     A,(HL)          
5AED: C5         PUSH    BC              
5AEE: FF         RST     0X38            
5AEF: F5         PUSH    AF              
5AF0: 82         ADD     A,D             
5AF1: F7         RST     0X30            
5AF2: F5         PUSH    AF              
5AF3: C4 19 90   CALL    NZ,$9019        
5AF6: C2 19 F5   JP      NZ,$F519        
5AF9: C3 28 86   JP      $8628           
5AFC: 85         ADD     A,L             
5AFD: 75         LD      (HL),L          
5AFE: 85         ADD     A,L             
5AFF: 73         LD      (HL),E          
5B00: 8F         ADC     A,A             
5B01: 58         LD      E,B             
5B02: 8D         ADC     A,L             
5B03: 59         LD      E,C             
5B04: 84         ADD     A,H             
5B05: 16 8D      LD      D,$8D           
5B07: 17         RLA                     
5B08: 84         ADD     A,H             
5B09: 18 89      JR      $5A94           
5B0B: C2 05 0A   JP      NZ,$0A05        
5B0E: 26 0A      LD      H,$0A           
5B10: C2 52 0A   JP      NZ,$0A52        
5B13: C2 63 0A   JP      NZ,$0A63        
5B16: 24         INC     H               
5B17: 08 27 08   LD      ($0827),SP      
5B1A: 56         LD      D,(HL)          
5B1B: 08 69 08   LD      ($0869),SP      
5B1E: 72         LD      (HL),D          
5B1F: 08 75 8F   LD      ($8F75),SP      
5B22: 83         ADD     A,E             
5B23: 33         INC     SP              
5B24: 44         LD      B,H             
5B25: 83         ADD     A,E             
5B26: 43         LD      B,E             
5B27: 44         LD      B,H             
5B28: 83         ADD     A,E             
5B29: 53         LD      D,E             
5B2A: 44         LD      B,H             
5B2B: 27         DAA                     
5B2C: 20 E1      JR      NZ,$5B0F        
5B2E: 1F         RRA                     
5B2F: E1         POP     HL              
5B30: 88         ADC     A,B             
5B31: 50         LD      D,B             
5B32: FE 03      CP      $03             
5B34: 0A         LD      A,(BC)          
5B35: 8A         ADC     A,D             
5B36: 00         NOP                     
5B37: 90         SUB     B               
5B38: 86         ADD     A,(HL)          
5B39: FF         RST     0X38            
5B3A: F5         PUSH    AF              
5B3B: C4 10 90   CALL    NZ,$9010        
5B3E: C2 1F F5   JP      NZ,$F51F        
5B41: C7         RST     0X00            
5B42: 19         ADD     HL,DE           
5B43: 90         SUB     B               
5B44: C4 19 F5   CALL    NZ,$F519        
5B47: C3 21 87   JP      $8721           
5B4A: 86         ADD     A,(HL)          
5B4B: 12         LD      (DE),A          
5B4C: 84         ADD     A,H             
5B4D: C6 28      ADD     $28             
5B4F: 86         ADD     A,(HL)          
5B50: 82         ADD     A,D             
5B51: 70         LD      (HL),B          
5B52: 85         ADD     A,L             
5B53: 72         LD      (HL),D          
5B54: 8E         ADC     A,(HL)          
5B55: 51         LD      D,C             
5B56: 8C         ADC     A,H             
5B57: 50         LD      D,B             
5B58: 84         ADD     A,H             
5B59: 11 88 18   LD      DE,$1888        
5B5C: 89         ADC     A,C             
5B5D: 82         ADD     A,D             
5B5E: 61         LD      H,C             
5B5F: 04         INC     B               
5B60: 67         LD      H,A             
5B61: 04         INC     B               
5B62: 76         HALT                    
5B63: 04         INC     B               
5B64: 60         LD      H,B             
5B65: 08 77 8F   LD      ($8F77),SP      
5B68: 78         LD      A,B             
5B69: 8B         ADC     A,E             
5B6A: 23         INC     HL              
5B6B: 3D         DEC     A               
5B6C: 82         ADD     A,D             
5B6D: 24         INC     H               
5B6E: 2F         CPL                     
5B6F: 26 3C      LD      H,$3C           
5B71: 33         INC     SP              
5B72: 38 82      JR      C,$5AF6         
5B74: 34         INC     (HL)            
5B75: 0E 36      LD      C,$36           
5B77: 37         SCF                     
5B78: 43         LD      B,E             
5B79: 32         LD      (HLD),A         
5B7A: 82         ADD     A,D             
5B7B: 44         LD      B,H             
5B7C: 2C         INC     L               
5B7D: 46         LD      B,(HL)          
5B7E: 31 FE 03   LD      SP,$03FE        
5B81: 04         INC     B               
5B82: C5         PUSH    BC              
5B83: FF         RST     0X38            
5B84: F5         PUSH    AF              
5B85: 60         LD      H,B             
5B86: F5         PUSH    AF              
5B87: 85         ADD     A,L             
5B88: 71         LD      (HL),C          
5B89: F5         PUSH    AF              
5B8A: 21 3D 83   LD      HL,$833D        
5B8D: 22         LD      (HLI),A         
5B8E: 2F         CPL                     
5B8F: 25         DEC     H               
5B90: 3C         INC     A               
5B91: C2 31 38   JP      NZ,$3831        
5B94: 51         LD      D,C             
5B95: 32         LD      (HLD),A         
5B96: 52         LD      D,D             
5B97: 2D         DEC     L               
5B98: 62         LD      H,D             
5B99: 32         LD      (HLD),A         
5B9A: 82         ADD     A,D             
5B9B: 63         LD      H,E             
5B9C: 2C         INC     L               
5B9D: 25         DEC     H               
5B9E: 3C         INC     A               
5B9F: C3 35 37   JP      $3735           
5BA2: 65         LD      H,L             
5BA3: 31 83 32   LD      SP,$3283        
5BA6: 0E 83      LD      C,$83           
5BA8: 42         LD      B,D             
5BA9: 0E 82      LD      C,$82           
5BAB: 53         LD      D,E             
5BAC: 0E 02      LD      C,$02           
5BAE: 0B         DEC     BC              
5BAF: 86         ADD     A,(HL)          
5BB0: 12         LD      (DE),A          
5BB1: 0B         DEC     BC              
5BB2: C4 F9 F5   CALL    NZ,$F5F9        
5BB5: 84         ADD     A,H             
5BB6: 75         LD      (HL),L          
5BB7: 04         INC     B               
5BB8: C6 27      ADD     $27             
5BBA: 0B         DEC     BC              
5BBB: FE 03      CP      $03             
5BBD: 04         INC     B               
5BBE: 86         ADD     A,(HL)          
5BBF: 7F         LD      A,A             
5BC0: F5         PUSH    AF              
5BC1: C4 FF F5   CALL    NZ,$F5FF        
5BC4: 60         LD      H,B             
5BC5: F5         PUSH    AF              
5BC6: 82         ADD     A,D             
5BC7: 14         INC     D               
5BC8: 09         ADD     HL,BC           
5BC9: 84         ADD     A,H             
5BCA: 41         LD      B,C             
5BCB: 09         ADD     HL,BC           
5BCC: 82         ADD     A,D             
5BCD: 52         LD      D,D             
5BCE: 09         ADD     HL,BC           
5BCF: 02         LD      (BC),A          
5BD0: 44         LD      B,H             
5BD1: 59         LD      E,C             
5BD2: 09         ADD     HL,BC           
5BD3: 82         ADD     A,D             
5BD4: 67         LD      H,A             
5BD5: 09         ADD     HL,BC           
5BD6: 62         LD      H,D             
5BD7: E8 82      ADD     SP,$82          
5BD9: 45         LD      B,L             
5BDA: 03         INC     BC              
5BDB: 54         LD      D,H             
5BDC: 03         INC     BC              
5BDD: 83         ADD     A,E             
5BDE: 63         LD      H,E             
5BDF: 03         INC     BC              
5BE0: 26 F5      LD      H,$F5           
5BE2: 32         LD      (HLD),A         
5BE3: F5         PUSH    AF              
5BE4: 38 F5      JR      C,$5BDB         
5BE6: C2 F9 F5   JP      NZ,$F5F9        
5BE9: 11 F5 24   LD      DE,$24F5        
5BEC: 20 35      JR      NZ,$5C23        
5BEE: 20 82      JR      NZ,$5B72        
5BF0: 77         LD      (HL),A          
5BF1: 04         INC     B               
5BF2: FE 03      CP      $03             
5BF4: 04         INC     B               
5BF5: 01 09 05   LD      BC,$0509        
5BF8: CD 06 CE   CALL    $CE06           
5BFB: 82         ADD     A,D             
5BFC: 02         LD      (BC),A          
5BFD: 03         INC     BC              
5BFE: 08 09 09   LD      ($0909),SP      
5C01: CD 16 FB   CALL    $FB16           
5C04: 19         ADD     HL,DE           
5C05: 09         ADD     HL,BC           
5C06: 22         LD      (HLI),A         
5C07: FB         EI                      
5C08: 30 FB      JR      NC,$5C05        
5C0A: 34         INC     (HL)            
5C0B: FB         EI                      
5C0C: 36 E8      LD      (HL),$E8        
5C0E: 42         LD      B,D             
5C0F: 09         ADD     HL,BC           
5C10: 43         LD      B,E             
5C11: E8 82      ADD     SP,$82          
5C13: 50         LD      D,B             
5C14: 09         ADD     HL,BC           
5C15: 82         ADD     A,D             
5C16: 52         LD      D,D             
5C17: 03         INC     BC              
5C18: 82         ADD     A,D             
5C19: 56         LD      D,(HL)          
5C1A: 09         ADD     HL,BC           
5C1B: 58         LD      E,B             
5C1C: 03         INC     BC              
5C1D: 82         ADD     A,D             
5C1E: 60         LD      H,B             
5C1F: 03         INC     BC              
5C20: 82         ADD     A,D             
5C21: 63         LD      H,E             
5C22: 09         ADD     HL,BC           
5C23: 83         ADD     A,E             
5C24: 46         LD      B,(HL)          
5C25: 03         INC     BC              
5C26: 86         ADD     A,(HL)          
5C27: 7F         LD      A,A             
5C28: F5         PUSH    AF              
5C29: 59         LD      E,C             
5C2A: FB         EI                      
5C2B: C2 FF F5   JP      NZ,$F5FF        
5C2E: FE 03      CP      $03             
5C30: 04         INC     B               
5C31: C4 08 F5   CALL    NZ,$F508        
5C34: 85         ADD     A,L             
5C35: 7F         LD      A,A             
5C36: F5         PUSH    AF              
5C37: 82         ADD     A,D             
5C38: 73         LD      (HL),E          
5C39: 04         INC     B               
5C3A: 00         NOP                     
5C3B: CE 83      ADC     $83             
5C3D: 04         INC     B               
5C3E: 03         INC     BC              
5C3F: 82         ADD     A,D             
5C40: 10 09      STOP    $09             
5C42: 13         INC     DE              
5C43: 03         INC     BC              
5C44: 14         INC     D               
5C45: 09         ADD     HL,BC           
5C46: 82         ADD     A,D             
5C47: 16 03      LD      D,$03           
5C49: 21 03 22   LD      HL,$2203        
5C4C: FB         EI                      
5C4D: 82         ADD     A,D             
5C4E: 25         DEC     H               
5C4F: 03         INC     BC              
5C50: 27         DAA                     
5C51: 09         ADD     HL,BC           
5C52: 82         ADD     A,D             
5C53: 42         LD      B,D             
5C54: 09         ADD     HL,BC           
5C55: 44         LD      B,H             
5C56: 03         INC     BC              
5C57: 45         LD      B,L             
5C58: FB         EI                      
5C59: 4F         LD      C,A             
5C5A: FB         EI                      
5C5B: 51         LD      D,C             
5C5C: 09         ADD     HL,BC           
5C5D: 82         ADD     A,D             
5C5E: 52         LD      D,D             
5C5F: 03         INC     BC              
5C60: 54         LD      D,H             
5C61: 09         ADD     HL,BC           
5C62: 57         LD      D,A             
5C63: 09         ADD     HL,BC           
5C64: 62         LD      H,D             
5C65: 09         ADD     HL,BC           
5C66: 63         LD      H,E             
5C67: 03         INC     BC              
5C68: 82         ADD     A,D             
5C69: 66         LD      H,(HL)          
5C6A: 03         INC     BC              
5C6B: 82         ADD     A,D             
5C6C: 34         INC     (HL)            
5C6D: 03         INC     BC              
5C6E: 61         LD      H,C             
5C6F: 03         INC     BC              
5C70: FE 03      CP      $03             
5C72: 04         INC     B               
5C73: C8         RET     Z               
5C74: 00         NOP                     
5C75: 38 C8      JR      C,$5C3F         
5C77: 01 0E C2   LD      BC,$C20E        
5C7A: 62         LD      H,D             
5C7B: 0E C3      LD      C,$C3           
5C7D: 02         LD      (BC),A          
5C7E: 9A         SBC     D               
5C7F: C4 43 9A   CALL    NZ,$9A43        
5C82: C7         RST     0X00            
5C83: 08 9A 09   LD      ($099A),SP      
5C86: 9D         SBC     L               
5C87: 32         LD      (HLD),A         
5C88: 9D         SBC     L               
5C89: 78         LD      A,B             
5C8A: 9D         SBC     L               
5C8B: 33         INC     SP              
5C8C: 9C         SBC     H               
5C8D: 42         LD      B,D             
5C8E: 97         SUB     A               
5C8F: 52         LD      D,D             
5C90: 94         SUB     H               
5C91: 19         ADD     HL,DE           
5C92: 97         SUB     A               
5C93: 29         ADD     HL,HL           
5C94: 94         SUB     H               
5C95: C2 F3 F5   JP      NZ,$F5F3        
5C98: 76         HALT                    
5C99: F5         PUSH    AF              
5C9A: 35         DEC     (HL)            
5C9B: 44         LD      B,H             
5C9C: 64         LD      H,H             
5C9D: 44         LD      B,H             
5C9E: C4 39 0D   CALL    NZ,$0D39        
5CA1: 79         LD      A,C             
5CA2: 99         SBC     C               
5CA3: C2 57 20   JP      NZ,$2057        
5CA6: FE 03      CP      $03             
5CA8: 0D         DEC     C               
5CA9: 8A         ADC     A,D             
5CAA: 00         NOP                     
5CAB: 99         SBC     C               
5CAC: 03         INC     BC              
5CAD: 9C         SBC     H               
5CAE: 83         ADD     A,E             
5CAF: 04         INC     B               
5CB0: 0C         INC     C               
5CB1: 07         RLCA                    
5CB2: 9B         SBC     E               
5CB3: 10 F9      STOP    $F9             
5CB5: E1         POP     HL              
5CB6: 14         INC     D               
5CB7: D5         PUSH    DE              
5CB8: 50         LD      D,B             
5CB9: 7C         LD      A,H             
5CBA: 13         INC     DE              
5CBB: 9D         SBC     L               
5CBC: 83         ADD     A,E             
5CBD: 14         INC     D               
5CBE: 99         SBC     C               
5CBF: 17         RLA                     
5CC0: 9E         SBC     (HL)            
5CC1: 82         ADD     A,D             
5CC2: 18 96      JR      $5C5A           
5CC4: 23         INC     HL              
5CC5: B7         OR      A               
5CC6: 24         INC     H               
5CC7: F9         LD      SP,HL           
5CC8: E1         POP     HL              
5CC9: 14         INC     D               
5CCA: D6 50      SUB     $50             
5CCC: 7C         LD      A,H             
5CCD: 27         DAA                     
5CCE: B7         OR      A               
5CCF: 82         ADD     A,D             
5CD0: 28 93      JR      Z,$5C65         
5CD2: 33         INC     SP              
5CD3: A2         AND     D               
5CD4: 37         SCF                     
5CD5: A2         AND     D               
5CD6: 43         LD      B,E             
5CD7: B6         OR      (HL)            
5CD8: 47         LD      B,A             
5CD9: B6         OR      (HL)            
5CDA: 83         ADD     A,E             
5CDB: 70         LD      (HL),B          
5CDC: 99         SBC     C               
5CDD: 82         ADD     A,D             
5CDE: 78         LD      A,B             
5CDF: 99         SBC     C               
5CE0: 73         LD      (HL),E          
5CE1: 9C         SBC     H               
5CE2: 77         LD      (HL),A          
5CE3: 9B         SBC     E               
5CE4: FE 03      CP      $03             
5CE6: 04         INC     B               
5CE7: 00         NOP                     
5CE8: 9E         SBC     (HL)            
5CE9: C7         RST     0X00            
5CEA: 01 9A C7   LD      BC,$C79A        
5CED: 09         ADD     HL,BC           
5CEE: 9A         SBC     D               
5CEF: 10 98      STOP    $98             
5CF1: 20 95      JR      NZ,$5C88        
5CF3: C4 30 0D   CALL    NZ,$0D30        
5CF6: 70         LD      (HL),B          
5CF7: 99         SBC     C               
5CF8: 71         LD      (HL),C          
5CF9: 9E         SBC     (HL)            
5CFA: 77         LD      (HL),A          
5CFB: 9B         SBC     E               
5CFC: 78         LD      A,B             
5CFD: 99         SBC     C               
5CFE: 79         LD      A,C             
5CFF: 9E         SBC     (HL)            
5D00: 15         DEC     D               
5D01: E8 32      ADD     SP,$32          
5D03: E8 38      ADD     SP,$38          
5D05: E8 45      ADD     SP,$45          
5D07: E8 63      ADD     SP,$63          
5D09: E8 67      ADD     SP,$67          
5D0B: E8 72      ADD     SP,$72          
5D0D: F5         PUSH    AF              
5D0E: FE 03      CP      $03             
5D10: 04         INC     B               
5D11: C8         RET     Z               
5D12: 09         ADD     HL,BC           
5D13: 37         SCF                     
5D14: C2 06 38   JP      NZ,$3806        
5D17: C3 34 38   JP      $3834           
5D1A: 24         INC     H               
5D1B: 3D         DEC     A               
5D1C: 25         DEC     H               
5D1D: 2F         CPL                     
5D1E: 26 34      LD      H,$34           
5D20: 83         ADD     A,E             
5D21: 34         INC     (HL)            
5D22: 38 64      JR      C,$5D88         
5D24: 32         LD      (HLD),A         
5D25: 65         LD      H,L             
5D26: 2C         INC     L               
5D27: 66         LD      H,(HL)          
5D28: 2D         DEC     L               
5D29: 67         LD      H,A             
5D2A: 38 C8      JR      C,$5CF4         
5D2C: 07         RLCA                    
5D2D: 0E C8      LD      C,$C8           
5D2F: 08 0E C3   LD      ($C30E),SP      
5D32: 35         DEC     (HL)            
5D33: 0E C3      LD      C,$C3           
5D35: 36 0E      LD      (HL),$0E        
5D37: 13         INC     DE              
5D38: 44         LD      B,H             
5D39: 75         LD      (HL),L          
5D3A: 44         LD      B,H             
5D3B: 76         HALT                    
5D3C: 38 C4      JR      C,$5D02         
5D3E: 00         NOP                     
5D3F: F5         PUSH    AF              
5D40: 74         LD      (HL),H          
5D41: F5         PUSH    AF              
5D42: FE 0A      CP      $0A             
5D44: EB                              
5D45: C8         RET     Z               
5D46: 00         NOP                     
5D47: 38 03      JR      C,$5D4C         
5D49: 3E 82      LD      A,$82           
5D4B: 04         INC     B               
5D4C: 3A         LD      A,(HLD)         
5D4D: 06 3F      LD      B,$3F           
5D4F: C3 13 37   JP      $3713           
5D52: C3 16 38   JP      $3816           
5D55: 43         LD      B,E             
5D56: 33         INC     SP              
5D57: 44         LD      B,H             
5D58: 48         LD      C,B             
5D59: 45         LD      B,L             
5D5A: E0 46      LDFF00  ($46),A         
5D5C: 34         INC     (HL)            
5D5D: C3 14 04   JP      $0414           
5D60: C3 15 04   JP      $0415           
5D63: 82         ADD     A,D             
5D64: 01 E9 82   LD      BC,$82E9        
5D67: 07         RLCA                    
5D68: E9         JP      (HL)            
5D69: 09         ADD     HL,BC           
5D6A: 39         ADD     HL,SP           
5D6B: C5         PUSH    BC              
5D6C: 11 ED C5   LD      DE,$C5ED        
5D6F: 12         LD      (DE),A          
5D70: ED                              
5D71: C3 17 ED   JP      $ED17           
5D74: 56         LD      D,(HL)          
5D75: C8         RET     Z               
5D76: 47         LD      B,A             
5D77: C8         RET     Z               
5D78: 24         INC     H               
5D79: A0         AND     B               
5D7A: 68         LD      L,B             
5D7B: FB         EI                      
5D7C: 71         LD      (HL),C          
5D7D: FB         EI                      
5D7E: 73         LD      (HL),E          
5D7F: FB         EI                      
5D80: 75         LD      (HL),L          
5D81: FB         EI                      
5D82: 77         LD      (HL),A          
5D83: FB         EI                      
5D84: 78         LD      A,B             
5D85: 4F         LD      C,A             
5D86: 79         LD      A,C             
5D87: 21 FE 09   LD      HL,$09FE        
5D8A: EB                              
5D8B: 00         NOP                     
5D8C: 3A         LD      A,(HLD)         
5D8D: 01 3B 02   LD      BC,$023B        
5D90: 2B         DEC     HL              
5D91: 84         ADD     A,H             
5D92: 03         INC     BC              
5D93: 2C         INC     L               
5D94: 07         RLCA                    
5D95: 2D         DEC     L               
5D96: 08 CD 09   LD      ($09CD),SP      
5D99: CE 12      ADC     $12             
5D9B: 37         SCF                     
5D9C: 84         ADD     A,H             
5D9D: 13         INC     DE              
5D9E: 04         INC     B               
5D9F: 16 A0      LD      D,$A0           
5DA1: C2 17 38   JP      NZ,$3817        
5DA4: 22         LD      (HLI),A         
5DA5: 33         INC     SP              
5DA6: 23         INC     HL              
5DA7: 3C         INC     A               
5DA8: 83         ADD     A,E             
5DA9: 24         INC     H               
5DAA: 04         INC     B               
5DAB: 33         INC     SP              
5DAC: 33         INC     SP              
5DAD: 34         INC     (HL)            
5DAE: 48         LD      C,B             
5DAF: 35         DEC     (HL)            
5DB0: E0 36      LDFF00  ($36),A         
5DB2: 49         LD      C,C             
5DB3: 37         SCF                     
5DB4: 34         INC     (HL)            
5DB5: C2 11 ED   JP      NZ,$ED11        
5DB8: 32         LD      (HLD),A         
5DB9: ED                              
5DBA: 43         LD      B,E             
5DBB: ED                              
5DBC: 46         LD      B,(HL)          
5DBD: C8         RET     Z               
5DBE: 60         LD      H,B             
5DBF: FB         EI                      
5DC0: 71         LD      (HL),C          
5DC1: FB         EI                      
5DC2: 73         LD      (HL),E          
5DC3: FB         EI                      
5DC4: 75         LD      (HL),L          
5DC5: FB         EI                      
5DC6: 77         LD      (HL),A          
5DC7: FB         EI                      
5DC8: 70         LD      (HL),B          
5DC9: 4F         LD      C,A             
5DCA: 71         LD      (HL),C          
5DCB: 21 79 B6   LD      HL,$B679        
5DCE: 14         INC     D               
5DCF: 6F         LD      L,A             
5DD0: FE 09      CP      $09             
5DD2: EB                              
5DD3: C3 40 EC   JP      $EC40           
5DD6: 41         LD      B,C             
5DD7: 2B         DEC     HL              
5DD8: 42         LD      B,D             
5DD9: 2C         INC     L               
5DDA: 43         LD      B,E             
5DDB: 2C         INC     L               
5DDC: 44         LD      B,H             
5DDD: 2D         DEC     L               
5DDE: C2 51 37   JP      NZ,$3751        
5DE1: C2 54 38   JP      NZ,$3854        
5DE4: 71         LD      (HL),C          
5DE5: 33         INC     SP              
5DE6: 82         ADD     A,D             
5DE7: 72         LD      (HL),D          
5DE8: 2F         CPL                     
5DE9: 74         LD      (HL),H          
5DEA: 34         INC     (HL)            
5DEB: 82         ADD     A,D             
5DEC: 52         LD      D,D             
5DED: 04         INC     B               
5DEE: 82         ADD     A,D             
5DEF: 62         LD      H,D             
5DF0: 04         INC     B               
5DF1: 28 C8      JR      Z,$5DBB         
5DF3: 37         SCF                     
5DF4: C8         RET     Z               
5DF5: 58         LD      E,B             
5DF6: C8         RET     Z               
5DF7: 66         LD      H,(HL)          
5DF8: C8         RET     Z               
5DF9: 27         DAA                     
5DFA: EC                              
5DFB: 31 EC 36   LD      SP,$36EC        
5DFE: EC                              
5DFF: 57         LD      D,A             
5E00: EC                              
5E01: 65         LD      H,L             
5E02: EC                              
5E03: 00         NOP                     
5E04: CD 02 CD   CALL    $CD02           
5E07: 05         DEC     B               
5E08: CD 07 CD   CALL    $CD07           
5E0B: 09         ADD     HL,BC           
5E0C: CD 01 CE   CALL    $CE01           
5E0F: 03         INC     BC              
5E10: CE 06      ADC     $06             
5E12: CE 08      ADC     $08             
5E14: CE 04      ADC     $04             
5E16: C8         RET     Z               
5E17: 70         LD      (HL),B          
5E18: B7         OR      A               
5E19: 75         LD      (HL),L          
5E1A: FB         EI                      
5E1B: 77         LD      (HL),A          
5E1C: FB         EI                      
5E1D: 79         LD      A,C             
5E1E: B6         OR      (HL)            
5E1F: FE 09      CP      $09             
5E21: ED                              
5E22: 00         NOP                     
5E23: CE C6      ADC     $C6             
5E25: 10 EB      STOP    $EB             
5E27: 82         ADD     A,D             
5E28: 31 EB 82   LD      SP,$82EB        
5E2B: 06 EB      LD      B,$EB           
5E2D: 82         ADD     A,D             
5E2E: 46         LD      B,(HL)          
5E2F: EB                              
5E30: 83         ADD     A,E             
5E31: 03         INC     BC              
5E32: EE 82      XOR     $82             
5E34: 37         SCF                     
5E35: EE 43      XOR     $43             
5E37: EE 13      XOR     $13             
5E39: FB         EI                      
5E3A: 15         DEC     D               
5E3B: FB         EI                      
5E3C: 24         INC     H               
5E3D: 21 25 4F   LD      HL,$4F25        
5E40: 34         INC     (HL)            
5E41: CD 35 CE   CALL    $CE35           
5E44: 44         LD      B,H             
5E45: FB         EI                      
5E46: 53         LD      D,E             
5E47: FB         EI                      
5E48: 55         LD      D,L             
5E49: FB         EI                      
5E4A: 54         LD      D,H             
5E4B: 4F         LD      C,A             
5E4C: 55         LD      D,L             
5E4D: 21 64 21   LD      HL,$2164        
5E50: 65         LD      H,L             
5E51: 4F         LD      C,A             
5E52: 74         LD      (HL),H          
5E53: CD 75 CE   CALL    $CE75           
5E56: C2 17 C8   JP      NZ,$C817        
5E59: C2 57 C8   JP      NZ,$C857        
5E5C: C8         RET     Z               
5E5D: 09         ADD     HL,BC           
5E5E: 38 70      JR      C,$5ED0         
5E60: B7         OR      A               
5E61: FE 03      CP      $03             
5E63: 04         INC     B               
5E64: C8         RET     Z               
5E65: 00         NOP                     
5E66: 37         SCF                     
5E67: C8         RET     Z               
5E68: 01 90 C8   LD      BC,$C890        
5E6B: 02         LD      (BC),A          
5E6C: 90         SUB     B               
5E6D: C8         RET     Z               
5E6E: 03         INC     BC              
5E6F: 90         SUB     B               
5E70: C5         PUSH    BC              
5E71: 04         INC     B               
5E72: 87         ADD     A,A             
5E73: 04         INC     B               
5E74: 88         ADC     A,B             
5E75: 85         ADD     A,L             
5E76: 05         DEC     B               
5E77: 84         ADD     A,H             
5E78: 38 8F      JR      C,$5E09         
5E7A: 39         ADD     HL,SP           
5E7B: 85         ADD     A,L             
5E7C: C2 48 86   JP      NZ,$8648        
5E7F: C2 49 90   JP      NZ,$9049        
5E82: 49         LD      C,C             
5E83: F5         PUSH    AF              
5E84: C2 51 F5   JP      NZ,$F551        
5E87: 53         LD      D,E             
5E88: 88         ADC     A,B             
5E89: 54         LD      D,H             
5E8A: 8C         ADC     A,H             
5E8B: C2 63 87   JP      NZ,$8763        
5E8E: 68         LD      L,B             
5E8F: 8D         ADC     A,L             
5E90: 69         LD      L,C             
5E91: 84         ADD     A,H             
5E92: 15         DEC     D               
5E93: 08 36 08   LD      ($0836),SP      
5E96: 65         LD      H,L             
5E97: 08 25 44   LD      ($4425),SP      
5E9A: 29         ADD     HL,HL           
5E9B: 44         LD      B,H             
5E9C: 56         LD      D,(HL)          
5E9D: 44         LD      B,H             
5E9E: C2 01 F5   JP      NZ,$F501        
5EA1: C2 12 F5   JP      NZ,$F512        
5EA4: FE 03      CP      $03             
5EA6: 04         INC     B               
5EA7: 82         ADD     A,D             
5EA8: 00         NOP                     
5EA9: 84         ADD     A,H             
5EAA: 02         LD      (BC),A          
5EAB: 8C         ADC     A,H             
5EAC: C4 07 86   CALL    NZ,$8607        
5EAF: C4 08 90   CALL    NZ,$9008        
5EB2: C4 09 90   CALL    NZ,$9009        
5EB5: C2 11 0A   JP      NZ,$0A11        
5EB8: 13         INC     DE              
5EB9: 08 22 0A   LD      ($0A22),SP      
5EBC: 47         LD      B,A             
5EBD: 8D         ADC     A,L             
5EBE: 82         ADD     A,D             
5EBF: 48         LD      C,B             
5EC0: 84         ADD     A,H             
5EC1: 83         ADD     A,E             
5EC2: 30 85      JR      NC,$5E49        
5EC4: 33         INC     SP              
5EC5: 8E         ADC     A,(HL)          
5EC6: 36 5C      LD      (HL),$5C        
5EC8: 83         ADD     A,E             
5EC9: 40         LD      B,B             
5ECA: 90         SUB     B               
5ECB: C2 43 87   JP      NZ,$8743        
5ECE: 83         ADD     A,E             
5ECF: 50         LD      D,B             
5ED0: 90         SUB     B               
5ED1: 82         ADD     A,D             
5ED2: 4F         LD      C,A             
5ED3: F5         PUSH    AF              
5ED4: 83         ADD     A,E             
5ED5: 60         LD      H,B             
5ED6: 84         ADD     A,H             
5ED7: 63         LD      H,E             
5ED8: 8C         ADC     A,H             
5ED9: 65         LD      H,L             
5EDA: 08 67 8F   LD      ($8F67),SP      
5EDD: 82         ADD     A,D             
5EDE: 68         LD      L,B             
5EDF: 85         ADD     A,L             
5EE0: 77         LD      (HL),A          
5EE1: 86         ADD     A,(HL)          
5EE2: 82         ADD     A,D             
5EE3: 78         LD      A,B             
5EE4: 90         SUB     B               
5EE5: 79         LD      A,C             
5EE6: F5         PUSH    AF              
5EE7: C2 08 F5   JP      NZ,$F508        
5EEA: 19         ADD     HL,DE           
5EEB: F5         PUSH    AF              
5EEC: 44         LD      B,H             
5EED: 44         LD      B,H             
5EEE: 56         LD      D,(HL)          
5EEF: 44         LD      B,H             
5EF0: FE 03      CP      $03             
5EF2: 04         INC     B               
5EF3: C4 00 90   CALL    NZ,$9000        
5EF6: C2 FF F5   JP      NZ,$F5FF        
5EF9: C4 01 87   CALL    NZ,$8701        
5EFC: 84         ADD     A,H             
5EFD: 06 90      LD      B,$90           
5EFF: 84         ADD     A,H             
5F00: 16 90      LD      D,$90           
5F02: 84         ADD     A,H             
5F03: 26 90      LD      H,$90           
5F05: 84         ADD     A,H             
5F06: 36 84      LD      (HL),$84        
5F08: C3 05 86   JP      $8605           
5F0B: 35         DEC     (HL)            
5F0C: 8D         ADC     A,L             
5F0D: 45         LD      B,L             
5F0E: D4 86 74   CALL    NC,$7486        
5F11: 85         ADD     A,L             
5F12: 73         LD      (HL),E          
5F13: 8F         ADC     A,A             
5F14: 16 88      LD      D,$88           
5F16: 17         RLA                     
5F17: 92         SUB     D               
5F18: 18 89      JR      $5EA3           
5F1A: 26 87      LD      H,$87           
5F1C: 27         DAA                     
5F1D: E4                              
5F1E: 28 86      JR      Z,$5EA6         
5F20: 36 8C      LD      (HL),$8C        
5F22: 38 8D      JR      C,$5EB1         
5F24: 37         SCF                     
5F25: E3                              
5F26: E1         POP     HL              
5F27: 0A         LD      A,(BC)          
5F28: BD         CP      L               
5F29: 50         LD      D,B             
5F2A: 7C         LD      A,H             
5F2B: 39         ADD     HL,SP           
5F2C: 89         ADC     A,C             
5F2D: C3 49 86   JP      $8649           
5F30: 40         LD      B,B             
5F31: 84         ADD     A,H             
5F32: 41         LD      B,C             
5F33: 8C         ADC     A,H             
5F34: 60         LD      H,B             
5F35: 85         ADD     A,L             
5F36: 61         LD      H,C             
5F37: 8E         ADC     A,(HL)          
5F38: 70         LD      (HL),B          
5F39: 90         SUB     B               
5F3A: 71         LD      (HL),C          
5F3B: 87         ADD     A,A             
5F3C: 7F         LD      A,A             
5F3D: F5         PUSH    AF              
5F3E: 72         LD      (HL),D          
5F3F: 08 82 65   LD      ($6582),SP      
5F42: 08 58 08   LD      ($0858),SP      
5F45: 79         LD      A,C             
5F46: 8B         ADC     A,E             
5F47: 52         LD      D,D             
5F48: 44         LD      B,H             
5F49: FE 03      CP      $03             
5F4B: 04         INC     B               
5F4C: 86         ADD     A,(HL)          
5F4D: FF         RST     0X38            
5F4E: F5         PUSH    AF              
5F4F: 82         ADD     A,D             
5F50: 00         NOP                     
5F51: F5         PUSH    AF              
5F52: 82         ADD     A,D             
5F53: 1F         RRA                     
5F54: F5         PUSH    AF              
5F55: C3 3F F5   JP      $F53F           
5F58: 82         ADD     A,D             
5F59: 20 F5      JR      NZ,$5F50        
5F5B: 33         INC     SP              
5F5C: F5         PUSH    AF              
5F5D: 44         LD      B,H             
5F5E: F5         PUSH    AF              
5F5F: 55         LD      D,L             
5F60: F5         PUSH    AF              
5F61: C3 18 0B   JP      $0B18           
5F64: 39         ADD     HL,SP           
5F65: 0B         DEC     BC              
5F66: 27         DAA                     
5F67: 08 75 3D   LD      ($3D75),SP      
5F6A: 76         HALT                    
5F6B: 48         LD      C,B             
5F6C: 77         LD      (HL),A          
5F6D: E0 78      LDFF00  ($78),A         
5F6F: 49         LD      C,C             
5F70: 79         LD      A,C             
5F71: 2F         CPL                     
5F72: 84         ADD     A,H             
5F73: 05         DEC     B               
5F74: 04         INC     B               
5F75: 67         LD      H,A             
5F76: 20 C2      JR      NZ,$5F3A        
5F78: 07         RLCA                    
5F79: 0B         DEC     BC              
5F7A: 82         ADD     A,D             
5F7B: 41         LD      B,C             
5F7C: 44         LD      B,H             
5F7D: 83         ADD     A,E             
5F7E: 51         LD      D,C             
5F7F: 44         LD      B,H             
5F80: 83         ADD     A,E             
5F81: 61         LD      H,C             
5F82: 44         LD      B,H             
5F83: 52         LD      D,D             
5F84: C4 FE 03   CALL    NZ,$03FE        
5F87: 04         INC     B               
5F88: 86         ADD     A,(HL)          
5F89: FF         RST     0X38            
5F8A: F5         PUSH    AF              
5F8B: 13         INC     DE              
5F8C: FB         EI                      
5F8D: 14         INC     D               
5F8E: FB         EI                      
5F8F: 14         INC     D               
5F90: C8         RET     Z               
5F91: 24         INC     H               
5F92: E1         POP     HL              
5F93: 32         LD      (HLD),A         
5F94: FB         EI                      
5F95: 35         DEC     (HL)            
5F96: FB         EI                      
5F97: 20 08      JR      NZ,$5FA1        
5F99: 18 08      JR      $5FA3           
5F9B: 86         ADD     A,(HL)          
5F9C: 70         LD      (HL),B          
5F9D: 2F         CPL                     
5F9E: 76         HALT                    
5F9F: 3C         INC     A               
5FA0: 77         LD      (HL),A          
5FA1: 0A         LD      A,(BC)          
5FA2: 30 0B      JR      NC,$5FAF        
5FA4: C3 31 0B   JP      $0B31           
5FA7: 83         ADD     A,E             
5FA8: 52         LD      D,D             
5FA9: 0B         DEC     BC              
5FAA: C2 34 0B   JP      NZ,$0B34        
5FAD: C2 19 F5   JP      NZ,$F519        
5FB0: 28 F5      JR      Z,$5FA7         
5FB2: 47         LD      B,A             
5FB3: 20 C2      JR      NZ,$5F77        
5FB5: 56         LD      D,(HL)          
5FB6: E8 79      ADD     SP,$79          
5FB8: F5         PUSH    AF              
5FB9: 48         LD      C,B             
5FBA: D4 E1 0E   CALL    NC,$0EE1        
5FBD: A2         AND     D               
5FBE: 50         LD      D,B             
5FBF: 7C         LD      A,H             
5FC0: 82         ADD     A,D             
5FC1: 07         RLCA                    
5FC2: 04         INC     B               
5FC3: FE 03      CP      $03             
5FC5: 0A         LD      A,(BC)          
5FC6: 8A         ADC     A,D             
5FC7: 00         NOP                     
5FC8: 04         INC     B               
5FC9: C7         RST     0X00            
5FCA: 10 04      STOP    $04             
5FCC: 86         ADD     A,(HL)          
5FCD: FF         RST     0X38            
5FCE: F5         PUSH    AF              
5FCF: C2 1F F5   JP      NZ,$F51F        
5FD2: 89         ADC     A,C             
5FD3: 11 51 C6   LD      DE,$C651        
5FD6: 21 51 85   LD      HL,$8551        
5FD9: 22         LD      (HLI),A         
5FDA: 09         ADD     HL,BC           
5FDB: 33         INC     SP              
5FDC: C4 34 03   CALL    NZ,$0334        
5FDF: 35         DEC     (HL)            
5FE0: C4 37 C4   CALL    NZ,$C437        
5FE3: 38 03      JR      C,$5FE8         
5FE5: 45         LD      B,L             
5FE6: 09         ADD     HL,BC           
5FE7: 46         LD      B,(HL)          
5FE8: 03         INC     BC              
5FE9: C2 51 04   JP      NZ,$0451        
5FEC: 53         LD      D,E             
5FED: C4 54 03   CALL    NZ,$0354        
5FF0: 55         LD      D,L             
5FF1: C4 57 C4   CALL    NZ,$C457        
5FF4: 82         ADD     A,D             
5FF5: 58         LD      E,B             
5FF6: 09         ADD     HL,BC           
5FF7: 65         LD      H,L             
5FF8: 03         INC     BC              
5FF9: 82         ADD     A,D             
5FFA: 66         LD      H,(HL)          
5FFB: 09         ADD     HL,BC           
5FFC: 7F         LD      A,A             
5FFD: F5         PUSH    AF              
5FFE: 82         ADD     A,D             
5FFF: 72         LD      (HL),D          
6000: 09         ADD     HL,BC           
6001: 82         ADD     A,D             
6002: 77         LD      (HL),A          
6003: 03         INC     BC              
6004: 79         LD      A,C             
6005: F5         PUSH    AF              
6006: 29         ADD     HL,HL           
6007: FB         EI                      
6008: 49         LD      C,C             
6009: FB         EI                      
600A: 69         LD      L,C             
600B: FB         EI                      
600C: FE 03      CP      $03             
600E: 0A         LD      A,(BC)          
600F: 8A         ADC     A,D             
6010: 00         NOP                     
6011: 04         INC     B               
6012: 85         ADD     A,L             
6013: FF         RST     0X38            
6014: F5         PUSH    AF              
6015: 03         INC     BC              
6016: 08 04 04   LD      ($0404),SP      
6019: 82         ADD     A,D             
601A: 18 04      JR      $6020           
601C: 88         ADC     A,B             
601D: 10 51      STOP    $51             
601F: 82         ADD     A,D             
6020: 13         INC     DE              
6021: 04         INC     B               
6022: C6 29      ADD     $29             
6024: 51         LD      D,C             
6025: 82         ADD     A,D             
6026: 31 03 33   LD      SP,$3303        
6029: C4 35 C4   CALL    NZ,$C435        
602C: 37         SCF                     
602D: C4 82 42   CALL    NZ,$4282        
6030: 03         INC     BC              
6031: 44         LD      B,H             
6032: 09         ADD     HL,BC           
6033: 82         ADD     A,D             
6034: 47         LD      B,A             
6035: 03         INC     BC              
6036: 83         ADD     A,E             
6037: 50         LD      D,B             
6038: 03         INC     BC              
6039: 51         LD      D,C             
603A: 0A         LD      A,(BC)          
603B: 53         LD      D,E             
603C: C4 55 C4   CALL    NZ,$C455        
603F: 57         LD      D,A             
6040: C4 82 62   CALL    NZ,$6282        
6043: 09         ADD     HL,BC           
6044: 7F         LD      A,A             
6045: F5         PUSH    AF              
6046: 82         ADD     A,D             
6047: 75         LD      (HL),L          
6048: 03         INC     BC              
6049: 08 F5 20   LD      ($20F5),SP      
604C: B7         OR      A               
604D: 30 CE      JR      NC,$601D        
604F: 40         LD      B,B             
6050: B7         OR      A               
6051: 50         LD      D,B             
6052: CE 60      ADC     $60             
6054: B7         OR      A               
6055: 70         LD      (HL),B          
6056: CE FE      ADC     $FE             
6058: 03         INC     BC              
6059: 04         INC     B               
605A: C8         RET     Z               
605B: 00         NOP                     
605C: 38 C8      JR      C,$6026         
605E: 01 0E C6   LD      BC,$C60E        
6061: 02         LD      (BC),A          
6062: 0E C6      LD      C,$C6           
6064: 03         INC     BC              
6065: 9A         SBC     D               
6066: 62         LD      H,D             
6067: 9B         SBC     E               
6068: 63         LD      H,E             
6069: 9E         SBC     (HL)            
606A: 72         LD      (HL),D          
606B: 9A         SBC     D               
606C: 73         LD      (HL),E          
606D: 9B         SBC     E               
606E: 86         ADD     A,(HL)          
606F: 74         LD      (HL),H          
6070: 99         SBC     C               
6071: C2 F6 F5   JP      NZ,$F5F6        
6074: 08 B7 18   LD      ($18B7),SP      
6077: A2         AND     D               
6078: 28 B6      JR      Z,$6030         
607A: 09         ADD     HL,BC           
607B: 96         SUB     (HL)            
607C: 19         ADD     HL,DE           
607D: 93         SUB     E               
607E: FE 03      CP      $03             
6080: 04         INC     B               
6081: 8A         ADC     A,D             
6082: 70         LD      (HL),B          
6083: 99         SBC     C               
6084: 83         ADD     A,E             
6085: 74         LD      (HL),H          
6086: 04         INC     B               
6087: 8A         ADC     A,D             
6088: 00         NOP                     
6089: 96         SUB     (HL)            
608A: 8A         ADC     A,D             
608B: 10 93      STOP    $93             
608D: 23         INC     HL              
608E: B7         OR      A               
608F: 27         DAA                     
6090: B7         OR      A               
6091: 33         INC     SP              
6092: A2         AND     D               
6093: 37         SCF                     
6094: A2         AND     D               
6095: 43         LD      B,E             
6096: B6         OR      (HL)            
6097: 47         LD      B,A             
6098: B6         OR      (HL)            
6099: 03         INC     BC              
609A: 9A         SBC     D               
609B: 07         RLCA                    
609C: 9A         SBC     D               
609D: 13         INC     DE              
609E: 9D         SBC     L               
609F: 17         RLA                     
60A0: 9E         SBC     (HL)            
60A1: 83         ADD     A,E             
60A2: 14         INC     D               
60A3: 99         SBC     C               
60A4: 83         ADD     A,E             
60A5: 04         INC     B               
60A6: 0D         DEC     C               
60A7: 24         INC     H               
60A8: F9         LD      SP,HL           
60A9: C3 22 5C   JP      $5C22           
60AC: C3 28 5C   JP      $5C28           
60AF: C2 32 5C   JP      NZ,$5C32        
60B2: C3 44 5C   JP      $5C44           
60B5: C4 45 0C   CALL    NZ,$0C45        
60B8: C3 46 5C   JP      $5C46           
60BB: 72         LD      (HL),D          
60BC: 9B         SBC     E               
60BD: 73         LD      (HL),E          
60BE: 9C         SBC     H               
60BF: 77         LD      (HL),A          
60C0: 9B         SBC     E               
60C1: 78         LD      A,B             
60C2: 9C         SBC     H               
60C3: E1         POP     HL              
60C4: 14         INC     D               
60C5: D3                              
60C6: 50         LD      D,B             
60C7: 7C         LD      A,H             
60C8: FE 03      CP      $03             
60CA: 04         INC     B               
60CB: 00         NOP                     
60CC: 96         SUB     (HL)            
60CD: 10 93      STOP    $93             
60CF: 01 B7 11   LD      BC,$11B7        
60D2: A2         AND     D               
60D3: 21 B6 C2   LD      HL,$C2B6        
60D6: F2                              
60D7: F5         PUSH    AF              
60D8: C6 70      ADD     $70             
60DA: 9A         SBC     D               
60DB: 67         LD      H,A             
60DC: 9D         SBC     L               
60DD: 68         LD      L,B             
60DE: 9C         SBC     H               
60DF: 87         ADD     A,A             
60E0: 70         LD      (HL),B          
60E1: 99         SBC     C               
60E2: 77         LD      (HL),A          
60E3: 9C         SBC     H               
60E4: 78         LD      A,B             
60E5: 9A         SBC     D               
60E6: 82         ADD     A,D             
60E7: 48         LD      C,B             
60E8: 2F         CPL                     
60E9: 82         ADD     A,D             
60EA: 58         LD      E,B             
60EB: 0E C2      LD      C,$C2           
60ED: 69         LD      L,C             
60EE: 0E C6      LD      C,$C6           
60F0: 07         RLCA                    
60F1: 9A         SBC     D               
60F2: 08 96 09   LD      ($0996),SP      
60F5: 98         SBC     B               
60F6: 18 93      JR      $608B           
60F8: 19         ADD     HL,DE           
60F9: 95         SUB     L               
60FA: 48         LD      C,B             
60FB: E0 FE      LDFF00  ($FE),A         
60FD: 03         INC     BC              
60FE: 04         INC     B               
60FF: C8         RET     Z               
6100: 09         ADD     HL,BC           
6101: 37         SCF                     
6102: C2 06 38   JP      NZ,$3806        
6105: C5         PUSH    BC              
6106: 37         SCF                     
6107: 38 36      JR      C,$613F         
6109: 32         LD      (HLD),A         
610A: 27         DAA                     
610B: 2D         DEC     L               
610C: 40         LD      B,B             
610D: 2F         CPL                     
610E: 41         LD      B,C             
610F: 3C         INC     A               
6110: C3 51 37   JP      $3751           
6113: C3 50 0E   JP      $0E50           
6116: C2 07 0E   JP      NZ,$0E07        
6119: C8         RET     Z               
611A: 08 0E 00   LD      ($000E),SP      
611D: F5         PUSH    AF              
611E: F4                              
611F: F5         PUSH    AF              
6120: C4 03 0D   CALL    NZ,$0D03        
6123: C4 34 0D   CALL    NZ,$0D34        
6126: C2 36 5C   JP      NZ,$5C36        
6129: C2 52 5C   JP      NZ,$5C52        
612C: 63         LD      H,E             
612D: 5C         LD      E,H             
612E: C2 55 F5   JP      NZ,$F555        
6131: 72         LD      (HL),D          
6132: F5         PUSH    AF              
6133: 26 32      LD      H,$32           
6135: FE 09      CP      $09             
6137: EE 01      XOR     $01             
6139: CD 02 CE   CALL    $CE02           
613C: 03         INC     BC              
613D: CD 04 CE   CALL    $CE04           
6140: 05         DEC     B               
6141: CD 06 CE   CALL    $CE06           
6144: 07         RLCA                    
6145: CD 08 CE   CALL    $CE08           
6148: 09         ADD     HL,BC           
6149: CD C8 00   CALL    $00C8           
614C: 38 C7      JR      C,$6115         
614E: 11 ED 82   LD      DE,$82ED        
6151: 26 EC      LD      H,$EC           
6153: 82         ADD     A,D             
6154: 36 EC      LD      (HL),$EC        
6156: 82         ADD     A,D             
6157: 46         LD      B,(HL)          
6158: ED                              
6159: 82         ADD     A,D             
615A: 56         LD      D,(HL)          
615B: ED                              
615C: 88         ADC     A,B             
615D: 62         LD      H,D             
615E: EB                              
615F: 88         ADC     A,B             
6160: 72         LD      (HL),D          
6161: EB                              
6162: 22         LD      (HLI),A         
6163: 2B         DEC     HL              
6164: 82         ADD     A,D             
6165: 23         INC     HL              
6166: 2C         INC     L               
6167: 25         DEC     H               
6168: 2D         DEC     L               
6169: C2 32 37   JP      NZ,$3732        
616C: 52         LD      D,D             
616D: 33         INC     SP              
616E: 82         ADD     A,D             
616F: 53         LD      D,E             
6170: 2F         CPL                     
6171: 55         LD      D,L             
6172: 34         INC     (HL)            
6173: C2 35 38   JP      NZ,$3835        
6176: 82         ADD     A,D             
6177: 43         LD      B,E             
6178: 04         INC     B               
6179: 33         INC     SP              
617A: A0         AND     B               
617B: 34         INC     (HL)            
617C: C6 E1      ADD     $E1             
617E: 05         DEC     B               
617F: B0         OR      B               
6180: 78         LD      A,B             
6181: 10 48      STOP    $48             
6183: FB         EI                      
6184: FE 09      CP      $09             
6186: EE 25      XOR     $25             
6188: FB         EI                      
6189: 27         DAA                     
618A: FB         EI                      
618B: 34         INC     (HL)            
618C: FB         EI                      
618D: 35         DEC     (HL)            
618E: 4F         LD      C,A             
618F: 40         LD      B,B             
6190: FB         EI                      
6191: 77         LD      (HL),A          
6192: FB         EI                      
6193: 79         LD      A,C             
6194: B6         OR      (HL)            
6195: 00         NOP                     
6196: CE 01      ADC     $01             
6198: CD 02 CE   CALL    $CE02           
619B: 03         INC     BC              
619C: CD 04 CE   CALL    $CE04           
619F: 05         DEC     B               
61A0: CD 06 CE   CALL    $CE06           
61A3: 07         RLCA                    
61A4: CD 08 CE   CALL    $CE08           
61A7: 09         ADD     HL,BC           
61A8: CD 82 53   CALL    $5382           
61AB: C8         RET     Z               
61AC: C2 65 C8   JP      NZ,$C865        
61AF: C2 42 ED   JP      NZ,$ED42        
61B2: C2 64 ED   JP      NZ,$ED64        
61B5: C4 46 ED   CALL    NZ,$ED46        
61B8: 55         LD      D,L             
61B9: EB                              
61BA: 84         ADD     A,H             
61BB: 60         LD      H,B             
61BC: EB                              
61BD: 84         ADD     A,H             
61BE: 70         LD      (HL),B          
61BF: EB                              
61C0: 39         ADD     HL,SP           
61C1: C8         RET     Z               
61C2: 29         ADD     HL,HL           
61C3: EC                              
61C4: FE 09      CP      $09             
61C6: EE 00      XOR     $00             
61C8: CE 01      ADC     $01             
61CA: FB         EI                      
61CB: 03         INC     BC              
61CC: FB         EI                      
61CD: 05         DEC     B               
61CE: CD 06 CE   CALL    $CE06           
61D1: 07         RLCA                    
61D2: CD 08 CE   CALL    $CE08           
61D5: 09         ADD     HL,BC           
61D6: CD 83 30   CALL    $3083           
61D9: C8         RET     Z               
61DA: C5         PUSH    BC              
61DB: 15         DEC     D               
61DC: ED                              
61DD: C3 46 ED   JP      $ED46           
61E0: 33         INC     SP              
61E1: ED                              
61E2: 34         INC     (HL)            
61E3: EC                              
61E4: 82         ADD     A,D             
61E5: 26 C8      LD      H,$C8           
61E7: 28 ED      JR      Z,$61D6         
61E9: 39         ADD     HL,SP           
61EA: C8         RET     Z               
61EB: 84         ADD     A,H             
61EC: 41         LD      B,C             
61ED: EB                              
61EE: C2 51 EC   JP      NZ,$EC51        
61F1: 83         ADD     A,E             
61F2: 52         LD      D,D             
61F3: C8         RET     Z               
61F4: 82         ADD     A,D             
61F5: 67         LD      H,A             
61F6: C8         RET     Z               
61F7: 69         LD      L,C             
61F8: EC                              
61F9: 70         LD      (HL),B          
61FA: B7         OR      A               
61FB: 71         LD      (HL),C          
61FC: FB         EI                      
61FD: 73         LD      (HL),E          
61FE: FB         EI                      
61FF: 75         LD      (HL),L          
6200: FB         EI                      
6201: 77         LD      (HL),A          
6202: FB         EI                      
6203: 79         LD      A,C             
6204: B6         OR      (HL)            
6205: FE 09      CP      $09             
6207: EE 00      XOR     $00             
6209: CE C8      ADC     $C8             
620B: 09         ADD     HL,BC           
620C: 38 83      JR      C,$6191         
620E: 01 ED 82   LD      BC,$82ED        
6211: 04         INC     B               
6212: C8         RET     Z               
6213: C4 06 ED   CALL    NZ,$ED06        
6216: C4 17 C8   CALL    NZ,$C817        
6219: C5         PUSH    BC              
621A: 08 ED C2   LD      ($C2ED),SP      
621D: 15         DEC     D               
621E: C8         RET     Z               
621F: 83         ADD     A,E             
6220: 30 C8      JR      NC,$61EA        
6222: 13         INC     DE              
6223: EC                              
6224: 24         INC     H               
6225: EC                              
6226: 33         INC     SP              
6227: EC                              
6228: 84         ADD     A,H             
6229: 53         LD      D,E             
622A: C8         RET     Z               
622B: C3 44 EC   JP      $EC44           
622E: 82         ADD     A,D             
622F: 41         LD      B,C             
6230: ED                              
6231: 82         ADD     A,D             
6232: 51         LD      D,C             
6233: ED                              
6234: 57         LD      D,A             
6235: ED                              
6236: 70         LD      (HL),B          
6237: B7         OR      A               
6238: 71         LD      (HL),C          
6239: FB         EI                      
623A: 73         LD      (HL),E          
623B: FB         EI                      
623C: 75         LD      (HL),L          
623D: FB         EI                      
623E: 77         LD      (HL),A          
623F: FB         EI                      
6240: FE 03      CP      $03             
6242: 04         INC     B               
6243: C4 00 37   CALL    NZ,$3700        
6246: 40         LD      B,B             
6247: 31 C3 50   LD      SP,$50C3        
624A: 90         SUB     B               
624B: C8         RET     Z               
624C: 01 90 C8   LD      BC,$C890        
624F: 02         LD      (BC),A          
6250: 90         SUB     B               
6251: C2 33 90   JP      NZ,$9033        
6254: C2 03 87   JP      NZ,$8703        
6257: 23         INC     HL              
6258: 8A         ADC     A,D             
6259: 24         INC     H               
625A: 8E         ADC     A,(HL)          
625B: C2 34 87   JP      NZ,$8734        
625E: 52         LD      D,D             
625F: 88         ADC     A,B             
6260: 53         LD      D,E             
6261: 84         ADD     A,H             
6262: 54         LD      D,H             
6263: 8C         ADC     A,H             
6264: 62         LD      H,D             
6265: 87         ADD     A,A             
6266: C3 F1 F5   JP      $F5F1           
6269: C2 50 F5   JP      NZ,$F550        
626C: 82         ADD     A,D             
626D: 70         LD      (HL),B          
626E: F5         PUSH    AF              
626F: 16 08      LD      D,$08           
6271: 27         DAA                     
6272: 08 63 08   LD      ($0863),SP      
6275: 38 F5      JR      C,$626C         
6277: C2 49 F5   JP      NZ,$F549        
627A: C2 58 F5   JP      NZ,$F558        
627D: C2 67 0A   JP      NZ,$0A67        
6280: 18 44      JR      $62C6           
6282: 45         LD      B,L             
6283: 44         LD      B,H             
6284: 63         LD      H,E             
6285: 44         LD      B,H             
6286: FE 03      CP      $03             
6288: 04         INC     B               
6289: C5         PUSH    BC              
628A: 07         RLCA                    
628B: 86         ADD     A,(HL)          
628C: C5         PUSH    BC              
628D: 08 90 C5   LD      ($C590),SP      
6290: 09         ADD     HL,BC           
6291: 90         SUB     B               
6292: C2 4F F5   JP      NZ,$F54F        
6295: 61         LD      H,C             
6296: F5         PUSH    AF              
6297: C3 30 F5   JP      $F530           
629A: 32         LD      (HLD),A         
629B: 20 82      JR      NZ,$621F        
629D: 23         INC     HL              
629E: F5         PUSH    AF              
629F: C5         PUSH    BC              
62A0: F9         LD      SP,HL           
62A1: F5         PUSH    AF              
62A2: C4 08 F5   CALL    NZ,$F508        
62A5: 46         LD      B,(HL)          
62A6: F5         PUSH    AF              
62A7: 57         LD      D,A             
62A8: F5         PUSH    AF              
62A9: 83         ADD     A,E             
62AA: 53         LD      D,E             
62AB: 0A         LD      A,(BC)          
62AC: 64         LD      H,H             
62AD: 0A         LD      A,(BC)          
62AE: 12         LD      (DE),A          
62AF: 08 14 08   LD      ($0814),SP      
62B2: 83         ADD     A,E             
62B3: 72         LD      (HL),D          
62B4: F5         PUSH    AF              
62B5: 44         LD      B,H             
62B6: 44         LD      B,H             
62B7: 53         LD      D,E             
62B8: 44         LD      B,H             
62B9: 55         LD      D,L             
62BA: 44         LD      B,H             
62BB: 64         LD      H,H             
62BC: 44         LD      B,H             
62BD: 54         LD      D,H             
62BE: A0         AND     B               
62BF: FE 03      CP      $03             
62C1: 04         INC     B               
62C2: C8         RET     Z               
62C3: 00         NOP                     
62C4: 90         SUB     B               
62C5: 89         ADC     A,C             
62C6: 71         LD      (HL),C          
62C7: 90         SUB     B               
62C8: C4 39 90   CALL    NZ,$9039        
62CB: C6 01      ADD     $01             
62CD: 87         ADD     A,A             
62CE: 86         ADD     A,(HL)          
62CF: 62         LD      H,D             
62D0: 85         ADD     A,L             
62D1: C2 03 86   JP      NZ,$8603        
62D4: C3 38 86   JP      $8638           
62D7: 68         LD      L,B             
62D8: 8B         ADC     A,E             
62D9: 61         LD      H,C             
62DA: 8A         ADC     A,D             
62DB: 23         INC     HL              
62DC: 8D         ADC     A,L             
62DD: 28 8F      JR      Z,$626E         
62DF: 29         ADD     HL,HL           
62E0: 85         ADD     A,L             
62E1: 47         LD      B,A             
62E2: 5C         LD      E,H             
62E3: 86         ADD     A,(HL)          
62E4: 52         LD      D,D             
62E5: 5C         LD      E,H             
62E6: 82         ADD     A,D             
62E7: 24         INC     H               
62E8: 84         ADD     A,H             
62E9: 82         ADD     A,D             
62EA: 14         INC     D               
62EB: 90         SUB     B               
62EC: 82         ADD     A,D             
62ED: 04         INC     B               
62EE: 90         SUB     B               
62EF: 26 8C      LD      H,$8C           
62F1: 16 87      LD      D,$87           
62F3: 06 88      LD      B,$88           
62F5: 60         LD      H,B             
62F6: F5         PUSH    AF              
62F7: 83         ADD     A,E             
62F8: 07         RLCA                    
62F9: 84         ADD     A,H             
62FA: 04         INC     B               
62FB: F5         PUSH    AF              
62FC: C5         PUSH    BC              
62FD: FF         RST     0X38            
62FE: F5         PUSH    AF              
62FF: 85         ADD     A,L             
6300: 71         LD      (HL),C          
6301: F5         PUSH    AF              
6302: C2 39 F5   JP      NZ,$F539        
6305: 35         DEC     (HL)            
6306: 44         LD      B,H             
6307: 42         LD      B,D             
6308: 44         LD      B,H             
6309: FE 03      CP      $03             
630B: 04         INC     B               
630C: 82         ADD     A,D             
630D: 00         NOP                     
630E: 84         ADD     A,H             
630F: C5         PUSH    BC              
6310: 30 90      JR      NC,$62A2        
6312: C8         RET     Z               
6313: 09         ADD     HL,BC           
6314: 90         SUB     B               
6315: C5         PUSH    BC              
6316: 28 86      JR      Z,$629E         
6318: 78         LD      A,B             
6319: 90         SUB     B               
631A: 02         LD      (BC),A          
631B: 8C         ADC     A,H             
631C: C5         PUSH    BC              
631D: F9         LD      SP,HL           
631E: F5         PUSH    AF              
631F: 71         LD      (HL),C          
6320: 90         SUB     B               
6321: C4 31 87   CALL    NZ,$8731        
6324: 20 85      JR      NZ,$62AB        
6326: 21 8E C3   LD      HL,$C38E        
6329: 3F         CCF                     
632A: F5         PUSH    AF              
632B: 86         ADD     A,(HL)          
632C: 62         LD      H,D             
632D: 85         ADD     A,L             
632E: 61         LD      H,C             
632F: 8A         ADC     A,D             
6330: 68         LD      L,B             
6331: 8B         ADC     A,E             
6332: 87         ADD     A,A             
6333: 71         LD      (HL),C          
6334: 90         SUB     B               
6335: 85         ADD     A,L             
6336: 71         LD      (HL),C          
6337: F5         PUSH    AF              
6338: 82         ADD     A,D             
6339: 05         DEC     B               
633A: 0A         LD      A,(BC)          
633B: 07         RLCA                    
633C: 8D         ADC     A,L             
633D: 08 89 C5   LD      ($C589),SP      
6340: 17         RLA                     
6341: 0A         LD      A,(BC)          
6342: 56         LD      D,(HL)          
6343: 0A         LD      A,(BC)          
6344: 52         LD      D,D             
6345: 08 18 86   LD      ($8618),SP      
6348: 14         INC     D               
6349: E8 23      ADD     SP,$23          
634B: 08 25 08   LD      ($0825),SP      
634E: 32         LD      (HLD),A         
634F: E8 34      ADD     SP,$34          
6351: 5C         LD      E,H             
6352: 36 E8      LD      (HL),$E8        
6354: 43         LD      B,E             
6355: 08 45 08   LD      ($0845),SP      
6358: 54         LD      D,H             
6359: E8 12      ADD     SP,$12          
635B: 44         LD      B,H             
635C: FE 03      CP      $03             
635E: 03         INC     BC              
635F: C8         RET     Z               
6360: 00         NOP                     
6361: 04         INC     B               
6362: 84         ADD     A,H             
6363: 06 3A      LD      B,$3A           
6365: 07         RLCA                    
6366: E0 C5      LDFF00  ($C5),A         
6368: FF         RST     0X38            
6369: F5         PUSH    AF              
636A: 05         DEC     B               
636B: 38 11      JR      C,$637E         
636D: 3D         DEC     A               
636E: 12         LD      (DE),A          
636F: 48         LD      C,B             
6370: 13         INC     DE              
6371: E0 14      LDFF00  ($14),A         
6373: 49         LD      C,C             
6374: 15         DEC     D               
6375: 34         INC     (HL)            
6376: C5         PUSH    BC              
6377: 21 38 83   LD      HL,$8338        
637A: 25         DEC     H               
637B: 0A         LD      A,(BC)          
637C: 26 08      LD      H,$08           
637E: 34         INC     (HL)            
637F: 0A         LD      A,(BC)          
6380: 83         ADD     A,E             
6381: 35         DEC     (HL)            
6382: 08 38 0A   LD      ($0A38),SP      
6385: 36 5C      LD      (HL),$5C        
6387: 83         ADD     A,E             
6388: 45         LD      B,L             
6389: 0A         LD      A,(BC)          
638A: 46         LD      B,(HL)          
638B: 08 71 32   LD      ($3271),SP      
638E: 88         ADC     A,B             
638F: 72         LD      (HL),D          
6390: 2C         INC     L               
6391: 26 08      LD      H,$08           
6393: FE 03      CP      $03             
6395: 04         INC     B               
6396: 86         ADD     A,(HL)          
6397: 00         NOP                     
6398: 3A         LD      A,(HLD)         
6399: C3 06 37   JP      $3706           
639C: 86         ADD     A,(HL)          
639D: 10 03      STOP    $03             
639F: 86         ADD     A,(HL)          
63A0: 20 03      JR      NZ,$63A5        
63A2: 86         ADD     A,(HL)          
63A3: 30 03      JR      NC,$63A8        
63A5: 86         ADD     A,(HL)          
63A6: 40         LD      B,B             
63A7: 03         INC     BC              
63A8: 86         ADD     A,(HL)          
63A9: 50         LD      D,B             
63AA: 03         INC     BC              
63AB: 86         ADD     A,(HL)          
63AC: 60         LD      H,B             
63AD: 03         INC     BC              
63AE: C4 17 0A   CALL    NZ,$0A17        
63B1: C3 F9 F5   JP      $F5F9           
63B4: 23         INC     HL              
63B5: 20 C2      JR      NZ,$6379        
63B7: 32         LD      (HLD),A         
63B8: 20 C2      JR      NZ,$637C        
63BA: 34         INC     (HL)            
63BB: 20 35      JR      NZ,$63F2        
63BD: 2B         DEC     HL              
63BE: 36 31      LD      (HL),$31        
63C0: 38 0A      JR      C,$63CC         
63C2: C3 45 37   JP      $3745           
63C5: 53         LD      D,E             
63C6: 20 56      JR      NZ,$641E        
63C8: 0A         LD      A,(BC)          
63C9: C2 58 F5   JP      NZ,$F558        
63CC: 69         LD      L,C             
63CD: F5         PUSH    AF              
63CE: 85         ADD     A,L             
63CF: 70         LD      (HL),B          
63D0: 2C         INC     L               
63D1: 75         LD      (HL),L          
63D2: 31 33 C6   LD      SP,$C633        
63D5: E1         POP     HL              
63D6: 0A         LD      A,(BC)          
63D7: DE 38      SBC     $38             
63D9: 40         LD      B,B             
63DA: FE 03      CP      $03             
63DC: 0A         LD      A,(BC)          
63DD: C8         RET     Z               
63DE: 00         NOP                     
63DF: 04         INC     B               
63E0: C3 FF F5   JP      $F5FF           
63E3: 31 04 C5   LD      SP,$C504        
63E6: 01 51 82   LD      BC,$8251        
63E9: 04         INC     B               
63EA: 09         ADD     HL,BC           
63EB: 06 03      LD      B,$03           
63ED: 09         ADD     HL,BC           
63EE: 04         INC     B               
63EF: F9         LD      SP,HL           
63F0: F5         PUSH    AF              
63F1: 13         INC     DE              
63F2: 09         ADD     HL,BC           
63F3: 14         INC     D               
63F4: C4 16 C4   CALL    NZ,$C416        
63F7: 83         ADD     A,E             
63F8: 17         RLA                     
63F9: 03         INC     BC              
63FA: 18 0A      JR      $6406           
63FC: 26 03      LD      H,$03           
63FE: 82         ADD     A,D             
63FF: 27         DAA                     
6400: 09         ADD     HL,BC           
6401: 34         INC     (HL)            
6402: C4 35 03   CALL    NZ,$0335        
6405: 36 C5      LD      (HL),$C5        
6407: 37         SCF                     
6408: 03         INC     BC              
6409: 82         ADD     A,D             
640A: 43         LD      B,E             
640B: 03         INC     BC              
640C: 82         ADD     A,D             
640D: 47         LD      B,A             
640E: 03         INC     BC              
640F: 49         LD      C,C             
6410: 09         ADD     HL,BC           
6411: C2 51 04   JP      NZ,$0451        
6414: 88         ADC     A,B             
6415: 52         LD      D,D             
6416: 51         LD      D,C             
6417: 71         LD      (HL),C          
6418: 08 72 38   LD      ($3872),SP      
641B: 62         LD      H,D             
641C: 3D         DEC     A               
641D: 87         ADD     A,A             
641E: 63         LD      H,E             
641F: 2F         CPL                     
6420: 87         ADD     A,A             
6421: 73         LD      (HL),E          
6422: 3A         LD      A,(HLD)         
6423: C2 50 F5   JP      NZ,$F550        
6426: 6F         LD      L,A             
6427: F5         PUSH    AF              
6428: 09         ADD     HL,BC           
6429: FB         EI                      
642A: E1         POP     HL              
642B: 0A         LD      A,(BC)          
642C: DF         RST     0X18            
642D: 38 30      JR      C,$645F         
642F: FE 03      CP      $03             
6431: 0A         LD      A,(BC)          
6432: FF         RST     0X38            
6433: F5         PUSH    AF              
6434: 01 09 82   LD      BC,$8209        
6437: 02         LD      (BC),A          
6438: 03         INC     BC              
6439: C4 09 51   CALL    NZ,$5109        
643C: 12         LD      (DE),A          
643D: 03         INC     BC              
643E: 13         INC     DE              
643F: C4 14 09   CALL    NZ,$0914        
6442: 15         DEC     D               
6443: C4 16 03   CALL    NZ,$0316        
6446: 17         RLA                     
6447: C4 21 03   CALL    NZ,$0321        
644A: 82         ADD     A,D             
644B: 22         LD      (HLI),A         
644C: 09         ADD     HL,BC           
644D: 26 09      LD      H,$09           
644F: 27         DAA                     
6450: 03         INC     BC              
6451: 32         LD      (HLD),A         
6452: 03         INC     BC              
6453: 33         INC     SP              
6454: C4 35 C4   CALL    NZ,$C435        
6457: 36 03      LD      (HL),$03        
6459: 82         ADD     A,D             
645A: 44         LD      B,H             
645B: 03         INC     BC              
645C: 84         ADD     A,H             
645D: 46         LD      B,(HL)          
645E: 51         LD      D,C             
645F: 85         ADD     A,L             
6460: 50         LD      D,B             
6461: 51         LD      D,C             
6462: 85         ADD     A,L             
6463: 60         LD      H,B             
6464: 2F         CPL                     
6465: 65         LD      H,L             
6466: 4E         LD      C,(HL)          
6467: 55         LD      D,L             
6468: 3D         DEC     A               
6469: 56         LD      D,(HL)          
646A: 35         DEC     (HL)            
646B: 85         ADD     A,L             
646C: 70         LD      (HL),B          
646D: 3A         LD      A,(HLD)         
646E: 75         LD      (HL),L          
646F: 3F         CCF                     
6470: 82         ADD     A,D             
6471: 68         LD      L,B             
6472: 04         INC     B               
6473: 84         ADD     A,H             
6474: 76         HALT                    
6475: 04         INC     B               
6476: 68         LD      L,B             
6477: F5         PUSH    AF              
6478: 76         HALT                    
6479: F5         PUSH    AF              
647A: 00         NOP                     
647B: B7         OR      A               
647C: 10 CE      STOP    $CE             
647E: FE 03      CP      $03             
6480: 0E 8A      LD      C,$8A           
6482: 60         LD      H,B             
6483: 04         INC     B               
6484: 8A         ADC     A,D             
6485: 70         LD      (HL),B          
6486: 04         INC     B               
6487: 60         LD      H,B             
6488: F5         PUSH    AF              
6489: 84         ADD     A,H             
648A: 72         LD      (HL),D          
648B: F5         PUSH    AF              
648C: C5         PUSH    BC              
648D: 00         NOP                     
648E: 38 50      JR      C,$64E0         
6490: 32         LD      (HLD),A         
6491: 89         ADC     A,C             
6492: 51         LD      D,C             
6493: 2C         INC     L               
6494: 86         ADD     A,(HL)          
6495: 04         INC     B               
6496: 96         SUB     (HL)            
6497: 86         ADD     A,(HL)          
6498: 14         INC     D               
6499: 93         SUB     E               
649A: 02         LD      (BC),A          
649B: 9D         SBC     L               
649C: 03         INC     BC              
649D: 9E         SBC     (HL)            
649E: 12         LD      (DE),A          
649F: 97         SUB     A               
64A0: 22         LD      (HLI),A         
64A1: 94         SUB     H               
64A2: 13         INC     DE              
64A3: 98         SBC     B               
64A4: 23         INC     HL              
64A5: 95         SUB     L               
64A6: 62         LD      H,D             
64A7: C6 E1      ADD     $E1             
64A9: 1F         RRA                     
64AA: FD                              
64AB: 58         LD      E,B             
64AC: 50         LD      D,B             
64AD: 85         ADD     A,L             
64AE: 64         LD      H,H             
64AF: E8 FE      ADD     SP,$FE          
64B1: 03         INC     BC              
64B2: 04         INC     B               
64B3: 8A         ADC     A,D             
64B4: 00         NOP                     
64B5: 96         SUB     (HL)            
64B6: 8A         ADC     A,D             
64B7: 10 93      STOP    $93             
64B9: 8A         ADC     A,D             
64BA: 20 0E      JR      NZ,$64CA        
64BC: 8A         ADC     A,D             
64BD: 30 0E      JR      NC,$64CD        
64BF: 8A         ADC     A,D             
64C0: 40         LD      B,B             
64C1: 0E 03      LD      C,$03           
64C3: 9E         SBC     (HL)            
64C4: 13         INC     DE              
64C5: 98         SBC     B               
64C6: 23         INC     HL              
64C7: 95         SUB     L               
64C8: 02         LD      (BC),A          
64C9: 9D         SBC     L               
64CA: 12         LD      (DE),A          
64CB: 97         SUB     A               
64CC: 22         LD      (HLI),A         
64CD: 94         SUB     H               
64CE: 07         RLCA                    
64CF: 9D         SBC     L               
64D0: 17         RLA                     
64D1: 97         SUB     A               
64D2: 27         DAA                     
64D3: 94         SUB     H               
64D4: 08 9E 18   LD      ($189E),SP      
64D7: 98         SBC     B               
64D8: 28 95      JR      Z,$646F         
64DA: 8A         ADC     A,D             
64DB: 50         LD      D,B             
64DC: 2C         INC     L               
64DD: 33         INC     SP              
64DE: 9F         SBC     A               
64DF: 37         SCF                     
64E0: 9F         SBC     A               
64E1: 43         LD      B,E             
64E2: 9A         SBC     D               
64E3: 47         LD      B,A             
64E4: 9A         SBC     D               
64E5: 53         LD      D,E             
64E6: A3         AND     E               
64E7: 57         LD      D,A             
64E8: A3         AND     E               
64E9: C6 04      ADD     $04             
64EB: 0D         DEC     C               
64EC: C6 06      ADD     $06             
64EE: 0D         DEC     C               
64EF: C8         RET     Z               
64F0: 05         DEC     B               
64F1: 0C         INC     C               
64F2: 70         LD      (HL),B          
64F3: F5         PUSH    AF              
64F4: 79         LD      A,C             
64F5: F5         PUSH    AF              
64F6: 83         ADD     A,E             
64F7: 14         INC     D               
64F8: AB         XOR     E               
64F9: 83         ADD     A,E             
64FA: 24         INC     H               
64FB: AC         XOR     H               
64FC: FE 03      CP      $03             
64FE: 04         INC     B               
64FF: 8A         ADC     A,D             
6500: 00         NOP                     
6501: 96         SUB     (HL)            
6502: 8A         ADC     A,D             
6503: 10 93      STOP    $93             
6505: 8A         ADC     A,D             
6506: 20 0E      JR      NZ,$6516        
6508: 8A         ADC     A,D             
6509: 30 0E      JR      NC,$6519        
650B: 8A         ADC     A,D             
650C: 40         LD      B,B             
650D: 0E 03      LD      C,$03           
650F: 9E         SBC     (HL)            
6510: 13         INC     DE              
6511: 98         SBC     B               
6512: 23         INC     HL              
6513: 95         SUB     L               
6514: 02         LD      (BC),A          
6515: 9D         SBC     L               
6516: 12         LD      (DE),A          
6517: 97         SUB     A               
6518: 22         LD      (HLI),A         
6519: 94         SUB     H               
651A: 07         RLCA                    
651B: 9D         SBC     L               
651C: 17         RLA                     
651D: 97         SUB     A               
651E: 27         DAA                     
651F: 94         SUB     H               
6520: 08 9E 18   LD      ($189E),SP      
6523: 98         SBC     B               
6524: 28 95      JR      Z,$64BB         
6526: 8A         ADC     A,D             
6527: 50         LD      D,B             
6528: 2C         INC     L               
6529: 33         INC     SP              
652A: 9F         SBC     A               
652B: 37         SCF                     
652C: 9F         SBC     A               
652D: 43         LD      B,E             
652E: 9A         SBC     D               
652F: 47         LD      B,A             
6530: 9A         SBC     D               
6531: 53         LD      D,E             
6532: A3         AND     E               
6533: 57         LD      D,A             
6534: A3         AND     E               
6535: C6 04      ADD     $04             
6537: 0D         DEC     C               
6538: C6 06      ADD     $06             
653A: 0D         DEC     C               
653B: C8         RET     Z               
653C: 05         DEC     B               
653D: 0C         INC     C               
653E: 70         LD      (HL),B          
653F: F5         PUSH    AF              
6540: 79         LD      A,C             
6541: F5         PUSH    AF              
6542: FE 03      CP      $03             
6544: 0E 8A      LD      C,$8A           
6546: 50         LD      D,B             
6547: 2C         INC     L               
6548: 8A         ADC     A,D             
6549: 60         LD      H,B             
654A: 04         INC     B               
654B: 8A         ADC     A,D             
654C: 70         LD      (HL),B          
654D: 04         INC     B               
654E: 87         ADD     A,A             
654F: 00         NOP                     
6550: 96         SUB     (HL)            
6551: 87         ADD     A,A             
6552: 10 93      STOP    $93             
6554: 86         ADD     A,(HL)          
6555: 7F         LD      A,A             
6556: F5         PUSH    AF              
6557: 07         RLCA                    
6558: 9D         SBC     L               
6559: 08 9E 17   LD      ($179E),SP      
655C: 97         SUB     A               
655D: 18 98      JR      $64F7           
655F: 27         DAA                     
6560: 94         SUB     H               
6561: 28 95      JR      Z,$64F8         
6563: FE 03      CP      $03             
6565: 04         INC     B               
6566: F2                              
6567: F5         PUSH    AF              
6568: F5         PUSH    AF              
6569: F5         PUSH    AF              
656A: C5         PUSH    BC              
656B: 00         NOP                     
656C: 0E C8      LD      C,$C8           
656E: 08 0E C3   LD      ($C30E),SP      
6571: 21 0E C3   LD      HL,$C30E        
6574: 27         DAA                     
6575: 0E 85      LD      C,$85           
6577: 22         LD      (HLI),A         
6578: 0E 01      LD      C,$01           
657A: 37         SCF                     
657B: 11 33 85   LD      DE,$8533        
657E: 12         LD      (DE),A          
657F: 2F         CPL                     
6580: 07         RLCA                    
6581: 38 17      JR      C,$659A         
6583: 34         INC     (HL)            
6584: 32         LD      (HLD),A         
6585: 2B         DEC     HL              
6586: 36 2D      LD      (HL),$2D        
6588: 42         LD      B,D             
6589: 37         SCF                     
658A: 46         LD      B,(HL)          
658B: 38 52      JR      C,$65DF         
658D: 31 56 32   LD      SP,$3256        
6590: 57         LD      D,A             
6591: 2D         DEC     L               
6592: 82         ADD     A,D             
6593: 50         LD      D,B             
6594: 2C         INC     L               
6595: C2 67 38   JP      NZ,$3867        
6598: C8         RET     Z               
6599: 09         ADD     HL,BC           
659A: 37         SCF                     
659B: 83         ADD     A,E             
659C: 33         INC     SP              
659D: 2C         INC     L               
659E: 14         INC     D               
659F: D8         RET     C               
65A0: 24         INC     H               
65A1: D9         RETI                    
65A2: 34         INC     (HL)            
65A3: DA 82 7F   JP      C,$7F82         
65A6: F5         PUSH    AF              
65A7: FE 09      CP      $09             
65A9: EB                              
65AA: C5         PUSH    BC              
65AB: 00         NOP                     
65AC: 38 50      JR      C,$65FE         
65AE: 32         LD      (HLD),A         
65AF: 89         ADC     A,C             
65B0: 51         LD      D,C             
65B1: 2C         INC     L               
65B2: 60         LD      H,B             
65B3: 3D         DEC     A               
65B4: 70         LD      (HL),B          
65B5: 38 89      JR      C,$6540         
65B7: 61         LD      H,C             
65B8: 2F         CPL                     
65B9: 89         ADC     A,C             
65BA: 71         LD      (HL),C          
65BB: 3A         LD      A,(HLD)         
65BC: C4 01 ED   CALL    NZ,$ED01        
65BF: 85         ADD     A,L             
65C0: 12         LD      (DE),A          
65C1: EC                              
65C2: 85         ADD     A,L             
65C3: 22         LD      (HLI),A         
65C4: EC                              
65C5: 85         ADD     A,L             
65C6: 32         LD      (HLD),A         
65C7: EC                              
65C8: 83         ADD     A,E             
65C9: 17         RLA                     
65CA: C8         RET     Z               
65CB: FE 09      CP      $09             
65CD: EB                              
65CE: 8A         ADC     A,D             
65CF: 50         LD      D,B             
65D0: 2C         INC     L               
65D1: 8A         ADC     A,D             
65D2: 60         LD      H,B             
65D3: 2F         CPL                     
65D4: 8A         ADC     A,D             
65D5: 70         LD      (HL),B          
65D6: 3A         LD      A,(HLD)         
65D7: 10 C8      STOP    $C8             
65D9: 83         ADD     A,E             
65DA: 21 C8 C3   LD      HL,$C3C8        
65DD: 05         DEC     B               
65DE: C8         RET     Z               
65DF: 26 C8      LD      H,$C8           
65E1: 82         ADD     A,D             
65E2: 38 C8      JR      C,$65AC         
65E4: 07         RLCA                    
65E5: CD 08 CE   CALL    $CE08           
65E8: 09         ADD     HL,BC           
65E9: CD C3 04   CALL    $04C3           
65EC: ED                              
65ED: C2 27 ED   JP      NZ,$ED27        
65F0: 06 ED      LD      B,$ED           
65F2: 20 ED      JR      NZ,$65E1        
65F4: FE 0A      CP      $0A             
65F6: EB                              
65F7: 00         NOP                     
65F8: CE 01      ADC     $01             
65FA: CD 02 CE   CALL    $CE02           
65FD: 03         INC     BC              
65FE: CD 04 CE   CALL    $CE04           
6601: 05         DEC     B               
6602: CD 06 CE   CALL    $CE06           
6605: 07         RLCA                    
6606: CD 08 CE   CALL    $CE08           
6609: 09         ADD     HL,BC           
660A: CD 83 30   CALL    $3083           
660D: C8         RET     Z               
660E: 88         ADC     A,B             
660F: 22         LD      (HLI),A         
6610: C8         RET     Z               
6611: 83         ADD     A,E             
6612: 45         LD      B,L             
6613: C8         RET     Z               
6614: 8A         ADC     A,D             
6615: 50         LD      D,B             
6616: 2C         INC     L               
6617: 8A         ADC     A,D             
6618: 60         LD      H,B             
6619: 2F         CPL                     
661A: 8A         ADC     A,D             
661B: 70         LD      (HL),B          
661C: 3A         LD      A,(HLD)         
661D: FE 0A      CP      $0A             
661F: ED                              
6620: 00         NOP                     
6621: CE 01      ADC     $01             
6623: CD 02 CE   CALL    $CE02           
6626: 03         INC     BC              
6627: CD 04 CE   CALL    $CE04           
662A: 05         DEC     B               
662B: CD 06 CE   CALL    $CE06           
662E: 07         RLCA                    
662F: CD 08 CE   CALL    $CE08           
6632: C8         RET     Z               
6633: 09         ADD     HL,BC           
6634: 38 84      JR      C,$65BA         
6636: 10 ED      STOP    $ED             
6638: 20 C8      JR      NZ,$6602        
663A: 83         ADD     A,E             
663B: 30 ED      JR      NC,$662A        
663D: 83         ADD     A,E             
663E: 40         LD      B,B             
663F: ED                              
6640: 33         INC     SP              
6641: C8         RET     Z               
6642: 83         ADD     A,E             
6643: 16 C8      LD      D,$C8           
6645: 28 C8      JR      Z,$660F         
6647: 50         LD      D,B             
6648: 2C         INC     L               
6649: 51         LD      D,C             
664A: 2D         DEC     L               
664B: 55         LD      D,L             
664C: 2B         DEC     HL              
664D: 82         ADD     A,D             
664E: 56         LD      D,(HL)          
664F: 2C         INC     L               
6650: 58         LD      E,B             
6651: 2D         DEC     L               
6652: 60         LD      H,B             
6653: 2F         CPL                     
6654: 61         LD      H,C             
6655: 4E         LD      C,(HL)          
6656: 65         LD      H,L             
6657: 2E 82      LD      L,$82           
6659: 66         LD      H,(HL)          
665A: 2F         CPL                     
665B: 68         LD      L,B             
665C: 4E         LD      C,(HL)          
665D: 70         LD      (HL),B          
665E: 3A         LD      A,(HLD)         
665F: 71         LD      (HL),C          
6660: 3F         CCF                     
6661: 75         LD      (HL),L          
6662: 3E 82      LD      A,$82           
6664: 76         HALT                    
6665: 3A         LD      A,(HLD)         
6666: 78         LD      A,B             
6667: 3F         CCF                     
6668: 83         ADD     A,E             
6669: 62         LD      H,D             
666A: E9         JP      (HL)            
666B: 83         ADD     A,E             
666C: 72         LD      (HL),D          
666D: E9         JP      (HL)            
666E: 84         ADD     A,H             
666F: 10 EB      STOP    $EB             
6671: 82         ADD     A,D             
6672: 30 EB      JR      NC,$665F        
6674: 82         ADD     A,D             
6675: 40         LD      B,B             
6676: EB                              
6677: FE FF      CP      $FF             
6679: FF         RST     0X38            
667A: FF         RST     0X38            
667B: FF         RST     0X38            
667C: FF         RST     0X38            
667D: FF         RST     0X38            
667E: FF         RST     0X38            
667F: FF         RST     0X38            
6680: FF         RST     0X38            
6681: FF         RST     0X38            
6682: FF         RST     0X38            
6683: FF         RST     0X38            
6684: FF         RST     0X38            
6685: FF         RST     0X38            
6686: FF         RST     0X38            
6687: FF         RST     0X38            
6688: FF         RST     0X38            
6689: FF         RST     0X38            
668A: FF         RST     0X38            
668B: FF         RST     0X38            
668C: FF         RST     0X38            
668D: FF         RST     0X38            
668E: FF         RST     0X38            
668F: FF         RST     0X38            
6690: FF         RST     0X38            
6691: FF         RST     0X38            
6692: FF         RST     0X38            
6693: FF         RST     0X38            
6694: FF         RST     0X38            
6695: FF         RST     0X38            
6696: FF         RST     0X38            
6697: FF         RST     0X38            
6698: FF         RST     0X38            
6699: FF         RST     0X38            
669A: FF         RST     0X38            
669B: FF         RST     0X38            
669C: FF         RST     0X38            
669D: FF         RST     0X38            
669E: FF         RST     0X38            
669F: FF         RST     0X38            
66A0: FF         RST     0X38            
66A1: FF         RST     0X38            
66A2: FF         RST     0X38            
66A3: FF         RST     0X38            
66A4: FF         RST     0X38            
66A5: FF         RST     0X38            
66A6: FF         RST     0X38            
66A7: FF         RST     0X38            
66A8: FF         RST     0X38            
66A9: FF         RST     0X38            
66AA: FF         RST     0X38            
66AB: FF         RST     0X38            
66AC: FF         RST     0X38            
66AD: FF         RST     0X38            
66AE: FF         RST     0X38            
66AF: FF         RST     0X38            
66B0: FF         RST     0X38            
66B1: FF         RST     0X38            
66B2: FF         RST     0X38            
66B3: FF         RST     0X38            
66B4: FF         RST     0X38            
66B5: FF         RST     0X38            
66B6: FF         RST     0X38            
66B7: FF         RST     0X38            
66B8: FF         RST     0X38            
66B9: FF         RST     0X38            
66BA: FF         RST     0X38            
66BB: FF         RST     0X38            
66BC: FF         RST     0X38            
66BD: FF         RST     0X38            
66BE: FF         RST     0X38            
66BF: FF         RST     0X38            
66C0: FF         RST     0X38            
66C1: FF         RST     0X38            
66C2: FF         RST     0X38            
66C3: FF         RST     0X38            
66C4: FF         RST     0X38            
66C5: FF         RST     0X38            
66C6: FF         RST     0X38            
66C7: FF         RST     0X38            
66C8: FF         RST     0X38            
66C9: FF         RST     0X38            
66CA: FF         RST     0X38            
66CB: FF         RST     0X38            
66CC: FF         RST     0X38            
66CD: FF         RST     0X38            
66CE: FF         RST     0X38            
66CF: FF         RST     0X38            
66D0: FF         RST     0X38            
66D1: FF         RST     0X38            
66D2: FF         RST     0X38            
66D3: FF         RST     0X38            
66D4: FF         RST     0X38            
66D5: FF         RST     0X38            
66D6: FF         RST     0X38            
66D7: FF         RST     0X38            
66D8: FF         RST     0X38            
66D9: FF         RST     0X38            
66DA: FF         RST     0X38            
66DB: FF         RST     0X38            
66DC: FF         RST     0X38            
66DD: FF         RST     0X38            
66DE: FF         RST     0X38            
66DF: FF         RST     0X38            
66E0: FF         RST     0X38            
66E1: FF         RST     0X38            
66E2: FF         RST     0X38            
66E3: FF         RST     0X38            
66E4: FF         RST     0X38            
66E5: FF         RST     0X38            
66E6: FF         RST     0X38            
66E7: FF         RST     0X38            
66E8: FF         RST     0X38            
66E9: FF         RST     0X38            
66EA: FF         RST     0X38            
66EB: FF         RST     0X38            
66EC: FF         RST     0X38            
66ED: FF         RST     0X38            
66EE: FF         RST     0X38            
66EF: FF         RST     0X38            
66F0: FF         RST     0X38            
66F1: FF         RST     0X38            
66F2: FF         RST     0X38            
66F3: FF         RST     0X38            
66F4: FF         RST     0X38            
66F5: FF         RST     0X38            
66F6: FF         RST     0X38            
66F7: FF         RST     0X38            
66F8: FF         RST     0X38            
66F9: FF         RST     0X38            
66FA: FF         RST     0X38            
66FB: FF         RST     0X38            
66FC: FF         RST     0X38            
66FD: FF         RST     0X38            
66FE: FF         RST     0X38            
66FF: FF         RST     0X38            
6700: 59         LD      E,C             
6701: 6F         LD      L,A             
6702: 75         LD      (HL),L          
6703: 5E         LD      E,(HL)          
6704: 76         HALT                    
6705: 65         LD      H,L             
6706: 20 66      JR      NZ,$676E        
6708: 6F         LD      L,A             
6709: 75         LD      (HL),L          
670A: 6E         LD      L,(HL)          
670B: 64         LD      H,H             
670C: 20 61      JR      NZ,$676F        
670E: 20 20      JR      NZ,$6730        
6710: 47         LD      B,A             
6711: 6F         LD      L,A             
6712: 6C         LD      L,H             
6713: 64         LD      H,H             
6714: 65         LD      H,L             
6715: 6E         LD      L,(HL)          
6716: 20 4C      JR      NZ,$6764        
6718: 65         LD      H,L             
6719: 61         LD      H,C             
671A: 66         LD      H,(HL)          
671B: 21 20 20   LD      HL,$2020        
671E: 20 20      JR      NZ,$6740        
6720: 59         LD      E,C             
6721: 6F         LD      L,A             
6722: 75         LD      (HL),L          
6723: 20 63      JR      NZ,$6788        
6725: 61         LD      H,C             
6726: 6E         LD      L,(HL)          
6727: 20 73      JR      NZ,$679C        
6729: 65         LD      H,L             
672A: 65         LD      H,L             
672B: 20 68      JR      NZ,$6795        
672D: 6F         LD      L,A             
672E: 77         LD      (HL),A          
672F: 20 6D      JR      NZ,$679E        
6731: 61         LD      H,C             
6732: 6E         LD      L,(HL)          
6733: 79         LD      A,C             
6734: 20 79      JR      NZ,$67AF        
6736: 6F         LD      L,A             
6737: 75         LD      (HL),L          
6738: 20 68      JR      NZ,$67A2        
673A: 61         LD      H,C             
673B: 76         HALT                    
673C: 65         LD      H,L             
673D: 20 6F      JR      NZ,$67AE        
673F: 6E         LD      L,(HL)          
6740: 74         LD      (HL),H          
6741: 68         LD      L,B             
6742: 65         LD      H,L             
6743: 20 53      JR      NZ,$6798        
6745: 75         LD      (HL),L          
6746: 62         LD      H,D             
6747: 2D         DEC     L               
6748: 53         LD      D,E             
6749: 63         LD      H,E             
674A: 72         LD      (HL),D          
674B: 65         LD      H,L             
674C: 65         LD      H,L             
674D: 6E         LD      L,(HL)          
674E: 2E FF      LD      L,$FF           
6750: 41         LD      B,C             
6751: 74         LD      (HL),H          
6752: 20 6C      JR      NZ,$67C0        
6754: 61         LD      H,C             
6755: 73         LD      (HL),E          
6756: 74         LD      (HL),H          
6757: 21 20 20   LD      HL,$2020        
675A: 59         LD      E,C             
675B: 6F         LD      L,A             
675C: 75         LD      (HL),L          
675D: 5E         LD      E,(HL)          
675E: 76         HALT                    
675F: 65         LD      H,L             
6760: 67         LD      H,A             
6761: 6F         LD      L,A             
6762: 74         LD      (HL),H          
6763: 20 74      JR      NZ,$67D9        
6765: 68         LD      L,B             
6766: 65         LD      H,L             
6767: 20 66      JR      NZ,$67CF        
6769: 69         LD      L,C             
676A: 6E         LD      L,(HL)          
676B: 61         LD      H,C             
676C: 6C         LD      L,H             
676D: 20 20      JR      NZ,$678F        
676F: 20 47      JR      NZ,$67B8        
6771: 6F         LD      L,A             
6772: 6C         LD      L,H             
6773: 64         LD      H,H             
6774: 65         LD      H,L             
6775: 6E         LD      L,(HL)          
6776: 20 4C      JR      NZ,$67C4        
6778: 65         LD      H,L             
6779: 61         LD      H,C             
677A: 66         LD      H,(HL)          
677B: 21 20 20   LD      HL,$2020        
677E: 20 20      JR      NZ,$67A0        
6780: 4E         LD      C,(HL)          
6781: 6F         LD      L,A             
6782: 77         LD      (HL),A          
6783: 20 67      JR      NZ,$67EC        
6785: 6F         LD      L,A             
6786: 20 61      JR      NZ,$67E9        
6788: 6E         LD      L,(HL)          
6789: 64         LD      H,H             
678A: 20 73      JR      NZ,$67FF        
678C: 65         LD      H,L             
678D: 65         LD      H,L             
678E: 20 20      JR      NZ,$67B0        
6790: 52         LD      D,D             
6791: 69         LD      L,C             
6792: 63         LD      H,E             
6793: 68         LD      L,B             
6794: 61         LD      H,C             
6795: 72         LD      (HL),D          
6796: 64         LD      H,H             
6797: 20 61      JR      NZ,$67FA        
6799: 62         LD      H,D             
679A: 6F         LD      L,A             
679B: 75         LD      (HL),L          
679C: 74         LD      (HL),H          
679D: 20 20      JR      NZ,$67BF        
679F: 20 74      JR      NZ,$6815        
67A1: 68         LD      L,B             
67A2: 61         LD      H,C             
67A3: 74         LD      (HL),H          
67A4: 20 6B      JR      NZ,$6811        
67A6: 65         LD      H,L             
67A7: 79         LD      A,C             
67A8: 2E 2E      LD      L,$2E           
67AA: 2E FF      LD      L,$FF           
67AC: 59         LD      E,C             
67AD: 6F         LD      L,A             
67AE: 75         LD      (HL),L          
67AF: 5E         LD      E,(HL)          
67B0: 76         HALT                    
67B1: 65         LD      H,L             
67B2: 20 67      JR      NZ,$681B        
67B4: 6F         LD      L,A             
67B5: 74         LD      (HL),H          
67B6: 20 61      JR      NZ,$6819        
67B8: 20 20      JR      NZ,$67DA        
67BA: 20 20      JR      NZ,$67DC        
67BC: 47         LD      B,A             
67BD: 75         LD      (HL),L          
67BE: 61         LD      H,C             
67BF: 72         LD      (HL),D          
67C0: 64         LD      H,H             
67C1: 69         LD      L,C             
67C2: 61         LD      H,C             
67C3: 6E         LD      L,(HL)          
67C4: 20 41      JR      NZ,$6807        
67C6: 63         LD      H,E             
67C7: 6F         LD      L,A             
67C8: 72         LD      (HL),D          
67C9: 6E         LD      L,(HL)          
67CA: 21 20 49   LD      HL,$4920        
67CD: 74         LD      (HL),H          
67CE: 20 77      JR      NZ,$6847        
67D0: 69         LD      L,C             
67D1: 6C         LD      L,H             
67D2: 6C         LD      L,H             
67D3: 20 72      JR      NZ,$6847        
67D5: 65         LD      H,L             
67D6: 64         LD      H,H             
67D7: 75         LD      (HL),L          
67D8: 63         LD      H,E             
67D9: 65         LD      H,L             
67DA: 20 20      JR      NZ,$67FC        
67DC: 74         LD      (HL),H          
67DD: 68         LD      L,B             
67DE: 65         LD      H,L             
67DF: 20 64      JR      NZ,$6845        
67E1: 61         LD      H,C             
67E2: 6D         LD      L,L             
67E3: 61         LD      H,C             
67E4: 67         LD      H,A             
67E5: 65         LD      H,L             
67E6: 20 79      JR      NZ,$6861        
67E8: 6F         LD      L,A             
67E9: 75         LD      (HL),L          
67EA: 20 20      JR      NZ,$680C        
67EC: 74         LD      (HL),H          
67ED: 61         LD      H,C             
67EE: 6B         LD      L,E             
67EF: 65         LD      H,L             
67F0: 20 62      JR      NZ,$6854        
67F2: 79         LD      A,C             
67F3: 20 68      JR      NZ,$685D        
67F5: 61         LD      H,C             
67F6: 6C         LD      L,H             
67F7: 66         LD      H,(HL)          
67F8: 21 FF 59   LD      HL,$59FF        
67FB: 6F         LD      L,A             
67FC: 75         LD      (HL),L          
67FD: 5E         LD      E,(HL)          
67FE: 76         HALT                    
67FF: 65         LD      H,L             
6800: 20 67      JR      NZ,$6869        
6802: 6F         LD      L,A             
6803: 74         LD      (HL),H          
6804: 20 74      JR      NZ,$687A        
6806: 68         LD      L,B             
6807: 65         LD      H,L             
6808: 20 20      JR      NZ,$682A        
680A: 4D         LD      C,L             
680B: 69         LD      L,C             
680C: 72         LD      (HL),D          
680D: 72         LD      (HL),D          
680E: 6F         LD      L,A             
680F: 72         LD      (HL),D          
6810: 20 53      JR      NZ,$6865        
6812: 68         LD      L,B             
6813: 69         LD      L,C             
6814: 65         LD      H,L             
6815: 6C         LD      L,H             
6816: 64         LD      H,H             
6817: 21 20 20   LD      HL,$2020        
681A: 59         LD      E,C             
681B: 6F         LD      L,A             
681C: 75         LD      (HL),L          
681D: 20 63      JR      NZ,$6882        
681F: 61         LD      H,C             
6820: 6E         LD      L,(HL)          
6821: 20 6E      JR      NZ,$6891        
6823: 6F         LD      L,A             
6824: 77         LD      (HL),A          
6825: 20 74      JR      NZ,$689B        
6827: 75         LD      (HL),L          
6828: 72         LD      (HL),D          
6829: 6E         LD      L,(HL)          
682A: 62         LD      H,D             
682B: 61         LD      H,C             
682C: 63         LD      H,E             
682D: 6B         LD      L,E             
682E: 20 74      JR      NZ,$68A4        
6830: 68         LD      L,B             
6831: 65         LD      H,L             
6832: 20 62      JR      NZ,$6896        
6834: 65         LD      H,L             
6835: 61         LD      H,C             
6836: 6D         LD      L,L             
6837: 73         LD      (HL),E          
6838: 20 20      JR      NZ,$685A        
683A: 79         LD      A,C             
683B: 6F         LD      L,A             
683C: 75         LD      (HL),L          
683D: 20 63      JR      NZ,$68A2        
683F: 6F         LD      L,A             
6840: 75         LD      (HL),L          
6841: 6C         LD      L,H             
6842: 64         LD      H,H             
6843: 6E         LD      L,(HL)          
6844: 5E         LD      E,(HL)          
6845: 74         LD      (HL),H          
6846: 20 20      JR      NZ,$6868        
6848: 20 20      JR      NZ,$686A        
684A: 62         LD      H,D             
684B: 6C         LD      L,H             
684C: 6F         LD      L,A             
684D: 63         LD      H,E             
684E: 6B         LD      L,E             
684F: 20 62      JR      NZ,$68B3        
6851: 65         LD      H,L             
6852: 66         LD      H,(HL)          
6853: 6F         LD      L,A             
6854: 72         LD      (HL),D          
6855: 65         LD      H,L             
6856: 21 FF 59   LD      HL,$59FF        
6859: 6F         LD      L,A             
685A: 75         LD      (HL),L          
685B: 5E         LD      E,(HL)          
685C: 76         HALT                    
685D: 65         LD      H,L             
685E: 20 67      JR      NZ,$68C7        
6860: 6F         LD      L,A             
6861: 74         LD      (HL),H          
6862: 20 61      JR      NZ,$68C5        
6864: 20 20      JR      NZ,$6886        
6866: 20 20      JR      NZ,$6888        
6868: 6D         LD      L,L             
6869: 6F         LD      L,A             
686A: 72         LD      (HL),D          
686B: 65         LD      H,L             
686C: 20 50      JR      NZ,$68BE        
686E: 6F         LD      L,A             
686F: 77         LD      (HL),A          
6870: 65         LD      H,L             
6871: 72         LD      (HL),D          
6872: 66         LD      H,(HL)          
6873: 75         LD      (HL),L          
6874: 6C         LD      L,H             
6875: 20 20      JR      NZ,$6897        
6877: 20 42      JR      NZ,$68BB        
6879: 72         LD      (HL),D          
687A: 61         LD      H,C             
687B: 63         LD      H,E             
687C: 65         LD      H,L             
687D: 6C         LD      L,H             
687E: 65         LD      H,L             
687F: 74         LD      (HL),H          
6880: 21 20 20   LD      HL,$2020        
6883: 4E         LD      C,(HL)          
6884: 6F         LD      L,A             
6885: 77         LD      (HL),A          
6886: 20 20      JR      NZ,$68A8        
6888: 79         LD      A,C             
6889: 6F         LD      L,A             
688A: 75         LD      (HL),L          
688B: 20 63      JR      NZ,$68F0        
688D: 61         LD      H,C             
688E: 6E         LD      L,(HL)          
688F: 20 61      JR      NZ,$68F2        
6891: 6C         LD      L,H             
6892: 6D         LD      L,L             
6893: 6F         LD      L,A             
6894: 73         LD      (HL),E          
6895: 74         LD      (HL),H          
6896: 20 20      JR      NZ,$68B8        
6898: 6C         LD      L,H             
6899: 69         LD      L,C             
689A: 66         LD      H,(HL)          
689B: 74         LD      (HL),H          
689C: 20 61      JR      NZ,$68FF        
689E: 20 77      JR      NZ,$6917        
68A0: 68         LD      L,B             
68A1: 61         LD      H,C             
68A2: 6C         LD      L,H             
68A3: 65         LD      H,L             
68A4: 21 FF 59   LD      HL,$59FF        
68A7: 6F         LD      L,A             
68A8: 75         LD      (HL),L          
68A9: 20 66      JR      NZ,$6911        
68AB: 6F         LD      L,A             
68AC: 75         LD      (HL),L          
68AD: 6E         LD      L,(HL)          
68AE: 64         LD      H,H             
68AF: 20 61      JR      NZ,$6912        
68B1: 20 20      JR      NZ,$68D3        
68B3: 20 20      JR      NZ,$68D5        
68B5: 20 53      JR      NZ,$690A        
68B7: 65         LD      H,L             
68B8: 63         LD      H,E             
68B9: 72         LD      (HL),D          
68BA: 65         LD      H,L             
68BB: 74         LD      (HL),H          
68BC: 20 53      JR      NZ,$6911        
68BE: 65         LD      H,L             
68BF: 61         LD      H,C             
68C0: 73         LD      (HL),E          
68C1: 68         LD      L,B             
68C2: 65         LD      H,L             
68C3: 6C         LD      L,H             
68C4: 6C         LD      L,H             
68C5: 21 49 66   LD      HL,$6649        
68C8: 20 79      JR      NZ,$6943        
68CA: 6F         LD      L,A             
68CB: 75         LD      (HL),L          
68CC: 20 63      JR      NZ,$6931        
68CE: 6F         LD      L,A             
68CF: 6C         LD      L,H             
68D0: 6C         LD      L,H             
68D1: 65         LD      H,L             
68D2: 63         LD      H,E             
68D3: 74         LD      (HL),H          
68D4: 20 61      JR      NZ,$6937        
68D6: 6C         LD      L,H             
68D7: 6F         LD      L,A             
68D8: 74         LD      (HL),H          
68D9: 20 6F      JR      NZ,$694A        
68DB: 66         LD      H,(HL)          
68DC: 20 74      JR      NZ,$6952        
68DE: 68         LD      L,B             
68DF: 65         LD      H,L             
68E0: 73         LD      (HL),E          
68E1: 65         LD      H,L             
68E2: 2C         INC     L               
68E3: 20 20      JR      NZ,$6905        
68E5: 20 73      JR      NZ,$695A        
68E7: 6F         LD      L,A             
68E8: 6D         LD      L,L             
68E9: 65         LD      H,L             
68EA: 74         LD      (HL),H          
68EB: 68         LD      L,B             
68EC: 69         LD      L,C             
68ED: 6E         LD      L,(HL)          
68EE: 67         LD      H,A             
68EF: 20 67      JR      NZ,$6958        
68F1: 6F         LD      L,A             
68F2: 6F         LD      L,A             
68F3: 64         LD      H,H             
68F4: 20 20      JR      NZ,$6916        
68F6: 69         LD      L,C             
68F7: 73         LD      (HL),E          
68F8: 20 62      JR      NZ,$695C        
68FA: 6F         LD      L,A             
68FB: 75         LD      (HL),L          
68FC: 6E         LD      L,(HL)          
68FD: 64         LD      H,H             
68FE: 20 74      JR      NZ,$6974        
6900: 6F         LD      L,A             
6901: 20 20      JR      NZ,$6923        
6903: 20 20      JR      NZ,$6925        
6905: 20 68      JR      NZ,$696F        
6907: 61         LD      H,C             
6908: 70         LD      (HL),B          
6909: 70         LD      (HL),B          
690A: 65         LD      H,L             
690B: 6E         LD      L,(HL)          
690C: 21 FF 57   LD      HL,$57FF        
690F: 61         LD      H,C             
6910: 6E         LD      L,(HL)          
6911: 74         LD      (HL),H          
6912: 20 74      JR      NZ,$6988        
6914: 6F         LD      L,A             
6915: 20 67      JR      NZ,$697E        
6917: 6F         LD      L,A             
6918: 20 6F      JR      NZ,$6989        
691A: 6E         LD      L,(HL)          
691B: 20 61      JR      NZ,$697E        
691D: 20 72      JR      NZ,$6991        
691F: 61         LD      H,C             
6920: 66         LD      H,(HL)          
6921: 74         LD      (HL),H          
6922: 20 72      JR      NZ,$6996        
6924: 69         LD      L,C             
6925: 64         LD      H,H             
6926: 65         LD      H,L             
6927: 20 66      JR      NZ,$698F        
6929: 6F         LD      L,A             
692A: 72         LD      (HL),D          
692B: 20 61      JR      NZ,$698E        
692D: 20 68      JR      NZ,$6997        
692F: 75         LD      (HL),L          
6930: 6E         LD      L,(HL)          
6931: 64         LD      H,H             
6932: 72         LD      (HL),D          
6933: 65         LD      H,L             
6934: 64         LD      H,H             
6935: 20 52      JR      NZ,$6989        
6937: 75         LD      (HL),L          
6938: 70         LD      (HL),B          
6939: 65         LD      H,L             
693A: 65         LD      H,L             
693B: 73         LD      (HL),E          
693C: 3F         CCF                     
693D: 20 20      JR      NZ,$695F        
693F: 20 20      JR      NZ,$6961        
6941: 20 59      JR      NZ,$699C        
6943: 65         LD      H,L             
6944: 73         LD      (HL),E          
6945: 20 20      JR      NZ,$6967        
6947: 4E         LD      C,(HL)          
6948: 6F         LD      L,A             
6949: 20 57      JR      NZ,$69A2        
694B: 61         LD      H,C             
694C: 79         LD      A,C             
694D: FE 4F      CP      $4F             
694F: 6B         LD      L,E             
6950: 61         LD      H,C             
6951: 79         LD      A,C             
6952: 2C         INC     L               
6953: 20 74      JR      NZ,$69C9        
6955: 68         LD      L,B             
6956: 65         LD      H,L             
6957: 20 72      JR      NZ,$69CB        
6959: 61         LD      H,C             
695A: 66         LD      H,(HL)          
695B: 74         LD      (HL),H          
695C: 20 20      JR      NZ,$697E        
695E: 69         LD      L,C             
695F: 73         LD      (HL),E          
6960: 20 72      JR      NZ,$69D4        
6962: 65         LD      H,L             
6963: 61         LD      H,C             
6964: 64         LD      H,H             
6965: 79         LD      A,C             
6966: 20 66      JR      NZ,$69CE        
6968: 6F         LD      L,A             
6969: 72         LD      (HL),D          
696A: 20 79      JR      NZ,$69E5        
696C: 6F         LD      L,A             
696D: 75         LD      (HL),L          
696E: 6F         LD      L,A             
696F: 75         LD      (HL),L          
6970: 74         LD      (HL),H          
6971: 73         LD      (HL),E          
6972: 69         LD      L,C             
6973: 64         LD      H,H             
6974: 65         LD      H,L             
6975: 21 20 20   LD      HL,$2020        
6978: 45         LD      B,L             
6979: 6E         LD      L,(HL)          
697A: 6A         LD      L,D             
697B: 6F         LD      L,A             
697C: 79         LD      A,C             
697D: 21 FF 57   LD      HL,$57FF        
6980: 61         LD      H,C             
6981: 74         LD      (HL),H          
6982: 65         LD      H,L             
6983: 72         LD      (HL),D          
6984: 66         LD      H,(HL)          
6985: 61         LD      H,C             
6986: 6C         LD      L,H             
6987: 6C         LD      L,H             
6988: 20 61      JR      NZ,$69EB        
698A: 74         LD      (HL),H          
698B: 20 74      JR      NZ,$6A01        
698D: 68         LD      L,B             
698E: 65         LD      H,L             
698F: 20 20      JR      NZ,$69B1        
6991: 20 20      JR      NZ,$69B3        
6993: 53         LD      D,E             
6994: 68         LD      L,B             
6995: 72         LD      (HL),D          
6996: 69         LD      L,C             
6997: 6E         LD      L,(HL)          
6998: 65         LD      H,L             
6999: FF         RST     0X38            
699A: 20 53      JR      NZ,$69EF        
699C: 6F         LD      L,A             
699D: 75         LD      (HL),L          
699E: 74         LD      (HL),H          
699F: 68         LD      L,B             
69A0: 20 6F      JR      NZ,$6A11        
69A2: 66         LD      H,(HL)          
69A3: 20 74      JR      NZ,$6A19        
69A5: 68         LD      L,B             
69A6: 65         LD      H,L             
69A7: 20 20      JR      NZ,$69C9        
69A9: 20 20      JR      NZ,$69CB        
69AB: 20 20      JR      NZ,$69CD        
69AD: 20 53      JR      NZ,$6A02        
69AF: 68         LD      L,B             
69B0: 72         LD      (HL),D          
69B1: 69         LD      L,C             
69B2: 6E         LD      L,(HL)          
69B3: 65         LD      H,L             
69B4: FF         RST     0X38            
69B5: 45         LD      B,L             
69B6: 6E         LD      L,(HL)          
69B7: 74         LD      (HL),H          
69B8: 72         LD      (HL),D          
69B9: 61         LD      H,C             
69BA: 6E         LD      L,(HL)          
69BB: 63         LD      H,E             
69BC: 65         LD      H,L             
69BD: 20 74      JR      NZ,$6A33        
69BF: 6F         LD      L,A             
69C0: 20 74      JR      NZ,$6A36        
69C2: 68         LD      L,B             
69C3: 65         LD      H,L             
69C4: 20 20      JR      NZ,$69E6        
69C6: 41         LD      B,C             
69C7: 6E         LD      L,(HL)          
69C8: 69         LD      L,C             
69C9: 6D         LD      L,L             
69CA: 61         LD      H,C             
69CB: 6C         LD      L,H             
69CC: 20 56      JR      NZ,$6A24        
69CE: 69         LD      L,C             
69CF: 6C         LD      L,H             
69D0: 6C         LD      L,H             
69D1: 61         LD      H,C             
69D2: 67         LD      H,A             
69D3: 65         LD      H,L             
69D4: FF         RST     0X38            
69D5: 57         LD      D,A             
69D6: 65         LD      H,L             
69D7: 20 77      JR      NZ,$6A50        
69D9: 65         LD      H,L             
69DA: 72         LD      (HL),D          
69DB: 65         LD      H,L             
69DC: 20 62      JR      NZ,$6A40        
69DE: 6F         LD      L,A             
69DF: 72         LD      (HL),D          
69E0: 6E         LD      L,(HL)          
69E1: 20 6F      JR      NZ,$6A52        
69E3: 66         LD      H,(HL)          
69E4: 20 6E      JR      NZ,$6A54        
69E6: 69         LD      L,C             
69E7: 67         LD      H,A             
69E8: 68         LD      L,B             
69E9: 74         LD      (HL),H          
69EA: 6D         LD      L,L             
69EB: 61         LD      H,C             
69EC: 72         LD      (HL),D          
69ED: 65         LD      H,L             
69EE: 73         LD      (HL),E          
69EF: 2E 2E      LD      L,$2E           
69F1: 2E 20      LD      L,$20           
69F3: 54         LD      D,H             
69F4: 6F         LD      L,A             
69F5: 74         LD      (HL),H          
69F6: 61         LD      H,C             
69F7: 6B         LD      L,E             
69F8: 65         LD      H,L             
69F9: 20 6F      JR      NZ,$6A6A        
69FB: 76         HALT                    
69FC: 65         LD      H,L             
69FD: 72         LD      (HL),D          
69FE: 20 74      JR      NZ,$6A74        
6A00: 68         LD      L,B             
6A01: 69         LD      L,C             
6A02: 73         LD      (HL),E          
6A03: 20 20      JR      NZ,$6A25        
6A05: 77         LD      (HL),A          
6A06: 6F         LD      L,A             
6A07: 72         LD      (HL),D          
6A08: 6C         LD      L,H             
6A09: 64         LD      H,H             
6A0A: 2C         INC     L               
6A0B: 20 77      JR      NZ,$6A84        
6A0D: 65         LD      H,L             
6A0E: 20 6D      JR      NZ,$6A7D        
6A10: 61         LD      H,C             
6A11: 64         LD      H,H             
6A12: 65         LD      H,L             
6A13: 20 20      JR      NZ,$6A35        
6A15: 74         LD      (HL),H          
6A16: 68         LD      L,B             
6A17: 65         LD      H,L             
6A18: 20 57      JR      NZ,$6A71        
6A1A: 69         LD      L,C             
6A1B: 6E         LD      L,(HL)          
6A1C: 64         LD      H,H             
6A1D: 20 46      JR      NZ,$6A65        
6A1F: 69         LD      L,C             
6A20: 73         LD      (HL),E          
6A21: 68         LD      L,B             
6A22: 20 20      JR      NZ,$6A44        
6A24: 20 73      JR      NZ,$6A99        
6A26: 6C         LD      L,H             
6A27: 65         LD      H,L             
6A28: 65         LD      H,L             
6A29: 70         LD      (HL),B          
6A2A: 20 65      JR      NZ,$6A91        
6A2C: 6E         LD      L,(HL)          
6A2D: 64         LD      H,H             
6A2E: 6C         LD      L,H             
6A2F: 65         LD      H,L             
6A30: 73         LD      (HL),E          
6A31: 73         LD      (HL),E          
6A32: 6C         LD      L,H             
6A33: 79         LD      A,C             
6A34: 21 49 66   LD      HL,$6649        
6A37: 20 74      JR      NZ,$6AAD        
6A39: 68         LD      L,B             
6A3A: 65         LD      H,L             
6A3B: 20 57      JR      NZ,$6A94        
6A3D: 69         LD      L,C             
6A3E: 6E         LD      L,(HL)          
6A3F: 64         LD      H,H             
6A40: 20 46      JR      NZ,$6A88        
6A42: 69         LD      L,C             
6A43: 73         LD      (HL),E          
6A44: 68         LD      L,B             
6A45: 64         LD      H,H             
6A46: 6F         LD      L,A             
6A47: 65         LD      H,L             
6A48: 73         LD      (HL),E          
6A49: 6E         LD      L,(HL)          
6A4A: 5E         LD      E,(HL)          
6A4B: 74         LD      (HL),H          
6A4C: 20 77      JR      NZ,$6AC5        
6A4E: 61         LD      H,C             
6A4F: 6B         LD      L,E             
6A50: 65         LD      H,L             
6A51: 20 75      JR      NZ,$6AC8        
6A53: 70         LD      (HL),B          
6A54: 2C         INC     L               
6A55: 74         LD      (HL),H          
6A56: 68         LD      L,B             
6A57: 69         LD      L,C             
6A58: 73         LD      (HL),E          
6A59: 20 69      JR      NZ,$6AC4        
6A5B: 73         LD      (HL),E          
6A5C: 6C         LD      L,H             
6A5D: 61         LD      H,C             
6A5E: 6E         LD      L,(HL)          
6A5F: 64         LD      H,H             
6A60: 20 77      JR      NZ,$6AD9        
6A62: 69         LD      L,C             
6A63: 6C         LD      L,H             
6A64: 6C         LD      L,H             
6A65: 6E         LD      L,(HL)          
6A66: 65         LD      H,L             
6A67: 76         HALT                    
6A68: 65         LD      H,L             
6A69: 72         LD      (HL),D          
6A6A: 20 64      JR      NZ,$6AD0        
6A6C: 69         LD      L,C             
6A6D: 73         LD      (HL),E          
6A6E: 61         LD      H,C             
6A6F: 70         LD      (HL),B          
6A70: 70         LD      (HL),B          
6A71: 65         LD      H,L             
6A72: 61         LD      H,C             
6A73: 72         LD      (HL),D          
6A74: 21 57 65   LD      HL,$6557        
6A77: 20 77      JR      NZ,$6AF0        
6A79: 6F         LD      L,A             
6A7A: 75         LD      (HL),L          
6A7B: 6C         LD      L,H             
6A7C: 64         LD      H,H             
6A7D: 20 68      JR      NZ,$6AE7        
6A7F: 61         LD      H,C             
6A80: 76         HALT                    
6A81: 65         LD      H,L             
6A82: 20 20      JR      NZ,$6AA4        
6A84: 20 62      JR      NZ,$6AE8        
6A86: 65         LD      H,L             
6A87: 65         LD      H,L             
6A88: 6E         LD      L,(HL)          
6A89: 20 74      JR      NZ,$6AFF        
6A8B: 68         LD      L,B             
6A8C: 65         LD      H,L             
6A8D: 20 6D      JR      NZ,$6AFC        
6A8F: 61         LD      H,C             
6A90: 73         LD      (HL),E          
6A91: 74         LD      (HL),H          
6A92: 65         LD      H,L             
6A93: 72         LD      (HL),D          
6A94: 73         LD      (HL),E          
6A95: 6F         LD      L,A             
6A96: 66         LD      H,(HL)          
6A97: 20 74      JR      NZ,$6B0D        
6A99: 68         LD      L,B             
6A9A: 69         LD      L,C             
6A9B: 73         LD      (HL),E          
6A9C: 20 70      JR      NZ,$6B0E        
6A9E: 6C         LD      L,H             
6A9F: 61         LD      H,C             
6AA0: 63         LD      H,E             
6AA1: 65         LD      H,L             
6AA2: 2E 2E      LD      L,$2E           
6AA4: 2E 42      LD      L,$42           
6AA6: 75         LD      (HL),L          
6AA7: 74         LD      (HL),H          
6AA8: 20 79      JR      NZ,$6B23        
6AAA: 6F         LD      L,A             
6AAB: 75         LD      (HL),L          
6AAC: 20 68      JR      NZ,$6B16        
6AAE: 61         LD      H,C             
6AAF: 64         LD      H,H             
6AB0: 20 74      JR      NZ,$6B26        
6AB2: 6F         LD      L,A             
6AB3: 20 20      JR      NZ,$6AD5        
6AB5: 63         LD      H,E             
6AB6: 6F         LD      L,A             
6AB7: 6D         LD      L,L             
6AB8: 65         LD      H,L             
6AB9: 20 68      JR      NZ,$6B23        
6ABB: 65         LD      H,L             
6ABC: 72         LD      (HL),D          
6ABD: 65         LD      H,L             
6ABE: 20 61      JR      NZ,$6B21        
6AC0: 6E         LD      L,(HL)          
6AC1: 64         LD      H,H             
6AC2: 20 20      JR      NZ,$6AE4        
6AC4: 20 64      JR      NZ,$6B2A        
6AC6: 69         LD      L,C             
6AC7: 73         LD      (HL),E          
6AC8: 72         LD      (HL),D          
6AC9: 75         LD      (HL),L          
6ACA: 70         LD      (HL),B          
6ACB: 74         LD      (HL),H          
6ACC: 20 6F      JR      NZ,$6B3D        
6ACE: 75         LD      (HL),L          
6ACF: 72         LD      (HL),D          
6AD0: 20 20      JR      NZ,$6AF2        
6AD2: 20 20      JR      NZ,$6AF4        
6AD4: 20 70      JR      NZ,$6B46        
6AD6: 6C         LD      L,H             
6AD7: 61         LD      H,C             
6AD8: 6E         LD      L,(HL)          
6AD9: 73         LD      (HL),E          
6ADA: 21 20 20   LD      HL,$2020        
6ADD: 48         LD      C,B             
6ADE: 65         LD      H,L             
6ADF: 68         LD      L,B             
6AE0: 20 68      JR      NZ,$6B4A        
6AE2: 65         LD      H,L             
6AE3: 68         LD      L,B             
6AE4: 21 59 6F   LD      HL,$6F59        
6AE7: 75         LD      (HL),L          
6AE8: 20 63      JR      NZ,$6B4D        
6AEA: 61         LD      H,C             
6AEB: 6E         LD      L,(HL)          
6AEC: 20 6E      JR      NZ,$6B5C        
6AEE: 65         LD      H,L             
6AEF: 76         HALT                    
6AF0: 65         LD      H,L             
6AF1: 72         LD      (HL),D          
6AF2: 20 20      JR      NZ,$6B14        
6AF4: 20 64      JR      NZ,$6B5A        
6AF6: 65         LD      H,L             
6AF7: 66         LD      H,(HL)          
6AF8: 65         LD      H,L             
6AF9: 61         LD      H,C             
6AFA: 74         LD      (HL),H          
6AFB: 20 75      JR      NZ,$6B72        
6AFD: 73         LD      (HL),E          
6AFE: 21 21 21   LD      HL,$2121        
6B01: 20 20      JR      NZ,$6B23        
6B03: 20 20      JR      NZ,$6B25        
6B05: 4C         LD      C,H             
6B06: 65         LD      H,L             
6B07: 74         LD      (HL),H          
6B08: 5E         LD      E,(HL)          
6B09: 73         LD      (HL),E          
6B0A: 20 72      JR      NZ,$6B7E        
6B0C: 75         LD      (HL),L          
6B0D: 6D         LD      L,L             
6B0E: 62         LD      H,D             
6B0F: 6C         LD      L,H             
6B10: 65         LD      H,L             
6B11: 21 FF 54   LD      HL,$54FF        
6B14: 68         LD      L,B             
6B15: 69         LD      L,C             
6B16: 73         LD      (HL),E          
6B17: 20 69      JR      NZ,$6B82        
6B19: 73         LD      (HL),E          
6B1A: 6C         LD      L,H             
6B1B: 61         LD      H,C             
6B1C: 6E         LD      L,(HL)          
6B1D: 64         LD      H,H             
6B1E: 20 69      JR      NZ,$6B89        
6B20: 73         LD      (HL),E          
6B21: 20 20      JR      NZ,$6B43        
6B23: 67         LD      H,A             
6B24: 6F         LD      L,A             
6B25: 69         LD      L,C             
6B26: 6E         LD      L,(HL)          
6B27: 67         LD      H,A             
6B28: 20 74      JR      NZ,$6B9E        
6B2A: 6F         LD      L,A             
6B2B: 20 64      JR      NZ,$6B91        
6B2D: 69         LD      L,C             
6B2E: 73         LD      (HL),E          
6B2F: 2D         DEC     L               
6B30: 20 20      JR      NZ,$6B52        
6B32: 20 61      JR      NZ,$6B95        
6B34: 70         LD      (HL),B          
6B35: 70         LD      (HL),B          
6B36: 65         LD      H,L             
6B37: 61         LD      H,C             
6B38: 72         LD      (HL),D          
6B39: 2E 2E      LD      L,$2E           
6B3B: 2E 20      LD      L,$20           
6B3D: 20 4F      JR      NZ,$6B8E        
6B3F: 75         LD      (HL),L          
6B40: 72         LD      (HL),D          
6B41: 20 20      JR      NZ,$6B63        
6B43: 77         LD      (HL),A          
6B44: 6F         LD      L,A             
6B45: 72         LD      (HL),D          
6B46: 6C         LD      L,H             
6B47: 64         LD      H,H             
6B48: 20 69      JR      NZ,$6BB3        
6B4A: 73         LD      (HL),E          
6B4B: 20 67      JR      NZ,$6BB4        
6B4D: 6F         LD      L,A             
6B4E: 69         LD      L,C             
6B4F: 6E         LD      L,(HL)          
6B50: 67         LD      H,A             
6B51: 20 20      JR      NZ,$6B73        
6B53: 74         LD      (HL),H          
6B54: 6F         LD      L,A             
6B55: 20 64      JR      NZ,$6BBB        
6B57: 69         LD      L,C             
6B58: 73         LD      (HL),E          
6B59: 61         LD      H,C             
6B5A: 70         LD      (HL),B          
6B5B: 70         LD      (HL),B          
6B5C: 65         LD      H,L             
6B5D: 61         LD      H,C             
6B5E: 72         LD      (HL),D          
6B5F: 2E 2E      LD      L,$2E           
6B61: 2E 20      LD      L,$20           
6B63: 4F         LD      C,A             
6B64: 75         LD      (HL),L          
6B65: 72         LD      (HL),D          
6B66: 20 77      JR      NZ,$6BDF        
6B68: 6F         LD      L,A             
6B69: 72         LD      (HL),D          
6B6A: 6C         LD      L,H             
6B6B: 64         LD      H,H             
6B6C: 2E 2E      LD      L,$2E           
6B6E: 2E 20      LD      L,$20           
6B70: 20 20      JR      NZ,$6B92        
6B72: 20 4F      JR      NZ,$6BC3        
6B74: 75         LD      (HL),L          
6B75: 72         LD      (HL),D          
6B76: 2E 2E      LD      L,$2E           
6B78: 2E 20      LD      L,$20           
6B7A: 77         LD      (HL),A          
6B7B: 6F         LD      L,A             
6B7C: 72         LD      (HL),D          
6B7D: 6C         LD      L,H             
6B7E: 64         LD      H,H             
6B7F: 2E 2E      LD      L,$2E           
6B81: 2E 20      LD      L,$20           
6B83: FF         RST     0X38            
6B84: 57         LD      D,A             
6B85: 6F         LD      L,A             
6B86: 77         LD      (HL),A          
6B87: 21 20 20   LD      HL,$2020        
6B8A: 23         INC     HL              
6B8B: 23         INC     HL              
6B8C: 23         INC     HL              
6B8D: 23         INC     HL              
6B8E: 23         INC     HL              
6B8F: 2C         INC     L               
6B90: 20 63      JR      NZ,$6BF5        
6B92: 61         LD      H,C             
6B93: 6E         LD      L,(HL)          
6B94: 49         LD      C,C             
6B95: 20 74      JR      NZ,$6C0B        
6B97: 72         LD      (HL),D          
6B98: 79         LD      A,C             
6B99: 20 74      JR      NZ,$6C0F        
6B9B: 68         LD      L,B             
6B9C: 69         LD      L,C             
6B9D: 73         LD      (HL),E          
6B9E: 3F         CCF                     
6B9F: 21 20 20   LD      HL,$2020        
6BA2: 20 20      JR      NZ,$6BC4        
6BA4: 57         LD      D,A             
6BA5: 68         LD      L,B             
6BA6: 61         LD      H,C             
6BA7: 74         LD      (HL),H          
6BA8: 20 64      JR      NZ,$6C0E        
6BAA: 6F         LD      L,A             
6BAB: 20 79      JR      NZ,$6C26        
6BAD: 6F         LD      L,A             
6BAE: 75         LD      (HL),L          
6BAF: 20 73      JR      NZ,$6C24        
6BB1: 61         LD      H,C             
6BB2: 79         LD      A,C             
6BB3: 3F         CCF                     
6BB4: 20 20      JR      NZ,$6BD6        
6BB6: 20 20      JR      NZ,$6BD8        
6BB8: 4F         LD      C,A             
6BB9: 6B         LD      L,E             
6BBA: 61         LD      H,C             
6BBB: 79         LD      A,C             
6BBC: 20 4E      JR      NZ,$6C0C        
6BBE: 6F         LD      L,A             
6BBF: 20 57      JR      NZ,$6C18        
6BC1: 61         LD      H,C             
6BC2: 79         LD      A,C             
6BC3: FE 43      CP      $43             
6BC5: 5E         LD      E,(HL)          
6BC6: 6D         LD      L,L             
6BC7: 6F         LD      L,A             
6BC8: 6E         LD      L,(HL)          
6BC9: 21 20 20   LD      HL,$2020        
6BCC: 49         LD      C,C             
6BCD: 20 77      JR      NZ,$6C46        
6BCF: 61         LD      H,C             
6BD0: 6E         LD      L,(HL)          
6BD1: 74         LD      (HL),H          
6BD2: 20 20      JR      NZ,$6BF4        
6BD4: 74         LD      (HL),H          
6BD5: 6F         LD      L,A             
6BD6: 20 64      JR      NZ,$6C3C        
6BD8: 6F         LD      L,A             
6BD9: 20 69      JR      NZ,$6C44        
6BDB: 74         LD      (HL),H          
6BDC: 21 20 43   LD      HL,$4320        
6BDF: 61         LD      H,C             
6BE0: 6E         LD      L,(HL)          
6BE1: 20 49      JR      NZ,$6C2C        
6BE3: 3F         CCF                     
6BE4: 49         LD      C,C             
6BE5: 74         LD      (HL),H          
6BE6: 20 6C      JR      NZ,$6C54        
6BE8: 6F         LD      L,A             
6BE9: 6F         LD      L,A             
6BEA: 6B         LD      L,E             
6BEB: 73         LD      (HL),E          
6BEC: 20 73      JR      NZ,$6C61        
6BEE: 6F         LD      L,A             
6BEF: 20 66      JR      NZ,$6C57        
6BF1: 75         LD      (HL),L          
6BF2: 6E         LD      L,(HL)          
6BF3: 21 20 20   LD      HL,$2020        
6BF6: 20 20      JR      NZ,$6C18        
6BF8: 59         LD      E,C             
6BF9: 65         LD      H,L             
6BFA: 73         LD      (HL),E          
6BFB: 20 20      JR      NZ,$6C1D        
6BFD: 4F         LD      C,A             
6BFE: 6B         LD      L,E             
6BFF: 61         LD      H,C             
6C00: 79         LD      A,C             
6C01: FE 59      CP      $59             
6C03: 6F         LD      L,A             
6C04: 75         LD      (HL),L          
6C05: 5E         LD      E,(HL)          
6C06: 72         LD      (HL),D          
6C07: 65         LD      H,L             
6C08: 20 67      JR      NZ,$6C71        
6C0A: 6F         LD      L,A             
6C0B: 6F         LD      L,A             
6C0C: 64         LD      H,H             
6C0D: 21 20 20   LD      HL,$2020        
6C10: 20 20      JR      NZ,$6C32        
6C12: 59         LD      E,C             
6C13: 6F         LD      L,A             
6C14: 75         LD      (HL),L          
6C15: 5E         LD      E,(HL)          
6C16: 72         LD      (HL),D          
6C17: 65         LD      H,L             
6C18: 20 61      JR      NZ,$6C7B        
6C1A: 20 70      JR      NZ,$6C8C        
6C1C: 72         LD      (HL),D          
6C1D: 6F         LD      L,A             
6C1E: 2C         INC     L               
6C1F: 20 20      JR      NZ,$6C41        
6C21: 20 61      JR      NZ,$6C84        
6C23: 72         LD      (HL),D          
6C24: 65         LD      H,L             
6C25: 6E         LD      L,(HL)          
6C26: 5E         LD      E,(HL)          
6C27: 74         LD      (HL),H          
6C28: 20 79      JR      NZ,$6CA3        
6C2A: 6F         LD      L,A             
6C2B: 75         LD      (HL),L          
6C2C: 3F         CCF                     
6C2D: 20 20      JR      NZ,$6C4F        
6C2F: 20 20      JR      NZ,$6C51        
6C31: 20 2E      JR      NZ,$6C61        
6C33: 2E 2E      LD      L,$2E           
6C35: 20 2E      JR      NZ,$6C65        
6C37: 2E 2E      LD      L,$2E           
6C39: 20 2E      JR      NZ,$6C69        
6C3B: 2E 2E      LD      L,$2E           
6C3D: 20 2E      JR      NZ,$6C6D        
6C3F: 2E 2E      LD      L,$2E           
6C41: 20 57      JR      NZ,$6C9A        
6C43: 65         LD      H,L             
6C44: 6C         LD      L,H             
6C45: 6C         LD      L,H             
6C46: 2C         INC     L               
6C47: 20 62      JR      NZ,$6CAB        
6C49: 65         LD      H,L             
6C4A: 61         LD      H,C             
6C4B: 74         LD      (HL),H          
6C4C: 20 69      JR      NZ,$6CB7        
6C4E: 74         LD      (HL),H          
6C4F: 21 20 20   LD      HL,$2020        
6C52: 50         LD      D,B             
6C53: 72         LD      (HL),D          
6C54: 6F         LD      L,A             
6C55: 73         LD      (HL),E          
6C56: 20 61      JR      NZ,$6CB9        
6C58: 72         LD      (HL),D          
6C59: 65         LD      H,L             
6C5A: 6E         LD      L,(HL)          
6C5B: 5E         LD      E,(HL)          
6C5C: 74         LD      (HL),H          
6C5D: 20 20      JR      NZ,$6C7F        
6C5F: 20 20      JR      NZ,$6C81        
6C61: 20 61      JR      NZ,$6CC4        
6C63: 6C         LD      L,H             
6C64: 6C         LD      L,H             
6C65: 6F         LD      L,A             
6C66: 77         LD      (HL),A          
6C67: 65         LD      H,L             
6C68: 64         LD      H,H             
6C69: 20 69      JR      NZ,$6CD4        
6C6B: 6E         LD      L,(HL)          
6C6C: 20 68      JR      NZ,$6CD6        
6C6E: 65         LD      H,L             
6C6F: 72         LD      (HL),D          
6C70: 65         LD      H,L             
6C71: 21 FF 47   LD      HL,$47FF        
6C74: 6F         LD      L,A             
6C75: 20 61      JR      NZ,$6CD8        
6C77: 77         LD      (HL),A          
6C78: 61         LD      H,C             
6C79: 79         LD      A,C             
6C7A: 21 FF 51   LD      HL,$51FF        
6C7D: 75         LD      (HL),L          
6C7E: 69         LD      L,C             
6C7F: 74         LD      (HL),H          
6C80: 20 69      JR      NZ,$6CEB        
6C82: 74         LD      (HL),H          
6C83: 21 FF 54   LD      HL,$54FF        
6C86: 68         LD      L,B             
6C87: 69         LD      L,C             
6C88: 73         LD      (HL),E          
6C89: 20 69      JR      NZ,$6CF4        
6C8B: 73         LD      (HL),E          
6C8C: 20 6E      JR      NZ,$6CFC        
6C8E: 6F         LD      L,A             
6C8F: 74         LD      (HL),H          
6C90: 20 61      JR      NZ,$6CF3        
6C92: 20 20      JR      NZ,$6CB4        
6C94: 20 63      JR      NZ,$6CF9        
6C96: 68         LD      L,B             
6C97: 65         LD      H,L             
6C98: 73         LD      (HL),E          
6C99: 74         LD      (HL),H          
6C9A: 2E 2E      LD      L,$2E           
6C9C: 2E 20      LD      L,$20           
6C9E: 20 57      JR      NZ,$6CF7        
6CA0: 68         LD      L,B             
6CA1: 61         LD      H,C             
6CA2: 74         LD      (HL),H          
6CA3: 3F         CCF                     
6CA4: 20 59      JR      NZ,$6CFF        
6CA6: 6F         LD      L,A             
6CA7: 75         LD      (HL),L          
6CA8: 20 6B      JR      NZ,$6D15        
6CAA: 6E         LD      L,(HL)          
6CAB: 65         LD      H,L             
6CAC: 77         LD      (HL),A          
6CAD: 20 74      JR      NZ,$6D23        
6CAF: 68         LD      L,B             
6CB0: 61         LD      H,C             
6CB1: 74         LD      (HL),H          
6CB2: 3F         CCF                     
6CB3: 20 20      JR      NZ,$6CD5        
6CB5: 4F         LD      C,A             
6CB6: 6B         LD      L,E             
6CB7: 61         LD      H,C             
6CB8: 79         LD      A,C             
6CB9: 2E FF      LD      L,$FF           
6CBB: 23         INC     HL              
6CBC: 23         INC     HL              
6CBD: 23         INC     HL              
6CBE: 23         INC     HL              
6CBF: 23         INC     HL              
6CC0: 20 63      JR      NZ,$6D25        
6CC2: 68         LD      L,B             
6CC3: 65         LD      H,L             
6CC4: 63         LD      H,E             
6CC5: 6B         LD      L,E             
6CC6: 65         LD      H,L             
6CC7: 64         LD      H,H             
6CC8: 20 20      JR      NZ,$6CEA        
6CCA: 20 74      JR      NZ,$6D40        
6CCC: 68         LD      L,B             
6CCD: 65         LD      H,L             
6CCE: 20 63      JR      NZ,$6D33        
6CD0: 68         LD      L,B             
6CD1: 65         LD      H,L             
6CD2: 73         LD      (HL),E          
6CD3: 74         LD      (HL),H          
6CD4: 2E 20      LD      L,$20           
6CD6: 20 57      JR      NZ,$6D2F        
6CD8: 6F         LD      L,A             
6CD9: 77         LD      (HL),A          
6CDA: 21 54 68   LD      HL,$6854        
6CDD: 69         LD      L,C             
6CDE: 73         LD      (HL),E          
6CDF: 20 69      JR      NZ,$6D4A        
6CE1: 73         LD      (HL),E          
6CE2: 20 61      JR      NZ,$6D45        
6CE4: 20 6E      JR      NZ,$6D54        
6CE6: 69         LD      L,C             
6CE7: 63         LD      H,E             
6CE8: 65         LD      H,L             
6CE9: 20 20      JR      NZ,$6D0B        
6CEB: 63         LD      H,E             
6CEC: 68         LD      L,B             
6CED: 65         LD      H,L             
6CEE: 73         LD      (HL),E          
6CEF: 74         LD      (HL),H          
6CF0: 21 FF 49   LD      HL,$49FF        
6CF3: 74         LD      (HL),H          
6CF4: 5E         LD      E,(HL)          
6CF5: 73         LD      (HL),E          
6CF6: 20 61      JR      NZ,$6D59        
6CF8: 6C         LD      L,H             
6CF9: 6C         LD      L,H             
6CFA: 20 72      JR      NZ,$6D6E        
6CFC: 65         LD      H,L             
6CFD: 61         LD      H,C             
6CFE: 64         LD      H,H             
6CFF: 79         LD      A,C             
6D00: 2C         INC     L               
6D01: 20 69      JR      NZ,$6D6C        
6D03: 74         LD      (HL),H          
6D04: 20 69      JR      NZ,$6D6F        
6D06: 73         LD      (HL),E          
6D07: 21 20 20   LD      HL,$2020        
6D0A: 54         LD      D,H             
6D0B: 61         LD      H,C             
6D0C: 6B         LD      L,E             
6D0D: 65         LD      H,L             
6D0E: 20 20      JR      NZ,$6D30        
6D10: 20 20      JR      NZ,$6D32        
6D12: 63         LD      H,E             
6D13: 61         LD      H,C             
6D14: 72         LD      (HL),D          
6D15: 65         LD      H,L             
6D16: 2C         INC     L               
6D17: 20 61      JR      NZ,$6D7A        
6D19: 73         LD      (HL),E          
6D1A: 20 74      JR      NZ,$6D90        
6D1C: 68         LD      L,B             
6D1D: 65         LD      H,L             
6D1E: 72         LD      (HL),D          
6D1F: 65         LD      H,L             
6D20: 5E         LD      E,(HL)          
6D21: 73         LD      (HL),E          
6D22: 6E         LD      L,(HL)          
6D23: 6F         LD      L,A             
6D24: 74         LD      (HL),H          
6D25: 20 6D      JR      NZ,$6D94        
6D27: 75         LD      (HL),L          
6D28: 63         LD      H,E             
6D29: 68         LD      L,B             
6D2A: 20 74      JR      NZ,$6DA0        
6D2C: 68         LD      L,B             
6D2D: 65         LD      H,L             
6D2E: 72         LD      (HL),D          
6D2F: 65         LD      H,L             
6D30: 21 20 57   LD      HL,$5720        
6D33: 68         LD      L,B             
6D34: 79         LD      A,C             
6D35: 20 6E      JR      NZ,$6DA5        
6D37: 6F         LD      L,A             
6D38: 74         LD      (HL),H          
6D39: 20 74      JR      NZ,$6DAF        
6D3B: 72         LD      (HL),D          
6D3C: 79         LD      A,C             
6D3D: 20 61      JR      NZ,$6DA0        
6D3F: 20 20      JR      NZ,$6D61        
6D41: 20 62      JR      NZ,$6DA5        
6D43: 69         LD      L,C             
6D44: 74         LD      (HL),H          
6D45: 20 69      JR      NZ,$6DB0        
6D47: 6E         LD      L,(HL)          
6D48: 20 6D      JR      NZ,$6DB7        
6D4A: 79         LD      A,C             
6D4B: 20 68      JR      NZ,$6DB5        
6D4D: 75         LD      (HL),L          
6D4E: 74         LD      (HL),H          
6D4F: 3F         CCF                     
6D50: FF         RST     0X38            
6D51: 48         LD      C,B             
6D52: 65         LD      H,L             
6D53: 79         LD      A,C             
6D54: 21 20 20   LD      HL,$2020        
6D57: 57         LD      D,A             
6D58: 68         LD      L,B             
6D59: 61         LD      H,C             
6D5A: 74         LD      (HL),H          
6D5B: 20 61      JR      NZ,$6DBE        
6D5D: 72         LD      (HL),D          
6D5E: 65         LD      H,L             
6D5F: 20 20      JR      NZ,$6D81        
6D61: 79         LD      A,C             
6D62: 61         LD      H,C             
6D63: 20 64      JR      NZ,$6DC9        
6D65: 6F         LD      L,A             
6D66: 69         LD      L,C             
6D67: 6E         LD      L,(HL)          
6D68: 5E         LD      E,(HL)          
6D69: 20 69      JR      NZ,$6DD4        
6D6B: 6E         LD      L,(HL)          
6D6C: 20 6D      JR      NZ,$6DDB        
6D6E: 79         LD      A,C             
6D6F: 20 20      JR      NZ,$6D91        
6D71: 63         LD      H,E             
6D72: 68         LD      L,B             
6D73: 65         LD      H,L             
6D74: 73         LD      (HL),E          
6D75: 74         LD      (HL),H          
6D76: 3F         CCF                     
6D77: 21 20 20   LD      HL,$2020        
6D7A: 57         LD      D,A             
6D7B: 68         LD      L,B             
6D7C: 65         LD      H,L             
6D7D: 72         LD      (HL),D          
6D7E: 65         LD      H,L             
6D7F: 5E         LD      E,(HL)          
6D80: 64         LD      H,H             
6D81: 79         LD      A,C             
6D82: 6F         LD      L,A             
6D83: 75         LD      (HL),L          
6D84: 20 6C      JR      NZ,$6DF2        
6D86: 65         LD      H,L             
6D87: 61         LD      H,C             
6D88: 72         LD      (HL),D          
6D89: 6E         LD      L,(HL)          
6D8A: 20 74      JR      NZ,$6E00        
6D8C: 61         LD      H,C             
6D8D: 20 64      JR      NZ,$6DF3        
6D8F: 6F         LD      L,A             
6D90: 20 73      JR      NZ,$6E05        
6D92: 75         LD      (HL),L          
6D93: 63         LD      H,E             
6D94: 68         LD      L,B             
6D95: 20 61      JR      NZ,$6DF8        
6D97: 20 74      JR      NZ,$6E0D        
6D99: 68         LD      L,B             
6D9A: 69         LD      L,C             
6D9B: 6E         LD      L,(HL)          
6D9C: 67         LD      H,A             
6D9D: 3F         CCF                     
6D9E: 21 FF FF   LD      HL,$FFFF        
6DA1: FF         RST     0X38            
6DA2: FF         RST     0X38            
6DA3: FF         RST     0X38            
6DA4: FF         RST     0X38            
6DA5: FF         RST     0X38            
6DA6: FF         RST     0X38            
6DA7: FF         RST     0X38            
6DA8: FF         RST     0X38            
6DA9: FF         RST     0X38            
6DAA: FF         RST     0X38            
6DAB: FF         RST     0X38            
6DAC: FF         RST     0X38            
6DAD: FF         RST     0X38            
6DAE: FF         RST     0X38            
6DAF: FF         RST     0X38            
6DB0: FF         RST     0X38            
6DB1: FF         RST     0X38            
6DB2: FF         RST     0X38            
6DB3: FF         RST     0X38            
6DB4: FF         RST     0X38            
6DB5: FF         RST     0X38            
6DB6: FF         RST     0X38            
6DB7: FF         RST     0X38            
6DB8: FF         RST     0X38            
6DB9: FF         RST     0X38            
6DBA: FF         RST     0X38            
6DBB: FF         RST     0X38            
6DBC: FF         RST     0X38            
6DBD: FF         RST     0X38            
6DBE: FF         RST     0X38            
6DBF: FF         RST     0X38            
6DC0: FF         RST     0X38            
6DC1: FF         RST     0X38            
6DC2: FF         RST     0X38            
6DC3: FF         RST     0X38            
6DC4: FF         RST     0X38            
6DC5: FF         RST     0X38            
6DC6: FF         RST     0X38            
6DC7: FF         RST     0X38            
6DC8: FF         RST     0X38            
6DC9: FF         RST     0X38            
6DCA: FF         RST     0X38            
6DCB: FF         RST     0X38            
6DCC: FF         RST     0X38            
6DCD: FF         RST     0X38            
6DCE: FF         RST     0X38            
6DCF: FF         RST     0X38            
6DD0: FF         RST     0X38            
6DD1: FF         RST     0X38            
6DD2: FF         RST     0X38            
6DD3: FF         RST     0X38            
6DD4: FF         RST     0X38            
6DD5: FF         RST     0X38            
6DD6: FF         RST     0X38            
6DD7: FF         RST     0X38            
6DD8: FF         RST     0X38            
6DD9: FF         RST     0X38            
6DDA: FF         RST     0X38            
6DDB: FF         RST     0X38            
6DDC: FF         RST     0X38            
6DDD: FF         RST     0X38            
6DDE: FF         RST     0X38            
6DDF: FF         RST     0X38            
6DE0: FF         RST     0X38            
6DE1: FF         RST     0X38            
6DE2: FF         RST     0X38            
6DE3: FF         RST     0X38            
6DE4: FF         RST     0X38            
6DE5: FF         RST     0X38            
6DE6: FF         RST     0X38            
6DE7: FF         RST     0X38            
6DE8: FF         RST     0X38            
6DE9: FF         RST     0X38            
6DEA: FF         RST     0X38            
6DEB: FF         RST     0X38            
6DEC: FF         RST     0X38            
6DED: FF         RST     0X38            
6DEE: FF         RST     0X38            
6DEF: FF         RST     0X38            
6DF0: FF         RST     0X38            
6DF1: FF         RST     0X38            
6DF2: FF         RST     0X38            
6DF3: FF         RST     0X38            
6DF4: FF         RST     0X38            
6DF5: FF         RST     0X38            
6DF6: FF         RST     0X38            
6DF7: FF         RST     0X38            
6DF8: FF         RST     0X38            
6DF9: FF         RST     0X38            
6DFA: FF         RST     0X38            
6DFB: FF         RST     0X38            
6DFC: FF         RST     0X38            
6DFD: FF         RST     0X38            
6DFE: FF         RST     0X38            
6DFF: FF         RST     0X38            
6E00: FF         RST     0X38            
6E01: FF         RST     0X38            
6E02: FF         RST     0X38            
6E03: FF         RST     0X38            
6E04: FF         RST     0X38            
6E05: FF         RST     0X38            
6E06: FF         RST     0X38            
6E07: FF         RST     0X38            
6E08: FF         RST     0X38            
6E09: FF         RST     0X38            
6E0A: FF         RST     0X38            
6E0B: FF         RST     0X38            
6E0C: FF         RST     0X38            
6E0D: FF         RST     0X38            
6E0E: FF         RST     0X38            
6E0F: FF         RST     0X38            
6E10: FF         RST     0X38            
6E11: FF         RST     0X38            
6E12: FF         RST     0X38            
6E13: FF         RST     0X38            
6E14: FF         RST     0X38            
6E15: FF         RST     0X38            
6E16: FF         RST     0X38            
6E17: FF         RST     0X38            
6E18: FF         RST     0X38            
6E19: FF         RST     0X38            
6E1A: FF         RST     0X38            
6E1B: FF         RST     0X38            
6E1C: FF         RST     0X38            
6E1D: FF         RST     0X38            
6E1E: FF         RST     0X38            
6E1F: FF         RST     0X38            
6E20: FF         RST     0X38            
6E21: FF         RST     0X38            
6E22: FF         RST     0X38            
6E23: FF         RST     0X38            
6E24: FF         RST     0X38            
6E25: FF         RST     0X38            
6E26: FF         RST     0X38            
6E27: FF         RST     0X38            
6E28: FF         RST     0X38            
6E29: FF         RST     0X38            
6E2A: FF         RST     0X38            
6E2B: FF         RST     0X38            
6E2C: FF         RST     0X38            
6E2D: FF         RST     0X38            
6E2E: FF         RST     0X38            
6E2F: FF         RST     0X38            
6E30: FF         RST     0X38            
6E31: FF         RST     0X38            
6E32: FF         RST     0X38            
6E33: FF         RST     0X38            
6E34: FF         RST     0X38            
6E35: FF         RST     0X38            
6E36: FF         RST     0X38            
6E37: FF         RST     0X38            
6E38: FF         RST     0X38            
6E39: FF         RST     0X38            
6E3A: FF         RST     0X38            
6E3B: FF         RST     0X38            
6E3C: FF         RST     0X38            
6E3D: FF         RST     0X38            
6E3E: FF         RST     0X38            
6E3F: FF         RST     0X38            
6E40: FF         RST     0X38            
6E41: FF         RST     0X38            
6E42: FF         RST     0X38            
6E43: FF         RST     0X38            
6E44: FF         RST     0X38            
6E45: FF         RST     0X38            
6E46: FF         RST     0X38            
6E47: FF         RST     0X38            
6E48: FF         RST     0X38            
6E49: FF         RST     0X38            
6E4A: FF         RST     0X38            
6E4B: FF         RST     0X38            
6E4C: FF         RST     0X38            
6E4D: FF         RST     0X38            
6E4E: FF         RST     0X38            
6E4F: FF         RST     0X38            
6E50: FF         RST     0X38            
6E51: FF         RST     0X38            
6E52: FF         RST     0X38            
6E53: FF         RST     0X38            
6E54: FF         RST     0X38            
6E55: FF         RST     0X38            
6E56: FF         RST     0X38            
6E57: FF         RST     0X38            
6E58: FF         RST     0X38            
6E59: FF         RST     0X38            
6E5A: FF         RST     0X38            
6E5B: FF         RST     0X38            
6E5C: FF         RST     0X38            
6E5D: FF         RST     0X38            
6E5E: FF         RST     0X38            
6E5F: FF         RST     0X38            
6E60: FF         RST     0X38            
6E61: FF         RST     0X38            
6E62: FF         RST     0X38            
6E63: FF         RST     0X38            
6E64: FF         RST     0X38            
6E65: FF         RST     0X38            
6E66: FF         RST     0X38            
6E67: FF         RST     0X38            
6E68: FF         RST     0X38            
6E69: FF         RST     0X38            
6E6A: FF         RST     0X38            
6E6B: FF         RST     0X38            
6E6C: FF         RST     0X38            
6E6D: FF         RST     0X38            
6E6E: FF         RST     0X38            
6E6F: FF         RST     0X38            
6E70: FF         RST     0X38            
6E71: FF         RST     0X38            
6E72: FF         RST     0X38            
6E73: FF         RST     0X38            
6E74: FF         RST     0X38            
6E75: FF         RST     0X38            
6E76: FF         RST     0X38            
6E77: FF         RST     0X38            
6E78: FF         RST     0X38            
6E79: FF         RST     0X38            
6E7A: FF         RST     0X38            
6E7B: FF         RST     0X38            
6E7C: FF         RST     0X38            
6E7D: FF         RST     0X38            
6E7E: FF         RST     0X38            
6E7F: FF         RST     0X38            
6E80: FF         RST     0X38            
6E81: FF         RST     0X38            
6E82: FF         RST     0X38            
6E83: FF         RST     0X38            
6E84: FF         RST     0X38            
6E85: FF         RST     0X38            
6E86: FF         RST     0X38            
6E87: FF         RST     0X38            
6E88: FF         RST     0X38            
6E89: FF         RST     0X38            
6E8A: FF         RST     0X38            
6E8B: FF         RST     0X38            
6E8C: FF         RST     0X38            
6E8D: FF         RST     0X38            
6E8E: FF         RST     0X38            
6E8F: FF         RST     0X38            
6E90: FF         RST     0X38            
6E91: FF         RST     0X38            
6E92: FF         RST     0X38            
6E93: FF         RST     0X38            
6E94: FF         RST     0X38            
6E95: FF         RST     0X38            
6E96: FF         RST     0X38            
6E97: FF         RST     0X38            
6E98: FF         RST     0X38            
6E99: FF         RST     0X38            
6E9A: FF         RST     0X38            
6E9B: FF         RST     0X38            
6E9C: FF         RST     0X38            
6E9D: FF         RST     0X38            
6E9E: FF         RST     0X38            
6E9F: FF         RST     0X38            
6EA0: FF         RST     0X38            
6EA1: FF         RST     0X38            
6EA2: FF         RST     0X38            
6EA3: FF         RST     0X38            
6EA4: FF         RST     0X38            
6EA5: FF         RST     0X38            
6EA6: FF         RST     0X38            
6EA7: FF         RST     0X38            
6EA8: FF         RST     0X38            
6EA9: FF         RST     0X38            
6EAA: FF         RST     0X38            
6EAB: FF         RST     0X38            
6EAC: FF         RST     0X38            
6EAD: FF         RST     0X38            
6EAE: FF         RST     0X38            
6EAF: FF         RST     0X38            
6EB0: FF         RST     0X38            
6EB1: FF         RST     0X38            
6EB2: FF         RST     0X38            
6EB3: FF         RST     0X38            
6EB4: FF         RST     0X38            
6EB5: FF         RST     0X38            
6EB6: FF         RST     0X38            
6EB7: FF         RST     0X38            
6EB8: FF         RST     0X38            
6EB9: FF         RST     0X38            
6EBA: FF         RST     0X38            
6EBB: FF         RST     0X38            
6EBC: FF         RST     0X38            
6EBD: FF         RST     0X38            
6EBE: FF         RST     0X38            
6EBF: FF         RST     0X38            
6EC0: FF         RST     0X38            
6EC1: FF         RST     0X38            
6EC2: FF         RST     0X38            
6EC3: FF         RST     0X38            
6EC4: FF         RST     0X38            
6EC5: FF         RST     0X38            
6EC6: FF         RST     0X38            
6EC7: FF         RST     0X38            
6EC8: FF         RST     0X38            
6EC9: FF         RST     0X38            
6ECA: FF         RST     0X38            
6ECB: FF         RST     0X38            
6ECC: FF         RST     0X38            
6ECD: FF         RST     0X38            
6ECE: FF         RST     0X38            
6ECF: FF         RST     0X38            
6ED0: FF         RST     0X38            
6ED1: FF         RST     0X38            
6ED2: FF         RST     0X38            
6ED3: FF         RST     0X38            
6ED4: FF         RST     0X38            
6ED5: FF         RST     0X38            
6ED6: FF         RST     0X38            
6ED7: FF         RST     0X38            
6ED8: FF         RST     0X38            
6ED9: FF         RST     0X38            
6EDA: FF         RST     0X38            
6EDB: FF         RST     0X38            
6EDC: FF         RST     0X38            
6EDD: FF         RST     0X38            
6EDE: FF         RST     0X38            
6EDF: FF         RST     0X38            
6EE0: FF         RST     0X38            
6EE1: FF         RST     0X38            
6EE2: FF         RST     0X38            
6EE3: FF         RST     0X38            
6EE4: FF         RST     0X38            
6EE5: FF         RST     0X38            
6EE6: FF         RST     0X38            
6EE7: FF         RST     0X38            
6EE8: FF         RST     0X38            
6EE9: FF         RST     0X38            
6EEA: FF         RST     0X38            
6EEB: FF         RST     0X38            
6EEC: FF         RST     0X38            
6EED: FF         RST     0X38            
6EEE: FF         RST     0X38            
6EEF: FF         RST     0X38            
6EF0: FF         RST     0X38            
6EF1: FF         RST     0X38            
6EF2: FF         RST     0X38            
6EF3: FF         RST     0X38            
6EF4: FF         RST     0X38            
6EF5: FF         RST     0X38            
6EF6: FF         RST     0X38            
6EF7: FF         RST     0X38            
6EF8: FF         RST     0X38            
6EF9: FF         RST     0X38            
6EFA: FF         RST     0X38            
6EFB: FF         RST     0X38            
6EFC: FF         RST     0X38            
6EFD: FF         RST     0X38            
6EFE: FF         RST     0X38            
6EFF: FF         RST     0X38            
6F00: FF         RST     0X38            
6F01: FF         RST     0X38            
6F02: FF         RST     0X38            
6F03: FF         RST     0X38            
6F04: FF         RST     0X38            
6F05: FF         RST     0X38            
6F06: FF         RST     0X38            
6F07: FF         RST     0X38            
6F08: FF         RST     0X38            
6F09: FF         RST     0X38            
6F0A: FF         RST     0X38            
6F0B: FF         RST     0X38            
6F0C: FF         RST     0X38            
6F0D: FF         RST     0X38            
6F0E: FF         RST     0X38            
6F0F: FF         RST     0X38            
6F10: FF         RST     0X38            
6F11: FF         RST     0X38            
6F12: FF         RST     0X38            
6F13: FF         RST     0X38            
6F14: FF         RST     0X38            
6F15: FF         RST     0X38            
6F16: FF         RST     0X38            
6F17: FF         RST     0X38            
6F18: FF         RST     0X38            
6F19: FF         RST     0X38            
6F1A: FF         RST     0X38            
6F1B: FF         RST     0X38            
6F1C: FF         RST     0X38            
6F1D: FF         RST     0X38            
6F1E: FF         RST     0X38            
6F1F: FF         RST     0X38            
6F20: FF         RST     0X38            
6F21: FF         RST     0X38            
6F22: FF         RST     0X38            
6F23: FF         RST     0X38            
6F24: FF         RST     0X38            
6F25: FF         RST     0X38            
6F26: FF         RST     0X38            
6F27: FF         RST     0X38            
6F28: FF         RST     0X38            
6F29: FF         RST     0X38            
6F2A: FF         RST     0X38            
6F2B: FF         RST     0X38            
6F2C: FF         RST     0X38            
6F2D: FF         RST     0X38            
6F2E: FF         RST     0X38            
6F2F: FF         RST     0X38            
6F30: FF         RST     0X38            
6F31: FF         RST     0X38            
6F32: FF         RST     0X38            
6F33: FF         RST     0X38            
6F34: FF         RST     0X38            
6F35: FF         RST     0X38            
6F36: FF         RST     0X38            
6F37: FF         RST     0X38            
6F38: FF         RST     0X38            
6F39: FF         RST     0X38            
6F3A: FF         RST     0X38            
6F3B: FF         RST     0X38            
6F3C: FF         RST     0X38            
6F3D: FF         RST     0X38            
6F3E: FF         RST     0X38            
6F3F: FF         RST     0X38            
6F40: FF         RST     0X38            
6F41: FF         RST     0X38            
6F42: FF         RST     0X38            
6F43: FF         RST     0X38            
6F44: FF         RST     0X38            
6F45: FF         RST     0X38            
6F46: FF         RST     0X38            
6F47: FF         RST     0X38            
6F48: FF         RST     0X38            
6F49: FF         RST     0X38            
6F4A: FF         RST     0X38            
6F4B: FF         RST     0X38            
6F4C: FF         RST     0X38            
6F4D: FF         RST     0X38            
6F4E: FF         RST     0X38            
6F4F: FF         RST     0X38            
6F50: FF         RST     0X38            
6F51: FF         RST     0X38            
6F52: FF         RST     0X38            
6F53: FF         RST     0X38            
6F54: FF         RST     0X38            
6F55: FF         RST     0X38            
6F56: FF         RST     0X38            
6F57: FF         RST     0X38            
6F58: FF         RST     0X38            
6F59: FF         RST     0X38            
6F5A: FF         RST     0X38            
6F5B: FF         RST     0X38            
6F5C: FF         RST     0X38            
6F5D: FF         RST     0X38            
6F5E: FF         RST     0X38            
6F5F: FF         RST     0X38            
6F60: FF         RST     0X38            
6F61: FF         RST     0X38            
6F62: FF         RST     0X38            
6F63: FF         RST     0X38            
6F64: FF         RST     0X38            
6F65: FF         RST     0X38            
6F66: FF         RST     0X38            
6F67: FF         RST     0X38            
6F68: FF         RST     0X38            
6F69: FF         RST     0X38            
6F6A: FF         RST     0X38            
6F6B: FF         RST     0X38            
6F6C: FF         RST     0X38            
6F6D: FF         RST     0X38            
6F6E: FF         RST     0X38            
6F6F: FF         RST     0X38            
6F70: FF         RST     0X38            
6F71: FF         RST     0X38            
6F72: FF         RST     0X38            
6F73: FF         RST     0X38            
6F74: FF         RST     0X38            
6F75: FF         RST     0X38            
6F76: FF         RST     0X38            
6F77: FF         RST     0X38            
6F78: FF         RST     0X38            
6F79: FF         RST     0X38            
6F7A: FF         RST     0X38            
6F7B: FF         RST     0X38            
6F7C: FF         RST     0X38            
6F7D: FF         RST     0X38            
6F7E: FF         RST     0X38            
6F7F: FF         RST     0X38            
6F80: FF         RST     0X38            
6F81: FF         RST     0X38            
6F82: FF         RST     0X38            
6F83: FF         RST     0X38            
6F84: FF         RST     0X38            
6F85: FF         RST     0X38            
6F86: FF         RST     0X38            
6F87: FF         RST     0X38            
6F88: FF         RST     0X38            
6F89: FF         RST     0X38            
6F8A: FF         RST     0X38            
6F8B: FF         RST     0X38            
6F8C: FF         RST     0X38            
6F8D: FF         RST     0X38            
6F8E: FF         RST     0X38            
6F8F: FF         RST     0X38            
6F90: FF         RST     0X38            
6F91: FF         RST     0X38            
6F92: FF         RST     0X38            
6F93: FF         RST     0X38            
6F94: FF         RST     0X38            
6F95: FF         RST     0X38            
6F96: FF         RST     0X38            
6F97: FF         RST     0X38            
6F98: FF         RST     0X38            
6F99: FF         RST     0X38            
6F9A: FF         RST     0X38            
6F9B: FF         RST     0X38            
6F9C: FF         RST     0X38            
6F9D: FF         RST     0X38            
6F9E: FF         RST     0X38            
6F9F: FF         RST     0X38            
6FA0: FF         RST     0X38            
6FA1: FF         RST     0X38            
6FA2: FF         RST     0X38            
6FA3: FF         RST     0X38            
6FA4: FF         RST     0X38            
6FA5: FF         RST     0X38            
6FA6: FF         RST     0X38            
6FA7: FF         RST     0X38            
6FA8: FF         RST     0X38            
6FA9: FF         RST     0X38            
6FAA: FF         RST     0X38            
6FAB: FF         RST     0X38            
6FAC: FF         RST     0X38            
6FAD: FF         RST     0X38            
6FAE: FF         RST     0X38            
6FAF: FF         RST     0X38            
6FB0: FF         RST     0X38            
6FB1: FF         RST     0X38            
6FB2: FF         RST     0X38            
6FB3: FF         RST     0X38            
6FB4: FF         RST     0X38            
6FB5: FF         RST     0X38            
6FB6: FF         RST     0X38            
6FB7: FF         RST     0X38            
6FB8: FF         RST     0X38            
6FB9: FF         RST     0X38            
6FBA: FF         RST     0X38            
6FBB: FF         RST     0X38            
6FBC: FF         RST     0X38            
6FBD: FF         RST     0X38            
6FBE: FF         RST     0X38            
6FBF: FF         RST     0X38            
6FC0: FF         RST     0X38            
6FC1: FF         RST     0X38            
6FC2: FF         RST     0X38            
6FC3: FF         RST     0X38            
6FC4: FF         RST     0X38            
6FC5: FF         RST     0X38            
6FC6: FF         RST     0X38            
6FC7: FF         RST     0X38            
6FC8: FF         RST     0X38            
6FC9: FF         RST     0X38            
6FCA: FF         RST     0X38            
6FCB: FF         RST     0X38            
6FCC: FF         RST     0X38            
6FCD: FF         RST     0X38            
6FCE: FF         RST     0X38            
6FCF: FF         RST     0X38            
6FD0: FF         RST     0X38            
6FD1: FF         RST     0X38            
6FD2: FF         RST     0X38            
6FD3: FF         RST     0X38            
6FD4: FF         RST     0X38            
6FD5: FF         RST     0X38            
6FD6: FF         RST     0X38            
6FD7: FF         RST     0X38            
6FD8: FF         RST     0X38            
6FD9: FF         RST     0X38            
6FDA: FF         RST     0X38            
6FDB: FF         RST     0X38            
6FDC: FF         RST     0X38            
6FDD: FF         RST     0X38            
6FDE: FF         RST     0X38            
6FDF: FF         RST     0X38            
6FE0: FF         RST     0X38            
6FE1: FF         RST     0X38            
6FE2: FF         RST     0X38            
6FE3: FF         RST     0X38            
6FE4: FF         RST     0X38            
6FE5: FF         RST     0X38            
6FE6: FF         RST     0X38            
6FE7: FF         RST     0X38            
6FE8: FF         RST     0X38            
6FE9: FF         RST     0X38            
6FEA: FF         RST     0X38            
6FEB: FF         RST     0X38            
6FEC: FF         RST     0X38            
6FED: FF         RST     0X38            
6FEE: FF         RST     0X38            
6FEF: FF         RST     0X38            
6FF0: FF         RST     0X38            
6FF1: FF         RST     0X38            
6FF2: FF         RST     0X38            
6FF3: FF         RST     0X38            
6FF4: FF         RST     0X38            
6FF5: FF         RST     0X38            
6FF6: FF         RST     0X38            
6FF7: FF         RST     0X38            
6FF8: FF         RST     0X38            
6FF9: FF         RST     0X38            
6FFA: FF         RST     0X38            
6FFB: FF         RST     0X38            
6FFC: FF         RST     0X38            
6FFD: FF         RST     0X38            
6FFE: FF         RST     0X38            
6FFF: FF         RST     0X38            
7000: FF         RST     0X38            
7001: FF         RST     0X38            
7002: FF         RST     0X38            
7003: FF         RST     0X38            
7004: FF         RST     0X38            
7005: FF         RST     0X38            
7006: FF         RST     0X38            
7007: FF         RST     0X38            
7008: FF         RST     0X38            
7009: FF         RST     0X38            
700A: FF         RST     0X38            
700B: FF         RST     0X38            
700C: FF         RST     0X38            
700D: FF         RST     0X38            
700E: FF         RST     0X38            
700F: FF         RST     0X38            
7010: FF         RST     0X38            
7011: FF         RST     0X38            
7012: FF         RST     0X38            
7013: FF         RST     0X38            
7014: FF         RST     0X38            
7015: FF         RST     0X38            
7016: FF         RST     0X38            
7017: FF         RST     0X38            
7018: FF         RST     0X38            
7019: FF         RST     0X38            
701A: FF         RST     0X38            
701B: FF         RST     0X38            
701C: FF         RST     0X38            
701D: FF         RST     0X38            
701E: FF         RST     0X38            
701F: FF         RST     0X38            
7020: FF         RST     0X38            
7021: FF         RST     0X38            
7022: FF         RST     0X38            
7023: FF         RST     0X38            
7024: FF         RST     0X38            
7025: FF         RST     0X38            
7026: FF         RST     0X38            
7027: FF         RST     0X38            
7028: FF         RST     0X38            
7029: FF         RST     0X38            
702A: FF         RST     0X38            
702B: FF         RST     0X38            
702C: FF         RST     0X38            
702D: FF         RST     0X38            
702E: FF         RST     0X38            
702F: FF         RST     0X38            
7030: FF         RST     0X38            
7031: FF         RST     0X38            
7032: FF         RST     0X38            
7033: FF         RST     0X38            
7034: FF         RST     0X38            
7035: FF         RST     0X38            
7036: FF         RST     0X38            
7037: FF         RST     0X38            
7038: FF         RST     0X38            
7039: FF         RST     0X38            
703A: FF         RST     0X38            
703B: FF         RST     0X38            
703C: FF         RST     0X38            
703D: FF         RST     0X38            
703E: FF         RST     0X38            
703F: FF         RST     0X38            
7040: FF         RST     0X38            
7041: FF         RST     0X38            
7042: FF         RST     0X38            
7043: FF         RST     0X38            
7044: FF         RST     0X38            
7045: FF         RST     0X38            
7046: FF         RST     0X38            
7047: FF         RST     0X38            
7048: FF         RST     0X38            
7049: FF         RST     0X38            
704A: FF         RST     0X38            
704B: FF         RST     0X38            
704C: FF         RST     0X38            
704D: FF         RST     0X38            
704E: FF         RST     0X38            
704F: FF         RST     0X38            
7050: FF         RST     0X38            
7051: FF         RST     0X38            
7052: FF         RST     0X38            
7053: FF         RST     0X38            
7054: FF         RST     0X38            
7055: FF         RST     0X38            
7056: FF         RST     0X38            
7057: FF         RST     0X38            
7058: FF         RST     0X38            
7059: FF         RST     0X38            
705A: FF         RST     0X38            
705B: FF         RST     0X38            
705C: FF         RST     0X38            
705D: FF         RST     0X38            
705E: FF         RST     0X38            
705F: FF         RST     0X38            
7060: FF         RST     0X38            
7061: FF         RST     0X38            
7062: FF         RST     0X38            
7063: FF         RST     0X38            
7064: FF         RST     0X38            
7065: FF         RST     0X38            
7066: FF         RST     0X38            
7067: FF         RST     0X38            
7068: FF         RST     0X38            
7069: FF         RST     0X38            
706A: FF         RST     0X38            
706B: FF         RST     0X38            
706C: FF         RST     0X38            
706D: FF         RST     0X38            
706E: FF         RST     0X38            
706F: FF         RST     0X38            
7070: FF         RST     0X38            
7071: FF         RST     0X38            
7072: FF         RST     0X38            
7073: FF         RST     0X38            
7074: FF         RST     0X38            
7075: FF         RST     0X38            
7076: FF         RST     0X38            
7077: FF         RST     0X38            
7078: FF         RST     0X38            
7079: FF         RST     0X38            
707A: FF         RST     0X38            
707B: FF         RST     0X38            
707C: FF         RST     0X38            
707D: FF         RST     0X38            
707E: FF         RST     0X38            
707F: FF         RST     0X38            
7080: FF         RST     0X38            
7081: FF         RST     0X38            
7082: FF         RST     0X38            
7083: FF         RST     0X38            
7084: FF         RST     0X38            
7085: FF         RST     0X38            
7086: FF         RST     0X38            
7087: FF         RST     0X38            
7088: FF         RST     0X38            
7089: FF         RST     0X38            
708A: FF         RST     0X38            
708B: FF         RST     0X38            
708C: FF         RST     0X38            
708D: FF         RST     0X38            
708E: FF         RST     0X38            
708F: FF         RST     0X38            
7090: FF         RST     0X38            
7091: FF         RST     0X38            
7092: FF         RST     0X38            
7093: FF         RST     0X38            
7094: FF         RST     0X38            
7095: FF         RST     0X38            
7096: FF         RST     0X38            
7097: FF         RST     0X38            
7098: FF         RST     0X38            
7099: FF         RST     0X38            
709A: FF         RST     0X38            
709B: FF         RST     0X38            
709C: FF         RST     0X38            
709D: FF         RST     0X38            
709E: FF         RST     0X38            
709F: FF         RST     0X38            
70A0: FF         RST     0X38            
70A1: FF         RST     0X38            
70A2: FF         RST     0X38            
70A3: FF         RST     0X38            
70A4: FF         RST     0X38            
70A5: FF         RST     0X38            
70A6: FF         RST     0X38            
70A7: FF         RST     0X38            
70A8: FF         RST     0X38            
70A9: FF         RST     0X38            
70AA: FF         RST     0X38            
70AB: FF         RST     0X38            
70AC: FF         RST     0X38            
70AD: FF         RST     0X38            
70AE: FF         RST     0X38            
70AF: FF         RST     0X38            
70B0: FF         RST     0X38            
70B1: FF         RST     0X38            
70B2: FF         RST     0X38            
70B3: FF         RST     0X38            
70B4: FF         RST     0X38            
70B5: FF         RST     0X38            
70B6: FF         RST     0X38            
70B7: FF         RST     0X38            
70B8: FF         RST     0X38            
70B9: FF         RST     0X38            
70BA: FF         RST     0X38            
70BB: FF         RST     0X38            
70BC: FF         RST     0X38            
70BD: FF         RST     0X38            
70BE: FF         RST     0X38            
70BF: FF         RST     0X38            
70C0: FF         RST     0X38            
70C1: FF         RST     0X38            
70C2: FF         RST     0X38            
70C3: FF         RST     0X38            
70C4: FF         RST     0X38            
70C5: FF         RST     0X38            
70C6: FF         RST     0X38            
70C7: FF         RST     0X38            
70C8: FF         RST     0X38            
70C9: FF         RST     0X38            
70CA: FF         RST     0X38            
70CB: FF         RST     0X38            
70CC: FF         RST     0X38            
70CD: FF         RST     0X38            
70CE: FF         RST     0X38            
70CF: FF         RST     0X38            
70D0: FF         RST     0X38            
70D1: FF         RST     0X38            
70D2: FF         RST     0X38            
70D3: FF         RST     0X38            
70D4: FF         RST     0X38            
70D5: FF         RST     0X38            
70D6: FF         RST     0X38            
70D7: FF         RST     0X38            
70D8: FF         RST     0X38            
70D9: FF         RST     0X38            
70DA: FF         RST     0X38            
70DB: FF         RST     0X38            
70DC: FF         RST     0X38            
70DD: FF         RST     0X38            
70DE: FF         RST     0X38            
70DF: FF         RST     0X38            
70E0: FF         RST     0X38            
70E1: FF         RST     0X38            
70E2: FF         RST     0X38            
70E3: FF         RST     0X38            
70E4: FF         RST     0X38            
70E5: FF         RST     0X38            
70E6: FF         RST     0X38            
70E7: FF         RST     0X38            
70E8: FF         RST     0X38            
70E9: FF         RST     0X38            
70EA: FF         RST     0X38            
70EB: FF         RST     0X38            
70EC: FF         RST     0X38            
70ED: FF         RST     0X38            
70EE: FF         RST     0X38            
70EF: FF         RST     0X38            
70F0: FF         RST     0X38            
70F1: FF         RST     0X38            
70F2: FF         RST     0X38            
70F3: FF         RST     0X38            
70F4: FF         RST     0X38            
70F5: FF         RST     0X38            
70F6: FF         RST     0X38            
70F7: FF         RST     0X38            
70F8: FF         RST     0X38            
70F9: FF         RST     0X38            
70FA: FF         RST     0X38            
70FB: FF         RST     0X38            
70FC: FF         RST     0X38            
70FD: FF         RST     0X38            
70FE: FF         RST     0X38            
70FF: FF         RST     0X38            
7100: FF         RST     0X38            
7101: FF         RST     0X38            
7102: FF         RST     0X38            
7103: FF         RST     0X38            
7104: FF         RST     0X38            
7105: FF         RST     0X38            
7106: FF         RST     0X38            
7107: FF         RST     0X38            
7108: FF         RST     0X38            
7109: FF         RST     0X38            
710A: FF         RST     0X38            
710B: FF         RST     0X38            
710C: FF         RST     0X38            
710D: FF         RST     0X38            
710E: FF         RST     0X38            
710F: FF         RST     0X38            
7110: FF         RST     0X38            
7111: FF         RST     0X38            
7112: FF         RST     0X38            
7113: FF         RST     0X38            
7114: FF         RST     0X38            
7115: FF         RST     0X38            
7116: FF         RST     0X38            
7117: FF         RST     0X38            
7118: FF         RST     0X38            
7119: FF         RST     0X38            
711A: FF         RST     0X38            
711B: FF         RST     0X38            
711C: FF         RST     0X38            
711D: FF         RST     0X38            
711E: FF         RST     0X38            
711F: FF         RST     0X38            
7120: FF         RST     0X38            
7121: FF         RST     0X38            
7122: FF         RST     0X38            
7123: FF         RST     0X38            
7124: FF         RST     0X38            
7125: FF         RST     0X38            
7126: FF         RST     0X38            
7127: FF         RST     0X38            
7128: FF         RST     0X38            
7129: FF         RST     0X38            
712A: FF         RST     0X38            
712B: FF         RST     0X38            
712C: FF         RST     0X38            
712D: FF         RST     0X38            
712E: FF         RST     0X38            
712F: FF         RST     0X38            
7130: FF         RST     0X38            
7131: FF         RST     0X38            
7132: FF         RST     0X38            
7133: FF         RST     0X38            
7134: FF         RST     0X38            
7135: FF         RST     0X38            
7136: FF         RST     0X38            
7137: FF         RST     0X38            
7138: FF         RST     0X38            
7139: FF         RST     0X38            
713A: FF         RST     0X38            
713B: FF         RST     0X38            
713C: FF         RST     0X38            
713D: FF         RST     0X38            
713E: FF         RST     0X38            
713F: FF         RST     0X38            
7140: FF         RST     0X38            
7141: FF         RST     0X38            
7142: FF         RST     0X38            
7143: FF         RST     0X38            
7144: FF         RST     0X38            
7145: FF         RST     0X38            
7146: FF         RST     0X38            
7147: FF         RST     0X38            
7148: FF         RST     0X38            
7149: FF         RST     0X38            
714A: FF         RST     0X38            
714B: FF         RST     0X38            
714C: FF         RST     0X38            
714D: FF         RST     0X38            
714E: FF         RST     0X38            
714F: FF         RST     0X38            
7150: FF         RST     0X38            
7151: FF         RST     0X38            
7152: FF         RST     0X38            
7153: FF         RST     0X38            
7154: FF         RST     0X38            
7155: FF         RST     0X38            
7156: FF         RST     0X38            
7157: FF         RST     0X38            
7158: FF         RST     0X38            
7159: FF         RST     0X38            
715A: FF         RST     0X38            
715B: FF         RST     0X38            
715C: FF         RST     0X38            
715D: FF         RST     0X38            
715E: FF         RST     0X38            
715F: FF         RST     0X38            
7160: FF         RST     0X38            
7161: FF         RST     0X38            
7162: FF         RST     0X38            
7163: FF         RST     0X38            
7164: FF         RST     0X38            
7165: FF         RST     0X38            
7166: FF         RST     0X38            
7167: FF         RST     0X38            
7168: FF         RST     0X38            
7169: FF         RST     0X38            
716A: FF         RST     0X38            
716B: FF         RST     0X38            
716C: FF         RST     0X38            
716D: FF         RST     0X38            
716E: FF         RST     0X38            
716F: FF         RST     0X38            
7170: FF         RST     0X38            
7171: FF         RST     0X38            
7172: FF         RST     0X38            
7173: FF         RST     0X38            
7174: FF         RST     0X38            
7175: FF         RST     0X38            
7176: FF         RST     0X38            
7177: FF         RST     0X38            
7178: FF         RST     0X38            
7179: FF         RST     0X38            
717A: FF         RST     0X38            
717B: FF         RST     0X38            
717C: FF         RST     0X38            
717D: FF         RST     0X38            
717E: FF         RST     0X38            
717F: FF         RST     0X38            
7180: FF         RST     0X38            
7181: FF         RST     0X38            
7182: FF         RST     0X38            
7183: FF         RST     0X38            
7184: FF         RST     0X38            
7185: FF         RST     0X38            
7186: FF         RST     0X38            
7187: FF         RST     0X38            
7188: FF         RST     0X38            
7189: FF         RST     0X38            
718A: FF         RST     0X38            
718B: FF         RST     0X38            
718C: FF         RST     0X38            
718D: FF         RST     0X38            
718E: FF         RST     0X38            
718F: FF         RST     0X38            
7190: FF         RST     0X38            
7191: FF         RST     0X38            
7192: FF         RST     0X38            
7193: FF         RST     0X38            
7194: FF         RST     0X38            
7195: FF         RST     0X38            
7196: FF         RST     0X38            
7197: FF         RST     0X38            
7198: FF         RST     0X38            
7199: FF         RST     0X38            
719A: FF         RST     0X38            
719B: FF         RST     0X38            
719C: FF         RST     0X38            
719D: FF         RST     0X38            
719E: FF         RST     0X38            
719F: FF         RST     0X38            
71A0: FF         RST     0X38            
71A1: FF         RST     0X38            
71A2: FF         RST     0X38            
71A3: FF         RST     0X38            
71A4: FF         RST     0X38            
71A5: FF         RST     0X38            
71A6: FF         RST     0X38            
71A7: FF         RST     0X38            
71A8: FF         RST     0X38            
71A9: FF         RST     0X38            
71AA: FF         RST     0X38            
71AB: FF         RST     0X38            
71AC: FF         RST     0X38            
71AD: FF         RST     0X38            
71AE: FF         RST     0X38            
71AF: FF         RST     0X38            
71B0: FF         RST     0X38            
71B1: FF         RST     0X38            
71B2: FF         RST     0X38            
71B3: FF         RST     0X38            
71B4: FF         RST     0X38            
71B5: FF         RST     0X38            
71B6: FF         RST     0X38            
71B7: FF         RST     0X38            
71B8: FF         RST     0X38            
71B9: FF         RST     0X38            
71BA: FF         RST     0X38            
71BB: FF         RST     0X38            
71BC: FF         RST     0X38            
71BD: FF         RST     0X38            
71BE: FF         RST     0X38            
71BF: FF         RST     0X38            
71C0: FF         RST     0X38            
71C1: FF         RST     0X38            
71C2: FF         RST     0X38            
71C3: FF         RST     0X38            
71C4: FF         RST     0X38            
71C5: FF         RST     0X38            
71C6: FF         RST     0X38            
71C7: FF         RST     0X38            
71C8: FF         RST     0X38            
71C9: FF         RST     0X38            
71CA: FF         RST     0X38            
71CB: FF         RST     0X38            
71CC: FF         RST     0X38            
71CD: FF         RST     0X38            
71CE: FF         RST     0X38            
71CF: FF         RST     0X38            
71D0: FF         RST     0X38            
71D1: FF         RST     0X38            
71D2: FF         RST     0X38            
71D3: FF         RST     0X38            
71D4: FF         RST     0X38            
71D5: FF         RST     0X38            
71D6: FF         RST     0X38            
71D7: FF         RST     0X38            
71D8: FF         RST     0X38            
71D9: FF         RST     0X38            
71DA: FF         RST     0X38            
71DB: FF         RST     0X38            
71DC: FF         RST     0X38            
71DD: FF         RST     0X38            
71DE: FF         RST     0X38            
71DF: FF         RST     0X38            
71E0: FF         RST     0X38            
71E1: FF         RST     0X38            
71E2: FF         RST     0X38            
71E3: FF         RST     0X38            
71E4: FF         RST     0X38            
71E5: FF         RST     0X38            
71E6: FF         RST     0X38            
71E7: FF         RST     0X38            
71E8: FF         RST     0X38            
71E9: FF         RST     0X38            
71EA: FF         RST     0X38            
71EB: FF         RST     0X38            
71EC: FF         RST     0X38            
71ED: FF         RST     0X38            
71EE: FF         RST     0X38            
71EF: FF         RST     0X38            
71F0: FF         RST     0X38            
71F1: FF         RST     0X38            
71F2: FF         RST     0X38            
71F3: FF         RST     0X38            
71F4: FF         RST     0X38            
71F5: FF         RST     0X38            
71F6: FF         RST     0X38            
71F7: FF         RST     0X38            
71F8: FF         RST     0X38            
71F9: FF         RST     0X38            
71FA: FF         RST     0X38            
71FB: FF         RST     0X38            
71FC: FF         RST     0X38            
71FD: FF         RST     0X38            
71FE: FF         RST     0X38            
71FF: FF         RST     0X38            
7200: FF         RST     0X38            
7201: FF         RST     0X38            
7202: FF         RST     0X38            
7203: FF         RST     0X38            
7204: FF         RST     0X38            
7205: FF         RST     0X38            
7206: FF         RST     0X38            
7207: FF         RST     0X38            
7208: FF         RST     0X38            
7209: FF         RST     0X38            
720A: FF         RST     0X38            
720B: FF         RST     0X38            
720C: FF         RST     0X38            
720D: FF         RST     0X38            
720E: FF         RST     0X38            
720F: FF         RST     0X38            
7210: FF         RST     0X38            
7211: FF         RST     0X38            
7212: FF         RST     0X38            
7213: FF         RST     0X38            
7214: FF         RST     0X38            
7215: FF         RST     0X38            
7216: FF         RST     0X38            
7217: FF         RST     0X38            
7218: FF         RST     0X38            
7219: FF         RST     0X38            
721A: FF         RST     0X38            
721B: FF         RST     0X38            
721C: FF         RST     0X38            
721D: FF         RST     0X38            
721E: FF         RST     0X38            
721F: FF         RST     0X38            
7220: FF         RST     0X38            
7221: FF         RST     0X38            
7222: FF         RST     0X38            
7223: FF         RST     0X38            
7224: FF         RST     0X38            
7225: FF         RST     0X38            
7226: FF         RST     0X38            
7227: FF         RST     0X38            
7228: FF         RST     0X38            
7229: FF         RST     0X38            
722A: FF         RST     0X38            
722B: FF         RST     0X38            
722C: FF         RST     0X38            
722D: FF         RST     0X38            
722E: FF         RST     0X38            
722F: FF         RST     0X38            
7230: FF         RST     0X38            
7231: FF         RST     0X38            
7232: FF         RST     0X38            
7233: FF         RST     0X38            
7234: FF         RST     0X38            
7235: FF         RST     0X38            
7236: FF         RST     0X38            
7237: FF         RST     0X38            
7238: FF         RST     0X38            
7239: FF         RST     0X38            
723A: FF         RST     0X38            
723B: FF         RST     0X38            
723C: FF         RST     0X38            
723D: FF         RST     0X38            
723E: FF         RST     0X38            
723F: FF         RST     0X38            
7240: FF         RST     0X38            
7241: FF         RST     0X38            
7242: FF         RST     0X38            
7243: FF         RST     0X38            
7244: FF         RST     0X38            
7245: FF         RST     0X38            
7246: FF         RST     0X38            
7247: FF         RST     0X38            
7248: FF         RST     0X38            
7249: FF         RST     0X38            
724A: FF         RST     0X38            
724B: FF         RST     0X38            
724C: FF         RST     0X38            
724D: FF         RST     0X38            
724E: FF         RST     0X38            
724F: FF         RST     0X38            
7250: FF         RST     0X38            
7251: FF         RST     0X38            
7252: FF         RST     0X38            
7253: FF         RST     0X38            
7254: FF         RST     0X38            
7255: FF         RST     0X38            
7256: FF         RST     0X38            
7257: FF         RST     0X38            
7258: FF         RST     0X38            
7259: FF         RST     0X38            
725A: FF         RST     0X38            
725B: FF         RST     0X38            
725C: FF         RST     0X38            
725D: FF         RST     0X38            
725E: FF         RST     0X38            
725F: FF         RST     0X38            
7260: FF         RST     0X38            
7261: FF         RST     0X38            
7262: FF         RST     0X38            
7263: FF         RST     0X38            
7264: FF         RST     0X38            
7265: FF         RST     0X38            
7266: FF         RST     0X38            
7267: FF         RST     0X38            
7268: FF         RST     0X38            
7269: FF         RST     0X38            
726A: FF         RST     0X38            
726B: FF         RST     0X38            
726C: FF         RST     0X38            
726D: FF         RST     0X38            
726E: FF         RST     0X38            
726F: FF         RST     0X38            
7270: FF         RST     0X38            
7271: FF         RST     0X38            
7272: FF         RST     0X38            
7273: FF         RST     0X38            
7274: FF         RST     0X38            
7275: FF         RST     0X38            
7276: FF         RST     0X38            
7277: FF         RST     0X38            
7278: FF         RST     0X38            
7279: FF         RST     0X38            
727A: FF         RST     0X38            
727B: FF         RST     0X38            
727C: FF         RST     0X38            
727D: FF         RST     0X38            
727E: FF         RST     0X38            
727F: FF         RST     0X38            
7280: FF         RST     0X38            
7281: FF         RST     0X38            
7282: FF         RST     0X38            
7283: FF         RST     0X38            
7284: FF         RST     0X38            
7285: FF         RST     0X38            
7286: FF         RST     0X38            
7287: FF         RST     0X38            
7288: FF         RST     0X38            
7289: FF         RST     0X38            
728A: FF         RST     0X38            
728B: FF         RST     0X38            
728C: FF         RST     0X38            
728D: FF         RST     0X38            
728E: FF         RST     0X38            
728F: FF         RST     0X38            
7290: FF         RST     0X38            
7291: FF         RST     0X38            
7292: FF         RST     0X38            
7293: FF         RST     0X38            
7294: FF         RST     0X38            
7295: FF         RST     0X38            
7296: FF         RST     0X38            
7297: FF         RST     0X38            
7298: FF         RST     0X38            
7299: FF         RST     0X38            
729A: FF         RST     0X38            
729B: FF         RST     0X38            
729C: FF         RST     0X38            
729D: FF         RST     0X38            
729E: FF         RST     0X38            
729F: FF         RST     0X38            
72A0: FF         RST     0X38            
72A1: FF         RST     0X38            
72A2: FF         RST     0X38            
72A3: FF         RST     0X38            
72A4: FF         RST     0X38            
72A5: FF         RST     0X38            
72A6: FF         RST     0X38            
72A7: FF         RST     0X38            
72A8: FF         RST     0X38            
72A9: FF         RST     0X38            
72AA: FF         RST     0X38            
72AB: FF         RST     0X38            
72AC: FF         RST     0X38            
72AD: FF         RST     0X38            
72AE: FF         RST     0X38            
72AF: FF         RST     0X38            
72B0: FF         RST     0X38            
72B1: FF         RST     0X38            
72B2: FF         RST     0X38            
72B3: FF         RST     0X38            
72B4: FF         RST     0X38            
72B5: FF         RST     0X38            
72B6: FF         RST     0X38            
72B7: FF         RST     0X38            
72B8: FF         RST     0X38            
72B9: FF         RST     0X38            
72BA: FF         RST     0X38            
72BB: FF         RST     0X38            
72BC: FF         RST     0X38            
72BD: FF         RST     0X38            
72BE: FF         RST     0X38            
72BF: FF         RST     0X38            
72C0: FF         RST     0X38            
72C1: FF         RST     0X38            
72C2: FF         RST     0X38            
72C3: FF         RST     0X38            
72C4: FF         RST     0X38            
72C5: FF         RST     0X38            
72C6: FF         RST     0X38            
72C7: FF         RST     0X38            
72C8: FF         RST     0X38            
72C9: FF         RST     0X38            
72CA: FF         RST     0X38            
72CB: FF         RST     0X38            
72CC: FF         RST     0X38            
72CD: FF         RST     0X38            
72CE: FF         RST     0X38            
72CF: FF         RST     0X38            
72D0: FF         RST     0X38            
72D1: FF         RST     0X38            
72D2: FF         RST     0X38            
72D3: FF         RST     0X38            
72D4: FF         RST     0X38            
72D5: FF         RST     0X38            
72D6: FF         RST     0X38            
72D7: FF         RST     0X38            
72D8: FF         RST     0X38            
72D9: FF         RST     0X38            
72DA: FF         RST     0X38            
72DB: FF         RST     0X38            
72DC: FF         RST     0X38            
72DD: FF         RST     0X38            
72DE: FF         RST     0X38            
72DF: FF         RST     0X38            
72E0: FF         RST     0X38            
72E1: FF         RST     0X38            
72E2: FF         RST     0X38            
72E3: FF         RST     0X38            
72E4: FF         RST     0X38            
72E5: FF         RST     0X38            
72E6: FF         RST     0X38            
72E7: FF         RST     0X38            
72E8: FF         RST     0X38            
72E9: FF         RST     0X38            
72EA: FF         RST     0X38            
72EB: FF         RST     0X38            
72EC: FF         RST     0X38            
72ED: FF         RST     0X38            
72EE: FF         RST     0X38            
72EF: FF         RST     0X38            
72F0: FF         RST     0X38            
72F1: FF         RST     0X38            
72F2: FF         RST     0X38            
72F3: FF         RST     0X38            
72F4: FF         RST     0X38            
72F5: FF         RST     0X38            
72F6: FF         RST     0X38            
72F7: FF         RST     0X38            
72F8: FF         RST     0X38            
72F9: FF         RST     0X38            
72FA: FF         RST     0X38            
72FB: FF         RST     0X38            
72FC: FF         RST     0X38            
72FD: FF         RST     0X38            
72FE: FF         RST     0X38            
72FF: FF         RST     0X38            
7300: FF         RST     0X38            
7301: FF         RST     0X38            
7302: FF         RST     0X38            
7303: FF         RST     0X38            
7304: FF         RST     0X38            
7305: FF         RST     0X38            
7306: FF         RST     0X38            
7307: FF         RST     0X38            
7308: FF         RST     0X38            
7309: FF         RST     0X38            
730A: FF         RST     0X38            
730B: FF         RST     0X38            
730C: FF         RST     0X38            
730D: FF         RST     0X38            
730E: FF         RST     0X38            
730F: FF         RST     0X38            
7310: FF         RST     0X38            
7311: FF         RST     0X38            
7312: FF         RST     0X38            
7313: FF         RST     0X38            
7314: FF         RST     0X38            
7315: FF         RST     0X38            
7316: FF         RST     0X38            
7317: FF         RST     0X38            
7318: FF         RST     0X38            
7319: FF         RST     0X38            
731A: FF         RST     0X38            
731B: FF         RST     0X38            
731C: FF         RST     0X38            
731D: FF         RST     0X38            
731E: FF         RST     0X38            
731F: FF         RST     0X38            
7320: FF         RST     0X38            
7321: FF         RST     0X38            
7322: FF         RST     0X38            
7323: FF         RST     0X38            
7324: FF         RST     0X38            
7325: FF         RST     0X38            
7326: FF         RST     0X38            
7327: FF         RST     0X38            
7328: FF         RST     0X38            
7329: FF         RST     0X38            
732A: FF         RST     0X38            
732B: FF         RST     0X38            
732C: FF         RST     0X38            
732D: FF         RST     0X38            
732E: FF         RST     0X38            
732F: FF         RST     0X38            
7330: FF         RST     0X38            
7331: FF         RST     0X38            
7332: FF         RST     0X38            
7333: FF         RST     0X38            
7334: FF         RST     0X38            
7335: FF         RST     0X38            
7336: FF         RST     0X38            
7337: FF         RST     0X38            
7338: FF         RST     0X38            
7339: FF         RST     0X38            
733A: FF         RST     0X38            
733B: FF         RST     0X38            
733C: FF         RST     0X38            
733D: FF         RST     0X38            
733E: FF         RST     0X38            
733F: FF         RST     0X38            
7340: FF         RST     0X38            
7341: FF         RST     0X38            
7342: FF         RST     0X38            
7343: FF         RST     0X38            
7344: FF         RST     0X38            
7345: FF         RST     0X38            
7346: FF         RST     0X38            
7347: FF         RST     0X38            
7348: FF         RST     0X38            
7349: FF         RST     0X38            
734A: FF         RST     0X38            
734B: FF         RST     0X38            
734C: FF         RST     0X38            
734D: FF         RST     0X38            
734E: FF         RST     0X38            
734F: FF         RST     0X38            
7350: FF         RST     0X38            
7351: FF         RST     0X38            
7352: FF         RST     0X38            
7353: FF         RST     0X38            
7354: FF         RST     0X38            
7355: FF         RST     0X38            
7356: FF         RST     0X38            
7357: FF         RST     0X38            
7358: FF         RST     0X38            
7359: FF         RST     0X38            
735A: FF         RST     0X38            
735B: FF         RST     0X38            
735C: FF         RST     0X38            
735D: FF         RST     0X38            
735E: FF         RST     0X38            
735F: FF         RST     0X38            
7360: FF         RST     0X38            
7361: FF         RST     0X38            
7362: FF         RST     0X38            
7363: FF         RST     0X38            
7364: FF         RST     0X38            
7365: FF         RST     0X38            
7366: FF         RST     0X38            
7367: FF         RST     0X38            
7368: FF         RST     0X38            
7369: FF         RST     0X38            
736A: FF         RST     0X38            
736B: FF         RST     0X38            
736C: FF         RST     0X38            
736D: FF         RST     0X38            
736E: FF         RST     0X38            
736F: FF         RST     0X38            
7370: FF         RST     0X38            
7371: FF         RST     0X38            
7372: FF         RST     0X38            
7373: FF         RST     0X38            
7374: FF         RST     0X38            
7375: FF         RST     0X38            
7376: FF         RST     0X38            
7377: FF         RST     0X38            
7378: FF         RST     0X38            
7379: FF         RST     0X38            
737A: FF         RST     0X38            
737B: FF         RST     0X38            
737C: FF         RST     0X38            
737D: FF         RST     0X38            
737E: FF         RST     0X38            
737F: FF         RST     0X38            
7380: FF         RST     0X38            
7381: FF         RST     0X38            
7382: FF         RST     0X38            
7383: FF         RST     0X38            
7384: FF         RST     0X38            
7385: FF         RST     0X38            
7386: FF         RST     0X38            
7387: FF         RST     0X38            
7388: FF         RST     0X38            
7389: FF         RST     0X38            
738A: FF         RST     0X38            
738B: FF         RST     0X38            
738C: FF         RST     0X38            
738D: FF         RST     0X38            
738E: FF         RST     0X38            
738F: FF         RST     0X38            
7390: FF         RST     0X38            
7391: FF         RST     0X38            
7392: FF         RST     0X38            
7393: FF         RST     0X38            
7394: FF         RST     0X38            
7395: FF         RST     0X38            
7396: FF         RST     0X38            
7397: FF         RST     0X38            
7398: FF         RST     0X38            
7399: FF         RST     0X38            
739A: FF         RST     0X38            
739B: FF         RST     0X38            
739C: FF         RST     0X38            
739D: FF         RST     0X38            
739E: FF         RST     0X38            
739F: FF         RST     0X38            
73A0: FF         RST     0X38            
73A1: FF         RST     0X38            
73A2: FF         RST     0X38            
73A3: FF         RST     0X38            
73A4: FF         RST     0X38            
73A5: FF         RST     0X38            
73A6: FF         RST     0X38            
73A7: FF         RST     0X38            
73A8: FF         RST     0X38            
73A9: FF         RST     0X38            
73AA: FF         RST     0X38            
73AB: FF         RST     0X38            
73AC: FF         RST     0X38            
73AD: FF         RST     0X38            
73AE: FF         RST     0X38            
73AF: FF         RST     0X38            
73B0: FF         RST     0X38            
73B1: FF         RST     0X38            
73B2: FF         RST     0X38            
73B3: FF         RST     0X38            
73B4: FF         RST     0X38            
73B5: FF         RST     0X38            
73B6: FF         RST     0X38            
73B7: FF         RST     0X38            
73B8: FF         RST     0X38            
73B9: FF         RST     0X38            
73BA: FF         RST     0X38            
73BB: FF         RST     0X38            
73BC: FF         RST     0X38            
73BD: FF         RST     0X38            
73BE: FF         RST     0X38            
73BF: FF         RST     0X38            
73C0: FF         RST     0X38            
73C1: FF         RST     0X38            
73C2: FF         RST     0X38            
73C3: FF         RST     0X38            
73C4: FF         RST     0X38            
73C5: FF         RST     0X38            
73C6: FF         RST     0X38            
73C7: FF         RST     0X38            
73C8: FF         RST     0X38            
73C9: FF         RST     0X38            
73CA: FF         RST     0X38            
73CB: FF         RST     0X38            
73CC: FF         RST     0X38            
73CD: FF         RST     0X38            
73CE: FF         RST     0X38            
73CF: FF         RST     0X38            
73D0: FF         RST     0X38            
73D1: FF         RST     0X38            
73D2: FF         RST     0X38            
73D3: FF         RST     0X38            
73D4: FF         RST     0X38            
73D5: FF         RST     0X38            
73D6: FF         RST     0X38            
73D7: FF         RST     0X38            
73D8: FF         RST     0X38            
73D9: FF         RST     0X38            
73DA: FF         RST     0X38            
73DB: FF         RST     0X38            
73DC: FF         RST     0X38            
73DD: FF         RST     0X38            
73DE: FF         RST     0X38            
73DF: FF         RST     0X38            
73E0: FF         RST     0X38            
73E1: FF         RST     0X38            
73E2: FF         RST     0X38            
73E3: FF         RST     0X38            
73E4: FF         RST     0X38            
73E5: FF         RST     0X38            
73E6: FF         RST     0X38            
73E7: FF         RST     0X38            
73E8: FF         RST     0X38            
73E9: FF         RST     0X38            
73EA: FF         RST     0X38            
73EB: FF         RST     0X38            
73EC: FF         RST     0X38            
73ED: FF         RST     0X38            
73EE: FF         RST     0X38            
73EF: FF         RST     0X38            
73F0: FF         RST     0X38            
73F1: FF         RST     0X38            
73F2: FF         RST     0X38            
73F3: FF         RST     0X38            
73F4: FF         RST     0X38            
73F5: FF         RST     0X38            
73F6: FF         RST     0X38            
73F7: FF         RST     0X38            
73F8: FF         RST     0X38            
73F9: FF         RST     0X38            
73FA: FF         RST     0X38            
73FB: FF         RST     0X38            
73FC: FF         RST     0X38            
73FD: FF         RST     0X38            
73FE: FF         RST     0X38            
73FF: FF         RST     0X38            
7400: FF         RST     0X38            
7401: FF         RST     0X38            
7402: FF         RST     0X38            
7403: FF         RST     0X38            
7404: FF         RST     0X38            
7405: FF         RST     0X38            
7406: FF         RST     0X38            
7407: FF         RST     0X38            
7408: FF         RST     0X38            
7409: FF         RST     0X38            
740A: FF         RST     0X38            
740B: FF         RST     0X38            
740C: FF         RST     0X38            
740D: FF         RST     0X38            
740E: FF         RST     0X38            
740F: FF         RST     0X38            
7410: FF         RST     0X38            
7411: FF         RST     0X38            
7412: FF         RST     0X38            
7413: FF         RST     0X38            
7414: FF         RST     0X38            
7415: FF         RST     0X38            
7416: FF         RST     0X38            
7417: FF         RST     0X38            
7418: FF         RST     0X38            
7419: FF         RST     0X38            
741A: FF         RST     0X38            
741B: FF         RST     0X38            
741C: FF         RST     0X38            
741D: FF         RST     0X38            
741E: FF         RST     0X38            
741F: FF         RST     0X38            
7420: FF         RST     0X38            
7421: FF         RST     0X38            
7422: FF         RST     0X38            
7423: FF         RST     0X38            
7424: FF         RST     0X38            
7425: FF         RST     0X38            
7426: FF         RST     0X38            
7427: FF         RST     0X38            
7428: FF         RST     0X38            
7429: FF         RST     0X38            
742A: FF         RST     0X38            
742B: FF         RST     0X38            
742C: FF         RST     0X38            
742D: FF         RST     0X38            
742E: FF         RST     0X38            
742F: FF         RST     0X38            
7430: FF         RST     0X38            
7431: FF         RST     0X38            
7432: FF         RST     0X38            
7433: FF         RST     0X38            
7434: FF         RST     0X38            
7435: FF         RST     0X38            
7436: FF         RST     0X38            
7437: FF         RST     0X38            
7438: FF         RST     0X38            
7439: FF         RST     0X38            
743A: FF         RST     0X38            
743B: FF         RST     0X38            
743C: FF         RST     0X38            
743D: FF         RST     0X38            
743E: FF         RST     0X38            
743F: FF         RST     0X38            
7440: FF         RST     0X38            
7441: FF         RST     0X38            
7442: FF         RST     0X38            
7443: FF         RST     0X38            
7444: FF         RST     0X38            
7445: FF         RST     0X38            
7446: FF         RST     0X38            
7447: FF         RST     0X38            
7448: FF         RST     0X38            
7449: FF         RST     0X38            
744A: FF         RST     0X38            
744B: FF         RST     0X38            
744C: FF         RST     0X38            
744D: FF         RST     0X38            
744E: FF         RST     0X38            
744F: FF         RST     0X38            
7450: FF         RST     0X38            
7451: FF         RST     0X38            
7452: FF         RST     0X38            
7453: FF         RST     0X38            
7454: FF         RST     0X38            
7455: FF         RST     0X38            
7456: FF         RST     0X38            
7457: FF         RST     0X38            
7458: FF         RST     0X38            
7459: FF         RST     0X38            
745A: FF         RST     0X38            
745B: FF         RST     0X38            
745C: FF         RST     0X38            
745D: FF         RST     0X38            
745E: FF         RST     0X38            
745F: FF         RST     0X38            
7460: FF         RST     0X38            
7461: FF         RST     0X38            
7462: FF         RST     0X38            
7463: FF         RST     0X38            
7464: FF         RST     0X38            
7465: FF         RST     0X38            
7466: FF         RST     0X38            
7467: FF         RST     0X38            
7468: FF         RST     0X38            
7469: FF         RST     0X38            
746A: FF         RST     0X38            
746B: FF         RST     0X38            
746C: FF         RST     0X38            
746D: FF         RST     0X38            
746E: FF         RST     0X38            
746F: FF         RST     0X38            
7470: FF         RST     0X38            
7471: FF         RST     0X38            
7472: FF         RST     0X38            
7473: FF         RST     0X38            
7474: FF         RST     0X38            
7475: FF         RST     0X38            
7476: FF         RST     0X38            
7477: FF         RST     0X38            
7478: FF         RST     0X38            
7479: FF         RST     0X38            
747A: FF         RST     0X38            
747B: FF         RST     0X38            
747C: FF         RST     0X38            
747D: FF         RST     0X38            
747E: FF         RST     0X38            
747F: FF         RST     0X38            
7480: FF         RST     0X38            
7481: FF         RST     0X38            
7482: FF         RST     0X38            
7483: FF         RST     0X38            
7484: FF         RST     0X38            
7485: FF         RST     0X38            
7486: FF         RST     0X38            
7487: FF         RST     0X38            
7488: FF         RST     0X38            
7489: FF         RST     0X38            
748A: FF         RST     0X38            
748B: FF         RST     0X38            
748C: FF         RST     0X38            
748D: FF         RST     0X38            
748E: FF         RST     0X38            
748F: FF         RST     0X38            
7490: FF         RST     0X38            
7491: FF         RST     0X38            
7492: FF         RST     0X38            
7493: FF         RST     0X38            
7494: FF         RST     0X38            
7495: FF         RST     0X38            
7496: FF         RST     0X38            
7497: FF         RST     0X38            
7498: FF         RST     0X38            
7499: FF         RST     0X38            
749A: FF         RST     0X38            
749B: FF         RST     0X38            
749C: FF         RST     0X38            
749D: FF         RST     0X38            
749E: FF         RST     0X38            
749F: FF         RST     0X38            
74A0: FF         RST     0X38            
74A1: FF         RST     0X38            
74A2: FF         RST     0X38            
74A3: FF         RST     0X38            
74A4: FF         RST     0X38            
74A5: FF         RST     0X38            
74A6: FF         RST     0X38            
74A7: FF         RST     0X38            
74A8: FF         RST     0X38            
74A9: FF         RST     0X38            
74AA: FF         RST     0X38            
74AB: FF         RST     0X38            
74AC: FF         RST     0X38            
74AD: FF         RST     0X38            
74AE: FF         RST     0X38            
74AF: FF         RST     0X38            
74B0: FF         RST     0X38            
74B1: FF         RST     0X38            
74B2: FF         RST     0X38            
74B3: FF         RST     0X38            
74B4: FF         RST     0X38            
74B5: FF         RST     0X38            
74B6: FF         RST     0X38            
74B7: FF         RST     0X38            
74B8: FF         RST     0X38            
74B9: FF         RST     0X38            
74BA: FF         RST     0X38            
74BB: FF         RST     0X38            
74BC: FF         RST     0X38            
74BD: FF         RST     0X38            
74BE: FF         RST     0X38            
74BF: FF         RST     0X38            
74C0: FF         RST     0X38            
74C1: FF         RST     0X38            
74C2: FF         RST     0X38            
74C3: FF         RST     0X38            
74C4: FF         RST     0X38            
74C5: FF         RST     0X38            
74C6: FF         RST     0X38            
74C7: FF         RST     0X38            
74C8: FF         RST     0X38            
74C9: FF         RST     0X38            
74CA: FF         RST     0X38            
74CB: FF         RST     0X38            
74CC: FF         RST     0X38            
74CD: FF         RST     0X38            
74CE: FF         RST     0X38            
74CF: FF         RST     0X38            
74D0: FF         RST     0X38            
74D1: FF         RST     0X38            
74D2: FF         RST     0X38            
74D3: FF         RST     0X38            
74D4: FF         RST     0X38            
74D5: FF         RST     0X38            
74D6: FF         RST     0X38            
74D7: FF         RST     0X38            
74D8: FF         RST     0X38            
74D9: FF         RST     0X38            
74DA: FF         RST     0X38            
74DB: FF         RST     0X38            
74DC: FF         RST     0X38            
74DD: FF         RST     0X38            
74DE: FF         RST     0X38            
74DF: FF         RST     0X38            
74E0: FF         RST     0X38            
74E1: FF         RST     0X38            
74E2: FF         RST     0X38            
74E3: FF         RST     0X38            
74E4: FF         RST     0X38            
74E5: FF         RST     0X38            
74E6: FF         RST     0X38            
74E7: FF         RST     0X38            
74E8: FF         RST     0X38            
74E9: FF         RST     0X38            
74EA: FF         RST     0X38            
74EB: FF         RST     0X38            
74EC: FF         RST     0X38            
74ED: FF         RST     0X38            
74EE: FF         RST     0X38            
74EF: FF         RST     0X38            
74F0: FF         RST     0X38            
74F1: FF         RST     0X38            
74F2: FF         RST     0X38            
74F3: FF         RST     0X38            
74F4: FF         RST     0X38            
74F5: FF         RST     0X38            
74F6: FF         RST     0X38            
74F7: FF         RST     0X38            
74F8: FF         RST     0X38            
74F9: FF         RST     0X38            
74FA: FF         RST     0X38            
74FB: FF         RST     0X38            
74FC: FF         RST     0X38            
74FD: FF         RST     0X38            
74FE: FF         RST     0X38            
74FF: FF         RST     0X38            
7500: FF         RST     0X38            
7501: FF         RST     0X38            
7502: FF         RST     0X38            
7503: FF         RST     0X38            
7504: FF         RST     0X38            
7505: FF         RST     0X38            
7506: FF         RST     0X38            
7507: FF         RST     0X38            
7508: FF         RST     0X38            
7509: FF         RST     0X38            
750A: FF         RST     0X38            
750B: FF         RST     0X38            
750C: FF         RST     0X38            
750D: FF         RST     0X38            
750E: FF         RST     0X38            
750F: FF         RST     0X38            
7510: FF         RST     0X38            
7511: FF         RST     0X38            
7512: FF         RST     0X38            
7513: FF         RST     0X38            
7514: FF         RST     0X38            
7515: FF         RST     0X38            
7516: FF         RST     0X38            
7517: FF         RST     0X38            
7518: FF         RST     0X38            
7519: FF         RST     0X38            
751A: FF         RST     0X38            
751B: FF         RST     0X38            
751C: FF         RST     0X38            
751D: FF         RST     0X38            
751E: FF         RST     0X38            
751F: FF         RST     0X38            
7520: FF         RST     0X38            
7521: FF         RST     0X38            
7522: FF         RST     0X38            
7523: FF         RST     0X38            
7524: FF         RST     0X38            
7525: FF         RST     0X38            
7526: FF         RST     0X38            
7527: FF         RST     0X38            
7528: FF         RST     0X38            
7529: FF         RST     0X38            
752A: FF         RST     0X38            
752B: FF         RST     0X38            
752C: FF         RST     0X38            
752D: FF         RST     0X38            
752E: FF         RST     0X38            
752F: FF         RST     0X38            
7530: FF         RST     0X38            
7531: FF         RST     0X38            
7532: FF         RST     0X38            
7533: FF         RST     0X38            
7534: FF         RST     0X38            
7535: FF         RST     0X38            
7536: FF         RST     0X38            
7537: FF         RST     0X38            
7538: FF         RST     0X38            
7539: FF         RST     0X38            
753A: FF         RST     0X38            
753B: FF         RST     0X38            
753C: FF         RST     0X38            
753D: FF         RST     0X38            
753E: FF         RST     0X38            
753F: FF         RST     0X38            
7540: FF         RST     0X38            
7541: FF         RST     0X38            
7542: FF         RST     0X38            
7543: FF         RST     0X38            
7544: FF         RST     0X38            
7545: FF         RST     0X38            
7546: FF         RST     0X38            
7547: FF         RST     0X38            
7548: FF         RST     0X38            
7549: FF         RST     0X38            
754A: FF         RST     0X38            
754B: FF         RST     0X38            
754C: FF         RST     0X38            
754D: FF         RST     0X38            
754E: FF         RST     0X38            
754F: FF         RST     0X38            
7550: FF         RST     0X38            
7551: FF         RST     0X38            
7552: FF         RST     0X38            
7553: FF         RST     0X38            
7554: FF         RST     0X38            
7555: FF         RST     0X38            
7556: FF         RST     0X38            
7557: FF         RST     0X38            
7558: FF         RST     0X38            
7559: FF         RST     0X38            
755A: FF         RST     0X38            
755B: FF         RST     0X38            
755C: FF         RST     0X38            
755D: FF         RST     0X38            
755E: FF         RST     0X38            
755F: FF         RST     0X38            
7560: FF         RST     0X38            
7561: FF         RST     0X38            
7562: FF         RST     0X38            
7563: FF         RST     0X38            
7564: FF         RST     0X38            
7565: FF         RST     0X38            
7566: FF         RST     0X38            
7567: FF         RST     0X38            
7568: FF         RST     0X38            
7569: FF         RST     0X38            
756A: FF         RST     0X38            
756B: FF         RST     0X38            
756C: FF         RST     0X38            
756D: FF         RST     0X38            
756E: FF         RST     0X38            
756F: FF         RST     0X38            
7570: FF         RST     0X38            
7571: FF         RST     0X38            
7572: FF         RST     0X38            
7573: FF         RST     0X38            
7574: FF         RST     0X38            
7575: FF         RST     0X38            
7576: FF         RST     0X38            
7577: FF         RST     0X38            
7578: FF         RST     0X38            
7579: FF         RST     0X38            
757A: FF         RST     0X38            
757B: FF         RST     0X38            
757C: FF         RST     0X38            
757D: FF         RST     0X38            
757E: FF         RST     0X38            
757F: FF         RST     0X38            
7580: FF         RST     0X38            
7581: FF         RST     0X38            
7582: FF         RST     0X38            
7583: FF         RST     0X38            
7584: FF         RST     0X38            
7585: FF         RST     0X38            
7586: FF         RST     0X38            
7587: FF         RST     0X38            
7588: FF         RST     0X38            
7589: FF         RST     0X38            
758A: FF         RST     0X38            
758B: FF         RST     0X38            
758C: FF         RST     0X38            
758D: FF         RST     0X38            
758E: FF         RST     0X38            
758F: FF         RST     0X38            
7590: FF         RST     0X38            
7591: FF         RST     0X38            
7592: FF         RST     0X38            
7593: FF         RST     0X38            
7594: FF         RST     0X38            
7595: FF         RST     0X38            
7596: FF         RST     0X38            
7597: FF         RST     0X38            
7598: FF         RST     0X38            
7599: FF         RST     0X38            
759A: FF         RST     0X38            
759B: FF         RST     0X38            
759C: FF         RST     0X38            
759D: FF         RST     0X38            
759E: FF         RST     0X38            
759F: FF         RST     0X38            
75A0: FF         RST     0X38            
75A1: FF         RST     0X38            
75A2: FF         RST     0X38            
75A3: FF         RST     0X38            
75A4: FF         RST     0X38            
75A5: FF         RST     0X38            
75A6: FF         RST     0X38            
75A7: FF         RST     0X38            
75A8: FF         RST     0X38            
75A9: FF         RST     0X38            
75AA: FF         RST     0X38            
75AB: FF         RST     0X38            
75AC: FF         RST     0X38            
75AD: FF         RST     0X38            
75AE: FF         RST     0X38            
75AF: FF         RST     0X38            
75B0: FF         RST     0X38            
75B1: FF         RST     0X38            
75B2: FF         RST     0X38            
75B3: FF         RST     0X38            
75B4: FF         RST     0X38            
75B5: FF         RST     0X38            
75B6: FF         RST     0X38            
75B7: FF         RST     0X38            
75B8: FF         RST     0X38            
75B9: FF         RST     0X38            
75BA: FF         RST     0X38            
75BB: FF         RST     0X38            
75BC: FF         RST     0X38            
75BD: FF         RST     0X38            
75BE: FF         RST     0X38            
75BF: FF         RST     0X38            
75C0: FF         RST     0X38            
75C1: FF         RST     0X38            
75C2: FF         RST     0X38            
75C3: FF         RST     0X38            
75C4: FF         RST     0X38            
75C5: FF         RST     0X38            
75C6: FF         RST     0X38            
75C7: FF         RST     0X38            
75C8: FF         RST     0X38            
75C9: FF         RST     0X38            
75CA: FF         RST     0X38            
75CB: FF         RST     0X38            
75CC: FF         RST     0X38            
75CD: FF         RST     0X38            
75CE: FF         RST     0X38            
75CF: FF         RST     0X38            
75D0: FF         RST     0X38            
75D1: FF         RST     0X38            
75D2: FF         RST     0X38            
75D3: FF         RST     0X38            
75D4: FF         RST     0X38            
75D5: FF         RST     0X38            
75D6: FF         RST     0X38            
75D7: FF         RST     0X38            
75D8: FF         RST     0X38            
75D9: FF         RST     0X38            
75DA: FF         RST     0X38            
75DB: FF         RST     0X38            
75DC: FF         RST     0X38            
75DD: FF         RST     0X38            
75DE: FF         RST     0X38            
75DF: FF         RST     0X38            
75E0: FF         RST     0X38            
75E1: FF         RST     0X38            
75E2: FF         RST     0X38            
75E3: FF         RST     0X38            
75E4: FF         RST     0X38            
75E5: FF         RST     0X38            
75E6: FF         RST     0X38            
75E7: FF         RST     0X38            
75E8: FF         RST     0X38            
75E9: FF         RST     0X38            
75EA: FF         RST     0X38            
75EB: FF         RST     0X38            
75EC: FF         RST     0X38            
75ED: FF         RST     0X38            
75EE: FF         RST     0X38            
75EF: FF         RST     0X38            
75F0: FF         RST     0X38            
75F1: FF         RST     0X38            
75F2: FF         RST     0X38            
75F3: FF         RST     0X38            
75F4: FF         RST     0X38            
75F5: FF         RST     0X38            
75F6: FF         RST     0X38            
75F7: FF         RST     0X38            
75F8: FF         RST     0X38            
75F9: FF         RST     0X38            
75FA: FF         RST     0X38            
75FB: FF         RST     0X38            
75FC: FF         RST     0X38            
75FD: FF         RST     0X38            
75FE: FF         RST     0X38            
75FF: FF         RST     0X38            
7600: FF         RST     0X38            
7601: FF         RST     0X38            
7602: FF         RST     0X38            
7603: FF         RST     0X38            
7604: FF         RST     0X38            
7605: FF         RST     0X38            
7606: FF         RST     0X38            
7607: FF         RST     0X38            
7608: FF         RST     0X38            
7609: FF         RST     0X38            
760A: FF         RST     0X38            
760B: FF         RST     0X38            
760C: FF         RST     0X38            
760D: FF         RST     0X38            
760E: FF         RST     0X38            
760F: FF         RST     0X38            
7610: FF         RST     0X38            
7611: FF         RST     0X38            
7612: FF         RST     0X38            
7613: FF         RST     0X38            
7614: FF         RST     0X38            
7615: FF         RST     0X38            
7616: FF         RST     0X38            
7617: FF         RST     0X38            
7618: FF         RST     0X38            
7619: FF         RST     0X38            
761A: FF         RST     0X38            
761B: FF         RST     0X38            
761C: FF         RST     0X38            
761D: FF         RST     0X38            
761E: FF         RST     0X38            
761F: FF         RST     0X38            
7620: FF         RST     0X38            
7621: FF         RST     0X38            
7622: FF         RST     0X38            
7623: FF         RST     0X38            
7624: FF         RST     0X38            
7625: FF         RST     0X38            
7626: FF         RST     0X38            
7627: FF         RST     0X38            
7628: FF         RST     0X38            
7629: FF         RST     0X38            
762A: FF         RST     0X38            
762B: FF         RST     0X38            
762C: FF         RST     0X38            
762D: FF         RST     0X38            
762E: FF         RST     0X38            
762F: FF         RST     0X38            
7630: FF         RST     0X38            
7631: FF         RST     0X38            
7632: FF         RST     0X38            
7633: FF         RST     0X38            
7634: FF         RST     0X38            
7635: FF         RST     0X38            
7636: FF         RST     0X38            
7637: FF         RST     0X38            
7638: FF         RST     0X38            
7639: FF         RST     0X38            
763A: FF         RST     0X38            
763B: FF         RST     0X38            
763C: FF         RST     0X38            
763D: FF         RST     0X38            
763E: FF         RST     0X38            
763F: FF         RST     0X38            
7640: FF         RST     0X38            
7641: FF         RST     0X38            
7642: FF         RST     0X38            
7643: FF         RST     0X38            
7644: FF         RST     0X38            
7645: FF         RST     0X38            
7646: FF         RST     0X38            
7647: FF         RST     0X38            
7648: FF         RST     0X38            
7649: FF         RST     0X38            
764A: FF         RST     0X38            
764B: FF         RST     0X38            
764C: FF         RST     0X38            
764D: FF         RST     0X38            
764E: FF         RST     0X38            
764F: FF         RST     0X38            
7650: FF         RST     0X38            
7651: FF         RST     0X38            
7652: FF         RST     0X38            
7653: FF         RST     0X38            
7654: FF         RST     0X38            
7655: FF         RST     0X38            
7656: FF         RST     0X38            
7657: FF         RST     0X38            
7658: FF         RST     0X38            
7659: FF         RST     0X38            
765A: FF         RST     0X38            
765B: FF         RST     0X38            
765C: FF         RST     0X38            
765D: FF         RST     0X38            
765E: FF         RST     0X38            
765F: FF         RST     0X38            
7660: FF         RST     0X38            
7661: FF         RST     0X38            
7662: FF         RST     0X38            
7663: FF         RST     0X38            
7664: FF         RST     0X38            
7665: FF         RST     0X38            
7666: FF         RST     0X38            
7667: FF         RST     0X38            
7668: FF         RST     0X38            
7669: FF         RST     0X38            
766A: FF         RST     0X38            
766B: FF         RST     0X38            
766C: FF         RST     0X38            
766D: FF         RST     0X38            
766E: FF         RST     0X38            
766F: FF         RST     0X38            
7670: FF         RST     0X38            
7671: FF         RST     0X38            
7672: FF         RST     0X38            
7673: FF         RST     0X38            
7674: FF         RST     0X38            
7675: FF         RST     0X38            
7676: FF         RST     0X38            
7677: FF         RST     0X38            
7678: FF         RST     0X38            
7679: FF         RST     0X38            
767A: FF         RST     0X38            
767B: FF         RST     0X38            
767C: FF         RST     0X38            
767D: FF         RST     0X38            
767E: FF         RST     0X38            
767F: FF         RST     0X38            
7680: FF         RST     0X38            
7681: FF         RST     0X38            
7682: FF         RST     0X38            
7683: FF         RST     0X38            
7684: FF         RST     0X38            
7685: FF         RST     0X38            
7686: FF         RST     0X38            
7687: FF         RST     0X38            
7688: FF         RST     0X38            
7689: FF         RST     0X38            
768A: FF         RST     0X38            
768B: FF         RST     0X38            
768C: FF         RST     0X38            
768D: FF         RST     0X38            
768E: FF         RST     0X38            
768F: FF         RST     0X38            
7690: FF         RST     0X38            
7691: FF         RST     0X38            
7692: FF         RST     0X38            
7693: FF         RST     0X38            
7694: FF         RST     0X38            
7695: FF         RST     0X38            
7696: FF         RST     0X38            
7697: FF         RST     0X38            
7698: FF         RST     0X38            
7699: FF         RST     0X38            
769A: FF         RST     0X38            
769B: FF         RST     0X38            
769C: FF         RST     0X38            
769D: FF         RST     0X38            
769E: FF         RST     0X38            
769F: FF         RST     0X38            
76A0: FF         RST     0X38            
76A1: FF         RST     0X38            
76A2: FF         RST     0X38            
76A3: FF         RST     0X38            
76A4: FF         RST     0X38            
76A5: FF         RST     0X38            
76A6: FF         RST     0X38            
76A7: FF         RST     0X38            
76A8: FF         RST     0X38            
76A9: FF         RST     0X38            
76AA: FF         RST     0X38            
76AB: FF         RST     0X38            
76AC: FF         RST     0X38            
76AD: FF         RST     0X38            
76AE: FF         RST     0X38            
76AF: FF         RST     0X38            
76B0: FF         RST     0X38            
76B1: FF         RST     0X38            
76B2: FF         RST     0X38            
76B3: FF         RST     0X38            
76B4: FF         RST     0X38            
76B5: FF         RST     0X38            
76B6: FF         RST     0X38            
76B7: FF         RST     0X38            
76B8: FF         RST     0X38            
76B9: FF         RST     0X38            
76BA: FF         RST     0X38            
76BB: FF         RST     0X38            
76BC: FF         RST     0X38            
76BD: FF         RST     0X38            
76BE: FF         RST     0X38            
76BF: FF         RST     0X38            
76C0: FF         RST     0X38            
76C1: FF         RST     0X38            
76C2: FF         RST     0X38            
76C3: FF         RST     0X38            
76C4: FF         RST     0X38            
76C5: FF         RST     0X38            
76C6: FF         RST     0X38            
76C7: FF         RST     0X38            
76C8: FF         RST     0X38            
76C9: FF         RST     0X38            
76CA: FF         RST     0X38            
76CB: FF         RST     0X38            
76CC: FF         RST     0X38            
76CD: FF         RST     0X38            
76CE: FF         RST     0X38            
76CF: FF         RST     0X38            
76D0: FF         RST     0X38            
76D1: FF         RST     0X38            
76D2: FF         RST     0X38            
76D3: FF         RST     0X38            
76D4: FF         RST     0X38            
76D5: FF         RST     0X38            
76D6: FF         RST     0X38            
76D7: FF         RST     0X38            
76D8: FF         RST     0X38            
76D9: FF         RST     0X38            
76DA: FF         RST     0X38            
76DB: FF         RST     0X38            
76DC: FF         RST     0X38            
76DD: FF         RST     0X38            
76DE: FF         RST     0X38            
76DF: FF         RST     0X38            
76E0: FF         RST     0X38            
76E1: FF         RST     0X38            
76E2: FF         RST     0X38            
76E3: FF         RST     0X38            
76E4: FF         RST     0X38            
76E5: FF         RST     0X38            
76E6: FF         RST     0X38            
76E7: FF         RST     0X38            
76E8: FF         RST     0X38            
76E9: FF         RST     0X38            
76EA: FF         RST     0X38            
76EB: FF         RST     0X38            
76EC: FF         RST     0X38            
76ED: FF         RST     0X38            
76EE: FF         RST     0X38            
76EF: FF         RST     0X38            
76F0: FF         RST     0X38            
76F1: FF         RST     0X38            
76F2: FF         RST     0X38            
76F3: FF         RST     0X38            
76F4: FF         RST     0X38            
76F5: FF         RST     0X38            
76F6: FF         RST     0X38            
76F7: FF         RST     0X38            
76F8: FF         RST     0X38            
76F9: FF         RST     0X38            
76FA: FF         RST     0X38            
76FB: FF         RST     0X38            
76FC: FF         RST     0X38            
76FD: FF         RST     0X38            
76FE: FF         RST     0X38            
76FF: FF         RST     0X38            
7700: FF         RST     0X38            
7701: FF         RST     0X38            
7702: FF         RST     0X38            
7703: FF         RST     0X38            
7704: FF         RST     0X38            
7705: FF         RST     0X38            
7706: FF         RST     0X38            
7707: FF         RST     0X38            
7708: FF         RST     0X38            
7709: FF         RST     0X38            
770A: FF         RST     0X38            
770B: FF         RST     0X38            
770C: FF         RST     0X38            
770D: FF         RST     0X38            
770E: FF         RST     0X38            
770F: FF         RST     0X38            
7710: FF         RST     0X38            
7711: FF         RST     0X38            
7712: FF         RST     0X38            
7713: FF         RST     0X38            
7714: FF         RST     0X38            
7715: FF         RST     0X38            
7716: FF         RST     0X38            
7717: FF         RST     0X38            
7718: FF         RST     0X38            
7719: FF         RST     0X38            
771A: FF         RST     0X38            
771B: FF         RST     0X38            
771C: FF         RST     0X38            
771D: FF         RST     0X38            
771E: FF         RST     0X38            
771F: FF         RST     0X38            
7720: FF         RST     0X38            
7721: FF         RST     0X38            
7722: FF         RST     0X38            
7723: FF         RST     0X38            
7724: FF         RST     0X38            
7725: FF         RST     0X38            
7726: FF         RST     0X38            
7727: FF         RST     0X38            
7728: FF         RST     0X38            
7729: FF         RST     0X38            
772A: FF         RST     0X38            
772B: FF         RST     0X38            
772C: FF         RST     0X38            
772D: FF         RST     0X38            
772E: FF         RST     0X38            
772F: FF         RST     0X38            
7730: FF         RST     0X38            
7731: FF         RST     0X38            
7732: FF         RST     0X38            
7733: FF         RST     0X38            
7734: FF         RST     0X38            
7735: FF         RST     0X38            
7736: FF         RST     0X38            
7737: FF         RST     0X38            
7738: FF         RST     0X38            
7739: FF         RST     0X38            
773A: FF         RST     0X38            
773B: FF         RST     0X38            
773C: FF         RST     0X38            
773D: FF         RST     0X38            
773E: FF         RST     0X38            
773F: FF         RST     0X38            
7740: FF         RST     0X38            
7741: FF         RST     0X38            
7742: FF         RST     0X38            
7743: FF         RST     0X38            
7744: FF         RST     0X38            
7745: FF         RST     0X38            
7746: FF         RST     0X38            
7747: FF         RST     0X38            
7748: FF         RST     0X38            
7749: FF         RST     0X38            
774A: FF         RST     0X38            
774B: FF         RST     0X38            
774C: FF         RST     0X38            
774D: FF         RST     0X38            
774E: FF         RST     0X38            
774F: FF         RST     0X38            
7750: FF         RST     0X38            
7751: FF         RST     0X38            
7752: FF         RST     0X38            
7753: FF         RST     0X38            
7754: FF         RST     0X38            
7755: FF         RST     0X38            
7756: FF         RST     0X38            
7757: FF         RST     0X38            
7758: FF         RST     0X38            
7759: FF         RST     0X38            
775A: FF         RST     0X38            
775B: FF         RST     0X38            
775C: FF         RST     0X38            
775D: FF         RST     0X38            
775E: FF         RST     0X38            
775F: FF         RST     0X38            
7760: FF         RST     0X38            
7761: FF         RST     0X38            
7762: FF         RST     0X38            
7763: FF         RST     0X38            
7764: FF         RST     0X38            
7765: FF         RST     0X38            
7766: FF         RST     0X38            
7767: FF         RST     0X38            
7768: FF         RST     0X38            
7769: FF         RST     0X38            
776A: FF         RST     0X38            
776B: FF         RST     0X38            
776C: FF         RST     0X38            
776D: FF         RST     0X38            
776E: FF         RST     0X38            
776F: FF         RST     0X38            
7770: FF         RST     0X38            
7771: FF         RST     0X38            
7772: FF         RST     0X38            
7773: FF         RST     0X38            
7774: FF         RST     0X38            
7775: FF         RST     0X38            
7776: FF         RST     0X38            
7777: FF         RST     0X38            
7778: FF         RST     0X38            
7779: FF         RST     0X38            
777A: FF         RST     0X38            
777B: FF         RST     0X38            
777C: FF         RST     0X38            
777D: FF         RST     0X38            
777E: FF         RST     0X38            
777F: FF         RST     0X38            
7780: FF         RST     0X38            
7781: FF         RST     0X38            
7782: FF         RST     0X38            
7783: FF         RST     0X38            
7784: FF         RST     0X38            
7785: FF         RST     0X38            
7786: FF         RST     0X38            
7787: FF         RST     0X38            
7788: FF         RST     0X38            
7789: FF         RST     0X38            
778A: FF         RST     0X38            
778B: FF         RST     0X38            
778C: FF         RST     0X38            
778D: FF         RST     0X38            
778E: FF         RST     0X38            
778F: FF         RST     0X38            
7790: FF         RST     0X38            
7791: FF         RST     0X38            
7792: FF         RST     0X38            
7793: FF         RST     0X38            
7794: FF         RST     0X38            
7795: FF         RST     0X38            
7796: FF         RST     0X38            
7797: FF         RST     0X38            
7798: FF         RST     0X38            
7799: FF         RST     0X38            
779A: FF         RST     0X38            
779B: FF         RST     0X38            
779C: FF         RST     0X38            
779D: FF         RST     0X38            
779E: FF         RST     0X38            
779F: FF         RST     0X38            
77A0: FF         RST     0X38            
77A1: FF         RST     0X38            
77A2: FF         RST     0X38            
77A3: FF         RST     0X38            
77A4: FF         RST     0X38            
77A5: FF         RST     0X38            
77A6: FF         RST     0X38            
77A7: FF         RST     0X38            
77A8: FF         RST     0X38            
77A9: FF         RST     0X38            
77AA: FF         RST     0X38            
77AB: FF         RST     0X38            
77AC: FF         RST     0X38            
77AD: FF         RST     0X38            
77AE: FF         RST     0X38            
77AF: FF         RST     0X38            
77B0: FF         RST     0X38            
77B1: FF         RST     0X38            
77B2: FF         RST     0X38            
77B3: FF         RST     0X38            
77B4: FF         RST     0X38            
77B5: FF         RST     0X38            
77B6: FF         RST     0X38            
77B7: FF         RST     0X38            
77B8: FF         RST     0X38            
77B9: FF         RST     0X38            
77BA: FF         RST     0X38            
77BB: FF         RST     0X38            
77BC: FF         RST     0X38            
77BD: FF         RST     0X38            
77BE: FF         RST     0X38            
77BF: FF         RST     0X38            
77C0: FF         RST     0X38            
77C1: FF         RST     0X38            
77C2: FF         RST     0X38            
77C3: FF         RST     0X38            
77C4: FF         RST     0X38            
77C5: FF         RST     0X38            
77C6: FF         RST     0X38            
77C7: FF         RST     0X38            
77C8: FF         RST     0X38            
77C9: FF         RST     0X38            
77CA: FF         RST     0X38            
77CB: FF         RST     0X38            
77CC: FF         RST     0X38            
77CD: FF         RST     0X38            
77CE: FF         RST     0X38            
77CF: FF         RST     0X38            
77D0: FF         RST     0X38            
77D1: FF         RST     0X38            
77D2: FF         RST     0X38            
77D3: FF         RST     0X38            
77D4: FF         RST     0X38            
77D5: FF         RST     0X38            
77D6: FF         RST     0X38            
77D7: FF         RST     0X38            
77D8: FF         RST     0X38            
77D9: FF         RST     0X38            
77DA: FF         RST     0X38            
77DB: FF         RST     0X38            
77DC: FF         RST     0X38            
77DD: FF         RST     0X38            
77DE: FF         RST     0X38            
77DF: FF         RST     0X38            
77E0: FF         RST     0X38            
77E1: FF         RST     0X38            
77E2: FF         RST     0X38            
77E3: FF         RST     0X38            
77E4: FF         RST     0X38            
77E5: FF         RST     0X38            
77E6: FF         RST     0X38            
77E7: FF         RST     0X38            
77E8: FF         RST     0X38            
77E9: FF         RST     0X38            
77EA: FF         RST     0X38            
77EB: FF         RST     0X38            
77EC: FF         RST     0X38            
77ED: FF         RST     0X38            
77EE: FF         RST     0X38            
77EF: FF         RST     0X38            
77F0: FF         RST     0X38            
77F1: FF         RST     0X38            
77F2: FF         RST     0X38            
77F3: FF         RST     0X38            
77F4: FF         RST     0X38            
77F5: FF         RST     0X38            
77F6: FF         RST     0X38            
77F7: FF         RST     0X38            
77F8: FF         RST     0X38            
77F9: FF         RST     0X38            
77FA: FF         RST     0X38            
77FB: FF         RST     0X38            
77FC: FF         RST     0X38            
77FD: FF         RST     0X38            
77FE: FF         RST     0X38            
77FF: FF         RST     0X38            
7800: FF         RST     0X38            
7801: FF         RST     0X38            
7802: FF         RST     0X38            
7803: FF         RST     0X38            
7804: FF         RST     0X38            
7805: FF         RST     0X38            
7806: FF         RST     0X38            
7807: FF         RST     0X38            
7808: FF         RST     0X38            
7809: FF         RST     0X38            
780A: FF         RST     0X38            
780B: FF         RST     0X38            
780C: FF         RST     0X38            
780D: FF         RST     0X38            
780E: FF         RST     0X38            
780F: FF         RST     0X38            
7810: FF         RST     0X38            
7811: FF         RST     0X38            
7812: FF         RST     0X38            
7813: FF         RST     0X38            
7814: FF         RST     0X38            
7815: FF         RST     0X38            
7816: FF         RST     0X38            
7817: FF         RST     0X38            
7818: FF         RST     0X38            
7819: FF         RST     0X38            
781A: FF         RST     0X38            
781B: FF         RST     0X38            
781C: FF         RST     0X38            
781D: FF         RST     0X38            
781E: FF         RST     0X38            
781F: FF         RST     0X38            
7820: FF         RST     0X38            
7821: FF         RST     0X38            
7822: FF         RST     0X38            
7823: FF         RST     0X38            
7824: FF         RST     0X38            
7825: FF         RST     0X38            
7826: FF         RST     0X38            
7827: FF         RST     0X38            
7828: FF         RST     0X38            
7829: FF         RST     0X38            
782A: FF         RST     0X38            
782B: FF         RST     0X38            
782C: FF         RST     0X38            
782D: FF         RST     0X38            
782E: FF         RST     0X38            
782F: FF         RST     0X38            
7830: FF         RST     0X38            
7831: FF         RST     0X38            
7832: FF         RST     0X38            
7833: FF         RST     0X38            
7834: FF         RST     0X38            
7835: FF         RST     0X38            
7836: FF         RST     0X38            
7837: FF         RST     0X38            
7838: FF         RST     0X38            
7839: FF         RST     0X38            
783A: FF         RST     0X38            
783B: FF         RST     0X38            
783C: FF         RST     0X38            
783D: FF         RST     0X38            
783E: FF         RST     0X38            
783F: FF         RST     0X38            
7840: FF         RST     0X38            
7841: FF         RST     0X38            
7842: FF         RST     0X38            
7843: FF         RST     0X38            
7844: FF         RST     0X38            
7845: FF         RST     0X38            
7846: FF         RST     0X38            
7847: FF         RST     0X38            
7848: FF         RST     0X38            
7849: FF         RST     0X38            
784A: FF         RST     0X38            
784B: FF         RST     0X38            
784C: FF         RST     0X38            
784D: FF         RST     0X38            
784E: FF         RST     0X38            
784F: FF         RST     0X38            
7850: FF         RST     0X38            
7851: FF         RST     0X38            
7852: FF         RST     0X38            
7853: FF         RST     0X38            
7854: FF         RST     0X38            
7855: FF         RST     0X38            
7856: FF         RST     0X38            
7857: FF         RST     0X38            
7858: FF         RST     0X38            
7859: FF         RST     0X38            
785A: FF         RST     0X38            
785B: FF         RST     0X38            
785C: FF         RST     0X38            
785D: FF         RST     0X38            
785E: FF         RST     0X38            
785F: FF         RST     0X38            
7860: FF         RST     0X38            
7861: FF         RST     0X38            
7862: FF         RST     0X38            
7863: FF         RST     0X38            
7864: FF         RST     0X38            
7865: FF         RST     0X38            
7866: FF         RST     0X38            
7867: FF         RST     0X38            
7868: FF         RST     0X38            
7869: FF         RST     0X38            
786A: FF         RST     0X38            
786B: FF         RST     0X38            
786C: FF         RST     0X38            
786D: FF         RST     0X38            
786E: FF         RST     0X38            
786F: FF         RST     0X38            
7870: FF         RST     0X38            
7871: FF         RST     0X38            
7872: FF         RST     0X38            
7873: FF         RST     0X38            
7874: FF         RST     0X38            
7875: FF         RST     0X38            
7876: FF         RST     0X38            
7877: FF         RST     0X38            
7878: FF         RST     0X38            
7879: FF         RST     0X38            
787A: FF         RST     0X38            
787B: FF         RST     0X38            
787C: FF         RST     0X38            
787D: FF         RST     0X38            
787E: FF         RST     0X38            
787F: FF         RST     0X38            
7880: FF         RST     0X38            
7881: FF         RST     0X38            
7882: FF         RST     0X38            
7883: FF         RST     0X38            
7884: FF         RST     0X38            
7885: FF         RST     0X38            
7886: FF         RST     0X38            
7887: FF         RST     0X38            
7888: FF         RST     0X38            
7889: FF         RST     0X38            
788A: FF         RST     0X38            
788B: FF         RST     0X38            
788C: FF         RST     0X38            
788D: FF         RST     0X38            
788E: FF         RST     0X38            
788F: FF         RST     0X38            
7890: FF         RST     0X38            
7891: FF         RST     0X38            
7892: FF         RST     0X38            
7893: FF         RST     0X38            
7894: FF         RST     0X38            
7895: FF         RST     0X38            
7896: FF         RST     0X38            
7897: FF         RST     0X38            
7898: FF         RST     0X38            
7899: FF         RST     0X38            
789A: FF         RST     0X38            
789B: FF         RST     0X38            
789C: FF         RST     0X38            
789D: FF         RST     0X38            
789E: FF         RST     0X38            
789F: FF         RST     0X38            
78A0: FF         RST     0X38            
78A1: FF         RST     0X38            
78A2: FF         RST     0X38            
78A3: FF         RST     0X38            
78A4: FF         RST     0X38            
78A5: FF         RST     0X38            
78A6: FF         RST     0X38            
78A7: FF         RST     0X38            
78A8: FF         RST     0X38            
78A9: FF         RST     0X38            
78AA: FF         RST     0X38            
78AB: FF         RST     0X38            
78AC: FF         RST     0X38            
78AD: FF         RST     0X38            
78AE: FF         RST     0X38            
78AF: FF         RST     0X38            
78B0: FF         RST     0X38            
78B1: FF         RST     0X38            
78B2: FF         RST     0X38            
78B3: FF         RST     0X38            
78B4: FF         RST     0X38            
78B5: FF         RST     0X38            
78B6: FF         RST     0X38            
78B7: FF         RST     0X38            
78B8: FF         RST     0X38            
78B9: FF         RST     0X38            
78BA: FF         RST     0X38            
78BB: FF         RST     0X38            
78BC: FF         RST     0X38            
78BD: FF         RST     0X38            
78BE: FF         RST     0X38            
78BF: FF         RST     0X38            
78C0: FF         RST     0X38            
78C1: FF         RST     0X38            
78C2: FF         RST     0X38            
78C3: FF         RST     0X38            
78C4: FF         RST     0X38            
78C5: FF         RST     0X38            
78C6: FF         RST     0X38            
78C7: FF         RST     0X38            
78C8: FF         RST     0X38            
78C9: FF         RST     0X38            
78CA: FF         RST     0X38            
78CB: FF         RST     0X38            
78CC: FF         RST     0X38            
78CD: FF         RST     0X38            
78CE: FF         RST     0X38            
78CF: FF         RST     0X38            
78D0: FF         RST     0X38            
78D1: FF         RST     0X38            
78D2: FF         RST     0X38            
78D3: FF         RST     0X38            
78D4: FF         RST     0X38            
78D5: FF         RST     0X38            
78D6: FF         RST     0X38            
78D7: FF         RST     0X38            
78D8: FF         RST     0X38            
78D9: FF         RST     0X38            
78DA: FF         RST     0X38            
78DB: FF         RST     0X38            
78DC: FF         RST     0X38            
78DD: FF         RST     0X38            
78DE: FF         RST     0X38            
78DF: FF         RST     0X38            
78E0: FF         RST     0X38            
78E1: FF         RST     0X38            
78E2: FF         RST     0X38            
78E3: FF         RST     0X38            
78E4: FF         RST     0X38            
78E5: FF         RST     0X38            
78E6: FF         RST     0X38            
78E7: FF         RST     0X38            
78E8: FF         RST     0X38            
78E9: FF         RST     0X38            
78EA: FF         RST     0X38            
78EB: FF         RST     0X38            
78EC: FF         RST     0X38            
78ED: FF         RST     0X38            
78EE: FF         RST     0X38            
78EF: FF         RST     0X38            
78F0: FF         RST     0X38            
78F1: FF         RST     0X38            
78F2: FF         RST     0X38            
78F3: FF         RST     0X38            
78F4: FF         RST     0X38            
78F5: FF         RST     0X38            
78F6: FF         RST     0X38            
78F7: FF         RST     0X38            
78F8: FF         RST     0X38            
78F9: FF         RST     0X38            
78FA: FF         RST     0X38            
78FB: FF         RST     0X38            
78FC: FF         RST     0X38            
78FD: FF         RST     0X38            
78FE: FF         RST     0X38            
78FF: FF         RST     0X38            
7900: FF         RST     0X38            
7901: FF         RST     0X38            
7902: FF         RST     0X38            
7903: FF         RST     0X38            
7904: FF         RST     0X38            
7905: FF         RST     0X38            
7906: FF         RST     0X38            
7907: FF         RST     0X38            
7908: FF         RST     0X38            
7909: FF         RST     0X38            
790A: FF         RST     0X38            
790B: FF         RST     0X38            
790C: FF         RST     0X38            
790D: FF         RST     0X38            
790E: FF         RST     0X38            
790F: FF         RST     0X38            
7910: FF         RST     0X38            
7911: FF         RST     0X38            
7912: FF         RST     0X38            
7913: FF         RST     0X38            
7914: FF         RST     0X38            
7915: FF         RST     0X38            
7916: FF         RST     0X38            
7917: FF         RST     0X38            
7918: FF         RST     0X38            
7919: FF         RST     0X38            
791A: FF         RST     0X38            
791B: FF         RST     0X38            
791C: FF         RST     0X38            
791D: FF         RST     0X38            
791E: FF         RST     0X38            
791F: FF         RST     0X38            
7920: FF         RST     0X38            
7921: FF         RST     0X38            
7922: FF         RST     0X38            
7923: FF         RST     0X38            
7924: FF         RST     0X38            
7925: FF         RST     0X38            
7926: FF         RST     0X38            
7927: FF         RST     0X38            
7928: FF         RST     0X38            
7929: FF         RST     0X38            
792A: FF         RST     0X38            
792B: FF         RST     0X38            
792C: FF         RST     0X38            
792D: FF         RST     0X38            
792E: FF         RST     0X38            
792F: FF         RST     0X38            
7930: FF         RST     0X38            
7931: FF         RST     0X38            
7932: FF         RST     0X38            
7933: FF         RST     0X38            
7934: FF         RST     0X38            
7935: FF         RST     0X38            
7936: FF         RST     0X38            
7937: FF         RST     0X38            
7938: FF         RST     0X38            
7939: FF         RST     0X38            
793A: FF         RST     0X38            
793B: FF         RST     0X38            
793C: FF         RST     0X38            
793D: FF         RST     0X38            
793E: FF         RST     0X38            
793F: FF         RST     0X38            
7940: FF         RST     0X38            
7941: FF         RST     0X38            
7942: FF         RST     0X38            
7943: FF         RST     0X38            
7944: FF         RST     0X38            
7945: FF         RST     0X38            
7946: FF         RST     0X38            
7947: FF         RST     0X38            
7948: FF         RST     0X38            
7949: FF         RST     0X38            
794A: FF         RST     0X38            
794B: FF         RST     0X38            
794C: FF         RST     0X38            
794D: FF         RST     0X38            
794E: FF         RST     0X38            
794F: FF         RST     0X38            
7950: FF         RST     0X38            
7951: FF         RST     0X38            
7952: FF         RST     0X38            
7953: FF         RST     0X38            
7954: FF         RST     0X38            
7955: FF         RST     0X38            
7956: FF         RST     0X38            
7957: FF         RST     0X38            
7958: FF         RST     0X38            
7959: FF         RST     0X38            
795A: FF         RST     0X38            
795B: FF         RST     0X38            
795C: FF         RST     0X38            
795D: FF         RST     0X38            
795E: FF         RST     0X38            
795F: FF         RST     0X38            
7960: FF         RST     0X38            
7961: FF         RST     0X38            
7962: FF         RST     0X38            
7963: FF         RST     0X38            
7964: FF         RST     0X38            
7965: FF         RST     0X38            
7966: FF         RST     0X38            
7967: FF         RST     0X38            
7968: FF         RST     0X38            
7969: FF         RST     0X38            
796A: FF         RST     0X38            
796B: FF         RST     0X38            
796C: FF         RST     0X38            
796D: FF         RST     0X38            
796E: FF         RST     0X38            
796F: FF         RST     0X38            
7970: FF         RST     0X38            
7971: FF         RST     0X38            
7972: FF         RST     0X38            
7973: FF         RST     0X38            
7974: FF         RST     0X38            
7975: FF         RST     0X38            
7976: FF         RST     0X38            
7977: FF         RST     0X38            
7978: FF         RST     0X38            
7979: FF         RST     0X38            
797A: FF         RST     0X38            
797B: FF         RST     0X38            
797C: FF         RST     0X38            
797D: FF         RST     0X38            
797E: FF         RST     0X38            
797F: FF         RST     0X38            
7980: FF         RST     0X38            
7981: FF         RST     0X38            
7982: FF         RST     0X38            
7983: FF         RST     0X38            
7984: FF         RST     0X38            
7985: FF         RST     0X38            
7986: FF         RST     0X38            
7987: FF         RST     0X38            
7988: FF         RST     0X38            
7989: FF         RST     0X38            
798A: FF         RST     0X38            
798B: FF         RST     0X38            
798C: FF         RST     0X38            
798D: FF         RST     0X38            
798E: FF         RST     0X38            
798F: FF         RST     0X38            
7990: FF         RST     0X38            
7991: FF         RST     0X38            
7992: FF         RST     0X38            
7993: FF         RST     0X38            
7994: FF         RST     0X38            
7995: FF         RST     0X38            
7996: FF         RST     0X38            
7997: FF         RST     0X38            
7998: FF         RST     0X38            
7999: FF         RST     0X38            
799A: FF         RST     0X38            
799B: FF         RST     0X38            
799C: FF         RST     0X38            
799D: FF         RST     0X38            
799E: FF         RST     0X38            
799F: FF         RST     0X38            
79A0: FF         RST     0X38            
79A1: FF         RST     0X38            
79A2: FF         RST     0X38            
79A3: FF         RST     0X38            
79A4: FF         RST     0X38            
79A5: FF         RST     0X38            
79A6: FF         RST     0X38            
79A7: FF         RST     0X38            
79A8: FF         RST     0X38            
79A9: FF         RST     0X38            
79AA: FF         RST     0X38            
79AB: FF         RST     0X38            
79AC: FF         RST     0X38            
79AD: FF         RST     0X38            
79AE: FF         RST     0X38            
79AF: FF         RST     0X38            
79B0: FF         RST     0X38            
79B1: FF         RST     0X38            
79B2: FF         RST     0X38            
79B3: FF         RST     0X38            
79B4: FF         RST     0X38            
79B5: FF         RST     0X38            
79B6: FF         RST     0X38            
79B7: FF         RST     0X38            
79B8: FF         RST     0X38            
79B9: FF         RST     0X38            
79BA: FF         RST     0X38            
79BB: FF         RST     0X38            
79BC: FF         RST     0X38            
79BD: FF         RST     0X38            
79BE: FF         RST     0X38            
79BF: FF         RST     0X38            
79C0: FF         RST     0X38            
79C1: FF         RST     0X38            
79C2: FF         RST     0X38            
79C3: FF         RST     0X38            
79C4: FF         RST     0X38            
79C5: FF         RST     0X38            
79C6: FF         RST     0X38            
79C7: FF         RST     0X38            
79C8: FF         RST     0X38            
79C9: FF         RST     0X38            
79CA: FF         RST     0X38            
79CB: FF         RST     0X38            
79CC: FF         RST     0X38            
79CD: FF         RST     0X38            
79CE: FF         RST     0X38            
79CF: FF         RST     0X38            
79D0: FF         RST     0X38            
79D1: FF         RST     0X38            
79D2: FF         RST     0X38            
79D3: FF         RST     0X38            
79D4: FF         RST     0X38            
79D5: FF         RST     0X38            
79D6: FF         RST     0X38            
79D7: FF         RST     0X38            
79D8: FF         RST     0X38            
79D9: FF         RST     0X38            
79DA: FF         RST     0X38            
79DB: FF         RST     0X38            
79DC: FF         RST     0X38            
79DD: FF         RST     0X38            
79DE: FF         RST     0X38            
79DF: FF         RST     0X38            
79E0: FF         RST     0X38            
79E1: FF         RST     0X38            
79E2: FF         RST     0X38            
79E3: FF         RST     0X38            
79E4: FF         RST     0X38            
79E5: FF         RST     0X38            
79E6: FF         RST     0X38            
79E7: FF         RST     0X38            
79E8: FF         RST     0X38            
79E9: FF         RST     0X38            
79EA: FF         RST     0X38            
79EB: FF         RST     0X38            
79EC: FF         RST     0X38            
79ED: FF         RST     0X38            
79EE: FF         RST     0X38            
79EF: FF         RST     0X38            
79F0: FF         RST     0X38            
79F1: FF         RST     0X38            
79F2: FF         RST     0X38            
79F3: FF         RST     0X38            
79F4: FF         RST     0X38            
79F5: FF         RST     0X38            
79F6: FF         RST     0X38            
79F7: FF         RST     0X38            
79F8: FF         RST     0X38            
79F9: FF         RST     0X38            
79FA: FF         RST     0X38            
79FB: FF         RST     0X38            
79FC: FF         RST     0X38            
79FD: FF         RST     0X38            
79FE: FF         RST     0X38            
79FF: FF         RST     0X38            
7A00: FF         RST     0X38            
7A01: FF         RST     0X38            
7A02: FF         RST     0X38            
7A03: FF         RST     0X38            
7A04: FF         RST     0X38            
7A05: FF         RST     0X38            
7A06: FF         RST     0X38            
7A07: FF         RST     0X38            
7A08: FF         RST     0X38            
7A09: FF         RST     0X38            
7A0A: FF         RST     0X38            
7A0B: FF         RST     0X38            
7A0C: FF         RST     0X38            
7A0D: FF         RST     0X38            
7A0E: FF         RST     0X38            
7A0F: FF         RST     0X38            
7A10: FF         RST     0X38            
7A11: FF         RST     0X38            
7A12: FF         RST     0X38            
7A13: FF         RST     0X38            
7A14: FF         RST     0X38            
7A15: FF         RST     0X38            
7A16: FF         RST     0X38            
7A17: FF         RST     0X38            
7A18: FF         RST     0X38            
7A19: FF         RST     0X38            
7A1A: FF         RST     0X38            
7A1B: FF         RST     0X38            
7A1C: FF         RST     0X38            
7A1D: FF         RST     0X38            
7A1E: FF         RST     0X38            
7A1F: FF         RST     0X38            
7A20: FF         RST     0X38            
7A21: FF         RST     0X38            
7A22: FF         RST     0X38            
7A23: FF         RST     0X38            
7A24: FF         RST     0X38            
7A25: FF         RST     0X38            
7A26: FF         RST     0X38            
7A27: FF         RST     0X38            
7A28: FF         RST     0X38            
7A29: FF         RST     0X38            
7A2A: FF         RST     0X38            
7A2B: FF         RST     0X38            
7A2C: FF         RST     0X38            
7A2D: FF         RST     0X38            
7A2E: FF         RST     0X38            
7A2F: FF         RST     0X38            
7A30: FF         RST     0X38            
7A31: FF         RST     0X38            
7A32: FF         RST     0X38            
7A33: FF         RST     0X38            
7A34: FF         RST     0X38            
7A35: FF         RST     0X38            
7A36: FF         RST     0X38            
7A37: FF         RST     0X38            
7A38: FF         RST     0X38            
7A39: FF         RST     0X38            
7A3A: FF         RST     0X38            
7A3B: FF         RST     0X38            
7A3C: FF         RST     0X38            
7A3D: FF         RST     0X38            
7A3E: FF         RST     0X38            
7A3F: FF         RST     0X38            
7A40: FF         RST     0X38            
7A41: FF         RST     0X38            
7A42: FF         RST     0X38            
7A43: FF         RST     0X38            
7A44: FF         RST     0X38            
7A45: FF         RST     0X38            
7A46: FF         RST     0X38            
7A47: FF         RST     0X38            
7A48: FF         RST     0X38            
7A49: FF         RST     0X38            
7A4A: FF         RST     0X38            
7A4B: FF         RST     0X38            
7A4C: FF         RST     0X38            
7A4D: FF         RST     0X38            
7A4E: FF         RST     0X38            
7A4F: FF         RST     0X38            
7A50: FF         RST     0X38            
7A51: FF         RST     0X38            
7A52: FF         RST     0X38            
7A53: FF         RST     0X38            
7A54: FF         RST     0X38            
7A55: FF         RST     0X38            
7A56: FF         RST     0X38            
7A57: FF         RST     0X38            
7A58: FF         RST     0X38            
7A59: FF         RST     0X38            
7A5A: FF         RST     0X38            
7A5B: FF         RST     0X38            
7A5C: FF         RST     0X38            
7A5D: FF         RST     0X38            
7A5E: FF         RST     0X38            
7A5F: FF         RST     0X38            
7A60: FF         RST     0X38            
7A61: FF         RST     0X38            
7A62: FF         RST     0X38            
7A63: FF         RST     0X38            
7A64: FF         RST     0X38            
7A65: FF         RST     0X38            
7A66: FF         RST     0X38            
7A67: FF         RST     0X38            
7A68: FF         RST     0X38            
7A69: FF         RST     0X38            
7A6A: FF         RST     0X38            
7A6B: FF         RST     0X38            
7A6C: FF         RST     0X38            
7A6D: FF         RST     0X38            
7A6E: FF         RST     0X38            
7A6F: FF         RST     0X38            
7A70: FF         RST     0X38            
7A71: FF         RST     0X38            
7A72: FF         RST     0X38            
7A73: FF         RST     0X38            
7A74: FF         RST     0X38            
7A75: FF         RST     0X38            
7A76: FF         RST     0X38            
7A77: FF         RST     0X38            
7A78: FF         RST     0X38            
7A79: FF         RST     0X38            
7A7A: FF         RST     0X38            
7A7B: FF         RST     0X38            
7A7C: FF         RST     0X38            
7A7D: FF         RST     0X38            
7A7E: FF         RST     0X38            
7A7F: FF         RST     0X38            
7A80: FF         RST     0X38            
7A81: FF         RST     0X38            
7A82: FF         RST     0X38            
7A83: FF         RST     0X38            
7A84: FF         RST     0X38            
7A85: FF         RST     0X38            
7A86: FF         RST     0X38            
7A87: FF         RST     0X38            
7A88: FF         RST     0X38            
7A89: FF         RST     0X38            
7A8A: FF         RST     0X38            
7A8B: FF         RST     0X38            
7A8C: FF         RST     0X38            
7A8D: FF         RST     0X38            
7A8E: FF         RST     0X38            
7A8F: FF         RST     0X38            
7A90: FF         RST     0X38            
7A91: FF         RST     0X38            
7A92: FF         RST     0X38            
7A93: FF         RST     0X38            
7A94: FF         RST     0X38            
7A95: FF         RST     0X38            
7A96: FF         RST     0X38            
7A97: FF         RST     0X38            
7A98: FF         RST     0X38            
7A99: FF         RST     0X38            
7A9A: FF         RST     0X38            
7A9B: FF         RST     0X38            
7A9C: FF         RST     0X38            
7A9D: FF         RST     0X38            
7A9E: FF         RST     0X38            
7A9F: FF         RST     0X38            
7AA0: FF         RST     0X38            
7AA1: FF         RST     0X38            
7AA2: FF         RST     0X38            
7AA3: FF         RST     0X38            
7AA4: FF         RST     0X38            
7AA5: FF         RST     0X38            
7AA6: FF         RST     0X38            
7AA7: FF         RST     0X38            
7AA8: FF         RST     0X38            
7AA9: FF         RST     0X38            
7AAA: FF         RST     0X38            
7AAB: FF         RST     0X38            
7AAC: FF         RST     0X38            
7AAD: FF         RST     0X38            
7AAE: FF         RST     0X38            
7AAF: FF         RST     0X38            
7AB0: FF         RST     0X38            
7AB1: FF         RST     0X38            
7AB2: FF         RST     0X38            
7AB3: FF         RST     0X38            
7AB4: FF         RST     0X38            
7AB5: FF         RST     0X38            
7AB6: FF         RST     0X38            
7AB7: FF         RST     0X38            
7AB8: FF         RST     0X38            
7AB9: FF         RST     0X38            
7ABA: FF         RST     0X38            
7ABB: FF         RST     0X38            
7ABC: FF         RST     0X38            
7ABD: FF         RST     0X38            
7ABE: FF         RST     0X38            
7ABF: FF         RST     0X38            
7AC0: FF         RST     0X38            
7AC1: FF         RST     0X38            
7AC2: FF         RST     0X38            
7AC3: FF         RST     0X38            
7AC4: FF         RST     0X38            
7AC5: FF         RST     0X38            
7AC6: FF         RST     0X38            
7AC7: FF         RST     0X38            
7AC8: FF         RST     0X38            
7AC9: FF         RST     0X38            
7ACA: FF         RST     0X38            
7ACB: FF         RST     0X38            
7ACC: FF         RST     0X38            
7ACD: FF         RST     0X38            
7ACE: FF         RST     0X38            
7ACF: FF         RST     0X38            
7AD0: FF         RST     0X38            
7AD1: FF         RST     0X38            
7AD2: FF         RST     0X38            
7AD3: FF         RST     0X38            
7AD4: FF         RST     0X38            
7AD5: FF         RST     0X38            
7AD6: FF         RST     0X38            
7AD7: FF         RST     0X38            
7AD8: FF         RST     0X38            
7AD9: FF         RST     0X38            
7ADA: FF         RST     0X38            
7ADB: FF         RST     0X38            
7ADC: FF         RST     0X38            
7ADD: FF         RST     0X38            
7ADE: FF         RST     0X38            
7ADF: FF         RST     0X38            
7AE0: FF         RST     0X38            
7AE1: FF         RST     0X38            
7AE2: FF         RST     0X38            
7AE3: FF         RST     0X38            
7AE4: FF         RST     0X38            
7AE5: FF         RST     0X38            
7AE6: FF         RST     0X38            
7AE7: FF         RST     0X38            
7AE8: FF         RST     0X38            
7AE9: FF         RST     0X38            
7AEA: FF         RST     0X38            
7AEB: FF         RST     0X38            
7AEC: FF         RST     0X38            
7AED: FF         RST     0X38            
7AEE: FF         RST     0X38            
7AEF: FF         RST     0X38            
7AF0: FF         RST     0X38            
7AF1: FF         RST     0X38            
7AF2: FF         RST     0X38            
7AF3: FF         RST     0X38            
7AF4: FF         RST     0X38            
7AF5: FF         RST     0X38            
7AF6: FF         RST     0X38            
7AF7: FF         RST     0X38            
7AF8: FF         RST     0X38            
7AF9: FF         RST     0X38            
7AFA: FF         RST     0X38            
7AFB: FF         RST     0X38            
7AFC: FF         RST     0X38            
7AFD: FF         RST     0X38            
7AFE: FF         RST     0X38            
7AFF: FF         RST     0X38            
7B00: FF         RST     0X38            
7B01: FF         RST     0X38            
7B02: FF         RST     0X38            
7B03: FF         RST     0X38            
7B04: FF         RST     0X38            
7B05: FF         RST     0X38            
7B06: FF         RST     0X38            
7B07: FF         RST     0X38            
7B08: FF         RST     0X38            
7B09: FF         RST     0X38            
7B0A: FF         RST     0X38            
7B0B: FF         RST     0X38            
7B0C: FF         RST     0X38            
7B0D: FF         RST     0X38            
7B0E: FF         RST     0X38            
7B0F: FF         RST     0X38            
7B10: FF         RST     0X38            
7B11: FF         RST     0X38            
7B12: FF         RST     0X38            
7B13: FF         RST     0X38            
7B14: FF         RST     0X38            
7B15: FF         RST     0X38            
7B16: FF         RST     0X38            
7B17: FF         RST     0X38            
7B18: FF         RST     0X38            
7B19: FF         RST     0X38            
7B1A: FF         RST     0X38            
7B1B: FF         RST     0X38            
7B1C: FF         RST     0X38            
7B1D: FF         RST     0X38            
7B1E: FF         RST     0X38            
7B1F: FF         RST     0X38            
7B20: FF         RST     0X38            
7B21: FF         RST     0X38            
7B22: FF         RST     0X38            
7B23: FF         RST     0X38            
7B24: FF         RST     0X38            
7B25: FF         RST     0X38            
7B26: FF         RST     0X38            
7B27: FF         RST     0X38            
7B28: FF         RST     0X38            
7B29: FF         RST     0X38            
7B2A: FF         RST     0X38            
7B2B: FF         RST     0X38            
7B2C: FF         RST     0X38            
7B2D: FF         RST     0X38            
7B2E: FF         RST     0X38            
7B2F: FF         RST     0X38            
7B30: FF         RST     0X38            
7B31: FF         RST     0X38            
7B32: FF         RST     0X38            
7B33: FF         RST     0X38            
7B34: FF         RST     0X38            
7B35: FF         RST     0X38            
7B36: FF         RST     0X38            
7B37: FF         RST     0X38            
7B38: FF         RST     0X38            
7B39: FF         RST     0X38            
7B3A: FF         RST     0X38            
7B3B: FF         RST     0X38            
7B3C: FF         RST     0X38            
7B3D: FF         RST     0X38            
7B3E: FF         RST     0X38            
7B3F: FF         RST     0X38            
7B40: FF         RST     0X38            
7B41: FF         RST     0X38            
7B42: FF         RST     0X38            
7B43: FF         RST     0X38            
7B44: FF         RST     0X38            
7B45: FF         RST     0X38            
7B46: FF         RST     0X38            
7B47: FF         RST     0X38            
7B48: FF         RST     0X38            
7B49: FF         RST     0X38            
7B4A: FF         RST     0X38            
7B4B: FF         RST     0X38            
7B4C: FF         RST     0X38            
7B4D: FF         RST     0X38            
7B4E: FF         RST     0X38            
7B4F: FF         RST     0X38            
7B50: FF         RST     0X38            
7B51: FF         RST     0X38            
7B52: FF         RST     0X38            
7B53: FF         RST     0X38            
7B54: FF         RST     0X38            
7B55: FF         RST     0X38            
7B56: FF         RST     0X38            
7B57: FF         RST     0X38            
7B58: FF         RST     0X38            
7B59: FF         RST     0X38            
7B5A: FF         RST     0X38            
7B5B: FF         RST     0X38            
7B5C: FF         RST     0X38            
7B5D: FF         RST     0X38            
7B5E: FF         RST     0X38            
7B5F: FF         RST     0X38            
7B60: FF         RST     0X38            
7B61: FF         RST     0X38            
7B62: FF         RST     0X38            
7B63: FF         RST     0X38            
7B64: FF         RST     0X38            
7B65: FF         RST     0X38            
7B66: FF         RST     0X38            
7B67: FF         RST     0X38            
7B68: FF         RST     0X38            
7B69: FF         RST     0X38            
7B6A: FF         RST     0X38            
7B6B: FF         RST     0X38            
7B6C: FF         RST     0X38            
7B6D: FF         RST     0X38            
7B6E: FF         RST     0X38            
7B6F: FF         RST     0X38            
7B70: FF         RST     0X38            
7B71: FF         RST     0X38            
7B72: FF         RST     0X38            
7B73: FF         RST     0X38            
7B74: FF         RST     0X38            
7B75: FF         RST     0X38            
7B76: FF         RST     0X38            
7B77: FF         RST     0X38            
7B78: FF         RST     0X38            
7B79: FF         RST     0X38            
7B7A: FF         RST     0X38            
7B7B: FF         RST     0X38            
7B7C: FF         RST     0X38            
7B7D: FF         RST     0X38            
7B7E: FF         RST     0X38            
7B7F: FF         RST     0X38            
7B80: FF         RST     0X38            
7B81: FF         RST     0X38            
7B82: FF         RST     0X38            
7B83: FF         RST     0X38            
7B84: FF         RST     0X38            
7B85: FF         RST     0X38            
7B86: FF         RST     0X38            
7B87: FF         RST     0X38            
7B88: FF         RST     0X38            
7B89: FF         RST     0X38            
7B8A: FF         RST     0X38            
7B8B: FF         RST     0X38            
7B8C: FF         RST     0X38            
7B8D: FF         RST     0X38            
7B8E: FF         RST     0X38            
7B8F: FF         RST     0X38            
7B90: FF         RST     0X38            
7B91: FF         RST     0X38            
7B92: FF         RST     0X38            
7B93: FF         RST     0X38            
7B94: FF         RST     0X38            
7B95: FF         RST     0X38            
7B96: FF         RST     0X38            
7B97: FF         RST     0X38            
7B98: FF         RST     0X38            
7B99: FF         RST     0X38            
7B9A: FF         RST     0X38            
7B9B: FF         RST     0X38            
7B9C: FF         RST     0X38            
7B9D: FF         RST     0X38            
7B9E: FF         RST     0X38            
7B9F: FF         RST     0X38            
7BA0: FF         RST     0X38            
7BA1: FF         RST     0X38            
7BA2: FF         RST     0X38            
7BA3: FF         RST     0X38            
7BA4: FF         RST     0X38            
7BA5: FF         RST     0X38            
7BA6: FF         RST     0X38            
7BA7: FF         RST     0X38            
7BA8: FF         RST     0X38            
7BA9: FF         RST     0X38            
7BAA: FF         RST     0X38            
7BAB: FF         RST     0X38            
7BAC: FF         RST     0X38            
7BAD: FF         RST     0X38            
7BAE: FF         RST     0X38            
7BAF: FF         RST     0X38            
7BB0: FF         RST     0X38            
7BB1: FF         RST     0X38            
7BB2: FF         RST     0X38            
7BB3: FF         RST     0X38            
7BB4: FF         RST     0X38            
7BB5: FF         RST     0X38            
7BB6: FF         RST     0X38            
7BB7: FF         RST     0X38            
7BB8: FF         RST     0X38            
7BB9: FF         RST     0X38            
7BBA: FF         RST     0X38            
7BBB: FF         RST     0X38            
7BBC: FF         RST     0X38            
7BBD: FF         RST     0X38            
7BBE: FF         RST     0X38            
7BBF: FF         RST     0X38            
7BC0: FF         RST     0X38            
7BC1: FF         RST     0X38            
7BC2: FF         RST     0X38            
7BC3: FF         RST     0X38            
7BC4: FF         RST     0X38            
7BC5: FF         RST     0X38            
7BC6: FF         RST     0X38            
7BC7: FF         RST     0X38            
7BC8: FF         RST     0X38            
7BC9: FF         RST     0X38            
7BCA: FF         RST     0X38            
7BCB: FF         RST     0X38            
7BCC: FF         RST     0X38            
7BCD: FF         RST     0X38            
7BCE: FF         RST     0X38            
7BCF: FF         RST     0X38            
7BD0: FF         RST     0X38            
7BD1: FF         RST     0X38            
7BD2: FF         RST     0X38            
7BD3: FF         RST     0X38            
7BD4: FF         RST     0X38            
7BD5: FF         RST     0X38            
7BD6: FF         RST     0X38            
7BD7: FF         RST     0X38            
7BD8: FF         RST     0X38            
7BD9: FF         RST     0X38            
7BDA: FF         RST     0X38            
7BDB: FF         RST     0X38            
7BDC: FF         RST     0X38            
7BDD: FF         RST     0X38            
7BDE: FF         RST     0X38            
7BDF: FF         RST     0X38            
7BE0: FF         RST     0X38            
7BE1: FF         RST     0X38            
7BE2: FF         RST     0X38            
7BE3: FF         RST     0X38            
7BE4: FF         RST     0X38            
7BE5: FF         RST     0X38            
7BE6: FF         RST     0X38            
7BE7: FF         RST     0X38            
7BE8: FF         RST     0X38            
7BE9: FF         RST     0X38            
7BEA: FF         RST     0X38            
7BEB: FF         RST     0X38            
7BEC: FF         RST     0X38            
7BED: FF         RST     0X38            
7BEE: FF         RST     0X38            
7BEF: FF         RST     0X38            
7BF0: FF         RST     0X38            
7BF1: FF         RST     0X38            
7BF2: FF         RST     0X38            
7BF3: FF         RST     0X38            
7BF4: FF         RST     0X38            
7BF5: FF         RST     0X38            
7BF6: FF         RST     0X38            
7BF7: FF         RST     0X38            
7BF8: FF         RST     0X38            
7BF9: FF         RST     0X38            
7BFA: FF         RST     0X38            
7BFB: FF         RST     0X38            
7BFC: FF         RST     0X38            
7BFD: FF         RST     0X38            
7BFE: FF         RST     0X38            
7BFF: FF         RST     0X38            
7C00: FF         RST     0X38            
7C01: FF         RST     0X38            
7C02: FF         RST     0X38            
7C03: FF         RST     0X38            
7C04: FF         RST     0X38            
7C05: FF         RST     0X38            
7C06: FF         RST     0X38            
7C07: FF         RST     0X38            
7C08: FF         RST     0X38            
7C09: FF         RST     0X38            
7C0A: FF         RST     0X38            
7C0B: FF         RST     0X38            
7C0C: FF         RST     0X38            
7C0D: FF         RST     0X38            
7C0E: FF         RST     0X38            
7C0F: FF         RST     0X38            
7C10: FF         RST     0X38            
7C11: FF         RST     0X38            
7C12: FF         RST     0X38            
7C13: FF         RST     0X38            
7C14: FF         RST     0X38            
7C15: FF         RST     0X38            
7C16: FF         RST     0X38            
7C17: FF         RST     0X38            
7C18: FF         RST     0X38            
7C19: FF         RST     0X38            
7C1A: FF         RST     0X38            
7C1B: FF         RST     0X38            
7C1C: FF         RST     0X38            
7C1D: FF         RST     0X38            
7C1E: FF         RST     0X38            
7C1F: FF         RST     0X38            
7C20: FF         RST     0X38            
7C21: FF         RST     0X38            
7C22: FF         RST     0X38            
7C23: FF         RST     0X38            
7C24: FF         RST     0X38            
7C25: FF         RST     0X38            
7C26: FF         RST     0X38            
7C27: FF         RST     0X38            
7C28: FF         RST     0X38            
7C29: FF         RST     0X38            
7C2A: FF         RST     0X38            
7C2B: FF         RST     0X38            
7C2C: FF         RST     0X38            
7C2D: FF         RST     0X38            
7C2E: FF         RST     0X38            
7C2F: FF         RST     0X38            
7C30: FF         RST     0X38            
7C31: FF         RST     0X38            
7C32: FF         RST     0X38            
7C33: FF         RST     0X38            
7C34: FF         RST     0X38            
7C35: FF         RST     0X38            
7C36: FF         RST     0X38            
7C37: FF         RST     0X38            
7C38: FF         RST     0X38            
7C39: FF         RST     0X38            
7C3A: FF         RST     0X38            
7C3B: FF         RST     0X38            
7C3C: FF         RST     0X38            
7C3D: FF         RST     0X38            
7C3E: FF         RST     0X38            
7C3F: FF         RST     0X38            
7C40: FF         RST     0X38            
7C41: FF         RST     0X38            
7C42: FF         RST     0X38            
7C43: FF         RST     0X38            
7C44: FF         RST     0X38            
7C45: FF         RST     0X38            
7C46: FF         RST     0X38            
7C47: FF         RST     0X38            
7C48: FF         RST     0X38            
7C49: FF         RST     0X38            
7C4A: FF         RST     0X38            
7C4B: FF         RST     0X38            
7C4C: FF         RST     0X38            
7C4D: FF         RST     0X38            
7C4E: FF         RST     0X38            
7C4F: FF         RST     0X38            
7C50: FF         RST     0X38            
7C51: FF         RST     0X38            
7C52: FF         RST     0X38            
7C53: FF         RST     0X38            
7C54: FF         RST     0X38            
7C55: FF         RST     0X38            
7C56: FF         RST     0X38            
7C57: FF         RST     0X38            
7C58: FF         RST     0X38            
7C59: FF         RST     0X38            
7C5A: FF         RST     0X38            
7C5B: FF         RST     0X38            
7C5C: FF         RST     0X38            
7C5D: FF         RST     0X38            
7C5E: FF         RST     0X38            
7C5F: FF         RST     0X38            
7C60: FF         RST     0X38            
7C61: FF         RST     0X38            
7C62: FF         RST     0X38            
7C63: FF         RST     0X38            
7C64: FF         RST     0X38            
7C65: FF         RST     0X38            
7C66: FF         RST     0X38            
7C67: FF         RST     0X38            
7C68: FF         RST     0X38            
7C69: FF         RST     0X38            
7C6A: FF         RST     0X38            
7C6B: FF         RST     0X38            
7C6C: FF         RST     0X38            
7C6D: FF         RST     0X38            
7C6E: FF         RST     0X38            
7C6F: FF         RST     0X38            
7C70: FF         RST     0X38            
7C71: FF         RST     0X38            
7C72: FF         RST     0X38            
7C73: FF         RST     0X38            
7C74: FF         RST     0X38            
7C75: FF         RST     0X38            
7C76: FF         RST     0X38            
7C77: FF         RST     0X38            
7C78: FF         RST     0X38            
7C79: FF         RST     0X38            
7C7A: FF         RST     0X38            
7C7B: FF         RST     0X38            
7C7C: FF         RST     0X38            
7C7D: FF         RST     0X38            
7C7E: FF         RST     0X38            
7C7F: FF         RST     0X38            
7C80: FF         RST     0X38            
7C81: FF         RST     0X38            
7C82: FF         RST     0X38            
7C83: FF         RST     0X38            
7C84: FF         RST     0X38            
7C85: FF         RST     0X38            
7C86: FF         RST     0X38            
7C87: FF         RST     0X38            
7C88: FF         RST     0X38            
7C89: FF         RST     0X38            
7C8A: FF         RST     0X38            
7C8B: FF         RST     0X38            
7C8C: FF         RST     0X38            
7C8D: FF         RST     0X38            
7C8E: FF         RST     0X38            
7C8F: FF         RST     0X38            
7C90: FF         RST     0X38            
7C91: FF         RST     0X38            
7C92: FF         RST     0X38            
7C93: FF         RST     0X38            
7C94: FF         RST     0X38            
7C95: FF         RST     0X38            
7C96: FF         RST     0X38            
7C97: FF         RST     0X38            
7C98: FF         RST     0X38            
7C99: FF         RST     0X38            
7C9A: FF         RST     0X38            
7C9B: FF         RST     0X38            
7C9C: FF         RST     0X38            
7C9D: FF         RST     0X38            
7C9E: FF         RST     0X38            
7C9F: FF         RST     0X38            
7CA0: FF         RST     0X38            
7CA1: FF         RST     0X38            
7CA2: FF         RST     0X38            
7CA3: FF         RST     0X38            
7CA4: FF         RST     0X38            
7CA5: FF         RST     0X38            
7CA6: FF         RST     0X38            
7CA7: FF         RST     0X38            
7CA8: FF         RST     0X38            
7CA9: FF         RST     0X38            
7CAA: FF         RST     0X38            
7CAB: FF         RST     0X38            
7CAC: FF         RST     0X38            
7CAD: FF         RST     0X38            
7CAE: FF         RST     0X38            
7CAF: FF         RST     0X38            
7CB0: FF         RST     0X38            
7CB1: FF         RST     0X38            
7CB2: FF         RST     0X38            
7CB3: FF         RST     0X38            
7CB4: FF         RST     0X38            
7CB5: FF         RST     0X38            
7CB6: FF         RST     0X38            
7CB7: FF         RST     0X38            
7CB8: FF         RST     0X38            
7CB9: FF         RST     0X38            
7CBA: FF         RST     0X38            
7CBB: FF         RST     0X38            
7CBC: FF         RST     0X38            
7CBD: FF         RST     0X38            
7CBE: FF         RST     0X38            
7CBF: FF         RST     0X38            
7CC0: FF         RST     0X38            
7CC1: FF         RST     0X38            
7CC2: FF         RST     0X38            
7CC3: FF         RST     0X38            
7CC4: FF         RST     0X38            
7CC5: FF         RST     0X38            
7CC6: FF         RST     0X38            
7CC7: FF         RST     0X38            
7CC8: FF         RST     0X38            
7CC9: FF         RST     0X38            
7CCA: FF         RST     0X38            
7CCB: FF         RST     0X38            
7CCC: FF         RST     0X38            
7CCD: FF         RST     0X38            
7CCE: FF         RST     0X38            
7CCF: FF         RST     0X38            
7CD0: FF         RST     0X38            
7CD1: FF         RST     0X38            
7CD2: FF         RST     0X38            
7CD3: FF         RST     0X38            
7CD4: FF         RST     0X38            
7CD5: FF         RST     0X38            
7CD6: FF         RST     0X38            
7CD7: FF         RST     0X38            
7CD8: FF         RST     0X38            
7CD9: FF         RST     0X38            
7CDA: FF         RST     0X38            
7CDB: FF         RST     0X38            
7CDC: FF         RST     0X38            
7CDD: FF         RST     0X38            
7CDE: FF         RST     0X38            
7CDF: FF         RST     0X38            
7CE0: FF         RST     0X38            
7CE1: FF         RST     0X38            
7CE2: FF         RST     0X38            
7CE3: FF         RST     0X38            
7CE4: FF         RST     0X38            
7CE5: FF         RST     0X38            
7CE6: FF         RST     0X38            
7CE7: FF         RST     0X38            
7CE8: FF         RST     0X38            
7CE9: FF         RST     0X38            
7CEA: FF         RST     0X38            
7CEB: FF         RST     0X38            
7CEC: FF         RST     0X38            
7CED: FF         RST     0X38            
7CEE: FF         RST     0X38            
7CEF: FF         RST     0X38            
7CF0: FF         RST     0X38            
7CF1: FF         RST     0X38            
7CF2: FF         RST     0X38            
7CF3: FF         RST     0X38            
7CF4: FF         RST     0X38            
7CF5: FF         RST     0X38            
7CF6: FF         RST     0X38            
7CF7: FF         RST     0X38            
7CF8: FF         RST     0X38            
7CF9: FF         RST     0X38            
7CFA: FF         RST     0X38            
7CFB: FF         RST     0X38            
7CFC: FF         RST     0X38            
7CFD: FF         RST     0X38            
7CFE: FF         RST     0X38            
7CFF: FF         RST     0X38            
7D00: 48         LD      C,B             
7D01: 61         LD      H,C             
7D02: 20 68      JR      NZ,$7D6C        
7D04: 61         LD      H,C             
7D05: 20 68      JR      NZ,$7D6F        
7D07: 61         LD      H,C             
7D08: 21 20 44   LD      HL,$4420        
7D0B: 6F         LD      L,A             
7D0C: 20 69      JR      NZ,$7D77        
7D0E: 74         LD      (HL),H          
7D0F: 21 44 6F   LD      HL,$6F44        
7D12: 20 69      JR      NZ,$7D7D        
7D14: 74         LD      (HL),H          
7D15: 21 20 20   LD      HL,$2020        
7D18: 44         LD      B,H             
7D19: 6F         LD      L,A             
7D1A: 20 69      JR      NZ,$7D85        
7D1C: 74         LD      (HL),H          
7D1D: 20 20      JR      NZ,$7D3F        
7D1F: 20 6D      JR      NZ,$7D8E        
7D21: 6F         LD      L,A             
7D22: 6F         LD      L,A             
7D23: 6F         LD      L,A             
7D24: 6F         LD      L,A             
7D25: 72         LD      (HL),D          
7D26: 65         LD      H,L             
7D27: 21 20 2E   LD      HL,$2E20        
7D2A: 2E 2E      LD      L,$2E           
7D2C: 20 2E      JR      NZ,$7D5C        
7D2E: 2E 2E      LD      L,$2E           
7D30: 48         LD      C,B             
7D31: 75         LD      (HL),L          
7D32: 6E         LD      L,(HL)          
7D33: 68         LD      L,B             
7D34: 3F         CCF                     
7D35: 20 20      JR      NZ,$7D57        
7D37: 4E         LD      C,(HL)          
7D38: 6F         LD      L,A             
7D39: 2C         INC     L               
7D3A: 20 69      JR      NZ,$7DA5        
7D3C: 74         LD      (HL),H          
7D3D: 5E         LD      E,(HL)          
7D3E: 73         LD      (HL),E          
7D3F: 20 6E      JR      NZ,$7DAF        
7D41: 6F         LD      L,A             
7D42: 74         LD      (HL),H          
7D43: 68         LD      L,B             
7D44: 69         LD      L,C             
7D45: 6E         LD      L,(HL)          
7D46: 67         LD      H,A             
7D47: 2E 2E      LD      L,$2E           
7D49: 2E 20      LD      L,$20           
7D4B: 49         LD      C,C             
7D4C: 20 20      JR      NZ,$7D6E        
7D4E: 20 20      JR      NZ,$7D70        
7D50: 64         LD      H,H             
7D51: 69         LD      L,C             
7D52: 64         LD      H,H             
7D53: 6E         LD      L,(HL)          
7D54: 5E         LD      E,(HL)          
7D55: 74         LD      (HL),H          
7D56: 20 6D      JR      NZ,$7DC5        
7D58: 65         LD      H,L             
7D59: 61         LD      H,C             
7D5A: 6E         LD      L,(HL)          
7D5B: 20 69      JR      NZ,$7DC6        
7D5D: 74         LD      (HL),H          
7D5E: 2E FF      LD      L,$FF           
7D60: 4E         LD      C,(HL)          
7D61: 6F         LD      L,A             
7D62: 74         LD      (HL),H          
7D63: 20 76      JR      NZ,$7DDB        
7D65: 65         LD      H,L             
7D66: 72         LD      (HL),D          
7D67: 79         LD      A,C             
7D68: 20 67      JR      NZ,$7DD1        
7D6A: 6F         LD      L,A             
7D6B: 6F         LD      L,A             
7D6C: 64         LD      H,H             
7D6D: 2E 2E      LD      L,$2E           
7D6F: 2E 45      LD      L,$45           
7D71: 68         LD      L,B             
7D72: 3F         CCF                     
7D73: 20 20      JR      NZ,$7D95        
7D75: 57         LD      D,A             
7D76: 68         LD      L,B             
7D77: 61         LD      H,C             
7D78: 74         LD      (HL),H          
7D79: 3F         CCF                     
7D7A: 20 20      JR      NZ,$7D9C        
7D7C: 44         LD      B,H             
7D7D: 69         LD      L,C             
7D7E: 64         LD      H,H             
7D7F: 20 49      JR      NZ,$7DCA        
7D81: 20 73      JR      NZ,$7DF6        
7D83: 61         LD      H,C             
7D84: 79         LD      A,C             
7D85: 20 73      JR      NZ,$7DFA        
7D87: 6F         LD      L,A             
7D88: 6D         LD      L,L             
7D89: 65         LD      H,L             
7D8A: 74         LD      (HL),H          
7D8B: 68         LD      L,B             
7D8C: 69         LD      L,C             
7D8D: 6E         LD      L,(HL)          
7D8E: 67         LD      H,A             
7D8F: 3F         CCF                     
7D90: 4E         LD      C,(HL)          
7D91: 6F         LD      L,A             
7D92: 2C         INC     L               
7D93: 20 79      JR      NZ,$7E0E        
7D95: 6F         LD      L,A             
7D96: 75         LD      (HL),L          
7D97: 5E         LD      E,(HL)          
7D98: 72         LD      (HL),D          
7D99: 65         LD      H,L             
7D9A: 20 68      JR      NZ,$7E04        
7D9C: 65         LD      H,L             
7D9D: 61         LD      H,C             
7D9E: 72         LD      (HL),D          
7D9F: 2D         DEC     L               
7DA0: 69         LD      L,C             
7DA1: 6E         LD      L,(HL)          
7DA2: 67         LD      H,A             
7DA3: 20 74      JR      NZ,$7E19        
7DA5: 68         LD      L,B             
7DA6: 69         LD      L,C             
7DA7: 6E         LD      L,(HL)          
7DA8: 67         LD      H,A             
7DA9: 73         LD      (HL),E          
7DAA: 2E 2E      LD      L,$2E           
7DAC: 2E FF      LD      L,$FF           
7DAE: 23         INC     HL              
7DAF: 23         INC     HL              
7DB0: 23         INC     HL              
7DB1: 23         INC     HL              
7DB2: 23         INC     HL              
7DB3: 2C         INC     L               
7DB4: 20 64      JR      NZ,$7E1A        
7DB6: 6F         LD      L,A             
7DB7: 20 79      JR      NZ,$7E32        
7DB9: 6F         LD      L,A             
7DBA: 75         LD      (HL),L          
7DBB: 20 20      JR      NZ,$7DDD        
7DBD: 20 61      JR      NZ,$7E20        
7DBF: 6C         LD      L,H             
7DC0: 77         LD      (HL),A          
7DC1: 61         LD      H,C             
7DC2: 79         LD      A,C             
7DC3: 73         LD      (HL),E          
7DC4: 20 6C      JR      NZ,$7E32        
7DC6: 6F         LD      L,A             
7DC7: 6F         LD      L,A             
7DC8: 6B         LD      L,E             
7DC9: 20 69      JR      NZ,$7E34        
7DCB: 6E         LD      L,(HL)          
7DCC: 20 20      JR      NZ,$7DEE        
7DCE: 6F         LD      L,A             
7DCF: 74         LD      (HL),H          
7DD0: 68         LD      L,B             
7DD1: 65         LD      H,L             
7DD2: 72         LD      (HL),D          
7DD3: 20 70      JR      NZ,$7E45        
7DD5: 65         LD      H,L             
7DD6: 6F         LD      L,A             
7DD7: 70         LD      (HL),B          
7DD8: 6C         LD      L,H             
7DD9: 65         LD      H,L             
7DDA: 5E         LD      E,(HL)          
7DDB: 73         LD      (HL),E          
7DDC: 20 20      JR      NZ,$7DFE        
7DDE: 64         LD      H,H             
7DDF: 72         LD      (HL),D          
7DE0: 61         LD      H,C             
7DE1: 77         LD      (HL),A          
7DE2: 65         LD      H,L             
7DE3: 72         LD      (HL),D          
7DE4: 73         LD      (HL),E          
7DE5: 3F         CCF                     
7DE6: FF         RST     0X38            
7DE7: 47         LD      B,A             
7DE8: 72         LD      (HL),D          
7DE9: 65         LD      H,L             
7DEA: 61         LD      H,C             
7DEB: 74         LD      (HL),H          
7DEC: 21 20 20   LD      HL,$2020        
7DEF: 44         LD      B,H             
7DF0: 69         LD      L,C             
7DF1: 67         LD      H,A             
7DF2: 20 69      JR      NZ,$7E5D        
7DF4: 74         LD      (HL),H          
7DF5: 21 20 44   LD      HL,$4420        
7DF8: 69         LD      L,C             
7DF9: 67         LD      H,A             
7DFA: 20 69      JR      NZ,$7E65        
7DFC: 74         LD      (HL),H          
7DFD: 21 20 20   LD      HL,$2020        
7E00: 44         LD      B,H             
7E01: 69         LD      L,C             
7E02: 67         LD      H,A             
7E03: 20 74      JR      NZ,$7E79        
7E05: 6F         LD      L,A             
7E06: 20 74      JR      NZ,$7E7C        
7E08: 68         LD      L,B             
7E09: 65         LD      H,L             
7E0A: 20 63      JR      NZ,$7E6F        
7E0C: 65         LD      H,L             
7E0D: 6E         LD      L,(HL)          
7E0E: 74         LD      (HL),H          
7E0F: 65         LD      H,L             
7E10: 72         LD      (HL),D          
7E11: 20 6F      JR      NZ,$7E82        
7E13: 66         LD      H,(HL)          
7E14: 20 20      JR      NZ,$7E36        
7E16: 20 74      JR      NZ,$7E8C        
7E18: 68         LD      L,B             
7E19: 65         LD      H,L             
7E1A: 20 65      JR      NZ,$7E81        
7E1C: 61         LD      H,C             
7E1D: 72         LD      (HL),D          
7E1E: 74         LD      (HL),H          
7E1F: 68         LD      L,B             
7E20: 21 21 FF   LD      HL,$FF21        
7E23: 57         LD      D,A             
7E24: 68         LD      L,B             
7E25: 65         LD      H,L             
7E26: 77         LD      (HL),A          
7E27: 21 20 20   LD      HL,$2020        
7E2A: 57         LD      D,A             
7E2B: 68         LD      L,B             
7E2C: 61         LD      H,C             
7E2D: 74         LD      (HL),H          
7E2E: 20 61      JR      NZ,$7E91        
7E30: 20 20      JR      NZ,$7E52        
7E32: 20 73      JR      NZ,$7EA7        
7E34: 75         LD      (HL),L          
7E35: 72         LD      (HL),D          
7E36: 70         LD      (HL),B          
7E37: 72         LD      (HL),D          
7E38: 69         LD      L,C             
7E39: 73         LD      (HL),E          
7E3A: 65         LD      H,L             
7E3B: 21 FF 4F   LD      HL,$4FFF        
7E3E: 68         LD      L,B             
7E3F: 68         LD      L,B             
7E40: 21 20 20   LD      HL,$2020        
7E43: 49         LD      C,C             
7E44: 5E         LD      E,(HL)          
7E45: 6D         LD      L,L             
7E46: 20 73      JR      NZ,$7EBB        
7E48: 6F         LD      L,A             
7E49: 72         LD      (HL),D          
7E4A: 72         LD      (HL),D          
7E4B: 79         LD      A,C             
7E4C: 21 41 72   LD      HL,$7241        
7E4F: 65         LD      H,L             
7E50: 20 79      JR      NZ,$7ECB        
7E52: 6F         LD      L,A             
7E53: 75         LD      (HL),L          
7E54: 20 6F      JR      NZ,$7EC5        
7E56: 6B         LD      L,E             
7E57: 61         LD      H,C             
7E58: 79         LD      A,C             
7E59: 3F         CCF                     
7E5A: 21 20 20   LD      HL,$2020        
7E5D: 23         INC     HL              
7E5E: 23         INC     HL              
7E5F: 23         INC     HL              
7E60: 23         INC     HL              
7E61: 23         INC     HL              
7E62: 3F         CCF                     
7E63: FF         RST     0X38            
7E64: 48         LD      C,B             
7E65: 65         LD      H,L             
7E66: 79         LD      A,C             
7E67: 20 4D      JR      NZ,$7EB6        
7E69: 6F         LD      L,A             
7E6A: 6E         LD      L,(HL)          
7E6B: 21 FF 59   LD      HL,$59FF        
7E6E: 6F         LD      L,A             
7E6F: 75         LD      (HL),L          
7E70: 20 6B      JR      NZ,$7EDD        
7E72: 6E         LD      L,(HL)          
7E73: 6F         LD      L,A             
7E74: 77         LD      (HL),A          
7E75: 20 6D      JR      NZ,$7EE4        
7E77: 65         LD      H,L             
7E78: 2C         INC     L               
7E79: 20 49      JR      NZ,$7EC4        
7E7B: 20 20      JR      NZ,$7E9D        
7E7D: 6C         LD      L,H             
7E7E: 69         LD      L,C             
7E7F: 6B         LD      L,E             
7E80: 65         LD      H,L             
7E81: 20 73      JR      NZ,$7EF6        
7E83: 68         LD      L,B             
7E84: 6F         LD      L,A             
7E85: 72         LD      (HL),D          
7E86: 74         LD      (HL),H          
7E87: 20 6E      JR      NZ,$7EF7        
7E89: 61         LD      H,C             
7E8A: 6D         LD      L,L             
7E8B: 65         LD      H,L             
7E8C: 73         LD      (HL),E          
7E8D: 74         LD      (HL),H          
7E8E: 68         LD      L,B             
7E8F: 65         LD      H,L             
7E90: 20 62      JR      NZ,$7EF4        
7E92: 65         LD      H,L             
7E93: 73         LD      (HL),E          
7E94: 74         LD      (HL),H          
7E95: 2E 2E      LD      L,$2E           
7E97: 2E FF      LD      L,$FF           
7E99: 49         LD      C,C             
7E9A: 74         LD      (HL),H          
7E9B: 20 63      JR      NZ,$7F00        
7E9D: 61         LD      H,C             
7E9E: 6E         LD      L,(HL)          
7E9F: 20 64      JR      NZ,$7F05        
7EA1: 69         LD      L,C             
7EA2: 73         LD      (HL),E          
7EA3: 70         LD      (HL),B          
7EA4: 6C         LD      L,H             
7EA5: 61         LD      H,C             
7EA6: 79         LD      A,C             
7EA7: 20 20      JR      NZ,$7EC9        
7EA9: 6D         LD      L,L             
7EAA: 69         LD      L,C             
7EAB: 6C         LD      L,H             
7EAC: 6C         LD      L,H             
7EAD: 69         LD      L,C             
7EAE: 6F         LD      L,A             
7EAF: 6E         LD      L,(HL)          
7EB0: 73         LD      (HL),E          
7EB1: 20 6F      JR      NZ,$7F22        
7EB3: 66         LD      H,(HL)          
7EB4: 20 20      JR      NZ,$7ED6        
7EB6: 20 20      JR      NZ,$7ED8        
7EB8: 20 70      JR      NZ,$7F2A        
7EBA: 6F         LD      L,A             
7EBB: 6C         LD      L,H             
7EBC: 79         LD      A,C             
7EBD: 67         LD      H,A             
7EBE: 6F         LD      L,A             
7EBF: 6E         LD      L,(HL)          
7EC0: 73         LD      (HL),E          
7EC1: 21 FF 49   LD      HL,$49FF        
7EC4: 20 64      JR      NZ,$7F2A        
7EC6: 65         LD      H,L             
7EC7: 66         LD      H,(HL)          
7EC8: 69         LD      L,C             
7EC9: 6E         LD      L,(HL)          
7ECA: 69         LD      L,C             
7ECB: 74         LD      (HL),H          
7ECC: 65         LD      H,L             
7ECD: 6C         LD      L,H             
7ECE: 79         LD      A,C             
7ECF: 20 20      JR      NZ,$7EF1        
7ED1: 20 20      JR      NZ,$7EF3        
7ED3: 6E         LD      L,(HL)          
7ED4: 65         LD      H,L             
7ED5: 65         LD      H,L             
7ED6: 64         LD      H,H             
7ED7: 20 69      JR      NZ,$7F42        
7ED9: 74         LD      (HL),H          
7EDA: 2C         INC     L               
7EDB: 20 61      JR      NZ,$7F3E        
7EDD: 73         LD      (HL),E          
7EDE: 20 73      JR      NZ,$7F53        
7EE0: 6F         LD      L,A             
7EE1: 6F         LD      L,A             
7EE2: 6E         LD      L,(HL)          
7EE3: 61         LD      H,C             
7EE4: 73         LD      (HL),E          
7EE5: 20 70      JR      NZ,$7F57        
7EE7: 6F         LD      L,A             
7EE8: 73         LD      (HL),E          
7EE9: 73         LD      (HL),E          
7EEA: 69         LD      L,C             
7EEB: 62         LD      H,D             
7EEC: 6C         LD      L,H             
7EED: 65         LD      H,L             
7EEE: 21 FF FF   LD      HL,$FFFF        
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
