![Bank 10](GBZelda.jpg)

# Bank 10

>>> cpu Z80GB

>>> memoryTable ram 
[RAM Usage](RAMUse.md)

>>> memoryTable hard 
[Hardware Info](../Hardware.md)

```
4000: FF         RST     0X38            
4001: FF         RST     0X38            
4002: FF         RST     0X38            
4003: FF         RST     0X38            
4004: FF         RST     0X38            
4005: FF         RST     0X38            
4006: FF         RST     0X38            
4007: FF         RST     0X38            
4008: FF         RST     0X38            
4009: FF         RST     0X38            
400A: FF         RST     0X38            
400B: FF         RST     0X38            
400C: EF         RST     0X28            
400D: EF         RST     0X28            
400E: F7         RST     0X30            
400F: F7         RST     0X30            
4010: FF         RST     0X38            
4011: FF         RST     0X38            
4012: FF         RST     0X38            
4013: FF         RST     0X38            
4014: FE FE      CP      $FE             
4016: FF         RST     0X38            
4017: FF         RST     0X38            
4018: FF         RST     0X38            
4019: FF         RST     0X38            
401A: FF         RST     0X38            
401B: FF         RST     0X38            
401C: FF         RST     0X38            
401D: FF         RST     0X38            
401E: FF         RST     0X38            
401F: FF         RST     0X38            
4020: FF         RST     0X38            
4021: FF         RST     0X38            
4022: FF         RST     0X38            
4023: FF         RST     0X38            
4024: FF         RST     0X38            
4025: FF         RST     0X38            
4026: 5F         LD      E,A             
4027: 5F         LD      E,A             
4028: AB         XOR     E               
4029: AB         XOR     E               
402A: D5         PUSH    DE              
402B: D5         PUSH    DE              
402C: FA FA FF   LD      A,($FFFA)       
402F: FF         RST     0X38            
4030: FF         RST     0X38            
4031: FF         RST     0X38            
4032: FF         RST     0X38            
4033: FF         RST     0X38            
4034: FF         RST     0X38            
4035: FF         RST     0X38            
4036: FF         RST     0X38            
4037: FF         RST     0X38            
4038: FF         RST     0X38            
4039: FF         RST     0X38            
403A: 55         LD      D,L             
403B: 55         LD      D,L             
403C: AA         XOR     D               
403D: AA         XOR     D               
403E: 55         LD      D,L             
403F: 55         LD      D,L             
4040: FA FA FD   LD      A,($FDFA)       
4043: FD         ???                     
4044: FE FE      CP      $FE             
4046: FF         RST     0X38            
4047: FF         RST     0X38            
4048: FA FA 55   LD      A,($55FA)       
404B: 55         LD      D,L             
404C: AB         XOR     E               
404D: AB         XOR     E               
404E: 5F         LD      E,A             
404F: 5F         LD      E,A             
4050: FF         RST     0X38            
4051: FF         RST     0X38            
4052: 5F         LD      E,A             
4053: 5F         LD      E,A             
4054: AA         XOR     D               
4055: AA         XOR     D               
4056: 55         LD      D,L             
4057: 55         LD      D,L             
4058: AA         XOR     D               
4059: AA         XOR     D               
405A: 55         LD      D,L             
405B: 55         LD      D,L             
405C: AA         XOR     D               
405D: AA         XOR     D               
405E: D5         PUSH    DE              
405F: D5         PUSH    DE              
4060: FE FE      CP      $FE             
4062: F5         PUSH    AF              
4063: F5         PUSH    AF              
4064: AB         XOR     E               
4065: AB         XOR     E               
4066: 57         LD      D,A             
4067: 57         LD      D,A             
4068: FF         RST     0X38            
4069: FF         RST     0X38            
406A: 5D         LD      E,L             
406B: 5D         LD      E,L             
406C: AA         XOR     D               
406D: AA         XOR     D               
406E: 55         LD      D,L             
406F: 55         LD      D,L             
4070: BB         CP      E               
4071: BB         CP      E               
4072: 7D         LD      A,L             
4073: 7D         LD      A,L             
4074: FE FE      CP      $FE             
4076: DF         RST     0X18            
4077: DF         RST     0X18            
4078: AB         XOR     E               
4079: AB         XOR     E               
407A: 55         LD      D,L             
407B: 55         LD      D,L             
407C: AA         XOR     D               
407D: AA         XOR     D               
407E: 5D         LD      E,L             
407F: 5D         LD      E,L             
4080: EA EA D5   LD      ($D5EA),A       
4083: D5         PUSH    DE              
4084: AA         XOR     D               
4085: AA         XOR     D               
4086: 55         LD      D,L             
4087: 55         LD      D,L             
4088: AA         XOR     D               
4089: AA         XOR     D               
408A: 55         LD      D,L             
408B: 55         LD      D,L             
408C: 2A         LD      A,(HLI)         
408D: 2A         LD      A,(HLI)         
408E: 05         DEC     B               
408F: 05         DEC     B               
4090: FA FA 7F   LD      A,($7FFA)       
4093: 7F         LD      A,A             
4094: AF         XOR     A               
4095: AF         XOR     A               
4096: 55         LD      D,L             
4097: 55         LD      D,L             
4098: AA         XOR     D               
4099: AA         XOR     D               
409A: 55         LD      D,L             
409B: 55         LD      D,L             
409C: AA         XOR     D               
409D: AA         XOR     D               
409E: 50         LD      D,B             
409F: 50         LD      D,B             
40A0: AB         XOR     E               
40A1: AB         XOR     E               
40A2: FD         ???                     
40A3: FD         ???                     
40A4: EA EA 55   LD      ($55EA),A       
40A7: 55         LD      D,L             
40A8: AA         XOR     D               
40A9: AA         XOR     D               
40AA: 55         LD      D,L             
40AB: 55         LD      D,L             
40AC: 0A         LD      A,(BC)          
40AD: 0A         LD      A,(BC)          
40AE: 00         NOP                     
40AF: 00         NOP                     
40B0: AF         XOR     A               
40B1: AF         XOR     A               
40B2: 55         LD      D,L             
40B3: 55         LD      D,L             
40B4: AA         XOR     D               
40B5: AA         XOR     D               
40B6: 55         LD      D,L             
40B7: 55         LD      D,L             
40B8: AA         XOR     D               
40B9: AA         XOR     D               
40BA: 55         LD      D,L             
40BB: 55         LD      D,L             
40BC: AA         XOR     D               
40BD: AA         XOR     D               
40BE: 50         LD      D,B             
40BF: 50         LD      D,B             
40C0: FF         RST     0X38            
40C1: FF         RST     0X38            
40C2: 3F         CCF                     
40C3: 3F         CCF                     
40C4: 1F         RRA                     
40C5: 1F         RRA                     
40C6: 03         INC     BC              
40C7: 03         INC     BC              
40C8: 80         ADD     A,B             
40C9: 80         ADD     A,B             
40CA: F0 F0      LD      A,($F0)         
40CC: FF         RST     0X38            
40CD: FF         RST     0X38            
40CE: FF         RST     0X38            
40CF: FF         RST     0X38            
40D0: FF         RST     0X38            
40D1: FF         RST     0X38            
40D2: FF         RST     0X38            
40D3: FF         RST     0X38            
40D4: FF         RST     0X38            
40D5: FF         RST     0X38            
40D6: E7         RST     0X20            
40D7: E7         RST     0X20            
40D8: 1F         RRA                     
40D9: 1F         RRA                     
40DA: FF         RST     0X38            
40DB: FF         RST     0X38            
40DC: FC         ???                     
40DD: FC         ???                     
40DE: F0 F0      LD      A,($F0)         
40E0: FF         RST     0X38            
40E1: FF         RST     0X38            
40E2: FF         RST     0X38            
40E3: FF         RST     0X38            
40E4: FF         RST     0X38            
40E5: FF         RST     0X38            
40E6: FF         RST     0X38            
40E7: FF         RST     0X38            
40E8: CF         RST     0X08            
40E9: CF         RST     0X08            
40EA: 07         RLCA                    
40EB: 07         RLCA                    
40EC: 03         INC     BC              
40ED: 03         INC     BC              
40EE: 01 01 FF   LD      BC,$FF01        
40F1: FF         RST     0X38            
40F2: FC         ???                     
40F3: FC         ???                     
40F4: F0 F0      LD      A,($F0)         
40F6: 84         ADD     A,H             
40F7: 84         ADD     A,H             
40F8: FF         RST     0X38            
40F9: FF         RST     0X38            
40FA: FF         RST     0X38            
40FB: FF         RST     0X38            
40FC: FF         RST     0X38            
40FD: FF         RST     0X38            
40FE: FF         RST     0X38            
40FF: FF         RST     0X38            
4100: FF         RST     0X38            
4101: 00         NOP                     
4102: EF         RST     0X28            
4103: 10 10      STOP    $10             
4105: EF         RST     0X28            
4106: 80         ADD     A,B             
4107: 7F         LD      A,A             
4108: 00         NOP                     
4109: F3         DI                      
410A: 00         NOP                     
410B: C0         RET     NZ              
410C: F0 00      LD      A,($00)         
410E: 3C         INC     A               
410F: 00         NOP                     
4110: C0         RET     NZ              
4111: 3F         CCF                     
4112: 07         RLCA                    
4113: F8 7F      LDHL    SP,$7F          
4115: 80         ADD     A,B             
4116: FE 01      CP      $01             
4118: 3F         CCF                     
4119: C0         RET     NZ              
411A: 0F         RRCA                    
411B: F0 00      LD      A,($00)         
411D: 0F         RRCA                    
411E: 1F         RRA                     
411F: 00         NOP                     
4120: 7F         LD      A,A             
4121: 80         ADD     A,B             
4122: 0E F1      LD      C,$F1           
4124: F0 0F      LD      A,($0F)         
4126: 03         INC     BC              
4127: FC         ???                     
4128: 9F         SBC     A               
4129: 60         LD      H,B             
412A: FF         RST     0X38            
412B: 00         NOP                     
412C: 1F         RRA                     
412D: E0 3E      LDFF00  ($3E),A         
412F: 01 C7 38   LD      BC,$38C7        
4132: 01 FE 3C   LD      BC,$3CFE        
4135: C3 FF 00   JP      $00FF           
4138: FF         RST     0X38            
4139: 00         NOP                     
413A: FE 01      CP      $01             
413C: F0 0F      LD      A,($0F)         
413E: 01 F8 1C   LD      BC,$1CF8        
4141: 00         NOP                     
4142: 07         RLCA                    
4143: 00         NOP                     
4144: 1E 00      LD      E,$00           
4146: 60         LD      H,B             
4147: 00         NOP                     
4148: 00         NOP                     
4149: 00         NOP                     
414A: 07         RLCA                    
414B: 00         NOP                     
414C: FF         RST     0X38            
414D: 00         NOP                     
414E: FF         RST     0X38            
414F: 3F         CCF                     
4150: 38 00      JR      C,$4152         
4152: E0 00      LDFF00  ($00),A         
4154: 03         INC     BC              
4155: 00         NOP                     
4156: 0E 00      LD      C,$00           
4158: 3C         INC     A               
4159: 0C         INC     C               
415A: FF         RST     0X38            
415B: 3F         CCF                     
415C: FF         RST     0X38            
415D: FF         RST     0X38            
415E: FF         RST     0X38            
415F: FF         RST     0X38            
4160: 00         NOP                     
4161: 00         NOP                     
4162: 70         LD      (HL),B          
4163: 00         NOP                     
4164: FC         ???                     
4165: 00         NOP                     
4166: FF         RST     0X38            
4167: 00         NOP                     
4168: 3F         CCF                     
4169: 00         NOP                     
416A: 03         INC     BC              
416B: 00         NOP                     
416C: E0 E0      LDFF00  ($E0),A         
416E: FF         RST     0X38            
416F: FF         RST     0X38            
4170: 00         NOP                     
4171: 00         NOP                     
4172: 00         NOP                     
4173: 00         NOP                     
4174: 00         NOP                     
4175: 00         NOP                     
4176: 80         ADD     A,B             
4177: 00         NOP                     
4178: FC         ???                     
4179: 00         NOP                     
417A: E1         POP     HL              
417B: 00         NOP                     
417C: 1F         RRA                     
417D: 00         NOP                     
417E: FE 00      CP      $00             
4180: FF         RST     0X38            
4181: FF         RST     0X38            
4182: FE FE      CP      $FE             
4184: E0 E0      LDFF00  ($E0),A         
4186: 00         NOP                     
4187: 00         NOP                     
4188: 00         NOP                     
4189: 00         NOP                     
418A: 83         ADD     A,E             
418B: 83         ADD     A,E             
418C: FF         RST     0X38            
418D: FF         RST     0X38            
418E: FF         RST     0X38            
418F: FF         RST     0X38            
4190: C3 C3 0E   JP      $0EC3           
4193: 0E 30      LD      C,$30           
4195: 30 00      JR      NC,$4197        
4197: 00         NOP                     
4198: 70         LD      (HL),B          
4199: 70         LD      (HL),B          
419A: FC         ???                     
419B: FC         ???                     
419C: FF         RST     0X38            
419D: FF         RST     0X38            
419E: FF         RST     0X38            
419F: FF         RST     0X38            
41A0: 80         ADD     A,B             
41A1: 80         ADD     A,B             
41A2: E0 E0      LDFF00  ($E0),A         
41A4: 7E         LD      A,(HL)          
41A5: 7E         LD      A,(HL)          
41A6: 7F         LD      A,A             
41A7: 7F         LD      A,A             
41A8: 3F         CCF                     
41A9: 3F         CCF                     
41AA: 0F         RRCA                    
41AB: 0F         RRCA                    
41AC: 07         RLCA                    
41AD: 07         RLCA                    
41AE: E1         POP     HL              
41AF: E1         POP     HL              
41B0: 7F         LD      A,A             
41B1: 7F         LD      A,A             
41B2: 0F         RRCA                    
41B3: 0F         RRCA                    
41B4: 00         NOP                     
41B5: 00         NOP                     
41B6: 80         ADD     A,B             
41B7: 80         ADD     A,B             
41B8: FE FE      CP      $FE             
41BA: FF         RST     0X38            
41BB: FF         RST     0X38            
41BC: FF         RST     0X38            
41BD: FF         RST     0X38            
41BE: FF         RST     0X38            
41BF: FF         RST     0X38            
41C0: F8 F8      LDHL    SP,$F8          
41C2: FF         RST     0X38            
41C3: FF         RST     0X38            
41C4: FF         RST     0X38            
41C5: FF         RST     0X38            
41C6: FF         RST     0X38            
41C7: FF         RST     0X38            
41C8: FF         RST     0X38            
41C9: FF         RST     0X38            
41CA: FF         RST     0X38            
41CB: FF         RST     0X38            
41CC: FF         RST     0X38            
41CD: FF         RST     0X38            
41CE: FF         RST     0X38            
41CF: FF         RST     0X38            
41D0: 03         INC     BC              
41D1: 03         INC     BC              
41D2: FF         RST     0X38            
41D3: FF         RST     0X38            
41D4: FF         RST     0X38            
41D5: FF         RST     0X38            
41D6: FF         RST     0X38            
41D7: FF         RST     0X38            
41D8: FF         RST     0X38            
41D9: FF         RST     0X38            
41DA: FF         RST     0X38            
41DB: FF         RST     0X38            
41DC: FF         RST     0X38            
41DD: FF         RST     0X38            
41DE: FF         RST     0X38            
41DF: FF         RST     0X38            
41E0: BF         CP      A               
41E1: 3F         CCF                     
41E2: DF         RST     0X18            
41E3: 1F         RRA                     
41E4: 6F         LD      L,A             
41E5: 8F         ADC     A,A             
41E6: 37         SCF                     
41E7: C7         RST     0X00            
41E8: 1B         DEC     DE              
41E9: E3         ???                     
41EA: 09         ADD     HL,BC           
41EB: F1         POP     AF              
41EC: 0D         DEC     C               
41ED: F1         POP     AF              
41EE: 06 F8      LD      B,$F8           
41F0: 06 F8      LD      B,$F8           
41F2: 07         RLCA                    
41F3: F8 07      LDHL    SP,$07          
41F5: F8 07      LDHL    SP,$07          
41F7: F8 0F      LDHL    SP,$0F          
41F9: F0 0F      LD      A,($0F)         
41FB: F1         POP     AF              
41FC: 1F         RRA                     
41FD: E1         POP     HL              
41FE: 3E C2      LD      A,$C2           
4200: FF         RST     0X38            
4201: FE FD      CP      $FD             
4203: FC         ???                     
4204: FF         RST     0X38            
4205: FC         ???                     
4206: FB         EI                      
4207: F8 FF      LDHL    SP,$FF          
4209: F8 F7      LDHL    SP,$F7          
420B: F0 FF      LD      A,($FF)         
420D: F0 EE      LD      A,($EE)         
420F: E0 FF      LDFF00  ($FF),A         
4211: 00         NOP                     
4212: FF         RST     0X38            
4213: 00         NOP                     
4214: E6 00      AND     $00             
4216: C6 00      ADD     $00             
4218: C6 00      ADD     $00             
421A: CE 00      ADC     $00             
421C: 7C         LD      A,H             
421D: 00         NOP                     
421E: 78         LD      A,B             
421F: 00         NOP                     
4220: 07         RLCA                    
4221: 00         NOP                     
4222: 0E 00      LD      C,$00           
4224: 1E 00      LD      E,$00           
4226: 1C         INC     E               
4227: 00         NOP                     
4228: 78         LD      A,B             
4229: 00         NOP                     
422A: E0 00      LDFF00  ($00),A         
422C: C1         POP     BC              
422D: 01 C3 03   LD      BC,$03C3        
4230: 00         NOP                     
4231: 00         NOP                     
4232: 00         NOP                     
4233: 00         NOP                     
4234: 31 31 31   LD      SP,$3131        
4237: 31 33 33   LD      SP,$3333        
423A: F7         RST     0X30            
423B: F7         RST     0X30            
423C: E7         RST     0X20            
423D: E7         RST     0X20            
423E: C3 C3 FF   JP      $FFC3           
4241: FF         RST     0X38            
4242: FF         RST     0X38            
4243: FF         RST     0X38            
4244: FF         RST     0X38            
4245: FF         RST     0X38            
4246: CF         RST     0X08            
4247: CF         RST     0X08            
4248: 8F         ADC     A,A             
4249: 8F         ADC     A,A             
424A: 8F         ADC     A,A             
424B: 8F         ADC     A,A             
424C: 0F         RRCA                    
424D: 0F         RRCA                    
424E: 0F         RRCA                    
424F: 0F         RRCA                    
4250: FA E5 D0   LD      A,($D0E5)       
4253: CF         RST     0X08            
4254: FD         ???                     
4255: C1         POP     BC              
4256: EF         RST     0X28            
4257: CF         RST     0X08            
4258: FF         RST     0X38            
4259: FF         RST     0X38            
425A: FC         ???                     
425B: FC         ???                     
425C: F7         RST     0X30            
425D: F0 FE      LD      A,($FE)         
425F: E0 3F      LDFF00  ($3F),A         
4261: C1         POP     BC              
4262: 00         NOP                     
4263: FF         RST     0X38            
4264: F9         LD      SP,HL           
4265: F8 FF      LDHL    SP,$FF          
4267: FF         RST     0X38            
4268: FF         RST     0X38            
4269: FF         RST     0X38            
426A: 03         INC     BC              
426B: 03         INC     BC              
426C: 78         LD      A,B             
426D: 00         NOP                     
426E: 78         LD      A,B             
426F: 00         NOP                     
4270: F3         DI                      
4271: C0         RET     NZ              
4272: F3         DI                      
4273: 00         NOP                     
4274: 36 C0      LD      (HL),$C0        
4276: 9E         SBC     (HL)            
4277: 80         ADD     A,B             
4278: F8 F8      LDHL    SP,$F8          
427A: FE FE      CP      $FE             
427C: 3F         CCF                     
427D: 3F         CCF                     
427E: C7         RST     0X00            
427F: 07         RLCA                    
4280: 00         NOP                     
4281: 00         NOP                     
4282: 1E 1E      LD      E,$1E           
4284: 3B         DEC     SP              
4285: 23         INC     HL              
4286: 3B         DEC     SP              
4287: 23         INC     HL              
4288: 23         INC     HL              
4289: 23         INC     HL              
428A: 1E 1E      LD      E,$1E           
428C: 8E         ADC     A,(HL)          
428D: 8E         ADC     A,(HL)          
428E: EC         ???                     
428F: EC         ???                     
4290: FF         RST     0X38            
4291: FF         RST     0X38            
4292: BF         CP      A               
4293: BF         CP      A               
4294: 9F         SBC     A               
4295: 9F         SBC     A               
4296: 1F         RRA                     
4297: 1F         RRA                     
4298: 3F         CCF                     
4299: 3F         CCF                     
429A: 7F         LD      A,A             
429B: 7F         LD      A,A             
429C: EF         RST     0X28            
429D: 8F         ADC     A,A             
429E: EF         RST     0X28            
429F: 8F         ADC     A,A             
42A0: F8 F8      LDHL    SP,$F8          
42A2: F8 F8      LDHL    SP,$F8          
42A4: 7D         LD      A,L             
42A5: 7D         LD      A,L             
42A6: 3F         CCF                     
42A7: 3F         CCF                     
42A8: 1D         DEC     E               
42A9: 1C         INC     E               
42AA: 3F         CCF                     
42AB: 38 77      JR      C,$4324         
42AD: 70         LD      (HL),B          
42AE: 7F         LD      A,A             
42AF: 70         LD      (HL),B          
42B0: 8F         ADC     A,A             
42B1: 8F         ADC     A,A             
42B2: FF         RST     0X38            
42B3: FF         RST     0X38            
42B4: FB         EI                      
42B5: FB         EI                      
42B6: F3         DI                      
42B7: 93         SUB     E               
42B8: F7         RST     0X30            
42B9: 37         SCF                     
42BA: BF         CP      A               
42BB: 3F         CCF                     
42BC: FF         RST     0X38            
42BD: 7F         LD      A,A             
42BE: BF         CP      A               
42BF: 3F         CCF                     
42C0: FF         RST     0X38            
42C1: FF         RST     0X38            
42C2: FF         RST     0X38            
42C3: FF         RST     0X38            
42C4: FF         RST     0X38            
42C5: FF         RST     0X38            
42C6: FF         RST     0X38            
42C7: FF         RST     0X38            
42C8: FF         RST     0X38            
42C9: FF         RST     0X38            
42CA: FF         RST     0X38            
42CB: FF         RST     0X38            
42CC: FF         RST     0X38            
42CD: FF         RST     0X38            
42CE: FF         RST     0X38            
42CF: 87         ADD     A,A             
42D0: BF         CP      A               
42D1: BF         CP      A               
42D2: DF         RST     0X18            
42D3: 9F         SBC     A               
42D4: AF         XOR     A               
42D5: CF         RST     0X08            
42D6: 97         SUB     A               
42D7: E7         RST     0X20            
42D8: 0B         DEC     BC              
42D9: 73         LD      (HL),E          
42DA: 0F         RRCA                    
42DB: 73         LD      (HL),E          
42DC: 05         DEC     B               
42DD: F9         LD      SP,HL           
42DE: 07         RLCA                    
42DF: F9         LD      SP,HL           
42E0: FE 03      CP      $03             
42E2: FC         ???                     
42E3: 05         DEC     B               
42E4: F8 0B      LDHL    SP,$0B          
42E6: F0 37      LD      A,($37)         
42E8: C0         RET     NZ              
42E9: CF         RST     0X08            
42EA: 81         ADD     A,C             
42EB: 7E         LD      A,(HL)          
42EC: E6 19      AND     $19             
42EE: F8 07      LDHL    SP,$07          
42F0: 02         LD      (BC),A          
42F1: FC         ???                     
42F2: 03         INC     BC              
42F3: FC         ???                     
42F4: 03         INC     BC              
42F5: FC         ???                     
42F6: 03         INC     BC              
42F7: FC         ???                     
42F8: 07         RLCA                    
42F9: F8 06      LDHL    SP,$06          
42FB: F8 0F      LDHL    SP,$0F          
42FD: F1         POP     AF              
42FE: 7E         LD      A,(HL)          
42FF: 82         ADD     A,D             
4300: FC         ???                     
4301: E0 D8      LDFF00  ($D8),A         
4303: C0         RET     NZ              
4304: F9         LD      SP,HL           
4305: C0         RET     NZ              
4306: B9         CP      C               
4307: 80         ADD     A,B             
4308: B3         OR      E               
4309: 80         ADD     A,B             
430A: F3         DI                      
430B: 80         ADD     A,B             
430C: 7F         LD      A,A             
430D: 00         NOP                     
430E: FF         RST     0X38            
430F: 00         NOP                     
4310: F0 00      LD      A,($00)         
4312: F1         POP     AF              
4313: 00         NOP                     
4314: F3         DI                      
4315: 00         NOP                     
4316: E7         RST     0X20            
4317: 00         NOP                     
4318: 87         ADD     A,A             
4319: 00         NOP                     
431A: 07         RLCA                    
431B: 00         NOP                     
431C: 06 00      LD      B,$00           
431E: 06 00      LD      B,$00           
4320: C3 03 C0   JP      $C003           
4323: 00         NOP                     
4324: C2 02 C6   JP      NZ,$C602        
4327: 06 86      LD      B,$86           
4329: 06 0E      LD      B,$0E           
432B: 0E 1C      LD      C,$1C           
432D: 1C         INC     E               
432E: 18 18      JR      $4348           
4330: 83         ADD     A,E             
4331: 83         ADD     A,E             
4332: 03         INC     BC              
4333: 03         INC     BC              
4334: 07         RLCA                    
4335: 07         RLCA                    
4336: 0F         RRCA                    
4337: 0F         RRCA                    
4338: 0E 0E      LD      C,$0E           
433A: 3C         INC     A               
433B: 3C         INC     A               
433C: 7C         LD      A,H             
433D: 7C         LD      A,H             
433E: 7D         LD      A,L             
433F: 7D         LD      A,L             
4340: 1F         RRA                     
4341: 1F         RRA                     
4342: 3F         CCF                     
4343: 3F         CCF                     
4344: 7F         LD      A,A             
4345: 7F         LD      A,A             
4346: F7         RST     0X30            
4347: F7         RST     0X30            
4348: F7         RST     0X30            
4349: F7         RST     0X30            
434A: EF         RST     0X28            
434B: EF         RST     0X28            
434C: FF         RST     0X38            
434D: FF         RST     0X38            
434E: FF         RST     0X38            
434F: FF         RST     0X38            
4350: BF         CP      A               
4351: BF         CP      A               
4352: DF         RST     0X18            
4353: 9F         SBC     A               
4354: AF         XOR     A               
4355: CF         RST     0X08            
4356: 97         SUB     A               
4357: E7         RST     0X20            
4358: 9F         SBC     A               
4359: E7         RST     0X20            
435A: 0B         DEC     BC              
435B: 73         LD      (HL),E          
435C: 0F         RRCA                    
435D: F3         DI                      
435E: 05         DEC     B               
435F: F9         LD      SP,HL           
4360: FF         RST     0X38            
4361: FF         RST     0X38            
4362: FF         RST     0X38            
4363: FF         RST     0X38            
4364: FF         RST     0X38            
4365: FF         RST     0X38            
4366: FF         RST     0X38            
4367: FF         RST     0X38            
4368: FF         RST     0X38            
4369: FF         RST     0X38            
436A: FF         RST     0X38            
436B: FF         RST     0X38            
436C: FF         RST     0X38            
436D: FF         RST     0X38            
436E: FE FE      CP      $FE             
4370: FF         RST     0X38            
4371: FE FD      CP      $FD             
4373: FC         ???                     
4374: FD         ???                     
4375: FC         ???                     
4376: FB         EI                      
4377: F8 FF      LDHL    SP,$FF          
4379: F8 F7      LDHL    SP,$F7          
437B: 84         ADD     A,H             
437C: 8F         ADC     A,A             
437D: 74         LD      (HL),H          
437E: 3E 38      LD      A,$38           
4380: 07         RLCA                    
4381: F9         LD      SP,HL           
4382: 07         RLCA                    
4383: F9         LD      SP,HL           
4384: 07         RLCA                    
4385: F9         LD      SP,HL           
4386: 06 F8      LD      B,$F8           
4388: 0E F2      LD      C,$F2           
438A: 3E C3      LD      A,$C3           
438C: FC         ???                     
438D: 05         DEC     B               
438E: F8 1B      LDHL    SP,$1B          
4390: 00         NOP                     
4391: 00         NOP                     
4392: 01 01 37   LD      BC,$3701        
4395: 36 3F      LD      (HL),$3F        
4397: 38 3F      JR      C,$43D8         
4399: 30 DF      JR      NC,$437A        
439B: D0         RET     NC              
439C: FF         RST     0X38            
439D: E0 BF      LDFF00  ($BF),A         
439F: A0         AND     B               
43A0: 1F         RRA                     
43A1: 10 FF      STOP    $FF             
43A3: F8 FF      LDHL    SP,$FF          
43A5: 06 FF      LD      B,$FF           
43A7: 01 FF 00   LD      BC,$00FF        
43AA: E0 1F      LDFF00  ($1F),A         
43AC: FC         ???                     
43AD: 03         INC     BC              
43AE: FE 01      CP      $01             
43B0: DF         RST     0X18            
43B1: 1F         RRA                     
43B2: F7         RST     0X30            
43B3: 07         RLCA                    
43B4: F9         LD      SP,HL           
43B5: 01 FF 80   LD      BC,$80FF        
43B8: FF         RST     0X38            
43B9: 00         NOP                     
43BA: FF         RST     0X38            
43BB: 00         NOP                     
43BC: 3F         CCF                     
43BD: C0         RET     NZ              
43BE: 00         NOP                     
43BF: FF         RST     0X38            
43C0: F0 F0      LD      A,($F0)         
43C2: DC C3 E0   CALL    C,$E0C3         
43C5: 9F         SBC     A               
43C6: F8 7F      LDHL    SP,$7F          
43C8: E6 07      AND     $07             
43CA: FD         ???                     
43CB: 01 3E C0   LD      BC,$C03E        
43CE: FF         RST     0X38            
43CF: 10 00      STOP    $00             
43D1: FE 40      CP      $40             
43D3: 3F         CCF                     
43D4: 10 CF      STOP    $CF             
43D6: 08 F7 00   LD      ($00F7),SP      
43D9: FF         RST     0X38            
43DA: 00         NOP                     
43DB: FF         RST     0X38            
43DC: 80         ADD     A,B             
43DD: FF         RST     0X38            
43DE: 40         LD      B,B             
43DF: 7F         LD      A,A             
43E0: 81         ADD     A,C             
43E1: 81         ADD     A,C             
43E2: 6E         LD      L,(HL)          
43E3: E0 13      LDFF00  ($13),A         
43E5: F0 08      LD      A,($08)         
43E7: F8 04      LDHL    SP,$04          
43E9: FC         ???                     
43EA: 06 FA      LD      B,$FA           
43EC: 80         ADD     A,B             
43ED: 7C         LD      A,H             
43EE: 41         LD      B,C             
43EF: BF         CP      A               
43F0: FF         RST     0X38            
43F1: FF         RST     0X38            
43F2: 7F         LD      A,A             
43F3: 7F         LD      A,A             
43F4: 98         SBC     B               
43F5: 18 CC      JR      $43C3           
43F7: 0C         INC     C               
43F8: 64         LD      H,H             
43F9: 04         INC     B               
43FA: 32         LD      (HLD),A         
43FB: 02         LD      (BC),A          
43FC: 10 00      STOP    $00             
43FE: 01 01 F0   LD      BC,$F001        
4401: F0 00      LD      A,($00)         
4403: 00         NOP                     
4404: 0F         RRCA                    
4405: 00         NOP                     
4406: 7F         LD      A,A             
4407: 00         NOP                     
4408: FF         RST     0X38            
4409: 00         NOP                     
440A: 3F         CCF                     
440B: 00         NOP                     
440C: 1C         INC     E               
440D: 00         NOP                     
440E: 00         NOP                     
440F: 00         NOP                     
4410: 1F         RRA                     
4411: 1F         RRA                     
4412: 07         RLCA                    
4413: 07         RLCA                    
4414: E1         POP     HL              
4415: 01 F0 00   LD      BC,$00F0        
4418: F0 00      LD      A,($00)         
441A: 80         ADD     A,B             
441B: 00         NOP                     
441C: 00         NOP                     
441D: 00         NOP                     
441E: 00         NOP                     
441F: 00         NOP                     
4420: FC         ???                     
4421: FB         EI                      
4422: FF         RST     0X38            
4423: F0 FF      LD      A,($FF)         
4425: FF         RST     0X38            
4426: EC         ???                     
4427: E3         ???                     
4428: F0 EF      LD      A,($EF)         
442A: DF         RST     0X18            
442B: C0         RET     NZ              
442C: DF         RST     0X18            
442D: DF         RST     0X18            
442E: 60         LD      H,B             
442F: 5F         LD      E,A             
4430: 1C         INC     E               
4431: E8 C4      ADD     SP,$C4          
4433: 3C         INC     A               
4434: FF         RST     0X38            
4435: E2         LDFF00  (C),A           
4436: 7B         LD      A,E             
4437: 92         SUB     D               
4438: 1F         RRA                     
4439: EC         ???                     
443A: F7         RST     0X30            
443B: 04         INC     B               
443C: 8F         ADC     A,A             
443D: 88         ADC     A,B             
443E: FF         RST     0X38            
443F: 70         LD      (HL),B          
4440: F0 60      LD      A,($60)         
4442: B1         OR      C               
4443: 30 EB      JR      NC,$4430        
4445: 28 77      JR      Z,$44BE         
4447: A4         AND     H               
4448: 6B         LD      L,E             
4449: B2         OR      D               
444A: C7         RST     0X00            
444B: 1B         DEC     DE              
444C: C7         RST     0X00            
444D: 5B         LD      E,E             
444E: 87         ADD     A,A             
444F: B9         CP      C               
4450: FF         RST     0X38            
4451: C3 7F 4C   JP      $4C7F           
4454: 7F         LD      A,A             
4455: 50         LD      D,B             
4456: 7F         LD      A,A             
4457: 50         LD      D,B             
4458: 7F         LD      A,A             
4459: 60         LD      H,B             
445A: 7F         LD      A,A             
445B: 60         LD      H,B             
445C: 7F         LD      A,A             
445D: 60         LD      H,B             
445E: 7F         LD      A,A             
445F: 40         LD      B,B             
4460: F8 87      LDHL    SP,$87          
4462: E1         POP     HL              
4463: 1E C7      LD      E,$C7           
4465: 38 CF      JR      C,$4436         
4467: 30 BF      JR      NC,$4428        
4469: 40         LD      B,B             
446A: BF         CP      A               
446B: 40         LD      B,B             
446C: FC         ???                     
446D: 00         NOP                     
446E: F0 00      LD      A,($00)         
4470: 38 C7      JR      C,$4439         
4472: E1         POP     HL              
4473: 1E C3      LD      E,$C3           
4475: 3C         INC     A               
4476: C7         RST     0X00            
4477: 38 87      JR      C,$4400         
4479: 78         LD      A,B             
447A: 8F         ADC     A,A             
447B: 70         LD      (HL),B          
447C: CF         RST     0X08            
447D: 30 CF      JR      NC,$444E        
447F: 30 FF      JR      NC,$4480        
4481: 0C         INC     C               
4482: BF         CP      A               
4483: 43         LD      B,E             
4484: BF         CP      A               
4485: 40         LD      B,B             
4486: 1F         RRA                     
4487: E0 07      LDFF00  ($07),A         
4489: F8 00      LDHL    SP,$00          
448B: FF         RST     0X38            
448C: 00         NOP                     
448D: FF         RST     0X38            
448E: 80         ADD     A,B             
448F: 7F         LD      A,A             
4490: 3F         CCF                     
4491: 3F         CCF                     
4492: FF         RST     0X38            
4493: C0         RET     NZ              
4494: FF         RST     0X38            
4495: 00         NOP                     
4496: FF         RST     0X38            
4497: 00         NOP                     
4498: F1         POP     AF              
4499: 0E 07      LD      C,$07           
449B: F8 1F      LDHL    SP,$1F          
449D: E0 3F      LDFF00  ($3F),A         
449F: C0         RET     NZ              
44A0: C1         POP     BC              
44A1: 9F         SBC     A               
44A2: E0 6F      LDFF00  ($6F),A         
44A4: F8 1F      LDHL    SP,$1F          
44A6: FC         ???                     
44A7: 07         RLCA                    
44A8: FE 03      CP      $03             
44AA: FE 03      CP      $03             
44AC: FF         RST     0X38            
44AD: 01 EF 0F   LD      BC,$0FEF        
44B0: 00         NOP                     
44B1: 00         NOP                     
44B2: 80         ADD     A,B             
44B3: 80         ADD     A,B             
44B4: 80         ADD     A,B             
44B5: 80         ADD     A,B             
44B6: 40         LD      B,B             
44B7: C0         RET     NZ              
44B8: 40         LD      B,B             
44B9: C0         RET     NZ              
44BA: 20 E0      JR      NZ,$449C        
44BC: 20 E0      JR      NZ,$449E        
44BE: 10 F0      STOP    $F0             
44C0: 00         NOP                     
44C1: 00         NOP                     
44C2: 00         NOP                     
44C3: 00         NOP                     
44C4: 00         NOP                     
44C5: 00         NOP                     
44C6: 00         NOP                     
44C7: 00         NOP                     
44C8: 02         LD      (BC),A          
44C9: 02         LD      (BC),A          
44CA: 02         LD      (BC),A          
44CB: 02         LD      (BC),A          
44CC: 03         INC     BC              
44CD: 03         INC     BC              
44CE: 03         INC     BC              
44CF: 03         INC     BC              
44D0: 00         NOP                     
44D1: 00         NOP                     
44D2: 00         NOP                     
44D3: 00         NOP                     
44D4: 03         INC     BC              
44D5: 03         INC     BC              
44D6: 0F         RRCA                    
44D7: 0F         RRCA                    
44D8: 3F         CCF                     
44D9: 3F         CCF                     
44DA: FF         RST     0X38            
44DB: FF         RST     0X38            
44DC: FF         RST     0X38            
44DD: FF         RST     0X38            
44DE: FF         RST     0X38            
44DF: FF         RST     0X38            
44E0: FF         RST     0X38            
44E1: 00         NOP                     
44E2: FF         RST     0X38            
44E3: 00         NOP                     
44E4: 3E 00      LD      A,$00           
44E6: F8 F8      LDHL    SP,$F8          
44E8: E7         RST     0X20            
44E9: E0 F1      LDFF00  ($F1),A         
44EB: F0 FC      LD      A,($FC)         
44ED: FC         ???                     
44EE: FF         RST     0X38            
44EF: FF         RST     0X38            
44F0: FC         ???                     
44F1: 05         DEC     B               
44F2: F8 1B      LDHL    SP,$1B          
44F4: C0         RET     NZ              
44F5: CF         RST     0X08            
44F6: C2 3D F8   JP      NZ,$F83D        
44F9: 07         RLCA                    
44FA: FD         ???                     
44FB: 02         LD      (BC),A          
44FC: 7F         LD      A,A             
44FD: 00         NOP                     
44FE: 9F         SBC     A               
44FF: 80         ADD     A,B             
4500: A0         AND     B               
4501: 3F         CCF                     
4502: 5F         LD      E,A             
4503: 90         SUB     B               
4504: 28 C8      JR      Z,$44CE         
4506: 3F         CCF                     
4507: CF         RST     0X08            
4508: 17         RLA                     
4509: E6 1D      AND     $1D             
450B: E5         PUSH    HL              
450C: 1E E4      LD      E,$E4           
450E: 1D         DEC     E               
450F: E6 7F      AND     $7F             
4511: A0         AND     B               
4512: BF         CP      A               
4513: 20 46      JR      NZ,$455B        
4515: 40         LD      B,B             
4516: 86         ADD     A,(HL)          
4517: 80         ADD     A,B             
4518: C6 00      ADD     $00             
451A: CE 00      ADC     $00             
451C: FC         ???                     
451D: 80         ADD     A,B             
451E: 78         LD      A,B             
451F: 40         LD      B,B             
4520: FF         RST     0X38            
4521: C0         RET     NZ              
4522: FF         RST     0X38            
4523: C0         RET     NZ              
4524: FF         RST     0X38            
4525: C0         RET     NZ              
4526: FF         RST     0X38            
4527: C0         RET     NZ              
4528: DF         RST     0X18            
4529: C0         RET     NZ              
452A: DF         RST     0X18            
452B: C0         RET     NZ              
452C: 6F         LD      L,A             
452D: 60         LD      H,B             
452E: 2C         INC     L               
452F: 20 E0      JR      NZ,$4511        
4531: 00         NOP                     
4532: C0         RET     NZ              
4533: 00         NOP                     
4534: C1         POP     BC              
4535: 01 81 01   LD      BC,$0181        
4538: 83         ADD     A,E             
4539: 03         INC     BC              
453A: 83         ADD     A,E             
453B: 03         INC     BC              
453C: 07         RLCA                    
453D: 07         RLCA                    
453E: 06 06      LD      B,$06           
4540: EF         RST     0X28            
4541: 10 7F      STOP    $7F             
4543: 00         NOP                     
4544: 7F         LD      A,A             
4545: 00         NOP                     
4546: 7F         LD      A,A             
4547: 00         NOP                     
4548: 3F         CCF                     
4549: 04         INC     B               
454A: BD         CP      L               
454B: 84         ADD     A,H             
454C: 9C         SBC     H               
454D: 84         ADD     A,H             
454E: CE C2      ADC     $C2             
4550: 80         ADD     A,B             
4551: 7F         LD      A,A             
4552: C0         RET     NZ              
4553: 3F         CCF                     
4554: F0 0F      LD      A,($0F)         
4556: FC         ???                     
4557: 03         INC     BC              
4558: FF         RST     0X38            
4559: 00         NOP                     
455A: FF         RST     0X38            
455B: 00         NOP                     
455C: FF         RST     0X38            
455D: 00         NOP                     
455E: 3F         CCF                     
455F: 00         NOP                     
4560: 7F         LD      A,A             
4561: 80         ADD     A,B             
4562: 0F         RRCA                    
4563: F0 1F      LD      A,($1F)         
4565: E0 07      LDFF00  ($07),A         
4567: F8 81      LDHL    SP,$81          
4569: 7E         LD      A,(HL)          
456A: FF         RST     0X38            
456B: 00         NOP                     
456C: FF         RST     0X38            
456D: 00         NOP                     
456E: FF         RST     0X38            
456F: 00         NOP                     
4570: B9         CP      C               
4571: 36 FC      LD      (HL),$FC        
4573: 1E FE      LD      E,$FE           
4575: 07         RLCA                    
4576: FF         RST     0X38            
4577: 03         INC     BC              
4578: FD         ???                     
4579: 1D         DEC     E               
457A: FF         RST     0X38            
457B: 08 FD 06   LD      ($06FD),SP      
457E: FD         ???                     
457F: 05         DEC     B               
4580: 10 F0      STOP    $F0             
4582: 88         ADC     A,B             
4583: 68         LD      L,B             
4584: 08 78 08   LD      ($0878),SP      
4587: 78         LD      A,B             
4588: 08 38 84   LD      ($8438),SP      
458B: 34         INC     (HL)            
458C: CC 14 CC   CALL    Z,$CC14         
458F: D4 07 07   CALL    NC,$0707        
4592: 07         RLCA                    
4593: 07         RLCA                    
4594: 07         RLCA                    
4595: 07         RLCA                    
4596: 0F         RRCA                    
4597: 0F         RRCA                    
4598: 0F         RRCA                    
4599: 0F         RRCA                    
459A: 1F         RRA                     
459B: 1F         RRA                     
459C: 1F         RRA                     
459D: 1F         RRA                     
459E: 3F         CCF                     
459F: 3F         CCF                     
45A0: FF         RST     0X38            
45A1: FF         RST     0X38            
45A2: FF         RST     0X38            
45A3: FF         RST     0X38            
45A4: FF         RST     0X38            
45A5: FF         RST     0X38            
45A6: CF         RST     0X08            
45A7: CF         RST     0X08            
45A8: 8F         ADC     A,A             
45A9: 8F         ADC     A,A             
45AA: 8F         ADC     A,A             
45AB: 8F         ADC     A,A             
45AC: 8F         ADC     A,A             
45AD: 8F         ADC     A,A             
45AE: 5B         LD      E,E             
45AF: 58         LD      E,B             
45B0: FF         RST     0X38            
45B1: FF         RST     0X38            
45B2: FF         RST     0X38            
45B3: FF         RST     0X38            
45B4: FF         RST     0X38            
45B5: FF         RST     0X38            
45B6: FF         RST     0X38            
45B7: FF         RST     0X38            
45B8: E1         POP     HL              
45B9: E1         POP     HL              
45BA: C0         RET     NZ              
45BB: C0         RET     NZ              
45BC: 80         ADD     A,B             
45BD: 80         ADD     A,B             
45BE: 00         NOP                     
45BF: 00         NOP                     
45C0: FF         RST     0X38            
45C1: FF         RST     0X38            
45C2: E7         RST     0X20            
45C3: E0 F1      LDFF00  ($F1),A         
45C5: F0 FC      LD      A,($FC)         
45C7: FC         ???                     
45C8: FF         RST     0X38            
45C9: FF         RST     0X38            
45CA: FF         RST     0X38            
45CB: FF         RST     0X38            
45CC: FF         RST     0X38            
45CD: FF         RST     0X38            
45CE: FF         RST     0X38            
45CF: FF         RST     0X38            
45D0: 00         NOP                     
45D1: 0F         RRCA                    
45D2: E5         PUSH    HL              
45D3: 1A         LD      A,(DE)          
45D4: F8 07      LDHL    SP,$07          
45D6: 7F         LD      A,A             
45D7: 00         NOP                     
45D8: 1E 00      LD      E,$00           
45DA: FE FE      CP      $FE             
45DC: EF         RST     0X28            
45DD: E0 F3      LDFF00  ($F3),A         
45DF: F0 19      LD      A,($19)         
45E1: E2         LDFF00  (C),A           
45E2: 38 CB      JR      C,$45AF         
45E4: F0 17      LD      A,($17)         
45E6: E0 2F      LDFF00  ($2F),A         
45E8: C0         RET     NZ              
45E9: DF         RST     0X18            
45EA: 08 F7 B1   LD      ($B1F7),SP      
45ED: 4E         LD      C,(HL)          
45EE: E7         RST     0X20            
45EF: 18 24      JR      $4615           
45F1: 20 31      JR      NZ,$4624        
45F3: 31 7C 7C   LD      SP,$7C7C        
45F6: F6 F6      OR      $F6             
45F8: F7         RST     0X30            
45F9: F7         RST     0X30            
45FA: EF         RST     0X28            
45FB: EF         RST     0X28            
45FC: FF         RST     0X38            
45FD: FF         RST     0X38            
45FE: FF         RST     0X38            
45FF: FF         RST     0X38            
4600: 05         DEC     B               
4601: 05         DEC     B               
4602: 05         DEC     B               
4603: 05         DEC     B               
4604: 84         ADD     A,H             
4605: 84         ADD     A,H             
4606: 82         ADD     A,D             
4607: 82         ADD     A,D             
4608: C2 C2 F1   JP      NZ,$F1C2        
460B: F1         POP     AF              
460C: EF         RST     0X28            
460D: EF         RST     0X28            
460E: EF         RST     0X28            
460F: E4         ???                     
4610: C3 C1 60   JP      $60C1           
4613: 60         LD      H,B             
4614: 30 30      JR      NC,$4646        
4616: FE 7E      CP      $7E             
4618: FB         EI                      
4619: 4B         LD      C,E             
461A: BF         CP      A               
461B: 28 9F      JR      Z,$45BC         
461D: 68         LD      L,B             
461E: F7         RST     0X30            
461F: 00         NOP                     
4620: 07         RLCA                    
4621: 00         NOP                     
4622: 80         ADD     A,B             
4623: 80         ADD     A,B             
4624: 60         LD      H,B             
4625: 60         LD      H,B             
4626: 3F         CCF                     
4627: 3F         CCF                     
4628: F7         RST     0X30            
4629: F7         RST     0X30            
462A: 3C         INC     A               
462B: 3C         INC     A               
462C: 7E         LD      A,(HL)          
462D: 76         HALT                    
462E: B5         OR      L               
462F: 97         SUB     A               
4630: FF         RST     0X38            
4631: 00         NOP                     
4632: 3E 00      LD      A,$00           
4634: 01 01 E3   LD      BC,$E301        
4637: E2         LDFF00  (C),A           
4638: D6 D5      SUB     $D5             
463A: 6C         LD      L,H             
463B: 4F         LD      C,A             
463C: 34         INC     (HL)            
463D: 26 33      LD      H,$33           
463F: 23         INC     HL              
4640: ED         ???                     
4641: 0C         INC     C               
4642: 68         LD      L,B             
4643: 67         LD      H,A             
4644: C0         RET     NZ              
4645: BE         CP      (HL)            
4646: 2D         DEC     L               
4647: C1         POP     BC              
4648: 1B         DEC     DE              
4649: 86         ADD     A,(HL)          
464A: 11 00 D7   LD      DE,$D700        
464D: C4 0D 0D   CALL    NZ,$0D0D        
4650: DC 44 9F   CALL    C,$9F44         
4653: 83         ADD     A,E             
4654: DF         RST     0X18            
4655: 83         ADD     A,E             
4656: EF         RST     0X28            
4657: 03         INC     BC              
4658: EF         RST     0X28            
4659: 03         INC     BC              
465A: EB         ???                     
465B: 03         INC     BC              
465C: EF         RST     0X28            
465D: 07         RLCA                    
465E: FF         RST     0X38            
465F: FF         RST     0X38            
4660: FF         RST     0X38            
4661: FF         RST     0X38            
4662: CF         RST     0X08            
4663: CF         RST     0X08            
4664: C7         RST     0X00            
4665: C7         RST     0X00            
4666: C3 C3 E1   JP      $E1C3           
4669: E1         POP     HL              
466A: 60         LD      H,B             
466B: 60         LD      H,B             
466C: 00         NOP                     
466D: 00         NOP                     
466E: 00         NOP                     
466F: 00         NOP                     
4670: E0 E0      LDFF00  ($E0),A         
4672: F8 F8      LDHL    SP,$F8          
4674: FF         RST     0X38            
4675: FF         RST     0X38            
4676: FB         EI                      
4677: F9         LD      SP,HL           
4678: FB         EI                      
4679: F8 FD      LDHL    SP,$FD          
467B: FC         ???                     
467C: 3E 3E      LD      A,$3E           
467E: 0F         RRCA                    
467F: 0F         RRCA                    
4680: FC         ???                     
4681: FC         ???                     
4682: FF         RST     0X38            
4683: FF         RST     0X38            
4684: FD         ???                     
4685: FD         ???                     
4686: FB         EI                      
4687: F8 FB      LDHL    SP,$FB          
4689: F8 F7      LDHL    SP,$F7          
468B: F0 F7      LD      A,($F7)         
468D: F0 EE      LD      A,($EE)         
468F: E0 7F      LDFF00  ($7F),A         
4691: 03         INC     BC              
4692: FC         ???                     
4693: FD         ???                     
4694: 9F         SBC     A               
4695: 80         ADD     A,B             
4696: E7         RST     0X20            
4697: 60         LD      H,B             
4698: 99         SBC     C               
4699: 18 FF      JR      $469A           
469B: 0F         RRCA                    
469C: 72         LD      (HL),D          
469D: 02         LD      (BC),A          
469E: 71         LD      (HL),C          
469F: 01 03 7D   LD      BC,$7D03        
46A2: 27         DAA                     
46A3: D9         RETI                    
46A4: CF         RST     0X08            
46A5: 31 FE 02   LD      SP,$02FE        
46A8: F4         ???                     
46A9: 05         DEC     B               
46AA: F9         LD      SP,HL           
46AB: FE 7E      CP      $7E             
46AD: 01 9F 80   LD      BC,$809F        
46B0: A0         AND     B               
46B1: 20 50      JR      NZ,$4703        
46B3: 90         SUB     B               
46B4: 39         ADD     HL,SP           
46B5: D9         RETI                    
46B6: 3D         DEC     A               
46B7: CD 1B EB   CALL    $EB1B           
46BA: 1D         DEC     E               
46BB: E9         JP      (HL)            
46BC: 3A         LD      A,(HLD)         
46BD: CC F1 16   CALL    Z,$16F1         
46C0: EF         RST     0X28            
46C1: E5         PUSH    HL              
46C2: D7         RST     0X10            
46C3: C6 DE      ADD     $DE             
46C5: CB DE      SET     1,E             
46C7: CB DF      SET     1,E             
46C9: C9         RET                     
46CA: DC CB A0   CALL    C,$A0CB         
46CD: 83         ADD     A,E             
46CE: A4         AND     H               
46CF: 87         ADD     A,A             
46D0: CF         RST     0X08            
46D1: C0         RET     NZ              
46D2: 0F         RRCA                    
46D3: F0 07      LD      A,($07)         
46D5: F8 00      LDHL    SP,$00          
46D7: FF         RST     0X38            
46D8: E0 1F      LDFF00  ($1F),A         
46DA: E0 EF      LDFF00  ($EF),A         
46DC: 38 C7      JR      C,$46A5         
46DE: 00         NOP                     
46DF: FE B8      CP      $B8             
46E1: 1E E1      LD      E,$E1           
46E3: 1C         INC     E               
46E4: F3         DI                      
46E5: 00         NOP                     
46E6: 1F         RRA                     
46E7: E0 07      LDFF00  ($07),A         
46E9: F8 03      LDHL    SP,$03          
46EB: FC         ???                     
46EC: 03         INC     BC              
46ED: FC         ???                     
46EE: C3 FC 39   JP      $39FC           
46F1: 21 39 21   LD      HL,$2139        
46F4: 39         ADD     HL,SP           
46F5: 21 BB 22   LD      HL,$22BB        
46F8: B6         OR      (HL)            
46F9: 25         DEC     H               
46FA: EC         ???                     
46FB: 6B         LD      L,E             
46FC: D3         ???                     
46FD: 53         LD      D,E             
46FE: E8 67      ADD     SP,$67          
4700: 9B         SBC     E               
4701: 98         SBC     B               
4702: F8 E7      LDHL    SP,$E7          
4704: 80         ADD     A,B             
4705: 87         ADD     A,A             
4706: 8C         ADC     A,H             
4707: 7F         LD      A,A             
4708: 07         RLCA                    
4709: FA 1F E2   LD      A,($E21F)       
470C: FF         RST     0X38            
470D: 87         ADD     A,A             
470E: FF         RST     0X38            
470F: DF         RST     0X18            
4710: BD         CP      L               
4711: 01 22 FC   LD      BC,$FC22        
4714: 31 DE 71   LD      SP,$71DE        
4717: 9E         SBC     (HL)            
4718: FF         RST     0X38            
4719: 10 FF      STOP    $FF             
471B: FE FF      CP      $FF             
471D: FF         RST     0X38            
471E: FF         RST     0X38            
471F: FF         RST     0X38            
4720: FF         RST     0X38            
4721: FF         RST     0X38            
4722: DF         RST     0X18            
4723: 1F         RRA                     
4724: 37         SCF                     
4725: 47         LD      B,A             
4726: 9B         SBC     E               
4727: E1         POP     HL              
4728: 89         ADC     A,C             
4729: F2         ???                     
472A: CC B7 EC   CALL    Z,$ECB7         
472D: D7         RST     0X10            
472E: F8 EF      LDHL    SP,$EF          
4730: FF         RST     0X38            
4731: FF         RST     0X38            
4732: FF         RST     0X38            
4733: FF         RST     0X38            
4734: FF         RST     0X38            
4735: FF         RST     0X38            
4736: FF         RST     0X38            
4737: FF         RST     0X38            
4738: FF         RST     0X38            
4739: FF         RST     0X38            
473A: 7F         LD      A,A             
473B: 7F         LD      A,A             
473C: BF         CP      A               
473D: 3F         CCF                     
473E: 9F         SBC     A               
473F: 1F         RRA                     
4740: F7         RST     0X30            
4741: 70         LD      (HL),B          
4742: DF         RST     0X18            
4743: 5F         LD      E,A             
4744: CD 4C 82   CALL    $824C           
4747: 02         LD      (BC),A          
4748: 87         ADD     A,A             
4749: 07         RLCA                    
474A: 0E 0E      LD      C,$0E           
474C: 1C         INC     E               
474D: 1C         INC     E               
474E: 18 18      JR      $4768           
4750: E1         POP     HL              
4751: 6E         LD      L,(HL)          
4752: A0         AND     B               
4753: 9F         SBC     A               
4754: F9         LD      SP,HL           
4755: 06 7F      LD      B,$7F           
4757: 00         NOP                     
4758: DD         ???                     
4759: C1         POP     BC              
475A: 7D         LD      A,L             
475B: 7C         LD      A,H             
475C: 77         LD      (HL),A          
475D: 70         LD      (HL),B          
475E: 7D         LD      A,L             
475F: 6C         LD      L,H             
4760: F0 77      LD      A,($77)         
4762: DC 5B EE   CALL    C,$EE5B         
4765: 4D         LD      C,L             
4766: 97         SUB     A               
4767: A6         AND     (HL)            
4768: 0A         LD      A,(BC)          
4769: 72         LD      (HL),D          
476A: 4B         LD      C,E             
476B: B3         OR      E               
476C: 9B         SBC     E               
476D: 63         LD      H,E             
476E: F7         RST     0X30            
476F: 07         RLCA                    
4770: 7F         LD      A,A             
4771: BF         CP      A               
4772: 0F         RRCA                    
4773: F7         RST     0X30            
4774: 03         INC     BC              
4775: FD         ???                     
4776: 81         ADD     A,C             
4777: 7E         LD      A,(HL)          
4778: C0         RET     NZ              
4779: 3F         CCF                     
477A: 60         LD      H,B             
477B: 1F         RRA                     
477C: 60         LD      H,B             
477D: 1F         RRA                     
477E: 60         LD      H,B             
477F: 1F         RRA                     
4780: A2         AND     D               
4781: 83         ADD     A,E             
4782: A0         AND     B               
4783: 80         ADD     A,B             
4784: D1         POP     DE              
4785: C1         POP     BC              
4786: D0         RET     NC              
4787: C0         RET     NZ              
4788: C4 40 EA   CALL    NZ,$EA40        
478B: 68         LD      L,B             
478C: 7C         LD      A,H             
478D: FC         ???                     
478E: 7E         LD      A,(HL)          
478F: BE         CP      (HL)            
4790: 20 FC      JR      NZ,$478E        
4792: 03         INC     BC              
4793: C0         RET     NZ              
4794: 1C         INC     E               
4795: E3         ???                     
4796: 80         ADD     A,B             
4797: F0 C6      LD      A,($C6)         
4799: B9         CP      C               
479A: 60         LD      H,B             
479B: 5F         LD      E,A             
479C: DF         RST     0X18            
479D: C0         RET     NZ              
479E: EF         RST     0X28            
479F: E0 E3      LDFF00  ($E3),A         
47A1: 3C         INC     A               
47A2: 07         RLCA                    
47A3: F8 07      LDHL    SP,$07          
47A5: F8 0F      LDHL    SP,$0F          
47A7: F1         POP     AF              
47A8: 1F         RRA                     
47A9: E3         ???                     
47AA: 7F         LD      A,A             
47AB: 8F         ADC     A,A             
47AC: F9         LD      SP,HL           
47AD: 39         ADD     HL,SP           
47AE: E1         POP     HL              
47AF: E1         POP     HL              
47B0: F1         POP     AF              
47B1: 6E         LD      L,(HL)          
47B2: E1         POP     HL              
47B3: 5E         LD      E,(HL)          
47B4: E3         ???                     
47B5: DC CF BF   CALL    C,$BFCF         
47B8: D7         RST     0X10            
47B9: 99         SBC     C               
47BA: 87         ADD     A,A             
47BB: BB         CP      E               
47BC: 0E 72      LD      C,$72           
47BE: 8E         ADC     A,(HL)          
47BF: 72         LD      (HL),D          
47C0: FF         RST     0X38            
47C1: 7F         LD      A,A             
47C2: F8 78      LDHL    SP,$78          
47C4: E1         POP     HL              
47C5: E1         POP     HL              
47C6: 82         ADD     A,D             
47C7: 82         ADD     A,D             
47C8: 05         DEC     B               
47C9: 04         INC     B               
47CA: 07         RLCA                    
47CB: 04         INC     B               
47CC: 0F         RRCA                    
47CD: 08 1F 10   LD      ($101F),SP      
47D0: F1         POP     AF              
47D1: F1         POP     AF              
47D2: 80         ADD     A,B             
47D3: 80         ADD     A,B             
47D4: 18 00      JR      $47D6           
47D6: 7E         LD      A,(HL)          
47D7: 00         NOP                     
47D8: FE 00      CP      $00             
47DA: FF         RST     0X38            
47DB: 00         NOP                     
47DC: FF         RST     0X38            
47DD: 00         NOP                     
47DE: FF         RST     0X38            
47DF: 00         NOP                     
47E0: FD         ???                     
47E1: FA 3F 3C   LD      A,($3C3F)       
47E4: 1F         RRA                     
47E5: 1E 0F      LD      E,$0F           
47E7: 0F         RRCA                    
47E8: 0F         RRCA                    
47E9: 0F         RRCA                    
47EA: 07         RLCA                    
47EB: 07         RLCA                    
47EC: 07         RLCA                    
47ED: 07         RLCA                    
47EE: 07         RLCA                    
47EF: 07         RLCA                    
47F0: BF         CP      A               
47F1: 1F         RRA                     
47F2: BF         CP      A               
47F3: DF         RST     0X18            
47F4: AF         XOR     A               
47F5: CF         RST     0X08            
47F6: 3F         CCF                     
47F7: CF         RST     0X08            
47F8: 6F         LD      L,A             
47F9: 8F         ADC     A,A             
47FA: FF         RST     0X38            
47FB: 1F         RRA                     
47FC: FF         RST     0X38            
47FD: 2F         CPL                     
47FE: DF         RST     0X18            
47FF: EF         RST     0X28            
4800: B6         OR      (HL)            
4801: 86         ADD     A,(HL)          
4802: A0         AND     B               
4803: 80         ADD     A,B             
4804: E1         POP     HL              
4805: 9E         SBC     (HL)            
4806: C0         RET     NZ              
4807: BF         CP      A               
4808: B0         OR      B               
4809: 8F         ADC     A,A             
480A: DF         RST     0X18            
480B: C0         RET     NZ              
480C: F7         RST     0X30            
480D: F0 FC      LD      A,($FC)         
480F: FC         ???                     
4810: 3D         DEC     A               
4811: 3C         INC     A               
4812: F7         RST     0X30            
4813: F0 FC      LD      A,($FC)         
4815: 03         INC     BC              
4816: 00         NOP                     
4817: FF         RST     0X38            
4818: 00         NOP                     
4819: FF         RST     0X38            
481A: 00         NOP                     
481B: FF         RST     0X38            
481C: 80         ADD     A,B             
481D: 7F         LD      A,A             
481E: E0 1F      LDFF00  ($1F),A         
4820: C0         RET     NZ              
4821: 3F         CCF                     
4822: 80         ADD     A,B             
4823: 7F         LD      A,A             
4824: 00         NOP                     
4825: FF         RST     0X38            
4826: 01 FE 01   LD      BC,$01FE        
4829: FE 03      CP      $03             
482B: FC         ???                     
482C: 0F         RRCA                    
482D: F0 7F      LD      A,($7F)         
482F: 80         ADD     A,B             
4830: FF         RST     0X38            
4831: 3F         CCF                     
4832: FB         EI                      
4833: 10 F0      STOP    $F0             
4835: 1D         DEC     E               
4836: F9         LD      SP,HL           
4837: 0C         INC     C               
4838: F8 0E      LDHL    SP,$0E          
483A: FE 04      CP      $04             
483C: FE 06      CP      $06             
483E: FF         RST     0X38            
483F: 03         INC     BC              
4840: EF         RST     0X28            
4841: EF         RST     0X28            
4842: F0 F0      LD      A,($F0)         
4844: 50         LD      D,B             
4845: 90         SUB     B               
4846: 24         INC     H               
4847: C4 16 E2   CALL    NZ,$E216        
484A: 93         SUB     E               
484B: 65         LD      H,L             
484C: 91         SUB     C               
484D: 66         LD      H,(HL)          
484E: F9         LD      SP,HL           
484F: 0E DB      LD      C,$DB           
4851: C3 FA 82   JP      $82FA           
4854: 7B         LD      A,E             
4855: 42         LD      B,D             
4856: 77         LD      (HL),A          
4857: 46         LD      B,(HL)          
4858: 3E 2E      LD      A,$2E           
485A: 37         SCF                     
485B: 36 87      LD      (HL),$87        
485D: 85         ADD     A,L             
485E: CE 4E      ADC     $4E             
4860: 9C         SBC     H               
4861: 64         LD      H,H             
4862: 7C         LD      A,H             
4863: 9C         SBC     H               
4864: AD         XOR     L               
4865: 35         DEC     (HL)            
4866: 1E 26      LD      E,$26           
4868: 1D         DEC     E               
4869: E4         ???                     
486A: 3B         DEC     SP              
486B: C8         RET     Z               
486C: FF         RST     0X38            
486D: F8 3B      LDHL    SP,$3B          
486F: 03         INC     BC              
4870: 7F         LD      A,A             
4871: 60         LD      H,B             
4872: BF         CP      A               
4873: 80         ADD     A,B             
4874: 7F         LD      A,A             
4875: 00         NOP                     
4876: FF         RST     0X38            
4877: 00         NOP                     
4878: FF         RST     0X38            
4879: 00         NOP                     
487A: FF         RST     0X38            
487B: 00         NOP                     
487C: FF         RST     0X38            
487D: 00         NOP                     
487E: 9F         SBC     A               
487F: 80         ADD     A,B             
4880: FF         RST     0X38            
4881: 00         NOP                     
4882: FF         RST     0X38            
4883: 00         NOP                     
4884: FF         RST     0X38            
4885: 00         NOP                     
4886: FE 00      CP      $00             
4888: FE 00      CP      $00             
488A: F4         ???                     
488B: 00         NOP                     
488C: F0 00      LD      A,($00)         
488E: E1         POP     HL              
488F: 01 07 07   LD      BC,$0707        
4892: 06 06      LD      B,$06           
4894: 0F         RRCA                    
4895: 0E 0F      LD      C,$0F           
4897: 0F         RRCA                    
4898: 1D         DEC     E               
4899: 1C         INC     E               
489A: 3E 3C      LD      A,$3C           
489C: 78         LD      A,B             
489D: 78         LD      A,B             
489E: F3         DI                      
489F: F3         DI                      
48A0: AF         XOR     A               
48A1: 4F         LD      C,A             
48A2: 3F         CCF                     
48A3: DF         RST     0X18            
48A4: DF         RST     0X18            
48A5: 1F         RRA                     
48A6: 1F         RRA                     
48A7: 1F         RRA                     
48A8: 3F         CCF                     
48A9: 3F         CCF                     
48AA: 7F         LD      A,A             
48AB: 7F         LD      A,A             
48AC: FF         RST     0X38            
48AD: FF         RST     0X38            
48AE: FF         RST     0X38            
48AF: FF         RST     0X38            
48B0: F8 F8      LDHL    SP,$F8          
48B2: FC         ???                     
48B3: FC         ???                     
48B4: 7F         LD      A,A             
48B5: 7F         LD      A,A             
48B6: 7F         LD      A,A             
48B7: 7F         LD      A,A             
48B8: 7F         LD      A,A             
48B9: 7F         LD      A,A             
48BA: FF         RST     0X38            
48BB: FF         RST     0X38            
48BC: FF         RST     0X38            
48BD: FF         RST     0X38            
48BE: FF         RST     0X38            
48BF: FF         RST     0X38            
48C0: FF         RST     0X38            
48C1: 00         NOP                     
48C2: 7F         LD      A,A             
48C3: 00         NOP                     
48C4: 7F         LD      A,A             
48C5: 00         NOP                     
48C6: BF         CP      A               
48C7: 80         ADD     A,B             
48C8: DF         RST     0X18            
48C9: C0         RET     NZ              
48CA: E7         RST     0X20            
48CB: E0 FC      LDFF00  ($FC),A         
48CD: FC         ???                     
48CE: FF         RST     0X38            
48CF: FF         RST     0X38            
48D0: FF         RST     0X38            
48D1: 00         NOP                     
48D2: FF         RST     0X38            
48D3: 00         NOP                     
48D4: FF         RST     0X38            
48D5: 00         NOP                     
48D6: FF         RST     0X38            
48D7: 00         NOP                     
48D8: FF         RST     0X38            
48D9: 00         NOP                     
48DA: FF         RST     0X38            
48DB: 00         NOP                     
48DC: 3F         CCF                     
48DD: 00         NOP                     
48DE: E1         POP     HL              
48DF: E0 FF      LDFF00  ($FF),A         
48E1: 03         INC     BC              
48E2: FF         RST     0X38            
48E3: 01 FF 01   LD      BC,$01FF        
48E6: FF         RST     0X38            
48E7: 01 FF 01   LD      BC,$01FF        
48EA: FF         RST     0X38            
48EB: 02         LD      (BC),A          
48EC: FF         RST     0X38            
48ED: 02         LD      (BC),A          
48EE: FF         RST     0X38            
48EF: 04         INC     B               
48F0: F0 FF      LD      A,($FF)         
48F2: 38 27      JR      C,$491B         
48F4: DD         ???                     
48F5: 12         LD      (DE),A          
48F6: EF         RST     0X28            
48F7: 08 F7 07   LD      ($07F7),SP      
48FA: F5         PUSH    AF              
48FB: 04         INC     B               
48FC: F3         DI                      
48FD: 02         LD      (BC),A          
48FE: FA 02 A4   LD      A,($A402)       
4901: 23         INC     HL              
4902: B8         CP      B               
4903: 17         RLA                     
4904: BF         CP      A               
4905: 1E 19      LD      E,$19           
4907: 69         LD      L,C             
4908: 18 E8      JR      $48F2           
490A: 15         DEC     D               
490B: E4         ???                     
490C: 95         SUB     L               
490D: 64         LD      H,H             
490E: F4         ???                     
490F: 04         INC     B               
4910: 72         LD      (HL),D          
4911: AC         XOR     H               
4912: 28 C7      JR      Z,$48DB         
4914: 30 C7      JR      NC,$48DD        
4916: FC         ???                     
4917: 8B         ADC     A,E             
4918: C7         RST     0X00            
4919: C0         RET     NZ              
491A: 7C         LD      A,H             
491B: 7C         LD      A,H             
491C: E3         ???                     
491D: 23         INC     HL              
491E: F9         LD      SP,HL           
491F: 01 67 60   LD      BC,$6067        
4922: D9         RETI                    
4923: 98         SBC     B               
4924: 94         SUB     H               
4925: 24         INC     H               
4926: 9E         SBC     (HL)            
4927: 26 89      LD      H,$89           
4929: 31 49 72   LD      SP,$7249        
492C: 09         ADD     HL,BC           
492D: 32         LD      (HLD),A         
492E: B8         CP      B               
492F: 83         ADD     A,E             
4930: E3         ???                     
4931: 03         INC     BC              
4932: C7         RST     0X00            
4933: 07         RLCA                    
4934: 0B         DEC     BC              
4935: 0B         DEC     BC              
4936: 0B         DEC     BC              
4937: 0B         DEC     BC              
4938: 13         INC     DE              
4939: 13         INC     DE              
493A: A3         AND     E               
493B: A3         AND     E               
493C: 67         LD      H,A             
493D: 67         LD      H,A             
493E: E7         RST     0X20            
493F: 67         LD      H,A             
4940: 0F         RRCA                    
4941: 08 7F 70   LD      ($707F),SP      
4944: FF         RST     0X38            
4945: 00         NOP                     
4946: 7C         LD      A,H             
4947: 00         NOP                     
4948: 80         ADD     A,B             
4949: 80         ADD     A,B             
494A: F8 F8      LDHL    SP,$F8          
494C: FE FE      CP      $FE             
494E: FF         RST     0X38            
494F: FF         RST     0X38            
4950: F9         LD      SP,HL           
4951: 01 FD 01   LD      BC,$01FD        
4954: 7D         LD      A,L             
4955: 01 FC 00   LD      BC,$00FC        
4958: FC         ???                     
4959: 00         NOP                     
495A: 78         LD      A,B             
495B: 00         NOP                     
495C: 00         NOP                     
495D: 00         NOP                     
495E: 80         ADD     A,B             
495F: 80         ADD     A,B             
4960: 7A         LD      A,D             
4961: 12         LD      (DE),A          
4962: 46         LD      B,(HL)          
4963: 5A         LD      E,D             
4964: C6 3A      ADD     $3A             
4966: C6 BA      ADD     $BA             
4968: EE 92      XOR     $92             
496A: FA 82 B7   LD      A,($B782)       
496D: 85         ADD     A,L             
496E: EB         ???                     
496F: E5         PUSH    HL              
4970: FC         ???                     
4971: 00         NOP                     
4972: FE 00      CP      $00             
4974: FE 00      CP      $00             
4976: 7E         LD      A,(HL)          
4977: 00         NOP                     
4978: 7C         LD      A,H             
4979: 00         NOP                     
497A: 7C         LD      A,H             
497B: 00         NOP                     
497C: 38 00      JR      C,$497E         
497E: 00         NOP                     
497F: 00         NOP                     
4980: F8 CF      LDHL    SP,$CF          
4982: 68         LD      L,B             
4983: 67         LD      H,A             
4984: 3D         DEC     A               
4985: 32         LD      (HLD),A         
4986: 1E 18      LD      E,$18           
4988: 1A         LD      A,(DE)          
4989: 1B         DEC     DE              
498A: 0F         RRCA                    
498B: 0C         INC     C               
498C: 1D         DEC     E               
498D: 1C         INC     E               
498E: 3F         CCF                     
498F: 3E A3      LD      A,$A3           
4991: 23         INC     HL              
4992: 03         INC     BC              
4993: 43         LD      B,E             
4994: 33         INC     SP              
4995: 53         LD      D,E             
4996: 33         INC     SP              
4997: D3         ???                     
4998: 37         SCF                     
4999: D7         RST     0X10            
499A: 5F         LD      E,A             
499B: 9F         SBC     A               
499C: DF         RST     0X18            
499D: 0F         RRCA                    
499E: 9F         SBC     A               
499F: 0F         RRCA                    
49A0: E3         ???                     
49A1: 9D         SBC     L               
49A2: E0 9C      LDFF00  ($9C),A         
49A4: FE 82      CP      $82             
49A6: BA         CP      D               
49A7: 82         ADD     A,D             
49A8: 07         RLCA                    
49A9: 83         ADD     A,E             
49AA: 0F         RRCA                    
49AB: F7         RST     0X30            
49AC: F7         RST     0X30            
49AD: 07         RLCA                    
49AE: 1F         RRA                     
49AF: 1F         RRA                     
49B0: 00         NOP                     
49B1: 00         NOP                     
49B2: 01 01 07   LD      BC,$0701        
49B5: 07         RLCA                    
49B6: 3F         CCF                     
49B7: 3F         CCF                     
49B8: FF         RST     0X38            
49B9: FF         RST     0X38            
49BA: FE FE      CP      $FE             
49BC: FC         ???                     
49BD: FC         ???                     
49BE: F0 F0      LD      A,($F0)         
49C0: 7F         LD      A,A             
49C1: 7F         LD      A,A             
49C2: FE F3      CP      $F3             
49C4: E9         JP      (HL)            
49C5: E0 A4      LDFF00  ($A4),A         
49C7: A2         AND     D               
49C8: 17         RLA                     
49C9: 10 18      STOP    $18             
49CB: 18 0F      JR      $49DC           
49CD: 0F         RRCA                    
49CE: 07         RLCA                    
49CF: 07         RLCA                    
49D0: AF         XOR     A               
49D1: 8F         ADC     A,A             
49D2: 2F         CPL                     
49D3: CF         RST     0X08            
49D4: 5F         LD      E,A             
49D5: 9F         SBC     A               
49D6: 1F         RRA                     
49D7: 1F         RRA                     
49D8: 3F         CCF                     
49D9: 3F         CCF                     
49DA: FF         RST     0X38            
49DB: FF         RST     0X38            
49DC: FF         RST     0X38            
49DD: FF         RST     0X38            
49DE: FF         RST     0X38            
49DF: FF         RST     0X38            
49E0: C3 C1 60   JP      $60C1           
49E3: 60         LD      H,B             
49E4: 30 30      JR      NC,$4A16        
49E6: 1E 1E      LD      E,$1E           
49E8: 8B         ADC     A,E             
49E9: 8B         ADC     A,E             
49EA: 6F         LD      L,A             
49EB: 69         LD      L,C             
49EC: 6F         LD      L,A             
49ED: 09         ADD     HL,BC           
49EE: F7         RST     0X30            
49EF: 00         NOP                     
49F0: 07         RLCA                    
49F1: 00         NOP                     
49F2: 80         ADD     A,B             
49F3: 80         ADD     A,B             
49F4: 60         LD      H,B             
49F5: 60         LD      H,B             
49F6: 3F         CCF                     
49F7: 3F         CCF                     
49F8: FF         RST     0X38            
49F9: FF         RST     0X38            
49FA: 62         LD      H,D             
49FB: 62         LD      H,D             
49FC: 81         ADD     A,C             
49FD: 81         ADD     A,C             
49FE: 00         NOP                     
49FF: 00         NOP                     
4A00: CF         RST     0X08            
4A01: C0         RET     NZ              
4A02: 0F         RRCA                    
4A03: F0 03      LD      A,($03)         
4A05: FC         ???                     
4A06: 00         NOP                     
4A07: FF         RST     0X38            
4A08: E0 1F      LDFF00  ($1F),A         
4A0A: E0 EF      LDFF00  ($EF),A         
4A0C: 38 C7      JR      C,$49D5         
4A0E: 44         LD      B,H             
4A0F: B8         CP      B               
4A10: 7C         LD      A,H             
4A11: 7C         LD      A,H             
4A12: FE 02      CP      $02             
4A14: FF         RST     0X38            
4A15: 00         NOP                     
4A16: 7F         LD      A,A             
4A17: 80         ADD     A,B             
4A18: 0F         RRCA                    
4A19: F0 07      LD      A,($07)         
4A1B: F8 03      LDHL    SP,$03          
4A1D: FC         ???                     
4A1E: C3 FC 44   JP      $44FC           
4A21: C3 01 CE   JP      $CE01           
4A24: 1F         RRA                     
4A25: FF         RST     0X38            
4A26: 8F         ADC     A,A             
4A27: EF         RST     0X28            
4A28: CF         RST     0X08            
4A29: BF         CP      A               
4A2A: 00         NOP                     
4A2B: 3F         CCF                     
4A2C: E0 F8      LDFF00  ($F8),A         
4A2E: EF         RST     0X28            
4A2F: E0 63      LDFF00  ($63),A         
4A31: FC         ???                     
4A32: E3         ???                     
4A33: FC         ???                     
4A34: E6 F8      AND     $F8             
4A36: C7         RST     0X00            
4A37: D9         RETI                    
4A38: 0F         RRCA                    
4A39: 33         INC     SP              
4A3A: 1F         RRA                     
4A3B: E7         RST     0X20            
4A3C: 39         ADD     HL,SP           
4A3D: C9         RET                     
4A3E: D1         POP     DE              
4A3F: 11 F7 F0   LD      DE,$F0F7        
4A42: FF         RST     0X38            
4A43: FF         RST     0X38            
4A44: 50         LD      D,B             
4A45: 90         SUB     B               
4A46: 24         INC     H               
4A47: C4 16 E2   CALL    NZ,$E216        
4A4A: 93         SUB     E               
4A4B: 65         LD      H,L             
4A4C: 91         SUB     C               
4A4D: 66         LD      H,(HL)          
4A4E: F9         LD      SP,HL           
4A4F: 0E 23      LD      C,$23           
4A51: 23         INC     HL              
4A52: 8A         ADC     A,D             
4A53: 82         ADD     A,D             
4A54: 7B         LD      A,E             
4A55: 42         LD      B,D             
4A56: 77         LD      (HL),A          
4A57: 46         LD      B,(HL)          
4A58: 3E 2E      LD      A,$2E           
4A5A: 37         SCF                     
4A5B: 36 87      LD      (HL),$87        
4A5D: 85         ADD     A,L             
4A5E: CE 4E      ADC     $4E             
4A60: 00         NOP                     
4A61: 00         NOP                     
4A62: 00         NOP                     
4A63: 00         NOP                     
4A64: 44         LD      B,H             
4A65: 44         LD      B,H             
4A66: 28 28      JR      Z,$4A90         
4A68: 10 10      STOP    $10             
4A6A: 28 28      JR      Z,$4A94         
4A6C: 44         LD      B,H             
4A6D: 44         LD      B,H             
4A6E: 00         NOP                     
4A6F: 00         NOP                     
4A70: FF         RST     0X38            
4A71: FF         RST     0X38            
4A72: FF         RST     0X38            
4A73: FF         RST     0X38            
4A74: FF         RST     0X38            
4A75: FF         RST     0X38            
4A76: FD         ???                     
4A77: FC         ???                     
4A78: FA F9 FF   LD      A,($FFF9)       
4A7B: F9         LD      SP,HL           
4A7C: F5         PUSH    AF              
4A7D: F3         DI                      
4A7E: FD         ???                     
4A7F: F2         ???                     
4A80: FF         RST     0X38            
4A81: FF         RST     0X38            
4A82: C1         POP     BC              
4A83: C1         POP     BC              
4A84: 83         ADD     A,E             
4A85: 7C         LD      A,H             
4A86: 33         INC     SP              
4A87: CC E7 F9   CALL    Z,$F9E7         
4A8A: 26 FB      LD      H,$FB           
4A8C: 2E F3      LD      L,$F3           
4A8E: CC F0 B0   CALL    Z,$B0F0         
4A91: 80         ADD     A,B             
4A92: F1         POP     AF              
4A93: F0 1E      LD      A,($1E)         
4A95: 1E 93      LD      E,$93           
4A97: 63         LD      H,E             
4A98: FC         ???                     
4A99: C0         RET     NZ              
4A9A: 38 A0      JR      C,$4A3C         
4A9C: 39         ADD     HL,SP           
4A9D: A0         AND     B               
4A9E: 31 20 C3   LD      SP,$C320        
4AA1: 03         INC     BC              
4AA2: C0         RET     NZ              
4AA3: 00         NOP                     
4AA4: 42         LD      B,D             
4AA5: 02         LD      (BC),A          
4AA6: C6 C6      ADD     $C6             
4AA8: 7E         LD      A,(HL)          
4AA9: 7E         LD      A,(HL)          
4AAA: 1E 1E      LD      E,$1E           
4AAC: 87         ADD     A,A             
4AAD: 07         RLCA                    
4AAE: 03         INC     BC              
4AAF: 03         INC     BC              
4AB0: 00         NOP                     
4AB1: 00         NOP                     
4AB2: 00         NOP                     
4AB3: 00         NOP                     
4AB4: 00         NOP                     
4AB5: 00         NOP                     
4AB6: 00         NOP                     
4AB7: 00         NOP                     
4AB8: 00         NOP                     
4AB9: 00         NOP                     
4ABA: 00         NOP                     
4ABB: 07         RLCA                    
4ABC: 00         NOP                     
4ABD: 1F         RRA                     
4ABE: 00         NOP                     
4ABF: 3E 00      LD      A,$00           
4AC1: 00         NOP                     
4AC2: 00         NOP                     
4AC3: 00         NOP                     
4AC4: 00         NOP                     
4AC5: 00         NOP                     
4AC6: 00         NOP                     
4AC7: 00         NOP                     
4AC8: 00         NOP                     
4AC9: 00         NOP                     
4ACA: 20 80      JR      NZ,$4A4C        
4ACC: 18 C0      JR      $4A8E           
4ACE: 0C         INC     C               
4ACF: 20 00      JR      NZ,$4AD1        
4AD1: 00         NOP                     
4AD2: 00         NOP                     
4AD3: 00         NOP                     
4AD4: 44         LD      B,H             
4AD5: 44         LD      B,H             
4AD6: 28 28      JR      Z,$4B00         
4AD8: 10 10      STOP    $10             
4ADA: 28 28      JR      Z,$4B04         
4ADC: 44         LD      B,H             
4ADD: 44         LD      B,H             
4ADE: 00         NOP                     
4ADF: 00         NOP                     
4AE0: 00         NOP                     
4AE1: 00         NOP                     
4AE2: 00         NOP                     
4AE3: 00         NOP                     
4AE4: 44         LD      B,H             
4AE5: 44         LD      B,H             
4AE6: 28 28      JR      Z,$4B10         
4AE8: 10 10      STOP    $10             
4AEA: 28 28      JR      Z,$4B14         
4AEC: 44         LD      B,H             
4AED: 44         LD      B,H             
4AEE: 00         NOP                     
4AEF: 00         NOP                     
4AF0: 00         NOP                     
4AF1: 00         NOP                     
4AF2: 00         NOP                     
4AF3: 00         NOP                     
4AF4: 44         LD      B,H             
4AF5: 44         LD      B,H             
4AF6: 28 28      JR      Z,$4B20         
4AF8: 10 10      STOP    $10             
4AFA: 28 28      JR      Z,$4B24         
4AFC: 44         LD      B,H             
4AFD: 44         LD      B,H             
4AFE: 00         NOP                     
4AFF: 00         NOP                     
4B00: 00         NOP                     
4B01: 00         NOP                     
4B02: 0F         RRCA                    
4B03: 00         NOP                     
4B04: 3F         CCF                     
4B05: 00         NOP                     
4B06: FF         RST     0X38            
4B07: 00         NOP                     
4B08: F8 07      LDHL    SP,$07          
4B0A: E0 1F      LDFF00  ($1F),A         
4B0C: 80         ADD     A,B             
4B0D: 7F         LD      A,A             
4B0E: 00         NOP                     
4B0F: C6 00      ADD     $00             
4B11: 20 03      JR      NZ,$4B16        
4B13: 00         NOP                     
4B14: CF         RST     0X08            
4B15: 00         NOP                     
4B16: FF         RST     0X38            
4B17: 00         NOP                     
4B18: FE 01      CP      $01             
4B1A: 78         LD      A,B             
4B1B: 87         ADD     A,A             
4B1C: 00         NOP                     
4B1D: F8 00      LDHL    SP,$00          
4B1F: 78         LD      A,B             
4B20: 7C         LD      A,H             
4B21: 00         NOP                     
4B22: FE 00      CP      $00             
4B24: FF         RST     0X38            
4B25: 00         NOP                     
4B26: FF         RST     0X38            
4B27: 00         NOP                     
4B28: 03         INC     BC              
4B29: FC         ???                     
4B2A: 00         NOP                     
4B2B: 07         RLCA                    
4B2C: 00         NOP                     
4B2D: 07         RLCA                    
4B2E: 00         NOP                     
4B2F: 0D         DEC     C               
4B30: 00         NOP                     
4B31: 40         LD      B,B             
4B32: 00         NOP                     
4B33: 00         NOP                     
4B34: 80         ADD     A,B             
4B35: 00         NOP                     
4B36: FF         RST     0X38            
4B37: 00         NOP                     
4B38: FF         RST     0X38            
4B39: 00         NOP                     
4B3A: 7F         LD      A,A             
4B3B: 80         ADD     A,B             
4B3C: 0F         RRCA                    
4B3D: F0 00      LD      A,($00)         
4B3F: 9F         SBC     A               
4B40: 00         NOP                     
4B41: 86         ADD     A,(HL)          
4B42: 00         NOP                     
4B43: FC         ???                     
4B44: 00         NOP                     
4B45: CC 00 6F   CALL    Z,$6F00         
4B48: 00         NOP                     
4B49: 3C         INC     A               
4B4A: 00         NOP                     
4B4B: 04         INC     B               
4B4C: 00         NOP                     
4B4D: 03         INC     BC              
4B4E: 00         NOP                     
4B4F: 00         NOP                     
4B50: 00         NOP                     
4B51: 7C         LD      A,H             
4B52: 00         NOP                     
4B53: 3F         CCF                     
4B54: 00         NOP                     
4B55: E1         POP     HL              
4B56: 00         NOP                     
4B57: E0 00      LDFF00  ($00),A         
4B59: DB         ???                     
4B5A: 00         NOP                     
4B5B: 8F         ADC     A,A             
4B5C: 00         NOP                     
4B5D: 00         NOP                     
4B5E: 00         NOP                     
4B5F: 00         NOP                     
4B60: 00         NOP                     
4B61: 78         LD      A,B             
4B62: 00         NOP                     
4B63: E0 00      LDFF00  ($00),A         
4B65: FF         RST     0X38            
4B66: 00         NOP                     
4B67: C3 00 80   JP      $8000           
4B6A: 00         NOP                     
4B6B: 00         NOP                     
4B6C: 00         NOP                     
4B6D: 00         NOP                     
4B6E: 00         NOP                     
4B6F: 00         NOP                     
4B70: 00         NOP                     
4B71: 99         SBC     C               
4B72: 00         NOP                     
4B73: E9         JP      (HL)            
4B74: 00         NOP                     
4B75: 07         RLCA                    
4B76: 00         NOP                     
4B77: 03         INC     BC              
4B78: 00         NOP                     
4B79: 00         NOP                     
4B7A: 00         NOP                     
4B7B: 00         NOP                     
4B7C: 00         NOP                     
4B7D: 00         NOP                     
4B7E: 00         NOP                     
4B7F: 00         NOP                     
4B80: FF         RST     0X38            
4B81: 00         NOP                     
4B82: FF         RST     0X38            
4B83: 80         ADD     A,B             
4B84: FF         RST     0X38            
4B85: 38 FF      JR      C,$4B86         
4B87: 7E         LD      A,(HL)          
4B88: FF         RST     0X38            
4B89: FF         RST     0X38            
4B8A: FF         RST     0X38            
4B8B: 0F         RRCA                    
4B8C: FF         RST     0X38            
4B8D: BF         CP      A               
4B8E: FF         RST     0X38            
4B8F: FF         RST     0X38            
4B90: FF         RST     0X38            
4B91: 00         NOP                     
4B92: FF         RST     0X38            
4B93: 10 FF      STOP    $FF             
4B95: 38 FF      JR      C,$4B96         
4B97: 7C         LD      A,H             
4B98: FF         RST     0X38            
4B99: 7F         LD      A,A             
4B9A: FF         RST     0X38            
4B9B: E7         RST     0X20            
4B9C: FF         RST     0X38            
4B9D: EF         RST     0X28            
4B9E: FF         RST     0X38            
4B9F: FF         RST     0X38            
4BA0: FF         RST     0X38            
4BA1: 3E FF      LD      A,$FF           
4BA3: 7F         LD      A,A             
4BA4: FF         RST     0X38            
4BA5: 0F         RRCA                    
4BA6: FF         RST     0X38            
4BA7: C7         RST     0X00            
4BA8: FF         RST     0X38            
4BA9: E3         ???                     
4BAA: FF         RST     0X38            
4BAB: FF         RST     0X38            
4BAC: FF         RST     0X38            
4BAD: FF         RST     0X38            
4BAE: FF         RST     0X38            
4BAF: FF         RST     0X38            
4BB0: FF         RST     0X38            
4BB1: 07         RLCA                    
4BB2: FF         RST     0X38            
4BB3: 0F         RRCA                    
4BB4: FF         RST     0X38            
4BB5: 9E         SBC     (HL)            
4BB6: FF         RST     0X38            
4BB7: BE         CP      (HL)            
4BB8: FF         RST     0X38            
4BB9: FF         RST     0X38            
4BBA: FF         RST     0X38            
4BBB: FF         RST     0X38            
4BBC: FF         RST     0X38            
4BBD: FF         RST     0X38            
4BBE: FF         RST     0X38            
4BBF: FF         RST     0X38            
4BC0: FF         RST     0X38            
4BC1: FF         RST     0X38            
4BC2: FF         RST     0X38            
4BC3: FF         RST     0X38            
4BC4: FF         RST     0X38            
4BC5: FF         RST     0X38            
4BC6: FF         RST     0X38            
4BC7: FF         RST     0X38            
4BC8: FF         RST     0X38            
4BC9: FF         RST     0X38            
4BCA: FF         RST     0X38            
4BCB: FB         EI                      
4BCC: FF         RST     0X38            
4BCD: FB         EI                      
4BCE: FF         RST     0X38            
4BCF: F9         LD      SP,HL           
4BD0: FF         RST     0X38            
4BD1: FF         RST     0X38            
4BD2: FF         RST     0X38            
4BD3: FF         RST     0X38            
4BD4: FF         RST     0X38            
4BD5: FF         RST     0X38            
4BD6: FF         RST     0X38            
4BD7: FF         RST     0X38            
4BD8: FF         RST     0X38            
4BD9: FF         RST     0X38            
4BDA: FF         RST     0X38            
4BDB: FF         RST     0X38            
4BDC: FF         RST     0X38            
4BDD: FF         RST     0X38            
4BDE: FF         RST     0X38            
4BDF: FE FF      CP      $FF             
4BE1: FF         RST     0X38            
4BE2: FF         RST     0X38            
4BE3: FF         RST     0X38            
4BE4: FF         RST     0X38            
4BE5: FF         RST     0X38            
4BE6: FF         RST     0X38            
4BE7: FF         RST     0X38            
4BE8: FF         RST     0X38            
4BE9: FF         RST     0X38            
4BEA: FF         RST     0X38            
4BEB: FD         ???                     
4BEC: FF         RST     0X38            
4BED: 7E         LD      A,(HL)          
4BEE: FF         RST     0X38            
4BEF: FE FF      CP      $FF             
4BF1: FF         RST     0X38            
4BF2: FF         RST     0X38            
4BF3: FF         RST     0X38            
4BF4: FF         RST     0X38            
4BF5: FF         RST     0X38            
4BF6: FF         RST     0X38            
4BF7: FF         RST     0X38            
4BF8: FF         RST     0X38            
4BF9: FF         RST     0X38            
4BFA: FF         RST     0X38            
4BFB: FF         RST     0X38            
4BFC: FF         RST     0X38            
4BFD: FF         RST     0X38            
4BFE: FF         RST     0X38            
4BFF: FD         ???                     
4C00: 00         NOP                     
4C01: 00         NOP                     
4C02: 00         NOP                     
4C03: 00         NOP                     
4C04: 00         NOP                     
4C05: 00         NOP                     
4C06: 00         NOP                     
4C07: 00         NOP                     
4C08: 00         NOP                     
4C09: 00         NOP                     
4C0A: 01 00 3F   LD      BC,$3F00        
4C0D: 00         NOP                     
4C0E: FF         RST     0X38            
4C0F: 00         NOP                     
4C10: 00         NOP                     
4C11: 00         NOP                     
4C12: 00         NOP                     
4C13: 00         NOP                     
4C14: 00         NOP                     
4C15: 00         NOP                     
4C16: 00         NOP                     
4C17: 00         NOP                     
4C18: 7F         LD      A,A             
4C19: 00         NOP                     
4C1A: FF         RST     0X38            
4C1B: 00         NOP                     
4C1C: FF         RST     0X38            
4C1D: 00         NOP                     
4C1E: FF         RST     0X38            
4C1F: 00         NOP                     
4C20: 00         NOP                     
4C21: 00         NOP                     
4C22: 07         RLCA                    
4C23: 00         NOP                     
4C24: 1F         RRA                     
4C25: 00         NOP                     
4C26: 7F         LD      A,A             
4C27: 00         NOP                     
4C28: FF         RST     0X38            
4C29: 00         NOP                     
4C2A: FF         RST     0X38            
4C2B: 00         NOP                     
4C2C: FF         RST     0X38            
4C2D: 00         NOP                     
4C2E: FF         RST     0X38            
4C2F: 00         NOP                     
4C30: 0F         RRCA                    
4C31: 00         NOP                     
4C32: FF         RST     0X38            
4C33: 00         NOP                     
4C34: FF         RST     0X38            
4C35: 00         NOP                     
4C36: FF         RST     0X38            
4C37: 00         NOP                     
4C38: FF         RST     0X38            
4C39: 00         NOP                     
4C3A: FF         RST     0X38            
4C3B: 00         NOP                     
4C3C: FF         RST     0X38            
4C3D: 00         NOP                     
4C3E: FF         RST     0X38            
4C3F: 00         NOP                     
4C40: 00         NOP                     
4C41: 00         NOP                     
4C42: 00         NOP                     
4C43: 00         NOP                     
4C44: 00         NOP                     
4C45: 00         NOP                     
4C46: 00         NOP                     
4C47: 00         NOP                     
4C48: 01 00 07   LD      BC,$0700        
4C4B: 00         NOP                     
4C4C: 7F         LD      A,A             
4C4D: 00         NOP                     
4C4E: FF         RST     0X38            
4C4F: 00         NOP                     
4C50: 01 00 07   LD      BC,$0700        
4C53: 00         NOP                     
4C54: 0F         RRCA                    
4C55: 00         NOP                     
4C56: 1F         RRA                     
4C57: 00         NOP                     
4C58: FF         RST     0X38            
4C59: 00         NOP                     
4C5A: FF         RST     0X38            
4C5B: 00         NOP                     
4C5C: FF         RST     0X38            
4C5D: 00         NOP                     
4C5E: FF         RST     0X38            
4C5F: 00         NOP                     
4C60: 01 00 01   LD      BC,$0100        
4C63: 00         NOP                     
4C64: 03         INC     BC              
4C65: 00         NOP                     
4C66: 07         RLCA                    
4C67: 00         NOP                     
4C68: 0F         RRCA                    
4C69: 00         NOP                     
4C6A: 3F         CCF                     
4C6B: 00         NOP                     
4C6C: 7F         LD      A,A             
4C6D: 00         NOP                     
4C6E: FF         RST     0X38            
4C6F: 00         NOP                     
4C70: E0 00      LDFF00  ($00),A         
4C72: FF         RST     0X38            
4C73: 00         NOP                     
4C74: FF         RST     0X38            
4C75: 00         NOP                     
4C76: FF         RST     0X38            
4C77: 00         NOP                     
4C78: FF         RST     0X38            
4C79: 00         NOP                     
4C7A: FF         RST     0X38            
4C7B: 00         NOP                     
4C7C: FF         RST     0X38            
4C7D: 00         NOP                     
4C7E: FF         RST     0X38            
4C7F: 00         NOP                     
4C80: 00         NOP                     
4C81: 00         NOP                     
4C82: 80         ADD     A,B             
4C83: 00         NOP                     
4C84: F8 00      LDHL    SP,$00          
4C86: FF         RST     0X38            
4C87: 00         NOP                     
4C88: FF         RST     0X38            
4C89: 00         NOP                     
4C8A: FF         RST     0X38            
4C8B: 00         NOP                     
4C8C: FF         RST     0X38            
4C8D: 00         NOP                     
4C8E: FF         RST     0X38            
4C8F: 00         NOP                     
4C90: 00         NOP                     
4C91: 00         NOP                     
4C92: 00         NOP                     
4C93: 00         NOP                     
4C94: 00         NOP                     
4C95: 00         NOP                     
4C96: 00         NOP                     
4C97: 00         NOP                     
4C98: F0 00      LD      A,($00)         
4C9A: FF         RST     0X38            
4C9B: 00         NOP                     
4C9C: FF         RST     0X38            
4C9D: 00         NOP                     
4C9E: FF         RST     0X38            
4C9F: 00         NOP                     
4CA0: 00         NOP                     
4CA1: 00         NOP                     
4CA2: 00         NOP                     
4CA3: 00         NOP                     
4CA4: 00         NOP                     
4CA5: 00         NOP                     
4CA6: 00         NOP                     
4CA7: 00         NOP                     
4CA8: 00         NOP                     
4CA9: 00         NOP                     
4CAA: 80         ADD     A,B             
4CAB: 00         NOP                     
4CAC: F0 00      LD      A,($00)         
4CAE: FF         RST     0X38            
4CAF: 00         NOP                     
4CB0: 80         ADD     A,B             
4CB1: 00         NOP                     
4CB2: 80         ADD     A,B             
4CB3: 00         NOP                     
4CB4: C0         RET     NZ              
4CB5: 00         NOP                     
4CB6: E0 00      LDFF00  ($00),A         
4CB8: F0 00      LD      A,($00)         
4CBA: FC         ???                     
4CBB: 00         NOP                     
4CBC: FE 00      CP      $00             
4CBE: FF         RST     0X38            
4CBF: 00         NOP                     
4CC0: 80         ADD     A,B             
4CC1: 00         NOP                     
4CC2: E0 00      LDFF00  ($00),A         
4CC4: F0 00      LD      A,($00)         
4CC6: F8 00      LDHL    SP,$00          
4CC8: FF         RST     0X38            
4CC9: 00         NOP                     
4CCA: FF         RST     0X38            
4CCB: 00         NOP                     
4CCC: FF         RST     0X38            
4CCD: 00         NOP                     
4CCE: FF         RST     0X38            
4CCF: 00         NOP                     
4CD0: 00         NOP                     
4CD1: 00         NOP                     
4CD2: 00         NOP                     
4CD3: 00         NOP                     
4CD4: 00         NOP                     
4CD5: 00         NOP                     
4CD6: 00         NOP                     
4CD7: 00         NOP                     
4CD8: 80         ADD     A,B             
4CD9: 00         NOP                     
4CDA: E0 00      LDFF00  ($00),A         
4CDC: FE 00      CP      $00             
4CDE: FF         RST     0X38            
4CDF: 00         NOP                     
4CE0: FF         RST     0X38            
4CE1: 00         NOP                     
4CE2: 3E 00      LD      A,$00           
4CE4: 00         NOP                     
4CE5: 00         NOP                     
4CE6: 00         NOP                     
4CE7: 00         NOP                     
4CE8: 00         NOP                     
4CE9: C0         RET     NZ              
4CEA: 00         NOP                     
4CEB: F1         POP     AF              
4CEC: 00         NOP                     
4CED: FF         RST     0X38            
4CEE: 00         NOP                     
4CEF: FF         RST     0X38            
4CF0: FF         RST     0X38            
4CF1: 00         NOP                     
4CF2: 0E 00      LD      C,$00           
4CF4: 00         NOP                     
4CF5: 00         NOP                     
4CF6: 00         NOP                     
4CF7: 00         NOP                     
4CF8: 00         NOP                     
4CF9: 01 00 C7   LD      BC,$C700        
4CFC: 00         NOP                     
4CFD: FF         RST     0X38            
4CFE: 00         NOP                     
4CFF: FF         RST     0X38            
4D00: 00         NOP                     
4D01: 00         NOP                     
4D02: 00         NOP                     
4D03: 00         NOP                     
4D04: 00         NOP                     
4D05: 01 00 01   LD      BC,$0100        
4D08: 00         NOP                     
4D09: 03         INC     BC              
4D0A: 00         NOP                     
4D0B: 03         INC     BC              
4D0C: 00         NOP                     
4D0D: 07         RLCA                    
4D0E: 00         NOP                     
4D0F: 07         RLCA                    
4D10: 00         NOP                     
4D11: 4E         LD      C,(HL)          
4D12: 00         NOP                     
4D13: 8F         ADC     A,A             
4D14: 00         NOP                     
4D15: 1F         RRA                     
4D16: 00         NOP                     
4D17: 3F         CCF                     
4D18: 00         NOP                     
4D19: F1         POP     AF              
4D1A: 00         NOP                     
4D1B: E0 00      LDFF00  ($00),A         
4D1D: E0 00      LDFF00  ($00),A         
4D1F: C0         RET     NZ              
4D20: 06 10      LD      B,$10           
4D22: 03         INC     BC              
4D23: 18 03      JR      $4D28           
4D25: 9C         SBC     H               
4D26: 01 FC 01   LD      BC,$01FC        
4D29: FE 01      CP      $01             
4D2B: F0 00      LD      A,($00)         
4D2D: E0 00      LDFF00  ($00),A         
4D2F: 60         LD      H,B             
4D30: 00         NOP                     
4D31: 00         NOP                     
4D32: 00         NOP                     
4D33: 00         NOP                     
4D34: 80         ADD     A,B             
4D35: 00         NOP                     
4D36: 80         ADD     A,B             
4D37: 00         NOP                     
4D38: C0         RET     NZ              
4D39: 00         NOP                     
4D3A: C0         RET     NZ              
4D3B: 00         NOP                     
4D3C: E0 00      LDFF00  ($00),A         
4D3E: E0 00      LDFF00  ($00),A         
4D40: 00         NOP                     
4D41: 0D         DEC     C               
4D42: 00         NOP                     
4D43: 08 00 08   LD      ($0800),SP      
4D46: 00         NOP                     
4D47: 08 00 10   LD      ($1000),SP      
4D4A: 00         NOP                     
4D4B: 10 00      STOP    $00             
4D4D: 10 00      STOP    $00             
4D4F: 19         ADD     HL,DE           
4D50: 00         NOP                     
4D51: C0         RET     NZ              
4D52: 00         NOP                     
4D53: C0         RET     NZ              
4D54: 00         NOP                     
4D55: C0         RET     NZ              
4D56: 00         NOP                     
4D57: E0 00      LDFF00  ($00),A         
4D59: F1         POP     AF              
4D5A: 00         NOP                     
4D5B: FF         RST     0X38            
4D5C: 00         NOP                     
4D5D: FF         RST     0X38            
4D5E: 00         NOP                     
4D5F: FF         RST     0X38            
4D60: 00         NOP                     
4D61: 60         LD      H,B             
4D62: 00         NOP                     
4D63: 60         LD      H,B             
4D64: 00         NOP                     
4D65: 70         LD      (HL),B          
4D66: 00         NOP                     
4D67: F8 00      LDHL    SP,$00          
4D69: FE 00      CP      $00             
4D6B: FE 00      CP      $00             
4D6D: FE 00      CP      $00             
4D6F: FC         ???                     
4D70: F0 00      LD      A,($00)         
4D72: F0 00      LD      A,($00)         
4D74: F0 00      LD      A,($00)         
4D76: F0 00      LD      A,($00)         
4D78: F8 00      LDHL    SP,$00          
4D7A: F8 00      LDHL    SP,$00          
4D7C: F8 00      LDHL    SP,$00          
4D7E: F8 00      LDHL    SP,$00          
4D80: 00         NOP                     
4D81: 1F         RRA                     
4D82: 00         NOP                     
4D83: 1F         RRA                     
4D84: 00         NOP                     
4D85: 1E 00      LD      E,$00           
4D87: 1C         INC     E               
4D88: 00         NOP                     
4D89: 1C         INC     E               
4D8A: 00         NOP                     
4D8B: 1C         INC     E               
4D8C: 00         NOP                     
4D8D: 0C         INC     C               
4D8E: 00         NOP                     
4D8F: 0E 00      LD      C,$00           
4D91: FE 00      CP      $00             
4D93: FC         ???                     
4D94: 00         NOP                     
4D95: 7C         LD      A,H             
4D96: 00         NOP                     
4D97: 3C         INC     A               
4D98: 00         NOP                     
4D99: 1C         INC     E               
4D9A: 00         NOP                     
4D9B: 0E 00      LD      C,$00           
4D9D: 0F         RRCA                    
4D9E: 00         NOP                     
4D9F: 0F         RRCA                    
4DA0: 00         NOP                     
4DA1: 38 00      JR      C,$4DA3         
4DA3: 18 01      JR      $4DA6           
4DA5: 18 01      JR      $4DA8           
4DA7: 18 03      JR      $4DAC           
4DA9: 18 03      JR      $4DAE           
4DAB: 38 07      JR      C,$4DB4         
4DAD: F0 0F      LD      A,($0F)         
4DAF: E0 F8      LDFF00  ($F8),A         
4DB1: 00         NOP                     
4DB2: F8 00      LDHL    SP,$00          
4DB4: F8 00      LDHL    SP,$00          
4DB6: F8 00      LDHL    SP,$00          
4DB8: F8 00      LDHL    SP,$00          
4DBA: F8 00      LDHL    SP,$00          
4DBC: F0 00      LD      A,($00)         
4DBE: F0 00      LD      A,($00)         
4DC0: 08 07 18   LD      ($1807),SP      
4DC3: 03         INC     BC              
4DC4: 3E 00      LD      A,$00           
4DC6: 3F         CCF                     
4DC7: 00         NOP                     
4DC8: 7F         LD      A,A             
4DC9: 00         NOP                     
4DCA: 7F         LD      A,A             
4DCB: 00         NOP                     
4DCC: 7F         LD      A,A             
4DCD: 00         NOP                     
4DCE: FF         RST     0X38            
4DCF: 00         NOP                     
4DD0: 00         NOP                     
4DD1: 1E 00      LD      E,$00           
4DD3: FC         ???                     
4DD4: 01 FC FF   LD      BC,$FFFC        
4DD7: 00         NOP                     
4DD8: FF         RST     0X38            
4DD9: 00         NOP                     
4DDA: FF         RST     0X38            
4DDB: 00         NOP                     
4DDC: FF         RST     0X38            
4DDD: 00         NOP                     
4DDE: FF         RST     0X38            
4DDF: 00         NOP                     
4DE0: 1F         RRA                     
4DE1: 00         NOP                     
4DE2: 3F         CCF                     
4DE3: 00         NOP                     
4DE4: FF         RST     0X38            
4DE5: 00         NOP                     
4DE6: FF         RST     0X38            
4DE7: 00         NOP                     
4DE8: FF         RST     0X38            
4DE9: 00         NOP                     
4DEA: FF         RST     0X38            
4DEB: 00         NOP                     
4DEC: FF         RST     0X38            
4DED: 00         NOP                     
4DEE: FF         RST     0X38            
4DEF: 00         NOP                     
4DF0: F0 00      LD      A,($00)         
4DF2: F8 00      LDHL    SP,$00          
4DF4: FC         ???                     
4DF5: 00         NOP                     
4DF6: FC         ???                     
4DF7: 00         NOP                     
4DF8: FE 00      CP      $00             
4DFA: FE 00      CP      $00             
4DFC: FE 00      CP      $00             
4DFE: FF         RST     0X38            
4DFF: 00         NOP                     
4E00: FF         RST     0X38            
4E01: FB         EI                      
4E02: FF         RST     0X38            
4E03: F9         LD      SP,HL           
4E04: FF         RST     0X38            
4E05: FB         EI                      
4E06: FF         RST     0X38            
4E07: F0 FF      LD      A,($FF)         
4E09: F1         POP     AF              
4E0A: FF         RST     0X38            
4E0B: 3F         CCF                     
4E0C: FF         RST     0X38            
4E0D: 00         NOP                     
4E0E: FF         RST     0X38            
4E0F: 00         NOP                     
4E10: FF         RST     0X38            
4E11: FE FF      CP      $FF             
4E13: FD         ???                     
4E14: FF         RST     0X38            
4E15: FC         ???                     
4E16: FF         RST     0X38            
4E17: FD         ???                     
4E18: FF         RST     0X38            
4E19: F8 FF      LDHL    SP,$FF          
4E1B: 07         RLCA                    
4E1C: FF         RST     0X38            
4E1D: 00         NOP                     
4E1E: FF         RST     0X38            
4E1F: 00         NOP                     
4E20: FF         RST     0X38            
4E21: FE FF      CP      $FF             
4E23: FE FF      CP      $FF             
4E25: FC         ???                     
4E26: FF         RST     0X38            
4E27: FC         ???                     
4E28: FF         RST     0X38            
4E29: 7F         LD      A,A             
4E2A: FF         RST     0X38            
4E2B: C0         RET     NZ              
4E2C: FF         RST     0X38            
4E2D: 00         NOP                     
4E2E: FF         RST     0X38            
4E2F: 00         NOP                     
4E30: FF         RST     0X38            
4E31: 79         LD      A,C             
4E32: FF         RST     0X38            
4E33: FB         EI                      
4E34: FF         RST     0X38            
4E35: 79         LD      A,C             
4E36: FF         RST     0X38            
4E37: F3         DI                      
4E38: FF         RST     0X38            
4E39: F9         LD      SP,HL           
4E3A: FF         RST     0X38            
4E3B: 0F         RRCA                    
4E3C: FF         RST     0X38            
4E3D: 00         NOP                     
4E3E: FF         RST     0X38            
4E3F: 00         NOP                     
4E40: 00         NOP                     
4E41: FF         RST     0X38            
4E42: 00         NOP                     
4E43: EF         RST     0X28            
4E44: 00         NOP                     
4E45: 7F         LD      A,A             
4E46: 00         NOP                     
4E47: DD         ???                     
4E48: 00         NOP                     
4E49: 77         LD      (HL),A          
4E4A: 00         NOP                     
4E4B: AA         XOR     D               
4E4C: 00         NOP                     
4E4D: 4D         LD      C,L             
4E4E: 00         NOP                     
4E4F: 90         SUB     B               
4E50: 1C         INC     E               
4E51: 1C         INC     E               
4E52: 22         LD      (HLI),A         
4E53: 3E 5D      LD      A,$5D           
4E55: 7F         LD      A,A             
4E56: 51         LD      D,C             
4E57: 7F         LD      A,A             
4E58: 51         LD      D,C             
4E59: 7F         LD      A,A             
4E5A: 5D         LD      E,L             
4E5B: 7F         LD      A,A             
4E5C: 22         LD      (HLI),A         
4E5D: 3E 1D      LD      A,$1D           
4E5F: 1C         INC     E               
4E60: 00         NOP                     
4E61: 0C         INC     C               
4E62: 0C         INC     C               
4E63: 1F         RRA                     
4E64: 1D         DEC     E               
4E65: 3F         CCF                     
4E66: 0C         INC     C               
4E67: 1F         RRA                     
4E68: 0C         INC     C               
4E69: 1F         RRA                     
4E6A: 2D         DEC     L               
4E6B: 1F         RRA                     
4E6C: 6C         LD      L,H             
4E6D: 1F         RRA                     
4E6E: E0 0C      LDFF00  ($0C),A         
4E70: 08 E3 E3   LD      ($E3E3),SP      
4E73: F7         RST     0X30            
4E74: B6         OR      (HL)            
4E75: FF         RST     0X38            
4E76: F3         DI                      
4E77: FF         RST     0X38            
4E78: 30 FF      JR      NC,$4E79        
4E7A: B6         OR      (HL)            
4E7B: FF         RST     0X38            
4E7C: E3         ???                     
4E7D: F7         RST     0X30            
4E7E: 08 E3 20   LD      ($20E3),SP      
4E81: 8E         ADC     A,(HL)          
4E82: 8E         ADC     A,(HL)          
4E83: DF         RST     0X18            
4E84: DB         ???                     
4E85: FF         RST     0X38            
4E86: C6 FF      ADD     $FF             
4E88: C3 FF DB   JP      $DBFF           
4E8B: FF         RST     0X38            
4E8C: 8E         ADC     A,(HL)          
4E8D: DF         RST     0X18            
4E8E: 20 8E      JR      NZ,$4E1E        
4E90: F0 06      LD      A,($06)         
4E92: 76         HALT                    
4E93: 0F         RRCA                    
4E94: 76         HALT                    
4E95: 8F         ADC     A,A             
4E96: 77         LD      (HL),A          
4E97: 0F         RRCA                    
4E98: 76         HALT                    
4E99: 8F         ADC     A,A             
4E9A: 76         HALT                    
4E9B: 8F         ADC     A,A             
4E9C: 76         HALT                    
4E9D: 8F         ADC     A,A             
4E9E: F0 06      LD      A,($06)         
4EA0: 01 6C 6C   LD      BC,$6C6C        
4EA3: FF         RST     0X38            
4EA4: 61         LD      H,C             
4EA5: FF         RST     0X38            
4EA6: 6D         LD      L,L             
4EA7: FF         RST     0X38            
4EA8: ED         ???                     
4EA9: FF         RST     0X38            
4EAA: 6D         LD      L,L             
4EAB: FF         RST     0X38            
4EAC: 6D         LD      L,L             
4EAD: FF         RST     0X38            
4EAE: 00         NOP                     
4EAF: 6D         LD      L,L             
4EB0: F0 06      LD      A,($06)         
4EB2: 06 6F      LD      B,$6F           
4EB4: 6F         LD      L,A             
4EB5: FF         RST     0X38            
4EB6: F6 FF      OR      $FF             
4EB8: B6         OR      (HL)            
4EB9: FF         RST     0X38            
4EBA: B6         OR      (HL)            
4EBB: FF         RST     0X38            
4EBC: B6         OR      (HL)            
4EBD: FF         RST     0X38            
4EBE: 00         NOP                     
4EBF: B6         OR      (HL)            
4EC0: FF         RST     0X38            
4EC1: 00         NOP                     
4EC2: 00         NOP                     
4EC3: 72         LD      (HL),D          
4EC4: 72         LD      (HL),D          
4EC5: FF         RST     0X38            
4EC6: DB         ???                     
4EC7: FF         RST     0X38            
4EC8: FB         EI                      
4EC9: FF         RST     0X38            
4ECA: C3 FF 7B   JP      $7BFF           
4ECD: FF         RST     0X38            
4ECE: 00         NOP                     
4ECF: 7B         LD      A,E             
4ED0: 80         ADD     A,B             
4ED1: 01 01 C7   LD      BC,$C701        
4ED4: C7         RST     0X00            
4ED5: FF         RST     0X38            
4ED6: ED         ???                     
4ED7: FF         RST     0X38            
4ED8: 6D         LD      L,L             
4ED9: FF         RST     0X38            
4EDA: 6D         LD      L,L             
4EDB: FF         RST     0X38            
4EDC: 67         LD      H,A             
4EDD: FF         RST     0X38            
4EDE: 00         NOP                     
4EDF: 67         LD      H,A             
4EE0: 00         NOP                     
4EE1: 80         ADD     A,B             
4EE2: 80         ADD     A,B             
4EE3: DC 9C FE   CALL    C,$FE9C         
4EE6: B6         OR      (HL)            
4EE7: FF         RST     0X38            
4EE8: B6         OR      (HL)            
4EE9: FF         RST     0X38            
4EEA: B6         OR      (HL)            
4EEB: FF         RST     0X38            
4EEC: 9C         SBC     H               
4EED: FE 00      CP      $00             
4EEF: 9C         SBC     H               
4EF0: 00         NOP                     
4EF1: 00         NOP                     
4EF2: 00         NOP                     
4EF3: 00         NOP                     
4EF4: 44         LD      B,H             
4EF5: 44         LD      B,H             
4EF6: 28 28      JR      Z,$4F20         
4EF8: 10 10      STOP    $10             
4EFA: 28 28      JR      Z,$4F24         
4EFC: 44         LD      B,H             
4EFD: 44         LD      B,H             
4EFE: 00         NOP                     
4EFF: 00         NOP                     
4F00: 00         NOP                     
4F01: 00         NOP                     
4F02: 00         NOP                     
4F03: 00         NOP                     
4F04: 00         NOP                     
4F05: 00         NOP                     
4F06: 00         NOP                     
4F07: 00         NOP                     
4F08: 00         NOP                     
4F09: 00         NOP                     
4F0A: 00         NOP                     
4F0B: 00         NOP                     
4F0C: 00         NOP                     
4F0D: 00         NOP                     
4F0E: 00         NOP                     
4F0F: 00         NOP                     
4F10: 01 00 01   LD      BC,$0100        
4F13: 00         NOP                     
4F14: 03         INC     BC              
4F15: 00         NOP                     
4F16: 07         RLCA                    
4F17: 00         NOP                     
4F18: 0F         RRCA                    
4F19: 00         NOP                     
4F1A: 3F         CCF                     
4F1B: 00         NOP                     
4F1C: 7F         LD      A,A             
4F1D: 00         NOP                     
4F1E: FF         RST     0X38            
4F1F: 00         NOP                     
4F20: FF         RST     0X38            
4F21: 00         NOP                     
4F22: FF         RST     0X38            
4F23: 00         NOP                     
4F24: FF         RST     0X38            
4F25: 00         NOP                     
4F26: FF         RST     0X38            
4F27: 00         NOP                     
4F28: FF         RST     0X38            
4F29: 00         NOP                     
4F2A: FF         RST     0X38            
4F2B: 00         NOP                     
4F2C: FF         RST     0X38            
4F2D: 00         NOP                     
4F2E: FF         RST     0X38            
4F2F: 00         NOP                     
4F30: FF         RST     0X38            
4F31: 00         NOP                     
4F32: FF         RST     0X38            
4F33: 00         NOP                     
4F34: FF         RST     0X38            
4F35: 00         NOP                     
4F36: FF         RST     0X38            
4F37: 00         NOP                     
4F38: FF         RST     0X38            
4F39: 00         NOP                     
4F3A: FF         RST     0X38            
4F3B: 00         NOP                     
4F3C: FF         RST     0X38            
4F3D: 00         NOP                     
4F3E: FF         RST     0X38            
4F3F: 00         NOP                     
4F40: FF         RST     0X38            
4F41: 00         NOP                     
4F42: FF         RST     0X38            
4F43: 00         NOP                     
4F44: FF         RST     0X38            
4F45: 00         NOP                     
4F46: FF         RST     0X38            
4F47: 00         NOP                     
4F48: FF         RST     0X38            
4F49: 00         NOP                     
4F4A: FF         RST     0X38            
4F4B: 00         NOP                     
4F4C: FF         RST     0X38            
4F4D: 00         NOP                     
4F4E: FF         RST     0X38            
4F4F: 00         NOP                     
4F50: FF         RST     0X38            
4F51: 00         NOP                     
4F52: FF         RST     0X38            
4F53: 00         NOP                     
4F54: FF         RST     0X38            
4F55: 00         NOP                     
4F56: FF         RST     0X38            
4F57: 00         NOP                     
4F58: FF         RST     0X38            
4F59: 00         NOP                     
4F5A: FF         RST     0X38            
4F5B: 00         NOP                     
4F5C: FF         RST     0X38            
4F5D: 00         NOP                     
4F5E: FF         RST     0X38            
4F5F: 00         NOP                     
4F60: FF         RST     0X38            
4F61: 00         NOP                     
4F62: FF         RST     0X38            
4F63: 00         NOP                     
4F64: FF         RST     0X38            
4F65: 00         NOP                     
4F66: FF         RST     0X38            
4F67: 00         NOP                     
4F68: FF         RST     0X38            
4F69: 00         NOP                     
4F6A: FF         RST     0X38            
4F6B: 00         NOP                     
4F6C: FF         RST     0X38            
4F6D: 00         NOP                     
4F6E: FF         RST     0X38            
4F6F: 00         NOP                     
4F70: FF         RST     0X38            
4F71: 00         NOP                     
4F72: FF         RST     0X38            
4F73: 00         NOP                     
4F74: FF         RST     0X38            
4F75: 00         NOP                     
4F76: FF         RST     0X38            
4F77: 00         NOP                     
4F78: FF         RST     0X38            
4F79: 00         NOP                     
4F7A: FF         RST     0X38            
4F7B: 00         NOP                     
4F7C: FF         RST     0X38            
4F7D: 00         NOP                     
4F7E: FF         RST     0X38            
4F7F: 00         NOP                     
4F80: 80         ADD     A,B             
4F81: 00         NOP                     
4F82: 80         ADD     A,B             
4F83: 00         NOP                     
4F84: C0         RET     NZ              
4F85: 00         NOP                     
4F86: E0 00      LDFF00  ($00),A         
4F88: F0 00      LD      A,($00)         
4F8A: FC         ???                     
4F8B: 00         NOP                     
4F8C: FE 00      CP      $00             
4F8E: FF         RST     0X38            
4F8F: 00         NOP                     
4F90: 00         NOP                     
4F91: 00         NOP                     
4F92: 00         NOP                     
4F93: 00         NOP                     
4F94: 00         NOP                     
4F95: 00         NOP                     
4F96: 00         NOP                     
4F97: 00         NOP                     
4F98: 00         NOP                     
4F99: 00         NOP                     
4F9A: 00         NOP                     
4F9B: 00         NOP                     
4F9C: 00         NOP                     
4F9D: 00         NOP                     
4F9E: 00         NOP                     
4F9F: 00         NOP                     
4FA0: 00         NOP                     
4FA1: 00         NOP                     
4FA2: 00         NOP                     
4FA3: 00         NOP                     
4FA4: 44         LD      B,H             
4FA5: 44         LD      B,H             
4FA6: 28 28      JR      Z,$4FD0         
4FA8: 10 10      STOP    $10             
4FAA: 28 28      JR      Z,$4FD4         
4FAC: 44         LD      B,H             
4FAD: 44         LD      B,H             
4FAE: 00         NOP                     
4FAF: 00         NOP                     
4FB0: 00         NOP                     
4FB1: 00         NOP                     
4FB2: 00         NOP                     
4FB3: 00         NOP                     
4FB4: 44         LD      B,H             
4FB5: 44         LD      B,H             
4FB6: 28 28      JR      Z,$4FE0         
4FB8: 10 10      STOP    $10             
4FBA: 28 28      JR      Z,$4FE4         
4FBC: 44         LD      B,H             
4FBD: 44         LD      B,H             
4FBE: 00         NOP                     
4FBF: 00         NOP                     
4FC0: 00         NOP                     
4FC1: 00         NOP                     
4FC2: 00         NOP                     
4FC3: 00         NOP                     
4FC4: 00         NOP                     
4FC5: 00         NOP                     
4FC6: 00         NOP                     
4FC7: 00         NOP                     
4FC8: 00         NOP                     
4FC9: 00         NOP                     
4FCA: 00         NOP                     
4FCB: 00         NOP                     
4FCC: 00         NOP                     
4FCD: 00         NOP                     
4FCE: 00         NOP                     
4FCF: 00         NOP                     
4FD0: FF         RST     0X38            
4FD1: 00         NOP                     
4FD2: FF         RST     0X38            
4FD3: 00         NOP                     
4FD4: FF         RST     0X38            
4FD5: 00         NOP                     
4FD6: FF         RST     0X38            
4FD7: 00         NOP                     
4FD8: FF         RST     0X38            
4FD9: 00         NOP                     
4FDA: FF         RST     0X38            
4FDB: 00         NOP                     
4FDC: FF         RST     0X38            
4FDD: 00         NOP                     
4FDE: FF         RST     0X38            
4FDF: 00         NOP                     
4FE0: 00         NOP                     
4FE1: FF         RST     0X38            
4FE2: 00         NOP                     
4FE3: FF         RST     0X38            
4FE4: 00         NOP                     
4FE5: FF         RST     0X38            
4FE6: 00         NOP                     
4FE7: FF         RST     0X38            
4FE8: 00         NOP                     
4FE9: FF         RST     0X38            
4FEA: 00         NOP                     
4FEB: FF         RST     0X38            
4FEC: 00         NOP                     
4FED: FF         RST     0X38            
4FEE: 00         NOP                     
4FEF: FF         RST     0X38            
4FF0: FF         RST     0X38            
4FF1: FF         RST     0X38            
4FF2: FF         RST     0X38            
4FF3: FF         RST     0X38            
4FF4: FF         RST     0X38            
4FF5: FF         RST     0X38            
4FF6: FF         RST     0X38            
4FF7: FF         RST     0X38            
4FF8: FF         RST     0X38            
4FF9: FF         RST     0X38            
4FFA: FF         RST     0X38            
4FFB: FF         RST     0X38            
4FFC: FF         RST     0X38            
4FFD: FF         RST     0X38            
4FFE: FF         RST     0X38            
4FFF: FF         RST     0X38            
5000: FF         RST     0X38            
5001: 00         NOP                     
5002: EF         RST     0X28            
5003: 10 10      STOP    $10             
5005: EF         RST     0X28            
5006: 80         ADD     A,B             
5007: 7F         LD      A,A             
5008: 00         NOP                     
5009: F3         DI                      
500A: 00         NOP                     
500B: C0         RET     NZ              
500C: F0 00      LD      A,($00)         
500E: 3C         INC     A               
500F: 00         NOP                     
5010: C0         RET     NZ              
5011: 3F         CCF                     
5012: 07         RLCA                    
5013: F8 7F      LDHL    SP,$7F          
5015: 80         ADD     A,B             
5016: FE 01      CP      $01             
5018: 3F         CCF                     
5019: C0         RET     NZ              
501A: 0F         RRCA                    
501B: F0 00      LD      A,($00)         
501D: 0F         RRCA                    
501E: 1F         RRA                     
501F: 00         NOP                     
5020: 7F         LD      A,A             
5021: 80         ADD     A,B             
5022: 0E F1      LD      C,$F1           
5024: F0 0F      LD      A,($0F)         
5026: 03         INC     BC              
5027: FC         ???                     
5028: 9F         SBC     A               
5029: 60         LD      H,B             
502A: FF         RST     0X38            
502B: 00         NOP                     
502C: 1F         RRA                     
502D: E0 3E      LDFF00  ($3E),A         
502F: 01 C7 38   LD      BC,$38C7        
5032: 01 FE 3C   LD      BC,$3CFE        
5035: C3 FF 00   JP      $00FF           
5038: FF         RST     0X38            
5039: 00         NOP                     
503A: FE 01      CP      $01             
503C: F0 0F      LD      A,($0F)         
503E: 01 F8 1C   LD      BC,$1CF8        
5041: 00         NOP                     
5042: 07         RLCA                    
5043: 00         NOP                     
5044: 1E 00      LD      E,$00           
5046: 60         LD      H,B             
5047: 00         NOP                     
5048: 00         NOP                     
5049: 00         NOP                     
504A: 07         RLCA                    
504B: 00         NOP                     
504C: FF         RST     0X38            
504D: 00         NOP                     
504E: FF         RST     0X38            
504F: 3F         CCF                     
5050: 38 00      JR      C,$5052         
5052: E0 00      LDFF00  ($00),A         
5054: 03         INC     BC              
5055: 00         NOP                     
5056: 0E 00      LD      C,$00           
5058: 3C         INC     A               
5059: 0C         INC     C               
505A: FF         RST     0X38            
505B: 3F         CCF                     
505C: FF         RST     0X38            
505D: FF         RST     0X38            
505E: FF         RST     0X38            
505F: FF         RST     0X38            
5060: 00         NOP                     
5061: 00         NOP                     
5062: 70         LD      (HL),B          
5063: 00         NOP                     
5064: FC         ???                     
5065: 00         NOP                     
5066: FF         RST     0X38            
5067: 00         NOP                     
5068: 3F         CCF                     
5069: 00         NOP                     
506A: 03         INC     BC              
506B: 00         NOP                     
506C: E0 E0      LDFF00  ($E0),A         
506E: FF         RST     0X38            
506F: FF         RST     0X38            
5070: 00         NOP                     
5071: 00         NOP                     
5072: 00         NOP                     
5073: 00         NOP                     
5074: 00         NOP                     
5075: 00         NOP                     
5076: 80         ADD     A,B             
5077: 00         NOP                     
5078: FC         ???                     
5079: 00         NOP                     
507A: E1         POP     HL              
507B: 00         NOP                     
507C: 1F         RRA                     
507D: 00         NOP                     
507E: FE 00      CP      $00             
5080: 00         NOP                     
5081: 00         NOP                     
5082: FF         RST     0X38            
5083: 00         NOP                     
5084: EF         RST     0X28            
5085: 10 10      STOP    $10             
5087: EF         RST     0X28            
5088: 80         ADD     A,B             
5089: 7F         LD      A,A             
508A: 00         NOP                     
508B: F3         DI                      
508C: 00         NOP                     
508D: C0         RET     NZ              
508E: C0         RET     NZ              
508F: 00         NOP                     
5090: 00         NOP                     
5091: 00         NOP                     
5092: C0         RET     NZ              
5093: 3F         CCF                     
5094: 07         RLCA                    
5095: F8 7F      LDHL    SP,$7F          
5097: 80         ADD     A,B             
5098: FE 01      CP      $01             
509A: 3F         CCF                     
509B: C0         RET     NZ              
509C: 0F         RRCA                    
509D: F0 00      LD      A,($00)         
509F: 0F         RRCA                    
50A0: 00         NOP                     
50A1: 00         NOP                     
50A2: 7F         LD      A,A             
50A3: 80         ADD     A,B             
50A4: 0E F1      LD      C,$F1           
50A6: F0 0F      LD      A,($0F)         
50A8: 03         INC     BC              
50A9: FC         ???                     
50AA: 9F         SBC     A               
50AB: 60         LD      H,B             
50AC: FF         RST     0X38            
50AD: 00         NOP                     
50AE: 1F         RRA                     
50AF: E0 00      LDFF00  ($00),A         
50B1: 00         NOP                     
50B2: C7         RST     0X00            
50B3: 38 01      JR      C,$50B6         
50B5: FE 3C      CP      $3C             
50B7: C3 FF 00   JP      $00FF           
50BA: FF         RST     0X38            
50BB: 00         NOP                     
50BC: FE 01      CP      $01             
50BE: F0 0F      LD      A,($0F)         
50C0: 30 00      JR      NC,$50C2        
50C2: 1F         RRA                     
50C3: 00         NOP                     
50C4: 1F         RRA                     
50C5: 00         NOP                     
50C6: F0 00      LD      A,($00)         
50C8: 00         NOP                     
50C9: 00         NOP                     
50CA: 07         RLCA                    
50CB: 00         NOP                     
50CC: FF         RST     0X38            
50CD: 00         NOP                     
50CE: FF         RST     0X38            
50CF: 3F         CCF                     
50D0: 3C         INC     A               
50D1: 00         NOP                     
50D2: F0 00      LD      A,($00)         
50D4: C3 00 0E   JP      $0E00           
50D7: 00         NOP                     
50D8: 3C         INC     A               
50D9: 0C         INC     C               
50DA: FF         RST     0X38            
50DB: 3F         CCF                     
50DC: FF         RST     0X38            
50DD: FF         RST     0X38            
50DE: FF         RST     0X38            
50DF: FF         RST     0X38            
50E0: 0E 01      LD      C,$01           
50E2: 70         LD      (HL),B          
50E3: 00         NOP                     
50E4: FC         ???                     
50E5: 00         NOP                     
50E6: FF         RST     0X38            
50E7: 00         NOP                     
50E8: 3F         CCF                     
50E9: 00         NOP                     
50EA: 03         INC     BC              
50EB: 00         NOP                     
50EC: E0 E0      LDFF00  ($E0),A         
50EE: FF         RST     0X38            
50EF: FF         RST     0X38            
50F0: 03         INC     BC              
50F1: F8 00      LDHL    SP,$00          
50F3: 00         NOP                     
50F4: 00         NOP                     
50F5: 00         NOP                     
50F6: 80         ADD     A,B             
50F7: 00         NOP                     
50F8: FC         ???                     
50F9: 00         NOP                     
50FA: E1         POP     HL              
50FB: 00         NOP                     
50FC: 1F         RRA                     
50FD: 00         NOP                     
50FE: FE 00      CP      $00             
5100: 00         NOP                     
5101: 00         NOP                     
5102: 00         NOP                     
5103: 00         NOP                     
5104: FF         RST     0X38            
5105: 00         NOP                     
5106: EF         RST     0X28            
5107: 10 10      STOP    $10             
5109: EF         RST     0X28            
510A: 80         ADD     A,B             
510B: 7F         LD      A,A             
510C: 00         NOP                     
510D: F3         DI                      
510E: 00         NOP                     
510F: C0         RET     NZ              
5110: 00         NOP                     
5111: 00         NOP                     
5112: 00         NOP                     
5113: 00         NOP                     
5114: C0         RET     NZ              
5115: 3F         CCF                     
5116: 07         RLCA                    
5117: F8 7F      LDHL    SP,$7F          
5119: 80         ADD     A,B             
511A: FE 01      CP      $01             
511C: 3F         CCF                     
511D: C0         RET     NZ              
511E: 0F         RRCA                    
511F: F0 00      LD      A,($00)         
5121: 00         NOP                     
5122: 00         NOP                     
5123: 00         NOP                     
5124: 7F         LD      A,A             
5125: 80         ADD     A,B             
5126: 0E F1      LD      C,$F1           
5128: F0 0F      LD      A,($0F)         
512A: 03         INC     BC              
512B: FC         ???                     
512C: 9F         SBC     A               
512D: 60         LD      H,B             
512E: FF         RST     0X38            
512F: 00         NOP                     
5130: 00         NOP                     
5131: 00         NOP                     
5132: 00         NOP                     
5133: 00         NOP                     
5134: C7         RST     0X00            
5135: 38 01      JR      C,$5138         
5137: FE 3C      CP      $3C             
5139: C3 FF 00   JP      $00FF           
513C: FF         RST     0X38            
513D: 00         NOP                     
513E: FE 01      CP      $01             
5140: E0 00      LDFF00  ($00),A         
5142: F3         DI                      
5143: 00         NOP                     
5144: 1F         RRA                     
5145: 00         NOP                     
5146: 78         LD      A,B             
5147: 00         NOP                     
5148: C0         RET     NZ              
5149: 00         NOP                     
514A: 07         RLCA                    
514B: 00         NOP                     
514C: FF         RST     0X38            
514D: 00         NOP                     
514E: FF         RST     0X38            
514F: 3F         CCF                     
5150: 00         NOP                     
5151: 0F         RRCA                    
5152: E0 00      LDFF00  ($00),A         
5154: 03         INC     BC              
5155: 00         NOP                     
5156: 0E 00      LD      C,$00           
5158: 3C         INC     A               
5159: 0C         INC     C               
515A: FF         RST     0X38            
515B: 3F         CCF                     
515C: FF         RST     0X38            
515D: FF         RST     0X38            
515E: FF         RST     0X38            
515F: FF         RST     0X38            
5160: 0F         RRCA                    
5161: 80         ADD     A,B             
5162: 72         LD      (HL),D          
5163: 01 FC 00   LD      BC,$00FC        
5166: FF         RST     0X38            
5167: 00         NOP                     
5168: 3F         CCF                     
5169: 00         NOP                     
516A: 03         INC     BC              
516B: 00         NOP                     
516C: E0 E0      LDFF00  ($E0),A         
516E: FF         RST     0X38            
516F: FF         RST     0X38            
5170: F0 0F      LD      A,($0F)         
5172: 00         NOP                     
5173: F8 00      LDHL    SP,$00          
5175: 00         NOP                     
5176: 80         ADD     A,B             
5177: 00         NOP                     
5178: FC         ???                     
5179: 00         NOP                     
517A: E1         POP     HL              
517B: 00         NOP                     
517C: 1F         RRA                     
517D: 00         NOP                     
517E: FE 00      CP      $00             
5180: 00         NOP                     
5181: 00         NOP                     
5182: 00         NOP                     
5183: 00         NOP                     
5184: 00         NOP                     
5185: 00         NOP                     
5186: FF         RST     0X38            
5187: 00         NOP                     
5188: EF         RST     0X28            
5189: 10 10      STOP    $10             
518B: EF         RST     0X28            
518C: 80         ADD     A,B             
518D: 7F         LD      A,A             
518E: 00         NOP                     
518F: F3         DI                      
5190: 00         NOP                     
5191: 00         NOP                     
5192: 00         NOP                     
5193: 00         NOP                     
5194: 00         NOP                     
5195: 00         NOP                     
5196: C0         RET     NZ              
5197: 3F         CCF                     
5198: 07         RLCA                    
5199: F8 7F      LDHL    SP,$7F          
519B: 80         ADD     A,B             
519C: FE 01      CP      $01             
519E: 3F         CCF                     
519F: C0         RET     NZ              
51A0: 00         NOP                     
51A1: 00         NOP                     
51A2: 00         NOP                     
51A3: 00         NOP                     
51A4: 00         NOP                     
51A5: 00         NOP                     
51A6: 7F         LD      A,A             
51A7: 80         ADD     A,B             
51A8: 0E F1      LD      C,$F1           
51AA: F0 0F      LD      A,($0F)         
51AC: 03         INC     BC              
51AD: FC         ???                     
51AE: 9F         SBC     A               
51AF: 60         LD      H,B             
51B0: 00         NOP                     
51B1: 00         NOP                     
51B2: 00         NOP                     
51B3: 00         NOP                     
51B4: 00         NOP                     
51B5: 00         NOP                     
51B6: C7         RST     0X00            
51B7: 38 01      JR      C,$51BA         
51B9: FE 3C      CP      $3C             
51BB: C3 FF 00   JP      $00FF           
51BE: FF         RST     0X38            
51BF: 00         NOP                     
51C0: 00         NOP                     
51C1: C0         RET     NZ              
51C2: F0 00      LD      A,($00)         
51C4: 3F         CCF                     
51C5: 00         NOP                     
51C6: 78         LD      A,B             
51C7: 00         NOP                     
51C8: E0 00      LDFF00  ($00),A         
51CA: 07         RLCA                    
51CB: 00         NOP                     
51CC: FF         RST     0X38            
51CD: 00         NOP                     
51CE: FF         RST     0X38            
51CF: 3F         CCF                     
51D0: 0F         RRCA                    
51D1: F0 40      LD      A,($40)         
51D3: 0C         INC     C               
51D4: 83         ADD     A,E             
51D5: 00         NOP                     
51D6: 0E 00      LD      C,$00           
51D8: 3C         INC     A               
51D9: 0C         INC     C               
51DA: FF         RST     0X38            
51DB: 3F         CCF                     
51DC: FF         RST     0X38            
51DD: FF         RST     0X38            
51DE: FF         RST     0X38            
51DF: FF         RST     0X38            
51E0: 8F         ADC     A,A             
51E1: 00         NOP                     
51E2: 73         LD      (HL),E          
51E3: 00         NOP                     
51E4: FC         ???                     
51E5: 00         NOP                     
51E6: FF         RST     0X38            
51E7: 00         NOP                     
51E8: 3F         CCF                     
51E9: 00         NOP                     
51EA: 03         INC     BC              
51EB: 00         NOP                     
51EC: E0 E0      LDFF00  ($E0),A         
51EE: FF         RST     0X38            
51EF: FF         RST     0X38            
51F0: FE 01      CP      $01             
51F2: F0 0F      LD      A,($0F)         
51F4: 00         NOP                     
51F5: 78         LD      A,B             
51F6: 80         ADD     A,B             
51F7: 00         NOP                     
51F8: FC         ???                     
51F9: 00         NOP                     
51FA: E1         POP     HL              
51FB: 00         NOP                     
51FC: 1F         RRA                     
51FD: 00         NOP                     
51FE: FE 00      CP      $00             
5200: 00         NOP                     
5201: 00         NOP                     
5202: 0F         RRCA                    
5203: 00         NOP                     
5204: 3F         CCF                     
5205: 00         NOP                     
5206: FF         RST     0X38            
5207: 00         NOP                     
5208: F8 07      LDHL    SP,$07          
520A: E0 1F      LDFF00  ($1F),A         
520C: 80         ADD     A,B             
520D: 7F         LD      A,A             
520E: 00         NOP                     
520F: C6 00      ADD     $00             
5211: 20 03      JR      NZ,$5216        
5213: 00         NOP                     
5214: CF         RST     0X08            
5215: 00         NOP                     
5216: FF         RST     0X38            
5217: 00         NOP                     
5218: FE 01      CP      $01             
521A: 78         LD      A,B             
521B: 87         ADD     A,A             
521C: 00         NOP                     
521D: F8 00      LDHL    SP,$00          
521F: 78         LD      A,B             
5220: 7C         LD      A,H             
5221: 00         NOP                     
5222: FE 00      CP      $00             
5224: FF         RST     0X38            
5225: 00         NOP                     
5226: FF         RST     0X38            
5227: 00         NOP                     
5228: 03         INC     BC              
5229: FC         ???                     
522A: 00         NOP                     
522B: 07         RLCA                    
522C: 00         NOP                     
522D: 07         RLCA                    
522E: 00         NOP                     
522F: 0D         DEC     C               
5230: 00         NOP                     
5231: 40         LD      B,B             
5232: 00         NOP                     
5233: 00         NOP                     
5234: 80         ADD     A,B             
5235: 00         NOP                     
5236: FF         RST     0X38            
5237: 00         NOP                     
5238: FF         RST     0X38            
5239: 00         NOP                     
523A: 7F         LD      A,A             
523B: 80         ADD     A,B             
523C: 0F         RRCA                    
523D: F0 00      LD      A,($00)         
523F: 9F         SBC     A               
5240: 00         NOP                     
5241: 86         ADD     A,(HL)          
5242: 00         NOP                     
5243: FC         ???                     
5244: 00         NOP                     
5245: CC 00 6F   CALL    Z,$6F00         
5248: 00         NOP                     
5249: 3C         INC     A               
524A: 00         NOP                     
524B: 04         INC     B               
524C: 00         NOP                     
524D: 03         INC     BC              
524E: 00         NOP                     
524F: 00         NOP                     
5250: 00         NOP                     
5251: 7C         LD      A,H             
5252: 00         NOP                     
5253: 3F         CCF                     
5254: 00         NOP                     
5255: E1         POP     HL              
5256: 00         NOP                     
5257: E0 00      LDFF00  ($00),A         
5259: DB         ???                     
525A: 00         NOP                     
525B: 8F         ADC     A,A             
525C: 00         NOP                     
525D: 00         NOP                     
525E: 00         NOP                     
525F: 00         NOP                     
5260: 00         NOP                     
5261: 78         LD      A,B             
5262: 00         NOP                     
5263: E0 00      LDFF00  ($00),A         
5265: FF         RST     0X38            
5266: 00         NOP                     
5267: C3 00 80   JP      $8000           
526A: 00         NOP                     
526B: 00         NOP                     
526C: 00         NOP                     
526D: 00         NOP                     
526E: 00         NOP                     
526F: 00         NOP                     
5270: 00         NOP                     
5271: 99         SBC     C               
5272: 00         NOP                     
5273: E9         JP      (HL)            
5274: 00         NOP                     
5275: 07         RLCA                    
5276: 00         NOP                     
5277: 03         INC     BC              
5278: 00         NOP                     
5279: 00         NOP                     
527A: 00         NOP                     
527B: 00         NOP                     
527C: 00         NOP                     
527D: 00         NOP                     
527E: 00         NOP                     
527F: 00         NOP                     
5280: 00         NOP                     
5281: 00         NOP                     
5282: 0F         RRCA                    
5283: 00         NOP                     
5284: 3F         CCF                     
5285: 00         NOP                     
5286: F8 07      LDHL    SP,$07          
5288: E0 1F      LDFF00  ($1F),A         
528A: 80         ADD     A,B             
528B: 7C         LD      A,H             
528C: 00         NOP                     
528D: 88         ADC     A,B             
528E: 00         NOP                     
528F: 08 00 20   LD      ($2000),SP      
5292: 03         INC     BC              
5293: 00         NOP                     
5294: CF         RST     0X08            
5295: 00         NOP                     
5296: FE 01      CP      $01             
5298: 78         LD      A,B             
5299: 87         ADD     A,A             
529A: 00         NOP                     
529B: FE 00      CP      $00             
529D: FC         ???                     
529E: 00         NOP                     
529F: 3F         CCF                     
52A0: 7C         LD      A,H             
52A1: 00         NOP                     
52A2: FE 00      CP      $00             
52A4: FF         RST     0X38            
52A5: 00         NOP                     
52A6: 03         INC     BC              
52A7: FC         ???                     
52A8: 00         NOP                     
52A9: 87         ADD     A,A             
52AA: 00         NOP                     
52AB: 07         RLCA                    
52AC: 00         NOP                     
52AD: 7C         LD      A,H             
52AE: 00         NOP                     
52AF: F8 00      LDHL    SP,$00          
52B1: 40         LD      B,B             
52B2: 00         NOP                     
52B3: 00         NOP                     
52B4: 80         ADD     A,B             
52B5: 00         NOP                     
52B6: FF         RST     0X38            
52B7: 00         NOP                     
52B8: 7F         LD      A,A             
52B9: 80         ADD     A,B             
52BA: 0F         RRCA                    
52BB: F0 00      LD      A,($00)         
52BD: DF         RST     0X18            
52BE: 00         NOP                     
52BF: 99         SBC     C               
52C0: 00         NOP                     
52C1: FC         ???                     
52C2: 00         NOP                     
52C3: 73         LD      (HL),E          
52C4: 00         NOP                     
52C5: 3A         LD      A,(HLD)         
52C6: 00         NOP                     
52C7: 06 00      LD      B,$00           
52C9: 03         INC     BC              
52CA: 00         NOP                     
52CB: 00         NOP                     
52CC: 00         NOP                     
52CD: 00         NOP                     
52CE: 00         NOP                     
52CF: 00         NOP                     
52D0: 00         NOP                     
52D1: F1         POP     AF              
52D2: 00         NOP                     
52D3: F0 00      LD      A,($00)         
52D5: D9         RETI                    
52D6: 00         NOP                     
52D7: 8F         ADC     A,A             
52D8: 00         NOP                     
52D9: 00         NOP                     
52DA: 00         NOP                     
52DB: 00         NOP                     
52DC: 00         NOP                     
52DD: 00         NOP                     
52DE: 00         NOP                     
52DF: 00         NOP                     
52E0: 00         NOP                     
52E1: FF         RST     0X38            
52E2: 00         NOP                     
52E3: C3 00 80   JP      $8000           
52E6: 00         NOP                     
52E7: 00         NOP                     
52E8: 00         NOP                     
52E9: 00         NOP                     
52EA: 00         NOP                     
52EB: 00         NOP                     
52EC: 00         NOP                     
52ED: 00         NOP                     
52EE: 00         NOP                     
52EF: 00         NOP                     
52F0: 00         NOP                     
52F1: 07         RLCA                    
52F2: 00         NOP                     
52F3: 03         INC     BC              
52F4: 00         NOP                     
52F5: 00         NOP                     
52F6: 00         NOP                     
52F7: 00         NOP                     
52F8: 00         NOP                     
52F9: 00         NOP                     
52FA: 00         NOP                     
52FB: 00         NOP                     
52FC: 00         NOP                     
52FD: 00         NOP                     
52FE: 00         NOP                     
52FF: 00         NOP                     
5300: 00         NOP                     
5301: 00         NOP                     
5302: 0F         RRCA                    
5303: 00         NOP                     
5304: 38 07      JR      C,$530D         
5306: E0 1C      LDFF00  ($1C),A         
5308: 80         ADD     A,B             
5309: 78         LD      A,B             
530A: 00         NOP                     
530B: C8         RET     Z               
530C: 00         NOP                     
530D: 8C         ADC     A,H             
530E: 00         NOP                     
530F: F3         DI                      
5310: 00         NOP                     
5311: 20 03      JR      NZ,$5316        
5313: 00         NOP                     
5314: CE 01      ADC     $01             
5316: 30 CF      JR      NC,$52E7        
5318: 00         NOP                     
5319: 3E 00      LD      A,$00           
531B: 37         SCF                     
531C: 00         NOP                     
531D: F8 00      LDHL    SP,$00          
531F: F8 7C      LDHL    SP,$7C          
5321: 00         NOP                     
5322: FE 00      CP      $00             
5324: 03         INC     BC              
5325: FC         ???                     
5326: 00         NOP                     
5327: 0F         RRCA                    
5328: 00         NOP                     
5329: 0C         INC     C               
532A: 00         NOP                     
532B: FF         RST     0X38            
532C: 00         NOP                     
532D: 78         LD      A,B             
532E: 00         NOP                     
532F: 60         LD      H,B             
5330: 00         NOP                     
5331: 40         LD      B,B             
5332: 00         NOP                     
5333: 00         NOP                     
5334: 80         ADD     A,B             
5335: 00         NOP                     
5336: 7F         LD      A,A             
5337: 80         ADD     A,B             
5338: 07         RLCA                    
5339: F8 00      LDHL    SP,$00          
533B: DF         RST     0X18            
533C: 00         NOP                     
533D: 75         LD      (HL),L          
533E: 00         NOP                     
533F: 33         INC     SP              
5340: 00         NOP                     
5341: 1A         LD      A,(DE)          
5342: 00         NOP                     
5343: 07         RLCA                    
5344: 00         NOP                     
5345: 00         NOP                     
5346: 00         NOP                     
5347: 00         NOP                     
5348: 00         NOP                     
5349: 00         NOP                     
534A: 00         NOP                     
534B: 00         NOP                     
534C: 00         NOP                     
534D: 00         NOP                     
534E: 00         NOP                     
534F: 00         NOP                     
5350: 00         NOP                     
5351: CC 00 87   CALL    Z,$8700         
5354: 00         NOP                     
5355: 00         NOP                     
5356: 00         NOP                     
5357: 00         NOP                     
5358: 00         NOP                     
5359: 00         NOP                     
535A: 00         NOP                     
535B: 00         NOP                     
535C: 00         NOP                     
535D: 00         NOP                     
535E: 00         NOP                     
535F: 00         NOP                     
5360: 00         NOP                     
5361: C0         RET     NZ              
5362: 00         NOP                     
5363: 80         ADD     A,B             
5364: 00         NOP                     
5365: 00         NOP                     
5366: 00         NOP                     
5367: 00         NOP                     
5368: 00         NOP                     
5369: 00         NOP                     
536A: 00         NOP                     
536B: 00         NOP                     
536C: 00         NOP                     
536D: 00         NOP                     
536E: 00         NOP                     
536F: 00         NOP                     
5370: 00         NOP                     
5371: 00         NOP                     
5372: 00         NOP                     
5373: 00         NOP                     
5374: 00         NOP                     
5375: 00         NOP                     
5376: 00         NOP                     
5377: 00         NOP                     
5378: 00         NOP                     
5379: 00         NOP                     
537A: 00         NOP                     
537B: 00         NOP                     
537C: 00         NOP                     
537D: 00         NOP                     
537E: 00         NOP                     
537F: 00         NOP                     
5380: 00         NOP                     
5381: 00         NOP                     
5382: 00         NOP                     
5383: 07         RLCA                    
5384: 00         NOP                     
5385: 3F         CCF                     
5386: 00         NOP                     
5387: C8         RET     Z               
5388: 00         NOP                     
5389: 8B         ADC     A,E             
538A: 00         NOP                     
538B: 7C         LD      A,H             
538C: 00         NOP                     
538D: 1E 00      LD      E,$00           
538F: 03         INC     BC              
5390: 00         NOP                     
5391: 20 00      JR      NZ,$5393        
5393: 01 00 CF   LD      BC,$CF00        
5396: 00         NOP                     
5397: 7F         LD      A,A             
5398: 00         NOP                     
5399: FC         ???                     
539A: 00         NOP                     
539B: F8 00      LDHL    SP,$00          
539D: CD 00 07   CALL    $0700           
53A0: 00         NOP                     
53A1: 00         NOP                     
53A2: 00         NOP                     
53A3: FC         ???                     
53A4: 00         NOP                     
53A5: 07         RLCA                    
53A6: 00         NOP                     
53A7: FE 00      CP      $00             
53A9: 5E         LD      E,(HL)          
53AA: 00         NOP                     
53AB: 63         LD      H,E             
53AC: 00         NOP                     
53AD: C0         RET     NZ              
53AE: 00         NOP                     
53AF: 00         NOP                     
53B0: 00         NOP                     
53B1: 40         LD      B,B             
53B2: 00         NOP                     
53B3: 00         NOP                     
53B4: 00         NOP                     
53B5: 80         ADD     A,B             
53B6: 00         NOP                     
53B7: FF         RST     0X38            
53B8: 00         NOP                     
53B9: EA 00 C7   LD      ($C700),A       
53BC: 00         NOP                     
53BD: 00         NOP                     
53BE: 00         NOP                     
53BF: 00         NOP                     
53C0: 00         NOP                     
53C1: 00         NOP                     
53C2: 00         NOP                     
53C3: 00         NOP                     
53C4: 00         NOP                     
53C5: 00         NOP                     
53C6: 00         NOP                     
53C7: 00         NOP                     
53C8: 00         NOP                     
53C9: 00         NOP                     
53CA: 00         NOP                     
53CB: 00         NOP                     
53CC: 00         NOP                     
53CD: 00         NOP                     
53CE: 00         NOP                     
53CF: 00         NOP                     
53D0: 00         NOP                     
53D1: 00         NOP                     
53D2: 00         NOP                     
53D3: 00         NOP                     
53D4: 00         NOP                     
53D5: 00         NOP                     
53D6: 00         NOP                     
53D7: 00         NOP                     
53D8: 00         NOP                     
53D9: 00         NOP                     
53DA: 00         NOP                     
53DB: 00         NOP                     
53DC: 00         NOP                     
53DD: 00         NOP                     
53DE: 00         NOP                     
53DF: 00         NOP                     
53E0: 00         NOP                     
53E1: 00         NOP                     
53E2: 00         NOP                     
53E3: 00         NOP                     
53E4: 00         NOP                     
53E5: 00         NOP                     
53E6: 00         NOP                     
53E7: 00         NOP                     
53E8: 00         NOP                     
53E9: 00         NOP                     
53EA: 00         NOP                     
53EB: 00         NOP                     
53EC: 00         NOP                     
53ED: 00         NOP                     
53EE: 00         NOP                     
53EF: 00         NOP                     
53F0: 00         NOP                     
53F1: 00         NOP                     
53F2: 00         NOP                     
53F3: 00         NOP                     
53F4: 00         NOP                     
53F5: 00         NOP                     
53F6: 00         NOP                     
53F7: 00         NOP                     
53F8: 00         NOP                     
53F9: 00         NOP                     
53FA: 00         NOP                     
53FB: 00         NOP                     
53FC: 00         NOP                     
53FD: 00         NOP                     
53FE: 00         NOP                     
53FF: 00         NOP                     
5400: 00         NOP                     
5401: 00         NOP                     
5402: 01 00 06   LD      BC,$0600        
5405: 01 08 07   LD      BC,$0708        
5408: 38 07      JR      C,$5411         
540A: 20 1F      JR      NZ,$542B        
540C: 2E 11      LD      L,$11           
540E: 1E 05      LD      E,$05           
5410: 2B         DEC     HL              
5411: 16 45      LD      D,$45           
5413: 3B         DEC     SP              
5414: 82         ADD     A,D             
5415: 7D         LD      A,L             
5416: 87         ADD     A,A             
5417: 78         LD      A,B             
5418: 79         LD      A,C             
5419: 06 11      LD      B,$11           
541B: 0E 20      LD      C,$20           
541D: 1F         RRA                     
541E: 3F         CCF                     
541F: 00         NOP                     
5420: 00         NOP                     
5421: 00         NOP                     
5422: F0 00      LD      A,($00)         
5424: 6E         LD      L,(HL)          
5425: F0 05      LD      A,($05)         
5427: FE 1D      CP      $1D             
5429: E2         LDFF00  (C),A           
542A: 3E D0      LD      A,$D0           
542C: F8 10      LDHL    SP,$10          
542E: F8 50      LDHL    SP,$50          
5430: FC         ???                     
5431: 58         LD      E,B             
5432: FC         ???                     
5433: F8 78      LDHL    SP,$78          
5435: F0 F0      LD      A,($F0)         
5437: 00         NOP                     
5438: E0 C0      LDFF00  ($C0),A         
543A: F0 C0      LD      A,($C0)         
543C: C8         RET     Z               
543D: 30 F8      JR      NC,$5437        
543F: 00         NOP                     
5440: 01 00 06   LD      BC,$0600        
5443: 01 08 07   LD      BC,$0708        
5446: 38 07      JR      C,$544F         
5448: 20 1F      JR      NZ,$5469        
544A: 2E 11      LD      L,$11           
544C: 1E 05      LD      E,$05           
544E: 1B         DEC     DE              
544F: 06 25      LD      B,$25           
5451: 1B         DEC     DE              
5452: 22         LD      (HLI),A         
5453: 1D         DEC     E               
5454: 43         LD      B,E             
5455: 3C         INC     A               
5456: 47         LD      B,A             
5457: 38 3D      JR      C,$5496         
5459: 02         LD      (BC),A          
545A: 08 07 10   LD      ($1007),SP      
545D: 0F         RRCA                    
545E: 1F         RRA                     
545F: 00         NOP                     
5460: F0 00      LD      A,($00)         
5462: 6C         LD      L,H             
5463: F0 06      LD      A,($06)         
5465: FC         ???                     
5466: 1A         LD      A,(DE)          
5467: E4         ???                     
5468: 3E D0      LD      A,$D0           
546A: F8 10      LDHL    SP,$10          
546C: F8 50      LDHL    SP,$50          
546E: FC         ???                     
546F: 58         LD      E,B             
5470: FC         ???                     
5471: F8 78      LDHL    SP,$78          
5473: F0 F0      LD      A,($F0)         
5475: 00         NOP                     
5476: E0 C0      LDFF00  ($C0),A         
5478: E0 C0      LDFF00  ($C0),A         
547A: E0 00      LDFF00  ($00),A         
547C: 10 E0      STOP    $E0             
547E: F0 00      LD      A,($00)         
5480: 01 00 1E   LD      BC,$1E00        
5483: 01 10 0F   LD      BC,$0F10        
5486: 10 0F      STOP    $0F             
5488: 16 09      LD      D,$09           
548A: 0F         RRCA                    
548B: 02         LD      (BC),A          
548C: 17         RLA                     
548D: 0A         LD      A,(BC)          
548E: 27         DAA                     
548F: 1B         DEC     DE              
5490: 27         DAA                     
5491: 19         ADD     HL,DE           
5492: 42         LD      B,D             
5493: 3D         DEC     A               
5494: 43         LD      B,E             
5495: 3C         INC     A               
5496: 27         DAA                     
5497: 18 1C      JR      $54B5           
5499: 03         INC     BC              
549A: 08 07 10   LD      ($1007),SP      
549D: 0F         RRCA                    
549E: 1F         RRA                     
549F: 00         NOP                     
54A0: E0 00      LDFF00  ($00),A         
54A2: 78         LD      A,B             
54A3: E0 04      LDFF00  ($04),A         
54A5: F8 06      LDHL    SP,$06          
54A7: FC         ???                     
54A8: 0A         LD      A,(BC)          
54A9: F4         ???                     
54AA: 1A         LD      A,(DE)          
54AB: E4         ???                     
54AC: 7C         LD      A,H             
54AD: 90         SUB     B               
54AE: F8 50      LDHL    SP,$50          
54B0: FC         ???                     
54B1: D8         RET     C               
54B2: FC         ???                     
54B3: F8 78      LDHL    SP,$78          
54B5: E0 F0      LDFF00  ($F0),A         
54B7: 00         NOP                     
54B8: 58         LD      E,B             
54B9: B0         OR      B               
54BA: 78         LD      A,B             
54BB: B0         OR      B               
54BC: 30 C0      JR      NC,$547E        
54BE: F0 00      LD      A,($00)         
54C0: 00         NOP                     
54C1: 00         NOP                     
54C2: 0F         RRCA                    
54C3: 00         NOP                     
54C4: 08 07 08   LD      ($0807),SP      
54C7: 07         RLCA                    
54C8: 0B         DEC     BC              
54C9: 04         INC     B               
54CA: 07         RLCA                    
54CB: 01 0B 05   LD      BC,$050B        
54CE: 13         INC     DE              
54CF: 0D         DEC     C               
54D0: 13         INC     DE              
54D1: 0C         INC     C               
54D2: 21 1E 21   LD      HL,$211E        
54D5: 1E 13      LD      E,$13           
54D7: 0C         INC     C               
54D8: 0E 01      LD      C,$01           
54DA: 08 07 10   LD      ($1007),SP      
54DD: 0F         RRCA                    
54DE: 1F         RRA                     
54DF: 00         NOP                     
54E0: F0 00      LD      A,($00)         
54E2: 3C         INC     A               
54E3: F0 02      LD      A,($02)         
54E5: FC         ???                     
54E6: 03         INC     BC              
54E7: FE 05      CP      $05             
54E9: FA 8D 72   LD      A,($728D)       
54EC: BE         CP      (HL)            
54ED: 48         LD      C,B             
54EE: FC         ???                     
54EF: A8         XOR     B               
54F0: FE EC      CP      $EC             
54F2: 7E         LD      A,(HL)          
54F3: FC         ???                     
54F4: BC         CP      H               
54F5: 70         LD      (HL),B          
54F6: F8 00      LDHL    SP,$00          
54F8: 2C         INC     L               
54F9: D8         RET     C               
54FA: 3C         INC     A               
54FB: D8         RET     C               
54FC: 38 C0      JR      C,$54BE         
54FE: F0 00      LD      A,($00)         
5500: 0F         RRCA                    
5501: 00         NOP                     
5502: 7F         LD      A,A             
5503: 07         RLCA                    
5504: FF         RST     0X38            
5505: 00         NOP                     
5506: 7F         LD      A,A             
5507: 07         RLCA                    
5508: FF         RST     0X38            
5509: 0C         INC     C               
550A: 7F         LD      A,A             
550B: 17         RLA                     
550C: 2F         CPL                     
550D: 1D         DEC     E               
550E: 16 0F      LD      D,$0F           
5510: 3F         CCF                     
5511: 00         NOP                     
5512: 54         LD      D,H             
5513: 3B         DEC     SP              
5514: 7B         LD      A,E             
5515: 37         SCF                     
5516: 38 07      JR      C,$551F         
5518: 3F         CCF                     
5519: 18 2F      JR      $554A           
551B: 1C         INC     E               
551C: 17         RLA                     
551D: 0C         INC     C               
551E: 0E 01      LD      C,$01           
5520: C0         RET     NZ              
5521: 00         NOP                     
5522: B0         OR      B               
5523: 40         LD      B,B             
5524: F8 90      LDHL    SP,$90          
5526: F8 30      LDHL    SP,$30          
5528: F4         ???                     
5529: A8         XOR     B               
552A: B2         OR      D               
552B: EC         ???                     
552C: A2         AND     D               
552D: DC FC 00   CALL    C,$00FC         
5530: 24         INC     H               
5531: D8         RET     C               
5532: 1E EC      LD      E,$EC           
5534: DE EC      SBC     $EC             
5536: 1C         INC     E               
5537: E0 FE      LDFF00  ($FE),A         
5539: 0C         INC     C               
553A: FA 1C F4   LD      A,($F41C)       
553D: 18 38      JR      $5577           
553F: 00         NOP                     
5540: 07         RLCA                    
5541: 00         NOP                     
5542: 0F         RRCA                    
5543: 00         NOP                     
5544: 1F         RRA                     
5545: 00         NOP                     
5546: 3F         CCF                     
5547: 13         INC     DE              
5548: 3F         CCF                     
5549: 14         INC     D               
554A: 27         DAA                     
554B: 1F         RRA                     
554C: 17         RLA                     
554D: 0F         RRCA                    
554E: 0D         DEC     C               
554F: 03         INC     BC              
5550: 1B         DEC     DE              
5551: 04         INC     B               
5552: 2E 19      LD      L,$19           
5554: 3D         DEC     A               
5555: 1B         DEC     DE              
5556: 1C         INC     E               
5557: 03         INC     BC              
5558: 17         RLA                     
5559: 0C         INC     C               
555A: 1F         RRA                     
555B: 0C         INC     C               
555C: 17         RLA                     
555D: 0C         INC     C               
555E: 0E 01      LD      C,$01           
5560: F0 00      LD      A,($00)         
5562: C8         RET     Z               
5563: 30 E4      JR      NC,$5549        
5565: 18 FE      JR      $5565           
5567: E4         ???                     
5568: FE 94      CP      $94             
556A: F2         ???                     
556B: FC         ???                     
556C: EE 70      XOR     $70             
556E: DC E0 F6   CALL    C,$F6E0         
5571: 08 0B F6   LD      ($F60B),SP      
5574: EB         ???                     
5575: F6 0E      OR      $0E             
5577: F0 FE      LD      A,($FE)         
5579: 00         NOP                     
557A: FD         ???                     
557B: 0E FA      LD      C,$FA           
557D: 1D         DEC     E               
557E: 3C         INC     A               
557F: 02         LD      (BC),A          
5580: 00         NOP                     
5581: 00         NOP                     
5582: 00         NOP                     
5583: 00         NOP                     
5584: 44         LD      B,H             
5585: 44         LD      B,H             
5586: 28 28      JR      Z,$55B0         
5588: 10 10      STOP    $10             
558A: 28 28      JR      Z,$55B4         
558C: 44         LD      B,H             
558D: 44         LD      B,H             
558E: 00         NOP                     
558F: 00         NOP                     
5590: 00         NOP                     
5591: 00         NOP                     
5592: 00         NOP                     
5593: 00         NOP                     
5594: 44         LD      B,H             
5595: 44         LD      B,H             
5596: 28 28      JR      Z,$55C0         
5598: 10 10      STOP    $10             
559A: 28 28      JR      Z,$55C4         
559C: 44         LD      B,H             
559D: 44         LD      B,H             
559E: 00         NOP                     
559F: 00         NOP                     
55A0: 00         NOP                     
55A1: 00         NOP                     
55A2: 00         NOP                     
55A3: 00         NOP                     
55A4: 44         LD      B,H             
55A5: 44         LD      B,H             
55A6: 28 28      JR      Z,$55D0         
55A8: 10 10      STOP    $10             
55AA: 28 28      JR      Z,$55D4         
55AC: 44         LD      B,H             
55AD: 44         LD      B,H             
55AE: 00         NOP                     
55AF: 00         NOP                     
55B0: 00         NOP                     
55B1: 00         NOP                     
55B2: 00         NOP                     
55B3: 00         NOP                     
55B4: 44         LD      B,H             
55B5: 44         LD      B,H             
55B6: 28 28      JR      Z,$55E0         
55B8: 10 10      STOP    $10             
55BA: 28 28      JR      Z,$55E4         
55BC: 44         LD      B,H             
55BD: 44         LD      B,H             
55BE: 00         NOP                     
55BF: 00         NOP                     
55C0: 00         NOP                     
55C1: 00         NOP                     
55C2: 00         NOP                     
55C3: 00         NOP                     
55C4: 00         NOP                     
55C5: 00         NOP                     
55C6: 00         NOP                     
55C7: 00         NOP                     
55C8: 00         NOP                     
55C9: 00         NOP                     
55CA: 00         NOP                     
55CB: 00         NOP                     
55CC: 00         NOP                     
55CD: 00         NOP                     
55CE: 00         NOP                     
55CF: 00         NOP                     
55D0: 00         NOP                     
55D1: 00         NOP                     
55D2: 00         NOP                     
55D3: 00         NOP                     
55D4: 00         NOP                     
55D5: 00         NOP                     
55D6: 01 00 00   LD      BC,$0000        
55D9: 00         NOP                     
55DA: 04         INC     B               
55DB: 00         NOP                     
55DC: 08 00 00   LD      ($0000),SP      
55DF: 00         NOP                     
55E0: 00         NOP                     
55E1: 00         NOP                     
55E2: 00         NOP                     
55E3: 00         NOP                     
55E4: 00         NOP                     
55E5: 00         NOP                     
55E6: 00         NOP                     
55E7: 00         NOP                     
55E8: 00         NOP                     
55E9: 00         NOP                     
55EA: 00         NOP                     
55EB: 00         NOP                     
55EC: 00         NOP                     
55ED: 00         NOP                     
55EE: 00         NOP                     
55EF: 00         NOP                     
55F0: 00         NOP                     
55F1: 00         NOP                     
55F2: 40         LD      B,B             
55F3: 00         NOP                     
55F4: 40         LD      B,B             
55F5: 00         NOP                     
55F6: 40         LD      B,B             
55F7: 00         NOP                     
55F8: 40         LD      B,B             
55F9: 00         NOP                     
55FA: 40         LD      B,B             
55FB: 00         NOP                     
55FC: 40         LD      B,B             
55FD: 00         NOP                     
55FE: C0         RET     NZ              
55FF: 00         NOP                     
5600: 00         NOP                     
5601: 00         NOP                     
5602: 00         NOP                     
5603: 00         NOP                     
5604: 00         NOP                     
5605: 00         NOP                     
5606: 00         NOP                     
5607: 00         NOP                     
5608: 00         NOP                     
5609: 00         NOP                     
560A: 04         INC     B               
560B: 00         NOP                     
560C: C8         RET     Z               
560D: 00         NOP                     
560E: 38 00      JR      C,$5610         
5610: 1F         RRA                     
5611: 00         NOP                     
5612: 1F         RRA                     
5613: 00         NOP                     
5614: 0F         RRCA                    
5615: 00         NOP                     
5616: 07         RLCA                    
5617: 00         NOP                     
5618: 03         INC     BC              
5619: 00         NOP                     
561A: 00         NOP                     
561B: 00         NOP                     
561C: 00         NOP                     
561D: 00         NOP                     
561E: 00         NOP                     
561F: 00         NOP                     
5620: 1F         RRA                     
5621: 00         NOP                     
5622: 5F         LD      E,A             
5623: 00         NOP                     
5624: 87         ADD     A,A             
5625: 00         NOP                     
5626: 00         NOP                     
5627: 00         NOP                     
5628: 00         NOP                     
5629: 00         NOP                     
562A: 00         NOP                     
562B: 00         NOP                     
562C: 00         NOP                     
562D: 00         NOP                     
562E: 00         NOP                     
562F: 00         NOP                     
5630: 80         ADD     A,B             
5631: 00         NOP                     
5632: FC         ???                     
5633: 00         NOP                     
5634: FF         RST     0X38            
5635: 00         NOP                     
5636: FF         RST     0X38            
5637: 00         NOP                     
5638: FF         RST     0X38            
5639: 00         NOP                     
563A: FF         RST     0X38            
563B: 00         NOP                     
563C: 18 00      JR      $563E           
563E: 00         NOP                     
563F: 00         NOP                     
5640: C0         RET     NZ              
5641: 00         NOP                     
5642: FF         RST     0X38            
5643: 00         NOP                     
5644: FF         RST     0X38            
5645: 00         NOP                     
5646: DE 00      SBC     $00             
5648: C0         RET     NZ              
5649: 00         NOP                     
564A: 50         LD      D,B             
564B: 00         NOP                     
564C: 48         LD      C,B             
564D: 00         NOP                     
564E: 4E         LD      C,(HL)          
564F: 00         NOP                     
5650: 7E         LD      A,(HL)          
5651: 00         NOP                     
5652: 7F         LD      A,A             
5653: 00         NOP                     
5654: FF         RST     0X38            
5655: 00         NOP                     
5656: FF         RST     0X38            
5657: 00         NOP                     
5658: FF         RST     0X38            
5659: 00         NOP                     
565A: FF         RST     0X38            
565B: 00         NOP                     
565C: 7F         LD      A,A             
565D: 00         NOP                     
565E: 0E 00      LD      C,$00           
5660: 00         NOP                     
5661: 00         NOP                     
5662: 00         NOP                     
5663: 00         NOP                     
5664: 00         NOP                     
5665: 00         NOP                     
5666: 00         NOP                     
5667: 00         NOP                     
5668: 00         NOP                     
5669: 00         NOP                     
566A: 00         NOP                     
566B: 00         NOP                     
566C: 00         NOP                     
566D: 00         NOP                     
566E: 00         NOP                     
566F: 00         NOP                     
5670: 00         NOP                     
5671: 00         NOP                     
5672: C0         RET     NZ              
5673: 00         NOP                     
5674: E0 00      LDFF00  ($00),A         
5676: FF         RST     0X38            
5677: 00         NOP                     
5678: FF         RST     0X38            
5679: 00         NOP                     
567A: FF         RST     0X38            
567B: 00         NOP                     
567C: C6 00      ADD     $00             
567E: 00         NOP                     
567F: 00         NOP                     
5680: C0         RET     NZ              
5681: C0         RET     NZ              
5682: 60         LD      H,B             
5683: 60         LD      H,B             
5684: 30 30      JR      NC,$56B6        
5686: 18 18      JR      $56A0           
5688: 0C         INC     C               
5689: 0C         INC     C               
568A: 06 06      LD      B,$06           
568C: 03         INC     BC              
568D: 03         INC     BC              
568E: 01 01 00   LD      BC,$0001        
5691: 00         NOP                     
5692: 00         NOP                     
5693: 00         NOP                     
5694: 00         NOP                     
5695: 00         NOP                     
5696: 00         NOP                     
5697: 00         NOP                     
5698: 00         NOP                     
5699: 00         NOP                     
569A: 00         NOP                     
569B: 00         NOP                     
569C: 00         NOP                     
569D: 00         NOP                     
569E: 00         NOP                     
569F: 00         NOP                     
56A0: 80         ADD     A,B             
56A1: 80         ADD     A,B             
56A2: C0         RET     NZ              
56A3: C0         RET     NZ              
56A4: 40         LD      B,B             
56A5: 40         LD      B,B             
56A6: 60         LD      H,B             
56A7: 60         LD      H,B             
56A8: 20 20      JR      NZ,$56CA        
56AA: 30 30      JR      NC,$56DC        
56AC: 10 10      STOP    $10             
56AE: 18 18      JR      $56C8           
56B0: 08 08 0C   LD      ($0C08),SP      
56B3: 0C         INC     C               
56B4: 04         INC     B               
56B5: 04         INC     B               
56B6: 04         INC     B               
56B7: 04         INC     B               
56B8: 00         NOP                     
56B9: 00         NOP                     
56BA: 00         NOP                     
56BB: 00         NOP                     
56BC: 00         NOP                     
56BD: 00         NOP                     
56BE: 00         NOP                     
56BF: 00         NOP                     
56C0: 01 01 01   LD      BC,$0101        
56C3: 01 03 03   LD      BC,$0303        
56C6: 0E 0E      LD      C,$0E           
56C8: 18 18      JR      $56E2           
56CA: 18 18      JR      $56E4           
56CC: 1C         INC     E               
56CD: 1C         INC     E               
56CE: 0E 0E      LD      C,$0E           
56D0: 03         INC     BC              
56D1: 03         INC     BC              
56D2: 01 01 01   LD      BC,$0101        
56D5: 01 07 07   LD      BC,$0707        
56D8: 1E 1E      LD      E,$1E           
56DA: 7C         LD      A,H             
56DB: 7C         LD      A,H             
56DC: E0 E0      LDFF00  ($E0),A         
56DE: C0         RET     NZ              
56DF: C0         RET     NZ              
56E0: 01 01 03   LD      BC,$0301        
56E3: 03         INC     BC              
56E4: 1E 1E      LD      E,$1E           
56E6: 38 38      JR      C,$5720         
56E8: 30 30      JR      NC,$571A        
56EA: 60         LD      H,B             
56EB: 60         LD      H,B             
56EC: 60         LD      H,B             
56ED: 60         LD      H,B             
56EE: 60         LD      H,B             
56EF: 60         LD      H,B             
56F0: 70         LD      (HL),B          
56F1: 70         LD      (HL),B          
56F2: 1C         INC     E               
56F3: 1C         INC     E               
56F4: 06 06      LD      B,$06           
56F6: 06 06      LD      B,$06           
56F8: 02         LD      (BC),A          
56F9: 02         LD      (BC),A          
56FA: 02         LD      (BC),A          
56FB: 02         LD      (BC),A          
56FC: 02         LD      (BC),A          
56FD: 02         LD      (BC),A          
56FE: 01 01 00   LD      BC,$0001        
5701: 00         NOP                     
5702: 00         NOP                     
5703: 00         NOP                     
5704: 00         NOP                     
5705: 00         NOP                     
5706: 00         NOP                     
5707: 00         NOP                     
5708: 00         NOP                     
5709: 00         NOP                     
570A: 00         NOP                     
570B: 00         NOP                     
570C: 00         NOP                     
570D: 00         NOP                     
570E: 00         NOP                     
570F: 00         NOP                     
5710: 03         INC     BC              
5711: 03         INC     BC              
5712: 1E 1E      LD      E,$1E           
5714: 30 30      JR      NC,$5746        
5716: 20 20      JR      NZ,$5738        
5718: 20 20      JR      NZ,$573A        
571A: 20 20      JR      NZ,$573C        
571C: 40         LD      B,B             
571D: 40         LD      B,B             
571E: 80         ADD     A,B             
571F: 80         ADD     A,B             
5720: 38 38      JR      C,$575A         
5722: 70         LD      (HL),B          
5723: 70         LD      (HL),B          
5724: E0 E0      LDFF00  ($E0),A         
5726: E0 E0      LDFF00  ($E0),A         
5728: 60         LD      H,B             
5729: 60         LD      H,B             
572A: 70         LD      (HL),B          
572B: 70         LD      (HL),B          
572C: 38 38      JR      C,$5766         
572E: 1C         INC     E               
572F: 1C         INC     E               
5730: 0E 0E      LD      C,$0E           
5732: 07         RLCA                    
5733: 07         RLCA                    
5734: 07         RLCA                    
5735: 07         RLCA                    
5736: 07         RLCA                    
5737: 07         RLCA                    
5738: 1E 1E      LD      E,$1E           
573A: 3C         INC     A               
573B: 3C         INC     A               
573C: 38 38      JR      C,$5776         
573E: 38 38      JR      C,$5778         
5740: 00         NOP                     
5741: 00         NOP                     
5742: 00         NOP                     
5743: 00         NOP                     
5744: 00         NOP                     
5745: 00         NOP                     
5746: 00         NOP                     
5747: 00         NOP                     
5748: 00         NOP                     
5749: 00         NOP                     
574A: 00         NOP                     
574B: 00         NOP                     
574C: 00         NOP                     
574D: 00         NOP                     
574E: 00         NOP                     
574F: 00         NOP                     
5750: 00         NOP                     
5751: 00         NOP                     
5752: 00         NOP                     
5753: 00         NOP                     
5754: 00         NOP                     
5755: 00         NOP                     
5756: 00         NOP                     
5757: 00         NOP                     
5758: 00         NOP                     
5759: 80         ADD     A,B             
575A: 00         NOP                     
575B: 61         LD      H,C             
575C: 00         NOP                     
575D: 3F         CCF                     
575E: 00         NOP                     
575F: 0F         RRCA                    
5760: 00         NOP                     
5761: 00         NOP                     
5762: 00         NOP                     
5763: 00         NOP                     
5764: 00         NOP                     
5765: 00         NOP                     
5766: 00         NOP                     
5767: 00         NOP                     
5768: 00         NOP                     
5769: 00         NOP                     
576A: 00         NOP                     
576B: 00         NOP                     
576C: 00         NOP                     
576D: 00         NOP                     
576E: 00         NOP                     
576F: 00         NOP                     
5770: 00         NOP                     
5771: 00         NOP                     
5772: 00         NOP                     
5773: 00         NOP                     
5774: 00         NOP                     
5775: 00         NOP                     
5776: 00         NOP                     
5777: 00         NOP                     
5778: 00         NOP                     
5779: E1         POP     HL              
577A: 00         NOP                     
577B: FF         RST     0X38            
577C: 00         NOP                     
577D: CE 00      ADC     $00             
577F: 80         ADD     A,B             
5780: 00         NOP                     
5781: 00         NOP                     
5782: 00         NOP                     
5783: 00         NOP                     
5784: 00         NOP                     
5785: 00         NOP                     
5786: 00         NOP                     
5787: 00         NOP                     
5788: 00         NOP                     
5789: 00         NOP                     
578A: 00         NOP                     
578B: 00         NOP                     
578C: 01 00 03   LD      BC,$0300        
578F: 01 03 01   LD      BC,$0103        
5792: 01 00 00   LD      BC,$0000        
5795: 00         NOP                     
5796: 00         NOP                     
5797: 00         NOP                     
5798: 00         NOP                     
5799: 00         NOP                     
579A: 00         NOP                     
579B: 00         NOP                     
579C: 00         NOP                     
579D: 00         NOP                     
579E: 00         NOP                     
579F: 00         NOP                     
57A0: 00         NOP                     
57A1: 00         NOP                     
57A2: 00         NOP                     
57A3: 00         NOP                     
57A4: 00         NOP                     
57A5: 00         NOP                     
57A6: 00         NOP                     
57A7: 00         NOP                     
57A8: 0C         INC     C               
57A9: 00         NOP                     
57AA: 0E 04      LD      C,$04           
57AC: 07         RLCA                    
57AD: 02         LD      (BC),A          
57AE: 03         INC     BC              
57AF: 01 03 01   LD      BC,$0103        
57B2: 07         RLCA                    
57B3: 02         LD      (BC),A          
57B4: 0E 04      LD      C,$04           
57B6: 0C         INC     C               
57B7: 00         NOP                     
57B8: 00         NOP                     
57B9: 00         NOP                     
57BA: 00         NOP                     
57BB: 00         NOP                     
57BC: 00         NOP                     
57BD: 00         NOP                     
57BE: 00         NOP                     
57BF: 00         NOP                     
57C0: 00         NOP                     
57C1: 00         NOP                     
57C2: 00         NOP                     
57C3: 00         NOP                     
57C4: 00         NOP                     
57C5: 00         NOP                     
57C6: 00         NOP                     
57C7: 00         NOP                     
57C8: 01 00 01   LD      BC,$0100        
57CB: 00         NOP                     
57CC: 01 00 0F   LD      BC,$0F00        
57CF: 01 1F 0F   LD      BC,$0F1F        
57D2: 0F         RRCA                    
57D3: 01 01 00   LD      BC,$0001        
57D6: 01 00 01   LD      BC,$0100        
57D9: 00         NOP                     
57DA: 00         NOP                     
57DB: 00         NOP                     
57DC: 00         NOP                     
57DD: 00         NOP                     
57DE: 00         NOP                     
57DF: 00         NOP                     
57E0: 00         NOP                     
57E1: 00         NOP                     
57E2: 00         NOP                     
57E3: 00         NOP                     
57E4: 00         NOP                     
57E5: 00         NOP                     
57E6: 80         ADD     A,B             
57E7: 00         NOP                     
57E8: C0         RET     NZ              
57E9: 80         ADD     A,B             
57EA: C0         RET     NZ              
57EB: 80         ADD     A,B             
57EC: C0         RET     NZ              
57ED: 80         ADD     A,B             
57EE: F8 C0      LDHL    SP,$C0          
57F0: FC         ???                     
57F1: F8 F8      LDHL    SP,$F8          
57F3: C0         RET     NZ              
57F4: C0         RET     NZ              
57F5: 80         ADD     A,B             
57F6: C0         RET     NZ              
57F7: 80         ADD     A,B             
57F8: C0         RET     NZ              
57F9: 80         ADD     A,B             
57FA: 80         ADD     A,B             
57FB: 00         NOP                     
57FC: 00         NOP                     
57FD: 00         NOP                     
57FE: 00         NOP                     
57FF: 00         NOP                     
5800: 34         INC     (HL)            
5801: CB 60      SET     1,E             
5803: 9F         SBC     A               
5804: 54         LD      D,H             
5805: AB         XOR     E               
5806: E0 1F      LDFF00  ($1F),A         
5808: A0         AND     B               
5809: 5F         LD      E,A             
580A: C8         RET     Z               
580B: 37         SCF                     
580C: A0         AND     B               
580D: 5F         LD      E,A             
580E: 50         LD      D,B             
580F: AF         XOR     A               
5810: 41         LD      B,C             
5811: 82         ADD     A,D             
5812: 04         INC     B               
5813: C1         POP     BC              
5814: 00         NOP                     
5815: E1         POP     HL              
5816: 22         LD      (HLI),A         
5817: C0         RET     NZ              
5818: 00         NOP                     
5819: F0 00      LD      A,($00)         
581B: F8 10      LDHL    SP,$10          
581D: EC         ???                     
581E: 86         ADD     A,(HL)          
581F: 79         LD      A,C             
5820: 02         LD      (BC),A          
5821: FD         ???                     
5822: 03         INC     BC              
5823: FC         ???                     
5824: 89         ADC     A,C             
5825: 76         HALT                    
5826: 5E         LD      E,(HL)          
5827: A1         AND     C               
5828: 55         LD      D,L             
5829: AA         XOR     D               
582A: FA 05 EC   LD      A,($EC05)       
582D: 13         INC     DE              
582E: F0 0F      LD      A,($0F)         
5830: C0         RET     NZ              
5831: 3F         CCF                     
5832: 50         LD      D,B             
5833: BF         CP      A               
5834: 90         SUB     B               
5835: 7F         LD      A,A             
5836: A8         XOR     B               
5837: 6F         LD      L,A             
5838: 29         ADD     HL,HL           
5839: EF         RST     0X28            
583A: 26 E6      LD      H,$E6           
583C: 64         LD      H,H             
583D: C4 67 C6   CALL    NZ,$C667        
5840: 00         NOP                     
5841: FF         RST     0X38            
5842: 20 FF      JR      NZ,$5843        
5844: 60         LD      H,B             
5845: FF         RST     0X38            
5846: A1         AND     C               
5847: BF         CP      A               
5848: 63         LD      H,E             
5849: 3F         CCF                     
584A: 95         SUB     L               
584B: 5D         LD      E,L             
584C: 9B         SBC     E               
584D: 59         LD      E,C             
584E: 93         SUB     E               
584F: 51         LD      D,C             
5850: 00         NOP                     
5851: FF         RST     0X38            
5852: 00         NOP                     
5853: FF         RST     0X38            
5854: 00         NOP                     
5855: FF         RST     0X38            
5856: 00         NOP                     
5857: FF         RST     0X38            
5858: 00         NOP                     
5859: FF         RST     0X38            
585A: 00         NOP                     
585B: FF         RST     0X38            
585C: 00         NOP                     
585D: FF         RST     0X38            
585E: 00         NOP                     
585F: FF         RST     0X38            
5860: A8         XOR     B               
5861: 57         LD      D,A             
5862: C8         RET     Z               
5863: 37         SCF                     
5864: F6 09      OR      $09             
5866: 6A         LD      L,D             
5867: 95         SUB     L               
5868: 7B         LD      A,E             
5869: 84         ADD     A,H             
586A: 38 C0      JR      C,$582C         
586C: 02         LD      (BC),A          
586D: E0 30      LDFF00  ($30),A         
586F: C0         RET     NZ              
5870: 01 FE 07   LD      BC,$07FE        
5873: F8 59      LDHL    SP,$59          
5875: A6         AND     (HL)            
5876: 4B         LD      C,E             
5877: B4         OR      H               
5878: 17         RLA                     
5879: E8 6A      ADD     SP,$6A          
587B: 15         DEC     D               
587C: 9C         SBC     H               
587D: 03         INC     BC              
587E: 08 07 03   LD      ($0307),SP      
5881: FC         ???                     
5882: 15         DEC     D               
5883: EA 0A F5   LD      ($F50A),A       
5886: 45         LD      B,L             
5887: BA         CP      D               
5888: 2B         DEC     HL              
5889: D4 DE 21   CALL    NC,$21DE        
588C: 74         LD      (HL),H          
588D: 8B         ADC     A,E             
588E: D8         RET     C               
588F: 27         DAA                     
5890: 84         ADD     A,H             
5891: 7C         LD      A,H             
5892: 87         ADD     A,A             
5893: 7F         LD      A,A             
5894: 84         ADD     A,H             
5895: 7C         LD      A,H             
5896: 04         INC     B               
5897: FC         ???                     
5898: 04         INC     B               
5899: FC         ???                     
589A: 04         INC     B               
589B: FC         ???                     
589C: 04         INC     B               
589D: FC         ???                     
589E: 02         LD      (BC),A          
589F: FE C3      CP      $C3             
58A1: 40         LD      B,B             
58A2: C3 C0 83   JP      $83C0           
58A5: 80         ADD     A,B             
58A6: 83         ADD     A,E             
58A7: 80         ADD     A,B             
58A8: 87         ADD     A,A             
58A9: 80         ADD     A,B             
58AA: 87         ADD     A,A             
58AB: 80         ADD     A,B             
58AC: 87         ADD     A,A             
58AD: 80         ADD     A,B             
58AE: 0F         RRCA                    
58AF: 00         NOP                     
58B0: E0 60      LDFF00  ($60),A         
58B2: E0 60      LDFF00  ($60),A         
58B4: E0 60      LDFF00  ($60),A         
58B6: E0 60      LDFF00  ($60),A         
58B8: E0 60      LDFF00  ($60),A         
58BA: E0 60      LDFF00  ($60),A         
58BC: E0 60      LDFF00  ($60),A         
58BE: D0         RET     NC              
58BF: 70         LD      (HL),B          
58C0: F1         POP     AF              
58C1: 11 F0 10   LD      DE,$10F0        
58C4: F0 10      LD      A,($10)         
58C6: F0 10      LD      A,($10)         
58C8: F1         POP     AF              
58C9: 10 F3      STOP    $F3             
58CB: 10 03      STOP    $03             
58CD: 00         NOP                     
58CE: 07         RLCA                    
58CF: 00         NOP                     
58D0: FE 83      CP      $83             
58D2: 7E         LD      A,(HL)          
58D3: 43         LD      B,E             
58D4: FF         RST     0X38            
58D5: 27         DAA                     
58D6: FB         EI                      
58D7: 2C         INC     L               
58D8: F3         DI                      
58D9: 1C         INC     E               
58DA: F6 19      OR      $19             
58DC: E4         ???                     
58DD: 3B         DEC     SP              
58DE: C4 7B 18   CALL    NZ,$187B        
58E1: FF         RST     0X38            
58E2: 78         LD      A,B             
58E3: FF         RST     0X38            
58E4: FC         ???                     
58E5: 8F         ADC     A,A             
58E6: FF         RST     0X38            
58E7: 0F         RRCA                    
58E8: B8         CP      B               
58E9: 78         LD      A,B             
58EA: 60         LD      H,B             
58EB: E0 C0      LDFF00  ($C0),A         
58ED: C0         RET     NZ              
58EE: C7         RST     0X00            
58EF: 87         ADD     A,A             
58F0: 3E C3      LD      A,$C3           
58F2: 1E E3      LD      E,$E3           
58F4: 1E E3      LD      E,$E3           
58F6: CE F3      ADC     $F3             
58F8: 7F         LD      A,A             
58F9: 71         LD      (HL),C          
58FA: 1F         RRA                     
58FB: 18 0F      JR      $590C           
58FD: 0C         INC     C               
58FE: C7         RST     0X00            
58FF: C6 74      ADD     $74             
5901: 8B         ADC     A,E             
5902: 28 D7      JR      Z,$58DB         
5904: 16 E9      LD      D,$E9           
5906: 0D         DEC     C               
5907: F2         ???                     
5908: 03         INC     BC              
5909: FC         ???                     
590A: 00         NOP                     
590B: FF         RST     0X38            
590C: 00         NOP                     
590D: FF         RST     0X38            
590E: 00         NOP                     
590F: FF         RST     0X38            
5910: 56         LD      D,(HL)          
5911: A9         XOR     C               
5912: AC         XOR     H               
5913: 53         LD      D,E             
5914: D9         RETI                    
5915: 27         DAA                     
5916: 73         LD      (HL),E          
5917: 8E         ADC     A,(HL)          
5918: C7         RST     0X00            
5919: 3C         INC     A               
591A: 0C         INC     C               
591B: F8 08      LDHL    SP,$08          
591D: F8 1D      LDHL    SP,$1D          
591F: F0 3C      LD      A,($3C)         
5921: FF         RST     0X38            
5922: FF         RST     0X38            
5923: C3 FF 01   JP      $01FF           
5926: FF         RST     0X38            
5927: 00         NOP                     
5928: FF         RST     0X38            
5929: 03         INC     BC              
592A: 7F         LD      A,A             
592B: 00         NOP                     
592C: FF         RST     0X38            
592D: 00         NOP                     
592E: 7F         LD      A,A             
592F: 80         ADD     A,B             
5930: E9         JP      (HL)            
5931: C9         RET                     
5932: 79         LD      A,C             
5933: 79         LD      A,C             
5934: 67         LD      H,A             
5935: 46         LD      B,(HL)          
5936: E3         ???                     
5937: 80         ADD     A,B             
5938: E7         RST     0X20            
5939: C3 EC 2C   JP      $2CEC           
593C: F1         POP     AF              
593D: 10 C7      STOP    $C7             
593F: 00         NOP                     
5940: 87         ADD     A,A             
5941: 47         LD      B,A             
5942: E9         JP      (HL)            
5943: E9         JP      (HL)            
5944: 19         ADD     HL,DE           
5945: D9         RETI                    
5946: 7F         LD      A,A             
5947: FF         RST     0X38            
5948: FF         RST     0X38            
5949: 80         ADD     A,B             
594A: 7F         LD      A,A             
594B: 00         NOP                     
594C: FE 00      CP      $00             
594E: 8C         ADC     A,H             
594F: 70         LD      (HL),B          
5950: 00         NOP                     
5951: FF         RST     0X38            
5952: C0         RET     NZ              
5953: FF         RST     0X38            
5954: F0 3F      LD      A,($3F)         
5956: F9         LD      SP,HL           
5957: 8E         ADC     A,(HL)          
5958: FD         ???                     
5959: 06 FF      LD      B,$FF           
595B: 02         LD      (BC),A          
595C: 7F         LD      A,A             
595D: 01 1F 01   LD      BC,$011F        
5960: 78         LD      A,B             
5961: 84         ADD     A,H             
5962: D5         PUSH    DE              
5963: 2A         LD      A,(HLI)         
5964: E0 1F      LDFF00  ($1F),A         
5966: C8         RET     Z               
5967: 37         SCF                     
5968: A0         AND     B               
5969: 5F         LD      E,A             
596A: D0         RET     NC              
596B: 2F         CPL                     
596C: A0         AND     B               
596D: 5F         LD      E,A             
596E: C8         RET     Z               
596F: 37         SCF                     
5970: 18 07      JR      $5979           
5972: 54         LD      D,H             
5973: AB         XOR     E               
5974: 1C         INC     E               
5975: E3         ???                     
5976: 2E D1      LD      L,$D1           
5978: 1E E1      LD      E,$E1           
597A: 4A         LD      C,D             
597B: B5         OR      L               
597C: 9E         SBC     (HL)            
597D: 61         LD      H,C             
597E: 2C         INC     L               
597F: D3         ???                     
5980: E0 1F      LDFF00  ($1F),A         
5982: 00         NOP                     
5983: FF         RST     0X38            
5984: 00         NOP                     
5985: FF         RST     0X38            
5986: 00         NOP                     
5987: FF         RST     0X38            
5988: 00         NOP                     
5989: FF         RST     0X38            
598A: 00         NOP                     
598B: FF         RST     0X38            
598C: 00         NOP                     
598D: FF         RST     0X38            
598E: 01 FE 02   LD      BC,$02FE        
5991: FE 02      CP      $02             
5993: FE 02      CP      $02             
5995: FE 01      CP      $01             
5997: FF         RST     0X38            
5998: 01 FF 70   LD      BC,$70FF        
599B: 8F         ADC     A,A             
599C: F8 07      LDHL    SP,$07          
599E: 9C         SBC     H               
599F: 63         LD      H,E             
59A0: 0F         RRCA                    
59A1: 00         NOP                     
59A2: 1F         RRA                     
59A3: 00         NOP                     
59A4: 3F         CCF                     
59A5: 00         NOP                     
59A6: FF         RST     0X38            
59A7: 01 FF 01   LD      BC,$01FF        
59AA: FE 83      CP      $83             
59AC: 7C         LD      A,H             
59AD: C7         RST     0X00            
59AE: 38 FF      JR      C,$59AF         
59B0: 98         SBC     B               
59B1: F0 9C      LD      A,($9C)         
59B3: F0 CE      LD      A,($CE)         
59B5: B8         CP      B               
59B6: CF         RST     0X08            
59B7: 38 E7      JR      C,$59A0         
59B9: 9C         SBC     H               
59BA: 77         LD      (HL),A          
59BB: CC 3B F6   CALL    Z,$F63B         
59BE: 0D         DEC     C               
59BF: FB         EI                      
59C0: 0F         RRCA                    
59C1: 00         NOP                     
59C2: 1F         RRA                     
59C3: 01 3E 03   LD      BC,$033E        
59C6: FC         ???                     
59C7: 07         RLCA                    
59C8: F8 0F      LDHL    SP,$0F          
59CA: F0 1F      LD      A,($1F)         
59CC: E0 3F      LDFF00  ($3F),A         
59CE: C0         RET     NZ              
59CF: FF         RST     0X38            
59D0: 81         ADD     A,C             
59D1: FF         RST     0X38            
59D2: 09         ADD     HL,BC           
59D3: FF         RST     0X38            
59D4: 0B         DEC     BC              
59D5: FE 1B      CP      $1B             
59D7: FE 1F      CP      $1F             
59D9: FE 1E      CP      $1E             
59DB: FF         RST     0X38            
59DC: 1E FF      LD      E,$FF           
59DE: 1E FF      LD      E,$FF           
59E0: CC 0C D8   CALL    Z,$D80C         
59E3: 18 D0      JR      $59B5           
59E5: 10 D0      STOP    $D0             
59E7: 10 D0      STOP    $D0             
59E9: 10 F9      STOP    $F9             
59EB: 18 EF      JR      $59DC           
59ED: 0F         RRCA                    
59EE: F0 00      LD      A,($00)         
59F0: 23         INC     HL              
59F1: 23         INC     HL              
59F2: 13         INC     DE              
59F3: 13         INC     DE              
59F4: 09         ADD     HL,BC           
59F5: 09         ADD     HL,BC           
59F6: 09         ADD     HL,BC           
59F7: 09         ADD     HL,BC           
59F8: F9         LD      SP,HL           
59F9: 09         ADD     HL,BC           
59FA: F0 30      LD      A,($30)         
59FC: C0         RET     NZ              
59FD: C0         RET     NZ              
59FE: 00         NOP                     
59FF: 00         NOP                     
5A00: 00         NOP                     
5A01: FF         RST     0X38            
5A02: 00         NOP                     
5A03: FF         RST     0X38            
5A04: 00         NOP                     
5A05: FF         RST     0X38            
5A06: 01 FF 01   LD      BC,$01FF        
5A09: FF         RST     0X38            
5A0A: 01 FF 01   LD      BC,$01FF        
5A0D: FF         RST     0X38            
5A0E: 81         ADD     A,C             
5A0F: 7F         LD      A,A             
5A10: 1F         RRA                     
5A11: F0 1F      LD      A,($1F)         
5A13: F0 9F      LD      A,($9F)         
5A15: F0 9F      LD      A,($9F)         
5A17: F0 DE      LD      A,($DE)         
5A19: 71         LD      (HL),C          
5A1A: FE 31      CP      $31             
5A1C: FC         ???                     
5A1D: 03         INC     BC              
5A1E: 78         LD      A,B             
5A1F: 87         ADD     A,A             
5A20: 3F         CCF                     
5A21: C0         RET     NZ              
5A22: 3F         CCF                     
5A23: C0         RET     NZ              
5A24: 1F         RRA                     
5A25: E0 0F      LDFF00  ($0F),A         
5A27: F0 27      LD      A,($27)         
5A29: F8 31      LDHL    SP,$31          
5A2B: FE 28      CP      $28             
5A2D: EF         RST     0X28            
5A2E: 46         LD      B,(HL)          
5A2F: C7         RST     0X00            
5A30: C7         RST     0X00            
5A31: 00         NOP                     
5A32: FF         RST     0X38            
5A33: 00         NOP                     
5A34: FE 01      CP      $01             
5A36: FC         ???                     
5A37: 03         INC     BC              
5A38: F8 07      LDHL    SP,$07          
5A3A: C1         POP     BC              
5A3B: 3F         CCF                     
5A3C: 06 FE      LD      B,$FE           
5A3E: 38 F8      JR      C,$5A38         
5A40: 8C         ADC     A,H             
5A41: 70         LD      (HL),B          
5A42: 0E F0      LD      C,$F0           
5A44: 07         RLCA                    
5A45: F8 47      LDHL    SP,$47          
5A47: F8 E3      LDHL    SP,$E3          
5A49: BC         CP      H               
5A4A: E3         ???                     
5A4B: 3C         INC     A               
5A4C: E1         POP     HL              
5A4D: 3E 71      LD      A,$71           
5A4F: 1E 1F      LD      E,$1F           
5A51: 00         NOP                     
5A52: 6F         LD      L,A             
5A53: 00         NOP                     
5A54: 3F         CCF                     
5A55: 00         NOP                     
5A56: FF         RST     0X38            
5A57: 00         NOP                     
5A58: FF         RST     0X38            
5A59: 00         NOP                     
5A5A: FF         RST     0X38            
5A5B: 00         NOP                     
5A5C: EB         ???                     
5A5D: 00         NOP                     
5A5E: EB         ???                     
5A5F: 00         NOP                     
5A60: E4         ???                     
5A61: 9B         SBC     E               
5A62: F2         ???                     
5A63: 8D         ADC     A,L             
5A64: BD         CP      L               
5A65: C2 9F E0   JP      NZ,$E09F        
5A68: 87         ADD     A,A             
5A69: F8 80      LDHL    SP,$80          
5A6B: FF         RST     0X38            
5A6C: C0         RET     NZ              
5A6D: 7F         LD      A,A             
5A6E: C0         RET     NZ              
5A6F: 7F         LD      A,A             
5A70: 9C         SBC     H               
5A71: 63         LD      H,E             
5A72: 38 C7      JR      C,$5A3B         
5A74: F0 0F      LD      A,($0F)         
5A76: E0 1F      LDFF00  ($1F),A         
5A78: 80         ADD     A,B             
5A79: 7F         LD      A,A             
5A7A: 00         NOP                     
5A7B: FF         RST     0X38            
5A7C: 01 FE 02   LD      BC,$02FE        
5A7F: FD         ???                     
5A80: 88         ADC     A,B             
5A81: FF         RST     0X38            
5A82: 9F         SBC     A               
5A83: F4         ???                     
5A84: BA         CP      D               
5A85: E2         LDFF00  (C),A           
5A86: DA E2 DE   JP      C,$DEE2         
5A89: E4         ???                     
5A8A: 4E         LD      C,(HL)          
5A8B: F4         ???                     
5A8C: 4F         LD      C,A             
5A8D: F8 33      LDHL    SP,$33          
5A8F: FC         ???                     
5A90: 00         NOP                     
5A91: FF         RST     0X38            
5A92: F0 0F      LD      A,($0F)         
5A94: 0C         INC     C               
5A95: 03         INC     BC              
5A96: 06 01      LD      B,$01           
5A98: 06 01      LD      B,$01           
5A9A: 0E 01      LD      C,$01           
5A9C: 1D         DEC     E               
5A9D: 03         INC     BC              
5A9E: F9         LD      SP,HL           
5A9F: 07         RLCA                    
5AA0: 8F         ADC     A,A             
5AA1: F0 8F      LD      A,($8F)         
5AA3: F0 47      LD      A,($47)         
5AA5: F8 47      LDHL    SP,$47          
5AA7: F8 A3      LDHL    SP,$A3          
5AA9: FC         ???                     
5AAA: A0         AND     B               
5AAB: FF         RST     0X38            
5AAC: 90         SUB     B               
5AAD: FF         RST     0X38            
5AAE: E8 FF      ADD     SP,$FF          
5AB0: C0         RET     NZ              
5AB1: 00         NOP                     
5AB2: E0 00      LDFF00  ($00),A         
5AB4: F0 00      LD      A,($00)         
5AB6: F8 00      LDHL    SP,$00          
5AB8: FC         ???                     
5AB9: 00         NOP                     
5ABA: FF         RST     0X38            
5ABB: 00         NOP                     
5ABC: 7F         LD      A,A             
5ABD: 80         ADD     A,B             
5ABE: 3F         CCF                     
5ABF: C0         RET     NZ              
5AC0: 03         INC     BC              
5AC1: 02         LD      (BC),A          
5AC2: 01 01 00   LD      BC,$0001        
5AC5: 00         NOP                     
5AC6: 00         NOP                     
5AC7: 00         NOP                     
5AC8: 00         NOP                     
5AC9: 00         NOP                     
5ACA: 00         NOP                     
5ACB: 00         NOP                     
5ACC: C0         RET     NZ              
5ACD: 00         NOP                     
5ACE: C0         RET     NZ              
5ACF: 00         NOP                     
5AD0: 0F         RRCA                    
5AD1: 00         NOP                     
5AD2: 00         NOP                     
5AD3: 00         NOP                     
5AD4: 1E 00      LD      E,$00           
5AD6: 01 00 00   LD      BC,$0000        
5AD9: 00         NOP                     
5ADA: 00         NOP                     
5ADB: 00         NOP                     
5ADC: 02         LD      (BC),A          
5ADD: 00         NOP                     
5ADE: 01 00 80   LD      BC,$8000        
5AE1: 00         NOP                     
5AE2: 60         LD      H,B             
5AE3: 00         NOP                     
5AE4: 00         NOP                     
5AE5: 00         NOP                     
5AE6: 80         ADD     A,B             
5AE7: 00         NOP                     
5AE8: 40         LD      B,B             
5AE9: 00         NOP                     
5AEA: 00         NOP                     
5AEB: 00         NOP                     
5AEC: 00         NOP                     
5AED: 00         NOP                     
5AEE: 00         NOP                     
5AEF: 00         NOP                     
5AF0: 80         ADD     A,B             
5AF1: FF         RST     0X38            
5AF2: 80         ADD     A,B             
5AF3: FF         RST     0X38            
5AF4: 80         ADD     A,B             
5AF5: FF         RST     0X38            
5AF6: 80         ADD     A,B             
5AF7: FF         RST     0X38            
5AF8: 40         LD      B,B             
5AF9: 7F         LD      A,A             
5AFA: 40         LD      B,B             
5AFB: 7F         LD      A,A             
5AFC: 40         LD      B,B             
5AFD: 7F         LD      A,A             
5AFE: 40         LD      B,B             
5AFF: 7F         LD      A,A             
5B00: C9         RET                     
5B01: 3F         CCF                     
5B02: CE 3F      ADC     $3F             
5B04: 6F         LD      L,A             
5B05: 99         SBC     C               
5B06: AF         XOR     A               
5B07: 58         LD      E,B             
5B08: 67         LD      H,A             
5B09: 9C         SBC     H               
5B0A: A4         AND     H               
5B0B: 5F         LD      E,A             
5B0C: C2 3F 41   JP      NZ,$413F        
5B0F: BF         CP      A               
5B10: 00         NOP                     
5B11: FF         RST     0X38            
5B12: 82         ADD     A,D             
5B13: FF         RST     0X38            
5B14: C1         POP     BC              
5B15: FF         RST     0X38            
5B16: C1         POP     BC              
5B17: 3F         CCF                     
5B18: 81         ADD     A,C             
5B19: 7F         LD      A,A             
5B1A: 01 FF 01   LD      BC,$01FF        
5B1D: FF         RST     0X38            
5B1E: 81         ADD     A,C             
5B1F: FF         RST     0X38            
5B20: 59         LD      E,C             
5B21: D9         RETI                    
5B22: 80         ADD     A,B             
5B23: A4         AND     H               
5B24: 00         NOP                     
5B25: 00         NOP                     
5B26: 80         ADD     A,B             
5B27: 80         ADD     A,B             
5B28: F0 70      LD      A,($70)         
5B2A: C8         RET     Z               
5B2B: C8         RET     Z               
5B2C: 84         ADD     A,H             
5B2D: 84         ADD     A,H             
5B2E: 8C         ADC     A,H             
5B2F: 8C         ADC     A,H             
5B30: C3 C3 00   JP      $00C3           
5B33: 04         INC     B               
5B34: 00         NOP                     
5B35: 00         NOP                     
5B36: 00         NOP                     
5B37: 00         NOP                     
5B38: 01 00 03   LD      BC,$0300        
5B3B: 01 06 02   LD      BC,$0206        
5B3E: 04         INC     B               
5B3F: 04         INC     B               
5B40: F0 9F      LD      A,($9F)         
5B42: 38 4F      JR      C,$5B93         
5B44: 7C         LD      A,H             
5B45: 07         RLCA                    
5B46: 7F         LD      A,A             
5B47: 13         INC     DE              
5B48: FE F7      CP      $F7             
5B4A: 1E 1F      LD      E,$1F           
5B4C: 0E 0B      LD      C,$0B           
5B4E: 6F         LD      L,A             
5B4F: 6E         LD      L,(HL)          
5B50: F1         POP     AF              
5B51: 00         NOP                     
5B52: 30 C0      JR      NC,$5B14        
5B54: 0D         DEC     C               
5B55: F0 1F      LD      A,($1F)         
5B57: E0 1F      LDFF00  ($1F),A         
5B59: E0 1F      LDFF00  ($1F),A         
5B5B: E0 38      LDFF00  ($38),A         
5B5D: F7         RST     0X30            
5B5E: E8 2F      ADD     SP,$2F          
5B60: E0 3F      LDFF00  ($3F),A         
5B62: F8 1F      LDHL    SP,$1F          
5B64: FF         RST     0X38            
5B65: 07         RLCA                    
5B66: FF         RST     0X38            
5B67: 00         NOP                     
5B68: FF         RST     0X38            
5B69: 00         NOP                     
5B6A: EF         RST     0X28            
5B6B: 10 0F      STOP    $0F             
5B6D: F3         DI                      
5B6E: 1F         RRA                     
5B6F: E7         RST     0X20            
5B70: 25         DEC     H               
5B71: FA 66 F9   LD      A,($F966)       
5B74: EA B5 EC   LD      ($ECB5),A       
5B77: 33         INC     SP              
5B78: CA 75 9C   JP      Z,$9C75         
5B7B: F3         DI                      
5B7C: 37         SCF                     
5B7D: F8 F6      LDHL    SP,$F6          
5B7F: D8         RET     C               
5B80: 21 FE 18   LD      HL,$18FE        
5B83: FF         RST     0X38            
5B84: 0F         RRCA                    
5B85: FF         RST     0X38            
5B86: 04         INC     B               
5B87: FF         RST     0X38            
5B88: 04         INC     B               
5B89: FF         RST     0X38            
5B8A: 05         DEC     B               
5B8B: FE 05      CP      $05             
5B8D: FE 04      CP      $04             
5B8F: FF         RST     0X38            
5B90: E3         ???                     
5B91: 1F         RRA                     
5B92: 0F         RRCA                    
5B93: FC         ???                     
5B94: FF         RST     0X38            
5B95: F8 18      LDHL    SP,$18          
5B97: E0 E0      LDFF00  ($E0),A         
5B99: 00         NOP                     
5B9A: 80         ADD     A,B             
5B9B: 00         NOP                     
5B9C: 80         ADD     A,B             
5B9D: 00         NOP                     
5B9E: C0         RET     NZ              
5B9F: 00         NOP                     
5BA0: 3C         INC     A               
5BA1: FF         RST     0X38            
5BA2: 86         ADD     A,(HL)          
5BA3: 7F         LD      A,A             
5BA4: C3 3F F1   JP      $F13F           
5BA7: 0F         RRCA                    
5BA8: 1C         INC     E               
5BA9: 1F         RRA                     
5BAA: 26 27      LD      H,$27           
5BAC: 26 23      LD      H,$23           
5BAE: 2E 23      LD      L,$23           
5BB0: 0F         RRCA                    
5BB1: F0 07      LD      A,($07)         
5BB3: F8 03      LDHL    SP,$03          
5BB5: FC         ???                     
5BB6: 87         ADD     A,A             
5BB7: F8 C7      LDHL    SP,$C7          
5BB9: F8 C7      LDHL    SP,$C7          
5BBB: F8 87      LDHL    SP,$87          
5BBD: F8 87      LDHL    SP,$87          
5BBF: F8 C0      LDHL    SP,$C0          
5BC1: 00         NOP                     
5BC2: 80         ADD     A,B             
5BC3: 00         NOP                     
5BC4: 80         ADD     A,B             
5BC5: 00         NOP                     
5BC6: 80         ADD     A,B             
5BC7: 00         NOP                     
5BC8: 80         ADD     A,B             
5BC9: 00         NOP                     
5BCA: 80         ADD     A,B             
5BCB: 00         NOP                     
5BCC: C0         RET     NZ              
5BCD: 00         NOP                     
5BCE: C0         RET     NZ              
5BCF: 00         NOP                     
5BD0: 00         NOP                     
5BD1: 00         NOP                     
5BD2: 00         NOP                     
5BD3: 00         NOP                     
5BD4: 00         NOP                     
5BD5: 00         NOP                     
5BD6: 00         NOP                     
5BD7: 00         NOP                     
5BD8: 00         NOP                     
5BD9: 00         NOP                     
5BDA: 00         NOP                     
5BDB: 00         NOP                     
5BDC: 00         NOP                     
5BDD: 00         NOP                     
5BDE: 00         NOP                     
5BDF: 00         NOP                     
5BE0: FF         RST     0X38            
5BE1: FF         RST     0X38            
5BE2: 00         NOP                     
5BE3: 00         NOP                     
5BE4: 00         NOP                     
5BE5: 6A         LD      L,D             
5BE6: 00         NOP                     
5BE7: 8E         ADC     A,(HL)          
5BE8: 00         NOP                     
5BE9: 8A         ADC     A,D             
5BEA: 00         NOP                     
5BEB: 6A         LD      L,D             
5BEC: 00         NOP                     
5BED: 00         NOP                     
5BEE: FF         RST     0X38            
5BEF: FF         RST     0X38            
5BF0: 40         LD      B,B             
5BF1: 7F         LD      A,A             
5BF2: 40         LD      B,B             
5BF3: 7F         LD      A,A             
5BF4: 20 3F      JR      NZ,$5C35        
5BF6: 20 3F      JR      NZ,$5C37        
5BF8: 20 3F      JR      NZ,$5C39        
5BFA: 20 3F      JR      NZ,$5C3B        
5BFC: 20 3F      JR      NZ,$5C3D        
5BFE: 20 3F      JR      NZ,$5C3F        
5C00: 80         ADD     A,B             
5C01: 7F         LD      A,A             
5C02: 00         NOP                     
5C03: FF         RST     0X38            
5C04: 00         NOP                     
5C05: FF         RST     0X38            
5C06: 00         NOP                     
5C07: FF         RST     0X38            
5C08: 0C         INC     C               
5C09: FF         RST     0X38            
5C0A: 0F         RRCA                    
5C0B: FB         EI                      
5C0C: 0F         RRCA                    
5C0D: F8 07      LDHL    SP,$07          
5C0F: FC         ???                     
5C10: 71         LD      (HL),C          
5C11: FF         RST     0X38            
5C12: 21 FF 21   LD      HL,$21FF        
5C15: FF         RST     0X38            
5C16: 13         INC     DE              
5C17: FF         RST     0X38            
5C18: 24         INC     H               
5C19: FC         ???                     
5C1A: C8         RET     Z               
5C1B: F8 C8      LDHL    SP,$C8          
5C1D: 38 BF      JR      C,$5BDE         
5C1F: 7F         LD      A,A             
5C20: 92         SUB     D               
5C21: 96         SUB     (HL)            
5C22: 9E         SBC     (HL)            
5C23: 96         SUB     (HL)            
5C24: CC 8C A0   CALL    Z,$A08C         
5C27: 98         SBC     B               
5C28: 81         ADD     A,C             
5C29: 80         ADD     A,B             
5C2A: 80         ADD     A,B             
5C2B: 82         ADD     A,D             
5C2C: 84         ADD     A,H             
5C2D: 84         ADD     A,H             
5C2E: 40         LD      B,B             
5C2F: 42         LD      B,D             
5C30: 00         NOP                     
5C31: 04         INC     B               
5C32: 04         INC     B               
5C33: 00         NOP                     
5C34: 00         NOP                     
5C35: 00         NOP                     
5C36: 00         NOP                     
5C37: 00         NOP                     
5C38: 00         NOP                     
5C39: 00         NOP                     
5C3A: 00         NOP                     
5C3B: 00         NOP                     
5C3C: 00         NOP                     
5C3D: 00         NOP                     
5C3E: 01 00 9F   LD      BC,$9F00        
5C41: BA         CP      D               
5C42: FF         RST     0X38            
5C43: BA         CP      D               
5C44: 7F         LD      A,A             
5C45: 72         LD      (HL),D          
5C46: 1F         RRA                     
5C47: E2         LDFF00  (C),A           
5C48: FF         RST     0X38            
5C49: 04         INC     B               
5C4A: FE 05      CP      $05             
5C4C: FC         ???                     
5C4D: 0B         DEC     BC              
5C4E: FC         ???                     
5C4F: F3         DI                      
5C50: C4 47 44   CALL    NZ,$4447        
5C53: D7         RST     0X10            
5C54: 44         LD      B,H             
5C55: D7         RST     0X10            
5C56: 54         LD      D,H             
5C57: D7         RST     0X10            
5C58: 44         LD      B,H             
5C59: D7         RST     0X10            
5C5A: 4E         LD      C,(HL)          
5C5B: CF         RST     0X08            
5C5C: 51         LD      D,C             
5C5D: D1         POP     DE              
5C5E: 60         LD      H,B             
5C5F: E0 1F      LDFF00  ($1F),A         
5C61: E0 3F      LDFF00  ($3F),A         
5C63: C0         RET     NZ              
5C64: 01 FE 03   LD      BC,$03FE        
5C67: FC         ???                     
5C68: 03         INC     BC              
5C69: FF         RST     0X38            
5C6A: 06 FB      LD      B,$FB           
5C6C: 0F         RRCA                    
5C6D: F1         POP     AF              
5C6E: 8F         ADC     A,A             
5C6F: F0 E0      LD      A,($E0)         
5C71: 3C         INC     A               
5C72: E6 38      AND     $38             
5C74: CF         RST     0X08            
5C75: 70         LD      (HL),B          
5C76: 8A         ADC     A,D             
5C77: F5         PUSH    AF              
5C78: 1C         INC     E               
5C79: E3         ???                     
5C7A: 1C         INC     E               
5C7B: E3         ???                     
5C7C: 1A         LD      A,(DE)          
5C7D: E5         PUSH    HL              
5C7E: 9C         SBC     H               
5C7F: E3         ???                     
5C80: 06 FF      LD      B,$FF           
5C82: 02         LD      (BC),A          
5C83: FF         RST     0X38            
5C84: 01 FF 01   LD      BC,$01FF        
5C87: FF         RST     0X38            
5C88: 01 FF 01   LD      BC,$01FF        
5C8B: FF         RST     0X38            
5C8C: 01 FF 00   LD      BC,$00FF        
5C8F: FF         RST     0X38            
5C90: E0 00      LDFF00  ($00),A         
5C92: 7F         LD      A,A             
5C93: 80         ADD     A,B             
5C94: 1F         RRA                     
5C95: E0 8F      LDFF00  ($8F),A         
5C97: F0 70      LD      A,($70)         
5C99: FF         RST     0X38            
5C9A: 0F         RRCA                    
5C9B: FF         RST     0X38            
5C9C: 00         NOP                     
5C9D: FF         RST     0X38            
5C9E: 90         SUB     B               
5C9F: EF         RST     0X28            
5CA0: FE 17      CP      $17             
5CA2: FD         ???                     
5CA3: 1F         RRA                     
5CA4: F3         DI                      
5CA5: 0F         RRCA                    
5CA6: C7         RST     0X00            
5CA7: 3E 1F      LD      A,$1F           
5CA9: FD         ???                     
5CAA: F6 FA      OR      $FA             
5CAC: 0E F2      LD      C,$F2           
5CAE: 3F         CCF                     
5CAF: C3 87 F8   JP      $F887           
5CB2: 87         ADD     A,A             
5CB3: F8 87      LDHL    SP,$87          
5CB5: F8 C7      LDHL    SP,$C7          
5CB7: F8 C7      LDHL    SP,$C7          
5CB9: 78         LD      A,B             
5CBA: C3 7C C3   JP      $C37C           
5CBD: 7C         LD      A,H             
5CBE: C3 7C C0   JP      $C07C           
5CC1: 00         NOP                     
5CC2: C0         RET     NZ              
5CC3: 00         NOP                     
5CC4: E0 00      LDFF00  ($00),A         
5CC6: E0 00      LDFF00  ($00),A         
5CC8: F0 00      LD      A,($00)         
5CCA: F0 00      LD      A,($00)         
5CCC: F8 00      LDHL    SP,$00          
5CCE: FC         ???                     
5CCF: 00         NOP                     
5CD0: FF         RST     0X38            
5CD1: FF         RST     0X38            
5CD2: 00         NOP                     
5CD3: 01 00 EA   LD      BC,$EA00        
5CD6: 00         NOP                     
5CD7: AB         XOR     E               
5CD8: 00         NOP                     
5CD9: C8         RET     Z               
5CDA: 00         NOP                     
5CDB: AB         XOR     E               
5CDC: 00         NOP                     
5CDD: 00         NOP                     
5CDE: FF         RST     0X38            
5CDF: FF         RST     0X38            
5CE0: FF         RST     0X38            
5CE1: FF         RST     0X38            
5CE2: 00         NOP                     
5CE3: 80         ADD     A,B             
5CE4: 00         NOP                     
5CE5: 3A         LD      A,(HLD)         
5CE6: 00         NOP                     
5CE7: 92         SUB     D               
5CE8: 00         NOP                     
5CE9: 92         SUB     D               
5CEA: 00         NOP                     
5CEB: 12         LD      (DE),A          
5CEC: 00         NOP                     
5CED: 00         NOP                     
5CEE: FF         RST     0X38            
5CEF: FF         RST     0X38            
5CF0: 20 3F      JR      NZ,$5D31        
5CF2: 20 3F      JR      NZ,$5D33        
5CF4: 20 3F      JR      NZ,$5D35        
5CF6: 20 3F      JR      NZ,$5D37        
5CF8: 20 3F      JR      NZ,$5D39        
5CFA: 20 3F      JR      NZ,$5D3B        
5CFC: 20 3F      JR      NZ,$5D3D        
5CFE: 20 3F      JR      NZ,$5D3F        
5D00: 06 FD      LD      B,$FD           
5D02: 02         LD      (BC),A          
5D03: FF         RST     0X38            
5D04: 02         LD      (BC),A          
5D05: FF         RST     0X38            
5D06: 01 FF 00   LD      BC,$00FF        
5D09: FF         RST     0X38            
5D0A: 1C         INC     E               
5D0B: E3         ???                     
5D0C: 2A         LD      A,(HLI)         
5D0D: D5         PUSH    DE              
5D0E: 65         LD      H,L             
5D0F: 9A         SBC     D               
5D10: 61         LD      H,C             
5D11: E1         POP     HL              
5D12: 40         LD      B,B             
5D13: C0         RET     NZ              
5D14: 44         LD      B,H             
5D15: CC CA CE   CALL    Z,$CECA         
5D18: 87         ADD     A,A             
5D19: 87         ADD     A,A             
5D1A: 87         ADD     A,A             
5D1B: 84         ADD     A,H             
5D1C: 40         LD      B,B             
5D1D: C0         RET     NZ              
5D1E: 78         LD      A,B             
5D1F: E0 C0      LDFF00  ($C0),A         
5D21: C0         RET     NZ              
5D22: C1         POP     BC              
5D23: C1         POP     BC              
5D24: E1         POP     HL              
5D25: E1         POP     HL              
5D26: E1         POP     HL              
5D27: E1         POP     HL              
5D28: F9         LD      SP,HL           
5D29: F1         POP     AF              
5D2A: 7F         LD      A,A             
5D2B: F9         LD      SP,HL           
5D2C: FF         RST     0X38            
5D2D: 0C         INC     C               
5D2E: 1F         RRA                     
5D2F: 02         LD      (BC),A          
5D30: 01 00 C3   LD      BC,$C300        
5D33: C0         RET     NZ              
5D34: E3         ???                     
5D35: E0 27      LDFF00  ($27),A         
5D37: 20 EF      JR      NZ,$5D28        
5D39: E7         RST     0X20            
5D3A: F8 C8      LDHL    SP,$C8          
5D3C: F0 10      LD      A,($10)         
5D3E: F0 10      LD      A,($10)         
5D40: F8 47      LDHL    SP,$47          
5D42: FF         RST     0X38            
5D43: 37         SCF                     
5D44: F8 48      LDHL    SP,$48          
5D46: F0 30      LD      A,($30)         
5D48: F6 92      OR      $92             
5D4A: 77         LD      (HL),A          
5D4B: 73         LD      (HL),E          
5D4C: 0F         RRCA                    
5D4D: 0E 07      LD      C,$07           
5D4F: 00         NOP                     
5D50: E0 E0      LDFF00  ($E0),A         
5D52: 90         SUB     B               
5D53: 90         SUB     B               
5D54: 99         SBC     C               
5D55: 89         ADC     A,C             
5D56: DE 4F      SBC     $4F             
5D58: FE 4B      CP      $4B             
5D5A: F6 4B      OR      $4B             
5D5C: AC         XOR     H               
5D5D: 57         LD      D,A             
5D5E: FF         RST     0X38            
5D5F: 0F         RRCA                    
5D60: 87         ADD     A,A             
5D61: F8 83      LDHL    SP,$83          
5D63: FC         ???                     
5D64: 00         NOP                     
5D65: FF         RST     0X38            
5D66: 00         NOP                     
5D67: FF         RST     0X38            
5D68: 00         NOP                     
5D69: FF         RST     0X38            
5D6A: 01 FF 01   LD      BC,$01FF        
5D6D: FE 81      CP      $81             
5D6F: FE FA      CP      $FA             
5D71: 65         LD      H,L             
5D72: FE 19      CP      $19             
5D74: 1D         DEC     E               
5D75: EA 1E F1   LD      ($F11E),A       
5D78: 67         LD      H,A             
5D79: F8 81      LDHL    SP,$81          
5D7B: FE 80      CP      $80             
5D7D: FF         RST     0X38            
5D7E: C0         RET     NZ              
5D7F: 7F         LD      A,A             
5D80: FF         RST     0X38            
5D81: FF         RST     0X38            
5D82: 00         NOP                     
5D83: 07         RLCA                    
5D84: 00         NOP                     
5D85: 94         SUB     H               
5D86: 00         NOP                     
5D87: D7         RST     0X10            
5D88: 00         NOP                     
5D89: B4         OR      H               
5D8A: 00         NOP                     
5D8B: 97         SUB     A               
5D8C: 00         NOP                     
5D8D: 00         NOP                     
5D8E: FF         RST     0X38            
5D8F: FF         RST     0X38            
5D90: 87         ADD     A,A             
5D91: F8 C3      LDHL    SP,$C3          
5D93: FC         ???                     
5D94: 60         LD      H,B             
5D95: FF         RST     0X38            
5D96: 38 FF      JR      C,$5D97         
5D98: 0F         RRCA                    
5D99: FF         RST     0X38            
5D9A: 00         NOP                     
5D9B: FF         RST     0X38            
5D9C: 00         NOP                     
5D9D: FF         RST     0X38            
5D9E: 00         NOP                     
5D9F: FF         RST     0X38            
5DA0: FF         RST     0X38            
5DA1: 01 F8 07   LD      BC,$07F8        
5DA4: 00         NOP                     
5DA5: FF         RST     0X38            
5DA6: 03         INC     BC              
5DA7: FF         RST     0X38            
5DA8: FF         RST     0X38            
5DA9: FE 10      CP      $10             
5DAB: FF         RST     0X38            
5DAC: 0C         INC     C               
5DAD: FF         RST     0X38            
5DAE: 03         INC     BC              
5DAF: FF         RST     0X38            
5DB0: E1         POP     HL              
5DB1: FE 30      CP      $30             
5DB3: FF         RST     0X38            
5DB4: 70         LD      (HL),B          
5DB5: FF         RST     0X38            
5DB6: E8 DF      ADD     SP,$DF          
5DB8: E4         ???                     
5DB9: 1F         RRA                     
5DBA: 07         RLCA                    
5DBB: FF         RST     0X38            
5DBC: 1A         LD      A,(DE)          
5DBD: FF         RST     0X38            
5DBE: E4         ???                     
5DBF: FF         RST     0X38            
5DC0: FF         RST     0X38            
5DC1: 00         NOP                     
5DC2: FF         RST     0X38            
5DC3: 00         NOP                     
5DC4: 7F         LD      A,A             
5DC5: 80         ADD     A,B             
5DC6: 3F         CCF                     
5DC7: C0         RET     NZ              
5DC8: 0F         RRCA                    
5DC9: F0 03      LD      A,($03)         
5DCB: FC         ???                     
5DCC: F0 FF      LD      A,($FF)         
5DCE: 00         NOP                     
5DCF: FF         RST     0X38            
5DD0: 00         NOP                     
5DD1: 00         NOP                     
5DD2: C0         RET     NZ              
5DD3: 00         NOP                     
5DD4: F8 00      LDHL    SP,$00          
5DD6: FF         RST     0X38            
5DD7: 00         NOP                     
5DD8: FF         RST     0X38            
5DD9: 00         NOP                     
5DDA: FF         RST     0X38            
5DDB: 00         NOP                     
5DDC: 7F         LD      A,A             
5DDD: 80         ADD     A,B             
5DDE: FF         RST     0X38            
5DDF: 00         NOP                     
5DE0: 00         NOP                     
5DE1: 00         NOP                     
5DE2: 00         NOP                     
5DE3: 00         NOP                     
5DE4: 00         NOP                     
5DE5: 00         NOP                     
5DE6: 00         NOP                     
5DE7: 00         NOP                     
5DE8: 80         ADD     A,B             
5DE9: 00         NOP                     
5DEA: 80         ADD     A,B             
5DEB: 00         NOP                     
5DEC: 80         ADD     A,B             
5DED: 00         NOP                     
5DEE: C0         RET     NZ              
5DEF: 00         NOP                     
5DF0: 20 3F      JR      NZ,$5E31        
5DF2: 10 1F      STOP    $1F             
5DF4: 10 1F      STOP    $1F             
5DF6: 08 0F 08   LD      ($080F),SP      
5DF9: 0F         RRCA                    
5DFA: 04         INC     B               
5DFB: 07         RLCA                    
5DFC: 04         INC     B               
5DFD: 07         RLCA                    
5DFE: 02         LD      (BC),A          
5DFF: 03         INC     BC              
5E00: 80         ADD     A,B             
5E01: 7F         LD      A,A             
5E02: C1         POP     BC              
5E03: 3E C0      LD      A,$C0           
5E05: 3F         CCF                     
5E06: 61         LD      H,C             
5E07: 9E         SBC     (HL)            
5E08: 2E D1      LD      L,$D1           
5E0A: 1C         INC     E               
5E0B: E3         ???                     
5E0C: 00         NOP                     
5E0D: FF         RST     0X38            
5E0E: 00         NOP                     
5E0F: FF         RST     0X38            
5E10: BE         CP      (HL)            
5E11: 70         LD      (HL),B          
5E12: 9F         SBC     A               
5E13: 7C         LD      A,H             
5E14: FF         RST     0X38            
5E15: 67         LD      H,A             
5E16: 63         LD      H,E             
5E17: C0         RET     NZ              
5E18: C7         RST     0X00            
5E19: C0         RET     NZ              
5E1A: EF         RST     0X28            
5E1B: 80         ADD     A,B             
5E1C: FF         RST     0X38            
5E1D: 80         ADD     A,B             
5E1E: FF         RST     0X38            
5E1F: 80         ADD     A,B             
5E20: 07         RLCA                    
5E21: 01 83 00   LD      BC,$0083        
5E24: E3         ???                     
5E25: 00         NOP                     
5E26: F3         DI                      
5E27: C0         RET     NZ              
5E28: B3         OR      E               
5E29: 60         LD      H,B             
5E2A: 93         SUB     E               
5E2B: 70         LD      (HL),B          
5E2C: 93         SUB     E               
5E2D: 70         LD      (HL),B          
5E2E: 13         INC     DE              
5E2F: F0 F0      LD      A,($F0)         
5E31: 10 F0      STOP    $F0             
5E33: F0 F1      LD      A,($F1)         
5E35: 90         SUB     B               
5E36: F1         POP     AF              
5E37: 91         SUB     C               
5E38: F1         POP     AF              
5E39: D0         RET     NC              
5E3A: B3         OR      E               
5E3B: F0 93      LD      A,($93)         
5E3D: F0 93      LD      A,($93)         
5E3F: F0 1F      LD      A,($1F)         
5E41: 00         NOP                     
5E42: FF         RST     0X38            
5E43: 00         NOP                     
5E44: FF         RST     0X38            
5E45: 00         NOP                     
5E46: FF         RST     0X38            
5E47: FF         RST     0X38            
5E48: 87         ADD     A,A             
5E49: FC         ???                     
5E4A: 87         ADD     A,A             
5E4B: FC         ???                     
5E4C: 8F         ADC     A,A             
5E4D: F8 CF      LDHL    SP,$CF          
5E4F: F8 FF      LDHL    SP,$FF          
5E51: 10 FF      STOP    $FF             
5E53: 20 F1      JR      NZ,$5E46        
5E55: C0         RET     NZ              
5E56: E0 80      LDFF00  ($80),A         
5E58: FB         EI                      
5E59: 00         NOP                     
5E5A: FF         RST     0X38            
5E5B: 00         NOP                     
5E5C: DF         RST     0X18            
5E5D: 20 DF      JR      NZ,$5E3E        
5E5F: 20 F1      JR      NZ,$5E52        
5E61: 7E         LD      A,(HL)          
5E62: F8 0F      LDHL    SP,$0F          
5E64: FC         ???                     
5E65: 07         RLCA                    
5E66: FA 07 FA   LD      A,($FA07)       
5E69: 07         RLCA                    
5E6A: FA 07 F1   LD      A,($F107)       
5E6D: 0F         RRCA                    
5E6E: F1         POP     AF              
5E6F: 0F         RRCA                    
5E70: E0 3F      LDFF00  ($3F),A         
5E72: E0 3F      LDFF00  ($3F),A         
5E74: 70         LD      (HL),B          
5E75: 9F         SBC     A               
5E76: 70         LD      (HL),B          
5E77: 9F         SBC     A               
5E78: 38 CF      JR      C,$5E49         
5E7A: 38 CF      JR      C,$5E4B         
5E7C: 1C         INC     E               
5E7D: E7         RST     0X20            
5E7E: 0F         RRCA                    
5E7F: F3         DI                      
5E80: 00         NOP                     
5E81: FF         RST     0X38            
5E82: 00         NOP                     
5E83: FF         RST     0X38            
5E84: 00         NOP                     
5E85: FF         RST     0X38            
5E86: C0         RET     NZ              
5E87: FF         RST     0X38            
5E88: 30 3F      JR      NC,$5EC9        
5E8A: 08 0F 04   LD      ($040F),SP      
5E8D: 07         RLCA                    
5E8E: 02         LD      (BC),A          
5E8F: 03         INC     BC              
5E90: FF         RST     0X38            
5E91: FF         RST     0X38            
5E92: 00         NOP                     
5E93: 36 00      LD      (HL),$00        
5E95: 7F         LD      A,A             
5E96: 00         NOP                     
5E97: 7F         LD      A,A             
5E98: 00         NOP                     
5E99: 3E 00      LD      A,$00           
5E9B: 1C         INC     E               
5E9C: 00         NOP                     
5E9D: 08 FF FF   LD      ($FFFF),SP      
5EA0: FE FF      CP      $FF             
5EA2: 1A         LD      A,(DE)          
5EA3: 07         RLCA                    
5EA4: 1A         LD      A,(DE)          
5EA5: 07         RLCA                    
5EA6: 19         ADD     HL,DE           
5EA7: 07         RLCA                    
5EA8: 19         ADD     HL,DE           
5EA9: 07         RLCA                    
5EAA: 19         ADD     HL,DE           
5EAB: 07         RLCA                    
5EAC: 19         ADD     HL,DE           
5EAD: 07         RLCA                    
5EAE: FF         RST     0X38            
5EAF: FF         RST     0X38            
5EB0: F8 00      LDHL    SP,$00          
5EB2: 78         LD      A,B             
5EB3: 80         ADD     A,B             
5EB4: 7C         LD      A,H             
5EB5: 80         ADD     A,B             
5EB6: 3C         INC     A               
5EB7: C0         RET     NZ              
5EB8: 3E C0      LD      A,$C0           
5EBA: 3F         CCF                     
5EBB: C0         RET     NZ              
5EBC: 1F         RRA                     
5EBD: E0 9F      LDFF00  ($9F),A         
5EBF: E0 00      LDFF00  ($00),A         
5EC1: 00         NOP                     
5EC2: 00         NOP                     
5EC3: 00         NOP                     
5EC4: 00         NOP                     
5EC5: 00         NOP                     
5EC6: 00         NOP                     
5EC7: 00         NOP                     
5EC8: 03         INC     BC              
5EC9: 03         INC     BC              
5ECA: 04         INC     B               
5ECB: 04         INC     B               
5ECC: 89         ADC     A,C             
5ECD: 09         ADD     HL,BC           
5ECE: 82         ADD     A,D             
5ECF: 02         LD      (BC),A          
5ED0: 41         LD      B,C             
5ED1: 41         LD      B,C             
5ED2: 21 21 23   LD      HL,$2321        
5ED5: 21 13 11   LD      HL,$1113        
5ED8: 17         RLA                     
5ED9: 11 8F 89   LD      DE,$898F        
5EDC: 8F         ADC     A,A             
5EDD: 89         ADC     A,C             
5EDE: 07         RLCA                    
5EDF: 07         RLCA                    
5EE0: C0         RET     NZ              
5EE1: 00         NOP                     
5EE2: 80         ADD     A,B             
5EE3: 00         NOP                     
5EE4: 80         ADD     A,B             
5EE5: 00         NOP                     
5EE6: C0         RET     NZ              
5EE7: 00         NOP                     
5EE8: C0         RET     NZ              
5EE9: 00         NOP                     
5EEA: F0 00      LD      A,($00)         
5EEC: E0 00      LDFF00  ($00),A         
5EEE: 80         ADD     A,B             
5EEF: 00         NOP                     
5EF0: 08 0F 04   LD      ($040F),SP      
5EF3: 07         RLCA                    
5EF4: 04         INC     B               
5EF5: 07         RLCA                    
5EF6: 02         LD      (BC),A          
5EF7: 03         INC     BC              
5EF8: 02         LD      (BC),A          
5EF9: 03         INC     BC              
5EFA: 01 01 01   LD      BC,$0101        
5EFD: 01 01 01   LD      BC,$0101        
5F00: E0 1F      LDFF00  ($1F),A         
5F02: F8 07      LDHL    SP,$07          
5F04: 5C         LD      E,H             
5F05: A3         AND     E               
5F06: B6         OR      (HL)            
5F07: 49         LD      C,C             
5F08: 0D         DEC     C               
5F09: F2         ???                     
5F0A: 53         LD      D,E             
5F0B: AC         XOR     H               
5F0C: 05         DEC     B               
5F0D: FA 1A E5   LD      A,($E51A)       
5F10: FE 81      CP      $81             
5F12: 6C         LD      L,H             
5F13: D3         ???                     
5F14: 48         LD      C,B             
5F15: F7         RST     0X30            
5F16: 28 FF      JR      Z,$5F17         
5F18: 14         INC     D               
5F19: FF         RST     0X38            
5F1A: 0F         RRCA                    
5F1B: FF         RST     0X38            
5F1C: 84         ADD     A,H             
5F1D: 7C         LD      A,H             
5F1E: 84         ADD     A,H             
5F1F: 7C         LD      A,H             
5F20: 13         INC     DE              
5F21: F0 13      LD      A,($13)         
5F23: F0 33      LD      A,($33)         
5F25: F0 A3      LD      A,($A3)         
5F27: E0 A3      LDFF00  ($A3),A         
5F29: E0 E3      LDFF00  ($E3),A         
5F2B: E0 E3      LDFF00  ($E3),A         
5F2D: 60         LD      H,B             
5F2E: C3 40 93   JP      $9340           
5F31: F0 93      LD      A,($93)         
5F33: F0 91      LD      A,($91)         
5F35: F0 91      LD      A,($91)         
5F37: F0 91      LD      A,($91)         
5F39: F0 D1      LD      A,($D1)         
5F3B: 70         LD      (HL),B          
5F3C: D1         POP     DE              
5F3D: 70         LD      (HL),B          
5F3E: E1         POP     HL              
5F3F: 60         LD      H,B             
5F40: CB 7C      SET     1,E             
5F42: C8         RET     Z               
5F43: 7F         LD      A,A             
5F44: C8         RET     Z               
5F45: 7F         LD      A,A             
5F46: C7         RST     0X00            
5F47: 7F         LD      A,A             
5F48: C4 7C E4   CALL    NZ,$E47C        
5F4B: 3C         INC     A               
5F4C: E8 38      ADD     SP,$38          
5F4E: FE 3E      CP      $3E             
5F50: 9F         SBC     A               
5F51: 60         LD      H,B             
5F52: 9F         SBC     A               
5F53: E0 9F      LDFF00  ($9F),A         
5F55: E0 8C      LDFF00  ($8C),A         
5F57: F3         DI                      
5F58: 60         LD      H,B             
5F59: 7F         LD      A,A             
5F5A: 11 1F 3E   LD      DE,$3E1F        
5F5D: 0F         RRCA                    
5F5E: 3C         INC     A               
5F5F: 07         RLCA                    
5F60: C1         POP     BC              
5F61: 3F         CCF                     
5F62: C1         POP     BC              
5F63: 3F         CCF                     
5F64: 01 FF 01   LD      BC,$01FF        
5F67: FF         RST     0X38            
5F68: 02         LD      (BC),A          
5F69: FF         RST     0X38            
5F6A: 02         LD      (BC),A          
5F6B: FF         RST     0X38            
5F6C: 04         INC     B               
5F6D: FF         RST     0X38            
5F6E: 08 FF 0F   LD      ($0FFF),SP      
5F71: F1         POP     AF              
5F72: 7E         LD      A,(HL)          
5F73: 83         ADD     A,E             
5F74: 7C         LD      A,H             
5F75: 87         ADD     A,A             
5F76: 78         LD      A,B             
5F77: 9F         SBC     A               
5F78: 78         LD      A,B             
5F79: 8F         ADC     A,A             
5F7A: 3C         INC     A               
5F7B: C7         RST     0X00            
5F7C: 3C         INC     A               
5F7D: C7         RST     0X00            
5F7E: 3E C3      LD      A,$C3           
5F80: 01 01 00   LD      BC,$0001        
5F83: 00         NOP                     
5F84: 00         NOP                     
5F85: 00         NOP                     
5F86: 00         NOP                     
5F87: 00         NOP                     
5F88: 00         NOP                     
5F89: 00         NOP                     
5F8A: 78         LD      A,B             
5F8B: 00         NOP                     
5F8C: F0 00      LD      A,($00)         
5F8E: C0         RET     NZ              
5F8F: 00         NOP                     
5F90: 00         NOP                     
5F91: FF         RST     0X38            
5F92: 80         ADD     A,B             
5F93: FF         RST     0X38            
5F94: 40         LD      B,B             
5F95: 7F         LD      A,A             
5F96: 20 3F      JR      NZ,$5FD7        
5F98: 20 3F      JR      NZ,$5FD9        
5F9A: 10 1F      STOP    $1F             
5F9C: 10 1F      STOP    $1F             
5F9E: 08 0F 81   LD      ($810F),SP      
5FA1: 81         ADD     A,C             
5FA2: 81         ADD     A,C             
5FA3: 81         ADD     A,C             
5FA4: 81         ADD     A,C             
5FA5: 81         ADD     A,C             
5FA6: 81         ADD     A,C             
5FA7: 81         ADD     A,C             
5FA8: 81         ADD     A,C             
5FA9: 81         ADD     A,C             
5FAA: 81         ADD     A,C             
5FAB: 81         ADD     A,C             
5FAC: 41         LD      B,C             
5FAD: 41         LD      B,C             
5FAE: 41         LD      B,C             
5FAF: 41         LD      B,C             
5FB0: FF         RST     0X38            
5FB1: FF         RST     0X38            
5FB2: 80         ADD     A,B             
5FB3: 80         ADD     A,B             
5FB4: 80         ADD     A,B             
5FB5: 80         ADD     A,B             
5FB6: 80         ADD     A,B             
5FB7: 80         ADD     A,B             
5FB8: 80         ADD     A,B             
5FB9: 80         ADD     A,B             
5FBA: 80         ADD     A,B             
5FBB: 80         ADD     A,B             
5FBC: 80         ADD     A,B             
5FBD: 80         ADD     A,B             
5FBE: 81         ADD     A,C             
5FBF: 81         ADD     A,C             
5FC0: FF         RST     0X38            
5FC1: FF         RST     0X38            
5FC2: 00         NOP                     
5FC3: 00         NOP                     
5FC4: 00         NOP                     
5FC5: 00         NOP                     
5FC6: 00         NOP                     
5FC7: 00         NOP                     
5FC8: 00         NOP                     
5FC9: 00         NOP                     
5FCA: 00         NOP                     
5FCB: 00         NOP                     
5FCC: 00         NOP                     
5FCD: 00         NOP                     
5FCE: FF         RST     0X38            
5FCF: FF         RST     0X38            
5FD0: 81         ADD     A,C             
5FD1: 81         ADD     A,C             
5FD2: 80         ADD     A,B             
5FD3: 80         ADD     A,B             
5FD4: 80         ADD     A,B             
5FD5: 80         ADD     A,B             
5FD6: 80         ADD     A,B             
5FD7: 80         ADD     A,B             
5FD8: 80         ADD     A,B             
5FD9: 80         ADD     A,B             
5FDA: 80         ADD     A,B             
5FDB: 80         ADD     A,B             
5FDC: 80         ADD     A,B             
5FDD: 80         ADD     A,B             
5FDE: FF         RST     0X38            
5FDF: FF         RST     0X38            
5FE0: FF         RST     0X38            
5FE1: FF         RST     0X38            
5FE2: 01 01 01   LD      BC,$0101        
5FE5: 01 01 01   LD      BC,$0101        
5FE8: 01 01 01   LD      BC,$0101        
5FEB: 01 01 01   LD      BC,$0101        
5FEE: 81         ADD     A,C             
5FEF: 81         ADD     A,C             
5FF0: 81         ADD     A,C             
5FF1: 81         ADD     A,C             
5FF2: 81         ADD     A,C             
5FF3: 81         ADD     A,C             
5FF4: 81         ADD     A,C             
5FF5: 81         ADD     A,C             
5FF6: 81         ADD     A,C             
5FF7: 81         ADD     A,C             
5FF8: 81         ADD     A,C             
5FF9: 81         ADD     A,C             
5FFA: 81         ADD     A,C             
5FFB: 81         ADD     A,C             
5FFC: 81         ADD     A,C             
5FFD: 81         ADD     A,C             
5FFE: 81         ADD     A,C             
5FFF: 81         ADD     A,C             
6000: FF         RST     0X38            
6001: 00         NOP                     
6002: 2F         CPL                     
6003: 00         NOP                     
6004: F0 00      LD      A,($00)         
6006: C3 00 1F   JP      $1F00           
6009: 00         NOP                     
600A: FC         ???                     
600B: 00         NOP                     
600C: 0F         RRCA                    
600D: 00         NOP                     
600E: 07         RLCA                    
600F: 00         NOP                     
6010: FF         RST     0X38            
6011: 00         NOP                     
6012: E0 00      LDFF00  ($00),A         
6014: 3F         CCF                     
6015: 00         NOP                     
6016: F3         DI                      
6017: 00         NOP                     
6018: 00         NOP                     
6019: 00         NOP                     
601A: FE 00      CP      $00             
601C: 07         RLCA                    
601D: 00         NOP                     
601E: FC         ???                     
601F: 00         NOP                     
6020: 00         NOP                     
6021: 00         NOP                     
6022: 02         LD      (BC),A          
6023: 00         NOP                     
6024: F8 00      LDHL    SP,$00          
6026: 3F         CCF                     
6027: 00         NOP                     
6028: 00         NOP                     
6029: 00         NOP                     
602A: 80         ADD     A,B             
602B: 00         NOP                     
602C: 04         INC     B               
602D: 00         NOP                     
602E: 01 00 7F   LD      BC,$7F00        
6031: 00         NOP                     
6032: 00         NOP                     
6033: 00         NOP                     
6034: 00         NOP                     
6035: 00         NOP                     
6036: 87         ADD     A,A             
6037: 00         NOP                     
6038: 7C         LD      A,H             
6039: 00         NOP                     
603A: 80         ADD     A,B             
603B: 00         NOP                     
603C: 00         NOP                     
603D: 00         NOP                     
603E: F5         PUSH    AF              
603F: 00         NOP                     
6040: 03         INC     BC              
6041: 03         INC     BC              
6042: 05         DEC     B               
6043: 06 FF      LD      B,$FF           
6045: 07         RLCA                    
6046: 3F         CCF                     
6047: 00         NOP                     
6048: 00         NOP                     
6049: 00         NOP                     
604A: 87         ADD     A,A             
604B: 07         RLCA                    
604C: 1E 18      LD      E,$18           
604E: 3B         DEC     SP              
604F: 27         DAA                     
6050: C7         RST     0X00            
6051: 87         ADD     A,A             
6052: 7A         LD      A,D             
6053: CE FC      ADC     $FC             
6055: FC         ???                     
6056: FF         RST     0X38            
6057: 30 7C      JR      NC,$60D5        
6059: 10 F8      STOP    $F8             
605B: D0         RET     NC              
605C: F0 30      LD      A,($30)         
605E: DD         ???                     
605F: F0 3F      LD      A,($3F)         
6061: 00         NOP                     
6062: 0F         RRCA                    
6063: 00         NOP                     
6064: 07         RLCA                    
6065: 00         NOP                     
6066: 07         RLCA                    
6067: 00         NOP                     
6068: 03         INC     BC              
6069: 00         NOP                     
606A: 03         INC     BC              
606B: 00         NOP                     
606C: 00         NOP                     
606D: 00         NOP                     
606E: 00         NOP                     
606F: 00         NOP                     
6070: FF         RST     0X38            
6071: 00         NOP                     
6072: FF         RST     0X38            
6073: 00         NOP                     
6074: FF         RST     0X38            
6075: 00         NOP                     
6076: FF         RST     0X38            
6077: 00         NOP                     
6078: FF         RST     0X38            
6079: 00         NOP                     
607A: FF         RST     0X38            
607B: 00         NOP                     
607C: 1F         RRA                     
607D: 00         NOP                     
607E: 07         RLCA                    
607F: 00         NOP                     
6080: FF         RST     0X38            
6081: 00         NOP                     
6082: FF         RST     0X38            
6083: 00         NOP                     
6084: FF         RST     0X38            
6085: 00         NOP                     
6086: FE 00      CP      $00             
6088: FC         ???                     
6089: 00         NOP                     
608A: FC         ???                     
608B: 00         NOP                     
608C: F8 00      LDHL    SP,$00          
608E: F8 00      LDHL    SP,$00          
6090: FC         ???                     
6091: 00         NOP                     
6092: E0 00      LDFF00  ($00),A         
6094: 00         NOP                     
6095: 00         NOP                     
6096: 00         NOP                     
6097: 00         NOP                     
6098: 00         NOP                     
6099: 00         NOP                     
609A: 00         NOP                     
609B: 00         NOP                     
609C: 00         NOP                     
609D: 00         NOP                     
609E: 00         NOP                     
609F: 00         NOP                     
60A0: F8 00      LDHL    SP,$00          
60A2: E0 00      LDFF00  ($00),A         
60A4: C0         RET     NZ              
60A5: 00         NOP                     
60A6: 80         ADD     A,B             
60A7: 00         NOP                     
60A8: 81         ADD     A,C             
60A9: 01 02 03   LD      BC,$0302        
60AC: 02         LD      (BC),A          
60AD: 03         INC     BC              
60AE: 04         INC     B               
60AF: 07         RLCA                    
60B0: 01 01 1F   LD      BC,$1F01        
60B3: 1F         RRA                     
60B4: 63         LD      H,E             
60B5: 7C         LD      A,H             
60B6: 80         ADD     A,B             
60B7: FF         RST     0X38            
60B8: 00         NOP                     
60B9: FF         RST     0X38            
60BA: 03         INC     BC              
60BB: FF         RST     0X38            
60BC: 1C         INC     E               
60BD: FF         RST     0X38            
60BE: 63         LD      H,E             
60BF: FC         ???                     
60C0: F8 F8      LDHL    SP,$F8          
60C2: DE E6      SBC     $E6             
60C4: FD         ???                     
60C5: 3B         DEC     SP              
60C6: 35         DEC     (HL)            
60C7: CF         RST     0X08            
60C8: 07         RLCA                    
60C9: FF         RST     0X38            
60CA: FF         RST     0X38            
60CB: FE EE      CP      $EE             
60CD: 1C         INC     E               
60CE: 06 FC      LD      B,$FC           
60D0: 7F         LD      A,A             
60D1: 7F         LD      A,A             
60D2: 9C         SBC     H               
60D3: E3         ???                     
60D4: 3E FF      LD      A,$FF           
60D6: 53         LD      D,E             
60D7: E1         POP     HL              
60D8: A1         AND     C               
60D9: C0         RET     NZ              
60DA: A1         AND     C               
60DB: C0         RET     NZ              
60DC: B3         OR      E               
60DD: C0         RET     NZ              
60DE: 9F         SBC     A               
60DF: E0 07      LDFF00  ($07),A         
60E1: 07         RLCA                    
60E2: DB         ???                     
60E3: DC 2F F3   CALL    C,$F32F         
60E6: AD         XOR     L               
60E7: FE 70      CP      $70             
60E9: FF         RST     0X38            
60EA: 7F         LD      A,A             
60EB: DF         RST     0X18            
60EC: 5E         LD      E,(HL)          
60ED: CF         RST     0X08            
60EE: 58         LD      E,B             
60EF: CF         RST     0X08            
60F0: E0 E0      LDFF00  ($E0),A         
60F2: 7E         LD      A,(HL)          
60F3: FE B1      CP      $B1             
60F5: CF         RST     0X08            
60F6: C0         RET     NZ              
60F7: 3F         CCF                     
60F8: 00         NOP                     
60F9: FF         RST     0X38            
60FA: FC         ???                     
60FB: FF         RST     0X38            
60FC: 7B         LD      A,E             
60FD: 87         ADD     A,A             
60FE: 06 F9      LD      B,$F9           
6100: FC         ???                     
6101: 00         NOP                     
6102: 03         INC     BC              
6103: 00         NOP                     
6104: F0 00      LD      A,($00)         
6106: 00         NOP                     
6107: 00         NOP                     
6108: 0F         RRCA                    
6109: 00         NOP                     
610A: F0 00      LD      A,($00)         
610C: 1F         RRA                     
610D: 00         NOP                     
610E: F9         LD      SP,HL           
610F: 00         NOP                     
6110: 00         NOP                     
6111: 00         NOP                     
6112: FF         RST     0X38            
6113: 00         NOP                     
6114: 00         NOP                     
6115: 00         NOP                     
6116: 1F         RRA                     
6117: 00         NOP                     
6118: E0 00      LDFF00  ($00),A         
611A: 07         RLCA                    
611B: 00         NOP                     
611C: F8 00      LDHL    SP,$00          
611E: 80         ADD     A,B             
611F: 00         NOP                     
6120: FF         RST     0X38            
6121: 00         NOP                     
6122: FC         ???                     
6123: 00         NOP                     
6124: 07         RLCA                    
6125: 00         NOP                     
6126: 40         LD      B,B             
6127: 00         NOP                     
6128: 00         NOP                     
6129: 00         NOP                     
612A: 02         LD      (BC),A          
612B: 00         NOP                     
612C: 00         NOP                     
612D: 00         NOP                     
612E: 00         NOP                     
612F: 00         NOP                     
6130: 80         ADD     A,B             
6131: 00         NOP                     
6132: 03         INC     BC              
6133: 00         NOP                     
6134: FF         RST     0X38            
6135: 00         NOP                     
6136: F8 00      LDHL    SP,$00          
6138: 01 00 00   LD      BC,$0000        
613B: 00         NOP                     
613C: 00         NOP                     
613D: 00         NOP                     
613E: 40         LD      B,B             
613F: 00         NOP                     
6140: EF         RST     0X28            
6141: 5C         LD      E,H             
6142: 94         SUB     H               
6143: FB         EI                      
6144: A3         AND     E               
6145: FF         RST     0X38            
6146: FE FF      CP      $FF             
6148: ED         ???                     
6149: 73         LD      (HL),E          
614A: 61         LD      H,C             
614B: 00         NOP                     
614C: 00         NOP                     
614D: 00         NOP                     
614E: 00         NOP                     
614F: 00         NOP                     
6150: 78         LD      A,B             
6151: 18 1B      JR      $616E           
6153: FC         ???                     
6154: EB         ???                     
6155: FC         ???                     
6156: 1E F8      LD      E,$F8           
6158: F9         LD      SP,HL           
6159: E0 E0      LDFF00  ($E0),A         
615B: 00         NOP                     
615C: 00         NOP                     
615D: 00         NOP                     
615E: 40         LD      B,B             
615F: 00         NOP                     
6160: 03         INC     BC              
6161: 00         NOP                     
6162: 01 00 01   LD      BC,$0100        
6165: 00         NOP                     
6166: 01 00 00   LD      BC,$0000        
6169: 00         NOP                     
616A: 00         NOP                     
616B: 00         NOP                     
616C: 00         NOP                     
616D: 00         NOP                     
616E: 00         NOP                     
616F: 00         NOP                     
6170: F8 00      LDHL    SP,$00          
6172: C0         RET     NZ              
6173: 00         NOP                     
6174: 80         ADD     A,B             
6175: 00         NOP                     
6176: 80         ADD     A,B             
6177: 00         NOP                     
6178: 80         ADD     A,B             
6179: 00         NOP                     
617A: 00         NOP                     
617B: 00         NOP                     
617C: 00         NOP                     
617D: 00         NOP                     
617E: 00         NOP                     
617F: 00         NOP                     
6180: 0F         RRCA                    
6181: 0F         RRCA                    
6182: FF         RST     0X38            
6183: 30 F9      JR      NC,$617E        
6185: C6 B7      ADD     $B7             
6187: F8 9F      LDHL    SP,$9F          
6189: F0 5C      LD      A,($5C)         
618B: F3         DI                      
618C: B8         CP      B               
618D: 7F         LD      A,A             
618E: 7F         LD      A,A             
618F: 7F         LD      A,A             
6190: FF         RST     0X38            
6191: FF         RST     0X38            
6192: FF         RST     0X38            
6193: 00         NOP                     
6194: FF         RST     0X38            
6195: 00         NOP                     
6196: FF         RST     0X38            
6197: 00         NOP                     
6198: 83         ADD     A,E             
6199: 7C         LD      A,H             
619A: 00         NOP                     
619B: FF         RST     0X38            
619C: FF         RST     0X38            
619D: FF         RST     0X38            
619E: 62         LD      H,D             
619F: 81         ADD     A,C             
61A0: 05         DEC     B               
61A1: 07         RLCA                    
61A2: 07         RLCA                    
61A3: 07         RLCA                    
61A4: 04         INC     B               
61A5: 07         RLCA                    
61A6: 08 0F 18   LD      ($180F),SP      
61A9: 17         RLA                     
61AA: 30 2F      JR      NC,$61DB        
61AC: 30 3F      JR      NC,$61ED        
61AE: 08 0F 80   LD      ($800F),SP      
61B1: FF         RST     0X38            
61B2: 03         INC     BC              
61B3: FF         RST     0X38            
61B4: 07         RLCA                    
61B5: FF         RST     0X38            
61B6: 0C         INC     C               
61B7: FF         RST     0X38            
61B8: 19         ADD     HL,DE           
61B9: FE 30      CP      $30             
61BB: FF         RST     0X38            
61BC: 20 FF      JR      NZ,$61BD        
61BE: 40         LD      B,B             
61BF: FF         RST     0X38            
61C0: FF         RST     0X38            
61C1: FC         ???                     
61C2: C5         PUSH    BC              
61C3: FE 36      CP      $36             
61C5: CF         RST     0X08            
61C6: C7         RST     0X00            
61C7: 3F         CCF                     
61C8: 04         INC     B               
61C9: FF         RST     0X38            
61CA: 1B         DEC     DE              
61CB: FC         ???                     
61CC: 34         INC     (HL)            
61CD: FB         EI                      
61CE: 29         ADD     HL,HL           
61CF: F7         RST     0X30            
61D0: 40         LD      B,B             
61D1: FF         RST     0X38            
61D2: BF         CP      A               
61D3: 7F         LD      A,A             
61D4: 51         LD      D,C             
61D5: E0 D1      LDFF00  ($D1),A         
61D7: E0 4E      LDFF00  ($4E),A         
61D9: F1         POP     AF              
61DA: 61         LD      H,C             
61DB: FF         RST     0X38            
61DC: FF         RST     0X38            
61DD: FF         RST     0X38            
61DE: 8E         ADC     A,(HL)          
61DF: FF         RST     0X38            
61E0: EF         RST     0X28            
61E1: DF         RST     0X18            
61E2: 49         LD      C,C             
61E3: FE 38      CP      $38             
61E5: FF         RST     0X38            
61E6: 7E         LD      A,(HL)          
61E7: FF         RST     0X38            
61E8: 47         LD      B,A             
61E9: FF         RST     0X38            
61EA: E9         JP      (HL)            
61EB: F7         RST     0X30            
61EC: 34         INC     (HL)            
61ED: FB         EI                      
61EE: 12         LD      (DE),A          
61EF: FD         ???                     
61F0: E1         POP     HL              
61F1: FE D8      CP      $D8             
61F3: 3F         CCF                     
61F4: 3E CF      LD      A,$CF           
61F6: 0B         DEC     BC              
61F7: F7         RST     0X30            
61F8: 01 FF 80   LD      BC,$80FF        
61FB: FF         RST     0X38            
61FC: C0         RET     NZ              
61FD: FF         RST     0X38            
61FE: C0         RET     NZ              
61FF: FF         RST     0X38            
6200: 07         RLCA                    
6201: 00         NOP                     
6202: 03         INC     BC              
6203: 00         NOP                     
6204: 81         ADD     A,C             
6205: 80         ADD     A,B             
6206: 41         LD      B,C             
6207: C0         RET     NZ              
6208: 20 E0      JR      NZ,$61EA        
620A: 20 E0      JR      NZ,$61EC        
620C: 90         SUB     B               
620D: F0 D0      LD      A,($D0)         
620F: F0 38      LD      A,($38)         
6211: 3F         CCF                     
6212: 60         LD      H,B             
6213: 5F         LD      E,A             
6214: 41         LD      B,C             
6215: 7F         LD      A,A             
6216: 72         LD      (HL),D          
6217: 7F         LD      A,A             
6218: 0A         LD      A,(BC)          
6219: 0F         RRCA                    
621A: F2         ???                     
621B: FF         RST     0X38            
621C: E4         ???                     
621D: 9F         SBC     A               
621E: 84         ADD     A,H             
621F: FF         RST     0X38            
6220: 80         ADD     A,B             
6221: FF         RST     0X38            
6222: 80         ADD     A,B             
6223: FF         RST     0X38            
6224: 00         NOP                     
6225: FF         RST     0X38            
6226: 01 FF 01   LD      BC,$01FF        
6229: FF         RST     0X38            
622A: 03         INC     BC              
622B: FF         RST     0X38            
622C: 03         INC     BC              
622D: FF         RST     0X38            
622E: 03         INC     BC              
622F: FF         RST     0X38            
6230: 61         LD      H,C             
6231: FF         RST     0X38            
6232: C3 FF 83   JP      $83FF           
6235: FF         RST     0X38            
6236: 82         ADD     A,D             
6237: FF         RST     0X38            
6238: 86         ADD     A,(HL)          
6239: FF         RST     0X38            
623A: 06 FF      LD      B,$FF           
623C: 04         INC     B               
623D: FF         RST     0X38            
623E: E4         ???                     
623F: FF         RST     0X38            
6240: A4         AND     H               
6241: DF         RST     0X18            
6242: 24         INC     H               
6243: DF         RST     0X18            
6244: 24         INC     H               
6245: DF         RST     0X18            
6246: 04         INC     B               
6247: FF         RST     0X38            
6248: 07         RLCA                    
6249: FF         RST     0X38            
624A: 07         RLCA                    
624B: FE 06      CP      $06             
624D: FD         ???                     
624E: 04         INC     B               
624F: FF         RST     0X38            
6250: 5A         LD      E,D             
6251: BD         CP      L               
6252: 28 DF      JR      Z,$6233         
6254: 28 DF      JR      Z,$6235         
6256: 0C         INC     C               
6257: FF         RST     0X38            
6258: 84         ADD     A,H             
6259: FF         RST     0X38            
625A: 84         ADD     A,H             
625B: 7F         LD      A,A             
625C: 06 FF      LD      B,$FF           
625E: 02         LD      (BC),A          
625F: FF         RST     0X38            
6260: E0 FF      LDFF00  ($FF),A         
6262: 60         LD      H,B             
6263: FF         RST     0X38            
6264: 30 FF      JR      NC,$6265        
6266: 30 FF      JR      NC,$6267        
6268: 30 FF      JR      NC,$6269        
626A: 10 FF      STOP    $FF             
626C: 10 FF      STOP    $FF             
626E: 10 FF      STOP    $FF             
6270: 21 FF 21   LD      HL,$21FF        
6273: FF         RST     0X38            
6274: 17         RLA                     
6275: FF         RST     0X38            
6276: 14         INC     D               
6277: FC         ???                     
6278: 16 FA      LD      D,$FA           
627A: 0B         DEC     BC              
627B: FD         ???                     
627C: 09         ADD     HL,BC           
627D: FF         RST     0X38            
627E: 09         ADD     HL,BC           
627F: FF         RST     0X38            
6280: 48         LD      C,B             
6281: FF         RST     0X38            
6282: 48         LD      C,B             
6283: FF         RST     0X38            
6284: 41         LD      B,C             
6285: FF         RST     0X38            
6286: 21 FF 21   LD      HL,$21FF        
6289: FF         RST     0X38            
628A: 11 FF 09   LD      DE,$09FF        
628D: FF         RST     0X38            
628E: 07         RLCA                    
628F: FF         RST     0X38            
6290: FF         RST     0X38            
6291: FF         RST     0X38            
6292: BF         CP      A               
6293: FF         RST     0X38            
6294: BF         CP      A               
6295: FF         RST     0X38            
6296: 1F         RRA                     
6297: FF         RST     0X38            
6298: 1F         RRA                     
6299: FF         RST     0X38            
629A: 0E FF      LD      C,$FF           
629C: 04         INC     B               
629D: FF         RST     0X38            
629E: 00         NOP                     
629F: FF         RST     0X38            
62A0: 10 FF      STOP    $FF             
62A2: 10 FF      STOP    $FF             
62A4: 10 FF      STOP    $FF             
62A6: 10 FF      STOP    $FF             
62A8: 13         INC     DE              
62A9: FF         RST     0X38            
62AA: 90         SUB     B               
62AB: FF         RST     0X38            
62AC: 90         SUB     B               
62AD: FF         RST     0X38            
62AE: 80         ADD     A,B             
62AF: FF         RST     0X38            
62B0: 0F         RRCA                    
62B1: FF         RST     0X38            
62B2: 0F         RRCA                    
62B3: FF         RST     0X38            
62B4: 0F         RRCA                    
62B5: FE 1F      CP      $1F             
62B7: FE 9E      CP      $9E             
62B9: FF         RST     0X38            
62BA: FF         RST     0X38            
62BB: FF         RST     0X38            
62BC: FF         RST     0X38            
62BD: 7F         LD      A,A             
62BE: 7F         LD      A,A             
62BF: FF         RST     0X38            
62C0: 82         ADD     A,D             
62C1: FF         RST     0X38            
62C2: 82         ADD     A,D             
62C3: 7F         LD      A,A             
62C4: 02         LD      (BC),A          
62C5: FF         RST     0X38            
62C6: 02         LD      (BC),A          
62C7: FF         RST     0X38            
62C8: 12         LD      (DE),A          
62C9: FF         RST     0X38            
62CA: 30 FF      JR      NC,$62CB        
62CC: E0 FF      LDFF00  ($FF),A         
62CE: C1         POP     BC              
62CF: FF         RST     0X38            
62D0: 3F         CCF                     
62D1: FF         RST     0X38            
62D2: 3F         CCF                     
62D3: FF         RST     0X38            
62D4: 3F         CCF                     
62D5: FF         RST     0X38            
62D6: FF         RST     0X38            
62D7: FF         RST     0X38            
62D8: 7E         LD      A,(HL)          
62D9: FF         RST     0X38            
62DA: 6C         LD      L,H             
62DB: FF         RST     0X38            
62DC: C0         RET     NZ              
62DD: FF         RST     0X38            
62DE: 80         ADD     A,B             
62DF: FF         RST     0X38            
62E0: E1         POP     HL              
62E1: DF         RST     0X18            
62E2: C1         POP     BC              
62E3: BF         CP      A               
62E4: 82         ADD     A,D             
62E5: FF         RST     0X38            
62E6: 82         ADD     A,D             
62E7: FF         RST     0X38            
62E8: C4 FF 44   CALL    NZ,$44FF        
62EB: FF         RST     0X38            
62EC: 48         LD      C,B             
62ED: FF         RST     0X38            
62EE: 70         LD      (HL),B          
62EF: FF         RST     0X38            
62F0: 00         NOP                     
62F1: 00         NOP                     
62F2: 00         NOP                     
62F3: 00         NOP                     
62F4: 24         INC     H               
62F5: 24         INC     H               
62F6: 18 18      JR      $6310           
62F8: 18 18      JR      $6312           
62FA: 24         INC     H               
62FB: 24         INC     H               
62FC: 00         NOP                     
62FD: 00         NOP                     
62FE: 00         NOP                     
62FF: 00         NOP                     
6300: 30 F0      JR      NC,$62F2        
6302: 08 F8 04   LD      ($04F8),SP      
6305: FC         ???                     
6306: 04         INC     B               
6307: FC         ???                     
6308: 82         ADD     A,D             
6309: FE C2      CP      $C2             
630B: FE 42      CP      $42             
630D: FE 61      CP      $61             
630F: FF         RST     0X38            
6310: 8C         ADC     A,H             
6311: FF         RST     0X38            
6312: 89         ADC     A,C             
6313: FF         RST     0X38            
6314: 89         ADC     A,C             
6315: FF         RST     0X38            
6316: 88         ADC     A,B             
6317: FF         RST     0X38            
6318: 88         ADC     A,B             
6319: FF         RST     0X38            
631A: 88         ADC     A,B             
631B: FF         RST     0X38            
631C: 88         ADC     A,B             
631D: FF         RST     0X38            
631E: 48         LD      C,B             
631F: FF         RST     0X38            
6320: 03         INC     BC              
6321: FF         RST     0X38            
6322: 87         ADD     A,A             
6323: FF         RST     0X38            
6324: C7         RST     0X00            
6325: FE E6      CP      $E6             
6327: FF         RST     0X38            
6328: FE 7F      CP      $7F             
632A: 7E         LD      A,(HL)          
632B: BF         CP      A               
632C: 3E FF      LD      A,$FF           
632E: 7E         LD      A,(HL)          
632F: FF         RST     0X38            
6330: CC FF C8   CALL    Z,$C8FF         
6333: 3F         CCF                     
6334: 08 FF 08   LD      ($08FF),SP      
6337: FF         RST     0X38            
6338: 08 FF 08   LD      ($08FF),SP      
633B: FF         RST     0X38            
633C: 08 FF 10   LD      ($10FF),SP      
633F: FF         RST     0X38            
6340: 04         INC     B               
6341: FF         RST     0X38            
6342: 04         INC     B               
6343: FF         RST     0X38            
6344: F4         ???                     
6345: FF         RST     0X38            
6346: 3C         INC     A               
6347: FF         RST     0X38            
6348: 3C         INC     A               
6349: CF         RST     0X08            
634A: 1C         INC     E               
634B: EF         RST     0X28            
634C: 0C         INC     C               
634D: FF         RST     0X38            
634E: 0F         RRCA                    
634F: FF         RST     0X38            
6350: 02         LD      (BC),A          
6351: FF         RST     0X38            
6352: 02         LD      (BC),A          
6353: FF         RST     0X38            
6354: 02         LD      (BC),A          
6355: FF         RST     0X38            
6356: 02         LD      (BC),A          
6357: FF         RST     0X38            
6358: 02         LD      (BC),A          
6359: FF         RST     0X38            
635A: 22         LD      (HLI),A         
635B: FF         RST     0X38            
635C: E2         LDFF00  (C),A           
635D: FF         RST     0X38            
635E: C2 FF 11   JP      NZ,$11FF        
6361: FF         RST     0X38            
6362: 17         RLA                     
6363: FF         RST     0X38            
6364: 1F         RRA                     
6365: FF         RST     0X38            
6366: FE FD      CP      $FD             
6368: 7C         LD      A,H             
6369: FB         EI                      
636A: 38 FF      JR      C,$636B         
636C: 3C         INC     A               
636D: FF         RST     0X38            
636E: 3E FF      LD      A,$FF           
6370: C9         RET                     
6371: FF         RST     0X38            
6372: 89         ADC     A,C             
6373: FF         RST     0X38            
6374: 09         ADD     HL,BC           
6375: FF         RST     0X38            
6376: 09         ADD     HL,BC           
6377: FF         RST     0X38            
6378: 09         ADD     HL,BC           
6379: FF         RST     0X38            
637A: 09         ADD     HL,BC           
637B: FF         RST     0X38            
637C: 09         ADD     HL,BC           
637D: FF         RST     0X38            
637E: 69         LD      L,C             
637F: FF         RST     0X38            
6380: F0 E0      LD      A,($E0)         
6382: DF         RST     0X18            
6383: 3F         CCF                     
6384: FF         RST     0X38            
6385: 00         NOP                     
6386: FF         RST     0X38            
6387: 00         NOP                     
6388: FF         RST     0X38            
6389: 00         NOP                     
638A: 1F         RRA                     
638B: E0 C0      LDFF00  ($C0),A         
638D: FF         RST     0X38            
638E: 3F         CCF                     
638F: FF         RST     0X38            
6390: 00         NOP                     
6391: 00         NOP                     
6392: FF         RST     0X38            
6393: FF         RST     0X38            
6394: FF         RST     0X38            
6395: 00         NOP                     
6396: FF         RST     0X38            
6397: 00         NOP                     
6398: FF         RST     0X38            
6399: 00         NOP                     
639A: C3 3C 00   JP      $003C           
639D: FF         RST     0X38            
639E: FF         RST     0X38            
639F: FF         RST     0X38            
63A0: 80         ADD     A,B             
63A1: FF         RST     0X38            
63A2: C1         POP     BC              
63A3: FF         RST     0X38            
63A4: C3 FF E7   JP      $E7FF           
63A7: FF         RST     0X38            
63A8: BE         CP      (HL)            
63A9: FF         RST     0X38            
63AA: BC         CP      H               
63AB: FF         RST     0X38            
63AC: 9B         SBC     E               
63AD: FC         ???                     
63AE: A7         AND     A               
63AF: D8         RET     C               
63B0: FF         RST     0X38            
63B1: FF         RST     0X38            
63B2: FF         RST     0X38            
63B3: FF         RST     0X38            
63B4: C1         POP     BC              
63B5: FF         RST     0X38            
63B6: 9E         SBC     (HL)            
63B7: E1         POP     HL              
63B8: 7F         LD      A,A             
63B9: 80         ADD     A,B             
63BA: 02         LD      (BC),A          
63BB: FD         ???                     
63BC: 00         NOP                     
63BD: FF         RST     0X38            
63BE: 90         SUB     B               
63BF: 6F         LD      L,A             
63C0: 81         ADD     A,C             
63C1: FF         RST     0X38            
63C2: C1         POP     BC              
63C3: FF         RST     0X38            
63C4: E3         ???                     
63C5: FF         RST     0X38            
63C6: E7         RST     0X20            
63C7: FF         RST     0X38            
63C8: 3F         CCF                     
63C9: FF         RST     0X38            
63CA: 1D         DEC     E               
63CB: FF         RST     0X38            
63CC: 49         LD      C,C             
63CD: BF         CP      A               
63CE: E1         POP     HL              
63CF: 1F         RRA                     
63D0: BF         CP      A               
63D1: C0         RET     NZ              
63D2: D3         ???                     
63D3: EC         ???                     
63D4: C1         POP     BC              
63D5: FE C1      CP      $C1             
63D7: FE C8      CP      $C8             
63D9: F7         RST     0X30            
63DA: 9C         SBC     H               
63DB: E3         ???                     
63DC: BE         CP      (HL)            
63DD: C1         POP     BC              
63DE: BE         CP      (HL)            
63DF: C1         POP     BC              
63E0: FF         RST     0X38            
63E1: 00         NOP                     
63E2: FF         RST     0X38            
63E3: 00         NOP                     
63E4: FF         RST     0X38            
63E5: 00         NOP                     
63E6: FF         RST     0X38            
63E7: 00         NOP                     
63E8: 92         SUB     D               
63E9: 6D         LD      L,L             
63EA: 00         NOP                     
63EB: FF         RST     0X38            
63EC: 00         NOP                     
63ED: FF         RST     0X38            
63EE: 3C         INC     A               
63EF: C3 FD 03   JP      $03FD           
63F2: F9         LD      SP,HL           
63F3: 07         RLCA                    
63F4: F1         POP     AF              
63F5: 0F         RRCA                    
63F6: A1         AND     C               
63F7: 5F         LD      E,A             
63F8: 05         DEC     B               
63F9: FB         EI                      
63FA: 0D         DEC     C               
63FB: F3         DI                      
63FC: 2F         CPL                     
63FD: D3         ???                     
63FE: FF         RST     0X38            
63FF: 03         INC     BC              
6400: FE 00      CP      $00             
6402: 03         INC     BC              
6403: 00         NOP                     
6404: 1C         INC     E               
6405: 00         NOP                     
6406: E2         LDFF00  (C),A           
6407: 01 01 00   LD      BC,$0001        
640A: 06 01      LD      B,$01           
640C: 30 0F      JR      NC,$641D        
640E: C0         RET     NZ              
640F: 3F         CCF                     
6410: FF         RST     0X38            
6411: 01 81 01   LD      BC,$0181        
6414: 32         LD      (HLD),A         
6415: 0F         RRCA                    
6416: 0F         RRCA                    
6417: FC         ???                     
6418: BF         CP      A               
6419: 70         LD      (HL),B          
641A: 3F         CCF                     
641B: E0 5F      LDFF00  ($5F),A         
641D: E0 5F      LDFF00  ($5F),A         
641F: E0 BF      LDFF00  ($BF),A         
6421: C0         RET     NZ              
6422: 3F         CCF                     
6423: C0         RET     NZ              
6424: 2F         CPL                     
6425: D0         RET     NC              
6426: 0F         RRCA                    
6427: F0 07      LD      A,($07)         
6429: F8 E2      LDHL    SP,$E2          
642B: 1D         DEC     E               
642C: E0 1F      LDFF00  ($1F),A         
642E: F0 0F      LD      A,($0F)         
6430: FF         RST     0X38            
6431: 00         NOP                     
6432: FF         RST     0X38            
6433: 00         NOP                     
6434: FF         RST     0X38            
6435: 00         NOP                     
6436: FF         RST     0X38            
6437: 00         NOP                     
6438: 3F         CCF                     
6439: C0         RET     NZ              
643A: 19         ADD     HL,DE           
643B: E6 00      AND     $00             
643D: FF         RST     0X38            
643E: E0 1F      LDFF00  ($1F),A         
6440: FD         ???                     
6441: 03         INC     BC              
6442: FD         ???                     
6443: 03         INC     BC              
6444: F8 07      LDHL    SP,$07          
6446: F8 07      LDHL    SP,$07          
6448: B0         OR      B               
6449: 4F         LD      C,A             
644A: 01 FE 03   LD      BC,$03FE        
644D: FC         ???                     
644E: 07         RLCA                    
644F: F8 FF      LDHL    SP,$FF          
6451: 00         NOP                     
6452: C1         POP     BC              
6453: 80         ADD     A,B             
6454: CC 70 F0   CALL    Z,$F070         
6457: 3F         CCF                     
6458: FD         ???                     
6459: 0E FC      LD      C,$FC           
645B: 07         RLCA                    
645C: FA 07 FA   LD      A,($FA07)       
645F: 07         RLCA                    
6460: 7F         LD      A,A             
6461: 00         NOP                     
6462: C0         RET     NZ              
6463: 00         NOP                     
6464: 38 00      JR      C,$6466         
6466: 47         LD      B,A             
6467: 80         ADD     A,B             
6468: 80         ADD     A,B             
6469: 00         NOP                     
646A: 60         LD      H,B             
646B: 80         ADD     A,B             
646C: 0C         INC     C               
646D: F0 03      LD      A,($03)         
646F: FC         ???                     
6470: 40         LD      B,B             
6471: 3F         CCF                     
6472: 30 0F      JR      NC,$6483        
6474: 96         SUB     (HL)            
6475: 01 3C 03   LD      BC,$033C        
6478: 10 0F      STOP    $0F             
647A: 38 07      JR      C,$6483         
647C: FF         RST     0X38            
647D: 00         NOP                     
647E: 0F         RRCA                    
647F: 00         NOP                     
6480: 43         LD      B,E             
6481: FC         ???                     
6482: 61         LD      H,C             
6483: FE 3C      CP      $3C             
6485: FF         RST     0X38            
6486: 02         LD      (BC),A          
6487: FF         RST     0X38            
6488: 01 FF 00   LD      BC,$00FF        
648B: FF         RST     0X38            
648C: C0         RET     NZ              
648D: 3F         CCF                     
648E: 0E 01      LD      C,$01           
6490: F9         LD      SP,HL           
6491: 06 FF      LD      B,$FF           
6493: 00         NOP                     
6494: FF         RST     0X38            
6495: 00         NOP                     
6496: 7F         LD      A,A             
6497: 80         ADD     A,B             
6498: 1C         INC     E               
6499: E3         ???                     
649A: C7         RST     0X00            
649B: FF         RST     0X38            
649C: 78         LD      A,B             
649D: FF         RST     0X38            
649E: 00         NOP                     
649F: FF         RST     0X38            
64A0: F0 0F      LD      A,($0F)         
64A2: F9         LD      SP,HL           
64A3: 06 FF      LD      B,$FF           
64A5: 00         NOP                     
64A6: FF         RST     0X38            
64A7: 00         NOP                     
64A8: 7E         LD      A,(HL)          
64A9: 81         ADD     A,C             
64AA: BD         CP      L               
64AB: C3 FF FF   JP      $FFFF           
64AE: 00         NOP                     
64AF: FF         RST     0X38            
64B0: CF         RST     0X08            
64B1: 30 FF      JR      NC,$64B2        
64B3: 00         NOP                     
64B4: FF         RST     0X38            
64B5: 00         NOP                     
64B6: FE 01      CP      $01             
64B8: 3C         INC     A               
64B9: C3 E3 FF   JP      $FFE3           
64BC: 1E FF      LD      E,$FF           
64BE: 00         NOP                     
64BF: FF         RST     0X38            
64C0: C2 3F 86   JP      NZ,$863F        
64C3: 7F         LD      A,A             
64C4: 3C         INC     A               
64C5: FF         RST     0X38            
64C6: 40         LD      B,B             
64C7: FF         RST     0X38            
64C8: 80         ADD     A,B             
64C9: FF         RST     0X38            
64CA: 00         NOP                     
64CB: FF         RST     0X38            
64CC: 03         INC     BC              
64CD: FC         ???                     
64CE: 70         LD      (HL),B          
64CF: 80         ADD     A,B             
64D0: 02         LD      (BC),A          
64D1: FC         ???                     
64D2: 0C         INC     C               
64D3: F0 69      LD      A,($69)         
64D5: 80         ADD     A,B             
64D6: 3C         INC     A               
64D7: C0         RET     NZ              
64D8: 08 F0 1C   LD      ($1CF0),SP      
64DB: E0 FF      LDFF00  ($FF),A         
64DD: 00         NOP                     
64DE: F0 00      LD      A,($00)         
64E0: 1F         RRA                     
64E1: 0F         RRCA                    
64E2: F7         RST     0X30            
64E3: F8 FF      LDHL    SP,$FF          
64E5: 00         NOP                     
64E6: FF         RST     0X38            
64E7: 00         NOP                     
64E8: FF         RST     0X38            
64E9: 00         NOP                     
64EA: 80         ADD     A,B             
64EB: 7F         LD      A,A             
64EC: FF         RST     0X38            
64ED: FF         RST     0X38            
64EE: 3C         INC     A               
64EF: C3 FC FC   JP      $FCFC           
64F2: FA 0E 89   LD      A,($890E)       
64F5: 7F         LD      A,A             
64F6: F9         LD      SP,HL           
64F7: 0F         RRCA                    
64F8: FF         RST     0X38            
64F9: 07         RLCA                    
64FA: 7E         LD      A,(HL)          
64FB: 87         ADD     A,A             
64FC: 05         DEC     B               
64FD: FE FD      CP      $FD             
64FF: FE 00      CP      $00             
6501: 00         NOP                     
6502: 00         NOP                     
6503: FF         RST     0X38            
6504: 81         ADD     A,C             
6505: 3E 18      LD      A,$18           
6507: E7         RST     0X20            
6508: 00         NOP                     
6509: FF         RST     0X38            
650A: 30 CF      JR      NC,$64DB        
650C: 00         NOP                     
650D: FF         RST     0X38            
650E: 03         INC     BC              
650F: FC         ???                     
6510: 00         NOP                     
6511: 00         NOP                     
6512: 00         NOP                     
6513: FF         RST     0X38            
6514: 8C         ADC     A,H             
6515: 73         LD      (HL),E          
6516: 00         NOP                     
6517: FF         RST     0X38            
6518: 40         LD      B,B             
6519: 9F         SBC     A               
651A: 00         NOP                     
651B: FF         RST     0X38            
651C: 00         NOP                     
651D: FF         RST     0X38            
651E: 06 F9      LD      B,$F9           
6520: 00         NOP                     
6521: FF         RST     0X38            
6522: 00         NOP                     
6523: FF         RST     0X38            
6524: 00         NOP                     
6525: FF         RST     0X38            
6526: 30 CF      JR      NC,$64F7        
6528: 00         NOP                     
6529: FF         RST     0X38            
652A: 00         NOP                     
652B: FF         RST     0X38            
652C: 00         NOP                     
652D: FF         RST     0X38            
652E: 00         NOP                     
652F: FF         RST     0X38            
6530: 00         NOP                     
6531: FF         RST     0X38            
6532: 00         NOP                     
6533: FF         RST     0X38            
6534: 00         NOP                     
6535: FF         RST     0X38            
6536: 60         LD      H,B             
6537: 9F         SBC     A               
6538: 00         NOP                     
6539: FF         RST     0X38            
653A: 00         NOP                     
653B: FF         RST     0X38            
653C: 00         NOP                     
653D: FF         RST     0X38            
653E: 00         NOP                     
653F: FF         RST     0X38            
6540: 01 FE 2C   LD      BC,$2CFE        
6543: D3         ???                     
6544: 00         NOP                     
6545: FF         RST     0X38            
6546: 00         NOP                     
6547: FF         RST     0X38            
6548: 00         NOP                     
6549: FF         RST     0X38            
654A: 00         NOP                     
654B: FF         RST     0X38            
654C: 72         LD      (HL),D          
654D: 8C         ADC     A,H             
654E: 19         ADD     HL,DE           
654F: E0 C0      LDFF00  ($C0),A         
6551: 3F         CCF                     
6552: 34         INC     (HL)            
6553: CB 00      SET     1,E             
6555: FF         RST     0X38            
6556: 00         NOP                     
6557: FF         RST     0X38            
6558: 00         NOP                     
6559: FF         RST     0X38            
655A: 00         NOP                     
655B: FF         RST     0X38            
655C: 20 1F      JR      NZ,$657D        
655E: C2 01 04   JP      NZ,$0401        
6561: 03         INC     BC              
6562: 03         INC     BC              
6563: FF         RST     0X38            
6564: FF         RST     0X38            
6565: FF         RST     0X38            
6566: F0 FF      LD      A,($FF)         
6568: 00         NOP                     
6569: FF         RST     0X38            
656A: 00         NOP                     
656B: FF         RST     0X38            
656C: 07         RLCA                    
656D: F8 3B      LDHL    SP,$3B          
656F: C4 04 F8   CALL    NZ,$F804        
6572: E0 FF      LDFF00  ($FF),A         
6574: FF         RST     0X38            
6575: FF         RST     0X38            
6576: 0F         RRCA                    
6577: FF         RST     0X38            
6578: 00         NOP                     
6579: FF         RST     0X38            
657A: 00         NOP                     
657B: FF         RST     0X38            
657C: E0 1F      LDFF00  ($1F),A         
657E: FC         ???                     
657F: 03         INC     BC              
6580: 00         NOP                     
6581: 00         NOP                     
6582: 00         NOP                     
6583: FF         RST     0X38            
6584: 70         LD      (HL),B          
6585: 8F         ADC     A,A             
6586: 02         LD      (BC),A          
6587: F9         LD      SP,HL           
6588: 00         NOP                     
6589: FF         RST     0X38            
658A: 00         NOP                     
658B: FF         RST     0X38            
658C: 0C         INC     C               
658D: F3         DI                      
658E: 00         NOP                     
658F: FF         RST     0X38            
6590: 00         NOP                     
6591: 00         NOP                     
6592: 00         NOP                     
6593: FF         RST     0X38            
6594: C2 3C 00   JP      NZ,$003C        
6597: FF         RST     0X38            
6598: 30 CF      JR      NC,$6569        
659A: 00         NOP                     
659B: FF         RST     0X38            
659C: 00         NOP                     
659D: FF         RST     0X38            
659E: 01 FE 00   LD      BC,$00FE        
65A1: FF         RST     0X38            
65A2: 00         NOP                     
65A3: FF         RST     0X38            
65A4: 00         NOP                     
65A5: FF         RST     0X38            
65A6: 01 FE 40   LD      BC,$40FE        
65A9: BF         CP      A               
65AA: 00         NOP                     
65AB: FF         RST     0X38            
65AC: 00         NOP                     
65AD: FF         RST     0X38            
65AE: 00         NOP                     
65AF: FF         RST     0X38            
65B0: 00         NOP                     
65B1: FF         RST     0X38            
65B2: 00         NOP                     
65B3: FF         RST     0X38            
65B4: 00         NOP                     
65B5: FF         RST     0X38            
65B6: 80         ADD     A,B             
65B7: 7F         LD      A,A             
65B8: 02         LD      (BC),A          
65B9: FD         ???                     
65BA: 00         NOP                     
65BB: FF         RST     0X38            
65BC: 00         NOP                     
65BD: FF         RST     0X38            
65BE: 00         NOP                     
65BF: FF         RST     0X38            
65C0: 00         NOP                     
65C1: FF         RST     0X38            
65C2: 61         LD      H,C             
65C3: 9E         SBC     (HL)            
65C4: 07         RLCA                    
65C5: F8 FC      LDHL    SP,$FC          
65C7: 03         INC     BC              
65C8: 00         NOP                     
65C9: FF         RST     0X38            
65CA: 00         NOP                     
65CB: FF         RST     0X38            
65CC: 00         NOP                     
65CD: FF         RST     0X38            
65CE: 60         LD      H,B             
65CF: 9F         SBC     A               
65D0: 00         NOP                     
65D1: FF         RST     0X38            
65D2: C2 3D 38   JP      NZ,$383D        
65D5: C7         RST     0X00            
65D6: 07         RLCA                    
65D7: F8 00      LDHL    SP,$00          
65D9: FF         RST     0X38            
65DA: 00         NOP                     
65DB: FF         RST     0X38            
65DC: 00         NOP                     
65DD: FF         RST     0X38            
65DE: 38 C7      JR      C,$65A7         
65E0: 18 E0      JR      $65C2           
65E2: 07         RLCA                    
65E3: 00         NOP                     
65E4: F0 0F      LD      A,($0F)         
65E6: 00         NOP                     
65E7: FF         RST     0X38            
65E8: 00         NOP                     
65E9: FF         RST     0X38            
65EA: 07         RLCA                    
65EB: F8 3F      LDHL    SP,$3F          
65ED: C0         RET     NZ              
65EE: FB         EI                      
65EF: 04         INC     B               
65F0: 20 1F      JR      NZ,$6611        
65F2: C1         POP     BC              
65F3: 0E 30      LD      C,$30           
65F5: C0         RET     NZ              
65F6: 06 F9      LD      B,$F9           
65F8: 00         NOP                     
65F9: FF         RST     0X38            
65FA: 80         ADD     A,B             
65FB: 7F         LD      A,A             
65FC: F0 0F      LD      A,($0F)         
65FE: FF         RST     0X38            
65FF: 00         NOP                     
6600: 00         NOP                     
6601: 00         NOP                     
6602: 00         NOP                     
6603: FF         RST     0X38            
6604: 30 CE      JR      NC,$65D4        
6606: 00         NOP                     
6607: FF         RST     0X38            
6608: 06 F9      LD      B,$F9           
660A: 00         NOP                     
660B: FF         RST     0X38            
660C: 00         NOP                     
660D: FF         RST     0X38            
660E: 80         ADD     A,B             
660F: 7F         LD      A,A             
6610: 00         NOP                     
6611: 00         NOP                     
6612: 00         NOP                     
6613: FF         RST     0X38            
6614: 82         ADD     A,D             
6615: 7C         LD      A,H             
6616: 18 E7      JR      $65FF           
6618: 00         NOP                     
6619: FF         RST     0X38            
661A: 00         NOP                     
661B: FF         RST     0X38            
661C: 00         NOP                     
661D: FF         RST     0X38            
661E: 0C         INC     C               
661F: F3         DI                      
6620: 00         NOP                     
6621: FF         RST     0X38            
6622: 00         NOP                     
6623: FF         RST     0X38            
6624: 00         NOP                     
6625: FF         RST     0X38            
6626: 0C         INC     C               
6627: F3         DI                      
6628: 00         NOP                     
6629: FF         RST     0X38            
662A: 00         NOP                     
662B: FF         RST     0X38            
662C: 00         NOP                     
662D: FF         RST     0X38            
662E: 00         NOP                     
662F: FF         RST     0X38            
6630: 00         NOP                     
6631: FF         RST     0X38            
6632: 00         NOP                     
6633: FF         RST     0X38            
6634: 00         NOP                     
6635: FF         RST     0X38            
6636: 00         NOP                     
6637: FF         RST     0X38            
6638: 02         LD      (BC),A          
6639: FD         ???                     
663A: 00         NOP                     
663B: FF         RST     0X38            
663C: 00         NOP                     
663D: FF         RST     0X38            
663E: 00         NOP                     
663F: FF         RST     0X38            
6640: 00         NOP                     
6641: FF         RST     0X38            
6642: 00         NOP                     
6643: FF         RST     0X38            
6644: 30 CF      JR      NC,$6615        
6646: 07         RLCA                    
6647: F8 8E      LDHL    SP,$8E          
6649: 71         LD      (HL),C          
664A: F8 07      LDHL    SP,$07          
664C: 00         NOP                     
664D: FF         RST     0X38            
664E: 00         NOP                     
664F: FF         RST     0X38            
6650: 00         NOP                     
6651: FF         RST     0X38            
6652: 00         NOP                     
6653: FF         RST     0X38            
6654: 06 F9      LD      B,$F9           
6656: F0 0F      LD      A,($0F)         
6658: 3F         CCF                     
6659: C0         RET     NZ              
665A: 00         NOP                     
665B: FF         RST     0X38            
665C: 00         NOP                     
665D: FF         RST     0X38            
665E: 00         NOP                     
665F: FF         RST     0X38            
6660: 00         NOP                     
6661: FF         RST     0X38            
6662: 00         NOP                     
6663: FF         RST     0X38            
6664: 0C         INC     C               
6665: F3         DI                      
6666: 73         LD      (HL),E          
6667: 8C         ADC     A,H             
6668: 18 E0      JR      $664A           
666A: 04         INC     B               
666B: 00         NOP                     
666C: FF         RST     0X38            
666D: 00         NOP                     
666E: FF         RST     0X38            
666F: 00         NOP                     
6670: 00         NOP                     
6671: FF         RST     0X38            
6672: 00         NOP                     
6673: FF         RST     0X38            
6674: 19         ADD     HL,DE           
6675: E6 E6      AND     $E6             
6677: 19         ADD     HL,DE           
6678: 0D         DEC     C               
6679: 00         NOP                     
667A: 30 00      JR      NC,$667C        
667C: FF         RST     0X38            
667D: 00         NOP                     
667E: FF         RST     0X38            
667F: 00         NOP                     
6680: 00         NOP                     
6681: 00         NOP                     
6682: 00         NOP                     
6683: FF         RST     0X38            
6684: C3 3C 00   JP      $003C           
6687: FF         RST     0X38            
6688: 0C         INC     C               
6689: F3         DI                      
668A: 00         NOP                     
668B: FF         RST     0X38            
668C: 00         NOP                     
668D: FF         RST     0X38            
668E: 30 CF      JR      NC,$665F        
6690: 00         NOP                     
6691: 00         NOP                     
6692: 00         NOP                     
6693: FF         RST     0X38            
6694: 0A         LD      A,(BC)          
6695: F1         POP     AF              
6696: 20 9F      JR      NZ,$6637        
6698: 00         NOP                     
6699: FF         RST     0X38            
669A: 00         NOP                     
669B: FF         RST     0X38            
669C: 00         NOP                     
669D: FF         RST     0X38            
669E: C0         RET     NZ              
669F: 3F         CCF                     
66A0: 00         NOP                     
66A1: FF         RST     0X38            
66A2: 00         NOP                     
66A3: FF         RST     0X38            
66A4: 00         NOP                     
66A5: FF         RST     0X38            
66A6: 00         NOP                     
66A7: FF         RST     0X38            
66A8: 60         LD      H,B             
66A9: 9F         SBC     A               
66AA: 00         NOP                     
66AB: FF         RST     0X38            
66AC: 00         NOP                     
66AD: FF         RST     0X38            
66AE: 01 FE 00   LD      BC,$00FE        
66B1: FF         RST     0X38            
66B2: 00         NOP                     
66B3: FF         RST     0X38            
66B4: 00         NOP                     
66B5: FF         RST     0X38            
66B6: 00         NOP                     
66B7: FF         RST     0X38            
66B8: 18 E7      JR      $66A1           
66BA: 00         NOP                     
66BB: FF         RST     0X38            
66BC: 00         NOP                     
66BD: FF         RST     0X38            
66BE: C0         RET     NZ              
66BF: 3F         CCF                     
66C0: 00         NOP                     
66C1: FF         RST     0X38            
66C2: 00         NOP                     
66C3: FF         RST     0X38            
66C4: 00         NOP                     
66C5: FF         RST     0X38            
66C6: 00         NOP                     
66C7: FF         RST     0X38            
66C8: 40         LD      B,B             
66C9: BF         CP      A               
66CA: 18 E0      JR      $66AC           
66CC: C8         RET     Z               
66CD: 07         RLCA                    
66CE: 60         LD      H,B             
66CF: 9F         SBC     A               
66D0: 00         NOP                     
66D1: FF         RST     0X38            
66D2: 00         NOP                     
66D3: FF         RST     0X38            
66D4: 00         NOP                     
66D5: FF         RST     0X38            
66D6: 00         NOP                     
66D7: FF         RST     0X38            
66D8: 00         NOP                     
66D9: FF         RST     0X38            
66DA: 70         LD      (HL),B          
66DB: 0F         RRCA                    
66DC: 18 E0      JR      $66BE           
66DE: 0E F1      LD      C,$F1           
66E0: 0F         RRCA                    
66E1: FF         RST     0X38            
66E2: E0 FF      LDFF00  ($FF),A         
66E4: 00         NOP                     
66E5: FF         RST     0X38            
66E6: 00         NOP                     
66E7: FF         RST     0X38            
66E8: C7         RST     0X00            
66E9: 38 38      JR      C,$6723         
66EB: C7         RST     0X00            
66EC: C4 38 17   CALL    NZ,$1738        
66EF: E0 E0      LDFF00  ($E0),A         
66F1: FF         RST     0X38            
66F2: 0F         RRCA                    
66F3: FF         RST     0X38            
66F4: 00         NOP                     
66F5: FF         RST     0X38            
66F6: 00         NOP                     
66F7: FF         RST     0X38            
66F8: C1         POP     BC              
66F9: 3E 3C      LD      A,$3C           
66FB: C3 67 18   JP      $1867           
66FE: C4 03 03   CALL    NZ,$0303        
6701: 00         NOP                     
6702: 04         INC     B               
6703: 03         INC     BC              
6704: 39         ADD     HL,SP           
6705: 07         RLCA                    
6706: 40         LD      B,B             
6707: 3F         CCF                     
6708: 40         LD      B,B             
6709: 3F         CCF                     
670A: 20 1F      JR      NZ,$672B        
670C: 30 0F      JR      NC,$671D        
670E: 20 1F      JR      NZ,$672F        
6710: 10 0F      STOP    $0F             
6712: 20 1F      JR      NZ,$6733        
6714: 20 1F      JR      NZ,$6735        
6716: 30 0F      JR      NC,$6727        
6718: 1C         INC     E               
6719: 03         INC     BC              
671A: 13         INC     DE              
671B: 0C         INC     C               
671C: 08 07 07   LD      ($0707),SP      
671F: 00         NOP                     
6720: 03         INC     BC              
6721: 00         NOP                     
6722: 07         RLCA                    
6723: 03         INC     BC              
6724: 1B         DEC     DE              
6725: 04         INC     B               
6726: 3D         DEC     A               
6727: 13         INC     DE              
6728: 39         ADD     HL,SP           
6729: 17         RLA                     
672A: 38 17      JR      C,$6743         
672C: 29         ADD     HL,HL           
672D: 17         RLA                     
672E: 18 07      JR      $6737           
6730: 14         INC     D               
6731: 0B         DEC     BC              
6732: 22         LD      (HLI),A         
6733: 1D         DEC     E               
6734: 21 1E 38   LD      HL,$381E        
6737: 07         RLCA                    
6738: 18 0F      JR      $6749           
673A: 17         RLA                     
673B: 0F         RRCA                    
673C: 08 07 07   LD      ($0707),SP      
673F: 00         NOP                     
6740: C0         RET     NZ              
6741: 00         NOP                     
6742: E0 C0      LDFF00  ($C0),A         
6744: F8 20      LDHL    SP,$20          
6746: 3C         INC     A               
6747: C8         RET     Z               
6748: 1C         INC     E               
6749: E8 5C      ADD     SP,$5C          
674B: A8         XOR     B               
674C: 34         INC     (HL)            
674D: C8         RET     Z               
674E: 98         SBC     B               
674F: E0 18      LDFF00  ($18),A         
6751: E0 14      LDFF00  ($14),A         
6753: E8 24      ADD     SP,$24          
6755: D8         RET     C               
6756: CC 30 18   CALL    Z,$1830         
6759: F0 E8      LD      A,($E8)         
675B: F0 10      LD      A,($10)         
675D: E0 E0      LDFF00  ($E0),A         
675F: 00         NOP                     
6760: 0F         RRCA                    
6761: 00         NOP                     
6762: 36 0F      LD      (HL),$0F        
6764: 60         LD      H,B             
6765: 3F         CCF                     
6766: 50         LD      D,B             
6767: 2F         CPL                     
6768: 33         INC     SP              
6769: 0C         INC     C               
676A: 1F         RRA                     
676B: 02         LD      (BC),A          
676C: 1F         RRA                     
676D: 0A         LD      A,(BC)          
676E: 3F         CCF                     
676F: 1E 2E      LD      E,$2E           
6771: 1D         DEC     E               
6772: 14         INC     D               
6773: 0B         DEC     BC              
6774: 0C         INC     C               
6775: 03         INC     BC              
6776: 14         INC     D               
6777: 0B         DEC     BC              
6778: 1B         DEC     DE              
6779: 04         INC     B               
677A: 10 0F      STOP    $0F             
677C: 08 07 07   LD      ($0707),SP      
677F: 00         NOP                     
6780: 80         ADD     A,B             
6781: 00         NOP                     
6782: 40         LD      B,B             
6783: 80         ADD     A,B             
6784: 30 C0      JR      NC,$6746        
6786: 08 F0 04   LD      ($04F0),SP      
6789: F8 04      LDHL    SP,$04          
678B: F8 08      LDHL    SP,$08          
678D: F0 04      LD      A,($04)         
678F: F8 04      LDHL    SP,$04          
6791: F8 02      LDHL    SP,$02          
6793: FC         ???                     
6794: 02         LD      (BC),A          
6795: FC         ???                     
6796: 02         LD      (BC),A          
6797: FC         ???                     
6798: 04         INC     B               
6799: F8 F8      LDHL    SP,$F8          
679B: 00         NOP                     
679C: 10 E0      STOP    $E0             
679E: E0 00      LDFF00  ($00),A         
67A0: 00         NOP                     
67A1: 00         NOP                     
67A2: 00         NOP                     
67A3: 00         NOP                     
67A4: 44         LD      B,H             
67A5: 00         NOP                     
67A6: 28 00      JR      Z,$67A8         
67A8: 10 00      STOP    $00             
67AA: 28 00      JR      Z,$67AC         
67AC: 44         LD      B,H             
67AD: 00         NOP                     
67AE: 00         NOP                     
67AF: 00         NOP                     
67B0: 00         NOP                     
67B1: 00         NOP                     
67B2: 00         NOP                     
67B3: 00         NOP                     
67B4: 44         LD      B,H             
67B5: 00         NOP                     
67B6: 28 00      JR      Z,$67B8         
67B8: 10 00      STOP    $00             
67BA: 28 00      JR      Z,$67BC         
67BC: 44         LD      B,H             
67BD: 00         NOP                     
67BE: 00         NOP                     
67BF: 00         NOP                     
67C0: 00         NOP                     
67C1: 00         NOP                     
67C2: 00         NOP                     
67C3: 00         NOP                     
67C4: 00         NOP                     
67C5: 00         NOP                     
67C6: 01 00 0F   LD      BC,$0F00        
67C9: 01 1F 0E   LD      BC,$0E1F        
67CC: 0E 00      LD      C,$00           
67CE: 00         NOP                     
67CF: 00         NOP                     
67D0: 00         NOP                     
67D1: 00         NOP                     
67D2: 00         NOP                     
67D3: 00         NOP                     
67D4: 00         NOP                     
67D5: 00         NOP                     
67D6: 00         NOP                     
67D7: 00         NOP                     
67D8: 00         NOP                     
67D9: 00         NOP                     
67DA: 00         NOP                     
67DB: 00         NOP                     
67DC: 00         NOP                     
67DD: 00         NOP                     
67DE: 00         NOP                     
67DF: 00         NOP                     
67E0: 00         NOP                     
67E1: 00         NOP                     
67E2: 00         NOP                     
67E3: 00         NOP                     
67E4: 01 00 03   LD      BC,$0300        
67E7: 01 07 02   LD      BC,$0207        
67EA: 0E 04      LD      C,$04           
67EC: 0E 04      LD      C,$04           
67EE: 04         INC     B               
67EF: 00         NOP                     
67F0: 00         NOP                     
67F1: 00         NOP                     
67F2: 00         NOP                     
67F3: 00         NOP                     
67F4: 00         NOP                     
67F5: 00         NOP                     
67F6: 00         NOP                     
67F7: 00         NOP                     
67F8: 00         NOP                     
67F9: 00         NOP                     
67FA: 00         NOP                     
67FB: 00         NOP                     
67FC: 00         NOP                     
67FD: 00         NOP                     
67FE: 00         NOP                     
67FF: 00         NOP                     
6800: 00         NOP                     
6801: 00         NOP                     
6802: 00         NOP                     
6803: 00         NOP                     
6804: 38 00      JR      C,$6806         
6806: 7C         LD      A,H             
6807: 38 9E      JR      C,$67A7         
6809: 7C         LD      A,H             
680A: 9F         SBC     A               
680B: 66         LD      H,(HL)          
680C: F7         RST     0X30            
680D: 03         INC     BC              
680E: 07         RLCA                    
680F: 03         INC     BC              
6810: 02         LD      (BC),A          
6811: 01 01 00   LD      BC,$0001        
6814: 00         NOP                     
6815: 00         NOP                     
6816: 00         NOP                     
6817: 00         NOP                     
6818: 00         NOP                     
6819: 00         NOP                     
681A: 00         NOP                     
681B: 00         NOP                     
681C: 00         NOP                     
681D: 00         NOP                     
681E: 00         NOP                     
681F: 00         NOP                     
6820: 38 00      JR      C,$6822         
6822: 7C         LD      A,H             
6823: 38 BE      JR      C,$67E3         
6825: 7C         LD      A,H             
6826: 9E         SBC     (HL)            
6827: 7C         LD      A,H             
6828: 9E         SBC     (HL)            
6829: 64         LD      H,H             
682A: 6F         LD      L,A             
682B: 06 07      LD      B,$07           
682D: 03         INC     BC              
682E: 07         RLCA                    
682F: 03         INC     BC              
6830: 02         LD      (BC),A          
6831: 01 01 00   LD      BC,$0001        
6834: 00         NOP                     
6835: 00         NOP                     
6836: 00         NOP                     
6837: 00         NOP                     
6838: 00         NOP                     
6839: 00         NOP                     
683A: 00         NOP                     
683B: 00         NOP                     
683C: 00         NOP                     
683D: 00         NOP                     
683E: 00         NOP                     
683F: 00         NOP                     
6840: E0 00      LDFF00  ($00),A         
6842: 90         SUB     B               
6843: 60         LD      H,B             
6844: 90         SUB     B               
6845: 60         LD      H,B             
6846: F8 70      LDHL    SP,$70          
6848: 78         LD      A,B             
6849: 30 3F      JR      NC,$688A        
684B: 18 1F      JR      $686C           
684D: 0F         RRCA                    
684E: 0F         RRCA                    
684F: 07         RLCA                    
6850: 06 01      LD      B,$01           
6852: 01 00 00   LD      BC,$0000        
6855: 00         NOP                     
6856: 00         NOP                     
6857: 00         NOP                     
6858: 00         NOP                     
6859: 00         NOP                     
685A: 00         NOP                     
685B: 00         NOP                     
685C: 00         NOP                     
685D: 00         NOP                     
685E: 00         NOP                     
685F: 00         NOP                     
6860: 00         NOP                     
6861: 00         NOP                     
6862: 00         NOP                     
6863: 00         NOP                     
6864: 00         NOP                     
6865: 00         NOP                     
6866: 60         LD      H,B             
6867: 00         NOP                     
6868: 90         SUB     B               
6869: 60         LD      H,B             
686A: 91         SUB     C               
686B: 60         LD      H,B             
686C: EF         RST     0X28            
686D: 71         LD      (HL),C          
686E: FF         RST     0X38            
686F: 3F         CCF                     
6870: 3E 19      LD      A,$19           
6872: 19         ADD     HL,DE           
6873: 00         NOP                     
6874: 00         NOP                     
6875: 00         NOP                     
6876: 00         NOP                     
6877: 00         NOP                     
6878: 00         NOP                     
6879: 00         NOP                     
687A: 00         NOP                     
687B: 00         NOP                     
687C: 00         NOP                     
687D: 00         NOP                     
687E: 00         NOP                     
687F: 00         NOP                     
6880: 00         NOP                     
6881: 00         NOP                     
6882: 00         NOP                     
6883: 00         NOP                     
6884: 00         NOP                     
6885: 00         NOP                     
6886: 00         NOP                     
6887: 00         NOP                     
6888: 00         NOP                     
6889: 00         NOP                     
688A: 01 00 03   LD      BC,$0300        
688D: 01 07 03   LD      BC,$0307        
6890: 06 03      LD      B,$03           
6892: 07         RLCA                    
6893: 02         LD      (BC),A          
6894: 0F         RRCA                    
6895: 06 1F      LD      B,$1F           
6897: 0E 7E      LD      C,$7E           
6899: 1C         INC     E               
689A: 9E         SBC     (HL)            
689B: 7C         LD      A,H             
689C: 8C         ADC     A,H             
689D: 78         LD      A,B             
689E: F8 00      LDHL    SP,$00          
68A0: 00         NOP                     
68A1: 00         NOP                     
68A2: 00         NOP                     
68A3: 00         NOP                     
68A4: 00         NOP                     
68A5: 00         NOP                     
68A6: 00         NOP                     
68A7: 00         NOP                     
68A8: 00         NOP                     
68A9: 00         NOP                     
68AA: 03         INC     BC              
68AB: 00         NOP                     
68AC: 0F         RRCA                    
68AD: 03         INC     BC              
68AE: 1F         RRA                     
68AF: 0F         RRCA                    
68B0: 3E 19      LD      A,$19           
68B2: 7D         LD      A,L             
68B3: 38 78      JR      C,$692D         
68B5: 30 F8      JR      NC,$68AF        
68B7: 70         LD      (HL),B          
68B8: 88         ADC     A,B             
68B9: 70         LD      (HL),B          
68BA: 88         ADC     A,B             
68BB: 70         LD      (HL),B          
68BC: 48         LD      C,B             
68BD: 30 38      JR      NC,$68F7        
68BF: 00         NOP                     
68C0: 00         NOP                     
68C1: 00         NOP                     
68C2: 02         LD      (BC),A          
68C3: 00         NOP                     
68C4: 07         RLCA                    
68C5: 02         LD      (BC),A          
68C6: 07         RLCA                    
68C7: 02         LD      (BC),A          
68C8: 0F         RRCA                    
68C9: 05         DEC     B               
68CA: 0D         DEC     C               
68CB: 00         NOP                     
68CC: 00         NOP                     
68CD: 00         NOP                     
68CE: 00         NOP                     
68CF: 00         NOP                     
68D0: 00         NOP                     
68D1: 00         NOP                     
68D2: 00         NOP                     
68D3: 00         NOP                     
68D4: 00         NOP                     
68D5: 00         NOP                     
68D6: 00         NOP                     
68D7: 00         NOP                     
68D8: 00         NOP                     
68D9: 00         NOP                     
68DA: 00         NOP                     
68DB: 00         NOP                     
68DC: 00         NOP                     
68DD: 00         NOP                     
68DE: 00         NOP                     
68DF: 00         NOP                     
68E0: 00         NOP                     
68E1: 00         NOP                     
68E2: 00         NOP                     
68E3: 00         NOP                     
68E4: 0C         INC     C               
68E5: 00         NOP                     
68E6: 1E 0C      LD      E,$0C           
68E8: 0F         RRCA                    
68E9: 02         LD      (BC),A          
68EA: 03         INC     BC              
68EB: 01 01 00   LD      BC,$0001        
68EE: 00         NOP                     
68EF: 00         NOP                     
68F0: 00         NOP                     
68F1: 00         NOP                     
68F2: 00         NOP                     
68F3: 00         NOP                     
68F4: 00         NOP                     
68F5: 00         NOP                     
68F6: 00         NOP                     
68F7: 00         NOP                     
68F8: 00         NOP                     
68F9: 00         NOP                     
68FA: 00         NOP                     
68FB: 00         NOP                     
68FC: 00         NOP                     
68FD: 00         NOP                     
68FE: 00         NOP                     
68FF: 00         NOP                     
6900: FF         RST     0X38            
6901: 00         NOP                     
6902: FF         RST     0X38            
6903: 42         LD      B,D             
6904: FF         RST     0X38            
6905: 24         INC     H               
6906: FF         RST     0X38            
6907: 18 FF      JR      $6908           
6909: 18 FF      JR      $690A           
690B: 24         INC     H               
690C: FF         RST     0X38            
690D: 42         LD      B,D             
690E: FF         RST     0X38            
690F: 00         NOP                     
6910: FF         RST     0X38            
6911: 00         NOP                     
6912: FF         RST     0X38            
6913: 42         LD      B,D             
6914: FF         RST     0X38            
6915: 24         INC     H               
6916: FF         RST     0X38            
6917: 18 FF      JR      $6918           
6919: 18 FF      JR      $691A           
691B: 24         INC     H               
691C: FF         RST     0X38            
691D: 42         LD      B,D             
691E: FF         RST     0X38            
691F: 00         NOP                     
6920: FF         RST     0X38            
6921: 00         NOP                     
6922: FF         RST     0X38            
6923: 42         LD      B,D             
6924: FF         RST     0X38            
6925: 24         INC     H               
6926: FF         RST     0X38            
6927: 18 FF      JR      $6928           
6929: 18 FF      JR      $692A           
692B: 24         INC     H               
692C: FF         RST     0X38            
692D: 42         LD      B,D             
692E: FF         RST     0X38            
692F: 00         NOP                     
6930: FF         RST     0X38            
6931: 00         NOP                     
6932: FF         RST     0X38            
6933: 42         LD      B,D             
6934: FF         RST     0X38            
6935: 24         INC     H               
6936: FF         RST     0X38            
6937: 18 FF      JR      $6938           
6939: 18 FF      JR      $693A           
693B: 24         INC     H               
693C: FF         RST     0X38            
693D: 42         LD      B,D             
693E: FF         RST     0X38            
693F: 00         NOP                     
6940: FF         RST     0X38            
6941: 00         NOP                     
6942: FF         RST     0X38            
6943: 42         LD      B,D             
6944: FF         RST     0X38            
6945: 24         INC     H               
6946: FF         RST     0X38            
6947: 18 FF      JR      $6948           
6949: 18 FF      JR      $694A           
694B: 24         INC     H               
694C: FF         RST     0X38            
694D: 42         LD      B,D             
694E: FF         RST     0X38            
694F: 00         NOP                     
6950: FF         RST     0X38            
6951: 00         NOP                     
6952: FF         RST     0X38            
6953: 42         LD      B,D             
6954: FF         RST     0X38            
6955: 24         INC     H               
6956: FF         RST     0X38            
6957: 18 FF      JR      $6958           
6959: 18 FF      JR      $695A           
695B: 24         INC     H               
695C: FF         RST     0X38            
695D: 42         LD      B,D             
695E: FF         RST     0X38            
695F: 00         NOP                     
6960: FF         RST     0X38            
6961: 00         NOP                     
6962: FF         RST     0X38            
6963: 42         LD      B,D             
6964: FF         RST     0X38            
6965: 24         INC     H               
6966: FF         RST     0X38            
6967: 18 FF      JR      $6968           
6969: 18 FF      JR      $696A           
696B: 24         INC     H               
696C: FF         RST     0X38            
696D: 42         LD      B,D             
696E: FF         RST     0X38            
696F: 00         NOP                     
6970: FF         RST     0X38            
6971: 00         NOP                     
6972: FF         RST     0X38            
6973: 42         LD      B,D             
6974: FF         RST     0X38            
6975: 24         INC     H               
6976: FF         RST     0X38            
6977: 18 FF      JR      $6978           
6979: 18 FF      JR      $697A           
697B: 24         INC     H               
697C: FF         RST     0X38            
697D: 42         LD      B,D             
697E: FF         RST     0X38            
697F: 00         NOP                     
6980: FF         RST     0X38            
6981: 00         NOP                     
6982: FF         RST     0X38            
6983: 42         LD      B,D             
6984: FF         RST     0X38            
6985: 24         INC     H               
6986: FF         RST     0X38            
6987: 18 FF      JR      $6988           
6989: 18 FF      JR      $698A           
698B: 24         INC     H               
698C: FF         RST     0X38            
698D: 42         LD      B,D             
698E: FF         RST     0X38            
698F: 00         NOP                     
6990: FF         RST     0X38            
6991: 00         NOP                     
6992: FF         RST     0X38            
6993: 42         LD      B,D             
6994: FF         RST     0X38            
6995: 24         INC     H               
6996: FF         RST     0X38            
6997: 18 FF      JR      $6998           
6999: 18 FF      JR      $699A           
699B: 24         INC     H               
699C: FF         RST     0X38            
699D: 42         LD      B,D             
699E: FF         RST     0X38            
699F: 00         NOP                     
69A0: FF         RST     0X38            
69A1: 00         NOP                     
69A2: FF         RST     0X38            
69A3: 42         LD      B,D             
69A4: FF         RST     0X38            
69A5: 24         INC     H               
69A6: FF         RST     0X38            
69A7: 18 FF      JR      $69A8           
69A9: 18 FF      JR      $69AA           
69AB: 24         INC     H               
69AC: FF         RST     0X38            
69AD: 42         LD      B,D             
69AE: FF         RST     0X38            
69AF: 00         NOP                     
69B0: FF         RST     0X38            
69B1: 00         NOP                     
69B2: FF         RST     0X38            
69B3: 42         LD      B,D             
69B4: FF         RST     0X38            
69B5: 24         INC     H               
69B6: FF         RST     0X38            
69B7: 18 FF      JR      $69B8           
69B9: 18 FF      JR      $69BA           
69BB: 24         INC     H               
69BC: FF         RST     0X38            
69BD: 42         LD      B,D             
69BE: FF         RST     0X38            
69BF: 00         NOP                     
69C0: FF         RST     0X38            
69C1: 00         NOP                     
69C2: FF         RST     0X38            
69C3: 42         LD      B,D             
69C4: FF         RST     0X38            
69C5: 24         INC     H               
69C6: FF         RST     0X38            
69C7: 18 FF      JR      $69C8           
69C9: 18 FF      JR      $69CA           
69CB: 24         INC     H               
69CC: FF         RST     0X38            
69CD: 42         LD      B,D             
69CE: FF         RST     0X38            
69CF: 00         NOP                     
69D0: FF         RST     0X38            
69D1: 00         NOP                     
69D2: FF         RST     0X38            
69D3: 42         LD      B,D             
69D4: FF         RST     0X38            
69D5: 24         INC     H               
69D6: FF         RST     0X38            
69D7: 18 FF      JR      $69D8           
69D9: 18 FF      JR      $69DA           
69DB: 24         INC     H               
69DC: FF         RST     0X38            
69DD: 42         LD      B,D             
69DE: FF         RST     0X38            
69DF: 00         NOP                     
69E0: FF         RST     0X38            
69E1: 00         NOP                     
69E2: FF         RST     0X38            
69E3: 42         LD      B,D             
69E4: FF         RST     0X38            
69E5: 24         INC     H               
69E6: FF         RST     0X38            
69E7: 18 FF      JR      $69E8           
69E9: 18 FF      JR      $69EA           
69EB: 24         INC     H               
69EC: FF         RST     0X38            
69ED: 42         LD      B,D             
69EE: FF         RST     0X38            
69EF: 00         NOP                     
69F0: FF         RST     0X38            
69F1: 00         NOP                     
69F2: FF         RST     0X38            
69F3: 42         LD      B,D             
69F4: FF         RST     0X38            
69F5: 24         INC     H               
69F6: FF         RST     0X38            
69F7: 18 FF      JR      $69F8           
69F9: 18 FF      JR      $69FA           
69FB: 24         INC     H               
69FC: FF         RST     0X38            
69FD: 42         LD      B,D             
69FE: FF         RST     0X38            
69FF: 00         NOP                     
6A00: 00         NOP                     
6A01: 00         NOP                     
6A02: 7E         LD      A,(HL)          
6A03: 00         NOP                     
6A04: FF         RST     0X38            
6A05: 3C         INC     A               
6A06: FF         RST     0X38            
6A07: 66         LD      H,(HL)          
6A08: FF         RST     0X38            
6A09: 66         LD      H,(HL)          
6A0A: FF         RST     0X38            
6A0B: 66         LD      H,(HL)          
6A0C: FF         RST     0X38            
6A0D: 66         LD      H,(HL)          
6A0E: FF         RST     0X38            
6A0F: 66         LD      H,(HL)          
6A10: 00         NOP                     
6A11: 00         NOP                     
6A12: FE 00      CP      $00             
6A14: FF         RST     0X38            
6A15: 7C         LD      A,H             
6A16: FF         RST     0X38            
6A17: 66         LD      H,(HL)          
6A18: FF         RST     0X38            
6A19: 66         LD      H,(HL)          
6A1A: FF         RST     0X38            
6A1B: 66         LD      H,(HL)          
6A1C: FF         RST     0X38            
6A1D: 66         LD      H,(HL)          
6A1E: FE 7C      CP      $7C             
6A20: 00         NOP                     
6A21: 00         NOP                     
6A22: 7E         LD      A,(HL)          
6A23: 00         NOP                     
6A24: FF         RST     0X38            
6A25: 3C         INC     A               
6A26: FF         RST     0X38            
6A27: 66         LD      H,(HL)          
6A28: FF         RST     0X38            
6A29: 66         LD      H,(HL)          
6A2A: FF         RST     0X38            
6A2B: 66         LD      H,(HL)          
6A2C: FF         RST     0X38            
6A2D: 60         LD      H,B             
6A2E: F0 60      LD      A,($60)         
6A30: 00         NOP                     
6A31: 00         NOP                     
6A32: FC         ???                     
6A33: 00         NOP                     
6A34: FE 78      CP      $78             
6A36: FF         RST     0X38            
6A37: 64         LD      H,H             
6A38: FF         RST     0X38            
6A39: 66         LD      H,(HL)          
6A3A: FF         RST     0X38            
6A3B: 66         LD      H,(HL)          
6A3C: FF         RST     0X38            
6A3D: 66         LD      H,(HL)          
6A3E: FF         RST     0X38            
6A3F: 66         LD      H,(HL)          
6A40: 00         NOP                     
6A41: 00         NOP                     
6A42: FF         RST     0X38            
6A43: 00         NOP                     
6A44: FF         RST     0X38            
6A45: 7E         LD      A,(HL)          
6A46: FF         RST     0X38            
6A47: 60         LD      H,B             
6A48: F0 60      LD      A,($60)         
6A4A: F0 60      LD      A,($60)         
6A4C: FE 60      CP      $60             
6A4E: FE 7C      CP      $7C             
6A50: FF         RST     0X38            
6A51: 3C         INC     A               
6A52: 7E         LD      A,(HL)          
6A53: 18 3C      JR      $6A91           
6A55: 18 3C      JR      $6A93           
6A57: 18 3C      JR      $6A95           
6A59: 18 3C      JR      $6A97           
6A5B: 18 3C      JR      $6A99           
6A5D: 00         NOP                     
6A5E: 00         NOP                     
6A5F: 00         NOP                     
6A60: FE 7C      CP      $7C             
6A62: FF         RST     0X38            
6A63: 66         LD      H,(HL)          
6A64: FF         RST     0X38            
6A65: 66         LD      H,(HL)          
6A66: FF         RST     0X38            
6A67: 66         LD      H,(HL)          
6A68: FF         RST     0X38            
6A69: 66         LD      H,(HL)          
6A6A: FF         RST     0X38            
6A6B: 66         LD      H,(HL)          
6A6C: FF         RST     0X38            
6A6D: 00         NOP                     
6A6E: 00         NOP                     
6A6F: 00         NOP                     
6A70: 00         NOP                     
6A71: 00         NOP                     
6A72: 7E         LD      A,(HL)          
6A73: 00         NOP                     
6A74: 7E         LD      A,(HL)          
6A75: 3C         INC     A               
6A76: 3C         INC     A               
6A77: 18 3C      JR      $6AB5           
6A79: 18 3C      JR      $6AB7           
6A7B: 18 3C      JR      $6AB9           
6A7D: 18 3C      JR      $6ABB           
6A7F: 18 00      JR      $6A81           
6A81: 00         NOP                     
6A82: 3F         CCF                     
6A83: 00         NOP                     
6A84: 3F         CCF                     
6A85: 1E 3F      LD      E,$3F           
6A87: 0C         INC     C               
6A88: 1E 0C      LD      E,$0C           
6A8A: 1E 0C      LD      E,$0C           
6A8C: 1E 0C      LD      E,$0C           
6A8E: 1E 0C      LD      E,$0C           
6A90: 00         NOP                     
6A91: 00         NOP                     
6A92: FF         RST     0X38            
6A93: 00         NOP                     
6A94: FF         RST     0X38            
6A95: 66         LD      H,(HL)          
6A96: FF         RST     0X38            
6A97: 66         LD      H,(HL)          
6A98: FE 6C      CP      $6C             
6A9A: FC         ???                     
6A9B: 78         LD      A,B             
6A9C: F8 70      LDHL    SP,$70          
6A9E: F8 70      LDHL    SP,$70          
6AA0: 00         NOP                     
6AA1: 00         NOP                     
6AA2: F7         RST     0X30            
6AA3: 00         NOP                     
6AA4: F7         RST     0X30            
6AA5: 62         LD      H,D             
6AA6: FF         RST     0X38            
6AA7: 62         LD      H,D             
6AA8: FF         RST     0X38            
6AA9: 76         HALT                    
6AAA: FF         RST     0X38            
6AAB: 7E         LD      A,(HL)          
6AAC: FF         RST     0X38            
6AAD: 7E         LD      A,(HL)          
6AAE: FF         RST     0X38            
6AAF: 7E         LD      A,(HL)          
6AB0: 00         NOP                     
6AB1: 00         NOP                     
6AB2: F7         RST     0X30            
6AB3: 00         NOP                     
6AB4: F7         RST     0X30            
6AB5: 62         LD      H,D             
6AB6: FF         RST     0X38            
6AB7: 62         LD      H,D             
6AB8: FF         RST     0X38            
6AB9: 72         LD      (HL),D          
6ABA: FF         RST     0X38            
6ABB: 72         LD      (HL),D          
6ABC: FF         RST     0X38            
6ABD: 7A         LD      A,D             
6ABE: FF         RST     0X38            
6ABF: 7A         LD      A,D             
6AC0: 00         NOP                     
6AC1: 00         NOP                     
6AC2: 7E         LD      A,(HL)          
6AC3: 00         NOP                     
6AC4: FF         RST     0X38            
6AC5: 3C         INC     A               
6AC6: FF         RST     0X38            
6AC7: 66         LD      H,(HL)          
6AC8: FF         RST     0X38            
6AC9: 66         LD      H,(HL)          
6ACA: FF         RST     0X38            
6ACB: 66         LD      H,(HL)          
6ACC: FF         RST     0X38            
6ACD: 60         LD      H,B             
6ACE: 7E         LD      A,(HL)          
6ACF: 3C         INC     A               
6AD0: 00         NOP                     
6AD1: 00         NOP                     
6AD2: FF         RST     0X38            
6AD3: 00         NOP                     
6AD4: FF         RST     0X38            
6AD5: 7E         LD      A,(HL)          
6AD6: FF         RST     0X38            
6AD7: 18 3C      JR      $6B15           
6AD9: 18 3C      JR      $6B17           
6ADB: 18 3C      JR      $6B19           
6ADD: 18 3C      JR      $6B1B           
6ADF: 18 00      JR      $6AE1           
6AE1: 00         NOP                     
6AE2: FF         RST     0X38            
6AE3: 00         NOP                     
6AE4: FF         RST     0X38            
6AE5: 6A         LD      L,D             
6AE6: FF         RST     0X38            
6AE7: 6A         LD      L,D             
6AE8: FF         RST     0X38            
6AE9: 6A         LD      L,D             
6AEA: FF         RST     0X38            
6AEB: 6A         LD      L,D             
6AEC: FF         RST     0X38            
6AED: 6A         LD      L,D             
6AEE: FF         RST     0X38            
6AEF: 6A         LD      L,D             
6AF0: FF         RST     0X38            
6AF1: 00         NOP                     
6AF2: FF         RST     0X38            
6AF3: 6A         LD      L,D             
6AF4: FF         RST     0X38            
6AF5: 6A         LD      L,D             
6AF6: FF         RST     0X38            
6AF7: 6A         LD      L,D             
6AF8: FF         RST     0X38            
6AF9: 6A         LD      L,D             
6AFA: FF         RST     0X38            
6AFB: 7E         LD      A,(HL)          
6AFC: FF         RST     0X38            
6AFD: 14         INC     D               
6AFE: 7E         LD      A,(HL)          
6AFF: 00         NOP                     
6B00: FF         RST     0X38            
6B01: 7E         LD      A,(HL)          
6B02: FF         RST     0X38            
6B03: 66         LD      H,(HL)          
6B04: FF         RST     0X38            
6B05: 66         LD      H,(HL)          
6B06: FF         RST     0X38            
6B07: 66         LD      H,(HL)          
6B08: FF         RST     0X38            
6B09: 66         LD      H,(HL)          
6B0A: FF         RST     0X38            
6B0B: 66         LD      H,(HL)          
6B0C: FF         RST     0X38            
6B0D: 00         NOP                     
6B0E: 00         NOP                     
6B0F: 00         NOP                     
6B10: FF         RST     0X38            
6B11: 66         LD      H,(HL)          
6B12: FF         RST     0X38            
6B13: 66         LD      H,(HL)          
6B14: FF         RST     0X38            
6B15: 66         LD      H,(HL)          
6B16: FF         RST     0X38            
6B17: 66         LD      H,(HL)          
6B18: FF         RST     0X38            
6B19: 66         LD      H,(HL)          
6B1A: FF         RST     0X38            
6B1B: 7C         LD      A,H             
6B1C: FE 00      CP      $00             
6B1E: 00         NOP                     
6B1F: 00         NOP                     
6B20: FF         RST     0X38            
6B21: 60         LD      H,B             
6B22: FF         RST     0X38            
6B23: 6E         LD      L,(HL)          
6B24: FF         RST     0X38            
6B25: 66         LD      H,(HL)          
6B26: FF         RST     0X38            
6B27: 66         LD      H,(HL)          
6B28: FF         RST     0X38            
6B29: 66         LD      H,(HL)          
6B2A: FF         RST     0X38            
6B2B: 3A         LD      A,(HLD)         
6B2C: 7E         LD      A,(HL)          
6B2D: 00         NOP                     
6B2E: 00         NOP                     
6B2F: 00         NOP                     
6B30: FF         RST     0X38            
6B31: 66         LD      H,(HL)          
6B32: FF         RST     0X38            
6B33: 66         LD      H,(HL)          
6B34: FF         RST     0X38            
6B35: 66         LD      H,(HL)          
6B36: FF         RST     0X38            
6B37: 66         LD      H,(HL)          
6B38: FF         RST     0X38            
6B39: 64         LD      H,H             
6B3A: FE 78      CP      $78             
6B3C: FC         ???                     
6B3D: 00         NOP                     
6B3E: 00         NOP                     
6B3F: 00         NOP                     
6B40: FE 60      CP      $60             
6B42: F0 60      LD      A,($60)         
6B44: F0 60      LD      A,($60)         
6B46: F0 60      LD      A,($60)         
6B48: FF         RST     0X38            
6B49: 60         LD      H,B             
6B4A: FF         RST     0X38            
6B4B: 7E         LD      A,(HL)          
6B4C: FF         RST     0X38            
6B4D: 00         NOP                     
6B4E: 00         NOP                     
6B4F: 00         NOP                     
6B50: FE 60      CP      $60             
6B52: F0 60      LD      A,($60)         
6B54: F0 60      LD      A,($60)         
6B56: F0 60      LD      A,($60)         
6B58: F0 60      LD      A,($60)         
6B5A: F0 60      LD      A,($60)         
6B5C: F0 00      LD      A,($00)         
6B5E: 00         NOP                     
6B5F: 00         NOP                     
6B60: FF         RST     0X38            
6B61: 66         LD      H,(HL)          
6B62: FF         RST     0X38            
6B63: 66         LD      H,(HL)          
6B64: FF         RST     0X38            
6B65: 66         LD      H,(HL)          
6B66: FF         RST     0X38            
6B67: 66         LD      H,(HL)          
6B68: FF         RST     0X38            
6B69: 66         LD      H,(HL)          
6B6A: FF         RST     0X38            
6B6B: 66         LD      H,(HL)          
6B6C: FF         RST     0X38            
6B6D: 00         NOP                     
6B6E: 00         NOP                     
6B6F: 00         NOP                     
6B70: 00         NOP                     
6B71: 00         NOP                     
6B72: FF         RST     0X38            
6B73: 00         NOP                     
6B74: FF         RST     0X38            
6B75: 7E         LD      A,(HL)          
6B76: FF         RST     0X38            
6B77: 0E 3F      LD      C,$3F           
6B79: 0E 3F      LD      C,$3F           
6B7B: 1C         INC     E               
6B7C: 3E 1C      LD      A,$1C           
6B7E: 7E         LD      A,(HL)          
6B7F: 1C         INC     E               
6B80: 1E 0C      LD      E,$0C           
6B82: FE 0C      CP      $0C             
6B84: FE 6C      CP      $6C             
6B86: FE 6C      CP      $6C             
6B88: FE 6C      CP      $6C             
6B8A: FE 38      CP      $38             
6B8C: 7C         LD      A,H             
6B8D: 00         NOP                     
6B8E: 00         NOP                     
6B8F: 00         NOP                     
6B90: FC         ???                     
6B91: 78         LD      A,B             
6B92: FC         ???                     
6B93: 78         LD      A,B             
6B94: FE 6C      CP      $6C             
6B96: FE 6C      CP      $6C             
6B98: FF         RST     0X38            
6B99: 66         LD      H,(HL)          
6B9A: FF         RST     0X38            
6B9B: 66         LD      H,(HL)          
6B9C: FF         RST     0X38            
6B9D: 00         NOP                     
6B9E: 00         NOP                     
6B9F: 00         NOP                     
6BA0: FF         RST     0X38            
6BA1: 7E         LD      A,(HL)          
6BA2: FF         RST     0X38            
6BA3: 6A         LD      L,D             
6BA4: FF         RST     0X38            
6BA5: 6A         LD      L,D             
6BA6: FF         RST     0X38            
6BA7: 6A         LD      L,D             
6BA8: FF         RST     0X38            
6BA9: 62         LD      H,D             
6BAA: F7         RST     0X30            
6BAB: 62         LD      H,D             
6BAC: F7         RST     0X30            
6BAD: 00         NOP                     
6BAE: 00         NOP                     
6BAF: 00         NOP                     
6BB0: FF         RST     0X38            
6BB1: 6E         LD      L,(HL)          
6BB2: FF         RST     0X38            
6BB3: 6E         LD      L,(HL)          
6BB4: FF         RST     0X38            
6BB5: 66         LD      H,(HL)          
6BB6: FF         RST     0X38            
6BB7: 66         LD      H,(HL)          
6BB8: FF         RST     0X38            
6BB9: 62         LD      H,D             
6BBA: F7         RST     0X30            
6BBB: 62         LD      H,D             
6BBC: F7         RST     0X30            
6BBD: 00         NOP                     
6BBE: 00         NOP                     
6BBF: 00         NOP                     
6BC0: FF         RST     0X38            
6BC1: 06 FF      LD      B,$FF           
6BC3: 66         LD      H,(HL)          
6BC4: FF         RST     0X38            
6BC5: 66         LD      H,(HL)          
6BC6: FF         RST     0X38            
6BC7: 66         LD      H,(HL)          
6BC8: FF         RST     0X38            
6BC9: 66         LD      H,(HL)          
6BCA: FF         RST     0X38            
6BCB: 3C         INC     A               
6BCC: 7E         LD      A,(HL)          
6BCD: 00         NOP                     
6BCE: 00         NOP                     
6BCF: 00         NOP                     
6BD0: 3C         INC     A               
6BD1: 18 3C      JR      $6C0F           
6BD3: 18 3C      JR      $6C11           
6BD5: 18 3C      JR      $6C13           
6BD7: 18 3C      JR      $6C15           
6BD9: 18 3C      JR      $6C17           
6BDB: 18 3C      JR      $6C19           
6BDD: 00         NOP                     
6BDE: 00         NOP                     
6BDF: 00         NOP                     
6BE0: FF         RST     0X38            
6BE1: 6A         LD      L,D             
6BE2: FF         RST     0X38            
6BE3: 6A         LD      L,D             
6BE4: FF         RST     0X38            
6BE5: 7E         LD      A,(HL)          
6BE6: FF         RST     0X38            
6BE7: 7E         LD      A,(HL)          
6BE8: FF         RST     0X38            
6BE9: 3E 7F      LD      A,$7F           
6BEB: 14         INC     D               
6BEC: 3E 00      LD      A,$00           
6BEE: 00         NOP                     
6BEF: 00         NOP                     
6BF0: F7         RST     0X30            
6BF1: 00         NOP                     
6BF2: FF         RST     0X38            
6BF3: 62         LD      H,D             
6BF4: FF         RST     0X38            
6BF5: 74         LD      (HL),H          
6BF6: FE 38      CP      $38             
6BF8: 7F         LD      A,A             
6BF9: 1C         INC     E               
6BFA: FF         RST     0X38            
6BFB: 2E FF      LD      L,$FF           
6BFD: 46         LD      B,(HL)          
6BFE: EF         RST     0X28            
6BFF: 00         NOP                     
6C00: 18 00      JR      $6C02           
6C02: 3C         INC     A               
6C03: 18 7E      JR      $6C83           
6C05: 24         INC     H               
6C06: FF         RST     0X38            
6C07: 66         LD      H,(HL)          
6C08: FF         RST     0X38            
6C09: 7E         LD      A,(HL)          
6C0A: FF         RST     0X38            
6C0B: 66         LD      H,(HL)          
6C0C: FF         RST     0X38            
6C0D: 66         LD      H,(HL)          
6C0E: FF         RST     0X38            
6C0F: 00         NOP                     
6C10: 3C         INC     A               
6C11: 00         NOP                     
6C12: 7E         LD      A,(HL)          
6C13: 3C         INC     A               
6C14: FF         RST     0X38            
6C15: 66         LD      H,(HL)          
6C16: FF         RST     0X38            
6C17: 60         LD      H,B             
6C18: FF         RST     0X38            
6C19: 60         LD      H,B             
6C1A: FF         RST     0X38            
6C1B: 66         LD      H,(HL)          
6C1C: 7E         LD      A,(HL)          
6C1D: 3C         INC     A               
6C1E: 3C         INC     A               
6C1F: 00         NOP                     
6C20: F8 00      LDHL    SP,$00          
6C22: FC         ???                     
6C23: 78         LD      A,B             
6C24: FE 64      CP      $64             
6C26: FF         RST     0X38            
6C27: 66         LD      H,(HL)          
6C28: FF         RST     0X38            
6C29: 66         LD      H,(HL)          
6C2A: FE 64      CP      $64             
6C2C: FC         ???                     
6C2D: 78         LD      A,B             
6C2E: F8 00      LDHL    SP,$00          
6C30: FF         RST     0X38            
6C31: 00         NOP                     
6C32: FF         RST     0X38            
6C33: 7E         LD      A,(HL)          
6C34: FF         RST     0X38            
6C35: 60         LD      H,B             
6C36: FE 7C      CP      $7C             
6C38: FE 60      CP      $60             
6C3A: FF         RST     0X38            
6C3B: 60         LD      H,B             
6C3C: FF         RST     0X38            
6C3D: 7E         LD      A,(HL)          
6C3E: FF         RST     0X38            
6C3F: 00         NOP                     
6C40: 7E         LD      A,(HL)          
6C41: 00         NOP                     
6C42: FF         RST     0X38            
6C43: 3C         INC     A               
6C44: FF         RST     0X38            
6C45: 66         LD      H,(HL)          
6C46: FF         RST     0X38            
6C47: 60         LD      H,B             
6C48: FF         RST     0X38            
6C49: 6E         LD      L,(HL)          
6C4A: FF         RST     0X38            
6C4B: 66         LD      H,(HL)          
6C4C: FF         RST     0X38            
6C4D: 3E 7E      LD      A,$7E           
6C4F: 00         NOP                     
6C50: FF         RST     0X38            
6C51: 00         NOP                     
6C52: FF         RST     0X38            
6C53: 66         LD      H,(HL)          
6C54: FF         RST     0X38            
6C55: 66         LD      H,(HL)          
6C56: FF         RST     0X38            
6C57: 7E         LD      A,(HL)          
6C58: FF         RST     0X38            
6C59: 66         LD      H,(HL)          
6C5A: FF         RST     0X38            
6C5B: 66         LD      H,(HL)          
6C5C: FF         RST     0X38            
6C5D: 66         LD      H,(HL)          
6C5E: FF         RST     0X38            
6C5F: 00         NOP                     
6C60: 7E         LD      A,(HL)          
6C61: 00         NOP                     
6C62: 7E         LD      A,(HL)          
6C63: 3C         INC     A               
6C64: 3C         INC     A               
6C65: 18 3C      JR      $6CA3           
6C67: 18 3C      JR      $6CA5           
6C69: 18 3C      JR      $6CA7           
6C6B: 18 7E      JR      $6CEB           
6C6D: 3C         INC     A               
6C6E: 7E         LD      A,(HL)          
6C6F: 00         NOP                     
6C70: FF         RST     0X38            
6C71: 00         NOP                     
6C72: FF         RST     0X38            
6C73: 66         LD      H,(HL)          
6C74: FF         RST     0X38            
6C75: 6C         LD      L,H             
6C76: FE 78      CP      $78             
6C78: FE 78      CP      $78             
6C7A: FF         RST     0X38            
6C7B: 6C         LD      L,H             
6C7C: FF         RST     0X38            
6C7D: 66         LD      H,(HL)          
6C7E: FF         RST     0X38            
6C7F: 00         NOP                     
6C80: F0 00      LD      A,($00)         
6C82: F0 60      LD      A,($60)         
6C84: F0 60      LD      A,($60)         
6C86: F0 60      LD      A,($60)         
6C88: F0 60      LD      A,($60)         
6C8A: FF         RST     0X38            
6C8B: 60         LD      H,B             
6C8C: FF         RST     0X38            
6C8D: 7E         LD      A,(HL)          
6C8E: FF         RST     0X38            
6C8F: 00         NOP                     
6C90: E3         ???                     
6C91: 00         NOP                     
6C92: F7         RST     0X30            
6C93: 62         LD      H,D             
6C94: FF         RST     0X38            
6C95: 76         HALT                    
6C96: FF         RST     0X38            
6C97: 7E         LD      A,(HL)          
6C98: FF         RST     0X38            
6C99: 6A         LD      L,D             
6C9A: FF         RST     0X38            
6C9B: 62         LD      H,D             
6C9C: F7         RST     0X30            
6C9D: 62         LD      H,D             
6C9E: F7         RST     0X30            
6C9F: 00         NOP                     
6CA0: E7         RST     0X20            
6CA1: 00         NOP                     
6CA2: F7         RST     0X30            
6CA3: 62         LD      H,D             
6CA4: FF         RST     0X38            
6CA5: 72         LD      (HL),D          
6CA6: FF         RST     0X38            
6CA7: 7A         LD      A,D             
6CA8: FF         RST     0X38            
6CA9: 6E         LD      L,(HL)          
6CAA: FF         RST     0X38            
6CAB: 66         LD      H,(HL)          
6CAC: F7         RST     0X30            
6CAD: 62         LD      H,D             
6CAE: F3         DI                      
6CAF: 00         NOP                     
6CB0: 3C         INC     A               
6CB1: 00         NOP                     
6CB2: 7E         LD      A,(HL)          
6CB3: 3C         INC     A               
6CB4: FF         RST     0X38            
6CB5: 66         LD      H,(HL)          
6CB6: FF         RST     0X38            
6CB7: 66         LD      H,(HL)          
6CB8: FF         RST     0X38            
6CB9: 66         LD      H,(HL)          
6CBA: FF         RST     0X38            
6CBB: 66         LD      H,(HL)          
6CBC: 7E         LD      A,(HL)          
6CBD: 3C         INC     A               
6CBE: 3C         INC     A               
6CBF: 00         NOP                     
6CC0: 00         NOP                     
6CC1: 00         NOP                     
6CC2: 00         NOP                     
6CC3: 00         NOP                     
6CC4: 00         NOP                     
6CC5: 00         NOP                     
6CC6: 00         NOP                     
6CC7: 00         NOP                     
6CC8: 00         NOP                     
6CC9: 00         NOP                     
6CCA: 01 00 02   LD      BC,$0200        
6CCD: 01 05 02   LD      BC,$0205        
6CD0: 07         RLCA                    
6CD1: 01 06 02   LD      BC,$0206        
6CD4: 04         INC     B               
6CD5: 00         NOP                     
6CD6: 04         INC     B               
6CD7: 00         NOP                     
6CD8: 1E 00      LD      E,$00           
6CDA: 12         LD      (DE),A          
6CDB: 00         NOP                     
6CDC: 29         ADD     HL,HL           
6CDD: 10 28      STOP    $28             
6CDF: 10 00      STOP    $00             
6CE1: 00         NOP                     
6CE2: 00         NOP                     
6CE3: 00         NOP                     
6CE4: 00         NOP                     
6CE5: 00         NOP                     
6CE6: 00         NOP                     
6CE7: 00         NOP                     
6CE8: 00         NOP                     
6CE9: 00         NOP                     
6CEA: C0         RET     NZ              
6CEB: 00         NOP                     
6CEC: 20 C0      JR      NZ,$6CAE        
6CEE: 90         SUB     B               
6CEF: 60         LD      H,B             
6CF0: 60         LD      H,B             
6CF1: 80         ADD     A,B             
6CF2: 20 40      JR      NZ,$6D34        
6CF4: 20 00      JR      NZ,$6CF6        
6CF6: 20 00      JR      NZ,$6CF8        
6CF8: 78         LD      A,B             
6CF9: 00         NOP                     
6CFA: 48         LD      C,B             
6CFB: 00         NOP                     
6CFC: 74         LD      (HL),H          
6CFD: 08 F4 08   LD      ($08F4),SP      
6D00: FC         ???                     
6D01: 00         NOP                     
6D02: FE 7C      CP      $7C             
6D04: FF         RST     0X38            
6D05: 66         LD      H,(HL)          
6D06: FF         RST     0X38            
6D07: 66         LD      H,(HL)          
6D08: FE 7C      CP      $7C             
6D0A: FC         ???                     
6D0B: 60         LD      H,B             
6D0C: F0 60      LD      A,($60)         
6D0E: F0 00      LD      A,($00)         
6D10: FC         ???                     
6D11: 00         NOP                     
6D12: FE 7C      CP      $7C             
6D14: FF         RST     0X38            
6D15: 66         LD      H,(HL)          
6D16: FF         RST     0X38            
6D17: 66         LD      H,(HL)          
6D18: FE 7C      CP      $7C             
6D1A: FE 6C      CP      $6C             
6D1C: FF         RST     0X38            
6D1D: 66         LD      H,(HL)          
6D1E: F7         RST     0X30            
6D1F: 00         NOP                     
6D20: 3E 00      LD      A,$00           
6D22: 7E         LD      A,(HL)          
6D23: 3C         INC     A               
6D24: FC         ???                     
6D25: 60         LD      H,B             
6D26: 7E         LD      A,(HL)          
6D27: 3C         INC     A               
6D28: FF         RST     0X38            
6D29: 06 FF      LD      B,$FF           
6D2B: 66         LD      H,(HL)          
6D2C: 7E         LD      A,(HL)          
6D2D: 3C         INC     A               
6D2E: 3C         INC     A               
6D2F: 00         NOP                     
6D30: FF         RST     0X38            
6D31: 00         NOP                     
6D32: FF         RST     0X38            
6D33: 7E         LD      A,(HL)          
6D34: FF         RST     0X38            
6D35: 18 3C      JR      $6D73           
6D37: 18 3C      JR      $6D75           
6D39: 18 3C      JR      $6D77           
6D3B: 18 3C      JR      $6D79           
6D3D: 18 3C      JR      $6D7B           
6D3F: 00         NOP                     
6D40: E7         RST     0X20            
6D41: 00         NOP                     
6D42: FF         RST     0X38            
6D43: 66         LD      H,(HL)          
6D44: FF         RST     0X38            
6D45: 66         LD      H,(HL)          
6D46: FF         RST     0X38            
6D47: 66         LD      H,(HL)          
6D48: FF         RST     0X38            
6D49: 66         LD      H,(HL)          
6D4A: FF         RST     0X38            
6D4B: 66         LD      H,(HL)          
6D4C: 7E         LD      A,(HL)          
6D4D: 3C         INC     A               
6D4E: 3C         INC     A               
6D4F: 00         NOP                     
6D50: FF         RST     0X38            
6D51: 00         NOP                     
6D52: FF         RST     0X38            
6D53: 66         LD      H,(HL)          
6D54: FF         RST     0X38            
6D55: 66         LD      H,(HL)          
6D56: FF         RST     0X38            
6D57: 66         LD      H,(HL)          
6D58: FF         RST     0X38            
6D59: 24         INC     H               
6D5A: 7E         LD      A,(HL)          
6D5B: 3C         INC     A               
6D5C: 7E         LD      A,(HL)          
6D5D: 18 3C      JR      $6D9B           
6D5F: 00         NOP                     
6D60: FF         RST     0X38            
6D61: 00         NOP                     
6D62: FF         RST     0X38            
6D63: 42         LD      B,D             
6D64: FF         RST     0X38            
6D65: 24         INC     H               
6D66: FF         RST     0X38            
6D67: 18 FF      JR      $6D68           
6D69: 18 FF      JR      $6D6A           
6D6B: 24         INC     H               
6D6C: FF         RST     0X38            
6D6D: 42         LD      B,D             
6D6E: FF         RST     0X38            
6D6F: 00         NOP                     
6D70: FF         RST     0X38            
6D71: 00         NOP                     
6D72: FF         RST     0X38            
6D73: 42         LD      B,D             
6D74: FF         RST     0X38            
6D75: 24         INC     H               
6D76: FF         RST     0X38            
6D77: 18 FF      JR      $6D78           
6D79: 18 FF      JR      $6D7A           
6D7B: 24         INC     H               
6D7C: FF         RST     0X38            
6D7D: 42         LD      B,D             
6D7E: FF         RST     0X38            
6D7F: 00         NOP                     
6D80: FF         RST     0X38            
6D81: 00         NOP                     
6D82: FF         RST     0X38            
6D83: 42         LD      B,D             
6D84: FF         RST     0X38            
6D85: 24         INC     H               
6D86: FF         RST     0X38            
6D87: 18 FF      JR      $6D88           
6D89: 18 FF      JR      $6D8A           
6D8B: 24         INC     H               
6D8C: FF         RST     0X38            
6D8D: 42         LD      B,D             
6D8E: FF         RST     0X38            
6D8F: 00         NOP                     
6D90: FF         RST     0X38            
6D91: 00         NOP                     
6D92: FF         RST     0X38            
6D93: 42         LD      B,D             
6D94: FF         RST     0X38            
6D95: 24         INC     H               
6D96: FF         RST     0X38            
6D97: 18 FF      JR      $6D98           
6D99: 18 FF      JR      $6D9A           
6D9B: 24         INC     H               
6D9C: FF         RST     0X38            
6D9D: 42         LD      B,D             
6D9E: FF         RST     0X38            
6D9F: 00         NOP                     
6DA0: FF         RST     0X38            
6DA1: 00         NOP                     
6DA2: FF         RST     0X38            
6DA3: 42         LD      B,D             
6DA4: FF         RST     0X38            
6DA5: 24         INC     H               
6DA6: FF         RST     0X38            
6DA7: 18 FF      JR      $6DA8           
6DA9: 18 FF      JR      $6DAA           
6DAB: 24         INC     H               
6DAC: FF         RST     0X38            
6DAD: 42         LD      B,D             
6DAE: FF         RST     0X38            
6DAF: 00         NOP                     
6DB0: FF         RST     0X38            
6DB1: 00         NOP                     
6DB2: FF         RST     0X38            
6DB3: 42         LD      B,D             
6DB4: FF         RST     0X38            
6DB5: 24         INC     H               
6DB6: FF         RST     0X38            
6DB7: 18 FF      JR      $6DB8           
6DB9: 18 FF      JR      $6DBA           
6DBB: 24         INC     H               
6DBC: FF         RST     0X38            
6DBD: 42         LD      B,D             
6DBE: FF         RST     0X38            
6DBF: 00         NOP                     
6DC0: 00         NOP                     
6DC1: 00         NOP                     
6DC2: 00         NOP                     
6DC3: 00         NOP                     
6DC4: 00         NOP                     
6DC5: 00         NOP                     
6DC6: 03         INC     BC              
6DC7: 00         NOP                     
6DC8: 0F         RRCA                    
6DC9: 03         INC     BC              
6DCA: 1F         RRA                     
6DCB: 0F         RRCA                    
6DCC: 7F         LD      A,A             
6DCD: 1F         RRA                     
6DCE: EE 77      XOR     $77             
6DD0: 7D         LD      A,L             
6DD1: 06 1D      LD      B,$1D           
6DD3: 0E 1A      LD      C,$1A           
6DD5: 0C         INC     C               
6DD6: 3A         LD      A,(HLD)         
6DD7: 1C         INC     E               
6DD8: 34         INC     (HL)            
6DD9: 18 68      JR      $6E43           
6DDB: 30 50      JR      NC,$6E2D        
6DDD: 20 60      JR      NZ,$6E3F        
6DDF: 00         NOP                     
6DE0: 00         NOP                     
6DE1: 00         NOP                     
6DE2: 00         NOP                     
6DE3: 00         NOP                     
6DE4: 0F         RRCA                    
6DE5: 00         NOP                     
6DE6: 3F         CCF                     
6DE7: 0F         RRCA                    
6DE8: 7F         LD      A,A             
6DE9: 3F         CCF                     
6DEA: FF         RST     0X38            
6DEB: 77         LD      (HL),A          
6DEC: FF         RST     0X38            
6DED: 47         LD      B,A             
6DEE: 5D         LD      E,L             
6DEF: 0E 1E      LD      C,$1E           
6DF1: 0C         INC     C               
6DF2: 3A         LD      A,(HLD)         
6DF3: 1C         INC     E               
6DF4: 3A         LD      A,(HLD)         
6DF5: 1C         INC     E               
6DF6: 34         INC     (HL)            
6DF7: 18 14      JR      $6E0D           
6DF9: 08 18 00   LD      ($0018),SP      
6DFC: 00         NOP                     
6DFD: 00         NOP                     
6DFE: 00         NOP                     
6DFF: 00         NOP                     
6E00: 00         NOP                     
6E01: 00         NOP                     
6E02: 00         NOP                     
6E03: 00         NOP                     
6E04: 00         NOP                     
6E05: 00         NOP                     
6E06: 00         NOP                     
6E07: 00         NOP                     
6E08: 00         NOP                     
6E09: 00         NOP                     
6E0A: 02         LD      (BC),A          
6E0B: 00         NOP                     
6E0C: FF         RST     0X38            
6E0D: 02         LD      (BC),A          
6E0E: 85         ADD     A,L             
6E0F: 7A         LD      A,D             
6E10: FF         RST     0X38            
6E11: 02         LD      (BC),A          
6E12: 85         ADD     A,L             
6E13: 7A         LD      A,D             
6E14: 85         ADD     A,L             
6E15: 00         NOP                     
6E16: FF         RST     0X38            
6E17: 00         NOP                     
6E18: 7C         LD      A,H             
6E19: 00         NOP                     
6E1A: 1F         RRA                     
6E1B: 00         NOP                     
6E1C: 00         NOP                     
6E1D: 00         NOP                     
6E1E: 10 00      STOP    $00             
6E20: 29         ADD     HL,HL           
6E21: 00         NOP                     
6E22: 4F         LD      C,A             
6E23: 20 57      JR      NZ,$6E7C        
6E25: 23         INC     HL              
6E26: 53         LD      D,E             
6E27: 20 54      JR      NZ,$6E7D        
6E29: 20 7C      JR      NZ,$6EA7        
6E2B: 20 FC      JR      NZ,$6E29        
6E2D: 00         NOP                     
6E2E: 0F         RRCA                    
6E2F: F0 FF      LD      A,($FF)         
6E31: 00         NOP                     
6E32: 00         NOP                     
6E33: FF         RST     0X38            
6E34: 00         NOP                     
6E35: 00         NOP                     
6E36: FF         RST     0X38            
6E37: 00         NOP                     
6E38: FF         RST     0X38            
6E39: 00         NOP                     
6E3A: F1         POP     AF              
6E3B: 00         NOP                     
6E3C: 5C         LD      E,H             
6E3D: 00         NOP                     
6E3E: 00         NOP                     
6E3F: 00         NOP                     
6E40: F4         ???                     
6E41: 00         NOP                     
6E42: F2         ???                     
6E43: 04         INC     B               
6E44: EA C4 EA   LD      ($EAC4),A       
6E47: 04         INC     B               
6E48: 3A         LD      A,(HLD)         
6E49: 04         INC     B               
6E4A: 7E         LD      A,(HL)          
6E4B: 04         INC     B               
6E4C: FF         RST     0X38            
6E4D: 00         NOP                     
6E4E: F8 07      LDHL    SP,$07          
6E50: FF         RST     0X38            
6E51: 08 14 EB   LD      ($EB14),SP      
6E54: 14         INC     D               
6E55: 00         NOP                     
6E56: FF         RST     0X38            
6E57: 00         NOP                     
6E58: FF         RST     0X38            
6E59: 00         NOP                     
6E5A: F7         RST     0X30            
6E5B: 00         NOP                     
6E5C: 00         NOP                     
6E5D: 00         NOP                     
6E5E: 88         ADC     A,B             
6E5F: 00         NOP                     
6E60: 00         NOP                     
6E61: 00         NOP                     
6E62: 00         NOP                     
6E63: 00         NOP                     
6E64: 00         NOP                     
6E65: 00         NOP                     
6E66: 00         NOP                     
6E67: 00         NOP                     
6E68: 00         NOP                     
6E69: 00         NOP                     
6E6A: 1C         INC     E               
6E6B: 00         NOP                     
6E6C: FF         RST     0X38            
6E6D: 10 29      STOP    $29             
6E6F: D6 FF      SUB     $FF             
6E71: 20 51      JR      NZ,$6EC4        
6E73: AE         XOR     (HL)            
6E74: 51         LD      D,C             
6E75: 00         NOP                     
6E76: FF         RST     0X38            
6E77: 00         NOP                     
6E78: 1F         RRA                     
6E79: 00         NOP                     
6E7A: F0 00      LD      A,($00)         
6E7C: E0 00      LDFF00  ($00),A         
6E7E: 08 00 00   LD      ($0000),SP      
6E81: 00         NOP                     
6E82: 00         NOP                     
6E83: 00         NOP                     
6E84: 00         NOP                     
6E85: 00         NOP                     
6E86: 00         NOP                     
6E87: 00         NOP                     
6E88: 00         NOP                     
6E89: 00         NOP                     
6E8A: 02         LD      (BC),A          
6E8B: 00         NOP                     
6E8C: FF         RST     0X38            
6E8D: 02         LD      (BC),A          
6E8E: 85         ADD     A,L             
6E8F: 7A         LD      A,D             
6E90: FF         RST     0X38            
6E91: 02         LD      (BC),A          
6E92: 85         ADD     A,L             
6E93: 7A         LD      A,D             
6E94: 85         ADD     A,L             
6E95: 00         NOP                     
6E96: FF         RST     0X38            
6E97: 00         NOP                     
6E98: FF         RST     0X38            
6E99: 00         NOP                     
6E9A: 38 00      JR      C,$6E9C         
6E9C: 07         RLCA                    
6E9D: 00         NOP                     
6E9E: 00         NOP                     
6E9F: 00         NOP                     
6EA0: 29         ADD     HL,HL           
6EA1: 00         NOP                     
6EA2: 4F         LD      C,A             
6EA3: 20 57      JR      NZ,$6EFC        
6EA5: 23         INC     HL              
6EA6: 53         LD      D,E             
6EA7: 20 54      JR      NZ,$6EFD        
6EA9: 20 7C      JR      NZ,$6F27        
6EAB: 20 FC      JR      NZ,$6EA9        
6EAD: 00         NOP                     
6EAE: 0F         RRCA                    
6EAF: F0 FF      LD      A,($FF)         
6EB1: 00         NOP                     
6EB2: 00         NOP                     
6EB3: FF         RST     0X38            
6EB4: 00         NOP                     
6EB5: 00         NOP                     
6EB6: FF         RST     0X38            
6EB7: 00         NOP                     
6EB8: 07         RLCA                    
6EB9: 00         NOP                     
6EBA: BF         CP      A               
6EBB: 00         NOP                     
6EBC: C0         RET     NZ              
6EBD: 00         NOP                     
6EBE: 48         LD      C,B             
6EBF: 00         NOP                     
6EC0: F4         ???                     
6EC1: 00         NOP                     
6EC2: F2         ???                     
6EC3: 04         INC     B               
6EC4: EA C4 EA   LD      ($EAC4),A       
6EC7: 04         INC     B               
6EC8: 3A         LD      A,(HLD)         
6EC9: 04         INC     B               
6ECA: 7E         LD      A,(HL)          
6ECB: 04         INC     B               
6ECC: FF         RST     0X38            
6ECD: 00         NOP                     
6ECE: F8 07      LDHL    SP,$07          
6ED0: FF         RST     0X38            
6ED1: 08 14 EB   LD      ($EB14),SP      
6ED4: 14         INC     D               
6ED5: 00         NOP                     
6ED6: FF         RST     0X38            
6ED7: 00         NOP                     
6ED8: F3         DI                      
6ED9: 00         NOP                     
6EDA: 3C         INC     A               
6EDB: 00         NOP                     
6EDC: E1         POP     HL              
6EDD: 00         NOP                     
6EDE: 00         NOP                     
6EDF: 00         NOP                     
6EE0: 00         NOP                     
6EE1: 00         NOP                     
6EE2: 00         NOP                     
6EE3: 00         NOP                     
6EE4: 00         NOP                     
6EE5: 00         NOP                     
6EE6: 00         NOP                     
6EE7: 00         NOP                     
6EE8: 00         NOP                     
6EE9: 00         NOP                     
6EEA: 1C         INC     E               
6EEB: 00         NOP                     
6EEC: FF         RST     0X38            
6EED: 10 29      STOP    $29             
6EEF: D6 FF      SUB     $FF             
6EF1: 20 51      JR      NZ,$6F44        
6EF3: AE         XOR     (HL)            
6EF4: 51         LD      D,C             
6EF5: 00         NOP                     
6EF6: FF         RST     0X38            
6EF7: 00         NOP                     
6EF8: FF         RST     0X38            
6EF9: 00         NOP                     
6EFA: 0E 00      LD      C,$00           
6EFC: C0         RET     NZ              
6EFD: 00         NOP                     
6EFE: 40         LD      B,B             
6EFF: 00         NOP                     
6F00: 00         NOP                     
6F01: 00         NOP                     
6F02: 00         NOP                     
6F03: 00         NOP                     
6F04: 00         NOP                     
6F05: 00         NOP                     
6F06: 00         NOP                     
6F07: 00         NOP                     
6F08: 00         NOP                     
6F09: 00         NOP                     
6F0A: 02         LD      (BC),A          
6F0B: 00         NOP                     
6F0C: FF         RST     0X38            
6F0D: 02         LD      (BC),A          
6F0E: 85         ADD     A,L             
6F0F: 7A         LD      A,D             
6F10: FF         RST     0X38            
6F11: 02         LD      (BC),A          
6F12: 85         ADD     A,L             
6F13: 7A         LD      A,D             
6F14: 85         ADD     A,L             
6F15: 00         NOP                     
6F16: FF         RST     0X38            
6F17: 00         NOP                     
6F18: 07         RLCA                    
6F19: 00         NOP                     
6F1A: 7E         LD      A,(HL)          
6F1B: 00         NOP                     
6F1C: 10 00      STOP    $00             
6F1E: 01 00 29   LD      BC,$2900        
6F21: 00         NOP                     
6F22: 4F         LD      C,A             
6F23: 20 57      JR      NZ,$6F7C        
6F25: 23         INC     HL              
6F26: 53         LD      D,E             
6F27: 20 54      JR      NZ,$6F7D        
6F29: 20 7C      JR      NZ,$6FA7        
6F2B: 20 FC      JR      NZ,$6F29        
6F2D: 00         NOP                     
6F2E: 0F         RRCA                    
6F2F: F0 FF      LD      A,($FF)         
6F31: 00         NOP                     
6F32: 00         NOP                     
6F33: FF         RST     0X38            
6F34: 00         NOP                     
6F35: 00         NOP                     
6F36: FF         RST     0X38            
6F37: 00         NOP                     
6F38: FF         RST     0X38            
6F39: 00         NOP                     
6F3A: 03         INC     BC              
6F3B: 00         NOP                     
6F3C: 1A         LD      A,(DE)          
6F3D: 00         NOP                     
6F3E: 00         NOP                     
6F3F: 00         NOP                     
6F40: F4         ???                     
6F41: 00         NOP                     
6F42: F2         ???                     
6F43: 04         INC     B               
6F44: EA C4 EA   LD      ($EAC4),A       
6F47: 04         INC     B               
6F48: 3A         LD      A,(HLD)         
6F49: 04         INC     B               
6F4A: 7E         LD      A,(HL)          
6F4B: 04         INC     B               
6F4C: FF         RST     0X38            
6F4D: 00         NOP                     
6F4E: F8 07      LDHL    SP,$07          
6F50: FF         RST     0X38            
6F51: 08 14 EB   LD      ($EB14),SP      
6F54: 14         INC     D               
6F55: 00         NOP                     
6F56: FF         RST     0X38            
6F57: 00         NOP                     
6F58: 83         ADD     A,E             
6F59: 00         NOP                     
6F5A: E0 00      LDFF00  ($00),A         
6F5C: 18 00      JR      $6F5E           
6F5E: 40         LD      B,B             
6F5F: 00         NOP                     
6F60: 00         NOP                     
6F61: 00         NOP                     
6F62: 00         NOP                     
6F63: 00         NOP                     
6F64: 00         NOP                     
6F65: 00         NOP                     
6F66: 00         NOP                     
6F67: 00         NOP                     
6F68: 00         NOP                     
6F69: 00         NOP                     
6F6A: 1C         INC     E               
6F6B: 00         NOP                     
6F6C: FF         RST     0X38            
6F6D: 10 29      STOP    $29             
6F6F: D6 FF      SUB     $FF             
6F71: 20 51      JR      NZ,$6FC4        
6F73: AE         XOR     (HL)            
6F74: 51         LD      D,C             
6F75: 00         NOP                     
6F76: FF         RST     0X38            
6F77: 00         NOP                     
6F78: F8 00      LDHL    SP,$00          
6F7A: 7E         LD      A,(HL)          
6F7B: 00         NOP                     
6F7C: 04         INC     B               
6F7D: 00         NOP                     
6F7E: 80         ADD     A,B             
6F7F: 00         NOP                     
6F80: 00         NOP                     
6F81: 00         NOP                     
6F82: 00         NOP                     
6F83: 00         NOP                     
6F84: 00         NOP                     
6F85: 00         NOP                     
6F86: 00         NOP                     
6F87: 00         NOP                     
6F88: 00         NOP                     
6F89: 00         NOP                     
6F8A: 02         LD      (BC),A          
6F8B: 00         NOP                     
6F8C: FF         RST     0X38            
6F8D: 02         LD      (BC),A          
6F8E: 85         ADD     A,L             
6F8F: 7A         LD      A,D             
6F90: FF         RST     0X38            
6F91: 02         LD      (BC),A          
6F92: 85         ADD     A,L             
6F93: 7A         LD      A,D             
6F94: 85         ADD     A,L             
6F95: 00         NOP                     
6F96: FF         RST     0X38            
6F97: 00         NOP                     
6F98: 3F         CCF                     
6F99: 00         NOP                     
6F9A: 01 00 18   LD      BC,$1800        
6F9D: 00         NOP                     
6F9E: 00         NOP                     
6F9F: 00         NOP                     
6FA0: 29         ADD     HL,HL           
6FA1: 00         NOP                     
6FA2: 4F         LD      C,A             
6FA3: 20 57      JR      NZ,$6FFC        
6FA5: 23         INC     HL              
6FA6: 53         LD      D,E             
6FA7: 20 54      JR      NZ,$6FFD        
6FA9: 20 7C      JR      NZ,$7027        
6FAB: 20 FC      JR      NZ,$6FA9        
6FAD: 00         NOP                     
6FAE: 0F         RRCA                    
6FAF: F0 FF      LD      A,($FF)         
6FB1: 00         NOP                     
6FB2: 00         NOP                     
6FB3: FF         RST     0X38            
6FB4: 00         NOP                     
6FB5: 00         NOP                     
6FB6: FF         RST     0X38            
6FB7: 00         NOP                     
6FB8: FB         EI                      
6FB9: 00         NOP                     
6FBA: 3E 00      LD      A,$00           
6FBC: 01 00 12   LD      BC,$1200        
6FBF: 00         NOP                     
6FC0: F4         ???                     
6FC1: 00         NOP                     
6FC2: F2         ???                     
6FC3: 04         INC     B               
6FC4: EA C4 EA   LD      ($EAC4),A       
6FC7: 04         INC     B               
6FC8: 3A         LD      A,(HLD)         
6FC9: 04         INC     B               
6FCA: 7E         LD      A,(HL)          
6FCB: 04         INC     B               
6FCC: FF         RST     0X38            
6FCD: 00         NOP                     
6FCE: F8 07      LDHL    SP,$07          
6FD0: FF         RST     0X38            
6FD1: 08 14 EB   LD      ($EB14),SP      
6FD4: 14         INC     D               
6FD5: 00         NOP                     
6FD6: FF         RST     0X38            
6FD7: 00         NOP                     
6FD8: FF         RST     0X38            
6FD9: 00         NOP                     
6FDA: 01 00 C0   LD      BC,$C000        
6FDD: 00         NOP                     
6FDE: 10 00      STOP    $00             
6FE0: 00         NOP                     
6FE1: 00         NOP                     
6FE2: 00         NOP                     
6FE3: 00         NOP                     
6FE4: 00         NOP                     
6FE5: 00         NOP                     
6FE6: 00         NOP                     
6FE7: 00         NOP                     
6FE8: 00         NOP                     
6FE9: 00         NOP                     
6FEA: 1C         INC     E               
6FEB: 00         NOP                     
6FEC: FF         RST     0X38            
6FED: 10 29      STOP    $29             
6FEF: D6 FF      SUB     $FF             
6FF1: 20 51      JR      NZ,$7044        
6FF3: AE         XOR     (HL)            
6FF4: 51         LD      D,C             
6FF5: 00         NOP                     
6FF6: FF         RST     0X38            
6FF7: 00         NOP                     
6FF8: FC         ???                     
6FF9: 00         NOP                     
6FFA: F0 00      LD      A,($00)         
6FFC: 1C         INC     E               
6FFD: 00         NOP                     
6FFE: 00         NOP                     
6FFF: 00         NOP                     
7000: FF         RST     0X38            
7001: FF         RST     0X38            
7002: F7         RST     0X30            
7003: FF         RST     0X38            
7004: C0         RET     NZ              
7005: F0 E0      LD      A,($E0)         
7007: E0 CB      LDFF00  ($CB),A         
7009: E0 87      LDFF00  ($87),A         
700B: C0         RET     NZ              
700C: 8E         ADC     A,(HL)          
700D: C0         RET     NZ              
700E: 9F         SBC     A               
700F: C0         RET     NZ              
7010: FF         RST     0X38            
7011: FF         RST     0X38            
7012: AF         XOR     A               
7013: FF         RST     0X38            
7014: D0         RET     NC              
7015: 0E 3B      LD      C,$3B           
7017: 00         NOP                     
7018: C0         RET     NZ              
7019: 00         NOP                     
701A: FF         RST     0X38            
701B: 00         NOP                     
701C: F9         LD      SP,HL           
701D: 06 FA      LD      B,$FA           
701F: 04         INC     B               
7020: FF         RST     0X38            
7021: FF         RST     0X38            
7022: C2 FF 25   JP      NZ,$25FF        
7025: 50         LD      D,B             
7026: 01 20 4F   LD      BC,$4F20        
7029: 00         NOP                     
702A: FE 01      CP      $01             
702C: FB         EI                      
702D: 04         INC     B               
702E: EF         RST     0X28            
702F: 00         NOP                     
7030: FF         RST     0X38            
7031: FF         RST     0X38            
7032: 0F         RRCA                    
7033: FF         RST     0X38            
7034: B5         OR      L               
7035: 0F         RRCA                    
7036: 9B         SBC     E               
7037: 07         RLCA                    
7038: FB         EI                      
7039: 07         RLCA                    
703A: E9         JP      (HL)            
703B: 17         RLA                     
703C: 7D         LD      A,L             
703D: 03         INC     BC              
703E: F5         PUSH    AF              
703F: 0B         DEC     BC              
7040: FF         RST     0X38            
7041: FF         RST     0X38            
7042: FF         RST     0X38            
7043: FF         RST     0X38            
7044: FF         RST     0X38            
7045: FF         RST     0X38            
7046: FF         RST     0X38            
7047: FF         RST     0X38            
7048: E0 FF      LDFF00  ($FF),A         
704A: E7         RST     0X20            
704B: FF         RST     0X38            
704C: EF         RST     0X28            
704D: FF         RST     0X38            
704E: EF         RST     0X28            
704F: FF         RST     0X38            
7050: FF         RST     0X38            
7051: FF         RST     0X38            
7052: FF         RST     0X38            
7053: FF         RST     0X38            
7054: FF         RST     0X38            
7055: FF         RST     0X38            
7056: BF         CP      A               
7057: FF         RST     0X38            
7058: 01 FF 80   LD      BC,$80FF        
705B: FF         RST     0X38            
705C: E0 FF      LDFF00  ($FF),A         
705E: E0 FF      LDFF00  ($FF),A         
7060: FF         RST     0X38            
7061: FF         RST     0X38            
7062: FF         RST     0X38            
7063: FF         RST     0X38            
7064: FF         RST     0X38            
7065: FF         RST     0X38            
7066: 7F         LD      A,A             
7067: FF         RST     0X38            
7068: 3E FF      LD      A,$FF           
706A: 0C         INC     C               
706B: FF         RST     0X38            
706C: 00         NOP                     
706D: FF         RST     0X38            
706E: 03         INC     BC              
706F: FC         ???                     
7070: FF         RST     0X38            
7071: FF         RST     0X38            
7072: FF         RST     0X38            
7073: FF         RST     0X38            
7074: FF         RST     0X38            
7075: FF         RST     0X38            
7076: F8 FF      LDHL    SP,$FF          
7078: 01 FF 50   LD      BC,$50FF        
707B: AF         XOR     A               
707C: 00         NOP                     
707D: FF         RST     0X38            
707E: 00         NOP                     
707F: FF         RST     0X38            
7080: FF         RST     0X38            
7081: FF         RST     0X38            
7082: 7F         LD      A,A             
7083: FF         RST     0X38            
7084: 3F         CCF                     
7085: FF         RST     0X38            
7086: 3F         CCF                     
7087: FF         RST     0X38            
7088: 1F         RRA                     
7089: FF         RST     0X38            
708A: 3F         CCF                     
708B: EF         RST     0X28            
708C: 3F         CCF                     
708D: EF         RST     0X28            
708E: 1F         RRA                     
708F: EF         RST     0X28            
7090: E7         RST     0X20            
7091: FF         RST     0X38            
7092: E1         POP     HL              
7093: FF         RST     0X38            
7094: E3         ???                     
7095: FF         RST     0X38            
7096: E7         RST     0X20            
7097: FF         RST     0X38            
7098: E7         RST     0X20            
7099: FF         RST     0X38            
709A: E7         RST     0X20            
709B: FF         RST     0X38            
709C: E0 FF      LDFF00  ($FF),A         
709E: E0 FF      LDFF00  ($FF),A         
70A0: F8 FF      LDHL    SP,$FF          
70A2: FC         ???                     
70A3: FF         RST     0X38            
70A4: FE FF      CP      $FF             
70A6: DE FF      SBC     $FF             
70A8: 9E         SBC     (HL)            
70A9: FF         RST     0X38            
70AA: 13         INC     DE              
70AB: EC         ???                     
70AC: 1F         RRA                     
70AD: E0 1F      LDFF00  ($1F),A         
70AF: E0 00      LDFF00  ($00),A         
70B1: FF         RST     0X38            
70B2: 00         NOP                     
70B3: FF         RST     0X38            
70B4: 00         NOP                     
70B5: FF         RST     0X38            
70B6: 18 FF      JR      $70B7           
70B8: 22         LD      (HLI),A         
70B9: FD         ???                     
70BA: D5         PUSH    DE              
70BB: 28 EB      JR      Z,$70A8         
70BD: 10 FF      STOP    $FF             
70BF: 00         NOP                     
70C0: 00         NOP                     
70C1: FF         RST     0X38            
70C2: 00         NOP                     
70C3: FF         RST     0X38            
70C4: 19         ADD     HL,DE           
70C5: FF         RST     0X38            
70C6: 7F         LD      A,A             
70C7: FF         RST     0X38            
70C8: FF         RST     0X38            
70C9: FF         RST     0X38            
70CA: 0B         DEC     BC              
70CB: FF         RST     0X38            
70CC: 90         SUB     B               
70CD: 6F         LD      L,A             
70CE: F0 0F      LD      A,($0F)         
70D0: 00         NOP                     
70D1: FF         RST     0X38            
70D2: 01 FF 81   LD      BC,$81FF        
70D5: FF         RST     0X38            
70D6: E0 FF      LDFF00  ($FF),A         
70D8: F0 FF      LD      A,($FF)         
70DA: F3         DI                      
70DB: FC         ???                     
70DC: 9F         SBC     A               
70DD: 60         LD      H,B             
70DE: FF         RST     0X38            
70DF: 00         NOP                     
70E0: C6 FF      ADD     $FF             
70E2: EF         RST     0X28            
70E3: FF         RST     0X38            
70E4: EF         RST     0X28            
70E5: FF         RST     0X38            
70E6: C6 FF      ADD     $FF             
70E8: 30 FF      JR      NC,$70E9        
70EA: 86         ADD     A,(HL)          
70EB: 79         LD      A,C             
70EC: 86         ADD     A,(HL)          
70ED: 79         LD      A,C             
70EE: CF         RST     0X08            
70EF: 30 30      JR      NC,$7121        
70F1: FF         RST     0X38            
70F2: 78         LD      A,B             
70F3: FF         RST     0X38            
70F4: 78         LD      A,B             
70F5: FF         RST     0X38            
70F6: 30 FF      JR      NC,$70F7        
70F8: C0         RET     NZ              
70F9: FF         RST     0X38            
70FA: 18 E7      JR      $70E3           
70FC: 1F         RRA                     
70FD: E0 3F      LDFF00  ($3F),A         
70FF: C0         RET     NZ              
7100: AF         XOR     A               
7101: C0         RET     NZ              
7102: A7         AND     A               
7103: C8         RET     Z               
7104: DB         ???                     
7105: 80         ADD     A,B             
7106: FF         RST     0X38            
7107: 80         ADD     A,B             
7108: C3 FC E0   JP      $E0FC           
710B: FF         RST     0X38            
710C: A8         XOR     B               
710D: FF         RST     0X38            
710E: FF         RST     0X38            
710F: FF         RST     0X38            
7110: DC 20 FF   CALL    C,$FF20         
7113: 00         NOP                     
7114: BF         CP      A               
7115: 00         NOP                     
7116: FF         RST     0X38            
7117: 00         NOP                     
7118: 0F         RRCA                    
7119: F0 73      LD      A,($73)         
711B: 8F         ADC     A,A             
711C: 0E FF      LD      C,$FF           
711E: FF         RST     0X38            
711F: FF         RST     0X38            
7120: FF         RST     0X38            
7121: 00         NOP                     
7122: F7         RST     0X30            
7123: 08 FF 00   LD      ($00FF),SP      
7126: B7         OR      A               
7127: 78         LD      A,B             
7128: 53         LD      D,E             
7129: EC         ???                     
712A: 7C         LD      A,H             
712B: 87         ADD     A,A             
712C: 36 FF      LD      (HL),$FF        
712E: FF         RST     0X38            
712F: FF         RST     0X38            
7130: C5         PUSH    BC              
7131: 23         INC     HL              
7132: E9         JP      (HL)            
7133: 07         RLCA                    
7134: C3 0F 57   JP      $570F           
7137: 0F         RRCA                    
7138: AD         XOR     L               
7139: 1F         RRA                     
713A: 69         LD      L,C             
713B: 9F         SBC     A               
713C: 0B         DEC     BC              
713D: FF         RST     0X38            
713E: FF         RST     0X38            
713F: FF         RST     0X38            
7140: 60         LD      H,B             
7141: FF         RST     0X38            
7142: C8         RET     Z               
7143: F7         RST     0X30            
7144: 98         SBC     B               
7145: E7         RST     0X20            
7146: 22         LD      (HLI),A         
7147: DD         ???                     
7148: 07         RLCA                    
7149: F8 3F      LDHL    SP,$3F          
714B: C0         RET     NZ              
714C: FF         RST     0X38            
714D: 00         NOP                     
714E: FF         RST     0X38            
714F: 00         NOP                     
7150: 00         NOP                     
7151: FF         RST     0X38            
7152: 00         NOP                     
7153: FF         RST     0X38            
7154: 18 FF      JR      $7155           
7156: 18 F7      JR      $714F           
7158: 02         LD      (BC),A          
7159: FD         ???                     
715A: FF         RST     0X38            
715B: 00         NOP                     
715C: FF         RST     0X38            
715D: 00         NOP                     
715E: FF         RST     0X38            
715F: 00         NOP                     
7160: 00         NOP                     
7161: FF         RST     0X38            
7162: 00         NOP                     
7163: FF         RST     0X38            
7164: 03         INC     BC              
7165: FF         RST     0X38            
7166: 17         RLA                     
7167: EF         RST     0X28            
7168: 3E C7      LD      A,$C7           
716A: FC         ???                     
716B: 0F         RRCA                    
716C: F4         ???                     
716D: 0F         RRCA                    
716E: F0 0F      LD      A,($0F)         
7170: 1F         RRA                     
7171: EF         RST     0X28            
7172: 7F         LD      A,A             
7173: FF         RST     0X38            
7174: BF         CP      A               
7175: FF         RST     0X38            
7176: 3F         CCF                     
7177: FF         RST     0X38            
7178: 3F         CCF                     
7179: FF         RST     0X38            
717A: 1B         DEC     DE              
717B: FF         RST     0X38            
717C: 17         RLA                     
717D: FB         EI                      
717E: 3F         CCF                     
717F: FF         RST     0X38            
7180: F0 FF      LD      A,($FF)         
7182: F1         POP     AF              
7183: FF         RST     0X38            
7184: FB         EI                      
7185: FE F8      CP      $F8             
7187: FF         RST     0X38            
7188: FC         ???                     
7189: FF         RST     0X38            
718A: F8 FF      LDHL    SP,$FF          
718C: F8 FF      LDHL    SP,$FF          
718E: F0 FF      LD      A,($FF)         
7190: 33         INC     SP              
7191: CC 38 C7   CALL    Z,$C738         
7194: 39         ADD     HL,SP           
7195: C6 1E      ADD     $1E             
7197: E1         POP     HL              
7198: 1E E1      LD      E,$E1           
719A: 1C         INC     E               
719B: E3         ???                     
719C: 1C         INC     E               
719D: E3         ???                     
719E: 3C         INC     A               
719F: C3 FF 00   JP      $00FF           
71A2: 80         ADD     A,B             
71A3: 7F         LD      A,A             
71A4: 00         NOP                     
71A5: FF         RST     0X38            
71A6: 00         NOP                     
71A7: FF         RST     0X38            
71A8: 00         NOP                     
71A9: 1C         INC     E               
71AA: 00         NOP                     
71AB: 1C         INC     E               
71AC: 00         NOP                     
71AD: 1C         INC     E               
71AE: 00         NOP                     
71AF: FF         RST     0X38            
71B0: E7         RST     0X20            
71B1: 18 8F      JR      $7142           
71B3: 70         LD      (HL),B          
71B4: 4F         LD      C,A             
71B5: B0         OR      B               
71B6: 3F         CCF                     
71B7: C0         RET     NZ              
71B8: 3F         CCF                     
71B9: 40         LD      B,B             
71BA: 1F         RRA                     
71BB: 60         LD      H,B             
71BC: 1F         RRA                     
71BD: 60         LD      H,B             
71BE: 17         RLA                     
71BF: E8 F0      ADD     SP,$F0          
71C1: 0F         RRCA                    
71C2: F0 0F      LD      A,($0F)         
71C4: F9         LD      SP,HL           
71C5: 06 FF      LD      B,$FF           
71C7: 00         NOP                     
71C8: FF         RST     0X38            
71C9: 00         NOP                     
71CA: FF         RST     0X38            
71CB: 00         NOP                     
71CC: FF         RST     0X38            
71CD: 00         NOP                     
71CE: 3F         CCF                     
71CF: C0         RET     NZ              
71D0: FF         RST     0X38            
71D1: 00         NOP                     
71D2: FF         RST     0X38            
71D3: 00         NOP                     
71D4: FF         RST     0X38            
71D5: 00         NOP                     
71D6: FF         RST     0X38            
71D7: 00         NOP                     
71D8: FF         RST     0X38            
71D9: 00         NOP                     
71DA: FF         RST     0X38            
71DB: 00         NOP                     
71DC: FF         RST     0X38            
71DD: 00         NOP                     
71DE: FF         RST     0X38            
71DF: 00         NOP                     
71E0: F9         LD      SP,HL           
71E1: 06 F0      LD      B,$F0           
71E3: 0F         RRCA                    
71E4: F0 0F      LD      A,($0F)         
71E6: F9         LD      SP,HL           
71E7: 06 FF      LD      B,$FF           
71E9: 00         NOP                     
71EA: FF         RST     0X38            
71EB: 00         NOP                     
71EC: FF         RST     0X38            
71ED: 00         NOP                     
71EE: FF         RST     0X38            
71EF: 00         NOP                     
71F0: FF         RST     0X38            
71F1: 00         NOP                     
71F2: FF         RST     0X38            
71F3: 00         NOP                     
71F4: FF         RST     0X38            
71F5: 00         NOP                     
71F6: FF         RST     0X38            
71F7: 00         NOP                     
71F8: 24         INC     H               
71F9: DB         ???                     
71FA: 6D         LD      L,L             
71FB: 92         SUB     D               
71FC: 65         LD      H,L             
71FD: 9A         SBC     D               
71FE: F1         POP     AF              
71FF: 0E EF      LD      C,$EF           
7201: 10 DF      STOP    $DF             
7203: 20 B9      JR      NZ,$71BE        
7205: 46         LD      B,(HL)          
7206: B7         OR      A               
7207: 48         LD      C,B             
7208: 02         LD      (BC),A          
7209: FD         ???                     
720A: 74         LD      (HL),H          
720B: 8B         ADC     A,E             
720C: DD         ???                     
720D: 22         LD      (HLI),A         
720E: C3 3C CF   JP      $CF3C           
7211: 30 B7      JR      NC,$71CA        
7213: 48         LD      C,B             
7214: 7B         LD      A,E             
7215: 84         ADD     A,H             
7216: B7         OR      A               
7217: 48         LD      C,B             
7218: CD 32 18   CALL    $1832           
721B: E7         RST     0X20            
721C: DD         ???                     
721D: 22         LD      (HLI),A         
721E: E1         POP     HL              
721F: 1E FF      LD      E,$FF           
7221: 00         NOP                     
7222: FF         RST     0X38            
7223: 00         NOP                     
7224: 8F         ADC     A,A             
7225: 70         LD      (HL),B          
7226: E7         RST     0X20            
7227: 18 24      JR      $724D           
7229: DB         ???                     
722A: 6D         LD      L,L             
722B: 92         SUB     D               
722C: 65         LD      H,L             
722D: 9A         SBC     D               
722E: F1         POP     AF              
722F: 0E 07      LD      C,$07           
7231: 58         LD      E,B             
7232: 03         INC     BC              
7233: BC         CP      H               
7234: 01 FE 70   LD      BC,$70FE        
7237: FF         RST     0X38            
7238: FF         RST     0X38            
7239: FF         RST     0X38            
723A: F8 FF      LDHL    SP,$FF          
723C: FF         RST     0X38            
723D: FF         RST     0X38            
723E: FF         RST     0X38            
723F: FF         RST     0X38            
7240: F3         DI                      
7241: 0C         INC     C               
7242: F3         DI                      
7243: 0C         INC     C               
7244: FB         EI                      
7245: 04         INC     B               
7246: FB         EI                      
7247: 04         INC     B               
7248: FD         ???                     
7249: 02         LD      (BC),A          
724A: FF         RST     0X38            
724B: 00         NOP                     
724C: FF         RST     0X38            
724D: 00         NOP                     
724E: FF         RST     0X38            
724F: 00         NOP                     
7250: 2F         CPL                     
7251: FF         RST     0X38            
7252: 2F         CPL                     
7253: FF         RST     0X38            
7254: 3B         DEC     SP              
7255: FF         RST     0X38            
7256: 37         SCF                     
7257: FB         EI                      
7258: 93         SUB     E               
7259: 3F         CCF                     
725A: 1B         DEC     DE              
725B: 3F         CCF                     
725C: EF         RST     0X28            
725D: 1F         RRA                     
725E: E7         RST     0X20            
725F: 1F         RRA                     
7260: F0 FF      LD      A,($FF)         
7262: F0 FF      LD      A,($FF)         
7264: F1         POP     AF              
7265: FF         RST     0X38            
7266: E3         ???                     
7267: FF         RST     0X38            
7268: E7         RST     0X20            
7269: FF         RST     0X38            
726A: CE FF      ADC     $FF             
726C: FD         ???                     
726D: FF         RST     0X38            
726E: C3 FF 3C   JP      $3CFF           
7271: C3 3C C3   JP      $C33C           
7274: C6 F9      ADD     $F9             
7276: C2 FC 80   JP      NZ,$80FC        
7279: FE C0      CP      $C0             
727B: FE C0      CP      $C0             
727D: FE A0      CP      $A0             
727F: DE 00      SBC     $00             
7281: FF         RST     0X38            
7282: 00         NOP                     
7283: E3         ???                     
7284: 00         NOP                     
7285: E3         ???                     
7286: 00         NOP                     
7287: 36 00      LD      (HL),$00        
7289: 1C         INC     E               
728A: 00         NOP                     
728B: 88         ADC     A,B             
728C: 00         NOP                     
728D: 63         LD      H,E             
728E: 00         NOP                     
728F: 00         NOP                     
7290: 1E E1      LD      E,$E1           
7292: 1E E1      LD      E,$E1           
7294: 31 CF 20   LD      SP,$20CF        
7297: 1F         RRA                     
7298: 00         NOP                     
7299: 3F         CCF                     
729A: 00         NOP                     
729B: BF         CP      A               
729C: 00         NOP                     
729D: 3F         CCF                     
729E: 03         INC     BC              
729F: 3C         INC     A               
72A0: FF         RST     0X38            
72A1: 00         NOP                     
72A2: DF         RST     0X18            
72A3: 00         NOP                     
72A4: 1F         RRA                     
72A5: C0         RET     NZ              
72A6: DF         RST     0X18            
72A7: 20 0F      JR      NZ,$72B8        
72A9: F0 47      LD      A,($47)         
72AB: B8         CP      B               
72AC: 21 DE 1F   LD      HL,$1FDE        
72AF: E0 F8      LDFF00  ($F8),A         
72B1: 07         RLCA                    
72B2: F0 0F      LD      A,($0F)         
72B4: C0         RET     NZ              
72B5: 3F         CCF                     
72B6: C0         RET     NZ              
72B7: 3F         CCF                     
72B8: 80         ADD     A,B             
72B9: 7F         LD      A,A             
72BA: 84         ADD     A,H             
72BB: 7B         LD      A,E             
72BC: 86         ADD     A,(HL)          
72BD: 79         LD      A,C             
72BE: CF         RST     0X08            
72BF: 30 1F      JR      NC,$72E0        
72C1: E0 0F      LDFF00  ($0F),A         
72C3: F0 1F      LD      A,($1F)         
72C5: E0 7F      LDFF00  ($7F),A         
72C7: 80         ADD     A,B             
72C8: 3F         CCF                     
72C9: C0         RET     NZ              
72CA: 1F         RRA                     
72CB: E0 1F      LDFF00  ($1F),A         
72CD: E0 1F      LDFF00  ($1F),A         
72CF: E0 F3      LDFF00  ($F3),A         
72D1: 0F         RRCA                    
72D2: F3         DI                      
72D3: 0F         RRCA                    
72D4: F3         DI                      
72D5: 0F         RRCA                    
72D6: E3         ???                     
72D7: 1F         RRA                     
72D8: E3         ???                     
72D9: 1F         RRA                     
72DA: D7         RST     0X10            
72DB: 2F         CPL                     
72DC: DF         RST     0X18            
72DD: 27         DAA                     
72DE: D7         RST     0X10            
72DF: 2F         CPL                     
72E0: 06 F8      LD      B,$F8           
72E2: 3E C0      LD      A,$C0           
72E4: 3F         CCF                     
72E5: C0         RET     NZ              
72E6: 7F         LD      A,A             
72E7: 80         ADD     A,B             
72E8: 78         LD      A,B             
72E9: 87         ADD     A,A             
72EA: 30 C8      JR      NC,$72B4        
72EC: 30 CB      JR      NC,$72B9        
72EE: 33         INC     SP              
72EF: CC 00 1C   CALL    Z,$1C00         
72F2: 00         NOP                     
72F3: 80         ADD     A,B             
72F4: 00         NOP                     
72F5: 63         LD      H,E             
72F6: 80         ADD     A,B             
72F7: 00         NOP                     
72F8: 00         NOP                     
72F9: E3         ???                     
72FA: 00         NOP                     
72FB: 3E 00      LD      A,$00           
72FD: FF         RST     0X38            
72FE: C1         POP     BC              
72FF: 3E 31      LD      A,$31           
7301: 0E 3F      LD      C,$3F           
7303: 80         ADD     A,B             
7304: 7F         LD      A,A             
7305: 00         NOP                     
7306: FF         RST     0X38            
7307: 00         NOP                     
7308: 0F         RRCA                    
7309: F0 07      LD      A,($07)         
730B: 08 07 E8   LD      ($E807),SP      
730E: E7         RST     0X20            
730F: 18 CF      JR      $72E0           
7311: 3F         CCF                     
7312: CF         RST     0X08            
7313: 3F         CCF                     
7314: C3 3F E3   JP      $E33F           
7317: 1F         RRA                     
7318: F3         DI                      
7319: 0F         RRCA                    
731A: F3         DI                      
731B: 0F         RRCA                    
731C: F3         DI                      
731D: 0F         RRCA                    
731E: F3         DI                      
731F: 0F         RRCA                    
7320: E0 FF      LDFF00  ($FF),A         
7322: E0 FF      LDFF00  ($FF),A         
7324: E0 FF      LDFF00  ($FF),A         
7326: E0 FF      LDFF00  ($FF),A         
7328: E6 FF      AND     $FF             
732A: EF         RST     0X28            
732B: FF         RST     0X38            
732C: EF         RST     0X28            
732D: FF         RST     0X38            
732E: E6 FF      AND     $FF             
7330: 1F         RRA                     
7331: E0 1F      LDFF00  ($1F),A         
7333: E0 3F      LDFF00  ($3F),A         
7335: C0         RET     NZ              
7336: 3F         CCF                     
7337: C0         RET     NZ              
7338: 0E F1      LD      C,$F1           
733A: 44         LD      B,H             
733B: FB         EI                      
733C: 44         LD      B,H             
733D: FB         EI                      
733E: 0E F1      LD      C,$F1           
7340: 80         ADD     A,B             
7341: 7F         LD      A,A             
7342: 80         ADD     A,B             
7343: 7F         LD      A,A             
7344: 94         SUB     H               
7345: 6B         LD      L,E             
7346: FF         RST     0X38            
7347: 00         NOP                     
7348: 7F         LD      A,A             
7349: 80         ADD     A,B             
734A: 3F         CCF                     
734B: C0         RET     NZ              
734C: 3F         CCF                     
734D: C0         RET     NZ              
734E: 7F         LD      A,A             
734F: 80         ADD     A,B             
7350: BF         CP      A               
7351: 40         LD      B,B             
7352: 5F         LD      E,A             
7353: 80         ADD     A,B             
7354: 58         LD      E,B             
7355: 87         ADD     A,A             
7356: D0         RET     NC              
7357: 0F         RRCA                    
7358: F3         DI                      
7359: 0C         INC     C               
735A: F7         RST     0X30            
735B: 08 F7 08   LD      ($08F7),SP      
735E: FF         RST     0X38            
735F: 00         NOP                     
7360: CF         RST     0X08            
7361: 30 9D      JR      NC,$7300        
7363: 62         LD      H,D             
7364: 1E E1      LD      E,$E1           
7366: BF         CP      A               
7367: 40         LD      B,B             
7368: FE 00      CP      $00             
736A: FF         RST     0X38            
736B: 00         NOP                     
736C: 8D         ADC     A,L             
736D: 00         NOP                     
736E: 73         LD      (HL),E          
736F: 00         NOP                     
7370: FF         RST     0X38            
7371: 00         NOP                     
7372: FF         RST     0X38            
7373: 00         NOP                     
7374: 06 79      LD      B,$79           
7376: C5         PUSH    BC              
7377: 3A         LD      A,(HLD)         
7378: F4         ???                     
7379: 08 E8 13   LD      ($13E8),SP      
737C: C8         RET     Z               
737D: 33         INC     SP              
737E: A7         AND     A               
737F: 40         LD      B,B             
7380: D7         RST     0X10            
7381: 20 E7      JR      NZ,$736A        
7383: 18 95      JR      $731A           
7385: 0A         LD      A,(BC)          
7386: 36 49      LD      (HL),$49        
7388: 85         ADD     A,L             
7389: 7A         LD      A,D             
738A: AA         XOR     D               
738B: 54         LD      D,H             
738C: 94         SUB     H               
738D: 68         LD      L,B             
738E: C4 39 FF   CALL    NZ,$FF39        
7391: 00         NOP                     
7392: FF         RST     0X38            
7393: 00         NOP                     
7394: A1         AND     C               
7395: 4E         LD      C,(HL)          
7396: B9         CP      C               
7397: 06 44      LD      B,$44           
7399: 38 6B      JR      C,$7406         
739B: 90         SUB     B               
739C: 51         LD      D,C             
739D: A2         AND     D               
739E: A7         AND     A               
739F: 40         LD      B,B             
73A0: E1         POP     HL              
73A1: FF         RST     0X38            
73A2: E3         ???                     
73A3: FF         RST     0X38            
73A4: E3         ???                     
73A5: FF         RST     0X38            
73A6: E1         POP     HL              
73A7: FF         RST     0X38            
73A8: E0 FF      LDFF00  ($FF),A         
73AA: E0 FF      LDFF00  ($FF),A         
73AC: E0 FF      LDFF00  ($FF),A         
73AE: E0 FF      LDFF00  ($FF),A         
73B0: 99         SBC     C               
73B1: E6 D0      AND     $D0             
73B3: EF         RST     0X28            
73B4: D0         RET     NC              
73B5: EF         RST     0X28            
73B6: 99         SBC     C               
73B7: E6 2F      AND     $2F             
73B9: F0 67      LD      A,($67)         
73BB: F8 67      LDHL    SP,$67          
73BD: F8 2F      LDHL    SP,$2F          
73BF: F0 FE      LD      A,($FE)         
73C1: 00         NOP                     
73C2: FF         RST     0X38            
73C3: 00         NOP                     
73C4: EF         RST     0X28            
73C5: 30 13      JR      NC,$73DA        
73C7: EC         ???                     
73C8: 7B         LD      A,E             
73C9: 80         ADD     A,B             
73CA: 7B         LD      A,E             
73CB: 80         ADD     A,B             
73CC: C7         RST     0X00            
73CD: 00         NOP                     
73CE: FF         RST     0X38            
73CF: 00         NOP                     
73D0: FF         RST     0X38            
73D1: 00         NOP                     
73D2: FF         RST     0X38            
73D3: 00         NOP                     
73D4: FF         RST     0X38            
73D5: 00         NOP                     
73D6: FF         RST     0X38            
73D7: 00         NOP                     
73D8: FE 01      CP      $01             
73DA: F8 07      LDHL    SP,$07          
73DC: F2         ???                     
73DD: 0D         DEC     C               
73DE: E8 17      ADD     SP,$17          
73E0: FF         RST     0X38            
73E1: 00         NOP                     
73E2: FF         RST     0X38            
73E3: 00         NOP                     
73E4: FF         RST     0X38            
73E5: 00         NOP                     
73E6: E5         PUSH    HL              
73E7: 1A         LD      A,(DE)          
73E8: 92         SUB     D               
73E9: 7D         LD      A,L             
73EA: 28 D7      JR      Z,$73C3         
73EC: 00         NOP                     
73ED: FF         RST     0X38            
73EE: 00         NOP                     
73EF: 77         LD      (HL),A          
73F0: C7         RST     0X00            
73F1: 38 BF      JR      C,$73B2         
73F3: 40         LD      B,B             
73F4: 7B         LD      A,E             
73F5: 80         ADD     A,B             
73F6: 84         ADD     A,H             
73F7: FB         EI                      
73F8: 8C         ADC     A,H             
73F9: F3         DI                      
73FA: 31 CE 03   LD      SP,$03CE        
73FD: FC         ???                     
73FE: 07         RLCA                    
73FF: 78         LD      A,B             
7400: BF         CP      A               
7401: 00         NOP                     
7402: 7E         LD      A,(HL)          
7403: 01 FD 02   LD      BC,$02FD        
7406: FF         RST     0X38            
7407: 00         NOP                     
7408: EB         ???                     
7409: 10 D7      STOP    $D7             
740B: 20 FF      JR      NZ,$740C        
740D: 00         NOP                     
740E: 5F         LD      E,A             
740F: 80         ADD     A,B             
7410: 1F         RRA                     
7411: E0 1F      LDFF00  ($1F),A         
7413: E0 1F      LDFF00  ($1F),A         
7415: E0 1F      LDFF00  ($1F),A         
7417: E0 1F      LDFF00  ($1F),A         
7419: E0 1F      LDFF00  ($1F),A         
741B: E0 3F      LDFF00  ($3F),A         
741D: C0         RET     NZ              
741E: 1F         RRA                     
741F: E0 FF      LDFF00  ($FF),A         
7421: 00         NOP                     
7422: FF         RST     0X38            
7423: 00         NOP                     
7424: EF         RST     0X28            
7425: 10 F7      STOP    $F7             
7427: 00         NOP                     
7428: FF         RST     0X38            
7429: 00         NOP                     
742A: FF         RST     0X38            
742B: 00         NOP                     
742C: FF         RST     0X38            
742D: 00         NOP                     
742E: FF         RST     0X38            
742F: 00         NOP                     
7430: C0         RET     NZ              
7431: 3E C0      LD      A,$C0           
7433: 3B         DEC     SP              
7434: 80         ADD     A,B             
7435: 75         LD      (HL),L          
7436: 80         ADD     A,B             
7437: 7B         LD      A,E             
7438: 00         NOP                     
7439: EF         RST     0X28            
743A: 00         NOP                     
743B: D7         RST     0X10            
743C: 01 EE 01   LD      BC,$01EE        
743F: FE 00      CP      $00             
7441: AA         XOR     D               
7442: 00         NOP                     
7443: 77         LD      (HL),A          
7444: 00         NOP                     
7445: FF         RST     0X38            
7446: 00         NOP                     
7447: FF         RST     0X38            
7448: 3F         CCF                     
7449: C0         RET     NZ              
744A: FF         RST     0X38            
744B: 00         NOP                     
744C: FF         RST     0X38            
744D: 00         NOP                     
744E: FF         RST     0X38            
744F: 00         NOP                     
7450: 0F         RRCA                    
7451: B0         OR      B               
7452: 1F         RRA                     
7453: 60         LD      H,B             
7454: 3F         CCF                     
7455: C0         RET     NZ              
7456: 7F         LD      A,A             
7457: 80         ADD     A,B             
7458: FF         RST     0X38            
7459: 00         NOP                     
745A: FF         RST     0X38            
745B: 00         NOP                     
745C: FF         RST     0X38            
745D: 00         NOP                     
745E: FF         RST     0X38            
745F: 00         NOP                     
7460: FF         RST     0X38            
7461: 00         NOP                     
7462: FF         RST     0X38            
7463: 00         NOP                     
7464: FF         RST     0X38            
7465: 00         NOP                     
7466: FF         RST     0X38            
7467: 00         NOP                     
7468: FE 01      CP      $01             
746A: FC         ???                     
746B: 03         INC     BC              
746C: F0 0F      LD      A,($0F)         
746E: 80         ADD     A,B             
746F: 7F         LD      A,A             
7470: 9F         SBC     A               
7471: E0 1F      LDFF00  ($1F),A         
7473: E0 3F      LDFF00  ($3F),A         
7475: C0         RET     NZ              
7476: 3F         CCF                     
7477: C0         RET     NZ              
7478: 1E E1      LD      E,$E1           
747A: 19         ADD     HL,DE           
747B: E7         RST     0X20            
747C: 00         NOP                     
747D: FF         RST     0X38            
747E: 60         LD      H,B             
747F: FF         RST     0X38            
7480: FF         RST     0X38            
7481: 00         NOP                     
7482: FE 01      CP      $01             
7484: F6 09      OR      $09             
7486: 87         ADD     A,A             
7487: 78         LD      A,B             
7488: 03         INC     BC              
7489: FC         ???                     
748A: 01 FE 80   LD      BC,$80FE        
748D: 7F         LD      A,A             
748E: 00         NOP                     
748F: FF         RST     0X38            
7490: FC         ???                     
7491: 03         INC     BC              
7492: 43         LD      B,E             
7493: BC         CP      H               
7494: 30 CF      JR      NC,$7465        
7496: 0E F1      LD      C,$F1           
7498: 81         ADD     A,C             
7499: 7E         LD      A,(HL)          
749A: F0 0F      LD      A,($0F)         
749C: 7F         LD      A,A             
749D: 80         ADD     A,B             
749E: 1F         RRA                     
749F: E0 01      LDFF00  ($01),A         
74A1: FE 06      CP      $06             
74A3: F9         LD      SP,HL           
74A4: F8 07      LDHL    SP,$07          
74A6: 03         INC     BC              
74A7: FC         ???                     
74A8: FC         ???                     
74A9: 03         INC     BC              
74AA: 01 FE FF   LD      BC,$FFFE        
74AD: 00         NOP                     
74AE: FF         RST     0X38            
74AF: 00         NOP                     
74B0: B9         CP      C               
74B1: 7E         LD      A,(HL)          
74B2: 3B         DEC     SP              
74B3: E6 23      AND     $23             
74B5: DC CE 70   CALL    C,$70CE         
74B8: 3C         INC     A               
74B9: C0         RET     NZ              
74BA: E0 01      LDFF00  ($01),A         
74BC: E0 1F      LDFF00  ($1F),A         
74BE: 00         NOP                     
74BF: FF         RST     0X38            
74C0: FF         RST     0X38            
74C1: 00         NOP                     
74C2: 04         INC     B               
74C3: FB         EI                      
74C4: 38 C7      JR      C,$748D         
74C6: C1         POP     BC              
74C7: 3E 07      LD      A,$07           
74C9: F8 7E      LDHL    SP,$7E          
74CB: 81         ADD     A,C             
74CC: F8 07      LDHL    SP,$07          
74CE: C0         RET     NZ              
74CF: 3F         CCF                     
74D0: FF         RST     0X38            
74D1: 00         NOP                     
74D2: 7F         LD      A,A             
74D3: 80         ADD     A,B             
74D4: F1         POP     AF              
74D5: 0E F3      LD      C,$F3           
74D7: 0C         INC     C               
74D8: B6         OR      (HL)            
74D9: 49         LD      C,C             
74DA: 3C         INC     A               
74DB: C3 38 C7   JP      $C738           
74DE: 31 CE E7   LD      SP,$E7CE        
74E1: 18 DF      JR      $74C2           
74E3: 20 BD      JR      NZ,$74A2        
74E5: 40         LD      B,B             
74E6: 7D         LD      A,L             
74E7: C0         RET     NZ              
74E8: 73         LD      (HL),E          
74E9: C8         RET     Z               
74EA: 5B         LD      E,E             
74EB: 84         ADD     A,H             
74EC: C7         RST     0X00            
74ED: 38 8C      JR      C,$747B         
74EF: 73         LD      (HL),E          
74F0: FE 01      CP      $01             
74F2: F4         ???                     
74F3: 0B         DEC     BC              
74F4: F8 07      LDHL    SP,$07          
74F6: F0 0F      LD      A,($0F)         
74F8: F0 0F      LD      A,($0F)         
74FA: E0 1F      LDFF00  ($1F),A         
74FC: E0 1F      LDFF00  ($1F),A         
74FE: E0 1F      LDFF00  ($1F),A         
7500: 00         NOP                     
7501: FF         RST     0X38            
7502: 08 FF 04   LD      ($04FF),SP      
7505: CB 30      SET     1,E             
7507: 87         ADD     A,A             
7508: 30 87      JR      NC,$7491        
750A: 00         NOP                     
750B: CF         RST     0X08            
750C: 00         NOP                     
750D: FF         RST     0X38            
750E: 00         NOP                     
750F: FF         RST     0X38            
7510: E0 FF      LDFF00  ($FF),A         
7512: F1         POP     AF              
7513: FF         RST     0X38            
7514: E3         ???                     
7515: FF         RST     0X38            
7516: E7         RST     0X20            
7517: FF         RST     0X38            
7518: E7         RST     0X20            
7519: FF         RST     0X38            
751A: EF         RST     0X28            
751B: FF         RST     0X38            
751C: ED         ???                     
751D: FE C0      CP      $C0             
751F: FF         RST     0X38            
7520: E0 FF      LDFF00  ($FF),A         
7522: E0 FF      LDFF00  ($FF),A         
7524: E0 FF      LDFF00  ($FF),A         
7526: A0         AND     B               
7527: FF         RST     0X38            
7528: F8 E0      LDHL    SP,$E0          
752A: D8         RET     C               
752B: 20 D8      JR      NZ,$7505        
752D: 20 DC      JR      NZ,$750B        
752F: 20 00      JR      NZ,$7531        
7531: FF         RST     0X38            
7532: 00         NOP                     
7533: FF         RST     0X38            
7534: 00         NOP                     
7535: FF         RST     0X38            
7536: 00         NOP                     
7537: FF         RST     0X38            
7538: 30 01      JR      NC,$753B        
753A: 70         LD      (HL),B          
753B: 00         NOP                     
753C: 70         LD      (HL),B          
753D: 00         NOP                     
753E: B8         CP      B               
753F: C0         RET     NZ              
7540: 00         NOP                     
7541: FF         RST     0X38            
7542: 00         NOP                     
7543: FF         RST     0X38            
7544: 02         LD      (BC),A          
7545: FF         RST     0X38            
7546: 01 FE 00   LD      BC,$00FE        
7549: FF         RST     0X38            
754A: 60         LD      H,B             
754B: 07         RLCA                    
754C: E0 01      LDFF00  ($01),A         
754E: F3         DI                      
754F: 00         NOP                     
7550: 00         NOP                     
7551: FF         RST     0X38            
7552: 00         NOP                     
7553: FF         RST     0X38            
7554: 00         NOP                     
7555: FF         RST     0X38            
7556: 00         NOP                     
7557: FF         RST     0X38            
7558: 00         NOP                     
7559: F1         POP     AF              
755A: 00         NOP                     
755B: E0 00      LDFF00  ($00),A         
755D: E0 80      LDFF00  ($80),A         
755F: 60         LD      H,B             
7560: 00         NOP                     
7561: FF         RST     0X38            
7562: 00         NOP                     
7563: FF         RST     0X38            
7564: 00         NOP                     
7565: FF         RST     0X38            
7566: 00         NOP                     
7567: FF         RST     0X38            
7568: 10 FF      STOP    $FF             
756A: 00         NOP                     
756B: F7         RST     0X30            
756C: 00         NOP                     
756D: FF         RST     0X38            
756E: 00         NOP                     
756F: FF         RST     0X38            
7570: 00         NOP                     
7571: FF         RST     0X38            
7572: 08 FF 24   LD      ($24FF),SP      
7575: FB         EI                      
7576: 44         LD      B,H             
7577: FB         EI                      
7578: 00         NOP                     
7579: F7         RST     0X30            
757A: 30 CF      JR      NC,$754B        
757C: 00         NOP                     
757D: FF         RST     0X38            
757E: 00         NOP                     
757F: FF         RST     0X38            
7580: 00         NOP                     
7581: FF         RST     0X38            
7582: 00         NOP                     
7583: FF         RST     0X38            
7584: 08 FF 00   LD      ($00FF),SP      
7587: FF         RST     0X38            
7588: 01 FF 06   LD      BC,$06FF        
758B: FF         RST     0X38            
758C: 0C         INC     C               
758D: FF         RST     0X38            
758E: 08 FF 33   LD      ($33FF),SP      
7591: CC 36 C9   CALL    Z,$C936         
7594: 3D         DEC     A               
7595: C3 3A C7   JP      $C73A           
7598: F3         DI                      
7599: CE 12      ADC     $12             
759B: ED         ???                     
759C: 24         INC     H               
759D: C9         RET                     
759E: 2D         DEC     L               
759F: C2 1E E1   JP      NZ,$E11E        
75A2: F3         DI                      
75A3: CC 51 AE   CALL    Z,$AE51         
75A6: 90         SUB     B               
75A7: 67         LD      H,A             
75A8: A4         AND     H               
75A9: 53         LD      D,E             
75AA: 56         LD      D,(HL)          
75AB: A9         XOR     C               
75AC: 03         INC     BC              
75AD: 9C         SBC     H               
75AE: B1         OR      C               
75AF: 4E         LD      C,(HL)          
75B0: 7F         LD      A,A             
75B1: 80         ADD     A,B             
75B2: 67         LD      H,A             
75B3: 98         SBC     B               
75B4: E3         ???                     
75B5: 1C         INC     E               
75B6: E0 1F      LDFF00  ($1F),A         
75B8: 68         LD      L,B             
75B9: 97         SUB     A               
75BA: 60         LD      H,B             
75BB: 9F         SBC     A               
75BC: 60         LD      H,B             
75BD: 9F         SBC     A               
75BE: E2         LDFF00  (C),A           
75BF: 1D         DEC     E               
75C0: E0 1E      LDFF00  ($1E),A         
75C2: C1         POP     BC              
75C3: 3C         INC     A               
75C4: C1         POP     BC              
75C5: 3C         INC     A               
75C6: C0         RET     NZ              
75C7: 3E 10      LD      A,$10           
75C9: FF         RST     0X38            
75CA: 08 F7 20   LD      ($20F7),SP      
75CD: FF         RST     0X38            
75CE: 10 EF      STOP    $EF             
75D0: 03         INC     BC              
75D1: 7C         LD      A,H             
75D2: 87         ADD     A,A             
75D3: 38 8F      JR      C,$7564         
75D5: 30 0F      JR      NC,$75E6        
75D7: 70         LD      (HL),B          
75D8: 1F         RRA                     
75D9: E0 1F      LDFF00  ($1F),A         
75DB: E0 3F      LDFF00  ($3F),A         
75DD: C0         RET     NZ              
75DE: 3F         CCF                     
75DF: C0         RET     NZ              
75E0: 80         ADD     A,B             
75E1: FF         RST     0X38            
75E2: CC FF EF   CALL    Z,$EFFF         
75E5: FF         RST     0X38            
75E6: E7         RST     0X20            
75E7: FF         RST     0X38            
75E8: E7         RST     0X20            
75E9: FF         RST     0X38            
75EA: E3         ???                     
75EB: FF         RST     0X38            
75EC: E1         POP     HL              
75ED: FF         RST     0X38            
75EE: E0 FF      LDFF00  ($FF),A         
75F0: DC 20 3E   CALL    C,$3E20         
75F3: C0         RET     NZ              
75F4: 1F         RRA                     
75F5: E0 EF      LDFF00  ($EF),A         
75F7: F0 60      LD      A,($60)         
75F9: FF         RST     0X38            
75FA: D0         RET     NC              
75FB: EF         RST     0X28            
75FC: EC         ???                     
75FD: F3         DI                      
75FE: E3         ???                     
75FF: FC         ???                     
7600: 38 80      JR      C,$7582         
7602: FC         ???                     
7603: 00         NOP                     
7604: 7E         LD      A,(HL)          
7605: 00         NOP                     
7606: FE 01      CP      $01             
7608: 00         NOP                     
7609: FF         RST     0X38            
760A: 08 FF 04   LD      ($04FF),SP      
760D: FB         EI                      
760E: 00         NOP                     
760F: FF         RST     0X38            
7610: F3         DI                      
7611: 00         NOP                     
7612: FA 01 F8   LD      A,($F801)       
7615: 07         RLCA                    
7616: 00         NOP                     
7617: FF         RST     0X38            
7618: 1C         INC     E               
7619: E3         ???                     
761A: 03         INC     BC              
761B: FC         ???                     
761C: 01 FE 70   LD      BC,$70FE        
761F: 8F         ADC     A,A             
7620: C0         RET     NZ              
7621: 31 00 FF   LD      SP,$FF00        
7624: 00         NOP                     
7625: FF         RST     0X38            
7626: 60         LD      H,B             
7627: 9F         SBC     A               
7628: 10 EF      STOP    $EF             
762A: 0F         RRCA                    
762B: F0 81      LD      A,($81)         
762D: 7E         LD      A,(HL)          
762E: C0         RET     NZ              
762F: 3F         CCF                     
7630: 08 FF 04   LD      ($04FF),SP      
7633: FB         EI                      
7634: 00         NOP                     
7635: FF         RST     0X38            
7636: 00         NOP                     
7637: FF         RST     0X38            
7638: 00         NOP                     
7639: FF         RST     0X38            
763A: 80         ADD     A,B             
763B: 7F         LD      A,A             
763C: F0 0F      LD      A,($0F)         
763E: 3F         CCF                     
763F: C0         RET     NZ              
7640: 00         NOP                     
7641: FF         RST     0X38            
7642: 00         NOP                     
7643: FF         RST     0X38            
7644: 00         NOP                     
7645: FF         RST     0X38            
7646: 00         NOP                     
7647: FF         RST     0X38            
7648: 0F         RRCA                    
7649: F0 3F      LD      A,($3F)         
764B: C0         RET     NZ              
764C: C0         RET     NZ              
764D: 3F         CCF                     
764E: 00         NOP                     
764F: FF         RST     0X38            
7650: 02         LD      (BC),A          
7651: FF         RST     0X38            
7652: 09         ADD     HL,BC           
7653: FE 15      CP      $15             
7655: FA 48 F7   LD      A,($F748)       
7658: 20 DF      JR      NZ,$7639        
765A: 80         ADD     A,B             
765B: FF         RST     0X38            
765C: 70         LD      (HL),B          
765D: 8F         ADC     A,A             
765E: 3F         CCF                     
765F: C0         RET     NZ              
7660: 1E C1      LD      E,$C1           
7662: F3         DI                      
7663: 0C         INC     C               
7664: B3         OR      E               
7665: 4C         LD      C,H             
7666: 36 C9      LD      (HL),$C9        
7668: 3C         INC     A               
7669: C3 38 C7   JP      $C738           
766C: B1         OR      C               
766D: 4E         LD      C,(HL)          
766E: 33         INC     SP              
766F: CC 18 E7   CALL    Z,$E718         
7672: 0C         INC     C               
7673: F3         DI                      
7674: 86         ADD     A,(HL)          
7675: 79         LD      A,C             
7676: C3 3C 61   JP      $613C           
7679: 9E         SBC     (HL)            
767A: F0 0F      LD      A,($0F)         
767C: 98         SBC     B               
767D: 67         LD      H,A             
767E: 0C         INC     C               
767F: F3         DI                      
7680: E0 1F      LDFF00  ($1F),A         
7682: 60         LD      H,B             
7683: 9F         SBC     A               
7684: 60         LD      H,B             
7685: 9F         SBC     A               
7686: 62         LD      H,D             
7687: 9D         SBC     L               
7688: E0 1F      LDFF00  ($1F),A         
768A: E3         ???                     
768B: 1C         INC     E               
768C: 67         LD      H,A             
768D: 98         SBC     B               
768E: 6F         LD      L,A             
768F: 90         SUB     B               
7690: 20 DF      JR      NZ,$7671        
7692: 80         ADD     A,B             
7693: FF         RST     0X38            
7694: 40         LD      B,B             
7695: BF         CP      A               
7696: 00         NOP                     
7697: FE C1      CP      $C1             
7699: 3C         INC     A               
769A: C1         POP     BC              
769B: 3C         INC     A               
769C: C0         RET     NZ              
769D: 3E E0      LD      A,$E0           
769F: 1F         RRA                     
76A0: 3F         CCF                     
76A1: C0         RET     NZ              
76A2: 3F         CCF                     
76A3: C0         RET     NZ              
76A4: 1F         RRA                     
76A5: E0 1F      LDFF00  ($1F),A         
76A7: 60         LD      H,B             
76A8: 8F         ADC     A,A             
76A9: 30 8F      JR      NC,$763A        
76AB: 30 07      JR      NC,$76B4        
76AD: 78         LD      A,B             
76AE: 03         INC     BC              
76AF: FC         ???                     
76B0: 61         LD      H,C             
76B1: FE 00      CP      $00             
76B3: FF         RST     0X38            
76B4: 18 E7      JR      $769D           
76B6: 0E F1      LD      C,$F1           
76B8: 0F         RRCA                    
76B9: F0 1F      LD      A,($1F)         
76BB: E0 3F      LDFF00  ($3F),A         
76BD: C0         RET     NZ              
76BE: 9F         SBC     A               
76BF: E0 F3      LDFF00  ($F3),A         
76C1: 0C         INC     C               
76C2: CF         RST     0X08            
76C3: 30 3A      JR      NC,$76FF        
76C5: C5         PUSH    BC              
76C6: 80         ADD     A,B             
76C7: FF         RST     0X38            
76C8: 02         LD      (BC),A          
76C9: FD         ???                     
76CA: 74         LD      (HL),H          
76CB: 8B         ADC     A,E             
76CC: 77         LD      (HL),A          
76CD: 80         ADD     A,B             
76CE: CF         RST     0X08            
76CF: 00         NOP                     
76D0: FC         ???                     
76D1: 03         INC     BC              
76D2: 87         ADD     A,A             
76D3: 78         LD      A,B             
76D4: 01 FE 78   LD      BC,$78FE        
76D7: 87         ADD     A,A             
76D8: 8E         ADC     A,(HL)          
76D9: 71         LD      (HL),C          
76DA: 01 FE 00   LD      BC,$00FE        
76DD: FF         RST     0X38            
76DE: FC         ???                     
76DF: 03         INC     BC              
76E0: 00         NOP                     
76E1: FF         RST     0X38            
76E2: 00         NOP                     
76E3: FF         RST     0X38            
76E4: 84         ADD     A,H             
76E5: 7F         LD      A,A             
76E6: E2         LDFF00  (C),A           
76E7: 1D         DEC     E               
76E8: 7A         LD      A,D             
76E9: 8C         ADC     A,H             
76EA: 15         DEC     D               
76EB: E8 00      ADD     SP,$00          
76ED: FF         RST     0X38            
76EE: 00         NOP                     
76EF: FF         RST     0X38            
76F0: 0C         INC     C               
76F1: F3         DI                      
76F2: 00         NOP                     
76F3: FF         RST     0X38            
76F4: 07         RLCA                    
76F5: F8 7F      LDHL    SP,$7F          
76F7: 80         ADD     A,B             
76F8: F0 0F      LD      A,($0F)         
76FA: 80         ADD     A,B             
76FB: 7F         LD      A,A             
76FC: 00         NOP                     
76FD: FF         RST     0X38            
76FE: FF         RST     0X38            
76FF: 00         NOP                     
7700: 70         LD      (HL),B          
7701: 8F         ADC     A,A             
7702: 0E F1      LD      C,$F1           
7704: 83         ADD     A,E             
7705: 7C         LD      A,H             
7706: E1         POP     HL              
7707: 1E 38      LD      E,$38           
7709: C7         RST     0X00            
770A: 0E F1      LD      C,$F1           
770C: 00         NOP                     
770D: FF         RST     0X38            
770E: 00         NOP                     
770F: FF         RST     0X38            
7710: 36 C9      LD      (HL),$C9        
7712: BC         CP      H               
7713: 43         LD      B,E             
7714: 38 C7      JR      C,$76DD         
7716: 30 CF      JR      NC,$76E7        
7718: 31 CE 33   LD      SP,$33CE        
771B: CC 7F 80   CALL    Z,$807F         
771E: FF         RST     0X38            
771F: 00         NOP                     
7720: 1E E1      LD      E,$E1           
7722: 33         INC     SP              
7723: CC 63 9C   CALL    Z,$9C63         
7726: CF         RST     0X08            
7727: 30 BF      JR      NC,$76E8        
7729: 40         LD      B,B             
772A: FF         RST     0X38            
772B: 00         NOP                     
772C: FF         RST     0X38            
772D: 00         NOP                     
772E: FF         RST     0X38            
772F: 00         NOP                     
7730: E0 1F      LDFF00  ($1F),A         
7732: E0 1F      LDFF00  ($1F),A         
7734: E0 1F      LDFF00  ($1F),A         
7736: F0 0F      LD      A,($0F)         
7738: F0 0F      LD      A,($0F)         
773A: F8 07      LDHL    SP,$07          
773C: F4         ???                     
773D: 0B         DEC     BC              
773E: FE 01      CP      $01             
7740: 01 FE 01   LD      BC,$01FE        
7743: EE 00      XOR     $00             
7745: D7         RST     0X10            
7746: 00         NOP                     
7747: EF         RST     0X28            
7748: 80         ADD     A,B             
7749: 7F         LD      A,A             
774A: 80         ADD     A,B             
774B: 7B         LD      A,E             
774C: C0         RET     NZ              
774D: 35         DEC     (HL)            
774E: C0         RET     NZ              
774F: 3B         DEC     SP              
7750: FF         RST     0X38            
7751: 00         NOP                     
7752: FF         RST     0X38            
7753: 00         NOP                     
7754: FF         RST     0X38            
7755: 00         NOP                     
7756: 3F         CCF                     
7757: C0         RET     NZ              
7758: 00         NOP                     
7759: FF         RST     0X38            
775A: 40         LD      B,B             
775B: FF         RST     0X38            
775C: 20 DF      JR      NZ,$773D        
775E: 00         NOP                     
775F: 7B         LD      A,E             
7760: FF         RST     0X38            
7761: 00         NOP                     
7762: FF         RST     0X38            
7763: 00         NOP                     
7764: FF         RST     0X38            
7765: 00         NOP                     
7766: FF         RST     0X38            
7767: 00         NOP                     
7768: 7F         LD      A,A             
7769: 80         ADD     A,B             
776A: 3F         CCF                     
776B: C0         RET     NZ              
776C: 1F         RRA                     
776D: E0 0F      LDFF00  ($0F),A         
776F: B0         OR      B               
7770: 80         ADD     A,B             
7771: 7F         LD      A,A             
7772: C3 3F E3   JP      $E33F           
7775: 0F         RRCA                    
7776: FF         RST     0X38            
7777: 03         INC     BC              
7778: F9         LD      SP,HL           
7779: 07         RLCA                    
777A: F1         POP     AF              
777B: 0F         RRCA                    
777C: F0 0F      LD      A,($0F)         
777E: F9         LD      SP,HL           
777F: 07         RLCA                    
7780: 77         LD      (HL),A          
7781: FF         RST     0X38            
7782: FF         RST     0X38            
7783: FF         RST     0X38            
7784: F3         DI                      
7785: FF         RST     0X38            
7786: 3B         DEC     SP              
7787: FF         RST     0X38            
7788: 5F         LD      E,A             
7789: BF         CP      A               
778A: 67         LD      H,A             
778B: FF         RST     0X38            
778C: C3 FF 1B   JP      $1BFF           
778F: E7         RST     0X20            
7790: E8 FF      ADD     SP,$FF          
7792: F4         ???                     
7793: FF         RST     0X38            
7794: EC         ???                     
7795: FF         RST     0X38            
7796: F4         ???                     
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
77A1: 00         NOP                     
77A2: FF         RST     0X38            
77A3: 00         NOP                     
77A4: C3 3C 00   JP      $003C           
77A7: FF         RST     0X38            
77A8: 3C         INC     A               
77A9: FF         RST     0X38            
77AA: FF         RST     0X38            
77AB: FF         RST     0X38            
77AC: FF         RST     0X38            
77AD: FF         RST     0X38            
77AE: FF         RST     0X38            
77AF: FF         RST     0X38            
77B0: FF         RST     0X38            
77B1: 00         NOP                     
77B2: FF         RST     0X38            
77B3: 00         NOP                     
77B4: FF         RST     0X38            
77B5: 00         NOP                     
77B6: F1         POP     AF              
77B7: 0E 00      LD      C,$00           
77B9: FF         RST     0X38            
77BA: 0E FF      LD      C,$FF           
77BC: FF         RST     0X38            
77BD: FF         RST     0X38            
77BE: FF         RST     0X38            
77BF: FF         RST     0X38            
77C0: E0 1E      LDFF00  ($1E),A         
77C2: F0 0F      LD      A,($0F)         
77C4: F8 07      LDHL    SP,$07          
77C6: FE 01      CP      $01             
77C8: 00         NOP                     
77C9: FF         RST     0X38            
77CA: 00         NOP                     
77CB: FF         RST     0X38            
77CC: FF         RST     0X38            
77CD: FF         RST     0X38            
77CE: FF         RST     0X38            
77CF: FF         RST     0X38            
77D0: 00         NOP                     
77D1: B5         OR      L               
77D2: 00         NOP                     
77D3: 7B         LD      A,E             
77D4: 00         NOP                     
77D5: FF         RST     0X38            
77D6: 00         NOP                     
77D7: FF         RST     0X38            
77D8: 3F         CCF                     
77D9: FF         RST     0X38            
77DA: 01 FF FF   LD      BC,$FFFF        
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
77F0: FD         ???                     
77F1: 03         INC     BC              
77F2: FD         ???                     
77F3: 03         INC     BC              
77F4: F9         LD      SP,HL           
77F5: 07         RLCA                    
77F6: F3         DI                      
77F7: 0F         RRCA                    
77F8: 07         RLCA                    
77F9: FE 1E      CP      $1E             
77FB: FF         RST     0X38            
77FC: FF         RST     0X38            
77FD: FF         RST     0X38            
77FE: FF         RST     0X38            
77FF: FF         RST     0X38            
7800: 7F         LD      A,A             
7801: FF         RST     0X38            
7802: FF         RST     0X38            
7803: C0         RET     NZ              
7804: E0 80      LDFF00  ($80),A         
7806: C1         POP     BC              
7807: 80         ADD     A,B             
7808: C3 80 E7   JP      $E780           
780B: 80         ADD     A,B             
780C: CF         RST     0X08            
780D: 80         ADD     A,B             
780E: C0         RET     NZ              
780F: 80         ADD     A,B             
7810: FF         RST     0X38            
7811: FF         RST     0X38            
7812: FF         RST     0X38            
7813: 00         NOP                     
7814: 08 20 B0   LD      ($B020),SP      
7817: 00         NOP                     
7818: E0 04      LDFF00  ($04),A         
781A: C0         RET     NZ              
781B: 00         NOP                     
781C: 00         NOP                     
781D: 00         NOP                     
781E: 01 00 FF   LD      BC,$FF00        
7821: FF         RST     0X38            
7822: FF         RST     0X38            
7823: 00         NOP                     
7824: 00         NOP                     
7825: 00         NOP                     
7826: 80         ADD     A,B             
7827: 80         ADD     A,B             
7828: 00         NOP                     
7829: 00         NOP                     
782A: 00         NOP                     
782B: 00         NOP                     
782C: C0         RET     NZ              
782D: 00         NOP                     
782E: 80         ADD     A,B             
782F: 00         NOP                     
7830: FF         RST     0X38            
7831: FF         RST     0X38            
7832: FF         RST     0X38            
7833: 00         NOP                     
7834: 00         NOP                     
7835: 00         NOP                     
7836: 00         NOP                     
7837: 00         NOP                     
7838: 00         NOP                     
7839: 00         NOP                     
783A: 00         NOP                     
783B: 00         NOP                     
783C: 00         NOP                     
783D: 00         NOP                     
783E: 00         NOP                     
783F: 00         NOP                     
7840: 3F         CCF                     
7841: FF         RST     0X38            
7842: 3F         CCF                     
7843: FF         RST     0X38            
7844: 37         SCF                     
7845: F3         DI                      
7846: 3F         CCF                     
7847: F3         DI                      
7848: 2D         DEC     L               
7849: FF         RST     0X38            
784A: 38 E7      JR      C,$7833         
784C: 3A         LD      A,(HLD)         
784D: E7         RST     0X20            
784E: 38 E7      JR      C,$7837         
7850: 80         ADD     A,B             
7851: FF         RST     0X38            
7852: 80         ADD     A,B             
7853: FF         RST     0X38            
7854: 80         ADD     A,B             
7855: FF         RST     0X38            
7856: 80         ADD     A,B             
7857: FF         RST     0X38            
7858: 80         ADD     A,B             
7859: FF         RST     0X38            
785A: 80         ADD     A,B             
785B: FF         RST     0X38            
785C: 80         ADD     A,B             
785D: FF         RST     0X38            
785E: 80         ADD     A,B             
785F: FF         RST     0X38            
7860: 01 FF 01   LD      BC,$01FF        
7863: FF         RST     0X38            
7864: 01 FF 01   LD      BC,$01FF        
7867: FF         RST     0X38            
7868: 01 FF 01   LD      BC,$01FF        
786B: FF         RST     0X38            
786C: 01 FF 01   LD      BC,$01FF        
786F: FF         RST     0X38            
7870: FC         ???                     
7871: FF         RST     0X38            
7872: DC CF FC   CALL    C,$FCCF         
7875: CF         RST     0X08            
7876: 34         INC     (HL)            
7877: FF         RST     0X38            
7878: 0C         INC     C               
7879: FF         RST     0X38            
787A: AC         XOR     H               
787B: 7F         LD      A,A             
787C: 8C         ADC     A,H             
787D: 7F         LD      A,A             
787E: 8C         ADC     A,H             
787F: 7F         LD      A,A             
7880: FF         RST     0X38            
7881: FF         RST     0X38            
7882: FF         RST     0X38            
7883: 00         NOP                     
7884: 00         NOP                     
7885: 00         NOP                     
7886: 00         NOP                     
7887: 00         NOP                     
7888: 03         INC     BC              
7889: 03         INC     BC              
788A: 0F         RRCA                    
788B: 0F         RRCA                    
788C: 3E 3F      LD      A,$3F           
788E: FF         RST     0X38            
788F: FB         EI                      
7890: FE FF      CP      $FF             
7892: EF         RST     0X28            
7893: 13         INC     DE              
7894: 03         INC     BC              
7895: 05         DEC     B               
7896: 47         LD      B,A             
7897: 7B         LD      A,E             
7898: CF         RST     0X08            
7899: FD         ???                     
789A: FF         RST     0X38            
789B: FF         RST     0X38            
789C: FF         RST     0X38            
789D: F1         POP     AF              
789E: FF         RST     0X38            
789F: F1         POP     AF              
78A0: D0         RET     NC              
78A1: 9F         SBC     A               
78A2: D0         RET     NC              
78A3: BF         CP      A               
78A4: F8 BF      LDHL    SP,$BF          
78A6: FC         ???                     
78A7: BF         CP      A               
78A8: FD         ???                     
78A9: BB         CP      E               
78AA: FF         RST     0X38            
78AB: B6         OR      (HL)            
78AC: FE BC      CP      $BC             
78AE: FE BD      CP      $BD             
78B0: 0C         INC     C               
78B1: FF         RST     0X38            
78B2: 1C         INC     E               
78B3: FF         RST     0X38            
78B4: 38 FF      JR      C,$78B5         
78B6: 70         LD      (HL),B          
78B7: FF         RST     0X38            
78B8: F0 FF      LD      A,($FF)         
78BA: D8         RET     C               
78BB: E7         RST     0X20            
78BC: 08 CF 18   LD      ($18CF),SP      
78BF: 1F         RRA                     
78C0: 1F         RRA                     
78C1: F6 0F      OR      $0F             
78C3: FF         RST     0X38            
78C4: 1F         RRA                     
78C5: FF         RST     0X38            
78C6: 3F         CCF                     
78C7: FE 3F      CP      $3F             
78C9: FF         RST     0X38            
78CA: 5F         LD      E,A             
78CB: DF         RST     0X18            
78CC: 37         SCF                     
78CD: B7         OR      A               
78CE: 0F         RRCA                    
78CF: 0F         RRCA                    
78D0: 88         ADC     A,B             
78D1: E0 00      LDFF00  ($00),A         
78D3: F8 05      LDHL    SP,$05          
78D5: FD         ???                     
78D6: 9E         SBC     (HL)            
78D7: FF         RST     0X38            
78D8: 3E FF      LD      A,$FF           
78DA: FD         ???                     
78DB: FF         RST     0X38            
78DC: FF         RST     0X38            
78DD: FE FF      CP      $FF             
78DF: FE 01      CP      $01             
78E1: 00         NOP                     
78E2: 43         LD      B,E             
78E3: 00         NOP                     
78E4: 41         LD      B,C             
78E5: 02         LD      (BC),A          
78E6: 00         NOP                     
78E7: E7         RST     0X20            
78E8: 80         ADD     A,B             
78E9: 7F         LD      A,A             
78EA: 80         ADD     A,B             
78EB: 7F         LD      A,A             
78EC: 01 FE 00   LD      BC,$00FE        
78EF: FF         RST     0X38            
78F0: 14         INC     D               
78F1: EB         ???                     
78F2: 08 05 10   LD      ($1005),SP      
78F5: 0F         RRCA                    
78F6: 00         NOP                     
78F7: 3F         CCF                     
78F8: 65         LD      H,L             
78F9: 9B         SBC     E               
78FA: FF         RST     0X38            
78FB: 0F         RRCA                    
78FC: FF         RST     0X38            
78FD: 17         RLA                     
78FE: 80         ADD     A,B             
78FF: 7F         LD      A,A             
7900: C0         RET     NZ              
7901: 80         ADD     A,B             
7902: C0         RET     NZ              
7903: 80         ADD     A,B             
7904: C0         RET     NZ              
7905: 80         ADD     A,B             
7906: C0         RET     NZ              
7907: 80         ADD     A,B             
7908: C0         RET     NZ              
7909: 80         ADD     A,B             
790A: C0         RET     NZ              
790B: 80         ADD     A,B             
790C: C0         RET     NZ              
790D: 80         ADD     A,B             
790E: C0         RET     NZ              
790F: 80         ADD     A,B             
7910: 03         INC     BC              
7911: 00         NOP                     
7912: 0E 00      LD      C,$00           
7914: 1C         INC     E               
7915: 00         NOP                     
7916: 78         LD      A,B             
7917: 00         NOP                     
7918: F0 00      LD      A,($00)         
791A: 01 00 01   LD      BC,$0100        
791D: 00         NOP                     
791E: 03         INC     BC              
791F: 00         NOP                     
7920: 05         DEC     B               
7921: 00         NOP                     
7922: 06 00      LD      B,$00           
7924: 08 00 31   LD      ($3100),SP      
7927: 01 C7 07   LD      BC,$07C7        
792A: 27         DAA                     
792B: 07         RLCA                    
792C: FF         RST     0X38            
792D: 0F         RRCA                    
792E: EE 0D      XOR     $0D             
7930: 00         NOP                     
7931: 00         NOP                     
7932: 1F         RRA                     
7933: 00         NOP                     
7934: 3F         CCF                     
7935: 01 9F 9F   LD      BC,$9F9F        
7938: FE FE      CP      $FE             
793A: FF         RST     0X38            
793B: FF         RST     0X38            
793C: FF         RST     0X38            
793D: FF         RST     0X38            
793E: 7E         LD      A,(HL)          
793F: FE 0C      CP      $0C             
7941: 0C         INC     C               
7942: FF         RST     0X38            
7943: FF         RST     0X38            
7944: F9         LD      SP,HL           
7945: FF         RST     0X38            
7946: FB         EI                      
7947: CF         RST     0X08            
7948: FF         RST     0X38            
7949: 8F         ADC     A,A             
794A: A7         AND     A               
794B: 07         RLCA                    
794C: 08 06 00   LD      ($0006),SP      
794F: 0F         RRCA                    
7950: E0 F8      LDFF00  ($F8),A         
7952: C6 F7      ADD     $F7             
7954: CD FF FF   CALL    $FFFF           
7957: FF         RST     0X38            
7958: FE FF      CP      $FF             
795A: FC         ???                     
795B: FF         RST     0X38            
795C: FF         RST     0X38            
795D: 78         LD      A,B             
795E: 7F         LD      A,A             
795F: 80         ADD     A,B             
7960: 00         NOP                     
7961: 00         NOP                     
7962: 00         NOP                     
7963: C0         RET     NZ              
7964: B8         CP      B               
7965: F8 FF      LDHL    SP,$FF          
7967: FD         ???                     
7968: 0B         DEC     BC              
7969: 89         ADC     A,C             
796A: 81         ADD     A,C             
796B: 41         LD      B,C             
796C: 01 01 01   LD      BC,$0101        
796F: 01 03 03   LD      BC,$0303        
7972: 07         RLCA                    
7973: 07         RLCA                    
7974: 0F         RRCA                    
7975: 0F         RRCA                    
7976: 1F         RRA                     
7977: 1F         RRA                     
7978: FF         RST     0X38            
7979: FF         RST     0X38            
797A: FC         ???                     
797B: FF         RST     0X38            
797C: C0         RET     NZ              
797D: FF         RST     0X38            
797E: 60         LD      H,B             
797F: EF         RST     0X28            
7980: FF         RST     0X38            
7981: FD         ???                     
7982: F9         LD      SP,HL           
7983: FF         RST     0X38            
7984: F0 FF      LD      A,($FF)         
7986: 80         ADD     A,B             
7987: FF         RST     0X38            
7988: 32         LD      (HLD),A         
7989: EF         RST     0X28            
798A: 0F         RRCA                    
798B: FF         RST     0X38            
798C: 3F         CCF                     
798D: FE 7F      CP      $7F             
798F: FF         RST     0X38            
7990: FF         RST     0X38            
7991: E1         POP     HL              
7992: EF         RST     0X28            
7993: F1         POP     AF              
7994: FB         EI                      
7995: CF         RST     0X08            
7996: FE 8D      CP      $8D             
7998: 5D         LD      E,L             
7999: A7         AND     A               
799A: FB         EI                      
799B: 07         RLCA                    
799C: FF         RST     0X38            
799D: 0D         DEC     C               
799E: FD         ???                     
799F: 1F         RRA                     
79A0: FD         ???                     
79A1: BB         CP      E               
79A2: FE BF      CP      $BF             
79A4: FE BF      CP      $BF             
79A6: FE BD      CP      $BD             
79A8: DA 9F E4   JP      C,$E49F         
79AB: 9F         SBC     A               
79AC: EF         RST     0X28            
79AD: 9F         SBC     A               
79AE: FF         RST     0X38            
79AF: 9F         SBC     A               
79B0: 3C         INC     A               
79B1: BE         CP      (HL)            
79B2: 3C         INC     A               
79B3: FE 10      CP      $10             
79B5: FF         RST     0X38            
79B6: 00         NOP                     
79B7: FF         RST     0X38            
79B8: 00         NOP                     
79B9: FF         RST     0X38            
79BA: A0         AND     B               
79BB: DF         RST     0X18            
79BC: 78         LD      A,B             
79BD: AF         XOR     A               
79BE: F0 FF      LD      A,($FF)         
79C0: 07         RLCA                    
79C1: 0F         RRCA                    
79C2: 07         RLCA                    
79C3: 1F         RRA                     
79C4: 00         NOP                     
79C5: 3F         CCF                     
79C6: 20 DD      JR      NZ,$79A5        
79C8: 00         NOP                     
79C9: FB         EI                      
79CA: 00         NOP                     
79CB: F0 40      LD      A,($40)         
79CD: A0         AND     B               
79CE: E0 01      LDFF00  ($01),A         
79D0: FF         RST     0X38            
79D1: FC         ???                     
79D2: FF         RST     0X38            
79D3: F8 1F      LDHL    SP,$1F          
79D5: FC         ???                     
79D6: 3F         CCF                     
79D7: DE 7E      SBC     $7E             
79D9: 2F         CPL                     
79DA: 3C         INC     A               
79DB: DF         RST     0X18            
79DC: 38 DF      JR      C,$79BD         
79DE: 72         LD      (HL),D          
79DF: BF         CP      A               
79E0: 00         NOP                     
79E1: FF         RST     0X38            
79E2: 80         ADD     A,B             
79E3: 7F         LD      A,A             
79E4: C4 3B 9C   CALL    NZ,$9C3B        
79E7: 63         LD      H,E             
79E8: 0E F1      LD      C,$F1           
79EA: 3F         CCF                     
79EB: C1         POP     BC              
79EC: 7E         LD      A,(HL)          
79ED: 81         ADD     A,C             
79EE: 4D         LD      C,L             
79EF: 92         SUB     D               
79F0: 00         NOP                     
79F1: FF         RST     0X38            
79F2: 00         NOP                     
79F3: FF         RST     0X38            
79F4: 00         NOP                     
79F5: FF         RST     0X38            
79F6: 00         NOP                     
79F7: FF         RST     0X38            
79F8: 01 FE 03   LD      BC,$03FE        
79FB: FC         ???                     
79FC: CF         RST     0X08            
79FD: D0         RET     NC              
79FE: E5         PUSH    HL              
79FF: 00         NOP                     
7A00: C0         RET     NZ              
7A01: 80         ADD     A,B             
7A02: C0         RET     NZ              
7A03: 80         ADD     A,B             
7A04: C1         POP     BC              
7A05: 81         ADD     A,C             
7A06: C2 82 C2   JP      NZ,$C282        
7A09: 82         ADD     A,D             
7A0A: C4 84 C4   CALL    NZ,$C484        
7A0D: 84         ADD     A,H             
7A0E: C0         RET     NZ              
7A0F: 80         ADD     A,B             
7A10: 07         RLCA                    
7A11: 00         NOP                     
7A12: 03         INC     BC              
7A13: 00         NOP                     
7A14: 07         RLCA                    
7A15: 01 0F 01   LD      BC,$010F        
7A18: 1F         RRA                     
7A19: 03         INC     BC              
7A1A: 0F         RRCA                    
7A1B: 07         RLCA                    
7A1C: 0F         RRCA                    
7A1D: 0F         RRCA                    
7A1E: 0F         RRCA                    
7A1F: 0F         RRCA                    
7A20: FC         ???                     
7A21: 1B         DEC     DE              
7A22: FC         ???                     
7A23: 73         LD      (HL),E          
7A24: E0 FC      LDFF00  ($FC),A         
7A26: E0 C8      LDFF00  ($C8),A         
7A28: C0         RET     NZ              
7A29: D0         RET     NC              
7A2A: 80         ADD     A,B             
7A2B: 80         ADD     A,B             
7A2C: 00         NOP                     
7A2D: 80         ADD     A,B             
7A2E: 80         ADD     A,B             
7A2F: 81         ADD     A,C             
7A30: 7C         LD      A,H             
7A31: BC         CP      H               
7A32: BC         CP      H               
7A33: 02         LD      (BC),A          
7A34: 58         LD      E,B             
7A35: 07         RLCA                    
7A36: 10 0F      STOP    $0F             
7A38: 00         NOP                     
7A39: 3F         CCF                     
7A3A: 0F         RRCA                    
7A3B: 7F         LD      A,A             
7A3C: 97         SUB     A               
7A3D: 7F         LD      A,A             
7A3E: 3D         DEC     A               
7A3F: FD         ???                     
7A40: 00         NOP                     
7A41: 1F         RRA                     
7A42: 00         NOP                     
7A43: 3F         CCF                     
7A44: 1E ED      LD      E,$ED           
7A46: 3F         CCF                     
7A47: FF         RST     0X38            
7A48: F0 FF      LD      A,($FF)         
7A4A: EF         RST     0X28            
7A4B: FF         RST     0X38            
7A4C: B7         OR      A               
7A4D: FF         RST     0X38            
7A4E: 3F         CCF                     
7A4F: FF         RST     0X38            
7A50: 87         ADD     A,A             
7A51: 78         LD      A,B             
7A52: 01 FE 00   LD      BC,$00FE        
7A55: FF         RST     0X38            
7A56: C4 FF DE   CALL    NZ,$DEFF        
7A59: FF         RST     0X38            
7A5A: FE FF      CP      $FF             
7A5C: FF         RST     0X38            
7A5D: FF         RST     0X38            
7A5E: FF         RST     0X38            
7A5F: FF         RST     0X38            
7A60: 00         NOP                     
7A61: 00         NOP                     
7A62: 00         NOP                     
7A63: 00         NOP                     
7A64: 1C         INC     E               
7A65: E0 0C      LDFF00  ($0C),A         
7A67: F0 06      LD      A,($06)         
7A69: F8 03      LDHL    SP,$03          
7A6B: FC         ???                     
7A6C: 8A         ADC     A,D             
7A6D: FC         ???                     
7A6E: FE FC      CP      $FC             
7A70: E8 EF      ADD     SP,$EF          
7A72: 38 3F      JR      C,$7AB3         
7A74: 3C         INC     A               
7A75: 3F         CCF                     
7A76: 3E 3F      LD      A,$3F           
7A78: 3F         CCF                     
7A79: 3F         CCF                     
7A7A: 1F         RRA                     
7A7B: 1F         RRA                     
7A7C: 07         RLCA                    
7A7D: 07         RLCA                    
7A7E: 01 03 1F   LD      BC,$1F03        
7A81: FF         RST     0X38            
7A82: 07         RLCA                    
7A83: FF         RST     0X38            
7A84: 06 FF      LD      B,$FF           
7A86: 0E FF      LD      C,$FF           
7A88: FE FF      CP      $FF             
7A8A: 7F         LD      A,A             
7A8B: 7F         LD      A,A             
7A8C: DF         RST     0X18            
7A8D: DC FF F0   CALL    C,$F0FF         
7A90: C3 3D 01   JP      $013D           
7A93: FF         RST     0X38            
7A94: 03         INC     BC              
7A95: FD         ???                     
7A96: 01 FF 03   LD      BC,$03FF        
7A99: FD         ???                     
7A9A: 07         RLCA                    
7A9B: F9         LD      SP,HL           
7A9C: 87         ADD     A,A             
7A9D: F1         POP     AF              
7A9E: E3         ???                     
7A9F: FD         ???                     
7AA0: DF         RST     0X18            
7AA1: 9F         SBC     A               
7AA2: CF         RST     0X08            
7AA3: 8F         ADC     A,A             
7AA4: C3 83 C7   JP      $C783           
7AA7: 8F         ADC     A,A             
7AA8: C7         RST     0X00            
7AA9: BF         CP      A               
7AAA: C3 BF C0   JP      $C0BF           
7AAD: BF         CP      A               
7AAE: C0         RET     NZ              
7AAF: BF         CP      A               
7AB0: F0 FF      LD      A,($FF)         
7AB2: E9         JP      (HL)            
7AB3: FF         RST     0X38            
7AB4: F0 FF      LD      A,($FF)         
7AB6: F1         POP     AF              
7AB7: FF         RST     0X38            
7AB8: E3         ???                     
7AB9: FF         RST     0X38            
7ABA: C7         RST     0X00            
7ABB: FF         RST     0X38            
7ABC: 07         RLCA                    
7ABD: FF         RST     0X38            
7ABE: EF         RST     0X28            
7ABF: 33         INC     SP              
7AC0: C0         RET     NZ              
7AC1: 13         INC     DE              
7AC2: 80         ADD     A,B             
7AC3: 87         ADD     A,A             
7AC4: 00         NOP                     
7AC5: 07         RLCA                    
7AC6: 00         NOP                     
7AC7: 0F         RRCA                    
7AC8: 80         ADD     A,B             
7AC9: 9B         SBC     E               
7ACA: E0 D6      LDFF00  ($D6),A         
7ACC: E0 81      LDFF00  ($81),A         
7ACE: 00         NOP                     
7ACF: C1         POP     BC              
7AD0: 3C         INC     A               
7AD1: FE 6D      CP      $6D             
7AD3: EC         ???                     
7AD4: 18 D8      JR      $7AAE           
7AD6: 00         NOP                     
7AD7: 80         ADD     A,B             
7AD8: 00         NOP                     
7AD9: 00         NOP                     
7ADA: 09         ADD     HL,BC           
7ADB: 00         NOP                     
7ADC: 1E 80      LD      E,$80           
7ADE: 3E C0      LD      A,$C0           
7AE0: A3         AND     E               
7AE1: 14         INC     D               
7AE2: 05         DEC     B               
7AE3: 0E 0B      LD      C,$0B           
7AE5: 0D         DEC     C               
7AE6: 1F         RRA                     
7AE7: 1E 35      LD      E,$35           
7AE9: 36 03      LD      (HL),$03        
7AEB: 0C         INC     C               
7AEC: 01 0E 03   LD      BC,$030E        
7AEF: 1C         INC     E               
7AF0: FB         EI                      
7AF1: 18 F0      JR      $7AE3           
7AF3: 70         LD      (HL),B          
7AF4: E0 00      LDFF00  ($00),A         
7AF6: E1         POP     HL              
7AF7: 00         NOP                     
7AF8: F3         DI                      
7AF9: 00         NOP                     
7AFA: FC         ???                     
7AFB: 03         INC     BC              
7AFC: F8 07      LDHL    SP,$07          
7AFE: F8 07      LDHL    SP,$07          
7B00: 5D         LD      E,L             
7B01: CB 5D      SET     1,E             
7B03: DF         RST     0X18            
7B04: 5D         LD      E,L             
7B05: CB 5D      SET     1,E             
7B07: C3 5D C3   JP      $C35D           
7B0A: 55         LD      D,L             
7B0B: CB 5D      SET     1,E             
7B0D: C3 4D D3   JP      $D34D           
7B10: 0F         RRCA                    
7B11: 0F         RRCA                    
7B12: 1F         RRA                     
7B13: 1F         RRA                     
7B14: 0F         RRCA                    
7B15: 0F         RRCA                    
7B16: 3F         CCF                     
7B17: 3F         CCF                     
7B18: 3E 3E      LD      A,$3E           
7B1A: 35         DEC     (HL)            
7B1B: 34         INC     (HL)            
7B1C: 60         LD      H,B             
7B1D: 60         LD      H,B             
7B1E: 61         LD      H,C             
7B1F: 60         LD      H,B             
7B20: C2 C1 80   JP      NZ,$80C1        
7B23: 87         ADD     A,A             
7B24: F1         POP     AF              
7B25: 0F         RRCA                    
7B26: E3         ???                     
7B27: 1F         RRA                     
7B28: EF         RST     0X28            
7B29: 1F         RRA                     
7B2A: DF         RST     0X18            
7B2B: 3F         CCF                     
7B2C: 9F         SBC     A               
7B2D: 1F         RRA                     
7B2E: 3F         CCF                     
7B2F: 3F         CCF                     
7B30: 72         LD      (HL),D          
7B31: F3         DI                      
7B32: E6 FF      AND     $FF             
7B34: DC FF 9F   CALL    C,$9FFF         
7B37: FF         RST     0X38            
7B38: BE         CP      (HL)            
7B39: FF         RST     0X38            
7B3A: FF         RST     0X38            
7B3B: FC         ???                     
7B3C: FF         RST     0X38            
7B3D: FC         ???                     
7B3E: FF         RST     0X38            
7B3F: FB         EI                      
7B40: 0F         RRCA                    
7B41: FF         RST     0X38            
7B42: 1F         RRA                     
7B43: FF         RST     0X38            
7B44: 3F         CCF                     
7B45: FF         RST     0X38            
7B46: 5E         LD      E,(HL)          
7B47: DF         RST     0X18            
7B48: FE FF      CP      $FF             
7B4A: FF         RST     0X38            
7B4B: FF         RST     0X38            
7B4C: FF         RST     0X38            
7B4D: FF         RST     0X38            
7B4E: FF         RST     0X38            
7B4F: FF         RST     0X38            
7B50: FF         RST     0X38            
7B51: FF         RST     0X38            
7B52: 7F         LD      A,A             
7B53: FF         RST     0X38            
7B54: 7F         LD      A,A             
7B55: FF         RST     0X38            
7B56: 7F         LD      A,A             
7B57: 8F         ADC     A,A             
7B58: FF         RST     0X38            
7B59: FF         RST     0X38            
7B5A: FF         RST     0X38            
7B5B: EF         RST     0X28            
7B5C: FF         RST     0X38            
7B5D: FF         RST     0X38            
7B5E: FF         RST     0X38            
7B5F: FF         RST     0X38            
7B60: FE FC      CP      $FC             
7B62: FC         ???                     
7B63: FF         RST     0X38            
7B64: FE FF      CP      $FF             
7B66: FE FF      CP      $FF             
7B68: FF         RST     0X38            
7B69: FF         RST     0X38            
7B6A: FF         RST     0X38            
7B6B: FF         RST     0X38            
7B6C: CF         RST     0X08            
7B6D: CF         RST     0X08            
7B6E: 3F         CCF                     
7B6F: FF         RST     0X38            
7B70: 1D         DEC     E               
7B71: 03         INC     BC              
7B72: 3E D1      LD      A,$D1           
7B74: 7E         LD      A,(HL)          
7B75: F9         LD      SP,HL           
7B76: FD         ???                     
7B77: FA F4 FA   LD      A,($FAF4)       
7B7A: F8 FE      LDHL    SP,$FE          
7B7C: F8 FE      LDHL    SP,$FE          
7B7E: FC         ???                     
7B7F: F2         ???                     
7B80: FF         RST     0X38            
7B81: E0 FF      LDFF00  ($FF),A         
7B83: E0 FF      LDFF00  ($FF),A         
7B85: 60         LD      H,B             
7B86: 30 AF      JR      NC,$7B37        
7B88: 00         NOP                     
7B89: 1F         RRA                     
7B8A: 00         NOP                     
7B8B: 1F         RRA                     
7B8C: 00         NOP                     
7B8D: 1F         RRA                     
7B8E: 00         NOP                     
7B8F: 0F         RRCA                    
7B90: E3         ???                     
7B91: 1D         DEC     E               
7B92: 87         ADD     A,A             
7B93: 79         LD      A,C             
7B94: 07         RLCA                    
7B95: F5         PUSH    AF              
7B96: 0F         RRCA                    
7B97: F9         LD      SP,HL           
7B98: 1F         RRA                     
7B99: FF         RST     0X38            
7B9A: 1F         RRA                     
7B9B: FF         RST     0X38            
7B9C: 3F         CCF                     
7B9D: FD         ???                     
7B9E: 7B         LD      A,E             
7B9F: 9D         SBC     L               
7BA0: C1         POP     BC              
7BA1: BE         CP      (HL)            
7BA2: E3         ???                     
7BA3: BC         CP      H               
7BA4: DB         ???                     
7BA5: 99         SBC     C               
7BA6: C1         POP     BC              
7BA7: 81         ADD     A,C             
7BA8: C0         RET     NZ              
7BA9: 80         ADD     A,B             
7BAA: E3         ???                     
7BAB: 9C         SBC     H               
7BAC: FF         RST     0X38            
7BAD: C0         RET     NZ              
7BAE: 7F         LD      A,A             
7BAF: FF         RST     0X38            
7BB0: C8         RET     Z               
7BB1: 4B         LD      C,E             
7BB2: F0 F7      LD      A,($F7)         
7BB4: F0 F7      LD      A,($F7)         
7BB6: E0 E7      LDFF00  ($E7),A         
7BB8: C0         RET     NZ              
7BB9: C3 FE 03   JP      $03FE           
7BBC: FF         RST     0X38            
7BBD: 03         INC     BC              
7BBE: FF         RST     0X38            
7BBF: FF         RST     0X38            
7BC0: 00         NOP                     
7BC1: C3 00 E7   JP      $E700           
7BC4: 07         RLCA                    
7BC5: F8 0F      LDHL    SP,$0F          
7BC7: F0 0F      LD      A,($0F)         
7BC9: E0 3F      LDFF00  ($3F),A         
7BCB: E0 FF      LDFF00  ($FF),A         
7BCD: C0         RET     NZ              
7BCE: FF         RST     0X38            
7BCF: FF         RST     0X38            
7BD0: 0E F1      LD      C,$F1           
7BD2: 0E F9      LD      C,$F9           
7BD4: 07         RLCA                    
7BD5: F6 80      OR      $80             
7BD7: 60         LD      H,B             
7BD8: 80         ADD     A,B             
7BD9: 00         NOP                     
7BDA: E7         RST     0X20            
7BDB: 18 FF      JR      $7BDC           
7BDD: 00         NOP                     
7BDE: FF         RST     0X38            
7BDF: FF         RST     0X38            
7BE0: 01 3E 03   LD      BC,$033E        
7BE3: FC         ???                     
7BE4: 07         RLCA                    
7BE5: F8 03      LDHL    SP,$03          
7BE7: 70         LD      (HL),B          
7BE8: 03         INC     BC              
7BE9: 00         NOP                     
7BEA: 0F         RRCA                    
7BEB: F0 FF      LD      A,($FF)         
7BED: 00         NOP                     
7BEE: FF         RST     0X38            
7BEF: FF         RST     0X38            
7BF0: F8 07      LDHL    SP,$07          
7BF2: F8 03      LDHL    SP,$03          
7BF4: F2         ???                     
7BF5: 01 31 C0   LD      BC,$C031        
7BF8: E0 00      LDFF00  ($00),A         
7BFA: FF         RST     0X38            
7BFB: 00         NOP                     
7BFC: FF         RST     0X38            
7BFD: 00         NOP                     
7BFE: FF         RST     0X38            
7BFF: FF         RST     0X38            
7C00: BA         CP      D               
7C01: 97         SUB     A               
7C02: BA         CP      D               
7C03: BF         CP      A               
7C04: BA         CP      D               
7C05: 97         SUB     A               
7C06: BA         CP      D               
7C07: 87         ADD     A,A             
7C08: BA         CP      D               
7C09: C7         RST     0X00            
7C0A: B2         OR      D               
7C0B: 8F         ADC     A,A             
7C0C: BA         CP      D               
7C0D: 87         ADD     A,A             
7C0E: BA         CP      D               
7C0F: 87         ADD     A,A             
7C10: 61         LD      H,C             
7C11: 60         LD      H,B             
7C12: C3 F0 CF   JP      $CFF0           
7C15: FA EE FC   LD      A,($FCEE)       
7C18: 1C         INC     E               
7C19: FC         ???                     
7C1A: 3E FA      LD      A,$FA           
7C1C: 3C         INC     A               
7C1D: 7C         LD      A,H             
7C1E: 7F         LD      A,A             
7C1F: FC         ???                     
7C20: 3F         CCF                     
7C21: 3F         CCF                     
7C22: BF         CP      A               
7C23: 7F         LD      A,A             
7C24: 76         HALT                    
7C25: 37         SCF                     
7C26: 24         INC     H               
7C27: 27         DAA                     
7C28: 34         INC     (HL)            
7C29: 37         SCF                     
7C2A: 34         INC     (HL)            
7C2B: 37         SCF                     
7C2C: 3E 3F      LD      A,$3F           
7C2E: 9F         SBC     A               
7C2F: 1F         RRA                     
7C30: FF         RST     0X38            
7C31: FF         RST     0X38            
7C32: 3E FF      LD      A,$FF           
7C34: 1F         RRA                     
7C35: FF         RST     0X38            
7C36: 1F         RRA                     
7C37: FF         RST     0X38            
7C38: 3F         CCF                     
7C39: FF         RST     0X38            
7C3A: 7F         LD      A,A             
7C3B: FF         RST     0X38            
7C3C: FF         RST     0X38            
7C3D: FF         RST     0X38            
7C3E: FF         RST     0X38            
7C3F: FF         RST     0X38            
7C40: 0F         RRCA                    
7C41: FF         RST     0X38            
7C42: 67         LD      H,A             
7C43: FF         RST     0X38            
7C44: D3         ???                     
7C45: FF         RST     0X38            
7C46: F7         RST     0X30            
7C47: FF         RST     0X38            
7C48: FF         RST     0X38            
7C49: FF         RST     0X38            
7C4A: FF         RST     0X38            
7C4B: FF         RST     0X38            
7C4C: FF         RST     0X38            
7C4D: FF         RST     0X38            
7C4E: FF         RST     0X38            
7C4F: FF         RST     0X38            
7C50: FE FF      CP      $FF             
7C52: FF         RST     0X38            
7C53: FF         RST     0X38            
7C54: F9         LD      SP,HL           
7C55: FF         RST     0X38            
7C56: E9         JP      (HL)            
7C57: EF         RST     0X28            
7C58: F1         POP     AF              
7C59: FF         RST     0X38            
7C5A: F3         DI                      
7C5B: FF         RST     0X38            
7C5C: FF         RST     0X38            
7C5D: E7         RST     0X20            
7C5E: FF         RST     0X38            
7C5F: E7         RST     0X20            
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
7C6D: F5         PUSH    AF              
7C6E: FF         RST     0X38            
7C6F: DD         ???                     
7C70: FC         ???                     
7C71: E2         LDFF00  (C),A           
7C72: FD         ???                     
7C73: F2         ???                     
7C74: F9         LD      SP,HL           
7C75: FE FF      CP      $FF             
7C77: F8 FC      LDHL    SP,$FC          
7C79: F3         DI                      
7C7A: FE FB      CP      $FB             
7C7C: FC         ???                     
7C7D: FB         EI                      
7C7E: F9         LD      SP,HL           
7C7F: FE 18      CP      $18             
7C81: 1F         RRA                     
7C82: 1F         RRA                     
7C83: 1E 8F      LD      E,$8F           
7C85: 0C         INC     C               
7C86: 8F         ADC     A,A             
7C87: 00         NOP                     
7C88: 2F         CPL                     
7C89: C0         RET     NZ              
7C8A: 47         LD      B,A             
7C8B: 80         ADD     A,B             
7C8C: C7         RST     0X00            
7C8D: 00         NOP                     
7C8E: C7         RST     0X00            
7C8F: 00         NOP                     
7C90: FF         RST     0X38            
7C91: 1F         RRA                     
7C92: FF         RST     0X38            
7C93: 3F         CCF                     
7C94: FD         ???                     
7C95: 3F         CCF                     
7C96: DB         ???                     
7C97: 1D         DEC     E               
7C98: 9B         SBC     E               
7C99: 2D         DEC     L               
7C9A: B7         OR      A               
7C9B: 5B         LD      E,E             
7C9C: 7F         LD      A,A             
7C9D: 3D         DEC     A               
7C9E: 43         LD      B,E             
7C9F: 7D         LD      A,L             
7CA0: FF         RST     0X38            
7CA1: FF         RST     0X38            
7CA2: 00         NOP                     
7CA3: 00         NOP                     
7CA4: 01 00 93   LD      BC,$9300        
7CA7: 00         NOP                     
7CA8: 9B         SBC     E               
7CA9: 00         NOP                     
7CAA: 9B         SBC     E               
7CAB: 00         NOP                     
7CAC: 64         LD      H,H             
7CAD: 9B         SBC     E               
7CAE: FF         RST     0X38            
7CAF: FF         RST     0X38            
7CB0: FF         RST     0X38            
7CB1: F8 FF      LDHL    SP,$FF          
7CB3: F8 FF      LDHL    SP,$FF          
7CB5: F0 FF      LD      A,($FF)         
7CB7: F0 07      LD      A,($07)         
7CB9: F8 23      LDHL    SP,$23          
7CBB: DC 77 DA   CALL    C,$DA77         
7CBE: 7F         LD      A,A             
7CBF: E4         ???                     
7CC0: F8 17      LDHL    SP,$17          
7CC2: FC         ???                     
7CC3: 03         INC     BC              
7CC4: FE 01      CP      $01             
7CC6: BF         CP      A               
7CC7: 00         NOP                     
7CC8: FF         RST     0X38            
7CC9: 00         NOP                     
7CCA: 7F         LD      A,A             
7CCB: 00         NOP                     
7CCC: FD         ???                     
7CCD: 06 FD      LD      B,$FD           
7CCF: 8E         ADC     A,(HL)          
7CD0: 07         RLCA                    
7CD1: F1         POP     AF              
7CD2: 17         RLA                     
7CD3: E1         POP     HL              
7CD4: 27         DAA                     
7CD5: D1         POP     DE              
7CD6: FF         RST     0X38            
7CD7: 01 F7 01   LD      BC,$01F7        
7CDA: F7         RST     0X30            
7CDB: 01 FB 05   LD      BC,$05FB        
7CDE: 87         ADD     A,A             
7CDF: 79         LD      A,C             
7CE0: 04         INC     B               
7CE1: FF         RST     0X38            
7CE2: 06 FD      LD      B,$FD           
7CE4: 06 FD      LD      B,$FD           
7CE6: 06 FD      LD      B,$FD           
7CE8: 06 FD      LD      B,$FD           
7CEA: 06 FD      LD      B,$FD           
7CEC: 06 FD      LD      B,$FD           
7CEE: 04         INC     B               
7CEF: FF         RST     0X38            
7CF0: F0 FF      LD      A,($FF)         
7CF2: F0 FF      LD      A,($FF)         
7CF4: F0 FF      LD      A,($FF)         
7CF6: F0 FF      LD      A,($FF)         
7CF8: B0         OR      B               
7CF9: FF         RST     0X38            
7CFA: F0 FF      LD      A,($FF)         
7CFC: F0 FF      LD      A,($FF)         
7CFE: F0 FF      LD      A,($FF)         
7D00: C0         RET     NZ              
7D01: 80         ADD     A,B             
7D02: C0         RET     NZ              
7D03: 80         ADD     A,B             
7D04: C0         RET     NZ              
7D05: 81         ADD     A,C             
7D06: C3 83 C3   JP      $C383           
7D09: 83         ADD     A,E             
7D0A: CF         RST     0X08            
7D0B: 8F         ADC     A,A             
7D0C: CF         RST     0X08            
7D0D: 8F         ADC     A,A             
7D0E: DF         RST     0X18            
7D0F: 9F         SBC     A               
7D10: FF         RST     0X38            
7D11: F8 FE      LDHL    SP,$FE          
7D13: F0 F2      LD      A,($F2)         
7D15: FC         ???                     
7D16: E0 FF      LDFF00  ($FF),A         
7D18: FB         EI                      
7D19: FE FF      CP      $FF             
7D1B: FC         ???                     
7D1C: FF         RST     0X38            
7D1D: FC         ???                     
7D1E: FF         RST     0X38            
7D1F: FA 5F 1F   LD      A,($1F5F)       
7D22: 1F         RRA                     
7D23: 1F         RRA                     
7D24: 5F         LD      E,A             
7D25: 1F         RRA                     
7D26: BF         CP      A               
7D27: 3F         CCF                     
7D28: 3F         CCF                     
7D29: 3F         CCF                     
7D2A: 2F         CPL                     
7D2B: 27         DAA                     
7D2C: 3F         CCF                     
7D2D: 37         SCF                     
7D2E: 9F         SBC     A               
7D2F: 0F         RRCA                    
7D30: FF         RST     0X38            
7D31: FF         RST     0X38            
7D32: FF         RST     0X38            
7D33: F9         LD      SP,HL           
7D34: FF         RST     0X38            
7D35: FB         EI                      
7D36: FF         RST     0X38            
7D37: E7         RST     0X20            
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
7D48: F7         RST     0X30            
7D49: F7         RST     0X30            
7D4A: CE FF      ADC     $FF             
7D4C: 8F         ADC     A,A             
7D4D: FF         RST     0X38            
7D4E: 3F         CCF                     
7D4F: FF         RST     0X38            
7D50: FF         RST     0X38            
7D51: C7         RST     0X00            
7D52: FF         RST     0X38            
7D53: FF         RST     0X38            
7D54: FF         RST     0X38            
7D55: FF         RST     0X38            
7D56: FF         RST     0X38            
7D57: FF         RST     0X38            
7D58: FF         RST     0X38            
7D59: FF         RST     0X38            
7D5A: 7F         LD      A,A             
7D5B: FF         RST     0X38            
7D5C: 7F         LD      A,A             
7D5D: FF         RST     0X38            
7D5E: FF         RST     0X38            
7D5F: FF         RST     0X38            
7D60: FF         RST     0X38            
7D61: FD         ???                     
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
7D6C: CF         RST     0X08            
7D6D: FF         RST     0X38            
7D6E: 83         ADD     A,E             
7D6F: FF         RST     0X38            
7D70: F9         LD      SP,HL           
7D71: FE FC      CP      $FC             
7D73: FF         RST     0X38            
7D74: FE FF      CP      $FF             
7D76: FC         ???                     
7D77: FF         RST     0X38            
7D78: E5         PUSH    HL              
7D79: FE E5      CP      $E5             
7D7B: FE C4      CP      $C4             
7D7D: FE CD      CP      $CD             
7D7F: FE E7      CP      $E7             
7D81: 05         DEC     B               
7D82: 3E 81      LD      A,$81           
7D84: FE 03      CP      $03             
7D86: FE 07      CP      $07             
7D88: BF         CP      A               
7D89: 07         RLCA                    
7D8A: 76         HALT                    
7D8B: 0B         DEC     BC              
7D8C: E7         RST     0X20            
7D8D: 18 FF      JR      $7D8E           
7D8F: 0C         INC     C               
7D90: 01 FF 03   LD      BC,$03FF        
7D93: FD         ???                     
7D94: 01 FF 03   LD      BC,$03FF        
7D97: FD         ???                     
7D98: 07         RLCA                    
7D99: F9         LD      SP,HL           
7D9A: 8F         ADC     A,A             
7D9B: 71         LD      (HL),C          
7D9C: DF         RST     0X18            
7D9D: 29         ADD     HL,HL           
7D9E: FF         RST     0X38            
7D9F: 13         INC     DE              
7DA0: C0         RET     NZ              
7DA1: 3F         CCF                     
7DA2: E0 1F      LDFF00  ($1F),A         
7DA4: F1         POP     AF              
7DA5: 0F         RRCA                    
7DA6: FF         RST     0X38            
7DA7: 0F         RRCA                    
7DA8: FF         RST     0X38            
7DA9: 0F         RRCA                    
7DAA: F7         RST     0X30            
7DAB: 0F         RRCA                    
7DAC: F0 0F      LD      A,($0F)         
7DAE: F8 07      LDHL    SP,$07          
7DB0: 7F         LD      A,A             
7DB1: E3         ???                     
7DB2: FF         RST     0X38            
7DB3: D5         PUSH    DE              
7DB4: FF         RST     0X38            
7DB5: E3         ???                     
7DB6: E5         PUSH    HL              
7DB7: F1         POP     AF              
7DB8: CD E0 83   CALL    $83E0           
7DBB: C2 03 81   JP      NZ,$8103        
7DBE: 06 80      LD      B,$80           
7DC0: EE 07      XOR     $07             
7DC2: D8         RET     C               
7DC3: 03         INC     BC              
7DC4: 84         ADD     A,H             
7DC5: 03         INC     BC              
7DC6: 04         INC     B               
7DC7: 07         RLCA                    
7DC8: 0E 07      LD      C,$07           
7DCA: 9F         SBC     A               
7DCB: 0C         INC     C               
7DCC: FE 19      CP      $19             
7DCE: BE         CP      (HL)            
7DCF: 81         ADD     A,C             
7DD0: 03         INC     BC              
7DD1: FD         ???                     
7DD2: 07         RLCA                    
7DD3: F9         LD      SP,HL           
7DD4: 03         INC     BC              
7DD5: FD         ???                     
7DD6: 07         RLCA                    
7DD7: F9         LD      SP,HL           
7DD8: 07         RLCA                    
7DD9: F1         POP     AF              
7DDA: 07         RLCA                    
7DDB: E1         POP     HL              
7DDC: 07         RLCA                    
7DDD: F1         POP     AF              
7DDE: 07         RLCA                    
7DDF: E1         POP     HL              
7DE0: 05         DEC     B               
7DE1: FC         ???                     
7DE2: 05         DEC     B               
7DE3: FC         ???                     
7DE4: 05         DEC     B               
7DE5: FC         ???                     
7DE6: 05         DEC     B               
7DE7: FC         ???                     
7DE8: 05         DEC     B               
7DE9: FC         ???                     
7DEA: 05         DEC     B               
7DEB: FC         ???                     
7DEC: 07         RLCA                    
7DED: FC         ???                     
7DEE: 05         DEC     B               
7DEF: FC         ???                     
7DF0: 30 FF      JR      NC,$7DF1        
7DF2: 30 FF      JR      NC,$7DF3        
7DF4: 30 FF      JR      NC,$7DF5        
7DF6: B0         OR      B               
7DF7: FF         RST     0X38            
7DF8: 30 FF      JR      NC,$7DF9        
7DFA: 70         LD      (HL),B          
7DFB: FF         RST     0X38            
7DFC: 70         LD      (HL),B          
7DFD: FF         RST     0X38            
7DFE: 30 FF      JR      NC,$7DFF        
7E00: FF         RST     0X38            
7E01: BF         CP      A               
7E02: FF         RST     0X38            
7E03: BF         CP      A               
7E04: DF         RST     0X18            
7E05: 9F         SBC     A               
7E06: FD         ???                     
7E07: 8E         ADC     A,(HL)          
7E08: E8 97      ADD     SP,$97          
7E0A: D0         RET     NC              
7E0B: BF         CP      A               
7E0C: E0 BF      LDFF00  ($BF),A         
7E0E: E0 BF      LDFF00  ($BF),A         
7E10: FD         ???                     
7E11: FE FC      CP      $FC             
7E13: FE FB      CP      $FB             
7E15: FD         ???                     
7E16: 7F         LD      A,A             
7E17: F7         RST     0X30            
7E18: 7F         LD      A,A             
7E19: DF         RST     0X18            
7E1A: 3F         CCF                     
7E1B: FF         RST     0X38            
7E1C: 3F         CCF                     
7E1D: FF         RST     0X38            
7E1E: 7F         LD      A,A             
7E1F: FF         RST     0X38            
7E20: FF         RST     0X38            
7E21: 27         DAA                     
7E22: FF         RST     0X38            
7E23: 03         INC     BC              
7E24: C1         POP     BC              
7E25: 41         LD      B,C             
7E26: C1         POP     BC              
7E27: 80         ADD     A,B             
7E28: C2 81 C2   JP      NZ,$C281        
7E2B: C0         RET     NZ              
7E2C: F1         POP     AF              
7E2D: 80         ADD     A,B             
7E2E: B1         OR      C               
7E2F: C0         RET     NZ              
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
7E3B: 7F         LD      A,A             
7E3C: F0 3F      LD      A,($3F)         
7E3E: C0         RET     NZ              
7E3F: 3F         CCF                     
7E40: FF         RST     0X38            
7E41: FF         RST     0X38            
7E42: 2F         CPL                     
7E43: 00         NOP                     
7E44: D9         RETI                    
7E45: 26 D9      LD      H,$D9           
7E47: 26 FB      LD      H,$FB           
7E49: 04         INC     B               
7E4A: FB         EI                      
7E4B: 04         INC     B               
7E4C: 04         INC     B               
7E4D: FF         RST     0X38            
7E4E: FF         RST     0X38            
7E4F: FF         RST     0X38            
7E50: FF         RST     0X38            
7E51: FF         RST     0X38            
7E52: FF         RST     0X38            
7E53: FF         RST     0X38            
7E54: FF         RST     0X38            
7E55: FF         RST     0X38            
7E56: F9         LD      SP,HL           
7E57: FF         RST     0X38            
7E58: F8 FF      LDHL    SP,$FF          
7E5A: 70         LD      (HL),B          
7E5B: 7F         LD      A,A             
7E5C: F1         POP     AF              
7E5D: FF         RST     0X38            
7E5E: 33         INC     SP              
7E5F: 3F         CCF                     
7E60: 07         RLCA                    
7E61: FF         RST     0X38            
7E62: 0F         RRCA                    
7E63: FF         RST     0X38            
7E64: AF         XOR     A               
7E65: EF         RST     0X28            
7E66: FF         RST     0X38            
7E67: FF         RST     0X38            
7E68: 7F         LD      A,A             
7E69: FF         RST     0X38            
7E6A: FF         RST     0X38            
7E6B: FF         RST     0X38            
7E6C: EE ED      XOR     $ED             
7E6E: E0 FE      LDFF00  ($FE),A         
7E70: F9         LD      SP,HL           
7E71: EC         ???                     
7E72: E9         JP      (HL)            
7E73: DE F0      SBC     $F0             
7E75: FC         ???                     
7E76: C0         RET     NZ              
7E77: F9         LD      SP,HL           
7E78: E8 D1      ADD     SP,$D1          
7E7A: F8 81      LDHL    SP,$81          
7E7C: D9         RETI                    
7E7D: 06 B9      LD      B,$B9           
7E7F: 06 FF      LD      B,$FF           
7E81: 08 FE 0F   LD      ($0FFE),SP      
7E84: 1E F9      LD      E,$F9           
7E86: 1C         INC     E               
7E87: FF         RST     0X38            
7E88: 5C         LD      E,H             
7E89: BF         CP      A               
7E8A: BC         CP      H               
7E8B: 7F         LD      A,A             
7E8C: B8         CP      B               
7E8D: 5F         LD      E,A             
7E8E: 7C         LD      A,H             
7E8F: F7         RST     0X30            
7E90: 7F         LD      A,A             
7E91: BD         CP      L               
7E92: 7F         LD      A,A             
7E93: 7D         LD      A,L             
7E94: 7F         LD      A,A             
7E95: F9         LD      SP,HL           
7E96: 77         LD      (HL),A          
7E97: B1         OR      C               
7E98: 77         LD      (HL),A          
7E99: 81         ADD     A,C             
7E9A: 77         LD      (HL),A          
7E9B: 81         ADD     A,C             
7E9C: FF         RST     0X38            
7E9D: 01 FF 01   LD      BC,$01FF        
7EA0: 7C         LD      A,H             
7EA1: 03         INC     BC              
7EA2: FF         RST     0X38            
7EA3: 00         NOP                     
7EA4: AE         XOR     (HL)            
7EA5: 01 50 0B   LD      BC,$0B50        
7EA8: 00         NOP                     
7EA9: 87         ADD     A,A             
7EAA: 00         NOP                     
7EAB: 07         RLCA                    
7EAC: 00         NOP                     
7EAD: 0F         RRCA                    
7EAE: 00         NOP                     
7EAF: 9F         SBC     A               
7EB0: 0D         DEC     C               
7EB1: C0         RET     NZ              
7EB2: 2F         CPL                     
7EB3: 90         SUB     B               
7EB4: 1E E1      LD      E,$E1           
7EB6: 1F         RRA                     
7EB7: E0 3F      LDFF00  ($3F),A         
7EB9: C0         RET     NZ              
7EBA: 7E         LD      A,(HL)          
7EBB: 81         ADD     A,C             
7EBC: 3D         DEC     A               
7EBD: C2 77 8E   JP      NZ,$8E77        
7EC0: FF         RST     0X38            
7EC1: FF         RST     0X38            
7EC2: 00         NOP                     
7EC3: 00         NOP                     
7EC4: FF         RST     0X38            
7EC5: 00         NOP                     
7EC6: FF         RST     0X38            
7EC7: 00         NOP                     
7EC8: FF         RST     0X38            
7EC9: 00         NOP                     
7ECA: FF         RST     0X38            
7ECB: 00         NOP                     
7ECC: 00         NOP                     
7ECD: FF         RST     0X38            
7ECE: FF         RST     0X38            
7ECF: FF         RST     0X38            
7ED0: 07         RLCA                    
7ED1: E1         POP     HL              
7ED2: 07         RLCA                    
7ED3: C1         POP     BC              
7ED4: 0F         RRCA                    
7ED5: 81         ADD     A,C             
7ED6: 1F         RRA                     
7ED7: 01 3F 01   LD      BC,$013F        
7EDA: 7F         LD      A,A             
7EDB: 41         LD      B,C             
7EDC: 7F         LD      A,A             
7EDD: 01 FF 01   LD      BC,$01FF        
7EE0: FF         RST     0X38            
7EE1: FF         RST     0X38            
7EE2: 9D         SBC     L               
7EE3: 80         ADD     A,B             
7EE4: A2         AND     D               
7EE5: DD         ???                     
7EE6: A6         AND     (HL)            
7EE7: D9         RETI                    
7EE8: B7         OR      A               
7EE9: 88         ADC     A,B             
7EEA: B7         OR      A               
7EEB: 88         ADC     A,B             
7EEC: C0         RET     NZ              
7EED: BF         CP      A               
7EEE: FF         RST     0X38            
7EEF: FF         RST     0X38            
7EF0: FF         RST     0X38            
7EF1: FF         RST     0X38            
7EF2: 03         INC     BC              
7EF3: 01 C5 03   LD      BC,$03C5        
7EF6: ED         ???                     
7EF7: 03         INC     BC              
7EF8: FB         EI                      
7EF9: 07         RLCA                    
7EFA: ED         ???                     
7EFB: 03         INC     BC              
7EFC: 01 FF FF   LD      BC,$FFFF        
7EFF: FF         RST     0X38            
7F00: E8 BF      ADD     SP,$BF          
7F02: D8         RET     C               
7F03: 9F         SBC     A               
7F04: D7         RST     0X10            
7F05: 95         SUB     L               
7F06: FE BF      CP      $BF             
7F08: FF         RST     0X38            
7F09: BF         CP      A               
7F0A: DE 9F      SBC     $9F             
7F0C: C8         RET     Z               
7F0D: 9F         SBC     A               
7F0E: C0         RET     NZ              
7F0F: 9F         SBC     A               
7F10: 3F         CCF                     
7F11: FF         RST     0X38            
7F12: 3F         CCF                     
7F13: DF         RST     0X18            
7F14: 6E         LD      L,(HL)          
7F15: BF         CP      A               
7F16: 5F         LD      E,A             
7F17: FF         RST     0X38            
7F18: FF         RST     0X38            
7F19: FF         RST     0X38            
7F1A: 1F         RRA                     
7F1B: FF         RST     0X38            
7F1C: 0F         RRCA                    
7F1D: FF         RST     0X38            
7F1E: 1F         RRA                     
7F1F: FF         RST     0X38            
7F20: 33         INC     SP              
7F21: C0         RET     NZ              
7F22: 3F         CCF                     
7F23: C0         RET     NZ              
7F24: 3C         INC     A               
7F25: C0         RET     NZ              
7F26: 88         ADC     A,B             
7F27: F0 C0      LD      A,($C0)         
7F29: F8 E1      LDHL    SP,$E1          
7F2B: FC         ???                     
7F2C: F3         DI                      
7F2D: FC         ???                     
7F2E: EF         RST     0X28            
7F2F: F8 80      LDHL    SP,$80          
7F31: 7F         LD      A,A             
7F32: 80         ADD     A,B             
7F33: 7F         LD      A,A             
7F34: 00         NOP                     
7F35: 7F         LD      A,A             
7F36: 00         NOP                     
7F37: 3E A0      LD      A,$A0           
7F39: 1C         INC     E               
7F3A: 60         LD      H,B             
7F3B: 00         NOP                     
7F3C: C0         RET     NZ              
7F3D: 20 C5      JR      NZ,$7F04        
7F3F: 24         INC     H               
7F40: E1         POP     HL              
7F41: FF         RST     0X38            
7F42: 00         NOP                     
7F43: FF         RST     0X38            
7F44: 01 FF 00   LD      BC,$00FF        
7F47: FF         RST     0X38            
7F48: 00         NOP                     
7F49: FF         RST     0X38            
7F4A: 00         NOP                     
7F4B: 7F         LD      A,A             
7F4C: 80         ADD     A,B             
7F4D: 3B         DEC     SP              
7F4E: 60         LD      H,B             
7F4F: 01 3F 3F   LD      BC,$3F3F        
7F52: FB         EI                      
7F53: FF         RST     0X38            
7F54: 81         ADD     A,C             
7F55: F8 02      LDHL    SP,$02          
7F57: FC         ???                     
7F58: 07         RLCA                    
7F59: F8 02      LDHL    SP,$02          
7F5B: FC         ???                     
7F5C: 06 F8      LD      B,$F8           
7F5E: 06 F1      LD      B,$F1           
7F60: 80         ADD     A,B             
7F61: FF         RST     0X38            
7F62: 00         NOP                     
7F63: FE 00      CP      $00             
7F65: FF         RST     0X38            
7F66: 00         NOP                     
7F67: FE 00      CP      $00             
7F69: 7C         LD      A,H             
7F6A: 40         LD      B,B             
7F6B: 3C         INC     A               
7F6C: C0         RET     NZ              
7F6D: 3E 00      LD      A,$00           
7F6F: FF         RST     0X38            
7F70: 70         LD      (HL),B          
7F71: 0E 40      LD      C,$40           
7F73: 1F         RRA                     
7F74: 03         INC     BC              
7F75: BD         CP      L               
7F76: 03         INC     BC              
7F77: 1F         RRA                     
7F78: 07         RLCA                    
7F79: 3E 0F      LD      A,$0F           
7F7B: 3C         INC     A               
7F7C: 3F         CCF                     
7F7D: 7C         LD      A,H             
7F7E: 7F         LD      A,A             
7F7F: F8 7C      LDHL    SP,$7C          
7F81: FF         RST     0X38            
7F82: FD         ???                     
7F83: F2         ???                     
7F84: BF         CP      A               
7F85: E4         ???                     
7F86: DF         RST     0X18            
7F87: 60         LD      H,B             
7F88: FF         RST     0X38            
7F89: 00         NOP                     
7F8A: FC         ???                     
7F8B: 03         INC     BC              
7F8C: F8 07      LDHL    SP,$07          
7F8E: F8 17      LDHL    SP,$17          
7F90: 73         LD      (HL),E          
7F91: 05         DEC     B               
7F92: 73         LD      (HL),E          
7F93: 05         DEC     B               
7F94: 7F         LD      A,A             
7F95: 01 F7 09   LD      BC,$09F7        
7F98: 07         RLCA                    
7F99: F1         POP     AF              
7F9A: 07         RLCA                    
7F9B: F9         LD      SP,HL           
7F9C: 07         RLCA                    
7F9D: F1         POP     AF              
7F9E: 07         RLCA                    
7F9F: F9         LD      SP,HL           
7FA0: 00         NOP                     
7FA1: FF         RST     0X38            
7FA2: 11 EE 3F   LD      DE,$3FEE        
7FA5: C0         RET     NZ              
7FA6: FF         RST     0X38            
7FA7: 40         LD      B,B             
7FA8: FE 80      CP      $80             
7FAA: FD         ???                     
7FAB: 82         ADD     A,D             
7FAC: FF         RST     0X38            
7FAD: 40         LD      B,B             
7FAE: FF         RST     0X38            
7FAF: FF         RST     0X38            
7FB0: E8 1F      ADD     SP,$1F          
7FB2: F3         DI                      
7FB3: 1E FF      LD      E,$FF           
7FB5: 3C         INC     A               
7FB6: FC         ???                     
7FB7: 7C         LD      A,H             
7FB8: 78         LD      A,B             
7FB9: 78         LD      A,B             
7FBA: FF         RST     0X38            
7FBB: 30 FF      JR      NC,$7FBC        
7FBD: 00         NOP                     
7FBE: FF         RST     0X38            
7FBF: FF         RST     0X38            
7FC0: FF         RST     0X38            
7FC1: 1C         INC     E               
7FC2: FF         RST     0X38            
7FC3: 7C         LD      A,H             
7FC4: FF         RST     0X38            
7FC5: 78         LD      A,B             
7FC6: 3F         CCF                     
7FC7: 30 0F      JR      NC,$7FD8        
7FC9: 00         NOP                     
7FCA: FF         RST     0X38            
7FCB: 00         NOP                     
7FCC: FF         RST     0X38            
7FCD: 00         NOP                     
7FCE: FF         RST     0X38            
7FCF: FF         RST     0X38            
7FD0: 7F         LD      A,A             
7FD1: 01 D7 11   LD      BC,$11D7        
7FD4: E7         RST     0X20            
7FD5: 25         DEC     H               
7FD6: FF         RST     0X38            
7FD7: 79         LD      A,C             
7FD8: FF         RST     0X38            
7FD9: F9         LD      SP,HL           
7FDA: FF         RST     0X38            
7FDB: F1         POP     AF              
7FDC: FF         RST     0X38            
7FDD: 63         LD      H,E             
7FDE: FE FF      CP      $FF             
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
7FF0: 00         NOP                     
7FF1: FF         RST     0X38            
7FF2: 00         NOP                     
7FF3: FF         RST     0X38            
7FF4: 00         NOP                     
7FF5: FF         RST     0X38            
7FF6: 00         NOP                     
7FF7: FF         RST     0X38            
7FF8: 00         NOP                     
7FF9: FF         RST     0X38            
7FFA: 00         NOP                     
7FFB: FF         RST     0X38            
7FFC: 00         NOP                     
7FFD: FF         RST     0X38            
7FFE: 00         NOP                     
7FFF: FF         RST     0X38            
```
